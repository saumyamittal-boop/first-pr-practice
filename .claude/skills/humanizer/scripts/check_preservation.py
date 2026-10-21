#!/usr/bin/env python3
"""Check that a revised document kept everything the original had.

Compares an original and a revised text and reports anything that went
missing: in-text citations, numbers, technical terms (acronyms and terms
like ATR-14), and sentences. Use it after rewriting an academic paper,
where every concept, citation and sentence has to survive.

Usage:
    python3 check_preservation.py original.docx revised.docx
    python3 check_preservation.py original.txt revised.txt --stop-at References

Inputs can be .docx (body text is extracted, tables included) or plain
text. By default the comparison stops at a paragraph that is exactly
"References" so the reference list itself is not compared; change that
with --stop-at, or pass --stop-at "" to compare everything.

Exit code is 0 when nothing is missing and 1 otherwise. New items that
appear only in the revision are listed too, so invented numbers or
citations get a second look.
"""

import argparse
import re
import sys
import zipfile
from collections import Counter
from xml.etree import ElementTree

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# A surname: capitalised word that may contain accented letters, hyphens or an apostrophe.
SURNAME = r"(?:van der |van |de |del |von )?[A-ZÀ-ÖØ-ÞĀ-ɏ][\wÀ-ɏ'’\-]+"
YEAR = r"(?:19|20)\d\d[a-z]?"

# "Author (2020)", "Author and Author (2020)", "Author et al. (2020)", "Author et al.'s (2020)"
NARRATIVE = re.compile(
    rf"({SURNAME})(?:\s+(?:and|&)\s+{SURNAME}|\s+et al\.)?(?:['’]s)?\s+\(({YEAR})\)"
)
# One part of a parenthetical citation: "Author, 2020", "Author & Author, 2020", "Author et al., 2020"
PAREN_PART = re.compile(
    rf"({SURNAME})(?:\s+(?:and|&)\s+{SURNAME}|\s+et al\.)?,\s+({YEAR})"
)
ABBREVIATIONS = ("et al.", "e.g.", "i.e.", "vs.", "cf.", "etc.", "Fig.", "No.", "approx.")


def read_paragraphs(path):
    if path.lower().endswith(".docx"):
        with zipfile.ZipFile(path) as z:
            root = ElementTree.fromstring(z.read("word/document.xml"))
        paras = []
        for p in root.iter(W + "p"):
            text = "".join(t.text or "" for t in p.iter(W + "t"))
            if text.strip():
                paras.append(" ".join(text.split()))
        return paras
    with open(path, encoding="utf-8") as f:
        return [" ".join(line.split()) for line in f if line.strip()]


def cut_at(paras, stop):
    if not stop:
        return paras
    for i, p in enumerate(paras):
        if p.strip() == stop:
            return paras[:i]
    return paras


def citations(text):
    found = Counter()
    for surname, year in NARRATIVE.findall(text):
        found[f"{surname} {year}"] += 1
    for group in re.findall(r"\(([^()]*(?:19|20)\d\d[^()]*)\)", text):
        for part in group.split(";"):
            for surname, year in PAREN_PART.findall(part):
                found[f"{surname} {year}"] += 1
    return found


def numbers(text):
    # Keep signs, decimals and percent signs; drop numbers that are part of a citation year or a word.
    cleaned = PAREN_PART.sub(" ", text)
    cleaned = NARRATIVE.sub(" ", cleaned)
    found = re.findall(r"(?<![\w.])[-+−]?\d[\d,]*(?:\.\d+)?%?(?![\w])", cleaned)
    return Counter(n.replace("−", "-").replace(",", "") for n in found)


def terms(text):
    # Acronyms and technical tokens: RMSE, NIFTY, ATR-14, XGBoost, BB_pctB, MACD_Signal.
    found = re.findall(r"\b(?:[A-Z]+[-_][A-Za-z0-9]+|[A-Za-z]+_[A-Za-z0-9]+|[A-Z][A-Za-z]*[A-Z][A-Za-z0-9]*)\b", text)
    return Counter(found)


def sentences(paragraph):
    protected = paragraph
    for i, abbr in enumerate(ABBREVIATIONS):
        protected = protected.replace(abbr, f"\u0000{i}\u0000")
    parts = re.split(r"(?<=[.?!])[\"”’)]?\s+(?=[A-Z0-9(\"“])", protected)
    return [p for p in parts if p.strip()]


def missing(before, after):
    return {k: before[k] - after.get(k, 0) for k in before if before[k] > after.get(k, 0)}


def added(before, after):
    return {k: after[k] - before.get(k, 0) for k in after if after[k] > before.get(k, 0)}


def show(title, items, limit=40):
    if not items:
        return
    print(f"  {title}:")
    for k, n in sorted(items.items())[:limit]:
        print(f"    {k}" + (f"  (x{n})" if n > 1 else ""))
    if len(items) > limit:
        print(f"    ... and {len(items) - limit} more")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("original")
    ap.add_argument("revised")
    ap.add_argument("--stop-at", default="References", help='paragraph text that ends the comparison (default "References")')
    args = ap.parse_args()

    old = cut_at(read_paragraphs(args.original), args.stop_at)
    new = cut_at(read_paragraphs(args.revised), args.stop_at)
    old_text, new_text = "\n".join(old), "\n".join(new)

    problems = 0
    # Citations and numbers are counted per occurrence, since each occurrence backs a different claim.
    # Terms only need to survive somewhere: rewording "LSTM" as "the recurrent model" once is fine.
    checks = [
        ("In-text citations", citations(old_text), citations(new_text), True),
        ("Numbers", numbers(old_text), numbers(new_text), True),
        ("Technical terms", terms(old_text), terms(new_text), False),
    ]
    for name, before, after, per_occurrence in checks:
        if per_occurrence:
            gone, extra = missing(before, after), added(before, after)
        else:
            gone = {k: 1 for k in before if k not in after}
            extra = {k: 1 for k in after if k not in before}
        status = "OK" if not gone else "MISSING"
        print(f"{name}: {sum(before.values())} before, {sum(after.values())} after  [{status}]")
        show("missing from the revision", gone)
        show("new in the revision (check these are real)", extra, limit=15)
        problems += bool(gone)

    old_sentences = sum(len(sentences(p)) for p in old)
    new_sentences = sum(len(sentences(p)) for p in new)
    status = "OK" if new_sentences >= old_sentences else "FEWER"
    print(f"Sentences: {old_sentences} before, {new_sentences} after  [{status}]")
    print(f"Paragraphs: {len(old)} before, {len(new)} after")
    if new_sentences < old_sentences:
        problems += 1
        if len(old) == len(new):
            for i, (a, b) in enumerate(zip(old, new)):
                if len(sentences(b)) < len(sentences(a)):
                    print(f"    paragraph {i + 1} lost {len(sentences(a)) - len(sentences(b))} sentence(s): {a[:70]}...")

    print("PASS" if not problems else "CHECK: something from the original is missing in the revision")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
