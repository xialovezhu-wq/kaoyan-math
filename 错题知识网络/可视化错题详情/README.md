# 可视化错题详情层

本目录用于保存从 MarginNote 4 迁移来的数学题目图片、解析图片、解析文字摘要和 Obsidian 折叠解析页。

它不是正式错题卡系统。正式 wrongnet 源数据仍在 `错题知识网络/错题卡/*.md`，派生数据仍由 `wrongnet.py rebuild` 写入 `错题知识网络/生成/`。

## 入口

- 总索引：`index.md`
- 详情页模板：`templates/visual_wrong_question_template.md`
- 图片资产：`../assets/visual_wrong_questions/`
- MarginNote 原始导出：`../raw_sources/marginnote_exports/`，或登记外部绝对路径
- 导入规则：`../schema/marginnote_visual_import.md`

## 使用方式

1. 用户从 MarginNote 4 导出同一焦点分支的 `.oo3`，建议同时导出 `docx`。
2. 原始导出包放入 `错题知识网络/raw_sources/marginnote_exports/`，或在索引中登记外部绝对路径，不改写原件。
3. Codex 优先从 `.oo3/contents.xml` 读取节点层级和图片引用，再从 `.oo3` 包内 PNG 抽取题图、解析图副本。
4. Codex 用 `docx` 校验文本层和顺序，必要时补充解析文字。
5. Codex 用模板创建单题详情页：题目图片直接显示，解析默认折叠。
6. 详情页只连回 wrongnet、wiki、方法页和错因模式页，不替代正式错题卡。

## 状态值

- `planned`：只登记了待迁移题目。
- `imported`：题图和详情页已生成。
- `needs_ocr`：图片已导入，但解析文字待 OCR 或校对。
- `needs_split`：导出包中题目/解析边界不清，需要二次切图。
- `needs_id_confirmation`：未能稳定匹配到 `GS/LA/PR/MX` 编号。
- `reviewed`：用户做题后已经完成复述、连线建议和错题判断。

## 硬边界

- 不把完整题图和长解析复制到 `错题卡/*.md`。
- 不手改 `错题知识网络/生成/`。
- 不修改回滚 JSON。
- 不把视觉详情页当作 Tutor safe source 的完整题干来源。
- 信息不足时写 `待确认`、`未记录`、`待补充`。
