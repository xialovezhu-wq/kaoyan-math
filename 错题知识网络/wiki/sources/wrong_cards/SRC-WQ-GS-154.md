---
wiki_id: SRC-WQ-GS-154
type: source_summary
title: "GS-154 1000题A5.6"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-154_1000题A5.6.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-154"
knowledge:
  - "一元函数微分学应用"
  - "复合函数求导"
  - "高阶导数"
  - "凹凸性与拐点"
error_causes:
  - "计算失误"
  - "复合函数求导细节错误"
methods:
  - "链式法则"
  - "二阶导计算"
  - "拐点条件：$y^{\\prime\\prime}=0$"
  - "代入条件求参数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-007_B7-CALC"
  - "MATHWIKI-ERROR-CLUSTER-014_计算失误"
  - "MATHWIKI-ERROR-CLUSTER-181_复合函数求导细节错误"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-018_凹凸性与拐点"
  - "MATHWIKI-KNOWLEDGE-027_高阶导数"
  - "MATHWIKI-KNOWLEDGE-030_复合函数求导"
  - "MATHWIKI-METHOD-CLUSTER-1016_拐点条件-$y^{-prime-prime}=0$"
  - "MATHWIKI-METHOD-CLUSTER-135_链式法则"
  - "MATHWIKI-METHOD-CLUSTER-567_二阶导计算"
  - "MATHWIKI-METHOD-CLUSTER-578_代入条件求参数"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-154 1000题A5.6

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-154_1000题A5.6.md`
- wrongnet ID：`GS-154`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 复合函数二阶导与拐点条件 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 复合函数求导
- 高阶导数
- 凹凸性与拐点

### 错因

- 计算失误
- 复合函数求导细节错误

### 方法

- 链式法则
- 二阶导计算
- 拐点条件：$y^{\prime\prime}=0$
- 代入条件求参数

### 陷阱

- 常数因子不要平方
- 先由 $y(1)=\sqrt2$ 得 $f(1)=2$
- 拐点给 $y^{\prime\prime}(1)=0$

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B7-CALC |
| expected_first_action | 先写 $y^{\prime}=\frac{f^{\prime}(x)}{2\sqrt{f(x)}}$，再把常数 $1/2$ 提出后对 $f^{\prime}(x)(f(x))^{-1/2}$ 求导。 |
| missed_action | 把分母里的常数 $2$ 也当成变量分母一起平方，导致二阶导系数错。 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到根式复合函数求二阶导，先提出常数因子，再对变量部分做乘积法则和链式法则。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-007_B7-CALC]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-ERROR-CLUSTER-181_复合函数求导细节错误]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-018_凹凸性与拐点]]
- [[MATHWIKI-KNOWLEDGE-027_高阶导数]]
- [[MATHWIKI-KNOWLEDGE-030_复合函数求导]]
- [[MATHWIKI-METHOD-CLUSTER-1016_拐点条件-$y^{-prime-prime}=0$]]
- [[MATHWIKI-METHOD-CLUSTER-135_链式法则]]
- [[MATHWIKI-METHOD-CLUSTER-567_二阶导计算]]
- [[MATHWIKI-METHOD-CLUSTER-578_代入条件求参数]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-143

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
