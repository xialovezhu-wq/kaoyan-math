---
wiki_id: SRC-WQ-GS-490
type: source_summary
title: "GS-490 57899-1 凹凸性不等式"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-490_57899-1凹凸性不等式.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-490_57899-1-2026.5.22.md"
visual_ids:
  - "VIS-GS-490"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-490/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-490"
related_wrongnet_refs: []
knowledge:
  - "一元函数微分学应用"
  - "凹凸性与拐点"
  - "二阶导数判凹凸性"
  - "微分不等式证明"
  - "三角函数不等式"
error_causes:
  - "方法选择错误"
  - "题型识别失败"
  - "过程跳步"
  - "条件忽略"
methods:
  - "构造辅助函数"
  - "二阶导判凹凸性"
  - "端点连线法"
  - "条件转化"
  - "先判型"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-018_凹凸性与拐点"
  - "MATHWIKI-KNOWLEDGE-098_二阶导数判凹凸性"
  - "MATHWIKI-KNOWLEDGE-146_微分不等式证明"
  - "MATHWIKI-KNOWLEDGE-286_三角函数不等式"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-089_二阶导判凹凸性"
  - "MATHWIKI-METHOD-CLUSTER-253_端点连线法"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-068
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 98a5d9d9c0b161e7368622202a78964de0ccca77dea16ebff3a87f6c310f94f1
---

# GS-490 57899-1 凹凸性不等式

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-490_57899-1凹凸性不等式.md`
- wrongnet ID：`GS-490`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-490_57899-1-2026.5.22.md`（`VIS-GS-490`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 微分不等式证明 |
| 日期 | 2026-05-22 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 凹凸性与拐点
- 二阶导数判凹凸性
- 微分不等式证明
- 三角函数不等式

### 错因

- 方法选择错误
- 题型识别失败
- 过程跳步
- 条件忽略

### 方法

- 构造辅助函数
- 二阶导判凹凸性
- 端点连线法
- 条件转化
- 先判型

### 陷阱

- 一阶导难判
- 凹凸方向
- 端点值
- 适用条件
- 三角函数符号

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先令 \(f(x)=\sin\frac{x}{2}-\frac{x}{\pi}\)，算 \(f(0)=f(\pi)=0\)，再求 \(f''(x)=-\frac14\sin\frac{x}{2}<0\) |
| missed_action | 构造差函数后卡在一阶导判号，没有切换到二阶导定号和端点连线法 |
| related_method_card_id | H05-004 |
| next_reminder | 看到端点为 0、内部要证正且一阶导难判，先查二阶导定号，再用凹凸性比较端点连线。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-018_凹凸性与拐点]]
- [[MATHWIKI-KNOWLEDGE-098_二阶导数判凹凸性]]
- [[MATHWIKI-KNOWLEDGE-146_微分不等式证明]]
- [[MATHWIKI-KNOWLEDGE-286_三角函数不等式]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-089_二阶导判凹凸性]]
- [[MATHWIKI-METHOD-CLUSTER-253_端点连线法]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
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
