# 明日方舟 · 活动剧情 · act1vautochess（22段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act1vautochess」完整剧情脚本（22个文件，54行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act1vautochess
- 脚本文件数：22

### guide_act1vautochess_cbuff_beg

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess选Buff引导
[Tutorial(waitForSignal="act1vautochess_battle_hud_prepare_enter")]
[PopupDialog(dialogHead="$avatar_amiya")] 为了应对不同种类的敌人，罗德岛准备了许多策略以<@tu.kw>强化干员</>能力。我方会在特定回合获得挑选策略的机会。
[Tutorial(target="btn_act1vautochess_battle_hud_choose_buff_select", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 请确认策略意向，正在复核效用......
[Tutorial(waitForSignal="act1vautochess_battle_hud_choose_buff_selected")]
[Tutorial(target="btn_act1vautochess_battle_hud_choose_buff_confirm", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] ......核对完毕，策略将启用。
```

### guide_act1vautochess_cbuff_end

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess选Buff引导2
[PopupDialog(dialogHead="$avatar_amiya")] 策略获取后将无法再进行更改，请您谨慎选择。
[Tutorial(focusX=0, focusY=-70, focusWidth=1000, focusHeight=130, anchor="Top",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 敌我双方的生命值会实时显示，本模拟的最终<@tu.kw>胜利目标</>是彻底摧毁不同的<@tu.kw>两个势力</>敌人的生命值，将他们的生命值全部降为0。
[Tutorial(focusX=55, focusY=-59, focusWidth=105, focusHeight=89, anchor="TopLeft",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 模拟可以在休整期内随时离开，并通过主页随时回归。
```

### guide_act1vautochess_r1_battle_begin

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess作战开始
[Battle.Pause]
[InputBlocker(blockInput=true)]
[Delay(time=0.5)]
[Tutorial(focusX=0, focusY=-75, focusWidth=350, focusHeight=128, anchor="Top",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 当作战开始时，舰船会生成护盾抵御进攻。请注意，在作战结束时<@tu.kw>护盾值不归零</>可视为作战<@tu.kw>胜利</>。
[PopupDialog(dialogHead="$avatar_amiya")] 由于模拟的底层逻辑与通常作战有所区别，因此在该模拟作战中，干员只会在敌人进入<@tu.kw>初始攻击范围</>时开启技能。
```

### guide_act1vautochess_r1_battle_end

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess战斗结束引导
[PopupDialog(dialogHead="$avatar_amiya")] 作战胜利时，舰船会依据剩余护盾值对敌方生命值<@tu.kw>造成伤害</>，每携带一名干员作战都会增加此伤害。
[PopupDialog(dialogHead="$avatar_amiya")] 罗德岛的数据库中收录了<@tu.kw>诸多地区的敌人</>模型。因此在战斗结束时会看到<@tu.kw>模拟敌人的切换</>，不同敌方势力间会独立计算生命值并<@tu.kw>轮流显示</>。
```

### guide_act1vautochess_r1_battle_gain_coin

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess回合开始获取金币引导
[PopupDialog(dialogHead="$avatar_sys")] 卫戍协议激活，模拟程序已启动。您好，博士，正在为您生成本次将要应对的敌人——
[PopupDialog(dialogHead="$avatar_sys")] 载入中......已为您加载<@tu.kw>两组敌人</>。
```

### guide_act1vautochess_r1_begin

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess进入回合
[Battle.LockAutoChessHud]
[InputBlocker(blockInput=true)]
[Battle.AutoChessOnlyAllow(reqConditionKey="buy_char",bindKey="buy_char", hint="请先完成教程")]
[Delay(time=1)]
[Tutorial(focusX=-375, focusY=20, focusWidth=400, focusHeight=480,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 在卫戍协议中，补给驳船会持续为前线战场运送补给，我们需要<@tu.kw>花费资金</>来采购这些补给。
[Tutorial(tileX=-0.5, tileY=7, focusWidth=158, focusHeight=74,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 在左上角可以查看持有的资金数量。每回合开始时，会<@tu.kw>提供一定量的资金</>用于在驳船上购买补给。
[InputBlocker(blockInput=true, battleTarget="tile_first_shop_char_chess", validWidth=70, validHeight=70)]
[Tutorial(battleTarget="tile_first_shop_char_chess", focusWidth=85, focusHeight=90,           waitForSignal="act1vautochess_shop_item_selected",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 干员将以模拟数据的形式加入作战。请尝试<@tu.kw>购买</>一个干员。
[InputBlocker(blockInput=true)]
[Delay(time=0.2)]
[Tutorial(target="panel_act1vautochess_battle_hud_chess_coin", focusWidth=320, focusHeight=60,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 通常情况下招募干员需要花费<@tu.kw>3资金</>，请选中以查看干员。
[Tutorial(target="btn_act1vautochess_shop_char_menu_buy",           waitForSignal="act1vautochess_battle_item_bought",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击购买将其加入手牌区。
```

### guide_act1vautochess_r1_prepare

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess准备开战
[Battle.LockAutoChessHud]
[InputBlocker(blockInput=true)]
[Battle.AutoChessOnlyAllow(reqConditionKey="disabled",bindKey="prepare_battle", hint="请先完成教程")]
[PopupDialog(dialogHead="$avatar_amiya")]战前准备差不多了。未用完的资金将会被<@tu.kw>清空</>，这部分资金在下回合<@tu.kw>不继承</>。不过请放心，驳船会提供新的资金，并且<@tu.kw>每回合提供的资金也更多</>。
[InputBlocker(blockInput=true, validX=-60, validY=-60, validWidth=75, validHeight=65, anchor="TopRight")]
[Battle.AutoChessOnlyDisable(reqConditionKey="disabled",bindKey="prepare_battle")]
[Battle.UnlockAutoChessHud]
[Battle.AutoChessOnlyAllow(reqConditionKey="round_battle_start", hint="请先开战")]
[Tutorial(focusX=-60, focusY=-60, focusWidth=75, focusHeight=65, anchor="TopRight",           waitForSignal="act1vautochess_battle_prepared",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 现在请点击作战按钮。
```

### guide_act1vautochess_r2_buy_equip

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess购买装备
[Battle.LockAutoChessHud]
[InputBlocker(blockInput=true)]
[Battle.AutoChessOnlyAllow(reqConditionKey="buy_equip",bindKey="buy_equip", hint="请先完成教程")]
[Delay(time=0.2)]
[InputBlocker(blockInput=true, battleTarget="tile_first_shop_equip_chess", validWidth=70, validHeight=70)]
[Tutorial(battleTarget="tile_first_shop_equip_chess", focusWidth=85, focusHeight=90,           waitForSignal="act1vautochess_shop_item_selected",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 驳船提供的补给中包括了各种装备，干员们佩戴在身上后可以获得各种效果。
[InputBlocker(blockInput=true)]
[Delay(time=0.5)]
[Tutorial(target="btn_act1vautochess_shop_char_menu_buy",           waitForSignal="act1vautochess_battle_item_bought",          animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 那么现在，博士，为干员们购买一件装备吧。
```

### guide_act1vautochess_r2_chess_level_up_1

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess购买重复干员1
[Battle.LockAutoChessHud]
[InputBlocker(blockInput=true)]
[Battle.AutoChessOnlyAllow(reqConditionKey="buy_char_shop2_hand1",bindKey="buy_char_shop2_hand1", hint="请先完成教程")]
[Delay(time=0.2)]
[InputBlocker(blockInput=true, battleTarget="tile_second_shop_char_chess", validWidth=70, validHeight=70)]
[Tutorial(battleTarget="tile_second_shop_char_chess", focusWidth=85, focusHeight=90,           waitForSignal="act1vautochess_shop_item_selected",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 本协议采用了模拟模块，因此将会出现复数名相同干员。为博士的作战提供更多抉择。
[InputBlocker(blockInput=true)]
[Delay(time=0.5)]
[Tutorial(target="btn_act1vautochess_shop_char_menu_buy",           waitForSignal="act1vautochess_battle_item_bought",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 现在点请购买第二名重复干员。
```

### guide_act1vautochess_r2_chess_level_up_2

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess购买重复干员2
[Battle.LockAutoChessHud]
[InputBlocker(blockInput=true)]
[Battle.AutoChessOnlyAllow(reqConditionKey="buy_char_shop1_hand2",bindKey="buy_char_shop1_hand2", hint="请先完成教程")]
[Delay(time=0.2)]
[InputBlocker(blockInput=true, battleTarget="tile_third_shop_char_chess", validWidth=70, validHeight=70)]
[Tutorial(battleTarget="tile_third_shop_char_chess", focusWidth=85, focusHeight=90,           waitForSignal="act1vautochess_shop_item_selected",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击第三名重复干员——
[InputBlocker(blockInput=true)]
[Delay(time=0.5)]
[Tutorial(target="btn_act1vautochess_shop_char_menu_buy",           waitForSignal="act1vautochess_battle_item_bought",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] ——并进行购买。
```

### guide_act1vautochess_r2_equip_level_up

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess装备升级
[Battle.LockAutoChessHud]
[InputBlocker(blockInput=true)]
[Battle.AutoChessOnlyAllow(reqConditionKey="buy_equip",bindKey="buy_equip", hint="请先完成教程")]
[Delay(time=0.2)]
[InputBlocker(blockInput=true, battleTarget="tile_first_shop_equip_chess", validWidth=70, validHeight=70)]
[Tutorial(battleTarget="tile_first_shop_equip_chess", focusWidth=85, focusHeight=90,           waitForSignal="act1vautochess_shop_item_selected",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 装备也有更高级的版本，不同的是只需要<@tu.kw>两个</>相同装备即可合并。
[InputBlocker(blockInput=true)]
[Delay(time=0.5)]
[Tutorial(target="btn_act1vautochess_shop_char_menu_buy",           waitForSignal="act1vautochess_battle_item_bought",          animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] ——点击购买。
```

### guide_act1vautochess_r2_shop_level_up

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess商店升级
[Battle.LockAutoChessHud]
[InputBlocker(blockInput=true)]
[Battle.AutoChessOnlyAllow(reqConditionKey="disabled",bindKey="deploy", hint="请先完成教程")]
[Tutorial(focusX=40, focusY=80, focusWidth=1200, focusHeight=130, anchor="Bottom",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这里是手牌区，购买的干员和道具都会存放在这里。
[Battle.SetDragOperationLock(isLocked=true)]
[Battle.SwitchToDefaultUIState]
[Delay(time=0.5)]
[InputBlocker(blockInput=false)]
[Battle.SetDragOperationLock(isLocked=false)]
[Tutorial(waitForSignal="act1vautochess_battle_field_char_putdown", dialogHead="$avatar_amiya", animStyle="Drag",           startBattleTarget="tile_first_hand_char_chess", endTileX=8, endTileY=4)] 干员的部署方式与其他模式没有区别，通过拖拽将干员从手牌区部署至战场。
[Tutorial(waitForSignal="act1vautochess_battle_field_char_build")]
[InputBlocker(blockInput=true)]
[Delay(time=0.5)]
[Tutorial(battleTarget="tile_first_battle_char_chess", focusWidth=85, focusHeight=90,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 已部署的干员可以直接拖拽改变部署位置。
[PopupDialog(dialogHead="$avatar_amiya")] 本回合剩余的资金将被<@tu.kw>清零</>，<@tu.kw>无法留存</>至下一回合。我们需要尽量在回合结束前花费所有资金。让我们看看还有什么能够做的吧。
[Battle.AutoChessOnlyDisable(reqConditionKey="disabled",bindKey="deploy")]
[Battle.AutoChessOnlyAllow(reqConditionKey="ugrade_store", hint="请先完成教程")]
[Delay(time=0.5)]
[InputBlocker(blockInput=true, battleTarget="tile_trap_shop_upgrade", validWidth=70, validHeight=70)]
[Tutorial(battleTarget="tile_trap_shop_upgrade", focusWidth=85, focusHeight=80,           waitForSignal="act1vautochess_util_trap_selected",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 驳船操作员是后勤部的专业干员，可以在操作员处消耗资金来<@tu.kw>升级</>驳船。
[InputBlocker(blockInput=true)]
[Delay(time=0.5)]
[Tutorial(focusX=220, focusY=-170, focusWidth=435, focusHeight=350, anchor="Left",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 随着等级提高，驳船操作员会将更高阶的干员和补给加入补给池。
[Tutorial(target="btn_act1vautochess_shop_char_menu_buy",           waitForSignal="act1vautochess_battle_shop_upgraded",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击按钮即可升级驳船。升级驳船需要消耗资金，请注意，升级驳船所需的资金会随着回合逐渐减少。所以请现在点击按钮进行<@tu.kw>升级</>。
```

### guide_act1vautochess_r2_shop_level_up_2

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess商店升级2
[Battle.LockAutoChessHud]
[Battle.AutoChessOnlyAllow(reqConditionKey="upgrade_store",bindKey="upgrade_store", hint="请先完成教程")]
[Delay(time=0.5)]
[Battle.SwitchToDefaultUIState]
[InputBlocker(blockInput=true, battleTarget="tile_trap_shop_upgrade", validWidth=70, validHeight=70)]
[Tutorial(battleTarget="tile_trap_shop_upgrade", focusWidth=85, focusHeight=90,           waitForSignal="act1vautochess_util_trap_selected",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 还有一些资金剩余，请博士再尝试<@tu.kw>升级一次</>驳船操作员的等级。
[InputBlocker(blockInput=true)]
[Delay(time=0.5)]
[Tutorial(target="btn_act1vautochess_shop_char_menu_buy",           waitForSignal="act1vautochess_battle_shop_upgraded",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 请点击<@tu.kw>升级</>。之后博士可以选择干员并装备上刚刚合成的<@tu.kw>装备</>。准备完毕后，即可点击<@tu.kw>右上角</>的按钮开始作战。
```

### guide_act1vautochess_r2_shop_refresh_2

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess商店刷新2
[Battle.LockAutoChessHud]
[InputBlocker(blockInput=true)]
[Battle.AutoChessOnlyAllow(reqConditionKey="refresh_store",bindKey="refresh_store", hint="请先完成教程")]
[Delay(time=0.5)]
[InputBlocker(blockInput=true, battleTarget="tile_trap_shop_refresh", validWidth=70, validHeight=70)]
[Tutorial(battleTarget="tile_trap_shop_refresh", focusWidth=85, focusHeight=90,           waitForSignal="act1vautochess_util_trap_selected",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这里是补给调配器，罗德岛的物流渠道之一。如果不满意补给的话，点击它就可以消耗资金，补给运输船会为我们<@tu.kw>换一批干员和物资</>。
[InputBlocker(blockInput=true)]
[Delay(time=0.5)]
[Tutorial(target="btn_act1vautochess_shop_char_menu_buy",           waitForSignal="act1vautochess_battle_shop_refreshed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 请点击刷新。
```

### guide_act1vautochess_r2_special_chess_buy

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess特殊招募
[Battle.LockAutoChessHud]
[InputBlocker(blockInput=true)]
[Battle.AutoChessOnlyAllow(reqConditionKey="recruit_char",bindKey="recruit_char", hint="请先完成教程")]
[Tutorial(focusX=-375, focusY=20, focusWidth=400, focusHeight=480,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 使用晋升调配特许后，将在驳船上随机刷新三名比当前驳船等级高一级的干员，您可以免费选择一位加入手牌。
[InputBlocker(blockInput=true, battleTarget="tile_first_shop_char_chess", validWidth=70, validHeight=70)]
[Tutorial(battleTarget="tile_first_shop_char_chess", focusWidth=85, focusHeight=90,           waitForSignal="act1vautochess_shop_item_selected",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击以确认干员。
[Delay(time=0.2)]
[Tutorial(target="btn_act1vautochess_shop_char_menu_buy",           waitForSignal="act1vautochess_battle_item_bought",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击以确认免费获取。
```

### guide_act1vautochess_r2_special_chess_gain

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess使用特殊招募卡
[Battle.LockAutoChessHud]
[InputBlocker(blockInput=true)]
[Battle.AutoChessOnlyAllow(reqConditionKey="use_sp_magic",bindKey="use_sp_magic", hint="请先完成教程")]
[Tutorial(focusX=40, focusY=80, focusWidth=1200, focusHeight=130, anchor="Bottom",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 三位同名干员会自动合并且晋级为<@tu.kw>精锐</>干员，该干员更加强大，且有明显的<@tu.kw>金色</>提示效果。
[Tutorial(battleTarget="tile_first_hand_equip_chess", focusWidth=85, focusHeight=90,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 在干员晋级后，干员所拥有的装备都会自动<@tu.kw>返回手牌区</>，博士可以灵活运用这个机制改变装备策略。
[InputBlocker(blockInput=false)]
[Tutorial(waitForSignal="act1vautochess_special_magic_used", dialogHead="$avatar_amiya", animStyle="Drag",           startBattleTarget="tile_sp_magic_chess",  endTileX=8, endTileY=4)] 三位同名干员合并后，会奖励一张<@tu.kw>晋升调配特许</>，帮助检索经验更丰富的干员。
```

### guide_act1vautochess_r2_wear_equip

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess穿装备
[Battle.LockAutoChessHud]
[InputBlocker(blockInput=true)]
[Battle.AutoChessOnlyAllow(reqConditionKey="wear_equip_not_replace",bindKey="wear_equip_not_replace", hint="请先完成教程")]
[Delay(time=0.2)]
[Battle.SwitchToDefaultUIState]
[Delay(time=0.2)]
[InputBlocker(blockInput=false)]
[Tutorial(waitForSignal="act1vautochess_battle_field_equip_wear_putdown", dialogHead="$avatar_amiya", animStyle="Drag",           startBattleTarget="tile_first_hand_equip_chess", endBattleTarget="tile_battle_char_chess")] 装备拖动到干员身上即可发挥作用，每个干员最多可拥有<@tu.kw>两件</>装备。选定后，装备会<@tu.kw>锁定</>在干员身上，暂时无法取下。
```

### guide_act1vautochess_r3

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess第3回合引导
[Tutorial(waitForSignal="act1vautochess_battle_hud_prepare_enter")]
[PopupDialog(dialogHead="$avatar_amiya")]位于手牌区的模拟干员可以<@tu.kw>出售</>给驳船，出售模拟干员会获得<@tu.kw>1</>资金。装备和法术只能被销毁，无法获得资金。
[Tutorial(target="btn_act1vautochess_battle_hud_enemy_camp_click", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 点击此处可查看所有敌方信息，包括本回合会出现的<@tu.kw>敌人类型</>以及敌人所获得的所有<@tu.kw>加强</>效果等。
[Tutorial(waitForSignal="act1vautochess_battle_hud_enemy_camp_shown")]
[InputBlocker(blockInput=true)]
[Tutorial(focusX=-130, focusY=0, focusWidth=500, focusHeight=360, anchor="Center",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 即将到来的敌人会聚集在上下两个甲板的红色入口前，博士可以根据他们的出现位置调整策略。
[Tutorial(focusX=369, focusY=-447, focusWidth=442, focusHeight=117, anchor="Top",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这里可以查看本局对战中的敌方战术，敌人可能因此获得不同的<@tu.kw>属性强化</>，请博士谨慎应对。
[Tutorial(target="btn_act1vautochess_battle_hud_self_camp_click", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 在查阅完敌方信息后，点击我方信息按钮可返回战场查看我方获得的所有效果。
```

### guide_act1vautochess_shop

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess商品库引导
[Tutorial(waitForSignal="act1vautochess_entry_main_view_routed")]
[Tutorial(target="btn_act1vautochess_main_chess_shop", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 现在，请点击“物资调配处”，对参与协议模拟的干员进行调配。
[Tutorial(waitForSignal="act1vautochess_shop_view_routed")]
[PopupDialog(dialogHead="$avatar_amiya")]本次参与演习的干员被称为目标干员，将在此界面进行调配。已拥有的干员可直接使用，没有任何限制。
[PopupDialog(dialogHead="$avatar_amiya")]若尚未持有目标干员，则会使用以<@tu.kw>精英干员</>为蓝本的原型干员进行补位。当然，也可向好友申请借用目标干员作为填补。
[Tutorial(target="panel_act1vautochess_shop_char_first_level",            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 本模式中不同阶级的干员练度将被限制并固定，阶级越高，其在模拟中发挥的实力便越强。
[Tutorial(target="btn_act1vautochess_shop_level_five_menu_item", searchBtnInChildren=true,          animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 可通过下方的分阶快速跳转定位并进行查看，五六阶的干员将由<@tu.kw>★6干员</>组成，请点击查看。
[Tutorial(waitForSignal="act1vautochess_shop_char_group_five_routed")]
[Tutorial(target="btn_act1vautochess_shop_level_five_diy_card_item",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 本次五六阶干员共开放<@tu.kw>四个甄选干员</>名额。请注意，甄选干员只可放入<@tu.kw>★6干员</>，放入后模拟中的补给池随机范围也将被相应扩大。
[Tutorial(target="btn_act1vautochess_shop_top_quick_assist", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 若当前未持有参加模拟的目标干员，则可借用好友<@tu.kw>设置到助战</>的对应干员以填补。本模式可以向好友选择多位干员以最大程度对缺失干员进行填补，敬请注意。
[Tutorial(target="btn_act1vautochess_shop_menu_trap_item_toggle", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击此处可查看所有可获得的<@tu.kw>装备</>与<@tu.kw>法术</>补给。
```

### guide_act1vautochess_shop_quick_assist

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess商品库快捷助战引导
[Tutorial(waitForSignal="act1vautochess_shop_quick_assist_view_routed")]
[PopupDialog(dialogHead="$avatar_amiya")]已列出所有尚未持有的目标干员，您可以自行选择向好友申请助战，从而对缺失的目标干员位进行填补。
```

### guide_act1vautochess_start

```
[HEADER(is_skippable=false, is_tutorial=true)] act1vautochess开局选分队引导
[Tutorial(waitForSignal="act1vautochess_entry_start_game_view_routed")]
[Tutorial(target="panel_act1vautochess_start_game_enemy_info", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 每次开始模拟后都会从多组敌人势力中随机抽选<@tu.kw>两组</>，每个敌人势力都包含了代表性敌人以及符合其势力描述的多种单位。
[Tutorial(target="btn_act1vautochess_start_game_band_item", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", waitForSignal="act1vautochess_start_game_band_info_displayed")] 可以从已有列表中选择一个策略，本次模拟已为您生成了一个新策略，请选择该策略。
[Tutorial(target="panel_act1vautochess_start_game_band_info", searchBtnInChildren=false,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 选择后您会根据所选策略获得对应开局强化，每种策略的我方生命值与效果都不相同，请在比对后选择最符合您指挥习惯的策略。
[Tutorial(target="btn_act1vautochess_start_game_start_confirm", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 现在，请正式开始本次模拟。
```

### level_act1vautochess_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_rhodescom",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$tech_intro", key="$tech_loop", volume=0.6, crossfade=1, delay=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$d_avg_crwddiscuss_inside", channel="slide", loop=true, volume=0.4)]
[Delay(time=2)]
[charslot]
[charslot(slot = "m", name = "avg_1037_amiya3_1#8$1",focus="m",duration=2)]
[delay(time=3)]
[name="阿米娅"]今天的会议就到这里，各位辛苦了。
[stopsound(channel="slide", fadetime=3)]
[Dialog]
[charslot]
[charslot(slot="m",name="avg_003_kalts_1#2$1",focus="all",duration=0.5)]
[delay(time=3)]
[Dialog]
[charslot]
[charslot(slot="r",name="char_130_doberm_ex#3",focus="all",duration=0.5)]
[charslot(slot="l",name="avg_npc_1300_1#1$1",focus="all",duration=0.5)]
[delay(time=3)]
[Dialog]
[charslot]
[charslot(slot="r",name="avg_391_rosmon_1#2$1",focus="all",duration=0.5)]
[charslot(slot="l",name="char_017_homura_3#1",focus="all",duration=0.5)]
[delay(time=3)]
[charslot]
[charslot(slot = "m", name = "avg_1037_amiya3_1#8$1",focus="m")]
[name="阿米娅"]离开的时候别把水杯落在这里哦~ 
[dialog]
[charslot]
[Dialog]
[charslot]
[charslot(slot="r",name="char_130_doberm_ex",focus="all")]
[charslot(slot="l",name="avg_npc_1300_1#2$1",focus="all")]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=2)]
[delay(time=2)]
[Dialog]
[charslot]
[charslot(slot="r",name="avg_391_rosmon_1#9$1",focus="all")]
[charslot(slot="l",name="char_017_homura_3#7",focus="all")]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=2)]
[delay(time=3)]
[Dialog]
[charslot]
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="all")]
[delay(time=3)]
[charslot]
[charslot(slot = "m", name = "avg_1037_amiya3_1#7$1",focus="m")]
[name="阿米娅"]凯尔希医生，可露希尔小姐还没到，我们要再等等吗？
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]博士的时间也不充裕，我们先开始吧。
[Dialog]
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="n")]
[Decision(options="要我留下有什么事？;需要我做什么？;......", values="1;2;3")]
[Predicate(references="1;2;3")]
[charslot(slot="m",name="avg_003_kalts_1#3$1",focus="m")]
[name="凯尔希"]只是对于强化罗德岛防卫体系的一些想法。
[charslot(slot="m",name="avg_003_kalts_1#3$1",focus="m")]
[name="凯尔希"]因为具体措施仍在可行性测试阶段，还没成熟到可以拿来公开讨论，所以我们先在小范围内进行闭门会议。
[charslot(slot="m",name="avg_003_kalts_1#3$1",focus="m")]
[name="凯尔希"]罗德岛需要你的意见作为参考。
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]阿米娅，向博士简单介绍一下吧。
[charslot(slot = "m", name = "avg_1037_amiya3_1#8$1",focus="m")]
[name="阿米娅"]好的，凯尔希医生。
[charslot(slot = "m", name = "avg_1037_amiya3_1#8$1",focus="m")]
[name="阿米娅"]这是相关的资料，博士。
[dialog]
[charslot]
[playsound(key="$d_avg_paper1",volume=0.8)]
[delay(time=1.2)]
[charslot(slot = "m", name = "avg_1037_amiya3_1#1$1",focus="m")]
[name="阿米娅"]根据我们之前应对袭击事件总结的经验，罗德岛在内外防卫方面都进行了优化调整。
[charslot(slot = "m", name = "avg_1037_amiya3_1#1$1",focus="m")]
[name="阿米娅"]从伦蒂尼姆事件中的反馈来看，这些调整是相当有效的。
[charslot(slot = "m", name = "avg_1037_amiya3_1#1$1",focus="m")]
[name="阿米娅"]在大量人手前去支援伦蒂尼姆的情况下，剩下的干员们仍能组织起来，对小型暴乱进行有效反击以确保罗德岛本舰的安全。
[charslot(slot = "m", name = "avg_1037_amiya3_1#1$1",focus="m")]
[name="阿米娅"]这也是凯尔希医生考虑进一步强化罗德岛防卫体系的主要原因......
[charslot(slot = "m", name = "avg_1037_amiya3_1#1$1",focus="m")]
[name="阿米娅"]在遭遇舰船级别的袭击时，本舰当然更倾向于在战斗发生前通过舰船自身的侦察手段或速度优势躲避攻击。
[charslot(slot = "m", name = "avg_1037_amiya3_1#1$1",focus="m")]
[name="阿米娅"]只是，到了万不得已的时刻，罗德岛也需要干员们做好准备，在外层平台上与敌人进行接舷战。
[dialog]
[charslot]
[playsound(key="$d_avg_paper1",volume=0.8)]
[delay(time=1.2)]
[charslot(slot = "m", name = "avg_1037_amiya3_1#8$1",focus="m")]
[name="阿米娅"]详细情况资料上也写得很清楚了，博士。如果还有疑问的话，我想凯尔希医生会很乐意为您解答的。
[dialog]
[charslot]
[playsound(key="$d_avg_paper1",volume=0.8)]
[delay(time=1.2)]
[Dialog]
[Decision(options="凯尔希，你确定这份文件是可行性研讨吗？", values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]怎么了？
[Dialog]
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="n")]
[Decision(options="罗德岛对外行动遭遇的敌人已经全部录入了。;这份是执行资料，不是训练预案，对吗？;精英干员都已知晓并参与计划，这还不成熟？", values="1;2;3")]
[Predicate(references="1;2;3")]
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]方案的详尽程度并不影响它仍需研讨的事实。
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]即使于我个人而言，这份防卫计划已经有相当的完成度。
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]但我更需要你，还有阿米娅，了解我的想法，并在这之上提出自己的意见。
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]毕竟最终执行它的人，并不是我。
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]所以，但凡有任何无法理解的部分，都可以指出来，我会进一步为你说明。
[Dialog]
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="n")]
[Decision(options="这份资料写得很清楚，凯尔希。;凯尔希，我看不懂！", values="1;2")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_003_kalts_1#2$1",focus="m")]
[name="凯尔希"]很好，我会尽快安排后续模拟环节。
[Predicate(references="2")]
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]......阿米娅，今天博士还有空闲时间吗？
[charslot(slot = "m", name = "avg_1037_amiya3_1#5$1",focus="m")]
[name="阿米娅"]博士今天的会议已经排得很满了，凯尔希医生，只有睡前还——
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]稍后我会预约那个时间段的会议室，帮助你消化资料里的所有内容。
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]阿米娅，麻烦你也一起来。
[charslot(slot = "m", name = "avg_1037_amiya3_1#8$1",focus="m")]
[name="阿米娅"]好的。
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_003_kalts_1#3$1",focus="m")]
[name="凯尔希"]......
[charslot(slot="m",name="avg_003_kalts_1#3$1",focus="m")]
[name="凯尔希"]可露希尔呢，会议邀请两小时前就发送给她了。
[dialog]
[charslot]
[PlaySound(key="$rungeneral", volume=0.4)]
[delay(time=1)]
[PlaySound(key="$d_gen_dooropen",volume=1)]
[Delay(time=0.4)]
[charslot(slot="m",name="avg_npc_411_1#5$1",focus="m",duration=1)]
[delay(time=2)]
[Dialog]
[charslot(slot="m",name="avg_npc_411_1#5$1",focus="n")]
[Decision(options="你来了，可露希尔。;会议结束了哦。;......（指了指时钟）", values="1;2;3")]
[Predicate(references="1;2;3")]
[charslot(slot="m",name="avg_npc_411_1#7$1"

... (全文8748字符)
```


## 统计

- 总字符数：31112
- 对话行数：54


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
