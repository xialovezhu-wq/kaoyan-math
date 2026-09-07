---
wiki_id: MATHWIKI-REVIEW-082
type: target_level_semantic_review_batch
title: 全库逐题语义复核第38批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-082_全库逐题语义复核第38批20题.json
status: active
last_updated: 2026-07-25
---

# 全库逐题语义复核第38批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 7 张；覆盖 39 个物理图片路径与 24 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 8 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `MATHWIKI-REVIEW-083`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-662](http://127.0.0.1:8765/open/GS-662) | 复合三角函数定积分大小比较 | 定积分、积分保序、函数单调性、三角不等式、复合函数点态比较 | A。由 \(0<\sin x<x<\frac\pi2\)，得 \(\sin(\sin x)<\sin x\)，故 \(I_1<1\)；又因 \(\cos x\) 在 \([0,\frac\pi2]\) 上递减，\(\sin x<x\) 推出 \(\cos(\sin x)>\cos x\)，故 \(I_2>1\)。所以 \(I_1<1<I_2\)。 | user_confirmed：没有从复合三角函数比较题中触发“引入 \\(x\\) 作中间量”的动作，而是持续尝试换元，把问题带到 \\(\\arcsin t\\) 的复杂路径。 | b38_source_literal_repair_gs_662 |
| [GS-663](http://127.0.0.1:8765/open/GS-663) | 三个定积分大小排序 | 定积分、作差法、倒数比较方向、变号区间分段、对称换元、区间再现 | A。先由 \((1+x)^2>1+x^2\) 且 \(\sin x>0\) 得 \(I_2>I_3\)。再作差 \(I_1-I_2=\int_0^{\pi/2}\frac{\cos x-\sin x}{1+x^2}dx\)，把后半段用 \(x\mapsto \frac\pi2-x\) 反折到 \((0,\frac\pi4)\)，得到正 integrand，故 \(I_1>I_2\)。综上 \(I_1>I_2>I_3\)。 | user_confirmed：有作差意识但没有把 \\(I_1-I_2\\) 落地；比较分母时忘记倒数不等号反向；反折换元时把 \\(\\frac\\pi2-\\frac\\pi4\\) 算成负数。 | b38_source_literal_repair_gs_663 |
| [GS-664](http://127.0.0.1:8765/open/GS-664) | 导函数符号与凹函数弦线积分比较选择题 | 变上限积分、导数判单调、二阶导数判凹凸、凹函数端点弦线、积分面积比较 | C。由 \(F'(x)=f(x)>0\)、\(F''(x)=f'(x)<0\)、\(F(0)=0\)，可知 \(F\) 在 \([0,1]\) 上递增且为凹函数。凹函数图像在端点弦线 \(y=xF(1)\) 上方，所以 \(F(x)>xF(1)\)。积分得 \(\int_0^1F(x)\,dx>\frac12F(1)\)，即 \(F(1)<2\int_0^1F(x)\,dx\)。又 \(0<x<1\) 时 \(F(x)<F(1)\)，故 \(F(x)<2\int_0^1F(x)\,dx\)。 | user_confirmed：没有从 \\(F'\\) 与 \\(F''\\) 的符号触发凹函数弦线图像比较；转而构造 \\(g(x)\\) 后，又把全区间积分常数在 \\(x=0\\) 处误消成 0。 | b38_false_F_prime_mismatch_withdrawn |
| [GS-665](http://127.0.0.1:8765/open/GS-665) | 凸函数条件下加权定积分比较选择题 | 凸函数、加权定积分不等式、变上限辅助函数、拉格朗日中值定理、二阶导数判号 | B。令 \(F(t)=\int_0^t x f(x)\,dx-\frac23t\int_0^t f(x)\,dx\)。则 \(F'(t)=\frac13t f(t)-\frac23\int_0^t f(x)\,dx,\ F'(0)=0\)，且 \(F''(t)=\frac13t f'(t)-\frac13f(t)\)。由拉格朗日中值定理，\(f(t)-f(0)=t f'(\xi)\)，其中 \(0<\xi<t\)；又 \(f''>0\)，故 \(f'(t)>f'(\xi)\)，所以 \(F''(t)=\frac13t[f'(t)-f'(\xi)]>0\)。于是 \(F'(t)>0,\ F(t)>0\)，取 \(t=a\) 得 \(\int_0^a x f(x)\,dx>\frac23a\int_0^a f(x)\,dx\)，即 \(3\int_0^a x f(x)\,dx>2a\int_0^a f(x)\,dx\)，选 B。 | user_confirmed：没有先围绕选项目标构造变上限差值辅助函数；转而使用凸函数弦线和 Taylor 的点态比较，后续卡在带权积分整体符号比较。 | — |
| [LA-001](http://127.0.0.1:8765/open/LA-001) | 行列式计算 | 行列式、行列式对一行的线性性、初等列变换、按行展开 | 10(a-3) | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | b38_complete_question_la_001、b38_method_gap_consistency_la_001 |
| [LA-002](http://127.0.0.1:8765/open/LA-002) | 行列式函数零点个数判断 | 行列式、列变换、行列式对一列的线性性、含参行列式多项式次数 | \boxed{f(x)=0\text{ 至多有一个零点}} | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | — |
| [LA-004](http://127.0.0.1:8765/open/LA-004) | 隐函数方程组求导 | 隐函数方程组、多元函数求导、点值代入、联立线性方程 | \boxed{\left.\frac{dz}{dx}\right\|_{x=\frac12}=-4} | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | b38_cross_subject_identity_hold_la_004 |
| [LA-005](http://127.0.0.1:8765/open/LA-005) | 线性代数综合题（OCR待核对） | 线性代数综合待精分 | 不可核验；缺少可独立作答的原子题面。 | missing_question_surface：不可推断；缺少可独立作答的原子题面。 | b38_missing_question_surface_la_005 |
| [LA-006](http://127.0.0.1:8765/open/LA-006) | 含参数问题 | 非原子来源待拆分 | 不可核验；缺少可独立作答的原子题面。 | missing_question_surface：不可推断；缺少可独立作答的原子题面。 | b38_non_atomic_outline_hold_la_006 |
| [LA-007](http://127.0.0.1:8765/open/LA-007) | 行列式函数方程根数 | 含参行列式、行列式结构化计算、多项式方程、实根去重 | \boxed{2} | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | — |
| [LA-008](http://127.0.0.1:8765/open/LA-008) | 增广矩阵秩条件判参 | 非齐次线性方程组有解条件、增广矩阵、行列式按列展开 | \boxed{D_2=8} | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | — |
| [LA-009](http://127.0.0.1:8765/open/LA-009) | 行列式展开中特定次数项系数 | 行列式按定义展开、排列与逆序数、含参多项式系数筛选 | \(-5\) | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | — |
| [LA-010](http://127.0.0.1:8765/open/LA-010) | 含参四阶行列式分块化计算 | 具体型行列式、初等行变换、分块上三角、参数边界检查 | \(a^4-4a^2\) | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | — |
| [LA-011](http://127.0.0.1:8765/open/LA-011) | 代数余子式线性组合求参 | 代数余子式、替换列行列式、按列展开 | \boxed{a=1.} | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | — |
| [LA-013](http://127.0.0.1:8765/open/LA-013) | 递推型行列式求通项 | n阶行列式、沿第一列展开、一阶递推、递推初值 | \boxed{D_n=b^n+a_1b^{n-1}+a_2b^{n-2}+\cdots+a_{n-1}b+a_n} | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | — |
| [LA-014](http://127.0.0.1:8765/open/LA-014) | 三对角行列式归纳证明 | 三对角行列式、二阶递推、数学归纳法、递推初值 | \boxed{D_n=(n+1)a^n} | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | — |
| [LA-015](http://127.0.0.1:8765/open/LA-015) | 正交矩阵行列式判零 | 正交矩阵、转置与行列式、奇数阶反号、乘积行列式 | \boxed{0} | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | b38_complete_proof_la_015 |
| [LA-016](http://127.0.0.1:8765/open/LA-016) | 伴随矩阵特征值与矩阵多项式行列式 | 伴随矩阵、伴随矩阵谱、特征值反推、矩阵多项式谱映射、行列式 | \boxed{-\dfrac{253}{8}} | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | — |
| [LA-017](http://127.0.0.1:8765/open/LA-017) | 特征多项式点值定系数 | 特征多项式、首一三次多项式重建、行列式点值 | \boxed{11} | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | — |
| [LA-018](http://127.0.0.1:8765/open/LA-018) | 幂等矩阵矩阵多项式行列式 | 实对称矩阵、幂等矩阵、秩与特征值重数、矩阵多项式谱映射、行列式 | \boxed{(-1)^n10^r9^{n-r}} | pending_user_confirmation：个人错因待确认；仅保留客观复做风险。 | — |

## 逐题复核

### GS-662 57909 复合三角积分比较

- 题目：{'title': '57909 复合三角积分比较', 'question_type': '复合三角函数定积分大小比较', 'atomic_problem_status': 'verified_atomic'}
- 所问：复合三角函数定积分大小比较
- 知识点：定积分；积分保序；函数单调性；三角不等式；复合函数点态比较
- 第一动作：先写 0<sin x<x，再分别用外层 sin 递增、cos 递减作点态比较。
- 答案：A。由 \(0<\sin x<x<\frac\pi2\)，得 \(\sin(\sin x)<\sin x\)，故 \(I_1<1\)；又因 \(\cos x\) 在 \([0,\frac\pi2]\) 上递减，\(\sin x<x\) 推出 \(\cos(\sin x)>\cos x\)，故 \(I_2>1\)。所以 \(I_1<1<I_2\)。
- 个人错因边界：user_confirmed；没有从复合三角函数比较题中触发“引入 \\(x\\) 作中间量”的动作，而是持续尝试换元，把问题带到 \\(\\arcsin t\\) 的复杂路径。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 先判型
  - 中间量比较
  - 点态比较
  - 积分保序
  - 三角函数单调性
  - 三角不等式
  - 定积分大小估计
- 质量发现：
  - `b38_source_literal_repair_gs_662`：；建议：
- 当前快照：`stale`；正式卡 `5ee5def09d57e0c573ccd0ec7467b6711a788b3ea5702e877cd3f5eb1b4436ce`；唯一图片 2 个；物理路径 2 个。

### GS-663 81436 定积分比较作差反折

- 题目：{'title': '81436 定积分比较作差反折', 'question_type': '三个定积分大小排序', 'atomic_problem_status': 'verified_atomic'}
- 所问：三个定积分大小排序
- 知识点：定积分；作差法；倒数比较方向；变号区间分段；对称换元；区间再现
- 第一动作：先直接比较 I2、I3，再将 I1-I2 作差并在 pi/4 处分段反折。
- 答案：A。先由 \((1+x)^2>1+x^2\) 且 \(\sin x>0\) 得 \(I_2>I_3\)。再作差 \(I_1-I_2=\int_0^{\pi/2}\frac{\cos x-\sin x}{1+x^2}dx\)，把后半段用 \(x\mapsto \frac\pi2-x\) 反折到 \((0,\frac\pi4)\)，得到正 integrand，故 \(I_1>I_2\)。综上 \(I_1>I_2>I_3\)。
- 个人错因边界：user_confirmed；有作差意识但没有把 \\(I_1-I_2\\) 落地；比较分母时忘记倒数不等号反向；反折换元时把 \\(\\frac\\pi2-\\frac\\pi4\\) 算成负数。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 先判型
  - 被积函数比较
  - 作差法
  - 对称换元
  - 积分保序
  - 分母单调转倒数单调
  - 定积分大小估计
- 质量发现：
  - `b38_source_literal_repair_gs_663`：；建议：
- 当前快照：`stale`；正式卡 `00b7e54def3a865444b2b39961d14d7c83e2434fc6b15d7217357c77c37a7d36`；唯一图片 2 个；物理路径 2 个。

### GS-664 170728 凹函数弦线积分均值

- 题目：{'title': '170728 凹函数弦线积分均值', 'question_type': '导函数符号与凹函数弦线积分比较选择题', 'atomic_problem_status': 'verified_atomic'}
- 所问：导函数符号与凹函数弦线积分比较选择题
- 知识点：变上限积分；导数判单调；二阶导数判凹凸；凹函数端点弦线；积分面积比较
- 第一动作：写 F'=f>0、F''=f'<0、F(0)=0，将 F 识别为递增凹函数。
- 答案：C。由 \(F'(x)=f(x)>0\)、\(F''(x)=f'(x)<0\)、\(F(0)=0\)，可知 \(F\) 在 \([0,1]\) 上递增且为凹函数。凹函数图像在端点弦线 \(y=xF(1)\) 上方，所以 \(F(x)>xF(1)\)。积分得 \(\int_0^1F(x)\,dx>\frac12F(1)\)，即 \(F(1)<2\int_0^1F(x)\,dx\)。又 \(0<x<1\) 时 \(F(x)<F(1)\)，故 \(F(x)<2\int_0^1F(x)\,dx\)。
- 个人错因边界：user_confirmed；没有从 \\(F'\\) 与 \\(F''\\) 的符号触发凹函数弦线图像比较；转而构造 \\(g(x)\\) 后，又把全区间积分常数在 \\(x=0\\) 处误消成 0。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 先判型
  - 导函数符号判单调凹凸
  - 凹函数图像判断
  - 端点弦线法
  - 积分保序
  - 面积比较
  - 定积分大小估计
- 质量发现：
  - `b38_false_F_prime_mismatch_withdrawn`：The image says y=F(x), not y=F'(x); the earlier candidate typo claim was false.；建议：
- 当前快照：`stale`；正式卡 `9e1bddcca9d25e272043d254b7f88fcb25176be6a5519425552112c16cb8a673`；唯一图片 2 个；物理路径 2 个。

### GS-665 170733 凸函数加权积分比较

- 题目：{'title': '170733 凸函数加权积分比较', 'question_type': '凸函数条件下加权定积分比较选择题', 'atomic_problem_status': 'verified_atomic'}
- 所问：凸函数条件下加权定积分比较选择题
- 知识点：凸函数；加权定积分不等式；变上限辅助函数；拉格朗日中值定理；二阶导数判号
- 第一动作：将 B 移项，把固定上限 a 变量化为 t，并构造同型变上限差值辅助函数。
- 答案：B。令 \(F(t)=\int_0^t x f(x)\,dx-\frac23t\int_0^t f(x)\,dx\)。则 \(F'(t)=\frac13t f(t)-\frac23\int_0^t f(x)\,dx,\ F'(0)=0\)，且 \(F''(t)=\frac13t f'(t)-\frac13f(t)\)。由拉格朗日中值定理，\(f(t)-f(0)=t f'(\xi)\)，其中 \(0<\xi<t\)；又 \(f''>0\)，故 \(f'(t)>f'(\xi)\)，所以 \(F''(t)=\frac13t[f'(t)-f'(\xi)]>0\)。于是 \(F'(t)>0,\ F(t)>0\)，取 \(t=a\) 得 \(\int_0^a x f(x)\,dx>\frac23a\int_0^a f(x)\,dx\)，即 \(3\int_0^a x f(x)\,dx>2a\int_0^a f(x)\,dx\)，选 B。
- 个人错因边界：user_confirmed；没有先围绕选项目标构造变上限差值辅助函数；转而使用凸函数弦线和 Taylor 的点态比较，后续卡在带权积分整体符号比较。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 目标移项
  - 构造辅助函数
  - 变上限积分整体设F
  - 变上限积分求导
  - 导数判单调
  - 拉格朗日中值定理
  - 凸函数判号
  - 积分不等式
- 当前快照：`stale`；正式卡 `dbf5d524212d74afd8db30edf46f7fdbc9f23958c1f2015638a1c1aa96a43d32`；唯一图片 2 个；物理路径 2 个。

### LA-001 线代1000题A组1.7

- 题目：{'title': '线代1000题A组1.7', 'question_type': '行列式计算', 'atomic_problem_status': 'verified_atomic'}
- 所问：行列式计算
- 知识点：行列式；行列式对一行的线性性；初等列变换；按行展开
- 第一动作：用行列式对一行的线性性，将差合并为差行行列式。
- 答案：10(a-3)
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 等价变形
  - 初等变换
  - 矩阵初等变换
- 质量发现：
  - `b38_complete_question_la_001`：；建议：
  - `b38_method_gap_consistency_la_001`：；建议：
- 当前快照：`current`；正式卡 `5b439ef04c4c5051cec94622e75a1ef2e9e59ede845d6b6ebe1a8e18b891b9df`；唯一图片 1 个；物理路径 1 个。

### LA-002 线代1000题A组1.4

- 题目：{'title': '线代1000题A组1.4', 'question_type': '行列式函数零点个数判断', 'atomic_problem_status': 'verified_atomic'}
- 所问：行列式函数零点个数判断
- 知识点：行列式；列变换；行列式对一列的线性性；含参行列式多项式次数
- 第一动作：做列差，使 x 只保留在一列，从而确认 f 是至多一次多项式。
- 答案：\boxed{f(x)=0\text{ 至多有一个零点}}
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 列变换
  - 行列式线性性
  - 零点个数判断
- 当前快照：`stale`；正式卡 `9dfcdd5351093c31706fb0937731184560573df59ad4f75b6f35288970ec4ae9`；唯一图片 1 个；物理路径 2 个。

### LA-004 强化例题13.17（历史编号待重连）

- 题目：{'title': '强化例题13.17（历史编号待重连）', 'question_type': '隐函数方程组求导', 'atomic_problem_status': 'verified_atomic'}
- 所问：隐函数方程组求导
- 知识点：隐函数方程组；多元函数求导；点值代入；联立线性方程
- 第一动作：先代 x=1/2 求 y=e^2、z=2，再对两个方程关于 x 求导并联立。
- 答案：\boxed{\left.\frac{dz}{dx}\right|_{x=\frac12}=-4}
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 隐函数求导
  - 点值代入
  - 联立方程组
- 质量发现：
  - `b38_cross_subject_identity_hold_la_004`：The content is a high-math implicit-system problem under a historical LA identifier; no merge or renumber is authorized.；建议：
- 当前快照：`current`；正式卡 `edbbac05f8c568755c589ced77a9594d7e7de82f1bb8ee03aa99a8a79c88de47`；唯一图片 1 个；物理路径 2 个。

### LA-005 2023年第13题

- 题目：{'title': '2023年第13题', 'question_type': '线性代数综合题（OCR待核对）', 'atomic_problem_status': 'missing_or_non_atomic_hold'}
- 所问：线性代数综合题（OCR待核对）
- 知识点：线性代数综合待精分
- 第一动作：先取得正确题图或可靠 OCR 并完成身份重连，当前不能推断方法。
- 答案：不可核验；缺少可独立作答的原子题面。
- 个人错因边界：missing_question_surface；不可推断；缺少可独立作答的原子题面。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
- 质量发现：
  - `b38_missing_question_surface_la_005`：No concrete stem, reliable OCR, answer or image exists; the same-title GS-465 image is explicitly excluded.；建议：
- 当前快照：`current`；正式卡 `fe885c8a92adb039c0bdc43bf081fdd2ca0c42a66be7450dfc8a534f568c2759`；唯一图片 0 个；物理路径 0 个。

### LA-006 线代强化

- 题目：{'title': '线代强化', 'question_type': '含参数问题', 'atomic_problem_status': 'missing_or_non_atomic_hold'}
- 所问：含参数问题
- 知识点：非原子来源待拆分
- 第一动作：先回源拆出原子题目；在此之前不应生成错因或题间强边。
- 答案：不可核验；缺少可独立作答的原子题面。
- 个人错因边界：missing_question_surface；不可推断；缺少可独立作答的原子题面。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
- 质量发现：
  - `b38_non_atomic_outline_hold_la_006`：The imported text is a truncated linear-algebra outline, not an independently answerable question.；建议：
- 当前快照：`current`；正式卡 `823fe1e065b8e27643b603a4575dbd104cc4425136beca54d7206fe60fd2883b`；唯一图片 0 个；物理路径 0 个。

### LA-007 强化例题1.1

- 题目：{'title': '强化例题1.1', 'question_type': '行列式函数方程根数', 'atomic_problem_status': 'verified_atomic'}
- 所问：行列式函数方程根数
- 知识点：含参行列式；行列式结构化计算；多项式方程；实根去重
- 第一动作：先分别结构化化简两个行列式函数，再解多项式方程。
- 答案：\boxed{2}
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 行列式化简
  - 初等变换
  - 多项式方程求根
- 当前快照：`current`；正式卡 `e05ea95d3757e50260e90e0068f1a693c2329545d9f6fd21355560fea50094a4`；唯一图片 1 个；物理路径 2 个。

### LA-008 强化例题1.2

- 题目：{'title': '强化例题1.2', 'question_type': '增广矩阵秩条件判参', 'atomic_problem_status': 'verified_atomic'}
- 所问：增广矩阵秩条件判参
- 知识点：非齐次线性方程组有解条件；增广矩阵；行列式按列展开
- 第一动作：把有解条件写成四阶增广行列式为 0。
- 答案：\boxed{D_2=8}
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 秩条件
  - 增广矩阵
  - 按列展开
  - 条件转化
- 当前快照：`stale`；正式卡 `e7e67099e72b6f9ff40fa18862b77691c91a79d5c89c8b9148852548c8a1ccf4`；唯一图片 1 个；物理路径 2 个。

### LA-009 2021年第16题

- 题目：{'title': '2021年第16题', 'question_type': '行列式展开中特定次数项系数', 'atomic_problem_status': 'verified_atomic'}
- 所问：行列式展开中特定次数项系数
- 知识点：行列式按定义展开；排列与逆序数；含参多项式系数筛选
- 第一动作：只筛选恰含三个 x 且每行每列各取一次的排列项。
- 答案：\(-5\)
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 行列式排列展开
  - 指定幂次项筛选
  - 逆序数判符号
- 当前快照：`current`；正式卡 `5b2a552cd60a69f9b060fdacdcd466225176d867e2a8fd1fd5f1fb804001e877`；唯一图片 2 个；物理路径 4 个。

### LA-010 2020年第14题

- 题目：{'title': '2020年第14题', 'question_type': '含参四阶行列式分块化计算', 'atomic_problem_status': 'verified_atomic'}
- 所问：含参四阶行列式分块化计算
- 知识点：具体型行列式；初等行变换；分块上三角；参数边界检查
- 第一动作：先用保值行变换化为分块上三角；若使用 1/a，最后补查 a=0。
- 答案：\(a^4-4a^2\)
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 初等行变换化分块
  - 分块上三角行列式
  - 参数特殊值检查
- 当前快照：`current`；正式卡 `69e813bec6bb35a52c787fd1c50650d0e94445e8d4a8dd7cbb35814375d16900`；唯一图片 2 个；物理路径 4 个。

### LA-011 1000题A组1.8

- 题目：{'title': '1000题A组1.8', 'question_type': '代数余子式线性组合求参', 'atomic_problem_status': 'verified_atomic'}
- 所问：代数余子式线性组合求参
- 知识点：代数余子式；替换列行列式；按列展开
- 第一动作：把代数余子式线性组合视作替换第 1 列后的行列式。
- 答案：\boxed{a=1.}
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 替列行列式
  - 行列式行变换
  - 按行展开
- 当前快照：`stale`；正式卡 `6ef7c391e4184af8c587ed7c4ad8d5303862bd685658d9fa84bef32ff787dda7`；唯一图片 1 个；物理路径 2 个。

### LA-013 强化例题1.4

- 题目：{'title': '强化例题1.4', 'question_type': '递推型行列式求通项', 'atomic_problem_status': 'verified_atomic'}
- 所问：递推型行列式求通项
- 知识点：n阶行列式；沿第一列展开；一阶递推；递推初值
- 第一动作：沿第一列展开，识别低阶同型行列式。
- 答案：\boxed{D_n=b^n+a_1b^{n-1}+a_2b^{n-2}+\cdots+a_{n-1}b+a_n}
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 拉普拉斯展开
  - 递推行列式
  - 第一列展开
- 当前快照：`stale`；正式卡 `4e082057de2dc7c3f48e0f8b9bd684e3cc0ee2043f9f7c40d8f4a1fe226a7117`；唯一图片 1 个；物理路径 2 个。

### LA-014 强化例题1.5

- 题目：{'title': '强化例题1.5', 'question_type': '三对角行列式归纳证明', 'atomic_problem_status': 'verified_atomic'}
- 所问：三对角行列式归纳证明
- 知识点：三对角行列式；二阶递推；数学归纳法；递推初值
- 第一动作：沿第一列建立二阶递推，并写初值。
- 答案：\boxed{D_n=(n+1)a^n}
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 三对角行列式递推
  - 拉普拉斯展开
  - 数学归纳法
- 当前快照：`stale`；正式卡 `99e9a0f71637aa35431d1810dce827d28b492ba24451e52c04aed6eac7cd303c`；唯一图片 1 个；物理路径 2 个。

### LA-015 强化例题1.6

- 题目：{'title': '强化例题1.6', 'question_type': '正交矩阵行列式判零', 'atomic_problem_status': 'verified_atomic'}
- 所问：正交矩阵行列式判零
- 知识点：正交矩阵；转置与行列式；奇数阶反号；乘积行列式
- 第一动作：利用正交性对两个因子同时作 A^T(·)B^T 变换，再使用转置与奇数阶反号。
- 答案：\boxed{0}
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 正交矩阵性质
  - 行列式乘法
  - 转置不变
  - 奇数阶负号
- 质量发现：
  - `b38_complete_proof_la_015`：；建议：
- 当前快照：`stale`；正式卡 `dcf8b4f321f18cd5fabb33ac1089f35e66b0759a736fa3b262eb8a85857231dd`；唯一图片 1 个；物理路径 2 个。

### LA-016 强化例题1.7

- 题目：{'title': '强化例题1.7', 'question_type': '伴随矩阵特征值与矩阵多项式行列式', 'atomic_problem_status': 'verified_atomic'}
- 所问：伴随矩阵特征值与矩阵多项式行列式
- 知识点：伴随矩阵；伴随矩阵谱；特征值反推；矩阵多项式谱映射；行列式
- 第一动作：由 det(A*)=det(A)^3 求 det(A)，再反推 A 的特征值。
- 答案：\boxed{-\dfrac{253}{8}}
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 伴随矩阵谱关系
  - 谱映射
  - 行列式等于特征值乘积
- 当前快照：`stale`；正式卡 `a915def5546a1f37ba7fabe96f1524791e0421245cc285e81e2eda0038f2907b`；唯一图片 1 个；物理路径 2 个。

### LA-017 1000题B组1.7

- 题目：{'title': '1000题B组1.7', 'question_type': '特征多项式点值定系数', 'atomic_problem_status': 'verified_atomic'}
- 所问：特征多项式点值定系数
- 知识点：特征多项式；首一三次多项式重建；行列式点值
- 第一动作：设 p(lambda)=det(lambda E-A)，把条件统一成 p(1)、p(-1)、p(2)。
- 答案：\boxed{11}
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 特征多项式
  - 点值定系数
  - 代入目标点
- 当前快照：`stale`；正式卡 `004b16e413ac9975dd940676cbbcf26576d00fee3d3fa079212a4e6d5b9c73cb`；唯一图片 1 个；物理路径 2 个。

### LA-018 1000题B组1.8

- 题目：{'title': '1000题B组1.8', 'question_type': '幂等矩阵矩阵多项式行列式', 'atomic_problem_status': 'verified_atomic'}
- 所问：幂等矩阵矩阵多项式行列式
- 知识点：实对称矩阵；幂等矩阵；秩与特征值重数；矩阵多项式谱映射；行列式
- 第一动作：由 A^2=A 得谱只含 0、1，再由秩确定重数。
- 答案：\boxed{(-1)^n10^r9^{n-r}}
- 个人错因边界：pending_user_confirmation；个人错因待确认；仅保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 幂等矩阵谱
  - 秩定重数
  - 谱映射
- 当前快照：`stale`；正式卡 `5508f21fdafc96de93600c6cec9e4540e762c1010666c23efdc19e1e2de592d3`；唯一图片 1 个；物理路径 2 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
