---
wiki_id: SRC-WQ-GS-604
type: source_summary
title: "GS-604 57707-2 有理函数分式拆分"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-604_57707有理函数分式拆分.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-604"
knowledge:
  - "不定积分"
  - "有理函数积分"
  - "分式拆分"
  - "部分分式"
error_causes:
  - "入口选择错误"
  - "有理函数积分识别不稳"
  - "凑微分优先级过高"
  - "分式拆分动作断点"
  - "平方差公式触发不稳"
  - "部分分式拆分不熟"
methods:
  - "有理函数积分"
  - "分母因式分解"
  - "分式拆分"
  - "部分分式"
  - "通分验证"
  - "平方差公式"
  - "化归经典形式"
  - "基本积分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-120_入口选择错误"
  - "MATHWIKI-ERROR-CLUSTER-127_凑微分优先级过高"
  - "MATHWIKI-ERROR-CLUSTER-136_分式拆分动作断点"
  - "MATHWIKI-ERROR-CLUSTER-206_平方差公式触发不稳"
  - "MATHWIKI-ERROR-CLUSTER-362_有理函数积分识别不稳"
  - "MATHWIKI-ERROR-CLUSTER-440_部分分式拆分不熟"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-044_有理函数积分"
  - "MATHWIKI-KNOWLEDGE-046_部分分式"
  - "MATHWIKI-KNOWLEDGE-194_分式拆分"
  - "MATHWIKI-METHOD-CLUSTER-035_部分分式"
  - "MATHWIKI-METHOD-CLUSTER-072_有理函数积分"
  - "MATHWIKI-METHOD-CLUSTER-091_化归经典形式"
  - "MATHWIKI-METHOD-CLUSTER-1380_通分验证"
  - "MATHWIKI-METHOD-CLUSTER-305_分式拆分"
  - "MATHWIKI-METHOD-CLUSTER-676_分母因式分解"
  - "MATHWIKI-METHOD-CLUSTER-853_基本积分"
  - "MATHWIKI-METHOD-CLUSTER-982_平方差公式"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-039_不定积分结构化化归入口"
  - "MATHWIKI-GS-METHOD-076_分式积分拆到底与分母降幂链"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-604 57707-2 有理函数分式拆分

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-604_57707有理函数分式拆分.md`
- wrongnet ID：`GS-604`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 有理函数积分：分式拆分 + 平方差公式 + 基本积分 |
| 日期 | 2026-06-13 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 不定积分
- 有理函数积分
- 分式拆分
- 部分分式

### 错因

- 入口选择错误
- 有理函数积分识别不稳
- 凑微分优先级过高
- 分式拆分动作断点
- 平方差公式触发不稳
- 部分分式拆分不熟

### 方法

- 有理函数积分
- 分母因式分解
- 分式拆分
- 部分分式
- 通分验证
- 平方差公式
- 化归经典形式
- 基本积分

### 陷阱

- 多项式分式先拆分不要先凑换元
- \(u=1/x\) 会让 \(1-x^4\) 更复杂
- 先通分验证拆分是否成立
- \(1-x^4=(1-x^2)(1+x^2)\)
- 不要把 \(1-x^4\) 写成 \(1+x^4\)
- \(\frac1{1-x^4}=\frac12(\frac1{1-x^2}+\frac1{1+x^2})\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先将分子分母同乘 \(x^2\)，制造 \(x^4(1-x^4)\)，再利用 \(\frac1{x^4(1-x^4)}=\frac1{x^4}+\frac1{1-x^4}\)。 |
| missed_action | 第1次入口先凑 \(d(\frac1x)\) 没先拆分（B3-METHOD）；第2次入口已对但拆分链中途停下，没把 \(\frac1{1-x^4}\) 拆成 \(\frac12(\frac1{1-x^2}+\frac1{1+x^2})\)、没把 \(\int\frac1{1-x… |
| related_method_card_id | H09-004 |
| next_reminder | 分母含 \(1-x^4\)：入口按有理函数拆出 \(\frac1{x^2}+\frac{x^2}{1-x^4}\) 后必须拆到底——\(\frac1{1-x^4}=\frac12(\frac1{1-x^2}+\frac1{1+x^2})\)，再把 \(\frac1{1-x^2}… |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-120_入口选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-127_凑微分优先级过高]]
- [[MATHWIKI-ERROR-CLUSTER-136_分式拆分动作断点]]
- [[MATHWIKI-ERROR-CLUSTER-206_平方差公式触发不稳]]
- [[MATHWIKI-ERROR-CLUSTER-362_有理函数积分识别不稳]]
- [[MATHWIKI-ERROR-CLUSTER-440_部分分式拆分不熟]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-044_有理函数积分]]
- [[MATHWIKI-KNOWLEDGE-046_部分分式]]
- [[MATHWIKI-KNOWLEDGE-194_分式拆分]]
- [[MATHWIKI-METHOD-CLUSTER-035_部分分式]]
- [[MATHWIKI-METHOD-CLUSTER-072_有理函数积分]]
- [[MATHWIKI-METHOD-CLUSTER-091_化归经典形式]]
- [[MATHWIKI-METHOD-CLUSTER-1380_通分验证]]
- [[MATHWIKI-METHOD-CLUSTER-305_分式拆分]]
- [[MATHWIKI-METHOD-CLUSTER-676_分母因式分解]]
- [[MATHWIKI-METHOD-CLUSTER-853_基本积分]]
- [[MATHWIKI-METHOD-CLUSTER-982_平方差公式]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-METHOD-076_分式积分拆到底与分母降幂链]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-603
- GS-605
- GS-266
- GS-270
- GS-278
- GS-581

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
