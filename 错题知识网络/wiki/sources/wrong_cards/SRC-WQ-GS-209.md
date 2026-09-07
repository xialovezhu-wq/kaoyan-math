---
wiki_id: SRC-WQ-GS-209
type: source_summary
title: "GS-209 1000题B组6.8"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-209_1000题B组6.8.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-209"
knowledge:
  - "一元函数微分学应用"
  - "微分不等式"
  - "辅助函数构造"
  - "积分因子"
  - "函数单调性"
  - "导数判单调"
  - "函数值不等式"
error_causes:
  - "暂无明确个人错因（本轮只有题图与折叠解析证据，未反推用户本人原始错因）"
methods:
  - "构造辅助函数"
  - "导数判单调"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-026_暂无明确个人错因（本轮只有题图与折叠解析证据-未反推用户本人原始错因）"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-071_函数单调性"
  - "MATHWIKI-KNOWLEDGE-076_辅助函数构造"
  - "MATHWIKI-KNOWLEDGE-091_导数判单调"
  - "MATHWIKI-KNOWLEDGE-099_函数值不等式"
  - "MATHWIKI-KNOWLEDGE-126_积分因子"
  - "MATHWIKI-KNOWLEDGE-209_微分不等式"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-209 1000题B组6.8

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-209_1000题B组6.8.md`
- wrongnet ID：`GS-209`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 导数不等式构造辅助函数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 微分不等式
- 辅助函数构造
- 积分因子
- 函数单调性
- 导数判单调
- 函数值不等式

### 错因

- 暂无明确个人错因（本轮只有题图与折叠解析证据，未反推用户本人原始错因）

### 方法

- 构造辅助函数
- 导数判单调
- 条件转化

### 陷阱

- 变量混淆
- 正负号
- 指数因子选择

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先构造 F(x)=f(x)e^{-2x} 并计算 F'(x) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有把 f'-2f 吸收到指数因子导数里 |
| related_method_card_id | H06-002 |
| next_reminder | 看到 f'-cf 型不等式，先构造 f(x)e^{-cx}，把条件转成单调性。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-026_暂无明确个人错因（本轮只有题图与折叠解析证据-未反推用户本人原始错因）]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-071_函数单调性]]
- [[MATHWIKI-KNOWLEDGE-076_辅助函数构造]]
- [[MATHWIKI-KNOWLEDGE-091_导数判单调]]
- [[MATHWIKI-KNOWLEDGE-099_函数值不等式]]
- [[MATHWIKI-KNOWLEDGE-126_积分因子]]
- [[MATHWIKI-KNOWLEDGE-209_微分不等式]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-184
- GS-191

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
