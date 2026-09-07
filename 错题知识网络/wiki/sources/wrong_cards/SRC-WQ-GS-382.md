---
wiki_id: SRC-WQ-GS-382
type: source_summary
title: "GS-382 2022年真题第20题"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-382_2022年真题第20题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-382"
knowledge:
  - "多元函数偏导"
  - "偏微分方程"
  - "复合函数求导"
  - "变量代换"
  - "多元函数极值"
error_causes:
  - "变量混淆"
  - "条件检查遗漏"
methods:
  - "条件转化"
  - "链式求导"
  - "回代化简"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-024_变量混淆"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-030_复合函数求导"
  - "MATHWIKI-KNOWLEDGE-055_多元函数极值"
  - "MATHWIKI-KNOWLEDGE-115_偏微分方程"
  - "MATHWIKI-KNOWLEDGE-117_变量代换"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-018_链式求导"
  - "MATHWIKI-METHOD-CLUSTER-070_回代化简"
  - "MATHWIKI-GS-METHOD-031_偏微分方程变量代换化简"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-382 2022年真题第20题

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-382_2022年真题第20题.md`
- wrongnet ID：`GS-382`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 偏微分方程化简求解 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数偏导
- 偏微分方程
- 复合函数求导
- 变量代换
- 多元函数极值

### 错因

- 变量混淆
- 条件检查遗漏

### 方法

- 条件转化
- 链式求导
- 回代化简

### 陷阱

- 链式求导符号方向
- 驻点判别二阶条件遗漏

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先由 \(u=x,\ v=y-x\) 写出 \(g_x=f_u-f_v\) |
| missed_action | 没有先识别 \(g_x\) 正好对应题设的 \(f_u-f_v\) |
| related_method_card_id | H13-011 |
| next_reminder | 看到 \(f_u-f_v\) 和 \(f(x,y-x)\)，先用链式求导检查能否直接凑出题设组合。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-024_变量混淆]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-030_复合函数求导]]
- [[MATHWIKI-KNOWLEDGE-055_多元函数极值]]
- [[MATHWIKI-KNOWLEDGE-115_偏微分方程]]
- [[MATHWIKI-KNOWLEDGE-117_变量代换]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-018_链式求导]]
- [[MATHWIKI-METHOD-CLUSTER-070_回代化简]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-031_偏微分方程变量代换化简]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

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
