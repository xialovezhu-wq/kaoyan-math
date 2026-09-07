---
wiki_id: SRC-WQ-GS-673
type: source_summary
title: "GS-673 58087 积分主部替换判阶"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-673_58087积分主部替换判阶.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-673"
knowledge:
  - "极限与连续"
  - "等价无穷小"
  - "无穷小阶数比较"
  - "一阶线性主部"
  - "定积分"
  - "变上限积分"
  - "洛必达法则"
error_causes:
  - "触发信息遗漏"
  - "方法论调取失败"
  - "方法选择错误"
  - "洛必达前置化简不足"
  - "动作链断裂"
methods:
  - "先判型"
  - "一阶线性主部"
  - "等价无穷小"
  - "积分主部"
  - "变上限积分等价替换"
  - "主导项比较"
  - "无穷小阶数比较"
  - "代入复合自变量"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-088_洛必达前置化简不足"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-045_洛必达法则"
  - "MATHWIKI-KNOWLEDGE-051_无穷小阶数比较"
  - "MATHWIKI-KNOWLEDGE-189_一阶线性主部"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-021_主导项比较"
  - "MATHWIKI-METHOD-CLUSTER-026_等价无穷小"
  - "MATHWIKI-METHOD-CLUSTER-1253_积分主部"
  - "MATHWIKI-METHOD-CLUSTER-137_一阶线性主部"
  - "MATHWIKI-METHOD-CLUSTER-332_变上限积分等价替换"
  - "MATHWIKI-METHOD-CLUSTER-384_无穷小阶数比较"
  - "MATHWIKI-METHOD-CLUSTER-577_代入复合自变量"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-016"
formal_projection_sha256: a29a986bfa15111cdc544ad0b46b4792b029283efb8ee40a63e1aad12e1551f0
---

# GS-673 58087 积分主部替换判阶

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-673_58087积分主部替换判阶.md`
- wrongnet ID：`GS-673`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 积分定义函数主部替换与无穷小阶数比较 |
| 日期 | 2026-07-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 等价无穷小
- 无穷小阶数比较
- 一阶线性主部
- 定积分
- 变上限积分
- 洛必达法则

### 错因

- 触发信息遗漏
- 方法论调取失败
- 方法选择错误
- 洛必达前置化简不足
- 动作链断裂

### 方法

- 先判型
- 一阶线性主部
- 等价无穷小
- 积分主部
- 变上限积分等价替换
- 主导项比较
- 无穷小阶数比较
- 代入复合自变量

### 陷阱

- 目标不是直接比较 $f(x)$ 与 $g(x)$，而是比较 $g(x^3)$ 与 $[g(x)]^3$。
- $f(0)=0,\ f'(0)=6$ 要先翻译成 $f(t)\sim6t$。
- 积分会把主部升一阶：$g(x)=\int_0^x f(t)dt\sim\int_0^x6t\,dt=3x^2$。
- 得到 $g(x)\sim3x^2$ 后，要分别处理复合上限 $g(x^3)$ 和整体三次方 $[g(x)]^3$。
- $\alpha(x)/\beta(x)\to1/9$ 只能说明同阶，不能说明等价。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 $f(t)\sim6t$，并计算 $g(x)=\int_0^x f(t)dt\sim\int_0^x6t\,dt=3x^2$。 |
| missed_action | 没有先找 $g(x)$ 的等价主部，而是直接比较 $f(x)$ 与 $g(x)$ 并反复套洛必达，导致没有把题目化成 $g(x^3)$ 与 $[g(x)]^3$ 的主部比较。 |
| related_method_card_id | H01-004 |
| next_reminder | 看到积分定义函数再复合或取幂比较阶数，先设 $g(x)=\int_0^x f(t)dt$，再用 $f$ 的主部积分出 $g$ 的主部，不要先硬套洛必达。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-088_洛必达前置化简不足]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-045_洛必达法则]]
- [[MATHWIKI-KNOWLEDGE-051_无穷小阶数比较]]
- [[MATHWIKI-KNOWLEDGE-189_一阶线性主部]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]
- [[MATHWIKI-METHOD-CLUSTER-026_等价无穷小]]
- [[MATHWIKI-METHOD-CLUSTER-1253_积分主部]]
- [[MATHWIKI-METHOD-CLUSTER-137_一阶线性主部]]
- [[MATHWIKI-METHOD-CLUSTER-332_变上限积分等价替换]]
- [[MATHWIKI-METHOD-CLUSTER-384_无穷小阶数比较]]
- [[MATHWIKI-METHOD-CLUSTER-577_代入复合自变量]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-016

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
