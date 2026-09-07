---
wiki_id: SRC-WQ-GS-273
type: source_summary
title: "GS-273 2018年第15题"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-273_2018年第15题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-273"
knowledge:
  - "分部积分"
  - "根式整体换元"
error_causes:
  - "旧批量导入未记录个人错因；依据题图/解析确认的可复做断点是没有先用分部积分降低反三角复合项。"
methods:
  - "分部积分"
  - "第一类换元"
  - "根式整体换元"
  - "回代化简"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-251_旧批量导入未记录个人错因-依据题图-解析确认的可复做断点是没有先用分部积"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-125_根式整体换元"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-070_回代化简"
  - "MATHWIKI-METHOD-CLUSTER-166_根式整体换元"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-039_不定积分结构化化归入口"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-273 2018年第15题

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-273_2018年第15题.md`
- wrongnet ID：`GS-273`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 不定积分 |
| 题型 | 分部积分后换元的不定积分 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 分部积分
- 根式整体换元

### 错因

- 旧批量导入未记录个人错因；依据题图/解析确认的可复做断点是没有先用分部积分降低反三角复合项。

### 方法

- 分部积分
- 第一类换元
- 根式整体换元
- 回代化简

### 陷阱

- 换元后dx处理不完整
- 内层函数导数识别断点
- 换元后回代不彻底

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把 \(\arctan\sqrt{e^x-1}\) 作为 \(u\)，\(e^{2x}dx\) 作为 \(dv\) 做分部积分。 |
| missed_action | 旧卡未保存用户当时动作；当前可确认的复做断点是没有先用分部积分降低反三角复合项。 |
| related_method_card_id | H09-005 |
| next_reminder | 看到易求导复合函数乘易积分因子，先试分部积分，再处理剩余换元。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-251_旧批量导入未记录个人错因-依据题图-解析确认的可复做断点是没有先用分部积]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-125_根式整体换元]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-070_回代化简]]
- [[MATHWIKI-METHOD-CLUSTER-166_根式整体换元]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
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
