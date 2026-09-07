---
wiki_id: SRC-WQ-GS-518
type: source_summary
title: "GS-518 102395 和型幂级数拆分收敛域 2026.5.30"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-518_102395和型幂级数拆分收敛域.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-518_102395-2026.5.30.md"
visual_ids:
  - "VIS-GS-518"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-518/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-518"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "幂级数"
  - "幂级数收敛域"
  - "级数拆项"
  - "广义调和级数"
  - "p级数"
  - "交错级数"
  - "莱布尼茨判别法"
  - "等比级数"
error_causes:
  - "方法选择错误"
  - "题型识别失败"
methods:
  - "先判型"
  - "级数拆分取交集"
  - "收敛半径比值公式"
  - "广义调和级数结论"
  - "莱布尼茨判别法"
  - "等比级数判敛"
  - "端点单独判"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-036_p级数"
  - "MATHWIKI-KNOWLEDGE-048_幂级数"
  - "MATHWIKI-KNOWLEDGE-059_交错级数"
  - "MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法"
  - "MATHWIKI-KNOWLEDGE-092_幂级数收敛域"
  - "MATHWIKI-KNOWLEDGE-104_等比级数"
  - "MATHWIKI-KNOWLEDGE-128_级数拆项"
  - "MATHWIKI-KNOWLEDGE-252_广义调和级数"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法"
  - "MATHWIKI-METHOD-CLUSTER-1045_收敛半径比值公式"
  - "MATHWIKI-METHOD-CLUSTER-1291_等比级数判敛"
  - "MATHWIKI-METHOD-CLUSTER-1301_级数拆分取交集"
  - "MATHWIKI-METHOD-CLUSTER-173_端点单独判"
  - "MATHWIKI-METHOD-CLUSTER-988_广义调和级数结论"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-070
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 75a5d1160b03292a3dc27ed251760fd334aba2fcd7566ac93fafb0e3942561d1
---

# GS-518 102395 和型幂级数拆分收敛域 2026.5.30

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-518_102395和型幂级数拆分收敛域.md`
- wrongnet ID：`GS-518`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-518_102395-2026.5.30.md`（`VIS-GS-518`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 幂级数收敛域（系数为两式之和，拆分取交集） |
| 日期 | 2026-05-30 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 无穷级数
- 幂级数
- 幂级数收敛域
- 级数拆项
- 广义调和级数
- p级数
- 交错级数
- 莱布尼茨判别法
- 等比级数

### 错因

- 方法选择错误
- 题型识别失败

### 方法

- 先判型
- 级数拆分取交集
- 收敛半径比值公式
- 广义调和级数结论
- 莱布尼茨判别法
- 等比级数判敛
- 端点单独判

### 陷阱

- 系数为和时拆成两级数分别判端点
- 收敛域取交集
- 端点整体判别法失效需拆开
- n ln n 广义调和 p=1 发散

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先拆成 \(\sum\frac{x^n}{n\ln n}\) 和 \(\sum\frac{x^n}{2^n}\)，分别求收敛域，再取两个收敛域的交集。 |
| missed_action | 把系数和整体硬套比值法，端点失效后没有回到原级数拆成熟悉级数。 |
| related_method_card_id | H16-020 |
| next_reminder | 看到系数是“和”，尤其两部分阶不同，先拆成两个幂级数分别求收敛域，再取交集；端点按拆分后的原级数判。 |
| evidence_origin | user_confirmed |
| repeat_count | 1 |
| repeat_count_source | wrong_history |

## 证据边界

- 个人错因仅来自正式卡 dated `wrong_history`；详情解析只核验题面与解法，不反推个人错因。
- 题图或解析图存在，只证明视觉来源已注册，不单独证明个人作答过程、错误次数或掌握度。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-036_p级数]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-059_交错级数]]
- [[MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法]]
- [[MATHWIKI-KNOWLEDGE-092_幂级数收敛域]]
- [[MATHWIKI-KNOWLEDGE-104_等比级数]]
- [[MATHWIKI-KNOWLEDGE-128_级数拆项]]
- [[MATHWIKI-KNOWLEDGE-252_广义调和级数]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法]]
- [[MATHWIKI-METHOD-CLUSTER-1045_收敛半径比值公式]]
- [[MATHWIKI-METHOD-CLUSTER-1291_等比级数判敛]]
- [[MATHWIKI-METHOD-CLUSTER-1301_级数拆分取交集]]
- [[MATHWIKI-METHOD-CLUSTER-173_端点单独判]]
- [[MATHWIKI-METHOD-CLUSTER-988_广义调和级数结论]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
