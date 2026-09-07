---
wiki_id: MATHWIKI-REVIEW-084
type: target_level_semantic_review_batch
title: 全库逐题语义复核第39批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-084_全库逐题语义复核第39批20题.json
status: active
last_updated: 2026-07-25
---

# 全库逐题语义复核第39批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 10 张；覆盖 54 个物理图片路径与 26 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 0 张出现结构、身份、元数据或来源正文质量问题。问题只进入派生回执与修复队列；当前 SHADOW 模式没有改正式卡的 `related`、错因字段或视觉详情正文。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决是 SHADOW 建议，不授权写回正式 `related`。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [LA-019](http://127.0.0.1:8765/open/LA-019) | 四阶行列式等于一个代数余子式线性组合加 10，求参数 a,b。 | 代数余子式、按行展开、线性组合对齐 | a=4，b 为任意常数。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | repeat_count_not_supported_by_dated_history、visual_detail_closeout_state_stale |
| [LA-020](http://127.0.0.1:8765/open/LA-020) | 求一个 5 阶分块反对角矩阵全部元素代数余子式之和。 | 代数余子式总和、伴随矩阵、分块反对角结构 | -4。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | — |
| [LA-021](http://127.0.0.1:8765/open/LA-021) | 由两个矩阵多项式行列式为零的条件确定三阶矩阵特征值，再求伴随矩阵迹。 | 矩阵多项式归零、谱映射、伴随矩阵迹、特征值对称多项式 | -13/2。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | duplicate_registered_question_asset_paths、visual_detail_closeout_state_stale |
| [LA-022](http://127.0.0.1:8765/open/LA-022) | 已知三阶矩阵特征值为 -1,2,3，求三个主代数余子式之和。 | 主子式和、特征多项式系数、特征值基本对称式 | 1。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | personal_evidence_schema_conflict |
| [LA-023](http://127.0.0.1:8765/open/LA-023) | 三阶可逆矩阵的逆矩阵每行和为 2，且行列式为 3，求第三列三个代数余子式之和。 | 逆矩阵、伴随矩阵下标转置、行和 | 6。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | personal_evidence_schema_conflict、question_asset_contains_method_annotation |
| [LA-024](http://127.0.0.1:8765/open/LA-024) | 待拆分具体题面 | 二次型讲义总纲 | — | missing_question_surface：不可推断；当前来源不是原子题目。 | not_a_concrete_wrong_question |
| [LA-025](http://127.0.0.1:8765/open/LA-025) | 二次型 f(x)=x^T Bx，其中 B=[[1,1,0],[0,1,1],[0,0,1]]，判断规范形。 | 非对称表示矩阵、对称部分、正定、规范形 | y1^2+y2^2+y3^2，选 B。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | formal_question_not_standalone、personal_evidence_schema_conflict |
| [LA-026](http://127.0.0.1:8765/open/LA-026) | alpha1=(1,2)^T、alpha2=(a,1)^T，二次型为两个内积平方和，求正定参数。 | Gram 矩阵、平方和型二次型、公共零点、正定 | a 不等于 1/2。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | formal_question_not_standalone、personal_evidence_schema_conflict |
| [LA-027](http://127.0.0.1:8765/open/LA-027) | 二次型 x1^2-x2^2+2a x1x3+4x2x3 的负惯性指数为 1，求 a 的范围。 | 含参二次型、惯性指数、行列式符号、边界零特征值 | a 属于 [-2,2]。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | formal_question_literal_truncation、repeat_count_not_supported_by_dated_history |
| [LA-028](http://127.0.0.1:8765/open/LA-028) | A=[[4,1,-2],[1,1,1],[-2,1,a]] 与 diag(k,6,0) 合同；再问何时可正交合同及对应 Q。 | 合同、惯性指数、正交相似、单位正交特征向量、列顺序 | 合同部分 a=4 且 k>0；正交部分 k=3。可取 Q 的列依次为 (1,1,1)^T/sqrt(3)、(-1,0,1)^T/sqrt(2)、(1,-2,1)^T/sqrt(6)。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | formal_question_not_standalone、personal_evidence_schema_conflict、formal_orthogonal_matrix_answer_is_wrong |
| [LA-029](http://127.0.0.1:8765/open/LA-029) | f=x1^2-4x1x2+a x2^2 经正交变换化为 g=4y1^2+4y1y2+b y2^2，求 a,b,Q。 | 二次型矩阵、正交合同、迹与行列式不变量、特征向量配对 | a=4，b=1；可取 Q=[[0,1],[-1,0]]，满足 Q^T[[1,-2],[-2,4]]Q=[[4,2],[2,1]]。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | formal_question_and_answer_not_closed_after_image_recovery、repeat_count_not_supported_by_dated_history |
| [LA-031](http://127.0.0.1:8765/open/LA-031) | 求一个三元平方和差二次型的规范形。 | 二次型矩阵、特征值、惯性指数、规范形 | y1^2-y2^2，选 B。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | — |
| [LA-032](http://127.0.0.1:8765/open/LA-032) | 矩阵 [[1,2,0],[2,a,0],[0,0,b]] 有一个正特征值和两个负特征值，判断 a,b。 | 分块实对称矩阵、特征值符号、二阶块行列式、惯性指数 | a<4 且 b<0，选 D。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | formal_question_not_standalone、personal_evidence_schema_conflict |
| [LA-033](http://127.0.0.1:8765/open/LA-033) | 由 ker(A) 严格包含于 ker(B^T) 确定参数，再正交化二次型 x^TBAx。 | 核空间严格包含、秩与零空间维数、二次型矩阵、重特征值正交基 | a=1,b=2；标准形 6y1^2，正式卡所列 Q 可用。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | method_route_partial_and_registry_text_truncated |
| [LA-034](http://127.0.0.1:8765/open/LA-034) | 求平方和差二次型的正、负惯性指数。 | 二次型矩阵、惯性指数、零特征值 | 正惯性指数 1，负惯性指数 1，选 B。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | — |
| [LA-036](http://127.0.0.1:8765/open/LA-036) | 二次型 x1^2-x2x3 经正交变换化为 y1y2+a y3^2，求 a,Q。 | 交叉项矩阵化、正交变换、特征值匹配、列顺序 | a=1；正式卡给出的 Q 可用。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | personal_evidence_schema_conflict |
| [LA-045](http://127.0.0.1:8765/open/LA-045) | 求一个对角线全为 1 的三阶上三角矩阵的 10 次幂。 | 单位阵加幂零矩阵、矩阵二项式、幂零截断 | [[1,10,35],[0,1,10],[0,0,1]]。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | registered_solution_asset_is_only_partial_formula_reference |
| [LA-046](http://127.0.0.1:8765/open/LA-046) | 计算左右两侧带幂的初等矩阵乘积。 | 初等矩阵、左乘行变换、右乘列变换、周期幂 | [[2,1],[-3,-4]]。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | — |
| [LA-047](http://127.0.0.1:8765/open/LA-047) | AB=B^2-BC，给定可逆 B 与 C，求 A^99。 | 矩阵方程、构造相似分解、幂等矩阵、高次幂 | [[1,0,-1],[0,1,-1],[0,0,0]]。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | formal_question_not_standalone、personal_evidence_schema_conflict |
| [LA-048](http://127.0.0.1:8765/open/LA-048) | 实对称矩阵满足三次矩阵多项式方程，求 A。 | 实对称矩阵、矩阵多项式归零、特征值方程、谱定理 | A=I/2。 | pending_user_confirmation：个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。 | — |

## 逐题复核

### LA-019 强化例题2.1-2

- 题目：四阶行列式等于一个代数余子式线性组合加 10，求参数 a,b。
- 所问：四阶行列式等于一个代数余子式线性组合加 10，求参数 a,b。
- 知识点：代数余子式；按行展开；线性组合对齐
- 第一动作：先写真实第 4 行展开式，再与题给余子式组合逐项比较。
- 答案：a=4，b 为任意常数。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 按第 4 行展开并与题给组合相减，等式差化为 10(a-4)=0；b 完全消去。
- 质量发现：
  - `repeat_count_not_supported_by_dated_history`：method_gap.repeat_count=1，但 mistake_count 与 wrong_history 均缺失，不能证明一次独立个人做错事件。；建议：
  - `visual_detail_closeout_state_stale`：详情仍写 wrongnet_rebuild=needed_after_card_update，和当前已存在正式卡、详情、source summary 的投影状态没有收口。；建议：
- 关系裁决：
  - LA-020：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`stale`；正式卡 `3cf325e7fdd2d40ceae99a810a975d4f3d3ee6700354fdae4e2616d922965dce`；唯一图片 1 个；物理路径 2 个。

### LA-020 强化例题2.2

- 题目：求一个 5 阶分块反对角矩阵全部元素代数余子式之和。
- 所问：求一个 5 阶分块反对角矩阵全部元素代数余子式之和。
- 知识点：代数余子式总和；伴随矩阵；分块反对角结构
- 第一动作：把总和写成全一向量与伴随矩阵的双线性式，再利用分块结构。
- 答案：-4。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 独立复算得 det(A)=-2，代数余子式总和为 -4；题图与解析图一致。
- 关系裁决：
  - LA-019：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`stale`；正式卡 `7160e51a5791dd6c53bb432ef078d90610525020cfd9c452c878c679168e6190`；唯一图片 2 个；物理路径 5 个。

### LA-021 强化例题7.1-2 伴随矩阵迹与特征值

- 题目：由两个矩阵多项式行列式为零的条件确定三阶矩阵特征值，再求伴随矩阵迹。
- 所问：由两个矩阵多项式行列式为零的条件确定三阶矩阵特征值，再求伴随矩阵迹。
- 知识点：矩阵多项式归零；谱映射；伴随矩阵迹；特征值对称多项式
- 第一动作：先由 det(A) 不为零把两个条件约去 A，转成 -2 与 -1/2 是特征值。
- 答案：-13/2。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - A 可逆；两个条件分别给出特征值 -2 与 -1/2，行列式 3 再给第三个特征值 3，伴随矩阵迹为两两乘积和 -13/2。
- 质量发现：
  - `duplicate_registered_question_asset_paths`：正式卡登记五个题图路径，但五个文件 SHA-256 完全相同，只是同一题图的五份物理副本。；建议：
  - `visual_detail_closeout_state_stale`：详情仍写 wrongnet_rebuild=needed_formal_card_updated，来源投影也没有 formal hash 与视觉引用。；建议：
- 关系裁决：
  - LA-029：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-051：`remove`；LA-021 remains canonical; LA-051/101/102 remain stable-ID identity holds only.
  - LA-101：`remove`；LA-021 remains canonical; LA-051/101/102 remain stable-ID identity holds only.
  - LA-102：`remove`；LA-021 remains canonical; LA-051/101/102 remain stable-ID identity holds only.
- 当前快照：`stale`；正式卡 `f69adff51ab61cb12e50d53daea7b90d7d90c95cb016d4fae2df238bd894b79c`；唯一图片 1 个；物理路径 5 个。

### LA-022 强化例题2.3

- 题目：已知三阶矩阵特征值为 -1,2,3，求三个主代数余子式之和。
- 所问：已知三阶矩阵特征值为 -1,2,3，求三个主代数余子式之和。
- 知识点：主子式和；特征多项式系数；特征值基本对称式
- 第一动作：把主代数余子式和识别为二阶主子式和。
- 答案：1。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 主代数余子式和等于特征值两两乘积和，计算为 -2-3+6=1。
- 质量发现：
  - `personal_evidence_schema_conflict`：wrong_history 明说原始个人动作未记录，method_gap 又缺 evidence_origin，却把 need_user_confirmation 设为 false；下游可能把候选入口误当成已确认个人错因。；建议：
- 关系裁决：
  - LA-023：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`stale`；正式卡 `2a940bca213dbba0f75c33ccc5a5a5521417df717561b019b04f3abc424e5a59`；唯一图片 1 个；物理路径 2 个。

### LA-023 强化例题2.4

- 题目：三阶可逆矩阵的逆矩阵每行和为 2，且行列式为 3，求第三列三个代数余子式之和。
- 所问：三阶可逆矩阵的逆矩阵每行和为 2，且行列式为 3，求第三列三个代数余子式之和。
- 知识点：逆矩阵；伴随矩阵下标转置；行和
- 第一动作：先写 A^{-1}=adj(A)/det(A)，并把目标定位到 adj(A) 的第 3 行。
- 答案：6。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 目标是 adj(A) 第 3 行之和，等于 det(A) 乘 A^{-1} 第 3 行之和，即 3×2=6。
- 质量发现：
  - `personal_evidence_schema_conflict`：wrong_history 明说原始个人动作未记录，method_gap 又缺 evidence_origin，却把 need_user_confirmation 设为 false；下游可能把候选入口误当成已确认个人错因。；建议：
  - `question_asset_contains_method_annotation`：题图上直接写有 D22 与“转换等价表达”等方法提示，不能作为严格答案安全的纯题面。；建议：
- 关系裁决：
  - LA-022：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`stale`；正式卡 `3a46cc1b91206751a653450ecb6070b26e6b74c5fe581060a87cba299a358ad8`；唯一图片 1 个；物理路径 2 个。

### LA-024 线代强化第九讲

- 题目：当前只有二次型讲义总纲，没有可独立作答的具体题目。
- 所问：待拆分具体题面
- 知识点：二次型讲义总纲
- 第一动作：—
- 答案：—
- 个人错因边界：missing_question_surface；不可推断；当前来源不是原子题目。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
- 质量发现：
  - `not_a_concrete_wrong_question`：卡片是二次型讲义总纲，没有具体题干、答案、题图、解析或个人作答证据。；建议：
- 当前快照：`current`；正式卡 `6f7032abaac33a15880b662f567ea4639e49991b462605f07d3b5e309cbc5846`；唯一图片 0 个；物理路径 0 个。

### LA-025 强化例题9.1

- 题目：二次型 f(x)=x^T Bx，其中 B=[[1,1,0],[0,1,1],[0,0,1]]，判断规范形。
- 所问：二次型 f(x)=x^T Bx，其中 B=[[1,1,0],[0,1,1],[0,0,1]]，判断规范形。
- 知识点：非对称表示矩阵；对称部分；正定；规范形
- 第一动作：先取 (B+B^T)/2，而不是直接把上三角矩阵当实对称矩阵。
- 答案：y1^2+y2^2+y3^2，选 B。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 二次型由 B 的对称部分决定；其特征值为 1,1±sqrt(2)/2，均为正，故正惯性指数为 3。
- 质量发现：
  - `formal_question_not_standalone`：正式卡题目摘要省略了解题必需的矩阵或向量数值，脱离登记题图无法独立复做。；建议：
  - `personal_evidence_schema_conflict`：wrong_history 明说原始个人动作未记录，method_gap 又缺 evidence_origin，却把 need_user_confirmation 设为 false；下游可能把候选入口误当成已确认个人错因。；建议：
- 关系裁决：
  - LA-026：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-028：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-032：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-036：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`stale`；正式卡 `c637bd03a3d582577d9649092ff24c78a5c4239ed918020bd0aecd3ba7f1cbd8`；唯一图片 1 个；物理路径 2 个。

### LA-026 强化例题9.2

- 题目：alpha1=(1,2)^T、alpha2=(a,1)^T，二次型为两个内积平方和，求正定参数。
- 所问：alpha1=(1,2)^T、alpha2=(a,1)^T，二次型为两个内积平方和，求正定参数。
- 知识点：Gram 矩阵；平方和型二次型；公共零点；正定
- 第一动作：先检查 alpha1,alpha2 是否张成 R^2，或写 Gram 矩阵。
- 答案：a 不等于 1/2。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 平方和正定等价于两个线性形式只有公共零解，也等价于 alpha1,alpha2 线性无关；行列式 1-2a 不为零。
- 质量发现：
  - `formal_question_not_standalone`：正式卡题目摘要省略了解题必需的矩阵或向量数值，脱离登记题图无法独立复做。；建议：
  - `personal_evidence_schema_conflict`：wrong_history 明说原始个人动作未记录，method_gap 又缺 evidence_origin，却把 need_user_confirmation 设为 false；下游可能把候选入口误当成已确认个人错因。；建议：
- 关系裁决：
  - LA-025：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-035：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-036：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`current`；正式卡 `d211e1bd4619ac4ca3f3b8238785a51fd7d304e97cea49cfe4c70ee8bfbac7b6`；唯一图片 1 个；物理路径 2 个。

### LA-027 线代基础6.7

- 题目：二次型 x1^2-x2^2+2a x1x3+4x2x3 的负惯性指数为 1，求 a 的范围。
- 所问：二次型 x1^2-x2^2+2a x1x3+4x2x3 的负惯性指数为 1，求 a 的范围。
- 知识点：含参二次型；惯性指数；行列式符号；边界零特征值
- 第一动作：先确认前 2×2 主块已有一正一负，再用 det(A) 判断第三个特征值及边界。
- 答案：a 属于 [-2,2]。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 前两变量已给一正一负；det(A)=a^2-4。det(A)<0 时负惯性指数为 1，边界 det(A)=0 时仍是一正一负一零，故含端点。
- 质量发现：
  - `formal_question_literal_truncation`：正式题目摘要在变换矩阵 C 的第一行中途截断，题干结构未闭合。；建议：
  - `repeat_count_not_supported_by_dated_history`：method_gap.repeat_count=1，但 mistake_count 与 wrong_history 均缺失。；建议：
- 当前快照：`current`；正式卡 `884184bbcfe1c95b723931a7aa058a2b23f6b0987f7817bfba407932f989768f`；唯一图片 1 个；物理路径 1 个。

### LA-028 强化例题9.3(164730)

- 题目：A=[[4,1,-2],[1,1,1],[-2,1,a]] 与 diag(k,6,0) 合同；再问何时可正交合同及对应 Q。
- 所问：A=[[4,1,-2],[1,1,1],[-2,1,a]] 与 diag(k,6,0) 合同；再问何时可正交合同及对应 Q。
- 知识点：合同；惯性指数；正交相似；单位正交特征向量；列顺序
- 第一动作：先用秩或行列式确定 a，再分开检查合同保持量与正交变换保持量。
- 答案：合同部分 a=4 且 k>0；正交部分 k=3。可取 Q 的列依次为 (1,1,1)^T/sqrt(3)、(-1,0,1)^T/sqrt(2)、(1,-2,1)^T/sqrt(6)。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - det(A)=3(a-4)，故 a=4；此时 A 的特征值为 3,6,0。正式卡给出的 Q 复算后 Q^T A Q 不是对角矩阵，必须替换。
- 质量发现：
  - `formal_question_not_standalone`：正式卡题目摘要省略了解题必需的矩阵或向量数值，脱离登记题图无法独立复做。；建议：
  - `personal_evidence_schema_conflict`：wrong_history 明说原始个人动作未记录，method_gap 又缺 evidence_origin，却把 need_user_confirmation 设为 false；下游可能把候选入口误当成已确认个人错因。；建议：
  - `formal_orthogonal_matrix_answer_is_wrong`：正式卡所列 Q 复算得到 Q^T A Q=[[1,-1,1],[-1,4,2],[1,2,4]]，不等于 diag(3,6,0)。参数 a=4、合同条件 k>0 和正交部分 k=3 正确，但 Q 错误。；建议：
- 关系裁决：
  - LA-025：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-032：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-036：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`current`；正式卡 `6c47bd3b28462d0bcded0b88fa65ea07702c91ec1718021fb4607c7f22395bcc`；唯一图片 1 个；物理路径 2 个。

### LA-029 线代基础6.6

- 题目：f=x1^2-4x1x2+a x2^2 经正交变换化为 g=4y1^2+4y1y2+b y2^2，求 a,b,Q。
- 所问：f=x1^2-4x1x2+a x2^2 经正交变换化为 g=4y1^2+4y1y2+b y2^2，求 a,b,Q。
- 知识点：二次型矩阵；正交合同；迹与行列式不变量；特征向量配对
- 第一动作：先写两个实对称矩阵，用迹与行列式确定参数。
- 答案：a=4，b=1；可取 Q=[[0,1],[-1,0]]，满足 Q^T[[1,-2],[-2,4]]Q=[[4,2],[2,1]]。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 迹与行列式不变量给 a=4,b=1；给出的 Q 已直接复算正交性和 Q^T A Q=B。
- 质量发现：
  - `formal_question_and_answer_not_closed_after_image_recovery`：正式题目摘要在目标矩阵 B 中途截断，答案仍写字段损坏；但 2026-07-10 回收题图已完整可读。；建议：
  - `repeat_count_not_supported_by_dated_history`：method_gap.repeat_count=1，但 mistake_count 与 wrong_history 均缺失。；建议：
- 关系裁决：
  - LA-021：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-051：`remove`；Recovered LA-029 is a distinct two-variable quadratic-form problem and must not inherit LA-021 identity links.
  - LA-101：`remove`；Recovered LA-029 is a distinct two-variable quadratic-form problem and must not inherit LA-021 identity links.
  - LA-102：`remove`；Recovered LA-029 is a distinct two-variable quadratic-form problem and must not inherit LA-021 identity links.
- 当前快照：`current`；正式卡 `1bc67d34d5d408ff2a2f5ddb7b3d1b6bccbf5ce1793017c627f5ae8ae5f9a8cd`；唯一图片 1 个；物理路径 1 个。

### LA-031 2023年真题第九题

- 题目：求一个三元平方和差二次型的规范形。
- 所问：求一个三元平方和差二次型的规范形。
- 知识点：二次型矩阵；特征值；惯性指数；规范形
- 第一动作：先展开并把交叉项系数平分到实对称矩阵。
- 答案：y1^2-y2^2，选 B。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 对应实对称矩阵特征值为 -7,0,3，故正、负惯性指数各 1。
- 关系裁决：
  - LA-033：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-034：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`current`；正式卡 `4a7cc42c80150b11f646bc6ff78f0683a006bff089e92ac97c22171b941b7b23`；唯一图片 2 个；物理路径 4 个。

### LA-032 2025年真题选择题第八题

- 题目：矩阵 [[1,2,0],[2,a,0],[0,0,b]] 有一个正特征值和两个负特征值，判断 a,b。
- 所问：矩阵 [[1,2,0],[2,a,0],[0,0,b]] 有一个正特征值和两个负特征值，判断 a,b。
- 知识点：分块实对称矩阵；特征值符号；二阶块行列式；惯性指数
- 第一动作：先把 2×2 块与独立特征值 b 分开判断。
- 答案：a<4 且 b<0，选 D。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 前 2×2 块行列式 a-4<0 时一正一负，再令 b<0 即得到一正两负。
- 质量发现：
  - `formal_question_not_standalone`：正式卡题目摘要省略了解题必需的矩阵或向量数值，脱离登记题图无法独立复做。；建议：
  - `personal_evidence_schema_conflict`：wrong_history 明说原始个人动作未记录，method_gap 又缺 evidence_origin，却把 need_user_confirmation 设为 false；下游可能把候选入口误当成已确认个人错因。；建议：
- 关系裁决：
  - LA-025：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-028：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`stale`；正式卡 `062b4cf0761d207c1e66cc04a34912b57777adff4ab5fbd5275adeff1e9c0fd7`；唯一图片 1 个；物理路径 2 个。

### LA-033 2024年真题第22题

- 题目：由 ker(A) 严格包含于 ker(B^T) 确定参数，再正交化二次型 x^TBAx。
- 所问：由 ker(A) 严格包含于 ker(B^T) 确定参数，再正交化二次型 x^TBAx。
- 知识点：核空间严格包含；秩与零空间维数；二次型矩阵；重特征值正交基
- 第一动作：先把解集条件准确翻译为 ker(A) 严格包含于 ker(B^T)，不能写成同解。
- 答案：a=1,b=2；标准形 6y1^2，正式卡所列 Q 可用。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 严格包含迫使 rank(B^T)=1，从而 b=2；再代入 ker(A) 得 a=1。BA 为秩 1 实对称矩阵，特征值 6,0,0，正式 Q 已复算正确。
- 质量发现：
  - `method_route_partial_and_registry_text_truncated`：L05-006 标题是齐次同解，而本题条件是严格单向核包含；方法库该节第一动作还字面截断在 r([A，且现有单链未覆盖第二问正交对角化。；建议：
- 关系裁决：
  - LA-031：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-034：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`current`；正式卡 `31161e5953b952f919a6917c29deb47ec77033efc435185ed675ed3d9d0862a9`；唯一图片 2 个；物理路径 4 个。

### LA-034 2021年第八题

- 题目：求平方和差二次型的正、负惯性指数。
- 所问：求平方和差二次型的正、负惯性指数。
- 知识点：二次型矩阵；惯性指数；零特征值
- 第一动作：先展开并写实对称矩阵，再数正负特征值。
- 答案：正惯性指数 1，负惯性指数 1，选 B。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 对应实对称矩阵特征值为 -1,0,3，题图、解析图与正式答案一致。
- 关系裁决：
  - LA-031：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-033：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`current`；正式卡 `76bd69f06e25b6e15c8c2e5351e78b115c29bde7de8787314907132973bbfe4b`；唯一图片 2 个；物理路径 4 个。

### LA-036 强化例题9.7（171639）

- 题目：二次型 x1^2-x2x3 经正交变换化为 y1y2+a y3^2，求 a,Q。
- 所问：二次型 x1^2-x2x3 经正交变换化为 y1y2+a y3^2，求 a,Q。
- 知识点：交叉项矩阵化；正交变换；特征值匹配；列顺序
- 第一动作：先把源式和目标式都写成实对称矩阵。
- 答案：a=1；正式卡给出的 Q 可用。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 源矩阵特征值为 1,1/2,-1/2，目标矩阵特征值为 a,1/2,-1/2，故 a=1；Q^T A Q 已复算为目标矩阵。
- 质量发现：
  - `personal_evidence_schema_conflict`：wrong_history 明说原始个人动作未记录，method_gap 又缺 evidence_origin，却把 need_user_confirmation 设为 false；下游可能把候选入口误当成已确认个人错因。；建议：
- 关系裁决：
  - LA-025：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-026：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-028：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`current`；正式卡 `3c1d484a4c424ae7c23e0d1c70bc12196e7f45f7107cce3a7f14d5b328e6a88e`；唯一图片 1 个；物理路径 2 个。

### LA-045 幂零分解求矩阵十次幂

- 题目：求一个对角线全为 1 的三阶上三角矩阵的 10 次幂。
- 所问：求一个对角线全为 1 的三阶上三角矩阵的 10 次幂。
- 知识点：单位阵加幂零矩阵；矩阵二项式；幂零截断
- 第一动作：先令 N=A-I 并确定 N 的幂零阶数。
- 答案：[[1,10,35],[0,1,10],[0,0,1]]。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 写 A=I+N，N^3=0，故 A^10=I+10N+45N^2；正式答案正确，但登记解析图只给二项式系数，没有完整落到本题矩阵。
- 质量发现：
  - `registered_solution_asset_is_only_partial_formula_reference`：solution_01 只显示二项式系数公式及 10、45，没有写 A=I+N、N^3=0 或最终矩阵；详情把它称为完整解析会高估证据。；建议：
- 当前快照：`stale`；正式卡 `96874e112c07a4d90c658624e5748efd2ef29b594fd7a4ed01778dd86c6f2572`；唯一图片 2 个；物理路径 4 个。

### LA-046 初等矩阵幂的行列变换

- 题目：计算左右两侧带幂的初等矩阵乘积。
- 所问：计算左右两侧带幂的初等矩阵乘积。
- 知识点：初等矩阵；左乘行变换；右乘列变换；周期幂
- 第一动作：先区分左乘作用于行、右乘作用于列，再处理幂次。
- 答案：[[2,1],[-3,-4]]。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 左乘矩阵重复 3 次行变换，右乘交换矩阵的 -5 次幂等于自身；直接复算结果与解析一致。
- 当前快照：`stale`；正式卡 `587532d198e240042765e4ec0ac0844be2c50e1839536b7f1fae2df39fd62709`；唯一图片 2 个；物理路径 4 个。

### LA-047 1000题强化B组3.4

- 题目：AB=B^2-BC，给定可逆 B 与 C，求 A^99。
- 所问：AB=B^2-BC，给定可逆 B 与 C，求 A^99。
- 知识点：矩阵方程；构造相似分解；幂等矩阵；高次幂
- 第一动作：先右乘 B^{-1}，构造 A 与 B-C 的相似关系。
- 答案：[[1,0,-1],[0,1,-1],[0,0,0]]。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 由 AB=B(B-C) 得 A=B(B-C)B^{-1}；B-C=diag(1,1,0) 为幂等矩阵，因此 A^99=B(B-C)B^{-1}，正式答案正确。
- 质量发现：
  - `formal_question_not_standalone`：正式卡题目摘要省略了解题必需的矩阵或向量数值，脱离登记题图无法独立复做。；建议：
  - `personal_evidence_schema_conflict`：wrong_history 明说原始个人动作未记录，method_gap 又缺 evidence_origin，却把 need_user_confirmation 设为 false；下游可能把候选入口误当成已确认个人错因。；建议：
- 当前快照：`stale`；正式卡 `c144cf633d3fcafab337a88350c6552411d55412a94e25ca799576783711bf7e`；唯一图片 1 个；物理路径 2 个。

### LA-048 实对称矩阵方程谱分解

- 题目：实对称矩阵满足三次矩阵多项式方程，求 A。
- 所问：实对称矩阵满足三次矩阵多项式方程，求 A。
- 知识点：实对称矩阵；矩阵多项式归零；特征值方程；谱定理
- 第一动作：先令任一实特征值满足同一标量多项式方程。
- 答案：A=I/2。
- 个人错因边界：pending_user_confirmation；个人错因待确认；旧导入没有用户真实作答过程，本批只保留客观复做风险。
- 一致性：题图—解析 —；正式卡—图片 —
- 解析主线：
  - 标量多项式因式分解为 (1+lambda^2)(1-2lambda)；实对称矩阵特征值全实，只能为 1/2，故 A=I/2。
- 关系裁决：
  - LA-056：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-104：`remove`；The broad matrix-operation similarity is insufficient for a strict formal edge under the B39 evidence gate.
  - LA-109：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
  - LA-113：`remove`；The pair lacks a verified shared personal breakpoint and therefore cannot remain a formal strong edge.
- 当前快照：`current`；正式卡 `69fbc68d9cdacf421e9e9df134e1c998ef7528d16019bf4bf5326447f0501c96`；唯一图片 2 个；物理路径 4 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
