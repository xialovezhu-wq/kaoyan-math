---
wiki_id: SRC-WQ-GS-304
type: source_summary
title: "GS-304 强化例题10.12：无界区域旋转体体积"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-304_强化例题10.12.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-304"
knowledge:
  - "定积分"
  - "旋转体体积"
  - "反常积分"
  - "Gamma型积分"
error_causes:
  - "目标识别断点"
  - "运算路径不稳"
methods:
  - "旋转体体积公式"
  - "无界区间反常积分"
  - "Gamma 函数积分"
  - "指数换元"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-006_B1-GOAL"
  - "MATHWIKI-ERROR-CLUSTER-028_运算路径不稳"
  - "MATHWIKI-ERROR-CLUSTER-034_目标识别断点"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-028_反常积分"
  - "MATHWIKI-KNOWLEDGE-149_旋转体体积"
  - "MATHWIKI-KNOWLEDGE-222_Gamma型积分"
  - "MATHWIKI-METHOD-CLUSTER-1063_无界区间反常积分"
  - "MATHWIKI-METHOD-CLUSTER-160_指数换元"
  - "MATHWIKI-METHOD-CLUSTER-163_旋转体体积公式"
  - "MATHWIKI-METHOD-CLUSTER-479_Gamma函数积分"
  - "MATHWIKI-GS-METHOD-083_旋转体曲面变量选择与生成量链"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-304 强化例题10.12：无界区域旋转体体积

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-304_强化例题10.12.md`
- wrongnet ID：`GS-304`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分应用 |
| 题型 | 无界区域旋转体体积 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 旋转体体积
- 反常积分
- Gamma型积分

### 错因

- 目标识别断点
- 运算路径不稳

### 方法

- 旋转体体积公式
- 无界区间反常积分
- Gamma 函数积分
- 指数换元

### 陷阱

- 绕 \(x\) 轴旋转体体积用 \(V=\pi\int f^2(x)\,dx\)
- 无界区域要写成 \(\int_0^{+\infty}\)
- \((\sqrt x e^{-3x/2})^2=x e^{-3x}\)，指数系数会变成 \(3x\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B1-GOAL |
| expected_first_action | 先写 V=pi∫_0^{+infty} f^2(x) dx |
| missed_action | 旧卡未记录个人动作缺口；可确认的复做断点是先识别体积目标和反常积分边界 |
| related_method_card_id | H10-002 |
| next_reminder | 看到无界区域绕轴旋转求体积，先写反常体积积分，再平方函数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-006_B1-GOAL]]
- [[MATHWIKI-ERROR-CLUSTER-028_运算路径不稳]]
- [[MATHWIKI-ERROR-CLUSTER-034_目标识别断点]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-028_反常积分]]
- [[MATHWIKI-KNOWLEDGE-149_旋转体体积]]
- [[MATHWIKI-KNOWLEDGE-222_Gamma型积分]]
- [[MATHWIKI-METHOD-CLUSTER-1063_无界区间反常积分]]
- [[MATHWIKI-METHOD-CLUSTER-160_指数换元]]
- [[MATHWIKI-METHOD-CLUSTER-163_旋转体体积公式]]
- [[MATHWIKI-METHOD-CLUSTER-479_Gamma函数积分]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-083_旋转体曲面变量选择与生成量链]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-297

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
