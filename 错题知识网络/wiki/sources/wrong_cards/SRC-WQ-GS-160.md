---
wiki_id: SRC-WQ-GS-160
type: source_summary
title: "GS-160 1000题B组5.7"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-160_1000题B组5.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-160"
knowledge:
  - "定积分"
  - "绝对值分类"
  - "单调性与极值"
  - "凹凸性与拐点"
error_causes:
  - "个人原始错因未记录"
methods:
  - "绝对值分段积分"
  - "求导判单调"
  - "二阶导判凹凸"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-029_个人原始错因未记录"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-018_凹凸性与拐点"
  - "MATHWIKI-KNOWLEDGE-052_绝对值分类"
  - "MATHWIKI-METHOD-CLUSTER-419_求导判单调"
  - "MATHWIKI-METHOD-CLUSTER-453_绝对值分段积分"
  - "MATHWIKI-METHOD-CLUSTER-563_二阶导判凹凸"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-160 1000题B组5.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-160_1000题B组5.7.md`
- wrongnet ID：`GS-160`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 绝对值定积分单调凹凸判别 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 绝对值分类
- 单调性与极值
- 凹凸性与拐点

### 错因

- 个人原始错因未记录

### 方法

- 绝对值分段积分
- 求导判单调
- 二阶导判凹凸

### 陷阱

- 绝对值分段点随参数x变化
- 凹凸性看二阶导不是看单调

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先按 \(t=0\) 与 \(t=x\) 拆开绝对值积分 |
| missed_action | 旧卡缺用户作答过程；待确认是否漏了随参数变化的绝对值分段点 |
| related_method_card_id | H09-007 |
| next_reminder | 看到绝对值积分且分段点含参数，先拆区间去绝对值，再求导判断性质。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-029_个人原始错因未记录]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-018_凹凸性与拐点]]
- [[MATHWIKI-KNOWLEDGE-052_绝对值分类]]
- [[MATHWIKI-METHOD-CLUSTER-419_求导判单调]]
- [[MATHWIKI-METHOD-CLUSTER-453_绝对值分段积分]]
- [[MATHWIKI-METHOD-CLUSTER-563_二阶导判凹凸]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-288

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
