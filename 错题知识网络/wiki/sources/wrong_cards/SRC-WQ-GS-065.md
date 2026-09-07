---
wiki_id: SRC-WQ-GS-065
type: source_summary
title: "GS-065 1000题强化2.4"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-065_1000题强化2.4.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-065"
knowledge:
  - "极限与连续"
  - "数列极限"
  - "递推数列"
  - "固定点方程"
  - "零点定理"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是先构造 \\(g(x)=f(x)-x\\) 证明唯一不动点，再比较迭代项到不动点的距离，需用户复做确认是否为当时第一…"
methods:
  - "零点定理"
  - "构造辅助函数"
  - "单调有界"
  - "固定点方程"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-282_旧批量未记录个人原始错因-当前仅确认复做入口是先构造-g-x-=f-x-"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-042_零点定理"
  - "MATHWIKI-KNOWLEDGE-053_递推数列"
  - "MATHWIKI-KNOWLEDGE-121_固定点方程"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-017_单调有界"
  - "MATHWIKI-METHOD-CLUSTER-039_零点定理"
  - "MATHWIKI-METHOD-CLUSTER-114_固定点方程"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-019_压缩映射不动点迭代"
  - "MATHWIKI-GS-TOPIC-007_数列极限错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-065 1000题强化2.4

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-065_1000题强化2.4.md`
- wrongnet ID：`GS-065`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 压缩映射不动点收敛证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 数列极限
- 递推数列
- 固定点方程
- 零点定理

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是先构造 \(g(x)=f(x)-x\) 证明唯一不动点，再比较迭代项到不动点的距离，需用户复做确认是否为当时第一…

### 方法

- 零点定理
- 构造辅助函数
- 单调有界
- 固定点方程

### 陷阱

- 唯一不动点
- 严格压缩不等式
- 同侧性保持

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先令 \(g(x)=f(x)-x\)，用端点异号和压缩不等式证明唯一根 \(\xi\)。 |
| missed_action | 个人原始作答未记录；当前只把题图解析确认的不动点入口登记为复做检查点。 |
| related_method_card_id | H02-002 |
| next_reminder | 看到压缩不等式和迭代平均式，先找唯一不动点，再比较到不动点的距离。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-282_旧批量未记录个人原始错因-当前仅确认复做入口是先构造-g-x-=f-x-]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-042_零点定理]]
- [[MATHWIKI-KNOWLEDGE-053_递推数列]]
- [[MATHWIKI-KNOWLEDGE-121_固定点方程]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-017_单调有界]]
- [[MATHWIKI-METHOD-CLUSTER-039_零点定理]]
- [[MATHWIKI-METHOD-CLUSTER-114_固定点方程]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-019_压缩映射不动点迭代]]
- [[MATHWIKI-GS-TOPIC-007_数列极限错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-054
- GS-070
- GS-434

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
