---
wiki_id: SRC-WQ-GS-609
type: source_summary
title: "GS-609 57707-5 对数幂乘积积分泰勒误用"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-609_57707对数幂积分泰勒误用.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-609"
knowledge:
  - "不定积分"
  - "分部积分"
  - "有理函数积分"
  - "分式拆分"
  - "部分分式"
  - "对数幂积分"
error_causes:
  - "目标识别断点"
  - "泰勒截断误当恒等替换"
  - "方法选择错误"
  - "分部积分入口未触发"
methods:
  - "先判型"
  - "恒等拆分"
  - "分部积分"
  - "部分分式"
  - "凑微分换元"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-006_B1-GOAL"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-034_目标识别断点"
  - "MATHWIKI-ERROR-CLUSTER-051_分部积分入口未触发"
  - "MATHWIKI-ERROR-CLUSTER-386_泰勒截断误当恒等替换"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-044_有理函数积分"
  - "MATHWIKI-KNOWLEDGE-046_部分分式"
  - "MATHWIKI-KNOWLEDGE-194_分式拆分"
  - "MATHWIKI-KNOWLEDGE-249_对数幂积分"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-035_部分分式"
  - "MATHWIKI-METHOD-CLUSTER-064_凑微分换元"
  - "MATHWIKI-METHOD-CLUSTER-1002_恒等拆分"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
status: indexed
last_updated: 2026-07-15
---

# GS-609 57707-5 对数幂乘积积分泰勒误用

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-609_57707对数幂积分泰勒误用.md`
- wrongnet ID：`GS-609`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 对数函数与幂函数乘积型不定积分：恒等拆分 + 分部积分 + 部分分式 |
| 日期 | 2026-06-16 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 不定积分
- 分部积分
- 有理函数积分
- 分式拆分
- 部分分式
- 对数幂积分

### 错因

- 目标识别断点
- 泰勒截断误当恒等替换
- 方法选择错误
- 分部积分入口未触发

### 方法

- 先判型
- 恒等拆分
- 分部积分
- 部分分式
- 凑微分换元

### 陷阱

- 泰勒截断只给局部近似，不是恒等替换
- 求精确原函数不能用有限阶泰勒替代被积函数
- 即使被积函数近似为常数也要积分成 \(-\frac x2\)，不是 \(-\frac12\)
- \(\frac1{x^2}dx=-d(\frac1x)\)
- \(\frac1{x(1-x)}=\frac1x+\frac1{1-x}\)
- \(1-x>0\) 时 \(\ln|1-x|=\ln(1-x)\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B1-GOAL |
| expected_first_action | 先写出 \(\frac{x+\ln(1-x)}{x^2}=\frac1x+\frac{\ln(1-x)}{x^2}\)。 |
| missed_action | 没有先判断题目目标是"求精确原函数"；没有优先寻找恒等拆分与分部积分入口，反而把有限阶泰勒截断当恒等替换。 |
| related_method_card_id | H09-005 |
| next_reminder | 看到"不定积分求精确原函数"，先找恒等变形、换元、分部积分；泰勒截断只给局部近似，不能直接替代原式求精确积分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-006_B1-GOAL]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-034_目标识别断点]]
- [[MATHWIKI-ERROR-CLUSTER-051_分部积分入口未触发]]
- [[MATHWIKI-ERROR-CLUSTER-386_泰勒截断误当恒等替换]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-044_有理函数积分]]
- [[MATHWIKI-KNOWLEDGE-046_部分分式]]
- [[MATHWIKI-KNOWLEDGE-194_分式拆分]]
- [[MATHWIKI-KNOWLEDGE-249_对数幂积分]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-035_部分分式]]
- [[MATHWIKI-METHOD-CLUSTER-064_凑微分换元]]
- [[MATHWIKI-METHOD-CLUSTER-1002_恒等拆分]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-601
- GS-603
- GS-604
- GS-605

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
