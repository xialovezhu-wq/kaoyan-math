---
wiki_id: SRC-WQ-LA-059
type: source_summary
title: "LA-059 块矩阵秩消元判断"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-059_强化例题4.8.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-059"
knowledge:
  - "矩阵秩"
  - "矩阵运算"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "分块矩阵秩判断"
  - "矩阵初等变换"
  - "列空间包含"
  - "反例排除"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-014_矩阵运算"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-METHOD-CLUSTER-067_反例排除"
  - "MATHWIKI-METHOD-CLUSTER-101_矩阵初等变换"
  - "MATHWIKI-METHOD-CLUSTER-143_分块矩阵秩判断"
  - "MATHWIKI-METHOD-CLUSTER-318_列空间包含"
  - "MATHWIKI-LA-METHOD-011_矩阵幂降维与秩空间判断"
  - "MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线"
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
review_batch: "MATHWIKI-REVIEW-086"
formal_projection_sha256: "70b749b09caa6cfd465eb175abf0912a09680c950f9dbb268b556dc4e08db926"
---

# LA-059 块矩阵秩消元判断

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-059_强化例题4.8.md`
- wrongnet ID：`LA-059`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 矩阵秩 |
| 题型 | 块矩阵秩恒等式判断 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 矩阵秩
- 矩阵运算

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 分块矩阵秩判断
- 矩阵初等变换
- 列空间包含
- 反例排除

### 陷阱

- \([A,AB]\) 可用列空间包含解释，但 \([A,BA]\) 不能照搬。
- 块矩阵消元前要确认右上角块是否能由左侧块的列线性表示。
- \(BA-AB\) 一般不为零，除非额外有可交换条件。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先比较 \(\operatorname{Col}(AB)\subseteq\operatorname{Col}(A)\) 是否能迁移到 \(BA\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是把 \(AB\) 的列空间包含结论直接迁移到 \(BA\) |
| related_method_card_id | L03-009 |
| next_reminder | 看到分块秩消元，先检查要消的块是否真的可消，再做初等变换。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-METHOD-CLUSTER-067_反例排除]]
- [[MATHWIKI-METHOD-CLUSTER-101_矩阵初等变换]]
- [[MATHWIKI-METHOD-CLUSTER-143_分块矩阵秩判断]]
- [[MATHWIKI-METHOD-CLUSTER-318_列空间包含]]

### 深度编译页

- [[MATHWIKI-LA-METHOD-011_矩阵幂降维与秩空间判断]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]

## wrongnet 关联题

- 暂无强边。
