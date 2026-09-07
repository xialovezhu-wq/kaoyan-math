---
wiki_id: SRC-WQ-LA-116
type: source_summary
title: "LA-116 循环基坐标求相似矩阵"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-116_2020年第23题.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-754_2020年第23题.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-116_2020年第23题.md"
visual_ids:
  - "MN4-GS-CH01-754"
  - "VIS-LA-116"
wrongnet_refs:
  - "LA-116"
knowledge:
  - "相似矩阵"
  - "特征值与特征向量"
  - "矩阵运算"
  - "向量组线性无关"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "换基表示"
  - "矩阵方程按列拆"
  - "相似对角化"
  - "特征值判定"
wiki_refs: []
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
review_batch: "MATHWIKI-REVIEW-086"
formal_projection_sha256: "f374bb6c68630424ea8f6fe8378ea9199d04b322c05077b66454bca4ef4e587c"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-754/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-116/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-754/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-116/solution_01.png"
reference_asset_refs: []
semantic_review_batch: "MATHWIKI-REVIEW-090"
content_review_status: "verified"
chapter: "相似理论"
topic: "循环基与坐标矩阵"
question_type: "循环基与相似对角化判定"
answer: "P可逆；P^{-1}AP为坐标矩阵B；A可相似对角化"
method_refs:
  - "L07-008"
  - "L08-001"
evidence_status: "pending_user_confirmation"
---

# LA-116 B42 source projection

## 正式投影对象

- formal_card: `错题知识网络/错题卡/LA-116_2020年第23题.md`
- registered_detail_count: 2

## 可视化入口

- `MN4-GS-CH01-754`: `错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-754_2020年第23题.md`
- `VIS-LA-116`: `错题知识网络/可视化错题详情/线性代数/LA-116_2020年第23题.md`

## 注册视觉资产

以下清单覆盖本题全部注册资产；角色来自冻结清单。字节相同的来源副本仍保留各自路径，但不重复计作独立内容证据。

- question: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-754/question_01.png`
- question: `错题知识网络/assets/visual_wrong_questions/LA-116/question_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-754/solution_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/LA-116/solution_01.png`
- reference: 无

## method_gap 摘要

| 字段 | 值 |
|---|---|
| evidence_origin | pending_user_confirmation |
| repeat_count | 1 个旧导入事件；不确认个人断点 |
| expected_first_action | 先证明 \(\alpha,A\alpha\) 线性无关，确认 \(P=(\alpha,A\alpha)\) 可逆后再读 \(AP=PB\)。 |
| candidate_break | 候选断点是把 \(\alpha,A\alpha\) 直接当成一组基，没有先证明线性无关。 |
| method route | L07-008；L08-001 |

## B42 语义核验

- 原题前提：\(\alpha\ne0\)，且 \(\alpha\) 不是 \(A\) 的特征向量。
- 先证明线性无关。若

$$
c_1\alpha+c_2A\alpha=0,
$$

且 \(c_2\ne0\)，则

$$
A\alpha=-\frac{c_1}{c_2}\alpha,
$$

这与 \(\alpha\) 不是特征向量矛盾。若 \(c_2=0\)，由 \(\alpha\ne0\) 得 \(c_1=0\)。
- 因而 \(\alpha,A\alpha\) 线性无关，\(P=(\alpha,A\alpha)\) 可逆；只有此后才能按列读取 \(AP=PB\)。
- 个人证据边界：不得把解析中的省略步骤伪造成用户已经掌握或已经犯过的错误。

## 关联卡片

- 暂无强边。
