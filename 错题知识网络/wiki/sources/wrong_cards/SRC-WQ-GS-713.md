---
wiki_id: SRC-WQ-GS-713
type: source_summary
title: GS-713 58046 目标积分分部积分
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-713_58046目标积分分部积分.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-713_58046目标积分分部积分.md
visual_ids:
- VIS-GS-713
wrongnet_refs:
- GS-713
knowledge:
- 定积分
- 分部积分
- 反三角函数导数
- 换元积分
- 初值与边界项
error_causes:
- 题面括号误读
- 目标导向不足
- 绕远路
- 分部积分触发不足
methods:
- 直接对目标积分分部积分
- 利用端点消项
- 连续换元
- 反正切函数分部积分
wiki_refs:
- MATHWIKI-ACTION-GAP-001
status: indexed
formal_projection_sha256: d607a9f4b9ad43bfd429265941ebec4c7b754c1f6e6388671daad17fb5dc22e5
last_updated: '2026-07-20'
---

# GS-713 58046 目标积分分部积分

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-713_58046目标积分分部积分.md`
- wrongnet ID：`GS-713`
- 可视化入口：[[错题知识网络/可视化错题详情/高等数学/GS-713_58046目标积分分部积分|VIS-GS-713]]

## 本次正式结论

- 题面中的平方属于 (x-1)，即 (arctan((x-1)^2))，不是反正切函数整体的平方。
- 已知 (f') 且目标是 (int f) 时，先对目标积分本身分部积分；写 (dx=d(x-1)) 可同时利用两端点消去边界项。
- 化到反正切定积分后再做一次标准分部积分即可。

## 动作断点

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
