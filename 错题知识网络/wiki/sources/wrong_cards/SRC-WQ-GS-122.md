---
wiki_id: SRC-WQ-GS-122
type: source_summary
title: "GS-122 57874 2026.4.1"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-122_578742026.4.1.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-122"
knowledge:
  - "一元函数微分学应用"
  - "函数奇偶性与导数性质"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是没有从 $f(x)$ 与 $f(1/x)$ 的互逆结构构造第二方程并联立消元，需用户复做确认。"
methods:
  - "换元构造方程组"
  - "线性方程组消元"
  - "奇偶性定义"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-323_旧批量未记录个人原始错因-当前仅确认复做断点是没有从$f-x-$与$f-"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-108_函数奇偶性与导数性质"
  - "MATHWIKI-METHOD-CLUSTER-1038_换元构造方程组"
  - "MATHWIKI-METHOD-CLUSTER-1305_线性方程组消元"
  - "MATHWIKI-METHOD-CLUSTER-878_奇偶性定义"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-122 57874 2026.4.1

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-122_578742026.4.1.md`
- wrongnet ID：`GS-122`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 函数方程与奇偶性 |
| 题型 | 函数方程求解析式与奇偶性 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 函数奇偶性与导数性质

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是没有从 $f(x)$ 与 $f(1/x)$ 的互逆结构构造第二方程并联立消元，需用户复做确认。

### 方法

- 换元构造方程组
- 线性方程组消元
- 奇偶性定义

### 陷阱

- 没有构造 $x\mapsto1/x$ 的第二方程
- 漏用 $|a|\ne|b|$ 保证分母非零
- 求出表达式后忘记验证奇偶性

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先把原方程中的 $x$ 替换成 $1/x$ 写出第二个方程 |
| missed_action | 旧批量未记录个人步骤；当前复做风险是没有先构造对称方程组，或求出表达式后忘记验证奇偶性 |
| related_method_card_id | H00-012 |
| next_reminder | 看到 $f(x)$ 与 $f(1/x)$ 同现，先代 $1/x$ 构造第二方程，再联立消元。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-323_旧批量未记录个人原始错因-当前仅确认复做断点是没有从$f-x-$与$f-]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-108_函数奇偶性与导数性质]]
- [[MATHWIKI-METHOD-CLUSTER-1038_换元构造方程组]]
- [[MATHWIKI-METHOD-CLUSTER-1305_线性方程组消元]]
- [[MATHWIKI-METHOD-CLUSTER-878_奇偶性定义]]

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
