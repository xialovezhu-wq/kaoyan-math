# StudyVault 接入设计：条件边界与分类讨论

日期：2026-06-28

## 定位

这是数学 Tutor 首批专题的输入设计。2026-06-28 已在安全边界内生成数学 LLM Wiki 的初版 StudyVault，不扫描整个数学系统，不读取或复制完整错题卡正文。

## StudyVault 位置

推荐位置：

```text
错题知识网络/wiki/study_vaults/条件边界与分类讨论/
```

已生成的全局数学 LLM Wiki StudyVault：

```text
错题知识网络/wiki/study_vaults/数学LLMWiki/StudyVault/
```

本专题仍可作为 `高等数学主线` 和 `方法错因训练` 的首批 drill 来源。

## 输入材料候选

| 类型 | 路径 | 使用方式 |
|---|---|---|
| 专题页 | `错题知识网络/wiki/topics/MATHWIKI-GS-TOPIC-001_条件边界与分类讨论.md` | 主输入，生成主动回忆问题。 |
| method_gap 规则 | `错题知识网络/方法论库/method_gap_schema.md` | 抽取 B2/B4/B5/B7 动作断点。 |
| 方法卡登记 | `错题知识网络/方法论库/method_card_registry.md` | 只引用方法卡 ID 和一句触发，不复制长正文。 |
| 无穷级数知识树 | `错题知识网络/知识树/高等数学18讲第16讲_无穷级数.md` | 只抽取端点、收敛域、条件收敛相关触发。 |
| 错题卡轻量标签 | `GS-027`、`GS-141`、`GS-285`、`GS-358`、`GS-558`、`GS-569`、`GS-635` | 只用 ID、知识点、错因、方法、触发，不复制题干解析。 |

## 训练题型

- 概念辨认：给出题面信号，判断是否需要先列边界。
- 第一动作：把“看到参数/端点/绝对值/收敛域”转成第一步动作。
- 分类边界列举：让用户列出应该分类的位置。
- 错因诊断：判断是 `B2-TRIGGER`、`B4-CHAIN`、`B5-CHECK` 还是 `B7-CALC`。
- 迁移练习：把级数端点意识迁移到积分分段、参数范围和定义域检查。

## 同步格式

Tutor 结果只允许同步高层摘要：

```markdown
## YYYY-MM-DD Tutor 摘要：条件边界与分类讨论

- weak_concepts:
- repeated_error_patterns:
- mastered_concepts:
- cross_system_candidates:
- next_review_candidate:
- do_not_write_back:
  - 不改错题卡
  - 不改回滚掌握度
  - 不写完整训练题和答案
```

## 禁止动作

- 不把 Tutor 分数写入 `数学一回滚复习系统/复习单元.json`。
- 不把 Tutor 训练题当正式错题卡。
- 不复制完整题干、完整解析或错题卡正文。
- 不直接对 `/Users/xiazhibin/Documents/kaoyan-math` 根目录运行 `tutor-setup`。

## 待确认

- 是否正式生成 StudyVault：已生成初版，路径为 `错题知识网络/wiki/study_vaults/数学LLMWiki/StudyVault/`。
- 是否补充线代或概率论的同类边界专题：待确认。
- 是否把训练摘要同步到第二大脑正式同步记录：待确认。
