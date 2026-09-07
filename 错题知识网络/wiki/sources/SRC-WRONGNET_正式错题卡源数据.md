---
source_id: SRC-WRONGNET
type: source_summary
title: 正式错题卡源数据
status: active
last_updated: 2026-06-28
---

# 正式错题卡源数据

## 定位

`错题知识网络/错题卡/*.md` 是数学 wrongnet 的正式源数据。LLM Wiki 可以引用错题编号、轻量标签和错因模式，但不复制完整题干和长解析。

## 写入边界

- 只有正式错题入库、更新旧卡、标记已掌握或补字段时，才修改错题卡。
- 修改错题卡后必须运行 `python3 错题知识网络/scripts/wrongnet.py rebuild`。
- wiki 页面只保留 `GS/LA/PR/MX` 编号、知识点、错因、方法和触发条件。

## Wiki 连接

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[MATHWIKI-COVERAGE-001_错题卡全量覆盖索引]]
- [[MATHWIKI-GS-TOPIC-002_一元积分近期错题簇]]
- [[MATHWIKI-GS-TOPIC-001_条件边界与分类讨论]]
- [[MATHWIKI-GS-ERROR-001_边界条件遗漏]]

## 来源

- `错题知识网络/README.md`
- `错题知识网络/AI维护规则.md`
- `错题知识网络/错题卡/`
