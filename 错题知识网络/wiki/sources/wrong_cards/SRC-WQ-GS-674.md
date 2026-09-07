---
wiki_id: SRC-WQ-GS-674
type: source_summary
title: "GS-674 193302 倒代换合并积分值域"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-674_193302倒代换合并积分值域.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-674"
knowledge:
  - "定积分"
  - "定积分等式"
  - "变上限积分"
  - "第一类换元"
  - "一元函数积分学的计算"
  - "单调性与极值"
error_causes:
  - "触发信息遗漏"
  - "方法论调取失败"
  - "目标识别断点"
methods:
  - "先判型"
  - "定积分等式入口"
  - "倒代换"
  - "定积分换元"
  - "上限统一"
  - "积分合并"
  - "通分化简"
  - "凑微分"
  - "值域求解"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-034_目标识别断点"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-084_定积分等式"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-094_定积分换元"
  - "MATHWIKI-METHOD-CLUSTER-109_倒代换"
  - "MATHWIKI-METHOD-CLUSTER-1261_积分合并"
  - "MATHWIKI-METHOD-CLUSTER-293_值域求解"
  - "MATHWIKI-METHOD-CLUSTER-467_通分化简"
  - "MATHWIKI-METHOD-CLUSTER-522_上限统一"
  - "MATHWIKI-METHOD-CLUSTER-637_凑微分"
  - "MATHWIKI-METHOD-CLUSTER-900_定积分等式入口"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-674 193302 倒代换合并积分值域

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-674_193302倒代换合并积分值域.md`
- wrongnet ID：`GS-674`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 倒代换合并变上限积分值域 |
| 日期 | 2026-07-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分等式
- 变上限积分
- 第一类换元
- 一元函数积分学的计算
- 单调性与极值

### 错因

- 触发信息遗漏
- 方法论调取失败
- 目标识别断点

### 方法

- 先判型
- 定积分等式入口
- 倒代换
- 定积分换元
- 上限统一
- 积分合并
- 通分化简
- 凑微分
- 值域求解

### 陷阱

- $x\to0^+$ 时只有第二个上限 $1/x\to+\infty$，不能把整道题直接当作 $x\to+\infty$ 来处理。
- 只看一端趋于 $+\infty$ 只能说明左侧函数无上界，不能说明完整取值范围。
- 上限出现 $1/x$ 且被积函数同形时，优先试 $t=1/u$ 倒代换，把积分上限统一。
- 合并后要通分成 $\frac{\ln t}{t}$，再由 $\ln x$ 的取值范围判断 $a$。
- $x=1$ 时左侧为 $0$，所以下端点 $0$ 取到。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先令第二个积分中 $t=1/u$，写出 $dt=-\frac1{u^2}du$，并把积分上下限 $1,1/x$ 转成 $1,x$。 |
| missed_action | 没有先用 $t=1/u$ 倒代换统一两个积分上限，而是只观察 $x\to0^+$ 时第二个积分趋向无穷的一端趋势。 |
| related_method_card_id | H11-001 |
| next_reminder | 看到同一被积函数的定积分上限同时出现 $x$ 与 $1/x$，先试 $t=1/u$ 把上限统一，再合并积分；求参数范围时必须看整个定义域上的值域。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-034_目标识别断点]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-084_定积分等式]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-094_定积分换元]]
- [[MATHWIKI-METHOD-CLUSTER-109_倒代换]]
- [[MATHWIKI-METHOD-CLUSTER-1261_积分合并]]
- [[MATHWIKI-METHOD-CLUSTER-293_值域求解]]
- [[MATHWIKI-METHOD-CLUSTER-467_通分化简]]
- [[MATHWIKI-METHOD-CLUSTER-522_上限统一]]
- [[MATHWIKI-METHOD-CLUSTER-637_凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-900_定积分等式入口]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-174
- GS-186
- GS-191

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
