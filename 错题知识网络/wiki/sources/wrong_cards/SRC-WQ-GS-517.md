---
wiki_id: SRC-WQ-GS-517
type: source_summary
title: "GS-517 102393 幂级数变形判敛 2026.5.30"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-517_102393幂级数变形判敛.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-517_102393-2026.5.30.md"
visual_ids:
  - "VIS-GS-517"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-517/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-517"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "幂级数"
  - "幂级数收敛半径"
  - "幂级数收敛域"
  - "阿贝尔定理"
  - "幂级数逐项求导"
  - "条件收敛"
error_causes:
  - "题型识别失败"
methods:
  - "先判型"
  - "阿贝尔定理"
  - "条件收敛定端点求R"
  - "逐项求导不变半径"
  - "中心平移"
  - "乘因式不改内部"
  - "端点单独判"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-048_幂级数"
  - "MATHWIKI-KNOWLEDGE-092_幂级数收敛域"
  - "MATHWIKI-KNOWLEDGE-095_条件收敛"
  - "MATHWIKI-KNOWLEDGE-145_幂级数逐项求导"
  - "MATHWIKI-KNOWLEDGE-251_幂级数收敛半径"
  - "MATHWIKI-KNOWLEDGE-431_阿贝尔定理"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-1100_条件收敛定端点求R"
  - "MATHWIKI-METHOD-CLUSTER-1371_逐项求导不变半径"
  - "MATHWIKI-METHOD-CLUSTER-1404_阿贝尔定理"
  - "MATHWIKI-METHOD-CLUSTER-173_端点单独判"
  - "MATHWIKI-METHOD-CLUSTER-535_中心平移"
  - "MATHWIKI-METHOD-CLUSTER-544_乘因式不改内部"
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
formal_projection_sha256: 30de057375dfdf1384b113ec087e85cf63ccc665ca6f25d83d52d3c29ceb4553
---

# GS-517 102393 幂级数变形判敛 2026.5.30

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-517_102393幂级数变形判敛.md`
- wrongnet ID：`GS-517`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-517_102393-2026.5.30.md`（`VIS-GS-517`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 幂级数变形后敛散性判断（阿贝尔定理） |
| 日期 | 2026-05-30 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 无穷级数
- 幂级数
- 幂级数收敛半径
- 幂级数收敛域
- 阿贝尔定理
- 幂级数逐项求导
- 条件收敛

### 错因

- 题型识别失败

### 方法

- 先判型
- 阿贝尔定理
- 条件收敛定端点求R
- 逐项求导不变半径
- 中心平移
- 乘因式不改内部
- 端点单独判

### 陷阱

- 条件收敛点必为端点据此定R
- 逐项求导端点敛散性可变
- 收敛区间内部绝对收敛
- 中心平移

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先看原级数 \(\sum a_n(x+1)^n\) 的中心是 \(-1\)，由 \(x=1\) 条件收敛推出该点是端点，所以 \(R=2\)。 |
| missed_action | 没有先用“条件收敛点只能是端点”确定半径，也没有把目标级数识别成原幂级数变形。 |
| related_method_card_id | H16-020 |
| next_reminder | 看到已知幂级数在某点条件收敛，先用“内部绝对收敛、条件收敛只能在端点”定半径；再追踪求导、平移、乘因式。 |
| evidence_origin | user_confirmed |
| repeat_count | 1 |
| repeat_count_source | wrong_history |

## 证据边界

- 个人错因仅来自正式卡 dated `wrong_history`；详情解析只核验题面与解法，不反推个人错因。
- 题图或解析图存在，只证明视觉来源已注册，不单独证明个人作答过程、错误次数或掌握度。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-092_幂级数收敛域]]
- [[MATHWIKI-KNOWLEDGE-095_条件收敛]]
- [[MATHWIKI-KNOWLEDGE-145_幂级数逐项求导]]
- [[MATHWIKI-KNOWLEDGE-251_幂级数收敛半径]]
- [[MATHWIKI-KNOWLEDGE-431_阿贝尔定理]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-1100_条件收敛定端点求R]]
- [[MATHWIKI-METHOD-CLUSTER-1371_逐项求导不变半径]]
- [[MATHWIKI-METHOD-CLUSTER-1404_阿贝尔定理]]
- [[MATHWIKI-METHOD-CLUSTER-173_端点单独判]]
- [[MATHWIKI-METHOD-CLUSTER-535_中心平移]]
- [[MATHWIKI-METHOD-CLUSTER-544_乘因式不改内部]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
