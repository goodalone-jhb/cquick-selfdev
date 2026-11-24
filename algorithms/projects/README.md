# 项目目录

每个算法项目在这里建一个子目录，目录名用小写英文加连字符，例如 `attitude-estimation`。

## 新建项目

1. 复制 `docs/templates/project-readme.md` 为 `<项目名>/README.md`
2. 建立 `src/`（可复用实现）、`scripts/`（分析脚本）、`data/`（小样本数据）
3. 在本目录的表格补一行

## 现有项目

| 项目 | 说明 | 状态 | 负责人 |
| --- | --- | --- | --- |
| `attitude-estimation` | 猫耳头带姿态解算：互补滤波 → 俯仰角 | 在研 | @goodalone-jhb |

## 目录结构

```text
<项目名>/
├── README.md        必填：目标、方法、结论、如何复现
├── src/             算法实现 + 单元测试
├── scripts/         一次性分析与绘图脚本
├── data/            小体积样本 CSV（首行注明采样条件）
├── figures/         输出图
└── tuning-log.md    调参记录
```

## 硬性要求

- 依赖版本固定（`requirements.txt`），保证别人能复现
- 数据样本必须附采样条件说明，否则结论无意义
- 失败参数组也要记进 `tuning-log.md`，避免重复试错
