---
wiki_id: SRC-WQ-GS-306
type: source_summary
title: "GS-306 强化例题11.1"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-306_强化例题11.1.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-306"
knowledge:
  - "定积分"
  - "定积分性质"
  - "中值定理"
  - "极限与连续"
error_causes:
  - "触发信息遗漏"
  - "动作链断裂"
methods:
  - "尖峰核分段估计"
  - "定积分第一中值定理"
  - "arctan原函数"
  - "局部化极限"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-METHOD-CLUSTER-492_arctan原函数"
  - "MATHWIKI-METHOD-CLUSTER-898_定积分第一中值定理"
  - "MATHWIKI-METHOD-CLUSTER-949_尖峰核分段估计"
  - "MATHWIKI-METHOD-CLUSTER-950_局部化极限"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-306 强化例题11.1

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-306_强化例题11.1.md`
- wrongnet ID：`GS-306`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 尖峰核定积分极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 中值定理
- 极限与连续

### 错因

- 触发信息遗漏
- 动作链断裂

### 方法

- 尖峰核分段估计
- 定积分第一中值定理
- arctan原函数
- 局部化极限

### 陷阱

- 把尖峰核当普通有界函数
- 没有把主质量锁到 0 点
- 忽略两侧区间权重趋零

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先把积分区间按 0 附近中段和两侧区间拆开 |
| missed_action | 旧卡未记录用户个人动作缺口；可确认的复做断点是没有先抓主质量集中点并拆出中段。 |
| related_method_card_id | H08-007 |
| next_reminder | 看到尖峰核积分极限，先抓质量集中点，再拆中段和两侧区间。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-492_arctan原函数]]
- [[MATHWIKI-METHOD-CLUSTER-898_定积分第一中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-949_尖峰核分段估计]]
- [[MATHWIKI-METHOD-CLUSTER-950_局部化极限]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

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
