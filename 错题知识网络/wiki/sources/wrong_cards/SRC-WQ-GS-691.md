---
wiki_id: SRC-WQ-GS-691
type: source_summary
title: "GS-691 102611 形心截面半径平方识别"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-691_102611形心截面半径平方识别.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-691"
knowledge:
  - "多元函数积分学"
  - "三重积分"
  - "二次曲面"
error_causes:
  - "公式记错"
  - "概念混淆"
  - "触发信息遗漏"
  - "动作链断裂"
methods:
  - "重积分应用"
  - "先二后一截面法"
  - "截面面积法"
  - "形心坐标公式"
  - "圆标准方程对照"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-015_公式记错"
  - "MATHWIKI-KNOWLEDGE-073_多元函数积分学"
  - "MATHWIKI-KNOWLEDGE-106_三重积分"
  - "MATHWIKI-KNOWLEDGE-132_二次曲面"
  - "MATHWIKI-METHOD-CLUSTER-155_截面面积法"
  - "MATHWIKI-METHOD-CLUSTER-194_先二后一截面法"
  - "MATHWIKI-METHOD-CLUSTER-471_重积分应用"
  - "MATHWIKI-METHOD-CLUSTER-846_圆标准方程对照"
  - "MATHWIKI-METHOD-CLUSTER-994_形心坐标公式"
status: indexed
last_updated: 2026-07-15
---

# GS-691 102611 形心截面半径平方识别

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-691_102611形心截面半径平方识别.md`
- wrongnet ID：`GS-691`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数积分学 |
| 题型 | 抛物面截顶区域的形心竖坐标 |
| 日期 | 2026-07-13 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 多元函数积分学
- 三重积分
- 二次曲面

### 错因

- 公式记错
- 概念混淆
- 触发信息遗漏
- 动作链断裂

### 方法

- 重积分应用
- 先二后一截面法
- 截面面积法
- 形心坐标公式
- 圆标准方程对照

### 陷阱

- 圆面积是 $\pi R^2$；$\frac12\pi R^2$ 只对应半圆面积。
- $x^2+y^2=z$ 中的 $z$ 是半径平方，不是半径。
- 半径是 $\sqrt z$，但截面面积化简后是 $\pi z$。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先把固定 $z$ 后的截面写成 $x^2+y^2\le R^2$，并比较得到 $R^2=z$。 |
| missed_action | 没有对照圆盘标准式区分 $R$ 与 $R^2$，同时对圆面积 $\pi R^2$ 不确定。 |
| related_method_card_id | H18-006 |
| next_reminder | 看到固定 $z$ 后出现 $x^2+y^2\le g(z)$，先写 $R^2=g(z)$，再写 $S(z)=\pi R^2$；不要把 $g(z)$ 直接当半径。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-015_公式记错]]
- [[MATHWIKI-KNOWLEDGE-073_多元函数积分学]]
- [[MATHWIKI-KNOWLEDGE-106_三重积分]]
- [[MATHWIKI-KNOWLEDGE-132_二次曲面]]
- [[MATHWIKI-METHOD-CLUSTER-155_截面面积法]]
- [[MATHWIKI-METHOD-CLUSTER-194_先二后一截面法]]
- [[MATHWIKI-METHOD-CLUSTER-471_重积分应用]]
- [[MATHWIKI-METHOD-CLUSTER-846_圆标准方程对照]]
- [[MATHWIKI-METHOD-CLUSTER-994_形心坐标公式]]

### 深度编译页

- 待编译到概念页、方法页、专题页、错因模式页或触发页

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-668

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
