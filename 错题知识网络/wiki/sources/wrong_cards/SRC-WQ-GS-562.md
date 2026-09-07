---
wiki_id: SRC-WQ-GS-562
type: source_summary
title: GS-562 138670 泰勒中间点放缩判敛
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-562_138670泰勒中间点放缩判敛.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-562_138670.md
visual_ids:
- VIS-GS-562
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-562/question_01.png
solution_asset_refs: []
reference_asset_refs: []
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
identity_peer_refs: []
wrongnet_refs:
- GS-562
related_wrongnet_refs: []
knowledge:
- 无穷级数
- 数项级数敛散性判别
- 任意项级数
- 绝对收敛
- 正项级数比较判别法
- 泰勒公式
- 拉格朗日余项
- 导数定义
- 一元函数微分学应用
- p级数
methods:
- 先判型
- 导数定义
- 二阶泰勒公式
- 拉格朗日余项
- 局部有界
- 绝对值放缩
- 比较判别法
- p级数判别
error_causes:
- 概念混淆
- 条件忽略
- 过程跳步
wiki_refs:
- MATHWIKI-COVERAGE-GS
- MATHWIKI-ACTION-GAP-002
- MATHWIKI-ERROR-CLUSTER-002
- MATHWIKI-ERROR-CLUSTER-005
- MATHWIKI-ERROR-CLUSTER-006
- MATHWIKI-KNOWLEDGE-001
- MATHWIKI-KNOWLEDGE-005
- MATHWIKI-KNOWLEDGE-006
- MATHWIKI-KNOWLEDGE-013
- MATHWIKI-KNOWLEDGE-015
- MATHWIKI-KNOWLEDGE-032
- MATHWIKI-KNOWLEDGE-036
- MATHWIKI-KNOWLEDGE-074
- MATHWIKI-KNOWLEDGE-087
- MATHWIKI-KNOWLEDGE-255
- MATHWIKI-METHOD-CLUSTER-001
- MATHWIKI-METHOD-CLUSTER-012
- MATHWIKI-METHOD-CLUSTER-013
- MATHWIKI-METHOD-CLUSTER-027
- MATHWIKI-METHOD-CLUSTER-118
- MATHWIKI-METHOD-CLUSTER-178
- MATHWIKI-METHOD-CLUSTER-568
- MATHWIKI-METHOD-CLUSTER-952
- MATHWIKI-GS-ERROR-004
- MATHWIKI-GS-METHOD-010
- MATHWIKI-GS-METHOD-013
- MATHWIKI-GS-TOPIC-003
- MATHWIKI-GS-TOPIC-005
- MATHWIKI-SYNTHESIS-001
evidence_status: pending_user_confirmation
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: block_strong_edges
status: indexed
last_updated: '2026-07-24'
formal_projection_sha256: 0b30abd3d2e7e97fd5a45a5c80820356bde602955967618df2fefb07c2bc8f04
evidence_boundary: "个人错因待用户确认；题图与生成式详情不得作为 user_confirmed 证据。"
review_batch: MATHWIKI-REVIEW-076
---

# GS-562 138670 泰勒中间点放缩判敛

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-562_138670泰勒中间点放缩判敛.md`
- wrongnet ID：`GS-562`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-562_138670.md`（`VIS-GS-562`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、数项级数敛散性判别、任意项级数、绝对收敛、正项级数比较判别法、泰勒公式、拉格朗日余项、导数定义、一元函数微分学应用、p级数
- 方法：先判型、导数定义、二阶泰勒公式、拉格朗日余项、局部有界、绝对值放缩、比较判别法、p级数判别
- 错因字段：概念混淆、条件忽略、过程跳步
- 第一动作：先由 \(\lim_{x\to0}\frac{f(x)}x=0\) 推出 \(f(0)=0\) 和 \(f'(0)=0\)
- 候选个人断点（待确认）：用二阶泰勒后把 \(\xi_n\to0\) 误当成 \(\xi_n=0\)，没有改用 \(f''\) 连续推出局部有界来做绝对值放缩
- 方法卡 ID：H16-009
- 当前强关系：暂无强边

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS]]
- [[MATHWIKI-ACTION-GAP-002]]
- [[MATHWIKI-ERROR-CLUSTER-002]]
- [[MATHWIKI-ERROR-CLUSTER-005]]
- [[MATHWIKI-ERROR-CLUSTER-006]]
- [[MATHWIKI-KNOWLEDGE-001]]
- [[MATHWIKI-KNOWLEDGE-005]]
- [[MATHWIKI-KNOWLEDGE-006]]
- [[MATHWIKI-KNOWLEDGE-013]]
- [[MATHWIKI-KNOWLEDGE-015]]
- [[MATHWIKI-KNOWLEDGE-032]]
- [[MATHWIKI-KNOWLEDGE-036]]
- [[MATHWIKI-KNOWLEDGE-074]]
- [[MATHWIKI-KNOWLEDGE-087]]
- [[MATHWIKI-KNOWLEDGE-255]]
- [[MATHWIKI-METHOD-CLUSTER-001]]
- [[MATHWIKI-METHOD-CLUSTER-012]]
- [[MATHWIKI-METHOD-CLUSTER-013]]
- [[MATHWIKI-METHOD-CLUSTER-027]]
- [[MATHWIKI-METHOD-CLUSTER-118]]
- [[MATHWIKI-METHOD-CLUSTER-178]]
- [[MATHWIKI-METHOD-CLUSTER-568]]
- [[MATHWIKI-METHOD-CLUSTER-952]]
- [[MATHWIKI-GS-ERROR-004]]
- [[MATHWIKI-GS-METHOD-010]]
- [[MATHWIKI-GS-METHOD-013]]
- [[MATHWIKI-GS-TOPIC-003]]
- [[MATHWIKI-GS-TOPIC-005]]
- [[MATHWIKI-SYNTHESIS-001]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
