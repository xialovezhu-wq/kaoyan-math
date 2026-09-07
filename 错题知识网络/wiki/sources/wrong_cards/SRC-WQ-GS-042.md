---
wiki_id: SRC-WQ-GS-042
type: source_summary
title: "GS-042 1000 B 1.14"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-042_1000B1.14.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-042"
knowledge:
  - "极限与连续"
  - "幂指极限"
error_causes:
  - "重要极限触发失败"
  - "幂指结构改写未触发"
methods:
  - "等价变形"
  - "取对数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-205_幂指结构改写未触发"
  - "MATHWIKI-ERROR-CLUSTER-443_重要极限触发失败"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-017_幂指极限"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-019_取对数"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-440"
formal_projection_sha256: e512ab6c65951fb82fef46b108ae5c77a8b3a755c7202afd5985d4c3147df0fd
---

# GS-042 1000 B 1.14

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-042_1000B1.14.md`
- wrongnet ID：`GS-042`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 幂指函数极限 |
| 日期 | 2026-05-07 |
| 状态 | 已掌握 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 幂指极限

### 错因

- 重要极限触发失败
- 幂指结构改写未触发

### 方法

- 等价变形
- 取对数

### 陷阱

- 定义域
- 适用条件

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把 \(\frac{x^x}{(1+x)^x}\) 改写为 \((1+\frac1x)^{-x}\)，再围绕重要极限 \(e\) 做一阶修正。 |
| missed_action | 没有先把 \(\frac{x^x}{(1+x)^x}\) 改写成重要极限结构，停在原式上无法触发 \(e\) 的一阶修正。 |
| related_method_card_id | H01-001 |
| next_reminder | 看到 \(\frac{x^x}{(1+x)^x}\) 或 \(\left(\frac{x}{x+1}\right)^x\)，先改写为 \((1+\frac1x)^{-x}\)，再对 \(e^{-1}\) 做一阶差值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-205_幂指结构改写未触发]]
- [[MATHWIKI-ERROR-CLUSTER-443_重要极限触发失败]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-017_幂指极限]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-019_取对数]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-440

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
