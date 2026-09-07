---
wiki_id: SRC-WQ-GS-544
type: source_summary
title: GS-544 78933 幂级数收敛域和函数
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-544_78933幂级数收敛域和函数.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-544_78933，2026.6.4.md
visual_ids:
- VIS-GS-544
wrongnet_refs:
- GS-544
knowledge:
- 无穷级数
- 幂级数
- 幂级数收敛域
- 幂级数和函数
- 缺项幂级数
- 幂级数逐项积分
- 交错级数
- 莱布尼茨判别法
- 反正切函数展开
error_causes:
- 题型识别失败
- 方法选择错误
- 概念混淆
- 条件忽略
- 方法论调取不稳
- 动作链断裂
- 端点检查概念混淆
- 交错级数判别结论误解
- 辅助函数记号混淆
methods:
- 先判型
- 比值判别法
- 整体通项比值
- 端点单独讨论
- 莱布尼茨判别法
- 逐项积分
- 先积后导
- 无穷等比级数求和
- 反正切函数展开
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-002_B4-CHAIN
- MATHWIKI-ERROR-CLUSTER-001_方法选择错误
- MATHWIKI-ERROR-CLUSTER-003_题型识别失败
- MATHWIKI-ERROR-CLUSTER-004_动作链断裂
- MATHWIKI-ERROR-CLUSTER-005_条件忽略
- MATHWIKI-ERROR-CLUSTER-006_概念混淆
- MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳
- MATHWIKI-ERROR-CLUSTER-115_交错级数判别结论误解
- MATHWIKI-ERROR-CLUSTER-397_端点检查概念混淆
- MATHWIKI-ERROR-CLUSTER-433_辅助函数记号混淆
- MATHWIKI-KNOWLEDGE-005_无穷级数
- MATHWIKI-KNOWLEDGE-048_幂级数
- MATHWIKI-KNOWLEDGE-059_交错级数
- MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法
- MATHWIKI-KNOWLEDGE-092_幂级数收敛域
- MATHWIKI-KNOWLEDGE-112_幂级数和函数
- MATHWIKI-KNOWLEDGE-176_幂级数逐项积分
- MATHWIKI-KNOWLEDGE-244_反正切函数展开
- MATHWIKI-KNOWLEDGE-269_缺项幂级数
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法
- MATHWIKI-METHOD-CLUSTER-098_比值判别法
- MATHWIKI-METHOD-CLUSTER-1066_无穷等比级数求和
- MATHWIKI-METHOD-CLUSTER-128_端点单独讨论
- MATHWIKI-METHOD-CLUSTER-132_逐项积分
- MATHWIKI-METHOD-CLUSTER-233_整体通项比值
- MATHWIKI-METHOD-CLUSTER-622_先积后导
- MATHWIKI-METHOD-CLUSTER-793_反正切函数展开
- MATHWIKI-GS-ERROR-003_方法选择错误
- MATHWIKI-GS-ERROR-005_题型识别失败
- MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点
- MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
last_updated: '2026-07-24'
related_wrongnet_refs:
- GS-511
formal_projection_sha256: e8b7e6813c287ea382704945ed045cd384076c352536720776be5c88b282496c
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-544/question_01.png
solution_asset_refs: []
reference_asset_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: allow
evidence_boundary: 个人错因只来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。
review_batch: MATHWIKI-REVIEW-074
---

# GS-544 78933 幂级数收敛域和函数

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-544_78933幂级数收敛域和函数.md`
- wrongnet ID：`GS-544`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-544_78933，2026.6.4.md`（`VIS-GS-544`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、幂级数、幂级数收敛域、幂级数和函数、缺项幂级数、幂级数逐项积分、交错级数、莱布尼茨判别法、反正切函数展开
- 方法：先判型、比值判别法、整体通项比值、端点单独讨论、莱布尼茨判别法、逐项积分、先积后导、无穷等比级数求和、反正切函数展开
- 错因字段：题型识别失败、方法选择错误、概念混淆、条件忽略、方法论调取不稳、动作链断裂、端点检查概念混淆、交错级数判别结论误解、辅助函数记号混淆
- 第一动作：先写出 \(u_n(x)=\frac{(-1)^{n-1}}{2n-1}x^{2n}\)，计算 \(\left|\frac{u_{n+1}}{u_n}\right|\to x^2\)。
- 个人断点：没有果断启动比值法；没有稳定执行端点代回；没有第一时间把 \(\frac1{2n-1}\) 识别为逐项积分产生的分母。
- 方法卡 ID：H16-020
- 当前强关系：GS-511

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳]]
- [[MATHWIKI-ERROR-CLUSTER-115_交错级数判别结论误解]]
- [[MATHWIKI-ERROR-CLUSTER-397_端点检查概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-433_辅助函数记号混淆]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-059_交错级数]]
- [[MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法]]
- [[MATHWIKI-KNOWLEDGE-092_幂级数收敛域]]
- [[MATHWIKI-KNOWLEDGE-112_幂级数和函数]]
- [[MATHWIKI-KNOWLEDGE-176_幂级数逐项积分]]
- [[MATHWIKI-KNOWLEDGE-244_反正切函数展开]]
- [[MATHWIKI-KNOWLEDGE-269_缺项幂级数]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法]]
- [[MATHWIKI-METHOD-CLUSTER-098_比值判别法]]
- [[MATHWIKI-METHOD-CLUSTER-1066_无穷等比级数求和]]
- [[MATHWIKI-METHOD-CLUSTER-128_端点单独讨论]]
- [[MATHWIKI-METHOD-CLUSTER-132_逐项积分]]
- [[MATHWIKI-METHOD-CLUSTER-233_整体通项比值]]
- [[MATHWIKI-METHOD-CLUSTER-622_先积后导]]
- [[MATHWIKI-METHOD-CLUSTER-793_反正切函数展开]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- [[错题知识网络/错题卡/GS-511_102386缺项幂级数收敛域|GS-511]]

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
