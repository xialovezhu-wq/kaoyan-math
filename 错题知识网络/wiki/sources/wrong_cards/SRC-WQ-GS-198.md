---
wiki_id: SRC-WQ-GS-198
type: source_summary
title: "GS-198 强化例题15.11：指数换元化一阶线性"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-198_强化例题15.11.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-198"
knowledge:
  - "一阶线性微分方程"
  - "指数函数求导"
error_causes:
  - "暂无明确个人错因：旧卡未记录作答过程"
methods:
  - "指数换元"
  - "一阶线性微分方程"
  - "分部积分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程"
  - "MATHWIKI-KNOWLEDGE-065_一阶线性微分方程"
  - "MATHWIKI-KNOWLEDGE-256_指数函数求导"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-088_一阶线性微分方程"
  - "MATHWIKI-METHOD-CLUSTER-160_指数换元"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-057_微分方程降阶换元与分支保护"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-198 强化例题15.11：指数换元化一阶线性

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-198_强化例题15.11.md`
- wrongnet ID：`GS-198`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 微分方程 |
| 题型 | 换元化一阶线性微分方程 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一阶线性微分方程
- 指数函数求导

### 错因

- 暂无明确个人错因：旧卡未记录作答过程

### 方法

- 指数换元
- 一阶线性微分方程
- 分部积分

### 陷阱

- 看到 \(e^{-y}\) 先乘 \(e^y\)
- 用 \(z=e^y\) 凑出 \((e^y)'\)
- 一阶线性方程积分因子为 \(e^x\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先两边乘 \(e^y\)，令 \(z=e^y\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有先乘 \(e^y\) 凑出 \((e^y)'\) |
| related_method_card_id | H15-010 |
| next_reminder | 看到 \(e^{-y}\) 与 \(y'\) 共现，先乘 \(e^y\)，再令 \(z=e^y\) 化一阶线性。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程]]
- [[MATHWIKI-KNOWLEDGE-065_一阶线性微分方程]]
- [[MATHWIKI-KNOWLEDGE-256_指数函数求导]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-088_一阶线性微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-160_指数换元]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-057_微分方程降阶换元与分支保护]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-199
- GS-201

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
