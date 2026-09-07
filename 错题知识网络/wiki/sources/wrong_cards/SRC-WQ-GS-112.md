---
wiki_id: SRC-WQ-GS-112
type: source_summary
title: "GS-112 1000讲B组4.15 2026.4.1"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-112_1000讲B组4.152026.4.1.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-112"
knowledge:
  - "一元函数微分学应用"
  - "高阶导数"
  - "泰勒公式"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是看到 $f^{(2n)}(0)$ 时没有先展开几何级数并读系数，需用户复做确认。"
methods:
  - "几何级数展开"
  - "麦克劳林系数对照"
  - "由系数读取高阶导数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-341_旧批量未记录个人原始错因-当前仅确认复做断点是看到$f^{-2n-}-0"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-KNOWLEDGE-027_高阶导数"
  - "MATHWIKI-METHOD-CLUSTER-142_几何级数展开"
  - "MATHWIKI-METHOD-CLUSTER-247_由系数读取高阶导数"
  - "MATHWIKI-METHOD-CLUSTER-475_麦克劳林系数对照"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-112 1000讲B组4.15 2026.4.1

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-112_1000讲B组4.152026.4.1.md`
- wrongnet ID：`GS-112`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 高阶导数系数对照 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 高阶导数
- 泰勒公式

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是看到 $f^{(2n)}(0)$ 时没有先展开几何级数并读系数，需用户复做确认。

### 方法

- 几何级数展开
- 麦克劳林系数对照
- 由系数读取高阶导数

### 陷阱

- 直接硬求高阶导
- 漏掉只有偶次幂有非零系数
- 忽略展开适用邻域

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写出 $f(x)=x^2/(1-x^2)=x^2+x^4+x^6+\\cdots$ |
| missed_action | 旧批量未记录个人步骤；当前复做风险是直接硬求 $2n$ 阶导数，没有转成系数读取 |
| related_method_card_id | H04-001 |
| next_reminder | 看到 $f^{(n)}(0)$ 且函数可展开，先写级数，再用 $n!$ 乘对应系数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-341_旧批量未记录个人原始错因-当前仅确认复做断点是看到$f^{-2n-}-0]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-KNOWLEDGE-027_高阶导数]]
- [[MATHWIKI-METHOD-CLUSTER-142_几何级数展开]]
- [[MATHWIKI-METHOD-CLUSTER-247_由系数读取高阶导数]]
- [[MATHWIKI-METHOD-CLUSTER-475_麦克劳林系数对照]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-117

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
