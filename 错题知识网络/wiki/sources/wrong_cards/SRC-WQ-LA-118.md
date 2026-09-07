---
wiki_id: SRC-WQ-LA-118
type: source_summary
title: "LA-118 递推向量相似对角化求通项"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-118_强化例题8.8（102152）.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-756_强化例题8.8（102152）.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-118_强化例题8.8（102152）.md"
visual_ids:
  - "MN4-GS-CH01-756"
  - "VIS-LA-118"
wrongnet_refs:
  - "LA-118"
knowledge:
  - "相似矩阵"
  - "特征值与特征向量"
  - "矩阵运算"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "特征分解"
  - "条件转化"
  - "标准化计算流程"
wiki_refs: []
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
review_batch: "MATHWIKI-REVIEW-086"
formal_projection_sha256: "ecc6451ff0d7c27e33690c2564df049017db45ff04f59b084f6b8fcfb9741d7e"
relation_review_batch: "MATHWIKI-REVIEW-088"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-756/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-118/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
semantic_review_batch: "MATHWIKI-REVIEW-090"
content_review_status: "verified"
chapter: "相似理论"
question_type: "递推关系矩阵化与矩阵幂"
answer: "\\(A=\\begin{pmatrix}-2&0&2\\\\0&-2&-2\\\\-6&-3&3\\end{pmatrix}\\)；当 \\(n\\ge1\\)，\\(x_n=(-2)^n+8,\\ y_n=-2(-2)^n-8,\\ z_n=12\\)。"
method_refs:
  - "L08-007"
  - "L08-001"
evidence_status: "pending_user_confirmation"
---

# LA-118 B42 source projection

## 正式投影对象

- formal_card: `错题知识网络/错题卡/LA-118_强化例题8.8（102152）.md`
- registered_detail_count: 2

## 可视化入口

- `MN4-GS-CH01-756`: `错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-756_强化例题8.8（102152）.md`
- `VIS-LA-118`: `错题知识网络/可视化错题详情/线性代数/LA-118_强化例题8.8（102152）.md`

## 注册视觉资产

以下清单覆盖本题全部注册资产；角色来自冻结清单。字节相同的来源副本仍保留各自路径，但不重复计作独立内容证据。

- question: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-756/question_01.png`
- question: `错题知识网络/assets/visual_wrong_questions/LA-118/question_01.png`
- solution: 无
- reference: 无

## method_gap 摘要

| 字段 | 值 |
|---|---|
| evidence_origin | pending_user_confirmation |
| repeat_count | 1 个旧导入事件；不确认个人断点 |
| expected_first_action | 先把三元递推写成 \(\alpha_n=A\alpha_{n-1}\)，再处理 \(A^n\)。 |
| candidate_break | 候选断点是没有先把分量递推向量化，或忽略 \(0^n\) 只在 \(n\ge1\) 时消失。 |
| method route | L08-007；L08-001 |

## B42 语义核验

- 客观对象：把三元递推向量化并利用相似对角化求通项。
- 第一动作：

$$
\alpha_n=A\alpha_{n-1},\qquad \alpha_n=A^n\alpha_0.
$$

- 边界：特征值 \(0\) 的幂只在 \(n\ge1\) 时消失，不能把同一表达式无条件套到 \(n=0\)。
- 个人证据边界：当前没有用户作答过程，向量化与下标边界只是候选检查点。

## 关联卡片

- 暂无强边。
