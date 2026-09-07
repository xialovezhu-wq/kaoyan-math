---
wiki_id: SRC-WQ-GS-621
type: source_summary
title: "GS-621 57931-1 三角有理式补分子"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-621_57931-1三角有理式补分子.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-621"
knowledge:
  - "不定积分"
  - "一元函数积分学的计算"
  - "三角函数有理式"
  - "三角恒等变形"
  - "恒等式补分子"
  - "三角拆项积分"
  - "第一类换元"
  - "整体凑微分"
error_causes:
  - "三角有理式入口识别不足"
  - "恒等式补分子意识不足"
  - "三角恒等式拆分断点"
  - "凑d(tanx)断点"
  - "凑微分目标不明确"
  - "分子分母翻转风险"
  - "方法论调取失败"
methods:
  - "先判型"
  - "三角函数有理式"
  - "三角恒等变形"
  - "恒等式补分子"
  - "拆项积分"
  - "第一类换元"
  - "凑d(tanx)"
  - "整体凑微分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-041_三角有理式入口识别不足"
  - "MATHWIKI-ERROR-CLUSTER-045_凑微分目标不明确"
  - "MATHWIKI-ERROR-CLUSTER-049_凑d-tanx-断点"
  - "MATHWIKI-ERROR-CLUSTER-065_三角恒等式拆分断点"
  - "MATHWIKI-ERROR-CLUSTER-131_分子分母翻转风险"
  - "MATHWIKI-ERROR-CLUSTER-214_恒等式补分子意识不足"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-043_三角恒等变形"
  - "MATHWIKI-KNOWLEDGE-050_整体凑微分"
  - "MATHWIKI-KNOWLEDGE-079_三角函数有理式"
  - "MATHWIKI-KNOWLEDGE-225_三角拆项积分"
  - "MATHWIKI-KNOWLEDGE-366_恒等式补分子"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-025_三角恒等变形"
  - "MATHWIKI-METHOD-CLUSTER-032_整体凑微分"
  - "MATHWIKI-METHOD-CLUSTER-055_三角函数有理式"
  - "MATHWIKI-METHOD-CLUSTER-1000_恒等式补分子"
  - "MATHWIKI-METHOD-CLUSTER-198_凑d-tanx"
  - "MATHWIKI-METHOD-CLUSTER-230_拆项积分"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-039_不定积分结构化化归入口"
  - "MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-621 57931-1 三角有理式补分子

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-621_57931-1三角有理式补分子.md`
- wrongnet ID：`GS-621`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 三角函数有理式不定积分：恒等式补分子拆项 |
| 日期 | 2026-06-24 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 不定积分
- 一元函数积分学的计算
- 三角函数有理式
- 三角恒等变形
- 恒等式补分子
- 三角拆项积分
- 第一类换元
- 整体凑微分

### 错因

- 三角有理式入口识别不足
- 恒等式补分子意识不足
- 三角恒等式拆分断点
- 凑d(tanx)断点
- 凑微分目标不明确
- 分子分母翻转风险
- 方法论调取失败

### 方法

- 先判型
- 三角函数有理式
- 三角恒等变形
- 恒等式补分子
- 拆项积分
- 第一类换元
- 凑d(tanx)
- 整体凑微分

### 陷阱

- 纯三角分式先看能否用 \(\sin^2x+\cos^2x=1\) 补分子
- 本题把 \(1\) 写成 \((\sin^2x+\cos^2x)^2\)
- 展开后逐项除以 \(\sin^2x\cos^4x\)
- \(\frac{\sin^2x}{\cos^4x}=\tan^2x\sec^2x\)
- \(\frac{2}{\cos^2x}=2\sec^2x\)
- \(\frac{1}{\sin^2x}=\csc^2x\)
- 若改走 \(\sin^2x=1-\cos^2x\)，必须继续转成 \(\tan x,\sec x\) 并凑 \(d(\tan x)\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把分子 \(1\) 写成 \((\sin^2x+\cos^2x)^2\)，再展开并按 \(\sin^2x\cos^4x\) 分项相除。 |
| missed_action | 没有想到补分子；把 \(\sin^2x\) 写成 \(1-\cos^2x\) 后，没有继续转成 \(\tan x,\sec x\) 并拆出 \(\sec^2x\,dx\)。 |
| related_method_card_id | H09-006 |
| next_reminder | 看到纯三角分式题，先问能不能用 \(\sin^2x+\cos^2x=1\) 补分子拆项，再问能不能凑 \(d(\tan x)\) 或 \(d(\cot x)\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-041_三角有理式入口识别不足]]
- [[MATHWIKI-ERROR-CLUSTER-045_凑微分目标不明确]]
- [[MATHWIKI-ERROR-CLUSTER-049_凑d-tanx-断点]]
- [[MATHWIKI-ERROR-CLUSTER-065_三角恒等式拆分断点]]
- [[MATHWIKI-ERROR-CLUSTER-131_分子分母翻转风险]]
- [[MATHWIKI-ERROR-CLUSTER-214_恒等式补分子意识不足]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-043_三角恒等变形]]
- [[MATHWIKI-KNOWLEDGE-050_整体凑微分]]
- [[MATHWIKI-KNOWLEDGE-079_三角函数有理式]]
- [[MATHWIKI-KNOWLEDGE-225_三角拆项积分]]
- [[MATHWIKI-KNOWLEDGE-366_恒等式补分子]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-025_三角恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-032_整体凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-055_三角函数有理式]]
- [[MATHWIKI-METHOD-CLUSTER-1000_恒等式补分子]]
- [[MATHWIKI-METHOD-CLUSTER-198_凑d-tanx]]
- [[MATHWIKI-METHOD-CLUSTER-230_拆项积分]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-600
- GS-603
- GS-619
- GS-622
- GS-623
- GS-624
- GS-625

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
