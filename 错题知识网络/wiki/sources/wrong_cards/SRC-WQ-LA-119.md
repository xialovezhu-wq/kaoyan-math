---
wiki_id: SRC-WQ-LA-119
type: source_summary
title: "LA-119 正交矩阵首元约束解方程"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-119_强化例题8.9.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-757_强化例题8.9.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-119_强化例题8.9.md"
visual_ids:
  - "MN4-GS-CH01-757"
  - "VIS-LA-119"
wrongnet_refs:
  - "LA-119"
knowledge:
  - "正交矩阵"
  - "矩阵运算"
  - "逆矩阵"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "正交矩阵行列单位长度约束"
  - "正交矩阵逆等于转置"
  - "单位向量结构"
wiki_refs: []
status: indexed
last_updated: "2026-07-25"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-757/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-119/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-757/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-119/solution_01.png"
reference_asset_refs: []
related_wrongnet_refs: []
formal_projection_sha256: "a2272d179eb34b5263515706937184d169ee19a5e5e15e8098efe51c12c16153"
semantic_review_batch: "MATHWIKI-REVIEW-090"
content_review_status: "verified"
chapter: "矩阵运算"
topic: "正交矩阵的单位行列约束"
question_type: "正交矩阵结构约束下线性方程组求解"
answer: "\\((1,0,0)^{\\mathsf T}\\)"
method_refs:
  - "L08-008"
evidence_status: "pending_user_confirmation"
---

# LA-119 B42 source projection

## 正式投影对象

- formal_card: `错题知识网络/错题卡/LA-119_强化例题8.9.md`
- registered_detail_count: 2

## 可视化入口

- `MN4-GS-CH01-757`: `错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-757_强化例题8.9.md`
- `VIS-LA-119`: `错题知识网络/可视化错题详情/线性代数/LA-119_强化例题8.9.md`

## 注册视觉资产

以下清单覆盖本题全部注册资产；角色来自冻结清单。字节相同的来源副本仍保留各自路径，但不重复计作独立内容证据。

- question: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-757/question_01.png`
- question: `错题知识网络/assets/visual_wrong_questions/LA-119/question_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-757/solution_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/LA-119/solution_01.png`
- reference: 无

## method_gap 摘要

| 字段 | 值 |
|---|---|
| evidence_origin | pending_user_confirmation |
| repeat_count | 1 个旧导入事件；不确认个人断点 |
| expected_first_action | 先用正交矩阵行列向量的单位长度，推出含 \(1\) 的同一行和同一列其余元素为 \(0\)。 |
| candidate_break | 候选断点是只调用 \(A^{-1}=A^{\mathsf T}\)，没有先利用 \(a_{11}=1\) 固定首行首列结构。 |
| method route | L08-008 |

## B42 语义核验

- 客观对象：三阶正交矩阵满足 \(a_{11}=1\)，求 \(AX=e_1\)。
- 第一动作：由首行、首列都是单位向量，推出首行首列除 \(a_{11}\) 外均为 \(0\)。
- 再用

$$
X=A^{-1}e_1=A^{\mathsf T}e_1=e_1.
$$

- 本题知识标签限定为正交矩阵、矩阵运算和逆矩阵；删除与 LA-115 以及无关谱结构有关的关系和标签。
- 个人证据边界：具体断点仍待复做确认。

## 关联卡片

- 暂无强边。
