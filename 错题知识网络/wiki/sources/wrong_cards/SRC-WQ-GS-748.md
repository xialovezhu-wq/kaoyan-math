---
wiki_id: "SRC-WQ-GS-748"
type: source_summary
title: "GS-748 84306 锥面母线消元与形心"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-748_84306锥面母线消元与形心.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-748_84306锥面母线消元与形心.md"
visual_ids:
  - "VIS-GS-748"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-748/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-748/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/GS-748/solution_02.png"
  - "错题知识网络/assets/visual_wrong_questions/GS-748/solution_03.png"
  - "错题知识网络/assets/visual_wrong_questions/GS-748/solution_04.png"
  - "错题知识网络/assets/visual_wrong_questions/GS-748/solution_05.png"
  - "错题知识网络/assets/visual_wrong_questions/GS-748/solution_06.png"
reference_asset_refs: []
wrongnet_refs:
  - "GS-748"
related_wrongnet_refs: []
knowledge:
  - "向量代数与空间解析几何"
  - "空间直线与平面"
  - "三重积分"
  - "空间直线参数方程"
  - "准线与母线"
  - "圆锥面"
  - "固定z截面法"
  - "实体形心"
error_causes:
  - "空间直线表示缺口"
  - "母线消元入口未建立"
  - "截面圆心平移遗漏"
  - "准线点与母线一般点混淆"
  - "参数角色混淆"
  - "截面边界与圆盘内部混淆"
  - "平移截面对称性误判"
  - "方向向量坐标差错误"
  - "平方和消元入口未触发"
methods:
  - "空间两点式"
  - "锥面母线消元"
  - "平移极坐标"
  - "形心积分"
  - "点向式参数方程"
  - "同比例变量平方和消元"
  - "固定z截面圆盘"
  - "圆锥体积公式"
wiki_refs:
  - MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
  - MATHWIKI-ACTION-GAP-010
  - MATHWIKI-KNOWLEDGE-089
chapter: "向量代数与空间解析几何"
question_type: "空间直线、锥面方程与形心"
card_status: "待复做"
priority: "A"
evidence_status: "user_confirmed"
status: indexed
last_updated: "2026-09-09"
formal_projection_sha256: "f1865f6ae55b7602e2f097d583d905c3eb08a86fddf9d518dc29810ba94a9364"
---

# GS-748 84306 锥面母线消元与形心

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-748_84306锥面母线消元与形心.md`
- wrongnet ID：`GS-748`
- 角色：正式错题卡的轻量可重建投影；本页不替代正式卡，也不保存完整题干或长解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-748_84306锥面母线消元与形心.md|VIS-GS-748]]

## 当前正式投影

- 章节：向量代数与空间解析几何
- 题型：空间直线、锥面方程与形心
- 知识点：向量代数与空间解析几何；空间直线与平面；三重积分；空间直线参数方程；准线与母线；圆锥面；固定z截面法；实体形心
- 方法：空间两点式；锥面母线消元；平移极坐标；形心积分；点向式参数方程；同比例变量平方和消元；固定z截面圆盘；圆锥体积公式
- 错因：空间直线表示缺口；母线消元入口未建立；截面圆心平移遗漏；准线点与母线一般点混淆；参数角色混淆；截面边界与圆盘内部混淆；平移截面对称性误判
- 状态：待复做

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-KG |
| expected_first_action | 写出 (x,y,z)=A+t(M1-A) |
| missed_action | 没有先分开固定顶点、准线点与母线一般点；未把 (x1,y1) 识别为选母线参数、t 识别为线上位置参数，导致直线表达和平方和消元都无法独立启动。 |
| next_reminder | 先写 P=A+t(M1-A)，逐项检查 t=0、1 的端点；再寻找 tx1、ty1 以调用准线约束。固定 z 做形心时先写圆盘中心、半径与内部径向范围。 |
| evidence_origin | user_confirmed |
| repeat_count | 2 |

## 证据边界

- 个人错因、复发次数与掌握证据只采用正式卡中的用户作答和确认事实。
- 助手讲解后的理解不计作无提示闭卷掌握；复习状态以正式卡与回滚系统为准。

## 已连接 Wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-010]]
- [[MATHWIKI-KNOWLEDGE-089]]

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]

## 2026-09-09 正式入库更新

- 一般点与准线点角色已区分；方向向量坐标差与平方和消元仍需提示。
