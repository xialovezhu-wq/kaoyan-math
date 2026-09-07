---
wiki_id: SRC-WQ-GS-205
type: source_summary
title: "GS-205 2020年第21题：面积比条件建立微分方程"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-205_2020年第21题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-205"
knowledge:
  - "微分方程"
  - "微分方程建模"
  - "平面图形面积"
  - "切线方程"
  - "变上限积分"
  - "二阶可降阶微分方程"
error_causes:
  - "题型入口风险：切线截距与两块面积先代数化，再对积分比例关系求导。"
methods:
  - "切线截距建模"
  - "面积关系建模"
  - "对积分关系求导"
  - "可降阶微分方程"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-450_题型入口风险-切线截距与两块面积先代数化-再对积分比例关系求导"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-KNOWLEDGE-060_平面图形面积"
  - "MATHWIKI-KNOWLEDGE-081_切线方程"
  - "MATHWIKI-KNOWLEDGE-114_二阶可降阶微分方程"
  - "MATHWIKI-KNOWLEDGE-147_微分方程建模"
  - "MATHWIKI-METHOD-CLUSTER-1418_面积关系建模"
  - "MATHWIKI-METHOD-CLUSTER-316_切线截距建模"
  - "MATHWIKI-METHOD-CLUSTER-818_可降阶微分方程"
  - "MATHWIKI-METHOD-CLUSTER-928_对积分关系求导"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-203"
  - "GS-204"
formal_projection_sha256: 8d4f0496d56406e9d4ffbde7e27bbf73059cea6a122f960ea65410530564f3c2
---

# GS-205 2020年第21题：面积比条件建立微分方程

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-205_2020年第21题.md`
- wrongnet ID：`GS-205`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 高等数学-微分方程 |
| 题型 | 几何面积关系建立微分方程 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 微分方程
- 微分方程建模
- 平面图形面积
- 切线方程
- 变上限积分
- 二阶可降阶微分方程

### 错因

- 题型入口风险：切线截距与两块面积先代数化，再对积分比例关系求导。

### 方法

- 切线截距建模
- 面积关系建模
- 对积分关系求导
- 可降阶微分方程

### 陷阱

- 三角形面积的底长来自切线截距，不是直接等于 $x$
- 面积比要先写成积分关系再求导
- 变量 $a$ 推导完要转成一般变量 $x$

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先取 $M(a,f(a))$，写切线截距、三角形面积和曲线下方面积。 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有先写面积关系，而直接猜曲线形状。 |
| related_method_card_id | H15-011 |
| next_reminder | 看到面积比例建模，先写几何量和积分关系，再对整体关系求导。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-450_题型入口风险-切线截距与两块面积先代数化-再对积分比例关系求导]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-KNOWLEDGE-060_平面图形面积]]
- [[MATHWIKI-KNOWLEDGE-081_切线方程]]
- [[MATHWIKI-KNOWLEDGE-114_二阶可降阶微分方程]]
- [[MATHWIKI-KNOWLEDGE-147_微分方程建模]]
- [[MATHWIKI-METHOD-CLUSTER-1418_面积关系建模]]
- [[MATHWIKI-METHOD-CLUSTER-316_切线截距建模]]
- [[MATHWIKI-METHOD-CLUSTER-818_可降阶微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-928_对积分关系求导]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-203
- GS-204

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
