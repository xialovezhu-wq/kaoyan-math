---
wiki_id: SRC-WQ-LA-030
type: source_summary
title: "LA-030 二次型配方法求正惯性指数"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-030_强化例题9.4.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-030"
knowledge:
  - "二次型"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "配方法"
  - "可逆线性变换"
  - "规范形"
  - "惯性指数"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-034_二次型"
  - "MATHWIKI-METHOD-CLUSTER-085_配方法"
  - "MATHWIKI-METHOD-CLUSTER-150_可逆线性变换"
  - "MATHWIKI-METHOD-CLUSTER-228_惯性指数"
  - "MATHWIKI-METHOD-CLUSTER-260_规范形"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-LA-METHOD-006_二次型配方法与正定判定"
  - "MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# LA-030 二次型配方法求正惯性指数

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-030_强化例题9.4.md`
- wrongnet ID：`LA-030`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 二次型 |
| 题型 | 二次型惯性指数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二次型

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 配方法
- 可逆线性变换
- 规范形
- 惯性指数

### 陷阱

- 正惯性指数数的是规范形中正平方项的个数，不是正系数交叉项的个数
- 做线性替换时要保证变换可逆
- 二次型交叉项需要先化成平方和再判正负号

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把二次型化为平方和标准形，而不是从交叉项符号猜惯性指数 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是凭交叉项数量或符号判断惯性指数，没有先化规范形 |
| related_method_card_id | L09-006 |
| next_reminder | 看到二次型问惯性指数，先化规范形，再数正负平方项。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-034_二次型]]
- [[MATHWIKI-METHOD-CLUSTER-085_配方法]]
- [[MATHWIKI-METHOD-CLUSTER-150_可逆线性变换]]
- [[MATHWIKI-METHOD-CLUSTER-228_惯性指数]]
- [[MATHWIKI-METHOD-CLUSTER-260_规范形]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-LA-METHOD-006_二次型配方法与正定判定]]
- [[MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-035
- LA-041
- LA-043

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
