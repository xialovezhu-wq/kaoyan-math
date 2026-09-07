---
wiki_id: SRC-WQ-GS-605
type: source_summary
title: "GS-605 57707-3 反三角乘有理分部绕圈"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-605_57707反三角乘有理分部绕圈.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-605"
knowledge:
  - "不定积分"
  - "有理函数积分"
  - "分式拆分"
  - "部分分式"
  - "分部积分"
  - "反三角函数积分"
error_causes:
  - "分式拆分入口未触发"
  - "分部积分绕圈未识别"
  - "有理函数拆分不熟"
  - "arctan与arccot导数符号混淆"
  - "凑微分与分部积分优先级判断不稳"
methods:
  - "有理函数积分"
  - "分式拆分"
  - "部分分式"
  - "分部积分"
  - "凑微分换元"
  - "化归经典形式"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-098_arctan与arccot导数符号混淆"
  - "MATHWIKI-ERROR-CLUSTER-126_凑微分与分部积分优先级判断不稳"
  - "MATHWIKI-ERROR-CLUSTER-135_分式拆分入口未触发"
  - "MATHWIKI-ERROR-CLUSTER-147_分部积分绕圈未识别"
  - "MATHWIKI-ERROR-CLUSTER-360_有理函数拆分不熟"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-044_有理函数积分"
  - "MATHWIKI-KNOWLEDGE-046_部分分式"
  - "MATHWIKI-KNOWLEDGE-194_分式拆分"
  - "MATHWIKI-KNOWLEDGE-243_反三角函数积分"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-035_部分分式"
  - "MATHWIKI-METHOD-CLUSTER-064_凑微分换元"
  - "MATHWIKI-METHOD-CLUSTER-072_有理函数积分"
  - "MATHWIKI-METHOD-CLUSTER-091_化归经典形式"
  - "MATHWIKI-METHOD-CLUSTER-305_分式拆分"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-605 57707-3 反三角乘有理分部绕圈

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-605_57707反三角乘有理分部绕圈.md`
- wrongnet ID：`GS-605`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 反三角函数乘有理函数不定积分：先拆有理函数 + 分部积分 + 凑微分 |
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
- 分部积分
- 反三角函数积分

### 错因

- 分式拆分入口未触发
- 分部积分绕圈未识别
- 有理函数拆分不熟
- arctan与arccot导数符号混淆
- 凑微分与分部积分优先级判断不稳

### 方法

- 有理函数积分
- 分式拆分
- 部分分式
- 分部积分
- 凑微分换元
- 化归经典形式

### 陷阱

- 反三角函数乘有理函数不要先整体分部，先拆有理函数
- \(\frac1{x^2(1+x^2)}=\frac1{x^2}-\frac1{1+x^2}\)
- 分部积分绕回 \(A=A\) 不是结论，是换路信号
- \(\int\frac{dx}{x(1+x^2)}\) 要继续拆成 \(\frac1x-\frac{x}{1+x^2}\)，不要再分部
- \((\arctan x)'=\frac1{1+x^2}\) 为正
- \((\operatorname{arccot}x)'=-\frac1{1+x^2}\) 为负
- 不要混淆 arctan 与 arccot 的导数符号

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写 \(\frac1{x^2(1+x^2)}=\frac1{x^2}-\frac1{1+x^2}\)。 |
| missed_action | 没有优先拆分有理函数；对 \(\int\frac{dx}{x(1+x^2)}\) 继续分部积分导致绕回原式得到 \(A=A\)；并混淆 \(\arctan x\) 与 \(\operatorname{arccot}x\) 的导数符号。 |
| related_method_card_id | H09-005 |
| next_reminder | 看到 arctan 乘有理函数，先拆有理函数再分部；分部绕回 \(A=A\) 时不要继续绕，去拆剩下的有理函数。arctan 导数为正，arccot 导数为负。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-098_arctan与arccot导数符号混淆]]
- [[MATHWIKI-ERROR-CLUSTER-126_凑微分与分部积分优先级判断不稳]]
- [[MATHWIKI-ERROR-CLUSTER-135_分式拆分入口未触发]]
- [[MATHWIKI-ERROR-CLUSTER-147_分部积分绕圈未识别]]
- [[MATHWIKI-ERROR-CLUSTER-360_有理函数拆分不熟]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-044_有理函数积分]]
- [[MATHWIKI-KNOWLEDGE-046_部分分式]]
- [[MATHWIKI-KNOWLEDGE-194_分式拆分]]
- [[MATHWIKI-KNOWLEDGE-243_反三角函数积分]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-035_部分分式]]
- [[MATHWIKI-METHOD-CLUSTER-064_凑微分换元]]
- [[MATHWIKI-METHOD-CLUSTER-072_有理函数积分]]
- [[MATHWIKI-METHOD-CLUSTER-091_化归经典形式]]
- [[MATHWIKI-METHOD-CLUSTER-305_分式拆分]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-266
- GS-270
- GS-601
- GS-603
- GS-604

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
