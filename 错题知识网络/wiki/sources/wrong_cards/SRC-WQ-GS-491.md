---
wiki_id: SRC-WQ-GS-491
type: source_summary
title: "GS-491 57899-2 幂指数单调性"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-491_57899-2幂指数单调性.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-491_57899-2-2026.5.22.md"
visual_ids:
  - "VIS-GS-491"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-491/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-491"
related_wrongnet_refs: []
knowledge:
  - "一元函数微分学应用"
  - "幂指函数比较"
  - "导数判单调"
  - "微分不等式证明"
  - "对数变形"
error_causes:
  - "方法选择错误"
  - "题型识别失败"
  - "过程跳步"
  - "条件忽略"
methods:
  - "先判型"
  - "取对数"
  - "构造辅助函数"
  - "固定变量"
  - "导数判单调"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-091_导数判单调"
  - "MATHWIKI-KNOWLEDGE-146_微分不等式证明"
  - "MATHWIKI-KNOWLEDGE-344_对数变形"
  - "MATHWIKI-KNOWLEDGE-355_幂指函数比较"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-019_取对数"
  - "MATHWIKI-METHOD-CLUSTER-841_固定变量"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-068
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 679f88042ee2f97137848fa92550983032143f9ba3c9c8f637e407ac6d179758
---

# GS-491 57899-2 幂指数单调性

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-491_57899-2幂指数单调性.md`
- wrongnet ID：`GS-491`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-491_57899-2-2026.5.22.md`（`VIS-GS-491`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 微分不等式证明 |
| 日期 | 2026-05-22 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 幂指函数比较
- 导数判单调
- 微分不等式证明
- 对数变形

### 错因

- 方法选择错误
- 题型识别失败
- 过程跳步
- 条件忽略

### 方法

- 先判型
- 取对数
- 构造辅助函数
- 固定变量
- 导数判单调
- 条件转化

### 陷阱

- 变量固定
- 对数单调性
- 单调区间
- 适用条件
- 端点比较

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先两边取对数，把目标化为 \(b\ln a>a\ln b\)，再固定 \(a\) 令 \(f(x)=x\ln a-a\ln x\) |
| missed_action | 取对数后没有固定 \(a\) 并把 \(b\) 函数化，导致没法用单调性比较 \(f(b)\) 与 \(f(a)\) |
| related_method_card_id | H05-002 |
| next_reminder | 看到 \(a^b\) 与 \(b^a\) 比较，先取对数；再固定一个量，把另一个量函数化后用单调性比端点。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-091_导数判单调]]
- [[MATHWIKI-KNOWLEDGE-146_微分不等式证明]]
- [[MATHWIKI-KNOWLEDGE-344_对数变形]]
- [[MATHWIKI-KNOWLEDGE-355_幂指函数比较]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-019_取对数]]
- [[MATHWIKI-METHOD-CLUSTER-841_固定变量]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
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
