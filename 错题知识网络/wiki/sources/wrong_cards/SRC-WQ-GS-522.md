---
wiki_id: SRC-WQ-GS-522
type: source_summary
title: "GS-522 19533 分子含n求导求和函数 2026.5.30"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-522_19533分子含n求导求和.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-522_19533-2026.5.30.md"
visual_ids:
  - "VIS-GS-522"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-522/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-522"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "幂级数"
  - "幂级数和函数"
  - "幂级数逐项求导"
  - "几何级数"
error_causes:
  - "题型识别失败"
  - "概念混淆"
methods:
  - "先判型"
  - "几何级数逐项求导"
  - "乘x配项"
  - "端点单独判"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-048_幂级数"
  - "MATHWIKI-KNOWLEDGE-112_幂级数和函数"
  - "MATHWIKI-KNOWLEDGE-145_幂级数逐项求导"
  - "MATHWIKI-KNOWLEDGE-192_几何级数"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-173_端点单独判"
  - "MATHWIKI-METHOD-CLUSTER-543_乘x配项"
  - "MATHWIKI-METHOD-CLUSTER-642_几何级数逐项求导"
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
formal_projection_sha256: 543680f214c6ea84933dbcae203fe5a8be19779c604613b8e47f104bfeca7639
---

# GS-522 19533 分子含n求导求和函数 2026.5.30

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-522_19533分子含n求导求和.md`
- wrongnet ID：`GS-522`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-522_19533-2026.5.30.md`（`VIS-GS-522`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 幂级数求和函数（分子含n，几何级数逐项求导） |
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
- 几何级数

### 错因

- 题型识别失败
- 概念混淆

### 方法

- 先判型
- 几何级数逐项求导
- 乘x配项
- 端点单独判

### 陷阱

- 分子含n用求导分母含n才用积分
- nx^n=x(x^n)'不要直接对nx^n求导得n²
- 端点nx^n通项不趋0发散

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写 Σnx^n=x(Σx^n)'，再对几何级数求导 |
| missed_action | 没有先把 nx^n 改写成 x(x^n)'，误把它当成分母含 n 的先导后积题 |
| related_method_card_id | H16-021 |
| next_reminder | 看到分子含 n 的幂级数，先把 nx^n 写成 x(x^n)'，再由几何级数求导并查端点。 |
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
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-112_幂级数和函数]]
- [[MATHWIKI-KNOWLEDGE-145_幂级数逐项求导]]
- [[MATHWIKI-KNOWLEDGE-192_几何级数]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-173_端点单独判]]
- [[MATHWIKI-METHOD-CLUSTER-543_乘x配项]]
- [[MATHWIKI-METHOD-CLUSTER-642_几何级数逐项求导]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
