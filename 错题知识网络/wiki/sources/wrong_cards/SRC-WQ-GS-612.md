---
wiki_id: SRC-WQ-GS-612
type: source_summary
title: GS-612 77127 对数复合二次式展成幂级数 2026.6.18
subject: 高等数学
source_role: formal_wrong_card
source_refs:
- 错题知识网络/错题卡/GS-612_77127对数复合二次式展开.md
visual_detail_refs:
- 错题知识网络/可视化错题详情/高等数学/GS-612_77127.md
visual_ids:
- VIS-GS-612
wrongnet_refs:
- GS-612
knowledge:
- 无穷级数
- 幂级数
- 函数展开成幂级数
- 常用幂级数展开式
- 对数级数展开
- 幂级数收敛域
- 代数恒等变形
error_causes:
- 因式分解未朝凑1+u目标
- 对数拆分忽略因子须为正
- 收敛区间未区分代换区间与端点收敛性
- 端点未单独判断
methods:
- 先判型
- 因式分解凑1+u
- 对数运算拆分
- 代入ln(1+t)母公式
- 公共收敛区间取交
- 端点单独检查
wiki_refs:
- MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表
- MATHWIKI-ACTION-GAP-001_B3-METHOD
- MATHWIKI-ERROR-CLUSTER-091_端点未单独判断
- MATHWIKI-ERROR-CLUSTER-178_因式分解未朝凑1+u目标
- MATHWIKI-ERROR-CLUSTER-196_对数拆分忽略因子须为正
- MATHWIKI-ERROR-CLUSTER-233_收敛区间未区分代换区间与端点收敛性
- MATHWIKI-KNOWLEDGE-005_无穷级数
- MATHWIKI-KNOWLEDGE-048_幂级数
- MATHWIKI-KNOWLEDGE-092_幂级数收敛域
- MATHWIKI-KNOWLEDGE-122_常用幂级数展开式
- MATHWIKI-KNOWLEDGE-137_函数展开成幂级数
- MATHWIKI-KNOWLEDGE-175_对数级数展开
- MATHWIKI-KNOWLEDGE-231_代数恒等变形
- MATHWIKI-METHOD-CLUSTER-001_先判型
- MATHWIKI-METHOD-CLUSTER-196_公共收敛区间取交
- MATHWIKI-METHOD-CLUSTER-445_端点单独检查
- MATHWIKI-METHOD-CLUSTER-576_代入ln-1+t-母公式
- MATHWIKI-METHOD-CLUSTER-839_因式分解凑1+u
- MATHWIKI-METHOD-CLUSTER-925_对数运算拆分
- MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点
- MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口
status: indexed
last_updated: '2026-07-25'
related_wrongnet_refs: []
formal_projection_sha256: 03ecac24e8a4668caed940401b8532f3eb55c0d6e4e457162d6271abc9bbbdc3
question_asset_refs:
- 错题知识网络/assets/visual_wrong_questions/GS-612/question_01.png
solution_asset_refs: []
reference_asset_refs: []
evidence_status: user_confirmed
question_surface_status: registered_answer_safe_question_only
aggregate_edge_policy: allow
evidence_boundary: "个人错因仅来自正式学习事务中的 wrong_history；视觉资产和客观解析不反推个人错因。"
review_batch: MATHWIKI-REVIEW-080
confirmation_state: confirmed
mismatch_evidence_refs: []
mismatch_evidence_visual_ids: []
---

# GS-612 77127 对数复合二次式展成幂级数 2026.6.18

## 来源定位

- 正式错题卡：`错题知识网络/错题卡/GS-612_77127对数复合二次式展开.md`
- wrongnet ID：`GS-612`
- 角色：正式错题卡的轻量 source summary；本页是可重建投影，不替代正式卡。

## 可视化入口

- 详情页：`错题知识网络/可视化错题详情/高等数学/GS-612_77127.md`（`VIS-GS-612`）
- 题图 1 张；解析图 0 张；参考图 0 张。

## 当前语义投影

- 知识点：无穷级数、幂级数、函数展开成幂级数、常用幂级数展开式、对数级数展开、幂级数收敛域、代数恒等变形
- 方法：先判型、因式分解凑1+u、对数运算拆分、代入ln(1+t)母公式、公共收敛区间取交、端点单独检查
- 错因字段：因式分解未朝凑1+u目标、对数拆分忽略因子须为正、收敛区间未区分代换区间与端点收敛性、端点未单独判断
- 第一动作：先把 \(1-x-2x^2\) 凑成 \((1+ax)(1+bx)\)：解 \(a+b=-1,\ ab=-2\) 得 \((1+x)(1-2x)\)。
- 个人断点：因式分解时把负常数 \(-2\) 提出，写成 \(\ln(-2)+\ln(\cdots)\)（实数无意义）；收敛区间直接照搬代换公式开区间，没单独判端点 \(x=\pm\frac12\)。
- 方法卡 ID：H04-003
- 当前强关系：暂无强边

## 证据边界

- 个人错因仅来自正式学习事务中的 wrong_history；视觉资产和客观解析不反推个人错因。
- 题图存在不等于个人作答过程、错误次数或掌握度已获证实。

## 已连接 wiki

- [[MATHWIKI-COVERAGE-GS_高等数学错题卡覆盖表]]
- [[MATHWIKI-ACTION-GAP-001_B3-METHOD]]
- [[MATHWIKI-ERROR-CLUSTER-091_端点未单独判断]]
- [[MATHWIKI-ERROR-CLUSTER-178_因式分解未朝凑1+u目标]]
- [[MATHWIKI-ERROR-CLUSTER-196_对数拆分忽略因子须为正]]
- [[MATHWIKI-ERROR-CLUSTER-233_收敛区间未区分代换区间与端点收敛性]]
- [[MATHWIKI-KNOWLEDGE-005_无穷级数]]
- [[MATHWIKI-KNOWLEDGE-048_幂级数]]
- [[MATHWIKI-KNOWLEDGE-092_幂级数收敛域]]
- [[MATHWIKI-KNOWLEDGE-122_常用幂级数展开式]]
- [[MATHWIKI-KNOWLEDGE-137_函数展开成幂级数]]
- [[MATHWIKI-KNOWLEDGE-175_对数级数展开]]
- [[MATHWIKI-KNOWLEDGE-231_代数恒等变形]]
- [[MATHWIKI-METHOD-CLUSTER-001_先判型]]
- [[MATHWIKI-METHOD-CLUSTER-196_公共收敛区间取交]]
- [[MATHWIKI-METHOD-CLUSTER-445_端点单独检查]]
- [[MATHWIKI-METHOD-CLUSTER-576_代入ln-1+t-母公式]]
- [[MATHWIKI-METHOD-CLUSTER-839_因式分解凑1+u]]
- [[MATHWIKI-METHOD-CLUSTER-925_对数运算拆分]]
- [[MATHWIKI-GS-METHOD-009_B3-METHOD方法调取断点]]
- [[MATHWIKI-SYNTHESIS-001_当前高价值错因与方法缺口]]

## wrongnet 关联题

- 暂无强边

## 总索引

- [[SRC-WRONGCARDS-INDEX_全量错题卡覆盖索引]]
- [[SRC-WRONGNET_正式错题卡源数据]]
