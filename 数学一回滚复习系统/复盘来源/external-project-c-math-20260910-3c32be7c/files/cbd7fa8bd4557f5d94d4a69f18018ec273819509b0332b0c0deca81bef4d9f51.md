---
solution_surface: true
formal_id: GS-371
source_app: MarginNote 4
source_export: "/Users/xiazhibin/Library/Containers/QReader.MarginStudy.easy/Data/Documents/ExportedOmniOutlinerFiles/考研高数(2026-06-30-20-10-36).oo3"
source_refid: 7fac687a08157cb6f01bbc614eba60a8
source_locator: 强化例题13.8
extraction: original OO3 child-node text
extracted_at: 2026-09-09
---

# GS-371 解析

按张宇“三向解题法”整理

---

## ✅ 1）对应章节与所用方法

* 章节定位：多元函数极限与连续、偏导与可微  
* 核心方法：  
  * 判断连续：分子分母同次 → 同阶路径法 \(y=kx\)  
  * 判断偏导：用定义式，沿坐标轴代入算极限  

---

## ✅ 2）详细作答

给  
\[
f(x,y)=
\begin{cases}
\dfrac{xy}{x^2+y^2}, & (x,y)\neq(0,0),\\[4pt]
0, & (x,y)=(0,0).
\end{cases}
\]

---

### （Ⅰ）在 \((0,0)\) 的连续性

取同阶路径 \(y=kx\)：  
\[
\lim_{x\to0}f(x,kx)
=
\lim_{x\to0}
\frac{x\cdot kx}{x^2+(kx)^2}
=
\frac{k}{1+k^2}.
\]

随 \(k\) 不同取不同值（\(k=0\Rightarrow0,\ k=1\Rightarrow\frac12\)），  
故
\[
\lim_{(x,y)\to(0,0)}f(x,y)\ \text{不存在}.
\]

⇒ 在原点不连续。

---

### （Ⅱ）在 \((0,0)\) 的偏导

\[
f_x(0,0)
=
\lim_{h\to0}
\frac{f(h,0)-f(0,0)}{h}
=
\lim_{h\to0}
\frac{0-0}{h}
=0.
\]

\[
f_y(0,0)
=
\lim_{h\to0}
\frac{f(0,h)-f(0,0)}{h}
=
\lim_{h\to0}
\frac{0-0}{h}
=0.
\]

两偏导数均存在（且为 \(0\)）。

---

## ✅ 3）结论与方法小结

\[
\boxed{\text{原点不连续，但偏导数存在}}
\quad\Rightarrow\quad \boxed{C}
\]

方法回顾：

- 同次齐次结构 → 先试 \(y=kx\) 判二重极限  
- 偏导只沿坐标轴算一维极限  
- 偏导存在 ≠ 连续（经典反例）

---
