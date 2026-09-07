---
wiki_id: SRC-WQ-GS-717
type: source_summary
title: GS-717 170635 绝对值分段与主项相消
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-717_170635绝对值分段与主项相消.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-717_170635绝对值分段与主项相消.md
visual_ids:
- VIS-GS-717
wrongnet_refs:
- GS-717
knowledge:
- 极限
- 含绝对值积分
- 分段积分
- 分部积分
- 等价无穷小
- 高阶展开
error_causes:
- 边界代入错误
- 三角项抄写错误
- 相消结构漏检
- 等价无穷小使用条件遗漏
methods:
- 绝对值分段
- 参数归一化换元
- 分部积分
- 因式分解保留高阶项
wiki_refs:
- MATHWIKI-ACTION-GAP-007
status: indexed
formal_projection_sha256: 2c878bab4b01bf3c966e169e759ec5c25bd1c4439f90b53327828353d6d7336e
last_updated: '2026-07-20'
---

# GS-717 170635 绝对值分段与主项相消

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-717_170635绝对值分段与主项相消.md`
- wrongnet ID：`GS-717`
- 可视化入口：[[错题知识网络/可视化错题详情/高等数学/GS-717_170635绝对值分段与主项相消|VIS-GS-717]]

## 本次正式结论

- 在 (t=x) 处分段的入口正确，第一个真实计算错误是把 (2x) 端点产生的 (-\cos2x) 写成了 (-\cos x)。
- 修正精确积分式后，(sin2x) 与 (2\sin x) 的一阶主项会抵消，不能再逐项使用一阶等价无穷小。
- 相消后应改用恒等式因式分解或保留足够阶数的展开。

## 动作断点

- [[MATHWIKI-ACTION-GAP-007_B7-CALC]]

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
