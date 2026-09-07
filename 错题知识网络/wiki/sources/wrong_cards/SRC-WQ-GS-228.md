---
wiki_id: SRC-WQ-GS-228
type: source_summary
title: "GS-228 1000题B组6.6"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-228_1000题B组6.6.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-228"
knowledge:
  - "一元函数微分学应用"
  - "凹凸性与拐点"
  - "泰勒公式"
  - "拉格朗日中值定理"
error_causes:
  - "旧批量未记录个人原始错因；当前仅确认复做断点是看到 \\(f''\\ge0\\) 时没有先转成凸函数切线下界，进而用非零斜率导致一侧线性无界来反证，需用户复做确认。"
methods:
  - "凸函数切线估计"
  - "泰勒公式"
  - "反证法"
  - "有界性矛盾"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-342_旧批量未记录个人原始错因-当前仅确认复做断点是看到-f''-ge0-时没"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-015_泰勒公式"
  - "MATHWIKI-KNOWLEDGE-018_凹凸性与拐点"
  - "MATHWIKI-KNOWLEDGE-021_拉格朗日中值定理"
  - "MATHWIKI-METHOD-CLUSTER-079_反证法"
  - "MATHWIKI-METHOD-CLUSTER-1090_有界性矛盾"
  - "MATHWIKI-METHOD-CLUSTER-1168_泰勒公式"
  - "MATHWIKI-METHOD-CLUSTER-646_凸函数切线估计"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-228 1000题B组6.6

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-228_1000题B组6.6.md`
- wrongnet ID：`GS-228`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 凸函数切线不等式与有界性证明 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | C |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 凹凸性与拐点
- 泰勒公式
- 拉格朗日中值定理

### 错因

- 旧批量未记录个人原始错因；当前仅确认复做断点是看到 \(f''\ge0\) 时没有先转成凸函数切线下界，进而用非零斜率导致一侧线性无界来反证，需用户复做确认。

### 方法

- 凸函数切线估计
- 泰勒公式
- 反证法
- 有界性矛盾

### 陷阱

- 凸函数方向
- 整轴有界条件
- 非零斜率推出无界

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先由 \(f''\ge0\) 写出 \(f(x)\ge f(x_0)+f'(x_0)(x-x_0)\) |
| missed_action | 没有先把二阶导非负翻译成凸函数切线下界 |
| related_method_card_id | H05-004 |
| next_reminder | 看到 \(f''\ge0\)，先写凸函数切线下界；若再给整轴有界，就用非零斜率推出无界矛盾。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-342_旧批量未记录个人原始错因-当前仅确认复做断点是看到-f''-ge0-时没]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-015_泰勒公式]]
- [[MATHWIKI-KNOWLEDGE-018_凹凸性与拐点]]
- [[MATHWIKI-KNOWLEDGE-021_拉格朗日中值定理]]
- [[MATHWIKI-METHOD-CLUSTER-079_反证法]]
- [[MATHWIKI-METHOD-CLUSTER-1090_有界性矛盾]]
- [[MATHWIKI-METHOD-CLUSTER-1168_泰勒公式]]
- [[MATHWIKI-METHOD-CLUSTER-646_凸函数切线估计]]

### 深度编译页

- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]

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
