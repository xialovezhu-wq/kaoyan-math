ID: 57969）

## 题目主题

点到平面的距离

## 题目原图

![题目原图](images/28-4_question.png)

## 题面文本

点 \(P(1,-1,2)\) 到平面
\[
\pi:2x-y+5z-12=0
\]
的距离 \(d=\underline{\qquad}\)。

## 标准答案

\(\dfrac{\sqrt{30}}{30}\)

## 解析图

### 解析图（按用户上传内容复刻）

![解析图（按用户上传内容复刻）](images/28-4_solution_recreated.png)

## 涉及知识点

- 点到平面的距离公式：d=|Ax0+By0+Cz0+D|/√(A²+B²+C²)。
- 分子是“点代入平面方程左端后的绝对值”；分母是平面法向量 (A,B,C) 的模。
- 两点距离：对应坐标作差、平方、相加、开根号。
- 二维点到直线与三维点到空间直线必须区分：前者使用一般式代入公式，后者通常使用叉乘求高或参数最值。
- 距离必须非负，因此分子要取绝对值。

## 本题学习断点

遗忘了点到平面的距离公式，并把点到二维直线、点到空间直线、点到点距离混在一起，需要建立公式分类。

## 完整对话记录

### 对话 1｜用户

这道题我是点到平面的距离公式有点忘记了，包括点到直线的距离公式，还有点跟点之间的距离公式，我都有点忘记了，你都给我列举一下。

### 对话 2｜助手

可以，这几个距离公式建议你**放在一起记**。

## 1. 两点之间的距离

空间中两点

\[
P_1(x_1,y_1,z_1),\qquad P_2(x_2,y_2,z_2),
\]

则

\[
\boxed{
d=
\sqrt{
(x_2-x_1)^2+
(y_2-y_1)^2+
(z_2-z_1)^2
}
}
\]

二维平面中就是少一个 \(z\)：

\[
\boxed{
d=
\sqrt{
(x_2-x_1)^2+
(y_2-y_1)^2
}
}
\]

记忆：**坐标对应作差 → 平方 → 相加 → 开根号。**

---

## 2. 点到平面的距离

点

\[
P(x_0,y_0,z_0)
\]

到平面

\[
\pi:Ax+By+Cz+D=0
\]

的距离：

\[
\boxed{
d=
\frac{
|Ax_0+By_0+Cz_0+D|
}{
\sqrt{A^2+B^2+C^2}
}
}
\]

这个非常重要。

### 怎么记？

分子：

\[
\boxed{\text{把点的坐标直接代进平面方程左边，取绝对值}}
\]

分母：

\[
\boxed{\text{平面法向量 }(A,B,C)\text{ 的模}}
\]

也就是

\[
\sqrt{A^2+B^2+C^2}.
\]

例如你现在这道题：

\[
P(1,-1,2),
\]

\[
2x-y+5z-12=0,
\]

所以

\[
d=
\frac{|2(1)-(-1)+5(2)-12|}
{\sqrt{2^2+(-1)^2+5^2}}
=
\frac1{\sqrt{30}}.
\]

---

# 3. 点到直线的距离

这里要分成**二维直线**和**空间直线**。

### 二维：点到平面直线

若

\[
P(x_0,y_0)
\]

到直线

\[
Ax+By+C=0,
\]

则

\[
\boxed{
d=
\frac{|Ax_0+By_0+C|}
{\sqrt{A^2+B^2}}
}
\]

你会发现它和刚才的点到平面公式长得几乎一模一样。

实际上可以一起记：

\[
\boxed{
\frac{\left|\text{点代入方程左端}\right|}
{\left|\text{法向量}\right|}
}
\]

二维直线法向量是

\[
(A,B),
\]

三维平面法向量是

\[
(A,B,C).
\]

---

### 三维：空间中的点到直线

这是你现在这一章更需要注意的。

空间直线 \(L\) 上取一点

\[
A(x_1,y_1,z_1),
\]

直线的方向向量为

\[
\boldsymbol s=(l,m,n).
\]

空间中另有一点 \(P\)。

先构造

\[
\overrightarrow{AP}.
\]

则点 \(P\) 到直线 \(L\) 的距离：

\[
\boxed{
d=
\frac{
\left\|
\overrightarrow{AP}\times \boldsymbol s
\right\|
}{
\|\boldsymbol s\|
}
}
\]

这个公式建议你**不要纯硬背**。

因为

\[
\left\|
\overrightarrow{AP}\times \boldsymbol s
\right\|
\]

表示以 \(\overrightarrow{AP}\) 和 \(\boldsymbol s\) 为邻边的平行四边形面积。

而

\[
\text{面积}=\text{底}\times\text{高}.
\]

这里：

\[
\text{底}=\|\boldsymbol s\|,
\]

“高”恰好就是**点到直线的距离** \(d\)。

所以

\[
\|\overrightarrow{AP}\times\boldsymbol s\|
=
\|\boldsymbol s\|d,
\]

自然得到

\[
\boxed{
d=
\frac{\|\overrightarrow{AP}\times\boldsymbol s\|}
{\|\boldsymbol s\|}
}.
\]

---

## 你现在先把这张“小表”记住

| 距离 | 公式 |
|---|---|
| **点—点** | \(\displaystyle d=\sqrt{(\Delta x)^2+(\Delta y)^2+(\Delta z)^2}\) |
| **点—平面** | \(\displaystyle d=\frac{|Ax_0+By_0+Cz_0+D|}{\sqrt{A^2+B^2+C^2}}\) |
| **点—二维直线** | \(\displaystyle d=\frac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}\) |
| **点—空间直线** | \(\displaystyle d=\frac{\|\overrightarrow{AP}\times\boldsymbol s\|}{\|\boldsymbol s\|}\) |

最值得区分的是最后两个：

\[
\boxed{\text{二维点到直线：代公式}}
\]

\[
\boxed{\text{空间点到直线：叉乘求高}}
\]

而你当前这道题属于第二种：

\[
\boxed{\text{点到平面}=
\frac{|\text{代入平面左端}|}{|\text{法向量}|}}
\]

这几个公式先记到这个程度就够用了。

---
