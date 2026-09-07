---
wiki_id: SRC-WQ-GS-483
type: source_summary
title: "GS-483 102436 对数裂项判敛散"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-483_102436对数裂项判敛散.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-483_102436-2026.5.21.md"
visual_ids:
  - "VIS-GS-483"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-483/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
identity_peer_refs: []
wrongnet_refs:
  - "GS-483"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "数项级数敛散性判别"
  - "正项级数敛散性判别"
  - "部分和数列"
  - "调和级数"
error_causes:
  - "审题遗漏"
  - "概念混淆"
  - "方法选择错误"
methods:
  - "先判型"
  - "对数裂项"
  - "裂项相消"
  - "部分和定义"
  - "比较判别法"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-008_B6-CLOSE"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-037_审题遗漏"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-097_调和级数"
  - "MATHWIKI-KNOWLEDGE-129_部分和数列"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-012_比较判别法"
  - "MATHWIKI-METHOD-CLUSTER-133_部分和定义"
  - "MATHWIKI-METHOD-CLUSTER-259_裂项相消"
  - "MATHWIKI-METHOD-CLUSTER-357_对数裂项"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
evidence_status: user_confirmed
question_surface_status: registered
aggregate_edge_policy: allow
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 8fc5d6b47dadedb7181f7d58935d6867c99d90b3ca2f90f2178daba6cdea6b17
---

# GS-483 102436 对数裂项判敛散

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-483_102436对数裂项判敛散.md`
- wrongnet ID：`GS-483`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 视觉证据

- 详情页：[[错题知识网络/可视化错题详情/高等数学/GS-483_102436-2026.5.21|VIS-GS-483]]
- visual_id：`VIS-GS-483`
- 题图：`错题知识网络/assets/visual_wrong_questions/GS-483/question_01.png`
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 正项级数敛散性判别 |
| 日期 | 2026-05-21 |
| 状态 | 已掌握 |
| 优先级 | B |
| 难度 | 2 |

## 可编译信息

### 知识点

- 无穷级数
- 数项级数敛散性判别
- 正项级数敛散性判别
- 部分和数列
- 调和级数

### 错因

- 审题遗漏
- 概念混淆
- 方法选择错误

### 方法

- 先判型
- 对数裂项
- 裂项相消
- 部分和定义
- 比较判别法

### 陷阱

- 选项条件混淆
- 部分和极限
- 对数裂项入口
- 导数趋零误判
- 正项级数入口

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B6-CLOSE |
| expected_first_action | 先写 \(\ln(1+\frac1n)=\ln(n+1)-\ln n\)，并计算部分和 \(S_n=\ln(n+1)\)。 |
| missed_action | 已算到 \(S_n=\ln(n+1)\) 后，没有回到级数敛散性目标判断 \(S_n\to+\infty\)，反而误用函数导数趋零判断收敛。 |
| related_method_card_id | H16-004 |
| next_reminder | 看到对数裂项级数，先算部分和，再看部分和极限是否有限；不要用导数趋零代替级数判敛。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-008_B6-CLOSE]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-037_审题遗漏]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-097_调和级数]]
- [[MATHWIKI-KNOWLEDGE-129_部分和数列]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-133_部分和定义]]
- [[MATHWIKI-METHOD-CLUSTER-259_裂项相消]]
- [[MATHWIKI-METHOD-CLUSTER-357_对数裂项]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 证据边界

- 个人断点只认“把选项中的敛散结论误读为已知条件，算出对数裂项部分和后也未检查其极限是否有限”；未发现同对象、同判断动作且双端均有用户证据的卡片。
- 相似的裂项或正项级数标签不单独构成强边。

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
