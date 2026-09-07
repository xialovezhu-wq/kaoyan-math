---
wiki_id: SRC-WQ-GS-410
type: source_summary
title: "GS-410 2021年真题第21题"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-410_2021年真题第21题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-410"
knowledge:
  - "二重积分"
  - "二重积分极坐标法"
error_causes:
  - "条件检查遗漏"
  - "方法调取失败"
methods:
  - "二重积分极坐标法"
  - "三角恒等变形"
  - "变量替换"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-013_方法调取失败"
  - "MATHWIKI-KNOWLEDGE-049_二重积分"
  - "MATHWIKI-KNOWLEDGE-070_二重积分极坐标法"
  - "MATHWIKI-METHOD-CLUSTER-025_三角恒等变形"
  - "MATHWIKI-METHOD-CLUSTER-047_二重积分极坐标法"
  - "MATHWIKI-METHOD-CLUSTER-809_变量替换"
  - "MATHWIKI-GS-METHOD-037_二重积分极坐标区域分块与对称化"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-410 2021年真题第21题

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-410_2021年真题第21题.md`
- wrongnet ID：`GS-410`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 二重积分 |
| 题型 | 二重积分极坐标计算 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 二重积分
- 二重积分极坐标法

### 错因

- 条件检查遗漏
- 方法调取失败

### 方法

- 二重积分极坐标法
- 三角恒等变形
- 变量替换

### 陷阱

- 由 \(r=\sqrt{\cos2\theta}\) 必须先判断 \(\cos2\theta\ge0\)
- 第一象限把角域收缩为 \(0\le\theta\le\frac{\pi}{4}\)
- \(xy\) 与面积微元共同给出 \(r^3\) 的径向积分

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先写出 r²=cos2θ，并由 cos2θ≥0 与第一象限限制角度范围 |
| missed_action | 没有先检查极坐标边界非负条件和角域 |
| related_method_card_id | H14-005 |
| next_reminder | 看到 (x²+y²)² 型曲线，先极坐标化，再用非负性和象限确定角域。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-KNOWLEDGE-049_二重积分]]
- [[MATHWIKI-KNOWLEDGE-070_二重积分极坐标法]]
- [[MATHWIKI-METHOD-CLUSTER-025_三角恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-047_二重积分极坐标法]]
- [[MATHWIKI-METHOD-CLUSTER-809_变量替换]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-037_二重积分极坐标区域分块与对称化]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-407
- GS-409
- GS-411
- GS-412

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
