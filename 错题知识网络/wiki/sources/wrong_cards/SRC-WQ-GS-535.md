---
wiki_id: SRC-WQ-GS-535
type: source_summary
title: "GS-535 57779 泰勒余项放缩"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-535_57779泰勒余项放缩.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-535_57779-2026.6.1.md"
visual_ids:
  - "VIS-GS-535"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-535/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-535"
related_wrongnet_refs: []
knowledge:
  - "一元函数微分学应用"
  - "泰勒公式"
  - "泰勒展开"
  - "拉格朗日中值定理"
  - "中值定理"
error_causes:
  - "题型识别失败"
  - "方法选择错误"
  - "过程跳步"
  - "证明结构不完整"
methods:
  - "泰勒展开"
  - "拉格朗日余项"
  - "端点代入"
  - "两式相减"
  - "绝对值放缩"
  - "二阶导有界估计"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS"
  - "MATHWIKI-ACTION-GAP-002"
  - "MATHWIKI-ERROR-CLUSTER-001"
  - "MATHWIKI-ERROR-CLUSTER-002"
  - "MATHWIKI-ERROR-CLUSTER-003"
  - "MATHWIKI-ERROR-CLUSTER-011"
  - "MATHWIKI-KNOWLEDGE-001"
  - "MATHWIKI-KNOWLEDGE-010"
  - "MATHWIKI-KNOWLEDGE-015"
  - "MATHWIKI-KNOWLEDGE-021"
  - "MATHWIKI-KNOWLEDGE-038"
  - "MATHWIKI-METHOD-CLUSTER-008"
  - "MATHWIKI-METHOD-CLUSTER-118"
  - "MATHWIKI-METHOD-CLUSTER-178"
  - "MATHWIKI-METHOD-CLUSTER-276"
  - "MATHWIKI-METHOD-CLUSTER-283"
  - "MATHWIKI-METHOD-CLUSTER-444"
  - "MATHWIKI-GS-ERROR-003"
  - "MATHWIKI-GS-ERROR-004"
  - "MATHWIKI-GS-ERROR-005"
  - "MATHWIKI-GS-METHOD-010"
  - "MATHWIKI-GS-TOPIC-003"
  - "MATHWIKI-GS-TOPIC-005"
  - "MATHWIKI-SYNTHESIS-001"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因只来自正式卡日期化 wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-072
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: ac990188169d1d79d6f212b62035cdc6a1b157d469c8d7eeeee0720311a049ef
---

# GS-535 57779 泰勒余项放缩

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-535_57779泰勒余项放缩.md`
- wrongnet ID：`GS-535`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-535_57779-2026.6.1.md`（`VIS-GS-535`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 泰勒公式拉格朗日余项与放缩证明 |
| 日期 | 2026-06-01 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 泰勒公式
- 泰勒展开
- 拉格朗日中值定理
- 中值定理

### 错因

- 题型识别失败
- 方法选择错误
- 过程跳步
- 证明结构不完整

### 方法

- 泰勒展开
- 拉格朗日余项
- 端点代入
- 两式相减
- 绝对值放缩
- 二阶导有界估计

### 陷阱

- 第一问服务第二问
- 公式题继续硬算
- 端点展开遗漏
- 余项放缩
- \((1-c)^2+c^2\le1\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先在 c 点对任意 x 写 f(x)=f(c)+f'(c)(x-c)+f''(ξ)(x-c)^2/2 |
| missed_action | 已写出泰勒公式但没有意识到第一问就是该公式，第二问也没有先代 x=0,1 制造 f'(c) |
| related_method_card_id | H06-006 |
| next_reminder | 看到二阶导有界并要估计 f'(c)，先在 c 点写带余项的一阶 Taylor，再代两个端点相减。 |
| evidence_origin | user_confirmed |
| repeat_count | 1 |
| repeat_count_source | wrong_history |

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；详情解析只核验题面与解法，不反推个人错因。
- 题图或解析图存在，只证明视觉来源已登记，不单独证明个人作答过程、错误次数或掌握度。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS]]
- [[MATHWIKI-ACTION-GAP-002]]
- [[MATHWIKI-ERROR-CLUSTER-001]]
- [[MATHWIKI-ERROR-CLUSTER-002]]
- [[MATHWIKI-ERROR-CLUSTER-003]]
- [[MATHWIKI-ERROR-CLUSTER-011]]
- [[MATHWIKI-KNOWLEDGE-001]]
- [[MATHWIKI-KNOWLEDGE-010]]
- [[MATHWIKI-KNOWLEDGE-015]]
- [[MATHWIKI-KNOWLEDGE-021]]
- [[MATHWIKI-KNOWLEDGE-038]]
- [[MATHWIKI-METHOD-CLUSTER-008]]
- [[MATHWIKI-METHOD-CLUSTER-118]]
- [[MATHWIKI-METHOD-CLUSTER-178]]
- [[MATHWIKI-METHOD-CLUSTER-276]]
- [[MATHWIKI-METHOD-CLUSTER-283]]
- [[MATHWIKI-METHOD-CLUSTER-444]]
- [[MATHWIKI-GS-ERROR-003]]
- [[MATHWIKI-GS-ERROR-004]]
- [[MATHWIKI-GS-ERROR-005]]
- [[MATHWIKI-GS-METHOD-010]]
- [[MATHWIKI-GS-TOPIC-003]]
- [[MATHWIKI-GS-TOPIC-005]]
- [[MATHWIKI-SYNTHESIS-001]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
