---
wiki_id: SRC-WQ-GS-135
type: source_summary
title: "GS-135 1000题A组5.4"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-135_1000题A组5.4.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-135"
knowledge:
  - "一元函数微分学应用"
  - "单调性与极值"
  - "恒成立不等式"
  - "参数范围"
error_causes:
  - "方法论调取失败"
  - "条件转化遗漏"
methods:
  - "分离参数"
  - "构造辅助函数"
  - "导数求最值"
  - "恒成立转最值"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-086_条件转化遗漏"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-100_参数范围"
  - "MATHWIKI-KNOWLEDGE-254_恒成立不等式"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-313_分离参数"
  - "MATHWIKI-METHOD-CLUSTER-943_导数求最值"
  - "MATHWIKI-METHOD-CLUSTER-999_恒成立转最值"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-136"
formal_projection_sha256: 84e48d9fe5decac7e3870946e3d3ff83542c83dc7bf60af19e2ec5825731925a
---

# GS-135 1000题A组5.4

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-135_1000题A组5.4.md`
- wrongnet ID：`GS-135`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 恒成立不等式分离参数求最值 |
| 日期 | 2026-05-07 |
| 状态 | 已掌握 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 单调性与极值
- 恒成立不等式
- 参数范围

### 错因

- 方法论调取失败
- 条件转化遗漏

### 方法

- 分离参数
- 构造辅助函数
- 导数求最值
- 恒成立转最值

### 陷阱

- 分离参数后取最大值
- 参数边界
- 正数定义域 $x>0$

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先设 $f(x)=\frac{10}{3}x^3-x^5$，再求 $\max_{x>0}f(x)$。 |
| missed_action | 没有从 $a\ge f(x)$ 触发“取右侧最大值”的动作。 |
| related_method_card_id | H05-006 |
| next_reminder | 看到恒成立且能分离参数，先转成 $a\ge\max f(x)$ 或 $a\le\min f(x)$，再求导找最值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-086_条件转化遗漏]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-100_参数范围]]
- [[MATHWIKI-KNOWLEDGE-254_恒成立不等式]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-313_分离参数]]
- [[MATHWIKI-METHOD-CLUSTER-943_导数求最值]]
- [[MATHWIKI-METHOD-CLUSTER-999_恒成立转最值]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-136

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
