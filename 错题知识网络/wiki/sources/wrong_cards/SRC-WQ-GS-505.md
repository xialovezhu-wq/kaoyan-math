---
wiki_id: "SRC-WQ-GS-505"
type: source_summary
title: "GS-505 30185 交错p级数条件收敛范围"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-505_30185交错p级数条件收敛范围.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-505_30185-2026.5.26.md"
visual_ids:
  - "VIS-GS-505"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-505/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-505"
related_wrongnet_refs:
  - "暂无强边"
knowledge:
  - "无穷级数"
  - "数项级数敛散性判别"
  - "任意项级数"
  - "交错级数"
  - "绝对收敛"
  - "条件收敛"
  - "莱布尼茨判别法"
  - "p级数"
  - "参数型p级数"
  - "级数收敛必要条件"
  - "等价通项比较"
  - "等价无穷小"
  - "根式有理化"
error_causes:
  - "条件忽略"
  - "概念混淆"
  - "参数范围错误"
  - "过程跳步"
  - "望远镜级数误触发"
  - "通项趋零充分性误判"
  - "数列与级数术语混淆"
  - "p与alpha端点对应错误"
methods:
  - "先判型"
  - "根式差有理化"
  - "等价通项"
  - "条件转化"
  - "交错级数判别"
  - "p级数判别"
  - "参数范围合并"
  - "通项趋零"
  - "参数边界检查"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002"
  - "MATHWIKI-ERROR-CLUSTER-006"
  - "MATHWIKI-KNOWLEDGE-005"
  - "MATHWIKI-METHOD-CLUSTER-575"
chapter: "无穷级数"
question_type: "含参数交错级数条件收敛范围"
card_status: "待复做"
priority: "A"
evidence_status: "user_confirmed"
status: indexed
last_updated: "2026-08-29"
formal_projection_sha256: "ab748dd4b74ae1fffb3095f15e47d53aee736aa702ef0981ca4752c70d19d46b"
---

# GS-505 30185 交错p级数条件收敛范围

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-505_30185交错p级数条件收敛范围.md`
- wrongnet ID：`GS-505`
- 角色：正式错题卡的轻量可重建投影；本页不替代正式卡，也不保存完整题干或长解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-505_30185-2026.5.26.md|VIS-GS-505]]

## 当前正式投影

- 章节：无穷级数
- 题型：含参数交错级数条件收敛范围
- 知识点：无穷级数；数项级数敛散性判别；任意项级数；交错级数；绝对收敛；条件收敛；莱布尼茨判别法；p级数；参数型p级数；级数收敛必要条件；等价通项比较；等价无穷小；根式有理化
- 方法：先判型；根式差有理化；等价通项；条件转化；交错级数判别；p级数判别；参数范围合并；通项趋零；参数边界检查
- 错因：条件忽略；概念混淆；参数范围错误；过程跳步；望远镜级数误触发；通项趋零充分性误判；数列与级数术语混淆；p与alpha端点对应错误
- 状态：待复做

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写 \(a_n=\frac{\sqrt{n+1}-\sqrt n}{n^p}\sim\frac1{2n^{p+1/2}}\)，令 \(\alpha=p+\frac12\) |
| missed_action | 未先保留交错因子并有理化正项部分；把通项趋零误作充分条件，提示后又把 \(p\) 与 \(\alpha\) 的端点对应说反。 |
| next_reminder | 看到“条件收敛”，先写原级数收敛与绝对值级数发散两条线；有理化后令 \(\alpha=p+\frac12\)，最后单独核对 \(\alpha=0,1\) 对应的两个 \(p\) 端点。 |
| evidence_origin | user_confirmed |
| repeat_count | 3 |

## 证据边界

- 个人错因、复发次数与掌握证据只采用正式卡中的用户作答和确认事实。
- 助手讲解后的理解不计作无提示闭卷掌握；复习状态以正式卡与回滚系统为准。

## 已连接 Wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002]]
- [[MATHWIKI-ERROR-CLUSTER-006]]
- [[MATHWIKI-KNOWLEDGE-005]]
- [[MATHWIKI-METHOD-CLUSTER-575]]

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
