---
wiki_id: SRC-WQ-LA-028
type: source_summary
title: LA-028 强化例题9.3(164730)
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-028_强化例题9.3(164730).md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-028_强化例题9.3(164730).md
- 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-664_强化例题9.3(164730).md
visual_ids:
- VIS-LA-028
- MN4-GS-CH01-664
provenance_alias_detail_refs: []
provenance_alias_visual_ids: []
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-028/question_01.png
- 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-664/question_01.png
solution_asset_refs: []
reference_asset_refs: []
provenance_alias_asset_refs: []
adjudicated_asset_roles:
- path: 错题知识网络/assets/visual_wrong_questions/LA-028/question_01.png
  sha256: cf0b5b6fc0956e28260221bf0b03eef40e4367443c2882fc7052fe006fc55257
  raw_role: question
  role: question
  evidence_scope: live_evidence
- path: 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-664/question_01.png
  sha256: cf0b5b6fc0956e28260221bf0b03eef40e4367443c2882fc7052fe006fc55257
  raw_role: question
  role: question
  evidence_scope: live_evidence
registered_raw_asset_role_counts:
  question: 2
  solution: 0
  reference: 0
wrongnet_refs:
- LA-028
related_wrongnet_refs: []
knowledge:
- 二次型
- 实对称矩阵
- 特征值与特征向量
error_causes:
- 个人错因候选待确认；没有用户真实作答过程。
answer: a=4，合同条件 k>0；若要求正交变换，则 k=3，Q 取按特征值 3、6、0 排列的单位正交特征向量矩阵。
methods:
- 合同变换
- 惯性指数
- 正交对角化
- 特征值匹配
traps:
- 合同与正交相似混淆
- 只由 detA=0 得到 a 后忘记 k 的范围
- 正交矩阵列向量顺序要匹配对角元
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-KNOWLEDGE-016_特征值与特征向量
- MATHWIKI-KNOWLEDGE-034_二次型
- MATHWIKI-KNOWLEDGE-056_实对称矩阵
- MATHWIKI-METHOD-CLUSTER-093_合同变换
- MATHWIKI-METHOD-CLUSTER-168_正交对角化
- MATHWIKI-METHOD-CLUSTER-228_惯性指数
- MATHWIKI-METHOD-CLUSTER-428_特征值匹配
- MATHWIKI-LA-METHOD-019_二次型矩阵化与惯性规范形
- MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线
related_method_card_id: L09-008
related_method_card_ids:
- L09-008
- L09-003
secondary_method_card_ids:
- L09-003
method_route_fit: composite_registered_route
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
formal_projection_sha256: d38b0d22facdd14d345012ba6f3274a8b92f7ad309cd8c397a8a3f8fc1b99a4f
status: indexed
last_updated: '2026-07-25'
---

# LA-028 强化例题9.3(164730)

## 正式投影

- 正式卡：`错题知识网络/错题卡/LA-028_强化例题9.3(164730).md`
- formal projection SHA-256：`d38b0d22facdd14d345012ba6f3274a8b92f7ad309cd8c397a8a3f8fc1b99a4f`
- review batch：`MATHWIKI-REVIEW-084`

## 可视化来源

- live：`错题知识网络/可视化错题详情/线性代数/LA-028_强化例题9.3(164730).md`（visual_id: `VIS-LA-028`）
- live：`错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-664_强化例题9.3(164730).md`（visual_id: `MN4-GS-CH01-664`）
- question：`错题知识网络/assets/visual_wrong_questions/LA-028/question_01.png`
- question：`错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-664/question_01.png`

## 客观题面与答案

- 题面：A=[[4,1,-2],[1,1,1],[-2,1,a]] 与 diag(k,6,0) 合同；再问何时可正交合同及对应 Q。
- 答案：合同部分 a=4 且 k>0；正交部分 k=3。可取 Q 的列依次为 (1,1,1)^T/sqrt(3)、(-1,0,1)^T/sqrt(2)、(1,-2,1)^T/sqrt(6)。
- 第一动作：先用秩或行列式确定 a，再分开检查合同保持量与正交变换保持量。

## 知识与方法投影

- 知识点：二次型; 实对称矩阵; 特征值与特征向量
- 方法：合同变换; 惯性指数; 正交对角化; 特征值匹配
- 主方法卡：L09-008
- 完整方法路线：L09-008 → L09-003

## 个人证据边界

个人错因和动作断点均为候选，等待用户独立复做确认；客观解析不能证明用户当时发生了方法失败。

## wrongnet 关联题

- 暂无强边
