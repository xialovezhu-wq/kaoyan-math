---
wiki_id: SRC-WQ-GS-296
type: source_summary
title: "GS-296 2023年真题第19题"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-296_2023年真题第19题.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-296"
knowledge:
  - "定积分"
  - "定积分应用"
  - "旋转体体积"
  - "反常积分"
error_causes:
  - "知识：三角倒数函数原函数记忆错误。"
  - "换元：函数、微分和积分限没有同步变化。"
  - "方法触发：平方恒等式调用不稳。"
  - "计算：定积分上下限与符号分配错误。"
  - "概念：混淆函数值未定义、发散符号与单侧极限。"
methods:
  - "反常积分建模"
  - "旋转体体积公式"
  - "部分分式拆分"
  - "无界区间收口"
  - "三角换元"
  - "平方恒等式"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-006"

  - "MATHWIKI-ERROR-CLUSTER-248"

  - "MATHWIKI-KNOWLEDGE-002"

  - "MATHWIKI-KNOWLEDGE-028"

  - "MATHWIKI-KNOWLEDGE-035"

  - "MATHWIKI-KNOWLEDGE-149"

  - "MATHWIKI-METHOD-CLUSTER-1064"

  - "MATHWIKI-METHOD-CLUSTER-163"

  - "MATHWIKI-METHOD-CLUSTER-470"

  - "MATHWIKI-METHOD-CLUSTER-788"

  - "MATHWIKI-GS-METHOD-083_旋转体曲面变量选择与生成量链"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-08-27
formal_projection_sha256: 6628a9fd921c8f79de7a1075d8d2657065a7ee63020cb0e4bdee2c694f20a09e
---

# GS-296 2023年真题第19题

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-296_2023年真题第19题.md`
- wrongnet ID：`GS-296`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分应用 |
| 题型 | 无界区域面积与旋转体体积 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分应用
- 旋转体体积
- 反常积分

### 错因

- 旧批量导入未记录个人错因；依据题图/解析确认的可复做断点是没有先区分面积反常积分与圆盘法体积反常积分。

### 方法

- 反常积分建模
- 旋转体体积公式
- 部分分式拆分
- 无界区间收口

### 陷阱

- 面积与体积积分公式混用
- 无界上限没有写反常积分
- 体积公式漏平方

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B1-GOAL |
| expected_first_action | 先分别写 \(S=\int_1^{+\infty} y\,dx\) 和 \(V=\pi\int_1^{+\infty}y^2\,dx\)。 |
| missed_action | 旧卡未保存用户当时动作；当前可确认的复做断点是没有先区分面积与体积的积分对象。 |
| related_method_card_id | H10-002 |
| next_reminder | 看到无界面积和旋转体体积，先分别写面积积分与体积积分，再处理反常收敛。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-006_B1-GOAL]]
- [[MATHWIKI-ERROR-CLUSTER-248_旧批量导入未记录个人错因-依据题图-解析确认的可复做断点是没有先区分面积]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-028_反常积分]]
- [[MATHWIKI-KNOWLEDGE-035_定积分应用]]
- [[MATHWIKI-KNOWLEDGE-149_旋转体体积]]
- [[MATHWIKI-METHOD-CLUSTER-1064_无界区间收口]]
- [[MATHWIKI-METHOD-CLUSTER-163_旋转体体积公式]]
- [[MATHWIKI-METHOD-CLUSTER-470_部分分式拆分]]
- [[MATHWIKI-METHOD-CLUSTER-788_反常积分建模]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-083_旋转体曲面变量选择与生成量链]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
