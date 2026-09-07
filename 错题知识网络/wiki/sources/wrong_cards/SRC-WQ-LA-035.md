---
wiki_id: SRC-WQ-LA-035
type: source_summary
title: LA-035 平方和二次型正定参数
subject: 线性代数
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/LA-035_强化例题9.6.md
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
- LA-035
knowledge:
- 二次型
- 正定矩阵
error_causes:
- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）
methods:
- 正定矩阵判定
- 平方和同时为零
- 行列式判定
- 参数分类讨论
wiki_refs:
- MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表
- MATHWIKI-ACTION-GAP-004_B5-CHECK
- MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）
- MATHWIKI-KNOWLEDGE-034_二次型
- MATHWIKI-KNOWLEDGE-113_正定矩阵
- MATHWIKI-METHOD-CLUSTER-040_参数分类讨论
- MATHWIKI-METHOD-CLUSTER-125_正定矩阵判定
- MATHWIKI-METHOD-CLUSTER-1321_行列式判定
- MATHWIKI-METHOD-CLUSTER-981_平方和同时为零
- MATHWIKI-LA-METHOD-006_二次型配方法与正定判定
- MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线
status: indexed
last_updated: '2026-07-25'
formal_projection_sha256: 5117a18bd8a05f4ab56b26fc386d6bf8fbb55f4c1e0cfd2831a25d29bb779ed1
related_wrongnet_refs: []
---

# LA-035 平方和二次型正定参数

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-035_强化例题9.6.md`
- wrongnet ID：`LA-035`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 二次型 |
| 题型 | 二次型正定参数判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二次型
- 正定矩阵

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 正定矩阵判定
- 平方和同时为零
- 行列式判定
- 参数分类讨论

### 陷阱

- 平方和形式只自动推出半正定，不自动推出正定
- 正定要求所有平方项同时为零时只能得到零向量
- 参数使线性形式矩阵不可逆时，会出现非零向量使二次型为 0

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先令所有平方项同时为零，写出对应线性方程组 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是把平方和误判为自动正定，漏查非零公共零点 |
| related_method_card_id | L09-009 |
| next_reminder | 看到平方和二次型判正定，先令所有平方项同时为零，检查是否只有零解。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-034_二次型]]
- [[MATHWIKI-KNOWLEDGE-113_正定矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-040_参数分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-125_正定矩阵判定]]
- [[MATHWIKI-METHOD-CLUSTER-1321_行列式判定]]
- [[MATHWIKI-METHOD-CLUSTER-981_平方和同时为零]]

### 深度编译页

- [[MATHWIKI-LA-METHOD-006_二次型配方法与正定判定]]
- [[MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线]]

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
