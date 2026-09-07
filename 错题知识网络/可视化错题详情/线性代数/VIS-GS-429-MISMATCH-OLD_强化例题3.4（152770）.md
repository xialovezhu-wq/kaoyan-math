---
visual_id: "VIS-GS-429-MISMATCH-OLD"
wrongnet_id: "待确认"
source_app: "MarginNote 4"
source_export: "/Users/xiazhibin/Library/Containers/QReader.MarginStudy.easy/Data/Documents/ExportedOmniOutlinerFiles/考研高数(2026-06-30-20-10-36).oo3/"
source_locator: "强化例题3.4（152770）"
source_refid: "b12f1569b06dc9520716108cf592c7c6"
subject: "线性代数"
chapter: "矩阵运算"
status: "imported"
link_status: "needs_card_decision"
card_decision: "visual_candidate_enriched"
original_wrongnet_id: "GS-429"
last_updated: "2026-07-03"
---

# VIS-GS-429-MISMATCH-OLD｜强化例题3.4（152770）

## 原误链说明

本页原先误作为 [GS-429](http://127.0.0.1:8765/open/GS-429) 的正式视觉详情，但题图、解析图和 MarginNote 父级路径都属于线代第三讲矩阵运算；原正式卡 `GS-429` 是高数导数定义旧卡，不能使用本页题图。

当前处理结果：本页已从高数目录移入线性代数目录，并作为线代视觉候选保留。由于没有用户本人错因，也没有匹配到正式 LA 卡，暂不正式入库。

## 题目

![[错题知识网络/assets/visual_wrong_questions/VIS-GS-429-MISMATCH-OLD/question_01.png]]

> [!answer]- 解析（做完后展开）
> ![[错题知识网络/assets/visual_wrong_questions/VIS-GS-429-MISMATCH-OLD/solution_01.png]]
> ![[错题知识网络/assets/visual_wrong_questions/VIS-GS-429-MISMATCH-OLD/solution_02.png]]
>
> 解析文字：待确认 / 未记录

## 复述

- 题目定位：给定二维旋转型矩阵 $A=\begin{bmatrix}\frac{1}{2}&-\frac{\sqrt3}{2}\\\frac{\sqrt3}{2}&\frac{1}{2}\end{bmatrix}$，要求计算 $A^{-11}$。
- 正确第一步：先识别这是旋转 $60^\circ$ 的矩阵，判断 $A^6=E$，再把负指数化为周期内的正指数。
- 核心方法：旋转矩阵周期；逆矩阵幂；指数模周期化简。
- 易错触发：看到 $\cos\theta,\sin\theta$ 组成的二阶矩阵且指数很大或为负，先判旋转角和周期。

## 连线建议

- wrongnet：待确认
- 原误链：[GS-429](http://127.0.0.1:8765/open/GS-429)（已取消；正式卡仍缺正确高数题图）
- 正式错题卡：暂不连接；缺用户本人错因和正式 LA 卡。
- 专题总线：[[错题知识网络/wiki/topics/MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线|MATHWIKI-LA-TOPIC-001]]
- 知识点：线性代数；矩阵运算；矩阵幂；逆矩阵；旋转矩阵
- 方法页：[[MATHWIKI-LA-METHOD-008_矩阵运算结构识别]]；[[MATHWIKI-LA-METHOD-011_矩阵幂降维与秩空间判断]]
- 错因模式：待确认
- 复做提醒：若后续确认这是本人错题，先补“当时卡在哪里”，再判断是否创建 LA 正式卡和 method_gap。

## 入库判断

- 状态：visual_candidate_enriched
- 说明：题图与解析图已经按线代候选保留；缺用户本人具体错因，暂不正式入库。
- 2026-07-04 M104 复核：继续保持 `needs_card_decision`。原 GS-429 误链已剥离；未发现可安全合并的正式 LA 卡。正式化前需用户确认是否确实做错，以及卡点是旋转矩阵周期识别还是负指数周期化简。
- 转正式卡前需确认：是没识别旋转矩阵周期，还是负指数转正指数时周期化简出错。
- wrongnet_rebuild：not_needed_visual_only
- rollback_action：not_needed

## 来源记录

- MarginNote 标题：强化例题3.4（152770）
- OO3 refid：b12f1569b06dc9520716108cf592c7c6
- 原误链：`GS-429`
- 来源导出：/Users/xiazhibin/Library/Containers/QReader.MarginStudy.easy/Data/Documents/ExportedOmniOutlinerFiles/考研高数(2026-06-30-20-10-36).oo3/
- 父级路径：考研数学强化 > 线代强化 > 线代第三讲矩阵运算 > 线代第三讲 > 计算 A^n：试算低次、找周期或规律。
