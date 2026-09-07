---
wiki_id: SRC-WQ-GS-221
type: source_summary
title: "GS-221 1000题B组6.14"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-221_1000题B组6.14.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-221"
knowledge:
  - "一元函数微分学应用"
  - "凹凸性与拐点"
  - "二阶导数判凹凸性"
  - "数列极限"
  - "单调有界准则"
  - "费马定理"
error_causes:
  - "题型识别失败"
  - "证明结构不完整"
  - "方法选择错误"
  - "概念混淆"
methods:
  - "单调有界准则"
  - "二阶导判凹凸性"
  - "费马定理"
  - "导数单调零点唯一"
  - "连续性传递"
  - "构造辅助函数"
  - "先判型"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-011_证明结构不完整"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-018_凹凸性与拐点"
  - "MATHWIKI-KNOWLEDGE-098_二阶导数判凹凸性"
  - "MATHWIKI-KNOWLEDGE-109_单调有界准则"
  - "MATHWIKI-KNOWLEDGE-187_费马定理"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-010_单调有界准则"
  - "MATHWIKI-METHOD-CLUSTER-089_二阶导判凹凸性"
  - "MATHWIKI-METHOD-CLUSTER-1354_连续性传递"
  - "MATHWIKI-METHOD-CLUSTER-180_费马定理"
  - "MATHWIKI-METHOD-CLUSTER-941_导数单调零点唯一"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: efdc86353469f43fe2fcff998bcb64961607ead48e5b4ea610c5f7e774086eed
---

# GS-221 1000题B组6.14

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-221_1000题B组6.14.md`
- wrongnet ID：`GS-221`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 数列极限存在性证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 凹凸性与拐点
- 二阶导数判凹凸性
- 数列极限
- 单调有界准则
- 费马定理

### 错因

- 题型识别失败
- 证明结构不完整
- 方法选择错误
- 概念混淆

### 方法

- 单调有界准则
- 二阶导判凹凸性
- 费马定理
- 导数单调零点唯一
- 连续性传递
- 构造辅助函数
- 先判型

### 陷阱

- 单调有界准则遗漏
- 导数零点唯一
- 导数值与函数值混淆
- 上界构造
- 适用条件

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先比较 \(f'(x_{n+1})=\frac{M}{n+1}<\frac{M}{n}=f'(x_n)\)，结合 \(f'\) 严格递减推出 \(x_n<x_{n+1}\)。 |
| missed_action | 没有先把 \(f'(x_n)=\frac{M}{n}\) 当作单调性信息使用，而误按 \(x_{n+1}=f(x_n)\) 的压缩映射模板。 |
| related_method_card_id | H06-001 |
| next_reminder | 看到 \(f'(x_n)=M/n\) 且 \(f''<0\)，先用 \(f'\) 严格递减把导数值大小转成 \(x_n\) 单调，再找上界并用单调有界准则收敛。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-011_证明结构不完整]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-018_凹凸性与拐点]]
- [[MATHWIKI-KNOWLEDGE-098_二阶导数判凹凸性]]
- [[MATHWIKI-KNOWLEDGE-109_单调有界准则]]
- [[MATHWIKI-KNOWLEDGE-187_费马定理]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-010_单调有界准则]]
- [[MATHWIKI-METHOD-CLUSTER-089_二阶导判凹凸性]]
- [[MATHWIKI-METHOD-CLUSTER-1354_连续性传递]]
- [[MATHWIKI-METHOD-CLUSTER-180_费马定理]]
- [[MATHWIKI-METHOD-CLUSTER-941_导数单调零点唯一]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
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
