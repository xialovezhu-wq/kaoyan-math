---
wiki_id: MATHWIKI-REVIEW-086
type: target_level_semantic_review_batch
title: 全库逐题语义复核第40批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-086_全库逐题语义复核第40批20题.json
status: active
last_updated: 2026-07-25
---

# 全库逐题语义复核第40批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 10 张；覆盖 23 个物理图片路径与 23 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 7 张出现结构、身份、元数据或来源正文质量问题。问题只进入派生回执与修复队列；当前 SHADOW 模式没有改正式卡的 `related`、错因字段或视觉详情正文。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决是 SHADOW 建议，不授权写回正式 `related`。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [LA-051](http://127.0.0.1:8765/open/LA-051) | 三阶 A 满足 det(A)=3、det(A^2+2A)=0、det(2A^2+A)=0，求三个主代数余子式之和；本卡正文在 tr(A*) 处截断。 | — | null | identity_alias_no_independent_event：不适用；不得由 canonical 客观内容反推 LA-051 的个人断点。 | personal_evidence_unadjudicated、formal_question_summary_truncated_and_unbalanced_math、duplicate_entity_unresolved、history_counter_inconsistency |
| [LA-052](http://127.0.0.1:8765/open/LA-052) | n 阶矩阵主对角为 0、非对角为 1，求逆矩阵。 | 逆矩阵、全一矩阵、秩一矩阵、矩阵可逆性、参数边界 n>=2 | 当 \\(n=1\\) 时不可逆；当 \\(n\\ge 2\\) 时，\\(A^{-1}=\\frac{1}{n-1}J-E\\)。 | pending_user_confirmation：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是按一般矩阵求逆硬算，没有先识别全一矩阵扰动结构 | personal_evidence_unadjudicated、missing_invertibility_domain_condition |
| [LA-053](http://127.0.0.1:8765/open/LA-053) | A 满足 A^3-2A^2+3A-4E=O，求 (A-E)^{-1}。 | 逆矩阵、矩阵多项式、矩阵多项式因式整理 | \((A-E)^{-1}=\frac{A^2-A+2E}{2}\)。 | pending_user_confirmation：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是只盯着逆矩阵定义，没有把矩阵多项式关系改写成 \((A-E)Q(A)=cE\) | personal_evidence_unadjudicated |
| [LA-054](http://127.0.0.1:8765/open/LA-054) | 非零 n 阶 A 满足 A^3=O，判断 E-A 与 E+A 的可逆性。 | 幂零矩阵、有限级数逆矩阵、矩阵可逆性 | C | pending_user_confirmation：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是把可逆性当行列式硬算，没有先识别幂零矩阵的有限级数逆 | personal_evidence_unadjudicated |
| [LA-056](http://127.0.0.1:8765/open/LA-056) | 已知 P 与 P^{-1}AP=diag(-1,-2,0)，计算 A^99。 | 相似对角化、矩阵高次幂、对角矩阵幂 | \(A^{99}=\begin{pmatrix}2^{99}-2&1-2^{99}&2-2^{98}\\2^{100}-2&1-2^{100}&2-2^{99}\\0&0&0\end{pmatrix}\)。 | pending_user_confirmation：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是直接乘 \(A\) 的高次幂，没有把相似关系转成高次幂关系 | personal_evidence_unadjudicated |
| [LA-057](http://127.0.0.1:8765/open/LA-057) | 给定四阶 A、4x2 矩阵 B 且 A=BC，求 C 与 A^10。 | 低秩分解、矩阵高次幂降维、列向量线性表示 | 见标准答案：\(C=\begin{pmatrix}-1&0&1&2\\2&1&0&-1\end{pmatrix}\)，\(A^{10}\) 如正文矩阵。 | pending_user_confirmation：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是对原阶矩阵硬算高次幂，没有把中间乘积 \(CB\) 降到低维 | personal_evidence_unadjudicated |
| [LA-058](http://127.0.0.1:8765/open/LA-058) | A、B 为 n 阶矩阵，判断横拼分块矩阵的秩恒等式。 | 矩阵秩、列空间包含、横拼分块矩阵 | A | pending_user_confirmation：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是看到横拼就套公式，没有先验证新增块是否落入原列空间 | personal_evidence_unadjudicated |
| [LA-061](http://127.0.0.1:8765/open/LA-061) | 二阶 A、非特征向量 alpha，P=[alpha,Aalpha]，由 A^2alpha+Aalpha-2alpha=0 求 AP=PB 中的 B。 | 循环基、相似变换、矩阵方程按列读、坐标表示 | \(B=\begin{pmatrix}0&2\\1&-1\end{pmatrix}\)。 | pending_user_confirmation：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是知道换基但没有按列读出坐标列 | personal_evidence_unadjudicated |
| [LA-062](http://127.0.0.1:8765/open/LA-062) | 把给定三阶幂零 A 相似到 J3(0)，并判断是否存在三阶 B 使 B^2=A。 | Jordan链、幂零矩阵、矩阵平方根存在性、交换矩阵 | \(P=\begin{pmatrix}1&0&0\\0&1&-\frac23\\0&0&\frac13\end{pmatrix}\) 可使 \(P^{-1}AP=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}\)；不存在三阶矩阵 \(B\) 使 \(B^2=A\)。 | pending_user_confirmation：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是只看相似式，没有按列拆出 Jordan 链并连接平方根存在性 | personal_evidence_unadjudicated、standalone_solution_proof_underexplained |
| [LA-063](http://127.0.0.1:8765/open/LA-063) | 含参 A 可经初等列变换化为 B，求 a 与所有满足 AP=B 的可逆 P。 | 列等价、秩不变性、矩阵方程、非齐次方程组通解、可逆性检验 | \(a=2\)，且 \(P=\begin{pmatrix}3-6k_1&4-6k_2&4-6k_3\\-1+2k_1&-1+2k_2&-1+2k_3\\k_1&k_2&k_3\end{pmatrix}\)，其中 \(k_2\ne k_3\)。 | pending_user_confirmation：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是跳过列等价保秩的参数条件，直接设 \(P\) 导致方程链混乱 | personal_evidence_unadjudicated |
| [LA-064](http://127.0.0.1:8765/open/LA-064) | 给定秩 2 的三阶 A，求全部非单位 B 使 AB=A。 | 矩阵方程、零空间、基础解系、解空间参数化 | 存在，\(B=\begin{pmatrix}1+k_1&k_2&k_3\\-k_1&1-k_2&-k_3\\k_1&k_2&1+k_3\end{pmatrix}\)，其中 \(k_1,k_2,k_3\) 不全为零。 | pending_user_confirmation：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是错误左消 \(A\)，没有转成零空间参数化 | personal_evidence_unadjudicated |
| [LA-065](http://127.0.0.1:8765/open/LA-065) | 占位卡；题面、图像、OCR 与答案均缺失。 | — | null | missing_problem_and_personal_evidence：不可推断。 | unreviewable_missing_personal_and_problem_evidence、missing_question_image_ocr_and_answer |
| [LA-066](http://127.0.0.1:8765/open/LA-066) | 截断的矩阵秩讲义总纲，不是一道具体题。 | — | null | missing_problem_and_personal_evidence：不可推断。 | unreviewable_missing_personal_and_problem_evidence、non_atomic_truncated_outline_misclassified_as_wrong_card |
| [LA-075](http://127.0.0.1:8765/open/LA-075) | 四个含 lambda 的三维向量，求两个三向量组等价时 lambda 的范围。 | 向量组等价、生成空间、矩阵秩、参数退化点 | C，\(\lambda\in\mathbb R,\ \lambda\ne -1,\ \lambda\ne -2\) | pending_user_confirmation：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是只看行列式因子，漏掉特殊参数点是否仍满足等价 | personal_evidence_unadjudicated |
| [LA-076](http://127.0.0.1:8765/open/LA-076) | 线性方程组章节提纲，不是一道具体题。 | — | null | missing_problem_and_personal_evidence：不可推断。 | unreviewable_missing_personal_and_problem_evidence、non_atomic_outline_misclassified_as_wrong_card |
| [LA-077](http://127.0.0.1:8765/open/LA-077) | 截断的线性方程组讲义总纲，不是一道具体题。 | — | null | missing_problem_and_personal_evidence：不可推断。 | unreviewable_missing_personal_and_problem_evidence、non_atomic_truncated_outline_misclassified_as_wrong_card |
| [LA-080](http://127.0.0.1:8765/open/LA-080) | 占位卡；题面、图像、OCR 与答案均缺失。 | — | null | missing_problem_and_personal_evidence：不可推断。 | unreviewable_missing_personal_and_problem_evidence、missing_question_image_ocr_and_answer |
| [LA-082](http://127.0.0.1:8765/open/LA-082) | Vandermonde 型三阶系数矩阵含参数 a、b，右端为 (1,2,4)^T，判断解的情形。 | 含参线性方程组、Vandermonde行列式、增广矩阵秩、参数退化点 | 选 D。若 \(a\ne1,b\ne1,a\ne b\)，则 \(r(A)=r(A,b)=3\)，方程组有唯一解；其余参数情形均有 \(r(A)<r(A,b)\)，方程组无解。 | pending_user_confirmation：候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是套 Vandermonde 非零行列式后漏掉退化参数的增广秩检查 | personal_evidence_unadjudicated |
| [LA-083](http://127.0.0.1:8765/open/LA-083) | 占位卡；题面、图像、OCR 与答案均缺失。 | — | null | missing_problem_and_personal_evidence：不可推断。 | unreviewable_missing_personal_and_problem_evidence、missing_question_image_ocr_and_answer |
| [LA-085](http://127.0.0.1:8765/open/LA-085) | 占位卡；题面、图像、OCR 与答案均缺失。 | — | null | missing_problem_and_personal_evidence：不可推断。 | unreviewable_missing_personal_and_problem_evidence、missing_question_image_ocr_and_answer |

## 逐题复核

### LA-051 强化例题7.1-3

- 题目：三阶 A 满足 det(A)=3、det(A^2+2A)=0、det(2A^2+A)=0，求三个主代数余子式之和；本卡正文在 tr(A*) 处截断。
- 所问：三阶 A 满足 det(A)=3、det(A^2+2A)=0、det(2A^2+A)=0，求三个主代数余子式之和；本卡正文在 tr(A*) 处截断。
- 知识点：—
- 第一动作：先用 det(A) 非零约去 A，把两个矩阵多项式行列式转成特征值 -2 与 -1/2。
- 答案：null
- 个人错因边界：identity_alias_no_independent_event；不适用；不得由 canonical 客观内容反推 LA-051 的个人断点。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 由第三个特征值 3 得主余子式和为两两乘积和 -13/2；与完整重复卡 LA-021 一致，但本卡自身缺原图，故仅条件性核验。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
  - `formal_question_summary_truncated_and_unbalanced_math`：正式卡第 58 行在 tr(A*) 公式中途结束，数学文本不闭合；本卡又没有注册题图。；建议：
  - `duplicate_entity_unresolved`：LA-051 与 LA-021 的题面、答案和第一动作完全相同；当前仍作为两个错题实体并以 related 相连。；建议：
  - `history_counter_inconsistency`：wrong_history 为空且 mistake_count 缺失，但 method_gap.repeat_count=1；无法解释该 1 是首错、导入次数还是复发。；建议：
- 当前快照：`current`；正式卡 `a62b49771a291ecf86d47b9187d0a340389a53f63f45c1f192621d098d3c5b5c`；唯一图片 0 个；物理路径 0 个。

### LA-052 全一矩阵扰动求逆

- 题目：n 阶矩阵主对角为 0、非对角为 1，求逆矩阵。
- 所问：n 阶矩阵主对角为 0、非对角为 1，求逆矩阵。
- 知识点：逆矩阵；全一矩阵；秩一矩阵；矩阵可逆性；参数边界 n>=2
- 第一动作：写 A=J-E，并用 J^2=nJ 构造逆。
- 答案：当 \\(n=1\\) 时不可逆；当 \\(n\\ge 2\\) 时，\\(A^{-1}=\\frac{1}{n-1}J-E\\)。
- 个人错因边界：pending_user_confirmation；候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是按一般矩阵求逆硬算，没有先识别全一矩阵扰动结构
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 乘积恒等式复算正确；题图与正式卡没有明示 n>=2，n=1 时 A 不可逆。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
  - `missing_invertibility_domain_condition`：题面与正式卡没有写 n>=2；当 n=1 时 A=[0] 不可逆，而答案含 1/(n-1)。；建议：
- 关系裁决：
  - LA-012：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-053：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-054：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`stale`；正式卡 `d345a5284b58fe9348d903f2c5515466cfd46ba3a22690a3ad473f6a69031692`；唯一图片 2 个；物理路径 2 个。

### LA-053 矩阵多项式除法求逆

- 题目：A 满足 A^3-2A^2+3A-4E=O，求 (A-E)^{-1}。
- 所问：A 满足 A^3-2A^2+3A-4E=O，求 (A-E)^{-1}。
- 知识点：逆矩阵；矩阵多项式；矩阵多项式因式整理
- 第一动作：将题设多项式按 A-E 除，整理成 (A^2-A+2E)(A-E)=2E。
- 答案：\((A-E)^{-1}=\frac{A^2-A+2E}{2}\)。
- 个人错因边界：pending_user_confirmation；候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是只盯着逆矩阵定义，没有把矩阵多项式关系改写成 \((A-E)Q(A)=cE\)
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 矩阵多项式乘积独立展开正确，且同时证明 A-E 可逆。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
- 关系裁决：
  - LA-052：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-054：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`stale`；正式卡 `131b1f081c1011acf3fd20af83c268b02c643765574a11505ed06655d6c8e27f`；唯一图片 2 个；物理路径 2 个。

### LA-054 幂零矩阵判可逆

- 题目：非零 n 阶 A 满足 A^3=O，判断 E-A 与 E+A 的可逆性。
- 所问：非零 n 阶 A 满足 A^3=O，判断 E-A 与 E+A 的可逆性。
- 知识点：幂零矩阵；有限级数逆矩阵；矩阵可逆性
- 第一动作：把 A 识别为幂零矩阵并写有限级数逆。
- 答案：C
- 个人错因边界：pending_user_confirmation；候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是把可逆性当行列式硬算，没有先识别幂零矩阵的有限级数逆
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - (E-A)^{-1}=E+A+A^2，(E+A)^{-1}=E-A+A^2；结论正确，A 非零对结论无影响。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
- 关系裁决：
  - LA-052：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-053：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`current`；正式卡 `a4d24849b91eaad30a1857ed0c69d372b9fa97081ce08884b3b2948910634063`；唯一图片 2 个；物理路径 2 个。

### LA-056 相似对角化求高次幂

- 题目：已知 P 与 P^{-1}AP=diag(-1,-2,0)，计算 A^99。
- 所问：已知 P 与 P^{-1}AP=diag(-1,-2,0)，计算 A^99。
- 知识点：相似对角化；矩阵高次幂；对角矩阵幂
- 第一动作：写 A^99=P diag((-1)^99,(-2)^99,0) P^{-1}。
- 答案：\(A^{99}=\begin{pmatrix}2^{99}-2&1-2^{99}&2-2^{98}\\2^{100}-2&1-2^{100}&2-2^{99}\\0&0&0\end{pmatrix}\)。
- 个人错因边界：pending_user_confirmation；候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是直接乘 \(A\) 的高次幂，没有把相似关系转成高次幂关系
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 符号矩阵乘法逐项与正式答案完全一致。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
- 关系裁决：
  - LA-061：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-103：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-118：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`stale`；正式卡 `1583742b7f6221a1f77d533ce9c74f1a1cf61c8622c51c3755e8195a7c6a9ff2`；唯一图片 2 个；物理路径 2 个。

### LA-057 低秩分解矩阵幂降维

- 题目：给定四阶 A、4x2 矩阵 B 且 A=BC，求 C 与 A^10。
- 所问：给定四阶 A、4x2 矩阵 B 且 A=BC，求 C 与 A^10。
- 知识点：低秩分解；矩阵高次幂降维；列向量线性表示
- 第一动作：先按列求 C，再写 A^10=B(CB)^9C 将幂降到二阶。
- 答案：见标准答案：\(C=\begin{pmatrix}-1&0&1&2\\2&1&0&-1\end{pmatrix}\)，\(A^{10}\) 如正文矩阵。
- 个人错因边界：pending_user_confirmation；候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是对原阶矩阵硬算高次幂，没有把中间乘积 \(CB\) 降到低维
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 独立核对 BC=A、CB=[[1,0],[2,3]]，并符号验证 B(CB)^9C 与答案逐项一致。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
- 关系裁决：
  - LA-058：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-095：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`stale`；正式卡 `a9537328578b4d82348942722c8ad623f9cdb6ea1199d351408c07feb0c010f8`；唯一图片 2 个；物理路径 2 个。

### LA-058 横拼矩阵秩列空间判断

- 题目：A、B 为 n 阶矩阵，判断横拼分块矩阵的秩恒等式。
- 所问：A、B 为 n 阶矩阵，判断横拼分块矩阵的秩恒等式。
- 知识点：矩阵秩；列空间包含；横拼分块矩阵
- 第一动作：逐列看 AB，确认 Col(AB) 包含于 Col(A)。
- 答案：A
- 个人错因边界：pending_user_confirmation；候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是看到横拼就套公式，没有先验证新增块是否落入原列空间
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 列空间包含直接给出等式；其余选项均无普遍保证。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
- 关系裁决：
  - LA-057：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-059：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`stale`；正式卡 `d998a466b8cac2a2912380315b372f14b7b530f562554450fbcf68c9ca237293`；唯一图片 2 个；物理路径 2 个。

### LA-061 换基表示求矩阵B

- 题目：二阶 A、非特征向量 alpha，P=[alpha,Aalpha]，由 A^2alpha+Aalpha-2alpha=0 求 AP=PB 中的 B。
- 所问：二阶 A、非特征向量 alpha，P=[alpha,Aalpha]，由 A^2alpha+Aalpha-2alpha=0 求 AP=PB 中的 B。
- 知识点：循环基；相似变换；矩阵方程按列读；坐标表示
- 第一动作：写 AP=[Aalpha,A^2alpha] 并在基 [alpha,Aalpha] 中逐列读坐标。
- 答案：\(B=\begin{pmatrix}0&2\\1&-1\end{pmatrix}\)。
- 个人错因边界：pending_user_confirmation；候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是知道换基但没有按列读出坐标列
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 第一列坐标 (0,1)，第二列坐标 (2,-1)，答案正确；本题没有单独解析图。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
- 关系裁决：
  - LA-056：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-062：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-087：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-106：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-116：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`stale`；正式卡 `596a6deed491de1dab2c6e6a2c55605bc55c190fde23dabeba44214993436f41`；唯一图片 1 个；物理路径 1 个。

### LA-062 Jordan链与矩阵平方根

- 题目：把给定三阶幂零 A 相似到 J3(0)，并判断是否存在三阶 B 使 B^2=A。
- 所问：把给定三阶幂零 A 相似到 J3(0)，并判断是否存在三阶 B 使 B^2=A。
- 知识点：Jordan链；幂零矩阵；矩阵平方根存在性；交换矩阵
- 第一动作：第一问按 AP=PJ 构造 Jordan 链；第二问先由 B^2=A 得 AB=BA。
- 答案：\(P=\begin{pmatrix}1&0&0\\0&1&-\frac23\\0&0&\frac13\end{pmatrix}\) 可使 \(P^{-1}AP=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}\)；不存在三阶矩阵 \(B\) 使 \(B^2=A\)。
- 个人错因边界：pending_user_confirmation；候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是只看相似式，没有按列拆出 Jordan 链并连接平方根存在性
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 验证 det(P)=1/3 且 P^{-1}AP=J；将可交换矩阵写成 aE+bJ+cJ^2 后，平方的 J 系数不可能为 1，故无平方根。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
  - `standalone_solution_proof_underexplained`：正式卡对 B^2=A 不存在只写“设元后推出矛盾”，未给出结构方程；离开解析图后证明链不完整。；建议：
- 关系裁决：
  - LA-061：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-064：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-106：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-116：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`stale`；正式卡 `43df022ee6da79aa54211bbcde8c53b4348fb94ac8716a67fce0962833efd8d8`；唯一图片 2 个；物理路径 2 个。

### LA-063 列等价与矩阵方程

- 题目：含参 A 可经初等列变换化为 B，求 a 与所有满足 AP=B 的可逆 P。
- 所问：含参 A 可经初等列变换化为 B，求 a 与所有满足 AP=B 的可逆 P。
- 知识点：列等价；秩不变性；矩阵方程；非齐次方程组通解；可逆性检验
- 第一动作：先用列等价保秩确定 a，再把 AP=B 按列拆。
- 答案：\(a=2\)，且 \(P=\begin{pmatrix}3-6k_1&4-6k_2&4-6k_3\\-1+2k_1&-1+2k_2&-1+2k_3\\k_1&k_2&k_3\end{pmatrix}\)，其中 \(k_2\ne k_3\)。
- 个人错因边界：pending_user_confirmation；候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是跳过列等价保秩的参数条件，直接设 \(P\) 导致方程链混乱
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - det(A) 恒为 0、det(B)=2-a，故 a=2；符号验证参数族满足 AP=B 且 det(P)=k3-k2。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
- 关系裁决：
  - LA-064：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`stale`；正式卡 `5dd082990c34167f3918ca73d16cfcbc832973d4335113745f97b6de2f37c4fc`；唯一图片 2 个；物理路径 2 个。

### LA-064 AB等于A的解空间参数

- 题目：给定秩 2 的三阶 A，求全部非单位 B 使 AB=A。
- 所问：给定秩 2 的三阶 A，求全部非单位 B 使 AB=A。
- 知识点：矩阵方程；零空间；基础解系；解空间参数化
- 第一动作：写 A(B-E)=O，将 B-E 的每列放进 N(A)。
- 答案：存在，\(B=\begin{pmatrix}1+k_1&k_2&k_3\\-k_1&1-k_2&-k_3\\k_1&k_2&1+k_3\end{pmatrix}\)，其中 \(k_1,k_2,k_3\) 不全为零。
- 个人错因边界：pending_user_confirmation；候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是错误左消 \(A\)，没有转成零空间参数化
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 独立验证 r(A)=2、A(1,-1,1)^T=0，参数化完整且排除了 B=E。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
- 关系裁决：
  - LA-062：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-063：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-090：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`stale`；正式卡 `2c62e6f0c6ddefe67d31c8901ab74cfab51beb1f7735ebc0aa8a17f35aabdadf`；唯一图片 2 个；物理路径 2 个。

### LA-065 线代强化第四讲求矩阵的秩

- 题目：占位卡；题面、图像、OCR 与答案均缺失。
- 所问：占位卡；题面、图像、OCR 与答案均缺失。
- 知识点：—
- 第一动作：先回源取得原子题面，当前不能推断方法。
- 答案：null
- 个人错因边界：missing_problem_and_personal_evidence；不可推断。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 不可审题。
- 质量发现：
  - `unreviewable_missing_personal_and_problem_evidence`：没有可确认的原子题面、标准答案和个人作答证据，无法进行数学、方法断点或题间强关系审查。；建议：
  - `missing_question_image_ocr_and_answer`：卡片只是“题干为图片，OCR 待核对”的占位，但当前没有任何注册图片或答案。；建议：
- 当前快照：`current`；正式卡 `60645b882ccacfff17bfad3d71db0be630102223fe7e624751e1abc3aece4225`；唯一图片 0 个；物理路径 0 个。

### LA-066 线代强化第四讲

- 题目：截断的矩阵秩讲义总纲，不是一道具体题。
- 所问：截断的矩阵秩讲义总纲，不是一道具体题。
- 知识点：—
- 第一动作：先回源拆分原子题。
- 答案：null
- 个人错因边界：missing_problem_and_personal_evidence；不可推断。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 正文截断在秩范围公式中，缺问题、条件、答案与个人作答。
- 质量发现：
  - `unreviewable_missing_personal_and_problem_evidence`：没有可确认的原子题面、标准答案和个人作答证据，无法进行数学、方法断点或题间强关系审查。；建议：
  - `non_atomic_truncated_outline_misclassified_as_wrong_card`：正文是矩阵秩总纲并截断于秩范围公式，不是具体题，却仍有复习调度。；建议：
- 当前快照：`current`；正式卡 `ca560659deadbef82ab4b81ccaa22f403674d70fc8b076d7f1f7fb9e883d1000`；唯一图片 0 个；物理路径 0 个。

### LA-075 参数向量组等价判定

- 题目：四个含 lambda 的三维向量，求两个三向量组等价时 lambda 的范围。
- 所问：四个含 lambda 的三维向量，求两个三向量组等价时 lambda 的范围。
- 知识点：向量组等价；生成空间；矩阵秩；参数退化点
- 第一动作：先写生成空间相同的秩条件，再对退化参数逐点回代。
- 答案：C，\(\lambda\in\mathbb R,\ \lambda\ne -1,\ \lambda\ne -2\)
- 个人错因边界：pending_user_confirmation；候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是只看行列式因子，漏掉特殊参数点是否仍满足等价
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 两行列式分别为 (lambda-1)^2(lambda+2) 与 (lambda-1)^2(lambda+1)^2；lambda=1 仍等价，-1、-2 不等价。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
- 关系裁决：
  - LA-093：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-099：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-100：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`stale`；正式卡 `268ab0e110fadb3c5c035942e932726fd22924273b3b89860210815805aafb98`；唯一图片 2 个；物理路径 2 个。

### LA-076 线代强化第五讲-线性方程组

- 题目：线性方程组章节提纲，不是一道具体题。
- 所问：线性方程组章节提纲，不是一道具体题。
- 知识点：—
- 第一动作：先回源拆分原子题。
- 答案：null
- 个人错因边界：missing_problem_and_personal_evidence；不可推断。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 缺具体条件、目标、答案和个人作答。
- 质量发现：
  - `unreviewable_missing_personal_and_problem_evidence`：没有可确认的原子题面、标准答案和个人作答证据，无法进行数学、方法断点或题间强关系审查。；建议：
  - `non_atomic_outline_misclassified_as_wrong_card`：正文只是线性方程组章节目录，没有可作答目标，却仍参与多条 related 关系。；建议：
- 关系裁决：
  - LA-077：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-080：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-083：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`current`；正式卡 `c7d191bc475d58eb33a69b74ced3eaab42a9688550a4446c744dd11e11fd0f0f`；唯一图片 0 个；物理路径 0 个。

### LA-077 线代强化第五讲-线性方程组-2

- 题目：截断的线性方程组讲义总纲，不是一道具体题。
- 所问：截断的线性方程组讲义总纲，不是一道具体题。
- 知识点：—
- 第一动作：先回源拆分原子题。
- 答案：null
- 个人错因边界：missing_problem_and_personal_evidence；不可推断。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 正文截断在齐次解线性组合条件中。
- 质量发现：
  - `unreviewable_missing_personal_and_problem_evidence`：没有可确认的原子题面、标准答案和个人作答证据，无法进行数学、方法断点或题间强关系审查。；建议：
  - `non_atomic_truncated_outline_misclassified_as_wrong_card`：正文是讲义总纲并截断在解的线性组合条件中，不是完整题。；建议：
- 关系裁决：
  - LA-076：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-080：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-083：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`current`；正式卡 `38feecaa7152529325a548627ee2fe0c4a9c9df1be421696864bbfa498a9b95f`；唯一图片 0 个；物理路径 0 个。

### LA-080 强化例题5.1-3

- 题目：占位卡；题面、图像、OCR 与答案均缺失。
- 所问：占位卡；题面、图像、OCR 与答案均缺失。
- 知识点：—
- 第一动作：先回源取得原子题面。
- 答案：null
- 个人错因边界：missing_problem_and_personal_evidence；不可推断。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 不可审题。
- 质量发现：
  - `unreviewable_missing_personal_and_problem_evidence`：没有可确认的原子题面、标准答案和个人作答证据，无法进行数学、方法断点或题间强关系审查。；建议：
  - `missing_question_image_ocr_and_answer`：卡片只是“题干为图片，OCR 待核对”的占位，但当前没有任何注册图片或答案。；建议：
- 关系裁决：
  - LA-076：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-077：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-083：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-085：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-086：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`current`；正式卡 `446f030a323814ac1ac455293ce06981ab8559e1ef947b2d332fb7499e46f91b`；唯一图片 0 个；物理路径 0 个。

### LA-082 Vandermonde方程组解情形

- 题目：Vandermonde 型三阶系数矩阵含参数 a、b，右端为 (1,2,4)^T，判断解的情形。
- 所问：Vandermonde 型三阶系数矩阵含参数 a、b，右端为 (1,2,4)^T，判断解的情形。
- 知识点：含参线性方程组；Vandermonde行列式；增广矩阵秩；参数退化点
- 第一动作：写增广矩阵并分类检查 a=1、b=1、a=b 的退化点。
- 答案：选 D。若 \(a\ne1,b\ne1,a\ne b\)，则 \(r(A)=r(A,b)=3\)，方程组有唯一解；其余参数情形均有 \(r(A)<r(A,b)\)，方程组无解。
- 个人错因边界：pending_user_confirmation；候选复做风险（待确认）：旧卡未记录用户实际漏步；复做风险是套 Vandermonde 非零行列式后漏掉退化参数的增广秩检查
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - det(A)=-(a-1)(a-b)(b-1)；所有退化情形均有 r(A)<r(A,b0)，其余唯一解，无无穷多解。
- 质量发现：
  - `personal_evidence_unadjudicated`：method_gap.evidence_origin 缺失；旧导入或来源解析只能支持客观复做入口，不能证明用户个人断点。；建议：
- 关系裁决：
  - LA-087：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-091：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`current`；正式卡 `fb4e3c67bf88667e1e817fb1a7d3c19a023e6aa0cf24ddd91d78aed31a0bedbc`；唯一图片 2 个；物理路径 2 个。

### LA-083 强化例题5.1-4

- 题目：占位卡；题面、图像、OCR 与答案均缺失。
- 所问：占位卡；题面、图像、OCR 与答案均缺失。
- 知识点：—
- 第一动作：先回源取得原子题面。
- 答案：null
- 个人错因边界：missing_problem_and_personal_evidence；不可推断。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 不可审题。
- 质量发现：
  - `unreviewable_missing_personal_and_problem_evidence`：没有可确认的原子题面、标准答案和个人作答证据，无法进行数学、方法断点或题间强关系审查。；建议：
  - `missing_question_image_ocr_and_answer`：卡片只是“题干为图片，OCR 待核对”的占位，但当前没有任何注册图片或答案。；建议：
- 关系裁决：
  - LA-076：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-077：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-080：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-085：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-086：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`current`；正式卡 `72fbf328a1894d17c518ca9f3fe5362ea6b7243f8f9e886fbab9b202e3fa7bf5`；唯一图片 0 个；物理路径 0 个。

### LA-085 强化例题5.1-5

- 题目：占位卡；题面、图像、OCR 与答案均缺失。
- 所问：占位卡；题面、图像、OCR 与答案均缺失。
- 知识点：—
- 第一动作：先回源取得原子题面。
- 答案：null
- 个人错因边界：missing_problem_and_personal_evidence；不可推断。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 不可审题。
- 质量发现：
  - `unreviewable_missing_personal_and_problem_evidence`：没有可确认的原子题面、标准答案和个人作答证据，无法进行数学、方法断点或题间强关系审查。；建议：
  - `missing_question_image_ocr_and_answer`：卡片只是“题干为图片，OCR 待核对”的占位，但当前没有任何注册图片或答案。；建议：
- 关系裁决：
  - LA-080：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-083：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
  - LA-086：`remove`；The pair does not satisfy the strict shared personal-breakpoint gate.
- 当前快照：`current`；正式卡 `40efdc1594b8a33cc865e683ad9bbe5da391b41b3716b3ff001f3a14112c5881`；唯一图片 0 个；物理路径 0 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
