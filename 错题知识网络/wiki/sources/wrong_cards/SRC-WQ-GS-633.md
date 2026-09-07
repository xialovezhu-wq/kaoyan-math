---
wiki_id: SRC-WQ-GS-633
type: source_summary
title: "GS-633 58045-1 根式配方对称换元"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-633_58045-1根式配方对称换元.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-633"
knowledge:
  - "定积分"
  - "定积分性质"
  - "一元函数积分学的计算"
  - "根式积分"
  - "配方"
  - "第二类换元"
  - "三角换元"
  - "对称换元"
  - "奇偶性"
  - "华里士公式"
error_causes:
  - "定积分换元误用"
  - "换元后dx处理不完整"
  - "非单调换元检查遗漏"
  - "条件检查遗漏"
  - "触发信息遗漏"
  - "根号二次式配方触发失败"
  - "对称结构未识别"
  - "方法论调取失败"
methods:
  - "先判型"
  - "配方"
  - "第二类换元"
  - "三角换元"
  - "对称换元"
  - "奇偶性积分"
  - "华里士公式"
  - "降幂公式"
  - "定积分计算"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-004_B5-CHECK"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏"
  - "MATHWIKI-ERROR-CLUSTER-056_换元后dx处理不完整"
  - "MATHWIKI-ERROR-CLUSTER-192_定积分换元误用"
  - "MATHWIKI-ERROR-CLUSTER-198_对称结构未识别"
  - "MATHWIKI-ERROR-CLUSTER-371_根号二次式配方触发失败"
  - "MATHWIKI-ERROR-CLUSTER-447_非单调换元检查遗漏"
  - "MATHWIKI-KNOWLEDGE-002_定积分"
  - "MATHWIKI-KNOWLEDGE-007_定积分性质"
  - "MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算"
  - "MATHWIKI-KNOWLEDGE-041_第二类换元"
  - "MATHWIKI-KNOWLEDGE-058_根式积分"
  - "MATHWIKI-KNOWLEDGE-080_三角换元"
  - "MATHWIKI-KNOWLEDGE-111_对称换元"
  - "MATHWIKI-KNOWLEDGE-138_华里士公式"
  - "MATHWIKI-KNOWLEDGE-204_奇偶性"
  - "MATHWIKI-KNOWLEDGE-274_配方"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-028_三角换元"
  - "MATHWIKI-METHOD-CLUSTER-042_定积分计算"
  - "MATHWIKI-METHOD-CLUSTER-044_第二类换元"
  - "MATHWIKI-METHOD-CLUSTER-084_配方"
  - "MATHWIKI-METHOD-CLUSTER-095_对称换元"
  - "MATHWIKI-METHOD-CLUSTER-110_华里士公式"
  - "MATHWIKI-METHOD-CLUSTER-136_降幂公式"
  - "MATHWIKI-METHOD-CLUSTER-218_奇偶性积分"
  - "MATHWIKI-GS-CONCEPT-002_积分结构中心"
  - "MATHWIKI-GS-ERROR-002_只看局部不看整体"
  - "MATHWIKI-GS-METHOD-002_换元合法性三件套"
  - "MATHWIKI-GS-TOPIC-002_一元积分近期错题簇"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-GS-TRIGGER-002_积分先找中心与整体"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-292"
  - "GS-326"
formal_projection_sha256: c12676f0f65f806ccfc2ba9206d595840a73c696e6fd67b4f540717d8af8e352
---

# GS-633 58045-1 根式配方对称换元

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-633_58045-1根式配方对称换元.md`
- wrongnet ID：`GS-633`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 定积分：根号二次式配方 + 对称区间 + 三角换元 |
| 日期 | 2026-06-27 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 定积分
- 定积分性质
- 一元函数积分学的计算
- 根式积分
- 配方
- 第二类换元
- 三角换元
- 对称换元
- 奇偶性
- 华里士公式

### 错因

- 定积分换元误用
- 换元后dx处理不完整
- 非单调换元检查遗漏
- 条件检查遗漏
- 触发信息遗漏
- 根号二次式配方触发失败
- 对称结构未识别
- 方法论调取失败

### 方法

- 先判型
- 配方
- 第二类换元
- 三角换元
- 对称换元
- 奇偶性积分
- 华里士公式
- 降幂公式
- 定积分计算

### 陷阱

- 定积分换元必须同时换新变量、微分和上下限
- 上下限都变成同一点不代表原积分一定为 0
- \(t=2x-x^2\) 在 \([0,2]\) 上不是单调一一对应
- 原式中没有 \(dt=(2-2x)dx\) 对应的微分因子
- 根号二次式先配方看中心
- \([0,2]\) 关于 \(x=1\) 对称
- \(u^2\sqrt{1-u^2}\) 是偶函数

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先把 \(2x-x^2\) 配方成 \(1-(x-1)^2\)，再令 \(u=x-1\) 并把积分限换成 \([-1,1]\)。 |
| missed_action | 令 \(t=2x-x^2\) 后，只把上下限都换成 0，没有处理 \(dt=(2-2x)dx\)，也没有检查该换元在 \([0,2]\) 上不是单调一一对应。 |
| related_method_card_id | H09-003 |
| next_reminder | 遇到定积分换元，必须同时检查新变量、微分 \(dx\)、上下限；如果上下限变成同一点，还要反查是否真的出现了 \(dt\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-010_条件检查遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-056_换元后dx处理不完整]]
- [[MATHWIKI-ERROR-CLUSTER-192_定积分换元误用]]
- [[MATHWIKI-ERROR-CLUSTER-198_对称结构未识别]]
- [[MATHWIKI-ERROR-CLUSTER-371_根号二次式配方触发失败]]
- [[MATHWIKI-ERROR-CLUSTER-447_非单调换元检查遗漏]]
- [[MATHWIKI-KNOWLEDGE-002_定积分]]
- [[MATHWIKI-KNOWLEDGE-007_定积分性质]]
- [[MATHWIKI-KNOWLEDGE-022_一元函数积分学的计算]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-KNOWLEDGE-058_根式积分]]
- [[MATHWIKI-KNOWLEDGE-080_三角换元]]
- [[MATHWIKI-KNOWLEDGE-111_对称换元]]
- [[MATHWIKI-KNOWLEDGE-138_华里士公式]]
- [[MATHWIKI-KNOWLEDGE-204_奇偶性]]
- [[MATHWIKI-KNOWLEDGE-274_配方]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-028_三角换元]]
- [[MATHWIKI-METHOD-CLUSTER-042_定积分计算]]
- [[MATHWIKI-METHOD-CLUSTER-044_第二类换元]]
- [[MATHWIKI-METHOD-CLUSTER-084_配方]]
- [[MATHWIKI-METHOD-CLUSTER-095_对称换元]]
- [[MATHWIKI-METHOD-CLUSTER-110_华里士公式]]
- [[MATHWIKI-METHOD-CLUSTER-136_降幂公式]]
- [[MATHWIKI-METHOD-CLUSTER-218_奇偶性积分]]

### 深度编译页

- [[MATHWIKI-GS-CONCEPT-002_积分结构中心]]
- [[MATHWIKI-GS-ERROR-002_只看局部不看整体]]
- [[MATHWIKI-GS-METHOD-002_换元合法性三件套]]
- [[MATHWIKI-GS-TOPIC-002_一元积分近期错题簇]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-GS-TRIGGER-002_积分先找中心与整体]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-292
- GS-326

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
