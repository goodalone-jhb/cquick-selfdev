# 文档中心

所有需要"写给以后看"的内容都放这里。代码旁边只放代码注释，跨模块的说明一律进 `docs/`。

## 索引

| 文档 | 内容 | 谁该读 |
| --- | --- | --- |
| [onboarding.md](onboarding.md) | 环境搭建、仓库上手、第一次提交 | 所有新成员 |
| [workflow.md](workflow.md) | 分支、提交、PR、评审、发布流程 | 所有成员 |
| [coding-style.md](coding-style.md) | 固件 C 语言与算法 Python 的代码风格 | 写代码的人 |
| [hardware-conventions.md](hardware-conventions.md) | 硬件命名、引脚表、原理图版本、接口约定 | 电控组 |
| [documentation-guide.md](documentation-guide.md) | 怎么写、放哪、命名、图片引用 | 所有成员 |
| [glossary.md](glossary.md) | 术语与缩写对照 | 所有成员 |
| [adr/](adr/) | 架构与选型决策记录 | 想知道"为什么这么做"的人 |

## 按需求找

- 我要开始做一块新板子 → [hardware-conventions.md](hardware-conventions.md)
- 我要上交一份周报 → [templates/weekly-report.md](templates/weekly-report.md)
- 项目出事了要复盘 → [templates/postmortem.md](templates/postmortem.md)
- 我要记录一次技术选型 → [adr/README.md](adr/README.md)
- 我在调 PID 但不知道参数怎么记 → [coding-style.md](coding-style.md) 末节「调参与实验记录」

## 文档分级

| 级别 | 存放位置 | 生命周期 |
| --- | --- | --- |
| 长期规范 | `docs/*.md` | 长期有效，随团队演进而修订 |
| 决策记录 | `docs/adr/NNNN-*.md` | 永久留存，推翻时新建一条而非改写 |
| 项目文档 | `projects/<项目>/README.md` | 随项目存续 |
| 周期性记录 | `docs/reports/` | 按学期/赛季归档 |
| 临时笔记 | 个人分支的 `notes/` | 结论稳定后并入正式文档 |

## 维护责任

每份文档在文首标注负责人和最后更新日期，格式见 [documentation-guide.md](documentation-guide.md)。
过期文档不要直接删除，移入 `docs/archive/` 并在原文顶部注明替代关系。
