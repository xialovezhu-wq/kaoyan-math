---
wiki_id: MATHWIKI-LA-METHOD-012
type: method
title: 矩阵方程按列拆与解空间参数化
subject: 线性代数
knowledge:
  - 矩阵运算
  - 矩阵秩
  - 线性方程组
  - 相似矩阵
methods:
  - 换基表示
  - 矩阵方程按列拆
  - Jordan链构造
  - 齐次方程组基础解系
  - 非齐次线性方程组通解
  - 可逆性检验
error_causes:
  - 待补充
triggers:
  - 题面出现 \(AP=PB\) 且 \(P\) 的列是向量组
  - 题面出现 \(P^{-1}AP=J\)
  - 题面出现 \(AP=B\) 且要求可逆 \(P\)
  - 题面出现 \(AB=A\) 且 \(A\) 可能不可逆
  - 题面出现 \(AB=\lambda B\) 或 \(CA^{\mathsf T}=\lambda C\)
source_refs:
  - 错题知识网络/错题卡/LA-061_1000题B组3.7.md
  - 错题知识网络/错题卡/LA-106_强化例题7.4.md
  - 错题知识网络/错题卡/LA-116_2020年第23题.md
  - 错题知识网络/错题卡/LA-062_强化例题3.20.md
  - 错题知识网络/错题卡/LA-063_1000题B组3.8.md
  - 错题知识网络/错题卡/LA-064_1000题B组3.11-3.md
  - 错题知识网络/可视化错题详情/线性代数/LA-061_1000题B组3.7.md
  - 错题知识网络/可视化错题详情/线性代数/LA-106_强化例题7.4.md
  - 错题知识网络/可视化错题详情/线性代数/LA-116_2020年第23题.md
  - 错题知识网络/可视化错题详情/线性代数/LA-062_强化例题3.20.md
  - 错题知识网络/可视化错题详情/线性代数/LA-063_1000题B组3.8.md
  - 错题知识网络/可视化错题详情/线性代数/LA-064_1000题B组3.11-3.md
wrongnet_refs:
  - LA-061
  - LA-106
  - LA-116
  - LA-062
  - LA-063
  - LA-064
method_card_ids:
  - 待匹配
wiki_refs:
  - MATHWIKI-LA-TOPIC-001
  - MATHWIKI-LA-TOPIC-003
  - MATHWIKI-KNOWLEDGE-015
  - MATHWIKI-KNOWLEDGE-030
  - MATHWIKI-KNOWLEDGE-062
status: active
last_updated: 2026-07-02
---

# 矩阵方程按列拆与解空间参数化

这组题的共同入口是：不要把矩阵方程当作一个“大等式”硬算。先把未知矩阵按列拆开，或把换基矩阵的列关系写出来。只要列关系清楚，题目就会落到向量坐标、齐次方程组、非齐次方程组或 Jordan 链。

## 第一动作表

| 题面信号 | 第一动作 | 常见断点 | 来源 |
|---|---|---|---|
| \(P=[\alpha,A\alpha]\)，且 \(AP=PB\) | 写 \(AP=[A\alpha,A^2\alpha]\)，逐列找在基 \((\alpha,A\alpha)\) 下的坐标 | 把 \(AP=PB\) 当普通乘法硬推，没有意识到 \(B\) 的列是坐标列 | [LA-061](http://127.0.0.1:8765/open/LA-061)；[LA-116](http://127.0.0.1:8765/open/LA-116) |
| \(AB=\lambda B\)，或 \(CA^{\mathsf T}=\lambda C\) | 前者直接按 \(B\) 的列读；后者先转置为 \(AC^{\mathsf T}=\lambda C^{\mathsf T}\) 再按列读 | 把矩阵等式整体硬解，或把 \(C\) 的列误当成 \(A\) 的特征向量 | [LA-106](http://127.0.0.1:8765/open/LA-106) |
| \(P^{-1}AP=J\)，其中 \(J\) 为 Jordan 块 | 改写成 \(AP=PJ\)，令 \(P=(a_1,a_2,a_3)\)，按列写链关系 | 随便取 \(P\) 的列，没按目标 Jordan 块构造链 | [LA-062](http://127.0.0.1:8765/open/LA-062) |
| 已知 \(A\) 经初等列变换化为 \(B\)，且要求 \(AP=B\) | 先用列等价保秩求参数，再令 \(P=(p_i)\)，拆成 \(Ap_i=b_i\) | 把列等价误判成相似；求出 \(P\) 后忘查可逆性 | [LA-063](http://127.0.0.1:8765/open/LA-063) |
| \(AB=A\)，且 \(A\) 不可逆 | 先写 \(A(B-E)=O\)，再把 \(B-E\) 的每一列放进 \(\mathcal N(A)\) | 两边错误消去 \(A\)，把奇异矩阵当可逆矩阵 | [LA-064](http://127.0.0.1:8765/open/LA-064) |

## 1. 换基表示：\(AP=PB\)

若 \(P=(p_1,p_2,\ldots,p_n)\)，则

$$
AP=(Ap_1,Ap_2,\ldots,Ap_n).
$$

当 \(AP=PB\) 时，\(B\) 的第 \(i\) 列表示 \(Ap_i\) 在基 \(P\) 下的坐标。

[LA-061](http://127.0.0.1:8765/open/LA-061) 中

$$
P=[\alpha,A\alpha],
\qquad
AP=[A\alpha,A^2\alpha].
$$

因此先写两列的坐标：

$$
A\alpha=0\cdot\alpha+1\cdot A\alpha,
$$

又由

$$
A^2\alpha+A\alpha-2\alpha=0
$$

得

$$
A^2\alpha=2\alpha-A\alpha.
$$

所以

$$
B=
\begin{pmatrix}
0&2\\
1&-1
\end{pmatrix}.
$$

[LA-116](http://127.0.0.1:8765/open/LA-116) 是同一动作的真题版本。先由 \(\alpha\) 不是 \(A\) 的特征向量证明 \(\alpha,A\alpha\) 线性无关，再由

$$
A^2\alpha+A\alpha-6\alpha=0
$$

得

$$
A^2\alpha=6\alpha-A\alpha.
$$

因此

$$
AP=(A\alpha,A^2\alpha)
=(\alpha,A\alpha)
\begin{pmatrix}
0&6\\
1&-1
\end{pmatrix}.
$$

这说明 \(P^{-1}AP\) 不必硬算 \(P^{-1}\)，而是直接读坐标矩阵。

## 1.5 按列读特征向量：\(AB=\lambda B\)

若

$$
B=(\beta_1,\beta_2,\ldots,\beta_m),
$$

则

$$
AB=(A\beta_1,A\beta_2,\ldots,A\beta_m).
$$

所以 \(AB=\lambda B\) 等价于

$$
A\beta_i=\lambda\beta_i\quad (i=1,\ldots,m).
$$

[LA-106](http://127.0.0.1:8765/open/LA-106) 还多了一个转置入口：

$$
CA^{\mathsf T}=2C
\quad\Longleftrightarrow\quad
AC^{\mathsf T}=2C^{\mathsf T}.
$$

转置之后，\(C^{\mathsf T}\) 的列向量才是 \(A\) 的特征向量候选。最后要用秩判断这些候选向量给出几个独立方向。

## 2. Jordan 链：\(P^{-1}AP=J\)

相似关系先改写：

$$
P^{-1}AP=J
\quad\Longleftrightarrow\quad
AP=PJ.
$$

若 \(P=(a_1,a_2,a_3)\)，且

$$
J=
\begin{pmatrix}
0&1&0\\
0&0&1\\
0&0&0
\end{pmatrix},
$$

则

$$
AP=(Aa_1,Aa_2,Aa_3),
\qquad
PJ=(0,a_1,a_2).
$$

因此目标列关系是

$$
Aa_1=0,\qquad Aa_2=a_1,\qquad Aa_3=a_2.
$$

这就是 Jordan 链构造，不是随意找一个可逆矩阵。

## 3. 普通矩阵方程：\(AP=B\)

设

$$
P=(p_1,p_2,\ldots,p_m),
\qquad
B=(b_1,b_2,\ldots,b_m).
$$

则

$$
AP=B
\quad\Longleftrightarrow\quad
Ap_i=b_i\quad (i=1,2,\ldots,m).
$$

所以问题会拆成若干个非齐次线性方程组。若题目要求 \(P\) 可逆，最后必须检查

$$
|P|\ne0.
$$

[LA-063](http://127.0.0.1:8765/open/LA-063) 的稳定链条是：

1. 用列等价保秩先求 \(a=2\)。
2. 解三个方程 \(Ap_i=b_i\)。
3. 用 \(|P|=k_3-k_2\) 得出 \(k_2\ne k_3\)。

## 4. 零空间参数化：\(AB=A\)

若 \(A\) 不可逆，不能两边消去 \(A\)。应先移项：

$$
AB=A
\quad\Longleftrightarrow\quad
A(B-E)=O.
$$

令

$$
B-E=(c_1,c_2,c_3),
$$

则每一列满足

$$
Ac_i=0.
$$

也就是

$$
c_i\in\mathcal N(A).
$$

所以只要求出 \(Ax=0\) 的基础解系，就能把 \(B-E\) 的每一列参数化。[LA-064](http://127.0.0.1:8765/open/LA-064) 中

$$
\mathcal N(A)=\operatorname{span}\{(1,-1,1)^{\mathsf T}\},
$$

于是

$$
B=
\begin{pmatrix}
1+k_1&k_2&k_3\\
-k_1&1-k_2&-k_3\\
k_1&k_2&1+k_3
\end{pmatrix},
$$

并且 \(k_1,k_2,k_3\) 不全为零，才能保证 \(B\ne E\)。

## 边界

本页只根据正式卡、题图和解析图沉淀可复用方法入口。`LA-061` 至 `LA-064` 的用户个人错因、掌握度和 `method_gap` 缺少作答过程证据，仍保留待补充/待评分，不从解析图反推。

## 连接

- 专题总线：[[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- 方程组总线：[[MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线]]
- 知识点簇：[[MATHWIKI-KNOWLEDGE-015_矩阵运算]]；[[MATHWIKI-KNOWLEDGE-030_线性方程组]]；[[MATHWIKI-KNOWLEDGE-062_矩阵秩]]
