---
wiki_id: SRC-WQ-GS-165
type: source_summary
title: "GS-165 2019年第1题"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-165_2019年第1题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-165"
knowledge:
  - "极限与连续"
  - "函数极限"
  - "幂指极限"
  - "洛必达法则"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是幂指极限没有先整体取对数并在最后指数还原，需用户复做确认。"
methods:
  - "幂指极限对数化"
  - "取对数"
  - "洛必达法则"
  - "标准化计算流程"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-315_旧批量未记录个人原始错因-当前仅确认复做断点是幂指极限没有先整体取对数并"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-017_幂指极限"
  - "MATHWIKI-KNOWLEDGE-039_函数极限"
  - "MATHWIKI-KNOWLEDGE-045_洛必达法则"
  - "MATHWIKI-METHOD-CLUSTER-011_标准化计算流程"
  - "MATHWIKI-METHOD-CLUSTER-019_取对数"
  - "MATHWIKI-METHOD-CLUSTER-099_洛必达法则"
  - "MATHWIKI-METHOD-CLUSTER-969_幂指极限对数化"
  - "MATHWIKI-GS-METHOD-006_先判型总流程"
  - "MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度"
  - "MATHWIKI-GS-METHOD-073_幂指极限对数化闭环"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-165 2019年第1题

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-165_2019年第1题.md`
- wrongnet ID：`GS-165`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 幂指极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 函数极限
- 幂指极限
- 洛必达法则

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是幂指极限没有先整体取对数并在最后指数还原，需用户复做确认。

### 方法

- 幂指极限对数化
- 取对数
- 洛必达法则
- 标准化计算流程

### 陷阱

- 幂指极限先取对数
- 底数极限与指数极限分开处理
- 0/0 型要化成可求导商

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先令整体为 y 并取对数 |
| missed_action | 旧批量未记录个人第一错步；当前只确认不能直接拆底数和指数，必须先对数化 |
| related_method_card_id | H01-002 |
| next_reminder | 看到幂指极限，先设整体取对数，再算 ln y 并指数还原。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-315_旧批量未记录个人原始错因-当前仅确认复做断点是幂指极限没有先整体取对数并]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-017_幂指极限]]
- [[MATHWIKI-KNOWLEDGE-039_函数极限]]
- [[MATHWIKI-KNOWLEDGE-045_洛必达法则]]
- [[MATHWIKI-METHOD-CLUSTER-011_标准化计算流程]]
- [[MATHWIKI-METHOD-CLUSTER-019_取对数]]
- [[MATHWIKI-METHOD-CLUSTER-099_洛必达法则]]
- [[MATHWIKI-METHOD-CLUSTER-969_幂指极限对数化]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-006_先判型总流程]]
- [[MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度]]
- [[MATHWIKI-GS-METHOD-073_幂指极限对数化闭环]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-072

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
