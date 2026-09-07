---
wiki_id: SRC-WQ-LA-100
type: source_summary
title: "LA-100 向量组等价与表示式"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-100_2019年第23题.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-739_2019年第23题.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-100_2019年第23题.md"
visual_ids:
  - "MN4-GS-CH01-739"
  - "VIS-LA-100"
wrongnet_refs:
  - "LA-100"
knowledge:
  - "向量组线性相关"
  - "矩阵秩"
  - "参数分类讨论"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "向量组等价判定"
  - "线性表示"
  - "矩阵秩判断"
  - "参数分类讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-047_参数分类讨论"
  - "MATHWIKI-KNOWLEDGE-101_向量组线性相关"
  - "MATHWIKI-METHOD-CLUSTER-040_参数分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断"
  - "MATHWIKI-METHOD-CLUSTER-177_线性表示"
  - "MATHWIKI-METHOD-CLUSTER-337_向量组等价判定"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
review_batch: "MATHWIKI-REVIEW-088"
formal_projection_sha256: "ac9296b4b9a754bc5f8691a01eef822c3a74b1a7b0df2a256d26ab5e5fc6cb75"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-739/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-100/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-739/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-100/solution_01.png"
reference_asset_refs: []
aggregate_edge_policy: "block_strong_edges"
evidence_status: "pending_user_confirmation"
---

# LA-100 向量组等价与表示式

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-100_2019年第23题.md`
- wrongnet ID：`LA-100`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 向量组 |
| 题型 | 向量组等价与线性表示 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 向量组线性相关
- 矩阵秩
- 参数分类讨论

### 错因

- 个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。

### 方法

- 向量组等价判定
- 线性表示
- 矩阵秩判断
- 参数分类讨论

### 陷阱

- 向量组等价的充要条件是 \(r(A)=r(B)=r(A,B)\)，不是只看两个组各自秩相同。
- \(a=-1\) 时 \(A\) 与 \(B\) 非零行个数不同，不满足等价。
- \(a=1\) 是退化情形，\(\beta_3\) 的表示式含任意参数；\(a\ne\pm1\) 时表示唯一。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先用 r(A)=r(B)=r(A,B) 判等价参数。 |
| missed_action | 旧卡未记录用户实际漏点；复做时重点确认是否漏掉“用 r(A)=r(B)=r(A,B) 判等价参数。”这一步。 |
| related_method_card_id | L06-006 |
| next_reminder | 看到向量组等价又要求表示式，先判等价参数，再解表示式；退化点单独查。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-047_参数分类讨论]]
- [[MATHWIKI-KNOWLEDGE-101_向量组线性相关]]
- [[MATHWIKI-METHOD-CLUSTER-040_参数分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断]]
- [[MATHWIKI-METHOD-CLUSTER-177_线性表示]]
- [[MATHWIKI-METHOD-CLUSTER-337_向量组等价判定]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
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

- 仅投影经核验的客观内容。

- 用户个人断点仍受证据门禁约束。
- 当前正式 strong edge 为零。
