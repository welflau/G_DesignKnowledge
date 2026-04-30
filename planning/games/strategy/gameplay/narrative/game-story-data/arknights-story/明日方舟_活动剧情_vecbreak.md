# 明日方舟 · 活动剧情 · vecbreak（2段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「vecbreak」完整剧情脚本（2个文件，0行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/vecbreak
- 脚本文件数：2

### guide_vec_break_defense

```
[HEADER(is_skippable=false, is_tutorial=true)] 矢量突破补给点引导
[Tutorial(waitForSignal="vec_break_defense_routed")]
[PopupDialog(dialogHead="$avatar_amiya")] 为了考核罗德岛干员们的协同作战能力，我们设置了特别战线测试区域，在此可以获取战备补给。
[Tutorial(target="buff_panel", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这是战备补给。使用干员在特别战线驻防后，我们便可以激活它们，从而为我们在核心突破行动中提供增益效果。
[Tutorial(target="enemy_panel", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这里是特别战线中会出现的敌人，也就是主要考核目标。我们可以提前查看情报，做好行动前的规划。
[PopupDialog(dialogHead="$avatar_amiya")] 为了防止敌人再度来袭，我们在特别战线中需要指定干员驻防在对应的地点，驻防干员将无法参与核心突破行动，也无法在助战中被选用。
[PopupDialog(dialogHead="$avatar_amiya")] 我们可以主动撤离驻防在特别战线中的干员，让他们重新加入到其他的行动中，但没有干员驻防，战备补给也会因此失效——更好的选择是选用其他干员替换驻防。
```

### guide_vec_break_entry

```
[HEADER(is_skippable=false, is_tutorial=true)] 矢量突破主页引导
[Tutorial(waitForSignal="template_act_entry_routed")]
[PopupDialog(dialogHead="$avatar_amiya")] 博士，欢迎来到罗德岛内部的考核测试“矢量突破”，本次考核将启用精英干员迷迭香的作战数据重构而成的作战模型作为训练官。
[Tutorial(target="btn_offense", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这里便是本次考核的主要测试场地——核心突破。在测试场地中每向上一层，便会增加新的考核点来检测我们的作战能力。
[Tutorial(target="btn_defense", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 在核心突破中突破第一层后，特别战线测试区域便会开放。通过关卡，派遣干员驻守，可以为我们在核心突破的战斗提供增益。
[Tutorial(target="btn_milestone", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 通过考核以后将会获得对应的胜绩积分，该积分可在突破里程碑中兑换奖励。
```


## 统计

- 总字符数：1859
- 对话行数：0


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
