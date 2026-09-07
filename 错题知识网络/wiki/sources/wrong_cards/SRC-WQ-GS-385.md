---
wiki_id: SRC-WQ-GS-385
type: source_summary
title: "GS-385 强化例题13.24"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-385_强化例题13.24.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-385"
knowledge:
  - "微分方程"
  - "一阶微分方程"
  - "多元函数微分学"
  - "多元函数偏导"
  - "偏微分方程"
error_causes:
  - "方法入口未沉淀"
  - "变量混淆"
  - "动作链断裂"
methods:
  - "偏微分方程化简"
  - "分离变量"
  - "条件转化"
  - "初值定常数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-012_方法入口未沉淀"
  - "MATHWIKI-ERROR-CLUSTER-024_变量混淆"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-KNOWLEDGE-105_一阶微分方程"
  - "MATHWIKI-KNOWLEDGE-115_偏微分方程"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-037_初值定常数"
  - "MATHWIKI-METHOD-CLUSTER-066_分离变量"
  - "MATHWIKI-METHOD-CLUSTER-606_偏微分方程化简"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-031_偏微分方程变量代换化简"
  - "MATHWIKI-GS-METHOD-056_微分方程入口判别链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-385 强化例题13.24

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-385_强化例题13.24.md`
- wrongnet ID：`GS-385`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 一阶偏微分方程求函数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 微分方程
- 一阶微分方程
- 多元函数微分学
- 多元函数偏导
- 偏微分方程

### 错因

- 方法入口未沉淀
- 变量混淆
- 动作链断裂

### 方法

- 偏微分方程化简
- 分离变量
- 条件转化
- 初值定常数

### 陷阱

- 把 \(C(y)\) 当普通常数
- 漏用 \(f_y(0,y)\)
- 初值定常数漏掉

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先由 \(f_x=-f\) 写出 \(f(x,y)=C(y)e^{-x}\)。 |
| missed_action | 历史卡没有沉淀“关于 x 解方程、积分常数是 C(y)”这一第一动作。 |
| related_method_card_id | H13-011 |
| next_reminder | 看到 \(f_x=\phi(f)\) 这类偏微分方程，先固定另一个变量，把它当关于 x 的一阶方程解，再用边界条件定任意函数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-012_方法入口未沉淀]]
- [[MATHWIKI-ERROR-CLUSTER-024_变量混淆]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-KNOWLEDGE-105_一阶微分方程]]
- [[MATHWIKI-KNOWLEDGE-115_偏微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-037_初值定常数]]
- [[MATHWIKI-METHOD-CLUSTER-066_分离变量]]
- [[MATHWIKI-METHOD-CLUSTER-606_偏微分方程化简]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-031_偏微分方程变量代换化简]]
- [[MATHWIKI-GS-METHOD-056_微分方程入口判别链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-380
- GS-382

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
