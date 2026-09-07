---
wiki_id: SRC-WQ-GS-046
type: source_summary
title: "GS-046 强化例题13.3"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-046_强化例题13.3.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-046"
knowledge:
  - "极限与连续"
  - "多元函数微分学"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做入口是先把正定二次型分母配方成平方和，再丢非负项获得单变量下界夹逼，需用户复做确认是否为当时第一断点。"
methods:
  - "夹逼"
  - "分类讨论"
  - "夹逼准则"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-278_旧批量未记录个人原始错因-当前仅确认复做入口是先把正定二次型分母配方成平"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-016_夹逼准则"
  - "MATHWIKI-METHOD-CLUSTER-024_夹逼"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-046 强化例题13.3

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-046_强化例题13.3.md`
- wrongnet ID：`GS-046`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 极限与连续 |
| 题型 | 二元函数无穷远极限夹逼 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 极限与连续
- 多元函数微分学

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做入口是先把正定二次型分母配方成平方和，再丢非负项获得单变量下界夹逼，需用户复做确认是否为当时第一断点。

### 方法

- 夹逼
- 分类讨论
- 夹逼准则

### 陷阱

- 定义域
- 正负号
- 变量混淆
- 适用条件

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把分母配方成平方和，例如 \(x^2-xy+y^2=(y-x/2)^2+\frac34x^2\)，丢非负平方项得到单变量下界。 |
| missed_action | 个人原始作答未记录；当前只把题图解析确认的配方夹逼入口登记为复做检查点。 |
| related_method_card_id | H13-002 |
| next_reminder | 二元无穷远分式且分母为正定二次型，先配方成平方和，再丢非负项做夹逼。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-278_旧批量未记录个人原始错因-当前仅确认复做入口是先把正定二次型分母配方成平]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-016_夹逼准则]]
- [[MATHWIKI-METHOD-CLUSTER-024_夹逼]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
