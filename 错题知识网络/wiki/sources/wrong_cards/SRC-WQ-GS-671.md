---
wiki_id: SRC-WQ-GS-671
type: source_summary
title: "GS-671 57959 对称拆区间判号"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-671_57959对称拆区间判号.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-671"
knowledge:
  - "定积分"
  - "定积分性质"
  - "函数单调性"
  - "分部积分"
  - "对称换元"
error_causes:
  - "触发信息遗漏"
  - "方法论调取失败"
  - "动作链断裂"
methods:
  - "先判型"
  - "区间拆分"
  - "区间再现"
  - "对称换元"
  - "积分保序"
  - "单调性比较"
  - "分部积分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-071_函数单调性"
  - "MATHWIKI-KNOWLEDGE-111_对称换元"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-048_区间拆分"
  - "MATHWIKI-METHOD-CLUSTER-060_积分保序"
  - "MATHWIKI-METHOD-CLUSTER-092_区间再现"
  - "MATHWIKI-METHOD-CLUSTER-095_对称换元"
  - "MATHWIKI-METHOD-CLUSTER-111_单调性比较"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-25
related_wrongnet_refs: []
formal_projection_sha256: 51581cb2c23ae75e413b753b7ec9bb63b0eee81df6a3f0cc97ddfc0f85e3b78a
---

# GS-671 57959 对称拆区间判号

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-671_57959对称拆区间判号.md`
- wrongnet ID：`GS-671`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 对称区间定积分符号判断 |
| 日期 | 2026-07-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 函数单调性
- 分部积分
- 对称换元

### 错因

- 触发信息遗漏
- 方法论调取失败
- 动作链断裂

### 方法

- 先判型
- 区间拆分
- 区间再现
- 对称换元
- 积分保序
- 单调性比较
- 分部积分

### 陷阱

- $\sin x$ 在 $[-\pi,0]$ 与 $[0,\pi]$ 上异号，不能只在原区间直接看整体正负。
- 对称区间上的 $\sin x$ 权函数常要先把负半轴换到正半轴，比较 $f(x)$ 与 $f(-x)$。
- $f'(x)<0$ 要转成 $x>0$ 时 $f(x)<f(-x)$，再与 $\sin x>0$ 结合。
- $\cos x$ 项可先分部积分成 $-f'(x)\sin x$，再复用前一类结论。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先把 $\int_{-\pi}^{\pi}f(x)\sin xdx$ 拆成 $\int_{-\pi}^{0}+\int_{0}^{\pi}$，再令 $x=-u$ 把前半段改写到 $[0,\pi]$。 |
| missed_action | 没有触发对称区间拆分和 $x=-u$ 换元再现，导致没有得到 $\int_0^\pi [f(x)-f(-x)]\sin xdx$ 这个可判号形式。 |
| related_method_card_id | H11-003 |
| next_reminder | 看到对称区间上的 $\sin x$、$\cos x$ 加单调性条件，先拆 $[-a,0]$ 与 $[0,a]$，把负半轴换到正半轴，再在同一区间比较。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-071_函数单调性]]
- [[MATHWIKI-KNOWLEDGE-111_对称换元]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-048_区间拆分]]
- [[MATHWIKI-METHOD-CLUSTER-060_积分保序]]
- [[MATHWIKI-METHOD-CLUSTER-092_区间再现]]
- [[MATHWIKI-METHOD-CLUSTER-095_对称换元]]
- [[MATHWIKI-METHOD-CLUSTER-111_单调性比较]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

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
