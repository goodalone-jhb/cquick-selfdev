# 术语表

统一叫法，避免同一件事在不同文档里三个名字。新增术语请补一行。

## 通用与组织

| 术语 | 全称 / 英文 | 说明 |
| --- | --- | --- |
| 自研方向 | In-house Development | 战队自行设计硬件、编写固件与算法的技术路线，区别于使用成品模块 |
| 电控组 | Electronics & Control | 负责硬件电路、固件、驱动与调试 |
| 算法组 | Algorithm | 负责感知、控制律、参数辨识与仿真 |
| ADR | Architecture Decision Record | 技术选型决策记录，放 `docs/adr/` |
| 复盘 | Postmortem | 事件后的事实梳理与改进项追踪 |

## 硬件

| 术语 | 全称 / 英文 | 说明 |
| --- | --- | --- |
| MCU | Microcontroller Unit | 微控制器，本项目为 PY32F002BF15P6 |
| SWD | Serial Wire Debug | 两线调试接口（SWDIO / SWCLK） |
| 最小系统 | Minimal System | 让 MCU 能运行的最小外围：电源、时钟、复位、调试口 |
| 电源树 | Power Tree | 从输入到各负载的电压转换关系图 |
| 去耦电容 | Decoupling Capacitor | 靠近芯片电源引脚的 100nF 电容，滤高频噪声 |
| 飞线 | Bodge Wire | 改板时手工焊接的跳线，必须在文档中记录 |
| 丝印 | Silkscreen | PCB 表面的文字标识层 |
| PDB | Power Distribution Board | 配电板 |

## 控制与算法

| 术语 | 全称 / 英文 | 说明 |
| --- | --- | --- |
| IMU | Inertial Measurement Unit | 惯性测量单元，含加速度计与陀螺仪 |
| DMP | Digital Motion Processor | MPU6050 内置的运动处理单元，可直接输出四元数 |
| 姿态解算 | Attitude Estimation | 由 IMU 数据推算俯仰/横滚/偏航角 |
| 互补滤波 | Complementary Filter | 陀螺积分与加速度计观测的加权融合，实现简单、算力低 |
| Mahony / Madgwick | — | 基于梯度下降的姿态滤波算法，精度高于互补滤波 |
| EKF | Extended Kalman Filter | 扩展卡尔曼滤波，处理非线性系统 |
| PID | Proportional-Integral-Derivative | 比例-积分-微分控制器 |
| 串级控制 | Cascade Control | 外环位置 + 内环速度/电流的两级控制结构 |
| 前馈 | Feedforward | 依据模型提前给出控制量，减小跟踪误差 |
| 阶跃响应 | Step Response | 输入突变时的输出变化曲线，评价超调与上升时间 |
| 超调量 | Overshoot | 响应峰值超出目标值的百分比 |
| 死区 | Deadband / Dead Zone | 输入变化但输出无响应的区间 |
| 系统辨识 | System Identification | 由输入输出数据拟合系统模型参数 |
| 零漂 | Bias Drift | 陀螺仪静止时的输出偏移随时间变化 |
| 标定 | Calibration | 消除传感器零偏与尺度误差的过程 |

## 工具与流程

| 术语 | 说明 |
| --- | --- |
| EIDE | VS Code 的嵌入式开发插件，管理工程、构建与烧录 |
| arm-none-eabi-gcc | ARM Cortex-M 裸机交叉编译器 |
| DAPLink | 常用调试器固件，支持 SWD 下载与调试 |
| CI | 持续集成，本仓库用于检查 Markdown 格式与链接 |
| Squash and merge | 把分支的多个提交压成一个合入，保持主分支历史线性 |
| Conventional Commits | 提交信息规范，格式 `type(scope): 描述` |

---

文档负责人：@goodalone-jhb ｜ 最后更新：2026-11-24
