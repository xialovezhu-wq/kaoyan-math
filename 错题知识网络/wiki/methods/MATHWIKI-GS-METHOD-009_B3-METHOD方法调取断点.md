---
wiki_id: MATHWIKI-GS-METHOD-009
type: method
title: B3-METHOD 方法调取断点
subject: 高等数学
knowledge:
  - 极限与连续
  - 一元函数微分学应用
  - 定积分
methods:
  - 方法调取
  - 先判型
  - 第一动作
error_causes:
  - 方法论调取失败
  - 方法选择错误
  - 题型识别失败
triggers:
  - 知道知识点但第一动作没有启动
source_refs:
  - 错题知识网络/wiki/methods/action_gap_clusters/MATHWIKI-ACTION-GAP-001_B3-METHOD.md
  - 错题知识网络/方法论库/method_gap_schema.md
  - 错题知识网络/wiki/methods/MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度.md
wrongnet_refs:
  - GS-001
  - GS-002
  - GS-005
  - GS-015
  - GS-016
  - GS-017
  - GS-020
  - GS-436
  - GS-576
  - GS-641
method_card_ids:
  - 待匹配
  - H11-007
  - H11-004
wiki_refs:
  - MATHWIKI-ACTION-GAP-001
  - MATHWIKI-GS-METHOD-006
  - MATHWIKI-GS-ERROR-003
  - MATHWIKI-GS-METHOD-041
status: active
last_updated: 2026-07-02
---

# B3-METHOD 方法调取断点

## 定位

本页把 `B3-METHOD` 从 method_gap 标签沉淀成复盘动作：题目不是不会，而是应该调用的方法没有被启动，或只想到了方法名没有写出第一动作。

## 核心结论

- B3 的修复重点不是多刷题，而是把“方法名”压缩成“第一动作句”。
- 每张 B3 题复做时，先遮住解析，只写“看到什么 -> 先做什么”。
- 如果只能写出方法名，仍然没有完成 B3 修复。

## 方法链

1. 写题面信号：例如趋零量、变上限、参数、绝对值、通项、矩阵秩。
2. 写方法名：例如泰勒、洛必达、换元、分部、构造辅助函数、特征分解。
3. 写第一动作：例如先取对数、先画轴、先设整体函数、先拆主项、先列特征方程。
4. 复做时只检查第一动作是否能自动启动。

## 新增训练项：积分不等式的变上限辅助函数

- 题面信号：单调函数 + 定积分不等式 + 固定上限 \(b\)。
- 第一动作：先移项，并把固定上限 \(b\) 改成变量 \(t\)，构造 \(F(t)\)。
- 收口动作：证明 \(F(a)=0,\ F'(t)\ge0\)，再推出 \(F(b)\ge0\)。
- 细节检查：变上限积分求导时，积分变量是哑变量；化简 \(F'(t)\) 时保留负号；把 \((t-a)f(t)\) 改写成 \(\int_a^t f(t)\,dx\) 后再同区间比较。
- 关联错题：GS-641。

## 新增训练项：微分不等式的指数因子辅助函数

- 题面信号：出现整体函数 \(F\) 满足 \(F'(x)>F(x)\)，或等价地 \(F'-F>0\)。
- 第一动作：不要停在 \(F'>F\)，立刻写 \(G(x)=e^{-x}F(x)\)。
- 收口动作：由 \(G'=e^{-x}(F'-F)>0\) 得 \(G\) 单调递增；若 \(G(0)=0\)，则 \(x>0\) 时 \(G>0\)，进而 \(F>0\)，再由 \(F'>F>0\) 推出 \(F\) 单调递增。
- 细节检查：这里的 \(F\) 是整体设出的变上限积分函数，不要和原题里的小 \(f\) 混淆。
- 关联错题：GS-576。

## 新增训练项：极限题先提稳定主量

- 题面信号：非零因子、外部参数、底数趋非 \(1\) 常数、同名函数差值、有限非零极限。
- 第一动作：不要先把所有局部项展开，先写“稳定主量/公共尺度是什么”。
- 收口动作：主量提出后，再进入等价、洛必达、中值定理或零点因式分解。
- 关联错题：GS-005、GS-027、GS-436、GS-438、GS-440、GS-443。

## 关联

- 动作断点簇：[[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- 方法：[[MATHWIKI-GS-METHOD-006_先判型总流程]]
- 主量尺度：[[MATHWIKI-GS-METHOD-041_极限主量提出与公共尺度]]
- 错因：[[MATHWIKI-GS-ERROR-003_方法选择错误]]

## 来源

- `错题知识网络/wiki/methods/action_gap_clusters/MATHWIKI-ACTION-GAP-001_B3-METHOD.md`
- `错题知识网络/方法论库/method_gap_schema.md`
