---
wiki_id: SRC-WQ-GS-670
type: source_summary
title: "GS-670 102450 椭球伸缩换元球面坐标"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-670_102450椭球伸缩换元球面坐标.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-670_102450椭球伸缩换元球面坐标.md"
visual_ids:
  - "VIS-GS-670"
wrongnet_refs:
  - "GS-670"
knowledge:
  - "多元函数积分学"
  - "三重积分"
  - "球面坐标"
  - "二次曲面"
error_causes:
  - "方法论调取失败"
  - "动作链断裂"
  - "空间几何图像断点"
  - "换元变量来源不清"
  - "雅可比因子遗漏风险"
  - "径向积分入口未触发"
  - "球壳分层未触发"
methods:
  - "三重积分换元"
  - "伸缩换元"
  - "雅可比行列式"
  - "球面坐标"
  - "坐标系选择"
  - "椭球化球"
  - "径向分层"
  - "球壳法"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS"
  - "MATHWIKI-ACTION-GAP-001"
  - "MATHWIKI-ERROR-CLUSTER-004"
  - "MATHWIKI-ERROR-CLUSTER-007"
  - "MATHWIKI-ERROR-CLUSTER-038"
  - "MATHWIKI-ERROR-CLUSTER-055"
  - "MATHWIKI-ERROR-CLUSTER-446"
  - "MATHWIKI-ERROR-CLUSTER-538"
  - "MATHWIKI-ERROR-CLUSTER-539"
  - "MATHWIKI-KNOWLEDGE-073"
  - "MATHWIKI-KNOWLEDGE-106"
  - "MATHWIKI-KNOWLEDGE-132"
  - "MATHWIKI-KNOWLEDGE-216"
  - "MATHWIKI-METHOD-CLUSTER-1145"
  - "MATHWIKI-METHOD-CLUSTER-1494"
  - "MATHWIKI-METHOD-CLUSTER-1495"
  - "MATHWIKI-METHOD-CLUSTER-246"
  - "MATHWIKI-METHOD-CLUSTER-273"
  - "MATHWIKI-METHOD-CLUSTER-345"
  - "MATHWIKI-METHOD-CLUSTER-472"
  - "MATHWIKI-METHOD-CLUSTER-597"
status: indexed
formal_projection_sha256: e2ac5cdc96a8edcc763dd6729518231052f5a44d5eac062aaf101c176dfa634d
last_updated: "2026-09-01"
related_wrongnet_refs: []
---

# GS-670 102450 椭球伸缩换元球面坐标

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-670_102450椭球伸缩换元球面坐标.md`
- wrongnet ID：`GS-670`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-670_102450椭球伸缩换元球面坐标|VIS-GS-670]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-670_102450%E6%A4%AD%E7%90%83%E4%BC%B8%E7%BC%A9%E6%8D%A2%E5%85%83%E7%90%83%E9%9D%A2%E5%9D%90%E6%A0%87)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-670/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-670/solution_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数积分学 |
| 题型 | 椭球区域三重积分的伸缩换元与球面坐标 |
| 日期 | 2026-07-06 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 本次正式结论

- 当前错点：看到椭球区域与被积函数共享同一个二次型 $x^2+4y^2+z^2$ 时，仍没有把 $4y^2$ 看成 $(2y)^2$ 并立即作伸缩换元 $u=x,\ v=2y,\ w=z$。会算椭球体积只能处理常数被积函数，不能替代对变量权重的积分；本次明确换元后，后续单位球计算能够推进。
- 最新错误证据：2026-07-28 第3次错（复发）：能够识别椭球半轴并正确算出体积 $\frac{2\pi}{3}$，但面对区域与被积函数共享二次型 $x^2+4y^2+z^2$ 时，仍没有触发伸缩换元 $u=x,\ v=2y,\ w=z$；提示换元后能够继续完成计算。本次口述中曾把原被积函数的减号说成加号，但没有稳定书面证据，故不计为正式错因。
- 最新掌握证据：2026-07-28 AI评分 1/5：能处理椭球体积，但没有由同形二次型调出伸缩换元这一主方法；明确提示换元后后续计算可以完成，当前首断点仍是方法入口。

## 可编译信息

### 知识点

- 多元函数积分学
- 三重积分
- 球面坐标
- 二次曲面

### 错因

- 方法论调取失败
- 动作链断裂
- 空间几何图像断点
- 换元变量来源不清
- 雅可比因子遗漏风险
- 径向积分入口未触发
- 球壳分层未触发

### 方法

- 三重积分换元
- 伸缩换元
- 雅可比行列式
- 球面坐标
- 坐标系选择
- 椭球化球
- 径向分层
- 球壳法

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把 $4y^2$ 写成 $(2y)^2$，令 $u=x,\ v=2y,\ w=z$。 |
| missed_action | 本次仍未由“区域与被积函数共享同一二次型”触发椭球伸缩换元；换元一经指出即可继续，首断点稳定落在第一方法入口。 |
| related_method_card_id | H18-016 |
| next_reminder | 看到椭球区域与被积函数共用同一二次型，先伸缩换元化单位球并补雅可比；若换元后被积函数只含 $r$，立即写球面坐标体积元，或用薄球壳 $4\pi r^2dr$ 化成一维径向积分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-038_空间几何图像断点]]
- [[MATHWIKI-ERROR-CLUSTER-055_换元变量来源不清]]
- [[MATHWIKI-ERROR-CLUSTER-446_雅可比因子遗漏风险]]
- [[MATHWIKI-ERROR-CLUSTER-538_径向积分入口未触发]]
- [[MATHWIKI-ERROR-CLUSTER-539_球壳分层未触发]]
- [[MATHWIKI-KNOWLEDGE-073_多元函数积分学]]
- [[MATHWIKI-KNOWLEDGE-106_三重积分]]
- [[MATHWIKI-KNOWLEDGE-132_二次曲面]]
- [[MATHWIKI-KNOWLEDGE-216_球面坐标]]
- [[MATHWIKI-METHOD-CLUSTER-1145_椭球化球]]
- [[MATHWIKI-METHOD-CLUSTER-1494_径向分层]]
- [[MATHWIKI-METHOD-CLUSTER-1495_球壳法]]
- [[MATHWIKI-METHOD-CLUSTER-246_球面坐标]]
- [[MATHWIKI-METHOD-CLUSTER-273_三重积分换元]]
- [[MATHWIKI-METHOD-CLUSTER-345_坐标系选择]]
- [[MATHWIKI-METHOD-CLUSTER-472_雅可比行列式]]
- [[MATHWIKI-METHOD-CLUSTER-597_伸缩换元]]

### 深度方法与专题

- 本批保持索引型编译；未新增深度专题关系。
