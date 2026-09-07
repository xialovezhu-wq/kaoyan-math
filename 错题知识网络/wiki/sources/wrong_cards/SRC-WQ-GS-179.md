---
wiki_id: SRC-WQ-GS-179
type: source_summary
title: "GS-179 1000题A组8.13"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-179_1000题A组8.13.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-179_1000题A组8.13.md"
visual_ids:
  - "VIS-GS-179"
wrongnet_refs:
  - "GS-179"
knowledge:
  - "反常积分"
  - "定积分"
  - "不定积分"
  - "分部积分"
  - "第一类换元"
  - "反正切型积分"
  - "对数型积分"
error_causes:
  - "柯西主值与普通反常积分混淆"
  - "无穷减无穷误判"
  - "收敛定义条件遗漏"
methods:
  - "反常积分极限"
  - "换元"
  - "比较判别法"
  - "逐项判别"
  - "双端反常积分拆分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS"
  - "MATHWIKI-ACTION-GAP-004"
  - "MATHWIKI-ERROR-CLUSTER-527"
  - "MATHWIKI-ERROR-CLUSTER-528"
  - "MATHWIKI-ERROR-CLUSTER-529"
  - "MATHWIKI-KNOWLEDGE-002"
  - "MATHWIKI-KNOWLEDGE-020"
  - "MATHWIKI-KNOWLEDGE-024"
  - "MATHWIKI-KNOWLEDGE-026"
  - "MATHWIKI-KNOWLEDGE-028"
  - "MATHWIKI-KNOWLEDGE-057"
  - "MATHWIKI-KNOWLEDGE-082"
  - "MATHWIKI-METHOD-CLUSTER-009"
  - "MATHWIKI-METHOD-CLUSTER-012"
  - "MATHWIKI-METHOD-CLUSTER-057"
  - "MATHWIKI-METHOD-CLUSTER-1368"
  - "MATHWIKI-METHOD-CLUSTER-1484"
  - "MATHWIKI-GS-TOPIC-006"
status: indexed
formal_projection_sha256: 86afa011667be9cdb6a77ede4d6607f37a2c089a4d48056e4746ea8bd53ce183
last_updated: "2026-07-27"
related_wrongnet_refs:
  - "GS-180"
---

# GS-179 1000题A组8.13

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-179_1000题A组8.13.md`
- wrongnet ID：`GS-179`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-179_1000题A组8.13|VIS-GS-179]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-179_1000%E9%A2%98A%E7%BB%848.13)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-179/question_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 反常积分 |
| 题型 | 反常积分敛散性选择 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 本次正式结论

- 当前错点：复做时把奇函数在对称截断下的相消误当成普通双端反常积分收敛，并把原函数两端的“正无穷减正无穷”直接判断为 0；没有先在有限点处分成左右两个反常积分并分别验证有限极限。
- 最新错误证据：2026-07-27 第2次错（正式错题复发）：最终选择 A；对 B、C 的换元与原函数判断基本正确，但认为 D 作为奇函数在对称区间积分应为 0，并把两端均趋于正无穷的对数原函数直接相减为 0。经讲解后才改用“左右两侧反常积分必须分别收敛”的定义判断 D 发散。
- 最新掌握证据：2026-07-27 AI评分 3/5：能够独立处理 B、C，并在讲解后准确复述普通收敛与柯西主值的区别；但最初选择错误，核心定义条件未独立触发，当前属于讲解后理解。

## 可编译信息

### 知识点

- 反常积分
- 定积分
- 不定积分
- 分部积分
- 第一类换元
- 反正切型积分
- 对数型积分

### 错因

- 柯西主值与普通反常积分混淆
- 无穷减无穷误判
- 收敛定义条件遗漏

### 方法

- 反常积分极限
- 换元
- 比较判别法
- 逐项判别
- 双端反常积分拆分

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先把无穷区间拆成两侧反常积分，逐侧检查极限是否有限存在。 |
| missed_action | 本次明确把 D 的奇函数对称相消和两端对数原函数的“正无穷减正无穷”当成收敛到 0，没有先分别检查左右两侧有限极限。 |
| related_method_card_id | H08-005 |
| next_reminder | 无穷区间奇函数题先拆两侧极限；主值相消不是收敛。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-527_柯西主值与普通反常积分混淆]]
- [[MATHWIKI-ERROR-CLUSTER-528_无穷减无穷误判]]
- [[MATHWIKI-ERROR-CLUSTER-529_收敛定义条件遗漏]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-028_反常积分]]
- [[MATHWIKI-KNOWLEDGE-057_对数型积分]]
- [[MATHWIKI-KNOWLEDGE-082_反正切型积分]]
- [[MATHWIKI-METHOD-CLUSTER-009_换元]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-057_反常积分极限]]
- [[MATHWIKI-METHOD-CLUSTER-1368_逐项判别]]
- [[MATHWIKI-METHOD-CLUSTER-1484_双端反常积分拆分]]

### 深度方法与专题

- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
