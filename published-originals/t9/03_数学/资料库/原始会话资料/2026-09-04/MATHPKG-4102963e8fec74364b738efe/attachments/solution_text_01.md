---
title: 考研数学两题完整学习记录（供 Codex 读取）
document_id: math-session-2026-09-04-vector-geometry-01
created_at: 2026-09-04T10:15:00+08:00
language: zh-CN
scope: 2 道题
subjects:
  - 线性代数：向量组线性相关、三维向量共面、行列式
  - 高等数学/空间解析几何：直线方向向量、两平面交线、两直线夹角
transcript_status: 已保存本轮与两道题有关的全部实质性对话
---

# 考研数学两题完整学习记录（供 Codex 读取）

## 0. 使用说明

本文件用于把两道题的原图、标准解析图、题目编号、知识点、用户真实思路、纠正过程和完整对话一次性交接给 Codex。

**读取时应特别保留以下事实：**

1. 第 1 题中，用户最初的真实断点是把“共面”与“成比例”联系在一起，不清楚“共面 ↔ 线性相关 ↔ 行列式为零”的关系。
2. 第 1 题是在完整讲解后理解，不能据此直接标记为“已独立完成”。
3. 第 2 题中，用户已经独立识别了两条直线的方向向量求法；用户说成 $(-1,-1,-2)$ 是**口误**，其实际计算结果是 $(-1,-1,2)$，不能记为叉乘计算错误。
4. 第 2 题的真实断点只是忘记“两直线夹角公式”，在局部提示后恢复。
5. 对话转录中仅把平台内部不可移植的引用标记改写为说明文字，其余数学内容和纠正关系均保留。

---

# 1. 题目目录

| 文档内部编号 | 原始题号 / ID | 题型 | 标准答案 | 当前掌握状态 |
|---|---|---|---|---|
| Q1 | 原图未显示题号或 ID | 三个三维向量共面，求参数 $k$ | D，$k=-2$ | 完整讲解后理解，尚未验证能否脱离提示独立复现 |
| Q2 | （28-2），ID: 57848 | 两条空间直线的夹角 | C，$\dfrac{\pi}{3}$ | 主方法独立完成；仅夹角公式遗忘，经局部提示恢复 |

---

# 2. Q1：三个三维向量共面，求参数 $k$

## 2.1 编号与原图

- **文档内部编号：** Q1
- **原始题号 / ID：** 原图未显示，不能擅自补造
- **标准答案：** D，$k=-2$

### 题目图片

![Q1 题目：三个三维向量共面求 k](images/q1_question_coplanar_vectors.png)

### 标准解析图片

![Q1 标准解析：由共面推出混合积或行列式为零](images/q1_solution_coplanar_vectors.png)

## 2.2 题面文字

设向量

$$
\boldsymbol a=(1,2,1),\qquad
\boldsymbol b=(-1,0,2),\qquad
\boldsymbol c=(0,k,-3)
$$

共面，则 $k=(\ \ )$。

- (A) $1$
- (B) $2$
- (C) $-1$
- (D) $-2$

## 2.3 涉及的知识点

1. **共线与成比例**
   
   对两个非零向量：

   $$
   \boldsymbol b=\lambda\boldsymbol a
   \iff
   \boldsymbol a,\boldsymbol b\text{ 共线}.
   $$

   “成比例”对应共线，不对应共面。

2. **三维向量共面与线性相关**

   三个三维向量共面，当且仅当它们线性相关：

   $$
   \boldsymbol a,\boldsymbol b,\boldsymbol c\text{ 共面}
   \iff
   \boldsymbol a,\boldsymbol b,\boldsymbol c\text{ 线性相关}.
   $$

3. **线性表示的几何含义**

   当 $\boldsymbol a,\boldsymbol b$ 不共线时，它们张成一个平面；向量 $\boldsymbol c$ 与它们共面，等价于存在数 $x,y$，使

   $$
   \boldsymbol c=x\boldsymbol a+y\boldsymbol b.
   $$

4. **向量个数等于维数时的行列式判据**

   对三个三维向量：

   $$
   \boldsymbol a,\boldsymbol b,\boldsymbol c\text{ 线性相关}
   \iff
   \det(\boldsymbol a,\boldsymbol b,\boldsymbol c)=0.
   $$

   向量按行放或按列放都可以，因为转置不改变行列式是否为零。

5. **数量积、向量积与混合积中的本题对象**

   标准解析使用的是混合积：

   $$
   (\boldsymbol a\,\boldsymbol b\,\boldsymbol c)
   =(\boldsymbol a\times\boldsymbol b)\cdot\boldsymbol c.
   $$

   混合积的绝对值表示以三个向量为棱的平行六面体体积；共面时体积为零。

## 2.4 触发信息与动作链

**看到：** 三个三维向量“共面”，其中含参数 $k$。

**想到：** 共面 $\Rightarrow$ 线性相关。

**第一动作：** 直接令由三个向量组成的三阶行列式等于零。

**动作链：**

$$
\text{三个三维向量共面}
\Rightarrow
\text{线性相关}
\Rightarrow
\det=0
\Rightarrow
\text{解参数 }k.
$$

**适用条件：** 这里是三个三维向量，恰好“向量个数 = 维数”，因此可直接使用三阶行列式判据。一般情形应转为秩或齐次方程判断，不能机械套三阶行列式。

## 2.5 标准解法一：行列式法

由共面知三个向量线性相关，因此

$$
\begin{vmatrix}
1&2&1\\
-1&0&2\\
0&k&-3
\end{vmatrix}=0.
$$

展开：

$$
-2k-6-k=0,
$$

即

$$
-3k-6=0.
$$

所以

$$
\boxed{k=-2}.
$$

选择 **D**。

## 2.6 标准解法二：线性表示法

先确认 $\boldsymbol a$ 与 $\boldsymbol b$ 不成比例，因此二者不共线，能够张成一个平面。

由 $\boldsymbol c$ 与二者共面，存在 $x,y$，使

$$
\boldsymbol c=x\boldsymbol a+y\boldsymbol b.
$$

代入：

$$
(0,k,-3)
=x(1,2,1)+y(-1,0,2)
=(x-y,2x,x+2y).
$$

对应分量得

$$
\begin{cases}
x-y=0,\\
2x=k,\\
x+2y=-3.
\end{cases}
$$

由 $x=y$ 及 $x+2y=-3$ 得 $x=y=-1$，故

$$
k=2x=-2.
$$

## 2.7 用户真实思路与断点诊断

### 用户已经独立做对的部分

- 能把“三个向量共面”理解为三个向量位于同一平面。
- 知道两个向量共线时可以通过“成比例”判断。
- 主动发现 $\boldsymbol a$ 与 $\boldsymbol b$ 明显不成比例，并据此产生疑问。

### 第一个真正断点

用户把“共面”可能对应“成比例”联系起来，不清楚以下区别：

- 共线：两个非零向量成比例；
- 共面：三个三维向量线性相关，或第三个向量可由另外两个向量线性表示；
- 三个三维向量线性相关：三阶行列式为零。

### 本轮纠正结果

用户随后能够自行复述：

$$
\text{共面}
\Rightarrow
\text{线性相关}
\Rightarrow
\text{行列式等于零}
\Rightarrow
\text{解 }k.
$$

### 掌握度边界

- **当前证据：** 完整讲解后理解并能复述主链。
- **尚未确认：** 换一组向量后能否脱离提示独立识别并完成。
- **不得误记为：** 已经从零独立完成本题。

---

# 3. Q2：两条空间直线的夹角

## 3.1 编号与原图

- **文档内部编号：** Q2
- **原始题号 / ID：** （28-2），ID: 57848
- **标准答案：** C，$\dfrac{\pi}{3}$

### 题目图片

![Q2 题目：ID 57848，两条空间直线的夹角](images/q2_question_line_angle_id57848.png)

### 标准解析图片

![Q2 标准解析：求两条直线的方向向量并使用点积公式](images/q2_solution_line_angle_id57848.png)

## 3.2 题面文字

设直线

$$
L_1:\frac{x-1}{1}=\frac{y-5}{-2}=\frac{z+8}{1}
$$

与

$$
L_2:
\begin{cases}
x-y=6,\\
2y+z=3,
\end{cases}
$$

则 $L_1$ 与 $L_2$ 的夹角为 $(\ \ )$。

- (A) $\dfrac{\pi}{6}$
- (B) $\dfrac{\pi}{4}$
- (C) $\dfrac{\pi}{3}$
- (D) $\dfrac{\pi}{2}$

## 3.3 涉及的知识点

1. **点向式 / 对称式直线的方向向量**

   对直线

   $$
   \frac{x-x_0}{l}=\frac{y-y_0}{m}=\frac{z-z_0}{n},
   $$

   方向向量为

   $$
   (l,m,n).
   $$

   因而

   $$
   \boldsymbol s_1=(1,-2,1).
   $$

2. **平面的一般式与法向量**

   平面

   $$
   Ax+By+Cz+D=0
   $$

   的法向量为 $(A,B,C)$。

   本题两个平面的法向量为

   $$
   \boldsymbol n_1=(1,-1,0),\qquad
   \boldsymbol n_2=(0,2,1).
   $$

3. **两平面交线的方向向量**

   交线同时垂直于两个平面的法向量，因此可取

   $$
   \boldsymbol s_2=\boldsymbol n_1\times\boldsymbol n_2.
   $$

4. **叉乘的行列式写法**

   $$
   \boldsymbol n_1\times\boldsymbol n_2
   =
   \begin{vmatrix}
   \boldsymbol i&\boldsymbol j&\boldsymbol k\\
   1&-1&0\\
   0&2&1
   \end{vmatrix}
   =(-1,-1,2).
   $$

5. **方向向量的不唯一性**

   方向向量可乘任意非零常数。反转叉乘顺序会使整个向量同时变号：

   $$
   \boldsymbol n_2\times\boldsymbol n_1
   =-(\boldsymbol n_1\times\boldsymbol n_2).
   $$

   因此 $(-1,-1,2)$ 与 $(1,1,-2)$ 都可作为 $L_2$ 的方向向量；不能只改变某一个分量的符号。

6. **两直线夹角公式**

   设两直线的方向向量为 $\boldsymbol s_1,\boldsymbol s_2$，则两直线夹角 $\theta$ 取较小的非钝角：

   $$
   0\leq\theta\leq\frac{\pi}{2},
   $$

   且

   $$
   \boxed{
   \cos\theta
   =
   \frac{|\boldsymbol s_1\cdot\boldsymbol s_2|}
   {\|\boldsymbol s_1\|\,\|\boldsymbol s_2\|}
   }.
   $$

   绝对值用于消除方向向量朝向的任意性，并保证取得两直线的较小夹角。

## 3.4 触发信息与动作链

**看到：** 一条直线用对称式给出，另一条直线由两个平面的交线给出，目标是求两直线夹角。

**想到：** 先统一获得两条直线的方向向量，再用点积公式。

**第一动作：**

- 从 $L_1$ 的分母直接读取 $\boldsymbol s_1$；
- 从 $L_2$ 的两个平面读取法向量，再叉乘求 $\boldsymbol s_2$。

**动作链：**

$$
\text{读 }L_1\text{ 的方向向量}
\rightarrow
\text{取 }L_2\text{ 两平面的法向量}
\rightarrow
\text{法向量叉乘得交线方向向量}
\rightarrow
\text{点积公式求夹角}.
$$

## 3.5 标准解法

由 $L_1$ 的对称式，取方向向量

$$
\boldsymbol s_1=(1,-2,1).
$$

$L_2$ 是平面

$$
x-y-6=0
$$

与平面

$$
2y+z-3=0
$$

的交线。两个法向量分别为

$$
\boldsymbol n_1=(1,-1,0),\qquad
\boldsymbol n_2=(0,2,1).
$$

因此 $L_2$ 的方向向量可取

$$
\boldsymbol s_2
=\boldsymbol n_1\times\boldsymbol n_2
=(-1,-1,2).
$$

计算点积：

$$
\boldsymbol s_1\cdot\boldsymbol s_2
=1\cdot(-1)+(-2)\cdot(-1)+1\cdot2
=3.
$$

计算模长：

$$
\|\boldsymbol s_1\|=\sqrt{1^2+(-2)^2+1^2}=\sqrt6,
$$

$$
\|\boldsymbol s_2\|=\sqrt{(-1)^2+(-1)^2+2^2}=\sqrt6.
$$

故

$$
\cos\theta
=\frac{|3|}{\sqrt6\cdot\sqrt6}
=\frac12.
$$

由于两直线夹角满足 $0\leq\theta\leq\dfrac{\pi}{2}$，所以

$$
\boxed{\theta=\frac{\pi}{3}}.
$$

选择 **C**。

## 3.6 用户真实思路与断点诊断

### 用户已经独立做对的部分

- 正确从 $L_1$ 的对称式读出方向向量：

  $$
  \boldsymbol s_1=(1,-2,1).
  $$

- 正确识别 $L_2$ 是两个平面的交线。
- 正确读出两个平面的法向量：

  $$
  \boldsymbol n_1=(1,-1,0),\qquad
  \boldsymbol n_2=(0,2,1).
  $$

- 正确想到通过 $\boldsymbol n_1\times\boldsymbol n_2$ 求 $L_2$ 的方向向量。
- 用户实际计算得到的是

  $$
  \boldsymbol s_2=(-1,-1,2).
  $$

### 关于符号的事实修正

用户在口述时把结果说成了 $(-1,-1,-2)$，随后明确说明这是**口误**，不是实际计算错误。因而：

- 不应把“叉乘符号算错”记录为该题错因；
- 助手先前关于“第一处错误在叉乘计算”的判断已被用户纠正；
- 真实掌握情况应按“叉乘方法和结果均正确”记录。

### 第一个真正断点

用户忘记了由两个方向向量求两直线夹角的公式，不确定能否直接用方向向量求夹角。

### 本轮纠正结果

经局部提示，用户恢复公式：

$$
\cos\theta
=
\frac{|\boldsymbol s_1\cdot\boldsymbol s_2|}
{\|\boldsymbol s_1\|\,\|\boldsymbol s_2\|}.
$$

用户随后确认本题没有问题。

### 掌握度边界

- **独立完成：** 方向向量提取、平面法向量提取、叉乘求交线方向。
- **局部提示后完成：** 两直线夹角公式的恢复。
- **不得误记为：** 叉乘计算错误或对交线方向向量方法不理解。

---

# 4. 两题联合复习卡

## 4.1 题目 Q1

**触发词：** 三个三维向量共面。

**立即翻译：**

$$
\text{共面}
\Longleftrightarrow
\text{线性相关}
\Longleftrightarrow
\det=0.
$$

**禁忌误用：** 不要把“共面”误判为“成比例”；成比例只对应两个非零向量共线。

## 4.2 题目 Q2

**触发词：** 一条直线是对称式，另一条直线是两平面交线，求夹角。

**立即翻译：**

$$
\text{两直线夹角}
\rightarrow
\text{先求两条直线的方向向量}
\rightarrow
\frac{|\boldsymbol s_1\cdot\boldsymbol s_2|}
{\|\boldsymbol s_1\|\|\boldsymbol s_2\|}.
$$

**交线方向：**

$$
\boldsymbol s_2=\boldsymbol n_1\times\boldsymbol n_2.
$$

**禁忌误用：**

- 两直线夹角取较小的非钝角，点积公式的分子要取绝对值；
- 反转叉乘顺序时是整个向量变号，不是只改一个分量；
- 方向向量不唯一，任意非零倍数均表示同一方向。

---

# 5. 项目资料方法论映射

以下映射只用于帮助 Codex延续同一套纠正标准：

- **Q1：** 与“向量组相关性”方法高度对应。项目资料中的动作链是：先看向量个数与维数；当“个数 = 维数”时可计算行列式；一般情形看秩。对应方法卡可匹配为 **L06-002**。
- **Q2：** “两平面交线的方向向量由两个法向量叉乘得到”与项目资料中“交线用 $\nabla F\times\nabla G$；叉乘顺序只影响方向”一致；该局部动作可对应 **H17-006**。但“两直线夹角”整题的完整方法卡 ID 在现有检索中未精确匹配，记为 **待匹配**。

---

# 6. 完整对话转录

下面按发生顺序保存本轮与两道题有关的全部实质性对话。附件位置改写为本文件中的相对图片路径。

## Turn 1 — 用户（Q1）

**附件：**

- `images/q1_question_coplanar_vectors.png`
- `images/q1_solution_coplanar_vectors.png`

> 这道题我完全无从下手。我好像知识储备没搞清楚，题目条件也没搞清楚。
>
> 他说这三个向量共面，就是说有个平面，这三个向量都在这个平面上。那能证明这三个向量是成比例的吗？但很明显 A 跟 B 不成比例啊，对吧？共线是成比例的，共面又有什么性质？我不是很清楚，这道题的知识点我忘记了。
>
> 你看我这道题应该怎么做？

## Turn 2 — 助手（Q1）

你现在真正缺的不是计算，而是**“共线、共面、线性相关”之间的对应关系**。这道题把这一块补上，以后基本就能直接识别了。

你前半句理解是对的：三个向量共面，就是把它们的起点都平移到原点以后，三个箭头都落在同一个平面里。

你这里的**第一个断点**是：

> “三个向量共面，会不会说明它们成比例？”

不会。**成比例对应的是共线，不是共面。**

### 先把这两个概念彻底分开

假设有两个非零向量 $\boldsymbol a,\boldsymbol b$。

如果它们**共线**，那么只能沿着同一个方向，因此

$$
\boldsymbol b=\lambda \boldsymbol a.
$$

所以：

$$
\boxed{\text{共线}\Longleftrightarrow\text{成比例}}
$$

但如果 $\boldsymbol a,\boldsymbol b$ **不共线**，它们就能“撑开”一个平面。

这个平面里的所有向量，都可以写成

$$
x\boldsymbol a+y\boldsymbol b.
$$

所以第三个向量 $\boldsymbol c$ 和它们共面，真正意味着：

$$
\boxed{\boldsymbol c=x\boldsymbol a+y\boldsymbol b}
$$

也就是：**第三个向量可以由前两个向量线性表示。**

你可以把它想成：

$$
\boldsymbol a,\boldsymbol b
\quad\Longrightarrow\quad
\text{撑出一个平面}
$$

而

$$
x\boldsymbol a+y\boldsymbol b
$$

会把这个平面里的所有向量都扫出来。

---

## 回到这道题

$$
\boldsymbol a=(1,2,1),\qquad
\boldsymbol b=(-1,0,2),\qquad
\boldsymbol c=(0,k,-3)
$$

很明显 $\boldsymbol a,\boldsymbol b$ 不成比例，所以它们不共线，可以撑出一个平面。

题目说 $\boldsymbol c$ 也在这个平面里，于是直接写：

$$
\boldsymbol c=x\boldsymbol a+y\boldsymbol b.
$$

即

$$
(0,k,-3)
=
x(1,2,1)+y(-1,0,2).
$$

右边展开：

$$
x(1,2,1)+y(-1,0,2)
=
(x-y,\;2x,\;x+2y).
$$

对应三个坐标：

$$
\begin{cases}
x-y=0,\\
2x=k,\\
x+2y=-3.
\end{cases}
$$

由第一式：

$$
x=y.
$$

代入第三式：

$$
3x=-3
$$

所以

$$
x=y=-1.
$$

于是第二式给出

$$
k=2x=-2.
$$

因此选

$$
\boxed{D}
$$

---

## 为什么解析直接写“行列式等于 0”？

这就是上面这个思想的**压缩版**。

三个三维向量共面

$$
\Longleftrightarrow
\text{这三个向量线性相关}
$$

而三个三维向量组成一个 $3\times3$ 矩阵时：

$$
\text{线性相关}
\Longleftrightarrow
\det A=0.
$$

所以直接有

$$
\begin{vmatrix}
1&2&1\\
-1&0&2\\
0&k&-3
\end{vmatrix}=0.
$$

展开：

$$
-2k-6-k=0
$$

即

$$
-3k-6=0,
$$

得到

$$
k=-2.
$$

所以以后看到这种题，脑子里要建立这条链：

$$
\boxed{
\text{三个三维向量共面}
\Rightarrow
\text{三个向量线性相关}
\Rightarrow
\det=0
}
$$

但更底层的几何理解其实是：

$$
\boxed{
\boldsymbol c=x\boldsymbol a+y\boldsymbol b
}
$$

你先回答我一个问题检查一下：**“两个向量共线”和“三个向量共面”，分别对应“成比例”还是“线性组合”？**

## Turn 3 — 用户（Q1）

> 哦，那我大概理解了。接下来这道题就是它们三个是共面的，所以它们三个是线性相关的，所以它们的行列式等于 0，直接令行列式等于 0 就可以求出 k 等于多少，对吧？
>
> 那我理解了。

## Turn 4 — 助手（Q1）

对，**完全正确**。你现在这条解题链已经通了：

$$
\boxed{\text{三个三维向量共面}}
\Longrightarrow
\boxed{\text{三个向量线性相关}}
\Longrightarrow
\boxed{\text{由它们组成的三阶行列式}=0}
$$

因为这里恰好是 **3 个三维向量**，即“向量个数 = 维数”，所以可以直接用行列式判断：

$$
|\boldsymbol a,\boldsymbol b,\boldsymbol c|=0
\iff
\boldsymbol a,\boldsymbol b,\boldsymbol c\text{ 线性相关}.
$$

这也是张宇这里给出的直接判断规则。

> 注：原对话此处附有平台内部文件引用标记；该标记在外部文档中不可解析，故仅保留其所对应的正文表述。

因此本题第一动作就是：

$$
\begin{vmatrix}
1&2&1\\
-1&0&2\\
0&k&-3
\end{vmatrix}=0,
$$

然后正常算行列式，解 $k$ 即可。

你现在只需要记住一个触发词：

> **看到“三个三维向量共面” → 立刻想到“线性相关” → 行列式 $=0$。**

这一题你已经理解到位了。

## Turn 5 — 用户（Q2）

**附件：**

- `images/q2_solution_line_angle_id57848.png`
- `images/q2_question_line_angle_id57848.png`

> 这道题我也无从下手吧。就这道题，我大概的想法就是说，通过 $L_1$ 的直线，它的方向向量应该是 (1, -2, 1)，对吧？
>
> 而 $L_2$ 是由两个平面决定的：
>
> 1. 第一个平面的法向量是 (1, -1, 0)
> 2. 第二个平面的法向量是 (0, 2, 1)
>
> 然后通过这两个平面的法向量叉乘得出 $L_2$ 的方向向量是 (-1, -1, -2)。因为这是一个 3 阶行列式嘛，第一行是 $i, j, k$，第二行是 (1, -1, 0)，第三行是 (0, 2, 1)。通过算这个行列式可以得到它的方向向量是 (-1, -1, -2)。
>
> 然后得到这两个直线的方向向量之后，就可以求它的夹角了。但具体求夹角的那个公式我忘了，我记得是两个方向向量可以求夹角，还是说不能求，得用别的方式求？

## Turn 6 — 助手（Q2）

对，你现在的**方法方向基本全对**，而且这道题其实已经被你做到最后一步了。你真正忘掉的是“**两直线夹角怎么由方向向量求**”。

不过先纠正你一个很小但关键的计算错误。

你前面这些都对：

$$
L_1:\frac{x-1}{1}=\frac{y-5}{-2}=\frac{z+8}{1}
$$

所以

$$
\boxed{\boldsymbol s_1=(1,-2,1)}
$$

而 $L_2$ 是两个平面的交线：

$$
\begin{cases}
x-y=6\\
2y+z=3
\end{cases}
$$

两个平面的法向量分别为

$$
\boldsymbol n_1=(1,-1,0),\qquad
\boldsymbol n_2=(0,2,1).
$$

因为交线 $L_2$ 同时垂直于两个法向量，所以

$$
\boldsymbol s_2=\boldsymbol n_1\times\boldsymbol n_2.
$$

你的**第一处错误就在这里的计算**：

$$
\begin{vmatrix}
\boldsymbol i&\boldsymbol j&\boldsymbol k\\
1&-1&0\\
0&2&1
\end{vmatrix}
$$

应该得到

$$
-\boldsymbol i-\boldsymbol j+2\boldsymbol k,
$$

所以

$$
\boxed{\boldsymbol s_2=(-1,-1,2)}
$$

不是 $(-1,-1,-2)$。

这里也有一个很好记的点：**叉乘顺序反过来，只会让整个向量同时变号**，比如 $(-1,-1,2)$ 变成 $(1,1,-2)$，这两个都可以作为同一直线的方向向量；但不能只把某一个分量变号。

---

然后你问的核心问题：

## 两条直线的方向向量当然可以直接求夹角

设两条直线的方向向量分别为

$$
\boldsymbol s_1,\boldsymbol s_2,
$$

那么两直线夹角 $\theta$ 满足

$$
\boxed{
\cos\theta=
\frac{|\boldsymbol s_1\cdot\boldsymbol s_2|}
{|\boldsymbol s_1||\boldsymbol s_2|}
}
$$

这其实就是普通的**向量夹角公式**，只不过这里有一个非常重要的区别：

普通两个向量的夹角可以是

$$
0\leq\varphi\leq\pi,
$$

但“两条直线的夹角”默认取较小的那个角，所以

$$
0\leq\theta\leq\frac{\pi}{2}.
$$

因此公式里直接加**绝对值**：

$$
\boxed{
\cos\theta=
\frac{|\boldsymbol s_1\cdot\boldsymbol s_2|}
{|\boldsymbol s_1||\boldsymbol s_2|}
}
$$

你以后看到：

> **求两直线夹角**

第一动作就是：

$$
\boxed{\text{先分别找两条直线的方向向量}}
$$

然后：

$$
\boxed{\text{方向向量点积公式，最后记得取绝对值}}
$$

你现在接着自己算一步：用

$$
\boldsymbol s_1=(1,-2,1),\qquad
\boldsymbol s_2=(-1,-1,2),
$$

算一下

$$
\boldsymbol s_1\cdot\boldsymbol s_2
$$

等于多少？

## Turn 7 — 用户（Q2 纠正与整理请求）

> 这道题我口误了。我算出来的方向向量应该是 (-1, -1, 2)，但我口误说成了 (-1, -1, -2)。
>
> 所以这道题的夹角 cosθ，它等于它俩点乘除以它俩的模长相乘。
>
> 好，这道题没问题了，把刚刚这两道题整理一下。好，将这几道题整理一下：把题目的图片、题目解析图、题目的编号，以及涉及的知识点、我和你对话的全部内容都存起来，整理成一个文档，给 Codex 看的文档。

---

# 7. 给 Codex 的后续处理边界

1. 后续复习 Q1 时，应先让用户独立说出“共面”的代数翻译，再判断是否真正掌握；不能仅凭本轮听懂就判定为独立掌握。
2. 后续复习 Q2 时，不要重复纠正叉乘结果；用户已明确该处只是口误。应重点抽查：
   
   $$
   \cos\theta=
   \frac{|\boldsymbol s_1\cdot\boldsymbol s_2|}
   {\|\boldsymbol s_1\|\|\boldsymbol s_2\|}
   $$

   以及为什么要取绝对值。
3. 若做轻微变式，可分别测试：
   - Q1：把参数放到不同分量，要求用户自行从“共面”触发行列式为零；
   - Q2：交换两个平面的顺序，检查用户是否理解方向向量整体变号不影响直线夹角。
4. 当前记录只覆盖本文件所列两题，不应自动扩展为其他题目的学习结论。
