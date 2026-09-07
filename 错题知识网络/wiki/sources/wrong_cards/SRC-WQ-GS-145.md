---
wiki_id: SRC-WQ-GS-145
type: source_summary
title: "GS-145 1000题B组5.13"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-145_1000题B组5.13.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-145"
related_wrongnet_refs:
  - "GS-125"
knowledge:
  - "一元函数微分学应用"
  - "变上限积分"
  - "隐函数求导"
  - "单调性与极值"
  - "隐函数实际定义域"
error_causes:
  - "计算失误"
  - "方法选择错误"
  - "条件忽略"
  - "概念混淆"
methods:
  - "变上限积分求导"
  - "隐函数求导"
  - "链式求导"
  - "导数判单调"
  - "分类讨论"
  - "积分函数值域检查"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-005_条件忽略"
  - "MATHWIKI-ERROR-CLUSTER-006_概念混淆"
  - "MATHWIKI-ERROR-CLUSTER-014_计算失误"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-008_变上限积分"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-078_隐函数求导"
  - "MATHWIKI-METHOD-CLUSTER-004_分类讨论"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-015_变上限积分求导"
  - "MATHWIKI-METHOD-CLUSTER-018_链式求导"
  - "MATHWIKI-METHOD-CLUSTER-054_隐函数求导"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: c3149d67192bb853b1c1577a3158243b0b9eb9fe760d612ea8695926206bade4
---

# GS-145 1000题B组5.13

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-145_1000题B组5.13.md`
- wrongnet ID：`GS-145`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数微分学应用 |
| 题型 | 积分方程确定隐函数极值 |
| 日期 | 2026-05-07 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 一元函数微分学应用
- 变上限积分
- 隐函数求导
- 单调性与极值
- 隐函数实际定义域

### 错因

- 计算失误
- 方法选择错误
- 条件忽略
- 概念混淆

### 方法

- 变上限积分求导
- 隐函数求导
- 链式求导
- 导数判单调
- 分类讨论
- 积分函数值域检查

### 陷阱

- 定义域
- 端点取值
- 端点不是驻点
- 漏因子
- 正负号

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先对两边求导，左边写成 \(e^{-y^2/2}y'\)，右边写出 \(\frac{\sqrt{x}-2}{3\sqrt{x}}\) 这个链式因子。 |
| missed_action | 右边 \((\sqrt{x}-2)^2\) 求导时漏掉 \(\sqrt{x}-2\) 因子，并误把端点 \(x=0\) 当作驻点。 |
| related_method_card_id | H04-008 |
| next_reminder | 看到积分方程求极值，先隐式求导得到 \(y'\)，再解 \(y'=0\) 并用两侧符号判断；端点不是内部驻点。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-005_条件忽略]]
- [[MATHWIKI-ERROR-CLUSTER-006_概念混淆]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-008_变上限积分]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-078_隐函数求导]]
- [[MATHWIKI-METHOD-CLUSTER-004_分类讨论]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-015_变上限积分求导]]
- [[MATHWIKI-METHOD-CLUSTER-018_链式求导]]
- [[MATHWIKI-METHOD-CLUSTER-054_隐函数求导]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-125

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
