---
wiki_id: SRC-WQ-LA-109
type: source_summary
title: "LA-109 特征空间内换基不改对角元"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-109_强化例题8.1-2.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-746_线代强化例题8.1.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-109_强化例题8.1-2.md"
visual_ids:
  - "MN4-GS-CH01-746"
  - "VIS-LA-109"
wrongnet_refs:
  - "LA-109"
knowledge:
  - "相似矩阵"
  - "特征值与特征向量"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "相似对角化"
  - "特征向量矩阵"
  - "特征空间换基"
  - "对角元顺序匹配"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确"
  - "MATHWIKI-KNOWLEDGE-016_特征值与特征向量"
  - "MATHWIKI-KNOWLEDGE-040_相似矩阵"
  - "MATHWIKI-METHOD-CLUSTER-100_相似对角化"
  - "MATHWIKI-METHOD-CLUSTER-1188_特征向量矩阵"
  - "MATHWIKI-METHOD-CLUSTER-1193_特征空间换基"
  - "MATHWIKI-METHOD-CLUSTER-935_对角元顺序匹配"
  - "MATHWIKI-LA-METHOD-005_相似对角化判定与特征向量换基"
  - "MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线"
status: indexed
last_updated: "2026-07-25"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-746/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-109/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-746/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-109/solution_01.png"
reference_asset_refs: []
related_wrongnet_refs: []
aggregate_edge_policy: "block_strong_edges"
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "59cbda63061fd4cfec11b4dfa1dbce89d19994aecaef83a261319f01b1ed7d0c"
evidence_status: "pending_user_confirmation"
---

# LA-109 特征空间内换基不改对角元

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-109_强化例题8.1-2.md`
- wrongnet ID：`LA-109`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 相似理论 |
| 题型 | 相似对角化中特征向量矩阵换基 |
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

- 相似对角化
- 特征向量矩阵
- 特征空间换基
- 对角元顺序匹配

### 陷阱

- 同一特征值对应的特征向量线性组合仍属于该特征空间
- 不要把特征空间内换基误判为对角元重新排序
- 相似对角化中第 i 列特征向量必须对应第 i 个对角元

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先判断 Q 的每一列仍属于哪个特征空间。 |
| missed_action | 旧卡未记录用户实际漏点；复做时重点确认是否漏掉“判断 Q 的每一列仍属于哪个特征空间。”这一步。 |
| related_method_card_id | L08-001 |
| next_reminder | 看到特征向量矩阵换列或列组合，先查新列所属特征空间，再决定对角元顺序。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确]]
- [[MATHWIKI-KNOWLEDGE-016_特征值与特征向量]]
- [[MATHWIKI-KNOWLEDGE-040_相似矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-100_相似对角化]]
- [[MATHWIKI-METHOD-CLUSTER-1188_特征向量矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-1193_特征空间换基]]
- [[MATHWIKI-METHOD-CLUSTER-935_对角元顺序匹配]]

### 深度编译页

- [[MATHWIKI-LA-METHOD-005_相似对角化判定与特征向量换基]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]

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

- 仅投影经核验的客观内容。

- 用户个人断点仍受证据门禁约束。
- 当前正式 strong edge 为零。
