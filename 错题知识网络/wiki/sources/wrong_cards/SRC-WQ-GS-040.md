---
wiki_id: SRC-WQ-GS-040
type: source_summary
title: "GS-040 58061 2026.5.5"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-040_580612026.5.5.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-040"
knowledge:
  - "数列极限"
  - "极限与连续"
error_causes:
  - "概念混淆"
  - "方法选择错误"
  - "题型识别失败"
methods:
  - "反例法"
  - "特值法"
  - "特殊值检验"
  - "分类讨论"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-075_特殊值检验"
  - "MATHWIKI-METHOD-CLUSTER-112_反例法"
  - "MATHWIKI-METHOD-CLUSTER-243_特值法"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: d148650b78f630921e3d1aea75f32732fafe1eb77e72a4d3f8ac308fdd0652b8
---

# GS-040 58061 2026.5.5

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-040_580612026.5.5.md`
- wrongnet ID：`GS-040`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 数列极限 |
| 题型 | 数列极限 |
| 日期 | 2026-05-07 |
| 状态 | 已掌握 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 数列极限
- 极限与连续

### 错因

- 概念混淆
- 方法选择错误
- 题型识别失败

### 方法

- 反例法
- 特值法
- 特殊值检验
- 分类讨论
- 条件转化

### 陷阱

- 必有命题
- 反例构造方向
- 单侧逼近
- 1/n扰动
- 正负号
- 适用条件

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把 D 选项移项，确定要构造 \(a_n\) 在 \(a-\frac1n\) 或 \(a+\frac1n\) 哪一侧，再用从上方或下方趋近 \(a\) 的反例否定命题 |
| missed_action | 没有先把待否定选项移项成可构造的侧向逼近关系，反例方向混乱 |
| related_method_card_id | H00-009 |
| next_reminder | 看到数列极限命题判断，先把选项翻译成定义或不等式目标；要否定命题时优先构造上方/下方趋近的反例。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-075_特殊值检验]]
- [[MATHWIKI-METHOD-CLUSTER-112_反例法]]
- [[MATHWIKI-METHOD-CLUSTER-243_特值法]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
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
