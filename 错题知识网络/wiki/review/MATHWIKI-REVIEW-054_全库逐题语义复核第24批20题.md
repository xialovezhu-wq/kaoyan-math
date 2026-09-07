---
wiki_id: MATHWIKI-REVIEW-054
type: target_level_semantic_review_batch
title: 全库逐题语义复核第24批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-054_全库逐题语义复核第24批20题.json
status: active
last_updated: 2026-07-23
---

# 全库逐题语义复核第24批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 0 张；覆盖 23 个物理图片路径与 15 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 17 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `MATH-TARGET-SEMANTIC-CLOSEOUT-20260723-B24`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-322](http://127.0.0.1:8765/open/GS-322) | 定积分符号判断 | 定积分、定积分性质、定积分等式、极限与连续、截断正弦积分 | $I>0$，选 A。 | pending_user_confirmation：旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先作区间再现，把原积分化为截断的 \(\sin x/x\) 型，再配对正负波瓣判号。 | duplicate_identity_hold |
| [GS-323](http://127.0.0.1:8765/open/GS-323) | 变上限积分与分部积分计算 | 定积分、变上限积分、分部积分、定积分换元 | $\frac{e-2}{6}$ | pending_user_confirmation：旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先由变上限定义得到 \(f'(x)\)，再对目标积分分部，把未知的 \(f\) 转成已知的 \(f'\)。 | duplicate_identity_hold |
| [GS-324](http://127.0.0.1:8765/open/GS-324) | 复合导函数分段还原求函数值 | 定积分、牛顿莱布尼茨公式、复合自变量还原、分段函数 | $e-1$ | pending_user_confirmation：旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先把目标写成 \(f(1)-f(0)=\int_0^1f'(t)\,dt\)，再令 \(x=e^t\) 将题设的 \(f'(\ln x)\) 还原成 \(f'(t)\)。 | duplicate_identity_hold |
| [GS-325](http://127.0.0.1:8765/open/GS-325) | 振荡积分分部估计 | 定积分、一元函数积分学的计算、分部积分、定积分性质 | 当 $x>0$ 时，$\left\|\int_x^{x+1}\sin u^2du\right\|\le\frac1x$。 | pending_user_confirmation：复做入口：看到 $\sin u^2$ 的振荡积分估计，先把 $\sin u^2du$ 改写成 $-\frac1{2u}d(\cos u^2)$，再分部积分估计边界项和余项。 | duplicate_identity_hold |
| [GS-326](http://127.0.0.1:8765/open/GS-326) | 积分型问题 | 定积分、定积分性质、函数奇偶性、对称换元、平移变换 | $$ \boxed{0} $$ | pending_user_confirmation：个人原始错因未记录；当前复做检查点是能否先将积分换元为关于 (a) 对称的区间，再使用图像关于 ((a,0)) 中心对称所对应的奇对称性质。 | — |
| [GS-327](http://127.0.0.1:8765/open/GS-327) | 定积分计算 | 定积分、定积分等式、定积分性质、根式积分 | $4\pi$ | pending_user_confirmation：旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先令 $t=x-2$，把根式配成 $\sqrt{4-t^2}$ 并把区间平移为 $[-2,2]$，再用奇偶性与半圆面积计算。 | duplicate_identity_hold |
| [GS-328](http://127.0.0.1:8765/open/GS-328) | 定积分符号判断 | 定积分、定积分性质、定积分等式、极限与连续、截断正弦积分 | $I>0$，选 A（恒正） | pending_user_confirmation：旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先作区间再现，把原积分化为截断的 $\sin x/x$ 型，再配对正负波瓣判号。 | duplicate_identity_hold |
| [GS-329](http://127.0.0.1:8765/open/GS-329) | 定积分分部积分计算 | 定积分、分部积分、第一类换元 | $\frac16-\frac14\ln 3$ | pending_user_confirmation：暂无明确个人错因；复做入口是先把 $g^{\prime}(2x)$ 的链式系数处理清楚，再对 $t g^{\prime}(t)$ 分部积分。 | — |
| [GS-330](http://127.0.0.1:8765/open/GS-330) | 变上限积分与分部积分计算 | 定积分、变上限积分、分部积分、定积分换元 | $\frac{e-2}{6}$ | pending_user_confirmation：旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先由变上限定义得到 $f^{\prime}(x)$，再对目标积分分部，把未知的 $f$ 转成已知的 $f^{\prime}$。 | duplicate_identity_hold |
| [GS-331](http://127.0.0.1:8765/open/GS-331) | 振荡积分估计 | 定积分、定积分性质、变上限积分、振荡积分估计、第二类换元、分部积分、定积分不等式 | \(x>0\) 时，\(\|f(x)\|\le \frac1x\) | user_confirmed：没有识别 \(\sin u^2\) 这类“变量平方在函数内部”的复合振荡积分应先整体换元 \(t=u^2\)，把相位化成普通 \(\sin t\) 后再分部积分；直接用 \(\|\sin u^2\|\le1\) 只能得到区间长度级估计，达不到 \(\|f(x)\|\le 1/x\)。 | same_card_visual_aliases |
| [GS-332](http://127.0.0.1:8765/open/GS-332) | 定积分等式证明 | 定积分、变上限积分、分部积分、第一类换元 | 等式成立，积分值为 $1-\sin 1$ | pending_user_confirmation：暂无明确个人错因；复做入口是内层积分上下限都依赖 $x$ 时，先设变限函数并用分部积分把外层积分转为 $xG^{\prime}(x)$。 | duplicate_identity_hold |
| [GS-333](http://127.0.0.1:8765/open/GS-333) | 定积分不等式证明 | 定积分、定积分性质、分部积分 | $\int_a^b x f(x)\,dx\le\int_a^b x g(x)\,dx$ | pending_user_confirmation：暂无明确个人错因；复做入口是前缀积分比较题先构造原函数 $F,G$，再用分部积分把 $\int xf$ 转成边界项减 $\int F$。 | duplicate_identity_hold |
| [GS-334](http://127.0.0.1:8765/open/GS-334) | 积分零点存在性证明 | 定积分、分部积分、零点定理 | 存在 $\xi\in(0,1)$，使 $\int_0^\xi f(x)\,dx=0$ | pending_user_confirmation：暂无明确个人错因；复做入口是同时出现裸积分和带权积分时，先设原函数 $F$ 并对带权积分分部，把条件转成 $\int xF(x)dx=0$。 | duplicate_identity_hold |
| [GS-335](http://127.0.0.1:8765/open/GS-335) | 复合导函数分段还原求函数值 | 定积分、牛顿莱布尼茨公式、复合自变量还原、分段函数 | $e-1$ | pending_user_confirmation：旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先把目标写成 $f(1)-f(0)=\int_0^1f'(t)\,dt$，再令 $x=e^t$ 将题设的 $f'(\ln x)$ 还原成 $f'(t)$。 | duplicate_identity_hold |
| [GS-336](http://127.0.0.1:8765/open/GS-336) | 定积分等式证明 | 定积分、变上限积分、分部积分、第一类换元 | 等式成立，积分值为 $1-\sin 1$ | pending_user_confirmation：个人原始错因未记录；当前复做入口是内层积分上下限都依赖 $x$ 时，先设变限函数并用分部积分把外层积分转为 $xG^{\prime}(x)$。 | duplicate_identity_hold |
| [GS-337](http://127.0.0.1:8765/open/GS-337) | 定积分不等式证明 | 定积分、定积分性质 | 不等式成立：$\int_a^b f^2(x)dx\le\frac{(b-a)^2}{2}\int_a^b[f^{\prime}(x)]^2dx$ | pending_user_confirmation：暂无明确个人错因；复做入口是目标含 $f^2$ 与 $(f^{\prime})^2$ 时，先用 $f(a)=0$ 把 $f(x)$ 还原为导数积分，再套积分型柯西不等式。 | duplicate_identity_hold |
| [GS-338](http://127.0.0.1:8765/open/GS-338) | 含参积分函数求导与导数连续性证明 | 定积分、含参定积分、第一类换元、变限积分、导数定义、极限与连续、洛必达法则 | g'(x)=\\frac{x f(x)-\\int_0^x f(u)\\,du}{x^2}\\ (x\\ne0),\\quad g'(0)=\\frac12，且 g'(x) 在 x=0 处连续。 | pending_user_confirmation：暂无明确个人错因；复做入口是先把含参积分中的积分变量换元，化成变上限积分函数，再分别处理 x≠0 与 x=0。 | — |
| [GS-339](http://127.0.0.1:8765/open/GS-339) | 定积分不等式求函数 | 定积分、定积分性质 | $f(x)\equiv x^2,\ 0\le x\le1$ | pending_user_confirmation：暂无明确个人错因；复做入口是看到 $\int f^2$、$\int 2x^2f$ 和常数项，先把常数写成 $\int x^4dx$，再凑完全平方。 | duplicate_identity_hold |
| [GS-340](http://127.0.0.1:8765/open/GS-340) | 定积分不等式证明 | 定积分、定积分性质、分部积分 | $\int_a^b x f(x)\,dx\le\int_a^b x g(x)\,dx$ | pending_user_confirmation：个人原始错因未记录；当前复做入口是前缀积分比较题先构造原函数 $F,G$，再用分部积分把 $\int xf$ 转成边界项减 $\int F$。 | duplicate_identity_hold |
| [GS-341](http://127.0.0.1:8765/open/GS-341) | 题面待恢复（source/visual ambiguity hold） | 定积分（仅按来源目录暂存）、题面待恢复 | 待核对；旧卡中的 \frac1x 来自错位解析，已排除为本题证据。 | pending_user_confirmation：个人原始错因未记录；当前题面证据发生来源与视觉身份冲突，必须先恢复正确的高数题面，不能沿用 GS-331 的振荡积分解析。 | source_visual_mismatch_held、formal_question_visual_gap |

## 逐题复核

### GS-322 强化例题11.13（判断定积分的正负）-2

- 题目：设

$$
I=\int_0^{3\pi/2}\frac{\cos x}{2x-3\pi}\,dx.
$$

判断 $I$ 恒正、恒负、存在零点还是发散；选项依次为 A、B、C、D。本卡与 GS-314、GS-328 为同题身份冻结组成员。
- 所问：定积分符号判断
- 知识点：定积分；定积分性质；定积分等式；极限与连续；截断正弦积分
- 第一动作：先作区间再现 x 替换为 3pi/2-x
- 答案：$I>0$，选 A。
- 个人错因边界：pending_user_confirmation；旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先作区间再现，把原积分化为截断的 \(\sin x/x\) 型，再配对正负波瓣判号。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 用区间再现把分式化成易判号标准核
- 质量发现：
  - `duplicate_identity_hold`：GS-314、GS-322、GS-328 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 当前快照：`stale`；正式卡 `ad1ce7d7cce3392defa603bae916567eeeeaf7da281043c2cc61fb4cca94cabc`；唯一图片 1 个；物理路径 1 个。

### GS-323 强化例题11.15

- 题目：设

$$
f(x)=\int_0^x e^{-t^2+2t}\,dt,
$$

求

$$
\int_0^1(x-1)^2f(x)\,dx.
$$
- 所问：变上限积分与分部积分计算
- 知识点：定积分；变上限积分；分部积分；定积分换元
- 第一动作：先对含 f 的定积分做分部积分
- 答案：$\frac{e-2}{6}$
- 个人错因边界：pending_user_confirmation；旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先由变上限定义得到 \(f'(x)\)，再对目标积分分部，把未知的 \(f\) 转成已知的 \(f'\)。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 定积分分部，把未知 f 转成已知的 f'
- 质量发现：
  - `duplicate_identity_hold`：GS-323、GS-330 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 当前快照：`stale`；正式卡 `c31e3f8382ebda9c767ebfae6cacb7ceaab624b65ef3475736e5ad9ce46bc91b`；唯一图片 1 个；物理路径 1 个。

### GS-324 强化例题11.16

- 题目：已知

$$
f'(\ln x)=
\begin{cases}
1,&x\in(0,1),\\
x,&x\in(1,+\infty),
\end{cases}
\qquad f(0)=0,
$$

求 $f(1)$。
- 所问：复合导函数分段还原求函数值
- 知识点：定积分；牛顿莱布尼茨公式；复合自变量还原；分段函数
- 第一动作：先写 f(1)-f(0) 等于 0 到 1 上 f'(t) 的积分
- 答案：$e-1$
- 个人错因边界：pending_user_confirmation；旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先把目标写成 \(f(1)-f(0)=\int_0^1f'(t)\,dt\)，再令 \(x=e^t\) 将题设的 \(f'(\ln x)\) 还原成 \(f'(t)\)。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先把导数自变量记为 t，再令 x=e^t 换元
- 质量发现：
  - `duplicate_identity_hold`：GS-324、GS-335 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 关系裁决：
  - GS-335：`remove_identity_edge`；题面身份已进入同题冻结组；同题身份只保留在 identity 元数据中，不再作为普通知识关系。
- 当前快照：`stale`；正式卡 `03ee20dae8f83d381d3a3261f07f477bd00a04ba0a421b810cec75cc7de8130a`；唯一图片 1 个；物理路径 1 个。

### GS-325 1000题A组11.11

- 题目：证明振荡积分函数 $f(x)=\int_x^{x+1}\sin u^2du$ 在 $x>0$ 时满足 $|f(x)|\le 1/x$。
- 所问：振荡积分分部估计
- 知识点：定积分；一元函数积分学的计算；分部积分；定积分性质
- 第一动作：先把 sin u^2 du 改写为 -1/(2u)d(cos u^2)
- 答案：当 $x>0$ 时，$\left|\int_x^{x+1}\sin u^2du\right|\le\frac1x$。
- 个人错因边界：pending_user_confirmation；复做入口：看到 $\sin u^2$ 的振荡积分估计，先把 $\sin u^2du$ 改写成 $-\frac1{2u}d(\cos u^2)$，再分部积分估计边界项和余项。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 提出相位导数后做分部积分估计
- 质量发现：
  - `duplicate_identity_hold`：GS-044、GS-249、GS-325、GS-343 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 当前快照：`stale`；正式卡 `90fe036058b8a30eb323b2801c9ecf4792d5e0c62bd80d5787fd50ba7e6a221a`；唯一图片 1 个；物理路径 1 个。

### GS-326 58122 2026.5.7

- 题目：设连续函数 $f$ 的图像关于点 $(a,0)$ 中心对称，计算

$$
I=\int_{-c}^{c}f(a-x)\,dx.
$$

令 $t=a-x$ 后，积分区间变为 $[a-c,a+c]$；再利用 $f(2a-t)=-f(t)$ 得 $I=0$。
- 所问：积分型问题
- 知识点：定积分；定积分性质；函数奇偶性；对称换元；平移变换
- 第一动作：先把对称中心平移到原点，重写被积函数并判断整体奇偶性
- 答案：$$ \boxed{0} $$
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；当前复做检查点是能否先将积分换元为关于 (a) 对称的区间，再使用图像关于 ((a,0)) 中心对称所对应的奇对称性质。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先做中心平移或区间再现换元，再用奇偶性简化定积分。
- 关系裁决：
  - GS-577：`verify_existing_strong_edge`；两题都先把积分区间平移到对称中心，再检查完整被积函数的奇偶性；GS-577 还需把多个积分统一到同一基准区间。
  - GS-633：`verify_existing_strong_edge`；两题都先找二次式或区间的对称中心并平移，再用对称区间上的奇偶性简化积分。
  - GS-634：`verify_existing_strong_edge`；两题都必须把非原点对称中心平移到原点，并判断整体被积函数而非局部因子的奇偶性。
- 当前快照：`stale`；正式卡 `4e11fb1c1a38cf9598fe82f2cfbbbe868f1e534d6e6e33aa5051cc8b6d0c7777`；唯一图片 1 个；物理路径 1 个。

### GS-327 强化例题11.12（还原对称性）-2

- 题目：计算

$$
\int_0^4 x\sqrt{4x-x^2}\,dx.
$$
- 所问：定积分计算
- 知识点：定积分；定积分等式；定积分性质；根式积分
- 第一动作：先令 \(t=x-2\)，把 \(4x-x^2\) 改写成 \(4-t^2\) 并同步改上下限
- 答案：$4\pi$
- 个人错因边界：pending_user_confirmation；旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先令 $t=x-2$，把根式配成 $\sqrt{4-t^2}$ 并把区间平移为 $[-2,2]$，再用奇偶性与半圆面积计算。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先配方平移还原对称性，再用奇偶性和半圆面积计算
- 质量发现：
  - `duplicate_identity_hold`：GS-293、GS-327 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 当前快照：`stale`；正式卡 `3ca02ee2031bd6e891430ba6849cf3877ea26b3e66f429e0654d0b9ed441af67`；唯一图片 1 个；物理路径 1 个。

### GS-328 强化例题11.13（判断定积分的正负）-3

- 题目：设

$$
I=\int_0^{3\pi/2}\frac{\cos x}{2x-3\pi}\,dx.
$$

判断 $I$ 恒正、恒负、存在零点还是发散；选项依次为 A、B、C、D。
- 所问：定积分符号判断
- 知识点：定积分；定积分性质；定积分等式；极限与连续；截断正弦积分
- 第一动作：先作 \(x\mapsto \frac{3\pi}{2}-x\)，写出再现后的积分并和原式比较
- 答案：$I>0$，选 A（恒正）
- 个人错因边界：pending_user_confirmation；旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先作区间再现，把原积分化为截断的 $\sin x/x$ 型，再配对正负波瓣判号。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先做区间再现，把积分核转成更容易比较符号的形式
- 质量发现：
  - `duplicate_identity_hold`：GS-314、GS-322、GS-328 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 关系裁决：
  - GS-244：`remove_broad_or_method_mismatched_edge`；GS-328 是截断正弦积分判号，GS-244 是变上限积分零点个数；共同出现定积分不足以支撑强边。
  - GS-671：`remove_broad_or_method_mismatched_edge`；两题虽都涉及积分符号，但一个依赖区间再现后的波瓣配对，另一个依赖对称拆区间与单调比较，第一动作不同。
- 当前快照：`stale`；正式卡 `1488a28695cb2f0ec80f9ea7184373dc5526e2e8981bf8b607d9ae5a89521673`；唯一图片 1 个；物理路径 1 个。

### GS-329 强化例题11.14 定积分的分部积分法

- 题目：已知 $f(x)=xg^{\prime}(2x)$ 且 $g$ 的一个原函数为 $\ln(1+x)$，求 $\int_0^1f(x)dx$。
- 所问：定积分分部积分计算
- 知识点：定积分；分部积分；第一类换元
- 第一动作：先令 \(t=2x\)，把原积分化为 \(\frac14\int_0^2 t g^{\prime}(t)\,dt\)
- 答案：$\frac16-\frac14\ln 3$
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；复做入口是先把 $g^{\prime}(2x)$ 的链式系数处理清楚，再对 $t g^{\prime}(t)$ 分部积分。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先换元处理复合导数系数，再对 \(t g^{\prime}(t)\) 做定积分分部
- 关系裁决：
  - GS-684：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；两题都先处理复合导数的链式系数，再用定积分分部把高阶导数或导函数降阶到题设已知量。
  - GS-685：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；两题都需要先校正复合自变量产生的系数，再通过分部积分把含导数的积分转为函数值与低阶积分。
- 当前快照：`stale`；正式卡 `acf182dc4fa71b61d623ccee12ac76ae73259bf067b861831b21584a6d781332`；唯一图片 1 个；物理路径 1 个。

### GS-330 强化例题11.15-2

- 题目：设

$$
f(x)=\int_0^x e^{-t^2+2t}\,dt,
$$

求

$$
\int_0^1(x-1)^2f(x)\,dx.
$$
- 所问：变上限积分与分部积分计算
- 知识点：定积分；变上限积分；分部积分；定积分换元
- 第一动作：先写出 \(f'(x)\)，再令 \(dv=(x-1)^2dx\) 对含 \(f\) 的积分分部
- 答案：$\frac{e-2}{6}$
- 个人错因边界：pending_user_confirmation；旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先由变上限定义得到 $f^{\prime}(x)$，再对目标积分分部，把未知的 $f$ 转成已知的 $f^{\prime}$。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 用定积分分部把目标中的 \(f\) 转成已知的 \(f'\)
- 质量发现：
  - `duplicate_identity_hold`：GS-323、GS-330 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 当前快照：`stale`；正式卡 `9e09625cb61abed3e885dc4e066ebf14d248daada7d380ce524f4721e7ee680e`；唯一图片 1 个；物理路径 1 个。

### GS-331 167713 振荡积分估计

- 题目：设 \(f(x)=\int_x^{x+1}\sin u^2\,du\)，证明 \(x>0\) 时 \(|f(x)|\le 1/x\)。核心是先令 \(t=u^2\)，再对 \(\int \frac{\sin t}{2\sqrt t}\,dt\) 分部积分并用 \(|\cos t|\le1\) 放缩。
- 所问：振荡积分估计
- 知识点：定积分；定积分性质；变上限积分；振荡积分估计；第二类换元；分部积分；定积分不等式
- 第一动作：先令 t=u^2，把 \sin u^2 的相位改写成 \sin t
- 答案：\(x>0\) 时，\(|f(x)|\le \frac1x\)
- 个人错因边界：user_confirmed；没有识别 \(\sin u^2\) 这类“变量平方在函数内部”的复合振荡积分应先整体换元 \(t=u^2\)，把相位化成普通 \(\sin t\) 后再分部积分；直接用 \(|\sin u^2|\le1\) 只能得到区间长度级估计，达不到 \(|f(x)|\le 1/x\)。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先整体换元把相位化成普通三角函数，再分部积分制造衰减因子。
- 质量发现：
  - `same_card_visual_aliases`：四个物理题图路径的 SHA-256 相同，按同一卡视觉别名只复核一次内容，同时保留全部路径。；建议：
- 关系裁决：
  - GS-341：`remove_misbinding_edge`；GS-341 的高数题面尚未恢复，现有线代图已排除；不得继续承接 GS-331 的振荡积分内容。
  - GS-344：`remove_source_ambiguous_edge`；GS-344 仍处于来源与视觉歧义冻结，不能以旧错位摘要同 GS-331 建立普通强边。
- 当前快照：`stale`；正式卡 `37d325c7cdd553ec93f31919d5ef046055e8f4894f2d89d525975ee60ca60074`；唯一图片 1 个；物理路径 4 个。

### GS-332 1000题B组11.4

- 题目：证明 $\int_0^1(\int_x^{\sqrt{x}}\frac{\sin t}{t}dt)dx=1-\sin1$。
- 所问：定积分等式证明
- 知识点：定积分；变上限积分；分部积分；第一类换元
- 第一动作：先设 \(G(x)=\int_x^{\sqrt{x}}\frac{\sin t}{t}\,dt\)，把外层积分写成 \(\int_0^1G(x)\,dx\)
- 答案：等式成立，积分值为 $1-\sin 1$
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；复做入口是内层积分上下限都依赖 $x$ 时，先设变限函数并用分部积分把外层积分转为 $xG^{\prime}(x)$。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 设变限辅助函数，再用分部积分和莱布尼茨公式处理上下限贡献
- 质量发现：
  - `duplicate_identity_hold`：GS-332、GS-336 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 关系裁决：
  - GS-336：`remove_identity_edge`；题面身份已进入同题冻结组；同题身份只保留在 identity 元数据中，不再作为普通知识关系。
- 当前快照：`stale`；正式卡 `aad1462d24b89a2d674ee7a8c6059463bca6f577c6e0e07183068d92fab4774a`；唯一图片 1 个；物理路径 1 个。

### GS-333 1000题B组11.5

- 题目：由前缀积分 $\int_a^x f\ge\int_a^x g$ 且端点总积分相等，证明带权积分比较。
- 所问：定积分不等式证明
- 知识点：定积分；定积分性质；分部积分
- 第一动作：先设 \(F(x)=\int_a^x f(t)\,dt\)，\(G(x)=\int_a^x g(t)\,dt\)
- 答案：$\int_a^b x f(x)\,dx\le\int_a^b x g(x)\,dx$
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；复做入口是前缀积分比较题先构造原函数 $F,G$，再用分部积分把 $\int xf$ 转成边界项减 $\int F$。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 构造前缀原函数，再用定积分分部把带权积分转成前缀积分比较
- 质量发现：
  - `duplicate_identity_hold`：GS-333、GS-340 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 关系裁决：
  - GS-340：`remove_identity_edge`；题面身份已进入同题冻结组；同题身份只保留在 identity 元数据中，不再作为普通知识关系。
- 当前快照：`stale`；正式卡 `5921ccc6348fe5464dc9ee5da9f79e34fff5c6350e72cf9fc7a27e390e3f9716`；唯一图片 1 个；物理路径 1 个。

### GS-334 1000题B组11.7-2

- 题目：由 $\int_0^1x^2f(x)dx=\int_0^1f(x)dx$ 证明存在内部点使原函数积分为零。
- 所问：积分零点存在性证明
- 知识点：定积分；分部积分；零点定理
- 第一动作：先设 \(F(x)=\int_0^x f(t)\,dt\)，将 \(f\) 改写成 \(F'\)
- 答案：存在 $\xi\in(0,1)$，使 $\int_0^\xi f(x)\,dx=0$
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；复做入口是同时出现裸积分和带权积分时，先设原函数 $F$ 并对带权积分分部，把条件转成 $\int xF(x)dx=0$。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 构造前缀原函数并对带权积分分部，再用连续函数保号反证
- 质量发现：
  - `duplicate_identity_hold`：GS-321、GS-334 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 当前快照：`stale`；正式卡 `1655ab01eab31444a7e42f92570f0fcc0e4b332ee90a62ba7674507a4fdd47c6`；唯一图片 1 个；物理路径 1 个。

### GS-335 强化例题11.16-2

- 题目：已知

$$
f'(\ln x)=
\begin{cases}
1,&x\in(0,1),\\
x,&x\in(1,+\infty),
\end{cases}
\qquad f(0)=0,
$$

求 $f(1)$。
- 所问：复合导函数分段还原求函数值
- 知识点：定积分；牛顿莱布尼茨公式；复合自变量还原；分段函数
- 第一动作：先写 \(f(1)-f(0)=\int_0^1 f'(t)\,dt\)，再令 \(x=e^t\) 建立 \(f'(t)\)
- 答案：$e-1$
- 个人错因边界：pending_user_confirmation；旧卡未保存用户原始作答，个人错因待确认；客观复做入口是先把目标写成 $f(1)-f(0)=\int_0^1f'(t)\,dt$，再令 $x=e^t$ 将题设的 $f'(\ln x)$ 还原成 $f'(t)$。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 用 \(x=e^t\) 把题设中的 \(f'(\ln x)\) 还原成 \(f'(t)\)，再用牛顿莱布尼茨公式
- 质量发现：
  - `duplicate_identity_hold`：GS-324、GS-335 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 关系裁决：
  - GS-336：`remove_broad_or_method_mismatched_edge`；旧边只共享宽泛章节或局部工具，具体对象、条件与第一动作不足以形成可核验的强关系。
- 当前快照：`stale`；正式卡 `15bf517a7dd61b4d15d92282d56ef4bcc72ca40c7c5bf3a9420aa0addc82bb91`；唯一图片 1 个；物理路径 1 个。

### GS-336 1000题B组11.4-2

- 题目：证明 $\int_0^1(\int_x^{\sqrt{x}}\frac{\sin t}{t}dt)dx=1-\sin1$。
- 所问：定积分等式证明
- 知识点：定积分；变上限积分；分部积分；第一类换元
- 第一动作：先设变限辅助函数 G(x) 并写出上下限贡献对应的 G'(x)
- 答案：等式成立，积分值为 $1-\sin 1$
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；当前复做入口是内层积分上下限都依赖 $x$ 时，先设变限函数并用分部积分把外层积分转为 $xG^{\prime}(x)$。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先设变限辅助函数，再用莱布尼茨公式和分部积分把嵌套积分转成可计算结构
- 质量发现：
  - `duplicate_identity_hold`：GS-332、GS-336 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 当前快照：`stale`；正式卡 `6efe39236203b872224e82bc74d9bf1666775cb0801c5a72c96a291ee997b1ae`；唯一图片 1 个；物理路径 1 个。

### GS-337 1000题B组11.6-2

- 题目：由 $f(a)=0$ 证明 $\int_a^bf^2(x)dx$ 与 $\int_a^b[f^{\prime}(x)]^2dx$ 的积分估计。
- 所问：定积分不等式证明
- 知识点：定积分；定积分性质
- 第一动作：先写 \(f(x)=\int_a^x f'(t)\,dt\)
- 答案：不等式成立：$\int_a^b f^2(x)dx\le\frac{(b-a)^2}{2}\int_a^b[f^{\prime}(x)]^2dx$
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；复做入口是目标含 $f^2$ 与 $(f^{\prime})^2$ 时，先用 $f(a)=0$ 把 $f(x)$ 还原为导数积分，再套积分型柯西不等式。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先用牛顿莱布尼茨公式把 \(f(x)\) 还原为导数积分，再用 Cauchy-Schwarz 放缩
- 质量发现：
  - `duplicate_identity_hold`：GS-053、GS-337 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 当前快照：`stale`；正式卡 `ffb3ec4c75424870113f928a19d15c898abafbba1cbdc63a1fe9cfade1ab8ff1`；唯一图片 1 个；物理路径 1 个。

### GS-338 2020年第16题

- 题目：设 $f(x)$ 连续，且 $\lim_{x\to0}\frac{f(x)}{x}=1$。定义
$$
g(x)=\int_0^1 f(xt)\,dt.
$$
求 $g'(x)$，并证明 $g'(x)$ 在 $x=0$ 处连续。
- 所问：含参积分函数求导与导数连续性证明
- 知识点：定积分；含参定积分；第一类换元；变限积分；导数定义；极限与连续；洛必达法则
- 第一动作：先令 \(u=xt\)，把 \(x\ne0\) 时的 \(g(x)\) 改写为 \(\frac1x\int_0^x f(u)\,du\)
- 答案：g'(x)=\\frac{x f(x)-\\int_0^x f(u)\\,du}{x^2}\\ (x\\ne0),\\quad g'(0)=\\frac12，且 g'(x) 在 x=0 处连续。
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；复做入口是先把含参积分中的积分变量换元，化成变上限积分函数，再分别处理 x≠0 与 x=0。
- 一致性：题图—解析 independent_solution_assets_present；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 先分清积分变量和外部参数，换元成变上限积分，再用导数定义处理特殊点
- 关系裁决：
  - GS-678：`verify_existing_strong_edge_and_complete_bidirectional_declaration`；两题都先用换元把函数内部的参数平移或缩放转成积分区间变化，再把特殊点与一般点分开核验。
  - GS-639：`add_specific_strong_edge_bidirectionally`；两题都是含参定积分：先区分积分变量与外部参数并换元成变上限结构，再单独用导数定义检查参数为零的特殊点。
- 当前快照：`stale`；正式卡 `ca5a2da1818fe04d8ece6c602dca9ef027f8aa2566c7a64cd91ce5331fda991b`；唯一图片 2 个；物理路径 2 个。

### GS-339 强化例题11.17 某些特殊的函数值，我们也可以用定积分表示出来-2

- 题目：由定积分不等式反推出连续函数 $f$ 的唯一形式。
- 所问：定积分不等式求函数
- 知识点：定积分；定积分性质
- 第一动作：先写 \(\frac15=\int_0^1x^4\,dx\)
- 答案：$f(x)\equiv x^2,\ 0\le x\le1$
- 个人错因边界：pending_user_confirmation；暂无明确个人错因；复做入口是看到 $\int f^2$、$\int 2x^2f$ 和常数项，先把常数写成 $\int x^4dx$，再凑完全平方。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 把常数项积分化，再凑成非负平方积分并利用等号情形
- 质量发现：
  - `duplicate_identity_hold`：GS-319、GS-339 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 当前快照：`stale`；正式卡 `9dd772c9b0a9d9260c65f5a744ee7c04057dff8e1342fd946f89a50934ff1772`；唯一图片 1 个；物理路径 1 个。

### GS-340 1000题B组11.5-2

- 题目：由前缀积分 $\int_a^x f\ge\int_a^x g$ 且端点总积分相等，证明带权积分比较。
- 所问：定积分不等式证明
- 知识点：定积分；定积分性质；分部积分
- 第一动作：先设 F(x)=∫_a^x f(t)dt 与 G(x)=∫_a^x g(t)dt 并比较 F-G
- 答案：$\int_a^b x f(x)\,dx\le\int_a^b x g(x)\,dx$
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；当前复做入口是前缀积分比较题先构造原函数 $F,G$，再用分部积分把 $\int xf$ 转成边界项减 $\int F$。
- 一致性：题图—解析 question_only_no_independent_solution_asset；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 构造原函数比较，再用分部积分把带权积分转为原函数积分
- 质量发现：
  - `duplicate_identity_hold`：GS-333、GS-340 的题面经图像哈希与数学内容核验为同题；稳定 ID 保留，普通聚合边冻结，个人证据与次数不迁移。；建议：
- 当前快照：`stale`；正式卡 `6a31a6fd52310ce051b193fd8d7144cf727c3b372c1d0558aaf0e0d6af000ea4`；唯一图片 1 个；物理路径 1 个。

### GS-341 1000题A组11.11-3

- 题目：目前只能确认来源定位为“考研数学错题预处理_结构化表.xlsx / 1000题A组11.11-3”，目录暂指向高等数学定积分。真实题面尚未恢复。
- 所问：题面待恢复（source/visual ambiguity hold）
- 知识点：定积分（仅按来源目录暂存）；题面待恢复
- 第一动作：先恢复并核验正确题面；在此之前不执行数学方法推断。
- 答案：待核对；旧卡中的 \frac1x 来自错位解析，已排除为本题证据。
- 个人错因边界：pending_user_confirmation；个人原始错因未记录；当前题面证据发生来源与视觉身份冲突，必须先恢复正确的高数题面，不能沿用 GS-331 的振荡积分解析。
- 一致性：题图—解析 formal_question_visual_missing_after_exclusion；正式卡—图片 mismatch_blocked
- 解析主线：
  - 待题面恢复后确认
- 质量发现：
  - `source_visual_mismatch_held`：现有题图属于 LA-011，且旧高数正文误用了 GS-331 的解析；二者均已排除。；建议：
  - `formal_question_visual_gap`：恢复与来源定位一致的高数题面前，答案、细知识点、方法入口和普通关系均不作确认。；建议：
- 当前快照：`stale`；正式卡 `15240ef748336cd55638ce3b576fa5904d9ae1ea1e0531e253809b30d477cf0a`；唯一图片 0 个；物理路径 0 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
