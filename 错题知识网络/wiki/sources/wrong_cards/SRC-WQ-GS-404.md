---
wiki_id: SRC-WQ-GS-404
type: source_summary
title: "GS-404 强化例题14.6"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-404_强化例题14.6.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-404"
knowledge:
  - "二重积分"
  - "二重积分换序"
  - "二重积分极坐标法"
error_causes:
  - "方法调取失败"
  - "变量混淆"
methods:
  - "二重积分换序"
  - "换元"
  - "条件转化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-ERROR-CLUSTER-024_变量混淆"
  - "MATHWIKI-KNOWLEDGE-049_二重积分"
  - "MATHWIKI-KNOWLEDGE-070_二重积分极坐标法"
  - "MATHWIKI-KNOWLEDGE-190_二重积分换序"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-009_换元"
  - "MATHWIKI-METHOD-CLUSTER-190_二重积分换序"
  - "MATHWIKI-GS-METHOD-034_二重积分区域化归与换序"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-398"
  - "GS-411"
formal_projection_sha256: 332d66a2985e6d3feaff8bb05ecf70dc4b1950160cc63c82e409aad7118d0930
---

# GS-404 强化例题14.6

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-404_强化例题14.6.md`
- wrongnet ID：`GS-404`
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
- 二重积分换序
- 二重积分极坐标法

### 错因

- 方法调取失败
- 变量混淆

### 方法

- 二重积分换序
- 换元
- 条件转化

### 陷阱

- 极坐标给的是区域而不是必须用极坐标积分
- \(u=x-y\) 后要重新描述 \(0\le u\le x\le1\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先把极坐标区域转成直角坐标三角形 0≤y≤x≤1 |
| missed_action | 没有先判断极坐标只是描述区域，而非必须用极坐标积分 |
| related_method_card_id | H14-002 |
| next_reminder | 看到极坐标区域但被积函数含 x-y，先判断是否转回直角坐标更简单。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-024_变量混淆]]
- [[MATHWIKI-KNOWLEDGE-049_二重积分]]
- [[MATHWIKI-KNOWLEDGE-070_二重积分极坐标法]]
- [[MATHWIKI-KNOWLEDGE-190_二重积分换序]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-009_换元]]
- [[MATHWIKI-METHOD-CLUSTER-190_二重积分换序]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-034_二重积分区域化归与换序]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-398
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
