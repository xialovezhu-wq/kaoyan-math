---
wiki_id: SRC-WQ-GS-144
type: source_summary
title: "GS-144 1000题B组5.12"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-144_1000题B组5.12.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-144"
knowledge:
  - "一元函数微分学应用"
  - "单调性与极值"
  - "二阶导数判极值"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是没有把一阶导为 0 的条件代回方程先判断二阶导符号，需用户复做确认。"
methods:
  - "二阶充分条件"
  - "方程代点"
  - "符号判断"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-340_旧批量未记录个人原始错因-当前仅确认复做断点是没有把一阶导为0的条件代回"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-296_二阶导数判极值"
  - "MATHWIKI-METHOD-CLUSTER-1057_方程代点"
  - "MATHWIKI-METHOD-CLUSTER-254_符号判断"
  - "MATHWIKI-METHOD-CLUSTER-560_二阶充分条件"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-156"
formal_projection_sha256: ef40d0a48ced672e2ff023ea61f94355ae79f5b92ee893b0ec1fd884fcd12f30
---

# GS-144 1000题B组5.12

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-144_1000题B组5.12.md`
- wrongnet ID：`GS-144`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 二阶充分条件判断极值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 单调性与极值
- 二阶导数判极值

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是没有把一阶导为 0 的条件代回方程先判断二阶导符号，需用户复做确认。

### 方法

- 二阶充分条件
- 方程代点
- 符号判断

### 陷阱

- $x_0\ne0$ 才能除以 $x_0$
- 极小值不是拐点

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把 x=x0 与 f'(x0)=0 代入原方程 |
| missed_action | 旧批量未记录个人步骤；当前复做风险是没有先代点或没有分 x0 正负判断符号 |
| related_method_card_id | H05-003 |
| next_reminder | 看到 f'(x0)=0 且方程含 f''，先代点求 f''(x0) 符号，再判极值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-340_旧批量未记录个人原始错因-当前仅确认复做断点是没有把一阶导为0的条件代回]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-296_二阶导数判极值]]
- [[MATHWIKI-METHOD-CLUSTER-1057_方程代点]]
- [[MATHWIKI-METHOD-CLUSTER-254_符号判断]]
- [[MATHWIKI-METHOD-CLUSTER-560_二阶充分条件]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-156

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
