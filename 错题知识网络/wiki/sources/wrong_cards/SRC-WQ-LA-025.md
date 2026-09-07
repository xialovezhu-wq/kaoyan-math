---
wiki_id: SRC-WQ-LA-025
type: source_summary
title: LA-025 强化例题9.1
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-025_强化例题9.1.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-025_强化例题9.1.md
- 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-662_强化例题9.1.md
visual_ids:
- VIS-LA-025
- MN4-GS-CH01-662
provenance_alias_detail_refs: []
provenance_alias_visual_ids: []
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-025/question_01.png
- 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-662/question_01.png
solution_asset_refs: []
reference_asset_refs: []
provenance_alias_asset_refs: []
adjudicated_asset_roles:
- path: 错题知识网络/assets/visual_wrong_questions/LA-025/question_01.png
  sha256: 866dc7d26088b9bfc4486f0e8f5aff07b2c1da06dd096bc8039be92e321c9f51
  raw_role: question
  role: question
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-662/question_01.png
  sha256: 866dc7d26088b9bfc4486f0e8f5aff07b2c1da06dd096bc8039be92e321c9f51
  raw_role: question
  role: question
  evidence_scope: live_evidence
registered_raw_asset_role_counts:
  question: 2
  solution: 0
  reference: 0
wrongnet_refs:
- LA-025
related_wrongnet_refs: []
knowledge:
- 二次型
- 正定矩阵
error_causes:
- 个人错因候选待确认；没有用户真实作答过程。
answer: \boxed{(B)\quad y_1^2+y_2^2+y_3^2}
methods:
- 二次型矩阵化
- 正定判定
- 规范形判定
traps:
- 非对称矩阵要取对称部分
- 规范形只看正负惯性指数
- 不要被上三角矩阵外观带偏
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-KNOWLEDGE-034_二次型
- MATHWIKI-KNOWLEDGE-113_正定矩阵
- MATHWIKI-METHOD-CLUSTER-056_二次型矩阵化
- MATHWIKI-METHOD-CLUSTER-1152_正定判定
- MATHWIKI-METHOD-CLUSTER-457_规范形判定
- MATHWIKI-LA-METHOD-019_二次型矩阵化与惯性规范形
- MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线
related_method_card_id: L09-001
related_method_card_ids:
- L09-001
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
formal_projection_sha256: a71aaa5ac7b1374bd5d3bb014f7162598348a8999eff767163fd80750e853b2a
status: indexed
last_updated: '2026-07-25'
---

# LA-025 强化例题9.1

## 正式投影

- 正式卡：`错题知识网络/错题卡/LA-025_强化例题9.1.md`
- formal projection SHA-256：`a71aaa5ac7b1374bd5d3bb014f7162598348a8999eff767163fd80750e853b2a`
- review batch：`MATHWIKI-REVIEW-084`

## 可视化来源

- live：`错题知识网络/可视化错题详情/线性代数/LA-025_强化例题9.1.md`（visual_id: `VIS-LA-025`）
- live：`错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-662_强化例题9.1.md`（visual_id: `MN4-GS-CH01-662`）
- question：`错题知识网络/assets/visual_wrong_questions/LA-025/question_01.png`
- question：`错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-662/question_01.png`

## 客观题面与答案

- 题面：二次型 f(x)=x^T Bx，其中 B=[[1,1,0],[0,1,1],[0,0,1]]，判断规范形。
- 答案：y1^2+y2^2+y3^2，选 B。
- 第一动作：先取 (B+B^T)/2，而不是直接把上三角矩阵当实对称矩阵。

## 知识与方法投影

- 知识点：二次型; 正定矩阵
- 方法：二次型矩阵化; 正定判定; 规范形判定
- 主方法卡：L09-001
- 完整方法路线：L09-001 → L09-009

## 个人证据边界

个人错因和动作断点均为候选，等待用户独立复做确认；客观解析不能证明用户当时发生了方法失败。

## wrongnet 关联题

- 暂无强边
