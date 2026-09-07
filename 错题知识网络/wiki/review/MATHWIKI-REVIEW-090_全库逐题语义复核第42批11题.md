---
wiki_id: MATHWIKI-REVIEW-090
type: target_level_semantic_review_batch
title: 全库逐题语义复核批次
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-090_全库逐题语义复核第42批11题.json
status: active
last_updated: 2026-07-25
---

# 全库逐题语义复核批次

## 本批结论

本批共逐题核对 11 张正式卡，当前哈希仍有效的完整复核为 0 张；覆盖 38 个物理图片路径与 19 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 1 张出现结构、身份、元数据或来源正文质量问题。问题只进入派生回执与修复队列；当前 SHADOW 模式没有改正式卡的 `related`、错因字段或视觉详情正文。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决是 SHADOW 建议，不授权写回正式 `related`。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [LA-110](http://127.0.0.1:8765/open/LA-110) | 判断下列矩阵中不能相似于对角矩阵的是哪一个。四个选项均为三阶矩阵，其中 A、B 都含重特征值，C 有三个不同特征值，D 为实对称矩阵。 | 相似矩阵、特征值与特征向量 | A。A 的 λ=1 代数重数为 2，但特征空间维数为 1，不能相似于对角矩阵。 | 待用户确认：未确认具体个人错因 | — |
| [LA-111](http://127.0.0.1:8765/open/LA-111) | 已知三阶矩阵 \(A\) 与 $$ \Lambda= \begin{pmatrix} 1&0&0\\ 0&-1&0\\ 0&0&0 \end{pmatrix}, $$ 要求判断“\(A\) 的特征值为 \(1,-1,0\)”的充分必要条件是哪一种矩阵关系。 | 相似矩阵、特征值与特征向量 | B | 待用户确认：未确认具体个人错因 | — |
| [LA-112](http://127.0.0.1:8765/open/LA-112) | 判断 3 阶实矩阵 \(A\) 中，“\(A\) 是实对称矩阵”是否是“\(A\) 有 3 个相互正交的特征向量”的充分必要条件。 | 实对称矩阵、特征值与特征向量、相似矩阵 | C | 待用户确认：未确认具体个人错因 | — |
| [LA-113](http://127.0.0.1:8765/open/LA-113) | recover the missing answer-determining condition before solving | 相似矩阵、特征值与特征向量、实对称矩阵、矩阵运算 | — | 历史结构化字段，来源未分类：未确认具体个人错因 | content_hold_missing_answer_determining_condition |
| [LA-114](http://127.0.0.1:8765/open/LA-114) | 已知 \(A,B\) 为可逆矩阵且 \(A\sim B\)，判断关于 \(A^{\mathsf T}\)、\(A^2+A^{-1}\)、\(A+A^{\mathsf T}\)、\(A^*-A^{-1}\) 的相似结论中哪一项错误。 | 相似矩阵、逆矩阵、伴随矩阵、矩阵运算 | C | 用户确认的个人错因：未确认具体个人错因 | — |
| [LA-115](http://127.0.0.1:8765/open/LA-115) | 已知 \(A^*\) 含参数 \(a\)，且 \(A^*\) 与矩阵 \(B\) 相似、\(\|A\|>0\)。求 \(a\)、可逆矩阵 \(Q\) 使 \(Q^{-1}A^*Q=B\)，并求 \(A^{99}\)。 | 相似矩阵、特征值与特征向量、伴随矩阵、逆矩阵、矩阵运算、行列式 | \(a=4,\ Q=\begin{pmatrix}0&1&1\\-2&0&0\\-1&1&2\end{pmatrix},\ A^{99}=\begin{pmatrix}3&2&-2\\0&-1&0\\4&2&-3\end{pmatrix}\). | 用户确认的个人错因：未确认具体个人错因 | — |
| [LA-116](http://127.0.0.1:8765/open/LA-116) | 设 \(A\) 为二阶矩阵， $$ P=(\alpha,A\alpha), $$ 其中 \(\alpha\ne0\) 且 \(\alpha\) 不是 \(A\) 的特征向量。先证明 \(P\) 可逆，再由 $$ A^2\alpha+A\alpha-6\alpha=0 $$ 求 \(P^{-1}AP\)，并判断 \(A\) 是否相似于对角矩阵。 | 相似矩阵、特征值与特征向量、矩阵运算、向量组线性无关 | P可逆；P^{-1}AP为坐标矩阵B；A可相似对角化 | 待用户确认：未确认具体个人错因 | — |
| [LA-117](http://127.0.0.1:8765/open/LA-117) | 给定上三角矩阵 $$ A= \begin{pmatrix} 1&1&0\\ 0&1&1\\ 0&0&1 \end{pmatrix}, $$ 要求在四个同样对角线为 \(1,1,1\) 的上三角矩阵中判断哪一个与 \(A\) 相似。 | 相似矩阵、特征值与特征向量、矩阵秩 | A | 待用户确认：未确认具体个人错因 | — |
| [LA-118](http://127.0.0.1:8765/open/LA-118) | 已知数列 \(\{x_n\},\{y_n\},\{z_n\}\) 满足 $$ x_0=-1,\qquad y_0=0,\qquad z_0=2, $$ 且 $$ \begin{cases} x_n=-2x_{n-1}+2z_{n-1},\\ y_n=-2y_{n-1}-2z_{n-1},\\ z_n=-6x_{n-1}-3y_{n-1}+3z_{n-1}. \end{cases} $$ 记 $$ \alpha_n= \begin{pmatrix} x_n\\y_n\\z_n \end{pmatrix}. $$ 写出满足 \(\alpha_n=A\alpha_{n-1}\) 的矩阵 \(A\)，并求 \(A^n\) 及 \(x_n,y_n,z_n\)。 | 相似矩阵、特征值与特征向量、矩阵运算 | \(A=\begin{pmatrix}-2&0&2\\0&-2&-2\\-6&-3&3\end{pmatrix}\)；当 \(n\ge1\)，\(x_n=(-2)^n+8,\ y_n=-2(-2)^n-8,\ z_n=12\)。 | 待用户确认：未确认具体个人错因 | — |
| [LA-119](http://127.0.0.1:8765/open/LA-119) | 设 \(A\) 为 3 阶正交矩阵，且第一行第一列元素为 \(1\)。令 \(\beta=(1,0,0)^{\mathsf T}\)，求方程组 \(AX=\beta\) 的解。 | 正交矩阵、矩阵运算、逆矩阵 | \((1,0,0)^{\mathsf T}\) | 待用户确认：未确认具体个人错因 | — |
| [PR-001](http://127.0.0.1:8765/open/PR-001) | 求含参数的和式极限，核心项形如 \(\sum_{i=1}^{n}\frac{i}{ni+a}\sin\frac{i}{n}\)，其中 \(a\in(0,1)\)。 | 定积分、定积分定义、黎曼和、一致估计、夹逼准则 | $$ 1-\cos 1 $$ 参数 \(a\) 不改变极限；先证明剩余乘法因子一致趋于 \(1\)，再保留标准黎曼和。 | 用户确认的个人错因：未确认具体个人错因 | — |

## 逐题复核

### LA-110 相似对角化几何重数判定

- 题目：判断下列矩阵中不能相似于对角矩阵的是哪一个。四个选项均为三阶矩阵，其中 A、B 都含重特征值，C 有三个不同特征值，D 为实对称矩阵。
- 所问：判断下列矩阵中不能相似于对角矩阵的是哪一个。四个选项均为三阶矩阵，其中 A、B 都含重特征值，C 有三个不同特征值，D 为实对称矩阵。
- 知识点：相似矩阵；特征值与特征向量
- 第一动作：先找重特征值，再计算对应的几何重数 \(n-r(\lambda I-A)\)。
- 答案：A。A 的 λ=1 代数重数为 2，但特征空间维数为 1，不能相似于对角矩阵。
- 个人错因边界：pending_user_confirmation；未确认具体个人错因
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 选 A。 对 A，有特征值 \(1,1,2\)。当 \(\lambda=1\) 时， $$ A-I= \begin{pmatrix} 0&1&0\\ 0&0&0\\ 0&0&1 \end{pmatrix}, $$ 所以 $$ r(A-I)=2,\qquad n-r(A-I)=1. $$ 而 \(\lambda=1\) 的代数重数为 \(2\)，几何重数只有 \(1\)，因此 A 不能相似于对角矩阵。
- 关系裁决：
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
- 当前快照：`stale`；正式卡 `32c90d1447325a94385721fccd279b88fb48de93641363f9fb0ed5ab8c011f57`；唯一图片 2 个；物理路径 4 个。

### LA-111 特征值充要条件相似形式

- 题目：已知三阶矩阵 \(A\) 与 $$ \Lambda= \begin{pmatrix} 1&0&0\\ 0&-1&0\\ 0&0&0 \end{pmatrix}, $$ 要求判断“\(A\) 的特征值为 \(1,-1,0\)”的充分必要条件是哪一种矩阵关系。
- 所问：已知三阶矩阵 \(A\) 与 $$ \Lambda= \begin{pmatrix} 1&0&0\\ 0&-1&0\\ 0&0&0 \end{pmatrix}, $$ 要求判断“\(A\) 的特征值为 \(1,-1,0\)”的充分必要条件是哪一种矩阵关系。
- 知识点：相似矩阵；特征值与特征向量
- 第一动作：先写普通相似对角化形式 \(A=P\Lambda P^{-1}\)，再检查互异特征值给出的可对角化条件。
- 答案：B
- 个人错因边界：pending_user_confirmation；未确认具体个人错因
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - \(B\)。存在可逆矩阵 \(P\)，使得 $$ A=P\Lambda P^{-1}. $$
- 关系裁决：
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
- 当前快照：`stale`；正式卡 `9762c41683dc9fe787cc0ca0a6f2630e70b0f4d898c0d51b3209847a89205205`；唯一图片 2 个；物理路径 4 个。

### LA-112 实对称与正交特征向量充要

- 题目：判断 3 阶实矩阵 \(A\) 中，“\(A\) 是实对称矩阵”是否是“\(A\) 有 3 个相互正交的特征向量”的充分必要条件。
- 所问：判断 3 阶实矩阵 \(A\) 中，“\(A\) 是实对称矩阵”是否是“\(A\) 有 3 个相互正交的特征向量”的充分必要条件。
- 知识点：实对称矩阵；特征值与特征向量；相似矩阵
- 第一动作：先把相互正交的特征向量单位化并组成正交矩阵 \(Q\)。
- 答案：C
- 个人错因边界：pending_user_confirmation；未确认具体个人错因
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - \(C\)，充分必要条件。
- 关系裁决：
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
- 当前快照：`stale`；正式卡 `c42bdbccd613783b95d59bee2e8259a23aba31c20d710fad495454fc3d6b8721`；唯一图片 2 个；物理路径 4 个。

### LA-113 行和实对称矩阵谱投影求幂

- 题目：题图只显示三阶实对称矩阵每行元素之和为 \(3\)，并在 $$ \lambda_1=\lambda_2= $$ 处结束。等号后没有可辨认数值，也没有独立解析图。因此，缺少决定答案的二重特征值，当前不能生成无条件答案。
- 所问：recover the missing answer-determining condition before solving
- 知识点：相似矩阵；特征值与特征向量；实对称矩阵；矩阵运算
- 第一动作：先回源补齐题图中二重特征值等号后的确切数值。
- 答案：—
- 个人错因边界：legacy_unclassified；未确认具体个人错因
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - \(J\)：三阶全一矩阵。 \(P\)：投影到 \(\operatorname{span}\{(1,1,1)^{\mathsf T}\}\) 的投影矩阵。 \(c\)：题图中缺失的二重特征值。 由行和为 \(3\) 可知 \((1,1,1)^{\mathsf T}\) 对应特征值 \(3\)，且 $$ P=\frac{1}{3}J. $$ 只有在补回二重特征值 \(c\) 后，才能条件化地写出 $$ A=c(I-P)+3P, $$ 以及 $$ A^n=c^n(I-P)+3^nP. $$
- 质量发现：
  - `content_hold_missing_answer_determining_condition`：；建议：
- 关系裁决：
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
- 当前快照：`stale`；正式卡 `773ab7eb415ed1af02474834c45f2cc1242154efbb7f21152362f8640fb86ac1`；唯一图片 1 个；物理路径 2 个。

### LA-114 相似关系传递边界

- 题目：已知 \(A,B\) 为可逆矩阵且 \(A\sim B\)，判断关于 \(A^{\mathsf T}\)、\(A^2+A^{-1}\)、\(A+A^{\mathsf T}\)、\(A^*-A^{-1}\) 的相似结论中哪一项错误。
- 所问：已知 \(A,B\) 为可逆矩阵且 \(A\sim B\)，判断关于 \(A^{\mathsf T}\)、\(A^2+A^{-1}\)、\(A+A^{\mathsf T}\)、\(A^*-A^{-1}\) 的相似结论中哪一项错误。
- 知识点：相似矩阵；逆矩阵；伴随矩阵；矩阵运算
- 第一动作：先固定同一个相似变换矩阵，再检查转置、逆、伴随和矩阵函数是否仍由该共轭变换传递。
- 答案：C
- 个人错因边界：confirmed_personal；未确认具体个人错因
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - \(C\)。
- 关系裁决：
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
- 当前快照：`stale`；正式卡 `9cb234d1b7612b5055acba0c9f39ff1e1bfb25afe04222fca9a035519489b163`；唯一图片 2 个；物理路径 4 个。

### LA-115 伴随矩阵相似传递求幂

- 题目：已知 \(A^*\) 含参数 \(a\)，且 \(A^*\) 与矩阵 \(B\) 相似、\(|A|>0\)。求 \(a\)、可逆矩阵 \(Q\) 使 \(Q^{-1}A^*Q=B\)，并求 \(A^{99}\)。
- 所问：已知 \(A^*\) 含参数 \(a\)，且 \(A^*\) 与矩阵 \(B\) 相似、\(|A|>0\)。求 \(a\)、可逆矩阵 \(Q\) 使 \(Q^{-1}A^*Q=B\)，并求 \(A^{99}\)。
- 知识点：相似矩阵；特征值与特征向量；伴随矩阵；逆矩阵；矩阵运算；行列式
- 第一动作：先比较 \(A^*\) 与 \(B\) 的特征多项式求参数，再构造换基矩阵。
- 答案：\(a=4,\ Q=\begin{pmatrix}0&1&1\\-2&0&0\\-1&1&2\end{pmatrix},\ A^{99}=\begin{pmatrix}3&2&-2\\0&-1&0\\4&2&-3\end{pmatrix}\).
- 个人错因边界：confirmed_personal；未确认具体个人错因
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - $$ a=4,\qquad Q= \begin{pmatrix} 0&1&1\\ -2&0&0\\ -1&1&2 \end{pmatrix}, $$ $$ A^{99}= \begin{pmatrix} 3&2&-2\\ 0&-1&0\\ 4&2&-3 \end{pmatrix}. $$
- 关系裁决：
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
- 当前快照：`stale`；正式卡 `cd19447f5cd47b72fda094638a526bdee99300a8d15c07e1f7c9a93aa2ddabe7`；唯一图片 2 个；物理路径 4 个。

### LA-116 循环基坐标求相似矩阵

- 题目：设 \(A\) 为二阶矩阵， $$ P=(\alpha,A\alpha), $$ 其中 \(\alpha\ne0\) 且 \(\alpha\) 不是 \(A\) 的特征向量。先证明 \(P\) 可逆，再由 $$ A^2\alpha+A\alpha-6\alpha=0 $$ 求 \(P^{-1}AP\)，并判断 \(A\) 是否相似于对角矩阵。
- 所问：设 \(A\) 为二阶矩阵， $$ P=(\alpha,A\alpha), $$ 其中 \(\alpha\ne0\) 且 \(\alpha\) 不是 \(A\) 的特征向量。先证明 \(P\) 可逆，再由 $$ A^2\alpha+A\alpha-6\alpha=0 $$ 求 \(P^{-1}AP\)，并判断 \(A\) 是否相似于对角矩阵。
- 知识点：相似矩阵；特征值与特征向量；矩阵运算；向量组线性无关
- 第一动作：先证明 \(\alpha,A\alpha\) 线性无关，确认 \(P=(\alpha,A\alpha)\) 可逆后再读 \(AP=PB\)。
- 答案：P可逆；P^{-1}AP为坐标矩阵B；A可相似对角化
- 个人错因边界：pending_user_confirmation；未确认具体个人错因
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - \(P\) 可逆，且 $$ P^{-1}AP= \begin{pmatrix} 0&6\\ 1&-1 \end{pmatrix}. $$ 该矩阵有两个不同特征值 \(2,-3\)，所以 \(A\) 相似于对角矩阵。
- 关系裁决：
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
- 当前快照：`stale`；正式卡 `b62b30f271393c8d2aef1dcb0b1250622288fdbb5ea588f0f6ac4177a999bae2`；唯一图片 2 个；物理路径 4 个。

### LA-117 同特征值矩阵相似秩不变量

- 题目：给定上三角矩阵 $$ A= \begin{pmatrix} 1&1&0\\ 0&1&1\\ 0&0&1 \end{pmatrix}, $$ 要求在四个同样对角线为 \(1,1,1\) 的上三角矩阵中判断哪一个与 \(A\) 相似。
- 所问：给定上三角矩阵 $$ A= \begin{pmatrix} 1&1&0\\ 0&1&1\\ 0&0&1 \end{pmatrix}, $$ 要求在四个同样对角线为 \(1,1,1\) 的上三角矩阵中判断哪一个与 \(A\) 相似。
- 知识点：相似矩阵；特征值与特征向量；矩阵秩
- 第一动作：先取唯一特征值 \(1\)，逐项比较 \(r(B_i-I)\)；不要先假设候选矩阵可对角化。
- 答案：A
- 个人错因边界：pending_user_confirmation；未确认具体个人错因
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - \(A\) 选项。
- 关系裁决：
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
- 当前快照：`stale`；正式卡 `cc3b7cc9525e257681961fb0df77129c718eed9a710d3244c4703fb7ac187924`；唯一图片 2 个；物理路径 4 个。

### LA-118 递推向量相似对角化求通项

- 题目：已知数列 \(\{x_n\},\{y_n\},\{z_n\}\) 满足 $$ x_0=-1,\qquad y_0=0,\qquad z_0=2, $$ 且 $$ \begin{cases} x_n=-2x_{n-1}+2z_{n-1},\\ y_n=-2y_{n-1}-2z_{n-1},\\ z_n=-6x_{n-1}-3y_{n-1}+3z_{n-1}. \end{cases} $$ 记 $$ \alpha_n= \begin{pmatrix} x_n\\y_n\\z_n \end{pmatrix}. $$ 写出满足 \(\alpha_n=A\alpha_{n-1}\) 的矩阵 \(A\)，并求 \(A^n\) 及 \(x_n,y_n,z_n\)。
- 所问：已知数列 \(\{x_n\},\{y_n\},\{z_n\}\) 满足 $$ x_0=-1,\qquad y_0=0,\qquad z_0=2, $$ 且 $$ \begin{cases} x_n=-2x_{n-1}+2z_{n-1},\\ y_n=-2y_{n-1}-2z_{n-1},\\ z_n=-6x_{n-1}-3y_{n-1}+3z_{n-1}. \end{cases} $$ 记 $$ \alpha_n= \begin{pmatrix} x_n\\y_n\\z_n \end{pmatrix}. $$ 写出满足 \(\alpha_n=A\alpha_{n-1}\) 的矩阵 \(A\)，并求 \(A^n\) 及 \(x_n,y_n,z_n\)。
- 知识点：相似矩阵；特征值与特征向量；矩阵运算
- 第一动作：先把三元递推写成 \(\alpha_n=A\alpha_{n-1}\)，再处理 \(A^n\)。
- 答案：\(A=\begin{pmatrix}-2&0&2\\0&-2&-2\\-6&-3&3\end{pmatrix}\)；当 \(n\ge1\)，\(x_n=(-2)^n+8,\ y_n=-2(-2)^n-8,\ z_n=12\)。
- 个人错因边界：pending_user_confirmation；未确认具体个人错因
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 由递推关系直接读出 $$ A= \begin{pmatrix} -2&0&2\\ 0&-2&-2\\ -6&-3&3 \end{pmatrix}. $$ 其特征值为 $$ -2,\ 0,\ 1. $$ 一组对应特征向量可取 $$ \lambda=-2:\begin{pmatrix}-1\\2\\0\end{pmatrix}, \qquad \lambda=0:\begin{pmatrix}1\\-1\\1\end{pmatrix}, \qquad \lambda=1:\begin{pmatrix}2\\-2\\3\end{pmatrix}. $$ 令 $$ P= \begin{pmatrix} -1&1&2\\ 2&-1&-2\\ 0&1&3 \end{pmatrix}, \qquad D=\operatorname{diag}(-2,0,1), $$ 则 $$ A=PDP^{-1}. $$ 当 \(n\ge1\) 时，\(0^n=0\)，所以 $$ A^n= \begin{pmatrix} -(-2)^n-4&-(-2)^n-2&2\\ 2(-2)^n+4&2(-2)^n+2&-2\\ -6&-3&3 \end{pmatrix}. $$ 又 $$ \alpha_0= \begin{pmatrix} -1\\0\\2 \end{pmatrix}, \qquad \alpha_n=A^n\alpha_0, $$ 故 $$ \begin{cases} x_n=(-2)^n+8,\\ y_n=-2(-2)^n-8,\\ z_n=12, \end{cases} \qquad n=1,2,\ldots $$
- 关系裁决：
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
- 当前快照：`stale`；正式卡 `89932a93a9c8e31994bc5f2d73d765118a228a59bd998e5e80308514683169b3`；唯一图片 1 个；物理路径 2 个。

### LA-119 正交矩阵首元约束解方程

- 题目：设 \(A\) 为 3 阶正交矩阵，且第一行第一列元素为 \(1\)。令 \(\beta=(1,0,0)^{\mathsf T}\)，求方程组 \(AX=\beta\) 的解。
- 所问：设 \(A\) 为 3 阶正交矩阵，且第一行第一列元素为 \(1\)。令 \(\beta=(1,0,0)^{\mathsf T}\)，求方程组 \(AX=\beta\) 的解。
- 知识点：正交矩阵；矩阵运算；逆矩阵
- 第一动作：先用正交矩阵行列向量的单位长度，推出含 \(1\) 的同一行和同一列其余元素为 \(0\)。
- 答案：\((1,0,0)^{\mathsf T}\)
- 个人错因边界：pending_user_confirmation；未确认具体个人错因
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - $$ X=(1,0,0)^{\mathsf T}. $$
- 关系裁决：
  - ：`remove_incident_strong_relation`；no independent question-method-personal-evidence basis survived the B42 target-level review
- 当前快照：`stale`；正式卡 `ff78cf080a6a0a7d6800c2167ce0fdffe4b73ce56cdfb11b4a40f1201eb06279`；唯一图片 2 个；物理路径 4 个。

### PR-001 强化例题8.2（历史编号待重连）

- 题目：求含参数的和式极限，核心项形如 \(\sum_{i=1}^{n}\frac{i}{ni+a}\sin\frac{i}{n}\)，其中 \(a\in(0,1)\)。
- 所问：求含参数的和式极限，核心项形如 \(\sum_{i=1}^{n}\frac{i}{ni+a}\sin\frac{i}{n}\)，其中 \(a\in(0,1)\)。
- 知识点：定积分；定积分定义；黎曼和；一致估计；夹逼准则
- 第一动作：拆出 \(1/n\) 后立刻估计 \(0<a/(ni)\le a/n\to0\)，把剩余因子识别为一致趋于 \(1\) 的扰动。
- 答案：$$
1-\cos 1
$$
参数 \(a\) 不改变极限；先证明剩余乘法因子一致趋于 \(1\)，再保留标准黎曼和。
- 个人错因边界：confirmed_personal；未确认具体个人错因
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - $$ 1-\cos 1 $$ 参数 \(a\) 不改变极限。先用统一估计消去乘法扰动，再得到 $$ \int_0^1\sin x\,dx=1-\cos 1. $$
- 当前快照：`stale`；正式卡 `077110e0e82513b047277aa36f24576457525995aa7f147b5b3a2e13e0db91cb`；唯一图片 1 个；物理路径 2 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
