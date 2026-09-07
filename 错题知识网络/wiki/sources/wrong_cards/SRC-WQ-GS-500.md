---
wiki_id: SRC-WQ-GS-500
type: source_summary
title: "GS-500 57941 全部渐近线清单"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-500_57941全部渐近线清单.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-500_57941-2026.5.25.md"
visual_ids:
  - "VIS-GS-500"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-500/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-500"
related_wrongnet_refs: []
knowledge:
  - "一元函数微分学应用"
  - "极限与连续"
  - "渐近线"
  - "无穷远极限"
  - "等价无穷小"
error_causes:
  - "审题遗漏"
  - "条件忽略"
  - "题型识别失败"
  - "过程跳步"
  - "定义域错误"
methods:
  - "先判型"
  - "定义域分析"
  - "斜渐近线公式"
  - "等价变形"
  - "有理化"
  - "分类讨论"
  - "正负无穷分别讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-030_定义域错误"
  - "MATHWIKI-ERROR-CLUSTER-037_审题遗漏"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-085_渐近线"
  - "MATHWIKI-KNOWLEDGE-093_无穷远极限"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-059_斜渐近线公式"
  - "MATHWIKI-METHOD-CLUSTER-235_有理化"
  - "MATHWIKI-METHOD-CLUSTER-238_正负无穷分别讨论"
  - "MATHWIKI-METHOD-CLUSTER-352_定义域分析"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-METHOD-048_渐近线题全类型检查链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-070
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 5905188b9a2dcbd0c2bef10c478c86369f22a073e9aa99317379eb6bcbbcccfc
---

# GS-500 57941 全部渐近线清单

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-500_57941全部渐近线清单.md`
- wrongnet ID：`GS-500`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-500_57941-2026.5.25.md`（`VIS-GS-500`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 全部渐近线判断 |
| 日期 | 2026-05-25 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 极限与连续
- 渐近线
- 无穷远极限
- 等价无穷小

### 错因

- 审题遗漏
- 条件忽略
- 题型识别失败
- 过程跳步
- 定义域错误

### 方法

- 先判型
- 定义域分析
- 斜渐近线公式
- 等价变形
- 有理化
- 分类讨论
- 正负无穷分别讨论

### 陷阱

- 全部渐近线
- 定义域端点
- 垂直渐近线漏判
- 左右无穷分别讨论
- 绝对值主导项
- 截距漏算
- 常数项

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先由 \(4x^2+x\ge0\) 和 \(2+\frac1x>0\) 求定义域，列出端点 \(x=-\frac12,0\)。 |
| missed_action | 没有先列“全部渐近线”检查表，只算了 \(x\to+\infty\) 方向，漏掉定义域端点和 \(x\to-\infty\) 方向。 |
| related_method_card_id | H05-005 |
| next_reminder | 看到“全部渐近线”，草纸第一行先写定义域端点、正无穷、负无穷三类检查点，再分别求垂直、水平或斜渐近线。 |
| evidence_origin | user_confirmed |
| repeat_count | 1 |
| repeat_count_source | wrong_history |

## 证据边界

- 个人错因仅来自正式卡 dated `wrong_history`；详情解析只核验题面与解法，不反推个人错因。
- 题图或解析图存在，只证明视觉来源已注册，不单独证明个人作答过程、错误次数或掌握度。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-030_定义域错误]]
- [[MATHWIKI-ERROR-CLUSTER-037_审题遗漏]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-085_渐近线]]
- [[MATHWIKI-KNOWLEDGE-093_无穷远极限]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-059_斜渐近线公式]]
- [[MATHWIKI-METHOD-CLUSTER-235_有理化]]
- [[MATHWIKI-METHOD-CLUSTER-238_正负无穷分别讨论]]
- [[MATHWIKI-METHOD-CLUSTER-352_定义域分析]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-METHOD-048_渐近线题全类型检查链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
