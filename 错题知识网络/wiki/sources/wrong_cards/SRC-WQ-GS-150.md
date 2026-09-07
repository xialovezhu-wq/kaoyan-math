---
wiki_id: SRC-WQ-GS-150
type: source_summary
title: "GS-150 强化例题5.7"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-150_强化例题5.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-150"
knowledge:
  - "一元函数微分学应用"
  - "反函数"
  - "渐近线"
  - "无穷远极限"
error_causes:
  - "条件检查遗漏"
  - "收尾验证遗漏"
methods:
  - "反函数求法"
  - "水平渐近线判定"
  - "正负无穷分别讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-032_收尾验证遗漏"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-085_渐近线"
  - "MATHWIKI-KNOWLEDGE-093_无穷远极限"
  - "MATHWIKI-KNOWLEDGE-171_反函数"
  - "MATHWIKI-METHOD-CLUSTER-1161_水平渐近线判定"
  - "MATHWIKI-METHOD-CLUSTER-238_正负无穷分别讨论"
  - "MATHWIKI-METHOD-CLUSTER-326_反函数求法"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-150 强化例题5.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-150_强化例题5.7.md`
- wrongnet ID：`GS-150`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 反函数渐近线判断 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 反函数
- 渐近线
- 无穷远极限

### 错因

- 条件检查遗漏
- 收尾验证遗漏

### 方法

- 反函数求法
- 水平渐近线判定
- 正负无穷分别讨论

### 陷阱

- 反函数变量互换
- 正负无穷都要查
- 双水平渐近线

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先解出 $g(x)=3\frac{e^{2x}-1}{e^{2x}+1}$，再分别算 $x\to+\infty$ 和 $x\to-\infty$ 的极限。 |
| missed_action | 只看了一个无穷远方向，漏掉另一条水平渐近线。 |
| related_method_card_id | H05-005 |
| next_reminder | 看到反函数渐近线，先求反函数，再把 $+\infty$ 和 $-\infty$ 两个方向都算完。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-032_收尾验证遗漏]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-085_渐近线]]
- [[MATHWIKI-KNOWLEDGE-093_无穷远极限]]
- [[MATHWIKI-KNOWLEDGE-171_反函数]]
- [[MATHWIKI-METHOD-CLUSTER-1161_水平渐近线判定]]
- [[MATHWIKI-METHOD-CLUSTER-238_正负无穷分别讨论]]
- [[MATHWIKI-METHOD-CLUSTER-326_反函数求法]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

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
