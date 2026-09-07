---
wiki_id: SRC-WQ-GS-624
type: source_summary
title: "GS-624 57931-5 倍角半角万能代换"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-624_57931-5倍角半角万能代换.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-624"
knowledge:
  - "不定积分"
  - "一元函数积分学的计算"
  - "三角函数有理式"
  - "三角恒等变形"
  - "二倍角公式"
  - "半角公式"
  - "万能代换"
  - "第一类换元"
  - "整体凑微分"
error_causes:
  - "三角有理式入口识别不足"
  - "倍角公式触发失败"
  - "半角公式触发失败"
  - "万能代换意识不足"
  - "动作链断裂"
  - "分式拆分误区"
  - "方法论调取失败"
methods:
  - "先判型"
  - "三角函数有理式"
  - "三角恒等变形"
  - "二倍角公式"
  - "半角公式"
  - "万能代换"
  - "第一类换元"
  - "凑d(tan(x/2))"
  - "整体凑微分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-041_三角有理式入口识别不足"
  - "MATHWIKI-ERROR-CLUSTER-070_半角公式触发失败"
  - "MATHWIKI-ERROR-CLUSTER-099_万能代换意识不足"
  - "MATHWIKI-ERROR-CLUSTER-117_倍角公式触发失败"
  - "MATHWIKI-ERROR-CLUSTER-137_分式拆分误区"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-043_三角恒等变形"
  - "MATHWIKI-KNOWLEDGE-050_整体凑微分"
  - "MATHWIKI-KNOWLEDGE-079_三角函数有理式"
  - "MATHWIKI-KNOWLEDGE-197_半角公式"
  - "MATHWIKI-KNOWLEDGE-223_万能代换"
  - "MATHWIKI-KNOWLEDGE-229_二倍角公式"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-025_三角恒等变形"
  - "MATHWIKI-METHOD-CLUSTER-032_整体凑微分"
  - "MATHWIKI-METHOD-CLUSTER-055_三角函数有理式"
  - "MATHWIKI-METHOD-CLUSTER-188_二倍角公式"
  - "MATHWIKI-METHOD-CLUSTER-203_半角公式"
  - "MATHWIKI-METHOD-CLUSTER-272_万能代换"
  - "MATHWIKI-METHOD-CLUSTER-298_凑d-tan-x-2"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-039_不定积分结构化化归入口"
  - "MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-624 57931-5 倍角半角万能代换

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-624_57931-5倍角半角万能代换.md`
- wrongnet ID：`GS-624`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 三角函数有理式不定积分：倍角化简 + 半角公式 + 万能代换 |
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
- 二倍角公式
- 半角公式
- 万能代换
- 第一类换元
- 整体凑微分

### 错因

- 三角有理式入口识别不足
- 倍角公式触发失败
- 半角公式触发失败
- 万能代换意识不足
- 动作链断裂
- 分式拆分误区
- 方法论调取失败

### 方法

- 先判型
- 三角函数有理式
- 三角恒等变形
- 二倍角公式
- 半角公式
- 万能代换
- 第一类换元
- 凑d(tan(x/2))
- 整体凑微分

### 陷阱

- 先把 \(\sin2x\) 写成 \(2\sin x\cos x\)
- \(\sin2x+2\sin x=2\sin x(1+\cos x)\)
- 出现 \(1+\cos x\) 后优先想到 \(1+\cos x=2\cos^2\frac{x}{2}\)
- \(\sin x=2\sin\frac{x}{2}\cos\frac{x}{2}\)
- \(t=\tan\frac{x}{2}\) 时 \(dx=\frac{2}{1+t^2}dt\)
- 不能把 \(\frac{1}{2\sin x(1+\cos x)}\) 拆成 \(\frac{1}{2\sin x}+\frac{1}{1+\cos x}\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先将 \(\sin2x\) 写成 \(2\sin x\cos x\)，把分母化为 \(2\sin x(1+\cos x)\)。 |
| missed_action | 没有想到倍角展开；没有提公因式；没有把 \(1+\cos x\) 半角化；没有触发 \(t=\tan\frac{x}{2}\) 的万能代换。 |
| related_method_card_id | H09-006 |
| next_reminder | 看到三角分母里有 \(\sin2x\)，先倍角展开；一旦出现 \(1+\cos x\) 或 \(1-\cos x\)，优先半角化并检查 \(t=\tan\frac{x}{2}\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-041_三角有理式入口识别不足]]
- [[MATHWIKI-ERROR-CLUSTER-070_半角公式触发失败]]
- [[MATHWIKI-ERROR-CLUSTER-099_万能代换意识不足]]
- [[MATHWIKI-ERROR-CLUSTER-117_倍角公式触发失败]]
- [[MATHWIKI-ERROR-CLUSTER-137_分式拆分误区]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-043_三角恒等变形]]
- [[MATHWIKI-KNOWLEDGE-050_整体凑微分]]
- [[MATHWIKI-KNOWLEDGE-079_三角函数有理式]]
- [[MATHWIKI-KNOWLEDGE-197_半角公式]]
- [[MATHWIKI-KNOWLEDGE-223_万能代换]]
- [[MATHWIKI-KNOWLEDGE-229_二倍角公式]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-025_三角恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-032_整体凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-055_三角函数有理式]]
- [[MATHWIKI-METHOD-CLUSTER-188_二倍角公式]]
- [[MATHWIKI-METHOD-CLUSTER-203_半角公式]]
- [[MATHWIKI-METHOD-CLUSTER-272_万能代换]]
- [[MATHWIKI-METHOD-CLUSTER-298_凑d-tan-x-2]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-600
- GS-619
- GS-621
- GS-622
- GS-623
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
