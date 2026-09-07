---
wiki_id: SRC-WQ-GS-726
type: source_summary
title: "GS-726 84289 旋转圆锥闭曲面通量"
subject: "高等数学"
source_role: formal_wrong_card
source_refs:
  - "错题知识网络/错题卡/GS-726_84289旋转圆锥闭曲面通量.md"
visual_detail_refs:
  - "错题知识网络/可视化错题详情/高等数学/GS-726_84289旋转圆锥闭曲面通量.md"
visual_ids:
  - "VIS-GS-726"
wrongnet_refs:
  - "GS-726"
knowledge:
  - "多元函数积分学"
  - "第二型曲面积分"
  - "旋转曲面"
  - "圆锥面"
  - "曲面定向"
  - "有向投影面积"
error_causes:
  - "旋转轴与径向距离混淆"
  - "空间几何图像断点"
  - "闭曲面分块未触发"
  - "外侧定向与投影符号混淆"
  - "动作链断裂"
methods:
  - "轴截面求母线"
  - "旋转曲面方程"
  - "闭曲面分块"
  - "第二型曲面积分投影法"
  - "外法向量分量判号"
  - "极坐标"
wiki_refs:
  - "MATHWIKI-COVERAGE-GS"
  - "MATHWIKI-ACTION-GAP-002"
  - "MATHWIKI-ERROR-CLUSTER-004"
  - "MATHWIKI-ERROR-CLUSTER-038"
  - "MATHWIKI-ERROR-CLUSTER-535"
  - "MATHWIKI-ERROR-CLUSTER-536"
  - "MATHWIKI-ERROR-CLUSTER-537"
  - "MATHWIKI-KNOWLEDGE-073"
  - "MATHWIKI-KNOWLEDGE-379"
  - "MATHWIKI-KNOWLEDGE-448"
  - "MATHWIKI-KNOWLEDGE-449"
  - "MATHWIKI-KNOWLEDGE-450"
  - "MATHWIKI-KNOWLEDGE-451"
  - "MATHWIKI-METHOD-CLUSTER-1109"
  - "MATHWIKI-METHOD-CLUSTER-1489"
  - "MATHWIKI-METHOD-CLUSTER-1490"
  - "MATHWIKI-METHOD-CLUSTER-1491"
  - "MATHWIKI-METHOD-CLUSTER-1492"
  - "MATHWIKI-METHOD-CLUSTER-1493"
  - "MATHWIKI-GS-METHOD-102"
status: indexed
formal_projection_sha256: 07c9af88650e8bbeadddd7c4d935d25893a90b972e9145b0c0fcc560fc740591
last_updated: "2026-08-28"
related_wrongnet_refs: []
---

# GS-726 84289 旋转圆锥闭曲面通量

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-726_84289旋转圆锥闭曲面通量.md`
- wrongnet ID：`GS-726`
- 角色：正式错题卡的轻量 source summary，不替代完整题干与解析。

## 可视化入口

- [[错题知识网络/可视化错题详情/高等数学/GS-726_84289旋转圆锥闭曲面通量|VIS-GS-726]]
- [Obsidian 直达](obsidian://open?vault=kaoyan-math&file=%E9%94%99%E9%A2%98%E7%9F%A5%E8%AF%86%E7%BD%91%E7%BB%9C%2F%E5%8F%AF%E8%A7%86%E5%8C%96%E9%94%99%E9%A2%98%E8%AF%A6%E6%83%85%2F%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6%2FGS-726_84289%E6%97%8B%E8%BD%AC%E5%9C%86%E9%94%A5%E9%97%AD%E6%9B%B2%E9%9D%A2%E9%80%9A%E9%87%8F)
- 已核验视觉资产：`错题知识网络/assets/visual_wrong_questions/GS-726/question_01.png`；`错题知识网络/assets/visual_wrong_questions/GS-726/solution_01.png`

## 轻量字段

| 字段 | 值 |
|---|---|
| 科目 | 高等数学 |
| 章节 | 多元函数积分学 |
| 题型 | 旋转圆锥闭曲面的第二型曲面积分 |
| 日期 | 2026-07-27 |
| 状态 | 待复做 |
| 优先级 | A |
| 难度 | 4 |

## 本次正式结论

- 当前错点：第一个断点是混淆旋转轴与径向距离：绕 \(z\) 轴旋转时，横向半径应为 \(\rho=\sqrt{x^2+y^2}\)，所以母线 \(z=-x\) 生成 \(x^2+y^2=z^2\)，不是 \(x^2+z^2=y^2\)。后续又未把闭曲面拆成下底、上底和侧面，也未将 \(dx\,dy\) 的符号与外法向量的 \(z\) 分量对应。
- 最新错误证据：2026-07-27 第1次错：正确识别母线位于 \(xOz\) 平面并想到绕 \(z\) 轴旋转得到圆锥，也知道 \(z=1,z=2\) 截取中间一段；但把旋转圆锥误写成 \(x^2+z^2=y^2\)，随后不知道闭曲面还应拆成上下底面和圆锥侧面，也不理解外侧定向怎样决定 \(dx\,dy\) 的正负号。经完整讲解后能够正确复述内外侧法向量以及改取内侧时三块曲面的符号反转。
- 最新掌握证据：2026-07-27 AI评分 2/5：母线所在平面、旋转成圆锥和两个水平截面均有独立正确识别；旋转轴对应的径向距离、闭曲面分块、投影区域和第二型曲面积分定向均依赖完整讲解，尚无无提示重做证据。
- 2026-08-28 跨来源同题 ID138759：独立完成侧面绝对值积分，但漏掉上下底面并未按外法向量的 (z) 分量给侧面判负；讲解后理解，不补造评分。

## 可编译信息

### 知识点

- 多元函数积分学
- 第二型曲面积分
- 旋转曲面
- 圆锥面
- 曲面定向
- 有向投影面积

### 错因

- 旋转轴与径向距离混淆
- 空间几何图像断点
- 闭曲面分块未触发
- 外侧定向与投影符号混淆
- 动作链断裂

### 方法

- 轴截面求母线
- 旋转曲面方程
- 闭曲面分块
- 第二型曲面积分投影法
- 外法向量分量判号
- 极坐标

## method_gap 摘要

| 字段 | 值 |
|---|---|
| action_gap_type | B4-CHAIN |
| expected_first_action | 先由 \(A(-1,0,1)\)、\(B(0,0,0)\) 写出母线 \(y=0,z=-x\)，再明确绕 \(z\) 轴时 \(|x|\) 替换成 \(\sqrt{x^2+y^2}\)。 |
| missed_action | 把绕 \(z\) 轴所得圆锥写成绕 \(y\) 轴的标准式；即使知道是圆锥，也没有继续列出闭曲面的三块组成、各自投影区域和外侧符号。 |
| related_method_card_id | H18-013 |
| next_reminder | 旋转曲面先盯旋转轴，写“到该轴的距离”；闭曲面再拆盖面与侧面；第二型曲面积分先按侧向判有向投影符号，再积分。 |

## 已连接 wiki

### 覆盖入口

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]

### 索引型簇页

- [[MATHWIKI-ACTION-GAP-002_B4-CHAIN]]
- [[MATHWIKI-ERROR-CLUSTER-004_动作链断裂]]
- [[MATHWIKI-ERROR-CLUSTER-038_空间几何图像断点]]
- [[MATHWIKI-ERROR-CLUSTER-535_旋转轴与径向距离混淆]]
- [[MATHWIKI-ERROR-CLUSTER-536_闭曲面分块未触发]]
- [[MATHWIKI-ERROR-CLUSTER-537_外侧定向与投影符号混淆]]
- [[MATHWIKI-KNOWLEDGE-073_多元函数积分学]]
- [[MATHWIKI-KNOWLEDGE-379_旋转曲面]]
- [[MATHWIKI-KNOWLEDGE-448_第二型曲面积分]]
- [[MATHWIKI-KNOWLEDGE-449_圆锥面]]
- [[MATHWIKI-KNOWLEDGE-450_曲面定向]]
- [[MATHWIKI-KNOWLEDGE-451_有向投影面积]]
- [[MATHWIKI-METHOD-CLUSTER-1109_极坐标]]
- [[MATHWIKI-METHOD-CLUSTER-1489_轴截面求母线]]
- [[MATHWIKI-METHOD-CLUSTER-1490_旋转曲面方程]]
- [[MATHWIKI-METHOD-CLUSTER-1491_闭曲面分块]]
- [[MATHWIKI-METHOD-CLUSTER-1492_第二型曲面积分投影法]]
- [[MATHWIKI-METHOD-CLUSTER-1493_外法向量分量判号]]

### 深度方法与专题

- [[MATHWIKI-GS-METHOD-102_第18讲多元积分方法卡总表]]
