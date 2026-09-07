---
wiki_id: SRC-WQ-GS-274
type: source_summary
title: "GS-274 1000题B组9.18（84341）"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-274_1000题B组9.18（84341）.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-274"
knowledge:
  - "定积分"
  - "含参积分"
  - "广义积分"
  - "Gamma型积分"
  - "对数幂积分"
error_causes:
  - "暂无明确个人错因（视觉证据仅支持复做入口）"
methods:
  - "公式识别"
  - "指数换元"
  - "分部递推"
  - "Gamma积分"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-222_Gamma型积分"
  - "MATHWIKI-KNOWLEDGE-246_含参积分"
  - "MATHWIKI-KNOWLEDGE-249_对数幂积分"
  - "MATHWIKI-KNOWLEDGE-360_广义积分"
  - "MATHWIKI-METHOD-CLUSTER-160_指数换元"
  - "MATHWIKI-METHOD-CLUSTER-480_Gamma积分"
  - "MATHWIKI-METHOD-CLUSTER-631_公式识别"
  - "MATHWIKI-METHOD-CLUSTER-686_分部递推"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-274 1000题B组9.18（84341）

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-274_1000题B组9.18（84341）.md`
- wrongnet ID：`GS-274`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 含参数对数幂定积分 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 含参积分
- 广义积分
- Gamma型积分
- 对数幂积分

### 错因

- 暂无明确个人错因（视觉证据仅支持复做入口）

### 方法

- 公式识别
- 指数换元
- 分部递推
- Gamma积分

### 陷阱

- $\ln x$ 在区间内为负
- 符号有 $(-1)^n$
- 分母指数是 n+1
- 不要漏 n!

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先令 x=e^{-t}，把区间和 x^2 dx、ln^n x 全部改写成 t 积分 |
| missed_action | 旧卡未记录用户实际漏步；复做风险是没有把 [0,1] 上的对数幂积分转成指数衰减积分，导致符号和 n! 漏掉 |
| related_method_card_id | 待匹配 |
| next_reminder | 看到 [0,1] 上的 x^a ln^n x，先想 x=e^{-t}，再处理符号和 n!。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-016_暂无明确个人错因（视觉证据仅支持复做入口）]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-222_Gamma型积分]]
- [[MATHWIKI-KNOWLEDGE-246_含参积分]]
- [[MATHWIKI-KNOWLEDGE-249_对数幂积分]]
- [[MATHWIKI-KNOWLEDGE-360_广义积分]]
- [[MATHWIKI-METHOD-CLUSTER-160_指数换元]]
- [[MATHWIKI-METHOD-CLUSTER-480_Gamma积分]]
- [[MATHWIKI-METHOD-CLUSTER-631_公式识别]]
- [[MATHWIKI-METHOD-CLUSTER-686_分部递推]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-284

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
