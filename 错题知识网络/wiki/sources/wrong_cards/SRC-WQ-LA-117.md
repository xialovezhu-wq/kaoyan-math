---
wiki_id: SRC-WQ-LA-117
type: source_summary
title: "LA-117 同特征值矩阵相似秩不变量"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-117_2018年第7题.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-755_2018年第7题.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-117_2018年第7题.md"
visual_ids:
  - "MN4-GS-CH01-755"
  - "VIS-LA-117"
wrongnet_refs:
  - "LA-117"
knowledge:
  - "相似矩阵"
  - "特征值与特征向量"
  - "矩阵秩"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "相似不变量判定"
  - "秩不变量判定"
  - "Jordan结构判定"
wiki_refs: []
status: indexed
last_updated: "2026-07-25"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-755/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-117/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-755/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-117/solution_01.png"
reference_asset_refs: []
related_wrongnet_refs: []
formal_projection_sha256: "d2733e3fbf734fa9da46d02fefb4f34deca467287278fe8f38fe59f34437007d"
semantic_review_batch: "MATHWIKI-REVIEW-090"
content_review_status: "verified"
chapter: "相似理论"
topic: "Jordan结构的秩不变量判定"
question_type: "相似矩阵必要条件与Jordan结构判定"
answer: "A"
method_refs:
  - "L08-002"
  - "L08-006"
evidence_status: "pending_user_confirmation"
---

# LA-117 B42 source projection

## 正式投影对象

- formal_card: `错题知识网络/错题卡/LA-117_2018年第7题.md`
- registered_detail_count: 2

## 可视化入口

- `MN4-GS-CH01-755`: `错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-755_2018年第7题.md`
- `VIS-LA-117`: `错题知识网络/可视化错题详情/线性代数/LA-117_2018年第7题.md`

## 注册视觉资产

以下清单覆盖本题全部注册资产；角色来自冻结清单。字节相同的来源副本仍保留各自路径，但不重复计作独立内容证据。

- question: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-755/question_01.png`
- question: `错题知识网络/assets/visual_wrong_questions/LA-117/question_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-755/solution_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/LA-117/solution_01.png`
- reference: 无

## method_gap 摘要

| 字段 | 值 |
|---|---|
| evidence_origin | pending_user_confirmation |
| repeat_count | 1 个旧导入事件；不确认个人断点 |
| expected_first_action | 先取唯一特征值 \(1\)，逐项比较 \(r(B_i-I)\)；不要先假设候选矩阵可对角化。 |
| candidate_break | 候选断点是把相同特征值当成相似的充分条件，没有比较 \(r(B_i-I)\)。 |
| method route | L08-002；L08-006 |

## B42 语义核验

- 客观对象：在特征值全部为 \(1\) 的候选矩阵中，用秩区分 Jordan 结构。
- 主方法卡：L08-002；第一动作是直接比较 \(r(B_i-I)\)。
- L08-006 只保留为“判断两个矩阵是否相似”的宽泛背景，不作为本题第一动作。
- 题面中选项 \(C\) 对应矩阵满足

$$
B_3-I=
\begin{pmatrix}
0&1&-1\\
0&0&0\\
0&0&0
\end{pmatrix},
\qquad r(B_3-I)=1.
$$

- 不可变解析图在该局部矩阵上显示错误，但其文字秩结论为 \(1\)。应以题面矩阵独立重算；正确选项仍为 \(A\)。
- 个人证据边界：是否漏掉秩比较仍待复做确认。

## 关联卡片

- 暂无强边。
