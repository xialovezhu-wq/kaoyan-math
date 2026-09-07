---
wiki_id: SRC-WQ-GS-101
type: source_summary
title: "GS-101 1000题B组3.13"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-101_1000题B组3.13.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-101"
knowledge:
  - "一元函数微分学应用"
  - "可导性判定"
  - "导数定义"
  - "分段函数"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是 |f(x)| 可导性判断未先看 f(a) 是否为 0 及是否一阶穿零，需用户复做确认。"
methods:
  - "按 f(a) 是否为 0 分类"
  - "绝对值尖点判定"
  - "用左右导数检验"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-300_旧批量未记录个人原始错因-当前仅确认复做断点是-f-x-可导性判断未先看"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-006_导数定义"
  - "MATHWIKI-KNOWLEDGE-118_可导性判定"
  - "MATHWIKI-KNOWLEDGE-235_分段函数"
  - "MATHWIKI-METHOD-CLUSTER-1027_按f-a-是否为0分类"
  - "MATHWIKI-METHOD-CLUSTER-1204_用左右导数检验"
  - "MATHWIKI-METHOD-CLUSTER-1309_绝对值尖点判定"
  - "MATHWIKI-GS-METHOD-013_导数定义差商入口"
  - "MATHWIKI-GS-METHOD-095_可导性候选点与局部形态判别链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-101 1000题B组3.13

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-101_1000题B组3.13.md`
- wrongnet ID：`GS-101`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 绝对值复合函数可导性判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 可导性判定
- 导数定义
- 分段函数

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是 |f(x)| 可导性判断未先看 f(a) 是否为 0 及是否一阶穿零，需用户复做确认。

### 方法

- 按 f(a) 是否为 0 分类
- 绝对值尖点判定
- 用左右导数检验

### 陷阱

- 只有过零且一阶穿过时才形成尖点
- f(a) 不为 0 时绝对值外层局部光滑
- f'(a)=0 时不一定不可导

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先分类讨论 f(a)≠0 与 f(a)=0 两种情况 |
| missed_action | 旧批量未记录个人步骤；当前复做风险是把有绝对值直接等同于不可导 |
| related_method_card_id | H03-004 |
| next_reminder | 看到 |f(x)| 的可导性，先看 f(a) 是否为 0，再看 f'(a) 是否非零穿零。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-300_旧批量未记录个人原始错因-当前仅确认复做断点是-f-x-可导性判断未先看]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-006_导数定义]]
- [[MATHWIKI-KNOWLEDGE-118_可导性判定]]
- [[MATHWIKI-KNOWLEDGE-235_分段函数]]
- [[MATHWIKI-METHOD-CLUSTER-1027_按f-a-是否为0分类]]
- [[MATHWIKI-METHOD-CLUSTER-1204_用左右导数检验]]
- [[MATHWIKI-METHOD-CLUSTER-1309_绝对值尖点判定]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-013_导数定义差商入口]]
- [[MATHWIKI-GS-METHOD-095_可导性候选点与局部形态判别链]]
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
