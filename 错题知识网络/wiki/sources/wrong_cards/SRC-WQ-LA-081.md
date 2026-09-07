---
wiki_id: SRC-WQ-LA-081
type: source_summary
title: "LA-081 强化例题5.2-2"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-081_强化例题5.2-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-081"
knowledge:
  - "线性方程组"
  - "矩阵秩"
  - "矩阵运算"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "反对称矩阵标准形"
  - "分块矩阵方程"
  - "矩阵秩判定解性"
  - "齐次与非齐次方程组判定"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-014_矩阵运算"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-033_线性方程组"
  - "MATHWIKI-METHOD-CLUSTER-1237_矩阵秩判定解性"
  - "MATHWIKI-METHOD-CLUSTER-1430_齐次与非齐次方程组判定"
  - "MATHWIKI-METHOD-CLUSTER-304_分块矩阵方程"
  - "MATHWIKI-METHOD-CLUSTER-786_反对称矩阵标准形"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-017_线性方程组零空间与秩约束入口链"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# LA-081 强化例题5.2-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-081_强化例题5.2-2.md`
- wrongnet ID：`LA-081`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 线性方程组 |
| 题型 | 反对称矩阵与分块线性方程组解性判断 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 线性方程组
- 矩阵秩
- 矩阵运算

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 反对称矩阵标准形
- 分块矩阵方程
- 矩阵秩判定解性
- 齐次与非齐次方程组判定

### 陷阱

- \(a_{ij}+a_{ji}=0\) 要先转化为 \(A^{\mathrm T}=-A\)
- 二阶实反对称矩阵可写成 \(\begin{pmatrix}0&a\\-a&0\end{pmatrix}\)
- \(A\alpha\) 非零说明 \(A\) 不为零矩阵，进而 \(P=[\alpha,A\alpha]\) 可逆

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先由 \(A^{\mathrm T}=-A\) 写出二阶反对称矩阵标准形 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是直接看分块方程组，漏掉反对称结构先保证 \(P\) 可逆 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到二阶反对称矩阵，先写标准形并判断 \(P=[\alpha,A\alpha]\) 可逆，再看方程组。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-033_线性方程组]]
- [[MATHWIKI-METHOD-CLUSTER-1237_矩阵秩判定解性]]
- [[MATHWIKI-METHOD-CLUSTER-1430_齐次与非齐次方程组判定]]
- [[MATHWIKI-METHOD-CLUSTER-304_分块矩阵方程]]
- [[MATHWIKI-METHOD-CLUSTER-786_反对称矩阵标准形]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-017_线性方程组零空间与秩约束入口链]]
- [[MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-078
- LA-079
- LA-086

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
