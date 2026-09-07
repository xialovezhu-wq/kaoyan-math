---
wiki_id: SRC-WQ-LA-012
type: source_summary
title: "LA-012 强化例题1.2-2 秩一扰动行列式"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-012_强化例题1.2-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-012"
knowledge:
  - "行列式"
  - "矩阵运算"
  - "特征值与特征向量"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "特征分解"
  - "秩一扰动"
  - "矩阵行列式引理"
  - "等价变形"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-014_矩阵运算"
  - "MATHWIKI-KNOWLEDGE-016_特征值与特征向量"
  - "MATHWIKI-KNOWLEDGE-023_行列式"
  - "MATHWIKI-METHOD-CLUSTER-003_等价变形"
  - "MATHWIKI-METHOD-CLUSTER-023_特征分解"
  - "MATHWIKI-METHOD-CLUSTER-1239_矩阵行列式引理"
  - "MATHWIKI-METHOD-CLUSTER-1243_秩一扰动"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-018_行列式结构化计算与指定项系数"
  - "MATHWIKI-LA-TOPIC-005_行列式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: "2026-07-25"
related_wrongnet_refs: []
review_batch: "MATHWIKI-REVIEW-086"
formal_projection_sha256: "f97315083242aa95b9a28d33d23067e0a9bee3d65116a8d3c2f8123aae0a775f"
---

# LA-012 强化例题1.2-2 秩一扰动行列式

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-012_强化例题1.2-2.md`
- wrongnet ID：`LA-012`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 行列式 |
| 题型 | 行列式计算 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 行列式
- 矩阵运算
- 特征值与特征向量

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 特征分解
- 秩一扰动
- 矩阵行列式引理
- 等价变形

### 陷阱

- 秩一矩阵只有一个非零特征值
- 加单位阵后特征值整体加 1
- 矩阵行列式引理的向量顺序

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先判断 alpha alpha^T 是秩一矩阵，非零特征值为 alpha^T alpha |
| missed_action | 旧卡未记录用户实际漏步；复做风险是把 I+alpha alpha^T 当普通 n 阶行列式硬算 |
| related_method_card_id | L03-001 |
| next_reminder | 看到 I+列向量乘行向量，先识别秩一外积，再用特征值或 det(I+uv^T) 引理。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-016_特征值与特征向量]]
- [[MATHWIKI-KNOWLEDGE-023_行列式]]
- [[MATHWIKI-METHOD-CLUSTER-003_等价变形]]
- [[MATHWIKI-METHOD-CLUSTER-023_特征分解]]
- [[MATHWIKI-METHOD-CLUSTER-1239_矩阵行列式引理]]
- [[MATHWIKI-METHOD-CLUSTER-1243_秩一扰动]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-018_行列式结构化计算与指定项系数]]
- [[MATHWIKI-LA-TOPIC-005_行列式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]

## wrongnet 关联题

- 暂无强边。
