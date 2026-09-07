---
wiki_id: MATHWIKI-REVIEW-058
type: target_level_semantic_review_batch
title: 全库逐题语义复核第26批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-058_全库逐题语义复核第26批20题.json
status: active
last_updated: 2026-07-23
---

# 全库逐题语义复核第26批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 2 张；覆盖 27 个物理图片路径与 24 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 6 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `MATH-TARGET-SEMANTIC-CLOSEOUT-20260723-B26`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-366](http://127.0.0.1:8765/open/GS-366) | 全微分恰当性判参 | 多元函数微分学、全微分、多元函数偏导 | \boxed{a=2}. | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有先把“是全微分”翻译成 \(M_y=N_x\)。 | duplicate_identity_hold |
| [GS-367](http://127.0.0.1:8765/open/GS-367) | 二元复合函数全微分计算 | 多元函数偏导、全微分、复合函数求导 | dz\\big\|_{(0,\\pi)}=(\\pi-1)\\,dx-dy | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有先拆出内层 \(u\) 并保留 \(\arctan u\) 的外层导数因子 | — |
| [GS-368](http://127.0.0.1:8765/open/GS-368) | 抽象可微函数全微分 | 多元函数微分学、多元函数连续可微、全微分、多元函数偏导、复合函数求导 | \boxed{df(1,1)=dy} | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有先把两条复合关系转成关于目标点偏导的方程组。 | — |
| [GS-369](http://127.0.0.1:8765/open/GS-369) | 连续与间断判定 | 多元函数微分学、多元函数连续可微、极限与连续 | \boxed{ \frac{\partial f}{\partial x}(0,0)\ \text{不连续},\qquad f(x,y)\ \text{在 }(0,0)\text{可微} } | pending_user_confirmation：缺少用户作答过程；低置信推断可能由偏导不连续直接否定可微，没有回到可微定义 | duplicate_identity_hold |
| [GS-370](http://127.0.0.1:8765/open/GS-370) | 分别连续与联合连续判定 | 多元函数微分学、多元函数连续可微、极限与连续、多元函数极限 | B | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有把分别连续与联合连续拆成两个不同检查对象。 | — |
| [GS-371](http://127.0.0.1:8765/open/GS-371) | 连续性与偏导存在性判定 | 多元函数微分学、多元函数连续可微、多元函数极限、多元函数偏导、极限与连续 | C | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有把连续性与偏导存在性拆开回到各自定义。 | — |
| [GS-372](http://127.0.0.1:8765/open/GS-372) | 连续性与偏导存在性判定 | 多元函数微分学、多元函数连续可微、极限与连续、多元函数极限、多元函数偏导 | (B) | pending_user_confirmation：用户作答过程未记录；低置信推断可能在确认连续后，没有再按偏导定义检查左右极限。 | — |
| [GS-374](http://127.0.0.1:8765/open/GS-374) | 二元复合函数二阶偏导 | 多元函数微分学、多元函数偏导、复合函数求导、多元函数极值 | \(\displaystyle \left.\frac{\partial^2 z}{\partial x\,\partial y}\right\|_{(1,1)}=f_{11}(2,2)+f_2(2,2)f_{12}(1,1)\) | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有先区分外层与内层取值点，并用极值点梯度为零清项。 | — |
| [GS-375](http://127.0.0.1:8765/open/GS-375) | 连续与间断判定 | 多元函数微分学、多元函数连续可微、极限与连续 | \boxed{ \frac{\partial f}{\partial x}(0,0)\ \text{不连续},\qquad f(x,y)\ \text{在 }(0,0)\text{可微} } | pending_user_confirmation：缺少用户作答过程；低置信推断可能由偏导不连续直接否定可微，没有回到可微定义 | duplicate_identity_hold |
| [GS-376](http://127.0.0.1:8765/open/GS-376) | 隐函数求偏导 / 全微分公式理解题 | 多元函数微分学、隐函数求偏导、全微分、偏导数含义 | \(dz=z_xdx+z_ydy\)；本题中 \(dz=\frac{z}{x+z}dx+\frac{z^2}{y(x+z)}dy\)。 | user_confirmed：误以为求出偏导后不需要乘 dx,dy，没有把偏导数和全微分的变化量区分开。 | duplicate_identity_hold |
| [GS-377](http://127.0.0.1:8765/open/GS-377) | 隐函数全微分 | 多元函数微分学、全微分、隐函数求导、多元函数偏导 | \(\displaystyle dz=\frac{z}{x+z}\,dx+\frac{z^2}{y(x+z)}\,dy\) | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有先把隐式方程整体微分并合并所有 \(dz\) 项。 | duplicate_identity_hold、evidence_non_transfer |
| [GS-378](http://127.0.0.1:8765/open/GS-378) | 恰当微分方程初值问题 | 微分方程、多元函数微分学、一阶微分方程、全微分 | \(\displaystyle 2xy-\frac32x^2-\frac52y^2+2=0\) | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有先检查 \(M_y=N_x\) 并转入势函数构造。 | — |
| [GS-379](http://127.0.0.1:8765/open/GS-379) | 全微分恰当性判参 | 多元函数微分学、全微分、多元函数偏导 | \boxed{a=2}. | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有先把“是全微分”翻译成 \(M_y=N_x\)。 | duplicate_identity_hold |
| [GS-380](http://127.0.0.1:8765/open/GS-380) | 二阶偏微分方程变量代换化简求解 | 多元函数偏导、偏微分方程、复合函数求导、二阶偏导、变量代换、一阶线性微分方程 | 由代换可得 \(\frac{\partial^2 z}{\partial u\partial v}=\frac15\frac{\partial z}{\partial u}\)，且 \(z(u,v)=\frac54 e^v+\left(u^2-\frac54\right)e^{v/5}\)。 | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有先把 \(x,y\) 下的偏导整体转写成 \(u,v\) 下的偏导 | — |
| [GS-381](http://127.0.0.1:8765/open/GS-381) | 偏微分方程化简求解 | 多元函数偏导、偏微分方程、复合函数求导、二阶偏导、变量代换 | \(\frac{\partial^2 f}{\partial u\partial v}=\frac1{25}\)，且 \(f(u,v)=\frac{uv}{25}-e^{-u}(u+1)+\frac{v^2}{50}\)。 | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有先把 \(g\) 的一阶和二阶偏导完整写成 \(f_1,f_2,f_{11},f_{12},f_{22}\) | — |
| [GS-382](http://127.0.0.1:8765/open/GS-382) | 偏微分方程化简求解 | 多元函数偏导、偏微分方程、复合函数求导、变量代换、多元函数极值 | \(g_x(x,y)=2(2x-y)e^{-y}\)， \(f(u,v)=(u^2+v^2)e^{-(u+v)}\)； \((0,0)\) 为极小值点，极小值为 \(0\)，\((1,1)\) 不是极值点。 | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有先识别 \(g_x\) 正好对应题设的 \(f_u-f_v\) | — |
| [GS-383](http://127.0.0.1:8765/open/GS-383) | 二阶偏微分方程变量代换求参数 | 多元函数偏导、偏微分方程、复合函数求导、二阶偏导、变量代换、参数退化讨论 | \(a=3\)。 | pending_user_confirmation：用户作答过程未记录；低置信推断可能只看目标形式，没有同时检查多余项消失且 \(z_{uv}\) 系数非零 | — |
| [GS-384](http://127.0.0.1:8765/open/GS-384) | 径向函数拉普拉斯方程求函数 | 多元函数偏导、偏微分方程、复合函数求导、导数定义、二阶偏导、变量代换、极限条件反推导数 | \(f(x)=\frac1{25}e^{5x}-\frac{11}{5}x-\frac1{25}\)。 | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有先固定径向中间变量 \(t\)，而是直接对 \(x,y\) 展开 | — |
| [GS-385](http://127.0.0.1:8765/open/GS-385) | 一阶偏微分方程求函数 | 微分方程、一阶微分方程、多元函数微分学、多元函数偏导、偏微分方程 | \boxed{\,f(x,y)=\bigl(1-\ln\|\cos y\|\bigr)e^{-x}\,.} | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有先固定 \(y\)，把方程视为关于 \(x\) 的一阶方程，并保留任意函数 \(C(y)\)。 | — |
| [GS-387](http://127.0.0.1:8765/open/GS-387) | 多元函数极值最值 | 多元函数极值、多元函数偏导 | \(y=2k\pi\) 时在 \((-e,2k\pi)\) 取极小值，极小值为 \(-e^2/2\)；\(y=(2k+1)\pi\) 时为鞍点，无极大值。 | pending_user_confirmation：用户作答过程未记录；低置信推断可能没有把 \(\sin y=0\) 分成偶数倍和奇数倍 \(\pi\) 后分别代回判别 | — |

## 逐题复核

### GS-366 强化例题13.14

- 题目：微分形式 ((x+ay)dx+y dy)/(x+y)^2 是某个二元函数的全微分，求参数 a。
- 所问：全微分恰当性判参
- 知识点：多元函数微分学；全微分；多元函数偏导
- 第一动作：先写 \(M=\frac{x+ay}{(x+y)^2},\ N=\frac{y}{(x+y)^2}\)，再计算 \(M_y,N_x\)。
- 答案：\boxed{a=2}.
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有先把“是全微分”翻译成 \(M_y=N_x\)。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 抽取 M=(x+ay)/(x+y)^2 与 N=y/(x+y)^2
  - 计算 M_y 与 N_x
  - 由恰当条件 M_y=N_x 比较参数，得 a=2
- 质量发现：
  - `duplicate_identity_hold`：GS-366 belongs to B26-ID-01; stable ID retained and ordinary aggregate edges blocked.；建议：
- 关系裁决：
  - GS-379：`remove`；同题身份组端点不保留普通 related
  - GS-376：`remove`；全微分同章但具体触发和第一动作不同
  - GS-368：`remove`；只有全微分主题相同，恰当条件判参与复合关系反求梯度不构成强边
- 当前快照：`stale`；正式卡 `6b565d19d5104f46d7c1cf4885c7007e999e24443a8d2580ca99cec38c69e7cf`；唯一图片 1 个；物理路径 1 个。

### GS-367 2020年第11题

- 题目：设 z=arctan[xy+sin(x+y)]，求点 (0,π) 处的全微分 dz。
- 所问：二元复合函数全微分计算
- 知识点：多元函数偏导；全微分；复合函数求导
- 第一动作：先设 \(u=xy+\sin(x+y)\)，并写出 \(dz=z_xdx+z_ydy\)
- 答案：dz\\big|_{(0,\\pi)}=(\\pi-1)\\,dx-dy
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有先拆出内层 \(u\) 并保留 \(\arctan u\) 的外层导数因子
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 设 u=xy+sin(x+y)
  - 链式求 z_x、z_y
  - 在 (0,π) 代值
  - 写 dz=z_xdx+z_ydy
- 关系裁决：
  - GS-368：`add`；由显式复合函数全微分递进到两条复合关系反求目标点梯度；共享链式求导后组装全微分的动作链
- 当前快照：`stale`；正式卡 `47f43b86d63c283e8637142998654360525df065fdf90e264076e54a799e6ab2`；唯一图片 2 个；物理路径 2 个。

### GS-368 2021年真题

- 题目：已知 f 可微，且 f(x+1,e^x)=x(x+1)^2、f(x,x^2)=2x^2 ln x，求 df(1,1)。
- 所问：抽象可微函数全微分
- 知识点：多元函数微分学；多元函数连续可微；全微分；多元函数偏导；复合函数求导
- 第一动作：先找使内层点等于 \((1,1)\) 的参数值，再对两条等式分别求导。
- 答案：\boxed{df(1,1)=dy}
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有先把两条复合关系转成关于目标点偏导的方程组。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 第一式在参数 x=0 求导得 f_x+f_y=1
  - 第二式在参数 x=1 求导得 f_x+2f_y=2
  - 解得 f_x=0、f_y=1，再写全微分
- 关系裁决：
  - GS-367：`add`；由显式复合函数全微分递进到两条复合关系反求目标点梯度；共享链式求导后组装全微分的动作链
  - GS-374：`keep`；抽象梯度反求与嵌套复合二阶偏导形成由一阶链式到二阶链式的递进链
  - GS-366：`remove`；只有全微分主题相同，恰当条件判参与复合关系反求梯度不构成强边
  - GS-379：`remove`；身份冻结端点且方法模板不同
  - GS-371：`remove`；仅同属多元微分学，问题对象与首动作不同
- 当前快照：`stale`；正式卡 `9b355ca198e23352dd444921607c30e823365eaa20a6bf029cf66a6133e0bc3d`；唯一图片 1 个；物理路径 1 个。

### GS-369 2024年真题选择题第五题-3

- 题目：分段函数 f=(x^2+y^2)sin(1/(xy))（xy≠0），xy=0 时 f=0；判断 f_x 在原点的连续性与 f 在原点的可微性。
- 所问：连续与间断判定
- 知识点：多元函数微分学；多元函数连续可微；极限与连续
- 第一动作：先用夹逼验证原函数增量为 o(rho)，再另算偏导函数极限判断连续性
- 答案：\boxed{ \frac{\partial f}{\partial x}(0,0)\ \text{不连续},\qquad f(x,y)\ \text{在 }(0,0)\text{可微} }
- 个人错因边界：pending_user_confirmation；缺少用户作答过程；低置信推断可能由偏导不连续直接否定可微，没有回到可微定义
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由 |f|≤x^2+y^2=o(sqrt(x^2+y^2)) 判 f 在原点可微且微分为 0
  - 由定义求 f_x(0,0)=0
  - 另选趋近路径考察 xy≠0 区域的 f_x，判其在原点不连续
- 质量发现：
  - `duplicate_identity_hold`：GS-369 belongs to B25-ID-02; stable ID retained and ordinary aggregate edges blocked.；建议：
- 当前快照：`current`；正式卡 `c80d023e0037c265d9a43d9aeddce240684c28b46ca7cce9c9f89f8685ff974d`；唯一图片 1 个；物理路径 1 个。

### GS-370 强化例题13.7

- 题目：分段函数 f=1（xy=0）、f=0（xy≠0）；判断原点处分别连续性与联合连续性。
- 所问：分别连续与联合连续判定
- 知识点：多元函数微分学；多元函数连续可微；极限与连续；多元函数极限
- 第一动作：先固定 \(y=0\) 或 \(x=0\) 检查单变量连续，再选 \(xy=0\) 与 \(xy\ne0\) 路径比较联合极限。
- 答案：B
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有把分别连续与联合连续拆成两个不同检查对象。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 固定 y=0 或 x=0，所得单变量函数恒为 1，故分别连续
  - 联合趋近时比较 xy=0 与 xy≠0 两类路径，极限值不同
- 关系裁决：
  - GS-371：`keep`；同为原点分段函数，均需把联合极限与坐标轴方向信息分开检查
  - GS-372：`remove`；仅泛化为概念独立性，GS-371 已是两者之间的精确中介
- 当前快照：`stale`；正式卡 `2c00207ad527d43935d3bad2a039c71b1cac065033cf54820d6113c4343730e5`；唯一图片 1 个；物理路径 1 个。

### GS-371 强化例题13.8

- 题目：分段函数 f=xy/(x^2+y^2)（非原点）、f(0,0)=0；判断原点连续性与两个一阶偏导是否存在。
- 所问：连续性与偏导存在性判定
- 知识点：多元函数微分学；多元函数连续可微；多元函数极限；多元函数偏导；极限与连续
- 第一动作：先沿 \(y=kx\) 查极限是否依赖 \(k\)，再用偏导定义沿坐标轴计算。
- 答案：C
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有把连续性与偏导存在性拆开回到各自定义。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 沿 y=kx 得 k/(1+k^2)，路径相关，故不连续
  - 按偏导定义沿两坐标轴计算，两个一阶偏导均为 0
- 关系裁决：
  - GS-372：`keep`；构成偏导存在不推出连续、连续不推出偏导存在的精确双向反例
  - GS-370：`keep`；同为原点分段函数，均需把联合极限与坐标轴方向信息分开检查
  - GS-368：`remove`；仅同属多元微分学，问题对象与首动作不同
- 当前快照：`stale`；正式卡 `7a5b40bf6ba40089db0017148a65578e50c1968609f437b6210322e18d4254c6`；唯一图片 1 个；物理路径 1 个。

### GS-372 强化例题13.9

- 题目：设 g(x,y)=sqrt(x^2+y^2)，判断原点连续性与两个一阶偏导是否存在。
- 所问：连续性与偏导存在性判定
- 知识点：多元函数微分学；多元函数连续可微；极限与连续；多元函数极限；多元函数偏导
- 第一动作：先用 \(\sqrt{x^2+y^2}\to0\) 判断连续，再算 \(g_x(0,0)=\lim_{h\to0}|h|/h\)。
- 答案：(B)
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能在确认连续后，没有再按偏导定义检查左右极限。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 用距离函数趋于 0 判连续
  - 按定义计算 g_x(0,0)=lim |h|/h，左右极限不同
  - g_y 同理不存在
- 关系裁决：
  - GS-371：`keep`；构成偏导存在不推出连续、连续不推出偏导存在的精确双向反例
  - GS-370：`remove`；仅泛化为概念独立性，GS-371 已是两者之间的精确中介
- 当前快照：`stale`；正式卡 `a5264f447825f82711d57c83821f2b2b078948bd602e96c822c415ca935b200f`；唯一图片 1 个；物理路径 1 个。

### GS-374 强化例题13.16

- 题目：f(u,v) 有二阶连续偏导，f(1,1)=2 且 (1,1) 是 f 的极值点；令 z=f(x+y,f(x,y))，求 z_xy(1,1)。
- 所问：二元复合函数二阶偏导
- 知识点：多元函数微分学；多元函数偏导；复合函数求导；多元函数极值
- 第一动作：先设外层变量 \(u=x+y,\ v=f(x,y)\)，写 \(z_x=f_1(u,v)u_x+f_2(u,v)v_x\)。
- 答案：\(\displaystyle \left.\frac{\partial^2 z}{\partial x\,\partial y}\right|_{(1,1)}=f_{11}(2,2)+f_2(2,2)f_{12}(1,1)\)
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有先区分外层与内层取值点，并用极值点梯度为零清项。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 设外层变量 u=x+y、v=f(x,y)，先写一阶链式式
  - 极值点给出内层 f_x(1,1)=f_y(1,1)=0
  - 对 y 再求导并代点，清去含内层一阶偏导的项
- 关系裁决：
  - GS-368：`keep`；抽象梯度反求与嵌套复合二阶偏导形成由一阶链式到二阶链式的递进链
  - GS-465：`remove`；显式嵌套复合二阶偏导与隐函数二阶偏导模板不同
- 当前快照：`stale`；正式卡 `0c134e1ea02a9b03f3b426f3e32d5372fa50f1d1e6976fe01a54e9f96cb10b5b`；唯一图片 1 个；物理路径 1 个。

### GS-375 2024年真题选择题第五题-4

- 题目：与 GS-369 同题同图：分段函数 (x^2+y^2)sin(1/(xy))；判断 f_x 连续性和 f 可微性。
- 所问：连续与间断判定
- 知识点：多元函数微分学；多元函数连续可微；极限与连续
- 第一动作：先用夹逼验证原函数增量为 o(rho)，再另算偏导函数极限判断连续性
- 答案：\boxed{ \frac{\partial f}{\partial x}(0,0)\ \text{不连续},\qquad f(x,y)\ \text{在 }(0,0)\text{可微} }
- 个人错因边界：pending_user_confirmation；缺少用户作答过程；低置信推断可能由偏导不连续直接否定可微，没有回到可微定义
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 同 GS-369：夹逼原函数增量判可微
  - 偏导按定义求点值后另选路径判偏导函数不连续
- 质量发现：
  - `duplicate_identity_hold`：GS-375 belongs to B25-ID-02; stable ID retained and ordinary aggregate edges blocked.；建议：
- 当前快照：`current`；正式卡 `073329a5f0ce97e5578471db233b5e2cc66372fee0bb0ed6b337628268708492`；唯一图片 1 个；物理路径 1 个。

### GS-376 强化例题13.15 隐函数全微分公式

- 题目：隐函数 z=z(x,y) 由 x/z=ln(z/y) 确定，求全微分 dz。
- 所问：隐函数求偏导 / 全微分公式理解题
- 知识点：多元函数微分学；隐函数求偏导；全微分；偏导数含义
- 第一动作：先把 z 明确看成 z(x,y)，对隐函数方程分别求 z_x,z_y。
- 答案：\(dz=z_xdx+z_ydy\)；本题中 \(dz=\frac{z}{x+z}dx+\frac{z^2}{y(x+z)}dy\)。
- 个人错因边界：user_confirmed；误以为求出偏导后不需要乘 dx,dy，没有把偏导数和全微分的变化量区分开。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 把方程视为 F(x,y,z)=0
  - 分别求 z_x、z_y
  - 最后组合 dz=z_xdx+z_ydy
- 质量发现：
  - `duplicate_identity_hold`：GS-376 belongs to B26-ID-02; stable ID retained and ordinary aggregate edges blocked.；建议：
- 关系裁决：
  - GS-366：`remove`；全微分同章但具体触发和第一动作不同
  - GS-465：`remove`；身份冻结端点，且一阶全微分与二阶隐函数偏导首动作不同
  - GS-377：`remove`；同题身份组内不建普通 related
  - GS-379：`remove`；两个身份冻结端点且仅共享全微分标签
- 当前快照：`stale`；正式卡 `d96ebd7e6966129017fbe95724942cfc580837d22a177a9bb041b43bae12b38d`；唯一图片 1 个；物理路径 1 个。

### GS-377 强化例题13.15-2

- 题目：与 GS-376 同题同图：隐函数 x/z=ln(z/y)，求全微分 dz。
- 所问：隐函数全微分
- 知识点：多元函数微分学；全微分；隐函数求导；多元函数偏导
- 第一动作：先改写 \(F=\frac{x}{z}-\ln z+\ln y=0\)，再整体微分并把所有 \(dz\) 项移到一侧。
- 答案：\(\displaystyle dz=\frac{z}{x+z}\,dx+\frac{z^2}{y(x+z)}\,dy\)
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有先把隐式方程整体微分并合并所有 \(dz\) 项。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 改写 F=x/z-ln z+ln y=0
  - 整体微分
  - 把全部 dz 项移到一侧并合并系数后解出 dz
- 质量发现：
  - `duplicate_identity_hold`：GS-377 belongs to B26-ID-02; stable ID retained and ordinary aggregate edges blocked.；建议：
  - `evidence_non_transfer`：GS-376 has explicit user-confirmed evidence, but identical question identity does not authorize copying that evidence to GS-377.；建议：
- 关系裁决：
  - GS-376：`remove`；同题身份组内不建普通 related
  - GS-465：`remove`；身份冻结端点，且整体微分与二阶隐函数求导模板不同
  - GS-378：`remove`；一阶隐函数全微分与恰当微分方程仅表面共享微分形式
- 当前快照：`stale`；正式卡 `1d776a1703d60dac766564c561d9faf958ac10d9d4dea11e70d51cb0d131b470`；唯一图片 1 个；物理路径 1 个。

### GS-378 2025年真题填空题第二题

- 题目：求恰当微分方程 (2y-3x)dx+(2x-5y)dy=0 满足 y(1)=1 的特解。
- 所问：恰当微分方程初值问题
- 知识点：微分方程；多元函数微分学；一阶微分方程；全微分
- 第一动作：先写 \(M=2y-3x,\ N=2x-5y\)，检查 \(M_y=N_x=2\)。
- 答案：\(\displaystyle 2xy-\frac32x^2-\frac52y^2+2=0\)
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有先检查 \(M_y=N_x\) 并转入势函数构造。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 检查 M_y=N_x=2，确认恰当
  - 积分 M 得势函数并由 N 确定 y 项
  - 代入 (1,1) 确定常数
- 关系裁决：
  - GS-377：`remove`；一阶隐函数全微分与恰当微分方程仅表面共享微分形式
  - GS-379：`remove`；身份冻结端点，且恰当方程求势函数与判参模板不同
  - GS-385：`remove`；仅同属微分方程，恰当方程与固定变量解 PDE 的首动作不同
- 当前快照：`stale`；正式卡 `fa0b1e450b86fdd159fe9ecaebb7dd3f467ede84c27d9e0a6410fa3ae34af3d5`；唯一图片 1 个；物理路径 1 个。

### GS-379 强化例题13.14-2

- 题目：与 GS-366 同题同图：给定微分形式是全微分，求参数 a。
- 所问：全微分恰当性判参
- 知识点：多元函数微分学；全微分；多元函数偏导
- 第一动作：先写 \(M=\frac{x+ay}{(x+y)^2},\ N=\frac{y}{(x+y)^2}\)，再计算 \(M_y,N_x\)。
- 答案：\boxed{a=2}.
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有先把“是全微分”翻译成 \(M_y=N_x\)。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 同 GS-366：抽取 M、N
  - 由 M_y=N_x 判定 a=2
- 质量发现：
  - `duplicate_identity_hold`：GS-379 belongs to B26-ID-01; stable ID retained and ordinary aggregate edges blocked.；建议：
- 关系裁决：
  - GS-366：`remove`；同题身份组端点不保留普通 related
  - GS-368：`remove`；身份冻结端点且方法模板不同
  - GS-376：`remove`；两个身份冻结端点且仅共享全微分标签
  - GS-378：`remove`；身份冻结端点，且恰当方程求势函数与判参模板不同
- 当前快照：`stale`；正式卡 `40554ff486eb749d69e89147c0269a6de9a58156145cdf77ff604673389ae2f5`；唯一图片 1 个；物理路径 1 个。

### GS-380 强化例题13.21

- 题目：z=z(u,v)，令 u=x-2y、v=x+3y 后满足 6z_xx+z_xy-z_yy=3z_x-z_y，且 d[z(0,v)]/dv=(1/5)z(0,v)+e^v、z(u,0)=u^2；证明 z_uv=(1/5)z_u 并求 z。
- 所问：二阶偏微分方程变量代换化简求解
- 知识点：多元函数偏导；偏微分方程；复合函数求导；二阶偏导；变量代换；一阶线性微分方程
- 第一动作：先写清 \(u,v\) 与 \(x,y\) 的关系，并求 \(z_x,z_y\)
- 答案：由代换可得 \(\frac{\partial^2 z}{\partial u\partial v}=\frac15\frac{\partial z}{\partial u}\)，且 \(z(u,v)=\frac54 e^v+\left(u^2-\frac54\right)e^{v/5}\)。
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有先把 \(x,y\) 下的偏导整体转写成 \(u,v\) 下的偏导
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 完整链式换元化简原 PDE
  - 令 w=z_u，得到 w_v=w/5
  - 结合 z(u,0)=u^2 传播 u 方向差值
  - 用 z(0,0)=0 解边界一阶线性方程并合并
- 关系裁决：
  - GS-381：`keep`；同为线性变量代换后隔离混合偏导并结合边界条件求解
  - GS-383：`keep`；同为对二阶 PDE 作线性变量变换并控制二阶项系数
  - GS-385：`remove`；仅同属 PDE，线性换元二阶方程与固定变量一阶方程模板不同
- 当前快照：`stale`；正式卡 `a5e276fdd7277c303e5b09f28abbb12afca19d87b4dd79a1be3597ec4e4c915c`；唯一图片 2 个；物理路径 2 个。

### GS-381 2024年真题20题

- 题目：g(x,y)=f(2x+y,3x-y)，且 g_xx+g_xy-6g_yy=1；先求 f_uv，再由 f_u(u,0)=u e^(-u)、f(0,v)=v^2/50-1 求 f。
- 所问：偏微分方程化简求解
- 知识点：多元函数偏导；偏微分方程；复合函数求导；二阶偏导；变量代换
- 第一动作：先设 \(u=2x+y,\ v=3x-y\)，写出 \(g_x,g_y\)
- 答案：\(\frac{\partial^2 f}{\partial u\partial v}=\frac1{25}\)，且 \(f(u,v)=\frac{uv}{25}-e^{-u}(u+1)+\frac{v^2}{50}\)。
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有先把 \(g\) 的一阶和二阶偏导完整写成 \(f_1,f_2,f_{11},f_{12},f_{22}\)
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 设 u=2x+y、v=3x-y，完整展开 g 的一、二阶偏导
  - 题设组合化为 25f_uv=1
  - 积分 f_uv 并用两组边界条件确定两个单变量函数
- 关系裁决：
  - GS-380：`keep`；同为线性变量代换后隔离混合偏导并结合边界条件求解
  - GS-382：`keep`；同为设计复合变量使链式偏导组合匹配题设 PDE
  - GS-383：`keep`；同为线性变量变换后二阶链式系数的系统展开
- 当前快照：`stale`；正式卡 `f869130dbc173a82db5a4abfa5399a54bd9ae5c02f04f5d0ccf4d4a35bd87c1c`；唯一图片 2 个；物理路径 2 个。

### GS-382 2022年真题第20题

- 题目：f_u-f_v=2(u-v)e^(-(u+v))，f(u,0)=u^2e^(-u)；令 g(x,y)=f(x,y-x)，求 g_x、f 的表达式及极值。
- 所问：偏微分方程化简求解
- 知识点：多元函数偏导；偏微分方程；复合函数求导；变量代换；多元函数极值
- 第一动作：先由 \(u=x,\ v=y-x\) 写出 \(g_x=f_u-f_v\)
- 答案：\(g_x(x,y)=2(2x-y)e^{-y}\)， \(f(u,v)=(u^2+v^2)e^{-(u+v)}\)； \((0,0)\) 为极小值点，极小值为 \(0\)，\((1,1)\) 不是极值点。
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有先识别 \(g_x\) 正好对应题设的 \(f_u-f_v\)
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 由复合关系得到 g_x=f_u-f_v 并代题设
  - 对 x 积分求 g，用 g(u,u)=f(u,0) 定积分函数
  - 反代 y=u+v 得 f，再求驻点并用 Hessian 分类
- 关系裁决：
  - GS-381：`keep`；同为设计复合变量使链式偏导组合匹配题设 PDE
  - GS-385：`remove`；仅同属 PDE，复合变量匹配与固定变量分离的触发不同
- 当前快照：`stale`；正式卡 `e4b05555f1674b23ffe174c3ef02a71e166da9b13c5fc5ce780b7f99a4fdf801`；唯一图片 2 个；物理路径 2 个。

### GS-383 强化例题13.22

- 题目：作线性变量变换 u=x-2y、v=x+ay，将 6z_xx+z_xy-z_yy=0 化为 z_uv=0，求 a。
- 所问：二阶偏微分方程变量代换求参数
- 知识点：多元函数偏导；偏微分方程；复合函数求导；二阶偏导；变量代换；参数退化讨论
- 第一动作：先写 \(u_x,u_y,v_x,v_y\)，再展开原方程中的二阶偏导系数
- 答案：\(a=3\)。
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能只看目标形式，没有同时检查多余项消失且 \(z_{uv}\) 系数非零
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 链式展开得 (5a+10)z_uv+(6+a-a^2)z_vv=0
  - 令 z_vv 系数为 0 且要求 z_uv 系数非零
  - 候选 a=3、-2 中排除退化的 -2
- 关系裁决：
  - GS-380：`keep`；同为对二阶 PDE 作线性变量变换并控制二阶项系数
  - GS-381：`keep`；同为线性变量变换后二阶链式系数的系统展开
- 当前快照：`stale`；正式卡 `1d2eaa6a082d1a25f0410ba8517c0eef73a0102797eb6e0c320477ed8e9db598`；唯一图片 2 个；物理路径 2 个。

### GS-384 强化例题13.23

- 题目：u=f(ln sqrt(x^2+y^2)) 满足 u_xx+u_yy=(x^2+y^2)^(3/2)，且 lim[x→0](∫_0^1 f(xt)dt)/x=-1，求 f。
- 所问：径向函数拉普拉斯方程求函数
- 知识点：多元函数偏导；偏微分方程；复合函数求导；导数定义；二阶偏导；变量代换；极限条件反推导数
- 第一动作：先设 \(t=\ln\sqrt{x^2+y^2}\)
- 答案：\(f(x)=\frac1{25}e^{5x}-\frac{11}{5}x-\frac1{25}\)。
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有先固定径向中间变量 \(t\)，而是直接对 \(x,y\) 展开
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 设径向变量 s=ln r，把拉普拉斯项化为 e^(-2s)f''(s)
  - 得到 f''(s)=e^(5s) 并积分两次
  - 由积分极限的有限性和值分别推出 f(0)=0、f'(0)=-2，确定常数
- 关系裁决：
  - GS-458：`add`；共享把极限改写为导数定义以反推点值与导数的具体入口
- 当前快照：`stale`；正式卡 `0a841195171d57525dbc2c719779e14c495df5781e1dd761a4d73a3b602fdeac`；唯一图片 2 个；物理路径 2 个。

### GS-385 强化例题13.24

- 题目：正值 C1 函数满足 f_x+f=0、f_y(0,y)=tan y、f(0,0)=1，求 f(x,y)。
- 所问：一阶偏微分方程求函数
- 知识点：微分方程；一阶微分方程；多元函数微分学；多元函数偏导；偏微分方程
- 第一动作：先由 \(f_x=-f\) 写出 \(f(x,y)=C(y)e^{-x}\)。
- 答案：\boxed{\,f(x,y)=\bigl(1-\ln|\cos y|\bigr)e^{-x}\,.}
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有先固定 \(y\)，把方程视为关于 \(x\) 的一阶方程，并保留任意函数 \(C(y)\)。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 固定 y 解关于 x 的一阶方程，得 f=C(y)e^(-x)
  - 由边界导数得 C'(y)=tan y
  - 积分并用 C(0)=1 定常数
- 关系裁决：
  - GS-378：`remove`；仅同属微分方程，恰当方程与固定变量解 PDE 的首动作不同
  - GS-380：`remove`；仅同属 PDE，线性换元二阶方程与固定变量一阶方程模板不同
  - GS-382：`remove`；仅同属 PDE，复合变量匹配与固定变量分离的触发不同
- 当前快照：`stale`；正式卡 `ee49f9d1d6873573c38da16ab9beaffd9f640f4be7ba5491b82395c7824cfa01`；唯一图片 1 个；物理路径 1 个。

### GS-387 2023年真题第18题

- 题目：求 f(x,y)=x e^(cos y)+x^2/2 的极值。
- 所问：多元函数极值最值
- 知识点：多元函数极值；多元函数偏导
- 第一动作：先联立 \(f_x=0,\ f_y=0\)，求出全部驻点
- 答案：\(y=2k\pi\) 时在 \((-e,2k\pi)\) 取极小值，极小值为 \(-e^2/2\)；\(y=(2k+1)\pi\) 时为鞍点，无极大值。
- 个人错因边界：pending_user_confirmation；用户作答过程未记录；低置信推断可能没有把 \(\sin y=0\) 分成偶数倍和奇数倍 \(\pi\) 后分别代回判别
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_documented_repairs
- 解析主线：
  - 联立 f_x=0、f_y=0 求出两类驻点
  - 分别代入 Hessian 判别
  - 偶数倍 π 为极小点，奇数倍 π 为鞍点
- 关系裁决：
  - GS-388：`keep`；同为多驻点极值题，首动作是求全驻点并逐点 Hessian 判别
  - GS-389：`keep`；同为无条件二元极值题，需完整求驻点并排除非极值点
  - GS-390：`keep`；同为多驻点极值题，需把极小点与鞍点逐一分类
- 当前快照：`stale`；正式卡 `07a3331ca0e557744745543f0bf49473592b2f70c047f0101197823448a0e723`；唯一图片 2 个；物理路径 2 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
