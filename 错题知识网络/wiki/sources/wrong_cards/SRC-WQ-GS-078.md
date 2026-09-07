---
wiki_id: SRC-WQ-GS-078
type: source_summary
title: "GS-078 1000题强化2.7"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-078_1000题强化2.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-078"
knowledge:
  - "极限与连续"
  - "数列极限"
  - "递推数列"
  - "等价无穷小"
error_causes:
  - "方法选择错误"
  - "动作链断裂"
methods:
  - "等价无穷小"
  - "递推式消去"
  - "单调有界准则"
  - "比值法"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-053_递推数列"
  - "MATHWIKI-METHOD-CLUSTER-010_单调有界准则"
  - "MATHWIKI-METHOD-CLUSTER-026_等价无穷小"
  - "MATHWIKI-METHOD-CLUSTER-1375_递推式消去"
  - "MATHWIKI-METHOD-CLUSTER-239_比值法"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-METHOD-092_三角隐式根与递推比阶入口链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-007_数列极限错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-078 1000题强化2.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-078_1000题强化2.7.md`
- wrongnet ID：`GS-078`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 余弦隐式递推二阶极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 4 |

## 可编译信息

### 知识点

- 极限与连续
- 数列极限
- 递推数列
- 等价无穷小

### 错因

- 方法选择错误
- 动作链断裂

### 方法

- 等价无穷小
- 递推式消去
- 单调有界准则
- 比值法

### 陷阱

- 余弦递推
- 高阶小量
- 二阶主项

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把递推式改写成 $x_{n+1}=(1-\cos x_n)-(1-\cos x_{n+1})$。 |
| missed_action | 没有先拆出 $1-\cos$，因此没有把 $x_{n+1}$ 与 $x_n^2$ 的二阶关系建立起来。 |
| related_method_card_id | H01-004 |
| next_reminder | 看到 $1-\cos$ 相关的二阶小量，先拆出 $1-\cos t$ 再比阶。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-053_递推数列]]
- [[MATHWIKI-METHOD-CLUSTER-010_单调有界准则]]
- [[MATHWIKI-METHOD-CLUSTER-026_等价无穷小]]
- [[MATHWIKI-METHOD-CLUSTER-1375_递推式消去]]
- [[MATHWIKI-METHOD-CLUSTER-239_比值法]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-METHOD-092_三角隐式根与递推比阶入口链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-007_数列极限错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-080
- GS-442
- GS-444

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
