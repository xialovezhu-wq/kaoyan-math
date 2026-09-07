---
wiki_id: SRC-WQ-GS-615
type: source_summary
title: "GS-615 78157 正弦展开奇延拓取值 2026.6.23"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-615_78157正弦展开奇延拓取值.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-615"
knowledge:
  - "无穷级数"
  - "傅里叶级数"
  - "傅里叶系数"
  - "正弦级数"
  - "半区间正弦展开"
  - "周期奇延拓"
  - "狄利克雷收敛定理"
error_causes:
  - "题型识别失败"
  - "方法选择错误"
  - "函数对象混淆"
  - "条件忽略"
  - "过程跳步"
methods:
  - "先判型"
  - "半区间正弦展开识别"
  - "傅里叶展开对象识别"
  - "周期奇延拓"
  - "周期性判断"
  - "奇性判断"
  - "狄利克雷收敛定理"
  - "连续点取函数值"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-130_函数对象混淆"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-136_傅里叶级数"
  - "MATHWIKI-KNOWLEDGE-164_傅里叶系数"
  - "MATHWIKI-KNOWLEDGE-215_狄利克雷收敛定理"
  - "MATHWIKI-KNOWLEDGE-317_半区间正弦展开"
  - "MATHWIKI-KNOWLEDGE-326_周期奇延拓"
  - "MATHWIKI-KNOWLEDGE-395_正弦级数"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-1359_连续点取函数值"
  - "MATHWIKI-METHOD-CLUSTER-193_傅里叶展开对象识别"
  - "MATHWIKI-METHOD-CLUSTER-215_周期性判断"
  - "MATHWIKI-METHOD-CLUSTER-432_狄利克雷收敛定理"
  - "MATHWIKI-METHOD-CLUSTER-722_半区间正弦展开识别"
  - "MATHWIKI-METHOD-CLUSTER-830_周期奇延拓"
  - "MATHWIKI-METHOD-CLUSTER-881_奇性判断"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-068_傅里叶展开对象识别与点值求和"
  - "MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线"
status: indexed
last_updated: 2026-07-25
related_wrongnet_refs: []
formal_projection_sha256: ad1cfb78d4859ca90d5dc7088513a30b55f7edd81ff8a8759f92d08f34de49d0
---

# GS-615 78157 正弦展开奇延拓取值 2026.6.23

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-615_78157正弦展开奇延拓取值.md`
- wrongnet ID：`GS-615`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 半区间正弦展开与奇延拓求级数值 |
| 日期 | 2026-06-23 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 无穷级数
- 傅里叶级数
- 傅里叶系数
- 正弦级数
- 半区间正弦展开
- 周期奇延拓
- 狄利克雷收敛定理

### 错因

- 题型识别失败
- 方法选择错误
- 函数对象混淆
- 条件忽略
- 过程跳步

### 方法

- 先判型
- 半区间正弦展开识别
- 傅里叶展开对象识别
- 周期奇延拓
- 周期性判断
- 奇性判断
- 狄利克雷收敛定理
- 连续点取函数值

### 陷阱

- 不要先算傅里叶系数
- 正弦级数对应奇延拓
- 周期为2
- 小f只在(0,1)上定义
- 大F是周期奇延拓函数
- 连续点取函数值

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先令 \(L=1\)，判断这是半区间正弦展开并构造周期为 2 的奇延拓 \(F(x)\) |
| missed_action | 没有立刻把题目给的 \(b_n\) 看成奇延拓函数 \(F(x)\) 的傅里叶正弦系数，也没有先区分小 \(f(x)\)、大 \(F(x)\) 与级数和 \(S(x)\)。 |
| related_method_card_id | H16-024 |
| next_reminder | 看到 \(2\int_0^1 f(x)\sin(n\pi x)\,dx\)，先想半区间正弦展开，不要先算积分；正弦展开对应奇延拓，周期是 \(2L\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-130_函数对象混淆]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-136_傅里叶级数]]
- [[MATHWIKI-KNOWLEDGE-164_傅里叶系数]]
- [[MATHWIKI-KNOWLEDGE-215_狄利克雷收敛定理]]
- [[MATHWIKI-KNOWLEDGE-317_半区间正弦展开]]
- [[MATHWIKI-KNOWLEDGE-326_周期奇延拓]]
- [[MATHWIKI-KNOWLEDGE-395_正弦级数]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-1359_连续点取函数值]]
- [[MATHWIKI-METHOD-CLUSTER-193_傅里叶展开对象识别]]
- [[MATHWIKI-METHOD-CLUSTER-215_周期性判断]]
- [[MATHWIKI-METHOD-CLUSTER-432_狄利克雷收敛定理]]
- [[MATHWIKI-METHOD-CLUSTER-722_半区间正弦展开识别]]
- [[MATHWIKI-METHOD-CLUSTER-830_周期奇延拓]]
- [[MATHWIKI-METHOD-CLUSTER-881_奇性判断]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-068_傅里叶展开对象识别与点值求和]]
- [[MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线]]

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
