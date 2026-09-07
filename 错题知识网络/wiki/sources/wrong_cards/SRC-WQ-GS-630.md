---
wiki_id: SRC-WQ-GS-630
type: source_summary
title: "GS-630 57979-3 分母平方凑微分分部"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-630_57979-3分母平方凑微分分部.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-630"
knowledge:
  - "不定积分"
  - "一元函数积分学的计算"
  - "分部积分"
  - "第一类换元"
  - "整体凑微分"
  - "分母平方凑微分"
  - "分部积分降幂"
error_causes:
  - "题型识别断点"
  - "触发信息遗漏"
  - "结构观察断点"
  - "分子求导检查遗漏"
  - "分部积分入口未触发"
  - "分部积分降幂意识不足"
  - "凑微分目标不明确"
methods:
  - "先判型"
  - "分子求导检查"
  - "第一类换元"
  - "整体凑微分"
  - "分部积分"
  - "分部积分降幂"
  - "二次分部积分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-040_题型识别断点"
  - "MATHWIKI-ERROR-CLUSTER-045_凑微分目标不明确"
  - "MATHWIKI-ERROR-CLUSTER-051_分部积分入口未触发"
  - "MATHWIKI-ERROR-CLUSTER-069_分部积分降幂意识不足"
  - "MATHWIKI-ERROR-CLUSTER-133_分子求导检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-416_结构观察断点"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-050_整体凑微分"
  - "MATHWIKI-KNOWLEDGE-196_分部积分降幂"
  - "MATHWIKI-KNOWLEDGE-236_分母平方凑微分"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-032_整体凑微分"
  - "MATHWIKI-METHOD-CLUSTER-315_分部积分降幂"
  - "MATHWIKI-METHOD-CLUSTER-550_二次分部积分"
  - "MATHWIKI-METHOD-CLUSTER-666_分子求导检查"
  - "MATHWIKI-GS-METHOD-039_不定积分结构化化归入口"
  - "MATHWIKI-GS-METHOD-076_分式积分拆到底与分母降幂链"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-630 57979-3 分母平方凑微分分部

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-630_57979-3分母平方凑微分分部.md`
- wrongnet ID：`GS-630`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 不定积分：分母平方凑微分 + 分部积分降分母幂次 |
| 日期 | 2026-06-26 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 不定积分
- 一元函数积分学的计算
- 分部积分
- 第一类换元
- 整体凑微分
- 分母平方凑微分
- 分部积分降幂

### 错因

- 题型识别断点
- 触发信息遗漏
- 结构观察断点
- 分子求导检查遗漏
- 分部积分入口未触发
- 分部积分降幂意识不足
- 凑微分目标不明确

### 方法

- 先判型
- 分子求导检查
- 第一类换元
- 整体凑微分
- 分部积分
- 分部积分降幂
- 二次分部积分

### 陷阱

- \(F(x)/(x+a)^2\) 先别展开分母
- 先检查 \(F'(x)\) 是否含有 \((x+a)\) 因子
- \(\frac{dx}{(x+a)^2}=-d(\frac1{x+a})\)
- 分部积分的目标是让分母平方降成一次
- \((x^2e^x)'=x(x+2)e^x\)
- 后续 \(\int xe^x dx\) 还要再分部

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先计算 \((x^2e^x)'\)，观察结果是否含有 \((x+2)\)。 |
| missed_action | 没有先检查分子求导后的结构，导致没发现分部积分后可以约掉一个 \((x+2)\)。 |
| related_method_card_id | H09-005 |
| next_reminder | 看到 \(F(x)/(x+a)^2\)，先别展开分母，先看 \(F'(x)\) 是否含有 \((x+a)\) 因子；若有，就把 \(\frac{dx}{(x+a)^2}\) 凑成 \(-d(\frac1{x+a})\) 并分部积分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-040_题型识别断点]]
- [[MATHWIKI-ERROR-CLUSTER-045_凑微分目标不明确]]
- [[MATHWIKI-ERROR-CLUSTER-051_分部积分入口未触发]]
- [[MATHWIKI-ERROR-CLUSTER-069_分部积分降幂意识不足]]
- [[MATHWIKI-ERROR-CLUSTER-133_分子求导检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-416_结构观察断点]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-050_整体凑微分]]
- [[MATHWIKI-KNOWLEDGE-196_分部积分降幂]]
- [[MATHWIKI-KNOWLEDGE-236_分母平方凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-032_整体凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-315_分部积分降幂]]
- [[MATHWIKI-METHOD-CLUSTER-550_二次分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-666_分子求导检查]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-METHOD-076_分式积分拆到底与分母降幂链]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-609
- GS-605
- GS-610
- GS-620
- GS-623
- GS-622

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
