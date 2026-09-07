---
wiki_id: SRC-WQ-GS-495
type: source_summary
title: "GS-495 102317 拆项根值判别"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-495_102317拆项根值判别.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-495_102317-2026.5.23.md"
visual_ids:
  - "VIS-GS-495"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-495/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-495"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "数项级数敛散性判别"
  - "正项级数敛散性判别"
  - "正项级数比较判别法"
  - "根值判别法"
  - "p级数"
  - "等价无穷小"
error_causes:
  - "题型识别失败"
  - "方法选择错误"
  - "条件忽略"
  - "过程跳步"
methods:
  - "先判型"
  - "拆项判断"
  - "比较判别法"
  - "根值判别法"
  - "等价变形"
  - "小量趋零"
  - "p级数比较"
  - "对数化幂"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-032_正项级数比较判别法"
  - "MATHWIKI-KNOWLEDGE-036_p级数"
  - "MATHWIKI-KNOWLEDGE-393_根值判别法"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-012_比较判别法"
  - "MATHWIKI-METHOD-CLUSTER-1013_拆项判断"
  - "MATHWIKI-METHOD-CLUSTER-362_小量趋零"
  - "MATHWIKI-METHOD-CLUSTER-408_根值判别法"
  - "MATHWIKI-METHOD-CLUSTER-498_p级数比较"
  - "MATHWIKI-METHOD-CLUSTER-907_对数化幂"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-068
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 0795e143d7e6747ab4e8b1b00dfc3f3684d745bd796bf85bc32dba7ad2a9e72c
---

# GS-495 102317 拆项根值判别

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-495_102317拆项根值判别.md`
- wrongnet ID：`GS-495`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-495_102317-2026.5.23.md`（`VIS-GS-495`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 复杂正项级数敛散性判断 |
| 日期 | 2026-05-23 |
| 状态 | 已掌握 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 无穷级数
- 数项级数敛散性判别
- 正项级数敛散性判别
- 正项级数比较判别法
- 根值判别法
- p级数
- 等价无穷小

### 错因

- 题型识别失败
- 方法选择错误
- 条件忽略
- 过程跳步

### 方法

- 先判型
- 拆项判断
- 比较判别法
- 根值判别法
- 等价变形
- 小量趋零
- p级数比较
- 对数化幂

### 陷阱

- 正项级数入口
- 拆项入口
- 整体高次幂
- 根值判别入口
- 等价使用条件
- 参数无关性

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把通项拆成 \(e^{\sin^2(\alpha n)/n^2}-1\) 和 \((\cos\frac1{\sqrt n})^{n^2}\) 两部分 |
| missed_action | 没有先拆项并分别选择判别法，导致根值判别入口没有触发 |
| related_method_card_id | H16-002 |
| next_reminder | 看到复杂正项通项相加，先拆成非负部分；\(e^{小量}-1\) 走比较，高次幂整体走根值判别。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-032_正项级数比较判别法]]
- [[MATHWIKI-KNOWLEDGE-036_p级数]]
- [[MATHWIKI-KNOWLEDGE-393_根值判别法]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-1013_拆项判断]]
- [[MATHWIKI-METHOD-CLUSTER-362_小量趋零]]
- [[MATHWIKI-METHOD-CLUSTER-408_根值判别法]]
- [[MATHWIKI-METHOD-CLUSTER-498_p级数比较]]
- [[MATHWIKI-METHOD-CLUSTER-907_对数化幂]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
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
