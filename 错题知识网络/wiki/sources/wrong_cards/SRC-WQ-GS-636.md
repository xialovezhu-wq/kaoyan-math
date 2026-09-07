---
wiki_id: SRC-WQ-GS-636
type: source_summary
title: "GS-636 58102-2 整体换元幂三角"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-636_58102-2整体换元幂三角.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-636"
knowledge:
  - "定积分"
  - "一元函数积分学的计算"
  - "第一类换元"
  - "第二类换元"
  - "整体凑微分"
  - "三角换元"
  - "华里士公式"
  - "三角恒等变形"
  - "幂三角积分"
error_causes:
  - "凑微分后动作链中断"
  - "整体变量识别不足"
  - "三角换元模板过窄"
  - "触发信息遗漏"
  - "动作链断裂"
  - "方法论调取不稳"
methods:
  - "先判型"
  - "整体凑微分"
  - "第一类换元"
  - "第二类换元"
  - "三角换元"
  - "特殊角换限"
  - "华里士公式"
  - "降幂公式"
  - "定积分计算"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳"
  - "MATHWIKI-ERROR-CLUSTER-104_三角换元模板过窄"
  - "MATHWIKI-ERROR-CLUSTER-128_凑微分后动作链中断"
  - "MATHWIKI-ERROR-CLUSTER-237_整体变量识别不足"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-041_第二类换元"
  - "MATHWIKI-KNOWLEDGE-043_三角恒等变形"
  - "MATHWIKI-KNOWLEDGE-050_整体凑微分"
  - "MATHWIKI-KNOWLEDGE-080_三角换元"
  - "MATHWIKI-KNOWLEDGE-138_华里士公式"
  - "MATHWIKI-KNOWLEDGE-354_幂三角积分"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-028_三角换元"
  - "MATHWIKI-METHOD-CLUSTER-032_整体凑微分"
  - "MATHWIKI-METHOD-CLUSTER-042_定积分计算"
  - "MATHWIKI-METHOD-CLUSTER-044_第二类换元"
  - "MATHWIKI-METHOD-CLUSTER-110_华里士公式"
  - "MATHWIKI-METHOD-CLUSTER-136_降幂公式"
  - "MATHWIKI-METHOD-CLUSTER-245_特殊角换限"
  - "MATHWIKI-GS-CONCEPT-002_积分结构中心"
  - "MATHWIKI-GS-ERROR-002_只看局部不看整体"
  - "MATHWIKI-GS-METHOD-005_凑微分后的整体变量链"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-TOPIC-002_一元积分近期错题簇"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-GS-TRIGGER-002_积分先找中心与整体"
  - "MATHWIKI-GS-TRIGGER-003_整体平方差先设整体"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-620"
  - "GS-633"
formal_projection_sha256: 6174b6748b1c3390c3cfc5b21d889dc41f03002ce3fe2fc7f360dda9815396f6
---

# GS-636 58102-2 整体换元幂三角

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-636_58102-2整体换元幂三角.md`
- wrongnet ID：`GS-636`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 凑微分后整体三角换元：幂三角积分 |
| 日期 | 2026-06-28 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 一元函数积分学的计算
- 第一类换元
- 第二类换元
- 整体凑微分
- 三角换元
- 华里士公式
- 三角恒等变形
- 幂三角积分

### 错因

- 凑微分后动作链中断
- 整体变量识别不足
- 三角换元模板过窄
- 触发信息遗漏
- 动作链断裂
- 方法论调取不稳

### 方法

- 先判型
- 整体凑微分
- 第一类换元
- 第二类换元
- 三角换元
- 特殊角换限
- 华里士公式
- 降幂公式
- 定积分计算

### 陷阱

- \(1-x^4\) 先看成 \(1-(x^2)^2\)
- \(x\,dx=\frac12d(x^2)\)
- 三角换元可以换整体，不一定只换 \(x\)
- 看到 \(1-[\text{整体}]^2\)，优先令这个整体等于 \(\sin t\)
- \(x^2=\sin t\) 后 \(2x\,dx=\cos t\,dt\)
- 换元后要同步改上下限
- \(\int_0^{\pi/2}\cos^4t\,dt=\frac{3\pi}{16}\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把 \(x\,dx\) 写成 \(\frac12d(x^2)\)，并把 \(1-x^4\) 改写成 \(1-(x^2)^2\)。 |
| missed_action | 凑微分后没有把 \(x^2\) 作为整体变量，也没有想到令 \(x^2=\sin t\)。 |
| related_method_card_id | H09-002 |
| next_reminder | 三角换元不一定是 \(x=\sin t\)；看到 \(1-[\text{整体}]^2\)，先让这个整体等于 \(\sin t\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳]]
- [[MATHWIKI-ERROR-CLUSTER-104_三角换元模板过窄]]
- [[MATHWIKI-ERROR-CLUSTER-128_凑微分后动作链中断]]
- [[MATHWIKI-ERROR-CLUSTER-237_整体变量识别不足]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-KNOWLEDGE-043_三角恒等变形]]
- [[MATHWIKI-KNOWLEDGE-050_整体凑微分]]
- [[MATHWIKI-KNOWLEDGE-080_三角换元]]
- [[MATHWIKI-KNOWLEDGE-138_华里士公式]]
- [[MATHWIKI-KNOWLEDGE-354_幂三角积分]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-032_整体凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-042_定积分计算]]
- [[MATHWIKI-METHOD-CLUSTER-044_第二类换元]]
- [[MATHWIKI-METHOD-CLUSTER-110_华里士公式]]
- [[MATHWIKI-METHOD-CLUSTER-136_降幂公式]]
- [[MATHWIKI-METHOD-CLUSTER-245_特殊角换限]]

### 深度编译页

- [[MATHWIKI-GS-CONCEPT-002_积分结构中心]]
- [[MATHWIKI-GS-ERROR-002_只看局部不看整体]]
- [[MATHWIKI-GS-METHOD-005_凑微分后的整体变量链]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-TOPIC-002_一元积分近期错题簇]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-GS-TRIGGER-002_积分先找中心与整体]]
- [[MATHWIKI-GS-TRIGGER-003_整体平方差先设整体]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-620
- GS-633

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
