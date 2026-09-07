---
wiki_id: SRC-WQ-GS-394
type: source_summary
title: "GS-394 强化例题13.29"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-394_强化例题13.29.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-394"
knowledge:
  - "多元函数极值"
  - "多元函数偏导"
  - "隐函数求导"
error_causes:
  - "条件检查遗漏"
  - "方法调取失败"
methods:
  - "拉格朗日乘数法"
  - "隐函数求导"
  - "条件极值必要条件"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-055_多元函数极值"
  - "MATHWIKI-KNOWLEDGE-078_隐函数求导"
  - "MATHWIKI-METHOD-CLUSTER-054_隐函数求导"
  - "MATHWIKI-METHOD-CLUSTER-157_拉格朗日乘数法"
  - "MATHWIKI-METHOD-CLUSTER-393_条件极值必要条件"
  - "MATHWIKI-GS-METHOD-033_多元函数条件与闭区域最值"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-394 强化例题13.29

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-394_强化例题13.29.md`
- wrongnet ID：`GS-394`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 约束极值必要条件 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数极值
- 多元函数偏导
- 隐函数求导

### 错因

- 条件检查遗漏
- 方法调取失败

### 方法

- 拉格朗日乘数法
- 隐函数求导
- 条件极值必要条件

### 陷阱

- 把约束极值误当无条件驻点
- 漏用 G_y 不为 0

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先把 \(G_y\ne0\) 转成局部可写 \(y=y(x)\) |
| missed_action | 没有利用 \(G_y\ne0\) 这个隐函数条件，容易误当无条件驻点处理 |
| related_method_card_id | H13-012 |
| next_reminder | 看到约束极值且给出 \(G_y\ne0\)，先用隐函数消元，再写限制函数的一阶必要条件。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-055_多元函数极值]]
- [[MATHWIKI-KNOWLEDGE-078_隐函数求导]]
- [[MATHWIKI-METHOD-CLUSTER-054_隐函数求导]]
- [[MATHWIKI-METHOD-CLUSTER-157_拉格朗日乘数法]]
- [[MATHWIKI-METHOD-CLUSTER-393_条件极值必要条件]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-033_多元函数条件与闭区域最值]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-393
- GS-395

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
