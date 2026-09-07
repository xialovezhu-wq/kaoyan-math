---
wiki_id: SRC-WQ-GS-281
type: source_summary
title: "GS-281 强化例题9.12（135752）"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-281_强化例题9.12（135752）.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-281"
knowledge:
  - "不定积分"
  - "一元函数积分学的计算"
  - "三角函数有理式"
  - "三角恒等变形"
  - "第一类换元"
error_causes:
  - "旧批量导入未记录原始个人错因；2026-06-28 仅确认复做正确，保留“三角奇次幂拆因子凑微分”的复查入口。"
methods:
  - "第一类换元"
  - "整体凑微分"
  - "三角恒等变形"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-256_旧批量导入未记录原始个人错因-2026-06-28仅确认复做正确-保留“"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-043_三角恒等变形"
  - "MATHWIKI-KNOWLEDGE-079_三角函数有理式"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-025_三角恒等变形"
  - "MATHWIKI-METHOD-CLUSTER-032_整体凑微分"
  - "MATHWIKI-GS-METHOD-039_不定积分结构化化归入口"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-281 强化例题9.12（135752）

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-281_强化例题9.12（135752）.md`
- wrongnet ID：`GS-281`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 三角幂函数不定积分：拆奇次幂凑微分 |
| 日期 | 2026-05-07 |
| 状态 | 已掌握 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 不定积分
- 一元函数积分学的计算
- 三角函数有理式
- 三角恒等变形
- 第一类换元

### 错因

- 旧批量导入未记录原始个人错因；2026-06-28 仅确认复做正确，保留“三角奇次幂拆因子凑微分”的复查入口。

### 方法

- 第一类换元
- 整体凑微分
- 三角恒等变形

### 陷阱

- 内层函数导数识别断点
- 换元后dx处理不完整
- 已掌握题，常规错题复做队列跳过

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先把 \(\cos^3x\) 拆成 \((1-\sin^2x)\cos x\)，令 \(t=\sin x\)。 |
| missed_action | 用户已反馈复做正确；原始错因未记录，此处只保留常规队列跳过后的快速复查入口。 |
| related_method_card_id | H09-002 |
| next_reminder | 看到三角函数奇次幂，先拆一个因子凑另一个函数的微分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-256_旧批量导入未记录原始个人错因-2026-06-28仅确认复做正确-保留“]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-043_三角恒等变形]]
- [[MATHWIKI-KNOWLEDGE-079_三角函数有理式]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-025_三角恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-032_整体凑微分]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
