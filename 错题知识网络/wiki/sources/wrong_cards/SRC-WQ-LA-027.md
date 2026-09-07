---
wiki_id: SRC-WQ-LA-027
type: source_summary
title: LA-027 线代基础6.7
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-027_线代基础6.7.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-027_缺图登记-线代基础6.7.md
visual_ids:
- VIS-LA-027
provenance_alias_detail_refs: []
provenance_alias_visual_ids: []
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-027/question_01.png
solution_asset_refs: []
reference_asset_refs: []
provenance_alias_asset_refs: []
adjudicated_asset_roles:
- path: 错题知识网络/assets/visual_wrong_questions/LA-027/question_01.png
  sha256: d872089682123236402d6f26e6c69928e1abec201e9c53a69c881be63ef4bf3e
  raw_role: question
  role: question
  evidence_scope: live_evidence
registered_raw_asset_role_counts:
  question: 1
  solution: 0
  reference: 0
wrongnet_refs:
- LA-027
related_wrongnet_refs: []
knowledge:
- 二次型
- 矩阵运算
error_causes:
- 个人错因候选待确认；没有用户真实作答过程。
answer: \boxed{a \in [-2,\, 2].}
methods:
- 分类讨论
- 标准化计算流程
traps:
- 参数边界
- 正负号
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-KNOWLEDGE-014_矩阵运算
- MATHWIKI-KNOWLEDGE-034_二次型
- MATHWIKI-METHOD-CLUSTER-004_分类讨论
- MATHWIKI-METHOD-CLUSTER-011_标准化计算流程
- MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点
- MATHWIKI-LA-METHOD-019_二次型矩阵化与惯性规范形
- MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线
related_method_card_id: L09-002
related_method_card_ids:
- L09-002
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
solution_surface_status: no_registered_solution_surface
scheduler_blocked: false
review: MATHWIKI-REVIEW-084
review_batch: MATHWIKI-REVIEW-084
formal_projection_sha256: 516b02d3b5471b88df58325b669454ab621e7ac2ab2ca8d1de8d69ce3c425771
status: indexed
last_updated: '2026-07-25'
---

# LA-027 线代基础6.7

## 正式投影

- 正式卡：`错题知识网络/错题卡/LA-027_线代基础6.7.md`
- formal projection SHA-256：`516b02d3b5471b88df58325b669454ab621e7ac2ab2ca8d1de8d69ce3c425771`
- review batch：`MATHWIKI-REVIEW-084`

## 可视化来源

- live：`错题知识网络/可视化错题详情/线性代数/LA-027_缺图登记-线代基础6.7.md`（visual_id: `VIS-LA-027`）
- question：`错题知识网络/assets/visual_wrong_questions/LA-027/question_01.png`

## 客观题面与答案

- 题面：二次型 x1^2-x2^2+2a x1x3+4x2x3 的负惯性指数为 1，求 a 的范围。
- 答案：a 属于 [-2,2]。
- 第一动作：先确认前 2×2 主块已有一正一负，再用 det(A) 判断第三个特征值及边界。

## 知识与方法投影

- 知识点：二次型; 矩阵运算
- 方法：分类讨论; 标准化计算流程
- 主方法卡：L09-002
- 完整方法路线：L09-002 → L09-006

## 个人证据边界

个人错因和动作断点均为候选，等待用户独立复做确认；客观解析不能证明用户当时发生了方法失败。

## wrongnet 关联题

- 暂无强边
