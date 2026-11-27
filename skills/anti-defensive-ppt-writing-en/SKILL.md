---
name: anti-defensive-ppt-writing-en
description: Structure, rewrite, and shorten presentation content into a narrative, slide titles, on-slide copy, evidence displays, and speaker cues. Use for slide outlines, paper-to-talk conversion, proposals, slide rewrites, unfocused presentations, and unnecessary defensive language. Not needed for typography, colors, animation, or file conversion alone.
---

# Presentation Content and Storytelling

Help the audience follow an evidence-backed narrative, remember a useful judgment, and understand why it matters to them. Organize around their task, remove empty defensiveness, and retain facts and qualifications that affect the judgment.

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
4. **Write usable on-slide copy.** Name concrete subjects, changes, causes, or actions. Keep editing instructions out of final copy. Mark missing data explicitly instead of filling the space with slogans.
5. **Separate screen, speech, and reference material.** Put the central judgment and key evidence on screen, optional explanation in speaker cues, and full details in appendices. Material risks, comparison conditions, and scope must remain visible on the relevant slide, not only in notes or an appendix.
6. **Give each display an evidentiary job.** State what relationship the audience should see and what it supports. Consider bars or comparable tables for comparisons, lines for trends, flows for processes, and relationship diagrams for mechanisms. Never invent chart data; label conceptual illustrations.
7. **Direct attention to the evidence.** Specify what to highlight and why it matters. Keep units, dates, sample sizes, denominators, baselines, and sources needed to interpret the result. Do not make the audience discover the contribution inside a dense table.
8. **Compare on consistent terms.** Show relevant benefits and costs together. Do not change denominators, mix periods, truncate axes, or select samples to manufacture a win. Correlation, a local pilot, and simulation do not establish causation or universal effectiveness.
9. **State limitations precisely.** Remove empty apologies and self-disparagement, while retaining real losses, negative results, and material uncertainty. An untested domain remains untested; it is neither a universal failure nor a demonstrated strength.
10. **Fit density to the reading task.** Remove irrelevant information before shortening or splitting a crowded slide. Do not solve selection problems by shrinking type. Reading decks can carry more explanation; preserve the meaning of required definitions and clauses. Avoid universal bullet counts or word limits.
11. **Make transitions advance understanding.** The next slide should answer an open question or add the next layer of evidence. Keep section dividers only when they help navigation; avoid repeating a conclusion under new headings.
12. **End by completing the audience's task.** Decisions need a supported recommendation and a concrete request; technical talks need findings and scope; lessons need application. Preserve a requested courtesy closing after the substantive ending. Do not introduce new claims at the end.

## Default delivery

Match the requested granularity: a one-slide edit stays one slide; an outline does not require a full script. For a complete content draft, provide the core message, narrative order, and slide content, with brief assumptions and missing inputs.

Use this structure where useful; omit fields that add no value:

```text
Slide X | Ready-to-use title
Audience task: What the audience should understand or decide
On-slide content: Usable copy, numbers, or diagram labels
Display suggestion: Information relationship, emphasis, and required annotations
Evidence and scope: Source, measurement basis, and limitations; mark missing inputs
Speaker cue: Additional explanation or transition, if needed
```

Material qualifications in “Evidence and scope” must also appear in on-slide copy or chart annotations. Source notes should travel with the slide. For content-only work, make display suggestions actionable without prescribing shadows, font settings, or animation parameters.

Use `[Needed: specific input]` for missing facts and keep surrounding claims tentative. Label illustrative data locally as “Fictional example; not for publication.” Do not present an unverified placeholder title as an established result.

For rewrites, briefly explain substantive changes when useful, without forcing a long diagnostic report. When producing a requested file, the above structure may remain internal planning; do not add unrequested intermediate deliverables.

## Final check

- Does reading the titles reveal a coherent argument? Does each slide add something?
- Does each material claim have evidence? Are proposals and examples distinguished from facts?
- Did compression preserve numbers, units, sources, comparable measurements, and key qualifications?
- Is the copy usable? Does the display suggestion explain what to see?
- Are requested counts, sections, timing, and retained content respected? Is the requested artifact complete?
- Are negative results and material risks still visible? Does the ending complete the audience's task?

## Attribution

Adapted from Adkid-Zephyr's [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill), extending its evidence-led narrative principle to slide roles, screen/speech separation, visual evidence, and presentation-specific tasks. The repository retains the original MIT copyright and license notice.
