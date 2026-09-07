---
wiki_id: SRC-WQ-GS-293
type: source_summary
title: "GS-293 强化例题11.12（还原对称性）"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-293_强化例题11.12（还原对称性）.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-293"
knowledge:
  - "定积分"
  - "定积分性质"
  - "第二类换元"
error_causes:
  - "旧批量导入未记录个人错因；依据题图/解析确认的可复做断点是没有先配方还原圆形并平移到对称区间。"
methods:
  - "配方还原圆形"
  - "区间平移"
  - "奇偶性消项"
  - "半圆面积公式"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-254_旧批量导入未记录个人错因-依据题图-解析确认的可复做断点是没有先配方还原"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-041_第二类换元"
  - "MATHWIKI-METHOD-CLUSTER-078_区间平移"
  - "MATHWIKI-METHOD-CLUSTER-1389_配方还原圆形"
  - "MATHWIKI-METHOD-CLUSTER-350_奇偶性消项"
  - "MATHWIKI-METHOD-CLUSTER-724_半圆面积公式"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-293 强化例题11.12（还原对称性）

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-293_强化例题11.12（还原对称性）.md`
- wrongnet ID：`GS-293`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 根式定积分几何法计算 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 第二类换元

### 错因

- 旧批量导入未记录个人错因；依据题图/解析确认的可复做断点是没有先配方还原圆形并平移到对称区间。

### 方法

- 配方还原圆形
- 区间平移
- 奇偶性消项
- 半圆面积公式

### 陷阱

- 看到根式二次式后硬算
- 平移后忘记对称区间奇偶消项
- 半圆面积倍数漏乘

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先配方 \(4x-x^2=4-(x-2)^2\)，再令 \(t=x-2\) 把区间平移到 \([-2,2]\)。 |
| missed_action | 旧卡未保存用户当时动作；当前可确认的复做断点是没有先配圆和平移对称区间。 |
| related_method_card_id | H09-009 |
| next_reminder | 看到根式二次式定积分，先配方看圆，再平移区间检查奇偶。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-254_旧批量导入未记录个人错因-依据题图-解析确认的可复做断点是没有先配方还原]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-METHOD-CLUSTER-078_区间平移]]
- [[MATHWIKI-METHOD-CLUSTER-1389_配方还原圆形]]
- [[MATHWIKI-METHOD-CLUSTER-350_奇偶性消项]]
- [[MATHWIKI-METHOD-CLUSTER-724_半圆面积公式]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-577
- GS-634

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
