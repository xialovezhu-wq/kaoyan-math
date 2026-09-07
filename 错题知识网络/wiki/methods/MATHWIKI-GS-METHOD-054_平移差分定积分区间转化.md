---
wiki_id: MATHWIKI-GS-METHOD-054
type: method
title: 平移差分定积分区间转化
subject: 高等数学
knowledge:
  - 定积分
  - 定积分等式
  - 一元函数积分学的计算
methods:
  - 定积分区间可加性
  - 区间平移
  - 定积分换元
  - 平移差分关系
  - 定积分等式
triggers:
  - f(x+T)-f(x)
  - 相邻平移区间积分
  - 已知某段积分为零
  - 求偏移后的定积分
source_refs:
  - 错题知识网络/错题卡/GS-186_2023年第15题.md
  - 错题知识网络/可视化错题详情/高等数学/GS-186_2023年第15题.md
wrongnet_refs:
  - GS-186
method_card_ids:
  - H11-001
  - H11-002
wiki_refs:
  - MATHWIKI-GS-TOPIC-006
status: active
last_updated: 2026-07-02
---

# 平移差分定积分区间转化

## 定位

本页沉淀 \(f(x+T)-f(x)\) 型定积分题的入口。题目不要求求出 \(f(x)\)，而是让目标积分区间通过拆补和平移，变成平移前后函数值之差的积分。

## 第一动作

看到

$$
f(x+T)-f(x)=g(x)
$$

并且要求某个偏移区间上的

$$
\int_\alpha^\beta f(x)\,dx,
$$

先检查能否把目标区间拆成两个相差 \(T\) 的同长区间之差：

$$
\int_{a+T}^{b+T} f(x)\,dx-\int_a^b f(x)\,dx.
$$

若能做到，立刻令 \(x=u+T\)，得到

$$
\int_{a+T}^{b+T} f(x)\,dx=\int_a^b f(u+T)\,du,
$$

于是

$$
\int_a^b \bigl[f(u+T)-f(u)\bigr]\,du=\int_a^b g(u)\,du.
$$

## 方法链

1. 先用定积分区间可加性，把目标区间拆补到包含已知积分区间。
2. 用已知积分值消掉多余区间。
3. 把剩余部分整理成“平移后区间积分 - 原区间积分”。
4. 对平移后区间换元，把积分区间拉回原区间。
5. 套用 \(f(u+T)-f(u)=g(u)\)，最后只计算 \(g(u)\) 的积分。

## 典型模板

若已知

$$
\int_a^{a+T} f(x)\,dx=0,
$$

目标区间刚好跨过这段区间，可以先拆补：

$$
\int_{\alpha}^{\beta} f(x)\,dx
=\int_{a+T}^{b+T} f(x)\,dx-\int_a^b f(x)\,dx.
$$

再平移换元：

$$
\int_{a+T}^{b+T} f(x)\,dx-\int_a^b f(x)\,dx
=\int_a^b \bigl[f(u+T)-f(u)\bigr]\,du.
$$

## 对应错题

- [GS-186](http://127.0.0.1:8765/open/GS-186)：由 \(f(x+2)-f(x)=x\) 与 \(\int_0^2 f(x)\,dx=0\)，求 \(\int_1^3 f(x)\,dx\)。

## 常见断点

- 看到函数方程后试图解出 \(f(x)\)，没有把它当成差分关系使用。
- 知道 \(\int_0^2 f=0\)，但没有把目标区间拆补到 \([0,2]\)。
- 平移换元后忘记 \(dx=du\)，或没有同步改上下限。
- 变量换名后仍写成旧变量，导致 \(f(x+2)-f(x)\) 与积分变量混乱。

## 关联

- 专题：[[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- 相关方法：[[MATHWIKI-GS-METHOD-003_整体函数奇偶性检查]]、[[MATHWIKI-GS-METHOD-040_绝对三角周期积分]]
- 方法卡：`H11-001`、`H11-002`
