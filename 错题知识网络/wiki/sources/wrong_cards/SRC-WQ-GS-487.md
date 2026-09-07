---
wiki_id: SRC-WQ-GS-487
type: source_summary
title: "GS-487 102488 正弦级数判敛"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-487_102488正弦级数判敛.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-487_102488-2026.5.21.md"
visual_ids:
  - "VIS-GS-487"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-487/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
identity_peer_refs: []
wrongnet_refs:
  - "GS-487"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "数项级数敛散性判别"
  - "正项级数比较判别法"
  - "极限比较判别法"
  - "p级数"
  - "等价无穷小"
error_causes:
  - "条件忽略"
  - "方法选择错误"
  - "参数范围错误"
methods:
  - "先判型"
  - "小量趋零"
  - "正项前置判断"
  - "正弦等价无穷小"
  - "极限比较判别法"
  - "对数幂比较"
  - "比较判别法"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-036_参数范围错误"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-032_正项级数比较判别法"
  - "MATHWIKI-KNOWLEDGE-036_p级数"
  - "MATHWIKI-KNOWLEDGE-061_极限比较判别法"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-012_比较判别法"
  - "MATHWIKI-METHOD-CLUSTER-033_极限比较判别法"
  - "MATHWIKI-METHOD-CLUSTER-074_正项前置判断"
  - "MATHWIKI-METHOD-CLUSTER-169_正弦等价无穷小"
  - "MATHWIKI-METHOD-CLUSTER-355_对数幂比较"
  - "MATHWIKI-METHOD-CLUSTER-362_小量趋零"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
evidence_status: user_confirmed
question_surface_status: registered
aggregate_edge_policy: allow
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 3bd0972b9d7c85f425eb602adf375dfed4736314f10696aabe3fccac2fe57001
---

# GS-487 102488 正弦级数判敛

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-487_102488正弦级数判敛.md`
- wrongnet ID：`GS-487`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 视觉证据

- 详情页：[[错题知识网络/可视化错题详情/高等数学/GS-487_102488-2026.5.21|VIS-GS-487]]
- visual_id：`VIS-GS-487`
- 题图：`错题知识网络/assets/visual_wrong_questions/GS-487/question_01.png`
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 含三角函数正项级数判敛 |
| 日期 | 2026-05-21 |
| 状态 | 已掌握 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 无穷级数
- 数项级数敛散性判别
- 正项级数比较判别法
- 极限比较判别法
- p级数
- 等价无穷小

### 错因

- 条件忽略
- 方法选择错误
- 参数范围错误

### 方法

- 先判型
- 小量趋零
- 正项前置判断
- 正弦等价无穷小
- 极限比较判别法
- 对数幂比较
- 比较判别法

### 陷阱

- 正项前置判断
- 等价使用条件
- 小量趋零
- 参数边界
- p级数条件
- 对数幂比较

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先令 \(t_n=\frac{\ln n}{n^\alpha}\)，检查 \(t_n\to0\) 且充分大时 \(0<t_n<\frac{\pi}{2}\) |
| missed_action | 没有先补齐等价比较判别法的前置条件，也没有单独检查 \(\alpha=1\) 边界 |
| related_method_card_id | H16-001 |
| next_reminder | 看到 \(\sin t_n\) 型级数，先证明 \(t_n\to0\) 和通项最终同号，再用等价无穷小比较并查边界。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-036_参数范围错误]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-032_正项级数比较判别法]]
- [[MATHWIKI-KNOWLEDGE-036_p级数]]
- [[MATHWIKI-KNOWLEDGE-061_极限比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-033_极限比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-074_正项前置判断]]
- [[MATHWIKI-METHOD-CLUSTER-169_正弦等价无穷小]]
- [[MATHWIKI-METHOD-CLUSTER-355_对数幂比较]]
- [[MATHWIKI-METHOD-CLUSTER-362_小量趋零]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 证据边界

- 个人断点只认“使用正弦等价无穷小前没有检查小量趋零、最终为正与参数边界”；未发现同一正弦级数对象、同一条件检查第一动作且双端均有用户证据的卡片。
- 方法页已按 B5-CHECK 检查断点投影，不再误连到 B4-CHAIN。

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
