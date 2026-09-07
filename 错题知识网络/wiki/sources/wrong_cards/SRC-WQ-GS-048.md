---
wiki_id: SRC-WQ-GS-048
type: source_summary
title: "GS-048 例题1.13"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-048_例题1.13.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-048"
knowledge:
  - "极限与连续"
  - "数列极限"
  - "一元函数微分学应用"
error_causes:
  - "条件忽略"
  - "计算失误"
  - "符号错误"
methods:
  - "单调有界"
  - "分类讨论"
  - "单调有界准则"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-014_计算失误"
  - "MATHWIKI-ERROR-CLUSTER-019_符号错误"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-010_单调有界准则"
  - "MATHWIKI-METHOD-CLUSTER-017_单调有界"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-048 例题1.13

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-048_例题1.13.md`
- wrongnet ID：`GS-048`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 递推数列极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 数列极限
- 一元函数微分学应用

### 错因

- 条件忽略
- 计算失误
- 符号错误

### 方法

- 单调有界
- 分类讨论
- 单调有界准则

### 陷阱

- 正负号
- 适用条件

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先固定任意 \(x_0\)，由单调减少写出对所有 \(t>x_0\) 有 \(f(x_0)\ge f(t)\)，再令 \(t\to+\infty\)。 |
| missed_action | 没有把固定点值与无穷远极限通过单调性比较，而是滑向导数符号判断。 |
| related_method_card_id | H05-002 |
| next_reminder | 看到“单调 + 无穷远极限 + 证明符号”，先固定任意点，再用远处点的极限压住固定点值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-ERROR-CLUSTER-019_符号错误]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-010_单调有界准则]]
- [[MATHWIKI-METHOD-CLUSTER-017_单调有界]]

### 深度编译页

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
