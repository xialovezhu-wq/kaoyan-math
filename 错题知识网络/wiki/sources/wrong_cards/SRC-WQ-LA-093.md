---
wiki_id: SRC-WQ-LA-093
type: source_summary
title: "LA-093 三向量相关两两无关参数"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-093_强化例题6.2.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-732_强化例题6.2.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-093_强化例题6.2.md"
visual_ids:
  - "MN4-GS-CH01-732"
  - "VIS-LA-093"
wrongnet_refs:
  - "LA-093"
knowledge:
  - "向量组线性相关"
  - "向量组线性无关"
  - "矩阵秩"
  - "参数分类讨论"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "矩阵秩判断"
  - "参数分类讨论"
  - "两两线性无关检查"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-008_B6-CLOSE"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-047_参数分类讨论"
  - "MATHWIKI-KNOWLEDGE-090_向量组线性无关"
  - "MATHWIKI-KNOWLEDGE-101_向量组线性相关"
  - "MATHWIKI-METHOD-CLUSTER-040_参数分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断"
  - "MATHWIKI-METHOD-CLUSTER-526_两两线性无关检查"
  - "MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "652b199057c878d88faa16edc597aa3e4b528e893f3d5a83373bc65d22b670e5"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-732/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-093/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-732/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-093/solution_01.png"
reference_asset_refs: []
aggregate_edge_policy: "block_strong_edges"
evidence_status: "pending_user_confirmation"
---

# LA-093 三向量相关两两无关参数

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-093_强化例题6.2.md`
- wrongnet ID：`LA-093`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 向量组 |
| 题型 | 向量组线性相关与两两无关判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 向量组线性相关
- 向量组线性无关
- 矩阵秩
- 参数分类讨论

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 矩阵秩判断
- 参数分类讨论
- 两两线性无关检查

### 陷阱

- \(r(\alpha_1,\alpha_2,\alpha_3)<3\) 只给三向量相关的候选参数。
- 题目还要求任意两个向量线性无关，必须把候选参数代回逐对检查。
- \(a=1\) 会导致 \(\alpha_1\) 与 \(\alpha_3\) 线性相关，应排除。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B6-CLOSE |
| expected_first_action | 先用 \(r(\alpha_1,\alpha_2,\alpha_3)<3\) 找候选参数，再逐对检查 \(r(\alpha_i,\alpha_j)=2\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是只满足三向量相关，漏查任意两个均线性无关这一附加条件 |
| related_method_card_id | L06-002 |
| next_reminder | 看到“整体相关但两两无关”，先找候选，再逐对回代检查附加条件。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-008_B6-CLOSE]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-047_参数分类讨论]]
- [[MATHWIKI-KNOWLEDGE-090_向量组线性无关]]
- [[MATHWIKI-KNOWLEDGE-101_向量组线性相关]]
- [[MATHWIKI-METHOD-CLUSTER-040_参数分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断]]
- [[MATHWIKI-METHOD-CLUSTER-526_两两线性无关检查]]

### 深度编译页

- [[MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示]]
- [[MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线]]

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
