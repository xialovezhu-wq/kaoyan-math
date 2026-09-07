---
wiki_id: SRC-WQ-GS-512
type: source_summary
title: "GS-512 102389 逐项积分收敛域"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-512_102389逐项积分收敛域.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-512_102389-2026.5.28.md"
visual_ids:
  - "VIS-GS-512"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-512/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-512"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "幂级数"
  - "幂级数收敛域"
  - "幂级数逐项积分"
  - "变上限积分"
  - "交错级数"
  - "莱布尼茨判别法"
error_causes:
  - "题型识别失败"
  - "方法选择错误"
  - "条件忽略"
  - "过程跳步"
methods:
  - "先判型"
  - "逐项积分"
  - "变上限积分"
  - "比值判别法"
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
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-048_幂级数"
  - "MATHWIKI-KNOWLEDGE-059_交错级数"
  - "MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法"
  - "MATHWIKI-KNOWLEDGE-092_幂级数收敛域"
  - "MATHWIKI-KNOWLEDGE-176_幂级数逐项积分"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法"
  - "MATHWIKI-METHOD-CLUSTER-098_比值判别法"
  - "MATHWIKI-METHOD-CLUSTER-128_端点单独讨论"
  - "MATHWIKI-METHOD-CLUSTER-132_逐项积分"
  - "MATHWIKI-METHOD-CLUSTER-800_变上限积分"
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
formal_projection_sha256: d37bb149d3e11134e22e688d010ba1490b990871f357ff2004640ff703357c61
---

# GS-512 102389 逐项积分收敛域

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-512_102389逐项积分收敛域.md`
- wrongnet ID：`GS-512`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-512_102389-2026.5.28.md`（`VIS-GS-512`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 幂级数逐项积分后收敛域 |
| 日期 | 2026-05-28 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 无穷级数
- 幂级数
- 幂级数收敛域
- 幂级数逐项积分
- 变上限积分
- 交错级数
- 莱布尼茨判别法

### 错因

- 题型识别失败
- 方法选择错误
- 条件忽略
- 过程跳步

### 方法

- 先判型
- 逐项积分
- 变上限积分
- 比值判别法
- 端点单独讨论
- 莱布尼茨判别法

### 陷阱

- 逐项积分后是新幂级数
- 端点重新判断
- 正负1端点不同
- 通项趋零
- 交错调和级数
- 调和级数发散

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写出逐项积分后的新通项，把它当作新幂级数，再重新判断端点 |
| missed_action | 没有把逐项积分后的 g(x) 当作新幂级数重新判断端点 |
| related_method_card_id | H16-021 |
| next_reminder | 看到幂级数逐项积分，先写出新通项，再重新查端点。 |
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
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-059_交错级数]]
- [[MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法]]
- [[MATHWIKI-KNOWLEDGE-092_幂级数收敛域]]
- [[MATHWIKI-KNOWLEDGE-176_幂级数逐项积分]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法]]
- [[MATHWIKI-METHOD-CLUSTER-098_比值判别法]]
- [[MATHWIKI-METHOD-CLUSTER-128_端点单独讨论]]
- [[MATHWIKI-METHOD-CLUSTER-132_逐项积分]]
- [[MATHWIKI-METHOD-CLUSTER-800_变上限积分]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
