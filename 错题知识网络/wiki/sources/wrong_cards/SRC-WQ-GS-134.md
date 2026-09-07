---
wiki_id: SRC-WQ-GS-134
type: source_summary
title: "GS-134 1000题B组5.36"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-134_1000题B组5.36.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-134"
knowledge:
  - "一元函数微分学应用"
  - "单调性与极值"
  - "对数不等式"
  - "不等式证明"
error_causes:
  - "方法论调取失败"
  - "符号错误"
  - "结论复用遗漏"
methods:
  - "导数判单调"
  - "参数固定求最值"
  - "复用最值结论"
  - "对数不等式放缩"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-019_符号错误"
  - "MATHWIKI-ERROR-CLUSTER-418_结论复用遗漏"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-161_不等式证明"
  - "MATHWIKI-KNOWLEDGE-174_对数不等式"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-752_参数固定求最值"
  - "MATHWIKI-METHOD-CLUSTER-868_复用最值结论"
  - "MATHWIKI-METHOD-CLUSTER-905_对数不等式放缩"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-134 1000题B组5.36

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-134_1000题B组5.36.md`
- wrongnet ID：`GS-134`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 参数函数最值与不等式证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 单调性与极值
- 对数不等式
- 不等式证明

### 错因

- 方法论调取失败
- 符号错误
- 结论复用遗漏

### 方法

- 导数判单调
- 参数固定求最值
- 复用最值结论
- 对数不等式放缩

### 陷阱

- $0<a<1$ 时 $\ln a<0$
- $a^{-1/\ln a}=e^{-1}$
- 除以负数不等号反向

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先令 $a=y$，把第一问的最大值结论套到 $xy^x(1-y)$ 上。 |
| missed_action | 没有先复用第一问结论，而是重新散算；随后对 $\ln y<0$ 的除法变号处理不稳。 |
| related_method_card_id | H05-006 |
| next_reminder | 看到第二问和第一问同形，先固定参数复用前一问最值，再检查负数除法方向。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-019_符号错误]]
- [[MATHWIKI-ERROR-CLUSTER-418_结论复用遗漏]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-161_不等式证明]]
- [[MATHWIKI-KNOWLEDGE-174_对数不等式]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-752_参数固定求最值]]
- [[MATHWIKI-METHOD-CLUSTER-868_复用最值结论]]
- [[MATHWIKI-METHOD-CLUSTER-905_对数不等式放缩]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-524

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
