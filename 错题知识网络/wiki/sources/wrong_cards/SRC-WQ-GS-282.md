---
wiki_id: SRC-WQ-GS-282
type: source_summary
title: "GS-282 强化例题9.15(171537)"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-282_强化例题9.15(171537).md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-282"
knowledge:
  - "反常积分"
  - "有理函数积分"
  - "部分分式"
  - "参数方程"
error_causes:
  - "暂无明确个人错因（视觉证据仅支持复做入口）"
methods:
  - "部分分式分解"
  - "反常积分极限"
  - "参数反求"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）"
  - "MATHWIKI-KNOWLEDGE-028_反常积分"
  - "MATHWIKI-KNOWLEDGE-044_有理函数积分"
  - "MATHWIKI-KNOWLEDGE-046_部分分式"
  - "MATHWIKI-KNOWLEDGE-169_参数方程"
  - "MATHWIKI-METHOD-CLUSTER-057_反常积分极限"
  - "MATHWIKI-METHOD-CLUSTER-183_部分分式分解"
  - "MATHWIKI-METHOD-CLUSTER-205_参数反求"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-076_分式积分拆到底与分母降幂链"
  - "MATHWIKI-GS-METHOD-087_含参反常积分候选根与奇点回查"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-282 强化例题9.15(171537)

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-282_强化例题9.15(171537).md`
- wrongnet ID：`GS-282`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 反常积分 |
| 题型 | 反常积分参数反求 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 反常积分
- 有理函数积分
- 部分分式
- 参数方程

### 错因

- 暂无明确个人错因（视觉证据仅支持复做入口）

### 方法

- 部分分式分解
- 反常积分极限
- 参数反求

### 陷阱

- 无穷远端要取极限
- 对数差不能漏常数
- a 在分母中影响下限值
- 先假定参数使积分有意义

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先分解 a/[x(2x+a)] = 1/x - 2/(2x+a) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有先拆部分分式，或无穷远端对数极限处理不完整 |
| related_method_card_id | H09-004 |
| next_reminder | 看到有理函数反常积分，先部分分式，再把无穷端写成极限后反求参数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）]]
- [[MATHWIKI-KNOWLEDGE-028_反常积分]]
- [[MATHWIKI-KNOWLEDGE-044_有理函数积分]]
- [[MATHWIKI-KNOWLEDGE-046_部分分式]]
- [[MATHWIKI-KNOWLEDGE-169_参数方程]]
- [[MATHWIKI-METHOD-CLUSTER-057_反常积分极限]]
- [[MATHWIKI-METHOD-CLUSTER-183_部分分式分解]]
- [[MATHWIKI-METHOD-CLUSTER-205_参数反求]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-076_分式积分拆到底与分母降幂链]]
- [[MATHWIKI-GS-METHOD-087_含参反常积分候选根与奇点回查]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-276
- GS-277
- GS-278

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
