---
wiki_id: SRC-WQ-GS-627
type: source_summary
title: GS-627 77447 两直线平行平面
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-627_77447两直线平行平面.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-627_77447.md
visual_ids:
- VIS-GS-627
wrongnet_refs:
- GS-627
knowledge:
- 向量代数与空间解析几何
- 空间直线与平面
- 空间平面方程
- 方向向量
- 法向量
- 叉乘
- 行列式
- 代数余子式
error_causes:
- 题面语言翻译断点
- 空间几何对象识别断点
- 平面方程条件不敏感
- 叉乘用途触发不足
- 方法论调取失败
- 平面一般式不熟
- 法向量与平面内方向关系不清
- 同一平面平行误推两直线平行
- 点乘判垂直不熟
- 叉乘定义与计算不熟
- 代数余子式符号遗漏
- 运算路径不稳
methods:
- 直线方程模板
- 平面点法式
- 方向向量提取
- 法向量构造
- 叉乘求法向量
- 条件转化
- 平面一般式
- 点乘判垂直
- 叉乘行列式展开
- 代数余子式符号检查
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-002
- MATHWIKI-ERROR-CLUSTER-007
- MATHWIKI-ERROR-CLUSTER-020
- MATHWIKI-ERROR-CLUSTER-028
- MATHWIKI-ERROR-CLUSTER-048
- MATHWIKI-ERROR-CLUSTER-072
- MATHWIKI-ERROR-CLUSTER-207
- MATHWIKI-ERROR-CLUSTER-465
- MATHWIKI-ERROR-CLUSTER-466
- MATHWIKI-ERROR-CLUSTER-467
- MATHWIKI-ERROR-CLUSTER-468
- MATHWIKI-ERROR-CLUSTER-469
- MATHWIKI-ERROR-CLUSTER-470
- MATHWIKI-KNOWLEDGE-023
- MATHWIKI-KNOWLEDGE-089
- MATHWIKI-KNOWLEDGE-127
- MATHWIKI-KNOWLEDGE-134
- MATHWIKI-KNOWLEDGE-157
- MATHWIKI-KNOWLEDGE-179
- MATHWIKI-KNOWLEDGE-198
- MATHWIKI-KNOWLEDGE-414
- MATHWIKI-METHOD-CLUSTER-002
- MATHWIKI-METHOD-CLUSTER-161
- MATHWIKI-METHOD-CLUSTER-170
- MATHWIKI-METHOD-CLUSTER-422
- MATHWIKI-METHOD-CLUSTER-765
- MATHWIKI-METHOD-CLUSTER-987
- MATHWIKI-METHOD-CLUSTER-1436
- MATHWIKI-METHOD-CLUSTER-1437
- MATHWIKI-METHOD-CLUSTER-1438
- MATHWIKI-METHOD-CLUSTER-1439
- MATHWIKI-GS-METHOD-045_空间解析几何对象判别链
- MATHWIKI-GS-TOPIC-012_空间解析几何错题总线
status: indexed
formal_projection_sha256: 480e02327d6053aa44f518242a1650fdd6eaffbc1c6f72858e957171047379bd
last_updated: '2026-07-26'
---
# GS-627 77447 两直线平行平面

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-627_77447两直线平行平面.md`
- wrongnet ID：`GS-627`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-627_77447|VIS-GS-627]]
- [Codex/Obsidian 本地桥接](http://127.0.0.1:8765/open/GS-627)

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 向量代数与空间解析几何 |
| 题型 | 空间平面方程：过原点且与两条空间直线平行 |
| 日期 | 2026-06-25 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 2 |

## 可编译信息

### 知识点

- 向量代数与空间解析几何
- 空间直线与平面
- 空间平面方程
- 方向向量
- 法向量
- 叉乘
- 行列式
- 代数余子式

### 错因

- 题面语言翻译断点
- 空间几何对象识别断点
- 平面方程条件不敏感
- 叉乘用途触发不足
- 方法论调取失败
- 平面一般式不熟
- 法向量与平面内方向关系不清
- 同一平面平行误推两直线平行
- 点乘判垂直不熟
- 叉乘定义与计算不熟
- 代数余子式符号遗漏
- 运算路径不稳

### 方法

- 直线方程模板
- 平面点法式
- 方向向量提取
- 法向量构造
- 叉乘求法向量
- 条件转化
- 平面一般式
- 点乘判垂直
- 叉乘行列式展开
- 代数余子式符号检查

### 陷阱

- 平面需要点和法向量
- 直线方向向量提取
- 两方向向量在平面内
- 叉乘顺序只差符号
- 过原点只确定平面一般式中的常数项为 0
- 两条直线都平行于同一平面不代表两直线彼此平行
- 平面法向量必须分别与两个平面内方向向量点乘为 0
- 叉乘的行列式写法不是矩阵乘法
- 按第一行展开叉乘行列式时符号为正负正，j 项必须带负号

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写 Ax+By+Cz+D=0，并由原点在平面上得到 D=0；随后标明还缺法向量 n=(A,B,C)。 |
| missed_action | 起初不知道平面一般式、法向量与平面内方向的垂直关系及点乘为 0 的含义，误把“都平行于同一平面”理解为“两直线彼此平行”，也不熟悉点乘和叉乘计算；经讲解后展开叉乘行列式时又漏掉 j 项代数余子式的负号。 |
| related_method_card_id | H00-007 |
| next_reminder | 看到求平面方程，先写“点 + 法向量”；若给两条平行于平面的直线，就令法向量分别与两个方向向量点乘为 0，并用叉乘求法向量；行列式按第一行展开后立即检查正负正及两个点乘是否为 0。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002]]
- [[MATHWIKI-ERROR-CLUSTER-007]]
- [[MATHWIKI-ERROR-CLUSTER-020]]
- [[MATHWIKI-ERROR-CLUSTER-028]]
- [[MATHWIKI-ERROR-CLUSTER-048]]
- [[MATHWIKI-ERROR-CLUSTER-072]]
- [[MATHWIKI-ERROR-CLUSTER-207]]
- [[MATHWIKI-ERROR-CLUSTER-465]]
- [[MATHWIKI-ERROR-CLUSTER-466]]
- [[MATHWIKI-ERROR-CLUSTER-467]]
- [[MATHWIKI-ERROR-CLUSTER-468]]
- [[MATHWIKI-ERROR-CLUSTER-469]]
- [[MATHWIKI-ERROR-CLUSTER-470]]
- [[MATHWIKI-KNOWLEDGE-023]]
- [[MATHWIKI-KNOWLEDGE-089]]
- [[MATHWIKI-KNOWLEDGE-127]]
- [[MATHWIKI-KNOWLEDGE-134]]
- [[MATHWIKI-KNOWLEDGE-157]]
- [[MATHWIKI-KNOWLEDGE-179]]
- [[MATHWIKI-KNOWLEDGE-198]]
- [[MATHWIKI-KNOWLEDGE-414]]
- [[MATHWIKI-METHOD-CLUSTER-002]]
- [[MATHWIKI-METHOD-CLUSTER-161]]
- [[MATHWIKI-METHOD-CLUSTER-170]]
- [[MATHWIKI-METHOD-CLUSTER-422]]
- [[MATHWIKI-METHOD-CLUSTER-765]]
- [[MATHWIKI-METHOD-CLUSTER-987]]
- [[MATHWIKI-METHOD-CLUSTER-1436]]
- [[MATHWIKI-METHOD-CLUSTER-1437]]
- [[MATHWIKI-METHOD-CLUSTER-1438]]
- [[MATHWIKI-METHOD-CLUSTER-1439]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-045_空间解析几何对象判别链]]
- [[MATHWIKI-GS-TOPIC-012_空间解析几何错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-628
- GS-629
- GS-645

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
