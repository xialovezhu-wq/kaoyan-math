---
wiki_id: SRC-WQ-GS-212
type: source_summary
title: "GS-212 1000题B组6.5"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-212_1000题B组6.5.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-212"
knowledge:
  - "一元函数微分学应用"
  - "凹凸性与拐点"
  - "中值定理"
  - "泰勒公式"
error_causes:
  - "旧批量导入未记录用户个人错因；本轮仅按题图、解析入口和方法页确认“正函数取对数转对数凹性”的复做断点，待用户复做后确认实际漏点。"
methods:
  - "取对数"
  - "凹函数切线估计"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-264_旧批量导入未记录用户个人错因-本轮仅按题图、解析入口和方法页确认“正函数"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-KNOWLEDGE-018_凹凸性与拐点"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-019_取对数"
  - "MATHWIKI-METHOD-CLUSTER-652_凹函数切线估计"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-212 1000题B组6.5

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-212_1000题B组6.5.md`
- wrongnet ID：`GS-212`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 对数凹性不等式证明 |
| 日期 | &id001 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 凹凸性与拐点
- 中值定理
- 泰勒公式

### 错因

- 旧批量导入未记录用户个人错因；本轮仅按题图、解析入口和方法页确认“正函数取对数转对数凹性”的复做断点，待用户复做后确认实际漏点。

### 方法

- 取对数
- 凹函数切线估计
- 条件转化

### 陷阱

- 正函数取对数条件
- 极值点导数为零
- 二阶导符号

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先令 F=ln f，并计算 F 的二阶导数符号 |
| missed_action | 没有先把题设不等式转成 (ln f) 的二阶导数小于 0 |
| related_method_card_id | H06-008 |
| next_reminder | 看到正函数和 f、f''、f'''' 的乘法型不等式，先取对数并计算 (ln f) 的二阶导数，再判断凹凸性。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-264_旧批量导入未记录用户个人错因-本轮仅按题图、解析入口和方法页确认“正函数]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-KNOWLEDGE-018_凹凸性与拐点]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-019_取对数]]
- [[MATHWIKI-METHOD-CLUSTER-652_凹函数切线估计]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
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
