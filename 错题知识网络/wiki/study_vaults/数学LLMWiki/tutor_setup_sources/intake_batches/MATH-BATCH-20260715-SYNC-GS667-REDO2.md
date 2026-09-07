---
type: tutor_safe_intake_batch
batch_id: "MATH-BATCH-20260715-SYNC-GS667-REDO2"
date: "2026-07-15"
status: source_only
---

# MATH-BATCH-20260715-SYNC-GS667-REDO2 Tutor 安全输入

> 仅含知识点、错点、方法断点、触发词和第一动作。不含完整题干、题图、长解析、答案或掌握度反写。

## GS-667

- knowledge: 多元函数积分学、三重积分、柱面坐标、二重积分极坐标法
- wrong_point: 看到圆柱投影圆盘后，没有区分“圆盘自身的固定半径 $1$”与“点到原点距离的极坐标变量 $r$”，也没有保留每根竖直小柱的贡献 $\int_0^{r^2/8}r\,dz$ 再对投影区域积分，而把受抛物面限制的变高度立体误按等高圆柱处理，用面积 $\pi$ 乘单点值；角域虽经讲解后能由 $\sin\theta\ge0$ 推出，但完整积分链尚未独立复做。
- method_trigger: 题目给出圆柱面 $x^2+(y-1)^2=1$、旋转抛物面 $8z=x^2+y^2$、平面 $z=0$ 围成区域，并要求计算 $\iiint_\Omega \sqrt{x^2+y^2}\,dV$。
- expected_first_action: 写出 $D:x^2+(y-1)^2\le1$ 和 $0\le z\le r^2/8$ 后，立即标注“圆盘半径 $1\ne$ 极坐标变量 $r$”，并写 $I=\iint_D[\int_0^{r^2/8}r\,dz]dA$，不能先用面积 $\pi$ 消掉投影积分。
- high_level_error: 图像理解错误、空间几何图像断点、方法论调取失败、动作链断裂、运算路径不稳、复习记忆不牢、概念混淆
