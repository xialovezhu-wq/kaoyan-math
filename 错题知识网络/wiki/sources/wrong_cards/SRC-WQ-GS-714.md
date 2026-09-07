---
wiki_id: SRC-WQ-GS-714
type: source_summary
title: GS-714 58077 参数积分换元极限
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-714_58077参数积分换元极限.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-714_58077参数积分换元极限.md
visual_ids:
- VIS-GS-714
wrongnet_refs:
- GS-714
knowledge:
- 极限
- 含参数积分
- 定积分换元
- 等价无穷小
- 洛必达法则
- 变上限积分求导
error_causes:
- 换元触发失败
- 参数与积分变量角色混淆
- 洛必达使用过早
- 等价无穷小公式误用
methods:
- 先换元消参数
- 分母等价无穷小
- 变上限积分求导
- 洛必达法则
wiki_refs:
- MATHWIKI-ACTION-GAP-003
status: indexed
formal_projection_sha256: 8b890fdd9c568719ec34b247ea1726670cf8c32943daf0b22e21e4598c2d420e
last_updated: '2026-07-20'
---

# GS-714 58077 参数积分换元极限

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-714_58077参数积分换元极限.md`
- wrongnet ID：`GS-714`
- 可视化入口：[[错题知识网络/可视化错题详情/高等数学/GS-714_58077参数积分换元极限|VIS-GS-714]]

## 本次正式结论

- 对 (u) 积分时，(x) 是参数；(xu) 与 (xdu) 成组出现时先令 (t=xu)，并同步修改上下限。
- 未消去积分内部参数前不应直接洛必达。
- 分母把 (2x^3) 视作整体小量，因此 (sqrt{1+2x^3}-1\sim x^3)。

## 动作断点

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
