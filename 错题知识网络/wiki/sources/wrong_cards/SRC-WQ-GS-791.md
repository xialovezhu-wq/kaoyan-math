---
wiki_id: "SRC-WQ-GS-791"
type: "source_summary"
title: "GS-791 57849偏导存在的推论"
subject: "高等数学"
source_role: "formal_wrong_card"
source_refs:
  - "错题知识网络/错题卡/GS-791_57849偏导存在的推论.md"
wrongnet_refs:
  - "GS-791"
knowledge:
  - "偏导定义"
  - "多元函数连续可微"
  - "可微定义"
  - "一元函数可导与连续"
  - "极限类型"
methods:
  - "对应坐标截线可导推出连续"
  - "区分一维与二维极限"
error_causes:
  - "方法入口未触发"
wiki_refs:
  - "MATHWIKI-ACTION-GAP-003"
  - "MATHWIKI-ERROR-CLUSTER-080"
  - "MATHWIKI-KNOWLEDGE-037"
  - "MATHWIKI-KNOWLEDGE-072"
  - "MATHWIKI-KNOWLEDGE-520"
  - "MATHWIKI-KNOWLEDGE-522"
  - "MATHWIKI-KNOWLEDGE-523"
  - "MATHWIKI-METHOD-CLUSTER-1597"
  - "MATHWIKI-METHOD-CLUSTER-1598"
status: "indexed"
last_updated: "2026-09-08"
formal_projection_sha256: "d3399b4ad41c32d9a2ffb524bca5be5ee1b6064d21727bd07ae706a5c1fb5c43"
---

# GS-791 57849偏导存在的推论

## 当前证据

能写偏导定义，却未从坐标截线的一元可导性想到相应连续性；附加追问又把非零常数除趋零量误称为未定式。

- 2026-09-06 AI评分 3/5：偏导差商独立正确；提示后能迁移到另一坐标方向，并正确回答可微推出连续与偏导存在；最后额外极限概念仍需纠正。

## 方法入口

将偏导先看成固定另一变量的一元导数，再使用可导必连续；不要跨对象扩大结论。

## 来源与簇入口

- [[错题知识网络/错题卡/GS-791_57849偏导存在的推论]]
- [[MATHWIKI-ACTION-GAP-003_B2-TRIGGER]]
- [[MATHWIKI-ERROR-CLUSTER-080_方法入口未触发]]
- [[MATHWIKI-KNOWLEDGE-037_多元函数连续可微]]
- [[MATHWIKI-KNOWLEDGE-072_可微定义]]
- [[MATHWIKI-KNOWLEDGE-520_偏导定义]]
- [[MATHWIKI-KNOWLEDGE-522_一元函数可导与连续]]
- [[MATHWIKI-KNOWLEDGE-523_极限类型]]
- [[MATHWIKI-METHOD-CLUSTER-1597_对应坐标截线可导推出连续]]
- [[MATHWIKI-METHOD-CLUSTER-1598_区分一维与二维极限]]
