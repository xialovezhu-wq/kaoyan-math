---
wiki_id: SRC-WQ-GS-339
type: source_summary
title: "GS-339 强化例题11.17 某些特殊的函数值，我们也可以用定积分表示出来-2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-339_强化例题11.17某些特殊的函数值，我们也可以用定积分表示出来-.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-339"
knowledge:
  - "定积分"
  - "定积分性质"
error_causes:
  - "触发信息遗漏"
  - "方法调取失败"
methods:
  - "常数项积分化"
  - "凑完全平方"
  - "积分保号性"
  - "等号情形"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-METHOD-CLUSTER-103_积分保号性"
  - "MATHWIKI-METHOD-CLUSTER-1286_等号情形"
  - "MATHWIKI-METHOD-CLUSTER-225_常数项积分化"
  - "MATHWIKI-METHOD-CLUSTER-300_凑完全平方"
  - "MATHWIKI-GS-METHOD-072_积分不等式证明入口链"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-339 强化例题11.17 某些特殊的函数值，我们也可以用定积分表示出来-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-339_强化例题11.17某些特殊的函数值，我们也可以用定积分表示出来-.md`
- wrongnet ID：`GS-339`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 定积分不等式求函数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质

### 错因

- 触发信息遗漏
- 方法调取失败

### 方法

- 常数项积分化
- 凑完全平方
- 积分保号性
- 等号情形

### 陷阱

- 没有把 $1/5$ 写成 $\int_0^1x^4dx$
- 凑平方方向符号反了
- 非负连续函数积分为 0 才能推出恒为 0

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先写 \(\frac15=\int_0^1x^4\,dx\) |
| missed_action | 没有把常数项积分化进平方结构 |
| related_method_card_id | H11-007 |
| next_reminder | 看到积分不等式里有平方项和常数项，先把常数积分化，再凑非负平方。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-METHOD-CLUSTER-103_积分保号性]]
- [[MATHWIKI-METHOD-CLUSTER-1286_等号情形]]
- [[MATHWIKI-METHOD-CLUSTER-225_常数项积分化]]
- [[MATHWIKI-METHOD-CLUSTER-300_凑完全平方]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-072_积分不等式证明入口链]]
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
