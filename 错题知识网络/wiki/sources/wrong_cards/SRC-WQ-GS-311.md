---
wiki_id: SRC-WQ-GS-311
type: source_summary
title: "GS-311 135837 绝对余弦半周期余段积分"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-311_强化例题11.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-311"
knowledge:
  - "定积分"
  - "定积分等式"
  - "定积分性质"
  - "三角恒等变形"
  - "周期函数"
  - "参数分类讨论"
error_causes:
  - "条件检查遗漏"
  - "动作链断裂"
methods:
  - "周期性积分"
  - "分类讨论"
  - "区间平移"
  - "绝对值三角函数积分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-043_三角恒等变形"
  - "MATHWIKI-KNOWLEDGE-047_参数分类讨论"
  - "MATHWIKI-KNOWLEDGE-084_定积分等式"
  - "MATHWIKI-KNOWLEDGE-102_周期函数"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-078_区间平移"
  - "MATHWIKI-METHOD-CLUSTER-257_绝对值三角函数积分"
  - "MATHWIKI-METHOD-CLUSTER-340_周期性积分"
  - "MATHWIKI-GS-METHOD-040_绝对三角周期积分"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-311 135837 绝对余弦半周期余段积分

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-311_强化例题11.7.md`
- wrongnet ID：`GS-311`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 绝对值三角函数半周期积分 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分等式
- 定积分性质
- 三角恒等变形
- 周期函数
- 参数分类讨论

### 错因

- 条件检查遗漏
- 动作链断裂

### 方法

- 周期性积分
- 分类讨论
- 区间平移
- 绝对值三角函数积分

### 陷阱

- \\sqrt{1-\\sin^2 x}=|\\cos x|，不是直接等于 \\cos x
- |cos x| 的周期是 pi，不是 pi/2
- k 为奇数时会剩下长度 pi/2 的余段，余段积分一般与起点 a 有关

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先把根式改写为绝对余弦 |
| missed_action | 没有先确认绝对值与半周期余段是否仍依赖起点 |
| related_method_card_id | H08-008 |
| next_reminder | 看到绝对三角积分，先化绝对值，再查周期和剩余区间。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-043_三角恒等变形]]
- [[MATHWIKI-KNOWLEDGE-047_参数分类讨论]]
- [[MATHWIKI-KNOWLEDGE-084_定积分等式]]
- [[MATHWIKI-KNOWLEDGE-102_周期函数]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-078_区间平移]]
- [[MATHWIKI-METHOD-CLUSTER-257_绝对值三角函数积分]]
- [[MATHWIKI-METHOD-CLUSTER-340_周期性积分]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-040_绝对三角周期积分]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-310

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
