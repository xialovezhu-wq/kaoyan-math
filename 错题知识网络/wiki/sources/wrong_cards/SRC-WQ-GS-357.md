---
wiki_id: SRC-WQ-GS-357
type: source_summary
title: "GS-357 强化例题13.6"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-357_强化例题13.6.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-357"
knowledge:
  - "多元函数极限"
  - "累次极限"
  - "极限与连续"
  - "多元函数微分学"
error_causes:
  - "触发信息遗漏"
  - "方法论调取不稳"
  - "动作链断裂"
methods:
  - "累次极限固定变量"
  - "特殊路径"
  - "二重极限判别"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-KNOWLEDGE-067_多元函数极限"
  - "MATHWIKI-KNOWLEDGE-268_累次极限"
  - "MATHWIKI-METHOD-CLUSTER-022_特殊路径"
  - "MATHWIKI-METHOD-CLUSTER-129_累次极限固定变量"
  - "MATHWIKI-METHOD-CLUSTER-189_二重极限判别"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-085_二重极限路径与累次极限判别链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-357 强化例题13.6

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-357_强化例题13.6.md`
- wrongnet ID：`GS-357`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 二重极限与累次极限判别 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数极限
- 累次极限
- 极限与连续
- 多元函数微分学

### 错因

- 触发信息遗漏
- 方法论调取不稳
- 动作链断裂

### 方法

- 累次极限固定变量
- 特殊路径
- 二重极限判别

### 陷阱

- 二重极限和累次极限顺序混淆
- 内层变量没有固定
- 累次极限不等时仍尝试求二重极限

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先固定内层变量分别计算两个累次极限 |
| missed_action | 缺少用户作答过程；低置信推断可能没有先按内外层顺序固定变量 |
| related_method_card_id | H13-003 |
| next_reminder | 看到 I1、I2、I3 同时出现，先固定内层变量算两个累次极限，再判断二重极限。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-021_方法论调取不稳]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-KNOWLEDGE-067_多元函数极限]]
- [[MATHWIKI-KNOWLEDGE-268_累次极限]]
- [[MATHWIKI-METHOD-CLUSTER-022_特殊路径]]
- [[MATHWIKI-METHOD-CLUSTER-129_累次极限固定变量]]
- [[MATHWIKI-METHOD-CLUSTER-189_二重极限判别]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-085_二重极限路径与累次极限判别链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-355

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
