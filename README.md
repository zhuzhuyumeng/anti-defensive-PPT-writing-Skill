# Anti-Defensive PPT Writing · PPT 内容叙事与展示

把零散材料整理成有主线、有证据、能讲清楚的 PPT 内容。轻量、零运行依赖，提供中英文 Skill 与可直接复制的提示词。

[English](README_EN.md) · [中文 Skill](skills/anti-defensive-ppt-writing/SKILL.md) · [English Skill](skills/anti-defensive-ppt-writing-en/SKILL.md) · [精简提示词](prompts/精简版提示词.txt)

## 核心原则

**围绕观众需要理解或决定的事，组织有证据支撑的主线，让每一页承担清晰的职责。**

材料不必平均上屏，过程不必逐项汇报，优势需要主动解释。真实的负向结果若本身就是判断，必须如实保留，不编造或夸大；口径、限制、来源、风险、适用范围和待补信息不要写上 PPT。上屏文案默认从简，只保留判断和关键数字，不重复标题，不把同一结论写多遍。“减少防御性表达”不等于隐瞒事实或夸大结果。

## 它能交付什么

- 一句核心信息与整套叙事顺序。
- 可直接上屏的逐页标题、文案与图内标签。
- 讲述提示和附录只在需要时提供；不要把口径、限制、来源、风险、适用范围或待补写上页面。

适合方案汇报、研究答辩、业务复盘、产品展示与教学讲解。既能从材料生成内容，也能压缩或改写已有页面。若要求实际 PPTX 或 HTML 成品，须结合所在工具的文件制作能力；本仓库本身不包含幻灯片渲染引擎。

## 效果对比

以下数字均为**虚构示例，不用于正式展示**。

| 常见写法 | 改写方向 |
| --- | --- |
| 标题：效果分析 | 单部门试点的平均处理时间由 10 分钟降至 6 分钟 |
| 调研 → 开发 → 测试 → 总结 | 建议 → 证据 → 取舍 → 资源请求 |
| “全面赋能业务，形成管理闭环” | “提交工单 → 自动分派 → 状态追踪”，每步标明执行者 |
| “虽然效果有限，但我们仍然……” | 准确写出观察结果，不把负向结果改写成优势 |
| 准确率较低却宣称“全面领先” | 同时展示准确率与延迟，说明目标场景的真实取舍 |

## 快速使用

### 复制提示词

打开 [中文精简提示词](prompts/精简版提示词.txt) 或 [English prompt](prompts/quick-prompt-en.txt)，复制到 AI 对话，再提供材料与要求。

```text
用这套原则，把以下材料整理成面向管理层的 8 页 PPT 内容。
目标：决定是否批准下一阶段试点。
每页给出可直接上屏的标题和文案。
[粘贴材料]
```

### 安装到 Codex skills 目录

```bash
git clone https://github.com/zhuzhuyumeng/anti-defensive-PPT-writing-Skill.git
cd anti-defensive-PPT-writing-Skill
mkdir -p ~/.codex/skills
cp -R skills/anti-defensive-ppt-writing ~/.codex/skills/
# 如需英文版：
cp -R skills/anti-defensive-ppt-writing-en ~/.codex/skills/
```

可只安装所需语言。显式使用示例：

```text
请用 $anti-defensive-ppt-writing 改写这套汇报：保留学校规定的五个章节，
把过程流水账整理成问题、证据和结论，并保留负向实验与局限。
```

其他支持 `SKILL.md` 的工具可复制对应 skill 整个目录，目录须包含 `references/` 与 `LICENSE`。

### Codex 插件包

仓库提供与上游相同结构的插件清单，以及本项目的本地 marketplace 条目：

```bash
codex plugin marketplace add zhuzhuyumeng/anti-defensive-PPT-writing-Skill
codex plugin add anti-defensive-ppt-writing@zhuzhuyumeng-presentations
```

上述命令需要支持插件 marketplace 的 Codex 版本。本仓库提供打包元数据，未声明已在官方目录上架。

构建包含全部 skill 引用资源的分发包：

```bash
python3 scripts/build_plugin.py
```

产物为 `dist/anti-defensive-ppt-writing-1.0.0.zip`。也可通过 `--output /path/to/package.zip` 指定位置。构建脚本只使用 Python 标准库，生成目录不提交到源码。

## 十二条规则

1. 一页服务一个主要问题，拆分独立结论，合并重复表达。
2. 标题传递有依据的判断，未知内容用问题或建议。
3. 按理解或决策需要排序，保留有解释价值的过程。
4. 上屏文案具体、简短、可直接使用，不复述标题，不用口号填空。
5. 分清上屏、讲述、备查，同一事实只写一次；口径、限制、来源、风险、适用范围和待补不上屏。
6. 图表承担论证职责，不虚构数据。
7. 明确视觉重点，数字保留必要单位，不在图上补充口径或来源。
8. 同口径比较，同时呈现相关代价。
9. 删除空泛道歉，如实保留作为判断的负向结果，不编造或夸大。
10. 密度适应演讲或阅读，默认从简，不为填满页面而重复。
11. 页面承接推进理解，不回放旧结论，少做重复导航。
12. 收尾完成观众的任务，给出结论、应用或行动请求。

完整工作流与交付格式见 [SKILL.md](skills/anti-defensive-ppt-writing/SKILL.md)，特殊情况见 [示例](skills/anti-defensive-ppt-writing/references/examples.md)。

## 仓库结构

```text
├── skills/
│   ├── anti-defensive-ppt-writing/       # 中文 skill、示例、UI 元数据与许可
│   └── anti-defensive-ppt-writing-en/    # English equivalent
├── prompts/                             # 中英文精简提示词
├── .codex-plugin/plugin.json            # Codex 插件清单
├── .agents/plugins/marketplace.json     # 本地 marketplace 条目
├── plugin.json                          # 通用插件清单
├── assets/icon.svg
├── scripts/build_plugin.py
├── PRIVACY.md
└── LICENSE
```

## 来源与许可

本项目由 zhuzhuyumeng 维护，参考 Adkid-Zephyr 的 [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)，将学术写作中的证据叙事思路改编为 PPT 内容工作流，并补充页面职责、图表表达、上屏与讲述分工和场景适配。

采用 MIT 许可，保留原项目版权与许可声明。隐私说明见 [PRIVACY.md](PRIVACY.md)。
