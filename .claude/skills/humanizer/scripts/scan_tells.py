#!/usr/bin/env python3
"""Flag signs of AI-generated writing in a piece of text.

Usage:
    python3 scan_tells.py FILE [FILE ...]
    python3 scan_tells.py < draft.txt
    python3 scan_tells.py --summary FILE

The patterns come from Wikipedia's "Signs of AI writing" field guide.
Each hit is marked "fix" (almost always a tell) or "check" (depends on
context). Fenced code blocks and inline code spans are skipped.

Exit status is 1 if any "fix" hit is found, otherwise 0.
"""

import argparse
import re
import sys
from collections import Counter

ADVICE = {
    "punctuation": "Use a comma, colon, period or parentheses. Use straight quotes.",
    "ai vocabulary": "Say it plainly. Rewrite the sentence instead of swapping in a synonym.",
    "significance": "Drop the claim about importance or legacy and give the specific fact.",
    "puffery": "Cut the promotional wording. State the plain fact or delete it.",
    "copula avoidance": "Try plain 'is', 'are' or 'has'.",
    "notability": "Say what the source said, not where it was covered.",
    "-ing tail": "Delete the trailing analysis, or make it a sentence with a real fact.",
    "vague link": "State the actual relationship (worked at, founded, taught).",
    "vague attribution": "Name the source or drop the claim.",
    "challenges formula": "Drop the 'despite challenges / future outlook' formula.",
    "negative parallelism": "Make the point directly, without the 'not X but Y' setup.",
    "didactic / summary": "Delete it. Don't lecture or recap.",
    "chat filler": "Delete it. Start with the answer and stop when done.",
    "disclaimer": "Delete it, or say plainly what you don't know.",
    "refusal": "Delete it.",
    "placeholder": "Fill in the real value or remove it.",
    "tool residue": "Remove the leftover chatbot markup.",
    "formatting": "Use plain sentences or plain list items. No bold labels, emoji or title case.",
    "rule of three": "Check that every item in the group of three earns its place.",
}

RULES = []


def rule(severity, category, pattern, case_sensitive=False):
    flags = 0 if case_sensitive else re.IGNORECASE
    RULES.append((severity, category, re.compile(pattern, flags)))


# Punctuation (checked against the original text, before quote normalizing).
PUNCT_RULES = [
    ("fix", "punctuation", re.compile("—")),           # em dash
    ("fix", "punctuation", re.compile(r"\s–\s")),      # spaced en dash
    ("fix", "punctuation", re.compile(r"\w\s--\s\w")),      # double hyphen dash
    ("fix", "punctuation", re.compile("[‘’“”]")),  # curly quotes
    ("fix", "punctuation", re.compile("↩")),           # footnote return arrow
]

# AI vocabulary.
rule("fix", "ai vocabulary", r"(^|[.!?]\s+)additionally\b")
rule("fix", "ai vocabulary", r"\balign(s|ed|ing)? with\b")
rule("fix", "ai vocabulary", r"\bboast(s|ed|ing)?\b")
rule("fix", "ai vocabulary", r"\bbolster(s|ed|ing)?\b")
rule("fix", "ai vocabulary", r"\bcrucial(ly)?\b")
rule("fix", "ai vocabulary", r"\bdeep(er)?[- ]dives?\b")
rule("fix", "ai vocabulary", r"\bdelv(e|es|ed|ing)\b")
rule("fix", "ai vocabulary", r"\bemphasi[sz](e|es|ed|ing)\b")
rule("fix", "ai vocabulary", r"\benduring\b")
rule("fix", "ai vocabulary", r"\benhanc(e|es|ed|ing|ement|ements)\b")
rule("fix", "ai vocabulary", r"\bfoster(s|ed|ing)?\b")
rule("fix", "ai vocabulary", r"\bgarner(s|ed|ing)?\b")
rule("fix", "ai vocabulary", r"\bhighlighting\b")
rule("check", "ai vocabulary", r"\bhighlighted\b")
rule("check", "ai vocabulary", r"\bhighlights?\b")
rule("fix", "ai vocabulary", r"\binterplay\b")
rule("fix", "ai vocabulary", r"\bintrica(te|cies|cy)\b")
rule("check", "ai vocabulary", r"\bkey\b")
rule("check", "ai vocabulary", r"\blandscapes?\b")
rule("fix", "ai vocabulary", r"\bmeticulous(ly)?\b")
rule("fix", "ai vocabulary", r"\bpivotal\b")
rule("check", "ai vocabulary", r"\brobust(ly|ness)?\b")
rule("fix", "ai vocabulary", r"\bshowcas(e|es|ed|ing)\b")
rule("fix", "ai vocabulary", r"\btapestr(y|ies)\b")
rule("fix", "ai vocabulary", r"\btestament\b")
rule("fix", "ai vocabulary", r"\bunderscor(es|ed|ing)\b")
rule("check", "ai vocabulary", r"\bunderscore\b")
rule("fix", "ai vocabulary", r"\bvaluable insights?\b")
rule("check", "ai vocabulary", r"\bvaluable\b")
rule("fix", "ai vocabulary", r"\bvibrant\b")
rule("fix", "ai vocabulary", r"\bresonat(e|es|ed|ing) with\b")

# Significance, legacy, broader trends.
rule("fix", "significance", r"\bstand(s|ing)? as an?\b")
rule("fix", "significance", r"\bserv(e|es|ed|ing) as an?\b")
rule("fix", "significance", r"\bplay(s|ed|ing)? an? (crucial|pivotal|vital|key|significant|important|central|major) role\b")
rule("fix", "significance", r"\bmark(s|ed|ing)? an? (pivotal|significant|key|major|new|turning|important)\b")
rule("fix", "significance", r"\brepresent(s|ed|ing)? an? (significant |major |pivotal |key )?shift\b")
rule("fix", "significance", r"\breflect(s|ed|ing)? (the )?broader\b")
rule("fix", "significance", r"\b(enduring|lasting|ongoing) (legacy|influence|relevance|impact|significance)\b")
rule("fix", "significance", r"\bset(s|ting)? the stage\b")
rule("fix", "significance", r"\bever[- ]?evolving\b|\bevolving landscape\b")
rule("fix", "significance", r"\bfocal point\b|\bindelible mark\b|\bdeeply rooted\b|\bturning point\b")
rule("fix", "significance", r"\bbroader (context|trends?|movement|history|reflection|debates?)\b")
rule("fix", "significance", r"\b(generated|sparked|prompted|fueled) (debate|discussions?|reflection)\b")
rule("check", "significance", r"\b(importance|significance)\b")

# Promotional language.
rule("fix", "puffery", r"\bnestled\b|\bin the heart of\b|\bbreathtaking\b|\bgroundbreaking\b")
rule("fix", "puffery", r"\brenowned\b|\bdiverse (array|range|tapestry)\b|\bnatural beauty\b")
rule("fix", "puffery", r"\brich (cultural )?(heritage|history|tradition|culture|tapestry)\b")
rule("fix", "puffery", r"\bcommitment to\b|\bseamless(ly)?\b|\bexemplif(y|ies|ied)\b")
rule("fix", "puffery", r"\b(game[- ]changer|cutting[- ]edge|world[- ]class|state[- ]of[- ]the[- ]art)\b")

# Copula avoidance.
rule("check", "copula avoidance", r"\b(functions|operates|acts) as an?\b")
rule("check", "copula avoidance", r"\brefers? to\b")
rule("check", "copula avoidance", r"\b(features|offers|maintains) an?\b")

# Notability and media coverage.
rule("fix", "notability", r"\b(featured|profiled) in\b")
rule("fix", "notability", r"\bindependent coverage\b|\btrade publications\b|\bmedia outlets\b")
rule("fix", "notability", r"\b(active|strong) (social media|digital|online) presence\b")
rule("check", "notability", r"\b(local|regional|national|international) (media|press) coverage\b")

# Superficial "-ing" tail.
rule("fix", "-ing tail", r",\s+(highlighting|underscoring|emphasi[sz]ing|reflecting|symboli[sz]ing|showcasing|ensuring|contributing to|fostering|cultivating|enhancing|solidifying|reinforcing|demonstrating|illustrating|cementing|embodying|signall?ing|making it a|creating a)\b")

# Vague connection.
rule("check", "vague link", r"\b(associated|connected) (with|to)\b|\bin connection (with|to)\b")

# Vague attribution.
rule("fix", "vague attribution", r"\b(experts|observers|critics|scholars|analysts|researchers|commentators)\s+(have\s+)?(argue|argued|say|said|note|noted|suggest|suggested|believe|agree|cited|claim|claimed)\b")
rule("fix", "vague attribution", r"\bindustry reports\b|\bsome critics\b|\baccording to (some|many|several|various)\b")
rule("check", "vague attribution", r"\bwidely (regarded|considered|seen|recognized|recognised)\b")
rule("check", "vague attribution", r"\b(several|many|various|numerous) (sources|publications|reviewers|scholars|outlets)\b")

# Challenges formula.
rule("fix", "challenges formula", r"\bfac(e|es|ed|ing) (several |many |numerous |significant |a number of |various )?challenges\b")
rule("fix", "challenges formula", r"\bdespite (these|the|its|their) challenges\b|\bcontinues? to thrive\b")
rule("fix", "challenges formula", r"\bfuture (outlook|prospects|directions)\b|\bchallenges and (legacy|opportunities|future)\b")
rule("check", "challenges formula", r"\bdespite (its|their|his|her)\b")

# Negative parallelism.
rule("fix", "negative parallelism", r"\bnot only\b")
rule("fix", "negative parallelism", r"\bnot (just|merely|simply)\b")
rule("fix", "negative parallelism", r"\b(isn't|is not|wasn't|was not|aren't|are not|doesn't|does not|don't|do not) (just|merely|simply)\b")
rule("fix", "negative parallelism", r"\bit's not\b[^.;!?]{1,60}[,;:]\s*(it's|it is)\b")
rule("fix", "negative parallelism", r"\bno \w+, no \w+,? (just|only)\b")
rule("check", "negative parallelism", r"\brather than\b")

# Didactic disclaimers and recaps.
rule("fix", "didactic / summary", r"\b(important|crucial|critical|essential|vital) to (note|remember|consider|understand|recognize|recognise)\b")
rule("fix", "didactic / summary", r"\bworth noting\b|\bmay vary\b")
rule("fix", "didactic / summary", r"(^|[.!?]\s+)(in summary|in conclusion|to sum up|to summarize|to summarise|overall|ultimately),")
rule("fix", "didactic / summary", r"^\s*(#+\s*)?(\*\*)?(conclusion|key takeaways?)\b")

# Chat filler.
rule("fix", "chat filler", r"\bgreat question\b|\bof course!|\bcertainly!|\babsolutely right\b")
rule("fix", "chat filler", r"\b(i )?hope (this|that) helps\b|\blet me know\b|\bis there anything else\b")
rule("fix", "chat filler", r"\bwould you like (me )?to\b|\bif you'd like\b|\bfeel free to\b|\b(happy|glad) to help\b|\bi'd be happy to\b")
rule("fix", "chat filler", r"\bhere(?:'s| is) (a|an|your)\b")
rule("fix", "chat filler", r"\bin this (article|section|guide|post),? (we|i) will\b")
rule("fix", "chat filler", r"\bhope this (message|email) finds you well\b|\bi am writing to\b")

# Disclaimers.
rule("fix", "disclaimer", r"\bas of my (last|latest) (knowledge|training)? ?(update|cutoff)\b|\bknowledge cutoff\b")
rule("fix", "disclaimer", r"\bbased on (the )?available information\b|\bin the provided (sources|search results|text)\b")
rule("fix", "disclaimer", r"\b(not|isn't|aren't) (widely|extensively|publicly) (documented|available|disclosed|transcribed)\b")
rule("fix", "disclaimer", r"\b(details|information) (is|are) (limited|scarce)\b|\bmaintains a low profile\b")
rule("fix", "disclaimer", r"\bshould be treated as\b")

# Refusals.
rule("fix", "refusal", r"\bas an ai\b|\bas a (large )?language model\b")

# Placeholders.
rule("fix", "placeholder", r"\[(your|insert|add|describe|link to|name of|specific|company|date)\b[^\]]{0,60}\]")
rule("fix", "placeholder", r"\b20\d\d-(XX|xx)-(XX|xx)\b|\b(PASTE|INSERT)_[A-Z_]+|\(add [^)]{0,40}here\)")

# Tool residue.
rule("fix", "tool residue", r"oaicite|oai_citation|contentReference|attributableIndex|turn\d+(search|image|news|file)\d+")
rule("fix", "tool residue", r"\[cite: ?\d|\((start|end)_span\)|grok[-_]card|grok_render_citation_card_json")
rule("fix", "tool residue", "【\\d+†|\\[(attached_file|web):\\d+\\]|ppl-ai-file-upload|:::writing")
rule("fix", "tool residue", r"utm_source=(chatgpt\.com|openai|copilot\.com)|referrer=grok\.com|```wikitext")

# Formatting.
rule("fix", "formatting", r"^\s*(?:[-*+•–]|\d+[.)])\s+(\*\*|__)[^*_]{1,80}?(\*\*|__)\s*:?")
rule("fix", "formatting", r"^\s*\*\*[^*]{1,60}:\*\*")
rule("check", "formatting", r"^\s*(?:[-*+•–]|\d+[.)])\s+[A-Z][\w &/'()-]{1,40}:\s")
rule("fix", "formatting", "[\U0001F300-\U0001FAFF\U0001F000-\U0001F2FF☀-➿⭐✅]")
rule("check", "formatting", r"^\s*(---|\*\*\*|___|-{4,})\s*$")
rule("fix", "formatting", r"\bawards and recognition\b")

# Rule of three ("X, Y, and Z" with short items).
rule("check", "rule of three", r"\b\w+(?: \w+)?, \w+(?: \w+)?,? (?:and|or) \w+(?: \w+)?\b")

SMALL_WORDS = {
    "a", "an", "the", "and", "or", "but", "for", "nor", "of", "on", "in", "to",
    "at", "by", "with", "from", "as", "vs", "via", "into", "over", "per",
}


def is_title_case(text):
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    big = [w for w in words if w.lower() not in SMALL_WORDS]
    return len(big) >= 3 and all(w[0].isupper() for w in big)


def blank_inline_code(line):
    return re.sub(r"`[^`]*`", lambda m: " " * len(m.group()), line)


def scan(text):
    hits = []
    in_fence = False
    words = 0
    bold_spans = 0
    for lineno, raw in enumerate(text.splitlines(), 1):
        if re.match(r"^\s*(```|~~~)", raw):
            # An opening fence of ```wikitext is itself a tell.
            if not in_fence and re.match(r"^\s*```wikitext", raw):
                hits.append((lineno, "fix", "tool residue", raw.strip()))
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = blank_inline_code(raw)
        words += len(line.split())
        bold_spans += len(re.findall(r"\*\*[^*]+\*\*|__[^_]+__", line))

        for severity, category, pattern in PUNCT_RULES:
            for m in pattern.finditer(line):
                hits.append((lineno, severity, category, m.group().strip() or repr(m.group())))

        normalized = line.replace("’", "'").replace("‘", "'")
        normalized = normalized.replace("“", '"').replace("”", '"')
        for severity, category, pattern in RULES:
            for m in pattern.finditer(normalized):
                hits.append((lineno, severity, category, m.group().strip()))

        heading = re.match(r"^\s*#{1,6}\s+(.*)$", line)
        if heading and is_title_case(heading.group(1)):
            hits.append((lineno, "fix", "formatting", "Title Case heading: " + heading.group(1).strip()))

    # Drop weaker duplicates: a "check" hit on the same line and text as a "fix" hit.
    fixed = {(n, t.lower()) for n, s, c, t in hits if s == "fix"}
    hits = [h for h in hits if not (h[1] == "check" and (h[0], h[3].lower()) in fixed)]
    hits.sort(key=lambda h: (h[0], h[1] != "fix"))

    if words and bold_spans and bold_spans * 100 / words > 1.5:
        hits.append((0, "check", "formatting",
                     f"{bold_spans} bold spans in {words} words; bold almost nothing"))
    return hits


def report(name, hits, summary_only):
    fix_count = sum(1 for h in hits if h[1] == "fix")
    check_count = len(hits) - fix_count
    if summary_only:
        counts = Counter((h[1], h[2]) for h in hits)
        for (severity, category), n in sorted(counts.items()):
            print(f"{name}: {severity:5} {category:22} {n}")
    else:
        seen_advice = set()
        for lineno, severity, category, text in hits:
            where = f"{name}:{lineno}" if lineno else f"{name}"
            print(f"{where:<16} {severity:5} {category:22} {text[:70]!r}")
            seen_advice.add(category)
        if seen_advice:
            print()
            for category in sorted(seen_advice):
                print(f"  {category}: {ADVICE[category]}")
    print(f"{name}: {fix_count} fix, {check_count} check")
    return fix_count


def main():
    parser = argparse.ArgumentParser(description="Flag signs of AI-generated writing.")
    parser.add_argument("files", nargs="*", help="files to scan (default: stdin)")
    parser.add_argument("--summary", action="store_true", help="print counts per category only")
    args = parser.parse_args()

    total_fix = 0
    if args.files:
        for path in args.files:
            with open(path, encoding="utf-8") as f:
                total_fix += report(path, scan(f.read()), args.summary)
    else:
        total_fix += report("stdin", scan(sys.stdin.read()), args.summary)
    sys.exit(1 if total_fix else 0)


if __name__ == "__main__":
    main()
