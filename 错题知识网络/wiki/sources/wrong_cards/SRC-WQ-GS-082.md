---
wiki_id: SRC-WQ-GS-082
type: source_summary
title: "GS-082 1000题B组1.33 2026.5.29"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-082_1000题B组1.33.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-082"
knowledge:
  - "泰勒公式"
  - "泰勒展开"
  - "一元函数微分学应用"
error_causes:
  - "概念混淆"
  - "计算细节遗漏"
methods:
  - "有理化"
  - "二项式展开"
  - "泰勒展开"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-007_B7-CALC"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-095_计算细节遗漏"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-KNOWLEDGE-038_泰勒展开"
  - "MATHWIKI-METHOD-CLUSTER-008_泰勒展开"
  - "MATHWIKI-METHOD-CLUSTER-139_二项式展开"
  - "MATHWIKI-METHOD-CLUSTER-235_有理化"
  - "MATHWIKI-GS-METHOD-093_局部展开对象与真实增量匹配"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-25
related_wrongnet_refs: []
formal_projection_sha256: 8cba6411cb18e965792626fc62dea92dd30a3e8a040f40c2d0a43ceedfe6c458
---

# GS-082 1000题B组1.33 2026.5.29

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-082_1000题B组1.33.md`
- wrongnet ID：`GS-082`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 二阶泰勒展开系数判断 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 泰勒公式
- 泰勒展开
- 一元函数微分学应用

### 错因

- 概念混淆
- 计算细节遗漏

### 方法

- 有理化
- 二项式展开
- 泰勒展开

### 陷阱

- 二次项系数除2阶乘
- 根式有理化
- 只保留目标阶数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B7-CALC |
| expected_first_action | 先写 $f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+o(x^2)$。 |
| missed_action | 把 $c$ 直接当成 $f''(0)$，漏掉二次项系数要除 $2!$。 |
| related_method_card_id | 待匹配 |
| next_reminder | 求泰勒多项式系数时，先写通式，再对照系数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-007_B7-CALC]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-095_计算细节遗漏]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-KNOWLEDGE-038_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-139_二项式展开]]
- [[MATHWIKI-METHOD-CLUSTER-235_有理化]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-093_局部展开对象与真实增量匹配]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

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
