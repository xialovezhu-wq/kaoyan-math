---
wiki_id: MATHWIKI-QUESTIONS-007
title: 候选正式化前置检查清单
type: question_formalization_preflight
status: active
created: 2026-07-05
updated: 2026-07-05
source_refs:
  - 错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-004_测试题候选台账.md
  - 错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-005_候选用户确认清单.md
  - 错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-006_候选确认第一批执行单.md
  - 错题知识网络/可视化错题详情/manifest.json
tags:
  - mathwiki/question-ledger
  - mathwiki/formalization-preflight
  - mathwiki/quality-scale
---

# MATHWIKI-QUESTIONS-007 候选正式化前置检查清单

本页承接 [[错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-006_候选确认第一批执行单|MATHWIKI-QUESTIONS-006]]。它不是正式错题卡，也不代表候选已经可以入库；作用是把第一批候选在“用户确认之后、正式改卡之前”必须做的检查固定下来。

核心边界：

- 没有用户本人第一卡点，不写 `wrong_point`。
- 没有迁移授权，不改变 `LA-004`、`GS-079`、`GS-152` 等历史编号归属。
- 没有正确解析或可靠题图身份，不运行正式入库。
- 未修改 `错题知识网络/错题卡/*.md` 时，不运行 `wrongnet.py rebuild`。

## 第一批前置检查表

| 候选组 | 当前身份 | 可进入正式化的最小用户回复 | 用户确认后的预检动作 | 确认前禁止动作 | 当前状态 |
| --- | --- | --- | --- | --- | --- |
| `CAND-0014` / `CAND-0015` | `LA-004` 历史编号异常；内容为高数隐函数方程组求导。 | “允许迁移为新的 GS 正式卡；我的第一卡点是……” 或 “不迁移，继续保留 LA-004 异常入口”。 | 先查 `LA-004`、`强化例题13.17`、`MN4-GS-CH01-514`；再跑 `intake_preflight.py --source 强化例题13.17 --knowledge 隐函数求导 --suggest`；若迁移，先写编号保留方案，再改正式卡和视觉入口。 | 不擅自把 `LA-004` 改成 GS；不改回滚 JSON；不把题图内容反推为个人错因。 | waiting_user |
| `CAND-0012` / `CAND-0013` | 两个视觉入口同源，实际不是原 `GS-079` / `GS-152`。 | “以 `CAND-0012` 为主入口；这是我的错题；第一卡点是……” 或 “只保留为重复视觉证据”。 | 先查 `1000题A组11.5`、`GS-079`、`GS-152`；再跑 `intake_preflight.py --source 1000题A组11.5 --knowledge 中值定理 --suggest`，必要时补查 `变限积分`。 | 不回写原 `GS-079` / `GS-152`；不把重复视觉入口拆成两张正式卡。 | waiting_user |
| `CAND-0003` | 2024 年 19 题，定积分应用/旋转体体积候选。 | “这是我的错题；第一卡点是没先建立 `V(t)` / 变限积分求导链断 / 其他……” | 先查 `2024年19题`、`旋转体体积`、`定积分应用`；再跑 `intake_preflight.py --source 2024年19题 --knowledge 旋转体体积 --suggest`。 | 不仅凭题图建卡；不预设错因是建模还是求导链断。 | waiting_user |
| `CAND-0001` | 58049 数列极限平方差裂项候选；不能按数字 ID 硬合并 `GS-069`。 | “这是我的错题；第一卡点是没识别平方差裂项 / 望远镜链断 / 其他……” | 先查 `58049`、`数列极限`、`平方差裂项`；再跑 `intake_preflight.py --source 58049 --knowledge 数列极限 --suggest`。 | 不硬合并 `GS-069`；不替用户选择裂项或望远镜断点。 | waiting_user |
| `CAND-0011` | 57718 不动点/压缩映射题；当前折叠解析串到 170684。 | “我能提供正确解析/本人卡点……” 或 “只保留为方法相似候选”。 | 先核对 `57718` 正确解析是否存在；再查 `固定点方程`、`数列极限`、`GS-058`；解析对应后才跑 preflight。 | 不并入 `GS-444` 或 `GS-058`；不使用 170684 解析补 57718 错因。 | waiting_user |

## 用户回复后执行顺序

1. 先更新本页对应候选的 `当前状态`，只写用户确认过的信息。
2. 运行查重预检，至少包含原始题号、视觉入口 ID、候选知识点三类检索。
3. 读命中的旧正式卡，判断是新建、更新、合并、还是继续候选。
4. 只有确认为正式卡修改时，才编辑 `错题知识网络/错题卡/*.md`。
5. 改正式卡后必须运行 `wrongnet.py rebuild` 或 `intake_closeout.py`，并补齐 wiki 覆盖、Obsidian 搜索和质量门。

## 不足信息清单

| 候选组 | 缺失字段 | 备注 |
| --- | --- | --- |
| `CAND-0014` / `CAND-0015` | 迁移授权；本人第一卡点；GS 新编号策略 | 这是历史编号异常，优先级最高。 |
| `CAND-0012` / `CAND-0013` | 主入口确认；是否本人错题；本人第一卡点 | 当前只确认视觉错连和同源重复。 |
| `CAND-0003` | 是否做错；入口断点 | 方法价值高，但不能代替用户确认。 |
| `CAND-0001` | 是否做错；裂项/望远镜具体断点 | 与 `GS-069` 数字接近但身份不同。 |
| `CAND-0011` | 正确解析；本人卡点；是否新建 GS 卡 | 解析串题风险未解除。 |

## 本页边界

- 本页只推进 N5 的操作化，不减少候选数量本身。
- 本页不改变 candidate/confirmed/formal 状态机。
- 本页不进入 Tutor 安全输入包；Tutor 只在正式卡或稳定高层模式形成后再判断是否需要更新。
- 本页不登记回滚复习，不写掌握度，不写复做日期。
