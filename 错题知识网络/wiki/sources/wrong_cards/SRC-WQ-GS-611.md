---
wiki_id: SRC-WQ-GS-611
type: source_summary
title: GS-611 79147 拆级数几何+积分型求收敛域和函数 2026.6.18
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-611_79147拆级数几何积分型求和.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-611_79147.md
visual_ids:
- VIS-GS-611
wrongnet_refs:
- GS-611
knowledge:
- 无穷级数
- 函数项级数
- 几何级数
- 幂级数
- 幂级数收敛域
- 幂级数和函数
- 幂级数逐项积分
- 先导后积
- 级数收敛必要条件
error_causes:
- 指数不等式方向判反
- 通项趋零检查遗漏
- 收敛域取交集方向错误
- 定积分计算符号不稳
- 端点未单独判断
methods:
- 拆成两个级数分别求收敛域取交集
- 几何级数求和
- 比值判别法
- 端点单独讨论
- 通项趋零判别
- 逐项求导
- 先导后积
- 逐项积分
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-007_B7-CALC
- MATHWIKI-ERROR-CLUSTER-091_端点未单独判断
- MATHWIKI-ERROR-CLUSTER-193_定积分计算符号不稳
- MATHWIKI-ERROR-CLUSTER-218_指数不等式方向判反
- MATHWIKI-ERROR-CLUSTER-234_收敛域取交集方向错误
- MATHWIKI-ERROR-CLUSTER-439_通项趋零检查遗漏
- MATHWIKI-KNOWLEDGE-005_无穷级数
- MATHWIKI-KNOWLEDGE-048_幂级数
- MATHWIKI-KNOWLEDGE-062_级数收敛必要条件
- MATHWIKI-KNOWLEDGE-092_幂级数收敛域
- MATHWIKI-KNOWLEDGE-112_幂级数和函数
- MATHWIKI-KNOWLEDGE-176_幂级数逐项积分
- MATHWIKI-KNOWLEDGE-192_几何级数
- MATHWIKI-KNOWLEDGE-233_先导后积
- MATHWIKI-KNOWLEDGE-307_函数项级数
- MATHWIKI-METHOD-CLUSTER-098_比值判别法
- MATHWIKI-METHOD-CLUSTER-1010_拆成两个级数分别求收敛域取交集
- MATHWIKI-METHOD-CLUSTER-128_端点单独讨论
- MATHWIKI-METHOD-CLUSTER-132_逐项积分
- MATHWIKI-METHOD-CLUSTER-1382_通项趋零判别
- MATHWIKI-METHOD-CLUSTER-195_先导后积
- MATHWIKI-METHOD-CLUSTER-464_逐项求导
- MATHWIKI-METHOD-CLUSTER-641_几何级数求和
- MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线
status: indexed
last_updated: '2026-07-25'
related_wrongnet_refs: []
formal_projection_sha256: fa9cc6b69a247ad8e3da2aae7c4819669ffc8dfb111b714d5c0f6736750d5362
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-611/question_01.png
solution_asset_refs: []
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

# GS-611 79147 拆级数几何+积分型求收敛域和函数 2026.6.18

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-611_79147拆级数几何积分型求和.md`
- wrongnet ID：`GS-611`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-611_79147.md`（`VIS-GS-611`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、函数项级数、几何级数、幂级数、幂级数收敛域、幂级数和函数、幂级数逐项积分、先导后积、级数收敛必要条件
- 方法：拆成两个级数分别求收敛域取交集、几何级数求和、比值判别法、端点单独讨论、通项趋零判别、逐项求导、先导后积、逐项积分
- 错因字段：指数不等式方向判反、通项趋零检查遗漏、收敛域取交集方向错误、定积分计算符号不稳、端点未单独判断
- 第一动作：先把 \(e^{-nx}\) 改写成 \((e^{-x})^n\)，令 \(q=e^{-x}\)，由指数单调递增解 \(|q|<1\Rightarrow e^{-x}<e^0\Rightarrow x>0\)。
- 个人断点：解 \(e^{-x}<1\) 时方向判反成 \(x<0\)；\(x=0\) 处通项 \(=1\) 没用"通项趋零"检查出发散；总收敛域交集方向错；\(\int_0^x-\ln(1-t)\,dt\) 算错符号。
- 方法卡 ID：H16-020
- 当前强关系：暂无强边

## 证据边界

- 个人错因仅来自正式学习事务中的 wrong_history；视觉资产和客观解析不反推个人错因。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-007_B7-CALC]]
- [[MATHWIKI-ERROR-CLUSTER-091_端点未单独判断]]
- [[MATHWIKI-ERROR-CLUSTER-193_定积分计算符号不稳]]
- [[MATHWIKI-ERROR-CLUSTER-218_指数不等式方向判反]]
- [[MATHWIKI-ERROR-CLUSTER-234_收敛域取交集方向错误]]
- [[MATHWIKI-ERROR-CLUSTER-439_通项趋零检查遗漏]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-062_级数收敛必要条件]]
- [[MATHWIKI-KNOWLEDGE-092_幂级数收敛域]]
- [[MATHWIKI-KNOWLEDGE-112_幂级数和函数]]
- [[MATHWIKI-KNOWLEDGE-176_幂级数逐项积分]]
- [[MATHWIKI-KNOWLEDGE-192_几何级数]]
- [[MATHWIKI-KNOWLEDGE-233_先导后积]]
- [[MATHWIKI-KNOWLEDGE-307_函数项级数]]
- [[MATHWIKI-METHOD-CLUSTER-098_比值判别法]]
- [[MATHWIKI-METHOD-CLUSTER-1010_拆成两个级数分别求收敛域取交集]]
- [[MATHWIKI-METHOD-CLUSTER-128_端点单独讨论]]
- [[MATHWIKI-METHOD-CLUSTER-132_逐项积分]]
- [[MATHWIKI-METHOD-CLUSTER-1382_通项趋零判别]]
- [[MATHWIKI-METHOD-CLUSTER-195_先导后积]]
- [[MATHWIKI-METHOD-CLUSTER-464_逐项求导]]
- [[MATHWIKI-METHOD-CLUSTER-641_几何级数求和]]
- [[MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
