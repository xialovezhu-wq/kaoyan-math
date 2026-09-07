---
wiki_id: SRC-WQ-GS-533
type: source_summary
title: "GS-533 62180 幂指泰勒展开"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-533_62180幂指泰勒展开.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-533_62180,-2026.6.1.md"
visual_ids:
  - "VIS-GS-533"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-533/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-533"
related_wrongnet_refs: []
knowledge:
  - "极限与连续"
  - "泰勒公式"
  - "泰勒展开"
  - "等价无穷小"
  - "幂指极限"
  - "一元函数微分学应用"
error_causes:
  - "题型识别失败"
  - "方法选择错误"
  - "过程跳步"
  - "复习记忆不牢"
methods:
  - "先判型"
  - "取对数"
  - "指数化"
  - "泰勒展开"
  - "等价变形"
  - "系数对齐"
  - "标准化计算流程"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS"
  - "MATHWIKI-ACTION-GAP-001"
  - "MATHWIKI-ERROR-CLUSTER-001"
  - "MATHWIKI-ERROR-CLUSTER-002"
  - "MATHWIKI-ERROR-CLUSTER-003"
  - "MATHWIKI-ERROR-CLUSTER-017"
  - "MATHWIKI-KNOWLEDGE-001"
  - "MATHWIKI-KNOWLEDGE-003"
  - "MATHWIKI-KNOWLEDGE-004"
  - "MATHWIKI-KNOWLEDGE-015"
  - "MATHWIKI-KNOWLEDGE-017"
  - "MATHWIKI-KNOWLEDGE-038"
  - "MATHWIKI-METHOD-CLUSTER-001"
  - "MATHWIKI-METHOD-CLUSTER-003"
  - "MATHWIKI-METHOD-CLUSTER-008"
  - "MATHWIKI-METHOD-CLUSTER-011"
  - "MATHWIKI-METHOD-CLUSTER-019"
  - "MATHWIKI-METHOD-CLUSTER-1296"
  - "MATHWIKI-METHOD-CLUSTER-374"
  - "MATHWIKI-GS-ERROR-003"
  - "MATHWIKI-GS-ERROR-004"
  - "MATHWIKI-GS-ERROR-005"
  - "MATHWIKI-GS-METHOD-009"
  - "MATHWIKI-GS-METHOD-012"
  - "MATHWIKI-GS-TOPIC-003"
  - "MATHWIKI-GS-TOPIC-004"
  - "MATHWIKI-GS-TOPIC-005"
  - "MATHWIKI-SYNTHESIS-001"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因只来自正式卡日期化 wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-072
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: a3c07df49c6aa9e842183018446ec38a207cc36f13869ad4a33c4898bae0fd88
---

# GS-533 62180 幂指泰勒展开

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-533_62180幂指泰勒展开.md`
- wrongnet ID：`GS-533`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-533_62180,-2026.6.1.md`（`VIS-GS-533`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 幂指函数泰勒展开 |
| 日期 | 2026-06-01 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 极限与连续
- 泰勒公式
- 泰勒展开
- 等价无穷小
- 幂指极限
- 一元函数微分学应用

### 错因

- 题型识别失败
- 方法选择错误
- 过程跳步
- 复习记忆不牢

### 方法

- 先判型
- 取对数
- 指数化
- 泰勒展开
- 等价变形
- 系数对齐
- 标准化计算流程

### 陷阱

- 展开阶数
- 复合函数展开
- 二次项系数
- 高阶无穷小
- 幂指数入口

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 f(x)=exp(ln(1+x)/x)，展开 ln(1+x)/x 到所需阶数 |
| missed_action | 没有先把幂指式转成 exp(ln(1+x)/x)，导致泰勒展开层次和系数对齐不稳 |
| related_method_card_id | H01-002 |
| next_reminder | 看到幂指式要配二次近似，先写成 exp(v ln u)，展开指数内部，再展开外层 e^u。 |
| evidence_origin | user_confirmed |
| repeat_count | 1 |
| repeat_count_source | wrong_history |

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；详情解析只核验题面与解法，不反推个人错因。
- 题图或解析图存在，只证明视觉来源已登记，不单独证明个人作答过程、错误次数或掌握度。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS]]
- [[MATHWIKI-ACTION-GAP-001]]
- [[MATHWIKI-ERROR-CLUSTER-001]]
- [[MATHWIKI-ERROR-CLUSTER-002]]
- [[MATHWIKI-ERROR-CLUSTER-003]]
- [[MATHWIKI-ERROR-CLUSTER-017]]
- [[MATHWIKI-KNOWLEDGE-001]]
- [[MATHWIKI-KNOWLEDGE-003]]
- [[MATHWIKI-KNOWLEDGE-004]]
- [[MATHWIKI-KNOWLEDGE-015]]
- [[MATHWIKI-KNOWLEDGE-017]]
- [[MATHWIKI-KNOWLEDGE-038]]
- [[MATHWIKI-METHOD-CLUSTER-001]]
- [[MATHWIKI-METHOD-CLUSTER-003]]
- [[MATHWIKI-METHOD-CLUSTER-008]]
- [[MATHWIKI-METHOD-CLUSTER-011]]
- [[MATHWIKI-METHOD-CLUSTER-019]]
- [[MATHWIKI-METHOD-CLUSTER-1296]]
- [[MATHWIKI-METHOD-CLUSTER-374]]
- [[MATHWIKI-GS-ERROR-003]]
- [[MATHWIKI-GS-ERROR-004]]
- [[MATHWIKI-GS-ERROR-005]]
- [[MATHWIKI-GS-METHOD-009]]
- [[MATHWIKI-GS-METHOD-012]]
- [[MATHWIKI-GS-TOPIC-003]]
- [[MATHWIKI-GS-TOPIC-004]]
- [[MATHWIKI-GS-TOPIC-005]]
- [[MATHWIKI-SYNTHESIS-001]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
