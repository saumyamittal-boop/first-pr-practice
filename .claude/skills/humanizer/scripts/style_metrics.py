#!/usr/bin/env python3
"""Score prose on features that research ties to LLM-written academic text.

Prints one column per input file, so an original and its revision can be
compared side by side. The features and their sources are described in
references/academic-papers.md:

  trailing ", ...ing" clauses   Reinhart et al. (2025): 2-5x the human rate in LLM text
  nominalizations               Reinhart et al. (2025); Herbold et al. (2023)
  subordinators                 Liu & Liu (2025): humans use more dependent clauses
  hedges and modals             Herbold et al. (2023); Jiang & Hyland (2025)
  numbers                       unflagged prose in one Turnitin report carried more of them
  sentence-length spread        Liu & Liu (2025); Munoz-Ortiz et al. (2024)
  marker words                  Kobak et al. (2025); Reinhart et al. (2025)

Usage:
    python3 style_metrics.py original.docx revised.docx
    python3 style_metrics.py draft.txt

Inputs can be .docx or plain text. Only running prose is scored: lines
under 15 words (headings, captions, table cells, equations) are skipped,
and scoring stops at a paragraph that is exactly "References". The
numbers are rates per 1,000 words, meant for comparing two versions of
the same text, not for judging a text on its own.
"""

import re
import statistics
import sys
import zipfile
from xml.etree import ElementTree

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
MARKERS = (r"delve|delves|delving|underscore|underscores|underscoring|showcase|showcases|showcasing|intricate|"
           r"pivotal|crucial|comprehensive|realm|tapestry|amidst|notably|particularly|additionally|"
           r"enhance|enhances|enhancing|insights?|landscape|seamless|seamlessly|meticulous|interplay")
SUBORDINATORS = r"because|although|though|while|whereas|since|unless|if|when|which|whether"
HEDGES = r"may|might|could|would|can|should|likely|probably|possibly|appears?|seems?|suggests?|perhaps"
NOT_PARTICIPLES = r"including|according|following|during|being|regarding|concerning|notwithstanding"


def paragraphs(path):
    if path.lower().endswith(".docx"):
        with zipfile.ZipFile(path) as z:
            root = ElementTree.fromstring(z.read("word/document.xml"))
        lines = ["".join(t.text or "" for t in p.iter(W + "t")) for p in root.iter(W + "p")]
    else:
        with open(path, encoding="utf-8") as f:
            lines = f.read().split("\n")
    lines = [" ".join(l.split()) for l in lines]
    if "References" in lines:
        lines = lines[:lines.index("References")]
    return [l for l in lines if len(l.split()) >= 15 and not re.match(r"^(Table|Figure) \d+:", l)]


def sentences(paragraph):
    protected = re.sub(r"\b(et al|e\.g|i\.e|vs|cf|Fig)\.", lambda m: m.group(1) + "<dot>", paragraph)
    return [s for s in re.split(r"(?<=[.?!])\s+(?=[A-Z0-9(\"])", protected) if s.strip()]


def score(path):
    paras = paragraphs(path)
    text = " ".join(paras)
    n = len(re.findall(r"[A-Za-z][A-Za-z'\-]*", text)) or 1
    lengths = [len(s.split()) for p in paras for s in sentences(p)] or [0]
    per_k = lambda pattern: round(1000 * len(re.findall(pattern, text, flags=re.I)) / n, 2)
    return {
        "words": n,
        "sentences": len(lengths),
        "mean sentence length": round(statistics.mean(lengths), 1),
        "sentence length spread (sd)": round(statistics.pstdev(lengths), 1),
        "sentences under 12 words %": round(100 * sum(l < 12 for l in lengths) / len(lengths), 1),
        "sentences over 35 words %": round(100 * sum(l > 35 for l in lengths) / len(lengths), 1),
        'trailing ", ...ing" /1k': per_k(rf", (?!(?:{NOT_PARTICIPLES})\b)[a-z]+ing\b"),
        "nominalizations /1k": per_k(r"\b[a-z]+(?:tion|tions|ment|ments|ness|ance|ances|ence|ences|ity|ities)\b"),
        "subordinators /1k": per_k(rf"\b(?:{SUBORDINATORS})\b"),
        "hedges and modals /1k": per_k(rf"\b(?:{HEDGES})\b"),
        "numbers /1k": round(1000 * len(re.findall(r"(?<![\w.])[-+]?\d[\d,]*(?:\.\d+)?%?", text)) / n, 1),
        "marker words /1k": per_k(rf"\b(?:{MARKERS})\b"),
    }


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    rows = {path: score(path) for path in sys.argv[1:]}
    names = [p.rsplit("/", 1)[-1] for p in rows]
    if len(set(names)) < len(names):  # same file name in different folders: show the folder too
        names = ["/".join(p.rsplit("/", 2)[-2:]) for p in rows]
    names = [n[-18:] for n in names]
    metrics = list(next(iter(rows.values())))
    print(f"{'':30s}" + "".join(f"{n:>20s}" for n in names))
    for m in metrics:
        print(f"{m:30s}" + "".join(f"{rows[p][m]:>20}" for p in rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
