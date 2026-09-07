---
wiki_id: MATHWIKI-LA-METHOD-003
type: method
title: 可交换矩阵保持特征子空间
subject: 线性代数
knowledge:
  - 特征值与特征向量
  - 相似理论
  - 可交换矩阵
  - 相似对角化
methods:
  - 特征子空间不变性
  - 充分必要性拆分
  - 反例构造
error_causes:
  - 方法调取失败
  - 条件忽略
  - 充要条件混淆
triggers:
  - AB=BA
  - A 有互异特征值
  - 判断充分必要条件
source_refs:
  - 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-748_2024年选择题第10题.md
  - 错题知识网络/方法论库/方法卡/考研数学方法论卡片库_v2.md
wrongnet_refs:
  - MN4-GS-CH01-748
method_card_ids:
  - L07-007
wiki_refs:
  - MATHWIKI-LA-TOPIC-001
  - MATHWIKI-KNOWLEDGE-020
status: active
last_updated: 2026-07-01
---

# 可交换矩阵保持特征子空间

## 核心识别

看到

$$
AB=BA
$$

并且 \(A\) 的特征值结构清晰，先想到：\(B\) 会把 \(A\) 的特征子空间映到自己里面。

如果 \(A\alpha=\lambda\alpha\)，则

$$
A(B\alpha)=AB\alpha=BA\alpha=B(\lambda\alpha)=\lambda B\alpha.
$$

这说明 \(B\alpha\) 仍在 \(A\) 关于 \(\lambda\) 的特征子空间中。

## 方法链

1. 先拆命题方向：充分性和必要性分开判定。
2. 证明充分性时，用 \(AB=BA\) 推出 \(B\) 保持 \(A\) 的特征子空间。
3. 若 \(A\) 有互异特征值，则每个特征子空间是一维，因而

   $$
   B\alpha_i=k_i\alpha_i.
   $$

4. 于是 \(A\) 的特征向量组也可作为 \(B\) 的特征向量组，\(B\) 可对角化。
5. 证明“不必要”时，优先找最小反例，例如零矩阵或数量矩阵，不要试图从充分性倒推。

## 易错点

- 把“\(A\) 有互异特征值推出 \(B\) 可对角化”误看成双向结论。
- 只记住“可同时对角化”口号，却不会写 \(A(B\alpha)=\lambda B\alpha\) 这一步。
- 判断充要条件时没有主动拆成两个方向。

## 关联

- 视觉候选：[MN4-GS-CH01-748｜2024年选择题第10题](http://127.0.0.1:8765/open/MN4-GS-CH01-748)
- 专题：[[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- 方法卡：`L07-007`

## 复盘提醒

可交换矩阵题的第一句不是“它们一定同时对角化”，而是先写出 \(A(B\alpha)=\lambda B\alpha\)，看特征子空间是否被保持。
