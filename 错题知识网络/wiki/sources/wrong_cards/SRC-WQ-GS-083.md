---
wiki_id: SRC-WQ-GS-083
type: source_summary
title: "GS-083 1000题B组1.38"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-083_1000题B组1.38.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-083"
knowledge:
  - "极限与连续"
  - "泰勒公式"
  - "变上限积分"
error_causes:
  - "公式记错"
  - "动作链断裂"
methods:
  - "牛顿莱布尼茨公式"
  - "逐项积分"
  - "泰勒展开"
  - "倒数展开"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-015_公式记错"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-METHOD-CLUSTER-008_泰勒展开"
  - "MATHWIKI-METHOD-CLUSTER-049_牛顿莱布尼茨公式"
  - "MATHWIKI-METHOD-CLUSTER-132_逐项积分"
  - "MATHWIKI-METHOD-CLUSTER-601_倒数展开"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-093_局部展开对象与真实增量匹配"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-083 1000题B组1.38

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-083_1000题B组1.38.md`
- wrongnet ID：`GS-083`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 导函数展开积分还原泰勒 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 泰勒公式
- 变上限积分

### 错因

- 公式记错
- 动作链断裂

### 方法

- 牛顿莱布尼茨公式
- 逐项积分
- 泰勒展开
- 倒数展开

### 陷阱

- 已知导函数不是原函数
- 积分后阶数提高
- 佩亚诺余项

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写 $f(x)-f(0)=\int_0^x f'(t)\,dt$。 |
| missed_action | 直接代入或展开 $f$，没有先由 $f'$ 积分得到 $f(x)-f(0)$。 |
| related_method_card_id | 待匹配 |
| next_reminder | 已知导函数展开时，先积分还原原函数增量，再处理目标式。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-015_公式记错]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-049_牛顿莱布尼茨公式]]
- [[MATHWIKI-METHOD-CLUSTER-132_逐项积分]]
- [[MATHWIKI-METHOD-CLUSTER-601_倒数展开]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-093_局部展开对象与真实增量匹配]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-052
- GS-157
- GS-231
- GS-248
- GS-283

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
