---
wiki_id: SRC-WQ-GS-309
type: source_summary
title: "GS-309 57723 2026.5.5"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-309_577232026.5.5.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-309"
knowledge:
  - "定积分"
  - "定积分性质"
  - "函数奇偶性"
error_causes:
  - "条件忽略"
methods:
  - "奇偶性判断"
  - "积分函数奇偶性"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-165_函数奇偶性"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-1254_积分函数奇偶性"
  - "MATHWIKI-METHOD-CLUSTER-349_奇偶性判断"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-308"
formal_projection_sha256: 013a33276eec802a50b2fb416d7ef188871caa22cced25e1b15895f0d61d1aab
---

# GS-309 57723 2026.5.5

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-309_577232026.5.5.md`
- wrongnet ID：`GS-309`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 积分函数奇偶性判断 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 函数奇偶性

### 错因

- 条件忽略

### 方法

- 奇偶性判断
- 积分函数奇偶性
- 条件转化

### 陷阱

- 正负号
- 积分下限不是0会带常数项
- 积分变量与参数混淆

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先判 \(t\) 是奇函数且 \(f(t)\) 是奇函数，从而 \(t f(t)\) 是偶函数 |
| missed_action | 把 \(t\) 的奇偶性和积分函数加常数后的奇偶性混在一起 |
| related_method_card_id | H11-004 |
| next_reminder | 看到嵌套积分奇偶性，先判最内层被积函数奇偶性，再看积分下限是否为 0；奇函数加常数会被破坏，偶函数加常数仍是偶函数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-165_函数奇偶性]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-1254_积分函数奇偶性]]
- [[MATHWIKI-METHOD-CLUSTER-349_奇偶性判断]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-308

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
