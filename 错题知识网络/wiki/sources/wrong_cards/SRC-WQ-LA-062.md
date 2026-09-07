---
wiki_id: SRC-WQ-LA-062
type: source_summary
title: LA-062 Jordan链与矩阵平方根
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-062_强化例题3.20.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/线性代数/LA-062_强化例题3.20.md
visual_ids:
- VIS-LA-062
wrongnet_refs:
- LA-062
knowledge:
- Jordan链
- 幂零矩阵
- 矩阵平方根存在性
- 交换矩阵
error_causes:
- 个人错因待确认；旧导入与客观解析只支持复做风险，不证明用户本人断点。
methods:
- Jordan链构造
- 矩阵方程整理
- 齐次方程组基础解系
- 反例排除
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-ACTION-GAP-002_B4-CHAIN
- MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）
- MATHWIKI-KNOWLEDGE-014_矩阵运算
- MATHWIKI-KNOWLEDGE-033_线性方程组
- MATHWIKI-KNOWLEDGE-040_相似矩阵
- MATHWIKI-KNOWLEDGE-202_基础解系
- MATHWIKI-METHOD-CLUSTER-067_反例排除
- MATHWIKI-METHOD-CLUSTER-104_齐次方程组基础解系
- MATHWIKI-METHOD-CLUSTER-249_矩阵方程整理
- MATHWIKI-METHOD-CLUSTER-485_Jordan链构造
- MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点
- MATHWIKI-LA-METHOD-012_矩阵方程按列拆与解空间参数化
- MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线
- MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
last_updated: '2026-07-25'
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-062/question_01.png
solution_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/LA-062/solution_01.png
reference_asset_refs: []
related_wrongnet_refs: []
identity_refs: []
evidence_status: pending_user_confirmation
question_surface_status: registered_question_image_reviewed_no_user_answer_marks_found
solution_surface_status: registered_solution_image_objective_only_not_personal_evidence
aggregate_edge_policy: block_strong_edges
evidence_boundary: Question, source and solution material verify objective content only and must not be used to infer a personal breakpoint.
review_batch: MATHWIKI-REVIEW-086
content_review_status: verified
atomic_problem_status: verified_atomic
personal_diagnosis_status: candidate_pending_user_confirmation
formal_projection_sha256: ca09cf750c792c80a80c408cedbd5074cfaf46399c5389a82b5d136713f965ab
---

# LA-062 Jordan链与矩阵平方根

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-062_强化例题3.20.md`
- wrongnet ID：`LA-062`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/线性代数/LA-062_强化例题3.20.md`（`VIS-LA-062`）
- 题图 1 张；解析图 1 张；参考图 0 张。

## 当前语义投影

- 知识点：Jordan链、幂零矩阵、矩阵平方根存在性、交换矩阵
- 方法：Jordan链构造、矩阵方程整理、齐次方程组基础解系、反例排除
- 错因字段：个人错因待确认；旧导入与客观解析只支持复做风险，不证明用户本人断点。
- 第一动作：客观第一动作：先令 \(P=(a_1,a_2,a_3)\)，由 \(AP=PJ\) 写出链式向量关系
- 个人断点：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是只看相似式，没有按列拆出 Jordan 链并连接平方根存在性
- 方法卡 ID：L03-013
- 当前强关系：暂无强边

## 证据边界

- 题图与解析只核验客观题意和解法；个人错因保持 pending_user_confirmation，候选 method-gap 保持 disabled。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-033_线性方程组]]
- [[MATHWIKI-KNOWLEDGE-040_相似矩阵]]
- [[MATHWIKI-KNOWLEDGE-202_基础解系]]
- [[MATHWIKI-METHOD-CLUSTER-067_反例排除]]
- [[MATHWIKI-METHOD-CLUSTER-104_齐次方程组基础解系]]
- [[MATHWIKI-METHOD-CLUSTER-249_矩阵方程整理]]
- [[MATHWIKI-METHOD-CLUSTER-485_Jordan链构造]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-LA-METHOD-012_矩阵方程按列拆与解空间参数化]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- [[MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]

## 中心化子证明补全

第一问可取

$$
P=
\begin{pmatrix}
1&0&0\\
0&1&-\frac23\\
0&0&\frac13
\end{pmatrix}.
$$

令 \(J=J_3(0)\)，且 \(P=(a_1,a_2,a_3)\)。由 \(AP=PJ\) 逐列得到

$$
Aa_1=0,\qquad Aa_2=a_1,\qquad Aa_3=a_2,
$$

上述 \(P\) 的三列正好构成所需 Jordan 链。

第二问不存在这样的实三阶矩阵 \(B\)。若 \(B^2=A\)，令

$$
C=P^{-1}BP,
$$

则

$$
C^2=P^{-1}B^2P=P^{-1}AP=J.
$$

因为 \(C\) 与 \(C^2=J\) 可交换，所以 \(CJ=JC\)。这里补齐中心化子结论：取 \(J\) 的循环向量 \(e_3\)，则

$$
(e_3,Je_3,J^2e_3)
$$

构成一组基。若

$$
Ce_3=a e_3+bJe_3+cJ^2e_3,
$$

利用 \(CJ=JC\)，可知 \(C\) 在这组三个基向量上的作用都与 \(aE+bJ+cJ^2\) 相同，因此

$$
C=aE+bJ+cJ^2.
$$

又因 \(J^3=O\)，有

$$
C^2=a^2E+2abJ+(b^2+2ac)J^2.
$$

若 \(C^2=J\)，比较 \(E\) 的系数得 \(a^2=0\)，故 \(a=0\)；再比较 \(J\) 的系数却要求

$$
2ab=1,
$$

但左端为 \(0\)，矛盾。因此不存在 \(B\) 使 \(B^2=A\)。
