---
wiki_id: SRC-WQ-LA-106
type: source_summary
title: "LA-106 矩阵乘法按列读特征向量"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-106_强化例题7.4.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-745_强化例题7.4.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-106_强化例题7.4.md"
visual_ids:
  - "MN4-GS-CH01-745"
  - "VIS-LA-106"
wrongnet_refs:
  - "LA-106"
knowledge:
  - "特征值与特征向量"
  - "矩阵运算"
  - "向量组线性无关"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "矩阵方程按列拆"
  - "列向量线性表示"
  - "矩阵初等变换"
  - "特征分解"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确"
  - "MATHWIKI-KNOWLEDGE-014_矩阵运算"
  - "MATHWIKI-KNOWLEDGE-016_特征值与特征向量"
  - "MATHWIKI-KNOWLEDGE-090_向量组线性无关"
  - "MATHWIKI-METHOD-CLUSTER-023_特征分解"
  - "MATHWIKI-METHOD-CLUSTER-101_矩阵初等变换"
  - "MATHWIKI-METHOD-CLUSTER-145_列向量线性表示"
  - "MATHWIKI-METHOD-CLUSTER-171_矩阵方程按列拆"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-LA-METHOD-012_矩阵方程按列拆与解空间参数化"
  - "MATHWIKI-LA-METHOD-015_矩阵多项式与特征值映射"
  - "MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "65cdc1fc849c7d300d4db0de84b08f7726113df81f65e5089df85e7e6e1c01b1"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-745/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-106/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
aggregate_edge_policy: "block_strong_edges"
evidence_status: "pending_user_confirmation"
---

# LA-106 矩阵乘法按列读特征向量

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-106_强化例题7.4.md`
- wrongnet ID：`LA-106`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 特征值与特征向量 |
| 题型 | 矩阵乘法按列提取特征空间 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 特征值与特征向量
- 矩阵运算
- 向量组线性无关

### 错因

- 个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。

### 方法

- 矩阵方程按列拆
- 列向量线性表示
- 矩阵初等变换
- 特征分解

### 陷阱

- \(AB=-2B\) 要按 B 的列向量逐列读
- \(CA^{\mathsf T}=2C\) 要先转置再按列读
- 需要检查 \(B\) 和 \(C^{\mathsf T}\) 提供的特征向量个数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把 B 拆成列向量，并把 CA^T=2C 转置成 AC^T=2C^T。 |
| missed_action | 旧卡未记录用户实际漏点；复做时重点确认是否漏掉“把 B 拆成列向量，并把 CA^T=2C 转置成 AC^T=2C^T。”这一步。 |
| related_method_card_id | L07-008 |
| next_reminder | 看到 AB=lambda B，先按列读 B；看到 CA^T=lambda C，先转置再按列读。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-016_特征值与特征向量]]
- [[MATHWIKI-KNOWLEDGE-090_向量组线性无关]]
- [[MATHWIKI-METHOD-CLUSTER-023_特征分解]]
- [[MATHWIKI-METHOD-CLUSTER-101_矩阵初等变换]]
- [[MATHWIKI-METHOD-CLUSTER-145_列向量线性表示]]
- [[MATHWIKI-METHOD-CLUSTER-171_矩阵方程按列拆]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-LA-METHOD-012_矩阵方程按列拆与解空间参数化]]
- [[MATHWIKI-LA-METHOD-015_矩阵多项式与特征值映射]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- [[MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线]]
- [[MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

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

## 关联卡片

- 暂无强边。

## B41 客观核验与证据边界

## 客观核验修正

- 题中矩阵必须转录为

$$
B=\begin{pmatrix}1&2&3\\-1&1&0\\2&-1&1\end{pmatrix},\qquad
C=\begin{pmatrix}1&-2&1\\-2&4&-2\\-1&2&-1\end{pmatrix}.
$$

- \(-2\) 的特征子空间可取基 \((1,-1,2)^{\mathsf T},(2,1,-1)^{\mathsf T}\)；\(2\) 的特征子空间可取基 \((1,-2,1)^{\mathsf T}\)。
- \(-2\) 特征子空间中的两个系数只要求不能同时为零，不得误写成两个系数都非零。
- 原题图和解析图资产保持字节不变。

- 用户个人断点仍受证据门禁约束。
- 当前正式 strong edge 为零。
