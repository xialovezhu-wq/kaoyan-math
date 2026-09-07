---
wiki_id: SRC-WQ-GS-047
type: source_summary
title: "GS-047 强化例题13.10"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-047_强化例题13.10.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-047"
knowledge:
  - "多元函数极限"
  - "多元函数连续可微"
  - "可微定义"
  - "多元函数偏导"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是连续性、偏导和可微性要分开按定义检查，尤其偏导存在后仍需检验 \\(\\Delta f/\\rho\\)，需用户复做确认…"
methods:
  - "取绝对值"
  - "有界性放缩"
  - "偏导定义"
  - "可微定义"
  - "特殊路径"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-297_旧批量未记录个人原始错因-当前仅确认复做入口是连续性、偏导和可微性要分开"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-037_多元函数连续可微"
  - "MATHWIKI-KNOWLEDGE-067_多元函数极限"
  - "MATHWIKI-KNOWLEDGE-072_可微定义"
  - "MATHWIKI-METHOD-CLUSTER-022_特殊路径"
  - "MATHWIKI-METHOD-CLUSTER-029_偏导定义"
  - "MATHWIKI-METHOD-CLUSTER-030_取绝对值"
  - "MATHWIKI-METHOD-CLUSTER-031_有界性放缩"
  - "MATHWIKI-METHOD-CLUSTER-041_可微定义"
  - "MATHWIKI-GS-METHOD-050_二元函数性质定义判别链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-047 强化例题13.10

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-047_强化例题13.10.md`
- wrongnet ID：`GS-047`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 多元函数连续与可微判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数极限
- 多元函数连续可微
- 可微定义
- 多元函数偏导

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是连续性、偏导和可微性要分开按定义检查，尤其偏导存在后仍需检验 \(\Delta f/\rho\)，需用户复做确认…

### 方法

- 取绝对值
- 有界性放缩
- 偏导定义
- 可微定义
- 特殊路径

### 陷阱

- 偏导存在不代表可微
- 小o余项检查
- 路径检验

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先用 \(|f(x,y)|\le |y|\) 判连续，再算原点偏导，最后检查 \(|\Delta f|/\rho\) 并用 \(\Delta y=\Delta x\) 反证可微。 |
| missed_action | 个人原始作答未记录；当前只把题图解析确认的性质分层检查链登记为复做检查点。 |
| related_method_card_id | H13-005 |
| next_reminder | 多元函数性质判断要分层：连续、偏导、可微分别查，偏导存在不能直接推出可微。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-297_旧批量未记录个人原始错因-当前仅确认复做入口是连续性、偏导和可微性要分开]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-037_多元函数连续可微]]
- [[MATHWIKI-KNOWLEDGE-067_多元函数极限]]
- [[MATHWIKI-KNOWLEDGE-072_可微定义]]
- [[MATHWIKI-METHOD-CLUSTER-022_特殊路径]]
- [[MATHWIKI-METHOD-CLUSTER-029_偏导定义]]
- [[MATHWIKI-METHOD-CLUSTER-030_取绝对值]]
- [[MATHWIKI-METHOD-CLUSTER-031_有界性放缩]]
- [[MATHWIKI-METHOD-CLUSTER-041_可微定义]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-050_二元函数性质定义判别链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-350

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
