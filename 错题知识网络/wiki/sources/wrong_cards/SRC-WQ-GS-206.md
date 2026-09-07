---
wiki_id: SRC-WQ-GS-206
type: source_summary
title: "GS-206 强化例题15.16：阻力运动中的变量转换"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-206_强化例题15.16.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-206"
knowledge:
  - "微分方程"
  - "微分方程建模"
  - "一阶微分方程"
error_causes:
  - "题型入口风险：问位移比例时用 $dv/dt=v\\,dv/dx$，把速度改写成位移函数。"
methods:
  - "牛顿第二定律建模"
  - "链式换元"
  - "用位移作自变量"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-006_B1-GOAL"
  - "MATHWIKI-ERROR-CLUSTER-456_题型入口风险-问位移比例时用$dv-dt=v-dv-dx$-把速度改写成"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-KNOWLEDGE-105_一阶微分方程"
  - "MATHWIKI-KNOWLEDGE-147_微分方程建模"
  - "MATHWIKI-METHOD-CLUSTER-1177_牛顿第二定律建模"
  - "MATHWIKI-METHOD-CLUSTER-1202_用位移作自变量"
  - "MATHWIKI-METHOD-CLUSTER-1393_链式换元"
  - "MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-206 强化例题15.16：阻力运动中的变量转换

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-206_强化例题15.16.md`
- wrongnet ID：`GS-206`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 高等数学-微分方程 |
| 题型 | 物理运动建模微分方程 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 微分方程
- 微分方程建模
- 一阶微分方程

### 错因

- 题型入口风险：问位移比例时用 $dv/dt=v\,dv/dx$，把速度改写成位移函数。

### 方法

- 牛顿第二定律建模
- 链式换元
- 用位移作自变量

### 陷阱

- 题目问总位移的一半处速度，不是时间过半速度
- 要用 $dv/dt=(dv/dx)(dx/dt)=v\,dv/dx$
- 总滑行距离来自速度降为 $0$ 的位置

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B1-GOAL |
| expected_first_action | 先把速度看成位移函数，写 $\frac{dv}{dt}=v\frac{dv}{dx}$。 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是把半位移误当成半时间，没有切换自变量。 |
| related_method_card_id | H15-011 |
| next_reminder | 看到题目问位移比例，先把 $v$ 看成 $x$ 的函数，再写 $\frac{dv}{dt}=v\frac{dv}{dx}$。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-006_B1-GOAL]]
- [[MATHWIKI-ERROR-CLUSTER-456_题型入口风险-问位移比例时用$dv-dt=v-dv-dx$-把速度改写成]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-KNOWLEDGE-105_一阶微分方程]]
- [[MATHWIKI-KNOWLEDGE-147_微分方程建模]]
- [[MATHWIKI-METHOD-CLUSTER-1177_牛顿第二定律建模]]
- [[MATHWIKI-METHOD-CLUSTER-1202_用位移作自变量]]
- [[MATHWIKI-METHOD-CLUSTER-1393_链式换元]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-205
- GS-207

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
