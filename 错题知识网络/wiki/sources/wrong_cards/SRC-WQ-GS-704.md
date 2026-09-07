---
wiki_id: SRC-WQ-GS-704
type: source_summary
title: GS-704 57870 反正弦复合分部积分
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-704_57870反正弦复合分部积分.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-704_57870反正弦复合分部积分.md
visual_ids:
- VIS-GS-704
wrongnet_refs:
- GS-704
knowledge:
- 不定积分
- 分部积分
- 反三角函数求导
- 复合函数求导
- 链式法则
error_causes:
- 分部积分调取失败
- 反三角导数遗忘
- 内函数导数漏乘
- 函数类型口述混淆
- 被积表达式读式错误
methods:
- 函数关系换元
- 凑微分
- 分部积分
- 复合函数链式求导
wiki_refs:
- MATHWIKI-COVERAGE-GS
- MATHWIKI-ACTION-GAP-001
- MATHWIKI-GS-METHOD-039
- MATHWIKI-GS-TOPIC-013
- MATHWIKI-ERROR-CLUSTER-495
- MATHWIKI-ERROR-CLUSTER-496
- MATHWIKI-ERROR-CLUSTER-497
- MATHWIKI-ERROR-CLUSTER-498
- MATHWIKI-ERROR-CLUSTER-507
- MATHWIKI-KNOWLEDGE-020
- MATHWIKI-KNOWLEDGE-024
- MATHWIKI-KNOWLEDGE-242
- MATHWIKI-KNOWLEDGE-030
- MATHWIKI-KNOWLEDGE-131
- MATHWIKI-METHOD-CLUSTER-1461
- MATHWIKI-METHOD-CLUSTER-637
- MATHWIKI-METHOD-CLUSTER-007
- MATHWIKI-METHOD-CLUSTER-1462
status: indexed
formal_projection_sha256: cbfec490ff76d8df159f70f3e383b1e292d6f2abdf7e80f758ffda7a755083d3
last_updated: '2026-07-18'
---

# GS-704 57870 反正弦复合分部积分

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-704_57870反正弦复合分部积分.md`
- wrongnet ID：`GS-704`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-704_57870反正弦复合分部积分|VIS-GS-704]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-704_57870%E5%8F%8D%E6%AD%A3%E5%BC%A6%E5%A4%8D%E5%90%88%E5%88%86%E9%83%A8%E7%A7%AF%E5%88%86)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-704/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-704/solution_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 不定积分 |
| 题型 | 函数关系求函数与反三角复合积分 |
| 日期 | 2026-07-18 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 不定积分
- 分部积分
- 反三角函数求导
- 复合函数求导
- 链式法则

### 错因

- 分部积分调取失败
- 反三角导数遗忘
- 内函数导数漏乘
- 函数类型口述混淆
- 被积表达式读式错误

### 方法

- 函数关系换元
- 凑微分
- 分部积分
- 复合函数链式求导

### 陷阱

- 由 \(\sin^2x=t\) 取 \(x=\arcsin\sqrt t\) 时，必须结合定义域确认 \(\sin x>0\)。
- \(\frac{dx}{\sqrt{1-x}}=-2\,d\sqrt{1-x}\)，这是分部积分的直接触发信号。
- \((\arcsin\sqrt x)'=\frac1{2\sqrt x\sqrt{1-x}}\)，不能漏掉 \((\sqrt x)'\)。
- 题中是 \(\arcsin\)，不是 \(\arccos\)；两者导数符号不同。
- \(\frac{dx}{\sqrt{1-x}}\) 的根式在分母，不能改写成 \(\sqrt{1-x}\,dx\)；应写成 \(-2\,d\sqrt{1-x}\)。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 \(\frac{dx}{\sqrt{1-x}}=-2\,d\sqrt{1-x}\)，然后设 \(u=\arcsin\sqrt x\)、\(dv=dx/\sqrt{1-x}\)。 |
| missed_action | 睡前诊断再次未先核对根式在分母，先把被积表达式读错；纠正后才写出 \(u=\arcsin\sqrt x\)、\(dv=d\sqrt{1-x}\) 的分部积分角色。 |
| related_method_card_id | H09-005 |
| next_reminder | 动笔前先用括号重写 \(\arcsin\sqrt x\cdot[dx/\sqrt{1-x}]\)，确认根式在分母；再凑 \(-2d\sqrt{1-x}\)，复合求导显式写内函数导数。 |

## 已连接 wiki

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-495_分部积分调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-496_反三角导数遗忘]]
- [[MATHWIKI-ERROR-CLUSTER-497_内函数导数漏乘]]
- [[MATHWIKI-ERROR-CLUSTER-498_函数类型口述混淆]]
- [[MATHWIKI-ERROR-CLUSTER-507_被积表达式读式错误]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-242_反三角函数求导]]
- [[MATHWIKI-KNOWLEDGE-030_复合函数求导]]
- [[MATHWIKI-KNOWLEDGE-131_链式法则]]
- [[MATHWIKI-METHOD-CLUSTER-1461_函数关系换元]]
- [[MATHWIKI-METHOD-CLUSTER-637_凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-1462_复合函数链式求导]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-039]]
- [[MATHWIKI-GS-TOPIC-013]]

说明：索引型簇页保证本题进入全量知识图谱；深度编译页沉淀可迁移的方法、专题或错因。

## wrongnet 关联题

- 暂无正式关系；本次相似关系只写入 SHADOW 提案回执。

## 下一步

- 复做时先检查 method_gap 中的第一动作，再检查对应错因簇。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
