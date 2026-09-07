---
wiki_id: SRC-WQ-LA-071
type: source_summary
title: "LA-071 秩不等式夹出扰动矩阵秩"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-071_强化例题4.5.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-071"
knowledge:
  - "矩阵秩"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "矩阵秩不等式"
  - "秩夹逼"
  - "可逆矩阵扰动"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-METHOD-CLUSTER-1248_秩夹逼"
  - "MATHWIKI-METHOD-CLUSTER-127_矩阵秩不等式"
  - "MATHWIKI-METHOD-CLUSTER-817_可逆矩阵扰动"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-LA-METHOD-013_矩阵秩约束与分块秩比较"
  - "MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# LA-071 秩不等式夹出扰动矩阵秩

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-071_强化例题4.5.md`
- wrongnet ID：`LA-071`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 矩阵秩 |
| 题型 | 矩阵秩不等式夹逼 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 矩阵秩

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 矩阵秩不等式
- 秩夹逼
- 可逆矩阵扰动

### 陷阱

- \(A(C+BA)=O\) 只给上界，不直接给精确秩。
- 下界要用 \(C+BA=C-(-BA)\)，再利用 \(r(C)=n\) 和 \(r(BA)\le r(A)=r\)。
- 上下界必须同时做，单边不等式不足以确定答案。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先由 \(A(C+BA)=O\) 写出上界，再用 \(C\) 可逆补下界 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是只从乘积为零得到一个方向，没有补出反向秩不等式 |
| related_method_card_id | L04-004 |
| next_reminder | 看到乘积为零加可逆扰动求秩，先写上界，再找下界夹出等号。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-METHOD-CLUSTER-1248_秩夹逼]]
- [[MATHWIKI-METHOD-CLUSTER-127_矩阵秩不等式]]
- [[MATHWIKI-METHOD-CLUSTER-817_可逆矩阵扰动]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-LA-METHOD-013_矩阵秩约束与分块秩比较]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-067
- LA-068
- LA-070
- LA-072
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
