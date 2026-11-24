# 编码规范

规范的作用不是限制写法，而是让任何一个人打开任何一个文件，都能在 30 秒内读懂它的结构。
以下规则优先服务于**可读性**和**可调试性**，其次才是简洁。

## 一、固件 C 语言

### 命名

| 对象 | 规则 | 示例 |
| --- | --- | --- |
| 全局变量 | `g_` 前缀 + 小写下划线 | `g_imu_raw`, `g_servo_target` |
| 静态变量 | `s_` 前缀 | `s_last_tick` |
| 函数 | 小写下划线，动词开头 | `imu_init()`, `servo_set_angle()` |
| 宏 / 常量 | 全大写下划线 | `SERVO_PULSE_MIN_US` |
| 类型 | `_t` 后缀 | `imu_sample_t`, `servo_state_t` |
| 枚举值 | 全大写，带模块前缀 | `IMU_STATE_IDLE` |

不要用拼音命名，也不要用 `a`、`tmp`、`data1` 这类名字。英文不好就用完整单词，宁可长一点。

### 格式

```c
/* 4 空格缩进，不使用 Tab */
void servo_set_angle(uint8_t ch, float deg)
{
    if (ch >= SERVO_CH_NUM) {
        return;
    }

    /* 上限保护：硬件限位 0~180，超出会顶死舵机 */
    if (deg < SERVO_ANGLE_MIN) {
        deg = SERVO_ANGLE_MIN;
    } else if (deg > SERVO_ANGLE_MAX) {
        deg = SERVO_ANGLE_MAX;
    }

    g_servo_target[ch] = deg;
}
```

- 大括号独立成行（K&R 之外统一 Allman 风格，与 ARM 官方例程保持一致）
- 一行不超过 100 字符
- 指针的 `*` 靠近变量名：`uint8_t *buf`
- 单行 `if` 也要写大括号

### 注释

注释解释**为什么**，不解释**是什么**。代码本身能说明"做了什么"。

```c
/* 差 */
/* 把 deg 赋值给 target */
g_servo_target[ch] = deg;

/* 好 */
/* 舵机响应有约 8ms 死区，目标值提前写入让下一个控制周期立即生效 */
g_servo_target[ch] = deg;
```

文件头统一用这段模板：

```c
/**
 * @file    servo.c
 * @brief   双舵机 PWM 输出与角度限幅
 * @author  姓名
 * @date    2026-11-24
 * @note    依赖 TIM3 CH1/CH2，50Hz，脉宽 500~2500us
 */
```

### 中断与实时性

| 规则 | 原因 |
| --- | --- |
| ISR 内不做浮点运算、不调用 `printf` | 耗时不可控，且部分平台浮点上下文不保存 |
| ISR 内不阻塞等待（`while` 等标志位） | 会拖垮整个系统时基 |
| ISR 与主循环共享的变量加 `volatile` | 否则编译器优化会读到缓存值 |
| 超过 10us 的逻辑移出 ISR，用标志位 + 主循环处理 | 保证中断响应时间 |
| 共享的多字节变量访问要关中断保护 | 8 位机上 32 位读写不是原子的 |

### 魔法数字

任何出现在代码里的非 0/1 数字，都应该是宏或常量，并注明来源。

```c
/* 差 */
if (adc_val > 3721) { ... }

/* 好 */
/* 3.0V 阈值，12 位 ADC、3.3V 参考：(3.0/3.3)*4095 ≈ 3723 */
#define VBAT_LOW_ADC_THRESHOLD  3723U
```

### 错误处理

不要静默失败。初始化失败要能通过日志或状态变量暴露出来：

```c
if (imu_init() != IMU_OK) {
    g_sys_status |= SYS_ERR_IMU;
    log_warn("imu init failed, continue without attitude");
}
```

上电默认状态必须是**安全状态**：舵机保持中位、电机输出为 0、功率器件关断。

## 二、算法 Python

### 基本约定

- 遵循 PEP 8，行宽 100
- 函数与模块写 docstring，说明输入输出的物理单位
- 单位一律写在变量名或注释里：`angle_deg`、`rate_dps`、`dt_s`
- 随机种子固定，保证结果可复现
- 绘图保存到 `assets/`，脚本里用相对路径

### 单位与命名

```python
def complementary_filter(accel_g: np.ndarray,
                         gyro_dps: np.ndarray,
                         dt_s: float,
                         alpha: float = 0.98) -> np.ndarray:
    """一阶互补滤波估计俯仰角。

    Args:
        accel_g:  加速度计三轴读数，单位 g，形状 (N, 3)
        gyro_dps: 陀螺仪三轴读数，单位 deg/s，形状 (N, 3)
        dt_s:     采样间隔，单位 s
        alpha:    高通权重，0.9~0.99，越大越信任陀螺

    Returns:
        俯仰角序列，单位 deg，形状 (N,)
    """
```

### 脚本结构

```text
algorithms/projects/<项目>/
├── README.md           做什么、怎么跑、结论是什么
├── data/               小体积样本数据（原始大数据放外部存储）
├── src/                可复用的算法实现
├── scripts/            一次性分析脚本，按功能命名
└── figures/            生成的图（可入库，也可 gitignore 后重跑生成）
```

一次性脚本不要写在 notebook 里就丢掉。notebook 用于探索，结论稳定后把逻辑抽到 `src/`，
并留一个能一键复现的 `scripts/`。

## 三、调参与实验记录

调参记录必须可追溯，否则下次调参等于从零开始。

每条实验记录包含：

| 字段 | 示例 |
| --- | --- |
| 日期与硬件版本 | 2026-11-24 / 主控板 v1.2 |
| 改动内容 | Kp 0.8 → 1.2，Ki 不变 |
| 现象 | 阶跃响应超调由 18% 降到 6%，上升时间 120ms → 95ms |
| 数据位置 | `figures/step-response-20261124.png` |
| 结论 | 保留本次参数，写入 `config/pid.h` 默认值 |

记录放在项目目录的 `tuning-log.md`，不要散在聊天记录里。

## 四、提交前检查

```text
[ ] 编译零 error，无新增 warning
[ ] 没有注释掉的死代码（真正的临时代码加 TODO + 日期 + 人名）
[ ] 没有硬编码的调试开关留在提交里
[ ] 新增文件已加入版本控制，未被 .gitignore 误伤
[ ] 接口变更已同步更新头文件注释与文档
```

---

文档负责人：@goodalone-jhb ｜ 最后更新：2026-11-24
