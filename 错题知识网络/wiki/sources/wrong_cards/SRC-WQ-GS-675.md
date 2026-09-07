---
wiki_id: SRC-WQ-GS-675
type: source_summary
title: "GS-675 57721 对数反常积分瑕点判敛"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-675_57721对数反常积分瑕点判敛.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-675"
knowledge:
  - "反常积分"
  - "对数型积分"
  - "等价无穷小"
  - "比较判别法"
  - "极限比较判别法"
error_causes:
  - "条件忽略"
  - "题型识别失败"
  - "过程跳步"
methods:
  - "先判型"
  - "找反常点"
  - "区间拆分"
  - "反常积分判敛"
  - "p型判敛"
  - "等价比较判别"
  - "极限比较判别法"
  - "边界单独验证"
  - "对数幂比较"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-028_反常积分"
  - "MATHWIKI-KNOWLEDGE-057_对数型积分"
  - "MATHWIKI-KNOWLEDGE-061_极限比较判别法"
  - "MATHWIKI-KNOWLEDGE-156_比较判别法"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-033_极限比较判别法"
  - "MATHWIKI-METHOD-CLUSTER-048_区间拆分"
  - "MATHWIKI-METHOD-CLUSTER-105_p型判敛"
  - "MATHWIKI-METHOD-CLUSTER-175_等价比较判别"
  - "MATHWIKI-METHOD-CLUSTER-207_反常积分判敛"
  - "MATHWIKI-METHOD-CLUSTER-229_找反常点"
  - "MATHWIKI-METHOD-CLUSTER-262_边界单独验证"
  - "MATHWIKI-METHOD-CLUSTER-355_对数幂比较"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-180"
formal_projection_sha256: 1561b750fea2d0d6682ad9f2628bb2ed3fc78c67854ef24640977e3a60c92097
---

# GS-675 57721 对数反常积分瑕点判敛

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-675_57721对数反常积分瑕点判敛.md`
- wrongnet ID：`GS-675`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 反常积分 |
| 题型 | 对数型反常积分含参判敛 |
| 日期 | 2026-07-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 反常积分
- 对数型积分
- 等价无穷小
- 比较判别法
- 极限比较判别法

### 错因

- 条件忽略
- 题型识别失败
- 过程跳步

### 方法

- 先判型
- 找反常点
- 区间拆分
- 反常积分判敛
- p型判敛
- 等价比较判别
- 极限比较判别法
- 边界单独验证
- 对数幂比较

### 陷阱

- 下端点ln1为0
- x等于1是瑕点
- 无穷端与有限瑕点条件不同
- 对数因子在无穷远处有利
- 对数因子在1点附近有害
- 瑕点p小于1收敛
- 无穷端p大于1收敛

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先标出两个反常点 \(x=1^+\) 与 \(x\to+\infty\)，并把积分拆成 \([1,e]\) 和 \([e,+\infty)\) 两段分别判敛。 |
| missed_action | 只把题目当成无穷远处的 \(1/x^p\) 比较题，没有先检查 \(x=1\) 处 \(\ln x=0\) 导致的有限瑕点。 |
| related_method_card_id | H08-005 |
| next_reminder | 看到反常积分从 \(1\) 起且分母有 \(\ln^q x\)，先查 \(x=1\) 是否因 \(\ln1=0\) 成为瑕点，再查 \(+\infty\)；两段都收敛才是原积分收敛。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-028_反常积分]]
- [[MATHWIKI-KNOWLEDGE-057_对数型积分]]
- [[MATHWIKI-KNOWLEDGE-061_极限比较判别法]]
- [[MATHWIKI-KNOWLEDGE-156_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-033_极限比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-048_区间拆分]]
- [[MATHWIKI-METHOD-CLUSTER-105_p型判敛]]
- [[MATHWIKI-METHOD-CLUSTER-175_等价比较判别]]
- [[MATHWIKI-METHOD-CLUSTER-207_反常积分判敛]]
- [[MATHWIKI-METHOD-CLUSTER-229_找反常点]]
- [[MATHWIKI-METHOD-CLUSTER-262_边界单独验证]]
- [[MATHWIKI-METHOD-CLUSTER-355_对数幂比较]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-180

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
