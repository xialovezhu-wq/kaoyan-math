---
wiki_id: SRC-WQ-GS-163
type: source_summary
title: "GS-163 强化例题9.13（135756）"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-163_强化例题9.13（135756）.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-163"
knowledge:
  - "不定积分"
  - "一元函数积分学的计算"
  - "三角函数有理式"
  - "部分分式"
  - "回代化简"
error_causes:
  - "公式记错"
  - "过程跳步"
methods:
  - "三角函数有理式"
  - "第一类换元"
  - "部分分式"
  - "回代化简"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-015_公式记错"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-046_部分分式"
  - "MATHWIKI-KNOWLEDGE-079_三角函数有理式"
  - "MATHWIKI-KNOWLEDGE-120_回代化简"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-035_部分分式"
  - "MATHWIKI-METHOD-CLUSTER-055_三角函数有理式"
  - "MATHWIKI-METHOD-CLUSTER-070_回代化简"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-163 强化例题9.13（135756）

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-163_强化例题9.13（135756）.md`
- wrongnet ID：`GS-163`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 不定积分 |
| 题型 | 三角函数有理式不定积分 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 不定积分
- 一元函数积分学的计算
- 三角函数有理式
- 部分分式
- 回代化简

### 错因

- 公式记错
- 过程跳步

### 方法

- 三角函数有理式
- 第一类换元
- 部分分式
- 回代化简

### 陷阱

- 换元后dx同步替换
- 反代对数项未合并

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把 \(\frac{2\sin x+\cos x}{\sin x+2\cos x}\) 同除以 \(\cos x\)，写成 \(\frac{2\tan x+1}{\tan x+2}\)。 |
| missed_action | 没有先完整写 \(t=\tan x,\ dx=\frac{dt}{1+t^2}\)，导致换元微分和后续部分分式链断。 |
| related_method_card_id | H09-001 |
| next_reminder | 看到三角一次式比一次式的不定积分，先同除以 \(\cos x\) 化成 \(\tan x\)，再写 \(t=\tan x,\ dx=\frac{dt}{1+t^2}\) 并做部分分式。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-015_公式记错]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-046_部分分式]]
- [[MATHWIKI-KNOWLEDGE-079_三角函数有理式]]
- [[MATHWIKI-KNOWLEDGE-120_回代化简]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-035_部分分式]]
- [[MATHWIKI-METHOD-CLUSTER-055_三角函数有理式]]
- [[MATHWIKI-METHOD-CLUSTER-070_回代化简]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-603

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
