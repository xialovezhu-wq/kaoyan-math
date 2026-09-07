---
wiki_id: SRC-WQ-LA-105
type: source_summary
title: "LA-105 特征空间内换基判定P矩阵"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-105_强化例题7.3.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-744_强化例题7.3.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-105_强化例题7.3.md"
visual_ids:
  - "MN4-GS-CH01-744"
  - "VIS-LA-105"
wrongnet_refs:
  - "LA-105"
knowledge:
  - "相似矩阵"
  - "特征值与特征向量"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "换基表示"
  - "特征分解"
  - "列向量线性表示"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确"
  - "MATHWIKI-KNOWLEDGE-016_特征值与特征向量"
  - "MATHWIKI-KNOWLEDGE-040_相似矩阵"
  - "MATHWIKI-METHOD-CLUSTER-023_特征分解"
  - "MATHWIKI-METHOD-CLUSTER-145_列向量线性表示"
  - "MATHWIKI-METHOD-CLUSTER-231_换基表示"
  - "MATHWIKI-LA-METHOD-005_相似对角化判定与特征向量换基"
  - "MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线"
  - "MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线"
status: indexed
last_updated: "2026-07-25"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-744/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-105/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-744/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-105/solution_01.png"
reference_asset_refs: []
related_wrongnet_refs: []
aggregate_edge_policy: "block_strong_edges"
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "5a63b80dc3ce1f4b5c0595efb039752386358cb424f2ceedd86b4d1d01c2cc55"
evidence_status: "pending_user_confirmation"
---

# LA-105 特征空间内换基判定P矩阵

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-105_强化例题7.3.md`
- wrongnet ID：`LA-105`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 相似理论 |
| 题型 | 特征向量矩阵列匹配 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 相似矩阵
- 特征值与特征向量

### 错因

- 个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。

### 方法

- 换基表示
- 特征分解
- 列向量线性表示

### 陷阱

- 不同特征值的特征向量不能混合成同一列
- 同一特征空间内线性组合仍属于原特征值
- \(P\) 的列位置必须和对角元位置对应

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先逐列标注候选 P 的每一列应对应哪个特征值。 |
| missed_action | 旧卡未记录用户实际漏点；复做时重点确认是否漏掉“逐列标注候选 P 的每一列应对应哪个特征值。”这一步。 |
| related_method_card_id | L08-001 |
| next_reminder | 看到 P^{-1}AP=Lambda，先逐列查特征空间，不能混用不同特征值的特征向量。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确]]
- [[MATHWIKI-KNOWLEDGE-016_特征值与特征向量]]
- [[MATHWIKI-KNOWLEDGE-040_相似矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-023_特征分解]]
- [[MATHWIKI-METHOD-CLUSTER-145_列向量线性表示]]
- [[MATHWIKI-METHOD-CLUSTER-231_换基表示]]

### 深度编译页

- [[MATHWIKI-LA-METHOD-005_相似对角化判定与特征向量换基]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- [[MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线]]

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

- A. \([\alpha_1,-2\alpha_2,\alpha_3]\)
- B. \([\alpha_1,\alpha_2+\alpha_3,\alpha_2-2\alpha_3]\)
- C. \([\alpha_1,\alpha_3,\alpha_2]\)
- D. \([\alpha_1+\alpha_2,\alpha_1-\alpha_2,\alpha_3]\)

- 用户个人断点仍受证据门禁约束。
- 当前正式 strong edge 为零。
