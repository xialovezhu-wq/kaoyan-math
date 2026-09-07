57761｜向量模长差的极限


### 题面转录
设 $\alpha$ 与 $\beta$ 是非零常向量，$|\beta|=2$，$|\beta|$ 表示 $\beta$ 的模，$\alpha$ 与 $\beta$ 之间的夹角为 $\pi/3$，求
\[
\lim_{x\to0}\frac{|\alpha+x\beta|-|\alpha|}{x}.
\]
**本轮解析与对话采用的答案：** $1$。题面没有给出 $|\alpha|$ 的具体数值。

### 涉及知识点
向量的模与标量、点积与叉积的区别；$\beta\cdot\beta=|\beta|^2$ 与 $\beta\times\beta=\mathbf0$；平方差有理化；$|u|^2=u\cdot u$；极限的四则运算和连续性；高阶无穷小；导数定义与复合函数求导。

### 本轮学习过程索引
用户先尝试叉乘替换，并把 $\sin(\pi/3)$ 记成 $1/2$；随后追问“自身点积是否为零”“为什么约去 $x$ 后可以取极限”“$4x$ 消失是否损失精度”。讲解逐步区分点积/叉积、向量/模长、函数值/极限，并转向有理化。最后用户正确完成变式 $\lim_{x\to0}(3+4x)/(2+x)=3/2$。来源：T01、T03、T05、T07。

**证据支持的学习状态：** 已在完整讲解后理解直接取极限的这个局部机制，并完成上述变式；没有展示脱离讲解后独立重做整道原题。原回复 T08 的“在局部提示和纠正后完成理解”原样保留，不将它自动升级为独立掌握。

### 便于定位的最终方法
\[
\frac{|\alpha+x\beta|-|\alpha|}{x}
=\frac{2\alpha\cdot\beta+x\beta\cdot\beta}{|\alpha+x\beta|+|\alpha|}\quad(x\ne0).
\]
分母趋于 $2|\alpha|\ne0$，故极限为 $\alpha\cdot\beta/|\alpha|=|\beta|\cos(\pi/3)=1$。该式是对 T02、T04、T06 的归纳，不替代原对话。

### 整理附注：不改写原始来源
解析二图片直接选择 $\alpha=(1,\sqrt3,0)$，因此用了 $|\alpha|=2$；这不是原题给出的条件，图片没有先论证这种选取对一般 $\alpha$ 的充分性。保留原图，不把这个取值写回题面。

原对话中的“不是未定式就直接代”应结合它实际使用的条件阅读：这里是分子、分母分别有极限，且分母极限不为零。原来的 $0/0$ 式不能直接赋值；模长求导式也应在向量不为零处使用。本题 $\alpha\ne\mathbf0$ 保证零点附近可用。


## 原图附件


### 题目原图

![28-12 / 57761 · 题目原图](assets/28-12_57761_question.png)

原文件：`CleanShot 2026-09-05 at 12.20.15@2x.png`；尺寸：1624 × 416；原附件 ID：`file_00000000eea88230ac06ad3387dcf114`；关联消息：T01。


### 解析一：有理化

![28-12 / 57761 · 解析一：有理化](assets/28-12_57761_solution_01.png)

原文件：`CleanShot 2026-09-05 at 12.23.01@2x.png`；尺寸：1640 × 2842；原附件 ID：`file_00000000f31081fda6e6fb6532d3c4d4`；关联消息：T01。


### 解析二：解析几何法

![28-12 / 57761 · 解析二：解析几何法](assets/28-12_57761_solution_02.png)

原文件：`CleanShot 2026-09-05 at 12.23.31@2x.png`；尺寸：1650 × 3032；原附件 ID：`file_00000000c83c81fd9c9b30e9126a298d`；关联消息：T01。



## 逐轮对话原文

以下为历史消息；保留当时说法，不用后来的正确结论覆盖。



### T01 · 用户

这道题我完全无从下手。

我算了一下 α 与 β 叉乘的模长，它等于 |α|·|β|·sin⟨α, β⟩。已知 sin⟨α, β⟩ = 1/2，|β| = 2，所以 |α × β| = |α|（这我知道）。

然后我就可以写成 lim (x→0) [|α + xβ| - |α × β|] / x。但接下来这个式子我不知道该怎么算：想把 α 和 β 提出去又提不出去，直接卡住了。

后面不管是按导数定义做，还是看成 0/0 型用洛必达法则：
如果用洛必达法则，分子该怎么求导？能导出来个什么东西？分母求导等于 1 我知道，但分子是个模长，对 x 求导后会出来一个 β 吗？因为 |α| 是常数求导就没了，而 α 后面带的是 xβ，导完难道就只剩 β 了？那它的模长就等于 2？这题答案直接等于 2，不可能吧？

这题确实不知道该怎么下手了



### T02 · 助手

你卡住的地方很典型。这道题真正的关键不是叉乘，而是**把“向量的模”转成“点积”**。

先纠正你前面一个小计算：

\[
\angle(\alpha,\beta)=\frac{\pi}{3}
\]

所以

\[
\sin\frac{\pi}{3}=\frac{\sqrt3}{2},
\qquad
\cos\frac{\pi}{3}=\frac12.
\]

因此

\[
|\alpha\times\beta|
=|\alpha||\beta|\sin\frac{\pi}{3}
=|\alpha|\cdot2\cdot\frac{\sqrt3}{2}
=\sqrt3|\alpha|,
\]

**并不是 \(|\alpha|\)**。

所以你不能把原题里的 \(|\alpha|\) 换成 \(|\alpha\times\beta|\)。

---

# 一、这道题最推荐的思路：分子有理化

原式：

\[
L=\lim_{x\to0}
\frac{|\alpha+x\beta|-|\alpha|}{x}.
\]

你说：

> \(\alpha\) 和 \(\beta\) 提不出去。

对，因为

\[
|\alpha+x\beta|
\]

本来就**不能像普通代数式那样提取 \(\alpha\)**。

原因是 \(\alpha,\beta\) 不是同方向的向量。只有类似

\[
|\alpha+x\alpha|
=|(1+x)\alpha|
=|1+x||\alpha|
\]

才能提。

所以看到

\[
|A|-|B|
\]

这种形式，尤其又是 \(0/0\)，一个非常自然的操作就是：

\[
\boxed{\text{乘 }(|A|+|B|)}
\]

也就是“平方差有理化”。

于是：

\[
L=
\lim_{x\to0}
\frac{|\alpha+x\beta|-|\alpha|}{x}
\cdot
\frac{|\alpha+x\beta|+|\alpha|}
{|\alpha+x\beta|+|\alpha|}.
\]

得到

\[
L=
\lim_{x\to0}
\frac{|\alpha+x\beta|^2-|\alpha|^2}
{x\left(|\alpha+x\beta|+|\alpha|\right)}.
\]

到这里是本题最关键的一步。

---

## 二、为什么平方以后突然就能算了？

因为向量模长平方有公式：

\[
\boxed{|u|^2=u\cdot u}
\]

所以

\[
|\alpha+x\beta|^2
=
(\alpha+x\beta)\cdot(\alpha+x\beta).
\]

展开：

\[
=\alpha\cdot\alpha
+2x\alpha\cdot\beta
+x^2\beta\cdot\beta.
\]

而

\[
|\alpha|^2=\alpha\cdot\alpha.
\]

因此相减以后：

\[
|\alpha+x\beta|^2-|\alpha|^2
=
2x\alpha\cdot\beta+x^2\beta\cdot\beta.
\]

代回去：

\[
L=
\lim_{x\to0}
\frac{2x\alpha\cdot\beta+x^2\beta\cdot\beta}
{x(|\alpha+x\beta|+|\alpha|)}.
\]

约掉 \(x\)：

\[
L=
\lim_{x\to0}
\frac{2\alpha\cdot\beta+x\beta\cdot\beta}
{|\alpha+x\beta|+|\alpha|}.
\]

现在就可以直接令 \(x\to0\)：

\[
L=
\frac{2\alpha\cdot\beta}
{2|\alpha|}
=
\frac{\alpha\cdot\beta}{|\alpha|}.
\]

接下来利用点积：

\[
\alpha\cdot\beta
=
|\alpha||\beta|\cos\frac{\pi}{3}.
\]

因此

\[
L
=
\frac{|\alpha||\beta|\cos\frac{\pi}{3}}
{|\alpha|}
=
|\beta|\cos\frac{\pi}{3}.
\]

已知

\[
|\beta|=2,
\]

所以

\[
L
=
2\times\frac12
=
\boxed{1}.
\]

---

# 三、你想到“导数定义”，其实完全正确

你其实离答案已经非常近了。

定义

\[
f(x)=|\alpha+x\beta|.
\]

那么

\[
f(0)=|\alpha|.
\]

于是题目原式正好就是

\[
\lim_{x\to0}
\frac{f(x)-f(0)}{x-0}.
\]

这不就是导数定义吗？

所以：

\[
\boxed{原极限=f'(0)}.
\]

你的问题就变成：

> \(|\alpha+x\beta|\) 对 \(x\) 怎么求导？

这正是你最困惑的地方。

---

# 四、为什么 \(|\alpha+x\beta|'\) 不是 \(|\beta|=2\)？

你刚才的想法大概是：

\[
(\alpha+x\beta)'=\beta
\]

于是猜：

\[
|\alpha+x\beta|'=|\beta|.
\]

**这里不能这么做。**

也就是说：

\[
\boxed{
\frac{d}{dx}|u(x)|
\neq
|u'(x)|
}
\]

一般情况下是不成立的。

最简单的反例：

\[
f(x)=|x|.
\]

如果按你的想法：

\[
f'(x)=|1|=1.
\]

但实际上：

\[
(|x|)'=
\begin{cases}
1,&x>0\\
-1,&x<0
\end{cases}
\]

显然不恒等于 \(1\)。

---

# 五、向量模长到底怎么求导？

设

\[
f(x)=|\alpha+x\beta|.
\]

先不要直接对模求导，而是写成平方根：

\[
|\alpha+x\beta|
=
\sqrt{(\alpha+x\beta)\cdot(\alpha+x\beta)}.
\]

令

\[
g(x)
=
(\alpha+x\beta)\cdot(\alpha+x\beta).
\]

那么

\[
f(x)=\sqrt{g(x)}.
\]

用链式法则：

\[
f'(x)
=
\frac{g'(x)}{2\sqrt{g(x)}}.
\]

而

\[
g(x)
=
\alpha\cdot\alpha
+2x\alpha\cdot\beta
+x^2\beta\cdot\beta.
\]

所以

\[
g'(x)
=
2\alpha\cdot\beta
+2x\beta\cdot\beta.
\]

于是

\[
f'(x)
=
\frac{
2\alpha\cdot\beta+2x\beta\cdot\beta
}{
2|\alpha+x\beta|
}.
\]

约掉 2：

\[
\boxed{
f'(x)
=
\frac{(\alpha+x\beta)\cdot\beta}
{|\alpha+x\beta|}
}
\]

这就是**向量模长函数的求导公式**。

所以 \(x=0\)：

\[
f'(0)
=
\frac{\alpha\cdot\beta}{|\alpha|}.
\]

再用点积：

\[
\alpha\cdot\beta
=
|\alpha||\beta|\cos\frac\pi3,
\]

得到：

\[
f'(0)
=
|\beta|\cos\frac\pi3
=
2\times\frac12
=
\boxed{1}.
\]

---

# 六、所以你用洛必达也完全可以

原式：

\[
\lim_{x\to0}
\frac{|\alpha+x\beta|-|\alpha|}{x}.
\]

是 \(0/0\) 型。

分母：

\[
x'=1.
\]

分子：

\[
\frac{d}{dx}
\left(|\alpha+x\beta|-|\alpha|\right)
=
\frac{(\alpha+x\beta)\cdot\beta}
{|\alpha+x\beta|}.
\]

所以洛必达：

\[
L
=
\lim_{x\to0}
\frac{(\alpha+x\beta)\cdot\beta}
{|\alpha+x\beta|}.
\]

令 \(x=0\)：

\[
L
=
\frac{\alpha\cdot\beta}{|\alpha|}
=
|\beta|\cos\frac\pi3
=
\boxed1.
\]

所以你的洛必达方向**没有问题**。

问题只出在你误以为：

\[
\boxed{
(|\alpha+x\beta|)'=|\beta|
}
\]

实际上应该是：

\[
\boxed{
(|\alpha+x\beta|)'
=
\frac{(\alpha+x\beta)\cdot\beta}
{|\alpha+x\beta|}
}
\]

---

# 七、这个公式其实有非常直观的几何意义

尤其值得理解。

\[
\frac{(\alpha+x\beta)\cdot\beta}
{|\alpha+x\beta|}
\]

把点积展开：

\[
=
\frac{
|\alpha+x\beta||\beta|\cos\theta
}
{|\alpha+x\beta|}
\]

所以

\[
\boxed{
\frac{d}{dx}|\alpha+x\beta|
=
|\beta|\cos\theta
}
\]

其中 \(\theta\) 是当前向量 \(\alpha+x\beta\) 与 \(\beta\) 的夹角。

在 \(x=0\)：

\[
\theta=\angle(\alpha,\beta)=\frac{\pi}{3}.
\]

因此：

\[
f'(0)
=
|\beta|\cos\frac\pi3
=
1.
\]

这句话的几何意义是：

> \(\beta\) 虽然本身长度是 2，但并不是它所有的“运动速度”都在增加 \(\alpha\) 的长度。

真正能够增加模长的，只是 \(\beta\) 在 \(\alpha\) 方向上的投影。

这个投影长度就是：

\[
|\beta|\cos\frac\pi3
=
2\times\frac12
=
1.
\]

所以你刚才问：

> “导完不是只剩一个 \(\beta\) 吗？那模长不就等于 2？”

这里可以抓住一句话：

\[
\boxed{\text{向量变化速度是 }\beta，
\quad\text{但模长变化速度是 }\beta\text{ 在当前向量方向上的投影。}}
\]

所以答案不是 \(2\)，而是

\[
2\cos60^\circ=1.
\]

---

## 这道题你最好记住两个“触发器”

以后看到：

\[
\frac{|A(x)|-|A(0)|}{x}
\]

第一反应可以有两个：

1. **分子有“两个模长相减”**  
   → 乘共轭：
   \[
   (|A(x)|-|A(0)|)(|A(x)|+|A(0)|)
   \]

2. **形式长得像**
   \[
   \frac{f(x)-f(0)}{x}
   \]
   → 想到：
   \[
   f'(0)
   \]

而这道题真正需要熟悉的桥梁公式是：

\[
\boxed{|u|^2=u\cdot u}
\]

以及

\[
\boxed{
u\cdot v=|u||v|\cos\theta
}
\]

**这里应该想到点积，而不是叉乘。**

你刚才的思路其实已经碰到了“向量长度变化率”这个核心，只是把“向量本身的导数 \(\beta\)”和“向量模长的导数”混在了一起。把这两个概念分开，这道题就顺了。



### T03 · 用户

# Selected text:

## Selection 1
于是：\[
L=
\lim_{x\to0}
\frac{|\alpha+x\beta|-|\alpha|}{x}
\cdot
\frac{|\alpha+x\beta|+|\alpha|}
{|\alpha+x\beta|+|\alpha|}.
\]得到\[
L=
\lim_{x\to0}
\frac{|\alpha+x\beta|^2-|\alpha|^2}
{x\left(|\alpha+x\beta|+|\alpha|\right)}.
\]

## Selection 2
约掉 \(x\)：\[
L=
\lim_{x\to0}
\frac{2\alpha\cdot\beta+x\beta\cdot\beta}
{|\alpha+x\beta|+|\alpha|}.
\]现在就可以直接令 \(x\to0\)：\[
L=
\frac{2\alpha\cdot\beta}
{2|\alpha|}
=
\frac{\alpha\cdot\beta}{|\alpha|}.
\]

## My request:
就是说，这个模长它是可以用平方差有理化，这个是有定义的，是吧？而且这里面 $\beta \cdot \beta$ 应该直接等于 0 吧？对，这个向量自己乘自己应该等于 0 啊。它等于零之后，x 后面直接没掉了呀，对吧？你不用令 x 等于 0 啊。

而且你这题为什么能让 x 直接等于 0 呢？我不是很理解。这题凭什么能让 x 直接等于 0？它明明有个 $x \times \beta$，对吧？你为什么让 x 等于 0 呢？它不是失去精度吗？你为什么可以让它 x 等于 0，然后把 $\beta$ 消掉？

我还是不懂。并且你后面提到的这个，它是 $f(x)$ 在零点的导数定义，然后你 $f(x)$ 等于 $\alpha$ 加上 $x$ 乘以 $\beta$ 的模长。那你这个求导你怎么求的？对，向量模长这个求导你怎么求的，我也不是很理解。

那这道题，你给我一个考试中最适合我的做法、最快最安全的做法，我这地方应该怎么做？



### T04 · 助手

先把你现在真正卡住的两个点纠正掉。**第一个断点就在这里：你把点积和叉积又混在一起了。**

本轮没有检索到指定 v5/v4 方法论资料中的精确条目，所以以下以当前题面、标准解析和已经核对过的向量规则为准。方法卡 ID：待匹配。

## 1. \(\beta\cdot\beta\) 绝对不等于 \(0\)

你说：

> 向量自己乘自己应该等于 0。

这里要分清“乘”是哪一种乘法。

### 点积自己

\[
\beta\cdot\beta
=
|\beta||\beta|\cos0
=
|\beta|^2.
\]

题目给

\[
|\beta|=2,
\]

所以

\[
\boxed{\beta\cdot\beta=4}.
\]

### 叉积自己

才是

\[
\beta\times\beta
=
\mathbf 0,
\]

因为

\[
|\beta\times\beta|
=
|\beta|^2\sin0=0.
\]

所以一定记成：

\[
\boxed{\beta\cdot\beta=|\beta|^2}
\]

\[
\boxed{\beta\times\beta=\mathbf 0}
\]

你之前的错题档案里也明确区分过：点积得到标量，而自身叉积才为零。fileciteturn2file0

---

# 2. 模长为什么可以“平方差有理化”？

可以，但不是因为“向量模长有一个特殊的有理化定义”。

而是因为：

\[
|\alpha+x\beta|
\]

算出来以后，本身就是一个**普通的非负实数**。

例如设

\[
A=|\alpha+x\beta|,\qquad B=|\alpha|.
\]

那么 \(A,B\) 都是实数。

当然满足普通代数恒等式：

\[
(A-B)(A+B)=A^2-B^2.
\]

所以：

\[
\frac{|\alpha+x\beta|-|\alpha|}{x}
\]

乘

\[
\frac{|\alpha+x\beta|+|\alpha|}
{|\alpha+x\beta|+|\alpha|}
\]

完全就是普通的平方差。

关键理解：

\[
\boxed{\text{模长里面是向量，但模长算出来是数。}}
\]

所以外层完全可以进行普通代数运算。

---

# 3. 你最不理解的：为什么后面可以“让 \(x=0\)”？

这里非常重要：

**我们不是在原式里面令 \(x=0\)。**

原式

\[
\frac{|\alpha+x\beta|-|\alpha|}{x}
\]

在 \(x=0\) 时就是

\[
\frac00,
\]

根本没有定义。

我们做的是：

> 先在 \(x\neq0\) 的条件下恒等变形，把造成 \(0/0\) 的那个 \(x\) 消掉；然后再求 \(x\to0\) 的极限。

看一个你最熟悉的例子：

\[
\lim_{x\to0}\frac{x^2+x}{x}.
\]

原式能不能直接令 \(x=0\)？

不能：

\[
\frac00.
\]

但是当 \(x\neq0\) 时，

\[
\frac{x^2+x}{x}=x+1.
\]

所以

\[
\lim_{x\to0}\frac{x^2+x}{x}
=
\lim_{x\to0}(x+1)
=
1.
\]

为什么最后能代 \(0\)？

因为化简后的

\[
x+1
\]

在 \(x=0\) 附近是连续的。

**你的这道题完全是同一回事。**

---

# 4. 我们重新走一遍，而且这次盯死每一个 \(x\)

原式：

\[
L=
\lim_{x\to0}
\frac{|\alpha+x\beta|-|\alpha|}{x}.
\]

先乘共轭：

\[
L=
\lim_{x\to0}
\frac{|\alpha+x\beta|^2-|\alpha|^2}
{x\left(|\alpha+x\beta|+|\alpha|\right)}.
\]

现在用

\[
|u|^2=u\cdot u.
\]

于是分子：

\[
|\alpha+x\beta|^2
=
(\alpha+x\beta)\cdot(\alpha+x\beta).
\]

展开：

\[
=
\alpha\cdot\alpha
+x\alpha\cdot\beta
+x\beta\cdot\alpha
+x^2\beta\cdot\beta.
\]

因为点积满足

\[
\alpha\cdot\beta=\beta\cdot\alpha,
\]

所以：

\[
=
\alpha\cdot\alpha
+2x\alpha\cdot\beta
+x^2\beta\cdot\beta.
\]

再减去

\[
|\alpha|^2=\alpha\cdot\alpha,
\]

得到：

\[
2x\alpha\cdot\beta+x^2\beta\cdot\beta.
\]

注意！

这里

\[
\boxed{\beta\cdot\beta=4}
\]

而不是 0。

于是实际上就是：

\[
2x\alpha\cdot\beta+4x^2.
\]

提一个 \(x\)：

\[
=x(2\alpha\cdot\beta+4x).
\]

和分母的 \(x\) 约掉：

\[
L=
\lim_{x\to0}
\frac{2\alpha\cdot\beta+4x}
{|\alpha+x\beta|+|\alpha|}.
\]

### 到这里才可以直接取极限。

因为现在分母趋向：

\[
|\alpha+0\beta|+|\alpha|
=
2|\alpha|.
\]

而题目明确说 \(\alpha\) 是非零向量，所以

\[
2|\alpha|\neq0.
\]

已经没有 \(0/0\) 了。

所以正常代入即可：

\[
L=
\frac{2\alpha\cdot\beta}
{2|\alpha|}
=
\frac{\alpha\cdot\beta}{|\alpha|}.
\]

---

# 5. 那 \(x\beta\) 为什么可以“消失”？会不会失去精度？

不会。

因为 \(\beta\) 是固定向量，而

\[
x\to0.
\]

所以：

\[
|x\beta|
=
|x||\beta|
=
2|x|
\to0.
\]

因此

\[
x\beta\to\mathbf 0.
\]

所以

\[
\alpha+x\beta\to\alpha.
\]

自然有：

\[
|\alpha+x\beta|\to|\alpha|.
\]

这不是“近似以后随手删掉”，而是**严格的极限运算**。

同样：

\[
x\beta\cdot\beta
=
4x\to0.
\]

所以这一项最终消失。

但注意，**\(\beta\) 并没有全没掉。**

前面的

\[
\alpha\cdot\beta
\]

仍然保留着 \(\beta\)。

最后正是靠：

\[
\alpha\cdot\beta
=
|\alpha||\beta|\cos\frac\pi3
\]

继续算。

所以不是：

> \(x=0\)，于是 \(\beta\) 被消掉了。

而是：

> 凡是前面乘了 \(x\) 的项，在 \(x\to0\) 时趋于 0；没有乘 \(x\) 的 \(\alpha\cdot\beta\) 仍然保留。

这两个概念必须分开。

---

# 6. 考试里，你这道题最快、最安全的方法

对你而言，我**不建议第一选择洛必达，也不建议先想模长求导公式**。

这道题就走一条非常固定的动作链：

\[
\boxed{
\text{模长之差}
\rightarrow
\text{乘共轭}
\rightarrow
|u|^2=u\cdot u
\rightarrow
\text{展开点积}
\rightarrow
\text{约掉 }x
\rightarrow
\text{代极限}
}
\]

考试直接这么写：

\[
\begin{aligned}
L
&=
\lim_{x\to0}
\frac{|\alpha+x\beta|-|\alpha|}{x}\\
&=
\lim_{x\to0}
\frac{|\alpha+x\beta|^2-|\alpha|^2}
{x\left(|\alpha+x\beta|+|\alpha|\right)}\\
&=
\lim_{x\to0}
\frac{2x\alpha\cdot\beta+x^2\beta\cdot\beta}
{x\left(|\alpha+x\beta|+|\alpha|\right)}\\
&=
\lim_{x\to0}
\frac{2\alpha\cdot\beta+x\beta\cdot\beta}
{|\alpha+x\beta|+|\alpha|}\\
&=
\frac{\alpha\cdot\beta}{|\alpha|}\\
&=
|\beta|\cos\frac{\pi}{3}\\
&=
\boxed{1}.
\end{aligned}
\]

这条路线你考试里优先用。

---

# 7. 至于“向量模长到底怎么求导”

你也需要搞懂，但可以当成第二套方法。

设

\[
f(x)=|\alpha+x\beta|.
\]

千万不要写成：

\[
f'(x)=|\beta|.
\]

正确做法是**先把模长改写成根号**：

\[
f(x)
=
\sqrt{(\alpha+x\beta)\cdot(\alpha+x\beta)}.
\]

展开：

\[
f(x)
=
\sqrt{
\alpha\cdot\alpha
+2x\alpha\cdot\beta
+x^2\beta\cdot\beta
}.
\]

现在里面全是普通的关于 \(x\) 的函数了。

求导：

\[
f'(x)
=
\frac{
2\alpha\cdot\beta
+2x\beta\cdot\beta
}{
2\sqrt{
\alpha\cdot\alpha
+2x\alpha\cdot\beta
+x^2\beta\cdot\beta
}
}.
\]

因此：

\[
\boxed{
f'(x)=
\frac{
\alpha\cdot\beta+x\beta\cdot\beta
}{
|\alpha+x\beta|}
}
\]

也可以写成：

\[
\boxed{
f'(x)
=
\frac{(\alpha+x\beta)\cdot\beta}
{|\alpha+x\beta|}
}.
\]

到了 \(x=0\)：

\[
f'(0)
=
\frac{\alpha\cdot\beta}{|\alpha|}.
\]

所以导数法最终和刚才有理化法完全一样。

但你现在考试里先记：

\[
\boxed{\text{这题优先有理化，不优先洛必达。}}
\]

因为有理化只需要你会两个最基础的东西：

\[
|u|^2=u\cdot u,
\qquad
u\cdot v=|u||v|\cos\theta.
\]

失误点更少。

---

现在我只确认你这一个断点：

\[
\boxed{\beta\cdot\beta\quad\text{和}\quad\beta\times\beta}
\]

你现在分别认为它们等于什么？



### T05 · 用户

# Selected text:

## Selection 1
\(L=
\lim_{x\to0}
\frac{2\alpha\cdot\beta+4x}
{|\alpha+x\beta|+|\alpha|}.\)

## My request:
这题我也不懂。它分子明明有个 4x，你凭什么让 x 趋向于 0，让这个 4x 直接消掉呢？我印象中这是不能做到的，为什么这道题可以这么做呢？

然后你是拆完之后，拆成了两个部分：

1. 第一个部分是 2|α|x 分之 2x · α · β
2. 另一个部分是 2|α|x 分之 x² · β²

因为分子比分母高次，所以直接等于 0。

我可以这么理解吗？把它们拆开之后，因为分子比分母高次，所以直接等于 0，对吧？



### T06 · 助手

你现在这个理解已经**接近了**，但要把一句话改准确：

> **不是“看到 \(4x\) 就随便把 \(x=0\)”；而是化简后，这个极限已经不再是未定式，所以可以按极限四则运算/连续性直接取极限。**

这正好对应方法卡 **H01-001：极限计算总流程**——先判断是不是未定式；**若已经不是未定式，就可以直接用连续性或极限四则运算。**

---

## 先看你现在卡的这一行

\[
L=
\lim_{x\to0}
\frac{2\alpha\cdot\beta+4x}
{|\alpha+x\beta|+|\alpha|}.
\]

现在分别看分子、分母：

\[
2\alpha\cdot\beta+4x
\longrightarrow
2\alpha\cdot\beta+0,
\]

因为

\[
\lim_{x\to0}4x=0.
\]

分母：

\[
|\alpha+x\beta|+|\alpha|
\longrightarrow
|\alpha|+|\alpha|
=
2|\alpha|.
\]

而题目告诉你 \(\alpha\neq \mathbf0\)，所以

\[
2|\alpha|\neq0.
\]

因此现在整个式子是：

\[
\frac{\text{一个有限数}}
{\text{一个非零的有限数}}.
\]

**已经不是 \(0/0\) 了。**

所以可以直接使用极限四则运算：

\[
L
=
\frac{2\alpha\cdot\beta}{2|\alpha|}.
\]

---

# 你真正要区分的是这两种情况

### 情况一：原式直接代 \(x=0\)

原题：

\[
\frac{|\alpha+x\beta|-|\alpha|}{x}.
\]

代 \(x=0\)：

\[
\frac{|\alpha|-|\alpha|}{0}
=
\frac00.
\]

这是未定式。

所以：

\[
\boxed{\text{这里不能直接代。}}
\]

---

### 情况二：有理化、约掉 \(x\) 以后

变成：

\[
\frac{2\alpha\cdot\beta+4x}
{|\alpha+x\beta|+|\alpha|}.
\]

再代趋势：

\[
\frac{2\alpha\cdot\beta+0}
{2|\alpha|}.
\]

分母不为 0。

所以：

\[
\boxed{\text{这里就可以直接取极限。}}
\]

你不要记成“极限里不能令 \(x=0\)”。

这个记忆是错的。

应该记：

\[
\boxed{
\text{先代趋势判断。若没有出现未定式，就直接算；出现未定式才继续变形。}
}
\]

---

## 那你说的“拆成两个部分”可不可以？

**可以，而且你的第二部分理解基本正确。**

从这里：

\[
L=
\lim_{x\to0}
\frac{
2x\alpha\cdot\beta+x^2\beta\cdot\beta
}{
x(|\alpha+x\beta|+|\alpha|)
}.
\]

你可以拆：

\[
L=
\lim_{x\to0}
\frac{2x\alpha\cdot\beta}
{x(|\alpha+x\beta|+|\alpha|)}
+
\lim_{x\to0}
\frac{x^2\beta\cdot\beta}
{x(|\alpha+x\beta|+|\alpha|)}.
\]

分别约掉 \(x\)。

第一部分：

\[
\lim_{x\to0}
\frac{2\alpha\cdot\beta}
{|\alpha+x\beta|+|\alpha|}
=
\frac{\alpha\cdot\beta}{|\alpha|}.
\]

第二部分：

\[
\lim_{x\to0}
\frac{x\beta\cdot\beta}
{|\alpha+x\beta|+|\alpha|}.
\]

因为

\[
\beta\cdot\beta=4,
\]

所以就是

\[
\lim_{x\to0}
\frac{4x}
{|\alpha+x\beta|+|\alpha|}
=
0.
\]

### 你可以把第二项理解成：

分子是 \(x^2\) 量级，原来的分母是 \(x\) 量级，

所以

\[
\frac{x^2}{x}\sim x\to0.
\]

因此第二项为 \(0\)。

**这一理解是对的。**

---

## 但“分子比分母高次，所以等于 0”这句话要加一个限制

不要泛化成：

> 只要分子次数比分母高，极限就是 0。

应该说：

> 当 \(x\to0\) 时，如果分子是比比分母**更高阶的无穷小**，那么它们的比值趋于 \(0\)。

例如：

\[
\frac{x^2}{x}=x\to0.
\]

这里：

- \(x^2\) 是二阶无穷小；
- \(x\) 是一阶无穷小；

所以

\[
x^2=o(x),
\]

于是：

\[
\frac{x^2}{x}\to0.
\]

这才是你脑子里那条规律的准确版本。

---

# 而且我更建议你考试时不要拆

你的拆法没错，但这题最安全的是：

\[
\frac{2x\alpha\cdot\beta+x^2\beta\cdot\beta}
{x(|\alpha+x\beta|+|\alpha|)}
\]

直接把分子提 \(x\)：

\[
=
\frac{x(2\alpha\cdot\beta+x\beta\cdot\beta)}
{x(|\alpha+x\beta|+|\alpha|)}.
\]

约掉：

\[
=
\frac{2\alpha\cdot\beta+x\beta\cdot\beta}
{|\alpha+x\beta|+|\alpha|}.
\]

然后**重新判断一次极限类型**：

\[
x\to0
\]

时，

\[
\text{分子}\to2\alpha\cdot\beta,
\]

\[
\text{分母}\to2|\alpha|\neq0.
\]

不是未定式，直接代趋势。

这一套考试里最稳。

---

所以你现在可以这样理解整道题：

\[
\boxed{
\frac00
\overset{\text{有理化}}{\longrightarrow}
\frac{x(\cdots)}{x(\cdots)}
\overset{\text{约 }x}{\longrightarrow}
\frac{\text{有限量}+4x}{\text{趋于非零常数}}
}
\]

到了最后这一步，**\(4x\to0\) 就只是最普通的极限 \(4x\to0\)**，没有任何“损失精度”。

我现在只确认你这一点：**如果极限化简以后变成 \(\displaystyle\lim_{x\to0}\frac{3+4x}{2+x}\)，你认为能不能直接代 \(x=0\)？为什么？**



### T07 · 用户

好，这道题可以直接代 $x=0$，因为它们不是未定式。分子代 $x=0$ 之后是等于 3，分母代 $x=0$ 是等于 2，所以它不是未定式，直接代 $x=0$ 这道题就等于二分之三。

好，那这道题我们就讲完了。



### T08 · 助手

对，这个判断完全正确：

\[
\lim_{x\to0}\frac{3+4x}{2+x}
=
\frac{3}{2},
\]

因为代入后分母不为 \(0\)，不存在未定式，直接代即可。

这道题收尾只记住三个点：

1. \(\beta\cdot\beta=|\beta|^2\)，而 \(\beta\times\beta=\mathbf 0\)，不要混淆。
2. 看到
   \[
   |\alpha+x\beta|-|\alpha|
   \]
   这种**模长之差**，考试优先考虑乘共轭有理化，再利用
   \[
   |u|^2=u\cdot u.
   \]
3. 极限不是“永远不能代 \(x=0\)”；而是**先代趋势判断**。如果得到正常有限值，就直接算；如果得到 \(0/0\)、\(\infty/\infty\) 等未定式，再继续变形。

这道题你属于**在局部提示和纠正后完成理解**，尤其是“什么时候可以直接代极限”这个断点现在已经打通了。
