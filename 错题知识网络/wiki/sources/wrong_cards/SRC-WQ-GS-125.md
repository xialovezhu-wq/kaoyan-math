---
wiki_id: SRC-WQ-GS-125
type: source_summary
title: "GS-125 1000题A组11.2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-125_1000题A组11.2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-125"
knowledge:
  - "定积分"
  - "变上限积分"
error_causes:
  - "已掌握"
methods:
  - "变上限积分求导"
  - "反函数关系"
  - "初值定常数"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-054_已掌握"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-METHOD-CLUSTER-015_变上限积分求导"
  - "MATHWIKI-METHOD-CLUSTER-037_初值定常数"
  - "MATHWIKI-METHOD-CLUSTER-777_反函数关系"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-125 1000题A组11.2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-125_1000题A组11.2.md`
- wrongnet ID：`GS-125`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 变上限积分方程求函数 |
| 日期 | 2026-05-07 |
| 状态 | 已掌握 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 变上限积分

### 错因

- 已掌握

### 方法

- 变上限积分求导
- 反函数关系
- 初值定常数

### 陷阱

- 忘记链式法则中的 $f^{\prime}(x)$
- 没有用反函数关系化简 $g(f(x))$
- 积分常数不由初值确定

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先对积分方程两边求导，写出 g(f(x))f'(x)=2x。 |
| missed_action | 旧批量导入未记录用户本人当时错因；本卡已掌握，此处只保留复做入口监控，不代表新的未掌握。 |
| related_method_card_id | H09-002 |
| next_reminder | 看到变上限积分方程，先求导；若出现反函数，马上检查 g(f(x))=x。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-054_已掌握]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-METHOD-CLUSTER-015_变上限积分求导]]
- [[MATHWIKI-METHOD-CLUSTER-037_初值定常数]]
- [[MATHWIKI-METHOD-CLUSTER-777_反函数关系]]

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
