---
wiki_id: SRC-WQ-GS-011
type: source_summary
title: "GS-011 58018 2026.4.18-2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-011_580182026.4.18-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-011"
knowledge:
  - "极限与连续"
  - "等价无穷小"
  - "洛必达法则"
  - "幂指极限"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是先保留右极限定义域，再把底数含 \\(x\\) 的幂指式指数化"
methods:
  - "等价变形"
  - "洛必达"
  - "取对数"
  - "条件转化"
  - "分类讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-273_旧批量未记录个人原始错因-当前仅确认复做入口是先保留右极限定义域-再把底"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-017_幂指极限"
  - "MATHWIKI-KNOWLEDGE-045_洛必达法则"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-019_取对数"
  - "MATHWIKI-METHOD-CLUSTER-034_洛必达"
  - "MATHWIKI-GS-METHOD-007_条件转化总流程"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-011 58018 2026.4.18-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-011_580182026.4.18-2.md`
- wrongnet ID：`GS-011`
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
- 洛必达法则
- 幂指极限

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是先保留右极限定义域，再把底数含 \(x\) 的幂指式指数化

### 方法

- 等价变形
- 洛必达
- 取对数
- 条件转化
- 分类讨论

### 陷阱

- 定义域
- 左右极限
- 适用条件
- 极限过程

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先确认 \(x\to0^+\) 时 \(x>0\)，再写 \(x^{\sin x}=e^{\sin x\ln x}\) |
| missed_action | 个人原始漏步未记录；当前只确认复做时必须先保留右极限定义域，再做幂指指数化 |
| related_method_card_id | H01-002 |
| next_reminder | 看到底数含 \(x\) 的幂指极限，先确认底数为正，再写成 \(e^{g(x)\ln f(x)}\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-273_旧批量未记录个人原始错因-当前仅确认复做入口是先保留右极限定义域-再把底]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-017_幂指极限]]
- [[MATHWIKI-KNOWLEDGE-045_洛必达法则]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-019_取对数]]
- [[MATHWIKI-METHOD-CLUSTER-034_洛必达]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-007_条件转化总流程]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-010
- GS-009
- GS-033

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
