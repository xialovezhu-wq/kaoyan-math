---
wiki_id: SRC-WQ-GS-654
type: source_summary
title: "GS-654 89961 方向导数反推梯度"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-654_89961方向导数反推梯度.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-654"
knowledge:
  - "多元函数微分学"
  - "多元函数偏导"
  - "方向导数"
  - "梯度"
error_causes:
  - "方法论调取失败"
  - "方向导数公式入口缺失"
  - "题面语言翻译断点"
  - "动作链断裂"
methods:
  - "方向导数公式"
  - "梯度点乘单位方向"
  - "方向导数反推梯度"
  - "最大方向导数梯度模"
  - "单位化方向向量"
  - "二元线性方程组"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-020_题面语言翻译断点"
  - "MATHWIKI-ERROR-CLUSTER-057_方向导数公式入口缺失"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-KNOWLEDGE-148_方向导数"
  - "MATHWIKI-KNOWLEDGE-182_梯度"
  - "MATHWIKI-METHOD-CLUSTER-1056_方向导数反推梯度"
  - "MATHWIKI-METHOD-CLUSTER-162_方向导数公式"
  - "MATHWIKI-METHOD-CLUSTER-167_梯度点乘单位方向"
  - "MATHWIKI-METHOD-CLUSTER-204_单位化方向向量"
  - "MATHWIKI-METHOD-CLUSTER-234_最大方向导数梯度模"
  - "MATHWIKI-METHOD-CLUSTER-549_二元线性方程组"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-026_方向导数反推梯度"
  - "MATHWIKI-GS-METHOD-044_方向导数与梯度入口判别链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-654 89961 方向导数反推梯度

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-654_89961方向导数反推梯度.md`
- wrongnet ID：`GS-654`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 已知两个方向导数反推梯度并求最大方向导数 |
| 日期 | 2026-07-01 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数微分学
- 多元函数偏导
- 方向导数
- 梯度

### 错因

- 方法论调取失败
- 方向导数公式入口缺失
- 题面语言翻译断点
- 动作链断裂

### 方法

- 方向导数公式
- 梯度点乘单位方向
- 方向导数反推梯度
- 最大方向导数梯度模
- 单位化方向向量
- 二元线性方程组

### 陷阱

- \(P_0P_1\)、\(P_0P_2\) 给的是方向向量，代入方向导数公式前必须单位化
- 两个非共线方向导数给出两个独立方程，可以反推出 \(\nabla f(P_0)\)
- 最大方向导数等于 \(|\nabla f(P_0)|\)，求出梯度后直接取模
- 若两个方向共线，则不能唯一反推出二维梯度

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先设 \(\nabla f(P_0)=(a,b)\)，并计算 \(\overrightarrow{P_0P_1}\)、\(\overrightarrow{P_0P_2}\) 的单位方向向量。 |
| missed_action | 没有把两个已知方向导数条件翻译成关于 \(a,b\) 的线性方程组，因此不知道从哪里求出梯度。 |
| related_method_card_id | H17-003 |
| next_reminder | 看到“已知两个方向导数，求最大方向导数”，先设梯度为未知向量，再用两个单位方向向量点乘列方程，最后取梯度模。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-020_题面语言翻译断点]]
- [[MATHWIKI-ERROR-CLUSTER-057_方向导数公式入口缺失]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-KNOWLEDGE-148_方向导数]]
- [[MATHWIKI-KNOWLEDGE-182_梯度]]
- [[MATHWIKI-METHOD-CLUSTER-1056_方向导数反推梯度]]
- [[MATHWIKI-METHOD-CLUSTER-162_方向导数公式]]
- [[MATHWIKI-METHOD-CLUSTER-167_梯度点乘单位方向]]
- [[MATHWIKI-METHOD-CLUSTER-204_单位化方向向量]]
- [[MATHWIKI-METHOD-CLUSTER-234_最大方向导数梯度模]]
- [[MATHWIKI-METHOD-CLUSTER-549_二元线性方程组]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-026_方向导数反推梯度]]
- [[MATHWIKI-GS-METHOD-044_方向导数与梯度入口判别链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-652
- GS-653

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
