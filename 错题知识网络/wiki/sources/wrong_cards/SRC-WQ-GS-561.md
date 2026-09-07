---
wiki_id: SRC-WQ-GS-561
type: source_summary
title: GS-561 138659 对数展开阶数判敛
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-561_138659对数展开阶数判敛.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-561_138659.md
visual_ids:
- VIS-GS-561
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-561/question_01.png
solution_asset_refs: []
reference_asset_refs: []
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
identity_peer_refs: []
wrongnet_refs:
- GS-561
related_wrongnet_refs: []
knowledge:
- 无穷级数
- 数项级数敛散性判别
- 正项级数敛散性判别
- 正项级数比较判别法
- 极限比较判别法
- 基本展开型f(n)
- 等价无穷小
- 泰勒公式
- p级数
methods:
- 先判型
- 基本展开型f(n)
- 对数泰勒展开
- 泰勒展开
- 首个非零主项
- 极限比较判别法
- p级数判别
error_causes:
- 公式记错
- 过程跳步
wiki_refs:
- MATHWIKI-COVERAGE-GS
- MATHWIKI-ACTION-GAP-002
- MATHWIKI-ERROR-CLUSTER-001
- MATHWIKI-ERROR-CLUSTER-002
- MATHWIKI-ERROR-CLUSTER-015
- MATHWIKI-KNOWLEDGE-004
- MATHWIKI-KNOWLEDGE-005
- MATHWIKI-KNOWLEDGE-013
- MATHWIKI-KNOWLEDGE-015
- MATHWIKI-KNOWLEDGE-029
- MATHWIKI-KNOWLEDGE-032
- MATHWIKI-KNOWLEDGE-036
- MATHWIKI-KNOWLEDGE-061
- MATHWIKI-KNOWLEDGE-172
- MATHWIKI-METHOD-CLUSTER-001
- MATHWIKI-METHOD-CLUSTER-008
- MATHWIKI-METHOD-CLUSTER-027
- MATHWIKI-METHOD-CLUSTER-033
- MATHWIKI-METHOD-CLUSTER-115
- MATHWIKI-METHOD-CLUSTER-267
- MATHWIKI-METHOD-CLUSTER-919
- MATHWIKI-GS-ERROR-003
- MATHWIKI-GS-ERROR-004
- MATHWIKI-GS-METHOD-010
- MATHWIKI-GS-METHOD-012
- MATHWIKI-GS-TOPIC-003
- MATHWIKI-GS-TOPIC-004
- MATHWIKI-SYNTHESIS-001
evidence_status: pending_user_confirmation
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: block_strong_edges
status: indexed
last_updated: '2026-07-24'
formal_projection_sha256: 2793b712f348dd56bc2a5c7923c22ccad391f263be48e89fdc918296460a50bc
evidence_boundary: "个人错因待用户确认；题图与生成式详情不得作为 user_confirmed 证据。"
review_batch: MATHWIKI-REVIEW-076
---

# GS-561 138659 对数展开阶数判敛

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-561_138659对数展开阶数判敛.md`
- wrongnet ID：`GS-561`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-561_138659.md`（`VIS-GS-561`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、数项级数敛散性判别、正项级数敛散性判别、正项级数比较判别法、极限比较判别法、基本展开型f(n)、等价无穷小、泰勒公式、p级数
- 方法：先判型、基本展开型f(n)、对数泰勒展开、泰勒展开、首个非零主项、极限比较判别法、p级数判别
- 错因字段：公式记错、过程跳步
- 第一动作：先把 \(\ln(1+\frac1n)\) 展开到 \(\frac1{n^3}\) 项，再乘 \(n+\frac12\) 找首个非零主项
- 候选个人断点（待确认）：把 \(\ln(1+x)\) 的二阶符号写错，并只展开到二阶，漏掉三阶项经外层 \(n\) 放大后形成的 \(\frac1{n^2}\) 主项
- 方法卡 ID：H16-005
- 当前强关系：暂无强边

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS]]
- [[MATHWIKI-ACTION-GAP-002]]
- [[MATHWIKI-ERROR-CLUSTER-001]]
- [[MATHWIKI-ERROR-CLUSTER-002]]
- [[MATHWIKI-ERROR-CLUSTER-015]]
- [[MATHWIKI-KNOWLEDGE-004]]
- [[MATHWIKI-KNOWLEDGE-005]]
- [[MATHWIKI-KNOWLEDGE-013]]
- [[MATHWIKI-KNOWLEDGE-015]]
- [[MATHWIKI-KNOWLEDGE-029]]
- [[MATHWIKI-KNOWLEDGE-032]]
- [[MATHWIKI-KNOWLEDGE-036]]
- [[MATHWIKI-KNOWLEDGE-061]]
- [[MATHWIKI-KNOWLEDGE-172]]
- [[MATHWIKI-METHOD-CLUSTER-001]]
- [[MATHWIKI-METHOD-CLUSTER-008]]
- [[MATHWIKI-METHOD-CLUSTER-027]]
- [[MATHWIKI-METHOD-CLUSTER-033]]
- [[MATHWIKI-METHOD-CLUSTER-115]]
- [[MATHWIKI-METHOD-CLUSTER-267]]
- [[MATHWIKI-METHOD-CLUSTER-919]]
- [[MATHWIKI-GS-ERROR-003]]
- [[MATHWIKI-GS-ERROR-004]]
- [[MATHWIKI-GS-METHOD-010]]
- [[MATHWIKI-GS-METHOD-012]]
- [[MATHWIKI-GS-TOPIC-003]]
- [[MATHWIKI-GS-TOPIC-004]]
- [[MATHWIKI-SYNTHESIS-001]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
