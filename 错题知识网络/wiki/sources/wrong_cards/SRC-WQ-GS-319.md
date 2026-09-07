---
wiki_id: SRC-WQ-GS-319
type: source_summary
title: "GS-319 强化例题11.17 某些特殊的函数值，我们也可以用定积分表示出来"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-319_强化例题11.17某些特殊的函数值，我们也可以用定积分表示出来.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-319"
knowledge:
  - "定积分"
  - "定积分性质"
  - "定积分不等式"
error_causes:
  - "触发信息遗漏"
  - "动作链断裂"
methods:
  - "常数项积分化"
  - "凑完全平方"
  - "积分保号性"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-068_定积分不等式"
  - "MATHWIKI-METHOD-CLUSTER-103_积分保号性"
  - "MATHWIKI-METHOD-CLUSTER-225_常数项积分化"
  - "MATHWIKI-METHOD-CLUSTER-300_凑完全平方"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-072_积分不等式证明入口链"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-319 强化例题11.17 某些特殊的函数值，我们也可以用定积分表示出来

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-319_强化例题11.17某些特殊的函数值，我们也可以用定积分表示出来.md`
- wrongnet ID：`GS-319`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 定积分不等式反推函数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 定积分不等式

### 错因

- 触发信息遗漏
- 动作链断裂

### 方法

- 常数项积分化
- 凑完全平方
- 积分保号性

### 陷阱

- 没有把 1/5 写成 \int_0^1 x^4 dx
- 只看不等式不凑平方
- 非负函数积分为零的等号条件漏用

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把 1/5 写成 0 到 1 上 x^4 的积分 |
| missed_action | 没有把常数项改写为积分以闭合平方 |
| related_method_card_id | H11-007 |
| next_reminder | 看到积分不等式里有平方项和交叉项，先把常数项积分化，再凑完全平方。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-068_定积分不等式]]
- [[MATHWIKI-METHOD-CLUSTER-103_积分保号性]]
- [[MATHWIKI-METHOD-CLUSTER-225_常数项积分化]]
- [[MATHWIKI-METHOD-CLUSTER-300_凑完全平方]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-072_积分不等式证明入口链]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
