---
wiki_id: SRC-WQ-GS-677
type: source_summary
title: "GS-677 81447 根式反常积分原函数"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-677_81447根式反常积分原函数.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-677"
knowledge:
  - "反常积分"
  - "反常积分极限"
  - "一元函数积分学的计算"
  - "不定积分"
  - "根式积分"
  - "对数型积分"
  - "参数分类讨论"
error_causes:
  - "方法选择错误"
  - "复习记忆不牢"
  - "题型识别失败"
  - "过程跳步"
methods:
  - "先判型"
  - "线性拆项"
  - "直接求原函数"
  - "根式积分公式"
  - "对数型原函数"
  - "反常积分极限"
  - "整体取极限"
  - "参数分类讨论"
  - "主导项比较"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-017_复习记忆不牢"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-028_反常积分"
  - "MATHWIKI-KNOWLEDGE-047_参数分类讨论"
  - "MATHWIKI-KNOWLEDGE-057_对数型积分"
  - "MATHWIKI-KNOWLEDGE-058_根式积分"
  - "MATHWIKI-KNOWLEDGE-110_反常积分极限"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-021_主导项比较"
  - "MATHWIKI-METHOD-CLUSTER-040_参数分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-057_反常积分极限"
  - "MATHWIKI-METHOD-CLUSTER-1050_整体取极限"
  - "MATHWIKI-METHOD-CLUSTER-1141_根式积分公式"
  - "MATHWIKI-METHOD-CLUSTER-1215_直接求原函数"
  - "MATHWIKI-METHOD-CLUSTER-1304_线性拆项"
  - "MATHWIKI-METHOD-CLUSTER-911_对数型原函数"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: 37fc3b31215860aefe598cd8687e050c43c5d12e371d7f4fc6381a4084be19ab
---

# GS-677 81447 根式反常积分原函数

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-677_81447根式反常积分原函数.md`
- wrongnet ID：`GS-677`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 反常积分 |
| 题型 | 含参反常积分计算与参数判敛 |
| 日期 | 2026-07-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 反常积分
- 反常积分极限
- 一元函数积分学的计算
- 不定积分
- 根式积分
- 对数型积分
- 参数分类讨论

### 错因

- 方法选择错误
- 复习记忆不牢
- 题型识别失败
- 过程跳步

### 方法

- 先判型
- 线性拆项
- 直接求原函数
- 根式积分公式
- 对数型原函数
- 反常积分极限
- 整体取极限
- 参数分类讨论
- 主导项比较

### 陷阱

- 通分后结构变复杂
- 根式积分公式遗忘
- 两个发散项差值要整体取极限
- 不能把无穷上限当普通端点代入
- a只在无穷远处决定收敛
- a等于1时对数发散项抵消
- a大于1或小于1都会发散

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把积分写成两个原函数项，分别写出 \(\ln(x+\sqrt{x^2+4})\) 和 \(a\ln(x+2)\)。 |
| missed_action | 先通分导致结构变复杂，并且忘记 \(\int dx/\sqrt{x^2+a^2}\) 的对数原函数公式。 |
| related_method_card_id | H09-001 |
| next_reminder | 看到反常积分中已有两项相减，先问每一项能不能直接求原函数；看到 \(1/\sqrt{x^2+a^2}\)，先写对数原函数，再整体取无穷上限极限。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-017_复习记忆不牢]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-028_反常积分]]
- [[MATHWIKI-KNOWLEDGE-047_参数分类讨论]]
- [[MATHWIKI-KNOWLEDGE-057_对数型积分]]
- [[MATHWIKI-KNOWLEDGE-058_根式积分]]
- [[MATHWIKI-KNOWLEDGE-110_反常积分极限]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-021_主导项比较]]
- [[MATHWIKI-METHOD-CLUSTER-040_参数分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-057_反常积分极限]]
- [[MATHWIKI-METHOD-CLUSTER-1050_整体取极限]]
- [[MATHWIKI-METHOD-CLUSTER-1141_根式积分公式]]
- [[MATHWIKI-METHOD-CLUSTER-1215_直接求原函数]]
- [[MATHWIKI-METHOD-CLUSTER-1304_线性拆项]]
- [[MATHWIKI-METHOD-CLUSTER-911_对数型原函数]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
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
