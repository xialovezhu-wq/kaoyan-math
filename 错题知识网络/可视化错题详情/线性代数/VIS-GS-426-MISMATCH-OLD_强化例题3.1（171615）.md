---
visual_id: "VIS-GS-426-MISMATCH-OLD"
wrongnet_id: "待确认"
source_app: "MarginNote 4"
source_export: "/Users/xiazhibin/Library/Containers/QReader.MarginStudy.easy/Data/Documents/ExportedOmniOutlinerFiles/考研高数(2026-06-30-20-10-36).oo3/"
source_locator: "强化例题3.1（171615）"
source_refid: "6bddc21baf5b9c6ae410a41efad62214"
subject: "线性代数"
chapter: "矩阵运算"
status: "imported"
link_status: "needs_card_decision"
card_decision: "visual_candidate_enriched"
original_wrongnet_id: "GS-426"
last_updated: "2026-07-03"
---

# VIS-GS-426-MISMATCH-OLD｜强化例题3.1（171615）

## 原误链说明

本页原先误作为 [GS-426](http://127.0.0.1:8765/open/GS-426) 的正式视觉详情，但题图、解析图和 MarginNote 父级路径都属于线代第三讲矩阵运算；原正式卡 `GS-426` 是高数导数定义旧卡，不能使用本页题图。

当前处理结果：本页已从高数目录移入线性代数目录，并作为线代视觉候选保留。由于没有用户本人错因，也没有匹配到正式 LA 卡，暂不正式入库。

## 题目

![[错题知识网络/assets/visual_wrong_questions/VIS-GS-426-MISMATCH-OLD/question_01.png]]

> [!answer]- 解析（做完后展开）
> ![[错题知识网络/assets/visual_wrong_questions/VIS-GS-426-MISMATCH-OLD/solution_01.png]]
>
> 解析文字：待确认 / 未记录

## 复述

- 题目定位：三阶实矩阵满足 $(A^{\mathsf T}-A)A=O$，要求证明 $A=A^{\mathsf T}$。
- 正确第一步：先令 $B=A^{\mathsf T}-A$，把目标改写为证明 $B=O$，再用实矩阵为零的判别思路处理。
- 核心方法：矩阵转置与对称性；证明矩阵为零；迹法/秩法候选。
- 易错触发：看到“证明矩阵等于零”时，不要只逐项硬算，先想 $r(A)=0$、$\operatorname{tr}(AA^{\mathsf T})=0$ 这类零矩阵判别。

## 连线建议

- wrongnet：待确认
- 原误链：[GS-426](http://127.0.0.1:8765/open/GS-426)（已取消；正式卡仍缺正确高数题图）
- 正式错题卡：暂不连接；缺用户本人错因和正式 LA 卡。
- 专题总线：[[错题知识网络/wiki/topics/MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线|MATHWIKI-LA-TOPIC-001]]
- 知识点：线性代数；矩阵运算；实矩阵；转置矩阵；对称矩阵
- 方法页：[[MATHWIKI-LA-METHOD-010_伴随矩阵与反对称结构]]；[[MATHWIKI-LA-METHOD-008_矩阵运算结构识别]]
- 错因模式：待确认
- 复做提醒：若后续确认这是本人错题，先补“当时卡在哪里”，再判断是否创建 LA 正式卡和 method_gap。

## 入库判断

- 状态：visual_candidate_enriched
- 说明：题图与解析图已经按线代候选保留；缺用户本人具体错因，暂不正式入库。
- 2026-07-04 M104 复核：继续保持 `needs_card_decision`。原 GS-426 误链已剥离；未发现可安全合并的正式 LA 卡。正式化前需用户确认是否确实做错，以及卡点是目标转成证明 $A^{\mathsf T}-A=O$，还是实矩阵零判别入口。
- 转正式卡前需确认：是没想到把目标改成证明 $A^{\mathsf T}-A=O$，还是不知道实矩阵零判别入口。
- wrongnet_rebuild：not_needed_visual_only
- rollback_action：not_needed

## 来源记录

- MarginNote 标题：强化例题3.1（171615）
- OO3 refid：6bddc21baf5b9c6ae410a41efad62214
- 原误链：`GS-426`
- 来源导出：/Users/xiazhibin/Library/Containers/QReader.MarginStudy.easy/Data/Documents/ExportedOmniOutlinerFiles/考研高数(2026-06-30-20-10-36).oo3/
- 父级路径：考研数学强化 > 线代强化 > 线代第三讲矩阵运算 > 线代第三讲 > 证 A = O：可考虑由秩、伴随矩阵、迹法或行列正交等角度获得。
