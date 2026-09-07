---
wiki_id: SRC-WQ-GS-342
type: source_summary
title: "GS-342 强化例题11.18-3"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-342_强化例题11.18-3.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-342"
knowledge:
  - "一元函数微分学应用"
  - "中值定理"
  - "泰勒公式"
  - "定积分"
  - "定积分性质"
error_causes:
  - "触发信息遗漏"
  - "动作链断裂"
methods:
  - "双端Taylor余项估计"
  - "加权消一阶项"
  - "积分保序"
  - "余项放缩"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-METHOD-CLUSTER-060_积分保序"
  - "MATHWIKI-METHOD-CLUSTER-141_余项放缩"
  - "MATHWIKI-METHOD-CLUSTER-707_加权消一阶项"
  - "MATHWIKI-METHOD-CLUSTER-768_双端Taylor余项估计"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-072_积分不等式证明入口链"
  - "MATHWIKI-GS-METHOD-084_双端点Taylor余项估值链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-342 强化例题11.18-3

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-342_强化例题11.18-3.md`
- wrongnet ID：`GS-342`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | Taylor余项积分估计证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 中值定理
- 泰勒公式
- 定积分
- 定积分性质

### 错因

- 触发信息遗漏
- 动作链断裂

### 方法

- 双端Taylor余项估计
- 加权消一阶项
- 积分保序
- 余项放缩

### 陷阱

- 只对一个端点展开
- 未用加权组合消去一阶项
- 点态估计后未积分化

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先在点 x 处分别展开 f(0) 与 f(1) |
| missed_action | 旧批量卡未记录用户个人错因；低置信推断为没有先做双端展开并加权消去一阶项 |
| related_method_card_id | H11-008 |
| next_reminder | 看到二阶导有界控制插值误差，先双端 Taylor 展开，再加权消一阶项。 |

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
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-METHOD-CLUSTER-060_积分保序]]
- [[MATHWIKI-METHOD-CLUSTER-141_余项放缩]]
- [[MATHWIKI-METHOD-CLUSTER-707_加权消一阶项]]
- [[MATHWIKI-METHOD-CLUSTER-768_双端Taylor余项估计]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-072_积分不等式证明入口链]]
- [[MATHWIKI-GS-METHOD-084_双端点Taylor余项估值链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
