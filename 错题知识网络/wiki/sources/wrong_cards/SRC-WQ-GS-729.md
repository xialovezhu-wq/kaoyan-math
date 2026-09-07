---
wiki_id: SRC-WQ-GS-729
type: source_summary
title: "GS-729 57891 凸函数积分平均值不等式"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-729_57891凸函数积分平均值不等式.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-729_57891凸函数积分平均值不等式.md"
visual_ids:
  - "VIS-GS-729"
wrongnet_refs:
  - "GS-729"
knowledge:
  - "严格凸函数"
  - "切线与弦线"
  - "定积分比较"
  - "积分平均值"
  - "中心对称换元"
error_causes:
  - "几何到代数转换断点"
  - "动作链断裂"
  - "仿射函数积分性质不熟"
  - "对称积分理由不清"
methods:
  - "中点切线下界"
  - "端点弦线上界"
  - "逐点不等式积分"
  - "中点中心化"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS"
  - "MATHWIKI-ACTION-GAP-002"
  - "MATHWIKI-ERROR-CLUSTER-004"
  - "MATHWIKI-ERROR-CLUSTER-546"
  - "MATHWIKI-ERROR-CLUSTER-547"
  - "MATHWIKI-ERROR-CLUSTER-548"
  - "MATHWIKI-KNOWLEDGE-459"
  - "MATHWIKI-KNOWLEDGE-461"
  - "MATHWIKI-KNOWLEDGE-462"
  - "MATHWIKI-KNOWLEDGE-463"
  - "MATHWIKI-KNOWLEDGE-464"
  - "MATHWIKI-METHOD-CLUSTER-1503"
  - "MATHWIKI-METHOD-CLUSTER-1504"
  - "MATHWIKI-METHOD-CLUSTER-1505"
  - "MATHWIKI-METHOD-CLUSTER-1506"
status: indexed
formal_projection_sha256: 257d9db958e5f92a83fff3e9e742dc8a9f7793fa839d27ee66d47d66200e6364
last_updated: "2026-07-28"
related_wrongnet_refs: []
---

# GS-729 57891 凸函数积分平均值不等式

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-729_57891凸函数积分平均值不等式.md`
- wrongnet ID：`GS-729`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-729_57891凸函数积分平均值不等式|VIS-GS-729]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-729_57891%E5%87%B8%E5%87%BD%E6%95%B0%E7%A7%AF%E5%88%86%E5%B9%B3%E5%9D%87%E5%80%BC%E4%B8%8D%E7%AD%89%E5%BC%8F)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-729/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-729/solution_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 严格凸函数的 Hermite-Hadamard 不等式证明 |
| 日期 | 2026-07-28 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 本次正式结论

- 当前错点：几何结论已经具备，但没有完成“比较函数解析化—逐点不等式—两端积分”的形式化动作；尤其不熟悉仿射函数积分平均值等于端点平均值，以及区间关于中点对称时线性偏差项积分为零。
- 最新错误证据：2026-07-28 第1次错：能够从 $f''(x)>0$ 判断函数图像位于端点弦下方，也能理解积分平均值应夹在中点函数值与端点平均值之间；但把这些几何判断当作默认事实，不能写出中点切线与端点弦的解析式并逐点积分。看答案后又卡在两个基础等式：仿射函数在区间上的平均值等于两端值平均数，以及以中点 $m=(a+b)/2$ 为中心时 $\int_a^b(x-m)\,dx=0$。
- 最新掌握证据：2026-07-28 AI评分 3/5：几何图像与目标不等式判断正确；经解释后能理解切线下界、弦线上界、仿射函数平均值和中心奇对称积分，用户确认整题无问题，但尚未闭卷复写证明。

## 可编译信息

### 知识点

- 严格凸函数
- 切线与弦线
- 定积分比较
- 积分平均值
- 中心对称换元

### 错因

- 几何到代数转换断点
- 动作链断裂
- 仿射函数积分性质不熟
- 对称积分理由不清

### 方法

- 中点切线下界
- 端点弦线上界
- 逐点不等式积分
- 中点中心化

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 令 $m=(a+b)/2$，先写中点切线 $T(x)=f(m)+f'(m)(x-m)$ 与端点弦线 $L(x)$。 |
| missed_action | 没有把“切线在下、弦线在上”的图像关系写成可积分的解析不等式，也不清楚两个一次函数积分为何化简。 |
| related_method_card_id | H11-007 |
| next_reminder | 凸函数积分夹逼时，先造两条直线；中点切线负责下界，端点弦线负责上界，再对直线积分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-546_几何到代数转换断点]]
- [[MATHWIKI-ERROR-CLUSTER-547_仿射函数积分性质不熟]]
- [[MATHWIKI-ERROR-CLUSTER-548_对称积分理由不清]]
- [[MATHWIKI-KNOWLEDGE-459_定积分比较]]
- [[MATHWIKI-KNOWLEDGE-461_严格凸函数]]
- [[MATHWIKI-KNOWLEDGE-462_切线与弦线]]
- [[MATHWIKI-KNOWLEDGE-463_积分平均值]]
- [[MATHWIKI-KNOWLEDGE-464_中心对称换元]]
- [[MATHWIKI-METHOD-CLUSTER-1503_中点切线下界]]
- [[MATHWIKI-METHOD-CLUSTER-1504_端点弦线上界]]
- [[MATHWIKI-METHOD-CLUSTER-1505_逐点不等式积分]]
- [[MATHWIKI-METHOD-CLUSTER-1506_中点中心化]]

### 深度方法与专题

- 本批保持索引型编译；未新增深度专题关系。
