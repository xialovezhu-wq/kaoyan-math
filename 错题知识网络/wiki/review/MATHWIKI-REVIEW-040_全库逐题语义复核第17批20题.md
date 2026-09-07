---
wiki_id: MATHWIKI-REVIEW-040
type: target_level_semantic_review_batch
title: 全库逐题语义复核第17批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-040_全库逐题语义复核第17批20题.json
status: active
last_updated: 2026-07-23
---

# 全库逐题语义复核第17批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 1 张；覆盖 27 个物理图片路径与 25 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 15 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `MATH-TARGET-SEMANTIC-CLOSEOUT-20260723-B17`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-166](http://127.0.0.1:8765/open/GS-166) | 分段函数求导与极值 | 一元函数微分学应用、复合函数求导、单调性与极值、分段函数求导 | \(x<0\) 时 \(f^{\prime}(x)=e^x(x+1)\)，\(x>0\) 时 \(f^{\prime}(x)=2x^{2x}(\ln x+1)\)，\(x=0\) 处不可导；极大值 \(f(0)=1\)，极小值 \(f(-1)=1-e^{-1}\)、\(f(e^{-1})=e^{-2/e}\)。 | pending_user_confirmation：pending_user_confirmation：旧卡缺用户作答过程；待确认是否漏了 \(x=0\) 分段点的左右导数检查 | piecewise_point_derivative_and_semantic_duplicate_boundary_repaired |
| [GS-167](http://127.0.0.1:8765/open/GS-167) | 拐点处切线方程 | 凹凸性与拐点、二阶导数判拐点、切线方程 | \(\displaystyle y=4x-3\) | pending_user_confirmation：pending_user_confirmation：旧批量未记录个人第一错步；当前只确认不能把拐点入口和切线斜率入口混成一步 | inflection_sign_change_and_tangent_chain_verified |
| [GS-168](http://127.0.0.1:8765/open/GS-168) | 有理函数反常积分 | 反常积分、有理函数积分、部分分式 | \(\displaystyle \frac12\ln2\) | pending_user_confirmation：pending_user_confirmation：旧批量未记录个人第一错步；当前只确认不能把无穷上限当普通端点直接代入 | improper_limit_and_log_cancellation_verified |
| [GS-169](http://127.0.0.1:8765/open/GS-169) | 参数方程曲线曲率 | 曲率、参数方程求导、高阶导数 | \(\displaystyle \frac23\) | pending_user_confirmation：pending_user_confirmation：旧批量未记录个人第一错步；当前只确认不能把对 t 的二阶导误当成对 x 的二阶导 | parametric_curvature_derivative_object_verified |
| [GS-170](http://127.0.0.1:8765/open/GS-170) | 连乘型数列极限 | 极限与连续、数列极限、连乘型极限、黎曼和、定积分、定积分定义 | \boxed{L=\frac{4}{e}} | confirmed_personal：没有先把 \(\frac1n\) 放入根号，也没有想到对 \(n\) 次根连乘积取对数。 | confirmed_recurrence_evidence_preserved |
| [GS-171](http://127.0.0.1:8765/open/GS-171) | 黎曼和连续性参数 | 极限与连续、定积分、定积分性质 | \(\boxed{a=1}\) | pending_user_confirmation：pending_user_confirmation：旧卡缺用户作答过程；待确认是否没有先把平均和式转为定积分 | chapter_and_continuity_object_repaired |
| [GS-172](http://127.0.0.1:8765/open/GS-172) | 黎曼和极限 | 定积分、定积分性质、极限与连续 | \(\displaystyle \frac14+\frac\pi8\) | pending_user_confirmation：pending_user_confirmation：旧卡缺用户作答过程；待确认是否漏了区间长度系数或误套 \([0,1]\) | — |
| [GS-173](http://127.0.0.1:8765/open/GS-173) | 中点取样黎曼和极限 | 定积分、定积分性质、极限与连续 | \(\displaystyle \int_0^1 (x+1)f(x)\,dx\)（选 C） | pending_user_confirmation：pending_user_confirmation：旧卡缺用户作答过程；待确认是否漏了中点取样点或前置系数重写 | — |
| [GS-174](http://127.0.0.1:8765/open/GS-174) | 反常积分倒代换计算 | 定积分、反常积分、反常积分极限、第二类换元、反正切型积分 | \(\displaystyle \int_0^{+\infty}\frac{dx}{1+x^4}=\int_0^{+\infty}\frac{x^2}{1+x^4}\,dx=\frac{\sqrt2\pi}{4}\) | pending_user_confirmation：pending_user_confirmation：旧卡缺少用户本人作答过程；待确认是否没有先触发倒代换与互补积分相加 | cross_id_exact_duplicate_question_held |
| [GS-175](http://127.0.0.1:8765/open/GS-175) | 含参反常积分判敛 | 反常积分、定积分、参数分类讨论、等价无穷小、对数型积分 | A；$0<p<1,\ 0<q<2$。 | pending_user_confirmation：pending_user_confirmation：缺少用户本人作答过程；待确认是否没有先拆端点并逐端判敛 | two_endpoint_parameter_boundary_verified |
| [GS-176](http://127.0.0.1:8765/open/GS-176) | 含参反常积分求参数 | 反常积分、有理函数积分、部分分式、对数型积分 | $a=2$。 | pending_user_confirmation：pending_user_confirmation：缺少用户本人作答过程；待确认是否算出候选值后漏查内部奇点 | internal_pole_candidate_rejected |
| [GS-177](http://127.0.0.1:8765/open/GS-177) | 含参反常积分最值 | 反常积分、对数型积分、定积分、单调性与极值、参数分类讨论 | A；$\alpha_0=-\dfrac{1}{\ln(\ln2)}$。 | pending_user_confirmation：pending_user_confirmation：缺少用户本人作答过程；待确认是否没有先把积分化为显式含参函数 | — |
| [GS-178](http://127.0.0.1:8765/open/GS-178) | 含参反常积分判敛 | 反常积分、定积分、参数分类讨论、等价无穷小、对数型积分 | 题图字面严格结论为 \(p>-1\)，给定 B、C、D 均被包含，故无唯一选项；只有另加“积分必须确为反常积分”这一题图未写明的限制时，才有 \(-1<p\le0\) 并选 B。 | pending_user_confirmation：pending_user_confirmation：个人作答过程缺失；无法确认用户是否受题目歧义影响，本轮只登记来源边界与客观判敛入口 | source_stem_nonunique_mcq |
| [GS-179](http://127.0.0.1:8765/open/GS-179) | 反常积分敛散性选择 | 反常积分、定积分、不定积分、分部积分、第一类换元、反正切型积分、对数型积分 | D；发散的是 $\int_{-\infty}^{+\infty}\frac{x}{1+x^2}\,dx$。 | pending_user_confirmation：pending_user_confirmation：缺少用户本人作答过程；待确认是否把主值相消误当作收敛 | option_interval_transcription_repaired |
| [GS-180](http://127.0.0.1:8765/open/GS-180) | 反常积分敛散性选择 | 反常积分、定积分、高斯积分、等价无穷小、比较判别法、对数型积分、正弦等价无穷小 | B；收敛的是 $\int_0^{+\infty} e^{-x^2}\,dx$。 | pending_user_confirmation：pending_user_confirmation：缺少用户本人作答过程；待确认是否没有逐项标出反常点就直接凭形式判断 | tail_comparison_domain_repaired |
| [GS-181](http://127.0.0.1:8765/open/GS-181) | 定积分大小比较 | 定积分、定积分性质、定积分不等式、奇偶性、函数单调性、导数判单调、不等式证明 | C；$K>M>N$。 | pending_user_confirmation：pending_user_confirmation：缺少用户本人作答过程；待确认是否把中间基准值当成结论或漏做差值比较 | — |
| [GS-182](http://127.0.0.1:8765/open/GS-182) | 定积分不等式比较 | 定积分、定积分性质、定积分不等式、函数单调性、导数判单调、不等式证明 | A。 | pending_user_confirmation：pending_user_confirmation：缺少用户本人作答过程；待确认是否漏查积分上下限方向导致不等号方向不稳 | — |
| [GS-183](http://127.0.0.1:8765/open/GS-183) | 反函数积分面积比较 | 定积分、定积分应用、平面图形面积、反函数、凹凸性与拐点、定积分不等式、一元函数微分学应用 | D，\(0<P<1\) | confirmed_personal：没有先分层判断“反函数面积互补”与“凹性弦线放缩”各自使用什么条件；讨论求导时又未先区分函数值、外层导数值和整个复合函数的导数。 | strict_midpoint_domain_and_user_evidence_repaired |
| [GS-184](http://127.0.0.1:8765/open/GS-184) | 定积分估值 | 定积分、定积分性质、定积分不等式、函数单调性、导数判单调 | B；$\frac12\le I\le\frac{\sqrt2}{2}$。 | pending_user_confirmation：pending_user_confirmation：缺少用户本人作答过程；待确认是否没有先判断 \(\sin x/x\) 的单调性就直接粗放缩 | integral_bound_endpoint_chain_verified |
| [GS-185](http://127.0.0.1:8765/open/GS-185) | 定积分几何意义：正负面积比较选区间 | 定积分、定积分性质、平面图形面积、积分保号 | A，\((a,b)=(-1,1)\) | pending_user_confirmation：pending_user_confirmation：旧批量未记录个人第一错步；当前只确认不能机械计算四个选项而忽略正负面积净贡献 | signed_area_interval_minimum_verified |

## 逐题复核

### GS-166 2019年第15题-2

- 题目：已知 \(f(x)=x^{2x}\ (x>0),\ f(x)=xe^x+1\ (x\le0)\)，求 \(f^{\prime}(x)\) 并求极值。
- 所问：分段函数求导与极值
- 知识点：一元函数微分学应用；复合函数求导；单调性与极值；分段函数求导
- 第一动作：先分别写出 \(x<0\)、\(x>0\) 两段的导数
- 答案：\(x<0\) 时 \(f^{\prime}(x)=e^x(x+1)\)，\(x>0\) 时 \(f^{\prime}(x)=2x^{2x}(\ln x+1)\)，\(x=0\) 处不可导；极大值 \(f(0)=1\)，极小值 \(f(-1)=1-e^{-1}\)、\(f(e^{-1})=e^{-2/e}\)。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡缺用户作答过程；待确认是否漏了 \(x=0\) 分段点的左右导数检查
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 分别求两段导数。
  - 在分段点用左右差商单独检查可导性。
  - 结合各区间导数符号与分段点函数值确定极值。
- 质量发现：
  - `piecewise_point_derivative_and_semantic_duplicate_boundary_repaired`：已补正 x=0 左差商趋于 1、右差商趋于负无穷，故该点不可导但仍为局部极大；同时识别与 GS-137 的跨 ID 语义同题边界。；建议：
- 关系裁决：
  - GS-166：`hold_duplicate_identity_without_aggregate_edge`；
- 当前快照：`stale`；正式卡 `d7fa31b390df28d12196797cb34d6f6f13e83411766110488b05da2d60abf415`；唯一图片 1 个；物理路径 1 个。

### GS-167 2018年第10题

- 题目：题图为曲线 \(y=x^2+2\ln x\) 在拐点处的切线方程，先用二阶导数找拐点，再用一阶导数求切线斜率。
- 所问：拐点处切线方程
- 知识点：凹凸性与拐点；二阶导数判拐点；切线方程
- 第一动作：先求二阶导并结合定义域确定拐点
- 答案：\(\displaystyle y=4x-3\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧批量未记录个人第一错步；当前只确认不能把拐点入口和切线斜率入口混成一步
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由定义域和二阶导数零点锁定拐点候选。
  - 检查二阶导数在候选点两侧变号。
  - 用一阶导数求斜率并写点斜式切线。
- 质量发现：
  - `inflection_sign_change_and_tangent_chain_verified`：已核对定义域、二阶导变号、拐点坐标和切线 y=4x-3 的完整动作链。；建议：
- 关系裁决：
  - GS-167：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `d15cbe444ecf29b0e35e2183bfa540557d2748e8a194c6b1b88da1595011b51d`；唯一图片 2 个；物理路径 2 个。

### GS-168 2018年第11题

- 题目：题图为反常积分 \(\int_5^{+\infty}\frac{1}{x^2-4x+3}\,dx\)，核心是先因式分解并做部分分式，再按无穷上限取极限。
- 所问：有理函数反常积分
- 知识点：反常积分；有理函数积分；部分分式
- 第一动作：先因式分解分母并做部分分式
- 答案：\(\displaystyle \frac12\ln2\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧批量未记录个人第一错步；当前只确认不能把无穷上限当普通端点直接代入
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 分母因式分解为一次因子乘积。
  - 部分分式后保留无穷上限截断参数。
  - 先合并对数再取极限，得到有限值。
- 质量发现：
  - `improper_limit_and_log_cancellation_verified`：题图与独立解析图一致，反常上限按截断极限处理后结果为二分之一乘 ln2。；建议：
- 关系裁决：
  - GS-687：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-604：`remove_broad_stale_or_identity_edge`；
- 当前快照：`current`；正式卡 `e9d95c8d25c7a1ba2dccde076b950fb23d7d4591f7442a83843f5f3f8d3a1012`；唯一图片 2 个；物理路径 2 个。

### GS-169 2018年第12题

- 题目：题图为参数曲线 \(x=\cos^3t,\ y=\sin^3t\) 在 \(t=\pi/4\) 对应点处的曲率，入口是参数方程的一阶、二阶导数与曲率公式。
- 所问：参数方程曲线曲率
- 知识点：曲率；参数方程求导；高阶导数
- 第一动作：先判断曲率公式里的 y' 和 y'' 都是关于 x 的导数
- 答案：\(\displaystyle \frac23\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧批量未记录个人第一错步；当前只确认不能把对 t 的二阶导误当成对 x 的二阶导
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先把参数导数转换为关于 x 的一阶导数。
  - 再用链式关系求关于 x 的二阶导数。
  - 代入曲率公式并在指定参数点化简。
- 质量发现：
  - `parametric_curvature_derivative_object_verified`：题图与独立解析图一致，明确 y 一撇、y 二撇均是关于 x 的导数，曲率为 2/3。；建议：
- 关系裁决：
  - GS-650：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
- 当前快照：`stale`；正式卡 `57075285ab09a797c930404bb5b40481d292df68bf737f551b79876c21087232`；唯一图片 2 个；物理路径 2 个。

### GS-170 强化例题8.1 / 135762 连乘n次根极限

- 题目：求 $$ \lim_{n\to\infty} \frac1n\sqrt[n]{n(n+1)(n+2)\cdots(2n-1)}. $$ 这是“$n$ 次根下有 $n$ 个因子”的连乘型数列极限。
- 所问：连乘型数列极限
- 知识点：极限与连续；数列极限；连乘型极限；黎曼和；定积分；定积分定义
- 第一动作：先把外面的 \(\frac1n\) 写成 \(n\) 次根内的 \(\frac1{n^n}\)，得到 \(\left[\prod_{k=0}^{n-1}(1+\frac{k}{n})\right]^{1/n}\)。
- 答案：\boxed{L=\frac{4}{e}}
- 个人错因边界：confirmed_personal；没有先把 \(\frac1n\) 放入根号，也没有想到对 \(n\) 次根连乘积取对数。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 把根号外因子内化，凑成 n 个标准因子的几何平均。
  - 取对数把连乘化成平均和式。
  - 用黎曼和转定积分，计算后指数还原。
- 质量发现：
  - `confirmed_recurrence_evidence_preserved`：保留 2026-05-11 与 2026-06-12 两次用户确认的同一入口复发，不把视觉复核重复计数。；建议：
- 关系裁决：
  - GS-688：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-442：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `7fa4a2a94225910a9eec81fe64f95ac628cbbf0ee2b6ac5a6519f1f3325e6b78`；唯一图片 1 个；物理路径 3 个。

### GS-171 强化例题8.3

- 题目：分段定义中 \(x>0\) 部分为余弦平均和的极限，且 \(f(-x)=f(x)\)，求连续时的 \(a\)。
- 所问：黎曼和连续性参数
- 知识点：极限与连续；定积分；定积分性质
- 第一动作：先将 \(\frac1n\sum\cos(ix/n)\) 改写为 \(\int_0^1\cos(tx)\,dt\)
- 答案：\(\boxed{a=1}\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡缺用户作答过程；待确认是否没有先把平均和式转为定积分
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 把余弦平均和式转成区间上的定积分。
  - 求出 x>0 时的显式函数并取右极限。
  - 利用偶性与分段点函数值匹配连续条件。
- 质量发现：
  - `chapter_and_continuity_object_repaired`：章节由宽泛定积分修正为极限与连续，参数由分段点连续条件确定。；建议：
- 关系裁决：
  - GS-172：`remove_broad_stale_or_identity_edge`；
  - GS-173：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `d7ac64c5e32b86ea1ef6eb43a744d128d1e2e0d78062caebba3c86fede4f73fe`；唯一图片 1 个；物理路径 1 个。

### GS-172 强化例题8.4

- 题目：求 \(\lim_{n\to\infty}\sum_{k=1}^n \frac{\pi}{4n}\cos^2\frac{k\pi}{4n}\)。
- 所问：黎曼和极限
- 知识点：定积分；定积分性质；极限与连续
- 第一动作：先确定 \(\Delta x=\pi/(4n)\)，积分区间为 \([0,\pi/4]\)
- 答案：\(\displaystyle \frac14+\frac\pi8\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡缺用户作答过程；待确认是否漏了区间长度系数或误套 \([0,1]\)
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 识别分割宽度与积分区间。
  - 把和式改写为对应黎曼和。
  - 计算三角函数定积分。
- 关系裁决：
  - GS-702：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-172：`remove_broad_stale_or_identity_edge`；
  - GS-173：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `3ad26a72a61b7f7f9146e2244a7f54f7fe027a356411987ca41f2260bc09918a`；唯一图片 1 个；物理路径 1 个。

### GS-173 强化例题8.5

- 题目：设 \(f(x)\) 连续，求 \(\lim_{n\to\infty}\sum_{k=1}^n\frac{k-1/2+n}{n^2}f\left(\frac{2k-1}{2n}\right)\)。
- 所问：中点取样黎曼和极限
- 知识点：定积分；定积分性质；极限与连续
- 第一动作：先令 \(x_k=(2k-1)/(2n)\)，再把系数写成 \(\frac1n(x_k+1)\)
- 答案：\(\displaystyle \int_0^1 (x+1)f(x)\,dx\)（选 C）
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡缺用户作答过程；待确认是否漏了中点取样点或前置系数重写
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 识别中点取样点。
  - 把前置系数重写为分割宽度乘被积函数权重。
  - 转成定积分并匹配选项。
- 关系裁决：
  - GS-173：`remove_broad_stale_or_identity_edge`；
  - GS-173：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `22671dc12c9838998397e83efaa17ea45ac29d92690561230f0931bf51c8424c`；唯一图片 1 个；物理路径 1 个。

### GS-174 1000题A组11.6

- 题目：证明 \(\int_0^{+\infty}\frac{dx}{1+x^4}=\int_0^{+\infty}\frac{x^2}{1+x^4}\,dx=\frac{\sqrt2}{4}\pi\)。
- 所问：反常积分倒代换计算
- 知识点：定积分；反常积分；反常积分极限；第二类换元；反正切型积分
- 第一动作：先对其中一个积分作 \(x=1/t\) 倒代换，确认两个积分可以互换相等。
- 答案：\(\displaystyle \int_0^{+\infty}\frac{dx}{1+x^4}=\int_0^{+\infty}\frac{x^2}{1+x^4}\,dx=\frac{\sqrt2\pi}{4}\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡缺少用户本人作答过程；待确认是否没有先触发倒代换与互补积分相加
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 对其中一个积分作倒数换元，证明两积分相等。
  - 两式相加后化为标准反正切型积分。
  - 计算公共值；同时将跨 ID 精确同题身份从普通关系图中阻断。
- 质量发现：
  - `cross_id_exact_duplicate_question_held`：GS-174 与 GS-315 的 source_locator、source_refid、题图 SHA-256、题面和解法一致；保留稳定 ID，阻断普通聚合边。；建议：
- 关系裁决：
  - GS-580：`remove_broad_stale_or_identity_edge`；
  - GS-674：`remove_broad_stale_or_identity_edge`；
  - GS-315：`hold_duplicate_identity_without_aggregate_edge`；
- 当前快照：`stale`；正式卡 `93326aba280e53a06402029fc9168e6a77fcaea42466cdd1d36f00811da03fe5`；唯一图片 1 个；物理路径 1 个。

### GS-175 强化例题8.6

- 题目：设 $p>0,q>0$，判断反常积分 $\int_0^1 \frac{\ln x}{x^p(1-x)^q}\,dx$ 收敛时的参数范围。
- 所问：含参反常积分判敛
- 知识点：反常积分；定积分；参数分类讨论；等价无穷小；对数型积分
- 第一动作：先把积分拆到 $0$ 与 $1$ 两个可疑端点，逐端写出等价主项。
- 答案：A；$0<p<1,\ 0<q<2$。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：缺少用户本人作答过程；待确认是否没有先拆端点并逐端判敛
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 分别检查 x 趋于 0 正侧和 x 趋于 1 负侧。
  - 用对数与幂函数等价主项得到两端参数条件。
  - 取两个条件的交集。
- 质量发现：
  - `two_endpoint_parameter_boundary_verified`：已明确两个端点分别产生 p 与 q 的限制，且个人错因仍为待确认。；建议：
- 关系裁决：
  - GS-178：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-177：`remove_broad_stale_or_identity_edge`；
  - GS-179：`remove_broad_stale_or_identity_edge`；
  - GS-580：`remove_broad_stale_or_identity_edge`；
  - GS-581：`remove_broad_stale_or_identity_edge`；
  - GS-582：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `5484afa3cd8ac6d067460e7dad7e75c2b3b10c74e7dd707ff0c51bfac6720b4b`；唯一图片 1 个；物理路径 1 个。

### GS-176 2025年真题填空题第一题

- 题目：已知 $\int_1^{+\infty}\frac{a}{x(2x+a)}\,dx=\ln2$，求参数 $a$。
- 所问：含参反常积分求参数
- 知识点：反常积分；有理函数积分；部分分式；对数型积分
- 第一动作：先做部分分式分解，算出候选参数后再检查 $2x+a=0$ 是否落入积分区间。
- 答案：$a=2$。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：缺少用户本人作答过程；待确认是否算出候选值后漏查内部奇点
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 部分分式并计算截断反常积分。
  - 由积分值方程求参数候选。
  - 回查分母零点是否落入积分区间，排除内部奇点候选。
- 质量发现：
  - `internal_pole_candidate_rejected`：方程给出候选 a=2 与 a=-6；a=-6 使 x=3 成为积分区间内奇点，必须排除。；建议：
- 关系裁决：
  - GS-177：`remove_broad_stale_or_identity_edge`；
  - GS-178：`remove_broad_stale_or_identity_edge`；
  - GS-179：`remove_broad_stale_or_identity_edge`；
  - GS-180：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `5b41bbaf3a35fc1e276fefffe7b1126b6cb3979f33156e17aa1b4fd2175250ab`；唯一图片 1 个；物理路径 1 个。

### GS-177 2023年真题第六题

- 题目：设 $f(\alpha)=\int_2^{+\infty}\frac{1}{x(\ln x)^{\alpha+1}}\,dx$，求使 $f(\alpha)$ 取得最小值的 $\alpha_0$。
- 所问：含参反常积分最值
- 知识点：反常积分；对数型积分；定积分；单调性与极值；参数分类讨论
- 第一动作：先令 $t=\ln x$，把反常积分化成关于 $\alpha$ 的显式函数。
- 答案：A；$\alpha_0=-\dfrac{1}{\ln(\ln2)}$。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：缺少用户本人作答过程；待确认是否没有先把积分化为显式含参函数
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 换元把反常积分化为参数的显式函数。
  - 先确定收敛参数域。
  - 对显式函数取对数或求导，定位并验证最小值。
- 关系裁决：
  - GS-177：`remove_broad_stale_or_identity_edge`；
  - GS-177：`remove_broad_stale_or_identity_edge`；
  - GS-178：`remove_broad_stale_or_identity_edge`；
  - GS-179：`remove_broad_stale_or_identity_edge`；
  - GS-180：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `62a04a53cb42c468e53165b0d3b03dca9deecafa7c4e7bd42917b279c99675ea`；唯一图片 1 个；物理路径 1 个。

### GS-178 强化例题8.7

- 题目：判断 $\int_0^1 x^p(1-x)^{p-1}\ln x\,dx$ 收敛时的参数范围，并处理单选题的隐含口径。
- 所问：含参反常积分判敛
- 知识点：反常积分；定积分；参数分类讨论；等价无穷小；对数型积分
- 第一动作：先把积分拆成左右端点两段，分别化为 $x^p\ln x$ 与 $t^p$ 型判别。
- 答案：题图字面严格结论为 \(p>-1\)，给定 B、C、D 均被包含，故无唯一选项；只有另加“积分必须确为反常积分”这一题图未写明的限制时，才有 \(-1<p\le0\) 并选 B。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：个人作答过程缺失；无法确认用户是否受题目歧义影响，本轮只登记来源边界与客观判敛入口
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 逐端点写等价主项并得到严格收敛域。
  - 将严格数学结论与题图选项逐一比对。
  - 标记题干缺少隐含限制导致选项不唯一，不把讲义口径冒充题面条件。
- 质量发现：
  - `source_stem_nonunique_mcq`：题图字面严格收敛条件是 p>-1，B、C、D 都被包含；只有额外加入题图未写明的确为反常限制才得到 B。；建议：
- 关系裁决：
  - GS-178：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-178：`remove_broad_stale_or_identity_edge`；
  - GS-178：`remove_broad_stale_or_identity_edge`；
  - GS-179：`remove_broad_stale_or_identity_edge`；
  - GS-180：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `e1bf528a9bcbc73a5c7cc25e986eb324f41074929719d976c8b727e320e2e663`；唯一图片 1 个；物理路径 1 个。

### GS-179 1000题A组8.13

- 题目：在四个反常积分中判断发散项，重点区分奇函数主值与真正反常积分收敛。
- 所问：反常积分敛散性选择
- 知识点：反常积分；定积分；不定积分；分部积分；第一类换元；反正切型积分；对数型积分
- 第一动作：先把无穷区间拆成两侧反常积分，逐侧检查极限是否有限存在。
- 答案：D；发散的是 $\int_{-\infty}^{+\infty}\frac{x}{1+x^2}\,dx$。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：缺少用户本人作答过程；待确认是否把主值相消误当作收敛
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 把全实轴反常积分拆成两侧独立极限。
  - 逐项检查端点或无穷端的收敛性。
  - 区分柯西主值相消与通常反常积分收敛。
- 质量发现：
  - `option_interval_transcription_repaired`：详情页旧版把 B、C 的积分区间抄错；已按题图修为全实轴，并区分绝对收敛的零值与 D 的通常反常积分发散。；建议：
- 关系裁决：
  - GS-180：`verify_existing_strong_edge`；
  - GS-580：`verify_existing_strong_edge`；
  - GS-179：`remove_broad_stale_or_identity_edge`；
  - GS-179：`remove_broad_stale_or_identity_edge`；
  - GS-179：`remove_broad_stale_or_identity_edge`；
  - GS-179：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `d93e4bb5397f7990bb17f659ef713b1c588458f712b2049984d37ff7cd9eecf7`；唯一图片 1 个；物理路径 1 个。

### GS-180 1000题A组8.15

- 题目：在四个反常积分中判断收敛项：A 为 $\int\frac{1}{x\ln x}$ 发散，B 为高斯积分收敛，C/D 分别有主值或端点发散陷阱。
- 所问：反常积分敛散性选择
- 知识点：反常积分；定积分；高斯积分；等价无穷小；比较判别法；对数型积分；正弦等价无穷小
- 第一动作：先逐项定位可疑端点或无穷端，再把局部主项化成标准反常积分。
- 答案：B；收敛的是 $\int_0^{+\infty} e^{-x^2}\,dx$。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：缺少用户本人作答过程；待确认是否没有逐项标出反常点就直接凭形式判断
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 逐项定位全部反常点。
  - 在每个反常点用等价主项或比较判别。
  - 高斯积分只需在尾部与可积函数比较，其他选项分别暴露对数或奇点发散。
- 质量发现：
  - `tail_comparison_domain_repaired`：比较 e 的负 x 平方与 e 的负 x 只用于 x 大于等于 1 的尾部，不能错误扩展到整个非负轴；章节同步修为反常积分。；建议：
- 关系裁决：
  - GS-180：`verify_existing_strong_edge`；
  - GS-675：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-676：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-580：`add_strong_edge`；
  - GS-180：`remove_broad_stale_or_identity_edge`；
  - GS-180：`remove_broad_stale_or_identity_edge`；
  - GS-180：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `27bff554689de02ffcc8b29433b0ca70869efaf07bf4a6002d2ba0884f0d82cd`；唯一图片 1 个；物理路径 1 个。

### GS-181 1000题A组6.4

- 题目：比较三个定积分 $M,N,K$ 的大小，先算 $M=1$，再分别判断 $N-M$ 与 $K-M$ 的符号。
- 所问：定积分大小比较
- 知识点：定积分；定积分性质；定积分不等式；奇偶性；函数单调性；导数判单调；不等式证明
- 第一动作：先算出 $M=1$，再分别构造 $N-M$ 与 $K-M$ 判符号。
- 答案：C；$K>M>N$。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：缺少用户本人作答过程；待确认是否把中间基准值当成结论或漏做差值比较
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先直接算出基准积分 M。
  - 分别把 N-M 与 K-M 写成便于判号的积分。
  - 用奇偶性、换元或函数比较得到严格次序。
- 关系裁决：
  - GS-577：`add_strong_edge`；
  - GS-182：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `f4df3c94e18303b42b27b331007922043d99c7f87aaacd94e38fb72b308a7134`；唯一图片 1 个；物理路径 1 个。

### GS-182 1000题A组8.7

- 题目：已知 $g$ 在 $[0,\pi/2]$ 连续且 $g'(x)\ge0$，判断含 $g(t)$ 与 $g(\sin t)$ 的积分不等式。
- 所问：定积分不等式比较
- 知识点：定积分；定积分性质；定积分不等式；函数单调性；导数判单调；不等式证明
- 第一动作：先由 $g'(x)\ge0$ 判出 $g$ 单调不减，再写 $g(t)\ge g(\sin t)$。
- 答案：A。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：缺少用户本人作答过程；待确认是否漏查积分上下限方向导致不等号方向不稳
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由导数非负得到 g 单调不减。
  - 在给定区间比较 t 与 sin t。
  - 保持积分上下限方向，逐点比较后积分。
- 关系裁决：
  - GS-662：`add_strong_edge`；
  - GS-182：`remove_broad_stale_or_identity_edge`；
  - GS-184：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `9c27088f1e6d529fe5eebfca1db85342ca23549f7afd9b61b08cbb890cce9cf4`；唯一图片 1 个；物理路径 1 个。

### GS-183 1000题A组6.12 反函数积分面积比较

- 题目：题图中的严格 midpoint 不等式按数学上可成立的意图解释为 \(x_1\ne x_2\)；若允许 \(x_1=x_2\)，严格不等式会立即自相矛盾。 设 \(f(x)\) 在 \([0,2]\) 上单调连续，\(f(0)=1,\ f(2)=2\)，且对任意 \(x_1,x_2\in[0,2]\) 有 $$ f\!\left(\frac{x_1+x_2}{2}\right)> \frac{f(x_1)+f(x_2)}2. $$ 令 \(g(x)\) 为 \(f(x)\) 的反函数，比较 $$ P=\int_1^2 g(x)\,dx $$ 所在范围。
- 所问：反函数积分面积比较
- 知识点：定积分；定积分应用；平面图形面积；反函数；凹凸性与拐点；定积分不等式；一元函数微分学应用
- 第一动作：先画 f 的端点弦线和反函数图像
- 答案：D，\(0<P<1\)
- 个人错因边界：confirmed_personal；没有先分层判断“反函数面积互补”与“凹性弦线放缩”各自使用什么条件；讨论求导时又未先区分函数值、外层导数值和整个复合函数的导数。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先用反函数积分面积互补恒等式改写 P。
  - 再由严格凹性与端点弦线比较原函数面积。
  - 分开检查反函数存在、逆导数公式条件与题干严格中点条件。
- 质量发现：
  - `strict_midpoint_domain_and_user_evidence_repaired`：严格中点条件若允许 x1=x2 会自相矛盾，已明确按 x1 不等于 x2 的数学意图解释；并同步 2026-07-18 用户确认的真实方法断点。；建议：
- 关系裁决：
  - GS-490：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-514：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-664：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-247：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `fee9916df74b7e5459b9e9ed3280e74b23b8c87490cc5f4daf33edde470145e2`；唯一图片 2 个；物理路径 2 个。

### GS-184 1000题A组6.15

- 题目：估计 $I=\int_{\pi/4}^{\pi/2}\frac{\sin x}{x}\,dx$ 的范围。
- 所问：定积分估值
- 知识点：定积分；定积分性质；定积分不等式；函数单调性；导数判单调
- 第一动作：先令 $f(x)=\frac{\sin x}{x}$ 并用导数判断其在 $[\pi/4,\pi/2]$ 上单调。
- 答案：B；$\frac12\le I\le\frac{\sqrt2}{2}$。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：缺少用户本人作答过程；待确认是否没有先判断 \(\sin x/x\) 的单调性就直接粗放缩
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 证明 sin x/x 在给定区间单调。
  - 用端点函数值给出逐点上下界。
  - 对上下界积分并保留闭区间端点等号。
- 质量发现：
  - `integral_bound_endpoint_chain_verified`：已核对 sin x/x 的单调性、端点界与积分区间长度，得到闭区间估值。；建议：
- 关系裁决：
  - GS-445：`verify_existing_strong_edge`；
  - GS-184：`remove_broad_stale_or_identity_edge`；
  - GS-209：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `3dfa86e61e37367c297b6dbff00b393713ee16f3a0bff90b639cbaf0f9d280c6`；唯一图片 1 个；物理路径 1 个。

### GS-185 1000题A组8.6 正负面积选区间最小

- 题目：设 $$ f(x)= \begin{cases} x\ln x,&x>0,\\ x^2+x,&x\le 0. \end{cases} $$ 在四个候选区间中，判断哪个 \((a,b)\) 使 $$ \int_a^b f(x)\,dx $$ 取得最小值。
- 所问：定积分几何意义：正负面积比较选区间
- 知识点：定积分；定积分性质；平面图形面积；积分保号
- 第一动作：先找分段函数的零点和正负区间
- 答案：A，\((a,b)=(-1,1)\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧批量未记录个人第一错步；当前只确认不能机械计算四个选项而忽略正负面积净贡献
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先找分段函数的零点和正负区间。
  - 把定积分理解为带符号面积。
  - 比较候选区间新增或删去的正负贡献，确定最小者。
- 质量发现：
  - `signed_area_interval_minimum_verified`：题图与独立解析图一致，按正负面积净贡献选择区间而非机械计算四个选项。；建议：
- 关系裁决：
  - GS-294：`verify_existing_strong_edge`；
- 当前快照：`stale`；正式卡 `374cb4fbac6ad112a8766537287672feeb0dcb2d965a1077c46af39942831538`；唯一图片 2 个；物理路径 2 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
