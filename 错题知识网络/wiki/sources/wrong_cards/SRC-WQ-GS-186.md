---
wiki_id: SRC-WQ-GS-186
type: source_summary
title: "GS-186 2023年第15题 平移差分定积分求值"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-186_2023年第15题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-186"
knowledge:
  - "定积分"
  - "定积分等式"
  - "定积分性质"
  - "第一类换元"
  - "平移变换"
  - "一元函数积分学的计算"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是没有先把目标积分拆成两个相差 2 的同长区间积分之差，需用户复做确认。"
methods:
  - "定积分区间可加性"
  - "区间平移"
  - "定积分换元"
  - "平移差分关系"
  - "定积分等式"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-332_旧批量未记录个人原始错因-当前仅确认复做断点是没有先把目标积分拆成两个相"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-084_定积分等式"
  - "MATHWIKI-KNOWLEDGE-177_平移变换"
  - "MATHWIKI-METHOD-CLUSTER-078_区间平移"
  - "MATHWIKI-METHOD-CLUSTER-094_定积分换元"
  - "MATHWIKI-METHOD-CLUSTER-353_定积分区间可加性"
  - "MATHWIKI-METHOD-CLUSTER-367_平移差分关系"
  - "MATHWIKI-METHOD-CLUSTER-899_定积分等式"
  - "MATHWIKI-GS-METHOD-054_平移差分定积分区间转化"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-186 2023年第15题 平移差分定积分求值

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-186_2023年第15题.md`
- wrongnet ID：`GS-186`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 平移差分方程定积分求值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分等式
- 定积分性质
- 第一类换元
- 平移变换
- 一元函数积分学的计算

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是没有先把目标积分拆成两个相差 2 的同长区间积分之差，需用户复做确认。

### 方法

- 定积分区间可加性
- 区间平移
- 定积分换元
- 平移差分关系
- 定积分等式

### 陷阱

- 不要试图先求出 \(f(x)\) 本身
- \(\int_0^2 f(x)\,dx=0\) 要用于拆补区间，不只是背景条件
- \([2,3]\) 平移到 \([0,1]\) 后，才能直接套 \(f(u+2)-f(u)=u\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先用已知积分把目标区间拆成两个相差 2 的同长区间 |
| missed_action | 旧批量未记录个人第一错步；当前只确认不能先硬求 f(x) 本身 |
| related_method_card_id | H11-001 |
| next_reminder | 看到函数平移差分和区间积分，先拆成相差 T 的同长区间，再平移换元代入差分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-332_旧批量未记录个人原始错因-当前仅确认复做断点是没有先把目标积分拆成两个相]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-084_定积分等式]]
- [[MATHWIKI-KNOWLEDGE-177_平移变换]]
- [[MATHWIKI-METHOD-CLUSTER-078_区间平移]]
- [[MATHWIKI-METHOD-CLUSTER-094_定积分换元]]
- [[MATHWIKI-METHOD-CLUSTER-353_定积分区间可加性]]
- [[MATHWIKI-METHOD-CLUSTER-367_平移差分关系]]
- [[MATHWIKI-METHOD-CLUSTER-899_定积分等式]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-054_平移差分定积分区间转化]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-310
- GS-311
- GS-338
- GS-575
- GS-634

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
