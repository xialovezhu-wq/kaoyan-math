---
wiki_id: SRC-WQ-GS-602
type: source_summary
title: GS-602 172987 速度积分平均速度
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-602_172987速度积分平均速度.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-602_172987.md
visual_ids:
- VIS-GS-602
wrongnet_refs:
- GS-602
knowledge:
- 定积分
- 定积分应用
- 定积分物理应用
- 反常积分
- 反常积分极限
- 根式换元
- 第二类换元
- 分部积分
error_causes:
- 题意翻译断点
- 方法论调取不稳
- 动作链断裂
- 换元上下限漏改
- 反常积分与定积分边界混淆
methods:
- 物理语言转定积分
- 速度积分求路程
- 平均速度公式
- 判断速度非负
- 根式换元
- 第二类换元
- 分部积分
- 反常积分计算
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-002_B4-CHAIN
- MATHWIKI-ERROR-CLUSTER-004_动作链断裂
- MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳
- MATHWIKI-ERROR-CLUSTER-063_题意翻译断点
- MATHWIKI-ERROR-CLUSTER-163_反常积分与定积分边界混淆
- MATHWIKI-ERROR-CLUSTER-225_换元上下限漏改
- MATHWIKI-KNOWLEDGE-002_定积分
- MATHWIKI-KNOWLEDGE-024_分部积分
- MATHWIKI-KNOWLEDGE-028_反常积分
- MATHWIKI-KNOWLEDGE-035_定积分应用
- MATHWIKI-KNOWLEDGE-041_第二类换元
- MATHWIKI-KNOWLEDGE-103_根式换元
- MATHWIKI-KNOWLEDGE-110_反常积分极限
- MATHWIKI-KNOWLEDGE-141_定积分物理应用
- MATHWIKI-METHOD-CLUSTER-007_分部积分
- MATHWIKI-METHOD-CLUSTER-044_第二类换元
- MATHWIKI-METHOD-CLUSTER-050_物理语言转定积分
- MATHWIKI-METHOD-CLUSTER-124_根式换元
- MATHWIKI-METHOD-CLUSTER-327_反常积分计算
- MATHWIKI-METHOD-CLUSTER-366_平均速度公式
- MATHWIKI-METHOD-CLUSTER-468_速度积分求路程
- MATHWIKI-METHOD-CLUSTER-702_判断速度非负
- MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点
- MATHWIKI-GS-METHOD-038_定积分物理应用微元法
- MATHWIKI-GS-TOPIC-006_定积分错题总线
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
last_updated: '2026-07-25'
related_wrongnet_refs: []
formal_projection_sha256: 48f9f759712b6368ea08ef3cb10fe71ed878aa2d3ab074f8f32445d97e45c24d
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-602/question_01.png
solution_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-602/solution_01.png
reference_asset_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: allow
evidence_boundary: "个人错因仅来自正式学习事务中的 wrong_history；视觉资产和客观解析不反推个人错因。"
review_batch: MATHWIKI-REVIEW-080
confirmation_state: confirmed
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
---

# GS-602 172987 速度积分平均速度

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-602_172987速度积分平均速度.md`
- wrongnet ID：`GS-602`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-602_172987.md`（`VIS-GS-602`）
- 题图 1 张；解析图 1 张；参考图 0 张。

## 当前语义投影

- 知识点：定积分、定积分应用、定积分物理应用、反常积分、反常积分极限、根式换元、第二类换元、分部积分
- 方法：物理语言转定积分、速度积分求路程、平均速度公式、判断速度非负、根式换元、第二类换元、分部积分、反常积分计算
- 错因字段：题意翻译断点、方法论调取不稳、动作链断裂、换元上下限漏改、反常积分与定积分边界混淆
- 第一动作：先判断 \(v(t)\ge0\)，再写总路程 \(s=\int_0^{+\infty}\sqrt t e^{-\sqrt t}\,dt\) 和平均速度 \(\bar v=\frac14\int_0^4\sqrt t e^{-\sqrt t}\,dt\)。
- 个人断点：没有先把速度函数积分为路程；第二问差点把总路程当作 \(0\) 到 \(4\) 秒内路程；令 \(u=\sqrt t\) 后没有稳定把上限 \(t=4\) 改成 \(u=2\)。
- 方法卡 ID：H12-002
- 当前强关系：暂无强边

## 证据边界

- 个人错因仅来自正式学习事务中的 wrong_history；视觉资产和客观解析不反推个人错因。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳]]
- [[MATHWIKI-ERROR-CLUSTER-063_题意翻译断点]]
- [[MATHWIKI-ERROR-CLUSTER-163_反常积分与定积分边界混淆]]
- [[MATHWIKI-ERROR-CLUSTER-225_换元上下限漏改]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-028_反常积分]]
- [[MATHWIKI-KNOWLEDGE-035_定积分应用]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-KNOWLEDGE-103_根式换元]]
- [[MATHWIKI-KNOWLEDGE-110_反常积分极限]]
- [[MATHWIKI-KNOWLEDGE-141_定积分物理应用]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-044_第二类换元]]
- [[MATHWIKI-METHOD-CLUSTER-050_物理语言转定积分]]
- [[MATHWIKI-METHOD-CLUSTER-124_根式换元]]
- [[MATHWIKI-METHOD-CLUSTER-327_反常积分计算]]
- [[MATHWIKI-METHOD-CLUSTER-366_平均速度公式]]
- [[MATHWIKI-METHOD-CLUSTER-468_速度积分求路程]]
- [[MATHWIKI-METHOD-CLUSTER-702_判断速度非负]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-038_定积分物理应用微元法]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
