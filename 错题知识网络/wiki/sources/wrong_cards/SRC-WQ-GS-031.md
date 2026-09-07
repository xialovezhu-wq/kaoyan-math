---
wiki_id: SRC-WQ-GS-031
type: source_summary
title: "GS-031 1000题A组6.16 2026.5.5"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-031_1000题A组6.162026.5.5.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-031"
knowledge:
  - "极限与连续"
  - "间断点分类"
  - "函数极限"
  - "零点定理"
  - "导数判单调"
error_causes:
  - "条件忽略"
  - "定义域错误"
methods:
  - "构造辅助函数"
  - "求导判单调"
  - "介值定理"
  - "条件转化"
  - "分类讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-030_定义域错误"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-039_函数极限"
  - "MATHWIKI-KNOWLEDGE-042_零点定理"
  - "MATHWIKI-KNOWLEDGE-064_间断点分类"
  - "MATHWIKI-KNOWLEDGE-091_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-140_介值定理"
  - "MATHWIKI-METHOD-CLUSTER-419_求导判单调"
  - "MATHWIKI-GS-METHOD-007_条件转化总流程"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-049_连续间断点候选点检查链"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-031 1000题A组6.16 2026.5.5

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-031_1000题A组6.162026.5.5.md`
- wrongnet ID：`GS-031`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 分式函数间断点个数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 间断点分类
- 函数极限
- 零点定理
- 导数判单调

### 错因

- 条件忽略
- 定义域错误

### 方法

- 构造辅助函数
- 求导判单调
- 介值定理
- 条件转化
- 分类讨论

### 陷阱

- 定义域
- 左右极限
- 分母零点
- 参数边界
- 适用条件
- 极限过程

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先令 \(g(x)=\ln x-\frac{x}{e}+k\)，再计算 \(g'(x)\) 判断单调区间。 |
| missed_action | 找到分母为零点后，没有继续用单调性和介值定理判断零点个数。 |
| related_method_card_id | H01-008 |
| next_reminder | 看到分式函数问间断点个数，先把分母设成辅助函数，再用导数单调性和介值定理数分母零点。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-030_定义域错误]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-039_函数极限]]
- [[MATHWIKI-KNOWLEDGE-042_零点定理]]
- [[MATHWIKI-KNOWLEDGE-064_间断点分类]]
- [[MATHWIKI-KNOWLEDGE-091_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-140_介值定理]]
- [[MATHWIKI-METHOD-CLUSTER-419_求导判单调]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-007_条件转化总流程]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-049_连续间断点候选点检查链]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-032
- GS-072

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
