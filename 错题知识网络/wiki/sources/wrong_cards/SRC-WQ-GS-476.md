---
wiki_id: SRC-WQ-GS-476
type: source_summary
title: "GS-476 57812 无穷区间费马引理"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-476_57812无穷区间费马引理.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-476_57812-2026.5.19.md"
visual_ids:
  - "VIS-GS-476"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-476/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
identity_peer_refs: []
wrongnet_refs:
  - "GS-476"
related_wrongnet_refs: []
knowledge:
  - "一元函数微分学应用"
  - "中值定理"
  - "费马引理"
  - "最值定理"
  - "函数极限"
error_causes:
  - "题型识别失败"
  - "方法选择错误"
  - "条件转化不足"
  - "证明结构不完整"
methods:
  - "先判型"
  - "极限定义"
  - "闭区间截断"
  - "最值定理"
  - "费马引理"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-011_证明结构不完整"
  - "MATHWIKI-ERROR-CLUSTER-085_条件转化不足"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-KNOWLEDGE-039_函数极限"
  - "MATHWIKI-KNOWLEDGE-152_最值定理"
  - "MATHWIKI-KNOWLEDGE-270_费马引理"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-121_极限定义"
  - "MATHWIKI-METHOD-CLUSTER-1397_闭区间截断"
  - "MATHWIKI-METHOD-CLUSTER-387_最值定理"
  - "MATHWIKI-METHOD-CLUSTER-462_费马引理"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: ec6a1dea8b1728ad55e925d937044320f2e51101957015cec415aae167932ba5
---

# GS-476 57812 无穷区间费马引理

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-476_57812无穷区间费马引理.md`
- wrongnet ID：`GS-476`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-476_57812-2026.5.19.md`（`VIS-GS-476`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 中值定理 |
| 题型 | 无穷区间上的罗尔型结论 |
| 日期 | 2026-05-19 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 中值定理
- 费马引理
- 最值定理
- 函数极限

### 错因

- 题型识别失败
- 方法选择错误
- 条件转化不足
- 证明结构不完整

### 方法

- 先判型
- 极限定义
- 闭区间截断
- 最值定理
- 费马引理

### 陷阱

- 无穷端点
- 极限定义是一整段范围
- 内部极值点
- 端点条件
- 恒等于零特例
- 适用条件

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先判断 \(f\equiv0\) 是否成立；若否，取 \(c\) 使 \(f(c)\ne0\)，再用极限定义选 \(b>c\) |
| missed_action | 没有用 \(\lim_{x\to+\infty}f(x)=0\) 选足够大的 \(b\)，使极值点落在内部 |
| related_method_card_id | H06-004 |
| next_reminder | 看到无穷区间上要证 \(f'(\xi)=0\)，先用极限定义截出有限闭区间，再用最值定理和费马引理。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-011_证明结构不完整]]
- [[MATHWIKI-ERROR-CLUSTER-085_条件转化不足]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-KNOWLEDGE-039_函数极限]]
- [[MATHWIKI-KNOWLEDGE-152_最值定理]]
- [[MATHWIKI-KNOWLEDGE-270_费马引理]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-121_极限定义]]
- [[MATHWIKI-METHOD-CLUSTER-1397_闭区间截断]]
- [[MATHWIKI-METHOD-CLUSTER-387_最值定理]]
- [[MATHWIKI-METHOD-CLUSTER-462_费马引理]]

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
