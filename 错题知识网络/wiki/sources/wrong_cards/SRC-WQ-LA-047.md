---
wiki_id: SRC-WQ-LA-047
type: source_summary
title: LA-047 1000题强化B组3.4
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-047_1000题强化B组3.4.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-047_1000题强化B组3.4.md
- 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-690_1000题强化B组3.4.md
visual_ids:
- VIS-LA-047
- MN4-GS-CH01-690
provenance_alias_detail_refs: []
provenance_alias_visual_ids: []
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-047/question_01.png
- 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-690/question_01.png
solution_asset_refs: []
reference_asset_refs: []
provenance_alias_asset_refs: []
adjudicated_asset_roles:
- path: 错题知识网络/assets/visual_wrong_questions/LA-047/question_01.png
  sha256: 2063e81fd7d6c0df909085ebec48c4e5a5fd6cee00c7e644bcd2b27678c8feb4
  raw_role: question
  role: question
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-690/question_01.png
  sha256: 2063e81fd7d6c0df909085ebec48c4e5a5fd6cee00c7e644bcd2b27678c8feb4
  raw_role: question
  role: question
  evidence_scope: live_evidence
registered_raw_asset_role_counts:
  question: 2
  solution: 0
  reference: 0
wrongnet_refs:
- LA-047
related_wrongnet_refs: []
knowledge:
- 矩阵运算
- 相似矩阵
- 逆矩阵
error_causes:
- 概念表述：左右乘与行、列线性组合的对应关系不够稳定。
- 证据边界：本次没有实质计算错误，但存在一次提示，不能认定无提示独立掌握。
answer: \boxed{\begin{pmatrix}1&0&-1\\0&1&-1\\0&0&0\end{pmatrix}}
methods:
- 相似分解
- 幂等矩阵
- 矩阵高次幂
- 逆矩阵计算
traps:
- 忘记先证明 B 可逆
- 高次幂硬算
- B^{-1} 符号
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-KNOWLEDGE-014

- MATHWIKI-KNOWLEDGE-040

- MATHWIKI-KNOWLEDGE-077

- MATHWIKI-METHOD-CLUSTER-1219

- MATHWIKI-METHOD-CLUSTER-1240

- MATHWIKI-METHOD-CLUSTER-1363

- MATHWIKI-METHOD-CLUSTER-972

- MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点
- MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线
related_method_card_id: L03-005
related_method_card_ids:
- L03-005
secondary_method_card_ids: []
method_route_fit: exact
evidence_status: user_confirmed
personal_diagnosis_status: user_confirmed
confirmation_state: confirmed
evidence_boundary: 2026-08-14 计算链独立正确，但存在一次概念澄清；mastery_candidate 已否决。
aggregate_edge_policy: block_strong_edges_pending_personal_confirmation
question_surface_status: registered_answer_safe_question_only
solution_surface_status: no_registered_solution_surface
scheduler_blocked: false
review: MATHWIKI-REVIEW-084
review_batch: MATHWIKI-REVIEW-084
formal_projection_sha256: 1c45503cd52fd4a2b737015199ac9756a137be29b76b64d37dfc0b41ea3d75fe
status: indexed
last_updated: '2026-08-27'
---

# LA-047 1000题强化B组3.4

## 正式投影

- 正式卡：`错题知识网络/错题卡/LA-047_1000题强化B组3.4.md`
- formal projection SHA-256：`79f6ed2a578fe9488fabec078b7f9c813628c207d0b0dec3387b5effd81b2746`
- review batch：`MATHWIKI-REVIEW-084`

## 可视化来源

- live：`错题知识网络/可视化错题详情/线性代数/LA-047_1000题强化B组3.4.md`（visual_id: `VIS-LA-047`）
- live：`错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-690_1000题强化B组3.4.md`（visual_id: `MN4-GS-CH01-690`）
- question：`错题知识网络/assets/visual_wrong_questions/LA-047/question_01.png`
- question：`错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-690/question_01.png`

## 客观题面与答案

- 题面：AB=B^2-BC，给定可逆 B 与 C，求 A^99。
- 答案：[[1,0,-1],[0,1,-1],[0,0,0]]。
- 第一动作：先右乘 B^{-1}，构造 A 与 B-C 的相似关系。

## 知识与方法投影

- 知识点：矩阵运算; 相似矩阵; 逆矩阵
- 方法：相似分解; 幂等矩阵; 矩阵高次幂; 逆矩阵计算
- 主方法卡：L03-005
- 完整方法路线：L03-005

## 个人证据边界

个人错因和动作断点均为候选，等待用户独立复做确认；客观解析不能证明用户当时发生了方法失败。

## wrongnet 关联题

- 暂无强边
