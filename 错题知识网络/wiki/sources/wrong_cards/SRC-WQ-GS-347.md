---
wiki_id: SRC-WQ-GS-347
type: source_summary
title: "GS-347 1000题A组11.9-2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-347_1000题A组11.9-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-347"
knowledge:
  - "定积分"
  - "定积分性质"
  - "一元函数微分学应用"
  - "中值定理"
error_causes:
  - "触发信息遗漏"
  - "动作链断裂"
methods:
  - "极值点控制"
  - "牛顿莱布尼茨公式"
  - "三角不等式"
  - "导数积分估计"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-METHOD-CLUSTER-049_牛顿莱布尼茨公式"
  - "MATHWIKI-METHOD-CLUSTER-138_三角不等式"
  - "MATHWIKI-METHOD-CLUSTER-396_极值点控制"
  - "MATHWIKI-METHOD-CLUSTER-944_导数积分估计"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-072_积分不等式证明入口链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-347 1000题A组11.9-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-347_1000题A组11.9-2.md`
- wrongnet ID：`GS-347`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 导数积分估计证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 一元函数微分学应用
- 中值定理

### 错因

- 触发信息遗漏
- 动作链断裂

### 方法

- 极值点控制
- 牛顿莱布尼茨公式
- 三角不等式
- 导数积分估计

### 陷阱

- 只从一个端点估计导致系数不紧
- 未先取最大值点
- 绝对值积分两段未相加

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先取 x0 使 |f(x0)| 达到全区间最大值 |
| missed_action | 旧批量卡未记录用户个人错因；低置信推断为没有先取最坏点并从两端同时估计 |
| related_method_card_id | H11-007 |
| next_reminder | 看到端点为零且要控制 |f|，先取最大点，再从左右端点分别积分估计。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-049_牛顿莱布尼茨公式]]
- [[MATHWIKI-METHOD-CLUSTER-138_三角不等式]]
- [[MATHWIKI-METHOD-CLUSTER-396_极值点控制]]
- [[MATHWIKI-METHOD-CLUSTER-944_导数积分估计]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-072_积分不等式证明入口链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-320
- GS-345
- GS-337

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
