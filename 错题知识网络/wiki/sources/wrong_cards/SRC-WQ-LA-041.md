---
wiki_id: SRC-WQ-LA-041
type: source_summary
title: "LA-041 二次型合同与正交变换判定"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/LA-041_强化例题9.11.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "LA-041"
knowledge:
  - "二次型"
  - "特征值与特征向量"
  - "实对称矩阵"
  - "相似矩阵"
error_causes:
  - "个人错因未记录（旧卡缺作答过程；仅可确认复做入口）"
methods:
  - "配方法"
  - "合同变换"
  - "可逆线性变换"
  - "正交变换"
  - "特征分解"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-005_A-CONCEPT"
  - "MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）"
  - "MATHWIKI-KNOWLEDGE-016_特征值与特征向量"
  - "MATHWIKI-KNOWLEDGE-034_二次型"
  - "MATHWIKI-KNOWLEDGE-040_相似矩阵"
  - "MATHWIKI-KNOWLEDGE-056_实对称矩阵"
  - "MATHWIKI-METHOD-CLUSTER-023_特征分解"
  - "MATHWIKI-METHOD-CLUSTER-085_配方法"
  - "MATHWIKI-METHOD-CLUSTER-093_合同变换"
  - "MATHWIKI-METHOD-CLUSTER-150_可逆线性变换"
  - "MATHWIKI-METHOD-CLUSTER-414_正交变换"
  - "MATHWIKI-LA-METHOD-007_二次型合同相似与正定平方根"
  - "MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线"
status: indexed
last_updated: 2026-07-15
---

# LA-041 二次型合同与正交变换判定

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/LA-041_强化例题9.11.md`
- wrongnet ID：`LA-041`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 二次型 |
| 题型 | 可逆合同变换与正交变换判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二次型
- 特征值与特征向量
- 实对称矩阵
- 相似矩阵

### 错因

- 个人错因未记录（旧卡缺作答过程；仅可确认复做入口）

### 方法

- 配方法
- 合同变换
- 可逆线性变换
- 正交变换
- 特征分解

### 陷阱

- 可逆合同变换存在不代表正交变换存在。
- 正交变换对应实对称矩阵的正交相似，必须保留特征值。
- 两个二次型都化成 \(z_1^2+z_2^2\) 后，还要检查换元矩阵合成方向。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-CONCEPT |
| expected_first_action | 先判断两个二次型是否合同，再单独判断能否正交相似 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是认为可逆变换存在就等于正交变换也存在 |
| related_method_card_id | L09-004 |
| next_reminder | 看到可逆变换和正交变换并列，先分清合同和正交相似的判据。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-005_A-CONCEPT]]
- [[MATHWIKI-ERROR-CLUSTER-009_个人错因未记录（旧卡缺作答过程-仅可确认复做入口）]]
- [[MATHWIKI-KNOWLEDGE-016_特征值与特征向量]]
- [[MATHWIKI-KNOWLEDGE-034_二次型]]
- [[MATHWIKI-KNOWLEDGE-040_相似矩阵]]
- [[MATHWIKI-KNOWLEDGE-056_实对称矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-023_特征分解]]
- [[MATHWIKI-METHOD-CLUSTER-085_配方法]]
- [[MATHWIKI-METHOD-CLUSTER-093_合同变换]]
- [[MATHWIKI-METHOD-CLUSTER-150_可逆线性变换]]
- [[MATHWIKI-METHOD-CLUSTER-414_正交变换]]

### 深度编译页

- [[MATHWIKI-LA-METHOD-007_二次型合同相似与正定平方根]]
- [[MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- LA-030
- LA-037
- LA-040
- LA-043
- LA-044

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
