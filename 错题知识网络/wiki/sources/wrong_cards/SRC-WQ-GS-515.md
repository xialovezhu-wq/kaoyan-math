---
wiki_id: SRC-WQ-GS-515
type: source_summary
title: "GS-515 170678 一阶线性微分不等式积分因子 2026.5.29"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-515_170678一阶线性微分不等式积分因子.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-515_170678-2026.5.29.md"
visual_ids:
  - "VIS-GS-515"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-515/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
wrongnet_refs:
  - "GS-515"
related_wrongnet_refs:
  - "GS-488"
knowledge:
  - "一元函数微分学应用"
  - "微分不等式"
  - "辅助函数构造"
  - "积分因子"
  - "一阶线性微分方程"
error_causes:
  - "题型识别失败"
  - "方法选择错误"
  - "复习记忆不牢"
methods:
  - "先判型"
  - "构造辅助函数"
  - "积分因子"
  - "特殊值法"
  - "导数判单调"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-017_复习记忆不牢"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-065_一阶线性微分方程"
  - "MATHWIKI-KNOWLEDGE-076_辅助函数构造"
  - "MATHWIKI-KNOWLEDGE-126_积分因子"
  - "MATHWIKI-KNOWLEDGE-209_微分不等式"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-061_积分因子"
  - "MATHWIKI-METHOD-CLUSTER-1196_特殊值法"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: "user_confirmed"
question_surface_status: "registered"
aggregate_edge_policy: "allow"
evidence_boundary: "个人错因仅来自正式卡 dated wrong_history；详情解析只核验题面与解法，不反推个人错因。"
review_batch: MATHWIKI-REVIEW-070
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: f75939d78d23e8066848eb48b4c44bd00216ba934db75f70ecda8adef6e3e360
---

# GS-515 170678 一阶线性微分不等式积分因子 2026.5.29

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-515_170678一阶线性微分不等式积分因子.md`
- wrongnet ID：`GS-515`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-515_170678-2026.5.29.md`（`VIS-GS-515`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 微分不等式与函数值大小比较 |
| 日期 | 2026-05-29 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 微分不等式
- 辅助函数构造
- 积分因子
- 一阶线性微分方程

### 错因

- 题型识别失败
- 方法选择错误
- 复习记忆不牢

### 方法

- 先判型
- 构造辅助函数
- 积分因子
- 特殊值法
- 导数判单调

### 陷阱

- f符号未知不能直接判f'正负
- 积分因子e指数恒正
- 选择题漏用特殊值法

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先取 \(\mu(x)=e^{-\int_0^x p(t)\,dt}\)，写 \((\mu f)'=\mu\,[f'-pf]>0\)，再由 \(\mu f\) 递增还原 \(f\) 的大小。 |
| missed_action | 没有把 \(f'-pf\) 反向凑成积分因子乘积导数，误想直接从不等式推出 \(f'>0\)。 |
| related_method_card_id | H15-005 |
| next_reminder | 看到 \(f'-pf\) 或 \(y'+P(x)y\)，先写积分因子；微分不等式也按一阶线性方程反向凑导数。 |
| evidence_origin | user_confirmed |
| repeat_count | 1 |
| repeat_count_source | wrong_history |

## 证据边界

- 个人错因仅来自正式卡 dated `wrong_history`；详情解析只核验题面与解法，不反推个人错因。
- 题图或解析图存在，只证明视觉来源已注册，不单独证明个人作答过程、错误次数或掌握度。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-017_复习记忆不牢]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-065_一阶线性微分方程]]
- [[MATHWIKI-KNOWLEDGE-076_辅助函数构造]]
- [[MATHWIKI-KNOWLEDGE-126_积分因子]]
- [[MATHWIKI-KNOWLEDGE-209_微分不等式]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-061_积分因子]]
- [[MATHWIKI-METHOD-CLUSTER-1196_特殊值法]]
- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- [[错题知识网络/错题卡/GS-488_57892指数因子罗尔|GS-488]]

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
