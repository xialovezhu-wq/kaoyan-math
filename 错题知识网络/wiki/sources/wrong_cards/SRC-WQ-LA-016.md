---
wiki_id: SRC-WQ-LA-016
type: source_summary
title: LA-016 强化例题1.7
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-016_强化例题1.7.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-016_强化例题1.7.md
- 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-654_强化例题1.7.md
visual_ids:
- VIS-LA-016
- MN4-GS-CH01-654
wrongnet_refs:
- LA-016
knowledge:
- 伴随矩阵
- 伴随矩阵谱
- 特征值反推
- 矩阵多项式谱映射
- 行列式
error_causes:
- "方法触发：未触发 det(A*)→det(A)→A 的谱→p(A) 的谱→行列式转换链。"
- "知识：混淆伴随矩阵特征值与原矩阵特征值的乘除关系。"
- "概念：未区分标量多项式 p(t) 与矩阵多项式 p(A)。"
- "方法：不知道 det(p(A)) 由各 p(λ_i) 的乘积得到。"
methods:
- 伴随矩阵谱关系
- 谱映射
- 行列式等于特征值乘积
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-ACTION-GAP-002

- MATHWIKI-ERROR-CLUSTER-012

- MATHWIKI-KNOWLEDGE-016

- MATHWIKI-KNOWLEDGE-023

- MATHWIKI-KNOWLEDGE-135

- MATHWIKI-METHOD-CLUSTER-1325

- MATHWIKI-METHOD-CLUSTER-461

- MATHWIKI-METHOD-CLUSTER-596

- MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点
- MATHWIKI-LA-METHOD-015_矩阵多项式与特征值映射
- MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
last_updated: '2026-08-27'
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-016/question_01.png
- 错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-654/question_01.png
solution_asset_refs: []
reference_asset_refs: []
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
related_wrongnet_refs: []
evidence_status: user_observed
confirmation_state: confirmed
question_surface_status: registered_answer_safe_question_only
solution_surface_status: missing_solution_surface
aggregate_edge_policy: block_until_relinked
evidence_boundary: 题图和解析只核验客观题意与解法；个人错因按 evidence_status 门禁。
review_batch: MATHWIKI-REVIEW-082
formal_projection_sha256: 3b19d54410db7ce569ceb356b1532676ce95db21f272cf93fd74d052b2188179
---

# LA-016 强化例题1.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-016_强化例题1.7.md`
- wrongnet ID：`LA-016`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/线性代数/LA-016_强化例题1.7.md`（`VIS-LA-016`）
- 详情页：`错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-654_强化例题1.7.md`（`MN4-GS-CH01-654`）
- 题图 2 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：伴随矩阵、伴随矩阵谱、特征值反推、矩阵多项式谱映射、行列式
- 方法：伴随矩阵谱关系、谱映射、行列式等于特征值乘积
- 错因字段：谱转换链未触发；伴随谱乘除关系、标量与矩阵多项式对象及行列式乘积连接不稳。
- 第一动作：由 det(A*)=det(A)^3 求 det(A)，再反推 A 的特征值。
- 已确认个人断点：完整谱转换链依赖提示，未证明无提示独立启动。
- 方法卡 ID：L02-004
- 当前强关系：暂无强边

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-012_方法入口未沉淀]]
- [[MATHWIKI-KNOWLEDGE-016_特征值与特征向量]]
- [[MATHWIKI-KNOWLEDGE-023_行列式]]
- [[MATHWIKI-KNOWLEDGE-135_伴随矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-1325_行列式等于特征值乘积]]
- [[MATHWIKI-METHOD-CLUSTER-461_谱映射]]
- [[MATHWIKI-METHOD-CLUSTER-596_伴随矩阵谱关系]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-LA-METHOD-015_矩阵多项式与特征值映射]]
- [[MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
