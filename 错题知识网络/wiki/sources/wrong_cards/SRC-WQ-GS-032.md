---
wiki_id: SRC-WQ-GS-032
type: source_summary
title: "GS-032 58083 2026.5.5"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-032_580832026.5.5.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-032"
knowledge:
  - "幂指极限"
  - "间断点分类"
error_causes:
  - "触发信息遗漏"
  - "定义域错误"
  - "方法论调取失败"
  - "过程跳步"
methods:
  - "候选点定位"
  - "指数化处理"
  - "分类讨论"
  - "左右极限"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-030_定义域错误"
  - "MATHWIKI-KNOWLEDGE-017_幂指极限"
  - "MATHWIKI-KNOWLEDGE-064_间断点分类"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-224_左右极限"
  - "MATHWIKI-METHOD-CLUSTER-292_候选点定位"
  - "MATHWIKI-METHOD-CLUSTER-375_指数化处理"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-METHOD-011_B5-CHECK检查断点"
  - "MATHWIKI-GS-METHOD-049_连续间断点候选点检查链"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-032 58083 2026.5.5

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-032_580832026.5.5.md`
- wrongnet ID：`GS-032`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 幂指式间断点分类 |
| 日期 | 2026-05-05 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 幂指极限
- 间断点分类

### 错因

- 触发信息遗漏
- 定义域错误
- 方法论调取失败
- 过程跳步

### 方法

- 候选点定位
- 指数化处理
- 分类讨论
- 左右极限
- 条件转化

### 陷阱

- 无定义点
- 分母零点
- 指数奇点
- 定义域
- 左右极限
- 可去间断

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先分别解 \(\tan(x-\frac{\pi}{4})=0\) 与 \(\tan(x-\frac{\pi}{4})\) 无定义，把四个候选点一次列全。 |
| missed_action | 只找了 \(\tan(x-\frac{\pi}{4})=0\) 的点，漏掉 \(\tan\) 无定义点；也没有先写成 \(e^{\frac{x\ln(1+x)}{\tan(x-\pi/4)}}\) 再分类。 |
| related_method_card_id | H01-008 |
| next_reminder | 看到幂指式问间断点，先列底数边界、指数分母零点和三角函数无定义点，再指数化逐点判左右极限。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-030_定义域错误]]
- [[MATHWIKI-KNOWLEDGE-017_幂指极限]]
- [[MATHWIKI-KNOWLEDGE-064_间断点分类]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-224_左右极限]]
- [[MATHWIKI-METHOD-CLUSTER-292_候选点定位]]
- [[MATHWIKI-METHOD-CLUSTER-375_指数化处理]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-011_B5-CHECK检查断点]]
- [[MATHWIKI-GS-METHOD-049_连续间断点候选点检查链]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-031
- GS-038

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
