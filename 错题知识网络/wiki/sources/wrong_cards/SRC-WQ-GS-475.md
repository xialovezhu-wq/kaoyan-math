---
wiki_id: SRC-WQ-GS-475
type: source_summary
title: "GS-475 57802 罗尔积分因子"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-475_57802罗尔积分因子.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-475_57802-2026.5.19.md"
visual_ids:
  - "VIS-GS-475"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-475/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
identity_peer_refs: []
wrongnet_refs:
  - "GS-475"
related_wrongnet_refs:
  - "GS-474"
knowledge:
  - "中值定理"
  - "罗尔定理"
  - "一元函数微分学应用"
  - "辅助函数构造"
  - "积分因子"
error_causes:
  - "题型识别失败"
  - "方法选择错误"
  - "证明结构不完整"
  - "过程跳步"
methods:
  - "先判型"
  - "构造辅助函数"
  - "罗尔定理"
  - "反向构造"
  - "积分因子"
  - "乘积求导"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-011_证明结构不完整"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-KNOWLEDGE-063_罗尔定理"
  - "MATHWIKI-KNOWLEDGE-076_辅助函数构造"
  - "MATHWIKI-KNOWLEDGE-126_积分因子"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-045_罗尔定理"
  - "MATHWIKI-METHOD-CLUSTER-046_乘积求导"
  - "MATHWIKI-METHOD-CLUSTER-061_积分因子"
  - "MATHWIKI-METHOD-CLUSTER-068_反向构造"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: fd614ad870649225a882e3f7379442ec3ae8190fe254ed43ccdc9c0968947e13
---

# GS-475 57802 罗尔积分因子

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-475_57802罗尔积分因子.md`
- wrongnet ID：`GS-475`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-475_57802-2026.5.19.md`（`VIS-GS-475`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 中值定理 |
| 题型 | 罗尔定理辅助函数构造 |
| 日期 | 2026-05-19 |
| 状态 | 已掌握 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 中值定理
- 罗尔定理
- 一元函数微分学应用
- 辅助函数构造
- 积分因子

### 错因

- 题型识别失败
- 方法选择错误
- 证明结构不完整
- 过程跳步

### 方法

- 先判型
- 构造辅助函数
- 罗尔定理
- 反向构造
- 积分因子
- 乘积求导

### 陷阱

- 辅助函数入口
- 端点条件
- 指数因子
- 非零因子
- 适用条件

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把目标式写成 \(af(x)+(x-b)f'(x)=0\)，再反推 \(F(x)=(b-x)^a f(x)\) |
| missed_action | 没有从目标等式反推乘子 \((b-x)^a\)，只停留在“要用罗尔定理” |
| related_method_card_id | H06-002 |
| next_reminder | 看到 \(af+(x-b)f'=0\)，先把它改写成 \((m(x)f(x))'=0\) 的目标，再试 \(F(x)=(b-x)^a f(x)\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-011_证明结构不完整]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-KNOWLEDGE-063_罗尔定理]]
- [[MATHWIKI-KNOWLEDGE-076_辅助函数构造]]
- [[MATHWIKI-KNOWLEDGE-126_积分因子]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-045_罗尔定理]]
- [[MATHWIKI-METHOD-CLUSTER-046_乘积求导]]
- [[MATHWIKI-METHOD-CLUSTER-061_积分因子]]
- [[MATHWIKI-METHOD-CLUSTER-068_反向构造]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-474

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
