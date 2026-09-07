---
wiki_id: SRC-WQ-LA-091
type: source_summary
title: "LA-091 增广矩阵秩判同解差异"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-091_强化例题5.8.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-730_强化例题5.8.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-091_强化例题5.8.md"
visual_ids:
  - "MN4-GS-CH01-730"
  - "VIS-LA-091"
wrongnet_refs:
  - "LA-091"
knowledge:
  - "线性方程组"
  - "矩阵秩"
  - "参数分类讨论"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "增广矩阵行变换"
  - "矩阵秩判断"
  - "同解变形"
  - "参数分类讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-033_线性方程组"
  - "MATHWIKI-KNOWLEDGE-047_参数分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-040_参数分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断"
  - "MATHWIKI-METHOD-CLUSTER-213_同解变形"
  - "MATHWIKI-METHOD-CLUSTER-346_增广矩阵行变换"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-016_线性方程组同解与公共解判定"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "958832c58bf2e107a0cb76da8732973d506b53d6135822e29b6419601b1a73ec"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-730/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-091/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-730/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-091/solution_01.png"
reference_asset_refs: []
aggregate_edge_policy: "block_strong_edges"
evidence_status: "pending_user_confirmation"
---

# LA-091 增广矩阵秩判同解差异

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-091_强化例题5.8.md`
- wrongnet ID：`LA-091`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 线性方程组 |
| 题型 | 线性方程组解集包含与参数判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 线性方程组
- 矩阵秩
- 参数分类讨论

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 增广矩阵行变换
- 矩阵秩判断
- 同解变形
- 参数分类讨论

### 陷阱

- 证明 \(Ax=\alpha\) 的解也是 \(Bx=\beta\) 的解，应比较上下拼接增广矩阵的秩，而不是分别求两个通解。
- 若两个方程组有不同解，必须让 \(Bx=\beta\) 的相容秩条件和 \(Ax=\alpha\) 的秩条件出现差异。
- \(a=1\) 时 \(B\) 的秩下降，导致两方程组不再同解。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 \((A,\alpha)\)、\((B,\beta)\) 以及上下拼接增广矩阵的秩关系 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是分别求通解导致计算膨胀，没先用增广矩阵秩判断解集包含 |
| related_method_card_id | L05-007 |
| next_reminder | 看到非齐次方程组解集比较，先拼增广矩阵看秩，再讨论参数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-033_线性方程组]]
- [[MATHWIKI-KNOWLEDGE-047_参数分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-040_参数分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断]]
- [[MATHWIKI-METHOD-CLUSTER-213_同解变形]]
- [[MATHWIKI-METHOD-CLUSTER-346_增广矩阵行变换]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-016_线性方程组同解与公共解判定]]
- [[MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线]]
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

- 仅投影经核验的客观内容。

- 用户个人断点仍受证据门禁约束。
- 当前正式 strong edge 为零。
