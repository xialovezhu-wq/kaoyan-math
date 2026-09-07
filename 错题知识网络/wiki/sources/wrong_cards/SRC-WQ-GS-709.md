---
wiki_id: SRC-WQ-GS-709
type: source_summary
title: GS-709 79076 含奇点曲线积分与挖洞格林公式
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-709_79076含奇点曲线积分与挖洞格林公式.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-709_79076含奇点曲线积分与挖洞格林公式.md
visual_ids:
- VIS-GS-709
wrongnet_refs:
- GS-709
knowledge:
- 多元函数积分学
- 曲线积分
- 第二型曲线积分
- 格林公式
- 多连通区域
- 有向边界
- 椭圆面积
error_causes:
- 格林公式条件检查遗漏
- 奇点识别遗漏
- 偏导顺序写反
- 基础公式遗忘
methods:
- P与Q识别
- 奇点检查
- 挖洞法
- 多连通区域格林公式
- 小椭圆辅助线
- 面积公式
wiki_refs:
- MATHWIKI-COVERAGE-GS
- MATHWIKI-ACTION-GAP-004

- MATHWIKI-ERROR-CLUSTER-520

- MATHWIKI-ERROR-CLUSTER-515

- MATHWIKI-ERROR-CLUSTER-508

- MATHWIKI-ERROR-CLUSTER-514

- MATHWIKI-KNOWLEDGE-073

- MATHWIKI-KNOWLEDGE-151

- MATHWIKI-KNOWLEDGE-447

- MATHWIKI-KNOWLEDGE-445

- MATHWIKI-KNOWLEDGE-442

- MATHWIKI-KNOWLEDGE-444

- MATHWIKI-KNOWLEDGE-446

- MATHWIKI-METHOD-CLUSTER-1464

- MATHWIKI-METHOD-CLUSTER-1471

- MATHWIKI-METHOD-CLUSTER-1476

- MATHWIKI-METHOD-CLUSTER-1470

- MATHWIKI-METHOD-CLUSTER-1473

- MATHWIKI-METHOD-CLUSTER-266

- MATHWIKI-GS-METHOD-102
- MATHWIKI-GS-TOPIC-014
status: indexed
formal_projection_sha256: 93a9d5b387250333d688d0f5d47361763a8281bf7f0d527e55b909ac56215185
last_updated: '2026-08-27'
---
# GS-709 79076 含奇点曲线积分与挖洞格林公式

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-709_79076含奇点曲线积分与挖洞格林公式.md`
- wrongnet ID：`GS-709`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-709_79076含奇点曲线积分与挖洞格林公式|VIS-GS-709]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-709_79076%E5%90%AB%E5%A5%87%E7%82%B9%E6%9B%B2%E7%BA%BF%E7%A7%AF%E5%88%86%E4%B8%8E%E6%8C%96%E6%B4%9E%E6%A0%BC%E6%9E%97%E5%85%AC%E5%BC%8F)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-709/question_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数积分学 |
| 题型 | 含奇点闭曲线积分与挖洞格林公式 |
| 日期 | 2026-07-19 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 4 |

## 可编译信息

### 知识点

- 多元函数积分学
- 曲线积分
- 第二型曲线积分
- 格林公式
- 多连通区域
- 有向边界
- 椭圆面积

### 错因

- 格林公式条件检查遗漏
- 奇点识别遗漏
- 偏导顺序写反
- 基础公式遗忘

### 方法

- P与Q识别
- 奇点检查
- 挖洞法
- 多连通区域格林公式
- 小椭圆辅助线
- 面积公式

### 陷阱

- Q_x=P_y 只在无奇点处成立时不能推出原闭路积分为零
- 格林公式要求 P、Q 在相关区域内满足连续偏导条件
- 正向边界的内圈方向是顺时针
- 格林公式的组合是 Q_x-P_y
- 椭圆面积是 πab

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先解 \(4x^2+y^2=0\)，确认原点是奇点且位于 \(x^2+y^2=2\) 内部，因此不能直接对整圆盘套格林公式。 |
| missed_action | 算出 \(Q_x=P_y\) 后没有核对连续偏导条件，也没有先处理区域内部的原点奇点。 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到分式型闭曲线积分，先查分母零点和格林公式条件；写公式时固定按 dx 前为 P、dy 前为 Q，再写 Q_x-P_y。 |

## 已连接 wiki

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-520_格林公式条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-515_奇点识别遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-508_偏导顺序写反]]
- [[MATHWIKI-ERROR-CLUSTER-514_基础公式遗忘]]
- [[MATHWIKI-KNOWLEDGE-073_多元函数积分学]]
- [[MATHWIKI-KNOWLEDGE-151_曲线积分]]
- [[MATHWIKI-KNOWLEDGE-447_第二型曲线积分]]
- [[MATHWIKI-KNOWLEDGE-445_格林公式]]
- [[MATHWIKI-KNOWLEDGE-442_多连通区域]]
- [[MATHWIKI-KNOWLEDGE-444_有向边界]]
- [[MATHWIKI-KNOWLEDGE-446_椭圆面积]]
- [[MATHWIKI-METHOD-CLUSTER-1464_P与Q识别]]
- [[MATHWIKI-METHOD-CLUSTER-1471_奇点检查]]
- [[MATHWIKI-METHOD-CLUSTER-1476_挖洞法]]
- [[MATHWIKI-METHOD-CLUSTER-1470_多连通区域格林公式]]
- [[MATHWIKI-METHOD-CLUSTER-1473_小椭圆辅助线]]
- [[MATHWIKI-METHOD-CLUSTER-266_面积公式]]

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
