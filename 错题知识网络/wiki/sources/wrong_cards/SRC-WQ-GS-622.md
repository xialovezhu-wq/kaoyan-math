---
wiki_id: SRC-WQ-GS-622
type: source_summary
title: "GS-622 57931-2 共轭有理化与半角平方化"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-622_57931-2半角平方化凑微分.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-622_57931-2.md"
visual_ids:
  - "VIS-GS-622"
wrongnet_refs:
  - "GS-622"
knowledge:
  - "不定积分"
  - "一元函数积分学的计算"
  - "三角函数有理式"
  - "三角恒等变形"
  - "半角公式"
  - "分母平方化"
  - "万能代换"
  - "第一类换元"
  - "整体凑微分"
error_causes:
  - "三角有理式入口识别不足"
  - "半角公式触发失败"
  - "半角平方和意识不足"
  - "半角化简断点"
  - "分母平方化断点"
  - "凑d(tan(x/2))断点"
  - "动作链断裂"
  - "方法论调取失败"
  - "共轭有理化入口未触发"
  - "换元微分不匹配"
  - "标准导数识别断点"
methods:
  - "先判型"
  - "三角函数有理式"
  - "三角恒等变形"
  - "半角公式"
  - "分母平方化"
  - "万能代换"
  - "第一类换元"
  - "凑d(tan(x/2))"
  - "整体凑微分"
  - "共轭有理化"
  - "拆项积分"
  - "标准导数匹配"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS"
  - "MATHWIKI-ACTION-GAP-002"
  - "MATHWIKI-ERROR-CLUSTER-004"
  - "MATHWIKI-ERROR-CLUSTER-007"
  - "MATHWIKI-ERROR-CLUSTER-041"
  - "MATHWIKI-ERROR-CLUSTER-070"
  - "MATHWIKI-ERROR-CLUSTER-125"
  - "MATHWIKI-ERROR-CLUSTER-143"
  - "MATHWIKI-ERROR-CLUSTER-149"
  - "MATHWIKI-ERROR-CLUSTER-150"
  - "MATHWIKI-ERROR-CLUSTER-530"
  - "MATHWIKI-ERROR-CLUSTER-531"
  - "MATHWIKI-ERROR-CLUSTER-532"
  - "MATHWIKI-KNOWLEDGE-020"
  - "MATHWIKI-KNOWLEDGE-022"
  - "MATHWIKI-KNOWLEDGE-026"
  - "MATHWIKI-KNOWLEDGE-043"
  - "MATHWIKI-KNOWLEDGE-050"
  - "MATHWIKI-KNOWLEDGE-079"
  - "MATHWIKI-KNOWLEDGE-197"
  - "MATHWIKI-KNOWLEDGE-223"
  - "MATHWIKI-KNOWLEDGE-312"
  - "MATHWIKI-METHOD-CLUSTER-001"
  - "MATHWIKI-METHOD-CLUSTER-020"
  - "MATHWIKI-METHOD-CLUSTER-025"
  - "MATHWIKI-METHOD-CLUSTER-032"
  - "MATHWIKI-METHOD-CLUSTER-055"
  - "MATHWIKI-METHOD-CLUSTER-1485"
  - "MATHWIKI-METHOD-CLUSTER-1486"
  - "MATHWIKI-METHOD-CLUSTER-203"
  - "MATHWIKI-METHOD-CLUSTER-230"
  - "MATHWIKI-METHOD-CLUSTER-272"
  - "MATHWIKI-METHOD-CLUSTER-298"
  - "MATHWIKI-METHOD-CLUSTER-679"
  - "MATHWIKI-GS-METHOD-039"
  - "MATHWIKI-GS-METHOD-042"
  - "MATHWIKI-GS-TOPIC-013"
status: indexed
formal_projection_sha256: 55eaf897a2cbc651a803cd97511460e1ec4baa4d28ae5659d07e1734efa28029
last_updated: "2026-07-27"
related_wrongnet_refs:
  - "GS-624"
---

# GS-622 57931-2 共轭有理化与半角平方化

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-622_57931-2半角平方化凑微分.md`
- wrongnet ID：`GS-622`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-622_57931-2|VIS-GS-622]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-622_57931-2)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-622/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-622/solution_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 三角函数有理式不定积分：共轭有理化与半角平方化 |
| 日期 | 2026-06-24 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 本次正式结论

- 当前错点：本次看到 \(\int\frac{dx}{1+\sin x}\) 时，没有触发同乘共轭因子 \(1-\sin x\)，并在换元前未检查 \(dt=\cos x\,dx\) 与原式是否匹配；得到 \((1-\sin x)/\cos^2x\) 后又未立即拆成 \(\sec^2x-\sec x\tan x\)。原卡的半角平方化仍是等价备用路线。
- 最新错误证据：2026-07-27 第2次错（正式错题复发）：面对同一积分仍无法启动；先尝试只适用于 \(\sin^2x\) 的降幂公式，又令 \(t=1+\sin x\) 并反解 \(x=\arcsin(t-1)\)，没有检查 \(dt=\cos x\,dx\) 与原微分是否匹配。经提示同乘 \(1-\sin x\) 后，仍不能立即把结果拆成 \(\sec^2x-\sec x\tan x\)，完整讲解后才得到 \(\tan x-\sec x+C\)。
- 最新掌握证据：2026-07-27 AI评分 3/5：经两轮提示和完整讲解后能够核对 \(d(\cos x)=-\sin x\,dx\) 并复述结果，但没有独立触发共轭有理化与拆项，属于提示后完成。

## 可编译信息

### 知识点

- 不定积分
- 一元函数积分学的计算
- 三角函数有理式
- 三角恒等变形
- 半角公式
- 分母平方化
- 万能代换
- 第一类换元
- 整体凑微分

### 错因

- 三角有理式入口识别不足
- 半角公式触发失败
- 半角平方和意识不足
- 半角化简断点
- 分母平方化断点
- 凑d(tan(x/2))断点
- 动作链断裂
- 方法论调取失败
- 共轭有理化入口未触发
- 换元微分不匹配
- 标准导数识别断点

### 方法

- 先判型
- 三角函数有理式
- 三角恒等变形
- 半角公式
- 分母平方化
- 万能代换
- 第一类换元
- 凑d(tan(x/2))
- 整体凑微分
- 共轭有理化
- 拆项积分
- 标准导数匹配

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 看到分母 \(1+\sin x\)，先检查同乘 \(1-\sin x\) 能否制造平方差。 |
| missed_action | 本次先调用了不适用于一次 \(\sin x\) 的降幂公式，又作微分不匹配的直接换元；经提示共轭化后仍未独立完成拆项。 |
| related_method_card_id | H09-006 |
| next_reminder | 看到 \(1\pm\sin x\) 或 \(1\pm\cos x\) 作分母，先检查共轭平方差；化成平方分母后再拆成标准导数，换元前必须核对 \(dt\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-041_三角有理式入口识别不足]]
- [[MATHWIKI-ERROR-CLUSTER-070_半角公式触发失败]]
- [[MATHWIKI-ERROR-CLUSTER-125_凑d-tan-x-2-断点]]
- [[MATHWIKI-ERROR-CLUSTER-143_分母平方化断点]]
- [[MATHWIKI-ERROR-CLUSTER-149_半角化简断点]]
- [[MATHWIKI-ERROR-CLUSTER-150_半角平方和意识不足]]
- [[MATHWIKI-ERROR-CLUSTER-530_共轭有理化入口未触发]]
- [[MATHWIKI-ERROR-CLUSTER-531_换元微分不匹配]]
- [[MATHWIKI-ERROR-CLUSTER-532_标准导数识别断点]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-043_三角恒等变形]]
- [[MATHWIKI-KNOWLEDGE-050_整体凑微分]]
- [[MATHWIKI-KNOWLEDGE-079_三角函数有理式]]
- [[MATHWIKI-KNOWLEDGE-197_半角公式]]
- [[MATHWIKI-KNOWLEDGE-223_万能代换]]
- [[MATHWIKI-KNOWLEDGE-312_分母平方化]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-025_三角恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-032_整体凑微分]]
- [[MATHWIKI-METHOD-CLUSTER-055_三角函数有理式]]
- [[MATHWIKI-METHOD-CLUSTER-1485_共轭有理化]]
- [[MATHWIKI-METHOD-CLUSTER-1486_标准导数匹配]]
- [[MATHWIKI-METHOD-CLUSTER-203_半角公式]]
- [[MATHWIKI-METHOD-CLUSTER-230_拆项积分]]
- [[MATHWIKI-METHOD-CLUSTER-272_万能代换]]
- [[MATHWIKI-METHOD-CLUSTER-298_凑d-tan-x-2]]
- [[MATHWIKI-METHOD-CLUSTER-679_分母平方化]]

### 深度方法与专题

- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-METHOD-042_三角函数有理式入口四分流]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
