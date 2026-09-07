---
wiki_id: SRC-WQ-GS-338
type: source_summary
title: "GS-338 2020年第16题"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-338_2020年第16题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-338"
knowledge:
  - "定积分"
  - "含参定积分"
  - "第一类换元"
  - "变限积分"
  - "导数定义"
  - "极限与连续"
  - "洛必达法则"
error_causes:
  - "变量混淆"
  - "条件检查遗漏"
methods:
  - "定积分换元"
  - "变上限积分求导"
  - "导数定义"
  - "洛必达法则"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-024_变量混淆"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-006_导数定义"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-045_洛必达法则"
  - "MATHWIKI-KNOWLEDGE-119_含参定积分"
  - "MATHWIKI-KNOWLEDGE-200_变限积分"
  - "MATHWIKI-METHOD-CLUSTER-013_导数定义"
  - "MATHWIKI-METHOD-CLUSTER-015_变上限积分求导"
  - "MATHWIKI-METHOD-CLUSTER-094_定积分换元"
  - "MATHWIKI-METHOD-CLUSTER-099_洛必达法则"
  - "MATHWIKI-GS-METHOD-013_导数定义差商入口"
  - "MATHWIKI-GS-METHOD-071_含参积分变量角色与特殊点定义法"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-338 2020年第16题

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-338_2020年第16题.md`
- wrongnet ID：`GS-338`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 含参积分函数求导与导数连续性证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 含参定积分
- 第一类换元
- 变限积分
- 导数定义
- 极限与连续
- 洛必达法则

### 错因

- 变量混淆
- 条件检查遗漏

### 方法

- 定积分换元
- 变上限积分求导
- 导数定义
- 洛必达法则

### 陷阱

- 积分变量与参数混淆
- 特殊点不能直接套 x≠0 的表达式
- 未证明导函数在分段点连续

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先令 \(u=xt\)，把 \(x\ne0\) 时的 \(g(x)\) 改写为 \(\frac1x\int_0^x f(u)\,du\) |
| missed_action | 没有先把含参积分改写成变上限积分并单独处理 \(x=0\) |
| related_method_card_id | H09-008 |
| next_reminder | 看到 \(\int_0^1 f(xt)\,dt\)，先分清积分变量和外部参数，再换元并单独检查特殊点。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-024_变量混淆]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-006_导数定义]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-045_洛必达法则]]
- [[MATHWIKI-KNOWLEDGE-119_含参定积分]]
- [[MATHWIKI-KNOWLEDGE-200_变限积分]]
- [[MATHWIKI-METHOD-CLUSTER-013_导数定义]]
- [[MATHWIKI-METHOD-CLUSTER-015_变上限积分求导]]
- [[MATHWIKI-METHOD-CLUSTER-094_定积分换元]]
- [[MATHWIKI-METHOD-CLUSTER-099_洛必达法则]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-013_导数定义差商入口]]
- [[MATHWIKI-GS-METHOD-071_含参积分变量角色与特殊点定义法]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-186

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
