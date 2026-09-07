---
wiki_id: MATHWIKI-LA-METHOD-002
type: method
title: 二次型 Rayleigh 商最值
subject: 线性代数
knowledge:
  - 二次型
  - 正定矩阵
  - 特征值与特征向量
  - Rayleigh 商
  - 广义 Rayleigh 商
  - 正交变换
methods:
  - 二次型矩阵化
  - 正定矩阵判定
  - Cholesky分解
  - 合同变换
  - 正交对角化
  - Rayleigh 商
  - 特征值最值
error_causes:
  - 方法调取失败
  - 目标识别断点
  - 条件忽略
triggers:
  - 二次型比值
  - 约束为 x^Tx
  - 分母为正定二次型
  - 实对称矩阵最值
source_refs:
  - 错题知识网络/可视化错题详情/线性代数/GS-425_强化例题9.15.md
  - 错题知识网络/错题卡/GS-424_强化例题13.30-2.md
  - 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-683_2022年22题.md
  - 错题知识网络/方法论库/方法卡/考研数学方法论卡片库_v2.md
wrongnet_refs:
  - GS-425
  - GS-424
  - MN4-GS-CH01-683
method_card_ids:
  - L09-011
wiki_refs:
  - MATHWIKI-LA-TOPIC-004
  - MATHWIKI-KNOWLEDGE-028
  - MATHWIKI-KNOWLEDGE-020
status: active
last_updated: 2026-07-03
---

# 二次型 Rayleigh 商最值

## 核心识别

看到二次型比值

$$
\frac{x^T A x}{x^T x}
$$

且 \(A\) 是实对称矩阵时，优先想到 Rayleigh 商：它的最小值和最大值分别对应 \(A\) 的最小、最大特征值。

如果分母不是 \(x^Tx\)，而是正定二次型 \(x^TBx\)，先不要直接套 \(A\) 的特征值。第一动作是把分母标准化：

$$
B=D^TD,\qquad z=Dx.
$$

再把广义商化成标准 Rayleigh 商。

## 方法链

1. 先把二次型写成 \(x^T A x\)，并确认 \(A\) 是实对称矩阵。
2. 做正交对角化：

   $$
   Q^T A Q=\Lambda,\quad x=Qy.
   $$

3. 利用正交变换保持长度：

   $$
   x^Tx=y^Ty.
   $$

4. 把比值化为加权平均：

   $$
   \frac{x^TAx}{x^Tx}
   =
   \frac{\lambda_1y_1^2+\cdots+\lambda_ny_n^2}{y_1^2+\cdots+y_n^2}.
   $$

5. 最值由特征值夹住：

   $$
   \lambda_{\min}\le \frac{x^TAx}{x^Tx}\le \lambda_{\max}.
   $$

## 正定分母的广义 Rayleigh 商

看到

$$
\frac{x^TAx}{x^TBx},\qquad B>0,
$$

按以下动作链处理：

1. 先判 \(B\) 正定。二阶矩阵可看顺序主子式，也可配方。
2. 找 \(D\)，使

   $$
   B=D^TD.
   $$

3. 令 \(z=Dx\)，即 \(x=D^{-1}z\)。
4. 分母变为

   $$
   x^TBx=(Dx)^T(Dx)=z^Tz.
   $$

5. 分子同步变为

   $$
   x^TAx=z^T(D^{-1})^TAD^{-1}z.
   $$

6. 最值转为矩阵 \((D^{-1})^TAD^{-1}\) 的最大或最小特征值。

## 易错点

- 第二问看到“最小值”后另起新方法，忘记第一问正交对角化已经给出特征值结构。
- 没有确认矩阵是实对称矩阵，就直接套 Rayleigh 商结论。
- 忘记正交变换保持 \(x^Tx\)，导致分母处理不清。
- 分母是 \(x^TBx\) 时，只求 \(A\) 的特征值，漏掉 \(B=D^TD\) 和 \(z=Dx\) 的标准化步骤。

## 关联

- 视觉候选：[MN4-GS-CH01-683｜2022年22题](http://127.0.0.1:8765/open/MN4-GS-CH01-683)
- 正式错题：[GS-425｜强化例题9.15](http://127.0.0.1:8765/open/GS-425)
- 高数交叉题：[GS-424｜强化例题13.30-2](http://127.0.0.1:8765/open/GS-424)，目标先平方化，再把二次型约束转为特征值倒数问题。
- 专题：[[MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线]]
- 方法卡：`L09-011`

## 复盘提醒

二次型最值题先看能不能写成 Rayleigh 商。若分母是 \(x^Tx\)，第一反应是特征值；若分母是正定二次型 \(x^TBx\)，先标准化分母，再求新矩阵的特征值。
