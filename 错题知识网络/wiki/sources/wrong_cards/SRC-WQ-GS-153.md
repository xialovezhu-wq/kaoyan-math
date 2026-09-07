---
wiki_id: SRC-WQ-GS-153
type: source_summary
title: "GS-153 1000题B组5.34"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-153_1000题B组5.34.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-153"
knowledge:
  - "一元函数微分学应用"
  - "单调性与极值"
  - "参数分类讨论"
  - "无穷远极限"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是没有先求导并按 n 的奇偶与端点无穷远极限完成全局最值分类，需用户复做确认。"
methods:
  - "导数判单调"
  - "奇偶分类讨论"
  - "符号表"
  - "无穷远极限兜底"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-336_旧批量未记录个人原始错因-当前仅确认复做断点是没有先求导并按n的奇偶与端"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-047_参数分类讨论"
  - "MATHWIKI-KNOWLEDGE-093_无穷远极限"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-1069_无穷远极限兜底"
  - "MATHWIKI-METHOD-CLUSTER-448_符号表"
  - "MATHWIKI-METHOD-CLUSTER-875_奇偶分类讨论"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-153 1000题B组5.34

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-153_1000题B组5.34.md`
- wrongnet ID：`GS-153`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 幂乘指数函数单调性与最值分类讨论 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 单调性与极值
- 参数分类讨论
- 无穷远极限

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是没有先求导并按 n 的奇偶与端点无穷远极限完成全局最值分类，需用户复做确认。

### 方法

- 导数判单调
- 奇偶分类讨论
- 符号表
- 无穷远极限兜底

### 陷阱

- 驻点不一定是极值点
- 奇偶决定 $x^{n-1}$ 符号
- 全局最值要看两端极限

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先求导并写出 f'(x)=x^{n-1}e^{-x}(n-x) |
| missed_action | 旧批量未记录个人第一错步；当前只确认复做时不能跳过求导符号表和奇偶分类 |
| related_method_card_id | H05-006 |
| next_reminder | 看到含参幂乘指数函数最值，先求导写符号主线，再按奇偶和两端极限收尾。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-336_旧批量未记录个人原始错因-当前仅确认复做断点是没有先求导并按n的奇偶与端]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-047_参数分类讨论]]
- [[MATHWIKI-KNOWLEDGE-093_无穷远极限]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-1069_无穷远极限兜底]]
- [[MATHWIKI-METHOD-CLUSTER-448_符号表]]
- [[MATHWIKI-METHOD-CLUSTER-875_奇偶分类讨论]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
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
