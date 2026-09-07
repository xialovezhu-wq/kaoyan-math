28-2｜ID:57858

## 同时垂直于两向量与数量投影确定未知向量

### 原题图

![ID 57858 原题](assets/id_57858_question.png)

### 官方解析图

![ID 57858 官方解析](assets/id_57858_official_solution.png)

### 对话中生成的辅助图：数量投影与 cosθ

![数量投影与 cosθ 示意图](assets/projection_cos_theta_infographic.png)

### 题面转写

设

\[
\mathbf a=(2,-3,1),\qquad \mathbf b=(1,-2,3),\qquad \mathbf c=(2,1,2).
\]

向量 \(\mathbf r\) 满足

\[
\mathbf r\perp\mathbf a,\qquad \mathbf r\perp\mathbf b,
\]

且

\[
\operatorname{Prj}_{\mathbf c}\mathbf r=14.
\]

求 \(\mathbf r\)。

### 官方答案

**\(\mathbf r=(14,10,2)\)。**

### 官方主线步骤（文本化）

由

\[
\mathbf r\perp\mathbf a,\qquad \mathbf r\perp\mathbf b
\]

可知 \(\mathbf r\) 与 \(\mathbf a\times\mathbf b\) 共线，因此设

\[
\mathbf r=k(\mathbf a\times\mathbf b).
\]

计算

\[
\mathbf a\times\mathbf b=(-7,-5,-1),
\]

故

\[
\mathbf r=(-7k,-5k,-k).
\]

再由数量投影条件

\[
\operatorname{Prj}_{\mathbf c}\mathbf r
=\frac{\mathbf r\cdot\mathbf c}{|\mathbf c|}=14
\]

以及 \(|\mathbf c|=3\)，得

\[
\frac{(-7k,-5k,-k)\cdot(2,1,2)}{3}
=\frac{-21k}{3}=-7k=14.
\]

所以 \(k=-2\)，最终

\[
\mathbf r=(14,10,2).
\]

### 涉及知识点

- Prj_c r 在本题中表示 r 在 c 方向上的数量投影（标量投影/有向投影长度），不是 |c|。
- 数量投影公式：Prj_c r=(r·c)/|c|=|r|cosθ。
- cosθ=邻边/斜边；向量夹角 θ 一般取 0≤θ≤π，不一定是锐角。钝角时数量投影为负。
- r⊥a 且 r⊥b 不能推出 a∥b；在 a、b 不共线时，r 必与 a×b 共线。
- 叉乘 a×b 负责确定 r 的方向；投影条件负责确定比例系数 k。
- 若题目要求向量投影，则公式为 proj_c r=((r·c)/|c|²)c；本题官方记号采用数量投影。

**项目方法论匹配：** 交叉乘方向识别可参考 H17-006；“共同垂直方向 + 数量投影定倍数”的精确方法卡 ID：待匹配。

### 用户断点与掌握状态

- **已独立做对/理解的部分：** 用户能够正确复述数量投影为 (r·c)/|c|，并理解投影条件可用于求比例倍数。
- **第一个真正断点：** 不清楚 Prj 的对象角色；误以为 r 同时垂直于 a、b 能推出 a、b 平行；未识别“共同垂直方向”应触发叉乘。
- **本轮纠正后：** 已经复述完整动作链：a×b 得到同时垂直于 a、b 的方向；r=k(a×b)；投影条件求 k。
- **当前状态：** 完整讲解后已理解，并能正确解释方法机制。

### 完整对话记录

#### 1. 用户

在这道题中，我不理解题目提到的 \(\text{prj}_{\vec{c}}\vec{r}\) 是什么意思。这指的是 \(\vec{c}\) 的模长吗？还是指别的什么？如果是 \(\vec{c}\) 的模长，干嘛不直接用绝对值符号把 \(\vec{c}\) 框住呢？
另外，这道题里向量 \(\vec{r}\) 满足 \(\vec{r} \perp \vec{a}\) 且 \(\vec{r} \perp \vec{b}\)，那我能判断出 \(\vec{a}\) 和 \(\vec{b}\) 是平行的吗？
至于这道题的 \(\vec{r}\) 具体该怎么求，我不是很清楚，目前没有什么思路。

#### 2. 助手

你这里有两个概念断点，我先只把它们理清，不急着把整题算完。

### 1. \(\operatorname{Prj}_{\vec c}\vec r\) 不是 \(|\vec c|\)

它表示：

\[
\boxed{\vec r\text{ 在 }\vec c\text{ 方向上的投影长度}}
\]

通常这里是**数量投影**，也就是一个数。

公式是

\[
\operatorname{Prj}_{\vec c}\vec r
=
|\vec r|\cos\theta
=
\frac{\vec r\cdot \vec c}{|\vec c|}
\]

其中 \(\theta\) 是 \(\vec r\) 与 \(\vec c\) 的夹角。

所以题目

\[
\operatorname{Prj}_{\vec c}\vec r=14
\]

意思是：

> 向量 \(\vec r\) 沿着 \(\vec c\) 这个方向“投过去”，得到的有向长度是 \(14\)。

它和

\[
|\vec c|
\]

完全是两回事。

\[
|\vec c|
\]

才表示 \(\vec c\) 自己的模长。

你可以先这样区分：

\[
\boxed{
|\vec c|=\text{向量 }\vec c\text{ 自己有多长}
}
\]

\[
\boxed{
\operatorname{Prj}_{\vec c}\vec r
=\text{向量 }\vec r\text{ 在 }\vec c\text{ 方向上有多长}
}
\]

---

### 2. \(\vec r\perp\vec a,\ \vec r\perp\vec b\)，不能推出 \(\vec a\parallel\vec b\)

这个判断不成立。

例如在三维空间里：

\[
\vec a=(1,0,0),\qquad
\vec b=(0,1,0),
\]

它们显然不平行。

但

\[
\vec r=(0,0,1)
\]

同时满足

\[
\vec r\perp\vec a,\qquad
\vec r\perp\vec b.
\]

所以“同一个向量同时垂直于两个向量”，并不要求那两个向量平行。

反而这里真正应该触发的是你上一题刚用过的**叉乘**：

\[
\vec a\times\vec b
\]

有一个很重要的性质：

\[
\vec a\times\vec b\perp\vec a,
\qquad
\vec a\times\vec b\perp\vec b.
\]

而题目告诉你

\[
\vec r\perp\vec a,\qquad
\vec r\perp\vec b.
\]

因此，在 \(\vec a,\vec b\) 不共线的情况下，

\[
\boxed{\vec r\parallel \vec a\times\vec b}
\]

这就是这道题的**第一动作**。

所以先不要去管那个 \(14\)。

你现在只做一步：

\[
\vec a=(2,-3,1),\qquad
\vec b=(1,-2,3),
\]

你能不能先算出

\[
\boxed{\vec a\times\vec b}
\]

是多少？

#### 3. 用户

# Selected text:

## Selection 1
\(\operatorname{Prj}_{\vec c}\vec r
=
|\vec r|\cos\theta
=
\frac{\vec r\cdot \vec c}{|\vec c|}\)

## My request:
这部分我不是很懂啊，它 r 在 c 方向的投影长度。

那我假设一个坐标轴对吧，纵坐标是 c，即 x、y。然后这个 r 就在第一象限，它投影下去，这个 θ 指的是个锐角是吧？

你把这个 cosθ 画个图给我看一下，这个 cosθ 指的值是什么？我记得 cosθ 是邻边比斜边对吧？就邻边去除以斜边，还是邻边除以邻边，还是斜边除以邻边？这个我不太熟悉，这是什么东西？

#### 4. 助手

生成并返回了一张“向量 \(\mathbf r\) 在 \(\mathbf c\) 方向上的数量投影与 \(\cos\theta\)”示意图。图中明确标注：

- \(\cos\theta=\dfrac{\text{邻边}}{\text{斜边}}\)；
- 邻边长度为 \(|\mathbf r|\cos\theta\)；
- \(\theta\) 是两向量夹角，通常取 \(0\le\theta\le\pi\)，不一定是锐角；
- 锐角时投影为正，直角时为 0，钝角时为负。

示意图原图见本题“辅助图”。

#### 5. 用户

移除此图像的背景。保持所有前景主体不变且完整，边缘干净平滑。将背景设为透明。

#### 6. 记录

该条为图像编辑操作请求，不包含新的数学推导；在随后继续数学讨论前，当前对话中没有形成独立的助手文字答复。

#### 7. 用户

这道题我大概懂了。它这个投影就是告诉我，R 跟 C 的点乘除以 C 的模长（即 R 在 C 方向的投影长度）是等于 14 的，然后题目问这个 R 的向量是多少。

到底要怎么算呢？你把这道题的步骤说一下：

1. 我为什么要算 A 跟 B 的叉乘？
2. 叉乘求出来的这个向量指的是什么东西？为什么要算这个？
3. 这个东西跟我最后的 R 有什么关系呢？

#### 8. 助手

对，你现在对投影条件已经理解了。你这道题真正缺的是：**为什么一看到 \(\vec r\perp\vec a,\ \vec r\perp\vec b\)，就要想到 \(\vec a\times\vec b\)**。

本轮项目资料检索没有成功匹配到这道“空间向量叉乘 + 投影”的对应方法卡，所以我直接根据当前题面把这条逻辑讲清楚。

## 先看题目到底给了什么

\[
\vec a=(2,-3,1),\qquad
\vec b=(1,-2,3),\qquad
\vec c=(2,1,2)
\]

未知的是

\[
\boxed{\vec r}
\]

它满足三个条件：

\[
\vec r\perp\vec a,
\]

\[
\vec r\perp\vec b,
\]

以及

\[
\operatorname{Prj}_{\vec c}\vec r=14.
\]

其实前两个条件负责确定 **\(\vec r\) 的方向**，最后一个条件负责确定 **\(\vec r\) 到底有多长、朝正方向还是反方向**。

---

# 1. 为什么要算 \(\vec a\times\vec b\)？

因为叉乘有一个核心性质：

\[
\boxed{
\vec a\times\vec b
\text{ 同时垂直于 }\vec a\text{ 和 }\vec b
}
\]

而题目恰好告诉你：

\[
\boxed{
\vec r\text{ 也同时垂直于 }\vec a\text{ 和 }\vec b
}
\]

所以它们拥有相同的方向特征。

你可以这样理解：

\[
\vec a,\vec b
\]

这两个不共线向量可以张成一个平面。

那么

\[
\vec r\perp\vec a,\qquad \vec r\perp\vec b
\]

实际上就是说：

\[
\vec r
\]

垂直于这个由 \(\vec a,\vec b\) 张成的平面。

而

\[
\vec a\times\vec b
\]

恰恰就是这个平面的**法向量**。

因此自然得到：

\[
\boxed{\vec r\parallel(\vec a\times\vec b)}
\]

这就是为什么要算叉乘。

---

# 2. \(\vec a\times\vec b\) 算出来到底是什么？

算：

\[
\vec a\times\vec b
=
\begin{vmatrix}
\vec i&\vec j&\vec k\\
2&-3&1\\
1&-2&3
\end{vmatrix}
\]

得到

\[
\vec a\times\vec b=(-7,-5,-1).
\]

这个

\[
\boxed{(-7,-5,-1)}
\]

不是最后的 \(\vec r\)。

它只是告诉你：

> **所有同时垂直于 \(\vec a,\vec b\) 的向量，都沿着 \((-7,-5,-1)\) 这条方向。**

所以 \(\vec r\) 只能长成：

\[
\boxed{
\vec r=k(-7,-5,-1)
}
\]

也就是

\[
\vec r=(-7k,-5k,-k).
\]

这里 \(k\) 是一个实数。

为什么还要有 \(k\)？

因为光知道“方向”是不够的。

比如

\[
(-7,-5,-1)
\]

和

\[
(-14,-10,-2)
\]

以及

\[
(7,5,1)
\]

全都同时垂直于 \(\vec a,\vec b\)。

它们只是**长度、正反方向不同**。

---

# 3. 那最后的投影条件是干什么的？

这时候你已经把未知向量从

\[
\vec r=(x,y,z)
\]

三个未知数，压缩成了：

\[
\boxed{\vec r=k(-7,-5,-1)}
\]

只剩一个未知数 \(k\)。

然后题目再告诉你：

\[
\operatorname{Prj}_{\vec c}\vec r=14.
\]

你刚刚已经理解这个公式：

\[
\operatorname{Prj}_{\vec c}\vec r
=
\frac{\vec r\cdot\vec c}{|\vec c|}.
\]

所以代入：

\[
\frac{k(-7,-5,-1)\cdot(2,1,2)}
{|(2,1,2)|}
=14.
\]

先算点乘：

\[
(-7,-5,-1)\cdot(2,1,2)
=
-14-5-2
=
-21.
\]

再算

\[
|\vec c|
=
\sqrt{2^2+1^2+2^2}
=
3.
\]

于是：

\[
\frac{-21k}{3}=14,
\]

即

\[
-7k=14.
\]

所以

\[
k=-2.
\]

最终：

\[
\vec r
=
-2(-7,-5,-1)
=
\boxed{(14,10,2)}.
\]

---

## 这道题以后看到就按这条链走

最值得你记的是这个：

\[
\boxed{
\vec r\perp\vec a,\quad
\vec r\perp\vec b
}
\]

看到这里马上想到：

\[
\boxed{
\vec r\parallel\vec a\times\vec b
}
\]

于是第一动作：

\[
\boxed{
\vec r=k(\vec a\times\vec b)
}
\]

然后剩下的条件——这题是投影条件——就是拿来**求 \(k\)** 的。

所以这道题可以拆成非常清楚的两步：

\[
\boxed{
\text{叉乘确定方向}
\quad\longrightarrow\quad
\text{投影确定倍数}
}
\]

你现在只需要确认一个地方：**为什么我们不能直接说 \(\vec r=\vec a\times\vec b\)，而必须写成 \(\vec r=k(\vec a\times\vec b)\)？**

#### 9. 用户

哦，我懂了。

这个隐含条件就是说，它告诉你 R 垂直于 a，又 R 垂直于 b，然后 a 跟 b 的叉乘（外积）刚好就满足条件。因为 a 跟 b 叉乘得出来的向量，是既垂直于 a 又垂直于 b 的，对吧？

所以说得到的这个 R 是某个方向向量的比例，然后它告诉你了这个 R 在 c 方向的投影是 14，就可以通过这个投影来确定具体的倍数，对吧？

那我懂了，这道题没问题了

---
