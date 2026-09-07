---
wiki_id: SRC-WQ-GS-628
type: source_summary
title: "GS-628 102423 直线投影辅助平面"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-628_102423直线投影辅助平面.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-628_102423.md"
visual_ids:
  - "VIS-GS-628"
wrongnet_refs:
  - "GS-628"
knowledge:
  - "向量代数与空间解析几何"
  - "空间直线与平面"
  - "空间直线投影"
  - "两平面交线"
  - "平面束方程"
  - "辅助平面"
  - "法向量"
error_causes:
  - "空间几何图像断点"
  - "投影过程对象化断点"
  - "平面束触发不足"
  - "辅助平面关系混淆"
  - "法向量点积对象混淆"
  - "方法论调取失败"
methods:
  - "平面束方程"
  - "辅助平面法"
  - "平面垂直法向量点积"
  - "投影线交线法"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS"
  - "MATHWIKI-ACTION-GAP-001"
  - "MATHWIKI-ERROR-CLUSTER-007"
  - "MATHWIKI-ERROR-CLUSTER-038"
  - "MATHWIKI-ERROR-CLUSTER-077"
  - "MATHWIKI-ERROR-CLUSTER-208"
  - "MATHWIKI-ERROR-CLUSTER-385"
  - "MATHWIKI-ERROR-CLUSTER-434"
  - "MATHWIKI-KNOWLEDGE-089"
  - "MATHWIKI-KNOWLEDGE-127"
  - "MATHWIKI-KNOWLEDGE-157"
  - "MATHWIKI-KNOWLEDGE-228"
  - "MATHWIKI-KNOWLEDGE-359"
  - "MATHWIKI-KNOWLEDGE-417"
  - "MATHWIKI-KNOWLEDGE-428"
  - "MATHWIKI-METHOD-CLUSTER-002"
  - "MATHWIKI-METHOD-CLUSTER-1006"
  - "MATHWIKI-METHOD-CLUSTER-1345"
  - "MATHWIKI-METHOD-CLUSTER-985"
  - "MATHWIKI-METHOD-CLUSTER-986"
status: indexed
formal_projection_sha256: 0213f406bd6d3a30f50d025ff12fab761a0b3110f495b7ba77520914ab501023
last_updated: "2026-08-30"
related_wrongnet_refs: []
---

# GS-628 102423 直线投影辅助平面

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-628_102423直线投影辅助平面.md`
- wrongnet ID：`GS-628`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-628_102423|VIS-GS-628]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-628_102423)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-628/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-628/question_02.png`；`错题知识网络/assets/visual_wrong_questions/GS-628/solution_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-628/solution_02.png`；`错题知识网络/assets/visual_wrong_questions/GS-628/solution_03.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 向量代数与空间解析几何 |
| 题型 | 空间直线在平面上的正投影 / 平面束辅助平面法 |
| 日期 | 2026-06-25 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 本次正式结论

- 当前错点：当前首个断点是已经得到原直线方向和投影平面法向量，却把“投影线位于投影平面内”停留在平行条件，没有继续构造过 \(L_0\) 且垂直于 \(\Sigma\) 的辅助平面 \(\Sigma'\)，也没有形成 \(L=\Sigma'\cap\Sigma\) 的对象链。本轮旧有叉乘符号错误没有复现；当前优先路线是直接用过 \(L_0\) 的平面束和法向量点积筛出 \(\Sigma'\)。
- 最新错误证据：2026-08-30 第4次错：已独立正确求出原直线方向 \((1,4,2)\) 和投影平面法向量 \((1,1,-1)\)，但只停在“投影线与投影平面平行”，没有建立辅助平面 \(\Sigma'\) 过 \(L_0\)、垂直于 \(\Sigma\)，以及 \(L=\Sigma'\cap\Sigma\) 的对象链；在完整讲解和答案图后能复述平面束求 \(\lambda\) 的路线，未见无提示完整重做。
- 最新掌握证据：2026-08-30 本轮无规范评分。原直线方向与投影平面法向量属于独立正确局部步骤；辅助平面、平面束和最终交线均在提示或答案后完成，不能标记为独立掌握。

## 可编译信息

### 知识点

- 向量代数与空间解析几何
- 空间直线与平面
- 空间直线投影
- 两平面交线
- 平面束方程
- 辅助平面
- 法向量

### 错因

- 空间几何图像断点
- 投影过程对象化断点
- 平面束触发不足
- 辅助平面关系混淆
- 法向量点积对象混淆
- 方法论调取失败

### 方法

- 平面束方程
- 辅助平面法
- 平面垂直法向量点积
- 投影线交线法
- 条件转化

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把目标写成 \\(L=\\Sigma'\\cap\\Sigma\\)，再立即列过 \\(L_0\\) 的平面束并用两平面垂直确定参数。 |
| missed_action | 已有原直线方向与投影平面法向量，但没有把这些局部量连接到辅助平面和最终交线；平面束入口在答案与完整讲解前未独立调出。 |
| related_method_card_id | H00-007 |
| next_reminder | 直线投影到平面时，先找“投影幕布”：幕布必须过原直线且垂直于投影平面；最后影子线就是幕布和平面的交线。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-038_空间几何图像断点]]
- [[MATHWIKI-ERROR-CLUSTER-077_投影过程对象化断点]]
- [[MATHWIKI-ERROR-CLUSTER-208_平面束触发不足]]
- [[MATHWIKI-ERROR-CLUSTER-385_法向量点积对象混淆]]
- [[MATHWIKI-ERROR-CLUSTER-434_辅助平面关系混淆]]
- [[MATHWIKI-KNOWLEDGE-089_向量代数与空间解析几何]]
- [[MATHWIKI-KNOWLEDGE-127_空间直线与平面]]
- [[MATHWIKI-KNOWLEDGE-157_法向量]]
- [[MATHWIKI-KNOWLEDGE-228_两平面交线]]
- [[MATHWIKI-KNOWLEDGE-359_平面束方程]]
- [[MATHWIKI-KNOWLEDGE-417_空间直线投影]]
- [[MATHWIKI-KNOWLEDGE-428_辅助平面]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-1006_投影线交线法]]
- [[MATHWIKI-METHOD-CLUSTER-1345_辅助平面法]]
- [[MATHWIKI-METHOD-CLUSTER-985_平面垂直法向量点积]]
- [[MATHWIKI-METHOD-CLUSTER-986_平面束方程]]

### 深度方法与专题

- 本批保持索引型编译；未新增深度专题关系。
