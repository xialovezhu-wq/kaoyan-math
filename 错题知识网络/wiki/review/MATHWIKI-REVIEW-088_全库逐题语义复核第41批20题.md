---
wiki_id: MATHWIKI-REVIEW-088
type: target_level_semantic_review_batch
title: 全库逐题语义复核第41批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-088_全库逐题语义复核第41批20题.json
status: active
last_updated: 2026-07-25
---

# 全库逐题语义复核第41批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 5 张；覆盖 56 个物理图片路径与 28 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 12 张出现结构、身份、元数据或来源正文质量问题。问题只进入派生回执与修复队列；当前 SHADOW 模式没有改正式卡的 `related`、错因字段或视觉详情正文。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决是 SHADOW 建议，不授权写回正式 `related`。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [LA-086](http://127.0.0.1:8765/open/LA-086) | 只有旧批量题号与线性方程组标签，没有可独立作答的具体题面。 | 线性方程组占位节点 | — | not_applicable_content_hold：不可推断。 | no_concrete_question_or_visual_evidence |
| [LA-087](http://127.0.0.1:8765/open/LA-087) | 三阶含参矩阵以 1 为特征多项式重根，并给出 A 对两个非零向量的两步作用关系，求参数及全部向量。 | 特征值重根、特征空间、链式矩阵作用、非齐次相容性 | \(a=3\)。所有解可写为 \(\alpha=(c_1,c_2,c_3)^{\mathsf T}\)，其中 \(2c_3-c_2-c_1\ne0\)，且 \(\beta=(2c_3-c_2-c_1)(1,1,1)^{\mathsf T}\)。 | pending_user_confirmation：旧卡未记录用户实际漏步；复做风险是硬解 \(\alpha,\beta\)，没有先识别 \(\beta\) 是特征向量 | formal_solution_misstates_lambda_one_eigenspace、embedded_ascii_control_characters |
| [LA-088](http://127.0.0.1:8765/open/LA-088) | 三阶矩阵满足 r(AB)=r(BA)+1，原题为四选一，判断相关齐次方程组的解性质。 | 矩阵秩、公共非零解、上下拼接矩阵 | 选 D。\(\begin{pmatrix}ABA\\BAB\end{pmatrix}x=0\) 有非零解，即 \(ABAx=0\) 与 \(BABx=0\) 有公共非零解。 | pending_user_confirmation：旧卡未记录用户实际漏步；复做风险是分别看两个方程组，忘记公共非零解要拼接成一个方程组 | formal_original_multiple_choice_not_standalone |
| [LA-089](http://127.0.0.1:8765/open/LA-089) | n 阶矩阵满足 A^2-A=3E，原题比较四个齐次方程组与 [A;B]x=0 是否同解。 | 矩阵多项式、可逆因子、齐次同解、特例反证 | 选 D。A、B、C 可由可逆变换得到与 \(\begin{pmatrix}A\\B\end{pmatrix}x=0\) 同解；D 可取 \(B=-A\)，使 \(\begin{pmatrix}A+B\\BA+B^2\end{pmatrix}x=0\) 与原方程组不同解。 | pending_user_confirmation：旧卡未记录用户实际漏步；复做风险是逐个方程组硬算通解，没有先找可逆变换链 | formal_original_multiple_choice_not_standalone、method_registry_route_mismatch |
| [LA-090](http://127.0.0.1:8765/open/LA-090) | 三阶含参矩阵的 A^2x=0 与 Ax=0 解集不同，求 a-b。 | 核空间包含、可逆性、行列式参数 | \(a-b=-4\) | pending_user_confirmation：旧卡未记录用户实际漏步；复做风险是直接展开 \(A^2\)，没有先利用可逆性和核空间包含关系 | — |
| [LA-091](http://127.0.0.1:8765/open/LA-091) | 给定两个三行四列矩阵及右端向量，证明一个非齐次方程组解集包含于另一个，并求使两解集不同的参数。 | 非齐次解集包含、增广矩阵行空间、参数秩退化 | 第 (1) 问成立；第 (2) 问 \(a=1\)。 | pending_user_confirmation：旧卡未记录用户实际漏步；复做风险是分别求通解导致计算膨胀，没先用增广矩阵秩判断解集包含 | — |
| [LA-092](http://127.0.0.1:8765/open/LA-092) | 求两个二维张成子空间在三维空间中的公共向量。 | 张成空间交、两种线性表示、齐次系数方程 | D，\(\gamma=k(1,5,8)^{\mathsf T},\ k\in\mathbb R\)。 | pending_user_confirmation：旧卡未记录用户实际漏步；复做风险是直接猜公共向量，没有先把两种表示式联立 | — |
| [LA-093](http://127.0.0.1:8765/open/LA-093) | 三个四维含参向量整体相关但任意两个无关，确定参数。 | 整体相关、两两无关、候选参数回验 | D，\(a=-2,\ b=2\)。 | pending_user_confirmation：旧卡未记录用户实际漏步；复做风险是只满足三向量相关，漏查任意两个均线性无关这一附加条件 | — |
| [LA-097](http://127.0.0.1:8765/open/LA-097) | 一组列向量可由另一组表示，原题为四选一，判断转置齐次方程组的解集包含。 | 向量组表示、矩阵关系转置、核空间包含方向 | D，\(B^{\mathsf T}x=0\) 的解均为 \(A^{\mathsf T}x=0\) 的解。 | pending_user_confirmation：旧卡未记录用户实际漏点；复做时重点确认是否漏掉“写矩阵关系 A=BC，再两边转置。”这一步。 | formal_original_multiple_choice_not_standalone |
| [LA-098](http://127.0.0.1:8765/open/LA-098) | 四列矩阵前三列无关且有一条列关系，求指定非齐次方程组通解。 | 抽象列关系、齐次方向、非齐次特解、通解 | \(\displaystyle x=\begin{pmatrix}5\\4\\-4\\0\end{pmatrix}+k\begin{pmatrix}1\\1\\-1\\-1\end{pmatrix},\ k\in\mathbb R\)，等价特解可取 \(\displaystyle \begin{pmatrix}1\\0\\0\\4\end{pmatrix}\)。 | pending_user_confirmation：旧卡未记录用户实际漏点；复做时重点确认是否漏掉“把 a1+a2=a3+a4 改写成齐次解方向。”这一步。 | duplicate_registered_question_asset_paths、visual_detail_closeout_state_stale |
| [LA-100](http://127.0.0.1:8765/open/LA-100) | 两个三维含参向量组等价时求参数，并把 beta3 用 alpha 组表示。 | 向量组等价、三秩相等、退化参数、线性表示 | 当 \(a\ne -1\) 时两向量组等价；若 \(a=1\)，\(\beta_3=(3-2k)\alpha_1+(k-2)\alpha_2+k\alpha_3\)；若 \(a\ne\pm1\)，\(\beta_3=\alpha_1-\alpha_2+\alpha_3\)。 | pending_user_confirmation：旧卡未记录用户实际漏点；复做时重点确认是否漏掉“用 r(A)=r(B)=r(A,B) 判等价参数。”这一步。 | — |
| [LA-101](http://127.0.0.1:8765/open/LA-101) | 与 LA-021、LA-051、LA-102 同一伴随矩阵迹题的截断副本。 | 矩阵多项式行列式、特征值、伴随矩阵迹 | — | identity_alias_no_independent_event：不适用。 | identity_duplicate_and_literal_question_truncation、repeat_count_not_supported_by_dated_history |
| [LA-102](http://127.0.0.1:8765/open/LA-102) | 与 LA-021、LA-051、LA-101 同一伴随矩阵迹题的截断副本。 | 矩阵多项式行列式、特征值、伴随矩阵迹 | — | identity_alias_no_independent_event：不适用。 | identity_duplicate_and_literal_question_truncation、repeat_count_not_supported_by_dated_history |
| [LA-103](http://127.0.0.1:8765/open/LA-103) | B=P^{-1}A^100P，求 B+E 的两条线性无关特征向量。 | 相似变换、矩阵多项式特征向量、坐标传递 | B | pending_user_confirmation：旧卡未记录用户实际漏点；复做时重点确认是否漏掉“求 A 的特征向量，再左乘 P^{-1}。”这一步。 | — |
| [LA-104](http://127.0.0.1:8765/open/LA-104) | 三阶实对称矩阵满足 A^2+A=2E 且行列式为 4，求二次型规范形。 | 矩阵多项式归零、实对称谱、特征值重数、惯性指数 | C | pending_user_confirmation：旧卡未记录用户实际漏点；复做时重点确认是否漏掉“由 f(A)=0 写出 f(lambda)=0。”这一步。 | — |
| [LA-105](http://127.0.0.1:8765/open/LA-105) | 已知相似对角阵为 diag(1,3,3)，原题四选一判断哪个候选 P 不可用。 | 相似对角化、列与对角元对应、特征空间内换基 | D | pending_user_confirmation：旧卡未记录用户实际漏点；复做时重点确认是否漏掉“逐列标注候选 P 的每一列应对应哪个特征值。”这一步。 | formal_original_multiple_choice_not_standalone |
| [LA-106](http://127.0.0.1:8765/open/LA-106) | 三阶矩阵满足 AB=-2B 与 CA^T=2C，给定 B、C，求 A 的全部特征值和特征向量。 | 矩阵方程按列读、转置、特征空间维数、向量组秩 | \(\lambda=-2\) 的特征向量为 \(\operatorname{span}\{(1,-1,2)^{\mathsf T},(2,1,-1)^{\mathsf T}\}\) 中的非零向量；\(\lambda=2\) 的特征向量为 \(k(1,-2,1)^{\mathsf T}\)，\(k\ne0\)。 | pending_user_confirmation：旧卡未记录用户实际漏点；复做时重点确认是否漏掉“把 B 拆成列向量，并把 CA^T=2C 转置成 AC^T=2C^T。”这一步。 | visual_detail_closeout_state_stale |
| [LA-107](http://127.0.0.1:8765/open/LA-107) | 相似理论讲义总纲的截断残片，不是具体题目。 | 相似理论总纲占位 | — | not_applicable_content_hold：不可推断。 | not_a_concrete_wrong_question_duplicate_outline |
| [LA-108](http://127.0.0.1:8765/open/LA-108) | 相似理论讲义总纲的截断残片，不是具体题目。 | 相似理论总纲占位 | — | not_applicable_content_hold：不可推断。 | not_a_concrete_wrong_question_duplicate_outline |
| [LA-109](http://127.0.0.1:8765/open/LA-109) | P^{-1}AP=diag(1,1,2)，把 P 第一列换成 alpha1+alpha2 后求新相似对角阵。 | 相似对角化、同一特征空间线性组合、列顺序 | B，Q^{-1}AQ=diag(1,1,2)。 | pending_user_confirmation：旧卡未记录用户实际漏点；复做时重点确认是否漏掉“判断 Q 的每一列仍属于哪个特征空间。”这一步。 | — |

## 逐题复核

### LA-086 强化例题5.2-3

- 题目：只有旧批量题号与线性方程组标签，没有可独立作答的具体题面。
- 所问：只有旧批量题号与线性方程组标签，没有可独立作答的具体题面。
- 知识点：线性方程组占位节点
- 第一动作：—
- 答案：—
- 个人错因边界：not_applicable_content_hold；不可推断。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 无题图、无可靠 OCR、无标准答案，不能做题目级数学核验。
- 质量发现：
  - `no_concrete_question_or_visual_evidence`：只有旧批量题号和宽泛标签，没有题面、题图、可靠 OCR、答案或个人作答证据。；建议：
- 当前快照：`current`；正式卡 `6fed0bb32c6afdcf7a4fd5d46666c6f1267bd94b56a73e2700b563d69e371a12`；唯一图片 0 个；物理路径 0 个。

### LA-087 重根特征值反求非齐次向量

- 题目：三阶含参矩阵以 1 为特征多项式重根，并给出 A 对两个非零向量的两步作用关系，求参数及全部向量。
- 所问：三阶含参矩阵以 1 为特征多项式重根，并给出 A 对两个非零向量的两步作用关系，求参数及全部向量。
- 知识点：特征值重根；特征空间；链式矩阵作用；非齐次相容性
- 第一动作：先用特征多项式在 lambda=1 处的重根条件确定 a，再比较 A(Aalpha) 与题设。
- 答案：\(a=3\)。所有解可写为 \(\alpha=(c_1,c_2,c_3)^{\mathsf T}\)，其中 \(2c_3-c_2-c_1\ne0\)，且 \(\beta=(2c_3-c_2-c_1)(1,1,1)^{\mathsf T}\)。
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏步；复做风险是硬解 \(\alpha,\beta\)，没有先识别 \(\beta\) 是特征向量
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 最终答案正确，但正式解析把 lambda=1 的二维特征空间误写成一维；正确做法是先保留两个特征方向，再由 (A-I)alpha=beta 的相容性排除第二方向。
- 质量发现：
  - `formal_solution_misstates_lambda_one_eigenspace`：a=3 时 N(A-E) 为二维，正式解析却直接写 beta=k(1,1,1)^T；最终一维限制实际来自 (A-E)alpha=beta 的相容性。最终答案正确，但中间论证错误。；建议：
  - `embedded_ascii_control_characters`：正文方法断点四行含 14 个 ASCII BEL/BS 控制字符，alpha 与 beta 被破坏，渲染和检索不稳定。；建议：
- 关系裁决：
  - ：``；
- 当前快照：`stale`；正式卡 `acbf511a32fe237d3e2e0e78c592e39a0c9dbd7f42423f3f70dca9788f3a587a`；唯一图片 2 个；物理路径 4 个。

### LA-088 秩差推出公共非零解

- 题目：三阶矩阵满足 r(AB)=r(BA)+1，原题为四选一，判断相关齐次方程组的解性质。
- 所问：三阶矩阵满足 r(AB)=r(BA)+1，原题为四选一，判断相关齐次方程组的解性质。
- 知识点：矩阵秩；公共非零解；上下拼接矩阵
- 第一动作：先用 |AB|=|BA| 把 r(BA) 压到不超过 1。
- 答案：选 D。\(\begin{pmatrix}ABA\\BAB\end{pmatrix}x=0\) 有非零解，即 \(ABAx=0\) 与 \(BABx=0\) 有公共非零解。
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏步；复做风险是分别看两个方程组，忘记公共非零解要拼接成一个方程组
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 由行列式乘法排除 r(BA)=2，得 r(BA) 不超过 1；上下拼接矩阵秩不超过 2，小于未知数个数 3。
- 质量发现：
  - `formal_original_multiple_choice_not_standalone`：正式卡省略原题选项；脱离登记题图不能完整复现原选择任务。；建议：
- 关系裁决：
  - ：``；
  - ：``；
  - ：``；
- 当前快照：`stale`；正式卡 `e5244202fa015b1ec52ec42a9e156923873246135f8f85ef493878e00cfa6830`；唯一图片 2 个；物理路径 4 个。

### LA-089 矩阵多项式下同解变形

- 题目：n 阶矩阵满足 A^2-A=3E，原题比较四个齐次方程组与 [A;B]x=0 是否同解。
- 所问：n 阶矩阵满足 A^2-A=3E，原题比较四个齐次方程组与 [A;B]x=0 是否同解。
- 知识点：矩阵多项式；可逆因子；齐次同解；特例反证
- 第一动作：先从 A^2-A=3E 提取 A 及相关因子的可逆性。
- 答案：选 D。A、B、C 可由可逆变换得到与 \(\begin{pmatrix}A\\B\end{pmatrix}x=0\) 同解；D 可取 \(B=-A\)，使 \(\begin{pmatrix}A+B\\BA+B^2\end{pmatrix}x=0\) 与原方程组不同解。
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏步；复做风险是逐个方程组硬算通解，没有先找可逆变换链
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - A、A+E、A-2E 均可逆；题图中的 A、B、C 可由可逆分块变换保持解集，D 可被 B=-A 反例否定。
- 质量发现：
  - `formal_original_multiple_choice_not_standalone`：正式卡省略原题选项；脱离登记题图不能完整复现原选择任务。；建议：
  - `method_registry_route_mismatch`：related_method_card_id=L07-005 指向 Cayley-Hamilton，但本题没有用特征多项式降幂；客观动作是从矩阵方程取可逆因子并判齐次同解。；建议：
- 关系裁决：
  - ：``；
  - ：``；
  - ：``；
- 当前快照：`stale`；正式卡 `b8fa761d1a6c41f94a6da23cd2ff0b4a4347c7405d54c1fe2ec5496fa2713dbb`；唯一图片 2 个；物理路径 4 个。

### LA-090 A2与A齐次方程不同解

- 题目：三阶含参矩阵的 A^2x=0 与 Ax=0 解集不同，求 a-b。
- 所问：三阶含参矩阵的 A^2x=0 与 Ax=0 解集不同，求 a-b。
- 知识点：核空间包含；可逆性；行列式参数
- 第一动作：先由解集不同排除 A 可逆。
- 答案：\(a-b=-4\)
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏步；复做风险是直接展开 \(A^2\)，没有先利用可逆性和核空间包含关系
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 解集不同必使 A 不可逆；det(A)=-a+b-4，故 a-b=-4。题目只问必要条件唯一确定的参数差。
- 关系裁决：
  - ：``；
  - ：``；
  - ：``；
- 当前快照：`stale`；正式卡 `1763cf6aac1c8b92cb4213b186919d06a71823005769562105d7a8cffa456a42`；唯一图片 2 个；物理路径 4 个。

### LA-091 增广矩阵秩判同解差异

- 题目：给定两个三行四列矩阵及右端向量，证明一个非齐次方程组解集包含于另一个，并求使两解集不同的参数。
- 所问：给定两个三行四列矩阵及右端向量，证明一个非齐次方程组解集包含于另一个，并求使两解集不同的参数。
- 知识点：非齐次解集包含；增广矩阵行空间；参数秩退化
- 第一动作：先比较 [A alpha; B beta] 与 [A alpha] 的秩。
- 答案：第 (1) 问成立；第 (2) 问 \(a=1\)。
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏步；复做风险是分别求通解导致计算膨胀，没先用增广矩阵秩判断解集包含
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 独立秩核验：r(A)=r(A,alpha)=3；拼接增广矩阵秩仍为 3。a=1 时 r(B)=r(B,beta)=2，第二个解集维数变大，故两者不同。
- 关系裁决：
  - ：``；
  - ：``；
  - ：``；
- 当前快照：`stale`；正式卡 `6dbccd68440e413c805666827108673b0257712302ba6ebc83d47f3b4f2d50c0`；唯一图片 2 个；物理路径 4 个。

### LA-092 两组向量张成空间交

- 题目：求两个二维张成子空间在三维空间中的公共向量。
- 所问：求两个二维张成子空间在三维空间中的公共向量。
- 知识点：张成空间交；两种线性表示；齐次系数方程
- 第一动作：先令同一 gamma 的两种线性组合相等。
- 答案：D，\(\gamma=k(1,5,8)^{\mathsf T},\ k\in\mathbb R\)。
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏步；复做风险是直接猜公共向量，没有先把两种表示式联立
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 联立两种线性表示的系数核为一维，可取 gamma=3alpha1-alpha2=(1,5,8)^T。
- 关系裁决：
  - ：``；
  - ：``；
  - ：``；
  - ：``；
- 当前快照：`stale`；正式卡 `6307650b3a1c2a9a8497b46063509345f2d7f61a0e05fb9c7e4a6dfa6bf1851c`；唯一图片 2 个；物理路径 4 个。

### LA-093 三向量相关两两无关参数

- 题目：三个四维含参向量整体相关但任意两个无关，确定参数。
- 所问：三个四维含参向量整体相关但任意两个无关，确定参数。
- 知识点：整体相关；两两无关；候选参数回验
- 第一动作：先用整体秩条件找候选，再逐对检查两两无关。
- 答案：D，\(a=-2,\ b=2\)。
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏步；复做风险是只满足三向量相关，漏查任意两个均线性无关这一附加条件
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 整体秩小于 3 给出 a=1 或 -2；a=1 使第一、第三向量相关，排除；a=-2 再由 a+b=0 得 b=2。
- 关系裁决：
  - ：``；
  - ：``；
  - ：``；
- 当前快照：`stale`；正式卡 `d168cfa49a265c59370c391b2a464bee3089e977c5cec6e54a6b38a32632e9e6`；唯一图片 2 个；物理路径 4 个。

### LA-097 表示关系转转置核包含

- 题目：一组列向量可由另一组表示，原题为四选一，判断转置齐次方程组的解集包含。
- 所问：一组列向量可由另一组表示，原题为四选一，判断转置齐次方程组的解集包含。
- 知识点：向量组表示；矩阵关系转置；核空间包含方向
- 第一动作：先把整组表示写成 A=BC，再转置。
- 答案：D，\(B^{\mathsf T}x=0\) 的解均为 \(A^{\mathsf T}x=0\) 的解。
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏点；复做时重点确认是否漏掉“写矩阵关系 A=BC，再两边转置。”这一步。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 写 A=BC 后转置为 A^T=C^T B^T，故 B^T x=0 必推出 A^T x=0。
- 质量发现：
  - `formal_original_multiple_choice_not_standalone`：正式卡省略原题选项；脱离登记题图不能完整复现原选择任务。；建议：
- 关系裁决：
  - ：``；
- 当前快照：`stale`；正式卡 `ce9c3a79def99a54ef53a857ef37c04ab1754b75d29481143252de6b1190f114`；唯一图片 2 个；物理路径 4 个。

### LA-098 强化例题6.5-2

- 题目：四列矩阵前三列无关且有一条列关系，求指定非齐次方程组通解。
- 所问：四列矩阵前三列无关且有一条列关系，求指定非齐次方程组通解。
- 知识点：抽象列关系；齐次方向；非齐次特解；通解
- 第一动作：先把列关系的系数写成齐次解方向。
- 答案：\(\displaystyle x=\begin{pmatrix}5\\4\\-4\\0\end{pmatrix}+k\begin{pmatrix}1\\1\\-1\\-1\end{pmatrix},\ k\in\mathbb R\)，等价特解可取 \(\displaystyle \begin{pmatrix}1\\0\\0\\4\end{pmatrix}\)。
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏点；复做时重点确认是否漏掉“把 a1+a2=a3+a4 改写成齐次解方向。”这一步。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 列关系给唯一齐次方向；矩阵秩为 3；右端列组合给出一个特解，两种所列特解相差 4 倍齐次方向。
- 质量发现：
  - `duplicate_registered_question_asset_paths`：LA-098/question_01.png 与 MN4-GS-CH01-737/question_01.png 字节完全相同，是两条物理路径的一份视觉内容。；建议：
  - `visual_detail_closeout_state_stale`：详情仍写 wrongnet_rebuild=needed_after_card_update，和当前已有正式卡、详情、source summary 的状态未收口。；建议：
- 关系裁决：
  - ：``；
  - ：``；
- 当前快照：`stale`；正式卡 `9a92dd7fb99cbb917e332faa6a16637ceea3fe7ca6688aa804edfa81f5b522a1`；唯一图片 1 个；物理路径 2 个。

### LA-100 向量组等价与表示式

- 题目：两个三维含参向量组等价时求参数，并把 beta3 用 alpha 组表示。
- 所问：两个三维含参向量组等价时求参数，并把 beta3 用 alpha 组表示。
- 知识点：向量组等价；三秩相等；退化参数；线性表示
- 第一动作：先检查 r(I)=r(II)=r(I,II)，再解 Ax=beta3。
- 答案：当 \(a\ne -1\) 时两向量组等价；若 \(a=1\)，\(\beta_3=(3-2k)\alpha_1+(k-2)\alpha_2+k\alpha_3\)；若 \(a\ne\pm1\)，\(\beta_3=\alpha_1-\alpha_2+\alpha_3\)。
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏点；复做时重点确认是否漏掉“用 r(A)=r(B)=r(A,B) 判等价参数。”这一步。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 独立复核四个代表参数：a=-1 时两组秩均为 2 但拼接秩为 3；a=1 时三秩均为 2；其他非退化点三秩均为 3。所列表示式均回代成立。
- 关系裁决：
  - ：``；
  - ：``；
  - ：``；
  - ：``；
- 当前快照：`stale`；正式卡 `c4e8a80974eb733193e8642510d4b6353b8eb5276511a5830d05d185628f3ebc`；唯一图片 2 个；物理路径 4 个。

### LA-101 强化例题7.1-4

- 题目：与 LA-021、LA-051、LA-102 同一伴随矩阵迹题的截断副本。
- 所问：与 LA-021、LA-051、LA-102 同一伴随矩阵迹题的截断副本。
- 知识点：矩阵多项式行列式；特征值；伴随矩阵迹
- 第一动作：先用 |A| 非零约去 A，再提取 -2 与 -1/2 两个特征值。
- 答案：—
- 个人错因边界：identity_alias_no_independent_event；不适用。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 客观答案可由规范卡 LA-021 核验；本卡自身题干在 tr(A^) 处截断，且无题图，不能作为独立原子题。
- 质量发现：
  - `identity_duplicate_and_literal_question_truncation`：题面在 tr(A^) 处字面截断、无自有题图，且与 LA-021、LA-051 及另一张同批卡是同题同答副本。；建议：
  - `repeat_count_not_supported_by_dated_history`：repeat_count=1 来自试点估计，但 mistake_count 与 wrong_history 均缺失；重复卡数量也不能当作重复做错次数。；建议：
- 当前快照：`current`；正式卡 `91a7abe98aa7f9b094985e4fce78e8c514d3c0a524972817fb796a0f8b036cbf`；唯一图片 0 个；物理路径 0 个。

### LA-102 强化例题7.1-5

- 题目：与 LA-021、LA-051、LA-101 同一伴随矩阵迹题的截断副本。
- 所问：与 LA-021、LA-051、LA-101 同一伴随矩阵迹题的截断副本。
- 知识点：矩阵多项式行列式；特征值；伴随矩阵迹
- 第一动作：先用 |A| 非零约去 A，再提取 -2 与 -1/2 两个特征值。
- 答案：—
- 个人错因边界：identity_alias_no_independent_event；不适用。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 客观答案可由规范卡 LA-021 核验；本卡自身题干在 tr(A^) 处截断，且无题图，不能作为独立原子题。
- 质量发现：
  - `identity_duplicate_and_literal_question_truncation`：题面在 tr(A^) 处字面截断、无自有题图，且与 LA-021、LA-051 及另一张同批卡是同题同答副本。；建议：
  - `repeat_count_not_supported_by_dated_history`：repeat_count=1 来自试点估计，但 mistake_count 与 wrong_history 均缺失；重复卡数量也不能当作重复做错次数。；建议：
- 当前快照：`current`；正式卡 `ce85973286d1e812669143aa9cfb0f9762cc23a6e38e1d080afbf62b426caebd`；唯一图片 0 个；物理路径 0 个。

### LA-103 相似变换传递特征向量

- 题目：B=P^{-1}A^100P，求 B+E 的两条线性无关特征向量。
- 所问：B=P^{-1}A^100P，求 B+E 的两条线性无关特征向量。
- 知识点：相似变换；矩阵多项式特征向量；坐标传递
- 第一动作：先求 A 的特征向量，再左乘 P^{-1}。
- 答案：B
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏点；复做时重点确认是否漏掉“求 A 的特征向量，再左乘 P^{-1}。”这一步。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - A 的特征向量可取 (-1,1)^T、(2,5)^T；左乘 P^{-1} 后分别得到 (-2,1)^T、(-3,5)^T，B+E 不改特征向量方向。
- 关系裁决：
  - ：``；
- 当前快照：`stale`；正式卡 `4481036a42973fa504b60d3f79f2a01ffb3e082b71fcebcc7d3f9c8b212e30ad`；唯一图片 2 个；物理路径 4 个。

### LA-104 矩阵多项式特征值定二次型规范形

- 题目：三阶实对称矩阵满足 A^2+A=2E 且行列式为 4，求二次型规范形。
- 所问：三阶实对称矩阵满足 A^2+A=2E 且行列式为 4，求二次型规范形。
- 知识点：矩阵多项式归零；实对称谱；特征值重数；惯性指数
- 第一动作：先令特征值满足 lambda^2+lambda-2=0。
- 答案：C
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏点；复做时重点确认是否漏掉“由 f(A)=0 写出 f(lambda)=0。”这一步。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 特征值只能为 1 或 -2，乘积为 4 迫使重数为 1,2；惯性为一正两负，规范形正确。
- 关系裁决：
  - ：``；
  - ：``；
- 当前快照：`stale`；正式卡 `5eb45f5a1af6d608eb022ded64dd824652c4037ae9f1f842f04bc2c7c7d8db31`；唯一图片 2 个；物理路径 4 个。

### LA-105 特征空间内换基判定P矩阵

- 题目：已知相似对角阵为 diag(1,3,3)，原题四选一判断哪个候选 P 不可用。
- 所问：已知相似对角阵为 diag(1,3,3)，原题四选一判断哪个候选 P 不可用。
- 知识点：相似对角化；列与对角元对应；特征空间内换基
- 第一动作：先逐列标注候选 P 的列向量所属特征空间。
- 答案：D
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏点；复做时重点确认是否漏掉“逐列标注候选 P 的每一列应对应哪个特征值。”这一步。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - D 的前两列混合了不同特征值的特征向量，不属于单一特征空间；其余候选只在 lambda=3 特征空间内做非退化换基或交换。
- 质量发现：
  - `formal_original_multiple_choice_not_standalone`：正式卡省略原题选项；脱离登记题图不能完整复现原选择任务。；建议：
- 关系裁决：
  - ：``；
  - ：``；
  - ：``；
- 当前快照：`stale`；正式卡 `d4bd20ad298fdc53c5d43ea940c345e9fb6f131f68e410b9ce110de21f9815ad`；唯一图片 2 个；物理路径 4 个。

### LA-106 矩阵乘法按列读特征向量

- 题目：三阶矩阵满足 AB=-2B 与 CA^T=2C，给定 B、C，求 A 的全部特征值和特征向量。
- 所问：三阶矩阵满足 AB=-2B 与 CA^T=2C，给定 B、C，求 A 的全部特征值和特征向量。
- 知识点：矩阵方程按列读；转置；特征空间维数；向量组秩
- 第一动作：先按列读 AB=-2B，并把 CA^T=2C 转置后再按列读。
- 答案：\(\lambda=-2\) 的特征向量为 \(\operatorname{span}\{(1,-1,2)^{\mathsf T},(2,1,-1)^{\mathsf T}\}\) 中的非零向量；\(\lambda=2\) 的特征向量为 \(k(1,-2,1)^{\mathsf T}\)，\(k\ne0\)。
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏点；复做时重点确认是否漏掉“把 B 拆成列向量，并把 CA^T=2C 转置成 AC^T=2C^T。”这一步。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - B 秩为 2、C 秩为 1，三条所得特征方向线性无关并张成三维空间；按列及转置核验矩阵等式均成立。
- 质量发现：
  - `visual_detail_closeout_state_stale`：详情仍写 wrongnet_rebuild=needed_after_formal_card_update。；建议：
- 关系裁决：
  - ：``；
  - ：``；
- 当前快照：`stale`；正式卡 `1ceb84218a8021f197384f3dfdfbbf6f788cb2e66afbebf84cb06ee2e985a3f6`；唯一图片 1 个；物理路径 2 个。

### LA-107 线代强化-第八讲-相似理论

- 题目：相似理论讲义总纲的截断残片，不是具体题目。
- 所问：相似理论讲义总纲的截断残片，不是具体题目。
- 知识点：相似理论总纲占位
- 第一动作：—
- 答案：—
- 个人错因边界：not_applicable_content_hold；不可推断。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 无具体条件、无题图、无解析、无可验证答案；与 LA-108 是同内容总纲副本。
- 质量发现：
  - `not_a_concrete_wrong_question_duplicate_outline`：内容是相似理论总纲截断残片，没有题目、答案或图片，并与 LA-108 实质重复。；建议：
- 关系裁决：
  - ：``；
- 当前快照：`current`；正式卡 `3f07f78d91341a4a474606c51e4809f386303a10726d232e39a2d757f30a8873`；唯一图片 0 个；物理路径 0 个。

### LA-108 线代强化第八讲-相似理论

- 题目：相似理论讲义总纲的截断残片，不是具体题目。
- 所问：相似理论讲义总纲的截断残片，不是具体题目。
- 知识点：相似理论总纲占位
- 第一动作：—
- 答案：—
- 个人错因边界：not_applicable_content_hold；不可推断。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 无具体条件、无题图、无解析、无可验证答案；与 LA-107 是同内容总纲副本。
- 质量发现：
  - `not_a_concrete_wrong_question_duplicate_outline`：内容是相似理论总纲截断残片，没有题目、答案或图片，并与 LA-107 实质重复。；建议：
- 关系裁决：
  - ：``；
- 当前快照：`current`；正式卡 `574509485f6da13d40b9c15426095f1f1a96f8ec4a5f9969674c6fe240b65e4e`；唯一图片 0 个；物理路径 0 个。

### LA-109 特征空间内换基不改对角元

- 题目：P^{-1}AP=diag(1,1,2)，把 P 第一列换成 alpha1+alpha2 后求新相似对角阵。
- 所问：P^{-1}AP=diag(1,1,2)，把 P 第一列换成 alpha1+alpha2 后求新相似对角阵。
- 知识点：相似对角化；同一特征空间线性组合；列顺序
- 第一动作：先判断 Q 的每一列仍属于哪个特征空间。
- 答案：B，Q^{-1}AQ=diag(1,1,2)。
- 个人错因边界：pending_user_confirmation；旧卡未记录用户实际漏点；复做时重点确认是否漏掉“判断 Q 的每一列仍属于哪个特征空间。”这一步。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - alpha1、alpha2 同属 lambda=1 特征空间，其和仍对应 lambda=1；三列顺序仍为 1,1,2。
- 关系裁决：
  - ：``；
  - ：``；
  - ：``；
  - ：``；
- 当前快照：`stale`；正式卡 `6c0692aee800f6ddfba68ebe6756b8eaafab736f47dbc18841b8eb795011d139`；唯一图片 2 个；物理路径 4 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
