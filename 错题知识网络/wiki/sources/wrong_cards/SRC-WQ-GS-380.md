---
wiki_id: SRC-WQ-GS-380
type: source_summary
title: "GS-380 强化例题13.21"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-380_强化例题13.21.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-380"
knowledge:
  - "多元函数偏导"
  - "偏微分方程"
  - "复合函数求导"
  - "二阶偏导"
  - "变量代换"
  - "一阶线性微分方程"
error_causes:
  - "变量混淆"
  - "动作链断裂"
methods:
  - "条件转化"
  - "链式求导"
  - "一阶线性微分方程"
  - "回代化简"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-024_变量混淆"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-030_复合函数求导"
  - "MATHWIKI-KNOWLEDGE-065_一阶线性微分方程"
  - "MATHWIKI-KNOWLEDGE-115_偏微分方程"
  - "MATHWIKI-KNOWLEDGE-117_变量代换"
  - "MATHWIKI-KNOWLEDGE-133_二阶偏导"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-018_链式求导"
  - "MATHWIKI-METHOD-CLUSTER-070_回代化简"
  - "MATHWIKI-METHOD-CLUSTER-088_一阶线性微分方程"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-031_偏微分方程变量代换化简"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-380 强化例题13.21

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-380_强化例题13.21.md`
- wrongnet ID：`GS-380`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 二阶偏微分方程变量代换化简求解 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数偏导
- 偏微分方程
- 复合函数求导
- 二阶偏导
- 变量代换
- 一阶线性微分方程

### 错因

- 变量混淆
- 动作链断裂

### 方法

- 条件转化
- 链式求导
- 一阶线性微分方程
- 回代化简

### 陷阱

- 变量替换后自变量对象混淆
- 二阶链式求导系数漏算
- 边界条件代入变量错误

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写清 \(u,v\) 与 \(x,y\) 的关系，并求 \(z_x,z_y\) |
| missed_action | 没有先把 \(x,y\) 下的偏导整体转写成 \(u,v\) 下的偏导 |
| related_method_card_id | H13-011 |
| next_reminder | 看到 \(z=f(u,v)\) 和偏导方程，先画变量依赖关系，再逐项链式求导。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-024_变量混淆]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-030_复合函数求导]]
- [[MATHWIKI-KNOWLEDGE-065_一阶线性微分方程]]
- [[MATHWIKI-KNOWLEDGE-115_偏微分方程]]
- [[MATHWIKI-KNOWLEDGE-117_变量代换]]
- [[MATHWIKI-KNOWLEDGE-133_二阶偏导]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-018_链式求导]]
- [[MATHWIKI-METHOD-CLUSTER-070_回代化简]]
- [[MATHWIKI-METHOD-CLUSTER-088_一阶线性微分方程]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-031_偏微分方程变量代换化简]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-381
- GS-385

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
