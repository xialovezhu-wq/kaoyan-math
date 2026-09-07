---
wiki_id: SRC-WQ-GS-246
type: source_summary
title: "GS-246 1000题A组6.18"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-246_1000题A组6.18.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-246"
knowledge:
  - "一元函数微分学应用"
  - "单调性与极值"
  - "凹凸性与拐点"
  - "不等式证明"
error_causes:
  - "旧批量未记录个人原始错因；当前可确认的复做断点是没有先把对称幂和不等式整体转成闭区间最值问题。"
methods:
  - "构造函数"
  - "导数判极值"
  - "端点比较"
  - "凸性判断"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-350_旧批量未记录个人原始错因-当前可确认的复做断点是没有先把对称幂和不等式整"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-018_凹凸性与拐点"
  - "MATHWIKI-KNOWLEDGE-161_不等式证明"
  - "MATHWIKI-METHOD-CLUSTER-081_导数判极值"
  - "MATHWIKI-METHOD-CLUSTER-404_构造函数"
  - "MATHWIKI-METHOD-CLUSTER-446_端点比较"
  - "MATHWIKI-METHOD-CLUSTER-649_凸性判断"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: f4f669639193e24fbad2c94152bec80f95ae7d0963442ba099c34d77a2f64589
---

# GS-246 1000题A组6.18

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-246_1000题A组6.18.md`
- wrongnet ID：`GS-246`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 函数最值证明不等式 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 单调性与极值
- 凹凸性与拐点
- 不等式证明

### 错因

- 旧批量未记录个人原始错因；当前可确认的复做断点是没有先把对称幂和不等式整体转成闭区间最值问题。

### 方法

- 构造函数
- 导数判极值
- 端点比较
- 凸性判断

### 陷阱

- p大于1保证导数符号
- 内点取最小值
- 端点取最大值

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先构造 \(F(x)=x^p+(1-x)^p\)，再求导找驻点并比较端点。 |
| missed_action | 旧批量未记录原始作答；当前复做入口显示容易直接代数估计，漏掉闭区间最值框架。 |
| related_method_card_id | H05-006 |
| next_reminder | 看到对称幂和不等式，先把上下界转成闭区间最小值和最大值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-350_旧批量未记录个人原始错因-当前可确认的复做断点是没有先把对称幂和不等式整]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-018_凹凸性与拐点]]
- [[MATHWIKI-KNOWLEDGE-161_不等式证明]]
- [[MATHWIKI-METHOD-CLUSTER-081_导数判极值]]
- [[MATHWIKI-METHOD-CLUSTER-404_构造函数]]
- [[MATHWIKI-METHOD-CLUSTER-446_端点比较]]
- [[MATHWIKI-METHOD-CLUSTER-649_凸性判断]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

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
