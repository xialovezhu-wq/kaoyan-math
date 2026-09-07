---
wiki_id: SRC-WQ-GS-592
type: source_summary
title: GS-592 57967 平均值三角换元
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-592_57967平均值三角换元.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-592_57967.md
visual_ids:
- VIS-GS-592
wrongnet_refs:
- GS-592
knowledge:
- 定积分
- 定积分应用
- 函数平均值
- 三角换元
- 三角恒等变形
error_causes:
- 题型识别失败
- 方法选择错误
- 过程跳步
methods:
- 平均值公式
- 先判型
- 三角换元
- 特殊角换限
- 降幂公式
- 定积分计算
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-003_B2-TRIGGER
- MATHWIKI-ERROR-CLUSTER-001_方法选择错误
- MATHWIKI-ERROR-CLUSTER-002_过程跳步
- MATHWIKI-ERROR-CLUSTER-003_题型识别失败
- MATHWIKI-KNOWLEDGE-002_定积分
- MATHWIKI-KNOWLEDGE-035_定积分应用
- MATHWIKI-KNOWLEDGE-043_三角恒等变形
- MATHWIKI-KNOWLEDGE-080_三角换元
- MATHWIKI-KNOWLEDGE-166_函数平均值
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-028_三角换元
- MATHWIKI-METHOD-CLUSTER-042_定积分计算
- MATHWIKI-METHOD-CLUSTER-136_降幂公式
- MATHWIKI-METHOD-CLUSTER-245_特殊角换限
- MATHWIKI-METHOD-CLUSTER-977_平均值公式
- MATHWIKI-GS-ERROR-003_方法选择错误
- MATHWIKI-GS-ERROR-004_过程跳步
- MATHWIKI-GS-ERROR-005_题型识别失败
status: indexed
last_updated: '2026-07-24'
related_wrongnet_refs: []
formal_projection_sha256: 9566923eee7eff842d58a5939ebfd52abf0c39bcaf1c752e3f1c307968632af3
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-592/question_01.png
solution_asset_refs: []
reference_asset_refs: []
evidence_status: legacy_unclassified
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: block_strong_edges
evidence_boundary: "个人错因待用户确认；题图、解析图与生成式详情仅核验客观内容，不得升级为 user_confirmed。"
review_batch: MATHWIKI-REVIEW-078
confirmation_state: pending_user_confirmation
---

# GS-592 57967 平均值三角换元

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-592_57967平均值三角换元.md`
- wrongnet ID：`GS-592`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-592_57967.md`（`VIS-GS-592`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：定积分、定积分应用、函数平均值、三角换元、三角恒等变形
- 方法：平均值公式、先判型、三角换元、特殊角换限、降幂公式、定积分计算
- 错因字段：题型识别失败、方法选择错误、过程跳步
- 第一动作：先令 \(x=\sin t\)，把积分限 \(\frac12,\frac{\sqrt3}{2}\) 改成 \(\frac{\pi}{6},\frac{\pi}{3}\)
- 候选个人断点（待确认）：没有把根式结构和特殊角端点转成三角换元，而是把 \(dx/\sqrt{1-x^2}\) 看成 \(d(\arcsin x)\) 后走分部积分
- 方法卡 ID：H09-003
- 正式强边：暂无强边（证据门禁未通过）。

## 证据边界

- 候选个人错因来自历史结构化字段，仍待用户确认；题图、解析图与详情叙述只核验客观内容。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-035_定积分应用]]
- [[MATHWIKI-KNOWLEDGE-043_三角恒等变形]]
- [[MATHWIKI-KNOWLEDGE-080_三角换元]]
- [[MATHWIKI-KNOWLEDGE-166_函数平均值]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-042_定积分计算]]
- [[MATHWIKI-METHOD-CLUSTER-136_降幂公式]]
- [[MATHWIKI-METHOD-CLUSTER-245_特殊角换限]]
- [[MATHWIKI-METHOD-CLUSTER-977_平均值公式]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
