---
wiki_id: MATHWIKI-LINT-001
title: 剩余质量门 warning 证据边界台账
type: lint_boundary_ledger
subject: 数学一
knowledge:
  - LLM Wiki Lint
  - 质量门
  - 证据边界
  - 可视化缺口
  - method_gap
wrongnet_refs:
  - GS-408
  - GS-414
  - LA-005
source_refs:
  - /tmp/kaoyan_math_m141_pre_scan.json
  - /tmp/kaoyan_math_m141_post_scan.json
  - 错题知识网络/wiki/maintenance/MATHWIKI-MAINT-140_候选用户确认清单与Obsidian可检索性复核报告_2026-07-05.md
  - 错题知识网络/wiki/maintenance/MATHWIKI-MAINT-138_已掌握卡review_next规范化与质量门复核报告_2026-07-05.md
  - 错题知识网络/可视化错题详情/manifest.json
  - 错题知识网络/可视化错题详情/index.md
status: active
created: 2026-07-05
updated: 2026-07-05
tags:
  - mathwiki/lint
  - mathwiki/quality-gate
  - mathwiki/evidence-boundary
---

# MATHWIKI-LINT-001 剩余质量门 warning 证据边界台账

## 定位

本页不是免检白名单，也不是把 warning 视为通过。本页用于解释 M141 巡检后剩余 70 个 warning 为什么不能继续用机械填字段的方式下降：这些项目要么已经登记为可视化缺图缺口，要么缺用户本人第一卡点和作答过程，要么是旧批量导入的总纲/重复/错连边界。

后续一旦获得题图、OCR、正确解析或用户本人错因，本页中的条目应按正常正式卡流程更新，而不是长期停留在台账里。

## 当前扫描口径

- 扫描时间：2026-07-05
- 扫描结果：`checked=777`，`error_cards=0`，`error_items=0`，`warn_cards=42`，`warn_items=70`
- 扫描快照：`/tmp/kaoyan_math_m141_pre_scan.json`、`/tmp/kaoyan_math_m141_post_scan.json`
- 口径修正：首次误把 `错题知识网络/错题卡/README.md` 当作正式卡，已排除；正式 ID 只取 `GS-*`、`LA-*`、`PR-*`、`MX-*`。

## Warning 分布

| warning | 数量 | 当前处理原则 |
|---|---:|---|
| `visual gap record has no asset mapping by design` | 41 | 已有 `VIS-GAP-*` 缺图登记；不能伪造题图、资产映射或 OCR。 |
| `method_gap not enabled` | 26 | 多数缺用户本人第一卡点或只是总纲/重复/错连边界；不能用解析倒推出个人错因。 |
| `methods is placeholder or empty` | 3 | 题图/OCR/题目身份不足，不能硬补方法标签。 |

## 41 个可视化缺口

这些卡的可视化层已在 `manifest.json` 中登记为 `visual_gap_registered` 或 `needs_ocr`，并在缺图详情页中标明“无题图，来源待确认；needs_ocr”。它们不是“没有处理”，而是当前没有可靠题图资产。

高等数学：

- [GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-048](http://127.0.0.1:8765/open/GS-048)、[GS-079](http://127.0.0.1:8765/open/GS-079)、[GS-152](http://127.0.0.1:8765/open/GS-152)、[GS-249](http://127.0.0.1:8765/open/GS-249)、[GS-341](http://127.0.0.1:8765/open/GS-341)、[GS-344](http://127.0.0.1:8765/open/GS-344)、[GS-349](http://127.0.0.1:8765/open/GS-349)、[GS-362](http://127.0.0.1:8765/open/GS-362)、[GS-369](http://127.0.0.1:8765/open/GS-369)、[GS-375](http://127.0.0.1:8765/open/GS-375)、[GS-405](http://127.0.0.1:8765/open/GS-405)、[GS-408](http://127.0.0.1:8765/open/GS-408)、[GS-414](http://127.0.0.1:8765/open/GS-414)、[GS-426](http://127.0.0.1:8765/open/GS-426)、[GS-427](http://127.0.0.1:8765/open/GS-427)、[GS-428](http://127.0.0.1:8765/open/GS-428)、[GS-429](http://127.0.0.1:8765/open/GS-429)、[GS-531](http://127.0.0.1:8765/open/GS-531)

线性代数：

- [LA-003](http://127.0.0.1:8765/open/LA-003)、[LA-005](http://127.0.0.1:8765/open/LA-005)、[LA-006](http://127.0.0.1:8765/open/LA-006)、[LA-024](http://127.0.0.1:8765/open/LA-024)、[LA-027](http://127.0.0.1:8765/open/LA-027)、[LA-029](http://127.0.0.1:8765/open/LA-029)、[LA-051](http://127.0.0.1:8765/open/LA-051)、[LA-065](http://127.0.0.1:8765/open/LA-065)、[LA-066](http://127.0.0.1:8765/open/LA-066)、[LA-076](http://127.0.0.1:8765/open/LA-076)、[LA-077](http://127.0.0.1:8765/open/LA-077)、[LA-080](http://127.0.0.1:8765/open/LA-080)、[LA-083](http://127.0.0.1:8765/open/LA-083)、[LA-084](http://127.0.0.1:8765/open/LA-084)、[LA-085](http://127.0.0.1:8765/open/LA-085)、[LA-086](http://127.0.0.1:8765/open/LA-086)、[LA-095](http://127.0.0.1:8765/open/LA-095)、[LA-096](http://127.0.0.1:8765/open/LA-096)、[LA-101](http://127.0.0.1:8765/open/LA-101)、[LA-102](http://127.0.0.1:8765/open/LA-102)、[LA-107](http://127.0.0.1:8765/open/LA-107)、[LA-108](http://127.0.0.1:8765/open/LA-108)

解除条件：

1. 找到原题图或解析图，补入可视化详情页和资产映射。
2. OCR 后能确认题目身份，不与旧卡错连。
3. 若同时要改正式错题卡，必须有用户错因或可复做的具体错点证据，并运行 rebuild。

## 26 个 method_gap 未启用

### 重复/占位卡

- [GS-280](http://127.0.0.1:8765/open/GS-280)：重复占位，正式错因已维护在 [GS-162](http://127.0.0.1:8765/open/GS-162)。
- [LA-003](http://127.0.0.1:8765/open/LA-003)：误归线代的重复占位，正式错因已维护在 [GS-256](http://127.0.0.1:8765/open/GS-256)。

处理原则：不为占位卡再建新的个人 method_gap；后续若用户要求清理，应走合并/弃用决策，而不是硬填。

### 总纲型旧批量卡

- [GS-349](http://127.0.0.1:8765/open/GS-349)、[LA-006](http://127.0.0.1:8765/open/LA-006)、[LA-024](http://127.0.0.1:8765/open/LA-024)、[LA-066](http://127.0.0.1:8765/open/LA-066)、[LA-076](http://127.0.0.1:8765/open/LA-076)、[LA-077](http://127.0.0.1:8765/open/LA-077)、[LA-107](http://127.0.0.1:8765/open/LA-107)、[LA-108](http://127.0.0.1:8765/open/LA-108)

处理原则：这些卡更像章节总纲或讲义入口，缺具体题目与个人错点。应等待拆分为具体题，或由用户确认某一道题的第一卡点后再启用 method_gap。

### OCR/题图/个人错因不足

- [GS-405](http://127.0.0.1:8765/open/GS-405)、[GS-408](http://127.0.0.1:8765/open/GS-408)、[GS-414](http://127.0.0.1:8765/open/GS-414)、[LA-005](http://127.0.0.1:8765/open/LA-005)、[LA-065](http://127.0.0.1:8765/open/LA-065)、[LA-080](http://127.0.0.1:8765/open/LA-080)、[LA-083](http://127.0.0.1:8765/open/LA-083)、[LA-084](http://127.0.0.1:8765/open/LA-084)、[LA-085](http://127.0.0.1:8765/open/LA-085)、[LA-086](http://127.0.0.1:8765/open/LA-086)、[LA-095](http://127.0.0.1:8765/open/LA-095)、[LA-096](http://127.0.0.1:8765/open/LA-096)

处理原则：当前只能保留“待复做后补齐”或“needs_ocr”。若用户提供题图和错解过程，可正式启用 method_gap。

### 疑似错连/原图缺失

- [GS-426](http://127.0.0.1:8765/open/GS-426)、[GS-427](http://127.0.0.1:8765/open/GS-427)、[GS-428](http://127.0.0.1:8765/open/GS-428)、[GS-429](http://127.0.0.1:8765/open/GS-429)

处理原则：这些卡不能只凭标题和方法标签补 method_gap，需要先确认视觉入口和原题身份。

## 3 个 methods 占位

- [GS-408](http://127.0.0.1:8765/open/GS-408)
- [GS-414](http://127.0.0.1:8765/open/GS-414)
- [LA-005](http://127.0.0.1:8765/open/LA-005)

处理原则：这三张卡应优先等待题图/OCR/题目身份确认。没有题目内容时，不应为降低 warning 随手挂方法标签；否则会污染方法簇。

## 下一步解除顺序

1. 优先解除 `methods is placeholder or empty`：只在拿到题图或题目身份后处理 [GS-408](http://127.0.0.1:8765/open/GS-408)、[GS-414](http://127.0.0.1:8765/open/GS-414)、[LA-005](http://127.0.0.1:8765/open/LA-005)。
2. 再处理 `method_gap not enabled`：只选有题图、解析和明确复做入口的卡；没有用户个人错因时只能写低置信复做第一动作，不能冒充原始错因。
3. 最后处理可视化缺口：需要真实资产，不通过文本猜测补图。

## 边界结论

M141 之后的剩余 warning 不应被理解为“没修改文件”或“没做质量维护”。本页把它们变成可追踪、可解除的证据边界。后续降低 warning 的方式只有三类：补真实题图/OCR、用户确认第一卡点、或按合并/弃用规则处理重复与总纲卡。
