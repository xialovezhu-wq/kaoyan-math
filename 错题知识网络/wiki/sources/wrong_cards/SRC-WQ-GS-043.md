---
wiki_id: SRC-WQ-GS-043
type: source_summary
title: "GS-043 2020年数2真题"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-043_2020年数2真题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-043"
knowledge:
  - "极限与连续"
  - "定积分"
  - "变上限积分平均型极限"
  - "周期函数"
  - "夹逼准则"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是先把变上限周期积分夹到相邻整周期积分，再对 S(x)/x 做夹逼。"
methods:
  - "周期拆分"
  - "整周期积分"
  - "夹逼准则"
  - "定积分估值"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-276_旧批量未记录个人原始错因-当前仅确认复做入口是先把变上限周期积分夹到相邻"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-083_夹逼准则"
  - "MATHWIKI-KNOWLEDGE-102_周期函数"
  - "MATHWIKI-KNOWLEDGE-199_变上限积分平均型极限"
  - "MATHWIKI-METHOD-CLUSTER-016_夹逼准则"
  - "MATHWIKI-METHOD-CLUSTER-1053_整周期积分"
  - "MATHWIKI-METHOD-CLUSTER-832_周期拆分"
  - "MATHWIKI-METHOD-CLUSTER-893_定积分估值"
  - "MATHWIKI-GS-METHOD-040_绝对三角周期积分"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: 05d498bc5e56d6446e77f173307b528a23d3faaa1fcba406605c37857f486bfb
---

# GS-043 2020年数2真题

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-043_2020年数2真题.md`
- wrongnet ID：`GS-043`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 周期函数积分平均值极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 定积分
- 变上限积分平均型极限
- 周期函数
- 夹逼准则

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是先把变上限周期积分夹到相邻整周期积分，再对 S(x)/x 做夹逼。

### 方法

- 周期拆分
- 整周期积分
- 夹逼准则
- 定积分估值

### 陷阱

- 尾段有界误差
- 周期平均值
- 除以变量后的上下界
- 整周期与余段

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先由 \\(n\\pi\\le x<(n+1)\\pi\\) 写出 \\(\\int_0^{n\\pi}|\\cos t|dt\\le S(x)<\\int_0^{(n+1)\\pi}|\\cos t|dt\\)。 |
| missed_action | 待确认：个人错因未记录；从解析看最需要训练的是没有先把变上限积分夹到相邻整周期积分，再除以 \\(x\\) 形成同极限夹逼。 |
| related_method_card_id | H08-008 |
| next_reminder | 看到长区间周期函数积分平均值，先拆整周期和尾段，再把尾段作为有界误差用夹逼消掉。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-276_旧批量未记录个人原始错因-当前仅确认复做入口是先把变上限周期积分夹到相邻]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-083_夹逼准则]]
- [[MATHWIKI-KNOWLEDGE-102_周期函数]]
- [[MATHWIKI-KNOWLEDGE-199_变上限积分平均型极限]]
- [[MATHWIKI-METHOD-CLUSTER-016_夹逼准则]]
- [[MATHWIKI-METHOD-CLUSTER-1053_整周期积分]]
- [[MATHWIKI-METHOD-CLUSTER-832_周期拆分]]
- [[MATHWIKI-METHOD-CLUSTER-893_定积分估值]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-040_绝对三角周期积分]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

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
