---
wiki_id: SRC-WQ-GS-053
type: source_summary
title: "GS-053 1000题B组11.6"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-053_1000题B组11.6.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-053"
knowledge:
  - "定积分"
  - "变上限积分"
  - "一元函数积分学的计算"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是先把 \\(f(x)\\) 还原为导数积分，再调用积分型柯西不等式并对 \\(x\\) 二次积分，需用户复做确认是否为当…"
methods:
  - "变量参数分离"
  - "取绝对值"
  - "有界性放缩"
  - "积分型柯西不等式"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-275_旧批量未记录个人原始错因-当前仅确认复做入口是先把-f-x-还原为导数积"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-METHOD-CLUSTER-030_取绝对值"
  - "MATHWIKI-METHOD-CLUSTER-031_有界性放缩"
  - "MATHWIKI-METHOD-CLUSTER-069_变量参数分离"
  - "MATHWIKI-METHOD-CLUSTER-440_积分型柯西不等式"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-072_积分不等式证明入口链"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-053 1000题B组11.6

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-053_1000题B组11.6.md`
- wrongnet ID：`GS-053`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 积分型柯西不等式证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 变上限积分
- 一元函数积分学的计算

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是先把 \(f(x)\) 还原为导数积分，再调用积分型柯西不等式并对 \(x\) 二次积分，需用户复做确认是否为当…

### 方法

- 变量参数分离
- 取绝对值
- 有界性放缩
- 积分型柯西不等式

### 陷阱

- 积分上限变量
- 二次积分放缩
- 常数因子提取

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 \(f(x)=\int_a^x f'(t)\,dt\)，再对 \(\int_a^x f'(t)\cdot1\,dt\) 用 Cauchy-Schwarz。 |
| missed_action | 个人原始作答未记录；当前只把题图解析确认的导数积分化入口登记为复做检查点。 |
| related_method_card_id | H11-007 |
| next_reminder | 看到 \(f^2\) 与 \((f')^2\) 的积分不等式，先把 \(f\) 还原为导数积分，再用积分型柯西。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-275_旧批量未记录个人原始错因-当前仅确认复做入口是先把-f-x-还原为导数积]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-METHOD-CLUSTER-030_取绝对值]]
- [[MATHWIKI-METHOD-CLUSTER-031_有界性放缩]]
- [[MATHWIKI-METHOD-CLUSTER-069_变量参数分离]]
- [[MATHWIKI-METHOD-CLUSTER-440_积分型柯西不等式]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-072_积分不等式证明入口链]]
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
