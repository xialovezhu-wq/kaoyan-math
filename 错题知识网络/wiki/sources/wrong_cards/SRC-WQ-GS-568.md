---
wiki_id: SRC-WQ-GS-568
type: source_summary
title: GS-568 138709 抽象级数反例判定
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-568_138709抽象级数反例判定.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-568_138709.md
visual_ids:
- VIS-GS-568
wrongnet_refs:
- GS-568
related_wrongnet_refs: []
knowledge:
- 无穷级数
- 数项级数敛散性判别
- 正项级数敛散性判别
- 正项级数比较判别法
- 级数收敛必要条件
- p级数
- 调和级数
error_causes:
- 方法选择错误
- 过程跳步
- 概念混淆
- 题型识别失败
methods:
- 先判型
- 正项前置判断
- 条件转化
- 比较判别法
- 构造上界
- 特殊值检验
- 反例法
- 分类讨论
- 通项趋零
- p级数判别
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-003_B2-TRIGGER
- MATHWIKI-ERROR-CLUSTER-001_方法选择错误
- MATHWIKI-ERROR-CLUSTER-002_过程跳步
- MATHWIKI-ERROR-CLUSTER-003_题型识别失败
- MATHWIKI-ERROR-CLUSTER-006_概念混淆
- MATHWIKI-KNOWLEDGE-005_无穷级数
- MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别
- MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别
- MATHWIKI-KNOWLEDGE-032_正项级数比较判别法
- MATHWIKI-KNOWLEDGE-036_p级数
- MATHWIKI-KNOWLEDGE-062_级数收敛必要条件
- MATHWIKI-KNOWLEDGE-097_调和级数
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-002_条件转化
- MATHWIKI-METHOD-CLUSTER-004_分类讨论
- MATHWIKI-METHOD-CLUSTER-012_比较判别法
- MATHWIKI-METHOD-CLUSTER-027_p级数判别
- MATHWIKI-METHOD-CLUSTER-062_通项趋零
- MATHWIKI-METHOD-CLUSTER-074_正项前置判断
- MATHWIKI-METHOD-CLUSTER-075_特殊值检验
- MATHWIKI-METHOD-CLUSTER-112_反例法
- MATHWIKI-METHOD-CLUSTER-122_构造上界
- MATHWIKI-GS-ERROR-003_方法选择错误
- MATHWIKI-GS-ERROR-004_过程跳步
- MATHWIKI-GS-ERROR-005_题型识别失败
status: indexed
last_updated: '2026-07-24'
formal_projection_sha256: 62b4affd19510ad7fa3beafa3bc18a8f13a46212f368ef41bd3720aa59562fcd
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-568/question_01.png
solution_asset_refs: []
reference_asset_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: allow
evidence_boundary: "个人错因只来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-076
---

# GS-568 138709 抽象级数反例判定

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-568_138709抽象级数反例判定.md`
- wrongnet ID：`GS-568`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-568_138709.md`（`VIS-GS-568`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、数项级数敛散性判别、正项级数敛散性判别、正项级数比较判别法、级数收敛必要条件、p级数、调和级数
- 方法：先判型、正项前置判断、条件转化、比较判别法、构造上界、特殊值检验、反例法、分类讨论、通项趋零、p级数判别
- 错因字段：方法选择错误、过程跳步、概念混淆、题型识别失败
- 第一动作：先写“一定收敛=对任意 \(a_n>0\) 且 \(\sum a_n\) 发散都收敛；不一定=找一个满足题设但该选项发散的 \(a_n\)”
- 个人断点：只比较 \(a_n>1\) 与 \(0<a_n<1\) 时的局部大小，没有主动构造 \(a_n=\frac1{n+1}\) 排除②、构造 \(a_n=n\) 排除③，也没有优先检查④能否统一压到 \(\frac1{n^2}\)
- 方法卡 ID：H00-009
- 当前强关系：暂无强边

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-032_正项级数比较判别法]]
- [[MATHWIKI-KNOWLEDGE-036_p级数]]
- [[MATHWIKI-KNOWLEDGE-062_级数收敛必要条件]]
- [[MATHWIKI-KNOWLEDGE-097_调和级数]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-027_p级数判别]]
- [[MATHWIKI-METHOD-CLUSTER-062_通项趋零]]
- [[MATHWIKI-METHOD-CLUSTER-074_正项前置判断]]
- [[MATHWIKI-METHOD-CLUSTER-075_特殊值检验]]
- [[MATHWIKI-METHOD-CLUSTER-112_反例法]]
- [[MATHWIKI-METHOD-CLUSTER-122_构造上界]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
