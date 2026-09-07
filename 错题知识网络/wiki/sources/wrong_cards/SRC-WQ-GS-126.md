---
wiki_id: SRC-WQ-GS-126
type: source_summary
title: "GS-126 25882 2026.2.28 T1"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-126_258822026.2.28T1.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-126"
knowledge:
  - "一元函数微分学应用"
  - "反函数求导"
  - "单调性与极值"
error_causes:
  - "方法论调取失败"
  - "动作链断裂"
methods:
  - "反函数求法"
  - "构造倒数消根号"
  - "单调性和值域"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-140_反函数求导"
  - "MATHWIKI-METHOD-CLUSTER-1124_构造倒数消根号"
  - "MATHWIKI-METHOD-CLUSTER-326_反函数求法"
  - "MATHWIKI-METHOD-CLUSTER-733_单调性和值域"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-126 25882 2026.2.28 T1

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-126_258822026.2.28T1.md`
- wrongnet ID：`GS-126`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学的计算 |
| 题型 | 反函数求表达式与定义域 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 反函数求导
- 单调性与极值

### 错因

- 方法论调取失败
- 动作链断裂

### 方法

- 反函数求法
- 构造倒数消根号
- 单调性和值域

### 陷阱

- 取指数后卡住
- 直接平方易增根
- 忘记反函数定义域等于原函数值域

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先由 $e^y=x+\sqrt{x^2+1}$ 构造 $e^{-y}=\sqrt{x^2+1}-x$，再相减解出 $x$。 |
| missed_action | 取指数后没有继续构造倒数消根号。 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到 $\ln(x+\sqrt{x^2+1})$，先取指数，再构造倒数 $e^{-y}$ 消根号。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-140_反函数求导]]
- [[MATHWIKI-METHOD-CLUSTER-1124_构造倒数消根号]]
- [[MATHWIKI-METHOD-CLUSTER-326_反函数求法]]
- [[MATHWIKI-METHOD-CLUSTER-733_单调性和值域]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-134
- GS-141
- GS-641
- GS-643

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
