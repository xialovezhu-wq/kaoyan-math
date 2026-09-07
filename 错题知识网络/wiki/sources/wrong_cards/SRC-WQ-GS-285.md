---
wiki_id: SRC-WQ-GS-285
type: source_summary
title: "GS-285 1000题B组7.1"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-285_1000题A组11.1-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-285"
knowledge:
  - "一元函数微分学应用"
  - "相关变化率"
  - "复合函数求导"
  - "球体几何量公式"
error_causes:
  - "暂无明确个人错因（视觉证据仅支持复做入口）"
methods:
  - "相关变化率建模"
  - "链式法则"
  - "球体表面积公式"
  - "球体体积公式"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-030_复合函数求导"
  - "MATHWIKI-KNOWLEDGE-096_相关变化率"
  - "MATHWIKI-KNOWLEDGE-407_球体几何量公式"
  - "MATHWIKI-METHOD-CLUSTER-1199_球体体积公式"
  - "MATHWIKI-METHOD-CLUSTER-1200_球体表面积公式"
  - "MATHWIKI-METHOD-CLUSTER-1225_相关变化率建模"
  - "MATHWIKI-METHOD-CLUSTER-135_链式法则"
  - "MATHWIKI-GS-CONCEPT-001_条件边界"
  - "MATHWIKI-GS-ERROR-001_边界条件遗漏"
  - "MATHWIKI-GS-METHOD-001_先做条件边界清单"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-001_条件边界与分类讨论"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-GS-TRIGGER-001_参数端点定义域先停"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-285 1000题B组7.1

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-285_1000题A组11.1-2.md`
- wrongnet ID：`GS-285`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 球体表面积与体积相关变化率 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 相关变化率
- 复合函数求导
- 球体几何量公式

### 错因

- 暂无明确个人错因（视觉证据仅支持复做入口）

### 方法

- 相关变化率建模
- 链式法则
- 球体表面积公式
- 球体体积公式

### 陷阱

- 先写静态几何关系
- 求的是对时间的导数
- 最后代入 r=50
- 单位分别是面积速度和体积速度

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 S=4pi r^2、V=4/3 pi r^3，并标出 dr/dt=5 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是把对 r 的导数误当作对时间的变化率，没有乘上 dr/dt |
| related_method_card_id | H07-001 |
| next_reminder | 看到相关变化率，先写静态关系，再对 t 求导并代入指定时刻。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-030_复合函数求导]]
- [[MATHWIKI-KNOWLEDGE-096_相关变化率]]
- [[MATHWIKI-KNOWLEDGE-407_球体几何量公式]]
- [[MATHWIKI-METHOD-CLUSTER-1199_球体体积公式]]
- [[MATHWIKI-METHOD-CLUSTER-1200_球体表面积公式]]
- [[MATHWIKI-METHOD-CLUSTER-1225_相关变化率建模]]
- [[MATHWIKI-METHOD-CLUSTER-135_链式法则]]

### 深度编译页

- [[MATHWIKI-GS-CONCEPT-001_条件边界]]
- [[MATHWIKI-GS-ERROR-001_边界条件遗漏]]
- [[MATHWIKI-GS-METHOD-001_先做条件边界清单]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-001_条件边界与分类讨论]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-GS-TRIGGER-001_参数端点定义域先停]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-260
- GS-261
- GS-262
- GS-295

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
