---
wiki_id: SRC-WQ-GS-151
type: source_summary
title: "GS-151 1000题A组5.20"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-151_1000题A组5.20.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-151"
knowledge:
  - "一元函数微分学应用"
  - "等价无穷小"
  - "泰勒展开"
  - "渐近线"
  - "极限与连续"
error_causes:
  - "条件忽略"
methods:
  - "定义域分析"
  - "斜渐近线公式"
  - "正负无穷分别讨论"
  - "等价变形"
  - "泰勒展开"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-038_泰勒展开"
  - "MATHWIKI-KNOWLEDGE-085_渐近线"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-008_泰勒展开"
  - "MATHWIKI-METHOD-CLUSTER-059_斜渐近线公式"
  - "MATHWIKI-METHOD-CLUSTER-238_正负无穷分别讨论"
  - "MATHWIKI-METHOD-CLUSTER-352_定义域分析"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-METHOD-048_渐近线题全类型检查链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-017"
  - "GS-150"
  - "GS-158"
formal_projection_sha256: 4ed0ad72a94cd9db98bbb95f103737e7b1fe8fa735c417c32a9aab8c2e1deb2e
---

# GS-151 1000题A组5.20

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-151_1000题A组5.20.md`
- wrongnet ID：`GS-151`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 渐近线条数判断 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 等价无穷小
- 泰勒展开
- 渐近线
- 极限与连续

### 错因

- 条件忽略

### 方法

- 定义域分析
- 斜渐近线公式
- 正负无穷分别讨论
- 等价变形
- 泰勒展开

### 陷阱

- 定义域
- 正负无穷方向

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先由 $x^2-1>0$ 写出定义域 $(-\infty,-1)\cup(1,\infty)$，列出 $x=\pm1$、$x\to+\infty$、$x\to-\infty$ 四个检查点。 |
| missed_action | 只检查了一个无穷远方向，没有把 $x\to-\infty$ 单独列入斜渐近线检查。 |
| related_method_card_id | H05-005 |
| next_reminder | 看到“全部渐近线/条数”，先列定义域端点、$x\to+\infty$、$x\to-\infty$，不要把正无穷结果自动复制到负无穷。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-038_泰勒展开]]
- [[MATHWIKI-KNOWLEDGE-085_渐近线]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-059_斜渐近线公式]]
- [[MATHWIKI-METHOD-CLUSTER-238_正负无穷分别讨论]]
- [[MATHWIKI-METHOD-CLUSTER-352_定义域分析]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-METHOD-048_渐近线题全类型检查链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-017
- GS-150
- GS-158

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
