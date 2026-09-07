---
type: tutor_safe_intake_batch
batch_id: "MATH-BATCH-20260715-SYNC-GS668-REDO2"
date: "2026-07-15"
status: source_only
---

# MATH-BATCH-20260715-SYNC-GS668-REDO2 Tutor 安全输入

> 仅含知识点、错点、方法断点、触发词和第一动作。不含完整题干、题图、长解析、答案或掌握度反写。

## GS-668

- knowledge: 多元函数积分学、三重积分、三重积分对称性、球面坐标、定积分
- wrong_point: 复做时轮换对称性入口正确，但把单位球区域条件 $x^2+y^2+z^2\le1$ 误当成球体内处处有 $x^2+y^2+z^2=1$，将随位置变化的 $\rho^2$ 直接替换为常数 $1$，再用球体积计算，混淆了球体内部与球面边界，也混淆了积分区域限制与被积函数取值。
- method_trigger: 题目给出单位球 $x^2+y^2+z^2\le1$，被积函数为 $z^2$，可先用三变量轮换对称性，再用球面坐标计算仍随半径变化的积分。
- expected_first_action: 先写 $I=\frac13\iiint_\Omega(x^2+y^2+z^2)\,dV$，再标注“$x^2+y^2+z^2\le1$ 只限定区域，不能把被积函数替换成 $1$”，令 $x^2+y^2+z^2=\rho^2$ 后继续球面坐标积分。
- high_level_error: 空间几何图像断点、方法论调取失败、动作链断裂、运算路径不稳、基础计算错误、符号代入错误、概念混淆
