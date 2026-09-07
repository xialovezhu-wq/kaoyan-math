---
wiki_id: SRC-WQ-GS-072
type: source_summary
title: "GS-072 2022年第六题 复合数列极限反推"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-072_2022年第六题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-072"
knowledge:
  - "数列极限"
  - "函数极限"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是先检查外层函数在内层值域上是否一一可逆，不可逆时构造同值振荡反例，需用户复做确认是否为当时第一断点。"
methods:
  - "一一性判断"
  - "反函数连续性"
  - "同值反例构造"
  - "选择题排除法"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-283_旧批量未记录个人原始错因-当前仅确认复做入口是先检查外层函数在内层值域上"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-039_函数极限"
  - "MATHWIKI-METHOD-CLUSTER-1365_选择题排除法"
  - "MATHWIKI-METHOD-CLUSTER-502_一一性判断"
  - "MATHWIKI-METHOD-CLUSTER-784_反函数连续性"
  - "MATHWIKI-METHOD-CLUSTER-821_同值反例构造"
  - "MATHWIKI-GS-METHOD-022_发散数列函数变换反例"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-007_数列极限错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-072 2022年第六题 复合数列极限反推

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-072_2022年第六题.md`
- wrongnet ID：`GS-072`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 数列极限与复合函数极限反推 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 数列极限
- 函数极限

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是先检查外层函数在内层值域上是否一一可逆，不可逆时构造同值振荡反例，需用户复做确认是否为当时第一断点。

### 方法

- 一一性判断
- 反函数连续性
- 同值反例构造
- 选择题排除法

### 陷阱

- 复合极限存在不一定推出原数列极限存在
- 只有外层函数在内层值域上可逆时，才能用反函数连续性反推
- 端点振荡数列可以让原数列不收敛，但复合后变成常数列

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先列出内层值域，并判断外层函数在该区间上是否严格单调或一一对应。 |
| missed_action | 个人原始作答未记录；当前只把题图解析确认的一一性检查入口登记为复做检查点。 |
| related_method_card_id | H02-007 |
| next_reminder | 看到复合极限反推，先查外层在内层值域是否一一可逆，不可逆就找同值振荡反例。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-283_旧批量未记录个人原始错因-当前仅确认复做入口是先检查外层函数在内层值域上]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-039_函数极限]]
- [[MATHWIKI-METHOD-CLUSTER-1365_选择题排除法]]
- [[MATHWIKI-METHOD-CLUSTER-502_一一性判断]]
- [[MATHWIKI-METHOD-CLUSTER-784_反函数连续性]]
- [[MATHWIKI-METHOD-CLUSTER-821_同值反例构造]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-022_发散数列函数变换反例]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-007_数列极限错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-031
- GS-037
- GS-165

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
