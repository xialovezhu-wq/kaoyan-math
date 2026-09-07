---
wiki_id: SRC-WQ-GS-187
type: source_summary
title: "GS-187 强化例题15.1（2️⃣（1））"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-187_强化例题15.1（2️⃣（1））.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-187"
knowledge:
  - "齐次微分方程"
error_causes:
  - "暂无明确个人错因：旧卡未记录作答过程"
methods:
  - "齐次方程换元"
  - "分离变量"
  - "变量代换"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程"
  - "MATHWIKI-KNOWLEDGE-280_齐次微分方程"
  - "MATHWIKI-METHOD-CLUSTER-066_分离变量"
  - "MATHWIKI-METHOD-CLUSTER-476_齐次方程换元"
  - "MATHWIKI-METHOD-CLUSTER-807_变量代换"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-056_微分方程入口判别链"
  - "MATHWIKI-GS-TOPIC-009_微分方程错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-187 强化例题15.1（2️⃣（1））

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-187_强化例题15.1（2️⃣（1））.md`
- wrongnet ID：`GS-187`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 微分方程 |
| 题型 | 齐次型一阶微分方程 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 齐次微分方程

### 错因

- 暂无明确个人错因：旧卡未记录作答过程

### 方法

- 齐次方程换元
- 分离变量
- 变量代换

### 陷阱

- 先整理成 \(y'=f(y/x)\)
- 换元后 \(y'=u+xu'\)
- 积分后要回代并合并对数项

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先整理成 \(y'=f(y/x)\)，令 \(u=y/x\) |
| missed_action | 缺少用户本人作答过程；待确认是否漏掉齐次换元入口或 \(y'=u+xu'\) 这一步 |
| related_method_card_id | H15-004 |
| next_reminder | 看到一阶方程能写成 \(y'=f(y/x)\)，先令 \(u=y/x\)，再写 \(y'=u+xu'\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-022_暂无明确个人错因-旧卡未记录作答过程]]
- [[MATHWIKI-KNOWLEDGE-280_齐次微分方程]]
- [[MATHWIKI-METHOD-CLUSTER-066_分离变量]]
- [[MATHWIKI-METHOD-CLUSTER-476_齐次方程换元]]
- [[MATHWIKI-METHOD-CLUSTER-807_变量代换]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-056_微分方程入口判别链]]
- [[MATHWIKI-GS-TOPIC-009_微分方程错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-188

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
