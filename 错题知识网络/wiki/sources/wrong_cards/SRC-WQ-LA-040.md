---
wiki_id: SRC-WQ-LA-040
type: source_summary
title: "LA-040 合同与相似判定"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-040_强化例题9.10.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-040"
knowledge:
  - "二次型"
  - "实对称矩阵"
  - "相似矩阵"
  - "特征值与特征向量"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "合同判定"
  - "惯性指数"
  - "相似矩阵判定"
  - "特征分解"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-005_A-CONCEPT"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-016_特征值与特征向量"
  - "MATHWIKI-KNOWLEDGE-034_二次型"
  - "MATHWIKI-KNOWLEDGE-040_相似矩阵"
  - "MATHWIKI-KNOWLEDGE-056_实对称矩阵"
  - "MATHWIKI-METHOD-CLUSTER-023_特征分解"
  - "MATHWIKI-METHOD-CLUSTER-1222_相似矩阵判定"
  - "MATHWIKI-METHOD-CLUSTER-228_惯性指数"
  - "MATHWIKI-METHOD-CLUSTER-819_合同判定"
  - "MATHWIKI-LA-METHOD-007_二次型合同相似与正定平方根"
  - "MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线"
status: indexed
last_updated: 2026-07-15
---

# LA-040 合同与相似判定

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-040_强化例题9.10.md`
- wrongnet ID：`LA-040`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 二次型 |
| 题型 | 合同与相似判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二次型
- 实对称矩阵
- 相似矩阵
- 特征值与特征向量

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 合同判定
- 惯性指数
- 相似矩阵判定
- 特征分解

### 陷阱

- 合同不要求特征值相同，只要求同阶实对称矩阵的正负惯性指数相同。
- 相似必须保留特征值；特征值不同就不相似。
- 不能因为两个矩阵秩相同就直接判相似。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-CONCEPT |
| expected_first_action | 先分别列出合同判据和相似判据，不能混用 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是把合同当成相似，或用特征值去判断合同充分性 |
| related_method_card_id | L09-008 |
| next_reminder | 看到合同和相似同题出现，先分清：合同看惯性指数，相似看特征值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-005_A-CONCEPT]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-016_特征值与特征向量]]
- [[MATHWIKI-KNOWLEDGE-034_二次型]]
- [[MATHWIKI-KNOWLEDGE-040_相似矩阵]]
- [[MATHWIKI-KNOWLEDGE-056_实对称矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-023_特征分解]]
- [[MATHWIKI-METHOD-CLUSTER-1222_相似矩阵判定]]
- [[MATHWIKI-METHOD-CLUSTER-228_惯性指数]]
- [[MATHWIKI-METHOD-CLUSTER-819_合同判定]]

### 深度编译页

- [[MATHWIKI-LA-METHOD-007_二次型合同相似与正定平方根]]
- [[MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-041
- LA-044

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
