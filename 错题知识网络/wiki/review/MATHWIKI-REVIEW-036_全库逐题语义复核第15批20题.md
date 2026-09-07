---
wiki_id: MATHWIKI-REVIEW-036
type: target_level_semantic_review_batch
title: 全库逐题语义复核第15批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-036_全库逐题语义复核第15批20题.json
status: active
last_updated: 2026-07-23
---

# 全库逐题语义复核第15批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 0 张；覆盖 27 个物理图片路径与 25 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 20 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `MATH-TARGET-SEMANTIC-CLOSEOUT-20260723-B15`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-123](http://127.0.0.1:8765/open/GS-123) | 求指定参数点处二阶导数 | 参数方程求导、高阶导数 | \(\displaystyle \frac{2}{3}\) | pending_user_confirmation：暂无明确个人错因：旧卡未记录作答过程；可确认的题型风险是，参数方程求二阶导时容易把对 t 求导误当成对 x 求导，漏掉再除以 x'(t) 这一层链式求导。 | parameter_second_derivative_chain_and_solution_evidence_boundary_verified |
| [GS-124](http://127.0.0.1:8765/open/GS-124) | 求反函数在指定自变量处的二阶导数 | 一元函数微分学应用、反函数求导 | $g^{\prime\prime}(2)=-\dfrac{1}{27}$。 | legacy_unclassified：旧视觉详情的来源叙述称，推导出 $g^{\prime\prime}(y)=-\frac{f^{\prime\prime}(x)}{(f^{\prime}(x))^3}$ 后曾把反函数自变量 $y=2$ 当成原函数自变量 $x=2$；当前题图未显示该作答，故仅作为待用户确认的历史错因，正确入口仍是先解 $f(x)=2$。 | inverse_second_derivative_corresponding_point_and_legacy_evidence_downgraded |
| [GS-125](http://127.0.0.1:8765/open/GS-125) | 求满足积分方程的原函数表达式 | 定积分、变上限积分 | $f(x)=2x-1$。 | pending_user_confirmation：已于 2026-06-02 复做正确并标记掌握；本轮依据题图与折叠解析确认复做入口：对变上限积分方程两边求导，把积分方程转成 $g(f(x))f^{\prime}(x)=2x$，再利用反函数关系收口。 | variable_upper_limit_inverse_initial_value_chain_repaired |
| [GS-126](http://127.0.0.1:8765/open/GS-126) | 求反函数表达式及定义域 | 反函数构造、有理化、单调性与值域 | $f^{-1}(x)=\dfrac12(e^x-e^{-x})$，定义域为 $(-\infty,+\infty)$。 | legacy_unclassified：旧视觉详情的来源叙述称，取指数得到 $e^y=x+\sqrt{x^2+1}$ 后曾未继续构造 $e^{-y}=\sqrt{x^2+1}-x$ 来消根号；当前题图未显示该作答，故仅作为待用户确认的历史错因。 | inverse_construction_tags_and_weak_edges_repaired |
| [GS-127](http://127.0.0.1:8765/open/GS-127) | 计算切线截距参与的极限 | 一元函数微分学应用、导数定义、切线方程、极限与连续、导数几何意义 | \boxed{1} | user_confirmed：正式错误事件的首个断点是没有把“切线在 x 轴上的截距”翻译成 \(u=x-\frac{f(x)}{f'(x)}\)。睡前独立诊断中这一步已经能完成，当前断点后移到证明 \(u\to0\)：把“\(u\) 与 \(x\) 同趋于 0”误说成 \(u=x\)，并漏写由一阶导数连续得到 \(f'(x)\to1\) 的条件。 | user_confirmed_intercept_chain_and_lhopital_error_edge_verified |
| [GS-128](http://127.0.0.1:8765/open/GS-128) | 求指定点处法线斜率 | 隐函数求导、法线方程 | \(\displaystyle -\frac{11}{9}\) | pending_user_confirmation：暂无明确个人错因；本轮依据题图与解析图补强可确认的题型入口：隐函数曲线在指定 \(x\) 处求法线斜率时，先代 \(x=1\) 解出对应点 \((1,1)\)，再隐函数求导得到切线斜率，最后取负倒数作为法线斜率。 | implicit_normal_unique_point_justification_repaired |
| [GS-129](http://127.0.0.1:8765/open/GS-129) | 分段写出各单调区间上的反函数 | 函数单调性、反函数、反三角函数主值、三角函数 | 在 \((0,\frac\pi2]\)、\([\frac\pi2,\frac{3\pi}2]\)、\([\frac{3\pi}2,2\pi)\) 三个单调区间上分别写 \(x=\arcsin y\)、\(x=\pi-\arcsin y\)、\(x=2\pi+\arcsin y\)，对应值域分别为 \((0,1]\)、\([-1,1]\)、\([-1,0)\)。 | legacy_unclassified：旧视觉详情的来源叙述称曾未先按 \(\sin x\) 在 \(0<x<2\pi\) 上的单调区间分段并写清每段值域，且反解时混淆变量角色与主值范围；当前题图未显示该作答，故仅作为待用户确认的历史错因。 | open_domain_and_inverse_branch_ranges_repaired |
| [GS-130](http://127.0.0.1:8765/open/GS-130) | 证明目标函数的单调不减性并辨析严格性 | 一元函数微分学应用、单调性与极值 | $F(x)=f(x)+x$ 在 $(-a,a)$ 上单调不减。 | pending_user_confirmation：个人原始错因未记录；本轮依据题图与折叠解析确认复做入口：题目没有给可导条件，不能硬用导数法；应任取 $x_1<x_2$，按单调定义把题设配成 $F(x_1)\le F(x_2)$。 | nonstrict_monotonicity_boundary_and_zero_degree_verified |
| [GS-131](http://127.0.0.1:8765/open/GS-131) | 求使极值点位于负半轴的参数范围 | 一元函数微分学应用、单调性与极值、参数分类讨论、对数函数性质 | $a\in(-\infty,-e)$ | legacy_unclassified：旧视觉详情的来源叙述称，处理含参数极值点位置时曾未先按 $a>0,a=0,a<0$ 分类，并漏查 $\ln(-e/a)$ 的定义域、符号和不等号方向；当前题图未显示该作答，故仅作为待用户确认的历史错因。 | parameter_sign_log_domain_and_chapter_repaired |
| [GS-132](http://127.0.0.1:8765/open/GS-132) | 判断分界点的可导性与极值性质 | 一元函数微分学应用、极值定义、分段函数连续可导、不可导点判别 | 选 B：$x=0$ 是不可导点，也是 $f(x)$ 的极大值点。 | legacy_unclassified：旧视觉详情的来源叙述称，曾把“极大值点”误按“全局最大值点”理解；当前题图未显示该作答，故仅作为待确认历史错因。数学上，右支 $x\ln x$ 在 $x\to+\infty$ 时无上界，所以函数无全局最大值；存在 $x>1$ 使函数值大于 0 只足以说明 $x=0$ 不是全局最大点，不影响其局部极大性质。 | local_extreme_and_unbounded_global_maximum_boundary_repaired |
| [GS-133](http://127.0.0.1:8765/open/GS-133) | 求闭区间最大值及其随 n 的极限 | 一元函数微分学应用、单调性与极值、极限与连续 | 最大值点为 \(x=\frac{1}{n+1}\)，最大值 \(M(n)=\left(\frac{n}{n+1}\right)^{n+1}\)，且 \(\lim_{n\to\infty}M(n)=e^{-1}\)。 | legacy_unclassified：历史来源记录了两次不同错误：第一次把最大值点的极限误当成最大值的极限，第二次未完整执行“内部驻点 + 端点值比较”流程。当前题图未显示用户作答，故两次记录均保留但归为待确认历史错因。 | closed_interval_endpoint_not_stationary_and_alias_verified |
| [GS-134](http://127.0.0.1:8765/open/GS-134) | 求参数函数最大值并证明不等式 | 一元函数微分学应用、单调性与极值、对数不等式、不等式证明 | (1) 最大值为 $\frac{a-1}{e\ln a}$，在 $x=-\frac1{\ln a}$ 处取得；(2) 对 $x>0,0<y<1$ 有 $xy^x(1-y)<\frac1e$。 | legacy_unclassified：旧来源解析叙述的候选错因：第二问可能没有把 $y$ 当固定参数复用第一问最大值结论，并可能遗漏除以 $\ln y<0$ 时不等号变向；当前题图不含用户作答，不能视为图像证实。 | fixed_parameter_maximum_and_negative_log_direction_verified |
| [GS-135](http://127.0.0.1:8765/open/GS-135) | 求恒成立不等式的参数范围 | 一元函数微分学应用、单调性与极值、恒成立不等式、参数范围 | $a\in\left[\frac{8\sqrt2}{3},+\infty\right)$ | legacy_unclassified：旧来源解析叙述的候选错因：分离参数后可能没有触发“$a\ge f(x)$ 对一切 $x>0$ 成立等价于 $a\ge \max_{x>0}f(x)$”的动作；当前题图不能独立证实该个人错因。 | universal_parameter_inequality_mastery_evidence_separated |
| [GS-136](http://127.0.0.1:8765/open/GS-136) | 求负半轴恒成立不等式的参数范围 | 一元函数微分学应用、单调性与极值、恒成立不等式、重要极限 | $a\in\left[-\frac12,+\infty\right)$ | pending_user_confirmation：个人原始错因未记录；本轮确认复做入口是先在 $x<0$ 下分离参数，除以 $2x<0$ 时必须变号，再求右侧辅助函数在 $(-\infty,0)$ 上的上确界。 | decreasing_supremum_endpoint_direction_repaired |
| [GS-138](http://127.0.0.1:8765/open/GS-138) | 判断极值、拐点与经典二次 Taylor 多项式命题的必然性 | 极限与连续、等价无穷小、Peano 余项、Peano 主部与经典 Taylor 多项式的边界、导数定义、单调性与极值、凹凸性与拐点、一元函数微分学应用 | A（0 项） | legacy_unclassified：旧来源候选错因是把函数等价 \(f(x)\sim\frac12x^2\) 当成可直接求导的等价；当前可确认的数学边界是题设仅推出 \(f(0)=0\) 与 \(f(x)=\frac12x^2+o(x^2)\)，不能推出经典二阶导数或经典二次 Taylor 多项式存在。 | incorrect_answer_and_peano_taylor_boundary_repaired |
| [GS-139](http://127.0.0.1:8765/open/GS-139) | 根据导函数图像判断原函数拐点个数 | 凹凸性与拐点、二阶导数判凹凸性 | 选 B，拐点个数为 2 | pending_user_confirmation：暂无明确个人错因；本轮依据题图与解析修复题型定位：本题核心是由 \(f'(x)\) 的图像判断 \(f(x)\) 的拐点，不能只看 \(f'(x)=0\)，而要看 \(f'\) 的单调性是否发生改变。 | derivative_graph_inflection_and_solution_evidence_boundary_verified |
| [GS-140](http://127.0.0.1:8765/open/GS-140) | 判断曲线拐点个数 | 一元函数微分学应用、凹凸性与拐点、二阶导数判凹凸性 | 选 C：拐点个数为 3。候选横坐标为 $-\sqrt3,0,\sqrt3$，且二阶导在三点均变号。 | legacy_unclassified：旧来源解析叙述的候选错因：二阶导整理时可能没有完整保留因式 $x(x^2-3)$，并可能混淆“凹凸性改变”与“一阶导变号”；当前题图不含用户作答，不能视为图像证实。 | second_derivative_factorization_and_counterexample_derivative_order_repaired |
| [GS-141](http://127.0.0.1:8765/open/GS-141) | 求同时满足无极值点且有拐点的参数范围 | 一元函数微分学应用、单调性与极值、凹凸性与拐点、参数范围 | $a\in[1,2)$ | legacy_unclassified：旧来源解析叙述的候选错因：可能没有把“没有极值点”和“有拐点”分别转成两个二次因子的符号条件；当前题图不含用户作答。对本题而言，无极值等价于 $q(x)\ge0$，有拐点等价于 $r(x)$ 有两个相异实根并变号。 | question_formula_and_discriminant_boundaries_repaired |
| [GS-142](http://127.0.0.1:8765/open/GS-142) | 判断点态导数与邻域性质的四个命题 | 函数单调性、导函数连续性、连续函数局部保号性、局部凹凸性 | B | pending_user_confirmation：暂无明确个人错因；本轮依据题图与解析修复题型定位：本题核心是区分“邻域内的单调/凹凸性质”和“点处导数值”，真命题用导数连续性与保号性证明，假命题用反例排除。 | pointwise_neighborhood_continuity_boundary_tags_repaired |
| [GS-143](http://127.0.0.1:8765/open/GS-143) | 求隐式曲线在指定点处的曲率 | 一元函数微分学应用、曲率、隐函数求导、高阶导数 | $$ k = \tfrac{3\sqrt{2}}{2} $$ | legacy_unclassified：旧来源解析叙述的候选错因是未先触发隐函数求导或曲率公式调用；当前题图不含用户推导。可确认的标准入口是由 \(x^2-xy+y^2=1\) 连续求出 \(y'\)、\(y''\)，再代入 \(K=\frac{\|y''\|}{(1+(y')^2)^{3/2}}\)。 | implicit_curve_curvature_and_source_evidence_boundary_repaired |

## 逐题复核

### GS-123 2021年第12题 参数方程二阶导链式求导

- 题目：参数方程确定 \(y=y(x)\)： $$ \begin{cases} x=2e^t+t+1,\\ y=4(t-1)e^t+t^2. \end{cases} $$ 求 $$ \left.\frac{d^2y}{dx^2}\right|_{t=0}. $$
- 所问：求指定参数点处二阶导数
- 知识点：参数方程求导；高阶导数
- 第一动作：先求 dy/dx=(dy/dt)/(dx/dt) 并尽量化简
- 答案：\(\displaystyle \frac{2}{3}\)
- 个人错因边界：pending_user_confirmation；暂无明确个人错因：旧卡未记录作答过程；可确认的题型风险是，参数方程求二阶导时容易把对 t 求导误当成对 x 求导，漏掉再除以 x'(t) 这一层链式求导。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 分别求参数导数 x′(t)、y′(t)。
  - 先化简 dy/dx，再对参数求导并除以 x′(t)。
  - 代入 t=0 得二阶导数。
- 质量发现：
  - `parameter_second_derivative_chain_and_solution_evidence_boundary_verified`：已核对参数方程二阶导链条与独立解析图，并把解析证据和个人错因证据分层。；建议：
- 关系裁决：
  - GS-650：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-169：`remove_broad_stale_or_weak_edge`；
  - GS-499：`remove_broad_stale_or_weak_edge`；
  - GS-579：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `6a80ec21e4935f0919d4d81dec97d2fe08601db803e241104ab858e49aa106bb`；唯一图片 2 个；物理路径 2 个。

### GS-124 强化例题4.9

- 题目：已知 $f(x)=e^x+2x+1$，$g$ 与 $f$ 互为反函数，求 $g^{\prime\prime}(2)$。
- 所问：求反函数在指定自变量处的二阶导数
- 知识点：一元函数微分学应用；反函数求导
- 第一动作：先解方程 $f(x_0)=2$，确定反函数自变量 2 对应的原函数自变量 $x_0$。
- 答案：$g^{\prime\prime}(2)=-\dfrac{1}{27}$。
- 个人错因边界：legacy_unclassified；旧视觉详情的来源叙述称，推导出 $g^{\prime\prime}(y)=-\frac{f^{\prime\prime}(x)}{(f^{\prime}(x))^3}$ 后曾把反函数自变量 $y=2$ 当成原函数自变量 $x=2$；当前题图未显示该作答，故仅作为待用户确认的历史错因，正确入口仍是先解 $f(x)=2$。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先解 f(x₀)=2，确定反函数对应点 x₀=0。
  - 用反函数二阶导公式代入 f′(x₀)、f″(x₀)。
- 质量发现：
  - `inverse_second_derivative_corresponding_point_and_legacy_evidence_downgraded`：已补齐反函数二阶导对应点链条，并将无原始作答支持的旧错因降为历史未分类证据。；建议：
- 关系裁决：
  - GS-683：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
- 当前快照：`stale`；正式卡 `24b3dd7d0992d207ebde5d91af7ca935696f9e58f2328f4a84ac28d79c3b0b02`；唯一图片 1 个；物理路径 1 个。

### GS-125 1000题A组11.2

- 题目：当 $x\ge0$ 时，$f$ 可导且有反函数 $g$，并满足 $\int_1^{f(x)}g(t)\,dt=x^2-1$，求 $f(x)$。
- 所问：求满足积分方程的原函数表达式
- 知识点：定积分；变上限积分
- 第一动作：先对积分方程两边求导，写出 g(f(x))f'(x)=2x。
- 答案：$f(x)=2x-1$。
- 个人错因边界：pending_user_confirmation；已于 2026-06-02 复做正确并标记掌握；本轮依据题图与折叠解析确认复做入口：对变上限积分方程两边求导，把积分方程转成 $g(f(x))f^{\prime}(x)=2x$，再利用反函数关系收口。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 对变上限积分方程求导。
  - 用 g(f(x))=x 化简并得到 f′(x)=2。
  - 用 x=1 时积分为零及反函数单射性验证 f(1)=1，确定常数。
- 质量发现：
  - `variable_upper_limit_inverse_initial_value_chain_repaired`：已修复变上限积分、反函数、零积分初值与单射性构成的完整合法链。；建议：
- 关系裁决：
  - GS-283：`add_strong_edge`；
  - GS-536：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `77f3e751014b773aff783a5e2ccd950d5025e77a76782ebb19f7df0e947b0870`；唯一图片 1 个；物理路径 1 个。

### GS-126 25882 2026.2.28 T1

- 题目：求 $y=f(x)=\ln(x+\sqrt{1+x^2})$ 的反函数 $f^{-1}(x)$ 及其定义域。
- 所问：求反函数表达式及定义域
- 知识点：反函数构造；有理化；单调性与值域
- 第一动作：先由 $e^y=x+\sqrt{x^2+1}$ 构造 $e^{-y}=\sqrt{x^2+1}-x$，再相减解出 $x$。
- 答案：$f^{-1}(x)=\dfrac12(e^x-e^{-x})$，定义域为 $(-\infty,+\infty)$。
- 个人错因边界：legacy_unclassified；旧视觉详情的来源叙述称，取指数得到 $e^y=x+\sqrt{x^2+1}$ 后曾未继续构造 $e^{-y}=\sqrt{x^2+1}-x$ 来消根号；当前题图未显示该作答，故仅作为待用户确认的历史错因。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 指数化原式。
  - 构造共轭形式得到 e 的负幂表达。
  - 两式相减消根号并核对反函数定义域。
- 质量发现：
  - `inverse_construction_tags_and_weak_edges_repaired`：已核对反函数构造、值域与定义域，并清除不能达到共同第一动作门槛的旧边。；建议：
- 关系裁决：
  - GS-134：`remove_broad_stale_or_weak_edge`；
  - GS-141：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `55c19d45e2152107ca42ce5fa518a8f58311b83902758e83455c7ae7818e392d`；唯一图片 1 个；物理路径 1 个。

### GS-127 强化例题5.1

- 题目：设 \(f(x)\) 有连续的一阶导数，且 $$ f(0)=0,\qquad f'(0)=1. $$ 曲线 \(y=f(x)\) 在点 \((x,f(x))\) 处的切线在 \(x\) 轴上的截距为 \(u\)，求 $$ \lim_{x\to0}\frac{x f(u)}{u f(x)}. $$
- 所问：计算切线截距参与的极限
- 知识点：一元函数微分学应用；导数定义；切线方程；极限与连续；导数几何意义
- 第一动作：先由切线方程令 \(Y=0\) 求 \(u=x-\frac{f(x)}{f'(x)}\)，再把原式拆成 \(\frac{x}{f(x)}\cdot\frac{f(u)}{u}\)。
- 答案：\boxed{1}
- 个人错因边界：user_confirmed；正式错误事件的首个断点是没有把“切线在 x 轴上的截距”翻译成 \(u=x-\frac{f(x)}{f'(x)}\)。睡前独立诊断中这一步已经能完成，当前断点后移到证明 \(u\to0\)：把“\(u\) 与 \(x\) 同趋于 0”误说成 \(u=x\)，并漏写由一阶导数连续得到 \(f'(x)\to1\) 的条件。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由切线方程求 x 轴截距 u。
  - 证明 u 趋于 0。
  - 把目标式拆成两个导数定义型因子。
- 质量发现：
  - `user_confirmed_intercept_chain_and_lhopital_error_edge_verified`：已保留用户确认的切线截距错误，并验证导数定义型极限的两条强关系。；建议：
- 关系裁决：
  - GS-507：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-540：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-530：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `5c9cc49dd7e745c07e643a0aa314cdb6147609803239e7cecab84ca165c1660d`；唯一图片 1 个；物理路径 1 个。

### GS-128 2023年真题第14题 隐函数法线斜率

- 题目：曲线 $$ 3x^3=y^5+2y^3 $$ 在 \(x=1\) 对应点处的法线斜率。
- 所问：求指定点处法线斜率
- 知识点：隐函数求导；法线方程
- 第一动作：先代入给定 x 值解出曲线上的对应点
- 答案：\(\displaystyle -\frac{11}{9}\)
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；本轮依据题图与解析图补强可确认的题型入口：隐函数曲线在指定 \(x\) 处求法线斜率时，先代 \(x=1\) 解出对应点 \((1,1)\)，再隐函数求导得到切线斜率，最后取负倒数作为法线斜率。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 代入 x=1 解对应点并用严格单调性证明唯一。
  - 隐式求导得到切线斜率。
  - 取负倒数得到法线斜率。
- 质量发现：
  - `implicit_normal_unique_point_justification_repaired`：已用严格递增证明对应点唯一，并核对隐式法线的独立解析图。；建议：
- 关系裁决：
  - GS-164：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-538：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-540：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `3e3e2c4d8de20f2d75aad5734bc249810846be5d04110e4c4332b3864a8efab3`；唯一图片 2 个；物理路径 3 个。

### GS-129 102310 反函数分段表达

- 题目：求 $y=\sin x$ 在 $0<x<2\pi$ 上各单调区间对应的反函数表达。关键不是直接套 $\arcsin$，而是先切单调区间、写值域，再把角拉回主值区间。
- 所问：分段写出各单调区间上的反函数
- 知识点：函数单调性；反函数；反三角函数主值；三角函数
- 第一动作：先用 \(\cos x\) 的符号把 \(0<x<2\pi\) 切成 \((0,\pi/2]\)、\([\pi/2,3\pi/2]\)、\([3\pi/2,2\pi)\) 三段单调区间
- 答案：在 \((0,\frac\pi2]\)、\([\frac\pi2,\frac{3\pi}2]\)、\([\frac{3\pi}2,2\pi)\) 三个单调区间上分别写 \(x=\arcsin y\)、\(x=\pi-\arcsin y\)、\(x=2\pi+\arcsin y\)，对应值域分别为 \((0,1]\)、\([-1,1]\)、\([-1,0)\)。
- 个人错因边界：legacy_unclassified；旧视觉详情的来源叙述称曾未先按 \(\sin x\) 在 \(0<x<2\pi\) 上的单调区间分段并写清每段值域，且反解时混淆变量角色与主值范围；当前题图未显示该作答，故仅作为待用户确认的历史错因。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 按余弦符号切出三个单调区间。
  - 逐段写值域。
  - 借助反正弦主值和诱导公式写各段反函数。
- 质量发现：
  - `open_domain_and_inverse_branch_ranges_repaired`：已恢复原题开区间，逐段校正反函数值域及首尾开端点。；建议：
- 关系裁决：
  - GS-312：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
- 当前快照：`stale`；正式卡 `426c75cc673b73fa661654d24382463c10845f8dbf8acd42b15cf4a4f2e27cf6`；唯一图片 1 个；物理路径 1 个。

### GS-130 57936 2026.4.16

- 题目：已知 $|f(x_1)-f(x_2)|\le |x_1-x_2|$，证明 $F(x)=f(x)+x$ 在 $(-a,a)$ 内单调增加。严格说可证明单调不减。
- 所问：证明目标函数的单调不减性并辨析严格性
- 知识点：一元函数微分学应用；单调性与极值
- 第一动作：先任取 x1<x2 并把右端绝对值化为 x2-x1
- 答案：$F(x)=f(x)+x$ 在 $(-a,a)$ 上单调不减。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；本轮依据题图与折叠解析确认复做入口：题目没有给可导条件，不能硬用导数法；应任取 $x_1<x_2$，按单调定义把题设配成 $F(x_1)\le F(x_2)$。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 任取 x₁<x₂。
  - 由 Lipschitz 条件推出 f(x₁)-f(x₂)≤x₂-x₁。
  - 移项得到 F(x₁)≤F(x₂)，并用反例排除严格单调。
- 质量发现：
  - `nonstrict_monotonicity_boundary_and_zero_degree_verified`：已把结论限定为单调不减，禁止越级加强为严格递增，并确认当前零度状态。；建议：
- 当前快照：`stale`；正式卡 `ed357e47250bd1f16e3351f8344849a8a0abe105c361b7d799b2a311a416b6bc`；唯一图片 1 个；物理路径 1 个。

### GS-131 1000题A组5.2

- 题目：函数 $f(x)=e^{-ax}-ex$ 的极值点要求小于 $0$，求参数 $a$ 的范围。题图中的 $ex$ 表示常数 $e$ 与 $x$ 的乘积，不是 $e^x$。
- 所问：求使极值点位于负半轴的参数范围
- 知识点：一元函数微分学应用；单调性与极值；参数分类讨论；对数函数性质
- 第一动作：先按 $a>0,a=0,a<0$ 分类，再在 $a<0$ 下解驻点并检查 $\ln$ 的定义域与符号。
- 答案：$a\in(-\infty,-e)$
- 个人错因边界：legacy_unclassified；旧视觉详情的来源叙述称，处理含参数极值点位置时曾未先按 $a>0,a=0,a<0$ 分类，并漏查 $\ln(-e/a)$ 的定义域、符号和不等号方向；当前题图未显示该作答，故仅作为待用户确认的历史错因。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先按参数正负分类。
  - 在可产生驻点的分支解驻点并检查对数定义域。
  - 联立驻点小于零的条件并核对不等号方向。
- 质量发现：
  - `parameter_sign_log_domain_and_chapter_repaired`：已校正参数分类中的符号、对数定义域和章节归属。；建议：
- 关系裁决：
  - GS-134：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-156：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `fb1a0b6380500981867fc7ee58a77913170a6e2d70b893eb106ea29d3676d16b`；唯一图片 1 个；物理路径 1 个。

### GS-132 1000题A组5.3

- 题目：分段函数在 $x=0$ 处由左侧 $\cos|x|-1$、右侧 $x\ln x$ 拼接，判断 $x=0$ 是可导点还是极值点。
- 所问：判断分界点的可导性与极值性质
- 知识点：一元函数微分学应用；极值定义；分段函数连续可导；不可导点判别
- 第一动作：先比较 $x=0$ 附近两侧函数值，再分别算左导数和右导数。
- 答案：选 B：$x=0$ 是不可导点，也是 $f(x)$ 的极大值点。
- 个人错因边界：legacy_unclassified；旧视觉详情的来源叙述称，曾把“极大值点”误按“全局最大值点”理解；当前题图未显示该作答，故仅作为待确认历史错因。数学上，右支 $x\ln x$ 在 $x\to+\infty$ 时无上界，所以函数无全局最大值；存在 $x>1$ 使函数值大于 0 只足以说明 $x=0$ 不是全局最大点，不影响其局部极大性质。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 分别比较分界点两侧邻域函数值。
  - 用左右差商检查可导性。
  - 区分局部极大点与不存在的全局最大值。
- 质量发现：
  - `local_extreme_and_unbounded_global_maximum_boundary_repaired`：已区分分界点局部极大值与右支无上界导致的全局最大值不存在。；建议：
- 关系裁决：
  - GS-137：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `9535a4b79739356e1adf1a2d896be409691e59c8a557ae4d44cf94422d2593af`；唯一图片 1 个；物理路径 1 个。

### GS-133 57978 闭区间最值流程

- 题目：设 \(n\) 为正整数， \[ f(x)=nx(1-x)^n,\qquad x\in[0,1]. \] 求 \(f(x)\) 在 \([0,1]\) 上的最大值 \(M(n)\) 及 \(\lim_{n\to\infty}M(n)\)。
- 所问：求闭区间最大值及其随 n 的极限
- 知识点：一元函数微分学应用；单调性与极值；极限与连续
- 第一动作：先在 \((0,1)\) 内令 \(f'(x)=0\) 找内部驻点，再把 \(x=0,1\) 作为端点候选列出
- 答案：最大值点为 \(x=\frac{1}{n+1}\)，最大值 \(M(n)=\left(\frac{n}{n+1}\right)^{n+1}\)，且 \(\lim_{n\to\infty}M(n)=e^{-1}\)。
- 个人错因边界：legacy_unclassified；历史来源记录了两次不同错误：第一次把最大值点的极限误当成最大值的极限，第二次未完整执行“内部驻点 + 端点值比较”流程。当前题图未显示用户作答，故两次记录均保留但归为待确认历史错因。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 在开区间求内部驻点。
  - 将两个端点作为独立候选并比较函数值。
  - 对最大值表达式取数列极限。
- 质量发现：
  - `closed_interval_endpoint_not_stationary_and_alias_verified`：已明确闭区间端点只是独立候选而非通用驻点，并核对同卡别名图片。；建议：
- 关系裁决：
  - GS-642：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-524：`remove_broad_stale_or_weak_edge`；
  - GS-525：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `e069349fd9a97f2f2fa13494a7654096adad4b3e85badea9467f60407ff12189`；唯一图片 2 个；物理路径 3 个。

### GS-134 1000题B组5.36

- 题目：先求 $f(x)=xa^x(1-a)$ 在 $0<a<1,x>0$ 下的最大值，再用该最大值证明 $xy^x(1-y)<1/e$。
- 所问：求参数函数最大值并证明不等式
- 知识点：一元函数微分学应用；单调性与极值；对数不等式；不等式证明
- 第一动作：先令 $a=y$，把第一问的最大值结论套到 $xy^x(1-y)$ 上。
- 答案：(1) 最大值为 $\frac{a-1}{e\ln a}$，在 $x=-\frac1{\ln a}$ 处取得；(2) 对 $x>0,0<y<1$ 有 $xy^x(1-y)<\frac1e$。
- 个人错因边界：legacy_unclassified；旧来源解析叙述的候选错因：第二问可能没有把 $y$ 当固定参数复用第一问最大值结论，并可能遗漏除以 $\ln y<0$ 时不等号变向；当前题图不含用户作答，不能视为图像证实。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先对参数固定时的函数求导并确定最大值。
  - 在第二问令参数等于 y，复用第一问最值结论。
  - 利用对数不等式严格化最终上界。
- 质量发现：
  - `fixed_parameter_maximum_and_negative_log_direction_verified`：已核对固定参数求最值、负对数方向与后续不等式复用。；建议：
- 关系裁决：
  - GS-134：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-134：`remove_broad_stale_or_weak_edge`；
  - GS-156：`remove_broad_stale_or_weak_edge`；
  - GS-524：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `17b4021e1e4e897d0e99f82839221c3c76586a5a4eb72797ef935babc73c54c4`；唯一图片 1 个；物理路径 1 个。

### GS-135 1000题A组5.4

- 题目：不等式 $x^2+ax^{-3}\ge 10/3$ 对一切 $x>0$ 恒成立，求参数 $a$ 的范围。
- 所问：求恒成立不等式的参数范围
- 知识点：一元函数微分学应用；单调性与极值；恒成立不等式；参数范围
- 第一动作：先设 $f(x)=\frac{10}{3}x^3-x^5$，再求 $\max_{x>0}f(x)$。
- 答案：$a\in\left[\frac{8\sqrt2}{3},+\infty\right)$
- 个人错因边界：legacy_unclassified；旧来源解析叙述的候选错因：分离参数后可能没有触发“$a\ge f(x)$ 对一切 $x>0$ 成立等价于 $a\ge \max_{x>0}f(x)$”的动作；当前题图不能独立证实该个人错因。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 把参数分离为 a≥φ(x)。
  - 求 φ 在 x>0 上的最大值。
  - 由“对一切 x”转为参数不小于全域最大值。
- 质量发现：
  - `universal_parameter_inequality_mastery_evidence_separated`：已核对恒成立分离参数链，同时把历史掌握事实与本题视觉证据分开保存。；建议：
- 关系裁决：
  - GS-524：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-136：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `a71c54f315d3ce7cf8efeac4047a8b959917cfc65c95c8ed5c174d2cc2094a1b`；唯一图片 1 个；物理路径 1 个。

### GS-136 1000题B组5.6

- 题目：不等式 $x^2-2ax+1-e^x\ge0$ 对一切 $x<0$ 恒成立，求参数 $a$ 的范围。
- 所问：求负半轴恒成立不等式的参数范围
- 知识点：一元函数微分学应用；单调性与极值；恒成立不等式；重要极限
- 第一动作：先把含 a 项移到一边，并注意除以 2x<0 时不等号变号
- 答案：$a\in\left[-\frac12,+\infty\right)$
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；本轮确认复做入口是先在 $x<0$ 下分离参数，除以 $2x<0$ 时必须变号，再求右侧辅助函数在 $(-\infty,0)$ 上的上确界。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 在 x<0 下分离参数并处理除以负数变号。
  - 证明辅助函数严格递减。
  - 由 x 趋于 0 的左极限取得上确界，端点不在定义域。
- 质量发现：
  - `decreasing_supremum_endpoint_direction_repaired`：已校正辅助函数严格递减方向，并注明开端点上确界不取到。；建议：
- 关系裁决：
  - GS-524：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-136：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `d0a6dac3d04a5fcb1b50e2bd2cd55765624daa4069d938cae66bbe6e2cc76a19`；唯一图片 1 个；物理路径 1 个。

### GS-138 1000题B组5.10

- 题目：已知 \(f(x)\) 连续，且当 \(x \to 0\) 时 \(e^{f(x)}-1\sim x-\ln(1+x)\)，判断 \(f(x)\) 在 \(x=0\) 处的极值、拐点与二次泰勒多项式相关结论。
- 所问：判断极值、拐点与经典二次 Taylor 多项式命题的必然性
- 知识点：极限与连续；等价无穷小；Peano 余项；Peano 主部与经典 Taylor 多项式的边界；导数定义；单调性与极值；凹凸性与拐点；一元函数微分学应用
- 第一动作：先由 \(e^{f(x)}-1\sim f(x)\) 和 \(x-\ln(1+x)\sim\frac12x^2\) 写出 \(f(x)=\frac12x^2+o(x^2)\)。
- 答案：A（0 项）
- 个人错因边界：legacy_unclassified；旧来源候选错因是把函数等价 \(f(x)\sim\frac12x^2\) 当成可直接求导的等价；当前可确认的数学边界是题设仅推出 \(f(0)=0\) 与 \(f(x)=\frac12x^2+o(x^2)\)，不能推出经典二阶导数或经典二次 Taylor 多项式存在。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由两侧等价关系得到 f(0)=0 与二次 Peano 主部。
  - 用主部判断严格局部极小与不换凹凸。
  - 用二阶导不存在的反例排除经典二次 Taylor 多项式必然存在。
- 质量发现：
  - `incorrect_answer_and_peano_taylor_boundary_repaired`：已将答案纠正为零项成立，限定为 Peano 主部，并用反例阻断经典二阶 Taylor 多项式的越级结论。；建议：
- 关系裁决：
  - GS-234：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-507：`add_strong_edge`；
  - GS-451：`remove_broad_stale_or_weak_edge`；
  - GS-525：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `94f61658469f4d96b0d0aa9873f3ec9f673c23027ecfbeec3ff4d950055a7d44`；唯一图片 1 个；物理路径 1 个。

### GS-139 1000题B组5.21 导函数图像判拐点

- 题目：已知 \(f(x)\) 在 \((-\infty,+\infty)\) 内连续，题目给出 \(f'(x)\) 的图像，并说明在 \(f'(x)\) 存在处 \(f''(x)\) 也存在。要求判断曲线 \(y=f(x)\) 的拐点个数。
- 所问：根据导函数图像判断原函数拐点个数
- 知识点：凹凸性与拐点；二阶导数判凹凸性
- 第一动作：先标出 f' 由增变减或由减变增的候选点
- 答案：选 B，拐点个数为 2
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；本轮依据题图与解析修复题型定位：本题核心是由 \(f'(x)\) 的图像判断 \(f(x)\) 的拐点，不能只看 \(f'(x)=0\)，而要看 \(f'\) 的单调性是否发生改变。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 把导函数图像的增减翻译为原函数的凹凸。
  - 标出导函数单调性改变点。
  - 逐点核验凹凸确实发生改变。
- 质量发现：
  - `derivative_graph_inflection_and_solution_evidence_boundary_verified`：已从导函数图像核对拐点判别，并把独立解析图和个人错因证据分层。；建议：
- 关系裁决：
  - GS-525：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-142：`remove_broad_stale_or_weak_edge`；
  - GS-167：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `544aac13830edc79849c52c2b8d8f9f72a70e589fd1fb4a5ecaf0999628faaa6`；唯一图片 2 个；物理路径 2 个。

### GS-140 1000题B组5.26

- 题目：曲线 $y=xe^{-x^2/2}$ 的拐点个数判断。
- 所问：判断曲线拐点个数
- 知识点：一元函数微分学应用；凹凸性与拐点；二阶导数判凹凸性
- 第一动作：先求二阶导并分区间判断符号。
- 答案：选 C：拐点个数为 3。候选横坐标为 $-\sqrt3,0,\sqrt3$，且二阶导在三点均变号。
- 个人错因边界：legacy_unclassified；旧来源解析叙述的候选错因：二阶导整理时可能没有完整保留因式 $x(x^2-3)$，并可能混淆“凹凸性改变”与“一阶导变号”；当前题图不含用户作答，不能视为图像证实。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 计算并完整因式分解二阶导。
  - 列出三个候选横坐标。
  - 逐区间判二阶导符号，确认三处均变号。
- 质量发现：
  - `second_derivative_factorization_and_counterexample_derivative_order_repaired`：已校正二阶导因式分解及反例中的导数阶数，保留逐候选点验变号。；建议：
- 关系裁决：
  - GS-451：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-490：`remove_broad_stale_or_weak_edge`；
  - GS-499：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `da87ae715066d7720983c91f114fb02e6513627caaf9ba8899f3326c57c4e381`；唯一图片 1 个；物理路径 1 个。

### GS-141 强化例题5.2

- 题目：函数 $f(x)=(x^2+a)e^x$ 无极值点且有拐点，求参数范围。
- 所问：求同时满足无极值点且有拐点的参数范围
- 知识点：一元函数微分学应用；单调性与极值；凹凸性与拐点；参数范围
- 第一动作：先求一阶导与二阶导并剥离正因子 $e^x$，分别写出 $q(x)$、$r(x)$ 的符号条件。
- 答案：$a\in[1,2)$
- 个人错因边界：legacy_unclassified；旧来源解析叙述的候选错因：可能没有把“没有极值点”和“有拐点”分别转成两个二次因子的符号条件；当前题图不含用户作答。对本题而言，无极值等价于 $q(x)\ge0$，有拐点等价于 $r(x)$ 有两个相异实根并变号。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 剥离始终为正的指数因子。
  - 用一阶导二次因子非负控制无极值，允许重根。
  - 用二阶导二次因子有两个相异实根控制有拐点并求交集。
- 质量发现：
  - `question_formula_and_discriminant_boundaries_repaired`：已按题图恢复函数表达式，并分别处理极值无重根变号与拐点两个相异实根的判别式边界。；建议：
- 关系裁决：
  - GS-146：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-141：`remove_broad_stale_or_weak_edge`；
  - GS-451：`remove_broad_stale_or_weak_edge`；
  - GS-525：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `0dec562772bfb95148273951e985e06af90b383f64f173eb72c950842580e69c`；唯一图片 1 个；物理路径 1 个。

### GS-142 强化例题5.4（2022年数2第三题）

- 题目：设函数 \(f(x)\) 在 \(x=x_0\) 处有二阶导数，判断下列命题真伪： - 若 \(f(x)\) 在 \(x_0\) 的某邻域内单调增加，则 \(f'(x_0)>0\)； - 若 \(f'(x_0)>0\)，则 \(f(x)\) 在 \(x_0\) 的某邻域内单调增加； - 若曲线 \(f(x)\) 在 \(x_0\) 的某邻域内是凹的，则 \(f''(x_0)>0\)； - 若 \(f''(x_0)>0\)，则 \(f(x)\) 在 \(x_0\) 的某邻域内是凹的。
- 所问：判断点态导数与邻域性质的四个命题
- 知识点：函数单调性；导函数连续性；连续函数局部保号性；局部凹凸性
- 第一动作：先把每个选项拆成邻域性质推出点处值或点处值推出邻域性质
- 答案：B
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；本轮依据题图与解析修复题型定位：本题核心是区分“邻域内的单调/凹凸性质”和“点处导数值”，真命题用导数连续性与保号性证明，假命题用反例排除。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 将每个命题拆成邻域性质与点态导数值的推导方向。
  - 真命题用相应导数连续性和局部保号。
  - 其余方向用反例排除。
- 质量发现：
  - `pointwise_neighborhood_continuity_boundary_tags_repaired`：已把点态导数、连续保号、邻域单调和局部凹凸拆成不同层级并修正标签。；建议：
- 关系裁决：
  - GS-452：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-142：`remove_broad_stale_or_weak_edge`；
  - GS-490：`remove_broad_stale_or_weak_edge`；
  - GS-508：`remove_broad_stale_or_weak_edge`；
  - GS-525：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `cf71159179eb2c179ec5b5d20cf3e69857d65eae197f9cf6252076bf7f622803`；唯一图片 2 个；物理路径 2 个。

### GS-143 1000题A组5.9

- 题目：曲线 $x^2 - xy + y^2 = 1$ 在点 $(1,1)$ 处的曲率。
- 所问：求隐式曲线在指定点处的曲率
- 知识点：一元函数微分学应用；曲率；隐函数求导；高阶导数
- 第一动作：先对 \(x^2-xy+y^2=1\) 两边关于 \(x\) 求导，写出 \(2x-y-xy'+2yy'=0\)。
- 答案：$$ k = \tfrac{3\sqrt{2}}{2} $$
- 个人错因边界：legacy_unclassified；旧来源解析叙述的候选错因是未先触发隐函数求导或曲率公式调用；当前题图不含用户推导。可确认的标准入口是由 \(x^2-xy+y^2=1\) 连续求出 \(y'\)、\(y''\)，再代入 \(K=\frac{|y''|}{(1+(y')^2)^{3/2}}\)。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 对隐式方程连续求一阶、二阶导。
  - 在给定点代入得到 y′、y″。
  - 代入曲率公式并化简。
- 质量发现：
  - `implicit_curve_curvature_and_source_evidence_boundary_repaired`：已核对隐式曲线点处曲率链，并把题图证据与历史个人错因边界分离。；建议：
- 关系裁决：
  - GS-148：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-468：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-538：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-650：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-149：`remove_broad_stale_or_weak_edge`；
  - GS-154：`remove_broad_stale_or_weak_edge`；
  - GS-464：`remove_broad_stale_or_weak_edge`；
  - GS-529：`remove_broad_stale_or_weak_edge`；
  - GS-539：`remove_broad_stale_or_weak_edge`；
- 当前快照：`stale`；正式卡 `ea2798e28f3ccfb1bb3f913f8271137ef7f3f36cd5c688e1748cbd3233193b9d`；唯一图片 1 个；物理路径 1 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
