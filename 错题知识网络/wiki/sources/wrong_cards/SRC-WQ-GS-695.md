---
wiki_id: "SRC-WQ-GS-695"
type: source_summary
title: "GS-695 84305 第一型曲线积分对称与形心"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-695_84305第一型曲线积分对称与形心.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-695_84305第一型曲线积分对称与形心.md"
visual_ids:
  - "VIS-GS-695"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-695/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-695/solution_01.png"
reference_asset_refs: []
wrongnet_refs:
  - "GS-695"
related_wrongnet_refs:
  - "GS-694"
  - "GS-690"
  - "GS-666"
knowledge:
  - "多元函数积分学"
  - "曲线积分"
  - "第一型曲线积分"
  - "弧长微元"
  - "曲线参数化"
error_causes:
  - "方法论调取失败"
  - "动作链断裂"
  - "概念混淆"
  - "积分整体等式与点态等式混淆"
  - "弧长微元与曲面面积微元混淆"
methods:
  - "第一型曲线积分轮换对称"
  - "积分整体系数平均"
  - "曲线方程代换"
  - "曲线形心公式逆用"
  - "圆周长计算"
  - "圆周参数化"
  - "弧长微元参数化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002"
  - "MATHWIKI-ERROR-CLUSTER-006"
  - "MATHWIKI-KNOWLEDGE-151"
  - "MATHWIKI-METHOD-CLUSTER-449"
chapter: "多元函数积分学"
question_type: "第一型曲线积分的互换对称与曲线形心"
card_status: "待复做"
priority: "A"
evidence_status: "user_confirmed"
status: indexed
last_updated: "2026-08-29"
formal_projection_sha256: "8a4ee02234da5d7a61d7a82f01d3b75ea4d5da3df1e220edc887c48aef2f9e2e"
---

# GS-695 84305 第一型曲线积分对称与形心

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-695_84305第一型曲线积分对称与形心.md`
- wrongnet ID：`GS-695`
- 角色：正式错题卡的轻量可重建投影；本页不替代正式卡，也不保存完整题干或长解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-695_84305第一型曲线积分对称与形心.md|VIS-GS-695]]

## 当前正式投影

- 章节：多元函数积分学
- 题型：第一型曲线积分的互换对称与曲线形心
- 知识点：多元函数积分学；曲线积分；第一型曲线积分；弧长微元；曲线参数化
- 方法：第一型曲线积分轮换对称；积分整体系数平均；曲线方程代换；曲线形心公式逆用；圆周长计算；圆周参数化；弧长微元参数化
- 错因：方法论调取失败；动作链断裂；概念混淆；积分整体等式与点态等式混淆；弧长微元与曲面面积微元混淆
- 状态：待复做

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先在积分号下写两个平方项积分相等；只在积分整体层面平均系数，不能先写被积函数点态等式。 |
| missed_action | 未把轮换对称写成两个曲线积分的整体等式；后续又把 \(ds\) 当成二维面积微元，未先确认曲线只有一个参数自由度。 |
| next_reminder | 看到第一型曲线积分中的 a x^2+b y^2，先写“积分整体相等”而不是点态相等；若需直接计算，先用一个参数表示曲线并写 \(ds=\\|r'(t)\\|dt\)。 |
| evidence_origin | 未单列 |
| repeat_count | 2 |

## 证据边界

- 个人错因、复发次数与掌握证据只采用正式卡中的用户作答和确认事实。
- 助手讲解后的理解不计作无提示闭卷掌握；复习状态以正式卡与回滚系统为准。

## 已连接 Wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002]]
- [[MATHWIKI-ERROR-CLUSTER-006]]
- [[MATHWIKI-KNOWLEDGE-151]]
- [[MATHWIKI-METHOD-CLUSTER-449]]

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
