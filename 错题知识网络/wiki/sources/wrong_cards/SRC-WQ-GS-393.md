---
wiki_id: SRC-WQ-GS-393
type: source_summary
title: "GS-393 强化例题13.30"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-393_强化例题13.30.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-393"
knowledge:
  - "多元函数极值"
  - "二次型"
error_causes:
  - "方法调取失败"
  - "目标识别断点"
methods:
  - "拉格朗日乘数法"
  - "二次型最值"
  - "特征值法"
  - "严格单调变换"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-ERROR-CLUSTER-034_目标识别断点"
  - "MATHWIKI-KNOWLEDGE-034_二次型"
  - "MATHWIKI-KNOWLEDGE-055_多元函数极值"
  - "MATHWIKI-METHOD-CLUSTER-1183_特征值法"
  - "MATHWIKI-METHOD-CLUSTER-157_拉格朗日乘数法"
  - "MATHWIKI-METHOD-CLUSTER-532_严格单调变换"
  - "MATHWIKI-METHOD-CLUSTER-552_二次型最值"
  - "MATHWIKI-GS-METHOD-033_多元函数条件与闭区域最值"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-393 强化例题13.30

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-393_强化例题13.30.md`
- wrongnet ID：`GS-393`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 二次型约束最值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数极值
- 二次型

### 错因

- 方法调取失败
- 目标识别断点

### 方法

- 拉格朗日乘数法
- 二次型最值
- 特征值法
- 严格单调变换

### 陷阱

- 根号目标未先平方
- 约束二次型未转特征值

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先令 \(S=x^2+y^2\)，把求 \(u\) 的最值转成求 \(S\) 的最值 |
| missed_action | 没有先把根号目标平方化并识别二次型约束最值结构 |
| related_method_card_id | H13-012 |
| next_reminder | 看到根号距离和二次型约束，先平方化目标，再用拉格朗日或特征值法求最值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-034_目标识别断点]]
- [[MATHWIKI-KNOWLEDGE-034_二次型]]
- [[MATHWIKI-KNOWLEDGE-055_多元函数极值]]
- [[MATHWIKI-METHOD-CLUSTER-1183_特征值法]]
- [[MATHWIKI-METHOD-CLUSTER-157_拉格朗日乘数法]]
- [[MATHWIKI-METHOD-CLUSTER-532_严格单调变换]]
- [[MATHWIKI-METHOD-CLUSTER-552_二次型最值]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-033_多元函数条件与闭区域最值]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-395
- GS-394

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
