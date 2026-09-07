---
wiki_id: SRC-WQ-GS-230
type: source_summary
title: "GS-230 1000题A组8.5"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-230_1000题A组8.5.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-230"
knowledge:
  - "定积分"
  - "变上限积分"
  - "拉格朗日中值定理"
  - "单调性与极值"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是没有先判 \\(g(1/2)<0<g(3/2)\\)，再拆成两个等长区间用拉格朗日中值定理比较绝对值，需用户复做确认。"
methods:
  - "变上限函数求导"
  - "拉格朗日中值定理"
  - "符号判断"
  - "绝对值比较"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-325_旧批量未记录个人原始错因-当前仅确认复做断点是没有先判-g-1-2-0-"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-021_拉格朗日中值定理"
  - "MATHWIKI-METHOD-CLUSTER-014_拉格朗日中值定理"
  - "MATHWIKI-METHOD-CLUSTER-1311_绝对值比较"
  - "MATHWIKI-METHOD-CLUSTER-254_符号判断"
  - "MATHWIKI-METHOD-CLUSTER-330_变上限函数求导"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: b4fadca1eeeec7b51d83fe59d95b4d9d2516a47ef0f7727ddf95848eb51499bb
---

# GS-230 1000题A组8.5

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-230_1000题A组8.5.md`
- wrongnet ID：`GS-230`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 变上限积分值比较 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 变上限积分
- 拉格朗日中值定理
- 单调性与极值

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是没有先判 \(g(1/2)<0<g(3/2)\)，再拆成两个等长区间用拉格朗日中值定理比较绝对值，需用户复做确认。

### 方法

- 变上限函数求导
- 拉格朗日中值定理
- 符号判断
- 绝对值比较

### 陷阱

- 积分上限小于下限时为负
- 两段长度相同
- 递减函数比较中值点

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写 \(g'(x)=f(x)>0\)，并判定 \(g(1/2)<0<g(3/2)\) |
| missed_action | 没有先把左右两侧改写成等长积分/中值点比较 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到变上限积分两侧取点比较，先判符号，再拆成等长区间并用中值点比较函数值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-325_旧批量未记录个人原始错因-当前仅确认复做断点是没有先判-g-1-2-0-]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-021_拉格朗日中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-014_拉格朗日中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-1311_绝对值比较]]
- [[MATHWIKI-METHOD-CLUSTER-254_符号判断]]
- [[MATHWIKI-METHOD-CLUSTER-330_变上限函数求导]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
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
