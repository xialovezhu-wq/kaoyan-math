---
wiki_id: SRC-WQ-GS-513
type: source_summary
title: "GS-513 57720 含参方程根个数 2026.5.29"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-513_57720含参方程根个数.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-513_57720-2026.5.29.md"
visual_ids:
  - "VIS-GS-513"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-513/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-513"
related_wrongnet_refs: []
knowledge:
  - "一元函数微分学应用"
  - "方程根个数"
  - "单调性与极值"
  - "零点定理"
error_causes:
  - "方法选择错误"
  - "结构转化失败"
  - "条件忽略"
methods:
  - "先判型"
  - "同解变形"
  - "导数判单调"
  - "极值符号判根"
  - "分类讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS"
  - "MATHWIKI-ACTION-GAP-002"
  - "MATHWIKI-ERROR-CLUSTER-001"
  - "MATHWIKI-ERROR-CLUSTER-005"
  - "MATHWIKI-ERROR-CLUSTER-093"
  - "MATHWIKI-KNOWLEDGE-001"
  - "MATHWIKI-KNOWLEDGE-011"
  - "MATHWIKI-KNOWLEDGE-042"
  - "MATHWIKI-KNOWLEDGE-259"
  - "MATHWIKI-METHOD-CLUSTER-001"
  - "MATHWIKI-METHOD-CLUSTER-004"
  - "MATHWIKI-METHOD-CLUSTER-005"
  - "MATHWIKI-METHOD-CLUSTER-1108"
  - "MATHWIKI-METHOD-CLUSTER-213"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-070
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 4ff7c9cb6dd45caa855d031040045295dde9469fd6828541df26073e1456caf9
---

# GS-513 57720 含参方程根个数 2026.5.29

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-513_57720含参方程根个数.md`
- wrongnet ID：`GS-513`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-513_57720-2026.5.29.md`（`VIS-GS-513`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 含参方程根的个数 |
| 日期 | 2026-05-29 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 方程根个数
- 单调性与极值
- 零点定理

### 错因

- 方法选择错误
- 结构转化失败
- 条件忽略

### 方法

- 先判型
- 同解变形
- 导数判单调
- 极值符号判根
- 分类讨论

### 陷阱

- 参数边界
- 定义域
- 分式求导路线繁琐

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先利用 \(x\ne0\) 两边同乘 \(x^2\)，化为 \(kx^3-x^2+1=0\)，并单列 \(k=0\)。 |
| missed_action | 没有先化成整式三次方程，直接对分式求导，并险些漏掉 \(k=0\) 的退化情形。 |
| related_method_card_id | H05-006 |
| next_reminder | 看到含参数分式方程且给出 \(x\ne0\)，先同乘 \(x^2\) 化为整式；再单列 \(k=0\)，其余参数用导数和极值符号判根数。 |
| evidence_origin | user_confirmed |
| repeat_count | 1 |
| repeat_count_source | wrong_history |

## 证据边界

- 个人错因仅来自正式卡 dated `wrong_history`；详情解析只核验题面与解法，不反推个人错因。
- 题图或解析图存在，只证明视觉来源已注册，不单独证明个人作答过程、错误次数或掌握度。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS]]
- [[MATHWIKI-ACTION-GAP-002]]
- [[MATHWIKI-ERROR-CLUSTER-001]]
- [[MATHWIKI-ERROR-CLUSTER-005]]
- [[MATHWIKI-ERROR-CLUSTER-093]]
- [[MATHWIKI-KNOWLEDGE-001]]
- [[MATHWIKI-KNOWLEDGE-011]]
- [[MATHWIKI-KNOWLEDGE-042]]
- [[MATHWIKI-KNOWLEDGE-259]]
- [[MATHWIKI-METHOD-CLUSTER-001]]
- [[MATHWIKI-METHOD-CLUSTER-004]]
- [[MATHWIKI-METHOD-CLUSTER-005]]
- [[MATHWIKI-METHOD-CLUSTER-1108]]
- [[MATHWIKI-METHOD-CLUSTER-213]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
