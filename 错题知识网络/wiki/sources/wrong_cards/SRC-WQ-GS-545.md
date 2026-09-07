---
wiki_id: SRC-WQ-GS-545
type: source_summary
title: GS-545 79077 递推系数幂级数求和
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-545_79077递推系数幂级数求和.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-545_79077,-2026.6.4.md
visual_ids:
- VIS-GS-545
wrongnet_refs:
- GS-545
knowledge:
- 无穷级数
- 幂级数
- 幂级数和函数
- 幂级数逐项求导
- 微分方程法求和函数
- 一阶线性微分方程
- 比值判别法
error_causes:
- 题型识别失败
- 方法选择错误
- 概念混淆
- 动作链断裂
- 重编号未拆首项
- 求和符号内n误提出
- 等式主语混淆
- 微分方程符号错误
- 计算符号错误
methods:
- 先判型
- 比值判别法
- 整体通项比值
- 逐项求导
- 重编号拆首项
- 凑xS'(x)
- 递推式转微分方程
- 一阶线性微分方程
- 积分因子
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-002_B4-CHAIN
- MATHWIKI-ERROR-CLUSTER-001_方法选择错误
- MATHWIKI-ERROR-CLUSTER-003_题型识别失败
- MATHWIKI-ERROR-CLUSTER-004_动作链断裂
- MATHWIKI-ERROR-CLUSTER-006_概念混淆
- MATHWIKI-ERROR-CLUSTER-211_微分方程符号错误
- MATHWIKI-ERROR-CLUSTER-384_求和符号内n误提出
- MATHWIKI-ERROR-CLUSTER-407_等式主语混淆
- MATHWIKI-ERROR-CLUSTER-425_计算符号错误
- MATHWIKI-ERROR-CLUSTER-442_重编号未拆首项
- MATHWIKI-KNOWLEDGE-005_无穷级数
- MATHWIKI-KNOWLEDGE-048_幂级数
- MATHWIKI-KNOWLEDGE-065_一阶线性微分方程
- MATHWIKI-KNOWLEDGE-112_幂级数和函数
- MATHWIKI-KNOWLEDGE-145_幂级数逐项求导
- MATHWIKI-KNOWLEDGE-214_比值判别法
- MATHWIKI-KNOWLEDGE-365_微分方程法求和函数
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-061_积分因子
- MATHWIKI-METHOD-CLUSTER-088_一阶线性微分方程
- MATHWIKI-METHOD-CLUSTER-098_比值判别法
- MATHWIKI-METHOD-CLUSTER-1376_递推式转微分方程
- MATHWIKI-METHOD-CLUSTER-1392_重编号拆首项
- MATHWIKI-METHOD-CLUSTER-233_整体通项比值
- MATHWIKI-METHOD-CLUSTER-464_逐项求导
- MATHWIKI-METHOD-CLUSTER-634_凑xS'-x
- MATHWIKI-GS-ERROR-003_方法选择错误
- MATHWIKI-GS-ERROR-005_题型识别失败
- MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
last_updated: '2026-07-24'
related_wrongnet_refs: []
formal_projection_sha256: 6926cfd5cae27e00c17f476a6d7d3fcccdb8b8abeedae408ff431b4490f2d32d
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-545/question_01.png
solution_asset_refs: []
reference_asset_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: allow
evidence_boundary: 个人错因只来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。
review_batch: MATHWIKI-REVIEW-074
---

# GS-545 79077 递推系数幂级数求和

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-545_79077递推系数幂级数求和.md`
- wrongnet ID：`GS-545`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-545_79077,-2026.6.4.md`（`VIS-GS-545`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、幂级数、幂级数和函数、幂级数逐项求导、微分方程法求和函数、一阶线性微分方程、比值判别法
- 方法：先判型、比值判别法、整体通项比值、逐项求导、重编号拆首项、凑xS'(x)、递推式转微分方程、一阶线性微分方程、积分因子
- 错因字段：题型识别失败、方法选择错误、概念混淆、动作链断裂、重编号未拆首项、求和符号内n误提出、等式主语混淆、微分方程符号错误、计算符号错误
- 第一动作：先逐项求导、乘 x 或移位，把递推关系转成 S 与 S' 的方程
- 个人断点：2026-06-18复发——重编号后忘拆首项a_1；把Σna_nx^n误当nS(x)（应xS'(x)）；等式主语把S'写成S；一阶线性式Q符号写负、∫(1-x)^{-1/2}漏链式负号；解完未立即用S(0)=0定C。
- 方法卡 ID：H16-022
- 当前强关系：暂无强边

## 证据边界

- 个人错因只来自正式卡日期化 `wrong_history`；题图与详情解析只用于核验题面和客观解法。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-211_微分方程符号错误]]
- [[MATHWIKI-ERROR-CLUSTER-384_求和符号内n误提出]]
- [[MATHWIKI-ERROR-CLUSTER-407_等式主语混淆]]
- [[MATHWIKI-ERROR-CLUSTER-425_计算符号错误]]
- [[MATHWIKI-ERROR-CLUSTER-442_重编号未拆首项]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-065_一阶线性微分方程]]
- [[MATHWIKI-KNOWLEDGE-112_幂级数和函数]]
- [[MATHWIKI-KNOWLEDGE-145_幂级数逐项求导]]
- [[MATHWIKI-KNOWLEDGE-214_比值判别法]]
- [[MATHWIKI-KNOWLEDGE-365_微分方程法求和函数]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-061_积分因子]]
- [[MATHWIKI-METHOD-CLUSTER-088_一阶线性微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-098_比值判别法]]
- [[MATHWIKI-METHOD-CLUSTER-1376_递推式转微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-1392_重编号拆首项]]
- [[MATHWIKI-METHOD-CLUSTER-233_整体通项比值]]
- [[MATHWIKI-METHOD-CLUSTER-464_逐项求导]]
- [[MATHWIKI-METHOD-CLUSTER-634_凑xS'-x]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
