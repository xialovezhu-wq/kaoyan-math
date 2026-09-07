---
wiki_id: SRC-WQ-GS-327
type: source_summary
title: "GS-327 强化例题11.12（还原对称性）-2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-327_强化例题11.12（还原对称性）-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-327"
knowledge:
  - "定积分"
  - "定积分等式"
  - "定积分性质"
  - "根式积分"
error_causes:
  - "触发信息遗漏"
  - "方法调取失败"
methods:
  - "配方平移"
  - "还原对称性"
  - "奇偶性消项"
  - "数形结合"
  - "半圆面积"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-058_根式积分"
  - "MATHWIKI-KNOWLEDGE-084_定积分等式"
  - "MATHWIKI-METHOD-CLUSTER-071_数形结合"
  - "MATHWIKI-METHOD-CLUSTER-1350_还原对称性"
  - "MATHWIKI-METHOD-CLUSTER-1388_配方平移"
  - "MATHWIKI-METHOD-CLUSTER-350_奇偶性消项"
  - "MATHWIKI-METHOD-CLUSTER-723_半圆面积"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-327 强化例题11.12（还原对称性）-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-327_强化例题11.12（还原对称性）-2.md`
- wrongnet ID：`GS-327`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 定积分计算 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分等式
- 定积分性质
- 根式积分

### 错因

- 触发信息遗漏
- 方法调取失败

### 方法

- 配方平移
- 还原对称性
- 奇偶性消项
- 数形结合
- 半圆面积

### 陷阱

- 未先配方找结构中心
- 对称区间奇项未消
- 半圆面积后漏乘外层系数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先令 \(t=x-2\)，把 \(4x-x^2\) 改写成 \(4-t^2\) 并同步改上下限 |
| missed_action | 没有先配方找结构中心并转成对称区间 |
| related_method_card_id | H09-009 |
| next_reminder | 看到根号二次式定积分，先配方找中心，再判断半圆面积和奇偶性。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-058_根式积分]]
- [[MATHWIKI-KNOWLEDGE-084_定积分等式]]
- [[MATHWIKI-METHOD-CLUSTER-071_数形结合]]
- [[MATHWIKI-METHOD-CLUSTER-1350_还原对称性]]
- [[MATHWIKI-METHOD-CLUSTER-1388_配方平移]]
- [[MATHWIKI-METHOD-CLUSTER-350_奇偶性消项]]
- [[MATHWIKI-METHOD-CLUSTER-723_半圆面积]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
