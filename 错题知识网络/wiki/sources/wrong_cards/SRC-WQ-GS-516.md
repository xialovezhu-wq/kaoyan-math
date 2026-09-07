---
wiki_id: SRC-WQ-GS-516
type: source_summary
title: "GS-516 79209 含参正项级数收敛域 2026.5.30"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-516_79209含参正项级数收敛域.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-516_79209-2026.5.30.md"
visual_ids:
  - "VIS-GS-516"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-516/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-516"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "正项级数敛散性判别"
  - "比值判别法"
  - "函数项级数收敛域"
  - "幂指极限"
  - "级数收敛必要条件"
error_causes:
  - "概念混淆"
  - "复习记忆不牢"
methods:
  - "先判型"
  - "比值判别法"
  - "重要极限"
  - "级数必要条件判端点"
  - "分类讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-017_复习记忆不牢"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-017_幂指极限"
  - "MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-062_级数收敛必要条件"
  - "MATHWIKI-KNOWLEDGE-214_比值判别法"
  - "MATHWIKI-KNOWLEDGE-308_函数项级数收敛域"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-098_比值判别法"
  - "MATHWIKI-METHOD-CLUSTER-1300_级数必要条件判端点"
  - "MATHWIKI-METHOD-CLUSTER-134_重要极限"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-070
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 74fd7bbb0313c065614abbf4fb9122e15f0397b7e5bc345de76f215ad0b9902c
---

# GS-516 79209 含参正项级数收敛域 2026.5.30

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-516_79209含参正项级数收敛域.md`
- wrongnet ID：`GS-516`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-516_79209-2026.5.30.md`（`VIS-GS-516`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 含参正项级数收敛域（比值审敛法） |
| 日期 | 2026-05-30 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 无穷级数
- 正项级数敛散性判别
- 比值判别法
- 函数项级数收敛域
- 幂指极限
- 级数收敛必要条件

### 错因

- 概念混淆
- 复习记忆不牢

### 方法

- 先判型
- 比值判别法
- 重要极限
- 级数必要条件判端点
- 分类讨论

### 陷阱

- 1^∞型不能直接代极限
- ρ=1时比值法失效需单独判端点
- 适用条件

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先算 \(\frac{u_{n+1}}{u_n}=e^{-x}\left(\frac{n}{n+1}\right)^n\)，再把 \(\left(\frac{n}{n+1}\right)^n=(1+\frac1n)^{-n}\to e^{-1}\)。 |
| missed_action | 把 \(\left(\frac{n}{n+1}\right)^n\) 当成普通极限 1，漏掉 \(1^\infty\) 的重要极限。 |
| related_method_card_id | H16-001 |
| next_reminder | 比值判别中看到 \((n/(n+1))^n\)、\((1+1/n)^n\) 这类因子，先按重要极限处理；\(\rho=1\) 的端点必须代回原级数。 |
| evidence_origin | user_confirmed |
| repeat_count | 1 |
| repeat_count_source | wrong_history |

## 证据边界

- 个人错因仅来自正式卡 dated `wrong_history`；详情解析只核验题面与解法，不反推个人错因。
- 题图或解析图存在，只证明视觉来源已注册，不单独证明个人作答过程、错误次数或掌握度。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-017_复习记忆不牢]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-017_幂指极限]]
- [[MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-062_级数收敛必要条件]]
- [[MATHWIKI-KNOWLEDGE-214_比值判别法]]
- [[MATHWIKI-KNOWLEDGE-308_函数项级数收敛域]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-098_比值判别法]]
- [[MATHWIKI-METHOD-CLUSTER-1300_级数必要条件判端点]]
- [[MATHWIKI-METHOD-CLUSTER-134_重要极限]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
