---
wiki_id: SRC-WQ-LA-029
type: source_summary
title: LA-029 线代基础6.6
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-029_线代基础6.6.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-029_缺图登记-线代基础6.6.md
visual_ids:
- VIS-LA-029
provenance_alias_detail_refs: []
provenance_alias_visual_ids: []
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-029/question_01.png
solution_asset_refs: []
reference_asset_refs: []
provenance_alias_asset_refs: []
adjudicated_asset_roles:
- path: 错题知识网络/assets/visual_wrong_questions/LA-029/question_01.png
  sha256: efd1167ae4539f58eb8aa760a52b504c57ed02d3956231df16bb27fb4b7fc5d4
  raw_role: question
  role: question
  evidence_scope: live_evidence
registered_raw_asset_role_counts:
  question: 1
  solution: 0
  reference: 0
wrongnet_refs:
- LA-029
related_wrongnet_refs: []
knowledge:
- 二次型
- 实对称矩阵
- 特征值与特征向量
- 行列式
error_causes:
- 个人错因候选待确认；没有用户真实作答过程。
answer: a=4，b=1，Q=[[0,1],[-1,0]]
methods:
- 等价变形
- 换元
- 条件转化
- 特征分解
traps:
- 参数边界
- 变量混淆
- 可逆性
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-KNOWLEDGE-016_特征值与特征向量
- MATHWIKI-KNOWLEDGE-023_行列式
- MATHWIKI-KNOWLEDGE-034_二次型
- MATHWIKI-KNOWLEDGE-056_实对称矩阵
- MATHWIKI-METHOD-CLUSTER-002_条件转化
- MATHWIKI-METHOD-CLUSTER-003_等价变形
- MATHWIKI-METHOD-CLUSTER-009_换元
- MATHWIKI-METHOD-CLUSTER-023_特征分解
- MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点
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
formal_projection_sha256: a84ee5d8e48b11b9163ac066c4dc13bd1fd4768c1225d53d6e5eb49ad83889aa
status: indexed
last_updated: '2026-07-25'
---

# LA-029 线代基础6.6

## 正式投影

- 正式卡：`错题知识网络/错题卡/LA-029_线代基础6.6.md`
- formal projection SHA-256：`a84ee5d8e48b11b9163ac066c4dc13bd1fd4768c1225d53d6e5eb49ad83889aa`
- review batch：`MATHWIKI-REVIEW-084`

## 可视化来源

- live：`错题知识网络/可视化错题详情/线性代数/LA-029_缺图登记-线代基础6.6.md`（visual_id: `VIS-LA-029`）
- question：`错题知识网络/assets/visual_wrong_questions/LA-029/question_01.png`

## 客观题面与答案

- 题面：f=x1^2-4x1x2+a x2^2 经正交变换化为 g=4y1^2+4y1y2+b y2^2，求 a,b,Q。
- 答案：a=4，b=1；可取 Q=[[0,1],[-1,0]]，满足 Q^T[[1,-2],[-2,4]]Q=[[4,2],[2,1]]。
- 第一动作：先写两个实对称矩阵，用迹与行列式确定参数。

## 知识与方法投影

- 知识点：二次型; 实对称矩阵; 特征值与特征向量; 行列式
- 方法：等价变形; 换元; 条件转化; 特征分解
- 主方法卡：L09-003
- 完整方法路线：L09-003

## 个人证据边界

个人错因和动作断点均为候选，等待用户独立复做确认；客观解析不能证明用户当时发生了方法失败。

## wrongnet 关联题

- 暂无强边
