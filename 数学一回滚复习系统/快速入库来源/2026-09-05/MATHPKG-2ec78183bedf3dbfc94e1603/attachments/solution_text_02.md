28-11｜ID 57744｜利用叉积求平行四边形面积 {#problem-57744}

**知识点标签：** 平行四边形面积；点积与余弦；叉积的模与正弦；叉积的双线性；反交换律；数乘向量的模；线性组合与面积倍数。

**可见学习状态：** 用户在 T25 明确表示已经理解、本题没问题，并要求归档；未记录独立重做。

### 题目文字与答案

设 $\alpha$ 与 $\beta$ 均为单位向量，其夹角为 $\pi/6$，则以 $\alpha+2\beta$ 与 $3\alpha+\beta$ 为邻边的平行四边形的面积为______。

**正确答案：** $5/2$。

### 题目与解析原图

**题目原图：线性组合向量作邻边的平行四边形面积**

![题目原图：线性组合向量作邻边的平行四边形面积｜28-11 ID 57744](assets/28-11_57744_question.png)

原图：`assets/28-11_57744_question.png` · 1636 × 388 像素。

**解析一：展开叉积，取模求面积**

![解析一：展开叉积，取模求面积｜28-11 ID 57744](assets/28-11_57744_solution_01.png)

原图：`assets/28-11_57744_solution_01.png` · 1576 × 2420 像素。

**解析二：建立坐标后计算叉积**

![解析二：建立坐标后计算叉积｜28-11 ID 57744](assets/28-11_57744_solution_02.png)

原图：`assets/28-11_57744_solution_02.png` · 1582 × 2476 像素。

### 校核后的知识点与考试路径

**平行四边形面积是邻边叉积的模。** 对非零向量 $\boldsymbol u,\boldsymbol v$，令两者夹角为 $\theta\in[0,\pi]$：

$$
S=\|\boldsymbol u\|\|\boldsymbol v\|\sin\theta
=\|\boldsymbol u\times\boldsymbol v\|.
$$

仅知道两条边长不能确定面积，还需要夹角或相应的高。题目中的 $\pi/6$ 是 $\alpha,\beta$ 的夹角，不是两个新向量的夹角。

本题直接展开：

$$
\begin{aligned}
(\alpha+2\beta)\times(3\alpha+\beta)
&=3(\alpha\times\alpha)+(\alpha\times\beta)
 +6(\beta\times\alpha)+2(\beta\times\beta)\\
&=(\alpha\times\beta)+6(\beta\times\alpha)\\
&=(\alpha\times\beta)-6(\alpha\times\beta)\\
&=-5(\alpha\times\beta).
\end{aligned}
$$

以上得到的是向量，再取模才得到面积：

$$
S=\|-5(\alpha\times\beta)\|
=|-5|\,\|\alpha\times\beta\|
=5\cdot1\cdot1\cdot\sin\frac\pi6
=\boxed{\frac52}.
$$

### 用户的实际卡点与纠正记录

| 原始卡点 | 校核结论 | 原文定位 |
|---|---|---|
| 只想算两条新边的长度后求面积 | 还需要新边夹角；直接算叉积的模避免绕路 | T21—T22 |
| 将第二条边口述成 $\alpha+\beta$ | 题图为 $3\alpha+\beta$ | T21—T22 |
| 认为叉积的模对应 $\cos\theta$ | 点积对应余弦，叉积的模对应正弦 | T23—T24 |
| 不理解 $\beta\times\alpha$ 的负号 | 叉积反交换：交换顺序后方向反转；也可由行列式换行变号理解 | T23—T24 |
| 不理解 $-5$ 为什么取模后变成 $5$ | $\|k\boldsymbol v\|=|k|\|\boldsymbol v\|$；方向改变不影响长度 | T23—T24 |

### 必须分开的三个对象

| 对象 | 类型 | 公式 |
|---|---|---|
| 点积 $\boldsymbol a\cdot\boldsymbol b$ | 标量，可正、可负或零 | $\|\boldsymbol a\|\|\boldsymbol b\|\cos\theta$ |
| 叉积 $\boldsymbol a\times\boldsymbol b$ | 向量 | 垂直于两向量，非零时方向服从右手定则 |
| 叉积的模 $\|\boldsymbol a\times\boldsymbol b\|$ | 非负数 | $\|\boldsymbol a\|\|\boldsymbol b\|\sin\theta$ |

$$
\cos\theta=\frac{\boldsymbol a\cdot\boldsymbol b}{\|\boldsymbol a\|\|\boldsymbol b\|},
\qquad
\sin\theta=\frac{\|\boldsymbol a\times\boldsymbol b\|}{\|\boldsymbol a\|\|\boldsymbol b\|}.
$$

余弦公式分子是点积本身，不应擅自加绝对值，否则会丢掉钝角信息。零向量不定义夹角；非零向量与自身的夹角为零，所以自身叉积为零。

**数乘提模的计算解释：** $\|k\boldsymbol v\|=\sqrt{k^2(v_1^2+v_2^2+v_3^2)}=|k|\|\boldsymbol v\|$。本题不是先得到 $-5\|\alpha\times\beta\|$ 再随意删负号，而是从 $\|-5(\alpha\times\beta)\|$ 正确提出 $|-5|$。

### 其他解法与可迁移结论

题图方法二选取 $\alpha=(1,0,0)$、$\beta=(\sqrt3/2,1/2,0)$，满足单位长度与已知夹角，计算新向量叉积得 $(0,0,-5/2)$，取模仍为 $5/2$。这是重新选择方便的坐标系，不是任意改变题设。

用户最初的“先求长度”路线也能完成：

$$
\|\alpha+2\beta\|^2=5+2\sqrt3,\qquad
\|3\alpha+\beta\|^2=10+3\sqrt3.
$$

再结合新向量点积 $5+7\sqrt3/2$，可用
$S^2=\|\boldsymbol u\|^2\|\boldsymbol v\|^2-(\boldsymbol u\cdot\boldsymbol v)^2=25/4$。
这一路线正确，但本题直接展开叉积更省计算。

对更一般的两条邻边，有：

$$
(a\alpha+b\beta)\times(c\alpha+d\beta)
=(ad-bc)(\alpha\times\beta),
$$
$$
S=|ad-bc|\,\|\alpha\|\|\beta\|\sin\varphi.
$$

这里 $a,b,c,d$ 是线性组合系数，不是边长。三角形面积才需在叉积模长前再乘 $1/2$。

### 复核问题（尚未在本轮独立作答）

若交换平行四边形两条邻边的顺序，说明叉积向量和面积各会如何变化；再用两向量平行时叉积为零，检查为什么叉积模长不可能使用余弦公式。

### 本题完整对话（T21—T24）

> 以下为历史对话正文。原文中出现的错误理解、口误或过强表述已在上方另行校核，不在原文内删改。

#### T21｜用户 {#t21}

**本条消息原附件顺序：** `assets/28-11_57744_solution_01.png`；`assets/28-11_57744_solution_02.png`；`assets/28-11_57744_question.png`。图片原件已在本题图片区完整展示。

这是这道题目和两个不同的解法。

我能想到的思路是：

1. 首先要知道平行四边形的面积公式。在已知两条邻边具体长度的情况下，要怎么求出平行四边形的面积？
2. 然后把 α + 2β 和 α + β 这两个向量的具体长度算出来。
3. 算出来之后，结合这两个长度和平行四边形的面积公式，把这道题的答案做出来。

但我现在卡住了：我忘记了已知两条邻边时该怎么求平行四边形的面积，同时也不知道怎么求这两个具体向量的长度。还是说我这个思路一开始就有问题，不应该往这个方向走？

#### T22｜助手 {#t22}

你的思路**不是错的**，但考试里不推荐，因为会绕很大一圈。

先纠正一个小地方：题目两条邻边是

\[
\boxed{\alpha+2\beta,\qquad 3\alpha+\beta}
\]

不是 \(\alpha+\beta\)。

这道题最实用的切入点其实就是：**题目问“以两个向量为邻边的平行四边形面积” → 第一反应直接想到叉乘。**

---

###### 1. 平行四边形面积公式你要记住

如果两条邻边向量是 \(\mathbf a,\mathbf b\)，夹角为 \(\theta\)，那么

\[
\boxed{S=|\mathbf a||\mathbf b|\sin\theta}
\]

而叉乘的模恰好就是这个东西：

\[
\boxed{|\mathbf a\times\mathbf b|
=|\mathbf a||\mathbf b|\sin\theta}
\]

所以可以直接记：

\[
\boxed{\text{两个向量为邻边的平行四边形面积}
=
|\mathbf a\times\mathbf b|}
\]

三角形面积才是：

\[
\frac12|\mathbf a\times\mathbf b|.
\]

---

##### 2. 你的方法为什么会卡住？

你想先算：

\[
|\alpha+2\beta|
\]

和

\[
|3\alpha+\beta|,
\]

这个当然能算。

因为 \(\alpha,\beta\) 都是单位向量，而且夹角：

\[
\varphi=\frac{\pi}{6},
\]

所以：

\[
\alpha\cdot\beta
=
|\alpha||\beta|\cos\frac\pi6
=
\frac{\sqrt3}{2}.
\]

比如：

\[
|\alpha+2\beta|^2
=
(\alpha+2\beta)\cdot(\alpha+2\beta)
\]

\[
=
|\alpha|^2+4|\beta|^2+4\alpha\cdot\beta
\]

\[
=1+4+2\sqrt3
\]

所以：

\[
|\alpha+2\beta|
=
\sqrt{5+2\sqrt3}.
\]

同理：

\[
|3\alpha+\beta|
=
\sqrt{10+3\sqrt3}.
\]

但到这里你会发现一个问题：

\[
S=|\mathbf a||\mathbf b|\sin\theta
\]

还缺什么？

缺的是

\[
\boxed{\alpha+2\beta\text{ 与 }3\alpha+\beta\text{ 之间的夹角 }\theta}.
\]

题目告诉你的 \(\pi/6\) 是 **\(\alpha\) 与 \(\beta\) 的夹角**，不是这两个新向量之间的夹角。

所以你还得算：

\[
(\alpha+2\beta)\cdot(3\alpha+\beta)
\]

再求 \(\cos\theta\)，再求 \(\sin\theta\)。

能做，但非常麻烦。

所以你这个路线：

\[
\text{算两条新边长度}
\rightarrow
\text{算新边夹角}
\rightarrow
S=ab\sin\theta
\]

理论完全正确，**考试不划算。**

---

##### 3. 这题考试应该直接叉乘

设：

\[
\mathbf u=\alpha+2\beta,
\qquad
\mathbf v=3\alpha+\beta.
\]

面积：

\[
S=
|(\alpha+2\beta)\times(3\alpha+\beta)|.
\]

直接展开：

\[
(\alpha+2\beta)\times(3\alpha+\beta)
\]

\[
=
3\alpha\times\alpha
+\alpha\times\beta
+6\beta\times\alpha
+2\beta\times\beta.
\]

这里使用两个非常重要的叉乘性质：

\[
\boxed{\alpha\times\alpha=0}
\]

因为一个向量和自己平行，夹角 \(0\)，所以叉乘为零。

同理：

\[
\boxed{\beta\times\beta=0}.
\]

另外：

\[
\boxed{\beta\times\alpha=-\alpha\times\beta}
\]

所以原式：

\[
=
\alpha\times\beta
+6(-\alpha\times\beta)
\]

\[
=
-5\alpha\times\beta.
\]

于是面积：

\[
S
=
|-5\alpha\times\beta|
=
5|\alpha\times\beta|.
\]

而题目已经告诉：

\[
|\alpha|=|\beta|=1,
\qquad
\angle(\alpha,\beta)=\frac\pi6.
\]

因此：

\[
|\alpha\times\beta|
=
|\alpha||\beta|\sin\frac\pi6
=
1\times1\times\frac12
=
\frac12.
\]

最终：

\[
\boxed{S=\frac52}.
\]

---

##### 4. 其实这道题有一个更值得你掌握的“秒算结构”

以后看到：

\[
a\alpha+b\beta
\]

和

\[
c\alpha+d\beta
\]

作为两条邻边，可以直接叉乘：

\[
(a\alpha+b\beta)\times(c\alpha+d\beta).
\]

展开以后：

\[
ac\,\alpha\times\alpha
+ad\,\alpha\times\beta
+bc\,\beta\times\alpha
+bd\,\beta\times\beta.
\]

首尾两项都是零：

\[
=(ad-bc)\alpha\times\beta.
\]

所以：

\[
\boxed{
(a\alpha+b\beta)\times(c\alpha+d\beta)
=
(ad-bc)(\alpha\times\beta)
}
\]

因此平行四边形面积直接：

\[
\boxed{
S=
|ad-bc|\,
|\alpha||\beta|\sin\varphi
}
\]

本题：

\[
\alpha+2\beta
\Rightarrow (a,b)=(1,2),
\]

\[
3\alpha+\beta
\Rightarrow (c,d)=(3,1).
\]

所以：

\[
ad-bc
=
1\times1-2\times3
=
-5.
\]

取绝对值：

\[
5.
\]

再乘：

\[
|\alpha||\beta|\sin\frac\pi6
=
\frac12.
\]

直接：

\[
\boxed{S=5\times\frac12=\frac52}.
\]

---

###### 5. 以后这种题你的第一反应

看到：

> “以两个向量为邻边的平行四边形面积”

直接触发：

\[
\boxed{S=|\mathbf a\times\mathbf b|}
\]

然后如果两条边还是：

\[
a\alpha+b\beta,\qquad c\alpha+d\beta
\]

这种线性组合，**不要先求它们的长度，也不要先求新夹角**。

直接展开叉乘：

\[
\boxed{
(a\alpha+b\beta)\times(c\alpha+d\beta)
}
\]

利用：

\[
\alpha\times\alpha=0,
\qquad
\beta\times\beta=0,
\qquad
\beta\times\alpha=-\alpha\times\beta.
\]

最后一定会化成：

\[
\boxed{\text{一个常数}\times(\alpha\times\beta)}.
\]

然后再使用原始的：

\[
|\alpha\times\beta|
=
|\alpha||\beta|\sin\varphi.
\]

**这才是这道题考试时最稳、最快、最值得形成肌肉记忆的方法。**

#### T23｜用户 {#t23}

这个叉乘的模长，不应该是 A 的模长乘以 B 的模长乘以 cos θ 吗？

我记得有这么个公式：cos θ 等于分母是 A 的模长乘以 B 的模长，分子是 A 跟 B 的叉乘的模长。我觉得 cos θ 应该是这么个东西，而不是 sin θ还有你提到的向量自己跟自己平行、叉乘等于 0，这我也理解。所以你直接将这两个向量做叉乘，让题目里的 (α + 2β) 跟 (3α + β) 做叉乘，展开后得出 3(α × α) + (α × β) + 6(β × α) + 2(β × β)。因为 β × β = 0 且 α × α = 0，很自然就变成了 (α × β) + 6(β × α)。

但后面我不理解：

1. 为什么 β × α 会变成 -α × β？这个是怎么得出来的，是什么结论？
2. 后面怎么变成了 -5|α × β|？为什么可以把 5 提出来？为什么前面有个负号还能提出来变成 5|α × β|？

这几个地方我不是很懂，讲一下这些问题吧。

#### T24｜助手 {#t24}

你这里其实混淆了**点积**和**叉积**的两个公式。把这两个分开以后，后面的所有步骤就顺了。

###### 先纠正最关键的一点：\(\cos\theta\) 对应点积，不是叉积

两个向量 \(\mathbf a,\mathbf b\) 夹角为 \(\theta\)。

###### 点积

\[
\boxed{\mathbf a\cdot\mathbf b
=\|\mathbf a\|\|\mathbf b\|\cos\theta}
\]

所以：

\[
\boxed{
\cos\theta
=
\frac{\mathbf a\cdot\mathbf b}
{\|\mathbf a\|\|\mathbf b\|}
}
\]

###### 叉积

\[
\boxed{
\|\mathbf a\times\mathbf b\|
=
\|\mathbf a\|\|\mathbf b\|\sin\theta
}
\]

所以：

\[
\boxed{
\sin\theta
=
\frac{\|\mathbf a\times\mathbf b\|}
{\|\mathbf a\|\|\mathbf b\|}
}
\]

你刚才记成了：

\[
\cos\theta
=
\frac{\|\mathbf a\times\mathbf b\|}
{\|\mathbf a\|\|\mathbf b\|}
\]

这里就是把**点积的 \(\cos\)** 和**叉积的 \(\sin\)** 混到一起了。

---

###### 为什么平行四边形面积对应 \(\sin\theta\)？

这个非常直观。

以 \(\mathbf a,\mathbf b\) 为邻边：

- 底边长度是 \(\|\mathbf a\|\)
- 高不是 \(\|\mathbf b\|\cos\theta\)
- 高是 \(\|\mathbf b\|\sin\theta\)

因为 \(\sin\theta\) 对应的是垂直于底边的那一部分。

所以：

\[
S=\text{底}\times\text{高}
\]

即

\[
\boxed{
S=\|\mathbf a\|\|\mathbf b\|\sin\theta
}
\]

而这个东西恰好就是：

\[
\boxed{S=\|\mathbf a\times\mathbf b\|}
\]

你也可以把它们记成：

\[
\boxed{
\begin{array}{c}
\text{点积}\rightarrow\cos\theta\rightarrow\text{平行方向的投影}\\[3pt]
\text{叉积}\rightarrow\sin\theta\rightarrow\text{垂直高度、面积}
\end{array}}
\]

---

##### 1. 为什么 \(\beta\times\alpha=-\alpha\times\beta\)？

这是叉积最基本的性质之一：

\[
\boxed{\mathbf a\times\mathbf b=-\mathbf b\times\mathbf a}
\]

叫做**反交换律**。

注意，普通乘法是：

\[
ab=ba
\]

但叉积不是。

---

###### 为什么？

因为叉积得到的是一个**有方向的向量**。

例如：

\[
\alpha\times\beta
\]

它的方向由右手定则确定。

如果把顺序反过来：

\[
\beta\times\alpha
\]

两者：

- 模长完全一样；
- 方向恰好相反。

所以：

\[
\boxed{
\beta\times\alpha
=
-(\alpha\times\beta)
}
\]

你可以简单记成：

> **叉乘交换位置，要变号。**

跟行列式交换两行变号很像。

实际上叉积写成行列式时：

\[
\alpha\times\beta
=
\begin{vmatrix}
\mathbf i&\mathbf j&\mathbf k\\
\alpha_1&\alpha_2&\alpha_3\\
\beta_1&\beta_2&\beta_3
\end{vmatrix}
\]

而交换 \(\alpha,\beta\)：

\[
\beta\times\alpha
=
\begin{vmatrix}
\mathbf i&\mathbf j&\mathbf k\\
\beta_1&\beta_2&\beta_3\\
\alpha_1&\alpha_2&\alpha_3
\end{vmatrix}.
\]

交换了两行，行列式变号，因此：

\[
\boxed{\beta\times\alpha=-\alpha\times\beta}.
\]

---

##### 2. 所以这道题是怎么得到 \(-5\alpha\times\beta\) 的？

我们已经有：

\[
(\alpha+2\beta)\times(3\alpha+\beta)
\]

展开：

\[
3\alpha\times\alpha
+\alpha\times\beta
+6\beta\times\alpha
+2\beta\times\beta.
\]

因为：

\[
\alpha\times\alpha=0,
\qquad
\beta\times\beta=0,
\]

所以只剩：

\[
\alpha\times\beta+6\beta\times\alpha.
\]

现在使用刚才的反交换律：

\[
\beta\times\alpha
=
-\alpha\times\beta.
\]

因此：

\[
\alpha\times\beta
+
6(-\alpha\times\beta)
\]

\[
=
\alpha\times\beta
-
6\alpha\times\beta.
\]

这其实就像：

\[
x-6x=-5x.
\]

所以：

\[
\boxed{
=-5(\alpha\times\beta)
}
\]

注意，到这一步我们得到的仍然是一个**向量**。

---

##### 3. 为什么最后负号又“消失”了？

因为题目求的是**平行四边形面积**。

面积不是叉积向量本身，而是：

\[
\boxed{
S=
\|(\alpha+2\beta)\times(3\alpha+\beta)\|
}
\]

刚才已经算出叉积向量：

\[
-5(\alpha\times\beta).
\]

于是：

\[
S=
\|-5(\alpha\times\beta)\|.
\]

这里使用向量模长的性质：

\[
\boxed{\|k\mathbf v\|=|k|\|\mathbf v\|}
\]

所以：

\[
\|-5(\alpha\times\beta)\|
=
|-5|\|\alpha\times\beta\|.
\]

而：

\[
|-5|=5.
\]

因此：

\[
\boxed{
S=5\|\alpha\times\beta\|
}
\]

负号为什么没了？

因为负号只表示**向量方向反过来了**，不会改变长度。

比如：

\[
\mathbf v=(3,4)
\]

模长是：

\[
\|\mathbf v\|=5.
\]

而：

\[
-\mathbf v=(-3,-4)
\]

方向完全相反，但模长还是：

\[
\|-\mathbf v\|=5.
\]

所以：

\[
\boxed{\|-\mathbf v\|=\|\mathbf v\|}.
\]

---

##### 4. 最后一步就很简单了

因为 \(\alpha,\beta\) 都是单位向量：

\[
\|\alpha\|=\|\beta\|=1.
\]

夹角：

\[
\theta=\frac{\pi}{6}.
\]

所以：

\[
\|\alpha\times\beta\|
=
\|\alpha\|\|\beta\|\sin\frac{\pi}{6}
\]

\[
=
1\cdot1\cdot\frac12
=
\frac12.
\]

于是：

\[
S=5\times\frac12
\]

得到：

\[
\boxed{\frac52}.
\]

---

###### 这道题你现在需要记牢 4 条叉积性质

以后这类题几乎全靠它们：

\[
\boxed{
\begin{aligned}
①\quad&\mathbf a\times\mathbf a=0\\[3pt]
②\quad&\mathbf a\times\mathbf b=-\mathbf b\times\mathbf a\\[3pt]
③\quad&\|k\mathbf a\|=|k|\|\mathbf a\|\\[3pt]
④\quad&\|\mathbf a\times\mathbf b\|
=\|\mathbf a\|\|\mathbf b\|\sin\theta
\end{aligned}}
\]

而最容易混淆的两个公式，建议你专门并排记：

\[
\boxed{
\mathbf a\cdot\mathbf b
=
\|\mathbf a\|\|\mathbf b\|\cos\theta
}
\]

\[
\boxed{
\|\mathbf a\times\mathbf b\|
=
\|\mathbf a\|\|\mathbf b\|\sin\theta
}
\]

**点积是 cos，叉积是 sin。**

这道题真正的计算链现在就变得非常短：

\[
\alpha\times\beta+6\beta\times\alpha
\]

\[
=
\alpha\times\beta-6\alpha\times\beta
\]

\[
=-5\alpha\times\beta
\]

然后求面积取模：

\[
\|-5\alpha\times\beta\|
=
5\|\alpha\times\beta\|
=
5\cdot1\cdot1\cdot\sin\frac{\pi}{6}
=
\boxed{\frac52}.
\]

---
