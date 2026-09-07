---
wiki_id: SRC-WQ-GS-360
type: source_summary
title: "GS-360 强化例题13.11"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-360_强化例题13.11.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-360"
knowledge:
  - "多元函数微分学"
  - "多元函数连续可微"
  - "多元函数偏导"
  - "极限与连续"
  - "可微定义"
error_causes:
  - "定义入口待确认"
  - "概念边界待确认"
  - "题型识别待确认"
methods:
  - "先判性质"
  - "特殊路径"
  - "偏导定义"
  - "邻域偏导存在性检查"
  - "可微定义"
  - "概念关系判别"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-006_B1-GOAL"
  - "MATHWIKI-ERROR-CLUSTER-031_概念边界待确认"
  - "MATHWIKI-ERROR-CLUSTER-062_题型识别待确认"
  - "MATHWIKI-ERROR-CLUSTER-076_定义入口待确认"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-KNOWLEDGE-037_多元函数连续可微"
  - "MATHWIKI-KNOWLEDGE-072_可微定义"
  - "MATHWIKI-METHOD-CLUSTER-022_特殊路径"
  - "MATHWIKI-METHOD-CLUSTER-029_偏导定义"
  - "MATHWIKI-METHOD-CLUSTER-041_可微定义"
  - "MATHWIKI-METHOD-CLUSTER-295_先判性质"
  - "MATHWIKI-METHOD-CLUSTER-413_概念关系判别"
  - "MATHWIKI-METHOD-CLUSTER-469_邻域偏导存在性检查"
  - "MATHWIKI-GS-METHOD-050_二元函数性质定义判别链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-360 强化例题13.11

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-360_强化例题13.11.md`
- wrongnet ID：`GS-360`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 二元分段函数连续性、偏导存在性与可微性判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数微分学
- 多元函数连续可微
- 多元函数偏导
- 极限与连续
- 可微定义

### 错因

- 定义入口待确认
- 概念边界待确认
- 题型识别待确认

### 方法

- 先判性质
- 特殊路径
- 偏导定义
- 邻域偏导存在性检查
- 可微定义
- 概念关系判别

### 陷阱

- 原点偏导存在不推出连续
- 函数不连续必不可微
- 偏导连续要看邻域是否处处存在并趋于原点偏导值
- 二重极限要看所有路径

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B1-GOAL |
| expected_first_action | 先判断题目问的是哪一种性质，再按连续、偏导、偏导连续、可微分别回到定义 |
| missed_action | 缺少用户作答过程；低置信推断可能把原点偏导存在当成连续或可微信号 |
| related_method_card_id | H13-005 |
| next_reminder | 看到二元函数性质题，先问清连续、偏导、偏导连续还是可微，再回对应定义。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-006_B1-GOAL]]
- [[MATHWIKI-ERROR-CLUSTER-031_概念边界待确认]]
- [[MATHWIKI-ERROR-CLUSTER-062_题型识别待确认]]
- [[MATHWIKI-ERROR-CLUSTER-076_定义入口待确认]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-KNOWLEDGE-037_多元函数连续可微]]
- [[MATHWIKI-KNOWLEDGE-072_可微定义]]
- [[MATHWIKI-METHOD-CLUSTER-022_特殊路径]]
- [[MATHWIKI-METHOD-CLUSTER-029_偏导定义]]
- [[MATHWIKI-METHOD-CLUSTER-041_可微定义]]
- [[MATHWIKI-METHOD-CLUSTER-295_先判性质]]
- [[MATHWIKI-METHOD-CLUSTER-413_概念关系判别]]
- [[MATHWIKI-METHOD-CLUSTER-469_邻域偏导存在性检查]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-050_二元函数性质定义判别链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-373
- GS-350
- GS-354
- GS-356
- GS-363
- GS-626

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
