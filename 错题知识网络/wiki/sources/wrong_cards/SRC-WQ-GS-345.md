---
wiki_id: SRC-WQ-GS-345
type: source_summary
title: "GS-345 强化例题11.19 135804 2026.4.28-4"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-345_强化例题11.191358042026.4.28-4.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-345"
knowledge:
  - "一元函数微分学应用"
  - "中值定理"
  - "凹凸性与拐点"
  - "定积分"
  - "定积分性质"
error_causes:
  - "触发信息遗漏"
  - "条件检查遗漏"
methods:
  - "凹凸性判定"
  - "最大值点拆区间"
  - "拉格朗日中值定理"
  - "牛顿莱布尼茨公式"
  - "放缩收尾"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-010_中值定理"
  - "MATHWIKI-KNOWLEDGE-018_凹凸性与拐点"
  - "MATHWIKI-METHOD-CLUSTER-014_拉格朗日中值定理"
  - "MATHWIKI-METHOD-CLUSTER-049_牛顿莱布尼茨公式"
  - "MATHWIKI-METHOD-CLUSTER-1048_放缩收尾"
  - "MATHWIKI-METHOD-CLUSTER-1087_最大值点拆区间"
  - "MATHWIKI-METHOD-CLUSTER-650_凹凸性判定"
  - "MATHWIKI-GS-METHOD-072_积分不等式证明入口链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-345 强化例题11.19 135804 2026.4.28-4

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-345_强化例题11.191358042026.4.28-4.md`
- wrongnet ID：`GS-345`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 凹函数积分不等式证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 中值定理
- 凹凸性与拐点
- 定积分
- 定积分性质

### 错因

- 触发信息遗漏
- 条件检查遗漏

### 方法

- 凹凸性判定
- 最大值点拆区间
- 拉格朗日中值定理
- 牛顿莱布尼茨公式
- 放缩收尾

### 陷阱

- 只想到罗尔定理而未用二阶导定号
- 未先判断分母正性
- 大区间没有拆成左右小区间

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先判断 f 在开区间内为正，并确定最大值点 |
| missed_action | 旧批量卡未记录用户个人错因；低置信推断为没有先用二阶导定号确认分母正性和拆区间入口 |
| related_method_card_id | H11-007 |
| next_reminder | 看到二阶导定号和分母含 f(x)，先判 f 的符号，再选最大值点拆区间。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-KNOWLEDGE-018_凹凸性与拐点]]
- [[MATHWIKI-METHOD-CLUSTER-014_拉格朗日中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-049_牛顿莱布尼茨公式]]
- [[MATHWIKI-METHOD-CLUSTER-1048_放缩收尾]]
- [[MATHWIKI-METHOD-CLUSTER-1087_最大值点拆区间]]
- [[MATHWIKI-METHOD-CLUSTER-650_凹凸性判定]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-072_积分不等式证明入口链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-052
- GS-231
- GS-347
- GS-248

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
