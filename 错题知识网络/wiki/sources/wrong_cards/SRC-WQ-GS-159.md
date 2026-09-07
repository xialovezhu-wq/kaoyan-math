---
wiki_id: SRC-WQ-GS-159
type: source_summary
title: "GS-159 1000题B组5.23"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-159_1000题B组5.23.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-159"
knowledge:
  - "定积分"
  - "变上限积分"
  - "单调性与极值"
error_causes:
  - "个人原始错因未记录"
methods:
  - "变上限积分求导"
  - "闭区间极值比较"
  - "指数三角积分公式"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-029_个人原始错因未记录"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-METHOD-CLUSTER-015_变上限积分求导"
  - "MATHWIKI-METHOD-CLUSTER-1019_指数三角积分公式"
  - "MATHWIKI-METHOD-CLUSTER-1398_闭区间极值比较"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-159 1000题B组5.23

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-159_1000题B组5.23.md`
- wrongnet ID：`GS-159`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 变上限积分最值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 变上限积分
- 单调性与极值

### 错因

- 个人原始错因未记录

### 方法

- 变上限积分求导
- 闭区间极值比较
- 指数三角积分公式

### 陷阱

- 闭区间极值要比较端点
- 只令导数为零不够

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写出 \(f'(x)=e^{-x}\cos x\) 并找临界点 |
| missed_action | 旧卡缺用户作答过程；待确认是否只找导数零点而漏了闭区间端点比较 |
| related_method_card_id | H05-003 |
| next_reminder | 看到闭区间上的变上限积分最值，先求导判单调，再把端点一起比较。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-029_个人原始错因未记录]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-METHOD-CLUSTER-015_变上限积分求导]]
- [[MATHWIKI-METHOD-CLUSTER-1019_指数三角积分公式]]
- [[MATHWIKI-METHOD-CLUSTER-1398_闭区间极值比较]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-157
- GS-155
- GS-160
- GS-166

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
