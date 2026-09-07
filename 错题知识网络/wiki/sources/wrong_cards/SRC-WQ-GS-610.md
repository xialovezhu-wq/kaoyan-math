---
wiki_id: SRC-WQ-GS-610
type: source_summary
title: "GS-610 57869-2 根式整体换元分部积分"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-610_57869根式整体换元分部.md"
visual_detail_refs: []
visual_ids: []
wrongnet_refs:
  - "GS-610"
knowledge:
  - "不定积分"
  - "根式积分"
  - "根式整体换元"
  - "第二类换元"
  - "根式换元"
  - "分部积分"
  - "有理函数积分"
  - "反正切型积分"
error_causes:
  - "方法入口错误"
  - "触发信息遗漏"
  - "根式整体换元触发不足"
  - "根式非法拆分倾向"
  - "分部积分二次触发不稳定"
methods:
  - "先判型"
  - "第二类换元"
  - "根式整体换元"
  - "分部积分"
  - "补常数化简"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表"
  - "MATHWIKI-ACTION-GAP-003_B2-TRIGGER"
  - "MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏"
  - "MATHWIKI-ERROR-CLUSTER-087_根式整体换元触发不足"
  - "MATHWIKI-ERROR-CLUSTER-145_分部积分二次触发不稳定"
  - "MATHWIKI-ERROR-CLUSTER-240_方法入口错误"
  - "MATHWIKI-ERROR-CLUSTER-376_根式非法拆分倾向"
  - "MATHWIKI-KNOWLEDGE-020_不定积分"
  - "MATHWIKI-KNOWLEDGE-024_分部积分"
  - "MATHWIKI-KNOWLEDGE-041_第二类换元"
  - "MATHWIKI-KNOWLEDGE-044_有理函数积分"
  - "MATHWIKI-KNOWLEDGE-058_根式积分"
  - "MATHWIKI-KNOWLEDGE-082_反正切型积分"
  - "MATHWIKI-KNOWLEDGE-103_根式换元"
  - "MATHWIKI-KNOWLEDGE-125_根式整体换元"
  - "MATHWIKI-METHOD-CLUSTER-001_先判型"
  - "MATHWIKI-METHOD-CLUSTER-007_分部积分"
  - "MATHWIKI-METHOD-CLUSTER-044_第二类换元"
  - "MATHWIKI-METHOD-CLUSTER-1331_补常数化简"
  - "MATHWIKI-METHOD-CLUSTER-166_根式整体换元"
  - "MATHWIKI-GS-METHOD-039_不定积分结构化化归入口"
  - "MATHWIKI-GS-METHOD-043_根式积分换元与回代链"
  - "MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线"
status: indexed
last_updated: 2026-07-24
related_wrongnet_refs:
  - "GS-270"
  - "GS-275"
  - "GS-609"
formal_projection_sha256: 2ece1121c0263fe71ca103e91dde21445d8f6a4c12c6c9aeeef7c65072bb3887
---

# GS-610 57869-2 根式整体换元分部积分

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-610_57869根式整体换元分部.md`
- wrongnet ID：`GS-610`
- 角色：raw source 的轻量 source summary，不替代正式错题卡。

## 可视化入口

- 暂无已确认可视化详情
- Codex/Obsidian 本地桥接：暂无已确认视觉映射

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 一元函数积分学 |
| 题型 | 根式复合结构第二类换元 + 对数函数分部积分 |
| 日期 | 2026-06-16 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 待确认 |

## 可编译信息

### 知识点

- 不定积分
- 根式积分
- 根式整体换元
- 第二类换元
- 根式换元
- 分部积分
- 有理函数积分
- 反正切型积分

### 错因

- 方法入口错误
- 触发信息遗漏
- 根式整体换元触发不足
- 根式非法拆分倾向
- 分部积分二次触发不稳定

### 方法

- 先判型
- 第二类换元
- 根式整体换元
- 分部积分
- 补常数化简

### 陷阱

- \(\sqrt{e^x-1}\) 是整体换元对象，不要拆
- \(\sqrt{a-b}\ne\sqrt a-\sqrt b\)
- \(\frac1{\sqrt{e^x-1}}\) 不能拆成两项分别积分
- 换元成功标准：根式、指数项、\(dx\) 能一起抵消
- \(\frac{t^2}{1+t^2}=1-\frac1{1+t^2}\) 补常数
- 换元后出现 \(\ln(1+t^2)\) 要继续分部积分

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B2-TRIGGER |
| expected_first_action | 先令 \(t=\sqrt{e^x-1}\)，并同步写出 \(e^x=t^2+1,\ x=\ln(1+t^2),\ dx=\frac{2t}{1+t^2}dt\)。 |
| missed_action | 没有先抓根式整体，而是尝试拆分 \(x\)、\(e^x\) 或把根式分母拆成两项；对根式差式有非法拆分倾向。 |
| related_method_card_id | H09-003 |
| next_reminder | 不定积分里有复杂根式整体，先问能不能令整个根式为 t；换元成功的标准是根式、指数项和 dx 一起抵消，不要把 \(\sqrt{a-b}\) 拆成 \(\sqrt a-\sqrt b\)。换元后出现 \(\ln(1+t^2)\) 继续分部。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-008_触发信息遗漏]]
- [[MATHWIKI-ERROR-CLUSTER-087_根式整体换元触发不足]]
- [[MATHWIKI-ERROR-CLUSTER-145_分部积分二次触发不稳定]]
- [[MATHWIKI-ERROR-CLUSTER-240_方法入口错误]]
- [[MATHWIKI-ERROR-CLUSTER-376_根式非法拆分倾向]]
- [[MATHWIKI-KNOWLEDGE-020_不定积分]]
- [[MATHWIKI-KNOWLEDGE-024_分部积分]]
- [[MATHWIKI-KNOWLEDGE-041_第二类换元]]
- [[MATHWIKI-KNOWLEDGE-044_有理函数积分]]
- [[MATHWIKI-KNOWLEDGE-058_根式积分]]
- [[MATHWIKI-KNOWLEDGE-082_反正切型积分]]
- [[MATHWIKI-KNOWLEDGE-103_根式换元]]
- [[MATHWIKI-KNOWLEDGE-125_根式整体换元]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-007_分部积分]]
- [[MATHWIKI-METHOD-CLUSTER-044_第二类换元]]
- [[MATHWIKI-METHOD-CLUSTER-1331_补常数化简]]
- [[MATHWIKI-METHOD-CLUSTER-166_根式整体换元]]

### 深度编译页

- [[MATHWIKI-GS-METHOD-039_不定积分结构化化归入口]]
- [[MATHWIKI-GS-METHOD-043_根式积分换元与回代链]]
- [[MATHWIKI-GS-TOPIC-013_不定积分与三角有理式错题总线]]

说明：覆盖表和索引型簇页表示本题已纳入 LLM Wiki 框架；深度编译页才表示已经进一步沉淀成可复用概念、方法、专题、错因或触发。

## wrongnet 关联题

- GS-270
- GS-275
- GS-609

## 下一步

- 若本题暴露可复用概念，更新 `wiki/concepts/`。
- 若本题暴露稳定第一动作，更新 `wiki/methods/` 或 `wiki/triggers/`。
- 若本题属于错题簇，更新 `wiki/topics/`。
- 若本题错因可复用，更新 `wiki/error_patterns/`。
- 不在本页复制完整题干或长解析。

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
