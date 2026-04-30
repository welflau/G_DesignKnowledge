# 明日方舟 · 活动剧情 · act1arcade（6段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act1arcade」完整剧情脚本（6个文件，0行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act1arcade
- 脚本文件数：6

### training_act1arcade_m1_01_a

```
[HEADER(is_tutorial=true, is_skippable=false, is_autoable=false)]电玩城黄金矿工模式教学关1_a
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.LockFunction(mask="CHARACTER_INFO")]
[Battle.LockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true, black=0.2)]
[Battle.SwitchToDefaultUIState]
[Battle.Pause]
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 【超级钩爪】通关指南
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 在超级钩爪中，玩家的目标是通过将<@tu.kw>敌人抓进坑洞中</>来获取尽可能多的关卡得分。
[Battle.EnsureMinSp(charId="trap_192_archook", sp=5)]
[Tutorial(tileX=5, tileY=6, focusWidth=100, focusHeight=150,          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",          protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 钩爪会不停摆动，在<@tu.kw>合适的时机</>释放钩爪即可抓取敌人。
[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true, tileX=5,tileY=6, validWidth=100, validHeight=150)]
[Tutorial(tileX=5, tileY=6, focusWidth=100, focusHeight=150,          animStyle="Click", focusStyle="HighlightCircle",waitForSignal="char_info", charId="trap_192_archook", black="$f_tut_black",          protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 现在正是好时机，准备开启钩爪的技能吧。
[Battle.LockFunction(mask="CHARACTER_INFO")]
[Battle.LockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true)]
[Tutorial(target="btn_skill", waitForSignal="use_skill",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 就是现在，释放钩爪！
[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true)]
[Battle.Delay(time=1)]
[Battle.Pause]
[PopupDialog(dialogHead="$avatar_sys")]成功将敌人拉进了坑洞中！玩家会获得和敌人<@tu.kw>重量</>相对应的关卡得分。注意，有些免疫失衡的敌人是无法被钩爪拉动的。
[Battle.Pause(pause=false)]
[Battle.Delay(time=0.4)]
[Battle.Pause]
[Battle.EnsureMinSp(charId="trap_187_arcgacha", sp=30)]
[InputBlocker(blockInput=true, tileX=4, tileY=6, validWidth=105, validHeight=111)]
[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[Tutorial(tileX=4, tileY=6, focusWidth=108, focusHeight=111,           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", waitForSignal="char_info", charId="trap_187_arcgacha",           protectTime=0.5, dialogHead="$avatar_sys",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 扭蛋机里有很多好用的道具，博士可以开启技能试试手气，并且在游戏中得分还会<@tu.kw>加速扭蛋机的充能</>哦。
[Battle.LockFunction(mask="CHARACTER_INFO")]
[Battle.LockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true)]
[Delay(time=0.3)]
[Tutorial(target="btn_skill", waitForSignal="use_skill",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")]先抽一个试试吧！
[Battle.Pause(pause=false)]
[Battle.Delay(time=1)]
[Battle.Pause]
[Tutorial(focusX=-50, focusY=90, focusWidth=100, focusHeight=150, anchor="BottomRight",          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",          protectTime=0.5, dialogHead="$avatar_sys")]是超时空电话亭。它可以呼叫一些神奇的敌人出场，击败他们可获取<@tu.kw>更高的关卡得分</>。
[InputBlocker(blockInput=false)]
[Tutorial(tileX=5, tileY=1, focusWidth=108, focusHeight=111, waitForSignal="put_down", charId="trap_190_arcsum3",           animStyle="Drag", startCardIndex=0, startRightStart=true, endTileX=8, endTileY=3, dialogHead="$avatar_sys",          focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5)] 将超时空电话亭部署在任意地块即可触发效果。
[Battle.Pause(pause=false)]
[Battle.Delay(time=5)]
[Battle.Pause]
[InputBlocker(blockInput=true)]
[Tutorial(tileX=2, tileY=7, focusWidth=100, focusHeight=150,          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",          protectTime=0.5, dialogHead="$avatar_sys")]看，大鲍勃接到电话出场了！  
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 除此之外，扭蛋机中还有很多神奇的支援道具，留待博士在接下来的游戏中一一探索。  
[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
```

### training_act1arcade_m2_01_a

```
[HEADER(is_tutorial=true, is_skippable=false, is_autoable=false)] 电玩城喷泉大战教学_a
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.LockFunction(mask="CHARACTER_INFO")]
[Battle.LockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true, black=0.2)]
[Battle.SwitchToDefaultUIState]
[Battle.Pause]
[popupdialog(dialogHead="$avatar_sys")]【喷泉大战】通关指南
[popupdialog(dialogHead="$avatar_sys")]在喷泉大战中，玩家的目标是尽可能多地在地块上铺上纯白水汽，【大战记分站】在技能开启时会按场上的<@tu.kw>纯白水汽数量</>进行记分。
[Tutorial(tileX=4, tileY=4, focusWidth=108, focusHeight=111,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", anchor="Center",           protectTime=0.5, dialogHead="$avatar_sys")] 博士，这个喷泉是不是非常眼熟？
[Tutorial(tileX=4, tileY=4, focusWidth=108, focusHeight=111,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", anchor="Center",           protectTime=0.5, dialogHead="$avatar_sys")] 这是在游戏中复现的汐斯塔的景观喷泉，<@tu.kw>部署在它四周</>的干员在攻击地面敌人时能在敌人脚下生成纯白水汽。
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 在喷泉大战中，玩家并不需要把敌人全部消灭，敌人到达目标点后也<@tu.kw>不会扣除关卡生命值</>。
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 玩家只需要尽可能在更多的地块上铺上纯白水汽，就能获得更高的关卡得分。
[Tutorial(tileX=5, tileY=4, focusWidth=108, focusHeight=111,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", anchor="Center",           protectTime=0.5, dialogHead="$avatar_sys")] 博士，请先试着在喷泉旁部署干员作战，给地块铺上纯白水汽吧。	
[Battle.Pause(pause=false)]
[Battle.Delay(time=1)]
[Battle.Pause(pause=true)]
[Battle.EnsureMinSp(charId="trap_187_arcgacha", sp=30)]
[InputBlocker(blockInput=true, tileX=1, tileY=3, validWidth=105, validHeight=111)]
[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[Tutorial(tileX=1, tileY=3, focusWidth=108, focusHeight=111,           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", waitForSignal="char_info", charId="trap_187_arcgacha",           protectTime=0.5, dialogHead="$avatar_sys",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 另外，扭蛋机里面也添加了新的支援道具。
[Battle.LockFunction(mask="CHARACTER_INFO")]
[Battle.LockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true)]
[Delay(time=0.3)]
[Tutorial(target="btn_skill", waitForSignal="use_skill",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 博士可以先抽一个试试。
[Battle.Pause(pause=false)]
[Battle.Delay(time=1)]
[Battle.Pause(pause=true)]
[Tutorial(cardIndex=0, focusWidth=100, focusHeight=100, rightStart=true,           animStyle="Highlight", focusStyle="HighlightCircle", black=0.5,           protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 是游戏中最新推出的道具口渴乐乐！
[InputBlocker(blockInput=false)]
[Tutorial(waitForSignal="put_down",charId="trap_194_arcsoda", posX=8, posY=1,endTileX=8, endTileY=1, dialogHead="$avatar_sys", animStyle="Drag", startCardIndex=0, startRightStart=true)] 博士可以把它部署到不太容易铺上纯白水汽的区域。
[Battle.Pause(pause=false)]
[Battle.Delay(time=0.5)]
[Battle.Pause(pause=true)]
[InputBlocker(blockInput=true, black=0.2)]
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 口渴乐乐被干员<@tu.kw>打破</>以后会为周围的地块铺上纯白水汽。
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 博士，请尽情利用这些道具来获取更高的关卡得分吧。
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
```

### training_act1arcade_m2_01_b

```
[HEADER(is_tutorial=true, is_skippable=false, is_autoable=false)] 电玩城喷泉大战教学_b
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.LockFunction(mask="CHARACTER_INFO")]
[Battle.LockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true, black=0.2)]
[Battle.SwitchToDefaultUIState]
[Battle.Pause(pause=true)]
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 注意，纯白水汽在场地上生成后，玩家并<@tu.kw>不能直接获得关卡得分</>。
[Battle.EnsureMinSp(charId="trap_193_arctoll", sp=25)]
[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true, tileX=1, tileY=5, validWidth=108, validHeight=111)]
[Tutorial(tileX=1, tileY=5, focusWidth=108, focusHeight=111, waitForSignal="char_info", charId="trap_193_arctoll",          animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", anchor="Center",           protectTime=0.5, dialogHead="$avatar_sys")] 玩家需要通过【大战记分站】来进行记分。
[Battle.LockFunction(mask="CHARACTER_INFO")]
[Battle.LockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true)]
[Delay(time=0.3)]
[InputBlocker(blockInput=true)]
[Tutorial(target="btn_skill", waitForSignal="use_skill",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 它会在技能开启后会记分。
[Tutorial(tileX=1, tileY=5, focusWidth=108, focusHeight=111,           focusStyle="HighlightCircle", black="$f_tut_black", anchor="Center",           protectTime=0.5, dialogHead="$avatar_sys")] 偷偷告诉博士一个秘密，随着水汽数量的增加，每个水汽获得的关卡得分也会<@tu.kw>递增</>。
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
```

### training_act1arcade_m2_01_c

```
[HEADER(is_tutorial=true, is_skippable=false, is_autoable=false)] 电玩城喷泉大战教学_c
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[InputBlocker(blockInput=true, black=0.2)]
[Battle.SwitchToDefaultUIState]
[Battle.Pause(pause=true)]
[Tutorial(tileX=7, tileY=1, focusWidth=108, focusHeight=111,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", anchor="Center",           protectTime=0.5, dialogHead="$avatar_sys")] 快看，喷泉“汽水侠”来了！
[Tutorial(tileX=7, tileY=1, focusWidth=108, focusHeight=111,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", anchor="Center",           protectTime=0.5, dialogHead="$avatar_sys")] 喷泉“汽水侠”喜欢和纯白水汽玩耍，每次经过纯白水汽时都会带来<@tu.kw>额外关卡得分</>。
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 博士，可以<@tu.kw>提前</>在喷泉“汽水侠”路线上铺上纯白水汽哦。
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
```

### training_act1arcade_m3_01_a

```
[HEADER(is_tutorial=true, is_skippable=false, is_autoable=false)] 电玩城拉索战教学_a
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[InputBlocker(blockInput=true, black=0.2)]
[Battle.SwitchToDefaultUIState]
[Battle.Pause(pause=true)]
[InputBlocker(blockInput=true, black=0.2)]
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys")] 【心连心】通关指南	
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys")] 在心连心中，玩家的目标是让更多的敌人<@tu.kw>通过干员之间的锁链</>。	
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys")] 博士，这是一个充满着爱的游戏。	
[Tutorial(focusX=-147, focusY=122, focusWidth=297, focusHeight=230,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", anchor="Center",           protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 注意看这些摇摇晃晃的地块。	
[Tutorial(focusX=-147, focusY=122, focusWidth=297, focusHeight=230,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", anchor="Center",           protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 干员们不能直接被部署在这些地块上，需要周围<@tu.kw>有其他干员协助</>，大家心连着心才能站稳。	
[Tutorial(tileX=1, tileY=3, focusWidth=108, focusHeight=111,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", anchor="Center",           protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 博士，可以先在这里部署干员来为后续干员提供心连心的支点。	
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 在心连心中，玩家并不需要把敌人全部消灭，敌人到达终点后也<@tu.kw>不会扣除关卡生命值</>。
[Tutorial(protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 尽可能让敌人更多次经过锁链来赚取关卡得分吧，博士。
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
```

### training_act1arcade_m4_01_a

```
[HEADER(is_tutorial=true, is_skippable=false)]电玩城计程车教学1_a
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.LockFunction(mask="CHARACTER_INFO")]
[Battle.LockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true)]
[Battle.SwitchToDefaultUIState]
[Battle.Delay(time=1.1)]
[Battle.Pause]
[popupdialog(dialogHead="$avatar_sys")]【障碍飞车】通关指南
[popupdialog(dialogHead="$avatar_sys")]在障碍飞车中，玩家的目标是让“两栖号”船车尽可能行驶更长的路程，并顺利到达<@tu.kw>灰色目标点</>。
[Battle.Pause(pause=false)]
[Battle.Delay(time=2)]
[Battle.Pause(pause=true)]
[Tutorial(tileX=1, tileY=1, focusWidth=150, focusHeight=150,  animStyle="Highlight", focusStyle="HighlightCircle", dialogHead="$avatar_sys")] 这里是“两栖号”船车出发的两栖码头。  
[Battle.Pause(pause=false)]
[Battle.Delay(time=2)]
[Battle.Pause(pause=true)]
[InputBlocker(blockInput=true)]
[Tutorial(tileX=1, tileY=1, focusWidth=150, focusHeight=150,           animStyle="Highlight", focusStyle="HighlightCircle", black=0.5,           protectTime=0.2, dialogHead="$avatar_sys")] 两栖码头准备就绪后，就会自动开启技能发射一辆<@tu.kw>“两栖号”船车</>。
[InputBlocker(blockInput=true)]
[Battle.Pause(pause=false)]
[Battle.Delay(time=5)]
[Battle.Pause(pause=true)]
[Tutorial(tileX=3, tileY=1, focusWidth=180, focusHeight=180,  animStyle="Highlight", focusStyle="HighlightCircle", dialogHead="$avatar_sys")] “两栖号”船车发射后会沿着直线方向行驶，对碰撞到的敌人造成<@tu.kw>无视闪避的物理伤害</>与<@tu.kw>短暂晕眩</>。   
[Tutorial(tileX=3, tileY=1, focusWidth=180, focusHeight=180,  animStyle="Highlight", focusStyle="HighlightCircle", dialogHead="$avatar_sys")] “两栖号”船车初始有一定的关卡得分，每行驶一定距离关卡得分就会增加。
[Tutorial(tileX=8, tileY=5, focusWidth=120, focusHeight=120,  animStyle="Highlight", focusStyle="HighlightCircle", dialogHead="$avatar_sys",  dialogY="$f_lower_dialog_pos_y")] 当“两栖号”船车顺利到达<@tu.kw>灰色目标点</>时，玩家就可以获得这些关卡得分。  
[Battle.Pause(pause=false)]
[Battle.Delay(time=3)]
[Battle.Pause(pause=true)]
[popupdialog(dialogHead="$avatar_sys")]“两栖号”船车如果驶进了<@tu.kw>不可通行</>的地形，就会被判出局，玩家也无法得到它的关卡得分。 
[popupdialog(dialogHead="$avatar_sys")]不过，我们可以改变“两栖号”船车的行驶方向来避免这一情况的出现。
[Battle.EnsureMinSp(charId="trap_187_arcgacha", sp=30)]
[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true, tileX=6, tileY=3, validWidth=108, validHeight=111)]
[Tutorial(tileX=6, tileY=3, focusWidth=108, focusHeight=111, waitForSignal="char_info", charId="trap_187_arcgacha",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", anchor="Center",           protectTime=0.5, dialogHead="$avatar_sys")] 看，这次扭蛋机中新增了道具——转向器。 
[Battle.LockFunction(mask="CHARACTER_INFO")]
[Battle.LockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true)]
[Delay(time=0.3)]
[Tutorial(target="btn_skill", waitForSignal="use_skill",           animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")]
[Battle.Pause(pause=false)]
[Battle.Delay(time=0.3)]
[Battle.Pause(pause=true)]
[InputBlocker(blockInput=false)]
[Tutorial(tileX=5, tileY=1, focusWidth=108, focusHeight=111, waitForSignal="put_down", charId="trap_081_turngear",            posX=5, posY=1, animStyle="Drag", startCardIndex=0, startRightStart=true, endTileX=5, endTileY=1,           dialogHead="$avatar_sys", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5)] 把它部署在这里。
[Battle.Pause]
[InputBlocker(blockInput=true, tileX=5, tileY=1, validWidth=150, validHeight=170)]
[Tutorial(waitForSignal="select_direction", animStyle="Drag",           startTileX=5, startTileY=1, endTileX=5, endTileY=3)]
[Battle.Pause(pause=false)]
[Battle.Delay(time=1.5)]
[Battle.Pause(pause=true)]
[InputBlocker(blockInput=true)]
[popupdialog(dialogHead="$avatar_sys")]“两栖号”船车只要经过转向器或者<@tu.kw>我方单位</>，就会<@tu.kw>沿着其部署方向行驶</>。  
[Battle.Pause(pause=false)]
[Battle.Delay(time=5)]
[Battle.Pause(pause=true)]
[popupdialog(dialogHead="$avatar_sys")]注意，“两栖号”船车如果遭到敌人攻击，它的生命值和关卡得分都会减少，博士需要及时清除障碍护送船车。
[popupdialog(dialogHead="$avatar_sys")]另外，场上还会随机出现一些“搁浅零件”，“两栖号”船车经过它们可以获得对应的<@tu.kw>增益效果</>。  
[popupdialog(dialogHead="$avatar_sys")]增益效果<@tu.kw>不止一种</>，博士可以在接下来的游戏中自行探索。
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[Battle.Pause(pause=false)]
```


## 统计

- 总字符数：16860
- 对话行数：0


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
