---
wiki_id: SRC-WQ-GS-588
type: source_summary
title: GS-588 138721 相邻项递推判散
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-588_138721相邻项递推判散.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-588_138721.md
visual_ids:
- VIS-GS-588
wrongnet_refs:
- GS-588
knowledge:
- 无穷级数
- 数项级数敛散性判别
- 正项级数敛散性判别
- 正项级数比较判别法
- 相邻项递推不等式
- 比值判别法边界失效
- 调和级数
error_causes:
- 方法选择错误
- 概念混淆
- 题型识别失败
- 动作链断裂
- 比值判别法误用
- 发散概念混淆
methods:
- 先判型
- 正项前置判断
- 条件转化
- 递推不等式变形
- 构造辅助数列
- 比值判别法边界检查
- 比较判别法
- 下界比较
- 调和级数比较
- 反例法
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-002_B4-CHAIN
- MATHWIKI-ERROR-CLUSTER-001_方法选择错误
- MATHWIKI-ERROR-CLUSTER-003_题型识别失败
- MATHWIKI-ERROR-CLUSTER-004_动作链断裂
- MATHWIKI-ERROR-CLUSTER-006_概念混淆
- MATHWIKI-ERROR-CLUSTER-168_发散概念混淆
- MATHWIKI-ERROR-CLUSTER-381_比值判别法误用
- MATHWIKI-KNOWLEDGE-005_无穷级数
- MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别
- MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别
- MATHWIKI-KNOWLEDGE-032_正项级数比较判别法
- MATHWIKI-KNOWLEDGE-097_调和级数
- MATHWIKI-KNOWLEDGE-397_比值判别法边界失效
- MATHWIKI-KNOWLEDGE-411_相邻项递推不等式
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-002_条件转化
- MATHWIKI-METHOD-CLUSTER-012_比较判别法
- MATHWIKI-METHOD-CLUSTER-074_正项前置判断
- MATHWIKI-METHOD-CLUSTER-112_反例法
- MATHWIKI-METHOD-CLUSTER-1157_比值判别法边界检查
- MATHWIKI-METHOD-CLUSTER-1373_递推不等式变形
- MATHWIKI-METHOD-CLUSTER-275_下界比较
- MATHWIKI-METHOD-CLUSTER-406_构造辅助数列
- MATHWIKI-METHOD-CLUSTER-460_调和级数比较
- MATHWIKI-GS-ERROR-003_方法选择错误
- MATHWIKI-GS-ERROR-005_题型识别失败
- MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
last_updated: '2026-07-24'
related_wrongnet_refs: []
formal_projection_sha256: 98468e85b82b4ec7977b24d087426b578db4e4af32be28b9d1f758ba41b60fff
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-588/question_01.png
solution_asset_refs: []
reference_asset_refs: []
evidence_status: legacy_unclassified
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: block_strong_edges
evidence_boundary: "个人错因待用户确认；题图、解析图与生成式详情仅核验客观内容，不得升级为 user_confirmed。"
review_batch: MATHWIKI-REVIEW-078
confirmation_state: pending_user_confirmation
---

# GS-588 138721 相邻项递推判散

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-588_138721相邻项递推判散.md`
- wrongnet ID：`GS-588`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-588_138721.md`（`VIS-GS-588`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、数项级数敛散性判别、正项级数敛散性判别、正项级数比较判别法、相邻项递推不等式、比值判别法边界失效、调和级数
- 方法：先判型、正项前置判断、条件转化、递推不等式变形、构造辅助数列、比值判别法边界检查、比较判别法、下界比较、调和级数比较、反例法
- 错因字段：方法选择错误、概念混淆、题型识别失败、动作链断裂、比值判别法误用、发散概念混淆
- 第一动作：先移项写 \(\frac{a_{n+1}}{a_n}>\frac{n-1}{n}\)，再同乘得到 \(na_{n+1}>(n-1)a_n\)
- 候选个人断点（待确认）：直接把下界 \(1-\frac1n\) 当成比值大于 1，误套比值判别法；没有构造 \(b_n=(n-1)a_n\)，也把级数发散误解成 \(a_n\to+\infty\)
- 方法卡 ID：H16-011
- 正式强边：暂无强边（证据门禁未通过）。

## 证据边界

- 候选个人错因来自历史结构化字段，仍待用户确认；题图、解析图与详情叙述只核验客观内容。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-168_发散概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-381_比值判别法误用]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-032_正项级数比较判别法]]
- [[MATHWIKI-KNOWLEDGE-097_调和级数]]
- [[MATHWIKI-KNOWLEDGE-397_比值判别法边界失效]]
- [[MATHWIKI-KNOWLEDGE-411_相邻项递推不等式]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-074_正项前置判断]]
- [[MATHWIKI-METHOD-CLUSTER-112_反例法]]
- [[MATHWIKI-METHOD-CLUSTER-1157_比值判别法边界检查]]
- [[MATHWIKI-METHOD-CLUSTER-1373_递推不等式变形]]
- [[MATHWIKI-METHOD-CLUSTER-275_下界比较]]
- [[MATHWIKI-METHOD-CLUSTER-406_构造辅助数列]]
- [[MATHWIKI-METHOD-CLUSTER-460_调和级数比较]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
