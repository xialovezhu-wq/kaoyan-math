---
wiki_id: SRC-WQ-GS-291
type: source_summary
title: "GS-291 强化例题9.21(19899)"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-291_强化例题9.21(19899).md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-291"
knowledge:
  - "定积分"
  - "分段函数积分"
  - "换元"
  - "平移变换"
error_causes:
  - "暂无明确个人错因（视觉证据仅支持复做入口）"
methods:
  - "整体换元"
  - "分段积分"
  - "区间平移"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-116_分段函数积分"
  - "MATHWIKI-KNOWLEDGE-177_平移变换"
  - "MATHWIKI-KNOWLEDGE-212_换元"
  - "MATHWIKI-METHOD-CLUSTER-078_区间平移"
  - "MATHWIKI-METHOD-CLUSTER-310_分段积分"
  - "MATHWIKI-METHOD-CLUSTER-383_整体换元"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-291 强化例题9.21(19899)

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-291_强化例题9.21(19899).md`
- wrongnet ID：`GS-291`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 分段函数平移定积分 |
| 日期 | 2026-05-07 |
| 状态 | 已掌握 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 分段函数积分
- 换元
- 平移变换

### 错因

- 暂无明确个人错因（视觉证据仅支持复做入口）

### 方法

- 整体换元
- 分段积分
- 区间平移

### 陷阱

- 先换元再分段
- 新区间是 [-3,1]
- 分段点是 u=0
- 指数项积分符号

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先令 \(u=x-1\)，把积分区间由 \([-2,2]\) 改成 \([-3,1]\)，再按 \(u=0\) 分段。 |
| missed_action | 用户已反馈复做正确；旧批量导入未记录原始个人错因，此处只保留快速复查入口。 |
| related_method_card_id | H09-001 |
| next_reminder | 分段函数复合自变量先换元，把分段点放到新变量轴上。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-116_分段函数积分]]
- [[MATHWIKI-KNOWLEDGE-177_平移变换]]
- [[MATHWIKI-KNOWLEDGE-212_换元]]
- [[MATHWIKI-METHOD-CLUSTER-078_区间平移]]
- [[MATHWIKI-METHOD-CLUSTER-310_分段积分]]
- [[MATHWIKI-METHOD-CLUSTER-383_整体换元]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
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
