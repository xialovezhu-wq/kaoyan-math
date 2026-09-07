---
wiki_id: MATHWIKI-GS-ERROR-001
type: error_pattern
title: 边界条件遗漏
subject: 高等数学
knowledge:
  - 参数分类讨论
  - 定义域
  - 幂级数收敛域
methods:
  - 边界检查
  - 分类讨论
error_causes:
  - 条件忽略
  - 条件检查遗漏
  - 参数范围错误
  - 分类讨论不全
triggers:
  - 参数、端点、定义域、绝对值、分段点、收敛域
source_refs:
  - 错题知识网络/方法论库/method_gap_schema.md
  - 错题知识网络/知识点库.md
wrongnet_refs:
  - GS-027
  - GS-141
  - GS-285
  - GS-358
  - GS-558
  - GS-569
  - GS-635
method_card_ids:
  - LM-H30
  - LM-H31
  - 待匹配
wiki_refs:
  - MATHWIKI-GS-CONCEPT-001
  - MATHWIKI-GS-METHOD-001
  - MATHWIKI-GS-TRIGGER-001
status: active
last_updated: 2026-06-28
---

# 边界条件遗漏

## 定位

本页记录“题会做，但边界没有先列出来，导致漏端点、漏等号、漏定义域或漏分段”的错因模式。

## 典型表现

- 看到参数先计算，没有先找临界值。
- 看到绝对值或分段函数，没有先画轴。
- 看到收敛域，没有单独检查端点。
- 使用公式前没有检查适用条件。

## 修复动作

1. 先写[[MATHWIKI-GS-METHOD-001_先做条件边界清单]]。
2. 每个边界旁边标注它改变了什么。
3. 最后做一次“端点/等号/定义域/分段归属”检查。

## 关联

- 概念：[[MATHWIKI-GS-CONCEPT-001_条件边界]]
- 触发：[[MATHWIKI-GS-TRIGGER-001_参数端点定义域先停]]
- 专题：[[MATHWIKI-GS-TOPIC-001_条件边界与分类讨论]]

## 来源

- `错题知识网络/方法论库/method_gap_schema.md`
- `错题知识网络/知识点库.md`
