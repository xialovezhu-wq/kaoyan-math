---
wiki_id: SRC-WQ-LA-078
type: source_summary
title: "LA-078 强化例题5.1-2"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-078_强化例题5.1-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-078"
knowledge:
  - "线性方程组"
  - "矩阵秩"
  - "向量组线性无关"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "秩判定解空间维数"
  - "行空间与零空间正交"
  - "齐次方程组基础解系"
  - "非齐次方程组有解唯一性判定"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-025_矩阵秩"
  - "MATHWIKI-KNOWLEDGE-033_线性方程组"
  - "MATHWIKI-KNOWLEDGE-090_向量组线性无关"
  - "MATHWIKI-METHOD-CLUSTER-104_齐次方程组基础解系"
  - "MATHWIKI-METHOD-CLUSTER-1247_秩判定解空间维数"
  - "MATHWIKI-METHOD-CLUSTER-1329_行空间与零空间正交"
  - "MATHWIKI-METHOD-CLUSTER-1417_非齐次方程组有解唯一性判定"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-017_线性方程组零空间与秩约束入口链"
  - "MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# LA-078 强化例题5.1-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-078_强化例题5.1-2.md`
- wrongnet ID：`LA-078`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 线性方程组 |
| 题型 | 矩阵秩与齐次方程组解空间 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 线性方程组
- 矩阵秩
- 向量组线性无关

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 秩判定解空间维数
- 行空间与零空间正交
- 齐次方程组基础解系
- 非齐次方程组有解唯一性判定

### 陷阱

- \(AB^{\mathrm T}=0\) 说明 \(A\) 的行空间与 \(B\) 的行空间正交
- \(b\) 是 \(Ax=0\) 的非零解时，先判断 \(b\in N(A)\)
- \(B^{\mathrm T}\) 为 \(5\times3\) 且列满秩时，若有解则唯一

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把 \(AB^{\mathrm T}=O\) 翻译成 \(A\) 的行空间与 \(B\) 的行空间正交 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是把它当普通矩阵乘法计算，没有转成行空间正交和解空间维数 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到 \(AB^{\mathrm T}=0\) 和秩相加满维，先想行空间互为正交补，再判解性。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-033_线性方程组]]
- [[MATHWIKI-KNOWLEDGE-090_向量组线性无关]]
- [[MATHWIKI-METHOD-CLUSTER-104_齐次方程组基础解系]]
- [[MATHWIKI-METHOD-CLUSTER-1247_秩判定解空间维数]]
- [[MATHWIKI-METHOD-CLUSTER-1329_行空间与零空间正交]]
- [[MATHWIKI-METHOD-CLUSTER-1417_非齐次方程组有解唯一性判定]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-017_线性方程组零空间与秩约束入口链]]
- [[MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-079
- LA-081

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
