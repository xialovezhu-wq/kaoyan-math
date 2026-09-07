---
wiki_id: SRC-WQ-GS-207
type: source_summary
title: "GS-207 强化例题15.17：追踪曲线建立微分方程"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-207_强化例题15.17.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-207"
knowledge:
  - "微分方程"
  - "微分方程建模"
  - "一阶微分方程"
error_causes:
  - "题型入口风险：把运动方向指向条件转成切线斜率，再联立长度条件建方程。"
methods:
  - "几何关系建模"
  - "切线方向转斜率"
  - "分离变量"
  - "三角换元"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-451_题型入口风险-把运动方向指向条件转成切线斜率-再联立长度条件建方程"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-KNOWLEDGE-105_一阶微分方程"
  - "MATHWIKI-KNOWLEDGE-147_微分方程建模"
  - "MATHWIKI-METHOD-CLUSTER-028_三角换元"
  - "MATHWIKI-METHOD-CLUSTER-066_分离变量"
  - "MATHWIKI-METHOD-CLUSTER-638_几何关系建模"
  - "MATHWIKI-METHOD-CLUSTER-693_切线方向转斜率"
  - "MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-207 强化例题15.17：追踪曲线建立微分方程

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-207_强化例题15.17.md`
- wrongnet ID：`GS-207`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 高等数学-微分方程 |
| 题型 | 追踪曲线微分方程建模 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 微分方程
- 微分方程建模
- 一阶微分方程

### 错因

- 题型入口风险：把运动方向指向条件转成切线斜率，再联立长度条件建方程。

### 方法

- 几何关系建模
- 切线方向转斜率
- 分离变量
- 三角换元

### 陷阱

- $Q$ 的运动方向始终指向 $P$，表示轨迹切线方向，不是只写 $PQ$ 直线
- $|PQ|=1$ 要和斜率关系联立使用
- 积分时要结合初始点 $Q(1,0)$ 定常数和分支

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先把 $Q$ 的运动方向指向 $P$ 翻译成轨迹切线斜率。 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是只写 $PQ$ 连线关系，没有把方向条件转成切线斜率。 |
| related_method_card_id | H15-011 |
| next_reminder | 看到追踪曲线的方向条件，先把方向翻译成切线斜率，再联立长度约束。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-451_题型入口风险-把运动方向指向条件转成切线斜率-再联立长度条件建方程]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-KNOWLEDGE-105_一阶微分方程]]
- [[MATHWIKI-KNOWLEDGE-147_微分方程建模]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-066_分离变量]]
- [[MATHWIKI-METHOD-CLUSTER-638_几何关系建模]]
- [[MATHWIKI-METHOD-CLUSTER-693_切线方向转斜率]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-203
- GS-205
- GS-206

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
