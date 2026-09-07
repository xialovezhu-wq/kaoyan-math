---
wiki_id: SRC-WQ-GS-596
type: source_summary
title: GS-596 138755 部分和裂项判敛
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-596_138755部分和裂项判敛.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-596_138755.md
visual_ids:
- VIS-GS-596
wrongnet_refs:
- GS-596
related_wrongnet_refs: []
knowledge:
- 无穷级数
- 数项级数敛散性判别
- 正项级数敛散性判别
- 部分和数列
- 级数拆项
error_causes:
- 方法论调取不稳
- 动作链断裂
- 方法选择错误
- 结构整理断点
- 部分和数列与级数通项混淆
- 等式变形与不等式放缩混淆
methods:
- 先判型
- 比较判别法
- 部分和定义
- 部分和有界
- 裂项相消
- 望远镜求和
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-002
- MATHWIKI-ERROR-CLUSTER-001
- MATHWIKI-ERROR-CLUSTER-004
- MATHWIKI-ERROR-CLUSTER-021
- MATHWIKI-ERROR-CLUSTER-035
- MATHWIKI-ERROR-CLUSTER-616
- MATHWIKI-ERROR-CLUSTER-617
- MATHWIKI-KNOWLEDGE-005
- MATHWIKI-KNOWLEDGE-013
- MATHWIKI-KNOWLEDGE-029
- MATHWIKI-KNOWLEDGE-128
- MATHWIKI-KNOWLEDGE-129
- MATHWIKI-METHOD-CLUSTER-001
- MATHWIKI-METHOD-CLUSTER-012
- MATHWIKI-METHOD-CLUSTER-073
- MATHWIKI-METHOD-CLUSTER-133
- MATHWIKI-METHOD-CLUSTER-259
- MATHWIKI-METHOD-CLUSTER-263
- MATHWIKI-GS-ERROR-003_方法选择错误
- MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
last_updated: '2026-08-13'
formal_projection_sha256: 72a85c320277501cac083d757bae66c25ce7f906889711aea1d276832309f9d1
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-596/question_01.png
solution_asset_refs: []
reference_asset_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: block_strong_edges
evidence_boundary: "个人错因只来自 2026-08-12 本人作答、追问与确认；题图与详情解析只用于核对题面和客观方法。"
review_batch: MATH-NIGHTLY-2026-08-13
confirmation_state: confirmed
---

# GS-596 138755 部分和裂项判敛

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-596_138755部分和裂项判敛.md`
- wrongnet ID：`GS-596`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-596_138755.md`（`VIS-GS-596`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、数项级数敛散性判别、正项级数敛散性判别、部分和数列、级数拆项
- 方法：先判型、比较判别法、部分和定义、部分和有界、裂项相消、望远镜求和
- 错因字段：方法论调取不稳、动作链断裂、方法选择错误、结构整理断点、部分和数列与级数通项混淆、等式变形与不等式放缩混淆
- 第一动作：先写 \(a_n=S_n-S_{n-1}\)，把 \(\frac{a_n}{S_n^2}\) 改成 \(\frac{S_n-S_{n-1}}{S_n^2}\)。
- 个人断点：先把目标级数的部分和与单个通项混淆；随后未从“要找可求和上界”反推到“需要凑出 \(S_nS_{n-1}\)”，并将放缩误称为等式改写。
- 方法卡 ID：H16-015
- 正式强边：暂无强边（证据门禁未通过）。

## 证据边界

- 本轮个人错因来自 2026-08-12 本人作答、追问与确认；题图与详情叙述只核验客观内容。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳]]
- [[MATHWIKI-ERROR-CLUSTER-035_结构整理断点]]
- [[MATHWIKI-ERROR-CLUSTER-616_部分和数列与级数通项混淆]]
- [[MATHWIKI-ERROR-CLUSTER-617_等式变形与不等式放缩混淆]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-128_级数拆项]]
- [[MATHWIKI-KNOWLEDGE-129_部分和数列]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-073_望远镜求和]]
- [[MATHWIKI-METHOD-CLUSTER-133_部分和定义]]
- [[MATHWIKI-METHOD-CLUSTER-259_裂项相消]]
- [[MATHWIKI-METHOD-CLUSTER-263_部分和有界]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
