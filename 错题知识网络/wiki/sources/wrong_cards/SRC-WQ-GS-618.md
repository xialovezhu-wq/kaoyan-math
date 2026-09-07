---
wiki_id: SRC-WQ-GS-618
type: source_summary
title: "GS-618 57869-3 根式三角代换回代"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-618_57869-3根式三角代换回代.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-618"
knowledge:
  - "不定积分"
  - "一元函数积分学的计算"
  - "根式积分"
  - "第一类换元"
  - "第二类换元"
  - "根式换元"
  - "三角换元"
  - "整体凑微分"
  - "回代化简"
  - "反三角回代"
error_causes:
  - "换元后回代不彻底"
  - "反三角函数与三角函数复合化简断点"
  - "答案形式整理不到位"
  - "动作链断裂"
  - "结构整理断点"
methods:
  - "先判型"
  - "凑微分换元"
  - "第一类换元"
  - "第二类换元"
  - "三角换元"
  - "回代化简"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-008_B6-CLOSE"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-035_结构整理断点"
  - "MATHWIKI-ERROR-CLUSTER-161_反三角函数与三角函数复合化简断点"
  - "MATHWIKI-ERROR-CLUSTER-228_换元后回代不彻底"
  - "MATHWIKI-ERROR-CLUSTER-409_答案形式整理不到位"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-026_第一类换元"
  - "MATHWIKI-KNOWLEDGE-041_第二类换元"
  - "MATHWIKI-KNOWLEDGE-050_整体凑微分"
  - "MATHWIKI-KNOWLEDGE-058_根式积分"
  - "MATHWIKI-KNOWLEDGE-080_三角换元"
  - "MATHWIKI-KNOWLEDGE-103_根式换元"
  - "MATHWIKI-KNOWLEDGE-120_回代化简"
  - "MATHWIKI-KNOWLEDGE-322_反三角回代"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-020_第一类换元"
  - "MATHWIKI-METHOD-CLUSTER-028_三角换元"
  - "MATHWIKI-METHOD-CLUSTER-044_第二类换元"
  - "MATHWIKI-METHOD-CLUSTER-064_凑微分换元"
  - "MATHWIKI-METHOD-CLUSTER-070_回代化简"
  - "MATHWIKI-GS-METHOD-039_不定积分结构化化归入口"
  - "MATHWIKI-GS-METHOD-043_根式积分换元与回代链"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-268"
  - "GS-619"
formal_projection_sha256: 7fa1ca145fca56434f65f10e1e15400f36d6c1907f595a13d080c0f39b33b24a
---

# GS-618 57869-3 根式三角代换回代

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-618_57869-3根式三角代换回代.md`
- wrongnet ID：`GS-618`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 根式型不定积分：凑微分或三角代换回代化简 |
| 日期 | 2026-06-24 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 不定积分
- 一元函数积分学的计算
- 根式积分
- 第一类换元
- 第二类换元
- 根式换元
- 三角换元
- 整体凑微分
- 回代化简
- 反三角回代

### 错因

- 换元后回代不彻底
- 反三角函数与三角函数复合化简断点
- 答案形式整理不到位
- 动作链断裂
- 结构整理断点

### 方法

- 先判型
- 凑微分换元
- 第一类换元
- 第二类换元
- 三角换元
- 回代化简

### 陷阱

- \(\sqrt{1+x^2}\) 先查能否凑 \(d(1+x^2)\)
- \(x^3dx=x^2\cdot xdx\)
- \(d(1+x^2)=2xdx\)
- 三角代换不能停在 \(\sec(\arctan x)\)
- \(\tan t=x\Rightarrow \sec t=\sqrt{1+x^2}\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B6-CLOSE |
| expected_first_action | 先写 \(t=\arctan x\)，再由 \(\tan t=x\) 推出 \(\sec t=\sqrt{1+x^2}\)。 |
| missed_action | 没有把 \(\sec(\arctan x)\) 化简为 \(\sqrt{1+x^2}\)。 |
| related_method_card_id | H09-003 |
| next_reminder | 看到根式 \(1+x^2\) 并走三角代换，先由 \(\tan t=x\) 写出 \(\sec t=\sqrt{1+x^2}\)，再把所有三角函数回到 \(x\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-008_B6-CLOSE]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-035_结构整理断点]]
- [[MATHWIKI-ERROR-CLUSTER-161_反三角函数与三角函数复合化简断点]]
- [[MATHWIKI-ERROR-CLUSTER-228_换元后回代不彻底]]
- [[MATHWIKI-ERROR-CLUSTER-409_答案形式整理不到位]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-026_第一类换元]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-KNOWLEDGE-050_整体凑微分]]
- [[MATHWIKI-KNOWLEDGE-058_根式积分]]
- [[MATHWIKI-KNOWLEDGE-080_三角换元]]
- [[MATHWIKI-KNOWLEDGE-103_根式换元]]
- [[MATHWIKI-KNOWLEDGE-120_回代化简]]
- [[MATHWIKI-KNOWLEDGE-322_反三角回代]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-020_第一类换元]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-044_第二类换元]]
- [[MATHWIKI-METHOD-CLUSTER-064_凑微分换元]]
- [[MATHWIKI-METHOD-CLUSTER-070_回代化简]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-METHOD-043_根式积分换元与回代链]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-268
- GS-619

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
