---
wiki_id: SRC-WQ-GS-283
type: source_summary
title: "GS-283 强化例题9.16（19906）2026.5.6"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-283_强化例题9.16（19906）2026.5.6.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-283"
knowledge:
  - "定积分"
  - "变上限积分"
  - "反函数"
  - "第一类换元"
  - "不定积分"
error_causes:
  - "方法选择错误"
  - "动作链断裂"
  - "收尾验证遗漏"
  - "函数自变量识别混淆"
methods:
  - "换元"
  - "变上限积分求导"
  - "反函数复合消去"
  - "由导数还原原函数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-032_收尾验证遗漏"
  - "MATHWIKI-ERROR-CLUSTER-042_函数自变量识别混淆"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-171_反函数"
  - "MATHWIKI-METHOD-CLUSTER-009_换元"
  - "MATHWIKI-METHOD-CLUSTER-015_变上限积分求导"
  - "MATHWIKI-METHOD-CLUSTER-1209_由导数还原原函数"
  - "MATHWIKI-METHOD-CLUSTER-779_反函数复合消去"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-283 强化例题9.16（19906）2026.5.6

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-283_强化例题9.16（19906）2026.5.6.md`
- wrongnet ID：`GS-283`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 变上限积分反函数综合 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 变上限积分
- 反函数
- 第一类换元
- 不定积分

### 错因

- 方法选择错误
- 动作链断裂
- 收尾验证遗漏
- 函数自变量识别混淆

### 方法

- 换元
- 变上限积分求导
- 反函数复合消去
- 由导数还原原函数

### 陷阱

- 被积函数含参
- 反函数复合
- 求导后积分还原
- 积分常数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先令 \(u=t-x\)，把积分化为 \(\int_0^{f(x)} g(u)\,du\) |
| missed_action | 没有先换元消掉被积函数中的 \(x\)，也没有在求出 \(f'(x)\) 后积分还原 \(f(x)\) |
| related_method_card_id | 待匹配 |
| next_reminder | 看到变上限积分里出现 \(t-x\)，先令 \(u=t-x\) 消掉参数，再求导并用反函数关系收口。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-032_收尾验证遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-042_函数自变量识别混淆]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-171_反函数]]
- [[MATHWIKI-METHOD-CLUSTER-009_换元]]
- [[MATHWIKI-METHOD-CLUSTER-015_变上限积分求导]]
- [[MATHWIKI-METHOD-CLUSTER-1209_由导数还原原函数]]
- [[MATHWIKI-METHOD-CLUSTER-779_反函数复合消去]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-083
- GS-332
- GS-336
- GS-157

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
