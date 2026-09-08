## [2026-08-13] ingest | 6 个数学目标正式 Wiki 增量编译

- scope: 按冻结清单 `MFI-FREEZE-29cb4273ebde6608c164ea7f` 编译 LA-114、LA-020、LA-023、GS-103、GS-596、GS-743；同题多轮讲解只汇总到同一正式题目身份。
- evidence: 个人错因只采用 2026-08-12 的真实作答、追问与确认；题图、解析图和板书只作客观题面与方法证据，讲解后理解不写成独立掌握。
- wiki: 6 份 source summary、来源总索引、GS/LA 覆盖表、多维矩阵和主索引已对齐当前正式投影；新增 5 个知识点簇、7 个方法簇和 18 个错因簇，既有相关簇按实际成员表更新。
- coverage: 正式题目身份 855，source summary 855，来源总索引 855，科目覆盖 855，多维矩阵 855；高等数学 737、线性代数 118。深度编译 821，待深度编译 34；知识点簇实际覆盖 850 张卡，不把其余 5 张边界卡虚报为已进入 knowledge 簇。
- relationships: 本轮不把对话中的相似感直接写成正式强边；既有关系与 SHADOW 证据门保持不变。
- boundary: 本记录只确认 Wiki 增量编译和只读终验；最终正式 close 仍由批次回执事务单独完成，不在 Wiki 日志提前宣告。

## [2026-08-13] lint | 6 个数学目标 Wiki 终验

- parity: `wiki_parity.py --global` 对 LA-114、LA-020、LA-023、GS-103、GS-596、GS-743 返回 `ok=true`；6 题的 subject、knowledge、methods、error_causes 与当前正式投影一致，cluster membership failures 为空。
- identity: 6 题在来源总索引、对应科目覆盖表和多维矩阵中各有且仅有一行；全库 formal/source summary/source index/subject coverage/matrix 均为 855，missing 与 orphan 均为空。
- clusters: knowledge 索引为 500 页且真实覆盖 850 张卡；method 索引为 1556 页；error 索引为 623 页。既有目标簇按实际成员数登记，包括 K021=38、K028=32、K035=24、K080=11、K141=6、M050=11、M109=6、M805=2、E006=104、E018=17。
- integrity: `wrong_questions.json` 解析通过，中央索引新增 ID 均唯一，`git diff --check` 通过。
- boundary: 未触碰 action-gap 索引的已验收更新，未运行退役的全库破坏性 Wiki 生成器，也未改写原始 capture 事实。

## [2026-08-05] ingest | LA-115 单题复发正式增量编译

- scope: 按冻结清单 `MFI-FREEZE-8dba0b7316207bccb46dd825` 更新既有正式卡 LA-115；本轮为 2026-08-05 的第 2 次错题记录。
- formal_card: 以真实对话证据替换旧的“个人错因待确认”，记录相似定义、矩阵乘法、方程组参数化、特征向量、共同对角化、逆矩阵与伴随矩阵高次幂的完整断点；掌握度为讲解依赖 2/5。
- wrongnet_and_rollback: 完成一次 successful wrongnet rebuild；回滚单元新增唯一事件 `LA-115|2026-08-05|2`，进入高优先级延迟复做。
- source_summary: `SRC-WQ-LA-115` 已对齐 2026-08-05 当前投影，并从旧占位错因簇移出；既有知识、方法和 B4-CHAIN 稳定引用保留。
- relationships: LA-018、LA-060 与 GS-413 只共享局部标签或粗动作类型，没有足够同方法证据；正式 `related` 不改，关系状态保持 SHADOW。

## [2026-08-05] lint | LA-115 目标级 Wiki 终验

- parity: source summary 的 subject、knowledge、methods、error_causes 与当前 wrongnet projection 一致，规范投影哈希为 `8a1f0f619123484f725080a51bb4ad335830451831ec78b5d11c0987b1011b78`。
- identity: LA-115 在来源总索引、线性代数覆盖表和多维矩阵中各有且仅有一行；旧占位错因簇不再包含该题。
- obsidian: Obsidian CLI 可完整读取 `SRC-WQ-LA-115`，目标摘要当前有 14 个反向链接。
- integrity: 目标正式卡、source summary 与三张索引通过 `git diff --check`；正式卡声明的两份视觉详情与四个题解资产均保留仓库内稳定路径。
- boundary: 本轮只更新 LA-115 及其必要派生表示；没有创建未经验证的新错因簇，也没有把 SHADOW 候选写入正式关系。

## [2026-08-04] formal-closeout | 10 个当日数学目标正式回落与 Wiki 增量编译

- freeze: `MFI-FREEZE-f84fd87107019fed439acc71`；按冻结账本将 GS-128、GS-629、GS-646、GS-669、GS-708、GS-738 至 GS-742 共 10 个真实题目目标串行处理。
- formal_cards: 更新 GS-128、GS-629、GS-646、GS-669、GS-708；新建 GS-738 至 GS-742；同题的多轮讲解只合并进一张正式卡，没有拆成重复错题。
- mastery: GS-629 与 GS-669 按用户当日明确的独立正确事实标记为已掌握并退出原题投递；历史断点继续保留，用于同类题迁移，不把本题删除出事实层。
- wrongnet_and_rollback: 在正式卡稳定后只执行一次成功的 wrongnet rebuild；GS-128、GS-646、GS-708 记录本日复发，GS-738 至 GS-742 创建首次错题回滚记录，掌握候选不制造做错事件。
- relationships: 关系层保持 SHADOW；只登记 GS-128↔GS-164、GS-646↔GS-647、GS-708↔GS-709、GS-738↔GS-740、GS-739↔GS-294、GS-741↔GS-742 的保留提案，GS-629 与 GS-669 无新增候选，正式 `related` 写入数为 0。
- wiki: 10 份 source summary、全量来源索引、高数覆盖表、多维矩阵、全量覆盖索引、旋转体方法页、参数曲线方法页与定积分专题页完成定点更新；计数为 854 张正式卡、854 份摘要、736 张高数卡。
- validation: `wiki_parity.py` 对 10 个目标返回 `ok=true`；Obsidian 搜索可达新卡与已掌握卡，SRC-WQ-GS-742 和 SRC-WQ-GS-629 分别有 4 与 26 个反向链接；JSON 解析与 `git diff --check` 通过。
- boundary: 未恢复或运行退役的全库破坏性 Wiki 生成器；未二次运行 wrongnet rebuild；未把提示后理解写成独立掌握，未改写原始 capture 事实。

## [2026-07-04] maintenance | MATHWIKI-MAINT-106 旧批量卡method_gap与error_causes第二批证据边界补强报告

- input: 用户指出必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并要求错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`，以及数学 wrong-intake 的 `workflow.md`、`tutor-integration.md`、`output-template.md`。
- card_updated: 10 张正式卡补强 `error_causes`、`method_gap`、正文方法断点和复做提醒：[GS-003](http://127.0.0.1:8765/open/GS-003)、[GS-004](http://127.0.0.1:8765/open/GS-004)、[GS-014](http://127.0.0.1:8765/open/GS-014)、[GS-038](http://127.0.0.1:8765/open/GS-038)、[GS-044](http://127.0.0.1:8765/open/GS-044)、[GS-045](http://127.0.0.1:8765/open/GS-045)、[GS-046](http://127.0.0.1:8765/open/GS-046)、[GS-047](http://127.0.0.1:8765/open/GS-047)、[GS-053](http://127.0.0.1:8765/open/GS-053)、[GS-054](http://127.0.0.1:8765/open/GS-054)。
- quality: 10 张单卡质量门全部 `quality_gate=ok`；全库质量门 `checked=777 failed=0 error_items=0 warn_cards=375 warn_items=717`，较 M105 减少 10 张 WARN 卡和 19 个 WARN 项。
- validation: `wrongnet.py rebuild` 成功，cards=777，strong=1934，medium=826，weak_audit=246；wiki 来源摘要、知识点簇、方法错因簇均已刷新；M106 报告已登记到 wiki/index。
- candidate_boundary: `MATHWIKI-QUESTIONS-004` 已登记完 148 条；剩余 10 条待正式判断、5 条人工重连仍缺用户确认或正确重连证据，本轮不硬转正式卡。
- tutor: 本轮只补正式卡证据边界和复做入口，没有新增稳定安全训练素材；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未手改 `生成/`；未修改回滚 JSON；未把完整题干或长解析写进正式卡；缺个人原始错因的字段均保留低置信与用户确认边界。

## [2026-07-04] maintenance | MATHWIKI-MAINT-105 旧批量卡error_causes证据边界补强报告

- input: 用户再次强调必须读取 `LLM Wiki Lint`、`Tutor` 等 skill，并要求错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`，以及数学 wrong-intake 的 `workflow.md`、`fast-path.md`、`tutor-integration.md`、`output-template.md`。
- card_updated: 12 张正式卡补强 `error_causes`、`wrong_point`、`method_gap` 和复做提醒：[GS-006](http://127.0.0.1:8765/open/GS-006)、[GS-008](http://127.0.0.1:8765/open/GS-008)、[GS-009](http://127.0.0.1:8765/open/GS-009)、[GS-010](http://127.0.0.1:8765/open/GS-010)、[GS-011](http://127.0.0.1:8765/open/GS-011)、[GS-013](http://127.0.0.1:8765/open/GS-013)、[GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-019](http://127.0.0.1:8765/open/GS-019)、[GS-023](http://127.0.0.1:8765/open/GS-023)、[GS-026](http://127.0.0.1:8765/open/GS-026)、[GS-029](http://127.0.0.1:8765/open/GS-029)、[GS-043](http://127.0.0.1:8765/open/GS-043)。
- quality: 12 张单卡质量门全部 `quality_gate=ok`；全库质量门 `checked=777 failed=0 error_items=0 warn_cards=385 warn_items=736`，较 M104 减少 12 张 WARN 卡和 12 个 WARN 项。
- validation: `wrongnet.py rebuild` 成功，cards=777，strong=1934，medium=827，weak_audit=246；wiki 来源摘要、知识点簇、方法错因簇均已刷新；M105 报告已登记到 wiki/index。
- tutor: 本轮只补正式卡证据边界和复做入口，没有新增稳定安全训练素材；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未手改 `生成/`；未修改回滚 JSON；未把完整题干或长解析写进正式卡；缺个人原始错因的字段均保留低置信与用户确认边界。

## [2026-07-04] maintenance | MATHWIKI-MAINT-104 needs_card_decision候选复核与质量扩量轮次报告

- input: 继续长期目标 `Math-WrongNet-QualityScale v1.0`，用户再次强调必须读取 `LLM Wiki Lint` 与 `Tutor` 等 skill，且质量提升必须落实到文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`，并按数学项目规则、候选台账规则和视觉导入规则执行。
- candidate_ledger: 更新 `MATHWIKI-QUESTIONS-004`，新增 `M104 needs_card_decision 决策包`；CAND-0001 至 CAND-0010 全部改写为可执行确认口径，仍保持 `candidate`。
- visual_details_updated: 10 个详情页写入 `2026-07-04 M104 复核`：`MN4-GS-CH01-079`、`MN4-GS-CH01-102`、`MN4-GS-CH01-418`、`MN4-GS-CH01-670`、`MN4-GS-CH01-683`、`VIS-GS-426-MISMATCH-OLD`、`VIS-GS-427-MISMATCH-OLD`、`VIS-GS-428-MISMATCH-OLD`、`VIS-GS-429-MISMATCH-OLD`、`MN4-GS-CH01-748`。
- manifest: 更新 `manifest.json` 的 `last_quality_enhancement=MATHWIKI-MAINT-104`、`needs_card_decision_reviewed=10`，并为 10 条候选补 `quality_note` 与 `last_reviewed=2026-07-04`。
- index_cleanup: 小范围修复 `wiki/index.md` 旧表格边界；补开 8 列来源行与 10 列 visual 行之间的边界，并把旧 `MATHWIKI-MAINT-017` 5 列记录改回当前 10 列索引格式。
- metrics: manifest `records=924 linked_wrongnet=683 merged_into_wrongnet=131 formal_card_enhanced=54 visual_gap_registered=41 needs_card_decision=10 needs_manual_relink=3 suspect_wrongnet_mismatch=2`；全库质量门 `checked=777 failed=0 error_items=0 warn_cards=397 warn_items=748`。
- validation: `manifest.json` 解析通过；台账表格和 wiki index 表格在识别 Obsidian wikilink 后 `masked_table_issues=0`；Obsidian CLI 可搜到 `M104` 详情页与 `MATHWIKI-MAINT-104`；`git diff --check` 通过。
- tutor: 本轮只做候选证据清晰化，没有新增安全训练素材；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改正式错题卡；未运行 `wrongnet.py rebuild`；未修改回滚 JSON；未伪造用户错因、正式编号或掌握度。

## [2026-07-04] maintenance | MATHWIKI-MAINT-103 N5人工重连候选复核与质量扩量轮次报告

- input: 继续长期目标 `Math-WrongNet-QualityScale v1.0`，用户要求质量提升不能只停留在查看层，必须落实到文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`workflow.md`、`tutor-integration.md`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`，并按数学项目规则和视觉导入规则执行。
- candidate_ledger: 更新 `MATHWIKI-QUESTIONS-004`，新增 `M103 人工重连决策包`；CAND-0012 至 CAND-0015 改写为可执行确认口径，CAND-0011 继续保留串题解析风险边界。
- visual_details_updated: 5 个详情页写入 `2026-07-04 M103 复核`：`MN4-GS-CH01-090`、`VIS-GS-079`、`VIS-GS-152`、`MN4-GS-CH01-514`、`VIS-LA-004`。
- metrics: manifest `records=924 linked_wrongnet=683 merged_into_wrongnet=131 formal_card_enhanced=54 visual_gap_registered=41 needs_card_decision=10 needs_manual_relink=3 suspect_wrongnet_mismatch=2`。
- validation: 台账表格在识别 Obsidian wikilink 后 `masked_table_issues=0`；Obsidian CLI 可搜到 `CAND-0012` 与 5 个 `M103` 详情页；[LA-004](http://127.0.0.1:8765/open/LA-004) 单卡质量门 `quality_gate=ok`；`git diff --check` 通过。
- tutor: 本轮只做候选重连证据清晰化，没有新增安全训练素材；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改正式错题卡；未运行 `wrongnet.py rebuild`；未修改回滚 JSON；未伪造用户错因、解析图或正式编号。

## [2026-07-04] maintenance | MATHWIKI-MAINT-102 第25轮formal_fallback缺图登记收口与质量门复核报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并要求错题质量提升必须落到文件修改。
- skills_read: 已读取 `llm-wiki-lint`、`Tutor`、`kaoyan-math-wrong-intake`、`workflow.md`、`tutor-integration.md`、`Obsidian CLI`，并复核数学项目规则与视觉导入规则。
- visual_gap_registered: 本轮为 29 张已有正式卡补 `VIS-GAP-*` 缺图登记入口：[GS-408](http://127.0.0.1:8765/open/GS-408)、[GS-414](http://127.0.0.1:8765/open/GS-414)、[GS-426](http://127.0.0.1:8765/open/GS-426)、[GS-427](http://127.0.0.1:8765/open/GS-427)、[GS-428](http://127.0.0.1:8765/open/GS-428)、[GS-429](http://127.0.0.1:8765/open/GS-429)、[GS-531](http://127.0.0.1:8765/open/GS-531)、[LA-003](http://127.0.0.1:8765/open/LA-003)、[LA-005](http://127.0.0.1:8765/open/LA-005)、[LA-006](http://127.0.0.1:8765/open/LA-006)、[LA-024](http://127.0.0.1:8765/open/LA-024)、[LA-027](http://127.0.0.1:8765/open/LA-027)、[LA-029](http://127.0.0.1:8765/open/LA-029)、[LA-051](http://127.0.0.1:8765/open/LA-051)、[LA-065](http://127.0.0.1:8765/open/LA-065)、[LA-066](http://127.0.0.1:8765/open/LA-066)、[LA-076](http://127.0.0.1:8765/open/LA-076)、[LA-077](http://127.0.0.1:8765/open/LA-077)、[LA-080](http://127.0.0.1:8765/open/LA-080)、[LA-083](http://127.0.0.1:8765/open/LA-083)、[LA-084](http://127.0.0.1:8765/open/LA-084)、[LA-085](http://127.0.0.1:8765/open/LA-085)、[LA-086](http://127.0.0.1:8765/open/LA-086)、[LA-095](http://127.0.0.1:8765/open/LA-095)、[LA-096](http://127.0.0.1:8765/open/LA-096)、[LA-101](http://127.0.0.1:8765/open/LA-101)、[LA-102](http://127.0.0.1:8765/open/LA-102)、[LA-107](http://127.0.0.1:8765/open/LA-107)、[LA-108](http://127.0.0.1:8765/open/LA-108)。
- candidate_ledger: 补登记 CAND-0144 至 CAND-0148；当前 manifest merged_into_wrongnet 维度剩余未登记 0 条。
- metrics: manifest `records=924 visual_gap_registered=41 linked_wrongnet=683 formal_card_enhanced=54`；bridge `records=924 visual_records=924 formal_fallbacks=0 assets=1270`。
- validation: 29 张单卡质量门全部 `quality_gate=ok`；全库质量门 `checked=777 failed=0 error_items=0 warn_cards=397 warn_items=748`；Obsidian CLI 已确认 `kaoyan-math` vault 可用并能搜到 `VIS-GAP-LA-108` 与 `CAND-0148`。
- tutor: 本轮只做视觉缺图登记和候选台账修补，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改正式错题卡；未运行 `wrongnet.py rebuild`；未修改回滚 JSON；未新增 Tutor 训练项；未伪造题图、解析图或 OCR。

## [2026-07-04] maintenance | MATHWIKI-MAINT-101 第24轮formal_fallback缺图登记与质量门复核报告

- input: 用户要求确认已读取相关 skill，并继续把错题质量提升落实到文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`。
- visual_gap_registered: 本轮为 12 张已有正式卡补 `VIS-GAP-*` 缺图登记入口：[GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-048](http://127.0.0.1:8765/open/GS-048)、[GS-079](http://127.0.0.1:8765/open/GS-079)、[GS-152](http://127.0.0.1:8765/open/GS-152)、[GS-249](http://127.0.0.1:8765/open/GS-249)、[GS-341](http://127.0.0.1:8765/open/GS-341)、[GS-344](http://127.0.0.1:8765/open/GS-344)、[GS-349](http://127.0.0.1:8765/open/GS-349)、[GS-362](http://127.0.0.1:8765/open/GS-362)、[GS-369](http://127.0.0.1:8765/open/GS-369)、[GS-375](http://127.0.0.1:8765/open/GS-375)、[GS-405](http://127.0.0.1:8765/open/GS-405)。
- metrics: manifest `records=895 visual_gap_registered=12 linked_wrongnet=683 formal_card_enhanced=54`；asset map 清理占位后 `records=1270 question_assets=889 solution_assets=381`；bridge `records=924 visual_records=895 formal_fallbacks=29 assets=1270`。
- validation: 12 张单卡质量门全部 `quality_gate=ok`；全库质量门 `checked=777 failed=0 error_items=0 warn_cards=0 warn_items=0`；source summaries 已刷新，`cards=777 summaries=777 compiled=753`；Obsidian CLI 已确认 `kaoyan-math` vault 可用并能搜到 `VIS-GAP-GS-042`。
- tutor: 本轮只做可视化缺图登记，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改正式错题卡；未运行 `wrongnet.py rebuild`；未修改回滚 JSON；未新增 Tutor 训练项；未伪造题图或 OCR；占位 PNG 映射已从 asset map 清理。

## 2026-07-04 MATHWIKI-MAINT-076 中值定理积分条件与Taylor视觉卡method_gap补强

- input: 用户提醒必须实际读取 `LLM Wiki Lint`、`Tutor` 等 skill，并要求错题质量提升不能停留在查看层。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-ingest`、`llm-wiki-query`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown` 及数学 wiki lint 规则。
- audit_scope: 读取并核对 8 张正式卡、8 个可视化详情页和对应题图：[GS-212](http://127.0.0.1:8765/open/GS-212)、[GS-214](http://127.0.0.1:8765/open/GS-214)、[GS-215](http://127.0.0.1:8765/open/GS-215)、[GS-216](http://127.0.0.1:8765/open/GS-216)、[GS-217](http://127.0.0.1:8765/open/GS-217)、[GS-219](http://127.0.0.1:8765/open/GS-219)、[GS-220](http://127.0.0.1:8765/open/GS-220)、[GS-223](http://127.0.0.1:8765/open/GS-223)。
- card_updated: 8 张正式卡启用低置信 `method_gap` 并补 `## 方法断点`；保留 `暂无明确个人错因`、`待评分`、`confidence: low`、`need_user_confirmation: true`。
- wiki_updated: 新增 `MATHWIKI-MAINT-076_中值定理积分条件与Taylor视觉卡method_gap补强.md`；更新 `wiki/index.md`、中值定理方法页、双端点 Taylor 方法页和 Tutor 安全输入包。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1915，medium=822，weak_audit=246；wiki coverage refresh 成功，source summaries=770/770，compiled=770/770，knowledge_clusters=406，method_clusters=1342，error_clusters=302，action_gap_clusters=9；Obsidian bridge refresh 成功，records=918，visual_records=876，assets=1256；本批 8 题单卡质量门均 `quality_gate=ok`；770 张正式卡全量质量门 `fail_count=0`，`warn_count=393`；Obsidian CLI 可检索到 `MATHWIKI-MAINT-076`。
- tutor_source: updated；只记录高层触发词、第一动作和证据边界，不复制完整题干、题图 OCR 或长解析；不启动 Tutor quiz，不反写正式卡或回滚账本。
- rollback_action: not_needed；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-04 MATHWIKI-MAINT-075 全量正式卡质量门脚本与第一动作收口

- input: 用户继续强调必须读取并应用 `LLM Wiki Lint`、`Tutor` 等 skill，同时要求质量提升必须有实际文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian Markdown` 与数学 wrong-intake workflow/Tutor integration 规则。
- audit_scope: 770 张正式错题卡运行 `intake_quality_gate.py --visual none`；首轮硬错误集中在 [GS-531](http://127.0.0.1:8765/open/GS-531) 的 wiki index/log 导航一致性；脚本修正后继续暴露 [GS-097](http://127.0.0.1:8765/open/GS-097) 裸 `待补充` wrong_point 和 [GS-225](http://127.0.0.1:8765/open/GS-225) 裸 `待补充` answer；另发现脚本对 `>-` 折叠块解析导致 11 张卡第一动作假阳性。
- code_updated: `错题知识网络/scripts/intake_quality_gate.py` 支持解析 frontmatter 中 `>-` / `|` 折叠或保留文本块，减少质量门误报。
- card_updated: [GS-048](http://127.0.0.1:8765/open/GS-048) 修正为“单调 + 无穷远极限”固定点比较入口；[GS-079](http://127.0.0.1:8765/open/GS-079) 修正为先证区间不变性，再接单调有界、固定点方程和泰勒展开；[GS-097](http://127.0.0.1:8765/open/GS-097) 将裸 `待补充` wrong_point 改为旧批量缺用户错因的证据边界句；[GS-225](http://127.0.0.1:8765/open/GS-225) 按卡内已有证明链补 `answer`。
- wiki_updated: 新增 `MATHWIKI-MAINT-075_全量正式卡质量门脚本与第一动作收口.md`；更新 `wiki/index.md` 和 Tutor 安全输入包；[GS-531](http://127.0.0.1:8765/open/GS-531) 已补入本轮 index/log 导航记录。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1915，medium=822，weak_audit=246；wiki coverage refresh 成功，summaries=770，knowledge_clusters=406，method_clusters=1342，error_clusters=302，action_gap_clusters=9；bridge refresh 成功，records=918，visual_records=876，assets=1256；[GS-048](http://127.0.0.1:8765/open/GS-048)、[GS-079](http://127.0.0.1:8765/open/GS-079)、[GS-097](http://127.0.0.1:8765/open/GS-097)、[GS-225](http://127.0.0.1:8765/open/GS-225)、[GS-531](http://127.0.0.1:8765/open/GS-531) 单卡质量门均 `quality_gate=ok`；770 张正式卡全量质量门 fail_count=0，warn_count=393。
- tutor_source: updated；只记录高层触发词、第一动作和错因训练入口，不复制完整题干、题图 OCR 或长解析；不启动 Tutor quiz，不反写正式卡或回滚账本。
- rollback_action: not_needed；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-04 MATHWIKI-MAINT-074 876条视觉记录全量质量门复核

- input: 用户提醒必须读取并应用 `LLM Wiki Lint`、`Tutor` 等 skill，且要求确认当前 876 条可视化题库是否真的处理完。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`llm-wiki-ingest`、`llm-wiki-query`、`obsidian-cli`、`obsidian-markdown` 及数学错题 workflow/Tutor integration 规则。
- audit_scope: 当前 `manifest.json` 共 876 条视觉记录；抽取 726 个唯一正式 ID 运行 `intake_quality_gate.py --visual expected`。
- validation: 726/726 `quality_gate=ok`，ERROR none，WARN none；报告保存于 `/tmp/kaoyan_math_visual_876_quality_gate_current.json`。
- boundary_decision: 剩余 10 条 `needs_card_decision`、3 条 `needs_manual_relink`、2 条 `suspect_wrongnet_mismatch` 属于证据边界，不是正式卡质量门失败；缺用户本人错因、正确解析或人工重连确认前不硬建/硬改正式卡。
- wiki_updated: 新增 `MATHWIKI-MAINT-074_876条视觉记录全量质量门复核.md`；更新 `wiki/index.md` 和 `MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md`。
- card_updated: none；不修改正式错题卡，不运行 `wrongnet.py rebuild`。
- tutor_source: not_needed；本轮未新增可训练方法模式，只确认现有证据边界；不启动 Tutor quiz，不反写正式卡或回滚账本。
- rollback_action: not_needed；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-04 MATHWIKI-MAINT-067 早期微分积分视觉质量门边界收口

- input: 历史 `already_in_wrongnet_enhanced` 视觉记录中仍写“质量门待复跑”的 14 条。
- scope: GS-248, GS-250, GS-251, GS-252, GS-254, GS-255, GS-259, GS-260, GS-261, GS-264, GS-265, GS-269, GS-270, GS-271。
- validation: 逐题运行 `intake_quality_gate.py --visual expected`，14/14 为 `quality_gate=ok`，ERROR none；WARN 均为 `method_gap not enabled`。
- boundary_decision: 不启用 method_gap；正式卡均明确缺用户本人作答过程，本轮不从题图/解析反推个人 missed_action。
- visual_update: 14 个可视化详情页、manifest 和可视化 index 已从“待复跑”收口为“quality_gate=ok，method_gap 因缺用户本人作答过程保持不反推”。
- card_updated: none；不修改正式错题卡。
- rollback_action: not_needed；本轮不修改回滚 JSON。

## 2026-07-04 MATHWIKI-MAINT-066 级数幂级数 method_gap 与来源保留收口

- input: 可视化详情 + 正式错题卡已有 `method_gap` 或已确认的正文方法断点。
- card_updated: 10 张正式卡补正文 `## 方法断点`：GS-483, GS-485, GS-486, GS-495, GS-503, GS-504, GS-502, GS-510, GS-521, GS-522；11 张已有断点卡确认同步：GS-555, GS-560, GS-561, GS-563, GS-565, GS-566, GS-588, GS-589, GS-590, GS-591, GS-596。
- visual_update: 同步 21 张高数正式视觉详情页为 `already_in_wrongnet_enhanced`；LA-001 与 MN4-GS-CH01-599 作为视觉来源页标记为 `already_in_wrongnet_source_retained`。
- wiki_updated: 新增 `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-066_级数幂级数method_gap与来源保留收口.md`，并更新 index/log/Tutor 安全输入包。
- wrongnet_rebuild: done；cards=770，strong=1918，medium=821，weak_audit=245；wiki coverage refresh success，source summaries=770，knowledge_clusters=406，method_clusters=1337，error_clusters=302，action_gap_clusters=9；visual_bridge_refresh success，records=918，visual_records=876，formal_fallbacks=42，assets=1256；quality_gate=ok，21/21，ERROR none，WARN none。
- manifest_status: `already_in_wrongnet` 队列已清零。
- rollback_action: not_needed；本轮不修改回滚 JSON。
- missing_info: LA-001 缺用户作答过程，保持来源保留；MN4-GS-CH01-599 仅作 GS-502 的别名视觉来源，不反推新错因。

## 2026-07-04 MATHWIKI-MAINT-065 变上限积分与多元隐函数 method_gap 补正文

- input: 可视化详情 + 正式错题卡已有或可由视觉详情确认的 `method_gap`。
- card_updated: 12 张正式卡补正文 `## 方法断点`：GS-287, GS-368, GS-370, GS-371, GS-372, GS-374, GS-376, GS-465, GS-464, GS-467, GS-377, GS-378；其中 GS-287 补正式错因和 method_gap，GS-376 修正旧 method_gap 串题。
- visual_update: 同步 12 张高数正式视觉详情页为 `already_in_wrongnet_enhanced`。
- wiki_updated: 新增 `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-065_变上限积分与多元隐函数method_gap补正文.md`，并更新 index/log/Tutor 安全输入包。
- wrongnet_rebuild: done；cards=770，strong=1918，medium=821，weak_audit=245；wiki coverage refresh success，source summaries=770，knowledge_clusters=406，method_clusters=1337，error_clusters=302，action_gap_clusters=9；visual_bridge_refresh success，records=918，assets=1256；quality_gate=ok，12/12，ERROR none，WARN none。
- rollback_action: not_needed；本轮不修改回滚 JSON。
- missing_info: 未新增掌握度；只使用正式卡和视觉解析中已有证据。

## 2026-07-04 MATHWIKI-MAINT-064 中值积分Wallis与多元函数 method_gap 补正文

- input: 可视化详情 + 正式错题卡已有 `method_gap`。
- card_updated: 12 张正式卡补正文 `## 方法断点`：GS-208, GS-309, GS-466, GS-316, GS-317, GS-318, GS-326, GS-359, GS-361, GS-364, GS-365, GS-366。
- visual_update: 同步 12 张高数正式视觉详情页为 `already_in_wrongnet_enhanced`；MN4-GS-CH01-278 作为 GS-208 合并来源页标记为 `already_in_wrongnet_source_retained`。
- wiki_updated: 新增 `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-064_中值积分Wallis与多元函数method_gap补正文.md`，并更新 index/log/Tutor 安全输入包。
- wrongnet_rebuild: done；cards=770，strong=1918，medium=821，weak_audit=245；wiki coverage refresh success，source summaries=770，knowledge_clusters=406，method_clusters=1335，error_clusters=301，action_gap_clusters=9；visual_bridge_refresh success，records=918，assets=1256；quality_gate=ok，12/12，ERROR none，WARN none。
- rollback_action: not_needed；本轮不修改回滚 JSON。
- missing_info: 未新增个人错因或掌握度；只把已有错点与视觉证据沉淀成可复做方法断点。

## 2026-07-04 MATHWIKI-MAINT-063 反函数变上限积分与早期高数 method_gap 补正文

- input: 可视化详情 + 正式错题卡已有或可由视觉详情确认的 `method_gap`。
- card_updated: 11 张正式卡补/修 `## 方法断点`：GS-129, GS-434, GS-480, GS-477, GS-243, GS-491, GS-473, GS-266, GS-267, GS-268, GS-283；GS-129 和 GS-283 同步修正旧卡空泛字段。
- visual_update: 同步 12 张高数可视化详情页；GS-097 因缺用户作答过程只标记为 `already_in_wrongnet_source_retained`，不反推正式错因。
- wiki_updated: 新增 `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-063_反函数变上限积分与早期高数method_gap补正文.md`，并更新 index/log/Tutor 安全输入包。
- wrongnet_rebuild: done；cards=770，strong=1918，medium=821，weak_audit=245；wiki coverage refresh success，source summaries=770，knowledge_clusters=406，method_clusters=1335，error_clusters=301，action_gap_clusters=9；visual_bridge_refresh success，records=918，assets=1256；quality_gate=ok，11/11，ERROR none，WARN none。
- rollback_action: not_needed；本轮不修改回滚 JSON。
- missing_info: GS-097 缺用户当时作答过程，正式卡 `wrong_point/error_causes/method_gap` 保持不反推。

## 2026-07-04 MATHWIKI-MAINT-062 连乘极限中值证明 method_gap 补正文

- input: 可视化详情 + 正式错题卡已有 `method_gap`。
- card_updated: 12 张正式卡补正文 `## 方法断点`：GS-442, GS-532, GS-474, GS-476, GS-221, GS-514, GS-506, GS-225, GS-232, GS-489, GS-432, GS-513。
- visual_update: 同步 12 张高数可视化详情页的状态、正确第一步、核心方法、易错触发和复做提醒，状态收口为 `already_in_wrongnet_enhanced`。
- skipped: GS-208 题图显示线代矩阵秩内容，与正式高数卡不一致，本轮不处理。
- wiki_updated: 新增 `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-062_连乘极限中值证明method_gap补正文.md`，并更新 index/log/Tutor 安全输入包。
- wrongnet_rebuild: done；cards=770，strong=1915，medium=822，weak_audit=248；wiki coverage refresh success，source summaries=770，knowledge_clusters=405，method_clusters=1330，error_clusters=301，action_gap_clusters=9；visual_bridge_refresh success，records=918，assets=1256；quality_gate=ok，12/12，ERROR none，WARN none。
- rollback_action: not_needed；本轮不修改回滚 JSON。
- missing_info: 未新增个人错因或掌握度；只使用已确认字段。

## 2026-07-04 MATHWIKI-MAINT-061 导数应用积分极限 method_gap 补正文

- input: 可视化详情 + 正式错题卡已有 `method_gap`。
- card_updated: 12 张正式卡补正文 `## 方法断点`：GS-100, GS-104, GS-107, GS-127, GS-524, GS-138, GS-451, GS-143, GS-145, GS-537, GS-163, GS-170。
- visual_update: 同步 12 张高数可视化详情页的状态、正确第一步、核心方法、易错触发和复做提醒，状态收口为 `already_in_wrongnet_enhanced`。
- wiki_updated: 新增 `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-061_导数应用积分极限method_gap补正文.md`，并更新 index/log/Tutor 安全输入包。
- wrongnet_rebuild: done；cards=770，strong=1911，medium=828，weak_audit=248。
- validation: LLM Wiki 覆盖脚本、Obsidian bridge refresh 已通过；12 张目标卡 `quality_gate=ok` 且无 ERROR/WARN。
- rollback_action: not_needed；本轮不修改回滚 JSON。
- missing_info: 未新增个人错因或掌握度；只使用已确认字段。

## 2026-07-04｜极限与递推第二批 method_gap 收口 GS-007/018/019/023/026/029

## 2026-07-04 MATHWIKI-MAINT-060 数列极限与导数定义 method_gap 补正文

- input: 可视化详情 + 正式错题卡已有 `method_gap`。
- card_updated: 12 张正式卡补正文 `## 方法断点`：GS-431, GS-439, GS-444, GS-441, GS-490, GS-433, GS-435, GS-086, GS-092, GS-093, GS-094, GS-096。
- visual_update: 同步 12 张高数可视化详情页的状态、正确第一步、核心方法、易错触发和复做提醒，状态收口为 `already_in_wrongnet_enhanced`。
- wiki_updated: 新增 `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-060_数列极限与导数定义method_gap补正文.md`，并更新 index/log/Tutor 安全输入包。
- wrongnet_rebuild: done；cards=770，strong=1911，medium=828，weak_audit=248。
- validation: LLM Wiki 覆盖脚本、Obsidian bridge refresh 已通过；12 张目标卡 `quality_gate=ok` 且无 ERROR/WARN。
- rollback_action: not_needed；本轮不修改回滚 JSON。
- missing_info: 未新增个人错因或掌握度；只使用已确认字段。

## 2026-07-04 MATHWIKI-MAINT-059 早期极限递推定积分 method_gap 补正文

- 范围：GS-001; GS-002; GS-021; GS-028; GS-044; GS-046; GS-051; GS-066; GS-071; GS-074; GS-081; GS-084。
- 读取：正式错题卡、可视化题图/折叠解析、manifest/index、Tutor 安全输入包。
- 修改：12 张正式卡补 `## 方法断点`；GS-001、GS-002、GS-021、GS-028、GS-044、GS-051、GS-066、GS-071、GS-074、GS-081、GS-084 启用/修正 method_gap；GS-046 仅登记安全复做入口，不反推个人错因。
- 同步：对应视觉详情、可视化 manifest/index、asset 映射、维护页和 Tutor 安全输入包。
- 验证：wrongnet rebuild 已通过；wiki coverage 与 Obsidian bridge 已刷新；质量门最终复跑后回填维护页。

- scope: [GS-007](http://127.0.0.1:8765/open/GS-007)、[GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-019](http://127.0.0.1:8765/open/GS-019)、[GS-023](http://127.0.0.1:8765/open/GS-023)、[GS-026](http://127.0.0.1:8765/open/GS-026)、[GS-029](http://127.0.0.1:8765/open/GS-029)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-ingest`、`llm-wiki-query`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库规则。
- evidence: 读取 6 张正式卡和 6 张可视化详情页；解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 6 张正式卡新增或启用 `method_gap` 与正文方法断点；[GS-018](http://127.0.0.1:8765/open/GS-018) 保持已掌握状态；个人原始错因不足的卡保留 `error_causes: 待补充`。
- visual_update: 同步 6 张高数可视化详情页的 frontmatter、“正确第一步”“易错触发”“复做提醒”和入库判断，状态收口为 `already_in_wrongnet_enhanced`。
- wiki_updated: 新增 `MATHWIKI-MAINT-058_极限与递推method_gap第二批第一动作收口.md`；更新 `wiki/index.md`、可视化 index/manifest/asset map 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入绝对值内对数符号、无穷远增长阶排序、无穷大分式最高阶、隐式递推中值定理、指数函数作差、对数差商合并等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；manifest、asset map 与 bridge records JSON 检查通过；Obsidian CLI 可搜到 `MATHWIKI-MAINT-058`；`git diff --check` 通过；6 张目标卡均为 `quality_gate=ok` 且无 ERROR，GS-018/019/023/026/029 的 WARN 仅为 `error_causes is placeholder or empty`，原因是个人原始错因未记录，本轮不编造个人错因；GS-007 无 WARN。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-04｜极限首批候选 method_gap 收口 GS-006/008/009/010/011/013
- scope: [GS-006](http://127.0.0.1:8765/open/GS-006)、[GS-008](http://127.0.0.1:8765/open/GS-008)、[GS-009](http://127.0.0.1:8765/open/GS-009)、[GS-010](http://127.0.0.1:8765/open/GS-010)、[GS-011](http://127.0.0.1:8765/open/GS-011)、[GS-013](http://127.0.0.1:8765/open/GS-013)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-ingest`、`llm-wiki-query`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库规则。
- evidence: 读取 6 张正式卡、6 张可视化详情页和 MAINT-004 的既有复做入口；折叠解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 6 张正式卡新增低置信度 `method_gap` 候选与正文方法断点；因个人原始错因未记录，保留 `error_causes: 待补充`，并设置 `need_user_confirmation: true`。
- visual_update: 同步 6 张高数可视化详情页的 frontmatter、“正确第一步”“易错触发”“复做提醒”和入库判断，状态收口为 `already_in_wrongnet_enhanced`，保持题目可见、解析折叠。
- wiki_updated: 新增 `MATHWIKI-MAINT-057_极限首批method_gap候选第一动作收口.md`；更新 `wiki/index.md`、可视化 index/manifest/asset map 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入 n 次根号最大项、递推收缩估计、幂指极限取对数、指数型作差、幂指定义域、负指数 n 次根号等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；manifest 与 asset map JSON 检查通过；Obsidian CLI 可搜到 `MATHWIKI-MAINT-057`；`git diff --check` 通过；6 张目标卡均为 `quality_gate=ok` 且无 ERROR，WARN 仅为 `error_causes is placeholder or empty`，原因是个人原始错因未记录，本轮不编造个人错因。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-04｜高数积分级数第一动作第十五批规范化 GS-576/578/579/581/586/611/618/625
- scope: [GS-576](http://127.0.0.1:8765/open/GS-576)、[GS-578](http://127.0.0.1:8765/open/GS-578)、[GS-579](http://127.0.0.1:8765/open/GS-579)、[GS-581](http://127.0.0.1:8765/open/GS-581)、[GS-586](http://127.0.0.1:8765/open/GS-586)、[GS-611](http://127.0.0.1:8765/open/GS-611)、[GS-618](http://127.0.0.1:8765/open/GS-618)、[GS-625](http://127.0.0.1:8765/open/GS-625)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-ingest`、`llm-wiki-query`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库规则。
- evidence: 读取 8 张正式卡、8 张可视化详情页和上一批 `MATHWIKI-MAINT-055` 格式；折叠解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 8 张正式卡补强 `method_gap.expected_first_action`，把变上限积分、凹函数定义、含参变限积分、反常积分收敛约束、周期平均值、指数项级数、三角代换回代和参数退化分类统一写成可复做第一动作。
- visual_update: 同步 8 张高数可视化详情页的 frontmatter、“正确第一步”和入库判断，状态收口为 `already_in_wrongnet_enhanced`，保持题目可见、解析折叠。
- wiki_updated: 新增 `MATHWIKI-MAINT-056_高数积分级数method_gap第十五批第一动作规范化.md`；更新 `wiki/index.md`、`wiki/log.md`、可视化 index/manifest/asset map 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入变上限积分微分不等式、凹函数定义定积分比较、参数方程含参变限积分、反常积分收敛性反推参数、周期函数积分平均值、拆级数几何入口、根式三角代换回代、参数退化三角凑微分等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；manifest、asset map 与 bridge records JSON 检查通过；8 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN；Obsidian CLI 可搜到 `MATHWIKI-MAINT-056`；`git diff --check` 通过；本轮 8 张目标卡的第一动作候选已清空。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-04｜高数级数与一元积分第一动作第十四批规范化 GS-552/553/554/556/557/558/559/564/569/572/573/574
- scope: [GS-552](http://127.0.0.1:8765/open/GS-552)、[GS-553](http://127.0.0.1:8765/open/GS-553)、[GS-554](http://127.0.0.1:8765/open/GS-554)、[GS-556](http://127.0.0.1:8765/open/GS-556)、[GS-557](http://127.0.0.1:8765/open/GS-557)、[GS-558](http://127.0.0.1:8765/open/GS-558)、[GS-559](http://127.0.0.1:8765/open/GS-559)、[GS-564](http://127.0.0.1:8765/open/GS-564)、[GS-569](http://127.0.0.1:8765/open/GS-569)、[GS-572](http://127.0.0.1:8765/open/GS-572)、[GS-573](http://127.0.0.1:8765/open/GS-573)、[GS-574](http://127.0.0.1:8765/open/GS-574)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor`，并沿用数学错题入库、Obsidian Markdown、Tutor 安全输入规则。
- evidence: 读取 12 张正式卡、12 张可视化详情页和上一批 `MATHWIKI-MAINT-054` 格式；折叠解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 12 张正式卡补强 `method_gap.expected_first_action`；[GS-552](http://127.0.0.1:8765/open/GS-552) 额外修正泛化 `method_trigger`、`expected_method`、`missed_action` 和 `next_reminder`，使其回到“对数小量 + 指数因子通项极限”的真实入口。
- visual_update: 同步 12 张高数可视化详情页的 frontmatter、“正确第一步”“复做提醒”和入库判断，状态收口为 `already_in_wrongnet_enhanced`，保持题目可见、解析折叠。
- wiki_updated: 新增 `MATHWIKI-MAINT-055_高数级数与一元积分method_gap第十四批第一动作规范化.md`；更新 `wiki/index.md`、`wiki/log.md`、可视化 index/manifest/asset map 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入对数小量通项、指数通项判散、对数主项判散、正弦小量、余弦二阶小量、幂对数互化、对数幂型、导数项差分、变指数积分判别、原函数性质、分段变上限积分、分段原函数常数匹配等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；manifest、asset map 与 bridge records JSON 检查通过；12 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN；Obsidian CLI 可搜到 `MATHWIKI-MAINT-055`；`git diff --check` 通过；第一动作候选复核后剩余同类 WARN 为 8 个，下一批从 GS-576 开始。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-03｜高数一元级数第一动作第十三批规范化 GS-538/540/541/542/543/544/546/547/548/549/550/551
- scope: [GS-538](http://127.0.0.1:8765/open/GS-538)、[GS-540](http://127.0.0.1:8765/open/GS-540)、[GS-541](http://127.0.0.1:8765/open/GS-541)、[GS-542](http://127.0.0.1:8765/open/GS-542)、[GS-543](http://127.0.0.1:8765/open/GS-543)、[GS-544](http://127.0.0.1:8765/open/GS-544)、[GS-546](http://127.0.0.1:8765/open/GS-546)、[GS-547](http://127.0.0.1:8765/open/GS-547)、[GS-548](http://127.0.0.1:8765/open/GS-548)、[GS-549](http://127.0.0.1:8765/open/GS-549)、[GS-550](http://127.0.0.1:8765/open/GS-550)、[GS-551](http://127.0.0.1:8765/open/GS-551)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库规则。
- evidence: 读取 12 张正式卡、12 张可视化详情页和对应题图；折叠解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 11 张正式卡补强 `method_gap.method_trigger`、`expected_method`、`expected_first_action`、`missed_action`、`action_gap_type`、`related_method_card_id` 和 `next_reminder`；[GS-544](http://127.0.0.1:8765/open/GS-544) 保留已具体化 method_gap，仅同步可视化状态。
- visual_update: 同步 12 张高数可视化详情页的“正确第一步”和“复做提醒”，状态收口为 `already_in_wrongnet_enhanced`，保持题目可见、解析折叠。
- wiki_updated: 新增 `MATHWIKI-MAINT-054_高数一元级数method_gap第十三批第一动作规范化.md`；更新 `wiki/index.md`、`wiki/log.md` 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入隐式曲线纵坐标最值、切线截距动点、加权点两段拉氏、行列式转割线斜率、分段拉氏与柯西、Wallis 递推差分、无穷小最低阶、对数母式拆分、反正切幂级数、傅里叶点值化简、半区间余弦偶延拓等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；manifest、asset map 与 bridge records JSON 检查通过；12 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN；Obsidian CLI 可搜到 `MATHWIKI-MAINT-054`；`git diff --check` 通过；此前 32 个第一动作候选复核后剩余同类 WARN 为 20 个，下一批从 GS-552 开始。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-03｜高数级数与一元应用第一动作第十二批规范化 GS-520/521/522/523/525/527/528/532/533/534/535/536
- scope: [GS-520](http://127.0.0.1:8765/open/GS-520)、[GS-521](http://127.0.0.1:8765/open/GS-521)、[GS-522](http://127.0.0.1:8765/open/GS-522)、[GS-523](http://127.0.0.1:8765/open/GS-523)、[GS-525](http://127.0.0.1:8765/open/GS-525)、[GS-527](http://127.0.0.1:8765/open/GS-527)、[GS-528](http://127.0.0.1:8765/open/GS-528)、[GS-532](http://127.0.0.1:8765/open/GS-532)、[GS-533](http://127.0.0.1:8765/open/GS-533)、[GS-534](http://127.0.0.1:8765/open/GS-534)、[GS-535](http://127.0.0.1:8765/open/GS-535)、[GS-536](http://127.0.0.1:8765/open/GS-536)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库规则。
- evidence: 读取 12 张正式卡、12 张可视化详情页和对应题图；解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 12 张正式卡补强 `method_gap.method_trigger`、`expected_method`、`expected_first_action`、`missed_action`、`action_gap_type`、`related_method_card_id` 和 `next_reminder`；撤掉级数通项、递推幂级数、二阶导、区间再现积分、通用中值构造、一阶 Peano、普通积分化简等不可靠模板误挂。
- visual_update: 同步 12 张高数可视化详情页的“正确第一步”和“复做提醒”，保持题目可见、解析折叠。
- wiki_updated: 新增 `MATHWIKI-MAINT-053_高数级数与一元应用method_gap第十二批第一动作规范化.md`；更新 `wiki/index.md`、`wiki/log.md` 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入常系数微分方程综合、分母含 \(n\) 幂级数、分子含 \(n\) 幂级数、分段点导函数连续、导函数图像判极值拐点、变上限积分方程、高阶导零因子筛选、指数因子罗尔、幂指泰勒、导数介值费马、Taylor 余项端点相减、整体求导判常数等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；manifest、asset map 与 bridge records JSON 检查通过；12 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN；Obsidian CLI 可搜到 `MATHWIKI-MAINT-053`；`git diff --check` 通过；44 个第一动作候选复核后剩余同类 WARN 为 32 个，下一批从 GS-538 开始。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-03｜高数级数与一元应用第一动作第十一批规范化 GS-504/506/508/509/510/511/514/515/516/517/518/519
- scope: [GS-504](http://127.0.0.1:8765/open/GS-504)、[GS-506](http://127.0.0.1:8765/open/GS-506)、[GS-508](http://127.0.0.1:8765/open/GS-508)、[GS-509](http://127.0.0.1:8765/open/GS-509)、[GS-510](http://127.0.0.1:8765/open/GS-510)、[GS-511](http://127.0.0.1:8765/open/GS-511)、[GS-514](http://127.0.0.1:8765/open/GS-514)、[GS-515](http://127.0.0.1:8765/open/GS-515)、[GS-516](http://127.0.0.1:8765/open/GS-516)、[GS-517](http://127.0.0.1:8765/open/GS-517)、[GS-518](http://127.0.0.1:8765/open/GS-518)、[GS-519](http://127.0.0.1:8765/open/GS-519)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库 workflow/output/tutor 集成规则。
- evidence: 读取 12 张正式卡、12 张可视化详情页和对应题图；解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 12 张正式卡补强 `method_gap.method_trigger`、`expected_method`、`expected_first_action`、`missed_action`、`action_gap_type`、`related_method_card_id` 和 `next_reminder`；撤掉乘积求导、一阶泰勒、中值定理构造、递推微分方程等不可靠方法误挂。
- visual_update: 同步 12 张高数可视化详情页的“正确第一步”和“复做提醒”，保持题目可见、解析折叠。
- wiki_updated: 新增 `MATHWIKI-MAINT-052_高数级数与一元应用method_gap第十一批第一动作规范化.md`；更新 `wiki/index.md`、`wiki/log.md` 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入乘积配项比较、交叉乘商函数、最低非零泰勒项、必有型反例、调和部分和根值、缺项幂级数整体比值、凸性端点弦、积分因子微分不等式、含参正项级数重要极限、条件收敛端点定半径、和型幂级数拆分、卷积型和函数等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；manifest、asset map 与 bridge records JSON 检查通过；12 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN；Obsidian CLI 可搜到 `MATHWIKI-MAINT-052`；104 个第一动作候选复核后剩余同类 WARN 为 44 个，下一批从 GS-520 开始。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-03｜高数级数与一元应用第一动作第十批规范化 GS-486/487/488/489/490/491/495/496/498/499/501/503
- scope: [GS-486](http://127.0.0.1:8765/open/GS-486)、[GS-487](http://127.0.0.1:8765/open/GS-487)、[GS-488](http://127.0.0.1:8765/open/GS-488)、[GS-489](http://127.0.0.1:8765/open/GS-489)、[GS-490](http://127.0.0.1:8765/open/GS-490)、[GS-491](http://127.0.0.1:8765/open/GS-491)、[GS-495](http://127.0.0.1:8765/open/GS-495)、[GS-496](http://127.0.0.1:8765/open/GS-496)、[GS-498](http://127.0.0.1:8765/open/GS-498)、[GS-499](http://127.0.0.1:8765/open/GS-499)、[GS-501](http://127.0.0.1:8765/open/GS-501)、[GS-503](http://127.0.0.1:8765/open/GS-503)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库 workflow/output/tutor 集成规则。
- evidence: 读取 12 张正式卡、12 张可视化详情页和对应题图；解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 12 张正式卡补强 `method_gap.method_trigger`、`expected_method`、`expected_first_action`、`missed_action`、`action_gap_type`、`related_method_card_id` 和 `next_reminder`；撤掉幂级数、傅里叶、通用中值、幂指比较、交错级数直接套判等不可靠方法误挂。
- visual_update: 同步 12 张高数可视化详情页的“正确第一步”和“复做提醒”；修正 GS-490/GS-491 视觉错挂，交换题图归属并更新 detail note 路径、可视化索引、open-link 表、manifest 与 asset map。
- wiki_updated: 新增 `MATHWIKI-MAINT-051_高数级数与一元应用method_gap第十批第一动作规范化.md`；更新 `wiki/index.md`、`wiki/log.md` 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入方程根列判敛、正弦小量级数、指数因子罗尔、柯西端点差、凹凸性不等式、幂指数比较、复杂正项级数拆项、交错级数正项检查、分段点极值、参数方程二阶导、分母含交错项、有界振荡因子等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；manifest 与 asset map JSON 检查通过；12 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN；Obsidian CLI 可搜到 `MATHWIKI-MAINT-051` 和 `GS-490_57899-1`；92 个第一动作候选复核后剩余同类 WARN 为 56 个，下一批从 GS-504 开始。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-03｜高数中值级数第一动作第九批规范化 GS-471/474/475/476/477/478/479/480/481/482/484/485
- scope: [GS-471](http://127.0.0.1:8765/open/GS-471)、[GS-474](http://127.0.0.1:8765/open/GS-474)、[GS-475](http://127.0.0.1:8765/open/GS-475)、[GS-476](http://127.0.0.1:8765/open/GS-476)、[GS-477](http://127.0.0.1:8765/open/GS-477)、[GS-478](http://127.0.0.1:8765/open/GS-478)、[GS-479](http://127.0.0.1:8765/open/GS-479)、[GS-480](http://127.0.0.1:8765/open/GS-480)、[GS-481](http://127.0.0.1:8765/open/GS-481)、[GS-482](http://127.0.0.1:8765/open/GS-482)、[GS-484](http://127.0.0.1:8765/open/GS-484)、[GS-485](http://127.0.0.1:8765/open/GS-485)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-ingest`、`llm-wiki-query`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库 workflow/output/tutor 集成规则。
- evidence: 读取 12 张正式卡、12 张可视化详情页和对应题图；解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 12 张正式卡补强 `method_gap.method_trigger`、`expected_method`、`expected_first_action`、`missed_action`、`action_gap_type`、`related_method_card_id` 和 `next_reminder`；撤掉一阶泰勒、通用乘积求导、不等式差函数、幂级数递推、对数估计、通项化简等不可靠方法误挂。
- visual_update: 同步 12 张高数可视化详情页的“正确第一步”和“复做提醒”，保持题目可见、解析折叠。
- wiki_updated: 新增 `MATHWIKI-MAINT-050_高数中值级数method_gap第九批第一动作规范化.md`；更新 `wiki/index.md`、`wiki/log.md` 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入乘法函数方程凑导数、罗尔积分因子、无穷区间费马、作差辅助函数、二阶导中值不等式、偏离点拉格朗日、零点分割拉氏、部分和子列、阶乘放缩、正项平方比较、单调错位比较等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；12 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN；80 个第一动作候选复核后剩余同类 WARN 为 68 个，下一批从 GS-486 开始。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-03｜高数早期第一动作第八批规范化 GS-450/451/452/453/454/455/456/464/465/466/467/469
- scope: [GS-450](http://127.0.0.1:8765/open/GS-450)、[GS-451](http://127.0.0.1:8765/open/GS-451)、[GS-452](http://127.0.0.1:8765/open/GS-452)、[GS-453](http://127.0.0.1:8765/open/GS-453)、[GS-454](http://127.0.0.1:8765/open/GS-454)、[GS-455](http://127.0.0.1:8765/open/GS-455)、[GS-456](http://127.0.0.1:8765/open/GS-456)、[GS-464](http://127.0.0.1:8765/open/GS-464)、[GS-465](http://127.0.0.1:8765/open/GS-465)、[GS-466](http://127.0.0.1:8765/open/GS-466)、[GS-467](http://127.0.0.1:8765/open/GS-467)、[GS-469](http://127.0.0.1:8765/open/GS-469)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-ingest`、`llm-wiki-query`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库规则。
- evidence: 读取 12 张正式卡、12 张可视化详情页和对应题图；解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 12 张正式卡补强 `method_gap.method_trigger`、`expected_method`、`expected_first_action`、`missed_action`、`action_gap_type`、`related_method_card_id`、`next_reminder`；撤掉一元积分、连续间断、递推固定点、幂指极限、二阶参数导、分段点、二重积分极坐标等不可靠方法误挂。
- visual_update: 同步 12 张高数可视化详情页的“正确第一步”和“复做提醒”，保持题目可见、解析折叠。
- wiki_updated: 新增 `MATHWIKI-MAINT-049_高数早期method_gap第八批第一动作规范化.md`；更新 `wiki/index.md`、`wiki/log.md` 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入泰勒余项积分放缩、拐点候选、单点导数保号、导数定义型数列极限、极限反推展开系数、对数展开符号、参数方程导数定义、隐函数极值、二元隐函数偏导、绝对值复合求导、对数化简求导、极坐标曲线切线等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；12 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN；92 个第一动作候选复核后剩余同类 WARN 为 80 个。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-03｜高数早期第一动作第七批规范化 GS-439/440/441/442/443/444/446/447/448/449
- scope: [GS-439](http://127.0.0.1:8765/open/GS-439)、[GS-440](http://127.0.0.1:8765/open/GS-440)、[GS-441](http://127.0.0.1:8765/open/GS-441)、[GS-442](http://127.0.0.1:8765/open/GS-442)、[GS-443](http://127.0.0.1:8765/open/GS-443)、[GS-444](http://127.0.0.1:8765/open/GS-444)、[GS-446](http://127.0.0.1:8765/open/GS-446)、[GS-447](http://127.0.0.1:8765/open/GS-447)、[GS-448](http://127.0.0.1:8765/open/GS-448)、[GS-449](http://127.0.0.1:8765/open/GS-449)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor` 与数学错题入库规则；沿用已读 `tutor-setup`、`obsidian-cli`、`obsidian-markdown` 规则。
- evidence: 读取 10 张正式卡、10 张可视化详情页和对应题图；解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 10 张正式卡补强 `method_gap.method_trigger`、`expected_method`、`expected_first_action`、`missed_action`、`next_reminder`；[GS-439](http://127.0.0.1:8765/open/GS-439)、[GS-442](http://127.0.0.1:8765/open/GS-442)、[GS-446](http://127.0.0.1:8765/open/GS-446)、[GS-447](http://127.0.0.1:8765/open/GS-447)、[GS-449](http://127.0.0.1:8765/open/GS-449) 撤掉不可靠 `related_method_card_id` 误挂，改为 `待匹配`。
- visual_update: 同步 10 张高数可视化详情页的“正确第一步”和“复做提醒”，保持题目可见、解析折叠。
- wiki_updated: 新增 `MATHWIKI-MAINT-048_高数早期method_gap第七批第一动作规范化.md`；更新 `wiki/index.md`、`wiki/log.md` 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入 \(n\) 次根差值指数化、变上限积分端点化、对数递推差商、连乘可消结构、多项式剩余因式、三角递推作差、相邻差递推、零点可导差商、未知分界点、奇函数导数符号迁移等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；10 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN；102 个第一动作候选复核后剩余同类 WARN 为 92 个。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-03｜高数早期第一动作第六批规范化 GS-318/326/331/430/431/432/434/435/436/438
- scope: [GS-318](http://127.0.0.1:8765/open/GS-318)、[GS-326](http://127.0.0.1:8765/open/GS-326)、[GS-331](http://127.0.0.1:8765/open/GS-331)、[GS-430](http://127.0.0.1:8765/open/GS-430)、[GS-431](http://127.0.0.1:8765/open/GS-431)、[GS-432](http://127.0.0.1:8765/open/GS-432)、[GS-434](http://127.0.0.1:8765/open/GS-434)、[GS-435](http://127.0.0.1:8765/open/GS-435)、[GS-436](http://127.0.0.1:8765/open/GS-436)、[GS-438](http://127.0.0.1:8765/open/GS-438)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库规则。
- evidence: 读取 10 张正式卡、10 张可视化详情页和对应题图；解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 10 张正式卡补强 `wrong_point`、`method_gap.method_trigger`、`expected_method`、`expected_first_action`、`missed_action`、`next_reminder`；[GS-326](http://127.0.0.1:8765/open/GS-326) 补掉旧卡 `error_causes` 占位并清理正文噪声；[GS-434](http://127.0.0.1:8765/open/GS-434) 去除不可靠的 `related_method_card_id` 误挂，改为 `待匹配`。
- visual_update: 同步 10 张高数可视化详情页的“正确第一步”“易错触发”和“复做提醒”，保持题目可见、解析折叠。
- wiki_updated: 新增 `MATHWIKI-MAINT-047_高数早期method_gap第六批第一动作规范化.md`；更新 `wiki/index.md` 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入辅助函数反推、对称区间定积分、复合振荡积分、比值型数列极限、三项递推降阶、零点唯一性、平移差望远镜、方程根列比较、非 1 底数幂指极限、同名函数差值等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；10 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN；112 个第一动作候选复核后剩余同类 WARN 为 102 个。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-03｜高数早期第一动作第五批规范化 GS-225/232/243/266/267/268/309/312/316/317
- scope: [GS-225](http://127.0.0.1:8765/open/GS-225)、[GS-232](http://127.0.0.1:8765/open/GS-232)、[GS-243](http://127.0.0.1:8765/open/GS-243)、[GS-266](http://127.0.0.1:8765/open/GS-266)、[GS-267](http://127.0.0.1:8765/open/GS-267)、[GS-268](http://127.0.0.1:8765/open/GS-268)、[GS-309](http://127.0.0.1:8765/open/GS-309)、[GS-312](http://127.0.0.1:8765/open/GS-312)、[GS-316](http://127.0.0.1:8765/open/GS-316)、[GS-317](http://127.0.0.1:8765/open/GS-317)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库规则。
- evidence: 读取 10 张正式卡、10 张可视化详情页和对应题图；解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 10 张正式卡补强 `method_gap.expected_first_action`、`missed_action`、`next_reminder`；其中 [GS-266](http://127.0.0.1:8765/open/GS-266) 从幂指极限误挂纠回有理函数不定积分，[GS-267](http://127.0.0.1:8765/open/GS-267) 修复断裂错点，[GS-309](http://127.0.0.1:8765/open/GS-309) 撤掉区间再现误挂，[GS-316](http://127.0.0.1:8765/open/GS-316) 撤掉固定点方程误挂，[GS-317](http://127.0.0.1:8765/open/GS-317) 补 Wallis 极限答案。
- visual_update: 同步 9 张高数可视化详情页的“正确第一步”和“复做提醒”；[GS-312](http://127.0.0.1:8765/open/GS-312) 的可视化主线原已正确，本轮主要修正式卡。
- wiki_updated: 新增 `MATHWIKI-MAINT-046_高数早期method_gap第五批第一动作规范化.md`；更新 `wiki/index.md` 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入 Hölder 差商、中值定理端点估计、积分型方程端点符号、有理函数反正切收尾、函数方程换元积分、含参积分凑微分、积分函数奇偶性、反三角主值周期、Wallis 正切换元、Wallis 奇偶夹逼等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1910，medium=827，weak_audit=249；source summaries=770，compiled=770；knowledge_clusters=405；method_clusters=1328，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；10 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN；122 个第一动作候选复核后剩余同类 WARN 为 112 个。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-03｜高数早期第一动作第四批规范化 GS-120/121/127/138/143/145/148/163/170/221
- scope: [GS-120](http://127.0.0.1:8765/open/GS-120)、[GS-121](http://127.0.0.1:8765/open/GS-121)、[GS-127](http://127.0.0.1:8765/open/GS-127)、[GS-138](http://127.0.0.1:8765/open/GS-138)、[GS-143](http://127.0.0.1:8765/open/GS-143)、[GS-145](http://127.0.0.1:8765/open/GS-145)、[GS-148](http://127.0.0.1:8765/open/GS-148)、[GS-163](http://127.0.0.1:8765/open/GS-163)、[GS-170](http://127.0.0.1:8765/open/GS-170)、[GS-221](http://127.0.0.1:8765/open/GS-221)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`llm-wiki-ingest`、`llm-wiki-query`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库 workflow/output/tutor 集成规则。
- evidence: 读取 10 张正式卡、10 张可视化详情页和对应题图；解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 10 张正式卡补强 `method_gap.expected_first_action`、`missed_action`、`next_reminder`；其中 [GS-138](http://127.0.0.1:8765/open/GS-138) 撤掉误挂切线入口，[GS-163](http://127.0.0.1:8765/open/GS-163) 从幂指极限/定积分错连纠回三角函数有理式不定积分，[GS-221](http://127.0.0.1:8765/open/GS-221) 撤掉压缩映射误挂。
- visual_update: 同步 10 张高数可视化详情页的“正确第一步”和“复做提醒”；[GS-163](http://127.0.0.1:8765/open/GS-163) 的专题总线和 deep wiki 连线同步迁回 `MATHWIKI-GS-TOPIC-013` 与 `MATHWIKI-GS-METHOD-042`。
- wiki_updated: 新增 `MATHWIKI-MAINT-045_高数早期method_gap第四批第一动作规范化.md`；更新 `wiki/index.md`、`MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线.md`、`MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流.md` 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入反三角复合高阶导、指数分式奇偶性、切线截距极限、等价 Peano 局部形态、隐式曲线曲率、变上限积分隐函数极值、竖直切线曲率圆、三角有理式换元、连乘根式黎曼和、导数值点列单调有界等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1917，medium=817，weak_audit=251；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；10 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN；`git diff --check` 通过；152 个第一动作候选复核后剩余同类 WARN 为 122 个。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-03｜高数早期第一动作第三批规范化 GS-074/081/086/092/093/094/096/100/104/107
- scope: [GS-074](http://127.0.0.1:8765/open/GS-074)、[GS-081](http://127.0.0.1:8765/open/GS-081)、[GS-086](http://127.0.0.1:8765/open/GS-086)、[GS-092](http://127.0.0.1:8765/open/GS-092)、[GS-093](http://127.0.0.1:8765/open/GS-093)、[GS-094](http://127.0.0.1:8765/open/GS-094)、[GS-096](http://127.0.0.1:8765/open/GS-096)、[GS-100](http://127.0.0.1:8765/open/GS-100)、[GS-104](http://127.0.0.1:8765/open/GS-104)、[GS-107](http://127.0.0.1:8765/open/GS-107)。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown` 与数学错题入库 workflow/output/tutor 集成规则。
- evidence: 读取 10 张正式卡、10 张可视化详情页和对应题图；解析文字只用于校准高层第一动作，不复制完整题干、题图 OCR 或长解析到 Tutor/正式卡正文。
- card_updated: 10 张正式卡补强 `method_gap.expected_first_action`、`missed_action`、`next_reminder`；[GS-081](http://127.0.0.1:8765/open/GS-081) 修正错因标签；[GS-094](http://127.0.0.1:8765/open/GS-094) 补答案；[GS-096](http://127.0.0.1:8765/open/GS-096) 补占位错因；[GS-092](http://127.0.0.1:8765/open/GS-092)、[GS-100](http://127.0.0.1:8765/open/GS-100)、[GS-107](http://127.0.0.1:8765/open/GS-107) 保留已掌握/重复题边界。
- visual_update: 同步 10 张高数可视化详情页的“正确第一步”和“复做提醒”，保持题目可见、解析折叠。
- wiki_updated: 新增 `MATHWIKI-MAINT-044_高数早期method_gap第三批第一动作规范化.md`；更新 `wiki/index.md` 和数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入双通项递推消元、对数差中值定理、微分方程局部泰勒、复合函数差商拆分、分段点导数定义、偶函数点导数、导数定义型极限、绝对值零点左右导数、一点导数差函数保号等安全训练项；不启动 quiz，不反写正式卡或回滚账本。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1920，medium=815，weak_audit=251；source summaries=770，compiled=770；knowledge_clusters=403；method_clusters=1326，error_clusters=301，action_gap_clusters=9；bridge snapshot records=918、visual_records=876、formal_fallbacks=42、assets=1256；10 张目标卡均为 `quality_gate=ok` 且无 ERROR/WARN。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-03｜高数早期第一动作第二批与 GS-042 视觉错连迁移
- scope: [GS-025](http://127.0.0.1:8765/open/GS-025)、[GS-034](http://127.0.0.1:8765/open/GS-034)、[GS-040](http://127.0.0.1:8765/open/GS-040)、[GS-041](http://127.0.0.1:8765/open/GS-041)、[GS-049](http://127.0.0.1:8765/open/GS-049)、[GS-050](http://127.0.0.1:8765/open/GS-050)、[GS-051](http://127.0.0.1:8765/open/GS-051)、[GS-059](http://127.0.0.1:8765/open/GS-059)、[GS-073](http://127.0.0.1:8765/open/GS-073)、[GS-042](http://127.0.0.1:8765/open/GS-042)；视觉错连迁移涉及 [GS-042](http://127.0.0.1:8765/open/GS-042) 与 [LA-001](http://127.0.0.1:8765/open/LA-001)。
- evidence: 读取正式卡、可视化详情页、题图/解析图和可视化 manifest 后确认，本批 9 张高数卡的 `method_gap.expected_first_action` 仍有模板化问题；原 `VIS-GS-042` 的题图/解析实际是线性代数行列式题 `线代1000题A组1.7`，不属于高数 `GS-042`。
- card_updated: 10 张高数正式卡补强具体第一动作、题型/方法标签、标准答案或复做提醒；其中 `GS-042` 仅根据正式卡内已有题面与错点补强，不使用错连线代图；`LA-001` 补上“旧结构化导入未记录个人错因；本轮仅确认视觉错连迁移归属”的正式边界字段。重点保留“第一步到底应该先做什么”，不把用户没有说过的个人错因扩写成新事实。
- visual_update: 同步 9 张高数可视化详情页的“正确第一步”和“复做提醒”；将 `VIS-GS-042` 迁移为 `VIS-LA-001`，详情页移动到 `错题知识网络/可视化错题详情/线性代数/LA-001_线代1000题A组1.7.md`，资产移动到 `错题知识网络/assets/visual_wrong_questions/LA-001/question_01.png`；`GS-042` 保持正式卡不改，转入缺正确高数题图队列。
- wiki_updated: 新增 `MATHWIKI-MAINT-043_高数早期method_gap第二批与GS042错连迁移.md`；更新 `wiki/index.md`、`MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md`、`manifest.json`、`asset_to_obsidian.json`、可视化索引、Obsidian bridge open links 和 `refresh_obsidian_bridge_snapshot.py` 的正式卡 fallback。
- tutor_safe_update: 补入早期第一动作精修训练项和视觉错连识别训练项；只写高层方法触发，不复制完整题干、长解析或正式卡正文。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1918，medium=816，weak_audit=251；LLM Wiki coverage 已刷新，source summaries=770，compiled=770，knowledge_clusters=403，method_clusters=1326，error_clusters=301，action_gap_clusters=9；bridge snapshot 已刷新为 records=918、assets=1256，其中 formal_fallbacks=42；10 张高数目标卡与 `LA-001` 均为 `quality_gate=ok`，`GS-042` 仅保留缺正确视觉页提醒，`LA-001` 仅保留未启用 method_gap 的边界提醒；`git diff --check` 通过；Obsidian CLI 可搜到 `MATHWIKI-MAINT-043`。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-02｜弧长、物理应用与不定积分计算链闭环 GS-600/601/602/603/604/630
- scope: [GS-600](http://127.0.0.1:8765/open/GS-600)、[GS-601](http://127.0.0.1:8765/open/GS-601)、[GS-602](http://127.0.0.1:8765/open/GS-602)、[GS-603](http://127.0.0.1:8765/open/GS-603)、[GS-604](http://127.0.0.1:8765/open/GS-604)、[GS-630](http://127.0.0.1:8765/open/GS-630)。
- evidence: 六题均已有正式卡、题图和折叠解析图，且已有用户错因和 method_gap 证据；本轮不复制长解析，只补强变上限积分弧长、积分计算符号复查、定积分物理应用、指数幂分式换元、分式拆到底和分母平方分部降幂。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-074_积分计算符号与边界项复查链.md`、`MATHWIKI-GS-METHOD-075_指数幂分式换元微分吸收链.md`、`MATHWIKI-GS-METHOD-076_分式积分拆到底与分母降幂链.md`。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-015_参数曲线几何量积分限.md`、`MATHWIKI-GS-METHOD-038_定积分物理应用微元法.md`、`MATHWIKI-GS-METHOD-039_不定积分结构化化归入口.md`、`MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线.md`、`wiki/index.md`、六个可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增积分计算符号复查、指数幂分式换元、分式积分拆到底、分母平方分部降幂、变上限积分曲线弧长、速度积分平均速度训练项；只写高层第一动作，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced；本批不修改回滚 JSON。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1929，medium=724，weak_audit=469；knowledge_clusters=352，method_clusters=998，error_clusters=276，action_gap_clusters=8；source summaries=770，compiled=708；bridge snapshot records=873，assets=1253；六题质量门均为 `quality_gate=ok` 且无 WARN/ERROR；HTTP bridge 六题均返回 200；`manifest.json`、`asset_to_obsidian.json` 合法；目标 wiki/index、可视化 index、open links 表格列数校验通过；`git diff --check` 通过。
- rollback_action: not_run。

## 2026-07-02｜有理函数反常积分极限收口 GS-168
- scope: [GS-168](http://127.0.0.1:8765/open/GS-168)。
- evidence: 题图与解析图已存在；题目为 \(\int_5^{+\infty}\frac{dx}{x^2-4x+3}\)，解析确认先写 \(x^2-4x+3=(x-1)(x-3)\)，再做部分分式 \(\frac12(\frac1{x-3}-\frac1{x-1})\)，最后按 \(t\to+\infty\) 取极限，答案为 \(\frac12\ln2\)。
- card_updated: `GS-168` 从“待补充”占位卡补强为“有理函数反常积分”正式卡；保留 `暂无明确个人错因` 与 `待评分`，不从解析图反推用户当时第一错步或掌握度。
- wiki_updated: 扩展 `MATHWIKI-GS-METHOD-076_分式积分拆到底与分母降幂链.md` 与 `MATHWIKI-GS-TOPIC-006_定积分错题总线.md`；更新 `wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“有理函数反常积分训练项”：分母因式分解、部分分式、无穷上限极限化、对数差合成商后取极限；只写高层第一动作，不复制完整题干或长解析。
- visual_update: 题图保持可见，解析图和公式推导置于折叠解析块；状态更新为 `already_in_wrongnet_enhanced`。
- card_decision: already_in_wrongnet_enhanced；本题不修改回滚 JSON。

## 2026-07-02｜拐点处切线方程动作分离 GS-167
- scope: [GS-167](http://127.0.0.1:8765/open/GS-167)。
- evidence: 题图与解析图已存在；题目为 \(y=x^2+2\ln x\) 在拐点处的切线方程，解析确认 \(y'=2x+\frac2x\)、\(y''=2-\frac2{x^2}\)，定义域 \(x>0\)，拐点横坐标 \(x=1\)，切点 \((1,1)\)，切线斜率 \(y'(1)=4\)，答案 \(y=4x-3\)。
- card_updated: `GS-167` 从“待补充”占位卡补强为“拐点处切线方程”正式卡；保留 `暂无明确个人错因` 与 `待评分`，不从解析图反推用户当时第一错步或掌握度。
- wiki_updated: 扩展 `MATHWIKI-GS-METHOD-052_局部性质与导数符号单向判别.md` 与 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`；更新 `wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 在局部性质训练项中补入“拐点处切线方程”第一动作：二阶导和定义域找拐点坐标，一阶导求切线斜率，点斜式收口；只写高层方法，不复制完整题干或长解析。
- visual_update: 题图保持可见，解析图和公式推导置于折叠解析块；状态更新为 `already_in_wrongnet_enhanced`。
- card_decision: already_in_wrongnet_enhanced；本题不修改回滚 JSON。

## 2026-07-02｜含参积分、积分不等式与几何量闭环 GS-638/639/640/641/642/643/644
- scope: [GS-638](http://127.0.0.1:8765/open/GS-638)、[GS-639](http://127.0.0.1:8765/open/GS-639)、[GS-640](http://127.0.0.1:8765/open/GS-640)、[GS-641](http://127.0.0.1:8765/open/GS-641)、[GS-642](http://127.0.0.1:8765/open/GS-642)、[GS-643](http://127.0.0.1:8765/open/GS-643)、[GS-644](http://127.0.0.1:8765/open/GS-644)。
- evidence: 七题均已有正式卡、题图和折叠解析图，且已有用户错因和 method_gap 证据；本轮不复制长解析，只补强含参积分变量角色、积分不等式证明入口、闭区间候选点、面积交点参数和参数曲线几何量积分限。
- card_updated: `GS-638` 至 `GS-644` 保留既有用户错因与掌握度口径，补入稳定视觉引用和 wiki 方法页连线。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-071_含参积分变量角色与特殊点定义法.md`、`MATHWIKI-GS-METHOD-072_积分不等式证明入口链.md`。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-014_面积区域与交点参数分离.md`、`MATHWIKI-GS-METHOD-015_参数曲线几何量积分限.md`、`MATHWIKI-GS-METHOD-069_分段函数极值候选点完整列举.md`、`MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`wiki/index.md`、七个可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入 `MATHWIKI-GS-METHOD-071` 与 `MATHWIKI-GS-METHOD-072` 的 Source Mapping，并为含参积分、积分不等式、闭区间最值、面积分区、参数曲线几何量训练项补来源 ID；只写高层第一动作，不复制完整题干、完整解析或正式卡正文。
- visual_update: 七题题图保持可见、解析图保持折叠；状态统一为 `already_in_wrongnet_enhanced`，并保留本地 bridge 跳转入口。
- card_decision: already_in_wrongnet_enhanced；本批不修改回滚 JSON。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1925，medium=727，weak_audit=469；knowledge_clusters=352，method_clusters=995，error_clusters=276，action_gap_clusters=8；source summaries=770，compiled=751；bridge snapshot records=873，assets=1253；七题质量门均为 `quality_gate=ok` 且无 WARN/ERROR；HTTP bridge 七题均返回 200；目标 wiki/index、可视化 index、open links 表格列数校验通过。
- rollback_action: not_run。

## 2026-07-02｜一元积分结构中心与指数中心化闭环 GS-633/634/635/636/637
- scope: [GS-633](http://127.0.0.1:8765/open/GS-633)、[GS-634](http://127.0.0.1:8765/open/GS-634)、[GS-635](http://127.0.0.1:8765/open/GS-635)、[GS-636](http://127.0.0.1:8765/open/GS-636)、[GS-637](http://127.0.0.1:8765/open/GS-637)。
- evidence: 五题均已有正式卡、题图和解析图，且已有用户错因与 method_gap 证据；本轮不复制长解析，只补强换元合法性、整体奇偶性、分段点排序、整体变量链和指数一增一减中心化的第一动作闭环。
- card_updated: `GS-633` 至 `GS-637` 保留既有用户掌握度与错因口径，补入稳定视觉引用和 wiki 方法页连线；`GS-637` 将“指数中心化专卡（待匹配）”收口为 `MATHWIKI-GS-METHOD-070`。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-070_指数一增一减中心化.md`。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-002_一元积分近期错题簇.md`、`MATHWIKI-GS-TRIGGER-002_积分先找中心与整体.md`、`MATHWIKI-GS-CONCEPT-002_积分结构中心.md`、`wiki/index.md`、五个可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“指数一增一减中心化训练项”，并强化一元积分结构中心训练；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- visual_update: 五题题图保持可见、解析图保持折叠；状态统一为 `already_in_wrongnet_enhanced`，并保留本地 bridge 跳转入口。
- card_decision: already_in_wrongnet_enhanced；本批不修改回滚 JSON。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1925，medium=727，weak_audit=469；knowledge_clusters=352，method_clusters=994，error_clusters=276，action_gap_clusters=8；source summaries=770，compiled=751；bridge snapshot records=873，assets=1253；五题质量门均为 `quality_gate=ok` 且无 WARN/ERROR；HTTP bridge 五题均返回 200。
- rollback_action: not_run。

## 2026-07-02｜幂级数下标对齐与傅里叶对象识别闭环 GS-613/614/615/616/617
- scope: [GS-613](http://127.0.0.1:8765/open/GS-613)、[GS-614](http://127.0.0.1:8765/open/GS-614)、[GS-615](http://127.0.0.1:8765/open/GS-615)、[GS-616](http://127.0.0.1:8765/open/GS-616)、[GS-617](http://127.0.0.1:8765/open/GS-617)。
- evidence: 五题均已有正式卡、题图和解析图；本轮不复制长解析，只补强“幂级数系数提取下标对齐”和“傅里叶展开对象识别与点值求和”两条第一动作闭环。
- card_updated: `GS-613`、`GS-614` 补入稳定视觉引用、方法页连线和 AI评分；`GS-615`、`GS-616`、`GS-617` 保留用户评分口径，并补入傅里叶对象识别方法页连线。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-067_幂级数系数提取下标对齐.md` 与 `MATHWIKI-GS-METHOD-068_傅里叶展开对象识别与点值求和.md`；保留既有 `MATHWIKI-GS-METHOD-066_二阶接触曲率充分必要判断.md` 不改号。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线.md`、`wiki/index.md`、五个可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“幂级数系数提取下标对齐训练项”和“傅里叶展开对象识别训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- visual_update: 五题题图保持可见、解析图保持折叠；补全 `GS-613`、`GS-614`、`GS-615`、`GS-616` 视觉复述中被截断的易错触发；`GS-615`、`GS-617` 标题同步为正式卡标题。
- card_decision: already_in_wrongnet_enhanced；本批不修改回滚 JSON。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1924，medium=728，weak_audit=469；knowledge_clusters=352，method_clusters=993，error_clusters=276，action_gap_clusters=8；source summaries=770，compiled=751；bridge snapshot records=873，assets=1253；五题质量门均为 `quality_gate=ok`，无 WARN/ERROR；HTTP bridge 五题均返回 200；目标索引行列数校验通过。
- rollback_action: not_run。

## 2026-07-02｜交错纠缠级数拆项与条件收敛闭环 GS-597/598/599/606/607/608
- scope: [GS-597](http://127.0.0.1:8765/open/GS-597)、[GS-598](http://127.0.0.1:8765/open/GS-598)、[GS-599](http://127.0.0.1:8765/open/GS-599)、[GS-606](http://127.0.0.1:8765/open/GS-606)、[GS-607](http://127.0.0.1:8765/open/GS-607)、[GS-608](http://127.0.0.1:8765/open/GS-608)。
- evidence: 六题均已有正式卡、题图和解析图；本轮不复制长解析，只补强对数交错小量、根式振荡扰动、隐藏交错相位、代数拆项和绝对收敛证明的第一动作闭环。
- card_updated: `GS-597`、`GS-598`、`GS-599` 补入稳定视觉引用、AI评分和方法页连线；`GS-606`、`GS-607`、`GS-608` 规范掌握度口径为 AI评分，并补入 `MATHWIKI-GS-METHOD-063` 连线。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-063_交错纠缠级数拆项与条件收敛闭环.md`。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线.md`、`wiki/index.md`、六个可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“无穷级数交错纠缠训练项”和“绝对收敛证明训练项”；只写高层第一动作、收敛类型闭环和来源 ID，不复制完整题干、完整解析或正式卡正文。
- visual_update: 六题题图保持可见、解析图保持折叠；补全 `GS-598`、`GS-599`、`GS-606`、`GS-607`、`GS-608` 视觉复述中被截断的易错触发；`GS-606`、`GS-607`、`GS-608` 标题同步为正式卡标题。
- card_decision: already_in_wrongnet_enhanced；本批有既有错因和 method_gap 证据，因此可按项目规则写 AI评分；不修改回滚 JSON。
- validation: `wrongnet.py rebuild` 已通过，cards=770，strong=1920，medium=726，weak_audit=469；knowledge_clusters=352，method_clusters=987，error_clusters=276，action_gap_clusters=8；source summaries=770，compiled=751；bridge snapshot records=873，assets=1253；六题质量门均为 `quality_gate=ok`，无 ERROR。
- rollback_action: not_run。

## 2026-07-02｜微分方程降阶换元与分支保护闭环 GS-192/193/194/198/199/211
- scope: [GS-192](http://127.0.0.1:8765/open/GS-192)、[GS-193](http://127.0.0.1:8765/open/GS-193)、[GS-194](http://127.0.0.1:8765/open/GS-194)、[GS-198](http://127.0.0.1:8765/open/GS-198)、[GS-199](http://127.0.0.1:8765/open/GS-199)、[GS-211](http://127.0.0.1:8765/open/GS-211)。
- evidence: 六题均已有正式卡、题图和解析图；本轮只按视觉证据补强微分方程降阶、换元、乘积导数、指数换元、根号整体换元以及零解/分支保护入口。
- card_updated: 六张正式错题卡统一规范为“暂无明确个人错因 + 可确认题型风险”；补入 `wrong_history`、`mastery_history`、`method_gap.enabled=false` 和方法页连线，不从题图/解析图反推用户本人错因或掌握度。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-057_微分方程降阶换元与分支保护.md`。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-009_微分方程错题总线.md`、`wiki/index.md`、六个可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“微分方程降阶换元与分支保护训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced + visual/wiki navigation enhancement；缺少用户当时作答过程，因此 `method_gap` 保持 disabled。
- validation: `wrongnet.py rebuild` 已通过，最终 cards=770，strong=1909，medium=699，weak_audit=469；source summaries=770，compiled=750；knowledge_clusters=351；method_clusters=977，error_clusters=267，action_gap_clusters=8；bridge snapshot records=873，assets=1253；六题质量门均 `quality_gate=ok`，无 ERROR，仅保留 `method_gap not enabled` 的预期 WARN；目标 wiki/index、可视化 index、open links 表格列数校验通过，HTTP bridge 六题均返回 200，Obsidian 搜索能定位新方法页。
- quality_note: 待质量门复核；不反推个人错因、掌握度或 method_gap。
- rollback_action: not_run。

# 数学一 LLM Wiki 操作日志

本日志只记录 wiki/schema 层操作。修改 `错题卡/*.md`、运行 `wrongnet.py rebuild`、更新回滚复习账本时，仍要按原数学错题系统规则单独说明。

## 2026-07-02｜周期函数积分平均值夹逼链闭环 GS-043
- scope: [GS-043](http://127.0.0.1:8765/open/GS-043)。
- evidence: 题图与解析图均已存在；题目为 \(S(x)=\int_0^x|\cos t|dt\)，先证明 \(n\pi\le x<(n+1)\pi\) 时 \(2n\le S(x)<2(n+1)\)，再求 \(\lim_{x\to+\infty}\frac{S(x)}x\)。解析支持“相邻整周期夹住变上限积分，再除以 \(x\) 做同极限夹逼”的入口。
- card_updated: `GS-043` 正式卡由薄卡补为可追踪卡；保留“个人错因未记录/待确认”边界，新增 `wrong_history`、`mastery_history: 待评分`、候选 `method_gap.action_gap_type: B2-TRIGGER`，并关联方法卡 `H08-008`。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-040_绝对三角周期积分.md`、`MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`wiki/index.md`、视觉详情页、可视化索引、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 将 GS-043 加入“绝对三角周期积分训练项”；只写高层第一动作和来源 ID，不复制完整题干、解析图或正式卡正文。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-02｜幂指函数间断点候选点检查链闭环 GS-032
- scope: [GS-032](http://127.0.0.1:8765/open/GS-032)。
- evidence: 题图与解析图均已存在；题目为 \(f(x)=(1+x)^{x/\tan(x-\pi/4)}\) 在 \((0,2\pi)\) 内求间断点并分类。解析支持两条入口：先把 \(\tan(x-\frac{\pi}{4})=0\) 与 \(\tan(x-\frac{\pi}{4})\) 无定义两类候选点列全，再写成 \(e^{\frac{x\ln(1+x)}{\tan(x-\pi/4)}}\) 逐点判左右极限。
- card_updated: `GS-032` 正式卡修复截断摘要和答案；将 `wrong_point` 收口为“候选点漏列 + 幂指指数化未触发”；将 `method_gap.action_gap_type` 从后置检查改为 `B2-TRIGGER`，补 `mastery_history` 为 `2026-07-02 AI评分 2/5`。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-049_连续间断点候选点检查链.md`、`MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md`、`wiki/index.md`、视觉详情页、可视化索引、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 将 GS-032 加入“连续间断点候选点检查链训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- rollback_action: not_run；不修改 `数学一回滚复习系统/复习单元.json` 或 `复习记录.jsonl`。

## 2026-07-02｜微分方程入口判别链视觉解析闭环 GS-187/188/189/190/196/201
- scope: [GS-187](http://127.0.0.1:8765/open/GS-187), [GS-188](http://127.0.0.1:8765/open/GS-188), [GS-189](http://127.0.0.1:8765/open/GS-189), [GS-190](http://127.0.0.1:8765/open/GS-190), [GS-196](http://127.0.0.1:8765/open/GS-196), [GS-201](http://127.0.0.1:8765/open/GS-201)。
- evidence: 六题均已有正式错题卡、题图和解析图；解析图支持“微分方程先判型再计算”的共同入口：齐次型先令 \(u=y/x\)，一次式比值先平移，一阶线性周期解先比较 \(y(x+T)\)，弧长综合先解 \(y(x)\)，常系数齐次先写特征方程，变上限积分方程先换元再求导。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-056_微分方程入口判别链.md`。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-009_微分方程错题总线.md`、六个可视化详情页、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_update: 六题视觉详情页均保留题图外显、解析折叠；`GS-196` 与 `GS-201` 的解析图由直接展开改为折叠解析；全部新增 `MATHWIKI-GS-METHOD-056` 方法页链接。
- tutor_safe_update: 新增“微分方程入口判别链训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-format-normalization + visual/wiki/Tutor enhancement；本批将六张旧正式卡的 frontmatter 统一为质量门可解析格式，补入“暂无明确个人错因”边界、wrong_history/mastery_history 待评分记录和 `method_gap.enabled: false` 原因；不修改回滚 JSON，不启动 Tutor 测验。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1875，medium=705，weak_audit=469；LLM Wiki coverage 刷新成功，source summaries=770，compiled=750，knowledge_clusters=351，method_clusters=975，error_clusters=267，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；六题质量门均为 `quality_gate=ok` 且无 ERROR，仅保留 `method_gap not enabled` 的预期提醒；`manifest.json`、`asset_to_obsidian.json`、bridge `records.json` 均合法；目标 wiki/index 行均为 10 列，目标可视化 index 行均为 13 列，打开链接表目标行均为 6 列；HTTP bridge `/open/{ID}` 六题均返回 200；Obsidian CLI 可搜索到 `MATHWIKI-GS-METHOD-056` 和六张正式卡/视觉详情页；`git diff --check` 通过。
- rollback_action: not_run。

## 2026-07-02｜参数方程二阶导链式求导闭环 GS-123
- scope: [GS-123](http://127.0.0.1:8765/open/GS-123)。
- evidence: 题图与解析图均已存在；题目为 2021 年第 12 题（数学 2），给参数方程并求 \(\left.\frac{d^2y}{dx^2}\right|_{t=0}\)。解析图确认答案为 \(\frac23\)，关键链条是先由参数方程求 \(\frac{dy}{dx}\)，再除以 \(x'(t)\) 得到对 \(x\) 的二阶导。
- card_updated: `GS-123` 从薄卡补成“2021年第12题 参数方程二阶导链式求导”正式卡；写入参数方程二阶导公式、先化简 \(\frac{dy}{dx}=2t\) 再求导、以及“不要把对 \(t\) 的求导直接当成对 \(x\) 的二阶导”的复做提醒。旧卡缺少用户本人作答过程，因此保留“暂无明确个人错因”和 `method_gap.enabled: false`，不反推掌握度。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-055_参数方程二阶导链式求导.md`。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、可视化详情页、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入“参数方程二阶导链式求导训练项”；只写高层第一动作和来源 ID，不复制完整题干、题图、解析图或正式卡正文。
- card_decision: formal-card-placeholder-repair + visual/wiki navigation enhancement；不修改回滚 JSON，不启动 Tutor 测验。
- validation: `intake_closeout.py --id GS-123 --source 2021年第12题（数学2） --knowledge 参数方程求导 --knowledge 高阶导数 --knowledge 一元函数微分学应用 --visual expected` 已通过；完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终 `quality_gate=ok`，无 ERROR，仅保留“method_gap 未启用”的预期 WARN。
- rollback_action: not_run。

## 2026-07-02｜导数定义型极限反推导数闭环 GS-099
- scope: [GS-099](http://127.0.0.1:8765/open/GS-099)。
- evidence: 题图与解析图均已存在；原正式卡仍为“题干为图片/OCR 待核对/错因待补充”类薄卡，答案字段存在 \(f''(1)\) 转义误写风险。本轮依据题图和解析图补全题目摘要、标准答案、导数定义入口和复做提醒。
- card_updated: `GS-099` 补成“2022年第17题 导数定义型极限反推导数”正式卡；答案修正为 \(f'(1)=-1\)；写入 \(f(1)=0\)、加减 \(f(1)\)、真实自变量增量 \(e^{x^2}-1\) 与 \(\sin^2x\) 的动作链；保留“暂无明确个人错因”和 `method_gap.enabled: false`，不从解析图反推用户第一错步或掌握度。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-013_导数定义差商入口.md`、`MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md`、可视化详情页、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入“复合自变量导数定义反推训练项”；只写高层第一动作和来源 ID，不复制完整题干、题图、解析图或正式卡正文。
- card_decision: formal-card-update-for-existing-card + visual/wiki navigation enhancement；不修改回滚 JSON，不启动 Tutor 测验。
- validation: `intake_closeout.py --id GS-099 --source 2022年第17题 --knowledge 导数定义 --knowledge 导数定义型极限 --knowledge 自变量增量 --visual expected` 已通过；完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终 `quality_gate=ok`，无 ERROR，仅保留“个人错因占位、method_gap 未启用”的预期 WARN；`manifest.json`、`asset_to_obsidian.json`、目标 wiki/index 行、可视化 index 行和打开链接表均校验通过；[GS-099](http://127.0.0.1:8765/open/GS-099) HTTP bridge 返回 200；`git diff --check` 通过。
- rollback_action: not_run。

## 2026-07-02｜线代二次型矩阵化与矩阵幂证明视觉解析闭环 LA-031/033/034/039
- scope: [LA-031](http://127.0.0.1:8765/open/LA-031), [LA-033](http://127.0.0.1:8765/open/LA-033), [LA-034](http://127.0.0.1:8765/open/LA-034), [LA-039](http://127.0.0.1:8765/open/LA-039)。
- evidence: 四题均已有正式错题卡和题图/解析图；旧卡均为“线性代数综合待精分/OCR 待核对”类占位。本轮依据题图和解析图补全题目摘要、标准答案、方法入口和轻量陷阱。
- card_updated: `LA-031` 补成二次型规范形题，答案为 `y_1^2-y_2^2`；`LA-033` 补成核空间包含定参数与正交标准形题，答案为 `a=1,b=2` 且标准形 `6y_1^2`；`LA-034` 补成二次型正负惯性指数题，答案为正惯性指数 `1`、负惯性指数 `1`；`LA-039` 补成矩阵幂秩稳定证明题。四题均不从解析图反推用户个人错因、掌握度或 method_gap。
- wiki_created: 新建 `MATHWIKI-LA-METHOD-019_二次型矩阵化与惯性规范形.md`。
- wiki_updated: 更新 `MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md`、`MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`MATHWIKI-LA-METHOD-011_矩阵幂降维与秩空间判断.md`、四道可视化详情页、`wiki/index.md`、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入“二次型矩阵化与惯性规范形训练项”和“矩阵幂秩稳定证明训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-update-for-existing-cards + visual/wiki navigation enhancement；不修改回滚 JSON，不启动 Tutor 测验。
- validation: `intake_closeout.py --id LA-031/LA-033/LA-034/LA-039 --visual expected` 均成功；`wrongnet.py rebuild` 成功，cards=770，strong=1825，medium=710，weak_audit=483；LLM Wiki coverage 刷新成功，source summaries=770，compiled=748，knowledge_clusters=350，method_clusters=955，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；四题正式卡、视觉详情页、`MATHWIKI-LA-METHOD-019`、`MATHWIKI-LA-METHOD-011` 与相关主题页均可检索；`manifest.json` 与 `asset_to_obsidian.json` JSON 合法，相关 wiki/index 和视觉 index 行列数正确；四题 HTTP bridge 均返回 200；质量门均为 `quality_gate=ok`，仅保留“个人错因占位、method_gap 未启用”的预期提醒。
- rollback_action: not_run。

## 2026-07-02｜线代行列式结构化计算视觉解析闭环 LA-009/010/020
- scope: [LA-009](http://127.0.0.1:8765/open/LA-009), [LA-010](http://127.0.0.1:8765/open/LA-010), [LA-020](http://127.0.0.1:8765/open/LA-020)。
- evidence: 三题均已有正式错题卡和题图/解析图；旧卡中 `LA-009`、`LA-010` 仍为“线性代数综合待精分”，`LA-020` 仅有答案和粗知识点。本轮依据题图和解析图补全题目摘要、标准答案、方法入口和轻量陷阱。
- card_updated: `LA-009` 补成行列式排列展开中特定次数项系数题，答案 \(-5\)；`LA-010` 补成含参分块上三角行列式题，答案 \(a^4-4a^2\)；`LA-020` 补成代数余子式和转伴随矩阵元素和题，答案 \(-4\)。三题均不从解析图反推用户个人错因、掌握度或 method_gap。
- wiki_created: 新建 `MATHWIKI-LA-METHOD-018_行列式结构化计算与指定项系数.md`。
- wiki_updated: 更新 `MATHWIKI-LA-TOPIC-005_行列式错题总线.md`、三道可视化详情页、`wiki/index.md`、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入“行列式结构化计算训练项”：指定次数项系数先筛合法排列项，块状含参行列式先化分块上三角并补特殊参数，代数余子式和先转伴随矩阵；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-update-for-existing-cards + visual/wiki navigation enhancement；不修改回滚 JSON，不启动 Tutor 测验。
- validation: pending，本条后续由 `intake_closeout.py --id LA-009/LA-010/LA-020 --visual expected`、bridge refresh、JSON/table/Obsidian 检查收口。
- rollback_action: not_run。

## 2026-07-02｜线性方程组零空间与秩约束视觉解析闭环 LA-078/079/081
- scope: [LA-078](http://127.0.0.1:8765/open/LA-078), [LA-079](http://127.0.0.1:8765/open/LA-079), [LA-081](http://127.0.0.1:8765/open/LA-081)。
- evidence: 三题均已有正式错题卡和题图/解析图；`LA-079` 正式卡仍为占位状态，本轮依据题图和解析图补全题目摘要、标准答案、方法入口和轻量陷阱；`LA-078`、`LA-081` 正式卡已有可用摘要，本轮补强 deep wiki 导航。
- card_updated: `LA-079` 从“题干图片/OCR 待核对”补成正式轻量卡；`LA-081` 补入 `LA-079` 为关联题；不从解析图反推用户个人错因、掌握度或 method_gap。
- wiki_updated: 新建 `MATHWIKI-LA-METHOD-017_线性方程组零空间与秩约束入口链.md`；更新 `MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线.md`、三道可视化详情页、`wiki/index.md`、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 补入 \(AC=O\) 按列拆入零空间、\(r(A)+r(C)\le n\) 秩约束反证、\(AB^{\mathsf T}=O\) 行空间正交三类训练项；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-update-for-LA079 + visual/wiki navigation enhancement；不修改回滚 JSON，不启动 Tutor 测验。
- validation: `LA-079`、`LA-081` 已分别通过 `intake_closeout.py --visual expected`，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；`LA-078` 已通过 `intake_quality_gate.py --visual expected`；三题最终 `quality_gate=ok`，仅保留缺少用户本人错因导致的 WARN；最终 bridge snapshot records=873，assets=1253；三个 HTTP bridge open URL 均返回 200；目标 wiki/index 行均为 10 列，目标可视化 index 行均为 13 列；`manifest.json` 与 `asset_to_obsidian.json` 均可解析；Obsidian CLI 可搜索到 `MATHWIKI-LA-METHOD-017`、三张视觉详情页和三张 source summary；`git diff --check` 通过。
- rollback_action: not_run。

## 2026-07-02｜二元函数性质定义判别链正式卡修正与视觉解析闭环 GS-350/354/356/363/626
- scope: [GS-350](http://127.0.0.1:8765/open/GS-350), [GS-354](http://127.0.0.1:8765/open/GS-354), [GS-356](http://127.0.0.1:8765/open/GS-356), [GS-363](http://127.0.0.1:8765/open/GS-363), [GS-626](http://127.0.0.1:8765/open/GS-626)。
- evidence: 五题均已有正式错题卡和可视化详情；`GS-350` 与 `GS-626` 有用户明确个人错因，证据支持定义入口和可微余项识别断点；`GS-354`、`GS-356`、`GS-363` 为同源重复候选，只按题图/解析补强方法导航，不反推个人错因。
- card_updated: `GS-350` 将 `mastery_history` 从 `待评分` 规范为 `2026-07-02 AI评分 2/5`，并补 `GS-354` 作为同类定义判别代表关联；`GS-626` 将旧“掌握度 3/5”规范为 `AI评分 3/5`，关键词同步为 `掌握度AI评分3`。三张同源重复候选正式卡未新增个人错因、未启用 `method_gap`。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-050_二元函数性质定义判别链.md`，收口连续性、偏导、混合偏导、二重极限、累次极限和可微定义余项的入口判别。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md`、五个可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 安全输入包新增二元函数性质定义判别链训练项；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-wording-and-relation-correction + visual/wiki navigation enhancement；`GS-354`、`GS-356`、`GS-363` 的 `error_causes placeholder` 与 `method_gap not enabled` 警告属于正确边界。
- validation: `GS-350`、`GS-626` 已分别通过 `intake_closeout.py --visual expected`，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查，二者最终 `quality_gate=ok` 且无 ERROR/WARN；`GS-354`、`GS-356`、`GS-363` 质量门均为 `quality_gate=ok`，仅保留缺少用户本人错因导致的 WARN；最终 bridge snapshot records=873，assets=1253；五个 HTTP bridge open URL 均返回 200；目标 wiki/index 行均为 10 列，目标可视化 index 行均为 13 列；`manifest.json` 与 `asset_to_obsidian.json` 均可解析；`git diff --check` 通过。
- rollback_action: not_run；本轮未运行 scheduler，未修改回滚 JSON/JSONL。

## 2026-07-02｜多元公式模板入口链视觉解析闭环 GS-655/658
- scope: [GS-655](http://127.0.0.1:8765/open/GS-655), [GS-658](http://127.0.0.1:8765/open/GS-658)。
- evidence: 两题均已有正式错题卡、题图和解析图；证据支持“公式题先固定公式对象和模板，再开始求偏导或匹配系数”的共同入口。`GS-655` 的核心对象是向量场分量 \(P,Q,R\)，`GS-658` 的核心对象是展开增量 \(h,k\) 与二阶泰勒模板。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-046_多元公式模板入口链.md`。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-027_旋度行列式微分算子.md`、`MATHWIKI-GS-METHOD-030_二元二阶泰勒展开格式.md`、`MATHWIKI-GS-TOPIC-014_向量场与旋度错题总线.md`、`MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md`、两个可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `GS-655` 收口“旋度行列式先拆 \(P,Q,R\)，再写 \((R_y-Q_z,\ P_z-R_x,\ Q_x-P_y)\)”；`GS-658` 收口“二元二阶泰勒先写 \(h=x-x_0,\ k=y-y_0\)，再写二阶模板”。
- tutor_safe_update: 新增“多元公式模板入口链训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: visual-wiki-navigation-only / evidence-backed-refinement-only；本批不修改正式错题卡，不修改生成目录，不运行 wrongnet rebuild，不写回滚 JSON。
- validation: `manifest.json`、`asset_to_obsidian.json` JSON 合法；`wiki/index.md` 相关 7 行均为 10 列，`可视化错题详情/index.md` 相关 2 行均为 13 列；bridge snapshot 刷新成功，records=873，assets=1253；2 题质量门均为 `quality_gate=ok` 且无 warn/error；HTTP bridge `/open/GS-655`、`/open/GS-658` 均返回 200；Obsidian CLI 可读取并搜索 `MATHWIKI-GS-METHOD-046`。
- quality_note: none。
- rollback_action: not_run；本轮未运行 scheduler，未修改回滚 JSON/JSONL。

## 2026-07-02｜空间解析几何对象判别链视觉解析闭环 GS-645/646/647/651
- scope: [GS-645](http://127.0.0.1:8765/open/GS-645), [GS-646](http://127.0.0.1:8765/open/GS-646), [GS-647](http://127.0.0.1:8765/open/GS-647), [GS-651](http://127.0.0.1:8765/open/GS-651)。
- evidence: 四题均已有正式错题卡、题图和解析图；证据支持空间交线坐标面投影、参数曲线切线、空间曲线法平面、抽象曲面柱面证明的对象判别链。缺少新的用户本人作答过程，因此不改掌握度、不新增个人错因。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-045_空间解析几何对象判别链.md`。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-012_空间解析几何错题总线.md`、`MATHWIKI-GS-METHOD-016_空间交线投影消元.md`、`MATHWIKI-GS-METHOD-017_参数曲线切线点向式.md`、`MATHWIKI-GS-METHOD-018_空间曲线法平面切向量.md`、`MATHWIKI-GS-METHOD-023_曲面柱面定向量判定.md`、`wiki/index.md`、四个可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `GS-645` 收口“交线投影先联立消元，不是一开始令 z=0”；`GS-646` 收口“参数曲线切线 = 代参定点 + 求导定向 + 点向式”；`GS-647` 收口“法平面用切向量作法向量，不是切线点向式”；`GS-651` 收口“柱面证明 = 任取点求法向量 + 找公共切方向”。
- tutor_safe_update: 新增“空间解析几何对象判别链训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: visual-wiki-navigation-only / evidence-backed-refinement-only；本批不修改正式错题卡，不修改生成目录，不运行 wrongnet rebuild，不写回滚 JSON。
- validation: `manifest.json`、`asset_to_obsidian.json` JSON 合法；`wiki/index.md` 相关 10 行均为 10 列，`可视化错题详情/index.md` 相关 4 行均为 13 列；bridge snapshot 刷新成功，records=873，assets=1253；4 题质量门均为 `quality_gate=ok` 且无 warn/error；HTTP bridge `/open/GS-645`、`/open/GS-646`、`/open/GS-647`、`/open/GS-651` 均返回 200；Obsidian CLI 可读取并搜索 `MATHWIKI-GS-METHOD-045`。
- quality_note: none。
- rollback_action: not_run；本轮未运行 scheduler，未修改回滚 JSON/JSONL。

## 2026-07-02｜不定积分三角函数有理式入口四分流视觉解析闭环 GS-621/622/623/624/625/632
- scope: [GS-621](http://127.0.0.1:8765/open/GS-621), [GS-622](http://127.0.0.1:8765/open/GS-622), [GS-623](http://127.0.0.1:8765/open/GS-623), [GS-624](http://127.0.0.1:8765/open/GS-624), [GS-625](http://127.0.0.1:8765/open/GS-625), [GS-632](http://127.0.0.1:8765/open/GS-632)。
- evidence: 六题均已有正式错题卡、题图和解析图；解析证据支持“纯三角分式先补分子、\(1\pm\sin x\) 或 \(1\pm\cos x\) 先半角化、分母整体先算 \(F'\) 并拆 \(AF'+BF\)、参数型先查退化、展开后出现 \(\sec^2x\) 与 \(\tan x\) 时先拆项并检查分部抵消”这一入口分流。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流.md`。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线.md`、`MATHWIKI-GS-METHOD-039_不定积分结构化化归入口.md`、6 个视觉详情页、`wiki/index.md`、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_update: 六题视觉详情页均保留题图外显、解析折叠；新增 `MATHWIKI-GS-METHOD-042` deep wiki / 方法页链接，并同步 manifest、asset map 和 bridge 快照。
- tutor_safe_update: 新增“三角函数有理式入口四分流训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: visual/wiki/Tutor-only；正式卡本身已有答案、wrong_point、method_gap，本轮未修改正式错题卡。
- validation: `manifest.json`、`asset_to_obsidian.json` 与 bridge `records.json` JSON 合法；bridge snapshot 刷新成功，records=873，assets=1253；6 题质量门均为 `quality_gate=ok`；Obsidian CLI 可精确读取新方法页，搜索可召回 6 个视觉详情页、专题总线、Tutor 安全输入包、方法页和 wiki index；HTTP bridge `/open/GS-621?status=1` 与 `/open/GS-632?status=1` 返回 200。
- quality_note: `GS-625` 质量门保留 `method_gap.expected_first_action may not be an executable first-action sentence` 警告，属于旧卡已有句式提醒；本轮不为消警告硬改用户个人 method_gap。
- rollback_action: not_run；本轮未运行 scheduler，未修改回滚 JSON/JSONL。

## 2026-07-02｜高数极限主量提出与公共尺度视觉解析闭环 GS-005/027/436/438/440/443
- scope: [GS-005](http://127.0.0.1:8765/open/GS-005), [GS-027](http://127.0.0.1:8765/open/GS-027), [GS-436](http://127.0.0.1:8765/open/GS-436), [GS-438](http://127.0.0.1:8765/open/GS-438), [GS-440](http://127.0.0.1:8765/open/GS-440), [GS-443](http://127.0.0.1:8765/open/GS-443)。
- evidence: 六题均已有正式错题卡和视觉详情；GS-005、GS-027 有题图与解析图，GS-436、GS-438、GS-440、GS-443 有题图与折叠解析文字。解析证据支持“非零因子先算、外部指数尺度提出、底数趋非 \(1\) 常数先提常数幂、同名函数差值先用中值定理、变上限平均型先转端点函数、有限非零极限先转零点结构”这一公共方法线。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度.md`。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md`、`MATHWIKI-GS-METHOD-006_先判型总流程.md`、`MATHWIKI-GS-METHOD-007_条件转化总流程.md`、`MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点.md`、`MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点.md`、`MATHWIKI-GS-METHOD-012_等价无穷小使用条件.md`、6 个视觉详情页、`wiki/index.md`、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- card_update: `GS-005` 根据解析图补正式答案 \(a=\frac16,\ b=3\)，并补 `无穷小阶数比较` 与 `主导项比较`；未改用户原始错因、掌握度或回滚字段。
- tutor_safe_update: 新增“极限主量提出与公共尺度训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；本批除 GS-005 的明确答案补全外，只根据题图/解析图补强可确认的学习入口，不从解析图反推新的个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1828，medium=683，weak_audit=497；LLM Wiki coverage 刷新成功，source summaries=770，compiled=744，knowledge_clusters=350，method_clusters=930，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`manifest.json`、`asset_to_obsidian.json` JSON 合法；6 题质量门均为 `quality_gate=ok`；Obsidian CLI 可精确读取新方法页，全文搜索可召回 6 个视觉详情页、极限总线和 Tutor 安全输入包；`wrongnet.py related GS-440` 可召回 `GS-438` 强关联，`wrongnet.py knowledge 极限与连续` 可召回 `GS-005`。
- quality_note: 质量门若保留 `method_gap.expected_first_action may not be an executable first-action sentence`，属于旧卡已有句式提示；本轮未为了消除警告而重写用户个人 method_gap。
- rollback_action: not_run；本轮未运行 scheduler，未修改回滚 JSON/JSONL。

## 2026-07-02｜线代方程组包含、张成空间交、向量组表示视觉解析闭环 LA-091/092/093/097/100
- scope: [LA-091](http://127.0.0.1:8765/open/LA-091), [LA-092](http://127.0.0.1:8765/open/LA-092), [LA-093](http://127.0.0.1:8765/open/LA-093), [LA-097](http://127.0.0.1:8765/open/LA-097), [LA-100](http://127.0.0.1:8765/open/LA-100)。
- evidence: 五题均已有正式错题卡、题图和解析图；解析图支持非齐次方程组解集包含的增广矩阵秩判定、两组向量张成空间交的齐次方程组入口、三向量整体相关且两两无关的参数排除、表示关系转转置核包含、向量组等价后的表示式求解。
- wiki_updated: 扩展 `MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示.md`、`MATHWIKI-LA-METHOD-016_线性方程组同解与公共解判定.md`；更新 `MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-091` 补入非齐次方程组解集包含要拼接增广矩阵并看秩；`LA-092` 补入同一向量由两组向量线性表示时要先写齐次方程组；`LA-093` 补入整体相关给候选参数后必须逐对回代排除两两相关；`LA-097` 补入由向量组表示关系写成矩阵关系，再转置判断核空间包含；`LA-100` 补入向量组等价先判参数，再在等价条件下求表示式。
- tutor_safe_update: 新增五个安全训练项，分别覆盖非齐次方程组解集包含、张成空间交、整体相关与两两无关、表示关系转置核包含、向量组等价与表示式；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1827，medium=684，weak_audit=497；LLM Wiki coverage 刷新成功，source summaries=770，compiled=744，knowledge_clusters=350，method_clusters=930，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`manifest.json`、`asset_to_obsidian.json` 与 bridge `records.json` JSON 合法；五题质量门均为 `quality_gate=ok`；bridge health 返回 200，`/open/LA-100?status=1` 返回正式打开页；bridge records 中五题均有 `linked_wrongnet` 正式详情页；Obsidian CLI 已确认 `kaoyan-math` vault 可用，可精确读取 `VIS-LA-100`，并可搜索到本批正式卡和视觉详情；`wrongnet.py related` 与 `wrongnet.py knowledge 向量组线性相关/线性方程组` 可召回本批题。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run；本轮未运行 scheduler，未修改回滚 JSON/JSONL。

## 2026-07-02｜线代满秩消去、秩不等式、伴随零空间与向量组等价视觉解析闭环 LA-067/069/071/072/074/075
- scope: [LA-067](http://127.0.0.1:8765/open/LA-067), [LA-069](http://127.0.0.1:8765/open/LA-069), [LA-071](http://127.0.0.1:8765/open/LA-071), [LA-072](http://127.0.0.1:8765/open/LA-072), [LA-074](http://127.0.0.1:8765/open/LA-074), [LA-075](http://127.0.0.1:8765/open/LA-075)。
- evidence: 六题均已有正式错题卡、题图和解析图；解析图支持满行秩右消、满列秩保核、秩不等式上下界夹逼、Frobenius 秩不等式保秩传递、伴随矩阵零空间列向量基、参数向量组等价判定。
- wiki_updated: 扩展 `MATHWIKI-LA-METHOD-013_矩阵秩约束与分块秩比较.md`、`MATHWIKI-LA-METHOD-010_伴随矩阵与反对称结构.md`、`MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示.md`；更新 `MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-067` 补入 \(C\) 行满秩时右消 \(AC=BC\Rightarrow A=B\)；`LA-069` 补入 \(A\) 满列秩时 \(A(Bx)=0\Rightarrow Bx=0\) 的保核入口；`LA-071` 补入乘积为零给上界、可逆矩阵减低秩矩阵给下界的夹逼链；`LA-072` 补入 Frobenius 秩不等式和乘积秩不增的上下界闭合；`LA-074` 补入 \(A^*A=|A|E\) 下 \(A\) 的列向量落入 \(A^*\) 零空间，并用余子式非零选独立列；`LA-075` 补入向量组等价转张成空间相同，特殊参数必须回代检查。
- tutor_safe_update: 新增“满行秩右消训练项”“满列秩保核训练项”“秩不等式上下界夹逼训练项”“Frobenius 秩不等式保秩传递训练项”“伴随矩阵零空间列向量基训练项”“参数向量组等价训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1813，medium=690，weak_audit=497；LLM Wiki coverage 刷新成功，source summaries=770，compiled=741，knowledge_clusters=350，method_clusters=927，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`manifest.json`、`asset_to_obsidian.json` 与 bridge `records.json` JSON 合法；六题质量门均为 `quality_gate=ok`，HTTP bridge `/open/{ID}` 均返回 200；Obsidian CLI 已确认 `kaoyan-math` vault 可用，可精确读取 `VIS-LA-067`，并可搜索到 `LA-075` 的正式卡、视觉详情和索引；`wrongnet.py related` 已确认 LA-067 与 LA-068/069/071/072 强关联、LA-074 与伴随矩阵和方程组题强关联、LA-075 与 LA-090/099 强关联，`wrongnet.py knowledge 矩阵秩/向量组线性相关/行列式` 可召回本批对应题。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run；本轮未运行 scheduler，未修改回滚 JSON/JSONL。

## 2026-07-02｜线代相似理论正交、转置边界与伴随矩阵求幂视觉解析闭环 LA-112/114/115/119
- scope: [LA-112](http://127.0.0.1:8765/open/LA-112), [LA-114](http://127.0.0.1:8765/open/LA-114), [LA-115](http://127.0.0.1:8765/open/LA-115), [LA-119](http://127.0.0.1:8765/open/LA-119)。
- evidence: 四题均已有正式错题卡、题图和解析图；解析图支持实对称与正交特征向量组充要关系、相似关系对转置/矩阵函数/逆/伴随组合的传递边界、\(A^*\sim B\) 下求参数与换基矩阵再求 \(A^{99}\)、正交矩阵 \(a_{11}=1\) 的单位向量约束。
- wiki_updated: 扩展 `MATHWIKI-LA-METHOD-005_相似对角化判定与特征向量换基.md`；更新 `MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包；补齐 `VIS-LA-119` 的总索引行，并同步 `VIS-LA-112/114/115/119` 标题与日期。
- update: `LA-112` 补入 \(Q^{-1}AQ=\Lambda\)、\(Q^{-1}=Q^{\mathsf T}\)、\(A=Q\Lambda Q^{\mathsf T}\) 的反向推导入口；`LA-114` 补入同一相似变换矩阵传递检查，强调 \(A^{\mathsf T}\sim B^{\mathsf T}\) 不推出 \(A+A^{\mathsf T}\sim B+B^{\mathsf T}\)；`LA-115` 补入 \(A^*\sim B\) 下特征值求参数、特征向量矩阵传递与 \(A^{99}\) 求法；`LA-119` 补入正交矩阵首元为 \(1\) 时同一行/列其余元素为 \(0\) 的约束。
- bridge_fix: 更新 `refresh_obsidian_bridge_snapshot.py`，使 `linked_wrongnet` 正式详情页在快照中优先于 `merged_into_wrongnet` 旧候选来源页；刷新后 `/open/LA-112`、`/open/LA-114`、`/open/LA-115`、`/open/LA-119` 首条命中均为对应 `VIS-LA-*` 正式详情页。
- tutor_safe_update: 新增“实对称与正交特征向量训练项”“相似关系传递边界训练项”“伴随矩阵相似传递与高次幂训练项”“正交矩阵首元约束训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1756，medium=714，weak_audit=495；LLM Wiki coverage 刷新成功，source summaries=770，compiled=723，knowledge_clusters=351，method_clusters=904，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；四题正式卡、视觉详情页、`MATHWIKI-LA-METHOD-005`、`MATHWIKI-LA-TOPIC-001`、`MATHWIKI-LA-TOPIC-004` 与 Tutor 安全输入包 YAML 均合法，`manifest.json`、`asset_to_obsidian.json` 和 bridge `records.json` JSON 合法；四题质量门均为 `quality_gate=ok`，HTTP bridge `/open/{ID}` 均返回 200；Obsidian CLI 已确认 `kaoyan-math` vault 可用，并可精确读取 `VIS-LA-112` 与 `MATHWIKI-LA-METHOD-005`；`wrongnet.py related` 已确认四题与 LA-109/110/112/114/115/119 形成相似理论强关联，`wrongnet.py knowledge 相似矩阵/实对称矩阵/逆矩阵` 可召回本批对应题。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代伴随传递、矩阵幂降维与秩空间视觉解析闭环 LA-055/056/057/058
- scope: [LA-055](http://127.0.0.1:8765/open/LA-055), [LA-056](http://127.0.0.1:8765/open/LA-056), [LA-057](http://127.0.0.1:8765/open/LA-057), [LA-058](http://127.0.0.1:8765/open/LA-058)。
- evidence: 四题均已有正式错题卡、题图和解析图；解析图支持交换列传到伴随矩阵时的乘积反序与负交换矩阵、相似对角化求 \(A^{99}\)、低秩分解 \(A^k=B(CB)^{k-1}C\)、横拼 \([A,AB]\) 的列空间包含判断。
- wiki_created: 新建 `MATHWIKI-LA-METHOD-011_矩阵幂降维与秩空间判断.md`。
- wiki_updated: 更新 `MATHWIKI-LA-METHOD-010_伴随矩阵与反对称结构.md`、`MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包；补齐 `VIS-LA-055`、`VIS-LA-056`、`VIS-LA-057` 的总索引行，并同步 `VIS-LA-058` 标题与日期。
- update: `LA-055` 补入 \(B=AE_{12}\)、\((AB)^*=B^*A^*\)、\(E_{12}^*=-E_{12}\) 的列交换传递入口；`LA-056` 补入 \(A^n=PB^nP^{-1}\) 的高次幂入口；`LA-057` 补入由列向量关系求 \(C\) 与 \(A^{10}=B(CB)^9C\) 的降维入口；`LA-058` 补入按列空间判断 \(r([A,AB])=r(A)\) 的恒等式入口。
- tutor_safe_update: 新增“矩阵幂降维与秩空间判断训练项”和“伴随矩阵初等列交换训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1754，medium=693，weak_audit=496；LLM Wiki coverage 刷新成功，source summaries=770，compiled=727，knowledge_clusters=351，method_clusters=877，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；四题正式卡、视觉详情页、`MATHWIKI-LA-METHOD-010`、`MATHWIKI-LA-METHOD-011` 与 `MATHWIKI-LA-TOPIC-001` YAML 均合法，`manifest.json` 与 `asset_to_obsidian.json` JSON 合法，视觉详情均含题图和默认折叠解析；四题质量门均为 `quality_gate=ok`，HTTP bridge 状态页均返回对应标题与 Obsidian URL；Obsidian CLI 已确认 `kaoyan-math` vault 可用，并可精确读取 `VIS-LA-055` 与 `MATHWIKI-LA-METHOD-011`；`wrongnet.py related` 已确认 `LA-055` 与 `LA-049/LA-050` 强关联、`LA-056` 与 `LA-057` 强关联、`LA-057` 与 `LA-058` 强关联，`wrongnet.py knowledge 矩阵运算/行列式/矩阵秩/相似矩阵` 可召回本批对应题。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代伴随矩阵与反对称结构视觉解析闭环 LA-049/050
- scope: [LA-049](http://127.0.0.1:8765/open/LA-049), [LA-050](http://127.0.0.1:8765/open/LA-050)。
- evidence: 两题均已有正式错题卡、题图和解析图；解析图支持 \(a_{ij}=-A_{ij}\Rightarrow A^{\mathsf T}=-A^*\) 后用行列式与秩排除 \(|A|=0\)，以及 \(a_{ij}=-a_{ji}\Rightarrow A^{\mathsf T}=-A\) 后把反对称性质传递给 \(A^*\)，从而 \(x^{\mathsf T}A^*x=0\)。
- wiki_updated: 新建 `MATHWIKI-LA-METHOD-010_伴随矩阵与反对称结构.md`；更新 `MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-049` 补入元素与代数余子式关系翻译成伴随矩阵等式、三阶行列式候选值和伴随矩阵秩排除法；`LA-050` 补入反对称矩阵阶数判断、伴随矩阵反对称性和反对称二次型为零入口。
- tutor_safe_update: 新增“伴随矩阵与反对称结构训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1748，medium=681，weak_audit=496；LLM Wiki coverage 刷新成功，source summaries=770，compiled=727，knowledge_clusters=351，method_clusters=868，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`LA-049`、`LA-050` 两题正式卡、视觉详情页和 `MATHWIKI-LA-METHOD-010` YAML 均合法，`manifest.json` 与 `asset_to_obsidian.json` JSON 合法且两题视觉记录已更新到 2026-07-02；两题质量门均为 `quality_gate=ok`，HTTP bridge 状态页均返回对应标题与 Obsidian URL；Obsidian CLI 已确认 `kaoyan-math` vault 可用，并可精确读取 `VIS-LA-049` 与 `MATHWIKI-LA-METHOD-010`；`wrongnet.py related` 已确认两题互为强关联，`wrongnet.py knowledge 行列式` 可召回两题。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代逆矩阵结构化求法视觉解析闭环 LA-052/053/054
- scope: [LA-052](http://127.0.0.1:8765/open/LA-052), [LA-053](http://127.0.0.1:8765/open/LA-053), [LA-054](http://127.0.0.1:8765/open/LA-054)。
- evidence: 三题均已有正式错题卡、题图和解析图；解析图支持全一矩阵 \(J-E\) 求逆、矩阵多项式除法求 \((A-E)^{-1}\)、幂零矩阵 \(A^3=O\) 判 \(E\pm A\) 可逆等入口补强。
- wiki_updated: 新建 `MATHWIKI-LA-METHOD-009_逆矩阵结构化求法.md`；更新 `MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-052` 补入 \(A=J-E\)、\(J^2=nJ\) 与 \(A^{-1}=\frac{1}{n-1}J-E\)；`LA-053` 补入用 \(A-E\) 除矩阵多项式并整理成逆矩阵定义；`LA-054` 补入幂零矩阵有限级数求逆和特征值判可逆入口。
- tutor_safe_update: 新增“逆矩阵结构化求法训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1747，medium=674，weak_audit=496；LLM Wiki coverage 刷新成功，source summaries=770，compiled=727，knowledge_clusters=351，method_clusters=862，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`LA-052`、`LA-053`、`LA-054` 三题正式卡、视觉详情页、`MATHWIKI-LA-METHOD-009` 与 `MATHWIKI-LA-TOPIC-001` YAML 均合法，`manifest.json` 与 `asset_to_obsidian.json` JSON 合法且三题视觉记录已更新到 2026-07-02；三题质量门均为 `quality_gate=ok`，HTTP bridge 状态页均返回对应标题与 Obsidian URL；Obsidian CLI 已确认 `kaoyan-math` vault 可用，并可精确读取 `VIS-LA-052` 与 `MATHWIKI-LA-METHOD-009`；`wrongnet.py related` 已确认三题互为强关联，`wrongnet.py knowledge 逆矩阵` 可召回三题。
- quality_note: 若质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代矩阵运算结构识别视觉解析闭环 LA-045/046/048
- scope: [LA-045](http://127.0.0.1:8765/open/LA-045), [LA-046](http://127.0.0.1:8765/open/LA-046), [LA-048](http://127.0.0.1:8765/open/LA-048)。
- evidence: 三题均已有正式错题卡、题图和解析图；解析图支持上三角单位阵加幂零矩阵的高次幂截断、初等矩阵左乘行变换与右乘列变换、实对称矩阵多项式方程转特征值方程等入口补强。
- wiki_updated: 新建 `MATHWIKI-LA-METHOD-008_矩阵运算结构识别.md`；更新 `MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-045` 补入 \(A=E+N\)、\(N^3=O\) 与二项式截断入口；`LA-046` 补入左乘动行、右乘动列和交换矩阵负幂周期入口；`LA-048` 补入实对称矩阵正交对角化后解特征值方程入口。
- tutor_safe_update: 新增“矩阵运算结构识别训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1744，medium=674，weak_audit=496；LLM Wiki coverage 刷新成功，source summaries=770，compiled=727，knowledge_clusters=350，method_clusters=853，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`LA-045`、`LA-046`、`LA-048` 三题正式卡、视觉详情页和 `MATHWIKI-LA-METHOD-008` YAML 均合法，`manifest.json` 与 `asset_to_obsidian.json` JSON 合法且三题视觉记录已更新到 2026-07-02；三题质量门均为 `quality_gate=ok`，HTTP bridge 状态页均返回对应标题与 Obsidian URL；Obsidian CLI 已确认 `kaoyan-math` vault 可用，并可精确读取 `VIS-LA-045` 与 `MATHWIKI-LA-METHOD-008`，全文搜索因 vault 较大超时，已用精确路径读取和 bridge 记录替代验证。
- quality_note: 质量门若保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代二次型合同、相似与正定平方根视觉解析闭环 LA-040-044
- scope: [LA-040](http://127.0.0.1:8765/open/LA-040), [LA-041](http://127.0.0.1:8765/open/LA-041), [LA-042](http://127.0.0.1:8765/open/LA-042), [LA-043](http://127.0.0.1:8765/open/LA-043), [LA-044](http://127.0.0.1:8765/open/LA-044)。
- evidence: 五题均已有正式错题卡、题图和解析图；解析图支持合同与相似判定、可逆合同变换与正交变换辨析、行列式展开后二次型正定判定、\(D^{\mathrm T}D=A\) 配方法读矩阵、实对称矩阵正交对角化后构造正定平方根等入口补强。
- wiki_updated: 新建 `MATHWIKI-LA-METHOD-007_二次型合同相似与正定平方根.md`；更新 `MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-040` 补入合同看惯性指数、相似看特征值的双线判定；`LA-041` 补入可逆变换与正交变换的强弱差异；`LA-042` 补入 \(|xA+yB|\) 先展开成二次型矩阵；`LA-043` 补入 \(D^{\mathrm T}D=A\) 先配 \(x^{\mathrm T}Ax\) 并按行读 \(D\)；`LA-044` 补入正交对角化后对特征值开方构造正定平方根。
- tutor_safe_update: 新增“二次型合同、相似与正定平方根训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1740，medium=672，weak_audit=496；LLM Wiki coverage 刷新成功，source summaries=770，compiled=727，knowledge_clusters=350，method_clusters=843，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`LA-040` 至 `LA-044` 五题 YAML 与视觉 JSON 均合法，五题质量门均为 `quality_gate=ok`，bridge records 均为唯一正式命中并指向对应线性代数详情页，HTTP bridge 状态页均返回 `ok=true` 并向 Obsidian 发送打开请求。
- quality_note: 质量门若保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代二次型合同矩阵视觉解析闭环 LA-037/038
- scope: [LA-037](http://127.0.0.1:8765/open/LA-037), [LA-038](http://127.0.0.1:8765/open/LA-038)。
- evidence: 两题均已有正式错题卡、题图和解析图；解析图支持二次型配方法构造合同矩阵、两个合同二次型化同一规范形、变量方向反解和矩阵合成方向检查。
- wiki_updated: 扩展 `MATHWIKI-LA-METHOD-006_二次型配方法与正定判定.md` 为“二次型配方法、正定与合同矩阵”；更新 `MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-037` 补入 \(C^{\mathrm T}AC=\Lambda\) 的变量方向反解入口，答案矩阵为 \(\begin{pmatrix}\sqrt2&0&0\\-\sqrt2&\sqrt3&0\\0&-\sqrt3&1\end{pmatrix}\)；`LA-038` 补入 \(A=D^{\mathrm T}BD\) 的双配方合成入口，答案矩阵为 \(\begin{pmatrix}\frac1{\sqrt2}&\frac1{\sqrt2}-\frac3{2\sqrt5}\\0&\frac2{\sqrt5}\end{pmatrix}\)。
- tutor_safe_update: 扩展“二次型配方法、正定与合同矩阵训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `intake_closeout.py` 已完成 phase 1/2 后在并行验证阶段因 Obsidian 搜索等待被人工中断；已完成部分显示 `wrongnet.py rebuild` 成功，cards=770，strong=1753，medium=656，weak_audit=496；LLM Wiki coverage 刷新成功，source summaries=770，compiled=722，knowledge_clusters=349，method_clusters=837，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253。随后手动验证 `manifest.json`、`asset_to_obsidian.json` 和 bridge records JSON 均合法，`LA-037` 与 `LA-038` 质量门均为 `quality_gate=ok`，bridge 状态页均确认打开到对应线性代数正式详情页。
- quality_note: 质量门若保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代二次型配方法与正定判定视觉解析闭环 LA-030/035
- scope: [LA-030](http://127.0.0.1:8765/open/LA-030), [LA-035](http://127.0.0.1:8765/open/LA-035)。
- evidence: 两题均已有正式错题卡、题图和解析图；解析图支持二次型配方法求正惯性指数、平方和二次型正定参数判定、公共零点和线性形式矩阵可逆性等复做入口补强。
- wiki_updated: 新建 `MATHWIKI-LA-METHOD-006_二次型配方法与正定判定.md`；更新 `MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-030` 补入答案 C、可逆线性变换配成规范形后数正平方项的入口；`LA-035` 补入答案 \(a\ne -1\)、平方和正定需检查公共零点只有原点的入口。
- tutor_safe_update: 新增“二次型配方法与正定训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1759，medium=649，weak_audit=496；LLM Wiki coverage 刷新成功，source summaries=770，compiled=720，knowledge_clusters=349，method_clusters=836，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`LA-030` 与 `LA-035` 质量门均为 `quality_gate=ok`，bridge 状态页均确认打开到对应线性代数正式详情页。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告；这是本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代相似对角化判定与换基视觉解析闭环 LA-109/110
- scope: [LA-109](http://127.0.0.1:8765/open/LA-109), [LA-110](http://127.0.0.1:8765/open/LA-110)。
- evidence: 两题均已有正式错题卡、题图和解析图；题图与解析图支持相似对角化中特征向量矩阵换基、同一特征空间内线性组合、能否相似于对角矩阵、重特征值几何重数判定等复做入口补强。
- wiki_updated: 新建 `MATHWIKI-LA-METHOD-005_相似对角化判定与特征向量换基.md`；更新 `MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-109` 补入 \(P^{-1}AP=D\) 后更换特征向量矩阵时逐列匹配特征值的入口，答案为 B；`LA-110` 补入先找重特征值、再比较几何重数与代数重数的入口，答案为 A。
- tutor_safe_update: 新增“相似矩阵与相似对角化”训练项；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1760，medium=646，weak_audit=496；LLM Wiki coverage 刷新成功，source summaries=770，compiled=720，knowledge_clusters=349，method_clusters=831，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`LA-109` 与 `LA-110` 质量门均为 `quality_gate=ok`，bridge 状态页均确认打开到对应线性代数正式详情页。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告；这是本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜多元函数极值与闭区域最值视觉解析补强 GS-390-396

- scope: [GS-390](http://127.0.0.1:8765/open/GS-390), [GS-391](http://127.0.0.1:8765/open/GS-391), [GS-392](http://127.0.0.1:8765/open/GS-392), [GS-393](http://127.0.0.1:8765/open/GS-393), [GS-394](http://127.0.0.1:8765/open/GS-394), [GS-395](http://127.0.0.1:8765/open/GS-395), [GS-396](http://127.0.0.1:8765/open/GS-396)。
- evidence: 7 题已有 OO3 题图、解析图或解析文字，主题集中在无条件极值 Hessian 判别、闭区域最值、条件极值、隐函数消元、二次型约束和实际问题建模。
- update: 7 张正式卡补入稳定 `lecture_refs`、轻量题目摘要、答案、知识点、方法入口、陷阱与复做提醒；7 个可视化详情页补齐 `题目定位`、`正确第一步`、`核心方法`、`易错触发`、`方法页` 与 `复做提醒`，并清理 GS-393、GS-396 中不相关的一元中值定理、数列极限标签。
- wiki_updated: 新建并登记 `MATHWIKI-GS-METHOD-033_多元函数条件与闭区域最值.md`；更新 `MATHWIKI-GS-METHOD-032_多元函数极值驻点判别.md`、`MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`manifest.json` 与 `数学LLMWiki安全输入包.md`。
- card_decision: evidence-backed-refinement-only；只写题图/解析可确认内容，不从解析反推用户本人错因，不启用 `method_gap`，掌握度标记为待评分。
- wrongnet_rebuild: needed_after_formal_card_update。
- rollback_action: not_run。

## 2026-07-01｜多元函数极值驻点判别视觉解析补强 GS-386-389

- scope: [GS-386](http://127.0.0.1:8765/open/GS-386), [GS-387](http://127.0.0.1:8765/open/GS-387), [GS-388](http://127.0.0.1:8765/open/GS-388), [GS-389](http://127.0.0.1:8765/open/GS-389)。
- evidence: 4 题均已有题图与解析图，主题集中在无条件多元函数极值、驻点求解、Hessian 判别、\(D=AC-B^2=0\) 时的路径验证，以及“所有直线路径极小不能推出二维邻域极小”的定义边界。
- update: 4 张正式卡补入稳定 `lecture_refs`、轻量题目摘要、标准答案、知识点、方法入口、陷阱与复做提醒；4 个可视化详情页补齐 `题目定位`、`正确第一步`、`核心方法`、`易错触发`、`方法页` 与 `复做提醒`。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-032_多元函数极值驻点判别.md`；更新 `MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md` 与 `数学LLMWiki安全输入包.md`。
- card_decision: evidence-backed-refinement-only；只写题图/解析图可确认内容，不从解析图反推用户本人错因，不启用 `method_gap`，不修改掌握度或回滚复习。
- wrongnet_rebuild: needed_after_formal_card_update。
- rollback_action: not_run。

## 2026-07-01 GS-656-138717-directional-derivative-existence-trap-intake

- input: 用户提供 `138717 / (224-1)` 题图与解析图；前序讲解后确认自己理解“方向导数存在性”和“不连续”的判断，并要求正式入库。
- source_refs: `/Users/xiazhibin/Library/Application Support/PixPin/Temp/PixPin_2026-07-01_15-39-17.png`；`/var/folders/5k/93syh_hn3rq0wyyh6m2bxlq80000gn/T/codex-clipboard-60cf0147-aa51-4ad5-ac6b-33ac4923cbc0.png`
- formal_card_updated: 新建 `错题知识网络/错题卡/GS-656_138717方向导数存在性陷阱.md`，答案 B；具体错点为没有区分“方向导数中的固定方向射线极限”和“连续性中的任意路径极限”，不清楚为什么所有方向导数存在但函数仍可不连续。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-028_方向导数存在性陷阱.md`；更新 `MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md` 和 Tutor 安全输入包中的方向导数存在性陷阱训练项。
- visual_quality_update: 新建 `VIS-GS-656`，题图与解析图复制到 `错题知识网络/assets/visual_wrong_questions/GS-656/`；更新 visual index、manifest、asset map 和 Obsidian open link。
- wrongnet_rebuild: closeout ok；`cards=768`，`records=871`，`assets=1249`，相关题检查命中 `GS-350`、`GS-652`、`GS-653`、`GS-654`、`GS-626` 等。
- rollback_action: not_run；未修改回滚复习 JSON；正式卡内写入 `AI评分 3/5`。
- tutor_boundary: 只补高层训练项“方向导数存在性陷阱”，不复制完整题干、长解析或截图到 Tutor。

## 2026-07-01 GS-655-19571-curl-determinant-operator-intake

- input: 用户提供 `19571 / (525-13)` 题图与解析图；前序讲解后明确自己误以为旋度行列式第二行表示“对整个向量场分别求偏导”，随后要求正式入库。
- source_refs: `/Users/xiazhibin/Library/Application Support/PixPin/Temp/PixPin_2026-07-01_15-25-02.png`；`/var/folders/5k/93syh_hn3rq0wyyh6m2bxlq80000gn/T/codex-clipboard-fe6494e1-1a34-4f06-a4b1-9b809ccafdf4.png`
- formal_card_updated: 新建 `错题知识网络/错题卡/GS-655_19571旋度行列式微分算子.md`，答案 \(i-k\)；具体错点为把旋度行列式的微分算子理解成对整个向量场整体求偏导，没有先拆 \(P,Q,R\) 再按 \((R_y-Q_z,\ P_z-R_x,\ Q_x-P_y)\) 计算。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-027_旋度行列式微分算子.md`、`MATHWIKI-GS-TOPIC-014_向量场与旋度错题总线.md`；更新 `wiki/index.md`、`知识点库.md` 和 Tutor 安全输入包中的旋度训练项。
- visual_quality_update: 新建 `VIS-GS-655`，题图与解析图复制到 `错题知识网络/assets/visual_wrong_questions/GS-655/`；更新 visual index、manifest、asset map 和 Obsidian open link。
- wrongnet_rebuild: closeout ok；`cards=767`，`records=870`，`assets=1247`，相关题检查命中 `GS-465`、`GS-627`、`GS-629` 等。
- rollback_action: not_run；未修改回滚复习 JSON；正式卡内写入 `AI评分 3/5`。
- tutor_boundary: 只补高层训练项“旋度行列式微分算子”，不复制完整题干、长解析或截图到 Tutor。

## 2026-07-01 GS-654-89961-directional-derivative-infer-gradient-intake

- input: 用户提供 `89961 / (524-12)` 题图、答案解析图和通用推导截图；前序讲解后明确要求正式入库。用户错点是能理解方向导数、最大方向导数的局部关系，但不清楚“两个不同方向导数如何反推出梯度”的整体流程。
- source_refs: `/Users/xiazhibin/Library/Application Support/PixPin/Temp/PixPin_2026-07-01_15-12-51.png`；`/var/folders/5k/93syh_hn3rq0wyyh6m2bxlq80000gn/T/codex-clipboard-6ccf3dd3-1063-4f59-9266-df3dfd8aed29.png`；`/var/folders/5k/93syh_hn3rq0wyyh6m2bxlq80000gn/T/codex-clipboard-924cc266-ef00-43a7-8c37-ead68b2f0677.png`
- formal_card_updated: 新建 `错题知识网络/错题卡/GS-654_89961方向导数反推梯度.md`，答案 \(\sqrt{10}\)；具体错点为没有先设 \(\nabla f(P_0)=(a,b)\)，用两个单位方向向量点乘列方程反推梯度，再取梯度模。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-026_方向导数反推梯度.md`；更新 `MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md` 和 Tutor 安全输入包中的方向导数反推梯度训练项。
- visual_quality_update: 新建 `VIS-GS-654`，题图复制为 `question_01.png`，答案解析和通用推导截图复制为 `solution_01.png`、`solution_02.png`；更新 visual index、manifest、asset map 和 Obsidian open link。
- wrongnet_rebuild: needed_after_card_update
- rollback_action: not_run；未修改回滚复习 JSON；正式卡内写入 `AI评分 3/5`。
- tutor_boundary: 只补高层训练项“方向导数反推梯度”，不复制完整题干、长解析或截图到 Tutor。

## 2026-07-01 GS-653-102591-max-directional-derivative-intake

- input: 用户提供 `102591 / (524-11)` 题图与解析图，先要求讲解“思路怎么产生”，随后明确入库；追问重点为为什么 \(z=f(x,y)\) 只对 \(x,y\) 求偏导、为什么不能直接移项成三元函数梯度、方向导数维数如何判断。
- source_refs: `/Users/xiazhibin/Library/Application Support/PixPin/Temp/PixPin_2026-07-01_14-54-09.png`；`/var/folders/5k/93syh_hn3rq0wyyh6m2bxlq80000gn/T/codex-clipboard-9479edf0-9ddd-4a2f-837f-e530869b5cc6.png`
- formal_card_updated: 新建 `错题知识网络/错题卡/GS-653_102591最大方向导数梯度模.md`，答案 A；具体错点为没有把“方向导数最大、最大值为 10”翻译成“梯度与给定方向同向且梯度模为 10”，并混淆 \(z=f(x,y)\) 的二维梯度与 \(F(x,y,z)=0\) 的三维法向量。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-025_最大方向导数梯度模.md`；更新 `MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md`、`知识点库.md` 和 Tutor 安全输入包中的最大方向导数训练项。
- visual_quality_update: 新建 `VIS-GS-653`，题图与解析图复制到 `错题知识网络/assets/visual_wrong_questions/GS-653/`；更新 visual index、manifest、asset map 和 Obsidian open link。
- wrongnet_rebuild: closeout ok；`cards=765`，`records=868`，`assets=1242`，相关题检查命中 `GS-652`、`GS-626`、`GS-629` 等。
- rollback_action: not_run；未修改回滚复习 JSON；正式卡内写入 `AI评分 2/5`。
- tutor_boundary: 只补高层训练项“最大方向导数梯度模”，不复制完整题干、长解析或截图到 Tutor。

## 2026-07-01 GS-652-78821-directional-derivative-intake

- input: 用户提供 `78821 / (523-10)` 题图与解析图，指出方向导数题没有入口，不理解梯度实际计算、\(\frac13(1,2,2)\) 的单位向量来源，以及为什么用梯度与单位方向向量点乘。
- source_refs: `/Users/xiazhibin/Library/Application Support/PixPin/Temp/PixPin_2026-07-01_14-36-16.png`；`/var/folders/5k/93syh_hn3rq0wyyh6m2bxlq80000gn/T/codex-clipboard-a61b2aa5-0cc6-4dd7-b7c2-1e73c4b43c8f.png`
- formal_card_updated: 新建 `错题知识网络/错题卡/GS-652_78821方向导数梯度点乘.md`，答案 D；具体错点为看到“沿向量求方向导数”时没有先写 \(D_{\mathbf e}f(P_0)=\nabla f(P_0)\cdot\mathbf e\)，且不知道题目给的方向向量需要先单位化。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-024_方向导数梯度点乘.md`；更新 `MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md`、`知识点库.md` 和 Tutor 安全输入包中的方向导数训练项。
- visual_quality_update: 新建 `VIS-GS-652`，题图与解析图复制到 `错题知识网络/assets/visual_wrong_questions/GS-652/`；更新 visual index、manifest、asset map 和 Obsidian open link。
- wrongnet_rebuild: closeout ok；`records=867`，`assets=1240`，相关题检查命中 `GS-626`、`GS-629`、`GS-651` 等。
- rollback_action: not_run；未修改回滚复习 JSON；按项目现行规则与用户最新确认，正式卡内保留 `AI评分 2/5`。
- tutor_boundary: 只补高层训练项“方向导数梯度点乘”，不复制完整题干、长解析或截图到 Tutor。

## 2026-07-01 visual_detail_obsidian_markdown_rendering_cleanup

- input: 用户指出 `GS-358 / 强化例题13.12` 可视化详情页的折叠解析仍存在 Obsidian 中公式不渲染、解析源码外露、可读性差的问题，要求按 Obsidian Markdown skill 的格式清理题库内同类问题。
- evidence: 以 `错题知识网络/可视化错题详情/高等数学/GS-358_强化例题13.12.md` 为样本，扫描 `错题知识网络/可视化错题详情/**/*.md` 共 870 个详情页；检查项包括 `\[...\]` 裸露公式、未闭合 `$$`、`\\[2mm]` / `\\[6pt]` 被拆断、行尾孤立反斜杠、折叠解析超长单行。
- visual_quality_update: 将折叠解析中的裸公式统一收进 Obsidian 稳定渲染的 `$$` 公式块；修复 cases / aligned / vmatrix 中被拆坏的行距换行；把被压成一行的解析拆成标题、步骤、公式块和结论；手工收口 `GS-009`、`GS-032`、`GS-064`、`GS-073`、`GS-097`、`GS-105`、`GS-115`、`MN4-GS-CH01-514`、`MN4-GS-CH01-652` 等剩余异常页。
- validation: 全量扫描 `files_scanned=870`，最终 `suspect_files=0`；`manifest.json` 与 `asset_to_obsidian.json` JSON 解析通过；`GS-358` 的解析区已改为可渲染公式块结构。
- formal_card_updated: none
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed

## 2026-07-01 GS-350-differentiability-and-visual-readability

- input: 用户指出 `强化例题13.10-2 / GS-350` 的 Obsidian 折叠解析可读性远差于 MarginNote 4，并补充本人错点：连续性与可微性都不知道从哪个定义动作起步，尤其不理解为什么两个偏导为 0。
- evidence: 对照用户截图与 `错题知识网络/可视化错题详情/高等数学/GS-350_强化例题13.10.md`；全量扫描 `错题知识网络/可视化错题详情/**/*.md`，识别“解析文字被压成单行且含未展开 Markdown/LaTeX 标记”的同类候选 453 页。
- formal_card_updated: `错题知识网络/错题卡/GS-350_强化例题13.10-2.md` 从旧导入的“递推数列极限”修正为“二元函数连续性与可微性判定”；补入具体错点、知识点、错因、方法、陷阱、`method_gap`，掌握度保留为“待评分”，未替用户打 0-5 分。
- visual_quality_update: 手工重排 `VIS-GS-350` 的折叠解析为“考点定位 / 详细解答 / 方法小结”结构；第一轮批量重排 453 个“解析文字被压成单行且含未展开 Markdown/LaTeX 标记”的详情页；第二轮对 34 个 `$$...$$`、标题和步骤仍压在超长单行里的详情页继续重排；第三轮对 98 个折叠解析中仍存在超长公式行的详情页做行内公式拆块。最终扫描确认 `remaining_original_ugly_candidates=0`，`answer_blocks_with_line_gt_1200=0`，折叠解析最大引用行长度降至 498。
- wiki_updated: `错题知识网络/知识点库.md` 补 `偏导定义`、`特殊路径` 方法标签；`MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md`、`数学LLMWiki安全输入包.md` 补入“连续性放缩 → 偏导定义 → 可微定义余项检验”训练入口。
- validation: `wrongnet.py rebuild` 成功，cards=763；`wrongnet.py related GS-350` 返回 `GS-047`、`GS-349`、`GS-358`、`GS-364`、`GS-626` 强关联；source summaries、knowledge clusters、pattern clusters 已刷新；可视化详情 `manifest.json`、`asset_to_obsidian.json` 和 `index.md` 的 `last_updated` 已按详情页 frontmatter 对齐；Obsidian bridge snapshot 刷新为 records=866、assets=1238；`manifest.json` 与 `asset_to_obsidian.json` 静默 JSON 校验通过；关键文件控制字符检查通过；`git diff --check` 通过。
- rollback_action: not_run；未修改数学一回滚复习系统 JSON。
- tutor_boundary: 只向 Tutor 安全输入包写入高层定义链训练项，未复制完整题干、完整长解析或正式卡正文。

## 2026-07-01 visual_detail_method_topic_lines

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；本轮补强 linked wrongnet 可视化详情页到深度方法页/专题总线的直接导航。
- evidence: `SRC-WQ-*` source summary 的“深度编译页”中已有 subject-specific `MATHWIKI-{GS|LA|PR}-METHOD-*` 与 `MATHWIKI-{GS|LA|PR}-TOPIC-*` 链接，但大量可视化详情页的“连线建议”没有独立方法页/专题总线行；另有 4 页把 `TOPIC` 误标在“方法页”行。
- wiki_updated: 727 个 `错题知识网络/可视化错题详情/**/{GS|LA|PR}-*.md`；`错题知识网络/wiki/log.md`。
- change: 从对应 `SRC-WQ-{ID}` 的“深度编译页”继承同学科方法页和专题总线链接；新增/更新专题总线行 722 页，新增/更新方法页行 492 页；纠正 4 处“方法页”误标专题总线。
- validation: checked linked visual pages=728；method_line_count=634；topic_line_count=726；方法页/专题总线行跨学科误链 0、断链 0、重复引用 0；subject-specific deep methods/topics 漏接 0；linked 视觉页缺折叠解析入口 0；`manifest.json` 和 `asset_to_obsidian.json` JSON 校验通过；Obsidian bridge snapshot 刷新为 records=865、assets=1236。
- formal_card_updated: none
- wrongnet_rebuild: not_needed_visual_wiki_only
- rollback_action: not_needed

## 2026-07-01 visual_merged_source_bridge_and_method_topic

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；本轮补强 `merged_into_wrongnet` 来源证据页到正式卡、方法页和专题总线的导航。
- evidence: 审计发现 130 个已合并来源页中，124 页缺少跳回正式 wrongnet 的 HTTP 桥接入口，9 页把 `TOPIC` 链接写在“方法页”行；同时 129 页可从对应 `SRC-WQ-{ID}` 继承同学科专题总线，22 页可继承同学科方法页。
- wiki_updated: 129 个 `错题知识网络/可视化错题详情/**/MN4-*.md` merged 来源页；`错题知识网络/wiki/log.md`。
- change: 为 124 个 merged 来源页补入 `合并后正式入口：[ID](http://127.0.0.1:8765/open/ID)`；拆分 9 处方法/专题混写；新增/更新专题总线行 129 页，新增/更新方法页行 22 页。
- validation: merged_checked=130；missing_bridge=0；method_topic_errors=0；missing_deep_methods_on_merged=0；missing_deep_topics_on_merged=0。
- formal_card_updated: none
- wrongnet_rebuild: not_needed_visual_wiki_only
- rollback_action: not_needed

## 2026-07-01 visual_candidate_method_topic_line_split

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；本轮清理候选页/人工重连页中“方法页”与“专题总线”混写。
- evidence: 6 个 `needs_card_decision` 候选页和 1 个 `needs_manual_relink` 页中，有 5 页把 `MATHWIKI-*-TOPIC-*` 链接混在“方法页”行。
- wiki_updated: `MN4-GS-CH01-079`；`MN4-GS-CH01-102`；`MN4-GS-CH01-418`；`MN4-GS-CH01-670`；`MN4-GS-CH01-090`；`错题知识网络/wiki/log.md`。
- change: 只拆分导航行：`MATHWIKI-*-METHOD-*` 保留在“方法页”，`MATHWIKI-*-TOPIC-*` 移入“专题总线”；不改变候选状态，不新建正式卡，不补用户错因。
- validation: 全量视觉页方法/专题语义检查通过；linked_wrongnet=728、merged_into_wrongnet=130、needs_card_decision=6、needs_manual_relink=1；method_topic_semantic_errors=0。
- formal_card_updated: none
- wrongnet_rebuild: not_needed_visual_wiki_only
- rollback_action: not_needed

## 2026-07-01 source_index_visual_coverage_columns

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；本轮补强全量 source index 与科目覆盖表的视觉覆盖可筛选性。
- evidence: `SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引.md` 和各科目覆盖表此前没有 `visual_detail` 列，只能看出 source summary / formal card / cluster_wiki / deep_wiki，不能直接筛选“哪些正式题有题图/折叠解析页”。
- wiki_updated: `错题知识网络/wiki/maintenance/build_wrong_card_source_summaries.py`；`错题知识网络/wiki/sources/SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引.md`；`错题知识网络/wiki/coverage/MATHWIKI-COVERAGE-001_错题卡全量覆盖索引.md`；`错题知识网络/wiki/coverage/MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表.md`；`MATHWIKI-COVERAGE-LA`；`MATHWIKI-COVERAGE-PR`。
- change: 全量索引和科目覆盖表新增 `visual_detail` 列；每行显示已确认视觉详情 wikilink 和题图/解析图计数；覆盖统计新增“已确认可视化详情”和视觉资产计数。
- validation: source index 视觉列存在；coverage 表视觉列存在；728 个有视觉详情的正式 wrongnet ID、858 条 linked/merged 视觉记录全部进入全量索引和覆盖表；缺失视觉 wikilink 目标 0；JSON 校验通过；Obsidian bridge snapshot 刷新为 records=865、assets=1236。
- formal_card_updated: none
- wrongnet_rebuild: not_needed_wiki_only
- rollback_action: not_needed

## 2026-07-01 source_summary_visual_backlinks

- input: 持续目标要求根据题图、解析和现有视觉详情进一步加强错题网络质量；本轮补强正式错题卡 source summary 到可视化详情页的反向导航。
- evidence: `manifest.json` 中 728 个正式 wrongnet ID 已有确认视觉详情，合计 858 条 `linked_wrongnet` / `merged_into_wrongnet` 视觉记录；此前对应 `SRC-WQ-*` 页面均缺少从 source summary 回到题图/折叠解析页的入口。
- wiki_updated: `错题知识网络/wiki/maintenance/build_wrong_card_source_summaries.py`；`错题知识网络/wiki/sources/wrong_cards/SRC-WQ-*.md`；`错题知识网络/wiki/sources/SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引.md`；`错题知识网络/wiki/coverage/MATHWIKI-COVERAGE-001_错题卡全量覆盖索引.md`；各科目覆盖表。
- change: 生成脚本新增 `visual_detail_refs` / `visual_ids`，并在每个 `SRC-WQ-{ID}` 中加入“可视化入口”；有视觉详情的 728 个 source summary 现在可反链到对应题图与折叠解析页，并保留本地桥接打开链接。
- validation: source summary 可视化入口 728/728；linked/merged 视觉记录反链 858/858；缺失视觉 wikilink 目标 0；JSON 校验通过；Obsidian bridge snapshot 刷新为 records=865、assets=1236。
- formal_card_updated: none
- wrongnet_rebuild: not_needed_wiki_only
- rollback_action: not_needed

## 2026-07-01 visual_candidate_enrich MN4-GS-CH01-418

- input: 持续目标要求根据题图和解析进一步加强错题网络质量；本轮复核候选页 `MN4-GS-CH01-418`。
- evidence: 候选页为 2024 年 19 题，解析文字给出旋转体体积 \(V(t)=\pi\int_t^{2t}xe^{-2x}\,dx\)，再用 Leibniz 公式求导并求最大值。
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-418_2024年19题.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-006_定积分错题总线.md
- card_decision: visual_candidate_enriched；缺用户本人错因，暂不正式入库。
- formal_card_updated: none
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed

## 2026-07-01 visual_candidate_enrich MN4-GS-CH01-748

- input: 持续目标要求根据题图和解析进一步加强错题网络质量；本轮复核候选页 `MN4-GS-CH01-748`。
- evidence: 父级路径与解析文字均定位到线代强化第八讲相似理论；题目考查 \(AB=BA\)、\(A\) 有两个不同特征值与 \(B\) 可对角化之间的充分必要关系。
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-748_2024年选择题第10题.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/topics/MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md
- card_decision: visual_candidate_enriched；缺用户本人错因，暂不正式入库。
- formal_card_updated: none
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed

## 2026-07-01 visual_source_merge GS-208-MN4-GS-CH01-278

- input: 持续目标要求根据题图和解析进一步加强错题网络质量；本轮复核候选页 `MN4-GS-CH01-278`。
- evidence: 候选页题干与解析文字均为“高数强化例题6.3”，目标式是 \(f'(\xi)=\left(1-\xi^{-1}\right)f(\xi)\)，方法链为构造 \(F(x)=xe^{-x}f(x)\)，再用积分中值定理和罗尔定理；与正式卡 `GS-208_强化例题6.3.md` 内容一致。
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-278_高数强化例题6.3-2026.5.9-2026.5.20.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/index.md
- card_decision: already_in_wrongnet；并入 `GS-208`，不新建正式卡。正式卡已记录 2026-05-09、2026-05-20 两次复发错因和积分因子 method_gap。
- formal_card_updated: `GS-208_强化例题6.3.md`；仅细化 `method_gap.expected_first_action`，改成可执行第一动作。
- wrongnet_rebuild: required_after_formal_card_update
- rollback_action: not_needed

## 2026-07-01 visual_quality_update MN4-GS-CH01-090-content-mismatch

- input: 持续目标要求根据题图和解析进一步加强错题网络质量；本轮复核候选页 `MN4-GS-CH01-090`。
- evidence: 题图为 `ID:57718` 的不动点/压缩映射证明题；折叠解析文字开头为 `ID:170684`，内容是 `GS-444` 正切递推数列题，题图与解析文字不匹配。
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-090_57718-2026.5.11.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md
- card_decision: manual_relink_required；不新建正式卡，不并入 `GS-444`。需后续补 `57718` 的正确解析或用户错因后再正式入库。
- formal_card_updated: none
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed
- missing_info: 后续如需正式专题页，再新建 `MATHWIKI-GS-TOPIC-*` 页面。

## 2026-07-01 ingest GS-645-84328-ROTATION-SURFACE-PROJECTION

- input: 用户要求将 ID:84328 入库；错因是对空间曲线/曲面和 \(xOy\) 面投影意义模糊，尤其不清楚“\(\Sigma_1\) 与 \(\Sigma_2\) 的交线在 \(xOy\) 面上的投影”为何要联立两曲面并消去 \(z\)。
- source_refs: 错题知识网络/错题卡/GS-645_84328旋转曲面投影.md；用户截图 `/Users/xiazhibin/Library/Application Support/PixPin/Temp/PixPin_2026-07-01_00-55-29.png`；用户截图 `/var/folders/5k/93syh_hn3rq0wyyh6m2bxlq80000gn/T/codex-clipboard-68507a6d-8fa3-461d-8aa8-79c390338ae5.png`
- wiki_updated: 错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-012_空间解析几何错题总线.md；错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-016_空间交线投影消元.md；错题知识网络/wiki/study_vaults/数学LLMWiki/tutor_setup_sources/数学LLMWiki安全输入包.md
- card_decision: formal-card，新建 GS-645；不与 GS-628、GS-629 合并，因为本题是独立来源 ID，且新增断点是“旋转曲面 + 两曲面交线 + 坐标面投影消元”的复合动作链。
- tutor_boundary: 只同步高层动作链到 Tutor 安全输入包，不复制完整长解析，不反写掌握度或回滚 JSON。

## 2026-07-01 update FAST-MATH-WRONG-INTAKE-CLOSEOUT

- input: 用户反馈正式错题入库耗时较长，要求在不考虑 token 消耗的前提下优化入库流程，让单题入库更快完成。
- source_refs: /Users/xiazhibin/.codex/skills/kaoyan-math-wrong-intake/SKILL.md；错题知识网络/scripts/wrongnet.py；错题知识网络/wiki/maintenance/；错题知识网络/可视化错题详情/tools/obsidian_link_bridge.py
- wiki_created: none
- wiki_updated: 错题知识网络/wiki/index.md；错题知识网络/wiki/log.md
- tooling_created: 错题知识网络/scripts/refresh_obsidian_bridge_snapshot.py；错题知识网络/scripts/intake_closeout.py
- skill_updated: 为 kaoyan-math-wrong-intake 增加 Fast Intake Route，要求单题入库后优先用 `intake_closeout.py` 完成 rebuild、wiki 覆盖、Obsidian 跳转桥刷新和 verification。
- validation: `python3 错题知识网络/scripts/intake_closeout.py --id GS-645 --source 84328 --knowledge 空间曲线投影 --knowledge 旋转曲面 --knowledge 坐标面投影` 通过；输出 `closeout ok`，桥快照为 758 个详情页、1043 张图片映射。
- card_decision: no_card，本次是流程工具优化；未新增或修改正式错题卡。
- wrongnet_rebuild: ran_by_validation，作为脚本冒烟测试重建派生索引；未手改生成目录。
- rollback_action: not_needed
- missing_info: 未来如果要进一步压缩到 5-10 秒，需要继续把 wiki coverage 脚本从全量重写改为单卡增量更新；本次先保留全量正确性。

## 2026-07-01 update QUALITY-EQUIVALENT-FAST-INTAKE

- input: 用户明确要求加快入库不能以牺牲入库质量为前提，即使需要消耗更多 token，也要保持正式入库质量不变。
- source_refs: /Users/xiazhibin/.codex/skills/kaoyan-math-wrong-intake/SKILL.md；错题知识网络/scripts/intake_preflight.py；错题知识网络/scripts/intake_closeout.py
- wiki_created: none
- wiki_updated: 错题知识网络/wiki/index.md；错题知识网络/wiki/log.md
- tooling_created: 错题知识网络/scripts/intake_preflight.py
- skill_updated: 将 Fast Intake Route 改名为 Quality-Equivalent Fast Intake Route，并写明不得跳过规则读取、查重、正式卡字段、视觉详情、wiki coverage、Tutor-safe 判断、Obsidian 可见性检查或 verification。
- validation: `python3 错题知识网络/scripts/intake_preflight.py --source 84328 --title 旋转曲面投影 --prefix GS` 通过；能查出既有 `GS-645`、下一个编号 `GS-646`、Obsidian 搜索结果和桥服务健康状态。
- card_decision: no_card，本次是流程质量约束和预检工具优化；未新增或修改正式错题卡。
- wrongnet_rebuild: not_needed，本次只改规则、脚本和 wiki 记录；预检脚本本身只读。
- rollback_action: not_needed
- missing_info: 后续真实单题入库仍需根据题目内容和用户错因完整判断 knowledge、wrong_point、method_gap、visual detail、wiki/Tutor 更新，预检脚本不能替代正式判断。

## 2026-07-01 update FAST-INTAKE-QUALITY-GATE

- input: 用户要求在不限制 token 的前提下继续优化正式错题入库，目标同时是高质量和高速度。
- source_refs: 错题知识网络/scripts/intake_closeout.py；错题知识网络/scripts/intake_quality_gate.py；错题知识网络/录入模板.md；错题知识网络/方法论库/method_gap_schema.md；错题知识网络/可视化错题详情/manifest.json
- wiki_created: none
- wiki_updated: 错题知识网络/wiki/index.md；错题知识网络/wiki/log.md
- tooling_created: 错题知识网络/scripts/intake_quality_gate.py
- tooling_updated: 错题知识网络/scripts/intake_closeout.py；/Users/xiazhibin/.codex/skills/kaoyan-math-wrong-intake/SKILL.md
- quality_gate_scope: 正式卡 frontmatter、必填字段、knowledge、wrong_history、mastery_history、method_gap 允许值与必填字段、review 字段、source summary、全量覆盖索引、多维覆盖矩阵、wrong_questions.json、视觉详情页、折叠解析、题图/解析资产、asset_to_obsidian、obsidian_open_links、本地桥快照。
- validation: `python3 错题知识网络/scripts/intake_quality_gate.py --id GS-645 --source 84328 --visual expected` 通过，ERROR none，WARN none；`intake_closeout.py ... --visual expected` 通过并自动执行质量门，总耗时约 21.4 秒。
- card_decision: no_card，本次是质量门和流程工具优化；未新增或修改正式错题卡。
- wrongnet_rebuild: ran_by_validation，作为 closeout 冒烟测试重建派生索引；未手改生成目录。
- rollback_action: not_needed
- missing_info: 进一步提速的下一阶段应考虑“单卡增量 wiki coverage”和“结构化 spec 生成正式卡/视觉页”，但不能跳过质量门。

## 2026-07-01 ingest GS-646-102465-PARAMETER-CURVE-TANGENT

- input: 用户要求将 ID:102465 入库；错因是看到参数式空间曲线在 \(t=0\) 处求切线方程时，没有想到“代 \(t_0\) 定切点、对参数求导定切向量、用点向式写直线”的入口；补充错因是计算 \(z=1+e^{3t}\) 时把导数误写成 \(1+3e^{3t}\)，没有把常数 \(1\) 的导数处理为 \(0\)。
- source_refs: 错题知识网络/错题卡/GS-646_102465参数曲线切线方程.md；用户截图 `/Users/xiazhibin/Library/Application Support/PixPin/Temp/PixPin_2026-07-01_02-17-54_1.png`；用户截图 `/var/folders/5k/93syh_hn3rq0wyyh6m2bxlq80000gn/T/codex-clipboard-4d4c5035-9410-4af7-9e3e-bc1fb4e22712.png`
- wiki_created: 错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-017_参数曲线切线点向式.md；错题知识网络/可视化错题详情/高等数学/GS-646_102465参数曲线切线方程.md；错题知识网络/assets/visual_wrong_questions/GS-646/question_01.png；错题知识网络/assets/visual_wrong_questions/GS-646/solution_01.png
- wiki_updated: 错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-012_空间解析几何错题总线.md；错题知识网络/wiki/study_vaults/数学LLMWiki/tutor_setup_sources/数学LLMWiki安全输入包.md；错题知识网络/可视化错题详情/index.md
- card_decision: formal-card，新建 GS-646；不与 GS-629 合并，因为本题是独立来源 ID，且新增断点是“参数式空间曲线切线入口 + 常数项求导误带入”。
- wrongnet_rebuild: success，758 cards，strong=1659，medium=526，weak_audit=500
- wiki_coverage_refresh: success，source summaries=758，knowledge_clusters=321，method_clusters=636，error_clusters=249，action_gap_clusters=8
- visual_bridge_refresh: success，records=759，assets=1045
- quality_gate: ok，ERROR none，WARN none
- rollback_action: not_run；本次只设置错题卡内 `review.next: 2026-07-02`，不手改回滚 JSON。
- tutor_boundary: 只同步高层动作链到 Tutor 安全输入包，不复制完整题干、题图、解析图或长解析，不反写掌握度或回滚 JSON。

## 2026-07-01 ingest GS-647-84298-CURVE-NORMAL-PLANE

- input: 用户要求将 ID:84298 入库；错因是看到曲线由 \(z=f(x,y)\) 与 \(y=0\) 给出并要求法平面时，没有找到入口，不知道应先把 \(x\) 看作参数并求切向量；同时把切线点向式误认为法平面方程。
- source_refs: 错题知识网络/错题卡/GS-647_84298曲线法平面方程.md；用户截图 `/Users/xiazhibin/Library/Application Support/PixPin/Temp/PixPin_2026-07-01_02-34-11.png`；用户截图 `/Users/xiazhibin/Library/Application Support/PixPin/Temp/PixPin_2026-07-01_02-34-22.png`
- wiki_created: 错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-018_空间曲线法平面切向量.md；错题知识网络/可视化错题详情/高等数学/GS-647_84298曲线法平面方程.md；错题知识网络/assets/visual_wrong_questions/GS-647/question_01.png；错题知识网络/assets/visual_wrong_questions/GS-647/solution_01.png
- wiki_updated: 错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-012_空间解析几何错题总线.md；错题知识网络/wiki/study_vaults/数学LLMWiki/tutor_setup_sources/数学LLMWiki安全输入包.md；错题知识网络/可视化错题详情/index.md
- card_decision: formal-card，新建 GS-647；不与 GS-646 合并，因为本题是独立来源 ID，且新增断点是“空间曲线法平面入口 + 切线点向式与法平面点法式混淆”。
- rollback_action: not_run；本次只设置错题卡内 `review.next: 2026-07-02`，不手改回滚 JSON。
- tutor_boundary: 只同步高层动作链到 Tutor 安全输入包，不复制完整题干、题图、解析图或长解析，不反写掌握度或回滚 JSON。
- wrongnet_rebuild: success，759 cards，strong=1666，medium=526，weak_audit=500
- wiki_coverage_refresh: success，source summaries=759，knowledge_clusters=321，method_clusters=639，error_clusters=249，action_gap_clusters=8
- visual_bridge_refresh: success，records=760，assets=1047
- quality_gate: ok，ERROR none，WARN none

## 2026-07-01 update VISUAL-WRONGNET-QUALITY-PASS-001

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量。
- source_refs: 错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-001_待调查问题与素材队列.md
- wiki_created: 错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md
- wiki_updated: 错题知识网络/wiki/index.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-001_待调查问题与素材队列.md；错题知识网络/错题卡/GS-403_2024年真题17.md；错题知识网络/可视化错题详情/高等数学/GS-403_2024年真题17.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/wiki/sources/wrong_cards/SRC-WQ-GS-403.md；错题知识网络/wiki/coverage/MATHWIKI-COVERAGE-MATRIX_错题卡多维编译矩阵.md；错题知识网络/wiki/methods/method_clusters/
- visual_assets_updated: 将 `MN4-GS-CH01-553`、`MN4-GS-CH01-559` 中与 `VIS-GS-403` 题图哈希一致、refid 相同的两张解析图复制为 `GS-403/solution_01.png`、`GS-403/solution_02.png`，并放入 `GS-403` 正式视觉详情页的折叠解析块。
- formal_card_updated: `GS-403` 旧卡补全标准答案、wrong_history/mastery_history、二重积分轮换对称性方法标签、复做提醒和相关题；具体错因仍保守标记为旧卡未记录，待复做确认。
- audit_result: 可视化记录 760；已连正式 wrongnet 624；候选页 136；标题/定位命中已有正式卡 29；题图哈希也一致 12；图片反查映射增至 1049。
- card_decision: update-existing-card；未新增正式卡；更新 `GS-403` 旧卡并增强视觉详情层、候选决策队列和 Obsidian 跳转映射。
- wrongnet_rebuild: success，cards=759，strong=1666，medium=526，weak_audit=500；wiki coverage refresh success，source summaries=759，knowledge_clusters=321，method_clusters=643，error_clusters=249，action_gap_clusters=8；visual_bridge_refresh success，records=760，assets=1049。
- quality_gate: `python3 错题知识网络/scripts/intake_quality_gate.py --id GS-403 --source 2024年真题17 --visual expected` 通过，ERROR none，WARN 仅 `method_gap not enabled`；因旧卡缺少用户作答过程，本轮不强行补 method_gap。
- rollback_action: not_needed
- tutor_boundary: not_needed；候选队列和补充解析图不进入 Tutor safe source，不复制完整题干或长解析进 Tutor。
- missing_info: 其余 136 个候选页仍需按队列逐步核验；标题一致但题图不同的候选不能自动合并或正式入库。

## 2026-07-01 update VISUAL-WRONGNET-LA-SUPPLEMENT-PASS-001

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理线代第三讲矩阵运算中数字题号与正式 LA 卡精确一致的 8 个可视化候选页。
- source_refs: 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-688_强化例题3.5（84129）.md；MN4-GS-CH01-689；MN4-GS-CH01-692；MN4-GS-CH01-693；MN4-GS-CH01-695；MN4-GS-CH01-696；MN4-GS-CH01-697；MN4-GS-CH01-701；对应正式错题卡 LA-045、LA-046、LA-049、LA-050、LA-052、LA-053、LA-054、LA-058。
- wiki_created: 错题知识网络/可视化错题详情/线性代数/LA-045_强化例题3.5（84129）.md；LA-046；LA-049；LA-050；LA-052；LA-053；LA-054；LA-058；以及对应 `错题知识网络/assets/visual_wrong_questions/LA-*/question_01.png`、`solution_01.png`。
- wiki_updated: 错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md。
- card_decision: update-existing-visual-layer；8 道题已有正式 LA 错题卡，本轮只补正式视觉详情层，不改正式卡 wrong_point、掌握度或回滚 JSON。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed
- tutor_boundary: not_needed；本轮只补题图/解析图和 Obsidian 跳转，不把完整题图或解析图写入 Tutor 安全源。
- missing_info: 原 LA 旧卡多数仍缺用户具体错因；需用户复做或口述后再补正式 wrong_point/method_gap。
- postcheck: 原 8 个 MN4 来源候选页已改为 `merged_into_wrongnet` 来源保留状态；待确认候选数从 136 校正为 128，正式错题卡仍未改动。

## 2026-07-01 update VISUAL-WRONGNET-HASH-DEDUPE-MISMATCH-PASS-002

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理题图哈希/refid 完全一致的重复候选和 GS-257 视觉错连风险。
- source_refs: 错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/可视化错题详情/线性代数/GS-257_强化例题7.1.md
- wiki_updated: 错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/wiki/index.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；相关来源视觉页 12 个。
- visual_quality_update: MN4-GS-CH01-465/479/482 标记并入 GS-331；MN4-GS-CH01-499/506/512 标记并入 GS-359；MN4-GS-CH01-549/553/559 标记并入 GS-403；VIS-GS-257 标记 suspect_wrongnet_mismatch；MN4-GS-CH01-694/740/741 标记 needs_manual_relink，候选目标 LA-021/LA-051/LA-101/LA-102。
- card_decision: visual-only；未修改正式错题卡。GS-257 正式卡仍是高数相关变化率，视觉页题图为线代题，故只标记错连风险，不自动改 formal wrongnet。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed
- tutor_boundary: not_needed；本轮只处理视觉索引状态，不复制完整题图或解析到 Tutor safe source。
- postcheck_target: manifest 应为 records=768、linked_wrongnet=631、needs_card_decision=116、merged_into_wrongnet=17、needs_manual_relink=3、suspect_wrongnet_mismatch=1。


## 2026-07-01 update VISUAL-WRONGNET-EXACT-ID-SUPPLEMENT-PASS-003

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理高置信正式卡纠错、重复来源并入和线代第八/九讲精确标题候选补页。
- source_refs: MN4-GS-CH01-110；MN4-GS-CH01-362；MN4-GS-CH01-440；MN4-GS-CH01-664；MN4-GS-CH01-672；MN4-GS-CH01-751；MN4-GS-CH01-756；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json。
- wiki_created: 错题知识网络/可视化错题详情/高等数学/GS-073_103499.md；错题知识网络/可视化错题详情/线性代数/LA-028_强化例题9.3(164730).md；LA-036；LA-113；LA-118；以及对应正式视觉题图资产。
- wiki_updated: 错题知识网络/可视化错题详情/index.md；obsidian_open_links.md；asset_to_obsidian.json；manifest.json；错题知识网络/wiki/index.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；相关来源候选页；GS-312 正式视觉详情页解析文字。
- visual_quality_update: GS-073 原正式视觉页内容与正式卡不一致，已撤出正式入口并标记误链保留；MN4-GS-CH01-110 校正为 GS-073 正式视觉入口；MN4-GS-CH01-362/440 标记并入 GS-258/GS-312；MN4-GS-CH01-664/672/751/756 补为 LA-028/LA-036/LA-113/LA-118 正式视觉详情页。
- card_decision: visual-only；未修改正式错题卡。58049 候选页内容与 GS-069 不一致，继续保留为 needs_card_decision，不按数字 ID 硬合并。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed
- tutor_boundary: not_needed；本轮只处理视觉索引、题图和来源状态，不复制完整题图或解析到 Tutor safe source。
- postcheck_target: manifest 应为 records=772、linked_wrongnet=635、needs_card_decision=109、merged_into_wrongnet=24、needs_manual_relink=3、suspect_wrongnet_mismatch=1。


## 2026-07-01 update VISUAL-LA-EXACT-TITLE-SINGLE-PASS-004

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理线代正式卡标题精确命中且只有一个候选来源的视觉页。
- source_refs: LA-003<-MN4-GS-CH01-341；LA-004<-MN4-GS-CH01-514；LA-007<-MN4-GS-CH01-645；LA-009<-MN4-GS-CH01-647；LA-010<-MN4-GS-CH01-648；LA-013<-MN4-GS-CH01-651；LA-014<-MN4-GS-CH01-652；LA-015<-MN4-GS-CH01-653；LA-016<-MN4-GS-CH01-654；LA-018<-MN4-GS-CH01-656；LA-020<-MN4-GS-CH01-658；LA-022<-MN4-GS-CH01-660；LA-023<-MN4-GS-CH01-661；LA-025<-MN4-GS-CH01-662；LA-026<-MN4-GS-CH01-663；LA-030<-MN4-GS-CH01-665；LA-031<-MN4-GS-CH01-666；LA-032<-MN4-GS-CH01-667；LA-033<-MN4-GS-CH01-668；LA-034<-MN4-GS-CH01-669；LA-035<-MN4-GS-CH01-671；LA-037<-MN4-GS-CH01-673；LA-038<-MN4-GS-CH01-674；LA-039<-MN4-GS-CH01-675；LA-040<-MN4-GS-CH01-676；LA-041<-MN4-GS-CH01-677；LA-042<-MN4-GS-CH01-678；LA-043<-MN4-GS-CH01-679；LA-044<-MN4-GS-CH01-680；LA-047<-MN4-GS-CH01-690；LA-048<-MN4-GS-CH01-691；LA-055<-MN4-GS-CH01-698；LA-056<-MN4-GS-CH01-699；LA-057<-MN4-GS-CH01-700；LA-059<-MN4-GS-CH01-702；LA-060<-MN4-GS-CH01-703；LA-061<-MN4-GS-CH01-704；LA-062<-MN4-GS-CH01-705；LA-063<-MN4-GS-CH01-706；LA-067<-MN4-GS-CH01-708；LA-069<-MN4-GS-CH01-710；LA-071<-MN4-GS-CH01-712；LA-072<-MN4-GS-CH01-713；LA-074<-MN4-GS-CH01-715；LA-075<-MN4-GS-CH01-716；LA-082<-MN4-GS-CH01-721；LA-087<-MN4-GS-CH01-726；LA-088<-MN4-GS-CH01-727；LA-089<-MN4-GS-CH01-728；LA-091<-MN4-GS-CH01-730；LA-092<-MN4-GS-CH01-731；LA-093<-MN4-GS-CH01-732；LA-097<-MN4-GS-CH01-736；LA-100<-MN4-GS-CH01-739；LA-104<-MN4-GS-CH01-743；LA-105<-MN4-GS-CH01-744；LA-106<-MN4-GS-CH01-745；LA-111<-MN4-GS-CH01-749；LA-116<-MN4-GS-CH01-754；LA-117<-MN4-GS-CH01-755；LA-119<-MN4-GS-CH01-757
- wiki_created: 新增 61 个线性代数正式视觉详情页，并复制对应题图/解析图资产。
- wiki_updated: 错题知识网络/可视化错题详情/manifest.json；index.md；asset_to_obsidian.json；obsidian_open_links.md；错题知识网络/wiki/index.md；MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；相关 MN4 来源候选页。
- card_decision: visual-only；只补已有正式 LA 卡的视觉详情，不修改正式错题卡 wrong_point、answer、method_gap、掌握度或回滚 JSON。
- skipped: LA-008、LA-079、LA-094 等重复候选组暂不自动合并，后续需人工看图确认主图/解析图关系。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed
- tutor_boundary: not_needed；本轮只处理视觉层和 Obsidian 跳转，不复制完整题图或解析到 Tutor safe source。
- postcheck_target: manifest 应为 records=833、linked_wrongnet=696、needs_card_decision=48、merged_into_wrongnet=85、assets=1180。


## 2026-07-01 update VISUAL-LA-DUPLICATE-TITLE-PASS-005

- input: 处理剩余线代重复标题候选组。
- visual_quality_update: LA-008 用 MN4-GS-CH01-646 补正式视觉详情，MN4-GS-CH01-650 因题图不同标记 needs_manual_relink；LA-079 与 LA-094 的重复候选题图/解析图哈希一致，已安全合并到正式视觉详情。
- card_decision: visual-only；未修改正式错题卡、掌握度、method_gap 或回滚 JSON。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed
- postcheck_target: manifest records=836、linked_wrongnet=699、needs_card_decision=42、merged_into_wrongnet=90、needs_manual_relink=4、assets=1185。

## 2026-07-01 update VISUAL-GS-PR-EXACT-TITLE-SUPPLEMENT-PASS-006

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理 5 个已存在正式卡、但仍停留在候选视觉页的高数/PR 精确来源。
- source_refs: MN4-GS-CH01-035->GS-025；MN4-GS-CH01-111->GS-080；MN4-GS-CH01-169->GS-121；MN4-GS-CH01-318->GS-234；MN4-GS-CH01-236->PR-001；跳过 MN4-GS-CH01-747。
- wiki_created: 错题知识网络/可视化错题详情/高等数学/GS-025_2020年第15题.md；GS-080_2023年真题第三题.md；GS-121_强化例题4.6.md；GS-234_2025年真题18.md；错题知识网络/可视化错题详情/概率论与数理统计/PR-001_强化例题8.2.md；以及对应 5 张正式视觉题图资产。
- wiki_updated: 错题知识网络/可视化错题详情/manifest.json；index.md；asset_to_obsidian.json；obsidian_open_links.md；错题知识网络/wiki/index.md；MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；相关 MN4 来源候选页。
- card_decision: visual-only；这些题已有正式错题卡，本轮只补正式视觉详情，不修改正式卡 wrong_point、answer、method_gap、掌握度或回滚 JSON。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed
- tutor_boundary: not_needed；本轮只处理题图、来源页和 Obsidian 跳转，不把完整题图或长解析写入 Tutor safe source。
- skipped: MN4-GS-CH01-747 与 PR-001 同名“强化例题8.2”，但内容为线代相似对角化，不能按标题硬合并。
- postcheck_target: manifest records=841、linked_wrongnet=704、needs_card_decision=37、merged_into_wrongnet=95、assets=1190。

## 2026-07-01 update VISUAL-LA-SIMILARITY-THEORY-PASS-007

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理线代第八讲相似理论中已有正式卡但仍停留在候选视觉页的 5 个高置信来源。
- source_refs: MN4-GS-CH01-746->LA-109；MN4-GS-CH01-747->LA-110；MN4-GS-CH01-750->LA-112；MN4-GS-CH01-752->LA-114；MN4-GS-CH01-753->LA-115。
- wiki_created: 错题知识网络/可视化错题详情/线性代数/LA-109_强化例题8.1-2.md；LA-110_强化例题8.2-2.md；LA-112_强化例题8.4-2.md；LA-114_强化例题8.7-2.md；LA-115_强化例题8.6-2.md；以及对应题图/解析图资产。
- wiki_updated: 错题知识网络/可视化错题详情/manifest.json；index.md；asset_to_obsidian.json；obsidian_open_links.md；错题知识网络/wiki/index.md；MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；相关 MN4 来源候选页。
- card_decision: visual-only；这些题已有正式 LA 错题卡，本轮只补正式视觉详情和折叠解析图，不修改正式卡 wrong_point、answer、method_gap、掌握度或回滚 JSON。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed
- tutor_boundary: not_needed；本轮只处理题图、解析图、来源页和 Obsidian 跳转，不把完整题图或长解析写入 Tutor safe source。
- postcheck_target: manifest 应为 records=846、linked_wrongnet=709、needs_card_decision=32、merged_into_wrongnet=100、assets=1200。


## 2026-07-01 update VISUAL-LA-MATRIX-RANK-EQUATION-PASS-008

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理线代矩阵秩、线性方程组、向量组和特征值中已有正式卡但仍停留在候选视觉页的 7 个高置信来源。
- source_refs: MN4-GS-CH01-707->LA-064；MN4-GS-CH01-709->LA-068；MN4-GS-CH01-711->LA-070；MN4-GS-CH01-714->LA-073；MN4-GS-CH01-729->LA-090；MN4-GS-CH01-738->LA-099；MN4-GS-CH01-742->LA-103。
- wiki_created: 错题知识网络/可视化错题详情/线性代数/LA-064_1000题B组3.11-3.md；LA-068_强化例题4.3-2.md；LA-070_强化例题4.4-2.md；LA-073_强化例题4.9-2.md；LA-090_强化例题5.7-2.md；LA-099_强化例题6.6-2.md；LA-103_强化例题7.2-2.md；以及对应题图/解析图资产。
- wiki_updated: 错题知识网络/可视化错题详情/manifest.json；index.md；asset_to_obsidian.json；obsidian_open_links.md；错题知识网络/wiki/index.md；MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；相关 MN4 来源候选页。
- card_decision: visual-only；这些题已有正式 LA 错题卡，本轮只补正式视觉详情和折叠解析图，不修改正式卡 wrong_point、answer、method_gap、掌握度或回滚 JSON。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed
- tutor_boundary: not_needed；本轮只处理题图、解析图、来源页和 Obsidian 跳转，不把完整题图或长解析写入 Tutor safe source。
- postcheck_target: manifest 应为 records=853、linked_wrongnet=716、needs_card_decision=25、merged_into_wrongnet=107、assets=1214。

## 2026-07-01 update VISUAL-LA-ABSTRACT-VECTOR-PASS-009

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理线代第六讲向量组综合问题候选页 `MN4-GS-CH01-737`。
- source_refs: 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-737_强化例题6.5.md；错题知识网络/错题卡/LA-098_强化例题6.5-2.md；错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-737/question_01.png
- wiki_created: 错题知识网络/可视化错题详情/线性代数/LA-098_强化例题6.5-2.md；错题知识网络/assets/visual_wrong_questions/LA-098/question_01.png
- wiki_updated: 错题知识网络/错题卡/LA-098_强化例题6.5-2.md；错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-737_强化例题6.5.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md
- card_decision: update-existing-card；`MN4-GS-CH01-737` 的父级路径为线代第六讲向量组综合问题，内容为抽象列向量关系求非齐次线性方程组通解，故并入正式卡 `LA-098`。同名 `GS-216` 为高数中值定理题，题图哈希与父级路径均不同，不合并。
- formal_card_updated: `LA-098` 补全题目定位、标准答案、知识点、方法入口、陷阱和复做提醒；因旧批量导入未记录用户具体错因，`wrong_point` 保守标记为暂无明确错因，掌握度标记待评分，不硬编 method_gap。
- visual_quality_update: 新建 `VIS-LA-098` 正式视觉详情页，复制题图到 `LA-098/question_01.png`；来源页 `MN4-GS-CH01-737` 改为 `merged_into_wrongnet` 来源保留状态。
- wrongnet_rebuild: success，cards=759，strong=1669，medium=523，weak_audit=500；wiki coverage refresh success，source summaries=759，knowledge_clusters=323，method_clusters=646，error_clusters=249，action_gap_clusters=8；visual_bridge_refresh success，records=854，assets=1215。
- quality_gate: `python3 错题知识网络/scripts/intake_quality_gate.py --id LA-098 --source 强化例题6.5 --visual expected` 通过，ERROR none，WARN 仅 `method_gap not enabled`；因旧批量导入缺用户作答过程，本轮不硬编 method_gap。
- rollback_action: not_needed
- tutor_boundary: not_needed；本轮只把高层方法入口进入 wrongnet/wiki 覆盖，不把完整题图或长解析写入 Tutor safe source。

## 2026-07-01 update VISUAL-LA-021-MISLINK-FIX-20260701

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理 GS-257 疑似视觉错连组。
- source_refs: VIS-GS-257；MN4-GS-CH01-694；MN4-GS-CH01-740；MN4-GS-CH01-741；错题知识网络/错题卡/LA-021_强化例题7.1-2.md。
- wiki_created: 错题知识网络/可视化错题详情/线性代数/LA-021_强化例题7.1-2.md；错题知识网络/assets/visual_wrong_questions/LA-021/question_01.png。
- wiki_updated: 错题知识网络/错题卡/LA-021_强化例题7.1-2.md；错题知识网络/可视化错题详情/线性代数/GS-257_强化例题7.1.md；MN4-GS-CH01-694/740/741 来源页；manifest.json；index.md；asset_to_obsidian.json；obsidian_open_links.md；wiki/index.md；MATHWIKI-QUESTIONS-002。
- card_decision: update-existing-card；题图和解析文字为线性代数伴随矩阵与特征值题，归并到正式主卡 LA-021；LA-051/LA-101/LA-102 为旧批量导入重复卡，本轮不删除、不改名。
- formal_card_updated: LA-021 补全题目定位、标准答案、知识点、方法入口、陷阱和复做提醒；因旧批量导入未记录用户具体错因，wrong_point 保守标记为暂无明确错因，掌握度标记待评分。
- visual_quality_update: 新建 VIS-LA-021 正式视觉详情；3 个来源页标记 merged_into_wrongnet；GS-257 页保留 suspect_wrongnet_mismatch 错连证据。
- wrongnet_rebuild: success，cards=759，strong=1668，medium=525，weak_audit=500；wiki coverage refresh success，source summaries=759，knowledge_clusters=323，method_clusters=646，error_clusters=249，action_gap_clusters=8；visual_bridge_refresh success，records=855，assets=1216。
- quality_gate: `python3 错题知识网络/scripts/intake_quality_gate.py --id LA-021 --source 强化例题7.1 --visual expected` 通过，ERROR none，WARN 仅 `method_gap not enabled`；因旧批量导入缺用户作答过程，本轮不硬编 method_gap。
- rollback_action: not_needed
- tutor_boundary: not_needed；本轮只把高层方法入口进入 wrongnet/wiki 覆盖，不把完整题图或长解析写入 Tutor safe source。
## 2026-07-01 visual_quality_update LA-012-MN4-GS-CH01-650

- input: 继续增强可视化错题网络；处理唯一 `needs_manual_relink`：MN4-GS-CH01-650。
- evidence: MN4-GS-CH01-650 题图/解析为 `det(I+alpha alpha^T)` 秩一扰动行列式；正式卡 LA-012 为同题；LA-008 是同名但不同的线性方程组/四阶子式题。
- updated_card: 错题知识网络/错题卡/LA-012_强化例题1.2-2.md，修正 OCR 残损公式，补清题目定位、标准答案、方法和陷阱；错因仍记为“暂无明确错因”。
- visual_created: 错题知识网络/可视化错题详情/线性代数/LA-012_强化例题1.2-2.md；题图与解析图已复制到 `错题知识网络/assets/visual_wrong_questions/LA-012/`。
- visual_merged: MN4-GS-CH01-650 标记 `merged_into_wrongnet` -> LA-012；排除 LA-008。
- wrongnet_rebuild: closeout_ok；`intake_closeout.py --id LA-012 --visual expected` 已通过，quality_gate=ok，WARN 仅为旧卡无 method_gap。
- tutor_update: 已把“\(I+\alpha\alpha^{\mathrm T}\) / \(I+uv^{\mathrm T}\) 先识别秩一外积，再用特征值平移或矩阵行列式引理”写入数学LLMWiki安全输入包和线性代数主线 StudyVault；未启动交互式 Tutor 测验，未反写掌握度。
- rollback_action: not_needed。

## 2026-07-01 visual_quality_update VIS-GS-257-resolved-to-LA-021

- input: 继续增强可视化错题网络；收口唯一 `suspect_wrongnet_mismatch`：VIS-GS-257。
- evidence: `GS-257/question_01.png` 与 `LA-021/question_01.png` 的 SHA-256 完全一致，题图内容为线性代数伴随矩阵迹与特征值题；正式 `GS-257` 是高数相关变化率题，不能作为本视觉页主卡。
- visual_updated: `错题知识网络/可视化错题详情/线性代数/GS-257_强化例题7.1.md` 从 `suspect_wrongnet_mismatch` 改为 `merged_into_wrongnet`，`wrongnet_id` 指向 `LA-021`，并保留 `original_wrongnet_id: GS-257` 与排除说明。
- index_updated: `manifest.json`、`asset_to_obsidian.json`、`obsidian_open_links.md`、`可视化错题详情/index.md`、`wiki/index.md`、`MATHWIKI-QUESTIONS-002` 已同步；当前视觉记录为 719 linked、24 needs_card_decision、113 merged_into_wrongnet、0 needs_manual_relink、0 suspect_wrongnet_mismatch。
- formal_card_updated: none；本轮不修改 `GS-257` 或 `LA-021` 正式错题卡，不改掌握度，不改 method_gap。
- wrongnet_rebuild: not_needed_visual_only。
- rollback_action: not_needed。

## 2026-07-01 ingest GS-648-79104-MVT-PROOF-ENTRY

- input: 视觉候选 MN4-GS-CH01-316 与 MN4-GS-CH01-324 同题，题号 79104 / 2020年第20题；324 已有明确错因归纳：中值定理证明题题型识别未启动，第一问未构造辅助函数，第二问未识别柯西中值定理。
- source_refs: 错题知识网络/错题卡/GS-648_79104中值定理证明入口.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-316_2020年第20题-79104-2026.5.8.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-324_2020年第20题-79104-2026.5.8.md；错题知识网络/assets/visual_wrong_questions/GS-648/question_01.png；错题知识网络/assets/visual_wrong_questions/GS-648/solution_01.png
- wiki_created: 错题知识网络/可视化错题详情/高等数学/GS-648_79104中值定理证明入口.md
- wiki_updated: 错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md
- card_decision: formal-card，新建 GS-648；MN4-GS-CH01-316 与 MN4-GS-CH01-324 标记为 merged_into_wrongnet 来源证据。
- wrongnet_rebuild: needed_after_card_create
- rollback_action: not_run
- missing_info: 回滚系统未更新；掌握度为 AI 依据来源错因归纳评分 3/5，后续复做可由用户修正。

## 2026-07-01 closeout GS-647-84298-CURVE-NORMAL-PLANE

- input: 用户确认 ID:84298 需要入库；本轮复核发现该题已作为 GS-647 入库，故不重复新建 GS-649。
- source_refs: 错题知识网络/错题卡/GS-647_84298曲线法平面方程.md；错题知识网络/可视化错题详情/高等数学/GS-647_84298曲线法平面方程.md
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/GS-647_84298曲线法平面方程.md
- card_decision: already-formal-card；保留 GS-647，来源 ID 84298 已命中正式卡、视觉详情、方法页与专题总线。
- wrongnet_rebuild: closeout ok，cards=760，quality_gate=ok，ERROR none，WARN none。
- rollback_action: not_run
- missing_info: 无；后续复做后可由用户修正掌握度。

## 2026-07-01 visual_candidate_quality_update MN4-GS-CH01-102

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理未匹配正式卡但有题图和解析图的候选页 `MN4-GS-CH01-102`。
- source_refs: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-102_2024年选择题第四题.md；错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-102/question_01.png；错题知识网络/assets/visual_wrong_questions/MN4-GS-CH01-102/solution_01.png
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-102_2024年选择题第四题.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-007_数列极限错题总线.md
- card_decision: visual_candidate_enriched；题目已复述为“发散数列经函数变换是否保持发散”，入口是先判函数一一对应，不一一对应则构造同值反例。未见用户本人具体错因，暂不新建正式 GS 卡。
- formal_card_updated: none
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed

## 2026-07-01 visual_source_merge GS-133-MN4-GS-CH01-023

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理候选页 `MN4-GS-CH01-023｜57978.2026.6.1`。
- evidence: 预检命中正式卡 `GS-133_1000题A组5.19.md`；人工核验两张题图均为 `f(x)=nx(1-x)^n` 在 `[0,1]` 上求最大值及极限的同题，候选页提供带 `ID:57978` 的题干截图。
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/GS-133_1000题A组5.19.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-023_57978.2026.6.1.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md。
- visual_quality_update: 将 `MN4-GS-CH01-023` 标记为 `merged_into_wrongnet -> GS-133`；复制题图为 `错题知识网络/assets/visual_wrong_questions/GS-133/question_02.png`，正式视觉页 `VIS-GS-133` 展示两张题图。
- card_decision: merge-existing-card；正式错题卡 `GS-133` 已完整记录复发错因和 method_gap，本轮不重复建卡、不修改正式卡。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed

## 2026-07-01 visual_source_merge GS-502-MN4-GS-CH01-599

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理候选页 `MN4-GS-CH01-599｜171554`。
- evidence: 预检命中正式卡 `GS-502_102347条件收敛奇偶拆分.md`，正式卡已记录 `ID171554` 为同题别名；人工核验题图为同一条件收敛与奇偶项拆分题，答案同为 A 发散。
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/GS-502_102347-2026.5.26.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-599_171554.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md。
- visual_quality_update: 将 `MN4-GS-CH01-599` 标记为 `merged_into_wrongnet -> GS-502`；复制题图为 `错题知识网络/assets/visual_wrong_questions/GS-502/question_02.png`，复制解析图为 `错题知识网络/assets/visual_wrong_questions/GS-502/solution_01.png`。
- card_decision: merge-existing-card；正式错题卡 `GS-502` 已记录复发错因、掌握度轨迹和 method_gap，本轮不重复建卡、不修改正式卡。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed

## 2026-07-01 visual_candidate_quality_update MN4-GS-CH01-670

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理候选页 `MN4-GS-CH01-670｜2018年数学2第22题`。
- evidence: 预检未命中正式 GS/LA 卡；人工看图确认其内容为线性代数二次型，父级路径也属于线代第九讲二次型，不是高等数学。
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-670_2018年数学2第22题.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/topics/MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md。
- visual_quality_update: 补全题目定位为线代二次型参数与规范形；第一动作为平方和为零时令每个平方项分别为 0；第二问提示按 \(a\ne2\) 与 \(a=2\) 处理可逆变换和配方法。
- card_decision: visual_candidate_enriched；缺用户本人具体错因，暂不新建 LA-120，不修改正式错题卡。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed

## 2026-07-01 visual_candidate_quality_update MN4-GS-CH01-683

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理候选页 `MN4-GS-CH01-683｜2022年22题`。
- evidence: 预检未命中正式 LA 卡；人工看图确认其内容为线性代数二次型正交变换与 Rayleigh 商最值，父级路径属于线代第九讲二次型。
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-683_2022年22题.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/topics/MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md。
- visual_quality_update: 补全题目定位为二次型正交变换与 Rayleigh 商；第一动作为写出实对称矩阵 \(A\)，再求特征值和标准正交特征向量；比值最小值由最小特征值给出。
- card_decision: visual_candidate_enriched；缺用户本人具体错因，暂不新建 LA-120，不修改正式错题卡。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed

## 2026-07-01 update VISUAL-LA-LINEAR-EQUATION-5-1-5-2-PASS-010

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理线代第五讲强化例题 5.1 / 5.2 重复候选组。
- evidence: 5.1 组 `MN4-GS-CH01-717/719/722/724` 题图与解析图 SHA-256 完全一致；5.2 组 `MN4-GS-CH01-720/725` 题图与三张解析图 SHA-256 完全一致；父级路径均为线代强化第五讲-线性方程组。
- wiki_created: 错题知识网络/可视化错题详情/线性代数/LA-078_强化例题5.1-2.md；错题知识网络/可视化错题详情/线性代数/LA-081_强化例题5.2-2.md；以及对应题图/解析图资产。
- wiki_updated: 错题知识网络/错题卡/LA-078_强化例题5.1-2.md；错题知识网络/错题卡/LA-081_强化例题5.2-2.md；manifest.json；index.md；asset_to_obsidian.json；obsidian_open_links.md；wiki/index.md；MATHWIKI-QUESTIONS-002；MATHWIKI-LA-TOPIC-003。
- card_decision: update-existing-card；两题已有正式 LA 占位卡，本轮补全题目定位、标准答案、知识点、方法入口、陷阱和视觉详情；缺用户本人具体错因，wrong_point 保守标记为暂无明确错因，mastery_history 为待评分。
- wrongnet_rebuild: closeout ok，cards=763，strong=1684，medium=536，weak_audit=500；wiki coverage refresh success，source summaries=763，knowledge_clusters=325，method_clusters=664，error_clusters=256，action_gap_clusters=8；visual_bridge_refresh success，records=866，assets=1238；quality_gate=ok，ERROR none，WARN none。
- rollback_action: not_needed
- tutor_boundary: not_needed；本轮不复制完整题图或长解析到 Tutor safe source，不反写掌握度或回滚 JSON。

## 2026-07-01 closeout GS-647-84298-SCORE-POLICY

- input: 用户要求将 ID:84298 入库；复核发现该题已作为 `GS-647` 入库并完成视觉详情，但正式卡中此前写有 `AI评分 2.5/5`。
- source_refs: 错题知识网络/错题卡/GS-647_84298曲线法平面方程.md；错题知识网络/可视化错题详情/高等数学/GS-647_84298曲线法平面方程.md
- wiki_updated: 错题知识网络/错题卡/GS-647_84298曲线法平面方程.md；错题知识网络/wiki/log.md
- card_decision: keep-existing-card；保留 `GS-647`，不重复建卡；掌握度改为 `待评分`，原因是用户本轮没有给出 0-5 分。
- wrongnet_rebuild: closeout ok，cards=760，quality_gate=ok，ERROR none，WARN none。
- rollback_action: not_run
- missing_info: 掌握度 0-5 分待用户复做后确认。

## 2026-07-01 visual_source_merge GS-003-MN4-GS-CH01-003

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理候选页 `MN4-GS-CH01-003｜2 2026.3.11 T1`。
- evidence: 人工看图确认 `MN4-GS-CH01-003` 题图为含变上限积分、指数函数与三角函数差的 \(\infty-\infty\) 型极限；与 `GS-001` 的反三角幂式极限不是同题。旧卡 `GS-003` 为同来源占位卡，题干 OCR 待核对。
- source_refs: 错题知识网络/错题卡/GS-003_22026.3.11T1-2.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-003_2-2026.3.11-T1.md；错题知识网络/可视化错题详情/高等数学/GS-003_2-2026.3.11-T1-2.md
- wiki_created: 错题知识网络/可视化错题详情/高等数学/GS-003_2-2026.3.11-T1-2.md；错题知识网络/assets/visual_wrong_questions/GS-003/question_01.png；错题知识网络/assets/visual_wrong_questions/GS-003/solution_01.png
- wiki_updated: 错题知识网络/错题卡/GS-003_22026.3.11T1-2.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-003_2-2026.3.11-T1.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-008_高等数学综合待精分分流台.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/study_vaults/数学LLMWiki/tutor_setup_sources/数学LLMWiki安全输入包.md
- card_decision: update-existing-card；补强旧占位卡 `GS-003`，不新建卡；掌握度保守写 `待评分`，错因保守写 `暂无明确错因`，因为旧导入未记录用户本人作答过程。
- visual_quality_update: 将 `MN4-GS-CH01-003` 标记为 `merged_into_wrongnet -> GS-003`；新增 `VIS-GS-003` 正式视觉详情页，题图可见、解析图折叠。
- wrongnet_rebuild: closeout ok，cards=760，quality_gate=ok，ERROR none；WARN method_gap not enabled 是保守边界，因缺用户本人作答过程未启用 method_gap。
- rollback_action: not_run
- missing_info: 用户原始错因和 0-5 掌握度待复做后补充。

## 2026-07-01 visual_candidate_formalize GS-649-MN4-GS-CH01-025

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理候选页 `MN4-GS-CH01-025｜170768 2026.5.9 ✅`。
- evidence: 人工看图确认题目为无穷远处变上限积分极限；来源页虽然无单独解析图，但有完整解析文字和明确错因归纳：洛必达后没有拆开主导项 \(x^2\sin\frac1x\) 与有界扰动项 \(\sin\frac1x-\cos x\)。
- source_refs: 错题知识网络/错题卡/GS-649_170768变上限积分无穷远主导项拆分.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-025_170768-2026.5.9.md；错题知识网络/可视化错题详情/高等数学/GS-649_170768变上限积分无穷远主导项拆分.md
- wiki_created: 错题知识网络/错题卡/GS-649_170768变上限积分无穷远主导项拆分.md；错题知识网络/可视化错题详情/高等数学/GS-649_170768变上限积分无穷远主导项拆分.md；错题知识网络/assets/visual_wrong_questions/GS-649/question_01.png
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-025_170768-2026.5.9.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/study_vaults/数学LLMWiki/tutor_setup_sources/数学LLMWiki安全输入包.md
- card_decision: formalize-new-card；新建正式卡 `GS-649`；因来源页有明确用户错因归纳，启用 method_gap；因无用户 0-5 掌握度，mastery_history 保守写 `待评分`。
- visual_quality_update: 将 `MN4-GS-CH01-025` 标记为 `merged_into_wrongnet -> GS-649`；新增 `VIS-GS-649` 正式视觉详情页，题图可见，解析文字折叠。
- wrongnet_rebuild: closeout ok，cards=761，quality_gate=ok，ERROR none，WARN none。
- rollback_action: not_run
- tutor_boundary: 已加入高层“无穷远主导项拆分训练项”，未复制完整题干或长解析。

## 2026-07-01 visual_candidate_enrich MN4-GS-CH01-079

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理候选页 `MN4-GS-CH01-079｜58049 2026.4.22✅`。
- evidence: 人工看图确认题目为 \(\lim_{n\to\infty}\sum_{k=1}^{n}\frac1{4k^2-1}\)；来源页无单独解析图，但有标准复习思路，核心是平方差因式分解、部分分式裂项和望远镜求和。
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-079_58049-2026.4.22.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/wiki/index.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-007_数列极限错题总线.md
- card_decision: visual-candidate-enriched；缺用户本人具体错因，暂不新建正式 GS 卡；已确认不按数字 ID 硬合并 `GS-069`。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_needed
- tutor_boundary: not_needed；本轮只补高层候选复述，不复制完整题干或长解析到 Tutor safe source。

## 2026-07-01 visual_candidate_formalize GS-650-MN4-GS-CH01-200

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理候选页 `MN4-GS-CH01-200｜57838 2026.5.17✅`。
- evidence: 人工看图确认题目为星形线参数方程 \(x=a\cos^3t,\ y=a\sin^3t\) 在 \(t=\frac{\pi}{4}\) 处求曲率；来源页无单独解析图，但有完整解析文字和明确错因归纳：参数方程转普通函数求二阶导时漏掉 \(\frac{dt}{dx}\)。
- source_refs: 错题知识网络/错题卡/GS-650_57838参数曲线曲率链式求导.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-200_57838-2026.5.17.md；错题知识网络/可视化错题详情/高等数学/GS-650_57838参数曲线曲率链式求导.md
- wiki_created: 错题知识网络/错题卡/GS-650_57838参数曲线曲率链式求导.md；错题知识网络/可视化错题详情/高等数学/GS-650_57838参数曲线曲率链式求导.md；错题知识网络/assets/visual_wrong_questions/GS-650/question_01.png
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-200_57838-2026.5.17.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/study_vaults/数学LLMWiki/tutor_setup_sources/数学LLMWiki安全输入包.md
- card_decision: formalize-new-card；新建正式卡 `GS-650`；因来源页有明确错因归纳，启用 method_gap；因无用户 0-5 掌握度，mastery_history 保守写 `待评分`。
- visual_quality_update: 将 `MN4-GS-CH01-200` 标记为 `merged_into_wrongnet -> GS-650`；新增 `VIS-GS-650` 正式视觉详情页，题图可见，解析文字折叠。
- wrongnet_rebuild: closeout ok，cards=762，quality_gate=ok，ERROR none，WARN none。
- rollback_action: not_run
- tutor_boundary: 已加入高层“参数方程曲率训练项”，未复制完整题干或长解析。

## 2026-07-01 visual_source_merge GS-468-MN4-GS-CH01-518

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理候选页 `MN4-GS-CH01-518｜57977 2026.5.17`。
- evidence: 人工看图确认题图 ID 为 `57977`，题目与旧正式卡 `GS-468_579977隐函数二阶导代数整理.md` 完全同题；旧卡 source/title 多写了一个 `9`，且 method_gap 误挂到“凹凸、拐点”。
- source_refs: 错题知识网络/错题卡/GS-468_57977隐函数二阶导代数整理.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-518_57977-2026.5.17.md；错题知识网络/可视化错题详情/高等数学/GS-468_57977隐函数二阶导代数整理.md
- wiki_created: 错题知识网络/可视化错题详情/高等数学/GS-468_57977隐函数二阶导代数整理.md；错题知识网络/assets/visual_wrong_questions/GS-468/question_01.png
- wiki_updated: 错题知识网络/错题卡/GS-468_57977隐函数二阶导代数整理.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-518_57977-2026.5.17.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/study_vaults/数学LLMWiki/tutor_setup_sources/数学LLMWiki安全输入包.md
- card_decision: merge-existing-card；保留正式编号 `GS-468`，不新建卡；修正来源编号为 `57977`，并将 method_gap 改为 `B7-CALC` 运算路径不稳。
- visual_quality_update: 将 `MN4-GS-CH01-518` 标记为 `merged_into_wrongnet -> GS-468`；新增 `VIS-GS-468` 正式视觉详情页，题图可见，解析文字折叠入口保留在来源页。
- wrongnet_rebuild: needed_after_card_update
- rollback_action: not_run
- tutor_boundary: 已加入高层“隐函数二阶导代数整理训练项”，未复制完整题干或长解析。

## 2026-07-01 visual_method_link MN4-GS-CH01-090-compression-map

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮继续处理 `MN4-GS-CH01-090｜57718 2026.5.11`。
- evidence: 人工看图确认题图为抽象不动点/压缩映射证明题；`GS-058` 题图为具体递推 \(x_{n+1}=\sqrt{4+3x_n}\)，二者同属压缩映射/不动点方法但不是同一道题。`MN4-GS-CH01-090` 折叠解析仍串入 `GS-444/170684` 正切递推题。
- wiki_created: 错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-019_压缩映射不动点迭代.md
- wiki_updated: 错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-007_数列极限错题总线.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-090_57718-2026.5.11.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md
- card_decision: method-link-only；不新建正式卡，不并入 `GS-444`，也不硬合并 `GS-058`。
- wrongnet_rebuild: not_needed_visual_and_wiki_only
- rollback_action: not_needed

## 2026-07-01 visual_source_merge LA-019-MN4-GS-CH01-657

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；本轮处理 `MN4-GS-CH01-657｜强化例题2.1`。
- evidence: 人工看图确认题目为线性代数行列式与代数余子式题；旧正式卡 `LA-019_强化例题2.1-2.md` 为同题但答案/摘要不完整。`GS-058` 也是“强化例题2.1”但题图是高数压缩映射递推题，已排除同题合并。
- source_refs: 错题知识网络/错题卡/LA-019_强化例题2.1-2.md；错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-657_强化例题2.1.md；错题知识网络/可视化错题详情/线性代数/LA-019_强化例题2.1-2.md
- wiki_created: 错题知识网络/可视化错题详情/线性代数/LA-019_强化例题2.1-2.md；错题知识网络/wiki/topics/MATHWIKI-LA-TOPIC-005_行列式错题总线.md；错题知识网络/wiki/methods/MATHWIKI-LA-METHOD-001_代数余子式线性组合展开.md；错题知识网络/assets/visual_wrong_questions/LA-019/question_01.png
- wiki_updated: 错题知识网络/错题卡/LA-019_强化例题2.1-2.md；错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-657_强化例题2.1.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-LA-TOPIC-002_线代综合待精分分流台.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md
- card_decision: merge-existing-card；保留正式编号 `LA-019`，不新建卡；补全答案为 `a=4，b 为任意常数`；用户本人错因未提供，正式错因仍保留 `待补充`。
- visual_quality_update: 将 `MN4-GS-CH01-657` 标记为 `merged_into_wrongnet -> LA-019`；新增 `VIS-LA-019` 正式视觉详情页。
- wrongnet_rebuild: needed_after_card_update
- rollback_action: not_run

## 2026-07-01 visual_source_merge GS-257-MN4-GS-CH01-355

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理候选页 `MN4-GS-CH01-355｜强化例题7.1 2026.5.19`。
- evidence: 题图为高数相关变化率题，曲线 \(y=x^{3/2}\)、距离变化率 \(11\ \mathrm{cm/s}\)、求 \(x=3\) 时水平速度；与正式卡 `GS-257_强化例题7.1.md` 的相关变化率错因和 method_gap 一致。旧 `VIS-GS-257` 为线代错连证据，继续并入 `LA-021`，不覆盖。
- source_refs: 错题知识网络/错题卡/GS-257_强化例题7.1.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-355_强化例题7.1-2026.5.19.md；错题知识网络/可视化错题详情/高等数学/GS-257_强化例题7.1距离变化率.md
- wiki_created: 错题知识网络/可视化错题详情/高等数学/GS-257_强化例题7.1距离变化率.md；错题知识网络/assets/visual_wrong_questions/GS-257/question_02.png
- wiki_updated: 错题知识网络/错题卡/GS-257_强化例题7.1.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-355_强化例题7.1-2026.5.19.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md
- card_decision: merge-existing-card；保留正式编号 `GS-257`，不新建卡；补正确题图和标准答案 `4 cm/s`。
- visual_quality_update: 将 `MN4-GS-CH01-355` 标记为 `merged_into_wrongnet -> GS-257`；新增 `VIS-GS-257-CORRECT` 正确视觉详情页；旧 `VIS-GS-257` 继续作为 `LA-021` 错连证据。
- wrongnet_rebuild: closeout ok，cards=762，strong=1677，medium=536，weak_audit=500；wiki coverage refresh success，source summaries=762，knowledge_clusters=324，method_clusters=662，error_clusters=255，action_gap_clusters=8；visual_bridge_refresh success，records=865，assets=1236；quality_gate=ok，ERROR none，WARN none。
- rollback_action: not_run
- tutor_boundary: not_needed；未复制完整题图或长解析到 Tutor safe source。

## 2026-07-01 update GS-647-84298-SCORE-POLICY-RECONCILE

- input: 用户再次要求将 ID:84298 入库；复核发现该题已作为 `GS-647` 入库，且用户已经明确说明“没有找到求法平面入口”“不理解默认 \(x=x\) 参数化”“把切线点向式当作法平面公式”。
- source_refs: 错题知识网络/错题卡/GS-647_84298曲线法平面方程.md；错题知识网络/AI维护规则.md；错题知识网络/可视化错题详情/高等数学/GS-647_84298曲线法平面方程.md
- wiki_updated: 错题知识网络/错题卡/GS-647_84298曲线法平面方程.md；错题知识网络/wiki/log.md
- card_decision: keep-existing-card；不重复建卡，保留 `GS-647`；按项目内最新 `AI维护规则.md` 的 2026-06-28 后默认 AI 评分规则，将掌握度从 `待评分` 修正为 `AI评分 2/5`。
- conflict_resolution: 用户全局说明中有“掌握度只能由用户给出”，但项目内规则明确要求在用户提供作答过程和错因证据时由 AI 给 0-5 分；本次采用项目内最新规则。
- wrongnet_rebuild: closeout ok，cards=762，strong=1677，medium=536，weak_audit=500；wiki coverage refresh success，source summaries=762，knowledge_clusters=324，method_clusters=662，error_clusters=255，action_gap_clusters=8；visual_bridge_refresh success，records=865，assets=1236；quality_gate=ok，ERROR none，WARN none。
- rollback_action: not_run

## 2026-07-01 visual_wiki_index_sync MERGED-SOURCE-LINKS

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮修复视觉详情、Obsidian 跳转索引与 wiki 专题总线之间的状态不一致。
- evidence: `manifest.json` 中 `merged_into_wrongnet` 记录已有正式目标，但部分 `wrongnet_id` 仍停留在 `待确认`；`MATHWIKI-GS-TOPIC-006`、`MATHWIKI-GS-TOPIC-007`、`MATHWIKI-LA-TOPIC-001` 页内已补视觉候选，`wiki/index.md` 仍缺对应来源。
- wiki_updated: 错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-007_数列极限错题总线.md；错题知识网络/wiki/log.md
- visual_quality_update: 已将 108 条 `merged_into_wrongnet` 视觉来源同步到正式 `wrongnet_id`，并刷新 107 个详情页 frontmatter、107 条可视化索引、107 条 Obsidian 打开链接和 184 条资产映射；同步后 `merged_into_wrongnet` 且 `wrongnet_id=待确认` 的记录为 0。
- card_decision: visual-index-sync-only；不新建正式卡，不把仍缺用户本人错因的视觉候选强行正式化。
- wrongnet_rebuild: not_needed_visual_index_and_wiki_only；本轮未改正式错题卡。
- visual_bridge_refresh: success，records=865，assets=1236。
- remaining_candidates: `needs_card_decision=6`，`needs_manual_relink=1`，需补用户本人错因或正确解析后再决定是否正式入库。
- rollback_action: not_run
- manual_relink_guard: 已将 `MN4-GS-CH01-090` 的折叠块从“解析”改为“疑似串题解析（不作为本题解析）”，避免把 `170684/GS-444` 正切递推解析误当成 `57718` 不动点题解析。

## 2026-07-01 visual_detail_subject_path_repair LINEAR-ALGEBRA-CANDIDATES

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；本轮发现 3 个线性代数视觉候选的 `subject` 已标为线性代数，但详情页仍位于 `可视化错题详情/高等数学/`。
- evidence: `MN4-GS-CH01-670` 为线代二次型参数与规范形，`MN4-GS-CH01-683` 为二次型正交变换与 Rayleigh 商，`MN4-GS-CH01-748` 为可交换矩阵与相似对角化关系判断；三者均不应继续挂在高数详情目录下。
- wiki_updated: 错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-670_2018年数学2第22题.md；错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-683_2022年22题.md；错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-748_2024年选择题第10题.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md；错题知识网络/wiki/topics/MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md；错题知识网络/wiki/log.md
- card_decision: subject-path-repair-only；仍保持 `visual_candidate_enriched` / `needs_card_decision`，不因学科路径修复而新建正式错题卡。
- wrongnet_rebuild: not_needed_visual_path_and_wiki_only；本轮未修改正式错题卡。
- rollback_action: not_run
- followup_sync: 已补齐 `MATHWIKI-LA-TOPIC-004` 的页头 `wrongnet_refs` 与 `knowledge`，使两个二次型视觉候选和 `wiki/index.md` 保持一致。

## 2026-07-01 visual_candidate_method_pages GS079-GS102-LA670

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理 3 个仍缺用户本人错因、但方法入口稳定的视觉候选。
- evidence: `MN4-GS-CH01-079` 的解析文字稳定指向“平方差分母 -> 部分分式裂项 -> 望远镜求和”；`MN4-GS-CH01-102` 的题图/解析图复述稳定指向“发散数列经函数变换，先判一一性并构造同值反例”；`MN4-GS-CH01-670` 的题图/解析图复述稳定指向“平方和二次型先令每个平方项为零，再按参数讨论规范形”。
- wiki_created: 错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-021_裂项望远镜求和.md；错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-022_发散数列函数变换反例.md；错题知识网络/wiki/methods/MATHWIKI-LA-METHOD-004_平方和二次型参数规范形.md
- wiki_updated: 错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-007_数列极限错题总线.md；错题知识网络/wiki/topics/MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-079_58049-2026.4.22.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-102_2024年选择题第四题.md；错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-670_2018年数学2第22题.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/log.md
- card_decision: method-page-only；三题仍保持 `visual_candidate_enriched` / `needs_card_decision`，不因方法页完成而正式入库。
- wrongnet_rebuild: not_needed_wiki_and_visual_only；本轮未修改正式错题卡。
- rollback_action: not_run

## 2026-07-01 visual_manual_relink_audit MN4-GS-CH01-090-raw-oo3

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；本轮复核 `MN4-GS-CH01-090｜57718 2026.5.11` 的原始 OO3 证据。
- source_refs: `/Users/xiazhibin/Library/Containers/QReader.MarginStudy.easy/Data/Documents/ExportedOmniOutlinerFiles/考研高数(2026-06-30-20-10-36).oo3/contents.xml`；`864e3f7ceba300714614eb1cea908e15.png`；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-090_57718-2026.5.11.md
- evidence: 原始包中 `57718 2026.5.11` 节点存在，题图 refid 与本页题图一致；但该节点唯一子节点为 `ID:170684` 正切递推解析，相邻节点未发现 57718 的正确解析。
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-090_57718-2026.5.11.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-002_可视化错题候选决策队列.md；错题知识网络/wiki/log.md
- card_decision: keep-needs-manual-relink；不新建正式卡，不并入 `GS-444`，也不并入 `GS-058`。
- wrongnet_rebuild: not_needed_visual_audit_only
- rollback_action: not_run
- missing_info: `57718` 的正确解析和用户本人错因仍缺失。

## 2026-07-01 visual_source_path_remap MN4-GS-CH01-EXPORTS

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；本轮全库审计发现早期视觉详情页和 wiki 索引仍指向已不存在的 Desktop 导出路径。
- source_refs: `/Users/xiazhibin/Library/Containers/QReader.MarginStudy.easy/Data/Documents/ExportedOmniOutlinerFiles/考研高数(2026-06-30-20-10-36).oo3/`；`/Users/xiazhibin/Library/Containers/QReader.MarginStudy.easy/Data/Documents/考研高数(2026-06-30-20-10-28).docx`
- evidence: 旧路径 `/Users/xiazhibin/Desktop/数学第一章/考研高数(2026-06-30-20-10-36).oo3/` 与 `/Users/xiazhibin/Desktop/数学第一章/考研高数(2026-06-30-20-10-28).docx` 当前均不存在；同名 OO3 与 DOCX 在 MarginStudy 容器目录中可访问。
- wiki_updated: 错题知识网络/可视化错题详情/*.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/index.md；错题知识网络/wiki/index.md；错题知识网络/wiki/log.md
- visual_quality_update: 将视觉详情层和 wiki 索引中的原始导出路径重映射到当前可访问位置，增强题图/解析来源追溯；历史日志旧 source_refs 不回写篡改，只记录本次 remap。
- card_decision: visual-source-traceability-only；不新建正式卡，不修改正式错题卡。
- wrongnet_rebuild: not_needed_visual_and_wiki_only
- rollback_action: not_run

## 2026-07-01 closeout GS-647-84298-STABLE-SOURCE-REFS

- input: 用户再次要求将 ID:84298 入库，并补充错因：没有找到求法平面入口，不理解默认 \(x=x\) 参数化，把切线点向式误认为法平面公式。
- source_refs: 错题知识网络/错题卡/GS-647_84298曲线法平面方程.md；错题知识网络/可视化错题详情/高等数学/GS-647_84298曲线法平面方程.md；错题知识网络/assets/visual_wrong_questions/GS-647/question_01.png；错题知识网络/assets/visual_wrong_questions/GS-647/solution_01.png
- wiki_updated: 错题知识网络/错题卡/GS-647_84298曲线法平面方程.md；错题知识网络/wiki/log.md
- card_decision: keep-existing-card；该题已作为 `GS-647` 正式入库，本轮不重复建卡；正式卡内容已覆盖“参数化入口缺失”和“切线方程/法平面方程混淆”，仅将 `lecture_refs` 从 PixPin 临时截图路径改为库内稳定视觉详情和资产路径。
- wrongnet_rebuild: success，cards=762，strong=1677，medium=536，weak_audit=500；related GS-647 已召回 GS-627、GS-629、GS-646 等强关联题；knowledge `空间曲线切线与法平面` 命中 GS-646、GS-647。
- visual_bridge_refresh: success，records=865，assets=1236。
- rollback_action: not_run

## 2026-07-01 visual_wiki_wrongnet_link_repair PATH-ALIASES

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；本轮审计发现视觉详情页和 wiki 页中存在大量 `[[GS-xxx]]`、`[[LA-xxx]]`、`[[PR-xxx]]` 形式的短 wrongnet 双链。
- evidence: 正式错题卡文件名均为 `错题知识网络/错题卡/{ID}_标题.md`，且错题卡未设置 `aliases`；短双链在 Obsidian 中可能无法稳定解析到真实卡片。审计确认 1070 个短链均能唯一匹配到一个正式错题卡文件，无 unresolved / ambiguous 匹配。
- wiki_updated: 错题知识网络/可视化错题详情/*.md；错题知识网络/wiki/*.md；错题知识网络/wiki/log.md
- navigation_update: 将 858 个视觉/wiki 页面中的 1070 个短 wrongnet 双链统一改为 `[[错题知识网络/错题卡/{ID}_标题|{ID}]]`，保留原显示文本但指向真实卡片路径。
- card_decision: navigation-only；不新建正式卡，不修改正式错题卡，不修改回滚 JSON。
- wrongnet_rebuild: not_needed_visual_and_wiki_navigation_only
- validation: 短 wrongnet 双链剩余 0；路径别名链接 1070；缺失目标 0。
- rollback_action: not_run

## 2026-07-01 visual_detail_source_summary_links SRC-WQ-BRIDGE

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；上一轮已修复视觉详情到正式错题卡的路径别名，本轮继续补齐视觉详情到正式卡 source summary 的证据链。
- evidence: 审计发现 858 个 `linked_wrongnet` / `merged_into_wrongnet` 视觉详情页都缺少 `SRC-WQ-{ID}` 链接；对应 `错题知识网络/wiki/sources/wrong_cards/SRC-WQ-{ID}.md` 文件均存在。
- wiki_updated: 错题知识网络/可视化错题详情/*.md；错题知识网络/wiki/log.md
- navigation_update: 为 858 个已正式关联的视觉详情页补入 `source summary：[[错题知识网络/wiki/sources/wrong_cards/SRC-WQ-{ID}|SRC-WQ-{ID}]]`；同时为唯一缺稳定 formal-card 路径的 `MN4-GS-CH01-657 -> LA-019` 补入 `wrongnet card` 路径别名。
- card_decision: navigation-and-evidence-chain-only；不新建正式卡，不修改正式错题卡，不修改回滚 JSON。
- wrongnet_rebuild: not_needed_visual_navigation_only
- validation: linked_or_merged=858；missing_wrongnet_path_link=0；missing_source_summary_link=0；missing_source_summary_target=0。
- rollback_action: not_run

## 2026-07-01 visual_detail_deep_wiki_links SRC-WQ-DEEP-REFS

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；本轮在视觉详情已连到 `SRC-WQ-{ID}` 的基础上，继续补齐到高层方法页、专题页、错因页、触发页或概念页的直达入口。
- evidence: 审计发现 858 个 `linked_wrongnet` / `merged_into_wrongnet` 视觉详情页中仍有 838 个缺少 deep wiki 链接；对应 `SRC-WQ-{ID}` 的 `wiki_refs` 已包含现有 deep wiki 编译结果。
- wiki_updated: 错题知识网络/可视化错题详情/*.md；错题知识网络/wiki/log.md
- navigation_update: 从对应 `SRC-WQ-{ID}` 中提取已存在且目标文件可解析的 `MATHWIKI-{GS|LA|PR}-{METHOD|TOPIC|ERROR|TRIGGER|CONCEPT}-*` 链接，为 838 个视觉详情页补入 `deep wiki` 行；优先方法页和专题页，排除无目标文件的链接。
- card_decision: visual-wiki-navigation-only；不新建正式卡，不修改正式错题卡，不修改回滚 JSON。
- wrongnet_rebuild: not_needed_visual_navigation_only
- validation: linked_or_merged_details=858；details_missing_deep_refs=0；details_with_deep_wiki_line=838；deep_links_total=2515；missing_deep_targets=0。
- rollback_action: not_run
## 2026-07-01 visual_gap_queue MATHWIKI-QUESTIONS-003

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮把剩余视觉候选和正式卡缺图状态整理成独立收口队列。
- evidence: manifest 当前为 865 条视觉记录，其中 linked_wrongnet=728、merged_into_wrongnet=130、needs_card_decision=6、needs_manual_relink=1；`SRC-WQ-*` source summary 中仍有 34 张正式错题卡缺 `visual_detail_refs`。
- wiki_created: 错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md
- wiki_updated: 错题知识网络/wiki/index.md；错题知识网络/wiki/log.md
- card_decision: queue-only；不新建正式卡，不将缺用户本人错因的视觉候选强行入库。
- wrongnet_rebuild: not_needed_wiki_queue_only
- rollback_action: not_run

## 2026-07-01 visual_gap_auto_match_audit C-QUEUE

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；本轮复查 `MATHWIKI-QUESTIONS-003` 中 C 队列 34 张“正式错题卡缺可视化详情”是否存在可自动接线证据。
- evidence: 逐项对照 `manifest.json`、`assets/visual_wrong_questions/`、`可视化错题详情/` 和 `obsidian_open_links.md`；34 张卡的 `wrongnet_id`、`VIS-{ID}`、资产目录、详情页和打开链接均为 0 命中。
- wiki_updated: 错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md；错题知识网络/wiki/log.md
- card_decision: no-auto-merge；没有安全自动接线项，后续必须补原题图、解析图、MarginNote 正确节点或用户截图后再补视觉入口。
- wrongnet_rebuild: not_needed_wiki_audit_only
- rollback_action: not_run

## 2026-07-01 visual_candidate_closure_prompts A-B-QUEUE

- input: 持续目标要求根据题图、解析和图片进一步加强错题网络质量；本轮处理 `MATHWIKI-QUESTIONS-003` 的 6 个 A 队列视觉候选和 1 个 B 队列人工重连候选。
- update: 在 `MN4-GS-CH01-079`、`MN4-GS-CH01-102`、`MN4-GS-CH01-418`、`MN4-GS-CH01-670`、`MN4-GS-CH01-683`、`MN4-GS-CH01-748`、`MN4-GS-CH01-090` 详情页补入本页 HTTP bridge 入口和“候选转正式卡前需要用户补充”的问题。
- boundary: 只记录候选收口问题，不凭解析编造用户本人错因、不创建正式卡、不更新掌握度、不修改回滚 JSON。
- wiki_updated: 错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-079_58049-2026.4.22.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-102_2024年选择题第四题.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-418_2024年19题.md；错题知识网络/可视化错题详情/高等数学/MN4-GS-CH01-090_57718-2026.5.11.md；错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-670_2018年数学2第22题.md；错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-683_2022年22题.md；错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-748_2024年选择题第10题.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md；错题知识网络/wiki/log.md
- wrongnet_rebuild: not_needed_visual_wiki_only
- rollback_action: not_run

## 2026-07-01 visual_manifest_structure_audit BASELINE-865

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮对 `manifest.json` 中 865 条视觉详情记录做结构巡检。
- audit_result: 缺详情页 0；缺资产 0；题图未嵌入详情页 0；登记了解析图但未折叠 0；`wrongnet_id` 指向不存在正式卡 0；候选状态却绑定正式 `wrongnet_id` 0。
- decision: 当前高风险结构问题为 0；剩余缺口属于证据边界而非文件结构错误，即 A 队列缺用户本人错因、B 队列缺正确解析、C 队列缺原图入口。
- wiki_updated: 错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md；错题知识网络/wiki/log.md
- wrongnet_rebuild: not_needed_readonly_audit_plus_wiki_log
- rollback_action: not_run

## 2026-07-01 spatial_geometry_entry_contrast GS-645-646-647

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮聚焦第 17 讲空间解析几何新近入库的 `GS-645`、`GS-646`、`GS-647`。
- update: 在 `MATHWIKI-GS-TOPIC-012_空间解析几何错题总线.md` 新增“最近三题入口判别”表，区分空间交线投影消元、参数曲线切线点向式、空间曲线法平面点法式三类入口。
- visual_updated: 在 `VIS-GS-645`、`VIS-GS-646`、`VIS-GS-647` 的连线建议中补入专题总线和邻近题 HTTP bridge 链接，强化横向复做召回。
- boundary: 不修改正式错题卡，不改掌握度，不新增错因；只补 wiki/visual 层的复做入口对照。
- wrongnet_rebuild: not_needed_visual_wiki_only
- rollback_action: not_run

## 2026-07-01 source_summary_h17_refs GS-646-GS-647

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮复查第 17 讲知识树 source summary 覆盖。
- update: `SRC-KTREE-H17_多元函数积分学预备知识树.md` 补入 `GS-626` 至 `GS-647` 的已接入错题表，并把 `GS-646`、`GS-647` 补进 frontmatter 与总 `wiki/index.md` 的 `SRC-SUMMARY-KTREE-H17` 行。
- boundary: 只更新 source summary 和 wiki index/log，不修改正式错题卡、不刷新生成目录。
- wrongnet_rebuild: not_needed_wiki_source_summary_only
- rollback_action: not_run

## 2026-07-01 visual_detail_http_bridge_backfill linked-728

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮审计 728 个 `linked_wrongnet` 视觉详情页的 Codex 可点击入口。
- audit_before: 728 个 `linked_wrongnet` 详情页均已有正式卡 wikilink 和 `SRC-WQ-*` 链接，但缺 `http://127.0.0.1:8765/open/{ID}` 形式的本题入口。
- update: 对 728 个已连正式卡的视觉详情页，在 `wrongnet` 行后补入 `- 本题入口：[ID](http://127.0.0.1:8765/open/ID)`。
- audit_after: linked_count=728；missing_bridge=0；duplicate_bridge=0；mismatched_bridge=0；bridge snapshot refresh ok，records=865，assets=1236。
- boundary: 只做视觉详情页导航增强，不修改正式错题卡、不改生成目录、不改回滚 JSON、不改变错因/知识点/掌握度。
- wrongnet_rebuild: not_needed_visual_only
- rollback_action: not_run

## 2026-07-01 intake GS-651-84887-CYLINDER-SURFACE

- input: 用户提供题图与解析图，要求记录“证明曲面为柱面”的方法，并将 ID:84887 正式错题入库。
- source_refs: `/Users/xiazhibin/Library/Application Support/PixPin/Temp/PixPin_2026-07-01_12-33-52.png`；`/var/folders/5k/93syh_hn3rq0wyyh6m2bxlq80000gn/T/codex-clipboard-7d1bc85b-ec65-4d88-abd8-8c9c420b3799.png`；错题知识网络/错题卡/GS-651_84887曲面柱面判定.md；错题知识网络/可视化错题详情/高等数学/GS-651_84887曲面柱面判定.md
- wiki_created: 错题知识网络/错题卡/GS-651_84887曲面柱面判定.md；错题知识网络/可视化错题详情/高等数学/GS-651_84887曲面柱面判定.md；错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-023_曲面柱面定向量判定.md；错题知识网络/assets/visual_wrong_questions/GS-651/question_01.png；错题知识网络/assets/visual_wrong_questions/GS-651/solution_01.png
- wiki_updated: 错题知识网络/知识点库.md；错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-012_空间解析几何错题总线.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/study_vaults/数学LLMWiki/tutor_setup_sources/数学LLMWiki安全输入包.md
- card_decision: formal-card；新建 `GS-651`，具体错点为不知道柱面证明动作链：任取点、求法向量、找与所有法向量垂直的定向量。
- visual_quality_update: 新建 `VIS-GS-651`，题图可见、解析图折叠；manifest/index/open link/asset map 已登记。
- wrongnet_rebuild: needed_after_card_update
- rollback_action: not_run
- tutor_boundary: 已加入高层“曲面柱面判定训练项”，未复制完整题干或长解析。

## 2026-07-01 intake GS-657-171552-MAX-DIRECTIONAL-DERIVATIVE-PROPORTION

- input: 用户提供题图与解析图，要求将 ID:171552 正式入库；用户错解为已能用方向向量单位化和点乘式推出 \(a+b=5\)，但比例条件误比较 \((a,b)\) 与 \(l=(1,2)\)。
- source_refs: `/Users/xiazhibin/Library/Application Support/PixPin/Temp/PixPin_2026-07-01_16-09-33.png`；`/var/folders/5k/93syh_hn3rq0wyyh6m2bxlq80000gn/T/codex-clipboard-03bfbaf9-5d59-48a9-ae6f-41ecac3be972.png`；错题知识网络/错题卡/GS-657_171552最大方向导数比例条件.md；错题知识网络/可视化错题详情/高等数学/GS-657_171552最大方向导数比例条件.md
- wiki_created: 错题知识网络/错题卡/GS-657_171552最大方向导数比例条件.md；错题知识网络/可视化错题详情/高等数学/GS-657_171552最大方向导数比例条件.md；错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-029_最大方向导数比例条件.md；错题知识网络/assets/visual_wrong_questions/GS-657/question_01.png；错题知识网络/assets/visual_wrong_questions/GS-657/solution_01.png
- wiki_updated: 错题知识网络/知识点库.md；错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md；错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-025_最大方向导数梯度模.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/study_vaults/数学LLMWiki/tutor_setup_sources/数学LLMWiki安全输入包.md；错题知识网络/wiki/log.md
- card_decision: formal-card；新建 `GS-657`，具体错点为只用点乘式得到一个数值方程后，漏用“最大方向即梯度方向”的同向比例条件，并把参数向量误当成梯度向量。
- visual_quality_update: 新建 `VIS-GS-657`，题图可见、解析图折叠；manifest/index/open link/asset map 已结构化刷新。
- wrongnet_rebuild: done_by_intake_closeout；quality_gate=ok
- rollback_action: not_run
- tutor_boundary: 已加入高层“最大方向导数比例条件训练项”，未复制完整题干或长解析。

## 2026-07-01 intake GS-658-171556-BIVARIATE-SECOND-TAYLOR

- input: 用户提供题图与解析图，要求将 ID:171556 正式入库；用户错点是能看出 \(f(0,0)=1\)，但不知道二元函数在一点处的二阶泰勒展开公式该怎么写。
- source_refs: `/Users/xiazhibin/Library/Application Support/PixPin/Temp/PixPin_2026-07-01_16-28-58.png`；`/var/folders/5k/93syh_hn3rq0wyyh6m2bxlq80000gn/T/codex-clipboard-8f092a6c-f35a-42ee-9da7-cf2c0475f628.png`；错题知识网络/错题卡/GS-658_171556二元二阶泰勒公式.md；错题知识网络/可视化错题详情/高等数学/GS-658_171556二元二阶泰勒公式.md
- wiki_created: 错题知识网络/错题卡/GS-658_171556二元二阶泰勒公式.md；错题知识网络/可视化错题详情/高等数学/GS-658_171556二元二阶泰勒公式.md；错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-030_二元二阶泰勒展开格式.md；错题知识网络/assets/visual_wrong_questions/GS-658/question_01.png；错题知识网络/assets/visual_wrong_questions/GS-658/solution_01.png
- wiki_updated: 错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/wiki/study_vaults/数学LLMWiki/tutor_setup_sources/数学LLMWiki安全输入包.md；错题知识网络/wiki/log.md
- card_decision: formal-card；新建 `GS-658`，具体错点为没有先写 \(h=x-x_0,k=y-y_0\) 和二元二阶泰勒固定结构，尤其不熟悉 \(h^2,hk,k^2\) 三个二阶项、交叉项系数 2 与整体 \(\frac12\)。
- visual_quality_update: 新建 `VIS-GS-658`，题图可见、解析图折叠；manifest/index/open link/asset map 已结构化刷新。
- wrongnet_rebuild: needed_after_card_update
- rollback_action: not_run
- tutor_boundary: 已加入高层“二元二阶泰勒公式训练项”，未复制完整题干或长解析。

## 2026-07-01 visual_mismatch_demote_GS426_GS429

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮处理 `GS-426` 至 `GS-429` 的视觉详情错连风险。
- evidence: 正式卡 `GS-426` 至 `GS-429` 均为高数导数定义旧卡；对应视觉页题图、解析图和 MarginNote 父级路径均为线代第三讲矩阵运算内容。已抽查 `GS-426` 题图为实矩阵转置/对称性证明，`GS-429` 题图为矩阵幂/逆矩阵计算。
- wiki_updated: 错题知识网络/可视化错题详情/manifest.json；错题知识网络/可视化错题详情/index.md；错题知识网络/可视化错题详情/obsidian_open_links.md；错题知识网络/可视化错题详情/asset_to_obsidian.json；错题知识网络/wiki/sources/wrong_cards/SRC-WQ-GS-426.md；SRC-WQ-GS-427.md；SRC-WQ-GS-428.md；SRC-WQ-GS-429.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md；错题知识网络/wiki/log.md
- card_decision: suspect_wrongnet_mismatch；4 个视觉页保留为错连证据，`wrongnet_id` 置为待确认，不再作为 `GS-426` 至 `GS-429` 正式视觉入口；4 张正式卡进入“缺正确视觉详情”队列。
- bridge_refresh: success，records=873，assets=1253。
- wrongnet_rebuild: not_needed_visual_wiki_only；正式错题卡未修改。
- rollback_action: not_run。

## 2026-07-01 direction_derivative_entry_contrast GS-652-657

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮复查近期方向导数/梯度链 `GS-652`、`GS-653`、`GS-654`、`GS-656`、`GS-657`。
- evidence: 5 张正式卡和视觉详情均已通过 `intake_quality_gate.py --visual expected`；它们共同问题不是单个公式缺失，而是“普通求值、最大值、反推梯度、存在性、含参最大比例条件”五类题面信号容易混用。
- wiki_updated: 错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md；错题知识网络/wiki/log.md
- update: 在 `MATHWIKI-GS-TOPIC-010` 新增“近期方向导数五题入口判别”表，用 HTTP bridge 链接直接连到 `GS-652`、`GS-653`、`GS-654`、`GS-656`、`GS-657`，并逐题标明第一动作、比较对象和对应方法页。
- card_decision: wiki-only；不新增正式卡，不修改正式错题卡，不改变掌握度。
- wrongnet_rebuild: not_needed_wiki_only
- rollback_action: not_run。

## 2026-07-01 visual_detail_navigation_closure linked-and-merged-862

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮全量审计已正式关联的视觉详情页导航链。
- audit_before: `manifest.json` 当前 873 条视觉记录；其中 `linked_wrongnet=732`、`merged_into_wrongnet=130`。862 个 `linked_wrongnet` / `merged_into_wrongnet` 详情页中，130 个已合并来源页缺标准 `本题入口` 行，28 个详情页缺统一 `deep wiki` 行；正式卡路径链接和 `SRC-WQ-*` 链接均已存在。
- wiki_updated: 错题知识网络/可视化错题详情/*.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md；错题知识网络/wiki/log.md
- navigation_update: 为 130 个 `merged_into_wrongnet` 详情页补入 `- 本题入口：[ID](http://127.0.0.1:8765/open/ID)`；为 28 个已正式关联详情页补入 `deep wiki` 行，链接只指向已存在的方法页、专题页、错因页、触发页或概念页，不把自动 cluster 页当作深度编译完成。
- validation: linked_or_merged=862；missing_detail=0；missing_bridge=0；bad_bridge=0；duplicate_bridge=0；missing_source_summary_link=0；missing_source_summary_target=0；missing_deep_line=0；missing_deep_target=0；bridge snapshot refresh ok，records=873，assets=1253。
- card_decision: visual-wiki-navigation-only；不新建正式卡，不修改正式错题卡，不改变错因、知识点、掌握度或回滚复习。
- wrongnet_rebuild: not_needed_visual_wiki_navigation_only
- rollback_action: not_run

## 2026-07-01 visual_detail_subject_path_repair LA-merged-103

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮审计 `linked_wrongnet` / `merged_into_wrongnet` 视觉详情页的 subject、目录路径和正式卡 `subject` 是否一致。
- audit_before: 862 个已正式关联视觉记录中发现 104 个 subject/path 不一致项；其中 103 个为已确认并入 `LA-*` 正式卡的来源详情页仍放在 `可视化错题详情/高等数学/`，1 个为 `MN4-GS-CH01-236 -> PR-001` 的语义归类疑点。
- wiki_updated: `错题知识网络/可视化错题详情/线性代数/MN4-GS-CH01-*.md` 来源页迁移 103 个；同步更新 `manifest.json`、`asset_to_obsidian.json`、`obsidian_open_links.md`、`可视化错题详情/index.md`、相关正式卡 `lecture_refs`、wiki/source summary 引用和 `MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md`。
- card_decision: path-repair-only；未新建错题卡，未改变正式错因、知识点、掌握度、answer、method_gap 或回滚复习；`PR-001` 保留为待确认语义归类疑点，不自动改正式学科归属。
- validation: 修复后详情页缺失 0；线代 merged 来源页仍留在高数目录 0；已正式关联记录的 subject/path 不一致仅剩 `MN4-GS-CH01-236 -> PR-001` 这一条待确认项。
- wrongnet_rebuild: success，cards=770，strong=1713，medium=534，weak_audit=500；随后刷新 wrong-card source summaries、knowledge clusters、pattern clusters 和 bridge snapshot。
- bridge_refresh: success，records=873，assets=1253。
- rollback_action: not_run。

## 2026-07-01 formal_card_frontmatter_yaml_repair 32-cards

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮在学科路径审计后继续检查正式错题卡结构化 frontmatter。
- audit_before: 770 张正式错题卡中有 32 张 YAML frontmatter 不能被标准解析器读取，主要原因是 LaTeX 反斜杠、冒号、`-` 开头文本或 `& 方法/& 解法` 导入噪声未做 YAML 安全写法。
- wiki_updated: 32 张正式错题卡 frontmatter 语法修复；`GS-144`、`GS-260`、`GS-262` 清理 `& 方法/& 解法` 噪声知识点；`错题知识网络/知识点库.md` 补入 `相关变化率`；`MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md` 登记本轮审计结果。
- card_decision: syntax-and-tag-repair-only；不重写题目正文、不新建或合并正式卡、不修改掌握度、不改回滚 JSON；`PR-001` 的高数/概率论语义归类疑点仍保留待确认。
- validation: YAML frontmatter 解析错误 32 -> 0；ID 前缀与 `subject` 硬冲突 0；视觉 subject/path 不一致仍仅剩 `MN4-GS-CH01-236 -> PR-001` 这一项。
- wrongnet_rebuild: success，cards=770，strong=1714，medium=535，weak_audit=500；随后刷新 wrong-card source summaries、knowledge clusters、pattern clusters 和 bridge snapshot。
- bridge_refresh: success，records=873，assets=1253。
- rollback_action: not_run。

## 2026-07-01 formal_card_lecture_refs_stabilization 56-cards

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮检查正式卡 `lecture_refs` 是否仍依赖 PixPin Temp 或 `/var/folders/` 临时截图路径。
- audit_before: 56 张已有 manifest 可视化详情与稳定图片资产的正式卡，`lecture_refs` 仍只挂临时截图路径，导致长期追溯依赖本机临时文件。
- wiki_updated: 56 张正式错题卡的 `lecture_refs`；`MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md`；`错题知识网络/wiki/log.md`。
- update: 将 56 张正式卡的临时截图引用替换/补入为 `错题知识网络/可视化错题详情/.../*.md` 与 `错题知识网络/assets/visual_wrong_questions/{ID}/question_*.png`、`solution_*.png`，并保留原有知识树、方法卡、主题卡等非临时引用。代表性入口包括 `GS-629`、`GS-638`、`GS-645`、`GS-646`。
- card_decision: reference-stabilization-only；不修改题目摘要、答案、错因、知识点、掌握度、`method_gap` 或回滚复习。
- validation: YAML frontmatter 解析错误 0；正式卡 `lecture_refs` 临时截图路径 56 -> 0；稳定引用目标文件缺失 0；HTTP bridge 抽查 `GS-646`、`GS-629`、`GS-647` 均返回 200。
- wrongnet_rebuild: success，cards=770，strong=1714，medium=535，weak_audit=500；随后刷新 wrong-card source summaries、knowledge clusters、pattern clusters 和 bridge snapshot。
- bridge_refresh: success，records=873，assets=1253。
- rollback_action: not_run。

## 2026-07-01 formal_card_lecture_refs_missing_target_repair 11-cards

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮在临时路径清理后继续检查所有正式卡 `lecture_refs` 的本地目标是否真实存在。
- audit_before: 库内相对引用缺失 0；绝对路径引用缺失 17，涉及 `GS-605` 至 `GS-610`、`GS-648`、`GS-649`、`GS-650`、`LA-021`、`LA-098` 共 11 张正式卡。
- wiki_updated: 11 张正式错题卡的 `lecture_refs`；`MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md`；`错题知识网络/wiki/log.md`。
- update: 删除不存在的 `.claude/image-cache` 与旧 `.oo3` 绝对路径，并补入 manifest 中已确认的稳定可视化详情页、题图和解析图资产。
- card_decision: missing-reference-repair-only；不修改题目摘要、答案、错因、知识点、掌握度、`method_gap` 或回滚复习。
- validation: YAML frontmatter 解析错误 0；库内相对引用缺失 0；绝对路径引用缺失 17 -> 0。
- wrongnet_rebuild: success，cards=770，strong=1714，medium=535，weak_audit=500；随后刷新 wrong-card source summaries、knowledge clusters、pattern clusters 和 bridge snapshot。
- bridge_refresh: success，records=873，assets=1253。
- rollback_action: not_run。

## 2026-07-01 formal_card_generic_knowledge_refinement_from_visual_parent_path 51-cards

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮针对旧导入高数卡中仍挂 `高等数学综合待精分` 的粗标签做保守精分。
- audit_before: 59 张 GS 正式卡 frontmatter 仍挂 `高等数学综合待精分`；其中 51 张有可视化详情页和足够清楚的 MarginNote 父级路径/题型目录，8 张只显示“计算出错”或缺明确章节对象。
- wiki_updated: 51 张正式错题卡；51 个对应可视化详情页；错题知识网络/知识点库.md；错题知识网络/wiki/index.md；错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-008_高等数学综合待精分分流台.md；错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md；错题知识网络/wiki/log.md。
- update: 为 51 张旧卡补齐更具体的 `chapter`、`question_type`、`knowledge`、`methods`、`traps` 与正文标签区；新增/登记 `定积分应用`、`定积分等式`、`平面图形面积`、`曲线弧长`、`旋转体体积`、`旋转曲面面积`、`多元函数极限`、`偏微分方程`、`二重积分换序`、`二重积分对称性`、`二重积分极坐标法` 等知识点。
- card_decision: tag-refinement-only；不根据图片反推用户本人的 `wrong_point`、`error_causes`、`method_gap`、掌握度或回滚复习；`GS-164`、`GS-165`、`GS-166`、`GS-167`、`GS-168`、`GS-169`、`GS-408`、`GS-414` 因证据不足保留待确认。
- validation: refined_cards=51；frontmatter_generic_count=8；body_generic_count=8；refined_bad_count=0；refined_visual_still_generic=0；YAML frontmatter 解析错误 0；`wrongnet.py related GS-647` 仍召回 `GS-627`、`GS-629`、`GS-646` 等强关联题。
- wrongnet_rebuild: success，cards=770，strong=1751，medium=673，weak_audit=500；source summaries=770；knowledge_clusters=368；method_clusters=710；error_clusters=265；action_gap_clusters=8；missing_method=166；missing_error=448；missing_action_gap=435。
- bridge_refresh: success，records=873，assets=1253；HTTP bridge 抽查 `GS-014`、`GS-302`、`GS-398`、`GS-647` 均返回 200。
- rollback_action: not_run。

## 2026-07-01 formal_card_generic_knowledge_refinement_from_question_solution_images 6-cards

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮继续处理上一轮保留的 8 张 `高等数学综合待精分` 卡。
- audit_before: `GS-164` 至 `GS-169` 已有题图/解析图入口，其中 `GS-166` 只有题图无解析图；`GS-408`、`GS-414` 仍缺题图/解析图入口。
- wiki_updated: 6 张正式错题卡；6 个对应可视化详情页；`错题知识网络/知识点库.md`；`错题知识网络/wiki/index.md`；`MATHWIKI-GS-TOPIC-008_高等数学综合待精分分流台.md`；`MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md`；knowledge/method/error/action-gap cluster 生成脚本；`错题知识网络/wiki/log.md`。
- update: 将 [GS-164](http://127.0.0.1:8765/open/GS-164)、[GS-165](http://127.0.0.1:8765/open/GS-165)、[GS-166](http://127.0.0.1:8765/open/GS-166)、[GS-167](http://127.0.0.1:8765/open/GS-167)、[GS-168](http://127.0.0.1:8765/open/GS-168)、[GS-169](http://127.0.0.1:8765/open/GS-169) 分别精分到微分方程、幂指极限、分段函数求导与极值、拐点切线、有理函数反常积分、参数方程曲率等具体标签；`GS-166` 因解析图缺失，标准答案保持待核对。
- generator_repair: 修复 `build_knowledge_cluster_pages.py` 与 `build_pattern_cluster_pages.py`，重建前清理旧自动簇文件，避免旧编号知识簇继续污染 source summary 反向链接。
- card_decision: tag-and-visual-refinement-only；不根据图片反推用户本人的 `wrong_point`、`error_causes`、`method_gap`、掌握度或回滚复习；`GS-408`、`GS-414` 因缺可视化证据继续保留待确认。
- validation: `高等数学综合待精分` 正式卡剩余 2 张；旧自动簇重复文件已清理，当前有效簇为 `MATHWIKI-KNOWLEDGE-203`，仅覆盖 `GS-408`、`GS-414`。
- wrongnet_rebuild: success，cards=770，strong=1752，medium=696，weak_audit=500；source summaries=770；knowledge_clusters=370；method_clusters=717；error_clusters=265；action_gap_clusters=8。
- bridge_refresh: success，records=873，assets=1253；同时修复本地桥 `open` 接口先等待 Obsidian CLI 导致页面卡住的问题，改为先用 macOS `open` 异步打开 Obsidian URL，并已重启 8765 桥接服务。
- rollback_action: not_run。

## 2026-07-01 visual_detail_restatement_closure_with_solution_images 10-cards

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮选取 10 张已有正式卡、且同时具备题图和解析图的旧导入卡，补齐视觉复述与正式卡方法入口。
- scope: [GS-014](http://127.0.0.1:8765/open/GS-014)、[GS-043](http://127.0.0.1:8765/open/GS-043)、[GS-072](http://127.0.0.1:8765/open/GS-072)、[GS-099](http://127.0.0.1:8765/open/GS-099)、[GS-115](http://127.0.0.1:8765/open/GS-115)、[GS-123](http://127.0.0.1:8765/open/GS-123)、[GS-128](http://127.0.0.1:8765/open/GS-128)、[GS-137](http://127.0.0.1:8765/open/GS-137)、[GS-147](http://127.0.0.1:8765/open/GS-147)、[GS-149](http://127.0.0.1:8765/open/GS-149)。
- update: 10 张正式卡均补入稳定 `lecture_refs`、标准答案、知识点/方法/陷阱和复做提醒；10 个可视化详情页均补齐 `题目定位`、`正确第一步`、`核心方法`、`易错触发`、`方法页` 与 `复做提醒`。
- card_decision: evidence-backed-refinement-only；只写题图/解析图可确认内容，不新建正式卡，不合并旧卡，不从解析图反推用户本人错因。除 `GS-115` 解析文字已明确“\((\ln x)^k\) 与 \(\ln(x^k)\) 混淆”外，其余 9 张仍保留个人错因待补充。
- mastery_boundary: 不修改掌握度或回滚复习 JSON；`GS-147` 保留既有 `已掌握` 状态。
- validation: YAML frontmatter parse ok；10 个目标视觉详情页的复述占位清零；正式卡 `lecture_refs` 目标文件缺失 0；`git diff --check` ok；bridge `/health` ok，records=873，assets=1253；HTTP bridge 实测 [GS-043](http://127.0.0.1:8765/open/GS-043) 可打开 Obsidian 详情页。
- wrongnet_rebuild: success，cards=770，strong=1752，medium=693，weak_audit=500；knowledge_clusters=376；method_clusters=730；error_clusters=267；action_gap_clusters=8；wrong-card source summaries=770，compiled=652。
- bridge_refresh: success，records=873，assets=1253。
- rollback_action: not_run。

## 2026-07-01 differential_equation_visual_restatement_closure 10-cards

- input: 持续目标要求根据已入库题目的解析和图片进一步加强错题网络质量；本轮选取第 15 讲微分方程 10 张已有正式卡且具备题图/解析图的旧导入卡。
- scope: [GS-187](http://127.0.0.1:8765/open/GS-187), [GS-188](http://127.0.0.1:8765/open/GS-188), [GS-189](http://127.0.0.1:8765/open/GS-189), [GS-190](http://127.0.0.1:8765/open/GS-190), [GS-192](http://127.0.0.1:8765/open/GS-192), [GS-194](http://127.0.0.1:8765/open/GS-194), [GS-195](http://127.0.0.1:8765/open/GS-195), [GS-198](http://127.0.0.1:8765/open/GS-198), [GS-199](http://127.0.0.1:8765/open/GS-199), [GS-202](http://127.0.0.1:8765/open/GS-202)。
- wiki_updated: 10 张正式错题卡；10 个对应可视化详情页；错题知识网络/知识点库.md；MATHWIKI-GS-TOPIC-009_微分方程错题总线.md；wiki/index.md；MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md；数学LLMWiki安全输入包.md。
- update: 根据题图/解析图补齐题型、标准答案、知识点、方法入口、陷阱和复做提醒；在微分方程总线新增第 15 讲入口判别表。
- card_decision: evidence-backed-refinement-only；不新建正式卡，不合并旧卡，不从解析图反推用户本人错因。
- mastery_boundary: 不修改掌握度或回滚复习 JSON。
- wrongnet_rebuild: success，cards=770，strong=1752，medium=653，weak_audit=500；source summaries=770；knowledge_clusters=383；method_clusters=749；error_clusters=267；action_gap_clusters=8；bridge snapshot records=873，assets=1253。
- validation: YAML frontmatter parse ok；10 个目标视觉详情页旧复述占位清零；manifest/asset_to_obsidian JSON parse ok；lecture_refs 目标文件缺失 0；bridge /health ok；HTTP bridge 实测 GS-187 返回 200；git diff --check ok。
- rollback_action: not_run

## 2026-07-01｜第15讲微分方程视觉解析补强（第二批）
- 本批补强正式错题卡与可视化详情页：[GS-193](http://127.0.0.1:8765/open/GS-193), [GS-196](http://127.0.0.1:8765/open/GS-196), [GS-197](http://127.0.0.1:8765/open/GS-197), [GS-201](http://127.0.0.1:8765/open/GS-201), [GS-203](http://127.0.0.1:8765/open/GS-203), [GS-204](http://127.0.0.1:8765/open/GS-204), [GS-205](http://127.0.0.1:8765/open/GS-205), [GS-206](http://127.0.0.1:8765/open/GS-206), [GS-207](http://127.0.0.1:8765/open/GS-207), [GS-211](http://127.0.0.1:8765/open/GS-211)。
- 重点补强：二阶可降阶、常系数特征方程、变上限积分方程、几何建模、物理变量转换、追踪曲线与乘积导数结构。
- 边界说明：仅使用题图和解析图可确认的信息；旧卡未记录的用户个人错因不反推，正式卡中保留待补充提示。
- 同步更新：`MATHWIKI-GS-TOPIC-009_微分方程错题总线.md` 与数学 LLMWiki 安全输入包。

## 2026-07-01｜一元函数中值定理视觉解析补强
- 本批补强正式错题卡与可视化详情页：[GS-213](http://127.0.0.1:8765/open/GS-213), [GS-218](http://127.0.0.1:8765/open/GS-218), [GS-237](http://127.0.0.1:8765/open/GS-237), [GS-253](http://127.0.0.1:8765/open/GS-253)。
- 重点补强：指数因子辅助函数、积分中值定理 + Rolle 链条、中点 Taylor 积分、双端点/极值点 Taylor 估值。
- 边界说明：仅使用题图和解析图可确认的信息；旧卡未记录用户个人错因，正式卡保留待补充提示。
- 同步更新：`MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md` 与数学 LLMWiki 安全输入包。

## 2026-07-01｜定积分应用视觉解析补强
- 本批补强正式错题卡与可视化详情页：[GS-294](http://127.0.0.1:8765/open/GS-294), [GS-295](http://127.0.0.1:8765/open/GS-295), [GS-297](http://127.0.0.1:8765/open/GS-297), [GS-298](http://127.0.0.1:8765/open/GS-298)。
- 重点补强：绝对值面积与周期分段求和、曲边面积变化率、函数方程 \(x\mapsto1/x\) 消元、水平切片旋转体、以 \(y\) 为参数的弧长与最值。
- 边界说明：仅使用题图和解析图可确认的信息；旧卡未记录用户个人错因，正式卡保留待补充提示。
- 同步更新：`MATHWIKI-GS-TOPIC-006_定积分错题总线.md` 与数学 LLMWiki 安全输入包。

## 2026-07-01｜定积分应用视觉解析补强（弧长与曲面面积）
- 本批补强正式错题卡与可视化详情页：[GS-299](http://127.0.0.1:8765/open/GS-299), [GS-300](http://127.0.0.1:8765/open/GS-300), [GS-301](http://127.0.0.1:8765/open/GS-301), [GS-302](http://127.0.0.1:8765/open/GS-302)。
- 重点补强：微分方程生成曲线弧长、变上限积分曲线弧长、弧长根式完全平方化简、旋转曲面面积公式。
- 边界说明：仅使用题图和解析图可确认的信息；旧卡未记录用户个人错因，正式卡保留待补充提示；`GS-301` 与 `GS-302` 标记为同源重复候选，但本轮不合并、不删除。
- 同步更新：`MATHWIKI-GS-TOPIC-006_定积分错题总线.md` 与数学 LLMWiki 安全输入包。

## 2026-07-01｜定积分应用视觉解析补强（几何量公式化归）
- 本批补强正式错题卡与可视化详情页：[GS-303](http://127.0.0.1:8765/open/GS-303), [GS-304](http://127.0.0.1:8765/open/GS-304), [GS-305](http://127.0.0.1:8765/open/GS-305)。
- 重点补强：三角变上限曲线全长、无界区域旋转体体积、双曲函数旋转曲面面积。
- 边界说明：仅使用题图和解析图可确认的信息；旧卡未记录用户个人错因，正式卡保留待补充提示。
- 同步更新：`MATHWIKI-GS-TOPIC-006_定积分错题总线.md` 与数学 LLMWiki 安全输入包。

## 2026-07-01｜祖孙三代奇偶性视觉解析补强
- 本批闭环正式错题卡与可视化详情页：[GS-307](http://127.0.0.1:8765/open/GS-307), [GS-308](http://127.0.0.1:8765/open/GS-308)。
- 重点补强：高阶导数奇偶周期递推、变上限积分奇偶性、复合函数奇偶性判断。
- 边界说明：旧卡未记录用户个人错因，本轮只根据题图和解析图补强方法入口、视觉索引、wiki 总索引和 Tutor 安全训练项，不反推掌握度或回滚复习。
- 同步更新：`MATHWIKI-GS-METHOD-003_整体函数奇偶性检查.md`、`MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`错题知识网络/可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。

## 2026-07-01｜视觉入口标题一致性补强（一元函数方法入口小批次）
- 本批同步视觉详情标题、Obsidian 打开链接标题、manifest/asset 标题、详情页 H1 和 wiki VIS 行：[GS-463](http://127.0.0.1:8765/open/GS-463), [GS-530](http://127.0.0.1:8765/open/GS-530), [GS-585](http://127.0.0.1:8765/open/GS-585), [GS-547](http://127.0.0.1:8765/open/GS-547), [GS-497](http://127.0.0.1:8765/open/GS-497), [GS-470](http://127.0.0.1:8765/open/GS-470), [GS-533](http://127.0.0.1:8765/open/GS-533), [GS-459](http://127.0.0.1:8765/open/GS-459), [GS-461](http://127.0.0.1:8765/open/GS-461), [GS-472](http://127.0.0.1:8765/open/GS-472)。
- 重点补强：把旧 MarginNote 标题升级为正式卡标题，例如导数定义差商、周期函数导数定义、嵌套变限积分链式、无穷小最低阶、斜渐近线、振荡因子可导性、幂指泰勒展开、绝对值可导阶数和指数平坦函数高阶导等入口。
- 边界说明：本批为导航与索引一致性维护，不改正式错题卡正文、不改个人错因、不启用 method_gap、不修改回滚复习账本。

## 2026-07-01｜method_gap 字段规范化收口
- 本批规范化正式错题卡 `method_gap.knowledge_gap_or_method_gap` 枚举值，并把部分 `expected_first_action` 收口为可执行动作句：[GS-492](http://127.0.0.1:8765/open/GS-492), [GS-545](http://127.0.0.1:8765/open/GS-545), [GS-570](http://127.0.0.1:8765/open/GS-570), [GS-571](http://127.0.0.1:8765/open/GS-571), [GS-575](http://127.0.0.1:8765/open/GS-575), [GS-577](http://127.0.0.1:8765/open/GS-577), [GS-580](http://127.0.0.1:8765/open/GS-580), [GS-582](http://127.0.0.1:8765/open/GS-582), [GS-583](http://127.0.0.1:8765/open/GS-583), [GS-584](http://127.0.0.1:8765/open/GS-584), [GS-587](http://127.0.0.1:8765/open/GS-587), [GS-592](http://127.0.0.1:8765/open/GS-592), [GS-605](http://127.0.0.1:8765/open/GS-605), [GS-609](http://127.0.0.1:8765/open/GS-609), [GS-610](http://127.0.0.1:8765/open/GS-610), [GS-611](http://127.0.0.1:8765/open/GS-611), [GS-612](http://127.0.0.1:8765/open/GS-612)。
- 新增维护页：`MATHWIKI-MAINT-002_method_gap字段规范化收口.md`，用于登记本批字段规范化、动作句收口和质量门口径。
- 边界说明：只修正字段枚举与动作句格式，不改变用户原始错因、不改掌握度、不修改回滚 JSON。

## 2026-07-01｜视觉入口标题一致性补强（结构化标题第二批）
- 本批同步 26 个正式卡标题到视觉详情标题、Obsidian 打开链接标题、manifest/asset 标题、详情页 H1 和 wiki VIS 行：[GS-509](http://127.0.0.1:8765/open/GS-509), [GS-542](http://127.0.0.1:8765/open/GS-542), [GS-479](http://127.0.0.1:8765/open/GS-479), [GS-541](http://127.0.0.1:8765/open/GS-541), [GS-578](http://127.0.0.1:8765/open/GS-578), [GS-507](http://127.0.0.1:8765/open/GS-507), [GS-446](http://127.0.0.1:8765/open/GS-446), [GS-430](http://127.0.0.1:8765/open/GS-430), [GS-455](http://127.0.0.1:8765/open/GS-455), [GS-448](http://127.0.0.1:8765/open/GS-448), [GS-498](http://127.0.0.1:8765/open/GS-498), [GS-471](http://127.0.0.1:8765/open/GS-471), [GS-584](http://127.0.0.1:8765/open/GS-584), [GS-447](http://127.0.0.1:8765/open/GS-447), [GS-452](http://127.0.0.1:8765/open/GS-452), [GS-453](http://127.0.0.1:8765/open/GS-453), [GS-456](http://127.0.0.1:8765/open/GS-456), [GS-469](http://127.0.0.1:8765/open/GS-469), [GS-523](http://127.0.0.1:8765/open/GS-523), [GS-574](http://127.0.0.1:8765/open/GS-574), [GS-573](http://127.0.0.1:8765/open/GS-573), [GS-527](http://127.0.0.1:8765/open/GS-527), [GS-120](http://127.0.0.1:8765/open/GS-120), [GS-549](http://127.0.0.1:8765/open/GS-549), [GS-528](http://127.0.0.1:8765/open/GS-528), [GS-449](http://127.0.0.1:8765/open/GS-449)。
- 重点补强：把旧日期/题号型视觉标题升级为能直接暴露方法断点的标题，如无穷远函数极限、幂级数、导数单调、反常积分、递推数列、分段函数、变上限积分、高阶导等。
- 边界说明：本批只做导航与索引一致性维护，不修改正式错题卡、不改个人错因、不修改回滚复习账本。
## 2026-07-01｜视觉入口标题一致性补强（结构化标题第三批）
- 本批同步 32 个正式卡标题到视觉详情标题、Obsidian 打开链接标题、manifest/asset 标题、详情页 H1 和 wiki VIS 行：[GS-458](http://127.0.0.1:8765/open/GS-458), [GS-515](http://127.0.0.1:8765/open/GS-515), [GS-516](http://127.0.0.1:8765/open/GS-516), [GS-517](http://127.0.0.1:8765/open/GS-517), [GS-518](http://127.0.0.1:8765/open/GS-518), [GS-519](http://127.0.0.1:8765/open/GS-519), [GS-520](http://127.0.0.1:8765/open/GS-520), [GS-558](http://127.0.0.1:8765/open/GS-558), [GS-562](http://127.0.0.1:8765/open/GS-562), [GS-567](http://127.0.0.1:8765/open/GS-567), [GS-568](http://127.0.0.1:8765/open/GS-568), [GS-570](http://127.0.0.1:8765/open/GS-570), [GS-571](http://127.0.0.1:8765/open/GS-571), [GS-575](http://127.0.0.1:8765/open/GS-575), [GS-576](http://127.0.0.1:8765/open/GS-576), [GS-577](http://127.0.0.1:8765/open/GS-577), [GS-579](http://127.0.0.1:8765/open/GS-579), [GS-580](http://127.0.0.1:8765/open/GS-580), [GS-581](http://127.0.0.1:8765/open/GS-581), [GS-582](http://127.0.0.1:8765/open/GS-582), [GS-583](http://127.0.0.1:8765/open/GS-583), [GS-586](http://127.0.0.1:8765/open/GS-586), [GS-587](http://127.0.0.1:8765/open/GS-587), [GS-593](http://127.0.0.1:8765/open/GS-593), [GS-597](http://127.0.0.1:8765/open/GS-597), [GS-598](http://127.0.0.1:8765/open/GS-598), [GS-599](http://127.0.0.1:8765/open/GS-599), [GS-600](http://127.0.0.1:8765/open/GS-600), [GS-601](http://127.0.0.1:8765/open/GS-601), [GS-602](http://127.0.0.1:8765/open/GS-602), [GS-611](http://127.0.0.1:8765/open/GS-611), [GS-612](http://127.0.0.1:8765/open/GS-612)。
- 重点补强：把旧题号/日期型视觉标题升级为方法入口标题，覆盖导数定义差商、微分不等式积分因子、正项级数/幂级数判敛、反常积分、变限积分、交错级数、曲线弧长和速度积分等入口。
- 边界说明：本批只做导航与索引一致性维护，不修改正式错题卡、不改用户个人错因、不修改掌握度、不修改回滚复习账本。
## 2026-07-01｜视觉入口标题一致性补强（结构化标题第四批）
- 本批同步 32 个来源可对齐的正式卡标题到视觉详情标题、Obsidian 打开链接标题、manifest/asset 标题、详情页 H1 和 wiki VIS 行：[GS-201](http://127.0.0.1:8765/open/GS-201), [GS-218](http://127.0.0.1:8765/open/GS-218), [GS-237](http://127.0.0.1:8765/open/GS-237), [GS-253](http://127.0.0.1:8765/open/GS-253), [GS-289](http://127.0.0.1:8765/open/GS-289), [GS-290](http://127.0.0.1:8765/open/GS-290), [GS-294](http://127.0.0.1:8765/open/GS-294), [GS-300](http://127.0.0.1:8765/open/GS-300), [GS-331](http://127.0.0.1:8765/open/GS-331), [GS-445](http://127.0.0.1:8765/open/GS-445), [GS-450](http://127.0.0.1:8765/open/GS-450), [GS-454](http://127.0.0.1:8765/open/GS-454), [GS-457](http://127.0.0.1:8765/open/GS-457), [GS-460](http://127.0.0.1:8765/open/GS-460), [GS-475](http://127.0.0.1:8765/open/GS-475), [GS-478](http://127.0.0.1:8765/open/GS-478), [GS-481](http://127.0.0.1:8765/open/GS-481), [GS-482](http://127.0.0.1:8765/open/GS-482), [GS-484](http://127.0.0.1:8765/open/GS-484), [GS-487](http://127.0.0.1:8765/open/GS-487), [GS-494](http://127.0.0.1:8765/open/GS-494), [GS-496](http://127.0.0.1:8765/open/GS-496), [GS-500](http://127.0.0.1:8765/open/GS-500), [GS-501](http://127.0.0.1:8765/open/GS-501), [GS-505](http://127.0.0.1:8765/open/GS-505), [GS-508](http://127.0.0.1:8765/open/GS-508), [GS-511](http://127.0.0.1:8765/open/GS-511), [GS-512](http://127.0.0.1:8765/open/GS-512), [GS-526](http://127.0.0.1:8765/open/GS-526), [GS-529](http://127.0.0.1:8765/open/GS-529), [GS-534](http://127.0.0.1:8765/open/GS-534), [GS-535](http://127.0.0.1:8765/open/GS-535)。
- 重点补强：把旧真题号、题组号、日期型视觉标题升级为方法入口标题，覆盖变限积分方程、中值定理、Taylor 估值、卷积分段、原函数拼接、反常/级数判敛、曲率、渐近线、导数定义和幂级数收敛域等入口。
- 边界说明：本批只处理来源编号能对上的标题一致性；疑似源题名不一致的候选保留待单独核查；不修改正式错题卡、不改个人错因、不修改掌握度、不修改回滚复习账本。
## 2026-07-01｜视觉入口标题一致性补强（结构化标题第五批）
- 本批同步 16 个来源可对齐的正式卡标题到视觉详情标题、Obsidian 打开链接标题、manifest/asset 标题、详情页 H1 和 wiki VIS 行：[GS-536](http://127.0.0.1:8765/open/GS-536), [GS-539](http://127.0.0.1:8765/open/GS-539), [GS-543](http://127.0.0.1:8765/open/GS-543), [GS-544](http://127.0.0.1:8765/open/GS-544), [GS-545](http://127.0.0.1:8765/open/GS-545), [GS-546](http://127.0.0.1:8765/open/GS-546), [GS-548](http://127.0.0.1:8765/open/GS-548), [GS-540](http://127.0.0.1:8765/open/GS-540), [GS-550](http://127.0.0.1:8765/open/GS-550), [GS-551](http://127.0.0.1:8765/open/GS-551), [GS-613](http://127.0.0.1:8765/open/GS-613), [GS-614](http://127.0.0.1:8765/open/GS-614), [GS-616](http://127.0.0.1:8765/open/GS-616), [GS-638](http://127.0.0.1:8765/open/GS-638), [GS-639](http://127.0.0.1:8765/open/GS-639), [GS-641](http://127.0.0.1:8765/open/GS-641)。
- 重点补强：收口导数为零、曲率弧长参数、分段中值定理、幂级数收敛域/求和、傅里叶/余弦级数、含参积分和变上限积分等入口标题。
- 边界说明：本批只处理来源编号能对上的标题一致性；疑似源题名不一致的候选继续保留待核查；不修改正式错题卡、不改个人错因、不修改掌握度、不修改回滚复习账本。

## 2026-07-01｜GS-288 / GS-312 视觉错连人工修复
- 本轮人工打开题图确认：[GS-288](http://127.0.0.1:8765/open/GS-288) 正式卡是 `1000题B组9.8（103491）含参绝对值积分`，但原视觉入口题图与 GS-125 重复；[GS-312](http://127.0.0.1:8765/open/GS-312) 正式卡是 `103059 反三角周期积分`，但原视觉入口挂了 103491 的题图与解析图。
- 已修复：103491 题图和两张解析图归还到 `GS-288` 资产目录；`MN4-GS-CH01-440` 的 103059 题图提升为 `GS-312` 正式视觉入口；两个详情页、`index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 和 wiki VIS 行已同步。
- 证据保留：原错绑资产已复制到 `错题知识网络/assets/visual_wrong_questions/_quarantine/2026-07-01-GS288-GS312-relink/`，来源候选页 `MN4-GS-CH01-440` 保留为 GS-312 的 OCR 解析来源。
- 边界说明：本轮只修视觉详情层与导航映射；未修改正式错题卡、未运行 wrongnet rebuild、未修改回滚 JSON、未新增或反推个人错因/掌握度。

## 2026-07-01｜GS-426 至 GS-429 旧错连收口为线代候选
- scope: [VIS-GS-426-MISMATCH-OLD](http://127.0.0.1:8765/open/VIS-GS-426-MISMATCH-OLD), [VIS-GS-427-MISMATCH-OLD](http://127.0.0.1:8765/open/VIS-GS-427-MISMATCH-OLD), [VIS-GS-428-MISMATCH-OLD](http://127.0.0.1:8765/open/VIS-GS-428-MISMATCH-OLD), [VIS-GS-429-MISMATCH-OLD](http://127.0.0.1:8765/open/VIS-GS-429-MISMATCH-OLD)。
- evidence: 4 张题图均为线代矩阵运算题；正式 `GS-426` 至 `GS-429` 是高数导数定义旧卡，不能复用这些题图。
- update: 4 个详情页从高等数学目录移入线性代数目录；资产目录从 `GS-426` 至 `GS-429` 改为对应 `VIS-GS-*-MISMATCH-OLD` 目录；`manifest.json`、`asset_to_obsidian.json`、`index.md`、`obsidian_open_links.md`、`MATHWIKI-QUESTIONS-003` 和 `MATHWIKI-LA-TOPIC-001` 已同步。
- card_decision: visual_candidate_enriched；缺用户本人错因和正式 LA 卡，暂不正式入库；原 `GS-426` 至 `GS-429` 继续留在正式卡缺可视化详情队列。
- wrongnet_rebuild: not_run_visual_only。
- rollback_action: not_run。

## 2026-07-01｜同源重复视觉源候选补强 GS-354/356/363
- scope: [GS-354](http://127.0.0.1:8765/open/GS-354), [GS-356](http://127.0.0.1:8765/open/GS-356), [GS-363](http://127.0.0.1:8765/open/GS-363)。
- evidence: 三个视觉详情页使用同一 OO3 `source_refid=64e4b1e777762420de15a4df47fc94ff` 和同一组题图/解析图；题目实际为分段二元函数在原点处偏导、混合偏导、二重极限与累次极限的概念判断题。
- update: 三张正式卡补入稳定 `lecture_refs`、轻量题目摘要、答案 B、知识点、方法入口、陷阱、同源重复候选关键词和相互 `related`；质量门要求 `wrong_point` 不得占位，因此写为“暂无明确个人错因；复做入口是……”，不伪造用户本人错因；三张视觉详情页补齐题目定位、正确第一步、核心方法、易错触发和同源重复说明。
- wiki_updated: `MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`；`wiki/index.md`；`MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md`；`数学LLMWiki安全输入包.md`；`wiki/log.md`。
- card_decision: duplicate-source-refinement-only；不删除、不合并正式卡，不从解析图反推用户本人错因，不修改掌握度或回滚复习。
- wrongnet_rebuild: needed_after_formal_card_update。
- rollback_action: not_run。

## 2026-07-01｜含参积分与全微分视觉解析补强 GS-338/367
- scope: [GS-338](http://127.0.0.1:8765/open/GS-338), [GS-367](http://127.0.0.1:8765/open/GS-367)。
- evidence: 两题均有题图与解析图。`GS-338` 题目为 \(g(x)=\int_0^1 f(xt)\,dt\) 的导数与 \(x=0\) 处连续性证明；`GS-367` 题目为 \(z=\arctan[xy+\sin(x+y)]\) 在 \((0,\pi)\) 处求全微分。
- update: 两张正式卡补入稳定 `lecture_refs`、轻量题目摘要、标准答案、知识点、方法入口、陷阱和复做提醒；两个可视化详情页补齐题目定位、正确第一步、核心方法、易错触发、方法入口和复做提醒。
- relation_guard: 将两张卡的 `error_causes` 保持为 `待补充`，并补充 `wrongnet.py` / `intake_quality_gate.py` / `build_pattern_cluster_pages.py` 的占位过滤，使“暂无明确个人错因”不参与错因强关联。
- generator_guard: 补充 `build_wrong_card_source_summaries.py`、`build_knowledge_cluster_pages.py`、`build_pattern_cluster_pages.py` 的 YAML 标量清洗，避免旧卡中带引号的标签生成重复知识簇；重建后带引号知识簇文件为 0。
- wiki_updated: `MATHWIKI-GS-TOPIC-006_定积分错题总线.md`；`MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`；`wiki/index.md`；`数学LLMWiki安全输入包.md`；`wiki/log.md`。
- card_decision: evidence-backed-refinement-only；仅使用题图/解析图可确认内容，不从解析图反推用户本人错因，不修改掌握度或回滚复习。
- wrongnet_rebuild: needed_after_formal_card_update。
- rollback_action: not_run。

## 2026-07-01｜偏微分方程变量代换视觉解析补强 GS-380-384
- scope: [GS-380](http://127.0.0.1:8765/open/GS-380), [GS-381](http://127.0.0.1:8765/open/GS-381), [GS-382](http://127.0.0.1:8765/open/GS-382), [GS-383](http://127.0.0.1:8765/open/GS-383), [GS-384](http://127.0.0.1:8765/open/GS-384)。
- evidence: 5 题均已有题图与解析图，主题集中在二阶偏微分方程变量代换、线性变量代换链式求导、径向变量 \(t=\ln r\) 化常微分方程和边界条件回代。
- update: 5 张正式卡补入稳定 `lecture_refs`、轻量题目摘要、标准答案、知识点、方法入口、陷阱与复做提醒；5 个可视化详情页补齐 `题目定位`、`正确第一步`、`核心方法`、`易错触发`、`方法页` 与 `复做提醒`。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-031_偏微分方程变量代换化简.md`；更新 `MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md` 与 `数学LLMWiki安全输入包.md`。
- card_decision: evidence-backed-refinement-only；只写题图/解析图可确认内容，不从解析图反推用户本人错因，不启用 `method_gap`，不修改掌握度或回滚复习。
- wrongnet_rebuild: needed_after_formal_card_update。
- rollback_action: not_run。

## 2026-07-02｜多元函数极值与闭区域最值视觉解析闭环 GS-390-396
- scope: [GS-390](http://127.0.0.1:8765/open/GS-390), [GS-391](http://127.0.0.1:8765/open/GS-391), [GS-392](http://127.0.0.1:8765/open/GS-392), [GS-393](http://127.0.0.1:8765/open/GS-393), [GS-394](http://127.0.0.1:8765/open/GS-394), [GS-395](http://127.0.0.1:8765/open/GS-395), [GS-396](http://127.0.0.1:8765/open/GS-396)。
- evidence: 7 题均已有正式错题卡和可视化详情页；题图与解析材料支持多元函数无条件极值、闭区域最值、条件极值、二次型约束和实际问题建模的复做入口补强。
- wiki_updated: `MATHWIKI-GS-METHOD-032_多元函数极值驻点判别.md`、`MATHWIKI-GS-METHOD-033_多元函数条件与闭区域最值.md`、`MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`manifest.json` 与数学 LLMWiki 安全输入包。
- update: 正式卡保留轻量题目摘要、答案、知识点、方法入口、陷阱和复做提醒；可视化详情页保留题图可见、解析折叠，并补齐 `题目定位`、`正确第一步`、`核心方法`、`易错触发`、方法页和 Obsidian bridge 入口。
- card_decision: evidence-backed-refinement-only；只根据题图/解析补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1747，medium=624，weak_audit=496；LLM Wiki coverage 顺序刷新成功，source summaries=770，knowledge_clusters=347，method_clusters=798，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；7 张卡 `intake_quality_gate --visual expected` 均为 `quality_gate=ok`。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告；这是本批正确边界，因为缺少用户本人作答过程，不能编造个人错因或方法断点。
- rollback_action: not_run。

## 2026-07-02｜二重积分区域化归与对称性视觉解析闭环 GS-397-404
- scope: [GS-397](http://127.0.0.1:8765/open/GS-397), [GS-398](http://127.0.0.1:8765/open/GS-398), [GS-399](http://127.0.0.1:8765/open/GS-399), [GS-400](http://127.0.0.1:8765/open/GS-400), [GS-401](http://127.0.0.1:8765/open/GS-401), [GS-402](http://127.0.0.1:8765/open/GS-402), [GS-403](http://127.0.0.1:8765/open/GS-403), [GS-404](http://127.0.0.1:8765/open/GS-404)。
- evidence: 8 题均已有正式错题卡和可视化详情页；题图、解析图或折叠解析文字支持二重积分和式极限、换序、区域选择、极坐标、普通对称性、轮换对称性、区域合并和坐标化归入口补强。
- wiki_updated: 新建并挂载 `MATHWIKI-GS-METHOD-034_二重积分区域化归与换序.md`、`MATHWIKI-GS-METHOD-035_二重积分对称性保号与轮换.md`；更新 `MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: 正式卡只保留轻量题目摘要、答案、知识点、方法入口、陷阱和复做提醒；可视化详情页保留题图可见、解析折叠，并补齐 `题目定位`、`正确第一步`、`核心方法`、`易错触发`、方法页和 Obsidian bridge 入口。
- tutor_safe_update: 新增“二重积分区域化归与换序训练项”和“二重积分对称性保号与轮换训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1747，medium=623，weak_audit=496；LLM Wiki coverage 顺序刷新成功，source summaries=770，knowledge_clusters=347，method_clusters=802，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253。
- quality_note: 质量门允许保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告；这是本批正确边界，因为缺少用户本人作答过程，不能编造个人错因或方法断点。
- rollback_action: not_run。

## 2026-07-02｜二重积分换元与雅可比链视觉解析闭环 GS-407/413
- scope: [GS-407](http://127.0.0.1:8765/open/GS-407), [GS-413](http://127.0.0.1:8765/open/GS-413)。
- evidence: 两题均已有正式错题卡和可视化详情页；折叠解析文字支持极坐标处理二次型边界、平移圆心、二重积分换元三步和雅可比链条补强。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-036_二重积分换元与雅可比链.md`；更新 `MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`manifest.json` 与数学 LLMWiki 安全输入包。
- update: `GS-407` 补入答案 \(\frac{\pi\ln2}{8\sqrt3}\)、二重积分极坐标法入口、径向先积与 \(t=\tan\theta\) 角向处理；`GS-413` 补入答案 \(-\frac83\)、平移到圆心、极坐标半圆区域和雅可比检查链。
- tutor_safe_update: 新增“二重积分换元与雅可比训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1752，medium=618，weak_audit=496；LLM Wiki coverage 顺序刷新成功，source summaries=770，knowledge_clusters=347，method_clusters=803，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253。
- quality_note: 质量门允许保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告；这是本批正确边界，因为缺少用户本人作答过程，不能编造个人错因或方法断点。
- rollback_action: not_run。

## 2026-07-02｜二重积分极坐标区域分块与重复候选闭环 GS-406/409-412
- scope: [GS-406](http://127.0.0.1:8765/open/GS-406), [GS-409](http://127.0.0.1:8765/open/GS-409), [GS-410](http://127.0.0.1:8765/open/GS-410), [GS-411](http://127.0.0.1:8765/open/GS-411), [GS-412](http://127.0.0.1:8765/open/GS-412)。
- evidence: 5 题均已有正式错题卡和可视化详情页；题图与解析图支持参数曲线区域、极坐标区域分块、角域非负性、对称性消奇部和重复候选关系补强。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-037_二重积分极坐标区域分块与对称化.md`；更新 `MATHWIKI-GS-METHOD-034_二重积分区域化归与换序.md`、`MATHWIKI-GS-METHOD-035_二重积分对称性保号与轮换.md`、`MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json`、`MATHWIKI-QUESTIONS-003_视觉证据缺口与候选收口队列.md` 与数学 LLMWiki 安全输入包。
- update: `GS-406` 补入参数曲线边界先内层积分再参数换元；`GS-409` 补入圆弧与直线极坐标分块；`GS-410` 补入 \(r^2=\cos2\theta\) 与角域非负性；`GS-411` 补入对称性消奇项；`GS-412` 标记为 GS-401 同源重复候选。
- tutor_safe_update: 新增“参数曲线二重积分区域训练项”“极坐标区域分块训练项”“同源重复候选识别训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`；重复候选只标记，不自动合并或删除。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1757，medium=619，weak_audit=496；LLM Wiki coverage 顺序刷新成功，source summaries=770，knowledge_clusters=347，method_clusters=806，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；GS-401/406/409/410/411/412 质量门均为 `quality_gate=ok`。
- rollback_action: not_run。

## 2026-07-02｜定积分物理应用微元法视觉解析闭环 GS-415/418-423
- scope: [GS-415](http://127.0.0.1:8765/open/GS-415), [GS-418](http://127.0.0.1:8765/open/GS-418), [GS-419](http://127.0.0.1:8765/open/GS-419), [GS-420](http://127.0.0.1:8765/open/GS-420), [GS-421](http://127.0.0.1:8765/open/GS-421), [GS-422](http://127.0.0.1:8765/open/GS-422), [GS-423](http://127.0.0.1:8765/open/GS-423)。
- evidence: 7 题均已有正式错题卡和可视化详情页；题图与解析图支持变力做功、抽水做功、静水压力、引力做功投影和管道流量环形微元的复做入口补强。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-038_定积分物理应用微元法.md`；更新 `MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: 正式卡补入稳定 `lecture_refs`、轻量题目摘要、标准答案、知识点、方法入口、陷阱和复做提醒；可视化详情页补齐 `题目定位`、`正确第一步`、`核心方法`、`易错触发`、方法页和 Obsidian bridge 入口。
- tutor_safe_update: 新增“定积分物理应用微元法训练项”“变力做功训练项”“抽水与静水压力训练项”“力的投影训练项”“环形流量微元训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1767，medium=635，weak_audit=496；LLM Wiki coverage 顺序刷新成功，source summaries=770，knowledge_clusters=347，method_clusters=815，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253。
- quality_note: 质量门允许保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告；这是本批正确边界，因为缺少用户本人作答过程，不能编造个人错因或方法断点。
- rollback_action: not_run。

## 2026-07-02｜不定积分结构化化归视觉解析闭环 GS-273/279/280/281
- scope: [GS-273](http://127.0.0.1:8765/open/GS-273), [GS-279](http://127.0.0.1:8765/open/GS-279), [GS-280](http://127.0.0.1:8765/open/GS-280), [GS-281](http://127.0.0.1:8765/open/GS-281)。
- evidence: 四题均已有正式错题卡和可视化详情页；题图与解析图支持分部积分后换元、有理函数部分分式、三角幂函数凑微分和重复占位导航收口。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-039_不定积分结构化化归入口.md`；更新 `MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`manifest.json` 与数学 LLMWiki 安全输入包。
- update: `GS-273` 补入分部积分后令根号内部换元；`GS-279` 补入重复线性因子与不可约二次因式的部分分式模板；`GS-281` 保留已掌握和常规队列跳过边界，只补齐三角幂积分入口；`GS-280` 保留重复占位卡属性，正式复做入口仍为 `GS-162`。
- tutor_safe_update: 新增“不定积分结构化化归训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因；重复占位只做导航收口，不自动删除或合并。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1767，medium=637，weak_audit=496；LLM Wiki coverage 刷新成功，source summaries=770，knowledge_clusters=347，method_clusters=815，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；GS-273/279/280/281 质量门均为 `quality_gate=ok`。
- quality_note: `GS-273`、`GS-279` 保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告；`GS-280` 保留重复占位卡的 `review.next: null`，`GS-281` 保留已掌握题的 `review.next: null`。这些都是本批正确边界：缺少用户本人作答过程时不编造个人错因、掌握度或方法断点；重复占位和已掌握题不强行进入常规复做队列。
- rollback_action: not_run。

## 2026-07-02｜线代二次型广义 Rayleigh 商分类修复 GS-425
- scope: [GS-425](http://127.0.0.1:8765/open/GS-425)。
- evidence: 题图与解析图明确为线代二次型：\(f(x_1,x_2)=x_1^2-4x_1x_2+4x_2^2\)，分母二次型矩阵 \(B=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}\)，问题为求 \(B=D^TD\) 及 \(\max_{x\ne0}f(x)/g(x)\)。可视化详情父级路径也属于“线代强化第九讲-二次型-二次型的最值”，原卡挂到“高等数学/不定积分”是历史 OCR/导入分类错误。
- update: 正式卡改为 `subject: 线性代数`、`chapter: 二次型`，补入正定矩阵、广义 Rayleigh 商、\(z=Dx\) 标准化分母、最大特征值入口；可视化详情页迁移到 `错题知识网络/可视化错题详情/线性代数/GS-425_强化例题9.15.md`，题图可见、解析图折叠。
- wiki_updated: 更新 `MATHWIKI-LA-METHOD-002_二次型Rayleigh商最值.md`、`MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“广义 Rayleigh 商训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图和可视化父级路径修复分类与方法入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `intake_closeout.py` 已完成重建、wiki 覆盖刷新、bridge snapshot 刷新后卡在并行验证阶段并被中断；其已完成部分显示 `wrongnet.py rebuild` 成功，cards=770，strong=1767，medium=642，weak_audit=496；knowledge_clusters=348，method_clusters=822，error_clusters=266，action_gap_clusters=8；source summaries=770；bridge snapshot records=873，assets=1253。随后手动验证 `manifest.json`、`asset_to_obsidian.json` 和 bridge records JSON 均合法，bridge 中 `GS-425` 唯一命中并指向线性代数详情页，`intake_quality_gate --visual expected` 为 `quality_gate=ok`。
- quality_note: 质量门允许保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告；这是本题正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜绝对三角周期积分视觉解析闭环 GS-310/311
- scope: [GS-310](http://127.0.0.1:8765/open/GS-310), [GS-311](http://127.0.0.1:8765/open/GS-311)。
- evidence: 两题均已有正式错题卡和可视化详情页；题图与解析图支持绝对值三角函数周期积分、任意起点整周期积分、半周期余段和 \(k\) 奇偶分类的复做入口补强。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-040_绝对三角周期积分.md`；更新 `MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `GS-310` 补入 \(t=nx\) 换元、\(|\sin t|\) 整周期积分与答案 D；`GS-311` 补入 \(\sqrt{1-\sin^2x}=|\cos x|\)、\(k\) 奇偶分类、半周期余段依赖起点与答案 C。
- tutor_safe_update: 新增“绝对三角周期积分训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图/解析图补强可确认的学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1768，medium=640，weak_audit=496；LLM Wiki coverage 刷新成功，source summaries=770，knowledge_clusters=348，method_clusters=824，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`GS-310` 与 `GS-311` 质量门均为 `quality_gate=ok`，bridge records 均为唯一命中并指向对应高等数学详情页。
- quality_note: 质量门若保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代矩阵秩、伴随矩阵与矩阵方程视觉解析闭环 LA-059-064
- scope: [LA-059](http://127.0.0.1:8765/open/LA-059), [LA-060](http://127.0.0.1:8765/open/LA-060), [LA-061](http://127.0.0.1:8765/open/LA-061), [LA-062](http://127.0.0.1:8765/open/LA-062), [LA-063](http://127.0.0.1:8765/open/LA-063), [LA-064](http://127.0.0.1:8765/open/LA-064)。
- evidence: 6 题均已有正式错题卡和可视化详情页；LA-059、LA-060、LA-062、LA-063、LA-064 有解析图，LA-061 有题图和折叠解析文字。证据支持分块矩阵秩消元、分块伴随矩阵、换基表示、Jordan 链、列等价矩阵方程和零空间参数化入口补强。
- wiki_updated: 更新 `MATHWIKI-LA-METHOD-010_伴随矩阵与反对称结构.md`、`MATHWIKI-LA-METHOD-011_矩阵幂降维与秩空间判断.md`；新建 `MATHWIKI-LA-METHOD-012_矩阵方程按列拆与解空间参数化.md`；更新 `MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: 正式卡只保留轻量题目摘要、答案、知识点、方法入口、陷阱和复做提醒；可视化详情页保留题图可见、解析折叠，并补齐题目定位、正确第一步、核心方法、易错触发、方法页和 Obsidian bridge 入口。
- tutor_safe_update: 新增“分块矩阵秩消元边界训练项”“分块伴随矩阵训练项”“矩阵方程按列拆训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图、解析图和正式卡轻量字段补强可确认学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1765，medium=708，weak_audit=495；LLM Wiki coverage 刷新成功，source summaries=770，knowledge_clusters=351，method_clusters=882，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`LA-059` 至 `LA-064` 六张卡 `intake_quality_gate --visual expected` 均为 `quality_gate=ok`；`manifest.json`、`asset_to_obsidian.json` 和 bridge records JSON 均合法；HTTP bridge health 为 ok。
- quality_note: 若质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代矩阵秩、方程组表示与相似特征向量视觉解析闭环 LA-068/070/073/090/099/103
- scope: [LA-068](http://127.0.0.1:8765/open/LA-068), [LA-070](http://127.0.0.1:8765/open/LA-070), [LA-073](http://127.0.0.1:8765/open/LA-073), [LA-090](http://127.0.0.1:8765/open/LA-090), [LA-099](http://127.0.0.1:8765/open/LA-099), [LA-103](http://127.0.0.1:8765/open/LA-103)。
- evidence: 6 题均已有正式错题卡和可视化详情页；题图与解析图支持 \(AB\) 反求 \(BA\)、\(ABC=O\) 分块秩比较、伴随矩阵秩约束、\(A^2x=0\) 与 \(Ax=0\) 核空间比较、向量组表示反求参数和相似变换下特征向量传递入口补强。
- wiki_updated: 新建 `MATHWIKI-LA-METHOD-013_矩阵秩约束与分块秩比较.md`、`MATHWIKI-LA-METHOD-014_齐次方程组核空间与向量组表示.md`；更新 `MATHWIKI-LA-METHOD-005_相似对角化判定与特征向量换基.md`、`MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线.md`、`MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: 正式卡补入稳定 `lecture_refs`、轻量题目摘要、标准答案、知识点、方法入口、陷阱和复做提醒；可视化详情页保留题图可见、解析折叠，并补齐题目定位、正确第一步、核心方法、易错触发、方法页和 Obsidian bridge 入口。
- tutor_safe_update: 新增“AB 反求 BA 训练项”“分块秩比较训练项”“伴随矩阵秩约束训练项”“齐次方程组核空间比较训练项”“向量组表示反求参数训练项”“相似变换特征向量传递训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图、解析图和正式卡轻量字段补强可确认学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1763，medium=707，weak_audit=495；LLM Wiki coverage 刷新成功，source summaries=770，knowledge_clusters=351，method_clusters=890，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`LA-068`、`LA-070`、`LA-073`、`LA-090`、`LA-099`、`LA-103` 六张卡 `intake_quality_gate --visual expected` 均为 `quality_gate=ok`；`manifest.json`、`asset_to_obsidian.json` 和 bridge records JSON 均合法；HTTP bridge health 为 ok，6 个 open URL 均返回 200。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代相似形式、循环基坐标与秩不变量视觉解析闭环 LA-111/116/117
- scope: [LA-111](http://127.0.0.1:8765/open/LA-111), [LA-116](http://127.0.0.1:8765/open/LA-116), [LA-117](http://127.0.0.1:8765/open/LA-117)。
- evidence: 3 题均已有正式错题卡和可视化详情页；题图与解析图支持互异特征值的普通相似形式、\(P=(\alpha,A\alpha)\) 循环基坐标矩阵、同特征值矩阵用 \(r(A-\lambda E)\) 区分 Jordan 结构的入口补强。
- wiki_updated: 更新 `MATHWIKI-LA-METHOD-005_相似对角化判定与特征向量换基.md`、`MATHWIKI-LA-METHOD-012_矩阵方程按列拆与解空间参数化.md`、`MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线.md`、`MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-111` 补入 \(A=P\Lambda P^{-1}\) 与正交相似、合同、左右乘可逆矩阵的边界；`LA-116` 补入 \(AP=PB\) 按列写坐标矩阵入口；`LA-117` 补入重特征值下继续比较 \(r(A-\lambda E)\) 的相似不变量入口。
- tutor_safe_update: 新增“相似形式辨析训练项”“循环基坐标矩阵训练项”“同特征值矩阵秩不变量训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图、解析图和正式卡轻量字段补强可确认学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1770，medium=712，weak_audit=495；LLM Wiki coverage 刷新成功，source summaries=770，knowledge_clusters=351，method_clusters=909，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`LA-111`、`LA-116`、`LA-117` 三张卡 `intake_quality_gate --visual expected` 均为 `quality_gate=ok`；`manifest.json`、`asset_to_obsidian.json` 和 bridge records JSON 均合法；HTTP bridge health 为 ok，3 个 open URL 均返回 200。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代矩阵多项式、特征空间换基与按列读特征向量视觉解析闭环 LA-104/105/106
- scope: [LA-104](http://127.0.0.1:8765/open/LA-104), [LA-105](http://127.0.0.1:8765/open/LA-105), [LA-106](http://127.0.0.1:8765/open/LA-106)。
- evidence: `LA-104`、`LA-105` 有正式错题卡、题图和解析图；`LA-106` 有正式错题卡、题图和旧卡摘要，未检测到单独解析图。证据支持矩阵多项式转特征值、特征空间内换基判定、矩阵乘法按列读特征向量的入口补强；缺少用户本人作答过程。
- wiki_updated: 新建 `MATHWIKI-LA-METHOD-015_矩阵多项式与特征值映射.md`；更新 `MATHWIKI-LA-METHOD-005_相似对角化判定与特征向量换基.md`、`MATHWIKI-LA-METHOD-012_矩阵方程按列拆与解空间参数化.md`、`MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线.md`、`MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-104` 补入 \(f(A)=0\Rightarrow f(\lambda)=0\)、\(|A|\) 定重数和二次型规范形正负惯性指数；`LA-105` 补入 \(P^{-1}AP=\Lambda\) 后逐列检查特征空间、同一特征空间内可换基、不同特征值不可混合；`LA-106` 补入 \(AB=\lambda B\) 按列读、\(CA^{\mathsf T}=\lambda C\) 先转置再按列读、最后用秩确认特征空间维数。
- tutor_safe_update: 新增“矩阵多项式特征值映射训练项”“特征空间内换基训练项”“按列读特征向量训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图、解析图、旧卡摘要和正式卡轻量字段补强可确认学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1780，medium=705，weak_audit=495；LLM Wiki coverage 顺序刷新成功，source summaries=770，compiled=728，knowledge_clusters=351，method_clusters=909，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`LA-104`、`LA-105`、`LA-106` 三张卡 `intake_quality_gate --visual expected` 均为 `quality_gate=ok`；`manifest.json`、`asset_to_obsidian.json` 和 bridge records JSON 均合法；HTTP bridge health 为 ok，3 个 open URL 均返回 200。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线代行和谱投影与递推向量化视觉解析闭环 LA-113/118
- scope: [LA-113](http://127.0.0.1:8765/open/LA-113), [LA-118](http://127.0.0.1:8765/open/LA-118)。
- evidence: 两题均已有正式错题卡和题图，未检测到单独解析图；题图可读，分别支持“行和给特征向量 + 实对称正交补 + 谱投影求幂”和“多元递推向量化 + 相似对角化求 \(A^n\alpha_0\)”的入口补强。缺少用户本人作答过程。
- wiki_updated: 更新 `MATHWIKI-LA-METHOD-005_相似对角化判定与特征向量换基.md`、`MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`MATHWIKI-LA-TOPIC-004_二次型与特征结构错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-113` 补入每行元素和为 \(3\) 时 \(A(1,1,1)^{\mathsf T}=3(1,1,1)^{\mathsf T}\)、\(\lambda=1\) 特征空间 \(x+y+z=0\)、\(A^n=E+\frac{3^n-1}{3}J\)；`LA-118` 补入递推矩阵 \(A=\begin{pmatrix}-2&0&2\\0&-2&-2\\-6&-3&3\end{pmatrix}\)、特征值 \(-2,0,1\)、\(n\ge1\) 时 \(x_n=(-2)^n+8,\ y_n=-2(-2)^n-8,\ z_n=12\)。
- tutor_safe_update: 新增“行和实对称谱投影训练项”和“多元递推矩阵化训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图和正式卡轻量字段补强可确认学习入口，不从题图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1787，medium=701，weak_audit=497；LLM Wiki coverage 顺序刷新成功，source summaries=770，compiled=730，knowledge_clusters=350，method_clusters=909，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；`LA-113`、`LA-118` 两张卡 `intake_quality_gate --visual expected` 均为 `quality_gate=ok`；`manifest.json`、`asset_to_obsidian.json` 和 bridge records JSON 均合法；HTTP bridge health 为 ok，2 个 open URL 均返回 200；Obsidian CLI 已确认 `kaoyan-math` vault 可用，并可读取 `VIS-LA-113`；`wrongnet.py related` 与 `knowledge 相似矩阵/实对称矩阵` 均能召回本批对应题。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点。
- rollback_action: not_run。

## 2026-07-02｜线性方程组解情形、公共非零解与同解判定视觉解析闭环 LA-082/087/088/089
- scope: [LA-082](http://127.0.0.1:8765/open/LA-082), [LA-087](http://127.0.0.1:8765/open/LA-087), [LA-088](http://127.0.0.1:8765/open/LA-088), [LA-089](http://127.0.0.1:8765/open/LA-089)。
- evidence: 四题均已有正式错题卡、题图和解析图；证据支持 Vandermonde 型含参方程组解情形、链式向量方程先识别 \(\beta\) 的特征向量身份、公共非零解转拼接矩阵秩判定、矩阵多项式推出可逆因子和同解变形入口。缺少用户本人作答过程。
- wiki_updated: 新建 `MATHWIKI-LA-METHOD-016_线性方程组同解与公共解判定.md`；更新 `MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线.md`、`wiki/index.md`、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `LA-082` 补入增广矩阵行变换、参数退化分类和 \(r(A),r(A,b),n\) 解情形判定；`LA-087` 补入 \(A^2\alpha=A(A\alpha)\) 联立推出 \(A\beta=\beta\)；`LA-088` 补入 \(r(BA)\le1\) 与上下拼接矩阵公共核空间；`LA-089` 补入 \((A-2E)(A+E)=E\) 可逆因子和同解/不同解判定。
- tutor_safe_update: 新增“线性方程组解情形训练项”“链式向量方程训练项”“公共非零解拼接矩阵训练项”“齐次方程组同解变形训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: evidence-backed-refinement-only；只根据题图、解析图和正式卡轻量字段补强可确认学习入口，不从解析图反推用户个人错因、掌握度或 `method_gap`。
- validation: `wrongnet.py rebuild` 成功，cards=770，strong=1793，medium=703，weak_audit=497；LLM Wiki coverage 顺序刷新成功，source summaries=770，compiled=735，knowledge_clusters=350，method_clusters=916，error_clusters=266，action_gap_clusters=8；bridge snapshot 刷新成功，records=873，assets=1253；四张卡 `intake_quality_gate --visual expected` 均为 `quality_gate=ok`；`manifest.json`、`asset_to_obsidian.json` 和 bridge records JSON 均合法；HTTP bridge 四个 open URL 均返回 200；Obsidian CLI 已确认 `kaoyan-math` vault 可用，并可读取 `VIS-LA-082`；`wrongnet.py related` 与 `knowledge 线性方程组` 均能召回本批对应题。
- quality_note: 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，属于本批正确边界，因为缺少用户本人作答过程，不能编造个人错因、掌握度或方法断点；另修正 `LA-082` 正式卡中行等价符号，避免矩阵行变换的 `\sim` 被误识别为“等价无穷小”，重建后 `knowledge 线性方程组` 已确认 `LA-082` 不再错误挂载“等价无穷小”。
- rollback_action: not_run。

## 2026-07-02｜根式积分换元与回代链视觉解析闭环 GS-610/618/619/620/631
- scope: [GS-610](http://127.0.0.1:8765/open/GS-610), [GS-618](http://127.0.0.1:8765/open/GS-618), [GS-619](http://127.0.0.1:8765/open/GS-619), [GS-620](http://127.0.0.1:8765/open/GS-620), [GS-631](http://127.0.0.1:8765/open/GS-631)。
- evidence: 五题均已有正式错题卡、题图和解析图；证据支持根式复合整体换元、根式幂次统一、三角代换中段化简、换元后反解原变量、部分分式与回代链补强。缺少新的用户本人作答过程，因此不改掌握度、不新增个人错因。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-043_根式积分换元与回代链.md`；更新 `MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线.md`、`MATHWIKI-GS-METHOD-039_不定积分结构化化归入口.md`、`wiki/index.md`、五个可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `GS-610` 补入 \(\sqrt{e^x-1}\) 完整根式整体换元与 \(dx\) 同步替换；`GS-618` 补入 \(\sqrt{1+x^2}\) 的凑微分/三角换元回代边界；`GS-619` 补入三角代换后 \(\tan t,\sec t\) 到 \(\sin t,\cos t\) 的中段化简；`GS-620` 补入分数幂统一和 \(d(x^{3/2})\) 触发；`GS-631` 补入根式套分式整体换元、反解 \(x\) 与部分分式收口。
- tutor_safe_update: 新增“根式积分换元与回代链训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: visual-wiki-navigation-only / evidence-backed-refinement-only；本批不修改正式错题卡，不修改生成目录，不运行 wrongnet rebuild，不写回滚 JSON。
- validation: `manifest.json` 与 `asset_to_obsidian.json` 均可解析；目标 wiki/index 行均为 10 列，目标可视化 index 行均为 13 列；bridge snapshot 刷新成功，records=873，assets=1253；HTTP bridge health 为 ok，五个 open URL 均返回 200；Obsidian CLI 已确认 `kaoyan-math` vault 可用，并可读取 `MATHWIKI-GS-METHOD-043`，搜索可召回五个可视化详情页、专题总线、Tutor 安全输入包和 wiki 索引；五张卡 `intake_quality_gate --visual expected` 均为 `quality_gate=ok`。
- quality_note: `GS-618` 质量门保留 `method_gap.expected_first_action may not be an executable first-action sentence` 警告，属于既有正式卡字段表达提示，不在本批 visual/wiki 补强范围内强改；`GS-631` 的日志缺失提示已由本条日志补齐。
- rollback_action: not_run。

## 2026-07-02｜方向导数与梯度入口判别链视觉解析闭环 GS-652/653/654/656/657
- scope: [GS-652](http://127.0.0.1:8765/open/GS-652), [GS-653](http://127.0.0.1:8765/open/GS-653), [GS-654](http://127.0.0.1:8765/open/GS-654), [GS-656](http://127.0.0.1:8765/open/GS-656), [GS-657](http://127.0.0.1:8765/open/GS-657)。
- evidence: 五题均已有正式错题卡、题图和解析图；证据支持普通方向导数求值、最大方向导数、两个方向导数反推梯度、所有方向导数存在性陷阱、含参最大方向比例条件的入口判别链。缺少新的用户本人作答过程，因此不改掌握度、不新增个人错因。
- wiki_updated: 新建 `MATHWIKI-GS-METHOD-044_方向导数与梯度入口判别链.md`；更新 `MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`MATHWIKI-GS-METHOD-024_方向导数梯度点乘.md`、`MATHWIKI-GS-METHOD-025_最大方向导数梯度模.md`、`MATHWIKI-GS-METHOD-026_方向导数反推梯度.md`、`MATHWIKI-GS-METHOD-028_方向导数存在性陷阱.md`、`MATHWIKI-GS-METHOD-029_最大方向导数比例条件.md`、`wiki/index.md`、五个可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- update: `GS-652` 收口“梯度点乘单位方向”；`GS-653` 收口“最大方向导数等于梯度模”；`GS-654` 收口“设梯度未知量并由两个方向导数列方程”；`GS-656` 收口“方向导数存在不推出连续/可微，需另查路径或定义”；`GS-657` 收口“最大方向用梯度与给定方向同向，再联立梯度模”。
- tutor_safe_update: 新增“方向导数与梯度入口判别链训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: visual-wiki-navigation-only / evidence-backed-refinement-only；本批不修改正式错题卡，不修改生成目录，不运行 wrongnet rebuild，不写回滚 JSON。
- validation: `manifest.json` 与 `asset_to_obsidian.json` 均可解析；目标 wiki/index 行均为 10 列，目标可视化 index 行均为 13 列；bridge snapshot 刷新成功，records=873，assets=1253；HTTP bridge health 为 ok，五个 open URL 均返回 200；Obsidian CLI 已确认 `kaoyan-math` vault 可用，并可读取 `MATHWIKI-GS-METHOD-044`，搜索可召回五个可视化详情页、专题总线、Tutor 安全输入包和 wiki 索引；五张卡 `intake_quality_gate --visual expected` 均为 `quality_gate=ok`，且无 ERROR、无 WARN；`git diff --check` 通过。
- quality_note: 本批质量门无警告；因只做 visual/wiki 导航与高层方法链补强，没有触碰用户个人错因、掌握度、正式错题卡或回滚账本。
- rollback_action: not_run。

## 2026-07-02｜曲率题变量对象判别链正式卡修正与视觉解析闭环 GS-529/539/650
- scope: [GS-529](http://127.0.0.1:8765/open/GS-529), [GS-539](http://127.0.0.1:8765/open/GS-539), [GS-650](http://127.0.0.1:8765/open/GS-650)。
- evidence: 三题均已有正式错题卡和可视化详情页；`GS-529`、`GS-539` 的正式卡 `method_gap` 与当前曲率错点不匹配，本批按正式卡 wrong_point 与视觉解析修正；`GS-650` 的正式卡 `method_gap` 已准确，未改正式卡。
- card_updated: 修正 `GS-529`、`GS-539` 的 `method_gap` 与正文方法断点；不改答案、错因历史、掌握度或回滚字段。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-047_曲率题变量对象判别链.md`，收口曲率圆、曲率半径弧长参数和参数曲线曲率的变量对象判别。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、四个视觉详情页（含 `MN4-GS-CH01-200` 来源页与 `VIS-GS-650` 正式页）、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“曲率题变量对象判别链训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-method-gap-correction + visual/wiki navigation enhancement；只修正可由正式卡和视觉解析确认的入口链，不编造新的个人错因或掌握度。
- validation: `GS-529`、`GS-539` 已分别通过 `intake_closeout.py --visual expected`，均完成 wrongnet 重建、wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新和质量门检查；`GS-650` 通过 `intake_quality_gate --visual expected`；最终 bridge snapshot 刷新成功，records=873，assets=1253；`manifest.json` 与 `asset_to_obsidian.json` 均可解析；索引中 `MATHWIKI-GS-METHOD-047`、`VIS-GS-529`、`VIS-GS-539`、`VIS-GS-650` 均已登记。
- quality_note: 三题质量门均为 `quality_gate=ok`，无 ERROR、无 WARN；`GS-650` 来源页与正式视觉详情页同时补链，但不重复建正式卡。
- rollback_action: not_run。

## 2026-07-02｜渐近线题全类型检查链正式卡修正与视觉解析闭环 GS-459/460/497/500
- scope: [GS-459](http://127.0.0.1:8765/open/GS-459), [GS-460](http://127.0.0.1:8765/open/GS-460), [GS-497](http://127.0.0.1:8765/open/GS-497), [GS-500](http://127.0.0.1:8765/open/GS-500)。
- evidence: 四题均已有正式错题卡与可视化详情页；原正式卡 `method_gap` 均停留在“问渐近线 -> 垂直看函数趋∞处”的泛化入口，本批按正式卡 `wrong_point` 和视觉解析修正为每题真实漏掉的第一动作。
- card_updated: 修正四题正式卡 `method_gap` 与正文 `## 方法断点`：`GS-459` 补“参数方程先找无穷远对应 \(t\to-1\)”；`GS-460` 补“差值极限有限先反推 \(a=4\)”；`GS-497` 补“极值点立即回代，斜渐近线继续求 \(b\)”；`GS-500` 补“全部渐近线先列定义域端点、正无穷、负无穷检查表”。
- correction: 修正 `GS-500` 可视化解析中正负无穷方向斜渐近线截距常数项，将误写的 \(\frac{\ln^2 2}{4}\) 改为 \(\frac{\ln2}{4}\)，与正式错题卡和实际展开一致。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-048_渐近线题全类型检查链.md`，收口全部渐近线、参数方程斜渐近线、根式差值极限、正负无穷斜渐近线四类入口。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md`、`MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、四个可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“渐近线题全类型检查链训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-method-gap-correction + visual/wiki navigation enhancement；只修正可由正式卡与视觉解析确认的入口链，不编造新的个人错因、掌握度或回滚安排。
- validation: `GS-459`、`GS-460`、`GS-497`、`GS-500` 已分别通过 `intake_closeout.py --visual expected`，均完成 wrongnet 重建、wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新和质量门检查；`GS-497` 首次收口的第一动作句式警告已修正并重跑通过；四题最终 `quality_gate=ok`，无 ERROR、无 WARN。
- quality_note: 本批正式卡、视觉详情、主题总线、方法页、Tutor 安全输入和桥接索引均已同步；不修改回滚 JSON，不修改掌握度。
- rollback_action: not_run。

## 2026-07-02｜渐近线题全类型检查链补齐 GS-024/151
- scope: [GS-024](http://127.0.0.1:8765/open/GS-024), [GS-151](http://127.0.0.1:8765/open/GS-151)。
- evidence: 两题均已有正式错题卡和可视化详情页；`GS-024` 的正式卡 `method_gap` 误停留在导数定义/一阶微分入口，实际是斜渐近线截距主量提出断点；`GS-151` 的正式卡入口过窄，只写“垂直看函数趋∞处”，实际断点是渐近线条数题先列定义域端点与正负无穷检查表。
- card_updated: 修正两题正式卡 `wrong_point`、`methods`、`traps`、`method_gap` 与正文 `## 方法断点`：`GS-024` 补“先求 \(k\)，再把 \(y-x\) 化成 \(x[(1+\frac1x)^{3/2}-1]\)”；`GS-151` 补“先由 \(x^2-1>0\) 列 \(x=\pm1\)、\(x\to+\infty\)、\(x\to-\infty\) 四个检查点”。
- wiki_updated: 扩展 `MATHWIKI-GS-METHOD-048_渐近线题全类型检查链.md` 到 6 道渐近线题；更新 `MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md`、`MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、两道可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 渐近线训练项补入“截距主量提出”和“条数题正负无穷检查表”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-method-gap-correction + visual/wiki navigation enhancement；只修正可由正式卡与视觉解析确认的入口链，不编造新的个人错因、掌握度或回滚安排。
- validation: `GS-024`、`GS-151` 已分别通过 `intake_closeout.py --visual expected`，均完成 wrongnet 重建、wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新和质量门检查；两题最终 `quality_gate=ok`，无 ERROR、无 WARN。
- rollback_action: not_run。

## 2026-07-02｜导数定义与分段点可导性链正式卡修正与视觉解析闭环 GS-463/530/461/470/472
- scope: [GS-463](http://127.0.0.1:8765/open/GS-463), [GS-530](http://127.0.0.1:8765/open/GS-530), [GS-461](http://127.0.0.1:8765/open/GS-461), [GS-470](http://127.0.0.1:8765/open/GS-470), [GS-472](http://127.0.0.1:8765/open/GS-472)。
- evidence: 五题均已有正式错题卡和可视化详情页；正式卡正文和视觉解析能确认真实入口分别是增量除以增量、周期切点转导数定义、绝对值分段比较左右高阶导、振荡因子临界指数、指数平坦函数分段点定义归纳。
- card_updated: 修正五题正式卡 `method_gap`：`GS-463` 从微分方程分类改为导数定义增量差商；`GS-530` 改为周期转化后减基点、除真实增量；`GS-461` 改为绝对值先分段；`GS-470` 改为先写 \(x^{k-1}\sin\frac1x\) 并标出 \(k=1\)；`GS-472` 改为分段点高阶导先回到定义。
- wiki_updated: 扩展 `MATHWIKI-GS-METHOD-013_导数定义差商入口.md`，更新 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、五个可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“导数定义与分段点可导性训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-method-gap-correction + visual/wiki navigation enhancement；只修正可由正式卡与视觉解析确认的入口链，不编造新的个人错因、掌握度或回滚安排。
- validation: 五题均已通过 `intake_closeout.py --visual expected`，完成 wrongnet rebuild、wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终 quality_gate=ok，ERROR/WARN 均为 none。
- rollback_action: not_run。

## 2026-07-02｜连续间断点候选点检查链正式卡修正与视觉解析闭环 GS-031/035/036/037/038
- scope: [GS-031](http://127.0.0.1:8765/open/GS-031), [GS-035](http://127.0.0.1:8765/open/GS-035), [GS-036](http://127.0.0.1:8765/open/GS-036), [GS-037](http://127.0.0.1:8765/open/GS-037), [GS-038](http://127.0.0.1:8765/open/GS-038)。
- evidence: 五题均已有正式错题卡和可视化详情页；证据支持分式函数间断点个数、根号平方绝对值尖点、连续性运算法则、含参极限分段连续性、幂指函数第一类间断点候选点检查链。
- card_updated: `GS-031` 补强分母辅助函数、求导判单调和介值定理数零点；`GS-035` 修正 `method_gap.expected_first_action` 为“先写出 \(\sqrt{(x-1)^2}=|x-1|\)”；`GS-036` 补入连续性运算法则入口；`GS-037` 补入按 \(|x|>1\)、\(|x|<1\)、\(x=\pm1\) 分段求极限函数；`GS-038` 只按题图/解析补强方法入口和候选点链，不编造个人错因或 `method_gap`。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-049_连续间断点候选点检查链.md`。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md`、`wiki/index.md`、五个可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“连续间断点候选点检查链训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-method-gap-correction + visual/wiki navigation enhancement；`GS-038` 因缺少用户本人作答过程，保留 `暂无明确个人错因`、不启用 `method_gap`，这是质量边界不是漏填。
- validation: 五题均已通过 `intake_closeout.py --visual expected`，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终 rebuild 结果 cards=770，strong=1817，medium=695，weak_audit=483；bridge snapshot records=873，assets=1253。
- quality_note: `GS-038` 质量门保留 `error_causes is placeholder or empty` 与 `method_gap not enabled` 警告，原因是不能从题图/解析反推用户个人错因；其余四题按正式卡与视觉解析完成可确认入口链修正。
- rollback_action: not_run。

## 2026-07-02｜空间直线平面向量角色判别链正式卡修正与视觉解析闭环 GS-627/628/629
- scope: [GS-627](http://127.0.0.1:8765/open/GS-627), [GS-628](http://127.0.0.1:8765/open/GS-628), [GS-629](http://127.0.0.1:8765/open/GS-629)。
- evidence: 三题均已有正式错题卡、题图和解析图；证据支持“平面点法式与叉乘求法向量”“直线投影辅助平面”“两平面交线方向向量”三类空间解析几何入口判别。
- card_updated: `GS-627` 将 `related` 从待补充改为 `GS-628`、`GS-629`；`GS-628` 补入 `GS-629` 关联；三题 `mastery_history` 统一规范为 `AI评分` 表述，关键词同步为 `掌握度AI评分`，未新增未经确认的个人错因。
- wiki_updated: 扩展 `MATHWIKI-GS-METHOD-045_空间解析几何对象判别链.md` 到七类对象判别；更新 `MATHWIKI-GS-TOPIC-012_空间解析几何错题总线.md`、`wiki/index.md`、三道可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- correction: 修正 `VIS-GS-629` 原误链 `MATHWIKI-GS-METHOD-017_参数曲线切线点向式`，改为 `MATHWIKI-GS-METHOD-045_空间解析几何对象判别链`。
- tutor_safe_update: 空间解析几何对象判别链训练项补入平面方程、直线投影、两直线夹角三类入口；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-relation-and-wording-correction + visual/wiki navigation enhancement；不修改回滚 JSON，不修改生成目录源码。
- validation: `GS-627`、`GS-628`、`GS-629` 已分别通过 `intake_closeout.py --visual expected`，均完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；三题最终 `quality_gate=ok`，无 ERROR、无 WARN；最终 bridge snapshot records=873，assets=1253；目标 bridge open URL 均返回 200；目标 wiki/index 行均为 10 列，目标可视化 index 行均为 13 列；`manifest.json` 与 `asset_to_obsidian.json` 均可解析；`git diff --check` 通过。
- progress_note: 今日日志闭环记录增至 38 条；按可视化题库唯一题号口径，未出现在今日加强日志中的题约 583 道；按本轮严格候选口径，剩余约 447 道。
- rollback_action: not_run。

## 2026-07-02｜幂零链线性无关与核空间秩稳定证明闭环 LA-094
- scope: [LA-094](http://127.0.0.1:8765/open/LA-094)。
- evidence: 题图与解析图均已存在；题目要求证明 \(A^{k-1}a\ne0,A^ka=0\) 时 \(a,Aa,\ldots,A^{k-1}a\) 线性无关，并证明 \(r(A^{n+1})=r(A^n)\)。旧正式卡仍为 OCR 占位，本轮依据题图/解析补全轻量摘要、标准答案、证明入口和复做提醒。
- card_updated: `LA-094` 从“题干为图片/OCR 待核对/待补充”补成幂零链线性无关与核空间秩稳定证明题；保留 `暂无明确个人错因`，不从解析图反推掌握度或 `method_gap`。
- wiki_updated: 扩展 `MATHWIKI-LA-METHOD-011_矩阵幂降维与秩空间判断.md`、`MATHWIKI-LA-TOPIC-001_线代矩阵运算错题总线.md`、`MATHWIKI-LA-TOPIC-003_线性方程组与向量组错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 矩阵幂降维与秩空间判断训练项补入 `LA-094`，只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- validation: `intake_closeout.py --id LA-094 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终 `quality_gate=ok`，仅保留“个人错因占位、method_gap 未启用”的预期提醒；重建结果 cards=770，strong=1828，medium=708，weak_audit=483，source summaries=770，compiled=749，knowledge_clusters=350，method_clusters=956，error_clusters=266，action_gap_clusters=8，bridge snapshot records=873，assets=1253。
- progress_note: 按今天日志 scope 的唯一题号口径，已闭环约 164/732，道剩余约 568；按本轮严格候选口径，剩余约 446。
- rollback_action: not_run。

## 2026-07-02｜LA-003 错分归并与函数不等式导数判号链闭环 GS-256
- scope: [GS-256](http://127.0.0.1:8765/open/GS-256), [LA-003](http://127.0.0.1:8765/open/LA-003)。
- evidence: `VIS-GS-256`、`VIS-LA-003` 与 `MN4-GS-CH01-341` 的题图/解析均指向同一道高数对数不等式证明；`LA-003` 原为线代错分来源，已确认不应作为独立线代题维护。
- card_updated: `GS-256` 从粗略旧卡修正为“对数不等式证明”，补入同号证明、导数判单调、二级辅助函数和参数最小值判号入口；`LA-003` 改为重复占位卡，正式复做入口并入 `GS-256`。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-051_函数不等式导数判号链.md`，沉淀 \((x-a)f(x)\ge0\) 型乘积非负证明的第一动作。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、`SRC-WQ-GS-256`、`SRC-WQ-LA-003`、三条可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_relink: `VIS-LA-003` 与 `MN4-GS-CH01-341` 均移动到高等数学可视化目录并标记 `merged_into_wrongnet`，统一指向 `GS-256`；`VIS-GS-256` 保持 `linked_wrongnet`。
- tutor_safe_update: 新增“函数不等式导数判号训练项”；只写高层第一动作、判号链和来源 ID，不复制完整题干或长解析。
- card_decision: formal-card-correction + duplicate-merge + visual/wiki navigation enhancement；由于只有题图/解析证据，没有用户当时作答过程，保留 `暂无明确个人错因` 且不启用 `method_gap`。
- validation: `intake_closeout.py --id GS-256 --visual expected` 已通过，完成 wrongnet rebuild、wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终 `quality_gate=ok`。预期警告仅为个人错因占位和 `method_gap` 未启用，原因是不从解析图反推个人错因。
- progress_note: 当前可视化 manifest 统计为 records=873、linked_wrongnet=731、merged_into_wrongnet=131、needs_card_decision=10、needs_manual_relink=1；linked 队列中 2026-07-02 已闭环 165 条，剩余约 566 条。
- rollback_action: not_run。

## 2026-07-02｜局部性质与导数符号单向判别链闭环 GS-142
- scope: [GS-142](http://127.0.0.1:8765/open/GS-142)。
- evidence: 题图与解析图已存在；题目为 2022 年数二第三题，要求判断局部单调、局部凹凸与 \(f'(x_0)\)、\(f''(x_0)\) 点处符号之间的命题真伪；解析确认正确选项为 B，A/C/D 分别用反例或保号条件缺失排除。
- card_updated: `GS-142` 从 OCR/待补充占位卡补全为“导数符号与局部单调凹凸判断”正式卡，写入答案 B、选项排除、反例链和复做提醒；保留 `暂无明确个人错因`，不从解析图反推用户第一错步。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-052_局部性质与导数符号单向判别.md`。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“局部性质与导数符号单向判别训练项”；只写题面信号、第一动作、反例方向和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-placeholder-repair + visual/wiki navigation enhancement；缺少用户当时作答过程，因此 `method_gap` 保持 disabled。
- validation: `intake_closeout.py --id GS-142 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终重建结果 cards=770，strong=1832，medium=706，weak_audit=472，knowledge_clusters=351，method_clusters=959，bridge snapshot records=873，assets=1253。
- quality_note: 质量门为 `quality_gate=ok`，无 ERROR；保留“个人错因占位、method_gap 未启用”的预期 WARN，原因是不能从题图/解析反推用户本人第一错步。
- progress_note: 当前可视化 manifest 统计为 linked_wrongnet=731；linked 队列中 2026-07-02 已闭环约 166 条，剩余约 565 条。
- rollback_action: not_run。

## 2026-07-02｜导数定义型极限量级判可导闭环 GS-087
- scope: [GS-087](http://127.0.0.1:8765/open/GS-087)。
- evidence: 题图与解析图已存在；题目为强化例题 3.2，要求判断 \(\frac{f(x)}{\sqrt[3]{x}}\)、\(\frac{f(x)}{x^2}\) 的极限条件与 \(x=0\) 处可导之间的命题真假；解析确认正确答案为 A，只有命题 2 为真。
- card_updated: `GS-087` 从 OCR/待补充占位卡补全为“导数定义型极限命题判断”正式卡，写入答案 A、导数定义差商入口、分母阶数比较、反例排除和复做提醒；保留 `暂无明确个人错因`，不从解析图反推用户第一错步。
- wiki_updated: 扩展 `MATHWIKI-GS-METHOD-013_导数定义差商入口.md` 与 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`；更新 `wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“导数定义型极限反推训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-placeholder-repair + visual/wiki navigation enhancement；缺少用户当时作答过程，因此 `method_gap` 保持 disabled。
- validation: `intake_closeout.py --id GS-087 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终重建结果 cards=770，strong=1835，medium=705，weak_audit=472，knowledge_clusters=351，method_clusters=962，bridge snapshot records=873，assets=1253。
- quality_note: 质量门为 `quality_gate=ok`，无 ERROR；保留“个人错因占位、method_gap 未启用”的预期 WARN，原因是不能从题图/解析反推用户本人第一错步。
- rollback_action: not_run。

## 2026-07-02｜质心横坐标积分比值证明链闭环 GS-247
- scope: [GS-247](http://127.0.0.1:8765/open/GS-247)。
- evidence: 题图与解析图已存在；题目为 1000题B组10.24 / ID:84256，要求证明平板 \(D\) 的质心横坐标满足 \(\bar{x}>\frac23a\)，解析确认入口为质心横坐标公式、变量上限辅助函数和拉格朗日中值定理判号。
- card_updated: `GS-247` 从“积分型问题/OCR 待核对/待补充”薄卡补全为“质心横坐标积分不等式证明”正式卡；写入面积矩公式、交叉相乘、构造 \(F(u)\)、用 \(f(0)=0\)、\(f''>0\) 和拉格朗日中值定理证明 \(F''(u)>0\) 的方法入口。
- wiki_created: 新建并升级 `MATHWIKI-GS-METHOD-053_质心横坐标积分比值证明链.md`；页面标题为“质心横坐标积分比值证明链”。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“质心横坐标积分比值证明链训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-placeholder-repair + visual/wiki navigation enhancement；缺少用户当时作答过程，因此 `method_gap` 保持 disabled。
- validation: `intake_closeout.py --id GS-247 --source '1000题B组10.24' --knowledge 定积分应用 --knowledge 平面图形面积 --knowledge 中值定理 --knowledge 拉格朗日中值定理 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终重建结果 cards=770，strong=1841，medium=705，weak_audit=472，knowledge_clusters=351，method_clusters=965，bridge snapshot records=873，assets=1253。
- quality_note: 旧卡未记录个人错因与作答过程，故保留 `暂无明确个人错因`、`待评分`，不反推掌握度或个人 method_gap。
- rollback_action: not_run。

## 2026-07-02｜平移差分定积分区间转化闭环 GS-186
- scope: [GS-186](http://127.0.0.1:8765/open/GS-186)。
- evidence: 题图与解析图已存在；题目为 2023 年第 15 题，条件为 \(f(x+2)-f(x)=x\)、\(\int_0^2 f(x)\,dx=0\)，要求计算 \(\int_1^3 f(x)\,dx\)。解析确认入口为区间拆补、平移换元和差分关系代入，结果为 \(\frac12\)。
- card_updated: `GS-186` 从“题干为图片/OCR 待核对/待补充”薄卡补全为“平移差分定积分求值”正式卡；写入 \(\int_1^3 f=\int_2^3 f-\int_0^1 f\)、令 \(x=u+2\) 与 \(\int_0^1[f(u+2)-f(u)]\,du\) 的方法入口。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-054_平移差分定积分区间转化.md`。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“平移差分定积分区间转化训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-placeholder-repair + visual/wiki navigation enhancement；缺少用户当时作答过程，因此 `method_gap` 保持 disabled。
- validation: `intake_closeout.py --id GS-186 --source '2023年第15题' --knowledge 定积分 --knowledge 定积分等式 --knowledge 一元函数积分学的计算 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终重建结果 cards=770，strong=1848，medium=708，weak_audit=469，knowledge_clusters=351，method_clusters=968，bridge snapshot records=873，assets=1253。
- quality_note: 旧卡未记录个人错因与作答过程，故保留 `暂无明确个人错因`、`待评分`，不反推掌握度或个人 method_gap；质量门预期 WARN 仅为个人错因占位与 `method_gap` 未启用。
- rollback_action: not_run。

## 2026-07-02｜导函数图像判拐点闭环 GS-139
- scope: [GS-139](http://127.0.0.1:8765/open/GS-139)。
- evidence: 题图与解析图已存在；题目为 1000题B组5.21，给出 \(f'(x)\) 的图像，要求判断 \(y=f(x)\) 的拐点个数；解析确认可疑点为 \(x_1,0,x_2\)，其中 \(x_1\)、\(0\) 对应 \(f'\) 单调性改变，\(x_2\) 只是 \(f'\) 过零点。
- card_updated: `GS-139` 从“正确答案选 B/OCR 不清楚/待补充”占位卡补全为“导函数图像判拐点”正式卡；写入答案 B、拐点个数 2、\(f'\) 正负看 \(f\) 增减、\(f'\) 增减看 \(f\) 凹凸的入口链。
- wiki_updated: 扩展 `MATHWIKI-GS-METHOD-052_局部性质与导数符号单向判别.md` 与 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`；更新 `wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 局部性质与导数符号单向判别训练项补入“导函数图像判别”：极值点看 \(f'\) 正负变号，拐点看 \(f'\) 单调性改变；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-placeholder-repair + visual/wiki navigation enhancement；缺少用户当时作答过程，因此 `method_gap` 保持 disabled。
- validation: `intake_closeout.py --id GS-139 --source '1000题B组5.21' --knowledge 一元函数微分学应用 --knowledge 凹凸性与拐点 --knowledge 单调性与极值 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终重建结果 cards=770，strong=1843，medium=706，weak_audit=472，knowledge_clusters=351，method_clusters=966，bridge snapshot records=873，assets=1253。
- quality_note: 旧卡未记录个人错因与作答过程，故保留 `暂无明确个人错因`、`待评分`，不反推掌握度或个人 method_gap。
- rollback_action: not_run。

## 2026-07-02｜复合数列极限反推闭环 GS-072
- scope: [GS-072](http://127.0.0.1:8765/open/GS-072)。
- evidence: 题图与解析图已存在；题目为 2022 年第六题，条件为 \(x_n\in[-\frac{\pi}{2},\frac{\pi}{2}]\)，考查 \(\cos(\sin x_n)\)、\(\sin(\cos x_n)\) 的极限存在性能否反推 \(\lim x_n\)、\(\lim\sin x_n\)、\(\lim\cos x_n\) 存在。解析确认真命题为 D，入口为内层值域、一一可逆性、反函数连续性和端点振荡反例。
- card_updated: `GS-072` 从“题干为图片/OCR 待核对/待补充”薄卡补全为“复合数列极限反推”正式卡；写入答案 D、\(\cos x_n\in[0,1]\)、\(\sin u\) 在 \([0,1]\) 上可逆，以及 \(x_n=(-1)^n\frac{\pi}{2}\) 统一反例。
- wiki_updated: 扩展 `MATHWIKI-GS-METHOD-022_发散数列函数变换反例.md`，新增“复合极限反推版本”；更新 `MATHWIKI-GS-TOPIC-007_数列极限错题总线.md`、`MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“复合数列极限反推训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-placeholder-repair + visual/wiki navigation enhancement；缺少用户当时作答过程，因此 `method_gap` 保持 disabled。
- validation: `intake_closeout.py --id GS-072 --source '2022年第六题' --knowledge 极限与连续 --knowledge 数列极限 --knowledge 函数极限 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终重建结果 cards=770，strong=1852，medium=704，weak_audit=469，knowledge_clusters=351，method_clusters=974，bridge snapshot records=873，assets=1253。
- quality_note: 旧卡未记录个人错因与作答过程，故保留 `暂无明确个人错因`、`待评分`，不反推掌握度或个人 method_gap；质量门预期 WARN 仅为个人错因占位与 `method_gap` 未启用。
- rollback_action: not_run。

## 2026-07-02｜等价无穷小关系命题判断闭环 GS-014
- scope: [GS-014](http://127.0.0.1:8765/open/GS-014)。
- evidence: 题图与解析图已存在；题目为 2022 年真题第一题，要求判断等价无穷小和小 \(o\) 关系命题真伪。解析确认正确选项为 C，真命题为 ①③④；② 用 \(\alpha(x)=-x,\ \beta(x)=x\) 作反例，平方等价但原量不等价。
- card_updated: `GS-014` 从“2022年真题第一题”薄卡补全为“等价无穷小命题判断”正式卡；写入答案 C、\(\sim\) 与 \(o(\cdot)\) 的定义转换、平方等价反推失败的符号反例和复做提醒。
- wiki_updated: 扩展 `MATHWIKI-GS-METHOD-012_等价无穷小使用条件.md` 与 `MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md`；更新 `wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- tutor_safe_update: 新增“等价无穷小关系命题判断”训练项；只写高层第一动作、定义转换、反例方向和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: formal-card-placeholder-repair + visual/wiki navigation enhancement；缺少用户当时作答过程，因此 `method_gap` 保持 disabled。
- validation: `intake_closeout.py --id GS-014 --source '2022年真题第一题' --knowledge 极限与连续 --knowledge 等价无穷小 --knowledge 无穷小阶数比较 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终重建结果 cards=770，strong=1852，medium=704，weak_audit=469，knowledge_clusters=351，method_clusters=974，bridge snapshot records=873，assets=1253。
- quality_note: 单独复核 `intake_quality_gate.py --id GS-014 --source '2022年真题第一题' --visual expected` 为 `quality_gate=ok`，无 ERROR；仅保留“个人错因占位、method_gap 未启用”的预期 WARN，原因是不能从题图/解析反推用户本人第一错步。
- rollback_action: not_run。

## 2026-07-02｜高阶导数奇偶周期归属修正闭环 GS-307
- scope: [GS-307](http://127.0.0.1:8765/open/GS-307)。
- evidence: 题图与解析图已存在；题目为强化例题 11.2 / ID:88806，已知 \(f(x)=e^{\sin x}+e^{-\sin x}\)，求 \(f'''(2\pi)\)。解析确认答案为 \(0\)，入口为 \(f(x)\) 为偶函数且 \(2\pi\) 周期，故 \(f'''(x)\) 为奇函数且同周期，\(f'''(2\pi)=f'''(0)=0\)。
- card_updated: `GS-307` 规范“无个人错因证据”的写法，将 `method_gap` 收口为 disabled + reason；保留正式卡轻量题目摘要和复做入口，不从解析图反推用户个人错因或掌握度。
- wiki_updated: 将 `GS-307` 从 `MATHWIKI-GS-TOPIC-006_定积分错题总线.md` 的代表行中移出，接入 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`；扩展 `MATHWIKI-GS-METHOD-003_整体函数奇偶性检查.md`，补入高阶导数特殊点取值的动作链；同步 `wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`manifest.json` 与 `asset_to_obsidian.json`。
- visual_update: `VIS-GS-307` 的章节由“定积分”修正为“一元函数微分学应用”，deep wiki 从定积分总线改为一元函数微分学应用总线，题图保持可见、解析图保持折叠。
- tutor_safe_update: 既有“高阶导数奇偶周期训练项”继续作为安全输入；本轮没有复制完整题干或长解析到 Tutor 层。
- card_decision: formal-card-boundary-normalization + topic-relink + visual/wiki navigation enhancement；缺少用户当时作答过程，因此 `method_gap` 保持 disabled。
- validation: `intake_closeout.py --id GS-307 --source '强化例题11.2 / ID:88806' --knowledge 一元函数微分学应用 --knowledge 高阶导数 --knowledge 周期函数 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终重建结果 cards=770，strong=1855，medium=701，weak_audit=469，knowledge_clusters=351，method_clusters=974，bridge snapshot records=873，assets=1253，source summaries=770，compiled=750。
- quality_note: 质量门为 `quality_gate=ok`，无 ERROR；仅保留“个人错因占位、method_gap 未启用”的预期 WARN，原因是不能从题图/解析反推用户本人第一错步。
- rollback_action: not_run。

## 2026-07-02｜变上限积分奇偶速判闭环 GS-308
- scope: [GS-308](http://127.0.0.1:8765/open/GS-308)。
- evidence: 题图与解析图已存在；题目为强化例题 11.3 / ID:105878，给出 \(f(x)=\int_0^x e^{\cos t}dt\)、\(g(x)=\int_0^{\sin x}e^{t^2}dt\)，解析确认正确答案为 C，二者均为奇函数。
- card_updated: `GS-308` 将 `wrong_point` 从“待补充”规范为“暂无明确个人错因 + 网络补强重点”，补入变上限积分奇偶速判表：\(h\) 偶则 \(H(x)=\int_0^x h(t)dt\) 奇，\(h\) 奇则 \(H\) 偶；复合上限先写成 \(H(\varphi(x))\) 再判。
- wiki_updated: 扩展 `MATHWIKI-GS-METHOD-003_整体函数奇偶性检查.md`，补入 \(F(-x)\) 定义证明和复合上限触发；更新 `MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`manifest.json` 与 `asset_to_obsidian.json`。
- tutor_safe_update: 更新数学 LLMWiki 安全输入包中的“变上限积分奇偶训练项”，只写高层速判规则和来源 ID，不复制完整题干或长解析。
- visual_update: `VIS-GS-308` 更新时间改为 2026-07-02，题图保持可见、解析图保持折叠，索引 note 改为“已复核题图/解析图；补强变上限积分奇偶速判和复合上限外层函数抽象”。
- card_decision: already_in_wrongnet_enhanced；缺少用户当时作答过程，因此 `method_gap` 保持 disabled。
- validation: `intake_closeout.py --id GS-308 --source '强化例题11.3 / ID:105878' --knowledge 定积分 --knowledge 定积分性质 --knowledge 变上限积分 --knowledge 函数奇偶性与导数性质 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终重建结果 cards=770，strong=1855，medium=701，weak_audit=469，knowledge_clusters=351，method_clusters=974，bridge snapshot records=873，assets=1253，source summaries=770，compiled=750。
- quality_note: 质量门为 `quality_gate=ok`，无 ERROR；仅保留 `method_gap not enabled` 的预期 WARN，原因是不能从题图/解析图反推用户本人第一错步。
- rollback_action: not_run。

## 2026-07-02｜无穷减无穷分式差二段收口闭环 GS-003
- scope: [GS-003](http://127.0.0.1:8765/open/GS-003)。
- evidence: 题图与解析图已存在；题目为 \(x\to0\) 时求 \(\frac{1+\int_0^x e^{t^2}dt}{e^x-1}-\frac1{\sin x}\) 的极限，解析确认先拆为变上限积分段与指数三角分式差段，结果为 \(\frac12\)。
- card_updated: `GS-003` 补清两段极限收口：\(L_1=\lim\frac{\int_0^x e^{t^2}dt}{e^x-1}=1\)，\(L_2=\lim(\frac1{e^x-1}-\frac1{\sin x})=-\frac12\)，最终 \(L=\frac12\)；新增 `GS-585`、`GS-649`、`GS-440` 为相邻题。
- wiki_updated: 扩展 `MATHWIKI-GS-METHOD-006_先判型总流程.md`，新增 \(\infty-\infty\) 型分式差变式；扩展 `MATHWIKI-GS-METHOD-012_等价无穷小使用条件.md`，补入通分后展开到二阶的加减抵消例；更新 `MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`manifest.json` 与 `asset_to_obsidian.json`。
- tutor_safe_update: 更新数学 LLMWiki 安全输入包中的“\(\infty-\infty\) 型极限拆分训练项”，只写高层拆分、通分、两段收口规则和来源 ID，不复制完整题干或长解析。
- visual_update: `VIS-GS-003` 更新时间改为 2026-07-02，题图保持可见、解析图保持折叠；`MN4-GS-CH01-003` 继续作为已并入来源证据保留。
- card_decision: already_in_wrongnet_enhanced；缺少用户当时作答过程，因此 `method_gap` 保持 disabled，错因仍为占位。
- validation: `intake_closeout.py --id GS-003 --source '2 2026.3.11 T1 / MN4-GS-CH01-003' --knowledge 极限与连续 --knowledge 函数极限 --knowledge 洛必达法则 --knowledge 泰勒公式 --knowledge 等价无穷小 --knowledge 变上限积分 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终重建结果 cards=770，strong=1858，medium=698，weak_audit=469，knowledge_clusters=351，method_clusters=975，error_clusters=267，bridge snapshot records=873，assets=1253，source summaries=770，compiled=750。
- quality_note: 质量门为 `quality_gate=ok`，无 ERROR；仅保留“错因占位、method_gap 未启用”的预期 WARN，原因是不能从题图/解析图反推用户本人第一错步。
- rollback_action: not_run。

## 2026-07-02｜多项式整除二重根条件闭环 GS-095
- scope: [GS-095](http://127.0.0.1:8765/open/GS-095)。
- evidence: 题图与答案图已存在；题目为 1000题B组4.1，核心条件是 \(f(x)+1\) 被 \((x-1)^2\) 整除、\(f(x)-1\) 被 \((x+1)^2\) 整除，答案图确认
  $$
  f(x)=\frac12(x-2)(x+1)^2+1.
  $$
- card_updated: `GS-095` 补全标准答案、题目摘要、构造路线、`mastery_history` 的 `AI评分 2/5`、真实相邻题 `GS-099/GS-035/GS-458/GS-470`，并把 `method_gap.related_method_card_id` 接到 `MATHWIKI-GS-METHOD-058`；个人错因来自既有复发记录，不从解析图反推。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-058_多项式整除二重根条件.md`，沉淀第一动作：看到 \((x-a)^2\mid[f(x)-c]\)，先写 \(f(x)-c=(x-a)^2Q(x)\)，再推出 \(f(a)=c,\ f'(a)=0\)。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`MATHWIKI-GS-METHOD-007_条件转化总流程.md`、`MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点.md`、`MATHWIKI-GS-METHOD-013_导数定义差商入口.md` 与 `wiki/index.md`。
- visual_update: `VIS-GS-095` 已复核题图/答案图，题图保持可见、答案图折叠，视觉详情页、manifest、asset map、可视化 index 和 Obsidian open-link 行均已更新到 2026-07-02。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增 `MATHWIKI-GS-METHOD-058` 来源映射和“多项式整除二重根训练项”；只写高层第一动作、商函数提醒和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced + method-gap-normalization；本题有既有复发记录，因此保留并规范 `method_gap.enabled: true`，不修改回滚 JSON。
- validation: `intake_closeout.py --id GS-095 --source '1000题B组4.1' --knowledge 一元函数微分学应用 --knowledge 多项式整除 --knowledge 二重根条件 --knowledge 导数定义 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终重建结果 cards=770，strong=1909，medium=699，weak_audit=469，knowledge_clusters=351，method_clusters=977，error_clusters=267，bridge snapshot records=873，assets=1253，source summaries=770，compiled=750。
- quality_note: closeout 质量门为 `quality_gate=ok`，无 ERROR；第一动作句式警告已通过字段修正消除，本条日志用于补齐 closeout 阶段的唯一剩余 WARN。
- progress_note: 当前可视化 manifest 统计为 records=873、linked_wrongnet=731、merged_into_wrongnet=131、needs_card_decision=10、needs_manual_relink=1；2026-07-02 已更新 linked 题约 194 道，剩余 linked 正式题约 537 道。
- rollback_action: not_run。


## 2026-07-02｜第15讲微分方程反推与建模转译链补强

- 范围：[GS-195](http://127.0.0.1:8765/open/GS-195)、[GS-197](http://127.0.0.1:8765/open/GS-197)、[GS-202](http://127.0.0.1:8765/open/GS-202)、[GS-203](http://127.0.0.1:8765/open/GS-203)、[GS-204](http://127.0.0.1:8765/open/GS-204)、[GS-205](http://127.0.0.1:8765/open/GS-205)、[GS-206](http://127.0.0.1:8765/open/GS-206)、[GS-207](http://127.0.0.1:8765/open/GS-207)。
- 新增方法页：[[MATHWIKI-GS-METHOD-060_微分方程反推与建模转译链]]。
- 处理：补强正式错题卡的旧卡边界、题图/解析图入口、视觉详情折叠解析、wiki/index、visual index、manifest、asset 映射和 Tutor 安全输入包。
- 边界：不反推用户个人错因，不修改回滚 JSON；掌握度保留待评分。
- 验证：wrongnet rebuild 已完成（cards=770，strong=1921，medium=722，weak_audit=469）；source summaries=770，compiled=750；knowledge_clusters=352；method_clusters=981，error_clusters=276，action_gap_clusters=8；bridge records=873，assets=1253；8 题 intake_quality_gate 均为 ok；已去除共享占位错因，避免“暂无明确个人错因”参与共同错因连边。

## 2026-07-02｜乘积求导零因子筛选闭环 GS-115
- scope: [GS-115](http://127.0.0.1:8765/open/GS-115)。
- evidence: 题图与解析图已存在；题目为 1000题基础篇4.2，核心是 \(f(x)=\prod_{k=1}^{n}((\ln x)^k-k)\) 在 \(x=e\) 处求导。解析图确认只有第一因子 \(\ln x-1\) 在 \(x=e\) 处为零，答案应为
  $$
  f'(e)=\frac1e(-1)^{n-1}(n-1)!.
  $$
- card_updated: `GS-115` 修正正式答案原先遗漏的 \(\frac1e\) 因子；补强 `wrong_point`、`methods`、`error_causes`、`knowledge`、`AI评分 3/5`、真实相邻题 `GS-120/GS-123/GS-307`，并启用 `method_gap`。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-061_乘积求导零因子筛选.md`，沉淀第一动作：看到多因子乘积在特殊点求导，先代点找零因子；若只有一个零因子，只保留“导零因子 × 其他非零因子”。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`manifest.json` 与 `asset_to_obsidian.json`；本轮同时发现 `MATHWIKI-GS-METHOD-059` 已有历史索引语义，故将本题新方法页顺延为 `MATHWIKI-GS-METHOD-061`。
- visual_update: `VIS-GS-115` 已复核题图/解析图，题图保持可见、解析图保持折叠；视觉详情页补入正确收口推导、入口复述和 Obsidian bridge 入口。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增 `MATHWIKI-GS-METHOD-061` 来源映射和“乘积求导零因子训练项”；只写高层第一动作、对数幂辨析和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced + answer-correction + method-gap-normalization；不修改回滚 JSON。
- validation: `intake_closeout.py --id GS-115 --source '1000题基础篇4.2' --knowledge 一元函数微分学应用 --knowledge 高阶导数 --knowledge 乘积求导 --knowledge 莱布尼茨公式 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；最终重建结果 cards=770，strong=1911，medium=698，weak_audit=469，knowledge_clusters=352，method_clusters=981，error_clusters=276，bridge snapshot records=873，assets=1253，source summaries=770，compiled=750。
- quality_note: closeout 质量门为 `quality_gate=ok`，无 ERROR、无 WARN。
- progress_note: 当前可视化 manifest 按项目脚本口径统计为 records=873、linked_wrongnet=731、merged_into_wrongnet=131、needs_card_decision=10、needs_manual_relink=1；2026-07-02 已更新正式可用视觉记录 207 条，其中 linked_wrongnet 203 条，剩余 linked_wrongnet 528 条、merged_into_wrongnet 127 条。
- rollback_action: not_run。

## 2026-07-02｜反函数积分面积比较闭环 GS-183
- scope: [GS-183](http://127.0.0.1:8765/open/GS-183)。
- evidence: 题图与解析图已存在；题目为 1000题A组6.12，设 \(f\) 单调连续且满足 midpoint 凹性条件，令 \(g=f^{-1}\)，要求判断 \(P=\int_1^2 g(x)\,dx\) 的范围；解析确认答案为 D，\(0<P<1\)。
- card_updated: `GS-183` 从旧的薄卡归属修正为“反函数积分面积比较”；写入端点弦线 \(y=1+\frac{x}{2}\)、由凹性推出 \(f(x)>1+\frac{x}{2}\)、反解得到 \(0<g(y)<2(y-1)\)，再积分放缩得到 \(0<P<1\)。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-062_反函数积分面积比较.md`，沉淀第一动作：看到反函数积分与凹凸性/端点值，先画 \(f\)、\(f^{-1}\) 和端点弦线，再做面积比较。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_update: `VIS-GS-183` 已复核题图/解析图，题图保持可见、解析图保持折叠；视觉详情页补入反函数面积、端点弦线与积分上界的复述。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增 `MATHWIKI-GS-METHOD-062` 来源映射和“反函数积分面积比较训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced + topic-relink + formal-card-boundary-normalization；缺少用户当时作答过程，因此 `method_gap` 保持 disabled，`mastery_history` 保留待评分。
- validation: `intake_closeout.py --id GS-183 --source '1000题A组6.12' --knowledge 定积分 --knowledge 定积分应用 --knowledge 平面图形面积 --knowledge 凹凸性与拐点 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；结果为 cards=770，strong=1919，medium=724，weak_audit=469，knowledge_clusters=352，method_clusters=983，error_clusters=276，bridge snapshot records=873，assets=1253，source summaries=770，compiled=751。
- quality_note: 个人错因和个人 method_gap 不能从题图/解析图反推；因此保留“暂无明确个人错因”和 `method_gap.enabled: false`，这是预期边界，不是质量缺口。
- rollback_action: not_run。

## 2026-07-02｜正负面积选区间最小闭环 GS-185
- scope: [GS-185](http://127.0.0.1:8765/open/GS-185)。
- evidence: 题图与解析图已存在；题目为 1000题A组8.6，给出分段函数 \(f(x)=x\ln x\ (x>0)\)、\(f(x)=x^2+x\ (x\le0)\)，在四个候选区间比较 \(\int_a^b f(x)\,dx\) 最小；解析确认答案为 A，即 \((a,b)=(-1,1)\)。
- card_updated: `GS-185` 从“积分型问题/待补充/OCR不清楚”占位卡补为“正负面积选区间最小”正式卡；写入 \(x^2+x<0\) 于 \((-1,0)\)，\(x\ln x<0\) 于 \((0,1)\)，\(x\ln x>0\) 于 \((1,+\infty)\)。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-064_正负面积选积分区间.md`，沉淀第一动作：候选区间比较定积分最大/最小时，先找零点和正负区间，再用带符号面积比较。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_update: `VIS-GS-185` 已复核题图/解析图，题图保持可见、解析图保持折叠；视觉详情页补入正负区间和带符号面积比较入口。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增 `MATHWIKI-GS-METHOD-064` 来源映射和“正负面积选积分区间训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced；缺少用户当时作答过程，因此 `method_gap` 保持 disabled，`mastery_history` 保留待评分。
- validation: `intake_closeout.py --id GS-185 --source '1000题A组8.6' --knowledge 定积分 --knowledge 定积分性质 --knowledge 一元函数积分学的计算 --knowledge 平面图形面积 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；结果为 cards=770，strong=1920，medium=726，weak_audit=469，knowledge_clusters=352，method_clusters=987，error_clusters=276，bridge snapshot records=873，assets=1253，source summaries=770，compiled=751。
- quality_note: 个人错因和个人 method_gap 不能从题图/解析图反推；因此保留“暂无明确个人错因”和 `method_gap.enabled: false`，这是预期边界，不是质量缺口。
- rollback_action: not_run。

## 2026-07-02｜隐函数法线斜率闭环 GS-128
- scope: [GS-128](http://127.0.0.1:8765/open/GS-128)。
- evidence: 题图与解析图已存在；题目为 2023 年真题第 14 题，曲线 \(3x^3=y^5+2y^3\) 在 \(x=1\) 对应点处求法线斜率。解析确认先定点 \((1,1)\)，再隐函数求导得切线斜率 \(\frac{9}{11}\)，法线斜率为 \(-\frac{11}{9}\)。
- card_updated: `GS-128` 从“题干为图片/OCR 待核对/待补充”薄卡补全为“隐函数法线斜率”正式卡；写入定点、隐函数求导、切线斜率和法线斜率负倒数入口链。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-065_隐函数定点法线斜率.md`，沉淀第一动作：隐式曲线在指定 \(x\) 处求法线斜率，先代点求对应坐标，再求切线斜率，最后取负倒数。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_update: `VIS-GS-128` 已复核题图/解析图，题图保持可见、解析图保持折叠；视觉详情页补入定点、隐函数求导和法线斜率负倒数推导。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增 `MATHWIKI-GS-METHOD-065` 来源映射和“隐函数定点法线斜率训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced；缺少用户当时作答过程，因此 `method_gap` 保持 disabled，`mastery_history` 保留待评分。
- validation: `intake_closeout.py --id GS-128 --source '2023年真题第14题' --knowledge 一元函数微分学应用 --knowledge 隐函数求导 --knowledge 切线方程 --knowledge 法线方程 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；结果为 cards=770，strong=1921，medium=727，weak_audit=469，knowledge_clusters=352，method_clusters=989，error_clusters=276，bridge snapshot records=873，assets=1253，source summaries=770，compiled=751。
- quality_note: 个人错因和个人 method_gap 不能从题图/解析图反推；因此保留“暂无明确个人错因”和 `method_gap.enabled: false`，这是预期边界，不是质量缺口。
- rollback_action: not_run。

## 2026-07-02｜二阶接触曲率充分必要判断闭环 GS-149
- scope: [GS-149](http://127.0.0.1:8765/open/GS-149)。
- evidence: 题图与解析图已存在；题目为 2019 年数二第 6 题，条件为 \(\lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^2}=0\)，问它是否为两曲线在 \(x=a\) 对应点处相切及曲率相等的条件；解析确认答案为 A，充分不必要。
- card_updated: `GS-149` 从“题干为图片/OCR 待核对/待补充”薄卡补全为“二阶接触与曲率相等充分必要判断”正式卡；写入 \(F=f-g\)、二阶 Taylor、充分性验证和必要性漏洞。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-066_二阶接触曲率充分必要判断.md`，沉淀第一动作：充分必要条件先拆两向，二阶小量条件用 Taylor，反向检查曲率公式的绝对值。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_update: `VIS-GS-149` 已复核题图/解析图，题图保持可见、解析图保持折叠；视觉详情页补入二阶 Taylor、曲率公式和反向漏洞。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增 `MATHWIKI-GS-METHOD-066` 来源映射和“二阶接触曲率充分必要判断训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced；缺少用户当时作答过程，因此 `method_gap` 保持 disabled，`mastery_history` 保留待评分。
- validation: `intake_closeout.py --id GS-149 --source '2019年数2（6）' --knowledge 一元函数微分学应用 --knowledge 高阶导数 --knowledge 曲率 --knowledge 泰勒公式 --knowledge 充分必要条件判断 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；结果为 cards=770，strong=1923，medium=729，weak_audit=469，knowledge_clusters=352，method_clusters=992，error_clusters=276，bridge snapshot records=873，assets=1253，source summaries=770，compiled=751。
- quality_note: 个人错因和个人 method_gap 不能从题图/解析图反推；因此保留“暂无明确个人错因”和 `method_gap.enabled: false`，这是预期边界，不是质量缺口。
- rollback_action: not_run。

## 2026-07-02｜分段函数求导与不可导点极值闭环 GS-137
- scope: [GS-137](http://127.0.0.1:8765/open/GS-137)。
- evidence: 题图与解析图已存在；题目为 2019 年第 15 题，分段函数 \(f(x)=x^{2x}\ (x>0)\)、\(f(x)=xe^x+1\ (x\le0)\)，要求求 \(f'(x)\) 和极值；解析确认 \(x=0\) 不可导但为极大值点。
- card_updated: `GS-137` 从“题干为图片/OCR 待核对/待补充”薄卡补全为“分段函数求导与不可导点极值”正式卡；写入幂指函数取对数求导、分段点左右导数检查、导数判单调和极值候选点完整列举。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-069_分段函数极值候选点完整列举.md`，沉淀第一动作：分段函数求极值时，除驻点外必须单独检查分段点、端点和不可导点。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_update: `VIS-GS-137` 已复核题图/解析图，题图保持可见、解析图保持折叠；视觉详情页补入 \(x^{2x}=e^{2x\ln x}\)、\(f'_+(0)=-\infty\) 和极值判断。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增 `MATHWIKI-GS-METHOD-069` 来源映射和“分段函数极值候选点训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced；缺少用户当时作答过程，因此 `method_gap` 保持 disabled，`mastery_history` 保留待评分。
- validation: `intake_closeout.py --id GS-137 --source '2019年第15题' --knowledge 一元函数微分学应用 --knowledge 单调性与极值 --knowledge 分段函数连续可导 --knowledge 分段函数求导 --knowledge 幂指函数求导 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；结果为 cards=770，strong=1924，medium=728，weak_audit=469，knowledge_clusters=352，method_clusters=993，error_clusters=276，bridge snapshot records=873，assets=1253，source summaries=770，compiled=751。
- quality_note: 个人错因和个人 method_gap 不能从题图/解析图反推；因此保留“暂无明确个人错因”和 `method_gap.enabled: false`，这是预期边界，不是质量缺口。
- rollback_action: not_run。

## 2026-07-02｜曲率圆变量方向判别闭环 GS-147
- scope: [GS-147](http://127.0.0.1:8765/open/GS-147)。
- evidence: 题图与解析图已存在；题目为 1000题B组5.43，设圆与曲线 \(x=y^2\) 在 \((0,0)\) 处有公切线，且它们关于 \(y\) 的二阶导数值相同，求圆方程；解析确认答案为 \(\left(x-\frac12\right)^2+y^2=\frac14\)。
- card_updated: `GS-147` 保持“已掌握”状态，补入 \(x=x(y)\) 型曲率公式、曲率半径、法线方向定圆心和相关旧题 `GS-148/GS-529/GS-143`；历史首次个人错因未记录，保留为“暂无明确个人错因”。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-047_曲率题变量对象判别链.md`，加入竖直切线与 \(x=x(y)\) 曲率圆模板；同步清理 `MATHWIKI-GS-METHOD-066_二阶接触曲率充分必要判断.md` 中偏宽的曲率圆关联。
- visual_update: `VIS-GS-147` 已复核题图/解析图，题图保持可见、解析图保持折叠；视觉详情页补入曲率、曲率半径与圆心方向推导。
- tutor_safe_update: 数学 LLMWiki 安全输入包更新“曲率题变量对象判别链训练项”，加入 \(x=x(y)\) 与竖直切线场景；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced；该题已由用户在 2026-06-02 复做正确，故不改变 `status: 已掌握` 和 `review.next: 已掌握`。
- validation: `intake_closeout.py --id GS-147 --source '1000题B组5.43' --knowledge 一元函数微分学应用 --knowledge 切线方程 --knowledge 曲率 --knowledge 曲率圆 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；结果为 cards=770，strong=1924，medium=728，weak_audit=469，knowledge_clusters=352，method_clusters=993，error_clusters=276，bridge snapshot records=873，assets=1253，source summaries=770，compiled=751。
- quality_note: 该题个人首次错因未记录，不能从题图/解析图反推；本轮补强的是题型入口和变量对象判别。
- rollback_action: not_run。

## 2026-07-02｜一阶线性方程与法线截距最值闭环 GS-164
- scope: [GS-164](http://127.0.0.1:8765/open/GS-164)。
- evidence: 题图与解析图已存在；题目为 2021 年第 20 题，给出 \(xy'-6y=-6\)、\(y(\sqrt3)=10\)，要求先求 \(y(x)\)，再求法线在 \(y\) 轴截距最小时的点 \(P\)。解析确认 \(y(x)=\frac13x^6+1\)，最小点为 \(P(1,\frac43)\)。
- card_updated: `GS-164` 从“待补充”薄卡补强为“一阶线性方程与法线截距最值”正式卡；写入积分因子、法线斜率、截距函数 \(I_P(x)\) 和最值求导主线。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-056_微分方程入口判别链.md`、`MATHWIKI-GS-METHOD-065_隐函数定点法线斜率.md`、`MATHWIKI-GS-TOPIC-009_微分方程错题总线.md`、`MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md` 与 `wiki/index.md`。
- visual_update: `VIS-GS-164` 已复核题图/解析图，题图保持可见、解析图保持折叠；视觉详情页补入标准型、积分因子、法线方程、截距函数和最值判断。
- tutor_safe_update: 数学 LLMWiki 安全输入包更新“微分方程入口判别链训练项”，加入外接法线截距、弧长等几何量时先解出 \(y(x)\) 再函数化/积分化的训练入口。
- card_decision: already_in_wrongnet_enhanced；缺少用户当时作答过程，因此 `method_gap` 保持 disabled，`mastery_history` 保留待评分。
- validation: `intake_closeout.py --id GS-164 --source '2021年第20题' --knowledge 微分方程 --knowledge 一阶线性微分方程 --knowledge 法线方程 --knowledge 单调性与极值 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；结果为 cards=770，strong=1925，medium=727，weak_audit=469，knowledge_clusters=352，method_clusters=994，error_clusters=276，bridge snapshot records=873，assets=1253，source summaries=770，compiled=751。
- quality_note: 个人错因和个人 method_gap 不能从题图/解析图反推；因此保留“暂无明确个人错因”和 `method_gap.enabled: false`，这是预期边界，不是质量缺口。
- rollback_action: not_run。

## 2026-07-02｜幂指极限对数化闭环 GS-165
- scope: [GS-165](http://127.0.0.1:8765/open/GS-165)。
- evidence: 题图与解析图已存在；题目为 2019 年第 1 题，计算 \(\lim_{x\to0}(x+2^x)^{2/x}\)。解析确认入口为先取对数，计算 \(L=\lim\ln y\)，再指数还原，答案为 \(4e^2\)。
- card_updated: `GS-165` 从“待补充”薄卡补强为“幂指极限对数化”正式卡；写入 \(\ln y=\frac{2}{x}\ln(x+2^x)\)、洛必达计算 \(L=2(1+\ln2)\) 和指数还原 \(e^L=4e^2\)。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-073_幂指极限对数化闭环.md`，沉淀幂指极限先取对数、再普通极限、最后指数还原的入口链。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-004_极限与连续错题总线.md`、`MATHWIKI-GS-METHOD-006_先判型总流程.md`、`MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度.md`、`wiki/index.md`。
- visual_update: `VIS-GS-165` 已复核题图/解析图，题图保持可见、解析图保持折叠；视觉详情页补入取对数、洛必达和指数还原推导。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增“幂指极限对数化训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced；缺少用户当时作答过程，因此 `method_gap` 保持 disabled，`mastery_history` 保留待评分。
- validation: `intake_closeout.py --id GS-165 --source '2019年第1题' --knowledge 极限与连续 --knowledge 函数极限 --knowledge 幂指极限 --knowledge 洛必达法则 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；结果为 cards=770，strong=1925，medium=727，weak_audit=469，knowledge_clusters=352，method_clusters=995，error_clusters=276，bridge snapshot records=873，assets=1253，source summaries=770，compiled=751。
- quality_note: 质量门为 `quality_gate=ok`，无 ERROR；仅保留“个人错因占位、method_gap 未启用”的预期 WARN，原因是不能从题图/解析图反推用户本人第一错步。
- rollback_action: not_run。

## 2026-07-02｜参数曲线曲率变量对象与二阶导链式求导闭环 GS-169
- scope: [GS-169](http://127.0.0.1:8765/open/GS-169)。
- evidence: 题图与解析图已存在；题目为 2018 年第 12 题，参数曲线 \(x=\cos^3t,\ y=\sin^3t\)，求 \(t=\frac{\pi}{4}\) 对应点处的曲率；解析确认答案为 \(\frac23\)。
- card_updated: `GS-169` 从“待补充”薄卡补强为“参数曲线曲率”正式卡；写入普通曲率公式下 \(y'\)、\(y''\) 都必须是关于 \(x\) 的导数，以及 \(y''=\frac{\frac{d}{dt}(y')}{dx/dt}\) 的链式求导入口。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-055_参数方程二阶导链式求导.md`、`MATHWIKI-GS-METHOD-047_曲率题变量对象判别链.md`、`MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md` 与 `wiki/index.md`。
- visual_update: `VIS-GS-169` 已复核题图/解析图，题图保持可见、解析图保持折叠；视觉详情页补入参数求导、二阶导换元和曲率公式代入推导。
- tutor_safe_update: 数学 LLMWiki 安全输入包更新“参数方程曲率训练项”“曲率题变量对象判别链训练项”和“参数方程二阶导链式求导训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced；缺少用户当时作答过程，因此 `method_gap` 保持 disabled，`mastery_history` 保留待评分。
- quality_note: 个人错因和个人 method_gap 不能从题图/解析图反推；因此保留“暂无明确个人错因”和 `method_gap.enabled: false`，这是预期边界，不是质量缺口。
- rollback_action: not_run。

## 2026-07-02｜指数因子辅助函数判单调闭环 GS-213
- scope: [GS-213](http://127.0.0.1:8765/open/GS-213)。
- evidence: 题图与解析图已存在；题目为 2020 年第六题，条件 \(f'(x)>f(x)>0\)，要求判断函数值比值不等式；解析确认入口为构造 \(F(x)=f(x)e^{-x}\)，答案为 B。
- card_updated: `GS-213` 补入 `mistake_count`、`wrong_history`、`mastery_history` 和 `method_gap.enabled: false`；将旧占位错因改为“暂无明确个人错因”，并补强指数因子辅助函数入口。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-080_指数因子辅助函数判单调.md`，沉淀 \(f'-f\)、\(F'-F\)、\(f''-\lambda f'\) 的指数因子触发链。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_update: `VIS-GS-213` 已复核题图/解析图，题图保持可见、解析图改为折叠；视觉详情页补入指数因子辅助函数、单调性和比值换回推导。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增 `MATHWIKI-GS-METHOD-080` 来源映射，并扩展“指数因子辅助函数训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced；缺少用户当时作答过程，因此 `method_gap` 保持 disabled，`mastery_history` 保留待评分。
- rollback_action: not_run。

## 2026-07-03｜积分中值定理与多次中值定理闭环 GS-218
- scope: [GS-218](http://127.0.0.1:8765/open/GS-218)。
- evidence: 题图与解析图已存在；题目为 2019 年第 21 题，条件 \(f(0)=0\)、\(f(1)=1\)、\(\int_0^1f(x)\,dx=1\)，要求证明存在 \(f'(\xi)=0\) 与 \(f''(\eta)<-2\)。解析确认入口为先用积分中值定理找 \(f(\xi_0)=1=f(1)\)，再 Rolle；第二问构造 \(F=f+x^2\)，比较两段平均斜率后对 \(F'\) 再用中值定理。
- card_updated: `GS-218` 补入 `mistake_count`、`wrong_history`、`mastery_history` 和 `method_gap.enabled: false`；将旧占位错因改为“暂无明确个人错因”，并补强积分中值定理、Rolle、多次 Lagrange 与辅助函数构造入口。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-077_中值定理证明目标反推链.md`、`MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_update: `VIS-GS-218` 已复核题图/解析图，题图保持可见，解析图与关键推导改为折叠；视觉详情页补入积分中值定理、Rolle、辅助函数 \(F=f+x^2\) 和平均斜率比较。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增 `MATHWIKI-GS-METHOD-077` 来源映射，并扩展“积分中值与 Rolle 链条”“多次中值定理训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced；缺少用户当时作答过程，因此 `method_gap` 保持 disabled，`mastery_history` 保留待评分。
- rollback_action: not_run。

## 2026-07-03｜剩余高优先级视觉解析 11 题质量补强收口 GS-208/262/288/289/290/292/360/373/502/593/648
- scope: [GS-208](http://127.0.0.1:8765/open/GS-208)、[GS-262](http://127.0.0.1:8765/open/GS-262)、[GS-288](http://127.0.0.1:8765/open/GS-288)、[GS-289](http://127.0.0.1:8765/open/GS-289)、[GS-290](http://127.0.0.1:8765/open/GS-290)、[GS-292](http://127.0.0.1:8765/open/GS-292)、[GS-360](http://127.0.0.1:8765/open/GS-360)、[GS-373](http://127.0.0.1:8765/open/GS-373)、[GS-502](http://127.0.0.1:8765/open/GS-502)、[GS-593](http://127.0.0.1:8765/open/GS-593)、[GS-648](http://127.0.0.1:8765/open/GS-648)。
- card_updated: 补强 `GS-208`、`GS-288`、`GS-289`、`GS-290`、`GS-292`、`GS-502`、`GS-593`、`GS-648` 的 lecture_refs、方法入口和复做第一动作；重写薄弱正式卡 `GS-262`、`GS-360`、`GS-373`，保留“暂无明确个人错因”和 `待评分`，不从题图/解析图反推个人错步。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-077_中值定理证明目标反推链.md`、`MATHWIKI-GS-METHOD-078_相关变化率静态关系建模链.md`、`MATHWIKI-GS-METHOD-079_分段积分变量角色与拼接链.md`。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-014_面积区域与交点参数分离.md`、`MATHWIKI-GS-METHOD-034_二重积分区域化归与换序.md`、`MATHWIKI-GS-METHOD-050_二元函数性质定义判别链.md`、`MATHWIKI-GS-METHOD-063_交错纠缠级数拆项与条件收敛闭环.md`，并同步 `MATHWIKI-GS-TOPIC-005/006/010/011`、`wiki/index.md`、可视化详情索引、`obsidian_open_links.md`、`manifest.json`、`asset_to_obsidian.json`。
- visual_update: 11 个 `VIS-GS-*` 页面均补入方法页、第一动作复述、入口链接和 `already_in_wrongnet_enhanced` 判断；题图保持可见，解析继续折叠。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增 `METHOD-077/078/079` 来源映射，并新增“中值定理证明目标反推”“相关变化率静态关系”“分段积分变量角色”训练项；只写高层方法触发和来源 ID，不复制完整题干、完整解析或正式卡正文。
- validation: 已运行 `wrongnet.py rebuild`、`build_wrong_card_source_summaries.py`、`build_knowledge_cluster_pages.py`、`build_pattern_cluster_pages.py`、`refresh_obsidian_bridge_snapshot.py`、`json.tool manifest/asset_to_obsidian`，结果为 cards=770，strong=1930，medium=729，weak_audit=469，knowledge_clusters=352，method_clusters=1004，error_clusters=281，action_gap_clusters=8，bridge snapshot records=873，assets=1253，source summaries=770，compiled=751。
- quality_gate: 11 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`；`GS-262/360/373` 的 `method_gap not enabled` 为预期边界，原因是缺少用户本人做题过程证据。
- rollback_action: not_run。

## 2026-07-03｜中点 Taylor 积分化判断函数值符号闭环 GS-237
- scope: [GS-237](http://127.0.0.1:8765/open/GS-237)。
- evidence: 题图与解析图已存在；题目为 2018 年数二第 4 题，给出 \(f\) 在 \([0,1]\) 上二阶可导且 \(\int_0^1f(x)\,dx=0\)，要求判断哪种附加条件能推出 \(f(\frac12)<0\)。解析确认入口为在 \(x_0=\frac12\) 处作二阶 Taylor 展开，再对 \([0,1]\) 积分，结论选 D。
- card_updated: `GS-237` 补入 `mistake_count`、`wrong_history`、`mastery_history` 和 `method_gap.enabled: false`；将旧占位错因改为“暂无明确个人错因”，并补强中点 Taylor 积分化、二阶余项积分保号和 \(f'\) 定号不足以决定中点符号的陷阱。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-072_积分不等式证明入口链.md`、`MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_update: `VIS-GS-237` 已复核题图/解析图，题图保持可见，解析图与关键推导改为折叠；视觉详情页补入 \(\xi_x\) 随 \(x\) 变化、一次项积分为 0 和 \(f''\) 符号决定结论。
- tutor_safe_update: 数学 LLMWiki 安全输入包扩展“中点 Taylor 积分训练项”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- card_decision: already_in_wrongnet_enhanced；缺少用户当时作答过程，因此 `method_gap` 保持 disabled，`mastery_history` 保留待评分。
- validation: `intake_closeout.py --id GS-237 --source '2018年数2第4题' --knowledge 一元函数微分学应用 --knowledge 中值定理 --knowledge 泰勒公式 --knowledge 定积分 --knowledge 凹凸性与拐点 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；结果为 cards=770，strong=1932，medium=731，weak_audit=469，knowledge_clusters=352，method_clusters=1007，error_clusters=281，bridge snapshot records=873，assets=1253，source summaries=770，compiled=751。
- quality_note: 质量门为 `quality_gate=ok`，无 ERROR；仅保留“个人错因占位、method_gap 未启用”的预期 WARN，原因是不能从题图/解析图反推用户本人第一错步。
- progress_note: 当前核心队列从 217/244 更新为约 218/244，剩余约 26 题。
- rollback_action: not_run。

## 2026-07-03｜定积分应用视觉解析 11 题方法链补强 GS-294/295/297/298/299/300/301/302/303/304/305
- scope: [GS-294](http://127.0.0.1:8765/open/GS-294)、[GS-295](http://127.0.0.1:8765/open/GS-295)、[GS-297](http://127.0.0.1:8765/open/GS-297)、[GS-298](http://127.0.0.1:8765/open/GS-298)、[GS-299](http://127.0.0.1:8765/open/GS-299)、[GS-300](http://127.0.0.1:8765/open/GS-300)、[GS-301](http://127.0.0.1:8765/open/GS-301)、[GS-302](http://127.0.0.1:8765/open/GS-302)、[GS-303](http://127.0.0.1:8765/open/GS-303)、[GS-304](http://127.0.0.1:8765/open/GS-304)、[GS-305](http://127.0.0.1:8765/open/GS-305)。
- card_updated: 11 张正式卡补入可解析 YAML 列表格式、方法页引用、视觉来源和 `## 复做提醒`；保留旧卡“用户个人错因待补充”的边界，不从题图/解析图反推个人第一错步。
- wiki_created: 新建并接入 `MATHWIKI-GS-METHOD-081_面积绝对值分段与变化率建模链.md`、`MATHWIKI-GS-METHOD-082_曲线弧长定义域与根式化简链.md`、`MATHWIKI-GS-METHOD-083_旋转体曲面变量选择与生成量链.md`。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-006_定积分错题总线.md`、`wiki/index.md`、可视化详情索引、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_update: 11 个 `VIS-GS-*` 页面均从旧版 `## 题图 / ## 解析图` 收口为 `## 题目` + 折叠解析 callout；补入方法页链接和 `already_in_wrongnet_enhanced` 判断。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增面积绝对值分段、曲线弧长定义域与根式化简、旋转体/旋转曲面生成量三类训练项；只写高层方法触发和来源 ID，不复制完整题干、完整解析或正式卡正文。
- validation: 已运行 `wrongnet.py rebuild`、`build_wrong_card_source_summaries.py`、`build_knowledge_cluster_pages.py`、`build_pattern_cluster_pages.py`、`refresh_obsidian_bridge_snapshot.py`、`json.tool manifest/asset_to_obsidian`，结果为 cards=770，strong=1938，medium=760，weak_audit=468，knowledge_clusters=352，method_clusters=1007，error_clusters=281，action_gap_clusters=8，bridge snapshot records=873，assets=1253，source summaries=770，compiled=751。
- quality_gate: 11 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`；WARN 仅为“error_causes 占位、method_gap 未启用”，原因是缺少用户本人做题过程证据。
- progress_note: 严格按 manifest 去重统计，有解析图的正式题为 245 题；本批完成后 `already_in_wrongnet_enhanced` 从 75 题更新到 86 题，严格未完成从 170 题降到 159 题。
- rollback_action: not_run。

## 2026-07-03｜定积分物理应用微元法 7 题视觉增强闭环 GS-415/418/419/420/421/422/423
- scope: [GS-415](http://127.0.0.1:8765/open/GS-415)、[GS-418](http://127.0.0.1:8765/open/GS-418)、[GS-419](http://127.0.0.1:8765/open/GS-419)、[GS-420](http://127.0.0.1:8765/open/GS-420)、[GS-421](http://127.0.0.1:8765/open/GS-421)、[GS-422](http://127.0.0.1:8765/open/GS-422)、[GS-423](http://127.0.0.1:8765/open/GS-423)。
- card_updated: 正式错题卡未改写；本批原卡已有知识点、方法、复做提醒和可视化引用，质量门已能通过。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-038_定积分物理应用微元法.md`，补入物理微元七题组闭环；同步 `wiki/index.md` 中 7 条 `VIS-GS-*` 主索引行，并补 Tutor 安全输入包的 `METHOD-038` 来源映射。
- visual_update: 7 个视觉详情页均标记为 `already_in_wrongnet_enhanced`；题图保持可见，解析保持折叠，方法页 `MATHWIKI-GS-METHOD-038` 已链接。
- manifest_update: `manifest.json`、`asset_to_obsidian.json`、`可视化错题详情/index.md` 均更新到 2026-07-03；Obsidian bridge snapshot 已刷新。
- validation: 已运行 `json.tool manifest/asset_to_obsidian`、`refresh_obsidian_bridge_snapshot.py`，结果为 records=873、assets=1253；7 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- quality_note: 仅保留“error_causes 占位、method_gap 未启用”的预期 WARN，原因是缺少用户本人做题过程证据，不能从题图/解析图反推个人错因。
- progress_note: 严格按 manifest 去重统计，本批完成后 `already_in_wrongnet_enhanced` 从 86 题更新到 93 题，严格未完成从 159 题降到 152 题。
- rollback_action: not_run。

## 2026-07-03｜二重积分区域、对称性与极坐标 10 题视觉增强闭环 GS-398/399/401/402/403/406/409/410/411/412
- scope: [GS-398](http://127.0.0.1:8765/open/GS-398)、[GS-399](http://127.0.0.1:8765/open/GS-399)、[GS-401](http://127.0.0.1:8765/open/GS-401)、[GS-402](http://127.0.0.1:8765/open/GS-402)、[GS-403](http://127.0.0.1:8765/open/GS-403)、[GS-406](http://127.0.0.1:8765/open/GS-406)、[GS-409](http://127.0.0.1:8765/open/GS-409)、[GS-410](http://127.0.0.1:8765/open/GS-410)、[GS-411](http://127.0.0.1:8765/open/GS-411)、[GS-412](http://127.0.0.1:8765/open/GS-412)。
- card_updated: 正式错题卡未改写；本批原卡已有知识点、方法、复做提醒和可视化引用，质量门已能通过。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-034_二重积分区域化归与换序.md`、`MATHWIKI-GS-METHOD-035_二重积分对称性保号与轮换.md`、`MATHWIKI-GS-METHOD-037_二重积分极坐标区域分块与对称化.md`、`MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md` 与数学 LLMWiki 安全输入包。
- visual_update: 10 个正式 `VIS-GS-*` 页面均标记为 `already_in_wrongnet_enhanced`；题图保持可见，解析保持折叠，方法页链接已确认。`GS-403` 的 `MN4-*` 来源保留页继续作为来源证据，不改成正式视觉详情页。
- manifest_update: `manifest.json`、`asset_to_obsidian.json`、`可视化错题详情/index.md` 均更新到 2026-07-03；Obsidian bridge snapshot 已刷新。
- validation: 已运行 `json.tool manifest/asset_to_obsidian`、`refresh_obsidian_bridge_snapshot.py`，结果为 records=873、assets=1253；10 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- quality_note: 仅保留“error_causes 占位、method_gap 未启用”的预期 WARN，原因是缺少用户本人做题过程证据，不能从题图/解析图反推个人错因。
- progress_note: 严格按 manifest 去重统计，本批完成后 `already_in_wrongnet_enhanced` 从 93 题更新到 103 题，严格未完成从 152 题降到 142 题。
- rollback_action: not_run。

## 2026-07-03｜双端点 Taylor 余项估值闭环 GS-253
- scope: [GS-253](http://127.0.0.1:8765/open/GS-253)。
- evidence: 题图与解析图已存在；题目为 2023 年真题第 21 题，条件 \(f\) 在 \([-a,a]\) 上二阶连续可导，第一问由 \(f(0)=0\) 证明存在 \(f''(\xi)=\frac{f(a)+f(-a)}{a^2}\)，第二问由内部极值证明存在 \(|f''(\eta)|\ge\frac{|f(a)-f(-a)|}{2a^2}\)。
- card_updated: `GS-253` 从浅层补强卡升级为“二阶 Taylor 余项证明二阶导存在性与估值”正式卡；补入 `mistake_count`、`wrong_history`、`mastery_history`、`method_gap.enabled: false`、方法页引用和复做提醒；保留“暂无明确个人错因”，不从解析图反推用户本人第一错步。
- wiki_created: 新建 `MATHWIKI-GS-METHOD-084_双端点Taylor余项估值链.md`，沉淀第一动作：先选能消去一次项的 Taylor 展开点；第一问在 0 对 \(a,-a\) 展开，第二问在内部极值点展开。
- wiki_updated: 更新 `MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线.md`、`wiki/index.md`、可视化详情页、`可视化错题详情/index.md`、`manifest.json`、`asset_to_obsidian.json` 与数学 LLMWiki 安全输入包。
- visual_update: `VIS-GS-253` 已复核题图/解析图，题图保持可见，解析图与关键推导改为折叠；视觉详情页补入方法页、强关联旧题和 `already_in_wrongnet_enhanced` 判断。
- tutor_safe_update: 数学 LLMWiki 安全输入包新增 `MATHWIKI-GS-METHOD-084` 来源映射，并扩展“双端点 Taylor 估值训练”；只写高层第一动作和来源 ID，不复制完整题干、完整解析或正式卡正文。
- validation: `intake_closeout.py --id GS-253 --source '2023年真题第21题' --knowledge 一元函数微分学应用 --knowledge 中值定理 --knowledge 泰勒公式 --knowledge 单调性与极值 --knowledge 凹凸性与拐点 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；结果为 cards=770，strong=1938，medium=763，weak_audit=468，knowledge_clusters=352，method_clusters=1009，error_clusters=281，bridge snapshot records=873，assets=1253，source summaries=770，compiled=751。
- quality_note: 质量门为 `quality_gate=ok`，无 ERROR；仅保留“个人错因占位、method_gap 未启用”的预期 WARN，原因是不能从题图/解析图反推用户本人第一错步。
- progress_note: 当前按唯一 GS 题号且有解析图的严格队列统计，`already_in_wrongnet_enhanced` 为 100/175，剩余 75 题；全部可视化 GS 记录不限定解析图时为 101/637 已增强，剩余 536 题。
- rollback_action: not_run。

## 2026-07-03｜方向导数、梯度与二元泰勒 6 题视觉增强闭环 GS-652/653/654/656/657/658
- scope: [GS-652](http://127.0.0.1:8765/open/GS-652)、[GS-653](http://127.0.0.1:8765/open/GS-653)、[GS-654](http://127.0.0.1:8765/open/GS-654)、[GS-656](http://127.0.0.1:8765/open/GS-656)、[GS-657](http://127.0.0.1:8765/open/GS-657)、[GS-658](http://127.0.0.1:8765/open/GS-658)。
- card_updated: 正式错题卡未改写；6 张卡已有用户本人错因、掌握度与 method_gap，本次不从解析图额外推断新错因。
- wiki_updated: 更新 `MATHWIKI-GS-METHOD-044_方向导数与梯度入口判别链.md`、`MATHWIKI-GS-METHOD-046_多元公式模板入口链.md`、`MATHWIKI-GS-METHOD-030_二元二阶泰勒展开格式.md`、`MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`、`wiki/index.md`。
- visual_update: 6 个视觉详情页均标记为 `already_in_wrongnet_enhanced`；题图保持可见，解析保持折叠，入口链接指向方向导数/梯度链与二元泰勒模板链。
- manifest_update: `manifest.json`、`asset_to_obsidian.json`、`可视化错题详情/index.md` 均更新到 2026-07-03；正式卡未变，因此不运行 wrongnet rebuild。
- tutor_safe_update: 数学 LLMWiki 安全输入包已覆盖 `METHOD-044` 与 `METHOD-046` 的高层训练项，本次验证已覆盖，无需复制题干或长解析。
- validation: 6 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`，无 WARN/ERROR；后续刷新 Obsidian bridge snapshot 并复核 JSON。
- progress_note: 本批将严格解析图队列中的 6 道从未增强收口为已增强；最新剩余数以后续统计脚本为准。
- rollback_action: not_run。

## 2026-07-03｜第17讲空间解析几何与多元公式 9 题状态收口 GS-626/627/628/629/645/646/647/651/655
- scope: [GS-626](http://127.0.0.1:8765/open/GS-626)、[GS-627](http://127.0.0.1:8765/open/GS-627)、[GS-628](http://127.0.0.1:8765/open/GS-628)、[GS-629](http://127.0.0.1:8765/open/GS-629)、[GS-645](http://127.0.0.1:8765/open/GS-645)、[GS-646](http://127.0.0.1:8765/open/GS-646)、[GS-647](http://127.0.0.1:8765/open/GS-647)、[GS-651](http://127.0.0.1:8765/open/GS-651)、[GS-655](http://127.0.0.1:8765/open/GS-655)。
- card_updated: 正式错题卡未改写；9 张卡已有方法入口、可视化引用和质量门所需字段，本次只做状态收口。
- visual_update: 9 个视觉详情页已确认 `## 题目` 可见、解析使用 `> [!answer]- 解析（做完后展开）` 折叠，且不存在旧版 `## 解析图` 外泄结构。
- manifest_update: `manifest.json`、`asset_to_obsidian.json`、`可视化错题详情/index.md` 已更新到 `already_in_wrongnet_enhanced` 与 `2026-07-03`；Obsidian bridge snapshot 已刷新。
- validation: 9 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`，无 WARN/ERROR；`manifest.json` 与 `asset_to_obsidian.json` 均已通过 JSON 解析；9 行可视化索引均保持 13 列。
- progress_note: 本批将严格解析图队列中的 9 道从未增强收口为已增强；最新剩余数以后续统计脚本为准。
- rollback_action: not_run。

## 2026-07-03｜Taylor 积分化与三角有理式 8 题状态收口 GS-237/621/622/623/624/625/631/632
- scope: [GS-237](http://127.0.0.1:8765/open/GS-237)、[GS-621](http://127.0.0.1:8765/open/GS-621)、[GS-622](http://127.0.0.1:8765/open/GS-622)、[GS-623](http://127.0.0.1:8765/open/GS-623)、[GS-624](http://127.0.0.1:8765/open/GS-624)、[GS-625](http://127.0.0.1:8765/open/GS-625)、[GS-631](http://127.0.0.1:8765/open/GS-631)、[GS-632](http://127.0.0.1:8765/open/GS-632)。
- card_updated: 正式错题卡未改写；本批原卡已有方法入口、视觉引用和质量门所需字段，本次只同步可视化状态。
- visual_update: 8 个视觉详情页已确认 `## 题目` 可见、解析折叠，且不存在旧版 `## 解析图` 外泄结构。
- manifest_update: `manifest.json`、`asset_to_obsidian.json`、`可视化错题详情/index.md` 已更新到 `already_in_wrongnet_enhanced` 与 `2026-07-03`；Obsidian bridge snapshot 已刷新。
- validation: 8 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`；`GS-237` 保留个人错因/method_gap 预期 WARN，`GS-625` 保留 first-action 句式 WARN，均非 ERROR；JSON 解析、索引 13 列和页面折叠结构均已通过。
- progress_note: 本批将严格解析图队列中的 8 道从未增强收口为已增强；最新剩余数以后续统计脚本为准。
- rollback_action: not_run。

## 2026-07-03｜高数解析资产严格队列剩余 52 题状态总收口
- scope: [GS-005](http://127.0.0.1:8765/open/GS-005)、[GS-014](http://127.0.0.1:8765/open/GS-014)、[GS-027](http://127.0.0.1:8765/open/GS-027)、[GS-032](http://127.0.0.1:8765/open/GS-032)、[GS-043](http://127.0.0.1:8765/open/GS-043)、[GS-072](http://127.0.0.1:8765/open/GS-072)、[GS-087](http://127.0.0.1:8765/open/GS-087)、[GS-095](http://127.0.0.1:8765/open/GS-095)、[GS-099](http://127.0.0.1:8765/open/GS-099)、[GS-123](http://127.0.0.1:8765/open/GS-123)、[GS-139](http://127.0.0.1:8765/open/GS-139)、[GS-142](http://127.0.0.1:8765/open/GS-142)、[GS-186](http://127.0.0.1:8765/open/GS-186)、[GS-187](http://127.0.0.1:8765/open/GS-187)、[GS-188](http://127.0.0.1:8765/open/GS-188)、[GS-189](http://127.0.0.1:8765/open/GS-189)、[GS-190](http://127.0.0.1:8765/open/GS-190)、[GS-196](http://127.0.0.1:8765/open/GS-196)、[GS-201](http://127.0.0.1:8765/open/GS-201)、[GS-247](http://127.0.0.1:8765/open/GS-247)、[GS-256](http://127.0.0.1:8765/open/GS-256)、[GS-273](http://127.0.0.1:8765/open/GS-273)、[GS-279](http://127.0.0.1:8765/open/GS-279)、[GS-280](http://127.0.0.1:8765/open/GS-280)、[GS-281](http://127.0.0.1:8765/open/GS-281)、[GS-310](http://127.0.0.1:8765/open/GS-310)、[GS-311](http://127.0.0.1:8765/open/GS-311)、[GS-338](http://127.0.0.1:8765/open/GS-338)、[GS-354](http://127.0.0.1:8765/open/GS-354)、[GS-356](http://127.0.0.1:8765/open/GS-356)、[GS-363](http://127.0.0.1:8765/open/GS-363)、[GS-367](http://127.0.0.1:8765/open/GS-367)、[GS-380](http://127.0.0.1:8765/open/GS-380)、[GS-381](http://127.0.0.1:8765/open/GS-381)、[GS-382](http://127.0.0.1:8765/open/GS-382)、[GS-383](http://127.0.0.1:8765/open/GS-383)、[GS-384](http://127.0.0.1:8765/open/GS-384)、[GS-386](http://127.0.0.1:8765/open/GS-386)、[GS-387](http://127.0.0.1:8765/open/GS-387)、[GS-388](http://127.0.0.1:8765/open/GS-388)、[GS-389](http://127.0.0.1:8765/open/GS-389)、[GS-391](http://127.0.0.1:8765/open/GS-391)、[GS-392](http://127.0.0.1:8765/open/GS-392)、[GS-394](http://127.0.0.1:8765/open/GS-394)、[GS-395](http://127.0.0.1:8765/open/GS-395)、[GS-425](http://127.0.0.1:8765/open/GS-425)、[GS-605](http://127.0.0.1:8765/open/GS-605)、[GS-609](http://127.0.0.1:8765/open/GS-609)、[GS-610](http://127.0.0.1:8765/open/GS-610)、[GS-618](http://127.0.0.1:8765/open/GS-618)、[GS-619](http://127.0.0.1:8765/open/GS-619)、[GS-620](http://127.0.0.1:8765/open/GS-620)。
- card_updated: 正式错题卡未改写；52 题逐题质量门已通过，本次只把可视化 manifest/index 状态与质量门结论同步，保留原 note 中已有的方法页和修复说明。
- visual_update: 52 个视觉详情页均已按 manifest 路径复核，题图可见、解析折叠，无旧版 `## 解析图` 外泄结构；其中 `GS-425` 保留在线性代数详情页。
- manifest_update: `manifest.json` 更新 54 条记录，`asset_to_obsidian.json` 更新 108 条资产映射，`可视化错题详情/index.md` 更新 52 行，均统一到 `already_in_wrongnet_enhanced` 与 `2026-07-03`；Obsidian bridge snapshot 已刷新。
- validation: 52 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`，无 ERROR；预期 WARN 仅来自缺少用户个人作答过程、少量 `method_gap` 未启用或 first-action 句式提醒。JSON 解析、索引 13 列、manifest 路径结构、HTTP bridge 跳转和 `git diff --check` 均通过。
- progress_note: 严格按唯一 GS 题号且有解析资产统计，`already_in_wrongnet_enhanced` 已达到 175/175，剩余 0。
- rollback_action: not_run。
## 2026-07-03｜线代行列式结构化计算 4 题视觉增强闭环 LA-009/010/012/020
- scope: [LA-009](http://127.0.0.1:8765/open/LA-009)、[LA-010](http://127.0.0.1:8765/open/LA-010)、[LA-012](http://127.0.0.1:8765/open/LA-012)、[LA-020](http://127.0.0.1:8765/open/LA-020)。
- card_updated: 仅补强 `LA-012` 正式卡，写入视觉详情引用、旧错题复发记录占位、`mastery_history: 待评分`、`method_gap.enabled: false` 和秩一扰动行列式复做入口；不从解析图反推个人错因。
- wiki_updated: 更新 `MATHWIKI-LA-METHOD-018_行列式结构化计算与指定项系数.md` 和 `MATHWIKI-LA-TOPIC-005_行列式错题总线.md`，把指定项系数、分块上三角、秩一扰动行列式、代数余子式和四类入口收成同一组方法链。
- visual_update: 4 个 `VIS-LA-*` 页面均标记为 `already_in_wrongnet_enhanced`；题图保持可见，解析保持折叠，方法页链接已确认。
- manifest_update: `manifest.json`、`asset_to_obsidian.json`、`可视化错题详情/index.md` 与 `wiki/index.md` 均更新到 2026-07-03。
- validation: `intake_closeout.py --id LA-012 --source 强化例题1.2-2 --knowledge 行列式 --knowledge 矩阵运算 --knowledge 特征值与特征向量 --visual expected` 已通过，完成 wrongnet rebuild、LLM Wiki 覆盖刷新、source summaries、Obsidian bridge snapshot 刷新、相似题/知识点/Obsidian 搜索校验与质量门检查；4 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- quality_note: 个人错因和个人 method_gap 不能从题图/解析图反推；`LA-009/010/012/020` 的占位 WARN 属于预期边界。
- rollback_action: not_run。

## 2026-07-03｜线代解析资产正式视觉页 66 题状态收口
- scope: [LA-009](http://127.0.0.1:8765/open/LA-009)、[LA-010](http://127.0.0.1:8765/open/LA-010)、[LA-012](http://127.0.0.1:8765/open/LA-012)、[LA-020](http://127.0.0.1:8765/open/LA-020)、[LA-030](http://127.0.0.1:8765/open/LA-030)、[LA-031](http://127.0.0.1:8765/open/LA-031)、[LA-033](http://127.0.0.1:8765/open/LA-033)、[LA-034](http://127.0.0.1:8765/open/LA-034)、[LA-035](http://127.0.0.1:8765/open/LA-035)、[LA-037](http://127.0.0.1:8765/open/LA-037)、[LA-038](http://127.0.0.1:8765/open/LA-038)、[LA-039](http://127.0.0.1:8765/open/LA-039)、[LA-040](http://127.0.0.1:8765/open/LA-040)、[LA-041](http://127.0.0.1:8765/open/LA-041)、[LA-042](http://127.0.0.1:8765/open/LA-042)、[LA-043](http://127.0.0.1:8765/open/LA-043)、[LA-044](http://127.0.0.1:8765/open/LA-044)、[LA-045](http://127.0.0.1:8765/open/LA-045)、[LA-046](http://127.0.0.1:8765/open/LA-046)、[LA-048](http://127.0.0.1:8765/open/LA-048)、[LA-049](http://127.0.0.1:8765/open/LA-049)、[LA-050](http://127.0.0.1:8765/open/LA-050)、[LA-052](http://127.0.0.1:8765/open/LA-052)、[LA-053](http://127.0.0.1:8765/open/LA-053)、[LA-054](http://127.0.0.1:8765/open/LA-054)、[LA-055](http://127.0.0.1:8765/open/LA-055)、[LA-056](http://127.0.0.1:8765/open/LA-056)、[LA-057](http://127.0.0.1:8765/open/LA-057)、[LA-058](http://127.0.0.1:8765/open/LA-058)、[LA-059](http://127.0.0.1:8765/open/LA-059)、[LA-060](http://127.0.0.1:8765/open/LA-060)、[LA-062](http://127.0.0.1:8765/open/LA-062)、[LA-063](http://127.0.0.1:8765/open/LA-063)、[LA-064](http://127.0.0.1:8765/open/LA-064)、[LA-067](http://127.0.0.1:8765/open/LA-067)、[LA-068](http://127.0.0.1:8765/open/LA-068)、[LA-069](http://127.0.0.1:8765/open/LA-069)、[LA-070](http://127.0.0.1:8765/open/LA-070)、[LA-071](http://127.0.0.1:8765/open/LA-071)、[LA-072](http://127.0.0.1:8765/open/LA-072)、[LA-073](http://127.0.0.1:8765/open/LA-073)、[LA-074](http://127.0.0.1:8765/open/LA-074)、[LA-075](http://127.0.0.1:8765/open/LA-075)、[LA-078](http://127.0.0.1:8765/open/LA-078)、[LA-079](http://127.0.0.1:8765/open/LA-079)、[LA-081](http://127.0.0.1:8765/open/LA-081)、[LA-082](http://127.0.0.1:8765/open/LA-082)、[LA-087](http://127.0.0.1:8765/open/LA-087)、[LA-088](http://127.0.0.1:8765/open/LA-088)、[LA-089](http://127.0.0.1:8765/open/LA-089)、[LA-090](http://127.0.0.1:8765/open/LA-090)、[LA-091](http://127.0.0.1:8765/open/LA-091)、[LA-092](http://127.0.0.1:8765/open/LA-092)、[LA-093](http://127.0.0.1:8765/open/LA-093)、[LA-094](http://127.0.0.1:8765/open/LA-094)、[LA-097](http://127.0.0.1:8765/open/LA-097)、[LA-099](http://127.0.0.1:8765/open/LA-099)、[LA-100](http://127.0.0.1:8765/open/LA-100)、[LA-103](http://127.0.0.1:8765/open/LA-103)、[LA-104](http://127.0.0.1:8765/open/LA-104)、[LA-105](http://127.0.0.1:8765/open/LA-105)、[LA-109](http://127.0.0.1:8765/open/LA-109)、[LA-110](http://127.0.0.1:8765/open/LA-110)、[LA-111](http://127.0.0.1:8765/open/LA-111)、[LA-116](http://127.0.0.1:8765/open/LA-116)、[LA-117](http://127.0.0.1:8765/open/LA-117)。
- card_updated: 正式错题卡未改写；66 题逐题质量门已通过，本次只同步正式视觉页的 manifest/index 状态。
- visual_update: 66 个 `VIS-LA-*` 正式视觉详情页均已按 manifest 路径复核，题图可见、解析折叠，无旧版 `## 解析图` 外泄结构。
- source_retention: 72 条 `MN4-GS-CH01-*` 合并来源记录保留为 `merged_into_wrongnet` 来源证据，`card_decision` 统一为 `already_in_wrongnet_source_retained`，不混入正式视觉页统计。
- manifest_update: `manifest.json` 中 66 条 `linked_wrongnet` 正式记录收口为 `already_in_wrongnet_enhanced`，`asset_to_obsidian.json` 更新相关资产日期，`可视化错题详情/index.md` 66 行正式索引更新到 `2026-07-03`；Obsidian bridge snapshot 已刷新。
- validation: 66 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`，无 ERROR；WARN 均为缺少用户个人作答过程导致的个人错因/method_gap 边界。JSON 解析、正式索引 13 列、manifest 路径结构、HTTP bridge 跳转均通过。
- rollback_action: not_run。
## 2026-07-03｜线代相似理论 4 题视觉状态补同步 LA-112/114/115/119
- scope: [LA-112](http://127.0.0.1:8765/open/LA-112)、[LA-114](http://127.0.0.1:8765/open/LA-114)、[LA-115](http://127.0.0.1:8765/open/LA-115)、[LA-119](http://127.0.0.1:8765/open/LA-119)。
- card_updated: 正式错题卡未改写。
- visual_update: 4 个视觉详情页由 `already_in_wrongnet` 同步为 `already_in_wrongnet_enhanced`；题图保持可见，解析保持折叠。
- manifest_update: `manifest.json`、`asset_to_obsidian.json`、`可视化错题详情/index.md` 与 `wiki/index.md` 日期同步到 2026-07-03。
- wrongnet_rebuild: not_run（本次未修改正式错题卡）。
- rollback_action: not_run。
## 2026-07-03｜正式解析图视觉状态全队列统一收口
- scope: 244 个有解析图且对应正式 wrongnet 卡的视觉详情页。
- visual_update: 统一 `## 入库判断` 为 `already_in_wrongnet_enhanced`，补齐 `quality_gate: ok` 和视觉层 `wrongnet_rebuild` 边界说明；本轮实际更新页面 238 个。
- manifest_update: `manifest.json`、`asset_to_obsidian.json`、`可视化错题详情/index.md` 与 `wiki/index.md` 同步到 2026-07-03。
- card_updated: none。
- wrongnet_rebuild: not_run（本轮只统一视觉层状态；正式卡变更已在先前 closeout 中处理）。
- rollback_action: not_run。

## 2026-07-03｜无单独解析图但质量门通过的正式视觉页 164 题状态收口
- scope: [GS-012](http://127.0.0.1:8765/open/GS-012)、[GS-015](http://127.0.0.1:8765/open/GS-015)、[GS-016](http://127.0.0.1:8765/open/GS-016)、[GS-017](http://127.0.0.1:8765/open/GS-017)、[GS-020](http://127.0.0.1:8765/open/GS-020)、[GS-022](http://127.0.0.1:8765/open/GS-022)、[GS-024](http://127.0.0.1:8765/open/GS-024)、[GS-025](http://127.0.0.1:8765/open/GS-025)、[GS-030](http://127.0.0.1:8765/open/GS-030)、[GS-031](http://127.0.0.1:8765/open/GS-031)、[GS-033](http://127.0.0.1:8765/open/GS-033)、[GS-034](http://127.0.0.1:8765/open/GS-034)、[GS-035](http://127.0.0.1:8765/open/GS-035)、[GS-036](http://127.0.0.1:8765/open/GS-036)、[GS-037](http://127.0.0.1:8765/open/GS-037)、[GS-038](http://127.0.0.1:8765/open/GS-038)、[GS-039](http://127.0.0.1:8765/open/GS-039)、[GS-040](http://127.0.0.1:8765/open/GS-040)、[GS-041](http://127.0.0.1:8765/open/GS-041)、[GS-049](http://127.0.0.1:8765/open/GS-049)、[GS-050](http://127.0.0.1:8765/open/GS-050)、[GS-056](http://127.0.0.1:8765/open/GS-056)、[GS-059](http://127.0.0.1:8765/open/GS-059)、[GS-063](http://127.0.0.1:8765/open/GS-063)、[GS-073](http://127.0.0.1:8765/open/GS-073)、[GS-079](http://127.0.0.1:8765/open/GS-079)、[GS-080](http://127.0.0.1:8765/open/GS-080)、[GS-091](http://127.0.0.1:8765/open/GS-091)、[GS-120](http://127.0.0.1:8765/open/GS-120)、[GS-121](http://127.0.0.1:8765/open/GS-121)、[GS-133](http://127.0.0.1:8765/open/GS-133)、[GS-148](http://127.0.0.1:8765/open/GS-148)、[GS-151](http://127.0.0.1:8765/open/GS-151)、[GS-162](http://127.0.0.1:8765/open/GS-162)、[GS-257](http://127.0.0.1:8765/open/GS-257)、[GS-258](http://127.0.0.1:8765/open/GS-258)、[GS-312](http://127.0.0.1:8765/open/GS-312)、[GS-331](http://127.0.0.1:8765/open/GS-331)、[GS-350](http://127.0.0.1:8765/open/GS-350)、[GS-390](http://127.0.0.1:8765/open/GS-390)、[GS-393](http://127.0.0.1:8765/open/GS-393)、[GS-396](http://127.0.0.1:8765/open/GS-396)、[GS-397](http://127.0.0.1:8765/open/GS-397)、[GS-400](http://127.0.0.1:8765/open/GS-400)、[GS-404](http://127.0.0.1:8765/open/GS-404)、[GS-407](http://127.0.0.1:8765/open/GS-407)、[GS-413](http://127.0.0.1:8765/open/GS-413)、[GS-430](http://127.0.0.1:8765/open/GS-430)、[GS-436](http://127.0.0.1:8765/open/GS-436)、[GS-438](http://127.0.0.1:8765/open/GS-438)、[GS-440](http://127.0.0.1:8765/open/GS-440)、[GS-443](http://127.0.0.1:8765/open/GS-443)、[GS-445](http://127.0.0.1:8765/open/GS-445)、[GS-446](http://127.0.0.1:8765/open/GS-446)、[GS-447](http://127.0.0.1:8765/open/GS-447)、[GS-448](http://127.0.0.1:8765/open/GS-448)、[GS-449](http://127.0.0.1:8765/open/GS-449)、[GS-450](http://127.0.0.1:8765/open/GS-450)、[GS-452](http://127.0.0.1:8765/open/GS-452)、[GS-453](http://127.0.0.1:8765/open/GS-453)、[GS-454](http://127.0.0.1:8765/open/GS-454)、[GS-455](http://127.0.0.1:8765/open/GS-455)、[GS-456](http://127.0.0.1:8765/open/GS-456)、[GS-457](http://127.0.0.1:8765/open/GS-457)、[GS-458](http://127.0.0.1:8765/open/GS-458)、[GS-459](http://127.0.0.1:8765/open/GS-459)、[GS-460](http://127.0.0.1:8765/open/GS-460)、[GS-461](http://127.0.0.1:8765/open/GS-461)、[GS-463](http://127.0.0.1:8765/open/GS-463)、[GS-468](http://127.0.0.1:8765/open/GS-468)、[GS-469](http://127.0.0.1:8765/open/GS-469)、[GS-470](http://127.0.0.1:8765/open/GS-470)、[GS-471](http://127.0.0.1:8765/open/GS-471)、[GS-472](http://127.0.0.1:8765/open/GS-472)、[GS-475](http://127.0.0.1:8765/open/GS-475)、[GS-478](http://127.0.0.1:8765/open/GS-478)、[GS-479](http://127.0.0.1:8765/open/GS-479)、[GS-481](http://127.0.0.1:8765/open/GS-481)、[GS-482](http://127.0.0.1:8765/open/GS-482)、[GS-484](http://127.0.0.1:8765/open/GS-484)、[GS-487](http://127.0.0.1:8765/open/GS-487)、[GS-488](http://127.0.0.1:8765/open/GS-488)、[GS-492](http://127.0.0.1:8765/open/GS-492)、[GS-493](http://127.0.0.1:8765/open/GS-493)、[GS-494](http://127.0.0.1:8765/open/GS-494)、[GS-496](http://127.0.0.1:8765/open/GS-496)、[GS-497](http://127.0.0.1:8765/open/GS-497)、[GS-498](http://127.0.0.1:8765/open/GS-498)、[GS-499](http://127.0.0.1:8765/open/GS-499)、[GS-500](http://127.0.0.1:8765/open/GS-500)、[GS-501](http://127.0.0.1:8765/open/GS-501)、[GS-505](http://127.0.0.1:8765/open/GS-505)、[GS-507](http://127.0.0.1:8765/open/GS-507)、[GS-508](http://127.0.0.1:8765/open/GS-508)、[GS-509](http://127.0.0.1:8765/open/GS-509)、[GS-511](http://127.0.0.1:8765/open/GS-511)、[GS-512](http://127.0.0.1:8765/open/GS-512)、[GS-515](http://127.0.0.1:8765/open/GS-515)、[GS-516](http://127.0.0.1:8765/open/GS-516)、[GS-517](http://127.0.0.1:8765/open/GS-517)、[GS-518](http://127.0.0.1:8765/open/GS-518)、[GS-519](http://127.0.0.1:8765/open/GS-519)、[GS-520](http://127.0.0.1:8765/open/GS-520)、[GS-523](http://127.0.0.1:8765/open/GS-523)、[GS-525](http://127.0.0.1:8765/open/GS-525)、[GS-526](http://127.0.0.1:8765/open/GS-526)、[GS-527](http://127.0.0.1:8765/open/GS-527)、[GS-528](http://127.0.0.1:8765/open/GS-528)、[GS-529](http://127.0.0.1:8765/open/GS-529)、[GS-530](http://127.0.0.1:8765/open/GS-530)、[GS-533](http://127.0.0.1:8765/open/GS-533)、[GS-534](http://127.0.0.1:8765/open/GS-534)、[GS-535](http://127.0.0.1:8765/open/GS-535)、[GS-536](http://127.0.0.1:8765/open/GS-536)、[GS-538](http://127.0.0.1:8765/open/GS-538)、[GS-539](http://127.0.0.1:8765/open/GS-539)、[GS-540](http://127.0.0.1:8765/open/GS-540)、[GS-541](http://127.0.0.1:8765/open/GS-541)、[GS-542](http://127.0.0.1:8765/open/GS-542)、[GS-543](http://127.0.0.1:8765/open/GS-543)、[GS-544](http://127.0.0.1:8765/open/GS-544)、[GS-545](http://127.0.0.1:8765/open/GS-545)、[GS-546](http://127.0.0.1:8765/open/GS-546)、[GS-547](http://127.0.0.1:8765/open/GS-547)、[GS-548](http://127.0.0.1:8765/open/GS-548)、[GS-549](http://127.0.0.1:8765/open/GS-549)、[GS-550](http://127.0.0.1:8765/open/GS-550)、[GS-551](http://127.0.0.1:8765/open/GS-551)、[GS-558](http://127.0.0.1:8765/open/GS-558)、[GS-562](http://127.0.0.1:8765/open/GS-562)、[GS-567](http://127.0.0.1:8765/open/GS-567)、[GS-568](http://127.0.0.1:8765/open/GS-568)、[GS-569](http://127.0.0.1:8765/open/GS-569)、[GS-570](http://127.0.0.1:8765/open/GS-570)、[GS-571](http://127.0.0.1:8765/open/GS-571)、[GS-573](http://127.0.0.1:8765/open/GS-573)、[GS-574](http://127.0.0.1:8765/open/GS-574)、[GS-575](http://127.0.0.1:8765/open/GS-575)、[GS-576](http://127.0.0.1:8765/open/GS-576)、[GS-577](http://127.0.0.1:8765/open/GS-577)、[GS-578](http://127.0.0.1:8765/open/GS-578)、[GS-579](http://127.0.0.1:8765/open/GS-579)、[GS-580](http://127.0.0.1:8765/open/GS-580)、[GS-581](http://127.0.0.1:8765/open/GS-581)、[GS-582](http://127.0.0.1:8765/open/GS-582)、[GS-583](http://127.0.0.1:8765/open/GS-583)、[GS-584](http://127.0.0.1:8765/open/GS-584)、[GS-585](http://127.0.0.1:8765/open/GS-585)、[GS-586](http://127.0.0.1:8765/open/GS-586)、[GS-587](http://127.0.0.1:8765/open/GS-587)、[GS-592](http://127.0.0.1:8765/open/GS-592)、[GS-594](http://127.0.0.1:8765/open/GS-594)、[GS-595](http://127.0.0.1:8765/open/GS-595)、[GS-611](http://127.0.0.1:8765/open/GS-611)、[GS-612](http://127.0.0.1:8765/open/GS-612)、[GS-649](http://127.0.0.1:8765/open/GS-649)、[GS-650](http://127.0.0.1:8765/open/GS-650)、[LA-019](http://127.0.0.1:8765/open/LA-019)、[LA-021](http://127.0.0.1:8765/open/LA-021)、[LA-061](http://127.0.0.1:8765/open/LA-061)、[LA-098](http://127.0.0.1:8765/open/LA-098)、[LA-106](http://127.0.0.1:8765/open/LA-106)、[LA-113](http://127.0.0.1:8765/open/LA-113)、[LA-118](http://127.0.0.1:8765/open/LA-118)。
- card_updated: 正式错题卡未改写；164 题逐题运行质量门已通过，本次只同步正式视觉页的 manifest/index 状态。
- visual_update: 164 个正式视觉详情页均已按 manifest 路径复核，题图可见、解析折叠，无旧版 `## 解析图` 外泄结构；这些题没有单独 `solution_assets`，但质量门确认折叠解析或视觉结构满足当前收口条件。
- source_retention: 24 条合并来源记录保留为 `merged_into_wrongnet` 来源证据，`card_decision` 统一为 `already_in_wrongnet_source_retained`，不混入正式视觉页统计。
- manifest_update: `manifest.json` 中 164 条 `linked_wrongnet` 正式记录收口为 `already_in_wrongnet_enhanced`，`asset_to_obsidian.json` 更新相关资产日期，`可视化错题详情/index.md` 164 行正式索引更新到 `2026-07-03`；Obsidian bridge snapshot 已刷新。
- validation: 164 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`，无 ERROR；JSON 解析、正式索引 13 列、manifest 路径结构均通过。
- remaining: 广义正式 `linked_wrongnet` 未 enhanced 队列剩余 321 题，其中多为正式卡字段缺失或 wiki/index 覆盖缺口；不得硬标 enhanced。
- rollback_action: not_run。

## 2026-07-03｜可视化质量门 wiki 索引补登 97 题
- scope: GS-004；GS-021；GS-028；GS-042；GS-046；GS-051；GS-066；GS-071；GS-074；GS-081；GS-084；GS-086；GS-092；GS-093；GS-094；GS-096；GS-097；GS-100；GS-104；GS-107；GS-127；GS-129；GS-138；GS-143；GS-145；GS-163；GS-170；GS-221；GS-225；GS-232；GS-243；GS-266；GS-267；GS-268；GS-283；GS-287；GS-309；GS-316；GS-317；GS-318；GS-326；GS-376；GS-431；GS-432；GS-433；GS-434；GS-435；GS-439；GS-441；GS-442；GS-444；GS-451；GS-464；GS-465；GS-466；GS-467；GS-473；GS-474；GS-476；GS-477；GS-480；GS-483；GS-485；GS-486；GS-489；GS-490；GS-491；GS-495；GS-503；GS-504；GS-506；GS-510；GS-513；GS-514；GS-521；GS-522；GS-524；GS-532；GS-537；GS-552；GS-553；GS-554；GS-555；GS-556；GS-557；GS-559；GS-560；GS-561；GS-563；GS-564；GS-565；GS-566；GS-572；GS-588；GS-590；GS-591；GS-596。
- card_updated: none。
- wiki_created: 新建 `MATHWIKI-MAINT-003_可视化质量门wiki索引补登.md`。
- wiki_updated: `wiki/index.md` 增加维护入口，集中挂接 97 个仅缺总索引登记的正式 `linked_wrongnet` 题号。
- validation_plan: 复跑本批质量门和全量 873 条可视化审计，确认剩余失败项只来自正式卡关键字段缺失或 `method_gap` 格式问题。
- wrongnet_rebuild: not_run（本次只修改 wiki/index/log 与维护页，未修改正式错题卡）。
- rollback_action: not_run。

## 2026-07-03｜极限首批缺字段补强 GS-006/008/009/010/011/013
- scope: [GS-006](http://127.0.0.1:8765/open/GS-006)、[GS-008](http://127.0.0.1:8765/open/GS-008)、[GS-009](http://127.0.0.1:8765/open/GS-009)、[GS-010](http://127.0.0.1:8765/open/GS-010)、[GS-011](http://127.0.0.1:8765/open/GS-011)、[GS-013](http://127.0.0.1:8765/open/GS-013)。
- evidence: 已查看 6 张题图，并读取对应可视化详情页折叠解析文字；这些题均无单独解析图，但解析文字足以确认复做入口与标准答案。
- card_updated: 6 张正式卡补入 `wrong_point` 复做入口和 `视觉详情已核对` 关键词；修正 GS-006、GS-008、GS-009、GS-010、GS-011、GS-013 的答案展示格式；不从题图/解析反推用户本人原始错因。
- wiki_created: 新建 `MATHWIKI-MAINT-004_极限首批缺字段补强.md`。
- wiki_updated: `wiki/index.md` 挂接本批维护页，确保 GS-008 进入总索引覆盖。
- validation: 已运行 `wrongnet.py rebuild`、`build_wrong_card_source_summaries.py`、`build_knowledge_cluster_pages.py`、`build_pattern_cluster_pages.py`、`refresh_obsidian_bridge_snapshot.py`；6 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- quality_note: WARN 仅保留个人错因占位和 `method_gap not enabled`，原因是缺少用户本人当时作答过程，不能编造个人错因或方法断点。
- rollback_action: not_run。

## 2026-07-03｜极限与估计第二批缺字段补强 GS-018/019/023/026/029/044
- scope: [GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-019](http://127.0.0.1:8765/open/GS-019)、[GS-023](http://127.0.0.1:8765/open/GS-023)、[GS-026](http://127.0.0.1:8765/open/GS-026)、[GS-029](http://127.0.0.1:8765/open/GS-029)、[GS-044](http://127.0.0.1:8765/open/GS-044)。
- evidence: 已查看 6 张题图，并读取对应正式卡和可视化详情页；GS-044 的旧折叠解析与题图不一致，本轮已按题图纠正。
- card_updated: 6 张正式卡补入具体 `wrong_point`、答案展示和 `视觉详情已核对` 关键词；GS-044 将题目摘要改回振荡积分分部估计，不再保留误混入的中值定理解析。
- visual_updated: 修正 `GS-044_1000题A组11.10.md` 可视化详情页折叠解析、复述和 deep wiki 链接。
- wiki_created: 新建 `MATHWIKI-MAINT-005_极限与估计第二批缺字段补强.md`。
- wiki_updated: `wiki/index.md` 挂接本批维护页，确保 GS-018/019/023/026/029/044 进入总索引覆盖。
- validation: 已运行 `wrongnet.py rebuild`、`build_wrong_card_source_summaries.py`、`build_knowledge_cluster_pages.py`、`build_pattern_cluster_pages.py`、`refresh_obsidian_bridge_snapshot.py`；6 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- full_audit: 全量 873 条可视化记录复跑完成；731 条 `linked_wrongnet` 中 521 条通过质量门、210 条未通过；另有 131 条 `merged_into_wrongnet`、10 条 `needs_card_decision`、1 条 `needs_manual_relink`。
- rollback_action: not_run。
## 2026-07-03｜早期高数缺字段第三批补强 GS-045/047/052/053/054/055/058/060/061/062/064/065
- scope: [GS-045](http://127.0.0.1:8765/open/GS-045)、[GS-047](http://127.0.0.1:8765/open/GS-047)、[GS-052](http://127.0.0.1:8765/open/GS-052)、[GS-053](http://127.0.0.1:8765/open/GS-053)、[GS-054](http://127.0.0.1:8765/open/GS-054)、[GS-055](http://127.0.0.1:8765/open/GS-055)、[GS-058](http://127.0.0.1:8765/open/GS-058)、[GS-060](http://127.0.0.1:8765/open/GS-060)、[GS-061](http://127.0.0.1:8765/open/GS-061)、[GS-062](http://127.0.0.1:8765/open/GS-062)、[GS-064](http://127.0.0.1:8765/open/GS-064)、[GS-065](http://127.0.0.1:8765/open/GS-065)。
- evidence: 已查看本批 12 张题图，并读取对应正式卡和可视化详情页折叠解析文字。
- card_updated: 12 张正式卡补入具体 `wrong_point`、题型、答案展示、知识点/方法/陷阱和复做提醒；仅对已有视觉详情明确错点的题保留 method_gap，不从题图反推用户本人原始错因。
- visual_updated: 12 个可视化详情页同步复述、正式卡入口、source summary 和入库判断，修正旧自动复述中的题型错配。
- wiki_created: 新建 `MATHWIKI-MAINT-006_早期高数缺字段第三批补强.md`。
- validation: 已运行 `wrongnet.py rebuild`、source summaries、知识点/方法簇页、Obsidian bridge snapshot；12 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- rollback_action: not_run。
- full_audit_after_maint006: 全量 873 条可视化记录复跑完成；731 条 `linked_wrongnet` 中 533 条通过质量门、198 条未通过；另有 131 条 `merged_into_wrongnet`、10 条 `needs_card_decision`、1 条 `needs_manual_relink`；最新可行动剩余 209 条。
## 2026-07-03｜早期高数缺字段第四批补强 GS-067/068/069/070/075/076/077/078/082/083/085/088
- scope: [GS-067](http://127.0.0.1:8765/open/GS-067)、[GS-068](http://127.0.0.1:8765/open/GS-068)、[GS-069](http://127.0.0.1:8765/open/GS-069)、[GS-070](http://127.0.0.1:8765/open/GS-070)、[GS-075](http://127.0.0.1:8765/open/GS-075)、[GS-076](http://127.0.0.1:8765/open/GS-076)、[GS-077](http://127.0.0.1:8765/open/GS-077)、[GS-078](http://127.0.0.1:8765/open/GS-078)、[GS-082](http://127.0.0.1:8765/open/GS-082)、[GS-083](http://127.0.0.1:8765/open/GS-083)、[GS-085](http://127.0.0.1:8765/open/GS-085)、[GS-088](http://127.0.0.1:8765/open/GS-088)。
- evidence: 已查看本批 12 张题图，并读取对应正式卡和可视化详情页折叠解析文字。
- card_updated: 12 张正式卡补入或修正 `answer`、`wrong_point`、`question_type`、知识点/方法/陷阱、复做提醒；对 GS-067/076/078/082/083 写入可由视觉详情支撑的 method_gap，其余不编造个人错因。
- visual_updated: 12 个可视化详情页同步复述、正式卡入口、source summary 和入库判断。
- wiki_created: 新建 `MATHWIKI-MAINT-007_早期高数缺字段第四批补强.md`。
- validation: 已运行 `wrongnet.py rebuild`、source summaries、知识点/方法簇页、Obsidian bridge snapshot；12 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- rollback_action: not_run。

## 2026-07-03｜导数定义与可导性缺字段第五批补强 GS-089/090/098/101/102/103/105/106/108/109/110/111
- scope: [GS-089](http://127.0.0.1:8765/open/GS-089)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-098](http://127.0.0.1:8765/open/GS-098)、[GS-101](http://127.0.0.1:8765/open/GS-101)、[GS-102](http://127.0.0.1:8765/open/GS-102)、[GS-103](http://127.0.0.1:8765/open/GS-103)、[GS-105](http://127.0.0.1:8765/open/GS-105)、[GS-106](http://127.0.0.1:8765/open/GS-106)、[GS-108](http://127.0.0.1:8765/open/GS-108)、[GS-109](http://127.0.0.1:8765/open/GS-109)、[GS-110](http://127.0.0.1:8765/open/GS-110)、[GS-111](http://127.0.0.1:8765/open/GS-111)。
- evidence: 已查看本批 12 张题图，并读取对应正式卡和可视化详情页折叠解析文字。
- card_updated: 12 张正式卡补入或修正 `question_type`、`wrong_point`、`answer`、知识点/方法/陷阱和复做提醒；仅对 GS-090/GS-103 写入可由视觉详情支撑的 method_gap，其余不编造个人错因。
- visual_updated: 12 个可视化详情页同步复述、正式卡入口、source summary 和入库判断。
- wiki_created: 新建 `MATHWIKI-MAINT-008_导数定义与可导性缺字段第五批补强.md`。
- validation: 已运行 `wrongnet.py rebuild`、source summaries、知识点/方法簇页、Obsidian bridge snapshot；12 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- rollback_action: not_run。
- full_audit_after_maint008: 全量 873 条可视化记录复跑完成；731 条 `linked_wrongnet` 中 557 条通过质量门、174 条未通过；另有 131 条 `merged_into_wrongnet`、10 条 `needs_card_decision`、1 条 `needs_manual_relink`；最新可行动剩余 185 条。

## 2026-07-03｜高阶导数与反函数缺字段第六批补强 GS-112/113/114/116/117/118/119/122/124/125/126/130
- scope: [GS-112](http://127.0.0.1:8765/open/GS-112), [GS-113](http://127.0.0.1:8765/open/GS-113), [GS-114](http://127.0.0.1:8765/open/GS-114), [GS-116](http://127.0.0.1:8765/open/GS-116), [GS-117](http://127.0.0.1:8765/open/GS-117), [GS-118](http://127.0.0.1:8765/open/GS-118), [GS-119](http://127.0.0.1:8765/open/GS-119), [GS-122](http://127.0.0.1:8765/open/GS-122), [GS-124](http://127.0.0.1:8765/open/GS-124), [GS-125](http://127.0.0.1:8765/open/GS-125), [GS-126](http://127.0.0.1:8765/open/GS-126), [GS-130](http://127.0.0.1:8765/open/GS-130)。
- evidence: 已读取本批 12 张正式卡、12 个可视化详情页和对应题图/折叠解析入口；本批多数题缺用户本人原始作答过程，按安全复做入口补强。
- card_updated: 12 张正式卡已补强或确认 `question_type`、`wrong_point`、`answer`、知识点/方法/陷阱和复做提醒；修复上一轮中断脚本遗留的 LaTeX 转义问题。
- visual_updated: 12 个可视化详情页同步复述、正式卡入口、source summary 和入库判断，题图保持可见，解析保持折叠。
- wiki_created: 新建 `MATHWIKI-MAINT-009_高阶导数与反函数缺字段第六批补强.md`。
- validation: 已运行 `wrongnet.py rebuild`、source summaries、知识点/方法簇页、Obsidian bridge snapshot；12 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`；全量 873 条审计已复跑，731 条 `linked_wrongnet` 中 569 条通过、162 条未通过；另有 10 条需建卡决策、1 条需人工重连，最新可行动剩余 173 条。
- rollback_action: not_run。

- full_audit_after_maint009: 全量 873 条可视化记录复跑完成；731 条 `linked_wrongnet` 中 569 条通过质量门、162 条未通过；另有 131 条 `merged_into_wrongnet`、10 条 `needs_card_decision`、1 条 `needs_manual_relink`；最新可行动剩余 173 条。

## 2026-07-03｜一元微分应用缺字段第七批补强 GS-131/132/134/135/136/140/141/144/146/150/153/154
- scope: [GS-131](http://127.0.0.1:8765/open/GS-131), [GS-132](http://127.0.0.1:8765/open/GS-132), [GS-134](http://127.0.0.1:8765/open/GS-134), [GS-135](http://127.0.0.1:8765/open/GS-135), [GS-136](http://127.0.0.1:8765/open/GS-136), [GS-140](http://127.0.0.1:8765/open/GS-140), [GS-141](http://127.0.0.1:8765/open/GS-141), [GS-144](http://127.0.0.1:8765/open/GS-144), [GS-146](http://127.0.0.1:8765/open/GS-146), [GS-150](http://127.0.0.1:8765/open/GS-150), [GS-153](http://127.0.0.1:8765/open/GS-153), [GS-154](http://127.0.0.1:8765/open/GS-154)。
- evidence: 已读取本批 12 张正式卡、12 个可视化详情页、关键题图和折叠解析文字；其中 GS-150 额外依据题图确认反函数渐近线为 $y=3$ 与 $y=-3$。
- card_updated: 12 张正式卡已补强或修正 `question_type`、`wrong_point`、`answer`、知识点/方法/陷阱和复做提醒；对 GS-131/132/134/135/140/141/150/154 写入视觉证据支撑的 method_gap，其余不编造个人错因。
- visual_updated: 12 个可视化详情页同步复述、正式卡入口、source summary 和入库判断，题图保持可见，解析保持折叠。
- wiki_created: 新建 `MATHWIKI-MAINT-010_一元微分应用缺字段第七批补强.md`。
- validation: 已运行 `wrongnet.py rebuild`、source summaries、知识点/方法簇页、Obsidian bridge snapshot；12 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- rollback_action: not_run。
- full_audit_after_maint010: 全量 873 条可视化记录复跑完成；731 条 `linked_wrongnet` 中 581 条通过质量门、150 条未通过；另有 131 条 `merged_into_wrongnet`、10 条 `needs_card_decision`、1 条 `needs_manual_relink`；最新可行动剩余 161 条。

## 2026-07-03｜一元微分与积分缺字段第八批补强 GS-155/156/157/158/159/160/161/166/171/172/173/174
- scope: [GS-155](http://127.0.0.1:8765/open/GS-155), [GS-156](http://127.0.0.1:8765/open/GS-156), [GS-157](http://127.0.0.1:8765/open/GS-157), [GS-158](http://127.0.0.1:8765/open/GS-158), [GS-159](http://127.0.0.1:8765/open/GS-159), [GS-160](http://127.0.0.1:8765/open/GS-160), [GS-161](http://127.0.0.1:8765/open/GS-161), [GS-166](http://127.0.0.1:8765/open/GS-166), [GS-171](http://127.0.0.1:8765/open/GS-171), [GS-172](http://127.0.0.1:8765/open/GS-172), [GS-173](http://127.0.0.1:8765/open/GS-173), [GS-174](http://127.0.0.1:8765/open/GS-174)。
- evidence: 已查看本批 12 张题图，并读取对应正式卡与可视化详情页；其中 GS-161、GS-166 原折叠解析不足，本轮依据题图补入轻量答案。
- card_updated: 12 张正式卡补强 `question_type`、`wrong_point`、`answer`、知识点/方法/陷阱和复做提醒；GS-156 保留并修正用户明确的符号判断 method_gap，其余题不从题图反推个人 method_gap。
- visual_updated: 12 个可视化详情页同步复述、正式卡入口、source summary 和 `already_in_wrongnet_enhanced` 判断，题图保持可见，解析保持折叠。
- wiki_created: 新建 `MATHWIKI-MAINT-011_一元微分与积分缺字段第八批补强.md`。
- validation: 已运行 `wrongnet.py rebuild`、source summaries、知识点/方法簇页、Obsidian bridge snapshot；12 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- full_audit_after_maint011: 全量 873 条可视化记录复跑完成；731 条 `linked_wrongnet` 中 593 条通过质量门、138 条未通过；另有 131 条 `merged_into_wrongnet`、10 条 `needs_card_decision`、1 条 `needs_manual_relink`；最新可行动剩余 149 条。
- rollback_action: not_run。

## 2026-07-03｜反常积分与定积分缺字段第九批补强
- scope: [GS-175](http://127.0.0.1:8765/open/GS-175)、[GS-176](http://127.0.0.1:8765/open/GS-176)、[GS-177](http://127.0.0.1:8765/open/GS-177)、[GS-178](http://127.0.0.1:8765/open/GS-178)、[GS-179](http://127.0.0.1:8765/open/GS-179)、[GS-180](http://127.0.0.1:8765/open/GS-180)、[GS-181](http://127.0.0.1:8765/open/GS-181)、[GS-182](http://127.0.0.1:8765/open/GS-182)、[GS-184](http://127.0.0.1:8765/open/GS-184)、[GS-191](http://127.0.0.1:8765/open/GS-191)、[GS-200](http://127.0.0.1:8765/open/GS-200)、[GS-209](http://127.0.0.1:8765/open/GS-209)。
- evidence: 已查看本批 12 张题图，并读取对应正式卡与可视化详情页折叠解析文字。
- card_updated: 12 张正式卡补强 `question_type`、`wrong_point`、`answer`、知识点/方法/陷阱、掌握度待评分说明和复做提醒；GS-182 清理旧的不相关 method_gap，不从题图反推个人错因。
- visual_updated: 12 个可视化详情页同步复述、正式卡入口、source summary 和 `already_in_wrongnet_enhanced` 判断，题图保持可见，解析保持折叠。
- wiki_created: 新建 `MATHWIKI-MAINT-012_反常积分与定积分缺字段第九批补强.md`。
- validation: 已运行 `wrongnet.py rebuild`、source summaries、知识点/方法簇页、Obsidian bridge snapshot；12 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- full_audit_after_maint012: 全量 873 条可视化记录复跑完成；862 条有效 wrongnet 挂接中 715 条通过质量门、147 条未通过；另有 11 条 `wrongnet_id` 为待确认，最新可行动剩余 158 条。
- tutor_safe_source: 已向 `数学LLMWiki安全输入包.md` 追加反常积分、主值陷阱、定积分比较、微分方程性质和指数因子辅助函数的高层训练项；未复制完整题干或长解析。
- rollback_action: not_run。

## 2026-07-03 MATHWIKI-MAINT-013：中值定理与黎曼和缺字段第十批补强

- 读取 873 条可视化题库审计失败队列后，补强 PR-001、GS-212、GS-214、GS-215、GS-216、GS-217、GS-219、GS-220、GS-223、GS-224、GS-226 的正式卡答案、知识点挂载、方法入口、易错陷阱和视觉详情复述。
- 修正 GS-224 的 method_gap：入口不是 0 点 Taylor，而是拉格朗日中值定理 $f(x)=f'(\xi_x)x$。
- 发现 VIS-GS-152 与 VIS-GS-079 的题图/解析内容和原挂载正式卡不一致，已标记为视觉错连待重连，未把错连视觉证据写入正式卡。
- 全量 873 条视觉记录复跑：正式有效挂载 860 条，质量通过 726 条，失败 134 条，待重连/未正式挂载 13 条，actionable remaining 147 条。

## 2026-07-03 MATHWIKI-MAINT-014：中值定理零点与Taylor估计缺字段补强

- 从 873 条可视化审计失败队列继续处理 15 张正式卡：GS-227, GS-228, GS-229, GS-230, GS-231, GS-234, GS-235, GS-236, GS-239, GS-240, GS-241, GS-242, GS-244, GS-245, GS-246。
- 依据题图和折叠解析文字补齐答案、具体错点、知识点、方法、陷阱和复做提醒；其中 GS-231 依据已有个人断点记录补强 method_gap。
- 同步更新视觉详情、manifest、visual index、open links、wiki/index、wiki/log 和数学 LLMWiki 安全输入包；不修改回滚 JSON。
- 全量 873 条视觉记录复跑：正式有效挂载 860 条，质量通过 742 条，失败 118 条，待重连/未正式挂载 13 条，actionable remaining 131 条。
## 2026-07-03 MATHWIKI-MAINT-015：导数应用相关变化率与根式积分补强

- scope: GS-248, GS-250, GS-251, GS-252, GS-254, GS-255, GS-259, GS-260, GS-261, GS-264, GS-265, GS-269, GS-270, GS-271；另标记 `GS-249` 视觉错连待人工重连。
- evidence: 已查看本批题图联系表，读取对应正式卡与可视化详情页折叠解析；对无解析文字但题图可判的 GS-254/GS-265 只补轻量入口和答案。
- card_updated: 14 张正式卡补强 `wrong_point`、`answer`、`question_type`、知识点/方法/陷阱、掌握度待评分说明和复做提醒；不从题图反推个人 method_gap。
- visual_updated: 14 个可视化详情页同步复述、正式卡入口、source summary 和 `already_in_wrongnet_enhanced` 判断；`GS-249` 改为 `suspect_wrongnet_mismatch`。
- wiki_created: 新建 `MATHWIKI-MAINT-015_导数应用相关变化率与根式积分补强.md`。
- validation: 已运行 `wrongnet.py rebuild`、source summaries、知识点/方法簇页、Obsidian bridge snapshot；14 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- full_audit_after_maint015: 全量 873 条可视化记录复跑完成；859 条有效 wrongnet 挂接中 756 条通过质量门、103 条未通过；另有 14 条待重连/未正式挂接，最新可行动剩余 117 条。审计快照为 `/tmp/kaoyan_math_visual_873_full_audit_after_maint015.json`。
- rollback_action: not_run。

## 2026-07-03 MATHWIKI-MAINT-016：积分计算与相关变化率缺字段补强

- scope: GS-343, GS-285, GS-272, GS-274, GS-275, GS-276, GS-277, GS-278, GS-282, GS-284, GS-286, GS-291。
- evidence: 已查看本批题图联系表，并读取对应正式卡与视觉详情页；对缺少解析文字的积分题按题图可确认的标准入口和答案补强。
- card_updated: 12 张正式卡补强 `wrong_point`、`answer`、`question_type`、知识点、方法、陷阱、掌握度待评分说明和复做提醒；GS-286 保留已掌握状态。
- visual_updated: 12 个可视化详情页同步折叠解析、复述、正式卡入口和入库判断。
- wiki_created: 新建 `MATHWIKI-MAINT-016_积分计算与相关变化率缺字段补强.md`。
- validation: 已运行 `wrongnet.py rebuild`、source summaries、知识点/方法簇页、Obsidian bridge snapshot；12 题逐题运行 `intake_quality_gate.py --visual expected` 均为 `quality_gate=ok`。
- full_audit_after_maint016: 全量 873 条可视化记录复跑完成；859 条有效 wrongnet 挂接中 768 条通过质量门、91 条未通过；另有 14 条待重连/未正式挂接，最新可行动剩余 105 条。审计快照为 `/tmp/kaoyan_math_visual_873_full_audit_after_maint016.json`。
- rollback_action: not_run。

## 2026-07-03｜MATHWIKI-MAINT-017

- 使用 Obsidian 运行时重新审计 873 条题库可视化记录。
- 当前剩余：102 条已挂正式卡但质量门硬失败，14 条未挂卡/待确认/疑似错连，总计 116 条动作项。
- 已写入维护页：[[maintenance/MATHWIKI-MAINT-017_873题库可视化实时审计剩余队列]]。
- 由于普通 shell/Python 对 kaoyan-math 既有文件返回 Operation not permitted，本轮未继续修改正式错题卡，未运行 wrongnet rebuild，等待权限恢复后继续闭环。

## 2026-07-03 MATHWIKI-MAINT-018：定积分等式不等式与积分表示缺字段补强

- input: 873 题库可视化审计剩余队列中的第 11 讲定积分相关缺字段卡片。
- source_refs: `错题知识网络/错题卡/`；`错题知识网络/可视化错题详情/高等数学/`；`错题知识网络/可视化错题详情/manifest.json`；`错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-006_定积分错题总线.md`；Tutor 安全输入包。
- cards_updated: GS-293；GS-296；GS-306；GS-313；GS-314；GS-315；GS-319；GS-320；GS-321；GS-322；GS-323；GS-324。
- visual_updated: GS-293；GS-296；GS-306；GS-313；GS-314；GS-315；GS-319；GS-320；GS-321；GS-322；GS-323；GS-324 的可视化详情、`manifest.json`、`可视化错题详情/index.md`。
- wiki_created: `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-018_定积分等式不等式与积分表示缺字段补强.md`。
- wiki_updated: `wiki/index.md`；`MATHWIKI-GS-TOPIC-006_定积分错题总线.md`；`MATHWIKI-GS-METHOD-072_积分不等式证明入口链.md`；`MATHWIKI-GS-METHOD-083_旋转体曲面变量选择与生成量链.md`；Tutor 安全输入包；wrong-card source summaries 和覆盖矩阵。
- card_decision: already_in_wrongnet_enhanced。
- wrongnet_rebuild: ok，`python3 错题知识网络/scripts/wrongnet.py rebuild` 输出 cards=770 strong=1924 medium=805 weak_audit=275。
- wiki_coverage: ok，source summaries=770，compiled=733，knowledge_clusters=394，method_clusters=1247，error_clusters=292，action_gap_clusters=9。
- obsidian_bridge: ok，records=873，assets=1253。
- quality_gate: ok，12/12 通过 `intake_quality_gate.py --visual expected`；合理警告为旧题缺少用户本人错因证据、method_gap 不启用。
- rollback_action: not_needed；未修改回滚 JSON。
- missing_info: 缺少用户当时作答过程，掌握度保持待评分；GS-314 与 GS-322 为同源重复候选，暂不合并。
- full_audit_after_maint018: 全量 873 条可视化记录复跑完成；859 条有效 wrongnet 挂接中 780 条通过质量门、79 条未通过；另有 14 条待重连/未正式挂接，最新可行动剩余 93 条。审计快照为 `/tmp/kaoyan_math_visual_873_full_audit_after_maint018.json`。

## 2026-07-03 MATHWIKI-MAINT-019：定积分分部变限与不等式缺字段补强

- input: 873 题库可视化审计剩余队列中的第 11 讲定积分分部、变限积分与不等式相关缺字段卡片。
- scope: [GS-327](http://127.0.0.1:8765/open/GS-327)、[GS-328](http://127.0.0.1:8765/open/GS-328)、[GS-329](http://127.0.0.1:8765/open/GS-329)、[GS-330](http://127.0.0.1:8765/open/GS-330)、[GS-332](http://127.0.0.1:8765/open/GS-332)、[GS-333](http://127.0.0.1:8765/open/GS-333)、[GS-334](http://127.0.0.1:8765/open/GS-334)、[GS-335](http://127.0.0.1:8765/open/GS-335)、[GS-336](http://127.0.0.1:8765/open/GS-336)、[GS-337](http://127.0.0.1:8765/open/GS-337)、[GS-339](http://127.0.0.1:8765/open/GS-339)、[GS-340](http://127.0.0.1:8765/open/GS-340)。
- source_refs: 正式错题卡；可视化详情页；`manifest.json`；`MATHWIKI-GS-TOPIC-006_定积分错题总线.md`；`MATHWIKI-GS-METHOD-072_积分不等式证明入口链.md`；Tutor 安全输入包。
- cards_updated: 12 张正式卡补强 `wrong_point`、`answer`、`question_type`、`knowledge`、`methods`、`traps`、`wrong_history`、`mastery_history`；缺少用户作答过程，掌握度保持待评分，`method_gap` 不启用。
- visual_updated: 12 个可视化详情页同步复述、正式卡入口、source summary 和 `already_in_wrongnet_enhanced` 判断。
- wiki_created: `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-019_定积分分部变限与不等式缺字段补强.md`。
- wiki_updated: `wiki/index.md`；`MATHWIKI-GS-TOPIC-006_定积分错题总线.md`；`MATHWIKI-GS-METHOD-072_积分不等式证明入口链.md`；Tutor 安全输入包；wrong-card source summaries 和覆盖矩阵。
- card_decision: already_in_wrongnet_enhanced。
- wrongnet_rebuild: ok，`python3 错题知识网络/scripts/wrongnet.py rebuild` 输出 cards=770 strong=1926 medium=800 weak_audit=268。
- wiki_coverage: ok，source summaries=770，compiled=716，knowledge_clusters=394，method_clusters=1258，error_clusters=292，action_gap_clusters=9。
- obsidian_bridge: ok，records=873，assets=1253。
- quality_gate: ok，12/12 通过 `intake_quality_gate.py --visual expected`；合理警告为旧题缺少用户本人错因证据、method_gap 不启用。
- full_audit_after_maint019: 全量 873 条可视化记录复跑完成；859 条有效 wrongnet 挂接中 792 条通过质量门、67 条未通过；另有 14 条待重连/未正式挂接，最新可行动剩余 81 条。审计快照为 `/tmp/kaoyan_math_visual_873_full_audit_after_maint019.json`。
- rollback_action: not_needed；未修改回滚 JSON。

## 2026-07-03 MATHWIKI-MAINT-020：中值积分估计与多元极限缺字段补强

- input: 873 题库可视化审计剩余队列中的中值积分估计、多元极限与二元函数性质相关缺字段卡片。
- scope: [GS-342](http://127.0.0.1:8765/open/GS-342)、[GS-325](http://127.0.0.1:8765/open/GS-325)、[GS-345](http://127.0.0.1:8765/open/GS-345)、[GS-346](http://127.0.0.1:8765/open/GS-346)、[GS-347](http://127.0.0.1:8765/open/GS-347)、[GS-348](http://127.0.0.1:8765/open/GS-348)、[GS-351](http://127.0.0.1:8765/open/GS-351)、[GS-352](http://127.0.0.1:8765/open/GS-352)、[GS-353](http://127.0.0.1:8765/open/GS-353)、[GS-355](http://127.0.0.1:8765/open/GS-355)、[GS-357](http://127.0.0.1:8765/open/GS-357)、[GS-358](http://127.0.0.1:8765/open/GS-358)。
- cards_updated: 12 张正式卡补强 `wrong_point`、`answer`、`question_type`、`knowledge`、`methods`、`traps`、`wrong_history`、`mastery_history`；缺少用户作答过程，掌握度保持待评分，`method_gap` 不启用。
- visual_updated: 12 个可视化详情页同步复述、正式卡入口、source summary 和 `already_in_wrongnet_enhanced` 判断；GS-325 原折叠解析与题图不一致，已按振荡积分分部估计修正。
- wiki_created: `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-020_中值积分估计与多元极限缺字段补强.md`；`错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-085_二重极限路径与累次极限判别链.md`。
- wiki_updated: `wiki/index.md`；`MATHWIKI-GS-TOPIC-006_定积分错题总线.md`；`MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`；`MATHWIKI-GS-METHOD-072_积分不等式证明入口链.md`；`MATHWIKI-GS-METHOD-084_双端点Taylor余项估值链.md`；`MATHWIKI-GS-METHOD-050_二元函数性质定义判别链.md`；Tutor 安全输入包。
- card_decision: already_in_wrongnet_enhanced。
- wrongnet_rebuild: ok，`python3 错题知识网络/scripts/wrongnet.py rebuild` 输出 cards=770 strong=1901 medium=830 weak_audit=266。
- wiki_coverage: ok，source summaries=770，compiled=716，knowledge_clusters=395，method_clusters=1270，error_clusters=292，action_gap_clusters=9。
- obsidian_bridge: ok，records=873，assets=1253。
- quality_gate: ok，12/12 通过 `intake_quality_gate.py --visual expected`；合理警告为旧题缺少用户本人错因证据、method_gap 不启用。
- full_audit_after_maint020: 全量 873 条可视化记录复跑完成；859 条有效 wrongnet 挂接中 793 条通过质量门、66 条未通过；另有 14 条待重连/未正式挂接，最新可行动剩余 80 条。相对 MAINT-019，本批 12 条失败记录均已离开失败列表，同时审计新浮出 11 条 `wrong_point` 仍含占位词的旧卡，净剩余减少 1 条；审计快照为 `/tmp/kaoyan_math_visual_873_full_audit_after_maint020.json`。
- rollback_action: not_needed；未修改回滚 JSON。

## 2026-07-03 MATHWIKI-MAINT-021：定积分应用旧卡占位错点补强

- input: MAINT-020 全量审计中新浮出的 11 条 `wrong_point` 仍含占位词的旧卡。
- scope: [GS-294](http://127.0.0.1:8765/open/GS-294)、[GS-295](http://127.0.0.1:8765/open/GS-295)、[GS-297](http://127.0.0.1:8765/open/GS-297)、[GS-298](http://127.0.0.1:8765/open/GS-298)、[GS-299](http://127.0.0.1:8765/open/GS-299)、[GS-300](http://127.0.0.1:8765/open/GS-300)、[GS-301](http://127.0.0.1:8765/open/GS-301)、[GS-302](http://127.0.0.1:8765/open/GS-302)、[GS-303](http://127.0.0.1:8765/open/GS-303)、[GS-304](http://127.0.0.1:8765/open/GS-304)、[GS-305](http://127.0.0.1:8765/open/GS-305)。
- cards_updated: 11 张正式卡将 `wrong_point` 从“待补充”占位改为可复做第一动作；`error_causes` 改为“暂无明确个人错因”。
- visual_updated: not_needed；本轮不改题图/解析图，沿用现有可视化详情和方法页入口。
- wiki_created: `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-021_定积分应用旧卡占位错点补强.md`。
- wiki_updated: `wiki/index.md`；Tutor 安全输入包。
- card_decision: already_in_wrongnet_enhanced。
- wrongnet_rebuild: ok，`python3 错题知识网络/scripts/wrongnet.py rebuild` 输出 cards=770 strong=1901 medium=831 weak_audit=266。
- wiki_coverage: ok，source summaries=770，compiled=716，knowledge_clusters=395，method_clusters=1270，error_clusters=292，action_gap_clusters=9。
- obsidian_bridge: ok，records=873，assets=1253。
- quality_gate: ok，11/11 通过 `intake_quality_gate.py --visual expected`；合理警告为旧题缺少用户本人错因证据、method_gap 不启用。
- full_audit_after_maint021: 全量 873 条可视化记录复跑完成；859 条有效 wrongnet 挂接中 804 条通过质量门、55 条未通过；另有 14 条待重连/未正式挂接，最新可行动剩余 69 条。相对 MAINT-020，本批 11 条失败记录均已离开失败列表；审计快照为 `/tmp/kaoyan_math_visual_873_full_audit_after_maint021.json`，剩余报告为 `/tmp/kaoyan_math_visual_873_remaining_report.md`。
- rollback_action: not_needed；未修改回滚 JSON。

## 2026-07-03 MATHWIKI-MAINT-022：多元函数性质全微分与恰当方程缺字段补强

- input: MAINT-021 全量审计剩余队列中的第 13 讲多元函数微分学与第 15 讲微分方程缺字段卡片。
- scope: [GS-359](http://127.0.0.1:8765/open/GS-359)、[GS-361](http://127.0.0.1:8765/open/GS-361)、[GS-364](http://127.0.0.1:8765/open/GS-364)、[GS-365](http://127.0.0.1:8765/open/GS-365)、[GS-366](http://127.0.0.1:8765/open/GS-366)、[GS-368](http://127.0.0.1:8765/open/GS-368)、[GS-370](http://127.0.0.1:8765/open/GS-370)、[GS-371](http://127.0.0.1:8765/open/GS-371)、[GS-372](http://127.0.0.1:8765/open/GS-372)、[GS-374](http://127.0.0.1:8765/open/GS-374)、[GS-377](http://127.0.0.1:8765/open/GS-377)、[GS-378](http://127.0.0.1:8765/open/GS-378)。
- cards_updated: 12 张正式卡补强 `question_type`、`wrong_point`、`knowledge`、`methods`、`traps`、`answer`、`wrong_history`、`mastery_history`、`method_gap` 和复做提醒；缺少用户当时作答过程，掌握度保持待评分。
- visual_updated: 12 个可视化详情页同步题目定位、正确第一步、核心方法、易错触发、方法页连线和 `already_in_wrongnet_enhanced` 判断。
- wiki_created: `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-022_多元函数性质全微分与恰当方程缺字段补强.md`。
- wiki_updated: `wiki/index.md`；`MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线.md`；`MATHWIKI-GS-TOPIC-009_微分方程错题总线.md`；`MATHWIKI-GS-METHOD-050_二元函数性质定义判别链.md`；`MATHWIKI-GS-METHOD-046_多元公式模板入口链.md`；`MATHWIKI-GS-METHOD-056_微分方程入口判别链.md`；Tutor 安全输入包。
- card_decision: already_in_wrongnet_enhanced。
- wrongnet_rebuild: ok，`python3 错题知识网络/scripts/wrongnet.py rebuild` 输出 cards=770 strong=1899 medium=831 weak_audit=265。
- wiki_coverage: ok，source summaries=770，compiled=716，knowledge_clusters=395，method_clusters=1283，error_clusters=297，action_gap_clusters=9。
- obsidian_bridge: ok，records=873，assets=1253。
- quality_gate: ok，12/12 通过 `intake_quality_gate.py --visual expected`；首次运行只有 log 未登记警告，已补本条 log 后复验。
- full_audit_after_maint022: ok，全量 873 条可视化记录中 859 条已链接现有卡，819 条达到 quality_ok，40 条仍 failed，14 条未链接或待确认，剩余 actionable 54 条；快照 `/tmp/kaoyan_math_visual_873_full_audit_after_maint022.json`，剩余清单 `/tmp/kaoyan_math_visual_873_remaining_report.md`。
- rollback_action: not_needed；未修改回滚 JSON。

## 2026-07-03 MATHWIKI-MAINT-023：全微分偏微分方程物理积分与错连收口

- input: MAINT-022 全量审计剩余队列中的全微分判参、偏微分方程、定积分物理应用、平均速度与约束二次型最值卡片。
- scope: [GS-379](http://127.0.0.1:8765/open/GS-379)、[GS-385](http://127.0.0.1:8765/open/GS-385)、[GS-416](http://127.0.0.1:8765/open/GS-416)、[GS-417](http://127.0.0.1:8765/open/GS-417)、[GS-424](http://127.0.0.1:8765/open/GS-424)；[GS-589](http://127.0.0.1:8765/open/GS-589) 补 wiki/log 覆盖并规范化 `method_gap.opd_tag`；VIS-GS-341、VIS-GS-344 标记为错连待重连。
- cards_updated: 5 张正式卡补强 `question_type`、`wrong_point`、`knowledge`、`methods`、`traps`、`method_gap` 和复做提醒；GS-589 仅修复旧卡 `method_gap.opd_tag` 结构；缺少用户当时作答过程的题，掌握度保持待评分。
- visual_updated: 5 个可视化详情页同步题目定位、正确第一步、核心方法、易错触发和 `already_in_wrongnet_enhanced`；VIS-GS-341、VIS-GS-344 改为 `suspect_wrongnet_mismatch`，不再作为正式 GS 卡证据。
- wiki_created: `错题知识网络/wiki/maintenance/MATHWIKI-MAINT-023_全微分偏微分方程物理积分与错连收口.md`。
- wiki_updated: `wiki/index.md`；`MATHWIKI-GS-METHOD-046_多元公式模板入口链.md`；`MATHWIKI-GS-METHOD-031_偏微分方程变量代换化简.md`；`MATHWIKI-GS-METHOD-056_微分方程入口判别链.md`；`MATHWIKI-GS-METHOD-038_定积分物理应用微元法.md`；`MATHWIKI-GS-METHOD-033_多元函数条件与闭区域最值.md`；`MATHWIKI-LA-METHOD-002_二次型Rayleigh商最值.md`；Tutor 安全输入包。
- wrongnet_rebuild: ok，`python3 错题知识网络/scripts/wrongnet.py rebuild` 输出 cards=770，strong=1916，medium=816，weak_audit=263。
- wiki_coverage: ok，source summaries=770，compiled=718，knowledge_clusters=395，method_clusters=1284，error_clusters=297，action_gap_clusters=9。
- obsidian_bridge: ok，records=873，assets=1253。
- quality_gate: ok，GS-379、GS-385、GS-416、GS-417、GS-424、GS-589 均通过 `intake_quality_gate.py --visual expected`。
- full_audit_after_maint023: ok，全量 873 条可视化记录中 857 条已链接现有卡，825 条达到 quality_ok，32 条仍 failed，16 条未链接或待确认，剩余 actionable 48 条；快照 `/tmp/kaoyan_math_visual_873_full_audit_after_maint023.json`，剩余清单 `/tmp/kaoyan_math_visual_873_remaining_report.md`。
- rollback_action: not_needed；未修改回滚 JSON。
## [2026-07-03] maintenance | MAINT-024 线代行列式二次型与矩阵幂缺字段补强

- 范围：LA-007, LA-008, LA-013, LA-014, LA-015, LA-016, LA-018, LA-022, LA-023, LA-025, LA-026, LA-028, LA-032, LA-036, LA-047。
- 写入：正式卡 method_gap、可视化详情复述/连线、manifest/index/open-link、线代 topic/method 页、Tutor 安全输入包。
- 边界：LA-004 / MN4-GS-CH01-514 标记为 suspect_wrongnet_mismatch，暂不作为线代 LA-004 证据；未修改回滚 JSON。
- 验证：wrongnet rebuild 通过（cards=770, strong=1939, medium=794）；覆盖脚本与 bridge snapshot 已刷新；15 张线代卡质量门全部 ok；873 条全量可视化审计 failed_records=0，not_linked_or_missing=18。

## [2026-07-03] maintenance | MAINT-025 待编译视觉卡深度方法链补强

- 范围：[GS-047](http://127.0.0.1:8765/open/GS-047)、[GS-054](http://127.0.0.1:8765/open/GS-054)、[GS-055](http://127.0.0.1:8765/open/GS-055)、[GS-062](http://127.0.0.1:8765/open/GS-062)、[GS-070](http://127.0.0.1:8765/open/GS-070)、[GS-176](http://127.0.0.1:8765/open/GS-176)、[GS-191](http://127.0.0.1:8765/open/GS-191)。
- 写入：新增 `MATHWIKI-GS-METHOD-086_递推数列不变区间与单调有界闭环.md`、`MATHWIKI-GS-METHOD-087_含参反常积分候选根与奇点回查.md`、`MATHWIKI-GS-METHOD-088_微分方程解后复合值域闭环.md`、`MATHWIKI-MAINT-025_待编译视觉卡深度方法链补强.md`。
- 更新：`MATHWIKI-GS-METHOD-050_二元函数性质定义判别链.md`、数列极限总线、定积分总线、微分方程总线、多元函数与二重积分总线、`wiki/index.md`、Tutor 安全输入包。
- 边界：本轮只补深度 wiki 编译链和 Tutor 高层训练入口；正式错题卡不改，回滚 JSON 不改，生成目录不手改。
- 验证：`build_wrong_card_source_summaries.py` 通过，cards=770、summaries=770、compiled=740；本批 7 张卡均离开 `深度编译页=待编译`；Obsidian CLI 可检索新方法页与维护页；7/7 正式卡通过 `intake_quality_gate.py --visual expected`。因未修改正式错题卡，本轮未运行 `wrongnet.py rebuild`。

## [2026-07-03] maintenance | MAINT-026 根式分式积分旧卡深度方法链补强

- 范围：[GS-269](http://127.0.0.1:8765/open/GS-269)、[GS-270](http://127.0.0.1:8765/open/GS-270)、[GS-271](http://127.0.0.1:8765/open/GS-271)、[GS-275](http://127.0.0.1:8765/open/GS-275)、[GS-276](http://127.0.0.1:8765/open/GS-276)、[GS-282](http://127.0.0.1:8765/open/GS-282)。
- 写入：新增 `MATHWIKI-MAINT-026_根式分式积分旧卡深度方法链补强.md`；更新 `MATHWIKI-GS-METHOD-043_根式积分换元与回代链.md`、`MATHWIKI-GS-METHOD-076_分式积分拆到底与分母降幂链.md`、`MATHWIKI-GS-METHOD-087_含参反常积分候选根与奇点回查.md`。
- 更新：不定积分总线、定积分总线、`wiki/index.md`、Tutor 安全输入包；修正 `build_wrong_card_source_summaries.py` 对 `formal_card_enhanced` 视觉状态的识别，使已增强正式卡的视觉详情能进入 source summary。
- 边界：本轮只补深度 wiki 编译链、视觉映射生成逻辑和 Tutor 高层训练入口；正式错题卡不改，回滚 JSON 不改，生成目录不手改。
- 验证：`build_wrong_card_source_summaries.py` 通过，cards=770、summaries=770、compiled=746；本批 6 张卡均离开 `deep_wiki=待编译` 且 source summary 已恢复视觉入口；6/6 通过 `intake_quality_gate.py --visual expected`，仅有旧题缺少用户作答过程导致的 `method_gap not enabled` 合理警告；Obsidian CLI 可检索维护页和方法页。因未修改正式错题卡，本轮未运行 `wrongnet.py rebuild`。

## [2026-07-03] maintenance | MAINT-027 剩余待编译线代高数旧卡分流补强

- 范围：[GS-405](http://127.0.0.1:8765/open/GS-405)、[LA-004](http://127.0.0.1:8765/open/LA-004)、[LA-006](http://127.0.0.1:8765/open/LA-006)、[LA-011](http://127.0.0.1:8765/open/LA-011)、[LA-017](http://127.0.0.1:8765/open/LA-017)、[LA-021](http://127.0.0.1:8765/open/LA-021)、[LA-024](http://127.0.0.1:8765/open/LA-024)、[LA-027](http://127.0.0.1:8765/open/LA-027)、[LA-029](http://127.0.0.1:8765/open/LA-029)、[LA-051](http://127.0.0.1:8765/open/LA-051)、[LA-065](http://127.0.0.1:8765/open/LA-065)、[LA-077](http://127.0.0.1:8765/open/LA-077)、[LA-080](http://127.0.0.1:8765/open/LA-080)、[LA-083](http://127.0.0.1:8765/open/LA-083)、[LA-084](http://127.0.0.1:8765/open/LA-084)、[LA-085](http://127.0.0.1:8765/open/LA-085)、[LA-086](http://127.0.0.1:8765/open/LA-086)、[LA-095](http://127.0.0.1:8765/open/LA-095)、[LA-096](http://127.0.0.1:8765/open/LA-096)、[LA-098](http://127.0.0.1:8765/open/LA-098)、[LA-101](http://127.0.0.1:8765/open/LA-101)、[LA-102](http://127.0.0.1:8765/open/LA-102)、[LA-107](http://127.0.0.1:8765/open/LA-107)、[LA-108](http://127.0.0.1:8765/open/LA-108)。
- 写入：新增 `MATHWIKI-MAINT-027_剩余待编译线代高数旧卡分流补强.md`；更新二重积分总线、二重积分区域化归方法页、线代综合待精分分流台、线代矩阵运算总线、线性方程组与向量组总线、二次型与特征结构总线、行列式总线、对应 LA/GS 方法页、`wiki/index.md`、Tutor 安全输入包。
- 分流：GS-405 只按“先核对区域再计算”接入二重积分链；LA-004 标记为线代标题与高数隐函数内容不一致的待核对样本；LA-006/024/077/107/108 作为章节总纲型旧卡；LA-011/017 接入行列式结构化计算；LA-021/051/101/102 接入 \(|f(A)|=0\) 与伴随矩阵迹链；LA-027/029 接入二次型矩阵化与正交变换链；LA-065 接入矩阵秩待核对入口；LA-080/083/084/085/086/095/096/098 接入方程组与向量组方法链。
- 边界：本轮只补深度 wiki 编译链和 Tutor 高层训练入口；正式错题卡不改，回滚 JSON 不改，`错题知识网络/生成/` 不手改；OCR 待核对、章节总纲和错连嫌疑卡不补造个人错因、掌握度或 method_gap。
- 验证：`build_wrong_card_source_summaries.py` 通过，cards=770、summaries=770、compiled=770；24/24 均离开 `deep_wiki=待编译`；因未修改正式错题卡，本轮未运行 `wrongnet.py rebuild`。

## [2026-07-03] maintenance | MAINT-028 剩余视觉候选方法链与 Tutor 安全补强

- 范围：[MN4-GS-CH01-670](http://127.0.0.1:8765/open/MN4-GS-CH01-670)、[MN4-GS-CH01-683](http://127.0.0.1:8765/open/MN4-GS-CH01-683)、[VIS-GS-426-MISMATCH-OLD](http://127.0.0.1:8765/open/VIS-GS-426-MISMATCH-OLD)、[VIS-GS-427-MISMATCH-OLD](http://127.0.0.1:8765/open/VIS-GS-427-MISMATCH-OLD)、[VIS-GS-428-MISMATCH-OLD](http://127.0.0.1:8765/open/VIS-GS-428-MISMATCH-OLD)、[VIS-GS-429-MISMATCH-OLD](http://127.0.0.1:8765/open/VIS-GS-429-MISMATCH-OLD)。
- 写入：新增 `MATHWIKI-MAINT-028_剩余视觉候选方法链与Tutor安全补强.md`；更新 4 个错连候选视觉详情页的方法页连线；更新 `MATHWIKI-LA-METHOD-008`、`MATHWIKI-LA-METHOD-010`、`MATHWIKI-LA-METHOD-011`、线代矩阵运算总线、候选决策队列、`wiki/index.md` 和 Tutor 安全输入包。
- 边界：6 个样本均有题图/解析图，但缺用户本人错因；本轮只做 method-page-only 和 Tutor-safe 补强，不创建正式 LA 卡，不写掌握度，不改回滚 JSON。
- 验证：本轮为 wiki/视觉候选补强，未修改正式错题卡，未运行 `wrongnet.py rebuild`；后续运行 Markdown/Obsidian 检索与结构校验。

## [2026-07-03] maintenance | MAINT-029 线代错连视觉入口重连

- 范围：[LA-002](http://127.0.0.1:8765/open/LA-002)、[LA-011](http://127.0.0.1:8765/open/LA-011)、[LA-017](http://127.0.0.1:8765/open/LA-017)；来源误挂页 `VIS-GS-249`、`VIS-GS-341`、`VIS-GS-344`。
- 写入：新增 `MATHWIKI-MAINT-029_线代错连视觉入口重连.md`；新增/补齐 `VIS-LA-002`、`VIS-LA-011`、`VIS-LA-017` 正式视觉详情；更新原误挂 GS 视觉页为来源保留状态。
- 更新：`manifest.json`、`asset_to_obsidian.json`、可视化 `index.md`、`obsidian_open_links.md`、`MATHWIKI-LA-TOPIC-005`、`MATHWIKI-LA-METHOD-001`、`MATHWIKI-LA-METHOD-015`、`MATHWIKI-LA-METHOD-018`、候选队列、`wiki/index.md`、Tutor 安全输入包。
- 边界：本轮先做视觉入口重连、wiki 方法链和 Tutor-safe 补强；质量门发现 LA-002、LA-011、LA-017 既有正式卡缺字段后，已补答案、题型、知识点和复做第一动作。回滚 JSON 不改，不新增个人错因或掌握度。
- 待复核：`VIS-GS-079`、`VIS-GS-152`、`VIS-LA-004` 仍为 `suspect_wrongnet_mismatch`；需要后续人工确认题图归属。
- 验证：正式卡补强后已运行 `wrongnet.py rebuild`，输出 cards=770、strong=1925、medium=806、weak_audit=257；source summaries=770、compiled=770；knowledge_clusters=403；method_clusters=1323；Obsidian bridge records=876、assets=1256；LA-002、LA-011、LA-017 三张卡 `intake_quality_gate.py --visual expected` 均为 ok。

## [2026-07-03] maintenance | MAINT-030 中值定理错连视觉候选收口

- 范围：[VIS-GS-079](http://127.0.0.1:8765/open/VIS-GS-079)、[VIS-GS-152](http://127.0.0.1:8765/open/VIS-GS-152)。
- 写入：新增 `MATHWIKI-MAINT-030_中值定理错连视觉候选收口.md`；修正两个视觉详情页正文，移除原 `GS-079`、`GS-152` 正式卡、source summary 和错误知识点连线。
- 更新：`MATHWIKI-GS-METHOD-077_中值定理证明目标反推链.md` 登记二者为候选视觉证据；`MATHWIKI-QUESTIONS-003` 新增 B5 当前 suspect 队列；`wiki/index.md`、可视化 `index.md`、`manifest.json` 和 Tutor 安全输入包同步当前状态。
- 边界：本轮只处理视觉候选正文残留、wiki 方法链和 Tutor-safe 补强；未修改正式错题卡，未新增个人错因、掌握度或 method_gap，未修改回滚 JSON。
- 验证：`manifest.json` 与 `asset_to_obsidian.json` 解析通过；Obsidian bridge 已刷新到 records=876、assets=1256；Obsidian CLI 可检索新维护页、方法页和两个候选视觉页；正文残留检查确认两页不再链接原正式 `GS-079`、`GS-152` 卡；`git diff --check` 通过。

## [2026-07-03] maintenance | MAINT-031 隐函数历史编号异常收口

- 范围：[LA-004](http://127.0.0.1:8765/open/LA-004)、[MN4-GS-CH01-514](http://127.0.0.1:8765/open/MN4-GS-CH01-514)、[VIS-LA-004](http://127.0.0.1:8765/open/VIS-LA-004)。
- 写入：新增 `MATHWIKI-GS-METHOD-089_隐函数方程组求导与点值联立.md`、`MATHWIKI-MAINT-031_隐函数历史编号异常收口.md`。
- 正式卡更新：`LA-004` 保留历史编号，但 subject/chapter/knowledge/methods 改为高数隐函数求导；移除错误的线代知识点、幂指极限标签和长 OCR 摘要；掌握度保持待评分，用户个人错因仍待确认。
- 视觉更新：`MN4-GS-CH01-514`、`VIS-LA-004` 改为 `needs_manual_relink`；open-link 优先跳转到视觉详情页自身；方法页挂接 `MATHWIKI-GS-METHOD-089`。
- wiki/Tutor 更新：更新 `wiki/index.md`、`MATHWIKI-QUESTIONS-003`、`MATHWIKI-LA-TOPIC-002`、可视化 index、open links、manifest、asset map 和数学 LLMWiki 安全输入包。
- 边界：不新建 `GS-*` 卡，不重编号，不补造用户个人错因，不写掌握度，不修改回滚 JSON。
- 验证：`wrongnet.py rebuild` 已通过，cards=770、strong=1918、medium=815、weak_audit=257；wiki 覆盖刷新完成，knowledge_clusters=403、method_clusters=1325、error_clusters=297、action_gap_clusters=9、source summaries=770、compiled=770；`manifest.json` 与 `asset_to_obsidian.json` 解析通过；Obsidian bridge 已刷新到 records=876、assets=1256；`LA-004` 质量门为 `quality_gate=ok`，仅保留用户个人错因未记录和 method_gap 未启用的预期 WARN；Obsidian CLI 可检索 `MATHWIKI-GS-METHOD-089` 与 `MATHWIKI-MAINT-031`；HTTP bridge 可打开 `LA-004`、`MN4-GS-CH01-514`、`VIS-LA-004`；旧簇残留检查未再命中 `SRC-WQ-LA-004` 的幂指极限/线性方程组错链。

## [2026-07-03] maintenance | MAINT-032 线代候选队列方法页一致性补校

- 范围：[VIS-GS-426-MISMATCH-OLD](http://127.0.0.1:8765/open/VIS-GS-426-MISMATCH-OLD)、[VIS-GS-427-MISMATCH-OLD](http://127.0.0.1:8765/open/VIS-GS-427-MISMATCH-OLD)、[VIS-GS-428-MISMATCH-OLD](http://127.0.0.1:8765/open/VIS-GS-428-MISMATCH-OLD)、[VIS-GS-429-MISMATCH-OLD](http://127.0.0.1:8765/open/VIS-GS-429-MISMATCH-OLD)。
- 写入：新增 `MATHWIKI-MAINT-032_线代候选队列方法页一致性补校.md`；更新 `MATHWIKI-QUESTIONS-003` A 队列中 4 个线代候选的“已挂方法页”字段，移除残留的“待补充”描述；更新 `wiki/index.md`。
- 核对：已查看题图/解析图，确认 426 为反对称差矩阵判零，427 为秩一矩阵幂，428 为 \(A=E+N\) 幂零截断，429 为旋转矩阵周期与负指数化简。
- 边界：本轮只做 wiki 队列一致性补校；正式 LA 卡仍因缺用户本人错因和第一卡点而不创建；不修改正式错题卡，不运行 `wrongnet.py rebuild`，不改回滚 JSON。Tutor 安全输入包已有对应高层训练入口，本轮只核对不重复写入。

## [2026-07-03] maintenance | MAINT-033 Wiki 索引日期与候选表格链接修复

- 范围：`wiki/index.md`、`MATHWIKI-QUESTIONS-003`。
- 写入：新增 `MATHWIKI-MAINT-033_Wiki索引日期与候选表格链接修复.md`；修复 `MATHWIKI-GS-METHOD-069`、`MATHWIKI-GS-METHOD-015` 两条索引的异常日期字段；清理 A/B/B2 候选表中会破坏 Markdown 表格列结构的 wikilink 别名管道。
- 边界：本轮只修 LLM Wiki 结构一致性；不修改正式错题卡，不创建新卡，不补造个人错因、掌握度或 method_gap，不改回滚 JSON，不手改生成目录。

## [2026-07-03] maintenance | MAINT-034 当前视觉与正式卡证据边界复核

- 范围：当前 `manifest.json` 876 条视觉记录、覆盖矩阵 16 张 `method_status = 缺方法标签` 正式卡、`MATHWIKI-QUESTIONS-003`。
- 写入：新增 `MATHWIKI-MAINT-034_当前视觉与正式卡证据边界复核.md`；刷新 `MATHWIKI-QUESTIONS-003` 的全量视觉结构巡检基线，从旧 873 条更新为当前 876 条，并标明 861 条已确认正式关联、15 条仍需证据判断。
- 复核结论：16 张正式卡的方法缺口均属于题干/OCR/正确视觉证据不足或历史误链保留，不应硬填正式 `methods`、个人错因或 `method_gap`。
- 脚本修复：`build_wrong_card_source_summaries.py` 的 `TODAY` 从固定 `2026-07-01` 改为按北京时间当天生成，避免后续覆盖/source summary 刷新继续写入过期日期。
- 边界：本轮不修改正式错题卡、不运行 `wrongnet.py rebuild`、不改回滚 JSON、不手改生成目录。

## [2026-07-03] maintenance | MAINT-035 PR001 历史编号异常收口

- 范围：[PR-001](http://127.0.0.1:8765/open/PR-001)、[VIS-PR-001](http://127.0.0.1:8765/open/PR-001)、[MN4-GS-CH01-236](http://127.0.0.1:8765/open/MN4-GS-CH01-236)。
- 写入：新增 `MATHWIKI-MAINT-035_PR001历史编号异常收口.md`；正式卡 `PR-001` 的 `subject` 改为高等数学，补稳定视觉引用、`wrong_history`、`keywords` 和历史编号说明；正式视觉详情迁入 `可视化错题详情/高等数学/`。
- 更新：`manifest.json`、`asset_to_obsidian.json`、可视化 `index.md`、`obsidian_open_links.md`、`MATHWIKI-QUESTIONS-003`、`wiki/index.md`、Tutor 安全输入包；同时修正 knowledge/method/action-gap 自动簇脚本的日期生成逻辑，避免后续重建写回旧日期。
- 验证：运行 `wrongnet.py rebuild`，当前正式卡 770 张、strong 1918、medium 815；重建 source summary 770 条、知识点簇 403、方法簇 1325、错因簇 297、动作断点簇 9；刷新 Obsidian bridge 快照 876 条记录、1256 个资产；`PR-001` 质量门无 ERROR。
- 收口：覆盖表按实际 `subject` 分组，旧 `MATHWIKI-COVERAGE-PR` 派生表已移除；`PR-001` 仅作为历史编号异常保留编号，实际进入高等数学覆盖表。
- 边界：保留历史 `PR-001` 编号，不新建 `GS-*` 卡；不补造用户个人错因、掌握度或 `method_gap`；不修改回滚 JSON。

## [2026-07-03] maintenance | MAINT-036 视觉候选边界与 Tutor 安全输入校准

- 范围：当前 876 条视觉详情记录；重点复核 VIS-GS-079、VIS-GS-152、MN4-GS-CH01-514、VIS-LA-004；质量门抽查 GS-651 至 GS-658。
- 写入：新增 `MATHWIKI-MAINT-036_视觉候选边界与Tutor安全输入校准.md`；更新 `wiki/index.md` 和数学 LLMWiki 安全输入包。
- 复核结论：当前 861 条视觉记录已确认正式关联或正式卡增强；剩余 15 条为证据边界项，其中 10 条缺用户本人错因、3 条需人工重连、2 条疑似错连，不能自动正式入库。
- Tutor 更新：新增“视觉候选证据边界”训练项，训练候选、人工重连、错连三类判断动作；不复制完整题干、完整解析或题图 OCR。
- 验证：`manifest.json` 当前统计为 linked_wrongnet=676、formal_card_enhanced=54、merged_into_wrongnet=131、needs_card_decision=10、needs_manual_relink=3、suspect_wrongnet_mismatch=2；GS-651 至 GS-658 已通过 `intake_quality_gate.py --visual expected`。
- 边界：本轮不修改正式错题卡，不运行 `wrongnet.py rebuild`，不修改回滚 JSON，不手改 `错题知识网络/生成/`。

## [2026-07-03] maintenance | MAINT-037 线代矩阵方程视觉状态复核

- 范围：[LA-059](http://127.0.0.1:8765/open/LA-059)、[LA-060](http://127.0.0.1:8765/open/LA-060)、[LA-061](http://127.0.0.1:8765/open/LA-061)、[LA-062](http://127.0.0.1:8765/open/LA-062)、[LA-063](http://127.0.0.1:8765/open/LA-063)、[LA-064](http://127.0.0.1:8765/open/LA-064)。
- 核对：已重新读取 LLM Wiki Lint、Tutor、数学错题入库、Obsidian CLI/Markdown 和 Tutor 集成规则；已核对 6 题正式卡、视觉详情、题图/解析图、方法页、Tutor 安全输入和质量门结果。
- 写入：新增 `MATHWIKI-MAINT-037_线代矩阵方程视觉状态复核.md`；修正 `LA-061_1000题B组3.7.md` 视觉详情页的入库判断状态为 `already_in_wrongnet_enhanced`，补 `quality_gate: ok`；更新 `wiki/index.md`。
- 复核结论：6 题均已入正式 wrongnet，题图/解析与正式卡轻量摘要一致；LA-059 至 LA-064 质量门均为 `quality_gate=ok`。旧批量卡缺用户本人作答过程，`error_causes` 占位和 `method_gap` 未启用仍是正确边界。
- Tutor：安全输入包已有“分块矩阵秩消元边界”“分块伴随矩阵”“矩阵方程按列拆”训练项，本轮验证不重复写入。
- 边界：未修改正式错题卡，不运行 `wrongnet.py rebuild`，不修改回滚 JSON，不手改 `错题知识网络/生成/`。

## [2026-07-03] maintenance | MAINT-038 线代秩零空间与向量组视觉复核

- 范围：[LA-067](http://127.0.0.1:8765/open/LA-067)、[LA-068](http://127.0.0.1:8765/open/LA-068)、[LA-069](http://127.0.0.1:8765/open/LA-069)、[LA-070](http://127.0.0.1:8765/open/LA-070)、[LA-071](http://127.0.0.1:8765/open/LA-071)、[LA-072](http://127.0.0.1:8765/open/LA-072)、[LA-073](http://127.0.0.1:8765/open/LA-073)、[LA-074](http://127.0.0.1:8765/open/LA-074)、[LA-075](http://127.0.0.1:8765/open/LA-075)、[LA-078](http://127.0.0.1:8765/open/LA-078)、[LA-079](http://127.0.0.1:8765/open/LA-079)、[LA-081](http://127.0.0.1:8765/open/LA-081)。
- 核对：已按用户要求重新读取 `LLM Wiki Lint`、`Tutor`、数学错题入库、Obsidian CLI/Markdown 和 Tutor 集成规则；已核对 12 题正式卡、视觉详情、题图/解析图、方法页、Tutor 安全输入包和 StudyVault dashboard。
- 写入：新增 `MATHWIKI-MAINT-038_线代秩零空间与向量组视觉复核.md`；更新 `wiki/index.md`，登记本轮实际复核范围和技能读取结果。
- 复核结论：LA-067 至 LA-073 仍由 `MATHWIKI-LA-METHOD-013` 覆盖；LA-074 由 `MATHWIKI-LA-METHOD-010` 覆盖；LA-075 由 `MATHWIKI-LA-METHOD-014` 覆盖；LA-078、LA-079、LA-081 由 `MATHWIKI-LA-METHOD-017` 覆盖。题图/解析图与方法页轻量摘要一致。
- Tutor：安全输入包已经覆盖矩阵秩约束、伴随矩阵、向量组等价、零空间和秩约束训练入口，本轮状态为 `verified_not_updated`，不复制完整题干或解析进入 Tutor。
- 边界：未修改正式错题卡，不运行 `wrongnet.py rebuild`，不修改回滚 JSON，不手改 `错题知识网络/生成/`；旧批量卡缺用户本人作答过程，不从标准解析反推个人错因、掌握度或 method_gap。

## [2026-07-03] maintenance | MAINT-039 线代方程组与向量组视觉复核

- 范围：[LA-082](http://127.0.0.1:8765/open/LA-082)、[LA-087](http://127.0.0.1:8765/open/LA-087)、[LA-088](http://127.0.0.1:8765/open/LA-088)、[LA-089](http://127.0.0.1:8765/open/LA-089)、[LA-090](http://127.0.0.1:8765/open/LA-090)、[LA-091](http://127.0.0.1:8765/open/LA-091)、[LA-092](http://127.0.0.1:8765/open/LA-092)、[LA-093](http://127.0.0.1:8765/open/LA-093)、[LA-094](http://127.0.0.1:8765/open/LA-094)、[LA-097](http://127.0.0.1:8765/open/LA-097)、[LA-099](http://127.0.0.1:8765/open/LA-099)、[LA-100](http://127.0.0.1:8765/open/LA-100)。
- 核对：已重新读取数学错题入库、LLM Wiki Lint、LLM Wiki Query、Tutor、Obsidian CLI/Markdown 和 Tutor 集成规则；已核对 12 题正式卡、视觉详情、题图/解析图、方法页、Tutor 安全输入包和 StudyVault dashboard。
- 写入：新增 `MATHWIKI-MAINT-039_线代方程组与向量组视觉复核.md`；更新 `wiki/index.md`，登记本轮实际复核范围、方法页覆盖和质量门结果。
- 复核结论：LA-082、LA-091 由 `MATHWIKI-LA-METHOD-016` 覆盖；LA-087 由 `MATHWIKI-LA-METHOD-005` 与 `MATHWIKI-LA-METHOD-016` 覆盖；LA-088 由 `MATHWIKI-LA-METHOD-013` 与 `MATHWIKI-LA-METHOD-017` 覆盖；LA-089、LA-090 由 `MATHWIKI-LA-METHOD-015` 与 `MATHWIKI-LA-METHOD-016` 覆盖；LA-092、LA-093、LA-099、LA-100 由 `MATHWIKI-LA-METHOD-014` 覆盖；LA-094 由 `MATHWIKI-LA-METHOD-011` 覆盖；LA-097 由 `MATHWIKI-LA-METHOD-014` 与 `MATHWIKI-LA-METHOD-016` 覆盖。
- 质量门：12 题均已运行 `intake_quality_gate.py --visual expected`，全部 `quality_gate=ok`；保留“无个人错因 / method_gap 未启用”的预期 WARN，不从标准解析反推用户本人错因。
- Tutor：安全输入包已经覆盖特征空间、幂零链、秩约束、向量组表示、方程组同解和零空间训练入口，本轮状态为 `verified_not_updated`，不复制完整题干或解析进入 Tutor。
- 边界：未修改正式错题卡，不运行 `wrongnet.py rebuild`，不修改回滚 JSON，不手改 `错题知识网络/生成/`；下一批从 LA-103、LA-104、LA-105、LA-109 及相邻题继续。

## [2026-07-03] maintenance | MAINT-040 线代相似理论视觉复核

- 范围：[LA-103](http://127.0.0.1:8765/open/LA-103)、[LA-104](http://127.0.0.1:8765/open/LA-104)、[LA-105](http://127.0.0.1:8765/open/LA-105)、[LA-106](http://127.0.0.1:8765/open/LA-106)、[LA-109](http://127.0.0.1:8765/open/LA-109)、[LA-110](http://127.0.0.1:8765/open/LA-110)、[LA-111](http://127.0.0.1:8765/open/LA-111)、[LA-112](http://127.0.0.1:8765/open/LA-112)、[LA-113](http://127.0.0.1:8765/open/LA-113)、[LA-114](http://127.0.0.1:8765/open/LA-114)、[LA-115](http://127.0.0.1:8765/open/LA-115)、[LA-116](http://127.0.0.1:8765/open/LA-116)。
- 核对：已核对 12 题正式卡、视觉详情、题图/解析图、缺解析图边界、方法页、Tutor 安全输入包和质量门结果。
- 写入：新增 `MATHWIKI-MAINT-040_线代相似理论视觉复核.md`；更新 `wiki/index.md`，登记相似理论后续段的视觉证据、方法页覆盖、资产边界和质量门结果。
- 复核结论：LA-103、LA-105、LA-109、LA-110、LA-111、LA-112、LA-113 由 `MATHWIKI-LA-METHOD-005` 覆盖；LA-104 由 `MATHWIKI-LA-METHOD-004` 与 `MATHWIKI-LA-METHOD-015` 覆盖；LA-106、LA-116 由 `MATHWIKI-LA-METHOD-012` 与 `MATHWIKI-LA-METHOD-005` 覆盖；LA-114、LA-115 由 `MATHWIKI-LA-METHOD-005` 与 `MATHWIKI-LA-METHOD-010` 覆盖。
- 资产边界：LA-106、LA-113 未检测到单独解析图，但视觉详情已用折叠解析文字补足，正式卡摘要一致；本轮只登记边界，不补造图片资产。
- 质量门：12 题均已运行 `intake_quality_gate.py --visual expected`，全部 `quality_gate=ok`；保留“无个人错因 / method_gap 未启用”的预期 WARN，不从标准解析反推用户本人错因。
- Tutor：安全输入包已经覆盖相似对角化、特征空间换基、几何重数、实对称正交对角化、谱投影、伴随矩阵和 \(AP=PB\) 训练入口，本轮状态为 `verified_not_updated`。
- 边界：未修改正式错题卡，不运行 `wrongnet.py rebuild`，不修改回滚 JSON，不手改 `错题知识网络/生成/`；下一批从 LA-117、LA-118、LA-119 及后续二次型/概率段继续。

## [2026-07-03] maintenance | MAINT-041 线代相似理论收尾与正交矩阵视觉复核

- 范围：[LA-117](http://127.0.0.1:8765/open/LA-117)、[LA-118](http://127.0.0.1:8765/open/LA-118)、[LA-119](http://127.0.0.1:8765/open/LA-119)。
- 技能读取：已按用户要求重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-ingest`、`llm-wiki-query`、`llm-wiki-lint`、`tutor`、`obsidian-cli`、`obsidian-markdown`，并按三层架构边界执行。
- 核对：已核对 3 题正式卡、视觉详情、题图/解析图、LA-118 缺单独解析图边界、方法页、Tutor 安全输入包和质量门结果。
- 写入：新增 `MATHWIKI-MAINT-041_线代相似理论收尾与正交矩阵视觉复核.md`；更新 `wiki/index.md`；修正 `LA-118_强化例题8.8（102152）` 视觉详情页的入库判断状态为 `already_in_wrongnet_enhanced` 并补 `quality_gate: ok`。
- 复核结论：LA-117 由“同特征值矩阵先比较 \(r(A-\lambda E)\)”覆盖；LA-118 由“多元递推先矩阵化，再用相似对角化求 \(A^n\alpha_0\)”覆盖；LA-119 由“正交矩阵 \(A^{-1}=A^{\mathsf T}\) 与单位行列约束联用”覆盖，均接入 `MATHWIKI-LA-METHOD-005`。
- 质量门：LA-117、LA-118、LA-119 均已运行 `intake_quality_gate.py --visual expected`，全部 `quality_gate=ok`；保留“无个人错因 / method_gap 未启用”的预期 WARN，不从标准解析反推用户本人错因。
- Tutor：安全输入包已有相似不变量、递推矩阵化和正交矩阵约束训练入口，本轮状态为 `verified_not_updated`，不复制完整题干或解析进入 Tutor。
- 边界：未修改正式错题卡，不运行 `wrongnet.py rebuild`，不修改回滚 JSON，不手改 `错题知识网络/生成/`；下一批继续进入后续二次型/概率段或按全量视觉审计剩余项推进。

## [2026-07-03] maintenance | MAINT-042 高数早期 method_gap 第一动作规范化

- 范围：[GS-005](http://127.0.0.1:8765/open/GS-005)、[GS-012](http://127.0.0.1:8765/open/GS-012)、[GS-015](http://127.0.0.1:8765/open/GS-015)、[GS-016](http://127.0.0.1:8765/open/GS-016)、[GS-017](http://127.0.0.1:8765/open/GS-017)、[GS-020](http://127.0.0.1:8765/open/GS-020)、[GS-022](http://127.0.0.1:8765/open/GS-022)、[GS-028](http://127.0.0.1:8765/open/GS-028)、[GS-030](http://127.0.0.1:8765/open/GS-030)、[GS-033](http://127.0.0.1:8765/open/GS-033)。
- 技能读取：已按用户要求重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-ingest`、`llm-wiki-query`、`llm-wiki-lint`、`tutor`、`obsidian-cli`、`obsidian-markdown`，并按三层架构边界执行。
- 写入：新增 `MATHWIKI-MAINT-042_高数早期method_gap第一动作规范化.md`；更新 10 张正式错题卡的 `method_gap.expected_first_action`、`missed_action`、`next_reminder`；同步 10 张可视化详情页的“正确第一步”和“复做提醒”；修正 `GS-012` 的 `|x|1` typo；补清 `GS-020`、`GS-028` 的占位错因。
- 复核结论：本批针对 `expected_first_action` 不可执行的 warning，把“普通型直接替换”“分别算左右极限”“有根式就有理化”等泛化模板替换为题目可直接执行的第一动作。
- 质量门：已运行 `wrongnet.py rebuild`，当前 `cards=770 strong=1918 medium=815 weak_audit=257`；10 题均运行 `intake_quality_gate.py --visual expected`，全部 `quality_gate=ok`，无 ERROR、无 WARN。
- 全量复审：728 个唯一正式视觉 ID，`clean=216`、`warning_only=512`、`fail=0`；目标 warning 从 162 降至 152。
- Tutor：本轮状态为 `verified_not_updated`；只把第一动作作为后续训练层边界，不启动 quiz，不把完整题干、解析或 Tutor 结果反写正式卡。
- 边界：未手改 `错题知识网络/生成/`，未修改回滚 JSON，未写掌握度。

## [2026-07-04] maintenance | MAINT-068 缺方法标签正式卡分流补强

- 范围：[GS-405](http://127.0.0.1:8765/open/GS-405)、[GS-408](http://127.0.0.1:8765/open/GS-408)、[GS-414](http://127.0.0.1:8765/open/GS-414)、[GS-426](http://127.0.0.1:8765/open/GS-426)、[GS-427](http://127.0.0.1:8765/open/GS-427)、[GS-428](http://127.0.0.1:8765/open/GS-428)、[GS-429](http://127.0.0.1:8765/open/GS-429)、[LA-005](http://127.0.0.1:8765/open/LA-005)、[LA-065](http://127.0.0.1:8765/open/LA-065)、[LA-080](http://127.0.0.1:8765/open/LA-080)、[LA-083](http://127.0.0.1:8765/open/LA-083)、[LA-084](http://127.0.0.1:8765/open/LA-084)、[LA-085](http://127.0.0.1:8765/open/LA-085)、[LA-086](http://127.0.0.1:8765/open/LA-086)、[LA-095](http://127.0.0.1:8765/open/LA-095)、[LA-096](http://127.0.0.1:8765/open/LA-096)。
- 技能读取：已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-ingest`、`llm-wiki-query`、`llm-wiki-lint`、`tutor`、`obsidian-cli`、`obsidian-markdown`，并按三层架构边界执行。
- 写入：16 张正式错题卡补证据边界字段，其中 13 张同步补 `methods` 标签；新增 `MATHWIKI-MAINT-068_缺方法标签正式卡分流补强.md`；更新 `wiki/index.md` 和 Tutor 安全输入包。
- 保留边界：GS-408、GS-414、LA-005 仍为综合待精分/OCR 待核对，保留 `缺方法标签`；所有 16 张均不补造个人错因、掌握度或 `method_gap`。
- 验证：`wrongnet.py rebuild` 已通过，cards=770、strong=1924、medium=814、weak_audit=246；source summaries=770/770；knowledge_clusters=406；method_clusters=1342；error_clusters=302；action_gap_clusters=9；coverage matrix 的 `missing_method` 从 16 降到 3；16 张卡 `intake_quality_gate.py --visual none` 均为 `quality_gate=ok`。
- 边界：未手改 `错题知识网络/生成/`，未修改回滚 JSON。

## [2026-07-04] maintenance | MAINT-069 旧批量卡必填字段证据边界收口

- 范围：[GS-048](http://127.0.0.1:8765/open/GS-048)、[GS-249](http://127.0.0.1:8765/open/GS-249)、[GS-341](http://127.0.0.1:8765/open/GS-341)、[GS-344](http://127.0.0.1:8765/open/GS-344)、[GS-349](http://127.0.0.1:8765/open/GS-349)、[GS-362](http://127.0.0.1:8765/open/GS-362)、[GS-369](http://127.0.0.1:8765/open/GS-369)、[GS-375](http://127.0.0.1:8765/open/GS-375)、[LA-006](http://127.0.0.1:8765/open/LA-006)、[LA-024](http://127.0.0.1:8765/open/LA-024)、[LA-027](http://127.0.0.1:8765/open/LA-027)、[LA-029](http://127.0.0.1:8765/open/LA-029)、[LA-051](http://127.0.0.1:8765/open/LA-051)、[LA-066](http://127.0.0.1:8765/open/LA-066)、[LA-076](http://127.0.0.1:8765/open/LA-076)、[LA-077](http://127.0.0.1:8765/open/LA-077)、[LA-101](http://127.0.0.1:8765/open/LA-101)、[LA-102](http://127.0.0.1:8765/open/LA-102)、[LA-107](http://127.0.0.1:8765/open/LA-107)、[LA-108](http://127.0.0.1:8765/open/LA-108)。
- 技能读取：已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-ingest`、`llm-wiki-query`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown`，并按三层架构边界执行。
- 写入：20 张正式错题卡补齐质量门必填字段；新增 `MATHWIKI-MAINT-069_旧批量卡必填字段证据边界收口.md`；更新 `wiki/index.md` 和 Tutor 安全输入包。
- 具体处理：GS-048 补标准答案；GS-249、GS-341、GS-344、GS-362、GS-369、GS-375、LA-027、LA-029、LA-051、LA-101、LA-102 补可复做入口；GS-349、LA-006、LA-024、LA-066、LA-076、LA-077、LA-107、LA-108 标明旧批量导入更像讲义总纲或答案字段缺证据。
- 保留边界：本批仍不补造用户个人错因、掌握度或 `method_gap`；同源重复候选暂不合并；视觉错连候选不作为正式证据。
- 验证：`wrongnet.py rebuild` 已通过，cards=770、strong=1915、medium=822、weak_audit=246；source summaries=770/770、compiled=770/770；knowledge_clusters=406；method_clusters=1342；error_clusters=302；action_gap_clusters=9；Obsidian bridge records=918、visual_records=876、formal_fallbacks=42、assets=1256；本批 20 张卡 `intake_quality_gate.py --visual none` 均为 `quality_gate=ok`、无 ERROR；全量 770 张正式卡必填字段缺失为 0；`git diff --check` 通过。
- 边界：未手改 `错题知识网络/生成/`，未修改回滚 JSON。

## [2026-07-04] maintenance | MAINT-070 早期高数视觉卡技能读取与方法补强

- 技能读取：已按用户提醒重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor`、`tutor-setup` 及 Tutor 集成规则，并按正式卡 / Wiki / Tutor 三层边界执行。
- 范围：[GS-003](http://127.0.0.1:8765/open/GS-003)、[GS-014](http://127.0.0.1:8765/open/GS-014)、[GS-053](http://127.0.0.1:8765/open/GS-053)、[GS-065](http://127.0.0.1:8765/open/GS-065)、[GS-072](http://127.0.0.1:8765/open/GS-072)。
- 核图：已查看 GS-003、GS-014、GS-053、GS-065、GS-072 的题图/解析图或折叠解析证据；GS-003、GS-014、GS-072 既有 Tutor 训练项有效，本轮只复核边界。
- 写入：新增 `MATHWIKI-MAINT-070_早期高数视觉卡技能读取与方法补强.md`；更新 `MATHWIKI-GS-METHOD-072_积分不等式证明入口链.md`、`MATHWIKI-GS-METHOD-019_压缩映射不动点迭代.md`、定积分总线、数列极限总线、`wiki/index.md` 和 Tutor 安全输入包。
- Tutor：新增 GS-053 积分型 Cauchy--Schwarz、GS-065 压缩映射平均迭代的安全训练项；不复制完整题干、完整解析或题图 OCR。
- 边界：本轮未修改正式错题卡，不运行 `wrongnet.py rebuild`；不从标准解析反推出用户个人错因、掌握度或正式 `method_gap`；未修改回滚 JSON，未手改 `错题知识网络/生成/`。

## [2026-07-04] maintenance | MAINT-071 早期高数第二批视觉卡方法补强

- 技能读取：已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown`，并按正式卡 / LLM Wiki / Tutor 安全输入三层边界执行。
- 范围：[GS-004](http://127.0.0.1:8765/open/GS-004)、[GS-045](http://127.0.0.1:8765/open/GS-045)、[GS-061](http://127.0.0.1:8765/open/GS-061)、[GS-068](http://127.0.0.1:8765/open/GS-068)、[GS-069](http://127.0.0.1:8765/open/GS-069)、[GS-075](http://127.0.0.1:8765/open/GS-075)。
- 核图：已查看 6 题正式卡、可视化详情和题图证据；均为已有正式卡，本轮目标是深度方法编译与 Tutor 安全训练补强。
- 写入：新增 `MATHWIKI-MAINT-071_早期高数第二批视觉卡方法补强.md`、`MATHWIKI-GS-METHOD-090_数列命题特值证伪与反证闭环.md`、`MATHWIKI-GS-METHOD-091_相邻和式根式差有理化.md`；更新 `MATHWIKI-GS-METHOD-072_积分不等式证明入口链.md`、`MATHWIKI-GS-METHOD-073_幂指极限对数化闭环.md`、`MATHWIKI-GS-METHOD-086_递推数列不变区间与单调有界闭环.md`、数列极限总线、定积分总线、`wiki/index.md` 和 Tutor 安全输入包。
- 正式卡修复：仅修复 [GS-075](http://127.0.0.1:8765/open/GS-075) 正式卡与视觉详情中的 `\right` 显示损坏；不改用户个人错因、掌握度或 `method_gap`。
- Tutor：新增 GS-004、GS-045、GS-061、GS-068、GS-069、GS-075 的安全训练入口；不复制完整题干、完整解析或题图 OCR。
- 验证：`wrongnet.py rebuild` 已通过，cards=770、strong=1915、medium=822、weak_audit=246；source summaries=770/770、compiled=770/770；knowledge_clusters=406；method_clusters=1342；error_clusters=302；action_gap_clusters=9；Obsidian bridge records=918、visual_records=876、assets=1256；本批 6 张卡 `intake_quality_gate.py --visual expected` 全部 `quality_gate=ok`；坏串检查和 `git diff --check` 均通过。
- 边界：旧批量卡缺用户本人作答过程时，不从标准解析反推出个人错因、掌握度或正式 `method_gap`；未修改回滚 JSON，未手改 `错题知识网络/生成/`。

## [2026-07-04] maintenance | MAINT-072 三角递推与局部展开视觉卡方法补强

- 技能读取：已重新读取 `kaoyan-math-wrong-intake`、`llm-wiki-ingest`、`llm-wiki-query`、`llm-wiki-lint`、`tutor`、`tutor-setup`、`obsidian-cli`、`obsidian-markdown`，并按正式卡 / LLM Wiki / Tutor 安全输入三层边界执行。
- 范围：[GS-076](http://127.0.0.1:8765/open/GS-076)、[GS-077](http://127.0.0.1:8765/open/GS-077)、[GS-078](http://127.0.0.1:8765/open/GS-078)、[GS-082](http://127.0.0.1:8765/open/GS-082)、[GS-083](http://127.0.0.1:8765/open/GS-083)、[GS-085](http://127.0.0.1:8765/open/GS-085)、[GS-088](http://127.0.0.1:8765/open/GS-088)、[GS-089](http://127.0.0.1:8765/open/GS-089)。
- 核图：已查看 8 题正式卡、可视化详情和题图；解析图均无单独图片，依据折叠解析文字和题图核对。
- 写入：新增 `MATHWIKI-MAINT-072_三角递推与局部展开视觉卡方法补强.md`、`MATHWIKI-GS-METHOD-092_三角隐式根与递推比阶入口链.md`、`MATHWIKI-GS-METHOD-093_局部展开对象与真实增量匹配.md`；更新极限与连续总线、一元函数微分学应用总线、数列极限总线、`MATHWIKI-GS-METHOD-013_导数定义差商入口.md`、`wiki/index.md` 和 Tutor 安全输入包。
- 正式卡/视觉修复：修复 GS-085、GS-088 正式卡题目摘要中 `\frac` 被控制字符破坏的问题；修复 GS-078 可视化详情折叠解析中余弦递推转化和后续分式符号方向。
- Tutor：新增 8 题安全训练入口；只保存触发词、第一动作和复做提醒，不复制完整题干、解析或题图 OCR。
- 验证：`wrongnet.py rebuild` 已通过，cards=770、strong=1915、medium=822、weak_audit=246；source summaries=770/770、compiled=770/770；knowledge_clusters=406；method_clusters=1342；error_clusters=302；action_gap_clusters=9；Obsidian bridge records=918、visual_records=876、assets=1256；本批 8 张卡 `intake_quality_gate.py --visual expected` 全部 `quality_gate=ok`；source summary 已挂新方法页；坏控制字符、旧符号残留、`git diff --check` 和 Obsidian CLI 搜索均通过。
- 边界：GS-077、GS-085、GS-088、GS-089 缺用户本人作答过程，不反推个人错因、掌握度或正式 `method_gap`；未修改回滚 JSON，未手改 `错题知识网络/生成/`。

## [2026-07-04] maintenance | MAINT-073 导数定义可导性视觉卡深度方法补强

- 技能读取：已按用户提醒重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，并按正式卡 / LLM Wiki / Tutor 安全输入三层边界执行。
- 范围：[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-091](http://127.0.0.1:8765/open/GS-091)、[GS-098](http://127.0.0.1:8765/open/GS-098)、[GS-101](http://127.0.0.1:8765/open/GS-101)、[GS-102](http://127.0.0.1:8765/open/GS-102)、[GS-103](http://127.0.0.1:8765/open/GS-103)、[GS-105](http://127.0.0.1:8765/open/GS-105)、[GS-106](http://127.0.0.1:8765/open/GS-106)、[GS-108](http://127.0.0.1:8765/open/GS-108)、[GS-109](http://127.0.0.1:8765/open/GS-109)。
- 写入：新增 `MATHWIKI-GS-METHOD-094_导数定义真实增量与补点求导链.md`、`MATHWIKI-GS-METHOD-095_可导性候选点与局部形态判别链.md`、`MATHWIKI-MAINT-073_导数定义可导性视觉卡深度方法补强.md`；更新一元微分总线、导数定义入口页、可视化详情 deep wiki / 方法页链接、`wiki/index.md` 和 Tutor 安全输入包。
- 正式卡修复：修复 GS-103 `\to` 控制字符损坏；修复 GS-108 复做提醒中 `$x\ne 0$` 被断行的问题。
- Tutor：新增 10 题安全训练入口；只保存触发词、第一动作和复做提醒，不复制完整题干、解析或题图 OCR。
- 验证：`wrongnet.py rebuild` 已通过，cards=770、strong=1915、medium=822、weak_audit=246；source summaries=770/770、compiled=770/770；knowledge_clusters=406；method_clusters=1342；error_clusters=302；action_gap_clusters=9；Obsidian bridge records=918、visual_records=876、assets=1256；本批 10 题 `intake_quality_gate.py --visual expected` 全部 `quality_gate=ok`；Obsidian CLI 能检索到 `MATHWIKI-GS-METHOD-094`、`MATHWIKI-GS-METHOD-095`、`MATHWIKI-MAINT-073`；`git diff --check` 和控制字符检查通过。
- 边界：GS-098、GS-101、GS-102、GS-105、GS-106、GS-108、GS-109 缺用户本人作答过程，不反推个人错因、掌握度或正式 `method_gap`；未修改回滚 JSON，未手改 `错题知识网络/生成/`。

## [2026-07-04] formal-intake | GS-659 57841 截面三角形体积

- 范围：[GS-659](http://127.0.0.1:8765/open/GS-659)、VIS-GS-659、MATHWIKI-GS-METHOD-096。
- 写入：新增正式错题卡 `GS-659_57841截面三角形体积.md`；复制用户题图与解析图到 `assets/visual_wrong_questions/GS-659/`；新增可视化详情页 `GS-659_57841截面三角形体积.md`，题图直接显示、解析默认折叠。
- 方法沉淀：新增 `MATHWIKI-GS-METHOD-096_截面面积积分求体积.md`，只保存“固定切片变量 -> 求底面线段 -> 写截面面积 -> 积分体积”的高层动作链，不复制完整题干或长解析。
- 错点：用户卡在“垂直于 \(x\) 轴”应理解为固定 \(x\) 切片，且没有把底面线段 \(0-(x^2-1)=1-x^2\) 识别为等边三角形边长；`method_gap` 标记为 B2-TRIGGER，关联方法卡 H10-007。
- Tutor：新增安全训练入口，只保存触发词、第一动作和复做提醒，不复制题图 OCR 或完整解析；推荐区域为 `高等数学主线` 与 `方法错因训练`。
- 验证：待运行 `intake_closeout.py --id GS-659 --source 57841 --visual expected` 完成 wrongnet rebuild、wiki coverage、bridge refresh、related/knowledge 查询和质量门。
- 边界：不手改 `错题知识网络/生成/`；不修改回滚 JSON；掌握度为 AI评分 3/5，依据用户连续追问中的卡点和最终理解情况。

## [2026-07-04] formal-intake | GS-660 170675 原函数存在性判断

- 范围：[GS-660](http://127.0.0.1:8765/open/GS-660)、VIS-GS-660、MATHWIKI-GS-METHOD-097。
- 写入：新增正式错题卡 `GS-660_170675原函数存在性判断.md`；复制用户题图与解析图到 `assets/visual_wrong_questions/GS-660/`；新增可视化详情页 `GS-660_170675原函数存在性判断.md`，题图直接显示、解析默认折叠。
- 方法沉淀：新增 `MATHWIKI-GS-METHOD-097_原函数存在性与连续可导链.md`，只保存“原函数定义 -> 可导必连续 -> 连续函数存在原函数 -> 构造 \((F+\Phi)'\)”的高层动作链，不复制完整题干或长解析。
- 错点：用户已能写出 \(F'=f\)，但没有继续推出 \(F\) 可导、\(F\) 连续，再由连续函数存在原函数构造 \(\Phi'=F\)；同时混淆 C 的“存在原函数”和 D 的“存在奇函数原函数”。
- Tutor：新增安全训练入口，只保存触发词、第一动作和复做提醒，不复制题图 OCR 或完整解析；推荐区域为 `高等数学主线` 与 `方法错因训练`。
- 验证：`intake_closeout.py --id GS-660 --source 170675 --visual expected` 已通过；wrongnet rebuild 后 cards=772，bridge records=920、visual_records=878、assets=1260；related 强关联 GS-572/GS-574/GS-583；`quality_gate=ok`。
- 边界：不手改 `错题知识网络/生成/`；不修改回滚 JSON；掌握度待评分，未替用户写入 0-5 分。

## [2026-07-04] formal-intake | GS-661 193707 变上限积分二阶可导

- 范围：[GS-661](http://127.0.0.1:8765/open/GS-661)、VIS-GS-661、MATHWIKI-GS-METHOD-098。
- 写入：新增正式错题卡 `GS-661_193707变上限积分二阶可导.md`；复制用户题图与解析图到 `assets/visual_wrong_questions/GS-661/`；新增可视化详情页 `GS-661_193707变上限积分二阶可导.md`，题图直接显示、解析默认折叠。
- 方法沉淀：新增 `MATHWIKI-GS-METHOD-098_极限函数分段与变上限二阶可导链.md`，只保存“极限函数先分段 -> \(f\) 连续则 \(F'=f\) -> 查 \(f\) 的分段点左右导数”的高层动作链，不复制完整题干或长解析。
- 错点：用户没有先把 \(f(x)=\lim_{n\to\infty}\ln(e^n+x^n)/n\) 按 \(1\le x\le e\) 与 \(x>e\) 分段化；也没有主动调用微积分基本定理，由 \(F'=f\) 转入 \(F\) 二阶可导性判断。`method_gap` 标记为 B4-CHAIN，关联方法卡 H01-001、H03-005、H09-008。
- Tutor：新增安全训练入口，只保存触发词、第一动作和复做提醒，不复制题图 OCR 或完整解析；推荐区域为 `高等数学主线` 与 `方法错因训练`。
- 验证：`intake_closeout.py --id GS-661 --source 193707 --visual expected` 已通过；wrongnet rebuild 后 cards=773，bridge records=921、visual_records=879、assets=1262；related 强关联 GS-083/GS-091/GS-096/GS-283/GS-290/GS-331/GS-440/GS-443；`quality_gate=ok`。
- 边界：不手改 `错题知识网络/生成/`；不修改回滚 JSON；掌握度为 AI评分 2/5，依据用户明确描述的分段触发和变上限积分求导定理缺口。

## [2026-07-04] formal-intake | GS-662 57909 复合三角积分比较

- 范围：[GS-662](http://127.0.0.1:8765/open/GS-662)、VIS-GS-662、MATHWIKI-GS-METHOD-099。
- 写入：新增正式错题卡 `GS-662_57909复合三角积分比较.md`；复制用户题图与解析图到 `assets/visual_wrong_questions/GS-662/`；新增可视化详情页 `GS-662_57909复合三角积分比较.md`，题图直接显示、解析默认折叠。
- 方法沉淀：新增 `MATHWIKI-GS-METHOD-099_复合三角积分中间量比较链.md`，只保存“复合函数积分比较 -> 找熟悉中间量 -> 点态比较 -> 积分保序”的高层动作链，不复制完整题干或长解析。
- 错点：用户知道 \(x>\sin x\) 以及 \(\sin x,\cos x\) 的单调性，但没有在 \(\sin(\sin x)\)、\(\cos(\sin x)\) 的积分比较中触发“引入 \(x\)”这个中间量；做题时被 \(\sin x=t\)、\(x=\arcsin t\) 的换元路径锁住。`method_gap` 标记为 B2-TRIGGER，方法卡暂待匹配。
- Tutor：新增安全训练入口，只保存触发词、第一动作和复做提醒，不复制题图 OCR 或完整解析；推荐区域为 `高等数学主线` 与 `方法错因训练`。
- 验证：`intake_closeout.py --id GS-662 --source 57909 --visual expected` 已通过；wrongnet rebuild 后 cards=774，bridge records=922、visual_records=880、assets=1264；related 强关联 GS-231/GS-289/GS-326/GS-331/GS-445/GS-575/GS-577/GS-578；`quality_gate=ok`，无 ERROR/WARN。
- 边界：不手改 `错题知识网络/生成/`；不修改回滚 JSON；掌握度为 AI评分 3/5，依据用户明确描述的知识已知但中间量比较触发失败。

## [2026-07-04] formal-intake | GS-663 81436 定积分比较作差反折

- 范围：[GS-663](http://127.0.0.1:8765/open/GS-663)、VIS-GS-663、MATHWIKI-GS-METHOD-100。
- 写入：新增正式错题卡 `GS-663_81436定积分比较作差反折.md`；复制用户题图与解析图到 `assets/visual_wrong_questions/GS-663/`；新增可视化详情页 `GS-663_81436定积分比较作差反折.md`，题图直接显示、解析默认折叠。
- 方法沉淀：新增 `MATHWIKI-GS-METHOD-100_定积分比较作差反折链.md`，只保存“多个定积分排序 -> 先分组 -> 同正分子比分母反向 -> 同分母交叉作差 -> 分段反折统一区间”的高层动作链，不复制完整题干或长解析。
- 错点：用户能想到被积函数比较和作差，但没有把 \(I_1-I_2\) 真正作差处理；比较 \(I_2,I_3\) 时忘记分母越大分式越小；反折换元中把 \(\frac\pi2-\frac\pi4=\frac\pi4\) 写成 \(-\frac\pi4\)。`method_gap` 标记为 B7-CALC，关联方法卡 H08-006。
- Tutor：新增安全训练入口，只保存触发词、第一动作和复做提醒，不复制题图 OCR 或完整解析；推荐区域为 `高等数学主线` 与 `方法错因训练`。
- 验证：`intake_closeout.py --id GS-663 --source 81436 --visual expected` 已通过；wrongnet rebuild 后 cards=775，bridge records=923、visual_records=881、assets=1266；related 强关联 GS-634/GS-231/GS-288/GS-289/GS-290/GS-292/GS-618/GS-619；`quality_gate=ok`，无 ERROR/WARN。
- 边界：不手改 `错题知识网络/生成/`；不修改回滚 JSON；掌握度为 AI评分 4/5，依据用户明确描述的入口基本想到但计算与方向复核不稳。

## [2026-07-04] formal-intake | GS-664 170728 凹函数弦线积分均值

- 范围：[GS-664](http://127.0.0.1:8765/open/GS-664)、VIS-GS-664、MATHWIKI-GS-METHOD-101。
- 写入：新增正式错题卡 `GS-664_170728凹函数弦线积分均值.md`；复制用户题图与解析图到 `assets/visual_wrong_questions/GS-664/`；新增可视化详情页 `GS-664_170728凹函数弦线积分均值.md`，题图直接显示、解析默认折叠。
- 方法沉淀：新增 `MATHWIKI-GS-METHOD-101_凹函数弦线积分均值比较链.md`，只保存“\(F'=f>0\)、\(F''=f'<0\) -> 递增凹函数 -> 端点弦线 \(y=xF(1)\) -> 积分面积比较”的高层动作链，不复制完整题干或长解析。
- 错点：用户能构造 \(g(x)=F(x)-2\int_0^1F(t)\,dt\) 并求 \(g'(x)>0\)，但把全区间积分常数在 \(x=0\) 处误消成 0；更关键的是没有从 \(F'\)、\(F''\) 的符号触发凹函数弦线图像比较。`method_gap` 标记为 B2-TRIGGER，关联方法卡 H06-001。
- Tutor：新增安全训练入口，只保存触发词、第一动作和复做提醒，不复制完整题干、解析或题图 OCR；推荐区域为 `高等数学主线` 与 `方法错因训练`。
- 验证：`intake_closeout.py --id GS-664 --source 170728 --visual expected` 已通过；wrongnet rebuild 后 cards=776，bridge records=924、visual_records=882、assets=1268；related 强关联 GS-183/GS-231/GS-578/GS-052/GS-138/GS-140/GS-141/GS-221；`quality_gate=ok`，无 ERROR/WARN。
- 边界：不手改 `错题知识网络/生成/`；不修改回滚 JSON；掌握度待评分，未替用户写入 0-5 分。

## [2026-07-04] formal-intake | GS-665 170733 凸函数加权积分比较

- 范围：[GS-665](http://127.0.0.1:8765/open/GS-665)、VIS-GS-665、MATHWIKI-GS-METHOD-072。
- 写入：新增正式错题卡 `GS-665_170733凸函数加权积分比较.md`；复制用户题图与解析图到 `assets/visual_wrong_questions/GS-665/`；新增可视化详情页 `GS-665_170733凸函数加权积分比较.md`，题图直接显示、解析默认折叠。
- 方法沉淀：更新 `MATHWIKI-GS-METHOD-072_积分不等式证明入口链.md`，补入“选项积分线性组合比较 -> 移项成差值 -> 固定上限变量化 -> 二阶导判正”的高层动作链；同步一元函数微分应用总线、定积分总线、wiki 索引与 Tutor 安全输入包。
- 错点：用户能想到 \(f''>0\) 触发凸函数弦线比较，也尝试用 Taylor/点态不等式，但路线过绕；关键断点是没有先把候选 B 移项为 \(\int_0^a xf-\frac23a\int_0^a f>0\)，再构造 \(F(t)\) 并用 \(F''>0\to F'>0\to F>0\) 收口。`method_gap` 标记为 B3-METHOD，关联方法卡 H11-007。
- Tutor：新增安全训练入口，只保存触发词、第一动作和复做提醒，不复制完整题干、解析或题图 OCR；推荐区域为 `高等数学主线` 与 `方法错因训练`。
- 验证：`intake_closeout.py --id GS-665 --source 170733 --visual expected` 已通过；wrongnet rebuild 后 cards=777，bridge records=925、visual_records=883、assets=1270；related 强关联 GS-237/GS-247/GS-578/GS-640/GS-641/GS-664/GS-231/GS-248；`quality_gate=ok`，无 ERROR/WARN。
- 边界：不手改 `错题知识网络/生成/`；不修改回滚 JSON；掌握度待评分，未替用户写入 0-5 分。

## [2026-07-04] maintenance | MATHWIKI-MAINT-077 第0轮质量扩量轮次报告

- input: 用户要求继续当前长期目标，并明确指出必须读取并应用 skill，质量提升不能停留在查看层。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian Markdown`、`Obsidian CLI`；按数学错题系统边界执行。
- rule_updated: `AI维护规则.md`、`录入模板.md` 已落地手工精卡“正确入口”规则；schema 已加入 index/log 检索式访问。
- archive_updated: 长期目标存档为 `MATHWIKI-GOAL-001`；`wiki/log_archive/2026-06.md` 归档 46 个 6 月 log 区块；三个历史导入报告/目录已移入 `批量导入/已处理/`。
- candidate_ledger: 新增 `MATHWIKI-QUESTIONS-004_测试题候选台账.md`，首批登记 30 条候选/重连/来源保留记录；当前 manifest 883 条，候选积压 143。
- metrics: N1 quality_gate checked=777 fail_count=0 warn_count=393；N3 related 待补充=342；N4 缺视觉映射=41；N6 非标准状态=2；N8 PR 正式卡=1。
- validation: `wrongnet.py rebuild` 成功，cards=777，strong=1935，medium=826，weak_audit=246；wiki coverage refresh 成功；bridge refresh 成功，records=925，visual_records=883，assets=1270；Obsidian CLI 可检索到 `MATHWIKI-QUESTIONS-004` 和 `MATHWIKI-GOAL-001`。
- boundary: 本轮没有修改正式错题卡、回滚 JSON 或 Tutor 结果；只运行脚本刷新派生 `生成/` 内容，不手工编辑 `生成/`。

## [2026-07-04] maintenance | MATHWIKI-MAINT-078 第1轮状态与强边质量扩量报告

- input: 用户指出必须读取 LLM Wiki Lint 与 Tutor 技能，并要求错题质量提升不能停留在查看层。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 32 张正式卡去除 `status` 引号变体；[GS-443](http://127.0.0.1:8765/open/GS-443)、[GS-458](http://127.0.0.1:8765/open/GS-458) 从非标准掌握状态规范为 `待复做` 并保留掌握度 4/5 证据；10 张多元函数微分学卡补齐 manual 强边 `related`。
- candidate_ledger: `MATHWIKI-QUESTIONS-004` 追加 CAND-0031 至 CAND-0035，均为已并入正式卡的来源保留记录；台账累计登记 35 条，剩余未登记 108 条。
- metrics: N1 quality_gate checked=777 fail_count=0 warn_card_count=393 warn_count=707；N3 related 待补充=332；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 和 bridge snapshot 已刷新；Obsidian CLI 可检索到 `MATHWIKI-QUESTIONS-004` 与 `GS-358`；`git diff --check` 通过。
- boundary: 未修改回滚 JSON；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-079 第2轮强边与候选台账扩量报告

- input: 用户提醒必须读取相关 skill，并要求错题质量提升落实到文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 15 张早期高数正式卡补齐 reciprocal manual 强边 `related`：[GS-005](http://127.0.0.1:8765/open/GS-005)、[GS-008](http://127.0.0.1:8765/open/GS-008)、[GS-009](http://127.0.0.1:8765/open/GS-009)、[GS-014](http://127.0.0.1:8765/open/GS-014)、[GS-020](http://127.0.0.1:8765/open/GS-020)、[GS-024](http://127.0.0.1:8765/open/GS-024)、[GS-026](http://127.0.0.1:8765/open/GS-026)、[GS-028](http://127.0.0.1:8765/open/GS-028)、[GS-031](http://127.0.0.1:8765/open/GS-031)、[GS-033](http://127.0.0.1:8765/open/GS-033)、[GS-037](http://127.0.0.1:8765/open/GS-037)、[GS-038](http://127.0.0.1:8765/open/GS-038)、[GS-041](http://127.0.0.1:8765/open/GS-041)、[GS-047](http://127.0.0.1:8765/open/GS-047)、[GS-054](http://127.0.0.1:8765/open/GS-054)。
- candidate_ledger: `MATHWIKI-QUESTIONS-004` 追加 CAND-0036 至 CAND-0045，均为已并入正式卡的来源保留记录；台账累计登记 45 条，其中来源保留 30 条，剩余来源保留 98 条。
- metrics: N1 quality_gate checked=777 fail_count=0 warn_card_count=393 warn_count=707；N3 related 待补充=317；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 和 bridge snapshot 已刷新；全库质量门 ERROR 0；Obsidian CLI 收尾检索待完成；不启动 Tutor quiz。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-080 第3轮强边与候选台账扩量报告

- input: 用户要求必须读取 LLM Wiki Lint 与 Tutor 等 skill，并继续把错题质量提升落实到文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 15 张早期高数正式卡补齐 reciprocal manual 强边 `related`：[GS-061](http://127.0.0.1:8765/open/GS-061)、[GS-064](http://127.0.0.1:8765/open/GS-064)、[GS-066](http://127.0.0.1:8765/open/GS-066)、[GS-071](http://127.0.0.1:8765/open/GS-071)、[GS-078](http://127.0.0.1:8765/open/GS-078)、[GS-081](http://127.0.0.1:8765/open/GS-081)、[GS-082](http://127.0.0.1:8765/open/GS-082)、[GS-086](http://127.0.0.1:8765/open/GS-086)、[GS-096](http://127.0.0.1:8765/open/GS-096)、[GS-097](http://127.0.0.1:8765/open/GS-097)、[GS-098](http://127.0.0.1:8765/open/GS-098)、[GS-103](http://127.0.0.1:8765/open/GS-103)、[GS-106](http://127.0.0.1:8765/open/GS-106)、[GS-108](http://127.0.0.1:8765/open/GS-108)、[GS-120](http://127.0.0.1:8765/open/GS-120)。
- candidate_ledger: `MATHWIKI-QUESTIONS-004` 追加 CAND-0046 至 CAND-0055，均为已并入正式卡的来源保留记录；台账累计登记 55 条，其中来源保留 40 条，剩余来源保留 88 条。
- metrics: N1 quality_gate checked=777 fail_count=0 warn_card_count=393 warn_count=707；N3 related 待补充=302；XLSX related 待补充=277；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 和 bridge snapshot 已刷新；全库质量门 ERROR 0；生成 `/tmp/kaoyan_math_full_quality_gate_round3_strict.json`。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-081 第4轮强边与候选台账扩量报告

- input: 用户提醒必须读取相关 skill，并要求错题质量提升必须落实到正式文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 15 张正式卡补齐 reciprocal manual 强边 `related`：[GS-134](http://127.0.0.1:8765/open/GS-134)、[GS-136](http://127.0.0.1:8765/open/GS-136)、[GS-138](http://127.0.0.1:8765/open/GS-138)、[GS-140](http://127.0.0.1:8765/open/GS-140)、[GS-141](http://127.0.0.1:8765/open/GS-141)、[GS-151](http://127.0.0.1:8765/open/GS-151)、[GS-154](http://127.0.0.1:8765/open/GS-154)、[GS-160](http://127.0.0.1:8765/open/GS-160)、[GS-165](http://127.0.0.1:8765/open/GS-165)、[GS-166](http://127.0.0.1:8765/open/GS-166)、[GS-174](http://127.0.0.1:8765/open/GS-174)、[GS-175](http://127.0.0.1:8765/open/GS-175)、[GS-187](http://127.0.0.1:8765/open/GS-187)、[GS-190](http://127.0.0.1:8765/open/GS-190)、[GS-200](http://127.0.0.1:8765/open/GS-200)。
- candidate_ledger: `MATHWIKI-QUESTIONS-004` 追加 CAND-0056 至 CAND-0065，均为已并入正式卡的来源保留记录；台账累计登记 65 条，其中来源保留 50 条，剩余来源保留 78 条。
- metrics: N1 quality_gate checked=777 fail_count=0 warn_card_count=393 warn_count=707；N3 related 待补充=287；XLSX related 待补充=262；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 和 bridge snapshot 已刷新；全库质量门 ERROR 0；生成 `/tmp/kaoyan_math_full_quality_gate_round4_strict.json`；`git diff --check` 通过。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-082 第5轮强边与候选台账扩量报告

- input: 用户要求必须读取相关 skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 15 张正式卡补齐 reciprocal manual 强边 `related`：[GS-214](http://127.0.0.1:8765/open/GS-214)、[GS-216](http://127.0.0.1:8765/open/GS-216)、[GS-217](http://127.0.0.1:8765/open/GS-217)、[GS-219](http://127.0.0.1:8765/open/GS-219)、[GS-225](http://127.0.0.1:8765/open/GS-225)、[GS-231](http://127.0.0.1:8765/open/GS-231)、[GS-246](http://127.0.0.1:8765/open/GS-246)、[GS-252](http://127.0.0.1:8765/open/GS-252)、[GS-260](http://127.0.0.1:8765/open/GS-260)、[GS-261](http://127.0.0.1:8765/open/GS-261)、[GS-269](http://127.0.0.1:8765/open/GS-269)、[GS-272](http://127.0.0.1:8765/open/GS-272)、[GS-293](http://127.0.0.1:8765/open/GS-293)、[GS-294](http://127.0.0.1:8765/open/GS-294)、[GS-309](http://127.0.0.1:8765/open/GS-309)。
- candidate_ledger: `MATHWIKI-QUESTIONS-004` 追加 CAND-0066 至 CAND-0075，均为已并入正式卡的来源保留记录；台账累计登记 75 条，其中来源保留 60 条，剩余来源保留 68 条。
- metrics: N1 quality_gate checked=777 fail_count=0 warn_card_count=393 warn_count=707；N3 related 待补充=272；XLSX related 待补充=247；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；全库质量门 `checked=777 fail_count=0 warn_card_count=393 warn_count=707`，生成 `/tmp/kaoyan_math_full_quality_gate_round5_strict.json`；Obsidian CLI 可检索 `MATHWIKI-MAINT-082`、`CAND-0075`、`GS-214`；`git diff --check` 通过。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-083 第6轮强边与候选台账扩量报告

- input: 用户要求必须读取相关 skill，尤其是 `LLM Wiki Lint` 与 `Tutor`，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 15 张正式卡补齐 reciprocal manual 强边 `related`：[GS-314](http://127.0.0.1:8765/open/GS-314)、[GS-317](http://127.0.0.1:8765/open/GS-317)、[GS-320](http://127.0.0.1:8765/open/GS-320)、[GS-325](http://127.0.0.1:8765/open/GS-325)、[GS-326](http://127.0.0.1:8765/open/GS-326)、[GS-338](http://127.0.0.1:8765/open/GS-338)、[GS-341](http://127.0.0.1:8765/open/GS-341)、[GS-343](http://127.0.0.1:8765/open/GS-343)、[GS-344](http://127.0.0.1:8765/open/GS-344)、[GS-349](http://127.0.0.1:8765/open/GS-349)、[GS-397](http://127.0.0.1:8765/open/GS-397)、[GS-399](http://127.0.0.1:8765/open/GS-399)、[GS-405](http://127.0.0.1:8765/open/GS-405)、[GS-431](http://127.0.0.1:8765/open/GS-431)、[GS-434](http://127.0.0.1:8765/open/GS-434)。
- candidate_ledger: `MATHWIKI-QUESTIONS-004` 追加 CAND-0076 至 CAND-0085，均为已并入正式卡的来源保留记录；台账累计登记 85 条，其中来源保留 70 条，剩余来源保留 58 条。
- metrics: N1 quality_gate checked=777 fail_count=0 warn_card_count=393 warn_count=707；N3 当前源文件可复现口径为 `related` 空占位 264，其中明面 `待补充` 247、空列表 17，复做队列内 230；XLSX 空占位 245，复做队列内 222；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；全库质量门 `checked=777 fail_count=0 warn_card_count=393 warn_count=707`，生成 `/tmp/kaoyan_math_full_quality_gate_round6_strict.json`。`build_wrong_card_source_summaries.py` 第一次与方法簇重建并行时遇到瞬时缺页，单独重跑后通过；Obsidian CLI 可检索 `MATHWIKI-MAINT-083`、`CAND-0085`、`GS-314`；`git diff --check` 通过。
- tutor: 本轮只补 `related` 与候选来源台账，没有新增可训练的概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-085 第8轮暂无强边收口与候选台账扩量报告

- input: 用户提醒必须读取相关 skill，并要求错题质量提升要落实到文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`，并读取 math intake workflow 与 Tutor 集成细则。
- formal_cards_updated: 10 张待复做正式卡经 `wrong_questions.json` 复核没有任何强关联边，因此把 `related` 从 `待补充` 收口为 `暂无强边`：[GS-002](http://127.0.0.1:8765/open/GS-002)、[GS-004](http://127.0.0.1:8765/open/GS-004)、[GS-006](http://127.0.0.1:8765/open/GS-006)、[GS-036](http://127.0.0.1:8765/open/GS-036)、[GS-045](http://127.0.0.1:8765/open/GS-045)、[GS-046](http://127.0.0.1:8765/open/GS-046)、[GS-048](http://127.0.0.1:8765/open/GS-048)、[GS-050](http://127.0.0.1:8765/open/GS-050)、[GS-053](http://127.0.0.1:8765/open/GS-053)、[GS-069](http://127.0.0.1:8765/open/GS-069)。
- candidate_ledger: `MATHWIKI-QUESTIONS-004` 追加 CAND-0096 至 CAND-0105，均为已并入正式卡的来源保留记录；台账累计登记 105 条，其中来源保留 90 条，剩余来源保留 38 条。
- metrics: N1 quality_gate checked=777 fail_count=0 warn_card_count=393 warn_count=707；N3 `related: 待补充` 从 247 降到 237，`暂无强边` 10；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；全库质量门生成 `/tmp/kaoyan_math_full_quality_gate_round8_strict.json`。
- tutor: 本轮只做 `related` 占位收口与候选来源台账，没有新增可训练的概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-089 第12轮强边纠偏与来源台账收尾报告

- input: 用户提醒必须读取相关 skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`，并读取 math intake workflow、Tutor 集成细则与输出模板。
- formal_cards_updated: 30 张正式卡；其中 10 张纠偏为真实强关联：[GS-001](http://127.0.0.1:8765/open/GS-001)、[GS-007](http://127.0.0.1:8765/open/GS-007)、[GS-010](http://127.0.0.1:8765/open/GS-010)、[GS-011](http://127.0.0.1:8765/open/GS-011)、[GS-012](http://127.0.0.1:8765/open/GS-012)、[GS-013](http://127.0.0.1:8765/open/GS-013)、[GS-019](http://127.0.0.1:8765/open/GS-019)、[GS-021](http://127.0.0.1:8765/open/GS-021)、[GS-023](http://127.0.0.1:8765/open/GS-023)、[GS-029](http://127.0.0.1:8765/open/GS-029)；另 20 张当前无强关联证据，从 `待补充` 收口为 `暂无强边`：[GS-228](http://127.0.0.1:8765/open/GS-228)、[GS-235](http://127.0.0.1:8765/open/GS-235)、[GS-242](http://127.0.0.1:8765/open/GS-242)、[GS-264](http://127.0.0.1:8765/open/GS-264)、[GS-265](http://127.0.0.1:8765/open/GS-265)、[GS-273](http://127.0.0.1:8765/open/GS-273)、[GS-279](http://127.0.0.1:8765/open/GS-279)、[GS-296](http://127.0.0.1:8765/open/GS-296)、[GS-297](http://127.0.0.1:8765/open/GS-297)、[GS-298](http://127.0.0.1:8765/open/GS-298)、[GS-299](http://127.0.0.1:8765/open/GS-299)、[GS-300](http://127.0.0.1:8765/open/GS-300)、[GS-303](http://127.0.0.1:8765/open/GS-303)、[GS-304](http://127.0.0.1:8765/open/GS-304)、[GS-305](http://127.0.0.1:8765/open/GS-305)、[GS-306](http://127.0.0.1:8765/open/GS-306)、[GS-313](http://127.0.0.1:8765/open/GS-313)、[GS-315](http://127.0.0.1:8765/open/GS-315)、[GS-319](http://127.0.0.1:8765/open/GS-319)、[GS-323](http://127.0.0.1:8765/open/GS-323)；并修正 GS-323 frontmatter `wrong_point` 中 `f''` 应为 `f'` 的笔误。
- correction: M088 的 `暂无强边` 结论已加后续更正，原因是上一轮未读取 `wrong_questions.json` 顶层 `similarities[].level=强关联`。
- candidate_ledger: 复核 `MATHWIKI-QUESTIONS-004` 已登记到 CAND-0143；台账累计 143 条，其中来源保留 128 条，`already_in_wrongnet_source_retained` 剩余未登记 0 条；本轮未重复追加。
- metrics: N1 quality_gate checked=777 error_cards=0 warn_cards=397 error_items=0 warn_items=748；N3 `related: 待补充` 从 207 降到 187，`暂无强边` 从 40 增到 50，已填 `related` 从 514 增到 524，空列表 16；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；全库质量门生成 `/tmp/kaoyan_math_full_quality_gate_round12_after_correction.json`。
- tutor: 本轮只做 `related` 强边纠偏、暂无强边收口与候选来源台账复核，没有新增可训练的概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-084 第7轮强边与候选台账扩量报告

- input: 用户要求必须读取相关 skill，尤其是 `LLM Wiki Lint` 与 `Tutor`，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 10 张正式卡补齐 reciprocal manual 强边 `related`：[GS-480](http://127.0.0.1:8765/open/GS-480)、[GS-486](http://127.0.0.1:8765/open/GS-486)、[GS-493](http://127.0.0.1:8765/open/GS-493)、[GS-527](http://127.0.0.1:8765/open/GS-527)、[GS-594](http://127.0.0.1:8765/open/GS-594)、[LA-019](http://127.0.0.1:8765/open/LA-019)、[LA-051](http://127.0.0.1:8765/open/LA-051)、[LA-086](http://127.0.0.1:8765/open/LA-086)、[LA-101](http://127.0.0.1:8765/open/LA-101)、[LA-102](http://127.0.0.1:8765/open/LA-102)。
- candidate_ledger: `MATHWIKI-QUESTIONS-004` 追加 CAND-0086 至 CAND-0095，均为已并入正式卡的来源保留记录；台账累计登记 95 条，其中来源保留 80 条，剩余来源保留 48 条。
- metrics: N1 quality_gate checked=777 fail_count=0 warn_card_count=393 warn_count=707；N3 `related: 待补充` 从 257 降到 247；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；全库质量门生成 `/tmp/kaoyan_math_full_quality_gate_round7_strict.json`。
- tutor: 本轮只补 `related` 与候选来源台账，没有新增可训练的概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-086 第9轮空列表强边补强报告

- input: 用户提醒必须读取相关 skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 1 张正式卡补齐 reciprocal manual 强边 `related`：[GS-425](http://127.0.0.1:8765/open/GS-425) 从空列表改为 `GS-424`、`LA-042`、`LA-043`、`LA-044`。
- candidate_ledger: 复核 `MATHWIKI-QUESTIONS-004` 已登记至 CAND-0105；台账累计 105 条，其中来源保留 90 条，剩余来源保留 38 条。
- metrics: N1 quality_gate checked=777 fail_count=0 warn_card_count=393 warn_count=707；源文件逐行口径 N3 related 空占位 253，其中 `待补充` 237、空列表 16；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；单卡质量门 `GS-425 quality_gate=ok`；全库质量门生成 `/tmp/kaoyan_math_full_quality_gate_round8_strict.json`。
- tutor: 本轮只补 `related`，没有新增可训练的概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-087 第10轮暂无强边收口与候选台账扩量报告

- input: 用户提醒必须读取相关 skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`，并读取 math intake workflow 与 Tutor 集成细则。
- formal_cards_updated: 10 张待复做正式卡经 `wrong_questions.json` 复核没有任何强关联边，因此把 `related` 从 `待补充` 收口为 `暂无强边`：[GS-077](http://127.0.0.1:8765/open/GS-077)、[GS-085](http://127.0.0.1:8765/open/GS-085)、[GS-088](http://127.0.0.1:8765/open/GS-088)、[GS-089](http://127.0.0.1:8765/open/GS-089)、[GS-101](http://127.0.0.1:8765/open/GS-101)、[GS-102](http://127.0.0.1:8765/open/GS-102)、[GS-105](http://127.0.0.1:8765/open/GS-105)、[GS-109](http://127.0.0.1:8765/open/GS-109)、[GS-110](http://127.0.0.1:8765/open/GS-110)、[GS-111](http://127.0.0.1:8765/open/GS-111)。
- candidate_ledger: `MATHWIKI-QUESTIONS-004` 追加 CAND-0106 至 CAND-0115，均为已并入正式卡的来源保留记录；台账累计登记 115 条，其中来源保留 100 条，剩余来源保留 28 条。
- metrics: N1 quality_gate checked=777 fail_count=0 warn_card_count=393 warn_count=707；N3 `related: 待补充` 从 237 降到 227，`暂无强边` 从 10 增到 20，空列表 16；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；全库质量门生成 `/tmp/kaoyan_math_full_quality_gate_round10_strict.json`。
- tutor: 本轮只做 `related` 占位收口与候选来源台账，没有新增可训练的概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-088 第11轮暂无强边收口与候选台账扩量报告

- input: 用户提醒必须读取相关 skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`，并读取 math intake workflow、Tutor 集成细则与输出模板。
- formal_cards_updated: 10 张待复做正式卡经 `wrong_questions.json` 复核没有任何强关联边，因此把 `related` 从 `待补充` 收口为 `暂无强边`：[GS-001](http://127.0.0.1:8765/open/GS-001)、[GS-007](http://127.0.0.1:8765/open/GS-007)、[GS-010](http://127.0.0.1:8765/open/GS-010)、[GS-011](http://127.0.0.1:8765/open/GS-011)、[GS-012](http://127.0.0.1:8765/open/GS-012)、[GS-013](http://127.0.0.1:8765/open/GS-013)、[GS-019](http://127.0.0.1:8765/open/GS-019)、[GS-021](http://127.0.0.1:8765/open/GS-021)、[GS-023](http://127.0.0.1:8765/open/GS-023)、[GS-029](http://127.0.0.1:8765/open/GS-029)。
- candidate_ledger: `MATHWIKI-QUESTIONS-004` 追加 CAND-0116 至 CAND-0125，均为已并入正式卡的来源保留记录；台账累计登记 125 条，其中来源保留 110 条，剩余来源保留 18 条。
- metrics: N1 quality_gate checked=777 error_cards=0 warn_cards=0；N3 `related: 待补充` 从 227 降到 217，`暂无强边` 从 20 增到 30，空列表 16；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；全库质量门生成 `/tmp/kaoyan_math_full_quality_gate_round11_strict.json`；Obsidian CLI 可检索 `CAND-0125`、`GS-001`、`暂无强边`；`git diff --check` 通过。
- tutor: 本轮只做 `related` 占位收口与候选来源台账，没有新增可训练的概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-090 第13轮强边补全与扩量边界报告

- input: 用户提醒必须读取相关 skill，并要求错题质量提升落实到文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`、`Obsidian Markdown`，并读取项目目标、README、AI维护规则、录入模板、schema 与上一轮报告。
- formal_cards_updated: 15 张正式卡补齐真实强关联 `related`：[GS-030](http://127.0.0.1:8765/open/GS-030)、[GS-044](http://127.0.0.1:8765/open/GS-044)、[GS-051](http://127.0.0.1:8765/open/GS-051)、[GS-052](http://127.0.0.1:8765/open/GS-052)、[GS-055](http://127.0.0.1:8765/open/GS-055)、[GS-058](http://127.0.0.1:8765/open/GS-058)、[GS-060](http://127.0.0.1:8765/open/GS-060)、[GS-062](http://127.0.0.1:8765/open/GS-062)、[GS-065](http://127.0.0.1:8765/open/GS-065)、[GS-067](http://127.0.0.1:8765/open/GS-067)、[GS-068](http://127.0.0.1:8765/open/GS-068)、[GS-074](http://127.0.0.1:8765/open/GS-074)、[GS-075](http://127.0.0.1:8765/open/GS-075)、[GS-076](http://127.0.0.1:8765/open/GS-076)、[GS-083](http://127.0.0.1:8765/open/GS-083)。
- candidate_ledger: 复核 `MATHWIKI-QUESTIONS-004` 已登记 143 条；剩余 10 条待正式判断与 5 条人工重连缺用户确认，本轮不硬推进、不建假正式卡。
- metrics: N1 full quality gate checked=777 error_cards=0 warn_cards=397 error_items=0 warn_items=748；N3 生成索引口径 `related: 待补充`=152、已填 related=559、`暂无强边`=50、空列表=16；bridge formal_fallbacks=42；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；本轮 15 张卡逐张质量门全部 `quality_gate=ok`；全库质量门生成 `/tmp/kaoyan_math_full_quality_gate_round13_project_parser.json`。
- tutor: 本轮只补 `related` 强边，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-091 第14轮强边回填与质量门复核报告

- input: 用户再次提醒必须读取相关 skill，并要求错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 20 张正式卡依据当前 `wrong_questions.json` 顶层 `similarities[].level=强关联` 回填 `related`：[GS-345](http://127.0.0.1:8765/open/GS-345)、[GS-287](http://127.0.0.1:8765/open/GS-287)、[GS-283](http://127.0.0.1:8765/open/GS-283)、[GS-248](http://127.0.0.1:8765/open/GS-248)、[GS-226](http://127.0.0.1:8765/open/GS-226)、[GS-157](http://127.0.0.1:8765/open/GS-157)、[GS-094](http://127.0.0.1:8765/open/GS-094)、[GS-336](http://127.0.0.1:8765/open/GS-336)、[GS-332](http://127.0.0.1:8765/open/GS-332)、[GS-215](http://127.0.0.1:8765/open/GS-215)、[GS-178](http://127.0.0.1:8765/open/GS-178)、[GS-117](http://127.0.0.1:8765/open/GS-117)、[GS-112](http://127.0.0.1:8765/open/GS-112)、[GS-347](http://127.0.0.1:8765/open/GS-347)、[GS-528](http://127.0.0.1:8765/open/GS-528)、[GS-114](http://127.0.0.1:8765/open/GS-114)、[GS-328](http://127.0.0.1:8765/open/GS-328)、[GS-146](http://127.0.0.1:8765/open/GS-146)、[GS-249](http://127.0.0.1:8765/open/GS-249)、[GS-359](http://127.0.0.1:8765/open/GS-359)。
- candidate_ledger: 本轮未新增候选或推进状态；剩余 10 条待正式判断和 5 条待人工重连均需要用户错因确认或人工重连证据，不为配额伪造状态。
- metrics: N1 quality_gate checked=777 error_cards=0 warn_cards=397 error_items=0 warn_items=748；N3 `related: 待补充` 从本轮核对口径 172 降到 152；剩余待补中 94 张仍有强关联证据，58 张当前无强边证据；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；20 张本批单卡质量门 `fail_count=0`；全库质量门结果 `/tmp/kaoyan_math_full_quality_gate_round13_after_related.json`；`git diff --check` 通过。
- tutor: 本轮只做 `related` 强边回填，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-098 第21轮暂无强边收口与质量门复核报告

- input: 用户要求读取相关 skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 20 张当前无强边证据的正式卡把 `related` 从 `待补充` 收口为 `暂无强边`：[GS-286](http://127.0.0.1:8765/open/GS-286)、[GS-291](http://127.0.0.1:8765/open/GS-291)、[GS-318](http://127.0.0.1:8765/open/GS-318)、[GS-327](http://127.0.0.1:8765/open/GS-327)、[GS-329](http://127.0.0.1:8765/open/GS-329)、[GS-330](http://127.0.0.1:8765/open/GS-330)、[GS-339](http://127.0.0.1:8765/open/GS-339)、[GS-342](http://127.0.0.1:8765/open/GS-342)、[GS-352](http://127.0.0.1:8765/open/GS-352)、[GS-353](http://127.0.0.1:8765/open/GS-353)、[GS-367](http://127.0.0.1:8765/open/GS-367)、[GS-384](http://127.0.0.1:8765/open/GS-384)、[GS-408](http://127.0.0.1:8765/open/GS-408)、[GS-414](http://127.0.0.1:8765/open/GS-414)、[GS-432](http://127.0.0.1:8765/open/GS-432)、[GS-433](http://127.0.0.1:8765/open/GS-433)、[GS-436](http://127.0.0.1:8765/open/GS-436)、[GS-478](http://127.0.0.1:8765/open/GS-478)、[GS-479](http://127.0.0.1:8765/open/GS-479)、[GS-482](http://127.0.0.1:8765/open/GS-482)。
- metrics: N1 全库质量门 `checked=777 failed=0 warn_cards=397 warn_items=748`；N3 `related: 待补充` 从 38 降到 18，且有强边证据的待补卡保持 0；`暂无强边` 从 70 增到 90，空列表 16，已填 related 653。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=827 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；本轮 20 张单卡质量门 `checked=20 failed=0 error_items=0 warn_cards=13 warn_items=30`；全库质量门 `checked=777 failed=0 error_items=0 warn_cards=397 warn_items=748`。
- tutor: 本轮只做 `related` 占位收口，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-099 第22轮显式待补清零与质量门复核报告

- input: 用户要求读取相关 skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 18 张当前无强边证据的正式卡把 `related` 从 `待补充` 收口为 `暂无强边`：[GS-483](http://127.0.0.1:8765/open/GS-483)、[GS-485](http://127.0.0.1:8765/open/GS-485)、[GS-487](http://127.0.0.1:8765/open/GS-487)、[GS-495](http://127.0.0.1:8765/open/GS-495)、[GS-496](http://127.0.0.1:8765/open/GS-496)、[GS-663](http://127.0.0.1:8765/open/GS-663)、[LA-002](http://127.0.0.1:8765/open/LA-002)、[LA-004](http://127.0.0.1:8765/open/LA-004)、[LA-005](http://127.0.0.1:8765/open/LA-005)、[LA-011](http://127.0.0.1:8765/open/LA-011)、[LA-017](http://127.0.0.1:8765/open/LA-017)、[LA-024](http://127.0.0.1:8765/open/LA-024)、[LA-027](http://127.0.0.1:8765/open/LA-027)、[LA-065](http://127.0.0.1:8765/open/LA-065)、[LA-066](http://127.0.0.1:8765/open/LA-066)、[LA-095](http://127.0.0.1:8765/open/LA-095)、[LA-096](http://127.0.0.1:8765/open/LA-096)、[PR-001](http://127.0.0.1:8765/open/PR-001)。
- metrics: N1 全库质量门 `checked=777 failed=0 error_items=0 warn_cards=397 warn_items=748`；N3 `related: 待补充` 从 18 降到 0，显式待补清零；`暂无强边` 从 90 增到 108，空列表 16，已填 related 653。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=827 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；本轮 18 张单卡质量门 `checked=18 failed=0 error_items=0 warn_cards=12 warn_items=35`；全库质量门 `checked=777 failed=0 error_items=0 warn_cards=397 warn_items=748`。
- tutor: 本轮只做 `related` 占位收口，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-100 第23轮空列表强边回填与质量门复核报告

- input: 用户要求读取相关 skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 16 张 `related: []` 空列表正式卡依据当前强边证据回填 `related`：[GS-659](http://127.0.0.1:8765/open/GS-659)、[LA-007](http://127.0.0.1:8765/open/LA-007)、[LA-008](http://127.0.0.1:8765/open/LA-008)、[LA-013](http://127.0.0.1:8765/open/LA-013)、[LA-014](http://127.0.0.1:8765/open/LA-014)、[LA-015](http://127.0.0.1:8765/open/LA-015)、[LA-016](http://127.0.0.1:8765/open/LA-016)、[LA-018](http://127.0.0.1:8765/open/LA-018)、[LA-022](http://127.0.0.1:8765/open/LA-022)、[LA-023](http://127.0.0.1:8765/open/LA-023)、[LA-025](http://127.0.0.1:8765/open/LA-025)、[LA-026](http://127.0.0.1:8765/open/LA-026)、[LA-028](http://127.0.0.1:8765/open/LA-028)、[LA-032](http://127.0.0.1:8765/open/LA-032)、[LA-036](http://127.0.0.1:8765/open/LA-036)、[LA-047](http://127.0.0.1:8765/open/LA-047)。
- metrics: N1 全库质量门 `checked=777 failed=0 error_items=0 warn_cards=397 warn_items=748`；N3 显式 `related: 待补充=0` 且空列表从 16 降到 0；真实 related 669，`暂无强边` 108。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=827 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；本轮 16 张单卡质量门 `checked=16 failed=0 error_items=0 warn_cards=0 warn_items=0`；全库质量门 `checked=777 failed=0 error_items=0 warn_cards=397 warn_items=748`。
- tutor: 本轮只做 `related` 强边回填，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-097 第20轮暂无强边收口与质量门复核报告

- input: 用户要求读取相关 skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 20 张当前无强边证据的正式卡把 `related` 从 `待补充` 收口为 `暂无强边`：[GS-015](http://127.0.0.1:8765/open/GS-015)、[GS-016](http://127.0.0.1:8765/open/GS-016)、[GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-027](http://127.0.0.1:8765/open/GS-027)、[GS-039](http://127.0.0.1:8765/open/GS-039)、[GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-056](http://127.0.0.1:8765/open/GS-056)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-092](http://127.0.0.1:8765/open/GS-092)、[GS-107](http://127.0.0.1:8765/open/GS-107)、[GS-118](http://127.0.0.1:8765/open/GS-118)、[GS-119](http://127.0.0.1:8765/open/GS-119)、[GS-125](http://127.0.0.1:8765/open/GS-125)、[GS-135](http://127.0.0.1:8765/open/GS-135)、[GS-152](http://127.0.0.1:8765/open/GS-152)、[GS-224](http://127.0.0.1:8765/open/GS-224)、[GS-232](http://127.0.0.1:8765/open/GS-232)、[GS-243](http://127.0.0.1:8765/open/GS-243)、[GS-251](http://127.0.0.1:8765/open/GS-251)、[GS-281](http://127.0.0.1:8765/open/GS-281)。
- metrics: N1 全库质量门 `checked=777 failed=0 warn_cards=0 warn_items=0`；N3 `related: 待补充` 从 58 降到 38，仍有强边证据的待补卡保持 0；`暂无强边` 从 50 增到 70，空列表 16，已填 related 653。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=827 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；本轮 20 张单卡质量门 `checked=20 failed=0 warn_items=0`；全库质量门 `checked=777 failed=0 warn_cards=0 warn_items=0`；`git diff --check` 通过。
- tutor: 本轮只做 `related` 占位收口，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-095 第18轮强边回填与质量门复核报告

- input: 继续长期目标 `Math-WrongNet-QualityScale`，按当前工作树继续推进质量线。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`。
- formal_cards_updated: 20 张正式卡回填 `related`：[GS-271](http://127.0.0.1:8765/open/GS-271)、[GS-274](http://127.0.0.1:8765/open/GS-274)、[GS-275](http://127.0.0.1:8765/open/GS-275)、[GS-276](http://127.0.0.1:8765/open/GS-276)、[GS-277](http://127.0.0.1:8765/open/GS-277)、[GS-282](http://127.0.0.1:8765/open/GS-282)、[GS-284](http://127.0.0.1:8765/open/GS-284)、[GS-285](http://127.0.0.1:8765/open/GS-285)、[GS-295](http://127.0.0.1:8765/open/GS-295)、[GS-321](http://127.0.0.1:8765/open/GS-321)、[GS-324](http://127.0.0.1:8765/open/GS-324)、[GS-333](http://127.0.0.1:8765/open/GS-333)、[GS-334](http://127.0.0.1:8765/open/GS-334)、[GS-335](http://127.0.0.1:8765/open/GS-335)、[GS-340](http://127.0.0.1:8765/open/GS-340)、[GS-346](http://127.0.0.1:8765/open/GS-346)、[GS-348](http://127.0.0.1:8765/open/GS-348)、[GS-351](http://127.0.0.1:8765/open/GS-351)、[GS-355](http://127.0.0.1:8765/open/GS-355)、[GS-357](http://127.0.0.1:8765/open/GS-357)。
- metrics: N1 全库质量门 `checked=777 failed=0 warning_count=0`；N3 `related: 待补充` 从 97 降到 77，其中仍有强边证据 19，当前无强边证据 58；N4 `formal_fallbacks=42`；N5 待正式判断 10、待人工重连 5；N8 概率论正式卡 1。
- expansion: 候选台账本轮未推进；剩余候选缺用户错因或人工重连证据，不为配额伪造状态。
- spot_check: 已掌握抽测建议为 [GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-022](http://127.0.0.1:8765/open/GS-022)、[GS-025](http://127.0.0.1:8765/open/GS-025)、[GS-015](http://127.0.0.1:8765/open/GS-015)、[GS-016](http://127.0.0.1:8765/open/GS-016)。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=827 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；本轮 20 张单卡质量门 `checked=20 failed=0`；全库质量门 `checked=777 failed=0 warning_count=0`；`git diff --check` 通过。
- tutor: 本轮只做 `related` 强边回填，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-093 第16轮强边回填与质量门复核报告

- input: 用户再次提醒必须读取相关 skill，并要求错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`。
- formal_cards_updated: 20 张正式卡回填 `related`：[GS-365](http://127.0.0.1:8765/open/GS-365)、[GS-361](http://127.0.0.1:8765/open/GS-361)、[GS-337](http://127.0.0.1:8765/open/GS-337)、[GS-322](http://127.0.0.1:8765/open/GS-322)、[GS-227](http://127.0.0.1:8765/open/GS-227)、[GS-223](http://127.0.0.1:8765/open/GS-223)、[GS-180](http://127.0.0.1:8765/open/GS-180)、[LA-085](http://127.0.0.1:8765/open/LA-085)、[LA-084](http://127.0.0.1:8765/open/LA-084)、[LA-083](http://127.0.0.1:8765/open/LA-083)、[LA-080](http://127.0.0.1:8765/open/LA-080)、[LA-077](http://127.0.0.1:8765/open/LA-077)、[LA-076](http://127.0.0.1:8765/open/LA-076)、[GS-429](http://127.0.0.1:8765/open/GS-429)、[GS-428](http://127.0.0.1:8765/open/GS-428)、[GS-427](http://127.0.0.1:8765/open/GS-427)、[GS-426](http://127.0.0.1:8765/open/GS-426)、[GS-388](http://127.0.0.1:8765/open/GS-388)、[GS-381](http://127.0.0.1:8765/open/GS-381)、[GS-375](http://127.0.0.1:8765/open/GS-375)。
- metrics: 正式卡 `related: 待补充` 从 137 降到 117；其中 59 张仍有强边证据，58 张当前无强边证据，空列表 16，`暂无强边` 50；status 分布未手工改动。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；20 张本批单卡质量门 `checked=20 failed=0`；全库质量门 `checked=777 failed=0 warning_count=0`；结果见 `/tmp/kaoyan_math_round16_batch20_quality_gate.json` 与 `/tmp/kaoyan_math_full_quality_gate_round16_after_related.json`。
- tutor: 本轮只做 `related` 强边回填，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-114 旧批量卡method_gap与error_causes第十批证据边界补强报告

- input: 用户要求必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-253](http://127.0.0.1:8765/open/GS-253)、[GS-256](http://127.0.0.1:8765/open/GS-256)、[GS-273](http://127.0.0.1:8765/open/GS-273)、[GS-279](http://127.0.0.1:8765/open/GS-279)、[GS-293](http://127.0.0.1:8765/open/GS-293)、[GS-294](http://127.0.0.1:8765/open/GS-294)、[GS-295](http://127.0.0.1:8765/open/GS-295)、[GS-296](http://127.0.0.1:8765/open/GS-296)、[GS-297](http://127.0.0.1:8765/open/GS-297)、[GS-298](http://127.0.0.1:8765/open/GS-298)。
- metrics: N1 全库质量门从 M113 `warn_cards=307 warn_items=577` 降到 M114 `warn_cards=297 warn_items=557`；`error_cards=0 error_items=0`；剩余主要 WARN 为 `method_gap not enabled=282`、`error_causes is placeholder or empty=213`、`visual gap record has no asset mapping by design=41`。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=827 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=755、knowledge_clusters=412、method_clusters=1358、error_clusters=410、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m114_full_quality_gate_details.json`。
- expansion: 候选台账本轮未推进；GS-281 因已掌握边界未混入普通低置信旧批量补强，建议后续单独复核。
- tutor: 已检查数学 LLM Wiki Tutor 安全输入包与 dashboard；本轮方法信号已被既有安全输入包覆盖，Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-092 第15轮强边回填与质量门复核报告

- input: 用户再次提醒必须读取相关 skill，并要求错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`。
- formal_cards_updated: 15 张正式卡依据当前 `wrong_questions.json` 顶层 `similarities[].level=强关联` 回填 `related`：[GS-084](http://127.0.0.1:8765/open/GS-084)、[GS-113](http://127.0.0.1:8765/open/GS-113)、[GS-116](http://127.0.0.1:8765/open/GS-116)、[GS-126](http://127.0.0.1:8765/open/GS-126)、[GS-131](http://127.0.0.1:8765/open/GS-131)、[GS-155](http://127.0.0.1:8765/open/GS-155)、[GS-156](http://127.0.0.1:8765/open/GS-156)、[GS-159](http://127.0.0.1:8765/open/GS-159)、[GS-161](http://127.0.0.1:8765/open/GS-161)、[GS-171](http://127.0.0.1:8765/open/GS-171)、[GS-172](http://127.0.0.1:8765/open/GS-172)、[GS-173](http://127.0.0.1:8765/open/GS-173)、[GS-176](http://127.0.0.1:8765/open/GS-176)、[GS-177](http://127.0.0.1:8765/open/GS-177)、[GS-179](http://127.0.0.1:8765/open/GS-179)。
- metrics: N1 quality_gate checked=777 error_cards=0 warn_cards=397 error_items=0 warn_items=748；N3 已填 `related` 从 609 增到 624，仍有强边证据的 `related: 待补充` 从 94 降到 79，当前无强边证据 58，空列表 16；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；本轮 15 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_full_quality_gate_round15_project_parser.json`。
- tutor: 本轮只做 `related` 强边回填，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-094 第17轮强边回填与质量门复核报告

- input: 用户要求必须读取相关 skill，并要求错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 20 张正式卡回填 `related`：[GS-181](http://127.0.0.1:8765/open/GS-181)、[GS-182](http://127.0.0.1:8765/open/GS-182)、[GS-184](http://127.0.0.1:8765/open/GS-184)、[GS-188](http://127.0.0.1:8765/open/GS-188)、[GS-189](http://127.0.0.1:8765/open/GS-189)、[GS-191](http://127.0.0.1:8765/open/GS-191)、[GS-209](http://127.0.0.1:8765/open/GS-209)、[GS-220](http://127.0.0.1:8765/open/GS-220)、[GS-229](http://127.0.0.1:8765/open/GS-229)、[GS-230](http://127.0.0.1:8765/open/GS-230)、[GS-239](http://127.0.0.1:8765/open/GS-239)、[GS-240](http://127.0.0.1:8765/open/GS-240)、[GS-241](http://127.0.0.1:8765/open/GS-241)、[GS-244](http://127.0.0.1:8765/open/GS-244)、[GS-245](http://127.0.0.1:8765/open/GS-245)、[GS-250](http://127.0.0.1:8765/open/GS-250)、[GS-254](http://127.0.0.1:8765/open/GS-254)、[GS-255](http://127.0.0.1:8765/open/GS-255)、[GS-259](http://127.0.0.1:8765/open/GS-259)、[GS-267](http://127.0.0.1:8765/open/GS-267)。
- metrics: `related: 待补充` 从 117 降到 97；其中 39 张仍有强边证据，58 张当前无强边证据；`暂无强边` 50，空列表 16；status 分布为 待复做 711、已掌握 65、待人工重连 1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1935 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；20 张本批单卡质量门 `failed=0`；全库质量门 `checked=777 failed=0 warn_cards=397 warn_items=748`；`git diff --check` 通过。
- tutor: 本轮只做 `related` 强边回填，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-096 第19轮强边证据清零与质量门复核报告

- input: 用户提醒必须读取相关 skill，并要求错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Tutor Setup`、`Obsidian CLI`、`Obsidian Markdown`；按数学错题系统边界执行。
- formal_cards_updated: 19 张正式卡依据当前 `wrong_questions.json` 顶层 `similarities[].level=强关联` 回填 `related`：[GS-362](http://127.0.0.1:8765/open/GS-362)、[GS-368](http://127.0.0.1:8765/open/GS-368)、[GS-369](http://127.0.0.1:8765/open/GS-369)、[GS-370](http://127.0.0.1:8765/open/GS-370)、[GS-371](http://127.0.0.1:8765/open/GS-371)、[GS-372](http://127.0.0.1:8765/open/GS-372)、[GS-378](http://127.0.0.1:8765/open/GS-378)、[GS-383](http://127.0.0.1:8765/open/GS-383)、[GS-430](http://127.0.0.1:8765/open/GS-430)、[GS-435](http://127.0.0.1:8765/open/GS-435)、[GS-526](http://127.0.0.1:8765/open/GS-526)、[GS-661](http://127.0.0.1:8765/open/GS-661)、[GS-662](http://127.0.0.1:8765/open/GS-662)、[LA-001](http://127.0.0.1:8765/open/LA-001)、[LA-006](http://127.0.0.1:8765/open/LA-006)、[LA-012](http://127.0.0.1:8765/open/LA-012)、[LA-029](http://127.0.0.1:8765/open/LA-029)、[LA-107](http://127.0.0.1:8765/open/LA-107)、[LA-108](http://127.0.0.1:8765/open/LA-108)。
- metrics: N1 全库质量门 `checked=777 failed=0 warn_cards=397 warn_items=748`；N3 `related: 待补充` 从 77 降到 58，且有强边证据的待补卡从 19 清零；剩余 58 张当前无强边证据，另有空列表 16、`暂无强边` 50、已填 related 653。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=827 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=753、knowledge_clusters=412、method_clusters=1358、error_clusters=310、action_gap_clusters=9；bridge snapshot records=925、visual_records=883、formal_fallbacks=42、assets=1270；本轮 19 张单卡质量门 `checked=19 failed=0 warn_items=23`；全库质量门 `checked=777 failed=0 warn_cards=397 warn_items=748`。
- tutor: 本轮只做 `related` 强边回填，没有新增可训练概念、方法、触发词或错因模式；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-107 旧批量卡method_gap与error_causes第三批证据边界补强报告

- input: 用户要求必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-055](http://127.0.0.1:8765/open/GS-055)、[GS-061](http://127.0.0.1:8765/open/GS-061)、[GS-062](http://127.0.0.1:8765/open/GS-062)、[GS-065](http://127.0.0.1:8765/open/GS-065)、[GS-068](http://127.0.0.1:8765/open/GS-068)、[GS-069](http://127.0.0.1:8765/open/GS-069)、[GS-070](http://127.0.0.1:8765/open/GS-070)、[GS-072](http://127.0.0.1:8765/open/GS-072)、[GS-075](http://127.0.0.1:8765/open/GS-075)、[GS-077](http://127.0.0.1:8765/open/GS-077)。
- metrics: N1 全库质量门从 M106 `warn_cards=375 warn_items=717` 降到 M107 `warn_cards=365 warn_items=697`；N3 当前 `related` 为 filled=669、暂无强边=108；N5 剩余 10 条待正式判断和 5 条人工重连仍缺用户确认；N6 状态分布为 待复做 712、已掌握 65；N8 ID 前缀分布为 GS=657、LA=119、PR=1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=828 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=754、knowledge_clusters=412、method_clusters=1358、error_clusters=340、action_gap_clusters=9；本轮 10 张单卡质量门 `checked=10 failed=0 warn_items=0`；全库质量门 `checked=777 failed=0 error_items=0 warn_cards=365 warn_items=697`。
- expansion: 候选台账本轮未推进；剩余候选缺用户本人错因或人工重连确认，不为配额伪造状态。
- spot_check: 已掌握抽测建议为 [GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-318](http://127.0.0.1:8765/open/GS-318)、[GS-441](http://127.0.0.1:8765/open/GS-441)。
- tutor: 本轮只做正式卡高层入口与证据边界补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-116 旧批量卡method_gap与error_causes第十二批质量扩量轮次报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-311](http://127.0.0.1:8765/open/GS-311)、[GS-313](http://127.0.0.1:8765/open/GS-313)、[GS-314](http://127.0.0.1:8765/open/GS-314)、[GS-315](http://127.0.0.1:8765/open/GS-315)、[GS-319](http://127.0.0.1:8765/open/GS-319)、[GS-320](http://127.0.0.1:8765/open/GS-320)、[GS-321](http://127.0.0.1:8765/open/GS-321)、[GS-322](http://127.0.0.1:8765/open/GS-322)、[GS-323](http://127.0.0.1:8765/open/GS-323)、[GS-324](http://127.0.0.1:8765/open/GS-324)。
- metrics: N1 全库质量门从 M115 `warn_cards=287 warn_items=537` 降到 M116 `warn_cards=277 warn_items=517`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 272 降至 262；`error_causes placeholder/empty` 从 203 降至 193。
- validation: `wrongnet.py rebuild` 成功；wiki coverage、source summaries、Obsidian bridge 已刷新；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m116_full_quality_gate_details.json`。
- expansion: 候选台账本轮未推进；剩余 10 条待正式判断和 5 条人工重连项仍缺用户本人错因、题目定位或人工确认，不为配额伪造状态。
- spot_check: 已掌握抽测建议沿用 [GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-318](http://127.0.0.1:8765/open/GS-318)、[GS-441](http://127.0.0.1:8765/open/GS-441)。
- tutor: Tutor 技能已读取；本轮只做正式卡高层入口与证据边界补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-115 旧批量卡method_gap与error_causes第十一批质量扩量轮次报告

- input: 用户要求必须读取相关 skill，并强调错题质量提升必须落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取数学项目规则、schema、method_gap schema、方法卡、候选台账和相关方法页。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-299](http://127.0.0.1:8765/open/GS-299)、[GS-300](http://127.0.0.1:8765/open/GS-300)、[GS-301](http://127.0.0.1:8765/open/GS-301)、[GS-302](http://127.0.0.1:8765/open/GS-302)、[GS-303](http://127.0.0.1:8765/open/GS-303)、[GS-304](http://127.0.0.1:8765/open/GS-304)、[GS-305](http://127.0.0.1:8765/open/GS-305)、[GS-306](http://127.0.0.1:8765/open/GS-306)、[GS-307](http://127.0.0.1:8765/open/GS-307)、[GS-310](http://127.0.0.1:8765/open/GS-310)。
- metrics: N1 全库质量门从 M114 `warn_cards=297 warn_items=557` 降到 M115 `warn_cards=287 warn_items=537`；`method_gap not enabled=272`、`error_causes is placeholder or empty=203`；N3 当前 `related` 为 filled=682、暂无强边=95；N5 候选台账仍为待正式判断 10、待人工重连 5，缺用户本人错因/确认，不为配额伪造状态；N6 状态分布为 待复做 712、已掌握 65。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1968 medium=794 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=755、knowledge_clusters=412、method_clusters=1358、error_clusters=410、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m115_full_quality_gate_details.json`。
- spot_check: 已掌握抽测池保留时间信息：[GS-018](http://127.0.0.1:8765/open/GS-018) 最近 2026-03-11（已做1遍：2026-03-11）；[GS-042](http://127.0.0.1:8765/open/GS-042) 时间未记录（次数未记录）；[GS-090](http://127.0.0.1:8765/open/GS-090) 最近 2026-05-07（已做1遍：2026-05-07）；[GS-318](http://127.0.0.1:8765/open/GS-318) 时间未记录（次数未记录）；[GS-441](http://127.0.0.1:8765/open/GS-441) 最近 2026-05-11（已做1遍：2026-05-11）。
- tutor: 本轮只做正式卡高层入口与证据边界补强，没有新增安全训练包；已有安全输入覆盖尖峰核、绝对三角周期积分、高阶导奇偶周期、弧长链和旋转体/曲面链；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-112 旧批量卡method_gap与error_causes第八批证据边界补强报告

- input: 用户提醒必须读取相关 skill，并要求把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`、`fast-path.md`。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-213](http://127.0.0.1:8765/open/GS-213)、[GS-218](http://127.0.0.1:8765/open/GS-218)、[GS-226](http://127.0.0.1:8765/open/GS-226)、[GS-227](http://127.0.0.1:8765/open/GS-227)、[GS-228](http://127.0.0.1:8765/open/GS-228)、[GS-229](http://127.0.0.1:8765/open/GS-229)、[GS-230](http://127.0.0.1:8765/open/GS-230)、[GS-234](http://127.0.0.1:8765/open/GS-234)、[GS-235](http://127.0.0.1:8765/open/GS-235)、[GS-236](http://127.0.0.1:8765/open/GS-236)。其中 GS-229、GS-234、GS-236 同步修正 frontmatter 答案字段中的导数阶数笔误。
- metrics: N1 全库质量门从 M111 `warn_cards=326 warn_items=617` 降到 M112 `warn_cards=316 warn_items=597`；`error_cards=0 error_items=0`；剩余主要 WARN 为 `method_gap not enabled=302`、`error_causes is placeholder or empty=233`、`visual gap record has no asset mapping by design=41`。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=755、knowledge_clusters=412、method_clusters=1358、error_clusters=390、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m112_full_quality_gate_details.json`。
- expansion: 候选台账本轮未推进；剩余候选缺用户本人错因、题目定位或人工重连确认，不为配额伪造状态。
- spot_check: 已掌握抽测建议为 [GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-318](http://127.0.0.1:8765/open/GS-318)、[GS-441](http://127.0.0.1:8765/open/GS-441)。
- tutor: 本轮只做正式卡高层入口、证据边界和答案字段笔误修正，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-113 旧批量卡method_gap与error_causes第九批证据边界补强报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并要求继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`、`fast-path.md`。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-237](http://127.0.0.1:8765/open/GS-237)、[GS-239](http://127.0.0.1:8765/open/GS-239)、[GS-240](http://127.0.0.1:8765/open/GS-240)、[GS-241](http://127.0.0.1:8765/open/GS-241)、[GS-242](http://127.0.0.1:8765/open/GS-242)、[GS-244](http://127.0.0.1:8765/open/GS-244)、[GS-245](http://127.0.0.1:8765/open/GS-245)、[GS-246](http://127.0.0.1:8765/open/GS-246)、[GS-247](http://127.0.0.1:8765/open/GS-247)、[GS-249](http://127.0.0.1:8765/open/GS-249)。其中 GS-246 同步修正 frontmatter 答案字段中的导数阶数笔误；GS-249 保留题图/OCR 待补边界。
- metrics: N1 全库质量门从 M112 `warn_cards=316 warn_items=597` 降到 M113 `warn_cards=307 warn_items=577`；`error_cards=0 error_items=0`；剩余主要 WARN 为 `method_gap not enabled=292`、`error_causes is placeholder or empty=223`、`visual gap record has no asset mapping by design=41`。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=755、knowledge_clusters=412、method_clusters=1358、error_clusters=400、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`，其中 GS-249 保留设计内视觉缺图 WARN；全库质量门结果 `/tmp/kaoyan_math_m113_full_quality_gate_details.json`。
- expansion: 候选台账本轮未推进；剩余候选缺用户本人错因、题目定位或人工重连确认，不为配额伪造状态。
- spot_check: 已掌握抽测建议沿用 [GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-318](http://127.0.0.1:8765/open/GS-318)、[GS-441](http://127.0.0.1:8765/open/GS-441)。
- tutor: 本轮只做正式卡高层入口、证据边界和答案字段笔误修正，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-108 旧批量卡method_gap与error_causes第四批证据边界补强报告

- input: 用户要求必须读取相关 skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-085](http://127.0.0.1:8765/open/GS-085)、[GS-087](http://127.0.0.1:8765/open/GS-087)、[GS-088](http://127.0.0.1:8765/open/GS-088)、[GS-089](http://127.0.0.1:8765/open/GS-089)、[GS-097](http://127.0.0.1:8765/open/GS-097)、[GS-098](http://127.0.0.1:8765/open/GS-098)、[GS-099](http://127.0.0.1:8765/open/GS-099)、[GS-101](http://127.0.0.1:8765/open/GS-101)、[GS-102](http://127.0.0.1:8765/open/GS-102)、[GS-105](http://127.0.0.1:8765/open/GS-105)。
- metrics: N1 全库质量门从 M107 `warn_cards=365 warn_items=697` 降到 M108 `warn_cards=355 warn_items=677`；N5 剩余 10 条待正式判断和 5 条人工重连相关项仍缺用户确认；N6 当前正式卡状态为 待复做 712、已掌握 65、待人工重连 0；N8 ID 前缀分布为 GS=657、LA=119、PR=1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=827 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=754、knowledge_clusters=412、method_clusters=1358、error_clusters=350、action_gap_clusters=9；本轮 10 张单卡质量门 `checked=10 failed=0 warn_items=[]`；全库质量门 `checked=777 failed=0 error_items=0 warn_cards=355 warn_items=677`。
- expansion: 候选台账本轮未推进；剩余候选缺用户本人错因、题目定位或人工重连确认，不为配额伪造状态。
- spot_check: 已掌握抽测建议沿用 [GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-318](http://127.0.0.1:8765/open/GS-318)、[GS-441](http://127.0.0.1:8765/open/GS-441)。
- tutor: 本轮只做正式卡高层入口与证据边界补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-109 旧批量卡method_gap与error_causes第五批证据边界补强报告

- input: 用户提醒必须读取相关 skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-106](http://127.0.0.1:8765/open/GS-106)、[GS-108](http://127.0.0.1:8765/open/GS-108)、[GS-109](http://127.0.0.1:8765/open/GS-109)、[GS-110](http://127.0.0.1:8765/open/GS-110)、[GS-111](http://127.0.0.1:8765/open/GS-111)、[GS-112](http://127.0.0.1:8765/open/GS-112)、[GS-113](http://127.0.0.1:8765/open/GS-113)、[GS-116](http://127.0.0.1:8765/open/GS-116)、[GS-117](http://127.0.0.1:8765/open/GS-117)、[GS-122](http://127.0.0.1:8765/open/GS-122)。
- metrics: N1 全库质量门从 M108 `warn_cards=355 warn_items=677` 降到 M109 `warn_cards=345 warn_items=657`；N3 当前 `related: 待补充=0`、空列表 `0`；N4 bridge `formal_fallbacks=0`；N6 状态分布为 待复做 712、已掌握 65；N8 ID 前缀分布为 GS=657、LA=119、PR=1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=824 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=754、knowledge_clusters=412、method_clusters=1358、error_clusters=360、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门 `checked=10 failed=0 warn_items=0`；全库质量门 `checked=777 failed=0 warn_cards=345 warn_items=657`。
- expansion: 候选台账本轮未推进；剩余候选缺用户本人错因、题目定位或人工重连确认，不为配额伪造状态。
- spot_check: 已掌握抽测建议沿用 [GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-318](http://127.0.0.1:8765/open/GS-318)、[GS-441](http://127.0.0.1:8765/open/GS-441)。
- tutor: 本轮只做正式卡高层入口与证据边界补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-110 旧批量卡method_gap与error_causes第六批证据边界补强报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并要求把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`、`fast-path.md`。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-128](http://127.0.0.1:8765/open/GS-128)、[GS-130](http://127.0.0.1:8765/open/GS-130)、[GS-136](http://127.0.0.1:8765/open/GS-136)、[GS-137](http://127.0.0.1:8765/open/GS-137)、[GS-139](http://127.0.0.1:8765/open/GS-139)、[GS-142](http://127.0.0.1:8765/open/GS-142)、[GS-144](http://127.0.0.1:8765/open/GS-144)、[GS-146](http://127.0.0.1:8765/open/GS-146)、[GS-147](http://127.0.0.1:8765/open/GS-147)、[GS-149](http://127.0.0.1:8765/open/GS-149)。
- metrics: N1 全库质量门从 M109 `warn_cards=345 warn_items=657` 降到 M110 `warn_cards=335 warn_items=637`；N3 当前 `related: 待补充=0`、空列表 `0`；N4 bridge `formal_fallbacks=0`；N6 状态分布为 待复做 712、已掌握 65；N8 ID 前缀分布为 GS=657、LA=119、PR=1。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=825 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=754、knowledge_clusters=412、method_clusters=1358、error_clusters=370、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门 `checked=10 failed=0 warn_items=0`；全库质量门 `checked=777 failed=0 warn_cards=335 warn_items=637`。
- expansion: 候选台账本轮未推进；剩余候选缺用户本人错因、题目定位或人工重连确认，不为配额伪造状态。
- spot_check: 已掌握抽测建议沿用 [GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-318](http://127.0.0.1:8765/open/GS-318)、[GS-441](http://127.0.0.1:8765/open/GS-441)。
- tutor: 本轮只做正式卡高层入口与证据边界补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-04] maintenance | MATHWIKI-MAINT-111 旧批量卡method_gap与error_causes第七批证据边界补强报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并要求把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`Obsidian CLI`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-152](http://127.0.0.1:8765/open/GS-152)、[GS-153](http://127.0.0.1:8765/open/GS-153)、[GS-164](http://127.0.0.1:8765/open/GS-164)、[GS-165](http://127.0.0.1:8765/open/GS-165)、[GS-167](http://127.0.0.1:8765/open/GS-167)、[GS-168](http://127.0.0.1:8765/open/GS-168)、[GS-169](http://127.0.0.1:8765/open/GS-169)、[GS-183](http://127.0.0.1:8765/open/GS-183)、[GS-185](http://127.0.0.1:8765/open/GS-185)、[GS-186](http://127.0.0.1:8765/open/GS-186)。
- metrics: N1 全库质量门从 M110 `warn_cards=335 warn_items=637` 降到 M111 `warn_cards=326 warn_items=617`；`error_cards=0 error_items=0`；剩余主要 WARN 为 `method_gap not enabled=312`、`error_causes is placeholder or empty=243`、`visual gap record has no asset mapping by design=41`。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=1934 medium=826 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=754、knowledge_clusters=412、method_clusters=1358、error_clusters=380、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`，其中 GS-152 保留视觉错连缺口 WARN；全库质量门结果 `/tmp/kaoyan_math_m111_full_quality_gate_details.json`。
- expansion: 候选台账本轮未推进；剩余候选缺用户本人错因、题目定位或人工重连确认，不为配额伪造状态。
- tutor: 本轮只做正式卡高层入口与证据边界补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-117 旧批量卡method_gap与error_causes第十三批质量扩量轮次报告

- input: 继续当前长期目标；用户要求必须读取相关 skill，并把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标文件、项目规则、method_gap schema、方法卡、M116 报告和 Tutor 安全输入包。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-338](http://127.0.0.1:8765/open/GS-338)、[GS-367](http://127.0.0.1:8765/open/GS-367)、[GS-380](http://127.0.0.1:8765/open/GS-380)、[GS-381](http://127.0.0.1:8765/open/GS-381)、[GS-382](http://127.0.0.1:8765/open/GS-382)、[GS-383](http://127.0.0.1:8765/open/GS-383)、[GS-384](http://127.0.0.1:8765/open/GS-384)、[GS-386](http://127.0.0.1:8765/open/GS-386)、[GS-387](http://127.0.0.1:8765/open/GS-387)、[GS-388](http://127.0.0.1:8765/open/GS-388)。
- metrics: N1 全库质量门从 M116 `warn_cards=277 warn_items=517` 降到 M117 `warn_cards=267 warn_items=497`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 262 降至 252；`error_causes placeholder/empty` 从 193 降至 183。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2024 medium=738 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=755、knowledge_clusters=412、method_clusters=1358、error_clusters=411、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m117_full_quality_gate_details.json`。
- expansion: 候选台账本轮未推进；剩余 10 条待正式判断和 5 条人工重连项仍缺用户本人错因、题目定位或人工确认，不为配额伪造状态。
- spot_check: 已掌握抽测建议沿用 [GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-318](http://127.0.0.1:8765/open/GS-318)、[GS-441](http://127.0.0.1:8765/open/GS-441)。
- tutor: Tutor 技能与安全输入包已读取；本轮只做旧批量卡低置信高层字段补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新；source summaries 首次并行运行遇到方法簇重建竞态，顺序重跑成功。

## [2026-07-05] maintenance | MATHWIKI-MAINT-118 旧批量卡method_gap与error_causes第十四批质量扩量轮次报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-389](http://127.0.0.1:8765/open/GS-389)、[GS-390](http://127.0.0.1:8765/open/GS-390)、[GS-391](http://127.0.0.1:8765/open/GS-391)、[GS-392](http://127.0.0.1:8765/open/GS-392)、[GS-393](http://127.0.0.1:8765/open/GS-393)、[GS-394](http://127.0.0.1:8765/open/GS-394)、[GS-395](http://127.0.0.1:8765/open/GS-395)、[GS-396](http://127.0.0.1:8765/open/GS-396)、[GS-397](http://127.0.0.1:8765/open/GS-397)、[GS-398](http://127.0.0.1:8765/open/GS-398)。
- metrics: N1 全库质量门从 M117 `warn_cards=267 warn_items=497` 降到 M118 `warn_cards=257 warn_items=477`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 252 降至 242；`error_causes placeholder/empty` 从 183 降至 173。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2047 medium=712 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=755、knowledge_clusters=412、method_clusters=1358、error_clusters=412、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m118_full_quality_gate_details.json`。
- expansion: 候选台账本轮未推进；剩余 10 条待正式判断和 5 条人工重连项仍缺用户本人错因、题目定位或人工确认，不为配额伪造状态。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层字段补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-119 旧批量卡method_gap与error_causes第十五批质量扩量轮次报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log 与 M118 报告。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-399](http://127.0.0.1:8765/open/GS-399)、[GS-400](http://127.0.0.1:8765/open/GS-400)、[GS-401](http://127.0.0.1:8765/open/GS-401)、[GS-402](http://127.0.0.1:8765/open/GS-402)、[GS-403](http://127.0.0.1:8765/open/GS-403)、[GS-404](http://127.0.0.1:8765/open/GS-404)、[GS-406](http://127.0.0.1:8765/open/GS-406)、[GS-407](http://127.0.0.1:8765/open/GS-407)、[GS-409](http://127.0.0.1:8765/open/GS-409)、[GS-410](http://127.0.0.1:8765/open/GS-410)。
- metrics: N1 全库质量门从 M118 `warn_cards=257 warn_items=477` 降到 M119 `warn_cards=247 warn_items=457`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 242 降至 232；`error_causes placeholder/empty` 从 173 降至 163。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2066 medium=694 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=755、knowledge_clusters=412、method_clusters=1358、error_clusters=412、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m119_full_quality_gate_details.json`。
- expansion: 候选台账本轮未推进；剩余 10 条待正式判断和 5 条人工重连项仍缺用户本人错因、题目定位或人工确认，不为配额伪造状态。
- skipped: GS-405、GS-408 证据不足，暂不补低置信错因。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层字段补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-120 旧批量卡method_gap与error_causes第十六批质量扩量轮次报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log 与 M119 报告。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-411](http://127.0.0.1:8765/open/GS-411)、[GS-412](http://127.0.0.1:8765/open/GS-412)、[GS-413](http://127.0.0.1:8765/open/GS-413)、[GS-415](http://127.0.0.1:8765/open/GS-415)、[GS-418](http://127.0.0.1:8765/open/GS-418)、[GS-419](http://127.0.0.1:8765/open/GS-419)、[GS-420](http://127.0.0.1:8765/open/GS-420)、[GS-421](http://127.0.0.1:8765/open/GS-421)、[GS-422](http://127.0.0.1:8765/open/GS-422)、[GS-423](http://127.0.0.1:8765/open/GS-423)。
- metrics: N1 全库质量门从 M119 `warn_cards=247 warn_items=457` 降到 M120 `warn_cards=237 warn_items=437`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 232 降至 222；`error_causes placeholder/empty` 从 163 降至 153。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2086 medium=675 weak_audit=246；wiki coverage 已刷新，source summaries=777、compiled=755、knowledge_clusters=412、method_clusters=1358、error_clusters=412、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m120_full_quality_gate_details.json`。
- expansion: 候选台账本轮未推进；剩余 10 条待正式判断和 5 条人工重连项仍缺用户本人错因、题目定位或人工确认，不为配额伪造状态。
- skipped: GS-414、GS-426、GS-427、GS-428、GS-429 证据不足，暂不补低置信错因。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层字段补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-121 旧批量卡method_gap与error_causes第十七批质量扩量轮次报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log 与 M120 报告。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-327](http://127.0.0.1:8765/open/GS-327)、[GS-328](http://127.0.0.1:8765/open/GS-328)、[GS-329](http://127.0.0.1:8765/open/GS-329)、[GS-330](http://127.0.0.1:8765/open/GS-330)、[GS-332](http://127.0.0.1:8765/open/GS-332)、[GS-333](http://127.0.0.1:8765/open/GS-333)、[GS-334](http://127.0.0.1:8765/open/GS-334)、[GS-335](http://127.0.0.1:8765/open/GS-335)、[GS-337](http://127.0.0.1:8765/open/GS-337)、[GS-339](http://127.0.0.1:8765/open/GS-339)。
- metrics: N1 全库质量门从 M120 `warn_cards=237 warn_items=437` 降到 M121 `warn_cards=227 warn_items=417`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 222 降至 212；`error_causes placeholder/empty` 从 153 降至 143。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2104 medium=656 weak_audit=248；wiki coverage 已刷新，source summaries=777、compiled=755、knowledge_clusters=412、method_clusters=1358、error_clusters=412、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m121_full_quality_gate_after.json`。
- lint_note: `build_wrong_card_source_summaries.py` 首次与 method-cluster 重建并行运行出现短暂读文件竞态，确认页面存在后单独重跑成功；不是数据缺失。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层字段补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-122 旧批量卡method_gap与error_causes第十八批质量扩量轮次报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`、`fast-path.md`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log、候选台账与 M121 报告。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-336](http://127.0.0.1:8765/open/GS-336)、[GS-340](http://127.0.0.1:8765/open/GS-340)、[GS-342](http://127.0.0.1:8765/open/GS-342)、[GS-345](http://127.0.0.1:8765/open/GS-345)、[GS-346](http://127.0.0.1:8765/open/GS-346)、[GS-347](http://127.0.0.1:8765/open/GS-347)、[GS-348](http://127.0.0.1:8765/open/GS-348)、[GS-351](http://127.0.0.1:8765/open/GS-351)、[GS-352](http://127.0.0.1:8765/open/GS-352)、[GS-353](http://127.0.0.1:8765/open/GS-353)。
- expansion: CAND-0001 至 CAND-0010 从 `candidate` 前进为 `confirmed`，仅表示视觉题目身份与缺口已确认；仍缺用户本人错因/正式入库确认，不建正式卡。
- metrics: N1 全库质量门从 M121 `warn_cards=227 warn_items=417` 降到 M122 `warn_cards=217 warn_items=397`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 212 降至 202；`error_causes placeholder/empty` 从 143 降至 133。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2124 medium=639 weak_audit=252；wiki coverage 已刷新，source summaries=777、compiled=755、knowledge_clusters=412、method_clusters=1358、error_clusters=412、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m122_full_quality_gate_after.json`。
- spot_check: 已掌握抽测建议为 [GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-318](http://127.0.0.1:8765/open/GS-318)、[GS-441](http://127.0.0.1:8765/open/GS-441)。
- tutor: Tutor 技能与安全输入包已读取；本轮只做旧批量卡低置信高层字段补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-123 多元函数旧批量卡method_gap与候选重连质量扩量轮次报告

- input: 继续当前长期目标；读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor` skill 后，把错题质量提升落实到正式文件修改。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `error_causes` 和 `method_gap`：[GS-354](http://127.0.0.1:8765/open/GS-354)、[GS-355](http://127.0.0.1:8765/open/GS-355)、[GS-356](http://127.0.0.1:8765/open/GS-356)、[GS-357](http://127.0.0.1:8765/open/GS-357)、[GS-358](http://127.0.0.1:8765/open/GS-358)、[GS-360](http://127.0.0.1:8765/open/GS-360)、[GS-362](http://127.0.0.1:8765/open/GS-362)、[GS-363](http://127.0.0.1:8765/open/GS-363)、[GS-369](http://127.0.0.1:8765/open/GS-369)、[GS-375](http://127.0.0.1:8765/open/GS-375)。
- expansion: CAND-0012 至 CAND-0015 从 `candidate` 前进为 `confirmed`，仅表示异常归属、主入口或双入口关系已确认；仍缺用户本人错因、迁移授权或正式入库确认。
- metrics: N1 全库质量门从 M122 `warn_cards=217 warn_items=397` 降到 M123 `warn_cards=210 warn_items=378`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 202 降至 192；`error_causes placeholder/empty` 从 133 降至 124。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2151 medium=617 weak_audit=252；wiki coverage 已刷新，source summaries=777、compiled=755、knowledge_clusters=412、method_clusters=1358、error_clusters=412、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m123_full_quality_gate_after.json`。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层字段补强和候选台账状态推进，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-124 旧批量卡method_gap结构化第十九批质量扩量轮次报告

- input: 继续当前长期目标；按要求读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor` skill 后，把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log、候选台账与 M123 报告。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `method_gap`：[GS-155](http://127.0.0.1:8765/open/GS-155)、[GS-157](http://127.0.0.1:8765/open/GS-157)、[GS-158](http://127.0.0.1:8765/open/GS-158)、[GS-159](http://127.0.0.1:8765/open/GS-159)、[GS-160](http://127.0.0.1:8765/open/GS-160)、[GS-161](http://127.0.0.1:8765/open/GS-161)、[GS-166](http://127.0.0.1:8765/open/GS-166)、[GS-171](http://127.0.0.1:8765/open/GS-171)、[GS-172](http://127.0.0.1:8765/open/GS-172)、[GS-173](http://127.0.0.1:8765/open/GS-173)。
- expansion: 本轮未新增或推进候选；当前剩余候选缺用户本人错因、正式入库确认或迁移授权，不为配额伪造状态。
- metrics: N1 全库质量门从 M123 `warn_cards=210 warn_items=378` 降到 M124 `warn_cards=200 warn_items=368`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 192 降至 182；`error_causes placeholder/empty` 维持 124。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2151 medium=617 weak_audit=252；wiki coverage 已刷新，source summaries=777、compiled=759、knowledge_clusters=412、method_clusters=1358、error_clusters=412、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m124_full_quality_gate_after.json`。
- tutor: Tutor 技能、安全输入包与 dashboard 已读取；既有安全输入已覆盖本轮极值、变限积分、黎曼和与积分计算第一动作，本轮不新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-125 反常积分与定积分旧卡method_gap结构化第二十批质量扩量轮次报告

- input: 用户强调要读取相关 skill，并继续把错题质量提升落实到正式文件修改，而不是只查看。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log 与 M124 报告。
- formal_cards_updated: 10 张旧批量正式卡补强低置信 `method_gap`：[GS-174](http://127.0.0.1:8765/open/GS-174)、[GS-175](http://127.0.0.1:8765/open/GS-175)、[GS-176](http://127.0.0.1:8765/open/GS-176)、[GS-177](http://127.0.0.1:8765/open/GS-177)、[GS-178](http://127.0.0.1:8765/open/GS-178)、[GS-179](http://127.0.0.1:8765/open/GS-179)、[GS-180](http://127.0.0.1:8765/open/GS-180)、[GS-181](http://127.0.0.1:8765/open/GS-181)、[GS-182](http://127.0.0.1:8765/open/GS-182)、[GS-184](http://127.0.0.1:8765/open/GS-184)。
- expansion: 本轮未新增或推进候选；当前剩余候选缺用户本人错因、正式入库确认或迁移授权，不为配额伪造状态。
- metrics: N1 全库质量门从 M124 `warn_cards=200 warn_items=368` 降到 M125 `warn_cards=190 warn_items=358`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 182 降至 172；`error_causes placeholder/empty` 维持 124。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2151 medium=617 weak_audit=252；wiki coverage 已刷新，source summaries=777、compiled=761、knowledge_clusters=412、method_clusters=1358、error_clusters=412、action_gap_clusters=9、missing_action_gap=171；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m125_full_quality_gate_after.json`。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层方法入口补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-129 一元积分计算旧卡method_gap结构化第二十四批质量扩量轮次报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并要求质量提升落实到正式文件修改；本轮继续当前长期目标。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log 与 M128 报告。
- formal_cards_updated: 12 张一元积分计算、定积分性质、反常积分、含参积分和相关变化率旧批量正式卡补强低置信 `method_gap`：[GS-269](http://127.0.0.1:8765/open/GS-269)、[GS-270](http://127.0.0.1:8765/open/GS-270)、[GS-271](http://127.0.0.1:8765/open/GS-271)、[GS-272](http://127.0.0.1:8765/open/GS-272)、[GS-274](http://127.0.0.1:8765/open/GS-274)、[GS-275](http://127.0.0.1:8765/open/GS-275)、[GS-276](http://127.0.0.1:8765/open/GS-276)、[GS-277](http://127.0.0.1:8765/open/GS-277)、[GS-278](http://127.0.0.1:8765/open/GS-278)、[GS-282](http://127.0.0.1:8765/open/GS-282)、[GS-284](http://127.0.0.1:8765/open/GS-284)、[GS-285](http://127.0.0.1:8765/open/GS-285)。
- skipped: `GS-280`、`GS-281`、`GS-286`、`GS-291` 属于重复占位或已掌握卡，且原卡明确写有不反写方法断点的边界；不为压低 warning 破坏语义。
- metrics: N1 全库质量门从 M128 `warn_cards=156 warn_items=324` 降到 M129 `warn_cards=144 warn_items=312`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 138 降至 126；`error_causes placeholder/empty` 维持 124。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2151 medium=617 weak_audit=252；wiki coverage 已刷新，source summaries=777、compiled=763、knowledge_clusters=412、method_clusters=1358、error_clusters=412、action_gap_clusters=9、missing_action_gap=125；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 12 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m129_full_quality_gate_after.json`。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层方法入口补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-130 高数线代旧卡method_gap结构化第二十五批质量扩量轮次报告

- input: 用户提醒必须读取相关 skill，并要求把错题质量提升落实为正式文件修改；本轮继续当前长期目标。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log 与 M129 报告。
- formal_cards_updated: 12 张高数与线代旧批量正式卡补强低置信 `method_gap`：[GS-123](http://127.0.0.1:8765/open/GS-123)、[GS-209](http://127.0.0.1:8765/open/GS-209)、[GS-308](http://127.0.0.1:8765/open/GS-308)、[GS-325](http://127.0.0.1:8765/open/GS-325)、[GS-343](http://127.0.0.1:8765/open/GS-343)、[GS-373](http://127.0.0.1:8765/open/GS-373)、[LA-001](http://127.0.0.1:8765/open/LA-001)、[LA-002](http://127.0.0.1:8765/open/LA-002)、[LA-009](http://127.0.0.1:8765/open/LA-009)、[LA-010](http://127.0.0.1:8765/open/LA-010)、[LA-011](http://127.0.0.1:8765/open/LA-011)、[LA-012](http://127.0.0.1:8765/open/LA-012)。
- error_boundary_updated: 6 张旧卡将空泛错因改为保守证据边界：`GS-325`、`LA-002`、`LA-009`、`LA-010`、`LA-011`、`LA-012`；不编造用户本人错因。
- skipped: `GS-280`、`GS-281`、`GS-286`、`GS-291` 为重复、已掌握或占位卡；`GS-405`、`GS-408`、`GS-414`、`GS-425` 至 `GS-429` 缺题图/OCR/身份信息；`GS-349` 更像讲义提纲；`LA-003`、`LA-004` 属于合并或跨题待确认。本轮不为压低 warning 破坏语义。
- metrics: N1 全库质量门从 M129 `warn_cards=144 warn_items=312` 降到 M130 `warn_cards=132 warn_items=294`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 126 降至 114；`error_causes placeholder/empty` 从 124 降至 118。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2159 medium=610 weak_audit=252；wiki coverage 已刷新，source summaries=777、compiled=766、knowledge_clusters=412、method_clusters=1358、error_clusters=413、action_gap_clusters=9、missing_action_gap=113；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 12 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m130_full_quality_gate_after.json`。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层方法入口补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-126 微分方程旧卡method_gap结构化第二十一批质量扩量轮次报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并要求质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、method_gap schema、H15 微分方程方法卡、wiki/index、wiki/log 与 M125 报告。
- formal_cards_updated: 10 张微分方程旧批量正式卡补强低置信 `method_gap`：[GS-187](http://127.0.0.1:8765/open/GS-187)、[GS-188](http://127.0.0.1:8765/open/GS-188)、[GS-189](http://127.0.0.1:8765/open/GS-189)、[GS-190](http://127.0.0.1:8765/open/GS-190)、[GS-191](http://127.0.0.1:8765/open/GS-191)、[GS-192](http://127.0.0.1:8765/open/GS-192)、[GS-193](http://127.0.0.1:8765/open/GS-193)、[GS-194](http://127.0.0.1:8765/open/GS-194)、[GS-195](http://127.0.0.1:8765/open/GS-195)、[GS-196](http://127.0.0.1:8765/open/GS-196)。
- expansion: 本轮未新增或推进候选；当前候选缺用户本人错因、正式入库确认或迁移授权，不为配额伪造状态。
- metrics: N1 全库质量门从 M125 `warn_cards=190 warn_items=358` 降到 M126 `warn_cards=180 warn_items=348`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 172 降至 162；`error_causes placeholder/empty` 维持 124。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2151 medium=617 weak_audit=252；wiki coverage 已刷新，source summaries=777、compiled=761、knowledge_clusters=412、method_clusters=1358、error_clusters=412、action_gap_clusters=9、missing_action_gap=161；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 10 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m126_full_quality_gate_after.json`。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层方法入口补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-127 微分方程建模旧卡method_gap结构化第二十二批质量扩量轮次报告

- input: 用户提醒必须读取相关 skill，并要求质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、method_gap schema、H15 微分方程方法卡、微分方程方法页、wiki/index、wiki/log、候选台账与 M126 报告。
- formal_cards_updated: 12 张微分方程建模旧批量正式卡补强低置信 `method_gap`：[GS-197](http://127.0.0.1:8765/open/GS-197)、[GS-198](http://127.0.0.1:8765/open/GS-198)、[GS-199](http://127.0.0.1:8765/open/GS-199)、[GS-200](http://127.0.0.1:8765/open/GS-200)、[GS-201](http://127.0.0.1:8765/open/GS-201)、[GS-202](http://127.0.0.1:8765/open/GS-202)、[GS-203](http://127.0.0.1:8765/open/GS-203)、[GS-204](http://127.0.0.1:8765/open/GS-204)、[GS-205](http://127.0.0.1:8765/open/GS-205)、[GS-206](http://127.0.0.1:8765/open/GS-206)、[GS-207](http://127.0.0.1:8765/open/GS-207)、[GS-211](http://127.0.0.1:8765/open/GS-211)。
- expansion: 本轮未新增或推进候选；当前候选缺用户本人错因、正式入库确认或迁移授权，不为配额伪造状态。
- metrics: N1 全库质量门从 M126 `warn_cards=180 warn_items=348` 降到 M127 `warn_cards=168 warn_items=336`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 162 降至 150；`error_causes placeholder/empty` 维持 124。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2151 medium=617 weak_audit=252；wiki coverage 已刷新，source summaries=777、compiled=762、knowledge_clusters=412、method_clusters=1358、error_clusters=412、action_gap_clusters=9、missing_action_gap=149；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 12 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m127_full_quality_gate_after.json`。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层方法入口补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-128 一元微分应用与相关变化率旧卡method_gap结构化第二十三批质量扩量轮次报告

- input: 用户提醒必须读取相关 skill，并继续把错题质量提升落实到正式文件修改，而不是只查看。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log 与 M127 报告。
- formal_cards_updated: 12 张一元微分应用、相关变化率、微分方程建模和复合积分旧批量正式卡补强低置信 `method_gap`：[GS-248](http://127.0.0.1:8765/open/GS-248)、[GS-250](http://127.0.0.1:8765/open/GS-250)、[GS-251](http://127.0.0.1:8765/open/GS-251)、[GS-252](http://127.0.0.1:8765/open/GS-252)、[GS-254](http://127.0.0.1:8765/open/GS-254)、[GS-255](http://127.0.0.1:8765/open/GS-255)、[GS-259](http://127.0.0.1:8765/open/GS-259)、[GS-260](http://127.0.0.1:8765/open/GS-260)、[GS-261](http://127.0.0.1:8765/open/GS-261)、[GS-262](http://127.0.0.1:8765/open/GS-262)、[GS-264](http://127.0.0.1:8765/open/GS-264)、[GS-265](http://127.0.0.1:8765/open/GS-265)。
- repair: `GS-262` 原卡存在旧 LaTeX 控制字符残留，本轮在同卡编辑范围内恢复为正常 `\theta`、`\frac`、`\boxed{5}` 形式。
- metrics: N1 全库质量门从 M127 `warn_cards=168 warn_items=336` 降到 M128 `warn_cards=156 warn_items=324`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 150 降至 138；`error_causes placeholder/empty` 维持 124。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2151 medium=617 weak_audit=252；wiki coverage 已刷新，source summaries=777、compiled=762、knowledge_clusters=412、method_clusters=1358、error_clusters=412、action_gap_clusters=9、missing_action_gap=137；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；本轮 12 张单卡质量门全部 `quality_gate=ok`；全库质量门结果 `/tmp/kaoyan_math_m128_full_quality_gate_after.json`。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层方法入口补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-131 线代旧卡method_gap结构化第二十六批质量扩量轮次报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并要求继续把错题质量提升落实到正式文件修改。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log 与 M130 报告。
- formal_cards_updated: 20 张线代旧批量正式卡补强低置信 `method_gap` 和保守错因边界：[LA-017](http://127.0.0.1:8765/open/LA-017)、[LA-020](http://127.0.0.1:8765/open/LA-020)、[LA-021](http://127.0.0.1:8765/open/LA-021)、[LA-027](http://127.0.0.1:8765/open/LA-027)、[LA-029](http://127.0.0.1:8765/open/LA-029)、[LA-030](http://127.0.0.1:8765/open/LA-030)、[LA-031](http://127.0.0.1:8765/open/LA-031)、[LA-033](http://127.0.0.1:8765/open/LA-033)、[LA-034](http://127.0.0.1:8765/open/LA-034)、[LA-035](http://127.0.0.1:8765/open/LA-035)、[LA-037](http://127.0.0.1:8765/open/LA-037)、[LA-038](http://127.0.0.1:8765/open/LA-038)、[LA-040](http://127.0.0.1:8765/open/LA-040)、[LA-041](http://127.0.0.1:8765/open/LA-041)、[LA-042](http://127.0.0.1:8765/open/LA-042)、[LA-043](http://127.0.0.1:8765/open/LA-043)、[LA-044](http://127.0.0.1:8765/open/LA-044)、[LA-045](http://127.0.0.1:8765/open/LA-045)、[LA-046](http://127.0.0.1:8765/open/LA-046)、[LA-048](http://127.0.0.1:8765/open/LA-048)。
- metrics: N1 全库质量门从 M130 `warn_cards=132 warn_items=294` 降到 M131 `warn_cards=114 warn_items=254`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 114 降至 94；`error_causes placeholder/empty` 从 118 降至 98。
- validation: `wrongnet.py rebuild` 成功，cards=777 strong=2202 medium=571 weak_audit=252；wiki coverage 已刷新，source summaries=777、compiled=767、knowledge_clusters=412、method_clusters=1358、error_clusters=413、action_gap_clusters=9；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；20 张 card-only 质量门 `0 errors/0 warnings`，完整质量门 `0 errors/2 design warnings`；全库质量门结果 `/tmp/kaoyan_math_m131_full_quality_gate_after_clean.json`。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层方法入口补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 本轮未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-132 线代旧卡method_gap结构化第二十七批质量扩量轮次报告

- input: 用户再次提醒必须读取相关 skill，并要求质量提升落实为正式错题卡修改，而不是只查看。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log、候选台账与 M131 报告。
- formal_cards_updated: 18 张线代旧批量正式卡补强低置信 `method_gap` 和保守错因边界：[LA-039](http://127.0.0.1:8765/open/LA-039)、[LA-049](http://127.0.0.1:8765/open/LA-049)、[LA-050](http://127.0.0.1:8765/open/LA-050)、[LA-052](http://127.0.0.1:8765/open/LA-052)、[LA-053](http://127.0.0.1:8765/open/LA-053)、[LA-054](http://127.0.0.1:8765/open/LA-054)、[LA-055](http://127.0.0.1:8765/open/LA-055)、[LA-056](http://127.0.0.1:8765/open/LA-056)、[LA-057](http://127.0.0.1:8765/open/LA-057)、[LA-058](http://127.0.0.1:8765/open/LA-058)、[LA-059](http://127.0.0.1:8765/open/LA-059)、[LA-060](http://127.0.0.1:8765/open/LA-060)、[LA-061](http://127.0.0.1:8765/open/LA-061)、[LA-062](http://127.0.0.1:8765/open/LA-062)、[LA-063](http://127.0.0.1:8765/open/LA-063)、[LA-064](http://127.0.0.1:8765/open/LA-064)、[LA-067](http://127.0.0.1:8765/open/LA-067)、[LA-068](http://127.0.0.1:8765/open/LA-068)。
- skipped: [LA-051](http://127.0.0.1:8765/open/LA-051)、[LA-065](http://127.0.0.1:8765/open/LA-065)、[LA-066](http://127.0.0.1:8765/open/LA-066) 证据不足或视觉缺口未补；`LA-003`、`LA-004`、`LA-005`、`LA-006`、`LA-024` 仍属合并、跨题或 OCR 待确认边界。
- metrics: N1 全库质量门从 M131 `warn_cards=114 warn_items=254` 降到 M132 `warn_cards=96 warn_items=218`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 94 降至 76；`error_causes placeholder/empty` 从 98 降至 80。
- validation: 18 张卡逐题质量门全部 `quality_gate=ok`；`wrongnet.py rebuild` 成功，cards=777 strong=2223 medium=551 weak_audit=264；wiki coverage 已刷新，source summaries=777、compiled=767、knowledge_clusters=412、method_clusters=1358、error_clusters=413、action_gap_clusters=9、missing_action_gap=75；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；全库扫描结果 `/tmp/kaoyan_math_m132_post_scan.json`。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层方法入口补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 本轮未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-133 线代旧卡method_gap结构化第二十八批质量扩量轮次报告

- input: 用户提醒必须读取相关 skill，并要求继续把错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`；同步读取项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log 与 M132 报告。
- formal_cards_updated: 19 张线代旧批量正式卡补强低置信 `method_gap` 和保守错因边界：[LA-069](http://127.0.0.1:8765/open/LA-069)、[LA-070](http://127.0.0.1:8765/open/LA-070)、[LA-071](http://127.0.0.1:8765/open/LA-071)、[LA-072](http://127.0.0.1:8765/open/LA-072)、[LA-073](http://127.0.0.1:8765/open/LA-073)、[LA-074](http://127.0.0.1:8765/open/LA-074)、[LA-075](http://127.0.0.1:8765/open/LA-075)、[LA-078](http://127.0.0.1:8765/open/LA-078)、[LA-079](http://127.0.0.1:8765/open/LA-079)、[LA-081](http://127.0.0.1:8765/open/LA-081)、[LA-082](http://127.0.0.1:8765/open/LA-082)、[LA-087](http://127.0.0.1:8765/open/LA-087)、[LA-088](http://127.0.0.1:8765/open/LA-088)、[LA-089](http://127.0.0.1:8765/open/LA-089)、[LA-090](http://127.0.0.1:8765/open/LA-090)、[LA-091](http://127.0.0.1:8765/open/LA-091)、[LA-092](http://127.0.0.1:8765/open/LA-092)、[LA-093](http://127.0.0.1:8765/open/LA-093)、[LA-094](http://127.0.0.1:8765/open/LA-094)。
- skipped: [LA-076](http://127.0.0.1:8765/open/LA-076)、[LA-077](http://127.0.0.1:8765/open/LA-077)、[LA-080](http://127.0.0.1:8765/open/LA-080)、[LA-083](http://127.0.0.1:8765/open/LA-083) 至 [LA-086](http://127.0.0.1:8765/open/LA-086) 证据不足；不为压低 warning 伪造个人错因。
- metrics: N1 全库质量门从 M132 `warn_cards=96 warn_items=218` 降到 M133 `warn_cards=77 warn_items=180`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 76 降至 57；`error_causes placeholder/empty` 从 80 降至 61。
- validation: 19 张卡逐题质量门全部 `quality_gate=ok`；`wrongnet.py rebuild` 成功，cards=777 strong=2255 medium=516 weak_audit=288；wiki coverage 已刷新，source summaries=777、compiled=767、knowledge_clusters=412、method_clusters=1358、error_clusters=413、action_gap_clusters=9、missing_action_gap=56；bridge snapshot records=924、visual_records=924、formal_fallbacks=0、assets=1270；全库扫描结果 `/tmp/kaoyan_math_m133_post_scan.json`。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层方法入口补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 本轮未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-134 线代旧卡method_gap结构化第二十九批质量扩量轮次报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并要求质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log、线代专题页与 M133 报告。
- formal_cards_updated: 19 张线代旧批量正式卡补强低置信 `method_gap` 和保守错因边界：[LA-097](http://127.0.0.1:8765/open/LA-097)、[LA-098](http://127.0.0.1:8765/open/LA-098)、[LA-099](http://127.0.0.1:8765/open/LA-099)、[LA-100](http://127.0.0.1:8765/open/LA-100)、[LA-103](http://127.0.0.1:8765/open/LA-103)、[LA-104](http://127.0.0.1:8765/open/LA-104)、[LA-105](http://127.0.0.1:8765/open/LA-105)、[LA-106](http://127.0.0.1:8765/open/LA-106)、[LA-109](http://127.0.0.1:8765/open/LA-109)、[LA-110](http://127.0.0.1:8765/open/LA-110)、[LA-111](http://127.0.0.1:8765/open/LA-111)、[LA-112](http://127.0.0.1:8765/open/LA-112)、[LA-113](http://127.0.0.1:8765/open/LA-113)、[LA-114](http://127.0.0.1:8765/open/LA-114)、[LA-115](http://127.0.0.1:8765/open/LA-115)、[LA-116](http://127.0.0.1:8765/open/LA-116)、[LA-117](http://127.0.0.1:8765/open/LA-117)、[LA-118](http://127.0.0.1:8765/open/LA-118)、[LA-119](http://127.0.0.1:8765/open/LA-119)。
- skipped: [LA-095](http://127.0.0.1:8765/open/LA-095)、[LA-096](http://127.0.0.1:8765/open/LA-096) 仍为 OCR 待核对；[LA-107](http://127.0.0.1:8765/open/LA-107)、[LA-108](http://127.0.0.1:8765/open/LA-108) 为总纲型旧卡；不为降低 warning 编造个人错因。
- metrics: N1 全库质量门从 M133 `warn_cards=77 warn_items=180` 降到 M134 `warn_cards=58 warn_items=142`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 57 降至 38；`error_causes placeholder/empty` 从 61 降至 42。
- validation: 19 张卡逐题质量门全部 `quality_gate=ok` 且无 warning；`wrongnet.py rebuild` 成功，cards=777 strong=2274 medium=490 weak_audit=291；wiki coverage 已刷新，source summaries=777、compiled=767、knowledge_clusters=412、method_clusters=1358、error_clusters=414、action_gap_clusters=9、missing_action_gap=37；全库扫描结果 `/tmp/kaoyan_math_m134_post_scan_final.json`。
- expansion: 本轮未新增或推进候选；当前候选缺用户本人错因、正式化确认或人工重连授权，不为配额伪造状态。
- tutor: Tutor 技能已读取；本轮只做旧批量卡低置信高层方法入口补强，没有新增安全训练包；Tutor source 为 `not_needed`，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 本轮未修改回滚 JSON；未新增 Tutor 训练项；未启动 Tutor quiz；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-135 中值定理与谱映射旧卡错因边界质量扩量轮次报告

- input: 用户指出必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并要求质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、method_gap schema、方法卡登记表、wiki/index、wiki/log、Tutor 安全输入包、候选台账、M134 报告与本轮证据方法页。
- formal_cards_updated: 10 张正式卡补强错因边界或低置信 `method_gap`：[GS-212](http://127.0.0.1:8765/open/GS-212)、[GS-214](http://127.0.0.1:8765/open/GS-214)、[GS-215](http://127.0.0.1:8765/open/GS-215)、[GS-216](http://127.0.0.1:8765/open/GS-216)、[GS-217](http://127.0.0.1:8765/open/GS-217)、[GS-219](http://127.0.0.1:8765/open/GS-219)、[GS-220](http://127.0.0.1:8765/open/GS-220)、[GS-223](http://127.0.0.1:8765/open/GS-223)、[LA-101](http://127.0.0.1:8765/open/LA-101)、[LA-102](http://127.0.0.1:8765/open/LA-102)。
- metrics: N1 全库质量门从 M134 `warn_cards=58 warn_items=142` 降到 M135 `warn_cards=50 warn_items=130`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 38 降至 36；`error_causes placeholder/empty` 从 42 降至 32。
- validation: 10 张目标卡逐题质量门均为 `quality_gate=ok`，LA-101、LA-102 仅保留设计型 visual warning；`wrongnet.py rebuild` 成功，cards=777 strong=2274 medium=489 weak_audit=291；wiki coverage 已刷新，source summaries=777、compiled=767、knowledge_clusters=412、method_clusters=1358、error_clusters=423、action_gap_clusters=9；全库扫描结果 `/tmp/kaoyan_math_m135_post_scan.json`。
- expansion: 本轮未新增或推进候选；当前候选缺用户本人错因、正式化确认或人工重连授权，不为配额伪造状态。
- tutor: Tutor 技能已读取并检查安全输入包与 StudyVault dashboard；本轮没有新增 Tutor 训练包，不启动 quiz，不反写错题卡或回滚掌握度。
- boundary: 本轮未修改回滚 JSON；未修改掌握度；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-136 旧批量残余 warning 错因边界与 method_gap 收口报告

- input: 承接用户要求继续提高错题库质量，并明确要求读取相关 skill 后落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、method_gap schema、质量门脚本、wiki/index、wiki/log、M135 报告与本轮证据方法页。
- formal_cards_updated: 11 张正式卡补强错因边界或低置信 `method_gap`：[GS-125](http://127.0.0.1:8765/open/GS-125)、[GS-281](http://127.0.0.1:8765/open/GS-281)、[GS-286](http://127.0.0.1:8765/open/GS-286)、[GS-291](http://127.0.0.1:8765/open/GS-291)、[GS-341](http://127.0.0.1:8765/open/GS-341)、[GS-344](http://127.0.0.1:8765/open/GS-344)、[GS-425](http://127.0.0.1:8765/open/GS-425)、[LA-004](http://127.0.0.1:8765/open/LA-004)、[LA-019](http://127.0.0.1:8765/open/LA-019)、[LA-051](http://127.0.0.1:8765/open/LA-051)、[PR-001](http://127.0.0.1:8765/open/PR-001)。
- metrics: N1 全库质量门从 M135 `warn_cards=50 warn_items=130` 降到 M136 `warn_cards=42 warn_items=111`；`error_cards=0 error_items=0`；`method_gap not enabled` 从 36 降至 26；`error_causes placeholder/empty` 从 32 降至 24。
- validation: 11 张目标卡逐题质量门全部 `quality_gate=ok`；`wrongnet.py rebuild` 成功，cards=777 strong=2274 medium=488 weak_audit=291；wiki 覆盖层已刷新，source summaries=777、compiled=767、knowledge_clusters=412、method_clusters=1358、error_clusters=430、action_gap_clusters=9、missing_method=3、missing_error=24、missing_action_gap=26；全库扫描结果 `/tmp/kaoyan_math_m136_post_scan.json`。
- skipped: 剩余项多为设计型视觉缺口、讲义总纲/OCR 待确认卡或重复占位卡；不为降低 warning 伪造资产、用户错因或回滚状态。
- tutor: Tutor 技能已读取；本轮没有新增 Tutor 训练包，不启动 quiz，不反写错题卡、回滚 JSON 或掌握度。
- boundary: 本轮未修改回滚 JSON；未修改掌握度；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-137 旧批量占位错因证据边界收口报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并要求质量提升落实到正式错题卡修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、质量门脚本、wiki/index、wiki/log、候选台账与 M136 报告。
- formal_cards_updated: 24 张旧批量正式卡补强占位错因、占位陷阱和证据边界：[GS-349](http://127.0.0.1:8765/open/GS-349)、[GS-405](http://127.0.0.1:8765/open/GS-405)、[GS-408](http://127.0.0.1:8765/open/GS-408)、[GS-414](http://127.0.0.1:8765/open/GS-414)、[GS-426](http://127.0.0.1:8765/open/GS-426)、[GS-427](http://127.0.0.1:8765/open/GS-427)、[GS-428](http://127.0.0.1:8765/open/GS-428)、[GS-429](http://127.0.0.1:8765/open/GS-429)、[LA-005](http://127.0.0.1:8765/open/LA-005)、[LA-006](http://127.0.0.1:8765/open/LA-006)、[LA-024](http://127.0.0.1:8765/open/LA-024)、[LA-065](http://127.0.0.1:8765/open/LA-065)、[LA-066](http://127.0.0.1:8765/open/LA-066)、[LA-076](http://127.0.0.1:8765/open/LA-076)、[LA-077](http://127.0.0.1:8765/open/LA-077)、[LA-080](http://127.0.0.1:8765/open/LA-080)、[LA-083](http://127.0.0.1:8765/open/LA-083)、[LA-084](http://127.0.0.1:8765/open/LA-084)、[LA-085](http://127.0.0.1:8765/open/LA-085)、[LA-086](http://127.0.0.1:8765/open/LA-086)、[LA-095](http://127.0.0.1:8765/open/LA-095)、[LA-096](http://127.0.0.1:8765/open/LA-096)、[LA-107](http://127.0.0.1:8765/open/LA-107)、[LA-108](http://127.0.0.1:8765/open/LA-108)。
- metrics: N1 全库质量门保持 `error_cards=0 error_items=0`；`warn_items` 从 111 降到 72；`error_causes placeholder/empty` 从 24 降到 0；`traps placeholder/empty` 从 15 降到 0；coverage `missing_error` 从 24 降到 0。
- validation: 24 张目标卡逐题质量门均为 `ERROR 0`；`wrongnet.py rebuild` 成功，cards=777 strong=2278 medium=494 weak_audit=337；wiki coverage 已刷新，source summaries=777、compiled=769、knowledge_clusters=412、method_clusters=1358、error_clusters=433、action_gap_clusters=9、missing_method=3、missing_error=0、missing_action_gap=26；全库扫描结果 `/tmp/kaoyan_math_m137_post_scan.json`。
- expansion: 本轮未推进候选台账转正式卡；当前 confirmed/candidate 项仍缺用户本人错因、正式入库确认或正确解析，不为扩量指标伪造正式卡。
- tutor: Tutor 技能已读取；本轮没有新增 Tutor 安全训练包，不启动 quiz，不反写正式错题卡、回滚 JSON 或掌握度。
- boundary: 本轮未修改回滚 JSON；未修改掌握度；未手工编辑 `生成/`，派生文件仅由脚本刷新；仍保留 41 个设计型视觉缺口、26 个 method_gap 未启用项、3 个 methods 占位项和 2 个重复/占位卡复习日期缺口。

## [2026-07-05] maintenance | MATHWIKI-MAINT-138 已掌握卡 review.next 规范化与质量门复核报告

- input: 用户指出必须读取相关 skill，并要求错题质量提升落实到正式文件修改。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、质量门脚本、wiki/index、wiki/log、M137 报告与目标卡。
- formal_cards_updated: 12 张已掌握正式卡规范化 `review.next`：[GS-042](http://127.0.0.1:8765/open/GS-042)、[GS-059](http://127.0.0.1:8765/open/GS-059)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-135](http://127.0.0.1:8765/open/GS-135)、[GS-280](http://127.0.0.1:8765/open/GS-280)、[GS-448](http://127.0.0.1:8765/open/GS-448)、[GS-454](http://127.0.0.1:8765/open/GS-454)、[GS-473](http://127.0.0.1:8765/open/GS-473)、[GS-475](http://127.0.0.1:8765/open/GS-475)、[GS-482](http://127.0.0.1:8765/open/GS-482)、[GS-485](http://127.0.0.1:8765/open/GS-485)、[LA-003](http://127.0.0.1:8765/open/LA-003)。
- metrics: 全库质量门保持 `error_cards=0 error_items=0`；`review.next missing` 从 2 降到 0；`warn_items` 从 72 降到 70；剩余 warning 为 41 个设计型视觉缺口、26 个 method_gap 未启用项、3 个 methods 占位项。
- validation: 12 张目标卡逐题质量门均为 `quality_gate=ok`；`wrongnet.py rebuild` 成功，cards=777 strong=2278 medium=494 weak_audit=337；wiki coverage 已刷新，source summaries=777、compiled=730、knowledge_clusters=412、method_clusters=1358、error_clusters=433、action_gap_clusters=9；全库扫描结果 `/tmp/kaoyan_math_m138_post_scan.json`。
- expansion: 本轮不推进候选台账转正式卡；当前剩余候选仍缺用户本人错因、正式入库确认或正确解析，不为扩量指标伪造状态。
- tutor: Tutor 技能已读取；本轮没有新增 Tutor 安全训练包，不启动 quiz，不反写正式错题卡、回滚 JSON 或掌握度。
- boundary: 本轮未修改回滚 JSON；未修改掌握度；未手工编辑 `生成/`，派生文件仅由脚本刷新。

## [2026-07-05] maintenance | MATHWIKI-MAINT-139 已掌握抽测池机制固化与质量边界复核报告

- input: 用户要求继续提高错题库质量，并强调必须读取相关 skill 后落实到本地文件。
- skills_read: 已读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、项目规则、质量门脚本、wiki/index、wiki/log、候选台账、M138 报告与目标卡。
- quality_scan: M139 预扫描 `checked=777 error_cards=0 error_items=0 warn_cards=42 warn_items=70`；剩余 warning 为 41 个设计型视觉缺口、26 个 method_gap 未启用项、3 个 methods 占位项。
- boundary_review: 已复核 `GS-408`、`GS-414`、`LA-005` 三张 `methods` 占位卡，均存在 OCR 待核对、旧批量导入未记录个人错点或综合待精分边界，不强行补写；正式卡状态字段与 `related` 待补充项未发现需要修复的问题。
- wiki_updated: 新增 [MATHWIKI-REVIEW-001](错题知识网络/wiki/review/MATHWIKI-REVIEW-001_已掌握抽测池机制.md)，固化已掌握低频抽测池规则，并给出 [GS-018](http://127.0.0.1:8765/open/GS-018)、[GS-015](http://127.0.0.1:8765/open/GS-015)、[GS-318](http://127.0.0.1:8765/open/GS-318)、[GS-224](http://127.0.0.1:8765/open/GS-224)、[GS-441](http://127.0.0.1:8765/open/GS-441) 作为第一批低频抽测建议。
- formal_cards_updated: 0 张。本轮不修改正式错题卡，因为剩余项缺证据，继续硬填会牺牲入库质量。
- validation: 本轮未修改 `错题知识网络/错题卡/*.md`，不运行 `wrongnet.py rebuild`；写入后全库质量门复扫保持 `checked=777 error_cards=0 error_items=0 warn_cards=42 warn_items=70`，结果保存于 `/tmp/kaoyan_math_m139_post_scan.json`。
- tutor: Tutor 技能已读取；本轮不启动 quiz，不新增 Tutor 安全输入包，不反写正式错题卡、回滚 JSON 或掌握度。
- boundary: 本轮未修改回滚 JSON；未修改掌握度；未手工编辑 `生成/`；未推进候选台账转正式卡。

## [2026-07-05] maintenance | MATHWIKI-MAINT-140 候选用户确认清单与 Obsidian 可检索性复核报告

- input: 用户提醒必须读取 `LLM Wiki Lint` 与 `Tutor` skill，并要求错题质量提升落实到本地文件，而不是只查看。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`；同步读取长期目标、候选台账、wiki/index、wiki/log、M139 报告和 manifest 摘要。
- quality_scan: 预扫描 `checked=777 error_cards=0 error_items=0 warn_cards=42 warn_items=70`；remaining warning 为 41 个设计型视觉缺口、26 个 method_gap 未启用项、3 个 methods 占位项；`related` 为 `待补充` 的正式卡为 0。
- wiki_updated: 新增 [[错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-005_候选用户确认清单|MATHWIKI-QUESTIONS-005]]，把 `CAND-0001` 至 `CAND-0015` 的确认问题抽出为用户可直接回答的清单；更新 `MATHWIKI-QUESTIONS-004`、`wiki/index.md` 与本 log。
- formal_cards_updated: 0 张。本轮剩余候选缺用户本人错因、正确解析或迁移授权；不为扩量伪造正式错题卡。
- validation: 本轮未修改 `错题知识网络/错题卡/*.md`，不运行 `wrongnet.py rebuild`；`rg` 与 Obsidian CLI 已确认 `MATHWIKI-QUESTIONS-005`、`MATHWIKI-MAINT-140` 可检索；全库复扫保持 `checked=777 error_cards=0 error_items=0 warn_cards=42 warn_items=70`，结果为 `/tmp/kaoyan_math_m140_post_scan.json`。
- tutor: Tutor 技能已读取；本轮不启动 quiz，不新增 Tutor 安全输入包，不反写正式错题卡、回滚 JSON 或掌握度。
- boundary: 本轮未修改回滚 JSON；未修改掌握度；未手工编辑 `生成/`；候选状态未跳过用户确认。

## [2026-07-05] maintenance | MATHWIKI-MAINT-141 剩余质量门 warning 证据边界台账报告

- input: 用户要求必须读取相关 skill，并要求错题质量提升落实到本地文件，不接受只查看。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`obsidian-cli`，以及数学入库技能 `workflow.md`、`tutor-integration.md`、`output-template.md`；同步读取长期目标、M140 报告、manifest 与可视化索引。
- quality_scan: 正式 ID 口径逐卡复扫 `checked=777 error_cards=0 error_items=0 warn_cards=42 warn_items=70`；首次误扫 `README.md` 已排除并在 M141 报告中记录。
- wiki_updated: 新增 [[错题知识网络/wiki/lint_reports/MATHWIKI-LINT-001_剩余质量门warning证据边界台账|MATHWIKI-LINT-001]]，把 41 个设计型可视化缺口、26 个 `method_gap not enabled`、3 个 `methods` 占位项分流到可解除证据边界；新增本报告并更新 `wiki/index.md`。
- formal_cards_updated: 0 张。当前剩余 warning 缺真实题图、OCR、用户本人第一卡点或题目身份确认，继续硬填会降低错题质量。
- validation: 本轮未修改 `错题知识网络/错题卡/*.md`，不运行 `wrongnet.py rebuild`；写入前后正式 ID 口径复扫均为 `checked=777 error_cards=0 error_items=0 warn_cards=42 warn_items=70`，快照保存到 `/tmp/kaoyan_math_m141_pre_scan.json` 与 `/tmp/kaoyan_math_m141_post_scan.json`。
- tutor: Tutor 技能已读取；本轮只是 lint 边界台账，不启动 quiz，不新增 Tutor 安全输入包，不反写正式错题卡、回滚 JSON 或掌握度。
- boundary: 本轮未修改回滚 JSON；未修改掌握度；未手工编辑 `生成/`；不把证据不足项伪造成正式 method_gap 或方法标签。

## [2026-07-05] maintenance | MATHWIKI-MAINT-142 候选确认入口可点击化与 N5 操作化报告

- input: 用户要求必须读取相关 skill，并继续把错题质量提升落实到本地文件；本轮承接 M141 的证据边界与候选确认清单。
- skills_read: 已重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor` 与长期目标文件；同步读取候选确认清单、候选台账、manifest 摘要、wiki/index、wiki/log 与 M141 报告。
- quality_scan: 正式 ID 口径逐卡复扫 `checked=777 error_cards=0 error_items=0 warn_cards=42 warn_items=70`，快照保存到 `/tmp/kaoyan_math_m142_post_scan.json`。
- wiki_updated: 更新 [[错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-005_候选用户确认清单|MATHWIKI-QUESTIONS-005]]，把 `CAND-0001` 至 `CAND-0015` 全部改为可点击的 Obsidian 视觉详情入口，并新增快速确认模板；新增本报告并更新 `wiki/index.md`。
- formal_cards_updated: 0 张。候选仍缺用户本人错因、正确解析、主入口确认或迁移授权，不跳过 confirmed 状态直接 formal。
- validation: 已用文本检索确认 15 个 `视觉详情` 链接存在；本轮未修改 `错题知识网络/错题卡/*.md`，不运行 `wrongnet.py rebuild`。
- tutor: Tutor 技能已读取；本轮是候选操作页维护，不启动 quiz，不新增 Tutor 安全输入包，不反写正式错题卡、回滚 JSON 或掌握度。
- boundary: 本轮未修改回滚 JSON；未修改掌握度；未手工编辑 `生成/`；不把候选题图或解析当成用户个人错因。

## [2026-07-05] maintenance | MATHWIKI-MAINT-143 候选确认第一批执行单与 N5 分批推进报告

- input: 继续当前长期目标；本轮先读取目标文件、`kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`obsidian-cli` 和数学 FULL PATH 项目规则。
- quality_scan: 正式 ID 口径逐卡复扫 `checked=777 error_cards=0 error_items=0 warn_cards=42 warn_items=70`，快照保存到 `/tmp/kaoyan_math_m143_post_scan.json`。
- wiki_updated: 新增 [[错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-006_候选确认第一批执行单|MATHWIKI-QUESTIONS-006]]，把 15 个待用户确认入口压缩为第一批 5 个决策位；更新 `MATHWIKI-QUESTIONS-004`、`MATHWIKI-QUESTIONS-005`、本报告与 `wiki/index.md`。
- formal_cards_updated: 0 张。第一批候选仍缺本人错因、迁移授权、主入口选择或正确解析，不直接 formal。
- validation: 本轮未修改 `错题知识网络/错题卡/*.md`，不运行 `wrongnet.py rebuild`；已用文本检索与 Obsidian CLI 检查 Q006、M143、第一批候选入口可检索。
- tutor: Tutor 技能已读取；本轮是候选执行单维护，不启动 quiz，不新增 Tutor 安全输入包，不反写正式错题卡、回滚 JSON 或掌握度。
- boundary: 本轮未修改回滚 JSON；未修改掌握度；未手工编辑 `生成/`；不把候选视觉材料当成用户个人错因。

## [2026-07-05] maintenance | MATHWIKI-MAINT-144 候选正式化前置检查清单与 N5 执行边界报告

- input: 用户提醒必须读取相关 skill；本轮重新读取 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`obsidian-cli` 和数学 FULL PATH 项目规则后继续推进。
- quality_scan: 正式 ID 口径逐卡复扫 `checked=777 error_cards=0 error_items=0 warn_cards=42 warn_items=70`，快照保存到 `/tmp/kaoyan_math_m144_post_scan.json`。
- wiki_updated: 新增 [[错题知识网络/wiki/questions/MATHWIKI-QUESTIONS-007_候选正式化前置检查清单|MATHWIKI-QUESTIONS-007]]，把第一批 5 个确认位的正式化前置查重、预检和禁止动作写成执行边界；更新 `MATHWIKI-QUESTIONS-004`、`MATHWIKI-QUESTIONS-005`、`MATHWIKI-QUESTIONS-006`、本报告与 `wiki/index.md`。
- formal_cards_updated: 0 张。候选仍缺用户本人错因、迁移授权、主入口选择或正确解析，不跳过 confirmed 状态直接 formal。
- validation: 本轮未修改 `错题知识网络/错题卡/*.md`，不运行 `wrongnet.py rebuild`；已用文本检索和 Obsidian CLI 检查 Q007、M144、Q006、Q005、Q004 可检索。
- tutor: Tutor 技能已读取；本轮是候选正式化前置清单维护，不启动 quiz，不新增 Tutor 安全输入包，不反写正式错题卡、回滚 JSON 或掌握度。
- boundary: 本轮未修改回滚 JSON；未修改掌握度；未手工编辑 `生成/`；不把候选题图、解析或 OCR 当作用户个人错因。

## [2026-07-05] maintenance | MATHWIKI-MAINT-145 已掌握抽测第二批与 N7 轮次报告

- input: 用户再次提醒必须读取相关 skill；本轮按 `kaoyan-math-wrong-intake`、`LLM Wiki Lint`、`Tutor`、`obsidian-cli` 规则继续推进长期质量目标。
- quality_scan: 正式 ID 口径逐卡复扫 `checked=777 error_cards=0 error_items=0 warn_cards=42 warn_items=70`，快照保存到 `/tmp/kaoyan_math_m145_post_scan.json`。
- wiki_updated: 新增 [[错题知识网络/wiki/review/MATHWIKI-REVIEW-002_已掌握抽测第二批执行单|MATHWIKI-REVIEW-002]]，给出 [GS-022](http://127.0.0.1:8765/open/GS-022)、[GS-090](http://127.0.0.1:8765/open/GS-090)、[GS-092](http://127.0.0.1:8765/open/GS-092)、[GS-436](http://127.0.0.1:8765/open/GS-436)、[GS-432](http://127.0.0.1:8765/open/GS-432) 第二批已掌握低频抽测入口；更新 `MATHWIKI-REVIEW-001`、本报告与 `wiki/index.md`。
- formal_cards_updated: 0 张。本轮推进 N7，不修改正式错题卡，不把抽测建议写成新的错因或掌握度。
- validation: 本轮未修改 `错题知识网络/错题卡/*.md`，不运行 `wrongnet.py rebuild`；已用文本检索和 Obsidian CLI 检查 REVIEW-002、M145 可检索。
- tutor: Tutor 技能已读取；本轮是抽测执行单维护，不启动 quiz，不新增 Tutor 安全输入包，不反写正式错题卡、回滚 JSON 或掌握度。
- boundary: 本轮未修改回滚 JSON；未修改掌握度；未手工编辑 `生成/`；`GS-107` 因与 `GS-092` 同题重复未重复列入抽测名额。

## [2026-07-05] ingest | 高数第18讲多元函数积分学预处理

- input: 用户提供《高数十八讲》第十八讲多元函数积分学学习任务、预处理包 zip 与三份高数讲义 PDF；用户明确说明材料内现有编号不是正式编号，后续做题时另给实际编号。
- skills_read: 已读取 `llm-wiki-ingest`、`pdf`、`obsidian-cli`；同步读取数学 README、错题知识网络 README、AI维护规则、ingest/query/lint/decision matrix/page template/Karpathy wiki 规则、wiki/index 与 wiki/log。
- source_processed: 解包并读取 `/tmp/kaoyan_math_h18_pre/高数第18讲_多元函数积分学_Codex预处理文档.md`、`method_cards_h18.json`、`examples_candidates_do_not_import.jsonl`；本轮没有对三份 PDF 做整本抽取，只保留来源路径用于后续核对。
- wiki_created: 新增 [[SRC-H18-MULTI-INTEGRAL_高数第18讲多元函数积分学预处理包]]、[[MATHWIKI-GS-OVERVIEW-002_第18讲多元函数积分学学习总览]]、[[MATHWIKI-GS-METHOD-102_第18讲多元积分方法卡总表]]、[[MATHWIKI-QUESTIONS-008_第18讲多元积分例题候选索引]]，并新增 `错题知识网络/知识树/高等数学18讲第18讲_多元函数积分学.md`。
- data_summary: 识别例题候选 66 条，其中《基础30讲》30 条、《高数18讲》36 条；高频方法卡为 `H18-013` 11 次、`H18-006` 10 次、`H18-014` 9 次、`H18-003` 8 次、`H18-008` 6 次、`H18-010` 6 次。
- boundary: 所有候选保持 `DO_NOT_IMPORT_AS_WRONG_QUESTION_YET`；临时号 `B30-18.x`、`H18-18.x`、`LM35-x` 仅用于讲义定位，不写成正式 `GS-*` 编号。
- formal_cards_updated: 0 张。本轮未修改 `错题知识网络/错题卡/*.md`，不运行 `wrongnet.py rebuild`。
- generated_updated: 0。本轮未手工编辑 `错题知识网络/生成/`。
- review_updated: 0。本轮未修改回滚 JSON、复习记录或掌握度。
- tutor: 本轮是学习前 wiki 预处理，不启动 Tutor quiz，不新增 Tutor 安全输入包。
- missing_info: 等待用户做题后提供实际正式编号、本人第一卡点、wrong_point、method_gap 判断和掌握度。

## [2026-07-05] formal-intake | GS-666 78292 轮换对称截面法

- 范围：[GS-666](http://127.0.0.1:8765/open/GS-666)、VIS-GS-666、SRC-WQ-GS-666。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-666_78292轮换对称截面法.md`；复制题图 1 张、解析/推导图 2 张；创建视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-666_78292轮换对称截面法.md`。
- 错点：第一次遇到第18讲三重积分时，没有先触发三变量轮换对称性；化为 `6∭z dV` 后，没有先固定 `z` 写截面边界 `x+y=1-z` 和面积 `1/2(1-z)^2`。
- 方法：三重积分轮换对称性（H18-003）+ 先二后一截面法/三重积分换序（H18-002）；关联旧卡 GS-403、GS-659。
- 验证：`intake_closeout.py --id GS-666 --source 78292 --knowledge 三重积分 --knowledge 多元函数积分学 --visual expected` 已通过；rebuild 成功 cards=778 strong=2276 medium=497 weak_audit=293；source summaries=778 compiled=770；bridge records=925 assets=1273；quality_gate=ok。
- Tutor：not_needed，本轮未新增 Tutor 安全输入包；本题已接入第18讲方法页和 action gap 覆盖层，可作为后续方法错因训练目标。
- 边界：未手改 `生成/`；未修改回滚 JSON；未默认输出旧题复做推荐；掌握度为 2026-07-05 AI评分 2/5，依据用户口述初始无法着手、讲解后能复述但待独立复做。

## [2026-07-05] formal-intake | GS-666 78292 轮换对称截面法 Obsidian公式修正

- 范围：[GS-666](http://127.0.0.1:8765/open/GS-666)、VIS-GS-666、SRC-WQ-GS-666。
- 修正：按 Obsidian Markdown 数学语法，将正式卡正文、frontmatter 可见字段和视觉详情页折叠解析中的 `\[` / `\]`、`\(...\)` 改为 `$$...$$` 与 `$...$`，修复公式在 Obsidian 中按纯文本显示的问题。
- 验证：已确认 `GS-666` 正式卡和视觉详情页无残留 `\[`、`\]`、`\(`、`\)`；重新运行 `intake_closeout.py --id GS-666 --source 78292 --knowledge 三重积分 --knowledge 多元函数积分学 --visual expected`，quality_gate=ok，ERROR none，WARN none。
- 边界：本次只修 Markdown 渲染格式，不改变题目事实、错点、知识点、掌握度、关联旧题或回滚 JSON。

## [2026-07-06] formal-intake | GS-667 102412 圆柱抛物面极坐标

- 范围：[GS-667](http://127.0.0.1:8765/open/GS-667)、VIS-GS-667、SRC-WQ-GS-667。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-667_102412圆柱抛物面极坐标.md`；复制题图 1 张、解析/区域图 2 张；创建视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-667_102412圆柱抛物面极坐标.md`。
- 错点：没有先把圆柱面投影写成 `D:x^2+(y-1)^2<=1` 并确定 `0<=z<=(x^2+y^2)/8`；转极坐标时未推出 `0<=theta<=pi, 0<=r<=2sin(theta)`；收尾漏用 `sin^5(theta)` 在 `[0,pi]` 上的对称性。
- 方法：三重积分投影/高度拆分（H18-002）+ 柱面坐标（H18-004）+ 二重积分极坐标法（H14-005）；关联旧卡 GS-666、GS-400、GS-409。
- Tutor：updated，已在安全输入包新增“三重积分柱面投影训练项”，只记录高层第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-667 --source 102412 --knowledge 多元函数积分学 --knowledge 三重积分 --knowledge 柱面坐标 --knowledge 二重积分极坐标法 --visual expected` 已通过；rebuild 成功 cards=779 strong=2279 medium=496 weak_audit=293；source summaries=779 compiled=770；bridge records=926 assets=1276；quality_gate=ok。
- 边界：不手改 `生成/`；不修改回滚 JSON；不启动 Tutor quiz；不默认输出旧题复做推荐；掌握度为 2026-07-06 AI评分 2/5，依据用户口述区域图像、极坐标上下限和三角幂积分收尾均需看答案后才明白。

## [2026-07-06] formal-intake | GS-668 102610 球体截面球面坐标

- 范围：[GS-668](http://127.0.0.1:8765/open/GS-668)、VIS-GS-668、方法页 `MATHWIKI-GS-METHOD-102_第18讲多元积分方法卡总表`。
- 写入：新增正式错题卡 `GS-668_102610球体截面球面坐标.md`；复制题图 1 张、解析/手写图 2 张；创建视觉详情页 `GS-668_102610球体截面球面坐标.md`，题图直接显示、解析默认折叠。
- 错点：先二后一法中没有由 `x^2+y^2=1-z^2` 对比圆标准式得出截面半径 `sqrt(1-z^2)`；计算中出现分子与分子误约分；球面坐标法中把 `[-cos φ]_0^π=-cosπ+cos0=2` 误算成 0。
- 方法：三重积分先二后一截面法（H18-002）+ 三重积分对称性（H18-003）+ 球面坐标（H18-005）；关联旧卡 GS-659、GS-666、GS-667。
- Tutor：updated，已在安全输入包新增“球体截面与球面坐标训练项”，只记录高层第一动作和计算提醒，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-668 --source 102610 --knowledge 多元函数积分学 --knowledge 三重积分 --knowledge 三重积分对称性 --knowledge 球面坐标 --knowledge 定积分 --visual expected` 已通过；rebuild 成功 cards=780 strong=2281 medium=496 weak_audit=293；source summaries=780 compiled=770；bridge records=927 assets=1279；quality_gate=ok。
- 边界：不手改 `生成/`；不修改回滚 JSON；不启动 Tutor quiz；不默认输出旧题复做推荐；掌握度为 2026-07-06 AI评分 2.5/5，依据用户口述截面半径识别、约分和三角函数定积分符号代入均有断点。

## [2026-07-06] formal-intake | GS-669 102438 圆锥面球面坐标

- 范围：[GS-669](http://127.0.0.1:8765/open/GS-669)、VIS-GS-669、SRC-WQ-GS-669。
- 写入：新增正式错题卡 `GS-669_102438圆锥面球面坐标.md`；复制题图 1 张、解析图 1 张；创建视觉详情页 `GS-669_102438圆锥面球面坐标.md`，题图直接显示、解析默认折叠。
- 错点：把 $z=\sqrt{x^2+y^2}$ / $x^2+y^2=z^2$ 误判为椭球面或球面类边界，按 $\varphi:0\to\frac{\pi}{2}$、$\rho:0\to1$ 设限；没有先识别上半圆锥面，并由 $\rho\sin\varphi\le\rho\cos\varphi$ 得到 $\varphi\le\frac{\pi}{4}$，再由 $z=1$ 得到 $\rho\le\frac1{\cos\varphi}$。
- 方法：球面坐标（H18-005）+ 圆锥面识别 + 极角范围确定；关联旧卡 GS-668、GS-667、GS-666、GS-651。
- Tutor：updated，已在安全输入包新增“圆锥面与球面坐标极角训练项”，只记录高层第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-669 --source 102438 --knowledge 多元函数积分学 --knowledge 三重积分 --knowledge 球面坐标 --knowledge 二次曲面 --knowledge 向量代数与空间解析几何 --visual expected` 已通过；rebuild 成功 cards=781 strong=2287 medium=496 weak_audit=293；source summaries=781 compiled=770；bridge records=928 assets=1281；quality_gate=ok。
- 边界：不手改 `生成/`；不修改回滚 JSON；不启动 Tutor quiz；不默认输出旧题复做推荐；掌握度为 2026-07-06 AI评分 2/5，依据用户口述本题主要断点是圆锥面/椭球面判型混淆并导致球面坐标设限整体错误。

## [2026-07-06] formal-intake | GS-670 102450 椭球伸缩换元球面坐标

- 范围：正式入库 `GS-670`，题目来源为 ID:102450 / 用户截图与答案图 / 2026-07-06。
- 错点：看到 $x^2+4y^2+z^2\le1$ 与同形被积函数时，没有先把 $4y^2$ 写成 $(2y)^2$，令 $u=x,\ v=2y,\ w=z$，把椭球化成单位球；同时没有同步补雅可比因子 $\frac12$ 并进入球面坐标。
- 方法断点：B3-METHOD；expected_first_action 为先写 $u=x,\ v=2y,\ w=z$；关联方法卡 `H18-016`，同时关联第18讲多元积分方法总表和球面坐标链。
- 更新：新增正式错题卡、视觉详情页、图片资产登记、Tutor 安全输入包训练项；运行 closeout 完成 rebuild、wiki coverage、bridge refresh、related/knowledge 查询和质量门。

## [2026-07-07] formal-intake | GS-671 57959 对称拆区间判号

- 范围：[GS-671](http://127.0.0.1:8765/open/GS-671)、VIS-GS-671、SRC-WQ-GS-671。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-671_57959对称拆区间判号.md`；复制题图 1 张、解析图 1 张；创建视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-671_57959对称拆区间判号.md`。
- 错点：知道三角函数图像，也想到看被积函数正负和分部积分，但没有先把 `[-π,0]` 与 `[0,π]` 拆开并用 `x=-u` 统一到正半轴比较，未触发对称区间再现。
- 方法：区间拆分 + 对称换元 + 单调性比较；`cos x` 项先分部积分回到 `sin x` 权函数；method_gap 为 B2-TRIGGER，方法卡 H11-003。
- Tutor：updated，已在安全输入包新增“对称区间定积分判号”训练项，只记录高层第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-671 --source 57959 --knowledge 定积分 --knowledge 定积分性质 --knowledge 函数单调性 --knowledge 分部积分 --visual expected` 已通过；cards=783，strong=2297，medium=494，weak_audit=293；bridge records=930，assets=1285；quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-07 AI评分 3/5，依据用户口述计算没问题但关键对称换元入口未触发。

## [2026-07-07] formal-intake | GS-672 112866 极坐标面积极限和

- 范围：[GS-672](http://127.0.0.1:8765/open/GS-672)、VIS-GS-672、SRC-WQ-GS-672。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-672_112866极坐标面积极限和.md`；复制题图 1 张、答案图 1 张；创建视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-672_112866极坐标面积极限和.md`。
- 错点：没有先调用极坐标面积微元 $dA=\frac12r^2d\theta$，也没有把定积分定义中的 $\Delta\theta$ 理解为每项必须乘上的小宽度；误把重点放在是否知道“螺线”名称。
- 方法：极坐标面积公式 + 定积分定义/黎曼和；method_gap 为 A+B混合、B3-METHOD，方法卡 H10-001，关联 H08-001。
- Tutor：updated，已在安全输入包新增“极坐标面积极限和”训练项，只记录高层第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-672 --source 112866 --knowledge 极坐标面积微元 --knowledge 平面图形面积 --knowledge 定积分 --knowledge 定积分应用 --knowledge 微元法建模 --knowledge 定积分定义 --knowledge 黎曼和 --visual expected` 已通过；cards=784，strong=2304，medium=490，weak_audit=293；bridge records=931，assets=1287；quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-07 AI评分 2.5/5，依据用户口述公式储备和“高乘宽”定义链条需讲解后才能串起来。

## [2026-07-07] formal-intake | GS-673 58087 积分主部替换判阶

- 范围：[GS-673](http://127.0.0.1:8765/open/GS-673)、VIS-GS-673、SRC-WQ-GS-673。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-673_58087积分主部替换判阶.md`；复制题图 1 张、解析图 1 张；创建视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-673_58087积分主部替换判阶.md`。
- 错点：没有先设 `g(x)=∫_0^x f(t)dt` 并由 `f(0)=0, f'(0)=6` 得 `f(t)~6t`、`g(x)~3x^2`；直接比较 `f` 与 `g` 并反复套洛必达，导致没有把问题化成 `g(x^3)` 与 `[g(x)]^3` 的主部比较。
- 方法：一阶线性主部 + 等价无穷小 + 积分主部 + 无穷小阶数比较；method_gap 为 B3-METHOD，方法卡 H01-004、H11-008；关联旧卡 GS-547、GS-579、GS-585、GS-127、GS-440。
- Tutor：updated，已在安全输入包新增“积分主部替换判阶”训练项，只记录高层第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-673 --source 58087 --knowledge 极限与连续 --knowledge 等价无穷小 --knowledge 无穷小阶数比较 --knowledge 一阶线性主部 --knowledge 定积分 --knowledge 变上限积分 --knowledge 洛必达法则 --visual expected` 已通过；cards=785，strong=2310，medium=488，weak_audit=293；bridge records=932，assets=1289；quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-07 AI评分 3/5，依据用户口述看懂解析但初始没有触发主部替换入口。

## [2026-07-07] formal-intake | GS-674 193302 倒代换合并积分值域

- 范围：[GS-674](http://127.0.0.1:8765/open/GS-674)、VIS-GS-674、SRC-WQ-GS-674。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-674_193302倒代换合并积分值域.md`；复制题图 1 张、解析图 1 张；创建视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-674_193302倒代换合并积分值域.md`。
- 错点：看到两个同形积分上限分别为 `x` 与 `1/x` 时，没有先对第二个积分作 `t=1/u` 倒代换统一到上限 `x`，而是只看 `x->0+` 一端趋势；该趋势只能说明无上界，不能得到完整值域。
- 方法：定积分等式入口（H11-001）+ 倒代换/第一类换元（H09-002）+ 值域收尾（H05-006）；关联旧卡 GS-174、GS-186、GS-191、GS-297、GS-671。
- Tutor：updated，已在安全输入包新增“倒代换合并积分值域”训练项，只记录高层第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-674 --source 193302 --knowledge 定积分 --knowledge 定积分等式 --knowledge 变上限积分 --knowledge 第一类换元 --knowledge 一元函数积分学的计算 --knowledge 单调性与极值 --visual expected` 已通过；cards=786，strong=2317，medium=486，weak_audit=293；bridge records=933，assets=1291；quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-07 AI评分 3/5，依据用户口述看懂换元合并和值域路线，但初始未触发倒代换入口。

## [2026-07-07] formal-intake | GS-675 57721 对数反常积分瑕点判敛

- 范围：[GS-675](http://127.0.0.1:8765/open/GS-675)、VIS-GS-675、SRC-WQ-GS-675。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-675_57721对数反常积分瑕点判敛.md`；复制题图 1 张、解析图 1 张；创建视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-675_57721对数反常积分瑕点判敛.md`。
- 错点：只分析了 `x->+∞` 时对数因子让分母更大，没有先检查下端点 `x=1` 处 `ln x=0` 导致的有限瑕点；应先拆 `[1,e]` 与 `[e,+∞)` 两段分别判敛。
- 方法：反常积分判敛（H08-005）+ 找反常点 + 等价比较 + p型判敛；关联旧卡 GS-580、GS-582、GS-581、GS-180、GS-177。
- Tutor：updated，已在安全输入包新增“对数反常积分瑕点判敛”训练项，只记录高层第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-675 --source 57721 --knowledge 反常积分 --knowledge 对数型积分 --knowledge 等价无穷小 --knowledge 比较判别法 --knowledge 极限比较判别法 --visual expected` 已通过；cards=787，strong=2323，medium=485，weak_audit=296；bridge records=934，assets=1293；quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-07 AI评分 3/5，依据用户口述无穷远处比较思路对，但初始漏查 `x=1` 瑕点。

## [2026-07-07] formal-intake | GS-676 170671 幂型反常积分瑕点判敛

- 范围：[GS-676](http://127.0.0.1:8765/open/GS-676)、VIS-GS-676。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-676_170671幂型反常积分瑕点判敛.md`；复制题图 1 张、解析图 1 张；创建视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-676_170671幂型反常积分瑕点判敛.md`。
- 错点：把 `arctan0` 和 `2+0^p` 都有定义当作 0 点正常，漏看 `x^{1-p}` 在 `p>1` 时会变成 `1/x^{p-1}`，应先拆 `0^+` 与 `+∞` 两段分别判敛。
- 方法：反常积分判敛（H08-005）+ 找反常点 + 等价比较 + p型判敛；关联旧卡 GS-675、GS-580、GS-582、GS-581、GS-180。
- Tutor：updated，已在安全输入包新增“幂型反常积分瑕点判敛”训练项，只记录高层第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-676 --source 170671 --knowledge 反常积分 --knowledge 等价无穷小 --knowledge 比较判别法 --knowledge 极限比较判别法 --visual expected` 已通过；cards=788，strong=2328，medium=485，weak_audit=296；bridge records=935，assets=1295；quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-07 AI评分 3/5，依据用户口述已理解 0 点瑕点来源，但初始漏查参数指数导致的端点风险。

## [2026-07-07] formal-intake | GS-677 81447 根式反常积分原函数

- 范围：[GS-677](http://127.0.0.1:8765/open/GS-677)、VIS-GS-677、SRC-WQ-GS-677。
- 写入：正式卡 `错题知识网络/错题卡/GS-677_81447根式反常积分原函数.md`；复制题图 1 张、解析图 1 张；创建视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-677_81447根式反常积分原函数.md`。
- 错点：没有先把两个简单积分项分别求原函数，而是通分后卡住；并且忘记 `∫dx/√(x^2+a^2)=ln(x+√(x^2+a^2))+C` 的根式积分基本公式。
- 方法：线性拆项 + 根式积分对数原函数 + 对数差整体取反常极限；method_gap 为 A+B混合、B3-METHOD，方法卡 H09-001，联动 H08-005 与 MATHWIKI-GS-METHOD-043。
- Tutor：updated，已在安全输入包新增“根式反常积分原函数”训练项，只记录高层第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-677 --source 81447 --knowledge 反常积分 --knowledge 一元函数积分学的计算 --knowledge 不定积分 --knowledge 根式积分 --knowledge 对数型积分 --visual expected` 已通过；cards=789，strong=2334，medium=485，weak_audit=304；bridge records=936，assets=1297；quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-07 AI评分 2/5，依据用户口述核心原函数公式完全遗忘且第一动作误走通分。

## [2026-07-07] formal-intake | GS-678 57857 平移换元变限极限

- 范围：[GS-678](http://127.0.0.1:8765/open/GS-678)、VIS-GS-678、SRC-WQ-GS-678。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-678_57857平移换元变限极限.md`；复制题图 1 张、解析图 1 张；创建视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-678_57857平移换元变限极限.md`。
- 错点：没有先令 `u=t+Δx`，把 `f(t+Δx)` 里的函数内部平移转成积分上下限平移；因此没能把原式化为关于 `Δx` 的变限积分差并用莱布尼茨法则求导。
- 方法：定积分换元 + 区间平移 + 变限积分求导；method_gap 为 B3-METHOD，方法卡 H09-008，联动 `MATHWIKI-GS-METHOD-054`。
- Tutor：updated，已在安全输入包新增“平移换元变限极限”训练项，只记录高层触发词和第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-678 --source 57857 --knowledge 函数极限 --knowledge 定积分 --knowledge 变限积分 --knowledge 第一类换元 --visual expected` 已通过；cards=790，strong=2339，medium=484，weak_audit=305；source summaries=790，compiled=778；bridge records=937，assets=1299；quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-07 AI评分 3/5，依据用户口述已理解换元后求导主线，但初始没有触发换元入口。

## [2026-07-07] formal-intake | GS-679 193323 对数导数微分方程

- 范围：[GS-679](http://127.0.0.1:8765/open/GS-679)、VIS-GS-679、SRC-WQ-GS-679。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-679_193323对数导数微分方程.md`；复制题图 1 张、解析图 1 张；创建视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-679_193323对数导数微分方程.md`。
- 错点：已推到 $\frac{f'}{f}=\frac{\sin x-x\cos x}{x\sin x}$，但没有把它识别成对数导数/可分离变量微分方程；漏掉先拆成 $\frac1x-\cot x$ 后积分求通解。
- 方法：幂指极限取对数 + 自变量增量匹配 + 导数定义 + 对数导数微分方程；method_gap 为 B4-CHAIN，方法卡 H15-002，联动 `MATHWIKI-GS-METHOD-073`、`MATHWIKI-GS-METHOD-013`、`MATHWIKI-GS-METHOD-056`。
- Tutor：updated，已在安全输入包新增“对数导数微分方程”训练项，只记录高层触发词和第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-679 --source 193323 --knowledge ... --visual expected` 已通过；cards=791，strong=2345，medium=485，weak_audit=305；source summaries=791，compiled=779；bridge records=938，assets=1301；quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-07 AI评分 3.5/5，依据用户口述前面推导基本会，断点集中在对数导数微分方程通解求法。

## [2026-07-08] formal-intake | GS-680 57968 双纽线极坐标面积

- 范围：[GS-680](http://127.0.0.1:8765/open/GS-680)、VIS-GS-680、SRC-WQ-GS-680。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-680_57968双纽线极坐标面积.md`；复制题图 1 张、解析图 1 张；创建视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-680_57968双纽线极坐标面积.md`。
- 错点：计算没问题，但没有把“面积=$\iint_D1\,dA$”、极坐标面积元 $dA=r\,dr\,d\theta$、坐标轴对称和 $r^2=\cos2\theta\ge0$ 的角域限制连成一条链。
- 方法：极坐标化边界 + 对称性判断 + 角域非负性检查 + 极坐标面积微元；method_gap 为 A+B混合、B4-CHAIN，方法卡 H10-001，联动 H14-005、GS-672、GS-410。
- Tutor：updated，已在安全输入包新增“极坐标面积与角域判定”训练项，只记录高层触发词和第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-680 --source 57968 --knowledge ... --visual expected` 已通过；cards=792，strong=2349，medium=486，weak_audit=305；source summaries=792；bridge records=939，assets=1303；quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-08 AI评分 3/5，依据用户口述计算能跟上但面积微元、对称性和角域判定需连续追问。

## [2026-07-08] formal-intake | GS-681 193347 心形线极坐标弧长

- 范围：[GS-681](http://127.0.0.1:8765/open/GS-681)、VIS-GS-681、SRC-WQ-GS-681。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-681_193347心形线极坐标弧长.md`；复制题图 1 张、解析图 1 张；创建并补齐视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-681_193347心形线极坐标弧长.md`。
- 错点：能理解完整周期 `0≤θ≤2π`，但没有先由 `r(θ)=r(2π-θ)` 验证极轴对称并把全长压成 `2∫_0^π ds`；计算时把 `r'` 误写成 `1-sinθ`，并忘记 `1+cosθ=2cos²(θ/2)`。
- 方法：极坐标弧长公式 + 周期与极轴对称定积分限 + 常数项求导检查 + 半角公式根式化简；method_gap 为 A+B混合、B4-CHAIN，方法卡 H10-003，联动 `MATHWIKI-GS-METHOD-082`、GS-595、GS-644、GS-680。
- Tutor：updated，已在安全输入包新增“极坐标弧长与对称积分限”训练项，只记录高层触发词和第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-681 --source 193347 --knowledge 定积分 --knowledge 定积分应用 --knowledge 曲线弧长 --knowledge 极坐标 --knowledge 三角恒等变形 --knowledge 半角公式 --visual expected` 已通过；cards=793，strong=2355，medium=485，weak_audit=305；source summaries=793，compiled=781；bridge records=940，assets=1305；quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-08 AI评分 3/5，依据用户口述弧长主公式能跟上，但积分限对称性、常数项求导和半角公式需讲解后才能串起来。

## [2026-07-08] formal-intake | GS-682 170719 极坐标转参数弧长

- 范围：[GS-682](http://127.0.0.1:8765/open/GS-682)、VIS-GS-682、SRC-WQ-GS-682。
- 写入：新增正式卡 `错题知识网络/错题卡/GS-682_170719极坐标转参数弧长.md`；复制题图 1 张、解析图 1 张；创建并补齐视觉详情页 `错题知识网络/可视化错题详情/高等数学/GS-682_170719极坐标转参数弧长.md`。
- 错点：看到 $\theta=\frac12(r+\frac1r)$ 且 $r\in[1,3]$ 时，没有先把 $r$ 当参数代入 $x=r\cos\theta,\ y=r\sin\theta$，转成参数方程后套弧长公式；后续平方相加又漏掉 $\cos^2\theta+\sin^2\theta=1$。
- 方法：曲线表达形式判断 + 极坐标转参数方程 + 参数方程弧长公式 + 平方和化简；method_gap 为 A+B混合、B3-METHOD，方法卡 H10-003，联动 `MATHWIKI-GS-METHOD-015`、`MATHWIKI-GS-METHOD-082`、GS-469、GS-595、GS-644、GS-681。
- Tutor：updated，已在安全输入包新增“theta=f(r) 极坐标关系转参数弧长”训练项，只记录高层触发词和第一动作，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-682 --source 170719 --knowledge 定积分 --knowledge 定积分应用 --knowledge 曲线弧长 --knowledge 极坐标 --knowledge 参数方程 --knowledge 参数方程求导 --knowledge 三角恒等变形 --visual expected` 已通过；cards=794，strong=2360，medium=485，weak_audit=305；source summaries=794，compiled=782；bridge records=941，assets=1307；quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-08 AI评分 2.5/5，依据用户口述主断点是概念入口未触发，同时平方和化简漏项。

## [2026-07-08] formal-intake | GS-683 193283 反函数求导收尾

- 范围：[GS-683](http://127.0.0.1:8765/open/GS-683)、VIS-GS-683。
- 写入：正式卡 / 图片资产 / 视觉详情页（题图可见、解析折叠）。
- 错点：已求出 f(1)=3、g(3)=1、f'(1)=1，但最后忘记反函数求导法则 g'(f(x0))=1/f'(x0)，导致 g'(3) 没有收尾；method_gap=B6-CLOSE，联动 H04-008。
- Tutor：updated（只写高层触发词和第一动作，不复制题干）。
- 验证：intake_closeout --id GS-683 --source 193283 --knowledge 一元函数微分学应用 --knowledge 反函数求导 --knowledge 变上限积分 --knowledge 复合函数求导 --visual expected 已通过；cards=795，related 强关联 GS-124/GS-283/GS-526/GS-678/GS-679；quality_gate=ok。
- 边界：不手改 生成/；不改回滚 JSON；掌握度 AI评分 3.5/5。

## [2026-07-08] formal-intake | GS-684 58093 分部积分降阶

- 范围：[GS-684](http://127.0.0.1:8765/open/GS-684)、VIS-GS-684、SRC-WQ-GS-684。
- 写入：正式卡 / 图片资产 / 视觉详情页（题图可见、解析折叠）。
- 错点：想到分部积分但没有落笔把 $f''(2x)dx$ 写成 $\frac12d(f'(2x))$ 做降阶，转去 Taylor 局部展开。
- Tutor：updated（只写高层触发词和第一动作，不复制题干）。
- 验证：intake_closeout --id GS-684 --source 58093 --knowledge 定积分 --knowledge 分部积分 --knowledge 一元函数积分学的计算 --knowledge 复合函数求导 --knowledge 第一类换元 --visual expected 已通过；quality_gate=ok。
- 边界：不手改 生成/；不改回滚 JSON；掌握度 AI评分 3/5。

## [2026-07-10] formal-intake | GS-685 194435 复合函数边界代入

- 范围：[GS-685](http://127.0.0.1:8765/open/GS-685)、VIS-GS-685、MATHWIKI-GS-METHOD-074。
- 写入：正式卡 / 图片资产 / 视觉详情页（题图可见、解析折叠）/ 边界项复查方法页 / Tutor 安全训练增量。
- 错点：分部积分边界项代入 x=1 时漏算内层 2x=2，把 f(2) 看成 f(1)；method_gap 为 B7-CALC，关联方法卡 H11-005。
- Tutor：updated（只写复合函数边界项三层代入触发词与第一动作，不复制题干）。
- 验证：intake_closeout --id GS-685 --source 194435 --knowledge 导数定义 --knowledge 导数定义型极限 --knowledge 等价无穷小 --knowledge 复合自变量 --knowledge 不定积分 --knowledge 定积分 --knowledge 分部积分 --knowledge 一元函数积分学的计算 --knowledge 复合函数求导 --visual expected 已通过；cards=797；Obsidian bridge records=944，assets=1313；强关联 GS-035、GS-601、GS-639、GS-684；quality_gate=ok。
- 边界：不手改 生成/；不改回滚 JSON；掌握度 AI评分 4/5。

## [2026-07-10] formal-intake | GS-686 57726 分母平方分部降幂

- 范围：[GS-686](http://127.0.0.1:8765/open/GS-686)、VIS-GS-686、SRC-WQ-GS-686、MATHWIKI-GS-METHOD-076、MATHWIKI-GS-METHOD-074。
- 写入：新增正式卡、题图与解析图、折叠视觉详情页；补强分母降幂方法页、边界项复查方法页与 Tutor 安全训练增量。
- 错点：想到分部积分但未把 $x^{-2}dx$ 单独分给 $dv$；原路线没有识别原积分重新出现并移项闭合；同时混淆原被积函数 $(\sin x/x)^2$ 与边界项 $\sin^2x/x$ 在 $0$ 处的极限。
- 方法：分母平方凑微分 + 分部积分降幂 + 反常端点边界检查 + 二倍角与换元；method_gap 为 A+B混合、B3-METHOD，方法卡 H09-005；强关联 GS-630、GS-609、GS-684、GS-601。
- Tutor：updated，只写 $F(x)/x^2$ 的触发词、第一动作、自指积分移项和边界对象辨析，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-686 --source 57726 ... --visual expected --strict-quality` 已通过；cards=798，strong=2383，medium=481，weak_audit=305；source summaries=798，compiled=786；bridge records=945，assets=1315；ERROR none，WARN none，quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-10 AI评分 3/5。

## [2026-07-10] formal-intake | GS-687 170665 反常积分原函数整体收口

- 范围：[GS-687](http://127.0.0.1:8765/open/GS-687)、VIS-GS-687、SRC-WQ-GS-687、MATHWIKI-GS-METHOD-074。
- 写入：新增正式卡、题图与解析图、折叠视觉详情页；补强积分边界项复查方法页、定积分总线与 Tutor 安全训练增量。
- 错点：想到分部积分，但在单独发散的原函数项处提前停止，没有保留共同有限上限并合并完整 F(b) 后取极限；另有根式换元系数漏倍数和 arctan(1)=pi/4 特殊值记错。method_gap 为 A+B混合、B4-CHAIN，主方法卡 H08-005，计算模块关联 H09-005、H11-005。
- Tutor：updated，只写有限上限截断、整体合并、换元四项检查和反正切特殊值复核，不复制完整题干或长解析。
- 验证：intake_closeout --id GS-687 --source 170665 --visual expected --strict-quality 已通过；cards=799，strong=2390，medium=477，weak_audit=305；bridge records=946，assets=1317；quality_gate=ok。
- 边界：未手改 生成/；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-10 AI评分 3/5。

## [2026-07-10] formal-intake | GS-688 193265 异构和式分流

- 范围：[GS-688](http://127.0.0.1:8765/open/GS-688)、VIS-GS-688、SRC-WQ-GS-688、MATHWIKI-GS-TOPIC-007。
- 写入：新增正式卡、题图与解析图、折叠视觉详情页；补充数列极限错题总线与 Tutor 安全训练增量。
- 错点：没有先把同一求和号内结构不同的分式项与对数项拆开；第一部分遗漏按 $1\le k\le n$ 放缩后夹逼，第二部分虽联想到黎曼和但忘记 $\frac1n\sum f(\frac{k}{n})$ 的标准形式，同时对 $\sum_{k=1}^n k=\frac{n(n+1)}2$ 不熟。
- 方法：有限和线性拆分 + 放缩型和式夹逼 + 等差数列求和 + 对数幂次提取 + 黎曼和；method_gap 为 A+B混合、B3-METHOD，主方法卡 H08-001，第一部分关联 H08-004；强关联 GS-069、GS-170、GS-445、GS-672。
- Tutor：updated，只写异构和式触发词、先拆分再判型、黎曼和双要素与夹逼入口，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-688 --source 193265 ... --visual expected --strict-quality` 已通过；cards=800，strong=2393，medium=479，weak_audit=305；source summaries=800，compiled=788；bridge records=947，assets=1319；ERROR none，WARN none，quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-10 AI评分 2.5/5。

## [2026-07-10] formal-intake | GS-689 193306 反常尾积分洛必达

- 范围：[GS-689](http://127.0.0.1:8765/open/GS-689)、VIS-GS-689、SRC-WQ-GS-689、MATHWIKI-GS-TOPIC-006。
- 写入：新增正式卡、题图与解析图、折叠视觉详情页；补充定积分错题总线与 Tutor 安全训练增量。
- 错点：已识别无穷比无穷并想到洛必达，但误以为固定的 $+\infty$ 阻止变下限积分求导；随后混淆 $\ln(1/x)$ 与 $1/\ln x$，把分母导数算错。method_gap 为 A+B混合、A-CONCEPT，主方法卡 H09-008，关联 H01-001；强关联 GS-440、GS-585、GS-678、GS-687。
- Tutor：updated，只写反常尾积分固定点拆分、变下限负号与对数对象辨形，不复制完整题干或长解析。
- 验证：`intake_closeout.py --id GS-689 --source 193306 ... --visual expected --strict-quality` 已通过；cards=801，strong=2396，medium=479，weak_audit=305；source summaries=801，compiled=789；bridge records=948，assets=1321；ERROR none，WARN none，quality_gate=ok。
- 边界：未手改 `生成/`；未修改回滚 JSON；未启动 Tutor quiz；未默认输出旧题复做推荐；掌握度为 2026-07-10 AI评分 2.5/5。

## [2026-07-10] maintenance | MATHWIKI-MAINT-146 全库质量门契约修复与第三批已掌握抽测

- 技能：已读取并遵守 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor`、`obsidian-cli` 及其要求预读的 Obsidian/Wiki/Tutor 配套技能。
- 质量门：修复 `暂无强边`、来源保留视觉记录、知识精确注册三类契约误报；新增对应测试，`python3 -m unittest tests.test_intake_quality_math` 为 `12/12 OK`。
- 正式卡：实际修改 70 张卡，其中 43 张为 XLSX 旧批量卡；归一 33 张卡的方法卡引用，给 38 条既有 AI 评分补显式依据，补齐 GS-224/LA-019 的计数字段，并移除 LA-006 的排版残片知识标签。没有改写用户错因、日期、分值或答案。
- 知识库：精确补登记 206 个正式卡已用细分知识标签；最终 801 张正式卡的知识注册与结构硬错误均通过质量门。
- 扩量：Q004 新增 `CAND-0149` 至 `CAND-0153` 五个第18讲定向来源候选；均等待用户实际编号、是否做错和第一卡点，不直接正式化。
- N7：新增 [[错题知识网络/wiki/review/MATHWIKI-REVIEW-003_已掌握抽测第三批执行单|MATHWIKI-REVIEW-003]]，覆盖 [GS-017](http://127.0.0.1:8765/open/GS-017)、[GS-056](http://127.0.0.1:8765/open/GS-056)、[GS-100](http://127.0.0.1:8765/open/GS-100)、[GS-312](http://127.0.0.1:8765/open/GS-312)、[GS-501](http://127.0.0.1:8765/open/GS-501)；只生成执行单，不启动 Tutor。
- 重建：`wrongnet.py rebuild` 输出 `cards=801 strong=2396 medium=479 weak_audit=305`；Wiki source/coverage 为 `summaries=801 compiled=789`；bridge 为 `records=948 assets=1321`。
- 关联抽查：`wrongnet.py related GS-224` 返回 8 条强关联；`wrongnet.py related LA-019` 返回 7 条强关联和 1 条中关联，关联原因可解释。
- 最终巡检：`checked=801 error_cards=0 error_items=0 warn_cards=41 warn_items=44`。41 条为已登记视觉缺口，另 3 条是 GS-408、GS-414、LA-005 的 OCR/题图缺失方法占位；证据不足，不编造修复。
- 边界：未手改 `错题知识网络/生成/**`，未修改回滚 JSON/JSONL，未新增 Tutor 安全输入包；完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-146_全库质量门契约修复与第三批已掌握抽测报告_2026-07-10|MATHWIKI-MAINT-146]]。

## [2026-07-10] maintenance | MATHWIKI-MAINT-147 全量深度编译清零与第四批已掌握抽测

- 技能：已实际读取并遵守 `kaoyan-math-wrong-intake`、`llm-wiki-lint` 与 `tutor`；Lint 用于索引/日志/来源/反链检查，Tutor 只作为安全边界，不启动 quiz。
- 深度编译：把 M146 剩余 12 张待编译卡 GS-125、GS-129、GS-179、GS-284、GS-362、GS-369、GS-375、GS-667、GS-668、GS-669、GS-674、PR-001 挂入概念/方法/专题页；新增 `MATHWIKI-GS-TOPIC-015`，source summary 刷新为 `cards=801 summaries=801 compiled=801`，待编译清零。
- Lint 修复：修正 TOPIC-004/006/007/010 共 21 行历史 Markdown 表格中绝对值竖线造成的列错位；10 张核心 Wiki 页复检 `tables_checked=74 table_issues=0`，12 张关键文件控制字符问题为 0。
- 候选扩量：Q004/Q008 新增 `CAND-0154` 至 `CAND-0158`，覆盖三重积分投影、第一型曲面积分、Green 奇点、第二型曲面积分投影和 Stokes；均保持 candidate，等待用户实际题号、是否做错和第一卡点。
- N7：新增 [[错题知识网络/wiki/review/MATHWIKI-REVIEW-004_已掌握抽测第四批执行单|MATHWIKI-REVIEW-004]]，覆盖 [GS-027](http://127.0.0.1:8765/open/GS-027)、[GS-243](http://127.0.0.1:8765/open/GS-243)、[GS-448](http://127.0.0.1:8765/open/GS-448)、[GS-482](http://127.0.0.1:8765/open/GS-482)、[GS-503](http://127.0.0.1:8765/open/GS-503)；全部避开近 7 天窗口，并保留完整已知做错/复做时间。
- 最终巡检：801 张正式卡逐卡质量门 `error_cards=0 error_items=0 warning_cards=41 warning_items=44`；41 条是已登记视觉缺口，另 3 条是 GS-408、GS-414、LA-005 的方法占位。单元测试 `12/12 OK`。
- Obsidian：CLI 可检索 `MATHWIKI-GS-TOPIC-015`、`CAND-0158`、`MATHWIKI-REVIEW-004`，新专题有 source/coverage 反链；bridge 为 `records=948 assets=1321`。
- 边界：本轮未修改正式错题卡，因此不运行 `wrongnet.py rebuild`；未手改 `生成/**`，未改回滚 JSON/JSONL，未新增 Tutor 安全输入包。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-147_全量深度编译清零与第四批已掌握抽测报告_2026-07-10|MATHWIKI-MAINT-147]]。

## [2026-07-10] maintenance | MATHWIKI-MAINT-148 OO3精确缺图回收与第五批已掌握抽测

- 技能：已实际读取并遵守 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor`、Obsidian/Wiki/Tutor 强制预载技能；Tutor 只作为安全边界，不启动 quiz。
- 质量范围：从只读 OO3 原件按来源标题精确命中并人工核对，为 [GS-249](http://127.0.0.1:8765/open/GS-249)、[GS-362](http://127.0.0.1:8765/open/GS-362)、[GS-369](http://127.0.0.1:8765/open/GS-369)、[GS-375](http://127.0.0.1:8765/open/GS-375)、[GS-405](http://127.0.0.1:8765/open/GS-405)、[GS-408](http://127.0.0.1:8765/open/GS-408)、[GS-414](http://127.0.0.1:8765/open/GS-414)、[LA-027](http://127.0.0.1:8765/open/LA-027)、[LA-029](http://127.0.0.1:8765/open/LA-029)、[LA-084](http://127.0.0.1:8765/open/LA-084)、[LA-095](http://127.0.0.1:8765/open/LA-095)、[LA-096](http://127.0.0.1:8765/open/LA-096) 回收 12 张题图和 9 张解析图；解析图均在折叠块。
- 视觉修复：视觉缺口 41→29；asset map 1321→1342。修复 GS-249 正确高数题与 LA-002 历史误挂来源的 ID/资产冲突；恢复 VIS-GS-079、VIS-GS-152、VIS-GS-341、VIS-GS-344 四张缺失来源图；由 manifest 重建 948 条视觉索引和 Obsidian 直达页；并转义 Q004 的 163 个、REVIEW-005 的 5 个表格 wikilink 别名分隔符。
- 候选扩量：Q004/Q008 新增 `CAND-0159` 至 `CAND-0163`，覆盖 H18-001、H18-003/H18-002、H18-006、H18-007、H18-012；均保持 candidate，等待用户实际题号、是否做错和第一卡点。
- N7：新增 [[错题知识网络/wiki/review/MATHWIKI-REVIEW-005_已掌握抽测第五批执行单|MATHWIKI-REVIEW-005]]，覆盖 [GS-232](http://127.0.0.1:8765/open/GS-232)、[GS-455](http://127.0.0.1:8765/open/GS-455)、[GS-478](http://127.0.0.1:8765/open/GS-478)、[GS-483](http://127.0.0.1:8765/open/GS-483)、[GS-600](http://127.0.0.1:8765/open/GS-600)；全部避开近 7 天窗口并保留已知做错/复做时间。
- 验证：12 张目标卡 `ERROR none`；全库 801 张 `error_cards=0 error_items=0 warning_cards=31 warning_items=32`，较 M147 减少 10 个 warning 卡和 12 个 warning 项；单元测试 12/12；视觉详情/资产缺失均为 0；bridge health 为 `records=948 assets=1342`。
- 边界与剩余：未修改正式错题卡，故不运行 rebuild；未手改 `生成/**`、未改回滚 JSON/JSONL、未新增 Tutor 安全包。剩余 29 个真实视觉缺口、3 个方法占位、8 张通用 YAML 不兼容旧卡和 Q004 的 117 个历史视觉链接漂移；完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-148_OO3精确缺图回收与第五批已掌握抽测报告_2026-07-10|MATHWIKI-MAINT-148]]。

## [2026-07-10] maintenance | MATHWIKI-MAINT-149 正式卡事务干跑与第六批已掌握抽测

- 技能：已实际读取并遵守 `kaoyan-math-wrong-intake`、`llm-wiki-lint`、`tutor` 与 Obsidian/Wiki/Tutor 强制预载技能；Tutor 只作为安全边界，不启动 quiz。
- 正式事务：为 GS-115、GS-246、GS-323、GS-408、GS-414、GS-416、GS-689、LA-035、LA-037、LA-038 生成真实 submission/claim/approved 包；逐项和整批均 `SHADOW_PASS`。最终批次 `MATH-BATCH-M149-20260710-DRYRUN-R2`、transaction `MATH-TX-45c6a3e45f114faeb9a6a10693d0f901`，`formal_repo_modified=false`。
- 证据判断：GS-403、GS-408、GS-414 的题图和两张解析图 SHA 完全相同；拟精分 GS-408/GS-414 并连到 GS-403，但不自动删除或合并。8 张旧卡只做 YAML 序列化兼容修复，GS-246 另把既有同义标题规范为事务要求的“必要提示”。
- Lint 修复：按 manifest 唯一映射修复 Q004 的 5 个实际漂移链接；现在 168/168 个带别名 wikilink 目标存在，manifest-backed drift=0，新增/修改页面表格列异常=0。
- 候选扩量：Q004/Q008 新增 `CAND-0164` 至 `CAND-0168`，覆盖 H18-009、H18-013、H18-014、H18-006、H18-014/H18-016；均保持 candidate，等待用户实际题号、是否做错和第一卡点。
- N7：新增 [[错题知识网络/wiki/review/MATHWIKI-REVIEW-006_已掌握抽测第六批执行单|MATHWIKI-REVIEW-006]]，覆盖 [GS-433](http://127.0.0.1:8765/open/GS-433)、[GS-450](http://127.0.0.1:8765/open/GS-450)、[GS-485](http://127.0.0.1:8765/open/GS-485)、[GS-016](http://127.0.0.1:8765/open/GS-016)、[GS-439](http://127.0.0.1:8765/open/GS-439)；全部避开近 7 天窗口并保留已知做错/复做时间。
- 验证：全库 801 张 `error_cards=0 error_items=0 warning_cards=31 warning_items=32`；单元测试 30/30；10 张正式卡 SHA 仍等于 before SHA；staged Tutor 输入不含题图、完整题干、答案或长解析。
- 边界与待决策：coordinator 当前固定 `SHADOW`，因此 10 张正式卡没有发布、没有 rebuild；未手改 `生成/**`、未改回滚 JSON/JSONL、未发布 Tutor 安全包。等待用户决定是否授权 SUPERVISED 发布，以及是否以后处理 GS-403/408/414 的正式合并。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-149_正式卡事务干跑与第六批已掌握抽测报告_2026-07-10|MATHWIKI-MAINT-149]]。

## [2026-07-10] maintenance | MATHWIKI-MAINT-150 视觉缺口身份收口与第七批已掌握抽测

- 技能与范围：已实际读取并遵守 `llm-wiki-lint` 和 `tutor`；本轮是数学单系统定向修复型 Lint。Tutor 只作为安全边界，不启动 quiz，不发布训练包。
- 质量收口：只读复核 OO3 原始包后，为 [GS-079](http://127.0.0.1:8765/open/GS-079)、[GS-152](http://127.0.0.1:8765/open/GS-152)、[GS-341](http://127.0.0.1:8765/open/GS-341)、[GS-344](http://127.0.0.1:8765/open/GS-344)、[GS-426](http://127.0.0.1:8765/open/GS-426) 至 [GS-429](http://127.0.0.1:8765/open/GS-429)、[LA-003](http://127.0.0.1:8765/open/LA-003)、[LA-005](http://127.0.0.1:8765/open/LA-005) 写入可核验的身份错配/历史并入结论；没有把错图附回正式卡，也没有反推用户错因。
- 视觉与 Lint：真实 `visual_gap_registered` 由 29 降至 19；另 10 个无资产入口已写明不可补原因。Q003 已按 948 条 manifest 重算并修复重复标题；最终 18 个检查对象复检 frontmatter、表格、缺失链接、歧义链接和重复标题均为 0。
- 候选扩量：Q004/Q008 新增 `CAND-0169` 至 `CAND-0173`，覆盖转动惯量、第一型曲面积分面积比较、空间路径无关、锥面转换投影和两类曲面积分关系；均保持 candidate，等待用户实际题号、是否做错和本人第一卡点。
- N7：新增 [[错题知识网络/wiki/review/MATHWIKI-REVIEW-007_已掌握抽测第七批执行单|MATHWIKI-REVIEW-007]]，覆盖 [GS-039](http://127.0.0.1:8765/open/GS-039)、[GS-487](http://127.0.0.1:8765/open/GS-487)、[GS-049](http://127.0.0.1:8765/open/GS-049)、[GS-451](http://127.0.0.1:8765/open/GS-451)、[GS-495](http://127.0.0.1:8765/open/GS-495)；七批累计 35 张，当前批避开近 7 天窗口并保留全部已知做错/复做时间。
- 验证与边界：全库 801 张 `error_cards=0 error_items=0 warning_cards=22 warning_items=22`，较 M149 的 31/32 下降 9/10；单元测试 32/32。未修改正式错题卡，故不运行 rebuild；未手改 `生成/**`，未改回滚 JSON/JSONL，未发布 Tutor 安全包。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-150_视觉缺口身份收口与第七批已掌握抽测报告_2026-07-10|MATHWIKI-MAINT-150]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-151 全库逐题关系重分配审计与语义门禁

- 根因：确认历史自动强边曾被回填 `related` 后再次无条件抬为人工强边；同时存在推断知识污染、证据边界说明参与评分、莱布尼茨公式/判别法混链、反向渲染缺字段和 manual 绕过上限。
- 规则与代码：新增 `relationship_quality_audit.md`、`relationship_signal_policy.json`、逐题 auditor 和关系质量 gate；更新 wrongnet，使 `related` 不能自证，推断知识只进候选，纳入登记方法卡并修复双端渲染、阈值和公平 cap。
- 逐题审计：当前不可变 run `MATH-REL-AUDIT-20260711-5d054637c87a` 为 801/801 张正式卡各生成一条记录，并归一 4637 条当前/模拟逻辑边；正式卡 tree SHA 前后均为 `4e44c3d42ad8595dab62458084b47af25eb6889d8fa2678fadde21165003e6bb`。先前 `a812ea31c886` / `1ac379d3c4d5` run 因泛信号分层与 declared 规则最终收紧而被 implementation SHA 淘汰，仅保留历史。
- 关系发现：1884 条当前声明边中，1185 条可由独立强边证据复现，684 条不足强边证据需逐边语义复核，16 条涉及重复/身份待决；另有 37 个 `暂无强边` 与声明入边矛盾、17 张知识待精分、21 张方法待精分、6 张活跃卡模拟后仍孤立。
- 异步边界：M149 的 10 张非终态目标卡标为 `DEFERRED_NONTERMINAL_JOB`，不创建第二套 update；当前仍为 `SHADOW`，`formal_mutation_allowed=false`。
- 验证：关系专项测试 `16/16 OK`、完整套件 `155/155 OK`；audit gate 为 `ok=true / cards=801 / edges=4637 / issues=[]`；release gate 按预期阻断未收口发现；隔离重建为 `strong=2228 / medium=563 / weak_audit=140`，2791 条选中逻辑边与审计完全同集且双端渲染 5582 条。
- 数据边界：正式错题卡 `0` 修改、`生成/**` `0` 修改、回滚 JSON/JSONL `0` 修改、Tutor/StudyVault `0` 修改。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-151_全库逐题关系重分配审计与语义门禁_2026-07-11|MATHWIKI-MAINT-151]]，运行索引见 [[错题知识网络/wiki/maintenance/relationship_quality/index|关系质量审计索引]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-152 第一批逐题语义重分配与 SHADOW 事务

- 逐题范围：独立阅读 15 张主卡及 8 张双端 storage 依赖卡，最终形成 20 张 `SHADOW_REPAIR`；GS-046、GS-048、LA-005 因重复身份或题图/OCR 缺口转 `NEEDS_USER`。
- 重分配：11 张精分 `knowledge`，14 张收口 `related`；人工双端复核并删除 17 条声明逻辑边的 26 个 storage occurrence。13 张旧卡只追加“待评分、无新作答证据”契约记录，没有伪造评分。
- 工具加固：新增 `prepare_relationship_repair_math.py` 及测试，实现 SHA 绑定、先全批内存构造再写草案、immutable 冲突预检、legacy mastery 安全契约和 queue 180 字边界。
- 关系规则：把递推数列、单调有界准则、递推题型/专题链及作差法/数学归纳法降为粗信号；修正投影中 3 条人工已删边被错误抬回强边的问题。
- 异步事务：一个早期 GS-039 草案被 mastery 来源门禁拦下并已终态化为 `FAILED`；修正后最终 20/20 个 `sync-one-shot` 与整批 `MATH-BATCH-M152-20260711-DRYRUN-R3` 均为 `SHADOW_PASS`。transaction `MATH-TX-ce61c13481024f1ca12afd464cadbb9b`，`formal_repo_modified=false`；20/20 张 transaction after 除 provenance marker 外与 R4 预览逐字节一致。
- 审计：当前正式 run `MATH-REL-AUDIT-20260711-1beae878825f` 为 PASS；最终 transaction-after 投影 `MATHWIKI-MAINT-152-25cf64c1c18b` 也为 PASS。17 条删除边全部无 storage，12 条只留派生边、5 条消失、0 条重新升为强边；REMOVE_CANDIDATE 投影由 704 降为 686。
- 后续：M152 正式发布后重绑定 canonical SHA，再处理 `GS-066↔GS-071` 新强边候选与 `GS-432↔GS-513` sentinel/inbound 矛盾。当前仍为 SHADOW，未改正式卡、`生成/**`、回滚账本或 Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-152_第一批逐题语义重分配与SHADOW事务_2026-07-11|MATHWIKI-MAINT-152]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-153 第二批 30 题逐题语义复核与关系重分配

- 逐题范围：从 canonical audit 选出 30 张未占用高风险卡，三组各 10 题并发只读核对正式卡、linked visual、题图/解析、incident edge 和对端卡；固定 selection/plan SHA，未创建 queue job。
- 合并门禁：只接受“人工结论、canonical verdict、同批完整 storage owner”三者交集；形成 26 张 `SHADOW_REPAIR`、3 张本批不改、1 张 identity block。19 张拟精分 knowledge，26 张拟调整 related，11 张仅补安全 `待评分` 契约，不产生掌握度分数。
- 关系处理：R2 最终删除 60 条逻辑边的 69 个 storage occurrence，并新增 `GS-572↔GS-586` 双端强边。60 条删除边在投影中 storage=0，56 条消失、4 条只留派生边、0 条重新升强。
- 反例反馈：R1 删除 `GS-270↔GS-575` 后被精分知识重新抬为 `ADD_STRONG`；R2 据此保留该边，证明隔离投影能拦截自相矛盾的删边计划。
- 身份门禁：确认 GS-604/GS-605 的题图和解析图成对交叉错绑；GS-604 不进入 preview，GS-603↔GS-604 也不裁决，等待 visual identity relink 专项。
- 投影验证：`MATHWIKI-MAINT-153-R2-719988effa43` 为 `status=PASS / audit gate ok=true / issues=[]`；801 卡、声明边 1825、模拟强边 2221、中边 571、REMOVE_CANDIDATE 635。
- 边界：coordinator 仍为 SHADOW；正式错题卡、`生成/**`、回滚 JSON/JSONL、Tutor/StudyVault 均未修改。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-153_第二批30题逐题语义复核与关系重分配SHADOW计划_2026-07-11|MATHWIKI-MAINT-153]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-153-VISUAL-R1 GS-604/GS-605 视觉身份原子重连

- 根因：两个完整 OO3 题图/解析图 bundle 被交叉分配给相反 wrongnet owner；旧 strict gate 只验路径、存在性与折叠结构，未验证内容身份。
- 正确映射：GS-604→`57707-2`（有理函数积分）；GS-605→`57707-4`（arctan 乘有理函数分部积分）。
- 事务：只持有 formal repo lock，使用仓库外 WAL 和 before/after SHA 原子发布；不取得 queue lock。
- 写入：四张视觉资产、两张详情页、manifest、asset map、视觉 index/open links 与本维护审计记录；legacy 详情文件名保留并显式标记。
- 边界：正式错题卡、`生成/**`、回滚 JSON/JSONL、Tutor/StudyVault 均未纳入事务；未运行 rebuild。
- 残余：GS-605 正式卡历史来源 `57707-3（题册第(4)题）` 与已核验视觉 locator `57707-4` 不同，留待 SUPERVISED 正式事务。
- receipt：`错题知识网络/wiki/maintenance/M153_visual_identity_relink_receipt.json`；报告：[[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-153-VISUAL-R1_GS604-GS605视觉身份原子重连_2026-07-11|MATHWIKI-MAINT-153-VISUAL-R1]]。

- 最终验收：两题 strict gate `2/2 PASS`；完整单测 `170/170 PASS`；bridge 为 `948 records / 1342 assets`；Obsidian 搜索与反链通过。
- 零改动复核：正式卡 tree、`生成/**` tree、回滚 JSON/JSONL 与事务前 SHA 完全一致；queue 仍为 `REVIEWED=30 / FAILED=4`。
- projection finalize receipt：`错题知识网络/wiki/maintenance/M153_visual_identity_projection_finalize_receipt.json`。

## [2026-07-11] maintenance | MATHWIKI-MAINT-154 第三批 30 题外部 Owner 逐题复核与累计 SHADOW 投影

- 选批：从 M153 的 69 条 deferred dependency edge 按真实 storage owner 聚类，排除 M149/M152/M153 已复核卡、30 个非终态 REVIEWED job 与未达到 linked_wrongnet 的 GS-269；最终 30 张新卡覆盖 46 条原 deferred edge。
- 并发复核：三个只读 reviewer 实际核对 30/30 正式卡、30 张题图、现有 20 张解析图、全部 incident edge 与对端卡；identity `PASS=30 / NEEDS_USER=0`，未创建 queue job。
- 新结论：原 46 条边最终 `REMOVE=39 / KEEP=6 / DEFER_RULE_CONFLICT=1`；另删 `GS-289↔GS-625`，新增 `GS-183↔GS-643`、`GS-320↔GS-641`。没有改个人 wrong_point、error_causes、method_gap 或掌握度分数。
- 累计依赖：把 M153 尚未发布的 26 张 repair 与 M154 新 30 张合为 56 张 R2 plan；累计删除 100 条逻辑边的 118 个 occurrence，新增 3 条双端强边。plan validate 与 56 份 preview/submission/approved binding 全部通过，正式写入标记均为 false。
- 反例反馈：R1 删除 `GS-587↔GS-618` 后被精分知识重新抬为 ADD_STRONG；R2 将其转为规则冲突暂缓。最终 100 条删除边全部 storage=0，88 条消失、12 条只留派生边、0 条重新升强；3 条新增边均为双端 KEEP_STRONG。
- 门禁加固：audit ID 新增知识点库 SHA；auditor 对 generated/knowledge/visual 做开始结束双快照；gate 和 draft 入口都复算当前输入 SHA，旧视觉或旧知识 run 不能再误报 PASS。
- 验证：canonical run `MATH-REL-AUDIT-20260711-c40b7fbbaab1` 与 projection `MATHWIKI-MAINT-154-R2-f4e112af3c1d` 均 PASS；完整单测 `175/175 OK`。正式卡、生成层、回滚账本 SHA 未变，queue 仍为 `REVIEWED=30 / FAILED=4`。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-154_第三批30题外部Owner逐题复核与累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-154]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-155 第四批 24 卡依赖闭包复核与存储归一化 SHADOW 投影

- 选批：19 张 M153 剩余合格外部 owner、GS-583 三个外部入边 owner，加上实际持有 occurrence 的 M153 `NO_CHANGE` 卡 GS-502/LA-090，共 24 张；selection gate 验证 22 条 seed edge、29 个 occurrence、owner 缺口 0、目标非终态 job 0。
- 并发复核：三个只读 reviewer 实际核对 24/24 正式卡、24 张题图、13 张解析图和全部 incident edge；identity `PASS=24 / NEEDS_USER=0`，没有从标准解析反推个人错因、method_gap 或掌握度。
- 新结论：22 条 seed edge 为 `REMOVE=18 / KEEP=4`；额外删除 LA-082↔LA-088，新增 GS-536↔GS-585、GS-502↔GS-606；GS-583↔GS-660 删除正式单向 storage、仅留派生中边。
- 累计计划：M154 56 张 carry 与 M155 24 张合为 80 张 R2 repair；累计删除 119 条逻辑边的 144 个 occurrence，新增 5 条逻辑强边，并对既有 KEEP_STRONG 的 LA-075↔LA-099 补 1 条 reciprocal storage occurrence。
- R1/R2：R1 的 reviewed 删除边已无 storage 且 0 条重升强，但删除 LA-090 后把 LA-099 新写成 sentinel；R2 storage normalization 不恢复弱边、不新增逻辑边，最终 LA-075↔LA-099 为双端 KEEP_STRONG，sentinel+inbound 从 M154 投影的 38 降为 37。
- 验证：最终 projection `MATHWIKI-MAINT-155-R2-81dcb0141f14` 为 `PASS / issues=[]`；119 条删除边中 106 条消失、13 条只留派生、0 条仍有 storage、0 条重升强；5 条逻辑新增和 1 条 normalization 均为双端 KEEP_STRONG。
- 工具加固：新增 selection closure gate；全局无关 queue 漂移只记 warning，同卡 REVIEWED/READY/REVIEWING 仍硬阻断；事务引擎新增显式 `storage_normalization=true` 门禁及回归测试，普通 ADD 仍只接受 ADD_STRONG。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-155_第四批24卡依赖闭包复核与存储归一化SHADOW投影_2026-07-11|MATHWIKI-MAINT-155]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-156 第五批 30 卡哨兵闭包复核与累计 SHADOW 投影

- 选批：从 canonical c40 排除 115 张 prior-review 卡和全部同卡非终态 job，选择 30 张、6 个 owner-closure 组件；selection gate 覆盖 40 条 edge、40 个 storage occurrence，owner 缺口 0。
- 并发复核：三个只读 reviewer 实际查看 30/30 正式卡、30 张题图和 1 张独立解析图；identity `PASS=30 / NEEDS_USER=0`。8 张 knowledge 有证据化修正，未改个人 wrong_point、error_causes、method_gap 或掌握度。
- 新结论：40 条 covered edge 为 `REMOVE=16 / KEEP=21 / NEEDS_USER_DEFER=3`；新增 `GS-585↔GS-649`、`GS-554↔GS-557`；另确认 9 条既有 KEEP 与 3 条 derived-only 候选。
- 累计计划：M155 80 张 carry 与 M156 30 张合为 110 张 R2 repair；累计删除 135 条逻辑边的 160 个 occurrence、累计 7 条逻辑新增边，并保留 2 条 storage normalization。
- R1/R2：R1 删除 GS-501 两条弱出边后制造新的 sentinel+inbound；R2 不恢复弱边，只对已双端确认且 canonical KEEP_STRONG 的 `GS-501↔GS-502` 补 reciprocal storage。最终 sentinel+inbound 从 37 降到 36，且没有新增项。
- 验证：最终 projection `MATHWIKI-MAINT-156-R2-41cff93f7a28` 为 `PASS / issues=[]`；135 条删除边中 121 条消失、14 条只留派生、0 条仍有 storage、0 条重升强；7 条逻辑新增和 2 条 normalization 均为双端 KEEP_STRONG。完整单测 `184/184 OK`。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-156_第五批30卡哨兵闭包复核与累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-156]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-157 第六批 13 卡线代双组件逐题复核与累计 SHADOW 投影

- 选批：排除 145 张 prior-review 卡与全部非终态 queue 端点后，选择二次型 6 卡和矩阵方程 7 卡；selection gate 为 `13 cards / 38 covered edges / 60 occurrences / selected owner 51 / base owner 9 / outside owner 0`。
- 并发复核：两个 owner reviewer 与一个 challenger 实际复看 13/13 张题图、6 卡共 8 张解析图及必要旧端点；identity `PASS=13 / NEEDS_USER=0`。12 张 knowledge 有证据化精分，未改个人 wrong_point、error_causes、method_gap 或掌握度。
- 新结论：38 条 covered edge 为 `REMOVE=17 / KEEP=20 / NEEDS_USER_DEFER=1`；challenger 唯一推翻 owner 的边为 LA-062↔LA-063，因两题只共享“按列拆”子步骤而采用保守删除。9 条人工 KEEP 仍与规则冲突，其中 5 条显式标为 human evidence only。
- 派生结论：LA-062↔LA-081、LA-063↔LA-081、LA-081↔LA-089 只留派生关系；规则建议新增 LA-063↔LA-089，但人工认为可逆性处于不同题型链，拒绝正式 ADD。
- 累计计划：M156 110 张 carry 与 M157 13 张合为 123 张 repair；累计删除 152 条逻辑边的 188 个 occurrence，承接 7 条逻辑新增强边和 2 条 storage normalization。123/123 preview 与 approved markdown 均匹配 after SHA，正式卡均匹配 before SHA。
- 投影：`MATHWIKI-MAINT-157-R1-54dd491d861f` 为 `PASS / issues=[]`；152 条删除边中 137 条消失、15 条只留派生、0 条仍有 storage、0 条重升强；sentinel+inbound 保持 36，新增 0、解决 0，因此不需要 R2。
- 门禁加固：selection gate 新增 covered external endpoint live/audit job 检查；批外端点有 `REVIEWED/READY/REVIEWING` 时以 `queue.covered_endpoint_nonterminal` 拒绝，audit/live 两类回归测试均通过。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-157_第六批13卡线代双组件逐题复核与累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-157]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-158 第七批 30 卡无穷级数逐题复核与累计 SHADOW 投影

- 选批：排除 158 张 prior-review 卡和所有非终态 queue 端点，选择常数项级数 13 卡与幂级数/傅里叶 17 卡；selection gate 为 `30 cards / 151 covered edges / 167 occurrences / outside owner 0`。
- 并发复核：两个 owner 与一个 challenger 实际查看 30/30 张题图、5 卡共 7 个解析资产和 15 个外部端点；identity `PASS=30 / NEEDS_USER=0`。5 张 knowledge 精分，个人错因、method_gap 和掌握度不变。
- 关系裁决：covered edge 为 `REMOVE=56 / KEEP=58 / NEEDS_USER=37`；其中 7 条 REMOVE 已由 M157 累计计划承接，只重新确认、不重复动作。新增 `GS-511↔GS-549`、`GS-565↔GS-599`，19 条只留派生候选。
- 保守边界：35 条 canonical KEEP_STRONG 弱证据边和 `GS-548/612↔GS-613` 两条评审分歧边都不进入正式动作；GS-501 与 GS-598 题图确认不是重复题。
- 累计计划：M157 123 张 carry 与 M158 30 张合为 153 张 repair；累计删除 201 条唯一逻辑边的 240 个 occurrence，累计 9 条逻辑新增和 2 条 storage normalization。153/153 before/after/approved 哈希通过。
- 投影：`MATHWIKI-MAINT-158-R1-21a2c503bb57` 为 `PASS / issues=[]`；201 条删除边中 182 条消失、19 条只留派生、0 条仍有 storage、0 条重升强；11 条 add/normalization 均为双端 KEEP_STRONG。sentinel+inbound 从 36 降到 35，新增 0、解决 GS-496，因此不需要 R2。
- 验收：完整单元测试 `204/204 OK`；M158 定向 Markdown/source-ref/wikilink lint 为 0 issues，Obsidian 搜索、outline 与反链均可复现。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-158_第七批30卡无穷级数逐题复核与累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-158]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-159 第八批 30 卡积分与多元函数逐题复核及累计 SHADOW 投影

- 选批：排除 prior-review union 188 与所有同卡非终态 job，选择反常积分/微分方程、定积分、三角积分、多元极值与多元 Taylor/向量场五组 30 卡；selection gate 为 `30 cards / 88 covered edges / 130 occurrences / outside owner 0`。
- 视觉复核：三位 owner、全量 challenger 与冲突专项 reviewer 覆盖 30/30 selected 题图、9/9 selected 解析、15/15 外端点题图及 12 个可用解析、11 个 M158 基线对端；identity `PASS=29 / NEEDS_USER=1`。
- 身份结论：GS-393 与 GS-424 的题图 SHA、来源定位、题面、答案和详情解析一致，确认同题重复；未获 merge 授权前 GS-393 与两条 incident edge 不进入 repair。GS-175/LA-115、GS-178/LA-114 只是跨学科 source 串号。
- 逐题结果：19 张 knowledge 精分；GS-176、GS-390、GS-394 为 reviewed-no-change，不制造空更新。没有改个人 wrong_point、error_causes、method_gap 或掌握度。
- 关系裁决：88 条 covered edge 为 `REMOVE=31 / KEEP=20 / NEEDS_USER=37`；31 条人工弱边因 canonical 仍为 KEEP_STRONG 而由事务门禁转 NEEDS_USER。新增 GS-179↔GS-580、GS-184↔GS-445、GS-387↔GS-389；10 条只留派生候选。
- 累计计划：M158 153 张 carry 与 M159 26 张实际 repair 合为 179 张；R2 最终删除 229 条逻辑边的 274 个 occurrence，累计 12 条逻辑新增和 2 条 storage normalization。179/179 before/after/approved 哈希通过。
- R1/R2：R1 删除 GS-082↔GS-658、GS-174↔GS-580 后制造两个新 sentinel；R2 不把旧弱边升级，也不临时补建未经 owner closure 的替代边，只撤回这两条删除动作。最终 sentinel+inbound 保持 35，新增/解决均为 0。
- 投影：`MATHWIKI-MAINT-159-R2-359014be07ea` 为 `PASS / issues=[]`；229 条删除边中 209 条消失、20 条只留派生、0 条仍有 storage、0 条重升强；14 条 add/normalization 均为双端 KEEP_STRONG。
- 验收：完整单元测试 `217/217 OK`；selection/plan/draft/projection 哈希门禁全部通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本 SHA 未变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-159_第八批30卡积分与多元函数逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-159]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-160 第九批 30 卡多元与积分逐题复核及累计 SHADOW 投影

- 选批：排除 prior-review union 218、未收口重复身份与全部同卡非终态 job，选择空间曲线/方向导数、多元积分/极坐标、变上限积分/定积分比较三组 30 卡；selection gate 为 `30 cards / 100 covered edges / 100 occurrences / outside owner 0`。
- 视觉复核：三位 owner、全量 challenger、知识点专项与冲突专项实际查看 30/30 selected 题图、33/33 selected 解析资产、45/45 covered 对端题图及 33 个可用解析；GS-650 使用详情完整文字解析。identity `PASS=30 / NEEDS_USER=0`。
- 逐题结果：9 张 knowledge 最小充分修正，20 张实际 repair，10 张 reviewed-no-change；GS-656/665/678 的 inferred 标签保持隔离，个人错因、method_gap 与掌握度不变。
- 关系裁决：100 条 covered edge 为 `REMOVE=26 / KEEP=32 / NEEDS_USER=42`；4 条 canonical REMOVE_CANDIDATE 由多路人工强证据保留，40 条 canonical KEEP_STRONG 弱边与 2 条强度分歧边均冻结。新增 GS-577↔GS-671；15 条只留派生候选。
- 累计计划：M159 179 张 carry 与 M160 20 张实际 repair 合为 199 张 R2；累计删除 254 条逻辑边的 299 个 occurrence，累计 13 条逻辑新增和 3 条 storage normalization。199/199 before/after/approved 哈希通过。
- R1/R2：R1 删除 GS-662 两条弱出边后制造新 sentinel，同时解决 GS-297；R2 暂缓 GS-577↔GS-662 删除，不把其升级为强边，并对三路证据一致的 GS-663↔GS-671 补 reciprocal storage。最终相对 M159 新增 sentinel 0、解决 GS-297/GS-663 两项。
- 投影：`MATHWIKI-MAINT-160-R2-5601d25e5182` 为 `PASS / issues=[]`；254 条删除边中 230 条消失、24 条只留派生、0 条仍有 storage、0 条重升强；13 条逻辑新增和 3 条 normalization 均为双端 KEEP_STRONG。sentinel+inbound 从 35 降至 33。
- 验收：完整单元测试 `233/233 OK`；定向 Markdown/JSON lint 为 0 issues；Obsidian 搜索、outline 与反链均可复现。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-160_第九批30卡多元与积分逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-160]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-161 第十批 30 卡积分、微分方程与二次型逐题复核及累计 SHADOW 投影

- 选批：排除 prior-review union 248、未收口身份碰撞与全部同卡非终态 job，选择积分方法链、微分方程、二次型/相似结构三组 30 卡；selection gate 为 `30 cards / 107 covered edges / 129 occurrences / 13 external endpoints / outside owner 0`。
- 视觉复核：三位 owner、全量独立 challenger、知识点专项和投影安全专项覆盖 selected 题图 30/30、selected 解析 31/31、covered endpoint 题图 72/72，并补核 19 份批外解析；identity `PASS=30 / NEEDS_USER=0`。
- 逐题结果：17 张 knowledge 得到最小充分修正，语义层 23 张实际变化、7 张 reviewed-no-change；累计计划因严格 mastery 来源门禁为 GS-632 补安全“待评分”来源记录，因此本轮进入计划 24 张。个人 wrong_point、error_causes、method_gap 与掌握度分数均未改。
- 关系裁决：107 条 covered edge 为 `REMOVE=29 / KEEP=19 / NEEDS_USER=59`；其中 19 条是本轮新增删除动作，另新增 `LA-030↔LA-041`、`LA-030↔LA-043` 两条双端强边，9 条只保留派生迁移价值。
- 保守边界：56 条 canonical KEEP_STRONG 因缺少双路支持继续冻结，3 条 canonical REMOVE_CANDIDATE 因 reviewer 分歧转 NEEDS_USER；GS-393/GS-424 重复身份与 GS-605 历史 locator/source 异常继续隔离。
- 累计计划：M160 的 199 张 carry 与 M161 的 24 张计划 repair 合为 223 张；累计删除 273 条逻辑边的 321 个 occurrence，累计 15 条逻辑新增和 3 条 storage normalization。223/223 before/preview/approved 哈希通过。
- 投影：`MATHWIKI-MAINT-161-R1-75523a2f09f7` 为 `PASS / issues=[]`；273 条删除边中 250 条消失、23 条只留派生、0 条仍有 storage、0 条重升强；18 条 add/normalization 均为双端 KEEP_STRONG。sentinel+inbound 保持 33，新增/解决均为 0。
- 验收：完整单元测试 `246/246 OK`；selection/decisions/plan/draft/projection 哈希门禁全部通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-161_第十批30卡积分微分方程二次型逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-161]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-162 第十一批 9 卡一元积分高影响闭包逐题复核及累计 SHADOW 投影

- 选批：没有机械凑满 30 卡；从 prior-review union 278 外选择周期积分/分段原函数/含参变限 5 卡和分部积分/复合边界/反常端点 4 卡。selection gate 为 `9 cards / 35 covered edges / 37 covered occurrences / outside owner 0`，另有 2 条 owner 不完整 incident edge 整条冻结。
- 视觉复核：两位 owner 与全量独立 challenger 实际查看 selected 题图 9/9、selected 解析资产 10/10、covered endpoint 题图 31/31，并补核 13 份端点解析；identity 为 `PASS=8 / PASS_WITH_CAVEAT=1 / NEEDS_USER=0`，GS-043 的题图裁切缺口已显式保留。
- 逐题结果：8 张 knowledge 得到最小充分修正，GS-686 reviewed-no-change；个人 wrong_point、error_causes、method_gap 和掌握度分数均不改。
- 关系裁决：35 条 covered edge 为 `REMOVE=6 / KEEP=11 / NEEDS_USER=18`；15 条 canonical KEEP 与 3 条 reviewer 分歧 REMOVE 全部冻结。`GS-043↔GS-586` 由双路实题证据保留并满足零出边原子保护；没有新增正式 ADD。
- 累计计划：M161 的 223 张 carry 与 M162 的 8 张实际 repair 合为 231 张；累计删除 279 条逻辑边的 327 个 occurrence，累计 15 条逻辑新增和 3 条 storage normalization。231/231 before/preview/approved 哈希通过。
- 投影：`MATHWIKI-MAINT-162-R1-bf1d1522c914` 为 `PASS / issues=[]`；279 条删除边中 256 条消失、23 条只留派生、0 条仍有 storage、0 条重升强；18 条 add/normalization 均为双端 KEEP_STRONG。sentinel+inbound 保持 33，新增/解决均为 0，`new_zero_outgoing_cards=[]`。
- 验收：完整单元测试 `259/259 OK`；selection/decisions/plan/draft/projection 哈希门禁与 Markdown/JSON 定向检查通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-162_第十一批9卡一元积分高影响闭包逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-162]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-163 第十二批 6 卡一元积分与换序闭包逐题复核及累计 SHADOW 投影

- 选批：从 prior-review union 287 外选择参数反常积分/面积区域 3 卡与根式换元/闭区间最值/反函数求导 3 卡；38 条 stored incident 先冻结 5 条历史已审边，再冻结 3 条 owner/身份不闭合边，净新增 covered 为 `6 cards / 30 edges / 30 occurrences / outside owner 0`。
- 视觉复核：两位 owner 与独立 root challenger 实际查看 selected 题图 6/6、selected 解析 7/7、24 张批外端点的 26 份题图及 13 份可用解析；6 张身份唯一，GS-593 保留解析仅覆盖换序区域的 caveat。
- 逐题结果：GS-593 补“二重积分换序”、GS-642 补“闭区间最值定理”，其余 knowledge 保持，GS-676 reviewed-no-change；个人 wrong_point、error_causes、method_gap 和掌握度分数均不改。
- 关系裁决：30 条 covered edge 为 `REMOVE=5 / KEEP=13 / NEEDS_USER=12`；4 条 reviewer 分歧与 8 条 canonical KEEP 保护边全部冻结，ADD review set 为空。`GS-404↔GS-593` 双路 KEEP，满足 GS-593 零出边原子保护。
- 累计计划：M162 的 231 张 carry 与 M163 的 5 张实际 repair 合为 236 张；累计删除 284 条逻辑边的 332 个 occurrence，累计 15 条逻辑新增和 3 条 storage normalization。236/236 before/preview/approved 哈希通过。
- 投影：`MATHWIKI-MAINT-163-R1-776d4de87813` 为 `PASS / issues=[]`；284 条删除边中 261 条消失、23 条只留派生、0 条仍有 storage、0 条重升强；18 条 add/normalization 均为双端 KEEP_STRONG。sentinel+inbound 保持 33，新增/解决均为 0，`new_zero_outgoing_cards=[]`。
- 验收：M163 定向测试 `14/14 OK`；selection/decisions/plan/draft/projection 哈希门禁通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-163_第十二批6卡一元积分与换序闭包逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-163]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-164 第十三批 4 卡符号面积与参数几何闭包逐题复核及累计 SHADOW 投影

- 选批：从 prior-review union 293 外选择 GS-185、GS-294、GS-644、GS-308；13 条 stored incident 冻结 3 条历史已审边与 2 条 owner 不闭合边，复核 `8 stored edges / 9 occurrences`，并显式穷尽 13 条 frozen ADD 候选，总复核 21 边。
- 视觉复核：两位 owner 与独立 root challenger 查看 selected 题图 4/4、selected 解析 7/7、15 张批外端点题图及全部 15 份可用解析；4 卡身份均为 PASS。
- 逐题结果：GS-185 用“积分保号”替换宽泛“一元函数积分学的计算”，GS-294 补“绝对值分段、等比级数”，GS-308 补“复合函数”，GS-644 保持；个人 wrong_point、error_causes、method_gap 和掌握度分数均不改。
- 关系裁决：8 条 stored edge 为 `REMOVE=2 / KEEP=5 / NEEDS_USER=1`；GS-643↔GS-644 因 reviewer 分歧且 canonical KEEP 而冻结。13 条 ADD 候选全部双路拒绝，未生成任何正式 ADD action。
- 累计计划：M163 的 236 张 carry 与 M164 的 4 张 repair 合为 240 张；累计删除 286 条逻辑边的 334 个 occurrence，累计 15 条逻辑新增和 3 条 storage normalization。240/240 before/preview/approved 哈希通过。
- 投影：`MATHWIKI-MAINT-164-R1-4bf8117e331f` 为 `PASS / issues=[]`；286 条删除边中 264 条消失、22 条只留派生、0 条仍有 storage、0 条重升强；18 条 add/normalization 均为双端 KEEP_STRONG。13 条被拒 ADD 均为 0 storage。sentinel+inbound 保持 33，`new_zero_outgoing_cards=[]`。
- 验收：M164 定向测试 `16/16 OK`、完整单元测试 `289/289 OK`；selection/decisions/plan/draft/projection 哈希门禁通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-164_第十三批4卡符号面积与参数几何闭包逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-164]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-165 第十四批 5 卡级数与空间几何闭包逐题复核及累计 SHADOW 投影

- 选批：从 prior-review union 297 外选择 GS-607、GS-608、GS-627、GS-628、GS-629；22 条 stored incident 冻结 12 条 M159/M160 历史已审边，复核 `10 stored edges / 14 occurrences`，并显式穷尽 12 条 frozen ADD 候选，总复核 22 边。
- 视觉复核：两位 owner 与独立 challenger 查看 selected 题图 5/5、selected 解析 8/8、15 张批外端点的 16 份题图及全部 10 份可用解析；五卡身份均为 PASS。另发现 GS-501/GS-598 虽图片 SHA、来源 ID 与版式不同，但数学表达式逐项相同，改判为 `NEEDS_USER_MERGE` 并撤回 GS-598。
- 逐题结果：GS-607 用“极限比较判别法、收敛级数线性运算”替换粗粒度“等价无穷小”，GS-628 补“两平面交线”；GS-608/627/629 保持，GS-627 reviewed-no-change；个人 wrong_point、error_causes、method_gap 和掌握度分数均不改。
- 关系裁决：10 条 stored edge 为 `REMOVE action=1 / KEEP=4 / NEEDS_USER=5`；GS-494↔GS-608 因 canonical KEEP 强边降级门禁冻结，另四条 reviewer 分歧边冻结。12 条 ADD 为 `accepted=2 / rejected=8 / needs_user=2`，只新增 GS-590↔GS-608 与 GS-597↔GS-607。
- 累计计划：M164 的 240 张 carry 与 M165 的 4 张实际 repair 合为 244 张；累计删除 287 条逻辑边的 336 个 occurrence，累计 17 条逻辑新增和 3 条 storage normalization。244/244 before/preview/approved 哈希通过。
- 投影：`MATHWIKI-MAINT-165-R1-bce09cc25436` 为 `PASS / issues=[]`；287 条删除边中 264 条消失、23 条只留派生、0 条仍有 storage、0 条重升强；20 条 add/normalization 均为双端 KEEP_STRONG。本批 8 条拒绝和 2 条冻结 ADD 均为 0 storage；sentinel+inbound 保持 33，`new_zero_outgoing_cards=[]`。
- 验收：M165 定向测试 `19/19 OK`、完整单元测试 `308/308 OK`；selection/decisions/plan/draft/projection 哈希门禁通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-165_第十四批5卡级数与空间几何闭包逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-165]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-166 第十五批 6 卡复合偏导与 PDE 闭包逐题复核及累计 SHADOW 投影

- 选批：从 prior-review union 302 外选择 GS-367、GS-380～384；4 条 stored incident 中 2 条 owner/证据闭合进入复核，2 条因 GS-385 无解析和 owner gap 冻结；另显式穷尽 13 条内部 ADD，总复核 15 边。16 条批外 ADD 因 5 个端点均无独立解析继续冻结。
- 视觉复核：两位 owner 与未读取 owner 结论的独立 challenger 实际查看 selected 题图 6/6、解析 6/6，并各自穷尽责任边/15 条全边；六卡身份均 PASS。另确认 GS-303/GS-600 只差纵向平移，完整弧长任务等价，登记 `NEEDS_USER_MERGE`。
- 逐题结果：GS-367 knowledge 保持；GS-380～384 补二阶偏导、变量代换、一阶线性微分方程、复合函数求导、多元函数极值、参数退化讨论或极限条件反推导数。个人 wrong_point、error_causes、method_gap 和掌握度分数均不改；GS-367 仅在 preview 追加待评分安全来源记录。
- 关系裁决：2 条 stored edge 为 `KEEP=1 / NEEDS_USER=1`；GS-381↔GS-382 虽双路判弱但 canonical KEEP，按降级门禁冻结。13 条 ADD 为 `accepted=2 / rejected=11 / needs_user=0`，只新增 GS-380↔GS-381 与 GS-381↔GS-383；owner/challenger 冲突为 0。
- 累计计划：M165 的 244 张 carry 与本批 6 张合为 250 张；累计删除 287 条逻辑边的 336 个 occurrence，累计 19 条逻辑新增和 3 条 storage normalization。250/250 before/preview/approved 哈希通过。
- 投影：`MATHWIKI-MAINT-166-R1-beaead419695` 为 `PASS / issues=[]`；287 条删除边中 264 条消失、23 条只留派生、0 条仍有 storage、0 条重升强；22 条 add/normalization 均为双端 KEEP_STRONG。11 条拒绝 ADD 与 16 条 external 冻结 ADD 均为 0 storage；sentinel+inbound 保持 33，`new_zero_outgoing_cards=[]`。
- 验收：M166 定向测试 `18/18 OK`、完整单元测试 `326/326 OK`；selection/decisions/plan/draft/projection 哈希门禁通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-166_第十五批6卡复合偏导与PDE闭包逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-166]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-167 第十六批 5 卡定积分物理微元闭包逐题复核及累计 SHADOW 投影

- 选批：从 prior-review union 308 外选择 GS-415、GS-418、GS-419、GS-420、GS-423；7 条 stored edge/12 个 occurrence 与 3 条内部 ADD 全部双端闭合，总复核 10 边；20 条批外 ADD 冻结。
- 视觉复核：owner、未读取 owner 结论的独立 challenger 各自查看 5/5 selected 题图与解析并穷尽 10/10 边；content auditor 另查 GS-421/422，确认 GS-421 不是重复题而是正式语义串入 GS-422，登记 `NEEDS_CONTENT_REPAIR`。
- 逐题结果：五卡删除会参与 fine_knowledge 的“定积分应用/定积分物理应用”，分别换成变力做功、抽水做功、静水压力或流量环形精确节点。GS-418 同时保留变力做功母链与抽水子型；个人 wrong_point、error_causes、method_gap 和掌握度分数均不改。
- 关系裁决：7 条 stored 为 `KEEP=2 / NEEDS_USER=5`；双路只确认 GS-415↔418 和 GS-419↔420，其余五边虽双路判弱但 canonical KEEP，按降级与 zero-outgoing 门禁冻结。3 条内部 ADD 全部双路拒绝，owner/challenger 冲突 0。
- GS-421 边界：5 条 external ADD 与既有 GS-421↔422 全部冻结；`solution_02` 只支持投影几何且含方向反转/无关做功语言，正确符号与结果以 question_01 和 solution_01 为准。内容修复须同时覆盖正式卡、视觉详情、manifest/index 与 source summary。
- 累计计划：M166 的 250 张 carry 与本批 5 张合为 255 张；累计删除 287 条逻辑边的 336 个 occurrence，累计 19 条逻辑新增和 3 条 storage normalization。255/255 before/preview/approved 哈希通过。
- 投影：首轮最小 knowledge 暴露 415-418 缺共同 fine node 的反例；二次独立裁决补 GS-418 的“变力做功积分”父节点。最终 `MATHWIKI-MAINT-167-R2-9d2c66745a8e` 为 `PASS / issues=[]`；confirmed KEEP 两边均由精确 fine knowledge 复现，五条异量纲 stored 边均为 REMOVE_CANDIDATE 且冻结保留，三条拒绝 ADD 只留 DERIVED_ONLY/0 storage；sentinel+inbound 保持 33，`new_zero_outgoing_cards=[]`。
- 验收：M167 定向测试 `19/19 OK`、完整单元测试 `345/345 OK`；selection/decisions/plan/draft/projection 哈希门禁通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-167_第十六批5卡定积分物理微元闭包逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-167]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-168 第十七批 5 卡一阶微分方程入口闭包逐题复核及累计 SHADOW 投影

- 选批：从 prior-review union 313 外选择 GS-187、GS-188、GS-189、GS-198、GS-199；14 条 stored edge/17 个 occurrence 与 1 条内部 ADD 全部闭合，总复核 15 边；21 条批外 ADD 冻结，4 个 external stored endpoint 补齐身份与方法证据。
- 视觉复核：owner、未读取 owner 结论的独立 challenger 各自查看 selected 题图与解析 5/5、external stored endpoint 4/4，并穷尽 15/15 边；五卡身份均 PASS。GS-188 解析首步存在局部正负号笔误但题图、后续推导与正式卡一致；GS-193 仅有答案图，方法证据从严。
- 逐题结果：GS-187/188 分配齐次与平移，GS-189 分配一阶线性与周期解，GS-198 分配一阶线性与指数函数求导，GS-199 分配根式整体换元；删除会参与 fine score 的微分方程根节点和泛化换元节点。个人 wrong_point、error_causes、method_gap 和掌握度分数均不改。
- 关系裁决：`REMOVE=5 / KEEP=2 / NEEDS_USER=7 / REJECT_ADD=1`；六条 canonical KEEP 降级边与唯一 198-199 reviewer 分歧边冻结。内部 ADD 187-199 双路拒绝；21 条 external ADD 全部 0 storage。
- 原子保护：R1 删除 187-198 后暴露 GS-187 新 zero-outgoing/sentinel+inbound；两位 reviewer 只授权在同一事务补 GS-187→188 reciprocal occurrence。R2 中 187-188 为 KEEP_STRONG/2 occurrences，187-198 absent，sentinel 与 zero-outgoing 均回到 M167 基线。
- 累计计划：M167 的 255 张 carry 与本批 5 张合为 260 张；累计删除 292 条逻辑边的 343 个 occurrence，累计 19 条逻辑新增和 4 条 storage normalization。260/260 before/preview/approved 哈希通过。
- 投影：`MATHWIKI-MAINT-168-R2-a0e0b2e6da9d` 为 `PASS / issues=[]`；292 条 reviewed REMOVE 中 266 条消失、25 条只留派生、0 条有 storage。唯一 GS-587↔620 因候选槽变化重现为 ADD_STRONG proposal，但 M154 人工 REMOVE 结论仍绑定且 storage=0；sentinel+inbound 保持 33，`new_zero_outgoing_cards=[]`。
- 验收：M168 定向测试 `20/20 OK`、完整单元测试 `365/365 OK`；selection/decisions/R1 resolution/R2 plan/draft/projection 哈希门禁通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-168_第十七批5卡一阶微分方程入口闭包逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-168]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-169 第十八批 5 卡定积分几何生成量闭包逐题复核及累计 SHADOW 投影

- 选批：从 prior-review union 318 外选择 GS-297、GS-299、GS-300、GS-304、GS-305；唯一 stored incident GS-297↔674 按 M168 历史 REMOVE 绑定，不重复投票；3 条 internal ADD 全部双端闭合，26 条批外 ADD 冻结。
- 视觉复核：owner 与未读取 owner 结论的独立 challenger 各自查看 5/5 selected 题图与解析、GS-674 双证据，并独立复核 3 条 ADD 与 1 条 historical edge；content auditor 另查内容口径和重复身份。
- 逐题结果：删除会参与 fine score 的“定积分应用”；GS-297 改为函数方程+旋转体体积+水平切片，GS-299/300 改为变上限积分+曲线弧长，GS-304 补反常积分+Gamma型积分，GS-305 只挂旋转曲面面积。个人 wrong_point、error_causes、method_gap 和掌握度分数均不改。
- 关系裁决：297-304 与 299-300 双路 ADD，297-300 双路拒绝；前两边在 R1 为 `KEEP_STRONG / 2 occurrences`，拒绝边与历史 297-674 都 absent。26 条 external ADD 为 `9 absent / 17 proposal-only / 0 storage`。
- 来源与重复边界：GS-299 的 $y=\sqrt{\sin x}$ 只在开区间内满足经典可导条件；GS-305 解析只计侧面而题面写表面积，保持 `NEEDS_SOURCE_CONFIRMATION`。新确认 GS-301/302、GS-194/211 两组精确重复，均不自动 merge。
- 累计计划：M168 的 260 张 carry 与本批 5 张合为 265 张；累计删除 292 条逻辑边的 343 个 occurrence，累计 21 条逻辑新增和 4 条 storage normalization。265/265 before/preview/approved 哈希通过。
- 投影：`MATHWIKI-MAINT-169-R1-4f96b66c2d35` 为 `PASS / issues=[]`；292 条 reviewed REMOVE 中 267 条消失、25 条只留派生、0 条有 storage 或重现强候选；25 条 add/normalization 均为双端 KEEP_STRONG。sentinel+inbound 保持 33，zero-outgoing 从 111 降至 107，没有新增项。
- 验收：M169 定向测试 `17/17 OK`、完整单元测试 `382/382 OK`；selection/decisions/plan/draft/projection 哈希门禁通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-169_第十八批5卡定积分几何生成量闭包逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-169]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-170 第十九批 5 卡拐点、积分入口与多元极值闭包逐题复核及累计 SHADOW 投影

- 选批：从 prior-review union 323 外选择 GS-139、GS-167、GS-273、GS-279、GS-388；6 条 canonical stored edge/6 个 occurrence 全闭合，37 条批外 ADD 冻结；GS-273/279 为既有 zero-outgoing，不用泛积分节点强行补边。
- 视觉复核：owner 与未读取 owner 结论的独立 challenger 各自查看 5/5 selected 题图、6 个解析资产和 4 个 external endpoint，并穷尽 6/6 stored edge；content auditor 另查 GS-167、GS-525、GS-386 的证据边界。
- 逐题结果：GS-139/167 分流图像态凹凸与解析态拐点切线；GS-273 只保留分部积分+根式整体换元；GS-279 只保留有理函数积分+部分分式；GS-388 只挂多元函数极值，把特殊路径留在方法层。个人 wrong_point、error_causes、method_gap 和掌握度分数均不改；GS-388 仅安全追加待评分。
- 关系裁决：确认 KEEP 139-167、139-525、387-388、388-389；139-142、142-167 双路判弱，但二者都是 canonical KEEP_STRONG，按降级门禁只登记 NEEDS_USER 并保留原 storage；本批没有 REMOVE/ADD 动作。
- 证据与身份边界：GS-167 所谓 `y'=0` 笔误未复现；GS-525 没有 solution asset，但原 OO3 父子节点长解析可追溯闭包；GS-386 的 formal 13.25 与解析页眉/教材 13.26 错配已确认，继续冻结；GS-273 保留实数定义域 caveat。
- 累计计划：M169 的 265 张 carry 与本批 5 张合为 270 张；累计删除仍为 292 条逻辑边/343 个 occurrence，累计 21 条逻辑新增和 4 条 storage normalization。270/270 before/preview/approved 哈希通过。
- 投影：`MATHWIKI-MAINT-170-R1-30696b262520` 为 `PASS / issues=[]`；292 条 reviewed REMOVE 中 266 条消失、26 条只留派生、0 条有 storage 或重现强候选；25 条 add/normalization 均为双端 KEEP_STRONG。4 条确认边和 2 条人工弱边都保留原 storage；sentinel+inbound 保持 33，zero-outgoing 保持 107。
- 验收：M170 定向测试 `15/15 OK`、完整单元测试 `397/397 OK`；selection/decisions/plan/draft/stage/projection 哈希门禁通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-170_第十九批5卡拐点积分入口与多元极值闭包逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-170]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-171 第二十批 5 卡隐函数、ODE、曲率逻辑与向量表示逐题复核及累计 SHADOW 投影

- 选批：从 prior-review union 328 外选择 GS-128、GS-164、GS-190、GS-149、LA-097；14 条 stored incident 中 3 条历史 SHA 绑定、11 条进入本批双路投票；19 条批外 ADD 冻结。
- 视觉复核：owner 与未读取 owner 结论的独立 challenger 各自查看 5/5 selected 题图与解析、9 个 external endpoint，并独立复核 11/11 stored edge；content auditor 另查五张身份、四个文字解析端点和 LA-097 provenance alias。
- 逐题结果：GS-128 只留隐函数求导+法线方程；GS-164/190 用一阶线性方程分流法线最值与弧长；GS-149 用曲率+Taylor+充分必要；LA-097 用列向量线性表示+列向量关系转齐次解替换泛标签。个人 wrong_point、error_causes、method_gap、掌握度分数和 mastery_history 均不改。
- 关系裁决：6 条双路 KEEP；128-164、143-149、148-149、LA092-LA097 为 reviewer conflict；128-540 双路判弱。后五条全进 NEEDS_USER 并保留原 storage，本批没有 REMOVE/ADD。LA097-99/100 虽因精确标签在自动审计显示 REMOVE_CANDIDATE，但双路人工证据成立，作为 human-evidence-only KEEP 保留。
- 证据与身份边界：GS-143/148/538/540 只有题图与 SHA 绑定完整文字解析，不伪称解析图；LA-097 的 MN4 alias 是同源 provenance；GS-128 唯一性有非阻塞严谨措辞 caveat，GS-190 有来源口头标签 caveat；GS-421/386 继续冻结。
- 累计计划：M170 的 270 张 carry 与本批 5 张合为 275 张；累计删除仍为 292 条逻辑边/343 个 occurrence，累计 21 条逻辑新增和 4 条 storage normalization。275/275 before/preview/approved 哈希通过。
- 投影：`MATHWIKI-MAINT-171-R1-75c10ff06d20` 为 `PASS / issues=[]`；292 条 reviewed REMOVE 中 266 条消失、26 条只留派生、0 条有 storage 或重现强候选；25 条 add/normalization 均为双端 KEEP_STRONG。6 条 KEEP 和 5 条 NEEDS_USER 均保持原 storage；sentinel+inbound 保持 33，zero-outgoing 保持 107。
- 验收：M171 定向测试 `15/15 OK`、完整单元测试 `412/412 OK`；selection/decisions/plan/draft/stage/projection 哈希门禁通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-171_第二十批5卡隐函数ODE曲率逻辑与向量表示逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-171]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-173 第二十二批 4 卡伴随矩阵机制分流逐题复核及累计 SHADOW 投影

- 选批：从 prior-review union 334 外选择 LA-049、LA-050、LA-055、LA-060；11 条 stored incident 中 10 条进入双路投票，060-073 只因 owner closure 延后；两条 external ADD 冻结。
- 身份纠偏：LA-073 与 GS-124 只是跨学科同名“强化例题4.9”，subject/refid/题图 SHA/内容均不同；已标为 `IDENTITY_PASS_CROSS_SUBJECT_LOCATOR_ALIAS`，不再误称来源未收口。
- 逐题结果：LA-049 精分为行列式+矩阵秩+代数余子式，LA-050 为行列式+二次型，LA-055 为行列式+初等变换，LA-060 为逆矩阵+行列式；矩阵运算章节根、泛伴随对象和方法标签留在 chapter/methods/keywords。个人字段、掌握度分数和 M173 mastery_history 均不改。
- registry 加固：新增 section-aware `formal_knowledge_registry_math.py`，只允许三个正式学科段与历史正式细分知识段；阻止 `矩阵初等变换`、`分块矩阵方程` 等方法标签混入新批 knowledge。
- 关系裁决：双路 KEEP 049-050、049-074、060-074；双路 REMOVE 7 条。50-74、55-74 两条自动弱边进入 SHADOW 删除；另 5 条 canonical KEEP_STRONG 双路判弱，按安全政策转 NEEDS_USER 并保留原 storage；060-074 是 human-evidence-only KEEP。
- 累计计划：M172 carry 277 张 + 本批 4 张，共 281 张；累计删除 294 条逻辑边/345 个 occurrence，累计 21 条逻辑 ADD + 5 条 storage normalization。preview 累计变更 170 knowledge、228 related、108 条历史安全待评分记录。
- 投影：`MATHWIKI-MAINT-173-R1-FINAL-dc987d7b63c7` 为 `PASS / issues=[]`；294 条 reviewed REMOVE 中 266 条消失、28 条只留派生、0 条有 storage 或重现强边；两条本批 REMOVE 为 1 absent + 1 derived-only。sentinel+inbound 32、zero-outgoing 106，均无新增/消失。
- 验收：M173 与公共 selection core 定向测试 `26/26 OK`、完整单元测试 `454/454 OK`；selection/decisions/plan/draft/stage/projection 哈希门禁通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-173_第二十二批4卡伴随矩阵机制分流逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-173]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-174 第二十三批 5 卡矩阵秩保核与 Frobenius 机制分流逐题复核及累计 SHADOW 投影

- 选批：从 prior-review union 338 外选择 LA-069～LA-073；19 条 stored incident 中 14 条进入双路投票，5 条只因 owner closure 延后；仅 072-073 为 internal ADD，11 条 external ADD 冻结。
- 身份与内容纠偏：LA-068/GS-114、LA-073/GS-124 均为跨学科同 locator 假碰撞，不合并；GS-114 正式卡正确，但视觉详情存在章节错标和三条错误泛化，登记为 `NEEDS_VISUAL_DETAIL_CONTENT_REPAIR` 并退出普通关系证据。
- 逐题结果：LA-069 为矩阵秩+线性方程组，LA-070 为初等变换+矩阵秩，LA-071/072 只保留矩阵秩，LA-073 为行列式+矩阵秩；矩阵运算泛根与具体定理名留在 methods。个人字段、掌握度分数和 M174 mastery_history 均不改。
- 关系裁决：14/15 票一致。双路 KEEP 6 条；68-71、68-72 双路 REMOVE 并进入 SHADOW 删除；072-073 双路 ADD 并规范为 reciprocal storage；5 条 canonical KEEP_STRONG 双路判弱但保留 storage；69-71 owner KEEP/challenger REMOVE，进入 NEEDS_USER。
- 累计计划：M173 carry 281 张 + 本批 5 张，共 286 张；累计删除 296 条逻辑边/347 个 occurrence，累计 22 条逻辑 ADD + 5 条 storage normalization。preview 累计变更 175 knowledge、232 related、108 条历史安全待评分记录。
- 投影：`MATHWIKI-MAINT-174-R1-FINAL-a1edcffdad42` 为 `PASS / issues=[]`；296 条 reviewed REMOVE 中 269 条消失、27 条只留派生、0 条有 storage 或重现强边；27 条 add/normalization 均为双端 KEEP_STRONG。sentinel+inbound 32、zero-outgoing 106，均无新增/消失。
- 验收：M174 定向测试 `15/15 OK`、M173 继承链 + M174 全链 `21/21 OK`、完整单元测试 `472/472 OK`；selection/decisions/plan/draft/stage/projection 哈希门禁通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-174_第二十三批5卡矩阵秩保核与Frobenius机制分流逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-174]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-175 第二十四批 3 卡向量组表示与参数分类逐题复核及 LA-099 内容隔离累计 SHADOW 投影

- 选批：从 prior-review union 343 外选择 LA-092、LA-093、LA-100；12 条 stored incident 分为 2 条历史裁决、8 条净新结构闭合、2 条 LA-098 owner-deferred；11 条 external ADD 冻结。
- 逐题结果：三张 selected 正文均 PASS；LA-093 把决定性的“参数分类讨论”提升到 formal knowledge，LA-092/100 knowledge 保持原值并作为 reviewed no-op 不进入 stage。个人错因、method_gap、掌握度和 mastery_history 均不改。
- 关系裁决：仅 075-100 双路 KEEP；092-093 双路 REMOVE 但 canonical 为 KEEP_STRONG，保留 storage 待用户授权；5 条 owner/challenger conflict 不由 root 强裁。M171 的 092-097/097-100 不重投。
- 内容纠偏：发现 LA-099 把“$A$ 可由 $B$ 表示”写成反方向并误答 `a=-2`。独立秩计算为：`a=1` 时 `r(A/B/B,A)=1/3/3` 满足，`a=-2` 时 `2/2/3` 不满足，正确答案应为 `a=1`。涉及 LA-099 的 3 条净新边全部 content-blocked。
- 累计隔离：从 M174 carry 移除 LA-099，撤回 090-099 REMOVE 与 075-099 reciprocal normalization，并按 canonical storage 恢复原状态；LA-090 回滚后成为 no-op 同步移出。最终 285 张 preview，累计 295 REMOVE/345 occurrences、22 logical ADD + 4 normalization。
- 投影：`MATHWIKI-MAINT-175-R1-FINAL-a85612f2e5c5` 为 `PASS / issues=[]`；295 条 reviewed REMOVE 中 269 条消失、26 条只留派生，0 条有 storage 或重现强边；sentinel+inbound 32、zero-outgoing 106，均无新增/消失。
- 验收：M175 selection/decisions/projection + M174 projection 回归定向测试 `20/20 OK`，完整单元测试 `487/487 OK`；Obsidian 搜索 4 命中、outline 与 log backlink 回读正常。正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-175_第二十四批3卡向量组表示与参数分类逐题复核及LA099内容隔离累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-175]]。

## [2026-07-11] maintenance | MATHWIKI-MAINT-172 第二十一批 2 卡自然参数弧长与极坐标参数化逐题复核及累计 SHADOW 投影

- 选批：从 prior-review union 333 外选择 GS-298 作为唯一零 deferred singleton，并把 prior-reviewed GS-682 作为 dependency revalidation；闭合 5 条 stored edge/5 个 occurrence，11 条 external ADD 冻结。
- 视觉复核：owner 与未读取 owner 结论的独立 challenger 各自查看 2/2 selected 题图与解析并穷尽 5/5 stored edge；content auditor 另查双端身份、答案、4 个 external endpoint 和分段光滑证据边界。
- 逐题结果：GS-298 用反函数求导+曲线弧长+单调性与极值替换泛定积分与参数方程求导；GS-682 保留极坐标、参数方程、参数方程求导、曲线弧长与三角恒等变形，分别覆盖入口、必要计算链和确认漏项。个人字段与掌握度分数均不改；GS-298 preview 仅携带一条安全待评分来源。
- 关系裁决：298-682、469-682、595-682、644-682 双路 KEEP；681-682 reviewer conflict，保留 canonical `KEEP_STRONG` 原 storage；本批没有 REMOVE 或逻辑 ADD，11 条 external ADD 全部 0 storage。
- R1→R2：R1 证明 GS-298 仍为有入边、无出边 sentinel；双路只授权补 GS-298→682 reciprocal occurrence。R2 保持逻辑边数不变，把 sentinel+inbound 33→32、zero-outgoing 107→106，且无新增项。
- 证据边界：GS-298 极值点按 $x=x(y)$ 连续延拓理解，不泛称普通反函数定理直接成立；GS-469/595 无 solution asset，只用 SHA 绑定完整文字解析；GS-595/644/681 公式按分段光滑积分理解；GS-421/386 与四组重复候选继续冻结。
- 累计计划：M171 的 275 张 carry 与本批 2 张合为 277 张；累计删除 292 条逻辑边/343 个 occurrence，累计 21 条逻辑 ADD 和 5 条 storage normalization。277/277 before/preview/approved 哈希通过。
- 投影：`MATHWIKI-MAINT-172-R2-FINAL-0b464550eb69` 为 `PASS / issues=[]`；292 条 reviewed REMOVE 中 266 条消失、26 条只留派生、0 条有 storage 或重现强候选；26 条 add/normalization 均为双端 KEEP_STRONG；冻结 external ADD 为 `9 proposal / 2 absent / 0 storage`。措辞冻结只重绑 decisions/plan/draft SHA，card projection 不变。
- 验收：M172 与公共 selection core 定向测试 `23/23 OK`、完整单元测试 `435/435 OK`；selection/decisions/R1 resolution/R2 plan/draft/stage/projection 哈希门禁通过，正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-172_第二十一批2卡自然参数弧长与极坐标参数化逐题复核及累计SHADOW投影_2026-07-11|MATHWIKI-MAINT-172]]。

## [2026-07-12] maintenance | 数学错题入库恢复为单题同步串行

- 用户决策：停用数学多题并发入库；以后所有明确单题入库口令默认由 `kaoyan-math-wrong-intake` 一题一结算。
- 路由调整：`kaoyan-math-question-worker` 仅负责当前题学习与事实整理；`kaoyan-math-intake-coordinator` 仅负责既有 MATH-JOB/WAL/receipt 的历史检查和串行恢复；daily-filter 与 visual-review 已同步改用新的单题路由。
- 事务约束：`MAX_REVIEWING=1`，协调器 `claim` 固定一次一题，`batch` 拒绝多 job；内部 audit job、WAL、receipt 和 strict gate 继续保留，质量门不降低。
- 运行模式：generation 1 已从 `SHADOW` 切换为 `SUPERVISED`，并写入 `serial_intake=true`；只有当前明确单题和匹配 batch ID 的监督确认可正式写入。
- 历史状态：运行时现有 34 条记录保持原样（30 REVIEWED、4 FAILED），不自动提交、不删除、不改写。
- 边界：本次未修改正式错题卡、`生成/**`、视觉正式层、Tutor 或回滚 JSON；未运行 wrongnet rebuild。

## [2026-07-12] maintenance | MATHWIKI-MAINT-176 第二十五批 3 卡逆矩阵结构化求法逐题复核及跨代内容隔离累计 SHADOW 投影

- 选批：从 M175 后剩余 43 张严格候选中选择 LA-052、LA-053、LA-054；4 条 stored incident 分为 3 条完全内部闭合与 1 条 LA-039 owner/job 双边界 deferred；`053-060` external ADD 冻结，剩余严格候选 40 张。
- 逐题结果：三卡正式卡、唯一题图与解析图均核对；LA-052 的 `A=J-E` 构造正确，但严格需 `n>1`，只登记非阻塞 caveat，不冒充已修正式正文；LA-053/054 内容 PASS。三卡 personal error evidence 均为 low。
- knowledge 裁决：三卡统一收紧为 `[逆矩阵]`；owner 与 challenger 对是否保留“矩阵运算”泛根有分歧，root 按 M173/M174 严格口径移除泛根，将全一矩阵、矩阵多项式除法、幂零与有限级数保留在 methods/keywords。
- 关系裁决：052-053、052-054、053-054 双路一致 KEEP；第三条虽然 audit 为 `REMOVE_CANDIDATE`，两位 reviewer 均以多项式除法特例给出可复现人工证据。本批 0 REMOVE / 0 ADD / 0 normalization，原 storage 保持。
- 跨代隔离：LA-099 继续由 M175 content quarantine 继承，不进入 plan/draft/stage；075-099 与 090-099 保持原 storage。本批不重复执行隔离动作，也不把“本轮新隔离为空”误读成解除隔离。
- 累计计划：288 张 preview，累计 295 REMOVE/345 occurrences、22 logical ADD + 4 normalization；本批三卡 changed fields 仅 knowledge。draft/stage 288/288 回读一致，formal_write_attempted=false。
- 投影：`MATHWIKI-MAINT-176-R1-FINAL-9b877fc99399` 为 `PASS / issues=[]`；801 卡、3618 边、simulated 2187 strong / 581 medium、410 remove candidates；sentinel+inbound 32、zero-outgoing 106，均无新增/消失。
- 验收：M176 selection/decisions/projection + M175 projection 回归定向测试 `20/20 OK`，完整单元测试 `502/502 OK`；正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-176_第二十五批3卡逆矩阵结构化求法逐题复核及跨代内容隔离累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-176]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-177 第二十六批 4 卡参数二阶导与 Hessian 双闭包逐题复核及累计 SHADOW 投影

- 选批：从 M176 后剩余 40 张严格候选中选择 GS-123、GS-169、GS-391、GS-392；10 条 stored incident 中 8 条进入双路投票，115-123 因 owner/job 边界 deferred，386-391 因 owner/content-repair 边界 deferred；24 条 external ADD 冻结，剩余严格候选 36 张。
- 证据闭包：selected 4/4 q+s；GS-390/396/499/579/650 为 q-only，但两名 reviewer 均逐卡核对正式卡完整文字解。GS-390 保留 locator caveat；GS-169/650 是 `a=1` 特例与 `a>0` 一般化，不作为资产重复。
- 逐题结果：GS-123/169 分别以参数二阶导链和曲率收口；GS-391/392 分别以 Hessian 排除内部极值和建立极大值充分条件收口，四卡内容均 PASS。个人错因证据 low，不修改 wrong_point、error_causes、method_gap、掌握度或 wrong_history。
- knowledge 裁决：GS-123 收紧为参数方程求导+高阶导数，GS-169 收紧为曲率+参数方程求导+高阶导数；移除一元微分泛根，把复合/链式求导留在 methods。GS-391/392 保持多元函数极值+多元函数偏导。
- 关系裁决：123-169/499/579/650、169-650、390-392、391-392/396 共 8 条双路一致 KEEP；每条均有参数二阶导、曲率缩放、Hessian 符号或闭域最值候选生成的具体机制。本批 0 REMOVE / 0 ADD / 0 normalization，原 storage 保持。
- 累计计划：290 张 preview，累计 295 REMOVE/345 occurrences、22 logical ADD + 4 normalization；本批实际 repair target 只有 GS-123/169，GS-391/392 为 reviewed no-change。GS-123 related 只做确定性顺序规范化；LA-099 跨代隔离继续生效。
- 投影：`MATHWIKI-MAINT-177-R1-FINAL-7b5509a86fd8` 为 `PASS / issues=[]`；801 卡、3616 边、simulated 2187 strong / 582 medium、410 remove candidates；sentinel+inbound 32、zero-outgoing 106，均无新增/消失。8 条 candidate-only 移除与 6 条新增均为 0 storage，declared network 不变。
- 验收：M177 selection/decisions/projection + M176 projection 回归定向测试 `22/22 OK`，完整单元测试 `518/518 OK`；正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-177_第二十六批4卡参数二阶导与Hessian双闭包逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-177]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-178 第二十七批 3 卡行列式机制分流与健康孤立逐题复核及累计 SHADOW 投影

- 选批：从 M177 后剩余 36 张严格候选中选择 LA-009、LA-010、LA-020；5 条 stored incident 分为 3 条完全内部 covered 和 2 条 LA-019 owner/evidence deferred；4 条 external ADD 冻结，剩余严格候选 33 张。
- 逐题结果：三卡 q+s、正式卡和答案均独立复算通过。LA-009 是排列展开指定幂次筛选，答案 -5；LA-010 是行变换化分块上三角并补验 `a=0`，结果 `a^4-4a^2`；LA-020 是余子式和转伴随/逆矩阵并用反对角分块，答案 -4。
- knowledge 裁决：三卡统一移除“矩阵运算”泛根；LA-009 只留行列式，LA-010 收紧为行列式+初等变换+参数分类讨论，LA-020 收紧为行列式+逆矩阵+代数余子式。个人错因证据 low，不修改 wrong_point、error_causes、method_gap、掌握度或 wrong_history。
- 关系裁决：009-010、009-020、010-020 三条双路一致 REMOVE，共删除 6 个 reciprocal occurrence；只共享行列式/矩阵运算或泛化分块不足以支撑强关系。009-019、019-020 因 LA-019 q-only、无 solution asset 且 owner 外闭包而保持原 storage。
- 健康孤立：删除后 LA-010 declared incoming/outgoing 均为空，zero-outgoing 106→107；sentinel-with-inbound 仍为 32 且无新增。它仍可通过行列式、初等变换、参数分类讨论和 `L03-009` 检索，不能为了连通性伪保留弱边。
- 累计计划：293 张 preview，累计 298 REMOVE/351 occurrences、22 logical ADD + 4 normalization；本批三卡 changed fields 均为 knowledge+related。LA-099 跨代内容隔离继续生效。
- 投影：`MATHWIKI-MAINT-178-R1-FINAL-93e611741614` 为 `PASS / issues=[]`；801 卡、3614 边、simulated 2188 strong / 581 medium、407 remove candidates；本批三条删除边为 1 derived-only + 2 absent，0 storage/0 strong re-add，且没有额外 candidate-only churn。
- 验收：M178 selection/decisions/projection + M177 projection 回归定向测试 `22/22 OK`，完整单元测试 `534/534 OK`；Obsidian 搜索、outline 与 log backlink 回读正常；正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-178_第二十七批3卡行列式机制分流与健康孤立逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-178]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-179 第二十八批 3 卡跨专题机制精分与 LA-081 内容隔离逐题复核及累计 SHADOW 投影

- 选批：从 M178 后剩余 33 张严格候选中选择 GS-168、GS-295、LA-078；10 条 stored incident 分为 1 条 M161 历史绑定、4 条新证据审核和 5 条 owner/evidence deferred；14 条 external ADD 冻结，剩余严格候选 30 张。
- 逐题结果：GS-168 部分分式后反常收口，结果 `(1/2)ln2`；GS-295 面积依赖加时间链式，结果 10；LA-078 行空间/零空间维数封闭并以 `B^T` 列满秩判唯一解，选 C。三题内容 PASS，个人错因证据 low，不反推 wrong_point/error_causes/method_gap/掌握度。
- knowledge 裁决：GS-168 收紧为反常积分+有理函数积分+部分分式；GS-295 收紧为定积分应用+平面图形面积+变上限积分+相关变化率；LA-078 收紧为线性方程组+矩阵秩+向量组线性无关。
- 关系裁决；168-604 与 262-295 双路一致 KEEP；168-637 双路一致 REMOVE，删除 1 个 occurrence；033-078 绑定 M161 high-confidence KEEP，不重投。
- 内容隔离：LA-081 题图未给 `A!=0`/`Aalpha!=0`，正式卡却增写该条件；取 `A=O_2`、`alpha=(1,0)^T` 即使 `P=[alpha,Aalpha]` 奇异。078-081 转 `NEEDS_CONTENT_REPAIR`，累计计划中 033-081/064-081 两条旧删除同步撤回；LA-081 不进入 stage，LA-033 因撤回后 no-op 剪枝。
- 累计计划：294 张 preview，累计 297 REMOVE/350 occurrences、22 logical ADD + 4 normalization；draft/stage 294/294 回读一致。GS-295 新增的只是“本轮无用户作答证据”安全待评分历史，不是掌握度分数。
- 投影：`MATHWIKI-MAINT-179-R1-FINAL-85159b3aa295` 为 `PASS / issues=[]`；801 卡、3616 边、declared 1609、simulated 2188 strong / 581 medium、408 remove candidates；sentinel+inbound 32、zero-outgoing 107，均无新增/解除。candidate-only churn 为删 6/加 7，全部 0 storage。
- 验收；M179 selection/decisions/projection 定向测试 `17/17 OK`，完整单元测试 `551/551 OK`；generic selection gate 与 projection audit gate 均 PASS；正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-179_第二十八批3卡跨专题机制精分与LA-081内容隔离逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-179]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-180 第二十九批 3 卡极限机制分流与 GS-237 余项论证隔离逐题复核及累计 SHADOW 投影

- 选批：从 M179 后 30 张严格候选中选择 GS-003、GS-014、GS-072；5 条 covered incident 双路审核，3 条 owner 外闭包 deferred，15 条 external ADD 冻结。移除 selected 后 raw remaining 27 张，再因 GS-237 内容隔离得 safe remaining 26 张。
- 逐题结果：三卡 q+s，两名 reviewer 实看资产、正式卡并独立复算通过；GS-003 结果 `1/2`，GS-014 选 C（010304），GS-072 选 D。个人错因证据 low，不反推 wrong_point/error_causes/method_gap/掌握度。
- knowledge 裁决：GS-003 收紧为函数极限+洛必达法则+泰勒公式+等价无穷小+变上限积分；GS-014 为函数极限+等价无穷小+无穷小阶数比较；GS-072 为数列极限+函数极限，三卡均移除“极限与连续”泛根。
- 关系裁决：003-072、014-072 双路一致 REMOVE，删除 3 个 storage occurrence；003-440/585/649 双路一致 KEEP，共享变上限积分、洛必达消积分号和后续主导项收口链。031-072、037-072、072-165 按 owner/evidence/历史冲突边界 deferred。
- 健康孤立：删边后 GS-014 declared 无入无出，zero-outgoing 107→108；sentinel-with-inbound 仍 32。它仍可通过三个严格 knowledge 与 `H01-004` 检索，不为连通性伪保留弱边。
- 内容隔离：GS-237 答案 D 正确，但现有卡/视觉页将逐点存在的拉格朗日余项点 `xi_x` 直接积分，未证明可测选择。标记 `NEEDS_CONTENT_REPAIR_LAGRANGE_REMAINDER_QUANTIFIER`，建议改用严格凸性/Hermite-Hadamard 或先逐点保号再积分；累计计划撤回 237-665 旧删除，恢复 GS-665→GS-237 的 1 个 occurrence。
- 累计计划：297 张 preview，累计 298 REMOVE/352 occurrences、22 logical ADD + 4 normalization；draft/stage 297/297 回读一致。LA-081、LA-099、GS-237 三张 content quarantine 不进入 stage。
- 投影：`MATHWIKI-MAINT-180-R1-FINAL-c519d77b7e06` 为 `PASS / issues=[]`；801 卡、3617 边、declared 1608、simulated 2187 strong / 582 medium、407 remove candidates；累计删除 270 absent + 28 derived-only，0 storage/0 strong re-add。candidate-only churn 删 9/加 10，全部 0 storage。
- 验收：M180 定向测试 `15/15 OK`，完整单元测试 `566/566 OK`；generic selection gate 与 projection audit gate 均 PASS。正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-180_第二十九批3卡极限机制分流与GS-237余项论证隔离逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-180]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-181 第三十批 3 卡跨专题保守精分与证据身份污染隔离逐题复核及累计 SHADOW 投影

- 选批：从 M180 剩余 26 张严格候选中选择 GS-032、GS-398、GS-262；三路 reviewer 实看 3/3 q+s 并独立复算。移除 selected 后 raw remaining 23 张，再隔离 GS-005/137 后 remaining 21 张。
- 逐题结果：GS-032 四个间断点与分类正确；GS-398 换序后求导得 `(pi/2)cos(2/pi)`；GS-262 相关变化率建模得上升速度 5（D）。三题都没有新用户作答证据，不改个人字段。
- knowledge 裁决：GS-032 收紧为幂指极限+间断点分类；GS-398 为二重积分+二重积分换序+变上限积分；GS-262 为相关变化率+复合函数求导+反三角函数求导。
- 关系边界；9 条 stored incident 中 262-295 继承 M179 双路 KEEP，其余 8 条因 outside owner/证据闭包 deferred；10 条 external ADD 全冻结。本批新 REMOVE/ADD/normalization 均为 0，三卡 related storage 不变。
- 身份隔离：新登记 GS-403/405/408/414、GS-137/166、GS-093/108、GS-401/412、LA-094/096 五组重复身份；GS-087/213/399/402/410/639、LA-058 因 incident 端点污染改走专项身份路线。
- 内容隔离；GS-005 q+s/答案正确，但正式摘要缺真实题式且 lecture_refs 待补；LA-095 线代卡错绑了高数 GS-208 的中值定理 q+s。两者均不进入普通关系审批。
- 措辞 caveat；GS-307 的最小正周期为 `pi`，`2pi` 仍是一个周期，故答案 0 正确；后续只修“以2pi为一个周期”的措辞。
- 累计计划：300 张 preview，累计 298 REMOVE/352 occurrences、22 logical ADD + 4 normalization；draft/stage 300/300 回读一致。LA-099、LA-081、GS-237、GS-005、LA-095 均未进入 stage。
- 投影：`MATHWIKI-MAINT-181-R1-FINAL-61a4e9f51da9` 为 `PASS / issues=[]`；801 卡、3620 边、declared 1608、simulated 2187 strong / 584 medium、407 remove candidates；sentinel 32、zero-outgoing 108，均无新增/解除。candidate-only churn 删 12/加 15，全部 0 storage。
- 验收：M181 定向测试 `13/13 OK`，完整单元测试 `579/579 OK`；generic selection gate 与 projection audit gate 均 PASS。正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：coordinator 仍为 SHADOW；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-181_第三十批3卡跨专题保守精分与证据身份污染隔离逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-181]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-182 GS-406 参数曲线积分精分与 LA-068 矩阵符号错录隔离逐题复核及累计 SHADOW 投影

- 选批：从 M181 remaining 21 张选择 GS-406；q+s 实看并独立复算 `3pi^2+5pi` 通过。去掉 GS-406 的“定积分”关系泛根，knowledge 收紧为二重积分+参数方程求导；移除 selected 后 raw remaining 20 张，再隔离 LA-068 后 remaining 19 张。
- 关系边界：397-406、404-406 双路语义倾向 REMOVE，但 GS-397/404 缺独立 solution asset，且 397 还有 outside owner，均 deferred；406-409 owner KEEP / challenger REMOVE，H14-005 极坐标方法卡又与 GS-406 摆线参数边界入口错配，状态为 `NEEDS_METHOD_REFERENCE_REPAIR`，不冒充 KEEP、不发布删除。7 条 canonical external ADD 全冻结。
- 内容隔离：LA-068 q+s 第二行首项是 `-3/2`，正式摘要误写 `+3/2`；正号矩阵不满足 `M^2=9M`，答案 `9I_2` 只对负号原题正确。LA-068 不进 draft/stage，累计计划同步撤下 068-071/072 两条历史 REMOVE。
- 累计计划：301 张 preview，累计 296 REMOVE/350 occurrences、22 logical ADD + 4 normalization；draft/stage 301/301 回读一致。LA-099、LA-081、GS-237、GS-005、LA-095、LA-068 六张隔离卡均未进入 stage。
- 投影：`MATHWIKI-MAINT-182-R1-FINAL-e5a0f5ac7d98` 为 `PASS / issues=[]`；801 卡、3622 边、declared 1610、simulated 2187 strong / 584 medium、409 remove candidates；sentinel 32、zero-outgoing 108，均无新增/解除。相对 M181 仅恢复 068-071/072 各 1 个 storage occurrence。
- 验收：M182 定向测试 `13/13 OK`，完整单元测试 `592/592 OK`；generic selection gate 与 projection audit gate 均 PASS。正式卡 tree、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：投影只读观察到全局 coordinator 为 `SUPERVISED / generation=1`，但本批 decisions/draft/stage 仍是 SHADOW review，`formal_write_attempted=false`；未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-182_第三十一批GS-406参数曲线积分精分与LA-068矩阵符号错录隔离逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-182]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-183 GS-307 奇偶周期精分与 GS-095 视觉推导错式隔离逐题复核及累计 SHADOW 投影

- 选批：从 M182 remaining 19 张选择 GS-307；q+s 实看并独立复算答案 0 正确。最小正周期是 `pi`，`2pi` 仍是一个周期；正文措辞只登记待修，不判答案错。knowledge 去掉“一元函数微分学应用”泛根，收紧为高阶导数+函数奇偶性与导数性质+周期函数。
- 关系边界：只覆盖 307-308 双端 q+s，双向 storage 保持 KEEP；121/457/530 因无独立 solution asset deferred，115 因 owner 闭包外且有 REVIEWED 非终态 job deferred。本批 0 REMOVE / 0 ADD / 0 normalization。
- 内容隔离：GS-095 视觉详情把正确的 `4(a+b)+4a=0` 写成 `4a+2(a+b)=0`，错误方程不能推出页面随后的系数；正式 `lecture_refs` 也未链接已存在 q+s。GS-095 退出普通关系批，不进入 draft/stage，未来关系 bundle 等内容与链接修复后重审。
- 累计计划：302 张 preview，累计 296 REMOVE/350 occurrences、22 logical ADD + 4 normalization；draft/stage 302/302 回读一致。七张 content block 均未进入 stage；GS-307 related 只做确定性顺序规范化，集合与语义不变。
- 投影：`MATHWIKI-MAINT-183-R1-FINAL-dffe2fe9692a` 为 `PASS / issues=[]`；801 卡、3622 边、declared 1610、simulated 2187 strong / 584 medium、409 remove candidates；相对 M182 无 storage、edge-set、verdict、sentinel 或 zero-outgoing 变化。
- 验收：M183 定向测试 `12/12 OK`，完整单元测试 `604/604 OK`；generic selection gate 与 projection audit gate 均 PASS。canonical 正式审计、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：全局 coordinator 虽为 `SUPERVISED / generation=1`，本批仍是 SHADOW review；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-183_第三十二批GS-307奇偶周期精分与GS-095视觉推导错式隔离逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-183]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-184 GS-099 导数定义型极限精分与全边证据冻结逐题复核及累计 SHADOW 投影

- 选批：从 M183 remaining 17 张选择 GS-099；q+s/正式卡一致，独立复算先得 `f(1)=0`，再按 `e^(x^2)-1` 与 `sin^2x` 两个真实增量拆差商，答案 `f'(1)=-1`。remaining 16 张。
- knowledge 裁决：收紧为导数定义、导数定义型极限、复合自变量、自变量增量、极限条件反推导数；删除“一元函数微分学应用”和普通“函数极限”，等价无穷小留在 methods。H03-001 绑定正确。
- 关系边界：5 条 stored 语义倾向为 087/091/458/530 KEEP、095 REMOVE，但 GS-087 等待 identity-adjacent 闭包，GS-095 已 content-blocked，GS-091/458/530 q-only，且 087/095 有外部 owner；全部 deferred，0 relation action。4 条 canonical ADD 全冻结。
- 顺序保护：R1 因计划器机械重排 related 未采用；新增可选显式保序能力后生成 R2，GS-099 preview changed fields 只有 knowledge，正式 related 源顺序保持。旧批次未提供字段时行为不变。
- 累计计划：303 张 preview，累计 296 REMOVE/350 occurrences、22 logical ADD + 4 normalization；R2 draft/stage 303/303 回读一致，七张 content block 均未进入 stage。
- 投影：`MATHWIKI-MAINT-184-R2-FINAL-590eef61f9bc` 为 `PASS / issues=[]`；801 卡、3623 边、declared 1610、simulated 2187 strong / 584 medium、409 remove candidates。相对 M183 无 storage/共同 verdict/sentinel/zero 变化；candidate-only edge +5/-4，均 0 storage。
- 验收：M184 定向测试 `12/12 OK`，完整单元测试 `616/616 OK`；generic selection gate 与 projection audit gate 均 PASS；canonical 正式审计、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：全局 coordinator 为 `SUPERVISED / generation=1`，本批仍是 SHADOW review；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-184_第三十三批GS-099导数定义型极限精分与全边证据冻结逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-184]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-185 GS-687 反常积分精分、LA-057 无改动复核与 LA-039 整题串卡隔离逐题复核及累计 SHADOW 投影

- 选批：从 M184 remaining 16 张选择 GS-687、LA-057；两卡 q+s、正式卡和视觉页 identity/content 均 PASS。GS-687 独立复算 `pi-2ln2`，LA-057 独立复算 `A^10=B(CB)^9C`；remaining 14 张。
- knowledge 裁决：GS-687 收紧为反常积分、分部积分、根式换元、反正切型积分、反三角函数主值、对数型积分、等价无穷小；LA-057 的矩阵运算、矩阵秩保持，登记 reviewed-no-change。两卡均不改个人错因、method_gap、掌握度或 wrong_history。
- 关系裁决：唯一执行动作是新增 637-687 双向强边；677-687、686-687 KEEP，266-687/687-689 受 q-only/job 门禁 deferred。168-687 的 owner REMOVE / challenger KEEP 冲突冻结为 needs_user，保留现有 1 个 occurrence。
- 内容隔离：LA-039 正式卡/视觉/source summary 是“幂零链与秩稳定”，绑定 q+s 实为“二次型可逆线性变换”；登记整题串卡与 REVIEWED job，退出普通关系证据，不进入 draft/stage。
- 顺序保护：R1 暴露 carry 卡 GS-099.related 纯排序 churn，已保留为 superseded；显式开启 carry 保序后生成 R2。GS-099 changed fields 恢复为仅 knowledge，源顺序 `[458,087,091,530,095]`；GS-687 顺序 `[168,677,686,266,637]`。
- 累计计划：304 张 preview，累计 296 REMOVE/350 occurrences、23 logical ADD + 4 normalization；R2 draft/stage 304/304 回读一致，字段计数 knowledge 195 / related 240 / safe mastery 109。
- 投影：`MATHWIKI-MAINT-185-R2-FINAL-b9941606536b` 为 `PASS / issues=[]`；801 卡、3623 边、declared 1611、simulated 2187 strong / 584 medium、409 remove candidates。相对 M184 唯一 storage 变化是 637-687 从 0 到双向 2 occurrences；sentinel 32、zero-outgoing 108，均无新增/解除。
- 验收：M185 定向测试 `8/8 OK`，完整单元测试 `624/624 OK`；projection context SHA `73d755844a09640d9cc6e63abd39b44e6c53394a6594e6c197f848b6e162298c`；canonical 正式审计、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：本批仍是 SHADOW review；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-185_第三十四批GS-687反常积分精分与LA-057无改动复核及LA-039整题串卡隔离逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-185]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-186 GS-142 局部导数逻辑精分与 GS-165 错误复做提示隔离逐题复核及累计 SHADOW 投影

- 选批：从 M185 remaining 14 张选择 GS-142；q+s/正式卡/视觉页一致，A/C/D 反例与 B 的导函数连续保号链独立复算通过。移出 selected 后 13 张，再隔离 GS-165 后 safe remaining 12 张。
- knowledge 裁决：GS-142 收紧为函数单调性、导函数连续性、连续函数局部保号性、二阶导数判凹凸性；删除章节泛根、组合粗节点和方法层标签。相关方法卡继续待匹配，不反推个人错因、method_gap、掌握度或 wrong_history。
- 关系边界：7 条 stored 语义倾向已逐边复核，但外端 q-only 或 M170 historical KEEP_STRONG 降级冲突使 covered=0；8 条 canonical ADD 全冻结。edge_actions/normalization 均为 0，GS-142 related 顺序 `[452,138,525,490,508]` 原样保留。
- 内容隔离：GS-165 真实底数 `x+2^x->1`，正式复做提醒却写“趋向非1常数”；主解和答案 `4e^2` 正确，登记局部 `NEEDS_CONTENT_REPAIR_INCORRECT_REDO_TRIGGER`，修复回读后可重新入池。
- 累计计划：305 张 preview，累计 296 REMOVE/350 occurrences、23 logical ADD + 4 normalization；draft/stage 305/305 回读一致，字段计数 knowledge 196 / related 240 / safe mastery 109。GS-099、GS-687、GS-142 的 related 源顺序均受回归测试保护。
- 投影：`MATHWIKI-MAINT-186-R1-FINAL-74f2744590f2` 为 `PASS / issues=[]`；801 卡、3624 边、declared 1611、simulated 2187 strong / 584 medium、410 remove candidates。storage 无变化，raw candidate churn +28/-27 均为 0 storage；142-167 audit-only `KEEP_STRONG→REMOVE_CANDIDATE` 仍保留 1 occurrence 并受历史门禁保护；sentinel 32、zero-outgoing 108 无增减。
- 验收：M186 定向测试 `7/7 OK`，完整单元测试 `631/631 OK`；projection context SHA `f5f36397f8285acc26760a4fe2acf6dcef6f12366b525e4d9fec42d1aad261b4`；canonical 正式审计、生成层、知识点库、视觉 manifest 与回滚账本保持不变。
- 边界：本批仍是 SHADOW review；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-186_第三十五批GS-142局部导数逻辑精分与GS-165错误复做提示隔离逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-186]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-187 GS-193 二阶降阶与 GS-422 定积分物理应用分层逐题复核及累计 SHADOW 投影

- 选批：从 M186 remaining 12 张选择 GS-193、GS-422；两题 q+s/正式卡/视觉页一致，双路 reviewer 独立复算通过。remaining 10 张。
- 逐题结果：GS-193 令 `p=y'=p(y)` 得 `y=(x-1)^2/4+1`；GS-422 先取克服引力的 x 向分量，做功为 `G(1-1/sqrt(l^2+1))`，选 B。两题均不反推个人错因、method_gap、掌握度或 wrong_history。
- knowledge 裁决：GS-193 只保留二阶可降阶微分方程；GS-422 按 M173 后 section-aware 现行规则保留定积分应用+定积分物理应用。变力做功、引力做功和力的投影继续留在 methods，不跨层写入 formal knowledge。
- 关系边界：188-193/193-199 继承 M168 `needs_user`；192/204 语义 KEEP 但 owner 闭包不足；194/211 同 q+s/source 重复身份未收口。187/190 两条 ADD 双路 REJECT，本批 0 executable edge action。
- 内容隔离：GS-421 真实题是细杆引力分量，正式卡却整题串成 GS-422 移动点质量做功；421-422 保留 2 个 storage occurrences 并标记 `FROZEN_CONTENT_BLOCKED`。GS-422 的 7 条批外 ADD 全部不批准，415/418 最多为派生中关联。
- 累计计划：307 张 preview，累计 296 REMOVE/350 occurrences、23 logical ADD + 4 normalization；draft/stage 307/307 回读一致，字段计数 knowledge 198 / related 240 / safe mastery 109。
- 投影：`MATHWIKI-MAINT-187-R1-FINAL-87b7820c14d1` 为 `PASS / issues=[]`；801 卡、3620 边、declared 1611、simulated 2184 strong / 584 medium、410 remove candidates。相对 M186 无 storage/共同 verdict/sentinel/zero 变化；candidate-only churn +6/-10 均为 0 storage。
- 验收：M187 定向测试 `7/7 OK`，完整单元测试 `638/638 OK`；generic selection gate 与 projection audit gate 均 PASS；projection context SHA `438c8b756778c3dd5c9253ef400824a83d2e5e29715091331d58ab58b3ce4cef`。
- 边界：本批仍是 SHADOW review；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-187_第三十六批GS-193二阶降阶与GS-422定积分物理应用分层逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-187]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-188 GS-247 质心凸性错连清理与 GS-253 二阶 Taylor 精分逐题复核及累计 SHADOW 投影

- 选批：从 M187 remaining 10 张选择 GS-247、GS-253；两题 q+s/正式卡/视觉页一致，双路 reviewer 独立复算通过。remaining 8 张。
- 逐题结果：GS-247 的质心矩积分、变上限差值函数与二阶导判正链正确；GS-253 的对称端点/内部极值点二阶 Taylor 余项估值两问正确。不反推个人错因、method_gap、掌握度或 wrong_history。
- knowledge 裁决：GS-247 收紧为定积分应用+定积分不等式+二阶导数判凹凸性；GS-253 收紧为泰勒公式+局部极值。质心公式、拉格朗日中值定理、构造辅助函数、对称端点与最大值估计留在 methods。
- 关系动作：删除 247–256、247–492、247–593 三条 owner-closed 跨机制错连。183–247 因 canonical-strong 降级门禁保留为 `needs_user`；237–247、247–343 受内容/重复身份冻结；218/237/253 簇继承 M180；13 条外部 ADD 保持 0 storage。
- 历史保护：247–665 虽在自动投影由 `KEEP_STRONG`降为`REMOVE_CANDIDATE`，但 M160 high-confidence KEEP 优先；GS-665 的 1 个 occurrence 保留且不进入可执行 REMOVE。247–489 的 `ADD_STRONG→DERIVED_ONLY` 前后均 0 storage，只是 candidate-only audit churn。
- 累计计划：309 张 preview，累计 299 REMOVE/353 occurrences、23 logical ADD + 4 normalization；draft/stage 309/309 回读一致，字段计数 knowledge 200 / related 241 / safe mastery 109。
- 投影：`MATHWIKI-MAINT-188-R1-FINAL-9e24d71d109f` 为 `PASS / issues=[]`；801 卡、3616 边、declared 1608、simulated 2181 strong / 587 medium、408 remove candidates。只有三条批准 REMOVE 的 storage 由 1→0；sentinel 32、zero-outgoing 108 无增减。
- 验收：M188 定向测试 `7/7 OK`，完整单元测试 `645/645 OK`；generic selection gate 与 projection audit gate 均 PASS；projection context SHA `33298a0331fb787eaf81fca94cbcc32bfaa55d08c5873396bc07d0672bb06af9`。
- 边界：本批仍是 SHADOW review；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-188_第三十七批GS-247质心凸性错连清理与GS-253二阶Taylor精分逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-188]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-189 GS-087/213/218 身份相邻卡片知识精分与 GS-411 整题串卡隔离逐题复核及累计 SHADOW 投影

- 选批：从 M188 remaining 8 张选择 GS-087、GS-213、GS-218；三题自身 q+s/正式卡/视觉页一致，全库唯一，独立复算通过。remaining 5 张。
- 知识裁决：GS-087 收紧为导数定义+导数定义型极限+无穷小阶数比较+极限条件反推导数；GS-213 为函数单调性+微分不等式；GS-218 为积分中值定理+中值定理+二阶导数。
- card-only 边界：13 条 stored incident 与 18 条 canonical ADD 全冻结，covered=0，新增 REMOVE/ADD/normalization 均为 0，related/storage 完全不变。087 受 093/108 重复和 GS-095 内容隔离影响；218/237/253 继承 M180/M188。
- 新内容隔离：主协调器实看 GS-411 题图/解析图后确认，原题是 `x=1,x=2,y=x,x轴` 围域上的 `sqrt(x^2+y^2)/x` 积分，正式卡却串成 GS-401/412 的对称积分与答案。GS-411 进入 non-plan content block，未进 plan/draft/stage。
- 累计计划：312 张 preview，累计 299 REMOVE/353 occurrences、23 logical ADD + 4 normalization；draft/stage 312/312 回读一致，字段计数 knowledge 203 / related 241 / safe mastery 109。
- 投影：`MATHWIKI-MAINT-189-R1-FINAL-1ab0dc067ea3` 为 `PASS / issues=[]`；801 卡、3614 边、declared 1608、simulated 2179 strong / 590 medium、409 remove candidates。storage 无变化；213–576 审计分类降级但原 1 occurrence 保留并禁止自动删除；sentinel 32、zero-outgoing 108 无增减。
- 验收：M189 定向测试 `7/7 OK`，完整单元测试 `652/652 OK`；generic selection gate 与 projection audit gate 均 PASS；projection context SHA `64dd562275af8af25a156f2843e600df1773f992ad48590604f741aebf81b6e6`。
- 边界：本批仍是 SHADOW review；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建或修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-189_第三十八批3卡身份相邻知识精分与GS-411整题串卡隔离逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-189]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-190 GS-410 无改写、LA-058 分块秩精分与 058–070 强边新增逐题复核及累计 SHADOW 投影

- 选批：从 M189 remaining 5 张选择 GS-410、LA-058；两卡 q+s/正式卡/视觉页一致、全库唯一、无 job。GS-410 独立复算 `1/48`，knowledge 已准确，登记 reviewed-no-change；LA-058 knowledge 收窄为矩阵秩。
- 关系裁决：双路一致新增 LA-058↔LA-070；410-667、058-088 双路 REJECT_ADD。400-410 即使 challenger 语义票偏强，也因 GS-400 q-only 继续冻结；406/413 与 410 的候选同样不越过证据/历史门禁。
- stored 边界：8 条 incident 均不执行 REMOVE；410-680 继承 M160 KEEP，410-411 受 GS-411 串卡阻断，410-412 与 058-094 受重复簇阻断，057-058 受历史冲突阻断。
- 累计计划：313 张 preview，累计 299 REMOVE/353 occurrences、24 logical ADD + 4 normalization；draft/stage 313/313 回读一致。GS-410 无改动未进入 preview，LA-058/070 双向补链。
- 投影：`MATHWIKI-MAINT-190-R1-FINAL-b3071520ec4a` 为 `PASS / issues=[]`；801 卡、3614 边、declared 1609、simulated 2179 strong / 590 medium、409 remove candidates。唯一 storage 变化为 058-070 从 0 到 2 occurrences；sentinel 32、zero-outgoing 108 无增减。
- 验收：M190 定向测试 `7/7 OK`，当前完整单元测试 `666/666 OK`；projection context SHA `176b35f1a2dd1ca40a53dd3e690bece010daba2233cd79490d9248e592407ba9`。
- 边界：本批仍是 SHADOW review；仅 isolated stage 运行 rebuild，未申请 writer lease、未创建/修改 queue job、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-190_第三十九批GS-410无改写与LA-058分块秩精分及058-070强边新增逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-190]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-191 最终严格候选池知识精分与关系冲突冻结逐题复核及累计 SHADOW 投影

- 选批：M190 remaining 根卡 GS-399/402/639 全部完成；GS-680 因旧版 knowledge 混入 method/trap 标签，作为 direct revalidation 一并精分。四卡 q+s/正式卡/视觉页一致，strict root pool 清零。
- knowledge：GS-399 为二重积分+积分保号；GS-402 只留二重积分对称性；GS-639 收紧为变上限/含参/第一类换元/导数定义/导函数连续性/复合与乘积求导；GS-680 只留极坐标法+对称性+平面图形面积。
- 关系裁决：638-639、639-641 双路 KEEP；399-402 双路 REJECT_ADD；402-680 owner KEEP/challenger REMOVE，转 needs_user_add 并保持 0 storage。639-685 继承 M162 REMOVE；其余 stored/ADD 因重复簇、q-only、GS-411 内容污染或 GS-115 REVIEWED job 冻结。
- 新重复簇：GS-053/337 的题图 SHA、source、题式与答案相同且均缺 solution asset，登记 NEEDS_USER_MERGE，阻断 053-639 ADD。
- 累计计划：317 张 preview，累计 299 REMOVE/353 occurrences、24 logical ADD + 4 normalization；本批新增关系动作 0。四张 selected preview 均只改 knowledge，related 原样保序。
- 投影：`MATHWIKI-MAINT-191-R1-FINAL-556e48677160` 为 `PASS / issues=[]`；801 卡、3609 边、declared 1609、simulated 2179 strong / 585 medium、409 remove candidates。storage/common verdict 无变化，中关联较 M190 减少 5；sentinel 32、zero-outgoing 108 无增减。
- 验收：M191 定向测试 `7/7 OK`，完整单元测试 `666/666 OK`；generic selection gate 与 projection audit gate 均 PASS；projection context SHA `b691e8a508661697f9d32354dde5238fdcd4f729e995e6ac99095578b3b5a5ac`。
- 边界：M191 是最终可提交的 SHADOW 累计计划，不等于正式写入。未申请 writer lease、未运行 canonical rebuild、未修改正式错题卡/`生成/**`/回滚/Tutor。完整报告见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-191_第四十批最终严格候选池知识精分与关系冲突冻结逐题复核及累计SHADOW投影_2026-07-12|MATHWIKI-MAINT-191]]。

## [2026-07-12] maintenance | MATHWIKI-MAINT-191-FORMAL 累计关系修复正式提交与共享 closeout

- 正式事务：按用户批准的 M191 累计计划，以 plan/draft/stage 三项 exact SHA 为授权锚，通过 `MATH-BATCH-M191-20260712-FINAL`、`MATH-TX-c299a3399c787461ea99047574ab35c5` 唯一写者事务发布 317/317 张目标卡；source journal=`COMMITTED`，maintenance receipt 已生成。
- closeout：最终 `DONE`；rebuild/coverage/bridge snapshot/bridge push 均完成，317/317 strict gates 通过，3546 项派生 diff 全部 journaled；回滚账本与 cards/visual inputs fingerprint 均保持不变，dirty journal=0。
- 硬边界：新审计确认 `REL-GS-402-GS-680` 仍为 0 storage；GS-053/GS-337 SHA 未变且未合并。
- 新基线：`MATH-REL-AUDIT-20260712-556e48677160` 为 `PASS`（801 cards / 3609 edges）；M192 coverage 已切换到该审计，SHA `43fef6fab1e3689239a53c28a827c93dfa73e83af5547ca068dd871f006bd3d3`。
- 测试边界：提交前完整测试 672/672 通过；提交后 current-state 定向测试 46/46 通过。M156–M191 历史 SHADOW replay 继续绑定提交前 immutable snapshot，正式树推进后拒绝重算是预期保护。
- 完整收口证据见 [[错题知识网络/wiki/maintenance/MATHWIKI-MAINT-191-FORMAL_累计关系修复正式提交收口报告_2026-07-12|MATHWIKI-MAINT-191-FORMAL]]。

## [2026-07-13] formal-intake-batch | MATH-BATCH-20260713-SYNC-102467

<!-- math-async-batch:MATH-BATCH-20260713-SYNC-102467 -->
- jobs: MATH-JOB-20260713T070533211219Z-b115a5edf6d6
- formal_ids: GS-690
- mode: unique-writer WAL batch; derived closeout resumes from VALIDATING on failure
- rollback: candidate-only; scheduler not invoked

## [2026-07-13] formal-intake-batch | MATH-BATCH-20260713-SYNC-102611

<!-- math-async-batch:MATH-BATCH-20260713-SYNC-102611 -->
- jobs: MATH-JOB-20260713T075955099005Z-f8bd35bbece8
- formal_ids: GS-691
- mode: unique-writer WAL batch; derived closeout resumes from VALIDATING on failure
- rollback: candidate-only; scheduler not invoked

## [2026-07-14] formal-intake-batch | MATH-BATCH-20260714-SYNC-102491

<!-- math-async-batch:MATH-BATCH-20260714-SYNC-102491 -->
- jobs: MATH-JOB-20260714T034754180609Z-4bc4f930822a
- formal_ids: GS-692
- mode: unique-writer WAL batch; derived closeout resumes from VALIDATING on failure
- rollback: candidate-only; scheduler not invoked

## [2026-07-14] formal-intake-batch | MATH-BATCH-20260714-SYNC-84892

<!-- math-async-batch:MATH-BATCH-20260714-SYNC-84892 -->
- jobs: MATH-JOB-20260714T052219017532Z-ef662dfedd34
- formal_ids: GS-693
- mode: unique-writer WAL batch; derived closeout resumes from VALIDATING on failure
- rollback: candidate-only; scheduler not invoked

## [2026-07-14] formal-intake-batch | MATH-BATCH-20260714-SYNC-84890

<!-- math-async-batch:MATH-BATCH-20260714-SYNC-84890 -->
- jobs: MATH-JOB-20260714T061713906618Z-a6520f96609e
- formal_ids: GS-694
- mode: unique-writer WAL batch; derived closeout resumes from VALIDATING on failure
- rollback: candidate-only; scheduler not invoked

## [2026-07-14] formal-intake-batch | MATH-BATCH-20260714-SYNC-84305

<!-- math-async-batch:MATH-BATCH-20260714-SYNC-84305 -->
- jobs: MATH-JOB-20260714T065839115262Z-00a5725d28c4
- formal_ids: GS-695
- mode: unique-writer WAL batch; derived closeout resumes from VALIDATING on failure
- rollback: candidate-only; scheduler not invoked

## [2026-07-15] formal-intake-batch | MATH-BATCH-20260715-SYNC-GS667-REDO2

<!-- math-async-batch:MATH-BATCH-20260715-SYNC-GS667-REDO2 -->
- jobs: MATH-JOB-20260715T013346742109Z-9d5588442e8c
- formal_ids: GS-667
- mode: unique-writer WAL batch; derived closeout resumes from VALIDATING on failure
- rollback: candidate-only; scheduler not invoked

## [2026-07-15] formal-intake-batch | MATH-BATCH-20260715-SYNC-GS668-REDO2

<!-- math-async-batch:MATH-BATCH-20260715-SYNC-GS668-REDO2 -->
- jobs: MATH-JOB-20260715T023132969536Z-22998314791f
- formal_ids: GS-668
- mode: unique-writer WAL batch; derived closeout resumes from VALIDATING on failure
- rollback: candidate-only; scheduler not invoked

## [2026-07-15] formal-intake-batch | MATH-BATCH-20260715-SYNC-GS595-CORRECT2

<!-- math-async-batch:MATH-BATCH-20260715-SYNC-GS595-CORRECT2 -->
- jobs: MATH-JOB-20260715T025612992807Z-c53043237f6b
- formal_ids: GS-595
- mode: unique-writer WAL batch; derived closeout resumes from VALIDATING on failure
- rollback: candidate-only; scheduler not invoked

## [2026-07-17] maintenance | 错题 Wiki 稳定编号增量同步

- input: 用户要求把本轮正式错题变更同步到 Wiki，使相关知识点、方法、错因和动作断点能够被及时检索。
- source_refs: GS-096、GS-627、GS-659、GS-669、GS-682、GS-696、GS-697、GS-698、GS-699、GS-700 的正式错题卡；`wrong_questions.json` 只读快照共 812 张。
- wiki_updated: 新增 `SRC-WQ-GS-696` 至 `SRC-WQ-GS-700`；刷新 10 张目标卡 source summary；更新全量 source index、高数覆盖表、总覆盖页、编译矩阵、四类簇索引和全局 Wiki index。
- cluster_policy: 保留全部既有 wiki_id，不运行会重新编号并删除旧簇页的归档生成器；本轮稳定追加 1 个知识簇、21 个方法簇、21 个错因簇，并刷新目标标签的成员、计数和动作断点迁移。
- tutor_source: 新增 GS-698 至 GS-700 的答案安全训练入口；修正 GS-669、GS-682 的当前来源关系，不改写历史 maintenance 记录。
- metrics: 正式卡 812；source summary 812；高等数学 694；线性代数 118；稳定编号知识簇 435、方法簇 1456、错因簇 481、动作断点簇 9；深度编译 809、待继续深度编译 3。
- visual_boundary: source summary 中显式挂载 13 条正式 visual_id；GS-696、GS-697 的详情页虽已存在，但因尚无 frontmatter/visual_id，仅在摘要正文标为待正式化，不伪造视觉编号。
- boundary: formal_cards_updated: 0；未修改正式错题卡、`wrong_questions.json`、wrongnet 关系或复习账本；Obsidian 未运行，CLI 不可用，本次采用文件系统增量同步与链接审计。

## [2026-07-17] lint | 错题 Wiki 增量同步终检

- scope: 812 张正式卡、812 份 source summary、全量来源索引、覆盖矩阵、高数与线代覆盖表；重点复核 GS-096、GS-627、GS-659、GS-669、GS-682、GS-696 至 GS-700。
- checks: 正式 ID 集合一致性、摘要 YAML 解析、wiki_refs 解析、四类簇成员一致性、动作断点计数、视觉注册、安全 Tutor 输入、控制字符和 `git diff --check`。
- result: 正式卡、来源摘要、来源索引和覆盖矩阵均为 812/812；高等数学 694/694、线性代数 118/118；知识簇 435、方法簇 1456、错因簇 481、动作断点簇 9；正式视觉映射 13。
- fixes: 补齐 GS-696 至 GS-700 来源摘要；移除 GS-096 的旧知识/方法簇残留和 GS-669 的旧 A-CONCEPT 残留；修复安全输入包中 GS-372 的 `\rho\to0` 转义；同步 GS-669、GS-682 关系及 GS-698 至 GS-700 安全训练入口。
- residual_limit: Obsidian 未运行，无法执行 vault CLI 的 backlinks/tag/graph 视图检查；已用全量文件系统链接、ID、YAML 与成员集合检查替代，未发现剩余阻断问题。
- boundary: formal_cards_updated: 0；wrongnet_rebuild: 0；未改变正式错题身份、答案或复习账本。

## [2026-07-18] nightly-closeout | MFI-CLOSE-65f25f3a2a2d524c7ab5114c

- input: 用户结束当天数学学习，要求把今日所有快速捕获或更新的错题逐题高质量复核、正式入库，并加强与既有错题库的连接。
- freeze: `MFI-FREEZE-c5ddbe4c303553e8800ad818`；冻结并收口 8 条 capture，目标为 GS-127、GS-183、GS-287、GS-666、GS-701、GS-702、GS-703、GS-704。
- formal_results: 更新 4 张复发卡 GS-127、GS-183、GS-287、GS-666；新建 4 张来源支持卡 GS-701 至 GS-704；均保留用户事实、首个断点、后续断点、掌握度证据边界、method_gap、rollback 和快速入库引用。
- rollback: 8 个目标均完成定点 upsert；4 张旧卡记录正式复发事件，4 张新卡建立首次做错事件；没有把用户未独立复做的理解状态写成已掌握。
- wrongnet: 严格只运行 1 次 rebuild；正式卡投影 816 张，8 个目标投影哈希均与当前正式卡一致。
- relationships: 仅生成 8 条 `proposal_only` 关系建议，分别指向 GS-540、GS-490、GS-573、GS-668、GS-129、GS-688、GS-323、GS-273；未在缺少用户确认时写入正式 `related`。
- wiki: source summary、source index、学科覆盖表和覆盖矩阵达到 816/816；高等数学 698、线性代数 118；知识簇 437、方法簇 1462、错因簇 498、动作断点簇 9；深度编译 813，保留 3 张历史待继续深度编译。
- visuals: 本批正式卡直接引用的视觉产物逐一通过哈希验证；GS-183、GS-287、GS-701 至 GS-704 共 16 个直接引用有效，GS-127 与 GS-666 的正式卡无直接视觉引用，按 `not_applicable` 收口。未趁本批局部修补历史全局视觉注册表；GS-696 至 GS-700 的既有登记漂移仍作为独立维护项保留。
- validation: closeout content hash `edba7cd72165dd638be57da74589fb23b1aa72b0cecd969914bb309e23ce5b0f`；关闭后 `pending_count=0`、`closed_count=8`、账本校验状态 `verified`；quick intake 单测 54 项和 scheduler targeted-upsert 单测 39 项均通过；Wiki YAML、目标 parity、全局 parity、成员关系、控制字符、Obsidian 搜索与 `git diff --check` 均通过。
- boundary: 未重编号历史 Wiki 稳定 ID；未把 SHADOW 关系提案提升为正式关系；未手改 wrongnet 生成物；未将历史视觉注册漂移误报为本批已修复。

## [2026-07-18] visual-registry-closeout | VISUAL-GS-696-700-REGISTRY-CLOSEOUT-20260718

- input: 用户要求修复 GS-696 至 GS-700 已知的低质量登记问题；本轮按既有正式卡、视觉详情页和仓库内图片证据定点处理。
- visual_identity: 为 GS-696、GS-697 补入 `VIS-GS-696`、`VIS-GS-697` 标准 frontmatter；五题全部进入 manifest、asset map、视觉详情索引、Obsidian 直达链接和 Wiki 页面索引。
- assets: 逐一核验 5 张题图与 5 张解析图，题号和内容匹配；GS-697、GS-699、GS-700 的解析图来源偏窄但可读，没有可靠高清源，因此不做无源放大或重采样。
- formal_quality: 移除 GS-696 正式卡中串入的网络协议文字；为 GS-696、GS-697 补 `evidence_origin: user_confirmed`；将 GS-699、GS-700 不同具体动作断点错误累计的 `repeat_count` 归一为 1；答案、用户错因和掌握度事实保持不变。
- evidence_boundary: GS-699 视觉详情将“已确认掌握”收紧为“经引导完成后段计算，尚无独立闭卷掌握证据”；SHADOW 关系与长期回滚账本均未改动。
- wrongnet: 正式卡稳定后严格运行 1 次 `wrongnet.py rebuild`；GS-696 至 GS-700 当前投影均为 `evidence_origin=user_confirmed`、`repeat_count=1`。
- wiki: 补齐 GS-696、GS-697 的 visual refs/ids 和本地桥入口；五份 source summary 更新当前 `formal_projection_sha256`；保留稳定 Wiki ID，不重编号簇页。
- registry_metrics: manifest 959 条、linked_wrongnet 730；asset map 1364 条，其中题图 936、解析图 428；历史陈旧 summary 已按 records 实际值重算。
- boundary: 未修改 `复习单元.json` 或 `复习记录.jsonl`；未手改 wrongnet 生成物；本条只关闭 2026-07-18 日终日志明确保留的 GS-696 至 GS-700 历史视觉登记漂移。

## [2026-07-18] ingest | 睡前 23 题独立诊断回流

- input: 同日 23 个可独立回答的诊断问题及用户逐题回答；只回流有新增证据的 9 张正式错题卡。
- targets: GS-127、GS-183、GS-287、GS-629、GS-666、GS-701、GS-702、GS-703、GS-704。
- source_summary: 刷新 9 份 SRC-WQ 摘要、正式投影哈希、method_gap 摘要和 Obsidian 视觉入口。
- clusters: 新增 9 个错因簇和 1 个方法簇，使点乘/叉乘角色、轮换等式层级、一般黎曼和左端点、读式对象等新证据进入可检索网络。
- evidence_boundary: 同一轮追问不增加 mistake_count 或 repeat_count；拆分子题答对只作能力证据，不直接标记掌握。
- relationships: 正式 related 未改；关系只保留 SHADOW 提案。

## [2026-07-19] ingest | 当日数学学习记录夜间正式编纂

- input: 冻结并逐题复核 2026-07-19 的 13 条快速捕获，对应 GS-109、GS-294、GS-470、GS-530、GS-646、GS-705 至 GS-709 共 10 个正式目标。
- source_summary: 刷新 5 份既有摘要，新建 5 份 `SRC-WQ` 摘要；同步当前 `formal_projection_sha256`、method_gap、视觉入口和证据边界。
- clusters: 保留全部既有稳定 wiki_id，增量追加 10 个知识簇、20 个方法簇和 19 个错因簇；知识簇、方法簇、错因簇、动作断点簇总数分别为 447、1483、526、9。
- deep_wiki: GS-705 至 GS-709 接入 `MATHWIKI-GS-METHOD-102`；GS-707 至 GS-709 进一步接入 `MATHWIKI-GS-TOPIC-014`，将变力做功、P/Q 映射、Green 公式方向和奇点挖洞条件编译成可迁移入口。
- metrics: 正式卡 821；source summary 821；高等数学 703；线性代数 118；全量来源索引、学科覆盖表和多维矩阵均为 821/821。
- evidence_boundary: GS-530 仅记录“本次复做正确”，因未提供独立过程，不将其提升为“已掌握”；GS-706 同样保留当日错因与后续计算已完成两类证据。
- relationships: 不改正式 `related`；候选连接只进入 `proposal_only` SHADOW 回执。

## [2026-07-19] lint | 当日数学夜间编纂终检

- scope: 821 张正式卡、821 份 source summary、全量来源索引、高数覆盖表、多维编译矩阵和 2465 个稳定簇页；目标为当日 10 个正式 ID。
- checks: 目标 YAML 必需字段、正式投影哈希、source/index/coverage/matrix 唯一身份、知识/方法/错因/action_gap 成员关系、深度页成员、视觉路径、Obsidian 搜索与反向链接、全 Wiki 控制字符。
- result: 10 个目标的 targeted parity 全部通过；全量 ID 集合为 821/821；目标无缺失簇、重复索引行或断链。
- fixes: 定点修复线性代数专题页中两个由 `alpha` 转义错误产生的响铃控制字符，数学内容未改变。
- boundary: 未重编号历史 Wiki ID；未把 SHADOW 提案写入正式关系；未修改原始来源。

## [2026-07-19] nightly-closeout | MFI-CLOSE-02c31dc0188ad97ae78237ca

- input: 用户要求将 2026-07-19 当天全部快速捕获和更新记录逐题复核并正式加入题库。
- freeze: `MFI-FREEZE-ad27a1c0c9894256f550e630`；13 条 capture 全部关闭，对应 GS-109、GS-294、GS-470、GS-530、GS-646、GS-705 至 GS-709 共 10 个正式目标。
- formal_results: 更新 5 张既有卡，新建 5 张来源支持卡；记录 4 次正式复发、5 次首次做错、2 次表示更新，并保留 2 条掌握候选的证据边界。
- evidence_boundary: GS-530 只确认本次做对，因没有独立解题过程，未升级为整卡已掌握；GS-706 的后续计算完成同样不替代其真实第一断点。
- rollback: 9 个做错或复发目标完成定点 upsert；GS-530 不生成虚假做错事件。
- wrongnet: 本批严格只运行 1 次 rebuild；正式投影 821 张，10 个目标均与当前正式卡一致。
- relationships: 仅保存覆盖 10 个目标的 `proposal_only` 关系审阅结果，未写入正式 `related`。
- wiki: source summary、来源索引、学科覆盖和矩阵均为 821/821；10 个目标 targeted parity 全部通过，稳定 Wiki ID 未重编号。
- validation: closeout content hash `59ea94e1e2e75a6759f5378e1390202d285ee48230f11609513bbb9326a4e321`；关闭后 `pending_count=0`、`closed_count=13`、账本状态 `verified`；quick intake 54 项和 scheduler targeted-upsert 39 项单测全部通过；`git diff --check` 通过。
- boundary: 未把未验证的理解写成掌握；未手改 wrongnet 生成物；正式卡引用的视觉产物逐项按哈希收口。

## [2026-07-20] ingest | 当日数学快速记录正式回流

- input: 冻结并逐题复核 2026-07-20 的 13 条快速捕获，对应 12 个正式目标：GS-628、GS-647、GS-681、PR-001、GS-710 至 GS-717。
- formal_cards: 更新 4 张复发卡，新建 8 张来源支持卡；GS-711 的两条捕获合并为一次错误事件和一次表述更新，没有重复累计错题次数。
- source_summary: 刷新 4 份既有摘要，新建 8 份 `SRC-WQ` 摘要；逐张同步当前 `formal_projection_sha256`、完整知识/方法/错因字段、动作断点和视觉入口。
- clusters: 保留既有稳定 Wiki ID；8 张新卡先进入 B2-TRIGGER、B3-METHOD、B4-CHAIN、B7-CALC 四个动作断点簇，不用一次性标签制造低复用度新簇。
- metrics: 正式卡 829；source summary 829；高等数学 711；线性代数 118；来源索引、学科覆盖表和多维矩阵均为 829/829。
- evidence_boundary: 只把用户明确说明的第一断点、后续断点和当前掌握证据写入正式卡；“看懂解析”或“后面会算”不自动等同于整题已掌握。
- relationships: 不改正式 `related`；本批相似题判断只保留为 `proposal_only` SHADOW 回执。

## [2026-07-20] nightly-closeout | 当日数学错题正式收口

- closeout: `MFI-CLOSE-b534db0a8da2cb6987bce6c3`；内容哈希 `2932f0acd47abde1799068d35b7b698bf1e5cd13907fdc2187e44709ebb27c03`。
- scope: 13 条 capture 全部关闭，对应 12 个正式目标；更新 4 张既有复发卡，新建 GS-710 至 GS-717 共 8 张正式卡。
- rollback: 12 个做错或复发目标均已绑定当日回滚记录；GS-711 的 `update_representation` 单独绑定最终正式卡，没有伪造第二条做错事件。
- generated: 本批只执行 1 次 successful wrongnet rebuild；九个生成物和 12 个目标投影均由 close writer 复核哈希。
- wiki_visuals: 12 份 source summary、稳定动作断点簇、覆盖索引与矩阵通过内置一致性检查；37 个正式视觉引用逐项通过哈希验证。
- relationships: 仅写入覆盖 12 个目标的 `proposal_only` 回执，未修改正式 `related`。
- validation: 关闭后 `pending_count=0`、`closed_count=13`、账本状态 `verified`；168 项项目单测与 `git diff --check` 全部通过。

## [2026-07-22] ingest | 2026-07-21 数学学习错题正式回流

- input: 冻结并逐题复核 2026-07-21 的 4 条快速捕获，对应 GS-303、GS-690、GS-718、GS-719。
- formal_cards: 更新 GS-303、GS-690 两张复发卡；新建 GS-718（77601 路径无关反求函数）与 GS-719（78806 路径无关偏导判据）。
- evidence_boundary: GS-303 保留“右半段独立算对、固定起点与自变量定义域混淆”的首断点；GS-690 区分体积计算首错与形心公式调取失败；GS-718、GS-719 只记录看解析或讲解后的理解，不写成独立掌握。
- rollback: 四个做错或复发目标均已完成定点 upsert；两张旧卡累计正式复发，两张新卡建立首次做错事件。
- wrongnet: 本批只执行 1 次 successful rebuild；正式投影共 831 张，四个目标投影与当前正式卡一致。
- wiki: 新建或刷新 4 份 source summary；来源索引、学科覆盖表和多维矩阵达到 831/831，高等数学 713、线性代数 118；目标接入稳定动作断点簇与第 18 讲多元积分方法总表。
- relationships: 不改正式 `related`；相似性判断只进入 `proposal_only` SHADOW 回执。

## [2026-07-22] lint | 2026-07-21 数学错题回流终检

- scope: 831 张正式卡、831 份 source summary、全量来源索引、高数覆盖表、多维编译矩阵；重点复核 GS-303、GS-690、GS-718、GS-719。
- checks: 目标正式投影哈希、source/index/coverage/matrix 唯一身份、动作断点簇成员、方法卡 H18-011 注册、视觉路径、Obsidian 反向链接、全 Wiki 控制字符与 `git diff --check`。
- result: 四个目标的 targeted parity 全部通过；正式卡、来源摘要、来源索引和覆盖矩阵均为 831/831；目标视觉文件存在且可读，未发现控制字符或重复索引行。
- boundary: 未重编号历史 Wiki ID；未把 SHADOW 提案写入正式关系；未手改 wrongnet 生成物；未把讲解后复述误记为独立复做掌握。

## [2026-07-22] nightly-closeout | 2026-07-21 数学错题正式收口

- closeout: `MFI-CLOSE-dba3000eefe30b6a9dc382f0`；内容哈希 `d7ea96caf6d6b5a4a27741f617338d6345f3423a2f62a3d4f33ba4de0186b11e`。
- freeze: `MFI-FREEZE-5906e87f646bc35efb68de7d`；4 条 capture 全部关闭，对应 GS-303、GS-690、GS-718、GS-719。
- formal_results: 更新 2 张复发卡，新建 2 张来源支持卡；四张卡均保存用户独立步骤、第一断点、后续断点和掌握证据边界。
- rollback: 4 个目标均绑定 2026-07-21 的定点回滚记录，记录哈希由 close writer 复核。
- generated: 本批只执行 1 次 successful wrongnet rebuild；九个生成物与四个目标投影均按哈希通过验证。
- wiki_visuals: 4 份 source summary、来源索引、学科覆盖、编译矩阵、动作断点簇和 10 个正式视觉引用通过内置一致性检查。
- relationships: 仅保存覆盖四个目标的 `proposal_only` SHADOW 回执，未修改正式 `related`。
- boundary: 未把看懂解析、讲解后复述或后续能算写成独立掌握；未扩大 2026-07-21 冻结清单。

## [2026-07-22] synthesis | 全量知识点—错因证据图谱

- scope: 扫描 831 张正式卡、831 个正式 ID 的视觉详情入口和 1410 张物理图片；ID 前缀为 GS 711、LA 119、PR 1。
- evidence_layers: 用户确认个人错因 46 张、待用户确认 362 张、历史来源未分类 422 张、解析推导 1 张；不同来源严格分层，不把解法或通用标签改写成用户个人错因。
- graph: 生成 470 个正式知识点节点、468 个可参与派生边的知识点节点、428 个可用错因节点、5527 条同卡知识点—错因分类边、1160 条知识点—动作断点边和 3745 条知识点—具体失败动作边。
- per_card: 新建逐题索引，逐张保存正式卡哈希、正文题目/解析覆盖、知识点、错因、首断点、证据来源、视觉详情、图片字节数与 SHA-256、manifest 状态和待核对项。
- visual: 1410 张图片全部完成可读性与 OCR 验收，处理错误为 0，识别字符 292964；OCR 只作资产验收，不当作数学语义复核或个人错因证明。
- blockers: 8 张已确认身份或内容错位的卡从汇总连线计数中排除；另登记 6 张解法/详情缺陷、11 张视觉身份缺口、29 张有效题面证据缺口、45 张视觉解答证据缺口和 21 张知识点待细化卡。
- duplicates: 题面图片 SHA-256 得到 42 个尚待裁决的跨正式 ID 重复簇，涉及 99 张卡；先走重复题、复发或身份合并判断，不直接写普通相似关系。
- historical_review: 对照 2026-07-12 的 M192 target-level coverage 与当前卡片哈希，308 张可按整文件 SHA 精确承接，字段级语义未漂移口径最多可暂时承接 357 张，当前仍有 474 张逐题语义复核缺口；第一批 30 张已冻结到逐题索引。
- artifacts: `MATHWIKI-SYNTHESIS-002_知识点错因证据图谱.md/json`、`MATHWIKI-SYNTHESIS-003_逐题内容与视觉证据索引.md`、`MATHWIKI-SYNTHESIS-002_语义复核边界回执.json`；输入状态哈希 `90722591496585383b8ee7e785072ae4d5b677b3387527744c07a01319b35d88`。
- validation: 派生构建后 `check` 可重现；新增证据分层、身份阻断、重复题图、摘要哈希与历史逐题复核覆盖分区测试；正式卡、`related` 与 `生成/` 均未改动。
- boundary: 图中的边是同题共现和复盘导航，不是因果证明；字段级承接只是保守差异启发式，不是新的逐题复核 receipt。只有绑定题面、解析或图片哈希的明确审核决定，才能把某个知识点—错因标签对升级为经过明确审核的语义决定。

## [2026-07-22] target-semantic-review | 全库逐题语义复核第1批20题

- scope: 逐题复核 GS-147、GS-192、GS-280、GS-281、GS-409、GS-425、GS-615、GS-616、GS-626、GS-670、LA-059、LA-067、GS-690 至 GS-697，共 20 张正式卡。
- content: 对每题分别核对题目所问、知识点、方法入口、最终答案、正文解析、题图与解析图；20 题均完成答案与推导一致性复核。
- evidence_boundary: 用户已确认个人错因 4 张、待用户确认 7 张、历史来源未分类 8 张、重复占位 1 张；不把解析推导或通用方法标签升级为用户个人错因。
- assets: 核对 57 个物理图片路径；按内容去重后为 49 张，其中题图 20 张、解析图 29 张；批次回执绑定正式卡、视觉详情和当前图片集合的 SHA-256，任一来源漂移即标记复核过期。
- quality_findings: 登记 GS-280 与 GS-162 的视觉绑定冲突、GS-409 到 GS-411 的身份阻断、GS-425 的历史命名空间异常、LA-067 到 LA-068 的身份阻断、GS-696 详情页残留口述片段、GS-697 到 GS-696 的弱关系降级，共 6 类质量发现。
- relations: 在 SHADOW 派生层保存 41 条关系决定；不改正式 `related`。GS-280、GS-409、LA-067 的不安全候选边保持阻断，GS-697 到 GS-696 不作为强关系。
- coverage: 全库当前 831 张；本批完成 20 张，剩余 811 张。历史逐题语义复核缺口从 474 张降为当前剩余 454 张。
- artifacts: `MATHWIKI-REVIEW-008_全库逐题语义复核第1批20题.md/json`、`MATHWIKI-SYNTHESIS-002_知识点错因证据图谱.md/json`、`MATHWIKI-SYNTHESIS-003_逐题内容与视觉证据索引.md`；输入状态哈希 `055bf03012f1415de0213bdc2dcb549f4b2bc525311cb588a7c9af99ec43aca9`。
- validation: 派生图谱 `check` 通过且来源状态哈希一致；全量 180 项单元测试通过；目标文件 `git diff --check` 通过；Obsidian CLI 可读取批次页、解析 26 个标题，并能从批次页、总索引和审计日志检索到 `MATHWIKI-REVIEW-008`。
- boundary: 未修改正式错题卡、正式 `related`、可视化详情正文、`生成/` 或回滚账本；当前批次只产生可审计、可失效的派生重组结果。

## [2026-07-22] target-semantic-closeout | 全库逐题语义复核第1批正式收口

- authorization: 用户明确授权按每批约 20 题正式收口证据充分且无歧义的关系与内容修正。
- relations: 移除 19 条弱、中或无关正式声明；保留并验证 17 条强方法边。逻辑边按任一端声明即成立，未为了 YAML 表面对称重复写边。
- content: 修复 GS-696 视觉详情中的跨学科口述污染；没有新增无证据个人错因。
- boundary: 4 个身份冲突或稳定 ID 问题继续保留 needs_user；未自动合并或删除稳定 ID。
- generated: 正式卡稳定后运行 1 次 wrongnet rebuild；九个生成物均保存 pre/post SHA 回执，生成目录未手改。
- validation: 逐题回执、双向关系查询、图谱 build/check、定点回归测试和哈希校验通过。
- artifacts: MATHWIKI-REVIEW-008、MATHWIKI-REVIEW-009。

## [2026-07-22] target-semantic-review | 全库逐题语义复核第2批20题

- scope: 逐题复核 GS-411、GS-421、LA-068、GS-208、LA-095、LA-003、GS-165、GS-237、GS-718、GS-005、GS-095、GS-646、GS-705 至 GS-712，共 20 张正式卡。
- assets: 核对 46 个物理图片路径，按内容去重为 42 个唯一 SHA；其中题图 20、解析图 20、辅助 reference 2。
- content: 每题分别核对题目所问、第一动作、知识点、答案、解析图与个人错因证据边界；LA-095 原解析第 2 问被确认存在数学错误。
- identity: GS-411、GS-421、GS-208 的 canonical 视觉与正式正文冲突；LA-003 是 GS-256 的重复占位；上述对象不进入普通聚合边。
- evidence_boundary: 不把解析图错误写成用户个人错因；GS-718 的“无法启动”是用户事实，具体偏导断点仍标为模型据题面细化。
- campaign: 两批共完成 40 张，verified 40，stale 0，remaining 791。
- artifacts: MATHWIKI-REVIEW-010 及更新后的知识点错因证据图谱。

## [2026-07-22] target-semantic-closeout | 全库逐题语义复核第2批正式收口

- relations: 移除 16 条弱、中或无关声明；验证 16 条强方法边。所有正式边都经过题面、解析或图片证据核对，并通过两个查询顺序验证。
- formal_cards: 写入 29 个正式源卡文件；修正 GS-165 提醒、GS-095 详情方程、GS-646 最新复发断点、GS-709 解析入口和 LA-095 的完整题面与秩分解答案。
- LA-095: 正式修正版使用原矩阵第 1、2 列组成 G，并以坐标矩阵 H 通过 GH=A 验算；原错误解析图作为来源证据保留，未归因于用户。
- visuals: 为 GS-705 至 GS-712、GS-718 补齐 9 条 manifest 记录和 18 条题图、解析图资产映射；manifest 972，asset map 1390，逐资产 SHA 全部匹配。
- boundary: 未自动改 GS-411、GS-421、GS-208、LA-003 的稳定身份；未改写 GS-095 疑似跨题污染的旧历史；未把 reference 图片伪装成 question 或 solution。
- generated: 本批只调用 1 次 wrongnet rebuild；第二批影响到的错题投影、强弱关系清单、相似题清单、图与索引均由该次重建更新，生成目录未手改。
- graph: 两批合计 103 个物理路径、91 个唯一 SHA；knowledge-error graph build/check 可重现，source_state_sha256 为 7eefbd3775d27b5fd719f1e9c87ed4a7d17960c716fb8d12d7ae3d841ebf207e。
- artifacts: MATHWIKI-REVIEW-010、MATHWIKI-REVIEW-011、视觉 registry 四件套与知识点错因证据图谱。

## [2026-07-22] target-semantic-review | 全库逐题语义复核第3批20题

- scope: 逐题复核 GS-627、GS-629、GS-645、GS-698 至 GS-704、GS-713 至 GS-717、GS-719、GS-249、LA-039、LA-099、LA-081，共 20 张正式卡。
- assets: 核对 55 个物理图片路径，按内容去重为 43 个唯一 SHA；其中唯一题图 20、解析图 23。
- content: 每题分别核对题目所问、知识点、第一动作、正式答案、正文解析、题图、解析图与个人错因证据边界；LA-039、LA-099 的旧视觉身份错位已据原图纠正，GS-249 的正式内容已对齐真实振荡积分题。
- quality_boundary: GS-704 的题源缺少原变量定义域，LA-081 缺少 Aα≠0 或等价条件；两题只保留条件式结论。GS-249 与 GS-044、GS-325、GS-343 共享题图，稳定 ID 不自动合并或删除。
- evidence_boundary: 本批没有从解析或正确答案反推新的个人错因；已有用户事实保持原证据层级。
- campaign: 三批累计完成 60 张，verified 60，stale 0，remaining 771；累计覆盖 158 个物理路径、134 个唯一 SHA。
- artifacts: MATHWIKI-REVIEW-012 及更新后的知识点错因证据图谱。

## [2026-07-22] target-semantic-closeout | 全库逐题语义复核第3批正式收口

- relations: 移除 26 条弱、中、无关或身份不安全的逻辑边，共清除 35 个物理声明；新增 GS-702—GS-172、GS-703—GS-585、GS-716—GS-458、LA-039—LA-041 四条强边，另复核保留 9 条既有强边。
- formal_cards: 写入 29 个正式源卡文件；所有关系均按任一端声明即成立的无向逻辑边检查，并在两个查询顺序下复验。
- visuals: 修正 14 份视觉详情；为 GS-713 至 GS-717、GS-719 补齐 6 条 manifest 记录和 12 条题图、解析图资产映射。manifest 978，asset map 1402，新增资产 SHA 全部匹配。
- boundary: 未新增无证据个人事实；未静默补造 GS-704、LA-081 的缺失题源条件；未裁决 GS-249 重复身份；未合并或删除稳定 ID。
- generated: 正式源稳定后只调用 1 次 wrongnet rebuild；9 份生成投影均记录 pre/post SHA，生成目录未手改。
- graph: 三批合计 158 个物理路径、134 个唯一 SHA；knowledge-error graph build/check 通过，source_state_sha256 为 fb47b13f36b1383f690aef9616c8886061f9ea984b1fa2466df31ff4a222ba3e。
- validation: 定向回归 18/18、全量测试 197/197 通过；JSON、831 份 YAML frontmatter、视觉登记、Obsidian read/outline/search、正式与生成哈希及 git diff check 全部通过。
- artifacts: MATHWIKI-REVIEW-012、MATHWIKI-REVIEW-013、视觉 registry 四件套与知识点错因证据图谱。

## [2026-07-26] ingest | 今日 12 道快速捕获正式收口

- scope: 按冻结清单 `MFI-FREEZE-e0132aae9853d5e494a22ee3` 逐题审核 GS-170、GS-523、GS-595、GS-627、GS-629、GS-645、GS-720 至 GS-725，共 12 个正式目标。
- formal_cards: 更新 6 张既有卡并新建 6 张正式卡；题目 ID 57805 与既有 GS-170 题面、表达式和答案完全一致，作为同题新来源合并，没有重复建卡。
- evidence_boundary: GS-523 与 GS-595 本日结果正确，但缺少完整步骤、闭卷和无提示证据，掌握候选均保守拒绝；正确记录已持久化，状态继续为待复做。
- rollback: GS-170、GS-627、GS-629、GS-645 及 GS-720 至 GS-725 的本日错误或复发均已写入回滚单元；GS-645 的同一方法指纹复发按既有规则累计，其余未强行合并为同一方法复发。
- relationships: 逐题检查后没有证据充分的新建、删除或改边候选，本批不改正式 `related`。
- generated: 正式源稳定后只运行 1 次 `wrongnet rebuild`；九份生成投影由该次重建更新，未手改生成目录，也未执行第二次成功重建。
- wiki: 12 个 source summary 均与当前 wrongnet projection 的 subject、knowledge、methods、error_causes 精确一致；六张新卡进入动作断点簇、总索引、科目覆盖表和多维矩阵。
- visuals: 逐卡核验正式卡声明的视觉引用，共 12 份详情页、13 张题图和 12 张解析图；缺少解析图的旧卡没有补造来源。

## [2026-07-26] lint | 今日 12 道夜间批次定向验收

- identity: 当前正式卡、source summary、全量来源索引和多维矩阵均为 837 个唯一 ID；高等数学覆盖表为 719 个唯一 ID，无 missing、orphan 或重复目标行。
- target_parity: 12 个目标的正式投影哈希均为 2026-07-26 当前版本；必要字段、簇引用、簇成员关系和三张索引唯一行检查全部通过。
- card_parse: 12 张正式卡均通过 `wrongnet related --ignore-declared` 解析；没有发现目标卡身份重复。
- obsidian: Obsidian CLI 能搜索到新 source summary，从覆盖表、矩阵、动作断点簇和总索引回链，并能完整读取目标摘要。
- integrity: 快速入库账本校验通过；`git diff --check` 通过；关闭前 pending 精确为冻结清单中的 12 条。
- boundary: 本次只做目标级 Wiki 编译和定向 lint，没有把全库历史语义页冒充为今日重编译，也没有为了补统计而再次运行 wrongnet rebuild。

## [2026-07-26] ingest | GS-523 与 GS-595 掌握状态正式纠正

- input: 冻结 `MFI-FREEZE-c0a73a92188a324f47105c8d` 中两条用户明确掌握确认，目标为 GS-523、GS-595。
- formal_cards: 两张正式卡均由“待复做”纠正为“已掌握”；保留原始错因、错误历史和此前保守裁决，并新增本次用户确认的 5/5 掌握依据。
- rollback: 两个定点回滚单元同步为 `已掌握: true`、`掌握状态: 已掌握`，清空下次复习日期，后续常规复盘与推荐跳过。
- source_summary: 刷新两份既有 `SRC-WQ` 摘要及其正式投影哈希；来源总索引和高等数学覆盖表状态同步为“已掌握”。
- relationships: 本批只有掌握状态纠正，没有新的解题结构或错因证据；不改正式 `related`，关系层记为 `proposal_only` 无候选。
- generated: 本批正式卡稳定后只运行 1 次 successful wrongnet rebuild；未手改生成目录，也不再执行第二次重建。

## [2026-07-26] lint | GS-523 与 GS-595 掌握收口定向验收

- scope: 两张正式卡、两个回滚单元、两份 source summary、来源总索引、高等数学覆盖表、多维矩阵及其现有稳定簇引用。
- checks: 正式投影哈希、source/index/coverage/matrix 唯一身份、知识/方法/错因字段一致性、稳定簇成员、视觉路径、Obsidian 读取与反向链接、推荐排除状态和快速入库账本。
- boundary: 只纠正已获用户明确确认的掌握状态；未删除历史错题卡，未新增关系，未把掌握结论反向写成新的首错证据。

## [2026-07-26] nightly-closeout | GS-523 与 GS-595 掌握状态正式收口

- closeout: `MFI-CLOSE-898a11694f9298e3cb40ef92`；内容哈希 `8ab4cb4a99b0e1aa819eade01414550b1dbf83d5776946361b06556c828cca0c`。
- freeze: `MFI-FREEZE-c0a73a92188a324f47105c8d`；两条掌握确认均以 `mastery_confirmed` 关闭。
- formal_and_rollback: GS-523、GS-595 的正式卡与回滚单元均已对齐“已掌握”，并退出常规错题复盘与推荐。
- generated_wiki_visuals: 本批一次 wrongnet rebuild、两份 source summary、索引唯一性、稳定簇成员和四个视觉引用均由 close writer 复核。
- boundary: 历史错因与此前裁决原样保留；没有删除正式卡，也没有将本次掌握确认误写为新的错误事件。

## [2026-07-27] ingest | 今日五道错题夜间增量编译

- scope: 按冻结清单 `MFI-FREEZE-3147af662b50cf708195b1dc` 正式编译 GS-179、GS-622、GS-646、GS-669、GS-726；用户明确排除的未完成题未进入冻结、正式卡、Wiki 或回滚系统。
- formal_cards: 更新四张既有卡并新建 GS-726；保留用户真实作答、提示依赖、首次断点、未确认项与掌握证据边界，没有把助手解释改写成用户独立能力。
- source_summary: 五份 `SRC-WQ` 摘要已对齐当前 wrongnet projection 的 subject、knowledge、methods、error_causes 和规范投影哈希，并登记五份视觉详情。
- clusters: 只增量刷新受本批五题影响的知识点、方法、错因和 action_gap 簇；新标签采用新稳定 ID，既有稳定 ID 未重命名或复用。
- coverage: 正式卡、source summary、来源总索引、科目覆盖表和多维矩阵均为 838 个唯一 ID；GS-726 已接入第18讲多元积分方法总表。
- study_success: GS-703 今日独立正确的 5 分已由正式评分事件持久化；由于它不是本次错误或复发捕获，未伪造成夜间错题事件，也未据单次成功擅自标记整卡已掌握。

## [2026-07-27] lint | 今日五道错题定向终验

- parity: 五个目标的正式投影哈希、日期、subject、knowledge、methods、error_causes、wrongnet_refs 与 source_refs 均精确一致；source/index/coverage/matrix 每题均只有一行。
- clusters: 五题引用的所有稳定簇均存在、反向列出目标且由对应子索引唯一登记；受影响簇的声明数量与实际卡行数一致。
- obsidian: Obsidian CLI 可完整读取 `SRC-WQ-GS-726`，并从视觉详情、覆盖表、矩阵及全部新簇检索到反向链接；全库搜索未发现被排除题的题目编号。
- identity: 当前正式卡、source summary、来源索引、科目覆盖和矩阵均为 838/838，无 missing、orphan 或目标重复行。
- boundary: 本次为目标级增量 ingest 与 lint；未运行破坏性全库簇生成器，未修改正式 `related`，关系判断保持 SHADOW 提案层。

## [2026-07-27] nightly-closeout | 今日五道错题正式收口

- closeout: `MFI-CLOSE-6971c8424272a79ab35c071d`；内容哈希 `9db4b959446c029fbfa54cd613c984a47752fe43d8fbe13ac4b006e5f31dd188`。
- freeze: `MFI-FREEZE-3147af662b50cf708195b1dc`；GS-179、GS-622、GS-646、GS-669 四条复发与 GS-726 一条新错题均已关闭。
- formal_and_rollback: 四张既有正式卡完成语义更新，GS-726 完成新建；五个目标均已绑定 2026-07-27 的回滚事件和当前正式源版本。
- generated_wiki_visuals: 一次 successful wrongnet rebuild、五份 source summary、索引与簇成员、十五个视觉引用均由 close writer 复核并写入可追溯回执。
- boundary: 用户明确排除的未完成题未进入冻结、捕获、正式卡、回滚、生成网络或 Wiki；GS-703 的独立正确 5 分仍作为既有评分事实单独保存，没有伪造成错误事件。

## [2026-07-28] ingest | 今日十道错题正式增量编译

- scope: 按冻结清单 `MFI-FREEZE-ec873a2351b2959ece654ca9` 正式编译 GS-628、GS-647、GS-668、GS-670、GS-699、GS-727 至 GS-731，共十个正式目标。
- formal_cards: 更新五张既有卡并新建五张正式卡；保留用户真实作答、首个断点、提示依赖和掌握证据边界，没有把讲解后理解写成无提示掌握。
- source_summary: 十份 `SRC-WQ` 摘要已对齐 2026-07-28 当前 wrongnet projection 的 subject、knowledge、methods、error_causes 与规范投影哈希，并登记当前视觉详情。
- clusters: 增量刷新受本批影响的知识、方法、错因和 action_gap 簇；新建 20 个知识簇、20 个方法簇和 15 个错因簇，稳定 ID 未重命名或复用。
- coverage: 正式卡、source summary、来源总索引、科目覆盖表和多维矩阵均为 843 个唯一 ID；十个目标在三张索引中均只有一行。
- relationships: 正式 `related` 未改；关系判断仅保留在 SHADOW 提案回执中。

## [2026-07-28] lint | 今日十道错题定向终验

- parity: 十个目标的正式投影哈希、日期、subject、knowledge、methods、error_causes、wrongnet_refs 与 source_refs 精确一致；定向 `wiki_parity.py` 返回 `ok=true`。
- identity: 当前正式卡、source summary、来源索引、科目覆盖和矩阵均为 843/843，无 missing、orphan 或目标重复行。
- clusters: 十题引用的稳定簇均存在并反向列出目标；action gap 已按当前首个断点迁移，未沿用过期分类。
- visuals: 十道正式卡声明的详情页与题图、解析图、参考图均按当前路径逐项核验，不补造缺失来源。
- boundary: 本次只做冻结目标的增量编译和定向 lint；关闭前发现 GS-647、GS-670 的正式修正晚于首轮生成快照，已执行一次受控最终重建，此后未再重建；未修改正式 `related`，也未把历史全库语义页冒充为今日重编译。

## [2026-07-28] nightly-closeout | 今日十道错题正式收口

- closeout: `MFI-CLOSE-c8ed3bdbae64d3aa73d2aa2f`；内容哈希 `7a88ad33a478752f5db98d3bc625cb3ba35ac19bdd4af2dd8d11c2b10a2d151d`。
- freeze: `MFI-FREEZE-ec873a2351b2959ece654ca9`；GS-628、GS-647、GS-668、GS-670、GS-699 五条复发与 GS-727 至 GS-731 五条新错题均已关闭。
- formal_and_rollback: 五张既有正式卡完成语义更新，五张新正式卡完成创建；十个目标均已绑定 2026-07-28 的回滚事件和当前正式源版本。
- generated_wiki_visuals: 最终 wrongnet 快照、十份 source summary、索引与稳定簇成员以及正式卡声明的视觉引用均由 close writer 逐项复核并写入可追溯回执。
- validation: 关闭后快速入库账本状态为 `verified`，`pending_count=0`、`closed_count=10`；关系层仅保存 SHADOW 提案，正式 `related` 未改。

## [2026-07-29] ingest | 今日三道错题正式增量编译

- scope: 按冻结清单 `MFI-FREEZE-e987191ef4ea0cb756ade6c8` 正式编译 GS-089、GS-690、LA-022，共三条复发记录。
- formal_cards: 三张既有正式卡均已更新；保留用户真实作答、独立正确步骤、首个断点、提示依赖与掌握证据边界，没有把查看答案或听懂讲解写成无提示掌握。
- source_summary: 三份 `SRC-WQ` 摘要已对齐 2026-07-29 当前 wrongnet projection 的 subject、knowledge、methods、error_causes 与规范投影哈希，并登记当前视觉证据。
- clusters: GS-089 从过期的“未先加减中间项”候选迁移到负增量对象边界与完整比例检查；LA-022 从“方法入口未沉淀”迁移到伴随矩阵、迹和行列式的对象边界；新增 3 个知识簇和 4 个方法簇，旧稳定 ID 未重命名或复用。
- relationships: 正式 `related` 未改；GS-690→GS-691、LA-022→LA-016、GS-089→GS-458 仅保留为 SHADOW 提案。

## [2026-07-29] lint | 今日三道错题定向终验

- parity: 三个目标的正式投影哈希、日期、subject、knowledge、methods、error_causes、wrongnet_refs 与 source_refs 精确一致；定向 `wiki_parity.py` 返回 `ok=true`。
- identity: 当前正式卡、source summary、来源索引、科目覆盖和矩阵均为 843/843，无 missing、orphan 或目标重复行。
- clusters: 三题引用的稳定簇均存在并反向列出目标；GS-089 与 LA-022 的动作断点已迁移为 A-CONCEPT，GS-690 保持 B3-METHOD。
- obsidian: Obsidian CLI 可读取三份目标摘要，并可从覆盖表、矩阵、错因簇、方法簇和动作断点簇检索到反向链接。
- boundary: 本次只做冻结目标的增量编译和定向 lint；未修改正式 `related`，未把历史全库语义页冒充为今日重编译。

## [2026-07-29] nightly-closeout | 今日三道错题正式收口

- closeout: `MFI-CLOSE-9b75ff153ec549ba7e37427a`；内容哈希 `284176528fcfe569db41c87a4ea97ebb169557fba248c0534f17e5dc76122bb1`。
- freeze: `MFI-FREEZE-e987191ef4ea0cb756ade6c8`；GS-089、GS-690、LA-022 三条复发记录均已关闭。
- formal_and_rollback: 三张既有正式卡完成语义更新；三个目标均已绑定 2026-07-29 的回滚事件和当前正式源版本。
- generated_wiki_visuals: 最终 wrongnet 快照、三份 source summary、索引与稳定簇成员以及正式卡声明的视觉引用均由 close writer 逐项复核并写入可追溯回执。
- validation: 关闭后快速入库账本状态为 `verified`，`pending_count=0`、`closed_count=3`；关系层仅保存 SHADOW 提案，正式 `related` 未改。

## [2026-07-30] ingest | 今日六道错题正式增量编译

- scope: 按冻结清单 `MFI-FREEZE-9c6242daab57da9871a3aa3c` 正式编译 GS-169、GS-655、GS-667、GS-698、LA-020 与 GS-732；前五题为复发更新，题目 165362 新建为 GS-732。
- formal_cards: 五张既有正式卡完成用户真实复做证据更新，新建一张正式卡；讲解后理解仍与闭卷掌握分开记录。
- source_summary: 六份 `SRC-WQ` 摘要已精确对齐 2026-07-30 的 subject、knowledge、methods、error_causes、source_refs 与正式投影哈希。
- clusters: 新建 3 个知识簇、6 个方法簇、12 个错因簇，并同步既有簇反向成员；GS-169 与 LA-020 已从缺证据旧错因簇迁出。
- coverage: 正式卡、source summary、来源总索引、科目覆盖表和多维矩阵均为 844 个唯一 ID；六个目标在三张索引中均只有一行。
- relationships: 正式 `related` 未新增；五个相似题建议保留为 SHADOW 提案，GS-655 因算子和首断点不同判为无充分候选。

## [2026-07-30] lint | 今日六道错题定向终验

- parity: 六个目标的正式投影哈希、日期、subject、knowledge、methods、error_causes、wrongnet_refs 与 source_refs 精确一致；定向及全局 `wiki_parity.py` 返回 `ok=true`。
- identity: 当前正式卡、source summary、来源索引、科目覆盖和矩阵均为 844/844，无 missing、orphan 或目标重复行。
- clusters: 六题引用的知识、方法、错因和 action gap 稳定簇均存在并反向列出目标；GS-732 未继承上一题不适用的第三分量判向与旧错因。
- obsidian: Obsidian CLI 可检索六份目标摘要；其反向链接数分别为 15、20、20、24、20、19。
- rollback: 六个回滚单元的定点 dry-run 均为 `noop`，当前正式源版本已同步；错因检查起始日均为 2026-07-31。
- boundary: 本轮只对冻结的六题做增量编译；wrongnet 使用一次最终批次快照，关系层保持 proposal-only，未将候选边写入正式关系。

## [2026-07-30] nightly-closeout | 今日六道错题正式收口

- closeout: `MFI-CLOSE-bfc13637adf0515b68fb6a8e`；内容哈希 `3c10af9047160d4cad2b2b934e6351347bd80eddcffa4e5fcee7609afa2a1805`。
- freeze: `MFI-FREEZE-9c6242daab57da9871a3aa3c`；GS-169、GS-655、GS-667、GS-698、LA-020 五条复发与 GS-732 一条新错题均已关闭。
- formal_and_rollback: 五张既有正式卡完成语义更新，GS-732 完成新建；六个目标均已绑定 2026-07-30 的回滚事件和当前正式源版本。
- generated_wiki_visuals: 最终 wrongnet 快照、六份 source summary、索引、稳定簇成员与视觉引用均由 close writer 逐项复核并写入可追溯回执。
- boundary: 关系层仅保存 SHADOW 提案，正式 `related` 未改；讲解后理解未被误写为闭卷掌握。

## [2026-07-31] ingest | 今日七道错题正式增量编译

- scope: 按冻结清单 `MFI-FREEZE-69204577f902f5fd422e9a88` 正式编译 GS-255、GS-694、GS-700、GS-705、LA-023、GS-733 与 GS-734；前五题为复发更新，来源题 57906、57944 分别新建为 GS-733、GS-734。
- formal_cards: 七张卡已写入用户本轮暴露的首个断点、具体错步、提示依赖和下一次第一动作；讲解后理解未写成闭卷掌握，七题状态均保持待复做。
- wrongnet_and_rollback: GS-705 的 same-method 指纹门拦下过期快照并保留原核心指纹后，完成一次最终有效 wrongnet 重建；七个回滚单元均已绑定当前正式源版本和 2026-07-31 事件。
- source_summary: 七份 `SRC-WQ` 摘要已精确对齐当前 wrongnet projection 的 subject、knowledge、methods、error_causes、source_refs 与规范投影哈希。
- clusters: 稳定增量新增 6 个知识簇、9 个方法簇、11 个错因簇；GS-255 从过期 B5-CHECK 迁移到 B4-CHAIN，LA-023 从旧占位错因簇迁入本轮用户确认错因。
- coverage: 正式卡、source summary、来源总索引、学科覆盖表和多维矩阵均为 846 个唯一 ID；高等数学覆盖 728，线性代数覆盖 118。
- relationships: 正式 `related` 未作本轮新增；相似题判断仅保留为 SHADOW 提案回执。

## [2026-07-31] lint | 今日七道错题定向终验

- parity: 七个目标的正式投影哈希、日期、subject、knowledge、methods、error_causes、wrongnet_refs 与 source_refs 精确一致；定向及全局 `wiki_parity.py` 均返回 `ok=true`。
- identity: 正式卡、source summary、来源索引、学科覆盖和矩阵均为 846/846，无 missing、orphan 或目标重复行；Wiki 稳定 ID 扫描未发现重复或控制字符。
- clusters: 七题引用的知识、方法、错因与 action gap 稳定簇均存在并反向列出目标；B4-CHAIN 为 241，B5-CHECK 为 75。
- obsidian: Obsidian CLI 可读取 `SRC-WQ-GS-734`，可检索 `SRC-WQ-GS-733`、`MATHWIKI-METHOD-CLUSTER-1530`，并能从覆盖表、矩阵和全部相关簇返回 GS-733 的反向链接。
- rollback: 七个回滚单元的定点 dry-run 均为 `noop`，当前正式源版本已同步；五条复发事件和两条新错题事件均已存在于对应单元。
- boundary: 本轮只更新冻结七题及其派生索引；未运行破坏性全库簇生成器，未把 SHADOW 候选写入正式关系，也未改动冻结外正式卡。

## [2026-07-31] nightly-closeout | 今日七道错题正式收口

- closeout: `MFI-CLOSE-80c17064a0f892a85a043bbc`；内容哈希 `2139e6d8498c4e0ab884a3d5f212bae2e4c236beb6c9337810a6133ffe622708`。
- freeze: `MFI-FREEZE-69204577f902f5fd422e9a88`；GS-255、GS-694、GS-700、GS-705、LA-023 五条复发与 GS-733、GS-734 两条新错题均已关闭。
- formal_and_rollback: 五张既有正式卡完成语义更新，两张新正式卡完成创建；七个目标均已绑定 2026-07-31 的回滚事件和当前正式源版本。
- generated_wiki_visuals: 最终 wrongnet 快照、七份 source summary、索引、稳定簇成员和正式卡声明的视觉引用均由 close writer 逐项复核并写入可追溯回执。
- validation: 关闭后快速入库账本 `pending_count=0`、`closed_count=7`，`verify` 返回 `status=verified`；收口回执模型字段按协议记录为 `unknown`。
- boundary: 关系层只保存 SHADOW 提案，正式 `related` 未作本轮新增；讲解后理解未被误写成闭卷掌握。

## [2026-08-01] ingest | 今日十一条捕获合并为八道正式错题

- scope: 按冻结清单 `MFI-FREEZE-6ee9c9f0ea608cf479face69` 将 11 条快速捕获按真实题目合并为 GS-105、GS-406、GS-625、GS-706、LA-049、GS-735、GS-736、GS-737 八个正式目标。
- formal_cards: 更新五张既有复发卡并新建 GS-735 至 GS-737；同题补充问题合并进同一张正式卡，没有把一次对话拆成重复题，也没有把讲解后理解写成闭卷掌握。
- wrongnet_and_rollback: GS-706 的同方法复发声明被精确指纹门拦下后改为 `same_method_gap=false`；最终 wrongnet 快照稳定，八个回滚单元均与当前正式源版本对齐且幂等检查为 `noop`。
- source_summary: 八份 `SRC-WQ` 摘要已精确对齐 2026-08-01 当前投影的 subject、knowledge、methods、error_causes、source_refs 与规范投影哈希。
- clusters: 增量新增 12 个知识簇、17 个方法簇、30 个错因簇和 1 个 A-KG 动作断点簇；既有簇按八张卡的最终标签同步移入或移出，稳定 ID 未重命名或复用。
- coverage: 正式卡、source summary、来源总索引、学科覆盖表和多维矩阵均为 849 个唯一 ID；高等数学覆盖 731，线性代数覆盖 118。
- visuals_and_relationships: GS-735 至 GS-737 的七个本地视觉资产逐项哈希核验；关系层仅记录 SHADOW 提案，未写入正式 `related`。

## [2026-08-01] lint | 今日八道错题定向与全库身份终验

- parity: 八个目标的正式投影哈希、日期、subject、knowledge、methods、error_causes、wrongnet_refs 与 source_refs 精确一致；定向并带全库身份检查的 `wiki_parity.py` 返回 `ok=true`。
- identity: 正式卡、source summary、来源索引、学科覆盖和矩阵均为 849/849，无 missing、orphan 或目标重复行；3790 份 Wiki Markdown 的 frontmatter `wiki_id` 扫描未发现重复。
- clusters: 八题引用的全部知识、方法、错因与 action gap 稳定簇均存在并反向列出目标；60 个新增簇与受影响旧簇的声明数量均按实际卡行重算。
- obsidian: Obsidian CLI 可读取 `SRC-WQ-GS-735`，检索到其正式视觉页、来源索引与相关稳定簇，并能从覆盖表、矩阵、错因簇、方法簇和动作断点簇返回反向链接。
- integrity: 目标 Markdown 通过 `git diff --check`，八份来源摘要的 Obsidian 链接均可解析，声明的视觉资产路径全部存在；七张新复制图片的 SHA-256 与来源核验值一致。
- boundary: 本轮只更新冻结八题及其派生层；未把 SHADOW 候选写入正式关系，未把历史深度页冒充为今日重编译，也未修改冻结外正式卡。

## [2026-08-01] nightly-closeout | 今日数学正式收口

- freeze: `MFI-FREEZE-6ee9c9f0ea608cf479face69` 的 11 条捕获已全部消费，按真实题目合并为 8 个正式目标。
- closeout: 已记录 `MFI-CLOSE-a69a47df05b797c1f39dfd6d`，内容哈希为 `f4a43a520006a4af86d82e0d455979c93796152210a0f9f5173f08ee2dc43694`；一次性收口回执已消费。
- result: 更新 GS-105、GS-406、GS-625、GS-706、LA-049 五张既有卡，新建 GS-735、GS-736、GS-737 三张卡；回滚层、wrongnet、Wiki、视觉资产与 SHADOW 关系回执均随关闭事件绑定。
- verification: 关闭后 `pending_count=0`、`closed_count=11`、active freeze 为空；账本校验返回 `status=verified`，账本哈希为 `259f2959003c12e07702988c747433dc6efbb7410de49aee694bd2661a61b0e9`。
- boundary: 模型身份按收口协议记为 `unknown`；未把讲解后理解升级为独立掌握，未把 SHADOW 候选写入正式 `related`。

## [2026-08-03] ingest | 2026-08-02 五道数学复发题正式增量编译

- scope: 按冻结清单 `MFI-FREEZE-c96dc899608f9b43766e5c6f` 更新 GS-447、GS-456、GS-619、GS-707、LA-074 五张既有正式卡；五条学习事实日期均为 2026-08-02。
- formal_cards: 五张卡分别保存本轮首个断点、独立正确局部、后续不同断点、提示依赖与掌握证据边界；没有把讲解后结果写成独立掌握。
- wrongnet_and_rollback: 本批完成一次 successful wrongnet rebuild；五个目标均新增唯一的 2026-08-02 正式复发事件并进入高优先级延迟复做。
- source_summary: 五份 `SRC-WQ` 摘要已对齐 2026-08-03 当前投影的 subject、knowledge、methods、error_causes、source_refs 与规范投影哈希。
- relationships: 正式 `related` 未改；关系判断仅保留为 SHADOW 提案。

## [2026-08-03] lint | 2026-08-02 五道数学复发题定向终验

- parity: 五个目标的正式投影哈希、日期、subject、knowledge、methods、error_causes、wrongnet_refs 与 source_refs 精确一致；定向 `wiki_parity.py` 返回 `ok=true`。
- identity: 正式卡、source summary、来源总索引、学科覆盖和矩阵均为 849 个唯一 ID，无 missing、orphan 或目标重复行。
- clusters: 五份摘要只引用仍有真实目标成员证据的稳定簇；新出现但尚无安全增量编译器的标签未被擅自扩展成全库簇页。
- boundary: 本轮只更新冻结目标及必要来源摘要，未运行已退役的全库 Wiki 生成器，也未修改正式关系。

## [2026-08-03] nightly-closeout | 2026-08-02 五道数学复发题正式收口

- closeout: `MFI-CLOSE-52631ac3dcbdcaad00c47948`；内容哈希 `2b1ba9f9489e936fbc41ce2e8c7795c8cd41a6cf5b90eab279b7355b98d0264c`，一次性收口凭证已消费。
- freeze: `MFI-FREEZE-c96dc899608f9b43766e5c6f` 中 GS-447、GS-456、GS-619、GS-707、LA-074 五条 2026-08-02 正式复发捕获均已关闭；派生产物日期为 2026-08-03。
- formal_and_rollback: 五张既有正式卡均完成第 2 次错题复发更新，并绑定唯一回滚事件、当前正式源版本与本轮掌握证据边界。
- generated_wiki_visuals: 一次最终 wrongnet rebuild 的九个生成物、五份 source summary、稳定簇成员和正式卡声明的全部视觉引用均由 close writer 逐项复核；GS-619、LA-074 的旧式文件名引用已规范为真实稳定 Wiki ID。
- validation: 关闭后 `pending_count=0`、`closed_count=5`、active freeze 为空，账本 `verify` 返回 `status=verified`；目标级 Wiki parity 返回 `ok=true`，全库身份层为 849/849 且无 missing、orphan。
- timing: 从 freeze 到 close commit 共 21 分 17 秒，按 5 个正式目标折算约 4 分 15 秒/题；close writer 提交耗时约 1.77 秒。
- boundary: 模型字段按协议记录为 `unknown`；关系层只保存 SHADOW 提案，正式 `related` 未改；讲解后理解未被升级为独立掌握。

## [2026-08-22] ingest | 2026-08-16 数学错题正式回流

- scope: GS-744, GS-745。
- source_summary: 2 份 source summary 已对齐当前 wrongnet projection。
- relationships: 正式 related 未改；关系层保持 SHADOW proposal-only。
- boundary: 原始 ZIP、DOCX 与题图只读；讲解后理解未写成独立掌握。

## [2026-08-22] ingest | 2026-08-17 数学错题正式回流

- scope: GS-746, GS-747, GS-748, GS-749, GS-750。
- source_summary: 5 份 source summary 已对齐当前 wrongnet projection。
- relationships: 正式 related 未改；关系层保持 SHADOW proposal-only。
- boundary: 原始 ZIP、DOCX 与题图只读；讲解后理解未写成独立掌握。

## [2026-08-22] ingest | 2026-08-21 数学错题正式回流

- scope: GS-761。
- source_summary: 1 份 source summary 已对齐当前 wrongnet projection。
- relationships: 正式 related 未改；关系层保持 SHADOW proposal-only。
- boundary: 原始 ZIP、DOCX 与题图只读；讲解后理解未写成独立掌握。

## [2026-08-22] ingest | GS-732 跨平台同题复发合并

- identity: ID138764 与 ID165362 题面完全一致，合并到既有 GS-732，未创建重复正式卡。
- formal: 追加 2026-08-21 第2次错误、掌握度 3/5、新 source bundle 与定点回滚事件。
- boundary: 两次均涉及位置与定向，但精确第一动作不同，same_method_gap=false；正式 related 未改。

## [2026-08-29] ingest | 四道快速入库题正式增量编译

- scope: 按冻结清单 `MFI-FREEZE-cbd1a138d1deeedb47209223` 更新 GS-505、GS-695、GS-698、GS-748 四张既有正式卡，四条复发学习事实日期均为 2026-08-29。
- formal_cards: 四张卡分别保存本轮首个断点、后续不同断点、提示依赖和掌握证据边界；讲解后理解与口头确认均未升级为独立闭卷掌握。
- wrongnet_and_rollback: 四个正式目标均绑定唯一的 2026-08-29 复发事件并进入 2026-08-30 起始的延迟复做；GS-698 与 GS-748 的方法指纹发生扩展，按精确门禁记录为 `same_method_gap=false`，没有虚增同方法复发次数。
- source_summary: 四份 `SRC-WQ` 摘要已对齐 2026-08-29 当前投影的 subject、knowledge、methods、error_causes、source_refs 与规范投影哈希；来源总索引、高数学科覆盖表、多维矩阵和总 Wiki 索引的目标行已同步。
- clusters: 四份摘要只引用已经存在且反向列出目标的稳定簇；本轮新增的细分错因和方法标签未在缺少安全全库增量编译器的情况下擅自扩展成新簇页。
- visuals_and_relationships: 四张卡的稳定视觉引用与历史归档来源均通过闭环校验；关系层保持 SHADOW proposal-only，正式 `related` 未作本轮新增。

## [2026-08-29] lint | 四道正式复发题定向与全库身份终验

- parity: GS-505、GS-695、GS-698、GS-748 的正式投影哈希、产物日期、subject、knowledge、methods、error_causes、wrongnet_refs 与 source_refs 精确一致；定向并带全库身份检查的 `wiki_parity.py` 返回 `ok=true`。
- identity: 正式卡、source summary、来源总索引、学科覆盖和矩阵均为 878/878，无 missing、orphan 或目标重复行。
- clusters: 四份摘要引用的稳定知识、方法、错因和 action gap 簇均存在并反向列出对应目标；没有把本轮新增自由标签冒充已完成全库簇编译。
- obsidian: Obsidian CLI 可读取四份目标 source summary；四张正式卡的稳定详情页和视觉资产均通过逐项哈希检查。
- integrity: 目标正式卡、视觉详情、Wiki 与回滚产物通过 `git diff --check`；关系层仍为 SHADOW proposal-only。

## [2026-08-29] nightly-closeout | 四道快速入库题正式收口与原始包归档

- closeout: 已记录 `MFI-CLOSE-d724be53ef1eb36259465d76`，内容哈希为 `8e64e9aec3947d104de34e85d196e027b6aa24291224be7d32621a59097ec2a0`；冻结中的四条 capture 均已关闭。
- formal_and_rollback: GS-505、GS-695、GS-698、GS-748 均作为既有卡完成正式复发更新，并绑定各自唯一回滚事件；下一次错因检查起始日为 2026-08-30。
- archives: 四个 `math-conversation-package-v1` 原始包均归档到 `T9-Data/03_数学/资料库/原始会话资料/2026-08-29/`，归档回执分别为 `MATH-ARCHIVE-b61e032ef9ce9722e76bb81c`、`MATH-ARCHIVE-6c99f0c7975d277e9a02e291`、`MATH-ARCHIVE-22311de259290985b8f13a7d`、`MATH-ARCHIVE-c56c374282788cf9fc2a74fc`；定位器、回执和恢复指针重验后，本地 `attachments/` 已清理。
- validation: 当日 `pending_count=0`、`closed_count=4`、active freeze 为空，账本 `verify` 为 `status=verified`；目标正式 lint、Wiki 878/878 全库身份 parity、四个 T9 定位器重开与 `git diff --check` 均通过。
- global_boundary: 基线累计门禁确认本批四条 capture 为 `completed`；另有 144 条更早的历史归档身份不匹配残留，均为 `writer_apply_policy=forbidden` 的 archive-repair 债务，不属于本批正式卡未完成。
- boundary: 模型字段按协议记录为 `unknown`；正式 `related` 未改，讲解后理解未升级为独立掌握。

## [2026-08-31] ingest | 六个冻结数学 Capture 正式卡与 Wiki 定向编译

- input: `MFI-FREEZE-6c507ea38d479419794822c6`；精确 Capture 为 `MFI-CAP-f56ed469bb04cbe29d8c0d9f`、`MFI-CAP-4c2208ac66368aef51ace828`、`MFI-CAP-258770e968d06d62e5b77405`、`MFI-CAP-5ddebce7fe44e72c2bbf1e9b`、`MFI-CAP-115a844b5081ab6ce4d9b75c`、`MFI-CAP-3c96905d085eeafcb10f99af`。
- source_refs: 六个 `math-conversation-package-v1` 原始包及其 manifest、conversation、source、receipt 与全部附件；每个包由 Sol 和只读 Luna 分别重开并核对哈希，Luna 均返回 `write_attempted=false`。
- wiki_created: 新建 `SRC-WQ-GS-767`，补入 Wiki 总索引、正式来源总索引、高数学科覆盖表、多维矩阵与 B4-CHAIN、变上限积分、相关变化率、变力做功等稳定簇入口。
- wiki_updated: 刷新 `SRC-WQ-GS-564`、`SRC-WQ-GS-645`、`SRC-WQ-GS-694`、`SRC-WQ-GS-755`、`SRC-WQ-GS-762` 的当前正式投影哈希、完整字段、证据边界和定向簇引用。
- card_decision: GS-564、GS-694、GS-755、GS-762 为正式复发更新；新来源 ID 19358 建为 GS-767；GS-645 的评分 4 与“独立做对”自报因缺实际作答、答案和推理链而裁决为 `mastery_rejected`，不制造错误事件，也不标记已掌握。
- wrongnet_rebuild: lint 前曾出现一次无效预构建；完成 GS-767 标准章节修正与 GS-645 证据标签归位后，已对最终六卡状态重新执行正式构建。最终 closeout 只绑定修正后的产物哈希。
- rollback_action: GS-564、GS-694、GS-755、GS-762 的唯一复发事件和 GS-767 的首次错误单元均已定点写入；GS-645 不进入错误回滚。
- display_and_relationships: 六个包均形成稳定展示 closure；关系层保持 SHADOW proposal-only，正式 `related` 不写新边。
- missing_info: GS-645 缺题图、作答与答案过程；其掌握候选保持证据不足裁决。其余缺失附件按原 manifest 保留，不补造。

## [2026-08-31] nightly-closeout | 六个初始数学 Capture 正式收口与 T9 归档

- closeout: `MFI-CLOSE-f2241c9bc6e70d4d5825f897`，内容哈希 `7f82da494c71a606f178a9bb56256d735b47b651d3c5909d4aa3ead8c71a390f`；初始精确六条 Capture 均已关闭。
- formal_results: 更新 GS-564、GS-645、GS-694、GS-755、GS-762，新建 GS-767；GS-645 为 `mastery_rejected`，其余分别绑定四个复发回滚与一个首次错误回滚。
- teaching_contexts: 六个 `math-teaching-context-v1` 均已物化并以冷验证返回 `valid`；内容不含结论、完整题干或完整解析。
- archives: 六个完整会话包均归档到 `T9-Data/03_数学/资料库/原始会话资料/2026-08-31/`；回执为 `MATH-ARCHIVE-6042ff3c7ea57f67fd178f20`、`MATH-ARCHIVE-91c55077e83db70ab3dc9ec6`、`MATH-ARCHIVE-271747199f880351f1076166`、`MATH-ARCHIVE-6c866a4dc697954e82338d4a`、`MATH-ARCHIVE-5170dd1f83e6123416d7a1ef`、`MATH-ARCHIVE-04af3409e111ea92c3d0b79d`。
- archive_validation: 六个归档命令再次执行均返回 verified noop；Obsidian `raw_archive_locator`、本地 pointer、display closure、formal-reference scan 与 attachment cleanup 全部重验通过。
- selection_boundary: 初始 exact-subset baseline 的最终 gate 为 6 completed、0 residual。其后新到达的 `MFI-CAP-1ad0287292fa163f0ab5e393` 与 `MFI-CAP-0d3f33c7e9ebde19fac049fe` 留给下一轮，不计入本轮失败。
- report_only_debt: 当前累计 planner 另列 4 条历史 `failed/archive_repair` 旧账，writer apply 均为 forbidden；本轮未自动修复或重放。
- rebuild_note: lint 前有一次无效预构建；修正 GS-767 章节名和 GS-645 证据标签后执行最终构建，closeout 只绑定最终九个派生产物哈希。

## [2026-08-31] ingest | GS-645 用户掌握状态确认

- input: `MFI-FREEZE-40c6bd2570069f6612b61ac0`；精确 Capture 为 `MFI-CAP-ac55062154a5a7c1488a1e96`，来源包为 `MATHPKG-eb446e66495bcc1d120617a1`。
- card_decision: 用户明确确认整题已掌握，并要求以后不再进入错题查找和错题复盘；正式卡与回滚单元均更新为“已掌握”，掌握度为 5，下次复习日期为空。
- evidence_boundary: 用户说明具体推理写在纸上，但纸面过程未上传；本轮不补造步骤，既有三次错误历史继续保留。
- wrongnet_and_wiki: 完成一次最终 wrongnet rebuild；`SRC-WQ-GS-645`、来源总索引与高数学科覆盖表已对齐当前投影，目标 Wiki parity 为 879/879 且无身份缺口。
- closeout: `MFI-CLOSE-d0e77e78158c9264cb1c2351`，内容哈希 `186e7389dd42a3e5832ef4c6680678e7fea89e9bf5febe3feba85b37e50b272b`；Capture 结果为 `mastery_confirmed`。
- archive: 原始包已归档到 `T9-Data/03_数学/资料库/原始会话资料/2026-08-31/MATHPKG-eb446e66495bcc1d120617a1`，回执 `MATH-ARCHIVE-231f71008fc2f1f21f1bdebe`；重复归档验证返回 verified noop。
- boundary: 正式 `related` 未改；常规错题查找、复盘与推荐永久跳过 GS-645，仅在用户点名或专题抽查时查看。


## 2026-09-08 ingest advice.zip 精确日期批次

- 本批正式目标：GS-629；GS-771；GS-772；GS-773；LA-120。
- 保存原始ZIP、角色分明的原始对话及题图；逐题正式判断不直接采纳网页建议。
- source summary、知识点/方法/错因/动作簇、来源索引及覆盖矩阵均按最终正式投影更新。索引型覆盖不冒称新增深度编译。
- 正式关系保持SHADOW；不写新related边。


## 2026-09-08 ingest advice.zip 精确日期批次

- 本批正式目标：GS-774；GS-775；GS-776；GS-777；GS-778；GS-779；GS-780；GS-781；GS-782；GS-783；GS-784；GS-785；GS-786；GS-787；GS-788。
- 保存原始ZIP、角色分明的原始对话及题图；逐题正式判断不直接采纳网页建议。
- source summary、知识点/方法/错因/动作簇、来源索引及覆盖矩阵均按最终正式投影更新。索引型覆盖不冒称新增深度编译。
- 正式关系保持SHADOW；不写新related边。


## 2026-09-08 ingest advice.zip 精确日期批次

- 本批正式目标：GS-789；GS-790；GS-791；GS-792；GS-793；GS-794；GS-795；GS-796。
- 保存原始ZIP、角色分明的原始对话及题图；逐题正式判断不直接采纳网页建议。
- source summary、知识点/方法/错因/动作簇、来源索引及覆盖矩阵均按最终正式投影更新。索引型覆盖不冒称新增深度编译。
- 正式关系保持SHADOW；不写新related边。


## 2026-09-08 ingest | 晨间五题正式复盘

更新GS-350、GS-627、GS-628、GS-666、GS-668的本轮真实学习记录与来源摘要。前三道保留定义进步/漏读条件/完整独立正确的区别；GS-666图解错误归助手；GS-668仅自报成功不补造过程。建议包SHA256=44e0bf191d6ad3c79bffe4571f20a287a83bcdc9dfcf7b20fd1e3c71ebb04e9f。正式关系保持SHADOW提案，不重复计分。
