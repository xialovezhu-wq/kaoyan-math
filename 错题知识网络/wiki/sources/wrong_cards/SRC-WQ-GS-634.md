---
wiki_id: SRC-WQ-GS-634
type: source_summary
title: "GS-634 58045-2 平移后整体奇偶"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-634_58045-2平移后整体奇偶.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-634"
knowledge:
  - "定积分"
  - "定积分性质"
  - "一元函数积分学的计算"
  - "函数奇偶性"
  - "对称换元"
error_causes:
  - "动作链断裂"
  - "方法论调取失败"
  - "整体奇偶性判断对象错误"
  - "只看单项不看整体"
  - "整体结构未识别"
methods:
  - "先判型"
  - "区间平移"
  - "对称换元"
  - "奇偶性积分"
  - "整体函数奇偶性检查"
  - "直接计算f(-t)"
  - "定积分性质"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-174_只看单项不看整体"
  - "MATHWIKI-ERROR-CLUSTER-238_整体奇偶性判断对象错误"
  - "MATHWIKI-ERROR-CLUSTER-239_整体结构未识别"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-111_对称换元"
  - "MATHWIKI-KNOWLEDGE-165_函数奇偶性"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-078_区间平移"
  - "MATHWIKI-METHOD-CLUSTER-095_对称换元"
  - "MATHWIKI-METHOD-CLUSTER-1216_直接计算f-t"
  - "MATHWIKI-METHOD-CLUSTER-218_奇偶性积分"
  - "MATHWIKI-METHOD-CLUSTER-232_整体函数奇偶性检查"
  - "MATHWIKI-METHOD-CLUSTER-896_定积分性质"
  - "MATHWIKI-GS-CONCEPT-002_积分结构中心"
  - "MATHWIKI-GS-ERROR-002_只看局部不看整体"
  - "MATHWIKI-GS-METHOD-003_整体函数奇偶性检查"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-TOPIC-002_一元积分近期错题簇"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-GS-TRIGGER-002_积分先找中心与整体"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-272"
  - "GS-326"
  - "GS-633"
formal_projection_sha256: e4a70f33ead44f41da003b71d0af50da2cd6a22b140299a8e1074fbeabd5c462
---

# GS-634 58045-2 平移后整体奇偶

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-634_58045-2平移后整体奇偶.md`
- wrongnet ID：`GS-634`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 定积分：区间平移后整体奇偶性判断 |
| 日期 | 2026-06-27 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 一元函数积分学的计算
- 函数奇偶性
- 对称换元

### 错因

- 动作链断裂
- 方法论调取失败
- 整体奇偶性判断对象错误
- 只看单项不看整体
- 整体结构未识别

### 方法

- 先判型
- 区间平移
- 对称换元
- 奇偶性积分
- 整体函数奇偶性检查
- 直接计算f(-t)
- 定积分性质

### 陷阱

- 平移到对称区间后不要只看单项
- 先把整个被积函数设为 \(f(t)\)
- 直接计算 \(f(-t)\) 判断整体奇偶性
- \(A(t)-A(-t)\) 优先怀疑是奇函数
- 奇函数在对称区间上的积分为 0

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先令 \(t=x-\frac\pi2\)，把 \([0,\pi]\) 平移成 \([-\frac\pi2,\frac\pi2]\)。 |
| missed_action | 平移后没有把 \(e^{\sin t}-e^{-\sin t}\) 作为整体判断奇偶性，只孤立判断了 \(e^{\sin t}\)。 |
| related_method_card_id | H08-008 |
| next_reminder | 看到可平移为对称区间的定积分，先把整个被积函数设为 \(f(t)\)，再直接计算 \(f(-t)\)，不要只判断单项。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-174_只看单项不看整体]]
- [[MATHWIKI-ERROR-CLUSTER-238_整体奇偶性判断对象错误]]
- [[MATHWIKI-ERROR-CLUSTER-239_整体结构未识别]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-111_对称换元]]
- [[MATHWIKI-KNOWLEDGE-165_函数奇偶性]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-078_区间平移]]
- [[MATHWIKI-METHOD-CLUSTER-095_对称换元]]
- [[MATHWIKI-METHOD-CLUSTER-1216_直接计算f-t]]
- [[MATHWIKI-METHOD-CLUSTER-218_奇偶性积分]]
- [[MATHWIKI-METHOD-CLUSTER-232_整体函数奇偶性检查]]
- [[MATHWIKI-METHOD-CLUSTER-896_定积分性质]]

### 深度编译页

- [[MATHWIKI-GS-CONCEPT-002_积分结构中心]]
- [[MATHWIKI-GS-ERROR-002_只看局部不看整体]]
- [[MATHWIKI-GS-METHOD-003_整体函数奇偶性检查]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-TOPIC-002_一元积分近期错题簇]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-GS-TRIGGER-002_积分先找中心与整体]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-272
- GS-326
- GS-633

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
