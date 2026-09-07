---
wiki_id: SRC-WQ-GS-195
type: source_summary
title: "GS-195 强化例题15.10：常系数特征根反推方程"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-195_强化例题15.10.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-195"
knowledge:
  - "微分方程"
  - "高阶常系数线性微分方程"
  - "特征方程"
error_causes:
  - "题型入口风险：由已知解的指数、三角和 $t e^t$ 因子反推出特征根与重数。"
methods:
  - "特征根反推特征方程"
  - "复根对应三角函数"
  - "重根判别"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-454_题型入口风险-由已知解的指数、三角和$te^t$因子反推出特征根与重数"
  - "MATHWIKI-KNOWLEDGE-031_微分方程"
  - "MATHWIKI-KNOWLEDGE-158_特征方程"
  - "MATHWIKI-KNOWLEDGE-160_高阶常系数线性微分方程"
  - "MATHWIKI-METHOD-CLUSTER-1192_特征根反推特征方程"
  - "MATHWIKI-METHOD-CLUSTER-1391_重根判别"
  - "MATHWIKI-METHOD-CLUSTER-865_复根对应三角函数"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-195 强化例题15.10：常系数特征根反推方程

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-195_强化例题15.10.md`
- wrongnet ID：`GS-195`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 高等数学-微分方程 |
| 题型 | 高阶常系数线性微分方程反推 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 微分方程
- 高阶常系数线性微分方程
- 特征方程

### 错因

- 题型入口风险：由已知解的指数、三角和 $t e^t$ 因子反推出特征根与重数。

### 方法

- 特征根反推特征方程
- 复根对应三角函数
- 重根判别

### 陷阱

- $te^t$ 表示 $\lambda=1$ 二重根
- $\sin2t$ 对应 $\lambda=\pm2i$
- 特征多项式展开符号要稳

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把 \(te^t\) 译为 \(\lambda=1\) 二重根，把 \(\sin2t\) 译为 \(\lambda=\pm2i\) |
| missed_action | 缺少用户本人作答过程；待确认是否漏掉 \(te^t\) 的重根或三角函数的共轭复根 |
| related_method_card_id | H15-009 |
| next_reminder | 看到已知解反推方程，先把每个解翻译成特征根和重数，再构造特征多项式。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-454_题型入口风险-由已知解的指数、三角和$te^t$因子反推出特征根与重数]]
- [[MATHWIKI-KNOWLEDGE-031_微分方程]]
- [[MATHWIKI-KNOWLEDGE-158_特征方程]]
- [[MATHWIKI-KNOWLEDGE-160_高阶常系数线性微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-1192_特征根反推特征方程]]
- [[MATHWIKI-METHOD-CLUSTER-1391_重根判别]]
- [[MATHWIKI-METHOD-CLUSTER-865_复根对应三角函数]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-196
- GS-197

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
