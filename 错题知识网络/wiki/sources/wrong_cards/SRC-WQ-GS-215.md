---
wiki_id: SRC-WQ-GS-215
type: source_summary
title: "GS-215 强化例题6.6"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-215_强化例题6.6.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-215"
knowledge:
  - "一元函数微分学应用"
  - "定积分"
  - "积分中值定理"
  - "罗尔定理"
  - "中值定理"
error_causes:
  - "旧批量导入未记录用户个人错因；本轮仅按题图、解析入口和方法页确认“构造变上限积分并分部积分换正权”的复做断点，待用户复做后确认实际漏点。"
methods:
  - "分部积分"
  - "积分中值定理"
  - "罗尔定理"
  - "构造辅助函数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-263_旧批量导入未记录用户个人错因-本轮仅按题图、解析入口和方法页确认“构造变"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-KNOWLEDGE-063_罗尔定理"
  - "MATHWIKI-KNOWLEDGE-159_积分中值定理"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-045_罗尔定理"
  - "MATHWIKI-METHOD-CLUSTER-102_积分中值定理"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-077_中值定理证明目标反推链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-215 强化例题6.6

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-215_强化例题6.6.md`
- wrongnet ID：`GS-215`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 积分条件推出两个零点 |
| 日期 | &id001 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 定积分
- 积分中值定理
- 罗尔定理
- 中值定理

### 错因

- 旧批量导入未记录用户个人错因；本轮仅按题图、解析入口和方法页确认“构造变上限积分并分部积分换正权”的复做断点，待用户复做后确认实际漏点。

### 方法

- 分部积分
- 积分中值定理
- 罗尔定理
- 构造辅助函数

### 陷阱

- 权函数变号
- 正权函数
- 两次罗尔

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先令 F(x)=int_0^x f(t)dt，并对带 cos x 的积分做分部积分 |
| missed_action | 没有先把 cos x 变号权通过分部积分换成 sin x 正权 |
| related_method_card_id | H11-006 |
| next_reminder | 看到积分条件推出多个零点，先构造变上限积分；若权函数变号，先分部积分换成正权。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-263_旧批量导入未记录用户个人错因-本轮仅按题图、解析入口和方法页确认“构造变]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-KNOWLEDGE-063_罗尔定理]]
- [[MATHWIKI-KNOWLEDGE-159_积分中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-045_罗尔定理]]
- [[MATHWIKI-METHOD-CLUSTER-102_积分中值定理]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-077_中值定理证明目标反推链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-216
- GS-218
- GS-031
- GS-214

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
