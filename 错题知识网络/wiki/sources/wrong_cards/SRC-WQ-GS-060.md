---
wiki_id: SRC-WQ-GS-060
type: source_summary
title: "GS-060 1000题强化3.25"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-060_1000题强化3.25.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-060"
knowledge:
  - "一元函数微分学应用"
  - "导数定义"
error_causes:
  - "方法论调取不稳"
  - "触发信息遗漏"
methods:
  - "导数定义拆差商"
  - "取绝对值"
  - "有界性放缩"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-006_导数定义"
  - "MATHWIKI-METHOD-CLUSTER-030_取绝对值"
  - "MATHWIKI-METHOD-CLUSTER-031_有界性放缩"
  - "MATHWIKI-METHOD-CLUSTER-117_导数定义拆差商"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-013_导数定义差商入口"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-060 1000题强化3.25

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-060_1000题强化3.25.md`
- wrongnet ID：`GS-060`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 导数定义型不等式证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 导数定义

### 错因

- 方法论调取不稳
- 触发信息遗漏

### 方法

- 导数定义拆差商
- 取绝对值
- 有界性放缩

### 陷阱

- 系数和对应导数
- 绝对值不等式放缩
- $f(0)=0$ 隐含检查

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把 $a_1+2a_2+\cdots+na_n$ 识别为 $f'(0)$。 |
| missed_action | 没有先把待证代数和与 $f'(0)$ 建立对应关系。 |
| related_method_card_id | H03-001 |
| next_reminder | 看到三角多项式系数加权和，先求 $f'(0)$，再用导数定义和题设不等式放缩。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-006_导数定义]]
- [[MATHWIKI-METHOD-CLUSTER-030_取绝对值]]
- [[MATHWIKI-METHOD-CLUSTER-031_有界性放缩]]
- [[MATHWIKI-METHOD-CLUSTER-117_导数定义拆差商]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-013_导数定义差商入口]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-095

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
