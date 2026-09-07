---
wiki_id: SRC-WQ-LA-087
type: source_summary
title: "LA-087 重根特征值反求非齐次向量"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-087_强化例题5、4.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-726_强化例题5、4.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-087_强化例题5、4.md"
visual_ids:
  - "MN4-GS-CH01-726"
  - "VIS-LA-087"
wrongnet_refs:
  - "LA-087"
knowledge:
  - "线性方程组"
  - "特征值与特征向量"
  - "矩阵秩"
  - "非齐次线性方程组通解"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "特征多项式"
  - "特征向量求解"
  - "非齐次线性方程组通解"
  - "相容条件检查"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-016_特征值与特征向量"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-033_线性方程组"
  - "MATHWIKI-KNOWLEDGE-432_非齐次线性方程组通解"
  - "MATHWIKI-METHOD-CLUSTER-1187_特征向量求解"
  - "MATHWIKI-METHOD-CLUSTER-1226_相容条件检查"
  - "MATHWIKI-METHOD-CLUSTER-265_非齐次线性方程组通解"
  - "MATHWIKI-METHOD-CLUSTER-430_特征多项式"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-LA-METHOD-016_线性方程组同解与公共解判定"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "9f535a72a51140f9460edc522fbc35cb62c10dbdcf3df1c7fb361cdef311150b"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-726/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-087/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-726/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-087/solution_01.png"
reference_asset_refs: []
aggregate_edge_policy: "block_strong_edges"
evidence_status: "pending_user_confirmation"
---

# LA-087 重根特征值反求非齐次向量

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-087_强化例题5、4.md`
- wrongnet ID：`LA-087`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 线性方程组 |
| 题型 | 特征值条件下的非齐次方程组 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 线性方程组
- 特征值与特征向量
- 矩阵秩
- 非齐次线性方程组通解

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 特征多项式
- 特征向量求解
- 非齐次线性方程组通解
- 相容条件检查

### 陷阱

- 由 \(A^2\alpha=A(\alpha+\beta)\) 和 \(A^2\alpha=\alpha+2\beta\) 可推出 \(A\beta=\bet…
- 解 \((A-E)\alpha=\beta\) 前必须先保证右端 \(\beta\) 落在列空间中
- \(\beta\ne0\) 给出 \(2c_3-c_2-c_1\ne0\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先由 \(1\) 是重根求参数，再把 \(A^2\alpha\) 改写成 \(A(A\alpha)\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是硬解 \(\alpha,\beta\)，没有先识别 \(\beta\) 是特征向量 |
| related_method_card_id | L07-008 |
| next_reminder | 看到链式向量方程，先把高次作用拆成连续作用，再识别中间向量的身份。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-016_特征值与特征向量]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-033_线性方程组]]
- [[MATHWIKI-KNOWLEDGE-432_非齐次线性方程组通解]]
- [[MATHWIKI-METHOD-CLUSTER-1187_特征向量求解]]
- [[MATHWIKI-METHOD-CLUSTER-1226_相容条件检查]]
- [[MATHWIKI-METHOD-CLUSTER-265_非齐次线性方程组通解]]
- [[MATHWIKI-METHOD-CLUSTER-430_特征多项式]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
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

## 客观核验修正

- \(A\)：题中三阶矩阵；\(N(A-I)\)：\(A-I\) 的零空间。
- \(N(A-I)\) 是二维空间，不得压成一维。可取两个线性无关方向 \((-1,1,0)^{\mathsf T}\) 与 \((2,0,1)^{\mathsf T}\)。
- \(\operatorname{Range}(A-I)=\operatorname{span}\{(1,1,1)^{\mathsf T}\}\)。
- 非齐次条件要求 \(\beta\) 位于上述值域且 \(\beta\ne0\)；应先保留完整二维齐次解空间，再用相容性确定仿射解族。

- 用户个人断点仍受证据门禁约束。
- 当前正式 strong edge 为零。
