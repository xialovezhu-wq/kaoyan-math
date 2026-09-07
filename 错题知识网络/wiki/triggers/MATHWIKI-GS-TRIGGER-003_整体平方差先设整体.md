---
wiki_id: MATHWIKI-GS-TRIGGER-003
type: trigger
title: 整体平方差先设整体
subject: 高等数学
knowledge:
  - 定积分
  - 一元函数积分学的计算
  - 第一类换元
  - 第二类换元
methods:
  - 整体凑微分
  - 整体变量换元
  - 三角换元
  - Wallis/特殊公式
error_causes:
  - 触发信息遗漏
  - 动作链断裂
  - 整体变量识别不足
triggers:
  - 1-[整体]^2
  - g'(x)dx 与 g(x) 同现
  - 标准幂三角积分
source_refs:
  - 错题知识网络/错题卡/GS-636_58102-2整体换元幂三角.md
  - 错题知识网络/方法论库/方法卡/考研数学方法论卡片库_v2.md
wrongnet_refs:
  - GS-636
method_card_ids:
  - H09-002
  - H09-003
  - H11-009
wiki_refs:
  - MATHWIKI-GS-METHOD-005
  - MATHWIKI-GS-CONCEPT-002
  - MATHWIKI-GS-TRIGGER-002
status: active
last_updated: 2026-06-28
---

# 整体平方差先设整体

## 触发句

看到 \(g'(x)dx\) 和 \(1-[g(x)]^2\) 同时出现时，先设整体变量，不要直接对原来的 \(x\) 做三角换元。

## 第一动作

- 先把 \(g'(x)dx\) 凑成 \(d[g(x)]\)。
- 再令 \(u=g(x)\)，把被积函数改写成关于 \(u\) 的形式。
- 若出现 \(1-u^2\)，优先令 \(u=\sin t\) 或 \(u=\cos t\)。
- 若进入 \([0,\pi/2]\) 上的 \(\sin^n t\) 或 \(\cos^n t\)，接 Wallis/降幂。

## 反向提醒

如果你已经想到了“凑微分”，但下一步只是在原变量上硬套三角换元，要停下来问：真正应该被换掉的是不是刚凑出来的整体变量。

## 关联

- 方法：[[MATHWIKI-GS-METHOD-005_凑微分后的整体变量链]]
- 概念：[[MATHWIKI-GS-CONCEPT-002_积分结构中心]]
- 上位触发：[[MATHWIKI-GS-TRIGGER-002_积分先找中心与整体]]
- 专题：[[MATHWIKI-GS-TOPIC-002_一元积分近期错题簇]]
- 错题：`GS-636`

## 来源

- `错题知识网络/错题卡/GS-636_58102-2整体换元幂三角.md`
- `错题知识网络/方法论库/方法卡/考研数学方法论卡片库_v2.md`
