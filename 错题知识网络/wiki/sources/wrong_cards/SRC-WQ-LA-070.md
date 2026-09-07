---
wiki_id: SRC-WQ-LA-070
type: source_summary
title: "LA-070 分块秩比较ABC为零"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-070_强化例题4.4-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-070"
knowledge:
  - "初等变换"
  - "矩阵秩"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "分块矩阵秩判断"
  - "矩阵初等变换"
  - "矩阵秩不等式"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-167_初等变换"
  - "MATHWIKI-METHOD-CLUSTER-101_矩阵初等变换"
  - "MATHWIKI-METHOD-CLUSTER-127_矩阵秩不等式"
  - "MATHWIKI-METHOD-CLUSTER-143_分块矩阵秩判断"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-013_矩阵秩约束与分块秩比较"
  - "MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# LA-070 分块秩比较ABC为零

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-070_强化例题4.4-2.md`
- wrongnet ID：`LA-070`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 矩阵秩 |
| 题型 | 分块矩阵秩比较 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 初等变换
- 矩阵秩

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 分块矩阵秩判断
- 矩阵初等变换
- 矩阵秩不等式

### 陷阱

- \(ABC=O\) 只用于分块消元和化简，不能把所有分块矩阵的秩直接看成相等。
- \(r_3\) 中出现的是 \((AB)^2\)，比较时要用 \(r((AB)^2)\le r(AB)\)。
- 分块矩阵秩比较要先化成可读的秩表达式，再排序。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先分别把 \(r_1,r_2,r_3\) 化成 \(n\)、\(n+r(AB)\)、\(n+r((AB)^2)\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是凭分块形状猜大小，没有先化成可比较秩表达式 |
| related_method_card_id | L03-009 |
| next_reminder | 看到分块矩阵秩排序，先逐个化简成同一对象的秩，再比较大小。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-167_初等变换]]
- [[MATHWIKI-METHOD-CLUSTER-101_矩阵初等变换]]
- [[MATHWIKI-METHOD-CLUSTER-127_矩阵秩不等式]]
- [[MATHWIKI-METHOD-CLUSTER-143_分块矩阵秩判断]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-013_矩阵秩约束与分块秩比较]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-059
- LA-068
- LA-073
- LA-058

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
