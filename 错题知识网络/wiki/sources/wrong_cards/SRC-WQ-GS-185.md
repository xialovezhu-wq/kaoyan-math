---
wiki_id: SRC-WQ-GS-185
type: source_summary
title: "GS-185 1000题A组8.6 正负面积选区间最小"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-185_1000题A组8.6.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-185"
knowledge:
  - "定积分"
  - "定积分性质"
  - "平面图形面积"
  - "积分保号"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是定积分最小值选区间时没有先找函数零点和正负面积分布，需用户复做确认。"
methods:
  - "定积分几何意义"
  - "函数正负区间判断"
  - "图像面积比较"
  - "分段函数积分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-310_旧批量未记录个人原始错因-当前仅确认复做断点是定积分最小值选区间时没有先"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-060_平面图形面积"
  - "MATHWIKI-KNOWLEDGE-184_积分保号"
  - "MATHWIKI-METHOD-CLUSTER-065_分段函数积分"
  - "MATHWIKI-METHOD-CLUSTER-343_图像面积比较"
  - "MATHWIKI-METHOD-CLUSTER-661_函数正负区间判断"
  - "MATHWIKI-METHOD-CLUSTER-894_定积分几何意义"
  - "MATHWIKI-GS-METHOD-064_正负面积选积分区间"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-185 1000题A组8.6 正负面积选区间最小

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-185_1000题A组8.6.md`
- wrongnet ID：`GS-185`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 定积分几何意义：正负面积比较选区间 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 平面图形面积
- 积分保号

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是定积分最小值选区间时没有先找函数零点和正负面积分布，需用户复做确认。

### 方法

- 定积分几何意义
- 函数正负区间判断
- 图像面积比较
- 分段函数积分

### 陷阱

- 积分最小不是区间最长，而是负面积尽量多、正面积尽量少
- \(x\ln x\) 在 \((0,1)\) 上为负，在 \((1,+\infty)\) 上为正
- \(x^2+x=x(x+1)\) 在 \((-1,0)\) 上为负

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先找分段函数的零点和正负区间 |
| missed_action | 旧批量未记录个人第一错步；当前只确认不能机械计算四个选项而忽略正负面积净贡献 |
| related_method_card_id | H10-001 |
| next_reminder | 看到定积分区间最值选择，先找零点和正负区间，再比较带符号面积。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-310_旧批量未记录个人原始错因-当前仅确认复做断点是定积分最小值选区间时没有先]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-060_平面图形面积]]
- [[MATHWIKI-KNOWLEDGE-184_积分保号]]
- [[MATHWIKI-METHOD-CLUSTER-065_分段函数积分]]
- [[MATHWIKI-METHOD-CLUSTER-343_图像面积比较]]
- [[MATHWIKI-METHOD-CLUSTER-661_函数正负区间判断]]
- [[MATHWIKI-METHOD-CLUSTER-894_定积分几何意义]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-064_正负面积选积分区间]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-294

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
