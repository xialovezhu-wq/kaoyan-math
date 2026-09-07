---
wiki_id: SRC-WQ-GS-511
type: source_summary
title: "GS-511 102386 缺项幂级数收敛域"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-511_102386缺项幂级数收敛域.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-511_102386-2026.5.28.md"
visual_ids:
  - "VIS-GS-511"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-511/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-511"
related_wrongnet_refs:
  - "GS-544"
knowledge:
  - "无穷级数"
  - "幂级数"
  - "幂级数收敛域"
  - "缺项幂级数"
  - "比值判别法"
  - "莱布尼茨判别法"
  - "交错级数"
error_causes:
  - "题型识别失败"
  - "方法选择错误"
  - "条件忽略"
  - "过程跳步"
methods:
  - "先判型"
  - "比值判别法"
  - "缺项换元"
  - "整体通项比值"
  - "端点单独讨论"
  - "莱布尼茨判别法"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-048_幂级数"
  - "MATHWIKI-KNOWLEDGE-059_交错级数"
  - "MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法"
  - "MATHWIKI-KNOWLEDGE-092_幂级数收敛域"
  - "MATHWIKI-KNOWLEDGE-214_比值判别法"
  - "MATHWIKI-KNOWLEDGE-269_缺项幂级数"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法"
  - "MATHWIKI-METHOD-CLUSTER-098_比值判别法"
  - "MATHWIKI-METHOD-CLUSTER-128_端点单独讨论"
  - "MATHWIKI-METHOD-CLUSTER-1314_缺项换元"
  - "MATHWIKI-METHOD-CLUSTER-233_整体通项比值"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
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
formal_projection_sha256: 1f1299bc378126212703e0578fb36329964d87406662bdcb7b3db91366d87249
---

# GS-511 102386 缺项幂级数收敛域

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-511_102386缺项幂级数收敛域.md`
- wrongnet ID：`GS-511`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-511_102386-2026.5.28.md`（`VIS-GS-511`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 缺项幂级数收敛域 |
| 日期 | 2026-05-28 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 无穷级数
- 幂级数
- 幂级数收敛域
- 缺项幂级数
- 比值判别法
- 莱布尼茨判别法
- 交错级数

### 错因

- 题型识别失败
- 方法选择错误
- 条件忽略
- 过程跳步

### 方法

- 先判型
- 比值判别法
- 缺项换元
- 整体通项比值
- 端点单独讨论
- 莱布尼茨判别法

### 陷阱

- 缺项幂级数
- 变量幂次
- 只看系数比值
- x平方因子
- 端点未单独讨论
- 莱布尼茨单调性

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先令 \(u_n(x)=\frac{(-1)^{n-1}}{2n-1}x^{2n}\)，直接算 \(\left\|\frac{u_{n+1}(x)}{u_n(x)}\right\|\to x^2\)，得到 \(\|x\|<1\)，再查 \(x=\pm1\)。 |
| missed_action | 只对系数 \(\frac{(-1)^{n-1}}{2n-1}\) 做比值，漏掉整体通项里的 \(x^{2n}\)。 |
| related_method_card_id | H16-020 |
| next_reminder | 看到缺项幂级数，先对整个 \(u_n(x)\) 做比值或令 \(t=x^2\)，不要只比系数；半径出来后端点逐个代回原级数。 |
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
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-059_交错级数]]
- [[MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法]]
- [[MATHWIKI-KNOWLEDGE-092_幂级数收敛域]]
- [[MATHWIKI-KNOWLEDGE-214_比值判别法]]
- [[MATHWIKI-KNOWLEDGE-269_缺项幂级数]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法]]
- [[MATHWIKI-METHOD-CLUSTER-098_比值判别法]]
- [[MATHWIKI-METHOD-CLUSTER-128_端点单独讨论]]
- [[MATHWIKI-METHOD-CLUSTER-1314_缺项换元]]
- [[MATHWIKI-METHOD-CLUSTER-233_整体通项比值]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- GS-544

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
