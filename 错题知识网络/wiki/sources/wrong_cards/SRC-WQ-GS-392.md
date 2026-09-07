---
wiki_id: SRC-WQ-GS-392
type: source_summary
title: "GS-392 强化例题13.28"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-392_强化例题13.28.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-392"
knowledge:
  - "多元函数极值"
  - "多元函数偏导"
error_causes:
  - "动作链断裂"
  - "运算路径不稳"
methods:
  - "驻点求解"
  - "Hessian 二次型"
  - "链式求偏导"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-028_运算路径不稳"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-055_多元函数极值"
  - "MATHWIKI-METHOD-CLUSTER-076_Hessian二次型"
  - "MATHWIKI-METHOD-CLUSTER-086_驻点求解"
  - "MATHWIKI-METHOD-CLUSTER-1394_链式求偏导"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-032_多元函数极值驻点判别"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-392 强化例题13.28

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-392_强化例题13.28.md`
- wrongnet ID：`GS-392`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 乘积型二元函数极值判别 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数极值
- 多元函数偏导

### 错因

- 动作链断裂
- 运算路径不稳

### 方法

- 驻点求解
- Hessian 二次型
- 链式求偏导

### 陷阱

- 只看驻点条件不看二阶符号
- 乘积函数偏导漏因子

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先分别求 \(z_x,z_y,z_{xx},z_{yy},z_{xy}\) |
| missed_action | 没有把一元驻点信息转成二元 Hessian 判别条件 |
| related_method_card_id | H13-012 |
| next_reminder | 看到乘积型二元函数极值，先求全套二阶偏导，再用 Hessian 判别符号条件。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-028_运算路径不稳]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-055_多元函数极值]]
- [[MATHWIKI-METHOD-CLUSTER-076_Hessian二次型]]
- [[MATHWIKI-METHOD-CLUSTER-086_驻点求解]]
- [[MATHWIKI-METHOD-CLUSTER-1394_链式求偏导]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-032_多元函数极值驻点判别]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-391
- GS-390

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
