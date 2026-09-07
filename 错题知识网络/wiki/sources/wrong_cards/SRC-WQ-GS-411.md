---
wiki_id: SRC-WQ-GS-411
type: source_summary
title: "GS-411 2020年第19题"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-411_2020年第19题.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-411_2020年第19题.md"
visual_ids:
  - "VIS-GS-411"
wrongnet_refs:
  - "GS-411"
knowledge:
  - "二重积分"
  - "二重积分极坐标法"
error_causes:
  - "历史错因未记录"
methods:
  - "积分区域描述"
  - "齐次换元 y=xt"
  - "二重积分极坐标法"
evidence_origin: pending_user_confirmation
evidence_note: "题图与解析图已核对；旧正式正文属于另一道题，旧个人错因不迁移，当前方法断点待复做确认。"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-152_历史错因未记录"
  - "MATHWIKI-KNOWLEDGE-049_二重积分"
  - "MATHWIKI-KNOWLEDGE-070_二重积分极坐标法"
  - "MATHWIKI-METHOD-CLUSTER-1257_积分区域描述"
  - "MATHWIKI-METHOD-CLUSTER-047_二重积分极坐标法"
  - "MATHWIKI-GS-METHOD-037_二重积分极坐标区域分块与对称化"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
formal_projection_sha256: 7b0521219f35754260c01f5fa2ae363a31713816563f0a8f6b8befecf4f5b41d
last_updated: 2026-07-23
---

# GS-411 2020年第19题

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-411_2020年第19题.md`
- wrongnet ID：`GS-411`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-411_2020年第19题|VIS-GS-411]]
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-411/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-411/solution_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 二重积分 |
| 题型 | 二重积分齐次换元与极坐标计算 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 题面摘要与答案

- 题面：区域由 \(x=1,x=2,y=x\) 与 \(x\) 轴围成，求 \(\iint_D\frac{\sqrt{x^2+y^2}}{x}\,dx\,dy\)。
- 答案：\(\frac34\left[\sqrt2+\ln(\sqrt2+1)\right]\)。
- 证据边界：题图与解析图已核对；旧正文属于另一道题，个人错因不能迁移，当前方法断点为 `pending_user_confirmation`。

## 可编译信息

### 知识点

- 二重积分
- 二重积分极坐标法

### 错因

- 历史错因未记录

### 方法

- 积分区域描述
- 齐次换元 \(y=xt\)
- 二重积分极坐标法

### 陷阱

- 直线 \(x=c\) 在极坐标下对应 \(r=c\sec\theta\)
- 齐次换元 \(y=xt\) 时必须同步写 \(dy=x\,dt\)
- 极坐标换元不能漏面积微元中的 \(r\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| evidence_origin | pending_user_confirmation |
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 \(1\le x\le2,0\le y\le x\)，并检查被积函数可化为 \(\sqrt{1+(y/x)^2}\) |
| missed_action | 旧卡正文绑定了另一道题；个人是否漏掉齐次换元或极坐标入口仍待复做确认 |
| related_method_card_id | H14-005 |
| next_reminder | 看到楔形区域且被积函数含 \(y/x\)，先写区域，再比较齐次换元与极坐标路线。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-152_历史错因未记录]]
- [[MATHWIKI-KNOWLEDGE-049_二重积分]]
- [[MATHWIKI-KNOWLEDGE-070_二重积分极坐标法]]
- [[MATHWIKI-METHOD-CLUSTER-1257_积分区域描述]]
- [[MATHWIKI-METHOD-CLUSTER-047_二重积分极坐标法]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-037_二重积分极坐标区域分块与对称化]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-404

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
