---
wiki_id: SRC-WQ-GS-663
type: source_summary
title: GS-663 81436 定积分比较作差反折
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-663_81436定积分比较作差反折.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-663_81436定积分比较作差反折.md
visual_ids:
- VIS-GS-663
wrongnet_refs:
- GS-663
knowledge:
- 定积分
- 作差法
- 倒数比较方向
- 变号区间分段
- 对称换元
- 区间再现
error_causes:
- 运算路径不稳
- 动作链断裂
- 方法论调取不稳
- 计算失误
- 符号错误
methods:
- 先判型
- 被积函数比较
- 作差法
- 对称换元
- 积分保序
- 分母单调转倒数单调
- 定积分大小估计
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-007_B7-CALC
- MATHWIKI-ERROR-CLUSTER-004_动作链断裂
- MATHWIKI-ERROR-CLUSTER-014_计算失误
- MATHWIKI-ERROR-CLUSTER-019_符号错误
- MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳
- MATHWIKI-ERROR-CLUSTER-028_运算路径不稳
- MATHWIKI-KNOWLEDGE-002_定积分
- MATHWIKI-KNOWLEDGE-007_定积分性质
- MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算
- MATHWIKI-KNOWLEDGE-111_对称换元
- MATHWIKI-KNOWLEDGE-224_三角函数单调性
- MATHWIKI-KNOWLEDGE-239_单调性比较
- MATHWIKI-KNOWLEDGE-300_作差法
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-060_积分保序
- MATHWIKI-METHOD-CLUSTER-063_作差法
- MATHWIKI-METHOD-CLUSTER-095_对称换元
- MATHWIKI-METHOD-CLUSTER-1332_被积函数比较
- MATHWIKI-METHOD-CLUSTER-219_定积分大小估计
- MATHWIKI-METHOD-CLUSTER-312_分母单调转倒数单调
- MATHWIKI-GS-METHOD-100_定积分比较作差反折链
- MATHWIKI-GS-TOPIC-006_定积分错题总线
status: indexed
last_updated: '2026-07-25'
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-663/question_01.png
solution_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-663/solution_01.png
reference_asset_refs: []
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
related_wrongnet_refs: []
evidence_status: user_confirmed
confirmation_state: confirmed
question_surface_status: registered_answer_safe_question_only
solution_surface_status: registered_solution_surface
aggregate_edge_policy: allow
evidence_boundary: 题图和解析只核验客观题意与解法；个人错因按 evidence_status 门禁。
review_batch: MATHWIKI-REVIEW-082
formal_projection_sha256: 1b7b3b90f8ee68a9bf4dda3ce65298596bfafb801c62faed5629441ffde8da08
---

# GS-663 81436 定积分比较作差反折

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-663_81436定积分比较作差反折.md`
- wrongnet ID：`GS-663`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-663_81436定积分比较作差反折.md`（`VIS-GS-663`）
- 题图 1 张；解析图 1 张；参考图 0 张。

## 当前语义投影

- 知识点：定积分、作差法、倒数比较方向、变号区间分段、对称换元、区间再现
- 方法：先判型、被积函数比较、作差法、对称换元、积分保序、分母单调转倒数单调、定积分大小估计
- 错因字段：运算路径不稳、动作链断裂、方法论调取不稳、计算失误、符号错误
- 第一动作：先直接比较 I2、I3，再将 I1-I2 作差并在 pi/4 处分段反折。
- 个人断点：有作差意识但没有把 \\(I_1-I_2\\) 落地；比较分母时忘记倒数不等号反向；反折换元时把 \\(\\frac\\pi2-\\frac\\pi4\\) 算成负数。
- 方法卡 ID：H11-003
- 当前强关系：暂无强边

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-007_B7-CALC]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-ERROR-CLUSTER-019_符号错误]]
- [[MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳]]
- [[MATHWIKI-ERROR-CLUSTER-028_运算路径不稳]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-111_对称换元]]
- [[MATHWIKI-KNOWLEDGE-224_三角函数单调性]]
- [[MATHWIKI-KNOWLEDGE-239_单调性比较]]
- [[MATHWIKI-KNOWLEDGE-300_作差法]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-060_积分保序]]
- [[MATHWIKI-METHOD-CLUSTER-063_作差法]]
- [[MATHWIKI-METHOD-CLUSTER-095_对称换元]]
- [[MATHWIKI-METHOD-CLUSTER-1332_被积函数比较]]
- [[MATHWIKI-METHOD-CLUSTER-219_定积分大小估计]]
- [[MATHWIKI-METHOD-CLUSTER-312_分母单调转倒数单调]]
- [[MATHWIKI-GS-METHOD-100_定积分比较作差反折链]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]

## 客观解法补强

- 分段后用 \(x\mapsto\frac\pi2-x\) 把 \((\frac\pi4,\frac\pi2)\) 反折到 \((0,\frac\pi4)\)，再比较同一区间上的正负。
