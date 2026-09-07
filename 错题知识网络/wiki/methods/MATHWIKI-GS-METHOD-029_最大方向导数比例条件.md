---
wiki_id: MATHWIKI-GS-METHOD-029
type: method
title: 最大方向导数比例条件
subject: 高等数学
knowledge:
  - 多元函数微分学
  - 方向导数
  - 梯度
  - 方向向量
source_refs:
  - 错题知识网络/知识树/高等数学18讲第17讲_多元函数积分学预备知识.md
  - 错题知识网络/方法论库/方法卡/考研数学方法论卡片库_v2.md
  - 错题知识网络/错题卡/GS-657_171552最大方向导数比例条件.md
wrongnet_refs:
  - GS-653
  - GS-657
wiki_refs:
  - MATHWIKI-GS-TOPIC-010
  - MATHWIKI-GS-METHOD-024
  - MATHWIKI-GS-METHOD-025
method_card_ids:
  - H17-003
  - MATHWIKI-GS-METHOD-044
status: active
last_updated: 2026-07-02
---

# 最大方向导数比例条件

## 题面信号

看到：

- 在某点处，沿给定方向的方向导数最大；
- 同时给出最大方向导数的最大值；
- 函数含参数，要求反求参数；
- 方向向量形如 \(l=i+2j\)、\(l=(-3,-4)\) 等。

## 第一动作

先写点处梯度，再写两个条件：

$$
\nabla f(P)\parallel l,
\qquad
|\nabla f(P)|=M.
$$

如果方向向量 \(l\) 不是单位向量，先单位化：

$$
\mathbf e=\frac{l}{|l|}.
$$

此时可以直接写：

$$
\nabla f(P)=M\mathbf e.
$$

## 动作链

1. 求点处梯度，例如：

$$
\nabla f(2,1)=(4a,2b).
$$

2. 把给定方向单位化：

$$
\mathbf e=\frac{l}{|l|}.
$$

3. 用“最大方向同向 + 最大值为模长”建立向量方程：

$$
\nabla f(P)=M\mathbf e.
$$

4. 按分量列方程反求参数。

如果先用点乘式：

$$
\nabla f(P)\cdot\mathbf e=M,
$$

这通常只给出一个数量方程。还必须继续使用

$$
\nabla f(P)\parallel l.
$$

## 常见断点

- 只用了点乘方程，忘记“最大方向”还给出梯度同向条件。
- 把参数向量 \((a,b)\) 当作梯度向量，比例比较对象错了。
- 比例应比较 \(\nabla f(P)\) 的分量，例如 \((4a,2b)\) 与 \((1,2)\)，不是比较原始参数 \((a,b)\)。
- 忘记同向要求比例常数为正；反向会对应方向导数最小值。

## 关联

- 总判别链：[[MATHWIKI-GS-METHOD-044_方向导数与梯度入口判别链]]

## 复做提醒

看到“沿某方向方向导数最大”，不要只写一个点乘等式。先写：

$$
\nabla f(P)\parallel l,\qquad |\nabla f(P)|=M.
$$

列比例时，比例比较对象一定是点处梯度的各分量。
