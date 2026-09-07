---
wiki_id: SRC-WQ-GS-641
type: source_summary
title: "GS-641 57751 变上限辅助函数积分不等式"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-641_57751变上限辅助函数积分不等式.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-641"
knowledge:
  - "定积分"
  - "定积分性质"
  - "定积分不等式"
  - "变上限积分"
  - "构造辅助函数"
  - "函数值比较"
  - "一元函数微分学应用"
  - "单调性与极值"
error_causes:
  - "方法论调取失败"
  - "题型识别失败"
  - "动作链断裂"
  - "积分变量与上限变量混淆"
  - "符号漏写"
  - "证明结构不完整"
methods:
  - "构造辅助函数"
  - "变上限积分整体设F"
  - "变上限积分求导"
  - "乘积求导"
  - "导数判单调"
  - "积分保序"
  - "单调性放缩"
  - "常数项积分化"
  - "函数值比较"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-011_证明结构不完整"
  - "MATHWIKI-ERROR-CLUSTER-394_积分变量与上限变量混淆"
  - "MATHWIKI-ERROR-CLUSTER-403_符号漏写"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-068_定积分不等式"
  - "MATHWIKI-KNOWLEDGE-304_函数值比较"
  - "MATHWIKI-KNOWLEDGE-390_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-015_变上限积分求导"
  - "MATHWIKI-METHOD-CLUSTER-046_乘积求导"
  - "MATHWIKI-METHOD-CLUSTER-060_积分保序"
  - "MATHWIKI-METHOD-CLUSTER-090_函数值比较"
  - "MATHWIKI-METHOD-CLUSTER-209_变上限积分整体设F"
  - "MATHWIKI-METHOD-CLUSTER-225_常数项积分化"
  - "MATHWIKI-METHOD-CLUSTER-734_单调性放缩"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-072_积分不等式证明入口链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: 81bb38b5eb56a59ecabdf78f1804b4332800904436a442c8a572dba8bb3cbe26
---

# GS-641 57751 变上限辅助函数积分不等式

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-641_57751变上限辅助函数积分不等式.md`
- wrongnet ID：`GS-641`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 单调函数积分不等式：变上限辅助函数与导数判单调证明 |
| 日期 | 2026-06-29 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 4 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 定积分不等式
- 变上限积分
- 构造辅助函数
- 函数值比较
- 一元函数微分学应用
- 单调性与极值

### 错因

- 方法论调取失败
- 题型识别失败
- 动作链断裂
- 积分变量与上限变量混淆
- 符号漏写
- 证明结构不完整

### 方法

- 构造辅助函数
- 变上限积分整体设F
- 变上限积分求导
- 乘积求导
- 导数判单调
- 积分保序
- 单调性放缩
- 常数项积分化
- 函数值比较
- 条件转化

### 陷阱

- 固定上限不会变量化
- 辅助函数 \(F(t)\) 与原函数 \(f(t)\) 混淆
- 变上限积分求导时把 \(dx\) 误认为只能对 \(x\) 求导
- 乘积求导漏括号
- \(-\frac12\int_a^t f(x)\,dx\) 的负号漏写
- \((t-a)f(t)\) 未改写为 \(\int_a^t f(t)\,dx\)
- 单调性比较必须放在同一区间积分内

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 \(F(t)=\int_a^t x f(x)\,dx-\frac{a+t}{2}\int_a^t f(x)\,dx\)，并检查 \(F(a)=0\)。 |
| missed_action | 没有想到把固定上限 \(b\) 变量化构造 \(F(t)\)；求导化简时混淆积分变量与上限变量，漏掉 \(-\frac12\int_a^t f(x)\,dx\) 的负号，也没有把 \((t-a)f(t)\) 改写为 \(\int_a^t f(t)\,dx\) 来同区间比较。 |
| related_method_card_id | H11-007 |
| next_reminder | 看到单调函数的积分不等式，先移项，把固定上限改成变量 \(t\) 构造 \(F(t)\)；求 \(F'(t)\) 时保留负号，再把 \((t-a)f(t)\) 写成 \(\int_a^t f(t)\,dx\) 与 \(\int_a^t f(x)\,dx\) 同区间比较。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-011_证明结构不完整]]
- [[MATHWIKI-ERROR-CLUSTER-394_积分变量与上限变量混淆]]
- [[MATHWIKI-ERROR-CLUSTER-403_符号漏写]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-068_定积分不等式]]
- [[MATHWIKI-KNOWLEDGE-304_函数值比较]]
- [[MATHWIKI-KNOWLEDGE-390_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-015_变上限积分求导]]
- [[MATHWIKI-METHOD-CLUSTER-046_乘积求导]]
- [[MATHWIKI-METHOD-CLUSTER-060_积分保序]]
- [[MATHWIKI-METHOD-CLUSTER-090_函数值比较]]
- [[MATHWIKI-METHOD-CLUSTER-209_变上限积分整体设F]]
- [[MATHWIKI-METHOD-CLUSTER-225_常数项积分化]]
- [[MATHWIKI-METHOD-CLUSTER-734_单调性放缩]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
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
