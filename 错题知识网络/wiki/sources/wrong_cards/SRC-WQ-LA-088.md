---
wiki_id: SRC-WQ-LA-088
type: source_summary
title: "LA-088 秩差推出公共非零解"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-088_强化例题5.5（2025年数2真题选择题第十题）.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-727_强化例题5.5（2025年数2真题选择题第十题）.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-088_强化例题5.5（2025年数2真题选择题第十题）.md"
visual_ids:
  - "MN4-GS-CH01-727"
  - "VIS-LA-088"
wrongnet_refs:
  - "LA-088"
knowledge:
  - "线性方程组"
  - "矩阵秩"
  - "矩阵运算"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "矩阵秩不等式"
  - "齐次方程组公共非零解"
  - "分块矩阵秩判断"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-014_矩阵运算"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-033_线性方程组"
  - "MATHWIKI-METHOD-CLUSTER-127_矩阵秩不等式"
  - "MATHWIKI-METHOD-CLUSTER-1431_齐次方程组公共非零解"
  - "MATHWIKI-METHOD-CLUSTER-143_分块矩阵秩判断"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-016_线性方程组同解与公共解判定"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: "2026-07-25"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-727/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-088/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-727/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-088/solution_01.png"
reference_asset_refs: []
related_wrongnet_refs: []
aggregate_edge_policy: "block_strong_edges"
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "b11567cb14b12e857938c2e7b87df05bfea59a4c5ba883ec36917e34ee90bfcb"
evidence_status: "pending_user_confirmation"
method_registry_followup_hold:
  enabled: true
  method_ids:
  - L05-004
  registry_write_authorized: false
  self_contained_first_action_in_source: true
  depends_on_registry_text_for_this_postimage: false
---

# LA-088 秩差推出公共非零解

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-088_强化例题5.5（2025年数2真题选择题第十题）.md`
- wrongnet ID：`LA-088`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 线性方程组 |
| 题型 | 齐次方程组公共非零解判定 |
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

- 矩阵秩不等式
- 齐次方程组公共非零解
- 分块矩阵秩判断

### 陷阱

- 三阶方阵有 \(|AB|=|BA|\)，不能让 \(r(AB)=3,r(BA)=2\) 同时成立
- 公共非零解可转成上下拼接矩阵的齐次方程组
- 上下拼接矩阵秩小于列数即可推出非零解

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先由秩差压缩 \(r(BA)\)，再把公共非零解写成上下拼接矩阵判秩 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是分别看两个方程组，忘记公共非零解要拼接成一个方程组 |
| related_method_card_id | L05-004 |
| next_reminder | 看到公共非零解，先拼接矩阵，再比较秩和未知数个数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-033_线性方程组]]
- [[MATHWIKI-METHOD-CLUSTER-127_矩阵秩不等式]]
- [[MATHWIKI-METHOD-CLUSTER-1431_齐次方程组公共非零解]]
- [[MATHWIKI-METHOD-CLUSTER-143_分块矩阵秩判断]]

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

- A. 方程组 \((A+B)x=0\) 只有零解
- B. 方程组 \(Ax=0\) 与方程组 \(Bx=0\) 均只有零解
- C. 方程组 \(Ax=0\) 与方程组 \(Bx=0\) 没有公共非零解
- D. 方程组 \(ABAx=0\) 与方程组 \(BABx=0\) 有公共非零解

## 客观核验修正

- 三个未知量的齐次方程组存在非零解时，系数矩阵的秩必须满足 \(r<3\)，不得写成 \(r=3\)。
- 本题由乘积秩与行列式约束推出所需拼接矩阵秩严格小于 3。

- 用户个人断点仍受证据门禁约束。
- 当前正式 strong edge 为零。
