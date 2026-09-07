---
wiki_id: SRC-WQ-GS-164
type: source_summary
title: "GS-164 2021年第20题"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-164_2021年第20题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-164"
knowledge:
  - "一阶线性微分方程"
  - "法线方程"
  - "单调性与极值"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是容易先盯法线截距而没有先解一阶线性微分方程得到 y(x)，需用户复做确认。"
methods:
  - "一阶线性微分方程"
  - "积分因子"
  - "法线方程"
  - "法线截距函数化"
  - "最值求导"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-311_旧批量未记录个人原始错因-当前仅确认复做断点是容易先盯法线截距而没有先解"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-065_一阶线性微分方程"
  - "MATHWIKI-KNOWLEDGE-263_法线方程"
  - "MATHWIKI-METHOD-CLUSTER-061_积分因子"
  - "MATHWIKI-METHOD-CLUSTER-088_一阶线性微分方程"
  - "MATHWIKI-METHOD-CLUSTER-1167_法线截距函数化"
  - "MATHWIKI-METHOD-CLUSTER-388_最值求导"
  - "MATHWIKI-METHOD-CLUSTER-423_法线方程"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-056_微分方程入口判别链"
  - "MATHWIKI-GS-METHOD-065_隐函数定点法线斜率"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-164 2021年第20题

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-164_2021年第20题.md`
- wrongnet ID：`GS-164`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 微分方程 |
| 题型 | 一阶线性微分方程与法线截距最值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一阶线性微分方程
- 法线方程
- 单调性与极值

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是容易先盯法线截距而没有先解一阶线性微分方程得到 y(x)，需用户复做确认。

### 方法

- 一阶线性微分方程
- 积分因子
- 法线方程
- 法线截距函数化
- 最值求导

### 陷阱

- 法线斜率是切线斜率的负倒数
- 法线截距需要先表示成自变量函数
- 初值条件代回通解

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把微分方程化为一阶线性标准型并解出 y(x) |
| missed_action | 旧批量未记录个人第一错步；当前只确认不能在未求出 y(x) 前直接处理法线截距 |
| related_method_card_id | H15-005 |
| next_reminder | 看到微分方程和法线截距混合题，先解出 y(x)，再把几何量写成单变量函数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-311_旧批量未记录个人原始错因-当前仅确认复做断点是容易先盯法线截距而没有先解]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-065_一阶线性微分方程]]
- [[MATHWIKI-KNOWLEDGE-263_法线方程]]
- [[MATHWIKI-METHOD-CLUSTER-061_积分因子]]
- [[MATHWIKI-METHOD-CLUSTER-088_一阶线性微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-1167_法线截距函数化]]
- [[MATHWIKI-METHOD-CLUSTER-388_最值求导]]
- [[MATHWIKI-METHOD-CLUSTER-423_法线方程]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-056_微分方程入口判别链]]
- [[MATHWIKI-GS-METHOD-065_隐函数定点法线斜率]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-128
- GS-190
- GS-203

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
