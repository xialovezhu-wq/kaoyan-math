---
wiki_id: SRC-WQ-GS-656
type: source_summary
title: "GS-656 138717 方向导数存在性陷阱"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-656_138717方向导数存在性陷阱.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-656"
knowledge:
  - "多元函数微分学"
  - "方向导数"
  - "方向导数存在性"
  - "多元函数极限"
  - "极限与连续"
error_causes:
  - "概念边界混淆"
  - "定义触发缺失"
  - "方法论调取失败"
  - "题面语言翻译断点"
  - "动作链断裂"
methods:
  - "定义法求方向导数"
  - "方向余弦参数化"
  - "固定射线取极限"
  - "特殊路径"
  - "二重极限路径法"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-020_题面语言翻译断点"
  - "MATHWIKI-ERROR-CLUSTER-027_概念边界混淆"
  - "MATHWIKI-ERROR-CLUSTER-052_定义触发缺失"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-KNOWLEDGE-067_多元函数极限"
  - "MATHWIKI-KNOWLEDGE-148_方向导数"
  - "MATHWIKI-KNOWLEDGE-377_方向导数存在性"
  - "MATHWIKI-METHOD-CLUSTER-022_特殊路径"
  - "MATHWIKI-METHOD-CLUSTER-1055_方向余弦参数化"
  - "MATHWIKI-METHOD-CLUSTER-555_二重极限路径法"
  - "MATHWIKI-METHOD-CLUSTER-842_固定射线取极限"
  - "MATHWIKI-METHOD-CLUSTER-890_定义法求方向导数"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-028_方向导数存在性陷阱"
  - "MATHWIKI-GS-METHOD-044_方向导数与梯度入口判别链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-656 138717 方向导数存在性陷阱

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-656_138717方向导数存在性陷阱.md`
- wrongnet ID：`GS-656`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 方向导数存在性与连续性反例判定 |
| 日期 | 2026-07-01 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数微分学
- 方向导数
- 方向导数存在性
- 多元函数极限
- 极限与连续

### 错因

- 概念边界混淆
- 定义触发缺失
- 方法论调取失败
- 题面语言翻译断点
- 动作链断裂

### 方法

- 定义法求方向导数
- 方向余弦参数化
- 固定射线取极限
- 特殊路径
- 二重极限路径法

### 陷阱

- 所有方向导数存在不能推出连续
- 方向导数中方向固定，只让步长 \(t\to0^+\)
- 连续性要求任意路径趋近，不能只看固定射线
- 沿 \(y=x^2\) 可使函数值恒为 1，但这不是固定方向射线

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先设固定方向 \(l=(\cos\theta,\sin\theta)\)，代入 \((x,y)=(t\cos\theta,t\sin\theta)\)，再判断足够小的 \(t>0\) 时是否落在 \(y=x^2,\ x\ne0\) 上。 |
| missed_action | 没有区分“固定方向射线上的一元极限”和“二元连续性中的任意路径极限”，也没有先用 \(t\sin\theta=t^2\cos^2\theta\) 分析射线与抛物线在原点附近是否重合。 |
| related_method_card_id | H17-002 |
| next_reminder | 看到“任意方向导数存在/判断连续”，先固定方向写 \((t\cos\theta,t\sin\theta)\) 做方向导数，再另用特殊路径检查二重极限。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-020_题面语言翻译断点]]
- [[MATHWIKI-ERROR-CLUSTER-027_概念边界混淆]]
- [[MATHWIKI-ERROR-CLUSTER-052_定义触发缺失]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-KNOWLEDGE-067_多元函数极限]]
- [[MATHWIKI-KNOWLEDGE-148_方向导数]]
- [[MATHWIKI-KNOWLEDGE-377_方向导数存在性]]
- [[MATHWIKI-METHOD-CLUSTER-022_特殊路径]]
- [[MATHWIKI-METHOD-CLUSTER-1055_方向余弦参数化]]
- [[MATHWIKI-METHOD-CLUSTER-555_二重极限路径法]]
- [[MATHWIKI-METHOD-CLUSTER-842_固定射线取极限]]
- [[MATHWIKI-METHOD-CLUSTER-890_定义法求方向导数]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-028_方向导数存在性陷阱]]
- [[MATHWIKI-GS-METHOD-044_方向导数与梯度入口判别链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-350
- GS-654

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
