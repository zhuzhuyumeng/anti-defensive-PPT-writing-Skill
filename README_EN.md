# Anti-Defensive PPT Writing

Turn raw material into a coherent, evidence-backed presentation: narrative, slide titles, usable copy, display suggestions, and speaker cues. Lightweight instructions with no runtime dependencies.

[中文](README.md) · [English Skill](skills/anti-defensive-ppt-writing-en/SKILL.md) · [中文 Skill](skills/anti-defensive-ppt-writing/SKILL.md) · [Quick prompt](prompts/quick-prompt-en.txt)

## Principle

**Organize a supported narrative around what the audience needs to understand or decide, and give every slide a clear job.**

Do not allocate equal space to every activity or make the audience discover the contribution inside a table. Explain the useful finding directly. Keep on-slide copy brief by default: keep only the judgment and key numbers, and do not restate the title or repeat the same conclusion in several places. If a negative result is the point of the slide, state it plainly. Do not put qualifications, limitations, sources, risks, scope-of-use notes, or missing-evidence markers on the slide. Reducing empty defensiveness never licenses inventing or exaggerating claims.

## Deliverables and scope

The skill produces a core message, narrative order, slide titles, and ready-to-use on-slide copy. Speaker cues, appendix notes, and missing-input lists appear only when needed, and not as on-slide qualifications, limitations, sources, risks, scope notes, or missing-evidence markers. It supports proposals, research talks, retrospectives, product demonstrations, and teaching; it can draft, rewrite, or shorten content.

If an actual PPTX or HTML deck is requested, the agent must use available file-authoring capabilities to finish it. This repository does not contain a slide-rendering engine.

## Quick start

Copy [the short prompt](prompts/quick-prompt-en.txt) into an AI conversation, then supply material and requirements. Or install the skill:

```bash
git clone https://github.com/zhuzhuyumeng/anti-defensive-PPT-writing-Skill.git
cd anti-defensive-PPT-writing-Skill
mkdir -p ~/.codex/skills
cp -R skills/anti-defensive-ppt-writing-en ~/.codex/skills/
# Optional Chinese version:
cp -R skills/anti-defensive-ppt-writing ~/.codex/skills/
```

You can install either language independently. Other `SKILL.md`-compatible tools can use the whole language-specific directory, including its references and license.

```text
Use $anti-defensive-ppt-writing-en to turn this material into an eight-slide
management proposal. The decision is whether to approve a wider pilot.
Provide ready-to-use titles and on-slide copy for each slide.
[Material]
```

## Plugin packaging

This repository includes plugin manifests and a local marketplace entry modeled on the upstream layout:

```bash
codex plugin marketplace add zhuzhuyumeng/anti-defensive-PPT-writing-Skill
codex plugin add anti-defensive-ppt-writing@zhuzhuyumeng-presentations
```

These commands require a Codex version with plugin marketplace support. This repository does not claim an official directory listing.

Build the distribution with Python's standard library:

```bash
python3 scripts/build_plugin.py
```

The output is `dist/anti-defensive-ppt-writing-1.0.0.zip`. Use `--output /path/to/package.zip` to change its destination. The archive includes both skills and their referenced examples, UI metadata, license notices, and plugin assets.

## Twelve rules

1. One main audience question per slide.
2. Informative titles, no stronger than their evidence.
3. Order by understanding and decision needs.
4. Usable, concise copy rather than restated titles, slogans, or editing instructions.
5. Separate screen, speech, and reference detail; state each fact once; keep qualifications, limitations, sources, risks, scope notes, and missing-evidence markers off the slide.
6. Give charts and diagrams an evidentiary job.
7. Highlight the evidence; keep units needed to read the numbers, not sources or measurement caveats on the chart.
8. Compare consistently and show relevant costs.
9. Remove empty apologies; retain real negative results when they are the finding, without inventing or exaggerating.
10. Adapt density to a talk or a reading deck; default to brevity and avoid filler.
11. Make transitions advance understanding; do not replay earlier conclusions.
12. Finish the audience's task with a finding, application, or concrete request.

See the [full workflow](skills/anti-defensive-ppt-writing-en/SKILL.md) and [examples](skills/anti-defensive-ppt-writing-en/references/examples.md). All example metrics are fictional and must be replaced before publication.

## Attribution and license

Maintained by zhuzhuyumeng. Adapted from Adkid-Zephyr's [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill), extending evidence-led academic storytelling to slide roles, visual evidence, screen/speech separation, and presentation-specific tasks.

MIT license with the original copyright notice retained. See [LICENSE](LICENSE) and [PRIVACY.md](PRIVACY.md).
