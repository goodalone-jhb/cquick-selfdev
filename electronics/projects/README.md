# 项目目录

每个自研项目在这里建一个子目录，目录名用小写英文加连字符，例如 `paw-headband`。

## 新建项目

1. 复制 `docs/templates/project-readme.md` 为 `<项目名>/README.md`
2. 按 [硬件约定](../../docs/hardware-conventions.md) 建立 `pinmap.md`
3. 固件工程放 `firmware/`，只提交源码与 EIDE 工程配置
4. 在本目录的表格补一行

## 现有项目

| 项目 | 说明 | 状态 | 负责人 |
| --- | --- | --- | --- |
| `paw-headband` | 猫耳头带：PY32F002B + MPU6050 + 双舵机 | 在研 | @goodalone-jhb |

## 目录结构

```text
<项目名>/
├── README.md        必填：目标、状态、编译方式、已知问题
├── pinmap.md        必填：引脚分配表
├── hardware/        原理图、PCB、BOM（大文件用链接）
├── firmware/        固件源码与工程配置
├── notes.md         调试记录，按日期追加
├── reviews/         硬件评审记录
└── CHANGELOG.md     版本变更
```
