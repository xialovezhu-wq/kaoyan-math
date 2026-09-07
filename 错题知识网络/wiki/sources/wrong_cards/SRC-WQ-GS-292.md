---
wiki_id: SRC-WQ-GS-292
type: source_summary
title: "GS-292 强化例题9.22（77306）根号二次式三角换元绝对值"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-292_强化例题9.22(77306).md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-292"
knowledge:
  - "定积分"
  - "一元函数积分学的计算"
  - "根式积分"
  - "第二类换元"
  - "三角换元"
  - "绝对值分类"
  - "积分保号"
  - "三角恒等变形"
error_causes:
  - "三角换元分支选择不稳"
  - "根号绝对值处理缺失"
  - "符号检查缺失"
  - "积分保号意识不足"
  - "条件检查遗漏"
  - "动作链断裂"
  - "定积分换元细节错误"
methods:
  - "先判型"
  - "配方"
  - "平移换元"
  - "第二类换元"
  - "三角换元"
  - "特殊角换限"
  - "根号绝对值化简"
  - "符号复查"
  - "降幂公式"
  - "定积分计算"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-103_三角换元分支选择不稳"
  - "MATHWIKI-ERROR-CLUSTER-191_定积分换元细节错误"
  - "MATHWIKI-ERROR-CLUSTER-374_根号绝对值处理缺失"
  - "MATHWIKI-ERROR-CLUSTER-393_积分保号意识不足"
  - "MATHWIKI-ERROR-CLUSTER-402_符号检查缺失"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-041_第二类换元"
  - "MATHWIKI-KNOWLEDGE-043_三角恒等变形"
  - "MATHWIKI-KNOWLEDGE-052_绝对值分类"
  - "MATHWIKI-KNOWLEDGE-058_根式积分"
  - "MATHWIKI-KNOWLEDGE-080_三角换元"
  - "MATHWIKI-KNOWLEDGE-184_积分保号"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-028_三角换元"
  - "MATHWIKI-METHOD-CLUSTER-042_定积分计算"
  - "MATHWIKI-METHOD-CLUSTER-044_第二类换元"
  - "MATHWIKI-METHOD-CLUSTER-084_配方"
  - "MATHWIKI-METHOD-CLUSTER-136_降幂公式"
  - "MATHWIKI-METHOD-CLUSTER-174_符号复查"
  - "MATHWIKI-METHOD-CLUSTER-226_平移换元"
  - "MATHWIKI-METHOD-CLUSTER-245_特殊角换限"
  - "MATHWIKI-METHOD-CLUSTER-409_根号绝对值化简"
  - "MATHWIKI-GS-METHOD-079_分段积分变量角色与拼接链"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-633"
formal_projection_sha256: 867d890ce662091b4e199c172ca635fd1e0252eb808788e623a72129609fe7e3
---

# GS-292 强化例题9.22（77306）根号二次式三角换元绝对值

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-292_强化例题9.22(77306).md`
- wrongnet ID：`GS-292`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 根号二次式定积分：配方 + 三角换元 + 绝对值符号判断 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 一元函数积分学的计算
- 根式积分
- 第二类换元
- 三角换元
- 绝对值分类
- 积分保号
- 三角恒等变形

### 错因

- 三角换元分支选择不稳
- 根号绝对值处理缺失
- 符号检查缺失
- 积分保号意识不足
- 条件检查遗漏
- 动作链断裂
- 定积分换元细节错误

### 方法

- 先判型
- 配方
- 平移换元
- 第二类换元
- 三角换元
- 特殊角换限
- 根号绝对值化简
- 符号复查
- 降幂公式
- 定积分计算

### 陷阱

- 根号二次式先配方看标准圆
- \(2x-x^2=1-(x-1)^2\)
- 三角换元不是只选端点角度，还要选符号稳定的角度区间
- \(\sqrt{\cos^2t}=|\cos t|\)
- 只有确认 \(\cos t\ge0\)，才能把 \(|\cos t|\) 改成 \(\cos t\)
- 如果取 \(t:\frac{3\pi}{2}\to0\)，必须拆区间处理 \(|\cos t|\)
- 原积分非负，结果出现负值时必须做保号复查

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先把 \(2x-x^2\) 配方成 \(1-(x-1)^2\)，再令 \(u=x-1\)，把积分限从 \([0,1]\) 改为 \([-1,0]\)。 |
| missed_action | 三角换元后没有检查角度区间内 \(\cos t\) 的正负，把 \(\sqrt{\cos^2t}=|\cos t|\) 直接写成 \(\cos t\)。 |
| related_method_card_id | H09-003 |
| next_reminder | 三角换元后遇到 \(\sqrt{\cos^2t}\)，先写 \(|\cos t|\)；只有确认 \(\cos t\ge0\)，才能改成 \(\cos t\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-103_三角换元分支选择不稳]]
- [[MATHWIKI-ERROR-CLUSTER-191_定积分换元细节错误]]
- [[MATHWIKI-ERROR-CLUSTER-374_根号绝对值处理缺失]]
- [[MATHWIKI-ERROR-CLUSTER-393_积分保号意识不足]]
- [[MATHWIKI-ERROR-CLUSTER-402_符号检查缺失]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-KNOWLEDGE-043_三角恒等变形]]
- [[MATHWIKI-KNOWLEDGE-052_绝对值分类]]
- [[MATHWIKI-KNOWLEDGE-058_根式积分]]
- [[MATHWIKI-KNOWLEDGE-080_三角换元]]
- [[MATHWIKI-KNOWLEDGE-184_积分保号]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-042_定积分计算]]
- [[MATHWIKI-METHOD-CLUSTER-044_第二类换元]]
- [[MATHWIKI-METHOD-CLUSTER-084_配方]]
- [[MATHWIKI-METHOD-CLUSTER-136_降幂公式]]
- [[MATHWIKI-METHOD-CLUSTER-174_符号复查]]
- [[MATHWIKI-METHOD-CLUSTER-226_平移换元]]
- [[MATHWIKI-METHOD-CLUSTER-245_特殊角换限]]
- [[MATHWIKI-METHOD-CLUSTER-409_根号绝对值化简]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-079_分段积分变量角色与拼接链]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-633

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
