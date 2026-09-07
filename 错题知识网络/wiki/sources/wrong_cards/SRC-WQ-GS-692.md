---
wiki_id: SRC-WQ-GS-692
type: source_summary
title: "GS-692 102491 第一型曲线积分函数记号与下限项"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-692_102491第一型曲线积分函数记号与下限项.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-692"
knowledge:
  - "多元函数积分学"
  - "曲线积分"
  - "定积分"
error_causes:
  - "概念混淆"
  - "运算路径不稳"
  - "边界项检查遗漏"
methods:
  - "第一型曲线积分直角坐标法"
  - "曲线方程代入"
  - "凑微分换元"
  - "定积分端点逐项代入"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-007_B7-CALC"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-028_运算路径不稳"
  - "MATHWIKI-ERROR-CLUSTER-061_边界项检查遗漏"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-073_多元函数积分学"
  - "MATHWIKI-KNOWLEDGE-151_曲线积分"
  - "MATHWIKI-METHOD-CLUSTER-064_凑微分换元"
  - "MATHWIKI-METHOD-CLUSTER-1076_曲线方程代入"
  - "MATHWIKI-METHOD-CLUSTER-1282_第一型曲线积分直角坐标法"
  - "MATHWIKI-METHOD-CLUSTER-897_定积分端点逐项代入"
status: indexed
last_updated: 2026-07-15
---

# GS-692 102491 第一型曲线积分函数记号与下限项

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-692_102491第一型曲线积分函数记号与下限项.md`
- wrongnet ID：`GS-692`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数积分学 |
| 题型 | 第一型曲线积分的直角坐标计算 |
| 日期 | 2026-07-14 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 多元函数积分学
- 曲线积分
- 定积分

### 错因

- 概念混淆
- 运算路径不稳
- 边界项检查遗漏

### 方法

- 第一型曲线积分直角坐标法
- 曲线方程代入
- 凑微分换元
- 定积分端点逐项代入

### 陷阱

- $f(x,y(x))$ 是函数取值记号，不是 $x$ 与 $y(x)$ 的乘积。
- 下限为 $0$ 不代表整个下限项为 $0$。
- 复合原函数代入端点时要保留常数项并执行上限减下限。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B7-CALC |
| expected_first_action | 先写明本题 $f(x,y)=x$，再单独计算 $y'(x)$ 和 $ds$；原函数求出后把 $F(\sqrt2)$ 与 $F(0)$ 分成两行计算。 |
| missed_action | 没有先确认 $f$ 的具体表达式，把函数取值记号误读成乘法；计算收尾时又没有完整代入下限的复合表达式。 |
| related_method_card_id | H18-007 |
| next_reminder | 看到第一型曲线积分，先圈出真正的被积函数并替换 $ds$；看到 $F(b)-F(a)$，两个端点都完整代入，不能因 $a=0$ 就跳过 $F(a)$。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-007_B7-CALC]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-028_运算路径不稳]]
- [[MATHWIKI-ERROR-CLUSTER-061_边界项检查遗漏]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-073_多元函数积分学]]
- [[MATHWIKI-KNOWLEDGE-151_曲线积分]]
- [[MATHWIKI-METHOD-CLUSTER-064_凑微分换元]]
- [[MATHWIKI-METHOD-CLUSTER-1076_曲线方程代入]]
- [[MATHWIKI-METHOD-CLUSTER-1282_第一型曲线积分直角坐标法]]
- [[MATHWIKI-METHOD-CLUSTER-897_定积分端点逐项代入]]

### 深度编译页

- 待编译到概念页、方法页、专题页、错因模式页或触发页

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-685

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
