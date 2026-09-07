---
wiki_id: SRC-RAW-SOURCES-MAP
type: source_map
title: 原始资料映射
subject: 数学一
source_role: raw_source_map
source_refs:
  - README.md
  - 错题知识网络/AI维护规则.md
  - 错题知识网络/wiki/index.md
wiki_refs:
  - MATHWIKI-HOME
  - MATHWIKI-OVERVIEW-001
  - SRC-WRONGNET
  - SRC-WRONGCARDS-INDEX
status: active
last_updated: 2026-07-05
---

# 原始资料映射

本页把 Karpathy LLM Wiki 的 raw sources 层落到数学项目里。raw sources 是证据层，不由 AI 修改；wiki 只在这里记录路径、处理状态和可追踪链接。

## 已确认 raw sources

| source | 角色 | 写入边界 | 已连接 wiki |
|---|---|---|---|
| `错题知识网络/错题卡/*.md` | formal wrong card source | 只有正式错题入库任务才可修改 | [[SRC-WRONGNET_正式错题卡源数据]]；[[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]] |
| `错题知识网络/知识树/*.md` | 讲次知识树种子 | 保留原位，不迁移 | [[SRC-KTREE-H16_无穷级数知识树]]；[[SRC-KTREE-H17_多元函数积分学预备知识树]]；[[SRC-H18-MULTI-INTEGRAL_高数第18讲多元函数积分学预处理包]] |
| `错题知识网络/方法论库/` | 方法卡与 method_gap 权威来源 | 保留原位，不由 wiki 改 ID | [[SRC-METHOD-LIB_方法论库]] |
| `高数讲义/` | 高数讲义 PDF | 只读，按讲次选择性 ingest | [[SRC-H18-MULTI-INTEGRAL_高数第18讲多元函数积分学预处理包]] |
| `线代讲义/` | 线代讲义 PDF | 只读，按讲次选择性 ingest | 待处理 |
| `概率论讲义/` | 概率论讲义 PDF | 只读，按讲次选择性 ingest | 待处理 |
| `kaoyan_math_project_v2/` | 历史 AI 项目资料 | 只读，不能替代正式错题卡 | [[SRC-METHOD-LIB_方法论库]] |
| `错题知识网络/批量导入/原始文件/` | 批量导入原始文件 | 只读，是否建卡需单独判断 | 待处理 |

## 编译规则

1. 讲义、讨论、NotebookLM 导出和视频笔记默认进入 wiki，不直接建正式错题卡。
2. 只有出现具体题目、用户错点、知识点和复做价值时，才进入正式错题卡判断。
3. 只修改 wiki 时，不运行 `wrongnet.py rebuild`。
4. 修改 `错题知识网络/错题卡/*.md` 后，才运行 `python3 错题知识网络/scripts/wrongnet.py rebuild`。

## 入口

- [[00-数学一 LLM Wiki]]
- [[MATHWIKI-OVERVIEW-001_数学错题知识库总览]]
- [[MATHWIKI-COVERAGE-001_错题卡全量覆盖索引]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
