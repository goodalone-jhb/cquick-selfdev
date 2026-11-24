# assets · 图片资源

放文档和说明里引用的图片，不放代码和数据。

## 放什么

- 电路原理图、PCB 截图
- 实物照片、装配示意
- 波形、曲线、比赛截图
- 上位机界面截图

## 不放什么

- 原始数据集、训练数据
- 视频、模型权重、压缩包
- 单张超过 1MB 的大图（先压缩或裁剪）

## 命名

`<主题>-<类型>-<序号或日期>.<扩展名>`，全英文小写加连字符：

```text
joint-node-block-diagram-01.png
ethercat-chain-topology.png
servo-waveform-20261124.png
field-detection-result-01.jpg
```

## 引用方式

在 Markdown 里用相对路径引用，例如从 `electronics/projects/joint-node/README.md` 引用：

```markdown
![节点框图](../../../assets/joint-node-block-diagram-01.png)
```

图片一定要写 alt 文本，说明图里是什么内容。
