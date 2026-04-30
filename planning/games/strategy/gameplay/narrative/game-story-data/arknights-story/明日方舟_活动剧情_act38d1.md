# 明日方舟 · 活动剧情 · act38d1（3段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act38d1」完整剧情脚本（3个文件，0行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act38d1
- 脚本文件数：3

### guide_act38d1_entry

```
[HEADER(is_skippable=false, is_tutorial=true)] act38d1引导
[PopupDialog(dialogHead="$avatar_doberm")] 博士，你终于来了，欢迎参加尖灭测试作战。
[PopupDialog(dialogHead="$avatar_doberm")] 在尖灭测试作战中，有多项测试指标等待着博士挑战。在完成指定的指标后，晶块陈列室将会对你开放，丰厚的奖励储存于其中。
[Tutorial(target="btn_act38d1_open_map", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm",           waitForSignal="act38d1_map_routed", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 现在随我前往测试场地吧。
[Tutorial(target="btn_act38d1_map_detail", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm",           waitForSignal="act38d1_map_detail_routed", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 博士，现在我们操作的是测试平台，你需要的关卡情报被存放在这里。
[PopupDialog(dialogHead="$avatar_doberm")] 这一次你要对付的敌对势力，来自莱茵生命。你应该还没忘记吧，那些动力装甲可是大麻烦。
[Tutorial(target="btn_act38d1_map_detail_back", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm",           waitForSignal="act38d1_map_back_routed", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 让我们回到测试平台。
[PopupDialog(dialogHead="$avatar_doberm")] 看看这里。
[Act38D1.FocusSlot(slotId="slot_6_1", slotType="NORMAL")]
[Tutorial(focusX=-491, focusY=-371, focusWidth=80, focusHeight=485, anchor="Top",          animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这些是起始节点，任何与之相连的测试指标都能被选择加入作战中。
[Tutorial(target="btn_act38d1_slot_6_1", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm",           dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 请点击测试指标。 
[Tutorial(target="btn_act38d1_slot_6_2", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm")] 请点击下一个测试指标。 
[Tutorial(target="btn_act38d1_slot_6_3", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm",           dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 请点击与之相连的下一个测试指标。
[Tutorial(target="btn_act38d1_map_rune_detail", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm",           waitForSignal="act38d1_map_rune_detail_routed", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 右下方显示的是当前所选测试指标的评分，这点难度应该难不倒你吧，博士。
[PopupDialog(dialogHead="$avatar_doberm")] 你可以在这里看到已添加的测试指标。
[Tutorial(target="btn_act38d1_map_rune_detail_back", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm",           waitForSignal="act38d1_map_back_routed", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 让我们返回测试平台。
[Tutorial(target="btn_act38d1_slot_6_3", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm",           dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 出于对未来的考量，我希望你能量力而行。如果你判断某项指标在本次作战中无法完成，再次点击即可取消添加。
[Tutorial(target="btn_act38d1_start_battle", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm",           dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 一切准备就绪，请开始测试吧，博士。我很期待你的表现。
```

### guide_act38d1_main

```
[HEADER(is_skippable=false, is_tutorial=true)] act38d1常驻图引导
[Tutorial(waitForSignal="act38d1_map_routed")]
[Tutorial(dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x",           dialogY="$f_lower_dialog_pos_y")] 抱歉，还有些事情我需要补充一下。
[Act38D1.JumpToPermanentMap]
[Delay(time=0.5)]
[PopupDialog(dialogHead="$avatar_doberm")] ......关于此次测试作战中的其他内容。
[Act38D1.FocusSlot(slotId="slot_41_1", slotType="NORMAL")]
[Tutorial(target="btn_act38d1_slot_41_1", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm",           dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 请点击此处。
[Delay(time=0.5)]
[Tutorial(target="rune_act38d1_treasure", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_doberm",           dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这里是晶块陈列室，想要获取其中存放的奖励，就必须完成与其相连的测试指标。
[Delay(time=0.5)]
[Act38D1.FocusSlot(slotId="slot_62_1", slotType="NORMAL")]
[Tutorial(target="btn_act38d1_slot_62_1", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm")] 接下来我们查看作战任务。
[Delay(time=0.5)]
[Tutorial(target="text_act38d1_challenge_desc", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_doberm",           dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 作战任务位于通往晶块陈列室的路径上，完成作战任务将激活该节点，使与之相连的测试指标可供选择，无需再从起始节点选起。
[Delay(time=0.5)]
[Act38D1.FocusSlot(slotId="slot_53_1", slotType="NORMAL")]
[PopupDialog(dialogHead="$avatar_doberm")]再看这里。
[PopupDialog(dialogHead="$avatar_doberm")]每隔一段时间，一个测试地块的入口将在平台上开放。
[Delay(time=0.5)]
[Tutorial(target="btn_act38d1_slot_53_1", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_doberm")] 完成测试地块的作战能够激活节点，获得报酬，并解锁新的测试指标。与作战任务相同，被激活的测试地块节点能使与之相连的测试指标可供选择。
[PopupDialog(dialogHead="$avatar_doberm")] 请注意，测试地块的报酬为限时奖励，请尽快完成。
[Delay(time=0.5)]
[Act38D1.FocusSlot(slotId="reward_0_1", slotType="REWARD_BOX")]
[Tutorial(target="btn_act38d1_reward_0_1", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_doberm",           dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 最后请不要忘记，完成通路两侧指标，即可领取通路上的零碎晶块。
```

### guide_act38d1_record

```
[HEADER(is_skippable=false, is_tutorial=true)] act38d1记录查看引导
[Tutorial(waitForSignal="act38d1_map_routed")]
[Tutorial(target="btn_act38d1_map_record", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_doberm",           waitForSignal="act38d1_map_detail_routed", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 恭喜你完成作战，点击此处即可查看本次作战的评分记录。
```


## 统计

- 总字符数：6889
- 对话行数：0


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
