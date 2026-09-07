---
wiki_id: SRC-WQ-GS-266
type: source_summary
title: "GS-266 强化例题9.1 2026.5.7"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-266_强化例题9.12026.5.7.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-266"
knowledge:
  - "一元函数积分学的计算"
  - "不定积分"
  - "有理函数积分"
  - "分子线性拆分"
  - "反正切型积分"
error_causes:
  - "反正切型识别断点"
  - "分母导数识别断点"
methods:
  - "有理函数积分"
  - "分母配方"
  - "分母导数拆分"
  - "分子线性拆分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-068_分母导数识别断点"
  - "MATHWIKI-ERROR-CLUSTER-073_反正切型识别断点"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-044_有理函数积分"
  - "MATHWIKI-KNOWLEDGE-082_反正切型积分"
  - "MATHWIKI-KNOWLEDGE-234_分子线性拆分"
  - "MATHWIKI-METHOD-CLUSTER-072_有理函数积分"
  - "MATHWIKI-METHOD-CLUSTER-200_分子线性拆分"
  - "MATHWIKI-METHOD-CLUSTER-677_分母导数拆分"
  - "MATHWIKI-METHOD-CLUSTER-683_分母配方"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-266 强化例题9.1 2026.5.7

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-266_强化例题9.12026.5.7.md`
- wrongnet ID：`GS-266`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学的计算 |
| 题型 | 有理函数不定积分 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数积分学的计算
- 不定积分
- 有理函数积分
- 分子线性拆分
- 反正切型积分

### 错因

- 反正切型识别断点
- 分母导数识别断点

### 方法

- 有理函数积分
- 分母配方
- 分母导数拆分
- 分子线性拆分

### 陷阱

- 配方后识别反正切
- 分子拆成分母导数项加常数项

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先把分母记为 \(D=x^2+2x+2\)，写出 \(D'=2x+2\)，并将 \(x\) 拆成 \(\frac12(2x+2)-1\) |
| missed_action | 没有在拆出对数项后继续把 \((x+1)^2+1\) 识别为反正切标准型 |
| related_method_card_id | H09-001 |
| next_reminder | 看到一次式除以二次式，先找分母导数并拆分子；剩下 \((x+a)^2+b^2\) 型时立即接反正切。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-068_分母导数识别断点]]
- [[MATHWIKI-ERROR-CLUSTER-073_反正切型识别断点]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-044_有理函数积分]]
- [[MATHWIKI-KNOWLEDGE-082_反正切型积分]]
- [[MATHWIKI-KNOWLEDGE-234_分子线性拆分]]
- [[MATHWIKI-METHOD-CLUSTER-072_有理函数积分]]
- [[MATHWIKI-METHOD-CLUSTER-200_分子线性拆分]]
- [[MATHWIKI-METHOD-CLUSTER-677_分母导数拆分]]
- [[MATHWIKI-METHOD-CLUSTER-683_分母配方]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-604

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
