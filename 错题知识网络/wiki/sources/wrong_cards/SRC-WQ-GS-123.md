---
wiki_id: SRC-WQ-GS-123
type: source_summary
title: "GS-123 2021年第12题 参数方程二阶导链式求导"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-123_2021年第12题（数学2）.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-123"
knowledge:
  - "参数方程求导"
  - "高阶导数"
error_causes:
  - "暂无明确个人错因：旧卡未记录作答过程"
methods:
  - "参数方程求导"
  - "参数方程二阶导"
  - "链式求导"
  - "先化简再求导"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程"
  - "MATHWIKI-KNOWLEDGE-027_高阶导数"
  - "MATHWIKI-KNOWLEDGE-054_参数方程求导"
  - "MATHWIKI-METHOD-CLUSTER-018_链式求导"
  - "MATHWIKI-METHOD-CLUSTER-038_参数方程求导"
  - "MATHWIKI-METHOD-CLUSTER-147_参数方程二阶导"
  - "MATHWIKI-METHOD-CLUSTER-619_先化简再求导"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-055_参数方程二阶导链式求导"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-25
related_wrongnet_refs: []
formal_projection_sha256: e1bccb1cb177d72a901e209b72870c88cceb0a6e8be24037ebcf1e402a72dcb0
---

# GS-123 2021年第12题 参数方程二阶导链式求导

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-123_2021年第12题（数学2）.md`
- wrongnet ID：`GS-123`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 参数方程二阶导 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 参数方程求导
- 高阶导数

### 错因

- 暂无明确个人错因：旧卡未记录作答过程

### 方法

- 参数方程求导
- 参数方程二阶导
- 链式求导
- 先化简再求导

### 陷阱

- 链式求导
- 二阶导变量误判
- 对 t 求导不能直接当二阶导
- 先约分化简一阶导

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先求 dy/dx=(dy/dt)/(dx/dt) 并尽量化简 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是把对 t 求导直接当成二阶导，漏掉再除以 x'(t) |
| related_method_card_id | H04-007 |
| next_reminder | 看到参数方程求二阶导，先求 dy/dx 并化简，再对 t 求导并除以 x'(t)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程]]
- [[MATHWIKI-KNOWLEDGE-027_高阶导数]]
- [[MATHWIKI-KNOWLEDGE-054_参数方程求导]]
- [[MATHWIKI-METHOD-CLUSTER-018_链式求导]]
- [[MATHWIKI-METHOD-CLUSTER-038_参数方程求导]]
- [[MATHWIKI-METHOD-CLUSTER-147_参数方程二阶导]]
- [[MATHWIKI-METHOD-CLUSTER-619_先化简再求导]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-055_参数方程二阶导链式求导]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
