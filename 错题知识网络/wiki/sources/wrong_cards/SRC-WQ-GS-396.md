---
wiki_id: SRC-WQ-GS-396
type: source_summary
title: "GS-396 强化例题13.31"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-396_强化例题13.31.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-396"
knowledge:
  - "多元函数极值"
  - "多元函数偏导"
  - "最值定理"
error_causes:
  - "动作链断裂"
  - "收尾验证遗漏"
methods:
  - "驻点求解"
  - "闭区域最值"
  - "边界化单变量"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-032_收尾验证遗漏"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-055_多元函数极值"
  - "MATHWIKI-KNOWLEDGE-152_最值定理"
  - "MATHWIKI-METHOD-CLUSTER-086_驻点求解"
  - "MATHWIKI-METHOD-CLUSTER-1346_边界化单变量"
  - "MATHWIKI-METHOD-CLUSTER-264_闭区域最值"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-033_多元函数条件与闭区域最值"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-396 强化例题13.31

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-396_强化例题13.31.md`
- wrongnet ID：`GS-396`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 闭区域最大最小值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数极值
- 多元函数偏导
- 最值定理

### 错因

- 动作链断裂
- 收尾验证遗漏

### 方法

- 驻点求解
- 闭区域最值
- 边界化单变量

### 陷阱

- 只算内部驻点不比较边界
- 局部极值与全局最值混淆

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先列内部驻点候选，再把边界化成单变量问题 |
| missed_action | 没有把内部候选和边界候选都列齐后统一比较函数值 |
| related_method_card_id | H13-012 |
| next_reminder | 看到闭区域最大最小值，先列内部驻点和边界候选，再统一比较函数值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-032_收尾验证遗漏]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-055_多元函数极值]]
- [[MATHWIKI-KNOWLEDGE-152_最值定理]]
- [[MATHWIKI-METHOD-CLUSTER-086_驻点求解]]
- [[MATHWIKI-METHOD-CLUSTER-1346_边界化单变量]]
- [[MATHWIKI-METHOD-CLUSTER-264_闭区域最值]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-033_多元函数条件与闭区域最值]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-390
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
