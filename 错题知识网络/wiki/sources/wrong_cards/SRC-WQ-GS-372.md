---
wiki_id: SRC-WQ-GS-372
type: source_summary
title: "GS-372 强化例题13.9"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-372_强化例题13.9.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-372"
knowledge:
  - "多元函数微分学"
  - "多元函数连续可微"
  - "极限与连续"
  - "多元函数极限"
  - "多元函数偏导"
error_causes:
  - "知识点挂载噪声"
  - "方法入口未沉淀"
methods:
  - "夹逼"
  - "极坐标"
  - "偏导定义"
  - "左右极限"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-005_A-CONCEPT"
  - "MATHWIKI-ERROR-CLUSTER-012_方法入口未沉淀"
  - "MATHWIKI-ERROR-CLUSTER-059_知识点挂载噪声"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-KNOWLEDGE-037_多元函数连续可微"
  - "MATHWIKI-KNOWLEDGE-067_多元函数极限"
  - "MATHWIKI-METHOD-CLUSTER-024_夹逼"
  - "MATHWIKI-METHOD-CLUSTER-029_偏导定义"
  - "MATHWIKI-METHOD-CLUSTER-1109_极坐标"
  - "MATHWIKI-METHOD-CLUSTER-224_左右极限"
  - "MATHWIKI-GS-METHOD-050_二元函数性质定义判别链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-372 强化例题13.9

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-372_强化例题13.9.md`
- wrongnet ID：`GS-372`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 连续性与偏导存在性判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数微分学
- 多元函数连续可微
- 极限与连续
- 多元函数极限
- 多元函数偏导

### 错因

- 知识点挂载噪声
- 方法入口未沉淀

### 方法

- 夹逼
- 极坐标
- 偏导定义
- 左右极限

### 陷阱

- 左右极限
- 适用条件
- 极限过程
- 连续不推出偏导存在

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-CONCEPT |
| expected_first_action | 先用 \(\sqrt{x^2+y^2}\to0\) 判断连续，再算 \(g_x(0,0)=\lim_{h\to0}|h|/h\)。 |
| missed_action | 历史卡未沉淀连续与偏导存在性的对象差异，并误挂二重积分。 |
| related_method_card_id | H13-006 |
| next_reminder | 看到根号距离函数，先判连续，再用 \(|h|/h\) 的左右极限查偏导。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-005_A-CONCEPT]]
- [[MATHWIKI-ERROR-CLUSTER-012_方法入口未沉淀]]
- [[MATHWIKI-ERROR-CLUSTER-059_知识点挂载噪声]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-KNOWLEDGE-037_多元函数连续可微]]
- [[MATHWIKI-KNOWLEDGE-067_多元函数极限]]
- [[MATHWIKI-METHOD-CLUSTER-024_夹逼]]
- [[MATHWIKI-METHOD-CLUSTER-029_偏导定义]]
- [[MATHWIKI-METHOD-CLUSTER-1109_极坐标]]
- [[MATHWIKI-METHOD-CLUSTER-224_左右极限]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-050_二元函数性质定义判别链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-361
- GS-365
- GS-371
- GS-370
- GS-359

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
