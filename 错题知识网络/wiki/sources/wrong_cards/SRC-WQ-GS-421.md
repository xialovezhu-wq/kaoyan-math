---
wiki_id: SRC-WQ-GS-421
type: source_summary
title: "GS-421 强化例题12.5"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-421_强化例题12.5.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-421_强化例题12.5.md"
visual_ids:
  - "VIS-GS-421"
wrongnet_refs:
  - "GS-421"
knowledge:
  - "定积分"
  - "定积分应用"
  - "万有引力微元"
  - "向量分量投影"
error_causes:
  - "历史错因未记录"
methods:
  - "物理语言转定积分"
  - "微元法建模"
  - "万有引力微元"
  - "力的投影"
evidence_origin: pending_user_confirmation
evidence_note: "题图与两张解析图已核对；旧正式正文复制自另一道做功题，旧个人错因不迁移，当前方法断点待复做确认。"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-152_历史错因未记录"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-035_定积分应用"
  - "MATHWIKI-METHOD-CLUSTER-050_物理语言转定积分"
  - "MATHWIKI-METHOD-CLUSTER-058_微元法建模"
  - "MATHWIKI-METHOD-CLUSTER-322_力的投影"
  - "MATHWIKI-GS-METHOD-038_定积分物理应用微元法"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
formal_projection_sha256: 48da2fb6c74daffe04367a0aa0e3e6e305db132cd4f0ec872841759692cb9b4e
last_updated: 2026-07-24
---

# GS-421 强化例题12.5

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-421_强化例题12.5.md`
- wrongnet ID：`GS-421`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-421_强化例题12.5|VIS-GS-421]]
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-421/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-421/solution_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-421/solution_02.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分应用 |
| 题型 | 定积分物理应用：细杆引力分量 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 题面摘要与答案

- 题面：沿 \(y\) 轴区间 \([0,1]\) 放置线密度为 \(\rho\) 的均匀细杆，在 \((1,0)\) 处有单位质点，求细杆引力沿 \(x\) 轴正向的分量。
- 答案：\(-G\rho/\sqrt2\)。
- 证据边界：题图与两张解析图已核对；旧正文复制自另一道做功题，个人错因不能迁移，当前方法断点为 `pending_user_confirmation`。

## 可编译信息

### 知识点

- 定积分
- 定积分应用
- 万有引力微元
- 向量分量投影

### 错因

- 历史错因未记录

### 方法

- 物理语言转定积分
- 微元法建模
- 万有引力微元
- 力的投影

### 陷阱

- 单位质点固定不发生位移，本题求力而不是功
- 细杆对 \((1,0)\) 处质点的引力沿 \(x\) 轴分量为负
- 引力大小与方向余弦要分别写清

## method_gap 摘要

| 字段 | 值 |
|---|---|
| evidence_origin | pending_user_confirmation |
| action_gap_type | B5-CHECK |
| expected_first_action | 先在 \((0,y)\) 取微元 \(\rho\,dy\)，画出质点所受引力方向，确认 \(x\) 分量为负 |
| missed_action | 旧卡正文绑定了另一道做功题；个人是否漏掉方向投影或负号仍待复做确认 |
| related_method_card_id | H12-005 |
| next_reminder | 连续质量分布求某方向引力时，先取质量微元、写方向向量并判分量正负，再积分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-152_历史错因未记录]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-035_定积分应用]]
- [[MATHWIKI-METHOD-CLUSTER-050_物理语言转定积分]]
- [[MATHWIKI-METHOD-CLUSTER-058_微元法建模]]
- [[MATHWIKI-METHOD-CLUSTER-322_力的投影]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-038_定积分物理应用微元法]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 当前无已确认的 strong related 边。

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
