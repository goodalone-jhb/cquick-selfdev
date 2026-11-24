# 电控组

负责硬件电路、固件、驱动与调试。目标是让"想法变成能动的实物"，并且这个实物能被别人接手维护。

## 技术栈

| 层次 | 内容 |
| --- | --- |
| 主控 | PY32F002BF15P6（Cortex-M0+，24MHz）、STM32F0/F1 系列备选 |
| 工具链 | EIDE + arm-none-eabi-gcc，DAPLink 调试 |
| 外设 | PWM（舵机）、I2C（IMU）、UART（调试/上位机）、ADC（电压监测） |
| 驱动 | 舵机、直流电机、MOSFET 驱动、电源管理 |
| 设计工具 | 立创 EDA / Altium，打样走嘉立创 |

## 目录约定

```text
electronics/
├── README.md            本文件
└── projects/
    └── <项目名>/
        ├── README.md        目标、状态、编译方法、已知问题
        ├── pinmap.md        引脚分配表（见硬件约定）
        ├── hardware/        原理图、PCB、BOM
        ├── firmware/        固件工程（EIDE 工程配置入库）
        ├── notes.md         调试记录
        ├── reviews/         硬件评审记录
        └── CHANGELOG.md     版本变更
```

固件工程只提交源码与工程配置（`eide.json`、`.code-workspace` 除外），
编译产物、Keil 中间文件由 `.gitignore` 排除。

## 在建项目

| 项目 | 说明 | 状态 |
| --- | --- | --- |
| 猫耳头带 | PY32F002B 主控 + MPU6050 + 双舵机，头部动作跟随 | 在研 |

新建项目时复制上面的目录结构，并在表格里补一行。

## 开工检查清单

拿到一块新板子，先按这个顺序走一遍，避免后面反复返工：

```text
[ ] 万用表测各路电源对地电阻，确认无短路
[ ] 上电测 3V3 / 5V 实际电压，记录偏差
[ ] 确认复位电平与 BOOT 引脚状态
[ ] SWD 能识别到芯片 ID
[ ] 烧一个最小程序，LED 能闪
[ ] 调试串口能打印
[ ] 逐个验证外设：PWM 波形、I2C 应答、ADC 读数
[ ] 测空载与满载电流，记录温升
```

## 常用命令

```bash
# 编译（以 EIDE 工程为例，也可在 VS Code 里点构建）
# 烧录（DAPLink）
pyocd flash -t py32f002x5 build/firmware.hex

# 或用 EIDE 内置的烧录功能，配置写进 eide.json
```

> 具体命令以各项目 README 为准，工具版本不一致时优先记录实际可用的那条。

## 调试习惯

- 串口日志分级：`ERROR` / `WARN` / `INFO` / `DEBUG`，量产版本关掉 DEBUG
- 关键变量用 VOFA+ 或串口上位机实时看波形，不要靠猜
- 改动前先量一下，改动后再量一次，把两次的数据都记进 `notes.md`
- 每次上电异常，先怀疑电源，再怀疑时序，最后才怀疑代码

## 交接要求

项目换人时，必须补齐：

```text
[ ] README 里的"当前状态"和"已知问题"是最新的
[ ] 引脚表与实际板子一致
[ ] 所有飞线、割线在 README 中标注位置和原因
[ ] 实物照片存入 assets/
[ ] 调参记录在 tuning-log.md 里
```
