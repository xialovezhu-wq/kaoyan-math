---
wiki_id: SRC-WQ-LA-092
type: source_summary
title: "LA-092 两组向量张成空间交"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-092_强化例题6.1.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-731_强化例题6.1.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-092_强化例题6.1.md"
visual_ids:
  - "MN4-GS-CH01-731"
  - "VIS-LA-092"
wrongnet_refs:
  - "LA-092"
knowledge:
  - "向量组线性相关"
  - "矩阵秩"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "线性表示"
  - "齐次方程组基础解系"
  - "矩阵秩判断"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-101_向量组线性相关"
  - "MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断"
  - "MATHWIKI-METHOD-CLUSTER-104_齐次方程组基础解系"
  - "MATHWIKI-METHOD-CLUSTER-177_线性表示"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: "2026-07-25"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-731/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-092/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-731/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-092/solution_01.png"
reference_asset_refs: []
related_wrongnet_refs: []
aggregate_edge_policy: "block_strong_edges"
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "410d3b4ce8153ceb6a938c1e7ba761641c1fc73753899a8ac38a5959f6a22a6b"
evidence_status: "pending_user_confirmation"
---

# LA-092 两组向量张成空间交

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-092_强化例题6.1.md`
- wrongnet ID：`LA-092`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 向量组 |
| 题型 | 两个张成空间的公共向量 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 向量组线性相关
- 矩阵秩

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 线性表示
- 齐次方程组基础解系
- 矩阵秩判断

### 陷阱

- “既可由这组表示，也可由那组表示”要转成同一个向量的两种线性组合相等。
- 求公共表示时不要只看某个候选向量是否在一组内，要解四个系数的齐次关系。
- 系数关系只确定一维公共方向，所以答案允许任意倍数 \(k\)。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 \(k_1\alpha_1+k_2\alpha_2=k_3\beta_1+k_4\beta_2\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是直接猜公共向量，没有先把两种表示式联立 |
| related_method_card_id | L06-001 |
| next_reminder | 看到张成空间交，先写同一向量的两种线性表示相等，再解系数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-101_向量组线性相关]]
- [[MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断]]
- [[MATHWIKI-METHOD-CLUSTER-104_齐次方程组基础解系]]
- [[MATHWIKI-METHOD-CLUSTER-177_线性表示]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
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

- 仅投影经核验的客观内容。

- 用户个人断点仍受证据门禁约束。
- 当前正式 strong edge 为零。
