---
wiki_id: SRC-WQ-GS-227
type: source_summary
title: "GS-227 强化例题6.12"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-227_强化例题6.12.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-227"
knowledge:
  - "一元函数微分学应用"
  - "中值定理"
  - "拉格朗日中值定理"
  - "闭区间最值定理"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是没有先取 \\(|f|\\) 最大值点并连最近端点套拉格朗日中值定理，需用户复做确认。"
methods:
  - "最大值点定位"
  - "拉格朗日中值定理"
  - "反证法"
  - "连续导数条件"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-326_旧批量未记录个人原始错因-当前仅确认复做断点是没有先取-f-最大值点并连"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-KNOWLEDGE-021_拉格朗日中值定理"
  - "MATHWIKI-KNOWLEDGE-221_闭区间最值定理"
  - "MATHWIKI-METHOD-CLUSTER-014_拉格朗日中值定理"
  - "MATHWIKI-METHOD-CLUSTER-079_反证法"
  - "MATHWIKI-METHOD-CLUSTER-1086_最大值点定位"
  - "MATHWIKI-METHOD-CLUSTER-1353_连续导数条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-219"
formal_projection_sha256: a00ed5f689929cf7aa4a2d3a2a0f134c05a232f1293d506180a84875940fb19a
---

# GS-227 强化例题6.12

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-227_强化例题6.12.md`
- wrongnet ID：`GS-227`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 导数最大值估计证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 中值定理
- 拉格朗日中值定理
- 闭区间最值定理

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是没有先取 \(|f|\) 最大值点并连最近端点套拉格朗日中值定理，需用户复做确认。

### 方法

- 最大值点定位
- 拉格朗日中值定理
- 反证法
- 连续导数条件

### 陷阱

- 最大值点不在端点
- 最近端点距离不超过1
- 等号情形需检查导数连续性

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先取 \(x_0\) 使 \(|f(x_0)|=M\)，并判断 \(x_0\) 离 0 还是 2 更近 |
| missed_action | 没有先把抽象的 \(M\) 落到最大值点，再连端点触发中值定理 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到端点为零且给出 \(M=\max |f|\)，先取最大值点，再连最近端点套拉格朗日中值定理。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-326_旧批量未记录个人原始错因-当前仅确认复做断点是没有先取-f-最大值点并连]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-KNOWLEDGE-021_拉格朗日中值定理]]
- [[MATHWIKI-KNOWLEDGE-221_闭区间最值定理]]
- [[MATHWIKI-METHOD-CLUSTER-014_拉格朗日中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-079_反证法]]
- [[MATHWIKI-METHOD-CLUSTER-1086_最大值点定位]]
- [[MATHWIKI-METHOD-CLUSTER-1353_连续导数条件]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-219

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
