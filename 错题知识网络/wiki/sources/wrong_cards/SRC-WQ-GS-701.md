---
wiki_id: SRC-WQ-GS-701
type: source_summary
title: GS-701 112834 反三角积分分支
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-701_112834反三角积分分支.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-701_112834反三角积分分支.md
visual_ids:
- VIS-GS-701
wrongnet_refs:
- GS-701
knowledge:
- 不定积分
- 反三角函数积分
- 反三角函数主值
- 第二类换元法
- 定义域
error_causes:
- 题干读式错误
- 基本导数混淆
- 绝对值分支遗漏
- 反三角主值混淆
- 推导顺序不严密
methods:
- 倒数换元
- 三角换元
- 定义域分支判定
- 初值定常数
wiki_refs:
- MATHWIKI-COVERAGE-GS
- MATHWIKI-ACTION-GAP-005
- MATHWIKI-GS-METHOD-039
- MATHWIKI-GS-TOPIC-013
- MATHWIKI-SYNTHESIS-001
- MATHWIKI-ERROR-CLUSTER-484
- MATHWIKI-ERROR-CLUSTER-485
- MATHWIKI-ERROR-CLUSTER-486
- MATHWIKI-ERROR-CLUSTER-487
- MATHWIKI-ERROR-CLUSTER-504
- MATHWIKI-KNOWLEDGE-020
- MATHWIKI-KNOWLEDGE-243
- MATHWIKI-KNOWLEDGE-170
- MATHWIKI-KNOWLEDGE-436
- MATHWIKI-KNOWLEDGE-341
- MATHWIKI-METHOD-CLUSTER-1457
- MATHWIKI-METHOD-CLUSTER-028
- MATHWIKI-METHOD-CLUSTER-1458
- MATHWIKI-METHOD-CLUSTER-037
status: indexed
formal_projection_sha256: 5b369b0e1a7b807e113a9cda985ca40c294e0b34556171a49793677aaab36ec0
last_updated: '2026-07-18'
---

# GS-701 112834 反三角积分分支

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-701_112834反三角积分分支.md`
- wrongnet ID：`GS-701`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-701_112834反三角积分分支|VIS-GS-701]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-701_112834%E5%8F%8D%E4%B8%89%E8%A7%92%E7%A7%AF%E5%88%86%E5%88%86%E6%94%AF)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-701/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-701/solution_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 不定积分 |
| 题型 | 给定导函数与初值求曲线方程 |
| 日期 | 2026-07-18 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 不定积分
- 反三角函数积分
- 反三角函数主值
- 第二类换元法
- 定义域

### 错因

- 题干读式错误
- 基本导数混淆
- 绝对值分支遗漏
- 反三角主值混淆
- 推导顺序不严密

### 方法

- 倒数换元
- 三角换元
- 定义域分支判定
- 初值定常数

### 陷阱

- \(\frac1{x\sqrt{x^2-1}}\) 中的 \(x\) 在分母，不是分子。
- \((\sec t)'=\sec t\tan t\)，\((\tan t)'=\sec^2t\)。
- \(x<-1\) 的三角代换中 \(\tan t<0\)，所以 \(\sqrt{\tan^2t}=-\tan t\)。
- \(\arccos\) 的值域是 \([0,\pi]\)，它没有偶性，\(\arccos(-z)=\pi-\arccos z\)。
- 证明 \(\arccos(-\frac12)\) 时从已知 \(\cos\frac\pi3=\frac12\) 出发：\(-\frac12=-\cos\frac\pi3=\cos(\pi-\frac\pi3)\)，不要先使用目标角。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-CONCEPT |
| expected_first_action | 先把斜率逐层写成 \(1\div[x\sqrt{x^2-1}]\)，验证分子分母后再选换元。 |
| missed_action | 正式错误事件中未先核对分式结构；睡前诊断的局部知识已改善，但证明反余弦主值时没有从已知特殊角按诱导公式单向推出，而是提前使用目标角。 |
| related_method_card_id | H09-003 |
| next_reminder | 先核对分子分母和定义域；推主值时从已知特殊角单向写 \(-\cos\alpha=\cos(\pi-\alpha)\)，不得先代入待证角。 |

## 已连接 wiki

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-005_A-CONCEPT]]
- [[MATHWIKI-ERROR-CLUSTER-484_题干读式错误]]
- [[MATHWIKI-ERROR-CLUSTER-485_基本导数混淆]]
- [[MATHWIKI-ERROR-CLUSTER-486_绝对值分支遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-487_反三角主值混淆]]
- [[MATHWIKI-ERROR-CLUSTER-504_推导顺序不严密]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-243_反三角函数积分]]
- [[MATHWIKI-KNOWLEDGE-170_反三角函数主值]]
- [[MATHWIKI-KNOWLEDGE-436_第二类换元法]]
- [[MATHWIKI-KNOWLEDGE-341_定义域]]
- [[MATHWIKI-METHOD-CLUSTER-1457_倒数换元]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-1458_定义域分支判定]]
- [[MATHWIKI-METHOD-CLUSTER-037_初值定常数]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-039]]
- [[MATHWIKI-GS-TOPIC-013]]
- [[MATHWIKI-SYNTHESIS-001]]

说明：索引型簇页保证本题进入全量知识图谱；深度编译页沉淀可迁移的方法、专题或错因。

## wrongnet 关联题

- 暂无正式关系；本次相似关系只写入 SHADOW 提案回执。

## 下一步

- 复做时先检查 method_gap 中的第一动作，再检查对应错因簇。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
