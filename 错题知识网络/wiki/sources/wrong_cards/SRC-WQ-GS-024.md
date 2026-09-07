---
wiki_id: SRC-WQ-GS-024
type: source_summary
title: "GS-024 例题5.6 2026.4.1"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-024_例题5.62026.4.1.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-024"
related_wrongnet_refs:
  - "GS-025"
knowledge:
  - "一元函数微分学应用"
  - "斜渐近线"
  - "无穷远主量"
  - "截距极限"
  - "二项展开"
error_causes:
  - "旧结构化字段记录主量提出动作断裂；来源未分类"
methods:
  - "斜渐近线公式"
  - "主导项比较"
  - "二项展开"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-KNOWLEDGE-021_拉格朗日中值定理"
  - "MATHWIKI-KNOWLEDGE-085_渐近线"
  - "MATHWIKI-KNOWLEDGE-093_无穷远极限"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-008_泰勒展开"
  - "MATHWIKI-METHOD-CLUSTER-021_主导项比较"
  - "MATHWIKI-METHOD-CLUSTER-059_斜渐近线公式"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-METHOD-048_渐近线题全类型检查链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 0cb53fb146a15792a22f3bd2e04b20e66f32bc5f230dc03a36030cf3f82250ad
---

# GS-024 例题5.6 2026.4.1

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-024_例题5.62026.4.1.md`
- wrongnet ID：`GS-024`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 曲线性质 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 斜渐近线
- 无穷远主量
- 截距极限
- 二项展开

### 错因

- 旧结构化字段记录主量提出动作断裂；来源未分类

### 方法

- 斜渐近线公式
- 主导项比较
- 二项展开

### 陷阱

- 主量未提出

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写 $k=\lim y/x=1$，再把 $y-x$ 化成 $x\left[\left(1+\frac{1}{x}\right)^{3/2}-1\right]$ 后求 $b$。 |
| missed_action | 求截距时没有先提出并约去主量 $x^{3/2}$，导致没有化到 $x[(1+1/x)^{3/2}-1]$ 这个经典极限形。 |
| related_method_card_id | H05-005 |
| next_reminder | 看到幂式根式曲线求斜渐近线，先求 $k$，再把 $y-kx$ 中的最高阶主量提出并约掉。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-KNOWLEDGE-021_拉格朗日中值定理]]
- [[MATHWIKI-KNOWLEDGE-085_渐近线]]
- [[MATHWIKI-KNOWLEDGE-093_无穷远极限]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]
- [[MATHWIKI-METHOD-CLUSTER-059_斜渐近线公式]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-METHOD-048_渐近线题全类型检查链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-025

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
