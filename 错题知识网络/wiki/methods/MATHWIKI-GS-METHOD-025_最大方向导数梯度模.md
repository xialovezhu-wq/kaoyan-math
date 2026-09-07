---
wiki_id: MATHWIKI-GS-METHOD-025
type: method
title: 最大方向导数梯度模
subject: 高等数学
knowledge:
  - 多元函数微分学
  - 方向导数
  - 梯度
  - 方向向量
source_refs:
  - 错题知识网络/知识树/高等数学18讲第17讲_多元函数积分学预备知识.md
  - 错题知识网络/方法论库/方法卡/考研数学方法论卡片库_v2.md
  - 错题知识网络/错题卡/GS-653_102591最大方向导数梯度模.md
  - 错题知识网络/错题卡/GS-657_171552最大方向导数比例条件.md
wrongnet_refs:
  - GS-653
  - GS-657
wiki_refs:
  - MATHWIKI-GS-TOPIC-010
  - MATHWIKI-GS-METHOD-024
  - MATHWIKI-GS-METHOD-029
method_card_ids:
  - H17-003
  - MATHWIKI-GS-METHOD-044
status: active
last_updated: 2026-07-02
---

# 最大方向导数梯度模

## 题面信号

看到：

- 方向导数最大；
- 增长最快方向；
- 沿某方向方向导数最大；
- 方向导数最大值为某个数；
- 反求参数 \(a,b\)。

## 第一动作

先写：

$$
D_{\mathbf e}f(P)=\nabla f(P)\cdot\mathbf e
=|\nabla f(P)|\cos\theta.
$$

所以：

$$
\max D_{\mathbf e}f(P)=|\nabla f(P)|,
\qquad
\mathbf e_{\max}\parallel \nabla f(P).
$$

## 动作链

1. 先判断函数有几个自变量。

若是

$$
z=f(x,y),
$$

则

$$
\nabla z=(z_x,z_y).
$$

若是

$$
u=f(x,y,z),
$$

则

$$
\nabla u=(u_x,u_y,u_z).
$$

2. 求点处梯度 \(\nabla f(P)\)。

3. 若题目给“最大方向”为 \(\mathbf v\)，先单位化：

$$
\mathbf e=\frac{\mathbf v}{|\mathbf v|}.
$$

4. 若最大值为 \(M\)，建立：

$$
\nabla f(P)=M\mathbf e.
$$

5. 按分量列方程，反求参数。

## 常见断点

- 知道梯度方向是增加最快方向，但不知道最大方向导数为什么等于梯度模。
- 忘记从点积公式推出 \(D_{\mathbf e}f=|\nabla f|\cos\theta\)。
- 把 \(z=f(x,y)\) 的二维梯度误当成三维梯度。
- 把移项后的 \(F(x,y,z)=0\) 的三元梯度误当成原函数方向导数的梯度。
- 只写 \(|\nabla f|=M\)，漏写梯度和给定最大方向同向。
- 含参数题中，比例比较对象是点处梯度分量，不是参数本身；例如应比较 \((4a,2b)\) 与方向 \((1,2)\)。

## 关联

- 总判别链：[[MATHWIKI-GS-METHOD-044_方向导数与梯度入口判别链]]

## 复做提醒

看到“方向导数最大/增长最快方向”，先判断自变量维数，再写：

$$
\text{最大方向}=\nabla f(P)\text{ 的方向},\qquad
\text{最大值}=|\nabla f(P)|.
$$

若题目给的是 \(z=f(x,y)\)，不要把 \(z\) 当自变量；移项成 \(F=0\) 后的 \(\nabla F\) 是曲面法向量。
