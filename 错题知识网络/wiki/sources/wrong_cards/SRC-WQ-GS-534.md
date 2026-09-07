---
wiki_id: SRC-WQ-GS-534
type: source_summary
title: "GS-534 58125 导数介值费马定理"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-534_58125导数介值费马定理.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-534_58125-2026.6.1.md"
visual_ids:
  - "VIS-GS-534"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-534/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-534"
related_wrongnet_refs: []
knowledge:
  - "一元函数微分学应用"
  - "中值定理"
  - "费马定理"
  - "最值定理"
  - "导数介值性质"
  - "辅助函数构造"
error_causes:
  - "概念混淆"
  - "条件忽略"
  - "方法选择错误"
  - "证明结构不完整"
methods:
  - "最值定理"
  - "费马定理"
  - "端点导数保号"
  - "构造辅助函数"
  - "平移导数值"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-009_A-COND"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-011_证明结构不完整"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-KNOWLEDGE-076_辅助函数构造"
  - "MATHWIKI-KNOWLEDGE-152_最值定理"
  - "MATHWIKI-KNOWLEDGE-187_费马定理"
  - "MATHWIKI-KNOWLEDGE-348_导数介值性质"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-1273_端点导数保号"
  - "MATHWIKI-METHOD-CLUSTER-180_费马定理"
  - "MATHWIKI-METHOD-CLUSTER-387_最值定理"
  - "MATHWIKI-METHOD-CLUSTER-984_平移导数值"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因只来自正式卡日期化 wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-072
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: d4b13ca62032eaeb6905b4a37effd8cc800182d38a7530553412f201f8c248c4
---

# GS-534 58125 导数介值费马定理

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-534_58125导数介值费马定理.md`
- wrongnet ID：`GS-534`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-534_58125-2026.6.1.md`（`VIS-GS-534`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 中值定理 |
| 题型 | 导数介值性质证明 |
| 日期 | 2026-06-01 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 4 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 中值定理
- 费马定理
- 最值定理
- 导数介值性质
- 辅助函数构造

### 错因

- 概念混淆
- 条件忽略
- 方法选择错误
- 证明结构不完整

### 方法

- 最值定理
- 费马定理
- 端点导数保号
- 构造辅助函数
- 平移导数值
- 条件转化

### 陷阱

- 误用零点定理
- 导函数不一定连续
- 端点单侧导数
- 内部极值点
- 第二问套第一问

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-COND |
| expected_first_action | 先在闭区间上取 f 的最大/最小值，再用端点单侧导数符号排除端点极值 |
| missed_action | 漏查 f' 未必连续这一条件，错误地想直接对 f' 使用零点定理 |
| related_method_card_id | H06-001 |
| next_reminder | 看到只给可导却要证明 f' 取值，先回到 f 的最值和费马定理，不要默认 f' 连续。 |
| evidence_origin | user_confirmed |
| repeat_count | 1 |
| repeat_count_source | wrong_history |

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；详情解析只核验题面与解法，不反推个人错因。
- 题图或解析图存在，只证明视觉来源已登记，不单独证明个人作答过程、错误次数或掌握度。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-009_A-COND]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-011_证明结构不完整]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-KNOWLEDGE-076_辅助函数构造]]
- [[MATHWIKI-KNOWLEDGE-152_最值定理]]
- [[MATHWIKI-KNOWLEDGE-187_费马定理]]
- [[MATHWIKI-KNOWLEDGE-348_导数介值性质]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-1273_端点导数保号]]
- [[MATHWIKI-METHOD-CLUSTER-180_费马定理]]
- [[MATHWIKI-METHOD-CLUSTER-387_最值定理]]
- [[MATHWIKI-METHOD-CLUSTER-984_平移导数值]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
