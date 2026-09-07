---
wiki_id: MATHWIKI-GS-ERROR-005
type: error_pattern
title: 题型识别失败
subject: 高等数学
knowledge:
  - 极限与连续
  - 一元函数微分学应用
  - 中值定理
methods:
  - 先判型
  - 触发词识别
  - 方法入口排序
error_causes:
  - 题型识别失败
  - 方法选择错误
  - 触发信息遗漏
triggers:
  - 题面有明确触发词但没有转成方法入口
source_refs:
  - 错题知识网络/wiki/error_patterns/error_clusters/MATHWIKI-ERROR-CLUSTER-003_题型识别失败.md
  - 错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-006_先判型总流程.md
wrongnet_refs:
  - GS-017
  - GS-040
  - GS-041
  - GS-049
  - GS-059
  - GS-063
  - GS-079
method_card_ids:
  - 待匹配
wiki_refs:
  - MATHWIKI-ERROR-CLUSTER-003
  - MATHWIKI-GS-METHOD-006
  - MATHWIKI-GS-ERROR-003
status: active
last_updated: 2026-06-28
---

# 题型识别失败

## 定位

本页记录“题面已经给出触发信号，但没有识别成题型入口”的错因。它比方法选择错误更前置：不是入口选错，而是根本没有进入入口列表。

## 典型表现

- 看到“存在”“至少一个”“证明等式”没有想到中值定理或构造辅助函数。
- 看到“端点、收敛域、定义域、绝对值”没有想到先分类。
- 看到“通项、正负交错、幂级数”没有先判级数类型。
- 看到“变上限、分段点、参数”没有想到先画轴或设整体函数。

## 修复动作

1. 先圈触发词，不急着计算。
2. 把触发词写成候选题型：极限型、导数定义型、中值型、积分结构型、级数型、线代结构型。
3. 对每个候选题型写第一动作。
4. 如果触发词没有被用到，回到题面重读。

## 关联

- 错因簇：[[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- 方法：[[MATHWIKI-GS-METHOD-006_先判型总流程]]
- 错因：[[MATHWIKI-GS-ERROR-003_方法选择错误]]

## 来源

- `错题知识网络/wiki/error_patterns/error_clusters/MATHWIKI-ERROR-CLUSTER-003_题型识别失败.md`
- `错题知识网络/wiki/coverage/MATHWIKI-COVERAGE-MATRIX_错题卡多维编译矩阵.md`

