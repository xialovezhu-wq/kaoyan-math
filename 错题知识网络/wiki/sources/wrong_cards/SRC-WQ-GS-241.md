---
wiki_id: SRC-WQ-GS-241
type: source_summary
title: "GS-241 1000题B组6.16"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-241_1000题B组6.16.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-241"
knowledge:
  - "一元函数微分学应用"
  - "泰勒公式"
  - "零点定理"
  - "极限与连续"
  - "参数范围"
error_causes:
  - "旧批量未记录个人原始错因；当前可确认的复做断点是没有把存在根的参数范围拆成近零主部必要条件和端点符号充分性。"
methods:
  - "构造辅助函数"
  - "泰勒展开"
  - "端点符号判定"
  - "介值定理"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-354_旧批量未记录个人原始错因-当前可确认的复做断点是没有把存在根的参数范围拆"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-KNOWLEDGE-042_零点定理"
  - "MATHWIKI-KNOWLEDGE-100_参数范围"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-008_泰勒展开"
  - "MATHWIKI-METHOD-CLUSTER-1278_端点符号判定"
  - "MATHWIKI-METHOD-CLUSTER-140_介值定理"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-241 1000题B组6.16

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-241_1000题B组6.16.md`
- wrongnet ID：`GS-241`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 参数方程有根范围 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 泰勒公式
- 零点定理
- 极限与连续
- 参数范围

### 错因

- 旧批量未记录个人原始错因；当前可确认的复做断点是没有把存在根的参数范围拆成近零主部必要条件和端点符号充分性。

### 方法

- 构造辅助函数
- 泰勒展开
- 端点符号判定
- 介值定理

### 陷阱

- 区间包含x=1
- 下端点闭开
- 近零三阶主部

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先构造 \(F(x)=x-\arctan x-kx^3\)，再展开近零三阶主部。 |
| missed_action | 旧批量未记录原始作答；当前复做入口显示容易漏掉近零主部与端点 \(1\) 开闭性的双重约束。 |
| related_method_card_id | H06-009 |
| next_reminder | 看到小区间参数方程有根，先查近零主部，再查端点符号和端点是否包含。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-354_旧批量未记录个人原始错因-当前可确认的复做断点是没有把存在根的参数范围拆]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-KNOWLEDGE-042_零点定理]]
- [[MATHWIKI-KNOWLEDGE-100_参数范围]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-1278_端点符号判定]]
- [[MATHWIKI-METHOD-CLUSTER-140_介值定理]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-215
- GS-216
- GS-239
- GS-240
- GS-244

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
