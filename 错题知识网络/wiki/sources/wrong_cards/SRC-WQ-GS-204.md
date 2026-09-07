---
wiki_id: SRC-WQ-GS-204
type: source_summary
title: "GS-204 强化例题15.15：曲率条件建立二阶可降阶方程"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-204_强化例题15.15.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-204"
knowledge:
  - "微分方程"
  - "二阶可降阶微分方程"
  - "曲率"
  - "曲率公式"
error_causes:
  - "题型入口风险：曲率与切线角统一写成导数，再用 $p=y^\\prime=p(y)$ 降阶。"
methods:
  - "曲率公式建模"
  - "三角关系转斜率"
  - "令 $p=y^\\prime$ 降阶"
  - "初值定常数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-452_题型入口风险-曲率与切线角统一写成导数-再用$p=y^-prime=p-"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-KNOWLEDGE-094_曲率"
  - "MATHWIKI-KNOWLEDGE-114_二阶可降阶微分方程"
  - "MATHWIKI-KNOWLEDGE-380_曲率公式"
  - "MATHWIKI-METHOD-CLUSTER-037_初值定常数"
  - "MATHWIKI-METHOD-CLUSTER-1073_曲率公式建模"
  - "MATHWIKI-METHOD-CLUSTER-512_三角关系转斜率"
  - "MATHWIKI-METHOD-CLUSTER-588_令$p=y^-prime$降阶"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-204 强化例题15.15：曲率条件建立二阶可降阶方程

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-204_强化例题15.15.md`
- wrongnet ID：`GS-204`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 高等数学-微分方程 |
| 题型 | 曲率公式与二阶可降阶微分方程 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 微分方程
- 二阶可降阶微分方程
- 曲率
- 曲率公式

### 错因

- 题型入口风险：曲率与切线角统一写成导数，再用 $p=y^\prime=p(y)$ 降阶。

### 方法

- 曲率公式建模
- 三角关系转斜率
- 令 $p=y^\prime$ 降阶
- 初值定常数

### 陷阱

- $\cos\alpha$ 要化为 $1/\sqrt{1+(y^\prime)^2}$
- 凹曲线条件对应曲率公式中取正的 $y^{\prime\prime}$
- 方程不显含 $x$ 后要用 $p(y)$ 降阶

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把曲率公式和 $\cos\alpha=\frac1{\sqrt{1+(y^\prime)^2}}$ 代入。 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有先把几何量转成导数，导致无法形成可降阶方程。 |
| related_method_card_id | H15-011 |
| next_reminder | 看到曲率和切线角条件，先全部翻译成 $y^\prime,y^{\prime\prime}$，再判断如何降阶。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-452_题型入口风险-曲率与切线角统一写成导数-再用$p=y^-prime=p-]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-KNOWLEDGE-094_曲率]]
- [[MATHWIKI-KNOWLEDGE-114_二阶可降阶微分方程]]
- [[MATHWIKI-KNOWLEDGE-380_曲率公式]]
- [[MATHWIKI-METHOD-CLUSTER-037_初值定常数]]
- [[MATHWIKI-METHOD-CLUSTER-1073_曲率公式建模]]
- [[MATHWIKI-METHOD-CLUSTER-512_三角关系转斜率]]
- [[MATHWIKI-METHOD-CLUSTER-588_令$p=y^-prime$降阶]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-193
- GS-211
- GS-205

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
