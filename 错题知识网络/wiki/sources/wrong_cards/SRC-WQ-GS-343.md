---
wiki_id: SRC-WQ-GS-343
type: source_summary
title: "GS-343 1000题A组11.10-3"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-343_1000题A组11.10-3.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-343"
knowledge:
  - "定积分"
  - "分部积分"
  - "定积分不等式"
  - "振荡积分估计"
  - "微分形式转换"
error_causes:
  - "暂无明确个人错因（视觉证据仅支持复做入口）"
methods:
  - "分部积分"
  - "振荡积分估计"
  - "微分形式转换"
  - "绝对值放缩"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-068_定积分不等式"
  - "MATHWIKI-KNOWLEDGE-257_振荡积分估计"
  - "MATHWIKI-KNOWLEDGE-362_微分形式转换"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-178_绝对值放缩"
  - "MATHWIKI-METHOD-CLUSTER-369_微分形式转换"
  - "MATHWIKI-METHOD-CLUSTER-379_振荡积分估计"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-343 1000题A组11.10-3

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-343_1000题A组11.10-3.md`
- wrongnet ID：`GS-343`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 振荡积分分部估计证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 分部积分
- 定积分不等式
- 振荡积分估计
- 微分形式转换

### 错因

- 暂无明确个人错因（视觉证据仅支持复做入口）

### 方法

- 分部积分
- 振荡积分估计
- 微分形式转换
- 绝对值放缩

### 陷阱

- 不能直接用区间长度估计
- 先把相位导数提出
- 边界项也要估计
- x>0 保证分母有下界

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 sin u^2 du=-1/(2u)d(cos u^2) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有先把相位导数提出，导致只能做粗放缩 |
| related_method_card_id | H11-005 |
| next_reminder | 看到振荡积分证明，先把相位导数提出成微分形式，再分部积分并分别估边界项和余项。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-068_定积分不等式]]
- [[MATHWIKI-KNOWLEDGE-257_振荡积分估计]]
- [[MATHWIKI-KNOWLEDGE-362_微分形式转换]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-178_绝对值放缩]]
- [[MATHWIKI-METHOD-CLUSTER-369_微分形式转换]]
- [[MATHWIKI-METHOD-CLUSTER-379_振荡积分估计]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-247

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
