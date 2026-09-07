---
wiki_id: SRC-WQ-GS-613
type: source_summary
title: GS-613 102155 幂级数偶数项系数求和 2026.6.19
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-613_102155幂级数偶数项系数求和.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-613_102155.md
visual_ids:
- VIS-GS-613
wrongnet_refs:
- GS-613
knowledge:
- 无穷级数
- 幂级数
- 函数展开成幂级数
- 常用幂级数展开式
- 对数级数展开
- 幂级数系数提取
- 数项级数求和
- 等比级数求和
error_causes:
- 下标替换断点
- 起点检查遗漏
- 等比级数首项错判
- 符号幂次简化不熟练
methods:
- 提常数化标准展开式
- 套ln(1+t)展开读系数
- 下标替换n→2n
- 系数提取下标对齐
- 重判新下标起点
- 等比级数求和先写首项
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-004_B5-CHECK
- MATHWIKI-ERROR-CLUSTER-105_下标替换断点
- MATHWIKI-ERROR-CLUSTER-400_符号幂次简化不熟练
- MATHWIKI-ERROR-CLUSTER-408_等比级数首项错判
- MATHWIKI-ERROR-CLUSTER-430_起点检查遗漏
- MATHWIKI-KNOWLEDGE-005_无穷级数
- MATHWIKI-KNOWLEDGE-048_幂级数
- MATHWIKI-KNOWLEDGE-122_常用幂级数展开式
- MATHWIKI-KNOWLEDGE-137_函数展开成幂级数
- MATHWIKI-KNOWLEDGE-175_对数级数展开
- MATHWIKI-KNOWLEDGE-208_幂级数系数提取
- MATHWIKI-KNOWLEDGE-267_等比级数求和
- MATHWIKI-KNOWLEDGE-376_数项级数求和
- MATHWIKI-METHOD-CLUSTER-1043_提常数化标准展开式
- MATHWIKI-METHOD-CLUSTER-1292_等比级数求和先写首项
- MATHWIKI-METHOD-CLUSTER-1390_重判新下标起点
- MATHWIKI-METHOD-CLUSTER-451_系数提取下标对齐
- MATHWIKI-METHOD-CLUSTER-523_下标替换n→2n
- MATHWIKI-METHOD-CLUSTER-885_套ln-1+t-展开读系数
- MATHWIKI-GS-METHOD-067_幂级数系数提取下标对齐
- MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线
status: indexed
last_updated: '2026-07-25'
related_wrongnet_refs: []
formal_projection_sha256: 23631f5f850f5adec99c90edfc35a8cf4130a0d18a011684e94c2a3c6edb2249
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-613/question_01.png
solution_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-613/solution_01.png
reference_asset_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: allow
evidence_boundary: "个人错因仅来自正式学习事务中的 wrong_history；视觉资产和客观解析不反推个人错因。"
review_batch: MATHWIKI-REVIEW-080
confirmation_state: confirmed
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
---

# GS-613 102155 幂级数偶数项系数求和 2026.6.19

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-613_102155幂级数偶数项系数求和.md`
- wrongnet ID：`GS-613`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-613_102155.md`（`VIS-GS-613`）
- 题图 1 张；解析图 1 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、幂级数、函数展开成幂级数、常用幂级数展开式、对数级数展开、幂级数系数提取、数项级数求和、等比级数求和
- 方法：提常数化标准展开式、套ln(1+t)展开读系数、下标替换n→2n、系数提取下标对齐、重判新下标起点、等比级数求和先写首项
- 错因字段：下标替换断点、起点检查遗漏、等比级数首项错判、符号幂次简化不熟练
- 第一动作：先写 \(a_{2n}=\frac{(-1)^{2n-1}}{2n\cdot2^{2n}}=-\frac1{2n\cdot4^n}\)，再检查原公式 \(a_n\) 适用范围 \(n\ge1\)，确定求和从 \(n=1\) 起。
- 个人断点：没检查 \(a_{2n}\) 的新起点；把从 \(n=1\) 开始的等比级数 \(\sum\frac1{4^n}\) 误当成从 \(n=0\) 开始，首项取成 \(-\frac12\) 而非正确的 \(-\frac18\)。
- 方法卡 ID：LM-H31
- 当前强关系：暂无强边

## 证据边界

- 个人错因仅来自正式学习事务中的 wrong_history；视觉资产和客观解析不反推个人错因。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-105_下标替换断点]]
- [[MATHWIKI-ERROR-CLUSTER-400_符号幂次简化不熟练]]
- [[MATHWIKI-ERROR-CLUSTER-408_等比级数首项错判]]
- [[MATHWIKI-ERROR-CLUSTER-430_起点检查遗漏]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-122_常用幂级数展开式]]
- [[MATHWIKI-KNOWLEDGE-137_函数展开成幂级数]]
- [[MATHWIKI-KNOWLEDGE-175_对数级数展开]]
- [[MATHWIKI-KNOWLEDGE-208_幂级数系数提取]]
- [[MATHWIKI-KNOWLEDGE-267_等比级数求和]]
- [[MATHWIKI-KNOWLEDGE-376_数项级数求和]]
- [[MATHWIKI-METHOD-CLUSTER-1043_提常数化标准展开式]]
- [[MATHWIKI-METHOD-CLUSTER-1292_等比级数求和先写首项]]
- [[MATHWIKI-METHOD-CLUSTER-1390_重判新下标起点]]
- [[MATHWIKI-METHOD-CLUSTER-451_系数提取下标对齐]]
- [[MATHWIKI-METHOD-CLUSTER-523_下标替换n→2n]]
- [[MATHWIKI-METHOD-CLUSTER-885_套ln-1+t-展开读系数]]
- [[MATHWIKI-GS-METHOD-067_幂级数系数提取下标对齐]]
- [[MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
