---
wiki_id: SRC-WQ-GS-275
type: source_summary
title: "GS-275 强化例题9.6（171647）"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-275_强化例题9.6（171647）.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-275"
knowledge:
  - "不定积分"
  - "分部积分"
  - "指数根式积分"
  - "第二类换元"
error_causes:
  - "暂无明确个人错因（视觉证据仅支持复做入口）"
methods:
  - "分部积分"
  - "整体凑微分"
  - "根式换元"
  - "对数回代"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-041_第二类换元"
  - "MATHWIKI-KNOWLEDGE-372_指数根式积分"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-032_整体凑微分"
  - "MATHWIKI-METHOD-CLUSTER-124_根式换元"
  - "MATHWIKI-METHOD-CLUSTER-910_对数回代"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-043_根式积分换元与回代链"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-275 强化例题9.6（171647）

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-275_强化例题9.6（171647）.md`
- wrongnet ID：`GS-275`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 不定积分 |
| 题型 | 指数根式分部积分 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 不定积分
- 分部积分
- 指数根式积分
- 第二类换元

### 错因

- 暂无明确个人错因（视觉证据仅支持复做入口）

### 方法

- 分部积分
- 整体凑微分
- 根式换元
- 对数回代

### 陷阱

- 先选 u=x
- 根式积分还要单独换元
- 回代时对数项不能漏
- 不要只换 e^x 不换 dx

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先取 u=x，dv=e^x/sqrt(e^x+1) dx，并求出 v=2sqrt(e^x+1) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有先按乘积分部选 u 和 dv，或把根式积分的换元链漏掉 |
| related_method_card_id | H09-005 |
| next_reminder | 看到 x 乘可积因子，先按分部积分取 u=x，再单独算 dv 的原函数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-KNOWLEDGE-372_指数根式积分]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-032_整体凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-124_根式换元]]
- [[MATHWIKI-METHOD-CLUSTER-910_对数回代]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-043_根式积分换元与回代链]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-269

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
