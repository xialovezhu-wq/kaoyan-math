---
wiki_id: SRC-WQ-GS-156
type: source_summary
title: "GS-156 1000题A组5.15"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-156_1000题A组5.15.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-156"
knowledge:
  - "一元函数微分学应用"
  - "单调性与极值"
  - "微分方程"
error_causes:
  - "符号错误"
  - "条件检查遗漏"
methods:
  - "极值必要条件"
  - "二阶导判别法"
  - "分类讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-019_符号错误"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-1104_极值必要条件"
  - "MATHWIKI-METHOD-CLUSTER-281_二阶导判别法"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-144"
formal_projection_sha256: 73f483d59efc06936c4c814b98ccd4546f1ef6ef6faf0026b62fe7abeb473811
---

# GS-156 1000题A组5.15

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-156_1000题A组5.15.md`
- wrongnet ID：`GS-156`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 由微分方程判极值类型 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 单调性与极值
- 微分方程

### 错因

- 符号错误
- 条件检查遗漏

### 方法

- 极值必要条件
- 二阶导判别法
- 分类讨论

### 陷阱

- alpha为负时分子分母同号
- x=0要单独用极限处理

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先按 \(\alpha>0\) 与 \(\alpha<0\) 分别判断分子、分母符号。 |
| missed_action | 漏掉 \(\alpha<0\) 时分子 \(1-e^{-\alpha}<0\)，导致二阶导符号误判。 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到含参数的二阶导符号式，先分参数正负，再合并分子分母符号判断。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-019_符号错误]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-1104_极值必要条件]]
- [[MATHWIKI-METHOD-CLUSTER-281_二阶导判别法]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-144

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
