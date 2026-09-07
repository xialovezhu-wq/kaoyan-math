---
wiki_id: SRC-WQ-LA-060
type: source_summary
title: "LA-060 分块伴随矩阵求法"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-060_2023年真题第八题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-060"
knowledge:
  - "矩阵运算"
  - "逆矩阵"
  - "行列式"
  - "伴随矩阵"
  - "分块矩阵"
  - "分块矩阵方程"
error_causes:
  - "概念：把普通二阶标量行列式公式误用于分块上三角矩阵。"
  - "方法触发：得到 M*=|M|M^{-1} 后没有继续求分块逆矩阵。"
  - "计算：求右上分块时漏掉负号。"
  - "表达：未把 |A|A^{-1}、|B|B^{-1} 对齐为 A*、B*。"
  - "对象：未稳定区分 n 阶单位块与 2n 阶单位矩阵。"
methods:
  - "伴随矩阵"
  - "分块矩阵方程"
  - "逆矩阵定义"
  - "行列式性质"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001"

  - "MATHWIKI-ERROR-CLUSTER-009"

  - "MATHWIKI-KNOWLEDGE-023"

  - "MATHWIKI-KNOWLEDGE-077"

  - "MATHWIKI-METHOD-CLUSTER-108"

  - "MATHWIKI-METHOD-CLUSTER-179"

  - "MATHWIKI-METHOD-CLUSTER-304"

  - "MATHWIKI-METHOD-CLUSTER-463"

  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-010_伴随矩阵与反对称结构"
  - "MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-08-27
formal_projection_sha256: b112ae1f79e2ee01d7238c8583ed4d48eac22ae1f13b95854aab50c503afed1d
---

# LA-060 分块伴随矩阵求法

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-060_2023年真题第八题.md`
- wrongnet ID：`LA-060`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 矩阵运算 |
| 题型 | 分块矩阵伴随矩阵 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 逆矩阵
- 行列式

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 伴随矩阵
- 分块矩阵方程
- 逆矩阵定义
- 行列式性质

### 陷阱

- \(M^*\) 是 \(2n\) 阶分块矩阵的伴随矩阵，不是分别对每个块取伴随后随意拼接。
- 分块上三角矩阵满足 \(|M|=|A||B|\)。
- 用 \(A^{-1}=A^*/|A|\)、\(B^{-1}=B^*/|B|\) 时要注意左右位置和负号。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先设 \(M^*=\begin{pmatrix}X&Y\\Z&W\end{pmatrix}\)，不要直接拼 \(A^*,B^*\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是直接套对角分块伴随，漏掉右上角单位块带来的非零块 |
| related_method_card_id | L03-009 |
| next_reminder | 看到非对角分块矩阵求伴随，先设未知块并代入 \(MM^*=|M|E\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-023_行列式]]
- [[MATHWIKI-KNOWLEDGE-077_逆矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-108_伴随矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-179_行列式性质]]
- [[MATHWIKI-METHOD-CLUSTER-304_分块矩阵方程]]
- [[MATHWIKI-METHOD-CLUSTER-463_逆矩阵定义]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-010_伴随矩阵与反对称结构]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-049
- LA-050
- LA-055

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
