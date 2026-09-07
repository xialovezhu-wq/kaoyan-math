---
wiki_id: SRC-WQ-GS-323
type: source_summary
title: "GS-323 强化例题11.15"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-323_强化例题11.15.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-323"
knowledge:
  - "定积分"
  - "变上限积分"
  - "分部积分"
  - "第二类换元"
error_causes:
  - "方法论调取失败"
  - "动作链断裂"
methods:
  - "分部积分升阶"
  - "指数配方"
  - "换元"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-041_第二类换元"
  - "MATHWIKI-METHOD-CLUSTER-009_换元"
  - "MATHWIKI-METHOD-CLUSTER-314_分部积分升阶"
  - "MATHWIKI-METHOD-CLUSTER-377_指数配方"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-323 强化例题11.15

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-323_强化例题11.15.md`
- wrongnet ID：`GS-323`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 变上限积分嵌套定积分 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 变上限积分
- 分部积分
- 第二类换元

### 错因

- 方法论调取失败
- 动作链断裂

### 方法

- 分部积分升阶
- 指数配方
- 换元

### 陷阱

- 没有把 f 通过分部积分换成 f''
- 指数配方中心漏掉
- 换元上下限方向漏改

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先对含 f 的定积分做分部积分 |
| missed_action | 没有先用分部积分把 f 换成已知的 f' |
| related_method_card_id | H11-005 |
| next_reminder | 看到变上限函数嵌入积分，先分部积分，把未知 f 换成已知 f'。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-METHOD-CLUSTER-009_换元]]
- [[MATHWIKI-METHOD-CLUSTER-314_分部积分升阶]]
- [[MATHWIKI-METHOD-CLUSTER-377_指数配方]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
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
