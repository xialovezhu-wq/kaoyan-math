---
wiki_id: SRC-WQ-GS-333
type: source_summary
title: "GS-333 1000题B组11.5"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-333_1000题B组11.5.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-333"
knowledge:
  - "定积分"
  - "定积分性质"
  - "分部积分"
error_causes:
  - "触发信息遗漏"
  - "方法调取失败"
methods:
  - "构造原函数"
  - "分部积分"
  - "前缀积分比较"
  - "积分保号性"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-103_积分保号性"
  - "MATHWIKI-METHOD-CLUSTER-123_构造原函数"
  - "MATHWIKI-METHOD-CLUSTER-321_前缀积分比较"
  - "MATHWIKI-GS-METHOD-072_积分不等式证明入口链"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-333 1000题B组11.5

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-333_1000题B组11.5.md`
- wrongnet ID：`GS-333`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 定积分不等式证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 分部积分

### 错因

- 触发信息遗漏
- 方法调取失败

### 方法

- 构造原函数
- 分部积分
- 前缀积分比较
- 积分保号性

### 陷阱

- 未利用端点积分相等导致边界项抵消
- 比较方向因负号反转
- 把点态函数比较误当已知条件

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先设 \(F(x)=\int_a^x f(t)\,dt\)，\(G(x)=\int_a^x g(t)\,dt\) |
| missed_action | 没有先把前缀积分条件转成原函数比较 |
| related_method_card_id | H11-007 |
| next_reminder | 条件给前缀积分比较时，先设前缀原函数，再分部处理带权积分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-103_积分保号性]]
- [[MATHWIKI-METHOD-CLUSTER-123_构造原函数]]
- [[MATHWIKI-METHOD-CLUSTER-321_前缀积分比较]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-072_积分不等式证明入口链]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-340
- GS-337

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
