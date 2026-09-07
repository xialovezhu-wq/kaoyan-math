# GPT 项目资料上传规划_方法论优先

目标：让 GPT 先调用方法论，再调用三本书回查。不要把所有资料同等对待。

## 第一优先级：Instructions

粘贴：

- `00_上传说明与提示词/GPT项目指令_方法论优先版.md`

作用：规定 GPT 的行为方式，确保它先查方法卡，再讲题。

## 第二优先级：Knowledge 必传方法论资料

建议按顺序上传：

1. `01_放入GPT项目_Knowledge文件/考研数学方法论优先入口.md`
2. `01_放入GPT项目_Knowledge文件/考研数学方法论卡片_极简检索版.md`
3. `01_放入GPT项目_Knowledge文件/考研数学触发词_方法论映射表.md`
4. `01_放入GPT项目_Knowledge文件/考研数学错因分类_动作断点表.md`
5. `01_放入GPT项目_Knowledge文件/考研数学方法论_快速索引_GPT优先.md`
6. `01_放入GPT项目_Knowledge文件/考研数学方法论卡片库_v2.md`
7. `01_放入GPT项目_Knowledge文件/考研数学方法论卡片库_v2.json`

说明：如果 Knowledge 文件数量有限，优先保留 1-4；完整卡片库和 JSON 可二选一，但最好都放。

## 第三优先级：Knowledge 上传三本书逐页 Markdown

建议上传：

1. `03_三本书_GPT可读逐页Markdown_v2/2026张宇高数18讲_GPT可读逐页Markdown_v2.md`
2. `03_三本书_GPT可读逐页Markdown_v2/2026张宇线性代数9讲_GPT可读逐页Markdown_v2.md`
3. `03_三本书_GPT可读逐页Markdown_v2/2026考研数学临门一脚_GPT可读逐页Markdown_v2.md`

说明：逐页 Markdown 比 HTML 更适合 GPT Knowledge 检索。Page N 对应原 PDF 第 N 页，方便回查。

## 不建议优先上传

- 三份 HTML 精读版：更适合你人工浏览，不是 GPT Knowledge 的首选。
- 原始 PDF：如果 GPT 已经有逐页 Markdown，再上传原始 PDF 可能增加模糊检索和 OCR 噪声。
- zip 包：用于保存和迁移，不适合作为 Knowledge 直接上传。

## 人工浏览文件

- `04_方法论可视化HTML/methodology_app_optimized.html`
- `02_三本书_GPT精读HTML/*.html`

这些文件用于你自己快速查看，不是 GPT 的核心知识源。
