# Academic papers: revising an AI-assisted draft

This file is for revising a research paper, thesis chapter or essay that was written with AI help, usually after an AI-detection report (Turnitin or similar) has flagged parts of it. It extends SKILL.md and `ai-tells.md`; their word lists are not repeated here.

Sources were gathered in October 2026 by research agents working mostly from publisher pages and search summaries. Figures marked [U] could not be confirmed from the full text.

## What the evidence says

Turnitin scores long-form prose, not tables, bullet lists or code. It slides overlapping windows of roughly five to ten sentences across the text, gives each window a score, and each sentence inherits the scores of the windows that cover it. The reported percentage is the share of qualifying prose judged AI-written, and anything from 1% to 19% is shown only as "*%". Turnitin added detection of AI-paraphrased text in July 2024 and of "AI bypasser" (humanizer) tools in August 2025, and in August 2026 it merged both into a single "AI-generated" highlight. It also says the first and last sentences of a document were a source of false positives.

Independent studies agree on three things:

- Detectors catch unedited AI text well.
- Editing or paraphrasing lowers detection in every study that tested it. In Weber-Wulff et al. (2023), average detection across 14 tools fell from 74% for unedited AI text to 42% for lightly edited text and 26% for paraphrase-tool output [U]. Liu et al. (2024) found Turnitin caught about 94% of ChatGPT text and about 30% of Wordtune-rephrased text. Van Vlasselaer et al. (2026) report Turnitin catching 50% of humanized papers [U].
- Scores move with style in both directions. Liang et al. (2023) found detectors flagging 61% of essays by non-native writers.

So no revision method guarantees a score, and a score is not proof of authorship either way. Text that an AI has revised is still AI-assisted text. The defensible position for the author rests on their own analysis, their drafts and version history, and disclosure where the venue requires it. The moves below are about making the writing better and more clearly the author's. Any change in a detector score is a side effect.

## Hard rules

These come from the user and override everything else in this file.

1. Keep every concept and every claim at its original strength. "Suggests" stays tentative and "is the only" stays definite.
2. Keep every in-text citation: same authors, same year, same number of occurrences, APA form. A citation may move between narrative form, "Arian et al. (2024) found", and parenthetical form, "(Arian et al., 2024)".
3. Keep every sentence. One original sentence may become two or three, but none may disappear, and two may not be merged into one. If a sentence is pure scaffolding, rewrite it so it says something concrete instead of deleting it.
4. Keep every number exactly as written, and add no new numbers or facts.
5. Leave the reference list, tables, equations, figure and table captions, and headings alone unless asked.
6. Keep the author's voice. If the paper says "this study", keep saying it, along with its spelling variety and its comma style.

## Revision moves, strongest evidence first

1. Replace a trailing present-participle clause (", showing ...", ", weighting ...") with a finite clause or a new sentence. Reinhart et al. (2025, PNAS) measured GPT-4o using present participial clauses 5.3 times as often as human writers, and instruction-tuned models 2 to 5 times as often. In one Turnitin report on a finance paper, flagged prose had 2.36 of these per 1,000 words and unflagged prose had 1.10.

2. Turn nominalizations back into verbs ("the computation of X was performed" becomes "X was computed"). Reinhart et al. measured nominalizations at 2.1 times the human rate for GPT-4o. Herbold et al. (2023, Scientific Reports) found the same direction, with effect sizes of d = -0.88 for GPT-3.5 and d = -1.35 for GPT-4. Liu and Liu (2025, PLOS ONE) counted 2.15 complex nominals per clause in ChatGPT essays against 1.04 in human essays.

3. Break up chains of coordinated phrases ("X, Y, and Z of A and B") and subject "that"-clauses, and split sentences that pack in too many noun phrases. Reinhart et al. found phrasal coordination at 1.9 times and subject "that"-clauses at 2.6 times the human rate. Liu and Liu counted 0.48 coordinate phrases per clause in ChatGPT essays against 0.07 in human essays. Markey et al. (2024) describe ChatGPT text as "dense and disconnected."

4. Let "because", "although" and "so" carry the argument, and join whole clauses with "and" or "but". Liu and Liu found 1.16 dependent clauses per T-unit in human essays against 0.37 in ChatGPT essays, and Reinhart et al. found that LLMs avoid joining whole clauses with "and" or "but". Use this where there is real reasoning to show. In the finance paper's own report, the flagged prose had more subordinators than the unflagged prose, so subordination added for decoration does nothing.

5. Show stance only at the strength the original already has. Jiang and Hyland (2025, English for Specific Purposes) found ChatGPT essays use fewer hedges, boosters and attitude markers than student essays. Herbold et al. found 10.84 modals per essay in human writing against 6.12 for GPT-4. Never strengthen or weaken a claim to add stance.

6. Rewrite formulaic openers, closers and announcing sentences ("In conclusion", "Read together, these studies...", "This study addresses that gap") so they state the actual content. Herbold et al. found every ChatGPT essay opened its conclusion with "In conclusion". Jiang and Hyland (2025, Applied Linguistics) found ChatGPT relies on noun- and preposition-based stock phrases where students use stance phrases. Rule 3 means rewriting these sentences, not deleting them.

7. Tie general sentences to evidence the paper already has by naming the table, figure or section where it appears. In the finance paper's Turnitin report, unflagged prose had 66 numbers per 1,000 words and flagged prose had 45. Rule 4 still applies: point to existing evidence rather than inventing new figures.

8. Vary sentence length and openings where it reads naturally. Liu and Liu found human argument sentences were longer and more variable (28.8 words on average against 18.2), and Muñoz-Ortiz et al. (2024) found LLM sentences cluster between 10 and 30 tokens. The evidence here is weaker than for moves 1 to 4.

9. Remove the marker words listed in `ai-tells.md` and the additional ones Kobak et al. (2025, Science Advances) measured in 15.1 million abstracts. Their top ratios were delves 28.0 and underscores 13.8, and they also list potential, findings, crucial, notably, additionally, comprehensive and insights. Don't swap one marker for another: Geng and Trotta (2025) show such lists go out of date once a word becomes known as a marker.

Skip lexical-diversity and discourse-marker targets, because the studies conflict.

## What not to do

- Don't use character tricks such as look-alike letters, invisible characters or odd spacing. They conceal text instead of revising it, Dugan et al.'s (2024) RAID benchmark treats them as attacks, and text normalization catches them.
- Don't insert spelling or grammar errors. Perkins et al. (2024) used error insertion as an adversarial technique, and it degrades the paper.
- Don't spin synonyms or run text through paraphrasing or humanizer tools. These change meaning. Krishna et al. (2023) and Sadasivan et al. (2025) frame them as attacks, and Turnitin has targeted bypasser output since August 2025.
- Don't break the hard rules by deleting or merging sentences, dropping a citation or moving it off its claim, changing claim strength, or adding facts or numbers.
- Don't treat a score as proof either way. Turnitin's own guidance says the score should not be the sole basis for an academic misconduct decision.

## Procedure

Work one section at a time, using prose paragraphs only (no headings, captions, tables, equations or references), and keep a stable ID for each paragraph.

When sub-agents are available, use three roles:

- A Sonnet agent does web lookups only, such as checking a citation detail or the wording of a source. It does no rewriting.
- One Opus rewriter per section applies the moves above under the hard rules and writes the revised paragraphs to a JSON file keyed by paragraph ID. It runs the checks below on its own section before handing back.
- An Opus reviewer at the top reads every revised paragraph against the original for meaning, claim strength, citations and numbers, and runs the checks. It sends back any failing paragraph with the reason. Only after that does it write the text into the document, validate the file and render it to check the layout.

Run these checks:

```bash
python3 <skill-dir>/scripts/check_preservation.py original.txt revised.txt
python3 <skill-dir>/scripts/scan_tells.py revised.txt
python3 <skill-dir>/scripts/style_metrics.py original.txt revised.txt
```

The work passes when:

- `check_preservation.py` prints PASS. Every item it lists as new must be a real item from the original paper, such as a table number.
- `scan_tells.py` reports 0 "fix" hits outside quoted titles.
- `style_metrics.py` shows trailing "-ing" clauses and nominalizations down, numbers per 1,000 words not lower, and sentence-length spread not lower. These are directions to aim for, not targets.

When reporting back, say what changed and what the checks showed. Don't predict a detector score.

## Examples

These come from a finance paper on explainable AI for NIFTY 50 trading. Citations, numbers and claims are unchanged, and no sentence is lost.

### A trailing participle clause becomes its own sentence

Moves 1 and 3; one sentence becomes two.
> Before: For the tree- and kernel-based models, SHAP (Salih et al., 2025) gives each feature a contribution, its SHAP value, showing how far that feature moved a single day's predicted return above or below the model's average output.
>
> After: For the tree- and kernel-based models, SHAP (Salih et al., 2025) gives each feature a contribution, its SHAP value. The value shows how far that feature moved a single day's predicted return above or below the model's average output.

### A participle clause becomes a joined clause

Moves 1 and 4; the sentence count stays the same.
> Before: Instead of processing the sequence one step at a time, the Transformer (Vaswani et al., 2017) lets each time step attend directly to every other time step, weighting each one by its relevance to the prediction.
>
> After: The Transformer (Vaswani et al., 2017) lets each time step attend directly to every other time step instead of reading the sequence one step at a time, and it weights each step by its relevance to the prediction.

### Nominalizations become verbs

Moves 2 and 3; one sentence becomes three.
> Before: The study's explainable-AI contribution comes from applying SHAP (for SVM, Random Forest, and XGBoost), Integrated Gradients (for LSTM and Transformer), and self-attention weights (for the Transformer) as a post-hoc explanation layer that breaks individual predictions into feature-level contributions, and from showing that these attributions shift measurably between a COVID-era validation regime and a more recent test regime.
>
> After: The study's explainable-AI contribution comes from two steps. It applies SHAP (for SVM, Random Forest, and XGBoost), Integrated Gradients (for LSTM and Transformer), and self-attention weights (for the Transformer) after training, as a post-hoc layer that breaks each prediction into the contributions of its features. It then shows that these attributions shift measurably between a COVID-era validation regime and a more recent test regime.

### A coordination chain is split

Move 3; one sentence becomes two.
> Before: Every model is scored on accuracy, on risk-adjusted return, and on which features its explanations rank highest, and accuracy and return are kept as separate outcomes throughout.
>
> After: Each model gets three scores: its accuracy, its risk-adjusted return, and the features its explanations rank highest. Accuracy and return stay separate outcomes throughout.

### A formulaic opener states its content

Move 6; the sentence count stays the same.
> Before: Read together, these four strands of literature leave a consistent gap.
>
> After: All four strands of literature reviewed above leave the same gap.

### A trailing "which" clause becomes its own sentence

Moves 1 and 3; one sentence becomes two.
> Before: For attention-based architectures, Ma et al. (2023) apply a self-attention Transformer to asset allocation and pair its attention weights with SHAP analysis to identify which economic features drive its allocation decisions, which is close to this study's joint use of Transformer attention weights and Integrated Gradients.
>
> After: For attention-based architectures, Ma et al. (2023) apply a self-attention Transformer to asset allocation and use SHAP alongside its attention weights to find which economic features drive its allocation decisions. That pairing is close to this study's joint use of Transformer attention weights and Integrated Gradients.

## Sources

- Dugan, L., et al. (2024). RAID: A shared benchmark for robust evaluation of machine-generated text detectors. ACL 2024. https://doi.org/10.18653/v1/2024.acl-long.674
- Geng, M., & Trotta, R. (2025). Human-LLM coevolution: Evidence from academic writing. Findings of ACL 2025. https://aclanthology.org/2025.findings-acl.657/
- Herbold, S., et al. (2023). A large-scale comparison of human-written versus ChatGPT-generated essays. Scientific Reports, 13, 18617. https://doi.org/10.1038/s41598-023-45644-9
- Jiang, F. K., & Hyland, K. (2025). Does ChatGPT argue like students? Bundles in argumentative essays. Applied Linguistics, 46(3), 375-391. https://doi.org/10.1093/applin/amae052
- Jiang, F. K., & Hyland, K. (2025). Rhetorical distinctions: Comparing metadiscourse in essays by ChatGPT and students. English for Specific Purposes, 79, 17-29.
- Kobak, D., et al. (2025). Delving into LLM-assisted writing in biomedical publications through excess vocabulary. Science Advances, 11(27), eadt3813. https://doi.org/10.1126/sciadv.adt3813
- Krishna, K., et al. (2023). Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense. NeurIPS 36.
- Liang, W., et al. (2023). GPT detectors are biased against non-native English writers. Patterns, 4(7), 100779. https://doi.org/10.1016/j.patter.2023.100779
- Liu, J. Q. J., et al. (2024). The great detectives: Humans versus AI detectors in catching large language model-generated medical writing. International Journal for Educational Integrity, 20, Article 8. https://doi.org/10.1007/s40979-024-00155-6
- Liu, W., & Liu, X. (2025). A comparative analysis of syntactic complexity in argumentative essays from rhetorical perspective: ChatGPT vs. English native speakers. PLOS ONE, 20(8), e0329410. https://doi.org/10.1371/journal.pone.0329410
- Markey, B., et al. (2024). Dense and disconnected: Analyzing the sedimented style of ChatGPT-generated text at scale. Written Communication, 41(4), 571-600. https://doi.org/10.1177/07410883241263528
- Muñoz-Ortiz, A., et al. (2024). Contrasting linguistic patterns in human and LLM-generated news text. Artificial Intelligence Review, 57, 265. https://doi.org/10.1007/s10462-024-10903-2
- Perkins, M., et al. (2024). Simple techniques to bypass GenAI text detectors: Implications for inclusive education. International Journal of Educational Technology in Higher Education, 21, Article 53. https://doi.org/10.1186/s41239-024-00487-w
- Reinhart, A., et al. (2025). Do LLMs write like humans? Variation in grammatical and rhetorical styles. PNAS, 122(8), e2422455122. https://doi.org/10.1073/pnas.2422455122
- Sadasivan, V. S., et al. (2025). Can AI-generated text be reliably detected? Transactions on Machine Learning Research.
- Van Vlasselaer, M., et al. (2026). Who wrote this? Evaluating the reliability of AI detection tools in higher education. International Journal for Educational Integrity, 22, Article 16. https://doi.org/10.1007/s40979-026-00226-w [U]
- Weber-Wulff, D., et al. (2023). Testing of detection tools for AI-generated text. International Journal for Educational Integrity, 19, Article 26. https://doi.org/10.1007/s40979-023-00146-z
- Turnitin product pages and guides on AI writing detection (guides.turnitin.com; turnitin.com/blog), read through search summaries.
