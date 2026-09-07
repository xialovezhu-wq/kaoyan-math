---
wiki_id: SRC-WQ-GS-267
type: source_summary
title: "GS-267 1000题B组9.7（103478） 2026.5.7"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-267_1000题B组9.7（103478）2026.5.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-267"
knowledge:
  - "一元函数积分学"
  - "定积分"
  - "第一类换元"
  - "变量代换"
error_causes:
  - "题面语言翻译断点"
  - "换元变量来源不清"
  - "计算失误"
methods:
  - "换元"
  - "条件转化"
  - "第一类换元"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-014_计算失误"
  - "MATHWIKI-ERROR-CLUSTER-020_题面语言翻译断点"
  - "MATHWIKI-ERROR-CLUSTER-055_换元变量来源不清"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-117_变量代换"
  - "MATHWIKI-KNOWLEDGE-282_一元函数积分学"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-009_换元"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-267 1000题B组9.7（103478） 2026.5.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-267_1000题B组9.7（103478）2026.5.7.md`
- wrongnet ID：`GS-267`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 函数方程定积分计算 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数积分学
- 定积分
- 第一类换元
- 变量代换

### 错因

- 题面语言翻译断点
- 换元变量来源不清
- 计算失误

### 方法

- 换元
- 条件转化
- 第一类换元

### 陷阱

- 变量混淆
- 幂运算零点

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先令 \(u=x^2\)，把条件改写为 \(f(u+1)-f(u)=\sqrt u\) |
| missed_action | 没有先把 \(x^2\) 统一成 \(u\)，也没有把等式两边在 \([0,1]\) 上积分 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到 \(f(x^2+1)-f(x^2)\) 这类条件，先把 \(x^2\) 统一成新变量，再对目标区间对应的变量范围积分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-ERROR-CLUSTER-020_题面语言翻译断点]]
- [[MATHWIKI-ERROR-CLUSTER-055_换元变量来源不清]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-117_变量代换]]
- [[MATHWIKI-KNOWLEDGE-282_一元函数积分学]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-009_换元]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-162
- GS-637

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
