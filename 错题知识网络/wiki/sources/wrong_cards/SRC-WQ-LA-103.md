---
wiki_id: SRC-WQ-LA-103
type: source_summary
title: "LA-103 相似变换传递特征向量"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-103_强化例题7.2-2.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-742_强化例题7.2.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-103_强化例题7.2-2.md"
visual_ids:
  - "MN4-GS-CH01-742"
  - "VIS-LA-103"
wrongnet_refs:
  - "LA-103"
knowledge:
  - "特征值与特征向量"
  - "相似矩阵"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "特征分解"
  - "相似矩阵"
  - "特征向量变换"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确"
  - "MATHWIKI-KNOWLEDGE-016_特征值与特征向量"
  - "MATHWIKI-KNOWLEDGE-040_相似矩阵"
  - "MATHWIKI-METHOD-CLUSTER-023_特征分解"
  - "MATHWIKI-METHOD-CLUSTER-1185_特征向量变换"
  - "MATHWIKI-METHOD-CLUSTER-1221_相似矩阵"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-005_相似对角化判定与特征向量换基"
  - "MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "1898d5a3e83d6301abee2b12ba8b9aa3e62440d181f53938ecb9c83b837913e1"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-742/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-103/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-742/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-103/solution_01.png"
reference_asset_refs: []
aggregate_edge_policy: "block_strong_edges"
evidence_status: "pending_user_confirmation"
---

# LA-103 相似变换传递特征向量

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-103_强化例题7.2-2.md`
- wrongnet ID：`LA-103`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 特征值与特征向量 |
| 题型 | 相似变换下特征向量 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 特征值与特征向量
- 相似矩阵

### 错因

- 个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。

### 方法

- 特征分解
- 相似矩阵
- 特征向量变换

### 陷阱

- \(B=P^{-1}A^{100}P\) 与 \(A^{100}\) 相似，特征向量需要乘 \(P^{-1}\) 转换。
- \(B+E\) 与 \(B\) 有相同特征向量，但特征值整体加 1。
- \(A^{100}\) 不改变 \(A\) 的特征向量方向，只改变特征值。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先求 A 的特征向量，再左乘 P^{-1}。 |
| missed_action | 旧卡未记录用户实际漏点；复做时重点确认是否漏掉“求 A 的特征向量，再左乘 P^{-1}。”这一步。 |
| related_method_card_id | L08-009 |
| next_reminder | 看到 B=P^{-1}f(A)P，先求 A 的特征向量，再用 P^{-1} 传递坐标。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确]]
- [[MATHWIKI-KNOWLEDGE-016_特征值与特征向量]]
- [[MATHWIKI-KNOWLEDGE-040_相似矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-023_特征分解]]
- [[MATHWIKI-METHOD-CLUSTER-1185_特征向量变换]]
- [[MATHWIKI-METHOD-CLUSTER-1221_相似矩阵]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-005_相似对角化判定与特征向量换基]]
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

- 仅投影经核验的客观内容。

- 用户个人断点仍受证据门禁约束。
- 当前正式 strong edge 为零。
