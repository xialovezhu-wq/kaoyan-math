---
wiki_id: SRC-WQ-LA-067
type: source_summary
title: "LA-067 满行秩右消判断"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-067_强化例题4.2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-067"
knowledge:
  - "矩阵秩"
  - "矩阵运算"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "满秩消去"
  - "矩阵秩判断"
  - "矩阵乘法结构"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-014_矩阵运算"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断"
  - "MATHWIKI-METHOD-CLUSTER-424_满秩消去"
  - "MATHWIKI-METHOD-CLUSTER-436_矩阵乘法结构"
  - "MATHWIKI-LA-METHOD-013_矩阵秩约束与分块秩比较"
  - "MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线"
status: indexed
last_updated: 2026-07-15
---

# LA-067 满行秩右消判断

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-067_强化例题4.2.md`
- wrongnet ID：`LA-067`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 矩阵秩 |
| 题型 | 满行秩消去判断 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 矩阵秩
- 矩阵运算

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 满秩消去
- 矩阵秩判断
- 矩阵乘法结构

### 陷阱

- \(C\) 是 \(n\times m\) 且 \(r(C)=n\)，是行满秩，不是列满秩。
- \(BC=O\) 等价于 \(BC=OC\)，右消 \(C\) 后得到 \(B=O\)，所以 \(r(B)=0\)。
- \(BC=C\) 等价于 \(BC=EC\)，右消 \(C\) 后得到 \(B=E\)，因此 \(r(B)=n\)。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先确认 \(C\) 行满秩，因此 \(AC=BC\Rightarrow A=B\) 可右消 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有先核对满行秩条件，导致右消或不可消的判断混淆 |
| related_method_card_id | L04-002 |
| next_reminder | 看到右乘满行秩矩阵，先确认满秩方向，再决定能否右消。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断]]
- [[MATHWIKI-METHOD-CLUSTER-424_满秩消去]]
- [[MATHWIKI-METHOD-CLUSTER-436_矩阵乘法结构]]

### 深度编译页

- [[MATHWIKI-LA-METHOD-013_矩阵秩约束与分块秩比较]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-068
- LA-069
- LA-071
- LA-072

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
