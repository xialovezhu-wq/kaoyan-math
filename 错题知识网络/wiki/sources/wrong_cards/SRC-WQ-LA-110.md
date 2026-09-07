---
wiki_id: SRC-WQ-LA-110
type: source_summary
title: "LA-110 相似对角化几何重数判定"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-110_强化例题8.2-2.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-747_强化例题8.2.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-110_强化例题8.2-2.md"
visual_ids:
  - "MN4-GS-CH01-747"
  - "VIS-LA-110"
wrongnet_refs:
  - "LA-110"
knowledge:
  - "相似矩阵"
  - "特征值与特征向量"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "相似对角化"
  - "几何重数判定"
  - "代数重数比较"
  - "实对称矩阵判定"
wiki_refs: []
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
formal_projection_sha256: "c7d43666fed0f69c48b2aab94157675da4ce887aa4cd75aedfb4bfb1cd21780f"
relation_review_batch: "MATHWIKI-REVIEW-088"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-747/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-110/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-747/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-110/solution_01.png"
reference_asset_refs: []
semantic_review_batch: "MATHWIKI-REVIEW-090"
content_review_status: "verified"
chapter: "相似理论"
question_type: "相似对角化判定"
answer: "A。A 的 λ=1 代数重数为 2，但特征空间维数为 1，不能相似于对角矩阵。"
method_refs:
  - "L08-002"
evidence_status: "pending_user_confirmation"
---

# LA-110 B42 source projection

## 正式投影对象

- formal_card: `错题知识网络/错题卡/LA-110_强化例题8.2-2.md`
- registered_detail_count: 2

## 可视化入口

- `MN4-GS-CH01-747`: `错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-747_强化例题8.2.md`
- `VIS-LA-110`: `错题知识网络/可视化错题详情/线性代数/LA-110_强化例题8.2-2.md`

## 注册视觉资产

以下清单覆盖本题全部注册资产；角色来自冻结清单。字节相同的来源副本仍保留各自路径，但不重复计作独立内容证据。

- question: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-747/question_01.png`
- question: `错题知识网络/assets/visual_wrong_questions/LA-110/question_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-747/solution_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/LA-110/solution_01.png`
- reference: 无

## method_gap 摘要

| 字段 | 值 |
|---|---|
| evidence_origin | pending_user_confirmation |
| repeat_count | 1 个旧导入事件；不确认个人断点 |
| expected_first_action | 先找重特征值，再计算对应的几何重数 \(n-r(\lambda I-A)\)。 |
| candidate_break | 候选断点是只看上三角对角线，没有继续核对重根的几何重数。 |
| method route | L08-002 |

## B42 语义核验

- 客观对象：判断三阶矩阵能否相似对角化。
- 知识连接：重特征值的代数重数必须与几何重数一致。
- 第一动作：对重根 \(\lambda\) 计算 \(n-r(\lambda I-A)\)。
- 个人证据边界：当前只有旧导入事件，具体个人断点仍是待复做候选，不得写成已确认错因。

## 关联卡片

- 暂无强边。
