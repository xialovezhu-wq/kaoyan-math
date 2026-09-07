---
wiki_id: SRC-WQ-GS-676
type: source_summary
title: "GS-676 170671 幂型反常积分瑕点判敛"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-676_170671幂型反常积分瑕点判敛.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-676"
knowledge:
  - "反常积分"
  - "等价无穷小"
  - "比较判别法"
  - "极限比较判别法"
error_causes:
  - "概念混淆"
  - "条件忽略"
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
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-005_A-CONCEPT"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-028_反常积分"
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
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-180"
  - "GS-675"
formal_projection_sha256: ad9d1f0ad91a5b98654258cc865eb31698c234b142e349ac11785bbdc8457057
---

# GS-676 170671 幂型反常积分瑕点判敛

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-676_170671幂型反常积分瑕点判敛.md`
- wrongnet ID：`GS-676`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 反常积分 |
| 题型 | 含参幂型反常积分敛散性判别 |
| 日期 | 2026-07-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 反常积分
- 等价无穷小
- 比较判别法
- 极限比较判别法

### 错因

- 概念混淆
- 条件忽略
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

### 陷阱

- x的参数指数可能变分母
- 0点可疑瑕点
- 分母非零极限可当常数
- 分子趋零不能直接丢掉
- 无穷端与有限瑕点条件不同
- 瑕点p小于1收敛
- 无穷端p大于1收敛

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-CONCEPT |
| expected_first_action | 先标出 \(x=0^+\) 与 \(x\to+\infty\) 两个反常端点，并把积分拆成 \([0,1]\) 和 \([1,+\infty)\) 两段。 |
| missed_action | 把 \(\arctan0\) 和 \(2+0^p\) 都有定义当作 0 点正常，漏看 \(x^{1-p}\) 在 \(p>1\) 时会变成 \(1/x^{p-1}\)。 |
| related_method_card_id | H08-005 |
| next_reminder | 看到下端点 0 且含 \(x^{\text{参数}}\)，先检查指数是否可能为负；再做整体等价，不要只把分子分母分别代 0。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-005_A-CONCEPT]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-028_反常积分]]
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

### 深度编译页

- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-180
- GS-675

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
