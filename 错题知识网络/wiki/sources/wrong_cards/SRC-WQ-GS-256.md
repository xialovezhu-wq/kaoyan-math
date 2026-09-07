---
wiki_id: SRC-WQ-GS-256
type: source_summary
title: "GS-256 强化例题6.20"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-256_强化例题6.20.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-256"
knowledge:
  - "一元函数微分学应用"
  - "微分不等式证明"
  - "对数不等式"
  - "导数判单调"
  - "单调性与极值"
error_causes:
  - "旧批量导入未记录个人错因；依据题图/解析确认的可复做断点是没有先把乘积非负转成同号证明。"
methods:
  - "构造辅助函数"
  - "条件转化"
  - "导数判单调"
  - "再构造辅助函数"
  - "参数最小值判号"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-249_旧批量导入未记录个人错因-依据题图-解析确认的可复做断点是没有先把乘积非"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-091_导数判单调"
  - "MATHWIKI-KNOWLEDGE-146_微分不等式证明"
  - "MATHWIKI-KNOWLEDGE-174_对数不等式"
  - "MATHWIKI-METHOD-CLUSTER-002_条件转化"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-006_构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-197_再构造辅助函数"
  - "MATHWIKI-METHOD-CLUSTER-757_参数最小值判号"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-051_函数不等式导数判号链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs: []
formal_projection_sha256: e1b4f1f978fa9139d34b04521ef3b217c89d51a235d00d1e9d26cfa86de36436
---

# GS-256 强化例题6.20

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-256_强化例题6.20.md`
- wrongnet ID：`GS-256`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 对数不等式证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 微分不等式证明
- 对数不等式
- 导数判单调
- 单调性与极值

### 错因

- 旧批量导入未记录个人错因；依据题图/解析确认的可复做断点是没有先把乘积非负转成同号证明。

### 方法

- 构造辅助函数
- 条件转化
- 导数判单调
- 再构造辅助函数
- 参数最小值判号

### 陷阱

- \(\ln x\) 隐含 \(x>0\)
- 乘积非负先看两因子同号
- \(f'(x)\) 的分子含参数时要再构造 \(g(x)\) 判最小值
- \(k\ge\ln2-1\) 要用在 \(g(2)\ge0\)

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先设 \(f(x)=x-\ln^2x+2k\ln x-1\)，把目标转成证明 \(x-1\) 与 \(f(x)\) 同号。 |
| missed_action | 旧卡未保存用户当时动作；当前可确认的复做断点是没有先做同号转化，并继续构造 \(g(x)\) 判 \(f'(x)\)。 |
| related_method_card_id | H06-008 |
| next_reminder | 看到 \((x-a)f(x)\ge0\)，先证明 \(f(a)=0\)，再用导数判 \(f(x)\) 与 \(x-a\) 同号。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-249_旧批量导入未记录个人错因-依据题图-解析确认的可复做断点是没有先把乘积非]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-091_导数判单调]]
- [[MATHWIKI-KNOWLEDGE-146_微分不等式证明]]
- [[MATHWIKI-KNOWLEDGE-174_对数不等式]]
- [[MATHWIKI-METHOD-CLUSTER-002_条件转化]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-006_构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-197_再构造辅助函数]]
- [[MATHWIKI-METHOD-CLUSTER-757_参数最小值判号]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-051_函数不等式导数判号链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
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
