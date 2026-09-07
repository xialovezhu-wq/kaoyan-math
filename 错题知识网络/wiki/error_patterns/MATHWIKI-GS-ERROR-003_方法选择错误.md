---
wiki_id: MATHWIKI-GS-ERROR-003
type: error_pattern
title: 方法选择错误
subject: 高等数学
knowledge:
  - 极限与连续
  - 一元函数微分学应用
  - 定积分
methods:
  - 先判型
  - 方法入口检查
error_causes:
  - 方法选择错误
  - 题型识别失败
  - 方法论调取失败
triggers:
  - 熟悉公式、熟悉结构、多个方法入口并存
source_refs:
  - 错题知识网络/wiki/error_patterns/error_clusters/MATHWIKI-ERROR-CLUSTER-001_方法选择错误.md
  - 错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-006_先判型总流程.md
wrongnet_refs:
  - GS-012
  - GS-016
  - GS-017
  - GS-025
  - GS-027
  - GS-032
  - GS-039
method_card_ids:
  - 待匹配
wiki_refs:
  - MATHWIKI-ERROR-CLUSTER-001
  - MATHWIKI-GS-METHOD-006
  - MATHWIKI-GS-METHOD-009
status: active
last_updated: 2026-06-28
---

# 方法选择错误

## 定位

本页记录“会算，但入口选错”的高频错因。它通常不是知识点完全不会，而是没有先判型、没有比较多个入口，或被局部形式诱导。

## 典型表现

- 看到可套公式就套，没判断公式是否是最短入口。
- 该先化结构，却先求导或积分。
- 该先看端点、符号、定义域，却直接代入。
- 该用整体、对称、换元或构造辅助函数，却只对局部表达式硬算。

## 修复动作

1. 先执行[[MATHWIKI-GS-METHOD-006_先判型总流程]]。
2. 写出两个候选入口，并删掉不满足条件的入口。
3. 对选定入口写第一动作，不只写方法名。
4. 做完后回查题干信号是否全部被使用。

## 关联

- 错因簇：[[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- 方法：[[MATHWIKI-GS-METHOD-006_先判型总流程]]
- B3 断点：[[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]

## 来源

- `错题知识网络/wiki/error_patterns/error_clusters/MATHWIKI-ERROR-CLUSTER-001_方法选择错误.md`
- `错题知识网络/wiki/coverage/MATHWIKI-COVERAGE-MATRIX_错题卡多维编译矩阵.md`

