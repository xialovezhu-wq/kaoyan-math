---
wiki_id: SRC-WQ-GS-559
type: source_summary
title: GS-559 138647 对数幂型判敛
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-559_138647对数幂型判敛.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-559_138647.md
visual_ids:
- VIS-GS-559
wrongnet_refs:
- GS-559
related_wrongnet_refs: []
knowledge:
- 无穷级数
- 数项级数敛散性判别
- 正项级数敛散性判别
- 正项级数比较判别法
- 通项恒等变形
- 对数型通项
- 对数幂型通项
- p级数
error_causes:
- 方法选择错误
- 过程跳步
- 计算失误
methods:
- 先判型
- 通项恒等变形
- 指数对数互化
- 对数恒等变形
- 对数放缩
- 比较判别法
- 上界比较
- p级数判别
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-002_B4-CHAIN
- MATHWIKI-ERROR-CLUSTER-001_方法选择错误
- MATHWIKI-ERROR-CLUSTER-002_过程跳步
- MATHWIKI-ERROR-CLUSTER-014_计算失误
- MATHWIKI-KNOWLEDGE-005_无穷级数
- MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别
- MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别
- MATHWIKI-KNOWLEDGE-032_正项级数比较判别法
- MATHWIKI-KNOWLEDGE-036_p级数
- MATHWIKI-KNOWLEDGE-205_对数型通项
- MATHWIKI-KNOWLEDGE-220_通项恒等变形
- MATHWIKI-KNOWLEDGE-345_对数幂型通项
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-012_比较判别法
- MATHWIKI-METHOD-CLUSTER-027_p级数判别
- MATHWIKI-METHOD-CLUSTER-159_指数对数互化
- MATHWIKI-METHOD-CLUSTER-181_通项恒等变形
- MATHWIKI-METHOD-CLUSTER-221_对数恒等变形
- MATHWIKI-METHOD-CLUSTER-521_上界比较
- MATHWIKI-METHOD-CLUSTER-916_对数放缩
- MATHWIKI-GS-ERROR-003_方法选择错误
- MATHWIKI-GS-ERROR-004_过程跳步
- MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
last_updated: '2026-07-24'
formal_projection_sha256: efe36e84a39d369ec2dc7c9e42abc0b5c5f961e4359408c45dbd1d1da985aacb
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-559/question_01.png
solution_asset_refs: []
reference_asset_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: allow
evidence_boundary: 个人错因只来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。
review_batch: MATHWIKI-REVIEW-074
---

# GS-559 138647 对数幂型判敛

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-559_138647对数幂型判敛.md`
- wrongnet ID：`GS-559`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-559_138647.md`（`VIS-GS-559`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、数项级数敛散性判别、正项级数敛散性判别、正项级数比较判别法、通项恒等变形、对数型通项、对数幂型通项、p级数
- 方法：先判型、通项恒等变形、指数对数互化、对数恒等变形、对数放缩、比较判别法、上界比较、p级数判别
- 错因字段：方法选择错误、过程跳步、计算失误
- 第一动作：先写出 \((\ln n)^{\ln n}=e^{\ln n\cdot\ln(\ln n)}\)
- 个人断点：化简时误写成 \(\ln(\ln n+1)\)，并且没有继续用 \(\ln(\ln n)>2\) 推出分母大于 \(n^2\)
- 方法卡 ID：H16-002
- 当前强关系：暂无强边

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。
- 原题图的下限保持为 `n=1`；字面原式首项无定义，不能判敛散。
- 只有明确改为 `n>=2` 的修正尾级数才可判定为收敛。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-032_正项级数比较判别法]]
- [[MATHWIKI-KNOWLEDGE-036_p级数]]
- [[MATHWIKI-KNOWLEDGE-205_对数型通项]]
- [[MATHWIKI-KNOWLEDGE-220_通项恒等变形]]
- [[MATHWIKI-KNOWLEDGE-345_对数幂型通项]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-027_p级数判别]]
- [[MATHWIKI-METHOD-CLUSTER-159_指数对数互化]]
- [[MATHWIKI-METHOD-CLUSTER-181_通项恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-221_对数恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-521_上界比较]]
- [[MATHWIKI-METHOD-CLUSTER-916_对数放缩]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
