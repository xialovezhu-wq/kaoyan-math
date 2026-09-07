---
wiki_id: MATHWIKI-GS-METHOD-099
type: method
title: 复合三角积分中间量比较链
subject: 高等数学
knowledge:
  - 定积分
  - 定积分性质
  - 函数单调性
  - 单调性比较
  - 三角不等式
  - 三角函数单调性
methods:
  - 中间量比较
  - 点态比较
  - 积分保序
  - 三角函数单调性
  - 定积分大小估计
error_causes:
  - 题型识别失败
  - 方法论调取失败
  - 触发信息遗漏
  - 换元路径锁定
  - 中间量引入缺失
triggers:
  - 复合三角函数定积分
  - 只比较积分大小
  - 内层为 \(\sin x\)
  - 基准值来自 \(\int\sin x\) 或 \(\int\cos x\)
source_refs:
  - 错题知识网络/错题卡/GS-662_57909复合三角积分比较.md
  - 错题知识网络/可视化错题详情/高等数学/GS-662_57909复合三角积分比较.md
wrongnet_refs:
  - GS-662
method_card_ids:
  - 待匹配
wiki_refs:
  - MATHWIKI-GS-TOPIC-005
  - MATHWIKI-GS-TOPIC-006
status: active
last_updated: 2026-07-04
---

# 复合三角积分中间量比较链

## 定位

这类题给出不能直接初等积分的复合被积函数，但目标只是比较大小。稳定入口不是先换元，而是先找一个熟悉中间量，把被积函数和可积基准函数做点态比较。

## 第一动作

| 题面信号 | 先做动作 | 后续判断 |
|---|---|---|
| \(\sin(\sin x)\)、\(\cos(\sin x)\) | 先写 \(0<\sin x<x<\frac\pi2\) | 再分别使用外层 \(\sin,\cos\) 的单调性 |
| 选项含 \(1\) | 想到 \(\int_0^{\pi/2}\sin xdx=1\) 与 \(\int_0^{\pi/2}\cos xdx=1\) | 把 \(1\) 变成比较基准 |
| 只问大小关系 | 优先点态比较，再积分保序 | 暂不进入复杂换元 |

## 方法链

以 [GS-662](http://127.0.0.1:8765/open/GS-662) 为例，先用三角不等式：

\[
0<\sin x<x<\frac\pi2.
\]

对 \(I_1\)，外层 \(\sin u\) 递增：

\[
\sin(\sin x)<\sin x
\quad\Longrightarrow\quad
I_1<\int_0^{\pi/2}\sin x\,dx=1.
\]

对 \(I_2\)，外层 \(\cos u\) 递减：

\[
\sin x<x
\quad\Longrightarrow\quad
\cos(\sin x)>\cos x
\quad\Longrightarrow\quad
I_2>\int_0^{\pi/2}\cos x\,dx=1.
\]

因此
\[
I_1<1<I_2.
\]

## 典型断点

- 看到 \(\sin(\sin x)\) 后机械换元，换成 \(t=\sin x\) 后出现 \(\arcsin t\) 或 \(\sqrt{1-t^2}\)，问题被人为复杂化。
- 只比较 \(\sin x\) 和 \(\cos x\) 在两段区间的大小，没有把内层 \(\sin x\) 与 \(x\) 比较。
- 记得 \(x>\sin x\)，但没有把它作为复合函数比较的中间桥梁。
- 忘记外层 \(\cos u\) 是递减函数，比较方向会反过来。

## 代表题

| 题号 | 题型信号 | 第一动作 | 复做提醒 |
|---|---|---|---|
| [GS-662](http://127.0.0.1:8765/open/GS-662) | \(I_1=\int\sin(\sin x)dx\)，\(I_2=\int\cos(\sin x)dx\)，比较与 \(1\) 的大小 | 先写 \(0<\sin x<x<\frac\pi2\) | \(1\) 来自 \(\int\sin x\) 和 \(\int\cos x\)；外层 \(\sin\) 递增，外层 \(\cos\) 递减。 |

## 关联

- 总线：[[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]、[[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- 待匹配方法卡：复合函数积分比较 / 中间量点态比较
