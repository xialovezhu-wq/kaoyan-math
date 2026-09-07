---
wiki_id: SRC-WQ-GS-108
type: source_summary
title: "GS-108 1000题B组3.11-2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-108_1000题B组3.11-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-108"
knowledge:
  - "一元函数微分学应用"
  - "导数定义"
  - "泰勒公式"
  - "可导性判定"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是把去心公式和补点处导数定义混用，需用户复做确认。"
methods:
  - "去心点和补点分开求导"
  - "用泰勒展开算补点导数"
  - "检查导函数连续性"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-318_旧批量未记录个人原始错因-当前仅确认复做断点是把去心公式和补点处导数定义"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-006_导数定义"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-KNOWLEDGE-118_可导性判定"
  - "MATHWIKI-METHOD-CLUSTER-1143_检查导函数连续性"
  - "MATHWIKI-METHOD-CLUSTER-1205_用泰勒展开算补点导数"
  - "MATHWIKI-METHOD-CLUSTER-748_去心点和补点分开求导"
  - "MATHWIKI-GS-METHOD-013_导数定义差商入口"
  - "MATHWIKI-GS-METHOD-094_导数定义真实增量与补点求导链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-108 1000题B组3.11-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-108_1000题B组3.11-2.md`
- wrongnet ID：`GS-108`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 去心商函数补点求导与连续 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 导数定义
- 泰勒公式
- 可导性判定

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是把去心公式和补点处导数定义混用，需用户复做确认。

### 方法

- 去心点和补点分开求导
- 用泰勒展开算补点导数
- 检查导函数连续性

### 陷阱

- x=0 不能直接套商法则
- g'(0) 要用定义或二阶泰勒
- f(0)=0 是补点连续的关键

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先把 x≠0 与 x=0 两种情形分开求导 |
| missed_action | 旧批量未记录个人步骤；当前复做风险是把 x≠0 的商法则结果直接代入补点 |
| related_method_card_id | H03-002 |
| next_reminder | 看到补点定义函数，先分去心点和补点，补点必须回到定义或泰勒。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-318_旧批量未记录个人原始错因-当前仅确认复做断点是把去心公式和补点处导数定义]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-006_导数定义]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-KNOWLEDGE-118_可导性判定]]
- [[MATHWIKI-METHOD-CLUSTER-1143_检查导函数连续性]]
- [[MATHWIKI-METHOD-CLUSTER-1205_用泰勒展开算补点导数]]
- [[MATHWIKI-METHOD-CLUSTER-748_去心点和补点分开求导]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-013_导数定义差商入口]]
- [[MATHWIKI-GS-METHOD-094_导数定义真实增量与补点求导链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-093
- GS-523

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
