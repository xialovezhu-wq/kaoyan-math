ID:57981｜直线在平面上的投影

## 题面转写

来源：`assets/29-04_57981_question.png`。

求直线

\[
L : \frac{x+2}{3}=\frac{2-y}{1}=\frac{z+1}{2}
\]

在平面

\[
\Pi:2x+3y+3z-8=0
\]

上的投影直线方程。

## 涉及的知识点与两种解析

来源：本题两张解析图及 T01—T06。

**知识点：** 空间直线的点向式与参数式；方向向量和法向量的角色；直线的正投影与向量投影长度的区别；平面束；两个平面的交线；垂直条件的数量积表达；由两个不同点确定直线。

**解析一：辅助平面法。** 把原直线写为两个平面的交线：

\[
\begin{cases}
x+3y-4=0,\\
2x-3z+1=0.
\end{cases}
\]

设过原直线的辅助平面为

\[
x+3y-4+\lambda(2x-3z+1)=0.
\]

其法向量为 \((1+2\lambda,3,-3\lambda)\)。由该平面与 \(\Pi\) 垂直，解析列出

\[
(1+2\lambda,3,-3\lambda)\cdot(2,3,3)=0,
\qquad \lambda=\frac{11}{5}.
\]

所求投影直线为

\[
\boxed{\begin{cases}
9x+5y-11z-3=0,\\
2x+3y+3z-8=0.
\end{cases}}
\]

**解析二：两个投影点法。** 先求原直线与 \(\Pi\) 的交点 \(O=(1,1,1)\)，再取原直线上 \(A=(4,0,3)\)，求其在 \(\Pi\) 上的垂足

\[
A'=\left(\frac{35}{11},-\frac{27}{22},\frac{39}{22}\right).
\]

题库给出的另一形式为

\[
\boxed{\frac{x-1}{48}=\frac{y-1}{-49}=\frac{z-1}{17}}.
\]

## 学习过程与证据

用户起初将目标理解为“投影长度”，并把直线点向式读出的向量称作法向量；读取 \(2-y\) 时还把对应方向分量写成 \(+1\)。助手在 T02 说明原直线方向可取 \((3,-1,2)\)，投影问题要确定的是一条直线的位置与方向。

T03 的核心困难是无法想象“一个包含斜直线、又垂直于已知平面的辅助平面”。作图后用户在 T05 表示“这道题没问题”。**现有证据支持：经过解释和图示后，用户表示理解；没有展示该题完整独立重做。**

## 原图与历史回复的使用提示

以下提示不替换原图或原话：

- 作图回合最后的明确要求是“以最后这张按本题几何关系绘制的图为准”，因此 `geometry_final.png` 是该回合最终采用的示意图；前三张仍作为历史资料保存。
- 早期生成图一出现“两个垂直平面的法向量平行”的文字，与本题解析中的法向量内积为零相冲突，不应作为公式依据。
- 早期生成图二、图三有把本题结论推广到一般直线的文字，且图三对非退化情形的表述不严谨；这些图的文字不是题库解析。不得从“直线不平行于平面”单独推出其正投影一定为直线。
- 本题没有给出一段具有固定端点的线段；方向向量的模不是“整条空间直线的长度”。这对应 T01—T02 中目标对象的区分。


## 题目与解析图

::: {.gallery}



![29-4 / 57981｜题目](assets/29-04_57981_question.png)

图片路径：`assets/29-04_57981_question.png`；尺寸：1616 × 386；状态：原文件，逐字节保留。



![29-4 / 57981｜解析一：辅助平面](assets/29-04_57981_solution_01.png)

图片路径：`assets/29-04_57981_solution_01.png`；尺寸：1602 × 3430；状态：原文件，逐字节保留。



![29-4 / 57981｜解析二：两个投影点](assets/29-04_57981_solution_02.png)

图片路径：`assets/29-04_57981_solution_02.png`；尺寸：1640 × 5440；状态：原文件，逐字节保留。


:::


## 本题完整对话

> 以下保持历史原话，包括错误结果、后续纠正、用户反馈和原有引用标记。



::: {.message .user #T01}

### T01｜用户

**归档附记：本条消息原附件顺序**

1. `assets/29-04_57981_solution_01.png`。
2. `assets/29-04_57981_question.png`。
3. `assets/29-04_57981_solution_02.png`。

**对话正文（原文）**

这道题题目有两个解析图，我有点不懂。它要求投影直线方程，我有点无从下手。

我好像看错题了，我之前一直在求投影的长度。求投影长度的话，投影长度等于 r 乘以 cosθ 对吧？而 cosθ 等于 (|r|·|m|) 分之 |r×m|。这里的 m 是平面的法向量，r 是直线的方向向量。然后这道题我通过直线的表达式得到法向量是 (3, 1, 2)，通过平面的表达式得到法向量是 (2, 3, 3)，那我得不到直线 L 的方向向量，连长度都求不出来。

而且我后面发现它其实不求长度，而是求投影直线方程。这就更不知该从何下手了，你看这道题我真不知道怎么做。

:::



::: {.message .assistant #T02}

### T02｜助手

你现在真正卡住的不是计算，而是**对象角色混了**。先把最前面的两个点纠正掉，后面的路就出来了。

你之前整理过类似的“投影直线 ≠ 投影长度”这个区别，本题本质上还是同一个断点：要求的是投影以后那条直线的位置和方向，而不是某个向量投影后有多长。fileciteturn1file0

### 先纠正你这里一个很关键的地方

直线

\[
L : \frac{x+2}{3}=\frac{2-y}{1}=\frac{z+1}{2}
\]

这里直接给出来的是：

- 一个**定点**；
- 一个**方向向量**。

它**不是在给法向量**。

令三者都等于 \(t\)：

\[
\begin{cases}
x=3t-2,\\
y=2-t,\\
z=2t-1.
\end{cases}
\]

所以直线 \(L\) 的方向向量其实是

\[
\boxed{\boldsymbol d=(3,-1,2)}
\]

注意中间是 \(-1\)，因为

\[
y=2-t.
\]

而平面

\[
\Pi:2x+3y+3z-8=0
\]

的法向量才是

\[
\boxed{\boldsymbol n=(2,3,3)}.
\]

所以你说“我得不到直线 \(L\) 的方向向量”这一点，其实恰恰相反：**题目已经直接把方向向量给你了。**

---

### 你关于“投影长度”的公式，也顺手校准一下

如果 \(\theta\) 表示**直线方向与平面的夹角**，那么

\[
|\boldsymbol d|\cos\theta
\]

确实是方向向量在平面上的投影长度。

而

\[
\cos\theta
=
\frac{|\boldsymbol d\times \boldsymbol n|}
{|\boldsymbol d||\boldsymbol n|}
\]

在这个定义下也是对的。

因为 \(\boldsymbol d\times\boldsymbol n\) 里面出现的是“\(\boldsymbol d\) 与法向量 \(\boldsymbol n\) 的夹角”的正弦，而它恰好等于“\(\boldsymbol d\) 与平面夹角”的余弦。

**但本题根本不需要求这个长度。**

因为只知道“投影以后多长”，完全不知道那条投影直线**在哪里**。

---

## 这道题真正的几何框架

你把它想成这样：

原来有一条空间直线 \(L\)，现在拿灯光**沿着平面 \(\Pi\) 的法向方向垂直照下去**。

直线 \(L\) 的影子落在 \(\Pi\) 上，形成另一条直线。

所以最终我们要找的是：

\[
\boxed{\text{投影直线的位置}+\text{投影直线的方向}}
\]

两个解析只是用了两种不同的办法。

第一张解析的思路尤其重要：

> 先造出一个平面 \(\Sigma\)，使它  
> ① 包含原直线 \(L\)；  
> ② 与 \(\Pi\) 垂直。

为什么？

因为整个投影过程都发生在这个平面 \(\Sigma\) 里面。

于是：

\[
\boxed{\text{投影直线}=\Sigma\cap\Pi}
\]

这句话就是第一种解析的核心。

你现在先不用管后面的 \(\lambda=\frac{11}{5}\) 怎么算。

### 我只问你当前下一步

既然

\[
\frac{x+2}{3}
=
\frac{2-y}{1}
=
\frac{z+1}{2},
\]

如果我让你先把这条直线 \(L\) 写成“**两个平面的交线**”，你能不能从这三个比值中任选两个等式，先写出其中一个平面方程？

:::



::: {.message .user #T03}

### T03｜用户

你可以弄个几何图给我，帮我想象一下吗？我实在想象不出来这个画面。

我脑子里想的画面是：一个平面在我面前是竖直的，上面有一条线。你是怎么构造出一个平面把这条线包含进去（让这条线在这个平面里），并且这个新平面还跟 2x + 3y + 3z - 8 = 0 这个平面垂直的？

我想象不到。因为我觉得除非这条直线本身就跟那个平面垂直，否则很难理解。

你能不能构造一个 3D 的图片给我看一下？我空间想象能力欠缺挺久了，很多题都想象不出来。

:::



::: {.message .assistant #T04}

### T04｜助手

**归档附记：本回合先有图像/代码输出，最后有文字回复。以下按顺序保留。**

#### 图像输出 1（历史草图，非最终采用图）

图像工具可见描述：

A crisp, white-background educational infographic uses translucent blue and green planes, a red spatial line, dashed normal projections, coordinate axes, and Chinese labels to explain projecting line \(L\) onto plane \(\Pi: 2x+3y+3z-8=0\). It emphasizes constructing a plane \(\Sigma\) containing \(L\) and perpendicular to \(\Pi\), so the projected line is the intersection \(L'=\Sigma\cap\Pi\), presented through a large 3D overview, explanatory notes, and three step-by-step panels.


![29-4 / 57981｜早期生成图一（非定稿，含错误文字）](assets/29-04_57981_geometry_draft_01.png)

图片路径：`assets/29-04_57981_geometry_draft_01.png`；尺寸：1312 × 1199；状态：原文件，逐字节保留。
#### 图像输出 2（历史草图，非最终采用图）

图像工具可见描述：

An educational Chinese infographic uses a clean grid layout to explain projecting line \(L\) onto plane \(\Pi:2x+3y+3z-8=0\), featuring 3D diagrams, cross-sections, formulas, and color-coded elements for \(L\), \(\Pi\), the auxiliary perpendicular plane \(\Sigma\), projection points, and normal vector \(\mathbf n=(2,3,3)\). It presents both geometric and algebraic methods, including \(L'=\Sigma\cap\Pi\), point projection \(P'=P-t\mathbf n\), direction projection \(\mathbf d'=\mathbf d-\frac{\mathbf d\cdot\mathbf n}{|\mathbf n|^2}\mathbf n\), and the key idea that the projection is a line—not a length.


![29-4 / 57981｜早期生成图二（非定稿）](assets/29-04_57981_geometry_draft_02.png)

图片路径：`assets/29-04_57981_geometry_draft_02.png`；尺寸：1536 × 1024；状态：原文件，逐字节保留。
#### 图像输出 3（历史草图，非最终采用图）

图像工具可见描述：

A crisp textbook-style 3D geometry infographic on a white background, annotated in Chinese, illustrates the orthogonal projection of a spatial line onto a plane using translucent colored surfaces, coordinate axes, dashed projection guides, and labeled arrows. The diagram features a red original line \(L\), its blue projected line \(L′\) on the green plane \(\Pi:2x+3y+3z-8=0\), an intersecting blue plane \(\Sigma\) containing \(L\) and perpendicular to \(\Pi\), plus a right-hand step panel and bottom “关键理解/补充说明” summaries explaining the construction and the special case \(L\parallel\Pi\).


![29-4 / 57981｜早期生成图三（非定稿，条件表述不严谨）](assets/29-04_57981_geometry_draft_03.png)

图片路径：`assets/29-04_57981_geometry_draft_03.png`；尺寸：1312 × 1199；状态：原文件，逐字节保留。
#### 当时向用户展示的 Python 绘图代码

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 选用可显示中文的字体；几何关系由题目的方向向量和法向量计算。
fonts = font_manager.findSystemFonts()
cjk = next((p for p in fonts if "NotoSansCJK" in p), None)
if cjk:
    font = font_manager.FontProperties(fname=cjk)
else:
    font = font_manager.FontProperties()

d = np.array([3.0, -1.0, 2.0])     # 原直线方向
n = np.array([2.0, 3.0, 3.0])      # 投影平面法向方向
normal_component = np.dot(d, n) / np.linalg.norm(n)
parallel_component = np.linalg.norm(d - np.dot(d, n) / np.dot(n, n) * n)
slope = normal_component / parallel_component

# 只旋转观察方向：将 Π 看作桌面，Σ 看作竖直玻璃板。
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection="3d", computed_zorder=False)

u, v = np.meshgrid([-3.2, 5.2], [-2.6, 2.6])
ax.plot_surface(u, v, np.zeros_like(u), alpha=0.20,
                shade=False, zorder=1)

u2, h = np.meshgrid([-3.2, 5.2], [-2.2, 3.6])
ax.plot_surface(u2, np.zeros_like(u2), h, alpha=0.17,
                shade=False, zorder=2)

s = np.array([-3.0, 0.0, 1.8, 4.0, 5.0])
ax.plot(s, np.zeros_like(s), np.zeros_like(s),
        linewidth=4, marker="o", markevery=[1, 2, 3],
        markersize=7, zorder=5)
ax.plot(s, np.zeros_like(s), slope*s,
        linewidth=4, marker="o", markevery=[1, 2, 3],
        markersize=7, zorder=6)

for position, label in [(1.8, "A"), (4.0, "B")]:
    height = slope*position
    ax.plot([position, position], [0, 0], [0, height],
            linestyle="--", linewidth=2, zorder=4)
    ax.text(position, 0, height+0.16, f"${label}$", fontsize=17, zorder=8)
    ax.text(position, -0.10, -0.30, f"${label}'$", fontsize=17, zorder=8)

# 两平面的直角标记：一个方向在桌面内，一个方向垂直桌面。
q, a = -1.7, 0.48
ax.plot([q, q, q], [0, a, a], [a, a, 0], linewidth=1.5, zorder=7)
ax.text(q, a+0.10, a+0.10, "$90^\\circ$", fontsize=15, zorder=8)

ax.text(-0.12, -0.20, -0.25, "$O$", fontsize=17, zorder=8)
ax.text(5.0, 0, slope*5.0+0.12, "$L$", fontsize=23, zorder=8)
ax.text(5.18, 0, -0.10, "$L'$", fontsize=23, zorder=8)
ax.text(-2.80, 0, 3.15, "$\\Sigma$", fontsize=29, zorder=8)
ax.text(-2.20, -2.0, 0.08, "$\\Pi$", fontsize=29, zorder=8)

ax.view_init(elev=24, azim=-63)
ax.set_box_aspect((8.4, 5.2, 5.8))
ax.set_xlim(-3.5, 5.8)
ax.set_ylim(-2.8, 2.8)
ax.set_zlim(-2.3, 3.8)
ax.set_axis_off()

fig.suptitle("斜线可以在竖直玻璃板内，不必垂直桌面",
             fontproperties=font, fontsize=21, y=0.95)
fig.text(0.5, 0.09, "Σ：竖直玻璃板　　Π：桌面　　L：原直线　　L′：投影直线",
         ha="center", fontproperties=font, fontsize=16)
fig.text(0.5, 0.045, "虚线 AA′、BB′ 垂直桌面；它们与原直线 L 都在玻璃板 Σ 内。",
         ha="center", fontproperties=font, fontsize=15)

plt.subplots_adjust(left=0, right=1, top=0.92, bottom=0.12)
path = "[原路径见完整原始ZIP]
fig.savefig(path, dpi=220, bbox_inches="tight")
plt.show()
```

#### Python 绘图输出（本轮最终采用图）


![29-4 / 57981｜对话最终采用的几何示意图](assets/29-04_57981_geometry_final.png)

图片路径：`assets/29-04_57981_geometry_final.png`；尺寸：1628 × 1846；状态：原文件，逐字节保留。

#### 本回合最终文字回复（原文）

以**最后这张按本题几何关系绘制的图**为准：[查看几何示意图原图](sandbox : [原路径见完整原始ZIP])。

:::



::: {.message .user #T05}

### T05｜用户

好，这道题没问题，这道题没问题

:::



::: {.message .assistant #T06}

### T06｜助手

好，这题先结束。

这道题你现在抓住的核心就是：

\[
\boxed{\text{投影直线}=\text{“包含原直线 }L\text{ 且垂直于 }\Pi\text{ 的辅助平面”}\cap \Pi}
\]

以及空间里**一条斜直线完全可以躺在一个与原平面垂直的平面里**，并不要求这条直线本身垂直于原平面。

这题目前记作：**经过图示和完整讲解后理解**。

:::


<a id="q29-5"></a>
