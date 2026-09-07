---
wiki_id: MATHWIKI-REVIEW-013
type: target_level_semantic_closeout
title: 全库逐题语义复核第3批正式收口
subject: 数学一
source_refs:
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-012_全库逐题语义复核第3批20题.json
  - 错题知识网络/wiki/review/MATHWIKI-REVIEW-013_全库逐题语义复核第3批正式收口.json
status: active
last_updated: 2026-07-22
---

# 全库逐题语义复核第3批正式收口

## 收口结果

第 3 批 20 题已经完成正式源写入、一次 wrongnet 派生重建、证据图重建与全库验证。共改写或修正 29 份正式卡、14 份视觉详情、4 份视觉登记和 1 份语义边界回执；未新增任何个人事实，未合并或删除稳定 ID。

关系层面移除 26 条逻辑边和 35 个物理声明，新增 4 条强边，并复核保留 9 条既有强边。

## 新增强边

- GS-702—GS-172；声明 owner：GS-702。
- GS-703—GS-585；声明 owner：GS-703。
- GS-716—GS-458；声明 owner：GS-716。
- LA-039—LA-041；声明 owner：LA-039。

## 复核保留的既有强边

- GS-627—GS-629；声明 owner：GS-627、GS-629。
- GS-698—GS-700；声明 owner：GS-698、GS-700。
- GS-700—GS-667；声明 owner：GS-700、GS-667。
- GS-704—GS-712；声明 owner：GS-712。
- GS-718—GS-719；声明 owner：GS-718。
- LA-099—LA-075；声明 owner：LA-075。
- LA-099—LA-100；声明 owner：LA-100。
- GS-647—GS-646；声明 owner：GS-647。
- GS-651—GS-647；声明 owner：GS-651。

## 删除关系

| 端点 A | 端点 B | 删除声明 owner |
|---|---|---|
| GS-627 | GS-628 | GS-627、GS-628 |
| GS-627 | GS-645 | GS-627、GS-645 |
| GS-627 | GS-647 | GS-647 |
| GS-627 | GS-651 | GS-651 |
| GS-629 | GS-645 | GS-629、GS-645 |
| GS-629 | GS-647 | GS-647 |
| GS-645 | GS-651 | GS-645、GS-651 |
| GS-698 | GS-699 | GS-698、GS-699 |
| GS-249 | GS-225 | GS-249 |
| GS-249 | GS-041 | GS-249 |
| GS-249 | GS-081 | GS-249 |
| GS-249 | GS-226 | GS-249 |
| GS-249 | GS-229 | GS-229 |
| LA-039 | LA-090 | LA-039 |
| LA-039 | LA-094 | LA-094 |
| LA-039 | LA-033 | LA-033 |
| LA-099 | LA-090 | LA-099、LA-090 |
| LA-099 | LA-097 | LA-097 |
| LA-099 | LA-093 | LA-093 |
| LA-099 | LA-092 | LA-092 |
| LA-099 | LA-098 | LA-098 |
| LA-081 | LA-078 | LA-081、LA-078 |
| LA-081 | LA-079 | LA-081、LA-079 |
| LA-081 | LA-086 | LA-081、LA-086 |
| LA-081 | LA-033 | LA-033 |
| LA-081 | LA-064 | LA-064 |

## 题源与身份边界

- GS-249：正式内容已按实际题图修正，但与 GS-044、GS-325、GS-343 共享题图；稳定 ID 仍不自动合并或删除。
- GS-704：来源缺少函数关系原变量的定义域；当前答案只保留为补充分支后的条件式结论。
- LA-081：来源缺少 Aα≠0 或等价条件；当前不能把 D 标成无条件正确。
- LA-039 与 LA-099：旧正式内容的视觉身份错位已修正，并分别完成矩阵回验与候选参数回代。

## 视觉登记

- 新增 VIS-GS-713、VIS-GS-714、VIS-GS-715、VIS-GS-716、VIS-GS-717、VIS-GS-719。
- manifest 现有 978 条记录；asset_to_obsidian 现有 1402 条映射。
- 每个新增题图和解析图均记录真实 SHA-256；四份登记的计数、路径和映射保持一致。

## 验证状态

- wrongnet 按约束只重建 1 次，9 份生成投影均记录前后 SHA-256。
- 知识点—错因—证据图的 source state 为 `fb47b13f36b1383f690aef9616c8886061f9ea984b1fa2466df31ff4a222ba3e`，build 与 check 均通过。
- 定向回归 18 / 18、全量测试 197 / 197 通过；JSON、831 份 YAML frontmatter、双向关系、视觉登记、Obsidian read / outline / search、生成文件哈希与 `git diff --check` 均通过。
- 机器可核对细节以同名 JSON 回执中的 `validation`、`wrongnet_rebuild` 和 `derived_evidence_graph` 为准。正式卡、视觉详情与登记文件的前后 SHA-256 也完整保存在该回执中。

## 活动进度

累计已完成 60 / 831 张，剩余 771 张；累计覆盖 158 个物理图片路径。
