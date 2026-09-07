---
wiki_id: MATHWIKI-REVIEW-026
type: target_level_semantic_review_batch
title: 全库逐题语义复核第10批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-026_全库逐题语义复核第10批20题.json
status: active
last_updated: 2026-07-23
---

# 全库逐题语义复核第10批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 0 张；覆盖 23 个物理图片路径与 22 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 10 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `MATH-TARGET-SEMANTIC-CLOSEOUT-20260723-B10`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-021](http://127.0.0.1:8765/open/GS-021) | 计算、判断或证明题目所问对象 | 极限与连续、左右极限、绝对值分段、实幂函数、复合函数极限、指数增长阶比较 | \(a=\sqrt{1+e-e^{-1}}\)，且实幂定义要求 \(a>0\)。 | pending_user_confirmation：个人原始错因未记录。旧详情曾把幂底数 a 误读成乘法系数，因此其中“把 e^{-∞} 误判为 1”的归因不能直接升级为用户事实；本轮只把“先识别 a 是幂底数，再分左右极限”登记为待复做检查点。 | power_base_misread_repaired |
| [GS-022](http://127.0.0.1:8765/open/GS-022) | 计算、判断或证明题目所问对象 | 极限与连续、拉格朗日中值定理、函数值差、无穷小阶数比较、参数边界、退化参数 | 当 \(a=1\) 时任意 \(P\in\mathbb R\)；当 \(a>0,\ a\ne1\) 时 \(P\le2\)。若题意要求对任意 \(a>0\) 都成立，则 \(P\le2\)。 | confirmed_personal：第2次错误已明确记录：非退化分支中已算出主阶 x^{P-2}，但只保留 P<2，漏掉 P=2 时极限仍为有限值。本轮另由题图发现必须先检查 a=1：此时差值恒为 0，任意实数 P 都成立。 | degenerate_parameter_branch_restored |
| [GS-023](http://127.0.0.1:8765/open/GS-023) | 计算、判断或证明题目所问对象 | 数列极限、指数隐式递推、拉格朗日中值定理、单调有界、极限方程 | \(\displaystyle\lim_{n\to\infty}x_n=0\)。 | pending_user_confirmation：个人原始错因未记录；当前只确认复做入口：不能直接代极限方程，应先把 e^{x_n}-1 写成 e^{x_n}-e^0，用拉格朗日中值定理推出 0<x_{n+1}<x_n，再由单调有界和极限方程收口。 | duplicate_formal_identity_hold |
| [GS-024](http://127.0.0.1:8765/open/GS-024) | 计算、判断或证明题目所问对象 | 一元函数微分学应用、斜渐近线、无穷远主量、截距极限、二项展开 | 斜渐近线为 \(y=x+\frac32\)。 | legacy_unclassified：旧结构化详情把断点记录为：求斜渐近线截距时，没有先提出 x^{3/2} 主量，因而没有把 y-x 化成 x[(1+1/x)^{3/2}-1]。原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。 | — |
| [GS-025](http://127.0.0.1:8765/open/GS-025) | 计算、判断或证明题目所问对象 | 一元函数微分学应用、斜渐近线、幂指极限、倒代换、泰勒展开、低阶项抵消 | \(y=\frac{x}{e}+\frac1{2e}\)。 | confirmed_personal：求截距 b 时没有把无穷远极限倒代换为零点小量，也没有在主项抵消后保留到二阶，导致常数项算错。 | same_card_asset_alias_preserved |
| [GS-026](http://127.0.0.1:8765/open/GS-026) | 计算、判断或证明题目所问对象 | 极限与连续、指数函数作差、等价无穷小、最低阶非零项、四阶泰勒展开 | \(\frac1{12}\)。 | pending_user_confirmation：个人原始错因未记录；本轮只确认复做入口：两个指数函数相减时先提公共指数因子造出 e^u-1，再对 u 展开到四阶，不能分别做粗略等价后相减。 | — |
| [GS-027](http://127.0.0.1:8765/open/GS-027) | 计算、判断或证明题目所问对象 | 极限与连续、含参变上限积分、积分变量与外部参数、高斯积分二阶矩、洛必达法则、非零极限反求参数 | \(a=-\frac{\sqrt\pi}{4},\ b=1\)。 | confirmed_personal：两次断点分别是积分变量与外部参数角色混淆，以及高斯积分常数和非零极限主项消失条件未落实。 | solution_asset_formula_only |
| [GS-028](http://127.0.0.1:8765/open/GS-028) | 计算、判断或证明题目所问对象 | 极限与连续、无穷远倒代换、复合等价无穷小、退化参数、分母公共结构 | A，即 \(k\ne1\)；此时 \(a=\frac1{k-1}\)。 | legacy_unclassified：旧结构化详情把断点记录为：已经想到 t=1/x，但没有先排除 k=1，也没有把分母整理为 (1+t)[(1+t)^{k-1}-1]。原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。 | — |
| [GS-029](http://127.0.0.1:8765/open/GS-029) | 计算、判断或证明题目所问对象 | 极限与连续、对数差合并、对数定义域、等价无穷小、二阶主量 | \(\displaystyle\lim_{x\to0}\frac{\ln(\sin^2x+e^x)-x}{\ln(e^{2x}-x^2)-2x}=-1\)。 | pending_user_confirmation：个人原始错因未记录；当前只确认复做入口：把 x、2x 分别写成 ln(e^x)、ln(e^{2x})，先合并对数差，再把两边都化成 ln(1+u) 比较二阶小量。 | checkmark_not_counted_as_failure |
| [GS-030](http://127.0.0.1:8765/open/GS-030) | 计算、判断或证明题目所问对象 | 极限与连续、取整函数、整数点左右取值、左右极限、对数等价无穷小 | \(a=-2,\ b=2\)。 | legacy_unclassified：旧结构化详情把断点记录为：虽已想到分左右极限，但没有同步固定取整函数在两侧的值，即 x→0+ 时 [x]=0、x→0- 时 [x]=-1。原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。 | — |
| [GS-031](http://127.0.0.1:8765/open/GS-031) | 计算、判断或证明题目所问对象 | 极限与连续、分式函数间断点、含参分母零点、导数判单调、介值定理 | B，共 2 个间断点。 | legacy_unclassified：旧结构化详情把断点记录为：令分母为零后，没有继续把分母设为辅助函数并用导数、两端趋势和介值定理判断零点个数。原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。 | false_removable_discontinuity_removed |
| [GS-032](http://127.0.0.1:8765/open/GS-032) | 计算、判断或证明题目所问对象 | 极限与连续、幂指式指数化、正切零点与无定义点、左右极限、间断点分类 | 间断点为 \(\frac\pi4,\frac{3\pi}4,\frac{5\pi}4,\frac{7\pi}4\)；其中 \(\frac{3\pi}4,\frac{7\pi}4\) 为可去间断点，\(\frac\pi4,\frac{5\pi}4\) 为第二类间断点。 | legacy_unclassified：旧结构化详情把断点记录为：只找了 tan(x-π/4)=0 的点，漏掉 tan 本身无定义的点；也没有先把幂指式指数化。来源日期存在冲突，个人原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。 | solution_asset_sketch_only |
| [GS-033](http://127.0.0.1:8765/open/GS-033) | 计算、判断或证明题目所问对象 | 极限与连续、候选间断点、x ln\|x\| 极限、指数奇点、左右极限、间断点分类 | C，共 2 个无穷间断点；\(x=1,2\) 为无穷间断点，\(x=0\) 为可去间断点。 | legacy_unclassified：旧结构化详情把断点记录为：没有从 ln\|x\|、\|x-1\| 和 (x-1)(x-2) 一次列全 x=0,1,2，也没有逐点判断指数项的正负无穷方向。原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。 | — |
| [GS-034](http://127.0.0.1:8765/open/GS-034) | 计算、判断或证明题目所问对象 | 极限与连续、绝对值分类、对数等价无穷小、左右极限符号、间断点分类 | A；\(x=\pm1\) 为跳跃间断点，\(x=0\) 为无穷间断点。 | confirmed_personal：两次错误都发生在临界点左右符号检查：分子绝对值和分母变号没有同步处理。 | — |
| [GS-035](http://127.0.0.1:8765/open/GS-035) | 计算、判断或证明题目所问对象 | 一元函数微分学应用、根号平方转绝对值、连续性、导数定义、左右导数 | D，在 \(x=1\) 连续但不可导。 | confirmed_personal：三次断点依次为：没有用左右导数；漏掉 sqrt(u^2)=\|u\|；连续性检查时把判断点 x=1 错代为 x=0。 | — |
| [GS-036](http://127.0.0.1:8765/open/GS-036) | 计算、判断或证明题目所问对象 | 极限与连续、连续函数代数封闭性、差函数还原、反证法、反例边界 | B。 | confirmed_personal：没有先利用连续函数对加减法封闭的性质检查 B；若 f+g 连续且 f 连续，则 g=(f+g)-f 连续，与题设矛盾。 | false_continuity_truth_table_removed |
| [GS-037](http://127.0.0.1:8765/open/GS-037) | 计算、判断或证明题目所问对象 | 极限与连续、函数列点态极限、幂次主导区域、分段极限函数、边界点连续性、参数反求 | 最小正值 \(\alpha=\frac\pi2\)。 | confirmed_personal：看到 x^{n+1} 与 x^n 后凭直觉判断整体趋于无穷，没有先按 \|x\|>1、\|x\|<1、x=±1 求点态极限函数，也漏掉用边界连续性反求 α。 | — |
| [GS-038](http://127.0.0.1:8765/open/GS-038) | 计算、判断或证明题目所问对象 | 极限与连续、底数边界、指数奇点、幂指式指数化、间断点分类 | C；第一类间断点只有 \(x=1\)，共 1 个。 | pending_user_confirmation：个人原始错因未记录；当前只确认复做入口：先列 x=0,1,2，再把幂指式写成指数式并逐点分类。 | removable_discontinuity_sides_repaired |
| [GS-039](http://127.0.0.1:8765/open/GS-039) | 计算、判断或证明题目所问对象 | 数列极限、递推数列通项、反正切递推、单调有界、固定点筛选、相邻比值压缩 | \(\displaystyle\lim_{n\to\infty}\frac{a_n}{b_n}=0\)。 | legacy_unclassified：旧结构化详情把断点记录为三段：没有先由 a_{n+1}=a_n^2 写出通项；没有利用 b_{n+1}∈(-π/4,0) 将 b_n=tan b_{n+1} 唯一改写为反正切递推；最后没有构造 c_n=a_n/b_n 并用相邻比值压缩。原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。 | — |
| [GS-040](http://127.0.0.1:8765/open/GS-040) | 计算、判断或证明题目所问对象 | 数列极限、极限定义、最终保号与保序、有界性、全称命题证伪、单侧扰动反例 | D。 | confirmed_personal：判断 D 时没有先把最终不等式翻译成待破坏目标，对从 a 上方或下方趋近的构造方向混乱。 | — |

## 逐题复核

### GS-021 1000题B组1.31

- 题目：幂底数参数的双侧极限存在
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；左右极限；绝对值分段；实幂函数；复合函数极限；指数增长阶比较
- 第一动作：先读清 \(a^{\frac{2+e^{1/x}}{1+e^{4/x}}}\) 的底数与指数角色，再分别计算左右极限。
- 答案：\(a=\sqrt{1+e-e^{-1}}\)，且实幂定义要求 \(a>0\)。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录。旧详情曾把幂底数 a 误读成乘法系数，因此其中“把 e^{-∞} 误判为 1”的归因不能直接升级为用户事实；本轮只把“先识别 a 是幂底数，再分左右极限”登记为待复做检查点。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先确认 a 是幂底数且 a>0，再分 \(x\to0^-\) 与 \(x\to0^+\)；右侧令 \(t=e^{1/x}\) 比较指数阶。
  - 先读清 \(a^{\frac{2+e^{1/x}}{1+e^{4/x}}}\) 的底数与指数角色，再分别计算左右极限。
- 质量发现：
  - `power_base_misread_repaired`：旧详情把幂底数 a 误读为乘法系数，导致左右极限和答案错误。；建议：
- 关系裁决：
  - GS-051：`remove_broad_or_stale_edge`；
  - GS-138：`remove_broad_or_stale_edge`；
  - GS-030：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `ab5c745670e6a2b870d19e36f04b4857aaef3333f132e2c05a93305ae910698a`；唯一图片 1 个；物理路径 1 个。

### GS-022 2 57971 2026.5.10 T1

- 题目：函数值差的无穷小阶数与退化参数
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；拉格朗日中值定理；函数值差；无穷小阶数比较；参数边界；退化参数
- 第一动作：先分 a=1 与 a≠1；非退化时设 f(u)=a^u，对 f(1/x)-f(1/(x+1)) 用拉格朗日中值定理。
- 答案：当 \(a=1\) 时任意 \(P\in\mathbb R\)；当 \(a>0,\ a\ne1\) 时 \(P\le2\)。若题意要求对任意 \(a>0\) 都成立，则 \(P\le2\)。
- 个人错因边界：confirmed_personal；第2次错误已明确记录：非退化分支中已算出主阶 x^{P-2}，但只保留 P<2，漏掉 P=2 时极限仍为有限值。本轮另由题图发现必须先检查 a=1：此时差值恒为 0，任意实数 P 都成立。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先检查 a=1 的退化分支；a≠1 时把差值写成同一函数在相近输入处的函数值差，用拉格朗日中值定理降阶。
  - 先分 a=1 与 a≠1；非退化时设 f(u)=a^u，对 f(1/x)-f(1/(x+1)) 用拉格朗日中值定理。
- 质量发现：
  - `degenerate_parameter_branch_restored`：旧答案漏掉 a=1 时原式恒为 0 的退化分支。；建议：
- 关系裁决：
  - GS-438：`verify_existing_strong_edge`；
  - GS-026：`remove_broad_or_stale_edge`；
  - GS-028：`remove_broad_or_stale_edge`；
  - GS-081：`remove_broad_or_stale_edge`；
- 当前快照：`stale`；正式卡 `5592f2e972e0e1918e2796adc6cc16c0e0e681bb54bd3e1f494e65cef7225da5`；唯一图片 1 个；物理路径 1 个。

### GS-023 2018年第21题 78861 2026.4.18

- 题目：指数隐式递推数列的收敛与极限
- 所问：计算、判断或证明题目所问对象
- 知识点：数列极限；指数隐式递推；拉格朗日中值定理；单调有界；极限方程
- 第一动作：把 e^{x_n}-1 写成 e^{x_n}-e^0，在 [0,x_n] 上用拉格朗日中值定理。
- 答案：\(\displaystyle\lim_{n\to\infty}x_n=0\)。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；当前只确认复做入口：不能直接代极限方程，应先把 e^{x_n}-1 写成 e^{x_n}-e^0，用拉格朗日中值定理推出 0<x_{n+1}<x_n，再由单调有界和极限方程收口。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先用拉格朗日中值定理制造相邻项大小关系，证明单调有界后再代极限方程。
  - 把 e^{x_n}-1 写成 e^{x_n}-e^0，在 [0,x_n] 上用拉格朗日中值定理。
- 质量发现：
  - `duplicate_formal_identity_hold`：与 GS-068 的来源、日期、方程和答案完全一致。；建议：
- 关系裁决：
  - GS-023：`remove_broad_or_stale_edge`；
  - GS-041：`remove_broad_or_stale_edge`；
  - GS-081：`remove_broad_or_stale_edge`；
- 当前快照：`stale`；正式卡 `1c44d7928a45a5c6f3880f0b3422ade588c7e38df96aba25036b3bacdf2c955b`；唯一图片 1 个；物理路径 1 个。

### GS-024 例题5.6 2026.4.1

- 题目：根式幂式曲线的斜渐近线
- 所问：计算、判断或证明题目所问对象
- 知识点：一元函数微分学应用；斜渐近线；无穷远主量；截距极限；二项展开
- 第一动作：先求 k=lim y/x=1，再把 y-x 化成 x[(1+1/x)^{3/2}-1]。
- 答案：斜渐近线为 \(y=x+\frac32\)。
- 个人错因边界：legacy_unclassified；旧结构化详情把断点记录为：求斜渐近线截距时，没有先提出 x^{3/2} 主量，因而没有把 y-x 化成 x[(1+1/x)^{3/2}-1]。原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 按 k、b 两步求斜渐近线；求 b 前先提出无穷远最高阶主量。
  - 先求 k=lim y/x=1，再把 y-x 化成 x[(1+1/x)^{3/2}-1]。
- 关系裁决：
  - GS-459：`verify_existing_strong_edge`；
  - GS-460：`verify_existing_strong_edge`；
  - GS-025：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `c7d5684fcab0473f7da419fd054acf262e184126ffce94a63d3b73a4dabeddfc`；唯一图片 1 个；物理路径 1 个。

### GS-025 2020年第15题 2026.4.1

- 题目：幂指型斜渐近线
- 所问：计算、判断或证明题目所问对象
- 知识点：一元函数微分学应用；斜渐近线；幂指极限；倒代换；泰勒展开；低阶项抵消
- 第一动作：先求 k=lim y/x=1/e，再令 t=1/x 处理 b=lim(y-kx)。
- 答案：\(y=\frac{x}{e}+\frac1{2e}\)。
- 个人错因边界：confirmed_personal；求截距 b 时没有把无穷远极限倒代换为零点小量，也没有在主项抵消后保留到二阶，导致常数项算错。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先拆 k、b；求 b 时令 t=1/x，并展开到主项抵消后的首个非零阶。
  - 先求 k=lim y/x=1/e，再令 t=1/x 处理 b=lim(y-kx)。
- 质量发现：
  - `same_card_asset_alias_preserved`：两条详情记录同 source_refid 且题图哈希相同。；建议：
- 关系裁决：
  - GS-025：`verify_existing_strong_edge`；
  - GS-151：`verify_existing_strong_edge`；
  - GS-454：`verify_existing_strong_edge`；
  - GS-455：`verify_existing_strong_edge`；
  - GS-459：`verify_existing_strong_edge`；
  - GS-460：`verify_existing_strong_edge`；
  - GS-497：`verify_existing_strong_edge`；
  - GS-500：`verify_existing_strong_edge`；
  - GS-533：`verify_existing_strong_edge`；
  - GS-467：`remove_broad_or_stale_edge`；
  - GS-025：`add_strong_edge`；
  - GS-029：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `50c09f179d0e8b011f1aaa70d0b9b27d4b7906f3524d547ac6526bc35b93f92b`；唯一图片 1 个；物理路径 2 个。

### GS-026 58037 2026.4.1 T1

- 题目：指数函数作差的四阶极限
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；指数函数作差；等价无穷小；最低阶非零项；四阶泰勒展开
- 第一动作：写成 e^{2-2cos x}[e^{x^2-2+2cos x}-1]。
- 答案：\(\frac1{12}\)。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；本轮只确认复做入口：两个指数函数相减时先提公共指数因子造出 e^u-1，再对 u 展开到四阶，不能分别做粗略等价后相减。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 提公共指数因子，把分子化成 e^u-1，再比较 u 与 x^4 的最低阶。
  - 写成 e^{2-2cos x}[e^{x^2-2+2cos x}-1]。
- 关系裁决：
  - GS-026：`verify_existing_strong_edge`；
  - GS-026：`remove_broad_or_stale_edge`；
  - GS-113：`remove_broad_or_stale_edge`；
  - GS-438：`remove_broad_or_stale_edge`；
- 当前快照：`stale`；正式卡 `b7bc4f21b6c2edad669b99658cd545e067d0cc0fbae61b0fb1b9247ccec97461`；唯一图片 1 个；物理路径 1 个。

### GS-027 1000题B组1.35 2026.5.9

- 题目：含参变上限积分的非零极限反求参数
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；含参变上限积分；积分变量与外部参数；高斯积分二阶矩；洛必达法则；非零极限反求参数
- 第一动作：把 e^{x^2-t^2} 拆成 e^{x^2}e^{-t^2}，把 e^{x^2} 提出积分号外。
- 答案：\(a=-\frac{\sqrt\pi}{4},\ b=1\)。
- 个人错因边界：confirmed_personal；两次断点分别是积分变量与外部参数角色混淆，以及高斯积分常数和非零极限主项消失条件未落实。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先分离变量并提出对 t 为常量的因子，再用有限非零极限条件消主项。
  - 把 e^{x^2-t^2} 拆成 e^{x^2}e^{-t^2}，把 e^{x^2} 提出积分号外。
- 质量发现：
  - `solution_asset_formula_only`：独立解析图仅含高斯积分公式，不是完整参数推导。；建议：
- 关系裁决：
  - GS-440：`remove_broad_or_stale_edge`；
  - GS-639：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `a6795537ee495e085625d881d26ddddda8c4754a4b619c250e05edb127a0be59`；唯一图片 2 个；物理路径 2 个。

### GS-028 579692 2026.4.28

- 题目：无穷远复合极限的参数条件
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；无穷远倒代换；复合等价无穷小；退化参数；分母公共结构
- 第一动作：先检查 k=1 使分母恒为 0；对 k≠1 再令 t=1/x。
- 答案：A，即 \(k\ne1\)；此时 \(a=\frac1{k-1}\)。
- 个人错因边界：legacy_unclassified；旧结构化详情把断点记录为：已经想到 t=1/x，但没有先排除 k=1，也没有把分母整理为 (1+t)[(1+t)^{k-1}-1]。原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先排除 k=1，再令 t=1/x，整理公共结构后使用等价无穷小。
  - 先检查 k=1 使分母恒为 0；对 k≠1 再令 t=1/x。
- 关系裁决：
  - GS-028：`remove_broad_or_stale_edge`；
  - GS-442：`remove_broad_or_stale_edge`；
- 当前快照：`stale`；正式卡 `c4f61cda2117c204626433331021d2376899ec2864ea1c3dcef895ee2bfd8655`；唯一图片 1 个；物理路径 1 个。

### GS-029 58018 2026.4.17 ✅2026.5.7

- 题目：对数差商的二阶极限
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；对数差合并；对数定义域；等价无穷小；二阶主量
- 第一动作：把 x 写成 ln(e^x)、把 2x 写成 ln(e^{2x})，分别合并对数差。
- 答案：\(\displaystyle\lim_{x\to0}\frac{\ln(\sin^2x+e^x)-x}{\ln(e^{2x}-x^2)-2x}=-1\)。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；当前只确认复做入口：把 x、2x 分别写成 ln(e^x)、ln(e^{2x})，先合并对数差，再把两边都化成 ln(1+u) 比较二阶小量。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 把线性主项写成对数，合并成 ln(1+u)，再比较二阶小量。
  - 把 x 写成 ln(e^x)、把 2x 写成 ln(e^{2x})，分别合并对数差。
- 质量发现：
  - `checkmark_not_counted_as_failure`：标题勾选日期不能独立证明第二次错误。；建议：
- 关系裁决：
  - GS-030：`remove_broad_or_stale_edge`；
  - GS-033：`remove_broad_or_stale_edge`；
  - GS-094：`remove_broad_or_stale_edge`；
  - GS-029：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `a8431ce73511b0c5fc0c3606f5f067e24bb5b7ed823792c776148919cf133232`；唯一图片 1 个；物理路径 1 个。

### GS-030 58098 2026.5.7

- 题目：取整函数双侧极限存在反求参数
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；取整函数；整数点左右取值；左右极限；对数等价无穷小
- 第一动作：写 x→0+ 时 [x]=0，x→0- 时 [x]=-1。
- 答案：\(a=-2,\ b=2\)。
- 个人错因边界：legacy_unclassified；旧结构化详情把断点记录为：虽已想到分左右极限，但没有同步固定取整函数在两侧的值，即 x→0+ 时 [x]=0、x→0- 时 [x]=-1。原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先固定取整函数的左右局部常值，再分别计算左右极限并令其相等。
  - 写 x→0+ 时 [x]=0，x→0- 时 [x]=-1。
- 关系裁决：
  - GS-030：`remove_broad_or_stale_edge`；
  - GS-033：`remove_broad_or_stale_edge`；
  - GS-030：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `8042b7a53b9115556d18fb33cdb10c9c4810f5457822b23e9471de3503154c20`；唯一图片 1 个；物理路径 1 个。

### GS-031 1000题A组6.16 2026.5.5

- 题目：含参分母零点个数与间断点计数
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；分式函数间断点；含参分母零点；导数判单调；介值定理
- 第一动作：令 g(x)=ln x-x/e+k，并计算 g′(x)=1/x-1/e。
- 答案：B，共 2 个间断点。
- 个人错因边界：legacy_unclassified；旧结构化详情把断点记录为：令分母为零后，没有继续把分母设为辅助函数并用导数、两端趋势和介值定理判断零点个数。原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 构造分母辅助函数，用唯一极值、两端趋势和介值定理数零点。
  - 令 g(x)=ln x-x/e+k，并计算 g′(x)=1/x-1/e。
- 质量发现：
  - `false_removable_discontinuity_removed`：分子恒为 1，分母零点不能约去。；建议：
- 关系裁决：
  - GS-032：`remove_broad_or_stale_edge`；
  - GS-051：`remove_broad_or_stale_edge`；
  - GS-072：`remove_broad_or_stale_edge`；
  - GS-215：`remove_broad_or_stale_edge`；
  - GS-240：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `9923d830f4c932a0dcf6bfb17dd82d7e0f6bcbd4eea1be44069b9403a1722a7f`；唯一图片 1 个；物理路径 1 个。

### GS-032 58083 2026.5.5

- 题目：幂指式间断点定位与分类
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；幂指式指数化；正切零点与无定义点；左右极限；间断点分类
- 第一动作：解 tan(x-π/4)=0 及 tan(x-π/4) 无定义，把四个候选点一次列全。
- 答案：间断点为 \(\frac\pi4,\frac{3\pi}4,\frac{5\pi}4,\frac{7\pi}4\)；其中 \(\frac{3\pi}4,\frac{7\pi}4\) 为可去间断点，\(\frac\pi4,\frac{5\pi}4\) 为第二类间断点。
- 个人错因边界：legacy_unclassified；旧结构化详情把断点记录为：只找了 tan(x-π/4)=0 的点，漏掉 tan 本身无定义的点；也没有先把幂指式指数化。来源日期存在冲突，个人原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 同时列出正切零点和无定义点，再指数化并逐点判断左右极限。
  - 解 tan(x-π/4)=0 及 tan(x-π/4) 无定义，把四个候选点一次列全。
- 质量发现：
  - `solution_asset_sketch_only`：解析图只是候选点草图；旧详情还缺左侧极限并含无法识别标记。；建议：
- 关系裁决：
  - GS-038：`verify_existing_strong_edge`；
  - GS-032：`remove_broad_or_stale_edge`；
  - GS-435：`remove_broad_or_stale_edge`；
  - GS-033：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `0294db69b6aed6f6e96b0ef48c4067d38d4c8ed88ee3962bcae4172c11893304`；唯一图片 2 个；物理路径 2 个。

### GS-033 81428 2026.5.5

- 题目：指数奇点乘积函数的无穷间断点计数
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；候选间断点；x ln|x| 极限；指数奇点；左右极限；间断点分类
- 第一动作：列出 x=0,1,2，并分别判断代数因子与指数因子的左右趋势。
- 答案：C，共 2 个无穷间断点；\(x=1,2\) 为无穷间断点，\(x=0\) 为可去间断点。
- 个人错因边界：legacy_unclassified；旧结构化详情把断点记录为：没有从 ln|x|、|x-1| 和 (x-1)(x-2) 一次列全 x=0,1,2，也没有逐点判断指数项的正负无穷方向。原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先从每个因子的定义域和分母列全候选点，再逐点做左右符号表。
  - 列出 x=0,1,2，并分别判断代数因子与指数因子的左右趋势。
- 关系裁决：
  - GS-033：`remove_broad_or_stale_edge`；
  - GS-033：`remove_broad_or_stale_edge`；
  - GS-094：`remove_broad_or_stale_edge`；
  - GS-500：`remove_broad_or_stale_edge`；
  - GS-033：`add_strong_edge`；
  - GS-038：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `da8a5fe0185e46020c1e131256269226e8e29688e3b56eec4d0ac7d8b2a4cc8a`；唯一图片 1 个；物理路径 1 个。

### GS-034 168317 1000题B组42

- 题目：绝对值对数商的间断点分类
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；绝对值分类；对数等价无穷小；左右极限符号；间断点分类
- 第一动作：列 x=-1,0,1，并对 ±1 分左右写出等价式与符号。
- 答案：A；\(x=\pm1\) 为跳跃间断点，\(x=0\) 为无穷间断点。
- 个人错因边界：confirmed_personal；两次错误都发生在临界点左右符号检查：分子绝对值和分母变号没有同步处理。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先列 -1,0,1，再在 ±1 同步跟踪分子绝对值和分母左右符号。
  - 列 x=-1,0,1，并对 ±1 分左右写出等价式与符号。
- 关系裁决：
  - GS-035：`verify_existing_strong_edge`；
  - GS-492：`verify_existing_strong_edge`；
  - GS-100：`remove_broad_or_stale_edge`；
  - GS-447：`remove_broad_or_stale_edge`；
  - GS-461：`remove_broad_or_stale_edge`；
  - GS-466：`remove_broad_or_stale_edge`；
- 当前快照：`stale`；正式卡 `ebcbcf3f36dc8be50ea7f77a7c531be7b8f8fa81af3ed266f7b8696f19583593`；唯一图片 1 个；物理路径 1 个。

### GS-035 1000题B组1.37 103059 根号平方可导性

- 题目：根号平方函数在尖点的连续与可导
- 所问：计算、判断或证明题目所问对象
- 知识点：一元函数微分学应用；根号平方转绝对值；连续性；导数定义；左右导数
- 第一动作：写 sqrt((x-1)^2)=|x-1|，得到 g(x)=e^{|x-1|}。
- 答案：D，在 \(x=1\) 连续但不可导。
- 个人错因边界：confirmed_personal；三次断点依次为：没有用左右导数；漏掉 sqrt(u^2)=|u|；连续性检查时把判断点 x=1 错代为 x=0。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先化为 |x-1|，再分别检查连续性和左右导数。
  - 写 sqrt((x-1)^2)=|x-1|，得到 g(x)=e^{|x-1|}。
- 关系裁决：
  - GS-035：`verify_existing_strong_edge`；
  - GS-097：`verify_existing_strong_edge`；
  - GS-100：`verify_existing_strong_edge`；
  - GS-447：`verify_existing_strong_edge`；
  - GS-448：`verify_existing_strong_edge`；
  - GS-461：`verify_existing_strong_edge`；
  - GS-466：`verify_existing_strong_edge`；
  - GS-492：`verify_existing_strong_edge`；
  - GS-049：`remove_broad_or_stale_edge`；
  - GS-472：`remove_broad_or_stale_edge`；
  - GS-498：`remove_broad_or_stale_edge`；
  - GS-523：`remove_broad_or_stale_edge`；
- 当前快照：`stale`；正式卡 `a07530eb2dae9370f11e95b621c657079a1c1420a058c1198c0c83a576bd3aa4`；唯一图片 1 个；物理路径 1 个。

### GS-036 1000题B组1.39

- 题目：连续函数代数运算必然性判断
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；连续函数代数封闭性；差函数还原；反证法；反例边界
- 第一动作：直接检查 B：若 f+g 连续，则 g=(f+g)-f 连续，产生矛盾。
- 答案：B。
- 个人错因边界：confirmed_personal；没有先利用连续函数对加减法封闭的性质检查 B；若 f+g 连续且 f 连续，则 g=(f+g)-f 连续，与题设矛盾。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 对声称“必然”的选项使用代数还原或合法反例，不套错误真值表。
  - 直接检查 B：若 f+g 连续，则 g=(f+g)-f 连续，产生矛盾。
- 质量发现：
  - `false_continuity_truth_table_removed`：旧详情把非连续函数运算误写成伪真值表并使用不合法反例。；建议：
- 当前快照：`stale`；正式卡 `9f0ff20c6295f5dfe2d588fe608d0304f3ab7853fc9b6ca7f0f0f30bdeae4131`；唯一图片 1 个；物理路径 1 个。

### GS-037 1000题B组1.40

- 题目：函数列点态极限的分段连续性反求参数
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；函数列点态极限；幂次主导区域；分段极限函数；边界点连续性；参数反求
- 第一动作：分 |x|>1、|x|<1、x=1、x=-1 四类求极限。
- 答案：最小正值 \(\alpha=\frac\pi2\)。
- 个人错因边界：confirmed_personal；看到 x^{n+1} 与 x^n 后凭直觉判断整体趋于无穷，没有先按 |x|>1、|x|<1、x=±1 求点态极限函数，也漏掉用边界连续性反求 α。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 按 |x| 与 1 的关系求分段极限函数，再在 ±1 列连续性条件。
  - 分 |x|>1、|x|<1、x=1、x=-1 四类求极限。
- 关系裁决：
  - GS-072：`remove_broad_or_stale_edge`；
- 当前快照：`stale`；正式卡 `7b8d34c04e94ce826c9d556845e26266c41a8b522afa56fe498d149f66674842`；唯一图片 1 个；物理路径 1 个。

### GS-038 2024年真题第一题

- 题目：幂指函数第一类间断点计数
- 所问：计算、判断或证明题目所问对象
- 知识点：极限与连续；底数边界；指数奇点；幂指式指数化；间断点分类
- 第一动作：列 x=0,1,2，再写 |x|^{g(x)}=e^{g(x)ln|x|}。
- 答案：C；第一类间断点只有 \(x=1\)，共 1 个。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；当前只确认复做入口：先列 x=0,1,2，再把幂指式写成指数式并逐点分类。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 列全候选点，指数化后逐点判断左右极限和类型。
  - 列 x=0,1,2，再写 |x|^{g(x)}=e^{g(x)ln|x|}。
- 质量发现：
  - `removable_discontinuity_sides_repaired`：正式正文一度误写为左右有限极限不等；实际两侧同趋 e。；建议：
- 关系裁决：
  - GS-038：`verify_existing_strong_edge`；
  - GS-038：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `dd1a7abede524691e794cdafe33ee8e5c916e9b392c1f5348b0ded85fad2dfd4`；唯一图片 1 个；物理路径 1 个。

### GS-039 1000题B组2.14 2026.5.5

- 题目：双递推数列的比值极限
- 所问：计算、判断或证明题目所问对象
- 知识点：数列极限；递推数列通项；反正切递推；单调有界；固定点筛选；相邻比值压缩
- 第一动作：先求 a_n=2^{-2^n}，并用 b_{n+1} 的区间把正切递推唯一改写为反正切递推。
- 答案：\(\displaystyle\lim_{n\to\infty}\frac{a_n}{b_n}=0\)。
- 个人错因边界：legacy_unclassified；旧结构化详情把断点记录为三段：没有先由 a_{n+1}=a_n^2 写出通项；没有利用 b_{n+1}∈(-π/4,0) 将 b_n=tan b_{n+1} 唯一改写为反正切递推；最后没有构造 c_n=a_n/b_n 并用相邻比值压缩。原始作答过程未单独保存，证据来源按 legacy_unclassified 处理。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先分别解析两列，再构造比值数列并用相邻比值趋零得到等比压缩。
  - 先求 a_n=2^{-2^n}，并用 b_{n+1} 的区间把正切递推唯一改写为反正切递推。
- 当前快照：`stale`；正式卡 `58c13eb85fd030b11d841fcd0dd5cf93f856aa4de489f737a55ec5cc4e532d09`；唯一图片 1 个；物理路径 1 个。

### GS-040 58061 2026.5.5

- 题目：数列极限性质真假判断与反例构造
- 所问：计算、判断或证明题目所问对象
- 知识点：数列极限；极限定义；最终保号与保序；有界性；全称命题证伪；单侧扰动反例
- 第一动作：把 D 的最终不等式写成待破坏目标，取 a_n=a-2/n。
- 答案：D。
- 个人错因边界：confirmed_personal；判断 D 时没有先把最终不等式翻译成待破坏目标，对从 a 上方或下方趋近的构造方向混乱。
- 一致性：题图—解析 —；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先把选项翻译成定义或不等式；否定全称命题时优先构造最简单反例。
  - 把 D 的最终不等式写成待破坏目标，取 a_n=a-2/n。
- 关系裁决：
  - GS-509：`verify_existing_strong_edge`；
  - GS-568：`verify_existing_strong_edge`；
  - GS-103：`remove_broad_or_stale_edge`；
  - GS-452：`remove_broad_or_stale_edge`；
  - GS-050：`add_strong_edge`；
- 当前快照：`stale`；正式卡 `41dfb05d532a0565c291e563fe5e7bda551d6be0047777ea15d736ea95691c5c`；唯一图片 1 个；物理路径 1 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
