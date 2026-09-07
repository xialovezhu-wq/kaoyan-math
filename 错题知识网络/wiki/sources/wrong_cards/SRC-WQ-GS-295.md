---
wiki_id: SRC-WQ-GS-295
type: source_summary
title: "GS-295 2018年数2第20题：面积变化率"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-295_2018年数2第20题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-295"
knowledge:
  - "定积分应用"
  - "平面图形面积"
  - "变上限积分"
  - "相关变化率"
error_causes:
  - "旧批量导入未记录个人错因；依据题图/解析确认的可复做断点是没有先写真实面积函数 \\(S(x)\\)。"
methods:
  - "几何面积拆分"
  - "变上限积分面积函数"
  - "链式法则"
  - "相关变化率"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-247_旧批量导入未记录个人错因-依据题图-解析确认的可复做断点是没有先写真实面"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-035_定积分应用"
  - "MATHWIKI-KNOWLEDGE-060_平面图形面积"
  - "MATHWIKI-KNOWLEDGE-096_相关变化率"
  - "MATHWIKI-METHOD-CLUSTER-135_链式法则"
  - "MATHWIKI-METHOD-CLUSTER-435_相关变化率"
  - "MATHWIKI-METHOD-CLUSTER-645_几何面积拆分"
  - "MATHWIKI-METHOD-CLUSTER-803_变上限积分面积函数"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-081_面积绝对值分段与变化率建模链"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-295 2018年数2第20题：面积变化率

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-295_2018年数2第20题.md`
- wrongnet ID：`GS-295`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分应用 |
| 题型 | 曲边图形面积的相关变化率 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分应用
- 平面图形面积
- 变上限积分
- 相关变化率

### 错因

- 旧批量导入未记录个人错因；依据题图/解析确认的可复做断点是没有先写真实面积函数 \(S(x)\)。

### 方法

- 几何面积拆分
- 变上限积分面积函数
- 链式法则
- 相关变化率

### 陷阱

- 先表达真实封闭区域面积 \(S(x)\)，不要直接套一个现成公式
- 求的是 \(\frac{dS}{dt}\)，要先求 \(\frac{dS}{dx}\)，再乘 \(\frac{dx}{dt}\)
- 曲边部分面积是 \(\int_0^x\frac49t^2\,dt\)，积分变量不能也写成运动点的 \(x\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把区域面积写成梯形面积减曲边积分，得到 \(S(x)\)。 |
| missed_action | 旧卡未保存用户当时动作；当前可确认的复做断点是没有先写真实面积函数 \(S(x)\)。 |
| related_method_card_id | H07-001 |
| next_reminder | 看到动点面积变化率，先写真实面积函数 \(S(x)\)，再乘 \(\frac{dx}{dt}\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-247_旧批量导入未记录个人错因-依据题图-解析确认的可复做断点是没有先写真实面]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-035_定积分应用]]
- [[MATHWIKI-KNOWLEDGE-060_平面图形面积]]
- [[MATHWIKI-KNOWLEDGE-096_相关变化率]]
- [[MATHWIKI-METHOD-CLUSTER-135_链式法则]]
- [[MATHWIKI-METHOD-CLUSTER-435_相关变化率]]
- [[MATHWIKI-METHOD-CLUSTER-645_几何面积拆分]]
- [[MATHWIKI-METHOD-CLUSTER-803_变上限积分面积函数]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-081_面积绝对值分段与变化率建模链]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-260
- GS-261
- GS-262
- GS-285

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
