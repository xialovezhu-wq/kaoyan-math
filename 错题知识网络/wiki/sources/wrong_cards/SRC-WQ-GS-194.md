---
wiki_id: SRC-WQ-GS-194
type: source_summary
title: "GS-194 强化例题15.7：乘积导数结构降阶"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-194_强化例题15.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-194"
knowledge:
  - "微分方程"
  - "二阶可降阶微分方程"
error_causes:
  - "暂无明确个人错因：旧卡未记录作答过程"
methods:
  - "乘积导数识别"
  - "令 P=yy'"
  - "一阶方程求解"
  - "常数合并"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-KNOWLEDGE-114_二阶可降阶微分方程"
  - "MATHWIKI-METHOD-CLUSTER-271_一阶方程求解"
  - "MATHWIKI-METHOD-CLUSTER-278_乘积导数识别"
  - "MATHWIKI-METHOD-CLUSTER-288_令P=yy'"
  - "MATHWIKI-METHOD-CLUSTER-364_常数合并"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-057_微分方程降阶换元与分支保护"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-194 强化例题15.7：乘积导数结构降阶

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-194_强化例题15.7.md`
- wrongnet ID：`GS-194`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 微分方程 |
| 题型 | 二阶可降阶微分方程（乘积导数结构） |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 微分方程
- 二阶可降阶微分方程

### 错因

- 暂无明确个人错因：旧卡未记录作答过程

### 方法

- 乘积导数识别
- 令 P=yy'
- 一阶方程求解
- 常数合并

### 陷阱

- 先识别 \(yy''+(y')^2=(yy')'\)
- 原式外层还有 \(x\)，不能直接把前三项看成一个完整导数
- 最后积分得到 \(y^2\) 型通解

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把 \(yy''+(y')^2\) 识别为 \((yy')'\) |
| missed_action | 缺少用户本人作答过程；待确认是否没有识别乘积导数结构 |
| related_method_card_id | H15-007 |
| next_reminder | 看到 \(yy''+(y')^2\)，先认出 \((yy')'\)，再令 \(P=yy'\) 降阶。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-KNOWLEDGE-114_二阶可降阶微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-271_一阶方程求解]]
- [[MATHWIKI-METHOD-CLUSTER-278_乘积导数识别]]
- [[MATHWIKI-METHOD-CLUSTER-288_令P=yy']]
- [[MATHWIKI-METHOD-CLUSTER-364_常数合并]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-057_微分方程降阶换元与分支保护]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-193
- GS-211
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
