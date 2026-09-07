---
wiki_id: SRC-WQ-GS-350
type: source_summary
title: "GS-350 强化例题13.10-2"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-350_强化例题13.10-2.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-350"
knowledge:
  - "多元函数微分学"
  - "多元函数连续可微"
  - "多元函数偏导"
  - "可微定义"
  - "一阶线性主部"
  - "极限与连续"
error_causes:
  - "定义触发缺失"
  - "可微定义遗忘"
  - "线性主部识别断点"
  - "小o结构识别不敏感"
  - "方法论调取失败"
methods:
  - "取绝对值"
  - "有界性放缩"
  - "偏导定义"
  - "可微定义"
  - "一阶线性主部"
  - "凑Δz-dz"
  - "小o误差项"
  - "特殊路径"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-052_定义触发缺失"
  - "MATHWIKI-ERROR-CLUSTER-053_小o结构识别不敏感"
  - "MATHWIKI-ERROR-CLUSTER-074_可微定义遗忘"
  - "MATHWIKI-ERROR-CLUSTER-092_线性主部识别断点"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-019_多元函数微分学"
  - "MATHWIKI-KNOWLEDGE-037_多元函数连续可微"
  - "MATHWIKI-KNOWLEDGE-072_可微定义"
  - "MATHWIKI-KNOWLEDGE-189_一阶线性主部"
  - "MATHWIKI-METHOD-CLUSTER-022_特殊路径"
  - "MATHWIKI-METHOD-CLUSTER-029_偏导定义"
  - "MATHWIKI-METHOD-CLUSTER-030_取绝对值"
  - "MATHWIKI-METHOD-CLUSTER-031_有界性放缩"
  - "MATHWIKI-METHOD-CLUSTER-041_可微定义"
  - "MATHWIKI-METHOD-CLUSTER-137_一阶线性主部"
  - "MATHWIKI-METHOD-CLUSTER-299_凑Δz-dz"
  - "MATHWIKI-METHOD-CLUSTER-360_小o误差项"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-050_二元函数性质定义判别链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-350 强化例题13.10-2

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-350_强化例题13.10-2.md`
- wrongnet ID：`GS-350`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 二元函数连续性与可微性判定 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数微分学
- 多元函数连续可微
- 多元函数偏导
- 可微定义
- 一阶线性主部
- 极限与连续

### 错因

- 定义触发缺失
- 可微定义遗忘
- 线性主部识别断点
- 小o结构识别不敏感
- 方法论调取失败

### 方法

- 取绝对值
- 有界性放缩
- 偏导定义
- 可微定义
- 一阶线性主部
- 凑Δz-dz
- 小o误差项
- 特殊路径

### 陷阱

- 可微定义误差项
- 线性主部反向识别
- 小o除以rho
- f(0,0)补项
- 偏导存在不推出可微

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 \(|f(x,y)|=\frac{x^2}{x^2+y^2}|y|\le |y|\)；进入可微性时，先分别沿 \(x\) 轴和 \(y\) 轴套偏导定义。 |
| missed_action | 不知道连续和可微各自从哪个定义起步，也没有把可微判断转成 \(\Delta f-f_x(0,0)\Delta x-f_y(0,0)\Delta y=o(\rho)\)。 |
| related_method_card_id | H13-005 |
| next_reminder | 看到二元函数在一点判断连续和可微，先连续放缩，再按偏导定义算坐标轴偏导，最后写可微定义余项并找路径检验是否趋零。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-052_定义触发缺失]]
- [[MATHWIKI-ERROR-CLUSTER-053_小o结构识别不敏感]]
- [[MATHWIKI-ERROR-CLUSTER-074_可微定义遗忘]]
- [[MATHWIKI-ERROR-CLUSTER-092_线性主部识别断点]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-019_多元函数微分学]]
- [[MATHWIKI-KNOWLEDGE-037_多元函数连续可微]]
- [[MATHWIKI-KNOWLEDGE-072_可微定义]]
- [[MATHWIKI-KNOWLEDGE-189_一阶线性主部]]
- [[MATHWIKI-METHOD-CLUSTER-022_特殊路径]]
- [[MATHWIKI-METHOD-CLUSTER-029_偏导定义]]
- [[MATHWIKI-METHOD-CLUSTER-030_取绝对值]]
- [[MATHWIKI-METHOD-CLUSTER-031_有界性放缩]]
- [[MATHWIKI-METHOD-CLUSTER-041_可微定义]]
- [[MATHWIKI-METHOD-CLUSTER-137_一阶线性主部]]
- [[MATHWIKI-METHOD-CLUSTER-299_凑Δz-dz]]
- [[MATHWIKI-METHOD-CLUSTER-360_小o误差项]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-050_二元函数性质定义判别链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-626
- GS-354
- GS-358
- GS-364
- GS-047
- GS-349

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
