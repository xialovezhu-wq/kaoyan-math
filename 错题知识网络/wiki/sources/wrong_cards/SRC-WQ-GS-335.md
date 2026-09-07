---
wiki_id: SRC-WQ-GS-335
type: source_summary
title: "GS-335 强化例题11.16-2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-335_强化例题11.16-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-335"
knowledge:
  - "定积分"
  - "第一类换元"
  - "复合函数求导"
error_causes:
  - "概念混淆"
  - "方法调取失败"
methods:
  - "对数变量还原"
  - "牛顿莱布尼茨公式"
  - "换元"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-030_复合函数求导"
  - "MATHWIKI-METHOD-CLUSTER-009_换元"
  - "MATHWIKI-METHOD-CLUSTER-049_牛顿莱布尼茨公式"
  - "MATHWIKI-METHOD-CLUSTER-909_对数变量还原"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-335 强化例题11.16-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-335_强化例题11.16-2.md`
- wrongnet ID：`GS-335`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 定积分求函数值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 第一类换元
- 复合函数求导

### 错因

- 概念混淆
- 方法调取失败

### 方法

- 对数变量还原
- 牛顿莱布尼茨公式
- 换元

### 陷阱

- 把 $f^{\prime}(\ln x)$ 直接当 $f^{\prime}(x)$
- 没有按 $t$ 的正负判断分段
- 换元时漏 $dt=dx/x$

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先写 \(f(1)-f(0)=\int_0^1 f'(t)\,dt\)，再令 \(x=e^t\) 建立 \(f'(t)\) |
| missed_action | 没有先统一导函数自变量 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到 \(f'(\ln x)\)，先把导函数自变量还原成统一变量，再积分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-030_复合函数求导]]
- [[MATHWIKI-METHOD-CLUSTER-009_换元]]
- [[MATHWIKI-METHOD-CLUSTER-049_牛顿莱布尼茨公式]]
- [[MATHWIKI-METHOD-CLUSTER-909_对数变量还原]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-324
- GS-336
- GS-283

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
