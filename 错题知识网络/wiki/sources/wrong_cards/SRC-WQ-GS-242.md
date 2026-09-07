---
wiki_id: SRC-WQ-GS-242
type: source_summary
title: "GS-242 1000题B组6.19"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-242_1000题B组6.19.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-242"
knowledge:
  - "极限与连续"
  - "一元函数微分学应用"
  - "单调性与极值"
  - "参数范围"
error_causes:
  - "旧批量未记录个人原始错因；当前可确认的复做断点是没有先把“处处连续”翻译为分母恒不为零并求 \\(xe^{-x}\\) 的值域。"
methods:
  - "分母无零点"
  - "导数判极值"
  - "值域分析"
  - "介值定理"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-349_旧批量未记录个人原始错因-当前可确认的复做断点是没有先把“处处连续”翻译"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-100_参数范围"
  - "MATHWIKI-METHOD-CLUSTER-081_导数判极值"
  - "MATHWIKI-METHOD-CLUSTER-140_介值定理"
  - "MATHWIKI-METHOD-CLUSTER-604_值域分析"
  - "MATHWIKI-METHOD-CLUSTER-681_分母无零点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-242 1000题B组6.19

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-242_1000题B组6.19.md`
- wrongnet ID：`GS-242`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 连续性参数范围 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 一元函数微分学应用
- 单调性与极值
- 参数范围

### 错因

- 旧批量未记录个人原始错因；当前可确认的复做断点是没有先把“处处连续”翻译为分母恒不为零并求 \(xe^{-x}\) 的值域。

### 方法

- 分母无零点
- 导数判极值
- 值域分析
- 介值定理

### 陷阱

- a=e^{-1}也会断点
- 最大值在x=1
- 左端趋负无穷

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先令 \(h(x)=xe^{-x}\)，把分母不为零转成 \(a\) 不落入 \(h\) 的值域。 |
| missed_action | 旧批量未记录原始作答；当前复做入口显示容易只局部看分母而没有整体求 \(xe^{-x}\) 的值域。 |
| related_method_card_id | H01-008 |
| next_reminder | 看到分式函数处处连续，先让分母恒不为零，再求分母中非参数部分的值域。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-349_旧批量未记录个人原始错因-当前可确认的复做断点是没有先把“处处连续”翻译]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-100_参数范围]]
- [[MATHWIKI-METHOD-CLUSTER-081_导数判极值]]
- [[MATHWIKI-METHOD-CLUSTER-140_介值定理]]
- [[MATHWIKI-METHOD-CLUSTER-604_值域分析]]
- [[MATHWIKI-METHOD-CLUSTER-681_分母无零点]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
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
