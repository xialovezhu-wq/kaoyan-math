---
wiki_id: SRC-WQ-GS-703
type: source_summary
title: GS-703 57708 变限积分分部积分
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-703_57708变限积分分部积分.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-703_57708变限积分分部积分.md
visual_ids:
- VIS-GS-703
wrongnet_refs:
- GS-703
knowledge:
- 定积分
- 分部积分
- 变上限积分
- 幂函数积分
- 复合函数求导
error_causes:
- 积分与求导规则混淆
- 上限代入不完整
- 复合函数计算漏层
- 细节校验缺失
methods:
- 分部积分
- 变上限积分求导
- 凑微分
- 复合上限完整代入
wiki_refs:
- MATHWIKI-COVERAGE-GS
- MATHWIKI-ACTION-GAP-007
- MATHWIKI-GS-TOPIC-006
- MATHWIKI-ERROR-CLUSTER-491
- MATHWIKI-ERROR-CLUSTER-492
- MATHWIKI-ERROR-CLUSTER-493
- MATHWIKI-ERROR-CLUSTER-494
- MATHWIKI-KNOWLEDGE-002
- MATHWIKI-KNOWLEDGE-024
- MATHWIKI-KNOWLEDGE-008
- MATHWIKI-KNOWLEDGE-437
- MATHWIKI-KNOWLEDGE-030
- MATHWIKI-METHOD-CLUSTER-007
- MATHWIKI-METHOD-CLUSTER-015
- MATHWIKI-METHOD-CLUSTER-637
- MATHWIKI-METHOD-CLUSTER-1460
status: indexed
formal_projection_sha256: 96165382afa9f097af5200dfd2e2f771f82747eb3dab38b85d783161e1938586
last_updated: 2026-07-24
related_wrongnet_refs: []
---

# GS-703 57708 变限积分分部积分

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-703_57708变限积分分部积分.md`
- wrongnet ID：`GS-703`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-703_57708变限积分分部积分|VIS-GS-703]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-703_57708%E5%8F%98%E9%99%90%E7%A7%AF%E5%88%86%E5%88%86%E9%83%A8%E7%A7%AF%E5%88%86)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-703/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-703/solution_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 变上限积分函数嵌套定积分 |
| 日期 | 2026-07-18 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 分部积分
- 变上限积分
- 幂函数积分
- 复合函数求导

### 错因

- 积分与求导规则混淆
- 上限代入不完整
- 复合函数计算漏层
- 细节校验缺失

### 方法

- 分部积分
- 变上限积分求导
- 凑微分
- 复合上限完整代入

### 陷阱

- \(\int u^\alpha\,du=\frac{u^{\alpha+1}}{\alpha+1}+C\)，不要把它写成 \((u^\alpha)'\)。
- \(F(x)=\int_1^{x^2}e^{-t^2}\,dt\) 中，先算 \(e^{-(x^2)^2}=e^{-x^4}\)，再乘 \((x^2)'=2x\)。
- 分部积分路线正确不代表后续复合代入可以省略层次。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B7-CALC |
| expected_first_action | 在新变量旁边明写“求原函数”；对 \(F(x)=\int^{g(x)}h(t)\,dt\) 先单独写 \(h(g(x))\)，再乘 \(g'(x)\)。 |
| missed_action | 第一问未做计算方向检查；第二问未先写完整的 \(h(g(x))\)，导致指数少一层平方。 |
| related_method_card_id | H09-008 |
| next_reminder | 看到幂函数凑微分，先确认当前在求导还是积分；看到复合上限，先写完整的 \(h(g(x))\)，再写 \(g'(x)\)；下一次用完整两问连续复做验证稳定性。 |

## 已连接 wiki

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-007_B7-CALC]]
- [[MATHWIKI-ERROR-CLUSTER-491_积分与求导规则混淆]]
- [[MATHWIKI-ERROR-CLUSTER-492_上限代入不完整]]
- [[MATHWIKI-ERROR-CLUSTER-493_复合函数计算漏层]]
- [[MATHWIKI-ERROR-CLUSTER-494_细节校验缺失]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-437_幂函数积分]]
- [[MATHWIKI-KNOWLEDGE-030_复合函数求导]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-015_变上限积分求导]]
- [[MATHWIKI-METHOD-CLUSTER-637_凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-1460_复合上限完整代入]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-006]]

说明：索引型簇页保证本题进入全量知识图谱；深度编译页沉淀可迁移的方法、专题或错因。

## wrongnet 关联题

- 暂无强边

## 下一步

- 复做时先检查 method_gap 中的第一动作，再检查对应错因簇。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
