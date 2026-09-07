---
wiki_id: SRC-WQ-GS-501
type: source_summary
title: "GS-501 19516 交错级数有理化拆项"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-501_19516交错级数有理化拆项.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-501_19516-2026.5.26.md"
visual_ids:
  - "VIS-GS-501"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-501/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-501"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "数项级数敛散性判别"
  - "交错级数"
  - "莱布尼茨判别法"
  - "调和级数"
  - "根式有理化"
  - "级数拆项"
error_causes:
  - "题型识别失败"
  - "方法选择错误"
  - "条件忽略"
  - "符号错误"
  - "过程跳步"
methods:
  - "先判型"
  - "正项部分提取"
  - "单调性检查"
  - "分母有理化"
  - "拆项判敛散"
  - "莱布尼茨判别法"
  - "调和级数发散"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-019_符号错误"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-059_交错级数"
  - "MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法"
  - "MATHWIKI-KNOWLEDGE-097_调和级数"
  - "MATHWIKI-KNOWLEDGE-128_级数拆项"
  - "MATHWIKI-KNOWLEDGE-154_根式有理化"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法"
  - "MATHWIKI-METHOD-CLUSTER-156_拆项判敛散"
  - "MATHWIKI-METHOD-CLUSTER-261_调和级数发散"
  - "MATHWIKI-METHOD-CLUSTER-417_正项部分提取"
  - "MATHWIKI-METHOD-CLUSTER-682_分母有理化"
  - "MATHWIKI-METHOD-CLUSTER-736_单调性检查"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-070
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: d9eac6f9e290d6dd98d4da2db032fa9306736750d4eb6ec88c3a85c1a01fe330
---

# GS-501 19516 交错级数有理化拆项

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-501_19516交错级数有理化拆项.md`
- wrongnet ID：`GS-501`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-501_19516-2026.5.26.md`（`VIS-GS-501`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 交错级数敛散性判断 |
| 日期 | 2026-05-26 |
| 状态 | 已掌握 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 无穷级数
- 数项级数敛散性判别
- 交错级数
- 莱布尼茨判别法
- 调和级数
- 根式有理化
- 级数拆项

### 错因

- 题型识别失败
- 方法选择错误
- 条件忽略
- 符号错误
- 过程跳步

### 方法

- 先判型
- 正项部分提取
- 单调性检查
- 分母有理化
- 拆项判敛散
- 莱布尼茨判别法
- 调和级数发散

### 陷阱

- 交错级数入口
- 莱布尼茨单调性遗漏
- 分母含负一的n次方
- 正项部分不单调
- 根式有理化
- 调和级数发散
- 不等号方向

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写正项部分 \(a_n=\frac1{\sqrt n+(-1)^n}\) 并检查它不单调，再对原通项分母有理化 |
| missed_action | 机械套莱布尼茨判别法，未先检查正项部分单调性，也没有先有理化拆出发散调和部分 |
| related_method_card_id | H16-016 |
| next_reminder | 看到 \((-1)^n\) 也在分母里，先检查正项部分是否单调；不满足莱布尼茨时先有理化拆项。 |
| evidence_origin | user_confirmed |
| repeat_count | 1 |
| repeat_count_source | wrong_history |

## 证据边界

- 个人错因仅来自正式卡 dated `wrong_history`；详情解析只核验题面与解法，不反推个人错因。
- 题图或解析图存在，只证明视觉来源已注册，不单独证明个人作答过程、错误次数或掌握度。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-019_符号错误]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-059_交错级数]]
- [[MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法]]
- [[MATHWIKI-KNOWLEDGE-097_调和级数]]
- [[MATHWIKI-KNOWLEDGE-128_级数拆项]]
- [[MATHWIKI-KNOWLEDGE-154_根式有理化]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法]]
- [[MATHWIKI-METHOD-CLUSTER-156_拆项判敛散]]
- [[MATHWIKI-METHOD-CLUSTER-261_调和级数发散]]
- [[MATHWIKI-METHOD-CLUSTER-417_正项部分提取]]
- [[MATHWIKI-METHOD-CLUSTER-682_分母有理化]]
- [[MATHWIKI-METHOD-CLUSTER-736_单调性检查]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
