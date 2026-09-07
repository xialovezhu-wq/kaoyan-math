---
wiki_id: SRC-WQ-LA-034
type: source_summary
title: LA-034 2021年第八题
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-034_2021年第八题.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-034_2021年第八题.md
- 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-669_2021年第八题.md
visual_ids:
- VIS-LA-034
- MN4-GS-CH01-669
provenance_alias_detail_refs: []
provenance_alias_visual_ids: []
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-034/question_01.png
- 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-669/question_01.png
solution_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-034/solution_01.png
- 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-669/solution_01.png
reference_asset_refs: []
provenance_alias_asset_refs: []
adjudicated_asset_roles:
- path: 错题知识网络/assets/visual_wrong_questions/LA-034/question_01.png
  sha256: 2ca51c9de82c3c409afa37480a3ba025dc0564f05ed7d56110a38a9c5fc6d8e9
  raw_role: question
  role: question
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/LA-034/solution_01.png
  sha256: 5a02d34b1b4cc1397a8a8afd005b79c1fc628ef8b0ae77748b7064c2d8e87b41
  raw_role: solution
  role: solution
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-669/question_01.png
  sha256: 2ca51c9de82c3c409afa37480a3ba025dc0564f05ed7d56110a38a9c5fc6d8e9
  raw_role: question
  role: question
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-669/solution_01.png
  sha256: 5a02d34b1b4cc1397a8a8afd005b79c1fc628ef8b0ae77748b7064c2d8e87b41
  raw_role: solution
  role: solution
  evidence_scope: live_evidence
registered_raw_asset_role_counts:
  question: 2
  solution: 2
  reference: 0
wrongnet_refs:
- LA-034
related_wrongnet_refs: []
knowledge:
- 二次型
- 实对称矩阵
- 特征值与特征向量
error_causes:
- 个人错因候选待确认；没有用户真实作答过程。
answer: 正惯性指数为 \(1\)，负惯性指数为 \(1\)
methods:
- 二次型矩阵化
- 特征值判惯性指数
- 正负惯性指数判定
traps:
- 不能凭原式中正负号数量判断惯性指数
- 交叉项写矩阵时非对角元要取交叉项系数的一半
- 零特征值不计入正惯性或负惯性指数
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-KNOWLEDGE-016_特征值与特征向量
- MATHWIKI-KNOWLEDGE-034_二次型
- MATHWIKI-KNOWLEDGE-056_实对称矩阵
- MATHWIKI-METHOD-CLUSTER-056_二次型矩阵化
- MATHWIKI-METHOD-CLUSTER-1154_正负惯性指数判定
- MATHWIKI-METHOD-CLUSTER-427_特征值判惯性指数
- MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点
- MATHWIKI-LA-METHOD-019_二次型矩阵化与惯性规范形
- MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线
related_method_card_id: L09-001
related_method_card_ids:
- L09-001
- L09-006
secondary_method_card_ids:
- L09-006
method_route_fit: exact_then_goal
evidence_status: pending_user_confirmation
personal_diagnosis_status: candidate_pending_user_confirmation
confirmation_state: pending_user_confirmation
evidence_boundary: objective_content_only_personal_diagnosis_pending
aggregate_edge_policy: block_strong_edges_pending_personal_confirmation
question_surface_status: registered_answer_safe_question_only
solution_surface_status: registered_solution_surface
scheduler_blocked: false
review: MATHWIKI-REVIEW-084
review_batch: MATHWIKI-REVIEW-084
formal_projection_sha256: 3b7655636af3c94d87f538d7f44c3b6923c03f45cf4fbedaf2cf9699601f4ab2
status: indexed
last_updated: '2026-07-25'
---

# LA-034 2021年第八题

## 正式投影

- 正式卡：`错题知识网络/错题卡/LA-034_2021年第八题.md`
- formal projection SHA-256：`3b7655636af3c94d87f538d7f44c3b6923c03f45cf4fbedaf2cf9699601f4ab2`
- review batch：`MATHWIKI-REVIEW-084`

## 可视化来源

- live：`错题知识网络/可视化错题详情/线性代数/LA-034_2021年第八题.md`（visual_id: `VIS-LA-034`）
- live：`错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-669_2021年第八题.md`（visual_id: `MN4-GS-CH01-669`）
- question：`错题知识网络/assets/visual_wrong_questions/LA-034/question_01.png`
- solution：`错题知识网络/assets/visual_wrong_questions/LA-034/solution_01.png`
- question：`错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-669/question_01.png`
- solution：`错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-669/solution_01.png`

## 客观题面与答案

- 题面：求平方和差二次型的正、负惯性指数。
- 答案：正惯性指数 1，负惯性指数 1，选 B。
- 第一动作：先展开并写实对称矩阵，再数正负特征值。

## 知识与方法投影

- 知识点：二次型; 实对称矩阵; 特征值与特征向量
- 方法：二次型矩阵化; 特征值判惯性指数; 正负惯性指数判定
- 主方法卡：L09-001
- 完整方法路线：L09-001 → L09-006

## 个人证据边界

个人错因和动作断点均为候选，等待用户独立复做确认；客观解析不能证明用户当时发生了方法失败。

## wrongnet 关联题

- 暂无强边
