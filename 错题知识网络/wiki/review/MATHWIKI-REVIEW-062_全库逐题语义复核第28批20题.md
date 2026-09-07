---
wiki_id: MATHWIKI-REVIEW-062
type: target_level_semantic_review_batch
title: 全库逐题语义复核第28批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-062_全库逐题语义复核第28批20题.json
status: active
last_updated: 2026-07-24
---

# 全库逐题语义复核第28批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 4 张；覆盖 21 个物理图片路径与 21 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 5 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `pending_MATH-TARGET-SEMANTIC-CLOSEOUT-20260724-B28`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-416](http://127.0.0.1:8765/open/GS-416) | 定积分物理应用加速度积分 | 定积分、定积分应用、定积分物理应用 | \boxed{0} | pending_user_confirmation：现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。 | yaml_and_question_summary_repaired |
| [GS-417](http://127.0.0.1:8765/open/GS-417) | 平均速度参数方程 | 定积分、定积分性质、定积分应用、定积分物理应用 | \boxed{k=\frac{3\pi}{2}} | pending_user_confirmation：现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。 | question_summary_repaired |
| [GS-418](http://127.0.0.1:8765/open/GS-418) | 定积分物理应用：抽水做功 | 定积分、变力做功积分、抽水做功微元 | \boxed{2^{1/4}} | pending_user_confirmation：现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。 | relation_scope_repaired |
| [GS-419](http://127.0.0.1:8765/open/GS-419) | 定积分物理应用：静水压力 | 定积分、静水压力微元 | \boxed{2} | pending_user_confirmation：现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。 | relation_scope_repaired |
| [GS-420](http://127.0.0.1:8765/open/GS-420) | 定积分物理应用：静水压力 | 定积分、静水压力微元 | \boxed{\frac13\rho g a^3} | pending_user_confirmation：现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。 | relation_scope_repaired |
| [GS-422](http://127.0.0.1:8765/open/GS-422) | 定积分物理应用：克服引力做功 | 定积分应用、定积分物理应用 | \boxed{\int_0^l \frac{Gx}{(x^2+1)^{3/2}}\,dx} | pending_user_confirmation：现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。 | work_sign_semantics_repaired |
| [GS-423](http://127.0.0.1:8765/open/GS-423) | 定积分物理应用：流量微元 | 定积分、流量环形微元 | \boxed{5\pi} | pending_user_confirmation：现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。 | relation_scope_repaired |
| [GS-424](http://127.0.0.1:8765/open/GS-424) | 约束二次型最值 | 多元函数微分学、多元函数极值、特征值与特征向量、二次型 | \boxed{u_{\max}=1,\qquad u_{\min}=\dfrac1{\sqrt6}}. | pending_user_confirmation：现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。 | duplicate_identity_hold、question_summary_repaired |
| [GS-426](http://127.0.0.1:8765/open/GS-426) | 导数定义型问题（OCR待核对） | 导数定义、一元函数微分学应用 | 旧批量导入未记录标准答案，待题图或 OCR 核对后补齐。 | not_assessable_missing_question_surface：正确高数题面尚未恢复，当前不能评估用户个人错因；历史错连视觉证据实际是实矩阵转置与对称矩阵题。 | missing_question_surface、gap_detail_boundary_repaired |
| [GS-427](http://127.0.0.1:8765/open/GS-427) | 导数定义型问题（OCR待核对） | 导数定义、一元函数微分学应用 | 旧批量导入未记录标准答案，待题图或 OCR 核对后补齐。 | not_assessable_missing_question_surface：正确高数题面尚未恢复，当前不能评估用户个人错因；历史错连视觉证据实际是三阶矩阵高次幂题。 | missing_question_surface、gap_detail_boundary_repaired |
| [GS-428](http://127.0.0.1:8765/open/GS-428) | 导数定义型问题（OCR待核对） | 导数定义、一元函数微分学应用 | 旧批量导入未记录标准答案，待题图或 OCR 核对后补齐。 | not_assessable_missing_question_surface：正确高数题面尚未恢复，当前不能评估用户个人错因；历史错连视觉证据实际是上三角幂零截断题。 | missing_question_surface、gap_detail_boundary_repaired |
| [GS-429](http://127.0.0.1:8765/open/GS-429) | 导数定义型问题（OCR待核对） | 导数定义、一元函数微分学应用 | 旧批量导入未记录标准答案，待题图或 OCR 核对后补齐。 | not_assessable_missing_question_surface：正确高数题面尚未恢复，当前不能评估用户个人错因；历史错连视觉证据实际是二维旋转矩阵负整数幂题。 | missing_question_surface、gap_detail_boundary_repaired |
| [GS-430](http://127.0.0.1:8765/open/GS-430) | 比值型数列极限证明 | 数列极限、极限与连续、绝对值分类 | $\lim\limits_{n\to\infty} a_n=0$ | legacy_unclassified：仅有历史入库日期，无法确认原始作答动作；收缩不等式只作为复做入口。 | evidence_boundary_repaired |
| [GS-431](http://127.0.0.1:8765/open/GS-431) | 三项递推数列极限 | 数列极限、极限与连续 | 第（1）问 $\lim\limits_{n\to\infty}x_n=3$；第（2）问 $\lim\limits_{n\to\infty}x_n=\frac53$。 | user_confirmed：没有识别出三项递推数列可令 $y_n=x_{n+1}-x_n$ 构造相邻差数列降阶，导致没有把递推式转化为等比数列，也没有用差值累加反推出 $x_n$。 | no_strong_edge_confirmed |
| [GS-432](http://127.0.0.1:8765/open/GS-432) | 零点唯一性与根的位置估计 | 极限与连续、数列极限、一元函数微分学应用 | 方程 $f_n(x)=\frac12$ 在 $\left(0,\frac{\pi}{2}\right)$ 内有且只有一个根 $x_n$；且 $\arccos\frac1n<x_n<\frac{\pi}{2}$，$\lim\limits_{n\to\infty}x_n=\frac{\pi}{2}$。 | user_confirmed：第一问只想到构造函数和零点定理，但没有接上“端点异号证存在、导数单调证唯一”的完整套路；第二问没有把根的位置比较 $\arccos\frac1n<x_n$ 转化为单调递减函数的函数值比较。 | solution_logic_gap_repaired |
| [GS-433](http://127.0.0.1:8765/open/GS-433) | 递推数列极限 | 数列极限、极限与连续、一元函数微分学应用、零点定理 | $\displaystyle \lim_{n\to\infty}x_n=\xi$，其中 $\xi$ 是方程 $x=1+2\ln x$ 在 $(e,+\infty)$ 内的唯一实根。 | user_confirmed：复发点集中在第二问：第一问唯一根已能识别，但递推数列极限不能直接设极限；必须先用数学归纳法证明区间不变性 \(e<x_n<\xi\)，再由 \(g(x)-x=1+2\ln x-x>0\)（在 \(e<x<\xi\) 内）推出 \(x_{n+1}>x_n\)，完成单调有界后才能取极限。 | repeat_evidence_and_relation_repaired |
| [GS-434](http://127.0.0.1:8765/open/GS-434) | 连续函数存在性证明 | 极限与连续、零点定理、一元函数微分学应用 | 存在 $\xi\in(0,\frac12]$，使 $f(\xi)=f(\xi+\frac12)$；对 $n\ge2$，存在 $\xi\in(0,1-\frac1n]$，使 $f(\xi)=f(\xi+\frac1n)$。 | user_confirmed：本次复发点主要在第二问：第一问的 \(1/2\) 平移差函数已能处理，但没有把 \(\frac1n\) 平移识别成“把 \([0,1]\) 分成 \(n\) 段 + 相邻函数值作差 + 望远镜求和”。应构造 \(\varphi(x)=f(x+\frac1n)-f(x)\)，考察 \(\varphi(0),\varphi(\frac1n),\ldots,\varphi(\frac{n-1}{n})\)，累加得到 \(f(1)-f(0)=0\)，再推出有零点。 | answer_domain_and_relation_repaired |
| [GS-435](http://127.0.0.1:8765/open/GS-435) | 方程根构造数列极限 | 数列极限、极限与连续、一元函数微分学应用、幂指极限、等价无穷小 | 对每个 $n$，方程 $x^n-\cos x=0$ 在 $(0,1)$ 内有唯一根 $x_n$；$x_n$ 单调递增且 $x_n\to1$；$\displaystyle \lim_{n\to\infty}(1-x_n)^{\frac1n\ln\cos x_n}=1$。 | user_confirmed：没有把“每个 $x_n$ 是不同函数 $f_n(x)$ 的零点”转化为“比较 $f_n(x_{n+1})$ 与 $f_n(x_n)$”；第一问已知 $f_n$ 在 $(0,1)$ 严格递增，但第二问没有把 $x_{n+1}$ 代回 $f_n(x)=x^n-\cos x$，利用 $f_n(x_{n+1})=x_{n+1}^n(1-x_{n+1})>0=f_n(x_n)$ 推出 $x_{n+1}>x_n$。 | incomplete_answer_repaired |
| [GS-436](http://127.0.0.1:8765/open/GS-436) | 变上限积分型极限 | 极限与连续、变上限积分、等价无穷小、洛必达法则、幂指极限 | $\displaystyle \frac{2}{27}$。 | user_confirmed：最后等价无穷小化简时丢了常数因子；底数接近常数 $3$ 时，没有先提出主量 $3$，把 $(3+2\tan x)^x$ 化成 $3^x(1+\frac{2\tan x}{3})^x$，导致把关键小量 $\frac{2\tan x}{3}$ 误当成 $2\tan x$。 | error_taxonomy_repaired |
| [GS-438](http://127.0.0.1:8765/open/GS-438) | 指数型极限 | 极限与连续、无穷远极限、幂指极限、拉格朗日中值定理、泰勒展开、等价无穷小 | $\displaystyle \frac18 e^{e+1}$。 | user_confirmed：没有把 $e^{(1+t)^{1/t}}$ 与 $e^{e\ln(1+t)/t}$ 看成同一函数 $e^u$ 在两个相近点处的函数值之差，导致没有用拉格朗日中值定理转成 $e^{\xi}(u_1-u_2)$；后续换元 $u=\frac{\ln(1+t)}t$ 后，没有继续用泰勒展开建立 $u-1\sim-\frac t2$，即 $t^2\sim4(u-1)^2$。 | detail_truncation_and_relation_repaired |

## 逐题复核

### GS-416 强化例题12.2

- 题目：设 \(s(t)\) 为物体的位置函数，\(v(t)=s'(t)\) 为速度，\(a(t)=v'(t)\) 为加速度。已知 \(s(1)-s(0)=2\) 且 \(v(1)=2\)，求 $$ \int_0^1 t a(t)\,dt. $$
- 所问：定积分物理应用加速度积分
- 知识点：定积分；定积分应用；定积分物理应用
- 第一动作：先写 \(s'(t)=v(t),\ v'(t)=a(t)\)，把原式改成 \(\int_0^1 t v'(t)\,dt\)。
- 答案：\boxed{0}
- 个人错因边界：pending_user_confirmation；现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 物理语言转定积分
  - 分部积分
  - 速度积分求路程
- 质量发现：
  - `yaml_and_question_summary_repaired`：YAML 撇号断裂与截断题目摘要已修复。；建议：
- 关系裁决：
  - ：`remove`；
  - ：`remove`；
- 当前快照：`stale`；正式卡 `0b1bc383219859d1dd49e13dc77ba297a28b03b3f97f4b8dcf8c7e5a3b444f50`；唯一图片 1 个；物理路径 1 个。

### GS-417 2024年真题15题

- 题目：物体的速度为 $$ v(t)=t+k\sin(\pi t). $$ 已知物体在时间区间 \([0,3]\) 上的平均速度为 \(5/2\)，求参数 \(k\)。
- 所问：平均速度参数方程
- 知识点：定积分；定积分性质；定积分应用；定积分物理应用
- 第一动作：先写 \(\frac13\int_0^3 v(t)\,dt=\frac52\)。
- 答案：\boxed{k=\frac{3\pi}{2}}
- 个人错因边界：pending_user_confirmation；现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 条件转化
  - 平均速度公式
  - 物理语言转定积分
  - 定积分计算
- 质量发现：
  - `question_summary_repaired`：截断 OCR 题目摘要已改为完整独立题面。；建议：
- 关系裁决：
  - ：`keep`；
  - ：`keep`；
  - ：`remove`；
- 当前快照：`stale`；正式卡 `1e63170fc300932db33eddba38a9c34e50e4a1bd6ed776b2940ab34c63e3ea74`；唯一图片 1 个；物理路径 1 个。

### GS-418 强化例题12.3

- 题目：半球形水池半径未知，已知将满池水抽出的最小做功，反求半径。
- 所问：定积分物理应用：抽水做功
- 知识点：定积分；变力做功积分；抽水做功微元
- 第一动作：先按深度 h 取水平薄片，同时写面积和提升距离
- 答案：\boxed{2^{1/4}}
- 个人错因边界：pending_user_confirmation；现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 物理语言转定积分
  - 微元法建模
  - 抽水做功微元
  - 水平切片
- 质量发现：
  - `relation_scope_repaired`：抽水做功仅保留与同型题 GS-415 的强边。；建议：
- 关系裁决：
  - ：`keep`；
  - ：`remove`；
  - ：`remove`；
  - ：`remove`；
- 当前快照：`stale`；正式卡 `a3aa4751ce27b694de925d5dc15882b1102e8e8bb26734622d390e45853cb88c`；唯一图片 2 个；物理路径 2 个。

### GS-419 强化例题12.4

- 题目：闸门由上部矩形和下部抛物线曲边区域组成，已知上下两部分所受静水压力比，求矩形高度参数。
- 所问：定积分物理应用：静水压力
- 知识点：定积分；静水压力微元
- 第一动作：先画水平条，并分段写出矩形部分和抛物线部分的条宽
- 答案：\boxed{2}
- 个人错因边界：pending_user_confirmation；现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 物理语言转定积分
  - 微元法建模
  - 静水压力微元
  - 水平切片
- 质量发现：
  - `relation_scope_repaired`：静水压力题仅保留同型水平条模型 GS-420。；建议：
- 关系裁决：
  - ：`keep`；
  - ：`remove`；
- 当前快照：`stale`；正式卡 `79c8419cba8f112812166a07b0b24480e23449c3ce70e31d5da8074bfac9ac5b`；唯一图片 2 个；物理路径 2 个。

### GS-420 2020年第12题

- 题目：等腰直角三角形平板竖直放入水中，斜边与水面重合，求平板一侧所受静水压力。
- 所问：定积分物理应用：静水压力
- 知识点：定积分；静水压力微元
- 第一动作：先从水面向下设深度 h，并写出该深度处三角形的水平宽度
- 答案：\boxed{\frac13\rho g a^3}
- 个人错因边界：pending_user_confirmation；现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 物理语言转定积分
  - 微元法建模
  - 静水压力微元
  - 水平切片
- 质量发现：
  - `relation_scope_repaired`：静水压力题仅保留同型水平条模型 GS-419。；建议：
- 关系裁决：
  - ：`keep`；
  - ：`remove`；
- 当前快照：`stale`；正式卡 `74a2f7daa11460da9a6c9b244cc8fc66fa33930aa9d5d98444903bac92a626ea`；唯一图片 2 个；物理路径 2 个。

### GS-422 2025年真题选择题第六题

- 题目：2025 年真题选择题中的克服引力做功模型，关键是把引力在位移方向上的分量写出来，并检查所求功的符号。
- 所问：定积分物理应用：克服引力做功
- 知识点：定积分应用；定积分物理应用
- 第一动作：先写距离 r，并把引力大小乘以 x/r 得到位移方向分量
- 答案：\boxed{\int_0^l \frac{Gx}{(x^2+1)^{3/2}}\,dx}
- 个人错因边界：pending_user_confirmation；现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 物理语言转定积分
  - 微元法建模
  - 引力做功积分
  - 力的投影
- 质量发现：
  - `work_sign_semantics_repaired`：已明确区分引力做功与克服引力所做正功。；建议：
- 当前快照：`stale`；正式卡 `77a0c4ff8cfdff7f04ee5b2d9d71691afaa867ae44dcd300627e7abecf7d84de`；唯一图片 2 个；物理路径 2 个。

### GS-423 强化例题12.6

- 题目：圆柱管道中流速随到中心距离 \(r\) 改变，求单位时间流过横截面的体积。
- 所问：定积分物理应用：流量微元
- 知识点：定积分；流量环形微元
- 第一动作：先写环形面积微元 dA=2πr dr
- 答案：\boxed{5\pi}
- 个人错因边界：pending_user_confirmation；现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 物理语言转定积分
  - 微元法建模
  - 流量环形微元
  - 极坐标面积微元
- 质量发现：
  - `relation_scope_repaired`：已移除只共享宽泛微元标签的关系。；建议：
- 关系裁决：
  - ：`remove`；
- 当前快照：`stale`；正式卡 `e53f944a4449c727566e013024b1bdea7a6c25aca8c4b32753c1d4ab93f545b7`；唯一图片 2 个；物理路径 2 个。

### GS-424 强化例题13.30-2

- 题目：在约束 $$ 5x^2+4xy+2y^2=1 $$ 下，求 $$ u=\sqrt{x^2+y^2} $$ 的最大值与最小值。
- 所问：约束二次型最值
- 知识点：多元函数微分学；多元函数极值；特征值与特征向量；二次型
- 第一动作：先令 \(S=x^2+y^2\)，把问题改写为在二次型约束下求 \(S\) 的最值。
- 答案：\boxed{u_{\max}=1,\qquad u_{\min}=\dfrac1{\sqrt6}}.
- 个人错因边界：pending_user_confirmation；现有题面与解析只支持复做入口；缺少用户原始作答，候选个人断点仍待确认。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_question_surface_with_duplicate_identity_hold
- 解析主线：
  - 拉格朗日乘数法
  - 条件极值必要条件
  - 二次型矩阵化
  - Rayleigh 商
  - 特征值最值
  - 等价变形
  - 特征分解
- 质量发现：
  - `duplicate_identity_hold`：GS-424 与 GS-393 的题图 SHA-256 相同；稳定 ID 暂不合并，普通关系保持为空。；建议：
  - `question_summary_repaired`：截断解析已替换为完整独立题面，库内误挂不再表述为用户错因。；建议：
- 当前快照：`stale`；正式卡 `29b8f846e72a8cdd700d782d1be762b6c725338b1b16f0be64dcfb9ce1f15c15`；唯一图片 1 个；物理路径 1 个。

### GS-426 强化例题3.1（171615）

- 题目：正确高数题面与标准答案均缺失。历史同名视觉证据实际是实矩阵转置与对称矩阵题，已作为错连证据隔离，不能充当本卡题面。
- 所问：导数定义型问题（OCR待核对）
- 知识点：导数定义；一元函数微分学应用
- 第一动作：—
- 答案：旧批量导入未记录标准答案，待题图或 OCR 核对后补齐。
- 个人错因边界：not_assessable_missing_question_surface；正确高数题面尚未恢复，当前不能评估用户个人错因；历史错连视觉证据实际是实矩阵转置与对称矩阵题。
- 一致性：题图—解析 question_and_answer_unavailable_gap_explicit；正式卡—图片 blocked_by_documented_evidence_gap
- 解析主线：
  - 导数定义差商入口
- 质量发现：
  - `missing_question_surface`：正确高数题面和标准答案仍缺失；旧同名视觉已核验为线性代数错配。；建议：
  - `gap_detail_boundary_repaired`：缺图详情已同步为恢复题面前禁止复做、答案判断和普通关系聚合。；建议：
- 关系裁决：
  - ：`remove`；
  - ：`remove`；
  - ：`remove`；
- 当前快照：`current`；正式卡 `f057159b2c928d5b3bd319215e31d4948cc57cdea43ddc8f4896d3d83d23ca15`；唯一图片 0 个；物理路径 0 个。

### GS-427 强化例题3.2（84104）

- 题目：正确高数题面与标准答案均缺失。历史同名视觉证据实际是三阶矩阵高次幂题，已作为错连证据隔离，不能充当本卡题面。
- 所问：导数定义型问题（OCR待核对）
- 知识点：导数定义；一元函数微分学应用
- 第一动作：—
- 答案：旧批量导入未记录标准答案，待题图或 OCR 核对后补齐。
- 个人错因边界：not_assessable_missing_question_surface；正确高数题面尚未恢复，当前不能评估用户个人错因；历史错连视觉证据实际是三阶矩阵高次幂题。
- 一致性：题图—解析 question_and_answer_unavailable_gap_explicit；正式卡—图片 blocked_by_documented_evidence_gap
- 解析主线：
  - 导数定义差商入口
- 质量发现：
  - `missing_question_surface`：正确高数题面和标准答案仍缺失；旧同名视觉已核验为线性代数错配。；建议：
  - `gap_detail_boundary_repaired`：缺图详情已同步为恢复题面前禁止复做、答案判断和普通关系聚合。；建议：
- 关系裁决：
  - ：`remove`；
  - ：`remove`；
  - ：`remove`；
- 当前快照：`current`；正式卡 `74e42851fc99fbebbd5792bc858c939dd95597cf227e929b8bd386cdef3be077`；唯一图片 0 个；物理路径 0 个。

### GS-428 强化例题3.3（171621）

- 题目：正确高数题面与标准答案均缺失。历史同名视觉证据实际是上三角幂零截断题，已作为错连证据隔离，不能充当本卡题面。
- 所问：导数定义型问题（OCR待核对）
- 知识点：导数定义；一元函数微分学应用
- 第一动作：—
- 答案：旧批量导入未记录标准答案，待题图或 OCR 核对后补齐。
- 个人错因边界：not_assessable_missing_question_surface；正确高数题面尚未恢复，当前不能评估用户个人错因；历史错连视觉证据实际是上三角幂零截断题。
- 一致性：题图—解析 question_and_answer_unavailable_gap_explicit；正式卡—图片 blocked_by_documented_evidence_gap
- 解析主线：
  - 导数定义差商入口
- 质量发现：
  - `missing_question_surface`：正确高数题面和标准答案仍缺失；旧同名视觉已核验为线性代数错配。；建议：
  - `gap_detail_boundary_repaired`：缺图详情已同步为恢复题面前禁止复做、答案判断和普通关系聚合。；建议：
- 关系裁决：
  - ：`remove`；
  - ：`remove`；
  - ：`remove`；
- 当前快照：`current`；正式卡 `5ee6f56b203c24feba33a0e795030bf1fd2c3a6f11c9e083b6b57272c1d8846c`；唯一图片 0 个；物理路径 0 个。

### GS-429 强化例题3.4（152770）

- 题目：正确高数题面与标准答案均缺失。历史同名视觉证据实际是二维旋转矩阵负整数幂题，已作为错连证据隔离，不能充当本卡题面。
- 所问：导数定义型问题（OCR待核对）
- 知识点：导数定义；一元函数微分学应用
- 第一动作：—
- 答案：旧批量导入未记录标准答案，待题图或 OCR 核对后补齐。
- 个人错因边界：not_assessable_missing_question_surface；正确高数题面尚未恢复，当前不能评估用户个人错因；历史错连视觉证据实际是二维旋转矩阵负整数幂题。
- 一致性：题图—解析 question_and_answer_unavailable_gap_explicit；正式卡—图片 blocked_by_documented_evidence_gap
- 解析主线：
  - 导数定义差商入口
- 质量发现：
  - `missing_question_surface`：正确高数题面和标准答案仍缺失；旧同名视觉已核验为线性代数错配。；建议：
  - `gap_detail_boundary_repaired`：缺图详情已同步为恢复题面前禁止复做、答案判断和普通关系聚合。；建议：
- 关系裁决：
  - ：`remove`；
  - ：`remove`；
  - ：`remove`；
- 当前快照：`current`；正式卡 `70a140186516d58b8f85cc40cf26ae2d41cc5d32be49bb11ede2ed81ffdf2599`；唯一图片 0 个；物理路径 0 个。

### GS-430 57717 比值型数列极限

- 题目：设数列 $\{a_n\}$ 满足 $\lim\limits_{n\to\infty}\dfrac{a_{n+1}}{a_n}=q$，且 $|q|<1$，证明 $\lim\limits_{n\to\infty}a_n=0$。
- 所问：比值型数列极限证明
- 知识点：数列极限；极限与连续；绝对值分类
- 第一动作：先取 r 满足 |q|<r<1，并写出充分大的 n 下 |a_{n+1}|\le r|a_n|
- 答案：$\lim\limits_{n\to\infty} a_n=0$
- 个人错因边界：legacy_unclassified；仅有历史入库日期，无法确认原始作答动作；收缩不等式只作为复做入口。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 条件转化
  - 单调有界
  - 单调有界准则
  - 夹逼准则
  - 反证法
- 质量发现：
  - `evidence_boundary_repaired`：收缩证明保留为复做入口，未反写成用户个人错因。；建议：
- 关系裁决：
  - ：`keep`；
  - ：`remove`；
- 当前快照：`stale`；正式卡 `2df5c5a7645dd726355212494bed702b56910dd4d713edd3ae50ea792d7de9d5`；唯一图片 1 个；物理路径 1 个。

### GS-431 58022 2026.5.8

- 题目：三项递推数列极限：$x_1=1,\ x_2=2$。第（1）问 $x_{n+2}=\frac12(3x_{n+1}-x_n)$；第（2）问 $x_{n+2}=\frac12(x_n+x_{n+1})$，分别求 $\lim x_n$。
- 所问：三项递推数列极限
- 知识点：数列极限；极限与连续
- 第一动作：先令 y_n=x_{n+1}-x_n，并把原递推式改写成 y_{n+1}=q y_n
- 答案：第（1）问 $\lim\limits_{n\to\infty}x_n=3$；第（2）问 $\lim\limits_{n\to\infty}x_n=\frac53$。
- 个人错因边界：user_confirmed；没有识别出三项递推数列可令 $y_n=x_{n+1}-x_n$ 构造相邻差数列降阶，导致没有把递推式转化为等比数列，也没有用差值累加反推出 $x_n$。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先判型
  - 差分构造
  - 构造辅助函数
  - 条件转化
  - 等比数列求和
  - 望远镜求和
- 质量发现：
  - `no_strong_edge_confirmed`：题面与解法已核验，当前没有足够强的逐题关系。；建议：
- 当前快照：`stale`；正式卡 `f3a8e0c58b6c62ebb6c02411a5e73291eb1bd8f1460e5050ac3ab43a90044677`；唯一图片 1 个；物理路径 1 个。

### GS-432 58053 2026.5.8

- 题目：设 $f_n(x)=1-(1-\cos x)^n$。证明方程 $f_n(x)=\frac12$ 在 $\left(0,\frac{\pi}{2}\right)$ 内有且只有一个实根 $x_n$；再证明 $\arccos\frac1n<x_n<\frac{\pi}{2}$，并求 $\lim x_n$。
- 所问：零点唯一性与根的位置估计
- 知识点：极限与连续；数列极限；一元函数微分学应用
- 第一动作：先把方程移项成 F_n(x)=0，计算 F_n'(x) 判单调并检查端点符号
- 答案：方程 $f_n(x)=\frac12$ 在 $\left(0,\frac{\pi}{2}\right)$ 内有且只有一个根 $x_n$；且 $\arccos\frac1n<x_n<\frac{\pi}{2}$，$\lim\limits_{n\to\infty}x_n=\frac{\pi}{2}$。
- 个人错因边界：user_confirmed；第一问只想到构造函数和零点定理，但没有接上“端点异号证存在、导数单调证唯一”的完整套路；第二问没有把根的位置比较 $\arccos\frac1n<x_n$ 转化为单调递减函数的函数值比较。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 构造辅助函数
  - 零点定理
  - 导数判单调
  - 函数值比较
  - 夹逼准则
  - 条件转化
- 质量发现：
  - `solution_logic_gap_repaired`：已用对数不等式补齐逐项小于 1/e 的证明。；建议：
- 关系裁决：
  - ：`add`；
  - ：`remove`；
- 当前快照：`stale`；正式卡 `b976c3f64f6c31ed53881d96fddaa898e9cddefac780851286ad0bb4e0f012ee`；唯一图片 1 个；物理路径 1 个。

### GS-433 58084 2026.5.22

- 题目：证明方程 $x=1+2\ln x$ 在 $(e,+\infty)$ 内有唯一实根 $\xi$；若 $x_0\in(e,\xi)$，递推 $x_n=1+2\ln x_{n-1}$，证明 $\lim_{n\to\infty}x_n=\xi$。
- 所问：递推数列极限
- 知识点：数列极限；极限与连续；一元函数微分学应用；零点定理
- 第一动作：先用归纳证明序列落在区间，再证明单调
- 答案：$\displaystyle \lim_{n\to\infty}x_n=\xi$，其中 $\xi$ 是方程 $x=1+2\ln x$ 在 $(e,+\infty)$ 内的唯一实根。
- 个人错因边界：user_confirmed；复发点集中在第二问：第一问唯一根已能识别，但递推数列极限不能直接设极限；必须先用数学归纳法证明区间不变性 \(e<x_n<\xi\)，再由 \(g(x)-x=1+2\ln x-x>0\)（在 \(e<x<\xi\) 内）推出 \(x_{n+1}>x_n\)，完成单调有界后才能取极限。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先判型
  - 构造辅助函数
  - 零点定理
  - 导数判单调
  - 数学归纳法
  - 条件转化
  - 单调有界
  - 单调有界准则
- 质量发现：
  - `repeat_evidence_and_relation_repaired`：三次明确错误日期与递推证明强边已同步。；建议：
- 关系裁决：
  - ：`add`；
- 当前快照：`stale`；正式卡 `ddc482f44bdf74056fc97ff412be235072d8f4cc14812172dfa97e126ce801ee`；唯一图片 1 个；物理路径 1 个。

### GS-434 58110 2026.5.20

- 题目：$f$ 在 $[0,1]$ 连续且 $f(0)=f(1)$。证明存在 $\xi$ 使 $f(\xi)=f(\xi+\frac12)$；推广到任意 $n\ge2$，证明存在 $\xi$ 使 $f(\xi)=f(\xi+\frac1n)$。
- 所问：连续函数存在性证明
- 知识点：极限与连续；零点定理；一元函数微分学应用
- 第一动作：先设 \varphi(x)=f(x+1/n)-f(x)，并列出 0,1/n,\ldots,(n-1)/n 处的相邻差
- 答案：存在 $\xi\in(0,\frac12]$，使 $f(\xi)=f(\xi+\frac12)$；对 $n\ge2$，存在 $\xi\in(0,1-\frac1n]$，使 $f(\xi)=f(\xi+\frac1n)$。
- 个人错因边界：user_confirmed；本次复发点主要在第二问：第一问的 \(1/2\) 平移差函数已能处理，但没有把 \(\frac1n\) 平移识别成“把 \([0,1]\) 分成 \(n\) 段 + 相邻函数值作差 + 望远镜求和”。应构造 \(\varphi(x)=f(x+\frac1n)-f(x)\)，考察 \(\varphi(0),\varphi(\frac1n),\ldots,\varphi(\frac{n-1}{n})\)，累加得到 \(f(1)-f(0)=0\)，再推出有零点。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先判型
  - 构造辅助函数
  - 零点定理
  - 条件转化
  - 望远镜求和
  - 分类讨论
- 质量发现：
  - `answer_domain_and_relation_repaired`：已补出平移点的实际定义域并删除宽泛作差关系。；建议：
- 关系裁决：
  - ：`keep`；
  - ：`remove`；
  - ：`remove`；
- 当前快照：`stale`；正式卡 `ceecb25f581b25e97cbe6db91f499327f39daa9c0c41ebee97c86e90da99aff8`；唯一图片 1 个；物理路径 1 个。

### GS-435 112872 2026.5.9

- 题目：对每个 $n$，方程 $f_n(x)=x^n-\cos x=0$ 在 $(0,1)$ 内有唯一根 $x_n$。研究 $\{x_n\}$ 的极限，并求 $\lim_{n\to\infty}(1-x_n)^{\frac1n\ln\cos x_n}$。
- 所问：方程根构造数列极限
- 知识点：数列极限；极限与连续；一元函数微分学应用；幂指极限；等价无穷小
- 第一动作：先固定 f_n(x)，把 x_{n+1} 代入 f_n(x) 并与 f_n(x_n)=0 比较
- 答案：对每个 $n$，方程 $x^n-\cos x=0$ 在 $(0,1)$ 内有唯一根 $x_n$；$x_n$ 单调递增且 $x_n\to1$；$\displaystyle \lim_{n\to\infty}(1-x_n)^{\frac1n\ln\cos x_n}=1$。
- 个人错因边界：user_confirmed；没有把“每个 $x_n$ 是不同函数 $f_n(x)$ 的零点”转化为“比较 $f_n(x_{n+1})$ 与 $f_n(x_n)$”；第一问已知 $f_n$ 在 $(0,1)$ 严格递增，但第二问没有把 $x_{n+1}$ 代回 $f_n(x)=x^n-\cos x$，利用 $f_n(x_{n+1})=x_{n+1}^n(1-x_{n+1})>0=f_n(x_n)$ 推出 $x_{n+1}>x_n$。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先判型
  - 构造辅助函数
  - 零点定理
  - 导数判单调
  - 单调有界
  - 单调有界准则
  - 条件转化
  - 取对数
  - 等价变形
- 质量发现：
  - `incomplete_answer_repaired`：标准答案已补齐唯一根、根列单调收敛和最终极限。；建议：
- 关系裁决：
  - ：`add`；
  - ：`remove`；
- 当前快照：`stale`；正式卡 `96b02cc676887e6c33d626781f0cc4cf33b531c22aa675f299ffde7868044ee9`；唯一图片 1 个；物理路径 1 个。

### GS-436 57740 2026.5.9

- 题目：计算 $\displaystyle \lim_{x\to0}\frac{\int_0^x[(3+2\tan t)^t-3^t]\,dt}{e^{3x^3}-1}$。核心是先用 $e^{3x^3}-1\sim3x^3$，再用洛必达把变上限积分求导，最后处理指数型差式。
- 所问：变上限积分型极限
- 知识点：极限与连续；变上限积分；等价无穷小；洛必达法则；幂指极限
- 第一动作：先写出 $$(3+2\tan x)^x=3^x\left(1+\frac{2\tan x}{3}\right)^x$$，并圈出小量中的系数 $1/3$
- 答案：$\displaystyle \frac{2}{27}$。
- 个人错因边界：user_confirmed；最后等价无穷小化简时丢了常数因子；底数接近常数 $3$ 时，没有先提出主量 $3$，把 $(3+2\tan x)^x$ 化成 $3^x(1+\frac{2\tan x}{3})^x$，导致把关键小量 $\frac{2\tan x}{3}$ 误当成 $2\tan x$。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先判型
  - 等价变形
  - 洛必达
  - 取对数
  - 条件转化
- 质量发现：
  - `error_taxonomy_repaired`：已从方法调取失败改为常数因子遗漏的 B5 检查断点。；建议：
- 关系裁决：
  - ：`keep`；
  - ：`remove`；
- 当前快照：`stale`；正式卡 `14b61aedde4e2b656808110df67f5855872eca08466b16baa7f0427b6cae6253`；唯一图片 1 个；物理路径 1 个。

### GS-438 170646 2026.5.9

- 题目：计算 $$ \lim_{x\to\infty}x^2\left[e^{(1+\frac1x)^x}-\left(1+\frac1x\right)^{ex}\right]. $$ 核心是令 $t=\frac1x$，把无穷远极限转成 $t\to0^+$；再把两个指数项都写成 $e^u$ 的函数值差。
- 所问：指数型极限
- 知识点：极限与连续；无穷远极限；幂指极限；拉格朗日中值定理；泰勒展开；等价无穷小
- 第一动作：先把两项写成 F(A)-F(B)，其中 F(u)=e^u，再用中值定理化成 F'(\xi)(A-B)
- 答案：$\displaystyle \frac18 e^{e+1}$。
- 个人错因边界：user_confirmed；没有把 $e^{(1+t)^{1/t}}$ 与 $e^{e\ln(1+t)/t}$ 看成同一函数 $e^u$ 在两个相近点处的函数值之差，导致没有用拉格朗日中值定理转成 $e^{\xi}(u_1-u_2)$；后续换元 $u=\frac{\ln(1+t)}t$ 后，没有继续用泰勒展开建立 $u-1\sim-\frac t2$，即 $t^2\sim4(u-1)^2$。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 换元
  - 中值定理
  - 泰勒展开
  - 洛必达
  - 等价变形
- 质量发现：
  - `detail_truncation_and_relation_repaired`：详情截断已修复，并仅保留同型强边。；建议：
- 关系裁决：
  - ：`keep`；
  - ：`keep`；
  - ：`remove`；
  - ：`remove`；
- 当前快照：`stale`；正式卡 `144b789c737a534d297202d97e68ca483b0a253f668eb0bb03ff0d0fdbb812ea`；唯一图片 1 个；物理路径 1 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
