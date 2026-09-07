---
wiki_id: SRC-WQ-GS-189
type: source_summary
title: "GS-189 强化例题15.3"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-189_强化例题15.3.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-189"
knowledge:
  - "一阶线性微分方程"
  - "微分方程周期解"
error_causes:
  - "暂无明确个人错因：旧卡未记录作答过程"
methods:
  - "一阶线性齐次通解"
  - "周期函数积分性质"
  - "充要条件判别"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程"
  - "MATHWIKI-KNOWLEDGE-065_一阶线性微分方程"
  - "MATHWIKI-KNOWLEDGE-363_微分方程周期解"
  - "MATHWIKI-METHOD-CLUSTER-508_一阶线性齐次通解"
  - "MATHWIKI-METHOD-CLUSTER-615_充要条件判别"
  - "MATHWIKI-METHOD-CLUSTER-829_周期函数积分性质"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-056_微分方程入口判别链"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: c54691dbb2656114c3a40316bc72a1b3f6fe7af2a5185beafa9a7a1626d7bd8f
---

# GS-189 强化例题15.3

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-189_强化例题15.3.md`
- wrongnet ID：`GS-189`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 微分方程 |
| 题型 | 一阶线性齐次微分方程周期解判别 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一阶线性微分方程
- 微分方程周期解

### 错因

- 暂无明确个人错因：旧卡未记录作答过程

### 方法

- 一阶线性齐次通解
- 周期函数积分性质
- 充要条件判别

### 陷阱

- 周期解要比较 \(y(x+T)\) 与 \(y(x)\)
- 非零解不能只看 \(C=0\)
- 利用周期函数一周期积分与起点无关

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写 \(y=Ce^{-\int p(x)\,dx}\) |
| missed_action | 缺少用户本人作答过程；待确认是否没有把周期条件代回通解比较 |
| related_method_card_id | H15-005 |
| next_reminder | 看到周期解条件，先写齐次通解，再比较 \(y(x+T)\) 与 \(y(x)\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程]]
- [[MATHWIKI-KNOWLEDGE-065_一阶线性微分方程]]
- [[MATHWIKI-KNOWLEDGE-363_微分方程周期解]]
- [[MATHWIKI-METHOD-CLUSTER-508_一阶线性齐次通解]]
- [[MATHWIKI-METHOD-CLUSTER-615_充要条件判别]]
- [[MATHWIKI-METHOD-CLUSTER-829_周期函数积分性质]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-056_微分方程入口判别链]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

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
