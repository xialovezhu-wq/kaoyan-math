---
wiki_id: SRC-WQ-GS-240
type: source_summary
title: "GS-240 1000题B组6.1"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-240_1000题B组6.1.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-240"
knowledge:
  - "一元函数微分学应用"
  - "单调性与极值"
  - "零点定理"
  - "参数范围"
error_causes:
  - "表达：抄题时将常数 3/2 写成 2/3。"
  - "方法触发：未主动用偶函数对称性把四个不同零点化为正半轴两个不同零点。"
  - "条件：使用驻点表达式前未显式检查 k>0。"
  - "计算：不等式乘以负数时未改变方向，最终范围方向相反。"
methods:
  - "偶函数化简"
  - "导数判极值"
  - "端点极限"
  - "参数分类讨论"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003"
  - "MATHWIKI-ERROR-CLUSTER-347"
  - "MATHWIKI-KNOWLEDGE-001"
  - "MATHWIKI-KNOWLEDGE-011"
  - "MATHWIKI-KNOWLEDGE-042"
  - "MATHWIKI-KNOWLEDGE-100"
  - "MATHWIKI-METHOD-CLUSTER-040"
  - "MATHWIKI-METHOD-CLUSTER-081"
  - "MATHWIKI-METHOD-CLUSTER-252"
  - "MATHWIKI-METHOD-CLUSTER-609"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
formal_projection_sha256: d6a64059f910ee176b3f50f5772fa4adbc77ee03880e99503b3f2470784c087b
last_updated: 2026-08-27
---

# GS-240 1000题B组6.1

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-240_1000题B组6.1.md`
- wrongnet ID：`GS-240`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 偶函数零点个数参数范围 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 单调性与极值
- 零点定理
- 参数范围

### 错因

- 表达：抄题时将常数 3/2 写成 2/3。
- 方法触发：未主动用偶函数对称性把四个不同零点化为正半轴两个不同零点。
- 条件：使用驻点表达式前未显式检查 k>0。
- 计算：不等式乘以负数时未改变方向，最终范围方向相反。

### 方法

- 偶函数化简
- 导数判极值
- 端点极限
- 参数分类讨论

### 陷阱

- 四根转正半轴两根
- k必须为正
- 极大值严格大于0
- 先核对题面常数 3/2，不要抄成 2/3
- 不等式乘负数必须反向
- 极大值等于 0 只产生相切根，不满足四个不同零点

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先利用偶函数性，把四个零点化为 \(x>0\) 上两个零点。 |
| missed_action | 本次未主动建立四根与正半轴两根的对应；该方法方向由提示补齐。 |
| related_method_card_id | H06-010 |
| next_reminder | 看到偶函数四个零点，先转成正半轴两个零点，再找唯一极大值。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-347_旧批量未记录个人原始错因-当前可确认的复做断点是没有先利用偶函数性把“四]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-042_零点定理]]
- [[MATHWIKI-KNOWLEDGE-100_参数范围]]
- [[MATHWIKI-METHOD-CLUSTER-040_参数分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-081_导数判极值]]
- [[MATHWIKI-METHOD-CLUSTER-252_端点极限]]
- [[MATHWIKI-METHOD-CLUSTER-609_偶函数化简]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-239
- GS-255
- GS-513
- GS-241
- GS-244

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
