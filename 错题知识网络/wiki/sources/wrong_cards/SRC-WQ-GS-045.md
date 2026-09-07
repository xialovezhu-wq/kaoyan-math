---
wiki_id: SRC-WQ-GS-045
type: source_summary
title: "GS-045 1000题B组11.3"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-045_1000题B组11.3.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-045"
knowledge:
  - "定积分"
  - "中值定理"
  - "一元函数微分学应用"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是把 \\(|f'|\\le1\\) 转成两端点出发的线性包络并分段积分，需用户复做确认是否为当时第一断点。"
methods:
  - "拉格朗日中值定理"
  - "特殊值检验"
  - "区间拆分"
  - "有界性放缩"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-290_旧批量未记录个人原始错因-当前仅确认复做入口是把-f'-le1-转成两端"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-METHOD-CLUSTER-014_拉格朗日中值定理"
  - "MATHWIKI-METHOD-CLUSTER-031_有界性放缩"
  - "MATHWIKI-METHOD-CLUSTER-048_区间拆分"
  - "MATHWIKI-METHOD-CLUSTER-075_特殊值检验"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-072_积分不等式证明入口链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-045 1000题B组11.3

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-045_1000题B组11.3.md`
- wrongnet ID：`GS-045`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 导数有界积分估计 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 中值定理
- 一元函数微分学应用

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是把 \(|f'|\le1\) 转成两端点出发的线性包络并分段积分，需用户复做确认是否为当时第一断点。

### 方法

- 拉格朗日中值定理
- 特殊值检验
- 区间拆分
- 有界性放缩

### 陷阱

- 端点取值
- 可导性限制
- 等号不可取

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先在 \([0,\frac12]\) 用 \(f(0)\) 得 \(1-x\le f(x)\le1+x\)，在 \([\frac12,1]\) 用 \(f(1)\) 得 \(x\le f(x)\le2-x\)。 |
| missed_action | 个人原始作答未记录；当前只把题图解析确认的端点线性包络入口登记为复做检查点。 |
| related_method_card_id | H11-007 |
| next_reminder | 端点值加导数有界，先写端点线性包络，再分段积分夹逼。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-290_旧批量未记录个人原始错因-当前仅确认复做入口是把-f'-le1-转成两端]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-014_拉格朗日中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-031_有界性放缩]]
- [[MATHWIKI-METHOD-CLUSTER-048_区间拆分]]
- [[MATHWIKI-METHOD-CLUSTER-075_特殊值检验]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-072_积分不等式证明入口链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
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
