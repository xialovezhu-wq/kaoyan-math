---
wiki_id: SRC-WQ-GS-149
type: source_summary
title: "GS-149 2019年数2（6） 二阶接触与曲率相等充分必要判断"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-149_2019年数2（6）.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-149"
knowledge:
  - "曲率"
  - "泰勒公式"
  - "充分必要条件判断"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是把充分性成立误当充分必要，没有单独检查反向漏洞，需用户复做确认。"
methods:
  - "二阶泰勒展开"
  - "曲率公式"
  - "充分必要性分向验证"
  - "反例构造"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-008_B6-CLOSE"
  - "MATHWIKI-ERROR-CLUSTER-317_旧批量未记录个人原始错因-当前仅确认复做断点是把充分性成立误当充分必要-"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-KNOWLEDGE-094_曲率"
  - "MATHWIKI-KNOWLEDGE-232_充分必要条件判断"
  - "MATHWIKI-METHOD-CLUSTER-096_曲率公式"
  - "MATHWIKI-METHOD-CLUSTER-569_二阶泰勒展开"
  - "MATHWIKI-METHOD-CLUSTER-614_充分必要性分向验证"
  - "MATHWIKI-METHOD-CLUSTER-775_反例构造"
  - "MATHWIKI-GS-METHOD-066_二阶接触曲率充分必要判断"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: 83d4eb20f0045c3c6019b3d50c2632cfc454d47d5a43e25787c7d721400a1b3d
---

# GS-149 2019年数2（6） 二阶接触与曲率相等充分必要判断

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-149_2019年数2（6）.md`
- wrongnet ID：`GS-149`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 曲率相等的充分必要判断 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 曲率
- 泰勒公式
- 充分必要条件判断

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是把充分性成立误当充分必要，没有单独检查反向漏洞，需用户复做确认。

### 方法

- 二阶泰勒展开
- 曲率公式
- 充分必要性分向验证
- 反例构造

### 陷阱

- 充分性成立不代表必要性成立
- 曲率相等只推出二阶导绝对值相等
- \(f''(a)=-g''(a)\ne0\) 时曲率可相等，但极限不为 0

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B6-CLOSE |
| expected_first_action | 先令 F=f-g 并写二阶 Taylor 展开 |
| missed_action | 旧批量未记录个人步骤；当前复做风险是只证 A=>B，没有单独检查 B=>A |
| related_method_card_id | 待匹配 |
| next_reminder | 看到充分必要判断，先拆 A=>B 和 B=>A；证完正向后必须单独找反向漏洞。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-008_B6-CLOSE]]
- [[MATHWIKI-ERROR-CLUSTER-317_旧批量未记录个人原始错因-当前仅确认复做断点是把充分性成立误当充分必要-]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-KNOWLEDGE-094_曲率]]
- [[MATHWIKI-KNOWLEDGE-232_充分必要条件判断]]
- [[MATHWIKI-METHOD-CLUSTER-096_曲率公式]]
- [[MATHWIKI-METHOD-CLUSTER-569_二阶泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-614_充分必要性分向验证]]
- [[MATHWIKI-METHOD-CLUSTER-775_反例构造]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-066_二阶接触曲率充分必要判断]]
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
