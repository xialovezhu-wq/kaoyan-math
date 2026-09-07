---
wiki_id: SRC-WQ-GS-576
type: source_summary
title: GS-576 193365 变上限积分微分不等式指数因子
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-576_193365变上限积分微分不等式指数因子.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-576_193365.md
visual_ids:
- VIS-GS-576
wrongnet_refs:
- GS-576
related_wrongnet_refs: []
knowledge:
- 一元函数微分学应用
- 定积分
- 变上限积分
- 单调性与极值
error_causes:
- 方法选择错误
- 概念混淆
- 题型识别失败
methods:
- 先判型
- 变上限积分整体设F
- 变上限积分求导
- 条件转化
- 指数因子辅助函数
- 导数判单调
- 定积分大小比较
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-001_B3-METHOD
- MATHWIKI-ERROR-CLUSTER-001_方法选择错误
- MATHWIKI-ERROR-CLUSTER-003_题型识别失败
- MATHWIKI-ERROR-CLUSTER-006_概念混淆
- MATHWIKI-KNOWLEDGE-001_一元函数微分学应用
- MATHWIKI-KNOWLEDGE-002_定积分
- MATHWIKI-KNOWLEDGE-008_变上限积分
- MATHWIKI-KNOWLEDGE-011_单调性与极值
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-002_条件转化
- MATHWIKI-METHOD-CLUSTER-005_导数判单调
- MATHWIKI-METHOD-CLUSTER-015_变上限积分求导
- MATHWIKI-METHOD-CLUSTER-209_变上限积分整体设F
- MATHWIKI-METHOD-CLUSTER-376_指数因子辅助函数
- MATHWIKI-METHOD-CLUSTER-895_定积分大小比较
- MATHWIKI-GS-ERROR-003_方法选择错误
- MATHWIKI-GS-ERROR-005_题型识别失败
- MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点
- MATHWIKI-GS-METHOD-080_指数因子辅助函数判单调
- MATHWIKI-GS-TOPIC-003_高频知识主线总览
- MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
aggregate_edge_policy: allow
status: indexed
last_updated: '2026-07-24'
formal_projection_sha256: 722020348288b91c1c1b24f9e94e2b76a34563cd00960f965a78b7616460332b
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-576/question_01.png
solution_asset_refs: []
reference_asset_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
evidence_boundary: "个人错因只来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-076
---

# GS-576 193365 变上限积分微分不等式指数因子

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-576_193365变上限积分微分不等式指数因子.md`
- wrongnet ID：`GS-576`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-576_193365.md`（`VIS-GS-576`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：一元函数微分学应用、定积分、变上限积分、单调性与极值
- 方法：先判型、变上限积分整体设F、变上限积分求导、条件转化、指数因子辅助函数、导数判单调、定积分大小比较
- 错因字段：方法选择错误、概念混淆、题型识别失败
- 第一动作：先令 F(x)=∫₀ˣf(t)dt，用 F'=f 把条件改写成 F'>F（不是对不等式两边求导）
- 个人断点：第1次没把变上限积分整体设为 F，把 e⁻ˣ 辅助函数构造在小 f 上；第2次已能推进到 \(F'>F\)，但仍没有把 \(F'-F>0\) 识别为 \((e^{-x}F)'=e^{-x}(F'-F)\) 的触发信号。
- 方法卡 ID：H15-005
- 当前强关系：暂无强边

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-015_变上限积分求导]]
- [[MATHWIKI-METHOD-CLUSTER-209_变上限积分整体设F]]
- [[MATHWIKI-METHOD-CLUSTER-376_指数因子辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-895_定积分大小比较]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-080_指数因子辅助函数判单调]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
