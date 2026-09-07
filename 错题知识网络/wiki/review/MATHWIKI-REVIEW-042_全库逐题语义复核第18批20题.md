---
wiki_id: MATHWIKI-REVIEW-042
type: target_level_semantic_review_batch
title: 全库逐题语义复核第18批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-042_全库逐题语义复核第18批20题.json
status: active
last_updated: 2026-07-23
---

# 全库逐题语义复核第18批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 12 张；覆盖 38 个物理图片路径与 38 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 1 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `MATH-TARGET-SEMANTIC-CLOSEOUT-20260723-B18`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-186](http://127.0.0.1:8765/open/GS-186) | 定积分数值 | 定积分区间可加性、平移换元、函数差分关系 | \(\frac12\) | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先把目标积分拆成相差 2 的同长区间，再平移回已知差分区间” | interval_translation_chain_verified |
| [GS-187](http://127.0.0.1:8765/open/GS-187) | 局部隐式通解 | 齐次型一阶微分方程、变量代换、局部分支 | \(\arctan(y/x)+\frac12\ln(x^2+y^2)=C\)，在避开原点且 \(x\ne0\) 的连续分支上成立。 | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先整理成 \(y'=F(y/x)\)，令 \(u=y/x\)” | local_angle_branch_and_origin_boundary_repaired |
| [GS-188](http://127.0.0.1:8765/open/GS-188) | 隐式特解 | 平移化齐次、齐次型一阶微分方程、初值与奇异直线 | \((y+2x-3)^2(4y-x-3)=5\) | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先求分子、分母两条直线的交点并平移坐标” | source_solution_intermediate_sign_typo_documented |
| [GS-189](http://127.0.0.1:8765/open/GS-189) | 充要性选项与证明 | 一阶线性齐次方程、周期解、周期函数一周期积分 | C：\(\int_0^T p(t)\,dt=0\) 是存在非零 \(T\) 周期解的充分必要条件。 | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先写非零通解，再比较 \(y(x+T)/y(x)\)” | periodic_solution_necessity_sufficiency_completed |
| [GS-190](http://127.0.0.1:8765/open/GS-190) | 曲线弧长 | 一阶线性微分方程、初值问题、曲线弧长 | \(\frac14e^2+\frac14\) | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先把方程化为一阶线性标准型并解出 \(y(x)\)” | arc_length_positive_root_domain_verified |
| [GS-191](http://127.0.0.1:8765/open/GS-191) | 全局值域 | 一阶线性微分方程、衰减振荡函数、全局值域 | \(y(x^2)\in[-\frac{\sqrt2}{2}e^{-5\pi/4},\frac{\sqrt2}{2}e^{-\pi/4}]\) | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先解方程，再令 \(t=x^2\ge0\) 化为单变量全局极值” | question_only_global_range_independently_verified |
| [GS-193](http://127.0.0.1:8765/open/GS-193) | 函数解 | 二阶可降阶微分方程、不显含自变量、分支保护 | \(y=\frac14(x-1)^2+1\) | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“令 \(p=y'=p(y)\)，写 \(y''=p\,dp/dy\)” | same_equation_distinct_geometric_domain_documented |
| [GS-195](http://127.0.0.1:8765/open/GS-195) | 微分方程选项 | 常系数线性微分方程、特征根重数、共轭复根 | A：\(y^{(4)}-2y'''+5y''-8y'+4y=0\) | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“把每个特解翻译成特征根及重数” | characteristic_root_multiplicity_reverse_proof_completed |
| [GS-196](http://127.0.0.1:8765/open/GS-196) | 通解 | 常系数齐次方程、特征方程、共轭复根实解 | \(y=C_1e^x+e^{-x/2}(C_2\cos(\sqrt3x/2)+C_3\sin(\sqrt3x/2))\) | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先写并分解特征方程 \(r^3-1=0\)” | real_and_complex_root_solution_roles_verified |
| [GS-197](http://127.0.0.1:8765/open/GS-197) | 参数组 | 通解反推特征方程、二重根、特解代回 | \((a,b,c)=(2,1,4)\) | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先从齐次部分读出 \(-1\) 是二重特征根” | homogeneous_and_particular_parameter_roles_verified |
| [GS-198](http://127.0.0.1:8765/open/GS-198) | 带定义域的实通解 | 指数换元、一阶线性微分方程、对数定义域 | \(y=\ln[\frac12(\sin x-\cos x)+Ce^{-x}]\)，仅在括号内为正的各连通区间成立。 | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“两边乘 \(e^y\)，令 \(z=e^y\)” | real_solution_positivity_domain_repaired |
| [GS-199](http://127.0.0.1:8765/open/GS-199) | 特解与端点 | 根式整体换元、初值问题、非Lipschitz端点与分支 | \(y=(x/2+1)^2-x^2\) | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“令 \(u=y+x^2\)，把根号整体化为 \(u'=\sqrt u\)” | non_lipschitz_endpoint_direct_verification_completed |
| [GS-200](http://127.0.0.1:8765/open/GS-200) | 函数与定积分 | 欧拉方程、变量角色、常系数方程与定积分 | \(y(x)=2x^3\)，积分值为 \(22\sqrt3/5\)。 | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“令 \(t=\ln x\)，另记 \(Y(t)=y(e^t)\)” | question_only_euler_variable_roles_verified |
| [GS-201](http://127.0.0.1:8765/open/GS-201) | 函数与参数 | Volterra积分方程、Leibniz求导、一阶线性微分方程 | \(f(x)=2a(1-e^{-x})\)，\(a=e/2\)。 | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先换元把 \(f(x-t)\) 改写成统一积分变量，再整体求导” | volterra_leibniz_regularization_chain_completed |
| [GS-202](http://127.0.0.1:8765/open/GS-202) | 函数、极小值与等号条件 | 乘法型函数方程、导数定义、基点可导性迁移、极值 | \(f(x)=ex\ln x\)；当 \(xy=e^{-1}\) 时极小值为 \(-1\)。 | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先取特殊值得 \(f(1)=0\)，再用差商把任意点可导性化归到基点 1” | basepoint_differentiability_proof_repaired |
| [GS-203](http://127.0.0.1:8765/open/GS-203) | 曲线、最值点与最小面积 | 切线截距、几何建模、一阶线性微分方程、面积最值 | \(y=x(2-\ln x),x>e\)；最小面积点 \((e^{3/2},e^{3/2}/2)\)，最小面积 \(e^3\)。 | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“写切点处切线并令一般点横坐标为 0 求纵轴截距” | original_positive_domain_restored |
| [GS-204](http://127.0.0.1:8765/open/GS-204) | 带几何定义域的曲线 | 曲率公式、切线倾角、二阶不显含自变量降阶 | \(y=\frac14(x-1)^2+1,\ x\ge1\) | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“把曲率与 \(\cos\alpha\) 全部写成 \(y',y''\)” | source_solution_angle_variable_typo_documented |
| [GS-205](http://127.0.0.1:8765/open/GS-205) | 曲线族与条件边界 | 切线横截距、面积积分方程、二阶降阶、端点条件 | 按官方题意的内点解释，\(f(x)=Cx^3,C>0\)。 | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先求切线横截距并把两块面积写成积分关系” | source_stem_endpoint_derivative_ambiguity |
| [GS-206](http://127.0.0.1:8765/open/GS-206) | 选择项与速度 | 牛顿第二定律、链式换元、渐近总位移 | B：\(v(0)/2\) | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“因目标按位移给出，把 \(v\) 看成 \(x\) 的函数并写 \(dv/dt=v\,dv/dx\)” | asymptotic_total_displacement_and_option_label_repaired |
| [GS-207](http://127.0.0.1:8765/open/GS-207) | 轨迹与定义域 | 追踪曲线、切线方向、平方根分支、定义域 | \(y=\ln\frac{1+\sqrt{1-x^2}}x-\sqrt{1-x^2},\ 0<x\le1\) | pending_user_confirmation：pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“把指向关系翻译成轨迹切线斜率，再联立距离约束” | trajectory_sign_branch_and_domain_verified |

## 逐题复核

### GS-186 2023年第15题 平移差分定积分求值

- 题目：利用函数平移差分关系与已知区间积分求目标定积分。
- 所问：定积分数值
- 知识点：定积分区间可加性；平移换元；函数差分关系
- 第一动作：先把目标积分拆成相差 2 的同长区间，再平移回已知差分区间
- 答案：\(\frac12\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先把目标积分拆成相差 2 的同长区间，再平移回已知差分区间”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 用已知积分拆补目标区间。
  - 把平移后的区间统一到同一变量。
  - 对差分关系积分并求值。
- 质量发现：
  - `interval_translation_chain_verified`：区间拆补、平移换元与差分关系积分已逐步核对。；建议：
- 关系裁决：
  - GS-678：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
  - GS-310：`remove_broad_or_method_mismatched_edge`；
  - GS-311：`remove_broad_or_method_mismatched_edge`；
  - GS-338：`remove_broad_or_method_mismatched_edge`；
  - GS-575：`remove_broad_or_method_mismatched_edge`；
- 当前快照：`stale`；正式卡 `aab84c412d5cf809d2ae55f3a552a8926afab98eaeeb86a44c4f97b8b0abc442`；唯一图片 2 个；物理路径 2 个。

### GS-187 强化例题15.1（2️⃣（1））

- 题目：求齐次型一阶微分方程的局部隐式通解。
- 所问：局部隐式通解
- 知识点：齐次型一阶微分方程；变量代换；局部分支
- 第一动作：先整理成 \(y'=F(y/x)\)，令 \(u=y/x\)
- 答案：\(\arctan(y/x)+\frac12\ln(x^2+y^2)=C\)，在避开原点且 \(x\ne0\) 的连续分支上成立。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先整理成 \(y'=F(y/x)\)，令 \(u=y/x\)”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 令 \(u=y/x\)，写出 \(y'=u+xu'\)。
  - 分离变量并积分。
  - 检查 \(x\ne0\)、原点与反正切连续分支。
- 质量发现：
  - `local_angle_branch_and_origin_boundary_repaired`：已补明 x 不等于 0、避开原点及反正切连续分支的局部解边界。；建议：
- 关系裁决：
  - GS-188：`verify_existing_strong_edge`；
- 当前快照：`current`；正式卡 `649a3a35a27d3987420785fc2292f29e64d69a3325a7d37eca2134a7b954c228`；唯一图片 2 个；物理路径 2 个。

### GS-188 强化例题15.2（3️⃣C）

- 题目：把一次式比值型一阶微分方程平移化齐次，并由初值确定解。
- 所问：隐式特解
- 知识点：平移化齐次；齐次型一阶微分方程；初值与奇异直线
- 第一动作：先求分子、分母两条直线的交点并平移坐标
- 答案：\((y+2x-3)^2(4y-x-3)=5\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先求分子、分母两条直线的交点并平移坐标”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 求两直线交点并平移。
  - 再令 \(U=Y/X\) 化齐次。
  - 用初值定常数并保护原方程分母非零的局部解支。
- 质量发现：
  - `source_solution_intermediate_sign_typo_documented`：解析中间行分母符号应为 2+4U；后续计算和最终答案按正确符号成立。；建议：
- 当前快照：`current`；正式卡 `b8c26c1a87cea1b8c4ddca765cc40607cadfd150c3b4e73043d7f9e3a98f6fa6`；唯一图片 2 个；物理路径 2 个。

### GS-189 强化例题15.3

- 题目：判定一阶线性齐次方程存在非零周期解的条件是充分、必要还是充要。
- 所问：充要性选项与证明
- 知识点：一阶线性齐次方程；周期解；周期函数一周期积分
- 第一动作：先写非零通解，再比较 \(y(x+T)/y(x)\)
- 答案：C：\(\int_0^T p(t)\,dt=0\) 是存在非零 \(T\) 周期解的充分必要条件。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先写非零通解，再比较 \(y(x+T)/y(x)\)”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 写指数形式通解。
  - 利用周期性把任意一周期积分化为固定区间积分。
  - 用实指数等于 1 当且仅当指数为 0 同时证明充分性与必要性。
- 质量发现：
  - `periodic_solution_necessity_sufficiency_completed`：已用非零通解比值同时证明一周期积分为零的充分性与必要性。；建议：
- 关系裁决：
  - GS-572：`add_specific_strong_edge_bidirectionally`；
  - GS-190：`remove_broad_or_method_mismatched_edge`；
- 当前快照：`current`；正式卡 `a29a972e1fad434470c360eaa6e04f30e00e81d893975475e5edf6e9fdeaaeb4`；唯一图片 2 个；物理路径 2 个。

### GS-190 强化例题15.4

- 题目：先解一阶线性微分方程确定曲线，再求指定区间弧长。
- 所问：曲线弧长
- 知识点：一阶线性微分方程；初值问题；曲线弧长
- 第一动作：先把方程化为一阶线性标准型并解出 \(y(x)\)
- 答案：\(\frac14e^2+\frac14\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先把方程化为一阶线性标准型并解出 \(y(x)\)”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 解方程得 \(y=-\frac12\ln x+\frac14x^2\)。
  - 由 \(x>0\) 确定弧长根式的正号。
  - 积分得到弧长。
- 质量发现：
  - `arc_length_positive_root_domain_verified`：已明确 x 大于 0 才能把弧长根式取为正的 x/2+1/(2x)。；建议：
- 关系裁决：
  - GS-164：`verify_existing_strong_edge`；
  - GS-299：`add_specific_strong_edge_bidirectionally`；
- 当前快照：`current`；正式卡 `a73e98a404787a820b080401f56edf0428e6d4988bf71d7618640619ff5b1a3c`；唯一图片 2 个；物理路径 2 个。

### GS-191 1000题B组5.22

- 题目：解给定一阶线性微分方程，并求复合函数 \(y(x^2)\) 的全局值域。
- 所问：全局值域
- 知识点：一阶线性微分方程；衰减振荡函数；全局值域
- 第一动作：先解方程，再令 \(t=x^2\ge0\) 化为单变量全局极值
- 答案：\(y(x^2)\in[-\frac{\sqrt2}{2}e^{-5\pi/4},\frac{\sqrt2}{2}e^{-\pi/4}]\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先解方程，再令 \(t=x^2\ge0\) 化为单变量全局极值”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 求得 \(y=e^{-x}\sin x\)。
  - 列出全部驻点 \(t_k=\pi/4+k\pi\)。
  - 用 \(e^{-\pi}\) 衰减比较极值序列并检查端点。
- 质量发现：
  - `question_only_global_range_independently_verified`：仅有题图；本轮独立列出全部驻点、衰减序列和端点，完成全局值域证明。；建议：
- 关系裁决：
  - GS-164：`verify_existing_strong_edge`；
  - GS-294：`add_specific_strong_edge_bidirectionally`；
  - GS-209：`remove_broad_or_method_mismatched_edge`；
  - GS-515：`remove_broad_or_method_mismatched_edge`；
  - GS-545：`remove_broad_or_method_mismatched_edge`；
- 当前快照：`stale`；正式卡 `464bd48a0f265cd9f50cad733986c81bf0e8c70a0da23540de487bd8460427b9`；唯一图片 1 个；物理路径 1 个。

### GS-193 强化例题15.6（2）：二阶不显含自变量微分方程

- 题目：求不显含自变量的二阶微分方程初值解。
- 所问：函数解
- 知识点：二阶可降阶微分方程；不显含自变量；分支保护
- 第一动作：令 \(p=y'=p(y)\)，写 \(y''=p\,dp/dy\)
- 答案：\(y=\frac14(x-1)^2+1\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“令 \(p=y'=p(y)\)，写 \(y''=p\,dp/dy\)”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 用 \(p(y)\) 降阶并分离变量。
  - 用 \(y(3)=2,y'(3)=1\) 定常数与分支。
  - 再积分恢复 \(y(x)\)。
- 质量发现：
  - `same_equation_distinct_geometric_domain_documented`：与 GS-204 共享方程和解，但本题没有 GS-204 的额外几何域限制。；建议：
- 关系裁决：
  - GS-204：`verify_existing_strong_edge`；
- 当前快照：`stale`；正式卡 `228323ecd713817ad76f8c9869172dd3ebe5219458b733552ec37dd93eb00377`；唯一图片 2 个；物理路径 2 个。

### GS-195 强化例题15.10：常系数特征根反推方程

- 题目：由两个特解反推四阶常系数齐次线性微分方程。
- 所问：微分方程选项
- 知识点：常系数线性微分方程；特征根重数；共轭复根
- 第一动作：把每个特解翻译成特征根及重数
- 答案：A：\(y^{(4)}-2y'''+5y''-8y'+4y=0\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“把每个特解翻译成特征根及重数”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由 \(te^t\) 得 \(P(1)=P'(1)=0\)。
  - 由 \(\sin2t\) 得 \(\pm2i\) 为根。
  - 构造并展开首一特征多项式。
- 质量发现：
  - `characteristic_root_multiplicity_reverse_proof_completed`：由 te^t 严格得到 P(1)=P'(1)=0，并由正弦解得到共轭复根。；建议：
- 关系裁决：
  - GS-197：`verify_existing_strong_edge`；
  - GS-196：`remove_broad_or_method_mismatched_edge`；
- 当前快照：`current`；正式卡 `48f616b23cbcd09b9ab84250d6988a4c788b5f3b96bc41c1154a8032e7f7a78d`；唯一图片 2 个；物理路径 2 个。

### GS-196 2021年第十五题：三阶常系数齐次线性微分方程

- 题目：求三阶常系数齐次线性方程 \(y'''-y=0\) 的实函数通解。
- 所问：通解
- 知识点：常系数齐次方程；特征方程；共轭复根实解
- 第一动作：先写并分解特征方程 \(r^3-1=0\)
- 答案：\(y=C_1e^x+e^{-x/2}(C_2\cos(\sqrt3x/2)+C_3\sin(\sqrt3x/2))\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先写并分解特征方程 \(r^3-1=0\)”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 求出一个实根和一对共轭复根。
  - 分别写实指数解与衰减振荡实解。
  - 用三个任意常数组成三阶通解。
- 质量发现：
  - `real_and_complex_root_solution_roles_verified`：三个特征根及其对应的一个实指数解和一对实振荡解已逐一核对。；建议：
- 关系裁决：
  - GS-520：`add_specific_strong_edge_bidirectionally`；
  - GS-197：`remove_broad_or_method_mismatched_edge`；
- 当前快照：`stale`；正式卡 `b769028645ec87e0984a19e3c5747f2564a04743d3b5ac684feba96b786df504`；唯一图片 2 个；物理路径 2 个。

### GS-197 2019年第四题：由通解反求常系数微分方程参数

- 题目：由二阶非齐次方程的通解反求参数 \(a,b,c\)。
- 所问：参数组
- 知识点：通解反推特征方程；二重根；特解代回
- 第一动作：先从齐次部分读出 \(-1\) 是二重特征根
- 答案：\((a,b,c)=(2,1,4)\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先从齐次部分读出 \(-1\) 是二重特征根”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由齐次通解确定 \(a=2,b=1\)。
  - 把特解 \(e^x\) 代回原方程。
  - 单独得到 \(c=4\)。
- 质量发现：
  - `homogeneous_and_particular_parameter_roles_verified`：齐次部分只用于确定 a,b，非齐次特解代回只用于确定 c。；建议：
- 当前快照：`current`；正式卡 `43d7d0b4031763c760de094c6b9fefbf61bbeb3f67fe579e0b852c208563a51f`；唯一图片 2 个；物理路径 2 个。

### GS-198 强化例题15.11：指数换元化一阶线性

- 题目：求 \(y'+1=e^{-y}\sin x\) 的实通解。
- 所问：带定义域的实通解
- 知识点：指数换元；一阶线性微分方程；对数定义域
- 第一动作：两边乘 \(e^y\)，令 \(z=e^y\)
- 答案：\(y=\ln[\frac12(\sin x-\cos x)+Ce^{-x}]\)，仅在括号内为正的各连通区间成立。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“两边乘 \(e^y\)，令 \(z=e^y\)”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 化为 \(z'+z=\sin x\)。
  - 求出 \(z\) 的通解。
  - 用 \(z=e^y>0\) 筛选实解区间。
- 质量发现：
  - `real_solution_positivity_domain_repaired`：形式等式 e^y=z 已补为仅在 z 大于 0 的连通区间上可回写实对数解。；建议：
- 关系裁决：
  - GS-199：`remove_broad_or_method_mismatched_edge`；
  - GS-201：`remove_broad_or_method_mismatched_edge`；
- 当前快照：`stale`；正式卡 `0b2ddf875083aa8c820e1b42f33e190473e0c2a966924d64751ffaca3ab71ef9`；唯一图片 2 个；物理路径 2 个。

### GS-199 强化例题15.12：根号整体换元与分支

- 题目：在 \(x\ge-2\) 上求含 \(\sqrt{y+x^2}\) 的初值问题特解。
- 所问：特解与端点
- 知识点：根式整体换元；初值问题；非Lipschitz端点与分支
- 第一动作：令 \(u=y+x^2\)，把根号整体化为 \(u'=\sqrt u\)
- 答案：\(y=(x/2+1)^2-x^2\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“令 \(u=y+x^2\)，把根号整体化为 \(u'=\sqrt u\)”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 在 \(u>0\) 内分离变量。
  - 用初值和主值平方根确定分支。
  - 对 \(x=-2,u=0\) 端点直接回代验证。
- 质量发现：
  - `non_lipschitz_endpoint_direct_verification_completed`：分离只覆盖 u 大于 0 的内部区间；x=-2 端点通过最终函数直接回代确认。；建议：
- 关系裁决：
  - GS-192：`retain_medium_navigation_without_yaml_strong_edge`；
- 当前快照：`stale`；正式卡 `8152566cdc6f8251e9591b82037a37df2f2bf1b51d991cb27151cca76361ade0`；唯一图片 2 个；物理路径 2 个。

### GS-200 2024年真题18题

- 题目：解欧拉方程初值问题，并把所得函数代入根式定积分。
- 所问：函数与定积分
- 知识点：欧拉方程；变量角色；常系数方程与定积分
- 第一动作：令 \(t=\ln x\)，另记 \(Y(t)=y(e^t)\)
- 答案：\(y(x)=2x^3\)，积分值为 \(22\sqrt3/5\)。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“令 \(t=\ln x\)，另记 \(Y(t)=y(e^t)\)”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 把欧拉方程化为 \(Y''-9Y=0\)。
  - 用变换后的初值求 \(Y\) 并回写 \(y(x)\)。
  - 在 \(x>0\) 分支完成定积分。
- 质量发现：
  - `question_only_euler_variable_roles_verified`：仅有题图；本轮独立区分原变量 x、新变量 t 与变换后函数 Y(t)，并核对正半轴解。；建议：
- 关系裁决：
  - GS-520：`verify_existing_strong_edge`；
- 当前快照：`stale`；正式卡 `227d63db9ea2c1019202fabfe77559e9897193b548da166ce0269ba331bfe752`；唯一图片 1 个；物理路径 1 个。

### GS-201 2018年第16题：变上限积分方程转微分方程

- 题目：把卷积型变上限积分方程转为微分方程，并由平均值条件确定参数。
- 所问：函数与参数
- 知识点：Volterra积分方程；Leibniz求导；一阶线性微分方程
- 第一动作：先换元把 \(f(x-t)\) 改写成统一积分变量，再整体求导
- 答案：\(f(x)=2a(1-e^{-x})\)，\(a=e/2\)。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先换元把 \(f(x-t)\) 改写成统一积分变量，再整体求导”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 换元消除复合输入的变量混淆。
  - 两次求导得到一阶线性方程并从原式恢复初值。
  - 用平均值条件确定参数。
- 质量发现：
  - `volterra_leibniz_regularization_chain_completed`：先换元统一输入，再两次求导转方程并恢复初值的链条已补全。；建议：
- 关系裁决：
  - GS-289：`add_specific_strong_edge_bidirectionally`；
  - GS-527：`add_specific_strong_edge_bidirectionally`；
  - GS-202：`remove_broad_or_method_mismatched_edge`；
  - GS-203：`remove_broad_or_method_mismatched_edge`；
  - GS-205：`remove_broad_or_method_mismatched_edge`；
- 当前快照：`stale`；正式卡 `63c8d891e65b5e71ac7598a1b1f19d4974955a6a47c053205a8a620a13e277a8`；唯一图片 2 个；物理路径 2 个。

### GS-202 强化例题15.3-2：函数方程求导建立微分方程

- 题目：由 \(f(xy)=yf(x)+xf(y)\) 与 \(f'(1)=e\) 求函数及 \(f(xy)\) 的极小值。
- 所问：函数、极小值与等号条件
- 知识点：乘法型函数方程；导数定义；基点可导性迁移；极值
- 第一动作：先取特殊值得 \(f(1)=0\)，再用差商把任意点可导性化归到基点 1
- 答案：\(f(x)=ex\ln x\)；当 \(xy=e^{-1}\) 时极小值为 \(-1\)。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先取特殊值得 \(f(1)=0\)，再用差商把任意点可导性化归到基点 1”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 用函数方程严格改写任意点差商。
  - 由 \(f'(1)\) 证明所有正数点可导并建立微分方程。
  - 解出函数后令 \(u=xy\) 求极值。
- 质量发现：
  - `basepoint_differentiability_proof_repaired`：题设只给 f'(1)，已用差商先证明任意正数点可导，替代不严谨的预设全域可导后参数求导。；建议：
- 关系裁决：
  - GS-471：`add_specific_strong_edge_bidirectionally`；
  - GS-203：`remove_broad_or_method_mismatched_edge`；
- 当前快照：`current`；正式卡 `91469588afc613dcaca0ca77735cba68cd5e023842814733bfa998979b5424d0`；唯一图片 2 个；物理路径 2 个。

### GS-203 强化例题15.14（2023年真题17题）：切线截距建模微分方程

- 题目：把切线在纵轴的截距条件翻译为微分方程，再求相关面积最值。
- 所问：曲线、最值点与最小面积
- 知识点：切线截距；几何建模；一阶线性微分方程；面积最值
- 第一动作：写切点处切线并令一般点横坐标为 0 求纵轴截距
- 答案：\(y=x(2-\ln x),x>e\)；最小面积点 \((e^{3/2},e^{3/2}/2)\)，最小面积 \(e^3\)。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“写切点处切线并令一般点横坐标为 0 求纵轴截距”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 区分切点与切线上一般点。
  - 把截距条件化为一阶线性方程。
  - 保留原域 \(x>e\) 后求面积最值。
- 质量发现：
  - `original_positive_domain_restored`：曲线答案已恢复题设原域 x 大于 e，并在该域上完成面积最值。；建议：
- 关系裁决：
  - GS-205：`verify_existing_strong_edge`；
  - GS-207：`verify_existing_strong_edge`；
- 当前快照：`current`；正式卡 `8bc358f836e88f195695bf83a2373c3318689c10f379243f2b443ac34c697aa9`；唯一图片 2 个；物理路径 2 个。

### GS-204 强化例题15.15：曲率条件建立二阶可降阶方程

- 题目：由曲率和切线倾角条件建立二阶可降阶方程并求凹向上曲线。
- 所问：带几何定义域的曲线
- 知识点：曲率公式；切线倾角；二阶不显含自变量降阶
- 第一动作：把曲率与 \(\cos\alpha\) 全部写成 \(y',y''\)
- 答案：\(y=\frac14(x-1)^2+1,\ x\ge1\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“把曲率与 \(\cos\alpha\) 全部写成 \(y',y''\)”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由凹向上知 \(y''>0\)，去掉曲率公式绝对值。
  - 建立与 GS-193 相同的二阶方程。
  - 降阶并用几何条件确定 \(x\ge1\) 分支。
- 质量发现：
  - `source_solution_angle_variable_typo_documented`：解析图中的 sec x、cos x 应为 sec alpha、cos alpha；并已用凹向上即 y''大于0解释去绝对值。；建议：
- 关系裁决：
  - GS-205：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；
- 当前快照：`current`；正式卡 `888938eaa4499afcf5ff54e3bff4b3770586216330b6befd2a2b3fae82809b9a`；唯一图片 2 个；物理路径 2 个。

### GS-205 2020年第21题：面积比条件建立微分方程

- 题目：由切线三角形面积与曲线下面积之比建立方程，求曲线族。
- 所问：曲线族与条件边界
- 知识点：切线横截距；面积积分方程；二阶降阶；端点条件
- 第一动作：先求切线横截距并把两块面积写成积分关系
- 答案：按官方题意的内点解释，\(f(x)=Cx^3,C>0\)。
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“先求切线横截距并把两块面积写成积分关系”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 在 \(x>0\) 上建立面积关系。
  - 由关系补足正则性后求导得到二阶方程。
  - 降阶并由 \(f(0)=0\) 收口；记录题干端点歧义。
- 质量发现：
  - `source_stem_endpoint_derivative_ambiguity`：若 f'(x)>0 包含端点 0，则与官方答案 f'(0)=0 冲突；本批按 x>0 内点条件记录有条件结论并保留来源歧义。；建议：
- 关系裁决：
  - GS-540：`add_specific_strong_edge_bidirectionally`；
  - GS-206：`remove_broad_or_method_mismatched_edge`；
  - GS-207：`remove_broad_or_method_mismatched_edge`；
- 当前快照：`current`；正式卡 `dc1c27a24e5b1477c2cdf3a94eeb4d7c39962b56cc843bff2c5fa6c9eaa3dbe8`；唯一图片 2 个；物理路径 2 个。

### GS-206 强化例题15.16：阻力运动中的变量转换

- 题目：线性阻力运动中，求达到渐近总位移一半时的速度。
- 所问：选择项与速度
- 知识点：牛顿第二定律；链式换元；渐近总位移
- 第一动作：因目标按位移给出，把 \(v\) 看成 \(x\) 的函数并写 \(dv/dt=v\,dv/dx\)
- 答案：B：\(v(0)/2\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“因目标按位移给出，把 \(v\) 看成 \(x\) 的函数并写 \(dv/dt=v\,dv/dx\)”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 在 \(v>0\) 的滑行阶段约去 \(v\)。
  - 得到速度关于位移的线性关系。
  - 用 \(t\to\infty\) 的位移极限求半程速度。
- 质量发现：
  - `asymptotic_total_displacement_and_option_label_repaired`：总位移是 t 趋于正无穷时的极限，约去 v 仅限 v>0；题图第四项字母重复也已注明。；建议：
- 关系裁决：
  - GS-207：`remove_broad_or_method_mismatched_edge`；
  - ：`preserve_zero_degree_card`；
- 当前快照：`current`；正式卡 `1538075cd58ca32269b7b0a0fb6a7142e11e3e2712b3c03ccddbd8118ce20fed`；唯一图片 2 个；物理路径 2 个。

### GS-207 强化例题15.17：追踪曲线建立微分方程

- 题目：把追踪方向和定长条件转成微分方程，求动点轨迹。
- 所问：轨迹与定义域
- 知识点：追踪曲线；切线方向；平方根分支；定义域
- 第一动作：把指向关系翻译成轨迹切线斜率，再联立距离约束
- 答案：\(y=\ln\frac{1+\sqrt{1-x^2}}x-\sqrt{1-x^2},\ 0<x\le1\)
- 个人错因边界：pending_user_confirmation；pending_user_confirmation：旧卡未记录用户作答过程；当前只确认复做第一动作是“把指向关系翻译成轨迹切线斜率，再联立距离约束”
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 令目标点与追踪点坐标角色分离。
  - 由运动方向选择正根并得到负斜率分支。
  - 积分后用初始点确定常数与 \(0<x\le1\)。
- 质量发现：
  - `trajectory_sign_branch_and_domain_verified`：已由运动方向、位置关系与初值共同确定平方根正支、负斜率及 0<x<=1。；建议：
- 当前快照：`current`；正式卡 `ee709811a93ce7e28ba857e054ba9321f548d4abd663b607e4d6d944d935dcd0`；唯一图片 2 个；物理路径 2 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
