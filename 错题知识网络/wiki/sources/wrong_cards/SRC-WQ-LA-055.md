---
wiki_id: SRC-WQ-LA-055
type: source_summary
title: "LA-055 伴随矩阵列交换传递"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-055_强化例题3.15.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-055"
knowledge:
  - "行列式"
  - "初等变换"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "伴随矩阵"
  - "初等交换矩阵"
  - "右乘列变换"
  - "伴随矩阵乘积反序"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-023_行列式"
  - "MATHWIKI-KNOWLEDGE-167_初等变换"
  - "MATHWIKI-METHOD-CLUSTER-108_伴随矩阵"
  - "MATHWIKI-METHOD-CLUSTER-336_右乘列变换"
  - "MATHWIKI-METHOD-CLUSTER-592_伴随矩阵乘积反序"
  - "MATHWIKI-METHOD-CLUSTER-698_初等交换矩阵"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-LA-METHOD-010_伴随矩阵与反对称结构"
  - "MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# LA-055 伴随矩阵列交换传递

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-055_强化例题3.15.md`
- wrongnet ID：`LA-055`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 矩阵运算 |
| 题型 | 伴随矩阵性质判断 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 行列式
- 初等变换

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 伴随矩阵
- 初等交换矩阵
- 右乘列变换
- 伴随矩阵乘积反序

### 陷阱

- 交换 \(A\) 的两列是右乘交换矩阵，不是左乘。
- 伴随矩阵满足 \((AB)^*=B^*A^*\)，乘积顺序会反过来。
- 三阶交换矩阵的伴随矩阵为负的交换矩阵，所以最后体现为 \(-A^*\) 的第 1、2 行互换。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写 \(B=AE_{12}\)，明确交换列是右乘 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是只凭直觉交换 \(B^*\) 的行列，忘记先判定左乘还是右乘 |
| related_method_card_id | L03-006 |
| next_reminder | 看到交换行列后的伴随矩阵，先写成初等矩阵乘法，再用 \((AB)^*=B^*A^*\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-023_行列式]]
- [[MATHWIKI-KNOWLEDGE-167_初等变换]]
- [[MATHWIKI-METHOD-CLUSTER-108_伴随矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-336_右乘列变换]]
- [[MATHWIKI-METHOD-CLUSTER-592_伴随矩阵乘积反序]]
- [[MATHWIKI-METHOD-CLUSTER-698_初等交换矩阵]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-LA-METHOD-010_伴随矩阵与反对称结构]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-049
- LA-050

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
