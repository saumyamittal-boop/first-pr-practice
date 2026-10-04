# Signs of AI writing: full catalog

Condensed from the Wikipedia project page "Wikipedia:Signs of AI writing" (WP:AISIGNS), as it stood on 2026-10-04. Wikipedia text is available under CC BY-SA 4.0. This file paraphrases it and keeps the word lists; the example sentences are new.

The page is a field guide for spotting undisclosed AI text on Wikipedia, so some items are about wiki markup. Those are kept here because the same habits show up in Markdown, email and chat.

Contents

1. The root cause
2. Content
3. Language and grammar
4. Style and formatting
5. Talking to the reader
6. Markup and tool residue
7. Citations
8. Comments and edit summaries
9. Miscellaneous
10. Older tells
11. What human writing does more
12. Things that do not indicate AI

## 1. The root cause

Models predict the most likely next words, so output regresses to the mean. Rare, specific facts get smoothed into common, generic, positive statements that could describe almost anything. The subject becomes less specific and more exaggerated at once. The guide stresses that the signs point to deeper problems (missing facts, invented claims, unsupported analysis), and that hiding the signs without fixing those problems just makes bad text harder to catch.

## 2. Content

### Undue emphasis on significance, legacy and broader trends

Statements that some ordinary detail represents or contributes to something bigger.

Words to watch: stands/serves as, is a testament/reminder, a crucial/pivotal/vital/significant/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted.

Variants: placing a subject inside "debates" or "public discussions"; adding this to dull topics like a town's name origin or population figures; hedging first ("though it saw limited use") and then claiming importance anyway; for plants and animals, stressing ties to "the broader ecosystem" and conservation status even when nothing is known.

Do instead: give the fact. If there's no fact, cut the sentence.

### Canned emphasis on notability, attribution and media coverage

Hitting the reader with proof of notability by describing the sources rather than what they say.

Words to watch: independent coverage, local/regional/national media outlets, music/business/tech outlets, trade publications, cited/featured/profiled in, written by a leading expert, active social media presence, maintains a strong digital presence, was identified by.

Newer chatbots also attach their own analysis to named sources ("Roger Ebert highlighted the lasting influence") whether or not the source says anything like it.

### Superficial analyses

An "-ing" phrase stuck on the end of a sentence to add meaning that isn't there, often with a vague third party.

Words to watch: highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., enhancing..., valuable insights, align/resonate with.

Example of the habit: "The station has eight tracks, facilitating the movement of passengers and goods and contributing to the socio-economic development of the region."

### Promotional, advertisement-like language

Travel guide or press release tone, even when asked for neutral writing, and even in rewrites that claim to remove promotional tone.

Words to watch: boasts a, vibrant, rich, profound, enhancing, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking, renowned, featuring, diverse array, breathtaking, offers visitors a glimpse, seamlessly, value-driven.

Sub-patterns: "cultural heritage" topics get constant reminders of their importance; people and companies get press-release phrasing about goals, sustainability, commitment and customer focus; products get car-brochure description ("imparts a sense of refined dynamism"). Newer models are more subtly positive and avoid flat superlatives like "the best".

### Vague expression of connection or association

"Associated with", "connected to", "in connection with" in place of the actual relationship. "Professor Doe was connected with science education at Example University" instead of "Professor Doe taught science at Example University." Often stacked with puffery: "particularly/widely associated with".

### Vague attributions and overgeneralized opinions

Weasel words that pin claims on unnamed authorities, and inflating a source or two into a consensus.

Words to watch: industry reports, observers have cited, experts argue, some critics argue, several sources/publications (when few are cited), researchers and conservationists, described in scholarship, modern researchers treat, such as (before a list that is actually complete).

### Outline-like conclusions about challenges and future prospects

A rigid formula: "Despite its [positive words], [subject] faces several challenges, including..." ending in a vaguely upbeat line or speculation about initiatives that could help. Often in sections called "Challenges", "Challenges and Legacy", "Future Outlook", "Future Prospects", "Future Directions".

Words to watch: Despite its... faces several challenges, Despite these challenges, continues to thrive, positions them as, the future of X lies in its ability to adapt.

The sign is the formula, not any mention of a challenge.

### "Awards and recognition" and "X and Y" headings

Headings shaped like "X and Y" are common in AI articles, and "Awards and recognition" (or just "Recognition") especially so.

## 3. Language and grammar

### High density of "AI vocabulary"

These words became far more frequent after 2022 and tend to appear together. One or two may be chance. Many of them in one piece of text is one of the strongest tells.

Additionally (especially opening a sentence), align with, boasts (meaning "has"), bolstered, crucial, deep dive, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), meticulous/meticulously, pivotal, robust, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant.

By era: 2023 to mid-2024 (GPT-4) leaned on additionally, boasts, bolstered, crucial, delve, emphasizing, enduring, garner, intricate, interplay, key, landscape, meticulous, pivotal, underscore, tapestry, testament, valuable, vibrant. Mid-2024 to mid-2025 (GPT-4o) on align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant. Mid-2025 on (GPT-5) on emphasizing, enhance, highlighting, showcasing, plus the notability phrasing above. Grok overuses "scientific" words such as causal, empirical, correlate, and still uses underscore.

Take the list literally. A tell word's synonyms are not automatically tells, and literal senses (a musical underscore, a landscape painting) are fine. The fix is to drop the habit behind the word, not to find a replacement word.

### Avoiding "is" and "are"

Replacing simple copulas with "serves as", "stands as", "marks", "functions as", "operates as", "represents", and replacing "has" with "boasts", "features", "maintains", "offers". Newer output gets more elaborate: "ventured into politics as a candidate" for "was a candidate", "began his career as" for "was". In first sentences, "X refers to..." instead of "X is...". AI copyedits often "improve" text this way.

### Negative parallelisms

Text that sounds like it's correcting a misconception nobody had.

- Not just X, but also Y: "not only... but...", "it is not just..., it's...", "doesn't just X; it Y".
- Not X, but Y: "it's not..., it's...", "no..., no..., just...", "is not a mirror but a portal".
- Y rather than X: the reversed form, common in Grok, also in ChatGPT and Claude.
- Across sentences: "He came from a famous theatrical family. His life, however, took a path of its own."

### Leads that treat a list or broad title as a proper noun

"The 'List of songs about Mexico' is a curated compilation..." or "Catchment area (health) refers to...". Defining the title instead of the subject.

### Rule of three

"Adjective, adjective, adjective" or "phrase, phrase, and phrase", used to make thin analysis look complete. Stronger as a sign where nobody would bother with a flourish, like an edit summary.

## 4. Style and formatting

- Title heading: a heading with the document name placed above everything, as if the title weren't already shown.
- Title case in headings: capitalizing every main word.
- Headings that contain only other headings.
- Overuse of boldface: bolding phrases mechanically, often every instance of a key term, in a "key takeaways" style learned from READMEs, slide decks and listicles.
- Inline-header vertical lists: a bullet or number followed by a bold header, a colon, then text. Sometimes the header has no punctuation at all. Bullets may be •, -, –, #, or emoji instead of real list markup.
- Em dashes: used more often than people use them, where a comma, parentheses or colon fits better, often with spaces around them, and in a punchy, sales-like way. A July 2026 study found Claude still uses more em dashes than professional writers. Newer ChatGPT versions suppress them.
- Emoji as formatting: in front of headings or bullets.
- Unusual tables: small, thin tables that should be a sentence.
- Curly quotation marks and apostrophes (ChatGPT, DeepSeek), sometimes mixed with straight ones. Not proof alone, since Word and phones convert quotes too.
- Skipped heading levels (starting at level 3) and overuse of level 1 headings, usually from Markdown being converted.
- Thematic breaks (horizontal rules) between every section.

## 5. Talking to the reader

### Collaborative communication

Text meant for the chatbot user, pasted into the final piece.

Words to watch: I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., is there anything else, let me know, more detailed breakdown, here is a. Also "In this section, we will discuss...", advice addressed to the writer ("ensure the content is presented in a neutral tone"), "Here's a template you can copy and paste", and offers to reformat.

### Disclaimers about knowledge cutoffs, sources or usage

Words to watch: up to my last training update, as of my last knowledge update, while specific details are limited/scarce, not widely available/documented/disclosed, in the provided/available sources or search results, [claim] should be treated as... rather than..., based on available information, maintains a low profile, keeps personal details private. These often come with speculation about what the missing information "likely" is.

### Phrasal templates and placeholders

Fill-in-the-blank text left unfilled: [Describe the specific section], [Your Name], [Entertainer's Name], [link to source list], (Add your channel URL here), access-date=2025-XX-XX, url=URL, INSERT_SOURCE_URL_30, PASTE_SPOTIFY_TRACK_URL_HERE, comments like "Add if available with citation".

## 6. Markup and tool residue

- Markdown where the medium doesn't use it: ## for headings, **bold**, [text](url), --- rules. Mixed Markdown and wiki syntax, and fenced blocks like ```wikitext, are strong signs.
- Broken or hallucinated markup, categories and templates.
- ChatGPT: `:contentReference[oaicite:0]{index=0}`, `oai_citation`, `Example+1`, `citeturn0search0`, `turn0image0`, `citeturn0news0`, `citeturn1file0`, `({"attribution":{"attributableIndex":"1009-1"}})`.
- Gemini: `[cite: 1]`, `[cite: 3, 12, 13]`, `[span_1](start_span)`, `[span_1](end_span)`.
- Grok: `<grok-card data-id=...>`, `grok_render_citation_card_json`.
- DeepSeek: lenticular brackets with daggers, like `【85†L261-269】`.
- Perplexity: `[attached_file:1]`, `[web:1]`, URLs containing `ppl-ai-file-upload`.
- Unclassified: `:::writing{variant="document" id="12345"}`.

## 7. Citations

- Several dead links that were never archived.
- Invalid ISBN checksums and DOIs that don't resolve.
- DOIs that resolve to unrelated papers.
- Book citations with no page numbers, or with page numbers that don't support the claim, and no URL.
- Odd reference syntax, reference names defined but never used, and the ↩ character around footnotes.
- Tracking parameters: `utm_source=chatgpt.com`, `utm_source=openai`, `utm_source=copilot.com`, `referrer=grok.com`.

## 8. Comments and edit summaries

People pasting chatbot text into discussions also tend to: misquote policies and invent policy shortcuts; post long comments split into titled sections; claim they put in the effort to follow the rules; ask critics to say exactly what to improve; call concerns about AI "unsubstantiated speculation"; and urge everyone to "focus on improving the content". Openers like "Dear Editorial Team, I am writing to..." and "I hope this message finds you well" belong here too.

AI edit summaries follow templates:

- Canned assurances of following the rules. Words to watch: ensured that... adheres to, refined, enhanced, enriched, streamlined, improved, in compliance with, guidelines/style/standards, revised, verifiability, neutrality, neutral tone, encyclopedic tone, clarity, flow.
- Mentioning what was kept or avoided. Words to watch: preserved, retained, avoided, ensured, aimed to. "Revised for neutrality while preserving the original meaning."
- Stressing that content is sourced rather than saying what it is. Words to watch: added sourced information, added verified content, added citations/references/coverage, improved attribution, with independent/secondary/third-party/peer-reviewed sources.
- Listing parameter and template names with their markup.
- "Addressed reviewer feedback", which goes without saying.

## 9. Miscellaneous

- A sudden jump in someone's writing quality or style compared with their earlier writing.
- An English variety that doesn't fit the writer or topic (American spelling by default).
- Notes to reviewers pasted into drafts arguing that the piece meets the rules.
- Pre-filled review or maintenance templates that make no sense.
- Canned profile pages: "Welcome To My User Page!", "About Me", "My Interests", "Let's Connect!", "Happy Editing! 🚀", with emoji and bold.
- Lots of benign-looking edits made very fast.
- Model differences: ChatGPT and Grok lean on broader context and run long; Gemini and Claude are usually more concise.
- Content bias: models can lean pro-authoritarian on some political prompts.

## 10. Older tells

Less common now but still worth avoiding.

- Didactic disclaimers: it's important/critical/crucial to note/remember/consider, worth noting, may vary.
- Section summaries: In summary, In conclusion, Overall, and sections titled "Conclusion".
- Prompt refusals: as an AI language model, as a large language model, I cannot offer medical advice but I can..., I'm sorry.
- Abrupt cut-offs mid-sentence.
- Citation access dates that are older than the edit.
- Elegant variation: cycling through synonyms for the same thing ("the artists... these non-conformists... like-minded creators") because of repetition penalties.

## 11. What human writing does more

Measured over 25 years of Wikipedia text, people use these more than models do:

- Simple "is" and "has" phrases ("there is a", "it has a").
- Plain words instead of stiff or euphemistic ones: wrote (authored), moved (relocated), used (utilized), tried (attempted), died (passed away).
- Superlative or definite statements: one of the best, is the only, was the first.
- Hedges and intensifiers: very, perhaps, tends to.
- Some wordy constructions: as a result of, in order to, all of the, a part of, the fact that.

## 12. Things that do not indicate AI

The guide lists these as unreliable, so there is no need to avoid them: perfect grammar; mixing casual and formal registers; bland prose; formal or academic prose in general (only the specific words above matter); transition words on their own; unsourced content; odd wiki markup in general; correct markup. Detectors and human judges are both unreliable, and a 2025 study found people do no better than chance at telling AI text from human text.
