---
wiki_id: SRC-WQ-GS-635
type: source_summary
title: "GS-635 58076-2 绝对值变上限分段"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-635_58076-2绝对值变上限分段.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-635"
knowledge:
  - "定积分"
  - "定积分性质"
  - "变上限积分"
  - "绝对值分类"
  - "绝对值分段"
  - "分段函数积分"
  - "参数范围"
  - "一元函数积分学的计算"
error_causes:
  - "变量取值范围未讨论"
  - "绝对值分段点与积分上下限位置关系未检查"
  - "默认变量为正"
  - "分类讨论不全"
  - "条件检查遗漏"
  - "动作链断裂"
  - "方法论调取失败"
methods:
  - "先判型"
  - "画轴排序"
  - "分段函数积分"
  - "绝对值分类"
  - "变上限积分拆区间"
  - "积分区间跨分段点检查"
  - "分类讨论"
  - "定积分计算"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-023_分类讨论不全"
  - "MATHWIKI-ERROR-CLUSTER-171_变量取值范围未讨论"
  - "MATHWIKI-ERROR-CLUSTER-419_绝对值分段点与积分上下限位置关系未检查"
  - "MATHWIKI-ERROR-CLUSTER-460_默认变量为正"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-052_绝对值分类"
  - "MATHWIKI-KNOWLEDGE-100_参数范围"
  - "MATHWIKI-KNOWLEDGE-116_分段函数积分"
  - "MATHWIKI-KNOWLEDGE-185_绝对值分段"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-042_定积分计算"
  - "MATHWIKI-METHOD-CLUSTER-065_分段函数积分"
  - "MATHWIKI-METHOD-CLUSTER-1259_积分区间跨分段点检查"
  - "MATHWIKI-METHOD-CLUSTER-248_画轴排序"
  - "MATHWIKI-METHOD-CLUSTER-258_绝对值分类"
  - "MATHWIKI-METHOD-CLUSTER-331_变上限积分拆区间"
  - "MATHWIKI-GS-CONCEPT-001_条件边界"
  - "MATHWIKI-GS-ERROR-001_边界条件遗漏"
  - "MATHWIKI-GS-METHOD-001_先做条件边界清单"
  - "MATHWIKI-GS-METHOD-004_分段点与上限变量排序"
  - "MATHWIKI-GS-METHOD-008_分类讨论闭环"
  - "MATHWIKI-GS-TOPIC-001_条件边界与分类讨论"
  - "MATHWIKI-GS-TOPIC-002_一元积分近期错题簇"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-GS-TRIGGER-001_参数端点定义域先停"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-288"
  - "GS-600"
formal_projection_sha256: f841e0b0e0b67266c80335ddcb2a129b4de4198c635ed572af46994c3bf88f91
---

# GS-635 58076-2 绝对值变上限分段

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-635_58076-2绝对值变上限分段.md`
- wrongnet ID：`GS-635`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 变上限定积分：绝对值分段点与上限变量位置讨论 |
| 日期 | 2026-06-27 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 变上限积分
- 绝对值分类
- 绝对值分段
- 分段函数积分
- 参数范围
- 一元函数积分学的计算

### 错因

- 变量取值范围未讨论
- 绝对值分段点与积分上下限位置关系未检查
- 默认变量为正
- 分类讨论不全
- 条件检查遗漏
- 动作链断裂
- 方法论调取失败

### 方法

- 先判型
- 画轴排序
- 分段函数积分
- 绝对值分类
- 变上限积分拆区间
- 积分区间跨分段点检查
- 分类讨论
- 定积分计算

### 陷阱

- 绝对值分段前先标出分段点
- 变上限积分要比较下限、分段点、上限变量的位置
- \(x\ge-1\) 不等于 \(x\ge0\)
- \(-1\le x<0\) 时区间 \([-1,x]\) 不跨过 \(0\)
- 只有 \(x\ge0\) 时才拆成 \([-1,0]\) 与 \([0,x]\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先画 \(t\) 轴，标出 \(-1,0,x\)，判断 \(x\) 在 \(0\) 左边还是右边。 |
| missed_action | 没有先讨论 \(x\) 的取值范围，直接默认 \(x\ge0\)，并把积分区间拆为 \([-1,0]\) 与 \([0,x]\)。 |
| related_method_card_id | H09-007 |
| next_reminder | 看到绝对值加变上限积分，先画轴排序下限、分段点、上限 \(x\)，再判断积分区间是否跨分段点。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-023_分类讨论不全]]
- [[MATHWIKI-ERROR-CLUSTER-171_变量取值范围未讨论]]
- [[MATHWIKI-ERROR-CLUSTER-419_绝对值分段点与积分上下限位置关系未检查]]
- [[MATHWIKI-ERROR-CLUSTER-460_默认变量为正]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-052_绝对值分类]]
- [[MATHWIKI-KNOWLEDGE-100_参数范围]]
- [[MATHWIKI-KNOWLEDGE-116_分段函数积分]]
- [[MATHWIKI-KNOWLEDGE-185_绝对值分段]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-042_定积分计算]]
- [[MATHWIKI-METHOD-CLUSTER-065_分段函数积分]]
- [[MATHWIKI-METHOD-CLUSTER-1259_积分区间跨分段点检查]]
- [[MATHWIKI-METHOD-CLUSTER-248_画轴排序]]
- [[MATHWIKI-METHOD-CLUSTER-258_绝对值分类]]
- [[MATHWIKI-METHOD-CLUSTER-331_变上限积分拆区间]]

### 深度编译页

- [[MATHWIKI-GS-CONCEPT-001_条件边界]]
- [[MATHWIKI-GS-ERROR-001_边界条件遗漏]]
- [[MATHWIKI-GS-METHOD-001_先做条件边界清单]]
- [[MATHWIKI-GS-METHOD-004_分段点与上限变量排序]]
- [[MATHWIKI-GS-METHOD-008_分类讨论闭环]]
- [[MATHWIKI-GS-TOPIC-001_条件边界与分类讨论]]
- [[MATHWIKI-GS-TOPIC-002_一元积分近期错题簇]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-GS-TRIGGER-001_参数端点定义域先停]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-288
- GS-600

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
