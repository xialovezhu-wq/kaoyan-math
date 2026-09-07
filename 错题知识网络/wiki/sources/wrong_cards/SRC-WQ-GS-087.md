---
wiki_id: SRC-WQ-GS-087
type: source_summary
title: "GS-087 强化例题3.2 极限量级判可导"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-087_强化例题3.2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-087"
knowledge:
  - "导数定义"
  - "导数定义型极限"
  - "无穷小阶数比较"
  - "极限条件反推导数"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是极限量级条件未先转回导数定义差商并核查 f(0)，需用户复做确认。"
methods:
  - "导数定义"
  - "差商转化"
  - "极限量级比较"
  - "反例排除"
  - "连续性推出函数值"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-322_旧批量未记录个人原始错因-当前仅确认复做断点是极限量级条件未先转回导数定"
  - "MATHWIKI-KNOWLEDGE-006_导数定义"
  - "MATHWIKI-KNOWLEDGE-051_无穷小阶数比较"
  - "MATHWIKI-KNOWLEDGE-143_导数定义型极限"
  - "MATHWIKI-KNOWLEDGE-153_极限条件反推导数"
  - "MATHWIKI-METHOD-CLUSTER-013_导数定义"
  - "MATHWIKI-METHOD-CLUSTER-067_反例排除"
  - "MATHWIKI-METHOD-CLUSTER-1122_极限量级比较"
  - "MATHWIKI-METHOD-CLUSTER-1355_连续性推出函数值"
  - "MATHWIKI-METHOD-CLUSTER-960_差商转化"
  - "MATHWIKI-GS-METHOD-013_导数定义差商入口"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-087 强化例题3.2 极限量级判可导

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-087_强化例题3.2.md`
- wrongnet ID：`GS-087`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 导数定义 |
| 题型 | 导数定义型极限命题判断 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 导数定义
- 导数定义型极限
- 无穷小阶数比较
- 极限条件反推导数

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是极限量级条件未先转回导数定义差商并核查 f(0)，需用户复做确认。

### 方法

- 导数定义
- 差商转化
- 极限量级比较
- 反例排除
- 连续性推出函数值

### 陷阱

- 由可导反推极限时，若不能确定 f(0)=0，分子不一定趋于 0
- 0 乘无穷大量不能直接判为 0
- 比 x^2 高阶能推出导数为 0，但比三次根号高阶不能直接推出可导

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先写 f'(0)=lim [f(x)-f(0)]/x，并逐项判断题设是否能确定 f(0)=0 |
| missed_action | 旧批量未记录个人步骤；当前复做风险是直接把给定比值当作导数定义差商 |
| related_method_card_id | H03-003 |
| next_reminder | 看到极限条件推出可导，先写导数定义差商，再查 f(0) 和分母阶数是否匹配。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-322_旧批量未记录个人原始错因-当前仅确认复做断点是极限量级条件未先转回导数定]]
- [[MATHWIKI-KNOWLEDGE-006_导数定义]]
- [[MATHWIKI-KNOWLEDGE-051_无穷小阶数比较]]
- [[MATHWIKI-KNOWLEDGE-143_导数定义型极限]]
- [[MATHWIKI-KNOWLEDGE-153_极限条件反推导数]]
- [[MATHWIKI-METHOD-CLUSTER-013_导数定义]]
- [[MATHWIKI-METHOD-CLUSTER-067_反例排除]]
- [[MATHWIKI-METHOD-CLUSTER-1122_极限量级比较]]
- [[MATHWIKI-METHOD-CLUSTER-1355_连续性推出函数值]]
- [[MATHWIKI-METHOD-CLUSTER-960_差商转化]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-013_导数定义差商入口]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-099
- GS-458
- GS-091
- GS-093
- GS-104

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
