---
wiki_id: SRC-WQ-GS-623
type: source_summary
title: "GS-623 57931-3 分母整体线性拆分"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-623_57931-3分母整体线性拆分.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-623"
knowledge:
  - "不定积分"
  - "一元函数积分学的计算"
  - "三角函数有理式"
  - "分母整体法"
  - "分子线性拆分"
  - "第一类换元"
  - "整体凑微分"
  - "对数型积分"
error_causes:
  - "三角有理式入口识别不足"
  - "分母整体意识不足"
  - "分母导数识别断点"
  - "分子线性拆分触发失败"
  - "分子拆分断点"
  - "凑微分识别不足"
  - "对数型积分入口未触发"
  - "方法论调取失败"
methods:
  - "先判型"
  - "三角函数有理式"
  - "分母整体法"
  - "分子线性拆分"
  - "第一类换元"
  - "整体凑微分"
  - "对数型积分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-041_三角有理式入口识别不足"
  - "MATHWIKI-ERROR-CLUSTER-067_凑微分识别不足"
  - "MATHWIKI-ERROR-CLUSTER-068_分母导数识别断点"
  - "MATHWIKI-ERROR-CLUSTER-132_分子拆分断点"
  - "MATHWIKI-ERROR-CLUSTER-134_分子线性拆分触发失败"
  - "MATHWIKI-ERROR-CLUSTER-144_分母整体意识不足"
  - "MATHWIKI-ERROR-CLUSTER-194_对数型积分入口未触发"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-050_整体凑微分"
  - "MATHWIKI-KNOWLEDGE-057_对数型积分"
  - "MATHWIKI-KNOWLEDGE-079_三角函数有理式"
  - "MATHWIKI-KNOWLEDGE-234_分子线性拆分"
  - "MATHWIKI-KNOWLEDGE-313_分母整体法"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-032_整体凑微分"
  - "MATHWIKI-METHOD-CLUSTER-055_三角函数有理式"
  - "MATHWIKI-METHOD-CLUSTER-200_分子线性拆分"
  - "MATHWIKI-METHOD-CLUSTER-354_对数型积分"
  - "MATHWIKI-METHOD-CLUSTER-680_分母整体法"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-039_不定积分结构化化归入口"
  - "MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-623 57931-3 分母整体线性拆分

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-623_57931-3分母整体线性拆分.md`
- wrongnet ID：`GS-623`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 三角函数有理式不定积分：分母整体 + 分子线性拆分 |
| 日期 | 2026-06-24 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 不定积分
- 一元函数积分学的计算
- 三角函数有理式
- 分母整体法
- 分子线性拆分
- 第一类换元
- 整体凑微分
- 对数型积分

### 错因

- 三角有理式入口识别不足
- 分母整体意识不足
- 分母导数识别断点
- 分子线性拆分触发失败
- 分子拆分断点
- 凑微分识别不足
- 对数型积分入口未触发
- 方法论调取失败

### 方法

- 先判型
- 三角函数有理式
- 分母整体法
- 分子线性拆分
- 第一类换元
- 整体凑微分
- 对数型积分

### 陷阱

- 分母 \(\sin x+\cos x\) 是整体 \(F(x)\)
- 先算 \(F'(x)=\cos x-\sin x\)
- 检查分子能否写成 \(AF'(x)+BF(x)\)
- \(\sin x=-\frac12(\cos x-\sin x)+\frac12(\sin x+\cos x)\)
- \(\int\frac{F'(x)}{F(x)}dx=\ln|F(x)|\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先算 \(F'(x)=\cos x-\sin x\)，再设 \(\sin x=A(\cos x-\sin x)+B(\sin x+\cos x)\) 并比较系数。 |
| missed_action | 没有把分母看成整体；没有主动用分母导数参与拆分分子；因此没有触发 \(\int\frac{F'(x)}{F(x)}dx=\ln|F(x)|\)。 |
| related_method_card_id | H09-006 |
| next_reminder | 分式积分中，分母若是明显整体 \(F(x)\)，先算 \(F'(x)\)，再看分子能不能写成 \(AF'(x)+BF(x)\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-041_三角有理式入口识别不足]]
- [[MATHWIKI-ERROR-CLUSTER-067_凑微分识别不足]]
- [[MATHWIKI-ERROR-CLUSTER-068_分母导数识别断点]]
- [[MATHWIKI-ERROR-CLUSTER-132_分子拆分断点]]
- [[MATHWIKI-ERROR-CLUSTER-134_分子线性拆分触发失败]]
- [[MATHWIKI-ERROR-CLUSTER-144_分母整体意识不足]]
- [[MATHWIKI-ERROR-CLUSTER-194_对数型积分入口未触发]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-050_整体凑微分]]
- [[MATHWIKI-KNOWLEDGE-057_对数型积分]]
- [[MATHWIKI-KNOWLEDGE-079_三角函数有理式]]
- [[MATHWIKI-KNOWLEDGE-234_分子线性拆分]]
- [[MATHWIKI-KNOWLEDGE-313_分母整体法]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-032_整体凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-055_三角函数有理式]]
- [[MATHWIKI-METHOD-CLUSTER-200_分子线性拆分]]
- [[MATHWIKI-METHOD-CLUSTER-354_对数型积分]]
- [[MATHWIKI-METHOD-CLUSTER-680_分母整体法]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-603
- GS-604
- GS-619
- GS-621
- GS-622
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
