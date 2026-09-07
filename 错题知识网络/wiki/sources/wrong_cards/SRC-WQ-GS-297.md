---
wiki_id: SRC-WQ-GS-297
type: source_summary
title: "GS-297 2020年第18题：函数方程反解与旋转体体积"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-297_2020年第18题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-297"
knowledge:
  - "定积分"
  - "函数方程"
  - "旋转体体积"
  - "水平切片"
error_causes:
  - "旧批量导入未记录个人错因；依据题图/解析确认的可复做断点是没有先写 \\(x\\mapsto1/x\\) 的同伴方程并在几何部分改用 \\(y\\) 切片。"
methods:
  - "互换 \\(x\\) 与 \\(\\frac1x\\) 消元"
  - "反解 \\(x=x(y)\\)"
  - "水平切片壳层法"
  - "三角换元"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-246_旧批量导入未记录个人错因-依据题图-解析确认的可复做断点是没有先写-x-"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-149_旋转体体积"
  - "MATHWIKI-KNOWLEDGE-193_函数方程"
  - "MATHWIKI-KNOWLEDGE-402_水平切片"
  - "MATHWIKI-METHOD-CLUSTER-028_三角换元"
  - "MATHWIKI-METHOD-CLUSTER-1160_水平切片壳层法"
  - "MATHWIKI-METHOD-CLUSTER-570_互换-x-与-frac1x-消元"
  - "MATHWIKI-METHOD-CLUSTER-795_反解-x=x-y"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-083_旋转体曲面变量选择与生成量链"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-297 2020年第18题：函数方程反解与旋转体体积

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-297_2020年第18题.md`
- wrongnet ID：`GS-297`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分应用 |
| 题型 | 函数方程反解与旋转体体积 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 函数方程
- 旋转体体积
- 水平切片

### 错因

- 旧批量导入未记录个人错因；依据题图/解析确认的可复做断点是没有先写 \(x\mapsto1/x\) 的同伴方程并在几何部分改用 \(y\) 切片。

### 方法

- 互换 \(x\) 与 \(\frac1x\) 消元
- 反解 \(x=x(y)\)
- 水平切片壳层法
- 三角换元

### 陷阱

- 含 \(f(1/x)\) 时，要再写一条 \(x\mapsto1/x\) 的同伴方程
- 旋转轴是 \(x\) 轴，但区域由两条水平线给出，按 \(y\) 切片更直接
- 反解 \(x=\frac{y}{\sqrt{1-y^2}}\) 后，体积微元是 \(2\pi yx(y)\,dy\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把原方程作 \(x\mapsto 1/x\)，写同伴方程消去 \(f(1/x)\)。 |
| missed_action | 旧卡未保存用户当时动作；当前可确认的复做断点是没有先写同伴方程，并在几何部分及时改用 \(y\) 切片。 |
| related_method_card_id | H10-002 |
| next_reminder | 看到 \(f(x)\) 与 \(f(1/x)\) 同现，先写同伴方程；看到水平边界旋转体，再判断按 \(y\) 切片。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-246_旧批量导入未记录个人错因-依据题图-解析确认的可复做断点是没有先写-x-]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-149_旋转体体积]]
- [[MATHWIKI-KNOWLEDGE-193_函数方程]]
- [[MATHWIKI-KNOWLEDGE-402_水平切片]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-1160_水平切片壳层法]]
- [[MATHWIKI-METHOD-CLUSTER-570_互换-x-与-frac1x-消元]]
- [[MATHWIKI-METHOD-CLUSTER-795_反解-x=x-y]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-083_旋转体曲面变量选择与生成量链]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-304

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
