---
wiki_id: SRC-WQ-GS-546
type: source_summary
title: GS-546 90742 积分数列级数求和
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-546_90742积分数列级数求和.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-546_90742,-2026.6.4.md
visual_ids:
- VIS-GS-546
wrongnet_refs:
- GS-546
knowledge:
- 无穷级数
- 定积分
- 三角换元
- 分部积分
- 华里士公式
- 交错级数
- 幂级数和函数
- 等比级数
error_causes:
- 题型识别失败
- 方法选择错误
- 概念混淆
- 过程跳步
methods:
- 先判型
- 三角换元
- 恒等变形
- 分部积分
- 递推关系
- 先导后积
- 等比级数求和
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-002_B4-CHAIN
- MATHWIKI-ERROR-CLUSTER-001_方法选择错误
- MATHWIKI-ERROR-CLUSTER-002_过程跳步
- MATHWIKI-ERROR-CLUSTER-003_题型识别失败
- MATHWIKI-ERROR-CLUSTER-006_概念混淆
- MATHWIKI-KNOWLEDGE-002_定积分
- MATHWIKI-KNOWLEDGE-005_无穷级数
- MATHWIKI-KNOWLEDGE-024_分部积分
- MATHWIKI-KNOWLEDGE-059_交错级数
- MATHWIKI-KNOWLEDGE-080_三角换元
- MATHWIKI-KNOWLEDGE-104_等比级数
- MATHWIKI-KNOWLEDGE-112_幂级数和函数
- MATHWIKI-KNOWLEDGE-138_华里士公式
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-007_分部积分
- MATHWIKI-METHOD-CLUSTER-028_三角换元
- MATHWIKI-METHOD-CLUSTER-195_先导后积
- MATHWIKI-METHOD-CLUSTER-227_恒等变形
- MATHWIKI-METHOD-CLUSTER-256_等比级数求和
- MATHWIKI-METHOD-CLUSTER-465_递推关系
- MATHWIKI-GS-ERROR-003_方法选择错误
- MATHWIKI-GS-ERROR-004_过程跳步
- MATHWIKI-GS-ERROR-005_题型识别失败
- MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
last_updated: '2026-07-24'
related_wrongnet_refs: []
formal_projection_sha256: cfceb48ab6beb5b4c9515880ecec68415c81e752bdccaa6393cc027c67470515
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-546/question_01.png
solution_asset_refs: []
reference_asset_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: allow
evidence_boundary: 个人错因只来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。
review_batch: MATHWIKI-REVIEW-074
---

# GS-546 90742 积分数列级数求和

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-546_90742积分数列级数求和.md`
- wrongnet ID：`GS-546`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-546_90742,-2026.6.4.md`（`VIS-GS-546`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、定积分、三角换元、分部积分、华里士公式、交错级数、幂级数和函数、等比级数
- 方法：先判型、三角换元、恒等变形、分部积分、递推关系、先导后积、等比级数求和
- 错因字段：题型识别失败、方法选择错误、概念混淆、过程跳步
- 第一动作：先对 \(a_n\) 作 \(x=\sin t\)，把 \(a_n\) 化为 \(b_n-b_{n+2}\)，再用 Wallis 递推求 \(b_{n+2}/b_n\)。
- 个人断点：停在交错级数判敛，没有先用三角换元和 Wallis 递推把 \(\frac{a_n}{b_n}\) 化成 \(\frac1{n+2}\)。
- 方法卡 ID：H11-009
- 当前强关系：暂无强边

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-059_交错级数]]
- [[MATHWIKI-KNOWLEDGE-080_三角换元]]
- [[MATHWIKI-KNOWLEDGE-104_等比级数]]
- [[MATHWIKI-KNOWLEDGE-112_幂级数和函数]]
- [[MATHWIKI-KNOWLEDGE-138_华里士公式]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-195_先导后积]]
- [[MATHWIKI-METHOD-CLUSTER-227_恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-256_等比级数求和]]
- [[MATHWIKI-METHOD-CLUSTER-465_递推关系]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
