---
wiki_id: SRC-WQ-GS-510
type: source_summary
title: "GS-510 102383 调和部分和收敛半径"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-510_102383调和部分和收敛半径.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-510_102383-2026.5.28.md"
visual_ids:
  - "VIS-GS-510"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-510/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-510"
related_wrongnet_refs:
  - "GS-481"
knowledge:
  - "无穷级数"
  - "幂级数"
  - "幂级数收敛半径"
  - "部分和数列"
  - "调和级数"
error_causes:
  - "概念混淆"
  - "审题遗漏"
  - "题型识别失败"
methods:
  - "先判型"
  - "根值判别法"
  - "夹逼准则"
  - "条件转化"
  - "部分和定义"
  - "构造上界"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-037_审题遗漏"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-048_幂级数"
  - "MATHWIKI-KNOWLEDGE-097_调和级数"
  - "MATHWIKI-KNOWLEDGE-129_部分和数列"
  - "MATHWIKI-KNOWLEDGE-251_幂级数收敛半径"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-016_夹逼准则"
  - "MATHWIKI-METHOD-CLUSTER-122_构造上界"
  - "MATHWIKI-METHOD-CLUSTER-133_部分和定义"
  - "MATHWIKI-METHOD-CLUSTER-408_根值判别法"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-070
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: f669f5144844d73eb587973406817ce58bdc2d195385f15969c48448eeb8f93c
---

# GS-510 102383 调和部分和收敛半径

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-510_102383调和部分和收敛半径.md`
- wrongnet ID：`GS-510`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-510_102383-2026.5.28.md`（`VIS-GS-510`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 幂级数收敛半径 |
| 日期 | 2026-05-28 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 无穷级数
- 幂级数
- 幂级数收敛半径
- 部分和数列
- 调和级数

### 错因

- 概念混淆
- 审题遗漏
- 题型识别失败

### 方法

- 先判型
- 根值判别法
- 夹逼准则
- 条件转化
- 部分和定义
- 构造上界

### 陷阱

- 部分和定义
- 通项与部分和混淆
- 收敛半径公式
- 根值判别入口
- 调和部分和增长

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写清 \(a_{n+1}=a_n+\frac1{n+1}\)，并用 \(1\le a_n\le n\) 夹逼出 \(\sqrt[n]{a_n}\to1\)。 |
| missed_action | 把调和部分和 \(a_n=\sum_{k=1}^n\frac1k\) 误看成单项 \(1/n\)，导致半径公式入口错。 |
| related_method_card_id | H16-020 |
| next_reminder | 看到 \(a_n\) 由求和号定义，先判断它是“部分和”还是“通项”；本题先用 \(1\le a_n\le n\) 算根值极限。 |
| evidence_origin | user_confirmed |
| repeat_count | 1 |
| repeat_count_source | wrong_history |

## 证据边界

- 个人错因仅来自正式卡 dated `wrong_history`；详情解析只核验题面与解法，不反推个人错因。
- 题图或解析图存在，只证明视觉来源已注册，不单独证明个人作答过程、错误次数或掌握度。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-037_审题遗漏]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-097_调和级数]]
- [[MATHWIKI-KNOWLEDGE-129_部分和数列]]
- [[MATHWIKI-KNOWLEDGE-251_幂级数收敛半径]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-016_夹逼准则]]
- [[MATHWIKI-METHOD-CLUSTER-122_构造上界]]
- [[MATHWIKI-METHOD-CLUSTER-133_部分和定义]]
- [[MATHWIKI-METHOD-CLUSTER-408_根值判别法]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- [[错题知识网络/错题卡/GS-481_102409部分和子列极限|GS-481]]

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
