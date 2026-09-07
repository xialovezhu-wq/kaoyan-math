---
wiki_id: SRC-WQ-GS-029
type: source_summary
title: "GS-029 58018 2026.4.17 ✅2026.5.7"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-029_580182026.4.17✅2026.5.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-029"
knowledge:
  - "极限与连续"
  - "等价无穷小"
  - "幂指极限"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是对数差先合并成 \\(\\ln(1+u)\\)，再比较二阶小量"
methods:
  - "等价变形"
  - "取对数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-286_旧批量未记录个人原始错因-当前仅确认复做入口是对数差先合并成-ln-1+"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-017_幂指极限"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-019_取对数"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-029 58018 2026.4.17 ✅2026.5.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-029_580182026.4.17✅2026.5.7.md`
- wrongnet ID：`GS-029`
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
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 等价无穷小
- 幂指极限

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是对数差先合并成 \(\ln(1+u)\)，再比较二阶小量

### 方法

- 等价变形
- 取对数

### 陷阱

- 定义域
- 适用条件

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把 \(x\) 写成 \(\ln e^x\)、把 \(2x\) 写成 \(\ln e^{2x}\)，合并对数差 |
| missed_action | 个人原始漏步未记录；当前只确认复做时必须先合并对数，不能直接分别展开到一阶 |
| related_method_card_id | H01-004 |
| next_reminder | 看到对数差 \(\ln A-x\)，先把 \(x\) 改写成 \(\ln e^x\)，合并成 \(\ln(A/e^x)\) 再做等价。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-286_旧批量未记录个人原始错因-当前仅确认复做入口是对数差先合并成-ln-1+]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-017_幂指极限]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-019_取对数]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-009
- GS-033
- GS-030

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
