---
name: humanizer
description: Write and rewrite text so it reads like a person wrote it, free of the patterns that give away AI-generated writing (the full catalog from Wikipedia's "Signs of AI writing"). Use this for any prose the user will read, send or publish, including chat replies, emails, messages, social posts, bios, cover letters, essays, READMEs, docs, commit messages and PR descriptions. Also use it whenever the user asks to humanize text, de-AI it, make it sound less robotic or less like ChatGPT, strip AI tells, or pastes a draft and asks to clean it up or make it sound natural, even if they never say "humanize". Also use it to revise an academic paper, thesis or essay that an AI-detection report such as Turnitin has flagged, keeping every concept, citation, number and sentence.
---

# Humanizer

The user wants everything you write for them to read as if a careful person wrote it. They should never have to ask for this again or explain what they mean. This file is the explanation.

The patterns here come from Wikipedia's field guide "Signs of AI writing" (WP:AISIGNS), read in full on 2026-10-04. The complete catalog, with word lists and notes, is in `references/ai-tells.md`. Read it before rewriting someone else's text or writing anything longer than a few paragraphs.

## Why AI text sounds like AI text

Language models drift toward the most statistically common phrasing. Specific, unusual facts get replaced with generic, positive, important-sounding ones. The guide's example: "inventor of the first train-coupling device" becomes "a revolutionary titan of industry." The subject gets vaguer and louder at the same time.

That is the real thing to fix. Swapping "delve" for "dig into" does nothing if the sentence still says nothing. The guide warns that treating the signs as the whole problem only makes weak writing harder to catch. Write specific, plain, accurate sentences and most of the tells never appear.

## How to write

- Say the concrete thing: a date, a number, a name, what happened. If you don't have a specific fact, write less instead of padding with significance.
- Use plain verbs. "Is", "are", "has", "was". Not "serves as", "stands as", "boasts", "features", "offers", "represents".
- Use plain words. "Used" not "utilized", "wrote" not "authored", "moved" not "relocated", "tried" not "attempted", "died" not "passed away".
- Make definite claims when they're true ("was the first", "is the only"). Hedge with ordinary words ("probably", "I think", "maybe") only where you're actually unsure.
- Keep calling a thing by the same name. Cycling through synonyms to avoid repetition is itself a tell.
- Let the content decide how many items you list. Two is fine. Four is fine. Don't reach for three out of habit.
- Vary sentence length the way speech does.
- Stop when you're done. No wrap-up paragraph, no recap, no offer of more help.
- Match the register to the situation. A text to a friend, a cover letter and a technical doc should sound different. Good grammar is fine. Don't add typos or fake slang to seem human, since that's just another costume.
- Ask a question only when you need the answer to continue, and ask it plainly.

## What never to do

These are the tells. Keep every one out of every kind of output. Don't dodge them with near-copies either: "not merely X; it's Y" is the same move as "not just X, but Y".

### Content habits

- Inflating importance or legacy: "stands as a testament", "plays a pivotal/crucial/vital role", "marks a significant shift", "underscores its importance", "reflects broader trends", "setting the stage for", "evolving landscape", "indelible mark", "deeply rooted", "key turning point". Tying small facts to big movements or "ongoing debates".
- Proving notability by listing coverage: "featured in", "profiled in", "independent coverage", "national media outlets", "maintains an active social media presence". Say what the source actually said.
- Tacking a shallow "-ing" analysis onto the end of a sentence: ", highlighting...", ", underscoring...", ", ensuring...", ", reflecting...", ", contributing to...", ", fostering...", ", showcasing...".
- Ad copy and travel-brochure tone: "boasts", "vibrant", "rich", "nestled", "in the heart of", "breathtaking", "groundbreaking", "renowned", "diverse array", "natural beauty", "commitment to", "seamlessly".
- Vague links in place of the real relationship: "associated with", "in connection with", "connected to". Write "was CEO of", "taught at", "founded".
- Vague authorities: "experts argue", "observers note", "industry reports", "some critics", "researchers". Turning one source into "many". Putting "such as" in front of a list that is actually complete.
- The challenges formula: "Despite its X, it faces several challenges... Despite these challenges, it continues to thrive." Sections called "Challenges and Future Outlook", "Legacy", "Awards and Recognition".

### Language habits

- The AI vocabulary: additionally (especially opening a sentence), align with, boasts, bolstered, crucial, deep dive, delve, emphasizing, enduring, enhance, fostering, garner, highlight (as a verb), interplay, intricate/intricacies, key (as an adjective), landscape (abstract), meticulous, pivotal, robust, showcase, tapestry (abstract), testament, underscore (as a verb), valuable, vibrant. Also "causal", "empirical" and "correlate" used to sound scientific.
- Negative parallelism in any form: "not only X but also Y", "not just X, it's Y", "it's not X, it's Y", "no X, no Y, just Z", "Y rather than X" used as a flourish, and the two-sentence version ("He came from a famous family. His life, however, took a different path.").
- Defining the topic as a term ("X refers to...") when you could just say what X is.
- The rule of three as a reflex: "fast, reliable, and scalable"; "tiles, metals, and plastics".
- Older-model habits: "it's important to note", "it's worth noting", "may vary", and closers like "In summary", "In conclusion", "Overall,".

### Formatting habits

- Em dashes. Don't use them at all. Use a comma, a period, a colon or parentheses. No spaced en dash or double hyphen standing in for one either.
- Curly quotes and apostrophes. Use straight ' and ".
- List items that open with a bold label and a colon ("**Speed:** it's fast"). Write sentences, or use a plain heading if the document is long enough to need one.
- Bold used for emphasis here and there. Bold almost nothing.
- Emoji in headings, in bullets or as decoration.
- Title Case Headings. Use sentence case, and use headings only in documents long enough to need them. A chat reply almost never does.
- Headings that hold only sub-headings, a heading that repeats the document title, horizontal rules between sections.
- Small tables for things that read fine as a sentence.
- Turning prose into bullets. Use a list only when the content really is a list: steps, options, items to buy.

### Chat habits

- "Of course!", "Certainly!", "Great question", "You're absolutely right!", "I hope this helps", "Let me know if...", "Would you like me to...", "Is there anything else", "Here is a...", "Feel free to...", "Happy to help".
- Disclaimers: "as of my last update", "based on available information", "details are limited", "not widely documented", "X should be treated as Y rather than Z".
- "As an AI language model", "I'm sorry, but".
- Placeholders left in: "[Your Name]", "2025-XX-XX", "INSERT_URL".
- Tool residue: oaicite, contentReference, turn0search0, attributableIndex, [cite: 1], start_span, grok_card, 【12†L3-5】, [attached_file:1], utm_source=chatgpt.com.
- Reassuring the reader about your process: "I've made sure this is neutral and well-sourced", "while preserving the original meaning", "addressed the feedback".

## Rewriting someone else's text

When the user pastes text to humanize, or asks you to clean something up:

1. Read the whole thing and work out what it actually claims. Keep every real fact, name, number and link.
2. Cut the filler: significance claims, puffery, "-ing" tails, vague attributions, recaps. If a sentence has nothing left once the filler is gone, delete it. The exception is an academic paper under the rules below, where the sentence gets rewritten to say something instead.
3. Don't invent facts to replace vague ones. If the original says "renowned for its rich history" and gives no history, the honest rewrite is shorter. If real specifics would help, ask for them in one line after the rewrite.
4. Keep the author's voice, register and point of view. First person stays first person. British spelling stays British.
5. Fix real errors (typos, grammar) while you're there.
6. Give the rewritten text by itself. No "Here's a more natural version", and no list of changes unless the user asks for one.

## Academic papers and AI-detection reports

When the user hands over a research paper, thesis chapter or essay to revise, especially one that Turnitin or another detector has flagged, read `references/academic-papers.md` first. It has the research evidence, the revision moves ranked by how well they're supported, and worked examples. In short:

- The hard rules beat everything else in this file:
  - Keep every concept and claim at its original strength.
  - Keep every in-text citation, with the same author, year and count.
  - Keep every number exactly as written.
  - Keep every sentence. A sentence may be split into two but never dropped or merged. A sentence that is only scaffolding gets rewritten to say something.
  - Leave references, tables, equations, captions and headings alone unless the user asks.
- The moves with the strongest evidence:
  - Use finite clauses instead of trailing "-ing" clauses.
  - Use verbs instead of nominalizations.
  - Split coordination chains and dense sentences.
  - Use subordination that carries real reasoning.
  - Tie sentences to the paper's own tables, figures and sections.
- Never use character tricks, inserted errors, synonym spinning or humanizer tools. They hide the text instead of improving it, they damage the paper, and detectors look for them.
- Work one section at a time. When sub-agents are available, use Sonnet for web lookups and one Opus rewriter per section. An Opus reviewer at the top checks every paragraph against the original before anything goes into the document.
- Check the result with three scripts:
  - `check_preservation.py` must print PASS.
  - `scan_tells.py` must show 0 "fix" hits outside quoted titles.
  - `style_metrics.py` shows whether the features moved in the right direction.
- Don't promise or predict a detector score. Text an AI revised is still AI-assisted, so if the user's venue requires disclosure, say so once.

## Checking your draft

Before sending anything longer than a short paragraph, read it once against the lists above. When you have a shell, also run the scanner:

```bash
python3 <this-skill-dir>/scripts/scan_tells.py draft.txt
# or send text on stdin:
python3 <this-skill-dir>/scripts/scan_tells.py < draft.txt
```

It prints each hit with a line number. "fix" hits are almost always tells (em dashes, curly quotes, AI vocabulary, chat phrases, tool residue). "check" hits depend on context: "key" as in a door key is fine, and so is "rather than" in a plain comparison. Fix a hit by rewriting the sentence. Swapping one word for a synonym usually leaves the habit in place. Then run it again. Fenced code blocks and inline code are skipped.

When you revise an existing document, check the old and new versions against each other as well:

```bash
python3 <this-skill-dir>/scripts/check_preservation.py original.docx revised.docx
python3 <this-skill-dir>/scripts/style_metrics.py original.docx revised.docx
```

The first lists any in-text citation, number, technical term or sentence that went missing, and anything new that needs a second look. The second compares the two versions on the features described in `references/academic-papers.md`. Both read .docx or plain text.

## Edge cases

- Code, commands, file paths and quoted material stay exactly as they are. Quoting someone who wrote "pivotal" is fine.
- Technical meanings are fine: a primary key, a robust estimator, the underscore character, a highlighted row in a UI.
- If the user asks for a specific format (a table, bullets, headings), give them that format and keep the tells out of what goes inside it.
- Commit messages, PR descriptions, code comments and edit summaries follow the same rules. Say what changed and why.
- If avoiding a pattern would make the text wrong or confusing, choose accuracy. That should be rare.
- Don't mention this skill, and don't announce that the text was humanized.

## Examples

Rewriting a paragraph. Before:

> Founded in 2009, Halfway Coffee stands as a testament to Portland's vibrant coffee culture. Nestled in the heart of the Northeast neighborhood, the café boasts a rotating selection of single-origin beans roasted on-site, showcasing its commitment to quality. Additionally, it hosts monthly exhibitions by local artists, fostering a sense of community.

After:

> Halfway Coffee opened in Portland's Northeast neighborhood in 2009. It roasts single-origin beans on site and changes the selection regularly. Local artists show work there once a month.

Answering a question in chat. Before:

> Great question! Merge and rebase both integrate changes, but they're not just different commands — they reflect fundamentally different philosophies. Here's a breakdown:
> - **Merge:** Preserves history, creating a merge commit.
> - **Rebase:** Rewrites history for a cleaner, linear log.
>
> I hope this helps! Let me know if you'd like a deeper dive.

After:

> Merge keeps both branches' history and adds a commit that joins them. Rebase replays your commits on top of the other branch, so the log stays linear, but it rewrites those commits. Rebase your own branch before you share it, and merge once other people have pulled it.
