---
wiki_id: SRC-WQ-GS-033
type: source_summary
title: "GS-033 81428 2026.5.5"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-033_814282026.5.5.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-033"
knowledge:
  - "极限与连续"
  - "等价无穷小"
  - "间断点分类"
  - "幂指极限"
error_causes:
  - "概念混淆"
  - "定义域错误"
methods:
  - "分类讨论"
  - "等价变形"
  - "取对数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-030_定义域错误"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-017_幂指极限"
  - "MATHWIKI-KNOWLEDGE-064_间断点分类"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-019_取对数"
  - "MATHWIKI-GS-METHOD-011_B5-CHECK检查断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-033 81428 2026.5.5

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-033_814282026.5.5.md`
- wrongnet ID：`GS-033`
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
- 幂指极限

### 错因

- 概念混淆
- 定义域错误

### 方法

- 分类讨论
- 等价变形
- 取对数

### 陷阱

- 定义域
- 左右极限
- 正负号
- 适用条件
- 极限过程

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先从 \(\ln|x|\)、\(|x-1|\) 分母和 \((x-1)(x-2)\) 指数分母列出可疑点 \(x=0,1,2\)，再逐点判断左右极限类型。 |
| missed_action | 没有先完整列出所有无定义点和指数分母为零点，导致间断点候选遗漏。 |
| related_method_card_id | H01-008 |
| next_reminder | 看到间断点个数题，先从定义域、分母、对数和指数型局部结构列全可疑点，再逐点分类。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-030_定义域错误]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-017_幂指极限]]
- [[MATHWIKI-KNOWLEDGE-064_间断点分类]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-019_取对数]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-011_B5-CHECK检查断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-500

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
