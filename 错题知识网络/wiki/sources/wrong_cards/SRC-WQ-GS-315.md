---
wiki_id: SRC-WQ-GS-315
type: source_summary
title: "GS-315 1000题A组11.6-2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-315_1000题A组11.6-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-315"
knowledge:
  - "定积分"
  - "反常积分"
  - "第二类换元"
  - "定积分性质"
error_causes:
  - "方法论调取失败"
  - "动作链断裂"
methods:
  - "倒代换"
  - "结构换元"
  - "反常积分标准型"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-028_反常积分"
  - "MATHWIKI-KNOWLEDGE-041_第二类换元"
  - "MATHWIKI-METHOD-CLUSTER-109_倒代换"
  - "MATHWIKI-METHOD-CLUSTER-452_结构换元"
  - "MATHWIKI-METHOD-CLUSTER-790_反常积分标准型"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-315 1000题A组11.6-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-315_1000题A组11.6-2.md`
- wrongnet ID：`GS-315`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 反常积分等式与换元求值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 反常积分
- 第二类换元
- 定积分性质

### 错因

- 方法论调取失败
- 动作链断裂

### 方法

- 倒代换
- 结构换元
- 反常积分标准型

### 陷阱

- 没有用 x=1/t 先证明两个积分相等
- 结构换元方向不明确
- 反常上下限变化漏写

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先令 x=1/t 检查两个反常积分是否相等 |
| missed_action | 没有先用倒代换建立对称等式 |
| related_method_card_id | H09-003 |
| next_reminder | 看到 0 到无穷的 x 与 1/x 对称反常积分，先倒代换，再找结构变量。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-028_反常积分]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-METHOD-CLUSTER-109_倒代换]]
- [[MATHWIKI-METHOD-CLUSTER-452_结构换元]]
- [[MATHWIKI-METHOD-CLUSTER-790_反常积分标准型]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
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
