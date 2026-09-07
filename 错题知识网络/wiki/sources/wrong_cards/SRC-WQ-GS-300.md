---
wiki_id: SRC-WQ-GS-300
type: source_summary
title: "GS-300 2023年真题第12题：变上限积分曲线弧长"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-300_2023年真题第12题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-300"
knowledge:
  - "定积分"
  - "曲线弧长"
  - "变上限积分"
error_causes:
  - "条件检查遗漏"
  - "动作链断裂"
methods:
  - "确定变上限函数定义域"
  - "变上限积分求导"
  - "曲线弧长公式"
  - "三角换元"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-069_曲线弧长"
  - "MATHWIKI-METHOD-CLUSTER-015_变上限积分求导"
  - "MATHWIKI-METHOD-CLUSTER-028_三角换元"
  - "MATHWIKI-METHOD-CLUSTER-120_曲线弧长公式"
  - "MATHWIKI-METHOD-CLUSTER-1241_确定变上限函数定义域"
  - "MATHWIKI-GS-METHOD-082_曲线弧长定义域与根式化简链"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-300 2023年真题第12题：变上限积分曲线弧长

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-300_2023年真题第12题.md`
- wrongnet ID：`GS-300`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分应用 |
| 题型 | 变上限积分定义曲线弧长 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 曲线弧长
- 变上限积分

### 错因

- 条件检查遗漏
- 动作链断裂

### 方法

- 确定变上限函数定义域
- 变上限积分求导
- 曲线弧长公式
- 三角换元

### 陷阱

- 根号 \(\sqrt{3-t^2}\) 要先限制 \(-\sqrt3\le x\le\sqrt3\)
- 弧长积分是 \(\int\sqrt{1+[y'(x)]^2}\,dx\)，不是原函数面积
- \(\int\sqrt{4-x^2}\,dx\) 可用圆面积或三角换元

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先由 3-x^2>=0 写出 -sqrt(3)<=x<=sqrt(3) |
| missed_action | 旧卡未记录个人动作缺口；可确认的复做断点是弧长前先定定义域和求 y'(x) |
| related_method_card_id | H10-003 |
| next_reminder | 看到变上限积分曲线全长，先定定义域，再求导套弧长公式。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-069_曲线弧长]]
- [[MATHWIKI-METHOD-CLUSTER-015_变上限积分求导]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-120_曲线弧长公式]]
- [[MATHWIKI-METHOD-CLUSTER-1241_确定变上限函数定义域]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-082_曲线弧长定义域与根式化简链]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-299

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
