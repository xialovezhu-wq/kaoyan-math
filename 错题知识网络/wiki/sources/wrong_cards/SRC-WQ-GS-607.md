---
wiki_id: SRC-WQ-GS-607
type: source_summary
title: GS-607 138782 交错有理因子拆主余项
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-607_138782交错有理因子拆主余项.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-607_138782.md
visual_ids:
- VIS-GS-607
wrongnet_refs:
- GS-607
knowledge:
- 无穷级数
- 数项级数敛散性判别
- 交错级数
- 莱布尼茨判别法
- 条件收敛
- 绝对收敛
- p级数
- 级数拆项
- 极限比较判别法
- 收敛级数线性运算
error_causes:
- 触发信息遗漏
- 拆项触发不敏感
- 有理因子恒等变形未触发
- 交错纠缠项处理不熟
- 条件收敛与绝对收敛结论表述不严谨
methods:
- 先判型
- 通项趋零
- 通项恒等变形
- 交错纠缠拆项
- 拆项判敛散
- 莱布尼茨判别法
- 取绝对值
- 极限比较判别法
- 收敛级数线性运算
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-003
- MATHWIKI-ERROR-CLUSTER-008
- MATHWIKI-ERROR-CLUSTER-078
- MATHWIKI-ERROR-CLUSTER-114
- MATHWIKI-ERROR-CLUSTER-363
- MATHWIKI-ERROR-CLUSTER-366
- MATHWIKI-KNOWLEDGE-005
- MATHWIKI-KNOWLEDGE-013
- MATHWIKI-KNOWLEDGE-036
- MATHWIKI-KNOWLEDGE-059
- MATHWIKI-KNOWLEDGE-061
- MATHWIKI-KNOWLEDGE-074
- MATHWIKI-KNOWLEDGE-075
- MATHWIKI-KNOWLEDGE-095
- MATHWIKI-KNOWLEDGE-128
- MATHWIKI-KNOWLEDGE-178
- MATHWIKI-METHOD-CLUSTER-001
- MATHWIKI-METHOD-CLUSTER-030
- MATHWIKI-METHOD-CLUSTER-033
- MATHWIKI-METHOD-CLUSTER-053
- MATHWIKI-METHOD-CLUSTER-062
- MATHWIKI-METHOD-CLUSTER-106
- MATHWIKI-METHOD-CLUSTER-119
- MATHWIKI-METHOD-CLUSTER-156
- MATHWIKI-METHOD-CLUSTER-181
- MATHWIKI-GS-METHOD-063_交错纠缠级数拆项与条件收敛闭环
- MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线
status: indexed
last_updated: '2026-09-01'
related_wrongnet_refs: []
formal_projection_sha256: ceac3d41a3365e82369c7ff502e745dd0f65c87be5f74c4ea3d00a536c09010e
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-607/question_01.png
solution_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-607/solution_01.png
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

# GS-607 138782 交错有理因子拆主余项

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-607_138782交错有理因子拆主余项.md`
- wrongnet ID：`GS-607`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-607_138782.md`（`VIS-GS-607`）
- 题图 1 张；解析图 1 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、数项级数敛散性判别、交错级数、莱布尼茨判别法、条件收敛、绝对收敛、p级数、级数拆项、极限比较判别法、收敛级数线性运算
- 方法：先判型、通项趋零、通项恒等变形、交错纠缠拆项、拆项判敛散、莱布尼茨判别法、取绝对值、极限比较判别法、收敛级数线性运算
- 错因字段：触发信息遗漏、拆项触发不敏感、有理因子恒等变形未触发、交错纠缠项处理不熟、条件收敛与绝对收敛结论表述不严谨
- 第一动作：先把 \(n-1\) 写成 \((n+1)-2\)，即 \(\frac{n-1}{n+1}=1-\frac2{n+1}\)
- 个人断点：没有主动凑 \((n+1)-2\) 做恒等变形拆项；最后“条件收敛+绝对收敛=条件收敛”结论缺严谨证明
- 方法卡 ID：H16-016
- 当前强关系：暂无强边

## 证据边界

- 个人错因仅来自正式学习事务中的 wrong_history；视觉资产和客观解析不反推个人错因。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-078_拆项触发不敏感]]
- [[MATHWIKI-ERROR-CLUSTER-114_交错纠缠项处理不熟]]
- [[MATHWIKI-ERROR-CLUSTER-363_有理因子恒等变形未触发]]
- [[MATHWIKI-ERROR-CLUSTER-366_条件收敛与绝对收敛结论表述不严谨]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-036_p级数]]
- [[MATHWIKI-KNOWLEDGE-059_交错级数]]
- [[MATHWIKI-KNOWLEDGE-061_极限比较判别法]]
- [[MATHWIKI-KNOWLEDGE-074_绝对收敛]]
- [[MATHWIKI-KNOWLEDGE-075_莱布尼茨判别法]]
- [[MATHWIKI-KNOWLEDGE-095_条件收敛]]
- [[MATHWIKI-KNOWLEDGE-128_级数拆项]]
- [[MATHWIKI-KNOWLEDGE-178_收敛级数线性运算]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-030_取绝对值]]
- [[MATHWIKI-METHOD-CLUSTER-033_极限比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-053_莱布尼茨判别法]]
- [[MATHWIKI-METHOD-CLUSTER-062_通项趋零]]
- [[MATHWIKI-METHOD-CLUSTER-106_交错纠缠拆项]]
- [[MATHWIKI-METHOD-CLUSTER-119_收敛级数线性运算]]
- [[MATHWIKI-METHOD-CLUSTER-156_拆项判敛散]]
- [[MATHWIKI-METHOD-CLUSTER-181_通项恒等变形]]
- [[MATHWIKI-GS-METHOD-063_交错纠缠级数拆项与条件收敛闭环]]
- [[MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
