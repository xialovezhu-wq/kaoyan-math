---
wiki_id: SRC-WQ-GS-696
type: source_summary
title: GS-696 194411 瑕点共同截断与主部抵消
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-696_194411瑕点共同截断与主部抵消.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-696_194411瑕点共同截断与主部抵消.md
visual_ids:
- VIS-GS-696
wrongnet_refs:
- GS-696
knowledge:
- 反常积分
- 反常积分极限
- 等价无穷小
- 洛必达法则
error_causes:
- 条件忽略
- 题型识别失败
- 反常积分极限收口遗漏
- 原函数拆项后未重新合并
- 过程跳步
methods:
- 先判型
- 找反常点
- 反常积分极限
- 牛顿莱布尼茨公式
- 原函数整体取极限
- 等价无穷小
- 洛必达法则
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-004
- MATHWIKI-ERROR-CLUSTER-002
- MATHWIKI-ERROR-CLUSTER-003
- MATHWIKI-ERROR-CLUSTER-005
- MATHWIKI-ERROR-CLUSTER-153
- MATHWIKI-ERROR-CLUSTER-165
- MATHWIKI-KNOWLEDGE-004
- MATHWIKI-KNOWLEDGE-028
- MATHWIKI-KNOWLEDGE-045
- MATHWIKI-KNOWLEDGE-110
- MATHWIKI-METHOD-CLUSTER-001
- MATHWIKI-METHOD-CLUSTER-026
- MATHWIKI-METHOD-CLUSTER-049
- MATHWIKI-METHOD-CLUSTER-057
- MATHWIKI-METHOD-CLUSTER-099
- MATHWIKI-METHOD-CLUSTER-229
- MATHWIKI-METHOD-CLUSTER-744
- MATHWIKI-GS-METHOD-011_B5-CHECK检查断点
- MATHWIKI-GS-METHOD-012_等价无穷小使用条件
- MATHWIKI-GS-METHOD-074_积分计算符号与边界项复查链
- MATHWIKI-GS-TOPIC-004_极限与连续错题总线
- MATHWIKI-GS-TOPIC-006_定积分错题总线
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
formal_projection_sha256: 91d664e3893ab02d3d33911c57287548c6e05f97c7632982cbf11f257ac1b11e
last_updated: '2026-07-18'
---
# GS-696 194411 瑕点共同截断与主部抵消

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-696_194411瑕点共同截断与主部抵消.md`
- wrongnet ID：`GS-696`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-696_194411瑕点共同截断与主部抵消|VIS-GS-696]]
- [Codex/Obsidian 本地桥接](http://127.0.0.1:8765/open/GS-696)

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 反常积分 |
| 题型 | 有限瑕点反常积分的共同截断与发散主部抵消 |
| 日期 | 2026-07-15 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 反常积分
- 反常积分极限
- 等价无穷小
- 洛必达法则

### 错因

- 条件忽略
- 题型识别失败
- 反常积分极限收口遗漏
- 原函数拆项后未重新合并
- 过程跳步

### 方法

- 先判型
- 找反常点
- 反常积分极限
- 牛顿莱布尼茨公式
- 原函数整体取极限
- 等价无穷小
- 洛必达法则

### 陷阱

- 下端点ln1为0
- x等于1是瑕点
- 原函数中单项发散不代表整体极限发散
- 两个发散项差值必须在同一截断下整体取极限

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 先检查 x=1 是否让分母失效，标为瑕点；对完整被积函数引入同一个下限截断 a→1+，在 [a,2] 上求原函数并合并后，再取联合极限。 |
| missed_action | 没有检查下限 x=1 的瑕点条件，直接把被积函数拆为两个分别发散的反常积分，并把未定义的下限项当作普通端点代入。 |
| related_method_card_id | H08-005 |
| next_reminder | 看到积分端点让分母为 0，先标瑕点并给整个被积函数设置同一个截断，再合并原函数取极限。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004]]
- [[MATHWIKI-ERROR-CLUSTER-002]]
- [[MATHWIKI-ERROR-CLUSTER-003]]
- [[MATHWIKI-ERROR-CLUSTER-005]]
- [[MATHWIKI-ERROR-CLUSTER-153]]
- [[MATHWIKI-ERROR-CLUSTER-165]]
- [[MATHWIKI-KNOWLEDGE-004]]
- [[MATHWIKI-KNOWLEDGE-028]]
- [[MATHWIKI-KNOWLEDGE-045]]
- [[MATHWIKI-KNOWLEDGE-110]]
- [[MATHWIKI-METHOD-CLUSTER-001]]
- [[MATHWIKI-METHOD-CLUSTER-026]]
- [[MATHWIKI-METHOD-CLUSTER-049]]
- [[MATHWIKI-METHOD-CLUSTER-057]]
- [[MATHWIKI-METHOD-CLUSTER-099]]
- [[MATHWIKI-METHOD-CLUSTER-229]]
- [[MATHWIKI-METHOD-CLUSTER-744]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-011_B5-CHECK检查断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-METHOD-074_积分计算符号与边界项复查链]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-675
- GS-687

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
