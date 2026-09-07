---
wiki_id: SRC-WQ-GS-412
type: source_summary
title: "GS-412 2019年第18题-2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-412_2019年第18题-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-412"
knowledge:
  - "二重积分"
  - "二重积分对称性"
  - "二重积分极坐标法"
error_causes:
  - "触发信息遗漏"
  - "方法调取失败"
methods:
  - "二重积分对称性"
  - "二重积分极坐标法"
  - "奇偶性"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-KNOWLEDGE-049_二重积分"
  - "MATHWIKI-KNOWLEDGE-070_二重积分极坐标法"
  - "MATHWIKI-KNOWLEDGE-107_二重积分对称性"
  - "MATHWIKI-METHOD-CLUSTER-047_二重积分极坐标法"
  - "MATHWIKI-METHOD-CLUSTER-077_二重积分对称性"
  - "MATHWIKI-METHOD-CLUSTER-217_奇偶性"
  - "MATHWIKI-GS-METHOD-035_二重积分对称性保号与轮换"
  - "MATHWIKI-GS-METHOD-037_二重积分极坐标区域分块与对称化"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-412 2019年第18题-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-412_2019年第18题-2.md`
- wrongnet ID：`GS-412`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 二重积分 |
| 题型 | 二重积分极坐标对称计算 |
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

- 二重积分对称性
- 二重积分极坐标法
- 奇偶性

### 陷阱

- 与 GS-401 为同源重复候选，复做时优先对照主卡
- 先拆 \(\frac{x+y}{\sqrt{x^2+y^2}}\) 再用对称性
- 右半区角域由 \(|x|\le y\) 与 \(r\le\sin^2\theta\) 共同确定

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先确认本卡与 GS-401 同源，再拆分被积函数并消去关于 x 的奇部 |
| missed_action | 没有先把同源重复题归并到对称性入口 |
| related_method_card_id | H14-004 |
| next_reminder | 同源重复题优先对照主卡；对称区域先拆奇偶部，再写极坐标角域。 |

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
- [[MATHWIKI-METHOD-CLUSTER-077_二重积分对称性]]
- [[MATHWIKI-METHOD-CLUSTER-217_奇偶性]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-035_二重积分对称性保号与轮换]]
- [[MATHWIKI-GS-METHOD-037_二重积分极坐标区域分块与对称化]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-401
- GS-409
- GS-410
- GS-411

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
