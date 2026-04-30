# 明日方舟 · 活动剧情 · act38side（40段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act38side」完整剧情脚本（40个文件，3886行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act38side
- 脚本文件数：40

### guide_firework_craft_01

```
[HEADER(is_skippable=false, is_tutorial=true)] 烟花拼装引导1-页面触发
[PopupDialog(dialogHead="$avatar_crosly2", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 现在你可以自己设定烟花燃放的<@tu.kw>效果</>。
[Tutorial(target="btn_firework_edit", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 点击左上角，进入<@tu.kw>装配工坊</>。
```

### guide_firework_craft_02

```
[HEADER(is_skippable=false, is_tutorial=true)]  烟花拼装引导2-兽主切换
[Firework.WaitForCraftPageStable]
[Tutorial(target="pool_puzzle_plate", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 装配了不同<@tu.kw>种类装药</>的烟花在燃放时的<@tu.kw>效果</>也会不同。
[Tutorial(target="pool_firework_btn_switch_animal", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_crosly2", waitForSignal="firework_craft_animal_select_state_routed")] 这里可以切换不同种类的装药。
[Tutorial(target="pool_firework_btn_select_animal", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 这是<@tu.kw>当前装药</>，你也可以选择切换。
```

### guide_firework_craft_03

```
[HEADER(is_skippable=false, is_tutorial=true)] 烟花拼装引导3-页面触发
[PopupDialog(dialogHead="$avatar_crosly2", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 庆典期间，你可以<@tu.kw>自己动手</>装配想要的烟花。
[Tutorial(target="btn_firework_edit", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 点击左上角，进入<@tu.kw>装配工坊</>。
```

### guide_firework_craft_04

```
[HEADER(is_skippable=false, is_tutorial=true)] 烟花拼装引导4--范围编辑
[Firework.WaitForCraftPageStable]
[Tutorial(target="pool_puzzle_plate", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 界面上<@tu.kw>有颜色的区域</>表示对应关卡中的<@tu.kw>烟花燃放范围</>，你可以选择右侧的烟花样片来自定义这个范围。
[Tutorial(target="pool_firework_craft_right_list_item", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y", waitForSignal="firework_craft_sub_list_shown")] 右侧列表选择这组烟花样片。
[Tutorial(target="pool_firework_craft_sub_list_item", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 再选择一张<@tu.kw>角度合适</>的烟花样片进行装配，烟花就会按图示范围燃放了，重叠的部分也可以<@tu.kw>正常燃放</>。
[Tutorial(target="pool_firework_craft_bottom_list", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_crosly2")] 正在使用的烟花样片会被收录在下方，点击可以<@tu.kw>快速拆卸</>。
[Tutorial(target="pool_firework_btn_switch_map", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 可以通过地图开关切换<@tu.kw>地图模式</>，查看当前烟花在<@tu.kw>关卡中</>的燃放效果。
[Tutorial(target="pool_firework_craft_save_btn", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 烟花设计完成后，<@tu.kw>点击这里</>进行保存。
```

### guide_firework_puzzle

```
[HEADER(is_skippable=false, is_tutorial=true)] 烟花解谜引导
[PopupDialog(dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 狂欢节期间，每天都会有新的烟花委托送来。
[Tutorial(target="pool_first_puzzle_item", searchBtnInChildren=true, waitForSignal="puzzle_detail_state_routed",            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 选择第一个委托。
[Tutorial(target="pool_puzzle_plate", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 这里是委托的烟花图案,你的任务是挑选合适的烟花样片来<@tu.kw>填满图案中的空白格点</>,但需要<@tu.kw>避开黑色打叉的禁用格点</>!
[Tutorial(target="pool_plate_list_area", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 右侧列表就是你可以使用的烟花样片,每种样片有对应的<@tu.kw>生效格点</>,并且有多个<@tu.kw>旋转角度</>。不同样片的<@tu.kw>生效格点允许互相重叠</>
[Tutorial(target="pool_plate_fill_area", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_crosly2")] 烟花的容量有限，在使用烟花样片时也有<@tu.kw>数量限制</>，可以注意下方槽位数量。
[Tutorial(target="pool_btn_hint", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 如果遇到困难，可以向热心的送货员求助，她会帮你标出一张<@tu.kw>正确可用</>的烟花样片。
[Tutorial(target="pool_btn_confirm", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_crosly2", dialogY="$f_lower_dialog_pos_y")] 完成筹委会指定的烟花图案后，点击这里<@tu.kw>提交</>，就可以获得委托报酬了！
```

### act38side_10

```
[HEADER(is_tutorial=true, is_skippable=false)] boss关教学
[Battle.Pause]
[popupdialog(dialogHead="$avatar_whitw2", dialogY="$f_lower_dialog_pos_y")]气氛终于火热起来了！不如，我们来让这场狂欢更有意思些！
[popupdialog(dialogHead="$avatar_whitw2", dialogY="$f_lower_dialog_pos_y")]来比一比，谁在狂欢时刻下击倒的坏家伙更多！
[Tutorial(focusX=127, focusY=-37, focusWidth=232, focusHeight=60, anchor="Left",          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=2, dialogHead="$avatar_whitw2",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]要是你们赢了，我就撤掉自己的<@tu.kw>减伤护盾</>，并且你们的下一个烟花<@tu.kw>特殊效果</>也会更强！
[Tutorial(focusX=127, focusY=20, focusWidth=232, focusHeight=60, anchor="Left",          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=2, dialogHead="$avatar_whitw2",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]要是你们输了，说明你们确实很无聊，你们的下一个烟花就会<@tu.kw>失去特殊效果</>！
[popupdialog(dialogHead="$avatar_whitw2", dialogY="$f_lower_dialog_pos_y")]听起来不错吧？那我来倒数，三、二——狂欢开始！
[Battle.Pause(pause=false)]
```

### act38side_10_f

```
[HEADER(is_tutorial=true, is_skippable=false)] boss关我方失败
[Battle.Pause]
[popupdialog(dialogHead="$avatar_whitw2", dialogY="$f_lower_dialog_pos_y")]哈哈，不过如此！你们果然很无聊，下一个烟花可就<@tu.kw>没有特殊效果</>了哦！
[Battle.Pause(pause=false)]
```

### act38side_10_w

```
[HEADER(is_tutorial=true, is_skippable=false)] boss关我方胜利
[Battle.Pause]
[popupdialog(dialogHead="$avatar_whitw2", dialogY="$f_lower_dialog_pos_y")]漂亮！那我就<@tu.kw>撤掉护盾</>了，但只有一小会儿。来，别错过机会！
[Battle.Pause(pause=false)]
```

### act38side_sp01

```
[HEADER(is_tutorial=true, is_skippable=false)] 趣味关01
[Battle.Pause]
[popupdialog(dialogHead="$avatar_texas", dialogY="$f_lower_dialog_pos_y")]这次的任务目标是确保烟花的燃放能顺利进行，一旦<@tu.kw>烟花熄灭</>，任务就<@tu.kw>失败</>了。
[popupdialog(dialogHead="$avatar_texas", dialogY="$f_lower_dialog_pos_y")]仔细观察，运用环境中的<@tu.kw>障碍物</>改变地形，也许就能拖慢敌人的行动。
[popupdialog(dialogHead="$avatar_texas", dialogY="$f_lower_dialog_pos_y")]借助烟花的力量与合理的<@tu.kw>火药装配</>，可以帮助我们完成任务。
[Battle.Pause(pause=false)]
```

### level_act38side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="56_g11_newvolsiniipier",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1099年12月5日</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[SoundVolume(volume=0.4, channel="s",fadetime=2)]
[PlaySound(key="$d_avg_craneworking", volume=1)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1550_1#1$1", duration=1, isblock=true)]
[name="码头工人"]运的什么东西？
[charslot(slot = "m", name = "avg_npc_698_1#1$1")]
[name="家族成员"]葡萄酒。
[dialog]
[charslot(slot = "m", name = "avg_npc_1550_1#1$1")]
[name="码头工人"]货运单号。
[charslot(slot = "m", name = "avg_npc_698_1#1$1")]
[name="家族成员"]SZ990183。
[charslot(slot = "m", name = "avg_npc_1550_1#1$1")]
[name="码头工人"]所属公司名称？
[charslot(slot = "m", name = "avg_npc_698_1#1$1")]
[name="家族成员"]抱歉，我没有听懂你的问题。
[charslot(slot = "m", name = "avg_npc_1550_1#1$1")]
[name="码头工人"]你车上装的货物，属于哪一家公司？这有什么听不懂的。
[charslot(slot = "m", name = "avg_npc_698_1#1$1")]
[name="家族成员"]哈哈......看起来，这位先生应该刚工作不久，还不懂规矩。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1, loop=true, channel="w")]
[StopSound(channel="w", fadetime=1)]
[charslot(slot = "m", name = "avg_npc_698_1#1$1", posfrom="0,0", posto="200,0", afrom=1, ato=1, duration=1)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_698_1#1$1", posfrom="-200,0", posto="0,0", duration=1)]
[delay(time=1.5)]
[charslot(slot = "m", focus="m")]
[name="家族成员"]没关系，我可以耐心地教你。这种时候，你应该恭敬地问：“您属于哪个家族？”
[charslot]
[charslot(slot = "m", name = "avg_npc_1550_1#3$1")]
[name="码头工人"]......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1542_1#1$1", posfrom="200,0", posto="50,0", duration=1.5)]
[charslot(slot = "l", name = "avg_npc_1547_1#1$1", posfrom="-200,0", posto="-50,0", duration=1.5)]
[delay(time=2)]
[charslot]
[charslot(slot = "m", name = "avg_npc_698_1#1$1")]
[name="家族成员"]你们......
[charslot(slot = "m", name = "avg_npc_1542_1#8$1")]
[name="伊雷妮"]抱歉先生，所属公司名称？
[charslot(slot = "m", name = "avg_npc_698_1#1$1")]
[name="家族成员"]......萨卢佐酒业。
[charslot(slot = "m", name = "avg_npc_1542_1#4$1")]
[name="伊雷妮"]嗯......行了，信息核对无误，可以通过。
[charslot(slot = "m", name = "avg_npc_698_1#1$1")]
[name="家族成员"]......
[charslot(slot = "m", name = "avg_npc_1542_1#4$1")]
[name="伊雷妮"]不要这样看着我，也不要带着老一套的思路在这里处理问题。看看关口上面的标志吧。
[charslot(slot = "m", name = "avg_npc_1542_1#1$1")]
[name="伊雷妮"]欢迎来到新沃尔西尼。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[bgeffect(name="$eb_tvnoise",layer=1)]
[delay(time=1)]
[Image(image="56_i22",screenadapt="coverall")]
[PlaySound(key="$d_avg_filmprojection")]
[playsound(key="$d_avg_filmprojection_loop", loop=true, channel="bgs",delay=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Sticker(id="st1", text="新都会", delay=0.001, width=800, x=250, y=520, duration=2, alignment="center", size=42)]
[delay(time=1)]
[Sticker(id="st1", duration=2, block = false)]
[StopSound(channel="bgs", fadetime=2)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[charslot]
[bgeffect]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Background(image="56_g9_truckcamp",screenadapt="coverall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月6日    7:00 A.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot = "m", name = "avg_npc_1542_1#2$1", duration=1.5, isblock=true)]
[Delay(time=0.5)]
[charslot]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot= "l", name= "avg_npc_1550_1#1$1", posfrom="-200,0", posto="0,0", duration=0.5)]
[delay(time=0.5)]
[charslot(slot= "r", name= "avg_npc_1561_1#1$1", posfrom="200,0", posto="0,0", duration=0.5)]
[delay(time=0.8)]
[charslot(slot= "l", name= "avg_npc_1550_1#1$1", focus="l")]
[name="卡车司机A"]头儿，你来得正好，有点事要和你商量。
[name="卡车司机A"]我们几个今天不出车，打算把营地的路面整个都规整一遍。
[name="卡车司机A"]要是山德罗下次倒车的时候再扎爆胎，就只能怪他自己实在是交不到好运了，哈哈。
[charslot(slot= "r", name= "avg_npc_1561_1#1$1", focus="r")]
[name="卡车司机B"]另外，定制的帐篷也到了，我们打算搭在靠西的出口。
[name="卡车司机B"]空间大，雨棚、净水装置、烧烤架都有地方安置。那边也更安静，到时候新加入的伙计们也能适应得更快一些。
[name="卡车司机B"]我还顺便添置了一块露天屏幕，以后大家伙在营地又多了个娱乐项目。
[name="卡车司机B"]我改天去租一些蓝卡坞的超级大片......我知道你要说什么——记得不要黑帮电影。
[charslot(slot= "l", name= "avg_npc_1550_1#1$1", focus="l")]
[name="卡车司机A"]对了，听说市政厅已经在着手建设新的安置区了？
[charslot(slot= "r", name= "avg_npc_1561_1#1$1", focus="r")]
[name="卡车司机B"]哈哈，那他们最好动作快一点，要不然到时候我可能都舍不得搬走了。
[name="卡车司机B"]虽然现在卡车只能停在营地里，大家伙只能住在卡车上，拖家带口的有很多不方便......
[name="卡车司机B"]但起码再也不用受那些家族的人欺负。这些卡车真的属于我们，和大家伙一起守着它们，安心。
[charslot]
[charslot(slot = "m", name = "avg_npc_1542_1#1$1")]
[name="伊雷妮"]......是啊。
[name="伊雷妮"]有时候看看眼前的营地，谁敢相信一年前这里还只是一块荒地呢？
[charslot(slot= "m", name= "avg_npc_1550_1#1$1")]
[name="卡车司机A"]对了，头儿，你为什么一晚上没回来？
[charslot(slot = "m", name = "avg_npc_1542_1#3$1")]
[name="伊雷妮"]啊，被你们一打岔，差点忘了正事！
[charslot(slot = "m", name = "avg_npc_1542_1#2$1")]
[name="伊雷妮"]把几个城区的负责人都叫过来，山德罗、金特、索默尔......
[charslot(slot= "m", name= "avg_npc_1550_1#1$1")]
[name="卡车司机A"]索默尔不在。
[charslot(slot = "m", name = "avg_npc_1542_1#5$1")]
[name="伊雷妮"]嗯？今天他不是休息吗？
[charslot(slot = "m", name = "avg_npc_1542_1#7$1")]
[name="伊雷妮"]都跟他说过好几次了，想给小古莉治病，想早点把她接到新沃尔西尼来，我能理解......
[name="伊雷妮"]小古莉也是我的妹妹，我会一起想办法，不要老给自己多加出车任务。
[charslot(slot= "m", name= "avg_npc_1550_1#2$1")]
[name="卡车司机A"]头儿，别生气，应、应该不是你想的这样。
[charslot(slot = "m", name = "avg_npc_1542_1#2

... (全文23019字符)
```

### level_act38side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Background(image="56_g9_truckcamp",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月6日    1:35 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", duration=1)]
[charslot(slot = "l", name = "avg_npc_1547_1#10$1", duration=1, isblock=true)]
[Delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", focus="r")]
[charslot(slot = "l", name = "avg_npc_1547_1#10$1", focus="n")]
[name="伊雷妮"]......我让彼得罗他们都出去了，营地暂时不会有人过来。
[charslot(slot = "l", name = "avg_npc_1547_1#10$1", focus="l")]
[name="索默尔"]伊雷妮，你昨天晚上和拉维妮娅法官在一起，你知道莱昂图索先生伤得重不重吗？他是不是......
[charslot(slot = "r", name = "avg_npc_1542_1#7$1", focus="r")]
[name="伊雷妮"]他昨晚好像已经抢救过来了，但......情况很不好......
[charslot(slot = "l", name = "avg_npc_1547_1#10$1", focus="l")]
[name="索默尔"]......
[dialog]
[PlaySound(key="$d_avg_chairrub", volume=1)]
[charslot(slot= "l", name= "avg_npc_1547_1#12$1", posfrom="0,0", posto="0,-15", afrom=1, ato=0, duration=1)]
[delay(time=1)]
[charslot(slot = "l", focus="n")]
卡车司机像泄了气的皮球一样瘫在了椅子上，他用脏污的手套捂住脸。
[name="索默尔"]他还那么年轻，也是个好人......可千万不要——唉，我真是......！
[dialog]
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", posfrom="0,0", posto="-200,0", afrom=1, ato=1, duration=1)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[name="伊雷妮"]到底怎么回事？
[name="伊雷妮"]是意外吗？
[charslot(slot = "r", focus="n")]
[name="索默尔"]我、我也说不上来。我本来正好好地开着车，可突然之间方向盘就不听使唤了......
[name="索默尔"]我来不及反应，直接撞晕了过去。等醒过来的时候，一切已经发生了。
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[name="伊雷妮"]可......哪怕情急之下慌了神，你也不该将重伤的人放在路边不管不顾呀！
[name="伊雷妮"]你知不知道！如果再耽误一点抢救时间，莱昂图索先生现在就已经......
[name="伊雷妮"]索默尔，你明明不是这样的人。
[charslot(slot = "r", focus="n")]
[name="索默尔"]对不起，伊雷妮......我真的想要救他的，我知道我应该救他，我不是没种的坏家伙！
[name="索默尔"]但、但我必须马上把车开走。
[charslot(slot = "r", name = "avg_npc_1542_1#5$1", focus="r")]
[name="伊雷妮"]为什么？
[charslot(slot = "r", focus="n")]
[name="索默尔"]......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r", name = "avg_npc_1542_1#9$1", focus="r")]
[name="伊雷妮"]索默尔，你别不说话啊。
[charslot(slot = "r", name = "avg_npc_1542_1#5$1", focus="r")]
[name="伊雷妮"]车上......有什么东西吗？
[dialog]
[charslot]
伊雷妮的声音开始颤抖，瘫坐在椅子上的司机面色惨白。
[dialog]
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", focus="r")]
[delay(time=1)]
[PlaySound(key="$d_avg_chairrub", volume=1)]
[charslot(slot = "l", name = "avg_npc_1547_1#10$1", posfrom="0,-30", posto="0,0", duration=1)]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_npc_1547_1#10$1", focus="l")]
[name="索默尔"]伊雷妮......对不起......
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[name="伊雷妮"]索默尔，你到底在替谁开车？
[charslot(slot = "l", name = "avg_npc_1547_1#10$1", focus="l")]
[name="索默尔"]威尼斯载具公司......威尼斯家族。
[charslot]
空气长久地静默，不知过了多久，伊雷妮才缓缓开口。
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[charslot(slot = "l", name = "avg_npc_1547_1#10$1", focus="n")]
[name="伊雷妮"]是因为小古莉的事情吗？
[charslot(slot = "l", name = "avg_npc_1547_1#12$1", focus="l")]
[name="索默尔"]伊雷妮，不用帮我找借口......我知道自己犯了多大的错。
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[name="伊雷妮"]为什么、为什么宁愿去找他们，也不愿意向互助会寻求帮助呢？
[name="伊雷妮"]你明明是互助会资历最老的司机，你知道咱们在新沃尔西尼的地位有多特殊，市政厅和家族都在盯着我们。
[charslot(slot = "l", name = "avg_npc_1547_1#10$1", focus="l")]
[name="索默尔"]伊雷妮，治矿石病的药是什么价格，我们都清楚。
[name="索默尔"]更何况后面把小古莉接到新沃尔西尼之后，安顿她，供她上一个好点的学校，还需要不知道多大的开支......
[charslot(slot = "r", name = "avg_npc_1542_1#7$1", focus="r")]
[name="伊雷妮"]还有我，索默尔。当初在西西里城，是你给了我活路，小古莉也是我的妹妹。
[charslot(slot = "l", name = "avg_npc_1547_1#10$1", focus="l")]
[name="索默尔"]伊雷妮，这根本不是互助会能帮我解决的。
[charslot(slot = "r", name = "avg_npc_1542_1#7$1", focus="r")]
[name="伊雷妮"]所以你就一个人......
[dialog]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1542_1#5$1", focus="r")]
[name="伊雷妮"]......不对。
[name="伊雷妮"]不管是接驳其他城市送到港口的物资，还是城内商户之间的货物转运，我们经手的所有东西都必须事先登记。
[name="伊雷妮"]这半年，每一次的排班表我都亲自确认过，定期检查也都没有出任何纰漏，你一个人是怎么做到——难道说......
[charslot(slot = "l", name = "avg_npc_1547_1#12$1", focus="l")]
[name="索默尔"]伊雷妮，不止我一个人。
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[name="伊雷妮"]......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="33_g10_smallrestaurant",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "r", name = "avg_npc_1561_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_1554_1#1$1", focus="l")]
[name="家族成员"]......所以，你们几个也不知道索默尔去了哪里。
[charslot(slot = "r", name = "avg_npc_1561_1#1$1", focus="r")]
[name="卡车司机"]他会不会已经连夜逃回西西里城了？毕竟撞了代理市长这么大的事......
[name="卡车司机"]警察肯定会一查到底的。咱们的事会不会暴露？偷运违禁品可是市政厅的红线，而且还是帮你们......
[charslot(slot = "l", name = "avg_npc_1554_1#1$1", focus="l")]
[name="家族成员"]不不，这件事和威尼斯载具公司可没有关系。
[dialog]
[charslot(slot = "r", posfrom="0,0", posto="80,0", duration=1, isblock=true)]
[charslot(slot = "r", name = "avg_npc_1561_1#3$1", focus="r")]
[name="卡车司机"]——
[name="卡车司机"]什么意思，你不会是想杀了我们灭口吧......
[charslot(slot = "l", name = "avg_npc_1554_1#1$1", focus="l")]
[name="家族成员"]灭口？哈哈哈，我已经好久没听过这个词了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1, loop=true, channel="w")]
[StopSound(channel="w", fadetime=1)]
[charslot(slot = "l", posfrom="0,0", posto="80,0", duration=1.5, isblock=true)]
[charslot(slot = "l", name = "avg_npc_1554_1#1$1", focus="l")]
[name="家族成员"]放松，别那么紧张，你看我手上如今拿的是武器吗？我只是希望你们不要说不该说的，就这么简单。
[charslot(slot = "r", name = "avg_npc_1561_1#3$1", focus="r")]
[name="卡车司机"]可万一警察真查到我们头上怎么办？
[name="卡车司机"]一直以来，我们瞒着伊雷妮，顶着市政厅的压力帮你们，如果真的出了事情，你们不能只想着撇清关系！
[charslot(sl

... (全文19534字符)
```

### level_act38side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="56_g11_newvolsiniipier",screenadapt="coverall")]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1542_1#5$1", duration=1, isblock=true)]
[name="伊雷妮"]卡车......什么什么......抱歉，您刚刚说的名字实在是太长了。
[charslot(slot = "m", name = "avg_4065_judge_1#1$1")]
[name="拉维妮娅"]“新沃尔西尼货运工人和卡车司机联合互助会”......我们需要学习一下维多利亚和哥伦比亚的这种工人组织。
[charslot(slot = "m", name = "avg_4065_judge_1#7$1")]
[name="拉维妮娅"]要想对抗家族的威胁，首先要让我们自己团结起来，拥有与他们对抗的力量。
[charslot(slot = "m", name = "avg_npc_1541_1#1$1")]
[name="莱昂图索"]运输业是一个城市的命脉。在过去，在叙拉古的其他任何一座城市，它始终被家族牢牢掌控着。
[name="莱昂图索"]我们想要改变这种现状。
[name="莱昂图索"]在新沃尔西尼，卡车不再是黑帮的快递箱，它只属于驾驶它的人，还有每一个正直的市民。
[charslot(slot = "m", name = "avg_npc_1542_1#5$1")]
[name="伊雷妮"]可是，为什么是我？
[name="伊雷妮"]我以前只是给索默尔的小超市开车进货......虽然车开得还算可以......
[charslot(slot = "m", name = "avg_npc_1541_1#8$1")]
[name="莱昂图索"]在沃尔西尼，没有接受过家族贿赂的市政府职员，两只手就能数得过来。
[charslot(slot = "m", name = "avg_npc_1542_1#2$1")]
[name="伊雷妮"]那是因为......
[charslot(slot = "m", name = "avg_4065_judge_1#8$1")]
[name="拉维妮娅"]对不起，伊雷妮。之前我私下调查过你和索默尔的经历。我知道那场惨案，我很抱歉。
[name="拉维妮娅"]我在想，如果你只是仇恨纵火焚烧了你们超市的那个家族，你完全可以接受另一个家族的帮助，去完成复仇......
[name="拉维妮娅"]但你没有这么做。
[charslot(slot = "m", name = "avg_4065_judge_1#2$1")]
[name="拉维妮娅"]只是我的一点揣测......如果有冒犯，还请原谅。
[charslot(slot = "m", name = "avg_npc_1542_1#1$1")]
[name="伊雷妮"]谢谢您......拉维妮娅法官。
[charslot(slot = "m", name = "avg_4065_judge_1#9$1")]
[name="拉维妮娅"]伊雷妮，姑且不论你是不是卡车工会负责人的最佳人选，我都相信你是一个善良的人。
[name="拉维妮娅"]请认真考虑一下这份邀请，好吗？
[charslot(slot = "m", name = "avg_npc_1542_1#2$1")]
[name="伊雷妮"]......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="56_g5_courtsquare_d",screenadapt="coverall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月6日    4:47 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", posfrom="200,0", posto="0,0", duration=1.5)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_702_1#1$1", posfrom="-100,0", posto="0,0", duration=1)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_702_1#1$1", focus="l")]
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", focus="n")]
[name="法官助理"]伊雷妮小姐，请稍等。拉维妮娅法官正在主持一场庭审，等结束后就可以来见你了。
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", focus="r")]
[name="伊雷妮"]好......好的，不着急。
[charslot(slot = "l", name = "avg_npc_702_1#1$1", focus="l")]
[name="法官助理"]你拿着的是要交给拉维妮娅法官的资料吗？我可以先转交给她。
[charslot(slot = "r", name = "avg_npc_1542_1#5$1", focus="r")]
[name="伊雷妮"]不！还是不用了......一会儿我自己给她吧。
[charslot]
伊雷妮说着，将手中的笔记本又攥得紧了一点。
[charslot(slot = "l", name = "avg_npc_702_1#1$1", focus="n")]
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", focus="r")]
[name="伊雷妮"]请问，拉维妮娅法官这会儿在审的案子是那些企业的纠纷吗，还是、还是和昨晚的车祸有关？
[charslot(slot = "l", name = "avg_npc_702_1#1$1", focus="l")]
[name="法官助理"]哦，都不是。
[name="法官助理"]严格意义上说，并不是一场庭审，而是一场可能连拉维妮娅法官都没办法处理的申诉。
[name="法官助理"]当事人只是一位普通的新沃尔西尼市民，但情况比较特殊。
[charslot(slot = "r", name = "avg_npc_1542_1#4$1", focus="r")]
[name="伊雷妮"]她是新沃尔西尼的大法官，有什么案子是她都......我能去听听看吗？
[charslot(slot = "l", name = "avg_npc_702_1#1$1", focus="l")]
[name="法官助理"]当然。那你就在旁听席上等她好了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", afrom=1, ato=0, duration=1.5)]
[stopmusic(fadetime=2)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="33_g3_srccourt",screenadapt="coverall")]
[PlayMusic(key="$wasteland_loop", volume=0.6)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4065_judge_1#1$1")]
[name="拉维妮娅"]......我会尽快联系蒙特卢佩市政府，寻求他们的协助来抓捕凶手。
[name="拉维妮娅"]同时，我们也会申请新沃尔西尼法院对这个案件的审判权。
[charslot(slot = "m", name = "avg_npc_696_1#1$1")]
[name="悲哀的市民"]那您能不能告诉我，可能性有多大？
[charslot(slot = "m", name = "avg_4065_judge_1#1$1")]
[name="拉维妮娅"]......
[name="拉维妮娅"]我会尽全力争取。提请异地审判，这一年不是没有过类似的事情——
[charslot(slot = "m", name = "avg_npc_696_1#1$1")]
[name="悲哀的市民"]但是一次都没有成功过，不是吗？
[charslot(slot = "m", name = "avg_4065_judge_1#7$1")]
[name="拉维妮娅"]......哪怕失败，我也会督促蒙特卢佩的同事公正地审理案件，让凶手得到应有的惩罚。
[charslot(slot = "m", name = "avg_npc_696_1#1$1")]
[name="悲哀的市民"]公正？
[name="悲哀的市民"]拉维妮娅法官，要是那样的话，我们都知道会是什么结果！
[name="悲哀的市民"]他们会说，是我的哥哥在酒吧喝醉了主动挑事，那几个家族的可怜人只是正当防卫，才失手酿成了意外。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_smashtable", volume=1)]
[name="悲哀的市民"]您知道的，根本不是那么回事！
[name="悲哀的市民"]他是因为狂欢节相关的事宜才去蒙特卢佩出差的，结果不小心得罪了当地的家族，被活活打死在了肮脏的巷子里......
[name="悲哀的市民"]拉维妮娅法官，我听说那个家族已经请法院的人吃过饭了，您还是想跟我说，您能够督促您的同事公平公正地审理吗？
[charslot(slot = "m", name = "avg_4065_judge_1#5$1")]
[name="拉维妮娅"]我——
[charslot(slot = "m", name = "avg_npc_696_1#1$1")]
[name="悲哀的市民"]我的哥哥是个好人，他一辈子没有做过什么恶事，我们是最早申请加入新沃尔西尼的市民，大家都很喜欢他......
[charslot(slot = "m", name = "avg_4065_judge_1#6$1")]
[name="拉维妮娅"]我很遗憾。
[charslot(slot = "m", name = "avg_npc_696_1#1$1")]
[name="悲哀的市民"]您不用遗憾，这种事情在叙拉古再常见不过了，不是吗？
[name="悲哀的市民"]拉维妮娅法官，我想报仇。
[name="悲哀的市民"]用我自己的方法，用在叙拉古再常见不过的方法......变卖家产，请一个杀手，或者去投靠和那个家族有仇的其他家族。
[name="悲哀的市民"]但这样是不是会违反新沃尔西尼法律的规定？
[name="悲哀的市民"]您会审判我吗，新沃尔西尼会永远驱逐我吗？
[charslot(slot = "m", name = "avg_4065_judge_1#6$1")]
[name="拉维妮娅"]......按照《新都市管理法案》，的确如此。
[charslot(slot = "m", name = "avg_npc_696_1#1$1")]
[name="悲哀的市民"]新沃尔西尼的法律是严格的、有效的，可它只在新沃尔西尼严格，只在新沃尔西尼有效......
[name="悲哀的市民"]您难道不觉得，这太可笑了吗？
[charslot(slot = "m", name =

... (全文21108字符)
```

### level_act38side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="56_g12_saluzzowinery",screenadapt="coverall")]
[playMusic(intro="$suspenseful_intro",key="$suspenseful_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月6日    10:15 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_686_1#9$1", duration=1, isblock=true)]
[name="阿尔贝托"]我刚开了一瓶酒，你很会挑时候，德米特里。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_690_1#7$1", posfrom="200,0", posto="0,0", duration=1.5)]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_npc_690_1#7$1", focus="r")]
[name="德米特里"]是你做的吗？
[charslot(slot = "l", name = "avg_npc_686_1#10$1", focus="l")]
[name="阿尔贝托"]什么？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_smashtable", volume=1)]
[charslot(slot = "r", name = "avg_npc_690_1#4$1", focus="r")]
[name="德米特里"]别装傻！
[name="德米特里"]那场车祸，莱昂现在生死未卜......别告诉我你什么都不知道！
[charslot(slot = "l", name = "avg_npc_686_1#7$1", focus="l")]
[name="阿尔贝托"]冷静一点，德米特里。你跟了贝纳尔多那么多年，却没有学会他的智慧。
[name="阿尔贝托"]我不喜欢受到无端的指责，更重要的是，我不喜欢有求于我的人是这个态度。
[charslot(slot = "r", name = "avg_npc_690_1#7$1", focus="r")]
[name="德米特里"]......告诉我你知道的所有事。
[charslot(slot = "l", name = "avg_npc_686_1#1$1", focus="l")]
[name="阿尔贝托"]不不不，关于这场意外，我知道的并不比你多。
[name="阿尔贝托"]但是我想讲一个故事，一个我很少提起的、很私人的故事。所以，安静一点，当一个好听众，好吗？
[charslot(slot = "r", name = "avg_npc_690_1#7$1", focus="r")]
[name="德米特里"]......
[charslot(slot = "l", name = "avg_npc_686_1#1$1", focus="l")]
[name="阿尔贝托"]我曾经，是很久以前的曾经，也有过一位“兄弟”。
[name="阿尔贝托"]我们的关系很好，我们一起长大，一起度过了人生中最愚蠢的青春时光。但是后来，我们之间慢慢出现了一些不同。
[name="阿尔贝托"]我开始学习打理家族的生意，学习叙拉古的规则，但是我的那位兄弟，很可惜，对这些并不感兴趣。
[name="阿尔贝托"]他喜欢维多利亚的文学、莱塔尼亚的音乐、叙拉古的戏剧......他的大把时间都耗在了那些滑稽的剧院里。
[charslot(slot = "l", name = "avg_npc_686_1#3$1", focus="l")]
[name="阿尔贝托"]在我刚刚接手家族生意的那一年，我在家里的停车场发现了他的尸体。
[charslot(slot = "l", name = "avg_npc_686_1#8$1", focus="l")]
[name="阿尔贝托"]当时我很愤怒，我知道他平时会得罪什么人，我完全有能力去为他复仇......但我还是放弃了。
[name="阿尔贝托"]德米特里，你知道为什么吗？
[charslot(slot = "r", name = "avg_npc_690_1#7$1", focus="r")]
[name="德米特里"]因为你是个冷血的人。
[charslot(slot = "l", name = "avg_npc_686_1#9$1", focus="l")]
[name="阿尔贝托"]哈哈，我不会把这当作冒犯......但这个答案还不够准确。
[charslot(slot = "l", name = "avg_npc_686_1#1$1", focus="l")]
[name="阿尔贝托"]很简单，太多人都误会了“家族”的含义。
[name="阿尔贝托"]家族成员之间的联系从来不是义务，而是需要维护的投资。人们至少要有共同的目的和站在一起的决心，才能自称为家族。
[charslot(slot = "l", name = "avg_npc_686_1#2$1", focus="l")]
[name="阿尔贝托"]我的那位兄弟，在他选择了和我不一样的路的那一刻，他就不再是家族的一员了。
[charslot(slot = "r", name = "avg_npc_690_1#7$1", focus="r")]
[name="德米特里"]你想说什么？
[charslot(slot = "l", name = "avg_npc_686_1#5$1", focus="l")]
[name="阿尔贝托"]我不喜欢与人争辩，做生意最重要的是寻找共识。
[name="阿尔贝托"]如果你真的很在意伤害了你兄弟的凶手，你应该去找市政厅寻求合作。在这里，我们要谈的只有生意。
[dialog]
[charslot(slot = "l", focus="n")]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_npc_686_1#1$1", focus="l")]
[name="阿尔贝托"]时间差不多了。我的日程排得很满，该见下一位客人了。
[charslot(slot = "r", name = "avg_npc_690_1#7$1", focus="r")]
[name="德米特里"]......
[name="德米特里"]阿尔贝托，我和莱昂的恩怨，我会亲自去跟他算清楚......但这和你没有关系。
[name="德米特里"]别让我发现你在做过线的事。
[dialog]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", posfrom="0,0", posto="200,0", afrom=1, ato=0, duration=1.5)]
[delay(time=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[playMusic(key="$formal_loop", volume=0.6)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
转过一排酒架，阿尔贝托重新回到那张长长的品酒桌边。
他不喜欢迟到，但有些时候，有些客人，让他们适当地等待往往很有必要。
[charslot(slot = "l", name = "avg_npc_686_1#9$1", focus="l")]
[name="阿尔贝托"]想要见你一面并不容易，伊雷妮小姐。
[name="阿尔贝托"]我没记错的话，我应该已经邀请过你许多次。你今天主动到访，让我倍感惊喜。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", posfrom="200,0", posto="0,0", duration=1.5)]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", focus="r")]
[name="伊雷妮"]......
[charslot(slot = "l", name = "avg_npc_686_1#1$1", focus="l")]
[name="阿尔贝托"]我知道你的来意，伊雷妮小姐。
[name="阿尔贝托"]你是想将那辆闯了祸的卡车，连带着车上的货物，统统转交给我。
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", focus="r")]
[name="伊雷妮"]是、是的。
[charslot(slot = "l", name = "avg_npc_686_1#9$1", focus="l")]
[name="阿尔贝托"]将自己惹上的麻烦，转移到家族与家族之间，你很聪明。
[charslot(slot = "l", name = "avg_npc_686_1#1$1", focus="l")]
[name="阿尔贝托"]所以......我拒绝。
[charslot(slot = "r", name = "avg_npc_1542_1#5$1", focus="r")]
[name="伊雷妮"]阿尔贝托先生，为什么？
[charslot(slot = "l", name = "avg_npc_686_1#1$1", focus="l")]
[name="阿尔贝托"]整件事情和萨卢佐没有任何关系。
[name="阿尔贝托"]你应该也知道，因为过去在沃尔西尼的事情，我们被市政厅盯得很紧，完全没有必要在这时候引火上身。
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[name="伊雷妮"]可是，这对您来说也是一个难得的机会不是吗？
[name="伊雷妮"]短短一年时间，新沃尔西尼的重要街区几乎都能看见威尼斯载具公司的售卖点和检修站......
[name="伊雷妮"]可如果他们偷运违禁品的证据在您手里，您可以去找他们谈判，也可以交出去，缓和与市政厅的关系......
[name="伊雷妮"]无论怎样，对您都是有好处的，不是吗？
[name="伊雷妮"]而您只需要让昨天晚上的事情和卡车互助会不再有任何关系——这对您来说应该不难。
[dialog]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_686_1#8$1", focus="l")]
[name="阿尔贝托"]为什么选择萨卢佐？
[charslot(slot = "r", name = "avg_npc_1542_1#5$1", focus="r")]
[name="伊雷妮"]您说什么？
[charslot(slot = "l", name = "avg_npc_686_1#5$1", focus="l")]
[name="阿尔贝托"]美第奇的投资公司、雷欧帝的药店、吉诺维斯的制糖工坊、洛卡的钢材厂......被迫改头换面进入新沃尔西尼的家族比比皆是。
[name="阿尔贝托"]你的选择明明有很多。
[charslot(slot = "r", name = "avg_npc_1542_1#4$1", focus="r")]
[name="伊雷妮"]......对我来说，这没有任何区别。
[name="伊雷妮"]我们这些司机只是想在这座新城市找个新活路，我们看不明白，也不想去管灰厅发生了什么变化，十二家族谁变强了谁变弱了......
[charslot(slot = "l", name = "avg_npc_686_1#1$1", focus="l")]
[name="阿尔贝托"]所以这个答案才显得尤为重要。
[dialog]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", focus="r")]
[name

... (全文21492字符)
```

### level_act38side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="56_g7_tailorshop",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Delay(time=2)]
[Subtitle(text="每一位猎人进入荒野前都会遇见狼。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="狼说，柘木做的弓很坚韧，石头磨出的刀很锋利，但要想活下来，就脱下你们为保护皮肉而穿上的衣物，唯独那不属于荒野。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="没有人相信。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="所以那穿着长袍大氅的猎人......被突出的树根绊住衣角，被藤蔓缠裹得动弹不得，直到闻声而来的野兽将他包围。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="所以那用甲胄将自己武装得严严实实的猎人......湍急的河水灌进他盔甲的缝隙，将他拖入河底腥臭的泥沙之中。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="只有一位猎人相信了这个忠告，他因此得到了狼的礼物。狼将自己的皮毛完整地撕下，披在了猎人的身上。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="皮毛是如此贴合他的身体，仿佛与他生而为一，它帮助猎人在无数危机中穿梭却又毫发无伤。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="那身皮毛又是如此顺滑光洁，猎人离开荒野的时候，它的表面甚至连血迹都不曾留下。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="猎人再也没有脱下它——", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月1日    8:10 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_4155_talr_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_npc_1543_1#9$1",focus="r")]
[name="翁贝托"]以至于猎人的后代，都习惯了这样挺括又舒适的穿着......慢慢地，它发展成了叙拉古人如今最常穿的套装。
[charslot(slot = "left", name = "avg_4155_talr_1#4$1",focus="l")]
[name="卢奇诺"]......爷爷，这没头没尾的故事，我几岁的时候您就在讲，我都十几岁了，您还在讲。
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]......
[name="翁贝托"]卢奇诺，这两套套装已经做得差不多了，现在就剩下纽扣没有加上去。
[name="翁贝托"]既然你已经自作主张替店里接下了订单，不管客人是什么身份，我们都不能马虎。
[name="翁贝托"]去里屋把那几枚特制的纽扣取来，上面有萨卢佐的家徽，你不会认错的。
[charslot(slot = "left", name = "avg_4155_talr_1#1$1",focus="l")]
[name="卢奇诺"]可按您教的规矩，我们不应该先带着这两套衣服去找那位拉普兰德小姐试衣，修改完再——
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]不必了，那位萨卢佐家的小姐并不需要。衣服合身与否，我会判断。
[charslot(slot = "left", name = "avg_4155_talr_1#6$1",focus="l")]
[name="卢奇诺"]可她下单时没提过这个要求......
[charslot(slot = "right", name = "avg_npc_1543_1#2$1",focus="r")]
[name="翁贝托"]我知道你在期待什么，孩子。
[charslot(slot = "right", name = "avg_npc_1543_1#3$1",focus="r")]
[name="翁贝托"]有时，客人们对套装的要求繁琐细致，有时却又含糊其辞，但我们都不能多问。
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]记住，卢奇诺，德蒙塔诺信誉好的原因，绝不仅仅是懂得量体裁衣。
[name="翁贝托"]人和料子没什么不同，我们得自己判断，哪些料子能碰，哪些料子碰不得。
[name="翁贝托"]去拿纽扣吧，这单生意该结了。
[charslot(slot = "left", name = "avg_4155_talr_1#1$1",focus="l")]
[name="卢奇诺"]嗯......好。
[charslot(slot = "m", focus = "n")]
卢奇诺看着那两套无比华丽的礼服，它们与过往爷爷所经手的任何一套套装都不一样。
无疑，那是能冠以“德蒙塔诺出品”的杰作。他多希望，自己也能参与其中。
卢奇诺下意识摸了摸自己的口袋，里面安静地放着几枚他私下做好的纽扣，上面刻着萨卢佐家的标志。
[charslot(slot = "left", name = "avg_4155_talr_1#1$1",focus="l")]
[name="卢奇诺"]我很快就拿过来，爷爷。
[dialog]
[playsound(key="$rungeneral",volume=0.7)]
[charslot(slot = "l",posfrom = "0,0", posto = "200,0",duration = 0.8)]
[charslot(slot = "l",afrom = 1, ato = 0,duration = 0.8)]
[delay(time=2.5)]
[charslot(slot = "right", name = "avg_npc_1543_1#2$1",focus="r")]
[name="翁贝托"]......唉。
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]您已经在门外站很久了，请进吧。
[dialog]
[delay(time=0.5)]
[playsound(key="$dooropenquite")]
[playsound(key="$d_avg_doorbell",channel="1",volume=0.5)]
[delay(time=0.5)]
[charslot(slot = "left", name = "avg_npc_1555_1#1$1",duration = 1,posfrom = "0,0", posto = "0,0")]
[delay(time=1.5)]
[charslot(slot = "l",focus="l")]
[name="家族成员"]老翁贝托，安东尼奥先生交代的差事实在没法拖了。
[name="家族成员"]老家主已经快到新沃尔西尼了，现在去还赶得上在狂欢节巡游之前替他把新衣做好。
[name="家族成员"]推掉其他所有的委托，和我去一趟威尼斯载具公司，不会花上太久的。
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]......现在我手上的这份委托，我同样得罪不起。
[dialog]
[charslot]
[playsound(key="$d_avg_walkfast")]
[charslot(slot = "m", name = "avg_4155_talr_1#5$1",duration = 0.7)]
[delay(time=1)]
[name="卢奇诺"]爷爷，我听到了有客人来！
[charslot(slot = "m", name = "avg_npc_1555_1#1$1")]
[name="家族成员"]......老翁贝托，其实量体这种小事，也不必你亲自去。
[name="家族成员"]小子，想去见见真正的大人物吗？
[dialog]
[charslot]
[charslot(slot = "left", name = "avg_4155_talr_1#5$1",focus="l")]
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="l")]
[name="卢奇诺"]嗯？大、大人物？爷爷，我——
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]卢奇诺，先把纽扣给我。
[charslot(slot = "left", name = "avg_4155_talr_1#5$1",focus="l")]
[name="卢奇诺"]是、是！
[charslot(slot = "left", name = "avg_4155_talr_1#1$1",focus="l")]
[name="卢奇诺"]......在这，爷爷。
[dialog]
[charslot(slot = "l",posfrom = "0,0", posto = "50,0",duration = 0.8,isblock=true)]
[delay(time=0.5)]
[charslot(slot = "l",posfrom = "50,0", posto = "0,0",duration = 0.7,isblock=true)]
[charslot(slot = "m", focus = "n")]
小裁缝紧张地盯着爷爷的脸。
[charslot(slot = "right", name = "avg_npc_1543_1#3$1",focus="r")]
[name="翁贝托"]......
[charslot(slot = "left", name = "avg_4155_talr_1#6$1",focus="l")]
[name="卢奇诺"]......
[charslot(slot = "right", name = "avg_npc_1543_1#9$1",focus="r")]
[name="翁贝托"]还不错。
[charslot(slot = "left", name = "avg_4155_talr_1#12$1",focus="l")]
[name="卢奇诺"]——！
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]但还达不到能用在这两套衣服上的标准，卢奇诺。
[charslot(slot = "left", name = "avg_4155_talr_1#5$1",focus="l")]
[name="卢奇诺"]可、可我比较了很久，它们没什么不同！
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]等你缝的扣子够多了，你也能在摸到它们的时候就知道

... (全文32778字符)
```

### level_act38side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="56_g12_saluzzowinery",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月6日    8:20 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_701_1#1$1",duration = 1)]
[delay(time=2)]
[name="伪装的警察A"]我推荐你尝尝这一款“酸红舌苔”，据说是从萨米弄回来的方子。
[dialog]
[charslot(slot = "r", name = "avg_npc_702_1#1$1",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "r",focus="r")]
[name="伪装的警察B"]你疯了，马内？让其他客人看到我们在酒庄里点了调制酒，结账走人之前我们会一直被嘲笑的！
[charslot(slot = "l",focus="l")]
[name="伪装的警察A"]咳咳，可我们上个月在哥伦比亚旅游的时候不是刚刚尝过类似的酒吗？
[name="伪装的警察A"]我只是有点怀念我们的蜜月了，亲爱的。
[name="伪装的警察A"]（别忘了老师在警校教的卧底课程，有时候我们反而得显眼些，帮其他人打打掩护。）
[name="伪装的警察A"]（大法官安排其他人把无关人员请离还需要时间。）
[charslot(slot = "r",focus="r")]
[name="伪装的警察B"]（......真不是你自己想要喝？）
[charslot(slot = "l",focus="l")]
[name="伪装的警察A"]我发誓，亲爱的！
[charslot(slot = "r",focus="r")]
[name="伪装的警察B"]闭、闭嘴......小声点，马内！
[charslot]
[name="？？？"]我还以为他的新沃尔西尼会更加宽容些。
[name="？？？"]女士，如果你愿意，我可以请你喝一杯酒。当然，也是调制酒。
[dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_690_1#1$1",duration=1.5)]
[delay(time=2)]
[name="德米特里"]就当是入乡随俗。
[dialog]
[charslot]
[charslot(slot = "r", name = "avg_npc_702_1#1$1",focus="r")]
[charslot(slot = "left", name = "avg_npc_701_1#1$1",focus="r")]
[name="伪装的警察B"]（马内，他过来了......）
[charslot(slot = "l",focus="l")]
[name="伪装的警察A"]先生，谢谢你的好意，但还轮不到你请我的——
[dialog]
[charslot]
[stopmusic(fadetime=2)]
[charslot(slot="m",name="avg_npc_690_1#1$1")]
[name="德米特里"]我想你误会了，警察先生，我要请的人不是你们。
[dialog]
[charslot]
[charslot(slot = "r", name = "avg_npc_702_1#1$1",focus="l")]
[charslot(slot = "left", name = "avg_npc_701_1#1$1",focus="l")]
[name="伪装的警察A"]——！
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_690_1#1$1")]
[name="德米特里"]好久不见，拉维妮娅。
[name="德米特里"]愿意坐下喝一杯吗？你在黑暗的角落里站了很久。
[dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4065_judge_1#1$1",duration=1)]
[delay(time=1.5)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[name="拉维妮娅"]我刚刚还在想，到底要多长时间你才会想结账走人。
[charslot(slot="m",name="avg_npc_690_1#1$1")]
[name="德米特里"]在这，我不用结账。萨卢佐从不亏待他们邀请的贵客。
[name="德米特里"]况且我来之前，阿尔贝托就给所有属于他的酒庄提前打好了招呼。“请随意品鉴”，他的原话。
[charslot(slot="m",name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]我之前从来不知道，你和萨卢佐家族关系这么好。你和阿尔贝托有什么合作？总不会是在这里当调酒师吧？
[charslot(slot="m",name="avg_npc_690_1#9$1")]
[name="德米特里"]......
[dialog]
[playsound(key="$d_avg_chairrub")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image(image="56_i30",screenadapt="coverall", xScale=1.1, yScale=1.1,x=70)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1,duration=60,xTo=0)]
[playsound(key="$pourwater")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="德米特里"]拉维妮娅，我不是来接受你的审讯的。
[name="德米特里"]我很在意莱昂的状况，这是我们今晚在这里碰面的唯一原因。
[charslot(slot="m",name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]“他还在昏迷”“他还没摆脱生命危险”......你期望听到什么样的答案？还是说，你害怕听到什么样的答案？
[charslot(slot="m",name="avg_npc_690_1#9$1")]
[name="德米特里"]你今天愿意来见我，至少说明，情况没有到最差的那一步。
[name="德米特里"]......我还是不能见他？
[charslot(slot="m",name="avg_4065_judge_1#2$1")]
[name="拉维妮娅"]不用问你明知道答案的问题。
[charslot(slot="m",name="avg_npc_690_1#9$1")]
[name="德米特里"]莱昂是我的兄弟，我希望他平安，就是这么简单。
[charslot(slot="m",name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]他是你的兄弟，还是贝洛内家族的叛徒？
[charslot(slot="m",name="avg_npc_690_1#9$1")]
[name="德米特里"]拉维妮娅，贝洛内家族每一个留下的人，都有理由恨他。
[name="德米特里"]我也恨他，我不认同莱昂当初的选择和如今的做法，但我不会用如此下作的手段对付他。
[charslot(slot="m",name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]这些话不能成为你洗脱嫌疑的证词。
[name="拉维妮娅"]莱昂是在与你碰面之前出事的，你当时就坐在离案发现场不远的餐厅里。你的嫌疑极大。
[charslot(slot="m",name="avg_npc_690_1#9$1")]
[name="德米特里"]那么，拉维妮娅法官，你准备怎么做？你想把我押回去再慢慢审问？我知道在座的许多“客人”都是警察。
[charslot(slot="m",name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]......在没有明确证据之前，我不会抓捕你。这就是法律的意义，和家族的“规则”不同。
[name="拉维妮娅"]但我对你的疑虑不会消除。
[name="拉维妮娅"]我会查到的，不论你有没有做什么，不论是谁卷入其中。我一定会查清楚真相。
[charslot(slot="m",name="avg_npc_690_1#9$1",focus="n")]
德米特里看着拉维妮娅坚定的眼神，叹了一口气。
[charslot(slot="m",name="avg_npc_690_1#9$1")]
[name="德米特里"]拉维妮娅，你一点也没变，还是当初那个刚当上法官，就敢当面质问首领的家伙。
[name="德米特里"]我一直没那么喜欢你，但......谢谢你替我照顾莱昂。
[name="德米特里"]而且，我还是要说。关于莱昂的意外，我和你一样想要知道凶手是谁......我也会去验证。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_decap",delay=1)]
德米特里取过一直放在旁边的一瓶酒，轻轻拔下塞子。
瓶子里晃晃荡荡的，只剩了小半瓶酒。
[dialog]
[charslot(slot="m",name="avg_npc_690_1#9$1",duration=0.5)]
[delay(time=1)]
[name="德米特里"]别人送我的酒，本来是打算请莱昂的。本来坐在这的，应该是他......
[name="德米特里"]总之，这杯就算我请你的。
[name="德米特里"]拉维妮娅，我真不能见他？
[charslot(slot = "m", focus = "n")]
他靠在桌边，等待着拉维妮娅的回答。
但法官看着眼前杯中的红酒，没有说话。
[charslot(slot="m",name="avg_npc_690_1#1$1")]
[name="德米特里"]好。那我继续待在这也没什么意思了。
[name="德米特里"]我现在离开，各位应该不会拦我吧？
[name="德米特里"]还是说，你准备用《新都市管理法案》中审查家族的特别程序扣留我？
[charslot(slot="m",name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]这里已经没有家族了，德米特里。
[charslot(slot="m",name="avg_npc_690_1#2$1")]
[name="德米特里"]......那我是不是应该走了？
[charslot(slot="m",name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]请便。
[dialog]
[charslot(slot="m",name="avg_npc_690_1#9$1")]
[delay(time=0.5)]
[charslot(duration=1)]
[playsound(key="$d_gen_walk_n")]
[delay(time=1.5)]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[image]
[Background(image="33_g10_smallrestaurant",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[delay(time=1)]
[playsound(key="$d_avg_dishes")]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_npc_1545_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_686_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot =

... (全文23840字符)
```

### level_act38side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="56_g1_newvolsiniistreet_d",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$mist_intro",key="$mist_loop", volume=0.6)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月7日    8:30 A.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_1553_1#1$2",duration = 1)]
[charslot(slot = "right", name = "avg_4065_judge_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1553_1#1$2",focus="l")]
[name="警察"]拉维妮娅法官，那个沃尔珀刚刚在这片区域被目击到过。
[name="警察"]她很敏锐，几乎一天换一个住所。我们调查了她这段时间去过的所有地方，才锁定了她的大致位置。
[charslot(slot = "right", name = "avg_4065_judge_1#8$1",focus="r")]
[name="拉维妮娅"]......“英格丽·威尼斯”。
[charslot(slot = "right", name = "avg_4065_judge_1#1$1",focus="r")]
[name="拉维妮娅"]当年还在法律学校读书时，教授法理学的老师曾经提到过这个名字，我昨晚一时间竟然没有想起来。
[name="拉维妮娅"]她当时说，叙拉古残忍与争斗的气质并非来自常居于此的种族，而是源于这片土地本身......
[name="拉维妮娅"]所以温顺的沃尔珀来到叙拉古后，也会被浸染成“比狼更狠的沃尔珀”——我们的法律便是要约束这种必然的演化。
[charslot(slot = "left",focus="l")]
[name="警察"]英格丽曾在五座移动城市的法院留下了二十余份卷宗，每一份都对应着威尼斯家族在当地势力的迅速扩张......
[name="警察"]而家族也总是会想尽办法帮她从仇杀和审判中脱身。
[name="警察"]有传言说，在家族内部，她甚至比老威尼斯的亲生女儿更得他喜欢。
[name="警察"]但在1094年，英格丽突然离开了家族。
[charslot(slot = "right", name = "avg_4065_judge_1#4$1",focus="r")]
[name="拉维妮娅"]离开？
[charslot(slot = "left",focus="l")]
[name="警察"]准确说，是叛逃。
[name="警察"]当时威尼斯家族的载具公司进驻特尔尼城，唐克雷蒂家族为了抢夺当地的合金资源主动挑衅，冲突愈演愈烈，最终诉诸暴力。
[name="警察"]同在灰厅的两大家族斗得不可开交，老威尼斯本人在当时都遭到了暗杀......
[name="警察"]那段时间，英格丽展开了对唐克雷蒂家族高层的袭杀，连续犯下了十多起命案。
[name="警察"]诡异的是，当西西里夫人亲自下场，双方终于能够坐下来谈判时，英格丽却罔顾家主的命令，并未停下自己的行动。
[name="警察"]我看过当时的记录，她所使用的手段......令人胆寒。
[charslot(slot = "right", name = "avg_4065_judge_1#1$1",focus="r")]
[name="拉维妮娅"]......
[name="拉维妮娅"]原因？
[charslot(slot = "left",focus="l")]
[name="警察"]不明。
[name="警察"]总之英格丽的行为无异于公然挑衅西西里夫人的权威，而她本人却在犯案后销声匿迹......
[name="警察"]整个威尼斯家族都被迁怒，差点重蹈德克萨斯家族的覆辙。
[charslot(slot = "right", name = "avg_4065_judge_1#8$1",focus="r")]
[name="拉维妮娅"]......
[charslot(slot = "m", focus = "n")]
年轻的法官想象着那个沃尔珀女性在城市中杀人如麻的样子，以及昨天在酒庄里，她嘴角始终挂着的微笑。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Image(image="56_i04_1",screenadapt="coverall", xScale=1.6, yScale=1.6,x=-180)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="拉维妮娅"]......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[charslot(slot = "left", name = "avg_npc_1553_1#1$2")]
[charslot(slot = "right", name = "avg_4065_judge_1#8$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "left",focus="l")]
[name="警察"]拉维妮娅法官？
[charslot(slot = "right", name = "avg_4065_judge_1#1$1",focus="r")]
[name="拉维妮娅"]一个身负血案、叛逃出家族的顶尖杀手，突然出现在新沃尔西尼......又恰逢狂欢节期间。不能放任她自由行动。
[charslot(slot = "left",focus="l")]
[name="警察"]您的意思是......
[charslot(slot = "right", name = "avg_4065_judge_1#1$1",focus="r")]
[name="拉维妮娅"]已经进驻新沃尔西尼的家族都接受过背景审查，每一个成员、每一件武器都被登记在册，接受严格管控......
[name="拉维妮娅"]英格丽这样的人，无论是否出自她的本意，她都极有可能成为某些人手里的刀。
[name="拉维妮娅"]不管怎么样，先控制住她。
[charslot(slot = "left",focus="l")]
[name="警察"]是。可......这片区域很大，我们还做不到准确定位她的位置。
[charslot(slot = "right", name = "avg_4065_judge_1#1$1",focus="r")]
[name="拉维妮娅"]如果关于她和她女儿的情报无误，我很确定她一定会去一个地方。
[charslot(slot = "m", focus = "n")]
拉维妮娅看向了不远处一块不起眼的招牌——“罗德岛办事处”。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="bg_offce",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_970_1#1$1",duration = 1)]
[charslot(slot = "l", name = "avg_npc_501_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "r", focus="r")]
[name="工程部干员"]唉，因为狂欢节，我常去采购材料的那家店今天也要开始休假了。
[name="工程部干员"]得提前在终端上把办事处的物资储备状况更新一下了。
[name="工程部干员"]伺夜干员的状况如何？本舰调派来支援的医生去了医院之后到现在都没有消息。
[charslot(slot = "l", focus="l")]
[name="医疗部干员"]不知道。这次本舰支援行动的保密级别很高，我的权限不够，没法查询伺夜干员最新的监测数据。
[name="医疗部干员"]我去找过斥罪小姐，她似乎也并不想透露太多。
[charslot(slot = "r", focus="r")]
[name="工程部干员"]相信同事吧。我们只需要完成相关的后勤保障工作就行。
[charslot(slot = "l", focus="l")]
[name="医疗部干员"]欸......PRTS更新了公告，“通过提高新沃尔西尼办事处安保等级的申请”，发起人是......
[name="医疗部干员"]斥罪小姐？
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=1)]
[delay(time=1)]
[charslot(slot="m",name="avg_4014_lunacu_1#6$2",duration=1)]
[delay(time=2)]
[name="子月"]这里也有罗德岛的安全屋......看来罗德岛的人就像牙兽一样，会为自己挖很多个巢穴。
[charslot(slot="m",name="avg_4014_lunacu_1#2$2")]
[name="子月"]呼呼......不要惊扰其他人，抓紧时间恢复体力——
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$d_avg_hungry",volume=1)]
“咕——”
子月缩在天花板与通风管道之间，有些无奈地按了按自己瘪瘪的肚子。
[charslot(slot="m",name="avg_4014_lunacu_1#7$2")]
[name="子月"]......还有甜甜的、蜜糖的味道。
[charslot(slot="m",name="avg_4014_lunacu_1#8$2")]
[name="子月"]不行，得打起精神。趁有时间，我要把手里的箭打磨得更锋利些——
[charslot(slot="m",name="avg_4014_lunacu_1#6$2")]
[name="子月"]可以先去吃饭？阿涅塞，可之前你不是教我，狩猎的过程里要有耐心——
[name="子月"]......
[charslot(slot="m",name="avg_4014_lunacu_1#8$2")]
[name="子月"]我不想阿涅塞输，我的肚子可以等。
[name="子月"]就是这样，其他事我会听阿涅塞的，但是这件事，我不想让阿涅塞失望。
[dialog]
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[delay(time=1)]
子月缩在角落里，近乎本能地握紧了手中的弓，瞄准。
[charslot(slot="m",name="avg_4014_lunacu_1#8$2")]
[name="子月"]（不是狼，是阿涅塞也讨厌的味道。）
[dialog]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4026_vulpis_1#2$1",duration=1.5)]
[delay(time=2)]
[name="英格丽"]我的鼻子没那么灵，分不清你是哪一个。
[name="英格丽"]但我知道你们中有一个躲在这。
[name="英格丽"]我给你十秒的时间，离开这个地方，我会在外面等你。
[name="英格丽"]当然，要绕开罗德岛的人解

... (全文27533字符)
```

### level_act38side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="56_g7_tailorshop",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月7日    11:40 A.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot = "left", name = "avg_4026_vulpis_1#2$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1543_1#6$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_npc_1543_1#6$1",focus="r")]
[name="翁贝托"]英格丽女士，你刚刚说，那孩子其实是被威尼斯家族的人带走了？
[charslot(slot = "left", name = "avg_4026_vulpis_1#2$1",focus="l")]
[name="英格丽"]告诉我消息的那个人没有欺骗我的道理。
[charslot(slot = "right", name = "avg_npc_1543_1#5$1",focus="r")]
[name="翁贝托"]卢奇诺当天晚上确实去了港口区，听说当时那里发生了一场车祸。
[charslot(slot = "left", name = "avg_4026_vulpis_1#2$1",focus="l")]
[name="英格丽"]是的，我当时也在离现场不远的地方。
[name="英格丽"]估计和威尼斯家族脱不了干系，如果没猜错的话，卢奇诺应该是正好发现了一些什么。
[charslot(slot = "right", name = "avg_npc_1543_1#5$1",focus="r")]
[name="翁贝托"]唉。
[dialog]
[charslot(slot = "right", name = "avg_npc_1543_1#2$1",focus="r")]
[charslot(slot = "m", focus = "all")]
[delay(time=1.5)]
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]英格丽女士，请你离开吧，我今天得提前关店了。
[charslot(slot = "left", name = "avg_4026_vulpis_1#6$1",focus="l")]
[name="英格丽"]你要自己去找小威尼斯？
[charslot(slot = "right", name = "avg_npc_1543_1#3$1",focus="r")]
[name="翁贝托"]......
[charslot(slot = "left", name = "avg_4026_vulpis_1#2$1",focus="l")]
[name="英格丽"]翁贝托，我不知道你过去是怎样的人。但我相信，即使是瓦古选中的人，也拿衰老没什么办法。
[name="英格丽"]一个病弱的老裁缝，可能连小威尼斯宅邸的门都进不去。
[charslot(slot = "right", name = "avg_npc_1543_1#5$1",focus="r")]
[name="翁贝托"]如果卢奇诺真知道了他不该知道的事情，那他可能没办法再从威尼斯家出来了。
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]英格丽女士，我已经垂垂老矣，哪怕没这档子事，我也快跟时间熬到头了。
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]非要说我还有什么对付不过去的事情，也就是这孩子。
[name="翁贝托"]他是我唯一的亲人，这也不算什么，可谁让我是他唯一的亲人呢。他还那么小，在孩子的事上，我们总是没什么办法。
[charslot(slot = "left", name = "avg_4026_vulpis_1#2$1",focus="l")]
[name="英格丽"]......
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]况且，威尼斯家，对我来说也没那么陌生。
[charslot(slot = "left", name = "avg_4026_vulpis_1#2$1",focus="l")]
[name="英格丽"]嗯？
[charslot(slot = "right", name = "avg_npc_1543_1#3$1",focus="r")]
[name="翁贝托"]其实我还隐瞒了你一件事——我其实算是你的前辈。
[name="翁贝托"]这算是，瓦古选择我的理由吧。
[charslot(slot = "right", name = "avg_npc_1543_1#2$1",focus="r")]
[name="翁贝托"]......唉，兜兜转转一大圈，结果又绕了回去。
[dialog]
[charslot(slot = "m", focus = "all")]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_4026_vulpis_1#2$1",focus="l")]
[name="英格丽"]我和你一起去。
[charslot(slot = "right", name = "avg_npc_1543_1#1$1",focus="r")]
[name="翁贝托"]英格丽女士......这件事本身和你没什么关系。
[name="翁贝托"]你发现了那孩子的线索，主动来告知我，我已经很感激了。
[name="翁贝托"]因为丽萨小姐的事，你当时和威尼斯家族闹得非常不愉快，贸然回去的话，想必会有不少麻烦。
[charslot(slot = "left", name = "avg_4026_vulpis_1#2$1",focus="l")]
[name="英格丽"]这个用不着你操心，我与瓦古有约在先。在当年的事情水落石出之前，你没有资格出事。
[charslot(slot = "left", name = "avg_4026_vulpis_1#3$1",focus="l")]
[name="英格丽"]而且，我很理解一个人为了自己的孩子会愿意付出什么。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="33_g11_mansionhall",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_4155_talr_1#6$1",duration=1)]
[delay(time=2)]
[name="卢奇诺"]......有人来了吗？我能离开了吗？
[charslot(slot = "m", focus = "n")]
[name="？？？"]孩子的声音？
[dialog]
[charslot]
[playsound(key="$d_avg_key")]
[delay(time=1.5)]
[playsound(key="$dooropenquite")]
[charslot(slot="m",name="avg_npc_1545_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1545_1#6$1")]
[name="老威尼斯"]刚刚是你在说话吗，孩子？
[charslot(slot="m",name="avg_4155_talr_1#7$1")]
[name="卢奇诺"]......
[charslot(slot="m",name="avg_npc_1545_1#6$1")]
[name="老威尼斯"]你在害怕我？
[charslot(slot="m",name="avg_4155_talr_1#6$1")]
[name="卢奇诺"]求您了，能不能让我回家？
[charslot(slot="m",name="avg_npc_1545_1#1$1")]
[name="老威尼斯"]我只是恰巧来这里做客，恐怕没法插手主人家的事。是什么原因让他们把你留在这？
[charslot(slot="m",name="avg_4155_talr_1#6$1")]
[name="卢奇诺"]我、我不知道。如果、如果您也没法做主......能否替我通知德蒙塔诺裁缝店的翁贝托·德蒙塔诺一声？
[charslot(slot="m",name="avg_npc_1545_1#3$1")]
[name="老威尼斯"]翁贝托......
[charslot(slot="m",name="avg_4155_talr_1#6$1")]
[name="卢奇诺"]他是我的爷爷，我离开太久了他会担心。还有我从药店给他取的药，他很需要那些，如果我不能、不能......
[charslot(slot="m",name="avg_npc_1545_1#1$1")]
[name="老威尼斯"]你在担心你的爷爷？
[charslot(slot="m",name="avg_4155_talr_1#6$1")]
[name="卢奇诺"]嗯。
[charslot(slot="m",name="avg_npc_1545_1#1$1")]
[name="老威尼斯"]跟着我吧，威尼斯家向来不会为难客人。
[charslot(slot="m",name="avg_npc_1545_1#3$1")]
[name="老威尼斯"]没想到，我来这一趟还能遇到其他意料之外的朋友。
[name="老威尼斯"]好在，我喜欢热闹。
[charslot(slot="m",name="avg_4155_talr_1#6$1")]
[name="卢奇诺"]就这么跟着您走吗......外面那些人......
[charslot(slot="m",name="avg_npc_1545_1#7$1")]
[name="老威尼斯"]他们也正忙着招待我这个客人呢。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[playsound(key="$doorclosequite")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
卢奇诺紧紧跟在老人的身后，一路上竟然没有遇到任何一个人。
[dialog]
[charslot(slot = "left", name = "avg_npc_1545_1#1$1",duration = 0.5)]
[charslot(slot = "right", name = "avg_4155_talr_1#6$1",duration = 0.5)]
[delay(time=1)]
[charslot(slot = "right", name = "avg_4155_talr_1#6$1",focus="r")]
[name="卢奇诺"]......您、您到底是谁？
[charslot(slot = "left", name = "avg_npc_1545_1#7$1",focus="l")]
[name="老威尼斯"]跟紧了，孩子，这栋宅子大得很。我们马上就到了。
[name="老威尼斯"]你刚刚不是说，有很多事想要我帮忙转告给你的爷爷吗？
[name="老威尼斯"]抱歉，我的年龄大了，记性实在糟糕。
[name="老威尼斯"]不过，我想你可以亲口告诉他。
[charslot(slot = "right", name = "avg_4155_talr_1#5$1",focus="r")]
[name="卢奇诺"]——？！
[charslot(slot = "left", name = "avg_npc_1545_1#3$1",focus="l")]
[name="老威尼斯"]老翁贝托，我真羡慕你有一个爱你的孙子。
[charslot(slot = "right", name = "avg_4155_talr_1#5$1",focus="r")]
[name="卢奇诺"]爷、爷爷？
[dialog]
[charslot]
[delay(time=1)]
[charslot(slot="m",name="avg_

... (全文23368字符)
```

### level_act38side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_iceforest_2",screenadapt="coverall")]
[Delay(time=1)]
[bgeffect(name="$eb_blizzard",layer=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$ghosthunter_intro",key="$ghosthunter_loop", volume=0.6)]
[Subtitle(text="老瓦西里是一位骁勇的皇帝。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="据说他已经年逾八十，依然能头戴宝冠走向战场。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="乌萨斯在雪原深处遭遇了惨败，死难同胞的尸体横于雪中，堆垒成墙。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="皇帝高喊着复仇，他的怒吼压过了风雪。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="残存的将士包围了营帐，但宝冠闪耀，人人只能高呼崇敬吾皇。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="突如其来的剧烈北风吹起了营帐，众人终于敢抬头前望。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="宝冠已经坠落当场。雪原上已经不再有皇帝。据说最终，老瓦西里受众人践踏而亡。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="营帐外跪倒的无名将士千万，无人知晓弑君之人姓甚名谁，又来自何方。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[bgeffect]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "r", name = "char_1002_nsabr_2",duration=1)]
[charslot(slot = "l", name = "char_1502_crowns",duration=1)]
[Delay(time=2)]
[playMusic(key="$calm_loop", volume=0.6)]
[charslot(slot = "r", name = "char_1002_nsabr_2",focus="r")]
[name="整合运动成员"]喔，我头一次听你用叙拉古语讲这个故事。
[name="整合运动成员"]“弑君者”，原来你的名字是从书里来的——那本书叫什么来着？
[charslot(slot = "l", name = "char_1502_crowns",focus="l")]
[name="柳德米拉"]《正当与正义》。
[charslot(slot = "r", name = "char_1002_nsabr_2",focus="r")]
[name="整合运动成员"]太难记了......我以为是那种全是大道理的大部头，原来是故事书？
[charslot(slot = "l", name = "char_1502_crowns",focus="l")]
[name="柳德米拉"]不，它不是故事书。那里面的故事不是用来让人娱乐，而是用来让人警醒。
[name="柳德米拉"]什么是“正当”，什么是“正义”？
[name="柳德米拉"]它们应该彼此混同吗？它们应该彼此矛盾吗？谁来为它们下定义？我们以为自己站在哪一边？
[name="柳德米拉"]还是说，它们其实都不存在。就像......已经完蛋了的整合运动一样。
[name="柳德米拉"]到头来，只是编一些漂亮理由的时候才用得到。
[charslot(slot = "r", name = "char_1002_nsabr_2",focus="r")]
[name="整合运动成员"]嗯......我是说，就是在你给我讲这个故事之前，我只是想问，我们接下来该去哪？
[charslot(slot = "l", name = "char_1502_crowns",focus="l")]
[name="柳德米拉"]这就是我要说的——就在这里分别吧，兄弟。
[name="柳德米拉"]沿着这个方向，一直往前，你就可以走到树林边缘，就能看到旧的移动城市航道。
[name="柳德米拉"]那附近可能会有莱塔尼亚的边检队，也可能会有叙拉古货运陆行舰经过，得小心。
[name="柳德米拉"]你经历过切尔诺伯格和龙门的战斗，避开他们应该不难。
[charslot(slot = "r", name = "char_1002_nsabr_2",focus="r")]
[name="整合运动成员"]唉，足足三十多号人，我是最后一个了......
[name="整合运动成员"]弑君者，我们为什么不能留在一起？
[charslot(slot = "l", name = "char_1502_crowns",focus="l")]
[name="柳德米拉"]留在一起只会成为那些掌权者的靶子，再不然就是再次变成被利用的炮灰。
[name="柳德米拉"]你们不愿跟着九，所以我送你们离开。
[name="柳德米拉"]这是我作为整合运......这是我最后能做的。
[charslot(slot = "r", name = "char_1002_nsabr_2",focus="r")]
[name="整合运动成员"]可是，那你要去哪呢，你不也变成孤零零一个人了吗？
[charslot(slot = "l", name = "char_1502_crowns",focus="l")]
[name="柳德米拉"]走一走，看一看，想一想。
[name="柳德米拉"]离开叙拉古前，我的老师劝过我，我不应该回到乌萨斯报仇，我的力量还太弱，我的觉悟也还不够......我没有听她的。
[name="柳德米拉"]现在或许是时候回去了，我想要去看看她。或许她可以再给我一点建议......可以让我变得更强。
[charslot(slot = "r", name = "char_1002_nsabr_2",focus="r")]
[name="整合运动成员"]你的老师，是个什么样的人？
[charslot(slot = "l", name = "char_1502_crowns",focus="l")]
[name="柳德米拉"]她来自一个叙拉古的家族。她是一个强大的战士，也是我见过最有智慧的人......她教会了我许多。
[charslot(slot = "r", name = "char_1002_nsabr_2",focus="r")]
[name="整合运动成员"]叙拉古，那还有好长一段路吧。
[charslot(slot = "l", name = "char_1502_crowns",focus="l")]
[name="柳德米拉"]兄弟，看看雪地上的这堆篝火。曾经，它可以点燃感染者的愤怒，点燃整合运动的理想，烧遍整个乌萨斯。
[name="柳德米拉"]但是现在，它只够你和我取暖。
[name="柳德米拉"]听我最后跟你说——忘记塔露拉，忘记切尔诺伯格，忘记龙门，忘记整合运动，忘记我们这些人。选择了离开，就不要再去想了。
[name="柳德米拉"]甚至，忘掉身上的结晶吧。也许全忘掉了，你就能回家了。
[charslot(slot = "r", name = "char_1002_nsabr_2",focus="r")]
[name="整合运动成员"]唉......
[name="整合运动成员"]虽然我们都选择了离开，但我一直觉得你和我们是不同的......
[name="整合运动成员"]你看上去懂很多东西，也读过很多书。有时候我觉得，你和大尉、塔露拉他们才更像一类人。
[charslot(slot = "l", name = "char_1502_crowns",focus="l")]
[name="柳德米拉"]......
[charslot(slot = "r", name = "char_1002_nsabr_2",focus="r")]
[name="整合运动成员"]唉......我的意思是，小时候我的爷爷就常说，读书太多的人，都容易钻牛角尖。
[name="整合运动成员"]总之......算了，再见，弑君者，祝你好运。你看上去确实需要一些好运。
[dialog]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[charslot(slot = "r", name = "char_1002_nsabr_2",afrom=1,ato=0,duration=1.5,posfrom = "0,0", posto = "200,0")]
[delay(time=2.5)]
[charslot(slot = "l", name = "char_1502_crowns",focus="l")]
[name="柳德米拉"]我们不会再见了，兄弟。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[bgeffect(name="$eb_rain",layer=1)]
[playsound(key="$d_avg_rainlight_loop", loop=true, channel="bgs",volume=1)]
[Background(image="33_g2_srcalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playsound(key="$d_avg_shallowswalk", loop=true, channel="a")]
[charslot(slot = "m", name = "char_1502_crowns",duration=1)]
[Delay(time=1)]
[StopSound(channel="a", fadetime=1)]
[name="柳德米拉"]唔，尾巴弄湿了。
[name="柳德米拉"]还真是一点都没变。无论是这些脏兮兮的街，还是烦死人的雨。
[name="柳德米拉"]不知道为什么，乌萨斯的雪能要人命，可还是这里的雨更让人不爽。
[name="柳德米拉"]但愿老师家有吹风机......
[dialog]
[charslot(duration=1)]
[playsound(key="$dooropenquite")]
[Delay(time=1)]
[bgeffect]
[playMusic(intro="$kjerag_n_intro",key="$kjerag_n_loop", volume=0.6)]
[StopSound(channel="bgs", fadetime=3)]
[Image(image="33_i16", xScale=1.6, yScale=1.6,y=300, x=350,fadetime=3)]
[ImageTween(duration=10,xTo=250, block=false)]
[Delay(time=2)]
[Image(image="33_i16", xScale=1.7, yScale=1.7,y=300,x=-100, fadetime=1)]
[ImageTween(duration=10,xTo=0, block=false)]
[Delay(time=2)]
[Image(image="33_i16", xScale=1.2, yScale=1.2,y=150, fadetime=1)]
[ImageTween(xScaleTo=0.88, yScaleTo=0.88, duration=30,yTo=-20, block=false)]
[Delay(time=1)]
[name="柳德米拉"]老师！！
化不开的血腥味。
她的老师仰面倒在地上，鲜血仍在向外流淌蔓延。
一把小刀掉落一边。
柳德米拉想要靠近，压住老师仍在流血的伤口，但她发现自己无法挪动一步，她连视线都无法移开。
有一股让她熟悉，又让她恐惧的气息正从阴影中浮现。
穿着红色连帽衫，有着灰色头发的狼。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image]

... (全文22420字符)
```

### level_act38side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="56_g9_truckcamp",screenadapt="coverall")]
[Delay(time=2)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[name="？？？"]索默尔，这是怎么回事？
[name="索默尔"]我也不知道！我正开车呢，发动机出了故障，结果发现这个人就躺在路边。吓我一跳，我还以为是我撞到了人。
[name="索默尔"]这孩子一个人晕倒在荒野上，嘴里还一直念叨着要找一个穿红色连帽衫的家伙。
[name="索默尔"]我想总不能把她扔在那，就先带她回来了......
[name="？？？"]找我？可我完全不认识她啊。
[name="索默尔"]她看上去就是个孤零零的倒霉蛋，或许能留她在营地？我们最近忙成这样，补充一个人手也行啊。
[name="？？？"]索默尔，你明知道互助会的每一个成员都是要经过严格审查的。
[name="？？？"]像她这样的感染......来历不明的人，万一和家族有什么关系怎么办？
[name="索默尔"]唉......
[name="？？？"]医生说她情况还算稳定，等她醒来后，就让她离开吧。
[name="索默尔"]好，好吧。
[name="索默尔"]这个倒霉蛋，怎么还紧紧握着刀不放，多危险啊。先给她——
[dialog]
[bgeffect(name="$eb_dim_openeye",layer=1)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=false)]
[Delay(time=3)]
[PlaySound(key="$d_avg_slap",volume=0.5)]
[CameraShake(duration=0.2, xstrength=20, ystrength=20, vibrato=15, randomness=90, fadeout=true, block=false)]
[name="柳德米拉"]别碰我！
[dialog]
[charslot(slot="m",name="avg_npc_1542_1#1$1",duration=1)]
[Delay(time=2)]
[bgeffect]
[name="穿红色连帽衫的人"]......
[name="穿红色连帽衫的人"]你醒了。
[charslot(slot="m",name="char_1502_crowns")]
[name="柳德米拉"]你——！
[charslot(slot = "m", focus = "n")]
柳德米拉看着眼前的人，很用力地揉了揉眼睛。
[charslot(slot="m",name="char_1502_crowns")]
[name="柳德米拉"]对不起......这是哪里？
[charslot(slot="m",name="avg_npc_1542_1#1$1")]
[name="穿红色连帽衫的人"]这里是新沃尔西尼，卡车互助会。
[charslot(slot="m",name="char_1502_crowns")]
[name="柳德米拉"]是你们救了我......谢谢。
[charslot(slot="m",name="avg_npc_1542_1#1$1")]
[name="穿红色连帽衫的人"]没什么，我们的成员不会对一个晕倒在荒野上的人见死不救。但后面的事，我们没有办法帮你太多。
[name="穿红色连帽衫的人"]我们最多招待你一顿饭，之后就离开吧。索默尔，你来负责这件事。
[dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[charslot(duration=1)]
[delay(time=2.5)]
[charslot(slot="m",name="char_1502_crowns")]
[name="柳德米拉"]谢谢你们的帮助......我这就走。
[charslot(slot = "m",name = "avg_npc_1547_1#1$1")]
[name="索默尔"]别急，年轻人。
[name="索默尔"]保险起见，我还是想问问你......你不是家族的人，对吧？
[charslot(slot="m",name="char_1502_crowns")]
[name="柳德米拉"]......我已经很多年没有听说过这个词了。
[charslot(slot = "m",name = "avg_npc_1547_1#2$1")]
[name="索默尔"]我也觉得，你看上去也不像和那帮人有什么往来。
[name="索默尔"]别在意，伊雷妮只是很担心家族的人会渗入互助会，她要操心的事很多，并不是对你有什么敌意。
[name="索默尔"]你来到营地后的医药费，其实全都是她自掏腰包的。
[charslot(slot="m",name="char_1502_crowns")]
[name="柳德米拉"]谢谢......我明白，我不会给你们添麻烦的。
[name="柳德米拉"]我只是需要花时间想想......接下来该做什么。
[charslot(slot = "m",name = "avg_npc_1547_1#2$1")]
[name="索默尔"]你会开车吗？
[charslot(slot="m",name="char_1502_crowns")]
[name="柳德米拉"]......
[name="柳德米拉"]在乌萨斯开过卡车，算吗？
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[focusout(duration=0, type="bg", from=0, to=1, block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="bg_rhodesbedroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(key="$wasteland_loop", volume=0.4)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Sticker(id="st1", text="红。", x=320,y=340, alignment="center", size=24, delay=0.001, width=700,block = true,duration=1)]
[Sticker(id="st1",duration=1,block = false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
很轻的呢喃，和声音同时出现的，是同样温柔的抚摸。
像是飘落在草地上的树叶，在荒野的背坡处感受到的风，没有危险。
她曾经在这样的呢喃和抚摸中睡去，长大。
在罗德岛，没有人敢对她这样，没有人会对她这样，哪怕是凯尔希。
[charslot(slot = "m",name = "char_144_red_7#7")]
[name="红"]......是外婆？！
[dialog]
[charslot]
[focusout(duration=1, type="char", from=0, to=0.5)]
[charslot(slot = "m", name = "avg_npc_1549_1#1$1", duration=1)]
[Delay(time=2)]
[focusout(duration=0, type="char", from=0, to=0)]
[charslot(slot = "m",name = "char_144_red_7#4")]
[name="红"]外婆，你已经完全看不清东西了吗？
[focusout(duration=0, type="char", from=0.5, to=0.5)]
[charslot(slot = "m",name = "avg_npc_1549_1#1$1")]
[name="外婆"]外婆说过的，外婆的双目被狼吞吃了，这副眼镜只是摆设。
[name="外婆"]只有剜出狼的双目，将它们重新放回外婆的眼眶，外婆才能看清红的模样。
[focusout(duration=0, type="char", from=0, to=0)]
[charslot(slot = "m",name = "char_144_red_7#4")]
[name="红"]外婆也没法抱抱红？
[focusout(duration=0, type="char", from=0.5, to=0.5)]
[charslot(slot = "m",name = "avg_npc_1549_1#1$1")]
[name="外婆"]外婆的双手被狼吞下肚，你要斩断狼的四肢，把双手还给外婆。
[focusout(duration=0, type="char", from=0, to=0)]
[charslot(slot = "m",name = "char_144_red_7#4")]
[name="红"]外婆也没法再教我唱歌？
[focusout(duration=0, type="char", from=0.5, to=0.5)]
[charslot(slot = "m",name = "avg_npc_1549_1#1$1")]
[name="外婆"]外婆也想继续教红唱歌。可狼总在嚎叫，外婆不敢惊到他们。
[focusout(duration=0, type="char", from=0, to=0)]
[charslot(slot = "m",name = "char_144_red_7#4")]
[name="红"]外婆，你为什么这么久才来找红？
[focusout(duration=0, type="char", from=0.5, to=0.5)]
[charslot(slot = "m",name = "avg_npc_1549_1#1$1")]
[name="外婆"]狼太多了，红，他们潜伏在路的两侧。你要割开狼的皮肉，用它们为外婆做一件衣衫。
[focusout(duration=0, type="char", from=0, to=0)]
[charslot(slot = "m",name = "char_144_red_7#4")]
[name="红"]呜......
[name="红"]外婆真的会消失吗？
[focusout(duration=0, type="char", from=0.5, to=0.5)]
[charslot(slot = "m",name = "avg_npc_1549_1#1$1")]
[name="外婆"]乖孩子，这就要看你能不能帮到外婆了。
[focusout(duration=0, type="char", from=0, to=0)]
[charslot(slot = "m",name = "char_144_red_7#4")]
[name="红"]红、红在龙门找到了狼，假的。但她身上有真狼的气味。
[name="红"]在那以后，红还没有新的发现......
[name="红"]唔，外婆，是红没有继续找。
[focusout(duration=0, type="char", from=0.5, to=0.5)]
[charslot(slot = "m",name = "avg_npc_1549_1#1$1")]
[name="外婆"]外婆不会怪红。红是最乖最好的孩子。
[focusout(duration=0, type="char", from=0, to=0)]
[charslot(slot = "m",name = "char_144_red_7#4")]
[name="红"]红不是。红在第一次猎狼的时候就晕倒了，红当时太弱小，凯尔希在草窠里救了红。
[charslot(slot = "m",name = "char_144_red_7#1")]
[name="红"]红暂时跟在她身边，她告诉红很多红不知道的事情。
[charslot(slot = "m",name = "char_144_red_7#3")]
[name="红"]什么是“保护”，什么是“行凶”？什么是“痛苦”，什么是“开心”？什么是红能够分辨的，什么是红能够做到的？
[name="红"]问题很多，也很难。红想不明白。
[focusout(duration=0, type="char", from=0.5, to=0.5)]
[charslot(slot = "m",name = "avg_npc_1549_1#1$1")]
[name="外婆"]“痛苦”？“开心”？
[name="外婆"]是外婆没有照顾好红，反而需要红来救助......
[name="外婆"]孩子，如果你不开心，就继续留在罗德岛。
[name="外婆"]外婆的时间本来也已经不多了。就这样忘记外婆，忘记自己是个猎狼人......
[focusout(duration=0, type="char", from=0, to=0)]
[charslot(slot = "m",name = "char_144_red_7#4

... (全文20354字符)
```

### level_act38side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="56_g2_newvolsiniistreet_n",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$darkness02_intro",key="$darkness02_loop", volume=0.6)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月5日    10:17 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[PlaySound(key="$d_avg_driveincar", volume=0, loop=true, channel="car")]
[SoundVolume(volume=0.4, channel="car",fadetime=1)]
[CameraShake(duration=5, xstrength=2, ystrength=2, vibrato=30, randomness=90, fadeout=true, block=false)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.1, fadetime=0.5)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.1, fadetime=0.5,block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_1547_1#4$1",duration=1)]
[charslot(slot="r",name="avg_1502_crosly_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_1547_1#1$1",focus="l")]
[name="索默尔"]......就是这样，柳德米拉，该说的我都跟你说了。
[charslot(slot="r",name="avg_1502_crosly_1#1$1",focus="r")]
[name="柳德米拉"]你帮威尼斯运的什么货？
[charslot(slot="l",name="avg_npc_1547_1#1$1",focus="l")]
[name="索默尔"]今天晚上是一批轮胎。
[name="索默尔"]基本都是载具生产会用到的耗材，源石引擎、钢件、合金之类的，有时候也有一些冻鳞冻肉酒精药品......
[name="索默尔"]这种事情在叙拉古的其他城市很常见，家族的商品基本都不走正常的报关程序，能避很大一笔税。只不过在新沃尔西尼——
[charslot(slot="r",name="avg_1502_crosly_1#1$1",focus="r")]
[name="柳德米拉"]你不用说那么多，我懂。
[charslot(slot="l",name="avg_npc_1547_1#1$1",focus="l")]
[name="索默尔"]好、好。
[charslot(slot="r",name="avg_1502_crosly_1#1$1",focus="r")]
[name="柳德米拉"]这不是第一次了，对吧？
[charslot(slot="l",name="avg_npc_1547_1#6$1",focus="l")]
[name="索默尔"]嗯......柳德米拉，你今天晚上不跟他们去拍电影，就是因为我？
[charslot(slot="r",name="avg_1502_crosly_1#1$1",focus="r")]
[name="柳德米拉"]不然呢？
[charslot(slot="l",name="avg_npc_1547_1#7$1",focus="l")]
[name="索默尔"]你是从什么时候发现的？
[stopmusic(fadetime=2)]
[Dialog]
[StopSound(channel="car", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="56_g4_newvolsiniialley_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkalley_intro",key="$darkalley_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_1547_1#1$1",duration = 0.5)]
[charslot(slot = "right", name = "avg_npc_1550_1#1$1",duration = 0.5)]
[delay(time=1)]
[charslot(slot = "right",focus="r")]
[name="卡车司机"]你干嘛一直跟着我们？
[charslot(slot = "left", name = "avg_npc_1547_1#8$1",focus="l")]
[name="索默尔"]不好意思，我和鲁杰罗真的很忙！可以请你离开吗？
[charslot]
[charslot(slot="m",name="avg_npc_1555_1#1$1")]
[name="家族成员"]忙到连喝杯咖啡的时间都没有吗？
[name="家族成员"]哎呀，索默尔，鲁杰罗，你们的戒心太重了！
[name="家族成员"]这里是新沃尔西尼，大家都是新沃尔西尼市民，日后相处的时间还长，彼此交流一下感情，还是很有必要的。
[charslot]
[charslot(slot = "r", name = "avg_npc_1550_1#1$1",focus="l")]
[charslot(slot = "left", name = "avg_npc_1547_1#1$1",focus="l")]
[name="索默尔"]......
[charslot]
[charslot(slot="m",name="avg_npc_1555_1#1$1")]
[name="家族成员"]这样吧，我们干脆在你们营地对面开个咖啡馆得了，那么多司机，不愁没生意，而且也方便咱们见面——
[dialog]
[PlaySound(key="$d_avg_smoke_grenade", volume=1)]
[bgeffect(name="$eb_smog",layer=1)]
[Blocker(a=0.5, r=0.7, g=0.7, b=0.7, fadetime=0.5, block=true)]
[name="家族成员"]什么情况，咳咳——哪儿来的这么大的烟，我的眼睛都瞎了——
[dialog]
[PlaySound(key="$punch_n1", volume=1)]
[CameraShake(duration=0.1, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.3)]
[name="家族成员"]哎哟，*叙拉古粗口*谁打我！
[dialog]
[PlaySound(key="$d_avg_punch", volume=1)]
[CameraShake(duration=0.2, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.21)]
[PlaySound(key="$fightgeneral", volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.5)]
[name="家族成员"]哎哟喂——
[dialog]
[Blocker(a=0.7, r=0.7, g=0.7, b=0.7, fadetime=0.5, block=true)]
[bgeffect]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1555_1#1$1")]
[name="家族成员"]......
[charslot]
[charslot(slot = "r", name = "avg_npc_1550_1#1$1",focus="r")]
[charslot(slot = "left", name = "avg_npc_1547_1#1$1",focus="r")]
[name="卡车司机"]......
[charslot(slot = "left", name = "avg_npc_1547_1#7$1",focus="l")]
[name="索默尔"]......
[dialog]
[charslot]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1555_1#1$1")]
[name="家族成员"]索默尔，鲁杰罗！
[charslot]
[charslot(slot = "r", name = "avg_npc_1550_1#1$1",focus="l")]
[charslot(slot = "left", name = "avg_npc_1547_1#8$1",focus="l")]
[name="索默尔"]我、我们什么都不知道！你也看到了，我们俩离你好几步远，我们站在原地动都没动......
[charslot(slot = "left", name = "avg_npc_1547_1#4$1",focus="l")]
[name="索默尔"]你也知道的，我们不会法术......
[charslot(slot = "r", name = "avg_npc_1550_1#1$1",focus="r")]
[name="卡车司机"]听说，这个地块之所以被划为最外围地块，在市政厅拨给我们建卡车营地之前都没有规划，就是因为这里以前是......
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1555_1#1$1")]
[name="家族成员"]少、少扯那些没用的，这次就先饶过你们。
[dialog]
[stopmusic(fadetime=2)]
[PlaySound(key="$rungeneral",volume=0.7)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[StopSound(channel="bgs", fadetime=2)]
[charslot(slot="l",name="avg_npc_1547_1#7$1")]
[delay(time=1)]
[charslot(slot="r",name="avg_1502_crosly_1#1$1")]
[curtain(direction = 0,fillfrom = 0.1,fillto = 0.1, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.1,fillto = 0.1, fadetime=0.1)]
[Background(image="56_g2_newvolsiniistreet_n",screenadapt="coverall")]
[playsound(key="$d_avg_truckengine", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.2, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[playMusic(intro="$newhope01_intro",key="$newhope01_loop",

... (全文25427字符)
```

### level_act38side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="56_g9_truckcamp",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月6日    3:20 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1550_1#1$1",duration=0.5)]
[delay(time=1)]
[name="卡车司机"]实在不好意思，助理先生，让您白跑一趟了。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_701_1#1$1",duration=0.5)]
[delay(time=1)]
[name="法官助理"]她没有告诉你们去哪里了？
[charslot(slot="m",name="avg_npc_1550_1#1$1")]
[name="卡车司机"]没有，但、但是请您转告拉维妮娅法官，伊雷妮有在认真调查她拜托的事情。
[name="卡车司机"]伊雷妮刚回到营地，就让我们对互助会名下的卡车进行自查了，她这会儿出去应该也是为了找车祸的线索——
[charslot(slot="m",name="avg_npc_701_1#1$1")]
[name="法官助理"]别紧张。我不是为这个事来的。
[charslot(slot="m",name="avg_npc_1550_1#1$1")]
[name="卡车司机"]啊？那——欸，柳德米拉，你知道伊雷妮去哪里了吗？
[name="卡车司机"]回营地怎么还偷偷摸摸的，差点都没注意到你......
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot="m",name="avg_1502_crosly_1#1$1",duration=1)]
[delay(time=2)]
[name="柳德米拉"]......
[charslot(slot="m",name="avg_npc_1550_1#1$1")]
[name="卡车司机"]你衣服怎么还破了？和别人打架了？
[charslot(slot="m",name="avg_1502_crosly_1#3$1")]
[name="柳德米拉"]摔了一跤。
[charslot(slot="m",name="avg_npc_701_1#1$1")]
[name="法官助理"]你就是柳德米拉？
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="柳德米拉"]......
[charslot(slot="m",name="avg_npc_701_1#1$1")]
[name="法官助理"]我有东西要给你。
[name="法官助理"]本来是应该由伊雷妮统一处理的，她不在，直接交到你手里也正合适。
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="柳德米拉"]这是？
[charslot(slot="m",name="avg_npc_701_1#1$1")]
[name="法官助理"]市民告知函和身份文件。
[name="法官助理"]你通过了市政厅与法院的背景审查，你的市民积分也够了......
[name="法官助理"]从今天起，你就是新沃尔西尼的合法市民、卡车工会的正式在籍司机了，享有《新都市管理法案》所规定的一切权益。
[charslot(slot="m",name="avg_npc_1550_1#1$1")]
[name="卡车司机"]哈哈，终于终于！
[name="卡车司机"]柳德米拉，你昨天那一顿盐汽水请早了！
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="柳德米拉"]......
[charslot(slot="m",name="avg_npc_701_1#1$1")]
[name="法官助理"]很意外吗？我们知道你的——呃，特殊之处。
[name="法官助理"]你还是需要定期接受矿石病检查，如果感染情况恶化的话，我们会重新评估对你的处理方案。
[name="法官助理"]卡车工会在这座城市的地位很特殊，以你的情况，本来确实很难通过背景审查......
[name="法官助理"]伊雷妮这段时间为这件事没少往市政厅和法院跑，最后她亲自为你做了风险担保，好些个司机都跟着在申请材料上签了字。
[charslot(slot="m",name="avg_1502_crosly_1#4$1")]
[name="柳德米拉"]......
[charslot(slot="m",name="avg_npc_1550_1#1$1")]
[name="卡车司机"]哎呀，柳德米拉，别用这样的眼神看着我嘛。总不能让你平时白请我们吃东西喝东西吧。
[charslot(slot="m",name="avg_npc_701_1#1$1")]
[name="法官助理"]柳德米拉？
[charslot(slot="m",name="avg_npc_1550_1#1$1")]
[name="卡车司机"]您别怪她，她一向话不多......我当时拿到告知函和身份文件的时候可比她失态多了。
[charslot(slot="m",name="avg_npc_701_1#1$1")]
[name="法官助理"]我能理解，根据资料显示，当初收养你的舅舅被卷入帮派斗争，全家都被灭门......其实大家都差不多......
[name="法官助理"]新沃尔西尼建成之后，许许多多曾受到家族压迫的叙拉古人都赶来了这里，取得新的身份，摆脱家族的影响......
[name="法官助理"]甚至有不少家族成员，也通过这种形式脱离了家族。
[name="法官助理"]在新沃尔西尼，我们每个人都拥有摆脱过去、拥抱新生活的权利。
[name="法官助理"]恭喜你，柳德米拉。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot = "m",posfrom = "0,0", posto = "200,0",duration = 1)]
[charslot(duration=1)]
[delay(time=2)]
柳德米拉看着手里的市民告知函和身份文件，沉默着。
[MusicVolume(volume=0.4, fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain(direction = 0,fillfrom = 0.1,fillto = 0.1, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.1,fillto = 0.1, fadetime=0.1)]
[charslot(slot = "left", name = "avg_npc_1547_1#2$1")]
[charslot(slot="r",name="avg_1502_crosly_1#1$1")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="56_g2_newvolsiniistreet_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "left", name = "avg_npc_1547_1#2$1",focus="l")]
[name="索默尔"]“不期而会”，我没什么文化，但我知道这是一个好词......你不觉得它就是在讲咱们这些人吗？
[dialog]
[charslot(slot = "m", focus = "all")]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_npc_1547_1#3$1",focus="l")]
[name="索默尔"]就当是倒霉蛋们不期而会了吧，哈哈。
[charslot(slot = "left", name = "avg_npc_1547_1#2$1",focus="l")]
[name="索默尔"]伊雷妮那丫头总说，再倒霉的人也会被生活眷顾的，只是会迟一些。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain]
[charslot(slot="m",name="avg_1502_crosly_1#3$1")]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=false)]
[Background(image="56_g9_truckcamp",screenadapt="coverall")]
[MusicVolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="柳德米拉"]这就是对倒霉蛋的眷顾吗......
[dialog]
[charslot(slot="r",name="avg_npc_1550_1#1$1",duration=1)]
[charslot(slot = "m",posfrom = "0,0", posto = "-200,0",duration = 1)]
[delay(time=1.5)]
[charslot(slot="r",focus="r")]
[name="卡车司机"]柳德米拉，你到底怎么了？
[charslot(slot="m",name="avg_1502_crosly_1#1$1",focus="m")]
[name="柳德米拉"]索默尔有没有回来？
[charslot(slot="r",focus="r")]
[name="卡车司机"]没有，他不是从昨晚开始到今天都休息嘛，可能去给小古莉挑狂欢节的礼物了吧。
[stopmusic(fadetime=2)]
[charslot(slot="m",name="avg_1502_crosly_1#1$1",focus="m")]
[name="柳德米拉"]别替他打掩护了，鲁杰罗。
[name="柳德米拉"]我知道你们的事情......我昨晚就在索默尔的车上。
[charslot(slot="r",focus="r")]
[name="卡车司机"]......
[playMusic(intro="$mist_intro",key="$mist_loop", volume=0.6)]
[name="卡车司机"]昨晚的那场车祸？
[charslot(slot="m",name="avg_1502_crosly_1#1$1",focus="m")]
[name="柳德米拉"]嗯，是我们的车。
[charslot(slot="r",focus="r")]
[name="卡车司机"]天哪——
[charslot(slot="m",name="avg_1502_crosly_1#7$1",focus="m")]
[name="柳德米拉"]......看你的反应，索默尔没回来。快想想他可能去哪儿了。
[charslot(slot="r",focus="r")]
[name="卡车司机"]他们昨晚应该原定在第三码头附近的载具检修站交货，我们有时候也会选威尼斯载具公司名下的几个废弃仓库......
[charslot(slot="m",name="avg_1502_crosly_1#5$1",focus="m")]
[name="柳德米拉"]都找遍了。
[name="柳德米拉"]我回了撞车的地方，现场已经被封锁，索默尔和车都不知所终，我也去了你刚刚说的那些地方......都没有。
[name="柳德米拉"]......
[charslot(slot="m",name="avg_1502_crosly_1#7$1",focus="m")]
[name="柳德米拉"]我怎么能就那么走掉呢，该死的，如果我没有被那个狼崽子吸引，说不定......
[charslot(slot="r",focus="r")]
[name="卡车司机"]柳德米拉......
[charslot(slot="m",name="avg_1502_crosly_1#7$1",focus="m")]
[name="柳德米拉"]我再去找！
[dialog]
[playsound(key="$rungeneral",volume=0.7)]
[charslot(slot =

... (全文14204字符)
```

### level_act38side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_wilderness_m",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[CameraShake(duration=1, xstrength=7, ystrength=5, vibrato=10, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_airwaramb", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=1, channel="bgs",fadetime=1)]
[Delay(time=1)]
[CameraShake(duration=1.5, xstrength=7, ystrength=5, vibrato=20, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[StopSound(channel="bgs", fadetime=1.5)]
[Delay(time=1)]
[Delay(time=2)]
[PlaySound(key="$d_avg_snowbootwalk")]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_683_1#1$1",duration=1.5)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_683_1#9$1")]
[name="拉普兰德"]啧啧......
[name="拉普兰德"]我们来迟了，这两帮人已经打完了，没一个活口。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_688_1#1$1",duration=1.5)]
[delay(time=2)]
[name="扎罗"]拉普兰德，你停下与我的决斗，只是为了来看这个无聊的火并现场？
[charslot]
一人一狼站在清晨的荒野上，不远处停着一辆黄色的出租车。
出租车的车头与一块巨石亲密接触，引擎盖已经深深地凹陷下去。车身后扭曲的车辙与翻飞的土石诉说着它刚刚是怎样一路狂飙而来......
车的周围横七竖八地躺着好几具尸体。风把血腥味送远，野兽的低吟声若隐若现。
[charslot(slot="m",name="avg_npc_683_1#9$1")]
[name="拉普兰德"]扎罗，有两件事你得搞清楚。
[name="拉普兰德"]第一，我不是给你解闷的玩物；第二，作为给我解闷的玩物，几个月下来，我发现不死不灭的狼之主也没趣得很......
[charslot(slot="m",name="avg_npc_683_1#3$1")]
[name="拉普兰德"]相比之下，一场莫名其妙发生在这荒野上的家族火并，不是更有看头？
[charslot(slot="m",name="avg_npc_688_1#1$1")]
[name="扎罗"]......
[dialog]
[charslot(slot="m",name="avg_npc_683_1#9$1")]
[delay(time=0.5)]
[charslot(slot = "m",posfrom = "0,0", posto = "150,0",duration = 1)]
[delay(time=1.5)]
[PlaySound(key="$sportscarstart")]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_683_1#3$1")]
[name="拉普兰德"]哈哈，车撞成这样，居然还能发动？
[charslot]
[charslot(slot="m",name="avg_npc_688_1#1$1")]
[name="扎罗"]它的目的地本来是哪里？
[charslot(slot="m",name="avg_npc_683_1#9$1")]
[name="拉普兰德"]让我看看......地图上被圈出来的地点是——“新沃尔西尼”，储物盒里还有入关文件......还挺齐全！
[charslot(slot="m",name="avg_npc_688_1#1$1")]
[name="扎罗"]熟悉的名字。
[charslot(slot="m",name="avg_npc_683_1#9$1")]
[name="拉普兰德"]喂，扎罗，帮忙把这些尸体拖到一边，腾出倒车的位置。
[charslot(slot="m",name="avg_npc_688_1#1$1")]
[name="扎罗"]你要......
[charslot(slot="m",name="avg_npc_683_1#3$1")]
[name="拉普兰德"]这可是叙拉古给你我的邀请函。
[name="拉普兰德"]难道你要拒绝邀请？狼之主这么没礼貌吗？
[charslot(slot="m",name="avg_npc_688_1#1$1")]
[name="扎罗"]我说过，在我们的斗争结束之前，我会与你同行。
[charslot(slot="m",name="avg_npc_683_1#9$1")]
[name="拉普兰德"]那就过来帮忙！
[Dialog]
[MusicVolume(volume=0.4, fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[bgeffect(name="$eb_tvnoise",layer=1)]
[delay(time=1)]
[Image(image="56_i25",screenadapt="coverall")]
[PlaySound(key="$d_avg_filmprojection")]
[playsound(key="$d_avg_filmprojection_loop", loop=true, channel="bgs",delay=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Sticker(id="st1", text="出租车司机", delay=0.001, width=800, x=250, y=520, duration=2, alignment="center", size=42)]
[delay(time=1)]
[Sticker(id="st1", duration=2, block = false)]
[StopSound(channel="bgs", fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image]
[bgeffect]
[delay(time=1)]
[Background(image="56_g4_newvolsiniialley_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年10月25日    9:00 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[MusicVolume(volume=0.6, fadetime=2)]
[charslot(slot = "right", name = "avg_npc_696_1#1$1",duration = 1)]
[charslot(slot = "left", name = "avg_npc_541_1#9$1",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_npc_541_1#9$1",focus="l")]
[name="卡彭"]你好。
[charslot(slot = "right",focus="r")]
[name="紧张的路人"]呃，您、您不用向我鞠躬的，卡彭先生。
[charslot(slot = "left", name = "avg_npc_541_1#9$1",focus="l")]
[name="卡彭"]别紧张，我只是不想自己这凶神恶煞的模样把你吓走，毕竟你好不容易才答应这次的见面。
[charslot(slot = "right",focus="r")]
[name="紧张的路人"]您的提议我想了很久。如果被市政厅的人发现我私下转让市民积分，会不会......
[charslot(slot = "left", name = "avg_npc_541_1#9$1",focus="l")]
[name="卡彭"]你只不过需要在那一大堆资质文件里挑几份，然后写份说明，更正一下所属人，很简单。
[name="卡彭"]这样我能得到五十个积分，你能得到......很大一笔钱。
[name="卡彭"]我们又没违规犯法，如果市政厅的人真有异议，那只不过说明《新都市管理法案》本身的规定还不够完善，这个你应该比我懂。
[charslot(slot = "right",focus="r")]
[name="紧张的路人"]话是这么说......
[charslot(slot = "left", name = "avg_npc_541_1#9$1",focus="l")]
[name="卡彭"]身份登记本身就很不公平，不是吗？
[charslot(slot = "left", name = "avg_npc_541_1#4$1",focus="l")]
[name="卡彭"]我明明已经洗心革面，因为有前科，这半年交了那么多认证金，做了那么多社区服务，一百二十个市民积分连一半都没攒到......
[charslot(slot = "left", name = "avg_npc_541_1#9$1",focus="l")]
[name="卡彭"]但像你，“履历清白”“从事法律等特定技术行业”......你才刚来新沃尔西尼，换算的市民积分都够成为三次新沃尔西尼市民了！
[name="卡彭"]不转让给我，也是白白浪费。
[charslot(slot = "right",focus="r")]
[name="紧张的路人"]......那、那好吧。
[name="紧张的路人"]我申请的正式认证时间在下周，在那之前我把你要的资质文件更正过来——
[charslot(slot = "left", name = "avg_npc_541_1#9$1",focus="l")]
[name="卡彭"]别那么急，朋友。
[charslot(slot = "right",focus="r")]
[name="紧张的路人"]啊，急的不是你吗？
[charslot(slot = "left", name = "avg_npc_541_1#9$1",focus="l")]
[name="卡彭"]不，我的意思是，你有没有考虑过，别那么着急成为新沃尔西尼市民？
[charslot(slot = "right",focus="r")]
[name="紧张的路人"]什、什么意思？
[charslot(slot = "left", name = "avg_npc_541_1#9$1",focus="l")]
[name="卡彭"]在新沃尔西尼，像我这样缺积分的人很多，但像你这样能攒积分的人少之又少，你迟一点正式认证，就可以一直靠转让......
[charslot(slot = "right",focus="r")]
[name="紧张的路人"]......
[charslot(slot = "left", name = "avg_npc_541_1#9$1",focus="l")]
[name="卡彭"]我很乐意当个中间人。
[charslot(slot = "right",focus="r")]
[name="紧张的路人"]新沃尔西尼推行《新都市管理法案》，就是为了防止你们这些人——抱、抱歉......
[name="紧张的路人"]总之，如果这样做，不就和这座城市的建立初衷背道而驰了吗？
[charslot(slot = "left", name = "avg_npc_541_1#9$1",focus="l")]
[name="卡彭"]唉，朋友，放轻松放轻松，我只是随口说说，你别介意。
[name="卡彭"]想一想，你来这座城市是为了什么......更稳定的收入？更好的新生活？
[name="卡彭"]这真的是你成为新沃尔西尼合法市民，找一个律所打杂能带来的吗？
[charslot(slot = "right",focus="r")]
[name="紧张的路人"]......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain(direction = 0,fillfrom = 0.1,fillto = 0.1, fadetime=0.1)

... (全文26171字符)
```

### level_act38side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_vipward",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月7日    12:00 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[PlaySound(key="$transmission")]
[delay(time=1)]
[name="收音机"]亲爱的市民们，中午好。
[name="收音机"]筹备数月之久的狂欢节将在十一月九日晚如期举行，届时数十万市民将走上街头，庆祝新沃尔西尼落成一周年。
[name="收音机"]根据狂欢节筹委会透露，所有的野兽花车已在新沃尔西尼港完成组装，今日将转移向拓展地块，为巡游做准备。
[name="收音机"]街头戏剧竞演也已经落下帷幕，俘获最多观众的团队将获得在狂欢节当夜代表全体市民点亮花车的资格......
[name="收音机"]其他入围剧目届时也将配合花车，在市民们巡游的道路两侧进行演出。
[name="收音机"]筹委会呼吁大家，保持花车在正式亮相前的神秘感！请务必按捺好奇心，不要前往窥探、偷拍或传播花车造型！
[dialog]
[charslot(slot="m",name="avg_1028_texas2_1#1$1",duration=1.5)]
[delay(time=2)]
[name="德克萨斯"]......
[charslot]
[name="收音机"]另外，十一月五日深夜，港口区第五大街发生了一起交通事故，现场有一人受伤，肇事车辆逃逸。
[name="收音机"]警方很快控制了现场，恢复了第五大街的秩序，该事故并未造成严重影响，请市民们不必惊慌。
[name="收音机"]目前警方已成立专案小组，在全城范围内排查肇事车辆，不日便将侦破此案。各位市民如发现相关线索，也请尽快联系警方......
[dialog]
[PlaySound(key="$dooropenquite")]
[delay(time=0.5)]
[charslot(slot="m",name="avg_4065_judge_1#1$1",duration=1)]
[delay(time=1.5)]
[name="拉维妮娅"]德克萨斯。
[charslot(slot="m",name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]你回来了。
[charslot(slot="m",name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]我过来看看，晚一些再去法院。
[name="拉维妮娅"]莱昂怎么样？
[charslot(slot="m",name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]医生过来了三趟......但都是常规检查，也没说别的——起码没有恶化？
[charslot(slot="m",name="avg_4065_judge_1#6$1")]
[name="拉维妮娅"]......
[charslot(slot="m",name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]看你的表情，昨天你临时要处理的那个案子并不顺利？
[charslot(slot="m",name="avg_4065_judge_1#2$1")]
[name="拉维妮娅"]案子结了......以一种我不愿意看到却又无能为力的方式。
[charslot(slot="m",name="avg_4065_judge_1#5$1")]
[name="拉维妮娅"]德克萨斯，我不记得你有收听午间新闻的习惯。
[charslot(slot="m",name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]情况不像新闻通报里说的那么乐观，对吧？
[charslot(slot="m",name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]有一些线索，也锁定了一些嫌疑人，但没什么实际的进展。
[charslot(slot="m",name="avg_1028_texas2_1#5$1")]
[name="德克萨斯"]有查过案发当晚报警的人吗？
[charslot(slot="m",name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]留下的都是假信息，不好查。
[charslot(slot="m",name="avg_1028_texas2_1#3$1")]
[name="德克萨斯"]或许我能帮上忙？城里有不少我们再熟悉不过的人，家族那些......
[charslot(slot="m",name="avg_4065_judge_1#6$1")]
[name="拉维妮娅"]谢谢你，德克萨斯......我知道你始终在关注这件事情。
[name="拉维妮娅"]在沃尔西尼，你的出现足以牵动城市里所有势力的神经，激怒一些人，警醒一些人，让事情出现转机。
[name="拉维妮娅"]但现在不是一年前，新沃尔西尼也不是沃尔西尼。在一座没有家族的城市里，“最后的德克萨斯”能做到的事情很有限。
[charslot(slot="m",name="avg_1028_texas2_1#8$1")]
[name="德克萨斯"]或者说，“最后的德克萨斯”在这里不应该还能做到那么多事情。
[charslot(slot="m",name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]......是。
[dialog]
[charslot]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[charslot(slot="m",name="avg_npc_702_1#1$1",duration=1)]
[delay(time=1.5)]
[name="护士"]德克萨斯小姐，前台有一通电话，是找您的。
[charslot(slot="m",name="avg_1028_texas2_1#3$1")]
[name="德克萨斯"]我？
[dialog]
[PlaySound(key="$doorclosequite")]
[charslot(duration=0.5)]
[delay(time=1.5)]
[name="德克萨斯"]谁？
[name="？？？"]哈哈，德克萨斯，需要用车吗？
[name="？？？"]我可不会等你太久。
[name="德克萨斯"]......
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background]
[charslot]
[delay(time=1)]
[playsound(key="$d_avg_rainheavy_loop", loop=true, channel="bgs",volume=0)]
[SoundVolume( channel="bgs",fadetime=2)]
[bgeffect(name="$eb_rain_fp",layer=1)]
[PlaySound(key="$dooropenquite")]
[gridbg(imagegroup="47_g14_skyovercast_L1/47_g14_skyovercast_R1/47_g14_skyovercast_L2/47_g14_skyovercast_R2", solidwidth="1280/1280/1280/1280", x=-640,y=320,solidheight="720/720/720/720",fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[bgeffect]
[gridbg]
[Background(image="33_g6_newtown_street",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playsound(key="$d_avg_umbrella_flap")]
[delay(time=1)]
[charslot(slot="m",name="avg_1028_texas2_1#1$1",duration=0.5)]
[delay(time=1)]
[name="德克萨斯"]明明这两天都艳阳高照的，怎么突然之间就暴雨倾盆了？
[playMusic(intro="$bar_intro",key="$bar_loop", volume=0.6)]
[charslot(slot = "m", focus = "n")]
[name="？？？"]真正惊讶的人，可不会随身带着一把伞哦。
[charslot(slot="m",name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]......
[charslot]
[dialog]
[playsound(key="$d_avg_carhorn")]
[delay(time=1)]
[name="？？？"]这边这边。
出租车的引擎盖上，黑色的巨大雨伞下，司机无聊地把玩着手中的钥匙。
[name="？？？"]哈哈，来得挺快嘛。
[name="？？？"]好久不见，德克萨斯。
[dialog]
[delay(time=1)]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_shallowswalk", volume=1, loop=true, channel="sh")]
[StopSound(channel="sh", fadetime=4)]
[interlude(maskid = "ui_cutin_mask_horizon" ,size = "1280,160",tsfrom="1,0.5", tsto ="1,1",tsduration = 1, style = 1,offset = "0,0", channel = 3)]
[interlude(channel = 3, type = 2, name = "56_g13_cutin_char_20", sfrom = "1.45,1.45", sto = "1.4,1.4", sduration = 0, pfrom = "20,-300", pto="70,-300", duration = 3, afrom = 0, ato = 1, aduration = 3)]
[delay(time=1)]
[interlude(channel = 3, type = 1, slot = "m", offset = "400,0", name = "cutin_char_20", sfrom = "1,1", sto = "0.8,0.8",pfrom = "-30,-110", pto = "0,-90", duration = 3, afrom = 0, ato = 1, aduration = 3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
司机缓缓抬起雨伞，露出弧度夸张的嘴角——那是一个很肆意的微笑。随后她若无其事地将雨伞扔开，向德克萨斯致意。
[dialog]
[interlude(channel = 3, clear = true,tsfrom="1,1",tsto="1,0",tsduration=0)]
[delay(time=1)]
[charslot(slot="m",name="avg_1028_texas2_1#1$1",duration=0.3,isblock=true)]
[delay]
[name="德克萨斯"]拉普兰德。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_dullthunderclap", volume=1)]
[bgeffect(name="$eb_thundershower",layer=1)]
[delay(time=2)]
[Background(image="bg_black",screenadapt="coverall",fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image(image="56_i08",screenadapt="coverall", xScale=1.5, yScale=1.5,x=300,y=-200)]
[Blocker(a

... (全文34514字符)
```

### level_act38side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_vipward",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$sjoyasorrow_intro",key="$sjoyasorrow_loop", volume=0.6)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月8日    2:17 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot="m",name="avg_4065_judge_1#1$1",duration=0.5, focus = "n")]
[delay(time=1)]
[PlaySound(key="$dooropenquite")]
[delay(time=1)]
[charslot(slot="m",name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]德克萨斯，你回来了。
[dialog]
[charslot]
[charslot(slot="l",name="avg_1028_texas2_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot = "r",name="avg_npc_1564_1#9$1",posfrom = "-200,0", posto = "0,0",duration = 0.8)]
[delay(time=1)]
[charslot(slot = "r",name="avg_npc_1564_1#9$1",focus="r")]
[multiline(name="拉普兰德")]还有我......
[charslot(slot = "r",name="avg_npc_1564_1#3$1",focus="r")]
[multiline(name="拉普兰德")]怎么，不欢迎？
[dialog]
[charslot]
[charslot(slot="m",name="avg_4065_judge_1#5$1")]
[name="拉维妮娅"]......拉普兰德？
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[charslot(slot = "r",name="avg_npc_1564_1#3$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "l",name="avg_4065_judge_1#7$1",posfrom = "-150,0", posto = "0,0",duration = 1)]
[delay(time=1.6)]
[charslot(slot = "r",name="avg_npc_1564_1#3$1",focus="r")]
[name="拉普兰德"]别这么如临大敌，要是惊扰到病人可怎么办呢？
[name="拉普兰德"]德克萨斯，快告诉法官小姐，我真的只是过来送文件的。
[dialog]
[charslot]
[charslot(slot="m",name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]（点头）
[dialog]
[charslot]
[charslot(slot = "l",name="avg_4065_judge_1#7$1",focus="r")]
[charslot(slot = "r",name="avg_npc_1564_1#9$1",focus="r")]
[name="拉普兰德"]接着，大法官小姐。
[name="拉普兰德"]刚刚在门口碰见个小法官来给你送卷宗。市长大人的病房不能有太多人打扰，我和德克萨斯就顺便给你带了进来。
[charslot(slot = "l",name="avg_4065_judge_1#5$1",focus="l")]
[name="拉维妮娅"]......
[dialog]
[playsound(key="$d_avg_paper1")]
[delay(time=1.5)]
[charslot(slot = "l",name="avg_4065_judge_1#4$1",focus="l")]
[name="拉维妮娅"]新沃尔西尼港失火，紧急庭审程序——被告伊雷妮？
[charslot(slot = "r",name="avg_npc_1564_1#9$1",focus="r")]
[name="拉普兰德"]......
[name="拉普兰德"]那个司机小姐是你的朋友吧？别紧张，往后翻，直接看审判结果，她当场就被无罪释放了。
[charslot(slot = "r",name="avg_npc_1564_1#3$1",focus="r")]
[name="拉普兰德"]我和德克萨斯碰巧去听了那场庭审，很精彩，威尼斯家族——
[name="拉普兰德"]哈哈，抱歉抱歉，是威尼斯载具公司和萨卢佐酒业的老板同时为她作证，还在庭审结束后争着抢着送她回家......
[charslot(slot = "r",name="avg_npc_1564_1#9$1",focus="r")]
[name="拉普兰德"]啧啧，司机小姐的人缘可真好！
[name="拉普兰德"]就是她走出法院的样子，让我想起了家族成员们进法院逛一圈出来的成人礼。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="56_g5_courtsquare_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月8日    11:35 A.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1542_1#2$1",duration=1)]
[delay(time=1.5)]
[name="伊雷妮"]......
[charslot]
签字确认，领走判决书，离开法院。流程并不麻烦，但伊雷妮还是觉得有些头晕。阳光很刺眼，晃得她低下了头——
偌大的法院广场，两辆车停在她的必经之路上，它们的引擎盖上各自缀着特制的车标——在叙拉古随处可见的图案。
就算她不认得萨卢佐的酒标和威尼斯的家徽，她也不会不认得车前那两个刚刚还在法庭上为自己辩护的人。
伊雷妮知道，他们在等她——萨卢佐家族与威尼斯家族在等她。
[dialog]
[charslot(slot="m",name="avg_npc_686_1#9$1",duration=0.5)]
[delay(time=1)]
[name="阿尔贝托"]恭喜你，伊雷妮小姐。
[charslot(slot = "m", name = "avg_npc_1542_1#2$1")]
[name="伊雷妮"]......没什么好恭喜的。
[name="伊雷妮"]阿尔贝托先生，虽然昨天那场火是个意外，但我担心的事情，确实也因此被稀里糊涂地解决了。
[name="伊雷妮"]我以为，已经辛苦您白跑了一趟，就更不应该继续给您添麻烦了。
[name="伊雷妮"]可您今天过来，就等于告诉所有人——
[charslot(slot="m",name="avg_npc_686_1#9$1")]
[name="阿尔贝托"]萨卢佐当然要帮卡车工会。
[name="阿尔贝托"]从目前的状况来看，有些交易确实已经不再作数，但你我都清楚，在叙拉古，搭建一段友谊有多么难能可贵。
[name="阿尔贝托"]约定依然存在，伊雷妮小姐。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1544_1#1$1",duration=0.5)]
[delay(time=0.8)]
[name="安东尼奥"]咳——阿尔贝托叔叔，我应该没有打扰你吧？
[name="安东尼奥"]伊雷妮小姐是为我们运的轮胎，现在货在她手里出了事，我还得找她谈谈该怎么赔偿。
[charslot(slot = "m", name = "avg_npc_1542_1#2$1")]
[name="伊雷妮"]安东尼奥先生......
[charslot(slot="m",name="avg_npc_1544_1#1$1")]
[name="安东尼奥"]别紧张，虽然我们今天才正式认识，但已经相当有默契了。
[name="安东尼奥"]你在法庭上什么都没有说，这很好。
[charslot(slot = "m", name = "avg_npc_1542_1#2$1")]
[name="伊雷妮"]......
[charslot(slot="m",name="avg_npc_1544_1#1$1")]
[name="安东尼奥"]关于卡车工会，以及许多事情，我想我们已经有很多东西可以交流。
[name="安东尼奥"]上车吧，我送你回营地。
[charslot(slot="m",name="avg_npc_686_1#7$1")]
[name="阿尔贝托"]小威尼斯——
[dialog]
[charslot]
[stopmusic(fadetime=2)]
[playsound(key="$d_avg_carhorn")]
[playsound(key="$d_avg_truckengine", loop=true, channel="1",volume=0)]
[SoundVolume(volume=0.6, channel="1",fadetime=1)]
[delay(time=1.5)]
[StopSound(channel="1", fadetime=2)]
嘹亮的鸣笛声打断了三人的对话，一辆卡车从两辆私家车之间穿过，稳稳地停在了伊雷妮面前。
[charslot(slot="m",name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]......
[charslot(slot="m",name="avg_npc_1544_1#4$1")]
[name="安东尼奥"]......
[charslot]
[playsound(key="$d_avg_cardoorc")]
车门打开，伊雷妮看到了下车的柳德米拉。
[charslot(slot = "m", name = "avg_npc_1542_1#5$1")]
[name="伊雷妮"]柳德米拉！
[playMusic(intro="$storyendjp_intro",key="$storyendjp_loop", volume=0.6)]
[dialog]
[charslot]
[charslot(slot="m",name="avg_1502_crosly_1#6$1",duration=1)]
[delay(time=1)]
[name="柳德米拉"]......
[charslot(slot = "m", name = "avg_npc_1542_1#7$1")]
[name="伊雷妮"]......你怎么了？
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="柳德米拉"]走吧，我来接你回家。营地里还有很多事情等着你拿主意呢。
[charslot(slot = "m", name = "avg_npc_1542_1#2$1")]
[name="伊雷妮"]好，我们走。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[playsound(key="$d_avg_cardoorc")]
[curtain(direction = 0,fillfrom = 0.1,fillto = 0.1, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.1,fillto = 0.1, fadetime=0.1)]
[charslot(slot = "left", name = "avg_1502_crosly_1#1$1")]
[charslot(slot = "right", name = "avg_npc_1542_1#2$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot = "right", name = "avg_npc_1542_1#2$1",focus="r")]
[name="

... (全文15236字符)
```

### level_act38side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g7_reception",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月8日    6:15 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[PlaySound(key="$doorknockquite")]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1555_1#1$1",duration=0.5)]
[delay(time=1)]
[name="惶恐的家族成员"]老爷，您找我？
[charslot(slot="m",name="avg_npc_1545_1#1$1")]
[name="老威尼斯"]安东有话问你。
[charslot(slot="m",name="avg_npc_1544_1#1$1")]
[name="安东尼奥"]卡尔，这边。
[charslot(slot="m",name="avg_npc_1555_1#1$1")]
[name="惶恐的家族成员"]安东尼奥......
[charslot(slot="m",name="avg_npc_1544_1#1$1")]
[name="安东尼奥"]最近新沃尔西尼还有车队发往西西里城吗？
[charslot(slot="m",name="avg_npc_1555_1#1$1")]
[name="惶恐的家族成员"]客运航线都在正常运转。不过这段时间都是赶来新沃尔西尼参加狂欢节的，倒没什么人往外面跑。
[charslot(slot="m",name="avg_npc_1544_1#1$1")]
[name="安东尼奥"]那就好。
[name="安东尼奥"]你现在去收拾行李，应该还来得及赶上末班车。
[charslot(slot="m",name="avg_npc_1555_1#1$1")]
[multiline(name="惶恐的家族成员")] 好的——
[CameraShake(duration=0.2, xstrength=15, ystrength=15, vibrato=20, randomness=90, fadeout=true, block=false)]
[multiline(name="惶恐的家族成员")] 啊、啊？安东尼奥，这是什么意思？
[charslot(slot="m",name="avg_npc_1544_1#1$1")]
[name="安东尼奥"]你不是还有个兄弟在西西里城吗？如果不能继续留在新沃尔西尼，也不能返回蒙特卢佩，你应该只能去投奔他吧。
[charslot(slot="m",name="avg_npc_1544_1#4$1")]
[name="安东尼奥"]因为你的疏忽，我们丢了整整一车“轮胎”。
[charslot(slot="m",name="avg_npc_1544_1#8$1")]
[name="安东尼奥"]我给过你机会，但哪怕只是去港口迎接家主，你竟然也没能办好。萨卢佐家的老混蛋甚至在你之前找到了家主。
[name="安东尼奥"]卡尔，你还能活着离开，已经是我能给你的最体面的结局。拿着这个——
[charslot]
[PlaySound(key="$d_avg_paper2")]
那是一张银行的本票，数目不小。
家族成员愣愣地接过来，他看见左上角写着自己的名字，安东尼奥已经在上面画了一个叉。
[charslot(slot="m",name="avg_npc_1544_1#4$1")]
[name="安东尼奥"]安置费。没了家族的庇佑，你要用钱的地方多得很。
[charslot(slot="m",name="avg_npc_1555_1#1$1")]
[name="惶恐的家族成员"]我在家族待了十几年，在你来之前，我就一直跟着老爷，你不能当着老爷的面，对我——
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="惶恐的家族成员"]老爷，老爷——
[charslot(slot="m",name="avg_npc_1544_1#1$1")]
[name="安东尼奥"]员工犯了错，自然要受到惩罚，您觉得呢？
[charslot(slot="m",name="avg_npc_1545_1#1$1")]
[name="老威尼斯"]当然，你是威尼斯载具公司的负责人。
[dialog]
[charslot(slot="m",name="avg_npc_1555_1#1$1")]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_1555_1#1$1",posfrom = "-200,0", posto = "-200,0",duration=0.5)]
[delay(time=0.7)]
[charslot(slot="l",posfrom = "-200,0", posto = "-80,0",duration=0.5)]
[delay(time=0.7)]
[PlaySound(key="$d_avg_clothmovement")]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=20, randomness=90, fadeout=true, block=true)]
[charslot(slot="l",posfrom = "-80,0", posto = "-280,0",duration=0.8,afrom=1,ato=0)]
[charslot(slot="m",posfrom = "0,0", posto = "-200,0",duration=0.8,afrom=1,ato=0)]
[delay(time=2)]
[charslot]
[charslot(slot = "left", name = "avg_npc_1545_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1544_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1545_1#1$1",focus="l")]
[name="老威尼斯"]......安东，这件事你并没有提前知会我。
[charslot(slot = "right", name = "avg_npc_1544_1#1$1",focus="r")]
[name="安东尼奥"]还请您不要怪罪。
[name="安东尼奥"]警察刚刚来过了。他们要检查威尼斯旗下的载具工厂和检修站，说是狂欢节前的例行检查，公函却是临时开具的。
[name="安东尼奥"]我刚刚还得到消息，阿尔贝托突然因为企业资质问题而被暂时拘留。
[name="安东尼奥"]毫无疑问，上午的庭审刺激了我们的拉维妮娅大法官，她希望以这种手段控制她所未知的局势。
[name="安东尼奥"]事情已经超出了我的控制，我不得不处置卡尔，否则很难服众。
[charslot(slot = "left", name = "avg_npc_1545_1#3$1",focus="l")]
[name="老威尼斯"]......
[charslot(slot = "right", name = "avg_npc_1544_1#1$1",focus="r")]
[name="安东尼奥"]这一年，威尼斯载具公司谨遵《新都市管理法案》，唯一留下的把柄，也在昨天港口的那场火里被烧掉了。
[name="安东尼奥"]唯一一个可能影响到我们生意的人也处理了。
[name="安东尼奥"]但等到狂欢节结束，拉维妮娅腾出手来，恐怕会尽全力针对我们。
[charslot(slot = "left", name = "avg_npc_1545_1#1$1",focus="l")]
[name="老威尼斯"]你打算怎么处理？
[charslot(slot = "right", name = "avg_npc_1544_1#1$1",focus="r")]
[name="安东尼奥"]我本来的想法，是慢慢地改造这座城市——让它既有其他城市所没有的行之有效的法律，也有叙拉古人已经习以为常的地下秩序。
[name="安东尼奥"]威尼斯载具公司的生意做得这么顺遂，诀窍只有两个：好好遵守《新都市管理法案》，不那么遵守《新都市管理法案》。
[name="安东尼奥"]其他家族显然也在这么做，不过适应新的游戏规则是很难的。
[name="安东尼奥"]威尼斯家族本可以完美地融入这两套秩序，我们已经做得很好了。
[name="安东尼奥"]所以时至今日，我们能做到抛弃其中的一部分，并转而加速另一部分。
[charslot(slot = "left", name = "avg_npc_1545_1#6$1",focus="l")]
[name="老威尼斯"]......
[name="老威尼斯"]你想要，彻底控制这座城市？
[charslot(slot = "left", name = "avg_npc_1545_1#5$1",focus="l")]
[name="老威尼斯"]你乱了阵脚，安东。别忘记，新沃尔西尼有西西里夫人的背书，她支持那群年轻人的改革。
[name="老威尼斯"]你这样做，等于是在公开挑衅她的权威，与整个叙拉古作对。你在拿整个威尼斯家族打赌！
[charslot(slot = "right", name = "avg_npc_1544_1#1$1",focus="r")]
[name="安东尼奥"]听起来是这样。
[charslot(slot = "left", name = "avg_npc_1545_1#5$1",focus="l")]
[name="老威尼斯"]上一个这么做的，是贝纳尔多......他才死了一年！
[charslot(slot = "right", name = "avg_npc_1544_1#1$1",focus="r")]
[name="安东尼奥"]您害怕西西里夫人，害怕市政厅里那些高喊理想的年轻人？
[name="安东尼奥"]......爸爸，您是真的老了。
[charslot(slot = "left", name = "avg_npc_1545_1#5$1",focus="l")]
[name="老威尼斯"]威尼斯是灰厅中最特别的存在，一个几乎由“杂种”组成的家族，没有血缘关系的离群的鲁珀，英格丽那样的沃尔珀，你这样的佩洛......
[name="老威尼斯"]其他家族并没有多么瞧得上我们，但我们走到了今天。这里面凝聚了每一个威尼斯人的心血。
[name="老威尼斯"]我们的联系比血缘更紧密，我希望家里的每个人都能有体面的结局。
[name="老威尼斯"]而你想要将家族置于如此险境......安东，你似乎遗忘了我的教诲。
[charslot(slot = "m", focus = "all")]
[dialog]
[charslot(slot = "right", name = "avg_npc_1544_1#3$1",focus="r")]
[delay(time=1.5)]
[charslot(slot = "right", name = "avg_npc_1544_1#4$1",focus="r")]
[name="安东尼奥"]爸爸，我是不是从来没讲过，我这只佩洛，是怎么来到叙拉古的？
[charslot(slot = "left", name = "avg_npc_1545_1#1$1",focus="l")]
[name="老威尼斯"]......
[charslot(slot = "right", name = "avg_npc_1544_1#4$1",focus="r")]
[name="安东尼奥"]......我是个军人，隶属“真正玻利瓦尔人解放运动”。
[charslot(slot = "left", name = "avg_npc_1545_1#1$1",focus="l")]
[name="老威尼斯"]我对玻利瓦尔的局势，只有一些很粗浅的了解......
[charslot(slot = "right", name = "avg_npc_1544_1#4$1",focus="r")]
[name="安东尼奥"]其实在玻利瓦尔，给谁当兵都没有任何区别，你不用懂三方势力为什么打仗，反正我们这些人不过是靠卖命讨一条活路。
[name="安东尼奥"]我所在的游击队在扫荡辛嘉斯王朝的一个村镇时暴露了行踪，整支队伍都成了俘虏。
[name="安东尼奥"]我们这二十号人掏干净了身上的每一个口袋，凑了所有家当买通行刑官，求他把我们在名单上的身份从“死刑犯”改成了“劳役犯”。
[name="安东尼奥"]负责转运我们的上级官员，是个大腹便便的贵族，他那天喝醉了酒，弄错了审核程序，只开来了一辆卡车......只够坐十个人。
[charsl

... (全文13767字符)
```

### level_act38side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.6)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Sticker(id="st1", multi = true, text="<i>传说，在大地西边的荒野上游荡着一只神秘的粉色梦魔。</i>", x=250,y=250, alignment="center", duration=1, size=24, delay=0.04, width=800)]
[Sticker(id="st1", multi = true, text="<i>\n\n它以漆黑的焦炭当皮囊，以火烧的云朵为毛发，以扭曲的枯枝作双角。</i>", block = true)]
[Sticker(id="st1", multi = true, text="<i>\n\n路人会被它美好的假面所迷惑，被它甜美的气味熏染得困倦疲乏，不知不觉堕入一重重幻梦中，成为它的养料。</i>", block = true)]
[Sticker(id="st1", duration=1, block = false)]
[Delay(time=1)]
[Sticker(id="st2", multi = true, text="<i>梦魔诱骗的主要目标是鲁珀小孩，据说在数百年前，它曾在某个夜晚拐走过一座城市里的上万个孩童。</i>", x=250,y=250, alignment="center", duration=1, size=24, delay=0.04, width=800)]
[Sticker(id="st2", multi = true, text="<i>\n\n还好叙拉古人是聪明的，他们想到了办法对抗这位可怕的粉色梦魔——</i>", block = true)]
[Sticker(id="st2", multi = true, text="<i>\n\n梦魔天生怕狼。所以，只需要在遇见它的时候朝它大喊三声“狼来了！”，梦魔就会消失得无影无踪。</i>", block = true)]
[Sticker(id="st2", duration=1, block = false)]
[stopmusic(fadetime=1)]
[Delay(time=1)]
[name="？？？"]——！
[PlaySound(key="$d_avg_blcksheepborn", volume=1)]
[name="？？？"]我实在是听不下去了！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[charslot]
[Image(image="56_i10_1", screenadapt="coverall", xScale=1.1, yScale=1.1)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=30, block=false)]
[Delay(time=1)]
[PlayMusic(key="$m_avg_playful_loop", volume=0)]
[musicvolume(volume=0.6, fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="大祭司"]别激动，多利。这个乐手也没胡说，在叙拉古的传说里，羊确实就是这么个形象。
[name="大祭司"]你要实在气不过，就从羊花车蹦到他头上踩几脚，反正今天晚上发生什么都没人会觉得稀奇。
[name="多利"]我只是曾经喜欢被那些狼追着跑，在叙拉古的那阵子，和他们捉迷藏算是我为数不多的乐趣......
[name="多利"]结果叙拉古人却以为我“害怕”那些狼？真是人言可畏。
[name="大帝"]这个成语可不是这么用的。
[name="多利"]你在说风凉话吗？
[name="多利"]大帝，你在叙拉古人的认知里是什么样的？
[name="大帝"]大嘴巴，告诉他黑袍歌唱家的伟大事迹！
[name="大祭司"]呃......从前有个家族领袖非常讨厌音乐，他禁止了音乐在他的城市出现，直到许多年后一位黑袍企鹅歌手到来。
[name="大祭司"]歌手在广场上自顾自唱歌，市民们对音乐没有概念，他们只觉得吵闹，所以想要把歌手抓起来交给家族领袖处罚。
[name="大祭司"]可歌手非常灵活，再精壮的小伙子也抓不住他......
[name="大祭司"]歌声不停，越来越多的人加入抓捕的队伍，渐渐，歌手与市民的搏斗变成了一场所有人都卷入其中的舞蹈。
[name="大祭司"]歌手就这么唱了三天三夜，直到怒不可遏的家族领袖亲自来抓他。可家族领袖一出门就被狂欢的人潮淹没，再也没有人见过他——
[name="多利"]为什么听起来像是聪明又正义的大英雄，可大帝明明不如我有智慧。
[name="大帝"]这不是智慧，是态度。是潘格温伯爵对音乐的态度，自由与抗争！多利，我送你的签名专辑你是不是都没有听？
[name="多利"]......
[name="大祭司"]走吧，别挡住后面人的路。
[dialog]
[PlaySound(key="$d_avg_cheer_street", volume=1)]
[PlaySound(key="$d_avg_carnival_crown", volume=0, loop=true, channel="carn")]
[SoundVolume(volume=0.5, channel="carn",fadetime=2)]
[Image(image="56_i10_2", screenadapt="coverall", xScale=1.75, yScale=1.75, y=200, fadetime=2)]
[ImageTween(xScaleFrom=1.75, yScaleFrom=1.75, xScaleTo=1.7, yScaleTo=1.7, duration=10, block=false)]
[delay(time=2)]
[name="乐手"]（兴奋地吹奏）
[name="杂耍艺人"]（兴奋地表演火舞）
[name="乐手"]（更卖力地吹奏）
[name="杂耍艺人"]（不服输地炫技）
[dialog]
[Image(image="56_i10_2", screenadapt="coverall", xScale=1.75, yScale=1.75, y=-270, fadetime=3)]
[ImageTween(xFrom=470, xTo=400, duration=20, block=false)]
[name="路人A"]阿基莱，我的阿基莱呢？
[name="路人B"]唉，女士，您才发现自己和陌生人并肩走了半个小时吗？
[name="路人A"]啊，我认得你的声音，你是之前特尔尼城的那个法官！对不起，是莱卡家族的人逼迫我做伪证——
[name="路人B"]（敲了敲面具）那都是过去的事了。女士，您违反了狂欢节的规则。
[name="路人B"]看看身边，大家都戴上了面具，今夜，无所谓身份、贫富、种族，忘却过往的仇恨......请我喝杯啤酒吧，为新沃尔西尼举杯！
[dialog]
[SoundVolume(volume=1, channel="carn",fadetime=2)]
[Image(image="56_i10_2", screenadapt="coverall", xScale=1.15, yScale=1.15, fadetime=2)]
[ImageTween(xScaleFrom=1.15, yScaleFrom=1.15, xScaleTo=1, yScaleTo=1, duration=30, block=false)]
[delay(time=2)]
人群从三位兽主的身边经过，多利的分身往来穿梭，所有人都看得见它们，但无人大惊小怪。
身处狂欢的洪流之中，没有一朵浪花称得上异样。
十多辆巨型花车前后相连，狼、羊、企鹅、猫、狗......传说中散落大地各处的野兽们齐聚在同一个城市，引领着人群向前。
传统戏剧表演和即兴演出挤满了街道，乐手与杂耍艺人像是比赛般炫技，食品车车主不得不一次次提高音量来兜售啤酒、披萨和冰淇淋。
[name="多利"]这里比喷薄的火山还要热闹。
[name="大祭司"]总比之前的狂欢节要好，连肥仔都不喜欢那样的派对。
[name="大帝"]我不会把所有混黑帮的戴着面具杀来杀去搞得整个城市都血淋淋的行为称为“派对”，别侮辱这个词。
[name="大帝"]一棵树上结不出两种果子，叙拉古人和那些狼真的太像了。
[name="大帝"]几千上万年前，我们嫌那些只知道厮杀的狼太蠢，每次开派对都不带他们，结果他们自己鼓捣出了所谓的狼主游戏。
[name="大帝"]不过好在叙拉古人总算有了点长进，知道生活中有比杀人和抢地盘更值得庆祝的事情。
[name="大帝"]至于那群一根筋的狼——
[name="大祭司"]肥仔，我们感受到的“不对劲”，他们肯定也感受到了......
[name="大祭司"]有些事还是得找他们商量，谁让我们是“同胞”呢。
[name="大祭司"]我已经见过他们里面没那么蠢的了，但在那无聊的游戏结束前，他们是听不进去任何话的。
[name="大帝"]按炎国话说，暂时先“入乡随俗”吧。
[name="大帝"]别辜负派对！叙拉古人最好安排了些更有趣的节目！
[dialog]
[stopmusic(fadetime=2)]
[SoundVolume(volume=0.2, channel="carn",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[charslot]
[Background(image="bg_vipward",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_snowstormflp", volume=0, loop=true, channel="s")]
[SoundVolume(volume=1, channel="s",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月9日    9:25 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[PlaySound(key="$dooropenquite", volume=1)]
[charslot(slot = "m", name = "avg_npc_690_1#9$1", duration=1.5, isblock=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_690_1#5$1")]
[delay(time=1)]
[charslot(slot = "m", focus="n")]
风吹在了德米特里的脸上。
他记得自己昨天离开时病房的窗户紧闭着，拉维妮娅也叮嘱过护士，深秋时节要注意室内的温度——他抬眼看去，病床上已经空了。
[charslot]
[StopSound(channel="carn", fadetime=2)]
[name="？？？"]好久不见，德米特。
[dialog]
[StopSound(channel="s", fadetime=2)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1541_1#8$1", duration=1.5, isblock=true)]
[delay(time=1)]
[charslot(slot = "m", focus="n")]
[name="私人医生"]抱歉，莱昂图索先生，这个人非要闯进来。市政厅和法院的电话都暂时打不通，我联系不上拉维妮娅法官......
[charslot(slot = "m", name = "avg_npc_1541_1#8$1")]
[name="莱昂图索"]没关系，你先去忙吧。
[dialog]
[charslot(slot = "m", focus="n")]
[PlaySound(key="$d_gen_walk_n",

... (全文28358字符)
```

### level_act38side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="56_g14_governmentoffice_n",screenadapt="coverall")]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1100年11月9日    11:10 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot = "l", name = "avg_4065_judge_1#1$1", duration=1)]
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", duration=1)]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_4065_judge_1#4$1", focus="l")]
[name="拉维妮娅"]......这是？
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", focus="r")]
[name="伊雷妮"]根据司机们的供述整理的名单，这大半年，名单上的人一直在通过各种手段威胁他们往城里运送违禁品。
[name="伊雷妮"]很显然，那天晚上的车祸、新沃尔西尼港的大火，还有此时此刻广场上的动乱，都是同一群人所为——家族。
[charslot(slot = "l", name = "avg_4065_judge_1#1$1", focus="l")]
[name="拉维妮娅"]......原来是这样。
[name="拉维妮娅"]伊雷妮，卡车工会遭遇的事情，你应该早点告诉我。昨天我去了一趟营地，但没有见到你——
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[name="伊雷妮"]说这些已经迟了，拉维妮娅法官。当务之急是，审判他们。
[charslot(slot = "l", name = "avg_4065_judge_1#5$1", focus="l")]
[name="拉维妮娅"]审判？
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[name="伊雷妮"]这帮人想占领法院，趁着狂欢节彻底解决他们的威胁......莱昂图索之后，就是你，拉维妮娅法官。
[name="伊雷妮"]此时此刻，他们已不再是新沃尔西尼市民，他们已犯下《新都市管理法案》所禁止的最为严重的罪行。
[name="伊雷妮"]眼前的一切就是现成的物证，司机们都是人证。
[charslot(slot = "r", name = "avg_npc_1542_1#4$1", focus="r")]
[name="伊雷妮"]这位德克萨斯小姐，她既不属于政府也不属于家族，和卡车互助会更没有关系，完全可以充当临时陪审员。
[charslot]
[charslot(slot = "m", name = "avg_1028_texas2_1#5$1")]
[name="德克萨斯"]呃......
[charslot]
[charslot(slot = "l", name = "avg_4065_judge_1#5$1", focus="n")]
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[name="伊雷妮"]而你是新沃尔西尼的大法官，这已经满足紧急审判程序的基本条件了......“紧急审判程序”，是叫这个名字吧？
[name="伊雷妮"]在极端情势下，只要满足最基本的条件，法院就可以对严重威胁到新沃尔西尼公共安全的犯罪者进行缺席判决。
[charslot(slot = "l", name = "avg_4065_judge_1#5$1", focus="l")]
[name="拉维妮娅"]......
[name="拉维妮娅"]当务之急应该是控制局势，确保民众的安全和狂欢节的顺利进行。
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[name="伊雷妮"]这正是我的目的，拉维妮娅法官。你下达判决，卡车工会可以帮助你执行判决。
[charslot(slot = "l", name = "avg_4065_judge_1#5$1", focus="l")]
[name="拉维妮娅"]是吗？
[dialog]
[charslot(slot = "l", name = "avg_4065_judge_1#1$1", focus="l")]
[playsound(key="$d_avg_paper1",volume=1)]
[delay(time=0.5)]
[playsound(key="$d_avg_paper2",volume=1)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_4065_judge_1#8$1", focus="l")]
[name="拉维妮娅"]你列出的这份名单——
[charslot(slot = "l", name = "avg_4065_judge_1#5$1", focus="l")]
[multiline(name="拉维妮娅",end=true)]有些太过详细了，伊雷妮。
[name="拉维妮娅"]威尼斯、萨卢佐、美第奇、雷欧帝、吉诺维斯......好几个家族......这些人真的都在外面的广场上吗？
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[name="伊雷妮"]拉维妮娅法官，上面没有一个人是无辜的。
[charslot(slot = "l", name = "avg_4065_judge_1#5$1", focus="l")]
[name="拉维妮娅"]......
[name="拉维妮娅"]一旦启用紧急审判程序，签署了这份判决书，就意味着名单上的所有人都成为了《新都市管理法案》认定的极端犯罪者......
[name="拉维妮娅"]任何人都能根据紧急避险原则控制他们，甚至处决他们，而不被追究责任。
[charslot(slot = "l", name = "avg_4065_judge_1#2$1", focus="l")]
[name="拉维妮娅"]眼前的局势，还不足以支持我作出这样的判断。
[charslot(slot = "r", name = "avg_npc_1542_1#9$1", focus="r")]
[name="伊雷妮"]可他们本就是要来对付你的，拉维妮娅。
[charslot(slot = "l", name = "avg_4065_judge_1#1$1", focus="l")]
[name="拉维妮娅"]没错。可伊雷妮，你今天来的真实目的是什么呢？
[charslot(slot = "l", name = "avg_4065_judge_1#5$1", focus="l")]
[name="拉维妮娅"]你今天开来这么多辆卡车围住法院，究竟是为了保护一个朋友，还是......为了方便拿到一份可以解决自己身上所有麻烦的凭据？
[dialog]
[charslot(slot = "r", name = "avg_npc_1542_1#3$1", focus="r")]
[delay(time=1.5)]
[charslot(slot = "r", name = "avg_npc_1542_1#11$1", focus="r")]
[name="伊雷妮"]昨天，你去营地找我的时候，我正在尝试为索默尔收尸......
[charslot(slot = "l", name = "avg_4065_judge_1#5$1", focus="l")]
[name="拉维妮娅"]——
[charslot(slot = "r", name = "avg_npc_1542_1#7$1", focus="r")]
[name="伊雷妮"]谢谢你还记得他......是的，他已经死了。但我动员了许多人，都没能找到他的尸体。
[name="伊雷妮"]我不知道凶手具体是谁，可我知道凶手就在外面。
[charslot(slot = "r", name = "avg_npc_1542_1#3$1", focus="r")]
[name="伊雷妮"]我甚至知道凶手并非具体的某个人，而是一道阴影，它始终悬在我们头顶，哪怕我们逃到了这座新城市，也还是没能逃开。
[charslot(slot = "r", name = "avg_npc_1542_1#8$1", focus="r")]
[name="伊雷妮"]我想让害死索默尔的凶手得到应有的惩罚，我想让剩下的那些人都不再受到伤害......
[name="伊雷妮"]拉维妮娅法官，这就是我的目的。
[dialog]
[charslot(slot = "r", focus="n")]
[PlaySound(key="$d_avg_audience_chaos", volume=0.5)]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1542_1#4$1", focus="r")]
[name="伊雷妮"]我该出去了，他们没有经历过这种场面，我得在他们身边......
[charslot(slot = "r", name = "avg_npc_1542_1#2$1", focus="r")]
[name="伊雷妮"]我理解，一下子知道太多事情，你需要一点时间想一想。我会安排人守住法院的门口，保证你们不被打扰。
[name="伊雷妮"]但别太久。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", afrom=1, ato=0, duration=1.5, isblock=true)]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="56_g6_courtsquare_n",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r", name = "avg_npc_1556_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_1557_1#1$1", focus="l")]
[name="家族成员A"]怎么回事？这是中了埋伏？
[name="家族成员A"]市政厅早就知道了我们今天晚上的行动？
[charslot(slot = "r", name = "avg_npc_1556_1#1$1", focus="r")]
[name="家族成员B"]我刚刚看到他们的头头进了法院，肯定是去找那个法官了......
[charslot]
[charslot(slot = "m", name = "avg_npc_541_1#6$1")]
[name="卡彭"]慌什么？不过是拉货的卡车，又不是开火的战车。
[name="卡彭"]而且，政府的人自己缩在里面，让一帮开车的出头，还有什么好怕的？
[charslot(slot = "m", name = "avg_npc_541_1#1$1")]
[name="卡彭"]别管他们。进法院！
[dialog]
[charslot]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=0, loop=true, channel="c")]
[SoundVolume(volume=1, channel="c",fadetime=2)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1542_1#2$1", duration = 1.5, isblock=true)]
[StopSound(channel="c", fadetime=2)]
[Delay(time=0.5)]
[cha

... (全文46238字符)
```

### level_act38side_10_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[name="？？？"]你醒了，幼崽。
[dialog]
[Background(image="56_g2_newvolsiniistreet_n",screenadapt="coverall")]
[bgeffect(name="$eb_dim_openeye",layer=1)]
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=3)]
[charslot(slot = "m", focus="n")]
[name="卢奇诺"]......
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[name="瓦古"]一时间不知道翁贝托是看着自己被衰老和疾病吞噬更可怜，还是看着自己的幼崽一代比一代愚蠢更可悲。
[name="瓦古"]人类真是悲哀！
[dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "m", name = "avg_4155_talr_1#5$2", posfrom="0,-20", posto="0,0", duration=1, isblock=true)]
[name="卢奇诺"]你、你是——
[dialog]
[charslot]
尽管印象已经非常模糊，但卢奇诺记得这个声音。
是在老翁贝托牵着他从郊野的农庄回到德蒙塔诺的那个夜晚......
他看着堆满了工具的操作台和一屋子的布料——这里以后就是他的家了。他感到无比陌生，只能呆呆地坐在椅子上。
老翁贝托在外面和别人说话，隔着窗户，他突然转过头来，似乎在把自己指给谁看，但卢奇诺没有看见他对面的是谁。
那是他的爷爷，他唯一的亲人，卢奇诺感到无比紧张。
然后，卢奇诺听见了一个声音有些愤怒又无奈地说：“故技重施，人类真是无耻！”
[charslot(slot = "m", name = "avg_4155_talr_1#5$2")]
[name="卢奇诺"]你是爷爷的......朋友？
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[name="瓦古"]朋友？
[name="瓦古"]朋友、师生、主仆、雇主与受托人......我已经无从界定我与翁贝托的关系。
[name="瓦古"]我是这片荒野的主人，幼崽，你的爷爷是我的獠牙。
[name="瓦古"]但他的表现实在是太过差劲......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="56_g7_tailorshop",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_sewingmachine", volume=0, loop=true, channel="s")]
[SoundVolume(volume=1, channel="s",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[SoundVolume(volume=0, channel="s",fadetime=2)]
[charslot(slot = "m", name = "avg_npc_1543_1#6$1")]
[name="翁贝托"]——
[charslot(slot = "m", name = "avg_npc_1543_1#2$1")]
[name="翁贝托"]看来是真的老了。
[multiline(name="翁贝托")]以前在操作台边待再久，也不会觉得夜晚有这么漫长......
[charslot(slot = "m", name = "avg_npc_1543_1#1$1")]
[multiline(name="翁贝托",end=true)]更不会连你是什么时候进来的都不知道。
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "char_144_red_7#1", duration=1.5, isblock=true)]
[Delay(time=0.5)]
[name="红"]十分钟前。
[SoundVolume(volume=0.1, channel="s", fadetime=2)]
[charslot(slot = "m", name = "avg_npc_1543_1#3$1")]
[name="翁贝托"]抱歉，你介意我一边工作一边说话吗？
[name="翁贝托"]刚刚有位意想不到的老朋友突然到访，耽误了些时间。这套套装，最关键的几道裁剪和拼接工序，我得抓紧做完......
[name="翁贝托"]至于最后的收尾，卢奇诺那孩子自己应该也能摸索着完成。
[charslot(slot = "m", name = "char_144_red_7#1")]
[name="红"]为什么？
[charslot(slot = "m", name = "avg_npc_1543_1#1$1")]
[name="翁贝托"]嗯？
[charslot(slot = "m", name = "char_144_red_7#1")]
[name="红"]红没有在你身上闻到哪怕一丝狼味。
[name="红"]你也没有使用特殊的手段来隐藏。红刚刚观察过，红能够分辨。
[name="红"]......你真是最后的真狼？
[charslot(slot = "m", name = "avg_npc_1543_1#1$1")]
[name="翁贝托"]“真狼”......唔，你是说獠牙。
[charslot(slot = "m", name = "avg_npc_1543_1#3$1")]
[name="翁贝托"]你没有找错人，孩子。
[dialog]
[StopSound(channel="s", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="56_g2_newvolsiniistreet_n",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[name="瓦古"]......我观察了翁贝托许久。
[name="瓦古"]我看着他上门为形形色色的人服务，在量体时突然将特制的剪刀送进某些人的喉咙，对方甚至连血都很少出。
[name="瓦古"]他并不像英格丽那样能打，但很聪明，懂得如何利用自己的身份。
[name="瓦古"]他也善于隐藏，更多的时间都待在那家叫德蒙塔诺的店里，作为杀手和作为裁缝的生意都很好。
[name="瓦古"]所以我选中了他，我告诉了他狼之主与游戏的存在。
[charslot(slot = "m", name = "avg_4155_talr_1#5$2")]
[name="卢奇诺"]爷爷的故事竟然都是真的！
[charslot(slot = "m", name = "avg_4155_talr_1#1$2")]
[name="卢奇诺"]你就是故事里的狼......难怪他会想要脱离家族，作为被狼之主选中的人类，作为叙拉古最特别的裁缝，他当然拥有那份清醒！
[name="卢奇诺"]爷爷答应了你吗？
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[name="瓦古"]没有獠牙能够拒绝狼之主。
[name="瓦古"]但翁贝托提出了一个条件。
[charslot(slot = "m", name = "avg_4155_talr_1#5$2")]
[name="卢奇诺"]条、条件？
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[name="瓦古"]漫长的岁月里，他并非第一个试图和狼之主讲条件的獠牙。狂妄的人类，我有一百种方法毁灭他们，再去物色新的人选。
[charslot(slot = "m", name = "avg_4155_talr_1#5$2")]
[name="卢奇诺"]爷爷他想要做什么？
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[name="瓦古"]翁贝托希望在为我赢得胜利之前，能够先将自己的幼崽抚养成人。
[name="瓦古"]他说他的妻子已经病亡，名为卢卡的幼崽年纪尚小，如果脱离了他，可能无法生存。
[charslot(slot = "m", name = "avg_4155_talr_1#5$2")]
[name="卢奇诺"]仅仅是这样？
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[name="瓦古"]仅仅是这样。所以我答应了。
[name="瓦古"]人类社会不比荒野那般凶险，养育一个幼崽而已，我彼时没有想过这会耗去他如此多的时间和精力。
[name="瓦古"]我会定期去那间裁缝店看看，确保他没有对我欺瞒。
[name="瓦古"]那之后，翁贝托停下了他的杀手业务，他所有的时间都投在了缝纫机、布料和那个日渐长大的幼崽身上。
[name="瓦古"]但他挥动剪刀的手依旧稳健，眼神依旧锐利，所以我愿意遵守承诺。
[name="瓦古"]我需要的是一支不会折断的獠牙，而非随时会因分心被咬断喉咙的牺牲品。我可以给他时间，我有的是时间。
[charslot(slot = "m", name = "avg_4155_talr_1#6$2")]
[name="卢奇诺"]可是爸爸他最终......
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[name="瓦古"]稀里糊涂地死了。
[name="瓦古"]翁贝托有些失魂落魄，我给了他足够的时间平复心情。
[name="瓦古"]虽然和翁贝托本来的计划有些出入，但总归他没有了牵挂。所以某个夜晚，我再次找上了他，要求他兑现承诺。
[name="瓦古"]可我的獠牙，竟然再次提出了一个条件——
狼之主突然停了下来，注视着眼前的小裁缝。
[charslot(slot = "m", name = "avg_4155_talr_1#5$2")]
[name="卢奇诺"]难道说......
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[name="瓦古"]他意外得知自己的幼崽竟然留下了血脉，他在世间还有唯一的亲人......他希望在开始狩猎之前，将你抚养成人。
[charslot(slot = "m", name = "avg_4155_talr_1#1$2")]
[name="卢奇诺"]“故技重施，人类真是无耻！”
[name="卢奇诺"]我那天晚上听到的......
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[name="瓦古"]这一次我并未同意，但他似乎忘记了自己卑贱的身份，忘记了我与他的关系！
[name="瓦古"]每次找到他，他都是絮叨着什么人生的很多情节像是重来了一遍，却还恬不知耻地说不会赖掉对我的承诺。
[charslot(slot = "m", name = "avg_4155_talr_1#6$2")]
[name="卢奇诺"]......
[name="卢奇诺"]可是从我记事起，爷爷的身体就已经不太好了。
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[name="瓦古"]作为獠牙，别说为我赢取胜利，他甚至已经无法解决自己的那些麻烦，这样的他连自保都困难......
[name="瓦古"]漫长的时间里，我等待他抽身，却只等来了他的衰老。
[charslot(slot = "m", name = "avg_4155_talr_1#6$2")]
[name="卢奇诺"]其实爷爷他——
[charslot(slot = "m", name = "avg_npc_1548_1#1$1")]
[name="瓦古"]我知道。
[name="瓦古"]我知道他真正在乎的从来都只有他的德蒙塔诺，他的那些套装，和自己身边的那些人。
[name="瓦古"]所以他才愿意去做那些他本来做不到的事情......翁贝托就是这样愚蠢的人类，我错看了他。


... (全文35002字符)
```

### level_act38side_10_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="56_g6_courtsquare_n",screenadapt="coverall")]
[Delay(time=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_gunshot", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[charslot(slot = "r", name = "avg_npc_1556_1#1$1", duration=0.5)]
[charslot(slot = "l", name = "avg_npc_1557_1#1$1", duration=0.5, isblock=true)]
[name="家族成员A&B"]......
[charslot]
[charslot(slot = "r", name = "avg_npc_1561_1#3$1")]
[charslot(slot = "l", name = "avg_npc_1550_1#3$1")]
[name="卡车司机A&B"]......
[charslot]
[charslot(slot = "m", name = "avg_1502_crosly_1#4$1")]
[name="柳德米拉"]......
[charslot(slot = "m", name = "avg_npc_1542_1#5$1")]
[name="伊雷妮"]......
[dialog]
[charslot]
[PlaySound(key="$d_avg_carnival_crown", volume=0, loop=true, channel="carn")]
[SoundVolume(volume=0.8, channel="carn",fadetime=2)]
[Delay(time=1.5)]
[SoundVolume(volume=0.2, channel="carn",fadetime=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r", name = "avg_npc_1556_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_1557_1#1$1", focus="l")]
[name="家族成员A"]*叙拉古粗口*，我、我还没有下令，你怎么敢扣动扳机？
[charslot(slot = "r", name = "avg_npc_1556_1#1$1", focus="r")]
[name="家族成员B"]不是我，我才刚刚拉开铳的保险——
[name="家族成员B"]也不是对面那些司机，看他们都已经被吓傻了，在那儿摸来摸去检查有没有伤口呢......
[charslot(slot = "l", name = "avg_npc_1557_1#1$1", focus="l")]
[name="家族成员A"]是有谁的武器走火了吗？
[charslot(slot = "r", name = "avg_npc_1556_1#1$1", focus="r")]
[name="家族成员B"]不对，没有人受伤——那铳响究竟是哪儿来的......
[name="家族成员B"]不是，刚刚我还知道怎么办，这突然冒出来一声铳响......现、现在该怎么办？
[charslot(slot = "l", name = "avg_npc_1557_1#1$1", focus="l")]
[name="家族成员A"]花车，我已经看见第一辆花车的兽头了......
[charslot]
[charslot(slot = "m", name = "avg_npc_1542_1#2$1")]
[name="伊雷妮"]......喂，对面的。
[dialog]
[StopSound(channel="carn", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="56_g4_newvolsiniialley_n",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_firework_amb", volume=0, loop=true, channel="fire")]
[SoundVolume(volume=0.4, channel="fire",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>三分钟前</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[name="？？？"]咳咳——嘶——
[name="？？？"]两百米、就两百米......
[dialog]
[PlaySound(key="$d_avg_openftstpwalk", volume=1)]
[charslot(slot = "m", name = "avg_npc_1544_1#11$2", bstart=0.2,bend=0.7, duration=1)]
[delay(time=1.5)]
[name="安东尼奥"]英格丽，你的刀术还是那么，咳，精准......
[name="安东尼奥"]真疼啊，就像你说的那样，我能感受到自己的血正在一点点往外流......但这也意味着，我还有时间......
[name="安东尼奥"]只要走出这条巷子，回到广场，我就还能控制局势......
[name="安东尼奥"]我们已经占领了法院、占领了港口......
[name="安东尼奥"]我会死去，咳咳，但在那之前，我要坐在法官席上，下达最后的命令，宣布对这座可笑试验场的，咳咳，判决......
[dialog]
[PlaySound(key="$d_avg_openftstpwalk", volume=1)]
[charslot(duration=1.5, isblock=true)]
安东尼奥扶着墙壁，勉力支撑自己不倒下，他颤颤巍巍地朝着出口挪去。
巷子很暗，对此时此刻的他来说，着实有些难走。
他没来由地想起当年，他领着那些从辛嘉斯政府手下死里逃生的游击队员，趁着夜色穿越雨林，逃离玻利瓦尔。
安东尼奥想着那个酒鬼贵族随手在名单上画的圆圈，和他最后被游击队员们割下的头。
安东尼奥想着英格丽、老威尼斯，还有莱昂图索、阿尔贝托、西西里夫人......这些他讨厌的人。
他要从他们手里夺走一切，他要在所有人的名字上画一个大大的叉。
[name="安东尼奥"]还没有结束，远远没有——
[dialog]
[PlaySound(key="$d_avg_gunload", volume=1)]
[delay(time=1.5)]
他突然停下了。
冰凉的触感，一把铳抵在了他的额头上。
[dialog]
[charslot(slot = "m", name = "avg_npc_1555_1#1$1", duration=1)]
[delay(time=1.5)]
[name="紧张的家族成员"]安、安东尼奥。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1544_1#6$2", duration=0.5, isblock=true)]
[name="安东尼奥"]......
[name="安东尼奥"]卡尔？
[charslot(slot = "m", name = "avg_npc_1544_1#8$2")]
[name="安东尼奥"]我不是已经让你滚出——
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_npc_1555_1#1$1")]
[name="紧张的家族成员"]我、我凭什么走！
[name="紧张的家族成员"]安东尼奥，你、你到底有什么资格？
[name="紧张的家族成员"]你只是老爷养的一条看门牙兽，哪怕你再怎么修饰自己的耳朵和尾巴，你——
[charslot(slot = "m", name = "avg_npc_1544_1#9$2")]
[name="安东尼奥"]你要杀我？
[name="安东尼奥"]你？
[name="安东尼奥"]你的手都还在抖！
[name="安东尼奥"]你知不知道我的敌人都是谁，你知不知道我在创造怎样的事业？你这个一无是处愚蠢不堪的狼——
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[PlaySound(key="$d_avg_gunshot", volume=1)]
[charslot(slot = "m", name = "avg_npc_1544_1#6$2")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_avg_bulletshtland", volume=1)]
[delay(time=1.5)]
[PlaySound(key="$bodyfalldown2", volume=1)]
[charslot(slot = "m", posfrom="0,0", posto="0,-50", afrom=1, ato=0, duration=0.5, isblock=true)]
[delay(time=1)]
[charslot]
[charslot(slot = "m", name = "avg_npc_1555_1#1$1")]
[name="紧张的家族成员"]......
[charslot]
卡尔呆呆地看着眼前倒地的人。安东尼奥最后的表情写满了愤怒，这愤怒卡尔前所未见。
卡尔甚至有种错觉，仿佛榨干对方最后生机的，不是子弹，而是自己杀了他这件事本身。
血在安东尼奥的身下漾开，顺着地面的纹路，看起来像是一个巨大的叉。
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot = "m", name = "avg_npc_1555_1#1$1")]
[delay(time=0.2)]
[charslot(slot = "m", afrom=1, ato=0, duration=0.5, isblock=true)]
[StopSound(channel="fire", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="56_g6_courtsquare_n",screenadapt="coverall")]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1542_1#2$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="伊雷妮"]喂，对面的。
[charslot(slot = "m", focus="n")]
[name="柳德米拉"]伊雷妮？
[charslot(slot = "m", name = "avg_npc_1542_1#2$1")]
[name="伊雷妮"]没事。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5, isblock=true)]
在所有人的注视

... (全文31538字符)
```

### level_act38side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act38side/PV01.mp4")]
```


> 本章节共40个脚本文件，此处展示前30个。

## 统计

- 总字符数：513605
- 对话行数：3886


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
