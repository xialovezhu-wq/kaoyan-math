---
wiki_id: SRC-WQ-GS-693
type: source_summary
title: "GS-693 84892 第一型曲线积分极坐标参数化"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-693_84892第一型曲线积分极坐标参数化.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-693"
knowledge:
  - "多元函数积分学"
  - "曲线积分"
  - "极坐标"
error_causes:
  - "方法论调取失败"
  - "参数范围遗漏"
  - "动作链断裂"
methods:
  - "第一型曲线积分极坐标法"
  - "极坐标曲线参数化"
  - "极坐标角域判定"
  - "极坐标弧长微元"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-157_参数范围遗漏"
  - "MATHWIKI-KNOWLEDGE-073_多元函数积分学"
  - "MATHWIKI-KNOWLEDGE-123_极坐标"
  - "MATHWIKI-KNOWLEDGE-151_曲线积分"
  - "MATHWIKI-METHOD-CLUSTER-1110_极坐标弧长微元"
  - "MATHWIKI-METHOD-CLUSTER-1111_极坐标曲线参数化"
  - "MATHWIKI-METHOD-CLUSTER-1112_极坐标角域判定"
  - "MATHWIKI-METHOD-CLUSTER-1281_第一型曲线积分极坐标法"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: 71383efcc5b18e62b6c86236f73d002df982ba57e72b281c8ba6008761cb7776
---

# GS-693 84892 第一型曲线积分极坐标参数化

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-693_84892第一型曲线积分极坐标参数化.md`
- wrongnet ID：`GS-693`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数积分学 |
| 题型 | 第一型曲线积分的极坐标计算 |
| 日期 | 2026-07-14 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 多元函数积分学
- 曲线积分
- 极坐标

### 错因

- 方法论调取失败
- 参数范围遗漏
- 动作链断裂

### 方法

- 第一型曲线积分极坐标法
- 极坐标曲线参数化
- 极坐标角域判定
- 极坐标弧长微元

### 陷阱

- 出现 $x^2+y^2$ 的曲线与径向被积函数时，不要错过极坐标入口。
- $r=-2\sin\theta$ 必须结合 $r\ge0$ 才能确定 $\theta$ 范围。
- $-2\sin\theta$ 的来源链是 $\sqrt{x^2+y^2}\to r\to$ 曲线条件，不能与 $ds$ 的计算混在一起。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先写 $x^2+y^2=r^2$、$y=r\sin\theta$，由 $r^2=-2r\sin\theta$ 得 $r=-2\sin\theta$，再用 $r\ge0$ 写出 $\theta$ 范围。 |
| missed_action | 没有从 $x^2+y^2$ 结构触发极坐标，也没有把被积函数化为 $r$ 与代入 $r=-2\sin\theta$ 分成两个连续步骤。 |
| related_method_card_id | H18-007 |
| next_reminder | 看到第一型曲线积分中曲线和被积函数同时含 $x^2+y^2$，先试极坐标；曲线、被积函数、$ds$ 三部分分别转换，最后再组合。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-157_参数范围遗漏]]
- [[MATHWIKI-KNOWLEDGE-073_多元函数积分学]]
- [[MATHWIKI-KNOWLEDGE-123_极坐标]]
- [[MATHWIKI-KNOWLEDGE-151_曲线积分]]
- [[MATHWIKI-METHOD-CLUSTER-1110_极坐标弧长微元]]
- [[MATHWIKI-METHOD-CLUSTER-1111_极坐标曲线参数化]]
- [[MATHWIKI-METHOD-CLUSTER-1112_极坐标角域判定]]
- [[MATHWIKI-METHOD-CLUSTER-1281_第一型曲线积分极坐标法]]

### 深度编译页

- 待编译到概念页、方法页、专题页、错因模式页或触发页

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
