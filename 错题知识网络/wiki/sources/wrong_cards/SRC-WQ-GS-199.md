---
wiki_id: SRC-WQ-GS-199
type: source_summary
title: "GS-199 强化例题15.12：根号整体换元与分支"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-199_强化例题15.12.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-199"
knowledge:
  - "根式整体换元"
error_causes:
  - "暂无明确个人错因：旧卡未记录作答过程"
methods:
  - "整体换元"
  - "分离变量"
  - "初值定常数"
  - "根号分支检查"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程"
  - "MATHWIKI-KNOWLEDGE-125_根式整体换元"
  - "MATHWIKI-METHOD-CLUSTER-037_初值定常数"
  - "MATHWIKI-METHOD-CLUSTER-066_分离变量"
  - "MATHWIKI-METHOD-CLUSTER-1135_根号分支检查"
  - "MATHWIKI-METHOD-CLUSTER-383_整体换元"
  - "MATHWIKI-GS-METHOD-057_微分方程降阶换元与分支保护"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-199 强化例题15.12：根号整体换元与分支

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-199_强化例题15.12.md`
- wrongnet ID：`GS-199`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 微分方程 |
| 题型 | 换元化可分离微分方程 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 根式整体换元

### 错因

- 暂无明确个人错因：旧卡未记录作答过程

### 方法

- 整体换元
- 分离变量
- 初值定常数
- 根号分支检查

### 陷阱

- 设 \(u=y+x^2\) 后要检查根号非负分支
- 初值决定常数和符号
- 不要漏掉题设 \(x\ge -2\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先令 \(u=y+x^2\)，并写出 \(u'=y'+2x\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是整体换元后没有用初值和 \(x\ge-2\) 固定根号分支 |
| related_method_card_id | H15-010 |
| next_reminder | 看到根号内是整体 \(y+x^2\)，先令 \(u=y+x^2\)，再用初值和定义域定分支。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程]]
- [[MATHWIKI-KNOWLEDGE-125_根式整体换元]]
- [[MATHWIKI-METHOD-CLUSTER-037_初值定常数]]
- [[MATHWIKI-METHOD-CLUSTER-066_分离变量]]
- [[MATHWIKI-METHOD-CLUSTER-1135_根号分支检查]]
- [[MATHWIKI-METHOD-CLUSTER-383_整体换元]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-057_微分方程降阶换元与分支保护]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-192
- GS-193
- GS-198

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
