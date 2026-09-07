---
wiki_id: SRC-WQ-GS-403
type: source_summary
title: "GS-403 2024年真题17"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-403_2024年真题17.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-403"
knowledge:
  - "二重积分"
  - "二重积分对称性"
error_causes:
  - "触发信息遗漏"
  - "方法调取失败"
methods:
  - "二重积分对称性"
  - "轮换对称性"
  - "区域面积计算"
  - "分段积分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-KNOWLEDGE-049_二重积分"
  - "MATHWIKI-KNOWLEDGE-107_二重积分对称性"
  - "MATHWIKI-METHOD-CLUSTER-077_二重积分对称性"
  - "MATHWIKI-METHOD-CLUSTER-1343_轮换对称性"
  - "MATHWIKI-METHOD-CLUSTER-310_分段积分"
  - "MATHWIKI-METHOD-CLUSTER-716_区域面积计算"
  - "MATHWIKI-GS-METHOD-035_二重积分对称性保号与轮换"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-403 2024年真题17

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-403_2024年真题17.md`
- wrongnet ID：`GS-403`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 二重积分 |
| 题型 | 二重积分计算 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二重积分
- 二重积分对称性

### 错因

- 触发信息遗漏
- 方法调取失败

### 方法

- 二重积分对称性
- 轮换对称性
- 区域面积计算
- 分段积分

### 陷阱

- 区域关于 y=x 对称
- f(x,y)+f(y,x) 为常数
- 面积分段上下界

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先写出交换 x,y 后的被积函数，并与原被积函数相加 |
| missed_action | 没有先检查区域关于 y=x 的轮换对称性 |
| related_method_card_id | H14-004 |
| next_reminder | 看到区域关于 y=x 对称，先交换 x,y 写出配对积分，再看相加是否简化。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-KNOWLEDGE-049_二重积分]]
- [[MATHWIKI-KNOWLEDGE-107_二重积分对称性]]
- [[MATHWIKI-METHOD-CLUSTER-077_二重积分对称性]]
- [[MATHWIKI-METHOD-CLUSTER-1343_轮换对称性]]
- [[MATHWIKI-METHOD-CLUSTER-310_分段积分]]
- [[MATHWIKI-METHOD-CLUSTER-716_区域面积计算]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-035_二重积分对称性保号与轮换]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-401
- GS-402
- GS-405
- GS-399
- GS-404
- GS-400
- GS-413

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
