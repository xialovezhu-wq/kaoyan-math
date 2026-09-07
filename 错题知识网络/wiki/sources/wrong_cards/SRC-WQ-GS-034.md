---
wiki_id: SRC-WQ-GS-034
type: source_summary
title: "GS-034 168317 1000题B组42"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-034_1000题B组42.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-034"
knowledge:
  - "极限与连续"
  - "间断点分类"
  - "绝对值分类"
  - "等价无穷小"
error_causes:
  - "计算失误"
  - "符号错误"
  - "分类讨论不全"
  - "过程跳步"
methods:
  - "分类讨论"
  - "取对数"
  - "等价变形"
  - "左右极限"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-014_计算失误"
  - "MATHWIKI-ERROR-CLUSTER-019_符号错误"
  - "MATHWIKI-ERROR-CLUSTER-023_分类讨论不全"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-052_绝对值分类"
  - "MATHWIKI-KNOWLEDGE-064_间断点分类"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-019_取对数"
  - "MATHWIKI-METHOD-CLUSTER-224_左右极限"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-METHOD-008_分类讨论闭环"
  - "MATHWIKI-GS-METHOD-011_B5-CHECK检查断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-035"
formal_projection_sha256: 0a839273ca0aaef957fe3cfe375e5b108f73db9c102c96dce1122099b9197de0
---

# GS-034 168317 1000题B组42

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-034_1000题B组42.md`
- wrongnet ID：`GS-034`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 间断点类型判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 间断点分类
- 绝对值分类
- 等价无穷小

### 错因

- 计算失误
- 符号错误
- 分类讨论不全
- 过程跳步

### 方法

- 分类讨论
- 取对数
- 等价变形
- 左右极限

### 陷阱

- 定义域
- 左右极限
- 正负号
- 适用条件
- 极限过程
- 分母零点

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先列可疑点 \(x=-1,0,1\)，再在 \(x=\pm1\) 处同步展开 \(|\ln|x||\) 与 \(x^2-1=(x-1)(x+1)\) 的左右符号，在 \(x=0\) 单独判无穷间断 |
| missed_action | 没有先把可疑点列全，并在 \(x=\pm1\) 处同步处理分子绝对值与分母左右符号 |
| related_method_card_id | H01-008 |
| next_reminder | 看到含 \(|\ln|x||\) 和分母零点的间断点题，先列可疑点，再逐点做左右等价和符号判断。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-ERROR-CLUSTER-019_符号错误]]
- [[MATHWIKI-ERROR-CLUSTER-023_分类讨论不全]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-052_绝对值分类]]
- [[MATHWIKI-KNOWLEDGE-064_间断点分类]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-019_取对数]]
- [[MATHWIKI-METHOD-CLUSTER-224_左右极限]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-008_分类讨论闭环]]
- [[MATHWIKI-GS-METHOD-011_B5-CHECK检查断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-035

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
