---
wiki_id: SRC-WQ-GS-310
type: source_summary
title: "GS-310 135836 绝对正弦整周期积分"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-310_强化例题11.6.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-310"
knowledge:
  - "定积分"
  - "定积分等式"
  - "定积分性质"
  - "第一类换元"
  - "周期函数"
error_causes:
  - "触发信息遗漏"
  - "方法论调取失败"
methods:
  - "定积分换元"
  - "周期性积分"
  - "区间平移"
  - "绝对值三角函数积分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-084_定积分等式"
  - "MATHWIKI-KNOWLEDGE-102_周期函数"
  - "MATHWIKI-METHOD-CLUSTER-078_区间平移"
  - "MATHWIKI-METHOD-CLUSTER-094_定积分换元"
  - "MATHWIKI-METHOD-CLUSTER-257_绝对值三角函数积分"
  - "MATHWIKI-METHOD-CLUSTER-340_周期性积分"
  - "MATHWIKI-GS-METHOD-040_绝对三角周期积分"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-310 135836 绝对正弦整周期积分

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-310_强化例题11.6.md`
- wrongnet ID：`GS-310`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 绝对值三角函数整周期积分 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分等式
- 定积分性质
- 第一类换元
- 周期函数

### 错因

- 触发信息遗漏
- 方法论调取失败

### 方法

- 定积分换元
- 周期性积分
- 区间平移
- 绝对值三角函数积分

### 陷阱

- 换元后上下限要同步乘 n，并带出 dx=dt/n
- |sin t| 的周期是 pi，长度 n pi 正好是 n 个整周期
- 不要只看原积分含 n 就误判结果一定与 n 有关

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先令 t=nx 并同步改上下限和 dx=dt/n |
| missed_action | 旧卡未记录用户个人动作缺口；可确认的复做断点是没有先换元并识别整周期 |
| related_method_card_id | H08-008 |
| next_reminder | 看到绝对三角函数含任意起点，先换元并检查区间长度是否为整周期。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-084_定积分等式]]
- [[MATHWIKI-KNOWLEDGE-102_周期函数]]
- [[MATHWIKI-METHOD-CLUSTER-078_区间平移]]
- [[MATHWIKI-METHOD-CLUSTER-094_定积分换元]]
- [[MATHWIKI-METHOD-CLUSTER-257_绝对值三角函数积分]]
- [[MATHWIKI-METHOD-CLUSTER-340_周期性积分]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-040_绝对三角周期积分]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-311

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
