---
wiki_id: SRC-WQ-GS-217
type: source_summary
title: GS-217 强化例题11.18
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-217_强化例题11.18.md
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
- GS-217
knowledge:
- 一元函数微分学应用
- 一阶 Taylor 公式
- 二阶 Lagrange 余项
- 端点线性插值误差
- 定积分
- 积分放缩
error_causes:
- 目标系数反推权重未触发
- 加权消项动作链断裂
- 积分三角不等式未独立写出
methods:
- 泰勒展开
- 拉格朗日余项
- 端点线性插值
- 积分放缩
wiki_refs:
- MATHWIKI-ACTION-GAP-002
- MATHWIKI-ERROR-CLUSTER-261
- MATHWIKI-KNOWLEDGE-001
- MATHWIKI-KNOWLEDGE-002
- MATHWIKI-KNOWLEDGE-007
- MATHWIKI-KNOWLEDGE-010
- MATHWIKI-KNOWLEDGE-015
- MATHWIKI-METHOD-CLUSTER-008
- MATHWIKI-METHOD-CLUSTER-118
- MATHWIKI-METHOD-CLUSTER-1279
- MATHWIKI-METHOD-CLUSTER-442
status: indexed
last_updated: '2026-09-02'
formal_projection_sha256: 9fc0eb527fcc2654321ba07074992f74f6f88f4461eb9f970e1f00356a775806
---

# GS-217 强化例题11.18

## 题目定位

一阶 Taylor 公式及二阶 Lagrange 余项误差估计。

## 当前错因

用户独立正确写出0、1两端带二阶Lagrange余项的Taylor公式，并知道两个中间点不同；写完后只尝试直接相加或相减，没有由目标端点系数反推出分别乘1-x、x的加权消项。加权与绝对值估计在讲解后建立，第二问的积分三角不等式由助手补齐。

## 独立步骤与提示依赖

未新增评分：双端Taylor书写和不同中间点的识别有独立证据；目标权重反推、第一问放缩与第二问完整证明依赖讲解。调度评分因2026-09-06才到期而未写入，保留score_ref缺失事实；未见无提示完整重做。

## 下次复做动作

先把0点展开式乘1-x、1点展开式乘x，再检查一阶项x(1-x)[f'(0)-f'(1)]为零。

## 来源

- [[错题知识网络/错题卡/GS-217_强化例题11.18|GS-217 正式卡与完整历史]]

## 知识簇

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-261_旧批量导入未记录用户个人错因-本轮仅按题图、解析入口和方法页确认“双端点]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-010_中值定理]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-METHOD-CLUSTER-008_泰勒展开]]
- [[MATHWIKI-METHOD-CLUSTER-118_拉格朗日余项]]
- [[MATHWIKI-METHOD-CLUSTER-1279_端点线性插值]]
- [[MATHWIKI-METHOD-CLUSTER-442_积分放缩]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-084_双端点Taylor余项估值链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]
