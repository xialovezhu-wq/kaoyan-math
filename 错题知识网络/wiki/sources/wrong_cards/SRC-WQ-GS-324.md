---
wiki_id: SRC-WQ-GS-324
type: source_summary
title: "GS-324 强化例题11.16"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-324_强化例题11.16.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-324"
knowledge:
  - "定积分"
  - "定积分性质"
  - "第二类换元"
error_causes:
  - "函数自变量识别混淆"
  - "方法论调取失败"
methods:
  - "牛顿莱布尼茨公式"
  - "对数变量换元"
  - "变量角色转换"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-005_A-CONCEPT"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-042_函数自变量识别混淆"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-041_第二类换元"
  - "MATHWIKI-METHOD-CLUSTER-049_牛顿莱布尼茨公式"
  - "MATHWIKI-METHOD-CLUSTER-811_变量角色转换"
  - "MATHWIKI-METHOD-CLUSTER-908_对数变量换元"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-324 强化例题11.16

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-324_强化例题11.16.md`
- wrongnet ID：`GS-324`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 导函数变量换元求值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 第二类换元

### 错因

- 函数自变量识别混淆
- 方法论调取失败

### 方法

- 牛顿莱布尼茨公式
- 对数变量换元
- 变量角色转换

### 陷阱

- 把 f''(ln x) 直接当 f''(x)
- 换元时漏 dx/x
- 没有先确认目标积分区间对应的分段

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | A-CONCEPT |
| expected_first_action | 先写 f(1)-f(0) 等于 0 到 1 上 f'(t) 的积分 |
| missed_action | 把 f'(ln x) 直接当成关于 x 的导数信息 |
| related_method_card_id | H09-003 |
| next_reminder | 看到 f'(ln x)，先把 ln x 设成导数自变量，再做 x=e^t 换元。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-005_A-CONCEPT]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-042_函数自变量识别混淆]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-METHOD-CLUSTER-049_牛顿莱布尼茨公式]]
- [[MATHWIKI-METHOD-CLUSTER-811_变量角色转换]]
- [[MATHWIKI-METHOD-CLUSTER-908_对数变量换元]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-335

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
