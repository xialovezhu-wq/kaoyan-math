---
wiki_id: SRC-WQ-GS-202
type: source_summary
title: "GS-202 强化例题15.3-2：函数方程求导建立微分方程"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-202_强化例题15.3-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-202"
related_wrongnet_refs: []
knowledge:
  - "微分方程"
  - "一阶线性微分方程"
  - "微分方程建模"
  - "单调性与极值"
  - "函数方程"
error_causes:
  - "题型入口风险：用特殊值和参数求导，把函数方程转译为一阶线性微分方程。"
methods:
  - "特殊值代入"
  - "对参数求导"
  - "函数方程转微分方程"
  - "一阶线性微分方程求解"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-453_题型入口风险-用特殊值和参数求导-把函数方程转译为一阶线性微分方程"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-KNOWLEDGE-065_一阶线性微分方程"
  - "MATHWIKI-KNOWLEDGE-147_微分方程建模"
  - "MATHWIKI-KNOWLEDGE-193_函数方程"
  - "MATHWIKI-METHOD-CLUSTER-1194_特殊值代入"
  - "MATHWIKI-METHOD-CLUSTER-507_一阶线性微分方程求解"
  - "MATHWIKI-METHOD-CLUSTER-660_函数方程转微分方程"
  - "MATHWIKI-METHOD-CLUSTER-903_对参数求导"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: eee6d5f31febc6660fb7f0dd83ae3f95e574ea9ff9fa3fc706f693d42297f9b9
---

# GS-202 强化例题15.3-2：函数方程求导建立微分方程

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-202_强化例题15.3-2.md`
- wrongnet ID：`GS-202`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 高等数学-微分方程 |
| 题型 | 函数方程建立一阶线性微分方程 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 微分方程
- 一阶线性微分方程
- 微分方程建模
- 单调性与极值
- 函数方程

### 错因

- 题型入口风险：用特殊值和参数求导，把函数方程转译为一阶线性微分方程。

### 方法

- 特殊值代入
- 对参数求导
- 函数方程转微分方程
- 一阶线性微分方程求解

### 陷阱

- 含 $f(xy)$ 的函数方程先试特殊值
- 对恒等式求导时要固定另一个变量
- 求完 $f(x)$ 后再回到极值目标

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先令 $x=1$ 得 $f(1)=0$，再对恒等式关于 $y$ 求导并令 $y=1$。 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有先取特殊值和参数求导，导致函数方程无法转为微分方程。 |
| related_method_card_id | H15-010 |
| next_reminder | 看到函数方程含 $f(xy)$，先取特殊值找初值，再对参数求导建微分方程。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-453_题型入口风险-用特殊值和参数求导-把函数方程转译为一阶线性微分方程]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-KNOWLEDGE-065_一阶线性微分方程]]
- [[MATHWIKI-KNOWLEDGE-147_微分方程建模]]
- [[MATHWIKI-KNOWLEDGE-193_函数方程]]
- [[MATHWIKI-METHOD-CLUSTER-1194_特殊值代入]]
- [[MATHWIKI-METHOD-CLUSTER-507_一阶线性微分方程求解]]
- [[MATHWIKI-METHOD-CLUSTER-660_函数方程转微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-903_对参数求导]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 证据边界

- GS-202 的个人断点证据仍为 `pending_user_confirmation`；与 GS-471 的普通强边因无法确认双方共享同一个人第一断点而降级。

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
