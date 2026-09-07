---
wiki_id: SRC-WQ-LA-099
type: source_summary
title: "LA-099 线性表示反求参数"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-099_强化例题6.6-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-099"
knowledge:
  - "向量组线性相关"
  - "矩阵秩"
error_causes:
  - "个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。"
methods:
  - "线性表示"
  - "矩阵秩判断"
  - "参数分类讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-101_向量组线性相关"
  - "MATHWIKI-METHOD-CLUSTER-040_参数分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断"
  - "MATHWIKI-METHOD-CLUSTER-177_线性表示"
  - "MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
status: indexed
last_updated: 2026-07-15
---

# LA-099 线性表示反求参数

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-099_强化例题6.6-2.md`
- wrongnet ID：`LA-099`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 向量组线性相关 |
| 题型 | 线性表示与参数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 向量组线性相关
- 矩阵秩

### 错因

- 个人错因未记录；本卡仅按题图、解析图和专题页补强复做入口，待用户复做后确认实际漏点。

### 方法

- 线性表示
- 矩阵秩判断
- 参数分类讨论

### 陷阱

- \(\alpha\) 组能表示 \(\beta\) 组，只说明 \(\operatorname{span}(\beta)\subseteq \operator…
- \(\det(\alpha)=0\) 只给候选 \(a=1\) 或 \(a=-2\)，还必须代回排除不满足表示关系的值。
- “不能表示”通常是包含关系失败，不只是秩不同这一种表现。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先写 span(beta) 包含于 span(alpha)，再找候选参数。 |
| missed_action | 旧卡未记录用户实际漏点；复做时重点确认是否漏掉“写 span(beta) 包含于 span(alpha)，再找候选参数。”这一步。 |
| related_method_card_id | L06-004 |
| next_reminder | 看到线性表示反求参数，先写空间包含，再把行列式得到的参数逐个回代。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-018_个人错因未记录-本卡仅按题图、解析图和专题页补强复做入口-待用户复做后确]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-101_向量组线性相关]]
- [[MATHWIKI-METHOD-CLUSTER-040_参数分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-051_矩阵秩判断]]
- [[MATHWIKI-METHOD-CLUSTER-177_线性表示]]

### 深度编译页

- [[MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示]]
- [[MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-090

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
