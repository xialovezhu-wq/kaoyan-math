---
wiki_id: SRC-WQ-LA-115
type: source_summary
title: "LA-115 伴随矩阵相似传递求幂"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-115_强化例题8.6-2.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-753_强化例题8.6.md"
  - "错题知识网络/可视化错题详情/线性代数/LA-115_强化例题8.6-2.md"
visual_ids:
  - "MN4-GS-CH01-753"
  - "VIS-LA-115"
wrongnet_refs:
  - "LA-115"
knowledge:
  - "相似矩阵"
  - "特征值与特征向量"
  - "伴随矩阵"
  - "逆矩阵"
  - "矩阵运算"
  - "行列式"
error_causes:
  - "相似矩阵定义与不变量遗忘"
  - "矩阵乘法对象和左右乘作用混淆"
  - "齐次方程组与自由变量参数化不熟"
  - "特征值与特征向量角色混淆"
  - "非零与线性无关条件混淆"
  - "共同对角化构造 Q 的动作链断裂"
  - "逆矩阵初等行变换不熟"
  - "伴随矩阵求高次幂入口未触发"
methods:
  - "相似矩阵特征值相同"
  - "特征向量矩阵传递"
  - "伴随矩阵与行列式关系"
  - "相似对角化求幂"
wiki_refs:
  - "MATHWIKI-KNOWLEDGE-014"
  - "MATHWIKI-KNOWLEDGE-016"
  - "MATHWIKI-KNOWLEDGE-023"
  - "MATHWIKI-KNOWLEDGE-040"
  - "MATHWIKI-KNOWLEDGE-077"
  - "MATHWIKI-KNOWLEDGE-135"
  - "MATHWIKI-METHOD-CLUSTER-591"
  - "MATHWIKI-METHOD-CLUSTER-1189"
  - "MATHWIKI-METHOD-CLUSTER-1220"
  - "MATHWIKI-METHOD-CLUSTER-1223"
  - "MATHWIKI-ACTION-GAP-002"
status: indexed
last_updated: "2026-08-05"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-753/question_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-115/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-753/solution_01.png"
  - "错题知识网络/assets/visual_wrong_questions/LA-115/solution_01.png"
reference_asset_refs: []
related_wrongnet_refs: []
formal_projection_sha256: "8a1f0f619123484f725080a51bb4ad335830451831ec78b5d11c0987b1011b78"
semantic_review_batch: "MATH-IMMEDIATE-2026-08-05-LA-115"
content_review_status: "verified_with_user_attempt"
chapter: "相似理论"
question_type: "伴随矩阵相似反求参数与高次幂"
answer: "\\(a=4,\\ Q=\\begin{pmatrix}0&1&1\\\\-2&0&0\\\\-1&1&2\\end{pmatrix},\\ A^{99}=\\begin{pmatrix}3&2&-2\\\\0&-1&0\\\\4&2&-3\\end{pmatrix}\\)."
method_refs:
  - "L07-003"
  - "L08-007"
evidence_status: "user_confirmed"
---

# LA-115 B42 source projection

## 正式投影对象

- formal_card: `错题知识网络/错题卡/LA-115_强化例题8.6-2.md`
- registered_detail_count: 2

## 可视化入口

- `MN4-GS-CH01-753`: `错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-753_强化例题8.6.md`
- `VIS-LA-115`: `错题知识网络/可视化错题详情/线性代数/LA-115_强化例题8.6-2.md`

## 注册视觉资产

以下清单覆盖本题全部注册资产；角色来自冻结清单。字节相同的来源副本仍保留各自路径，但不重复计作独立内容证据。

- question: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-753/question_01.png`
- question: `错题知识网络/assets/visual_wrong_questions/LA-115/question_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-753/solution_01.png`
- solution: `错题知识网络/assets/visual_wrong_questions/LA-115/solution_01.png`
- reference: 无

## method_gap 摘要

| 字段 | 值 |
|---|---|
| evidence_origin | user_confirmed |
| repeat_count | 2026-08-05 首次取得真实个人作答证据；旧导入事件不用于判定同方法复发 |
| expected_first_action | 先写相似矩阵共享行列式与特征多项式，并由 \(|A^*|=|B|\) 求参数。 |
| confirmed_break | 忘记相似矩阵定义与公式，无法启动；矩阵乘法、方程组、特征向量、共同对角化、求逆和伴随矩阵高次幂链均不稳。 |
| method route | L07-003；L08-007 |

## B42 语义核验

- 客观对象：由 \(A^*\sim B\) 求参数、换基矩阵，并计算 \(A^{99}\)。
- 完整客观链：

$$
\chi_{A^*}(\lambda)=(\lambda-1)(\lambda+1)^2,\qquad \det(A^*)=1.
$$

构造题目要求的 \(Q\)，并直接核对

$$
Q^{-1}A^*Q=B,\qquad \det Q=2.
$$

再由三阶伴随矩阵关系

$$
\det(A^*)=\det(A)^2=1,\qquad \det(A)>0,
$$

得到 \(\det(A)=1\)，故 \(A=(A^*)^{-1}\)。又因

$$
(A^*)^2=I,
$$

最终有

$$
A^{99}=A^*.
$$

- 个人证据边界：2026-08-05 已确认整条知识与动作链存在真实断点；当前 2/5 来自讲解后局部复述和迁移，尚未无提示独立复做。

## 关联卡片

- 暂无强边。
