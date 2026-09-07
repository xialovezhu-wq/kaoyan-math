---
wiki_id: MATHWIKI-GS-METHOD-012
type: method
title: 等价无穷小使用条件
subject: 高等数学
knowledge:
  - 等价无穷小
  - 无穷小阶数比较
  - 极限与连续
  - 幂指极限
  - 函数极限
methods:
  - 等价变形
  - 主导项比较
  - 公共因子提取
  - 小 o 定义转换
  - 反例检验
error_causes:
  - 条件忽略
  - 方法选择错误
triggers:
  - 加减式先看主项
  - 平方等价反推原量等价
source_refs:
  - 错题知识网络/错题卡/GS-003_22026.3.11T1-2.md
  - 错题知识网络/可视化错题详情/高等数学/GS-003_2-2026.3.11-T1-2.md
  - 错题知识网络/wiki/topics/knowledge_clusters/MATHWIKI-KNOWLEDGE-004_等价无穷小.md
  - 错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度.md
  - 错题知识网络/wiki/sources/wrong_cards/SRC-WQ-GS-014.md
wrongnet_refs:
  - GS-003
  - GS-014
  - GS-005
  - GS-016
  - GS-436
  - GS-438
  - GS-440
  - GS-455
wiki_refs:
  - MATHWIKI-KNOWLEDGE-004
  - MATHWIKI-KNOWLEDGE-041
  - MATHWIKI-KNOWLEDGE-099
  - MATHWIKI-GS-TOPIC-004
  - MATHWIKI-GS-METHOD-041
status: active
last_updated: 2026-07-02
---

# 等价无穷小使用条件

等价无穷小不是“看到小量就替换”。它的第一判断是结构位置：乘除型可以优先替换，加减型必须先看主项是否抵消。

## 第一动作

1. 先确认趋向点和小量是谁。
2. 再判断结构是乘除、复合、加减还是幂指。
3. 如果是加减式，先展开到能看主项，不直接逐项替换。
4. 如果有参数、绝对值、左右趋向，先处理边界。
5. 如果有非零因子或公共尺度，先把它提出，再对剩余小量做等价。

## 常见失误

- 把等价无穷小当成恒等式。
- 在加减抵消结构中直接替换，导致主项丢失。
- 忽略小量趋向条件，例如变量并不趋向 0。
- 忘记幂指结构先取对数或转指数。
- 底数趋非 \(1\) 常数时，没有先提出常数幂，例如把 \((3+2\tan x)^x\) 直接当 \(1+o(1)\) 处理。
- 由 \(\alpha^2\sim\beta^2\) 直接反推 \(\alpha\sim\beta\)，漏掉 \(\frac{\alpha}{\beta}\to-1\) 的反例可能。

## 等价关系与小 o 关系命题判断

命题判断题的第一动作不是套泰勒，而是先回定义：

$$
\alpha\sim\beta
\Longleftrightarrow
\lim\frac{\alpha}{\beta}=1,
$$

$$
\alpha-\beta=o(\alpha)
\Longleftrightarrow
\lim\frac{\alpha-\beta}{\alpha}=0.
$$

对这类题要特别区分“可逆”和“不可逆”：

| 关系 | 判断 |
|---|---|
| \(\alpha\sim\beta\Rightarrow \alpha^2\sim\beta^2\) | 真，直接平方极限 |
| \(\alpha^2\sim\beta^2\Rightarrow \alpha\sim\beta\) | 假，只能推出绝对值尺度一致，不能排除符号相反 |
| \(\alpha\sim\beta\Rightarrow \alpha-\beta=o(\alpha)\) | 真，写成 \(1-\frac{\beta}{\alpha}\to0\) |
| \(\alpha-\beta=o(\alpha)\Rightarrow \alpha\sim\beta\) | 真，先得 \(\frac{\beta}{\alpha}\to1\)，再取倒数 |

典型反例是

$$
\alpha(x)=-x,\qquad \beta(x)=x.
$$

它满足 \(\alpha^2\sim\beta^2\)，但 \(\alpha/\beta=-1\)，所以不能推出 \(\alpha\sim\beta\)。来源：[GS-014](http://127.0.0.1:8765/open/GS-014)。

## 与主量尺度的关系

等价无穷小常常不是第一步，而是第二步：

| 结构 | 先做 | 再做 |
|---|---|---|
| \(\sqrt{1+x^2}\to1\) 的非零因子 | 先确认它只贡献稳定主量 | 对剩余 \(0-0\) 部分做等价或洛必达 |
| \((3+2\tan x)^x\) | 先提出 \(3^x\) | 对 \(\left(1+\frac{2\tan x}{3}\right)^x\) 处理指数小量 |
| \(e^A-e^B\)，且 \(A,B\to1\) | 先用中值定理合并差值 | 对 \(A-B\) 做等价 |
| \(\frac1x\int_0^xF(t)\,dt\) | 先用洛必达转端点函数 | 对端点函数中的括号小量做等价 |
| \(\frac1{e^x-1}-\frac1{\sin x}\) | 先通分成 \(\frac{\sin x-(e^x-1)}{\sin x(e^x-1)}\) | 展开到二阶，不能只用 \(\sin x\sim x,\ e^x-1\sim x\) |

## 加减抵消中的展开阶数

在加减抵消结构里，最低阶项可能会被消掉，因此展开阶数要覆盖第一个非零项。以 [GS-003](http://127.0.0.1:8765/open/GS-003) 的局部极限为例：

\[
\frac1{e^x-1}-\frac1{\sin x}
=
\frac{\sin x-(e^x-1)}{\sin x(e^x-1)}.
\]

此时只写 \(\sin x\sim x\)、\(e^x-1\sim x\) 会得到 \(0/0\) 的空信息。必须继续写

\[
\sin x=x-\frac{x^3}{6}+o(x^3),
\qquad
e^x-1=x+\frac{x^2}{2}+o(x^2),
\]

所以分子主项为 \(-\frac{x^2}{2}\)，分母主项为 \(x^2\)，局部极限为 \(-\frac12\)。

## 相关页面

- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-METHOD-006_先判型总流程]]
- [[MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度]]
- [[MATHWIKI-GS-METHOD-007_条件转化总流程]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-099_无穷小阶数比较]]
