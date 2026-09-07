---
wiki_id: SRC-WQ-GS-598
type: source_summary
title: GS-598 138763 根式扰动交错级数
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-598_138763根式扰动交错级数.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-598_138763.md
visual_ids:
- VIS-GS-598
wrongnet_refs:
- GS-598
knowledge:
- 无穷级数
- 数项级数敛散性判别
- 任意项级数
- 交错级数
- 莱布尼茨判别法
- p级数
- 绝对收敛
- 条件收敛
- 等价无穷小
- 泰勒公式
error_causes:
- 方法入口缺失
- 触发信息遗漏
- 方法论调取失败
- 动作链断裂
- 条件检查遗漏
methods:
- 先判型
- 交错纠缠拆项
- 主量提出
- 泰勒展开
- 二项式展开
- 交错级数判别法
- 莱布尼茨判别法
- p级数判别
- 取绝对值
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-003_B2-TRIGGER
- MATHWIKI-ERROR-CLUSTER-004_动作链断裂
- MATHWIKI-ERROR-CLUSTER-007_方法论调取失败
- MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏
- MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏
- MATHWIKI-ERROR-CLUSTER-058_方法入口缺失
- MATHWIKI-KNOWLEDGE-004_等价无穷小
- MATHWIKI-KNOWLEDGE-005_无穷级数
- MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别
- MATHWIKI-KNOWLEDGE-015_泰勒公式
- MATHWIKI-KNOWLEDGE-036_p级数
- MATHWIKI-KNOWLEDGE-059_交错级数
- MATHWIKI-KNOWLEDGE-074_绝对收敛
- MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法
- MATHWIKI-KNOWLEDGE-087_任意项级数
- MATHWIKI-KNOWLEDGE-095_条件收敛
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-008_泰勒展开
- MATHWIKI-METHOD-CLUSTER-027_p级数判别
- MATHWIKI-METHOD-CLUSTER-030_取绝对值
- MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法
- MATHWIKI-METHOD-CLUSTER-106_交错纠缠拆项
- MATHWIKI-METHOD-CLUSTER-139_二项式展开
- MATHWIKI-METHOD-CLUSTER-284_交错级数判别法
- MATHWIKI-METHOD-CLUSTER-542_主量提出
- MATHWIKI-GS-METHOD-012_等价无穷小使用条件
- MATHWIKI-GS-METHOD-063_交错纠缠级数拆项与条件收敛闭环
- MATHWIKI-GS-TOPIC-003_高频知识主线总览
- MATHWIKI-GS-TOPIC-004_极限与连续错题总线
- MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线
status: indexed
last_updated: '2026-07-24'
related_wrongnet_refs: []
formal_projection_sha256: 265fc0052cec7c172829a9eb34eba4ea7e71a65c6698b58d4cfea814b1968083
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-598/question_01.png
solution_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-598/solution_01.png
reference_asset_refs: []
evidence_status: legacy_unclassified
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: block_strong_edges
evidence_boundary: "个人错因待用户确认；题图、解析图与生成式详情仅核验客观内容，不得升级为 user_confirmed。"
review_batch: MATHWIKI-REVIEW-078
confirmation_state: pending_user_confirmation
---

# GS-598 138763 根式扰动交错级数

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-598_138763根式扰动交错级数.md`
- wrongnet ID：`GS-598`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-598_138763.md`（`VIS-GS-598`）
- 题图 1 张；解析图 1 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、数项级数敛散性判别、任意项级数、交错级数、莱布尼茨判别法、p级数、绝对收敛、条件收敛、等价无穷小、泰勒公式
- 方法：先判型、交错纠缠拆项、主量提出、泰勒展开、二项式展开、交错级数判别法、莱布尼茨判别法、p级数判别、取绝对值
- 错因字段：方法入口缺失、触发信息遗漏、方法论调取失败、动作链断裂、条件检查遗漏
- 第一动作：先提出 \(\sqrt n\)，写出 \(\frac{(-1)^n}{\sqrt n}\left(1+\frac{(-1)^n}{n}\right)^{-1/2}\)。
- 候选个人断点（待确认）：没有从根号扰动结构联想到 \((1+x)^{-1/2}\) 的泰勒展开，也没有完整执行“原级数收敛 + 绝对值级数发散”的条件收敛确认。
- 方法卡 ID：H16-016
- 正式强边：暂无强边（证据门禁未通过）。

## 证据边界

- 候选个人错因来自历史结构化字段，仍待用户确认；题图、解析图与详情叙述只核验客观内容。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-058_方法入口缺失]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-KNOWLEDGE-036_p级数]]
- [[MATHWIKI-KNOWLEDGE-059_交错级数]]
- [[MATHWIKI-KNOWLEDGE-074_绝对收敛]]
- [[MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法]]
- [[MATHWIKI-KNOWLEDGE-087_任意项级数]]
- [[MATHWIKI-KNOWLEDGE-095_条件收敛]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-027_p级数判别]]
- [[MATHWIKI-METHOD-CLUSTER-030_取绝对值]]
- [[MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法]]
- [[MATHWIKI-METHOD-CLUSTER-106_交错纠缠拆项]]
- [[MATHWIKI-METHOD-CLUSTER-139_二项式展开]]
- [[MATHWIKI-METHOD-CLUSTER-284_交错级数判别法]]
- [[MATHWIKI-METHOD-CLUSTER-542_主量提出]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-METHOD-063_交错纠缠级数拆项与条件收敛闭环]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
