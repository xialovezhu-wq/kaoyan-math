---
wiki_id: SRC-WQ-GS-351
type: source_summary
title: "GS-351 强化例题13.12"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-351_强化例题13.12.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-351"
knowledge:
  - "多元函数微分学"
  - "多元函数偏导"
  - "多元函数连续可微"
  - "可微定义"
  - "极限与连续"
error_causes:
  - "概念边界混淆"
  - "动作链断裂"
methods:
  - "偏导定义"
  - "特殊路径"
  - "可微定义"
  - "有界性放缩"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-005_A-CONCEPT"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-027_概念边界混淆"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-KNOWLEDGE-037_多元函数连续可微"
  - "MATHWIKI-KNOWLEDGE-072_可微定义"
  - "MATHWIKI-METHOD-CLUSTER-022_特殊路径"
  - "MATHWIKI-METHOD-CLUSTER-029_偏导定义"
  - "MATHWIKI-METHOD-CLUSTER-031_有界性放缩"
  - "MATHWIKI-METHOD-CLUSTER-041_可微定义"
  - "MATHWIKI-GS-METHOD-050_二元函数性质定义判别链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-351 强化例题13.12

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-351_强化例题13.12.md`
- wrongnet ID：`GS-351`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 可微性与偏导连续性判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数微分学
- 多元函数偏导
- 多元函数连续可微
- 可微定义
- 极限与连续

### 错因

- 概念边界混淆
- 动作链断裂

### 方法

- 偏导定义
- 特殊路径
- 可微定义
- 有界性放缩

### 陷阱

- 把偏导连续当成可微必要条件
- 只算原点偏导不查邻域偏导
- 可微定义中未除以 rho 检验

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-CONCEPT |
| expected_first_action | 先用偏导定义计算原点偏导，再写可微定义余项 |
| missed_action | 旧批量卡未记录用户个人错因；低置信推断为没有先把偏导连续性与可微性拆开逐项核验 |
| related_method_card_id | H13-005 |
| next_reminder | 看到二元函数性质判断，先拆连续、偏导、可微、偏导连续四件事，再逐项回定义。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-005_A-CONCEPT]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-027_概念边界混淆]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-KNOWLEDGE-037_多元函数连续可微]]
- [[MATHWIKI-KNOWLEDGE-072_可微定义]]
- [[MATHWIKI-METHOD-CLUSTER-022_特殊路径]]
- [[MATHWIKI-METHOD-CLUSTER-029_偏导定义]]
- [[MATHWIKI-METHOD-CLUSTER-031_有界性放缩]]
- [[MATHWIKI-METHOD-CLUSTER-041_可微定义]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-050_二元函数性质定义判别链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-358

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
