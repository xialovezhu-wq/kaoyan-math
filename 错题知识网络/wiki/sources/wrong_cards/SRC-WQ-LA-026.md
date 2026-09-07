---
wiki_id: SRC-WQ-LA-026
type: source_summary
title: LA-026 强化例题9.2
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-026_强化例题9.2.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-026_强化例题9.2.md
- 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-663_强化例题9.2.md
visual_ids:
- VIS-LA-026
- MN4-GS-CH01-663
provenance_alias_detail_refs: []
provenance_alias_visual_ids: []
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-026/question_01.png
- 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-663/question_01.png
solution_asset_refs: []
reference_asset_refs: []
provenance_alias_asset_refs: []
adjudicated_asset_roles:
- path: 错题知识网络/assets/visual_wrong_questions/LA-026/question_01.png
  sha256: c15e7a0d1ecf410c69bd630e77f062e99e0656bfdb09ccce3023dcc84716c8cd
  raw_role: question
  role: question
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-663/question_01.png
  sha256: c15e7a0d1ecf410c69bd630e77f062e99e0656bfdb09ccce3023dcc84716c8cd
  raw_role: question
  role: question
  evidence_scope: live_evidence
registered_raw_asset_role_counts:
  question: 2
  solution: 0
  reference: 0
wrongnet_refs:
- LA-026
related_wrongnet_refs: []
knowledge:
- 二次型
- 正定矩阵
error_causes:
- 个人错因候选待确认；没有用户真实作答过程。
answer: \boxed{a\ne\frac12}
methods:
- 二次型矩阵化
- Gram矩阵
- 顺序主子式判定
traps:
- 平方和只说明半正定
- 正定还要排除非零公共零点
- 行列式等于零的参数边界
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-KNOWLEDGE-034_二次型
- MATHWIKI-KNOWLEDGE-113_正定矩阵
- MATHWIKI-METHOD-CLUSTER-056_二次型矩阵化
- MATHWIKI-METHOD-CLUSTER-1422_顺序主子式判定
- MATHWIKI-METHOD-CLUSTER-481_Gram矩阵
- MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点
- MATHWIKI-LA-METHOD-019_二次型矩阵化与惯性规范形
- MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线
related_method_card_id: L09-005
related_method_card_ids:
- L09-005
- L09-009
secondary_method_card_ids:
- L09-009
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
formal_projection_sha256: 8a0bb6e0181c0b305b033ff22eba08ea825ef7c3a506f37f751e4945852ea1fa
status: indexed
last_updated: '2026-07-25'
---

# LA-026 强化例题9.2

## 正式投影

- 正式卡：`错题知识网络/错题卡/LA-026_强化例题9.2.md`
- formal projection SHA-256：`8a0bb6e0181c0b305b033ff22eba08ea825ef7c3a506f37f751e4945852ea1fa`
- review batch：`MATHWIKI-REVIEW-084`

## 可视化来源

- live：`错题知识网络/可视化错题详情/线性代数/LA-026_强化例题9.2.md`（visual_id: `VIS-LA-026`）
- live：`错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-663_强化例题9.2.md`（visual_id: `MN4-GS-CH01-663`）
- question：`错题知识网络/assets/visual_wrong_questions/LA-026/question_01.png`
- question：`错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-663/question_01.png`

## 客观题面与答案

- 题面：alpha1=(1,2)^T、alpha2=(a,1)^T，二次型为两个内积平方和，求正定参数。
- 答案：a 不等于 1/2。
- 第一动作：先检查 alpha1,alpha2 是否张成 R^2，或写 Gram 矩阵。

## 知识与方法投影

- 知识点：二次型; 正定矩阵
- 方法：二次型矩阵化; Gram矩阵; 顺序主子式判定
- 主方法卡：L09-005
- 完整方法路线：L09-005 → L09-009

## 个人证据边界

个人错因和动作断点均为候选，等待用户独立复做确认；客观解析不能证明用户当时发生了方法失败。

## wrongnet 关联题

- 暂无强边
