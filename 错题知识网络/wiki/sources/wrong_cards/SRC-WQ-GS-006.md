---
wiki_id: SRC-WQ-GS-006
type: source_summary
title: "GS-006 1000题基础2.6 103017 2026.5.7"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-006_1000题基础2.61030172026.5.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-006"
knowledge:
  - "极限与连续"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是 n 次根号最大底数主导与绝对值分段，需用户确认是否为当时第一断点"
methods:
  - "分类讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-272_旧批量未记录个人原始错因-当前仅确认复做入口是n次根号最大底数主导与绝对"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-GS-METHOD-008_分类讨论闭环"
status: indexed
last_updated: 2026-07-25
related_wrongnet_refs:
  - "GS-013"
formal_projection_sha256: 3b8f159bdb401837dd89b20b9b145111eb8f8ffc87c44475cb15800955b09c34
---

# GS-006 1000题基础2.6 103017 2026.5.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-006_1000题基础2.61030172026.5.7.md`
- wrongnet ID：`GS-006`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 含参数问题 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是 n 次根号最大底数主导与绝对值分段，需用户确认是否为当时第一断点

### 方法

- 分类讨论

### 陷阱

- 参数边界
- 正负号
- 定义域

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先把根号内写成 \(1^n+(|x|^3)^n\)，比较 \(1\) 与 \(|x|^3\) |
| missed_action | 个人原始漏步未记录；当前只确认复做时必须先做最大项比较和绝对值分段 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到 n 次根号套 n 次幂之和，先改写成底数的 \(n\) 次幂并比较最大底数，再处理绝对值分段。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-272_旧批量未记录个人原始错因-当前仅确认复做入口是n次根号最大底数主导与绝对]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-008_分类讨论闭环]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-013

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
