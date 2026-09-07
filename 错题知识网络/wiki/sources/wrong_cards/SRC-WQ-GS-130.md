---
wiki_id: SRC-WQ-GS-130
type: source_summary
title: "GS-130 57936 2026.4.16"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-130_579362026.4.16.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-130"
knowledge:
  - "一元函数微分学应用"
  - "单调性与极值"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是没有从任意两点差值估计转入单调定义法，需用户复做确认。"
methods:
  - "单调定义法"
  - "两点差值估计"
  - "绝对值不等式"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-324_旧批量未记录个人原始错因-当前仅确认复做断点是没有从任意两点差值估计转入"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-METHOD-CLUSTER-1307_绝对值不等式"
  - "MATHWIKI-METHOD-CLUSTER-530_两点差值估计"
  - "MATHWIKI-METHOD-CLUSTER-729_单调定义法"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-130 57936 2026.4.16

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-130_579362026.4.16.md`
- wrongnet ID：`GS-130`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 两点差值估计证明单调性 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 单调性与极值

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是没有从任意两点差值估计转入单调定义法，需用户复做确认。

### 方法

- 单调定义法
- 两点差值估计
- 绝对值不等式

### 陷阱

- 没有可导条件不能用导数法
- 题面“单调增加”实际只能证明单调不减
- 没有先取 $x_1<x_2$ 固定方向

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先任取 x1<x2 并把右端绝对值化为 x2-x1 |
| missed_action | 旧批量未记录个人步骤；当前复做风险是误走导数法或没有固定 x1<x2 的方向 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到两点差值估计证明单调，先任取 x1<x2，再按单调定义配凑 F(x1)<=F(x2)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-324_旧批量未记录个人原始错因-当前仅确认复做断点是没有从任意两点差值估计转入]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-METHOD-CLUSTER-1307_绝对值不等式]]
- [[MATHWIKI-METHOD-CLUSTER-530_两点差值估计]]
- [[MATHWIKI-METHOD-CLUSTER-729_单调定义法]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

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
