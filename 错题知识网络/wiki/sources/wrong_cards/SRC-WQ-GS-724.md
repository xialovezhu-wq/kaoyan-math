---
wiki_id: SRC-WQ-GS-724
type: source_summary
title: "GS-724 170682 正弦幂积分递推"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-724_170682正弦幂积分递推.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-724_170682正弦幂积分递推.md"
visual_ids:
  - "VIS-GS-724"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-724/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-724/solution_01.png"
wrongnet_refs:
  - "GS-724"
knowledge:
  - "定积分"
  - "区间再现"
  - "分部积分"
  - "华里士公式"
  - "夹逼准则"
  - "数列极限"
error_causes:
  - "分部积分因子选取错误"
  - "区间反射触发失败"
  - "链式求导因子遗漏"
  - "夹逼入口遗漏"
methods:
  - "区间反射换元"
  - "对称配对"
  - "Wallis递推"
  - "分部积分降幂"
  - "相邻幂次比较"
  - "夹逼准则"
wiki_refs:
  - "MATHWIKI-ACTION-GAP-002"
status: indexed
formal_projection_sha256: 9c19f51042b6a742b1672a5c3cbfab376c3b84cde32180f109026f37172ecabf
last_updated: "2026-07-26"
---

# GS-724 170682 正弦幂积分递推

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-724_170682正弦幂积分递推.md`
- wrongnet ID：`GS-724`
- 可视化入口：[[错题知识网络/可视化错题详情/高等数学/GS-724_170682正弦幂积分递推|VIS-GS-724]]

## 本次正式结论

- 能识别华里士型结构，但未把对称落实为区间反射换元，也未按递推下标跨度选分部积分因子。
- 计算层还出现链式求导漏因子；第二问未利用正弦函数在区间内的范围比较相邻幂次。

## 动作断点

- [[MATHWIKI-ACTION-GAP-002

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
