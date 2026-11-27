---
name: anti-defensive-ppt-writing-en
description: Structure, rewrite, and shorten presentation content into a narrative, slide titles, and ready-to-use on-slide copy. Use for slide outlines, paper-to-talk conversion, proposals, slide rewrites, unfocused presentations, and unnecessary defensive language. Not needed for typography, colors, animation, or file conversion alone.
---

# Presentation Content and Storytelling

Help the audience follow an evidence-backed narrative, remember a useful judgment, and understand why it matters to them. Organize around their task, remove empty defensiveness, and retain facts and qualifications that affect the judgment. Keep on-slide copy brief: include only what helps the judgment, and do not repeat the same conclusion, background, or reasoning in several places.

## Scope

- Handle content selection, narrative order, slide hierarchy, and evidence presentation. Content-only work needs no rendering, coding, or network dependency.
- Respect requested templates, slide counts, sections, terminology, and language. Retrospectives may need chronology; teaching may need gradual explanation; defenses and audits must answer required questions.
- When the user requests a PPTX, HTML deck, or changes to a presentation file, complete that artifact using available authoring capabilities and their required rendering checks. An outline is not a substitute for a requested deck.

## Workflow

### 1. Identify the audience's task

Read the supplied material and existing slides. Identify the audience, purpose, intended understanding or decision, duration or slide count, and required content. Do not ask again for information already supplied.

For missing preferences, state a brief assumption and proceed. For missing facts, mark the gap and complete what is possible. A topic alone permits a structure and evidence checklist, not invented achievements, findings, or customer stories.

Distinguish a live talk from a standalone reading deck. Move supporting explanation into speaker cues for a talk; retain enough context for an independent reader. Choose slide count from the material, duration, and user constraints rather than a rigid slides-per-minute rule.

### 2. Match claims to evidence

Form one core message: **subject or problem + supported judgment + audience significance**. Label unvalidated proposals as recommendations or hypotheses.

Prioritize useful, well-supported information instead of allocating equal space to every activity. Distinguish observations from interpretations and recommendations. Check both the evidence for a claim and its scope.

Narrow unsupported claims or mark them for validation. Where no advantage is established, present the current state, trade-offs, and open problems accurately; do not manufacture a breakthrough.

Select a suitable narrative rather than filling a mandatory template:

| Task | Possible progression |
| --- | --- |
| Decision or proposal | Recommendation and evidence → alternatives and trade-offs → resources, risks, and decision request |
| Research or technical talk | Problem and gap → method or mechanism → results and scope → significance |
| Retrospective | Target and actual outcome → gaps and causes → effective practices → corrective action |
| Product demonstration | User task → usage → verifiable outcome → fit and next step |
| Teaching | Learning goal → concept → example or demonstration → practice and transfer |

### 3. Build the slides

Assign each slide a job before writing its title, copy, and display suggestion. The title sequence should communicate the main reasoning without relying on the presenter to repair missing logic. For calibration and edge cases, read [references/examples.md](references/examples.md).

## Twelve rules

1. **One main audience question per slide.** Several pieces of evidence may support one judgment. Split independent conclusions and merge repetition. Covers, navigation, references, and appendices need not use conclusion titles.
2. **Make titles informative.** State a specific supported finding instead of a generic topic. Use a clear question or recommendation for unsettled decisions; guiding questions can suit teaching. Never make the title stronger than the evidence.
3. **Order by understanding or decision needs.** Establish the key understanding, then add necessary context. Do not default to company history or a project diary. When chronology matters, show how turning points changed the outcome.
4. **Write usable, concise on-slide copy.** Name concrete subjects, changes, causes, or actions in short phrases, numbers, or contrasts—not paragraphs or a speaker script. Do not restate a title that already makes the point. Keep editing instructions out of final copy. Mark missing data explicitly instead of filling the space with slogans.
5. **Separate screen, speech, and reference material; state each fact once.** Put the central judgment and key evidence on screen, optional explanation in speaker cues, and full details in appendices. Do not copy the same sentence into the title, bullets, chart labels, and speaker cues. Material risks, comparison conditions, and scope must remain visible on the relevant slide, not only in notes or an appendix.
6. **Give each display an evidentiary job.** State what relationship the audience should see and what it supports. Consider bars or comparable tables for comparisons, lines for trends, flows for processes, and relationship diagrams for mechanisms. Never invent chart data; label conceptual illustrations.
7. **Direct attention to the evidence.** Specify what to highlight and why it matters. Keep units, dates, sample sizes, denominators, baselines, and sources needed to interpret the result. Do not make the audience discover the contribution inside a dense table.
8. **Compare on consistent terms.** Show relevant benefits and costs together. Do not change denominators, mix periods, truncate axes, or select samples to manufacture a win. Correlation, a local pilot, and simulation do not establish causation or universal effectiveness.
9. **State limitations precisely.** Remove empty apologies and self-disparagement, while retaining real losses, negative results, and material uncertainty. An untested domain remains untested; it is neither a universal failure nor a demonstrated strength.
10. **Fit density to the reading task; default to brevity.** Remove repetition, background, and points already made on other slides before shortening wording or splitting a crowded slide. Do not solve selection problems by shrinking type. Reading decks may add necessary context, but still avoid paraphrasing the same point. Preserve the meaning of required definitions and clauses. Avoid universal bullet counts or word limits, and do not fill a slide just to make it look complete.
11. **Make transitions advance understanding; do not replay old conclusions.** The next slide should answer an open question or add the next layer of evidence. Keep section dividers only when they help navigation; avoid repeating a conclusion under new headings. A closing slide should keep the decision, scope, or request, not relist earlier titles.
12. **End by completing the audience's task.** Decisions need a supported recommendation and a concrete request; technical talks need findings and scope; lessons need application. Preserve a requested courtesy closing after the substantive ending. Do not introduce new claims at the end.

## Default delivery

Match the requested granularity: a one-slide edit stays one slide; an outline does not require a full script.

For a complete content draft, deliver only three things: one core message, the narrative order (a list of slide titles is enough), and each slide's ready-to-use title and on-slide copy. State assumptions and missing inputs once, not on every slide.

By default, write each slide as:

```text
Slide X | Ready-to-use title
On-slide content: Scannable short lines, numbers, or diagram labels
```

Do not add audience-task, display-suggestion, or evidence-and-scope fields on every slide. Put material qualifications, limitations, and needed sources in the on-slide copy or chart annotations. Add a speaker cue only when a live talk needs a point that is not already on screen; do not include one by default.

Keep on-slide copy as scannable short lines or bullets. Do not paste planning notes or a speaker script onto the slide. If the user explicitly asks how to display something, say in one sentence what relationship to show; do not prescribe shadows, font settings, or animation parameters.

Use `[Needed: specific input]` for missing facts and keep surrounding claims tentative. Label illustrative data locally as “Fictional example; not for publication.” Do not present an unverified placeholder title as an established result.

For rewrites, briefly explain substantive changes when useful, without forcing a long diagnostic report. When producing a requested file, do not add unrequested intermediate drafts or field templates.

## Final check

- Does reading the titles reveal a coherent argument? Does each slide add something?
- Does each material claim have evidence? Are proposals and examples distinguished from facts?
- Did compression preserve numbers, units, sources, comparable measurements, and key qualifications?
- Is the copy ready to put on a slide? If deleting a sentence or slide leaves the judgment, numbers, and material qualifications intact, should it have been cut? Do the title and body, or adjacent slides, restate one another?
- Did the draft add audience-task, display-suggestion, or evidence fields that are not needed for presentation?
- Are requested counts, sections, timing, and retained content respected? Is the requested artifact complete?
- Are negative results and material risks still visible? Does the ending complete the audience's task?

## Attribution

Adapted from Adkid-Zephyr's [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill), extending its evidence-led narrative principle to slide roles, screen/speech separation, visual evidence, and presentation-specific tasks. The repository retains the original MIT copyright and license notice.
