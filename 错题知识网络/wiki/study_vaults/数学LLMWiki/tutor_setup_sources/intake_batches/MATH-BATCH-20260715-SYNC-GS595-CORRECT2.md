---
type: tutor_safe_intake_batch
batch_id: "MATH-BATCH-20260715-SYNC-GS595-CORRECT2"
date: "2026-07-15"
status: source_only
---

# MATH-BATCH-20260715-SYNC-GS595-CORRECT2 Tutor 安全输入

> 仅含知识点、错点、方法断点、触发词和第一动作。不含完整题干、题图、长解析、答案或掌握度反写。

## GS-595

- knowledge: 定积分、定积分应用、曲线积分、极坐标、曲线弧长
- wrong_point: 看到 \(r=r(\theta)\) 形式的极坐标曲线求弧长时，没有先写 \(s=\int_\alpha^\beta\sqrt{r^2+\left(\frac{dr}{d\theta}\right)^2}\,d\theta\)，误把入口停在直角坐标弧长公式；本题应先求 \(r'\)，再代入极坐标弧长公式化简。
- method_trigger: 看到极坐标曲线 \(r=r(\theta)\) 且题目要求曲线弧长
- expected_first_action: 先写出 \(s=\int_0^{3\pi}\sqrt{r^2+\left(\frac{dr}{d\theta}\right)^2}\,d\theta\)
- high_level_error: 题型识别断点、方法论调取失败、公式遗忘、方法选择错误、过程跳步
