---
wiki_id: SRC-WQ-GS-328
type: source_summary
title: "GS-328 强化例题11.13（判断定积分的正负）-3"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-328_强化例题11.13（判断定积分的正负）-3.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-328"
knowledge:
  - "定积分"
  - "定积分等式"
  - "定积分性质"
error_causes:
  - "触发信息遗漏"
  - "方法调取失败"
methods:
  - "区间再现"
  - "反折比较"
  - "换元"
  - "符号判断"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-084_定积分等式"
  - "MATHWIKI-METHOD-CLUSTER-009_换元"
  - "MATHWIKI-METHOD-CLUSTER-092_区间再现"
  - "MATHWIKI-METHOD-CLUSTER-254_符号判断"
  - "MATHWIKI-METHOD-CLUSTER-792_反折比较"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-328 强化例题11.13（判断定积分的正负）-3

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-328_强化例题11.13（判断定积分的正负）-3.md`
- wrongnet ID：`GS-328`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 定积分符号判断 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分等式
- 定积分性质

### 错因

- 触发信息遗漏
- 方法调取失败

### 方法

- 区间再现
- 反折比较
- 换元
- 符号判断

### 陷阱

- 端点可去奇点不等于发散
- 尾段反折后符号改变
- 只看局部符号未合并比较

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先作 \(x\mapsto \frac{3\pi}{2}-x\)，写出再现后的积分并和原式比较 |
| missed_action | 没有先做区间再现和反折比较 |
| related_method_card_id | H11-003 |
| next_reminder | 看到定积分符号判断，先查能否区间再现，再拆区间比较符号。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-084_定积分等式]]
- [[MATHWIKI-METHOD-CLUSTER-009_换元]]
- [[MATHWIKI-METHOD-CLUSTER-092_区间再现]]
- [[MATHWIKI-METHOD-CLUSTER-254_符号判断]]
- [[MATHWIKI-METHOD-CLUSTER-792_反折比较]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-314
- GS-322

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
