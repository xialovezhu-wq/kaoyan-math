---
wiki_id: SRC-WQ-GS-085
type: source_summary
title: "GS-085 1000题B组3.20"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-085_1000题B组3.20.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-085"
knowledge:
  - "一元函数微分学应用"
  - "泰勒公式"
  - "等价无穷小"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是复合自变量增量与一阶泰勒入口未先落地，需用户复做确认是否为当时第一断点。"
methods:
  - "一阶泰勒展开"
  - "等价无穷小"
  - "有限极限反推"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-308_旧批量未记录个人原始错因-当前仅确认复做断点是复合自变量增量与一阶泰勒入"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-METHOD-CLUSTER-026_等价无穷小"
  - "MATHWIKI-METHOD-CLUSTER-1094_有限极限反推"
  - "MATHWIKI-METHOD-CLUSTER-506_一阶泰勒展开"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-METHOD-013_导数定义差商入口"
  - "MATHWIKI-GS-METHOD-093_局部展开对象与真实增量匹配"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-085 1000题B组3.20

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-085_1000题B组3.20.md`
- wrongnet ID：`GS-085`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 复合自变量一阶泰勒求导数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 泰勒公式
- 等价无穷小

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是复合自变量增量与一阶泰勒入口未先落地，需用户复做确认是否为当时第一断点。

### 方法

- 一阶泰勒展开
- 等价无穷小
- 有限极限反推

### 陷阱

- 常数项发散
- 复合自变量增量
- 同阶项系数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先设 Δ1=cos x-1、Δ2=sin²x，并写出 f(1+Δ)=f(1)+f'(1)Δ+o(Δ) |
| missed_action | 旧批量未记录个人步骤；当前复做风险是没有先识别两个真实增量并检查常数项 |
| related_method_card_id | H03-001 |
| next_reminder | 看到多个复合自变量同时趋近同一点，先写各自真实增量，再用一阶泰勒检查常数项。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-308_旧批量未记录个人原始错因-当前仅确认复做断点是复合自变量增量与一阶泰勒入]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-METHOD-CLUSTER-026_等价无穷小]]
- [[MATHWIKI-METHOD-CLUSTER-1094_有限极限反推]]
- [[MATHWIKI-METHOD-CLUSTER-506_一阶泰勒展开]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-METHOD-013_导数定义差商入口]]
- [[MATHWIKI-GS-METHOD-093_局部展开对象与真实增量匹配]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

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
