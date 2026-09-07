---
wiki_id: SRC-WQ-GS-287
type: source_summary
title: GS-287 57742 2026.5.6
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-287_577422026.5.6.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-287_57742-2026.5.6.md
visual_ids:
- VIS-GS-287
wrongnet_refs:
- GS-287
knowledge:
- 定积分
- 变上限积分
- 间断点分类
- 导数定义
- 等价无穷小
- 极限与连续
error_causes:
- 概念边界混淆
- 函数对象混淆
- 分段积分常数错误
methods:
- 分类讨论
- 主导项比较
- 等价变形
- 变上限积分函数性质
- 间断点判定
wiki_refs:
- MATHWIKI-COVERAGE-GS
- MATHWIKI-ACTION-GAP-005
- MATHWIKI-GS-METHOD-098
- MATHWIKI-GS-TOPIC-004
- MATHWIKI-GS-TOPIC-006
- MATHWIKI-ERROR-CLUSTER-027
- MATHWIKI-ERROR-CLUSTER-130
- MATHWIKI-ERROR-CLUSTER-483
- MATHWIKI-KNOWLEDGE-002
- MATHWIKI-KNOWLEDGE-008
- MATHWIKI-KNOWLEDGE-064
- MATHWIKI-KNOWLEDGE-006
- MATHWIKI-KNOWLEDGE-004
- MATHWIKI-KNOWLEDGE-003
- MATHWIKI-METHOD-CLUSTER-004
- MATHWIKI-METHOD-CLUSTER-021
- MATHWIKI-METHOD-CLUSTER-003
- MATHWIKI-METHOD-CLUSTER-801
- MATHWIKI-METHOD-CLUSTER-1399
status: indexed
formal_projection_sha256: 2793eb8fb2dfc739a408aae4a81e892ece3eed6922b7cd3c906fabfacd1027a5
last_updated: 2026-07-24
related_wrongnet_refs: []
---

# GS-287 57742 2026.5.6

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-287_577422026.5.6.md`
- wrongnet ID：`GS-287`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-287_57742-2026.5.6|VIS-GS-287]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-287_57742-2026.5.6)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-287/question_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 极限定义函数与变上限积分可导性 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 变上限积分
- 间断点分类
- 导数定义
- 等价无穷小
- 极限与连续

### 错因

- 概念边界混淆
- 函数对象混淆
- 分段积分常数错误

### 方法

- 分类讨论
- 主导项比较
- 等价变形
- 变上限积分函数性质
- 间断点判定

### 陷阱

- 定义域
- 左右极限
- 参数边界
- 适用条件
- 极限过程
- 量纲/阶数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-CONCEPT |
| expected_first_action | 写出 \(F(0)=\int_{-1}^{0}f(t)\,dt\)，不把 \(f(0)\) 直接代替它。 |
| missed_action | 在已求对 \(f\) 的分段表达后，把被积函数的点值 \(f(0)\) 误作积分函数的点值 \(F(0)\)。 |
| related_method_card_id | H09-008 |
| next_reminder | 看到 \(F(x)=\int_a^x f(t)\,dt\)，先问“我现在求的是 \(f\) 还是 \(F\)”；下一次用整题闭卷复做验证，不因拆分子题答对直接标记掌握。 |

## 已连接 wiki

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-005_A-CONCEPT]]
- [[MATHWIKI-ERROR-CLUSTER-027_概念边界混淆]]
- [[MATHWIKI-ERROR-CLUSTER-130_函数对象混淆]]
- [[MATHWIKI-ERROR-CLUSTER-483_分段积分常数错误]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-064_间断点分类]]
- [[MATHWIKI-KNOWLEDGE-006_导数定义]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-801_变上限积分函数性质]]
- [[MATHWIKI-METHOD-CLUSTER-1399_间断点判定]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-098]]
- [[MATHWIKI-GS-TOPIC-004]]
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
