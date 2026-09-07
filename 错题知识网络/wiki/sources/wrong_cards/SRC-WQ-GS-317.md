---
wiki_id: SRC-WQ-GS-317
type: source_summary
title: "GS-317 1000题B组2.13"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-317_1000题B组2.13.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-317"
knowledge:
  - "数列极限"
  - "定积分"
  - "夹逼准则"
  - "华里士公式"
error_causes:
  - "概念混淆"
  - "方法选择错误"
  - "公式记错"
methods:
  - "夹逼"
  - "夹逼准则"
  - "华里士公式"
  - "单调性比较"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-015_公式记错"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-083_夹逼准则"
  - "MATHWIKI-KNOWLEDGE-138_华里士公式"
  - "MATHWIKI-METHOD-CLUSTER-016_夹逼准则"
  - "MATHWIKI-METHOD-CLUSTER-024_夹逼"
  - "MATHWIKI-METHOD-CLUSTER-110_华里士公式"
  - "MATHWIKI-METHOD-CLUSTER-111_单调性比较"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-073"
  - "GS-316"
formal_projection_sha256: 4c28683bfb15cf0f6531860dd4204f957c1299d11235c307a6c3f0fca3fcf03b
---

# GS-317 1000题B组2.13

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-317_1000题B组2.13.md`
- wrongnet ID：`GS-317`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 数列极限 |
| 题型 | 华里士积分数列极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 数列极限
- 定积分
- 夹逼准则
- 华里士公式

### 错因

- 概念混淆
- 方法选择错误
- 公式记错

### 方法

- 夹逼
- 夹逼准则
- 华里士公式
- 单调性比较

### 陷阱

- 适用条件
- 双阶乘

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先在 \(0<x<1\) 上比较 \((1-x^2)^{(n+1)/2}\) 与 \((1-x^2)^{n/2}\)，推出 \(a_{n+1}<a_n\) |
| missed_action | 没有先利用 \(0<1-x^2<1\) 判断幂次越大积分越小，也没有接 Wallis 奇偶项夹逼 |
| related_method_card_id | H11-009 |
| next_reminder | 看到 \(\int_0^1(1-x^2)^{n/2}dx\)，先比较幂次证明单调；若要求 \(n a_n^2\)，立刻用 \(x=\sin t\) 接 Wallis 积分并做奇偶夹逼。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-015_公式记错]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-083_夹逼准则]]
- [[MATHWIKI-KNOWLEDGE-138_华里士公式]]
- [[MATHWIKI-METHOD-CLUSTER-016_夹逼准则]]
- [[MATHWIKI-METHOD-CLUSTER-024_夹逼]]
- [[MATHWIKI-METHOD-CLUSTER-110_华里士公式]]
- [[MATHWIKI-METHOD-CLUSTER-111_单调性比较]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-073
- GS-316

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
