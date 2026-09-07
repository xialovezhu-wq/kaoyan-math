---
wiki_id: SRC-WQ-GS-239
type: source_summary
title: "GS-239 强化例题6.17"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-239_强化例题6.17.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-239"
knowledge:
  - "一元函数微分学应用"
  - "单调性与极值"
  - "凹凸性与拐点"
  - "零点定理"
error_causes:
  - "旧批量未记录个人原始错因；当前可确认的复做断点是没有先把 \\(a>0\\) 归一化并令 \\(t=b/a\\)，导致零点个数无法转成极小值判定。"
methods:
  - "参数化"
  - "导数判极值"
  - "端点极限"
  - "凸函数最小值"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-348_旧批量未记录个人原始错因-当前可确认的复做断点是没有先把-a-0-归一化"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-018_凹凸性与拐点"
  - "MATHWIKI-KNOWLEDGE-042_零点定理"
  - "MATHWIKI-METHOD-CLUSTER-081_导数判极值"
  - "MATHWIKI-METHOD-CLUSTER-252_端点极限"
  - "MATHWIKI-METHOD-CLUSTER-647_凸函数最小值"
  - "MATHWIKI-METHOD-CLUSTER-750_参数化"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-239 强化例题6.17

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-239_强化例题6.17.md`
- wrongnet ID：`GS-239`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 零点个数参数范围 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 单调性与极值
- 凹凸性与拐点
- 零点定理

### 错因

- 旧批量未记录个人原始错因；当前可确认的复做断点是没有先把 \(a>0\) 归一化并令 \(t=b/a\)，导致零点个数无法转成极小值判定。

### 方法

- 参数化
- 导数判极值
- 端点极限
- 凸函数最小值

### 陷阱

- a大于0可除
- t=e只有一个切点
- 两端极限都为正无穷

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先令 \(t=b/a\)，构造 \(g(x)=x-t\ln x\)。 |
| missed_action | 旧批量未记录原始作答；当前复做入口显示容易漏掉除以 \(a\) 后只研究 \(b/a\)。 |
| related_method_card_id | H06-009 |
| next_reminder | 看到含参数零点个数，先归一化参数，再用端点极限和极值判根数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-348_旧批量未记录个人原始错因-当前可确认的复做断点是没有先把-a-0-归一化]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-018_凹凸性与拐点]]
- [[MATHWIKI-KNOWLEDGE-042_零点定理]]
- [[MATHWIKI-METHOD-CLUSTER-081_导数判极值]]
- [[MATHWIKI-METHOD-CLUSTER-252_端点极限]]
- [[MATHWIKI-METHOD-CLUSTER-647_凸函数最小值]]
- [[MATHWIKI-METHOD-CLUSTER-750_参数化]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-240
- GS-255
- GS-513
- GS-241
- GS-244

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
