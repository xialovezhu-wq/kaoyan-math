---
wiki_id: SRC-WQ-GS-486
type: source_summary
title: "GS-486 77954 方程根估计判敛"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-486_77954方程根估计判敛.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-486_77954-2026.5.21.md"
visual_ids:
  - "VIS-GS-486"
question_asset_refs:
  - "错题知识网络/assets/visual_wrong_questions/GS-486/question_01.png"
solution_asset_refs: []
reference_asset_refs: []
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
identity_peer_refs: []
wrongnet_refs:
  - "GS-486"
related_wrongnet_refs: []
knowledge:
  - "无穷级数"
  - "数项级数敛散性判别"
  - "正项级数敛散性判别"
  - "正项级数比较判别法"
  - "p级数"
  - "零点定理"
  - "一元函数微分学应用"
  - "方程根个数"
  - "单调性与极值"
error_causes:
  - "计算失误"
  - "方法选择错误"
  - "过程跳步"
methods:
  - "先判型"
  - "零点定理"
  - "导数判单调"
  - "方程根放缩"
  - "原方程反解"
  - "比较判别法"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-014_计算失误"
  - "MATHWIKI-KNOWLEDGE-001_一元函数微分学应用"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-011_单调性与极值"
  - "MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别"
  - "MATHWIKI-KNOWLEDGE-032_正项级数比较判别法"
  - "MATHWIKI-KNOWLEDGE-036_p级数"
  - "MATHWIKI-KNOWLEDGE-042_零点定理"
  - "MATHWIKI-KNOWLEDGE-259_方程根个数"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-005_导数判单调"
  - "MATHWIKI-METHOD-CLUSTER-012_比较判别法"
  - "MATHWIKI-METHOD-CLUSTER-039_零点定理"
  - "MATHWIKI-METHOD-CLUSTER-1058_方程根放缩"
  - "MATHWIKI-METHOD-CLUSTER-747_原方程反解"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
evidence_status: user_confirmed
question_surface_status: registered
aggregate_edge_policy: allow
status: indexed
last_updated: 2026-07-24
formal_projection_sha256: 9408ce75374dde04543c6f10102e71333681e99bdf2d9f027bfa55a1d6aff352
---

# GS-486 77954 方程根估计判敛

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-486_77954方程根估计判敛.md`
- wrongnet ID：`GS-486`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 视觉证据

- 详情页：[[错题知识网络/可视化错题详情/高等数学/GS-486_77954-2026.5.21|VIS-GS-486]]
- visual_id：`VIS-GS-486`
- 题图：`错题知识网络/assets/visual_wrong_questions/GS-486/question_01.png`
- 题图 1 张；解析图 0 张；参考图 0 张。

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 方程根估计与正项级数判敛 |
| 日期 | 2026-05-21 |
| 状态 | 待复做 |
| 优先级 | B |
| 难度 | 3 |

## 可编译信息

### 知识点

- 无穷级数
- 数项级数敛散性判别
- 正项级数敛散性判别
- 正项级数比较判别法
- p级数
- 零点定理
- 一元函数微分学应用
- 方程根个数
- 单调性与极值

### 错因

- 计算失误
- 方法选择错误
- 过程跳步

### 方法

- 先判型
- 零点定理
- 导数判单调
- 方程根放缩
- 原方程反解
- 比较判别法

### 陷阱

- 端点值计算
- 根的位置估计
- 方程根放缩
- p级数条件
- 比较对象选择

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先令 \(f_n(x)=x^n+nx-1\)，计算 \(f_n(0)=-1,\ f_n(1)=n>0\)，并用 \(f_n'(x)>0\) 定唯一正根 |
| missed_action | 没有先固定根所在区间和唯一性，后半段也没有从 \(x_n^n+nx_n-1=0\) 反解出 \(x_n<1/n\) |
| related_method_card_id | H16-001 |
| next_reminder | 看到“方程正根 \(x_n\)+判断 \(\sum f(x_n)\)”时，先定根区间和唯一性，再从原方程反解 \(x_n\) 的标准上界。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-014_计算失误]]
- [[MATHWIKI-KNOWLEDGE-001_一元函数微分学应用]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-011_单调性与极值]]
- [[MATHWIKI-KNOWLEDGE-013_数项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-029_正项级数敛散性判别]]
- [[MATHWIKI-KNOWLEDGE-032_正项级数比较判别法]]
- [[MATHWIKI-KNOWLEDGE-036_p级数]]
- [[MATHWIKI-KNOWLEDGE-042_零点定理]]
- [[MATHWIKI-KNOWLEDGE-259_方程根个数]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-005_导数判单调]]
- [[MATHWIKI-METHOD-CLUSTER-012_比较判别法]]
- [[MATHWIKI-METHOD-CLUSTER-039_零点定理]]
- [[MATHWIKI-METHOD-CLUSTER-1058_方程根放缩]]
- [[MATHWIKI-METHOD-CLUSTER-747_原方程反解]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-005_一元函数微分学应用错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- 暂无强边

## 证据边界

- 个人断点只认“零点定理端点值算错，且没有从原方程反解出正根上界”；未发现同时共享该方程根对象、端点定位与反解放缩第一动作，并有双端用户证据的卡片。
- 原有候选端点不保留为正式关系。

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
