---
wiki_id: SRC-WQ-GS-005
type: source_summary
title: "GS-005 1000题B组1.30 2026.4.17 ✅"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-005_1000题B组1.302026.4.17✅.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-005"
knowledge:
  - "极限与连续"
  - "等价无穷小"
  - "无穷小阶数比较"
  - "泰勒展开"
error_causes:
  - "条件忽略"
  - "计算失误"
methods:
  - "等价变形"
  - "泰勒展开"
  - "先判型"
  - "主导项比较"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-014_计算失误"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-038_泰勒展开"
  - "MATHWIKI-KNOWLEDGE-051_无穷小阶数比较"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-008_泰勒展开"
  - "MATHWIKI-METHOD-CLUSTER-021_主导项比较"
  - "MATHWIKI-GS-METHOD-006_先判型总流程"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: 0a6e97d23240132e3e50326ca2a3bf8047f24abacc6a44b81924902ed1071470
---

# GS-005 1000题B组1.30 2026.4.17 ✅

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-005_1000题B组1.302026.4.17✅.md`
- wrongnet ID：`GS-005`
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
- 无穷小阶数比较
- 泰勒展开

### 错因

- 条件忽略
- 计算失误

### 方法

- 等价变形
- 泰勒展开
- 先判型
- 主导项比较

### 陷阱

- 适用条件

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先判未定式类型，把趋于非零常数的因子单独取极限，再对剩余趋零差值用等价无穷小或泰勒保留目标阶。 |
| missed_action | 没有先执行“判型 -> 非零因子先算 -> 剩余趋零部分等价化简”的第一动作，直接展开导致阶次压力变大。 |
| related_method_card_id | H01-004 |
| next_reminder | 看到无穷小阶数比较，先判型并把非零因子单独算掉，再只处理真正趋零的主量。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-038_泰勒展开]]
- [[MATHWIKI-KNOWLEDGE-051_无穷小阶数比较]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-006_先判型总流程]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
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
