---
wiki_id: SRC-WQ-GS-482
type: source_summary
title: "GS-482 102421 阶乘级数放缩"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-482_102421阶乘级数放缩.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-482_102421-2026.5.21.md"
visual_ids:
  - "VIS-GS-482"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-482/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
identity_peer_refs: []
wrongnet_refs:
  - "GS-482"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "数项级数敛散性判别"
  - "正项级数敛散性判别"
  - "部分和数列"
error_causes:
  - "方法选择错误"
  - "题型识别失败"
  - "过程跳步"
methods:
  - "先判型"
  - "比较判别法"
  - "部分和有界"
  - "阶乘放缩"
  - "裂项相消"
  - "望远镜求和"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-129_部分和数列"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-012_比较判别法"
  - "MATHWIKI-METHOD-CLUSTER-073_望远镜求和"
  - "MATHWIKI-METHOD-CLUSTER-1401_阶乘放缩"
  - "MATHWIKI-METHOD-CLUSTER-259_裂项相消"
  - "MATHWIKI-METHOD-CLUSTER-263_部分和有界"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: user_confirmed
question_surface_status: registered
aggregate_edge_policy: allow
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 6c3ec298f8d9b9d569ee5980adeda6d8facd636912dcc5d129b1949e8831d89e
---

# GS-482 102421 阶乘级数放缩

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-482_102421阶乘级数放缩.md`
- wrongnet ID：`GS-482`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 视觉证据

- 详情页：[[错题知识网络/可视化错题详情/高等数学/GS-482_102421-2026.5.21|VIS-GS-482]]
- visual_id：`VIS-GS-482`
- 题图：`错题知识网络/assets/visual_wrong_questions/GS-482/question_01.png`
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 正项级数敛散性判别 |
| 日期 | 2026-05-21 |
| 状态 | 已掌握 |
| 优先级 | B |
| 难度 | 2 |

## 可编译信息

### 知识点

- 无穷级数
- 数项级数敛散性判别
- 正项级数敛散性判别
- 部分和数列

### 错因

- 方法选择错误
- 题型识别失败
- 过程跳步

### 方法

- 先判型
- 比较判别法
- 部分和有界
- 阶乘放缩
- 裂项相消
- 望远镜求和

### 陷阱

- 正项级数入口
- 部分和有界
- 阶乘分母放缩
- 裂项相消入口

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先拆出 \(0!\) 和 \(1!\) 两项，再对 \(k\ge2\) 写 \(k!\ge(k-1)k\) |
| missed_action | 没有想到把阶乘分母放缩成 \(\frac1{(k-1)k}\) 这种可裂项相消形式 |
| related_method_card_id | H16-001 |
| next_reminder | 看到阶乘在分母的正项级数，先找阶乘下界，把通项放大成可裂项相消的比较对象。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-129_部分和数列]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-073_望远镜求和]]
- [[MATHWIKI-METHOD-CLUSTER-1401_阶乘放缩]]
- [[MATHWIKI-METHOD-CLUSTER-259_裂项相消]]
- [[MATHWIKI-METHOD-CLUSTER-263_部分和有界]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 证据边界

- 个人断点只认“没有把阶乘分母放缩成可裂项相消的比较对象”；未发现同一阶乘级数对象、同一放缩第一动作且双端均有用户证据的卡片。
- 相似的正项级数判敛标签只保留为聚合索引，不提升为题间强边。

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
