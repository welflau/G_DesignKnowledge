# 明日方舟 · 活动剧情 · vecbv2（3段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「vecbv2」完整剧情脚本（3个文件，0行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/vecbv2
- 脚本文件数：3

### guide_vec_break_v2_defense

```
[HEADER(is_skippable=false, is_tutorial=true)] VecBreakV2 特别战线引导
[Tutorial(waitForSignal="vec_break_v2_defense_page_routed")]
[PopupDialog(dialogHead="$avatar_amiya")] 这里是特别战线的总览界面，博士可以在这里查看所有关卡的状态。完成关卡可以获得奖励，在限定时间内完成对应关卡可以获得额外奖励。
[PopupDialog(dialogHead="$avatar_amiya")] 本次作战中部分战备补给存在高级版。普通补给和高级补给无法同时激活，博士需要选择一个进行激活。高级关卡有各自的解锁条件，需要博士进行确认。同时，普通关卡驻守的干员不可以用于高级关卡的战斗中。
[Tutorial(target="pool_first_defense_stage", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击查看关卡的详细介绍。
[Tutorial(focusX=304, focusY=-82, focusWidth=583, focusHeight=190, anchor="Center",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这是战备补给。安排干员在特别战线中驻守后，我们便可以激活战备补给，从而为我们在核心突破的行动中提供增益效果。
[Tutorial(target="pool_defense_stage_enemy_area", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这里是特别战线中会出现的敌人，也就是主要考核目标。我们可以提前查看情报，做好行动前的规划。
[Tutorial(target="pool_defense_stage_btn_start", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 为了防止敌人再度来袭，我们在特别战线中需要指定干员驻守在对应的地点，驻守的干员将无法参与核心突破行动，也无法在助战中被选用。
[Tutorial(target="pool_defense_stage_btn_start", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 我们可以主动撤离驻守在特别战线中的干员，让他们重新加入到其他的行动中。
[Tutorial(target="pool_defense_stage_btn_start", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 但如果没有干员驻守，战备补给也会因此失效——更好的选择是选用其他干员替换驻守。
[Tutorial(target="pool_btn_defense_overview", waitForSignal="vec_break_v2_defense_overview_routed", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击此处，进入驻守总览界面。
[PopupDialog(dialogHead="$avatar_amiya")] 在驻守总览界面，博士可以总览所有的补给信息。同时，也可以查看所有关卡的详细情报以及驻守情况。
```

### guide_vec_break_v2_entry

```
[HEADER(is_skippable=false, is_tutorial=true)] VecBreakV2 主页引导
[Tutorial(waitForSignal="template_act_entry_routed")]
[PopupDialog(dialogHead="$avatar_amiya")] 博士，欢迎来到罗德岛内部的考核测试“矢量突破”，本次考核将启用精英干员的作战数据重构而成的作战模型作为训练官。
[Tutorial(target="pool_entry_btn_offense", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这里是本次考核的主要测试场地——核心突破。训练官会在终点迎接各位挑战。
[Tutorial(target="pool_entry_btn_hard", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 突破12层核心后，第二周将解锁高难度关卡入口，迎接更具挑战性的试炼。同时，往期的精英干员也将返场。
[Tutorial(target="pool_entry_btn_achv", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 每个赛季的成绩会在赛季结束后常驻记录，可以点击此处跳转查看。
[Tutorial(target="pool_entry_btn_offense", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 博士开始挑战吧。
```

### guide_vec_break_v2_squad_buff

```
[HEADER(is_skippable=false, is_tutorial=true)] VecBreakV2 编队引导
[Tutorial(waitForSignal="vec_break_v2_squad_buff_guide_ready")]
[Tutorial(target="pool_btn_edit_buff", waitForSignal="vec_break_v2_squad_buff_page_routed", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 为了考核罗德岛干员们的协同作战能力，我们设置了特别战线的测试区域，此区域可以获取战备补给。
[Tutorial(target="pool_squad_buff_edit_area", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这里可以看到所有战备补给的激活和启用情况。
[Tutorial(target="pool_squad_buff_equip_area", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击已激活的战备补给可以启用补给，并在右侧看到对应的具体效果。可启用的补给存在数量限制，博士最多可以同时启用六个补给。
[Tutorial(target="pool_squad_buff_btn_nav", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击此处可进入特别战线，驻防干员激活更多战备补给，以挑战训练官为目标吧！
```


## 统计

- 总字符数：4613
- 对话行数：0


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
