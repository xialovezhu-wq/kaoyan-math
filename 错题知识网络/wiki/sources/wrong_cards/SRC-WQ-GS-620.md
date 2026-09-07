---
wiki_id: SRC-WQ-GS-620
type: source_summary
title: "GS-620 57869-6 根式幂次凑微分"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-620_57869-6根式幂次凑微分.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-620"
knowledge:
  - "不定积分"
  - "一元函数积分学的计算"
  - "根式积分"
  - "幂次统一"
  - "分数幂凑微分"
  - "第一类换元"
  - "第二类换元"
  - "根式换元"
  - "整体凑微分"
error_causes:
  - "根式幂次统一意识不足"
  - "换元后dx处理不完整"
  - "凑微分触发失败"
  - "内层函数导数识别断点"
  - "动作链断裂"
methods:
  - "先判型"
  - "幂次统一"
  - "分数幂凑微分"
  - "第一类换元"
  - "第二类换元"
  - "整体凑微分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-056_换元后dx处理不完整"
  - "MATHWIKI-ERROR-CLUSTER-124_内层函数导数识别断点"
  - "MATHWIKI-ERROR-CLUSTER-129_凑微分触发失败"
  - "MATHWIKI-ERROR-CLUSTER-375_根式幂次统一意识不足"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-041_第二类换元"
  - "MATHWIKI-KNOWLEDGE-050_整体凑微分"
  - "MATHWIKI-KNOWLEDGE-058_根式积分"
  - "MATHWIKI-KNOWLEDGE-103_根式换元"
  - "MATHWIKI-KNOWLEDGE-309_分数幂凑微分"
  - "MATHWIKI-KNOWLEDGE-356_幂次统一"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-032_整体凑微分"
  - "MATHWIKI-METHOD-CLUSTER-044_第二类换元"
  - "MATHWIKI-METHOD-CLUSTER-670_分数幂凑微分"
  - "MATHWIKI-METHOD-CLUSTER-971_幂次统一"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-039_不定积分结构化化归入口"
  - "MATHWIKI-GS-METHOD-043_根式积分换元与回代链"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-620 57869-6 根式幂次凑微分

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-620_57869-6根式幂次凑微分.md`
- wrongnet ID：`GS-620`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 根式型不定积分：分数幂统一后凑微分 |
| 日期 | 2026-06-24 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 不定积分
- 一元函数积分学的计算
- 根式积分
- 幂次统一
- 分数幂凑微分
- 第一类换元
- 第二类换元
- 根式换元
- 整体凑微分

### 错因

- 根式幂次统一意识不足
- 换元后dx处理不完整
- 凑微分触发失败
- 内层函数导数识别断点
- 动作链断裂

### 方法

- 先判型
- 幂次统一
- 分数幂凑微分
- 第一类换元
- 第二类换元
- 整体凑微分

### 陷阱

- 根式题先把 \(\sqrt{x}\) 写成 \(x^{1/2}\)
- \(x\sqrt{x}=x^{3/2}\)
- \(d(x^{3/2})=\frac32x^{1/2}dx\)
- 令 \(\sqrt{x}=t\) 时必须同时替换 \(x=t^2\) 和 \(dx=2t\,dt\)
- 看到 \(1-t^3\) 要检查分子是否有 \(t^2dt\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把原式改写成 \(\int\frac{x^{1/2}}{\sqrt{1-x^{3/2}}}\,dx\)，再凑 \(d(x^{3/2})\)。 |
| missed_action | 没有把分子 \(\sqrt{x}\,dx\) 放到导数后面；令 \(\sqrt{x}=t\) 后没有正确利用 \(dx=2t\,dt\) 得到 \(2t^2dt\) 并凑 \(d(1-t^3)\)。 |
| related_method_card_id | H09-002 |
| next_reminder | 看到根式题，先幂次化；换元后必须同时替换 \(x\)、根式和 \(dx\)，再检查分子是否正好是内层函数的微分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-056_换元后dx处理不完整]]
- [[MATHWIKI-ERROR-CLUSTER-124_内层函数导数识别断点]]
- [[MATHWIKI-ERROR-CLUSTER-129_凑微分触发失败]]
- [[MATHWIKI-ERROR-CLUSTER-375_根式幂次统一意识不足]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-KNOWLEDGE-050_整体凑微分]]
- [[MATHWIKI-KNOWLEDGE-058_根式积分]]
- [[MATHWIKI-KNOWLEDGE-103_根式换元]]
- [[MATHWIKI-KNOWLEDGE-309_分数幂凑微分]]
- [[MATHWIKI-KNOWLEDGE-356_幂次统一]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-032_整体凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-044_第二类换元]]
- [[MATHWIKI-METHOD-CLUSTER-670_分数幂凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-971_幂次统一]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-METHOD-043_根式积分换元与回代链]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-268
- GS-603
- GS-610
- GS-618
- GS-619

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
