---
wiki_id: MATHWIKI-GS-ERROR-004
type: error_pattern
title: 过程跳步
subject: 高等数学
knowledge:
  - 极限与连续
  - 中值定理
  - 一元函数微分学应用
methods:
  - 动作链补全
  - 条件转化
  - 检查闭环
error_causes:
  - 过程跳步
  - 动作链断裂
  - 证明结构不完整
triggers:
  - 会做方向但中间少一步、直接写结论、证明题跳到目标式
source_refs:
  - 错题知识网络/wiki/error_patterns/error_clusters/MATHWIKI-ERROR-CLUSTER-002_过程跳步.md
  - 错题知识网络/wiki/methods/action_gap_clusters/MATHWIKI-ACTION-GAP-002_B4-CHAIN.md
wrongnet_refs:
  - GS-017
  - GS-022
  - GS-025
  - GS-032
  - GS-034
  - GS-059
  - GS-063
method_card_ids:
  - 待匹配
wiki_refs:
  - MATHWIKI-ERROR-CLUSTER-002
  - MATHWIKI-GS-METHOD-010
status: active
last_updated: 2026-06-28
---

# 过程跳步

## 定位

本页记录“知道方向，但中间动作没有写完整”的错因。它常发生在证明、构造、分类、换元、端点检查和代数整理中。

## 典型表现

- 直接从题设跳到目标式，没有桥接条件。
- 看到熟悉结论就省掉验证条件。
- 换元、分段、构造辅助函数后，没有把变量、区间、端点、符号交代清楚。
- 证明题缺少“为什么存在”“为什么同号”“为什么可用定理”的一步。

## 修复动作

1. 把当前题写成“输入条件 -> 中间对象 -> 目标结论”。
2. 每个箭头必须补一个理由：定义、定理、等价变形、单调性、连续性、可导性、端点。
3. 若理由说不清，说明这里就是断点，不继续往后写。
4. 最后检查变量、区间和条件是否从头到尾一致。

## 关联

- 错因簇：[[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- B4 断点：[[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- 条件转化：[[MATHWIKI-GS-METHOD-007_条件转化总流程]]

## 来源

- `错题知识网络/wiki/error_patterns/error_clusters/MATHWIKI-ERROR-CLUSTER-002_过程跳步.md`
- `错题知识网络/wiki/methods/action_gap_clusters/MATHWIKI-ACTION-GAP-002_B4-CHAIN.md`

