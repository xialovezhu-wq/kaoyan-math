---
wiki_id: SRC-WQ-GS-374
type: source_summary
title: "GS-374 强化例题13.16"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-374_强化例题13.16.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-374"
knowledge:
  - "多元函数微分学"
  - "多元函数偏导"
  - "复合函数求导"
  - "多元函数极值"
error_causes:
  - "知识点挂载错误"
  - "方法入口未沉淀"
methods:
  - "链式求导"
  - "乘积法则"
  - "极值点梯度为零"
  - "代入化简"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-012_方法入口未沉淀"
  - "MATHWIKI-ERROR-CLUSTER-044_知识点挂载错误"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-KNOWLEDGE-030_复合函数求导"
  - "MATHWIKI-KNOWLEDGE-055_多元函数极值"
  - "MATHWIKI-METHOD-CLUSTER-018_链式求导"
  - "MATHWIKI-METHOD-CLUSTER-1107_极值点梯度为零"
  - "MATHWIKI-METHOD-CLUSTER-285_代入化简"
  - "MATHWIKI-METHOD-CLUSTER-546_乘积法则"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-046_多元公式模板入口链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-374 强化例题13.16

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-374_强化例题13.16.md`
- wrongnet ID：`GS-374`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 二元复合函数二阶偏导 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数微分学
- 多元函数偏导
- 复合函数求导
- 多元函数极值

### 错因

- 知识点挂载错误
- 方法入口未沉淀

### 方法

- 链式求导
- 乘积法则
- 极值点梯度为零
- 代入化简

### 陷阱

- 适用条件
- 外层偏导取值点错位
- 内层偏导取值点错位
- 漏用极值点梯度为零

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先设外层变量 \(u=x+y,\ v=f(x,y)\)，写 \(z_x=f_1(u,v)u_x+f_2(u,v)v_x\)。 |
| missed_action | 历史卡误归入无穷小比较，未沉淀复合链式求导和极值清项。 |
| related_method_card_id | H13-007 |
| next_reminder | 看到二元复合函数二阶偏导，先画变量依赖图，再求一阶、再对目标变量求导并代点清项。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-012_方法入口未沉淀]]
- [[MATHWIKI-ERROR-CLUSTER-044_知识点挂载错误]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-KNOWLEDGE-030_复合函数求导]]
- [[MATHWIKI-KNOWLEDGE-055_多元函数极值]]
- [[MATHWIKI-METHOD-CLUSTER-018_链式求导]]
- [[MATHWIKI-METHOD-CLUSTER-1107_极值点梯度为零]]
- [[MATHWIKI-METHOD-CLUSTER-285_代入化简]]
- [[MATHWIKI-METHOD-CLUSTER-546_乘积法则]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-046_多元公式模板入口链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-376
- GS-465

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
