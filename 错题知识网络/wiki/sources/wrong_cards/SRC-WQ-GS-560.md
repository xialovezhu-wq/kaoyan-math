---
wiki_id: SRC-WQ-GS-560
type: source_summary
title: GS-560 138655 根式差式判敛
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-560_138655根式差式判敛.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-560_138655.md
visual_ids:
- VIS-GS-560
wrongnet_refs:
- GS-560
related_wrongnet_refs: []
knowledge:
- 无穷级数
- 数项级数敛散性判别
- 基本展开型f(n)
- 等价无穷小
- 泰勒公式
- p级数
- 参数型级数
error_causes:
- 方法选择错误
- 过程跳步
- 计算失误
- 同项抵消与跨项裂项混淆
- 共轭公式适用判断错误
- 主项比较整体路线未建立
- 小o量级与级数收敛关系未厘清
methods:
- 先判型
- 基本展开型f(n)
- 指数对数互化
- 泰勒展开
- 二项式展开
- 首个非零主项
- p级数判别
- 参数分类
wiki_refs:
- MATHWIKI-ACTION-GAP-003
- MATHWIKI-ERROR-CLUSTER-001
- MATHWIKI-ERROR-CLUSTER-002
- MATHWIKI-ERROR-CLUSTER-014
- MATHWIKI-ERROR-CLUSTER-036
- MATHWIKI-KNOWLEDGE-004
- MATHWIKI-KNOWLEDGE-005
- MATHWIKI-KNOWLEDGE-013
- MATHWIKI-KNOWLEDGE-015
- MATHWIKI-KNOWLEDGE-036
- MATHWIKI-KNOWLEDGE-172
- MATHWIKI-KNOWLEDGE-319
- MATHWIKI-METHOD-CLUSTER-001
- MATHWIKI-METHOD-CLUSTER-008
- MATHWIKI-METHOD-CLUSTER-027
- MATHWIKI-METHOD-CLUSTER-115
- MATHWIKI-METHOD-CLUSTER-139
- MATHWIKI-METHOD-CLUSTER-146
- MATHWIKI-METHOD-CLUSTER-159
- MATHWIKI-METHOD-CLUSTER-267
status: indexed
last_updated: '2026-09-02'
formal_projection_sha256: 397f920467bc1332c9190f92daf601a40c5d7700432d47161b0c9ff62a77b534
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-560/question_01.png
solution_asset_refs: []
reference_asset_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: allow
evidence_boundary: 个人错因只来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。
review_batch: MATHWIKI-REVIEW-076
---

# GS-560 138655 根式差式判敛

## 题目定位

参数型基本展开差式判敛。

## 当前错因

把同一通项中两项展开后的相消误解为前后求和项裂项相消，也误以为指数不同不能使用共轭；没有从两项同趋1建立先检查通项、再找抵消后首个非零主项并分类比较的路线。提示后一阶展开能复述，但仍需解释一阶相消后仅剩o(1/n)不能直接判收敛。

## 独立步骤与提示依赖

调度评分3/5；指数与二项式模板的一阶代入是在讲解后正确复述。用户主动质疑仅凭o(1/n)能否判收敛，该疑问合理；二阶展开、临界参数与极限比较完整结论由助手给出，未见独立全解。

## 下次复做动作

先写a^(1/n)=exp((ln a)/n)，把两项按同一小量1/n展开并保留余项。

## 来源

- [[错题知识网络/错题卡/GS-560_138655根式差式判敛|GS-560 正式卡与完整历史]]

## 知识簇

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-ERROR-CLUSTER-036_参数范围错误]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-KNOWLEDGE-036_p级数]]
- [[MATHWIKI-KNOWLEDGE-172_基本展开型f(n)]]
- [[MATHWIKI-KNOWLEDGE-319_参数型级数]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-027_p级数判别]]
- [[MATHWIKI-METHOD-CLUSTER-115_基本展开型f-n]]
- [[MATHWIKI-METHOD-CLUSTER-139_二项式展开]]
- [[MATHWIKI-METHOD-CLUSTER-146_参数分类]]
- [[MATHWIKI-METHOD-CLUSTER-159_指数对数互化]]
- [[MATHWIKI-METHOD-CLUSTER-267_首个非零主项]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
