---
wiki_id: SRC-WQ-GS-012
type: source_summary
title: "GS-012 58109 2026.4.22"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-012_581092026.4.22.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-012"
knowledge:
  - "极限与连续"
  - "数列极限"
  - "间断点分类"
  - "主导项"
  - "等价无穷小"
error_causes:
  - "条件忽略"
  - "概念混淆"
  - "方法选择错误"
methods:
  - "分类讨论"
  - "主导项比较"
  - "等价变形"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-064_间断点分类"
  - "MATHWIKI-KNOWLEDGE-086_主导项"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-021_主导项比较"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-METHOD-011_B5-CHECK检查断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-25
related_wrongnet_refs: []
formal_projection_sha256: 6f4084b6834cd5a9e20b705923cf8a6e381917138d79aa49e24453c05796749e
---

# GS-012 58109 2026.4.22

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-012_581092026.4.22.md`
- wrongnet ID：`GS-012`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 无穷小阶数比较 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 数列极限
- 间断点分类
- 主导项
- 等价无穷小

### 错因

- 条件忽略
- 概念混淆
- 方法选择错误

### 方法

- 分类讨论
- 主导项比较
- 等价变形

### 陷阱

- 定义域
- 左右极限
- 适用条件
- 极限过程
- 量纲/阶数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先按 \(0<|x|<1\)、\(|x|=1\)、\(|x|>1\) 求出极限定义的分段函数，再检查 \(x=0,\pm1\) 的左右极限和函数值。 |
| missed_action | 没有先把 \(n\to\infty\) 下的幂函数型极限拆成分段函数，就直接进入连续性判断。 |
| related_method_card_id | H01-008 |
| next_reminder | 看到含 \(x^n,x^{-n}\) 且 \(n\to\infty\) 的连续性题，先按 \(|x|\) 分段求函数表达式，再讨论连续点。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-064_间断点分类]]
- [[MATHWIKI-KNOWLEDGE-086_主导项]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-METHOD-011_B5-CHECK检查断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

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
