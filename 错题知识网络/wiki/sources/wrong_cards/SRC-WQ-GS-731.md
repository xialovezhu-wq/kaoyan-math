---
wiki_id: SRC-WQ-GS-731
type: source_summary
title: "GS-731 57902 偶周期函数线性权重积分"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-731_57902偶周期函数线性权重积分.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-731_57902偶周期函数线性权重积分.md"
visual_ids:
  - "VIS-GS-731"
wrongnet_refs:
  - "GS-731"
knowledge:
  - "周期函数定积分"
  - "偶函数"
  - "区间反射换元"
  - "线性权重配对"
  - "绝对值三角函数积分"
error_causes:
  - "区间对称入口未触发"
  - "周期性条件检查缺失"
  - "第一问结论迁移失败"
methods:
  - "区间再现"
  - "中点反射换元"
  - "原积分与反射积分相加"
  - "周期积分拆段"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS"
  - "MATHWIKI-ACTION-GAP-004"
  - "MATHWIKI-ERROR-CLUSTER-550"
  - "MATHWIKI-ERROR-CLUSTER-551"
  - "MATHWIKI-ERROR-CLUSTER-552"
  - "MATHWIKI-KNOWLEDGE-467"
  - "MATHWIKI-KNOWLEDGE-468"
  - "MATHWIKI-KNOWLEDGE-469"
  - "MATHWIKI-KNOWLEDGE-470"
  - "MATHWIKI-KNOWLEDGE-471"
  - "MATHWIKI-METHOD-CLUSTER-092"
  - "MATHWIKI-METHOD-CLUSTER-1511"
  - "MATHWIKI-METHOD-CLUSTER-1512"
  - "MATHWIKI-METHOD-CLUSTER-1513"
status: indexed
card_status: 已掌握
formal_projection_sha256: 6289aa865dc4a26b5007ea830cba0b18a022a02826157783c72e6cc25ad04f01
last_updated: "2026-08-28"
related_wrongnet_refs: []
---

# GS-731 57902 偶周期函数线性权重积分

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-731_57902偶周期函数线性权重积分.md`
- wrongnet ID：`GS-731`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-731_57902偶周期函数线性权重积分|VIS-GS-731]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-731_57902%E5%81%B6%E5%91%A8%E6%9C%9F%E5%87%BD%E6%95%B0%E7%BA%BF%E6%80%A7%E6%9D%83%E9%87%8D%E7%A7%AF%E5%88%86)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-731/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-731/solution_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 偶周期函数的区间反射与线性权重积分 |
| 日期 | 2026-07-28 |
| 状态 | 已掌握 |
| 优先级 | A |
| 难度 | 3 |

## 本次正式结论

- 当前错点：没有识别 $[0,nT]$ 的中心反射 $x\mapsto nT-x$ 能把线性权重 $x$ 变成互补权重 $nT-x$，再借周期性与偶性保持函数因子不变；并错误地把“周期函数乘以 $x$”仍当作周期函数。
- 最新错误证据：2026-07-28 第1次错：第一问知道周期函数有 $\int_0^{nT}f=n\int_0^Tf$，也尝试换元和分部积分，但没有把积分区间关于中点 $nT/2$ 反射，使原积分与反射后的积分相加消去线性权重。第二问又把 $x|\cos x|$ 整体误判为以 $\pi$ 为周期，写成 $n\int_0^\pi x|\cos x|dx$；没有检查乘上非周期因子 $x$ 后周期性已被破坏，也没有识别第一问正是为“线性权重乘偶周期函数”准备的结论。
- 最新掌握证据：2026-07-28 AI评分 2/5：知道 $|\cos x|$ 本身是偶函数且以 $\pi$ 为周期，也能完成最后单周期积分；区间反射入口与第二问调用第一问均需提示。讲解后计算无误，但尚未闭卷复写第一问。
- 2026-08-28 正式评分 5/5：实际交付后用户明确报告整题无提示独立做对；只确认 GS-731 本题，不外推到原锚点。

## 可编译信息

### 知识点

- 周期函数定积分
- 偶函数
- 区间反射换元
- 线性权重配对
- 绝对值三角函数积分

### 错因

- 区间对称入口未触发
- 周期性条件检查缺失
- 第一问结论迁移失败

### 方法

- 区间再现
- 中点反射换元
- 原积分与反射积分相加
- 周期积分拆段

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B5-CHECK |
| expected_first_action | 设 $I=\int_0^{nT}xf(x)dx$，再写同一区间反射式 $I=\int_0^{nT}(nT-x)f(nT-x)dx$。 |
| missed_action | 没有由整数周期区间想到中心反射；第二问未检查 $x|\cos x|$ 的整体周期性，也未把 $|\cos x|$ 识别为第一问中的 $f$。 |
| related_method_card_id | H11-003 |
| next_reminder | 看到 $x\times$ 偶周期函数且积分到 $nT$，先反射全区间；先检查谁真正有周期，线性权重通常没有。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-004_B5-CHECK]]
- [[MATHWIKI-ERROR-CLUSTER-550_区间对称入口未触发]]
- [[MATHWIKI-ERROR-CLUSTER-551_周期性条件检查缺失]]
- [[MATHWIKI-ERROR-CLUSTER-552_第一问结论迁移失败]]
- [[MATHWIKI-KNOWLEDGE-467_周期函数定积分]]
- [[MATHWIKI-KNOWLEDGE-468_偶函数]]
- [[MATHWIKI-KNOWLEDGE-469_区间反射换元]]
- [[MATHWIKI-KNOWLEDGE-470_线性权重配对]]
- [[MATHWIKI-KNOWLEDGE-471_绝对值三角函数积分]]
- [[MATHWIKI-METHOD-CLUSTER-092_区间再现]]
- [[MATHWIKI-METHOD-CLUSTER-1511_中点反射换元]]
- [[MATHWIKI-METHOD-CLUSTER-1512_原积分与反射积分相加]]
- [[MATHWIKI-METHOD-CLUSTER-1513_周期积分拆段]]

### 深度方法与专题

- 本批保持索引型编译；未新增深度专题关系。
