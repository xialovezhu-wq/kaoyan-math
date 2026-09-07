---
wiki_id: SRC-WQ-GS-147
type: source_summary
title: "GS-147 1000题B组5.43"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-147_1000题B组5.43.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-147"
knowledge:
  - "一元函数微分学应用"
  - "切线方程"
  - "曲率"
  - "曲率圆"
error_causes:
  - "已掌握题历史首错未记录；当前仅确认复做断点是曲率圆题未先判断曲线应按 x=x(y) 处理，需用户复做确认。"
methods:
  - "曲率公式"
  - "数形结合"
  - "变量互换"
  - "曲率半径"
  - "法线方向定圆心"
  - "圆方程"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-204_已掌握题历史首错未记录-当前仅确认复做断点是曲率圆题未先判断曲线应按x="
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-081_切线方程"
  - "MATHWIKI-KNOWLEDGE-094_曲率"
  - "MATHWIKI-KNOWLEDGE-260_曲率圆"
  - "MATHWIKI-METHOD-CLUSTER-071_数形结合"
  - "MATHWIKI-METHOD-CLUSTER-096_曲率公式"
  - "MATHWIKI-METHOD-CLUSTER-210_变量互换"
  - "MATHWIKI-METHOD-CLUSTER-216_圆方程"
  - "MATHWIKI-METHOD-CLUSTER-241_法线方向定圆心"
  - "MATHWIKI-METHOD-CLUSTER-385_曲率半径"
  - "MATHWIKI-GS-METHOD-047_曲率题变量对象判别链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-148"
formal_projection_sha256: 3ce032a26c4dcc1d421db8bb6ea43dfb4042df68e8c504e957d42e19e167f1e2
---

# GS-147 1000题B组5.43

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-147_1000题B组5.43.md`
- wrongnet ID：`GS-147`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 曲率圆与曲率半径 |
| 日期 | 2026-05-07 |
| 状态 | 已掌握 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 切线方程
- 曲率
- 曲率圆

### 错因

- 已掌握题历史首错未记录；当前仅确认复做断点是曲率圆题未先判断曲线应按 x=x(y) 处理，需用户复做确认。

### 方法

- 曲率公式
- 数形结合
- 变量互换
- 曲率半径
- 法线方向定圆心
- 圆方程

### 陷阱

- x=y² 要按 x 关于 y 的曲率处理
- 圆心方向

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先把 x=y^2 看成 x 关于 y 的函数并计算 x'(0)、x''(0) |
| missed_action | 旧批量未记录个人步骤；当前复做风险是硬套 y=y(x) 型曲率公式或圆心方向判断不清 |
| related_method_card_id | H05-007 |
| next_reminder | 看到曲率圆题，先判断用 y=y(x) 还是 x=x(y)，再算曲率半径和圆心方向。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-204_已掌握题历史首错未记录-当前仅确认复做断点是曲率圆题未先判断曲线应按x=]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-081_切线方程]]
- [[MATHWIKI-KNOWLEDGE-094_曲率]]
- [[MATHWIKI-KNOWLEDGE-260_曲率圆]]
- [[MATHWIKI-METHOD-CLUSTER-071_数形结合]]
- [[MATHWIKI-METHOD-CLUSTER-096_曲率公式]]
- [[MATHWIKI-METHOD-CLUSTER-210_变量互换]]
- [[MATHWIKI-METHOD-CLUSTER-216_圆方程]]
- [[MATHWIKI-METHOD-CLUSTER-241_法线方向定圆心]]
- [[MATHWIKI-METHOD-CLUSTER-385_曲率半径]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-047_曲率题变量对象判别链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-148

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
