---
wiki_id: SRC-WQ-GS-213
type: source_summary
title: "GS-213 2020年第六题：指数因子辅助函数比较"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-213_2020年第六题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-213"
knowledge:
  - "函数单调性"
  - "微分不等式"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是看到 \\(f'(x)>f(x)>0\\) 时没有先构造指数因子辅助函数 \\(f(x)e^{-x}\\)，需用户复做确…"
methods:
  - "指数因子辅助函数"
  - "构造指数因子辅助函数"
  - "导数判单调"
  - "函数值比值比较"
  - "排除选项"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-343_旧批量未记录个人原始错因-当前仅确认复做断点是看到-f'-x-f-x-0"
  - "MATHWIKI-KNOWLEDGE-071_函数单调性"
  - "MATHWIKI-KNOWLEDGE-209_微分不等式"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-1041_排除选项"
  - "MATHWIKI-METHOD-CLUSTER-1128_构造指数因子辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-376_指数因子辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-656_函数值比值比较"
  - "MATHWIKI-GS-METHOD-080_指数因子辅助函数判单调"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-209"
formal_projection_sha256: a37f75ff12c461578f15f7cbe05cf4c29acf596a9edec8bb9a7f09f5d0320824
---

# GS-213 2020年第六题：指数因子辅助函数比较

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-213_2020年第六题.md`
- wrongnet ID：`GS-213`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 高等数学-一元函数微分学应用 |
| 题型 | 导数不等式构造指数因子辅助函数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 函数单调性
- 微分不等式

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是看到 \(f'(x)>f(x)>0\) 时没有先构造指数因子辅助函数 \(f(x)e^{-x}\)，需用户复做确…

### 方法

- 指数因子辅助函数
- 构造指数因子辅助函数
- 导数判单调
- 函数值比值比较
- 排除选项

### 陷阱

- 看到 f'(x)>f(x) 要想到 f(x)e^{-x} 或 f(x)/e^x
- 比较的是 f(k)/f(-1) 与 e 的幂次，不是直接比较 f(k)
- 由辅助函数单调性推出比值方向后，选项 C、D 方向恰好相反

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先写 \(F(x)=f(x)e^{-x}\)，并计算 \(F'(x)=e^{-x}(f'(x)-f(x))\) |
| missed_action | 没有先把 \(f'(x)-f(x)>0\) 转成指数因子辅助函数的单调性 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到 \(f'-f\) 型导数不等式，先乘 \(e^{-x}\) 构造指数因子辅助函数，再比较新函数值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-343_旧批量未记录个人原始错因-当前仅确认复做断点是看到-f'-x-f-x-0]]
- [[MATHWIKI-KNOWLEDGE-071_函数单调性]]
- [[MATHWIKI-KNOWLEDGE-209_微分不等式]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-1041_排除选项]]
- [[MATHWIKI-METHOD-CLUSTER-1128_构造指数因子辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-376_指数因子辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-656_函数值比值比较]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-080_指数因子辅助函数判单调]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-209

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
