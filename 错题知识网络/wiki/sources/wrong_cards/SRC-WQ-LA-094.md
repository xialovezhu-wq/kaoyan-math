---
wiki_id: SRC-WQ-LA-094
type: source_summary
title: "LA-094 强化例题6.4 幂零链线性无关与秩稳定"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-094_强化例题6.4.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-094"
knowledge:
  - "矩阵运算"
  - "矩阵秩"
  - "向量组线性无关"
  - "线性方程组"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "幂零链线性无关"
  - "核空间包含"
  - "秩-零化度关系"
  - "反证法"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-014_矩阵运算"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-033_线性方程组"
  - "MATHWIKI-KNOWLEDGE-090_向量组线性无关"
  - "MATHWIKI-METHOD-CLUSTER-079_反证法"
  - "MATHWIKI-METHOD-CLUSTER-1242_秩-零化度关系"
  - "MATHWIKI-METHOD-CLUSTER-365_幂零链线性无关"
  - "MATHWIKI-METHOD-CLUSTER-407_核空间包含"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-011_矩阵幂降维与秩空间判断"
  - "MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# LA-094 强化例题6.4 幂零链线性无关与秩稳定

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-094_强化例题6.4.md`
- wrongnet ID：`LA-094`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 矩阵幂与向量组线性无关 |
| 题型 | 证明题 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 矩阵运算
- 矩阵秩
- 向量组线性无关
- 线性方程组

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 幂零链线性无关
- 核空间包含
- 秩-零化度关系
- 反证法

### 陷阱

- \(A^{k-1}a\ne0,A^ka=0\) 不能直接口头断言无关，必须设线性组合并左乘矩阵幂逐个杀系数
- 证明 \(r(A^{n+1})=r(A^n)\) 时，只写 \(\mathcal N(A^n)\subseteq \mathcal N(A^{n+1})\) …
- 反证时构造出 \(n+1\) 个 \(n\) 维向量线性无关即矛盾

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先设线性组合为零，并从最高幂条件逐步杀系数 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有把矩阵幂条件转成向量链或核空间包含证明 |
| related_method_card_id | L06-005 |
| next_reminder | 看到矩阵幂链证明，先把目标转成向量链或核空间包含，再做秩或线性无关证明。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-033_线性方程组]]
- [[MATHWIKI-KNOWLEDGE-090_向量组线性无关]]
- [[MATHWIKI-METHOD-CLUSTER-079_反证法]]
- [[MATHWIKI-METHOD-CLUSTER-1242_秩-零化度关系]]
- [[MATHWIKI-METHOD-CLUSTER-365_幂零链线性无关]]
- [[MATHWIKI-METHOD-CLUSTER-407_核空间包含]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-011_矩阵幂降维与秩空间判断]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- [[MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-039
- LA-056
- LA-058

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
