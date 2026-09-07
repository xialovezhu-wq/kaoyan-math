---
wiki_id: SRC-WQ-GS-606
type: source_summary
title: GS-606 138781 加法项拆等比调和判散
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-606_138781加法项拆等比调和判散.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-606_138781.md
visual_ids:
- VIS-GS-606
wrongnet_refs:
- GS-606
knowledge:
- 无穷级数
- 数项级数敛散性判别
- 收敛级数线性运算
- 等比级数
- 调和级数
- 级数拆项
error_causes:
- 触发信息遗漏
- 通项极限后动作中断
- 拆项触发不敏感
- 负底数幂符号处理不熟
- 级数线性性质表述不严谨
methods:
- 先判型
- 通项趋零
- 交错纠缠拆项
- 拆项判敛散
- 收敛级数线性运算
- 等比数列求和
- 调和级数比较
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-003_B2-TRIGGER
- MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏
- MATHWIKI-ERROR-CLUSTER-078_拆项触发不敏感
- MATHWIKI-ERROR-CLUSTER-414_级数线性性质表述不严谨
- MATHWIKI-ERROR-CLUSTER-428_负底数幂符号处理不熟
- MATHWIKI-ERROR-CLUSTER-438_通项极限后动作中断
- MATHWIKI-KNOWLEDGE-005_无穷级数
- MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别
- MATHWIKI-KNOWLEDGE-097_调和级数
- MATHWIKI-KNOWLEDGE-104_等比级数
- MATHWIKI-KNOWLEDGE-128_级数拆项
- MATHWIKI-KNOWLEDGE-178_收敛级数线性运算
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-062_通项趋零
- MATHWIKI-METHOD-CLUSTER-106_交错纠缠拆项
- MATHWIKI-METHOD-CLUSTER-119_收敛级数线性运算
- MATHWIKI-METHOD-CLUSTER-156_拆项判敛散
- MATHWIKI-METHOD-CLUSTER-255_等比数列求和
- MATHWIKI-METHOD-CLUSTER-460_调和级数比较
- MATHWIKI-GS-METHOD-063_交错纠缠级数拆项与条件收敛闭环
- MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线
status: indexed
last_updated: '2026-07-25'
related_wrongnet_refs: []
formal_projection_sha256: 1c16063f241ef1bc0809a17f52e0f3bcaa2647289fcf3cfe4de61b5afa8e7a3e
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-606/question_01.png
solution_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-606/solution_01.png
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

# GS-606 138781 加法项拆等比调和判散

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-606_138781加法项拆等比调和判散.md`
- wrongnet ID：`GS-606`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-606_138781.md`（`VIS-GS-606`）
- 题图 1 张；解析图 1 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、数项级数敛散性判别、收敛级数线性运算、等比级数、调和级数、级数拆项
- 方法：先判型、通项趋零、交错纠缠拆项、拆项判敛散、收敛级数线性运算、等比数列求和、调和级数比较
- 错因字段：触发信息遗漏、通项极限后动作中断、拆项触发不敏感、负底数幂符号处理不熟、级数线性性质表述不严谨
- 第一动作：先把原通项按分子两项拆成 \(\frac{(-2)^{1-n}}{2^n}+\frac1n\)，并化简第一项为 \(\frac{(-1)^{n-1}}{2^{2n-1}}\)
- 个人断点：没有在通项趋零后立刻拆项；对 \((-1)^{1-n}=(-1)^{n-1}\) 的符号等价不够熟；最终“收敛+发散=发散”的线性性质表述略泛化
- 方法卡 ID：H16-001
- 当前强关系：暂无强边

## 证据边界

- 个人错因仅来自正式学习事务中的 wrong_history；视觉资产和客观解析不反推个人错因。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-078_拆项触发不敏感]]
- [[MATHWIKI-ERROR-CLUSTER-414_级数线性性质表述不严谨]]
- [[MATHWIKI-ERROR-CLUSTER-428_负底数幂符号处理不熟]]
- [[MATHWIKI-ERROR-CLUSTER-438_通项极限后动作中断]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-097_调和级数]]
- [[MATHWIKI-KNOWLEDGE-104_等比级数]]
- [[MATHWIKI-KNOWLEDGE-128_级数拆项]]
- [[MATHWIKI-KNOWLEDGE-178_收敛级数线性运算]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-062_通项趋零]]
- [[MATHWIKI-METHOD-CLUSTER-106_交错纠缠拆项]]
- [[MATHWIKI-METHOD-CLUSTER-119_收敛级数线性运算]]
- [[MATHWIKI-METHOD-CLUSTER-156_拆项判敛散]]
- [[MATHWIKI-METHOD-CLUSTER-255_等比数列求和]]
- [[MATHWIKI-METHOD-CLUSTER-460_调和级数比较]]
- [[MATHWIKI-GS-METHOD-063_交错纠缠级数拆项与条件收敛闭环]]
- [[MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
