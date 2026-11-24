# 新人入门

目标：一个下午之内，让你能独立编译、烧录、改一行代码并提一个 PR。

## 一、先搞清楚自己在哪个组

| 组别 | 你的第一件事 |
| --- | --- |
| 电控组 | 把固件编译烧录到板子上，让 LED 闪起来 |
| 算法组 | 把一条串口数据采下来，画出曲线 |

不要跳过这一步。工具链没跑通之前，读多少文档都是空的。

## 二、通用准备

### 1. Git 与账号

```bash
git --version          # 需要 2.30 以上
git config --global user.name  "你的名字"
git config --global user.email "你的邮箱"
```

把 GitHub 账号告诉仓库维护人，拉你进协作。首次推送需要认证，推荐用
Git Credential Manager（Git for Windows 自带），推送一次后凭据会被记住。

### 2. 克隆仓库

```bash
git clone https://github.com/goodalone-jhb/cquick-selfdev.git
cd cquick-selfdev
```

### 3. 编辑器

推荐 VS Code。统一使用仓库根目录的 `.editorconfig` 风格：UTF-8、LF、4 空格（C）/ 4 空格（Python）、行尾不留空格。

## 三、电控组环境

### 工具链清单

| 工具 | 用途 | 备注 |
| --- | --- | --- |
| EIDE（VS Code 插件） | 工程管理、构建、烧录 | 用它管理 `eide.json`，工程配置入库 |
| arm-none-eabi-gcc | 交叉编译 | 建议固定版本，写进 `projects/<项目>/README.md` |
| DAPLink | 调试与烧录 | 装好驱动，确认设备管理器能识别 |
| 串口工具 | 日志与在线调参 | 推荐 VOFA+ 或 串口助手 |
| 立创 EDA / Altium | 原理图与 PCB | 按项目组习惯 |

### 验证流程

```text
1. 打开 projects/<项目>/ 下的 EIDE 工程
2. 选择目标芯片型号，确认编译器路径正确
3. 编译，应无 error；warning 记录数量，不要新增
4. 接 DAPLink，烧录，确认程序运行（LED / 串口打印）
5. 打开串口，看到心跳日志即算环境就绪
```

### 常见卡点

| 现象 | 排查方向 |
| --- | --- |
| 编译报 `arm-none-eabi-gcc not found` | 工具链未加入 PATH，或 EIDE 里未指定路径 |
| 烧录报 `No target connected` | 排线/供电/SWD 引脚复用；目标芯片是否被读保护 |
| 程序跑了但串口无输出 | 波特率、TX/RX 交叉、时钟配置、引脚复用 |
| 上电就重启 | 看门狗未喂、电源跌落、启动文件栈大小不足 |

## 四、算法组环境

### 工具链清单

| 工具 | 用途 |
| --- | --- |
| Python 3.10+（建议 venv） | 数据处理、仿真、上位机 |
| numpy / scipy / matplotlib | 数值计算与绘图 |
| pandas | 实验数据整理 |
| Jupyter | 探索性分析 |

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install numpy scipy matplotlib pandas jupyter
```

### 验证流程

```text
1. 从串口/日志导出一段原始数据（CSV）
2. 用脚本读入、画出一条曲线
3. 保存图到 assets/，脚本入库到 algorithms/projects/<项目>/
```

## 五、第一次提交

```bash
git switch -c docs/your-name-intro
# 改点什么：修个错别字也行
git add .
git commit -m "docs(onboarding): 补充串口无输出的排查项"
git push -u origin docs/your-name-intro
```

然后在 GitHub 上开 Pull Request，按模板填写。等评审通过、合并，你就正式加入了。

## 六、读什么

按顺序读这三份，其余用到再翻：

1. [协作流程](workflow.md) —— 代码怎么走
2. [编码规范](coding-style.md) —— 代码怎么写
3. [硬件约定](hardware-conventions.md) 或 [术语表](glossary.md) —— 按组选

## 七、遇到问题怎么办

1. 先在本仓库搜：GitHub 搜索框 + `Ctrl+Shift+F` 本地搜
2. 再翻 [Issue](https://github.com/goodalone-jhb/cquick-selfdev/issues) 里有没有人问过
3. 还没有就开一个 Issue，写清现象、复现步骤、已排除的可能
4. 问人时把上面这些一起发出来，不要只发"报错了怎么办"

---

文档负责人：@goodalone-jhb ｜ 最后更新：2026-11-24
