# 明日方舟 · 活动剧情 · act1autochess（14段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act1autochess」完整剧情脚本（14个文件，0行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act1autochess
- 脚本文件数：14

### guide_auto_chess_mode_training_1_band

```
[HEADER(is_skippable=false, is_tutorial=true, dont_clear_gameobjectpool_onstart = true)] 自走棋赛季-分队轮选介绍
[Tutorial(waitForSignal="auto_chess_band_routed")]
[Tutorial(target="auto_chess_band_player_list", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya")] 模拟正式开始之前，会以随机顺序进行策略轮选，顺序会显示在左侧，似乎已经有人选好了呢！
[Tutorial(target="auto_chess_band_item", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya")] 博士可以在另一侧看到所有可选的策略标识，我们也选择一个策略试一试吧！
[AutoChess.FocusBand()]
[Tutorial(target="auto_chess_band_detail", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya")] 选择策略之后，博士可以在这里确认策略提供的初始生命值以及特殊效果，后者在整场模拟中会一直生效。
[Tutorial(target="auto_chess_band_confirm_btn", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya")] 这个策略应该很不错，博士，我们就选它吧！
```

### guide_auto_chess_mode_training_1_entry

```
[HEADER(is_skippable=false, is_tutorial=true)] 自走棋赛季-活动入口
[Activity.ResetToEntry]
[Tutorial(waitForSignal="template_act_entry_routed")]
[PopupDialog(dialogHead="char_002_amiya")] 博士，欢迎来到卫戍协议模拟训练场！
[Tutorial(target="auto_chess_start_btn", waitForSignal="auto_chess_mode_choice_routed", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya")] 在这里，博士可以和队友进行模拟训练，我们这就去联合模拟的场地看看吧！
[Tutorial(target="auto_chess_mode_list", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya")] 卫戍协议有着多种不同的模拟难度，高难度模拟中敌人攻击的强度更高，作战环境更加艰难，但奖励也会更加丰厚。
[Tutorial(target="auto_chess_mode_start_btn", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya")] 现在，我们开始实际模拟看看吧！
```

### guide_auto_chess_mode_training_1_r1_deploy

```
[HEADER(is_skippable=false, is_tutorial=true, dont_clear_gameobjectpool_onstart = true)] 卫戍战斗-第一回合休整期
[InputBlocker(blockInput=true)]
[Battle.SwitchToDefaultUIState]
[Delay(time=0.5)]
[InputBlocker(blockInput=false)]
[Battle.SetDragOperationLock(isLocked=false)]
[Tutorial(waitForSignal="signal_auto_chess_battle_place_on_battlefield",           dialogHead="$avatar_amiya", animStyle="Drag",           startBattleTarget="key_auto_chess_first_valid_hand_tile", endTileX=4, endTileY=12, posX=4, posY=12)] 博士应该很熟悉部署干员的方式吧？没错！只要<@tu.kw>拖拽干员</>就可以把他们从整备区部署到战场区。
```

### guide_auto_chess_mode_training_1_r1_prepare

```
[HEADER(is_skippable=false, is_tutorial=true)] 卫戍战斗-第一回合休整期
[InputBlocker(blockInput=true)]
[PopupDialog(dialogHead="$avatar_amiya")]博士，我们已经接入模拟指挥系统了。接下来，我们需要抵御敌人多个回合的进攻，最后战胜敌方领袖。让我来为你介绍一下模拟训练中的各种操作吧！
[Tutorial(target="key_auto_chess_shop_btn_switch_fold", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 每次进入新的回合，博士都会获得一定量的<@tu.kw>资金</>用于调度干员或购买装备，一定要合理利用哦！
[Tutorial(target="key_auto_chess_first_card_in_shop", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 在这里，干员将以模拟数据的形式参与战斗，先试着用资金调度一位干员吧。
[Tutorial(focusX=216, focusY=-94, focusWidth=432, focusHeight=142, anchor="Left",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 博士你看，模拟中干员具有可在不同时机触发的<@tu.kw>特质</>，有效利用这些特质是达成完美作战的关键。
[Tutorial(target="key_auto_chess_first_card_in_shop", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 就选择调度这位干员吧~
[Tutorial(battleTarget="key_auto_chess_hand_tile", focusWidth=850, focusHeight=80,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这里是<@tu.kw>整备区</>，是干员的待命场地，也是装备的存放处。
```

### guide_auto_chess_mode_training_1_r1_refresh

```
[HEADER(is_skippable=false, is_tutorial=true, dont_clear_gameobjectpool_onstart = true)] 卫戍战斗-第一回合休整期
[InputBlocker(blockInput=true)]
[Delay(time=0.5)]
[InputBlocker(blockInput=true)]
[Tutorial(battleTarget="key_auto_chess_battle_chess_tile", focusWidth=85, focusHeight=90,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 另外，博士也可以直接拖拽已经部署完毕的干员来改变他们的作战位置。
[Tutorial(target="key_auto_chess_first_bond_in_hud", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 看，博士！场上部署干员后，他的<@tu.kw>盟约</>就会显现，不过我们现在还没有<@tu.kw>激活盟约</>，只有场上归属于相同盟约的干员<@tu.kw>人数达标</>之后，盟约才能被激活。
[PopupDialog(dialogHead="$avatar_amiya")]博士，我们还有剩余的资金，这些资金<@tu.kw>不能留到下一回合</>。让我们来看看还有什么事情可以做吧！
[Tutorial(target="key_auto_chess_shop_btn_refresh", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 我们可以花费资金来<@tu.kw>刷新</>调度中心，刷新之后调度中心的干员及装备会被替换，博士，试试看吧~
[Tutorial(target="key_auto_chess_btn_prep_ready", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 现在，我们已经没有剩余的可用资金了，开始作战吧！
```

### guide_auto_chess_mode_training_1_r2_active

```
[HEADER(is_skippable=false, is_tutorial=true, dont_clear_gameobjectpool_onstart = true)] 卫戍战斗-第二回合休整期
[InputBlocker(blockInput=true)]
[Delay(time=0.4)]
[Tutorial(target="key_auto_chess_first_bond_in_hud", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 只要部署人数满足条件，盟约就能<@tu.kw>激活</>，给我们带来战斗中的各种<@tu.kw>效果加成</>，盟约可以在整场模拟中<@tu.kw>多次叠加</>，层数越多，它的效果就越强。
[Tutorial(target="key_auto_chess_shop_btn_upgrade", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 另外，除了晋级干员，我们也可以使用资金<@tu.kw>升级</>调度中心，从而获取<@tu.kw>更高</>等级的干员。
[Tutorial(target="key_auto_chess_shop_btn_upgrade", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 调度中心升级后，会解锁更多栏位。如果博士手头没有足够的资金也不必担忧，升级调度中心所需的资金每一回合都会减少。
[Tutorial(target="key_auto_chess_btn_prep_ready", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这一回合的休整就到此为止，博士，再次开始战斗吧！
```

### guide_auto_chess_mode_training_1_r2_battle

```
[HEADER(is_skippable=false, is_tutorial=true)] 卫戍战斗-第二回合补漏
[PopupDialog(dialogHead="$avatar_amiya")]如果有入侵的敌人突破了防线？别担心，在模拟中博士并不是孤军奋战！
[PopupDialog(dialogHead="$avatar_amiya")]模拟中只要有队友达成完美作战，就可以前来进行<@tu.kw>联防</>，联防成功的话，将不会扣除我方的生命值。
[PopupDialog(dialogHead="$avatar_amiya")]在<@tu.kw>作战时间结束</>时，如果战场中存在<@tu.kw>仍未被击杀</>的敌人，就无法达成完美作战。
```

### guide_auto_chess_mode_training_1_r2_deploy

```
[HEADER(is_skippable=false, is_tutorial=true, dont_clear_gameobjectpool_onstart = true)] 卫戍战斗-第二回合休整期
[InputBlocker(blockInput=true)]
[Battle.SwitchToDefaultUIState]
[Delay(time=0.5)]
[InputBlocker(blockInput=false)]
[Battle.SetDragOperationLock(isLocked=false)]
[Tutorial(waitForSignal="signal_auto_chess_battle_place_on_battlefield",           dialogHead="$avatar_amiya", animStyle="Drag",           startBattleTarget="key_auto_chess_upgrade_bonus_chess_tile", endTileX=4, endTileY=11, posX=4, posY=11)] 之前提到过，想要<@tu.kw>激活盟约</>的话，需要部署一定数量的对应干员。事不宜迟，我们快部署干员上场吧！
```

### guide_auto_chess_mode_training_1_r2_prepare

```
[HEADER(is_skippable=false, is_tutorial=true)] 卫戍战斗-第二回合休整期
[InputBlocker(blockInput=true)]
[Tutorial(waitForSignal="signal_auto_chess_battle_shop_ui_registered")]
[Tutorial(target="key_auto_chess_first_card_in_shop", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 博士应该注意到了，因为采用模拟数据，调度中心里出现了多个同名的干员。获取了三位同名干员之后，该干员就会自动<@tu.kw>晋级</>，博士可以试着选择一位已有干员的同名干员——
[Tutorial(target="key_auto_chess_first_card_in_shop", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 接着确认购买。
[Tutorial(target="key_auto_chess_second_card_in_shop", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 然后再选择一次同名干员——
[Tutorial(target="key_auto_chess_second_card_in_shop", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 执行同样的操作。
[Delay(time=0.2)]
[Tutorial(battleTarget="key_auto_chess_battle_chess_tile", focusWidth=85, focusHeight=90,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这样，我们就获得了自动<@tu.kw>晋级</>之后的精锐干员。精锐干员拥有更强的战斗属性，能在模拟中发挥更大的作用。
[Tutorial(target="key_auto_chess_first_card_in_shop", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 每次晋级干员，博士都可以<@tu.kw>免费获取</>一位比当前调度中心等级<@tu.kw>高出一级</>的干员。
[Tutorial(focusX=216, focusY=-94, focusWidth=432, focusHeight=142, anchor="Left",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 博士也要注意，部分干员拥有可以为盟约<@tu.kw>叠加层数</>的特质，这些特质能够强化盟约的效果。
[Tutorial(focusX=216, focusY=-94, focusWidth=432, focusHeight=142, anchor="Left",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] <@tu.kw>特质</>带来的<@tu.kw>叠加层数</>效果能让我们的阵容不断变强，这在卫戍协议的模拟中拥有非常重要的意义，博士一定要重点关注并多加利用这些特质！
[Tutorial(target="key_auto_chess_first_card_in_shop", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 但无论可免费获取的干员特质如何，奖励干员在刷新调度中心后无法保留，博士不要错过获取奖励的机会哦~
```

### guide_auto_chess_mode_training_1_r3_prepare

```
[HEADER(is_skippable=false, is_tutorial=true)] 卫戍战斗-第三回合休整期
[Tutorial(protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 在特定回合的休整期会出现机变阶段，这时会有许多额外内容供大家轮流挑选。
[Tutorial(target="key_auto_chess_first_avail_effect_expand", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 每项额外内容只能选择一次，不能重复选择，所有参与者都选择完毕后，机变阶段就会结束。博士，这次我们就先选这个吧！
[Delay(time=0.4)]
[Tutorial(target="key_auto_chess_first_avail_effect_confirm", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y",           waitForSignal="signal_auto_chess_battle_enter_prepare_main_state")] 确认选择！
[Delay(time=0.5)]
[Tutorial(battleTarget="key_auto_chess_equip_tile", focusWidth=85, focusHeight=90,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这样我们挑选的装备就已经存放到整备区了，接下来只要<@tu.kw>拖拽它并放置到干员身上</>，就可以完成装备配置了，试一试吧博士！
[Tutorial(target="key_auto_chess_first_mate_in_list", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 博士可以在下一个休整期开始之前，通过<@tu.kw>点击队友头像</>前往其场地，查看他们的作战情况。
```

### guide_auto_chess_mode_training_1_r4_prepare

```
[HEADER(is_skippable=false, is_tutorial=true)] 卫戍战斗-第四回合休整期
[PopupDialog(dialogHead="$avatar_amiya")]在最后一个回合，也就是最终攻势阶段，我们将会<@tu.kw>直面敌方领袖</>。此时整个队伍的生命值会<@tu.kw>合并</>，我们将协力应对这个最强大的敌人！
[PopupDialog(dialogHead="$avatar_amiya")]在这个阶段，参与者将被<@tu.kw>两两分组</>，每一组都会进入一个合并场地进行协同战斗。与敌方领袖作战过程中，盟约层数叠加也将禁用。
[Delay(time=0.5)]
[Tutorial(battleTarget="key_auto_chess_boss_tile", focusWidth=300, focusHeight=200,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 小心！作战期开始后敌方领袖就会发起进攻。博士，请快做好准备，和队友一起应对这场决战吧！
```

### guide_auto_chess_mode_training_1_stage_info

```
[HEADER(is_skippable=false, is_tutorial=true, dont_clear_gameobjectpool_onstart = true)] 自走棋赛季-本局信息介绍
[Tutorial(waitForSignal="auto_chess_stage_info_routed")]
[PopupDialog(dialogHead="char_002_amiya")] 博士，在卫戍协议中，每一次模拟的战场环境都会发生随机改变，我们先来确认一下模拟的一些基础信息吧！
[AutoChess.FocusStageInfo(itemType = "ENEMY")]
[Tutorial(target="auto_chess_stage_info_enemy", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya", dialogY="$f_lower_dialog_pos_y")] 模拟的最终目标是击败敌方领袖，在这里会显示本次模拟中敌方领袖的信息，以及其带领队伍的构成，博士一定要小心应对。
[AutoChess.FocusStageInfo(itemType = "TEMP_BOND_TITLE")]
[Tutorial(target="auto_chess_stage_info_season_bond_title", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya", dialogY="$f_lower_dialog_pos_y")] 盟约在模拟中非常重要，可以为战斗提供多种加成效果，博士可以通过部署特定的干员来激活与其对应的盟约。
[AutoChess.FocusStageInfo(itemType = "BOND")]
[Tutorial(target="auto_chess_stage_info_season_bond_group", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya", dialogY="$f_lower_dialog_pos_y")] 每次模拟中，都将<@tu.kw>随机部分</>盟约可用。在这里可以分别查看核心盟约与附加盟约的随机结果。
[Tutorial(target="auto_chess_stage_info_season_bond_active_item", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya", dialogY="$f_lower_dialog_pos_y")] 盟约图标点亮意味着这一次模拟中该盟约可以正常激活。
[Tutorial(target="auto_chess_stage_info_season_bond_inactive_item", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya", dialogY="$f_lower_dialog_pos_y")] 而盟约图标置灰代表归属于该盟约的部分干员<@tu.kw>不会进入调度中心</>，因此该盟约在本次模拟中极难激活。
[AutoChess.FocusStageInfo(itemType = "CHESS")]
[Tutorial(target="auto_chess_stage_info_season_chess_group", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya", dialogY="$f_lower_dialog_pos_y")] 在这里，博士可以查看不会出现在本次模拟中的干员。
[Tutorial(target="auto_chess_stage_info_confirm_btn", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya")] 这就是卫戍协议模拟训练的所有注意事项了。看起来已经有队友在等着我们了，博士，我们也点击这里准备模拟吧！
```

### guide_auto_chess_shop_home

```
[HEADER(is_skippable=false, is_tutorial=true)] 自走棋商品库引导
[Activity.ResetToEntry]
[Tutorial(waitForSignal="template_act_entry_routed")]
[Tutorial(target="auto_chess_shop_btn", searchBtnInChildren=false,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_002_amiya")] 博士可以点击这里，查看模拟中可供调度的干员与资源的相关信息哦~
[Tutorial(waitForSignal="auto_chess_shop_view_routed")]
[PopupDialog(dialogHead="$avatar_amiya")]本次参与模拟的干员被称为<@tu.kw>预设干员</>，将在此界面进行调配。已拥有的干员可以直接使用，没有任何限制。
[PopupDialog(dialogHead="$avatar_amiya")]若尚未持有预设干员，则会使用以<@tu.kw>精英干员</>为蓝本的原型干员进行补位。当然，也可向好友申请借用干员作为填补。
[Tutorial(target="panel_auto_chess_shop_char_first_level",            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 卫戍协议中不同阶级的干员练度将被限制并固定，阶级越高，其在模拟中发挥的实力便越强。
[Tutorial(target="panel_auto_chess_shop_char_first_level_char_item_click_part",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 模拟中每位非自选干员都具备独特的能力，可点击干员进行查看。
[Tutorial(waitForSignal="auto_chess_shop_char_detail_routed")]
[Tutorial(target="panel_auto_chess_shop_char_detail_status_switch",            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 同一干员存在初始和精锐两种状态，在模拟中通过合并三位相同干员可将干员从初始状态晋级为精锐状态，解锁使用模组的能力。
[AutoChess.ShopDetailFocus(type="garrison")]
[Tutorial(target="panel_auto_chess_shop_char_detail_garrison",            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 协议模拟中的干员具备的特质将在不同的时机下触发。
[AutoChess.ShopDetailFocus(type="bond")]
[Tutorial(target="panel_auto_chess_shop_char_detail_bond",            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 有效使用特质可以强化盟约效果，活用盟约可以极大增强博士在模拟中的实力。
[Tutorial(target="panel_auto_chess_shop_char_detail_confirm",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 现在，请点击确认并返回上一级界面。
[Tutorial(waitForSignal="auto_chess_shop_view_routed")]
[Tutorial(target="btn_auto_chess_shop_level_five_menu_item", searchBtnInChildren=true,          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 博士可以随时点击下方的快捷跳转栏，查看不同等级的调度中心内可出现的干员，现在点击下方的五阶按钮尝试一下。
[AutoChess.ShopListFocusDiyChess]
[Tutorial(target="btn_auto_chess_shop_level_five_diy_card_item",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 本次五六阶干员开放<@tu.kw>两个</>自选编队干员的名额，需要注意的是，自选编队仅可放置<@tu.kw>六星干员</>，在放入后调度中心随机资源的范围将被扩大。
[Tutorial(target="btn_auto_chess_shop_top_quick_assist", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 若当前未持有参加模拟的预设干员，则可借用好友<@tu.kw>设置到助战</>的对应干员以填补。本模式可以向好友借用<@tu.kw>多位</>干员以最大程度对缺失干员进行填补，敬请注意。
[Tutorial(target="btn_auto_chess_shop_menu_trap_item_toggle", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击此处可切换查看所有可在调度中心获得的<@tu.kw>装备</>。
```

### guide_auto_chess_shop_quick_assist

```
[HEADER(is_skippable=false, is_tutorial=true)] 自走棋商品库快捷助战引导
[Tutorial(waitForSignal="auto_chess_shop_quick_assist_view_routed")]
[PopupDialog(dialogHead="$avatar_amiya")]已列出所有尚未持有的预设干员，您可以自行选择向好友申请助战，从而对缺失的预设干员位进行填补。
```


## 统计

- 总字符数：18799
- 对话行数：0


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
