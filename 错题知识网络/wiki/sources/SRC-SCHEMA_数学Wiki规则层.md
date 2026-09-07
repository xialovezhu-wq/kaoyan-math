---
wiki_id: SRC-SUMMARY-SCHEMA
type: source_summary
title: 数学 Wiki Schema 规则层
subject: 数学一
source_role: local_schema
source_refs:
  - 错题知识网络/schema/README.md
  - 错题知识网络/schema/ingest.md
  - 错题知识网络/schema/query.md
  - 错题知识网络/schema/lint.md
  - 错题知识网络/schema/decision_matrix.md
  - 错题知识网络/schema/karpathy_llm_wiki.md
wiki_refs:
  - MATHWIKI-HOME
  - MATHWIKI-MAINT-001
status: active
last_updated: 2026-06-28
---

# 数学 Wiki Schema 规则层

## 来源定位

`错题知识网络/schema/` 是 AI 操作规则层。它告诉 Codex 什么时候只写 wiki，什么时候进入正式错题卡，什么时候运行 wrongnet，什么时候只做 lint 报告。

## 当前规则文件

- `README.md`：schema 总说明。
- `karpathy_llm_wiki.md`：Karpathy 模式在数学系统中的落地规则。
- `decision_matrix.md`：wiki-only、candidate-card、formal-card、rollback-unit、rebuild-required 的决策矩阵。
- `ingest.md`：导入来源资料。
- `query.md`：基于 wiki 回答和沉淀。
- `lint.md`：体检 wiki 和边界风险。
- `page_template.md`：页面 frontmatter 和正文模板。

## 使用规则

每次操作先按任务类型读对应 schema，再读 `wiki/index.md` 和 `wiki/log.md`。如果 schema 与正式 wrongnet 规则冲突，以 `AI维护规则.md` 和错题系统正式规则为准。

## 关联

- 模式参考：[[SRC-KARPATHY-LLM-WIKI_模式参考]]
- 维护标准：[[MATHWIKI-MAINT-001_维护节奏与完成标准]]
