---
wiki_id: SRC-WQ-GS-401
type: source_summary
title: "GS-401 2019年第18题"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-401_2019年第18题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-401"
knowledge:
  - "二重积分"
  - "二重积分对称性"
  - "二重积分极坐标法"
error_causes:
  - "触发信息遗漏"
  - "方法调取失败"
methods:
  - "数形结合"
  - "二重积分对称性"
  - "二重积分极坐标法"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-KNOWLEDGE-049_二重积分"
  - "MATHWIKI-KNOWLEDGE-070_二重积分极坐标法"
  - "MATHWIKI-KNOWLEDGE-107_二重积分对称性"
  - "MATHWIKI-METHOD-CLUSTER-047_二重积分极坐标法"
  - "MATHWIKI-METHOD-CLUSTER-071_数形结合"
  - "MATHWIKI-METHOD-CLUSTER-077_二重积分对称性"
  - "MATHWIKI-GS-METHOD-035_二重积分对称性保号与轮换"
  - "MATHWIKI-GS-METHOD-037_二重积分极坐标区域分块与对称化"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-401 2019年第18题

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-401_2019年第18题.md`
- wrongnet ID：`GS-401`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 二重积分 |
| 题型 | 二重积分对称性 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二重积分
- 二重积分对称性
- 二重积分极坐标法

### 错因

- 触发信息遗漏
- 方法调取失败

### 方法

- 数形结合
- 二重积分对称性
- 二重积分极坐标法

### 陷阱

- 定义域
- 先用对称性拆分被积函数
- 极坐标角度范围由 |x|≤y 决定

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先把被积函数拆成 x 项和 y 项，并判断 x 项关于 x 为奇函数 |
| missed_action | 没有先拆被积函数并用 y 轴对称性消去奇部 |
| related_method_card_id | H14-004 |
| next_reminder | 看到对称区域中的二重积分，先拆被积函数奇偶部分，再决定是否只算半区。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-KNOWLEDGE-049_二重积分]]
- [[MATHWIKI-KNOWLEDGE-070_二重积分极坐标法]]
- [[MATHWIKI-KNOWLEDGE-107_二重积分对称性]]
- [[MATHWIKI-METHOD-CLUSTER-047_二重积分极坐标法]]
- [[MATHWIKI-METHOD-CLUSTER-071_数形结合]]
- [[MATHWIKI-METHOD-CLUSTER-077_二重积分对称性]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-035_二重积分对称性保号与轮换]]
- [[MATHWIKI-GS-METHOD-037_二重积分极坐标区域分块与对称化]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-400
- GS-402
- GS-403
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
