---
wiki_id: MATHWIKI-REVIEW-010
type: target_level_semantic_review_batch
title: 全库逐题语义复核第2批20题
subject: 数学一
knowledge:
  - 全库逐题复核
  - 题图解析图核对
  - 知识点错因连线
source_refs:
  - 错题知识网络/错题卡/
  - 错题知识网络/可视化错题详情/
  - 错题知识网络/assets/visual_wrong_questions/
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-010_全库逐题语义复核第2批20题.json
status: active
last_updated: 2026-07-22
---

# 全库逐题语义复核第2批20题

## 本批结论

本批共逐题核对 20 张正式卡，当前哈希仍有效的完整复核为 4 张；覆盖 49 个物理图片路径与 42 个唯一图片内容。全库当前共 882 张正式卡，本轮活动累计完成 119 张，剩余 763 张。

本批有 4 张出现结构、身份、元数据或来源正文质量问题。证据充分且无歧义的修正已经正式收口；身份冲突、稳定 ID 合并或证据不足项仍保留为 needs_user，详见 `MATH-TARGET-SEMANTIC-CLOSEOUT-20260722-B02`。

## 证据边界

- `verified` 表示题面、所问对象、答案、解析路线和当前全部图片内容已经逐一核对，并由正式卡 SHA、详情页 SHA 与图片 SHA-256 绑定。
- 个人错因仍按 `confirmed_personal`、`legacy_unclassified`、`pending_user_confirmation` 和重复占位分别处理；读懂解析不能反推用户为什么做错。
- 同一哈希的重复物理图片只视觉核对一次，但所有物理路径都纳入数量和集合一致性检查。
- 关系裁决中已正式应用的变更以正式收口回执为准；未应用项仍是 SHADOW 建议。

## 批次总览

| 错题 | 题目在问什么 | 知识点 | 答案 | 个人错因边界 | 质量发现 |
|---|---|---|---|---|---|
| [GS-411](http://127.0.0.1:8765/open/GS-411) | 求二重积分值。 | 二重积分、二重积分极坐标法、齐次换元 y=xt | 3/4 × [sqrt(2)+ln(sqrt(2)+1)] | pending_user_confirmation：旧正式正文属于另一道题，旧个人错因不迁移；当前个人断点仍待复做确认。 | canonical_visual_identity_conflict |
| [GS-421](http://127.0.0.1:8765/open/GS-421) | 求引力的 x 方向分量。 | 定积分、定积分应用、万有引力微元、向量分量投影 | -Gρ/sqrt(2) | pending_user_confirmation：旧正式正文属于另一道做功题，旧个人错因不迁移；当前个人断点仍待复做确认。 | canonical_visual_identity_conflict |
| [LA-068](http://127.0.0.1:8765/open/LA-068) | 求 BA。 | 矩阵秩、满列秩、满行秩、矩阵乘积消去 | BA=9I₂ | pending_user_confirmation：旧卡无个人作答，只确认满秩消去是复做入口。 | — |
| [GS-208](http://127.0.0.1:8765/open/GS-208) | 按正式正文证明目标点存在。 | 积分因子、辅助函数构造、积分中值定理、罗尔定理 | 存在 ξ∈(0,1)，使 f'(ξ)=(1-ξ⁻¹)f(ξ)。 | legacy_unclassified：保留正式卡既有记录，但当前 canonical 图片不能为它补证。 | canonical_visual_identity_conflict |
| [LA-095](http://127.0.0.1:8765/open/LA-095) | 求 a、列空间基 G 与坐标矩阵 H。 | 含参数矩阵的秩、极大线性无关组、主元列下标、列空间基、坐标矩阵、秩分解 | a=1；G=[[1,-1],[-1,0],[1,1]]；H=[[1,0,2,1,1],[0,1,-1,1,2]]。 | legacy_unclassified：旧批量没有用户作答；解析资产错误不能归因于用户。 | solution_asset_mathematical_error |
| [LA-003](http://127.0.0.1:8765/open/LA-003) | 证明参数条件下的对数不等式。 | 微分不等式证明、对数不等式、辅助函数 | 正式内容维护在 GS-256。 | duplicate_placeholder：个人错因归属 GS-256；LA-003 只保留历史痕迹。 | stable_id_duplicate_placeholder |
| [GS-165](http://127.0.0.1:8765/open/GS-165) | 求幂指极限。 | 幂指极限、1 的无穷次幂、对数化、洛必达法则 | 4e² | pending_user_confirmation：旧批量无个人首答，只确认对数化是复做入口。 | formal_body_indeterminate_form_label_corrected |
| [GS-237](http://127.0.0.1:8765/open/GS-237) | 选择充分条件。 | 二阶 Taylor 公式、中点展开、积分条件、凹凸性 | D，f''(x)>0。 | pending_user_confirmation：旧批量没有个人作答。 | — |
| [GS-718](http://127.0.0.1:8765/open/GS-718) | 求端点积分。 | 第二型曲线积分、路径无关、偏导判据、反求未知函数 | 1/2 | model_inferred_from_solution：用户只确认无法启动；具体偏导断点由题面与讲解链细化。 | visual_registry_backfill_applied |
| [GS-005](http://127.0.0.1:8765/open/GS-005) | 求等价无穷小的系数和阶数。 | 等价无穷小、阶数比较、洛必达法则 | a=1/6，b=3。 | legacy_unclassified：正式卡记录直接全 Taylor 等风险，但证据来源未分类。 | formal_lecture_refs_backfilled |
| [GS-095](http://127.0.0.1:8765/open/GS-095) | 求 f。 | 多项式整除、二重根条件、函数值与导数条件 | f(x)=x³/2-3x/2。 | legacy_unclassified_with_current_question_evidence：只有 2026-06-10 记录可绑定当前题；更早历史疑似跨题污染。 | cross_question_wrong_history_contamination、visual_detail_equation_corrected、formal_lecture_refs_backfilled |
| [GS-646](http://127.0.0.1:8765/open/GS-646) | 写空间切线方程。 | 参数式空间曲线、切向量、空间直线点向式 | x/1=(y-1)/2=(z-2)/3。 | confirmed_personal：复做时已求出切点和切向量，但没有继续写空间直线，并误用平面显函数切线公式。 | visual_detail_latest_recurrence_corrected |
| [GS-705](http://127.0.0.1:8765/open/GS-705) | 求曲线积分。 | 参数曲线、有向边界、绝对值分段、第二型曲线积分 | -3π/16 | confirmed_personal：误把完整星形线当区域边界，并机械反转积分限。 | visual_registry_backfill_applied |
| [GS-706](http://127.0.0.1:8765/open/GS-706) | 求最优 a 与曲线。 | 第二型曲线积分参数化、位置权重、参数最值 | a=1，y=sin x；最小值 π-8/3。 | confirmed_personal：把无权 ∫dy=0 机械推广到带位置权重的 ∫xdy=0。 | visual_registry_backfill_applied |
| [GS-707](http://127.0.0.1:8765/open/GS-707) | 求功。 | 向量场、变力做功、格林公式、方向 | -π/2 | confirmed_personal：把位置相关变力当固定力，企图用圆周长相乘。 | visual_registry_backfill_applied |
| [GS-708](http://127.0.0.1:8765/open/GS-708) | 求曲线积分。 | P 与 Q 映射、开曲线补线、格林公式、有向边界 | π/2-4 | confirmed_personal：未稳定建立 dx 系数对应 P、dy 系数对应 Q。 | visual_registry_backfill_applied |
| [GS-709](http://127.0.0.1:8765/open/GS-709) | 求含奇点闭曲线积分。 | 格林公式条件、内部奇点、多连通区域、挖洞法 | π | confirmed_personal：准备直接套格林公式，未检查原点奇点。 | visual_registry_backfill_applied、visual_detail_solution_embed_backfilled |
| [GS-710](http://127.0.0.1:8765/open/GS-710) | 求原函数。 | 凑微分、分部积分、抵消结构 | x exp(sin x)-exp(sin x)/cos x+C | confirmed_personal：拆分正确，但未识别两个微分与余项抵消。 | visual_registry_backfill_applied |
| [GS-711](http://127.0.0.1:8765/open/GS-711) | 求原函数。 | 整体换元、三角恒等变形、商的导数 | 8 exp(-sin x)/(1-sin x)+C | confirmed_personal：换元没有统一全部结构，后续也未做分子凑分母。 | visual_registry_backfill_applied |
| [GS-712](http://127.0.0.1:8765/open/GS-712) | 求 ∫f(x)dx。 | 复合函数反求、自变量角色、分部积分 | x-(1+exp(-x))ln(1+exp(x))+C | confirmed_personal：把反求函数与积分换元混在一起，得到 f 后又未触发分部积分。 | visual_registry_backfill_applied |

## 逐题复核

### GS-411 2020年第19题

- 题目：区域 D 由 x=1、x=2、y=x 与 x 轴围成，计算被积函数 sqrt(x^2+y^2)/x 的二重积分。
- 所问：求二重积分值。
- 知识点：二重积分；二重积分极坐标法；齐次换元 y=xt
- 第一动作：先按四条边界写 1≤x≤2、0≤y≤x，并识别 y/x 的齐次结构。
- 答案：3/4 × [sqrt(2)+ln(sqrt(2)+1)]
- 个人错因边界：pending_user_confirmation；旧正式正文属于另一道题，旧个人错因不迁移；当前个人断点仍待复做确认。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_batch27_source_repair
- 解析主线：
  - 先写 1≤x≤2、0≤y≤x。
  - 可令 y=xt 分离变量，或把竖直边界改写为极坐标径向边界。
- 质量发现：
  - `canonical_visual_identity_conflict`：第2批识别出的正式卡与视觉身份冲突已由第27批按当前题图、解析图和稳定 ID 完成源层重联。；建议：
- 关系裁决：
  - GS-404：`add_in_batch27`；同为第一象限楔形区域，需把直线和 x=c 边界准确翻译为直角坐标或极坐标积分限。
  - GS-409：`remove_in_batch27`；旧边来自错位正文；当前 GS-411 的楔形齐次结构与 GS-409 不构成强边。
  - GS-410：`remove_in_batch27`；旧边来自错位正文；当前 GS-411 与双纽线区域题不共享具体触发和第一动作。
- 当前快照：`stale`；正式卡 `7b0521219f35754260c01f5fa2ae363a31713816563f0a8f6b8befecf4f5b41d`；唯一图片 2 个；物理路径 2 个。

### GS-421 强化例题12.5

- 题目：y 轴区间 [0,1] 上的均匀细杆对 (1,0) 处单位质点产生引力，求引力的 x 方向分量。
- 所问：求引力的 x 方向分量。
- 知识点：定积分；定积分应用；万有引力微元；向量分量投影
- 第一动作：先画细杆微元到质点的方向，并确定 x 分量为负。
- 答案：-Gρ/sqrt(2)
- 个人错因边界：pending_user_confirmation；旧正式正文属于另一道做功题，旧个人错因不迁移；当前个人断点仍待复做确认。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_batch27_source_repair
- 解析主线：
  - 取细杆微元 ρdy。
  - 写出指向细杆的负 x 方向投影并积分 -Gρ∫₀¹(1+y²)^(-3/2)dy。
- 质量发现：
  - `canonical_visual_identity_conflict`：第2批识别出的正式卡与视觉身份冲突已由第27批按当前题图、两张解析图和稳定 ID 完成源层重联。；建议：
- 关系裁决：
  - GS-422：`remove_in_batch27`；GS-421 是固定质点受细杆引力分量，GS-422 是移动质点的引力做功；旧边由错位正文产生。
- 当前快照：`stale`；正式卡 `48da2fb6c74daffe04367a0aa0e3e6e305db132cd4f0ec872841759692cb9b4e`；唯一图片 3 个；物理路径 3 个。

### LA-068 AB平方反推BA

- 题目：A 为 3×2 矩阵、B 为 2×3 矩阵，给定 AB，求 BA。
- 所问：求 BA。
- 知识点：矩阵秩；满列秩；满行秩；矩阵乘积消去
- 第一动作：先算 r(AB) 与 (AB)²。
- 答案：BA=9I₂
- 个人错因边界：pending_user_confirmation；旧卡无个人作答，只确认满秩消去是复做入口。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 由 r(AB)=2 得 A 满列秩、B 满行秩。
  - 算得 (AB)²=9AB，再用满秩条件合法消去两端。
- 关系裁决：
  - LA-067：`strong_candidate`；共享满秩条件下合法消去的核心动作。
  - LA-070：`medium_navigation`；共享矩阵秩与乘积结构，但主方法不同。
  - LA-073：`reject_as_strong`；只共享矩阵秩粗标签。
- 当前快照：`stale`；正式卡 `bb34f405a7c78af8f40f22a45f9a604d157410c4ff84e447bd23be7a84b3769b`；唯一图片 2 个；物理路径 4 个。

### GS-208 强化例题6.3 2026.5.20

- 题目：正式正文为积分因子、积分中值定理和罗尔定理证明题；当前 canonical 图片误绑 LA-095 的含参矩阵题。
- 所问：按正式正文证明目标点存在。
- 知识点：积分因子；辅助函数构造；积分中值定理；罗尔定理
- 第一动作：先把目标式整理成 f' 与 f 的线性组合。
- 答案：存在 ξ∈(0,1)，使 f'(ξ)=(1-ξ⁻¹)f(ξ)。
- 个人错因边界：legacy_unclassified；保留正式卡既有记录，但当前 canonical 图片不能为它补证。
- 一致性：题图—解析 canonical 图片属于 LA-095；正式卡—图片 identity_conflict
- 解析主线：
  - 反推积分因子构造 F(x)=xe^(-x)f(x)。
  - 用积分中值定理得到等值点，再用罗尔定理。
- 质量发现：
  - `canonical_visual_identity_conflict`：GS-208 与 LA-095 共用题图和解析图 SHA；另有高数题图支持正式正文，但 canonical 解析仍错位。；建议：完成视觉身份重绑前冻结关系验证。
- 关系裁决：
  - GS-648：`freeze_until_identity_relinked`；当前 canonical 视觉证据不支持正式高数内容。
  - GS-218：`freeze_until_identity_relinked`；当前 canonical 视觉证据不支持正式高数内容。
  - GS-213：`freeze_until_identity_relinked`；当前 canonical 视觉证据不支持正式高数内容。
  - GS-576：`freeze_until_identity_relinked`；当前 canonical 视觉证据不支持正式高数内容。
- 当前快照：`stale`；正式卡 `a776932ee6311282076b529a1c323ea5483c65ea00b6083eeb4e7480140d35a2`；唯一图片 3 个；物理路径 3 个。

### LA-095 强化例题6.3-2

- 题目：含参数 3×5 矩阵秩为 2；求参数、列极大无关组并构造 A=GH。
- 所问：求 a、列空间基 G 与坐标矩阵 H。
- 知识点：含参数矩阵的秩；极大线性无关组；主元列下标；列空间基；坐标矩阵；秩分解
- 第一动作：先定参数和主元列下标，再回原矩阵取列。
- 答案：a=1；G=[[1,-1],[-1,0],[1,1]]；H=[[1,0,2,1,1],[0,1,-1,1,2]]。
- 个人错因边界：legacy_unclassified；旧批量没有用户作答；解析资产错误不能归因于用户。
- 一致性：题图—解析 第1问正确，第2问解析图数学错误；正式卡—图片 正式卡和详情已修正，原解析图仍保留缺陷
- 解析主线：
  - 行变换并用秩为 2 定 a=1。
  - 从阶梯形读取主元列下标，再回原矩阵取列。
  - 把原列坐标组成 H，并验算 GH=A。
- 质量发现：
  - `solution_asset_mathematical_error`：解析图把行阶梯矩阵的列直接作为 G，不能还原原矩阵 A。；建议：正式卡使用经 GH=A 验算的修正版；正确解析资产补齐前保持阻断。
- 关系裁决：
  - LA-057：`strong_candidate`；共享由原矩阵列基和坐标矩阵构造秩分解。
  - LA-100：`strong_candidate`；共享参数定秩后求列向量坐标。
  - LA-063：`medium_navigation`；共享秩约束后按列求坐标，但最终目标不同。
- 当前快照：`stale`；正式卡 `c30fae15795e9170d8e82c0dddc98b25f590e1facb8b3b319a28e60f7cb7a800`；唯一图片 2 个；物理路径 2 个。

### LA-003 2018年第18题

- 题目：历史错分重复占位卡；题图与 GS-256 相同，是含参数对数不等式证明。
- 所问：证明参数条件下的对数不等式。
- 知识点：微分不等式证明；对数不等式；辅助函数
- 第一动作：转到 GS-256，不把 LA-003 当独立复做题。
- 答案：正式内容维护在 GS-256。
- 个人错因边界：duplicate_placeholder；个人错因归属 GS-256；LA-003 只保留历史痕迹。
- 一致性：题图—解析 consistent；正式卡—图片 与 GS-256 同题，稳定 ID 与学科命名错误
- 解析主线：
  - 转到 GS-256 的辅助函数与单调性证明链。
- 质量发现：
  - `stable_id_duplicate_placeholder`：LA-003 不是独立线代错题，而是 GS-256 的重复来源。；建议：只做身份重定向与聚合阻断；未经用户确认不合并或删除稳定 ID。
- 关系裁决：
  - GS-256：`identity_duplicate_redirect`；同一道题，不计作普通强边。
- 当前快照：`stale`；正式卡 `ebb3af071399563147cdfeeca33a0b864de7b92dacfd16ed04c09cc787c5d600`；唯一图片 2 个；物理路径 2 个。

### GS-165 2019年第1题

- 题目：求 x→0 时 (x+2^x)^(2/x) 的极限。
- 所问：求幂指极限。
- 知识点：幂指极限；1 的无穷次幂；对数化；洛必达法则
- 第一动作：先设整体取对数。
- 答案：4e²
- 个人错因边界：pending_user_confirmation；旧批量无个人首答，只确认对数化是复做入口。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 整体取对数。
  - 对 0/0 型用洛必达，再指数还原。
- 质量发现：
  - `formal_body_indeterminate_form_label_corrected`：旧提醒误称底数趋非 1；实际趋 1。；建议：已修正为典型 1 的无穷次幂。
- 关系裁决：
  - GS-679：`strong_candidate`；共享幂指极限先取对数。
  - GS-072：`medium_navigation`；只共享极限主题。
- 当前快照：`stale`；正式卡 `692d845a3196d5162607e9b0806d6b40ad1168ec9784e48361f71e9436af921b`；唯一图片 2 个；物理路径 2 个。

### GS-237 2018年数2第4题：中点泰勒展开判断函数值符号

- 题目：f 在 [0,1] 二阶可导且积分为 0，判断保证 f(1/2)<0 的充分条件。
- 所问：选择充分条件。
- 知识点：二阶 Taylor 公式；中点展开；积分条件；凹凸性
- 第一动作：把 1/2 选作 Taylor 展开中心。
- 答案：D，f''(x)>0。
- 个人错因边界：pending_user_confirmation；旧批量没有个人作答。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 以 1/2 为中心写二阶 Taylor 公式。
  - 积分后一次项对称抵消，二阶余项保号。
- 关系裁决：
  - GS-253：`strong_candidate`；共享二阶 Taylor 余项保号。
  - GS-218：`medium_navigation`；共享积分条件但证明主链不同。
  - GS-665：`medium_navigation`；共享凹凸与积分比较，但目标不同。
- 当前快照：`stale`；正式卡 `40f827470d7eb31fd4e525254704b0224f1999e5b001f802d2daa49ef9f54fba`；唯一图片 2 个；物理路径 2 个。

### GS-718 77601 路径无关反求函数

- 题目：第二型曲线积分与路径无关，含未知函数 α 且给初值；先反求 α 再求端点积分。
- 所问：求端点积分。
- 知识点：第二型曲线积分；路径无关；偏导判据；反求未知函数
- 第一动作：先标 P、Q 并写 P_y=Q_x。
- 答案：1/2
- 个人错因边界：model_inferred_from_solution；用户只确认无法启动；具体偏导断点由题面与讲解链细化。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 标 P、Q，由 P_y=Q_x 求 α'(x)。
  - 结合初值得 α=x²，再选简便路径。
- 质量发现：
  - `visual_registry_backfill_applied`：正式卡、详情和图片存在，但 registry 原缺记录。；建议：四份视觉登记已补齐并通过计数与 SHA 校验。
- 关系裁决：
  - GS-719：`strong_candidate`；共享路径无关偏导判据并反求未知量。
- 当前快照：`current`；正式卡 `14465f48d2cc4ee1b2261b994c72ced23db016e220c25dd10d72880c49e5bd25`；唯一图片 2 个；物理路径 2 个。

### GS-005 1000题B组1.30 2026.4.17 ✅

- 题目：x-ln(x+sqrt(1+x²)) 与 ax^b 等价，求 a、b。
- 所问：求等价无穷小的系数和阶数。
- 知识点：等价无穷小；阶数比较；洛必达法则
- 第一动作：先判等价比值并分离非零因子。
- 答案：a=1/6，b=3。
- 个人错因边界：legacy_unclassified；正式卡记录直接全 Taylor 等风险，但证据来源未分类。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 对比值用洛必达。
  - 分离趋于非零常数的因子与真正趋零部分，再匹配幂次和系数。
- 质量发现：
  - `formal_lecture_refs_backfilled`：正式卡原 lecture_refs 未直接绑定当前视觉证据。；建议：已补详情、题图和解析图路径。
- 关系裁决：
  - GS-547：`strong_candidate`；共享无穷小比阶和幂次匹配。
  - GS-113：`strong_candidate`；共享最低阶主项判断。
  - GS-455：`strong_candidate`；共享相消后找最低非零项。
  - GS-074：`reject_as_strong`；只共享 Taylor 工具。
- 当前快照：`stale`；正式卡 `49bbebe427fbb60ca9b38a836bfb9dfd5e5100870bb21d6e579d96e1ed0ce5ab`；唯一图片 2 个；物理路径 2 个。

### GS-095 1000题B组4.1

- 题目：平方因式分别整除 f(x)+1 与 f(x)-1，构造三次多项式 f。
- 所问：求 f。
- 知识点：多项式整除；二重根条件；函数值与导数条件
- 第一动作：平方因式整除同时触发函数值与导数条件。
- 答案：f(x)=x³/2-3x/2。
- 个人错因边界：legacy_unclassified_with_current_question_evidence；只有 2026-06-10 记录可绑定当前题；更早历史疑似跨题污染。
- 一致性：题图—解析 consistent；正式卡—图片 consistent_after_detail_equation_fix
- 解析主线：
  - 把平方因式整除转成函数值与导数条件。
  - 保留一次商并代入另一组二重根条件。
- 质量发现：
  - `cross_question_wrong_history_contamination`：前两条 wrong_history 描述导数定义型极限，无法由当前题验证。；建议：保留不可变历史；个人错因聚合只采用 2026-06-10 可绑定证据。
  - `visual_detail_equation_corrected`：详情页原代入式少计一项。；建议：已修正为 4(a+b)+4a=0。
  - `formal_lecture_refs_backfilled`：正式卡原视觉引用不完整。；建议：已补详情、题图与解析图。
- 关系裁决：
  - GS-443：`strong_candidate`；共享由整除条件抽取已知因式。
  - GS-099：`medium_navigation`；共享把条件翻译成导数信息。
  - GS-458：`medium_navigation`；共享导数条件反推。
  - GS-035：`reject_as_strong`；不共享多项式二重根整除主链。
  - GS-470：`reject_as_strong`；不共享多项式二重根整除主链。
  - GS-060：`reject_as_strong`；不共享多项式二重根整除主链。
  - GS-100：`reject_as_strong`；不共享多项式二重根整除主链。
  - GS-456：`reject_as_strong`；不共享多项式二重根整除主链。
  - GS-463：`reject_as_strong`；不共享多项式二重根整除主链。
  - GS-471：`reject_as_strong`；不共享多项式二重根整除主链。
- 当前快照：`stale`；正式卡 `ac1d92f4bb3f463cc94ce12a86918e13d63fbe49724c3741bc25136d5694560a`；唯一图片 2 个；物理路径 2 个。

### GS-646 102465 参数曲线切线方程

- 题目：参数式空间曲线在 t=0 处求切线。
- 所问：写空间切线方程。
- 知识点：参数式空间曲线；切向量；空间直线点向式
- 第一动作：先代 t=0 求切点。
- 答案：x/1=(y-1)/2=(z-2)/3。
- 个人错因边界：confirmed_personal；复做时已求出切点和切向量，但没有继续写空间直线，并误用平面显函数切线公式。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 代 t=0 求切点。
  - 对三个坐标求导得切向量，再写空间直线点向式。
- 质量发现：
  - `visual_detail_latest_recurrence_corrected`：详情页停留在较早错误版本。；建议：已更新为最新用户确认复发断点。
- 关系裁决：
  - GS-647：`strong_candidate`；共享参数曲线求切向量并进入点向结构。
  - GS-629：`medium_navigation`；只共享方向向量角色。
- 当前快照：`stale`；正式卡 `9d1a23708692b36c0facfe7f7c01dc309687269197f44421dda9726c642b7d6a`；唯一图片 3 个；物理路径 4 个。

### GS-705 102340 星形线边界方向与绝对值

- 题目：上半星形线与 x 轴围成区域，沿逆时针边界计算含绝对值的第二型曲线积分。
- 所问：求曲线积分。
- 知识点：参数曲线；有向边界；绝对值分段；第二型曲线积分
- 第一动作：先列边界每一段及方向。
- 答案：-3π/16
- 个人错因边界：confirmed_personal；误把完整星形线当区域边界，并机械反转积分限。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 先确认真实边界和参数范围。
  - 分段处理绝对值并用对称性。
- 质量发现：
  - `visual_registry_backfill_applied`：正式卡、详情和图片存在但 registry 原缺记录。；建议：四份视觉登记已补齐并核验。
- 关系裁决：
  - GS-644：`strong_candidate`；共享星形线参数范围与几何量计算。
  - GS-708：`medium_navigation`；共享有向边界，但主积分结构不同。
- 当前快照：`stale`；正式卡 `d0d5bc1b41ef5f0faaf3ac7d14f5cdf222dab070c278e06ed9b655fbdfe080b0`；唯一图片 3 个；物理路径 4 个。

### GS-706 76551 带权微分与参数最值

- 题目：曲线族 y=a sin x 中求使第二型曲线积分最小的曲线。
- 所问：求最优 a 与曲线。
- 知识点：第二型曲线积分参数化；位置权重；参数最值
- 第一动作：写 dy=a cos x dx，把整条曲线化为一元积分。
- 答案：a=1，y=sin x；最小值 π-8/3。
- 个人错因边界：confirmed_personal；把无权 ∫dy=0 机械推广到带位置权重的 ∫xdy=0。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 统一用 x 参数化。
  - 得到 I(a)=π+4a³/3-4a 后求极值。
- 质量发现：
  - `visual_registry_backfill_applied`：视觉 registry 原缺记录。；建议：四份视觉登记已补齐并核验。
- 当前快照：`stale`；正式卡 `7c2d538271c8f109da490be8d405884a363d354d5af4bbc6fc5cf34c088c2118`；唯一图片 2 个；物理路径 2 个。

### GS-707 102348 向量场做功与格林公式

- 题目：位置相关向量场中沿单位圆顺时针一周，求变力做功。
- 所问：求功。
- 知识点：向量场；变力做功；格林公式；方向
- 第一动作：先写 dW=Pdx+Qdy。
- 答案：-π/2
- 个人错因边界：confirmed_personal；把位置相关变力当固定力，企图用圆周长相乘。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 读出 P、Q 并写功积分。
  - 用格林公式并处理顺时针负号。
- 质量发现：
  - `visual_registry_backfill_applied`：视觉 registry 原缺记录。；建议：四份视觉登记已补齐并核验。
- 关系裁决：
  - GS-708：`strong_candidate`；共享 P/Q 映射、格林公式与有向边界。
  - GS-709：`medium_navigation`；共享格林公式，但主断点不同。
- 当前快照：`stale`；正式卡 `25f2dbb7a3136a2c61972ad271dfbecf7c1120fd6c5f5ba7e7fc8333dcdebe06`；唯一图片 2 个；物理路径 2 个。

### GS-708 78025 补线格林公式与PQ映射

- 题目：第一象限两段圆弧组成开曲线，补线后用格林公式求第二型曲线积分。
- 所问：求曲线积分。
- 知识点：P 与 Q 映射；开曲线补线；格林公式；有向边界
- 第一动作：圈出 dx 前的 P 与 dy 前的 Q。
- 答案：π/2-4
- 个人错因边界：confirmed_personal；未稳定建立 dx 系数对应 P、dy 系数对应 Q。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 标 P、Q 并算 Q_x-P_y=1。
  - 补 y 轴线段，按面积作差并扣补线积分。
- 质量发现：
  - `visual_registry_backfill_applied`：视觉 registry 原缺记录。；建议：四份视觉登记已补齐并核验。
- 关系裁决：
  - GS-709：`strong_candidate`；共享 P/Q 映射、格林公式和方向；GS-709 是含奇点扩展。
  - GS-719：`medium_navigation`；共享偏导组合，但任务目标不同。
- 当前快照：`stale`；正式卡 `285f3fad94109e012cf43aec55c501edba3267114976344091f031718865935b`；唯一图片 2 个；物理路径 3 个。

### GS-709 79076 含奇点曲线积分与挖洞格林公式

- 题目：逆时针圆周上的分式型第二型曲线积分，分母在原点产生内部奇点。
- 所问：求含奇点闭曲线积分。
- 知识点：格林公式条件；内部奇点；多连通区域；挖洞法
- 第一动作：闭曲线积分出现分母时先找奇点。
- 答案：π
- 个人错因边界：confirmed_personal；准备直接套格林公式，未检查原点奇点。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 先找内部奇点。
  - 挖小椭圆后在多连通区域使用格林公式。
- 质量发现：
  - `visual_registry_backfill_applied`：视觉 registry 原缺记录。；建议：四份视觉登记已补齐并核验。
  - `visual_detail_solution_embed_backfilled`：详情页原缺解析图折叠入口和正式卡 solution 引用。；建议：已补 solution 引用与折叠解析。
- 关系裁决：
  - GS-708：`strong_candidate`；共享格林公式、P/Q 映射和有向边界。
  - GS-707：`medium_navigation`；共享格林公式但主断点不同。
- 当前快照：`stale`；正式卡 `b1e45e7ccd8ad4f5c3ca6f20afa3b2afa8ee77748316cc913d3ff7c6960716cd`；唯一图片 2 个；物理路径 2 个。

### GS-710 57932 凑微分与抵消

- 题目：含 exp(sin x) 的不定积分，拆项后两次分部积分产生相反余项。
- 所问：求原函数。
- 知识点：凑微分；分部积分；抵消结构
- 第一动作：拆项后逐项做导数反查。
- 答案：x exp(sin x)-exp(sin x)/cos x+C
- 个人错因边界：confirmed_personal；拆分正确，但未识别两个微分与余项抵消。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 逐项做导数反查。
  - 两项分部积分后的中间积分抵消。
- 质量发现：
  - `visual_registry_backfill_applied`：视觉 registry 原缺记录。；建议：四份视觉登记已补齐并核验。
- 关系裁决：
  - GS-632：`strong_candidate`；共享拆项、分部积分与余项精确抵消。
- 当前快照：`current`；正式卡 `62b61865586a760e1c8304d94fbe2e06a022be5108ceb501579548710533aedc`；唯一图片 2 个；物理路径 2 个。

### GS-711 28875 整体换元与乘积求导

- 题目：含 exp(-sin x) 与三角幂分母的不定积分，需整体换元并识别商导数。
- 所问：求原函数。
- 知识点：整体换元；三角恒等变形；商的导数
- 第一动作：选择能同时统一最多结构的换元。
- 答案：8 exp(-sin x)/(1-sin x)+C
- 个人错因边界：confirmed_personal；换元没有统一全部结构，后续也未做分子凑分母。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 令 u=-sin x 统一指数、分母和微分。
  - 分子凑分母后识别乘积或商的导数。
- 质量发现：
  - `visual_registry_backfill_applied`：视觉 registry 原缺记录。；建议：四份视觉登记已补齐并核验。
- 关系裁决：
  - GS-636：`medium_navigation`；共享整体换元，但后续目标不同。
- 当前快照：`current`；正式卡 `7199dc390876c7cb996c671f4dc64d6326aeb2b7445bce60d2af19f666af3107`；唯一图片 2 个；物理路径 2 个。

### GS-712 58015 复合函数反求与分部积分

- 题目：已知 f(ln x) 的表达式，先反求 f，再计算不定积分。
- 所问：求 ∫f(x)dx。
- 知识点：复合函数反求；自变量角色；分部积分
- 第一动作：先只解决函数身份，不同时改目标积分。
- 答案：x-(1+exp(-x))ln(1+exp(x))+C
- 个人错因边界：confirmed_personal；把反求函数与积分换元混在一起，得到 f 后又未触发分部积分。
- 一致性：题图—解析 consistent；正式卡—图片 consistent
- 解析主线：
  - 先单独反求 f。
  - 再对所得乘积做分部积分。
- 质量发现：
  - `visual_registry_backfill_applied`：视觉 registry 原缺记录。；建议：四份视觉登记已补齐并核验。
- 关系裁决：
  - GS-704：`strong_candidate`；共享先反求函数再分部积分。
  - GS-265：`medium_navigation`；只共享复合函数反求。
  - GS-273：`medium_navigation`；只共享后半段分部积分。
- 当前快照：`current`；正式卡 `7141ce73c6590a733fea7a2fc4923346e96a20c846427d4bfce9fd0cf7dce4b2`；唯一图片 2 个；物理路径 2 个。

## 重建与验收

```bash
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py build
python3 错题知识网络/scripts/build_knowledge_error_evidence_graph.py check
python3 -m unittest tests.test_knowledge_error_evidence_graph
```
