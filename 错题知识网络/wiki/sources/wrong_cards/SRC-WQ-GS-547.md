---
wiki_id: SRC-WQ-GS-547
type: source_summary
title: GS-547 136827 无穷小比阶最低阶
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-547_136827无穷小比阶最低阶.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-547_136827-2026.6.4.md
visual_ids:
- VIS-GS-547
wrongnet_refs:
- GS-547
knowledge:
- 极限与连续
- 等价无穷小
- 变上限积分
- 泰勒展开
- 幂级数
- 无穷小阶数比较
- 主导项
error_causes:
- 概念混淆
- 方法选择错误
- 过程跳步
methods:
- 先判型
- 等价变形
- 泰勒展开
- 主导项比较
- 变上限积分等价替换
- 最低阶非零项
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-002_B4-CHAIN
- MATHWIKI-ERROR-CLUSTER-001_方法选择错误
- MATHWIKI-ERROR-CLUSTER-002_过程跳步
- MATHWIKI-ERROR-CLUSTER-006_概念混淆
- MATHWIKI-KNOWLEDGE-003_极限与连续
- MATHWIKI-KNOWLEDGE-004_等价无穷小
- MATHWIKI-KNOWLEDGE-008_变上限积分
- MATHWIKI-KNOWLEDGE-038_泰勒展开
- MATHWIKI-KNOWLEDGE-048_幂级数
- MATHWIKI-KNOWLEDGE-051_无穷小阶数比较
- MATHWIKI-KNOWLEDGE-086_主导项
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-003_等价变形
- MATHWIKI-METHOD-CLUSTER-008_泰勒展开
- MATHWIKI-METHOD-CLUSTER-021_主导项比较
- MATHWIKI-METHOD-CLUSTER-1082_最低阶非零项
- MATHWIKI-METHOD-CLUSTER-332_变上限积分等价替换
- MATHWIKI-GS-ERROR-003_方法选择错误
- MATHWIKI-GS-ERROR-004_过程跳步
- MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点
- MATHWIKI-GS-METHOD-012_等价无穷小使用条件
- MATHWIKI-GS-TOPIC-003_高频知识主线总览
- MATHWIKI-GS-TOPIC-004_极限与连续错题总线
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
last_updated: '2026-07-24'
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-547/question_01.png
solution_asset_refs: []
reference_asset_refs: []
related_wrongnet_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: allow
evidence_boundary: 个人错因只来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。
review_batch: MATHWIKI-REVIEW-074
formal_projection_sha256: 62bc98975d449e86c4311e105a45ac7f712b2d5f013dd88620d334f3a70aa710
---

# GS-547 136827 无穷小比阶最低阶

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-547_136827无穷小比阶最低阶.md`
- wrongnet ID：`GS-547`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-547_136827-2026.6.4.md`（`VIS-GS-547`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：极限与连续、等价无穷小、变上限积分、泰勒展开、幂级数、无穷小阶数比较、主导项
- 方法：先判型、等价变形、泰勒展开、主导项比较、变上限积分等价替换、最低阶非零项
- 错因字段：概念混淆、方法选择错误、过程跳步
- 第一动作：先用 \(\sin(t^2)\sim t^2\)、\(\sin x\sim x\) 得 \(f(x)\sim\int_0^x t^2dt=\frac{x^3}{3}\)，再抓 \(g(x)\) 的最低阶项。
- 个人断点：把幂级数求和模板误当入口，没有先抓 \(x\to0\) 时的最低阶非零项。
- 方法卡 ID：H01-004
- 当前强关系：暂无强边

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-038_泰勒展开]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-051_无穷小阶数比较]]
- [[MATHWIKI-KNOWLEDGE-086_主导项]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]
- [[MATHWIKI-METHOD-CLUSTER-1082_最低阶非零项]]
- [[MATHWIKI-METHOD-CLUSTER-332_变上限积分等价替换]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
