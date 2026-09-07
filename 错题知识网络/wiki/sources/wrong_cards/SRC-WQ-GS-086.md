---
wiki_id: SRC-WQ-GS-086
type: source_summary
title: "GS-086 57964 2026.4.28"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-086_579642026.4.28.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-086"
knowledge:
  - "微分方程"
  - "高阶常系数线性微分方程"
  - "泰勒公式"
  - "泰勒展开"
  - "等价无穷小"
error_causes:
  - "证明结构不完整"
methods:
  - "等价变形"
  - "泰勒展开"
  - "取对数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-006_B1-GOAL"
  - "MATHWIKI-ERROR-CLUSTER-011_证明结构不完整"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-KNOWLEDGE-038_泰勒展开"
  - "MATHWIKI-KNOWLEDGE-160_高阶常系数线性微分方程"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-008_泰勒展开"
  - "MATHWIKI-METHOD-CLUSTER-019_取对数"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-086 57964 2026.4.28

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-086_579642026.4.28.md`
- wrongnet ID：`GS-086`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 微分方程 |
| 题型 | 幂指函数极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 微分方程
- 高阶常系数线性微分方程
- 泰勒公式
- 泰勒展开
- 等价无穷小

### 错因

- 证明结构不完整

### 方法

- 等价变形
- 泰勒展开
- 取对数

### 陷阱

- 适用条件
- 主导项
- 定义域
- 量纲/阶数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B1-GOAL |
| expected_first_action | 先把 \(x=0,\ y(0)=0,\ y'(0)=0\) 代入方程求 \(y''(0)\) |
| missed_action | 没有先由方程代值求局部泰勒主项，而是想完整解微分方程。 |
| related_method_card_id | H15-001 |
| next_reminder | 看到微分方程初值条件但只问局部等价，先代点求最低非零阶导数，再写泰勒主项，不急着求通解。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-006_B1-GOAL]]
- [[MATHWIKI-ERROR-CLUSTER-011_证明结构不完整]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-KNOWLEDGE-038_泰勒展开]]
- [[MATHWIKI-KNOWLEDGE-160_高阶常系数线性微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-019_取对数]]

### 深度编译页

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
