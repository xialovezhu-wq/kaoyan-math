---
wiki_id: SRC-WQ-GS-139
type: source_summary
title: "GS-139 1000题B组5.21 导函数图像判拐点"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-139_1000题B组5.21.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-139"
knowledge:
  - "凹凸性与拐点"
  - "二阶导数判凹凸性"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是把 f' 过零点误当拐点，需用户复做确认。"
methods:
  - "导函数图像判别"
  - "导数判单调"
  - "二阶导判凹凸性"
  - "图像分析"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-316_旧批量未记录个人原始错因-当前仅确认复做断点是把f'过零点误当拐点-需用"
  - "MATHWIKI-KNOWLEDGE-018_凹凸性与拐点"
  - "MATHWIKI-KNOWLEDGE-098_二阶导数判凹凸性"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-089_二阶导判凹凸性"
  - "MATHWIKI-METHOD-CLUSTER-342_图像分析"
  - "MATHWIKI-METHOD-CLUSTER-937_导函数图像判别"
  - "MATHWIKI-GS-METHOD-052_局部性质与导数符号单向判别"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: 31f2837449f470b0ec13377cc2751b02b03ae4c82eb8c60d2c3a1296f58d8399
---

# GS-139 1000题B组5.21 导函数图像判拐点

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-139_1000题B组5.21.md`
- wrongnet ID：`GS-139`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 导函数图像判断拐点个数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 2 |

## 可编译信息

### 知识点

- 凹凸性与拐点
- 二阶导数判凹凸性

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是把 f' 过零点误当拐点，需用户复做确认。

### 方法

- 导函数图像判别
- 导数判单调
- 二阶导判凹凸性
- 图像分析

### 陷阱

- \(f'(x)=0\) 不是拐点判定条件
- \(f'\) 过零点只说明 \(f\) 的增减可能变化
- 拐点要看 \(f'\) 由增变减或由减变增，即 \(f''\) 变号

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先标出 f' 由增变减或由减变增的候选点 |
| missed_action | 旧批量未记录个人步骤；当前复做风险是只看 f'=0 或图像交轴点 |
| related_method_card_id | H05-004 |
| next_reminder | 看到 f' 图像判拐点，先看 f' 的增减变化，不要只看 f'=0。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-316_旧批量未记录个人原始错因-当前仅确认复做断点是把f'过零点误当拐点-需用]]
- [[MATHWIKI-KNOWLEDGE-018_凹凸性与拐点]]
- [[MATHWIKI-KNOWLEDGE-098_二阶导数判凹凸性]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-089_二阶导判凹凸性]]
- [[MATHWIKI-METHOD-CLUSTER-342_图像分析]]
- [[MATHWIKI-METHOD-CLUSTER-937_导函数图像判别]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-052_局部性质与导数符号单向判别]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

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
