---
wiki_id: SRC-WQ-LA-089
type: source_summary
title: "LA-089 矩阵多项式下同解变形"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-089_强化例题5.6.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-728_强化例题5.6.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-089_强化例题5.6.md"
visual_ids:
  - "MN4-GS-CH01-728"
  - "VIS-LA-089"
wrongnet_refs:
  - "LA-089"
knowledge:
  - "线性方程组"
  - "矩阵运算"
  - "矩阵秩"
  - "逆矩阵"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "同解变形"
  - "可逆性检验"
  - "矩阵多项式"
  - "特例反证"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-014_矩阵运算"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-033_线性方程组"
  - "MATHWIKI-KNOWLEDGE-077_逆矩阵"
  - "MATHWIKI-METHOD-CLUSTER-1178_特例反证"
  - "MATHWIKI-METHOD-CLUSTER-212_可逆性检验"
  - "MATHWIKI-METHOD-CLUSTER-213_同解变形"
  - "MATHWIKI-METHOD-CLUSTER-437_矩阵多项式"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-016_线性方程组同解与公共解判定"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: "2026-07-25"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-728/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-089/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-728/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-089/solution_01.png"
reference_asset_refs: []
related_wrongnet_refs: []
aggregate_edge_policy: "block_strong_edges"
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "30e9ebdf5aeb73d982c89a0ffae97b0f972d5e59fcf02ebefddbbacb3bb954fc"
evidence_status: "pending_user_confirmation"
method_registry_followup_hold:
  enabled: true
  method_ids:
  - L05-006
  registry_write_authorized: false
  self_contained_first_action_in_source: true
  depends_on_registry_text_for_this_postimage: false
---

# LA-089 矩阵多项式下同解变形

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-089_强化例题5.6.md`
- wrongnet ID：`LA-089`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 线性方程组 |
| 题型 | 齐次方程组同解判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 线性方程组
- 矩阵运算
- 矩阵秩
- 逆矩阵

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 同解变形
- 可逆性检验
- 矩阵多项式
- 特例反证

### 陷阱

- \(A^2-A=3E\) 可转化出 \((A-2E)(A+E)=E\)，相关因子可逆
- 齐次方程组同解可以通过可逆分块变换判定
- 判断“不同解”时可取 \(B=-A\) 构造特例

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先由 \(A^2-A=3E\) 整理出相关矩阵的可逆性 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是逐个方程组硬算通解，没有先找可逆变换链 |
| related_method_card_id | L07-005 |
| next_reminder | 看到同解判断和矩阵多项式，先找可逆因子，再用可逆变换保解集。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-033_线性方程组]]
- [[MATHWIKI-KNOWLEDGE-077_逆矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-1178_特例反证]]
- [[MATHWIKI-METHOD-CLUSTER-212_可逆性检验]]
- [[MATHWIKI-METHOD-CLUSTER-213_同解变形]]
- [[MATHWIKI-METHOD-CLUSTER-437_矩阵多项式]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-016_线性方程组同解与公共解判定]]
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

- A. \(\begin{pmatrix}A-B\\A+AB\end{pmatrix}x=0\)
- B. \(\begin{pmatrix}A+B\\A+AB-B\end{pmatrix}x=0\)
- C. \(\begin{pmatrix}A-B\\2A+B\end{pmatrix}x=0\)
- D. \(\begin{pmatrix}A+B\\BA+B^2\end{pmatrix}x=0\)

- 用户个人断点仍受证据门禁约束。
- 当前正式 strong edge 为零。
