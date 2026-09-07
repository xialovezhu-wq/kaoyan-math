---
wiki_id: SRC-WQ-GS-326
type: source_summary
title: "GS-326 58122 2026.5.7"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-326_581222026.5.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-326"
knowledge:
  - "定积分"
  - "定积分性质"
  - "函数奇偶性"
  - "对称换元"
  - "平移变换"
error_causes:
  - "触发信息遗漏"
  - "方法选择错误"
methods:
  - "换元"
  - "条件转化"
  - "数形结合"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-111_对称换元"
  - "MATHWIKI-KNOWLEDGE-165_函数奇偶性"
  - "MATHWIKI-KNOWLEDGE-177_平移变换"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-009_换元"
  - "MATHWIKI-METHOD-CLUSTER-071_数形结合"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-633"
  - "GS-634"
formal_projection_sha256: 2f2a4b11ecf29a0f2c1404e2341c08c9e5d6f564c2a69969ead30116ec64e18f
---

# GS-326 58122 2026.5.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-326_581222026.5.7.md`
- wrongnet ID：`GS-326`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 积分型问题 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 函数奇偶性
- 对称换元
- 平移变换

### 错因

- 触发信息遗漏
- 方法选择错误

### 方法

- 换元
- 条件转化
- 数形结合

### 陷阱

- 适用条件

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把对称中心平移到原点，重写被积函数并判断整体奇偶性 |
| missed_action | 没有先把对称中心平移到原点，导致没有利用奇函数对称区间积分为零 |
| related_method_card_id | H11-003 |
| next_reminder | 看到对称区间定积分，先把对称中心平移到原点，再判断被积函数整体奇偶性。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-111_对称换元]]
- [[MATHWIKI-KNOWLEDGE-165_函数奇偶性]]
- [[MATHWIKI-KNOWLEDGE-177_平移变换]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-009_换元]]
- [[MATHWIKI-METHOD-CLUSTER-071_数形结合]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-633
- GS-634

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
