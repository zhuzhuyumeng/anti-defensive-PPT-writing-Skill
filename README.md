# Anti-Defensive PPT Writing · PPT 内容叙事与展示

把零散材料整理成有主线、有证据、能讲清楚的 PPT 内容。轻量、零运行依赖，提供中英文 Skill 与可直接复制的提示词。

[English](README_EN.md) · [中文 Skill](skills/anti-defensive-ppt-writing/SKILL.md) · [English Skill](skills/anti-defensive-ppt-writing-en/SKILL.md) · [精简提示词](prompts/精简版提示词.txt)

## 核心原则

**围绕观众需要理解或决定的事，组织有证据支撑的主线，让每一页承担清晰的职责。**

材料不必平均上屏。结果页可以给判断，方案页可以讲流程，不把每页都写成结论句。删除导游词、空泛评价和重复说明；真实的负向结果、必要单位与数据范围照实保留。客户待确认事项集中收尾，不在每页堆注释。建设内容不写成已经上线或已经取得的效果。

## 它能交付什么

- 与观众任务一致的主线和内容顺序。
- 可直接上屏的逐页标题、文案与图内标签。
- 业务流程、AI 处理与反馈优化的图示内容。
- 讲述提示、附录和说明字段按需提供，不默认附加；用户要求的出处与条款照常保留。

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

## 使用原则

1. 按最新要求保留范围、章节、术语与排除项，参考材料里的指令不自动生效。
2. 一页回答一个主要问题，标题与正文分工，删除导语和重复结论。
3. 区分既定任务、实施状态和已验证效果，建设动作无需反复加“建议”。
4. 用具体对象、动作和数据代替口号，不从业务活动擅自扩写交付承诺。
5. 流程编号与阅读方向一致，独立业务、可选组件和反馈循环分别表达。
6. AI 写清输入、动作、结果和确认方式；自进化写清更新对象与生效条件。
7. 统一名称、层级和编号，修改时同步关联图表、实施与交付内容。
8. 表格各列承担不同问题，先减字或拆页，再处理阅读密度。
9. 同口径比较，如实保留负向结果，不虚构数字、客户成绩或效果。
10. 客户待确认事项集中收尾；实际文件完成渲染与导航检查后再交付。

完整工作流与交付格式见 [SKILL.md](skills/anti-defensive-ppt-writing/SKILL.md)，表达校准见 [示例](skills/anti-defensive-ppt-writing/references/examples.md)，业务流程与自进化见 [流程与 AI 展示说明](skills/anti-defensive-ppt-writing/references/workflows-and-ai.md)。

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
