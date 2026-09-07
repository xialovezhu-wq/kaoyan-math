---
wiki_id: SRC-WQ-LA-042
type: source_summary
title: "LA-042 行列式二次型正定参数"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-042_强化例题9.12.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-042"
knowledge:
  - "二次型"
  - "正定矩阵"
  - "行列式"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "行列式展开"
  - "二次型矩阵化"
  - "正定矩阵判定"
  - "参数分类讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-023_行列式"
  - "MATHWIKI-KNOWLEDGE-034_二次型"
  - "MATHWIKI-KNOWLEDGE-113_正定矩阵"
  - "MATHWIKI-METHOD-CLUSTER-040_参数分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-056_二次型矩阵化"
  - "MATHWIKI-METHOD-CLUSTER-125_正定矩阵判定"
  - "MATHWIKI-METHOD-CLUSTER-1323_行列式展开"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-007_二次型合同相似与正定平方根"
  - "MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# LA-042 行列式二次型正定参数

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-042_强化例题9.12.md`
- wrongnet ID：`LA-042`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 二次型 |
| 题型 | 行列式构造二次型正定参数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二次型
- 正定矩阵
- 行列式

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 行列式展开
- 二次型矩阵化
- 正定矩阵判定
- 参数分类讨论

### 陷阱

- \(|xA+yB|\) 展开后是关于 \(x,y\) 的二次型，不是普通一元参数不等式。
- 交叉项 \(-2xy\) 在矩阵中对应两个 \(-1\)。
- 二阶正定要同时检查首项系数和行列式。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把 \(|xA+yB|\) 展开成 \(ax^2+2bxy+cy^2\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是把它当作普通参数不等式，或交叉项矩阵化时忘记除以 2 |
| related_method_card_id | L09-009 |
| next_reminder | 看到 \(|xA+yB|\) 正定，先展开成二次型，再写对称矩阵判正定。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-023_行列式]]
- [[MATHWIKI-KNOWLEDGE-034_二次型]]
- [[MATHWIKI-KNOWLEDGE-113_正定矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-040_参数分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-056_二次型矩阵化]]
- [[MATHWIKI-METHOD-CLUSTER-125_正定矩阵判定]]
- [[MATHWIKI-METHOD-CLUSTER-1323_行列式展开]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-007_二次型合同相似与正定平方根]]
- [[MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-035
- GS-425

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
