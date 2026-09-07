---
wiki_id: SRC-WQ-GS-507
type: source_summary
title: "GS-507 170727 洛必达反用极值判断"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-507_170727洛必达反用极值判断.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-507_170727-2026.5.26.md"
visual_ids:
  - "VIS-GS-507"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-507/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-507"
related_wrongnet_refs: []
knowledge:
  - "一元函数微分学应用"
  - "导数定义"
  - "极限与连续"
  - "极限保号性"
  - "局部极值"
  - "等价无穷小"
  - "洛必达法则使用条件"
error_causes:
  - "概念混淆"
  - "方法选择错误"
  - "条件忽略"
  - "题型识别失败"
methods:
  - "先判型"
  - "条件转化"
  - "导数定义"
  - "极限保号性"
  - "可导推出连续"
  - "等价无穷小"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-006_导数定义"
  - "MATHWIKI-KNOWLEDGE-124_极限保号性"
  - "MATHWIKI-KNOWLEDGE-144_局部极值"
  - "MATHWIKI-KNOWLEDGE-403_洛必达法则使用条件"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-013_导数定义"
  - "MATHWIKI-METHOD-CLUSTER-026_等价无穷小"
  - "MATHWIKI-METHOD-CLUSTER-083_极限保号性"
  - "MATHWIKI-METHOD-CLUSTER-816_可导推出连续"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-METHOD-013_导数定义差商入口"
  - "MATHWIKI-GS-METHOD-052_局部性质与导数符号单向判别"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-070
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 559110a5953aebedb84e673f93e372e546d11b4b53c415f0ab5e142f8bdaee83
---

# GS-507 170727 洛必达反用极值判断

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-507_170727洛必达反用极值判断.md`
- wrongnet ID：`GS-507`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-507_170727-2026.5.26.md`（`VIS-GS-507`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 导数定义与极限保号性判极值 |
| 日期 | 2026-05-27 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 导数定义
- 极限与连续
- 极限保号性
- 局部极值
- 等价无穷小
- 洛必达法则使用条件

### 错因

- 概念混淆
- 方法选择错误
- 条件忽略
- 题型识别失败

### 方法

- 先判型
- 条件转化
- 导数定义
- 极限保号性
- 可导推出连续
- 等价无穷小

### 陷阱

- 洛必达反用
- 原函数比值不能反推导数比值
- 导函数极限不保证存在
- 导数为零不能单独判极值
- 极限保号性入口

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先由 \(\frac{f(x)}{x^2}\to1\) 得 \(f(x)\to0\)，结合可导必连续写出 \(f(0)=0\)。 |
| missed_action | 把洛必达法则反向使用，试图由原函数比值极限推出导数比值极限。 |
| related_method_card_id | H05-006 |
| next_reminder | 看到原函数比值极限，先检查能推出的函数值、符号和导数定义；不能反向推出导数比值极限。 |
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
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-006_导数定义]]
- [[MATHWIKI-KNOWLEDGE-124_极限保号性]]
- [[MATHWIKI-KNOWLEDGE-144_局部极值]]
- [[MATHWIKI-KNOWLEDGE-403_洛必达法则使用条件]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-013_导数定义]]
- [[MATHWIKI-METHOD-CLUSTER-026_等价无穷小]]
- [[MATHWIKI-METHOD-CLUSTER-083_极限保号性]]
- [[MATHWIKI-METHOD-CLUSTER-816_可导推出连续]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-METHOD-013_导数定义差商入口]]
- [[MATHWIKI-GS-METHOD-052_局部性质与导数符号单向判别]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
