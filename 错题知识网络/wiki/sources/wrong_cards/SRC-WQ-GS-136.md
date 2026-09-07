---
wiki_id: SRC-WQ-GS-136
type: source_summary
title: "GS-136 1000题B组5.6"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-136_1000题B组5.6.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-136"
knowledge:
  - "一元函数微分学应用"
  - "单调性与极值"
  - "恒成立不等式"
  - "重要极限"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是分离参数时除以负数未变号或没有取辅助函数上确界，需用户复做确认。"
methods:
  - "分离参数"
  - "构造辅助函数"
  - "导数判单调"
  - "端点极限求上确界"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-302_旧批量未记录个人原始错因-当前仅确认复做断点是分离参数时除以负数未变号或"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-130_重要极限"
  - "MATHWIKI-KNOWLEDGE-254_恒成立不等式"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-1276_端点极限求上确界"
  - "MATHWIKI-METHOD-CLUSTER-313_分离参数"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-135"
formal_projection_sha256: 9a530c476846fb19744a5c448c1ea1994657f002a1fc105888a27c5de93d02bc
---

# GS-136 1000题B组5.6

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-136_1000题B组5.6.md`
- wrongnet ID：`GS-136`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 恒成立不等式分离参数与端点极限 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 单调性与极值
- 恒成立不等式
- 重要极限

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是分离参数时除以负数未变号或没有取辅助函数上确界，需用户复做确认。

### 方法

- 分离参数
- 构造辅助函数
- 导数判单调
- 端点极限求上确界

### 陷阱

- 除以负数变号
- 开区间端点不能直接取到
- 重要极限 $\frac{e^x-1}{x}$

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先把含 a 项移到一边，并注意除以 2x<0 时不等号变号 |
| missed_action | 旧批量未记录个人步骤；当前复做风险是除以负数不变号或把端点极限当成可取点 |
| related_method_card_id | H05-006 |
| next_reminder | 看到参数恒成立不等式，先分离参数；若除以负量，先变号，再求上确界。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-302_旧批量未记录个人原始错因-当前仅确认复做断点是分离参数时除以负数未变号或]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-130_重要极限]]
- [[MATHWIKI-KNOWLEDGE-254_恒成立不等式]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-1276_端点极限求上确界]]
- [[MATHWIKI-METHOD-CLUSTER-313_分离参数]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-135

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
