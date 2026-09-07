---
wiki_id: SRC-WQ-GS-247
type: source_summary
title: "GS-247 84256 质心横坐标凸性不等式"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-247_1000题B组10.24.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-247"
knowledge:
  - "定积分应用"
  - "定积分不等式"
  - "二阶导数判凹凸性"
error_causes:
  - "旧批量未记录个人原始错因；当前可确认的复做断点是没有先把质心横坐标翻译成矩积分比值，再交叉相乘构造辅助函数。"
methods:
  - "质心公式"
  - "构造辅助函数"
  - "拉格朗日中值定理"
  - "凸函数判号"
  - "积分不等式"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-352_旧批量未记录个人原始错因-当前可确认的复做断点是没有先把质心横坐标翻译成"
  - "MATHWIKI-KNOWLEDGE-035_定积分应用"
  - "MATHWIKI-KNOWLEDGE-068_定积分不等式"
  - "MATHWIKI-KNOWLEDGE-098_二阶导数判凹凸性"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-014_拉格朗日中值定理"
  - "MATHWIKI-METHOD-CLUSTER-1340_质心公式"
  - "MATHWIKI-METHOD-CLUSTER-172_积分不等式"
  - "MATHWIKI-METHOD-CLUSTER-301_凸函数判号"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-053_质心横坐标积分比值证明链"
  - "MATHWIKI-GS-METHOD-072_积分不等式证明入口链"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-25
related_wrongnet_refs: []
formal_projection_sha256: a48ed194c4354582885218f0e3b57b804a9a8d4a86f0e64b9b0c109591b18e9f
---

# GS-247 84256 质心横坐标凸性不等式

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-247_1000题B组10.24.md`
- wrongnet ID：`GS-247`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 质心横坐标不等式证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 4 |

## 可编译信息

### 知识点

- 定积分应用
- 定积分不等式
- 二阶导数判凹凸性

### 错因

- 旧批量未记录个人原始错因；当前可确认的复做断点是没有先把质心横坐标翻译成矩积分比值，再交叉相乘构造辅助函数。

### 方法

- 质心公式
- 构造辅助函数
- 拉格朗日中值定理
- 凸函数判号
- 积分不等式

### 陷阱

- 不要把质心横坐标当成图形中点
- 目标 \(\bar x>\frac23a\) 要先化成积分不等式
- \(f''>0\) 应转成 \(f'\) 单调递增，再配合中值定理比较 \(f(a)-f(0)\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 \(\bar x=\frac{\int_0^a x f(x)\,dx}{\int_0^a f(x)\,dx}\)。 |
| missed_action | 旧批量未记录原始作答；当前复做入口显示容易停在图形直觉，漏掉质心横坐标的矩积分公式。 |
| related_method_card_id | H10-005 |
| next_reminder | 看到质心横坐标，先写矩积分比值，再交叉相乘构造变量上限辅助函数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-352_旧批量未记录个人原始错因-当前可确认的复做断点是没有先把质心横坐标翻译成]]
- [[MATHWIKI-KNOWLEDGE-035_定积分应用]]
- [[MATHWIKI-KNOWLEDGE-068_定积分不等式]]
- [[MATHWIKI-KNOWLEDGE-098_二阶导数判凹凸性]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-014_拉格朗日中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-1340_质心公式]]
- [[MATHWIKI-METHOD-CLUSTER-172_积分不等式]]
- [[MATHWIKI-METHOD-CLUSTER-301_凸函数判号]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-053_质心横坐标积分比值证明链]]
- [[MATHWIKI-GS-METHOD-072_积分不等式证明入口链]]
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
