---
solution_surface: true
formal_id: GS-390
source_app: MarginNote 4
source_export: "/Users/xiazhibin/Library/Containers/QReader.MarginStudy.easy/Data/Documents/ExportedOmniOutlinerFiles/考研高数(2026-06-30-20-10-36).oo3"
source_refid: c311f3978ae79b54a6d9d261c2a123e4
source_locator: 强化例题13.26
extraction: original OO3 child-node text
extracted_at: 2026-09-09
---

# GS-390 解析

题目  \(f(x,y)=3(x^2+y^2)-x^3\) 求极值

# 张宇式三步法

---

### ① 求驻点（先一阶导为零）

\[
f_x=6x-3x^2=3x(2-x),\qquad f_y=6y .
\]

解  
\[
f_x=0,\ f_y=0 \ \Rightarrow\ x=0\text{ 或 }2,\ y=0.
\]

驻点：\((0,0)\)、\((2,0)\)。

---

### ② 二阶判别（Hessian 判别法）

\[
f_{xx}=6-6x,\quad f_{xy}=0,\quad f_{yy}=6.
\]

记  
\[
D=f_{xx}f_{yy}-f_{xy}^2.
\]

---

#### ✅ 在 \((0,0)\)

\[
f_{xx}=6,\ f_{yy}=6,\ f_{xy}=0
\]

\[
D=6\cdot6-0=36>0,\quad f_{xx}=6>0
\]

\[
\Rightarrow\ \text{局部极小点}
\]

极小值  
\[
f(0,0)=0.
\]

---

#### ✅ 在 \((2,0)\)

\[
f_{xx}=-6,\ f_{yy}=6,\ f_{xy}=0
\]

\[
D=-6\cdot6=-36<0
\]

\[
\Rightarrow\ \text{鞍点（非极值点）}.
\]

---

### ③ 最终结论

函数 \(f(x,y)\) 只有一个极值点 \((0,0)\)，为极小值点，且

\[
\boxed{f_{\min}=f(0,0)=0}.
\]
