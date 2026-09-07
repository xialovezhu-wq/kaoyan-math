---
wiki_id: SRC-WQ-GS-632
type: source_summary
title: "GS-632 57979-6 平方展开分部抵消"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-632_57979-6平方展开分部抵消.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-632"
knowledge:
  - "不定积分"
  - "一元函数积分学的计算"
  - "三角函数有理式"
  - "三角恒等变形"
  - "三角拆项积分"
  - "第一类换元"
  - "整体凑微分"
  - "分部积分"
error_causes:
  - "触发信息遗漏"
  - "三角恒等式拆分断点"
  - "凑d(tanx)断点"
  - "凑微分目标不明确"
  - "分部积分入口未触发"
  - "动作链断裂"
  - "方法论调取失败"
methods:
  - "先判型"
  - "三角函数有理式"
  - "三角恒等变形"
  - "拆项积分"
  - "第一类换元"
  - "凑d(tanx)"
  - "整体凑微分"
  - "分部积分"
  - "乘积求导逆用"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-045_凑微分目标不明确"
  - "MATHWIKI-ERROR-CLUSTER-049_凑d-tanx-断点"
  - "MATHWIKI-ERROR-CLUSTER-051_分部积分入口未触发"
  - "MATHWIKI-ERROR-CLUSTER-065_三角恒等式拆分断点"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-043_三角恒等变形"
  - "MATHWIKI-KNOWLEDGE-050_整体凑微分"
  - "MATHWIKI-KNOWLEDGE-079_三角函数有理式"
  - "MATHWIKI-KNOWLEDGE-225_三角拆项积分"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-025_三角恒等变形"
  - "MATHWIKI-METHOD-CLUSTER-032_整体凑微分"
  - "MATHWIKI-METHOD-CLUSTER-055_三角函数有理式"
  - "MATHWIKI-METHOD-CLUSTER-198_凑d-tanx"
  - "MATHWIKI-METHOD-CLUSTER-230_拆项积分"
  - "MATHWIKI-METHOD-CLUSTER-279_乘积求导逆用"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-039_不定积分结构化化归入口"
  - "MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-632 57979-6 平方展开分部抵消

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-632_57979-6平方展开分部抵消.md`
- wrongnet ID：`GS-632`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 不定积分：平方项展开 + 线性拆分 + 分部积分抵消 |
| 日期 | 2026-06-27 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 不定积分
- 一元函数积分学的计算
- 三角函数有理式
- 三角恒等变形
- 三角拆项积分
- 第一类换元
- 整体凑微分
- 分部积分

### 错因

- 触发信息遗漏
- 三角恒等式拆分断点
- 凑d(tanx)断点
- 凑微分目标不明确
- 分部积分入口未触发
- 动作链断裂
- 方法论调取失败

### 方法

- 先判型
- 三角函数有理式
- 三角恒等变形
- 拆项积分
- 第一类换元
- 凑d(tanx)
- 整体凑微分
- 分部积分
- 乘积求导逆用

### 陷阱

- 展开平方项后不要停在“看起来不好算”
- \(1+\tan^2x=\sec^2x\)
- \(\sec^2x\,dx=d(\tan x)\)
- 拆成 \(\int e^{2x}\sec^2x\,dx+2\int e^{2x}\tan x\,dx\) 后必须分治
- 第一项按 \(\int e^{2x}\,d(\tan x)\) 分部积分
- 分部后检查是否与剩余项抵消

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先展开 \((1+\tan x)^2\)，并用 \(1+\tan^2x=\sec^2x\) 整理成 \(e^{2x}\sec^2x+2e^{2x}\tan x\)。 |
| missed_action | 没有把整理后的两项拆成两个积分分别处理，也没有继续把 \(\int e^{2x}\sec^2x\,dx\) 写成 \(\int e^{2x}\,d(\tan x)\) 做分部积分观察抵消。 |
| related_method_card_id | H09-005 |
| next_reminder | 看到积分题拆完项后先别停；先把每一项分别问一遍能不能凑微分、分部积分，或者与其他项抵消。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-045_凑微分目标不明确]]
- [[MATHWIKI-ERROR-CLUSTER-049_凑d-tanx-断点]]
- [[MATHWIKI-ERROR-CLUSTER-051_分部积分入口未触发]]
- [[MATHWIKI-ERROR-CLUSTER-065_三角恒等式拆分断点]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-043_三角恒等变形]]
- [[MATHWIKI-KNOWLEDGE-050_整体凑微分]]
- [[MATHWIKI-KNOWLEDGE-079_三角函数有理式]]
- [[MATHWIKI-KNOWLEDGE-225_三角拆项积分]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-025_三角恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-032_整体凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-055_三角函数有理式]]
- [[MATHWIKI-METHOD-CLUSTER-198_凑d-tanx]]
- [[MATHWIKI-METHOD-CLUSTER-230_拆项积分]]
- [[MATHWIKI-METHOD-CLUSTER-279_乘积求导逆用]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-605
- GS-609
- GS-621
- GS-622
- GS-623
- GS-630
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
