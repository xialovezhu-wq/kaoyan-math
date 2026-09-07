---
wiki_id: SRC-WQ-GS-353
type: source_summary
title: "GS-353 强化例题13.3-2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-353_强化例题13.3-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-353"
knowledge:
  - "多元函数极限"
  - "极限与连续"
  - "多元函数微分学"
error_causes:
  - "触发信息遗漏"
  - "动作链断裂"
methods:
  - "配方法"
  - "正定二次型估计"
  - "夹逼准则"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-KNOWLEDGE-067_多元函数极限"
  - "MATHWIKI-METHOD-CLUSTER-016_夹逼准则"
  - "MATHWIKI-METHOD-CLUSTER-085_配方法"
  - "MATHWIKI-METHOD-CLUSTER-1151_正定二次型估计"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-085_二重极限路径与累次极限判别链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-353 强化例题13.3-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-353_强化例题13.3-2.md`
- wrongnet ID：`GS-353`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 无穷远二元极限夹逼 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数极限
- 极限与连续
- 多元函数微分学

### 错因

- 触发信息遗漏
- 动作链断裂

### 方法

- 配方法
- 正定二次型估计
- 夹逼准则

### 陷阱

- 分母正定性没有转成下界
- 无穷远极限只按一条路径判断
- 拆分子后未分别夹逼

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把 x^2-xy+y^2 配成平方和并写出下界 |
| missed_action | 旧批量卡未记录用户个人错因；低置信推断为没有先把正定二次型转成可用于夹逼的下界 |
| related_method_card_id | H13-002 |
| next_reminder | 看到正定二次型分母，先配方给下界，再分别夹逼分子各项。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-KNOWLEDGE-067_多元函数极限]]
- [[MATHWIKI-METHOD-CLUSTER-016_夹逼准则]]
- [[MATHWIKI-METHOD-CLUSTER-085_配方法]]
- [[MATHWIKI-METHOD-CLUSTER-1151_正定二次型估计]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-085_二重极限路径与累次极限判别链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

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
