---
wiki_id: SRC-WQ-LA-111
type: source_summary
title: "LA-111 特征值充要条件相似形式"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-111_2022年真题第8题.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-749_2022年真题第8题.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-111_2022年真题第8题.md"
visual_ids:
  - "MN4-GS-CH01-749"
  - "VIS-LA-111"
wrongnet_refs:
  - "LA-111"
knowledge:
  - "相似矩阵"
  - "特征值与特征向量"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "相似对角化"
  - "相似不变量判定"
  - "合同相似区分"
wiki_refs: []
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
formal_projection_sha256: "55dde23f64cb1050b235b4cfccad6d724e8e471087c33255f9067d6c568c383d"
relation_review_batch: "MATHWIKI-REVIEW-088"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-749/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-111/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-749/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-111/solution_01.png"
reference_asset_refs: []
semantic_review_batch: "MATHWIKI-REVIEW-090"
content_review_status: "verified"
chapter: "相似理论"
topic: "特征值充要条件与相似形式辨析"
question_type: "特征值充要条件与相似形式辨析"
answer: "B"
method_refs:
  - "L08-001"
  - "L08-003"
evidence_status: "pending_user_confirmation"
---

# LA-111 B42 source projection

## 正式投影对象

- formal_card: `错题知识网络/错题卡/LA-111_2022年真题第8题.md`
- registered_detail_count: 2

## 可视化入口

- `MN4-GS-CH01-749`: `错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-749_2022年真题第8题.md`
- `VIS-LA-111`: `错题知识网络/可视化错题详情/线性代数/LA-111_2022年真题第8题.md`

## 注册视觉资产

以下清单覆盖本题全部注册资产；角色来自冻结清单。字节相同的来源副本仍保留各自路径，但不重复计作独立内容证据。

- question: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-749/question_01.png`
- question: `错题知识网络/assets/visual_wrong_questions/LA-111/question_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-749/solution_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/LA-111/solution_01.png`
- reference: 无

## method_gap 摘要

| 字段 | 值 |
|---|---|
| evidence_origin | pending_user_confirmation |
| repeat_count | 1 个旧导入事件；不确认个人断点 |
| expected_first_action | 先写普通相似对角化形式 \(A=P\Lambda P^{-1}\)，再检查互异特征值给出的可对角化条件。 |
| candidate_break | 候选断点是混淆普通相似、正交相似、合同和任意左右乘；尚无个人作答证据。 |
| method route | L08-001；L08-003 |

## B42 语义核验

- 客观对象：给定三个互异特征值，辨认普通相似对角化的充要形式。
- 正确路线：

$$
A=P\Lambda P^{-1}.
$$

- 解析图边界：一般情形下，“特征值相同”不能反推两个矩阵相似；本题能够收口，是因为三个特征值互不相同，从而矩阵可对角化。
- 个人证据边界：合同、正交相似或任意左右乘是否构成用户真实混淆，仍待复做确认。

## 关联卡片

- 暂无强边。
