---
wiki_id: SRC-WQ-GS-662
type: source_summary
title: GS-662 57909 复合三角积分比较
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-662_57909复合三角积分比较.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-662_57909复合三角积分比较.md
visual_ids:
- VIS-GS-662
wrongnet_refs:
- GS-662
knowledge:
- 定积分
- 积分保序
- 函数单调性
- 三角不等式
- 复合函数点态比较
error_causes:
- 题型识别失败
- 方法论调取失败
- 触发信息遗漏
- 换元路径锁定
- 中间量引入缺失
methods:
- 先判型
- 中间量比较
- 点态比较
- 积分保序
- 三角函数单调性
- 三角不等式
- 定积分大小估计
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-003_B2-TRIGGER
- MATHWIKI-ERROR-CLUSTER-003_题型识别失败
- MATHWIKI-ERROR-CLUSTER-007_方法论调取失败
- MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏
- MATHWIKI-ERROR-CLUSTER-109_中间量引入缺失
- MATHWIKI-ERROR-CLUSTER-230_换元路径锁定
- MATHWIKI-KNOWLEDGE-002_定积分
- MATHWIKI-KNOWLEDGE-007_定积分性质
- MATHWIKI-KNOWLEDGE-071_函数单调性
- MATHWIKI-KNOWLEDGE-224_三角函数单调性
- MATHWIKI-KNOWLEDGE-239_单调性比较
- MATHWIKI-KNOWLEDGE-284_三角不等式
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-060_积分保序
- MATHWIKI-METHOD-CLUSTER-138_三角不等式
- MATHWIKI-METHOD-CLUSTER-219_定积分大小估计
- MATHWIKI-METHOD-CLUSTER-425_点态比较
- MATHWIKI-METHOD-CLUSTER-513_三角函数单调性
- MATHWIKI-METHOD-CLUSTER-540_中间量比较
- MATHWIKI-GS-ERROR-005_题型识别失败
- MATHWIKI-GS-METHOD-099_复合三角积分中间量比较链
- MATHWIKI-GS-TOPIC-006_定积分错题总线
status: indexed
last_updated: '2026-07-25'
related_wrongnet_refs: []
formal_projection_sha256: b067302d826c05c6e77e726a4a685732fd3f24b6e3d2bcd654de22ee638ff47d
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-662/question_01.png
solution_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-662/solution_01.png
reference_asset_refs: []
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
evidence_status: user_confirmed
confirmation_state: confirmed
question_surface_status: registered_answer_safe_question_only
solution_surface_status: registered_solution_surface
aggregate_edge_policy: allow
evidence_boundary: 题图和解析只核验客观题意与解法；个人错因按 evidence_status 门禁。
review_batch: MATHWIKI-REVIEW-082
---

# GS-662 57909 复合三角积分比较

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-662_57909复合三角积分比较.md`
- wrongnet ID：`GS-662`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-662_57909复合三角积分比较.md`（`VIS-GS-662`）
- 题图 1 张；解析图 1 张；参考图 0 张。

## 当前语义投影

- 知识点：定积分、积分保序、函数单调性、三角不等式、复合函数点态比较
- 方法：先判型、中间量比较、点态比较、积分保序、三角函数单调性、三角不等式、定积分大小估计
- 错因字段：题型识别失败、方法论调取失败、触发信息遗漏、换元路径锁定、中间量引入缺失
- 第一动作：先写 0<sin x<x，再分别用外层 sin 递增、cos 递减作点态比较。
- 个人断点：没有从复合三角函数比较题中触发“引入 \\(x\\) 作中间量”的动作，而是持续尝试换元，把问题带到 \\(\\arcsin t\\) 的复杂路径。
- 方法卡 ID：H08-006
- 当前强关系：暂无强边

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-109_中间量引入缺失]]
- [[MATHWIKI-ERROR-CLUSTER-230_换元路径锁定]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-071_函数单调性]]
- [[MATHWIKI-KNOWLEDGE-224_三角函数单调性]]
- [[MATHWIKI-KNOWLEDGE-239_单调性比较]]
- [[MATHWIKI-KNOWLEDGE-284_三角不等式]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-060_积分保序]]
- [[MATHWIKI-METHOD-CLUSTER-138_三角不等式]]
- [[MATHWIKI-METHOD-CLUSTER-219_定积分大小估计]]
- [[MATHWIKI-METHOD-CLUSTER-425_点态比较]]
- [[MATHWIKI-METHOD-CLUSTER-513_三角函数单调性]]
- [[MATHWIKI-METHOD-CLUSTER-540_中间量比较]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-099_复合三角积分中间量比较链]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]

## 客观解法补强

- 在 \((0,\frac\pi2)\) 上，\(\sin x<x\)，且外层 \(\sin\) 递增、\(\cos\) 递减，因此 \(\sin(\sin x)<\sin x\)，而 \(\cos(\sin x)>\cos x\)。
