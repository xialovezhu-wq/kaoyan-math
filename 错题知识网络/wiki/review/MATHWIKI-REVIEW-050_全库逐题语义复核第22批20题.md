---
wiki_id: MATHWIKI-REVIEW-050
type: target_level_semantic_review_batch
title: 全库逐题语义复核第22批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-050_全库逐题语义复核第22批20题.json
status: active
last_updated: 2026-07-23
---

# 全库逐题语义复核第22批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 0 张；覆盖 34 个物理图片路径与 34 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 20 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `MATH-TARGET-SEMANTIC-CLOSEOUT-20260723-B22`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-278](http://127.0.0.1:8765/open/GS-278) | 有理函数定积分计算 | 定积分、有理函数积分、部分分式、不可约二次因子配方、牛顿莱布尼茨公式 | $$\int_0^1\frac{dx}{(x+1)(x^2-2x+2)}=\frac{3\ln2}{10}+\frac{\pi}{10}$$ | pending_user_confirmation：暂无明确个人错因；待用户确认的复做入口是，看到一次因子乘不可约二次因子的有理函数定积分，先写完整部分分式，再把二次因子配方成 $(x-1)^2+1$，分别处理对数和反正切项。 | duplicate_identity_and_partial_fraction_verified |
| [GS-279](http://127.0.0.1:8765/open/GS-279) | 有理函数积分：重复线性因子与不可约二次因式部分分式 | 有理函数积分、部分分式、原函数定义域连通区间 | -2\ln\|x-1\|-\frac{3}{x-1}+\ln(x^2+x+1)+C | pending_user_confirmation：旧卡未保存用户当时个人错因；复做入口是先按重复线性因子和不可约二次因式写完整部分分式模板。 | domain_connected_components_verified |
| [GS-282](http://127.0.0.1:8765/open/GS-282) | 反常积分参数反求 | 反常积分、有理函数积分、部分分式、参数方程、参数可积性条件、区间内部奇点 | $$a=2$$ | pending_user_confirmation：暂无明确个人错因；待用户确认的复做入口是先检查参数使积分有意义，再做部分分式、处理无穷远端极限并排除区间内奇点。 | improper_integral_domain_and_internal_pole_verified |
| [GS-283](http://127.0.0.1:8765/open/GS-283) | 变上限积分反函数综合 | 定积分、变上限积分、反函数、第一类换元、不定积分 | \(f(x)=\ln(1+x)+2x\ln(1+x)-x\)。 | pending_user_confirmation：暂无明确个人错因；待用户确认的复做入口是先令 \(u=t-x\) 消参，求导后用 \(g(f(x))=x\) 化简，并由 \(f'(x)\) 积分还原 \(f(x)\)。 | inverse_upper_limit_chain_and_external_cleanup_verified |
| [GS-284](http://127.0.0.1:8765/open/GS-284) | 含绝对值参数定积分求导与最值 | 定积分、含参积分、绝对值分段、最值问题、导数应用 | $$f'(x)=\begin{cases}2x(2x-1),&0<x<1,\\2x,&x\ge1,\end{cases}\quad f_{\min}=\frac14$$ | pending_user_confirmation：视觉详情确认复做入口：看到积分中含 $\|t^2-x^2\|$ 且 $x>0$，应先按 $0<x<1$ 与 $x\ge1$ 分段拆绝对值，再求导和最值。 | asked_output_boundary_verified |
| [GS-285](http://127.0.0.1:8765/open/GS-285) | 球体表面积与体积相关变化率 | 一元函数微分学应用、相关变化率、复合函数求导、球体几何量公式 | $$\frac{dS}{dt}=2000\pi\ \mathrm{cm^2/s},\quad \frac{dV}{dt}=50000\pi\ \mathrm{cm^3/s}$$ | pending_user_confirmation：暂无明确个人错因；待用户确认的复做入口是先写球的 $S(r)$、$V(r)$，再用链式法则乘上 $dr/dt$。题解所示的“对 $r$ 求导与对时间求导混淆”只作为候选风险。 | source_filename_title_mismatch_documented |
| [GS-286](http://127.0.0.1:8765/open/GS-286) | 变上限积分方程零点个数 | 定积分、变上限积分、零点定理、单调性、均值不等式 | $$1\text{ 个（B）}$$ | pending_user_confirmation：暂无明确个人错因；待用户确认的复做入口是把两个变上限积分的和定义为函数，先核对端点符号，再求导并用 $u+1/u\ge2$ 证明严格递增，从而判定唯一根。 | wrong_mastery_transfer_isolated |
| [GS-287](http://127.0.0.1:8765/open/GS-287) | 极限定义函数与变上限积分可导性 | 定积分、变上限积分、间断点分类、导数定义、极限与连续、被积函数点值与积分函数点值区分、单点值不影响定积分 | 选 C：\(F\) 在 \(x=0\) 处连续但不可导。 | confirmed_personal：本次对 \(f\) 的分类讨论没问题；第一个真正偏离是把 \(f(0)\) 当成 \(F(0)\)。\(F(0)\) 必须由 \(\int_{-1}^{0}f(t)\,dt\) 计算，而且积分不会因被积函数在单点的取值改变。 | f0_vs_F0_user_breakpoint_verified |
| [GS-288](http://127.0.0.1:8765/open/GS-288) | 含参绝对值积分：先求函数表达式再积分 | 定积分、含参定积分、绝对值分类、分段函数积分、一元函数积分学的计算、积分变量与参数混淆 | \(\displaystyle \frac76\)。先得 \(f(t)=\begin{cases}-t^2+\frac12t,&t<0,\\ t^3-t^2+\frac12t,&0\le t<1,\\ t^2-\frac12t,&t\ge1,\end{cases}\) 再按 \([-1,0]\)、\([0,1]\)、\([1,2]\) 积分。 | confirmed_personal：看到 \(f(t)=\int_0^1 t\|t-x\|dx\) 时，没有先区分积分变量 \(x\) 与参数 \(t\)，没有先求出 \(f(t)\) 的分段表达式；应先写 \(f(t)=t\int_0^1\|t-x\|dx\)，按 \(t<0,\,0\le t<1,\,t\ge1\) 分段，再对 \([-1,2]\) 分段积分。计算中还要逐项检查负号、减括号和系数积分。 | parameter_integral_role_chain_verified |
| [GS-289](http://127.0.0.1:8765/open/GS-289) | 卷积型含参定积分：复合自变量分段函数积分 | 定积分、定积分性质、含参定积分、分段函数积分、卷积型积分、第二类换元、分部积分、一元函数积分学的计算 | \(\displaystyle F(x)=\begin{cases}1-\cos x,&0\le x\le\pi,\\2,&x>\pi.\end{cases}\) | confirmed_personal：看到 \(g(x-t)\) 是分段函数时，没有先区分“\(g\) 的自变量”和“积分变量 \(t\)”；\(\pi\) 是 \(g\) 的输入变量 \(u=x-t\) 的分段点，不是原 \(t\) 轴上的直接分段点。应先令 \(u=x-t\)，把 \(g(x-t)\) 化为 \(g(u)\)，再按 \(u=\pi\) 讨论 \([0,x]\) 是否跨过分段点。 | source_F_prime_mislabel_corrected |
| [GS-290](http://127.0.0.1:8765/open/GS-290) | 分段函数求原函数：分段积分后连续性拼接常数 | 不定积分、原函数、分段函数连续可导、极限与连续、一元函数积分学的计算、分部积分、分段函数积分 | D。分段积分得 \(x\le0\)：\(\ln(\sqrt{1+x^2}+x)+C_1\)；\(x>0\)：\((x+1)\sin x+\cos x+C_2\)。原函数在 \(x=0\) 处连续，故 \(C_1=1+C_2\)。取 \(C_2=0\) 时 \(C_1=1\)，对应 D。 | confirmed_personal：知道要用连续性，但没有把连续性落成 \(F(0^-)=F(0^+)\) 的左右极限方程；分段求原函数后应保留 \(C_1,C_2\)，在 \(x=0\) 代入得到 \(C_1=1+C_2\)，再筛选常数。 | primitive_continuity_equation_verified |
| [GS-291](http://127.0.0.1:8765/open/GS-291) | 分段函数平移定积分 | 定积分、分段函数积分、换元、平移变换 | $$\int_{-2}^{2}f(x-1)dx=13-e^{-1}$$ | pending_user_confirmation：旧卡未保存用户当时个人错因；安全复做入口是看到 $f(x-1)$ 的积分，先令 $u=x-1$ 改区间，再按分段点 $u=0$ 拆开积分，是否曾断在此处仍待用户确认。 | shifted_breakpoint_verified |
| [GS-292](http://127.0.0.1:8765/open/GS-292) | 根号二次式定积分：配方 + 三角换元 + 绝对值符号判断 | 定积分、一元函数积分学的计算、根式积分、第二类换元、三角换元、绝对值分类、积分保号、三角恒等变形 | \(\displaystyle \frac{\pi}{4}\) | confirmed_personal：三角换元时只检查端点角度是否满足 \(\sin t=-1,0\)，没有检查所选角度区间内 \(\cos t\) 的符号。取 \(t:\frac{3\pi}{2}\to0\) 这一分支本身并非非法；真正错误是没有保留 \(\sqrt{\cos^2t}=\|\cos t\|\) 并按符号分段，直接把它写成 \(\cos t\)。更稳的做法是令 \(u=x-1=\sin t\)，选 \(t\in[-\frac{\pi}{2},0]\)，确保 \(\cos t\ge0\)。 | absolute_value_branch_and_external_cleanup_verified |
| [GS-293](http://127.0.0.1:8765/open/GS-293) | 根式定积分几何法计算 | 定积分、定积分性质、第二类换元 | $4\pi$ | pending_user_confirmation：旧卡未保存用户当时个人错因；安全复做入口是先把根号内二次式配成圆并平移到对称区间，再用奇偶性消项，是否曾断在此处仍待用户确认。 | exact_duplicate_identity_mirrored |
| [GS-294](http://127.0.0.1:8765/open/GS-294) | 含绝对值面积积分与级数求和 | 定积分、定积分应用、平面图形面积、绝对值分段、等比级数 | \(\displaystyle S_n=\frac{1+e^{-\pi}}{2}\cdot\frac{1-e^{-n\pi}}{1-e^{-\pi}},\quad \lim_{n\to\infty}S_n=\frac{e^\pi+1}{2(e^\pi-1)}\) | confirmed_personal：已识别 \(\|\sin x\|\) 的周期性和指数衰减，却没有先用定积分区间可加性写成 \(\sum_{k=0}^{n-1}\int_{k\pi}^{(k+1)\pi}\)，因而一开始不知道如何把总面积转成等比数列。 | interval_additivity_breakpoint_verified |
| [GS-295](http://127.0.0.1:8765/open/GS-295) | 曲边图形面积的相关变化率 | 定积分应用、平面图形面积、变上限积分、相关变化率 | \(10\) | pending_user_confirmation：旧卡没有保存用户当时个人错因；安全复做入口是先写出封闭区域面积函数 \(S(x)\)，再用链式法则计算 \(\frac{dS}{dt}\)，是否曾断在此处仍待用户确认。 | area_rate_model_verified |
| [GS-296](http://127.0.0.1:8765/open/GS-296) | 无界区域面积与旋转体体积 | 定积分、定积分应用、旋转体体积、反常积分 | 面积 $S=\ln(1+\sqrt2)$，绕 $x$ 轴旋转体体积 $V=\pi-\frac{\pi^2}{4}$。 | pending_user_confirmation：旧卡未保存用户当时个人错因；安全复做入口是分别建立面积反常积分与圆盘法体积反常积分，是否曾断在此处仍待用户确认。 | improper_area_volume_models_verified |
| [GS-297](http://127.0.0.1:8765/open/GS-297) | 函数方程反解与旋转体体积 | 定积分、函数方程、旋转体体积、水平壳法、三角换元 | \(\displaystyle f(x)=\frac{x}{\sqrt{1+x^2}},\quad V=\frac{\pi^2}{6}\) | pending_user_confirmation：旧卡没有保存用户当时个人错因；复做时要先对含 \(f(1/x)\) 的方程补写 \(x\mapsto 1/x\) 的同伴方程，再反解曲线用于体积积分。 | involution_elimination_and_shell_method_verified |
| [GS-298](http://127.0.0.1:8765/open/GS-298) | 以 \(y\) 为参数的弧长与最大值 | 由微分关系求 \(\frac{dx}{dy}\)、以 \(y\) 为参数的曲线、曲线弧长、单调性与极值 | \(\displaystyle s=\frac{21}{16},\quad x_{\max}=-\frac3{4^{4/3}}\) | pending_user_confirmation：旧卡没有保存用户当时个人错因；安全复做入口是由微分关系求 \(\frac{dx}{dy}\)，再按以 \(y\) 为参数的弧长公式和一元最值链计算，是否曾断在此处仍待用户确认。 | yaml_and_y_parameter_arc_length_verified |
| [GS-299](http://127.0.0.1:8765/open/GS-299) | 由微分方程生成积分曲线弧长 | 定积分、曲线弧长、变上限积分、微分方程的定义区间 | 命题意图下为 \(4n\) | pending_user_confirmation：旧卡没有保存用户当时个人错因；安全复做入口是在命题意图的区间解释下先得到 \(y=\sqrt{\sin x}\)，再对变上限积分求导进入弧长公式，是否曾断在此处仍待用户确认。 | classical_endpoint_no_solution_boundary_documented |

## 逐题复核

### GS-278 2025年真题17题

- 题目：计算 $\int_0^1\frac{1}{(x+1)(x^2-2x+2)}dx$。
- 所问：有理函数定积分计算
- 知识点：定积分；有理函数积分；部分分式；不可约二次因子配方；牛顿莱布尼茨公式
- 第一动作：先按一次因子与不可约二次因子写完整部分分式。
- 答案：$$\int_0^1\frac{dx}{(x+1)(x^2-2x+2)}=\frac{3\ln2}{10}+\frac{\pi}{10}$$
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；待用户确认的复做入口是，看到一次因子乘不可约二次因子的有理函数定积分，先写完整部分分式，再把二次因子配方成 $(x-1)^2+1$，分别处理对数和反正切项。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 部分分式后配方，分别积分对数项与反正切项并代入上下限。
- 质量发现：
  - `duplicate_identity_and_partial_fraction_verified`：与 GS-161 数学同题但题图渲染不同；保留稳定 ID 并冻结普通聚合边。；建议：
- 关系裁决：
  - GS-276：`remove_identity_or_broad_edge`；涉及身份冻结卡或仅共享宽泛积分标签，不再保留普通语义边。
  - GS-604：`remove_identity_or_broad_edge`；涉及身份冻结卡或仅共享宽泛积分标签，不再保留普通语义边。
  - GS-282：`remove_identity_or_broad_edge`；涉及身份冻结卡或仅共享宽泛积分标签，不再保留普通语义边。
- 当前快照：`stale`；正式卡 `02050739451e7c4e9be84870f52ab66a76457f85db80f010b37c68f085fcfab0`；唯一图片 1 个；物理路径 1 个。

### GS-279 2019年第16题

- 题目：求不定积分 \[ \int\frac{3x+6}{(x-1)^2(x^2+x+1)}\,dx. \]
- 所问：有理函数积分：重复线性因子与不可约二次因式部分分式
- 知识点：有理函数积分；部分分式；原函数定义域连通区间
- 第一动作：先按重复一次因子与不可约二次因子写完整部分分式模板。
- 答案：-2\ln|x-1|-\frac{3}{x-1}+\ln(x^2+x+1)+C
- 个人错因边界：pending_user_confirmation；旧卡未保存用户当时个人错因；复做入口是先按重复线性因子和不可约二次因式写完整部分分式模板。
- 一致性：题图—解析 independent_solution_assets_present；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 比较系数后逐项积分，并在不跨越 x=1 的连通区间理解积分常数。
- 质量发现：
  - `domain_connected_components_verified`：已明确 x=1 把定义域分成两个连通分支，两侧积分常数不应被强行视为同一常数。；建议：
- 当前快照：`stale`；正式卡 `6bbfe82485318002929d49783d04cc1d921ba36ad31c529dcf4c0b03a35ad300`；唯一图片 3 个；物理路径 3 个。

### GS-282 强化例题9.15(171537)

- 题目：设 $\int_1^{+\infty}\frac{a}{x(2x+a)}dx=\ln2$，求 $a$。
- 所问：反常积分参数反求
- 知识点：反常积分；有理函数积分；部分分式；参数方程；参数可积性条件；区间内部奇点
- 第一动作：先检查分母零点是否进入积分区间，得到普通反常积分存在需 a>-2。
- 答案：$$a=2$$
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；待用户确认的复做入口是先检查参数使积分有意义，再做部分分式、处理无穷远端极限并排除区间内奇点。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 在合法参数域内部分分式、取无穷远极限，并排除产生内部奇点的候选 a=-6。
- 质量发现：
  - `improper_integral_domain_and_internal_pole_verified`：已先落实 a>-2 的存在条件，并明确 a=-6 在 x=3 产生内部奇点、必须排除。；建议：
- 当前快照：`stale`；正式卡 `ccca3e5fbc3f618b3128f2edbed9418bae52dfe1eef1d60c697ff998b4c1bf1a`；唯一图片 1 个；物理路径 1 个。

### GS-283 强化例题9.16（19906）2026.5.6

- 题目：设 \(f\) 在 \([0,+\infty)\) 上可导，\(f(0)=0\)，\(g\) 为 \(f\) 的反函数，且 $$ \int_x^{x+f(x)}g(t-x)\,dt=x^2\ln(1+x), $$ 求 \(f(x)\)。
- 所问：变上限积分反函数综合
- 知识点：定积分；变上限积分；反函数；第一类换元；不定积分
- 第一动作：先令 u=t-x，把含参变上限积分化为从 0 到 f(x) 的积分。
- 答案：\(f(x)=\ln(1+x)+2x\ln(1+x)-x\)。
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；待用户确认的复做入口是先令 \(u=t-x\) 消参，求导后用 \(g(f(x))=x\) 化简，并由 \(f'(x)\) 积分还原 \(f(x)\)。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 换元消参后求导，用反函数复合消元，再由初值还原 f。
- 质量发现：
  - `inverse_upper_limit_chain_and_external_cleanup_verified`：变上限反函数链已核对，并清理 GS-335 指向本卡的外部单向宽边。；建议：
- 关系裁决：
  - GS-125：`verify_existing_strong_edge`；同为变上限积分与反函数复合，先求导消积分，再用初值确定常数。
  - GS-332：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
  - GS-336：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
  - GS-683：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
  - GS-283：`remove_external_inbound_only_broad_edge`；外部端点仅单向指向本批卡，未共享足够具体的对象、条件与第一动作，按 external_inbound_cleanup 删除。
- 当前快照：`stale`；正式卡 `21af4d5bc91d4bd66a18726988aa15631bba9b400d200d3a395d8da1a0fca5a4`；唯一图片 1 个；物理路径 1 个。

### GS-284 强化例题9.18（78365）

- 题目：设 $f(x)=\int_0^1|t^2-x^2|dt\ (x>0)$，求 $f'(x)$ 并求 $f(x)$ 的最小值。
- 所问：含绝对值参数定积分求导与最值
- 知识点：定积分；含参积分；绝对值分段；最值问题；导数应用
- 第一动作：先按 0<x<1 与 x>=1 判断移动分界点是否落在积分区间内并拆绝对值。
- 答案：$$f'(x)=\begin{cases}2x(2x-1),&0<x<1,\\2x,&x\ge1,\end{cases}\quad f_{\min}=\frac14$$
- 个人错因边界：pending_user_confirmation；视觉详情确认复做入口：看到积分中含 $|t^2-x^2|$ 且 $x>0$，应先按 $0<x<1$ 与 $x\ge1$ 分段拆绝对值，再求导和最值。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 分段求显式函数和导数，只回答题目所问的导数与最小值。
- 质量发现：
  - `asked_output_boundary_verified`：正式答案已删除题目未要求的最大值，只保留导数和最小值。；建议：
- 关系裁决：
  - GS-160：`add_specific_strong_edge_bidirectionally`；两题都先判断移动零点是否落入固定积分区间，再拆绝对值求导。
  - GS-288：`add_specific_strong_edge_bidirectionally`；两题都先区分积分变量与参数，并按参数相对固定区间的位置分段。
  - GS-638：`add_specific_strong_edge_bidirectionally`；几乎同构的固定区间绝对值含参积分，第一动作都是定位移动分段点。
- 当前快照：`stale`；正式卡 `0f877ee48ecd7799e360957c344b3a841879f2f932f81329cad0fb9d70ec37b8`；唯一图片 1 个；物理路径 1 个。

### GS-285 1000题B组7.1

- 题目：球半径以 $5\ \mathrm{cm/s}$ 增长，求 $r=50\ \mathrm{cm}$ 时表面积和体积的增长速度。
- 所问：球体表面积与体积相关变化率
- 知识点：一元函数微分学应用；相关变化率；复合函数求导；球体几何量公式
- 第一动作：先写球的表面积、体积关于半径的静态关系，再统一对时间求导。
- 答案：$$\frac{dS}{dt}=2000\pi\ \mathrm{cm^2/s},\quad \frac{dV}{dt}=50000\pi\ \mathrm{cm^3/s}$$
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；待用户确认的复做入口是先写球的 $S(r)$、$V(r)$，再用链式法则乘上 $dr/dt$。题解所示的“对 $r$ 求导与对时间求导混淆”只作为候选风险。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 对 S(r)、V(r) 作链式求导，最后代入半径、速度并核对单位。
- 质量发现：
  - `source_filename_title_mismatch_documented`：文件名残留 A组11.1-2，而题图、标题与详情均为 B组7.1；保留稳定路径并按题图语义审定。；建议：
- 关系裁决：
  - GS-261：`verify_existing_strong_edge`；两题都先写几何体的表面积与体积公式，再对时间求导并区分尺寸变化率。
  - GS-295：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
- 当前快照：`stale`；正式卡 `2271409b710a9a1bd09bdf28d68d7edcbe1234fb55b47fe827c8afd3b39bbe21`；唯一图片 1 个；物理路径 1 个。

### GS-286 1000题A组11.2-2

- 题目：设 $a>0$，求 $[0,a]$ 上变上限积分方程根的个数。
- 所问：变上限积分方程零点个数
- 知识点：定积分；变上限积分；零点定理；单调性；均值不等式
- 第一动作：把两个变上限积分之和定义为函数，先查端点符号再求导判单调。
- 答案：$$1\text{ 个（B）}$$
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；待用户确认的复做入口是把两个变上限积分的和定义为函数，先核对端点符号，再求导并用 $u+1/u\ge2$ 证明严格递增，从而判定唯一根。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由端点异号给存在性，由导数严格为正给唯一性。
- 质量发现：
  - `wrong_mastery_transfer_isolated`：已隔离历史误把本卡当作 GS-125 同题而迁移的掌握证据；与 GS-243 的字节同图身份继续冻结。；建议：
- 当前快照：`stale`；正式卡 `66d8f2f803c2c572fbce85b517dc9e66d41926cb3636ab24ca4066810c7f4dca`；唯一图片 1 个；物理路径 1 个。

### GS-287 57742 2026.5.6

- 题目：定义 $$ f(x)=\lim_{t\to+∞}\frac{x+2^{tx}}{1+2^{tx}}, \qquad F(x)=\int_{-1}^{x}f(t)\,dt. $$ 判断 \(F\) 在 \(x=0\) 处是可导、间断、连续但不可导，还是无法判定。
- 所问：极限定义函数与变上限积分可导性
- 知识点：定积分；变上限积分；间断点分类；导数定义；极限与连续；被积函数点值与积分函数点值区分；单点值不影响定积分
- 第一动作：先分类求出 f，再由积分定义单独计算 F(0)，不能把 f(0) 当成 F(0)。
- 答案：选 C：\(F\) 在 \(x=0\) 处连续但不可导。
- 个人错因边界：confirmed_personal；本次对 \(f\) 的分类讨论没问题；第一个真正偏离是把 \(f(0)\) 当成 \(F(0)\)。\(F(0)\) 必须由 \(\int_{-1}^{0}f(t)\,dt\) 计算，而且积分不会因被积函数在单点的取值改变。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 按积分定义求点值，再用左右差商判断连续但不可导。
- 质量发现：
  - `f0_vs_F0_user_breakpoint_verified`：用户确认的首个断点是混淆 f(0) 与 F(0)，最终选项正确不抵消推理错误。；建议：
- 关系裁决：
  - GS-573：`add_specific_strong_edge_bidirectionally`；两题都需由被积函数的单侧行为判断变上限积分函数的连续性与可导性。
  - GS-012：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
- 当前快照：`stale`；正式卡 `8cfc6a2ad2ab5f1975fb542a5570e22e7fa2ea8d5882454cfbb57a2ddd38317f`；唯一图片 1 个；物理路径 1 个。

### GS-288 1000题B组9.8（103491）含参绝对值积分

- 题目：已知 \[ f(t)=\int_0^1 t|t-x|\,dx, \] 求 \[ \int_{-1}^{2}f(t)\,dt. \]
- 所问：含参绝对值积分：先求函数表达式再积分
- 知识点：定积分；含参定积分；绝对值分类；分段函数积分；一元函数积分学的计算；积分变量与参数混淆
- 第一动作：先区分内层积分变量 x 与参数 t，求出 f(t) 的完整分段表达式。
- 答案：\(\displaystyle \frac76\)。先得 \(f(t)=\begin{cases}-t^2+\frac12t,&t<0,\\ t^3-t^2+\frac12t,&0\le t<1,\\ t^2-\frac12t,&t\ge1,\end{cases}\) 再按 \([-1,0]\)、\([0,1]\)、\([1,2]\) 积分。
- 个人错因边界：confirmed_personal；看到 \(f(t)=\int_0^1 t|t-x|dx\) 时，没有先区分积分变量 \(x\) 与参数 \(t\)，没有先求出 \(f(t)\) 的分段表达式；应先写 \(f(t)=t\int_0^1|t-x|dx\)，按 \(t<0,\,0\le t<1,\,t\ge1\) 分段，再对 \([-1,2]\) 分段积分。计算中还要逐项检查负号、减括号和系数积分。
- 一致性：题图—解析 independent_solution_assets_present；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 按 t<0、0<=t<1、t>=1 求 f(t)，再对外层区间分段积分。
- 质量发现：
  - `parameter_integral_role_chain_verified`：积分变量与参数角色、移动分段点和外层分段均已核对。；建议：
- 关系裁决：
  - GS-160：`verify_existing_strong_edge`；同为固定区间含外部参数的绝对值积分，先定位移动分段点。
  - GS-635：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；两题都先区分积分变量与外部参数，再按移动分段点拆绝对值。
  - GS-638：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；两题都对固定区间含参绝对值积分先定位分界点，再分段求函数性质。
  - GS-289：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
  - GS-290：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
- 当前快照：`stale`；正式卡 `3cad53d61abdae7e01b0995289070282e619b280fcc7e18eac90bb2054f395c8`；唯一图片 3 个；物理路径 3 个。

### GS-289 1000题B组9.22（103257）卷积分段点解耦

- 题目：设 \[ f(x)=x,\qquad g(x)= \begin{cases} \cos x,&x\le\pi,\\ 0,&x>\pi, \end{cases} \] 求 \[ F(x)=\int_0^x f(t)g(x-t)\,dt,\qquad x\ge0. \]
- 所问：卷积型含参定积分：复合自变量分段函数积分
- 知识点：定积分；定积分性质；含参定积分；分段函数积分；卷积型积分；第二类换元；分部积分；一元函数积分学的计算
- 第一动作：先令 u=x-t 解耦 g 的复合输入，再把分段点映射到 u 轴。
- 答案：\(\displaystyle F(x)=\begin{cases}1-\cos x,&0\le x\le\pi,\\2,&x>\pi.\end{cases}\)
- 个人错因边界：confirmed_personal；看到 \(g(x-t)\) 是分段函数时，没有先区分“\(g\) 的自变量”和“积分变量 \(t\)”；\(\pi\) 是 \(g\) 的输入变量 \(u=x-t\) 的分段点，不是原 \(t\) 轴上的直接分段点。应先令 \(u=x-t\)，把 \(g(x-t)\) 化为 \(g(u)\)，再按 \(u=\pi\) 讨论 \([0,x]\) 是否跨过分段点。
- 一致性：题图—解析 independent_solution_assets_present；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 换元后按 u=pi 分段，计算并还原累计积分函数 F。
- 质量发现：
  - `source_F_prime_mislabel_corrected`：来源解析图把累计函数 F 多处误标为 F'；正式卡按题目定义统一为 F。；建议：
- 关系裁决：
  - GS-201：`verify_existing_strong_edge`；共同第一动作是换元解耦复合输入的变量角色。
  - GS-291：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；两题都先把复合平移输入换到新变量轴，再按映射后的分段点积分。
  - GS-290：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
  - GS-292：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
- 当前快照：`stale`；正式卡 `8f266eb8f7cc861c967e5b09cea67840ecbab0a1fcfbb217da55d662f7ed1712`；唯一图片 3 个；物理路径 3 个。

### GS-290 强化例题9.20(90116)分段原函数连续拼接

- 题目：已知 \[ f(x)= \begin{cases} \dfrac{1}{\sqrt{1+x^2}}, & x\le0,\\ (x+1)\cos x, & x>0, \end{cases} \] 求 \(f(x)\) 的一个原函数。
- 所问：分段函数求原函数：分段积分后连续性拼接常数
- 知识点：不定积分；原函数；分段函数连续可导；极限与连续；一元函数积分学的计算；分部积分；分段函数积分
- 第一动作：分段积分后保留 C1、C2，并把原函数连续写成左右极限方程。
- 答案：D。分段积分得 \(x\le0\)：\(\ln(\sqrt{1+x^2}+x)+C_1\)；\(x>0\)：\((x+1)\sin x+\cos x+C_2\)。原函数在 \(x=0\) 处连续，故 \(C_1=1+C_2\)。取 \(C_2=0\) 时 \(C_1=1\)，对应 D。
- 个人错因边界：confirmed_personal；知道要用连续性，但没有把连续性落成 \(F(0^-)=F(0^+)\) 的左右极限方程；分段求原函数后应保留 \(C_1,C_2\)，在 \(x=0\) 代入得到 \(C_1=1+C_2\)，再筛选常数。
- 一致性：题图—解析 independent_solution_assets_present；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 分段求原函数并由 F(0-)=F(0+)匹配积分常数。
- 质量发现：
  - `primitive_continuity_equation_verified`：用户确认的首个断点是没有把连续性落实成左右极限方程。；建议：
- 关系裁决：
  - GS-574：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；两题都分段求原函数，并在分段点用连续性方程匹配积分常数。
  - GS-523：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
  - GS-572：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
  - GS-573：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
- 当前快照：`stale`；正式卡 `de24b9af12ff0acfa1e4df433fb1af83969a42ed080953a211f65b2ffcd5a003`；唯一图片 3 个；物理路径 3 个。

### GS-291 强化例题9.21(19899)

- 题目：设 $f(x)=e^{-x}\ (x\ge0)$，$f(x)=1+x^2\ (x<0)$，求 $\int_{-2}^2f(x-1)dx$。
- 所问：分段函数平移定积分
- 知识点：定积分；分段函数积分；换元；平移变换
- 第一动作：先令 u=x-1 同步平移积分区间，再按 u=0 分段。
- 答案：$$\int_{-2}^{2}f(x-1)dx=13-e^{-1}$$
- 个人错因边界：pending_user_confirmation；旧卡未保存用户当时个人错因；安全复做入口是看到 $f(x-1)$ 的积分，先令 $u=x-1$ 改区间，再按分段点 $u=0$ 拆开积分，是否曾断在此处仍待用户确认。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 把区间平移为 [-3,1]，按 u=0 拆分并计算。
- 质量发现：
  - `shifted_breakpoint_verified`：平移换元后的新区间与分段点已核对。；建议：
- 当前快照：`stale`；正式卡 `e1e2b428f9acf7a72eaf8977c67eb7ff6024a4fc627283b3d71e65d8d049a661`；唯一图片 1 个；物理路径 1 个。

### GS-292 强化例题9.22（77306）根号二次式三角换元绝对值

- 题目：计算定积分 \[ \int_0^1\sqrt{2x-x^2}\,dx. \]
- 所问：根号二次式定积分：配方 + 三角换元 + 绝对值符号判断
- 知识点：定积分；一元函数积分学的计算；根式积分；第二类换元；三角换元；绝对值分类；积分保号；三角恒等变形
- 第一动作：先配方和平移，再选择使 cos 符号稳定的三角换元分支。
- 答案：\(\displaystyle \frac{\pi}{4}\)
- 个人错因边界：confirmed_personal；三角换元时只检查端点角度是否满足 \(\sin t=-1,0\)，没有检查所选角度区间内 \(\cos t\) 的符号。取 \(t:\frac{3\pi}{2}\to0\) 这一分支本身并非非法；真正错误是没有保留 \(\sqrt{\cos^2t}=|\cos t|\) 并按符号分段，直接把它写成 \(\cos t\)。更稳的做法是令 \(u=x-1=\sin t\)，选 \(t\in[-\frac{\pi}{2},0]\)，确保 \(\cos t\ge0\)。
- 一致性：题图—解析 independent_solution_assets_present；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 保留 sqrt(cos^2 t)=|cos t|，在符号稳定分支上计算。
- 质量发现：
  - `absolute_value_branch_and_external_cleanup_verified`：用户确认的首个断点是漏写 sqrt(cos^2 t)=|cos t|；并清理 GS-636 的外部单向宽边。；建议：
- 关系裁决：
  - GS-592：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；两题都先配方再作三角换元，并检查根号化简时的符号条件。
  - GS-633：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；两题都把根号二次式配方和平移到标准圆结构，再选择稳定换元。
  - GS-600：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
  - GS-618：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
  - GS-619：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
  - GS-292：`remove_external_inbound_only_broad_edge`；外部端点仅单向指向本批卡，未共享足够具体的对象、条件与第一动作，按 external_inbound_cleanup 删除。
- 当前快照：`stale`；正式卡 `60e1bcbf37546bf148eda3557e634e4297f1782159d7b357f14a3aebf1575e73`；唯一图片 2 个；物理路径 2 个。

### GS-293 强化例题11.12（还原对称性）

- 题目：计算 $\int_0^4 x\sqrt{4x-x^2}\,dx$。
- 所问：根式定积分几何法计算
- 知识点：定积分；定积分性质；第二类换元
- 第一动作：先把根号内二次式配成圆并平移到对称区间。
- 答案：$4\pi$
- 个人错因边界：pending_user_confirmation；旧卡未保存用户当时个人错因；安全复做入口是先把根号内二次式配成圆并平移到对称区间，再用奇偶性消项，是否曾断在此处仍待用户确认。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 平移后用奇偶性消去奇项，并以半圆面积收口。
- 质量发现：
  - `exact_duplicate_identity_mirrored`：与 GS-327 的题图字节相同且数学同题；双向身份元数据已镜像并冻结普通聚合边。；建议：
- 关系裁决：
  - GS-577：`remove_identity_or_broad_edge`；涉及身份冻结卡或仅共享宽泛积分标签，不再保留普通语义边。
  - GS-634：`remove_identity_or_broad_edge`；涉及身份冻结卡或仅共享宽泛积分标签，不再保留普通语义边。
- 当前快照：`stale`；正式卡 `1821b83bb418d6d10ad739611d0d1bc2d0a70879d10ce3ba0a12406d3ce8a0a0`；唯一图片 1 个；物理路径 1 个。

### GS-294 2019年数2第19题：绝对值面积与几何级数

- 题目：设 \(n\) 为正整数，\(S_n\) 是曲线 \(y=e^{-x}\sin x\) 在 \(0\le x\le n\pi\) 内与 \(x\) 轴所围成图形的面积，求 \(S_n\) 与 \(\lim_{n\to\infty}S_n\)。
- 所问：含绝对值面积积分与级数求和
- 知识点：定积分；定积分应用；平面图形面积；绝对值分段；等比级数
- 第一动作：先用区间可加性把总面积拆成 n 个长度为 pi 的分段面积。
- 答案：\(\displaystyle S_n=\frac{1+e^{-\pi}}{2}\cdot\frac{1-e^{-n\pi}}{1-e^{-\pi}},\quad \lim_{n\to\infty}S_n=\frac{e^\pi+1}{2(e^\pi-1)}\)
- 个人错因边界：confirmed_personal；已识别 \(|\sin x|\) 的周期性和指数衰减，却没有先用定积分区间可加性写成 \(\sum_{k=0}^{n-1}\int_{k\pi}^{(k+1)\pi}\)，因而一开始不知道如何把总面积转成等比数列。
- 一致性：题图—解析 independent_solution_assets_present；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 逐段面积形成等比数列，先求有限和再取极限。
- 质量发现：
  - `interval_additivity_breakpoint_verified`：用户确认的首个断点是未主动用区间可加性拆分总面积。；建议：
- 关系裁决：
  - GS-185：`verify_existing_strong_edge`；同为利用定积分的带符号面积比较候选区间的净贡献。
  - GS-191：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
- 当前快照：`stale`；正式卡 `35dbab2de48ccef3b75e6f9d8be4c82258c6a6e0e9009e44378337a92ec7603c`；唯一图片 2 个；物理路径 2 个。

### GS-295 2018年数2第20题：面积变化率

- 题目：曲线 \(L:y=\frac49x^2\,(x\ge0)\)，点 \(O(0,0)\)、\(A(0,1)\)，点 \(P\) 在曲线 \(L\) 上运动。设 \(S\) 为 \(OA\)、\(AP\) 与曲线 \(L\) 围成的面积。当 \(P=(3,4)\)、\(\frac{dx}{dt}=4\) 时，求 \(\frac{dS}{dt}\)。
- 所问：曲边图形面积的相关变化率
- 知识点：定积分应用；平面图形面积；变上限积分；相关变化率
- 第一动作：先把封闭区域写成真实面积函数 S(x)，再用链式法则求 dS/dt。
- 答案：\(10\)
- 个人错因边界：pending_user_confirmation；旧卡没有保存用户当时个人错因；安全复做入口是先写出封闭区域面积函数 \(S(x)\)，再用链式法则计算 \(\frac{dS}{dt}\)，是否曾断在此处仍待用户确认。
- 一致性：题图—解析 independent_solution_assets_present；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 用梯形面积减曲边面积得到 S(x)，再乘 dx/dt。
- 质量发现：
  - `area_rate_model_verified`：真实面积函数与时间链式求导已核对。；建议：
- 当前快照：`stale`；正式卡 `1ef5d14fd6379e3d663c5e7ce46cdfc192c1d82e3f2ad2ba763ad203d085313e`；唯一图片 2 个；物理路径 2 个。

### GS-296 2023年真题第19题

- 题目：无界区域 $0\le y\le \frac1{x\sqrt{1+x^2}},\ x\ge1$ 的面积及绕 $x$ 轴旋转体体积。
- 所问：无界区域面积与旋转体体积
- 知识点：定积分；定积分应用；旋转体体积；反常积分
- 第一动作：分别建立面积反常积分与圆盘法体积反常积分。
- 答案：面积 $S=\ln(1+\sqrt2)$，绕 $x$ 轴旋转体体积 $V=\pi-\frac{\pi^2}{4}$。
- 个人错因边界：pending_user_confirmation；旧卡未保存用户当时个人错因；安全复做入口是分别建立面积反常积分与圆盘法体积反常积分，是否曾断在此处仍待用户确认。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 面积用一阶高度、体积用高度平方，分别在无界上限收口。
- 质量发现：
  - `improper_area_volume_models_verified`：面积和旋转体体积的积分对象、反常上限与平方因子已核对。；建议：
- 关系裁决：
  - GS-304：`add_specific_strong_edge_bidirectionally`；两题都对无界区域分别建立面积或旋转体体积反常积分并检查收敛。
- 当前快照：`stale`；正式卡 `7056b9998ee1935f06ada4f46e9660329ec0feefe88ab9ae52267de74700adac`；唯一图片 1 个；物理路径 1 个。

### GS-297 2020年第18题：函数方程反解与旋转体体积

- 题目：函数 \(f(x)\) 在 \((0,+\infty)\) 上满足 \[ 2f(x)+x^2f\!\left(\frac1x\right)=\frac{x^2+2x}{\sqrt{1+x^2}}. \] 求 \(f(x)\)，并求由 \(y=f(x)\)、\(y=\frac12\)、\(y=\frac{\sqrt3}{2}\)、\(y\) 轴围成区域绕 \(x\) 轴旋转所得旋转体体积。
- 所问：函数方程反解与旋转体体积
- 知识点：定积分；函数方程；旋转体体积；水平壳法；三角换元
- 第一动作：先作 x 到 1/x 的替换，构造同伴方程再联立消元。
- 答案：\(\displaystyle f(x)=\frac{x}{\sqrt{1+x^2}},\quad V=\frac{\pi^2}{6}\)
- 个人错因边界：pending_user_confirmation；旧卡没有保存用户当时个人错因；复做时要先对含 \(f(1/x)\) 的方程补写 \(x\mapsto 1/x\) 的同伴方程，再反解曲线用于体积积分。
- 一致性：题图—解析 independent_solution_assets_present；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 消元求 f，反解 x(y)，再以水平壳法计算旋转体体积。
- 质量发现：
  - `involution_elimination_and_shell_method_verified`：函数方程同伴消元与水平壳法的变量选择已核对。；建议：
- 关系裁决：
  - GS-122：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；同为函数方程中同时出现 x 与 1/x，需先构造互逆替换方程组再消元。
  - GS-304：`remove_broad_or_method_mismatched_edge`；只共享宽泛章节、局部工具或最终函数类型，具体对象、条件与第一动作不一致。
- 当前快照：`stale`；正式卡 `7d435a1710e904a201598b319504c2899eb78120f30dd1d1c6854acd04a3907b`；唯一图片 2 个；物理路径 2 个。

### GS-298 1000题强化10.21：以 y 为参数的弧长与最值

- 题目：曲线 \(x=x(y)\) 满足微分关系，\(-2\le y\le-1\)，且 \(x(-1)=-\frac9{16}\)。求曲线弧长 \(s\) 与 \(x\) 的最大值。
- 所问：以 \(y\) 为参数的弧长与最大值
- 知识点：由微分关系求 \(\frac{dx}{dy}\)；以 \(y\) 为参数的曲线；曲线弧长；单调性与极值
- 第一动作：先由微分关系整理 dx/dy，并以 y 为参数建立弧长积分。
- 答案：\(\displaystyle s=\frac{21}{16},\quad x_{\max}=-\frac3{4^{4/3}}\)
- 个人错因边界：pending_user_confirmation；旧卡没有保存用户当时个人错因；安全复做入口是由微分关系求 \(\frac{dx}{dy}\)，再按以 \(y\) 为参数的弧长公式和一元最值链计算，是否曾断在此处仍待用户确认。
- 一致性：题图—解析 independent_solution_assets_present；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 以 y 为参数算弧长，再积分得到 x(y) 并检查内部驻点。
- 质量发现：
  - `yaml_and_y_parameter_arc_length_verified`：当前 YAML 已修复并现场解析；dx/dy 与 y 参数角色、弧长和内部最值均已核对。；建议：
- 关系裁决：
  - GS-682：`verify_existing_strong_edge`；两题都以 y 为参数写 dx/dy，并据此进入曲线弧长或几何量计算。
- 当前快照：`stale`；正式卡 `c0a87b984eeda5247acec397cd86c67c1a754ab0aa609214ca803ae71c812e78`；唯一图片 2 个；物理路径 2 个。

### GS-299 1000题10.23：由微分方程生成曲线弧长

- 题目：设非负函数 \(y(x)\) 是微分方程 \(2yy'=\cos x\) 满足 \(y(0)=0\) 的解，求曲线 \[ f_n(x)=n\int_0^{x/n}y(t)\,dt,\qquad 0\le x\le n\pi \] 的弧长。
- 所问：由微分方程生成积分曲线弧长
- 知识点：定积分；曲线弧长；变上限积分；微分方程的定义区间
- 第一动作：先检查经典端点解边界，再在命题意图区间内由微分方程求生成函数。
- 答案：命题意图下为 \(4n\)
- 个人错因边界：pending_user_confirmation；旧卡没有保存用户当时个人错因；安全复做入口是在命题意图的区间解释下先得到 \(y=\sqrt{\sin x}\)，再对变上限积分求导进入弧长公式，是否曾断在此处仍待用户确认。
- 一致性：题图—解析 independent_solution_assets_present；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 在开区间解出 y，变上限求导后用半角恒等式计算弧长。
- 质量发现：
  - `classical_endpoint_no_solution_boundary_documented`：若要求方程在 x=0 经典可微则无解；正式答案明确采用开区间方程加闭区间连续端点的命题意图。；建议：
- 关系裁决：
  - GS-300：`verify_existing_strong_edge`；两题都先由微分方程确定生成曲线，再进入变上限积分与弧长计算。
  - GS-190：`verify_existing_strong_edge`；共同动作链是先由微分方程确定曲线，再进入弧长积分。
- 当前快照：`stale`；正式卡 `e201e439383c8ab28ef3c60824fc179f399cb913a529881cf8ce3268c9c9f381`；唯一图片 2 个；物理路径 2 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
