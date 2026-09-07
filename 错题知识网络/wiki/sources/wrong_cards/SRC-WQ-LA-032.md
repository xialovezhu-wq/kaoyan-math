---
wiki_id: SRC-WQ-LA-032
type: source_summary
title: LA-032 2025年真题选择题第八题
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-032_2025年真题选择题第八题.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-032_2025年真题选择题第八题.md
- 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-667_2025年真题选择题第八题.md
visual_ids:
- VIS-LA-032
- MN4-GS-CH01-667
provenance_alias_detail_refs: []
provenance_alias_visual_ids: []
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-032/question_01.png
- 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-667/question_01.png
solution_asset_refs: []
reference_asset_refs: []
provenance_alias_asset_refs: []
adjudicated_asset_roles:
- path: 错题知识网络/assets/visual_wrong_questions/LA-032/question_01.png
  sha256: a3bc1bbafd618ff14d155a2f3097be381a269138b6b4780ed7b4ded6ef1eaf56
  raw_role: question
  role: question
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-667/question_01.png
  sha256: a3bc1bbafd618ff14d155a2f3097be381a269138b6b4780ed7b4ded6ef1eaf56
  raw_role: question
  role: question
  evidence_scope: live_evidence
registered_raw_asset_role_counts:
  question: 2
  solution: 0
  reference: 0
wrongnet_refs:
- LA-032
related_wrongnet_refs: []
knowledge:
- 二次型
- 实对称矩阵
- 特征值与特征向量
error_causes:
- 个人错因候选待确认；没有用户真实作答过程。
answer: \boxed{a<4,\ b<0}
methods:
- 二次型配方法
- 惯性定理
- 参数范围判定
traps:
- 直接硬算三阶特征方程
- 配方后忘记固定正系数
- 严格不等号边界
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-KNOWLEDGE-016_特征值与特征向量
- MATHWIKI-KNOWLEDGE-034_二次型
- MATHWIKI-KNOWLEDGE-056_实对称矩阵
- MATHWIKI-METHOD-CLUSTER-1004_惯性定理
- MATHWIKI-METHOD-CLUSTER-553_二次型配方法
- MATHWIKI-METHOD-CLUSTER-760_参数范围判定
- MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点
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
formal_projection_sha256: 1efe77cca379d8771041e5cf0e93b9c812bb5bebaa267213b7b3267d9acba83b
status: indexed
last_updated: '2026-07-25'
---

# LA-032 2025年真题选择题第八题

## 正式投影

- 正式卡：`错题知识网络/错题卡/LA-032_2025年真题选择题第八题.md`
- formal projection SHA-256：`1efe77cca379d8771041e5cf0e93b9c812bb5bebaa267213b7b3267d9acba83b`
- review batch：`MATHWIKI-REVIEW-084`

## 可视化来源

- live：`错题知识网络/可视化错题详情/线性代数/LA-032_2025年真题选择题第八题.md`（visual_id: `VIS-LA-032`）
- live：`错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-667_2025年真题选择题第八题.md`（visual_id: `MN4-GS-CH01-667`）
- question：`错题知识网络/assets/visual_wrong_questions/LA-032/question_01.png`
- question：`错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-667/question_01.png`

## 客观题面与答案

- 题面：矩阵 [[1,2,0],[2,a,0],[0,0,b]] 有一个正特征值和两个负特征值，判断 a,b。
- 答案：a<4 且 b<0，选 D。
- 第一动作：先把 2×2 块与独立特征值 b 分开判断。

## 知识与方法投影

- 知识点：二次型; 实对称矩阵; 特征值与特征向量
- 方法：二次型配方法; 惯性定理; 参数范围判定
- 主方法卡：L09-002
- 完整方法路线：L09-002 → L09-006

## 个人证据边界

个人错因和动作断点均为候选，等待用户独立复做确认；客观解析不能证明用户当时发生了方法失败。

## wrongnet 关联题

- 暂无强边
