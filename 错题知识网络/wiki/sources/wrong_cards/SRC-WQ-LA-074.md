---
wiki_id: SRC-WQ-LA-074
type: source_summary
title: "LA-074 伴随矩阵零空间列向量基"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-074_2020年第7题.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/LA-074_2020年第7题.md"
visual_ids:
  - "VIS-LA-074"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/LA-074/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/LA-074/solution_01.png"
wrongnet_refs:
  - "LA-074"
knowledge:
  - "矩阵运算"
  - "行列式"
  - "矩阵秩"
  - "线性方程组"
  - "向量组线性无关"
  - "伴随矩阵"
  - "代数余子式"
  - "伴随矩阵秩公式"
  - "零空间"
  - "零空间基"
error_causes:
  - "知识点不熟"
  - "目标识别断点"
  - "数学对象混淆"
  - "解空间与基础解系混淆"
  - "代数余子式结构理解不稳"
methods:
  - "伴随矩阵秩公式"
  - "代数余子式"
  - "齐次方程组通解"
  - "向量组线性无关判定"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA"
  - "MATHWIKI-KNOWLEDGE-014"
  - "MATHWIKI-KNOWLEDGE-023"
  - "MATHWIKI-KNOWLEDGE-025"
  - "MATHWIKI-KNOWLEDGE-033"
  - "MATHWIKI-KNOWLEDGE-090"
  - "MATHWIKI-KNOWLEDGE-135"
  - "MATHWIKI-METHOD-CLUSTER-1434"
  - "MATHWIKI-METHOD-CLUSTER-287"
  - "MATHWIKI-METHOD-CLUSTER-595"
  - "MATHWIKI-METHOD-CLUSTER-827"
  - "MATHWIKI-GS-METHOD-009"
  - "MATHWIKI-LA-METHOD-010"
  - "MATHWIKI-LA-TOPIC-001"
  - "MATHWIKI-SYNTHESIS-001"
status: indexed
last_updated: 2026-08-03
formal_projection_sha256: 79023e323e1f5dbf9fdd215c994f8b847d02db5582505c612dca30b20f2fce1d
---

# LA-074 伴随矩阵零空间列向量基

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-074_2020年第7题.md`
- wrongnet ID：`LA-074`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 伴随矩阵与线性方程组 |
| 题型 | 伴随矩阵齐次方程组通解 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 矩阵运算
- 行列式
- 矩阵秩
- 线性方程组
- 向量组线性无关
- 伴随矩阵

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 伴随矩阵秩公式
- 代数余子式
- 齐次方程组通解
- 向量组线性无关判定

### 陷阱

- \(A_{12}\ne0\) 不是随便说明 \(A^*\ne0\)，还要对应到删去第 1 行第 2 列后的三阶子式。
- \(A^*x=0\) 的解空间维数是 \(4-r(A^*)=3\)，所以需要三条线性无关解向量。
- \(A^*A=O\) 只能说明四个列向量都是解，还必须从中挑出线性无关的三列。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先由 \(A_{12}\ne0\) 判断 \(r(A)=3\) 与 \(r(A^*)=1\) |
| missed_action | 旧卡未记录用户实际漏步；复做风险是直接猜通解，没先用伴随矩阵秩确定解空间维数 |
| related_method_card_id | L04-006 |
| next_reminder | 看到 \(A^*x=0\)，先判 \(r(A^*)\) 和零空间维数，再用 \(A^*A=|A|E\) 找基。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-014_矩阵运算]]
- [[MATHWIKI-KNOWLEDGE-023_行列式]]
- [[MATHWIKI-KNOWLEDGE-025_矩阵秩]]
- [[MATHWIKI-KNOWLEDGE-033_线性方程组]]
- [[MATHWIKI-KNOWLEDGE-090_向量组线性无关]]
- [[MATHWIKI-KNOWLEDGE-135_伴随矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-1434_齐次方程组通解]]
- [[MATHWIKI-METHOD-CLUSTER-287_代数余子式]]
- [[MATHWIKI-METHOD-CLUSTER-595_伴随矩阵秩公式]]
- [[MATHWIKI-METHOD-CLUSTER-827_向量组线性无关判定]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-010_伴随矩阵与反对称结构]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-049
- LA-060

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
