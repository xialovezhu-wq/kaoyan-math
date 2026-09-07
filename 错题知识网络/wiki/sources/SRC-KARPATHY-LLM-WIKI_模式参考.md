---
wiki_id: SRC-SUMMARY-KARPATHY-LLM-WIKI
type: source_summary
title: Karpathy LLM Wiki 模式参考
subject: 数学一
source_role: external_schema_reference
source_refs:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
wiki_refs:
  - MATHWIKI-HOME
  - MATHWIKI-OVERVIEW-001
  - MATHWIKI-MAINT-001
status: active
last_updated: 2026-06-28
---

# Karpathy LLM Wiki 模式参考

## 来源定位

这是数学一 LLM Wiki 的外部模式来源。它不替代本地 wrongnet 规则，只规定 wiki 应该如何持续编译知识。

## 对数学系统的启发

- 不把 AI 当成一次性问答工具，而是让 AI 持续维护一个 Markdown wiki。
- raw sources 只读，wiki 是 AI 编译后的长期知识层。
- `index.md` 管内容目录，`log.md` 管操作时间线。
- ingest 不只是摘要来源，还要更新相关概念、方法、专题和综合页。
- query 的高价值答案应回写成 wiki 页面，而不是留在聊天记录里。
- lint 是长期维护动作，用来发现孤立页、矛盾、过期结论、断链和未处理来源。

## 本地落地

- 入口：[[00-数学一 LLM Wiki]]
- 总览：[[MATHWIKI-OVERVIEW-001_数学错题知识库总览]]
- 维护规则：[[MATHWIKI-MAINT-001_维护节奏与完成标准]]
- 待处理队列：[[MATHWIKI-QUESTIONS-001_待调查问题与素材队列]]

## 边界

本页只保存模式摘要，不复制原文长段落。具体数学写入边界以 `错题知识网络/schema/karpathy_llm_wiki.md`、`ingest.md`、`query.md`、`lint.md` 为准。
