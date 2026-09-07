---
wiki_id: SRC-WQ-LA-064
type: source_summary
title: LA-064 AB等于A的解空间参数
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-064_1000题B组3.11-3.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-064_1000题B组3.11-3.md
visual_ids:
- VIS-LA-064
wrongnet_refs:
- LA-064
knowledge:
- 矩阵方程
- 零空间
- 基础解系
- 解空间参数化
error_causes:
- 个人错因待确认；旧导入与客观解析只支持复做风险，不证明用户本人断点。
methods:
- 矩阵方程整理
- 齐次方程组基础解系
- 列向量关系转齐次解
- 秩与自由变量判断
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-ACTION-GAP-001_B3-METHOD
- MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）
- MATHWIKI-KNOWLEDGE-014_矩阵运算
- MATHWIKI-KNOWLEDGE-025_矩阵秩
- MATHWIKI-KNOWLEDGE-033_线性方程组
- MATHWIKI-KNOWLEDGE-202_基础解系
- MATHWIKI-METHOD-CLUSTER-104_齐次方程组基础解系
- MATHWIKI-METHOD-CLUSTER-249_矩阵方程整理
- MATHWIKI-METHOD-CLUSTER-317_列向量关系转齐次解
- MATHWIKI-METHOD-CLUSTER-438_秩与自由变量判断
- MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点
- MATHWIKI-LA-METHOD-012_矩阵方程按列拆与解空间参数化
- MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线
- MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
last_updated: '2026-07-25'
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-064/question_01.png
solution_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-064/solution_01.png
reference_asset_refs: []
related_wrongnet_refs: []
identity_refs: []
evidence_status: pending_user_confirmation
question_surface_status: registered_question_image_reviewed_no_user_answer_marks_found
solution_surface_status: registered_solution_image_objective_only_not_personal_evidence
aggregate_edge_policy: block_strong_edges
evidence_boundary: Question, source and solution material verify objective content only and must not be used to infer a personal breakpoint.
review_batch: MATHWIKI-REVIEW-086
content_review_status: verified
atomic_problem_status: verified_atomic
personal_diagnosis_status: candidate_pending_user_confirmation
formal_projection_sha256: 9360c6466461a2a66a3ccfcce103ce3734b242d6cc0845c77006b7c0b39d9ff6
---

# LA-064 AB等于A的解空间参数

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-064_1000题B组3.11-3.md`
- wrongnet ID：`LA-064`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/线性代数/LA-064_1000题B组3.11-3.md`（`VIS-LA-064`）
- 题图 1 张；解析图 1 张；参考图 0 张。

## 当前语义投影

- 知识点：矩阵方程、零空间、基础解系、解空间参数化
- 方法：矩阵方程整理、齐次方程组基础解系、列向量关系转齐次解、秩与自由变量判断
- 错因字段：个人错因待确认；旧导入与客观解析只支持复做风险，不证明用户本人断点。
- 第一动作：客观第一动作：先写 \(A(B-E)=O\)，再求齐次方程 \(Ax=0\) 的基础解系
- 个人断点：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是错误左消 \(A\)，没有转成零空间参数化
- 方法卡 ID：L03-010
- 当前强关系：暂无强边

## 证据边界

- 题图与解析只核验客观题意和解法；个人错因保持 pending_user_confirmation，候选 method-gap 保持 disabled。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-033_线性方程组]]
- [[MATHWIKI-KNOWLEDGE-202_基础解系]]
- [[MATHWIKI-METHOD-CLUSTER-104_齐次方程组基础解系]]
- [[MATHWIKI-METHOD-CLUSTER-249_矩阵方程整理]]
- [[MATHWIKI-METHOD-CLUSTER-317_列向量关系转齐次解]]
- [[MATHWIKI-METHOD-CLUSTER-438_秩与自由变量判断]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-012_矩阵方程按列拆与解空间参数化]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- [[MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]

## 解析图量词边界

- 解析图把“\(A\) 奇异”直接写成“\(B-E\ne O\)”并不严谨，因为 \(B=E\) 始终满足 \(AB=A\)。
- 正确的存在性表述是：\(A\) 奇异使齐次方程 \(Ax=0\) 有非零解，因此可以让 \(B-E\) 至少有一列取非零解，从而存在非单位矩阵 \(B\)。
- 写出全部解后，题目要求 \(B\ne E\)，所以参数 \(k_1,k_2,k_3\) 不能全为零。
- 该说明只修正文数量词；原 `solution_01.png` 保持字节不变。
