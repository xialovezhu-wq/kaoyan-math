---
wiki_id: SRC-WQ-GS-626
type: source_summary
title: "GS-626 102369 可微定义线性主部"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-626_102369可微定义线性主部.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-626"
knowledge:
  - "多元函数偏导"
  - "全微分"
  - "多元函数连续可微"
  - "可微定义"
  - "一阶线性主部"
  - "空间曲面切平面与法线"
error_causes:
  - "定义触发缺失"
  - "可微定义遗忘"
  - "线性主部识别断点"
  - "小o结构识别不敏感"
  - "方法论调取失败"
methods:
  - "可微定义"
  - "一阶线性主部"
  - "点积展开"
  - "凑Δz-dz"
  - "小o误差项"
  - "显式曲面法向量"
  - "切平面一阶近似"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-007_方法论调取失败"
  - "MATHWIKI-ERROR-CLUSTER-052_定义触发缺失"
  - "MATHWIKI-ERROR-CLUSTER-053_小o结构识别不敏感"
  - "MATHWIKI-ERROR-CLUSTER-074_可微定义遗忘"
  - "MATHWIKI-ERROR-CLUSTER-092_线性主部识别断点"
  - "MATHWIKI-KNOWLEDGE-012_多元函数偏导"
  - "MATHWIKI-KNOWLEDGE-037_多元函数连续可微"
  - "MATHWIKI-KNOWLEDGE-072_可微定义"
  - "MATHWIKI-KNOWLEDGE-088_全微分"
  - "MATHWIKI-KNOWLEDGE-189_一阶线性主部"
  - "MATHWIKI-KNOWLEDGE-266_空间曲面切平面与法线"
  - "MATHWIKI-METHOD-CLUSTER-041_可微定义"
  - "MATHWIKI-METHOD-CLUSTER-1072_显式曲面法向量"
  - "MATHWIKI-METHOD-CLUSTER-137_一阶线性主部"
  - "MATHWIKI-METHOD-CLUSTER-242_点积展开"
  - "MATHWIKI-METHOD-CLUSTER-299_凑Δz-dz"
  - "MATHWIKI-METHOD-CLUSTER-360_小o误差项"
  - "MATHWIKI-METHOD-CLUSTER-689_切平面一阶近似"
  - "MATHWIKI-GS-METHOD-050_二元函数性质定义判别链"
  - "MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线"
status: indexed
last_updated: 2026-07-15
---

# GS-626 102369 可微定义线性主部

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-626_102369可微定义线性主部.md`
- wrongnet ID：`GS-626`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数微分学 |
| 题型 | 多元函数可微定义反用极限 / 一阶线性主部识别 / 显式曲面法向量点积 |
| 日期 | 2026-06-25 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 多元函数偏导
- 全微分
- 多元函数连续可微
- 可微定义
- 一阶线性主部
- 空间曲面切平面与法线

### 错因

- 定义触发缺失
- 可微定义遗忘
- 线性主部识别断点
- 小o结构识别不敏感
- 方法论调取失败

### 方法

- 可微定义
- 一阶线性主部
- 点积展开
- 凑Δz-dz
- 小o误差项
- 显式曲面法向量
- 切平面一阶近似

### 陷阱

- 可微定义误差项
- 线性主部反向识别
- 小o除以rho
- f(0,0)补项
- \(\mathbf n=(f_x(0,0),f_y(0,0),-1)\) 点乘后是线性主部减真实增量

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先展开 \(\mathbf n\cdot(x,y,f(x,y))\)，再补上 \(f(0,0)=0\)，凑出 \(-(\Delta z-dz)\)。 |
| missed_action | 没有把分子识别成可微定义中的误差项的相反数。 |
| related_method_card_id | H17-005 |
| next_reminder | 看到可微题里有 \(\sqrt{x^2+y^2}\) 作分母，先想 \(\rho\)；看到 \(f_xx+f_yy-f\)，先反向凑 \(\Delta z-dz\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-007_方法论调取失败]]
- [[MATHWIKI-ERROR-CLUSTER-052_定义触发缺失]]
- [[MATHWIKI-ERROR-CLUSTER-053_小o结构识别不敏感]]
- [[MATHWIKI-ERROR-CLUSTER-074_可微定义遗忘]]
- [[MATHWIKI-ERROR-CLUSTER-092_线性主部识别断点]]
- [[MATHWIKI-KNOWLEDGE-012_多元函数偏导]]
- [[MATHWIKI-KNOWLEDGE-037_多元函数连续可微]]
- [[MATHWIKI-KNOWLEDGE-072_可微定义]]
- [[MATHWIKI-KNOWLEDGE-088_全微分]]
- [[MATHWIKI-KNOWLEDGE-189_一阶线性主部]]
- [[MATHWIKI-KNOWLEDGE-266_空间曲面切平面与法线]]
- [[MATHWIKI-METHOD-CLUSTER-041_可微定义]]
- [[MATHWIKI-METHOD-CLUSTER-1072_显式曲面法向量]]
- [[MATHWIKI-METHOD-CLUSTER-137_一阶线性主部]]
- [[MATHWIKI-METHOD-CLUSTER-242_点积展开]]
- [[MATHWIKI-METHOD-CLUSTER-299_凑Δz-dz]]
- [[MATHWIKI-METHOD-CLUSTER-360_小o误差项]]
- [[MATHWIKI-METHOD-CLUSTER-689_切平面一阶近似]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-050_二元函数性质定义判别链]]
- [[MATHWIKI-GS-TOPIC-010_多元函数与二重积分错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-350
- GS-364
- GS-358

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
