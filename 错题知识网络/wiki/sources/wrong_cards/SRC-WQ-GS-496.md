---
wiki_id: SRC-WQ-GS-496
type: source_summary
title: "GS-496 102339 交错级数莱布尼茨"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-496_102339交错级数莱布尼茨.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-496_102339-2026.5.23.md"
visual_ids:
  - "VIS-GS-496"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-496/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-496"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "数项级数敛散性判别"
  - "交错级数"
  - "莱布尼茨判别法"
  - "级数收敛必要条件"
  - "函数单调性"
error_causes:
  - "题型识别失败"
  - "方法选择错误"
  - "条件忽略"
  - "过程跳步"
methods:
  - "先判型"
  - "正项部分提取"
  - "莱布尼茨判别法"
  - "导数判单调"
  - "分母单调转倒数单调"
  - "有限项不影响敛散性"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-059_交错级数"
  - "MATHWIKI-KNOWLEDGE-062_级数收敛必要条件"
  - "MATHWIKI-KNOWLEDGE-071_函数单调性"
  - "MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法"
  - "MATHWIKI-METHOD-CLUSTER-236_有限项不影响敛散性"
  - "MATHWIKI-METHOD-CLUSTER-312_分母单调转倒数单调"
  - "MATHWIKI-METHOD-CLUSTER-417_正项部分提取"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-068
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: cfe6e335bc255383376b8fb82d4f017a1540970529bd81ad2e61998dfb9e69d6
---

# GS-496 102339 交错级数莱布尼茨

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-496_102339交错级数莱布尼茨.md`
- wrongnet ID：`GS-496`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-496_102339-2026.5.23.md`（`VIS-GS-496`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 交错级数敛散性判断 |
| 日期 | 2026-05-23 |
| 状态 | 已掌握 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 无穷级数
- 数项级数敛散性判别
- 交错级数
- 莱布尼茨判别法
- 级数收敛必要条件
- 函数单调性

### 错因

- 题型识别失败
- 方法选择错误
- 条件忽略
- 过程跳步

### 方法

- 先判型
- 正项部分提取
- 莱布尼茨判别法
- 导数判单调
- 分母单调转倒数单调
- 有限项不影响敛散性

### 陷阱

- 交错级数入口
- 正项部分
- 莱布尼茨单调性遗漏
- 有限项不影响敛散性
- 对数幂比较

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写 \(b_n=\frac1{\sqrt n-\ln n}\)，检查 \(b_n\to0\)，再令 \(g(x)=\sqrt x-\ln x\) 判 \(b_n\) 最终递减 |
| missed_action | 没有把交错级数转成对正项部分的两个检查目标，也漏掉有限项不影响敛散性 |
| related_method_card_id | H16-016 |
| next_reminder | 看到 \((-1)^n b_n\)，先写出 \(b_n\)，再按“趋零、最终单调、有限项不影响”检查。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-059_交错级数]]
- [[MATHWIKI-KNOWLEDGE-062_级数收敛必要条件]]
- [[MATHWIKI-KNOWLEDGE-071_函数单调性]]
- [[MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法]]
- [[MATHWIKI-METHOD-CLUSTER-236_有限项不影响敛散性]]
- [[MATHWIKI-METHOD-CLUSTER-312_分母单调转倒数单调]]
- [[MATHWIKI-METHOD-CLUSTER-417_正项部分提取]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
