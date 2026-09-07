---
wiki_id: SRC-WQ-LA-036
type: source_summary
title: LA-036 强化例题9.7（171639）
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-036_强化例题9.7（171639）.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-036_强化例题9.7（171639）.md
- 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-672_强化例题9.7（171639）.md
visual_ids:
- VIS-LA-036
- MN4-GS-CH01-672
provenance_alias_detail_refs: []
provenance_alias_visual_ids: []
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-036/question_01.png
- 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-672/question_01.png
solution_asset_refs: []
reference_asset_refs: []
provenance_alias_asset_refs: []
adjudicated_asset_roles:
- path: 错题知识网络/assets/visual_wrong_questions/LA-036/question_01.png
  sha256: 65900a77383d1966a39ca9c04c69893dcf3dc3ee874700beece568b19c95c029
  raw_role: question
  role: question
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-672/question_01.png
  sha256: 65900a77383d1966a39ca9c04c69893dcf3dc3ee874700beece568b19c95c029
  raw_role: question
  role: question
  evidence_scope: live_evidence
registered_raw_asset_role_counts:
  question: 2
  solution: 0
  reference: 0
wrongnet_refs:
- LA-036
related_wrongnet_refs: []
knowledge:
- 二次型
- 实对称矩阵
- 特征值与特征向量
error_causes:
- 个人错因候选待确认；没有用户真实作答过程。
answer: \boxed{a=1,\quad Q=\begin{pmatrix}0&0&1\\1&0&0\\0&-1&0\end{pmatrix}}
methods:
- 二次型矩阵化
- 正交变换
- 特征值匹配
traps:
- 交叉项矩阵元素要除以 2
- 正交变换保持特征值
- 目标二次型也要先矩阵化
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-KNOWLEDGE-016_特征值与特征向量
- MATHWIKI-KNOWLEDGE-034_二次型
- MATHWIKI-KNOWLEDGE-056_实对称矩阵
- MATHWIKI-METHOD-CLUSTER-056_二次型矩阵化
- MATHWIKI-METHOD-CLUSTER-414_正交变换
- MATHWIKI-METHOD-CLUSTER-428_特征值匹配
- MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点
- MATHWIKI-LA-METHOD-019_二次型矩阵化与惯性规范形
- MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线
related_method_card_id: L09-003
related_method_card_ids:
- L09-003
secondary_method_card_ids: []
method_route_fit: exact
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
formal_projection_sha256: ecb26178d35f23702c57cabab90c12af74d837db6d7130006b5621a62c4b8c35
status: indexed
last_updated: '2026-07-25'
---

# LA-036 强化例题9.7（171639）

## 正式投影

- 正式卡：`错题知识网络/错题卡/LA-036_强化例题9.7（171639）.md`
- formal projection SHA-256：`ecb26178d35f23702c57cabab90c12af74d837db6d7130006b5621a62c4b8c35`
- review batch：`MATHWIKI-REVIEW-084`

## 可视化来源

- live：`错题知识网络/可视化错题详情/线性代数/LA-036_强化例题9.7（171639）.md`（visual_id: `VIS-LA-036`）
- live：`错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-672_强化例题9.7（171639）.md`（visual_id: `MN4-GS-CH01-672`）
- question：`错题知识网络/assets/visual_wrong_questions/LA-036/question_01.png`
- question：`错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-672/question_01.png`

## 客观题面与答案

- 题面：二次型 x1^2-x2x3 经正交变换化为 y1y2+a y3^2，求 a,Q。
- 答案：a=1；正式卡给出的 Q 可用。
- 第一动作：先把源式和目标式都写成实对称矩阵。

## 知识与方法投影

- 知识点：二次型; 实对称矩阵; 特征值与特征向量
- 方法：二次型矩阵化; 正交变换; 特征值匹配
- 主方法卡：L09-003
- 完整方法路线：L09-003

## 个人证据边界

个人错因和动作断点均为候选，等待用户独立复做确认；客观解析不能证明用户当时发生了方法失败。

## wrongnet 关联题

- 暂无强边
