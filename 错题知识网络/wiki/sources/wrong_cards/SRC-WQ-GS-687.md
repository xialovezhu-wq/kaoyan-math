---
wiki_id: SRC-WQ-GS-687
type: source_summary
title: "GS-687 170665 反常积分原函数整体收口"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-687_170665反常积分原函数整体收口.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-687"
knowledge:
  - "反常积分"
  - "分部积分"
  - "根式换元"
  - "反正切型积分"
  - "反三角函数主值"
  - "对数型积分"
  - "等价无穷小"
error_causes:
  - "动作链断裂"
  - "反常积分极限收口遗漏"
  - "原函数拆项后未重新合并"
  - "换元系数错误"
  - "反三角函数特殊值记忆错误"
  - "过程跳步"
methods:
  - "有限上限截断"
  - "牛顿莱布尼茨公式"
  - "原函数整体取极限"
  - "对数差合并"
  - "分部积分"
  - "定积分分部"
  - "根式换元"
  - "反正切型积分"
  - "等价无穷小"
  - "三联换元检查"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-002_B4-CHAIN"
  - "MATHWIKI-ERROR-CLUSTER-002_过程跳步"
  - "MATHWIKI-ERROR-CLUSTER-004_动作链断裂"
  - "MATHWIKI-ERROR-CLUSTER-153_原函数拆项后未重新合并"
  - "MATHWIKI-ERROR-CLUSTER-162_反三角函数特殊值记忆错误"
  - "MATHWIKI-ERROR-CLUSTER-165_反常积分极限收口遗漏"
  - "MATHWIKI-ERROR-CLUSTER-229_换元系数错误"
  - "MATHWIKI-KNOWLEDGE-004_等价无穷小"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-028_反常积分"
  - "MATHWIKI-KNOWLEDGE-057_对数型积分"
  - "MATHWIKI-KNOWLEDGE-082_反正切型积分"
  - "MATHWIKI-KNOWLEDGE-103_根式换元"
  - "MATHWIKI-KNOWLEDGE-170_反三角函数主值"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-026_等价无穷小"
  - "MATHWIKI-METHOD-CLUSTER-049_牛顿莱布尼茨公式"
  - "MATHWIKI-METHOD-CLUSTER-1092_有限上限截断"
  - "MATHWIKI-METHOD-CLUSTER-116_定积分分部"
  - "MATHWIKI-METHOD-CLUSTER-124_根式换元"
  - "MATHWIKI-METHOD-CLUSTER-149_反正切型积分"
  - "MATHWIKI-METHOD-CLUSTER-510_三联换元检查"
  - "MATHWIKI-METHOD-CLUSTER-744_原函数整体取极限"
  - "MATHWIKI-METHOD-CLUSTER-913_对数差合并"
  - "MATHWIKI-GS-ERROR-004_过程跳步"
  - "MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点"
  - "MATHWIKI-GS-METHOD-012_等价无穷小使用条件"
  - "MATHWIKI-GS-METHOD-074_积分计算符号与边界项复查链"
  - "MATHWIKI-GS-TOPIC-003_高频知识主线总览"
  - "MATHWIKI-GS-TOPIC-004_极限与连续错题总线"
  - "MATHWIKI-GS-TOPIC-006_定积分错题总线"
  - "MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口"
status: indexed
last_updated: 2026-07-15
---

# GS-687 170665 反常积分原函数整体收口

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-687_170665反常积分原函数整体收口.md`
- wrongnet ID：`GS-687`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 反常积分 |
| 题型 | 对数根式反常积分：分部积分、根式换元与原函数整体收口 |
| 日期 | 2026-07-10 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 3 |

## 可编译信息

### 知识点

- 反常积分
- 分部积分
- 根式换元
- 反正切型积分
- 反三角函数主值
- 对数型积分
- 等价无穷小

### 错因

- 动作链断裂
- 反常积分极限收口遗漏
- 原函数拆项后未重新合并
- 换元系数错误
- 反三角函数特殊值记忆错误
- 过程跳步

### 方法

- 有限上限截断
- 牛顿莱布尼茨公式
- 原函数整体取极限
- 对数差合并
- 分部积分
- 定积分分部
- 根式换元
- 反正切型积分
- 等价无穷小
- 三联换元检查

### 陷阱

- 无穷大不是可直接代入原函数的普通数值
- 原函数中单项发散不代表整体极限发散
- 两个发散项可能抵消，必须保留共同上限后合并
- 换元必须同时检查变量、微分和外部系数
- $\arctan1=\pi/4$，不是 $0$

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先写 $I=\lim_{b\to+\infty}\int_1^b f(x)\,dx=\lim_{b\to+\infty}[F(b)-F(1)]$，暂时不把 $+\infty$ 代入任何一个原函数单项。 |
| missed_action | 在 $2\sqrt{x}\ln(1+x)$ 这一单项处提前判断发散并停止，没有把它与 $-2\sqrt{x}\ln x$ 合成 $2\sqrt{x}\ln\frac{1+x}{x}$；随后换元漏掉一倍系数，并把 $\arctan1$ 的特殊值记错。 |
| related_method_card_id | H08-005 |
| next_reminder | 看到反常积分原函数里有单独发散项，先保留同一个有限上限并合并整个 $F(b)$，再取极限；换元后立即检查 $dx$、上下限、外部系数，反正切端点值单独核对。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-002_过程跳步]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-153_原函数拆项后未重新合并]]
- [[MATHWIKI-ERROR-CLUSTER-162_反三角函数特殊值记忆错误]]
- [[MATHWIKI-ERROR-CLUSTER-165_反常积分极限收口遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-229_换元系数错误]]
- [[MATHWIKI-KNOWLEDGE-004_等价无穷小]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-028_反常积分]]
- [[MATHWIKI-KNOWLEDGE-057_对数型积分]]
- [[MATHWIKI-KNOWLEDGE-082_反正切型积分]]
- [[MATHWIKI-KNOWLEDGE-103_根式换元]]
- [[MATHWIKI-KNOWLEDGE-170_反三角函数主值]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-026_等价无穷小]]
- [[MATHWIKI-METHOD-CLUSTER-049_牛顿莱布尼茨公式]]
- [[MATHWIKI-METHOD-CLUSTER-1092_有限上限截断]]
- [[MATHWIKI-METHOD-CLUSTER-116_定积分分部]]
- [[MATHWIKI-METHOD-CLUSTER-124_根式换元]]
- [[MATHWIKI-METHOD-CLUSTER-149_反正切型积分]]
- [[MATHWIKI-METHOD-CLUSTER-510_三联换元检查]]
- [[MATHWIKI-METHOD-CLUSTER-744_原函数整体取极限]]
- [[MATHWIKI-METHOD-CLUSTER-913_对数差合并]]

### 深度编译页

- [[MATHWIKI-GS-ERROR-004_过程跳步]]
- [[MATHWIKI-GS-METHOD-010_B4-CHAIN动作链断点]]
- [[MATHWIKI-GS-METHOD-012_等价无穷小使用条件]]
- [[MATHWIKI-GS-METHOD-074_积分计算符号与边界项复查链]]
- [[MATHWIKI-GS-TOPIC-003_高频知识主线总览]]
- [[MATHWIKI-GS-TOPIC-004_极限与连续错题总线]]
- [[MATHWIKI-GS-TOPIC-006_定积分错题总线]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-168
- GS-677
- GS-686
- GS-266
- GS-637

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
