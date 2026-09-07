---
wiki_id: SRC-WQ-GS-269
type: source_summary
title: "GS-269 强化例题9.3（1）"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-269_强化例题9.3（1）.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-269_强化例题9.3（1）.md"
visual_ids:
  - "VIS-GS-269"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-269/question_01.png"
wrongnet_refs:
  - "GS-269"
knowledge:
  - "不定积分"
  - "根式积分"
  - "三角换元"
  - "倒代换"
  - "第二类换元"
  - "回代化简"
  - "原函数分定义域连通区间理解"
error_causes:
  - "表达：最后回代时没有保持倒数结构，把 $1/\sin t$ 按 $\sin t$ 代入。"
  - "检查：主体换元正确后没有逐层核对外层负号、倒数与三角关系的对象角色。"
methods:
  - "三角换元"
  - "倒代换"
  - "根式化简"
  - "回代"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001"

  - "MATHWIKI-ERROR-CLUSTER-016"

  - "MATHWIKI-KNOWLEDGE-020"

  - "MATHWIKI-KNOWLEDGE-041"

  - "MATHWIKI-KNOWLEDGE-058"

  - "MATHWIKI-KNOWLEDGE-080"

  - "MATHWIKI-KNOWLEDGE-120"

  - "MATHWIKI-METHOD-CLUSTER-028"

  - "MATHWIKI-METHOD-CLUSTER-109"

  - "MATHWIKI-METHOD-CLUSTER-1137"

  - "MATHWIKI-METHOD-CLUSTER-837"

  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-043_根式积分换元与回代链"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-08-27
formal_projection_sha256: 3327ed52115b61f92469be515f4f3a3b39487914211c63413ebce52f869bc85c
---

# GS-269 强化例题9.3（1）

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-269_强化例题9.3（1）.md`
- wrongnet ID：`GS-269`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 不定积分 |
| 题型 | 根式积分三角换元 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 不定积分
- 根式积分
- 三角换元
- 第二类换元
- 回代化简

### 错因

- 表达：最后回代时丢失倒数结构。
- 检查：主体方法正确后未核对外层对象角色。

### 方法

- 三角换元
- 倒代换
- 根式化简
- 回代

### 陷阱

- x 不等于 0
- dx 同步替换
- 三角函数回代
- 绝对值符号判断

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先判断根式形式并试令 x=tan t 或 x=1/u，同时写出 dx 的替换 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是只处理根式或 x^{-2}，没有同步替换 dx 并完整回代 |
| related_method_card_id | H09-003 |
| next_reminder | 看到根式和 x^{-2} 同时出现，先选三角换元或倒代换，再同步换 dx 并回代。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-KNOWLEDGE-058_根式积分]]
- [[MATHWIKI-KNOWLEDGE-080_三角换元]]
- [[MATHWIKI-KNOWLEDGE-120_回代化简]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-109_倒代换]]
- [[MATHWIKI-METHOD-CLUSTER-1137_根式化简]]
- [[MATHWIKI-METHOD-CLUSTER-837_回代]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-043_根式积分换元与回代链]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-575
- GS-587
- GS-619

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
