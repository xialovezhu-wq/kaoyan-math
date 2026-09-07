---
wiki_id: SRC-WQ-GS-555
type: source_summary
title: GS-555 138805 对数阶乘判散
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-555_138805对数阶乘判散.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-555_138805-2026.6.6.md
visual_ids:
- VIS-GS-555
wrongnet_refs:
- GS-555
related_wrongnet_refs: []
knowledge:
- 无穷级数
- 数项级数敛散性判别
- 正项级数敛散性判别
- 正项级数比较判别法
- 对数型通项
- 阶乘放缩
- 对数调和级数
- 广义调和级数
error_causes:
- 方法选择错误
- 概念混淆
- 条件忽略
methods:
- 先判型
- 通项极限
- 对数整体放缩
- 阶乘与幂比较
- 比较判别法
- 下界比较
- 对数调和级数判别
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-003_B2-TRIGGER
- MATHWIKI-ERROR-CLUSTER-001_方法选择错误
- MATHWIKI-ERROR-CLUSTER-005_条件忽略
- MATHWIKI-ERROR-CLUSTER-006_概念混淆
- MATHWIKI-KNOWLEDGE-005_无穷级数
- MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别
- MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别
- MATHWIKI-KNOWLEDGE-032_正项级数比较判别法
- MATHWIKI-KNOWLEDGE-205_对数型通项
- MATHWIKI-KNOWLEDGE-252_广义调和级数
- MATHWIKI-KNOWLEDGE-346_对数调和级数
- MATHWIKI-KNOWLEDGE-430_阶乘放缩
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-012_比较判别法
- MATHWIKI-METHOD-CLUSTER-1400_阶乘与幂比较
- MATHWIKI-METHOD-CLUSTER-182_通项极限
- MATHWIKI-METHOD-CLUSTER-275_下界比较
- MATHWIKI-METHOD-CLUSTER-917_对数整体放缩
- MATHWIKI-METHOD-CLUSTER-923_对数调和级数判别
- MATHWIKI-GS-ERROR-003_方法选择错误
status: indexed
last_updated: '2026-07-24'
formal_projection_sha256: 449b9b2eab9995e09e85f5490c5c9ca7abc3307701b912ad95c3d72da21b3e52
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-555/question_01.png
solution_asset_refs: []
reference_asset_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: allow
evidence_boundary: 个人错因只来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。
review_batch: MATHWIKI-REVIEW-074
---

# GS-555 138805 对数阶乘判散

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-555_138805对数阶乘判散.md`
- wrongnet ID：`GS-555`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-555_138805-2026.6.6.md`（`VIS-GS-555`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、数项级数敛散性判别、正项级数敛散性判别、正项级数比较判别法、对数型通项、阶乘放缩、对数调和级数、广义调和级数
- 方法：先判型、通项极限、对数整体放缩、阶乘与幂比较、比较判别法、下界比较、对数调和级数判别
- 错因字段：方法选择错误、概念混淆、条件忽略
- 第一动作：先写出 \(n!<n^n\)，再对两边取对数得到 \(\ln(n!)<n\ln n\)
- 个人断点：只展开 \(\ln(n!)\) 并用 \(\ln k<k\) 得到错误比较对象，没有转向 \(n!<n^n\) 的整体放缩
- 方法卡 ID：H16-004
- 当前强关系：暂无强边

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。
- 原题图的下限保持为 `n=1`；字面原式首项无定义，不能判敛散。
- 只有明确改为 `n>=2` 的修正尾级数才可判定为发散。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-032_正项级数比较判别法]]
- [[MATHWIKI-KNOWLEDGE-205_对数型通项]]
- [[MATHWIKI-KNOWLEDGE-252_广义调和级数]]
- [[MATHWIKI-KNOWLEDGE-346_对数调和级数]]
- [[MATHWIKI-KNOWLEDGE-430_阶乘放缩]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-1400_阶乘与幂比较]]
- [[MATHWIKI-METHOD-CLUSTER-182_通项极限]]
- [[MATHWIKI-METHOD-CLUSTER-275_下界比较]]
- [[MATHWIKI-METHOD-CLUSTER-917_对数整体放缩]]
- [[MATHWIKI-METHOD-CLUSTER-923_对数调和级数判别]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
