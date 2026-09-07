---
wiki_id: SRC-WQ-GS-069
type: source_summary
title: "GS-069 58049 2026.4.18"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-069_580492026.4.18.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-069"
knowledge:
  - "极限与连续"
  - "数列极限"
  - "根式有理化"
  - "主导项"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是先把相邻和式写成等差求和公式，再对根式差有理化并比较主导项，需用户复做确认是否为当时第一断点。"
methods:
  - "等差数列求和"
  - "根式有理化"
  - "主导项比较"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-279_旧批量未记录个人原始错因-当前仅确认复做入口是先把相邻和式写成等差求和公"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-086_主导项"
  - "MATHWIKI-KNOWLEDGE-154_根式有理化"
  - "MATHWIKI-METHOD-CLUSTER-021_主导项比较"
  - "MATHWIKI-METHOD-CLUSTER-412_根式有理化"
  - "MATHWIKI-METHOD-CLUSTER-450_等差数列求和"
  - "MATHWIKI-GS-METHOD-091_相邻和式根式差有理化"
  - "MATHWIKI-GS-TOPIC-007_数列极限错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-069 58049 2026.4.18

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-069_580492026.4.18.md`
- wrongnet ID：`GS-069`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 相邻根式作差数列极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 2 |

## 可编译信息

### 知识点

- 极限与连续
- 数列极限
- 根式有理化
- 主导项

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是先把相邻和式写成等差求和公式，再对根式差有理化并比较主导项，需用户复做确认是否为当时第一断点。

### 方法

- 等差数列求和
- 根式有理化
- 主导项比较

### 陷阱

- 相邻和式
- 根式差
- 最高阶量

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先写 \(1+\cdots+n=\frac{n(n+1)}2\) 和 \(1+\cdots+(n-1)=\frac{n(n-1)}2\)。 |
| missed_action | 个人原始作答未记录；当前只把题图解析确认的求和和有理化入口登记为复做检查点。 |
| related_method_card_id | H01-006 |
| next_reminder | 看到相邻和式根式差，先求和，再有理化，不要直接凭阶数猜。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-279_旧批量未记录个人原始错因-当前仅确认复做入口是先把相邻和式写成等差求和公]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-086_主导项]]
- [[MATHWIKI-KNOWLEDGE-154_根式有理化]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]
- [[MATHWIKI-METHOD-CLUSTER-412_根式有理化]]
- [[MATHWIKI-METHOD-CLUSTER-450_等差数列求和]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-091_相邻和式根式差有理化]]
- [[MATHWIKI-GS-TOPIC-007_数列极限错题总线]]

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
