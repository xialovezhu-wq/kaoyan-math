---
wiki_id: SRC-WQ-GS-162
type: source_summary
title: "GS-162 强化例题9.11（135747）三角有理式换元"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-162_强化例题9.11（135747）.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-162"
knowledge:
  - "不定积分"
  - "一元函数积分学的计算"
  - "三角函数有理式"
  - "三角恒等变形"
  - "第一类换元"
  - "整体凑微分"
  - "有理函数积分"
  - "部分分式"
  - "对数型积分"
error_causes:
  - "三角恒等式使用断点"
  - "公式记错"
  - "凑微分识别不足"
  - "换元后dx处理不完整"
  - "部分分式规则断点"
  - "计算失误"
methods:
  - "先判型"
  - "三角函数有理式"
  - "三角恒等变形"
  - "第一类换元"
  - "整体凑微分"
  - "有理函数积分"
  - "部分分式"
  - "对数型积分"
  - "回代化简"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-007_B7-CALC"
  - "MATHWIKI-ERROR-CLUSTER-014_计算失误"
  - "MATHWIKI-ERROR-CLUSTER-015_公式记错"
  - "MATHWIKI-ERROR-CLUSTER-056_换元后dx处理不完整"
  - "MATHWIKI-ERROR-CLUSTER-064_三角恒等式使用断点"
  - "MATHWIKI-ERROR-CLUSTER-067_凑微分识别不足"
  - "MATHWIKI-ERROR-CLUSTER-096_部分分式规则断点"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-043_三角恒等变形"
  - "MATHWIKI-KNOWLEDGE-044_有理函数积分"
  - "MATHWIKI-KNOWLEDGE-046_部分分式"
  - "MATHWIKI-KNOWLEDGE-050_整体凑微分"
  - "MATHWIKI-KNOWLEDGE-057_对数型积分"
  - "MATHWIKI-KNOWLEDGE-079_三角函数有理式"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-025_三角恒等变形"
  - "MATHWIKI-METHOD-CLUSTER-032_整体凑微分"
  - "MATHWIKI-METHOD-CLUSTER-035_部分分式"
  - "MATHWIKI-METHOD-CLUSTER-055_三角函数有理式"
  - "MATHWIKI-METHOD-CLUSTER-070_回代化简"
  - "MATHWIKI-METHOD-CLUSTER-072_有理函数积分"
  - "MATHWIKI-METHOD-CLUSTER-354_对数型积分"
  - "MATHWIKI-GS-METHOD-039_不定积分结构化化归入口"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-162 强化例题9.11（135747）三角有理式换元

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-162_强化例题9.11（135747）.md`
- wrongnet ID：`GS-162`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 三角有理式不定积分：凑微分转有理函数积分 |
| 日期 | 2026-06-28 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 不定积分
- 一元函数积分学的计算
- 三角函数有理式
- 三角恒等变形
- 第一类换元
- 整体凑微分
- 有理函数积分
- 部分分式
- 对数型积分

### 错因

- 三角恒等式使用断点
- 公式记错
- 凑微分识别不足
- 换元后dx处理不完整
- 部分分式规则断点
- 计算失误

### 方法

- 先判型
- 三角函数有理式
- 三角恒等变形
- 第一类换元
- 整体凑微分
- 有理函数积分
- 部分分式
- 对数型积分
- 回代化简

### 陷阱

- \(1+\sin^2x\) 不能化成 \(\cos^2x\)
- 只有 \(1-\sin^2x=\cos^2x\)
- 凑出 \(\sin x\,dx=-d(\cos x)\) 后，要把所有 \(\sin^2x\) 统一换成 \(1-\cos^2x\)
- \(\frac{1}{(1-t^2)(2-t^2)}=\frac{1}{1-t^2}-\frac{1}{2-t^2}\)
- \(\int\frac{dt}{2-t^2}\) 中 \(a=\sqrt2\)，不是 \(2\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B7-CALC |
| expected_first_action | 先写成 \(\frac{1}{\sin x(1+\sin^2x)}\)，再乘 \(\frac{\sin x}{\sin x}\)，凑 \(\sin x\,dx=-d(\cos x)\)。 |
| missed_action | 把 \(1+\sin^2x\) 误写成 \(\cos^2x\)；后续在 \(\int dx/(a^2-x^2)\) 公式中把 \(a\) 与 \(\sqrt a\) 混淆。 |
| related_method_card_id | H09-006 |
| next_reminder | 看到 \(1+\sin^2x\)，先查正负号：只有 \(1-\sin^2x=\cos^2x\)；公式里 \(a^2-x^2\) 的 \(a\) 是开根号后的数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-007_B7-CALC]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-ERROR-CLUSTER-015_公式记错]]
- [[MATHWIKI-ERROR-CLUSTER-056_换元后dx处理不完整]]
- [[MATHWIKI-ERROR-CLUSTER-064_三角恒等式使用断点]]
- [[MATHWIKI-ERROR-CLUSTER-067_凑微分识别不足]]
- [[MATHWIKI-ERROR-CLUSTER-096_部分分式规则断点]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-043_三角恒等变形]]
- [[MATHWIKI-KNOWLEDGE-044_有理函数积分]]
- [[MATHWIKI-KNOWLEDGE-046_部分分式]]
- [[MATHWIKI-KNOWLEDGE-050_整体凑微分]]
- [[MATHWIKI-KNOWLEDGE-057_对数型积分]]
- [[MATHWIKI-KNOWLEDGE-079_三角函数有理式]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-025_三角恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-032_整体凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-035_部分分式]]
- [[MATHWIKI-METHOD-CLUSTER-055_三角函数有理式]]
- [[MATHWIKI-METHOD-CLUSTER-070_回代化简]]
- [[MATHWIKI-METHOD-CLUSTER-072_有理函数积分]]
- [[MATHWIKI-METHOD-CLUSTER-354_对数型积分]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-280
- GS-623
- GS-624
- GS-621
- GS-604
- GS-631

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
