---
wiki_id: SRC-WQ-GS-019
type: source_summary
title: "GS-019 58018 2026.4.16"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-019_580182026.4.16.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-019"
knowledge:
  - "极限与连续"
  - "等价无穷小"
  - "无穷大量比较"
  - "数列极限"
  - "一元函数微分学应用"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是无穷大分式先同除最高阶，再把三角扰动压成有界量乘无穷小"
methods:
  - "单调有界"
  - "等价变形"
  - "单调有界准则"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-294_旧批量未记录个人原始错因-当前仅确认复做入口是无穷大分式先同除最高阶-再"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-150_无穷大量比较"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-010_单调有界准则"
  - "MATHWIKI-METHOD-CLUSTER-017_单调有界"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-019 58018 2026.4.16

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-019_580182026.4.16.md`
- wrongnet ID：`GS-019`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 无穷小阶数比较 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 等价无穷小
- 无穷大量比较
- 数列极限
- 一元函数微分学应用

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是无穷大分式先同除最高阶，再把三角扰动压成有界量乘无穷小

### 方法

- 单调有界
- 等价变形
- 单调有界准则

### 陷阱

- 定义域
- 量纲/阶数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先上下同除最高阶 \(x^2\)，把 \(x\sin x/x^2\) 改成 \(\sin x/x\) |
| missed_action | 个人原始漏步未记录；当前只确认复做时不要把三角扰动当作同阶主项，必须先抓最高阶 |
| related_method_card_id | H01-007 |
| next_reminder | 无穷大分式极限先抓最高阶；遇到 \(\sin x\) 这类有界振荡项，要制造趋零因子压掉。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-294_旧批量未记录个人原始错因-当前仅确认复做入口是无穷大分式先同除最高阶-再]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-150_无穷大量比较]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-010_单调有界准则]]
- [[MATHWIKI-METHOD-CLUSTER-017_单调有界]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-020
- GS-028
- GS-349

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
