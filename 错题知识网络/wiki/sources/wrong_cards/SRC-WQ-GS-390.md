---
wiki_id: SRC-WQ-GS-390
type: source_summary
title: "GS-390 强化例题13.26"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-390_强化例题13.26.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-390"
knowledge:
  - "多元函数极值"
  - "多元函数偏导"
error_causes:
  - "动作链断裂"
  - "概念混淆"
methods:
  - "驻点求解"
  - "Hessian 二次型"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-055_多元函数极值"
  - "MATHWIKI-METHOD-CLUSTER-076_Hessian二次型"
  - "MATHWIKI-METHOD-CLUSTER-086_驻点求解"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-032_多元函数极值驻点判别"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-390 强化例题13.26

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-390_强化例题13.26.md`
- wrongnet ID：`GS-390`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 多元函数无条件极值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数极值
- 多元函数偏导

### 错因

- 动作链断裂
- 概念混淆

### 方法

- 驻点求解
- Hessian 二次型

### 陷阱

- 驻点不是极值点
- 局部极值与全局最值混淆

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先联立 \(f_x=0,\ f_y=0\) 求出所有驻点 |
| missed_action | 没有逐点做 Hessian 判别，容易把驻点直接当成极值点 |
| related_method_card_id | H13-012 |
| next_reminder | 看到二元函数求极值，先完整求驻点，再逐点 Hessian 判别，不要把驻点默认当极值点。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-055_多元函数极值]]
- [[MATHWIKI-METHOD-CLUSTER-076_Hessian二次型]]
- [[MATHWIKI-METHOD-CLUSTER-086_驻点求解]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-032_多元函数极值驻点判别]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-396
- GS-387
- GS-389

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
