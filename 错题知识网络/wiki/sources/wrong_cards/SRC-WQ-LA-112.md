---
wiki_id: SRC-WQ-LA-112
type: source_summary
title: "LA-112 实对称与正交特征向量充要"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-112_强化例题8.4-2.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-750_强化例题8.4.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-112_强化例题8.4-2.md"
visual_ids:
  - "MN4-GS-CH01-750"
  - "VIS-LA-112"
wrongnet_refs:
  - "LA-112"
knowledge:
  - "实对称矩阵"
  - "特征值与特征向量"
  - "相似矩阵"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "实对称矩阵正交对角化"
  - "正交矩阵相似对角化"
  - "特征向量正交化"
wiki_refs: []
status: indexed
last_updated: "2026-07-25"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-750/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-112/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-750/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-112/solution_01.png"
reference_asset_refs: []
related_wrongnet_refs: []
formal_projection_sha256: "8c384c9f65c1c995bd108b4508bb222f0d638085157729fd7a76635523324b1d"
semantic_review_batch: "MATHWIKI-REVIEW-090"
content_review_status: "verified"
chapter: "相似理论"
question_type: "实对称矩阵与正交特征向量充要关系"
answer: "C"
method_refs:
  - "L08-005"
  - "L08-001"
evidence_status: "pending_user_confirmation"
---

# LA-112 B42 source projection

## 正式投影对象

- formal_card: `错题知识网络/错题卡/LA-112_强化例题8.4-2.md`
- registered_detail_count: 2

## 可视化入口

- `MN4-GS-CH01-750`: `错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-750_强化例题8.4.md`
- `VIS-LA-112`: `错题知识网络/可视化错题详情/线性代数/LA-112_强化例题8.4-2.md`

## 注册视觉资产

以下清单覆盖本题全部注册资产；角色来自冻结清单。字节相同的来源副本仍保留各自路径，但不重复计作独立内容证据。

- question: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-750/question_01.png`
- question: `错题知识网络/assets/visual_wrong_questions/LA-112/question_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-750/solution_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/LA-112/solution_01.png`
- reference: 无

## method_gap 摘要

| 字段 | 值 |
|---|---|
| evidence_origin | pending_user_confirmation |
| repeat_count | 1 个旧导入事件；不确认个人断点 |
| expected_first_action | 先把相互正交的特征向量单位化并组成正交矩阵 \(Q\)。 |
| candidate_break | 候选断点是只记住实对称矩阵的充分方向，没有用 \(A=Q\Lambda Q^{\mathsf T}\) 完成反向证明。 |
| method route | L08-005；L08-001 |

## B42 语义核验

- 客观对象：实对称与存在一组相互正交特征向量之间的充要关系。
- 第一动作：把正交特征向量单位化并组成正交矩阵 \(Q\)。
- 反向链：

$$
A=Q\Lambda Q^{\mathsf T}
\quad\Longrightarrow\quad
A^{\mathsf T}=A.
$$

- 个人证据边界：是否只记住充分方向仍是候选断点。

## 关联卡片

- 暂无强边。
