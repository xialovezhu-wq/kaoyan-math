---
wiki_id: SRC-WQ-GS-329
type: source_summary
title: "GS-329 强化例题11.14 定积分的分部积分法"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-329_强化例题11.14定积分的分部积分法.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-329"
knowledge:
  - "定积分"
  - "分部积分"
  - "第一类换元"
error_causes:
  - "动作链断裂"
  - "运算路径不稳"
methods:
  - "换元处理复合导数"
  - "分部积分"
  - "原函数关系求导"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-028_运算路径不稳"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-1036_换元处理复合导数"
  - "MATHWIKI-METHOD-CLUSTER-742_原函数关系求导"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-329 强化例题11.14 定积分的分部积分法

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-329_强化例题11.14定积分的分部积分法.md`
- wrongnet ID：`GS-329`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 定积分分部积分计算 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 分部积分
- 第一类换元

### 错因

- 动作链断裂
- 运算路径不稳

### 方法

- 换元处理复合导数
- 分部积分
- 原函数关系求导

### 陷阱

- 把“$g$ 的原函数”误当成 $g$ 本身
- 漏掉 $t=2x$ 带来的 $1/4$ 系数
- 分部积分边界项漏算

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先令 \(t=2x\)，把原积分化为 \(\frac14\int_0^2 t g^{\prime}(t)\,dt\) |
| missed_action | 没有先处理链式系数和分部积分边界项 |
| related_method_card_id | H11-005 |
| next_reminder | 看到 \(g'(kx)\)，先换元补齐链式系数，再决定是否分部。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-028_运算路径不稳]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-1036_换元处理复合导数]]
- [[MATHWIKI-METHOD-CLUSTER-742_原函数关系求导]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
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
