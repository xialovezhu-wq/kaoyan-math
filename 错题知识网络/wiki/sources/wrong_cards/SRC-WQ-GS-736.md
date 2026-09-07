---
wiki_id: SRC-WQ-GS-736
type: source_summary
title: GS-736 102387 高斯公式与奇对称
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-736_102387高斯公式与奇对称.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-736_102387高斯公式与奇对称.md
visual_ids:
- VIS-GS-736
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-736/question_01.png
solution_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-736/solution_01.png
reference_asset_refs: []
wrongnet_refs:
- GS-736
related_wrongnet_refs: []
knowledge:
- 多元函数积分学
- 第二型曲面积分
- 高斯公式
- 三重积分
- 空间区域对称性
- 有符号定积分
- 极坐标
error_causes:
- 对称性触发缺失
- 对称平面识别不稳
- 平方公式辨认混乱
- 完整周期符号忽略
- 积分几何意义混淆
- 闭合边界对象不清
- 外法向与体内积分混淆
- 坐标轴与坐标面对称混淆
- 只看投影忽略高度约束
- 反射变量选择不稳
methods:
- 高斯公式
- 坐标反射配对
- 奇函数积分为零
- 先积 z 再投影
- 圆盘极坐标
wiki_refs:
- MATHWIKI-ACTION-GAP-003
- MATHWIKI-ERROR-CLUSTER-593
- MATHWIKI-ERROR-CLUSTER-594
- MATHWIKI-ERROR-CLUSTER-595
- MATHWIKI-ERROR-CLUSTER-596
- MATHWIKI-ERROR-CLUSTER-597
- MATHWIKI-KNOWLEDGE-073
- MATHWIKI-KNOWLEDGE-106
- MATHWIKI-KNOWLEDGE-123
- MATHWIKI-KNOWLEDGE-448
- MATHWIKI-KNOWLEDGE-491
- MATHWIKI-KNOWLEDGE-492
- MATHWIKI-KNOWLEDGE-493
- MATHWIKI-METHOD-CLUSTER-1540
- MATHWIKI-METHOD-CLUSTER-1541
- MATHWIKI-METHOD-CLUSTER-1542
- MATHWIKI-METHOD-CLUSTER-1543
- MATHWIKI-METHOD-CLUSTER-1544
chapter: 多元函数积分学
question_type: 高斯公式与空间区域奇对称化简
card_status: 待复做
priority: A
evidence_status: user_confirmed
personal_diagnosis_status: user_confirmed
status: indexed
formal_projection_sha256: 64e6987e8bd1a2cac9e5b1c3331eb26fd10a542f220067dc79ce4a747711ac7d
last_updated: '2026-09-02'
---

# GS-736 102387 高斯公式与奇对称

## 题目定位

高斯公式与空间区域奇对称化简。

## 当前错因

已独立写出x²+y²≤1、0≤z≤1-x并想到高斯公式，但先不理解整个边界已封闭及外侧的法向约定，把体内三重积分与曲面取内侧混淆；随后只看圆盘的轴对称，未检查完整立体的坐标反射不变性，并混淆应取反哪个变量。

## 独立步骤与提示依赖

调度评分3/5；区域不等式和高斯公式入口有独立证据。闭合性、外法向符号、散度修正、y取反时区域不变及奇项消去均经讲解后确认；最终5π/4来自助手卷面写法，未见用户独立计算。卷面补充包属于同一次学习，不新增错次或评分。

## 下次复做动作

先将Σ认作Ω的完整封闭边界，外侧采用标准高斯公式正号；区分体内积分区域与边界法向方向。

## 来源

- [[错题知识网络/错题卡/GS-736_102387高斯公式与奇对称|GS-736 正式卡与完整历史]]

## 知识簇

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-003]]
- [[MATHWIKI-KNOWLEDGE-073]]
- [[MATHWIKI-KNOWLEDGE-448]]
- [[MATHWIKI-KNOWLEDGE-123]]
- [[MATHWIKI-KNOWLEDGE-491]]
- [[MATHWIKI-KNOWLEDGE-106]]
- [[MATHWIKI-KNOWLEDGE-492]]
- [[MATHWIKI-KNOWLEDGE-493]]
- [[MATHWIKI-METHOD-CLUSTER-1540]]
- [[MATHWIKI-METHOD-CLUSTER-1541]]
- [[MATHWIKI-METHOD-CLUSTER-1542]]
- [[MATHWIKI-METHOD-CLUSTER-1543]]
- [[MATHWIKI-METHOD-CLUSTER-1544]]
- [[MATHWIKI-ERROR-CLUSTER-593]]
- [[MATHWIKI-ERROR-CLUSTER-594]]
- [[MATHWIKI-ERROR-CLUSTER-595]]
- [[MATHWIKI-ERROR-CLUSTER-596]]
- [[MATHWIKI-ERROR-CLUSTER-597]]
