---
wiki_id: SRC-WQ-GS-383
type: source_summary
title: "GS-383 强化例题13.22"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-383_强化例题13.22.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-383"
knowledge:
  - "多元函数偏导"
  - "偏微分方程"
  - "复合函数求导"
  - "二阶偏导"
  - "变量代换"
  - "参数退化讨论"
error_causes:
  - "动作链断裂"
  - "条件检查遗漏"
methods:
  - "条件转化"
  - "链式求导"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-030_复合函数求导"
  - "MATHWIKI-KNOWLEDGE-115_偏微分方程"
  - "MATHWIKI-KNOWLEDGE-117_变量代换"
  - "MATHWIKI-KNOWLEDGE-133_二阶偏导"
  - "MATHWIKI-KNOWLEDGE-241_参数退化讨论"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-018_链式求导"
  - "MATHWIKI-GS-METHOD-031_偏微分方程变量代换化简"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-383 强化例题13.22

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-383_强化例题13.22.md`
- wrongnet ID：`GS-383`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 二阶偏微分方程变量代换求参数 |
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
- 参数退化讨论

### 错因

- 动作链断裂
- 条件检查遗漏

### 方法

- 条件转化
- 链式求导

### 陷阱

- 二阶链式求导系数漏算
- 参数条件只取形式根未验系数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先写 \(u_x,u_y,v_x,v_y\)，再展开原方程中的二阶偏导系数 |
| missed_action | 只看目标形式，未完整展开二阶项并检查 \(z_{uv}\) 系数非零 |
| related_method_card_id | H13-011 |
| next_reminder | 看到 PDE 变量变换求参数，先完整展开二阶系数，再同时验目标项保留和多余项消失。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-030_复合函数求导]]
- [[MATHWIKI-KNOWLEDGE-115_偏微分方程]]
- [[MATHWIKI-KNOWLEDGE-117_变量代换]]
- [[MATHWIKI-KNOWLEDGE-133_二阶偏导]]
- [[MATHWIKI-KNOWLEDGE-241_参数退化讨论]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-018_链式求导]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-031_偏微分方程变量代换化简]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-380
- GS-381

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
