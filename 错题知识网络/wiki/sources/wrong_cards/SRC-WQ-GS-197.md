---
wiki_id: SRC-WQ-GS-197
type: source_summary
title: "GS-197 2019年第四题：由通解反求常系数微分方程参数"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-197_2019年第四题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-197"
knowledge:
  - "微分方程"
  - "高阶常系数线性微分方程"
  - "特征方程"
error_causes:
  - "题型入口风险：由齐次通解结构读重根，再用特解代回确定参数。"
methods:
  - "通解结构反推特征根"
  - "齐次解确定特征方程"
  - "特解代回求参数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-455_题型入口风险-由齐次通解结构读重根-再用特解代回确定参数"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-KNOWLEDGE-158_特征方程"
  - "MATHWIKI-KNOWLEDGE-160_高阶常系数线性微分方程"
  - "MATHWIKI-METHOD-CLUSTER-1197_特解代回求参数"
  - "MATHWIKI-METHOD-CLUSTER-1381_通解结构反推特征根"
  - "MATHWIKI-METHOD-CLUSTER-1435_齐次解确定特征方程"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-197 2019年第四题：由通解反求常系数微分方程参数

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-197_2019年第四题.md`
- wrongnet ID：`GS-197`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 高等数学-微分方程 |
| 题型 | 常系数非齐次线性微分方程反求参数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 微分方程
- 高阶常系数线性微分方程
- 特征方程

### 错因

- 题型入口风险：由齐次通解结构读重根，再用特解代回确定参数。

### 方法

- 通解结构反推特征根
- 齐次解确定特征方程
- 特解代回求参数

### 陷阱

- 先由齐次通解反推 $a,b$，不要正向硬解
- 出现 $(C_1+C_2x)e^{-x}$ 说明 $-1$ 是二重根
- 右端常数 $c$ 要用特解 $e^x$ 代回原方程确定

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先从 $(C_1+C_2x)e^{-x}$ 读出 $\lambda=-1$ 是二重根。 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有先读齐次解结构，而是正向硬解方程。 |
| related_method_card_id | H15-009 |
| next_reminder | 看到通解已给出，先读齐次部分的特征根和重数，再用特解代回求参数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-455_题型入口风险-由齐次通解结构读重根-再用特解代回确定参数]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-KNOWLEDGE-158_特征方程]]
- [[MATHWIKI-KNOWLEDGE-160_高阶常系数线性微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-1197_特解代回求参数]]
- [[MATHWIKI-METHOD-CLUSTER-1381_通解结构反推特征根]]
- [[MATHWIKI-METHOD-CLUSTER-1435_齐次解确定特征方程]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-195
- GS-196

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
