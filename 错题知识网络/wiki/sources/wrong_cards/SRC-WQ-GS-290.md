---
wiki_id: SRC-WQ-GS-290
type: source_summary
title: "GS-290 强化例题9.20(90116)分段原函数连续拼接"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-290_强化例题9.20(90116).md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-290"
knowledge:
  - "不定积分"
  - "原函数"
  - "分段函数连续可导"
  - "极限与连续"
  - "一元函数积分学的计算"
  - "分部积分"
  - "分段函数积分"
error_causes:
  - "连续性条件未方程化"
  - "分段原函数常数拼接不熟"
  - "思路知道但动作未落地"
  - "积分常数匹配遗漏"
  - "条件检查遗漏"
  - "动作链断裂"
methods:
  - "先判型"
  - "分段函数积分"
  - "分段求原函数"
  - "分部积分"
  - "分段点连续检验"
  - "积分常数匹配"
  - "左右极限方程"
  - "排除法"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-138_分段原函数常数拼接不熟"
  - "MATHWIKI-ERROR-CLUSTER-213_思路知道但动作未落地"
  - "MATHWIKI-ERROR-CLUSTER-395_积分常数匹配遗漏"
  - "MATHWIKI-ERROR-CLUSTER-436_连续性条件未方程化"
  - "MATHWIKI-KNOWLEDGE-003_极限与连续"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-066_分段函数连续可导"
  - "MATHWIKI-KNOWLEDGE-116_分段函数积分"
  - "MATHWIKI-KNOWLEDGE-139_原函数"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-065_分段函数积分"
  - "MATHWIKI-METHOD-CLUSTER-309_分段点连续检验"
  - "MATHWIKI-METHOD-CLUSTER-380_排除法"
  - "MATHWIKI-METHOD-CLUSTER-441_积分常数匹配"
  - "MATHWIKI-METHOD-CLUSTER-672_分段求原函数"
  - "MATHWIKI-METHOD-CLUSTER-958_左右极限方程"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-079_分段积分变量角色与拼接链"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: 6ce830cbc6c565fa1aabe578ad555a96b97ba78fadd24d47baeec822367185f2
---

# GS-290 强化例题9.20(90116)分段原函数连续拼接

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-290_强化例题9.20(90116).md`
- wrongnet ID：`GS-290`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 不定积分 |
| 题型 | 分段函数求原函数：分段积分后连续性拼接常数 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 不定积分
- 原函数
- 分段函数连续可导
- 极限与连续
- 一元函数积分学的计算
- 分部积分
- 分段函数积分

### 错因

- 连续性条件未方程化
- 分段原函数常数拼接不熟
- 思路知道但动作未落地
- 积分常数匹配遗漏
- 条件检查遗漏
- 动作链断裂

### 方法

- 先判型
- 分段函数积分
- 分段求原函数
- 分部积分
- 分段点连续检验
- 积分常数匹配
- 左右极限方程
- 排除法

### 陷阱

- 原函数必连续
- 分段积分后必须保留 \(C_1,C_2\)
- 连续性不是口头判断，要写左右极限方程
- \(x=0\) 左段值为 \(C_1\)，右段值为 \(1+C_2\)
- \(C_1=1+C_2\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先分别写出 \(x\le0\) 与 \(x>0\) 两段原函数，并保留 \(C_1,C_2\)。 |
| missed_action | 没有把连续性落实为 \(F(0^-)=F(0^+)\)，因此没有得到 \(C_1=1+C_2\)。 |
| related_method_card_id | H03-005 |
| next_reminder | 分段原函数题：先分别积分，再在分段点代入左右表达式，令左右极限相等，不要只停留在“要连续”这句话。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-138_分段原函数常数拼接不熟]]
- [[MATHWIKI-ERROR-CLUSTER-213_思路知道但动作未落地]]
- [[MATHWIKI-ERROR-CLUSTER-395_积分常数匹配遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-436_连续性条件未方程化]]
- [[MATHWIKI-KNOWLEDGE-003_极限与连续]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-066_分段函数连续可导]]
- [[MATHWIKI-KNOWLEDGE-116_分段函数积分]]
- [[MATHWIKI-KNOWLEDGE-139_原函数]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-065_分段函数积分]]
- [[MATHWIKI-METHOD-CLUSTER-309_分段点连续检验]]
- [[MATHWIKI-METHOD-CLUSTER-380_排除法]]
- [[MATHWIKI-METHOD-CLUSTER-441_积分常数匹配]]
- [[MATHWIKI-METHOD-CLUSTER-672_分段求原函数]]
- [[MATHWIKI-METHOD-CLUSTER-958_左右极限方程]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-079_分段积分变量角色与拼接链]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
