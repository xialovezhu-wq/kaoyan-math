---
wiki_id: SRC-WQ-GS-270
type: source_summary
title: "GS-270 强化例题9.3（2）"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-270_强化例题9.3（2）.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-270"
knowledge:
  - "不定积分"
  - "根式积分"
  - "根式整体换元"
  - "部分分式"
  - "回代化简"
error_causes:
  - "暂无明确个人错因（视觉证据仅支持复做入口）"
methods:
  - "根式整体换元"
  - "指数换元"
  - "部分分式"
  - "反代合并对数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-046_部分分式"
  - "MATHWIKI-KNOWLEDGE-058_根式积分"
  - "MATHWIKI-KNOWLEDGE-120_回代化简"
  - "MATHWIKI-KNOWLEDGE-125_根式整体换元"
  - "MATHWIKI-METHOD-CLUSTER-035_部分分式"
  - "MATHWIKI-METHOD-CLUSTER-160_指数换元"
  - "MATHWIKI-METHOD-CLUSTER-166_根式整体换元"
  - "MATHWIKI-METHOD-CLUSTER-774_反代合并对数"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-043_根式积分换元与回代链"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-270 强化例题9.3（2）

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-270_强化例题9.3（2）.md`
- wrongnet ID：`GS-270`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 不定积分 |
| 题型 | 指数根式整体换元 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 不定积分
- 根式积分
- 根式整体换元
- 部分分式
- 回代化简

### 错因

- 暂无明确个人错因（视觉证据仅支持复做入口）

### 方法

- 根式整体换元
- 指数换元
- 部分分式
- 反代合并对数

### 陷阱

- dx 同步替换
- t 的定义域
- 部分分式系数
- 对数绝对值

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先令 t=sqrt(e^x+1)，写出 e^x=t^2-1 和 dx=2t/(t^2-1)dt |
| missed_action | 旧卡未记录用户实际漏步；复做风险是只换根号，没有同步写出 e^x 与 dx，导致不能转入部分分式 |
| related_method_card_id | H09-003 |
| next_reminder | 看到指数根式，先整体设根式为 t，再同步改写 e^x 和 dx。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-046_部分分式]]
- [[MATHWIKI-KNOWLEDGE-058_根式积分]]
- [[MATHWIKI-KNOWLEDGE-120_回代化简]]
- [[MATHWIKI-KNOWLEDGE-125_根式整体换元]]
- [[MATHWIKI-METHOD-CLUSTER-035_部分分式]]
- [[MATHWIKI-METHOD-CLUSTER-160_指数换元]]
- [[MATHWIKI-METHOD-CLUSTER-166_根式整体换元]]
- [[MATHWIKI-METHOD-CLUSTER-774_反代合并对数]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-043_根式积分换元与回代链]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-603
- GS-604

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
