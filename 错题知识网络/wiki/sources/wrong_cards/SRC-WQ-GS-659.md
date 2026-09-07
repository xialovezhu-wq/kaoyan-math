---
wiki_id: SRC-WQ-GS-659
type: source_summary
title: GS-659 57841 截面三角形体积
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-659_57841截面三角形体积.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-659_57841截面三角形体积.md
visual_ids:
- VIS-GS-659
wrongnet_refs:
- GS-659
knowledge:
- 定积分
- 定积分应用
- 平面图形面积
- 微元法建模
- 面积微元
error_causes:
- 图像理解错误
- 题面语言翻译断点
- 题型识别失败
- 方法论调取失败
- 动作链断裂
- 空间立体构造理解断点
- 几何公式遗忘
methods:
- 先判型
- 几何应用变量选择
- 微元法建模
- 截面面积法
- 竖线法
- 上下函数相减
- 等边三角形面积公式
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-003
- MATHWIKI-ERROR-CLUSTER-003
- MATHWIKI-ERROR-CLUSTER-004
- MATHWIKI-ERROR-CLUSTER-007
- MATHWIKI-ERROR-CLUSTER-020
- MATHWIKI-ERROR-CLUSTER-043
- MATHWIKI-ERROR-CLUSTER-471
- MATHWIKI-ERROR-CLUSTER-472
- MATHWIKI-KNOWLEDGE-002
- MATHWIKI-KNOWLEDGE-035
- MATHWIKI-KNOWLEDGE-060
- MATHWIKI-KNOWLEDGE-253
- MATHWIKI-KNOWLEDGE-433
- MATHWIKI-METHOD-CLUSTER-001
- MATHWIKI-METHOD-CLUSTER-058
- MATHWIKI-METHOD-CLUSTER-155
- MATHWIKI-METHOD-CLUSTER-274
- MATHWIKI-METHOD-CLUSTER-443
- MATHWIKI-METHOD-CLUSTER-639
- MATHWIKI-METHOD-CLUSTER-1293
- MATHWIKI-GS-ERROR-005_题型识别失败
- MATHWIKI-GS-METHOD-096_截面面积积分求体积
status: indexed
formal_projection_sha256: 8813e82af533654e02814ef81b4849b2e96cc5f6544221f7b2c670233bf0965a
last_updated: '2026-08-28'
---
# GS-659 57841 截面三角形体积

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-659_57841截面三角形体积.md`
- wrongnet ID：`GS-659`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-659_57841截面三角形体积|VIS-GS-659]]
- [Codex/Obsidian 本地桥接](http://127.0.0.1:8765/open/GS-659)

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 定积分 |
| 题型 | 平行截面面积积分求体积 |
| 日期 | 2026-07-04 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 定积分
- 定积分应用
- 平面图形面积
- 微元法建模
- 面积微元

### 错因

- 图像理解错误
- 题面语言翻译断点
- 题型识别失败
- 方法论调取失败
- 动作链断裂
- 空间立体构造理解断点
- 几何公式遗忘

### 方法

- 先判型
- 几何应用变量选择
- 微元法建模
- 截面面积法
- 竖线法
- 上下函数相减
- 等边三角形面积公式

### 陷阱

- “垂直于 \(x\) 轴”表示固定 \(x\) 切片，不是沿 \(y\) 方向从上往下切。
- 底面竖线段只是在平面内确定边长；真正的截面是在三维空间中的等边三角形。
- \(A(x)\) 是第 \(x\) 处的截面面积，不是原平面底面面积。
- 题目不需要再单独给一个统一的 \(z\) 高度；“截面是等边三角形”已经使底面线段成为三角形边长，并由等边三角形几何关系唯一确定该截面的 \(z\) 向高度。
- 等边三角形边长为 \(a\) 时，高为 \(\frac{\sqrt3}{2}a\)，面积为 \(\frac{\sqrt3}{4}a^2\)。
- 在 \([-1,1]\) 内 \(y=0\) 在上，\(y=x^2-1\) 在下，所以边长为 \(0-(x^2-1)=1-x^2\)。
- 积分求体积时累加的是截面面积：\(V=\int A(x)\,dx\)，不是直接累加底面线段长度。

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先固定一个 \(x\)，在底面中画出从 \((x,x^2-1)\) 到 \((x,0)\) 的竖线段，并写出边长 \(a(x)=0-(x^2-1)=1-x^2\)。 |
| missed_action | 没有把“垂直于 \(x\) 轴”翻译成固定 \(x\) 的切片；也没有先求该切片在底面上的线段长度，导致不理解 \(A(x)\) 和体积积分。 |
| related_method_card_id | H10-007 |
| next_reminder | 看到“垂直于某轴的截面形状已知”，先固定该轴变量，求底面线段作为截面尺寸，再写 \(A(x)\) 并积分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003]]
- [[MATHWIKI-ERROR-CLUSTER-003]]
- [[MATHWIKI-ERROR-CLUSTER-004]]
- [[MATHWIKI-ERROR-CLUSTER-007]]
- [[MATHWIKI-ERROR-CLUSTER-020]]
- [[MATHWIKI-ERROR-CLUSTER-043]]
- [[MATHWIKI-ERROR-CLUSTER-471]]
- [[MATHWIKI-ERROR-CLUSTER-472]]
- [[MATHWIKI-KNOWLEDGE-002]]
- [[MATHWIKI-KNOWLEDGE-035]]
- [[MATHWIKI-KNOWLEDGE-060]]
- [[MATHWIKI-KNOWLEDGE-253]]
- [[MATHWIKI-KNOWLEDGE-433]]
- [[MATHWIKI-METHOD-CLUSTER-001]]
- [[MATHWIKI-METHOD-CLUSTER-058]]
- [[MATHWIKI-METHOD-CLUSTER-155]]
- [[MATHWIKI-METHOD-CLUSTER-274]]
- [[MATHWIKI-METHOD-CLUSTER-443]]
- [[MATHWIKI-METHOD-CLUSTER-639]]
- [[MATHWIKI-METHOD-CLUSTER-1293]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-096_截面面积积分求体积]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-643
- GS-666
- GS-668

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
