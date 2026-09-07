---
wiki_id: MATHWIKI-QUESTIONS-001
type: question_queue
title: 待调查问题与素材队列
subject: 数学一
source_refs:
  - 错题知识网络/wiki/index.md
  - 错题知识网络/wiki/log.md
wiki_refs:
  - MATHWIKI-OVERVIEW-001
  - MATHWIKI-SYNTHESIS-001
  - MATHWIKI-QUESTIONS-002
status: active
last_updated: 2026-07-01
---

# 待调查问题与素材队列

## 定位

本页记录 LLM Wiki 后续要继续编译的问题和来源。它不是正式错题卡候选池；只有满足 wrongnet 入库条件并经用户确认的内容，才进入正式错题卡流程。

## 待编译来源

| 优先级 | 来源 | 当前状态 | 下一步 |
|---|---|---|---|
| 高 | GS-633 到 GS-637 一元积分近期错题簇 | 已有专题页；已拆出换元、整体奇偶、分段点、结构中心、整体变量链和局部/整体错因页 | 继续补根式/三角换元后续动作链，例如 GS-618、GS-619、GS-620 |
| 高 | [[MATHWIKI-QUESTIONS-002_可视化错题候选决策队列]] | 已整理 136 个 `needs_card_decision` 可视化候选页，并按题图哈希一致、标题/定位一致、未匹配正式卡分层 | 优先处理有解析图且能高置信并入旧卡的候选；没有明确错点时不新建正式卡 |
| 高 | `错题知识网络/方法论库/method_card_registry.md` | 已登记 source summary | 匹配 wiki 方法页的 `method_card_ids` |
| 中 | `高数讲义/` | 未处理 | 按已学章节逐份生成 source summary |
| 中 | `线代讲义/` | 未处理 | 等线代复习进入当前主线后再编译 |
| 中 | `概率论讲义/` | 未处理 | 等概率论复习进入当前主线后再编译 |
| 中 | ChatGPT/Codex 数学讨论 | 零散 | 只沉淀高价值方法和错因模式 |

## 待调查问题

| 问题 | 需要证据 | 输出形态 |
|---|---|---|
| 一元积分近期错题中，GS-636 应归到“整体换元”“幂三角结构”还是“边界检查”？ | GS-636 的轻量字段、方法论库 | 已沉淀到 [[MATHWIKI-GS-METHOD-005_凑微分后的整体变量链]] 和 [[MATHWIKI-GS-TRIGGER-003_整体平方差先设整体]] |
| 条件边界专题下是否应拆出“端点归属”独立概念页？ | GS-635、知识树、讲义对应页 | concept page |
| 方法论库中哪些方法卡最适合链接到条件边界专题？ | `method_card_registry.md`、方法卡库 | 更新方法页 |
| 线代和概率论是否已有可做首批专题的错题簇？ | wrongnet 轻量索引、错题卡 frontmatter | topic candidate |

## 不进入本页的内容

- 完整题干。
- 完整长解析。
- 未经确认的用户掌握度。
- 可以直接正式入库但用户尚未授权的错题正文。

## 关联

- 导航：[[MATHWIKI-MAP-001_Obsidian导航图]]
- 综合：[[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]
