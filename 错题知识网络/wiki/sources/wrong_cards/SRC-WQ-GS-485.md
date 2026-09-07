---
wiki_id: SRC-WQ-GS-485
type: source_summary
title: "GS-485 102454 单调错位比较"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-485_102454单调错位比较.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-485_102454-2026.5.21.md"
visual_ids:
  - "VIS-GS-485"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-485/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
identity_peer_refs: []
wrongnet_refs:
  - "GS-485"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "数项级数敛散性判别"
  - "正项级数敛散性判别"
  - "正项级数比较判别法"
error_causes:
  - "方法选择错误"
  - "概念混淆"
  - "符号错误"
methods:
  - "先判型"
  - "比较判别法"
  - "单调性比较"
  - "错位比较"
  - "有限项不影响敛散性"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-019_符号错误"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-032_正项级数比较判别法"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-012_比较判别法"
  - "MATHWIKI-METHOD-CLUSTER-111_单调性比较"
  - "MATHWIKI-METHOD-CLUSTER-1395_错位比较"
  - "MATHWIKI-METHOD-CLUSTER-236_有限项不影响敛散性"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: user_confirmed
question_surface_status: registered
aggregate_edge_policy: allow
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: a6051cc62609918ec84c4fc2909f3168d347bc3a84ca1c3fc14c7f5950b69af5
---

# GS-485 102454 单调错位比较

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-485_102454单调错位比较.md`
- wrongnet ID：`GS-485`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 视觉证据

- 详情页：[[错题知识网络/可视化错题详情/高等数学/GS-485_102454-2026.5.21|VIS-GS-485]]
- visual_id：`VIS-GS-485`
- 题图：`错题知识网络/assets/visual_wrong_questions/GS-485/question_01.png`
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 正项级数比较判别 |
| 日期 | 2026-05-21 |
| 状态 | 已掌握 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 无穷级数
- 数项级数敛散性判别
- 正项级数敛散性判别
- 正项级数比较判别法

### 错因

- 方法选择错误
- 概念混淆
- 符号错误

### 方法

- 先判型
- 比较判别法
- 单调性比较
- 错位比较
- 有限项不影响敛散性

### 陷阱

- 比较方向错误
- 通项相乘误判
- 错位一项
- 有限项不影响敛散性
- 比较对象选择

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先由 \(u_{n+1}\le u_n\) 写出 \(u_{n+1}\le\sqrt{u_nu_{n+1}}\le u_n\) |
| missed_action | 没有先确定比较方向，误把通项乘积关系当成目标级数收敛关系 |
| related_method_card_id | H16-001 |
| next_reminder | 看到 \(\sqrt{u_nu_{n+1}}\) 和单调性，先写夹在中间的不等式，再用 \(\sum u_{n+1}\) 与 \(\sum u_n\) 只差有限项。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-019_符号错误]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-032_正项级数比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-111_单调性比较]]
- [[MATHWIKI-METHOD-CLUSTER-1395_错位比较]]
- [[MATHWIKI-METHOD-CLUSTER-236_有限项不影响敛散性]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 证据边界

- 个人断点只认“没有先用单调性写出相邻项几何平均的正确夹逼方向，并把乘积通项与目标级数混淆”；未发现同对象、同第一动作且双端均有用户证据的卡片。
- 相似的正项级数比较标签不单独构成强边。

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
