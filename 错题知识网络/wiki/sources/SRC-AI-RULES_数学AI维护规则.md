---
wiki_id: SRC-SUMMARY-AI-RULES
type: source_summary
title: 数学 AI 维护规则
subject: 数学一
source_role: local_rule
source_refs:
  - 错题知识网络/AI维护规则.md
wiki_refs:
  - MATHWIKI-HOME
  - MATHWIKI-MAINT-001
status: active
last_updated: 2026-06-28
---

# 数学 AI 维护规则

## 来源定位

`错题知识网络/AI维护规则.md` 是数学错题系统的核心维护规则。它规定 wrongnet 入库、method_gap、相似题召回、知识树挂载、回滚系统衔接和 LLM Wiki 兼容层。

## 对 wiki 的约束

- 知识点是错题网络主轴，wiki 页不能绕开知识点体系。
- 用户没明确给错因时，不编造 `wrong_point` 或 `error_causes`。
- `method_gap` 必须保留“题面触发信息、第一动作、漏掉动作、下次提醒”的动作断点含义。
- `错题知识网络/生成/` 是派生目录，不作为 wiki 源数据手改。
- 修改正式错题卡后才运行 `wrongnet.py rebuild`。

## 与 LLM Wiki 的关系

本规则决定了 wiki 的边界：wiki 可以沉淀概念、方法、专题、错因模式和触发条件，但不能替代一题一卡的正式错题源数据。

## 关联

- 入口页：[[00-数学一 LLM Wiki]]
- 维护页：[[MATHWIKI-MAINT-001_维护节奏与完成标准]]
- 正式源摘要：[[SRC-WRONGNET_正式错题卡源数据]]
