---
wiki_id: SRC-WQ-GS-027
type: source_summary
title: "GS-027 1000题B组1.35 2026.5.9"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-027_1000题B组1.35.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-027"
knowledge:
  - "极限与连续"
  - "变上限积分"
  - "含参定积分"
  - "反常积分"
  - "高斯积分"
  - "洛必达法则"
  - "定积分"
error_causes:
  - "公式记错"
  - "公式遗忘"
  - "方法选择错误"
  - "条件忽略"
  - "参数范围错误"
  - "结构整理断点"
  - "积分变量与参数混淆"
  - "洛必达前置化简不足"
methods:
  - "先判型"
  - "变量参数分离"
  - "外部参数提出"
  - "高斯积分公式"
  - "洛必达前置化简"
  - "等价变形"
  - "洛必达"
  - "主导项比较"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-015_公式记错"
  - "MATHWIKI-ERROR-CLUSTER-035_结构整理断点"
  - "MATHWIKI-ERROR-CLUSTER-036_参数范围错误"
  - "MATHWIKI-ERROR-CLUSTER-039_公式遗忘"
  - "MATHWIKI-ERROR-CLUSTER-047_积分变量与参数混淆"
  - "MATHWIKI-ERROR-CLUSTER-088_洛必达前置化简不足"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-028_反常积分"
  - "MATHWIKI-KNOWLEDGE-045_洛必达法则"
  - "MATHWIKI-KNOWLEDGE-119_含参定积分"
  - "MATHWIKI-KNOWLEDGE-278_高斯积分"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-021_主导项比较"
  - "MATHWIKI-METHOD-CLUSTER-034_洛必达"
  - "MATHWIKI-METHOD-CLUSTER-069_变量参数分离"
  - "MATHWIKI-METHOD-CLUSTER-1169_洛必达前置化简"
  - "MATHWIKI-METHOD-CLUSTER-1424_高斯积分公式"
  - "MATHWIKI-METHOD-CLUSTER-348_外部参数提出"
  - "MATHWIKI-GS-CONCEPT-001_条件边界"
  - "MATHWIKI-GS-ERROR-001_边界条件遗漏"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-METHOD-001_先做条件边界清单"
  - "MATHWIKI-GS-METHOD-006_先判型总流程"
  - "MATHWIKI-GS-METHOD-007_条件转化总流程"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度"
  - "MATHWIKI-GS-TOPIC-001_条件边界与分类讨论"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TRIGGER-001_参数端点定义域先停"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-027 1000题B组1.35 2026.5.9

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-027_1000题B组1.35.md`
- wrongnet ID：`GS-027`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 已知极限值反求参数 |
| 日期 | 2026-05-09 |
| 状态 | 已掌握 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 变上限积分
- 含参定积分
- 反常积分
- 高斯积分
- 洛必达法则
- 定积分

### 错因

- 公式记错
- 公式遗忘
- 方法选择错误
- 条件忽略
- 参数范围错误
- 结构整理断点
- 积分变量与参数混淆
- 洛必达前置化简不足

### 方法

- 先判型
- 变量参数分离
- 外部参数提出
- 高斯积分公式
- 洛必达前置化简
- 等价变形
- 洛必达
- 主导项比较
- 条件转化

### 陷阱

- 定义域
- 参数边界
- 适用条件
- 量纲/阶数
- 常数项
- 高斯积分常数
- 积分变量与参数混淆
- 指数因子拆分
- 0/0型前置整理

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把 $e^{x^2-t^2}$ 拆成 $e^{x^2}e^{-t^2}$，并将 $e^{x^2}$ 提出积分号外 |
| missed_action | 没有真正把 $e^{x^2}$ 下放到分母中，也误记 $\int_0^{+\infty}t^2e^{-t^2}\,dt=\frac{\sqrt{\pi}}4$，导致漏掉先令分子主项为 0 再洛必达 |
| related_method_card_id | H09-001 |
| next_reminder | 看到积分里同时有 $x$ 和 $t$，先问谁是积分变量、谁是外部参数；遇到 $e^{x^2-t^2}$，先拆成 $e^{x^2}e^{-t^2}$。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-015_公式记错]]
- [[MATHWIKI-ERROR-CLUSTER-035_结构整理断点]]
- [[MATHWIKI-ERROR-CLUSTER-036_参数范围错误]]
- [[MATHWIKI-ERROR-CLUSTER-039_公式遗忘]]
- [[MATHWIKI-ERROR-CLUSTER-047_积分变量与参数混淆]]
- [[MATHWIKI-ERROR-CLUSTER-088_洛必达前置化简不足]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-028_反常积分]]
- [[MATHWIKI-KNOWLEDGE-045_洛必达法则]]
- [[MATHWIKI-KNOWLEDGE-119_含参定积分]]
- [[MATHWIKI-KNOWLEDGE-278_高斯积分]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]
- [[MATHWIKI-METHOD-CLUSTER-034_洛必达]]
- [[MATHWIKI-METHOD-CLUSTER-069_变量参数分离]]
- [[MATHWIKI-METHOD-CLUSTER-1169_洛必达前置化简]]
- [[MATHWIKI-METHOD-CLUSTER-1424_高斯积分公式]]
- [[MATHWIKI-METHOD-CLUSTER-348_外部参数提出]]

### 深度编译页

- [[MATHWIKI-GS-CONCEPT-001_条件边界]]
- [[MATHWIKI-GS-ERROR-001_边界条件遗漏]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-METHOD-001_先做条件边界清单]]
- [[MATHWIKI-GS-METHOD-006_先判型总流程]]
- [[MATHWIKI-GS-METHOD-007_条件转化总流程]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度]]
- [[MATHWIKI-GS-TOPIC-001_条件边界与分类讨论]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TRIGGER-001_参数端点定义域先停]]
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
