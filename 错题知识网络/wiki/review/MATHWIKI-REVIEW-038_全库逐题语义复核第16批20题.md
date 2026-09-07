---
wiki_id: MATHWIKI-REVIEW-038
type: target_level_semantic_review_batch
title: 全库逐题语义复核第16批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-038_全库逐题语义复核第16批20题.json
status: active
last_updated: 2026-07-23
---

# 全库逐题语义复核第16批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 0 张；覆盖 21 个物理图片路径与 21 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 20 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `MATH-TARGET-SEMANTIC-CLOSEOUT-20260723-B16`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-144](http://127.0.0.1:8765/open/GS-144) | 二阶充分条件判断极值 | 一元函数微分学应用、单调性与极值、二阶导数判极值 | 选 B：$f(x_0)$ 是 $f(x)$ 的极小值。 | pending_user_confirmation：pending_user_confirmation：个人原始错因未记录；题图只能确认客观入口是把 $x=x_0$ 与 $f^{\prime}(x_0)=0$ 代入方程，再判断 $\frac{1-e^{-x_0}}{x_0}>0$，不能据此反推用户当时漏了哪一步。 | stationary_substitution_sign_chain_verified |
| [GS-145](http://127.0.0.1:8765/open/GS-145) | 积分方程确定隐函数极值 | 一元函数微分学应用、变上限积分、隐函数求导、单调性与极值、隐函数实际定义域 | 选择 B：只有极小值点 \(x=4\)，极小值为 \(0\)。 | confirmed_personal：用户确认对积分方程两边求导的方向正确，但右边 \(\frac13(\sqrt{x}-2)^2\) 求导时漏掉关键因子 \(\sqrt{x}-2\)，导致没有找到 \(x=4\)；同时把 \(x=0\) 当作候选，却未先检查左侧积分的值域，事实上 \(x=0\) 时方程无实数解。 | integral_exponent_domain_and_unique_minimum_repaired |
| [GS-146](http://127.0.0.1:8765/open/GS-146) | 导函数判别式反推参数范围 | 一元函数微分学应用、单调性与极值、凹凸性与拐点、参数范围 | $a\in\left[\frac94,\frac{13}{4}\right)$ | pending_user_confirmation：pending_user_confirmation：个人原始错因未记录；题图只能确认客观入口是先剥离正因子 $e^x$，再分别把“无极值点”和“有拐点”翻译为两个二次因子的判别式条件。 | double_discriminant_boundary_verified |
| [GS-148](http://127.0.0.1:8765/open/GS-148) | 竖直切线处曲率圆 | 一元函数微分学应用、曲率、曲率圆、切线方程 | \(\left(x-\frac12\right)^2+y^2=\frac14\) | legacy_unclassified：legacy_unclassified：旧来源候选错因是把曲率公式固定理解为 \(y=y(x)\) 型；当前题图无用户作答。可确认的客观入口是把 \(y^2=x\) 改写为 \(x=y^2\)，用 \(x=x(y)\) 型曲率公式求半径并沿法线方向定圆心。 | vertical_tangent_curvature_representation_verified |
| [GS-149](http://127.0.0.1:8765/open/GS-149) | 曲率相等的充分必要判断 | 曲率、二阶接触、泰勒公式、充分必要条件判断 | A（充分不必要条件） | pending_user_confirmation：暂无明确个人错因；本轮依据题图与解析图补强可确认的题型入口：判断“\(\lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^2}=0\)”与“两曲线相切且曲率相等”的关系时，必须分充分性和必要性两向验证，不能把能推出曲率相等直接当成等价条件。 | necessity_counterexample_added |
| [GS-150](http://127.0.0.1:8765/open/GS-150) | 反函数渐近线判断 | 一元函数微分学应用、反函数、渐近线、无穷远极限 | $y=3$ 与 $y=-3$。由 $g(x)=3\frac{e^{2x}-1}{e^{2x}+1}=3\tanh x$ 得出。 | legacy_unclassified：legacy_unclassified：旧来源候选错因是只检查一个无穷远方向；当前题图无用户作答。客观上 $g(x)=3\tanh x$，必须分别检查 $x\to+\infty$ 与 $x\to-\infty$，得到两条水平渐近线。 | both_infinity_directions_verified |
| [GS-151](http://127.0.0.1:8765/open/GS-151) | 渐近线条数判断 | 一元函数微分学应用、等价无穷小、泰勒展开、渐近线、极限与连续 | (A) 4 | legacy_unclassified：legacy_unclassified：旧来源候选错因是没有把定义域端点、$x\to+\infty$、$x\to-\infty$ 列成完整检查清单；当前题图无用户作答，具体个人错步待复做确认。 | complete_asymptote_checklist_verified |
| [GS-152](http://127.0.0.1:8765/open/GS-152) | 极坐标曲线斜渐近线 | 一元函数微分学应用、极限与连续、渐近线、极坐标 | $$\boxed{y=\sqrt3x+\frac23}$$ 令 $\alpha=\frac\pi3$，当 $\theta\to\alpha$ 时 $r\to\infty$，且 $$r\sin(\theta-\alpha)\to\frac13.$$ 故斜渐近线满足 $-x\sin\alpha+y\cos\alpha=\frac13$，化简得 $y=\sqrt3x+\frac23$。 | pending_user_confirmation：pending_user_confirmation：旧正式卡只保留极坐标题摘要，暂无用户原始作答过程；当前路径下的 question_01.png 实际属于另一道积分中值定理题，禁止据此补写本题题面、答案或个人错因。 | formal_visual_mismatch_held |
| [GS-153](http://127.0.0.1:8765/open/GS-153) | 幂乘指数函数单调性与最值分类讨论 | 一元函数微分学应用、单调性与极值、参数分类讨论、无穷远极限 | $n=1$：$(-\infty,1)$ 增、$(1,+\infty)$ 减，最大值 $e^{-1}$，无最小值；$n\ge3$ 奇数：$(-\infty,n)$ 增、$(n,+\infty)$ 减，最大值 $n^ne^{-n}$，无最小值；$n\ge2$ 偶数：$(-\infty,0)$ 减、$(0,n)$ 增、$(n,+\infty)$ 减，最小值 $0$，无最大值。 | pending_user_confirmation：pending_user_confirmation：个人原始错因未记录；题图只能确认客观入口是先求导得到 $x^{n-1}e^{-x}(n-x)$，再按 $n=1$、奇数 $n\ge3$、偶数 $n\ge2$ 分类并检查两端极限。 | parity_classification_and_endpoint_limits_verified |
| [GS-154](http://127.0.0.1:8765/open/GS-154) | 复合函数二阶导与拐点条件 | 一元函数微分学应用、复合函数求导、高阶导数、凹凸性与拐点 | $f^{\prime\prime}(1)=1$ | legacy_unclassified：legacy_unclassified：旧来源候选错因是对 $y=\sqrt{f(x)}$ 求二阶导时误处理常数因子 $1/2$；当前题图无用户作答。客观入口是先提出 $1/2$，再对 $f^{\prime}(x)f(x)^{-1/2}$ 用乘积与链式法则。 | composite_second_derivative_factor_verified |
| [GS-155](http://127.0.0.1:8765/open/GS-155) | 极值点方程与数列极限 | 一元函数微分学应用、单调性与极值、对数重要极限、数列极限 | \(\lim_{n\to\infty}\xi_n=1\) | pending_user_confirmation：个人原始错因未记录；以下仅能确认复做入口：先由极值条件解出 \(\xi_n=n\ln(1+1/n)\)，再转成对数重要极限，真实第一错步待用户复做确认。 | extreme_point_log_limit_chain_verified |
| [GS-156](http://127.0.0.1:8765/open/GS-156) | 由微分方程判极值类型 | 一元函数微分学应用、单调性与极值、微分方程 | (1) 极小值；(2) 极小值。 | legacy_unclassified：历史折叠解析把错步定位为 \(\alpha<0\) 时没有合并检查 \(1-e^{-\alpha}\) 与分母 \(\alpha\) 的符号，但缺少可追溯原始作答，暂按 legacy_unclassified 保留，不能视为本轮已确认个人错因。 | zero_point_and_nonzero_stationary_boundaries_verified |
| [GS-157](http://127.0.0.1:8765/open/GS-157) | 含参变上限积分极值 | 定积分、变上限积分、分部积分、单调性与极值 | 极大值为 \(f(0)=\frac13\ln2+\frac49-\frac\pi6\)，极小值为 \(f(1)=0\)。 | pending_user_confirmation：个人原始错因未记录；题面可确认的复做入口是先对含参变上限积分使用莱布尼茨公式求导，再判两个驻点并回代求极值，真实第一错步待用户复做确认。 | oriented_integral_sign_and_extrema_repaired |
| [GS-158](http://127.0.0.1:8765/open/GS-158) | 无穷远根式极限 | 极限与连续、函数极限、无穷远根式极限、指数衰减 | \(b=-\frac12\) | pending_user_confirmation：个人原始错因未记录；题面可确认的复做入口是先处理 \(x\to-\infty\) 下 \(\sqrt{x^2-x+1}=-x\sqrt{1-1/x+1/x^2}\) 的符号，再保留根式一阶小量与 \(xe^x\to0\)，真实第一错步待用户复做确认。 | negative_infinity_rationalization_sign_repaired |
| [GS-159](http://127.0.0.1:8765/open/GS-159) | 变上限积分最值 | 定积分、变上限积分、单调性与极值 | 最大值为 \(\frac{1+e^{-\pi/2}}{2}\)。 | pending_user_confirmation：个人原始错因未记录；题面可确认的复做入口是由 \(f^{\prime}(x)=e^{-x}\cos x\) 作完整符号表，确定闭区间最大点后再计算积分值，真实第一错步待用户复做确认。 | closed_interval_extremum_chain_verified |
| [GS-160](http://127.0.0.1:8765/open/GS-160) | 绝对值定积分单调凹凸判别 | 定积分、绝对值分类、单调性与极值、凹凸性判定 | \(\boxed{A}\)：在 \((0,\frac{\sqrt2}{2})\) 上单调减少，在 \((\frac{\sqrt2}{2},1)\) 上单调增加，且按本题教材术语曲线为凹。 | pending_user_confirmation：个人原始错因未记录；题面可确认的复做入口是先按移动分界点 \(t=x\) 分段去绝对值，再由 \(f^{\prime}(x)\)、\(f^{\prime\prime}(x)\) 判断单调与本题教材口径下的“凹”，真实第一错步待用户复做确认。 | absolute_integral_and_concavity_convention_verified |
| [GS-161](http://127.0.0.1:8765/open/GS-161) | 有理函数定积分计算 | 定积分、有理函数积分、部分分式、反正切型积分 | \(\displaystyle \frac{\pi+3\ln2}{10}\) | pending_user_confirmation：个人原始错因未记录；题面可确认的复做入口是先按“一次因式配常数、不可约二次因式配一次式”拆部分分式，再把二次项分子配成分母导数与常数，真实第一错步待用户复做确认。 | duplicate_identity_with_GS_278_held |
| [GS-162](http://127.0.0.1:8765/open/GS-162) | 三角有理式不定积分：凑微分转有理函数积分 | 不定积分、一元函数积分学的计算、三角函数有理式、三角恒等变形、第一类换元、整体凑微分、有理函数积分、部分分式、对数型积分、原函数按定义域连通区间分别理解 | \(\displaystyle \frac12\ln\left\|\frac{1-\cos x}{1+\cos x}\right\|+\frac{1}{2\sqrt2}\ln\left\|\frac{\sqrt2+\cos x}{\sqrt2-\cos x}\right\|+C\)；在每个 \((k\pi,(k+1)\pi)\) 上分别理解，积分常数可不同。 | confirmed_personal：看到 \(\int\frac{1}{\sin x+\sin^3x}\,dx\) 时，虽已想到提 \(\sin x\) 并凑 \(\sin x\,dx=-d(\cos x)\)，但把 \(1+\sin^2x\) 误写成 \(\cos^2x\)，且转成有理函数后混淆 \(a^2-x^2\) 公式中 \(a\) 与 \(\sqrt a\) 的角色。 | current_asset_mismatch_and_batch1_lineage_held |
| [GS-163](http://127.0.0.1:8765/open/GS-163) | 三角一次式比值的不定积分：常数项与分母导数拆分 | 不定积分、一元函数积分学的计算、三角函数有理式、原函数按定义域连通区间分别理解、部分分式、回代化简 | \(\frac45x-\frac35\ln\|\sin x+2\cos x\|+C\)；在 \(\sin x+2\cos x\ne0\) 的各个连通区间上分别理解，积分常数可不同。 | legacy_unclassified：历史解析称化 \(\tan x\) 时漏写 \(dx=\dfrac{dt}{1+t^2}\) 且反代未合并对数，但证据来源未分级；本轮补强更短的首选入口“分子拆成分母及其导数”，个人第一错步仍待确认。 | denominator_whole_derivative_split_promoted |
| [GS-164](http://127.0.0.1:8765/open/GS-164) | 一阶线性微分方程与法线截距最值 | 一阶线性微分方程、法线方程、单调性与极值 | \(\displaystyle y(x)=\frac13x^6+1,\quad P\left(1,\frac43\right)\) | pending_user_confirmation：暂无明确个人错因；题图与解析图只能确认正确动作链：先解一阶线性微分方程得到 \(y(x)\)，再把法线在 \(y\) 轴上的截距写成关于 \(x\) 的函数求最小值；“先盯法线截距”只是 pending 复做诊断候选。 | ode_normal_intercept_minimum_chain_verified |

## 逐题复核

### GS-144 1000题B组5.12

- 题目：函数满足 $xf''(x)+3x[f'(x)]^2=1-e^{-x}$，且 $f'(x_0)=0,x_0\ne0$，判断 $f(x_0)$ 的性质。
- 所问：二阶充分条件判断极值
- 知识点：一元函数微分学应用；单调性与极值；二阶导数判极值
- 第一动作：先把 x=x0 与 f'(x0)=0 代入原方程
- 答案：选 B：$f(x_0)$ 是 $f(x)$ 的极小值。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：个人原始错因未记录；题图只能确认客观入口是把 $x=x_0$ 与 $f^{\prime}(x_0)=0$ 代入方程，再判断 $\frac{1-e^{-x_0}}{x_0}>0$，不能据此反推用户当时漏了哪一步。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 把驻点条件代入微分方程，得到二阶导的显式比值。
  - 分别检查驻点横坐标为正、为负时分子与分母同号，故二阶导恒正。
- 质量发现：
  - `stationary_substitution_sign_chain_verified`：驻点代回方程和正负两侧符号链已核对。；建议：
- 关系裁决：
  - GS-156：`add_strong_edge`；
  - GS-537：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `ec1c1ff6e8345ddccb31985c055f347785bfc64b153e72704ff04c260e5da6a6`；唯一图片 1 个；物理路径 1 个。

### GS-145 1000题B组5.13

- 题目：由积分方程 \[ \int_0^{y(x)} e^{-\frac{t^2}{2}}\,dt=\frac13(\sqrt{x}-2)^2 \] 确定 \(y=y(x)\)，判断 \(y(x)\) 的极值点与极值。
- 所问：积分方程确定隐函数极值
- 知识点：一元函数微分学应用；变上限积分；隐函数求导；单调性与极值；隐函数实际定义域
- 第一动作：先对两边求导，左边写成 \(e^{-y^2/2}y'\)，右边写出 \(\frac{\sqrt{x}-2}{3\sqrt{x}}\) 这个链式因子。
- 答案：选择 B：只有极小值点 \(x=4\)，极小值为 \(0\)。
- 个人错因边界：confirmed_personal；用户确认对积分方程两边求导的方向正确，但右边 \(\frac13(\sqrt{x}-2)^2\) 求导时漏掉关键因子 \(\sqrt{x}-2\)，导致没有找到 \(x=4\)；同时把 \(x=0\) 当作候选，却未先检查左侧积分的值域，事实上 \(x=0\) 时方程无实数解。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 对变上限积分方程隐式求导，保留复合上限的链式因子。
  - 令 A=sqrt(pi/2)、c=sqrt(3A)，由积分函数值域得到实际定义域 ((2-c)^2,(2+c)^2)；两端开且 y 趋于正无穷。
  - 由导数在 x=4 两侧先负后正，确定 y(4)=0 是唯一全局最小值，并排除最大值。
- 质量发现：
  - `integral_exponent_domain_and_unique_minimum_repaired`：已修正指数误写，补足完整实际定义域、开端点行为、唯一全局最小值和无最大值结论。；建议：
- 关系裁决：
  - GS-464：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-527：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-538：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-145：`add_strong_edge`；
  - GS-243：`remove_broad_stale_or_identity_edge`；
  - GS-524：`remove_broad_stale_or_identity_edge`；
  - GS-537：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `7311055fe4eb992ebba05786b10fb0524e897ee343393f64acc6bc5393c10530`；唯一图片 1 个；物理路径 1 个。

### GS-146 1000题B组5.40

- 题目：已知 $f'(x)=(x^2-3x+a)e^x$，由“无极值点且有拐点”反推参数 $a$。
- 所问：导函数判别式反推参数范围
- 知识点：一元函数微分学应用；单调性与极值；凹凸性与拐点；参数范围
- 第一动作：先写出 e^x>0 并把 f' 的符号问题转给二次因子
- 答案：$a\in\left[\frac94,\frac{13}{4}\right)$
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：个人原始错因未记录；题图只能确认客观入口是先剥离正因子 $e^x$，再分别把“无极值点”和“有拐点”翻译为两个二次因子的判别式条件。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 剥离恒正因子 e^x，把一阶导与二阶导的符号问题分别转为二次式。
  - 无极值允许一阶导二次式重根不变号；有拐点要求二阶导二次式有两个相异实根，求条件交集。
- 质量发现：
  - `double_discriminant_boundary_verified`：无极值的重根边界与拐点的相异根条件已分离。；建议：
- 关系裁决：
  - GS-146：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-451：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `dd78817082c32389cf077e48883a486d0016af682b617137f1feb1b024a48a27`；唯一图片 1 个；物理路径 1 个。

### GS-148 2024年真题11

- 题目：曲线 \(y^2=x\) 在原点处的曲率圆方程。
- 所问：竖直切线处曲率圆
- 知识点：一元函数微分学应用；曲率；曲率圆；切线方程
- 第一动作：先把 \(y^2=x\) 改写成 \(x=y^2\)，用 \(x=x(y)\) 的曲率公式求 \(K(0)\)。
- 答案：\(\left(x-\frac12\right)^2+y^2=\frac14\)
- 个人错因边界：legacy_unclassified；legacy_unclassified：旧来源候选错因是把曲率公式固定理解为 \(y=y(x)\) 型；当前题图无用户作答。可确认的客观入口是把 \(y^2=x\) 改写为 \(x=y^2\)，用 \(x=x(y)\) 型曲率公式求半径并沿法线方向定圆心。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 将曲线改写为 x=y^2，使用 x=x(y) 型曲率公式。
  - 原点曲率为 2、半径为 1/2，再沿法线方向确定圆心。
- 质量发现：
  - `vertical_tangent_curvature_representation_verified`：已选择 x=x(y) 表示并核对曲率圆方向。；建议：
- 关系裁决：
  - GS-148：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-148：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-529：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-539：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-149：`remove_broad_stale_or_identity_edge`；
  - GS-538：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `070547ab9a687f1676709205749d7416ab39ca62665b4204a1d4645e3f3e5a39`；唯一图片 1 个；物理路径 1 个。

### GS-149 2019年数2（6） 二阶接触与曲率相等充分必要判断

- 题目：设函数 \(f(x),g(x)\) 的二阶导数在 \(x=a\) 处连续。判断条件 $$ \lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^2}=0 $$ 是否为两条曲线 \(y=f(x)\)、\(y=g(x)\) 在 \(x=a\) 对应点处相切且曲率相等的条件。
- 所问：曲率相等的充分必要判断
- 知识点：曲率；二阶接触；泰勒公式；充分必要条件判断
- 第一动作：先令 F=f-g 并写二阶 Taylor 展开
- 答案：A（充分不必要条件）
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；本轮依据题图与解析图补强可确认的题型入口：判断“\(\lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^2}=0\)”与“两曲线相切且曲率相等”的关系时，必须分充分性和必要性两向验证，不能把能推出曲率相等直接当成等价条件。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由二阶 Taylor 展开验证给定极限足以推出同点、同切线与同二阶导。
  - 用二次函数正负号相反的反例说明曲率相等只要求二阶导绝对值相等，因此条件不必要。
- 质量发现：
  - `necessity_counterexample_added`：已补充分不必要的二次函数反例。；建议：
- 关系裁决：
  - GS-529：`add_strong_edge`；
  - GS-149：`remove_broad_stale_or_identity_edge`；
  - GS-149：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `f4ea75e9697350ceeda1cc8d23e2e80282e35017155b74bc07760b080f9a254f`；唯一图片 2 个；物理路径 2 个。

### GS-150 强化例题5.7

- 题目：$g(x)$ 是 $f(x)=\frac12\ln\frac{3+x}{3-x}$ 的反函数，求曲线 $y=g(x)$ 的渐近线。
- 所问：反函数渐近线判断
- 知识点：一元函数微分学应用；反函数；渐近线；无穷远极限
- 第一动作：先解出 $g(x)=3\frac{e^{2x}-1}{e^{2x}+1}$，再分别算 $x\to+\infty$ 和 $x\to-\infty$ 的极限。
- 答案：$y=3$ 与 $y=-3$。由 $g(x)=3\frac{e^{2x}-1}{e^{2x}+1}=3\tanh x$ 得出。
- 个人错因边界：legacy_unclassified；legacy_unclassified：旧来源候选错因是只检查一个无穷远方向；当前题图无用户作答。客观上 $g(x)=3\tanh x$，必须分别检查 $x\to+\infty$ 与 $x\to-\infty$，得到两条水平渐近线。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 解出反函数 g(x)=3 tanh x。
  - 分别计算正负无穷方向极限，得到两条水平渐近线。
- 质量发现：
  - `both_infinity_directions_verified`：反函数两端水平渐近线均已核对。；建议：
- 关系裁决：
  - GS-151：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `86d75ebe5bfe25bf9dee2fa7bf01c2892f08b9c5065b4f346a642fb2e6e1f221`；唯一图片 1 个；物理路径 1 个。

### GS-151 1000题A组5.20

- 题目：$$ y = \frac{x^2 + 1}{\sqrt{x^2 - 1}} $$ 求渐近线的条数。
- 所问：渐近线条数判断
- 知识点：一元函数微分学应用；等价无穷小；泰勒展开；渐近线；极限与连续
- 第一动作：先由 $x^2-1>0$ 写出定义域 $(-\infty,-1)\cup(1,\infty)$，列出 $x=\pm1$、$x\to+\infty$、$x\to-\infty$ 四个检查点。
- 答案：(A) 4
- 个人错因边界：legacy_unclassified；legacy_unclassified：旧来源候选错因是没有把定义域端点、$x\to+\infty$、$x\to-\infty$ 列成完整检查清单；当前题图无用户作答，具体个人错步待复做确认。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先由根号内正值确定定义域，并检查两个有限端点。
  - 再分别计算正无穷和负无穷方向的斜渐近线，合计四条。
- 质量发现：
  - `complete_asymptote_checklist_verified`：有限端点与正负无穷方向已完整检查。；建议：
- 关系裁决：
  - GS-151：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-500：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-151：`add_strong_edge`；
  - GS-158：`add_strong_edge`；
  - GS-151：`remove_broad_stale_or_identity_edge`；
  - GS-459：`remove_broad_stale_or_identity_edge`；
  - GS-460：`remove_broad_stale_or_identity_edge`；
  - GS-497：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `be8b83b40693e8972129e756f63cb6cf8ee9a0895528a0d0ee09c56b7a5f3fb3`；唯一图片 1 个；物理路径 1 个。

### GS-152 1000题B组17题

- 题目：曲线 $r(3\theta-\pi)=1$，求其斜渐近线。该题面来自既有正式卡摘要，不是由当前 `GS-152/question_01.png` 转写；该图片属于另一道积分中值定理题，不能作为本题题图证据。
- 所问：极坐标曲线斜渐近线
- 知识点：一元函数微分学应用；极限与连续；渐近线；极坐标
- 第一动作：先求使 r 趋于无穷的角度方向
- 答案：$$\boxed{y=\sqrt3x+\frac23}$$
令 $\alpha=\frac\pi3$，当 $\theta\to\alpha$ 时 $r\to\infty$，且
$$r\sin(\theta-\alpha)\to\frac13.$$
故斜渐近线满足 $-x\sin\alpha+y\cos\alpha=\frac13$，化简得 $y=\sqrt3x+\frac23$。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧正式卡只保留极坐标题摘要，暂无用户原始作答过程；当前路径下的 question_01.png 实际属于另一道积分中值定理题，禁止据此补写本题题面、答案或个人错因。
- 一致性：题图—解析 —；正式卡—图片 mismatch_blocked
- 解析主线：
  - 由正式卡摘要找使 r 趋于无穷的角度方向，再用极坐标直线距离极限求截距。
  - 当前图片属于另一道积分中值定理题，只用于证明错配，不能支撑正式题面或个人错因。
- 质量发现：
  - `formal_visual_mismatch_held`：正式极坐标题与积分中值定理图片不一致。；建议：
- 关系裁决：
  - GS-459：`remove_broad_stale_or_identity_edge`；
  - ：`hold_without_merge_delete_or_aggregate_edge`；
- 当前快照：`stale`；正式卡 `ee49da01474e2dedf57ca5137d4f3e3962ce0b8ff6851a65e965827e3420d045`；唯一图片 0 个；物理路径 0 个。

### GS-153 1000题B组5.34

- 题目：设 $n$ 为正整数，讨论 $f(x)=x^ne^{-x}$ 的单调性和全局最值。
- 所问：幂乘指数函数单调性与最值分类讨论
- 知识点：一元函数微分学应用；单调性与极值；参数分类讨论；无穷远极限
- 第一动作：先求导并写出 f'(x)=x^{n-1}e^{-x}(n-x)
- 答案：$n=1$：$(-\infty,1)$ 增、$(1,+\infty)$ 减，最大值 $e^{-1}$，无最小值；$n\ge3$ 奇数：$(-\infty,n)$ 增、$(n,+\infty)$ 减，最大值 $n^ne^{-n}$，无最小值；$n\ge2$ 偶数：$(-\infty,0)$ 减、$(0,n)$ 增、$(n,+\infty)$ 减，最小值 $0$，无最大值。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：个人原始错因未记录；题图只能确认客观入口是先求导得到 $x^{n-1}e^{-x}(n-x)$，再按 $n=1$、奇数 $n\ge3$、偶数 $n\ge2$ 分类并检查两端极限。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 求导并提取恒正因子，将符号交给 x 的幂次与 n-x。
  - 按 n=1、奇数 n 大于等于 3、偶数 n 大于等于 2 分类，并结合两端极限判断全局最值。
- 质量发现：
  - `parity_classification_and_endpoint_limits_verified`：参数奇偶分类和两端极限已核对。；建议：
- 当前快照：`stale`；正式卡 `eafde3c7561102f5ad1b267ff0dfe01fbaf401985ebbfaf7ddf0f172f921f583`；唯一图片 1 个；物理路径 1 个。

### GS-154 1000题A5.6

- 题目：设 \(f(x)>0\) 且 \(f\) 二阶可导。曲线 $y=\sqrt{f(x)}$ 在 $(1,\sqrt2)$ 有拐点，且 $f'(1)=2$，求 $f''(1)$。
- 所问：复合函数二阶导与拐点条件
- 知识点：一元函数微分学应用；复合函数求导；高阶导数；凹凸性与拐点
- 第一动作：先写 $y^{\prime}=\frac{f^{\prime}(x)}{2\sqrt{f(x)}}$，再把常数 $1/2$ 提出后对 $f^{\prime}(x)(f(x))^{-1/2}$ 求导。
- 答案：$f^{\prime\prime}(1)=1$
- 个人错因边界：legacy_unclassified；legacy_unclassified：旧来源候选错因是对 $y=\sqrt{f(x)}$ 求二阶导时误处理常数因子 $1/2$；当前题图无用户作答。客观入口是先提出 $1/2$，再对 $f^{\prime}(x)f(x)^{-1/2}$ 用乘积与链式法则。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 在 f(x)>0 且 f 二阶可导的题设下，由点坐标先得 f(1)=2，再对 y=sqrt(f(x)) 求二阶导。
  - 只使用拐点在上述条件下给出的必要条件 y''(1)=0；代入 f(1)、f'(1) 后解得 f''(1)=1，不能反向把 y''(1)=0 当作拐点充分条件。
- 质量发现：
  - `composite_second_derivative_factor_verified`：根式复合二阶导的常数因子与代值链已核对。；建议：
- 当前快照：`stale`；正式卡 `9b1b802d7dca1d8133d06e18e0f6e02fdc904c4e8e214ce1e00db1d71742aec7`；唯一图片 1 个；物理路径 1 个。

### GS-155 1000题A5.14

- 题目：设 \(f(x)=n^2e^{x/n}-(1+n)x\)，已知在 \(x=\xi_n\) 处取极值，求 \(\lim_{n\to\infty}\xi_n\)。
- 所问：极值点方程与数列极限
- 知识点：一元函数微分学应用；单调性与极值；对数重要极限；数列极限
- 第一动作：先求 f'(x) 并令 f'(\(\xi_n\))=0 解出 \(\xi_n\)
- 答案：\(\lim_{n\to\infty}\xi_n=1\)
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；以下仅能确认复做入口：先由极值条件解出 \(\xi_n=n\ln(1+1/n)\)，再转成对数重要极限，真实第一错步待用户复做确认。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由极值必要条件解出 xi_n=n ln(1+1/n)。
  - 调用对数重要极限得到数列极限为 1。
- 质量发现：
  - `extreme_point_log_limit_chain_verified`：极值点方程与对数重要极限已核对。；建议：
- 关系裁决：
  - GS-159：`remove_broad_stale_or_identity_edge`；
  - GS-160：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `6ba63c3b2cc2e6daf1f209a66d20bc03fa8c603e911169d3ee068ce9cd65593d`；唯一图片 1 个；物理路径 1 个。

### GS-156 1000题A组5.15

- 题目：函数满足 \(xf^{\prime\prime}(x)+5x^2[f^{\prime}(x)]^2=2(1-e^{-x})\)，判断 \(x=\alpha\ne0\) 与 \(x=0\) 处极值类型。
- 所问：由微分方程判极值类型
- 知识点：一元函数微分学应用；单调性与极值；微分方程
- 第一动作：先按 \(\alpha>0\) 与 \(\alpha<0\) 分别判断分子、分母符号。
- 答案：(1) 极小值；(2) 极小值。
- 个人错因边界：legacy_unclassified；历史折叠解析把错步定位为 \(\alpha<0\) 时没有合并检查 \(1-e^{-\alpha}\) 与分母 \(\alpha\) 的符号，但缺少可追溯原始作答，暂按 legacy_unclassified 保留，不能视为本轮已确认个人错因。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 在非零驻点把 f'(alpha)=0 代回微分方程，合并判断比值符号。
  - 在 x=0 处先由极值必要条件得 f'(0)=0；再求穿孔极限，并对 f' 使用拉格朗日中值定理推出 f''(0)=2。
- 质量发现：
  - `zero_point_and_nonzero_stationary_boundaries_verified`：非零驻点符号链已核对；零点处已用拉格朗日中值定理补上从穿孔极限到 f''(0)=2 的严格闭合。；建议：
- 关系裁决：
  - GS-156：`add_strong_edge`；
  - GS-537：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `908add681ad275a5cf8a04bcc126c5455a4b4f50623fd95dc557f930bcf1dcd7`；唯一图片 1 个；物理路径 1 个。

### GS-157 1000题B组5.8

- 题目：求 \(f(x)=\int_1^x (x^2-t^2)\ln(1+t^2)\,dt\) 的极值。
- 所问：含参变上限积分极值
- 知识点：定积分；变上限积分；分部积分；单调性与极值
- 第一动作：先对 f(x) 求导，拆出上限项和参数偏导项
- 答案：极大值为 \(f(0)=\frac13\ln2+\frac49-\frac\pi6\)，极小值为 \(f(1)=0\)。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；题面可确认的复做入口是先对含参变上限积分使用莱布尼茨公式求导，再判两个驻点并回代求极值，真实第一错步待用户复做确认。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 用莱布尼茨公式同时处理上限项与被积函数中的参数。
  - 由导数符号找驻点并用分部积分计算相应函数值，区分极大值和极小值。
- 质量发现：
  - `oriented_integral_sign_and_extrema_repaired`：旧解析关于积分零点的论证已修复。；建议：
- 关系裁决：
  - GS-159：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-283：`remove_broad_stale_or_identity_edge`；
  - GS-332：`remove_broad_stale_or_identity_edge`；
  - GS-336：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `a157b4c239936a1bfa3478761e42baa6a4ddf54c019dec065533c7a7bb0ecb5b`；唯一图片 1 个；物理路径 1 个。

### GS-158 1000题B组5.15

- 题目：计算 \(b=\lim_{x\to-\infty}\left(\frac{\sqrt{x^2-x+1}}{e^x-1}-x\right)\)。
- 所问：无穷远根式极限
- 知识点：极限与连续；函数极限；无穷远根式极限；指数衰减
- 第一动作：先把 \(\sqrt{x^2-x+1}\) 写成 \(-x\sqrt{1-1/x+1/x^2}\)
- 答案：\(b=-\frac12\)
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；题面可确认的复做入口是先处理 \(x\to-\infty\) 下 \(\sqrt{x^2-x+1}=-x\sqrt{1-1/x+1/x^2}\) 的符号，再保留根式一阶小量与 \(xe^x\to0\)，真实第一错步待用户复做确认。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 在负无穷方向先写 sqrt(x^2)=-x，避免主量符号错误。
  - 精确有理化根式余项，并用 x e^x 趋于 0 收口。
- 质量发现：
  - `negative_infinity_rationalization_sign_repaired`：旧解析通分负号已修复。；建议：
- 关系裁决：
  - GS-158：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `f09e02a70e91cfc50ba16f60a287cacb29a4f9ab7a49af79f54ec3dd22fc67fc`；唯一图片 1 个；物理路径 1 个。

### GS-159 1000题B组5.23

- 题目：求 \(f(x)=\int_0^x e^{-t}\cos t\,dt\) 在 \([0,\pi]\) 上的最大值。
- 所问：变上限积分最值
- 知识点：定积分；变上限积分；单调性与极值
- 第一动作：先写出 \(f'(x)=e^{-x}\cos x\) 并找临界点
- 答案：最大值为 \(\frac{1+e^{-\pi/2}}{2}\)。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；题面可确认的复做入口是由 \(f^{\prime}(x)=e^{-x}\cos x\) 作完整符号表，确定闭区间最大点后再计算积分值，真实第一错步待用户复做确认。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由变上限积分求导得到 e^{-x} cos x，列闭区间符号表。
  - 比较驻点与端点函数值，最大值在 pi/2 处取得。
- 质量发现：
  - `closed_interval_extremum_chain_verified`：闭区间驻点和端点比较链已核对。；建议：
- 关系裁决：
  - GS-159：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-159：`remove_broad_stale_or_identity_edge`；
  - GS-160：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `08d43df65eb993ac45a342e56363cfa3ef45268be07cb04cd75cc730683d41f2`；唯一图片 1 个；物理路径 1 个。

### GS-160 1000题B组5.7

- 题目：设 \(f(x)=\int_0^1 |t(t-x)|\,dt\ (0<x<1)\)，判断单调区间和凹凸性。
- 所问：绝对值定积分单调凹凸判别
- 知识点：定积分；绝对值分类；单调性与极值；凹凸性判定
- 第一动作：在 \(t\in[0,1]\) 且 \(0<x<1\) 时，只需以内部符号分界点 \(t=x\) 拆成 \([0,x]\) 与 \([x,1]\)
- 答案：\(\boxed{A}\)：在 \((0,\frac{\sqrt2}{2})\) 上单调减少，在 \((\frac{\sqrt2}{2},1)\) 上单调增加，且按本题教材术语曲线为凹。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；题面可确认的复做入口是先按移动分界点 \(t=x\) 分段去绝对值，再由 \(f^{\prime}(x)\)、\(f^{\prime\prime}(x)\) 判断单调与本题教材口径下的“凹”，真实第一错步待用户复做确认。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 把 t 作为积分变量并按移动分界点 t=x 分段去绝对值。
  - 写出显式函数后求一阶、二阶导，按题目教材口径判断单调与凹凸。
- 质量发现：
  - `absolute_integral_and_concavity_convention_verified`：分段积分和教材凹凸术语已核对。；建议：
- 关系裁决：
  - GS-288：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-638：`add_strong_edge`；
  - GS-160：`remove_broad_stale_or_identity_edge`；
  - GS-160：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `1d3a35f2799d88f1188fa598405024a16a66cb0e986589409f5a40e69cc0f9c9`；唯一图片 1 个；物理路径 1 个。

### GS-161 强化例题9.10（171530）

- 题目：身份边界：GS-161 与 GS-278 的题目、积分区间、方法和答案完全一致，仅来源标签与图片渲染不同。两张卡保留稳定 ID，不合并、不删除；GS-161—GS-278 当前是 `duplicate_identity_hold`，聚合策略为 `block_until_relinked`，不能当作普通 `related` 强边解释。 计算 \(\int_0^1 \frac{dx}{(x+1)(x^2-2x+2)}\)。
- 所问：有理函数定积分计算
- 知识点：定积分；有理函数积分；部分分式；反正切型积分
- 第一动作：先设 \(\frac{A}{x+1}+\frac{Bx+C}{x^2-2x+2}\) 并求系数
- 答案：\(\displaystyle \frac{\pi+3\ln2}{10}\)
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；题面可确认的复做入口是先按“一次因式配常数、不可约二次因式配一次式”拆部分分式，再把二次项分子配成分母导数与常数，真实第一错步待用户复做确认。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 按一次因式配常数、不可约二次因式配一次式作部分分式。
  - 分别积分对数项和反正切项并代上下限；同时与 GS-278 保持重复身份冻结。
- 质量发现：
  - `duplicate_identity_with_GS_278_held`：与 GS-278 为同题，仅来源标签和渲染不同。；建议：
- 关系裁决：
  - GS-174：`remove_broad_stale_or_identity_edge`；
  - GS-278：`remove_broad_stale_or_identity_edge`；
  - ：`hold_without_merge_delete_or_aggregate_edge`；
- 当前快照：`stale`；正式卡 `b631e2f1dae2b9acb3149016826aad677203f7d55f1a17054d9b876946afabea`；唯一图片 1 个；物理路径 1 个。

### GS-162 强化例题9.11（135747）三角有理式换元

- 题目：视觉身份说明：GS-162 当前目录下的 `question_01.png` 实为 \(\int\sin^5x/\cos^4x\,dx\)，与本卡正式题面不符，不能作为证据。本题题面与解答图沿用第 1 批已复核的 GS-280 历史 lineage；不合并或删除任何 ID，也不把该历史资产重复计入本批。 计算不定积分 \[ \int \frac{1}{\sin x+\sin^3x}\,dx. \]
- 所问：三角有理式不定积分：凑微分转有理函数积分
- 知识点：不定积分；一元函数积分学的计算；三角函数有理式；三角恒等变形；第一类换元；整体凑微分；有理函数积分；部分分式；对数型积分；原函数按定义域连通区间分别理解
- 第一动作：先写成 \(\frac{1}{\sin x(1+\sin^2x)}\)，再乘 \(\frac{\sin x}{\sin x}\)，凑 \(\sin x\,dx=-d(\cos x)\)。
- 答案：\(\displaystyle \frac12\ln\left|\frac{1-\cos x}{1+\cos x}\right|+\frac{1}{2\sqrt2}\ln\left|\frac{\sqrt2+\cos x}{\sqrt2-\cos x}\right|+C\)；在每个 \((k\pi,(k+1)\pi)\) 上分别理解，积分常数可不同。
- 个人错因边界：confirmed_personal；看到 \(\int\frac{1}{\sin x+\sin^3x}\,dx\) 时，虽已想到提 \(\sin x\) 并凑 \(\sin x\,dx=-d(\cos x)\)，但把 \(1+\sin^2x\) 误写成 \(\cos^2x\)，且转成有理函数后混淆 \(a^2-x^2\) 公式中 \(a\) 与 \(\sqrt a\) 的角色。
- 一致性：题图—解析 —；正式卡—图片 current_asset_mismatch_blocked
- 解析主线：
  - 提取 sin x 并乘入 sin x，以 u=cos x 整体凑微分。
  - 化为有理函数后部分分式积分；当前错配图片排除，正式视觉证据沿用第1批 GS-280 lineage。
- 质量发现：
  - `current_asset_mismatch_and_batch1_lineage_held`：当前图片错配；正式题视觉沿用已复核 GS-280 lineage。；建议：
- 关系裁决：
  - GS-267：`remove_broad_stale_or_identity_edge`；
  - GS-280：`remove_broad_stale_or_identity_edge`；
  - ：`hold_without_merge_delete_or_aggregate_edge`；
- 当前快照：`stale`；正式卡 `340df107ea0d6373c1a55c0744bbe19038fe741f0b8308c2d88268fe654ba88b`；唯一图片 1 个；物理路径 1 个。

### GS-163 强化例题9.13（135756）

- 题目：计算 $$ \int\frac{2\sin x+\cos x}{\sin x+2\cos x}\,dx. $$
- 所问：三角一次式比值的不定积分：常数项与分母导数拆分
- 知识点：不定积分；一元函数积分学的计算；三角函数有理式；原函数按定义域连通区间分别理解；部分分式；回代化简
- 第一动作：令 \(D=\sin x+2\cos x\)，先解 \(2\sin x+\cos x=A D+B D'\)，得到 \(A=4/5, B=-3/5\)。
- 答案：\(\frac45x-\frac35\ln|\sin x+2\cos x|+C\)；在 \(\sin x+2\cos x\ne0\) 的各个连通区间上分别理解，积分常数可不同。
- 个人错因边界：legacy_unclassified；历史解析称化 \(\tan x\) 时漏写 \(dx=\dfrac{dt}{1+t^2}\) 且反代未合并对数，但证据来源未分级；本轮补强更短的首选入口“分子拆成分母及其导数”，个人第一错步仍待确认。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 令 F=sin x+2 cos x 并计算 F'。
  - 将分子写成 4F/5-3F'/5，直接得到常数项与对数导数项；化 tan x 只在 cos x 不等于 0 的局部区间作为备选。
- 质量发现：
  - `denominator_whole_derivative_split_promoted`：分母整体与导数拆分已提升为首选入口，并补足分母非零与分区间积分常数边界。；建议：
- 关系裁决：
  - GS-623：`add_strong_edge`；
  - GS-603：`remove_broad_stale_or_identity_edge`；
  - GS-633：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `270be304665126743059709301a889cc7637bd3ffaeb8d0750a811a670560808`；唯一图片 1 个；物理路径 1 个。

### GS-164 2021年第20题

- 题目：设 \(y=y(x)\ (x>0)\) 满足 $$ xy'-6y=-6,\qquad y(\sqrt3)=10. $$ 1. 求 \(y(x)\)。 2. 设 \(P\) 为曲线 \(y=y(x)\) 上一点，曲线在 \(P\) 处的法线在 \(y\) 轴上的截距为 \(I_P\)。当 \(I_P\) 最小时，求点 \(P\) 的坐标。
- 所问：一阶线性微分方程与法线截距最值
- 知识点：一阶线性微分方程；法线方程；单调性与极值
- 第一动作：先把微分方程化为一阶线性标准型并解出 y(x)
- 答案：\(\displaystyle y(x)=\frac13x^6+1,\quad P\left(1,\frac43\right)\)
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；题图与解析图只能确认正确动作链：先解一阶线性微分方程得到 \(y(x)\)，再把法线在 \(y\) 轴上的截距写成关于 \(x\) 的函数求最小值；“先盯法线截距”只是 pending 复做诊断候选。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先用积分因子解一阶线性微分方程并由初值确定常数。
  - 写出法线 y 轴截距的单变量函数；由导数在 x=1 两侧先负后正闭合唯一全局最小点，再回代曲线。
- 质量发现：
  - `ode_normal_intercept_minimum_chain_verified`：微分方程、法线截距和最值全链已核对。；建议：
- 关系裁决：
  - GS-164：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-190：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-191：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-203：`remove_broad_stale_or_identity_edge`；
- 当前快照：`stale`；正式卡 `c0afc384841f5efa198cbcf3888f9d3f9290e622d2579d10f11426f83e749726`；唯一图片 2 个；物理路径 2 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
