---
wiki_id: SRC-WQ-GS-425
type: source_summary
title: "GS-425 强化例题9.15"
subject: "线性代数"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-425_强化例题9.15.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-425"
knowledge:
  - "二次型"
  - "正定矩阵"
  - "特征值与特征向量"
error_causes:
  - "旧批量导入未记录用户个人错因；本轮仅确认历史分类误挂与广义 Rayleigh 商入口，待复做确认实际漏点。"
methods:
  - "二次型矩阵化"
  - "正定矩阵判定"
  - "配方法"
  - "Cholesky分解"
  - "合同变换"
  - "Rayleigh 商"
  - "特征值最值"
wiki_refs:
  - "MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-267_旧批量导入未记录用户个人错因-本轮仅确认历史分类误挂与广义Rayleig"
  - "MATHWIKI-KNOWLEDGE-016_特征值与特征向量"
  - "MATHWIKI-KNOWLEDGE-034_二次型"
  - "MATHWIKI-KNOWLEDGE-113_正定矩阵"
  - "MATHWIKI-METHOD-CLUSTER-056_二次型矩阵化"
  - "MATHWIKI-METHOD-CLUSTER-085_配方法"
  - "MATHWIKI-METHOD-CLUSTER-093_合同变换"
  - "MATHWIKI-METHOD-CLUSTER-125_正定矩阵判定"
  - "MATHWIKI-METHOD-CLUSTER-268_Cholesky分解"
  - "MATHWIKI-METHOD-CLUSTER-269_Rayleigh商"
  - "MATHWIKI-METHOD-CLUSTER-429_特征值最值"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-LA-METHOD-002_二次型Rayleigh商最值"
  - "MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-425 强化例题9.15

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-425_强化例题9.15.md`
- wrongnet ID：`GS-425`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 线性代数 |
| 章节 | 二次型 |
| 题型 | 正定分母广义 Rayleigh 商最值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二次型
- 正定矩阵
- 特征值与特征向量

### 错因

- 旧批量导入未记录用户个人错因；本轮仅确认历史分类误挂与广义 Rayleigh 商入口，待复做确认实际漏点。

### 方法

- 二次型矩阵化
- 正定矩阵判定
- 配方法
- Cholesky分解
- 合同变换
- Rayleigh 商
- 特征值最值

### 陷阱

- 二次型矩阵必须对称化，\(x_1x_2\) 的系数要拆到对称位置。
- 分母是 \(x^TBx\) 时不能直接套 \(x^Tx\) 形式的 Rayleigh 商。
- \(B=D^TD\) 需要先确认 \(B\) 正定，变量替换后分子矩阵也要同步变为 \((D^{-1})^TAD^{-1}\)。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先判 \(B\) 正定并写 \(B=D^TD\)，再令 \(z=Dx\) 把分母化为 \(z^Tz\)。 |
| missed_action | 用户本人错因未记录；本轮只确认旧卡分类误挂和复做入口，不反推明确个人断点。 |
| related_method_card_id | L09-011 |
| next_reminder | 分母是正定二次型时，先标准化分母，再求新矩阵的特征值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-LA_线性代数错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-267_旧批量导入未记录用户个人错因-本轮仅确认历史分类误挂与广义Rayleig]]
- [[MATHWIKI-KNOWLEDGE-016_特征值与特征向量]]
- [[MATHWIKI-KNOWLEDGE-034_二次型]]
- [[MATHWIKI-KNOWLEDGE-113_正定矩阵]]
- [[MATHWIKI-METHOD-CLUSTER-056_二次型矩阵化]]
- [[MATHWIKI-METHOD-CLUSTER-085_配方法]]
- [[MATHWIKI-METHOD-CLUSTER-093_合同变换]]
- [[MATHWIKI-METHOD-CLUSTER-125_正定矩阵判定]]
- [[MATHWIKI-METHOD-CLUSTER-268_Cholesky分解]]
- [[MATHWIKI-METHOD-CLUSTER-269_Rayleigh商]]
- [[MATHWIKI-METHOD-CLUSTER-429_特征值最值]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-LA-METHOD-002_二次型Rayleigh商最值]]
- [[MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-424
- LA-042
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
