---
wiki_id: MATHWIKI-REVIEW-032
type: target_level_semantic_review_batch
title: 全库逐题语义复核第13批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-032_全库逐题语义复核第13批20题.json
status: active
last_updated: 2026-07-23
---

# 全库逐题语义复核第13批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 5 张；覆盖 22 个物理图片路径与 22 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 20 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `MATH-TARGET-SEMANTIC-CLOSEOUT-20260723-B13`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-082](http://127.0.0.1:8765/open/GS-082) | 判断二次泰勒多项式中 a、b、c 的值。 | 一元函数泰勒公式、二阶泰勒多项式、导数值与展开系数对应 | B，\(a=1,\ b=1,\ c=\frac12\)。 | confirmed_personal：已确认的个人第一断点是导数值与泰勒系数混淆：虽然正确得到 \(f''(0)=1\)，却写成 \(c=1\)；二次项系数实际是 \(c=f''(0)/2!\)。 | factorial_coefficient_boundary_verified |
| [GS-083](http://127.0.0.1:8765/open/GS-083) | 求连续补点值 a，并写出 g(x) 到三阶的 Peano 展开。 | 牛顿莱布尼茨公式、导函数与原函数增量、佩亚诺余项逐项积分、倒数型泰勒展开 | \(a=1\)，且 \(g(x)=1-\frac{x^2}{3}-\frac{x^3}{4}+o(x^3)\)。 | confirmed_personal：已确认的个人第一断点是动作链缺失：已知的是 \(f'(x)\) 的局部展开，却没有先写 \(f(x)-f(0)=\int_0^x f'(t)\,dt\)，导致后续对 \(g(x)\) 的展开失去依据。 | derivative_series_integral_chain_verified |
| [GS-084](http://127.0.0.1:8765/open/GS-084) | 求连续补点值 a，并判断可导性、写出 f'(x)。 | 分段函数连续性、点处导数定义、二阶泰勒展开、二阶主导项、商法则 | \(a=0\)；\(x\ne0\) 时 \(f'(x)=\frac{x(g'(x)+e^{-x})-(g(x)-e^{-x})}{x^2}\)，\(x=0\) 时 \(f'(0)=\frac{g''(0)-1}{2}\)。 | confirmed_personal：已确认的个人第一断点是把点值条件当成函数恒等式；随后又没有识别 \(g(x)\) 与 \(e^{-x}\) 的常数项、一次项全部抵消，因而漏掉决定连续值和点处导数的二阶主导项。 | second_order_cancellation_and_identity_block_verified |
| [GS-085](http://127.0.0.1:8765/open/GS-085) | 由给定复合极限求 f'(1)。 | 点处可导的一阶展开、复合自变量真实增量、有限极限与常数项消失、等价无穷小 | \(f'(1)=-\frac47\)。 | pending_user_confirmation：个人原始错因未记录。题图与解析只能确认候选复做入口：两个复合自变量都趋近 1，应先写各自真实增量，并先由极限有限检查常数项是否迫使 \(f(1)=0\)。 | compound_increment_chain_verified |
| [GS-086](http://127.0.0.1:8765/open/GS-086) | 从四个选项中选出与 y(x) 等价的无穷小。 | 二阶常系数线性微分方程、初值条件与局部导数、泰勒公式、等价无穷小 | D，\(y(x)\sim\ln\sqrt{1+x^2}\)。 | confirmed_personal：已确认的个人第一断点是目标识别偏离：题目只要求解在零点附近的等价无穷小，却选择完整求解微分方程；应先把 \(x=0\) 和初值代入方程，求最低非零阶导数。 | local_goal_method_repaired |
| [GS-087](http://127.0.0.1:8765/open/GS-087) | 判断四个命题的真假并给出真命题个数。 | 点处导数定义、连续性确定函数值、无穷小阶数比较、极限条件反推可导 | A，只有命题2为真，真命题个数为1。 | pending_user_confirmation：个人原始错因未记录。题图与解析只能确认候选复做入口：先把每个命题转回 \(f'(0)=\lim_{x\to0}[f(x)-f(0)]/x\)，再检查条件能否推出 \(f(0)=0\)，以及分母阶数是否足以控制差商。 | solution_image_counterexample_normalized |
| [GS-088](http://127.0.0.1:8765/open/GS-088) | 计算函数增量与微分之差除以自变量增量的极限。 | 可导的等价定义、函数增量与微分、一阶线性主部、高阶小量 | D，0。 | pending_user_confirmation：个人原始错因未记录。题图与解析只能确认候选复做入口：由可导定义把函数增量拆成一阶线性主部与高阶小量，再识别 \(\Delta f-df=o(\Delta x)\)。 | differential_error_definition_verified |
| [GS-089](http://127.0.0.1:8765/open/GS-089) | 计算两侧函数值之差除以 sin(1/n) 的数列极限。 | 导数定义、数列极限、等价无穷小、函数增量分解 | $\displaystyle 2f'(x_0)$。 | pending_user_confirmation：个人原始作答未独立留存；当前只确认复做入口是先加减 $f(x_0)$，把两段函数差分别配成导数定义差商，再处理真实增量与外层分母的比例。该入口是否为当时第一断点仍待复做确认。 | dual_increment_chain_verified |
| [GS-090](http://127.0.0.1:8765/open/GS-090) | 用 f'(0) 与参数 t 表示极限。 | 导数定义、奇函数、复合自变量差商、真实增量 | $(t-5)f'(0)$。 | confirmed_personal：视觉详情明确记录：曾把第一项直接当作以 $x$ 为分母的导数差商，漏掉 $f(tx)-f(0)$ 应先除以 $tx$ 再外乘 $t$，因此算成了 $-4f'(0)$。 | missing_outer_scale_factor_restored |
| [GS-091](http://127.0.0.1:8765/open/GS-091) | 判断 f 在 x0 处是否可导并求 f'(x0)。 | 导数定义、函数方程、平移关系、基点导数搬运 | A；$f$ 在 $x_0$ 处可导，且 $f'(x_0)=\alpha\beta$。 | confirmed_personal：两次记录共同指向：虽然能写出 $x_0$ 处导数定义，但没有先在函数关系中代入 $x=0$ 得到 $f(x_0)=\alpha f(0)$，也没有把 $x_0$ 处差商搬回 0 点差商。 | repeat_count_and_basepoint_transport_repaired |
| [GS-092](http://127.0.0.1:8765/open/GS-092) | 判断 F(x)=g(f(x)) 在 x=0 处的连续、可导性质。 | 导数定义、复合函数可导性、链式法则、可导展开 | B；$F$ 在 $x=0$ 处可导，且 $F'(0)=0$。 | confirmed_personal：既有记录指出未调取复合函数在点处可导的链式法则入口。现有旧解析把差商除以 $f(x)-f(0)$，但本题该量在趋近 0 的无穷多个点上为 0；正式证明改用可导余项表示，避免非法除法。 | illegal_division_removed_and_identity_hold |
| [GS-093](http://127.0.0.1:8765/open/GS-093) | 求分段函数 g'(x)，并讨论 g' 在零点的连续性。 | 分段函数、导数定义、二阶连续可导、导函数连续性 | $g'(x)=\begin{cases}\dfrac{x f'(x)-f(x)}{x^2},&x\ne0,\\[4pt]\dfrac12f''(0),&x=0,\end{cases}$ 且 $g'$ 在 $x=0$ 处连续。 | confirmed_personal：2026-06-01 的用户粘贴错因表明：曾把 $x\ne0$ 时由商法则得到的导函数公式直接用于分段点 $x=0$，没有回到补点处导数定义，因而把 $g'(0)$ 误算成 $f''(0)$，漏掉系数 $1/2$。 | piecewise_point_derivative_and_identity_hold |
| [GS-094](http://127.0.0.1:8765/open/GS-094) | 求 f'(-1)。 | 函数奇偶性与导数性质、商法则、ln绝对值求导、点导数 | $f'(-1)=-\dfrac12$。 | pending_user_confirmation：旧视觉解析只记录“没有想到利用函数等式或导数定义”，未保存个人原始作答过程。当前可确认的复做入口是先识别 $f$ 为偶函数，从而 $f'$ 为奇函数，再把负点导数转到 $x=1$ 计算；是否为当时第一断点待复做确认。 | parity_transfer_chain_verified |
| [GS-096](http://127.0.0.1:8765/open/GS-096) | 计算 n[x(1/n)-1] 的极限。 | 一元函数微分学应用、导数定义、数列极限、变上限积分、隐函数求导、复合函数求导、定积分 | \(\boxed{3}\) | confirmed_personal：复做时没有先求 \(x(0)=1\) 并把 \(n[x(1/n)-1]\) 改写成导数定义差商，而是把隐式方程右端的积分误当作 \(x(1/n)\) 本身；随后又把 \(x(y)\) 误读为乘积 \(xy\)，没有明确 \(y\) 是自变量、\(x\) 是 \(y\) 的函数，应对整个隐式方程关于 \(y\) 求导，并对上限 \(x(y)-y\) 补乘 \(x'(y)-1\)。 | implicit_variable_roles_and_relation_scope_repaired |
| [GS-097](http://127.0.0.1:8765/open/GS-097) | 求使 f 的 n 阶导数在零点存在的最大阶数 n。 | 一元函数微分学应用、导数定义、绝对值分段、高阶导数、Taylor 主项 | 选 B；最高阶数为 2。\(f'(0)=f''(0)=0\)，而 \(f'''(0)\) 不存在。 | pending_user_confirmation：旧批量导入未记录用户个人错点；当前只能确认复做入口：把 \(f(x)=\|x\|\sin^2x\) 在 \(x>0\) 与 \(x<0\) 分段，逐阶比较 \(x=0\) 处的左右导数。是否正是原始第一断点，仍待复做确认。 | highest_differentiability_order_verified |
| [GS-098](http://127.0.0.1:8765/open/GS-098) | 判断 x=2 是否为驻点以及局部极值类型。 | 一元函数微分学应用、导数定义、无穷小阶数比较、极值判定 | 选 C；x=2 是驻点且为局部极小值点。 | pending_user_confirmation：个人原始错因未记录；本轮依据题图与解析确认复做入口：把对数极限先转成 f(2+h) 与 h^2 的等价关系，再同时推出 f(2)=0、f'(2)=0 和局部极小。 | second_order_local_sign_chain_verified |
| [GS-099](http://127.0.0.1:8765/open/GS-099) | 由给定复合极限求 f'(1)。 | 导数定义、导数定义型极限、复合自变量、自变量增量、极限条件反推导数 | \(\displaystyle f'(1)=-1\) | pending_user_confirmation：暂无明确个人错因。可确认的题型风险是：看到含 \(f(e^{x^2})\)、\(f(1+\sin^2 x)\) 的极限条件时，容易只盯 \(e^{x^2}\) 和 \(\sin^2 x\) 的等价无穷小，而漏掉先由极限有限推出 \(f(1)=0\)，再把两项分别拆成 \(1\) 点导数定义差商。 | question_solution_image_cross_checked |
| [GS-100](http://127.0.0.1:8765/open/GS-100) | 求 f'(a)，并说明绝对值零点处的左右导数理由。 | 一元函数微分学应用、导数定义、绝对值分类、极限与连续 | \(f'(a)=0\) | confirmed_personal：再次忽略绝对值函数在零点处可导的核心限制：若 \(f(a)=0\)，则判断 \(\|f(x)\|\) 在 \(x=a\) 处可导时，必须分别看左右导数；左导数为 \(-\|f'(a)\|\)，右导数为 \(\|f'(a)\|\)，两者相等只能推出 \(f'(a)=0\)。 | repeat_count_and_one_sided_derivatives_verified |
| [GS-101](http://127.0.0.1:8765/open/GS-101) | 选择使 \|f\| 在 a 处不可导的充要条件。 | 一元函数微分学应用、可导性判定、导数定义、分段函数 | 选 B；充要条件是 f(a)=0 且 f'(a)≠0。 | pending_user_confirmation：个人原始错因未记录；本轮依据题图与解析确认复做入口：判断 \|f(x)\| 在 a 处不可导时，先分类看 f(a) 是否为 0，再检查 f'(a) 是否非零形成穿零尖点。 | absolute_value_differentiability_iff_repaired |
| [GS-102](http://127.0.0.1:8765/open/GS-102) | 判断四个条件中有多少个能推出 f 在零点可导。 | 一元函数微分学应用、可导性判定、导数定义、绝对值函数、局部保号性、双侧极限 | 选 D；四个条件都能推出 f 在 x=0 处可导。 | pending_user_confirmation：个人原始错因未记录；旧卡把原题误读成含 f(\|x\|) 的单侧信息题。本批按题图恢复为四个绝对值差商条件。可确认复做入口是：每项先用有限极限消去常数项，再按 f(0) 的符号分类并回到导数定义；是否为用户原始断点仍待复做确认。 | misread_absolute_value_and_wrong_answer_repaired |

## 逐题复核

### GS-082 1000题B组1.33 2026.5.29

- 题目：一元二阶泰勒多项式系数匹配
- 所问：判断二次泰勒多项式中 a、b、c 的值。
- 知识点：一元函数泰勒公式；二阶泰勒多项式；导数值与展开系数对应
- 第一动作：先写 \(f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+o(x^2)\)。
- 答案：B，\(a=1,\ b=1,\ c=\frac12\)。
- 个人错因边界：confirmed_personal；已确认的个人第一断点是导数值与泰勒系数混淆：虽然正确得到 \(f''(0)=1\)，却写成 \(c=1\)；二次项系数实际是 \(c=f''(0)/2!\)。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 根式恒等变形
  - 二项式展开
  - 按目标阶截断
  - 系数匹配
- 质量发现：
  - `factorial_coefficient_boundary_verified`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-455：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-658：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
- 当前快照：`stale`；正式卡 `fe87f5ce149e217b90e05eac03725d63fd384fc64b1914d1055968cc6bbd0b64`；唯一图片 1 个；物理路径 1 个。

### GS-083 1000题B组1.38

- 题目：导函数局部展开逐项积分还原原函数
- 所问：求连续补点值 a，并写出 g(x) 到三阶的 Peano 展开。
- 知识点：牛顿莱布尼茨公式；导函数与原函数增量；佩亚诺余项逐项积分；倒数型泰勒展开
- 第一动作：先写 \(f(x)-f(0)=\int_0^x f'(t)\,dt\)。
- 答案：\(a=1\)，且 \(g(x)=1-\frac{x^2}{3}-\frac{x^3}{4}+o(x^3)\)。
- 个人错因边界：confirmed_personal；已确认的个人第一断点是动作链缺失：已知的是 \(f'(x)\) 的局部展开，却没有先写 \(f(x)-f(0)=\int_0^x f'(t)\,dt\)，导致后续对 \(g(x)\) 的展开失去依据。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 逐项积分还原原函数增量
  - 提取一次主项
  - 倒数展开
  - 按目标阶保留余项
- 质量发现：
  - `derivative_series_integral_chain_verified`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-157：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-283：`remove_broad_stale_or_identity_ambiguous_edge`；
- 当前快照：`stale`；正式卡 `0e8c238e2c7a4a3feeab947c7027300403ecbb197092a81b99969507372dc056`；唯一图片 1 个；物理路径 1 个。

### GS-084 1000题B组3.10

- 题目：分段商函数连续可导与二阶主导项
- 所问：求连续补点值 a，并判断可导性、写出 f'(x)。
- 知识点：分段函数连续性；点处导数定义；二阶泰勒展开；二阶主导项；商法则
- 第一动作：先写 \(g(x)=1-x+\frac12g''(0)x^2+o(x^2)\) 与 \(e^{-x}=1-x+\frac12x^2+o(x^2)\)。
- 答案：\(a=0\)；\(x\ne0\) 时 \(f'(x)=\frac{x(g'(x)+e^{-x})-(g(x)-e^{-x})}{x^2}\)，\(x=0\) 时 \(f'(0)=\frac{g''(0)-1}{2}\)。
- 个人错因边界：confirmed_personal；已确认的个人第一断点是把点值条件当成函数恒等式；随后又没有识别 \(g(x)\) 与 \(e^{-x}\) 的常数项、一次项全部抵消，因而漏掉决定连续值和点处导数的二阶主导项。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 二阶泰勒展开
  - 分段点回到导数定义
  - 非分段点使用商法则
  - 主导项比较
- 质量发现：
  - `second_order_cancellation_and_identity_block_verified`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-103：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-127：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-540：`remove_broad_stale_or_identity_ambiguous_edge`；
  - ：`block_candidate_edge_until_GS-093_GS-108_identity_resolution`；
- 当前快照：`stale`；正式卡 `8659feb376a5baed2d1a4932cbac6fadc81a608d44aa18406c6391e8b9ee494a`；唯一图片 1 个；物理路径 1 个。

### GS-085 1000题B组3.20

- 题目：复合自变量一阶展开反求点处导数
- 所问：由给定复合极限求 f'(1)。
- 知识点：点处可导的一阶展开；复合自变量真实增量；有限极限与常数项消失；等价无穷小
- 第一动作：先设 \(\Delta_1=\cos x-1,\ \Delta_2=\sin^2x\)，并写 \(f(1+\Delta)=f(1)+f'(1)\Delta+o(\Delta)\)。
- 答案：\(f'(1)=-\frac47\)。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录。题图与解析只能确认候选复做入口：两个复合自变量都趋近 1，应先写各自真实增量，并先由极限有限检查常数项是否迫使 \(f(1)=0\)。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 设置真实自变量增量
  - 一阶可导展开
  - 有限极限反推基点函数值
  - 同阶系数比较
- 质量发现：
  - `compound_increment_chain_verified`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-099：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `9075616cf6c0626013d32c0ddddf8ef618d5e8d68b3fdb6e0184a4ce7df46475`；唯一图片 1 个；物理路径 1 个。

### GS-086 57964 2026.4.28

- 题目：微分方程初值的局部泰勒主项与等价无穷小
- 所问：从四个选项中选出与 y(x) 等价的无穷小。
- 知识点：二阶常系数线性微分方程；初值条件与局部导数；泰勒公式；等价无穷小
- 第一动作：先把 \(x=0,\ y(0)=0,\ y'(0)=0\) 代入方程求 \(y''(0)\)。
- 答案：D，\(y(x)\sim\ln\sqrt{1+x^2}\)。
- 个人错因边界：confirmed_personal；已确认的个人第一断点是目标识别偏离：题目只要求解在零点附近的等价无穷小，却选择完整求解微分方程；应先把 \(x=0\) 和初值代入方程，求最低非零阶导数。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 方程代点求低阶导数
  - 泰勒主项
  - 等价无穷小比较
  - 选项量级比较
- 质量发现：
  - `local_goal_method_repaired`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 当前快照：`stale`；正式卡 `77f5a81d668aea71cc1ba297470216c5f5e37b8cb46622211ac1788580b2e7e4`；唯一图片 1 个；物理路径 1 个。

### GS-087 强化例题3.2 极限量级判可导

- 题目：极限量级条件与点处可导性命题判断
- 所问：判断四个命题的真假并给出真命题个数。
- 知识点：点处导数定义；连续性确定函数值；无穷小阶数比较；极限条件反推可导
- 第一动作：先写 \(f'(0)=\lim_{x\to0}\frac{f(x)-f(0)}x\)，逐项核查 \(f(0)\) 与阶数。
- 答案：A，只有命题2为真，真命题个数为1。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录。题图与解析只能确认候选复做入口：先把每个命题转回 \(f'(0)=\lim_{x\to0}[f(x)-f(0)]/x\)，再检查条件能否推出 \(f(0)=0\)，以及分母阶数是否足以控制差商。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 导数定义
  - 连续性定点
  - 极限量级换算
  - 反例排除
- 质量发现：
  - `solution_image_counterexample_normalized`：解析图结论正确，但反例行把一个实际趋于 0 的比值写成无穷；正式文字解已用同一有效反例重写极限并保留不可导结论。；建议：
- 关系裁决：
  - GS-091：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-093：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-104：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-458：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-099：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
- 当前快照：`stale`；正式卡 `5bdd985b38fcdc60096cd3acbfe403c7de4614c0b9cf2dd5284f5fc13a1122c3`；唯一图片 2 个；物理路径 2 个。

### GS-088 1000题A组3.9

- 题目：可导定义中的函数增量与微分误差
- 所问：计算函数增量与微分之差除以自变量增量的极限。
- 知识点：可导的等价定义；函数增量与微分；一阶线性主部；高阶小量
- 第一动作：先写 \(f(1+\Delta x)-f(1)=f'(1)\Delta x+o(\Delta x)\)，再代入 \(df(1)=f'(1)\Delta x\)。
- 答案：D，0。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录。题图与解析只能确认候选复做入口：由可导定义把函数增量拆成一阶线性主部与高阶小量，再识别 \(\Delta f-df=o(\Delta x)\)。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 可导定义
  - 一阶线性主部
  - 高阶小量消去
- 质量发现：
  - `differential_error_definition_verified`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-626：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `9d4bf208d5b90004d8a5839d76b98cfc9e008121ae124a0cf3e1cdc847344517`；唯一图片 1 个；物理路径 1 个。

### GS-089 1000题A组3.12

- 题目：两侧增量拆分的导数定义型数列极限
- 所问：计算两侧函数值之差除以 sin(1/n) 的数列极限。
- 知识点：导数定义；数列极限；等价无穷小；函数增量分解
- 第一动作：先在分子中加减 $f(x_0)$。
- 答案：$\displaystyle 2f'(x_0)$。
- 个人错因边界：pending_user_confirmation；个人原始作答未独立留存；当前只确认复做入口是先加减 $f(x_0)$，把两段函数差分别配成导数定义差商，再处理真实增量与外层分母的比例。该入口是否为当时第一断点仍待复做确认。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 加减中间项
  - 导数定义
  - 真实增量匹配
  - 等价无穷小
- 质量发现：
  - `dual_increment_chain_verified`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-458：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `b1652dbaed7d4ccb630e9b4ac71c2380c5e5e0dc6c307581bcbbc975a0e68f04`；唯一图片 1 个；物理路径 1 个。

### GS-090 1000题A组3.13

- 题目：复合自变量真实增量匹配的导数定义极限
- 所问：用 f'(0) 与参数 t 表示极限。
- 知识点：导数定义；奇函数；复合自变量差商；真实增量
- 第一动作：先由奇函数写 $f(0)=0$，再把第一项改写为以 $tx$ 为分母的差商。
- 答案：$(t-5)f'(0)$。
- 个人错因边界：confirmed_personal；视觉详情明确记录：曾把第一项直接当作以 $x$ 为分母的导数差商，漏掉 $f(tx)-f(0)$ 应先除以 $tx$ 再外乘 $t$，因此算成了 $-4f'(0)$。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 奇函数推出零点函数值
  - 导数定义
  - 真实增量匹配
  - 外层系数补偿
- 质量发现：
  - `missing_outer_scale_factor_restored`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-121：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-458：`add_strong_edge`；
- 当前快照：`current`；正式卡 `a0da87e4e3f3a7cbd7904df08c0d02e5f362252130c39e67a88388a3dfeeddbb`；唯一图片 1 个；物理路径 1 个。

### GS-091 1000题B组3.2

- 题目：函数方程搬运基点导数
- 所问：判断 f 在 x0 处是否可导并求 f'(x0)。
- 知识点：导数定义；函数方程；平移关系；基点导数搬运
- 第一动作：先令 $x=0$，得到 $f(x_0)=\alpha f(0)$。
- 答案：A；$f$ 在 $x_0$ 处可导，且 $f'(x_0)=\alpha\beta$。
- 个人错因边界：confirmed_personal；两次记录共同指向：虽然能写出 $x_0$ 处导数定义，但没有先在函数关系中代入 $x=0$ 得到 $f(x_0)=\alpha f(0)$，也没有把 $x_0$ 处差商搬回 0 点差商。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 特殊值代入
  - 导数定义
  - 函数关系代换
  - 基点差商搬运
- 质量发现：
  - `repeat_count_and_basepoint_transport_repaired`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-091：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-092：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-099：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-104：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-452：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-453：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-456：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-458：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-463：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-530：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-471：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
- 当前快照：`current`；正式卡 `5650dcfeb88f537057d37a6f0693c951490f0fba9fefd684338f145281740166`；唯一图片 1 个；物理路径 1 个。

### GS-092 1000题B组3.5

- 题目：复合函数在分段点的可导性
- 所问：判断 F(x)=g(f(x)) 在 x=0 处的连续、可导性质。
- 知识点：导数定义；复合函数可导性；链式法则；可导展开
- 第一动作：先由定义计算 $f'(0)=0$。
- 答案：B；$F$ 在 $x=0$ 处可导，且 $F'(0)=0$。
- 个人错因边界：confirmed_personal；既有记录指出未调取复合函数在点处可导的链式法则入口。现有旧解析把差商除以 $f(x)-f(0)$，但本题该量在趋近 0 的无穷多个点上为 0；正式证明改用可导余项表示，避免非法除法。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先求内层点导数
  - 链式法则
  - 可导余项表示
  - 避免除以可能为零的内层增量
- 质量发现：
  - `illegal_division_removed_and_identity_hold`：旧解析把可能在无穷多个点为零的内层增量放入分母；正式证明已改用外层函数的可导余项，并对 GS-092/GS-107 保持身份待裁决。；建议：
- 关系裁决：
  - GS-092：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-447：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-453：`remove_broad_stale_or_identity_ambiguous_edge`；
  - ：`hold_without_merge_delete_or_aggregate_edge`；
- 当前快照：`current`；正式卡 `c3000f14f883ef1245f14b36aa951abe142486f6756a028d5d7d0eca53aa3e18`；唯一图片 1 个；物理路径 1 个。

### GS-093 1000题B组3.11

- 题目：去心商补点求导与导函数连续性
- 所问：求分段函数 g'(x)，并讨论 g' 在零点的连续性。
- 知识点：分段函数；导数定义；二阶连续可导；导函数连续性
- 第一动作：先把 $x\ne0$ 与 $x=0$ 两种情形分开。
- 答案：$g'(x)=\begin{cases}\dfrac{x f'(x)-f(x)}{x^2},&x\ne0,\\[4pt]\dfrac12f''(0),&x=0,\end{cases}$ 且 $g'$ 在 $x=0$ 处连续。
- 个人错因边界：confirmed_personal；2026-06-01 的用户粘贴错因表明：曾把 $x\ne0$ 时由商法则得到的导函数公式直接用于分段点 $x=0$，没有回到补点处导数定义，因而把 $g'(0)$ 误算成 $f''(0)$，漏掉系数 $1/2$。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 去心点商法则
  - 补点处导数定义
  - 二阶泰勒展开
  - 导函数连续性检查
- 质量发现：
  - `piecewise_point_derivative_and_identity_hold`：去心商法则只用于非零点；零点已回到导数定义并恢复二分之一系数，同时对 GS-093/GS-108 保持身份待裁决。；建议：
- 关系裁决：
  - GS-093：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-108：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-127：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-448：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-470：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-472：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-507：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-523：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-540：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-639：`remove_broad_stale_or_identity_ambiguous_edge`；
  - ：`hold_without_merge_delete_or_aggregate_edge`；
- 当前快照：`current`；正式卡 `ec13e41d0b05649c0a134a31a9c4211f8979558357ba686bae473aa603a7f8e9`；唯一图片 1 个；物理路径 1 个。

### GS-094 1000题B组3.18

- 题目：偶函数的导函数奇偶性与负点求导
- 所问：求 f'(-1)。
- 知识点：函数奇偶性与导数性质；商法则；ln绝对值求导；点导数
- 第一动作：先观察分子、分母都是偶函数，确认 $f$ 为偶函数。
- 答案：$f'(-1)=-\dfrac12$。
- 个人错因边界：pending_user_confirmation；旧视觉解析只记录“没有想到利用函数等式或导数定义”，未保存个人原始作答过程。当前可确认的复做入口是先识别 $f$ 为偶函数，从而 $f'$ 为奇函数，再把负点导数转到 $x=1$ 计算；是否为当时第一断点待复做确认。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先判函数奇偶性
  - 导函数奇偶性
  - 商法则
  - 整体等式求导
- 质量发现：
  - `parity_transfer_chain_verified`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-096：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-449：`add_strong_edge`；
- 当前快照：`current`；正式卡 `9879c69163c6f7089bfac2b895c0dc2fb228d7e82ee7b489b0534aadfcd249dc`；唯一图片 1 个；物理路径 1 个。

### GS-096 1000题B组4.10

- 题目：数列极限凑导数定义与隐式变上限积分求导
- 所问：计算 n[x(1/n)-1] 的极限。
- 知识点：一元函数微分学应用；导数定义；数列极限；变上限积分；隐函数求导；复合函数求导；定积分
- 第一动作：先令 \(y=0\) 求 \(x(0)=1\)，再把极限改写成 \(x'(0)\)
- 答案：\(\boxed{3}\)
- 个人错因边界：confirmed_personal；复做时没有先求 \(x(0)=1\) 并把 \(n[x(1/n)-1]\) 改写成导数定义差商，而是把隐式方程右端的积分误当作 \(x(1/n)\) 本身；随后又把 \(x(y)\) 误读为乘积 \(xy\)，没有明确 \(y\) 是自变量、\(x\) 是 \(y\) 的函数，应对整个隐式方程关于 \(y\) 求导，并对上限 \(x(y)-y\) 补乘 \(x'(y)-1\)。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 导数定义
  - 条件转化
  - 隐函数求导
  - 变上限积分求导
  - 链式法则
- 质量发现：
  - `implicit_variable_roles_and_relation_scope_repaired`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-096：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-453：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
- 当前快照：`stale`；正式卡 `53c1d53829a386dffeb2eccf242716edf08388cf34425b542302e889791738cf`；唯一图片 1 个；物理路径 1 个。

### GS-097 1000题B组4.16

- 题目：含绝对值函数在零点的最高可导阶数
- 所问：求使 f 的 n 阶导数在零点存在的最大阶数 n。
- 知识点：一元函数微分学应用；导数定义；绝对值分段；高阶导数；Taylor 主项
- 第一动作：先写 x>0 时主项为 x³、x<0 时主项为 -x³，再判断各阶导数在 0 点的左右一致性
- 答案：选 B；最高阶数为 2。\(f'(0)=f''(0)=0\)，而 \(f'''(0)\) 不存在。
- 个人错因边界：pending_user_confirmation；旧批量导入未记录用户个人错点；当前只能确认复做入口：把 \(f(x)=|x|\sin^2x\) 在 \(x>0\) 与 \(x<0\) 分段，逐阶比较 \(x=0\) 处的左右导数。是否正是原始第一断点，仍待复做确认。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 分类讨论
  - 左右导数
  - 逐阶求导
  - Taylor 主项比较
- 质量发现：
  - `highest_differentiability_order_verified`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-100：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-287：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-447：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-035：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-461：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `263fcd9748f533823da745ea1e5f95ce43a939aed5070f930fc5f9c0c5bfd848`；唯一图片 1 个；物理路径 1 个。

### GS-098 1000题B组5.38

- 题目：对数极限反推驻点与极值
- 所问：判断 x=2 是否为驻点以及局部极值类型。
- 知识点：一元函数微分学应用；导数定义；无穷小阶数比较；极值判定
- 第一动作：先由有限极限推出对数真数趋于 1，得到 f(2)=0；再把 ln(1+u)、1-cos x 和 e^(x²)-1 同阶化简
- 答案：选 C；x=2 是驻点且为局部极小值点。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；本轮依据题图与解析确认复做入口：把对数极限先转成 f(2+h) 与 h^2 的等价关系，再同时推出 f(2)=0、f'(2)=0 和局部极小。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 对数极限转等价无穷小
  - 由二阶小量反推函数值与导数
  - 局部符号判极值
- 质量发现：
  - `second_order_local_sign_chain_verified`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-507：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
- 当前快照：`stale`；正式卡 `933168019682ef7ef654bdfddf38e705bc7098556c7faba271a5d53b9b992f6a`；唯一图片 1 个；物理路径 1 个。

### GS-099 2022年第17题 导数定义型极限反推导数

- 题目：导数定义型极限反推导数
- 所问：由给定复合极限求 f'(1)。
- 知识点：导数定义；导数定义型极限；复合自变量；自变量增量；极限条件反推导数
- 第一动作：先令 x 趋近 0 检查分子常数项，利用连续性推出 f(1)=0
- 答案：\(\displaystyle f'(1)=-1\)
- 个人错因边界：pending_user_confirmation；暂无明确个人错因。可确认的题型风险是：看到含 \(f(e^{x^2})\)、\(f(1+\sin^2 x)\) 的极限条件时，容易只盯 \(e^{x^2}\) 和 \(\sin^2 x\) 的等价无穷小，而漏掉先由极限有限推出 \(f(1)=0\)，再把两项分别拆成 \(1\) 点导数定义差商。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 导数定义
  - 导数定义拆差商
  - 条件转化
  - 增量匹配
  - 加减同项
  - 一阶展开
  - 等价无穷小
- 质量发现：
  - `question_solution_image_cross_checked`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-099：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-530：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-099：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-458：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-099：`add_strong_edge`；
  - GS-002：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
- 当前快照：`stale`；正式卡 `3f5a1367a7698e903e7c4cccb1d49b742e0b666e1ed453140762ccb58445aa26`；唯一图片 2 个；物理路径 2 个。

### GS-100 1000题B组3.9

- 题目：绝对值函数可导性判定
- 所问：求 f'(a)，并说明绝对值零点处的左右导数理由。
- 知识点：一元函数微分学应用；导数定义；绝对值分类；极限与连续
- 第一动作：先分别计算 \(|f(x)|\) 在 \(x=a\) 的右导数 \(|f'(a)|\) 和左导数 \(-|f'(a)|\)
- 答案：\(f'(a)=0\)
- 个人错因边界：confirmed_personal；再次忽略绝对值函数在零点处可导的核心限制：若 \(f(a)=0\)，则判断 \(|f(x)|\) 在 \(x=a\) 处可导时，必须分别看左右导数；左导数为 \(-|f'(a)|\)，右导数为 \(|f'(a)|\)，两者相等只能推出 \(f'(a)=0\)。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 导数定义
  - 分类讨论
  - 左右导数
- 质量发现：
  - `repeat_count_and_one_sided_derivatives_verified`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-100：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-104：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-447：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-448：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-461：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-466：`remove_broad_stale_or_identity_ambiguous_edge`；
  - GS-035：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-101：`add_strong_edge`；
  - GS-102：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `6b19c7be917b80f71f2100943c491bf846db69a6965a8b603948f31a7e081175`；唯一图片 1 个；物理路径 1 个。

### GS-101 1000题B组3.13

- 题目：绝对值复合函数可导性判定
- 所问：选择使 |f| 在 a 处不可导的充要条件。
- 知识点：一元函数微分学应用；可导性判定；导数定义；分段函数
- 第一动作：先分类讨论 f(a)≠0 与 f(a)=0 两种情况
- 答案：选 B；充要条件是 f(a)=0 且 f'(a)≠0。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；本轮依据题图与解析确认复做入口：判断 |f(x)| 在 a 处不可导时，先分类看 f(a) 是否为 0，再检查 f'(a) 是否非零形成穿零尖点。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 按 f(a) 是否为 0 分类
  - 绝对值尖点判定
  - 用左右导数检验
- 质量发现：
  - `absolute_value_differentiability_iff_repaired`：题图、答案、解析主链、知识点、错因证据边界与关系裁决已按当前正式源逐项核对。；建议：
- 关系裁决：
  - GS-101：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `83dba3a88ef382ee177059cbfcf8b7ff0c9b95a17cdf994bdebfbc216fbe9122`；唯一图片 1 个；物理路径 1 个。

### GS-102 2025年真题选择题第七题

- 题目：绝对值差商条件反推零点可导性
- 所问：判断四个条件中有多少个能推出 f 在零点可导。
- 知识点：一元函数微分学应用；可导性判定；导数定义；绝对值函数；局部保号性；双侧极限
- 第一动作：逐项令 x 趋于 0，先检查分子常数项是否必须为 0
- 答案：选 D；四个条件都能推出 f 在 x=0 处可导。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；旧卡把原题误读成含 f(|x|) 的单侧信息题。本批按题图恢复为四个绝对值差商条件。可确认复做入口是：每项先用有限极限消去常数项，再按 f(0) 的符号分类并回到导数定义；是否为用户原始断点仍待复做确认。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 有限极限先消常数项
  - 按 f(0) 的符号分类
  - 导数定义
  - 左右极限符号检查
- 质量发现：
  - `misread_absolute_value_and_wrong_answer_repaired`：旧卡把题图中的函数值绝对值误读成绝对值自变量，因而错误排除一个条件；本批已恢复四个真实差商条件并把答案由 3 修正为 4。；建议：
- 关系裁决：
  - GS-102：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `e14a06a46460d6816393d9cb65817b985cdd3e6c4be9f419402cde8565352b87`；唯一图片 1 个；物理路径 1 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
