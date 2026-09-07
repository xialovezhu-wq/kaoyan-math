---
wiki_id: SRC-WQ-LA-022
type: source_summary
title: LA-022 强化例题2.3
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-022_强化例题2.3.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-022_强化例题2.3.md
- 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-660_强化例题2.3.md
visual_ids:
- VIS-LA-022
- MN4-GS-CH01-660
provenance_alias_detail_refs: []
provenance_alias_visual_ids: []
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-022/question_01.png
- 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-660/question_01.png
solution_asset_refs: []
reference_asset_refs: []
provenance_alias_asset_refs: []
adjudicated_asset_roles:
- path: 错题知识网络/assets/visual_wrong_questions/LA-022/question_01.png
  sha256: b803ebf72e1ea101123846302e0e586a64a11cca01e9811b36a5340d6c6a5489
  raw_role: question
  role: question
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-660/question_01.png
  sha256: b803ebf72e1ea101123846302e0e586a64a11cca01e9811b36a5340d6c6a5489
  raw_role: question
  role: question
  evidence_scope: live_evidence
registered_raw_asset_role_counts:
  question: 2
  solution: 0
  reference: 0
wrongnet_refs:
- LA-022
related_wrongnet_refs: []
knowledge:
- 行列式
- 代数余子式
- 特征值与特征向量
- 特征多项式
- 伴随矩阵
- 矩阵的迹
- 逆矩阵与特征值
error_causes:
- 知识点不熟
- 方法论调取失败
- 概念边界混淆
- 计算失误
answer: \boxed{1}
methods:
- 特征值不变量
- 主子式和
- 特征多项式系数
- 伴随矩阵特征值
- 迹等于特征值之和
traps:
- 混淆原矩阵元素、代数余子式与伴随矩阵对角元素
- 把应求的迹改成行列式
- 对三阶矩阵误用标量倍数的行列式规则
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-ACTION-GAP-005

- MATHWIKI-ERROR-CLUSTER-007

- MATHWIKI-ERROR-CLUSTER-014

- MATHWIKI-ERROR-CLUSTER-027

- MATHWIKI-ERROR-CLUSTER-090

- MATHWIKI-KNOWLEDGE-016

- MATHWIKI-KNOWLEDGE-023

- MATHWIKI-KNOWLEDGE-134

- MATHWIKI-KNOWLEDGE-135

- MATHWIKI-KNOWLEDGE-264

- MATHWIKI-KNOWLEDGE-473

- MATHWIKI-KNOWLEDGE-474

- MATHWIKI-METHOD-CLUSTER-541

- MATHWIKI-METHOD-CLUSTER-1179

- MATHWIKI-METHOD-CLUSTER-1190

- MATHWIKI-METHOD-CLUSTER-1516

- MATHWIKI-METHOD-CLUSTER-1517

- MATHWIKI-LA-METHOD-018_行列式结构化计算与指定项系数
- MATHWIKI-LA-TOPIC-005_行列式错题总线
related_method_card_id: L02-004
related_method_card_ids:
- L02-004
secondary_method_card_ids: []
method_route_fit: exact
evidence_status: user_confirmed
personal_diagnosis_status: user_confirmed
confirmation_state: confirmed
evidence_boundary: 2026-05-07个人错因未知；2026-07-29真实作答已确认
aggregate_edge_policy: block_strong_edges
question_surface_status: registered_answer_safe_question_only
solution_surface_status: no_registered_solution_surface
scheduler_blocked: false
review: MATHWIKI-REVIEW-084
review_batch: MATHWIKI-REVIEW-084
formal_projection_sha256: e68086a2c0184e8689692b6eba7128f0661d924f7dab95a59cdb725cdb1f15eb
status: indexed
last_updated: '2026-08-27'
---

# LA-022 强化例题2.3

## 正式投影

- 正式卡：`错题知识网络/错题卡/LA-022_强化例题2.3.md`
- formal projection SHA-256：`1a5e5f54c6d8cc18e9aaccb2a840f763d05bd8d90ce769c78e2fbc0c761a192e`
- review batch：`MATHWIKI-REVIEW-084`

## 可视化来源

- live：`错题知识网络/可视化错题详情/线性代数/LA-022_强化例题2.3.md`（visual_id: `VIS-LA-022`）
- live：`错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-660_强化例题2.3.md`（visual_id: `MN4-GS-CH01-660`）
- question：`错题知识网络/assets/visual_wrong_questions/LA-022/question_01.png`
- question：`错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-660/question_01.png`

## 客观题面与答案

- 题面：已知三阶矩阵特征值为 -1,2,3，求三个主代数余子式之和。
- 答案：1。
- 第一动作：区分 \(a_{ii}\)、\(A_{ii}\) 与 \(A^*\)，把三个主代数余子式之和写成 \(\operatorname{tr}(A^*)\)。

## 知识与方法投影

- 知识点：行列式；代数余子式；特征值与特征向量；特征多项式；伴随矩阵；矩阵的迹；逆矩阵与特征值
- 方法：特征值不变量；主子式和；特征多项式系数；伴随矩阵特征值；迹等于特征值之和
- 主方法卡：L02-004
- 完整方法路线：L02-004

## 个人证据边界

2026-05-07 的个人错因仍未知；2026-07-29 的真实作答确认了首个对象边界断点，且连续讲解后仍出现迹与行列式混淆。听懂讲解不等于已经无提示掌握。

## 索引型簇页

- [[MATHWIKI-ACTION-GAP-005_A-CONCEPT]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-ERROR-CLUSTER-027_概念边界混淆]]
- [[MATHWIKI-ERROR-CLUSTER-090_知识点不熟]]
- [[MATHWIKI-KNOWLEDGE-016_特征值与特征向量]]
- [[MATHWIKI-KNOWLEDGE-023_行列式]]
- [[MATHWIKI-KNOWLEDGE-134_代数余子式]]
- [[MATHWIKI-KNOWLEDGE-135_伴随矩阵]]
- [[MATHWIKI-KNOWLEDGE-264_特征多项式]]
- [[MATHWIKI-KNOWLEDGE-473_矩阵的迹]]
- [[MATHWIKI-KNOWLEDGE-474_逆矩阵与特征值]]
- [[MATHWIKI-METHOD-CLUSTER-541_主子式和]]
- [[MATHWIKI-METHOD-CLUSTER-1179_特征值不变量]]
- [[MATHWIKI-METHOD-CLUSTER-1190_特征多项式系数]]
- [[MATHWIKI-METHOD-CLUSTER-1516_伴随矩阵特征值]]
- [[MATHWIKI-METHOD-CLUSTER-1517_迹等于特征值之和]]

## wrongnet 关联题

- 暂无强边
