---
wiki_id: MATHWIKI-PR-ANCHOR-MAP-001
type: knowledge_anchor_map
title: 概率论与数理统计知识锚点建设图
subject: 概率论与数理统计
source_refs:
- "错题知识网络/知识点库.md"
status: active
last_updated: '2026-09-11'
---

# 概率论与数理统计知识锚点建设图

由参考包 `A-math-anchor-distribution-20260909-01` 的讲义提炼结果落地。本页只组织通用知识锚点与关系提案，不含个人作答证据，不推断错因或掌握度。

## 模块与锚点

### PR01 随机事件、概率与条件化

- 上级知识节点：随机事件与概率；条件概率；独立性
- 逻辑链：样本空间 → 事件集合运算 → 概率公理 → 条件概率／乘法 → 完备分割与全概率 → 贝叶斯 → 独立性

- [[MATHWIKI-KNOWLEDGE-629|随机试验、样本空间与事件]]
- [[MATHWIKI-KNOWLEDGE-630|事件的包含、相等、互斥与对立]]
- [[MATHWIKI-KNOWLEDGE-631|事件并、交、差、补与运算律]]
- [[MATHWIKI-KNOWLEDGE-632|至少、至多、恰好与发生次数的事件表达]]
- [[MATHWIKI-KNOWLEDGE-633|概率的公理、单调性与界]]
- [[MATHWIKI-KNOWLEDGE-634|加法公式、减法公式与容斥]]
- [[MATHWIKI-KNOWLEDGE-635|计数原则、排列与组合]]
- [[MATHWIKI-KNOWLEDGE-636|古典概型的抽样与分配模型]]
- [[MATHWIKI-KNOWLEDGE-637|几何概型与随机区域]]
- 条件概率（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-638|乘法公式与顺序事件链]]
- [[MATHWIKI-KNOWLEDGE-639|完备事件组与全概率公式]]
- 贝叶斯公式（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-640|两个事件独立与补事件保持]]
- [[MATHWIKI-KNOWLEDGE-641|两两独立、相互独立与分组保持]]
- [[MATHWIKI-KNOWLEDGE-642|独立重复试验与停止规则]]
- [[MATHWIKI-KNOWLEDGE-643|事件“相互有利”的条件概率比较]]

### PR02 随机变量、分布函数与分布合法性

- 上级知识节点：随机变量分布；分布函数
- 逻辑链：随机变量 → 一般分布函数 → 跳跃与端点 → 离散分布律／连续密度 → 混合类型

- [[MATHWIKI-KNOWLEDGE-644|随机变量与随机事件的对应]]
- 分布函数（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-645|分布函数的跳跃、单点质量与开闭端点]]
- [[MATHWIKI-KNOWLEDGE-646|分布律与离散分布函数的互换]]
- [[MATHWIKI-KNOWLEDGE-647|密度的非负性、归一性与概率积分]]
- [[MATHWIKI-KNOWLEDGE-648|连续型密度与分布函数的微积分关系]]
- [[MATHWIKI-KNOWLEDGE-649|分段分布、端点与待定参数]]
- [[MATHWIKI-KNOWLEDGE-650|混合分布与离散原子]]
- [[MATHWIKI-KNOWLEDGE-651|同分布、几乎处处相等与同矩的层级]]
- [[MATHWIKI-KNOWLEDGE-652|分布函数和密度的组合合法性]]

### PR03 常用分布与分布模型

- 上级知识节点：离散型随机变量；连续型随机变量
- 逻辑链：试验机制 → 随机量和支持 → 参数约定 → 分布律／密度 → 数字特征 → 闭包或近似

- [[MATHWIKI-KNOWLEDGE-653|0—1分布与指示变量]]
- [[MATHWIKI-KNOWLEDGE-654|二项分布]]
- [[MATHWIKI-KNOWLEDGE-655|二项概率的递推、众数与奇偶计数]]
- [[MATHWIKI-KNOWLEDGE-656|泊松分布]]
- [[MATHWIKI-KNOWLEDGE-657|泊松近似二项与泊松定理]]
- [[MATHWIKI-KNOWLEDGE-658|几何分布与离散无记忆性]]
- [[MATHWIKI-KNOWLEDGE-659|超几何分布与无放回计数]]
- [[MATHWIKI-KNOWLEDGE-660|一维均匀分布]]
- [[MATHWIKI-KNOWLEDGE-661|指数分布与连续无记忆性]]
- [[MATHWIKI-KNOWLEDGE-662|泊松计数与等待时间转换]]
- [[MATHWIKI-KNOWLEDGE-663|正态分布的参数、对称与标准化]]
- [[MATHWIKI-KNOWLEDGE-664|正态分位数与概率反求参数]]
- [[MATHWIKI-KNOWLEDGE-665|指数二次型密度的配方识别]]
- [[MATHWIKI-KNOWLEDGE-666|独立和的分布闭包]]
- [[MATHWIKI-KNOWLEDGE-667|双侧指数型、对数变换型等题目密度模型]]
- [[MATHWIKI-KNOWLEDGE-668|多项式分布]]
- [[MATHWIKI-KNOWLEDGE-669|第r次成功与帕斯卡分布]]
- [[MATHWIKI-KNOWLEDGE-670|Γ分布与连续第r次到达]]
- [[MATHWIKI-KNOWLEDGE-671|贝塔分布及均匀样本最大值接口]]
- [[MATHWIKI-KNOWLEDGE-672|概率生成函数的题型接口]]
- [[MATHWIKI-KNOWLEDGE-673|泊松计数的独立筛选（二项条件混合）]]

### PR04 一维随机变量函数的分布

- 上级知识节点：随机变量分布；分布函数
- 逻辑链：先求变换值域 → 离散同值合并／连续逆像 → 单调Jacobian或分支积分 → 原子和端点检查

- [[MATHWIKI-KNOWLEDGE-674|离散变量函数的分布与同值合并]]
- [[MATHWIKI-KNOWLEDGE-675|分布函数法求变换分布]]
- [[MATHWIKI-KNOWLEDGE-676|单调变换的密度公式]]
- [[MATHWIKI-KNOWLEDGE-677|非单调、多分支变换]]
- [[MATHWIKI-KNOWLEDGE-678|平移、缩放与反射变换]]
- [[MATHWIKI-KNOWLEDGE-679|截顶、阈值与混合型变换]]
- [[MATHWIKI-KNOWLEDGE-680|限尾与切尾的区分]]
- [[MATHWIKI-KNOWLEDGE-681|分布函数变换到均匀分布]]
- [[MATHWIKI-KNOWLEDGE-682|逆分布变换及标准指数变换]]
- [[MATHWIKI-KNOWLEDGE-683|正态变量的指数、平方与绝对值变换]]

### PR05 多维分布、条件分布与独立性

- 上级知识节点：二维随机变量；边缘分布；条件分布；独立性
- 逻辑链：联合分布 → 边缘化 → 条件化 → 独立性判据 → 二维均匀／正态 → 退化与混合联合模型

- [[MATHWIKI-KNOWLEDGE-684|联合分布函数与矩形增量]]
- 边缘分布（复用本地已有规范键，未新建页面）
- [[MATHWIKI-KNOWLEDGE-685|二维离散联合分布表]]
- [[MATHWIKI-KNOWLEDGE-686|离散条件分布]]
- [[MATHWIKI-KNOWLEDGE-687|二维密度的支持、归一化与区域概率]]
- [[MATHWIKI-KNOWLEDGE-688|条件密度与固定点条件]]
- [[MATHWIKI-KNOWLEDGE-689|条件为取值与条件为区间事件]]
- [[MATHWIKI-KNOWLEDGE-690|由边缘和条件重建联合分布]]
- [[MATHWIKI-KNOWLEDGE-691|随机变量独立的等价判据]]
- [[MATHWIKI-KNOWLEDGE-692|独立变量函数及互不重叠分组]]
- [[MATHWIKI-KNOWLEDGE-693|二维均匀分布]]
- [[MATHWIKI-KNOWLEDGE-694|二维正态分布及参数识别]]
- [[MATHWIKI-KNOWLEDGE-695|二维正态中的独立、不相关与线性组合]]
- [[MATHWIKI-KNOWLEDGE-696|奇异联合分布与确定函数关系]]
- [[MATHWIKI-KNOWLEDGE-697|离散—连续混合联合模型]]

### PR06 多维变量函数、和积商与极值

- 上级知识节点：二维随机变量；随机变量分布
- 逻辑链：联合支持 → 函数的逆像事件 → 分布函数法／积分变换 → 多分支 → 和积商、极值与联合变换

- [[MATHWIKI-KNOWLEDGE-698|二维离散函数的分布]]
- [[MATHWIKI-KNOWLEDGE-699|二维函数的分布函数法与分区]]
- [[MATHWIKI-KNOWLEDGE-700|和、差与线性组合的卷积型公式]]
- [[MATHWIKI-KNOWLEDGE-701|乘积和商的分布]]
- [[MATHWIKI-KNOWLEDGE-702|绝对值差、距离与径向变量]]
- [[MATHWIKI-KNOWLEDGE-703|二维联合变换与Jacobian]]
- [[MATHWIKI-KNOWLEDGE-704|最大值和最小值的分布]]
- [[MATHWIKI-KNOWLEDGE-705|多个独立同分布变量的极值]]
- [[MATHWIKI-KNOWLEDGE-706|最大值与最小值的联合分布]]
- [[MATHWIKI-KNOWLEDGE-707|条件抽样与混合变换的全概率路线]]

### PR07 期望、方差、矩与相关

- 上级知识节点：数字特征；协方差与相关系数
- 逻辑链：分布 → 可积性 → 期望线性 → 二阶矩／方差 → 混合矩与协方差 → 相关系数 → 独立性的特殊联系

- [[MATHWIKI-KNOWLEDGE-708|数学期望的存在性与定义]]
- [[MATHWIKI-KNOWLEDGE-709|随机变量函数的期望]]
- [[MATHWIKI-KNOWLEDGE-710|期望线性与指示变量拆分]]
- [[MATHWIKI-KNOWLEDGE-711|独立乘积期望与分组因式分解]]
- [[MATHWIKI-KNOWLEDGE-712|方差与二阶原点矩]]
- [[MATHWIKI-KNOWLEDGE-713|线性组合的方差与协方差项]]
- [[MATHWIKI-KNOWLEDGE-714|独立乘积的方差]]
- [[MATHWIKI-KNOWLEDGE-715|方差为零与最小均方误差常数]]
- [[MATHWIKI-KNOWLEDGE-716|原点矩、中心矩与混合矩]]
- [[MATHWIKI-KNOWLEDGE-717|协方差的定义与双线性]]
- [[MATHWIKI-KNOWLEDGE-718|相关系数及线性变换规则]]
- [[MATHWIKI-KNOWLEDGE-719|完全相关与几乎处处线性关系]]
- [[MATHWIKI-KNOWLEDGE-720|独立与不相关的逻辑边界]]
- [[MATHWIKI-KNOWLEDGE-721|二维正态与两点变量的不相关特例]]
- [[MATHWIKI-KNOWLEDGE-722|对称性、绝对值与截顶函数的矩]]
- [[MATHWIKI-KNOWLEDGE-723|条件化计算数字特征]]
- [[MATHWIKI-KNOWLEDGE-724|方差与相关系数优化]]

### PR08 大数定律、切比雪夫与中心极限定理

- 上级知识节点：大数定律；中心极限定理
- 逻辑链：概率界 → 依概率收敛 → 大数定律稳定值 → 中心极限定理波动尺度 → 有限样本近似与误差界区别

- [[MATHWIKI-KNOWLEDGE-725|切比雪夫不等式]]
- [[MATHWIKI-KNOWLEDGE-726|依概率收敛]]
- [[MATHWIKI-KNOWLEDGE-727|切比雪夫大数定律]]
- [[MATHWIKI-KNOWLEDGE-728|辛钦大数定律与伯努利大数定律]]
- [[MATHWIKI-KNOWLEDGE-729|变换样本及分组序列的定律适用性]]
- [[MATHWIKI-KNOWLEDGE-730|独立同分布中心极限定理]]
- [[MATHWIKI-KNOWLEDGE-731|棣莫弗—拉普拉斯与二项正态近似]]
- [[MATHWIKI-KNOWLEDGE-732|样本量、容量与整数阈值反求]]

### PR09 样本、统计量与抽样分布

- 上级知识节点：抽样分布
- 逻辑链：总体与样本 → 样本统计量 → 正态／χ²／t／F构造 → 样本均值方差独立 → 单双总体抽样

- [[MATHWIKI-KNOWLEDGE-733|总体、简单随机样本与样本值]]
- [[MATHWIKI-KNOWLEDGE-734|统计量与未知参数排除]]
- [[MATHWIKI-KNOWLEDGE-735|样本均值、样本方差与样本矩]]
- [[MATHWIKI-KNOWLEDGE-736|经验分布函数]]
- [[MATHWIKI-KNOWLEDGE-737|顺序统计量、最大最小样本与极差]]
- [[MATHWIKI-KNOWLEDGE-738|χ²分布的构造与自由度]]
- [[MATHWIKI-KNOWLEDGE-739|t分布的构造]]
- [[MATHWIKI-KNOWLEDGE-740|F分布的构造]]
- [[MATHWIKI-KNOWLEDGE-741|t、F与χ²的关系及分位数]]
- [[MATHWIKI-KNOWLEDGE-742|正态样本均值的精确分布]]
- [[MATHWIKI-KNOWLEDGE-743|正态样本方差、已知均值平方和与自由度]]
- [[MATHWIKI-KNOWLEDGE-744|正态样本均值与样本方差独立]]
- [[MATHWIKI-KNOWLEDGE-745|正态线性组合的独立性与平方和分解]]
- [[MATHWIKI-KNOWLEDGE-746|双总体抽样与合并方差]]
- [[MATHWIKI-KNOWLEDGE-747|新观测与样本均值之差的抽样分布]]

### PR10 点估计、矩估计、最大似然与评价

- 上级知识节点：参数估计
- 逻辑链：参数与估计量 → 选择可识别的矩／似然 → 支持约束 → 求候选与极大性 → 偏差、方差、一致性与均方误差

- [[MATHWIKI-KNOWLEDGE-748|点估计量与估计值]]
- [[MATHWIKI-KNOWLEDGE-749|矩估计的基本构造]]
- [[MATHWIKI-KNOWLEDGE-750|一阶矩失效与高阶矩、绝对矩]]
- [[MATHWIKI-KNOWLEDGE-751|似然函数与对数似然]]
- [[MATHWIKI-KNOWLEDGE-752|内点极大、边界极大与多解]]
- [[MATHWIKI-KNOWLEDGE-753|参数出现在支持中的最大似然]]
- [[MATHWIKI-KNOWLEDGE-754|多参数模型与联合样本估计]]
- [[MATHWIKI-KNOWLEDGE-755|正态均值、方差的矩估计与最大似然]]
- [[MATHWIKI-KNOWLEDGE-756|估计参数函数与似然不变性]]
- [[MATHWIKI-KNOWLEDGE-757|变换后观测的估计模型]]
- [[MATHWIKI-KNOWLEDGE-758|估计量的无偏性与偏差修正]]
- [[MATHWIKI-KNOWLEDGE-759|无偏估计的有效性与最小方差权重]]
- [[MATHWIKI-KNOWLEDGE-760|一致性及均方一致的充分条件]]
- [[MATHWIKI-KNOWLEDGE-761|均方误差与偏差—方差权衡]]
- [[MATHWIKI-KNOWLEDGE-762|绝对偏差似然与样本中位数型极大]]

### PR11 区间估计与枢轴

- 上级知识节点：参数估计；抽样分布
- 逻辑链：置信水平 → 枢轴分布 → 分位数和尾部 → 不等式反解 → 条件、宽度与变换

- [[MATHWIKI-KNOWLEDGE-763|置信区间与置信水平的解释]]
- [[MATHWIKI-KNOWLEDGE-764|枢轴量构造与不等式反演]]
- [[MATHWIKI-KNOWLEDGE-765|单正态总体均值区间]]
- [[MATHWIKI-KNOWLEDGE-766|单正态总体方差和标准差区间]]
- [[MATHWIKI-KNOWLEDGE-767|双正态总体均值差区间]]
- [[MATHWIKI-KNOWLEDGE-768|双正态总体方差比区间]]
- [[MATHWIKI-KNOWLEDGE-769|非正态模型的精确区间]]
- [[MATHWIKI-KNOWLEDGE-770|参数单调变换的置信区间]]
- [[MATHWIKI-KNOWLEDGE-771|区间宽度、置信水平与样本容量]]

### PR12 假设检验

- 上级知识节点：假设检验；抽样分布
- 逻辑链：业务方向 → H0/H1 → H0下统计量 → 显著性水平和拒绝域 → 样本结论 → 两类错误／区间联系

- [[MATHWIKI-KNOWLEDGE-772|原假设、备择假设与检验方向]]
- [[MATHWIKI-KNOWLEDGE-773|显著性水平与拒绝域]]
- [[MATHWIKI-KNOWLEDGE-774|第一类错误与第二类错误]]
- [[MATHWIKI-KNOWLEDGE-775|单正态总体均值的Z／t检验]]
- [[MATHWIKI-KNOWLEDGE-776|单正态总体方差的χ²检验]]
- [[MATHWIKI-KNOWLEDGE-777|双正态总体均值差检验]]
- [[MATHWIKI-KNOWLEDGE-778|双正态总体方差比F检验]]
- [[MATHWIKI-KNOWLEDGE-779|拒绝域、置信区间与水平变化]]
- [[MATHWIKI-KNOWLEDGE-780|检验结论的表述与数据单位]]

### PR13 选学深化：条件矩与正态矩阵结构

- 上级知识节点：数字特征；条件分布；协方差与相关系数
- 逻辑链：条件分布 → 条件期望／条件方差 → 全期望与全方差 → 最优平方预测；协方差矩阵 → 二次型正态密度 → 条件与线性变换

- [[MATHWIKI-KNOWLEDGE-781|条件数学期望]]
- [[MATHWIKI-KNOWLEDGE-782|亚当公式（全期望公式）]]
- [[MATHWIKI-KNOWLEDGE-783|条件期望的线性、可提出量与独立性]]
- [[MATHWIKI-KNOWLEDGE-784|条件方差与夏娃公式（全方差公式）]]
- [[MATHWIKI-KNOWLEDGE-785|条件期望的最小均方预测性质]]
- [[MATHWIKI-KNOWLEDGE-786|协方差矩阵与多元正态的二次型表示]]
- [[MATHWIKI-KNOWLEDGE-787|二维正态条件分布与条件矩]]
- [[MATHWIKI-KNOWLEDGE-788|正态线性变换与二次型配方的跨分支接口]]

## 关系提案

以下关系来自本参考包，`accepted=false`，尚未作为本地正式关系生效；前置是学习依赖，不是数学等号。

- `prerequisite` PR01.01 → PR01.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR01.02 → PR01.03：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR01.03 → PR01.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR01.06 → PR01.10：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR01.10 → PR01.11：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR01.11 → PR01.12：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR01.12 → PR01.13：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR01.07 → PR01.08：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR01.08 → PR03.07：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR01.14 → PR01.15：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR01.15 → PR01.16：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR01.16 → PR03.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR03.02 → PR03.05：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR02.01 → PR02.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR02.02 → PR02.03：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR02.03 → PR02.07：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR02.07 → PR02.08：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR02.04 → PR04.01：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR04.01 → PR06.01：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR02.05 → PR02.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR02.06 → PR04.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR04.02 → PR04.03：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR04.03 → PR04.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR03.11 → PR03.12：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR03.12 → PR09.10：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR05.01 → PR05.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR05.02 → PR05.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR05.04 → PR05.08：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR05.05 → PR05.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR05.06 → PR05.07：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR05.09 → PR05.10：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR05.10 → PR05.13：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR05.05 → PR06.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR06.02 → PR06.03：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR06.03 → PR06.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR06.07 → PR06.08：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR06.08 → PR09.05：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR09.05 → PR10.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR07.01 → PR07.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR07.02 → PR07.05：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR07.05 → PR07.10：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR07.10 → PR07.11：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR07.11 → PR07.12：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR07.03 → PR07.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR07.06 → PR07.17：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR07.05 → PR08.01：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR08.01 → PR08.03：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR08.03 → PR08.05：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR08.02 → PR08.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR08.04 → PR10.13：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR03.11 → PR08.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR08.06 → PR08.07：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR08.07 → PR08.08：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR09.01 → PR09.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR09.02 → PR09.03：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR09.03 → PR09.11：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR09.11 → PR09.12：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR03.11 → PR09.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR09.06 → PR09.07：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR09.07 → PR09.09：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR09.06 → PR09.08：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR09.08 → PR09.14：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR09.03 → PR10.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR10.02 → PR10.03：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR09.01 → PR10.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR10.04 → PR10.05：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR10.05 → PR10.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR10.06 → PR10.07：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR10.01 → PR10.11：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR10.11 → PR10.12：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR10.12 → PR10.14：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR11.01 → PR11.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR11.02 → PR11.03：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR11.03 → PR11.09：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR11.02 → PR11.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR11.04 → PR11.06：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR12.01 → PR12.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR12.02 → PR12.03：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR12.03 → PR12.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR12.04 → PR12.09：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR05.06 → PR13.01：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR13.01 → PR13.02：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR13.02 → PR13.04：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR13.04 → PR13.05：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR03.02 → PR03.16：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR03.06 → PR03.17：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR03.17 → PR03.18：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR02.04 → PR03.20：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `prerequisite` PR01.12 → PR03.21：建议的学习／调用前置，不是逻辑充分条件；允许其他学习顺序。
- `contrast` PR01.02 → PR01.14：互斥是集合空交；独立是概率乘积。概率均正的两个互斥事件不独立。
- `contrast` PR01.14 → PR01.15：三个以上事件：只检查两两乘积不等于相互独立。
- `contrast` PR01.10 → PR05.06：正概率事件条件与连续取值条件的定义途径不同；不能把P(Y=y)=0直接放进普通比值。
- `contrast` PR02.03 → PR02.05：分布函数跳跃给单点质量；密度值本身不是概率。
- `contrast` PR02.06 → PR02.08：原子不能靠普通求导保留；混合型变量需同时存跳跃质量与连续部分。
- `contrast` PR03.02 → PR03.07：固定次数独立试验与有限总体不放回抽样的机制不同。
- `contrast` PR03.02 → PR03.17：固定n数成功次数，与固定r数等待次数，支持和随机量均不同。
- `contrast` PR04.06 → PR04.07：改记越界数值与删除越界样本后条件化是不同操作。
- `contrast` PR05.02 → PR05.09：边缘分布不能一般决定联合分布；独立时方可乘起来。
- `contrast` PR05.06 → PR05.07：条件Y=y和条件a<Y<b不是同一个条件分布。
- `contrast` PR03.11 → PR05.12：X、Y分别正态不自动组成二维正态；和正态也须核对联合条件。
- `contrast` PR05.09 → PR07.13：独立在矩存在时推出不相关；不相关不能一般反推独立。
- `contrast` PR07.02 → PR07.03：E[g(X)]一般不等于g(EX)；线性是特例。
- `contrast` PR08.04 → PR08.06：大数定律研究平均值趋稳，中心极限定理研究标准化波动的分布极限。
- `contrast` PR09.03 → PR10.08：样本无偏方差通常除n−1；正态方差MLE通常除n，字段不能混名。
- `contrast` PR10.11 → PR10.13：无偏与一致分别是有限样本期望和大样本收敛，不能互相替代。
- `contrast` PR10.12 → PR10.14：最小方差的比较范围常限于无偏类；允许有偏时需用MSE比较。
- `contrast` PR11.01 → PR12.02：置信度描述区间程序覆盖率；显著性水平约束拒绝真原假设的风险，语义不同。
- `contrast` PR12.02 → PR12.03：α与β对应不同真实状态，通常不互为补数。
- `contrast` PR03.19 → PR01.13：贝塔分布和贝叶斯公式不是别名，不建立等价合并边。
- `specialization` PR01.09 → PR05.11：二维均匀分布下，区域概率为面积比；非矩形支持的边缘通常不均匀。
- `analogy` PR03.09 → PR03.06：连续等待与离散等待均有相应无记忆形式；不是同分布或同一支持。
- `equivalent_under_condition` PR05.13 → PR07.13：二维联合正态、方差正时，不相关等价于独立；去掉联合正态条件不成立。
- `equivalent_under_condition` PR03.01 → PR07.14：两个非退化两点随机变量的不相关与独立可相互推出；不推广到任意离散支持。
- `specialization` PR03.06 → PR03.17：r=1时第r次成功总试验次数退化为几何模型。
- `specialization` PR03.09 → PR03.18：Γ分布形状参数为1时，与同率指数分布对应。
- `application` PR04.08 → PR04.09：连续分布积分变换后再作逆函数或对数变换，保留来源单调条件。
- `application` PR01.12 → PR06.10：按离散条件分支求Y或g(X,Y)的分布；独立性不足时保留条件分布。
- `application` PR09.11 → PR11.04：正态总体下的χ²枢轴导出方差区间；端点倒数反向。
- `application` PR09.07 → PR11.03：方差未知的单正态均值，使用独立性成立的t枢轴。
- `application` PR09.08 → PR11.06：独立双正态样本的方差比使用F枢轴，分子／分母自由度对应。
- `application` PR09.10 → PR12.04：均值Z／t检验的分母选择依已知或未知方差。
- `application` PR09.11 → PR12.05：方差χ²检验的自由度依是否估计均值确定。
- `application` PR09.14 → PR12.06：双总体均值差检验必须保留两个样本独立、方差条件及合并方差约定。
- `duality_under_condition` PR11.02 → PR12.08：相匹配的模型、枢轴、单双侧方向、水平下，检验与置信区间可互相解释；不是任意检验的无条件规则。
- `specialization` PR07.08 → PR13.05：以常数预测是条件均方预测的特殊情形，有限二阶矩为前提。
