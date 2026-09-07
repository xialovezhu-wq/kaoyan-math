---
wiki_id: SRC-WQ-GS-077
type: source_summary
title: "GS-077 1000题强化2.6"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-077_1000题强化2.6.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-077"
knowledge:
  - "极限与连续"
  - "数列极限"
  - "无穷小阶数比较"
  - "凹凸性与拐点"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是先证明 \\(\\sin x\\) 的线性下界，再给 \\(x_n\\) 建下界并与 \\(y_n\\) 的显式式子比阶，需用…"
methods:
  - "凹凸性证明不等式"
  - "单调有界准则"
  - "比值法"
  - "阶的比较"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-285_旧批量未记录个人原始错因-当前仅确认复做入口是先证明-sinx-的线性下"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-018_凹凸性与拐点"
  - "MATHWIKI-KNOWLEDGE-051_无穷小阶数比较"
  - "MATHWIKI-METHOD-CLUSTER-010_单调有界准则"
  - "MATHWIKI-METHOD-CLUSTER-1403_阶的比较"
  - "MATHWIKI-METHOD-CLUSTER-239_比值法"
  - "MATHWIKI-METHOD-CLUSTER-651_凹凸性证明不等式"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-092_三角隐式根与递推比阶入口链"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-007_数列极限错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-077 1000题强化2.6

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-077_1000题强化2.6.md`
- wrongnet ID：`GS-077`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 双数列高阶无穷小比较证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 数列极限
- 无穷小阶数比较
- 凹凸性与拐点

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是先证明 \(\sin x\) 的线性下界，再给 \(x_n\) 建下界并与 \(y_n\) 的显式式子比阶，需用…

### 方法

- 凹凸性证明不等式
- 单调有界准则
- 比值法
- 阶的比较

### 陷阱

- 线性下界
- 指数与指数的指数
- 高阶无穷小定义

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先用凹凸性或辅助函数证明 \(\sin x>\frac2\pi x\)，并把它转成 \(x_{n+1}>\frac2\pi x_n\)。 |
| missed_action | 个人原始作答未记录；当前只把题图解析确认的线性下界和比阶入口登记为复做检查点。 |
| related_method_card_id | H02-008 |
| next_reminder | 看到双数列比阶，先给慢衰减序列建下界，再写快衰减序列显式式子比较。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-285_旧批量未记录个人原始错因-当前仅确认复做入口是先证明-sinx-的线性下]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-018_凹凸性与拐点]]
- [[MATHWIKI-KNOWLEDGE-051_无穷小阶数比较]]
- [[MATHWIKI-METHOD-CLUSTER-010_单调有界准则]]
- [[MATHWIKI-METHOD-CLUSTER-1403_阶的比较]]
- [[MATHWIKI-METHOD-CLUSTER-239_比值法]]
- [[MATHWIKI-METHOD-CLUSTER-651_凹凸性证明不等式]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-092_三角隐式根与递推比阶入口链]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-007_数列极限错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

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
