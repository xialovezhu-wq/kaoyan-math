---
wiki_id: SRC-WQ-GS-398
type: source_summary
title: "GS-398 2021年第14题"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-398_2021年第14题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-398"
knowledge:
  - "二重积分"
  - "二重积分换序"
  - "变上限积分"
error_causes:
  - "方法调取失败"
  - "变量混淆"
methods:
  - "二重积分换序"
  - "区间拆分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-ERROR-CLUSTER-024_变量混淆"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-049_二重积分"
  - "MATHWIKI-KNOWLEDGE-190_二重积分换序"
  - "MATHWIKI-METHOD-CLUSTER-048_区间拆分"
  - "MATHWIKI-METHOD-CLUSTER-190_二重积分换序"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-034_二重积分区域化归与换序"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-398 2021年第14题

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-398_2021年第14题.md`
- wrongnet ID：`GS-398`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 二重积分 |
| 题型 | 二重积分交换积分次序 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二重积分
- 二重积分换序
- 变上限积分

### 错因

- 方法调取失败
- 变量混淆

### 方法

- 二重积分换序
- 区间拆分

### 陷阱

- 积分变量与参数混淆

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把 \(\sqrt{x}\le y\le t,\ 1\le x\le t^2\) 改写为 \(1\le y\le t,\ 1\le x\le y^2\) |
| missed_action | 没有先画区域换序，容易直接对难积的原次序求导 |
| related_method_card_id | H14-002 |
| next_reminder | 看到含参累次积分求导且内层难积，先画区域换序，再对新上限求导。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-024_变量混淆]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-049_二重积分]]
- [[MATHWIKI-KNOWLEDGE-190_二重积分换序]]
- [[MATHWIKI-METHOD-CLUSTER-048_区间拆分]]
- [[MATHWIKI-METHOD-CLUSTER-190_二重积分换序]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-034_二重积分区域化归与换序]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-404

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
