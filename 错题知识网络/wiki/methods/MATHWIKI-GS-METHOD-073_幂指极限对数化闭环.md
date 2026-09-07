---
wiki_id: MATHWIKI-GS-METHOD-073
type: method
title: 幂指极限对数化闭环
subject: 高等数学
knowledge:
  - 极限与连续
  - 函数极限
  - 数列极限
  - 幂指极限
  - 等价无穷小
  - 洛必达法则
methods:
  - 幂指极限对数化
  - 取对数
  - 指数还原
  - 洛必达法则
error_causes:
  - 方法论调取失败
  - 题型识别失败
  - 过程跳步
source_refs:
  - 错题知识网络/错题卡/GS-165_2019年第1题.md
  - 错题知识网络/可视化错题详情/高等数学/GS-165_2019年第1题.md
  - 错题知识网络/错题卡/GS-075_强化例题2.10.md
  - 错题知识网络/可视化错题详情/高等数学/GS-075_强化例题2.10.md
  - 错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md
wrongnet_refs:
  - GS-165
  - GS-436
  - GS-075
wiki_refs:
  - MATHWIKI-GS-TOPIC-004
  - MATHWIKI-GS-TOPIC-007
  - MATHWIKI-GS-METHOD-006
  - MATHWIKI-GS-METHOD-012
  - MATHWIKI-GS-METHOD-041
status: active
last_updated: 2026-07-04
---

# 幂指极限对数化闭环

本页处理 \(u(x)^{v(x)}\) 型极限，尤其是底数趋向非 \(1\) 常数、指数趋于无穷或含 \(\frac1x\) 的情况。核心不是把底数和指数分别求极限，而是先取对数，把幂指式变成乘积或商式极限。

## 第一动作

看到

$$
\lim u(x)^{v(x)}
$$

先设

$$
y=u(x)^{v(x)},\qquad \ln y=v(x)\ln u(x).
$$

然后计算

$$
L=\lim v(x)\ln u(x),
$$

最后指数还原：

$$
\lim y=e^L.
$$

## 适用条件

- 底数 \(u(x)>0\) 的邻域要能保证对数有意义。
- 不能把 \(\lim u(x)\) 与 \(\lim v(x)\) 分别算完就代入；幂指未定式的有效对象是 \(v(x)\ln u(x)\)。
- 若取对数后出现 \(0/0\) 或 \(\infty/\infty\)，再决定洛必达、泰勒或等价无穷小。
- 算完 \(L\) 以后必须回到原极限 \(e^L\)，不要把 \(\ln y\) 的极限当作原题答案。

## 代表题：GS-165

来源：[GS-165](http://127.0.0.1:8765/open/GS-165)。

$$
\lim_{x\to0}(x+2^x)^{2/x}
$$

设

$$
y=(x+2^x)^{2/x}.
$$

则

$$
\ln y=\frac{2}{x}\ln(x+2^x).
$$

因为 \(x\to0\) 时

$$
\ln(x+2^x)\to \ln 1=0,
$$

所以

$$
L=\lim_{x\to0}\ln y
=\lim_{x\to0}\frac{2\ln(x+2^x)}{x}
$$

是 \(0/0\) 型。用洛必达：

$$
L
=2\lim_{x\to0}\frac{1+2^x\ln2}{x+2^x}
=2(1+\ln2).
$$

于是

$$
\lim_{x\to0}(x+2^x)^{2/x}
=e^L
=e^{2(1+\ln2)}
=4e^2.
$$

## 代表题：GS-075

来源：[GS-075](http://127.0.0.1:8765/open/GS-075)。

数列型幂指极限同样先指数化。第一步不是直接处理

$$
b_n^{\frac{\ln\cos b_n}{n}},
$$

而是先从题设关系和余弦单调性得到

$$
0<b_n<a_n\to0,
$$

从而 \(b_n\to0^+\)。随后写成

$$
b_n^{\frac{\ln\cos b_n}{n}}
=\exp\left(\frac{\ln\cos b_n}{n}\ln b_n\right).
$$

由

$$
(1-b_n)^n=\cos b_n
$$

得到

$$
\frac{\ln\cos b_n}{n}=\ln(1-b_n).
$$

所以指数中的核心量是

$$
\ln(1-b_n)\ln b_n
\sim -b_n\ln b_n\to0.
$$

最后指数还原：

$$
\lim_{n\to\infty}b_n^{\frac{\ln\cos b_n}{n}}
=e^0=1.
$$

## 易错闭环

| 断点 | 正确处理 |
|---|---|
| 直接把底数和指数分开代入 | 先取对数，研究 \(v(x)\ln u(x)\) |
| 取对数后忘记指数还原 | 最后答案必须是 \(e^L\) |
| 把 \(0/0\) 型直接跳过 | 取对数后的普通极限再用洛必达、泰勒或等价 |
| 底数趋非 \(1\) 常数时忽略常数贡献 | 先稳定底数主量，再处理指数尺度 |

## 与其他方法页的关系

- 总入口：[[MATHWIKI-GS-METHOD-006_先判型总流程]]
- 等价替换条件：[[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- 底数趋非 \(1\) 常数和公共尺度：[[MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度]]
- 极限专题：[[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
