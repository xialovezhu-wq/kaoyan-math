---
source_pdf: 数学LLMWiki安全输入包.md
part: linear-algebra-practice
keywords: practice, linear-algebra, object-type
---

# 线性代数主线 Practice (9 questions)

#practice #math #linear-algebra

## Related Concepts

- [[线代对象判型总览]]
- [[方法缺口与错因模式]]

> [!hint]- 核心模式
> | Signal | Action |
> |---|---|
> | \(I+\alpha\alpha^{\mathrm T}\) | 秩一外积 |
> | 方程组 | 比秩 |
> | 向量组 | 判对象 |
> | 二次型 | 矩阵化 |
> | 特征值 | 写特征方程 |

## Question 1 - 方程组 [recall]
> 齐次线性方程组第一步看什么？

> [!answer]- 정답 보기
> 看系数矩阵秩，并确定自由变量个数和解空间维数。

## Question 2 - 非齐次 [recall]
> 非齐次线性方程组判断有无解要比较什么？

> [!answer]- 정답 보기
> 比较系数矩阵秩和增广矩阵秩。

## Question 3 - 向量组 [recall]
> 判断向量组线性相关前，必须先确认什么对象？

> [!answer]- 정답 보기
> 确认是行向量还是列向量，以及向量所在空间。

## Question 4 - 二次型 [recall]
> 二次型题的第一步是什么？

> [!answer]- 정답 보기
> 写出对应对称矩阵，并明确目标是标准形、正定性还是合同关系。

## Question 5 - 维数检查 [application]
> 矩阵乘法题最容易在第一步漏什么？

> [!answer]- 정답 보기
> 漏检查维数和乘法顺序，误把矩阵乘法当普通数乘。

## Question 6 - 特征结构 [application]
> 特征值题把特征值代入后，下一步应求什么？

> [!answer]- 정답 보기
> 求特征子空间，不能只停在特征方程。

## Question 7 - 秩一外积 [application]
> 看到 \(I+\alpha\alpha^{\mathrm T}\) 型行列式，第一反应应是什么？

> [!answer]- 정답 보기
> 先识别 \(\alpha\alpha^{\mathrm T}\) 是秩一外积矩阵；可用特征值平移，或用矩阵行列式引理。

## Question 8 - 变换区分 [analysis]
> 为什么二次型中的合同变换不能随便换成相似变换？

> [!answer]- 정답 보기
> 合同保持二次型结构，相似保持线性变换特征结构，目标不同。

## Question 9 - 错因诊断 [analysis]
> 用户算完行变换但不知道答案表示什么，这属于计算问题还是对象判型问题？

> [!answer]- 정답 보기
> 更接近对象判型和动作链问题：没有把行变换结果解释为秩、自由变量或解空间。

> [!summary]- 模式总结
> | Topic | First action |
> |---|---|
> | 秩一外积 | 特征值平移 / 行列式引理 |
> | 方程组 | 比秩 |
> | 向量组 | 判对象 |
> | 二次型 | 写矩阵 |
> | 特征值 | 求子空间 |
