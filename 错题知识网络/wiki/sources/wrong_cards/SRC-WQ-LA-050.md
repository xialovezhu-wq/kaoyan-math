---
wiki_id: SRC-WQ-LA-050
type: source_summary
title: "LA-050 反对称伴随矩阵二次型"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-050_强化例题3.11(171611).md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/线性代数/LA-050_强化例题3.11(171611).md"
visual_ids:
  - "VIS-LA-050"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/LA-050/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/LA-050/solution_01.png"
wrongnet_refs:
  - "LA-050"
knowledge:
  - "行列式"
  - "二次型"
  - "伴随矩阵"
  - "逆矩阵"
  - "反对称矩阵"
error_causes:
  - "概念：未将逐元素反对称关系矩阵化为 A^T=-A，反对称矩阵定义不稳。"
  - "方法：得到 A*=A^{-1} 后仍求具体逆矩阵，没有只传递转置结构。"
  - "表达：混淆全部元素之和为 0 与每个元素都为 0。"
methods:
  - "反对称矩阵"
  - "伴随矩阵"
  - "伴随矩阵与逆矩阵关系"
  - "行列式性质"
  - "二次型为零"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001"

  - "MATHWIKI-ERROR-CLUSTER-009"

  - "MATHWIKI-KNOWLEDGE-023"

  - "MATHWIKI-KNOWLEDGE-034"

  - "MATHWIKI-METHOD-CLUSTER-108"

  - "MATHWIKI-METHOD-CLUSTER-179"

  - "MATHWIKI-METHOD-CLUSTER-551"

  - "MATHWIKI-METHOD-CLUSTER-785"

  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-010_伴随矩阵与反对称结构"
  - "MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-08-27
formal_projection_sha256: a81971c3a18e0b5154fa56316c71463faf95d25c08e568293d47fd13b77dfc1f
---

# LA-050 反对称伴随矩阵二次型

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-050_强化例题3.11(171611).md`
- wrongnet ID：`LA-050`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/线性代数/LA-050_强化例题3.11(171611).md`（`VIS-LA-050`）
- 题图 1 张；解析图 1 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 矩阵运算 |
| 题型 | 反对称矩阵与伴随矩阵 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 行列式
- 二次型

### 错因

- 概念：未把逐元素反对称关系转成矩阵关系。
- 方法：没有只传递逆矩阵的反对称结构。
- 表达：混淆元素总和为零与每个元素为零。

### 方法

- 反对称矩阵
- 伴随矩阵
- 行列式性质
- 二次型为零

### 陷阱

- 反对称矩阵奇数阶行列式为 \(0\)，与 \(|A|=1\) 矛盾，所以 \(n\) 必为偶数。
- \((kA)^*=k^{n-1}A^*\)，这里 \(n\) 为偶数，故 \((-A)^*=-A^*\)。
- 反对称矩阵 \(B\) 满足 \(x^{\mathsf T}Bx=0\)，不要把所有元素直接相加硬算。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先由反对称关系写 \(A^{\mathsf T}=-A\)，再判断 \(A^*\) 的反对称性 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是直接展开二次型，或忘记先证明 \(A^*\) 仍保持反对称结构 |
| related_method_card_id | L03-006 |
| next_reminder | 看到反对称矩阵和二次型，先确认矩阵是否反对称，再用 \(x^{\mathsf T}Bx=0\) 收口。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-023_行列式]]
- [[MATHWIKI-KNOWLEDGE-034_二次型]]
- [[MATHWIKI-METHOD-CLUSTER-108_伴随矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-179_行列式性质]]
- [[MATHWIKI-METHOD-CLUSTER-551_二次型为零]]
- [[MATHWIKI-METHOD-CLUSTER-785_反对称矩阵]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-010_伴随矩阵与反对称结构]]
- [[MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-049

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
