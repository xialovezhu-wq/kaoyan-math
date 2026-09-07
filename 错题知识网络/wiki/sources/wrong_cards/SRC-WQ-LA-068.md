---
wiki_id: SRC-WQ-LA-068
type: source_summary
title: "LA-068 AB平方反推BA"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-068_强化例题4.3-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-068"
knowledge:
  - "矩阵秩"
  - "矩阵运算"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "矩阵秩判断"
  - "矩阵乘法结构"
  - "满秩消去"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-014_矩阵运算"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断"
  - "MATHWIKI-METHOD-CLUSTER-424_满秩消去"
  - "MATHWIKI-METHOD-CLUSTER-436_矩阵乘法结构"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-LA-METHOD-013_矩阵秩约束与分块秩比较"
  - "MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# LA-068 AB平方反推BA

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-068_强化例题4.3-2.md`
- wrongnet ID：`LA-068`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 矩阵秩 |
| 题型 | 矩阵乘积秩约束 |
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

- 矩阵秩判断
- 矩阵乘法结构
- 满秩消去

### 陷阱

- \(A\) 是 \(3\times2\) 矩阵、\(B\) 是 \(2\times3\) 矩阵，不能像方阵一样直接左右消去。
- 先算 \((AB)^2\)，再把 \(ABAB\) 改写成 \(A(BA)B\)。
- 满秩消去必须建立在 \(r(A)=r(B)=2\) 的基础上。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先计算或判断 \(r(AB)\) 与 \((AB)^2\)，再写 \(ABAB=A(BA)B\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是把非方阵乘积直接互推，没有先建立满列秩和满行秩消去条件 |
| related_method_card_id | L04-002 |
| next_reminder | 看到已知 \(AB\) 求 \(BA\)，先查秩和平方关系，再用 \(ABAB=A(BA)B\) 连接。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断]]
- [[MATHWIKI-METHOD-CLUSTER-424_满秩消去]]
- [[MATHWIKI-METHOD-CLUSTER-436_矩阵乘法结构]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-LA-METHOD-013_矩阵秩约束与分块秩比较]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-070
- LA-073

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
