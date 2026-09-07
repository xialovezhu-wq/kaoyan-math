---
wiki_id: SRC-WQ-GS-089
type: source_summary
title: "GS-089 1000题A组3.12"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-089_1000题A组3.12.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-089_1000题A组3.12.md"
visual_ids:
  - "VIS-GS-089"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-089/question_01.png"
wrongnet_refs:
  - "GS-089"
related_wrongnet_refs:
  - "GS-458"
knowledge:
  - "导数定义"
  - "数列极限"
  - "等价无穷小"
  - "函数增量分解"
error_causes:
  - "概念边界混淆"
  - "符号错误"
  - "计算失误"
methods:
  - "加减中间项"
  - "导数定义"
  - "真实增量匹配"
  - "等价无穷小"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-005"
  - "MATHWIKI-ERROR-CLUSTER-014"
  - "MATHWIKI-ERROR-CLUSTER-019"
  - "MATHWIKI-ERROR-CLUSTER-027"
  - "MATHWIKI-KNOWLEDGE-004"
  - "MATHWIKI-KNOWLEDGE-006"
  - "MATHWIKI-KNOWLEDGE-009"
  - "MATHWIKI-KNOWLEDGE-472"
  - "MATHWIKI-METHOD-CLUSTER-013"
  - "MATHWIKI-METHOD-CLUSTER-026"
  - "MATHWIKI-METHOD-CLUSTER-1514"
  - "MATHWIKI-METHOD-CLUSTER-1515"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-METHOD-013_导数定义差商入口"
  - "MATHWIKI-GS-METHOD-093_局部展开对象与真实增量匹配"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
formal_projection_sha256: 2315b929dab8b25297930d546e58a13d9f90552585740b4e8d3e0d953e69b11b
evidence_status: user_attempt_with_assistant_inferred_break
personal_diagnosis_status: user_confirmed_after_explanation
last_updated: "2026-07-29"
---

# GS-089 1000题A组3.12

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-089_1000题A组3.12.md`
- wrongnet ID：`GS-089`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-089_1000题A组3.12|VIS-GS-089]]
- 已核验题图：`错题知识网络/assets/visual_wrong_questions/GS-089/question_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 导数定义型数列极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 导数定义
- 数列极限
- 等价无穷小
- 函数增量分解

### 错因

- 概念边界混淆
- 符号错误
- 计算失误

### 方法

- 加减中间项
- 导数定义
- 真实增量匹配
- 等价无穷小

### 陷阱

- 分母必须匹配真实增量
- 左右两段差商都要处理
- sin(1/n) 与 1/n 同阶

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-CONCEPT |
| expected_first_action | 每段拆开后先标出真实增量；第二段令 \(h_n=-x_n\) |
| missed_action | 已正确加减中间项，但把 \(-x_n\) 的负号重复处理，并在完整比例中遗漏常数项 \(-1\) |
| related_method_card_id | H03-001 |
| next_reminder | 看到两个函数值趋近同一点作差，先加减中间值，再分别匹配真实自变量增量。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-005_A-CONCEPT]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-ERROR-CLUSTER-019_符号错误]]
- [[MATHWIKI-ERROR-CLUSTER-027_概念边界混淆]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-006_导数定义]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-472_函数增量分解]]
- [[MATHWIKI-METHOD-CLUSTER-013_导数定义]]
- [[MATHWIKI-METHOD-CLUSTER-026_等价无穷小]]
- [[MATHWIKI-METHOD-CLUSTER-1514_加减中间项]]
- [[MATHWIKI-METHOD-CLUSTER-1515_真实增量匹配]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-METHOD-013_导数定义差商入口]]
- [[MATHWIKI-GS-METHOD-093_局部展开对象与真实增量匹配]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
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
