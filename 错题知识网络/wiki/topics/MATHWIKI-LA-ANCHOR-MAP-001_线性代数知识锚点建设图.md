---
wiki_id: MATHWIKI-LA-ANCHOR-MAP-001
type: knowledge_anchor_map
title: 线性代数知识锚点建设图
subject: 线性代数
source_refs:
- "错题知识网络/知识点库.md"
status: active
last_updated: '2026-09-11'
---

# 线性代数知识锚点建设图

由参考包 `A-math-anchor-distribution-20260909-01` 的讲义提炼结果落地。本页只组织通用知识锚点与关系提案，不含个人作答证据，不推断错因或掌握度。

## 模块与锚点

### LA01 行列式与余子式

- 上级知识节点：行列式；代数余子式
- 逻辑链：行列式性质 → 按行列展开／基本形 → 高阶结构与递推 → 余子式线性组合 → 伴随矩阵／特征值接口

- 行列式线性性（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-530|行列式初等变换与转置]]
- [[MATHWIKI-KNOWLEDGE-531|三角形、对角形与副对角形行列式]]
- [[MATHWIKI-KNOWLEDGE-532|按行列展开与拉普拉斯分块展开]]
- 范德蒙德行列式（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-533|行和列和与行列式多项式]]
- [[MATHWIKI-KNOWLEDGE-534|加边法与秩一扰动行列式]]
- [[MATHWIKI-KNOWLEDGE-535|递推型行列式]]
- [[MATHWIKI-KNOWLEDGE-536|数学归纳法证明行列式公式]]
- [[MATHWIKI-KNOWLEDGE-537|矩阵乘积与抽象行列式]]
- [[MATHWIKI-KNOWLEDGE-538|余子式与代数余子式符号]]
- [[MATHWIKI-KNOWLEDGE-539|代数余子式线性组合的逆展开]]
- [[MATHWIKI-KNOWLEDGE-540|代数余子式与伴随矩阵、迹的接口]]

### LA02 矩阵结构、运算与特殊矩阵

- 上级知识节点：矩阵运算
- 逻辑链：形状与顺序 → 转置／迹／内外积 → 特殊矩阵 → 幂与多项式 → 分块运算

- [[MATHWIKI-KNOWLEDGE-541|矩阵形状与乘法顺序]]
- [[MATHWIKI-KNOWLEDGE-542|转置运算与对称、反对称分解]]
- [[MATHWIKI-KNOWLEDGE-543|矩阵的迹与平方和判零]]
- [[MATHWIKI-KNOWLEDGE-544|向量内积、外积与秩一分解]]
- [[MATHWIKI-KNOWLEDGE-545|行列求和、复制与缩放的矩阵表达]]
- [[MATHWIKI-KNOWLEDGE-546|秩一矩阵的幂]]
- [[MATHWIKI-KNOWLEDGE-547|低次矩阵关系与幂的递推]]
- [[MATHWIKI-KNOWLEDGE-548|幂零矩阵与有限几何和求逆]]
- [[MATHWIKI-KNOWLEDGE-549|可交换矩阵的二项式展开]]
- [[MATHWIKI-KNOWLEDGE-550|幂等矩阵与对合矩阵]]
- [[MATHWIKI-KNOWLEDGE-551|旋转矩阵与周期矩阵的幂]]
- [[MATHWIKI-KNOWLEDGE-552|分块矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-553|矩阵多项式与矩阵根]]

### LA03 逆、伴随、初等变换与矩阵方程

- 上级知识节点：逆矩阵；初等变换；矩阵运算
- 逻辑链：可逆条件 → 求逆与伴随 → 行列变换 → 矩阵等价 → 矩阵方程按列还原

- [[MATHWIKI-KNOWLEDGE-554|可逆矩阵的等价条件网络]]
- [[MATHWIKI-KNOWLEDGE-555|逆矩阵运算与乘积逆序]]
- [[MATHWIKI-KNOWLEDGE-556|初等变换求逆与伴随公式求逆]]
- [[MATHWIKI-KNOWLEDGE-557|矩阵多项式关系求逆]]
- [[MATHWIKI-KNOWLEDGE-558|伴随矩阵定义与基本恒等式]]
- [[MATHWIKI-KNOWLEDGE-559|伴随矩阵的秩与二次伴随]]
- [[MATHWIKI-KNOWLEDGE-560|初等矩阵的左乘、右乘与逆]]
- [[MATHWIKI-KNOWLEDGE-561|初等变换的对象保持范围]]
- [[MATHWIKI-KNOWLEDGE-562|矩阵等价及等价标准形]]
- [[MATHWIKI-KNOWLEDGE-563|满秩分解与降维计算矩阵幂]]
- [[MATHWIKI-KNOWLEDGE-564|可逆情形的矩阵方程]]
- [[MATHWIKI-KNOWLEDGE-565|奇异或矩形情形的矩阵方程]]

### LA04 秩、零空间与分块关系

- 上级知识节点：矩阵秩
- 逻辑链：子式／阶梯形 → 满秩与消去 → 秩不等式 → 列空间、核与分块关系

- [[MATHWIKI-KNOWLEDGE-566|矩阵秩的定义与计算]]
- [[MATHWIKI-KNOWLEDGE-567|满行秩、满列秩与消去条件]]
- [[MATHWIKI-KNOWLEDGE-568|秩的和、差与拼接不等式]]
- [[MATHWIKI-KNOWLEDGE-569|乘积秩与Sylvester、Frobenius不等式]]
- [[MATHWIKI-KNOWLEDGE-570|零乘积与列空间落入零空间]]
- [[MATHWIKI-KNOWLEDGE-571|分块初等变换求秩]]
- [[MATHWIKI-KNOWLEDGE-572|格拉姆矩阵的秩与核]]
- [[MATHWIKI-KNOWLEDGE-573|多项式分解给出的互补秩]]
- [[MATHWIKI-KNOWLEDGE-574|矩阵幂的秩稳定与链式无关]]

### LA05 向量组、基与坐标

- 上级知识节点：向量组线性相关；向量组线性无关
- 逻辑链：线性表示 → 相关／无关 → 极大无关组和秩 → 张成空间与等价 → 基、坐标和换基

- [[MATHWIKI-KNOWLEDGE-575|向量线性表示与系数唯一性]]
- 向量组线性相关（复用本地已有规范键，未新建页面）
- 向量组线性无关（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-576|增减向量与增减分量的相关性]]
- [[MATHWIKI-KNOWLEDGE-577|向量组的秩与极大线性无关组]]
- [[MATHWIKI-KNOWLEDGE-578|向量组线性表示方向与秩比较]]
- [[MATHWIKI-KNOWLEDGE-579|向量组等价与张成空间]]
- [[MATHWIKI-KNOWLEDGE-580|向量空间的基、维数与坐标]]
- [[MATHWIKI-KNOWLEDGE-581|过渡矩阵与坐标变换方向]]
- [[MATHWIKI-KNOWLEDGE-582|正交向量组与施密特正交化]]
- [[MATHWIKI-KNOWLEDGE-583|正交补与解空间维数]]
- [[MATHWIKI-KNOWLEDGE-584|正交三角分解的题型接口]]

### LA06 线性方程组

- 上级知识节点：线性方程组；基础解系
- 逻辑链：消元与相容 → 齐次基础解系 → 非齐次特解＋核 → 公共解／同解／包含 → 几何解释

- [[MATHWIKI-KNOWLEDGE-585|消元、主变量与自由变量]]
- [[MATHWIKI-KNOWLEDGE-586|线性方程组的相容性与解的个数]]
- 基础解系（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-587|齐次通解与秩—零度联系]]
- [[MATHWIKI-KNOWLEDGE-588|非齐次通解与仿射解结构]]
- [[MATHWIKI-KNOWLEDGE-589|已知解向量反推未知系统]]
- [[MATHWIKI-KNOWLEDGE-590|公共解与解空间交集]]
- [[MATHWIKI-KNOWLEDGE-591|齐次同解与行空间等价]]
- [[MATHWIKI-KNOWLEDGE-592|解集包含与非齐次同解]]
- [[MATHWIKI-KNOWLEDGE-593|方程组与直线、平面位置关系]]
- [[MATHWIKI-KNOWLEDGE-594|正规方程的可解性接口]]
- [[MATHWIKI-KNOWLEDGE-595|矩形矩阵左逆、右逆的构造]]

### LA07 特征值、特征向量与多项式

- 上级知识节点：特征值与特征向量
- 逻辑链：非零特征向量定义 → 特征方程 → 特征子空间 → 谱映射与重数 → 矩阵条件反推

- [[MATHWIKI-KNOWLEDGE-596|特征值与特征向量的定义]]
- 特征多项式（复用本地已有规范键，未新建页面）
- 特征方程（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-597|代数重数与几何重数]]
- [[MATHWIKI-KNOWLEDGE-598|特征向量线性组合与不同特征子空间]]
- [[MATHWIKI-KNOWLEDGE-599|迹、行列式与特征值]]
- 矩阵多项式的谱映射（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-600|湮灭多项式与凯莱—哈密顿定理]]
- [[MATHWIKI-KNOWLEDGE-601|转置矩阵与左右特征向量]]
- [[MATHWIKI-KNOWLEDGE-602|抽象线性作用与基下矩阵]]
- [[MATHWIKI-KNOWLEDGE-603|可交换矩阵与共同特征方向]]

### LA08 相似、正交与谱分解

- 上级知识节点：相似矩阵；实对称矩阵
- 逻辑链：相似定义和不变量 → 可对角化判据 → 实对称的正交化 → 谱分解 → 幂、递推与矩阵重建

- 相似矩阵（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-604|相似对角化的充要条件]]
- [[MATHWIKI-KNOWLEDGE-605|可对角化的典型充分条件与反例]]
- [[MATHWIKI-KNOWLEDGE-606|实对称矩阵的谱性质]]
- [[MATHWIKI-KNOWLEDGE-607|实对称矩阵的正交对角化]]
- 正交矩阵（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-608|实对称矩阵的谱分解与重建]]
- [[MATHWIKI-KNOWLEDGE-609|相似变换计算幂与线性递推]]
- [[MATHWIKI-KNOWLEDGE-610|相似关系在同一矩阵函数下的保持]]

### LA09 二次型、合同与惯性

- 上级知识节点：二次型
- 逻辑链：对称矩阵表示 → 可逆变量替换 → 标准形／规范形 → 惯性指数 → 合同判定与构造

- [[MATHWIKI-KNOWLEDGE-611|二次型的对称矩阵表示]]
- [[MATHWIKI-KNOWLEDGE-612|二次型标准形与规范形]]
- [[MATHWIKI-KNOWLEDGE-613|配方法及变换可逆性]]
- [[MATHWIKI-KNOWLEDGE-614|正交变换化二次型]]
- [[MATHWIKI-KNOWLEDGE-615|平方和与“伪配方法”]]
- [[MATHWIKI-KNOWLEDGE-616|惯性定理、正负惯性指数与秩]]
- [[MATHWIKI-KNOWLEDGE-617|合同关系的判定与构造]]
- [[MATHWIKI-KNOWLEDGE-618|等价、相似、合同三者的区分]]
- [[MATHWIKI-KNOWLEDGE-619|正交合同变换的传递与构造]]
- [[MATHWIKI-KNOWLEDGE-620|二次型与二次曲面类型的接口]]

### LA10 正定、Gram分解与二次型最值

- 上级知识节点：正定矩阵；二次型
- 逻辑链：严格正值定义 → 谱／主子式／Gram判据 → 参数与分解 → 普通及正定分母二次型比值

- 正定矩阵（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-621|顺序主子式判定正定]]
- [[MATHWIKI-KNOWLEDGE-622|正定、半正定、负定与不定的区分]]
- [[MATHWIKI-KNOWLEDGE-623|Gram分解与平方和表示]]
- [[MATHWIKI-KNOWLEDGE-624|正定性的保持与矩阵乘积条件]]
- [[MATHWIKI-KNOWLEDGE-625|实对称正定平方根的谱构造]]
- [[MATHWIKI-KNOWLEDGE-626|单位球面二次型最值与谱界]]
- [[MATHWIKI-KNOWLEDGE-627|正定分母的二次型比值最值]]
- [[MATHWIKI-KNOWLEDGE-628|二次型恒等式与行列式型参数题]]

## 关系提案

以下关系来自本参考包，`accepted=false`，尚未作为本地正式关系生效；前置是学习依赖，不是数学等号。

- `prerequisite` LA01.11 → LA01.12：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA01.12 → LA03.05：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA03.05 → LA03.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA02.01 → LA02.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA02.04 → LA02.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA03.07 → LA04.01：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA04.01 → LA05.05：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA05.05 → LA05.08：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA05.08 → LA05.09：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA03.07 → LA06.01：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA06.01 → LA06.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA06.02 → LA06.03：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA06.03 → LA06.05：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA06.05 → LA06.07：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA04.01 → LA04.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA04.02 → LA04.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA04.04 → LA04.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA05.01 → LA05.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA05.02 → LA05.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA05.06 → LA05.07：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA05.03 → LA05.10：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA05.10 → LA05.12：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA06.03 → LA07.01：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA07.01 → LA07.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA07.02 → LA07.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA07.04 → LA08.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA07.01 → LA07.07：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA07.07 → LA03.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA08.04 → LA08.05：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA08.05 → LA08.07：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA08.07 → LA10.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA09.01 → LA09.03：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA09.03 → LA09.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA09.06 → LA09.07：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA09.01 → LA09.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA09.04 → LA10.01：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA10.01 → LA10.07：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` LA10.07 → LA10.08：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `contrast` LA03.09 → LA05.07：同型矩阵等价由秩刻画；向量组等价还要求张成空间相同。
- `contrast` LA03.09 → LA08.01：初等等价与相似变换作用不同；同秩不推出相似。
- `contrast` LA08.01 → LA09.07：相似是P⁻¹AP，合同是CᵀAC；仅在正交变换等特定条件下二者重合。
- `contrast` LA05.02 → LA05.03：全组相关／无关是整体定义，不等同于两两关系。
- `contrast` LA05.09 → LA07.10：基的列变换与坐标逆变换必须约定方向；两者不是同一个对象。
- `contrast` LA06.07 → LA06.08：存在公共非零解不等于同解；交集非平凡不等于解空间相同。
- `contrast` LA07.02 → LA07.08：湮灭多项式不必是特征多项式；根集合与根重数不能直接替换。
- `contrast` LA07.04 → LA08.02：有重特征值不必不可对角化；须检查每根的几何重数。
- `contrast` LA09.02 → LA09.06：标准形保留一般对角系数，规范形缩放到±1、0；惯性指数是不变量。
- `contrast` LA10.01 → LA10.03：正定是严格正；半正定可有零特征值，不能只用同一个顺序主子式严格判据。
- `equivalent_under_condition` LA03.01 → LA06.02：n阶方阵A：可逆等价于对每个b都有唯一解；单个右端有解不够。
- `application` LA04.07 → LA06.11：实矩阵的Gram核相等性质，用于正规方程的相容性。
- `specialization` LA08.06 → LA09.04：正交Q满足Q⁻¹=Qᵀ，故正交合同同时是相似。
- `application` LA08.07 → LA10.04：实对称正定A可由正特征值构造平方根及Gram因子；不写唯一一般因子。
- `cross_branch_application` LA01.10 → PR06.06：二维变量变换中Jacobian为行列式；取反变换及绝对值并核对支持。
- `cross_branch_application` LA09.01 → PR07.06：随机线性组合方差可整理成协方差矩阵的二次型；不是把所有矩阵二次型当概率密度。
- `cross_branch_application` LA10.03 → PR13.06：协方差矩阵至少半正定；带逆矩阵和行列式分母的非退化正态密度需正定。
- `cross_branch_application` LA03.02 → PR13.06：正态密度的二次型使用协方差矩阵的逆，归一化使用其行列式。
- `cross_branch_application` LA08.06 → PR09.13：标准联合正态的正交线性变换为独立标准正态结构提供接口；只保协方差不代表任意分布仍独立。
- `cross_branch_application` LA10.07 → PR07.17：方差／相关系数参数优化与对称二次型的谱界相通，须对应相同约束和实对称条件。
- `cross_branch_application` LA01.03 → PR03.01：题本用独立0—1变量作矩阵元素；行列式事件应先化成具体随机变量事件，再使用独立性。
