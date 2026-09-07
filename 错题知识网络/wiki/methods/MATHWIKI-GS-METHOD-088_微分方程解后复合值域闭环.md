---
wiki_id: MATHWIKI-GS-METHOD-088
type: method
title: 微分方程解后复合值域闭环
subject: 高等数学
knowledge:
  - 微分方程
  - 一阶线性微分方程
  - 单调性与极值
  - 复合函数求导
methods:
  - 积分因子
  - 复合函数换元
  - 导数判极值
  - 值域求解
error_causes:
  - 暂无明确个人错因
  - 解出微分方程后未继续处理目标函数
  - 复合自变量范围遗漏
triggers:
  - 解微分方程后要求复合函数值域
  - 目标含有 y(x^2) 或其他限制自变量
  - 解出 y(x) 不是整题终点
source_refs:
  - 错题知识网络/错题卡/GS-191_1000题B组5.22.md
  - 错题知识网络/可视化错题详情/高等数学/GS-191_1000题B组5.22.md
wrongnet_refs:
  - GS-191
wiki_refs:
  - MATHWIKI-GS-TOPIC-009
status: active
last_updated: 2026-07-03
---

# 微分方程解后复合值域闭环

微分方程综合题常见断点是：方程解出来以后就停了。但如果题目问的是 \(y(x^2)\) 的值域，解方程只是第一段，后面还要把复合自变量范围单独处理。

$$
\text{先解微分方程}
\Longrightarrow
\text{写清复合自变量范围}
\Longrightarrow
\text{转成一元函数极值}.
$$

## 第一动作

对 [GS-191](http://127.0.0.1:8765/open/GS-191)，先把一阶线性微分方程解出：

$$
y'+y=e^{-x}\cos x,\qquad y(0)=0.
$$

使用积分因子后得到：

$$
y=e^{-x}\sin x.
$$

但题目目标是 \(y(x^2)\)，所以必须另设：

$$
t=x^2,\qquad t\ge0.
$$

问题变成求：

$$
g(t)=e^{-t}\sin t,\qquad t\ge0
$$

的值域。

## 极值闭环

对 \(g(t)\) 求导：

$$
g'(t)=e^{-t}(\cos t-\sin t).
$$

驻点满足：

$$
\cos t-\sin t=0
\Longleftrightarrow
t=\frac{\pi}{4}+k\pi.
$$

由于 \(e^{-t}\) 衰减，最大正值出现在第一个正峰：

$$
t=\frac{\pi}{4},
\qquad
g(t)=\frac{\sqrt2}{2}e^{-\pi/4}.
$$

最小负值出现在第一个负谷：

$$
t=\frac{5\pi}{4},
\qquad
g(t)=-\frac{\sqrt2}{2}e^{-5\pi/4}.
$$

## 对应题

| 题号 | 题型信号 | 第一动作 | 复做提醒 |
|---|---|---|---|
| [GS-191](http://127.0.0.1:8765/open/GS-191) | 一阶线性微分方程 + \(y(x^2)\) 值域 | 先解 \(y\)，再令 \(t=x^2\ge0\) | 解出 \(y=e^{-x}\sin x\) 后不能停；目标函数已经限制成 \(t\ge0\)。 |

## 最短提醒

$$
\text{微分方程解出来以后，按题目真正问的对象继续闭环。}
$$

关联：[[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
