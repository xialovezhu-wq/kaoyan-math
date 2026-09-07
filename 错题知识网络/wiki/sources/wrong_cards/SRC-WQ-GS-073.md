---
wiki_id: SRC-WQ-GS-073
type: source_summary
title: "GS-073 103499"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-073_103499.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-073"
knowledge:
  - "定积分"
  - "三角换元"
  - "分部积分"
  - "数列极限"
  - "指数型极限"
  - "等价无穷小"
error_causes:
  - "概念混淆"
  - "方法选择错误"
  - "结构转化失败"
  - "过程跳步"
methods:
  - "三角换元"
  - "恒等变形"
  - "分部积分"
  - "递推关系"
  - "指数型极限对数化"
  - "等价无穷小"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-093_结构转化失败"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-009_数列极限"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-080_三角换元"
  - "MATHWIKI-KNOWLEDGE-210_指数型极限"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-026_等价无穷小"
  - "MATHWIKI-METHOD-CLUSTER-028_三角换元"
  - "MATHWIKI-METHOD-CLUSTER-1024_指数型极限对数化"
  - "MATHWIKI-METHOD-CLUSTER-227_恒等变形"
  - "MATHWIKI-METHOD-CLUSTER-465_递推关系"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-316"
  - "GS-317"
formal_projection_sha256: 727336551010a0ae185e01ab328b6f96f3b73aef1b125897c9c049becc4a3c31
---

# GS-073 103499

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-073_103499.md`
- wrongnet ID：`GS-073`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 三角换元积分与指数型数列极限 |
| 日期 | 2026-05-11 |
| 状态 | 已掌握 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 三角换元
- 分部积分
- 数列极限
- 指数型极限
- 等价无穷小

### 错因

- 概念混淆
- 方法选择错误
- 结构转化失败
- 过程跳步

### 方法

- 三角换元
- 恒等变形
- 分部积分
- 递推关系
- 指数型极限对数化
- 等价无穷小

### 陷阱

- 积分比值不可约
- 积分号不是乘法括号
- 递推关系入口
- 指数型极限

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先令 \(x=\sin t\) 把积分化为三角形式，再用 \(\cos^2t=1-\sin^2t\) 得到 \(a_n=b_n-b_{n+2}\)，再建立递推比值 |
| missed_action | 没有先把积分结构转成递推关系，而是把两个积分的比值误当作被积函数可以约掉 |
| related_method_card_id | H09-001 |
| next_reminder | 看到两个参数积分的比值，先找恒等变形建立积分递推关系，不要约掉被积函数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-093_结构转化失败]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-009_数列极限]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-080_三角换元]]
- [[MATHWIKI-KNOWLEDGE-210_指数型极限]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-026_等价无穷小]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-1024_指数型极限对数化]]
- [[MATHWIKI-METHOD-CLUSTER-227_恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-465_递推关系]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-316
- GS-317

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
