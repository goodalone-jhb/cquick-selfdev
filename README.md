# CQuick 自研方向 · 电控组 & 算法组

[![文档检查](https://github.com/goodalone-jhb/cquick-selfdev/actions/workflows/docs-check.yml/badge.svg)](https://github.com/goodalone-jhb/cquick-selfdev/actions/workflows/docs-check.yml)

> 从硬件电控到控制算法的全链路技术沉淀：代码、文档、踩坑记录、复盘。

这个仓库不是"交作业用的文件夹"，而是让下一届接手的人能少走弯路的地方。
每一份设计、每一次调参、每一个失败的尝试，只要值得后人参考，就应该落进这里。

## 仓库定位

- **代码仓**：电控固件、算法实现、仿真脚本、上位机工具
- **文档仓**：设计决策记录（ADR）、硬件约定、调试手册、周报与复盘
- **知识库**：新人入门、术语表、常见故障排查

不适合放这里的内容：比赛当天的临时脚本、体积巨大的原始测试数据（用外部存储 + 链接）、他人未授权的第三方资料。

## 目录结构

```text
.
├── README.md               仓库总览（本文件）
├── CONTRIBUTING.md         协作规范：分支、提交、PR、评审
├── docs/                   文档中心
│   ├── README.md           文档索引
│   ├── onboarding.md       新人入门：环境搭建与第一条提交
│   ├── workflow.md         协作流程详解
│   ├── coding-style.md     编码规范（C / Python）
│   ├── hardware-conventions.md  硬件命名、引脚表、版本管理约定
│   ├── documentation-guide.md   文档维护规范
│   ├── reports/            周报、阶段总结、复盘
│   └── templates/          周报 / 复盘模板
├── electronics/            电控组
│   ├── README.md           电控组技术栈与在建项目
│   └── projects/           每个项目一个子目录
├── algorithms/             算法组
│   ├── README.md           算法组技术栈与在建项目
│   └── projects/           每个项目一个子目录
├── assets/                 文档配图（原理图截图、波形、曲线）
└── .github/                Issue / PR 模板、CI
```

## 两个组分别在做什么

| 方向 | 电控组 | 算法组 |
| --- | --- | --- |
| 核心任务 | 硬件平台与固件：主控最小系统、驱动电路、电源与保护、通信总线、固件架构与在线调试 | 感知与控制：姿态解算、控制律设计、参数辨识、运动规划、仿真与数据分析 |
| 典型产出 | 原理图 / PCB、固件工程、硬件测试报告 | 算法实现、仿真工程、调参记录、性能对比 |
| 常用工具 | EIDE、arm-none-eabi-gcc、DAPLink、立创 EDA / Altium | Python、MATLAB/Simulink、Jupyter、串口数据采集工具 |
| 关注指标 | 稳定性、EMC、功耗、实时性 | 精度、响应延迟、鲁棒性、算力占用 |

### 在建项目

| 项目 | 方向 | 状态 | 入口 |
| --- | --- | --- | --- |
| 猫耳头带（MPU6050 姿态跟随 + 双舵机） | 电控 + 算法 | 在研 | [electronics/projects](electronics/projects) · [algorithms/projects](algorithms/projects) |

新增项目时，请在 `electronics/projects/` 或 `algorithms/projects/` 下建目录，并在上面的表格补一行。

## 快速开始

```bash
git clone https://github.com/goodalone-jhb/cquick-selfdev.git
cd cquick-selfdev
```

第一次参与，先读 [docs/onboarding.md](docs/onboarding.md)，按里面的清单把环境配好，
再读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解怎么提代码和提文档。

## 文档导航

| 我想…… | 该看 |
| --- | --- |
| 第一次参与这个仓库 | [新人入门](docs/onboarding.md) |
| 知道代码怎么提、PR 怎么过 | [协作流程](docs/workflow.md) |
| 写固件 / 写算法脚本的代码风格 | [编码规范](docs/coding-style.md) |
| 画板子、接传感器、命名引脚 | [硬件约定](docs/hardware-conventions.md) |
| 写一份留得住的文档 | [文档维护规范](docs/documentation-guide.md) |
| 写周报 / 做复盘 | [周报模板](docs/templates/weekly-report.md) · [复盘模板](docs/templates/postmortem.md) |
| 查术语 | [术语表](docs/glossary.md) |
| 找历史决策的原因 | `docs/adr/` |

## 协作方式

- **分支**：`main` 为稳定分支，禁止直接推送；开发走 `feat/`、`fix/`、`docs/` 前缀分支
- **提交**：遵循 Conventional Commits，例如 `feat(servo): 加入舵机软启动`
- **合并**：一律通过 Pull Request，至少 1 人评审；文档类改动可自审后合并
- **Issue**：任务、缺陷、需求都开 Issue，PR 描述里用 `Closes #12` 关联

细节见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 维护约定

- 每个项目目录必须有 `README.md`：目标、当前状态、如何编译/运行、已知问题
- 调试过程中的关键结论，当天写进对应的 `notes.md` 或周报，不留在聊天记录里
- 文档里的截图放 `assets/`，用相对路径引用，文件名用英文小写加连字符
- 半年以上的过期文档，标记 `> ⚠️ 已归档` 或移入 `docs/archive/`，不要悄悄删掉

## 联系

- 仓库维护：[@goodalone-jhb](https://github.com/goodalone-jhb)
- 问题反馈：开 [Issue](https://github.com/goodalone-jhb/cquick-selfdev/issues)

---

本仓库内容版权归 CQuick 战队所有，未经许可请勿外传或商用。
