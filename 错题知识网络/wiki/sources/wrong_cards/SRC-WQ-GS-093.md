---
wiki_id: SRC-WQ-GS-093
type: source_summary
title: "GS-093 1000题B组3.11"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-093_1000题B组3.11.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-093"
knowledge:
  - "一元函数微分学应用"
  - "导数定义"
  - "极限与连续"
  - "分段函数连续可导"
  - "导函数连续性"
  - "二阶导数定义"
error_causes:
  - "概念混淆"
  - "方法选择错误"
  - "过程跳步"
methods:
  - "先判型"
  - "分类讨论"
  - "导数定义"
  - "条件转化"
  - "商法则"
  - "二阶导数定义"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-006_导数定义"
  - "MATHWIKI-KNOWLEDGE-066_分段函数连续可导"
  - "MATHWIKI-KNOWLEDGE-142_导函数连续性"
  - "MATHWIKI-KNOWLEDGE-297_二阶导数定义"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-013_导数定义"
  - "MATHWIKI-METHOD-CLUSTER-341_商法则"
  - "MATHWIKI-METHOD-CLUSTER-565_二阶导数定义"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-METHOD-013_导数定义差商入口"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-093 1000题B组3.11

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-093_1000题B组3.11.md`
- wrongnet ID：`GS-093`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 分段函数求导与导函数连续性 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 导数定义
- 极限与连续
- 分段函数连续可导
- 导函数连续性
- 二阶导数定义

### 错因

- 概念混淆
- 方法选择错误
- 过程跳步

### 方法

- 先判型
- 分类讨论
- 导数定义
- 条件转化
- 商法则
- 二阶导数定义

### 陷阱

- 分段点
- 非分段表达式误用
- 商法则适用条件
- 适用条件
- 极限过程

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先用导数定义写 \(g'(0)=\lim_{x\to0}\frac{f(x)-xf'(0)}{x^2}\) |
| missed_action | 把 \(x\ne0\) 的商法则公式直接代到分段点，漏了导数定义。 |
| related_method_card_id | H01-008 |
| next_reminder | 看到分段点处求导，先分开 \(x\ne0\) 公式和点处导数定义，再比较导函数极限与点值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-006_导数定义]]
- [[MATHWIKI-KNOWLEDGE-066_分段函数连续可导]]
- [[MATHWIKI-KNOWLEDGE-142_导函数连续性]]
- [[MATHWIKI-KNOWLEDGE-297_二阶导数定义]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-013_导数定义]]
- [[MATHWIKI-METHOD-CLUSTER-341_商法则]]
- [[MATHWIKI-METHOD-CLUSTER-565_二阶导数定义]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-013_导数定义差商入口]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-108
- GS-523
- GS-472
- GS-470

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
