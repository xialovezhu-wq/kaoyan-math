---
wiki_id: SRC-WQ-LA-090
type: source_summary
title: "LA-090 A2与A齐次方程不同解"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-090_强化例题5.7-2.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-729_强化例题5.7.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-090_强化例题5.7-2.md"
visual_ids:
  - "MN4-GS-CH01-729"
  - "VIS-LA-090"
wrongnet_refs:
  - "LA-090"
knowledge:
  - "线性方程组"
  - "矩阵秩"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "齐次方程组基础解系"
  - "可逆性检验"
  - "行列式性质"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-033_线性方程组"
  - "MATHWIKI-METHOD-CLUSTER-104_齐次方程组基础解系"
  - "MATHWIKI-METHOD-CLUSTER-179_行列式性质"
  - "MATHWIKI-METHOD-CLUSTER-212_可逆性检验"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "b1785b6ac6eaaefe6ad8ee497521a9396f1a78dfde9a41834030e3f66548302d"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-729/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-090/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-729/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-090/solution_01.png"
reference_asset_refs: []
aggregate_edge_policy: "block_strong_edges"
evidence_status: "pending_user_confirmation"
---

# LA-090 A2与A齐次方程不同解

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-090_强化例题5.7-2.md`
- wrongnet ID：`LA-090`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 线性方程组 |
| 题型 | 齐次方程组解空间比较 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 线性方程组
- 矩阵秩

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 齐次方程组基础解系
- 可逆性检验
- 行列式性质

### 陷阱

- 若 \(A\) 可逆，则两个方程组都只有零解，解一定相同。
- 题目只问 \(a-b\)，由“解不同”先得到 \(|A|=0\) 即可推出参数关系。
- 不要先展开 \(A^2\)，计算量会被放大。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先判断 \(A\) 是否可逆，再由解不同推出 \(|A|=0\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是直接展开 \(A^2\)，没有先利用可逆性和核空间包含关系 |
| related_method_card_id | L04-007 |
| next_reminder | 看到 \(A^2x=0\) 和 \(Ax=0\) 比较，先查可逆性和核空间包含，不要先平方矩阵。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-033_线性方程组]]
- [[MATHWIKI-METHOD-CLUSTER-104_齐次方程组基础解系]]
- [[MATHWIKI-METHOD-CLUSTER-179_行列式性质]]
- [[MATHWIKI-METHOD-CLUSTER-212_可逆性检验]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示]]
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

## 客观核验修正

- \(A\)：题中三阶方阵；\(N(A)\)：\(A\) 的零空间。
- 恒有 \(N(A)\subseteq N(A^2)\)。若 \(N(A^2)\ne N(A)\)，则 \(A\) 必为奇异矩阵；本题只能使用这个必要方向。
- 逆命题不成立。取 \(A=\operatorname{diag}(1,0,0)\)，则 \(A\) 奇异但 \(A^2=A\)，所以两个零空间相同。
- 原 `solution_01.png` 保持字节不变；上述文字是对解析图错误逆命题的显式勘误。

- 用户个人断点仍受证据门禁约束。
- 当前正式 strong edge 为零。
