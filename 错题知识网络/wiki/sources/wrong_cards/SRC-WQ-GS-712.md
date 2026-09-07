---
wiki_id: SRC-WQ-GS-712
type: source_summary
title: GS-712 58015 复合函数反求与分部积分
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-712_58015复合函数反求与分部积分.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-712_58015复合函数反求与分部积分.md
visual_ids:
- VIS-GS-712
wrongnet_refs:
- GS-712
knowledge:
- 复合函数
- 换元与反函数
- 不定积分
- 分部积分
- 指数对数求导
error_causes:
- 自变量角色混淆
- 复合函数反求入口缺失
- 分部积分触发不足
methods:
- 令内层函数为新变量
- 字母复位
- 分部积分
- 有理式拆分
wiki_refs:
- MATHWIKI-ACTION-GAP-002
status: indexed
formal_projection_sha256: 5abc07f74f4b8c239cd13471f5adb029786df995344d3917b457b5fb17b959d7
last_updated: '2026-07-20'
---

# GS-712 58015 复合函数反求与分部积分

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-712_58015复合函数反求与分部积分.md`
- wrongnet ID：`GS-712`
- 可视化入口：[[错题知识网络/可视化错题详情/高等数学/GS-712_58015复合函数反求与分部积分|VIS-GS-712]]

## 本次正式结论

- 第一阶段只反求函数身份：令 (u=\ln x)，由 (x=e^u) 得到 (f(u))，不要同时改写目标积分的微分。
- 第二阶段再把哑变量复位为 (x)，对所得指数因子与对数因子的乘积做分部积分。
- 关键微分入口是 (e^{-x}dx=d(-e^{-x}))。

## 动作断点

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
