---
wiki_id: SRC-WQ-GS-193
type: source_summary
title: "GS-193 强化例题15.6（2）：二阶不显含自变量微分方程"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-193_强化例题15.6（2）.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-193"
knowledge:
  - "二阶可降阶微分方程"
error_causes:
  - "暂无明确个人错因：旧卡未记录作答过程"
methods:
  - "令 p=y' 降阶"
  - "y''=p dp/dy"
  - "分离变量"
  - "初值定常数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程"
  - "MATHWIKI-KNOWLEDGE-114_二阶可降阶微分方程"
  - "MATHWIKI-METHOD-CLUSTER-037_初值定常数"
  - "MATHWIKI-METHOD-CLUSTER-066_分离变量"
  - "MATHWIKI-METHOD-CLUSTER-501_y''=pdp-dy"
  - "MATHWIKI-METHOD-CLUSTER-589_令p=y'降阶"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-057_微分方程降阶换元与分支保护"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-193 强化例题15.6（2）：二阶不显含自变量微分方程

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-193_强化例题15.6（2）.md`
- wrongnet ID：`GS-193`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 微分方程 |
| 题型 | 二阶可降阶微分方程（不显含自变量） |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二阶可降阶微分方程

### 错因

- 暂无明确个人错因：旧卡未记录作答过程

### 方法

- 令 p=y' 降阶
- y''=p dp/dy
- 分离变量
- 初值定常数

### 陷阱

- 不显含 x 时应把 y' 看成 y 的函数
- 代换后 \(y''=p\frac{dp}{dy}\)，不是单独的 \(\frac{dp}{dx}\)
- 初值 \(y(3)=2\) 与 \(y'(3)=1\) 同时用于确定常数和分支

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先令 \(p=y'=p(y)\)，写 \(y''=p\,dp/dy\) |
| missed_action | 缺少用户本人作答过程；待确认是否仍按 \(p=p(x)\) 处理，漏掉不显含 \(x\) 的降阶入口 |
| related_method_card_id | H15-007 |
| next_reminder | 看到二阶方程不显含 \(x\)，先令 \(p=y'=p(y)\)，再写 \(y''=p\,dp/dy\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程]]
- [[MATHWIKI-KNOWLEDGE-114_二阶可降阶微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-037_初值定常数]]
- [[MATHWIKI-METHOD-CLUSTER-066_分离变量]]
- [[MATHWIKI-METHOD-CLUSTER-501_y''=pdp-dy]]
- [[MATHWIKI-METHOD-CLUSTER-589_令p=y'降阶]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-057_微分方程降阶换元与分支保护]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-192
- GS-204
- GS-211

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
