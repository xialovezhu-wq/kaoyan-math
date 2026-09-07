---
wiki_id: SRC-WQ-GS-642
type: source_summary
title: "GS-642 57792 闭区间最值判号"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-642_57792闭区间最值判号.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-642"
related_wrongnet_refs:
  - "GS-133"
  - "GS-638"
knowledge:
  - "一元函数微分学应用"
  - "变上限积分"
  - "单调性与极值"
  - "闭区间最值定理"
  - "定积分"
error_causes:
  - "动作链断裂"
  - "过程跳步"
  - "条件检查遗漏"
  - "计算失误"
  - "方法选择错误"
methods:
  - "变上限积分求导"
  - "导数判单调"
  - "驻点求解"
  - "二次式配方判号"
  - "函数值比较"
  - "标准化计算流程"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-014_计算失误"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-221_闭区间最值定理"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-011_标准化计算流程"
  - "MATHWIKI-METHOD-CLUSTER-015_变上限积分求导"
  - "MATHWIKI-METHOD-CLUSTER-086_驻点求解"
  - "MATHWIKI-METHOD-CLUSTER-090_函数值比较"
  - "MATHWIKI-METHOD-CLUSTER-554_二次式配方判号"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-069_分段函数极值候选点完整列举"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 38c2145efbe8e3d4960a4b30de1ebed0ae93e4d7873fce9ecbedf49b61c5b97f
---

# GS-642 57792 闭区间最值判号

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-642_57792闭区间最值判号.md`
- wrongnet ID：`GS-642`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 变上限积分函数在闭区间上的最大值与最小值 |
| 日期 | 2026-06-29 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 变上限积分
- 单调性与极值
- 闭区间最值定理
- 定积分

### 错因

- 动作链断裂
- 过程跳步
- 条件检查遗漏
- 计算失误
- 方法选择错误

### 方法

- 变上限积分求导
- 导数判单调
- 驻点求解
- 二次式配方判号
- 函数值比较
- 标准化计算流程

### 陷阱

- 二次式误配方
- 分母恒正判号
- 求导后直接看区间
- 极值点不等于全局最值点
- 闭区间端点必须比较
- 分数代入合并错误

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先求出 \(f'(x)\)，再用配方或判别式确认分母符号，并令分子为 0 找内部驻点。 |
| missed_action | 求导后没有先找驻点；把 \(x^2-x+1\) 误看成 \((x-1)^2-x\)，没有确认分母恒正；找到 \(x=\frac12\) 后没有比较 \(f(-1)\)、\(f(\frac12)\)、\(f(1)\)，并把 \(\frac14-\frac12+1\) 误算成 \(… |
| related_method_card_id | H05-006 |
| next_reminder | 看到闭区间最值，求导后先判分母符号并找驻点，再列端点值和驻点值统一比较；代入分数时先合并负项再加常数。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-221_闭区间最值定理]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-011_标准化计算流程]]
- [[MATHWIKI-METHOD-CLUSTER-015_变上限积分求导]]
- [[MATHWIKI-METHOD-CLUSTER-086_驻点求解]]
- [[MATHWIKI-METHOD-CLUSTER-090_函数值比较]]
- [[MATHWIKI-METHOD-CLUSTER-554_二次式配方判号]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-069_分段函数极值候选点完整列举]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-133
- GS-638

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
