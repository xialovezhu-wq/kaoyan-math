---
wiki_id: SRC-WQ-GS-719
type: source_summary
title: "GS-719 78806 路径无关偏导判据"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-719_78806路径无关偏导判据.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-719_78806路径无关偏导判据.md"
visual_ids:
  - "VIS-GS-719"
wrongnet_refs:
  - "GS-719"
knowledge:
  - "多元函数积分学"
  - "曲线积分"
  - "第二型曲线积分"
  - "路径无关"
  - "单连通区域"
error_causes:
  - "触发信息遗漏"
  - "方法调取失败"
methods:
  - "P与Q识别"
  - "路径无关偏导判据"
  - "参数恒等式"
wiki_refs:
  - "MATHWIKI-ACTION-GAP-003"
  - "MATHWIKI-GS-METHOD-102_第18讲多元积分方法卡总表"
status: indexed
formal_projection_sha256: ef5f29f740c557c76585a8e152eb52cb15383c22d8aee2fd1d29cd2da7f97fb7
last_updated: "2026-08-28"
---

# GS-719 78806 路径无关偏导判据

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-719_78806路径无关偏导判据.md`
- wrongnet ID：`GS-719`
- 可视化入口：[[错题知识网络/可视化错题详情/高等数学/GS-719_78806路径无关偏导判据|VIS-GS-719]]

## 当前正式结论

- 2026-08-27 再次完全无法启动；虽然能标出 P、Q，也能注意到分母为零会产生奇点，但没有把区域、奇点位置、路径无关和偏导判据分层处理，首断点仍是没有触发定义域检查与 (Q_x=P_y)。
- 看到“路径无关”和“单连通区域”时，应先按 dx、dy 的位置标 P、Q，检查连续性，再写偏导相等。
- 分母零点只在开区域边界时不构成内部奇点；若零点进入区域内部，则不能跨过奇点直接套普通格林公式或只凭偏导相等判路径无关。
- 提示后的参数比较和穿孔区域讨论不扩写为无提示独立作答证据。

## 动作断点

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]

## 深度编译

- [[MATHWIKI-GS-METHOD-102_第18讲多元积分方法卡总表]]

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
