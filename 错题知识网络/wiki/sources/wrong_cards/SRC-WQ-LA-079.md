---
wiki_id: SRC-WQ-LA-079
type: source_summary
title: "LA-079 强化例题5.3"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-079_强化例题5.3.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-079"
knowledge:
  - "线性方程组"
  - "矩阵秩"
  - "矩阵运算"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "齐次方程组基础解系"
  - "零空间构造右零因子"
  - "Sylvester秩不等式反证"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-014_矩阵运算"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-033_线性方程组"
  - "MATHWIKI-METHOD-CLUSTER-104_齐次方程组基础解系"
  - "MATHWIKI-METHOD-CLUSTER-1413_零空间构造右零因子"
  - "MATHWIKI-METHOD-CLUSTER-488_Sylvester秩不等式反证"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-017_线性方程组零空间与秩约束入口链"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# LA-079 强化例题5.3

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-079_强化例题5.3.md`
- wrongnet ID：`LA-079`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 线性方程组 |
| 题型 | 矩阵零空间与右零因子秩构造 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 线性方程组
- 矩阵秩
- 矩阵运算

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 齐次方程组基础解系
- 零空间构造右零因子
- Sylvester秩不等式反证

### 陷阱

- \(AC=O\) 表示 \(C\) 的每一列都落入 \(A\) 的零空间
- 构造秩一矩阵时，可让三列都取同一个非零零空间向量
- 反证秩二右零因子时，用 \(r(A)+r(C)\le n\) 约束，不要只凭直觉猜构造

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先求 \(Ax=0\) 的基础解系，并把 \(C\) 的每一列看成零空间向量 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是把 \(C\) 当整体硬设，没有按列进入 \(A\) 的零空间 |
| related_method_card_id | L03-010 |
| next_reminder | 看到 \(AC=O\)，先按列拆 \(C\)，每一列都必须属于 \(Ax=0\) 的零空间。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-033_线性方程组]]
- [[MATHWIKI-METHOD-CLUSTER-104_齐次方程组基础解系]]
- [[MATHWIKI-METHOD-CLUSTER-1413_零空间构造右零因子]]
- [[MATHWIKI-METHOD-CLUSTER-488_Sylvester秩不等式反证]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-017_线性方程组零空间与秩约束入口链]]
- [[MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-078
- LA-081
- LA-090

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
