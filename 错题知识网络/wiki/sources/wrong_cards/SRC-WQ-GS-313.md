---
wiki_id: SRC-WQ-GS-313
type: source_summary
title: "GS-313 强化例题11.7-2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-313_强化例题11.7-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-313"
knowledge:
  - "定积分"
  - "定积分性质"
  - "定积分等式"
  - "三角换元"
error_causes:
  - "方法论调取失败"
  - "触发信息遗漏"
methods:
  - "三角换元"
  - "区间再现"
  - "对称平均"
  - "差角公式化简"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-080_三角换元"
  - "MATHWIKI-KNOWLEDGE-084_定积分等式"
  - "MATHWIKI-METHOD-CLUSTER-028_三角换元"
  - "MATHWIKI-METHOD-CLUSTER-092_区间再现"
  - "MATHWIKI-METHOD-CLUSTER-931_对称平均"
  - "MATHWIKI-METHOD-CLUSTER-962_差角公式化简"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-313 强化例题11.7-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-313_强化例题11.7-2.md`
- wrongnet ID：`GS-313`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 三角换元与区间再现定积分 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 定积分等式
- 三角换元

### 错因

- 方法论调取失败
- 触发信息遗漏

### 方法

- 三角换元
- 区间再现
- 对称平均
- 差角公式化简

### 陷阱

- 看到 1+x^2 分母没有想到 x=tan t
- 区间再现对称点选错
- 对数相加没有化成常数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先令 x=tan t 把积分区间换成 0 到 pi/4 |
| missed_action | 没有先把 1+x^2 分母转成三角变量后再配对 |
| related_method_card_id | H09-003 |
| next_reminder | 看到 1+x^2 分母，先令 x=tan t，再看新区间能否再现配对。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-080_三角换元]]
- [[MATHWIKI-KNOWLEDGE-084_定积分等式]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-092_区间再现]]
- [[MATHWIKI-METHOD-CLUSTER-931_对称平均]]
- [[MATHWIKI-METHOD-CLUSTER-962_差角公式化简]]

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
