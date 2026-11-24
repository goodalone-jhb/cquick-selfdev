# CQuick 自研方向 · 电控组 & 算法组

[![文档检查](https://github.com/goodalone-jhb/cquick-selfdev/actions/workflows/docs-check.yml/badge.svg)](https://github.com/goodalone-jhb/cquick-selfdev/actions/workflows/docs-check.yml)

战队自研方向的代码与文档仓库，电控组和算法组共用。

## 目录

| 目录 | 用途 |
| --- | --- |
| `electronics/` | 电控组的固件、硬件资料与文档 |
| `algorithms/` | 算法组的实现、脚本与实验记录 |
| `docs/` | 跨组的规范与说明文档 |
| `assets/` | 文档引用的图片 |
| `tools/` | 脚本工具 |

各组项目在自己目录下建子目录，不要直接堆在仓库根目录。

## 推送规则

| 项目 | 规则 |
| --- | --- |
| 分支 | `main` 为稳定分支，已禁止 force push 和删除；开发走 `feat/`、`fix/`、`docs/` 前缀分支 |
| 提交信息 | `type(scope): 说明`，type 用 `feat` / `fix` / `docs` / `refactor` / `chore` |
| 提交粒度 | 一个提交只做一件事，不要把无关改动混在一起 |
| 合并 | 通过 Pull Request 合入 `main`，用 Squash and merge |
| 禁止提交 | 编译产物、临时调试文件、密钥和密码、大体积数据包 |

```bash
git switch -c feat/xxx
git add -p
git commit -m "feat(xxx): 改了什么"
git push -u origin feat/xxx
```

## 文档维护要求

- 每个项目目录必须有 `README.md`：说明是什么、怎么编译运行、有哪些已知问题
- 改了代码接口，在同一次提交里同步更新相关文档
- 文档用 Markdown，一个文件一个一级标题，标题层级不跳级
- 图片放 `assets/`，文件名用英文小写加连字符，如 `servo-waveform-01.png`
- 过时文档标注"已归档"并指向替代文档，不要直接删除
- 提交前跑一遍检查，链接失效会让 CI 失败：

```bash
python tools/check_docs.py
```

CI 配置在 `.github/workflows/docs-check.yml`，推送到 `main` 或提 PR 时自动检查 Markdown 的相对链接、代码围栏和文件结尾换行。

## 维护人

[@goodalone-jhb](https://github.com/goodalone-jhb)
