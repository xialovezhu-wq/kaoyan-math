---
wiki_id: SRC-WQ-GS-022
type: source_summary
title: "GS-022 2 57971 2026.5.10 T1"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-022_2579712026.4.1T1.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-022"
knowledge:
  - "极限与连续"
  - "等价无穷小"
  - "拉格朗日中值定理"
  - "中值定理"
  - "无穷小阶数比较"
error_causes:
  - "条件忽略"
  - "参数边界错误"
  - "过程跳步"
methods:
  - "等价变形"
  - "构造辅助函数"
  - "中值定理"
  - "分类讨论"
  - "主导项比较"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-159_参数边界错误"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-KNOWLEDGE-021_拉格朗日中值定理"
  - "MATHWIKI-KNOWLEDGE-051_无穷小阶数比较"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-021_主导项比较"
  - "MATHWIKI-METHOD-CLUSTER-036_中值定理"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-022 2 57971 2026.5.10 T1

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-022_2579712026.4.1T1.md`
- wrongnet ID：`GS-022`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 无穷小阶数比较 |
| 日期 | 2026-05-10 |
| 状态 | 已掌握 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 等价无穷小
- 拉格朗日中值定理
- 中值定理
- 无穷小阶数比较

### 错因

- 条件忽略
- 参数边界错误
- 过程跳步

### 方法

- 等价变形
- 构造辅助函数
- 中值定理
- 分类讨论
- 主导项比较

### 陷阱

- 参数边界
- 主导项
- 变量混淆
- 极限过程
- 量纲/阶数
- 端点取值

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先设 \(f(t)=a^t\)，把 \(a^{1/x}-a^{1/(x+1)}\) 写成 \(f(1/x)-f(1/(x+1))\)，再用拉格朗日中值定理降阶。 |
| missed_action | 没有先把函数差值识别为可用拉格朗日中值定理降阶的结构，后续主阶判断边界也漏掉了等号。 |
| related_method_card_id | H06-001 |
| next_reminder | 看到指数函数在相邻小变量处的差，先改写成函数差值并用中值定理降阶，再讨论幂指数边界是否含等号。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-159_参数边界错误]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-KNOWLEDGE-021_拉格朗日中值定理]]
- [[MATHWIKI-KNOWLEDGE-051_无穷小阶数比较]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]
- [[MATHWIKI-METHOD-CLUSTER-036_中值定理]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-438
- GS-028
- GS-020
- GS-026
- GS-081

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
