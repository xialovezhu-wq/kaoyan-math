---
wiki_id: SRC-WQ-GS-750
type: source_summary
title: GS-750 138824 球面坐标质量与角色区分
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-750_138824球面坐标质量与角色区分.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-750_138824球面坐标质量与角色区分.md
wrongnet_refs:
- GS-750
knowledge:
- 多元函数积分学
- 球面坐标
- 三重积分
methods:
- 球面坐标
- 球锥区域定限
- 变密度质量积分
error_causes:
- 球面坐标角度定义混淆
- 密度与体积元角色混淆
- 边界曲面与立体区域混淆
- 边界等式未转为内部不等式
- 区域条件到坐标范围的动作链未建立
wiki_refs:
- MATHWIKI-ACTION-GAP-005
- MATHWIKI-KNOWLEDGE-073
chapter: 多元函数积分学
question_type: 球锥区域变密度质量积分
card_status: 待复做
evidence_status: user_confirmed
status: indexed
formal_projection_sha256: f9f8ffc0ba32e6d33442a503050788ad77081861fc4a1e5f9a5a254aaa9be76d
last_updated: '2026-09-02'
---

# GS-750 138824 球面坐标质量与角色区分

## 题目定位

球锥区域变密度质量积分。

## 当前错因

已独立识别质量是密度三重积分并想到球面坐标，但把两个边界曲面等式当作围成区域的完整描述，没有先建立球内且圆锥上方的不等式，因此无法确定角度范围。提示后给出正确范围；报积分式时只说dV，密度乘入由助手明确补齐。

## 独立步骤与提示依赖

调度评分3/5；质量积分、密度径向表达和球面坐标方向有独立证据。区域不等式、角度范围与完整质量积分依赖提示；用户自报后续积分算对，但未提交最终值或计算过程，不能认定整题独立正确。未将旧记录中密度r误写r²的问题重判为今日已确认错误。

## 下次复做动作

先写球内与圆锥上方两个不等式，再代入球面坐标定义确定范围。

## 来源

- [[错题知识网络/错题卡/GS-750_138824球面坐标质量与角色区分|GS-750 正式卡与完整历史]]

## 知识簇

- [[MATHWIKI-KNOWLEDGE-073]]
- [[MATHWIKI-ACTION-GAP-005]]
