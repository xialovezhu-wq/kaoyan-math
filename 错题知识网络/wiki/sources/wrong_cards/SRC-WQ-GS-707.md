---
wiki_id: SRC-WQ-GS-707
type: source_summary
title: GS-707 102348 向量场做功与格林公式
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-707_102348向量场做功与格林公式.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-707_102348向量场做功与格林公式.md
visual_ids:
- VIS-GS-707
wrongnet_refs:
- GS-707
knowledge:
- 多元函数积分学
- 向量场
- 曲线积分
- 第二型曲线积分
- 格林公式
- 二重积分极坐标法
- 变力做功积分
error_causes:
- 概念边界混淆
- 向量场分量映射不熟
- 方法调取失败
- 区域对象混淆
- 方向条件检查遗漏
methods:
- 向量场分量拆分
- 功的点积微元
- 格林公式
- 方向换号
- 极坐标面积微元
wiki_refs:
- MATHWIKI-COVERAGE-GS
- MATHWIKI-ACTION-GAP-001
- MATHWIKI-ERROR-CLUSTER-027
- MATHWIKI-ERROR-CLUSTER-513
- MATHWIKI-ERROR-CLUSTER-013
- MATHWIKI-ERROR-CLUSTER-510
- MATHWIKI-KNOWLEDGE-073
- MATHWIKI-KNOWLEDGE-325
- MATHWIKI-KNOWLEDGE-151
- MATHWIKI-KNOWLEDGE-447
- MATHWIKI-KNOWLEDGE-445
- MATHWIKI-KNOWLEDGE-070
- MATHWIKI-KNOWLEDGE-245
- MATHWIKI-METHOD-CLUSTER-826
- MATHWIKI-METHOD-CLUSTER-1467
- MATHWIKI-METHOD-CLUSTER-1478
- MATHWIKI-METHOD-CLUSTER-1477
- MATHWIKI-METHOD-CLUSTER-237
- MATHWIKI-GS-METHOD-102
- MATHWIKI-GS-TOPIC-014
status: indexed
formal_projection_sha256: 26ce1f213bd1461c0b8be4c5918b5a58938c3ca81be334057568b2c43e665948
last_updated: '2026-08-03'
---
# GS-707 102348 向量场做功与格林公式

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-707_102348向量场做功与格林公式.md`
- wrongnet ID：`GS-707`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-707_102348向量场做功与格林公式|VIS-GS-707]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-707_102348%E5%90%91%E9%87%8F%E5%9C%BA%E5%81%9A%E5%8A%9F%E4%B8%8E%E6%A0%BC%E6%9E%97%E5%85%AC%E5%BC%8F)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-707/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-707/solution_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数积分学 |
| 题型 | 向量场沿闭曲线做功与格林公式 |
| 日期 | 2026-07-19 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数积分学
- 向量场
- 曲线积分
- 第二型曲线积分
- 格林公式
- 二重积分极坐标法
- 变力做功积分

### 错因

- 概念边界混淆
- 向量场分量映射不熟
- 方法调取失败
- 区域对象混淆
- 方向条件检查遗漏

### 方法

- 向量场分量拆分
- 功的点积微元
- 格林公式
- 方向换号
- 极坐标面积微元

### 陷阱

- 变力不能用总路程乘固定力
- i 前系数是 P，j 前系数是 Q
- 格林公式正向是逆时针
- L 是边界曲线，D 是内部圆盘
- dA=r dr dθ

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 \(P=-x^2y\)、\(Q=xy^2\)，从而 \(W=\oint_LP\,dx+Q\,dy\)。 |
| missed_action | 虽想到闭曲线和格林公式，但没有先把 F 拆成 P、Q 并与位移微元点乘写成功的第二型曲线积分。 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到位置相关力场沿曲线做功，先拆 P、Q 并写 F·dr=Pdx+Qdy；闭曲线再查方向和格林公式。 |

## 已连接 wiki

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-027_概念边界混淆]]
- [[MATHWIKI-ERROR-CLUSTER-513_向量场分量映射不熟]]
- [[MATHWIKI-ERROR-CLUSTER-013_方法调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-510_区域对象混淆]]
- [[MATHWIKI-KNOWLEDGE-073_多元函数积分学]]
- [[MATHWIKI-KNOWLEDGE-325_向量场]]
- [[MATHWIKI-KNOWLEDGE-151_曲线积分]]
- [[MATHWIKI-KNOWLEDGE-447_第二型曲线积分]]
- [[MATHWIKI-KNOWLEDGE-445_格林公式]]
- [[MATHWIKI-KNOWLEDGE-070_二重积分极坐标法]]
- [[MATHWIKI-KNOWLEDGE-245_变力做功积分]]
- [[MATHWIKI-METHOD-CLUSTER-826_向量场分量拆分]]
- [[MATHWIKI-METHOD-CLUSTER-1467_功的点积微元]]
- [[MATHWIKI-METHOD-CLUSTER-1478_格林公式]]
- [[MATHWIKI-METHOD-CLUSTER-1477_方向换号]]
- [[MATHWIKI-METHOD-CLUSTER-237_极坐标面积微元]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-102_第18讲多元积分方法卡总表]]
- [[MATHWIKI-GS-TOPIC-014_向量场与旋度错题总线]]

说明：索引型簇页保证本题进入全量知识图谱；深度编译页沉淀可迁移的方法、专题或错因。

## wrongnet 关联题

- 暂无正式关系；本次相似关系只写入 SHADOW 提案回执。

## 下一步

- 复做时先检查 method_gap 中的第一动作，再检查对应错因簇。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
