---
wiki_id: SRC-WQ-GS-284
type: source_summary
title: "GS-284 强化例题9.18（78365）"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-284_强化例题9.18（78365）.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-284"
knowledge:
  - "定积分"
  - "含参积分"
  - "绝对值分段"
  - "最值问题"
  - "导数应用"
error_causes:
  - "暂无明确个人错因（视觉证据仅支持复做入口）"
methods:
  - "分段讨论"
  - "拆绝对值"
  - "参数积分求导"
  - "单调性最值"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-185_绝对值分段"
  - "MATHWIKI-KNOWLEDGE-246_含参积分"
  - "MATHWIKI-KNOWLEDGE-350_导数应用"
  - "MATHWIKI-KNOWLEDGE-383_最值问题"
  - "MATHWIKI-METHOD-CLUSTER-1011_拆绝对值"
  - "MATHWIKI-METHOD-CLUSTER-311_分段讨论"
  - "MATHWIKI-METHOD-CLUSTER-735_单调性最值"
  - "MATHWIKI-METHOD-CLUSTER-759_参数积分求导"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-284 强化例题9.18（78365）

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-284_强化例题9.18（78365）.md`
- wrongnet ID：`GS-284`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 含绝对值参数定积分求导与最值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 含参积分
- 绝对值分段
- 最值问题
- 导数应用

### 错因

- 暂无明确个人错因（视觉证据仅支持复做入口）

### 方法

- 分段讨论
- 拆绝对值
- 参数积分求导
- 单调性最值

### 陷阱

- 分界点是 t=x 是否落在 [0,1]
- x>1 时绝对值全同号
- 最小值在 x=1/2
- 函数无最大值

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先比较 x 与积分区间 [0,1]，按 0<x<1 和 x>=1 分段 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有先判断 t=x 是否落在积分区间，直接对绝对值整体求导 |
| related_method_card_id | H09-007 |
| next_reminder | 看到绝对值积分含参数，先判断零点是否进区间，再拆绝对值分段求导。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-185_绝对值分段]]
- [[MATHWIKI-KNOWLEDGE-246_含参积分]]
- [[MATHWIKI-KNOWLEDGE-350_导数应用]]
- [[MATHWIKI-KNOWLEDGE-383_最值问题]]
- [[MATHWIKI-METHOD-CLUSTER-1011_拆绝对值]]
- [[MATHWIKI-METHOD-CLUSTER-311_分段讨论]]
- [[MATHWIKI-METHOD-CLUSTER-735_单调性最值]]
- [[MATHWIKI-METHOD-CLUSTER-759_参数积分求导]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-274

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
