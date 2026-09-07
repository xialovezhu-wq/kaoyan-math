---
wiki_id: SRC-WQ-LA-097
type: source_summary
title: "LA-097 表示关系转转置核包含"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-097_2021年第九题.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-736_2021年第九题.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-097_2021年第九题.md"
visual_ids:
  - "MN4-GS-CH01-736"
  - "VIS-LA-097"
wrongnet_refs:
  - "LA-097"
knowledge:
  - "列向量线性表示"
  - "列向量关系转齐次解"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "线性表示"
  - "矩阵关系转置"
  - "齐次方程组核空间包含"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确"
  - "MATHWIKI-KNOWLEDGE-315_列向量关系转齐次解"
  - "MATHWIKI-KNOWLEDGE-316_列向量线性表示"
  - "MATHWIKI-METHOD-CLUSTER-1231_矩阵关系转置"
  - "MATHWIKI-METHOD-CLUSTER-1433_齐次方程组核空间包含"
  - "MATHWIKI-METHOD-CLUSTER-177_线性表示"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: "2026-07-25"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-736/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-097/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-736/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-097/solution_01.png"
reference_asset_refs: []
related_wrongnet_refs: []
aggregate_edge_policy: "block_strong_edges"
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "914046132835fc41b07a508d4db2740856451d647c2e6bce5fff7bef0cb26031"
evidence_status: "pending_user_confirmation"
---

# LA-097 表示关系转转置核包含

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-097_2021年第九题.md`
- wrongnet ID：`LA-097`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 向量组 |
| 题型 | 向量组表示推出齐次方程组核包含 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 列向量线性表示
- 列向量关系转齐次解

### 错因

- 个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。

### 方法

- 线性表示
- 矩阵关系转置
- 齐次方程组核空间包含

### 陷阱

- \(A=BC\) 不推出 \(Ax=0\) 与 \(Bx=0\) 同解。
- 转置后 \(A^{\mathsf T}=C^{\mathsf T}B^{\mathsf T}\)，所以 \(B^{\mathsf T}x=0\) 能推出 \(…
- 不要把 \(A=BC\) 误读成 \(A\) 与 \(B\) 可逆等价。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写矩阵关系 A=BC，再两边转置。 |
| missed_action | 旧卡未记录用户实际漏点；复做时重点确认是否漏掉“写矩阵关系 A=BC，再两边转置。”这一步。 |
| related_method_card_id | L06-004 |
| next_reminder | 看到向量组可由另一组表示，先写 A=BC，再转置判断核包含方向。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确]]
- [[MATHWIKI-KNOWLEDGE-315_列向量关系转齐次解]]
- [[MATHWIKI-KNOWLEDGE-316_列向量线性表示]]
- [[MATHWIKI-METHOD-CLUSTER-1231_矩阵关系转置]]
- [[MATHWIKI-METHOD-CLUSTER-1433_齐次方程组核空间包含]]
- [[MATHWIKI-METHOD-CLUSTER-177_线性表示]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示]]
- [[MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线]]
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

## B41 客观核验与证据边界

## 原题选项（客观复原）

- A. \(Ax=0\) 的解均为 \(Bx=0\) 的解
- B. \(A^{\mathsf T}x=0\) 的解均为 \(B^{\mathsf T}x=0\) 的解
- C. \(Bx=0\) 的解均为 \(Ax=0\) 的解
- D. \(B^{\mathsf T}x=0\) 的解均为 \(A^{\mathsf T}x=0\) 的解

- 用户个人断点仍受证据门禁约束。
- 当前正式 strong edge 为零。
