---
wiki_id: SRC-WQ-GS-020
type: source_summary
title: "GS-020 58072 2026.5.7"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-020_580722026.5.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-020"
related_wrongnet_refs: []
knowledge:
  - "极限与连续"
  - "等价无穷小"
  - "主导项"
  - "无穷大量比较"
error_causes:
  - "结构整理断点"
  - "主导项判断遗漏"
methods:
  - "主导项比较"
  - "等价变形"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-035_结构整理断点"
  - "MATHWIKI-ERROR-CLUSTER-110_主导项判断遗漏"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-086_主导项"
  - "MATHWIKI-KNOWLEDGE-150_无穷大量比较"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-021_主导项比较"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: f67f42f264177a3841e448b6bca9f769c1cd11eacde0ed348a6c569e017bbbd0
---

# GS-020 58072 2026.5.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-020_580722026.5.7.md`
- wrongnet ID：`GS-020`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 无穷小阶数比较 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 等价无穷小
- 主导项
- 无穷大量比较

### 错因

- 结构整理断点
- 主导项判断遗漏

### 方法

- 主导项比较
- 等价变形

### 陷阱

- 定义域
- 参数边界
- 适用条件
- 量纲/阶数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先从 \(\sqrt[3]{1-x^6}\) 中提出最高次项 \(x^2\)，确定主导项为 \(-x^2\)，再逐级消去主项。 |
| missed_action | 没有先按 \(x\to\infty\) 的最高次项提取三次根主量，而是把根式题误归到“有理化”入口。 |
| related_method_card_id | H01-006 |
| next_reminder | 看到无穷远处根式主项相消，先提出最高次幂并确定主导项，再用待定系数消主项。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-035_结构整理断点]]
- [[MATHWIKI-ERROR-CLUSTER-110_主导项判断遗漏]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-086_主导项]]
- [[MATHWIKI-KNOWLEDGE-150_无穷大量比较]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 证据边界

- GS-020 的个人断点证据仍为 `legacy_unclassified`；与 GS-460 的普通强边因无法确认双方共享同一个人第一断点而降级。

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
