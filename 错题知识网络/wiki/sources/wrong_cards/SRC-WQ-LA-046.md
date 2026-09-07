---
wiki_id: SRC-WQ-LA-046
type: source_summary
title: LA-046 初等矩阵幂的行列变换
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-046_强化例题3.6（152785）.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-046_强化例题3.6（152785）.md
- 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-689_强化例题3.6（152785）.md
visual_ids:
- VIS-LA-046
- MN4-GS-CH01-689
provenance_alias_detail_refs: []
provenance_alias_visual_ids: []
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-046/question_01.png
- 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-689/question_01.png
solution_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-046/solution_01.png
- 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-689/solution_01.png
reference_asset_refs: []
provenance_alias_asset_refs: []
adjudicated_asset_roles:
- path: 错题知识网络/assets/visual_wrong_questions/LA-046/question_01.png
  sha256: 5481a0260f925a5568fb97358c4bd397f3ca81a37ffdae432f3962f401fe4bee
  raw_role: question
  role: question
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/LA-046/solution_01.png
  sha256: 8da5663fee0126692ac1a19feda32de134c21cbf7a8a1dfb4f1b1356a12d699d
  raw_role: solution
  role: solution
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-689/question_01.png
  sha256: 5481a0260f925a5568fb97358c4bd397f3ca81a37ffdae432f3962f401fe4bee
  raw_role: question
  role: question
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-689/solution_01.png
  sha256: 8da5663fee0126692ac1a19feda32de134c21cbf7a8a1dfb4f1b1356a12d699d
  raw_role: solution
  role: solution
  evidence_scope: live_evidence
registered_raw_asset_role_counts:
  question: 2
  solution: 2
  reference: 0
wrongnet_refs:
- LA-046
related_wrongnet_refs: []
knowledge:
- 矩阵运算
error_causes:
- 个人错因候选待确认；没有用户真实作答过程。
answer: \(\begin{pmatrix}2&1\\-3&-4\end{pmatrix}\)。
methods:
- 初等矩阵
- 左乘行变换
- 右乘列变换
- 矩阵乘法顺序
traps:
- 左乘作用于行，右乘作用于列。
- 初等矩阵的负幂要先看矩阵自身的周期或逆矩阵结构。
- \(C=\begin{pmatrix}0&1\\1&0\end{pmatrix}\) 满足 \(C^{-1}=C\)，所以 \(C^{-5}=C^5=C\)。
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-KNOWLEDGE-014_矩阵运算
- MATHWIKI-METHOD-CLUSTER-1229_矩阵乘法顺序
- MATHWIKI-METHOD-CLUSTER-336_右乘列变换
- MATHWIKI-METHOD-CLUSTER-700_初等矩阵
- MATHWIKI-METHOD-CLUSTER-955_左乘行变换
- MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点
- MATHWIKI-LA-METHOD-008_矩阵运算结构识别
- MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线
related_method_card_id: L03-008
related_method_card_ids:
- L03-008
secondary_method_card_ids: []
method_route_fit: exact
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
formal_projection_sha256: b5893ec847314c358434c4dcdc65f45a3a7804d79528b94afeef070b58bbe2d9
status: indexed
last_updated: '2026-07-25'
---

# LA-046 初等矩阵幂的行列变换

## 正式投影

- 正式卡：`错题知识网络/错题卡/LA-046_强化例题3.6（152785）.md`
- formal projection SHA-256：`b5893ec847314c358434c4dcdc65f45a3a7804d79528b94afeef070b58bbe2d9`
- review batch：`MATHWIKI-REVIEW-084`

## 可视化来源

- live：`错题知识网络/可视化错题详情/线性代数/LA-046_强化例题3.6（152785）.md`（visual_id: `VIS-LA-046`）
- live：`错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-689_强化例题3.6（152785）.md`（visual_id: `MN4-GS-CH01-689`）
- question：`错题知识网络/assets/visual_wrong_questions/LA-046/question_01.png`
- solution：`错题知识网络/assets/visual_wrong_questions/LA-046/solution_01.png`
- question：`错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-689/question_01.png`
- solution：`错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-689/solution_01.png`

## 客观题面与答案

- 题面：计算左右两侧带幂的初等矩阵乘积。
- 答案：[[2,1],[-3,-4]]。
- 第一动作：先区分左乘作用于行、右乘作用于列，再处理幂次。

## 知识与方法投影

- 知识点：矩阵运算
- 方法：初等矩阵; 左乘行变换; 右乘列变换; 矩阵乘法顺序
- 主方法卡：L03-008
- 完整方法路线：L03-008

## 个人证据边界

个人错因和动作断点均为候选，等待用户独立复做确认；客观解析不能证明用户当时发生了方法失败。

## wrongnet 关联题

- 暂无强边
