---
wiki_id: SRC-WQ-GS-652
type: source_summary
title: "GS-652 78821 方向导数梯度点乘"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-652_78821方向导数梯度点乘.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-652"
knowledge:
  - "多元函数微分学"
  - "多元函数偏导"
  - "方向导数"
  - "梯度"
error_causes:
  - "方法论调取失败"
  - "方向导数公式入口缺失"
  - "单位化方向向量遗漏"
  - "概念边界混淆"
  - "动作链断裂"
methods:
  - "方向导数公式"
  - "梯度点乘单位方向"
  - "单位化方向向量"
  - "偏导计算"
  - "点积展开"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-027_概念边界混淆"
  - "MATHWIKI-ERROR-CLUSTER-057_方向导数公式入口缺失"
  - "MATHWIKI-ERROR-CLUSTER-151_单位化方向向量遗漏"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-KNOWLEDGE-148_方向导数"
  - "MATHWIKI-KNOWLEDGE-182_梯度"
  - "MATHWIKI-METHOD-CLUSTER-162_方向导数公式"
  - "MATHWIKI-METHOD-CLUSTER-167_梯度点乘单位方向"
  - "MATHWIKI-METHOD-CLUSTER-192_偏导计算"
  - "MATHWIKI-METHOD-CLUSTER-204_单位化方向向量"
  - "MATHWIKI-METHOD-CLUSTER-242_点积展开"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-024_方向导数梯度点乘"
  - "MATHWIKI-GS-METHOD-044_方向导数与梯度入口判别链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-652 78821 方向导数梯度点乘

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-652_78821方向导数梯度点乘.md`
- wrongnet ID：`GS-652`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 三元函数沿给定向量的方向导数 |
| 日期 | 2026-07-01 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 多元函数微分学
- 多元函数偏导
- 方向导数
- 梯度

### 错因

- 方法论调取失败
- 方向导数公式入口缺失
- 单位化方向向量遗漏
- 概念边界混淆
- 动作链断裂

### 方法

- 方向导数公式
- 梯度点乘单位方向
- 单位化方向向量
- 偏导计算
- 点积展开

### 陷阱

- 方向导数公式中的方向向量必须单位化
- 不能直接用 \(n=(1,2,2)\) 与梯度点乘
- 梯度先对变量求偏导，再代入点坐标
- \(n^\circ=\frac{n}{|n|}\) 不是新向量猜法，而是把方向向量标准化

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写出公式 \(D_{\mathbf e}f(P_0)=\nabla f(P_0)\cdot\mathbf e\)，并计算 \(\nabla f(P_0)\)。 |
| missed_action | 没有从“沿向量的方向导数”触发梯度点乘单位方向公式；也没有先把 \(n=(1,2,2)\) 单位化为 \(\frac13(1,2,2)\)。 |
| related_method_card_id | H17-001 |
| next_reminder | 看到“沿某向量的方向导数”，先求点处梯度，再把方向向量除以长度单位化，最后做点积。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-027_概念边界混淆]]
- [[MATHWIKI-ERROR-CLUSTER-057_方向导数公式入口缺失]]
- [[MATHWIKI-ERROR-CLUSTER-151_单位化方向向量遗漏]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-KNOWLEDGE-148_方向导数]]
- [[MATHWIKI-KNOWLEDGE-182_梯度]]
- [[MATHWIKI-METHOD-CLUSTER-162_方向导数公式]]
- [[MATHWIKI-METHOD-CLUSTER-167_梯度点乘单位方向]]
- [[MATHWIKI-METHOD-CLUSTER-192_偏导计算]]
- [[MATHWIKI-METHOD-CLUSTER-204_单位化方向向量]]
- [[MATHWIKI-METHOD-CLUSTER-242_点积展开]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-024_方向导数梯度点乘]]
- [[MATHWIKI-GS-METHOD-044_方向导数与梯度入口判别链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-626
- GS-651

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
