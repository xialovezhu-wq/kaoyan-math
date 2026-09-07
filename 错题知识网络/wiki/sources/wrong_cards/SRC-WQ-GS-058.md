---
wiki_id: SRC-WQ-GS-058
type: source_summary
title: "GS-058 强化例题2.1"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-058_强化例题2.1.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-058"
knowledge:
  - "数列极限"
  - "递推数列"
  - "固定点方程"
  - "中值定理"
error_causes:
  - "方法论调取不稳"
  - "动作链断裂"
methods:
  - "拉格朗日中值定理"
  - "固定点方程"
  - "压缩映射"
  - "构造上界"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-KNOWLEDGE-053_递推数列"
  - "MATHWIKI-KNOWLEDGE-121_固定点方程"
  - "MATHWIKI-METHOD-CLUSTER-014_拉格朗日中值定理"
  - "MATHWIKI-METHOD-CLUSTER-114_固定点方程"
  - "MATHWIKI-METHOD-CLUSTER-122_构造上界"
  - "MATHWIKI-METHOD-CLUSTER-740_压缩映射"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-019_压缩映射不动点迭代"
  - "MATHWIKI-GS-TOPIC-007_数列极限错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-058 强化例题2.1

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-058_强化例题2.1.md`
- wrongnet ID：`GS-058`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 数列极限 |
| 题型 | 压缩映射型递推数列极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 数列极限
- 递推数列
- 固定点方程
- 中值定理

### 错因

- 方法论调取不稳
- 动作链断裂

### 方法

- 拉格朗日中值定理
- 固定点方程
- 压缩映射
- 构造上界

### 陷阱

- 不变区间
- 压缩常数
- 不动点筛选

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先解不动点 $a=f(a)$，并选出迭代保持不出的闭区间。 |
| missed_action | 没有先找不动点，也没有把中值定理写成误差递推链。 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到递推迭代和导数界，先找不动点与不变区间，再用中值定理写误差压缩。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-KNOWLEDGE-053_递推数列]]
- [[MATHWIKI-KNOWLEDGE-121_固定点方程]]
- [[MATHWIKI-METHOD-CLUSTER-014_拉格朗日中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-114_固定点方程]]
- [[MATHWIKI-METHOD-CLUSTER-122_构造上界]]
- [[MATHWIKI-METHOD-CLUSTER-740_压缩映射]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-019_压缩映射不动点迭代]]
- [[MATHWIKI-GS-TOPIC-007_数列极限错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-054
- GS-070
- GS-068

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
