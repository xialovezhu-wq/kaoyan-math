---
wiki_id: SRC-WQ-GS-619
type: source_summary
title: "GS-619 57869-4 三角代换中段化简"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-619_57869-4三角代换中段化简.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-619_57869-4.md"
visual_ids:
  - "VIS-GS-619"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-619/question_01.png"
solution_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-619/solution_01.png"
wrongnet_refs:
  - "GS-619"
knowledge:
  - "不定积分"
  - "一元函数积分学的计算"
  - "第二类换元"
  - "第一类换元"
  - "根式换元"
  - "三角换元"
  - "三角恒等变形"
  - "整体凑微分"
  - "回代化简"
  - "三角形回代"
  - "反正切型积分"
  - "反三角函数积分"
  - "对数型积分"
error_causes:
  - "三角代换后中段化简断点"
  - "三角恒等式使用断点"
  - "整体凑微分识别断点"
  - "三角形回代断点"
  - "动作链断裂"
  - "结构整理断点"
  - "常见积分公式提取不稳"
methods:
  - "先判型"
  - "第二类换元"
  - "三角换元"
  - "三角恒等变形"
  - "整体凑微分"
  - "第一类换元"
  - "三角形回代"
  - "回代化简"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS"
  - "MATHWIKI-ERROR-CLUSTER-004"
  - "MATHWIKI-ERROR-CLUSTER-035"
  - "MATHWIKI-ERROR-CLUSTER-064"
  - "MATHWIKI-ERROR-CLUSTER-100"
  - "MATHWIKI-ERROR-CLUSTER-102"
  - "MATHWIKI-ERROR-CLUSTER-236"
  - "MATHWIKI-KNOWLEDGE-020"
  - "MATHWIKI-KNOWLEDGE-022"
  - "MATHWIKI-KNOWLEDGE-026"
  - "MATHWIKI-KNOWLEDGE-041"
  - "MATHWIKI-KNOWLEDGE-043"
  - "MATHWIKI-KNOWLEDGE-050"
  - "MATHWIKI-KNOWLEDGE-080"
  - "MATHWIKI-KNOWLEDGE-082"
  - "MATHWIKI-KNOWLEDGE-103"
  - "MATHWIKI-KNOWLEDGE-120"
  - "MATHWIKI-KNOWLEDGE-290"
  - "MATHWIKI-METHOD-CLUSTER-001"
  - "MATHWIKI-METHOD-CLUSTER-020"
  - "MATHWIKI-METHOD-CLUSTER-025"
  - "MATHWIKI-METHOD-CLUSTER-028"
  - "MATHWIKI-METHOD-CLUSTER-032"
  - "MATHWIKI-METHOD-CLUSTER-044"
  - "MATHWIKI-METHOD-CLUSTER-070"
  - "MATHWIKI-METHOD-CLUSTER-515"
  - "MATHWIKI-GS-METHOD-010"
  - "MATHWIKI-GS-METHOD-039"
  - "MATHWIKI-GS-METHOD-043"
  - "MATHWIKI-GS-TOPIC-013"
  - "MATHWIKI-SYNTHESIS-001"
status: indexed
last_updated: 2026-08-03
related_wrongnet_refs:
  - "GS-269"
  - "GS-618"
formal_projection_sha256: 3994a77c03c24533664f1bbec3ca76bf817f4678f203f0504d7e6eed869fb04e
---

# GS-619 57869-4 三角代换中段化简

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-619_57869-4三角代换中段化简.md`
- wrongnet ID：`GS-619`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-619_57869-4|VIS-GS-619]]
- 已核验题图与解析图各 1 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 根式复杂分母型不定积分：第二类换元后接第一类换元 |
| 日期 | 2026-06-24 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 不定积分
- 一元函数积分学的计算
- 第二类换元
- 第一类换元
- 根式换元
- 三角换元
- 三角恒等变形
- 整体凑微分
- 回代化简
- 三角形回代
- 反正切型积分
- 反三角函数积分
- 对数型积分

### 错因

- 三角代换后中段化简断点
- 三角恒等式使用断点
- 整体凑微分识别断点
- 三角形回代断点
- 动作链断裂
- 结构整理断点
- 常见积分公式提取不稳

### 方法

- 先判型
- 第二类换元
- 三角换元
- 三角恒等变形
- 整体凑微分
- 第一类换元
- 三角形回代
- 回代化简

### 陷阱

- \(\sqrt{1+x^2}\) 可先考虑 \(x=\tan t\)
- 换元后 \(\tan t,\sec t,\cos t\) 混杂时先统一成 \(\sin t,\cos t\)
- 分子分母同乘 \(\cos t\) 是为了制造 \(\cos tdt=d(\sin t)\)
- \(2\sin^2t+\cos^2t=1+\sin^2t\)
- 不要把 \(\int\frac{d(\sin t)}{1+\sin^2t}\) 误看成 \(\int \arctan(\sin t)d(\sin t)\)
- \(x=\tan t\Rightarrow \sin t=\frac{x}{\sqrt{1+x^2}}\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先把 \(\sec t\) 和 \(\tan t\) 全部改写成 \(\sin t,\cos t\)，再检查能否凑出 \(\cos tdt=d(\sin t)\)。 |
| missed_action | 没有想到分子分母同乘 \(\cos t\)，没有把分母化成 \(1+\sin^2t\)，没有把 \(\sin t\) 看成整体，最后也没有主动通过直角三角形回代 \(\sin t\)。 |
| related_method_card_id | H09-003 |
| next_reminder | 看到三角代换后出现 \(\cos tdt\)，先检查分母能不能化成只含 \(\sin t\) 的式子，再令 \(u=\sin t\) 并做三角形回代。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-035_结构整理断点]]
- [[MATHWIKI-ERROR-CLUSTER-064_三角恒等式使用断点]]
- [[MATHWIKI-ERROR-CLUSTER-100_三角代换后中段化简断点]]
- [[MATHWIKI-ERROR-CLUSTER-102_三角形回代断点]]
- [[MATHWIKI-ERROR-CLUSTER-236_整体凑微分识别断点]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-KNOWLEDGE-043_三角恒等变形]]
- [[MATHWIKI-KNOWLEDGE-050_整体凑微分]]
- [[MATHWIKI-KNOWLEDGE-080_三角换元]]
- [[MATHWIKI-KNOWLEDGE-082_反正切型积分]]
- [[MATHWIKI-KNOWLEDGE-103_根式换元]]
- [[MATHWIKI-KNOWLEDGE-120_回代化简]]
- [[MATHWIKI-KNOWLEDGE-290_三角形回代]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-025_三角恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-032_整体凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-044_第二类换元]]
- [[MATHWIKI-METHOD-CLUSTER-070_回代化简]]
- [[MATHWIKI-METHOD-CLUSTER-515_三角形回代]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-METHOD-043_根式积分换元与回代链]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-269
- GS-618

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
