---
wiki_id: MATHWIKI-GS-METHOD-055
type: method
title: 参数方程二阶导链式求导
subject: 高等数学
knowledge:
  - 一元函数微分学应用
  - 参数方程求导
  - 高阶导数
  - 复合函数求导
methods:
  - 参数方程求导
  - 参数方程二阶导
  - 链式求导
  - 先化简再求导
triggers:
  - x=x(t), y=y(t)
  - 求 d2y/dx2
  - 参数方程确定 y=y(x)
  - 参数曲线求凹凸或曲率
source_refs:
  - 错题知识网络/错题卡/GS-123_2021年第12题（数学2）.md
  - 错题知识网络/可视化错题详情/高等数学/GS-123_2021年第12题（数学2）.md
  - 错题知识网络/错题卡/GS-499_57905参数二阶导凹凸.md
  - 错题知识网络/错题卡/GS-650_57838参数曲线曲率链式求导.md
  - 错题知识网络/错题卡/GS-169_2018年第12题.md
  - 错题知识网络/可视化错题详情/高等数学/GS-169_2018年第12题.md
wrongnet_refs:
  - GS-123
  - GS-499
  - GS-650
  - GS-169
  - GS-579
wiki_refs:
  - MATHWIKI-GS-TOPIC-005
  - MATHWIKI-GS-METHOD-047
method_card_ids:
  - H04-007
status: active
last_updated: 2026-07-02
---

# 参数方程二阶导链式求导

## 定位

看到参数方程

$$
\begin{cases}
x=x(t),\\
y=y(t)
\end{cases}
$$

并要求

$$
\frac{d^2y}{dx^2},
$$

第一反应不是“对 \(t\) 连续求两次导”，而是先把导数对象固定为关于 \(x\) 的导数。

## 第一动作

先写一阶导：

$$
\frac{dy}{dx}
=
\frac{dy/dt}{dx/dt}
=
\frac{y'(t)}{x'(t)}.
$$

设

$$
\varphi(t)=\frac{dy}{dx}.
$$

二阶导必须再除一次 \(x'(t)\)：

$$
\frac{d^2y}{dx^2}
=
\frac{d}{dx}\left(\frac{dy}{dx}\right)
=
\frac{\frac{d}{dt}\varphi(t)}{dx/dt}
=
\frac{\varphi'(t)}{x'(t)}.
$$

## 方法链

1. 先求 \(x'(t)\)、\(y'(t)\)，确认 \(x'(t)\neq0\) 的局部范围。
2. 写

$$
\frac{dy}{dx}=\frac{y'(t)}{x'(t)}.
$$

3. 若一阶导可以约分，先约到最简形式。
4. 对已经化简的 \(\frac{dy}{dx}\) 关于 \(t\) 求导。
5. 最后除以 \(x'(t)\)，得到 \(\frac{d^2y}{dx^2}\)。
6. 若题目要求某个 \(t_0\)，最后再代 \(t=t_0\)。

## 省算检查

参数方程二阶导题常常故意让一阶导大幅约分。先化简能减少后续商法则计算。

例如 [GS-123](http://127.0.0.1:8765/open/GS-123) 中：

$$
\frac{dy}{dx}
=
\frac{4te^t+2t}{2e^t+1}
=
t\cdot\frac{4e^t+2}{2e^t+1}
=2t.
$$

于是

$$
\frac{d^2y}{dx^2}
=
\frac{\frac{d}{dt}(2t)}{2e^t+1},
$$

而不是对原来的大分式硬套商法则。

## 常见断点

- 把 \(\frac{d}{dt}\left(\frac{dy}{dx}\right)\) 直接当成 \(\frac{d^2y}{dx^2}\)。
- 求完 \(\frac{dy}{dx}\) 后没有先化简，导致二阶导计算量扩大。
- 参数区间、凹凸区间或拐点坐标最终要回到 \(x\) 或点坐标时，忘记代回 \(x=x(t)\)。
- 曲率题若走普通函数曲率公式，里面的 \(y'\)、\(y''\) 都必须是关于 \(x\) 的导数。

## 对应错题

| 题号 | 题型定位 | 第一动作 | 复做提醒 |
|---|---|---|---|
| [GS-123](http://127.0.0.1:8765/open/GS-123) | 参数方程直接求 \(\left.\frac{d^2y}{dx^2}\right|_{t=0}\) | 先求 \(\frac{dy}{dx}\)，约成 \(2t\) | 二阶导是 \(\frac{\frac{d}{dt}(dy/dx)}{x'(t)}\)，不是只对 \(t\) 求导。 |
| [GS-499](http://127.0.0.1:8765/open/GS-499) | 参数方程单调凹凸和拐点 | 先求 \(\frac{dy}{dx}\)、\(\frac{d^2y}{dx^2}\)，再把 \(t\) 区间转成 \(x\) 区间 | 参数区间不等于 \(x\) 区间。 |
| [GS-650](http://127.0.0.1:8765/open/GS-650) | 参数曲线曲率 | 若用普通曲率公式，先确保 \(y'\)、\(y''\) 都是对 \(x\) 的导数 | 求 \(y''\) 时补 \(\frac{dt}{dx}=\frac1{x'(t)}\)。 |
| [GS-169](http://127.0.0.1:8765/open/GS-169) | 参数方程 \(x=\cos^3t,\ y=\sin^3t\) 求指定参数处曲率 | 先求 \(y'=\frac{dy/dt}{dx/dt}\)，再用 \(y''=\frac{\frac{d}{dt}(y')}{dx/dt}\) | 曲率公式里的 \(y'\)、\(y''\) 都是关于 \(x\) 的导数。 |

## 关联

- 专题：[[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- 曲率变量对象：[[MATHWIKI-GS-METHOD-047_曲率题变量对象判别链]]
- 动作链断点：[[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- 方法卡：`H04-007`
