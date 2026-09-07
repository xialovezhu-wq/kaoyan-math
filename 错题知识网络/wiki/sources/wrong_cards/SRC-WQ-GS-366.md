---
wiki_id: SRC-WQ-GS-366
type: source_summary
title: "GS-366 强化例题13.14"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-366_强化例题13.14.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-366"
knowledge:
  - "多元函数微分学"
  - "全微分"
  - "多元函数偏导"
error_causes:
  - "方法入口未沉淀"
  - "条件检查遗漏"
methods:
  - "全微分条件"
  - "偏导匹配"
  - "变量参数分离"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-012_方法入口未沉淀"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-KNOWLEDGE-088_全微分"
  - "MATHWIKI-METHOD-CLUSTER-069_变量参数分离"
  - "MATHWIKI-METHOD-CLUSTER-294_偏导匹配"
  - "MATHWIKI-METHOD-CLUSTER-296_全微分条件"
  - "MATHWIKI-GS-METHOD-046_多元公式模板入口链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-366 强化例题13.14

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-366_强化例题13.14.md`
- wrongnet ID：`GS-366`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 全微分恰当性判参 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数微分学
- 全微分
- 多元函数偏导

### 错因

- 方法入口未沉淀
- 条件检查遗漏

### 方法

- 全微分条件
- 偏导匹配
- 变量参数分离

### 陷阱

- 分母整体求导
- 变量混淆
- 参数项漏求导

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先写 \(M=\frac{x+ay}{(x+y)^2},\ N=\frac{y}{(x+y)^2}\)，再计算 \(M_y,N_x\)。 |
| missed_action | 历史卡只写答案，没有沉淀 \(M_y=N_x\) 这个入口。 |
| related_method_card_id | H13-009 |
| next_reminder | 看到某个微分形式是全微分，先写 M、N，再查 \(M_y=N_x\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-012_方法入口未沉淀]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-KNOWLEDGE-088_全微分]]
- [[MATHWIKI-METHOD-CLUSTER-069_变量参数分离]]
- [[MATHWIKI-METHOD-CLUSTER-294_偏导匹配]]
- [[MATHWIKI-METHOD-CLUSTER-296_全微分条件]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-046_多元公式模板入口链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-379
- GS-376

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
