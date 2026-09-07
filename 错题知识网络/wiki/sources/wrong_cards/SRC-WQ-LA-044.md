---
wiki_id: SRC-WQ-LA-044
type: source_summary
title: "LA-044 正交对角化构造正定平方根"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-044_强化例题9.14.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-044"
knowledge:
  - "实对称矩阵"
  - "特征值与特征向量"
  - "正定矩阵"
  - "相似矩阵"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "正交对角化"
  - "特征分解"
  - "正定矩阵判定"
  - "矩阵平方根"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-016_特征值与特征向量"
  - "MATHWIKI-KNOWLEDGE-040_相似矩阵"
  - "MATHWIKI-KNOWLEDGE-056_实对称矩阵"
  - "MATHWIKI-KNOWLEDGE-113_正定矩阵"
  - "MATHWIKI-METHOD-CLUSTER-023_特征分解"
  - "MATHWIKI-METHOD-CLUSTER-1236_矩阵平方根"
  - "MATHWIKI-METHOD-CLUSTER-125_正定矩阵判定"
  - "MATHWIKI-METHOD-CLUSTER-168_正交对角化"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-007_二次型合同相似与正定平方根"
  - "MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
formal_projection_sha256: "667916ffe557b9b2ed174587777201064d3e3a9d74b9a1497fea33f9903ee6a5"
relation_review_batch: "MATHWIKI-REVIEW-088"
---

# LA-044 正交对角化构造正定平方根

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-044_强化例题9.14.md`
- wrongnet ID：`LA-044`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 二次型 |
| 题型 | 实对称矩阵正交对角化与正定平方根 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 实对称矩阵
- 特征值与特征向量
- 正定矩阵
- 相似矩阵

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 正交对角化
- 特征分解
- 正定矩阵判定
- 矩阵平方根

### 陷阱

- 实对称矩阵可用正交矩阵 \(P\) 对角化，\(P\) 的列是单位正交特征向量。
- \((a+3)E-A\) 的特征值要由 \(A\) 的特征值同步变换。
- 正定平方根不是逐元素开方，而是在正交对角化后的特征值上开方。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先求实对称矩阵的特征值和单位正交特征向量 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是对矩阵逐元素开方，或重特征值子空间未取单位正交基 |
| related_method_card_id | L08-010 |
| next_reminder | 看到矩阵正定开方，先谱分解 \(M=Q\Lambda Q^{\mathsf T}\)，再写 \(C=Q\sqrt\Lambda Q^{\mathsf T}\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-016_特征值与特征向量]]
- [[MATHWIKI-KNOWLEDGE-040_相似矩阵]]
- [[MATHWIKI-KNOWLEDGE-056_实对称矩阵]]
- [[MATHWIKI-KNOWLEDGE-113_正定矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-023_特征分解]]
- [[MATHWIKI-METHOD-CLUSTER-1236_矩阵平方根]]
- [[MATHWIKI-METHOD-CLUSTER-125_正定矩阵判定]]
- [[MATHWIKI-METHOD-CLUSTER-168_正交对角化]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-007_二次型合同相似与正定平方根]]
- [[MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## 关联卡片

- 暂无强边。

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
