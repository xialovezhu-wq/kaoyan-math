---
wiki_id: SRC-WQ-GS-521
type: source_summary
title: "GS-521 82157 先导后积求和函数 2026.5.30"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-521_82157先导后积求和函数.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-521_82157-2026.5.30.md"
visual_ids:
  - "VIS-GS-521"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-521/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-521"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "幂级数"
  - "幂级数和函数"
  - "幂级数逐项求导"
  - "先导后积"
  - "等比级数"
error_causes:
  - "题型识别失败"
methods:
  - "先判型"
  - "逐项求导消n"
  - "先导后积"
  - "等比级数求和"
  - "端点单独判"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-048_幂级数"
  - "MATHWIKI-KNOWLEDGE-104_等比级数"
  - "MATHWIKI-KNOWLEDGE-112_幂级数和函数"
  - "MATHWIKI-KNOWLEDGE-145_幂级数逐项求导"
  - "MATHWIKI-KNOWLEDGE-233_先导后积"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-1372_逐项求导消n"
  - "MATHWIKI-METHOD-CLUSTER-173_端点单独判"
  - "MATHWIKI-METHOD-CLUSTER-195_先导后积"
  - "MATHWIKI-METHOD-CLUSTER-256_等比级数求和"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因只来自正式卡日期化 wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-072
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 545553020a69e1aae7d5a7baa8e648d290cfc47e95b3701d6aa6588db416b127
---

# GS-521 82157 先导后积求和函数 2026.5.30

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-521_82157先导后积求和函数.md`
- wrongnet ID：`GS-521`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-521_82157-2026.5.30.md`（`VIS-GS-521`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 幂级数求和函数（逐项求导+先导后积） |
| 日期 | 2026-05-30 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 无穷级数
- 幂级数
- 幂级数和函数
- 幂级数逐项求导
- 先导后积
- 等比级数

### 错因

- 题型识别失败

### 方法

- 先判型
- 逐项求导消n
- 先导后积
- 等比级数求和
- 端点单独判

### 陷阱

- 分母含n先逐项求导消n
- x0取幂级数中心使S(x0)易算
- 端点单独判
- 收敛区间内部才能逐项求导

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先设 S(x)=Σx^n/n，并在收敛区间内逐项求导得到几何级数 |
| missed_action | 没有先逐项求导消掉分母 n，再从幂级数中心积分还原 S(x) |
| related_method_card_id | H16-021 |
| next_reminder | 看到分母含 n 的幂级数求和，先逐项求导消 n，再从中心点积分还原并查端点。 |
| evidence_origin | user_confirmed |
| repeat_count | 1 |
| repeat_count_source | wrong_history |

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；详情解析只核验题面与解法，不反推个人错因。
- 题图或解析图存在，只证明视觉来源已登记，不单独证明个人作答过程、错误次数或掌握度。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-104_等比级数]]
- [[MATHWIKI-KNOWLEDGE-112_幂级数和函数]]
- [[MATHWIKI-KNOWLEDGE-145_幂级数逐项求导]]
- [[MATHWIKI-KNOWLEDGE-233_先导后积]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-1372_逐项求导消n]]
- [[MATHWIKI-METHOD-CLUSTER-173_端点单独判]]
- [[MATHWIKI-METHOD-CLUSTER-195_先导后积]]
- [[MATHWIKI-METHOD-CLUSTER-256_等比级数求和]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
