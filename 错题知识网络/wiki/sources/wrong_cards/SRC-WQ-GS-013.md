---
wiki_id: SRC-WQ-GS-013
type: source_summary
title: "GS-013 58041 2026.5.7"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-013_580412026.5.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-013"
knowledge:
  - "数列极限"
  - "主导项"
  - "幂指极限"
  - "等价无穷小"
  - "极限与连续"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是负指数先倒数化，再比较 n 次根号最大主导底数"
methods:
  - "等价变形"
  - "主导项比较"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-296_旧批量未记录个人原始错因-当前仅确认复做入口是负指数先倒数化-再比较n次"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-017_幂指极限"
  - "MATHWIKI-KNOWLEDGE-086_主导项"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-021_主导项比较"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-013 58041 2026.5.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-013_580412026.5.7.md`
- wrongnet ID：`GS-013`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 数列极限 |
| 题型 | 幂指函数极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 数列极限
- 主导项
- 幂指极限
- 等价无穷小
- 极限与连续

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是负指数先倒数化，再比较 n 次根号最大主导底数

### 方法

- 等价变形
- 主导项比较
- 条件转化

### 陷阱

- 适用条件
- 主导项
- 定义域
- 量纲/阶数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先把 \(a_i^{-n}\) 写成 \((1/a_i)^n\)，比较 \(1/a_1\) 与 \(1/a_2\) |
| missed_action | 个人原始漏步未记录；当前只确认复做时必须先倒数化再比较主导底数，不能直接按 \(a_1<a_2\) 原顺序判断 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到负指数的 n 次根号主导项，先倒数化再比较底数；负指数会反转大小关系。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-296_旧批量未记录个人原始错因-当前仅确认复做入口是负指数先倒数化-再比较n次]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-017_幂指极限]]
- [[MATHWIKI-KNOWLEDGE-086_主导项]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-010
- GS-011
- GS-038

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
