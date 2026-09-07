---
wiki_id: SRC-WQ-GS-616
type: source_summary
title: "GS-616 138808 余弦系数小角极限 2026.6.23"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-616_138808余弦系数小角极限.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-616"
knowledge:
  - "无穷级数"
  - "傅里叶级数"
  - "傅里叶系数"
  - "余弦级数"
  - "半区间余弦展开"
  - "周期偶延拓"
  - "等价无穷小"
  - "正弦等价无穷小"
error_causes:
  - "方法入口未触发"
  - "傅里叶系数公式调用不熟"
  - "题型识别失败"
  - "方法选择错误"
  - "过程跳步"
methods:
  - "先判型"
  - "半区间余弦展开识别"
  - "傅里叶展开对象识别"
  - "余弦级数系数公式"
  - "分部积分"
  - "奇数项提取"
  - "小角等价"
  - "有理函数极限"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-001_B3-METHOD"
  - "MATHWIKI-ERROR-CLUSTER-001_方法选择错误"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-003_题型识别失败"
  - "MATHWIKI-ERROR-CLUSTER-080_方法入口未触发"
  - "MATHWIKI-ERROR-CLUSTER-118_傅里叶系数公式调用不熟"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-005_无穷级数"
  - "MATHWIKI-KNOWLEDGE-136_傅里叶级数"
  - "MATHWIKI-KNOWLEDGE-155_正弦等价无穷小"
  - "MATHWIKI-KNOWLEDGE-163_余弦级数"
  - "MATHWIKI-KNOWLEDGE-164_傅里叶系数"
  - "MATHWIKI-KNOWLEDGE-201_周期偶延拓"
  - "MATHWIKI-KNOWLEDGE-238_半区间余弦展开"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-1089_有理函数极限"
  - "MATHWIKI-METHOD-CLUSTER-193_傅里叶展开对象识别"
  - "MATHWIKI-METHOD-CLUSTER-290_余弦级数系数公式"
  - "MATHWIKI-METHOD-CLUSTER-323_半区间余弦展开识别"
  - "MATHWIKI-METHOD-CLUSTER-361_小角等价"
  - "MATHWIKI-METHOD-CLUSTER-884_奇数项提取"
  - "MATHWIKI-GS-ERROR-003_方法选择错误"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-ERROR-005_题型识别失败"
  - "MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-METHOD-068_傅里叶展开对象识别与点值求和"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-25
related_wrongnet_refs: []
formal_projection_sha256: f8dbdad565cd3cb4147b8cb5a584439e7f973edf68451b0f3eaf523da57571c4
---

# GS-616 138808 余弦系数小角极限 2026.6.23

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-616_138808余弦系数小角极限.md`
- wrongnet ID：`GS-616`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 无穷级数 |
| 题型 | 半区间余弦展开求系数后求极限 |
| 日期 | 2026-06-23 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 无穷级数
- 傅里叶级数
- 傅里叶系数
- 余弦级数
- 半区间余弦展开
- 周期偶延拓
- 等价无穷小
- 正弦等价无穷小

### 错因

- 方法入口未触发
- 傅里叶系数公式调用不熟
- 题型识别失败
- 方法选择错误
- 过程跳步

### 方法

- 先判型
- 半区间余弦展开识别
- 傅里叶展开对象识别
- 余弦级数系数公式
- 分部积分
- 奇数项提取
- 小角等价
- 有理函数极限

### 陷阱

- 不要先纠结公式来源
- 余弦展开直接写a_n公式
- 区间[0,pi]对应l=pi
- 只含cos项对应偶延拓
- 取a_2n-1时符号为负
- sin小量等价使用前先确认a_2n-1趋于0

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B3-METHOD |
| expected_first_action | 先写 \(a_n=\frac{2}{\pi}\int_0^\pi (x+1)\cos nx\,dx\) |
| missed_action | 没有按傅里叶余弦展开式的固定流程写出 \(a_n\)，把“理解公式来源”和“做题流程启动”混在一起，导致入口处卡住。 |
| related_method_card_id | H16-024 |
| next_reminder | 看到半区间余弦展开，第一动作就是写 \(a_n=\frac{2}{l}\int_0^l f(x)\cos\frac{n\pi x}{l}\,dx\)；本题 \(l=\pi\)，所以 \(a_n=\frac{2}{\pi}\int_0^\pi f(x)\cos nx\,dx\)。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-001_方法选择错误]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-003_题型识别失败]]
- [[MATHWIKI-ERROR-CLUSTER-080_方法入口未触发]]
- [[MATHWIKI-ERROR-CLUSTER-118_傅里叶系数公式调用不熟]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-136_傅里叶级数]]
- [[MATHWIKI-KNOWLEDGE-155_正弦等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-163_余弦级数]]
- [[MATHWIKI-KNOWLEDGE-164_傅里叶系数]]
- [[MATHWIKI-KNOWLEDGE-201_周期偶延拓]]
- [[MATHWIKI-KNOWLEDGE-238_半区间余弦展开]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-1089_有理函数极限]]
- [[MATHWIKI-METHOD-CLUSTER-193_傅里叶展开对象识别]]
- [[MATHWIKI-METHOD-CLUSTER-290_余弦级数系数公式]]
- [[MATHWIKI-METHOD-CLUSTER-323_半区间余弦展开识别]]
- [[MATHWIKI-METHOD-CLUSTER-361_小角等价]]
- [[MATHWIKI-METHOD-CLUSTER-884_奇数项提取]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-003_方法选择错误]]
- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-ERROR-005_题型识别失败]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-METHOD-068_傅里叶展开对象识别与点值求和]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-011_无穷级数与幂级数错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

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
