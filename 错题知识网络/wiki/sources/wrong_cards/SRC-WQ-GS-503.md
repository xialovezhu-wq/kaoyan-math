---
wiki_id: SRC-WQ-GS-503
type: source_summary
title: "GS-503 78385 有界因子望远镜绝对收敛"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-503_78385有界因子望远镜绝对收敛.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-503_78385-2026.5.26.md"
visual_ids:
  - "VIS-GS-503"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-503/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-503"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "数项级数敛散性判别"
  - "任意项级数"
  - "绝对收敛"
  - "正项级数比较判别法"
  - "望远镜级数"
  - "有界函数放缩"
error_causes:
  - "题型识别失败"
  - "方法选择错误"
  - "条件忽略"
  - "比较方向错误"
methods:
  - "先判型"
  - "取绝对值"
  - "有界性放缩"
  - "比较判别法"
  - "望远镜求和"
  - "部分和计算"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-383_比较方向错误"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-032_正项级数比较判别法"
  - "MATHWIKI-KNOWLEDGE-074_绝对收敛"
  - "MATHWIKI-KNOWLEDGE-087_任意项级数"
  - "MATHWIKI-KNOWLEDGE-262_望远镜级数"
  - "MATHWIKI-KNOWLEDGE-384_有界函数放缩"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-012_比较判别法"
  - "MATHWIKI-METHOD-CLUSTER-030_取绝对值"
  - "MATHWIKI-METHOD-CLUSTER-031_有界性放缩"
  - "MATHWIKI-METHOD-CLUSTER-073_望远镜求和"
  - "MATHWIKI-METHOD-CLUSTER-1385_部分和计算"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-070
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: bd91fae5a0bedef52aa666bca42f0e5dde6a9226f7272694297396da730fcfec
---

# GS-503 78385 有界因子望远镜绝对收敛

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-503_78385有界因子望远镜绝对收敛.md`
- wrongnet ID：`GS-503`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-503_78385-2026.5.26.md`（`VIS-GS-503`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 任意项级数绝对收敛判断 |
| 日期 | 2026-05-26 |
| 状态 | 已掌握 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 无穷级数
- 数项级数敛散性判别
- 任意项级数
- 绝对收敛
- 正项级数比较判别法
- 望远镜级数
- 有界函数放缩

### 错因

- 题型识别失败
- 方法选择错误
- 条件忽略
- 比较方向错误

### 方法

- 先判型
- 取绝对值
- 有界性放缩
- 比较判别法
- 望远镜求和
- 部分和计算

### 陷阱

- 任意项级数入口
- 绝对收敛优先
- 有界因子
- 放缩对象选错
- 大级数发散不能推出小级数发散
- 收敛大级数控制小级数
- 望远镜级数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先取绝对值并写 \(\|\sin(n+k)\|\le1\)，把通项压到 \(\frac1{\sqrt n}-\frac1{\sqrt{n+1}}\) |
| missed_action | 没有先走绝对收敛入口，而是被 \(\sin(n+k)\) 的符号变化带偏到交错级数 |
| related_method_card_id | H16-019 |
| next_reminder | 看到有界振荡因子乘可求和正项，先取绝对值，用有界性压到已知收敛级数。 |
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
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-383_比较方向错误]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-032_正项级数比较判别法]]
- [[MATHWIKI-KNOWLEDGE-074_绝对收敛]]
- [[MATHWIKI-KNOWLEDGE-087_任意项级数]]
- [[MATHWIKI-KNOWLEDGE-262_望远镜级数]]
- [[MATHWIKI-KNOWLEDGE-384_有界函数放缩]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-030_取绝对值]]
- [[MATHWIKI-METHOD-CLUSTER-031_有界性放缩]]
- [[MATHWIKI-METHOD-CLUSTER-073_望远镜求和]]
- [[MATHWIKI-METHOD-CLUSTER-1385_部分和计算]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
