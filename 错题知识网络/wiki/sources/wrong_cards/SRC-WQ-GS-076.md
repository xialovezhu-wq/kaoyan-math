---
wiki_id: SRC-WQ-GS-076
type: source_summary
title: "GS-076 1000题B2.2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-076_1000题B2.2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-076"
knowledge:
  - "极限与连续"
  - "数列极限"
  - "三角恒等变形"
  - "主导项"
error_causes:
  - "触发信息遗漏"
  - "公式记错"
  - "动作链断裂"
methods:
  - "区间定位"
  - "正切差角公式"
  - "夹逼准则"
  - "主导项比较"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-015_公式记错"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-043_三角恒等变形"
  - "MATHWIKI-KNOWLEDGE-086_主导项"
  - "MATHWIKI-METHOD-CLUSTER-016_夹逼准则"
  - "MATHWIKI-METHOD-CLUSTER-021_主导项比较"
  - "MATHWIKI-METHOD-CLUSTER-1150_正切差角公式"
  - "MATHWIKI-METHOD-CLUSTER-718_区间定位"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-092_三角隐式根与递推比阶入口链"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-007_数列极限错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-076 1000题B2.2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-076_1000题B2.2.md`
- wrongnet ID：`GS-076`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 隐式根序列差值极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 4 |

## 可编译信息

### 知识点

- 极限与连续
- 数列极限
- 三角恒等变形
- 主导项

### 错因

- 触发信息遗漏
- 公式记错
- 动作链断裂

### 方法

- 区间定位
- 正切差角公式
- 夹逼准则
- 主导项比较

### 陷阱

- 根所在区间
- 正切周期
- 差角公式分母

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先由 $(n\pi)^2<a_n<(n\pi+\frac\pi2)^2$ 写出 $n\pi<\sqrt{a_n}<n\pi+\frac\pi2$。 |
| missed_action | 没有先使用区间定位和正切差角公式，导致无法判断相邻根差趋向哪个周期长度。 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到三角方程的第 n 个根，先写根所在周期区间，再考虑相邻根差。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-015_公式记错]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-043_三角恒等变形]]
- [[MATHWIKI-KNOWLEDGE-086_主导项]]
- [[MATHWIKI-METHOD-CLUSTER-016_夹逼准则]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]
- [[MATHWIKI-METHOD-CLUSTER-1150_正切差角公式]]
- [[MATHWIKI-METHOD-CLUSTER-718_区间定位]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-092_三角隐式根与递推比阶入口链]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-007_数列极限错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-162
- GS-292
- GS-632
- GS-636

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
