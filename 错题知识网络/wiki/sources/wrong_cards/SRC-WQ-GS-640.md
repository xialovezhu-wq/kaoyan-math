---
wiki_id: SRC-WQ-GS-640
type: source_summary
title: "GS-640 57734 泰勒积分不等式"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-640_57734泰勒积分不等式.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-640"
knowledge:
  - "泰勒公式"
  - "高阶导数"
  - "凹凸性与拐点"
  - "定积分"
  - "定积分性质"
  - "一元函数微分学应用"
  - "定积分不等式"
error_causes:
  - "动作链断裂"
  - "过程跳步"
  - "证明结构不完整"
methods:
  - "泰勒展开"
  - "拉格朗日余项"
  - "积分保序"
  - "函数值比较"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-011_证明结构不完整"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-KNOWLEDGE-018_凹凸性与拐点"
  - "MATHWIKI-KNOWLEDGE-027_高阶导数"
  - "MATHWIKI-KNOWLEDGE-068_定积分不等式"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-008_泰勒展开"
  - "MATHWIKI-METHOD-CLUSTER-060_积分保序"
  - "MATHWIKI-METHOD-CLUSTER-090_函数值比较"
  - "MATHWIKI-METHOD-CLUSTER-118_拉格朗日余项"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-072_积分不等式证明入口链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: cbc65ec94b5b87e3d322d80ff1f897ac65aa50aaf83f74f1b4d35e4eada4079e
---

# GS-640 57734 泰勒积分不等式

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-640_57734泰勒积分不等式.md`
- wrongnet ID：`GS-640`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 二阶导正号下的泰勒展开与定积分不等式证明 |
| 日期 | 2026-06-29 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 泰勒公式
- 高阶导数
- 凹凸性与拐点
- 定积分
- 定积分性质
- 一元函数微分学应用
- 定积分不等式

### 错因

- 动作链断裂
- 过程跳步
- 证明结构不完整

### 方法

- 泰勒展开
- 拉格朗日余项
- 积分保序
- 函数值比较
- 条件转化

### 陷阱

- 展开后停在点态不等式
- 线性项积分为零
- 中点展开
- 严格不等式保序积分
- 二阶导正号

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先在 \(x=a/2\) 处写带拉格朗日余项的二阶泰勒展开 |
| missed_action | 展开得到 \(f(x)>f(a/2)+f'(a/2)(x-a/2)\) 后，没有对 \([0,a]\) 取积分并用 \(\int_0^a(x-a/2)\,dx=0\) 收口 |
| related_method_card_id | H11-008 |
| next_reminder | 看到积分不等式右端是区间长度乘中点函数值，先在中点泰勒展开得到点态不等式，再对整个区间积分，检查线性项是否因对称中心积分为 0。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-011_证明结构不完整]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-KNOWLEDGE-018_凹凸性与拐点]]
- [[MATHWIKI-KNOWLEDGE-027_高阶导数]]
- [[MATHWIKI-KNOWLEDGE-068_定积分不等式]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-060_积分保序]]
- [[MATHWIKI-METHOD-CLUSTER-090_函数值比较]]
- [[MATHWIKI-METHOD-CLUSTER-118_拉格朗日余项]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-072_积分不等式证明入口链]]
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
