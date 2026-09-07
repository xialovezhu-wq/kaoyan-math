---
wiki_id: SRC-WQ-GS-129
type: source_summary
title: "GS-129 102310 反函数分段表达"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-129_1023102026.4.16T2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-129"
knowledge:
  - "极限与连续"
  - "函数单调性"
  - "反函数"
  - "反三角函数主值"
  - "三角函数"
error_causes:
  - "概念混淆"
  - "题面语言翻译断点"
  - "函数自变量识别混淆"
methods:
  - "单调区间分段"
  - "变量互换"
  - "反三角函数主值化"
  - "诱导公式"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-005_A-CONCEPT"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-020_题面语言翻译断点"
  - "MATHWIKI-ERROR-CLUSTER-042_函数自变量识别混淆"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-071_函数单调性"
  - "MATHWIKI-KNOWLEDGE-170_反三角函数主值"
  - "MATHWIKI-KNOWLEDGE-171_反函数"
  - "MATHWIKI-KNOWLEDGE-285_三角函数"
  - "MATHWIKI-METHOD-CLUSTER-1336_诱导公式"
  - "MATHWIKI-METHOD-CLUSTER-210_变量互换"
  - "MATHWIKI-METHOD-CLUSTER-728_单调区间分段"
  - "MATHWIKI-METHOD-CLUSTER-771_反三角函数主值化"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-129 102310 反函数分段表达

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-129_1023102026.4.16T2.md`
- wrongnet ID：`GS-129`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 反函数分段表达 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 函数单调性
- 反函数
- 反三角函数主值
- 三角函数

### 错因

- 概念混淆
- 题面语言翻译断点
- 函数自变量识别混淆

### 方法

- 单调区间分段
- 变量互换
- 反三角函数主值化
- 诱导公式

### 陷阱

- 反函数定义域值域互换
- arcsin主值范围
- 区间单调性

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-CONCEPT |
| expected_first_action | 先用 \(\cos x\) 的符号把 \([0,2\pi]\) 切成 \([0,\pi/2]\)、\([\pi/2,3\pi/2]\)、\([3\pi/2,2\pi]\) 三段单调区间 |
| missed_action | 没有先区分原函数变量与反函数变量，误把 \(\arcsin(y)=x\) 写成 \(y=\arcsin x\)，并忽略 \(\arcsin\) 的主值范围 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到三角函数反函数，先切单调区间并写值域，再把 \(x\) 表示为关于 \(y\) 的函数；超出主值区间时用诱导公式拉回。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-005_A-CONCEPT]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-020_题面语言翻译断点]]
- [[MATHWIKI-ERROR-CLUSTER-042_函数自变量识别混淆]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-071_函数单调性]]
- [[MATHWIKI-KNOWLEDGE-170_反三角函数主值]]
- [[MATHWIKI-KNOWLEDGE-171_反函数]]
- [[MATHWIKI-KNOWLEDGE-285_三角函数]]
- [[MATHWIKI-METHOD-CLUSTER-1336_诱导公式]]
- [[MATHWIKI-METHOD-CLUSTER-210_变量互换]]
- [[MATHWIKI-METHOD-CLUSTER-728_单调区间分段]]
- [[MATHWIKI-METHOD-CLUSTER-771_反三角函数主值化]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

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
