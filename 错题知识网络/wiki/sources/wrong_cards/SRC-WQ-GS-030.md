---
wiki_id: SRC-WQ-GS-030
type: source_summary
title: "GS-030 58098 2026.5.7"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-030_580982026.5.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-030"
knowledge:
  - "极限与连续"
  - "等价无穷小"
  - "间断点分类"
  - "取整函数"
  - "幂指极限"
error_causes:
  - "分类讨论不全"
methods:
  - "分类讨论"
  - "等价变形"
  - "取对数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-023_分类讨论不全"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-017_幂指极限"
  - "MATHWIKI-KNOWLEDGE-064_间断点分类"
  - "MATHWIKI-KNOWLEDGE-324_取整函数"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-019_取对数"
  - "MATHWIKI-GS-METHOD-008_分类讨论闭环"
  - "MATHWIKI-GS-METHOD-011_B5-CHECK检查断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-030 58098 2026.5.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-030_580982026.5.7.md`
- wrongnet ID：`GS-030`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 幂指函数极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 等价无穷小
- 间断点分类
- 取整函数
- 幂指极限

### 错因

- 分类讨论不全

### 方法

- 分类讨论
- 等价变形
- 取对数

### 陷阱

- 左右极限
- 参数边界
- 适用条件
- 定义域
- 极限过程

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先分 \(x\to0^+\)、\(x\to0^-\)，分别把 \([x]\) 固定为 \(0\) 和 \(-1\)，再计算左右极限并令其相等。 |
| missed_action | 虽然想到分左右极限，但没有同步替换取整函数在两侧的具体取值。 |
| related_method_card_id | H01-008 |
| next_reminder | 看到取整函数的连续性题，先锁定左右邻域内 \([x]\) 的具体常值，再代入极限。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-023_分类讨论不全]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-017_幂指极限]]
- [[MATHWIKI-KNOWLEDGE-064_间断点分类]]
- [[MATHWIKI-KNOWLEDGE-324_取整函数]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-019_取对数]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-008_分类讨论闭环]]
- [[MATHWIKI-GS-METHOD-011_B5-CHECK检查断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-029
- GS-033
- GS-009

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
