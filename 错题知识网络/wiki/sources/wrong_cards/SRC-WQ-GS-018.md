---
wiki_id: SRC-WQ-GS-018
type: source_summary
title: "GS-018 2 58086 2026.3.11 T2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-018_2580862026.3.11T2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-018"
knowledge:
  - "极限与连续"
  - "洛必达法则"
  - "无穷大量比较"
  - "幂指极限"
  - "等价无穷小"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是先写增长阶链并用比值极限验证，而不是凭函数外观排序"
methods:
  - "洛必达"
  - "取对数"
  - "主导项比较"
  - "先判型"
  - "等价变形"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-274_旧批量未记录个人原始错因-当前仅确认复做入口是先写增长阶链并用比值极限验"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-017_幂指极限"
  - "MATHWIKI-KNOWLEDGE-045_洛必达法则"
  - "MATHWIKI-KNOWLEDGE-150_无穷大量比较"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-019_取对数"
  - "MATHWIKI-METHOD-CLUSTER-021_主导项比较"
  - "MATHWIKI-METHOD-CLUSTER-034_洛必达"
  - "MATHWIKI-GS-METHOD-006_先判型总流程"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-018 2 58086 2026.3.11 T2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-018_2580862026.3.11T2.md`
- wrongnet ID：`GS-018`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 幂指函数极限 |
| 日期 | 2026-05-07 |
| 状态 | 已掌握 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 洛必达法则
- 无穷大量比较
- 幂指极限
- 等价无穷小

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是先写增长阶链并用比值极限验证，而不是凭函数外观排序

### 方法

- 洛必达
- 取对数
- 主导项比较
- 先判型
- 等价变形

### 陷阱

- 定义域
- 量纲/阶数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先写增长阶链 \((\ln x)^p\ll x^q\ll a^x\)，再用比值极限验证相邻两项 |
| missed_action | 个人原始漏步未记录；当前只确认复做入口是先做增长阶排序，而不是凭函数外观排序 |
| related_method_card_id | H01-001 |
| next_reminder | 无穷远比较多个函数大小时，先写增长阶链；不确定就用比值极限逐对验证。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-274_旧批量未记录个人原始错因-当前仅确认复做入口是先写增长阶链并用比值极限验]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-017_幂指极限]]
- [[MATHWIKI-KNOWLEDGE-045_洛必达法则]]
- [[MATHWIKI-KNOWLEDGE-150_无穷大量比较]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-019_取对数]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]
- [[MATHWIKI-METHOD-CLUSTER-034_洛必达]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-006_先判型总流程]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

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
