---
wiki_id: SRC-WQ-GS-106
type: source_summary
title: "GS-106 1000题B组3.1"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-106_1000题B组3.1.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-106"
knowledge:
  - "一元函数微分学应用"
  - "可导性判定"
  - "无穷小阶数比较"
  - "绝对值函数"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是把绝对值内部零点直接等同不可导点，需用户复做确认。"
methods:
  - "先找绝对值内部零点"
  - "分解因式判断候选点"
  - "用高阶零点消尖点"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-319_旧批量未记录个人原始错因-当前仅确认复做断点是把绝对值内部零点直接等同不"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-051_无穷小阶数比较"
  - "MATHWIKI-KNOWLEDGE-118_可导性判定"
  - "MATHWIKI-KNOWLEDGE-422_绝对值函数"
  - "MATHWIKI-METHOD-CLUSTER-1206_用高阶零点消尖点"
  - "MATHWIKI-METHOD-CLUSTER-620_先找绝对值内部零点"
  - "MATHWIKI-METHOD-CLUSTER-684_分解因式判断候选点"
  - "MATHWIKI-GS-METHOD-013_导数定义差商入口"
  - "MATHWIKI-GS-METHOD-095_可导性候选点与局部形态判别链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-106 1000题B组3.1

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-106_1000题B组3.1.md`
- wrongnet ID：`GS-106`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 绝对值函数可导性判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 可导性判定
- 无穷小阶数比较
- 绝对值函数

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是把绝对值内部零点直接等同不可导点，需用户复做确认。

### 方法

- 先找绝对值内部零点
- 分解因式判断候选点
- 用高阶零点消尖点

### 陷阱

- 绝对值内部为零只是候选不可导点
- 外部因子可能提高零点阶数
- x^2-x+1 无实根

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先分解绝对值内部表达式并列出内部为零的候选点 |
| missed_action | 旧批量未记录个人步骤；当前复做风险是没有继续检查外部因子阶数是否消掉尖点 |
| related_method_card_id | H03-007 |
| next_reminder | 看到绝对值不可导点，先列内部零点，再检查外部因子是否消掉尖点。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-319_旧批量未记录个人原始错因-当前仅确认复做断点是把绝对值内部零点直接等同不]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-051_无穷小阶数比较]]
- [[MATHWIKI-KNOWLEDGE-118_可导性判定]]
- [[MATHWIKI-KNOWLEDGE-422_绝对值函数]]
- [[MATHWIKI-METHOD-CLUSTER-1206_用高阶零点消尖点]]
- [[MATHWIKI-METHOD-CLUSTER-620_先找绝对值内部零点]]
- [[MATHWIKI-METHOD-CLUSTER-684_分解因式判断候选点]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-013_导数定义差商入口]]
- [[MATHWIKI-GS-METHOD-095_可导性候选点与局部形态判别链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-447

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
