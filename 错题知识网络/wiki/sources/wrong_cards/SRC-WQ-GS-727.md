---
wiki_id: SRC-WQ-GS-727
type: source_summary
title: "GS-727 165360 锥面正向单位法向量"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-727_165360锥面正向单位法向量.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-727_165360锥面正向单位法向量.md"
visual_ids:
  - "VIS-GS-727"
wrongnet_refs:
  - "GS-727"
knowledge:
  - "向量代数与空间解析几何"
  - "隐式曲面"
  - "梯度与法向量"
  - "定向曲面"
  - "向量单位化"
error_causes:
  - "概念边界混淆"
  - "偏导链式法则不稳"
  - "定向条件不清"
  - "等价分式识别不稳"
methods:
  - "隐式化"
  - "梯度求法向量"
  - "第三分量判定方向"
  - "向量单位化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS"
  - "MATHWIKI-ACTION-GAP-005"
  - "MATHWIKI-ERROR-CLUSTER-027"
  - "MATHWIKI-ERROR-CLUSTER-540"
  - "MATHWIKI-ERROR-CLUSTER-541"
  - "MATHWIKI-ERROR-CLUSTER-542"
  - "MATHWIKI-KNOWLEDGE-089"
  - "MATHWIKI-KNOWLEDGE-452"
  - "MATHWIKI-KNOWLEDGE-453"
  - "MATHWIKI-KNOWLEDGE-454"
  - "MATHWIKI-KNOWLEDGE-455"
  - "MATHWIKI-METHOD-CLUSTER-1496"
  - "MATHWIKI-METHOD-CLUSTER-1497"
  - "MATHWIKI-METHOD-CLUSTER-1498"
  - "MATHWIKI-METHOD-CLUSTER-1499"
status: indexed
formal_projection_sha256: 3fc240e98aeef990060bf1d259a5c967dbb923a8a02ca0161e5aaa4dcbc0a288
last_updated: "2026-08-28"
related_wrongnet_refs: []
---

# GS-727 165360 锥面正向单位法向量

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-727_165360锥面正向单位法向量.md`
- wrongnet ID：`GS-727`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-727_165360锥面正向单位法向量|VIS-GS-727]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-727_165360%E9%94%A5%E9%9D%A2%E6%AD%A3%E5%90%91%E5%8D%95%E4%BD%8D%E6%B3%95%E5%90%91%E9%87%8F)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-727/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-727/solution_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 向量代数与空间解析几何 |
| 题型 | 隐式曲面的定向单位法向量 |
| 日期 | 2026-07-28 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 本次正式结论

- 当前错点：没有区分“曲面上的点坐标”与“法向量的分量”，也没有形成“写成 $F=0$—求梯度—按第三分量选方向—除以模长单位化”的固定链条；其中 $x/\sqrt{x^2+y^2}$ 与 $y/\sqrt{x^2+y^2}$ 来自复合函数平方根的偏导，而不是任意取出的分量。
- 最新错误证据：2026-07-28 第1次错：能够识别曲面是上半圆锥，但不清楚“下侧为正”是在两个法向量方向中选择第三分量小于零者，也把点坐标 $z$ 与法向量第三分量混为一谈；求梯度时又把 $\partial\sqrt{x^2+y^2}/\partial x$ 误解成对半径求导，不知道 $x/\sqrt{x^2+y^2}$、$y/\sqrt{x^2+y^2}$ 的来源，并把 $F_z=1$ 误说成 $z=1$。最后单位化时没有认出 $1/\sqrt2=\sqrt2/2$。
- 最新掌握证据：2026-07-28 AI评分 0/5：题型对象、偏导链式法则、定向条件和单位化等号均需逐项解释；讲解后用户确认理解，但尚无独立复做证据。
- 2026-08-27 用户报告本次独立做对并形成正式 4/5 评分；完整的 (F=0)、梯度、判向与单位化过程未进入会话包，因此只记录一次正确复做，不据此删除旧错因或把整卡升级为已掌握。

## 可编译信息

### 知识点

- 向量代数与空间解析几何
- 隐式曲面
- 梯度与法向量
- 定向曲面
- 向量单位化

### 错因

- 概念边界混淆
- 偏导链式法则不稳
- 定向条件不清
- 等价分式识别不稳

### 方法

- 隐式化
- 梯度求法向量
- 第三分量判定方向
- 向量单位化

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-CONCEPT |
| expected_first_action | 令 $F(x,y,z)=z-\sqrt{x^2+y^2}$，逐项计算 $F_x,F_y,F_z$，暂不急着选正负号。 |
| missed_action | 不清楚梯度各分量的偏导来源，并把方向条件作用在点坐标 $z$ 上；单位化后又未识别等价分式。 |
| related_method_card_id | H17-005 |
| next_reminder | 法向量的上下看第三分量，不看曲面点的 $z$；梯度给方向，除以模长才得到单位法向量。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-005_A-CONCEPT]]
- [[MATHWIKI-ERROR-CLUSTER-027_概念边界混淆]]
- [[MATHWIKI-ERROR-CLUSTER-540_偏导链式法则不稳]]
- [[MATHWIKI-ERROR-CLUSTER-541_定向条件不清]]
- [[MATHWIKI-ERROR-CLUSTER-542_等价分式识别不稳]]
- [[MATHWIKI-KNOWLEDGE-089_向量代数与空间解析几何]]
- [[MATHWIKI-KNOWLEDGE-452_隐式曲面]]
- [[MATHWIKI-KNOWLEDGE-453_梯度与法向量]]
- [[MATHWIKI-KNOWLEDGE-454_定向曲面]]
- [[MATHWIKI-KNOWLEDGE-455_向量单位化]]
- [[MATHWIKI-METHOD-CLUSTER-1496_隐式化]]
- [[MATHWIKI-METHOD-CLUSTER-1497_梯度求法向量]]
- [[MATHWIKI-METHOD-CLUSTER-1498_第三分量判定方向]]
- [[MATHWIKI-METHOD-CLUSTER-1499_向量单位化]]

### 深度方法与专题

- 本批保持索引型编译；未新增深度专题关系。
