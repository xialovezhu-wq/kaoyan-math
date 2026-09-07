---
wiki_id: SRC-WQ-GS-037
type: source_summary
title: "GS-037 1000题B组1.40"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-037_1000题B组1.40.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-037"
knowledge:
  - "极限与连续"
  - "函数极限"
  - "间断点分类"
  - "参数分类讨论"
error_causes:
  - "条件忽略"
  - "定义域错误"
  - "参数范围错误"
methods:
  - "分类讨论"
  - "条件转化"
  - "边界点连续性检查"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-030_定义域错误"
  - "MATHWIKI-ERROR-CLUSTER-036_参数范围错误"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-039_函数极限"
  - "MATHWIKI-KNOWLEDGE-047_参数分类讨论"
  - "MATHWIKI-KNOWLEDGE-064_间断点分类"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-1347_边界点连续性检查"
  - "MATHWIKI-GS-METHOD-011_B5-CHECK检查断点"
  - "MATHWIKI-GS-METHOD-049_连续间断点候选点检查链"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-037 1000题B组1.40

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-037_1000题B组1.40.md`
- wrongnet ID：`GS-037`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 含参极限分段连续性 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 函数极限
- 间断点分类
- 参数分类讨论

### 错因

- 条件忽略
- 定义域错误
- 参数范围错误

### 方法

- 分类讨论
- 条件转化
- 边界点连续性检查

### 陷阱

- 定义域
- 参数边界
- 分段边界
- 适用条件
- 正负号

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先把 \(x\) 分成 \(|x|>1\)、\(|x|<1\)、\(x=1\)、\(x=-1\) 四类求极限函数。 |
| missed_action | 没有先分 \(|x|>1\)、\(|x|<1\) 和边界点，误把幂次结构直觉看成趋无穷。 |
| related_method_card_id | H01-008 |
| next_reminder | 看到含 \(n\) 次幂极限还要求参数连续，先按 \(|x|>1\)、\(|x|<1\)、边界点分段，再用边界连续性列参数方程。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-030_定义域错误]]
- [[MATHWIKI-ERROR-CLUSTER-036_参数范围错误]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-039_函数极限]]
- [[MATHWIKI-KNOWLEDGE-047_参数分类讨论]]
- [[MATHWIKI-KNOWLEDGE-064_间断点分类]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-1347_边界点连续性检查]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-011_B5-CHECK检查断点]]
- [[MATHWIKI-GS-METHOD-049_连续间断点候选点检查链]]
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
