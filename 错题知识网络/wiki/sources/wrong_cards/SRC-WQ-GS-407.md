---
wiki_id: SRC-WQ-GS-407
type: source_summary
title: "GS-407 强化例题14.7"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-407_强化例题14.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-407"
knowledge:
  - "二重积分"
  - "二重积分极坐标法"
error_causes:
  - "触发信息遗漏"
  - "方法调取失败"
methods:
  - "二重积分极坐标法"
  - "三角换元"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-KNOWLEDGE-049_二重积分"
  - "MATHWIKI-KNOWLEDGE-070_二重积分极坐标法"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-028_三角换元"
  - "MATHWIKI-METHOD-CLUSTER-047_二重积分极坐标法"
  - "MATHWIKI-GS-METHOD-036_二重积分换元与雅可比链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-407 强化例题14.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-407_强化例题14.7.md`
- wrongnet ID：`GS-407`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 二重积分 |
| 题型 | 二重积分极坐标计算 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二重积分
- 二重积分极坐标法

### 错因

- 触发信息遗漏
- 方法调取失败

### 方法

- 二重积分极坐标法
- 三角换元
- 条件转化

### 陷阱

- \(x^2+y^2-xy=c\) 在极坐标下不是常半径圆
- 先对 \(r\) 积分可利用两条边界半径比恒为 \(\sqrt2\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先令 x=r cosθ、y=r sinθ，写出 x²+y²-xy 的极坐标形式 |
| missed_action | 没有先把二次型边界转成 r(θ) 并比较上下半径 |
| related_method_card_id | H14-005 |
| next_reminder | 看到二次型边界和射线边界，先试极坐标并检查半径上下界比值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-KNOWLEDGE-049_二重积分]]
- [[MATHWIKI-KNOWLEDGE-070_二重积分极坐标法]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-047_二重积分极坐标法]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-036_二重积分换元与雅可比链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-409
- GS-410
- GS-411
- GS-412

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
