# method_gap 解题方法断点层标准

`method_gap` 是数学错题卡中的“解题方法断点层”，用于记录：

```text
看到什么题面信号 -> 本应想到什么方法 -> 第一动作该做什么 -> 实际漏掉什么动作 -> 下次如何提醒
```

它不替代原有的 `wrong_point`、`error_causes`、`methods`、`traps`，而是在知识点错因之外，单独记录“知识学过但方法没有触发”或“动作链没有执行完整”的断点。

## 标准字段

```yaml
method_gap:
  enabled: true
  evidence_origin: user_confirmed
  knowledge_gap_or_method_gap: ""
  method_trigger: ""
  expected_method: ""
  expected_first_action: ""
  missed_action: ""
  action_gap_type: ""
  opd_tag: []
  related_method_card_id: ""
  next_reminder: ""
  repeat_count: 1
  repeat_count_source: "试点阶段估计，未全局统计"
  review_priority: 3
  confidence: ""
  need_user_confirmation: false
```

## 字段解释

| 字段 | 含义 | 写法要求 |
| -- | -- | -- |
| `enabled` | 是否启用 `method_gap` | 一般写 `true` |
| `evidence_origin` | 这个断点的证据来源 | 只能写 `user_confirmed`、`model_inferred_from_solution`、`pending_user_confirmation` |
| `knowledge_gap_or_method_gap` | 判断本题是知识缺口、方法断点还是混合问题 | 必须从允许值中选择 |
| `method_trigger` | 题面触发信息，即“看到什么” | 不能空，要写题面信号 |
| `expected_method` | 看到触发信息后本应想到的方法论 | 写方法路径，不写长解析 |
| `expected_first_action` | 第一动作 | 必须是可执行动作句，不能只是方法名 |
| `missed_action` | 实际漏掉的动作 | 必须具体到漏了哪一步 |
| `action_gap_type` | 动作断点统一标签 | 必须从统一标签中选择 |
| `opd_tag` | 对应 OPD 解题结构 | 只能用 `O目标`、`P思路`、`D细节` |
| `related_method_card_id` | 对应方法论库方法卡 ID | 优先查方法论库；找不到写 `待匹配` |
| `next_reminder` | 下次复习提醒句 | 必须写成考场动作句 |
| `repeat_count` | 该动作断点历史重复次数 | 本阶段默认可写 `1` |
| `repeat_count_source` | `repeat_count` 来源说明 | 默认写 `试点阶段估计，未全局统计` |
| `review_priority` | 方法断点回滚优先级 | 取 `1` 到 `5` |
| `confidence` | 归因置信度 | 只能写 `high`、`medium`、`low` |
| `need_user_confirmation` | 是否需要用户确认 | `confidence: low` 时必须为 `true` |

### evidence_origin

- `user_confirmed`：用户的作答过程、第一错步、口述错因或明确复发证据直接支持该断点。只有这一类可以无保留地称为“个人真实错因”。
- `model_inferred_from_solution`：模型仅根据题面、标准解析或正确路线提炼复做入口。它可以作为待验证的教学建议，不得冒充用户实际错因。
- `pending_user_confirmation`：已有候选断点，但证据不足或仍需用户确认。该类证据不能用于确定性的针对性出题。

历史卡缺少 `evidence_origin` 时，读取层标记为 `legacy_unclassified`，不批量猜测或迁移。只有旧卡已经具备高置信、具体动作字段且不需用户确认时，筛选层才可将它作为有限的历史结构化证据；对外仍不宣称它已由用户确认。

## 允许值

### knowledge_gap_or_method_gap

- `知识缺口`
- `定理条件未知`
- `概念混淆`
- `方法调取失败`
- `动作链断裂`
- `条件检查遗漏`
- `收尾验证遗漏`
- `运算路径不稳`
- `A+B混合`
- `需人工确认`

### action_gap_type

| 标签 | 中文名 | 判断标准 |
| -- | -- | -- |
| `A-KG` | 知识点不熟 | 公式、定义、定理、性质本身不会 |
| `A-COND` | 定理条件未知 | 会用结论但不知道适用条件 |
| `A-CONCEPT` | 概念混淆 | 概念含义、对象、等价关系理解错 |
| `B1-GOAL` | 目标识别断点 | 没先判断题目到底要求什么 |
| `B2-TRIGGER` | 触发信息遗漏 | 题面信号明显，但没有识别出来 |
| `B3-METHOD` | 方法调取失败 | 识别出模块，但没有调出对应套路 |
| `B4-CHAIN` | 动作链断裂 | 方向对，但少了关键步骤 |
| `B5-CHECK` | 条件检查遗漏 | 用了公式或定理，但漏验条件 |
| `B6-CLOSE` | 收尾验证遗漏 | 算出中间量后没回到题目要求检查 |
| `B7-CALC` | 运算路径不稳 | 方法知道，但计算、变形、分类讨论中断 |

### opd_tag

- `O目标`
- `P思路`
- `D细节`

映射建议：

| action_gap_type | 建议 opd_tag |
| -- | -- |
| `B1-GOAL` | `O目标` |
| `B2-TRIGGER` | `P思路` |
| `B3-METHOD` | `P思路` |
| `B4-CHAIN` | `D细节` |
| `B5-CHECK` | `D细节` |
| `B6-CLOSE` | `D细节` |
| `B7-CALC` | `D细节` |
| `A-KG` / `A-COND` / `A-CONCEPT` | 知识层；若必须归类，写 `D细节` |

### review_priority

| 值 | 含义 |
| -- | -- |
| `1` | 低优先级，偶发问题 |
| `2` | 轻微问题 |
| `3` | 常规复习 |
| `4` | 高频断点 |
| `5` | 严重反复断点 |

### confidence

| 值 | 判断标准 |
| -- | -- |
| `high` | 错因明确写出漏掉的动作 |
| `medium` | 可从 `wrong_point`、`methods`、`traps` 合理推断 |
| `low` | 信息不足，只能猜测 |

## 新增错题时的写入规则

### 必须写 method_gap

如果错题原因属于以下情况，必须写 `method_gap`：

- 知识点学过，但做题时没想到入口；
- 题面出现明显触发词，但没有转成方法；
- 方向对，但动作链少了一步；
- 用了公式，但漏了使用条件；
- 算出中间结论，但没回代题目目标；
- 做题时不是不会知识，而是方法没有触发。

### 可以暂不写 method_gap

以下情况可以暂不写 `method_gap`：

- 纯粹公式没背；
- 定义完全不知道；
- 概念本身混淆；
- 题干缺失，无法判断触发信息；
- 用户没有提供任何思考过程，无法判断是知识缺口还是方法断点。

如果是知识缺口和方法断点混合，应该写 `method_gap`，并标记：

```yaml
knowledge_gap_or_method_gap: A+B混合
```

### A 类和 B 类区分

- A 类：确实不知道定义、公式、定理、性质、适用条件，或概念本身理解错误。
- B 类：知识可能学过，也能看懂答案，但实战时没有从题面信号触发正确方法，或动作链没有执行完整。

如果是“看得懂答案，但自己做时没想到入口”，优先考虑 `B2-TRIGGER`、`B3-METHOD`、`B4-CHAIN`，不要直接归为“知识点不熟”。

## related_method_card_id 规则

1. 优先查询 `错题知识网络/方法论库/方法卡/` 和 `错题知识网络/方法论库/method_card_registry.md`。
2. 只能引用 registry 中已有 ID。
3. 找不到可靠对应方法卡时，写 `related_method_card_id: 待匹配`。
4. 不得随意乱造 ID。
5. 如果确实需要新增方法卡，必须先更新方法卡来源文件，并登记到 `method_card_registry.md`。
6. 错题卡只引用 `related_method_card_id`，不得复制整张方法卡。

## next_reminder 写法

`next_reminder` 必须写成考场动作句，推荐格式：

```text
看到____，先____，再____。
```

示例：

- 看到级数判敛，先查通项极限，再选判别法。
- 看到幂级数，先求半径，再逐个查端点。
- 看到中值证明含 f 和 f'，先从目标式反推辅助函数。
- 看到闭区间最值，先找驻点，再列端点比较。
- 看到隐函数求导，先确认谁随 x 变，再做链式求导。
- 看到中间量已算出，先代回题目目标式，再结束。

## 正确与错误写法

### expected_first_action

正确写法：

- `先计算 lim u_n`
- `先写出逐项积分后的新通项`
- `先令 f'(x)=0 找内部驻点`
- `先标出谁是自变量，谁随谁变化`
- `先写出二次型对应的对称矩阵`

错误写法：

- `用比较法`
- `用中值定理`
- `用特征值`
- `用正定判别`

## 标准示例

### 示例 1：级数判敛

```yaml
method_gap:
  enabled: true
  knowledge_gap_or_method_gap: 方法调取失败
  method_trigger: 看到数项级数判敛散
  expected_method: 先检查通项极限，再选择判别法
  expected_first_action: 计算 lim u_n
  missed_action: 没有先检查通项是否趋于 0
  action_gap_type: B3-METHOD
  opd_tag:
    - P思路
  related_method_card_id: 待匹配
  next_reminder: 看到级数判敛，先查通项极限，再选判别法。
  repeat_count: 1
  repeat_count_source: 试点阶段估计，未全局统计
  review_priority: 3
  confidence: medium
  need_user_confirmation: false
```

### 示例 2：幂级数端点

```yaml
method_gap:
  enabled: true
  knowledge_gap_or_method_gap: 动作链断裂
  method_trigger: 看到幂级数收敛域
  expected_method: 先求收敛半径或收敛区间，再单独检查端点
  expected_first_action: 先对一般项做比值、根值或换元求半径
  missed_action: 只求了半径，没有单独检查端点
  action_gap_type: B4-CHAIN
  opd_tag:
    - D细节
  related_method_card_id: 待匹配
  next_reminder: 看到幂级数，先求半径，再逐个查端点。
  repeat_count: 1
  repeat_count_source: 试点阶段估计，未全局统计
  review_priority: 3
  confidence: medium
  need_user_confirmation: false
```

### 示例 3：中值定理辅助函数

```yaml
method_gap:
  enabled: true
  knowledge_gap_or_method_gap: 方法调取失败
  method_trigger: 看到结论中含 f、f'、端点值、存在 xi
  expected_method: 从目标式反推辅助函数
  expected_first_action: 把目标式改写成某个辅助函数的导数为零
  missed_action: 没有反推辅助函数入口
  action_gap_type: B3-METHOD
  opd_tag:
    - P思路
  related_method_card_id: 待匹配
  next_reminder: 看到中值证明含 f 和 f'，先从目标式反推辅助函数。
  repeat_count: 1
  repeat_count_source: 试点阶段估计，未全局统计
  review_priority: 3
  confidence: medium
  need_user_confirmation: false
```

### 示例 4：隐函数求导

```yaml
method_gap:
  enabled: true
  knowledge_gap_or_method_gap: 运算路径不稳
  method_trigger: 看到隐函数求导或参数函数求导
  expected_method: 先明确自变量和因变量
  expected_first_action: 标出谁随谁变化
  missed_action: 把中间变量当常量，漏掉链式求导
  action_gap_type: B7-CALC
  opd_tag:
    - D细节
  related_method_card_id: 待匹配
  next_reminder: 看到隐函数求导，先确认谁随 x 变，再做链式求导。
  repeat_count: 1
  repeat_count_source: 试点阶段估计，未全局统计
  review_priority: 3
  confidence: medium
  need_user_confirmation: false
```

### 示例 5：收尾回代

```yaml
method_gap:
  enabled: true
  knowledge_gap_or_method_gap: 收尾验证遗漏
  method_trigger: 算出中间量、参数、驻点、中值点、特征值、极限后
  expected_method: 回到题目目标式检查
  expected_first_action: 把中间结论代回原题要求
  missed_action: 没有代回目标式化简或验证
  action_gap_type: B6-CLOSE
  opd_tag:
    - D细节
  related_method_card_id: H00-013
  next_reminder: 看到中间量已算出，先代回题目目标式，再结束。
  repeat_count: 1
  repeat_count_source: 试点阶段估计，未全局统计
  review_priority: 3
  confidence: high
  need_user_confirmation: false
```

## 校验规则

以后任何 `method_gap` 必须满足：

1. `method_trigger` 不能空。
2. `expected_method` 不能空。
3. `expected_first_action` 必须是动作句，不能只是方法名。
4. `missed_action` 必须具体到“漏了哪一步”。
5. `action_gap_type` 必须来自统一标签。
6. `opd_tag` 必须来自 `O目标`、`P思路`、`D细节`。
7. `related_method_card_id` 必须来自方法论库；找不到写 `待匹配`。
8. `next_reminder` 必须是考场动作句。
9. `confidence: low` 时，`need_user_confirmation` 必须为 `true`。
10. 不得覆盖原 `wrong_point`、`error_causes`、`methods`、`traps`。
