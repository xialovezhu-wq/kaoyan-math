---
wiki_id: MATHWIKI-REVIEW-018
type: target_level_semantic_review_batch
title: 全库逐题语义复核第6批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-018_全库逐题语义复核第6批20题.json
status: active
last_updated: 2026-07-22
---

# 全库逐题语义复核第6批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 0 张；覆盖 43 个物理图片路径与 37 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 3 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `MATH-TARGET-SEMANTIC-CLOSEOUT-20260722-B06`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-405](http://127.0.0.1:8765/open/GS-405) | 计算二重积分 | 二重积分、二重积分对称性、二重积分轮换对称性、极坐标换元、二重积分变量换元、雅可比行列式 | \(\frac{8}{3}\ln 3\) | pending_user_confirmation：旧卡没有用户真实作答；轮换对称、极坐标和变量换元仅作为客观复做入口。 | cross_id_byte_identical_question_and_two_solutions |
| [GS-408](http://127.0.0.1:8765/open/GS-408) | 计算二重积分 | 二重积分、二重积分对称性、二重积分轮换对称性、极坐标换元、二重积分变量换元、雅可比行列式 | \(\frac{8}{3}\ln 3\) | pending_user_confirmation：旧卡没有用户真实作答；轮换对称、极坐标和变量换元仅作为客观复做入口。 | cross_id_byte_identical_question_and_two_solutions |
| [GS-414](http://127.0.0.1:8765/open/GS-414) | 计算二重积分 | 二重积分、二重积分对称性、二重积分轮换对称性、极坐标换元、二重积分变量换元、雅可比行列式 | \(\frac{8}{3}\ln 3\) | pending_user_confirmation：旧卡没有用户真实作答；轮换对称、极坐标和变量换元仅作为客观复做入口。 | cross_id_byte_identical_question_and_two_solutions |
| [GS-600](http://127.0.0.1:8765/open/GS-600) | 求曲线全长 | 定积分、变上限积分、定积分应用、曲线弧长、三角恒等变形、绝对值分类、定义域、曲线方程约束、定义域与固定弧长区间 \(x\in[-\frac\pi2,\frac\pi2]\) | \(4\) | confirmed_personal：没有先固定曲线全长的 \(x\) 区间；没有及时调用 \(1+\cos x=2\cos^2\frac x2\)；去根号时没有先写绝对值。 | — |
| [GS-603](http://127.0.0.1:8765/open/GS-603) | 求不定积分 | 不定积分、指数幂分式化简、指数对数互化、第一类换元、整体凑微分、有理函数积分、部分分式、原函数按定义域连通区间分别理解 | \(\displaystyle \frac{1}{2\ln\frac32}\ln\left\|\frac{3^x-2^x}{3^x+2^x}\right\|+C\) | confirmed_personal：换元后没有把 \(du=\ln\frac32\cdot u\,dx\) 中的 \(u\,dx\) 整体吸收，误把积分变成 \(\int\frac{u}{u^2-1}\,du\)，而不是 \(\frac1{\ln(3/2)}\int\frac{du}{u^2-1}\)。 | — |
| [GS-604](http://127.0.0.1:8765/open/GS-604) | 求不定积分 | 不定积分、有理函数积分、分式拆分、部分分式、原函数按定义域连通区间分别理解 | \(\displaystyle -\frac1x+\frac14\ln\left\|\frac{1+x}{1-x}\right\|-\frac12\arctan x+C\) | confirmed_personal：第1次入口先凑 \(d(\frac1x)\) 没先拆分（B3-METHOD）；第2次入口已对但拆分链中途停下，没把 \(\frac1{1-x^4}\) 拆成 \(\frac12(\frac1{1-x^2}+\frac1{1+x^2})\)、没把 \(\int\frac1{1-x^2}dx\) 推到对数型（B4-CHAIN）。 | — |
| [GS-605](http://127.0.0.1:8765/open/GS-605) | 求不定积分 | 不定积分、有理函数积分、分式拆分、部分分式、分部积分、反三角函数积分 | \(\displaystyle -\frac{\arctan x}{x}-\frac12(\arctan x)^2+\frac12\ln\frac{x^2}{1+x^2}+C\) | confirmed_personal：没有优先拆分有理函数；对 \(\int\frac{dx}{x(1+x^2)}\) 继续分部积分导致绕回原式得到 \(A=A\)；并混淆 \(\arctan x\) 与 \(\operatorname{arccot}x\) 的导数符号。 | — |
| [GS-609](http://127.0.0.1:8765/open/GS-609) | 求不定积分 | 不定积分、分部积分、有理函数积分、分式拆分、部分分式、对数幂积分 | \(\displaystyle \left(1-\frac1x\right)\ln(1-x)+C\) | confirmed_personal：没有先判断题目目标是"求精确原函数"；没有优先寻找恒等拆分与分部积分入口，反而把有限阶泰勒截断当恒等替换。 | — |
| [GS-610](http://127.0.0.1:8765/open/GS-610) | 求不定积分 | 不定积分、根式积分、根式整体换元、第二类换元、根式换元、分部积分、有理函数积分、反正切型积分 | \(\displaystyle 2x\sqrt{e^x-1}-4\sqrt{e^x-1}+4\arctan\sqrt{e^x-1}+C\) | confirmed_personal：没有先抓根式整体，而是尝试拆分 \(x\)、\(e^x\) 或把根式分母拆成两项；对根式差式有非法拆分倾向。 | — |
| [GS-618](http://127.0.0.1:8765/open/GS-618) | 求不定积分 | 不定积分、一元函数积分学的计算、根式积分、第一类换元、第二类换元、根式换元、三角换元、整体凑微分、回代化简、反三角回代 | \(\displaystyle \frac13(1+x^2)^{3/2}-(1+x^2)^{1/2}+C\) | confirmed_personal：没有把 \(\sec(\arctan x)\) 化简为 \(\sqrt{1+x^2}\)。 | solution_route_and_user_route_separated |
| [GS-619](http://127.0.0.1:8765/open/GS-619) | 求不定积分 | 不定积分、一元函数积分学的计算、第二类换元、第一类换元、根式换元、三角换元、三角恒等变形、整体凑微分、回代化简、三角形回代、反正切型积分 | \(\displaystyle \arctan\frac{x}{\sqrt{1+x^2}}+C\) | confirmed_personal：没有想到分子分母同乘 \(\cos t\)，没有把分母化成 \(1+\sin^2t\)，没有把 \(\sin t\) 看成整体，最后也没有主动通过直角三角形回代 \(\sin t\)。 | — |
| [GS-620](http://127.0.0.1:8765/open/GS-620) | 求不定积分 | 不定积分、一元函数积分学的计算、根式积分、幂次统一、分数幂凑微分、第一类换元、第二类换元、根式换元、整体凑微分 | \(\displaystyle -\frac43\sqrt{1-x^{3/2}}+C\) | confirmed_personal：没有把分子 \(\sqrt{x}\,dx\) 放到导数后面；令 \(\sqrt{x}=t\) 后没有正确利用 \(dx=2t\,dt\) 得到 \(2t^2dt\) 并凑 \(d(1-t^3)\)。 | — |
| [GS-621](http://127.0.0.1:8765/open/GS-621) | 求不定积分 | 不定积分、一元函数积分学的计算、三角函数有理式、三角恒等变形、恒等式补分子、三角拆项积分、第一类换元、整体凑微分 | \(\displaystyle \frac13\tan^3x+2\tan x-\cot x+C\) | confirmed_personal：没有想到补分子；把 \(\sin^2x\) 写成 \(1-\cos^2x\) 后，没有继续转成 \(\tan x,\sec x\) 并拆出 \(\sec^2x\,dx\)。 | — |
| [GS-622](http://127.0.0.1:8765/open/GS-622) | 求不定积分 | 不定积分、一元函数积分学的计算、三角函数有理式、三角恒等变形、半角公式、分母平方化、万能代换、第一类换元、整体凑微分 | \(\displaystyle -\frac{2}{1+\tan\frac{x}{2}}+C\) | confirmed_personal：没有想到半角公式；没有想到把 \(1\) 写成半角平方和；没有想到分子分母同除 \(\cos^2\frac{x}{2}\)；没有凑出 \(d(\tan\frac{x}{2})\)。 | — |
| [GS-623](http://127.0.0.1:8765/open/GS-623) | 求不定积分 | 不定积分、一元函数积分学的计算、三角函数有理式、分母整体法、分子线性拆分、第一类换元、整体凑微分、对数型积分 | \(\displaystyle \frac12x-\frac12\ln\|\sin x+\cos x\|+C\) | confirmed_personal：没有把分母看成整体；没有主动用分母导数参与拆分分子；因此没有触发 \(\int\frac{F'(x)}{F(x)}dx=\ln\|F(x)\|\)。 | — |
| [GS-624](http://127.0.0.1:8765/open/GS-624) | 求不定积分 | 不定积分、一元函数积分学的计算、三角函数有理式、三角恒等变形、二倍角公式、半角公式、万能代换、第一类换元、整体凑微分 | \(\displaystyle \frac14\ln\left\|\tan\frac{x}{2}\right\|+\frac18\tan^2\frac{x}{2}+C\) | confirmed_personal：没有想到倍角展开；没有提公因式；没有把 \(1+\cos x\) 半角化；没有触发 \(t=\tan\frac{x}{2}\) 的万能代换。 | — |
| [GS-625](http://127.0.0.1:8765/open/GS-625) | 求不定积分 | 不定积分、一元函数积分学的计算、三角函数有理式、参数分类讨论、参数退化讨论、第一类换元、整体凑微分、提公因式凑微分、反正切型积分 | \(\displaystyle \begin{cases}\frac{1}{b^2}\tan x+C, & a=0,\ b\ne0,\\ -\frac{1}{a^2}\cot x+C, & a\ne0,\ b=0,\\ \frac{1}{ab}\arctan\!\left(\frac{a}{b}\tan x\right)+C, & a\ne0,\ b\ne0.\end{cases}\) | confirmed_personal：默认 \(a,b\ne0\)，没有分情况；非零情况没有提取 \(b^2\cos^2x\) 来制造 \(\sec^2x\,dx=d(\tan x)\)。 | — |
| [GS-630](http://127.0.0.1:8765/open/GS-630) | 求不定积分 | 不定积分、一元函数积分学的计算、分部积分、第一类换元、整体凑微分、分母平方凑微分、分部积分降幂 | \(\displaystyle -\frac{x^2e^x}{x+2}+xe^x-e^x+C\) | confirmed_personal：没有先检查分子求导后的结构，导致没发现分部积分后可以约掉一个 \((x+2)\)。 | — |
| [GS-631](http://127.0.0.1:8765/open/GS-631) | 求不定积分 | 不定积分、一元函数积分学的计算、根式积分、第二类换元、根式换元、根式整体换元、换元后反解原变量、有理函数积分、部分分式、复合函数求导、对数型积分 | \(\displaystyle -\frac{\sqrt{1-x^2}}{x}+\ln\left\|\frac{\sqrt{1+x}+\sqrt{1-x}}{\sqrt{1+x}-\sqrt{1-x}}\right\|+C\) | confirmed_personal：没有稳定触发根式整体换元；根号套分式求导漏外层根号因子；从 \(t^2(1+x)=1-x\) 反解 \(x\) 时没有把含 \(x\) 项集中并提取 \(x\)；部分分式中混淆不可约二次因式和重复一次因式；对 \(\arctan x\) 的导数与积分方向曾混淆。 | same_event_action_gaps_not_counted_as_recurrences |
| [GS-632](http://127.0.0.1:8765/open/GS-632) | 求不定积分 | 不定积分、一元函数积分学的计算、三角函数有理式、三角恒等变形、三角拆项积分、第一类换元、整体凑微分、分部积分 | \(\displaystyle e^{2x}\tan x+C\) | confirmed_personal：没有把整理后的两项拆成两个积分分别处理，也没有继续把 \(\int e^{2x}\sec^2x\,dx\) 写成 \(\int e^{2x}\,d(\tan x)\) 做分部积分观察抵消。 | — |

## 逐题复核

### GS-405 2024年真题17-2

- 题目：第一象限内由 xy=1/3、xy=3、y=x/3、y=3x 围成区域，计算二重积分 ∬(1+x-y)dxdy。
- 所问：计算二重积分
- 知识点：二重积分；二重积分对称性；二重积分轮换对称性；极坐标换元；二重积分变量换元；雅可比行列式
- 第一动作：先写交换 \(x,y\) 后的配对积分，并检查两式相加是否消去 \(x-y\)。
- 答案：\(\frac{8}{3}\ln 3\)
- 个人错因边界：pending_user_confirmation；旧卡没有用户真实作答；轮换对称、极坐标和变量换元仅作为客观复做入口。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 交换 x、y 后区域不变，配对积分使 x-y 相消。
  - 把积分化为区域面积。
  - 用极坐标或 u=xy、v=y/x 直化边界并计算面积。
- 质量发现：
  - `cross_id_byte_identical_question_and_two_solutions`：GS-403、GS-405、GS-408、GS-414 的题图、两张解析图和 source_refid 完全相同。；建议：保留四个稳定 ID，禁止普通知识聚合，等待用户决定是否合并或删除。
- 关系裁决：
  - GS-403：`identity_candidate_blocked`；题图、两张解析图和 source_refid 完全相同且无独立复发证据；不建立普通知识边。
- 当前快照：`stale`；正式卡 `6ef54191b2ae9aa2ddcb00b706acf99e69644719d7d08ad800db9e38a340a51e`；唯一图片 3 个；物理路径 3 个。

### GS-408 2024年真题17-3

- 题目：第一象限内由 xy=1/3、xy=3、y=x/3、y=3x 围成区域，计算二重积分 ∬(1+x-y)dxdy。
- 所问：计算二重积分
- 知识点：二重积分；二重积分对称性；二重积分轮换对称性；极坐标换元；二重积分变量换元；雅可比行列式
- 第一动作：先写交换 \(x,y\) 后的配对积分，并检查两式相加是否消去 \(x-y\)。
- 答案：\(\frac{8}{3}\ln 3\)
- 个人错因边界：pending_user_confirmation；旧卡没有用户真实作答；轮换对称、极坐标和变量换元仅作为客观复做入口。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 交换 x、y 后区域不变，配对积分使 x-y 相消。
  - 把积分化为区域面积。
  - 用极坐标或 u=xy、v=y/x 直化边界并计算面积。
- 质量发现：
  - `cross_id_byte_identical_question_and_two_solutions`：GS-403、GS-405、GS-408、GS-414 的题图、两张解析图和 source_refid 完全相同。；建议：保留四个稳定 ID，禁止普通知识聚合，等待用户决定是否合并或删除。
- 关系裁决：
  - GS-403：`identity_candidate_blocked`；题图、两张解析图和 source_refid 完全相同且无独立复发证据；不建立普通知识边。
- 当前快照：`stale`；正式卡 `1ad195158de46c164cce4aa954c6b04987eb87d73b5ce8d7791ba9bb7021f5e2`；唯一图片 3 个；物理路径 3 个。

### GS-414 2024年真题17-4

- 题目：第一象限内由 xy=1/3、xy=3、y=x/3、y=3x 围成区域，计算二重积分 ∬(1+x-y)dxdy。
- 所问：计算二重积分
- 知识点：二重积分；二重积分对称性；二重积分轮换对称性；极坐标换元；二重积分变量换元；雅可比行列式
- 第一动作：先写交换 \(x,y\) 后的配对积分，并检查两式相加是否消去 \(x-y\)。
- 答案：\(\frac{8}{3}\ln 3\)
- 个人错因边界：pending_user_confirmation；旧卡没有用户真实作答；轮换对称、极坐标和变量换元仅作为客观复做入口。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 交换 x、y 后区域不变，配对积分使 x-y 相消。
  - 把积分化为区域面积。
  - 用极坐标或 u=xy、v=y/x 直化边界并计算面积。
- 质量发现：
  - `cross_id_byte_identical_question_and_two_solutions`：GS-403、GS-405、GS-408、GS-414 的题图、两张解析图和 source_refid 完全相同。；建议：保留四个稳定 ID，禁止普通知识聚合，等待用户决定是否合并或删除。
- 关系裁决：
  - GS-403：`identity_candidate_blocked`；题图、两张解析图和 source_refid 完全相同且无独立复发证据；不建立普通知识边。
- 当前快照：`stale`；正式卡 `1600b6c33f97ea29410717315c6c6f40987e531b0eb3fce1026d3b2edaf6a521`；唯一图片 3 个；物理路径 3 个。

### GS-600 58064 变上限积分曲线弧长

- 题目：求变上限积分函数 y=∫[-π/2,x]√(cos t)dt 所表示曲线的全长。
- 所问：求曲线全长
- 知识点：定积分；变上限积分；定积分应用；曲线弧长；三角恒等变形；绝对值分类；定义域；曲线方程约束；定义域与固定弧长区间 \(x\in[-\frac\pi2,\frac\pi2]\)
- 第一动作：先由 \(\sqrt{\cos t}\) 要求 \(\cos t\ge0\)，并结合积分路径从 \(-\frac\pi2\) 到 \(x\)，确定 \(-\frac\pi2\le x\le\frac\pi2\)
- 答案：\(4\)
- 个人错因边界：confirmed_personal；没有先固定曲线全长的 \(x\) 区间；没有及时调用 \(1+\cos x=2\cos^2\frac x2\)；去根号时没有先写绝对值。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 先由根式确定 x∈[-π/2,π/2]。
  - 求 y′=√(cos x)，套直角坐标弧长公式。
  - 用 1+cos x=2cos²(x/2) 并按区间去绝对值。
- 关系裁决：
  - GS-292：`verify_existing_strong_edge`；根式化简必须保留绝对值并用区间判符号。
  - GS-595：`verify_existing_strong_edge`；曲线弧长对象识别及对应表示下公式选择。
  - GS-635：`verify_existing_strong_edge`；先固定积分路径和变量范围，再处理绝对值或分段。
  - GS-644：`verify_existing_strong_edge`；曲线完整描线范围、对称性与弧长区间。
  - GS-621：`remove_broad_or_stale_edge`；题目所问数学对象不同。
  - GS-622：`remove_broad_or_stale_edge`；题目所问数学对象不同。
  - GS-624：`remove_broad_or_stale_edge`；题目所问数学对象不同。
  - GS-466：`remove_broad_or_stale_edge`；题目所问数学对象不同。
- 当前快照：`stale`；正式卡 `40cc572da1755d6b50eff49b76660968bda6267550d0fb1901935d16abc78f1e`；唯一图片 2 个；物理路径 2 个。

### GS-603 57707-1 指数幂分式换元

- 题目：计算 ∫(2^x·3^x)/(9^x-4^x)dx。
- 所问：求不定积分
- 知识点：不定积分；指数幂分式化简；指数对数互化；第一类换元；整体凑微分；有理函数积分；部分分式；原函数按定义域连通区间分别理解
- 第一动作：先将分子分母同时除以 \(4^x\)，得到 \(\frac{(\frac32)^x}{[(\frac32)^x]^2-1}\)。
- 答案：\(\displaystyle \frac{1}{2\ln\frac32}\ln\left|\frac{3^x-2^x}{3^x+2^x}\right|+C\)
- 个人错因边界：confirmed_personal；换元后没有把 \(du=\ln\frac32\cdot u\,dx\) 中的 \(u\,dx\) 整体吸收，误把积分变成 \(\int\frac{u}{u^2-1}\,du\)，而不是 \(\frac1{\ln(3/2)}\int\frac{du}{u^2-1}\)。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 分子分母同除 4^x。
  - 令 u=(3/2)^x 并整体吸收 u dx。
  - 对 1/(u²-1) 做部分分式并回代。
- 关系裁决：
  - GS-620：`verify_existing_strong_edge`；换元后都必须让新变量微分整体吸收原分子因子。
  - GS-163：`verify_existing_strong_edge`；换元时必须整体吸收内层微分因子。
  - GS-268：`verify_existing_strong_edge`；必须让内层幂的微分与原分子完整对齐。
  - GS-270：`verify_existing_strong_edge`；完整整体换元、同步替换微分并转有理函数。
  - GS-587：`verify_existing_strong_edge`；主动制造内层导数，再换元并做部分分式。
  - GS-637：`verify_existing_strong_edge`；指数结构先中心化或同除主因子，再换元为有理函数。
  - GS-604：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-605：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-609：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-618：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-619：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-621：`remove_broad_or_stale_edge`；只共享上位主题，不能支撑普通强边。
  - GS-622：`remove_broad_or_stale_edge`；只共享上位主题，不能支撑普通强边。
  - GS-623：`remove_broad_or_stale_edge`；只共享上位主题，不能支撑普通强边。
  - GS-625：`remove_broad_or_stale_edge`；只共享上位主题，不能支撑普通强边。
- 当前快照：`stale`；正式卡 `2a31ea6a45c95511c85d67feb73e09e5503209b4a2f13c625fd7a0f5c4a7347d`；唯一图片 2 个；物理路径 2 个。

### GS-604 57707-2 有理函数分式拆分

- 题目：计算 ∫dx/[x²(1-x⁴)]。
- 所问：求不定积分
- 知识点：不定积分；有理函数积分；分式拆分；部分分式；原函数按定义域连通区间分别理解
- 第一动作：先将分子分母同乘 \(x^2\)，制造 \(x^4(1-x^4)\)，再利用 \(\frac1{x^4(1-x^4)}=\frac1{x^4}+\frac1{1-x^4}\)。
- 答案：\(\displaystyle -\frac1x+\frac14\ln\left|\frac{1+x}{1-x}\right|-\frac12\arctan x+C\)
- 个人错因边界：confirmed_personal；第1次入口先凑 \(d(\frac1x)\) 没先拆分（B3-METHOD）；第2次入口已对但拆分链中途停下，没把 \(\frac1{1-x^4}\) 拆成 \(\frac12(\frac1{1-x^2}+\frac1{1+x^2})\)、没把 \(\int\frac1{1-x^2}dx\) 推到对数型（B4-CHAIN）。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 分子分母同乘 x²并拆出 1/x⁴ 与 1/(1-x⁴)。
  - 继续按平方差与不可约二次因式拆分。
  - 分别收口为幂、对数和反正切项。
- 关系裁决：
  - GS-605：`verify_existing_strong_edge`；第一动作均为先拆有理分式再决定后续积分。
  - GS-168：`verify_existing_strong_edge`；有理分式因式分解、部分分式及对数项收口。
  - GS-266：`verify_existing_strong_edge`；拆出分母导数项后识别反正切标准型。
  - GS-278：`verify_existing_strong_edge`；一次因子与不可约二次因子的部分分式拆分。
  - GS-609：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-631：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-162：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-270：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-581：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
- 当前快照：`stale`；正式卡 `aca851f981a5c244cb5c7a423bffb15edf6ab5e35a8a32332427fe2b09ceb996`；唯一图片 2 个；物理路径 2 个。

### GS-605 57707-3 反三角乘有理分部绕圈

- 题目：计算 ∫arctan(x)/[x²(1+x²)]dx。
- 所问：求不定积分
- 知识点：不定积分；有理函数积分；分式拆分；部分分式；分部积分；反三角函数积分
- 第一动作：先写 \(\frac1{x^2(1+x^2)}=\frac1{x^2}-\frac1{1+x^2}\)。
- 答案：\(\displaystyle -\frac{\arctan x}{x}-\frac12(\arctan x)^2+\frac12\ln\frac{x^2}{1+x^2}+C\)
- 个人错因边界：confirmed_personal；没有优先拆分有理函数；对 \(\int\frac{dx}{x(1+x^2)}\) 继续分部积分导致绕回原式得到 \(A=A\)；并混淆 \(\arctan x\) 与 \(\operatorname{arccot}x\) 的导数符号。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 先拆 1/[x²(1+x²)]。
  - 分别以 d(-1/x) 与 d(arctan x) 做分部积分。
  - 剩余有理函数继续拆分，避免恒等式绕圈。
- 关系裁决：
  - GS-609：`verify_existing_strong_edge`；先拆式，再用倒数型微分做分部积分。
  - GS-630：`verify_existing_strong_edge`；把分母倒数的微分选作分部积分入口。
  - GS-632：`verify_existing_strong_edge`；构成无效恒等式绕圈与有效辅助项抵消的诊断对照。
  - GS-631：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-266：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-270：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-601：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
- 当前快照：`stale`；正式卡 `8408d320fc6acfcf199178af759c30857fe1d4daba9fc95bd3439a7c55788973`；唯一图片 2 个；物理路径 2 个。

### GS-609 57707-5 对数幂乘积积分泰勒误用

- 题目：计算 ∫[x+ln(1-x)]/x² dx。
- 所问：求不定积分
- 知识点：不定积分；分部积分；有理函数积分；分式拆分；部分分式；对数幂积分
- 第一动作：先写出 \(\frac{x+\ln(1-x)}{x^2}=\frac1x+\frac{\ln(1-x)}{x^2}\)。
- 答案：\(\displaystyle \left(1-\frac1x\right)\ln(1-x)+C\)
- 个人错因边界：confirmed_personal；没有先判断题目目标是"求精确原函数"；没有优先寻找恒等拆分与分部积分入口，反而把有限阶泰勒截断当恒等替换。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 先拆成 1/x 与 ln(1-x)/x²。
  - 第二项用分部积分。
  - 合并对数项；泰勒截断不用于精确原函数。
- 关系裁决：
  - GS-610：`verify_existing_strong_edge`；结构化归后出现对数因子，再触发分部积分。
  - GS-630：`verify_existing_strong_edge`；都需识别负倒数微分并用分部积分降复杂度。
  - GS-632：`verify_existing_strong_edge`；分部积分后必须检查残余项是否精确抵消。
  - GS-686：`verify_existing_strong_edge`；识别倒数型微分并用分部积分降低复杂度。
  - GS-601：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
- 当前快照：`stale`；正式卡 `28bcfbff391f24e72291b91c03481b3396cfd5e465c979d2256a8a3855057640`；唯一图片 2 个；物理路径 2 个。

### GS-610 57869-2 根式整体换元分部积分

- 题目：计算 ∫x e^x/√(e^x-1) dx。
- 所问：求不定积分
- 知识点：不定积分；根式积分；根式整体换元；第二类换元；根式换元；分部积分；有理函数积分；反正切型积分
- 第一动作：先令 \(t=\sqrt{e^x-1}\)，并同步写出 \(e^x=t^2+1,\ x=\ln(1+t^2),\ dx=\frac{2t}{1+t^2}dt\)。
- 答案：\(\displaystyle 2x\sqrt{e^x-1}-4\sqrt{e^x-1}+4\arctan\sqrt{e^x-1}+C\)
- 个人错因边界：confirmed_personal；没有先抓根式整体，而是尝试拆分 \(x\)、\(e^x\) 或把根式分母拆成两项；对根式差式有非法拆分倾向。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 令 t=√(e^x-1)，同步反解 e^x、x 与 dx。
  - 化为 2∫ln(1+t²)dt。
  - 分部积分并把 t²/(1+t²) 补常数化简。
- 关系裁决：
  - GS-631：`verify_existing_strong_edge`；都要求把完整根式作为换元对象并同步反解原变量。
  - GS-270：`verify_existing_strong_edge`；都以指数根式整体为换元对象。
  - GS-575：`verify_existing_strong_edge`；根式整体换元后化成反正切型有理积分。
  - GS-618：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-619：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-620：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-630：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-602：`remove_broad_or_stale_edge`；题目所问数学对象不同。
- 当前快照：`stale`；正式卡 `27be846eacebaf6ba7c5b9e86c97bb568dbbf9ebb1d49f896faa9d467d52274a`；唯一图片 2 个；物理路径 2 个。

### GS-618 57869-3 根式三角代换回代

- 题目：计算 ∫x³/√(1+x²) dx。
- 所问：求不定积分
- 知识点：不定积分；一元函数积分学的计算；根式积分；第一类换元；第二类换元；根式换元；三角换元；整体凑微分；回代化简；反三角回代
- 第一动作：先写 \(t=\arctan x\)，再由 \(\tan t=x\) 推出 \(\sec t=\sqrt{1+x^2}\)。
- 答案：\(\displaystyle \frac13(1+x^2)^{3/2}-(1+x^2)^{1/2}+C\)
- 个人错因边界：confirmed_personal；没有把 \(\sec(\arctan x)\) 化简为 \(\sqrt{1+x^2}\)。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 图片路线直接令 u=1+x²。
  - 把 x³dx 写成 (u-1)du/2。
  - 积分后回代；另将用户三角路线的回代断点单独保留。
- 质量发现：
  - `solution_route_and_user_route_separated`：解析图使用 u=1+x² 的直接路线；用户历史记录对应 x=tan t 的回代断点，二者已分层记录。；建议：
- 关系裁决：
  - GS-619：`verify_existing_strong_edge`；共享三角代换局部路线中的中段化简与完整回代。
  - GS-268：`verify_existing_strong_edge`；优先检查内层整体微分的直接换元路线。
  - GS-292：`verify_existing_strong_edge`；三角代换的角度范围、根式符号和回代必须一致。
  - GS-592：`verify_existing_strong_edge`；根式积分中的三角换元与答案形式还原。
  - GS-620：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-631：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-546：`remove_broad_or_stale_edge`；题目所问数学对象不同。
  - GS-587：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
- 当前快照：`stale`；正式卡 `44bea9ab0cb0e80611d29f59c257940bba28945c282924f2329b7fb140ef4a50`；唯一图片 2 个；物理路径 2 个。

### GS-619 57869-4 三角代换中段化简

- 题目：计算 ∫dx/[(2x²+1)√(1+x²)]。
- 所问：求不定积分
- 知识点：不定积分；一元函数积分学的计算；第二类换元；第一类换元；根式换元；三角换元；三角恒等变形；整体凑微分；回代化简；三角形回代；反正切型积分
- 第一动作：先把 \(\sec t\) 和 \(\tan t\) 全部改写成 \(\sin t,\cos t\)，再检查能否凑出 \(\cos tdt=d(\sin t)\)。
- 答案：\(\displaystyle \arctan\frac{x}{\sqrt{1+x^2}}+C\)
- 个人错因边界：confirmed_personal；没有想到分子分母同乘 \(\cos t\)，没有把分母化成 \(1+\sin^2t\)，没有把 \(\sin t\) 看成整体，最后也没有主动通过直角三角形回代 \(\sin t\)。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 可令 u=x/√(1+x²) 直接化为反正切型。
  - 用户三角路线中需把分母化成只含 sin t。
  - 完成中段化简并回代。
- 关系裁决：
  - GS-269：`verify_existing_strong_edge`；三角代换后必须完成中段化简和回代。
  - GS-292：`verify_existing_strong_edge`；共享三角代换中段化简与完整回代。
  - GS-592：`verify_existing_strong_edge`；三角换元后统一三角函数并凑新变量微分。
  - GS-620：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-621：`remove_broad_or_stale_edge`；只共享上位主题，不能支撑普通强边。
  - GS-622：`remove_broad_or_stale_edge`；只共享上位主题，不能支撑普通强边。
  - GS-623：`remove_broad_or_stale_edge`；只共享上位主题，不能支撑普通强边。
  - GS-624：`remove_broad_or_stale_edge`；只共享上位主题，不能支撑普通强边。
  - GS-546：`remove_broad_or_stale_edge`；题目所问数学对象不同。
- 当前快照：`stale`；正式卡 `b11437a72982f64e3cff187acf24c343581d999d118712bd88db621cfe11f695`；唯一图片 2 个；物理路径 2 个。

### GS-620 57869-6 根式幂次凑微分

- 题目：计算 ∫√[x/(1-x√x)] dx。
- 所问：求不定积分
- 知识点：不定积分；一元函数积分学的计算；根式积分；幂次统一；分数幂凑微分；第一类换元；第二类换元；根式换元；整体凑微分
- 第一动作：先把原式改写成 \(\int\frac{x^{1/2}}{\sqrt{1-x^{3/2}}}\,dx\)，再凑 \(d(x^{3/2})\)。
- 答案：\(\displaystyle -\frac43\sqrt{1-x^{3/2}}+C\)
- 个人错因边界：confirmed_personal；没有把分子 \(\sqrt{x}\,dx\) 放到导数后面；令 \(\sqrt{x}=t\) 后没有正确利用 \(dx=2t\,dt\) 得到 \(2t^2dt\) 并凑 \(d(1-t^3)\)。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 把根式统一写成 x^(1/2)/√(1-x^(3/2))。
  - 令 u=1-x^(3/2)。
  - 积分并回代。
- 关系裁决：
  - GS-268：`verify_existing_strong_edge`；根式统一为幂后凑内层幂微分。
  - GS-636：`verify_existing_strong_edge`；统一幂次后把内层幂作为整体变量。
  - GS-630：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-631：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
- 当前快照：`stale`；正式卡 `a290b8db5c45b2fa40469833265c5dec604c8c9b71a16da4c03947a2c49c5761`；唯一图片 2 个；物理路径 2 个。

### GS-621 57931-1 三角有理式补分子

- 题目：计算 ∫dx/(sin²x cos⁴x)。
- 所问：求不定积分
- 知识点：不定积分；一元函数积分学的计算；三角函数有理式；三角恒等变形；恒等式补分子；三角拆项积分；第一类换元；整体凑微分
- 第一动作：先把分子 \(1\) 写成 \((\sin^2x+\cos^2x)^2\)，再展开并按 \(\sin^2x\cos^4x\) 分项相除。
- 答案：\(\displaystyle \frac13\tan^3x+2\tan x-\cot x+C\)
- 个人错因边界：confirmed_personal；没有想到补分子；把 \(\sin^2x\) 写成 \(1-\cos^2x\) 后，没有继续转成 \(\tan x,\sec x\) 并拆出 \(\sec^2x\,dx\)。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 用 (sin²x+cos²x)² 补分子。
  - 按 sin²x cos⁴x 分项相除。
  - 分别积分为 tan 与 cot 项。
- 关系裁决：
  - GS-632：`verify_existing_strong_edge`；都需先展开平方结构，再按积分线性性拆项。
  - GS-622：`remove_broad_or_stale_edge`；关系只来自同来源或邻近编号。
  - GS-623：`remove_broad_or_stale_edge`；关系只来自同来源或邻近编号。
  - GS-624：`remove_broad_or_stale_edge`；关系只来自同来源或邻近编号。
  - GS-625：`remove_broad_or_stale_edge`；关系只来自同来源或邻近编号。
  - GS-162：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
- 当前快照：`stale`；正式卡 `0225df44761e29e71ac0884d46321f65157ec9730a018b899189c51ad67c056a`；唯一图片 2 个；物理路径 2 个。

### GS-622 57931-2 共轭有理化与半角平方化

- 题目：计算 ∫dx/(1+sin x)。
- 所问：求不定积分
- 知识点：不定积分；一元函数积分学的计算；三角函数有理式；三角恒等变形；半角公式；分母平方化；万能代换；第一类换元；整体凑微分
- 第一动作：先把分母 \(1+\sin x\) 改写成 \((\sin\frac{x}{2}+\cos\frac{x}{2})^2\)。
- 答案：\(\displaystyle -\frac{2}{1+\tan\frac{x}{2}}+C\)
- 个人错因边界：confirmed_personal；没有想到半角公式；没有想到把 \(1\) 写成半角平方和；没有想到分子分母同除 \(\cos^2\frac{x}{2}\)；没有凑出 \(d(\tan\frac{x}{2})\)。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 把 1+sin x 半角化为平方。
  - 同除 cos²(x/2) 并令 u=tan(x/2)。
  - 在定义域连通区间内解释坐标表达式。
- 关系裁决：
  - GS-624：`verify_existing_strong_edge`；共享半角平方化到正切半角换元的明确动作链。
  - GS-623：`remove_broad_or_stale_edge`；关系只来自同来源或邻近编号。
  - GS-625：`remove_broad_or_stale_edge`；关系只来自同来源或邻近编号。
  - GS-630：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-632：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-681：`remove_broad_or_stale_edge`；只共享单个恒等式，不能支撑普通强边。
- 当前快照：`stale`；正式卡 `9116a15bba897ec32f410d90e9eecd34f02bcc182d23ba95bcdbe0a41ce5ce55`；唯一图片 2 个；物理路径 2 个。

### GS-623 57931-3 分母整体线性拆分

- 题目：计算 ∫sin x/(sin x+cos x) dx。
- 所问：求不定积分
- 知识点：不定积分；一元函数积分学的计算；三角函数有理式；分母整体法；分子线性拆分；第一类换元；整体凑微分；对数型积分
- 第一动作：先算 \(F'(x)=\cos x-\sin x\)，再设 \(\sin x=A(\cos x-\sin x)+B(\sin x+\cos x)\) 并比较系数。
- 答案：\(\displaystyle \frac12x-\frac12\ln|\sin x+\cos x|+C\)
- 个人错因边界：confirmed_personal；没有把分母看成整体；没有主动用分母导数参与拆分分子；因此没有触发 \(\int\frac{F'(x)}{F(x)}dx=\ln|F(x)|\)。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 令 F=sin x+cos x 并计算 F′。
  - 把分子写成 AF′+BF。
  - 分别积分为线性项与 ln|F|。
- 关系裁决：
  - GS-266：`add_verified_strong_edge`；分母整体、分母导数与分子线性拆分为同一首动作。
  - GS-624：`remove_broad_or_stale_edge`；关系只来自同来源或邻近编号。
  - GS-625：`remove_broad_or_stale_edge`；关系只来自同来源或邻近编号。
  - GS-630：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-632：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-162：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
- 当前快照：`stale`；正式卡 `f79682d695f0ddc1133420218b29586be8f00aea3ac0a8eb53e7762c6dce877e`；唯一图片 2 个；物理路径 2 个。

### GS-624 57931-5 倍角半角万能代换

- 题目：计算 ∫dx/(sin 2x+2sin x)。
- 所问：求不定积分
- 知识点：不定积分；一元函数积分学的计算；三角函数有理式；三角恒等变形；二倍角公式；半角公式；万能代换；第一类换元；整体凑微分
- 第一动作：先将 \(\sin2x\) 写成 \(2\sin x\cos x\)，把分母化为 \(2\sin x(1+\cos x)\)。
- 答案：\(\displaystyle \frac14\ln\left|\tan\frac{x}{2}\right|+\frac18\tan^2\frac{x}{2}+C\)
- 个人错因边界：confirmed_personal；没有想到倍角展开；没有提公因式；没有把 \(1+\cos x\) 半角化；没有触发 \(t=\tan\frac{x}{2}\) 的万能代换。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 先展开 sin 2x 并提取 2sin x。
  - 对 1+cos x 使用半角公式。
  - 令 t=tan(x/2) 化为有理积分。
- 关系裁决：
  - GS-625：`remove_broad_or_stale_edge`；关系只来自同来源或邻近编号。
  - GS-162：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-681：`remove_broad_or_stale_edge`；只共享单个恒等式，不能支撑普通强边。
- 当前快照：`stale`；正式卡 `63c642271ddfc95ebfaf40f9603250884e8a1643d5a8904fbc5bdcee584df631`；唯一图片 2 个；物理路径 2 个。

### GS-625 57931-6 参数退化三角凑微分

- 题目：在 a²+b²>0 下计算 ∫dx/(a²sin²x+b²cos²x)。
- 所问：求不定积分
- 知识点：不定积分；一元函数积分学的计算；三角函数有理式；参数分类讨论；参数退化讨论；第一类换元；整体凑微分；提公因式凑微分；反正切型积分
- 第一动作：先由 \(a^2+b^2>0\) 判断 \((a,b)\ne(0,0)\)，再列出 \(a=0,b\ne0\)、\(a\ne0,b=0\)、\(a\ne0,b\ne0\) 三种情况。
- 答案：\(\displaystyle \begin{cases}\frac{1}{b^2}\tan x+C, & a=0,\ b\ne0,\\ -\frac{1}{a^2}\cot x+C, & a\ne0,\ b=0,\\ \frac{1}{ab}\arctan\!\left(\frac{a}{b}\tan x\right)+C, & a\ne0,\ b\ne0.\end{cases}\)
- 个人错因边界：confirmed_personal；默认 \(a,b\ne0\)，没有分情况；非零情况没有提取 \(b^2\cos^2x\) 来制造 \(\sec^2x\,dx=d(\tan x)\)。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 先按 a、b 是否为零分三支。
  - 非零支提取 b²cos²x。
  - 令 u=(a/b)tan x，并按图册区间调整常数。
- 当前快照：`stale`；正式卡 `c6dc6001b533289ec251cfeeef34ad1973ef55a6616b77d145c2c68f8fb8e5a6`；唯一图片 2 个；物理路径 2 个。

### GS-630 57979-3 分母平方凑微分分部

- 题目：计算 ∫x²e^x/(x+2)² dx。
- 所问：求不定积分
- 知识点：不定积分；一元函数积分学的计算；分部积分；第一类换元；整体凑微分；分母平方凑微分；分部积分降幂
- 第一动作：先计算 \((x^2e^x)'\)，观察结果是否含有 \((x+2)\)。
- 答案：\(\displaystyle -\frac{x^2e^x}{x+2}+xe^x-e^x+C\)
- 个人错因边界：confirmed_personal；没有先检查分子求导后的结构，导致没发现分部积分后可以约掉一个 \((x+2)\)。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 识别 dx/(x+2)²=-d(1/(x+2))。
  - 分部积分并利用 (x²e^x)′ 含 x+2。
  - 约去一次分母并收口。
- 关系裁决：
  - GS-686：`verify_existing_strong_edge`；分母平方对应负倒数微分，再用分部积分降幂。
  - GS-631：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-632：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-684：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
- 当前快照：`stale`；正式卡 `ed2ce2cc54ac8681b96c0e4b95fe0a00c9865cd0135eb4b7d56c8d7d47a1be45`；唯一图片 2 个；物理路径 2 个。

### GS-631 57979-5 根式换元反解部分分式

- 题目：计算 ∫x⁻²√[(1-x)/(1+x)] dx。
- 所问：求不定积分
- 知识点：不定积分；一元函数积分学的计算；根式积分；第二类换元；根式换元；根式整体换元；换元后反解原变量；有理函数积分；部分分式；复合函数求导；对数型积分
- 第一动作：先令 \(t=\sqrt{\frac{1-x}{1+x}}\)，平方后写 \(t^2(1+x)=1-x\) 并反解 \(x\)。
- 答案：\(\displaystyle -\frac{\sqrt{1-x^2}}{x}+\ln\left|\frac{\sqrt{1+x}+\sqrt{1-x}}{\sqrt{1+x}-\sqrt{1-x}}\right|+C\)
- 个人错因边界：confirmed_personal；没有稳定触发根式整体换元；根号套分式求导漏外层根号因子；从 \(t^2(1+x)=1-x\) 反解 \(x\) 时没有把含 \(x\) 项集中并提取 \(x\)；部分分式中混淆不可约二次因式和重复一次因式；对 \(\arctan x\) 的导数与积分方向曾混淆。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 令 t=√[(1-x)/(1+x)]。
  - 平方后反解 x 并求 dx。
  - 化为有理函数、部分分式并回代。
- 质量发现：
  - `same_event_action_gaps_not_counted_as_recurrences`：同一 2026-06-26 事件中的四个动作断点不能计为四次复发；repeat_count 已归一为 1。；建议：
- 关系裁决：
  - GS-270：`add_verified_strong_edge`；共享完整根式换元、反解原变量和转部分分式。
  - GS-632：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
  - GS-162：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
- 当前快照：`stale`；正式卡 `474f491d78549155819ac83ecbf8f59163bb4003b81d4924a40c8471e752a53a`；唯一图片 2 个；物理路径 2 个。

### GS-632 57979-6 平方展开分部抵消

- 题目：计算 ∫e^(2x)(1+tan x)² dx。
- 所问：求不定积分
- 知识点：不定积分；一元函数积分学的计算；三角函数有理式；三角恒等变形；三角拆项积分；第一类换元；整体凑微分；分部积分
- 第一动作：先展开 \((1+\tan x)^2\)，并用 \(1+\tan^2x=\sec^2x\) 整理成 \(e^{2x}\sec^2x+2e^{2x}\tan x\)。
- 答案：\(\displaystyle e^{2x}\tan x+C\)
- 个人错因边界：confirmed_personal；没有把整理后的两项拆成两个积分分别处理，也没有继续把 \(\int e^{2x}\sec^2x\,dx\) 写成 \(\int e^{2x}\,d(\tan x)\) 做分部积分观察抵消。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 展开平方并用 1+tan²x=sec²x。
  - 把 sec²x 项写成 d(tan x) 做分部积分。
  - 与剩余 tan x 项精确抵消。
- 关系裁决：
  - GS-710：`verify_existing_strong_edge`；B2 已验证保护边：拆项、并排分部积分和残余项精确抵消。
  - GS-076：`remove_broad_or_stale_edge`；只共享上位主题，不能支撑普通强边。
  - GS-684：`remove_broad_or_stale_edge`；只共享方法名称，具体对象、第一动作或收口目标不同。
- 当前快照：`stale`；正式卡 `1253acbb919d4d142684b3b742527ce5039b55c55bd2823b536030a9d597547a`；唯一图片 2 个；物理路径 2 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
