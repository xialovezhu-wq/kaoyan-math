---
wiki_id: SRC-WQ-GS-192
type: source_summary
title: "GS-192 强化例题15 .5(1)"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-192_强化例题15.5(1).md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-192"
knowledge:
  - "微分方程"
  - "二阶可降阶微分方程"
error_causes:
  - "暂无明确个人错因：旧卡未记录作答过程"
methods:
  - "降阶换元"
  - "分离变量"
  - "初值定常数"
  - "零解检查"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-KNOWLEDGE-114_二阶可降阶微分方程"
  - "MATHWIKI-METHOD-CLUSTER-037_初值定常数"
  - "MATHWIKI-METHOD-CLUSTER-066_分离变量"
  - "MATHWIKI-METHOD-CLUSTER-1405_降阶换元"
  - "MATHWIKI-METHOD-CLUSTER-1414_零解检查"
  - "MATHWIKI-GS-METHOD-057_微分方程降阶换元与分支保护"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-192 强化例题15 .5(1)

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-192_强化例题15.5(1).md`
- wrongnet ID：`GS-192`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 微分方程 |
| 题型 | 二阶可降阶微分方程定解问题 |
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

- 降阶换元
- 分离变量
- 初值定常数
- 零解检查

### 陷阱

- 分离变量时不能除掉 \(u=0\) 解
- 初值 \(y'(0)=0\) 要保留零解
- 不能取导致 \(x=0\) 发散的常数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先令 \(u=y'\)，并检查 \(u\equiv0\) 是否满足初值 |
| missed_action | 缺少用户本人作答过程；待确认是否分离变量时除以 \(u^2\) 丢掉零解 |
| related_method_card_id | H15-007 |
| next_reminder | 看到降阶后要除以 \(u\) 或 \(u^2\)，先检查零解是否满足初值，再分离变量。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-KNOWLEDGE-114_二阶可降阶微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-037_初值定常数]]
- [[MATHWIKI-METHOD-CLUSTER-066_分离变量]]
- [[MATHWIKI-METHOD-CLUSTER-1405_降阶换元]]
- [[MATHWIKI-METHOD-CLUSTER-1414_零解检查]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-057_微分方程降阶换元与分支保护]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-193
- GS-194
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
