---
source_pdf: 数学LLMWiki安全输入包.md
part: method-error-practice
keywords: practice, method-gap, error-pattern
---

# 方法错因训练 Practice (8 questions)

#practice #math #method-gap #error-pattern

## Related Concepts

- [[方法缺口与错因模式]]
- [[高数第一动作总览]]
- [[线代对象判型总览]]

> [!hint]- 核心模式
> | Gap | Repair |
> |---|---|
> | B2 | 信号触发 |
> | B3 | 方法落地 |
> | B4 | 动作链 |
> | B5 | 检查闭环 |

## Question 1 - B2 [recall]
> B2-TRIGGER 主要描述什么问题？

> [!answer]- 정답 보기
> 看见题面信号但没有触发对应第一动作。

## Question 2 - B3 [recall]
> B3-METHOD 和“不会知识点”有什么区别？

> [!answer]- 정답 보기
> B3 是知道方法名但不能落成可执行第一步。

## Question 3 - B4 [recall]
> B4-CHAIN 的复盘重点是什么？

> [!answer]- 정답 보기
> 补齐步骤之间的理由和下一步动作。

## Question 4 - B5 [recall]
> B5-CHECK 最常见的遗漏是什么？

> [!answer]- 정답 보기
> 忘记回查端点、定义域、符号、分段归属或定理条件。

## Question 5 - 分类断点 [application]
> 用户开始分类讨论但漏掉端点，这更像哪类断点？

> [!answer]- 정답 보기
> 更像 B4-CHAIN 或 B5-CHECK，说明分类链条或检查闭环不完整。

## Question 6 - 方法落地 [application]
> 用户说“这里应该用中值定理”，但不会构造辅助函数，这属于什么问题？

> [!answer]- 정답 보기
> 属于 B3-METHOD：方法名没有落成第一步动作。

## Question 7 - 具体 wrong_point [analysis]
> “计算失误”为什么不够适合作为 wrong_point？

> [!answer]- 정답 보기
> 它不可复做；应改成具体动作缺口，如“换元后没有同步改上下限和微分”。

## Question 8 - Tutor 边界 [analysis]
> Tutor 测验发现某概念薄弱，能否直接改回滚 JSON 掌握度？

> [!answer]- 정답 보기
> 不能。Tutor 只记录概念训练结果，不反写正式回滚掌握度。

> [!summary]- 模式总结
> | Gap | Question |
> |---|---|
> | B2 | 有没有被信号触发？ |
> | B3 | 第一动作是什么？ |
> | B4 | 下一步理由是什么？ |
> | B5 | 是否回查条件？ |

