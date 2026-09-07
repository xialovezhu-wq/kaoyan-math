---
wiki_id: SRC-WQ-GS-201
type: source_summary
title: "GS-201 2018年第16题：变上限积分方程转微分方程"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-201_2018年第16题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-201"
knowledge:
  - "微分方程"
  - "一阶线性微分方程"
  - "变上限积分"
  - "定积分"
  - "卷积型积分"
  - "函数平均值"
error_causes:
  - "暂无明确个人错因：旧卡未记录作答过程"
methods:
  - "换元统一积分变量"
  - "对变上限积分方程求导"
  - "一阶线性微分方程"
  - "平均值条件定参数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-KNOWLEDGE-065_一阶线性微分方程"
  - "MATHWIKI-KNOWLEDGE-166_函数平均值"
  - "MATHWIKI-KNOWLEDGE-240_卷积型积分"
  - "MATHWIKI-METHOD-CLUSTER-088_一阶线性微分方程"
  - "MATHWIKI-METHOD-CLUSTER-1040_换元统一积分变量"
  - "MATHWIKI-METHOD-CLUSTER-904_对变上限积分方程求导"
  - "MATHWIKI-METHOD-CLUSTER-978_平均值条件定参数"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-056_微分方程入口判别链"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-289"
formal_projection_sha256: b785fba6e6ac4d4545a60837b8afc7f7c8e7b35cc5959a745fc80344f97a09b4
---

# GS-201 2018年第16题：变上限积分方程转微分方程

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-201_2018年第16题.md`
- wrongnet ID：`GS-201`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 高等数学-微分方程 |
| 题型 | 变上限积分方程与一阶线性微分方程 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 微分方程
- 一阶线性微分方程
- 变上限积分
- 定积分
- 卷积型积分
- 函数平均值

### 错因

- 暂无明确个人错因：旧卡未记录作答过程

### 方法

- 换元统一积分变量
- 对变上限积分方程求导
- 一阶线性微分方程
- 平均值条件定参数

### 陷阱

- 第二个积分要先换元，避免 x 同时出现在上限和被积函数内部
- 平均值条件最后再用来求 a
- 由求导得到初值 f(0)=0，不要漏掉

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把 \(\int_0^x t f(x-t)\,dt\) 换元为 \(\int_0^x (x-s)f(s)\,ds\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有先统一积分变量就直接求导 |
| related_method_card_id | H15-010 |
| next_reminder | 看到含 \(f(x-t)\) 的变上限积分方程，先换元统一积分变量，再对整体等式求导。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-KNOWLEDGE-065_一阶线性微分方程]]
- [[MATHWIKI-KNOWLEDGE-166_函数平均值]]
- [[MATHWIKI-KNOWLEDGE-240_卷积型积分]]
- [[MATHWIKI-METHOD-CLUSTER-088_一阶线性微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-1040_换元统一积分变量]]
- [[MATHWIKI-METHOD-CLUSTER-904_对变上限积分方程求导]]
- [[MATHWIKI-METHOD-CLUSTER-978_平均值条件定参数]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-056_微分方程入口判别链]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-289

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
