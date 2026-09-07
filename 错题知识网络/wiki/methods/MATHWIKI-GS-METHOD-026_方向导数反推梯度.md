---
wiki_id: MATHWIKI-GS-METHOD-026
type: method
title: 方向导数反推梯度
subject: 高等数学
knowledge:
  - 多元函数微分学
  - 方向导数
  - 梯度
  - 方向向量
source_refs:
  - 错题知识网络/知识树/高等数学18讲第17讲_多元函数积分学预备知识.md
  - 错题知识网络/方法论库/方法卡/考研数学方法论卡片库_v2.md
  - 错题知识网络/错题卡/GS-654_89961方向导数反推梯度.md
wrongnet_refs:
  - GS-654
wiki_refs:
  - MATHWIKI-GS-TOPIC-010
  - MATHWIKI-GS-METHOD-024
  - MATHWIKI-GS-METHOD-025
method_card_ids:
  - H17-001
  - H17-003
  - MATHWIKI-GS-METHOD-044
status: active
last_updated: 2026-07-02
---

# 方向导数反推梯度

## 题面信号

看到：

- 给出同一点处沿两个不同方向的方向导数；
- 只知道方向导数数值，没有给出 \(f(x,y)\) 的具体表达式；
- 问该点的最大方向导数；
- 给出 \(P_0\) 到其他点的方向，而不是直接给单位向量。

## 第一动作

先把点处梯度设成未知向量：

$$
\nabla f(P_0)=(a,b).
$$

然后把每个已知方向导数写成：

$$
D_{\mathbf e_i}f(P_0)=\nabla f(P_0)\cdot\mathbf e_i.
$$

其中 \(\mathbf e_i\) 是第 \(i\) 个方向的单位方向向量。

## 动作链

1. 由两点差求方向向量：

$$
\overrightarrow{P_0P_i}=(x_i-x_0,y_i-y_0).
$$

2. 单位化：

$$
\mathbf e_i=\frac{\overrightarrow{P_0P_i}}{\left|\overrightarrow{P_0P_i}\right|}.
$$

3. 设梯度：

$$
\nabla f(P_0)=(a,b).
$$

4. 对每个方向导数列方程：

$$
(a,b)\cdot\mathbf e_i=D_{\mathbf e_i}f(P_0).
$$

5. 两个非共线方向给两个独立方程，解出 \(a,b\)。

6. 最大方向导数为：

$$
\max D_{\mathbf e}f(P_0)=|\nabla f(P_0)|.
$$

## 常见断点

- 忘记先把两点确定的方向向量单位化。
- 只记得方向导数公式，但没有想到把梯度设成未知量。
- 把两个方向导数当成两个孤立数值，没有列成线性方程组。
- 求出梯度后忘记题目问的是最大方向导数，应取梯度模。
- 忽略“两个方向不共线”这个保证方程组可唯一确定二维梯度的条件。

## 关联

- 总判别链：[[MATHWIKI-GS-METHOD-044_方向导数与梯度入口判别链]]

## 复做提醒

看到“已知两个方向导数，求最大方向导数”，先设梯度为未知向量，再把两个方向单位化并点乘列方程；解出梯度后，最大方向导数就是梯度模。
