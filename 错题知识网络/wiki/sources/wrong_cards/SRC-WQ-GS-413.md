---
wiki_id: SRC-WQ-GS-413
type: source_summary
title: "GS-413 强化例题14.8"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-413_强化例题14.8.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-413"
knowledge:
  - "二重积分"
  - "二重积分极坐标法"
  - "行列式"
error_causes:
  - "方法调取失败"
  - "变量混淆"
methods:
  - "换元"
  - "二重积分极坐标法"
  - "雅可比行列式"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-ERROR-CLUSTER-024_变量混淆"
  - "MATHWIKI-KNOWLEDGE-023_行列式"
  - "MATHWIKI-KNOWLEDGE-049_二重积分"
  - "MATHWIKI-KNOWLEDGE-070_二重积分极坐标法"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-009_换元"
  - "MATHWIKI-METHOD-CLUSTER-047_二重积分极坐标法"
  - "MATHWIKI-METHOD-CLUSTER-472_雅可比行列式"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-036_二重积分换元与雅可比链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-413 强化例题14.8

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-413_强化例题14.8.md`
- wrongnet ID：`GS-413`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 二重积分 |
| 题型 | 二重积分计算 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二重积分
- 二重积分极坐标法
- 行列式

### 错因

- 方法调取失败
- 变量混淆

### 方法

- 换元
- 二重积分极坐标法
- 雅可比行列式
- 条件转化

### 陷阱

- 平移后不改变雅可比
- 极坐标换元必须补微元因子 \(\rho\)
- \(v\ge u\) 对应角域 \([\frac{\pi}{4},\frac{5\pi}{4}]\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先令 u=x-1, v=y-1，把圆域和 v>=u 同时改写 |
| missed_action | 没有先完成平移变量、区域条件和微元的同步转换 |
| related_method_card_id | H14-005 |
| next_reminder | 二重积分换元要同时改函数、区域和微元；圆心不在原点时先平移再极坐标。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-024_变量混淆]]
- [[MATHWIKI-KNOWLEDGE-023_行列式]]
- [[MATHWIKI-KNOWLEDGE-049_二重积分]]
- [[MATHWIKI-KNOWLEDGE-070_二重积分极坐标法]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-009_换元]]
- [[MATHWIKI-METHOD-CLUSTER-047_二重积分极坐标法]]
- [[MATHWIKI-METHOD-CLUSTER-472_雅可比行列式]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-036_二重积分换元与雅可比链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-407
- GS-404
- GS-400

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
