---
wiki_id: SRC-WQ-GS-113
type: source_summary
title: "GS-113 58068 2026.4.1"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-113_580682026.4.1.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-113"
knowledge:
  - "等价无穷小"
  - "泰勒公式"
  - "无穷小阶数比较"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是 $o(x^3)$ 条件下未把三阶及以下系数全部消掉，需用户复做确认。"
methods:
  - "泰勒展开"
  - "待定系数法"
  - "无穷小阶数比较"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-299_旧批量未记录个人原始错因-当前仅确认复做断点是$o-x^3-$条件下未把"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-KNOWLEDGE-051_无穷小阶数比较"
  - "MATHWIKI-METHOD-CLUSTER-008_泰勒展开"
  - "MATHWIKI-METHOD-CLUSTER-384_无穷小阶数比较"
  - "MATHWIKI-METHOD-CLUSTER-996_待定系数法"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-455"
formal_projection_sha256: 7bc69a7c78c9b20cf64eab21c9dbd8c15631521c846a6e295aac1f402198d904
---

# GS-113 58068 2026.4.1

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-113_580682026.4.1.md`
- wrongnet ID：`GS-113`
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

- 等价无穷小
- 泰勒公式
- 无穷小阶数比较

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是 $o(x^3)$ 条件下未把三阶及以下系数全部消掉，需用户复做确认。

### 方法

- 泰勒展开
- 待定系数法
- 无穷小阶数比较

### 陷阱

- 只消到低阶项
- 漏掉 $x^3$ 同阶项也必须为 0
- 把高阶无穷小误当同阶无穷小

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先写 $\\tan x=x+x^3/3+o(x^3)$ |
| missed_action | 旧批量未记录个人步骤；当前复做风险是只消掉低阶项，漏掉 $x^3$ 同阶系数也必须为 0 |
| related_method_card_id | H01-004 |
| next_reminder | 看到 $o(x^k)$，先展开到 k 阶，并把 k 阶及以下系数全部消掉。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-299_旧批量未记录个人原始错因-当前仅确认复做断点是$o-x^3-$条件下未把]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-KNOWLEDGE-051_无穷小阶数比较]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-384_无穷小阶数比较]]
- [[MATHWIKI-METHOD-CLUSTER-996_待定系数法]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-455

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
