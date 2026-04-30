# 明日方舟 · 活动剧情 · act46side（33段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act46side」完整剧情脚本（33个文件，4277行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act46side
- 脚本文件数：33

### guide_act46side_monopoly_stage1

```
[HEADER(is_skippable=false, is_tutorial=true)] 重建谢拉格教程关
[PopupDialog(dialogHead="$avatar_gnosis")] 博士，谢拉格火车站因雪崩严重坍塌，请在移动中收集不同种类的资源，在限定的回合数内获得一定数量的重建值，完成灾后重建。
[Tutorial(target="monopoly_panel_mission", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_gnosis", dialogX=-600, dialogY=-114)] 这里是任务清单，记载着需要完成的任务与所需材料。收集资源时，所有任务同步累计进度，当前任务完成后会自动为你补充新的任务。
[Tutorial(target="monopoly_panel_map", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_gnosis", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 画面中间是火车站地图。你可以在这里看到当前所处的位置，预览不同区域内的资源种类与单次收集可获得的基础数量。
[Tutorial(target="monopoly_panel_card", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_gnosis")] 下方为行动区，每回合你将获得数张修缮规划，可以选择其一，用于前进或收集资源。使用修缮规划收集资源时，若修缮规划的点数为X，则获得的资源为区域基础数量的X倍。
[Tutorial(target="monopoly_panel_card", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_gnosis")] <color=#00aff8>完成一次前进后，才可对当前区域进行一次资源收集。</color>
[Tutorial(target="monopoly_panel_card", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_gnosis")] 收集资源时，<color=#00aff8>点数连续的修缮规划可连续使用（combo）</color>，显著提升收集效率。<color=#00aff8>每次连续使用（combo）都会额外获得一定数量的全种类资源。</color>
[Tutorial(target="monopoly_panel_round", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_gnosis")] 当前已完成的回合数可在此查看，点击结束回合后，剩余修缮规划清空，进入下一回合。
[Tutorial(target="monopoly_panel_buff", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_gnosis", dialogX=-600, dialogY=104)] 在不同的可重建区域中，存在着不同的场地效果，具体内容可点击上方图标查看。合理利用场地效果，便能事半功倍。
```

### act46side_05

```
[HEADER(is_tutorial=true, is_skippable=false, is_autoable=false)] 活动46side普通关_05
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.2)]
[popupdialog(dialogHead="$avatar_aguard")]看来，干员不得不部署在<@tu.kw>禁区</>里了。
[tutorial(focusWidth=300, focusHeight=300, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_aguard", tileY=2, tileX=4)]别担心，博士。我们只要守住<@tu.kw>禁区</>别让敌人进入就行。
```

### act46side_10

```
[HEADER(is_tutorial=true, is_skippable=false, is_autoable=false)] 活动46side普通关_10
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.2)]
[popupdialog(dialogHead="$avatar_aguard", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]初雪要向<@tu.kw>圣女像</>祈祷，她可以唤醒耶拉冈德，只是需要时间。
[popupdialog(dialogHead="$avatar_aguard", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]而雪崩会打断祈祷仪式。
[popupdialog(dialogHead="$avatar_aguard", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]注意保护初雪，维持仪式的进行。
```

### level_act46side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="67_G1_stationruins",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[playsound(key="$d_avg_crowdtalk_fear", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.8, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_199_yak_1#6$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_199_yak_1#6$1",focus="m")]
[name="角峰"]一队，把物资放到东边的空地。
[name="角峰"]配合佩尔罗契的增援一起搭建医疗帐篷，准备接收伤员！
[Dialog]
[charslot]
[name="救援队员A"]明白！
[charslot(slot="m",name="avg_199_yak_1#6$1",focus="m")]
[name="角峰"]二队，带上雪铲和酒袋，继续在火车站那边的废墟寻找幸存者。仔细搜，不要漏听呼救声。
[Dialog]
[charslot]
[name="救援队员B"]明白！大家伙，带上东西跟我走——
[charslot(slot="m",name="avg_199_yak_1#6$1",focus="m")]
[name="角峰"]切记不要发出太大的声音，山上的情况还不清楚，不排除还有发生二次雪崩的可能。探查情况的小队已经在去往山顶的路上了。
[charslot(slot="m",name="avg_199_yak_1#3$1",focus="m")]
[name="角峰"]相信我们的同伴，相信耶拉冈德正在庇佑着谢拉格人。
[Dialog]
[charslot]
[name="救援队员B"]耶拉冈德在上。
[name="救援队员A"]......耶拉冈德在上。
[charslot(slot="m",name="avg_199_yak_1#6$1",focus="m")]
[name="角峰"]耶拉冈德在上。
[charslot(slot="m",name="avg_199_yak_1#1$1",focus="m")]
[name="角峰"]时间不等人，立刻开始行动吧。
[Dialog]
[charslot]
[name="众救援队员"]是！
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[PlaySound(key="$d_avg_snowcrwdmarch",volume=1)]
[charslot(duration=1)]
[delay(time=2)]
交叠在一起的回答声还未从冷风中散去，希瓦艾什家的侍从已经在雪地上散开，奔向各个方向。
在这里的不只有他们，这场白色的崩溃显然在祥和的日子里造成了一片清晰的创口。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="67_G1_stationruins",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_snowfall", volume=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_283_1#1$1",focus="m")]
[name="救援队员"]这里，这里还有一个活着的！
[charslot(slot="m",name="avg_npc_254_1#7$1",focus="m")]
[name="阿克托斯"]喂——撑住了！是个谢拉格人就给我咬着牙挺住了，别睡着！
[Dialog]
[charslot]
[name="受伤的男人"]腿，我的腿......
[name="受伤的男人"]我的腿动不了，我的腿已经......呃！
[charslot(slot="m",name="avg_npc_254_1#7$1",focus="m")]
[name="阿克托斯"]别动！后面的，情况看清楚了没，到底怎么样？！
[charslot(slot="m",name="avg_npc_283_1#1$1",focus="m")]
[name="救援队员"]挖开了，雪洞已经挖开了！但是他的腿被钢筋压住了，如果这玩意儿没断就只能找医生来......不对，先别急，我再挖开一点试试！
[Dialog]
[charslot]
[playsound(key="$d_avg_brnchflsnw", volume=0.8)]
[CameraShake(duration=1, xstrength=15, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_283_1#1$1",focus="m")]
[name="救援队员"]呼——嘿！呼......好消息，这钢筋已经完全断了，我们只要能抬起来就行！
[charslot(slot="m",name="avg_npc_254_1#1$1",focus="m")]
[name="阿克托斯"]出力气能办好的事儿都不用担心，都过来，搭把手！
[multiline(name="阿克托斯")]抓稳了，一、二、三
[charslot(slot="m",name="avg_npc_254_1#8$1",focus="m")]
[PlaySound(key="$d_avg_scratchmetalwall", volume=1, loop=true, channel="sc")]
[StopSound(channel="sc", fadetime=1.5)]
[CameraShake(duration=1, xstrength=12, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.5)]
[multiline(name="阿克托斯")]——喝啊！
[Dialog]
[charslot]
[name="受伤的男人"]痛、呃啊啊......好痛......
[charslot(slot="m",name="avg_npc_254_1#7$1",focus="m")]
[name="阿克托斯"]好了，有空当了，把他拖出来！尽快！
[charslot(slot="m",name="avg_npc_283_1#1$1",focus="m")]
[name="救援队员"]我拉住他了，轻一点，把他的身体抬起来，用布垫在底下，对，小心，别扯到他的伤口......
[multiline(name="救援队员")]就这样慢慢地拖出来——
[PlaySound(key="$d_avg_clothtrailground", volume=1)]
[delay(time=1)]
[multiline(name="救援队员")]好！成了！担架，快点把担架弄过来！
[Dialog]
[charslot(slot = "m", name = "avg_npc_501_1#1$1",focus="m")]
[PlaySound(key="$d_avg_kneelsnow_s", volume=1)]
[name="罗德岛医疗干员"]让一让，让一让，担架到了！
[Dialog]
[charslot]
压抑着的、克制着的呼唤。救援。担架。生还者。
白茫茫的雪地之上，无数人忙碌地奔跑着，脸颊滚烫，甚至溢出汗水。
[charslot(slot="m",name="avg_npc_254_1#1$1",focus="m")]
[name="阿克托斯"]古罗，这边暂时交给你。看好了，能救活的一个也别放弃。
[charslot(slot="m",name="avg_npc_260_1#1$1",focus="m")]
[multiline(name="古罗")]明白！
[charslot(slot="m",name="avg_npc_260_1#7$1",focus="m")]
[multiline(name="古罗")]但......您要去哪儿？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="67_G1_stationruins",screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_199_yak_1#4$1")]
[charslot(slot="r",name="avg_npc_254_1#1$1")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_199_yak_1#4$1",focus="l")]
[name="角峰"]阿克托斯老爷......南侧的救援难道已经结束了？
[charslot(slot="r",name="avg_npc_254_1#1$1",focus="r")]
[name="阿克托斯"]没，还没结束。
[name="阿克托斯"]古罗在看着，我是来找你的。
[charslot(slot="l",name="avg_199_yak_1#1$1",focus="l")]
[name="角峰"]我们这里还算顺利，您不用担心。布朗陶的增援也到了，带来了不少毛毯和食物。
[name="角峰"]菈塔托丝夫人本想亲自过来的，但似乎实在是分不开身。
[charslot(slot="r",name="avg_npc_254_1#5$1",focus="r")]
[name="阿克托斯"]......算了，想来也是。
[charslot(slot="r",name="avg_npc_254_1#1$1",focus="r")]
[name="阿克托斯"]大家心里有数，没人会因为这个怪她的。
[charslot(slot="r",name="avg_npc_254_1#7$1",focus="r")]
[name="阿克托斯"]*谢拉格俚语*，怎么就碰上了这么场灾！
[charslot(slot="l",name="avg_199_yak_1#6$1",focus="l")]
[name="角峰"]这次雪崩来得太突然了，没有一点征兆，我们所有人都没有预备。
[charslot(slot="r",name="avg_npc_254_1#7$1",focus="r")]
[name="阿克托斯"]对，就是这个，我要找你说的就是这个事儿！
[name="阿克托斯"]你知道谢拉格的规矩，这雪崩发生的地方在佩尔罗契家的领地，我们负责照看领地内的雪山。
[name="阿克托斯"]我们一直在记录积雪的厚度，那记录我看了好几次，明明一切正常！
[charslot(slot="r",name="avg_npc_254_1#5$1",focus="r")]
[name="阿克托斯"]所以我才来问你，你们那个什么研究院里不是还有人专门跑去看雪山的吗？那些人怎么说？
[charslot(slot="l",name="avg_199_yak_1#4$1",focus="l")]
[name="角峰"]研究院......您说莱茵生命？
[charslot(slot="r",name="avg_npc_254_1#5$1",focus="r")]
[name="阿克托斯"]是啊，他们天天在山上跑来跑去的，鼓捣什么高科技装备，总不能一点发现都没有吧？
[charslot(slot="l",name="avg_199_yak_1#2$1",focus="l")]
[name="角峰"]按理来说应该是有的。但他们也有自己的任务，未必会把所有精力都放在研究雪山上。
[name="角峰"]而且雪崩发生后我们立刻就赶过来了，他们到底有没有发现什么我也并不确定。
[name="角峰"]恩希欧迪斯老爷也派了锏小姐带领队伍上山调查，估计很快就能回来了。
[charslot(slot="r",name="avg_npc_254_1#2$1",focus="r")]
[name="阿克托斯"]嗯......
[charslot(slot="r",name="avg_npc_254_1#9$1",focus="r")]
[name="阿克托斯"]啧，总觉得后背发凉，这场雪崩到底是什

... (全文17450字符)
```

### level_act46side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="67_G3_rhineobservatory_i",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0.7, keep=true)]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>谢拉格-莱茵生命观测站</><p=2>两个月前</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot="m",name="avg_249_mlyss_1#7$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_249_mlyss_1#7$1",focus="m")]
[name="缪尔赛思"]哇......建得真快，这个规模的观测站居然这么点时间就搭出来了......
[charslot(slot="m",name="avg_249_mlyss_1#9$1",focus="m")]
[name="缪尔赛思"]这样的工程体量，商务科这回怕是要大出血了吧。
[charslot(slot="m",name="avg_1031_slent2_1#7$1",focus="m")]
[name="赫默"]谢拉格观测站的议案在委员会投票通过后的第一时间，就有两位数的金融机构找了上来。
[name="赫默"]这样看来，经费反而是这次项目中最不需要担心的环节。
[charslot(slot="m",name="avg_249_mlyss_1#2$1",focus="m")]
[name="缪尔赛思"]赫默，老实说......我本来以为这项提案在委员会那边没这么容易通过呢。
[charslot(slot="m",name="avg_1031_slent2_1#1$1",focus="m")]
[name="赫默"]......我犹豫过，我仍然坚持认为现在莱茵生命对于“星荚”的研究进度还是算得上激进，还有许多潜在的问题我们都没有考虑周全。
[name="赫默"]可是我也认识到，或许我期待的那个稳定的局面永远不会到来。
[name="赫默"]不管任何时候，我们能相信的只能是具体的人。
[charslot(slot="m",name="avg_249_mlyss_1#1$1",focus="m")]
[name="缪尔赛思"]那我要感谢你的信任啦，赫默委员。
[charslot(slot="m",name="avg_1031_slent2_1#6$1",focus="m")]
[name="赫默"]希望我们做的这一切，都是有价值的......
[charslot(slot="m",name="avg_249_mlyss_1#9$1",focus="m")]
[name="缪尔赛思"]当然啦，对于整个莱茵生命来说这个观测站都是绝无仅有的机会吧。
[name="缪尔赛思"]除了星荚的研究，谢拉格低源石浓度的环境也是很难得的生物研究环境。还有马里亚姆！他也一直说早就想来喀兰雪山看看了。
[name="缪尔赛思"]就连斐尔迪南，拿到观测站的立项通知后，只用了两周的时间就给出了观测站核心能量井的供能方案。
[name="缪尔赛思"]不过之后他就又一头扎进他的理论研究里去了，负责后续落地工作的是能量科的埃琳娜。
[charslot(slot="m",name="avg_1031_slent2_1#6$1",focus="m")]
[name="赫默"]希望在考察之外，和谢拉格方面的相处也可以顺利......
[dialog]
[charslot]
[playsound(key="$d_avg_glassdooropen")]
[delay(time=1)]
[dialog]
[name="？？？"]我想这一点就不劳各位学者操心了。
观测站的大门从外侧打开，来人扫去肩头落下的雪花，走入室内。
[dialog]
[charslot(slot="m",name="avg_206_gnosis_1#1$1",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_249_mlyss_1#9$1",focus="m")]
[name="缪尔赛思"]又见面了，诺希斯先生。
[charslot(slot="m",name="avg_206_gnosis_1#1$1",focus="m")]
[name="诺希斯"]例行访问，来确认观测站的修建工作是否有需要帮助的地方......
[charslot(slot="m",name="avg_206_gnosis_1#9$1",focus="m")]
[name="诺希斯"]不过看上去，这里的进度十分理想。
[dialog]
[charslot]
诺希斯抬起头，莱茵生命观测站光洁而宽阔的吊顶之上镶嵌着散发柔光的灯带。
莱茵生命与喀兰贸易合力，在短得不可思议的时间内搭建起了这座结实又光亮的小殿堂。
外形特殊、先锋，和谢拉格的民居相比如同来自未来的造物。
[charslot(slot="m",name="avg_206_gnosis_1#9$1",focus="m")]
[name="诺希斯"]喀兰贸易会尽一切可能协助莱茵生命推进观测站的项目，也愿意在工作之外为各位提供必要的帮助。
[name="诺希斯"]只要莱茵生命不违背条约中的共识，各位在谢拉格的活动就可以畅通无阻。
[charslot(slot="m",name="avg_1031_slent2_1#1$1",focus="m")]
[name="赫默"]......谢谢您的好意，诺希斯先生。
[name="赫默"]莱茵生命只是一个科研公司，除了科学研究外不会有任何别的目的。我想我们没有理由主动破坏条约。
[charslot(slot="m",name="avg_206_gnosis_1#9$1",focus="m")]
[name="诺希斯"]......当然，我也是这样相信的。
[name="诺希斯"]像这样的跨国合作，在整个泰拉都没有先例，这样的初次尝试必然会有重重阻碍......
[charslot(slot="m",name="avg_206_gnosis_1#1$1",focus="m")]
[name="诺希斯"]我只是想强调，只要我们双方在科研信息上保持必要的坦诚，类似特里蒙那样的意外情况，完全可以避免。
[charslot(slot="m",name="avg_1031_slent2_1#5$1",focus="m")]
[name="赫默"]......
[charslot(slot="m",name="avg_249_mlyss_1#9$1",focus="m")]
[name="缪尔赛思"]对了！圣女大人会来观测站访问吗？
[charslot(slot="m",name="avg_206_gnosis_1#1$1",focus="m")]
[name="诺希斯"]等观测站正式落成的时候，圣女应该会出席相关的仪式......您想见圣女大人，是有什么事吗？
[charslot(slot="m",name="avg_249_mlyss_1#1$1",focus="m")]
[name="缪尔赛思"]哎呀，没有什么严肃的理由啦，只是有点好奇。
[name="缪尔赛思"]我还记得上次拜访圣女大人的时候，她一开始还对我们的合作项目十分抵触，可后来忽然之间就同意了。
[name="缪尔赛思"]我有点好奇，她到底是因为什么才转变了想法，一直都想找个机会问问她呢。
[charslot(slot="m",name="avg_206_gnosis_1#1$1",focus="m")]
[name="诺希斯"]圣女平日工作繁忙，如果您想和圣女交流的话，可以抽空去参与一下本地的仪式活动......如果您感兴趣的话。
[name="诺希斯"]圣女和蔓珠院的长老都会很乐意招待各位......如果各位有这样的打算，我会代为安排。
[charslot(slot="m",name="avg_249_mlyss_1#10$1",focus="m")]
[name="缪尔赛思"]好周到，您真是适合做这份工作~
[charslot(slot="m",name="avg_206_gnosis_1#1$1",focus="m")]
[name="诺希斯"]基本的地主之谊，这是谢拉格应该做的。
[name="诺希斯"]各位应该都会在谢拉格留一段时间，我们都希望这是一段没有麻烦......愉快的合作。
[charslot(slot="m",name="avg_249_mlyss_1#9$1",focus="m")]
[name="缪尔赛思"]多谢您的体贴，如果没有您的帮助，这次的合作很难进展得如此顺利。
[charslot(slot="m",name="avg_206_gnosis_1#1$1",focus="m")]
[name="诺希斯"]不，不是帮助。是达成我们共同的目标。缪尔赛思小姐。
[name="诺希斯"]喀兰贸易为你们连接谢拉格的山峰，铺设方便前来的路与行动的自由。
[name="诺希斯"]按照约定，莱茵生命会共享研究本地生态得出的部分数据，协助本土药物研发。
[charslot(slot="m",name="avg_249_mlyss_1#9$1",focus="m")]
[name="缪尔赛思"]当然，菲茨罗伊主任会针对合同的细节和喀兰贸易详谈的。
[name="缪尔赛思"]我只是个研究员，没那么善于交际。只希望能让您相信，莱茵生命是带着绝对友好的态度来到这片神圣的土地的。
[charslot(slot="m",name="avg_206_gnosis_1#9$1",focus="m")]
[name="诺希斯"]至少在这一点上，我们应该没有区别。
[dialog]
[charslot]
二人握手，相互点头，脸上带着笑。如同所有下方题注着“展开友好合作”的新闻照一样。
[charslot(slot="m",name="avg_206_gnosis_1#9$1",focus="m")]
[name="诺希斯"]不必有太多担忧......
[charslot(slot="m",name="avg_206_gnosis_1#1$1",focus="m")]
[name="诺希斯"]只要遵守契约，我们就仍是“朋友”。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="38_g5_rhinelab_indoor",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_1047_halo2_1#17$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_2007_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_2007_1#1$1",focus="r")]
[name="能量科研究员"]埃琳娜组长，喀兰贸易的代表来了。
[name="能量科研究员"]他们要求尽快与莱茵生命代表进行会面。
[charslot(slot="l",name="avg_1047_halo2_1#17$1",focus="l")]
[name="埃琳娜"]为什么？我们近期应该没有与喀兰贸易开会的安排吧？
[name="埃琳娜"]......是因为天灾？
[charslot(slot="r",name="avg_npc_2007_1#1$1",focus="r")]
[name="能量科研究员"]嗯......
[name="能量科研究员"]他们希望能就天灾的成因和莱茵生命进行讨论，至少希望我们可以提供观测站的观测数据。
[charslot(slot="l",name="avg_1047_halo2_1#12$1",focus="l")]
[name="埃琳娜"]我明白了......
[charslot(slot="l",name="avg_1047_halo2_1#17$1",focus="l")]
[name="埃琳娜"]对了，你见到卡罗琳前辈了吗？观测数据应该是她在负责吧？
[charslot(slot="r",name="a

... (全文14297字符)
```

### level_act46side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="67_G2_rhineobservatory_o",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[PlaySound(key="$d_avg_crwddiscuss_outside",loop=true, channel="mes", volume=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_278_1#1$1",focus="m")]
[name="呼喊的村民"]不洁净者......不洁净者！就是他们，践踏了圣山，践踏了谢拉格的信仰！
[name="呼喊的村民"]是这不属于谢拉格的铁屋子——点燃了耶拉冈德的怒火！
[charslot(slot="m",name="avg_npc_277_1#1$1",focus="m")]
[name="男性村民"]耶拉冈德在上，请您宽恕我们的罪过......
[Dialog]
[charslot]
祈祷的声音，啜泣的声音，呼唤的夹杂着愤怒的声音。
杂乱的声响拧成一股绳索，将一个又一个点缀着泪水或是惊怒的脸孔串成珠链，围着新落成的观测站盘绕。
那道铁门依旧岿然不动。人群之中传来一道苍老的声音。
[name="老妇人村民"]“你们要记得，群山之中终年盘旋的风，不是空无而来的风。”
寒风仍在呼啸，老妇一步步向前，涉过雪地走向紧闭的门扉。她的声音清晰地传入人们耳中。
[name="老妇人村民"]“那是祂的呼吸，从雪白峰顶上吹拂而下。”
[charslot(slot="m",name="avg_npc_282_1#1$1",focus="m")]
[name="女性村民"]“那是祂昼夜不息的守卫，从幽深谷底里重返云端。”
[Dialog]
[charslot]
[name="众村民"]“它将驱散邪瘴的雾气，赶灭藏身于石缝里的毒虫。”
[name="众村民"]“它将一切声响都带回祂的耳边，使祂明辨，群山就此清明了——”
[charslot(slot="m",name="avg_npc_282_1#1$1",focus="m")]
[name="女性村民"]等等，那扇门......那扇门是不是动了？
[charslot(slot="m",name="avg_npc_278_1#1$1",focus="m")]
[name="呼喊的村民"]太好了！他们开门了，各位，我们的抗议是有效的！
[name="呼喊的村民"]开门！打开门来，听听我们的声音！
[name="呼喊的村民"]听耶拉冈德的子民、谢拉格人真正的声音吧，这里已经不欢迎你们了，你们必须离开！
[charslot(slot="m",name="avg_npc_282_1#1$1",focus="m")]
[name="女性村民"]外来者，离开圣山！回到你们来的地方去！
[Dialog]
[charslot(slot="m",name="avg_npc_278_1#1$1",focus="m")]
[CameraShake(duration=0.5, xstrength=15, ystrength=20, vibrato=25, randomness=90, fadeout=true, block=false)]
[name="呼喊的村民"]外来者！离开圣山！
[CameraShake(duration=0.7, xstrength=30, ystrength=30, vibrato=25, randomness=90, fadeout=true, block=false)]
[name="呼喊的村民"]外来者！离开圣山！
[Dialog]
[charslot]
汇集的呼声越来越大，也越来越明晰。有人伸出双手，向着天空挥舞。
是出于诚心祈祷之故吗？或是齐声祈祷的气势足以震动钢铁？
[Dialog]
[StopSound(channel="mes", fadetime=2.5)]
[PlaySound(key="$d_gen_dooropen", volume=1)]
[delay(time=2)]
大门打开了。
一时间，所有声音都在屏息之中平静了下去。
[Dialog]
[PlaySound(key="$d_gen_soldiersrun",volume=0.8)]
[charslot(slot="l",name="avg_npc_285_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_286_1#1$1",duration=1)]
[delay(time=2.5)]
[charslot(slot="l",name="avg_npc_285_1#1$1",focus="l")]
[name="希瓦艾什家的侍卫"]......
[charslot(slot="r",name="avg_npc_285_1#1$1",focus="r")]
[name="希瓦艾什家的侍卫"]......
[charslot]
[charslot(slot="m",name="avg_npc_277_1#1$1",focus="m")]
[name="男性村民"]那身衣服，是......是希瓦艾什家的人？
[charslot(slot="m",name="avg_npc_282_1#1$1",focus="m")]
[name="女性村民"]后头那个人是......埃德怀斯家的那位？他是来送这些外来者走的吗？
[charslot(slot="m",name="avg_npc_277_1#1$1",focus="m")]
[name="男性村民"]如果真是就好了，这些人可是他们牵头带进来的，要是真得有人收拾烂摊子，也确实该他们来，但......我看他的表情怎么......
[charslot(slot="m",name="avg_206_gnosis_1#1$1",focus="m")]
[name="诺希斯"]清退示威者。不要造成伤亡。
[charslot(slot="m",name="avg_npc_285_1#1$1",focus="m")]
[name="希瓦艾什家的侍卫"]各位，放下武器，向后退！
[charslot(slot="m",name="avg_npc_282_1#1$1",focus="m")]
[multiline(name="女性村民")]我们不走，你为什么要我们走，该走的......
[PlaySound(key="$d_avg_clothmovementsp",volume=0.8)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=25, randomness=90, fadeout=true, block=false)]
[multiline(name="女性村民")]别拉我！
[charslot(slot="m",name="avg_npc_282_1#1$1",focus="m")]
[name="女性村民"]喂！埃德怀斯！你到底是站哪边的？！
[charslot(slot="m",name="avg_npc_277_1#1$1",focus="m")]
[name="男性村民"]......还能站哪边......他们的武器和盾牌都向着我们了，谁是他的敌人，谁是他的朋友，你还不清楚吗？
[charslot(slot="m",name="avg_206_gnosis_1#2$1",focus="m")]
[name="诺希斯"]......
[charslot(slot="m",name="avg_206_gnosis_1#1$1",focus="m")]
[name="诺希斯"]山上的风雪要变大了。
[name="诺希斯"]在下山的路被堵起来之前，各位还是早些回去吧。
[multiline(name="诺希斯")]不必担心路途中的危险，希瓦艾什家的侍卫会保证各位的安全，把你们送回......
[playsound(key="$d_avg_brnchflsnw")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=25, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[charslot(slot="m",name="avg_206_gnosis_1#5$1",focus="m")]
[multiline(name="诺希斯")]呃！
[charslot(slot="m",name="avg_npc_282_1#1$1",focus="m")]
[name="女性村民"]奶奶，等等......别——
[Dialog]
[charslot]
佝偻的老妇人从侍卫与侍卫的缝隙中挤出一条手臂。
她的动作利落，丝毫不拖泥带水。一捧冰冷的雪挥洒出去，泼了侃侃而谈的黎博利满头满脸。
[name="老妇人村民"]愿耶拉冈德原谅你的罪孽。
沟壑纵横的面目上，怜悯与坚决的慈悲凝结在一起。
她冰冷的手指触碰到诺希斯的额头，画下一道简单的弧线。
那是谢拉格人的习惯，寓意为驱散高热不退的孩子身上沾染的邪祟。
[name="老妇人村民"]愿祂神迹显现，邪瘴的雾气与藏身石缝的毒虫将会离开你的身体......
[name="老妇人村民"]诺希斯，你且记得，耶拉冈德的山风已经造访过你的顽固。
[name="老妇人村民"]如今，是你送祂离去。
[charslot(slot="m",name="avg_206_gnosis_1#1$1",focus="m")]
[name="诺希斯"]......
[name="诺希斯"]早些回去吧，老人家。
[Dialog]
[Delay(time=1)]
诺希斯的表情没有变化，热气呵出，融化的雪水从他脸上缓缓流下。
[charslot(slot="m",name="avg_206_gnosis_1#1$1",focus="m")]
[name="诺希斯"]山风寒冷，不要被吹坏了身子才好。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[verticalbg(cggroup="67_i15_1/67_i15_2", solidwidth="1600", solidheight="900/900",y=200,xScale=0.8, yScale=0.8,fadetime=0)]
[largebgtween(duration = 10,yFrom = 200, yTo = 810,block = false)]
[bgeffect(name="$eb_camara_01",layer = 1)]
[delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[PlaySound(key="$d_avg_devicebeep", volume=1)]
[delay(time=2)]
谢拉格。美丽的秘境，风雪覆盖的洁净之地，虔诚而纯粹的、被庇佑的一隅。
这里的人们信仰仍旧坚定，如同巍峨雪山，亘古不变、屹立不倒。或者，也可从一片雪花开始溃散......
[Dialog]
[delay(time=1)]
“请问您对天灾有什么看法？这会影响您对耶拉冈德的信仰吗？”
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[verticalbg]
[charslot]
[Background(image="bg_snowconutryinside",screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_npc_279_1#1$1",focus="m")]
[delay(time=1)]
[PlaySound(key="$d_avg_camera_snapshot", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[name="谢拉格老人"]谢拉格的信仰不是如此孱弱的东西！就算是往日最严酷的考验，谢拉格人也不曾退步半分！
[name="谢拉格老人"]等天灾处理干净，我的腿能下地了，我就去圣山。
[name="谢拉格老人"]谢拉格的朝阳照耀，沐浴者必将无痛无灾，洗涤一身污浊与诅咒，还有那什么石头病......
[name="谢拉格老人"]耶拉冈德慈悲而宽宏，决然不会抛下谢拉格，只要扫干净积雪，一切都会和往日一样好起来的......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=

... (全文24310字符)
```

### level_act46side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g3_mainhall",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_174_slbell_1#7$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_174_slbell_1#7$1",focus="m")]
[name="恩雅"]......
[Dialog]
[PlaySound(key="$d_avg_open_drawer", volume=1)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_woodenladder", volume=1)]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[PlaySound(key="$d_avg_paper1", volume=1)]
[Delay(time=1)]
[name="恩雅"]“从前冬日漫长，遍地不见食物，祂走入山林中寻觅种子......”
[name="恩雅"]......不对，不会是这一段。
[name="恩雅"]古谢拉格语中甚至不存在“天灾”一词，这是否真的代表谢拉格从来没有发生过天灾？
[name="恩雅"]如果是古时候的人们还没有意识到天灾与其他灾害的区别，那是否会有别的记述......
[Dialog]
[PlaySound(key="$d_avg_paper1", volume=1)]
[Delay(time=1)]
[name="恩雅"]“融化的积雪淹没了农田与牧场......有违时节的寒潮杀死庄稼......”
[name="恩雅"]不对，都不对......这些都不像是对天灾的记述。
[name="恩雅"]我记得还有一个故事，从前她讲过的......
[name="恩雅"]“当寒冷的冬日冻结了喀兰之心，远处的敌人因此渡过冰面而来。”
[name="恩雅"]“手执武器的战士日日守备，这一天黄昏，他在如镜的冰面中见到了可怕的怪物......拉德索恩。”
[name="恩雅"]“战士急切地带回了这个消息以警示邻人，但是......”
[name="阿德颂"]“但是除了战士，没人能看到怪物，没有人相信他说的话，战士因此开始惶惶不可终日。”
[name="恩雅"]阿德颂长老？您是何时......
[Dialog]
[charslot(slot="m",name="avg_npc_1998_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1998_1#1$1",focus="m")]
[name="阿德颂"]今日晨祷后就在这里了。怕打扰到您，所以一直没出声响......刚才听到您提到了熟悉的经文，才忍不住搭话......
[name="阿德颂"]惊扰到了圣女，实在抱歉。
[Dialog]
[charslot]
[name="恩雅"]没什么......我只是以为这个时候，您还在处理政务......
室内灯光昏黄，坐在高处的梯子上，恩雅看到大长老的长袍几乎与木地板的色彩融为一体。
她看不清他的表情。
[name="恩雅"]您刚刚接手大长老的职务，应该十分繁忙吧。可还顺利？
[charslot(slot="m",name="avg_npc_1998_1#2$1",focus="m")]
[name="阿德颂"]请圣女大人见谅，老朽半生的时间都花在了这间藏经阁里，且不说政务，与蔓珠院之外的人打交道的机会都算不上多......
[name="阿德颂"]只是靠这把年纪忝为长老，也只敢说勉力为之......
[Dialog]
[charslot]
[name="恩雅"]您过谦了。就算之前与您交谈的机会不多，但是对您博学的名声也早有耳闻。
[charslot(slot="m",name="avg_npc_1998_1#2$1",focus="m")]
[name="阿德颂"]惭愧......越是研读这些书籍，我就越意识到自己见识的鄙薄，与祂相比，我们都是见识短浅的。
[name="阿德颂"]只是我听闻圣女大人在藏经阁已经两日不眠不休了。所以特地赶来，不知是否能为圣女大人分忧。
[Dialog]
[charslot]
[name="恩雅"]......正好，我也有一些问题想要与您讨论，希望您能为我解惑。
[Dialog]
[PlaySound(key="$d_avg_scroll", volume=1)]
[Delay(time=1.5)]
她合起经卷，将其叠成一沓，转身向下。
[Dialog]
[PlaySound(key="$d_avg_woodenladder", volume=1)]
[Delay(time=1)]
老木梯发出陈旧的吱呀声，忠诚地连接着高处的知识与沉默的地面。
[Dialog]
[PlaySound(key="$d_avg_kneelsnow_s", volume=1)]
[charslot(slot="m",name="avg_174_slbell_1#1$1",duration=0.7)]
[delay(time=1.5)]
[charslot]
抱着经卷，恩雅踱步走出狭窄的书架间隙，在宽大的书桌旁坐下，而桌面上几乎堆满了被翻开的经卷。
[charslot(slot="l",name="avg_174_slbell_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_1998_1#2$1",focus="l")]
[name="恩雅"]这是我这两天整理出来的成果......
[name="恩雅"]我试着搜集了文献中每一处对谢拉格特殊灾害的记录，可我依然没有办法确定，谢拉格过往千年的历史上是否发生过天灾。
[name="恩雅"]更没有办法解释......当下这场天灾，为何偏偏发生在此时。您也知晓，今年的冬季一如既往，并无特别之处。
[charslot(slot="l",name="avg_174_slbell_1#1$1",focus="n")]
少女将眼睛从经书中抬起来，看向面前的大长老。
而老人似乎对摆在面前的经文并无兴趣，他垂首默然，白色的鬓发之下，一双皮肤松弛、垂坠的眼睛缓慢地眯起，拉成一道弧线。
[charslot(slot="l",name="avg_174_slbell_1#7$1",focus="l")]
[name="恩雅"]......大长老似乎并不认同我做的这些功课。
[charslot(slot="r",name="avg_npc_1998_1#1$1",focus="r")]
[name="阿德颂"]不......老朽不敢......
[name="阿德颂"]您在寻觅天灾发生的真相，那降临在眼前的庞然大物，一种表象的恐惧。
[name="阿德颂"]就如遇见山便辟开山道，遇见水便修建桥梁......您的行为当然是合乎逻辑的。
[name="阿德颂"]可是要从头到尾审视谢拉格的历史，搜索与追查只言片语中每一次波折与灾患......此旅实乃苦修，堪比手持烛火在雪地中寻找盐粒。
[charslot(slot="l",name="avg_174_slbell_1#1$1",focus="l")]
[name="恩雅"]这点辛苦不足挂齿......我必须要为这场天灾找到一个合理的解释......我必须要做到。
[charslot(slot="r",name="avg_npc_1998_1#1$1",focus="r")]
[name="阿德颂"]我能体谅圣女大人您心中的焦虑。您为谢拉格担忧，为受灾的百姓心生怜悯......我甚至能感受到，还有某些急切的心情鼓动着您。
[name="阿德颂"]但是这样急切的心情，似乎使您盲目了。
[charslot(slot="l",name="avg_174_slbell_1#6$1",focus="l")]
[name="恩雅"]......
[name="恩雅"]阿德颂大长老，我从来没有在私下的场合询问过您的意见......
[name="恩雅"]您到底如何看待，当下发生在谢拉格的这场天灾？
[charslot(slot="r",name="avg_npc_1998_1#7$1",focus="r")]
[name="阿德颂"]我必须得承认，我的知识是浅薄的，无法解释这场天灾的成因。
[charslot(slot="r",name="avg_npc_1998_1#2$1",focus="r")]
[name="阿德颂"]不过，我倒是十分认同圣女大人前日说过的话......
[name="阿德颂"]耶拉冈德从未向祂的子民许诺过，祂可以保护我们不受天灾的袭扰。
[name="阿德颂"]事实上，耶拉冈德从未向祂的子民许诺过什么。反倒是经文中强调过，不要用“神迹”去验证祂的存在......
[name="阿德颂"]我们信奉祂，只因我们相信祂是善的，祂是一切美德的化身。我们遵循祂的道，会成为更好的“我们”。
[charslot(slot="l",name="avg_174_slbell_1#6$1",focus="l")]
[name="恩雅"]我认同您的看法......
[name="恩雅"]可我同样担忧，对教义这样的诠释并不能服众......
[charslot(slot="r",name="avg_npc_1998_1#2$1",focus="r")]
[name="阿德颂"]是啊，“理性的崇高与真知灼见是一双金鞋子，它能让你走得更远，但你也要有能穿进去的脚。”
[name="阿德颂"]也许有朝一日，您的真理之路会行得通。但不是现在，至少，不是现在。
[charslot(slot="l",name="avg_174_slbell_1#6$1",focus="l")]
[name="恩雅"]我们现在到底该怎么做......
[charslot(slot="r",name="avg_npc_1998_1#2$1",focus="r")]
[name="阿德颂"]该如何去做......老朽也无法给出答案。
[name="阿德颂"]圣女大人，您刚刚念到过“拉德索恩”的故事......那就让我们讲完这个故事吧。
[Dialog]
[charslot]
桌案上摊开的册子中抄录了一场围绕水源而爆发的矛盾。
这是任何文明中都有的故事，常见，毫无新意。大长老伸出手，从书本下抽出另一本书来。
灰尘与壁炉中轻微的柴烟气息缠绕在一起，如同一团凝滞的琥珀。
[Dialog]
[PlaySound(key="$d_avg_paper2", volume=1)]
[delay(time=1)]
[charslot(slot="l",name="avg_174_slbell_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_1998_1#1$1",focus="r")]
[name="阿德颂"]“战士上下求索，寻找可以对抗怪物的方式。可即使是耶拉冈德，也无法为战士铲除那‘看不见的怪物’。”
[name="阿德颂"]“祂引领战士回到了那片冰封的湖面，对他说：‘别人看不到怪物，故而无从应对，你能看到它，也一定能看到击败它的方式。’”
[name="阿德颂"]“战士因此开悟，喀兰之心因此融化，春日因此驱散寒冬。”
[name="阿德颂"]“耶拉冈德赐予祂的子民最后的福祉，祂的泪水冻结了敌人，化为三座永恒的雪峰。”
[charslot(slot="l",name="avg_174_slbell_1#1$1",focus="l")]
[name="恩雅"]这是《耶拉冈德》中的筑家园篇的第一个故事，历代的学者对此都有各种各样的解读。
[name="恩雅"]故事里的“喀兰之心”指的应当就是如今的银心湖，也有学者认为这个聆听耶拉冈德神谕的战士实际上就是圣女的原型。
[name="恩雅"]“渡冰面而来的敌人”究竟是谁众说纷纭，至于故事里的“看不见的怪物”......
[charslot(slot="r",name="avg_npc_1998_1#1$1",focus="r")]
[name="阿德颂"]——“拉德索恩”。
[name="阿德颂"]一个意义不明确的读音，丢失了真实意思的词语。也是谢拉格最为出名的睡前故事之一。
[name="阿德颂"]当孩子们贪恋玩乐不肯入睡时，父母们总会讲起这个故事，而后将孩子塞回温暖的被褥中。
[name="阿德颂"]它的使用过于广泛，以至于大部分谢拉格人都忘了，“拉德索恩”并非一段咒文或是混乱中的胡言乱语，而是一个具有明确意义的词语。
[charslot(slot="l",name="avg_174_slbell_1#1$1",focus="l")]
[name="恩雅"]许多词都在漫长的历史中丢失了自己的意思。
[name="恩雅"]“拉德索恩”一度被推断为近千年前流入谢拉格的外来语，在来源这方面，它和“天灾”是一样的。
[charslot(slot="l",name="avg_174_slbell_1#10$1",focus="l")]
[name="恩雅"]如果我没记错的话，翻译已经涵义失传的外来语词汇正是您在藏经阁主导的课题......
[charslot(slot="r",name="avg_npc_1998_1#2$1",focus="r")]
[name="阿德颂"]很幸运

... (全文27015字符)
```

### level_act46side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g8_nobleroom",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_278_1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_278_1#1$1",focus="m")]
[name="佩尔罗契信使"]菈塔托丝大人，关于前天三家讨论的事，我家大人还有话想和您说。
[name="佩尔罗契信使"]佩尔罗契家对那些外来者的态度一贯是坚定的，对于那些没有信仰的人，再怎么警惕都不为过。
[name="佩尔罗契信使"]何况现在圣女出巡，谢拉格的政务暂时分归三家各自处理，这个时候我们更要多留一个心眼。
[name="佩尔罗契信使"]我们大人并不是觉得恩希欧迪斯是个坏人，但是希瓦艾什家确实和维多利亚人走得太近了，谁也说不准他还会有啥别的心思。
[name="佩尔罗契信使"]大人他相信您是尊重谢拉格传统的人，所以愿意和您沟通。要是您还有什么想法，我家大人也乐意和您当面聊聊。
[charslot(slot="m",name="avg_npc_253_1#7$1",focus="m")]
[name="菈塔托丝"]......都说完了？
[name="菈塔托丝"]好，看在你这么坦诚的分上，也替我原话转告阿克托斯。
[name="菈塔托丝"]我不知道阿克托斯是不是还因为天灾发生在佩尔罗契的领地而耿耿于怀，我也不在乎。
[name="菈塔托丝"]但是该讨论的问题上次会上已经有结论了，没有蔓珠院的指示，我们哪一家都不该轻举妄动。
[name="菈塔托丝"]现在圣女大人不在，我们各自照顾好自家的事，不要多生事端，就是对谢拉格最好的方式。
[charslot(slot="m",name="avg_npc_253_1#2$1",focus="m")]
[name="菈塔托丝"]就这样，送客。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="24_g8_nobleroom",screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_npc_253_1#1$1")]
[charslot(slot="r",name="avg_npc_2012_1#2$1")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_2012_1#2$1",focus="r")]
[name="维多利亚大使"]看上去，这样的麻烦在哪里都躲不过。
[charslot(slot="l",name="avg_npc_253_1#1$1",focus="l")]
[name="菈塔托丝"]让您见笑了，不过不必担忧，只是一些小麻烦。
[name="菈塔托丝"]还是让我们回到正题上吧——关于维多利亚几个高端服装品牌和布朗陶家的长期合作......
[charslot(slot="r",name="avg_npc_2012_1#1$1",focus="r")]
[name="维多利亚大使"]不......不不，尊敬的布朗陶夫人，我并不觉得这是一个可以忽视的问题。
[name="维多利亚大使"]如果谢拉格的人们普遍对维多利亚怀有这样的敌意，我们又该如何相信我们之间的合作能够长久呢？
[charslot(slot="l",name="avg_npc_253_1#1$1",focus="l")]
[name="菈塔托丝"]我们三大家族之间时有分歧，但是从来没有别人可以代表布朗陶家的态度，这一点您可以放心。
[charslot(slot="r",name="avg_npc_2012_1#2$1",focus="r")]
[name="维多利亚大使"]三大家族的矛盾......哈哈，作为一个维多利亚人，这样的局面也并不难理解。
[name="维多利亚大使"]留在谢拉格的这段时间，我一直试图了解这个国家，这里的文化陌生，但是有趣。
[name="维多利亚大使"]在我看来，虽然谢拉格团结在对耶拉冈德的信仰之下，但是同样的教义，似乎对不同的家族产生了截然不同的指导意义。
[name="维多利亚大使"]佩尔罗契家族勇敢，希瓦艾什家族精明，至于布朗陶家......抱歉，我很难用单一的词语表示赞赏。
[name="维多利亚大使"]如果一定要说的话，我认为布朗陶家是“高尚且值得信赖的”。
[charslot(slot="l",name="avg_npc_253_1#4$1",focus="l")]
[name="菈塔托丝"]......也真难为你们还要做这样的功课。
[charslot(slot="r",name="avg_npc_2012_1#1$1",focus="r")]
[name="维多利亚大使"]当然，充分的了解是合作的前提。
[name="维多利亚大使"]公爵大人十分看重与谢拉格的合作，而她也一直在寻找一位可靠的，可以代表谢拉格的合作对象。
[charslot(slot="l",name="avg_npc_253_1#5$1",focus="l")]
[name="菈塔托丝"]可以代表谢拉格的合作对象？难道是公爵大人和喀兰贸易合作不愉快了？
[charslot(slot="r",name="avg_npc_2012_1#1$1",focus="r")]
[name="维多利亚大使"]恩希欧迪斯先生是一位无比聪明的商人，但这也是他的缺点所在。在他的生意场中，他绝对不允许出现除他以外的赢家。
[name="维多利亚大使"]我想您作为他的邻居，应该很清楚这一点。
[charslot(slot="l",name="avg_npc_253_1#1$1",focus="l")]
[name="菈塔托丝"]呵......还真是精准的概括。
[charslot(slot="r",name="avg_npc_2012_1#1$1",focus="r")]
[name="维多利亚大使"]问题就在这里，三大家族名义上是耶拉冈德平等的子民，可是在我一个纯粹的旁观者眼中，却完全不这样觉得。
[name="维多利亚大使"]恕我直言，就连我这个外人都看得出来，这场天灾当中，您的家族与佩尔罗契家族几乎无法做出任何有效决策。
[name="维多利亚大使"]希瓦艾什家的喀兰贸易不仅垄断了几乎所有谢拉格的外贸生意，更是在政治层面主导了谢拉格所有的对外交流。
[name="维多利亚大使"]而理论上谢拉格真正的掌权者，圣女大人——也就是恩希欧迪斯先生的胞妹，她似乎对这样的现状没有任何意见。
[charslot(slot="l",name="avg_npc_253_1#5$1",focus="l")]
[name="菈塔托丝"]注意你的言辞，先生。不要用你的偏见揣测谢拉格圣女的虔诚，这是极度的不敬。
[charslot(slot="r",name="avg_npc_2012_1#1$1",focus="r")]
[name="维多利亚大使"]哦抱歉，如果我的坦诚冒犯了您，我为此道歉。请相信我绝对没有恶意。如我刚才所说，这一切都只是一个外来者观察到的现象。
[charslot(slot="l",name="avg_npc_253_1#5$1",focus="l")]
[name="菈塔托丝"]好了，就请直接说明吧——您到底有什么提议？
[charslot(slot="r",name="avg_npc_2012_1#2$1",focus="r")]
[name="维多利亚大使"]很简单，维多利亚在寻求一种友好且平等，真正互利互惠的合作。
[name="维多利亚大使"]不只有某一方获利，也不受限于狭隘的民族观念。展开高效而长远的合作。
[name="维多利亚大使"]而布朗陶家族以及您个人，也是受到公爵阁下青睐的，我出现在这里即是证明。
[charslot(slot="l",name="avg_npc_253_1#1$1",focus="l")]
[name="菈塔托丝"]布朗陶家不会认为任何外人的看法具有价值。你们的承诺，恰好证明维多利亚的立场飘忽不定。
[name="菈塔托丝"]如果在你们眼中布朗陶不过是另一个更好操纵的希瓦艾什，那就大错特错了。
[charslot(slot="r",name="avg_npc_2012_1#1$1",focus="r")]
[name="维多利亚大使"]不不，菈塔托丝大人，完全不。
[name="维多利亚大使"]维多利亚并非青睐顺从者，也不图他人攀附，而是做正确的事。
[name="维多利亚大使"]希瓦艾什只是一扇时开时关的窗户，房间里有什么，还是身处其中的人最清楚。
[name="维多利亚大使"]请告诉我，布朗陶夫人，您是否厌倦了这片土地上无休止且毫无意义的族群矛盾？
[charslot(slot="r",name="avg_npc_2012_1#2$1",focus="r")]
[name="维多利亚大使"]或者说......您是否期待，由自己来引领一个全新的谢拉格？
[charslot(slot="l",name="avg_npc_253_1#4$1",focus="l")]
[name="菈塔托丝"]......
[charslot(slot="l",name="avg_npc_253_1#2$1",focus="l")]
[name="菈塔托丝"]好了，就到这里吧。
[charslot(slot="l",name="avg_npc_253_1#5$1",focus="l")]
[name="菈塔托丝"]感谢您今晚的光顾，我充分理解了你们的提议——我也有话要您带给你们的公爵大人。
[name="菈塔托丝"]她还不够了解谢拉格，但我发自内心地希望她了解。
[charslot(slot="r",name="avg_npc_2012_1#1$1",focus="r")]
[name="维多利亚大使"]明白了，布朗陶夫人。虽然很遗憾，不过在这些政治问题得到解决之前，我们之间的商务合作恐怕是要暂缓了。
[name="维多利亚大使"]不过也无妨，对于您这位重要的合作伙伴，我们还是有着充足的耐心的。
[name="维多利亚大使"]我们永远期待您的回复。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="24_g10_manorhouse",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[playsound(key="$d_avg_paper2")]
[Delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Sticker(id="st1", multi = true, text="亲爱的恩希亚，展信佳。", x=180,y=170, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n你看到这封信的时候，应该已经知道了我的决定。",block = true)]
[Sticker(id="st1", multi = true, text="\n不用担心，就当作姐姐只是出一趟远门，用不了多久就会回来了。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="答应带你去蔓珠院后厨偷吃奶酪火锅的计划，可能又要延迟了，不过等我回来的时候，我一定兑现承诺，我保证。", x=180,y=170, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n也不用替恩希欧迪斯担心，他有自己的安排，只是这段时间可能会格外繁忙一点，就要拜托你一个人看家啦。",block = true)]
[Sticker(id="st1", multi = true, text="\n最近发生了许多事，你一定要保护好自己，出门时千万要谨慎。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", 

... (全文18423字符)
```

### level_act46side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g5_guestroom",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[PlayMusic(key="$saferoom_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_2010_1#1$1",duration=0.7)]
[charslot(slot="l",name="avg_4211_snhunt_1#1$2",duration=0.7)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_2010_1#1$1",focus="r")]
[name="恩雅"]这里是......
[charslot(slot="l",name="avg_4211_snhunt_1#1$2",focus="l")]
[name="小猎手"]我家。
[name="小猎手"]最后看到的那些人走了相反的方向，这里很安全。等处理完你的伤口，你就立马离开。
[charslot(slot="r",name="avg_npc_2010_1#1$1",focus="r")]
[name="恩雅"]......谢谢，我——
[Dialog]
[charslot(slot="r",name="avg_npc_2010_1#12$1",focus="r")]
[charslot(slot = "r", action="shake",random=true, power=5, times=30,duration=0.5)]
[delay(time=1)]
[charslot(slot="l",name="avg_4211_snhunt_1#1$2",focus="l")]
[name="小猎手"]少说话，也别乱动，希瓦艾什。
[name="小猎手"]......
[charslot(slot="l",name="avg_4211_snhunt_1#10$2",focus="l")]
[name="小猎手"]外衣还算厚，距离又远，伤口不是很深。
[name="小猎手"]......不过他们用的箭有一个小倒钩，拔的时候会很疼，我尽量稳着来。
[Dialog]
[charslot]
年轻的猎手将箭杆折断一截，她捏紧剩余的部分，目光瞟向伤者，而对方只是轻轻点头，没有流露出一丝恐慌。
猎手深深呼吸，缓缓地拔出箭镞，倒钩牵动肉体的触感让她也不禁冷汗直流。
她竭尽全力地让双手稳定，直至箭镞完全从对方的身上分离。
[Dialog]
[charslot(slot="l",name="avg_4211_snhunt_1#7$2",focus="l")]
[charslot(slot="r",name="avg_npc_2010_1#12$1",focus="l")]
[name="小猎手"]呼——呼——总算......
[charslot(slot="r",name="avg_npc_2010_1#12$1",focus="r")]
[name="恩雅"]非常......感谢......
[charslot(slot="l",name="avg_4211_snhunt_1#1$2",focus="l")]
[name="小猎手"]还没弄好，你再忍忍。
[Dialog]
[PlaySound(key="$d_avg_clothtrailground", volume=1)]
[Delay(time=1)]
紧接着她从腰包里掏出一包药粉，挽起恩雅的裙摆，熟练地抹匀在她的伤口上，又拿出一根布条将那里紧紧包扎起来。
[charslot(slot="l",name="avg_4211_snhunt_1#1$2",focus="l")]
[name="小猎手"]你疼的话可以叫出来，我不会笑话你。
[charslot(slot="r",name="avg_npc_2010_1#12$1",focus="r")]
[name="恩雅"]我不想让你更加紧张。
[charslot(slot="r",name="avg_npc_2010_1#1$1",focus="r")]
[name="恩雅"]万一手抖了，我自己也不好受。
[charslot(slot="l",name="avg_4211_snhunt_1#1$2",focus="l")]
[name="小猎手"]嘁。
[charslot(slot="l",name="avg_4211_snhunt_1#5$2",focus="l")]
[name="小猎手"]......嗯？
[Dialog]
[charslot(slot = "m", name = "avg_4211_snhunt_1#5$1",posfrom = "-200,0", posto = "-200,0",duration=1.5,isCopy=true)]
[delay(time=2)]
一只雪白的小云兽从猎手的兜帽中探出细长的身体，双爪扒着猎手的发辫，湿润的鼻头在恩雅的毛领边微微颤动。
随后，它伸着脑袋嗅闻着陌生人的气味。
[charslot(slot="l",name="avg_4211_snhunt_1#1$1",focus="l",isCopy=true)]
[charslot(slot="r",name="avg_npc_2010_1#3$1",focus="l")]
[name="小猎手"]别碰它，它很讨厌生人。
[charslot(slot="l",name="avg_4211_snhunt_1#1$1",focus="n",isCopy=true)]
不等猎手说完，恩雅的手指已经轻轻揉上了小云兽的下巴。仅仅是抚摸到它柔软的皮毛，仿佛内心在严寒下也能升起一丝暖意。
[charslot(slot="l",name="avg_4211_snhunt_1#8$1",focus="l",isCopy=true)]
[name="小猎手"]（压低声音）裂云兽，快回去......
[charslot(slot="r",name="avg_npc_2010_1#3$1",focus="r")]
[name="恩雅"]这个小家伙......叫“裂云兽”吗？
[name="恩雅"]不过，我还不知道你的名字呢，我的救星大人。
[charslot(slot="l",name="avg_4211_snhunt_1#4$1",focus="l",isCopy=true)]
[name="小猎手"]......
[charslot(slot="l",name="avg_4211_snhunt_1#1$1",focus="l",isCopy=true)]
[name="小猎手"]茱安娜。
[name="茱安娜"]我可不想知道你叫什么，希瓦艾什。你最好别以为我是你的朋友。
[charslot(slot="r",name="avg_npc_2010_1#2$1",focus="r")]
[name="恩雅"]为什么？你对我很好啊。
[charslot(slot="l",name="avg_4211_snhunt_1#8$1",focus="l",isCopy=true)]
[name="茱安娜"]那你们又是怎么对我的！
[charslot(slot="l",name="avg_4211_snhunt_1#1$1",focus="l",isCopy=true)]
[name="小猎手"]哼......跟你也没关系，不说了。
[charslot(slot="r",name="avg_npc_2010_1#2$1",focus="r")]
[name="恩雅"]“你们”的意思，是指希瓦艾什家吗？
[name="恩雅"]或者，你在说恩希欧迪斯......
[charslot(slot="l",name="avg_4211_snhunt_1#8$1",focus="l",isCopy=true)]
[name="茱安娜"]不止他一个。
[name="茱安娜"]我父亲说，从恩希欧迪斯的父亲开始，希瓦艾什就痴迷于亵渎耶拉冈德。
[name="茱安娜"]他把沥青浇淋在耶拉冈德的脊骨，把毒水倾倒在耶拉冈德的尾巴，他的贪婪也为自己带来了毁灭。
[charslot(slot="r",name="avg_npc_2010_1#12$1",focus="r")]
[name="恩雅"]......
[charslot(slot="l",name="avg_4211_snhunt_1#8$1",focus="l",isCopy=true)]
[name="茱安娜"]结果现在，这个恩希欧迪斯压根没有吸取教训，他变本加厉地搅扰耶拉冈德的安宁。
[name="茱安娜"]但他最重的罪孽，是他竟敢在耶拉冈德的血肉上开了个大洞。这一次的灾祸，不就是希瓦艾什惹怒了耶拉冈德的证明？
[charslot(slot="r",name="avg_npc_2010_1#12$1",focus="r")]
[name="恩雅"]可是......谢拉格人不可能永远困在雪山。
[name="恩雅"]工业和商业不是真的让我们过上更好的生活了吗？慈悲的耶拉冈德怎么会因为我们过上了好日子而惩罚我们呢？
[charslot(slot="l",name="avg_4211_snhunt_1#8$1",focus="l",isCopy=true)]
[name="茱安娜"]更好的生活？
[name="茱安娜"]你们希瓦艾什能有这副鬼样，天天躲在温暖的壁炉边吃香喝辣......
[charslot(slot="l",name="avg_4211_snhunt_1#8$1",focus="l",isCopy=true)]
[multiline(name="茱安娜")]靠的......
[charslot(slot="l",name="avg_4211_snhunt_1#6$1",focus="l",isCopy=true)]
[multiline(name="茱安娜")]就是把我们变成代价！
[charslot(slot="l",name="avg_4211_snhunt_1#11$1",focus="l",isCopy=true)]
[name="茱安娜"]在我小时候，雪山脚下还栖息着许多兽群。
[name="茱安娜"]它们以山川为给养，到溪流边饮用清水，回山林里啃食草木与浆果，如此度过千年，从未改变。
[name="茱安娜"]但是喀兰贸易却把铁轨一路修到这里，硬生生把山川分割开来，逼着野兽冒死来回跨过铁轨才能生存。
[charslot(slot="l",name="avg_4211_snhunt_1#8$1",focus="l",isCopy=true)]
[name="茱安娜"]偶尔列车撞死了它们，你们竟还抱怨是它们不长眼睛。
[name="茱安娜"]兽群们只能往更高的地方迁居，可山上的土地根本不够养活数量那么庞大的族群，它们互相争斗、撕咬，能活下来的越来越少。
[name="茱安娜"]更别说还有许多对列车噪音敏感的云兽......这其中有多少生灵逝去，我又是怎么收养到了裂云兽，你根本不会明白！
[charslot(slot="r",name="avg_npc_2010_1#12$1",focus="r")]
[name="恩雅"]......可是，山脚下的农民们，需要那些列车送来的肥料与种子，山上的病人，也需要那些药物。
[charslot(slot="l",name="avg_4211_snhunt_1#8$1",focus="l",isCopy=true)]
[name="茱安娜"]那耶拉冈德赐予我们的富足的猎获又在哪里呢？
[name="茱安娜"]每年我们打到的猎物，都比过去一年更少，连泉水也不再像以往那么清甜。
[name="茱安娜"]我们家族遵循着耶拉冈德神圣的教诲，世世代代在山上以狩猎谋生，为此还会雕刻圣像以表敬爱。
[charslot(slot="l",name="avg_4211_snhunt_1#11$1",focus="l",isCopy=true)]
[name="茱安娜"]父亲......还有我，甚至弟弟妹妹，也向来虔心祈祷，不敢对耶拉冈德轻慢一次。
[charslot(slot="l",name="avg_4211_snhunt_1#6$1",focus="l",isCopy=true)]
[name="茱安娜"]凭什么成为“代价”的是我们？！
[Dialog]
[charslot]
突然的喊声让裂云兽有些惊怕，它从浑身发抖的茱安娜身上跃下，徘徊在恩雅的脚边。
恩雅俯身抱起裂云兽，将它送回茱安娜的肩上。
[Dialog]
[charslot(slot="l",name="avg_4211_snhunt_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_2010_1#1$1",focus="l")]
[name="茱安娜"]......别再这么乱动了，伤口容易崩开。
[charslot(slot="r",name="avg_npc_2010_1#1$1",focus="r")]
[name="恩雅"]其实......你说的这些，我都是第一次听到。
[charslot(slot="l",name="avg_4211_snhunt_1#8$1",focus="l")]
[name="茱安娜"]我知道你想反驳什么，尽管说吧，希瓦艾什。
[charslot(slot="r",name="avg_

... (全文17595字符)
```

### level_act46side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g8_nobleroom",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[PlaySound(key="$doorknockquite", volume=1,channel="kc")]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_253_1#7$1",focus="m")]
[name="菈塔托丝"]烦死了！不是和你们说过今天别再打扰我了吗？
[name="菈塔托丝"]是谁在——
[Dialog]
[charslot]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_262_1#5$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_262_1#5$1",focus="m")]
[name="休露丝"]......姐姐。
[charslot(slot="m",name="avg_npc_253_1#4$1",focus="m")]
[name="菈塔托丝"]你怎么来了......
[charslot(slot="m",name="avg_npc_253_1#5$1",focus="m")]
[name="菈塔托丝"]快坐下，怎么了，睡不着吗？
[name="菈塔托丝"]尤卡坦怎么搞的，明明叫他盯好你——
[charslot(slot="m",name="avg_npc_262_1#5$1",focus="m")]
[name="休露丝"]不......
[Dialog]
她摇了摇头。
[charslot(slot="m",name="avg_npc_262_1#5$1",focus="m")]
[name="休露丝"]不，是我不让尤卡坦跟来的。
[name="休露丝"]我想单独和你谈谈。
[charslot(slot="m",name="avg_npc_253_1#4$1",focus="m")]
[name="菈塔托丝"]......
[charslot(slot="m",name="avg_npc_253_1#4$1",focus="n")]
菈塔托丝从未想过，会在这个直率开朗的妹妹脸上看到这样的神色。
[charslot(slot="m",name="avg_npc_253_1#5$1",focus="m")]
[name="菈塔托丝"]好吧，不过只能一会，然后就去乖乖睡觉。
[name="菈塔托丝"]真是......都是当妈妈的人了，怎么还像个小孩一样。
[charslot(slot="m",name="avg_npc_262_1#5$1",focus="m")]
[name="休露丝"]我今天，听到了阿克托斯在客厅里大吼大叫......
[charslot(slot="m",name="avg_npc_253_1#5$1",focus="m")]
[multiline(name="菈塔托丝")]还是吵到你了？
[charslot(slot="m",name="avg_npc_253_1#9$1",focus="m")]
[multiline(name="菈塔托丝")]该死的，回头必须找他算账......
[charslot(slot="m",name="avg_npc_262_1#5$1",focus="m")]
[name="休露丝"]不......不是......
[name="休露丝"]我听到了你们争论的事，我也知道这段时间，谢拉格发生了很多糟糕的事......
[name="休露丝"]菈塔......我请求你。如果你知道些什么，一定、一定要告诉我。
[charslot(slot="m",name="avg_npc_253_1#2$1",focus="m")]
[name="菈塔托丝"]耶拉冈德在上......
[charslot(slot="m",name="avg_npc_253_1#10$1",focus="m")]
[name="菈塔托丝"]休露丝，这些都不是你现在应该操心的事。
[name="菈塔托丝"]放心吧，等你以后接过这一大摊子事了，有的是要你操心的机会呢。
[charslot(slot="m",name="avg_npc_262_1#6$1",focus="m")]
[name="休露丝"]可是，最近的变故一件接着一件，就算我一直待在房间里，也能感觉到一切都在变得很糟......
[name="休露丝"]每天都能在窗户外面看见愁眉不展的人，还有莫希她，到现在还是一点消息都没有......
[charslot(slot="m",name="avg_npc_253_1#9$1",focus="m")]
[name="菈塔托丝"]我还在派人寻找她的下落......我相信她不会有事的，别忘了，她现在可是布朗陶家最厉害的战士之一。
[charslot(slot="m",name="avg_npc_262_1#6$1",focus="m")]
[name="休露丝"]我当然知道......
[name="休露丝"]可我更担心的是你，菈塔。
[charslot(slot="m",name="avg_npc_253_1#5$1",focus="m")]
[name="菈塔托丝"]......
[charslot(slot="m",name="avg_npc_262_1#5$1",focus="m")]
[name="休露丝"]虽然以前我也不太能帮上你的什么忙，但至少还能站在你身边，给你一点支持......
[name="休露丝"]可是现在，只有你一个人应付这一切......菈塔，我还是希望你能多和我说说话。
[name="休露丝"]你不用一个人坚持什么，我和尤卡坦，在任何时候都一定会支持你的。
[charslot(slot="m",name="avg_npc_253_1#10$1",focus="m")]
[name="菈塔托丝"]......你想的太多了，我的傻瓜妹妹。你是在怀疑我当不好这个家主，想要早点接班了？
[charslot(slot="m",name="avg_npc_262_1#5$1",focus="m")]
[name="休露丝"]我不是——
[charslot(slot="m",name="avg_npc_253_1#10$1",focus="m")]
[name="菈塔托丝"]我向你发誓，休露丝。
[name="菈塔托丝"]我会保护好你，还有尤卡坦，以及整个布朗陶家。
[name="菈塔托丝"]就算豁出命去，我也一定会做到。
[name="菈塔托丝"]耶拉冈德见证，绝不食言。
[charslot(slot="m",name="avg_npc_262_1#6$1",focus="m")]
[name="休露丝"]......
[charslot(slot="m",name="avg_npc_253_1#10$1",focus="m")]
[name="菈塔托丝"]怎么，你就算不信我，还能不信耶拉冈德吗？
[charslot(slot="m",name="avg_npc_262_1#5$1",focus="m")]
[name="休露丝"]没必要把话说得那么重......
[charslot(slot="m",name="avg_npc_253_1#10$1",focus="m")]
[name="菈塔托丝"]好......那你答应我，现在就去休息。
[name="菈塔托丝"]放心吧，明天一定会比今天更好......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="45_g7_lakescenery_n",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_253_1#7$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_2012_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_2012_1#1$1",focus="r")]
[name="维多利亚大使"]我很荣幸收到您的邀请，尊敬的布朗陶夫人。
[name="维多利亚大使"]您这个时候主动约见我，想必是改变主意了？
[charslot(slot="l",name="avg_npc_253_1#7$1",focus="l")]
[name="菈塔托丝"]......少说废话。
[name="菈塔托丝"]对希瓦艾什家和佩尔罗契家的人发起刺杀，离间三族关系，这就是你们逼迫我与你们合作的方式？
[charslot(slot="l",name="avg_npc_253_1#2$1",focus="l")]
[name="菈塔托丝"]呵，我原本以为维多利亚的政治家至少会用点更聪明的手段。
[Dialog]
[charslot(slot="r",name="avg_npc_2012_1#2$1",focus="r")]
[delay(time=1)]
男人不置可否地笑了笑。
[charslot(slot="r",name="avg_npc_2012_1#2$1",focus="r")]
[name="维多利亚大使"]布朗陶夫人，我不明白您为何会这样想。
[name="维多利亚大使"]在别国境内对其领导人发起刺杀，这可是毫无疑问的宣战行为......如果被证实的话。
[name="维多利亚大使"]您确定要对维多利亚发起这样的指控吗？
[charslot(slot="l",name="avg_npc_253_1#2$1",focus="l")]
[name="菈塔托丝"]......这就是你们有恃无恐的理由。
[charslot(slot="r",name="avg_npc_2012_1#2$1",focus="r")]
[name="维多利亚大使"]尊敬的夫人，恐怕我还是不明白您的意思。
[name="维多利亚大使"]不过既然您今天选择与我见面，那我十分乐意听您讲讲——有什么是我可以为您效劳的？
[charslot(slot="l",name="avg_npc_253_1#2$1",focus="l")]
[name="菈塔托丝"]......哼，得意吧，你们粗糙的计谋还是达成了目的，起码佩尔罗契和布朗陶的关系已经彻底破裂，在其他人眼里我也戴上了可疑的帽子。
[charslot(slot="l",name="avg_npc_253_1#9$1",focus="l")]
[name="菈塔托丝"]至于恩希欧迪斯......那套什么三家都想要稳定的话术，就是临时编出来骗骗阿克托斯那个傻子的。
[name="菈塔托丝"]他心里清楚得很，以谢拉格的现状，一旦某家领袖“意外”遇害，只要有人稍微挑拨，失去最后希望的本地领民们肯定会一哄而散。
[name="菈塔托丝"]万一我们见面的事被他知道了，就算他清楚我没有答应你们任何事情，也会毫不犹豫带着佩尔罗契向我发难。
[name="菈塔托丝"]毕竟现在的谢拉格，急缺一位能担负所有的“罪人”。
[name="菈塔托丝"]以他的手腕，最坏的下场，就是布朗陶家从此断绝于谢拉格。
[charslot(slot="l",name="avg_npc_253_1#5$1",focus="l")]
[name="菈塔托丝"]......我的时间不多了。
[charslot(slot="r",name="avg_npc_2012_1#2$1",focus="r")]
[name="维多利亚大使"]我很同情您的处境，夫人。我也认为您对局势的分析一点不差。
[name="维多利亚大使"]那么，您是否有意打破这样的局面呢？
[charslot(slot="l",name="avg_npc_253_1#7$1",focus="l")]
[name="菈塔托丝"]......
[name="菈塔托丝"]......那我们就别废话了。
[name="菈塔托丝"]首先，我要你们绝对的承诺——不管在任何情况下，都要优先保证布朗陶家的安全，还有领民的安全。
[charslot(slot="r",name="avg_npc_2012_1#1$1",focus="r")]
[name="维多利亚大使"]当然，我们素来同情被希瓦艾什边缘化的普通本地民众，这是我们推进与谢拉格和平合作的初心之一。
[charslot(slot="l",name="avg_npc_2

... (全文18553字符)
```

### level_act46side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g4_luxurywarminterior",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_254_1#5$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_260_1#7$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_254_1#5$1",focus="l")]
[name="阿克托斯"]古罗，头上纱布还没揭，怎么就回来了？
[charslot(slot="l",name="avg_npc_254_1#7$1",focus="l")]
[name="阿克托斯"]总是这么鲁莽，说了多少遍了，行动之前要三思！你现在就给我回去医院好好躺着。
[charslot(slot="r",name="avg_npc_260_1#1$1",focus="r")]
[name="古罗"]老爷......我是听说您要应布朗陶家的约去和菈塔托丝谈判。
[name="古罗"]老爷，您千万不能去......
[charslot(slot="l",name="avg_npc_254_1#7$1",focus="l")]
[name="阿克托斯"]怎么，我还怕她不成？
[name="阿克托斯"]菈塔托丝那个毒女人说要跟我挑明真相，我倒要看看她嘴巴里能吐出什么货色。
[charslot(slot="r",name="avg_npc_260_1#1$1",focus="r")]
[name="古罗"]可是老爷......布朗陶把约见的地方选在了自家领地，明摆着就是有阴谋。
[charslot(slot="l",name="avg_npc_254_1#7$1",focus="l")]
[name="阿克托斯"]哼，你以为我什么都不知道吗？
[name="阿克托斯"]就算她真敢动手，我佩尔罗契家何时忌惮过任何一场战斗？
[name="阿克托斯"]就算是她的地盘，我佩尔罗契家就无计可施？
[name="阿克托斯"]倒是你小子，不来倒好，来了，我看到你的那个头就来气。
[charslot(slot="r",name="avg_npc_260_1#6$1",focus="r")]
[name="古罗"]老爷生气我也得劝老爷！我就坐在门口，不走了。
[charslot(slot="l",name="avg_npc_254_1#7$1",focus="l")]
[name="阿克托斯"]跟你有什么关系？
[charslot(slot="r",name="avg_npc_260_1#6$1",focus="r")]
[name="古罗"]属下没本事，自己伤成这副模样，没办法保护老爷，只能让老爷别去冒险。
[charslot(slot="l",name="avg_npc_254_1#2$1",focus="l")]
[name="阿克托斯"]哎......！我说的生气不是生你的气，是布朗陶那帮杂碎。
[charslot(slot="l",name="avg_npc_254_1#7$1",focus="l")]
[name="阿克托斯"]放心，古罗，我这就帮你去找他们算账。我会让他们知道，没人能欺负到佩尔罗契家头上！
[name="阿克托斯"]古罗，是我佩尔罗契家的兄弟，你就让开。
[charslot(slot="r",name="avg_npc_260_1#1$1",focus="r")]
[name="古罗"]老爷......
[charslot(slot="l",name="avg_npc_254_1#1$1",focus="l")]
[name="阿克托斯"]来人，送古罗将军回房间。
[Dialog]
[charslot(slot="r",name="avg_npc_260_1#1$1",focus="r")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_openftstpwalk", volume=1, loop=true, channel="o")]
[StopSound(channel="o", fadetime=3)]
[charslot(slot="r",afrom=1,ato=0,duration=1,focus="r")]
[Delay(time=1.5)]
几个士兵搀扶着古罗，把他扶回了房间里。
[charslot(slot="l",name="avg_npc_254_1#9$1",focus="l")]
[name="阿克托斯"]哼......
[name="阿克托斯"]不怕归不怕，还是要做好准备，得多带点人过去。
[charslot(slot="l",name="avg_npc_254_1#1$1",focus="l")]
[name="阿克托斯"]*谢拉格俚语*，儿郎们，多备几辆车。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="24_g8_nobleroom",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_270_1#1$1",focus="m")]
[name="布朗陶管家"]休露丝夫人，晚餐已经准备好了。
[charslot(slot="m",name="avg_npc_262_1#1$1",focus="m")]
[name="休露丝"]大夫人呢？不一起吃饭吗？
[charslot(slot="m",name="avg_npc_270_1#1$1",focus="m")]
[name="布朗陶管家"]菈塔托丝夫人刚刚离家了，让二位不要过分担心。
[charslot(slot="m",name="avg_npc_263_1#7$1",focus="m")]
[name="尤卡坦"]我记得大夫人说过今天要和佩尔罗契家谈判，可是这个时间也太早了......
[charslot(slot="m",name="avg_npc_263_1#3$1",focus="m")]
[name="尤卡坦"]她是自己一个人去的吗？
[charslot(slot="m",name="avg_npc_270_1#1$1",focus="m")]
[name="布朗陶管家"]我们不清楚......
[charslot(slot="m",name="avg_npc_262_1#5$1",focus="m")]
[name="休露丝"]......尤卡坦，我总觉得不对劲。
[name="休露丝"]你去找她。
[charslot(slot="m",name="avg_npc_263_1#3$1",focus="m")]
[name="尤卡坦"]嗯......
[charslot(slot="m",name="avg_npc_270_1#1$1",focus="m")]
[name="布朗陶管家"]休露丝夫人，尤卡坦老爷，请等一下......
[charslot(slot="m",name="avg_npc_262_1#4$1",focus="m")]
[name="休露丝"]又怎么了？
[charslot(slot="m",name="avg_npc_270_1#1$1",focus="m")]
[name="布朗陶管家"]大夫人离开家以前，给我留下最后的命令是......
[name="布朗陶管家"]今天晚上，绝对不可以让二位离开家。
[name="布朗陶管家"]不管用什么办法......
[charslot(slot="m",name="avg_npc_263_1#2$1",focus="m")]
[name="尤卡坦"]......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="24_g5_guestroom",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_4211_snhunt_1#8$1",focus="m")]
[name="茱安娜"]圣女大人！趴下！
[Dialog]
[charslot]
[playsound(key="$d_avg_crossbow_door",volume=1)]
[playsound(key="$glass",volume=0.6,delay=1)]
[CameraShake(duration=1.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.7, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_4211_snhunt_1#6$1",focus="m")]
[name="茱安娜"]该死......这些到底是什么人？
[name="茱安娜"]在谢拉格的土地上，竟然想谋害圣女？
[charslot(slot="m",name="avg_npc_2010_1#11$1",focus="m")]
[name="恩雅"]也许不是谢拉格人......
[name="恩雅"]他们很危险......
[charslot(slot="m",name="avg_4211_snhunt_1#6$1",focus="m")]
[name="茱安娜"]放心圣女大人！我拼了命也会保护好你的！
[name="茱安娜"]他们想进来也没那么容易......瞧瞧谢拉格猎人的本事吧！
[Dialog]
[PlaySound(key="$d_avg_bowstring_tightened", volume=1)]
[delay(time=1)]
小猎手拿起重弩，熟练地拉弦搭箭，从破碎的窗户探出身去，几乎没有瞄准便扣动扳机。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_bowstring_rebound", volume=1)]
[PlaySound(key="$d_avg_arrowshot", volume=1,delay=0.3)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
屋外立即传来几声惨叫。
[charslot(slot="m",name="avg_4211_snhunt_1#8$1",focus="m")]
[name="茱安娜"]......命中。
[Dialog]
[charslot]
[playsound(key="$d_avg_crossbow_door",volume=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255,g=255, b=255, fadet

... (全文24345字符)
```

### level_act46side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="67_G3_rhineobservatory_i",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>谢拉格-莱茵生命观测站 </><p=2>1101年12月7日</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
谢拉格天灾发生前三十三小时
[dialog]
[charslot(slot="m",name="avg_1047_halo2_1#14$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_1047_halo2_1#14$1",focus="m")]
[name="埃琳娜"]仪器正常，终端电量充足，笔芯和稿纸充足......还有足够的咖啡，好！
[charslot(slot="m",name="avg_1047_halo2_1#15$1",focus="m")]
[multiline(name="埃琳娜")]熟悉的通宵之夜就要开始啦——
[charslot(slot="m",name="avg_1047_halo2_1#15$1",focus="n")]
[PlaySound(key="$d_avg_scroll", volume=1)]
[delay(time=1)]
[charslot(slot="m",name="avg_1047_halo2_1#4$1",focus="m")]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="埃琳娜")]哇啊啊！
[dialog]
[charslot]
埃琳娜被房间角落里传来的窸窸窣窣的声音吓了一跳，她这才发现即使在这个时间自己也不是观测间唯一的使用者。
[dialog]
[PlaySound(key="$d_avg_rollpaper", volume=0.6)]
[delay(time=1)]
接着，仪器旁边成堆的废稿纸里爬出了一个人。
[dialog]
[charslot(slot="m",name="avg_npc_1999_1#3$1",duration=1)]
[delay(time=2)]
[charslot]
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="l")]
[charslot(slot="r",name="avg_1047_halo2_1#4$1",focus="l")]
[name="卡罗琳"]哦......埃琳娜，是你啊。
[name="卡罗琳"]（哈欠）......我说这个点是有哪个想追求麦克斯奖的大科学家还在工作呢......
[charslot(slot="r",name="avg_1047_halo2_1#4$1",focus="r")]
[name="埃琳娜"]你......你是卡罗琳前辈？！
[name="埃琳娜"]您竟然，还记得我？
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="l")]
[name="卡罗琳"]能量科最年轻的明星研究员，不要太小看自己的名气了。
[charslot(slot="r",name="avg_1047_halo2_1#1$1",focus="r")]
[name="埃琳娜"]您过奖了......
[name="埃琳娜"]我以为您已经回去了，我看排期表上今天应该是我来记录观测才对——
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="l")]
[name="卡罗琳"]算了吧，项目进度什么时候跟着排期表走过——不然我也不会在这里住了半个月了。
[charslot(slot="r",name="avg_1047_halo2_1#2$1",focus="r")]
[multiline(name="埃琳娜")]怪不得来观测站以后，都没见过您几次......
[charslot(slot="r",name="avg_1047_halo2_1#1$1",focus="r")]
[multiline(name="埃琳娜")]辛苦了。
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="l")]
[name="卡罗琳"]回来的感觉怎么样？
[charslot(slot="r",name="avg_1047_halo2_1#17$1",focus="r")]
[name="埃琳娜"]您是说......？
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="l")]
[name="卡罗琳"]再次回到莱茵生命。
[name="卡罗琳"]虽然这次观测站项目开始组织人手的时候，我第一个就想到了你，但我本来以为，你会拒绝的。
[charslot(slot="r",name="avg_1047_halo2_1#2$1",focus="r")]
[name="埃琳娜"]......说实话，我也犹豫过。
[charslot(slot="r",name="avg_1047_halo2_1#17$1",focus="r")]
[name="埃琳娜"]不管怎么说，莱茵生命曾经给了我很珍贵的机会，而且，我从来都没有怀疑过，莱茵生命本身是个很伟大的科技公司。
[name="埃琳娜"]我至今还是觉得，在莱茵学习的那段时间，是我离自己的梦想最近的时候。
[name="埃琳娜"]而且我也得承认......哪怕是斐尔迪南，在科研领域，他的才华确实让人羡慕。
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="l")]
[name="卡罗琳"]是啊，他是长了一个好用的物理脑子，那就让他去做他适合做的事吧。
[name="卡罗琳"]反正从特区监狱里出来以后，他就一门心思扑在了他的研究上，也没空去欺负别的研究员了。
[name="卡罗琳"]我看能量科主任这个位置用不了多久就该变动一下了......小埃琳娜，加油哦。
[charslot(slot="r",name="avg_1047_halo2_1#4$1",focus="r")]
[name="埃琳娜"]不不！那太夸张了——
[charslot(slot="r",name="avg_1047_halo2_1#17$1",focus="r")]
[name="埃琳娜"]我只是想，来仔细看看......
[dialog]
[charslot(fadetime=0.5)]
[delay(time=0.7)]
[Image(image="cg_moonmasked", screenadapt="coverall", fadetime=2.5,block=true)]
[delay(time=1)]
[charslot]
埃琳娜下意识地仰起头，透过观测站透明的穹顶，她看到了被风雪遮蔽的天空。
她讨厌这样的感觉。
就像她讨厌家族里那些古旧的传统与认知，那些曾经阻挡在她面前的一切与科学本身无关的阻碍。
她相信科学理应在纯粹的环境里不断突破，解开人们对于这片大地的每一个疑问......
[dialog]
[Image(fadetime=1.5, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="r")]
[charslot(slot="r",name="avg_1047_halo2_1#17$1",focus="r")]
[name="埃琳娜"]这次观测站的项目，是非常非常难得的机会。
[name="埃琳娜"]我只是想专心地做我的研究，如果有可能的话，可以在已有知识的边界上，走得再远一点......
[charslot(slot="l",name="avg_npc_1999_1#4$1",focus="l")]
[name="卡罗琳"]边界啊......这里还真是离“边界”最近的地方。
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="l")]
[name="卡罗琳"]对了，你听说过谢拉格的传说吗？
[charslot(slot="r",name="avg_1047_halo2_1#5$1",focus="r")]
[name="埃琳娜"]传说？什么传说？
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="l")]
[name="卡罗琳"]这片土地一千年来从来没有遭受过天灾，是因为有神明保护这里。
[charslot(slot="r",name="avg_1047_halo2_1#1$1",focus="r")]
[name="埃琳娜"]哈哈......每个国家早期都有过将特殊的现象归因于“神明”的传统啦。
[name="埃琳娜"]或许是谢拉格相对隔绝的环境让这样的传说保留的时间长了一点......
[charslot(slot="l",name="avg_npc_1999_1#4$1",focus="l")]
[name="卡罗琳"]可是从考察结果来看，谢拉格确实至少一千年没有遭遇过天灾呢。
[charslot(slot="r",name="avg_1047_halo2_1#9$1",focus="r")]
[name="埃琳娜"]的确是很少见的情况......但也一定是有可以解释的理由的。
[name="埃琳娜"]我想最大的可能应该是谢拉格的高海拔环境导致源石粉尘沉降无法集中，或者是——
[charslot(slot="l",name="avg_npc_1999_1#1$1",focus="l")]
[name="卡罗琳"]一只巨兽？
[charslot(slot="r",name="avg_1047_halo2_1#5$1",focus="r")]
[name="埃琳娜"]欸？
[charslot(slot="r",name="avg_1047_halo2_1#15$1",focus="r")]
[name="埃琳娜"]前辈就不要用这种神秘学笑话来调侃我啦，我可是很认真地在做假设的！
[name="埃琳娜"]我知道这片大地上还有许多地方保留着关于巨兽的传说和想象——一种体型等同于山脉的古老巨物，在死后身躯也会化为山川湖泊。
[charslot(slot="r",name="avg_1047_halo2_1#1$1",focus="r")]
[name="埃琳娜"]且不说根本没有可信的能证实巨兽存在的记录，而且，如果真的有这样的生物存在，那维持它们生命活动的能量从何而来呢？
[name="埃琳娜"]前辈突然提起这个......？
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="l")]
[name="卡罗琳"]没什么，闲聊突然想到罢了。
[name="卡罗琳"]行了，就先聊到这吧。去休息吧，晚上的观测交给我来就好。
[charslot(slot="r",name="avg_1047_halo2_1#2$1",focus="r")]
[name="埃琳娜"]真的可以吗？可是前辈已经连续好几晚值夜班了——
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="l")]
[name="卡罗琳"]反正作息已经颠倒过来了，和你聊了会天，正好清醒了一点。
[name="卡罗琳"]我没记错的话，高能粒子束轰击装置的供能结构应该还有问题没解决吧？
[charslot(slot="r",name="avg_1047_halo2_1#5$1",focus="r")]
[name="埃琳娜"]欸？前辈这么了解......
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="l")]
[name="卡罗琳"]养足精神，把你聪明的大脑用在更有价值的地方。
[charslot(slot="r",name="avg_1047_halo2_1#1$1",focus="r")]
[name="埃琳娜"]那就，多谢前辈啦！
[charslot(slot="r",name="avg_1047_halo2_1#14$1",focus="r")]
[name="埃琳娜"]等您有空的时候，我请您吃山下新开的维多利亚餐厅的炸鳞薯条！
[charslot(slot="l",name="avg_npc_1999_1#3$1",focus="l")]
[name="卡罗琳"]算了吧，没有一个维多利亚人会想在异国他乡吃到正宗的维多利亚食物的。
[charslot(slot="r",name="avg_1047_halo2_1#15$1",focus="r")]

... (全文18375字符)
```

### level_act46side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_snowconutryinside",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$dooropenquite", volume=1)]
[PlayMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[PlaySound(key="$d_avg_snowstormlp",volume=0, loop=true, channel="wind")]
[SoundVolume(volume=0.7,channel="wind", fadetime=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$doorclosequite", volume=1)]
[Delay(time=1)]
[stopsound(channel="wind", fadetime=1)]
[charslot(slot="m",name="avg_npc_1999_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1999_1#1$1",focus="m")]
[name="卡罗琳"]......
[name="卡罗琳"]门锁又被动过了，你就是不死心，是吗？
[name="卡罗琳"]遗憾的是，我确认过搜查队的路线，他们今天的活动范围离这里至少还有五公里。不要指望他们能听到你的求救信号。
[charslot(slot="m",name="avg_npc_255_1#6$1",focus="m")]
[name="莫希"]哼......
[Dialog]
[charslot(slot="m",name="avg_npc_1999_1#1$1",focus="m")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_plasticbag", volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1999_1#1$1",focus="m")]
[name="卡罗琳"]至少吃点东西吧。
[name="卡罗琳"]恢复期间不摄入足量的食物，断骨的恢复时间会延长大约百分之二十，留下后遗症的概率则会提升百分之三十五。
[name="卡罗琳"]我没打算伤害你，也不忍心见一个优秀的战士自此落下残疾。
[charslot(slot="m",name="avg_npc_255_1#7$1",focus="m")]
[name="莫希"]别假惺惺的！
[charslot(slot="m",name="avg_npc_255_1#6$1",focus="m")]
[name="莫希"]你最好立刻杀了我......
[charslot(slot="m",name="avg_npc_1999_1#4$1",focus="m")]
[name="卡罗琳"]我的确有这个选择......
[name="卡罗琳"]可就像我说的，我从来没有打算做危害谢拉格的事，更没有必要去杀害一个无辜的谢拉格人。
[multiline(name="卡罗琳")]何况，我们能从那场雪崩中活下来本身就是奇迹......
[charslot(slot="m",name="avg_npc_1999_1#1$1",focus="m")]
[multiline(name="卡罗琳")]用你们的话说，“耶拉冈德的庇护”，对吗？
[name="卡罗琳"]作为虔诚的信徒，这种时候不该更珍惜自己的生命吗？
[charslot(slot="m",name="avg_npc_255_1#7$1",focus="m")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="莫希"]你作为维多利亚的间谍，偷取谢拉格的军事情报，还说不是在危害谢拉格？！
[charslot(slot="m",name="avg_npc_1999_1#2$1",focus="m")]
[name="卡罗琳"]这可真的是冤枉我了......
[charslot(slot="m",name="avg_npc_1999_1#9$1",focus="m")]
[name="卡罗琳"]作为谢拉格人，你为什么会觉得谢拉格最重要的秘密，只在于那几艘微不足道的高速战舰的消息？
[name="卡罗琳"]明明口口声声感念着神明的恩典，但你们真的从来没有人质疑过，你们口中的“神”是什么？
[charslot(slot="m",name="avg_npc_255_1#4$1",focus="m")]
[name="莫希"]你在说什么......耶拉冈德就是耶拉冈德，没有人应该质疑祂——
[charslot(slot="m",name="avg_npc_1999_1#1$1",focus="m")]
[name="卡罗琳"]还是说不通吗......唉，也就是被困在这里没事可做才会想和你聊这个。
[charslot(slot="m",name="avg_npc_1999_1#8$1",focus="m")]
[name="卡罗琳"]算了，不聊也罢。
[charslot(slot="m",name="avg_npc_255_1#6$1",focus="m")]
[name="莫希"]......那我倒是想和你聊聊。
[name="莫希"]你是维多利亚的间谍，又是怎么在莱茵生命工作了那么久的？
[charslot(slot="m",name="avg_npc_1999_1#1$1",focus="m")]
[name="卡罗琳"]我既然已经为莱茵生命工作了这么久，你又怎么确信，我还是维多利亚的间谍？
[charslot(slot="m",name="avg_npc_1999_1#3$1",focus="m")]
[name="卡罗琳"]哈......你要是想听的话，我就来讲一个故事吧——
[name="卡罗琳"]有一个出生在维多利亚的孩子，她从小就对这片大地上一切规律法则充满了好奇。她本来准备用毕生精力来研究这些现象背后的秘密。
[charslot(slot="m",name="avg_npc_1999_1#4$1",focus="m")]
[name="卡罗琳"]当她苦读十几年，准备以皇家科学院荣誉学者的身份，前往哥伦比亚交流深造的时候......
[name="卡罗琳"]找上她的不是维多利亚的学术基金会，而是情报组织。
[name="卡罗琳"]从此，她被允许可以好奇的问题，就仅局限于哥伦比亚政府的秘密文件了。
[name="卡罗琳"]可是人的好奇心又如何能被限制住呢，她在挖掘哥伦比亚深藏的秘密的时候，真的碰巧发现了一个，可以让她尽情满足好奇心的机会......
[charslot(slot="m",name="avg_npc_255_1#6$1",focus="m")]
[name="莫希"]......
[charslot(slot="m",name="avg_npc_1999_1#4$1",focus="m")]
[name="卡罗琳"]不过说到底......哥伦比亚，维多利亚，都没什么区别。
[name="卡罗琳"]人们永远为眼前一点蝇头小利争得头破血流，费力搭建的秩序在毫无意义又你死我活的战争里苟延残喘......
[charslot(slot="m",name="avg_npc_1999_1#10$1",focus="m")]
[name="卡罗琳"]谁还有余力关心天空......或者是这片人们其实根本就不了解的大地？
[name="卡罗琳"]......我只怪这一切无聊透了。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="24_g3_mainhall",screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
清晨，蔓珠院藏经阁。
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(slot="m",name="avg_1047_halo2_1#2$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_1047_halo2_1#2$1",focus="m")]
[name="埃琳娜"]呼，还好窗户的位置不高。
[Dialog]
[charslot(slot="m",name="avg_1047_halo2_1#12$1",focus="m")]
[delay(time=1)]
[charslot(slot="m",name="avg_1047_halo2_1#13$1",focus="m")]
[delay(time=1)]
[charslot(slot="m",name="avg_1047_halo2_1#7$1",focus="m")]
[name="埃琳娜"]修士们也去晨祷了......这种时候，观测站正在风口浪尖上，必须要躲着点他们。
[name="埃琳娜"]我看看，地图、地理志，任何能帮上忙的......
[Dialog]
[charslot]
晨曦透过窗户，薄薄地铺在斑驳的书脊上。
埃琳娜拂去眼前每一本图书的灰尘，但方方正正的修士字体难以辨认，她开始懊悔自己没有多带一本谢拉格语词典。
[charslot(slot="m",name="avg_1047_halo2_1#2$1",focus="m")]
[name="埃琳娜"]这里的书到底是按什么分类的......这一本是格......格言集？
[name="埃琳娜"]“耶拉冈德，向我，显圣，祂，说道——”
[charslot(slot="m",name="avg_1047_halo2_1#2$1",focus="n")]
[name="？？？"]“不要求于我的殿，而要求于我的心。”
[charslot(slot="m",name="avg_1047_halo2_1#4$1",focus="m")]
[name="埃琳娜"]呜哇——！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_manybooksdrop", volume=1)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
埃琳娜惊慌地撒开了手，厚厚的书砸在木地板上。
隔着书架，她看到了一副藏在兜帽下惊讶的面孔，还有一张对准了自己的弩。
[Dialog]
[charslot(slot="l",name="avg_4211_snhunt_1#8$1",duration=1)]
[charslot(slot="r",name="avg_npc_2010_1#6$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_4211_snhunt_1#8$1",focus="l")]
[name="茱安娜"]恩雅......看敌人的手势，她好像投降了，我们怎么办？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_1047_halo2_1#6$1",focus="m")]
[name="埃琳娜"]你说谁投降了？！
[charslot(slot="m",name="avg_1047_halo2_1#4$1",focus="m")]
[name="埃琳娜"]不，不对不对，恩雅......恩雅·希瓦艾什？
[charslot(slot="m",name="avg_npc_2010_1#6$1",focus="m")]
[name="恩雅"]......
[charslot(slot="m",name="avg_1047_halo2_1#4$1",focus="m")]
[name="埃琳娜"]你......你就是圣女？
[charslot(slot="m",name="avg_npc_2010_1#1$1",focus="m")]
[name="恩雅"]嘘——
[Dialog]
[charslot]
埃琳娜恍然大悟般地点点头。
[charslot(slot="m",name="avg_npc_2010_1#3$1",focus="m")]
[name="恩雅"]不要声张，我们可以友好地聊聊，好吗？
[Dialog]
[charslot]
埃琳娜小心翼翼地点点头。
[charslot(slot="m",name="avg_npc_2010_1#3$1

... (全文17092字符)
```

### level_act46side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_manorindoor",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_867_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="“灰礼帽”"]还要多久？
[charslot(slot="m",name="avg_npc_493_1#1$1",focus="m")]
[name="维多利亚管家"]稍安勿躁，贝林厄姆先生。
[name="维多利亚管家"]您知道的，公爵阁下最近事务繁忙，每天都要接见好几位客人。
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[name="“灰礼帽”"]先生，你应该还记得，上一次我来这里......
[charslot(slot="m",name="avg_npc_493_1#1$1",focus="m")]
[name="维多利亚管家"]哈——
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[name="“灰礼帽”"]因此我想问......她最近心情如何？
[charslot(slot="m",name="avg_npc_493_1#1$1",focus="m")]
[name="维多利亚管家"]大多数时候还是比较愉快的，毕竟这几天和卡西米尔人的谈判接近尾声了——
[Dialog]
[charslot]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_1256_1#1$1",duration=1.5)]
[Delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m", afrom=1, ato=0, duration=1)]
[charslot(slot="m", posfrom="0,0", posto="-150,0", duration=1.5)]
[Delay(time=2.5)]
话音刚落，一个垂头丧气的绅士快步走过“灰礼帽”身边。
[charslot]
“灰礼帽”认出这是新闻办公室的德里克主任，想来是最近的舆情不利，主任那擦着汗的手在不住地颤抖。
[charslot(slot="m",name="avg_npc_493_1#1$1",focus="m")]
[name="维多利亚管家"]......我想，今天可能例外。
[Dialog]
[charslot]
[name="开斯特公爵"]外面的是贝林厄姆吗？先让他进来，别在门外等了。
[Dialog]
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[Delay(time=1)]
[charslot(slot="m", afrom=1, ato=0, duration=1)]
[charslot(slot="m", posfrom="0,0", posto="150,0", duration=1.5)]
[Delay(time=1.5)]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=2)]
管家点点头，“灰礼帽”迟疑片刻，走进房内。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="34_g6_noblelivingroom",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
开斯特公爵坐在正中，身旁站着一位年轻的贵族人士。
[Dialog]
[charslot(slot="m",name="avg_npc_726_1#7$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_726_1#7$1",focus="m")]
[name="开斯特公爵"]......还有一个问题，你约见的那位卡西米尔代表，是一个什么样的人？
[charslot(slot="m",name="avg_npc_726_1#7$1",focus="none")]
[name="维多利亚贵族"]他是一个商人，公爵阁下。
[charslot(slot="m",name="avg_npc_726_1#2$1",focus="m")]
[name="开斯特公爵"]嗯，卡西米尔......
[charslot(slot="m",name="avg_npc_726_1#7$1",focus="m")]
[name="开斯特公爵"]告诉他，如果答应我的条件，我可以特许开放部分禁运的工业设备。
[name="开斯特公爵"]对他们而言，获取廉价矿产的途径还有很多，谢拉格并非不可替代。
[charslot(slot="m",name="avg_npc_726_1#7$1",focus="none")]
[name="维多利亚贵族"]我会向他传达的，只有维多利亚能在技术和设备上满足他的需求，尤其是源石——
[charslot(slot="m",name="avg_npc_726_1#7$1",focus="m")]
[name="开斯特公爵"]不。
[name="开斯特公爵"]你是开斯特家族的后辈，确切的信息是留给下人去说的，而我们永远要留有余地。
[name="开斯特公爵"]卡西米尔人对我们所掌握的资源没有多少认知，不妨让他发挥一些想象力，明白吗？
[charslot(slot="m",name="avg_npc_726_1#7$1",focus="none")]
[name="维多利亚贵族"]没问题，我敢保证他会倒向我们的。
[charslot(slot="m",name="avg_npc_726_1#2$1",focus="m")]
[name="开斯特公爵"]“永远兑现承诺”，若是做不到，就应当缄口不言。
[charslot(slot="m",name="avg_npc_726_1#7$1",focus="m")]
[name="开斯特公爵"]对卡西米尔代表如此，对我尤其如此。
[name="开斯特公爵"]你也可以出去了。
[charslot(slot="m",name="avg_npc_726_1#7$1",focus="none")]
[name="维多利亚贵族"]是......抱歉，阁下。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_726_1#1$1",focus="m")]
[Delay(time=1.5)]
[name="开斯特公爵"]又让你见到我教育这些不争气的小鬼了。
[name="开斯特公爵"]贝里。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_726_1#1$1",focus="l")]
[name="“灰礼帽”"]......感谢公爵阁下对我的信任。
[charslot(slot="r",name="avg_npc_726_1#7$1",focus="r")]
[name="开斯特公爵"]家常先不多说。你应该看到那位，更早之前出去的绅士了吧？
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]如果我没认错的话，他是主管新闻与舆论的德里克先生。
[charslot(slot="r",name="avg_npc_726_1#7$1",focus="r")]
[name="开斯特公爵"]他理应在今天向我汇报，无论谢拉格还是维多利亚，负面新闻已在控制之中了。
[name="开斯特公爵"]然而他却抱怨半天，说自己做不到，与派出的摄制组沟通需要时间，还想麻烦我看他们发回的录像。
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]......
[charslot(slot="r",name="avg_npc_726_1#1$1",focus="r")]
[name="开斯特公爵"]如果他觉得给的时间不足，那他最好应该知道我的耐心也不足。
[name="开斯特公爵"]所以，你有什么好消息吗，贝里？
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]......是，公爵阁下。
[name="“灰礼帽”"]我们在莱茵观测站的线人的情报十分准确，谢拉格与卡西米尔合作的矿区确实有极大的蹊跷。
[name="“灰礼帽”"]我的人循着她提供的线索，成功地潜入矿区，拿到了这几份数据表格。
[charslot(slot="r",name="avg_npc_726_1#7$1",focus="r")]
[name="开斯特公爵"]直接指明上面的“亮点”。
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]您请看这一段，还有下页这段......
[name="“灰礼帽”"]前者是该矿区每天的开采量，后者是收购量或者说出口量，最后那页是矿区的财报，尤其注意净利润一项。比如前两个月——
[charslot(slot="r",name="avg_npc_726_1#6$1",focus="r")]
[name="开斯特公爵"]差额巨大......这个矿区一直在亏损，并且开采的矿产越多，亏损反而越高。
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]没错，我们甚至还发现了这本矿区进口记录，您请看......
[charslot(slot="r",name="avg_npc_726_1#9$1",focus="r")]
[name="开斯特公爵"]嗯？一个大型矿区，要额外进口相同的矿产......
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]因此，我认为这验证了早期的推测。
[name="“灰礼帽”"]所谓的“合作矿区”，实质上是一个被伪装的喀兰贸易军工厂。
[charslot(slot="r",name="avg_npc_726_1#7$1",focus="r")]
[name="开斯特公爵"]......
[name="开斯特公爵"]这就是那张倒扣的底牌吗？居然在与外国合资的矿区里？
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]所以本人在内的特工起初都忽视了这片区域......常识上难以想象会有人做出如此冒险之举。
[charslot(slot="r",name="avg_npc_726_1#6$1",focus="r")]
[name="开斯特公爵"]......在注意力的盲区落子，倒像是他的风格。
[charslot(slot="r",name="avg_npc_726_1#7$1",focus="r")]
[name="开斯特公爵"]不过，还差一步，贝里。
[name="开斯特公爵"]虽然不愿意这样承认，但是在威灵顿做出了那样的举动后，我们加强自身的力量已经是迫在眉睫。
[name="开斯特公爵"]在这样的势态下，谢拉格是珍贵的资产。
[charslot(slot="r",name="avg_npc_726_1#2$1",focus="r")]
[name="开斯特公爵"]两败俱伤不是我能接受的，必须确保恩希欧迪斯没有超出我们预估的军事准备。
[charslot(slot="r",name="avg_npc_726_1#7$1",focus="r")]
[name="开斯特公爵"]只有知道这张底牌具体是什么，才好提前布置对谢拉格的行动。
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]阁下，若要与威灵顿公爵对抗的话......
[name="“灰礼帽”"]将谢拉格纳入开斯特家族的控制范围，攫取人力

... (全文31325字符)
```

### level_act46side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g10_manorhouse",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_262_1#7$1",duration=1.5)]
[Delay(time=2)]
[name="休露丝"]这些天，想和你见一面，可真是不容易。
[charslot(slot="m",name="avg_npc_262_1#7$1",focus="m")]
[name="休露丝"]......恩希欧迪斯。
[charslot(slot="m",name="avg_172_svrash_1#2$1",focus="m")]
[name="恩希欧迪斯"]未能出席大夫人的葬礼，实在抱歉。
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]休露丝夫人，我为布朗陶家的遭遇深感遗憾，如果有任何希瓦艾什家能帮上忙的地方，请务必相告。
[charslot(slot="m",name="avg_npc_262_1#2$1",focus="m")]
[name="休露丝"]谢谢你，恩希欧迪斯。
[charslot(slot="m",name="avg_npc_262_1#2$1",focus="m")]
[name="休露丝"]不过今天我来找你，也不是为了说这些的。
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]休露丝夫人此次来访，想必是要给我一个赢得信任的机会。
[charslot(slot="m",name="avg_npc_262_1#9$1",focus="m")]
[name="休露丝"]哼......姐姐说过，你放低姿态的时候，就是最难以令人信任的时候。
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]那不知休露丝夫人又是如何看待我的呢？
[charslot(slot="m",name="avg_npc_262_1#7$1",focus="m")]
[name="休露丝"]不用这样拐弯抹角的，我不喜欢。
[charslot(slot="m",name="avg_npc_262_1#9$1",focus="m")]
[name="休露丝"]......以前姐姐一直责骂我冲动，说话办事不过脑子......
[name="休露丝"]我想向她证明，证明我不需要躲藏在她的羽翼下，证明我能够为布朗陶家做点什么。
[charslot(slot="m",name="avg_npc_262_1#6$1",focus="m")]
[name="休露丝"]但如今，我是布朗陶的家主，已经没有人能来评判我的“证明”了。
[charslot(slot="m",name="avg_172_svrash_1#9$1",focus="m")]
[name="恩希欧迪斯"]......
[charslot(slot="m",name="avg_172_svrash_1#2$1",focus="m")]
[name="恩希欧迪斯"]我可以理解，我也有......两个妹妹。
[charslot(slot="m",name="avg_npc_262_1#6$1",focus="m")]
[name="休露丝"]在你看来，圣女大人，与恩希亚......她们都比我要聪明得多吧？
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]休露丝夫人自谦了。
[charslot(slot="m",name="avg_172_svrash_1#10$1",focus="m")]
[name="恩希欧迪斯"]不过，我倒是认为，她们也有与你相似的执着与决心。
[charslot(slot="m",name="avg_npc_262_1#6$1",focus="m")]
[name="休露丝"]......
[name="休露丝"]恩希亚她还好吗？我听说，她也遇上了意外。
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]谢谢休露丝夫人记挂，她并无大碍，已经回家了。
[charslot(slot="m",name="avg_npc_262_1#9$1",focus="m")]
[name="休露丝"]恩希欧迪斯先生永远是这样一副处变不惊的样子......
[charslot(slot="m",name="avg_npc_262_1#7$1",focus="m")]
[name="休露丝"]我想问，对这些发生在谢拉格的袭击，包括我姐姐的事......你早有预料吗？
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]原来这才是休露丝夫人今天来访的目的......
[charslot(slot="m",name="avg_npc_262_1#7$1",focus="m")]
[name="休露丝"]恩希欧迪斯，姐姐她一直在帮你做事，是不是？
[name="休露丝"]我对此并非一无所知，但是直到姐姐发生意外后我才发现......
[name="休露丝"]你们的计划，关于维多利亚，莱茵生命，还有莫希在追查的事......还有太多我不知道的事。
[charslot(slot="m",name="avg_172_svrash_1#9$1",focus="m")]
[name="恩希欧迪斯"]......
[charslot(slot="m",name="avg_npc_262_1#7$1",focus="m")]
[name="休露丝"]不要否认，不要骗我，恩希欧迪斯，你一定知道关于她遇害的真相。
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]休露丝夫人，如果你认为大夫人的死与我——
[charslot(slot="m",name="avg_npc_262_1#9$1",focus="m")]
[name="休露丝"]不......你误会我的意思了。
[name="休露丝"]虽然我不知道菈塔托丝究竟在和你谋划什么，但我相信，她一定是在做保护谢拉格的事。
[charslot(slot="m",name="avg_npc_262_1#6$1",focus="m")]
[name="休露丝"]那么......我也会做与她一样的事......布朗陶家的事，不论什么，我都会承担。
[name="休露丝"]所以，我需要你告诉我，姐姐她到底——
[Dialog]
[charslot]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=2)]
[PlaySound(key="$d_gen_soldiersrun", volume=1)]
[Delay(time=2)]
[name="希瓦艾什家护卫"]抱歉，恩希欧迪斯老爷，他们无论如何都要闯进来——
[Dialog]
[charslot(slot="m",name="avg_npc_262_1#7$1",focus="m")]
[name="休露丝"]......？
[charslot(slot="m",name="avg_172_svrash_1#7$1",focus="m")]
[name="恩希欧迪斯"]各位就这样闯入我家中，到底有何贵干？
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_268",duration=1.5)]
[Delay(time=2)]
[name="蔓珠院使者"]恩希欧迪斯大人，喀兰贸易为何私自将谢拉格与卡西米尔联合矿场的股份尽数转让给维多利亚？
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]......这是哪里来的消息？
[charslot(slot="m",name="avg_npc_268",focus="m")]
[name="蔓珠院使者"]如今矿场已经全面由维多利亚人接管，这已经是人人可见的事实了。
[name="蔓珠院使者"]阿德颂大长老认为，喀兰贸易这样的举动已有私通他国之嫌，蔓珠院不得不行使权力介入了。
[name="蔓珠院使者"]我们要求你现在就去蔓珠院，为此事说明。
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]听蔓珠院的意思，这是要正式审问希瓦艾什家了。
[charslot(slot="m",name="avg_npc_268",focus="m")]
[name="蔓珠院使者"]如今谢拉格人心惶惶，我们也不愿意看到矛盾愈演愈烈。
[name="蔓珠院使者"]只是恩希欧迪斯大人为一族之长，如果还自认为对谢拉格负有责任，请现在就前往蔓珠院，与我们共商对策。
[charslot(slot="m",name="avg_172_svrash_1#2$1",focus="m")]
[name="恩希欧迪斯"]好，我当然不会推辞。
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]但是既然要说明情况，整理好相关文件还需要一点时间，容我做好准备。
[name="恩希欧迪斯"]另外，我与休露丝夫人还有一些话没说完，请修士暂且等候。
[charslot(slot="m",name="avg_npc_268",focus="m")]
[name="蔓珠院使者"]当然，恩希欧迪斯大人。
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]......休露丝夫人，感谢你最近能抽出时间关照恩希亚，我想正式邀请你来希瓦艾什家做客。
[name="恩希欧迪斯"]我也想与她一起当面感谢你的关心。
[charslot(slot="m",name="avg_npc_262_1#4$1",focus="m")]
[name="休露丝"]什......
[charslot(slot="m",name="avg_172_svrash_1#2$1",focus="m")]
[name="恩希欧迪斯"]按礼数，我本来该正式送上邀请函。
[charslot(slot="m",name="avg_172_svrash_1#10$1",focus="m")]
[name="恩希欧迪斯"]事出仓促，我临时手写一张，请休露丝夫人见谅。
[name="恩希欧迪斯"]届时恭候休露丝夫人光临。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_paper2", volume=1)]
[Delay(time=2)]
不及对方回应，他径直从桌上拿起纸笔，几笔写完后递了过去。
休露丝接过。这不是“邀请函”，纸上只有一串地址。
[charslot(slot="m",name="avg_npc_262_1#7$1",focus="m")]
[name="休露丝"]......感谢你的邀请。
[name="休露丝"]我会按时到的。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="45_g11_karlanheadquarters",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_paper2")]
[Delay(time=2)]
[Sticker(id="st1", multi = true, text="致喀兰贸易诺希斯先生", x=180,y=170, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n展信佳。", x=380,y=170, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n在您看到这封信时，我还未被授予莱茵生命情况通报权限，

... (全文16183字符)
```

### level_act46side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[delay(time=0.5)]
[name="阿德颂"]......你终于到了。
[name="阿德颂"]恩希欧迪斯。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="24_g2_temple_indoor",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="l",name="avg_npc_268",duration=1.5)]
[charslot(slot="r",name="avg_npc_268",duration=1.5)]
[Delay(time=2)]
[charslot(slot="l", posfrom="0,0", posto="-150,0", duration=2)]
[charslot(slot="r", posfrom="0,0", posto="150,0", duration=2)]
[Delay(time=2.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_1998_1#1$1",duration=1.5)]
[Delay(time=1)]
[charslot(slot="l",afrom=1,ato=0,posfrom="-150,0", posto="-200,0", duration=1)]
[charslot(slot="r",afrom=1,ato=0,posfrom="150,0", posto="200,0", duration=1)]
[Delay(time=3.5)]
[charslot]
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]蔓珠院的邀请，我自然不敢怠慢......阿德颂长老。
[charslot(slot="m",name="avg_npc_1998_1#1$1",focus="m")]
[name="阿德颂"]我记得，从希瓦艾什领到蔓珠院要不了那么长时间。
[charslot(slot="m",name="avg_172_svrash_1#2$1",focus="m")]
[name="恩希欧迪斯"]来蔓珠院述职事关重大，何况是蔓珠院怀疑我私通维多利亚，我不得不做好准备来自证清白。
[charslot(slot="m",name="avg_npc_1998_1#1$1",focus="m")]
[name="阿德颂"]事不宜迟，就请恩希欧迪斯大人移步，与我进屋中详谈吧。
[charslot(slot="m",name="avg_172_svrash_1#10$1",focus="m")]
[name="恩希欧迪斯"]请等一下。
[Dialog]
[charslot]
[PlaySound(key="$drift", volume=1)]
[CameraShake(duration=1.5, xstrength=10, ystrength=10, vibrato=20, randomness=70, fadeout=true, block=true)]
[PlaySound(key="$d_gen_soldiersrun", volume=1)]
[charslot(slot="l",name="avg_npc_275",posfrom="-200,0", posto="-200,0",duration=1.5)]
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_275",posfrom="200,0", posto="200,0",duration=1.5)]
[Delay(time=2.5)]
[charslot]
一支声势浩大的车队停在了蔓珠院中央。
[charslot(slot="m",name="avg_npc_1998_1#8$1",focus="m")]
[name="阿德颂"]希瓦艾什......你这是要做什么？
[charslot(slot="m",name="avg_172_svrash_1#10$1",focus="m")]
[name="恩希欧迪斯"]蔓珠院不是要调查喀兰贸易与维多利亚的合作？
[name="恩希欧迪斯"]我叫人把近十年来喀兰贸易与维多利亚所有的往来文件都整理好带了过来，数量有些多，只能多装几辆车了。
[name="恩希欧迪斯"]阿德颂大长老，您要是感兴趣的话，可以慢慢看。
[charslot(slot="m",name="avg_npc_1998_1#1$1",focus="m")]
[name="阿德颂"]好......很好。
[name="阿德颂"]那就把这些东西留下，叫你的人离开吧。
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]不可。
[charslot(slot="m",name="avg_npc_1998_1#8$1",focus="m")]
[name="阿德颂"]恩希欧迪斯，你这是什么意思？
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]最近谢拉格的确发生了不少风波，其中许多事，也都被证明与维多利亚有关......
[name="恩希欧迪斯"]我们的士兵，的确发现了蔓珠院的修士与维多利亚间谍接触的证据。
[charslot(slot="m",name="avg_npc_1998_1#8$1",focus="m")]
[name="阿德颂"]空口无凭，你何来权力搜查蔓珠院？
[charslot(slot="m",name="avg_172_svrash_1#12$1",focus="m")]
[name="恩希欧迪斯"]我不敢搜查蔓珠院，只是今天蔓珠院请我来讨论“有人私通维多利亚”的事，我便来了。
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]听我命令，今天在我和阿德颂长老商讨出一个结果之前，任何人不得离开蔓珠院。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_275")]
[charslot(slot="r",name="avg_npc_275")]
[CameraShake(duration=0.5, xstrength=5, ystrength=5, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="“山雪鬼”"]是！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_172_svrash_1#10$1",focus="m")]
[name="恩希欧迪斯"]阿德颂长老，请吧。
[charslot(slot="m",name="avg_npc_1998_1#1$1",focus="m")]
[name="阿德颂"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="24_g3_mainhall",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1998_1#1$1",focus="m")]
[name="阿德颂"]......我们之前从来没有像这样交谈过。
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]以往我来到蔓珠院，都很少能见到你，遑论交谈。
[name="恩希欧迪斯"]曾听修士们说，阿德颂长老多年来一直在藏经阁里潜心研究典籍，深居简出，从不过问一句俗务。
[name="恩希欧迪斯"]如今长老代管蔓珠院事务，似乎也是得心应手。
[charslot(slot="m",name="avg_npc_1998_1#7$1",focus="m")]
[name="阿德颂"]多年来我在做的唯一一件事，就是确保谢拉格，走在祂定下的道路上。
[charslot(slot="m",name="avg_npc_1998_1#1$1",focus="m")]
[name="阿德颂"]何况在这存亡绝续的关头，难道蔓珠院应该眼睁睁看着你将谢拉格拖入深渊，任由卡西米尔、维多利亚或是别的国家蚕食殆尽？
[name="阿德颂"]你不是谢拉格的国王，大人。
[charslot(slot="m",name="avg_172_svrash_1#11$1",focus="m")]
[name="恩希欧迪斯"]多谢长老警示。如果谢拉格有国王，那只能是祂。
[charslot(slot="m",name="avg_172_svrash_1#10$1",focus="m")]
[name="恩希欧迪斯"]如果蔓珠院想匡正外交上的过失，喀兰贸易将会尽力配合。
[charslot(slot="m",name="avg_172_svrash_1#10$1",focus="m")]
[name="恩希欧迪斯"]只是，有一个问题令我困惑不已，还须向你请教。
[charslot(slot="m",name="avg_172_svrash_1#7$1",focus="m")]
[name="恩希欧迪斯"]蔓珠院到底在以何种方式，与维多利亚交涉呢？
[name="恩希欧迪斯"]是以谢拉格本身作为筹码？
[Dialog]
[charslot]
[PlaySound(key="$dooropenquite", volume=1)]
[charslot(slot="m",name="avg_npc_268",duration=1.5)]
[Delay(time=2)]
[name="蔓珠院修士"]长老！
[Dialog]
[charslot(slot="m", afrom=1, ato=0, duration=1)]
[charslot(slot="m", posfrom="0,0", posto="150,0", duration=1.5)]
[Delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1998_1#1$1",focus="m")]
[charslot(slot="l",name="avg_npc_268",afrom=0, ato=1, duration=1)]
[charslot(slot="l", posfrom="-150,0", posto="-50,0", duration=1.5)]
[Delay(time=1.5)]
[charslot(slot="l",focus="l")]
[name="蔓珠院修士"]（低声）我们刚才看了一圈，希瓦艾什的军队已经把下山的路围死了。
[name="蔓珠院修士"]（低声）我们，我们再去看看后门和——
[Dialog]
[charslot]
[charslot(slot="m",name="avg_172_svrash_1#10$1",focus="m")]
[name="恩希欧迪斯"]密道？
[charslot(slot="m",name="avg_172_svrash_1#11$1",focus="m")]
[name="恩希欧迪斯"]不必浪费时间，除非你们中有人对“山雪鬼”感兴趣。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1998_1#1$1",focus="l")]
[charslot(slot="l",name="avg_npc_268", posfrom="-50,0", posto="-50,0",focus="l")]
[name="蔓珠院修士"]啊——
[Dialog]
[charslot]
[charslot(slot="m",name="avg_172_svrash_1#10$1

... (全文26551字符)
```

### level_act46side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_gen_soldiersrun", volume=1)]
[Delay(time=2)]
[name="远处的声音"]快！后面的都跟上！
[name="远处的声音"]情报上显示目标应该就在这附近，仔细搜，一点都不能放过了！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_snowconutryinside",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$dignified_intro",key="$dignified_loop", volume=0.6)]
[Delay(time=1)]
[name="莫希"]......
[Dialog]
在那个人离开这间屋子后又过去了不知多久，莫希几乎失去了对时间的感知。
只有身上还紧紧束缚着的绳索带来的刺痛，提醒她自己还没有失去知觉。
门外终于传来了希望的声音，莫希竭尽全力呼喊。
[Dialog]
[charslot(slot="m",name="avg_npc_255_1#5$1",afrom=0, ato=1, duration=1)]
[charslot(slot="m", posfrom="0,-50", posto="0,0", duration=2.5)]
[Delay(time=3)]
[name="莫希"]我在......这......
[name="莫希"]我在——
[charslot(slot="m",name="avg_npc_255_1#5$1",focus="none")]
莫希想要呼喊，可是干枯的喉咙几乎无法发声。
[Dialog]
[PlaySound(key="$d_avg_ftrub", volume=1)]
[charslot(slot="m", posfrom="0,0", posto="-20,0", duration=2.5)]
[Delay(time=3)]
[PlaySound(key="$d_avg_ftrub", volume=1)]
[charslot(slot="m", posfrom="-20,0", posto="-40,0", duration=2.5)]
[Delay(time=3)]
[PlaySound(key="$d_avg_ftrub", volume=1)]
[charslot(slot="m",afrom=1, ato=0, duration=1)]
[charslot(slot="m", posfrom="-40,0", posto="-60,0", duration=2.5)]
[Delay(time=3)]
[charslot]
她艰难地向门的方向匍匐爬去。
[Dialog]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=2)]
门打开了。
[Dialog]
[charslot(slot="m",name="avg_npc_262_1#8$1",duration=1.5)]
[Delay(time=1.5)]
[name="休露丝"]莫希！
[Dialog]
[charslot(slot="m", posfrom="0,0", posto="50,-20", duration=1.5)]
[Delay(time=2)]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot="m", posfrom="50,-20", posto="-200,0", duration=3.5)]
[charslot(slot="r",name="avg_npc_255_1#5$1",afrom=0, ato=1, duration=1)]
[charslot(slot="r", posfrom="20,-50", posto="0,0", duration=2.5)]
[Delay(time=3.5)]
[charslot(slot="r",focus="r")]
[name="莫希"]夫人......怎么是你......
[charslot(slot="m",name="avg_npc_262_1#6$1", posfrom="-200,0",posto="-200,0",focus="m")]
[name="休露丝"]天灾发生后我们一直在找你！该死的希瓦艾什，装模作样的，我还以为他们掌握了多么准确的情报......到头来还不是得我自己慢慢找！
[name="休露丝"]你怎么样，有没有哪里受伤了？
[charslot(slot="m",name="avg_npc_262_1#4$1", posfrom="-200,0",posto="-200,0",focus="m")]
[name="休露丝"]等等，你的腿——
[charslot(slot="r",name="avg_npc_255_1#5$1",focus="r")]
[name="莫希"]我......没事......
[name="莫希"]夫人，你听我说......
[name="莫希"]我在追踪的那个研究员......她来自维多利亚，但更重要的是......她还和，哥伦比亚......
[name="莫希"]他们的真正目的是......
[Dialog]
[PlaySound(key="$bodyfalldown1", volume=1)]
[charslot(slot="r",afrom=1, ato=0, duration=1)]
[charslot(slot="r", posfrom="0,0", posto="0,-30", duration=2.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_262_1#8$1", posfrom="-200,0",posto="-200,0",focus="m")]
[name="休露丝"]莫希！莫希！
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="67_G14_miningarea",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
狭窄的山路上，拥挤的车队缓慢挪动着。
在刚刚突然的一幕发生后，不少人也纷纷下了车，驻足观望矛盾的中央。
[Dialog]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[charslot(slot="m",name="avg_199_yak_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="角峰"]熄火，下车。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_cardoorc", volume=1)]
[charslot(slot="m",name="avg_npc_399_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="维多利亚特工"]你们是什么人，敢做这种事情！
[name="维多利亚特工"]我......我是维多利亚派驻的产业调查员，你们这是非法妨碍公务。
[name="维多利亚特工"]你们在维多利亚的产业上危害维多利亚人的安全，还差点造成交通事故，我一定会向蔓珠院告发你们的行为！
[name="维多利亚特工"]*维多利亚粗口*，就不该来这种鬼地方......
[charslot(slot="m",name="avg_199_yak_1#1$1",focus="m")]
[name="角峰"]......说够了？
[name="角峰"]都拍下来了吗？
[charslot(slot="m",name="avg_npc_286_1#1$1",focus="m")]
[name="希瓦艾什家护卫"]是！
[charslot(slot="m",name="avg_199_yak_1#6$1",focus="m")]
[name="角峰"]维多利亚人，现在不是你们掌握局势的场合，配合一点。
[name="角峰"]把后车厢打开。
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="维多利亚特工"]我......
[charslot(slot="m",name="avg_199_yak_1#6$1",focus="m")]
[name="角峰"]不愿意配合？无所谓，你们大可以保存着力气在审判席上为自己辩护——冷的话，需要给你一条毯子吗？
[Dialog]
[charslot]
[PlaySound(key="$d_avg_hgldshcrrig", volume=1)]
[Delay(time=2)]
角峰挥了挥手，护卫不由分说地撬开了后厢室。
端坐在草垛上的，是一名老修士。
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot="m",name="avg_npc_268",duration=1.5)]
[Delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5)]
[Delay(time=2)]
他扑打净身上的灰尘，坦然走了出来。
没有任何情绪，也谈不上什么勇气。
老修士看着眼前一片刺眼的明亮，回想起先前一幕。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.1,fadetime=0)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.1,fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0.8, fadetime=0)]
十几分钟前。
[Dialog]
[charslot(slot="l",name="avg_npc_1999_1#1$1")]
[charslot(slot="r",name="avg_npc_268")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot(slot="l",name="avg_npc_1999_1#2$1",focus="l")]
[name="卡罗琳"]怎么车停了？
[name="卡罗琳"]我们到了吗？
[charslot(slot="l",name="avg_npc_1999_1#10$1",focus="l")]
[name="卡罗琳"]......
[Dialog]
[charslot(slot="l",name="avg_npc_1999_1#10$1",focus="none")]
卡罗琳压低了声音。
[charslot(slot="l",name="avg_npc_1999_1#2$1",focus="l")]
[name="卡罗琳"]......什么情况？
[charslot(slot="r",name="avg_npc_268",focus="r")]
[name="年迈的修士"]女士，稍安勿躁。
[charslot(slot="l",name="avg_npc_1999_1#5$1",focus="l")]
[name="卡罗琳"]......我们被发现了吗？
[charslot(slot="r",name="avg_npc_268",focus="r")]
[name="年迈的修士"]......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[curtain(direction = 0,fillfrom = 0.5,fill

... (全文27296字符)
```

### level_act46side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g8_kjeragstreet",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1.5)]
寂静与空旷令人更觉寒冷，记者背着沉重的背包缓慢向前，踏在积雪上的声响清晰可闻。
[dialog]
[charslot(slot="m",name="avg_npc_2006_1#12$1",afrom=0, ato=1,duration=1)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_2006_1#12$1",focus="m")]
[name="维多利亚记者"]连这里的人都在变少......
[charslot(slot="m",name="avg_npc_2006_1#6$1",focus="m")]
[name="维多利亚记者"]......欸？
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="r",posfrom="0,0",posto="150,0",duration=0,block=true)]
[delay(time=0.1)]
[charslot(slot="r",name="avg_npc_273_1$1",afrom=0, ato=1,duration=1)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_2006_1#2$1")]
[delay(time=0.1)]
[charslot(slot="m",posfrom="0,0",posto="150,0",duration=1,block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_2006_1#2$1",focus="m")]
[name="维多利亚记者"]女士！抱歉打扰您，可以问您几个简短的问题吗？
[charslot(slot="r",name="avg_npc_273_1$1",focus="r")]
[name="匆忙的谢拉格人"]有什么问题？
[charslot(slot="m",name="avg_npc_2006_1#11$1",focus="m")]
[name="维多利亚记者"]如今喀兰贸易——
[charslot(slot="r",name="avg_npc_273_1$1",focus="r")]
[name="匆忙的谢拉格人"]我不想听这几个字。
[name="匆忙的谢拉格人"]让恩希欧迪斯大人出来说说，签那几个协议的前因后果。
[name="匆忙的谢拉格人"]什么“资源换发展”，结果换来了这一场天灾，他要怎么解释？
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="r",name="avg_npc_273_1$1",afrom=1, ato=0,posfrom="150,0",posto="200,0",duration=1)]
[delay(time=1)]
[charslot(slot="m",posfrom="150,0",posto="0,0",duration=2,block=true)]
[delay(time=1)]
[name="维多利亚记者"]......
[dialog]
[charslot(slot="m",name="avg_npc_2006_1#12$1",focus="m")]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_2006_1#12$1",focus="none")]
在记者还在消化愤怒的言辞时，这名谢拉格人早已拂衣而去。
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="l",posfrom="0,0",posto="-100,0",duration=0,block=true)]
[delay(time=0.1)]
[charslot(slot="l",name="avg_npc_278_1$1",afrom=0, ato=1,duration=1)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_2006_1#2$1")]
[charslot(slot="m",posfrom="0,0",posto="-70,0",duration=2,block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_278_1$1",focus="m")]
[charslot(slot="m",name="avg_npc_2006_1#2$1",focus="m")]
[name="维多利亚记者"]......这位先生，请留步！
[charslot(slot="l",name="avg_npc_278_1$1",focus="l")]
[name="温和的谢拉格人"]你是，来自维多利亚的记者吧？
[name="温和的谢拉格人"]最近谢拉格可不太平，连本地人都更愿意躲在家里，你得小心了。
[charslot(slot="m",name="avg_npc_2006_1#10$1",focus="m")]
[name="维多利亚记者"]但越到这种时候，就越不能够恐惧，否则我就不配拿起相机。
[charslot(slot="m",name="avg_npc_2006_1#2$1",focus="m")]
[name="维多利亚记者"]......还是感谢您的提醒。不过我想了解的是，如今您对恩希欧迪斯最真实的看法是？
[charslot(slot="l",name="avg_npc_278_1$1",focus="l")]
[name="温和的谢拉格人"]嗯......抱歉，维多利亚的记者，我觉得他欺骗了谢拉格人，但维多利亚确实值得怀疑。
[name="温和的谢拉格人"]这么多年来，谢拉格改变有多大我也看在眼里，要是说恩希欧迪斯大人没有苦衷显然也不属实。
[name="温和的谢拉格人"]要是蔓珠院的大长老现在能出来说两句话就好了——
[dialog]
[charslot(slot="l",name="avg_npc_278_1$1",focus="all")]
[charslot(slot="m",name="avg_npc_2006_1#2$1",focus="all")]
[PlaySound(key="$d_avg_throwstone")]
[delay(time=0.5)]
[PlaySound(key="$d_avg_windowbreak")]
[CameraShake(duration=0.2, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_2006_1#6$1",focus="all")]
[charslot(slot="l",name="avg_npc_278_1$1",afrom=1, ato=0,posfrom="-100,0",posto="-200,0",focus="all",duration=2)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_2006_1#6$1",focus="n")]
突如其来的石块几乎划过记者的鼻尖，它径直撞破后边的店铺橱窗。
[charslot(slot="m",name="avg_npc_2006_1#6$1",focus="m")]
[characteraction(name="middle", type="shake", power=2, times=70, fadetime=0.5, block=false)]
[name="维多利亚记者"]啊——
[charslot(slot="m",name="avg_npc_2006_1#6$1",focus="none")]
[name="愤怒的谢拉格人"]维多利亚滚出谢拉格！
[name="愤怒的谢拉格人"]恩希欧迪斯、蔓珠院、我们，都和你没有半点干系！
[CameraShake(duration=0.4, xstrength=40, ystrength=40, vibrato=40, randomness=90, fadeout=true, block=false)]
[name="愤怒的谢拉格人"]还敢再拍？给我*谢拉格俚语*滚！
[dialog]
[charslot(slot="m",name="avg_npc_2006_1#12$1")]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_2006_1#12$1",focus="none")]
没有什么比这一刻更令她五味杂陈。
她看到平凡生活中的谢拉格人，渐渐变得多疑、烦躁。
她更看到了曾经推心置腹的摄制组成员们，竟潜进她的房间，对着她的稿纸和相机反复检视......
[dialog]
[charslot(slot="m",name="avg_npc_2006_1#12$1")]
[dialog]
[delay(time=0.5)]
[PlaySound(key="$rungeneral")]
[charslot(slot="m",name="avg_npc_2006_1#12$1",posfrom="-70,0",posto="150,0",afrom=1,ato=0,duration=1,block=true)]
[delay(time=1)]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
当男人再次掏出一块石头，记者朝受访者鞠躬告别，跑离了现场......
似乎只有逃跑这一种选择......然而，她又能逃到哪里？
[dialog]
[delay(time=2)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Background(image="67_G4_kjeragstreet",screenadapt="coverall", block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$rungeneral")]
[charslot(slot="l",name="avg_npc_2006_1#12$1",posfrom="-150,0",posto="0,0",afrom=0,ato=1,duration=1,block=true)]
[delay(time=2)]
[charslot(slot="r",name="avg_npc_2002_1$1",afrom=0,ato=1,duration=1,block=true)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_2002_1$1",focus="r")]
[name="谢拉格儿童"]姐姐，你是维多利亚人吗？
[charslot(slot="l",name="avg_npc_2006_1#4$1",focus="l")]
[name="维多利亚记者"]啊......小朋友，你好。
[charslot(slot="l",name="avg_npc_2006_1#12$1",focus="l")]
[name="维多利亚记者"]......你，不讨厌维多利亚吗？
[charslot(slot="r",name="avg_npc_2002_1$1",focus="r")]
[name="谢拉格儿童"]嗯，我不讨厌。
[dialog]
[charslot(slot="l",name="avg_npc_2006_1#12$1",focus="r")]
[charslot(slot="r",name="avg_npc_2002_1$1")]
[delay(time=0.1)]
[charslot(slot="l",name="avg_npc_2006_1#12$1",focus="r")]
[charslot(slot="r",posfrom="0,0",posto="-150,0",duration=1.5,block=true)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_2006_1#12$1",focus="r")]
[charslot(slot="r",posfrom="-150,0",posto="0,0",duration=1.5,block=true)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_2006_1#12$

... (全文18463字符)
```

### level_act46side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g11_karlanheadquarters",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[delay(time=1.5)]
[PlaySound(key="$dooropenquite")]
[Delay(time=2)]
空空荡荡的办公室。
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_206_gnosis_1#1$1",afrom=0, ato=1,duration=1)]
[Delay(time=2)]
诺希斯并不熟悉这种感觉，他走近办公桌，桌上杯子里，新倒的咖啡冒着热气，下方压着一张有恩希欧迪斯签名的文件。
[charslot(slot="m",name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]“委任状”。
[charslot(slot="m",name="avg_206_gnosis_1#2$1")]
[name="诺希斯"]不在公司里告别吗......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale",amount=1,fadetime=0,keep=true)]
[charslot(slot="l",name="avg_172_svrash_1#2$1")]
[charslot(slot="r",name="avg_206_gnosis_1#1$1")]
[charslot(slot="l",posfrom="0,0",posto="-60,0",duration=0,block=true)]
[charslot(slot="r",posfrom="0,0",posto="60,0",duration=0,block=true)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = false, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_172_svrash_1#2$1",focus="l")]
[name="恩希欧迪斯"]......文件已经签好了。
[charslot(slot="r",name="avg_206_gnosis_1#1$1",focus="r")]
[name="诺希斯"]你明白这么做的风险。
[charslot(slot="r",name="avg_206_gnosis_1#5$1",focus="r")]
[name="诺希斯"]矿产和土地密不可分，我们绕过蔓珠院，直接与外国合资建设矿区。
[charslot(slot="r",name="avg_206_gnosis_1#7$1",focus="r")]
[name="诺希斯"]未来会有很多麻烦。
[charslot(slot="l",name="avg_172_svrash_1#1$1",focus="l")]
[name="恩希欧迪斯"]如果不在今天付出这些，拉近差距，未来他们只会索要更多。
[charslot(slot="l",name="avg_172_svrash_1#8$1",focus="l")]
[name="恩希欧迪斯"]所以，这已是我们能接受的最低代价。
[charslot(slot="r",name="avg_206_gnosis_1#7$1",focus="r")]
[name="诺希斯"]你的结论未免有些乐观，恩希欧迪斯。
[charslot(slot="l",name="avg_172_svrash_1#1$1",focus="l")]
[name="恩希欧迪斯"]无论对任何事，你从不像我这般乐观。
[charslot(slot="l",name="avg_172_svrash_1#10$1",focus="l")]
[name="恩希欧迪斯"]这意味着很多时候，你能比我走得更远。
[charslot(slot="r",name="avg_206_gnosis_1#4$1",focus="r")]
[name="诺希斯"]......
[charslot(slot="r",name="avg_206_gnosis_1#2$1",focus="r")]
[name="诺希斯"]没有你的那点“乐观”帮忙，我也不会有黑暗中迈出一步的信心。
[charslot(slot="l",name="avg_172_svrash_1#11$1",focus="l")]
[name="恩希欧迪斯"]哼哼。
[charslot(slot="l",name="avg_172_svrash_1#10$1",focus="l")]
[name="恩希欧迪斯"]很久没有听到你恭维什么人了。
[name="恩希欧迪斯"]去完成后面的计划吧，诺希斯。
[charslot(slot="r",name="avg_206_gnosis_1#8$1",focus="r")]
[name="诺希斯"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[stopmusic(fadetime=2)]
[CameraEffect(effect="Grayscale",amount=1,fadetime=0,keep=false)]
[Background(image="45_g11_karlanheadquarters",screenadapt="coverall", block=true)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1161_1#1$1")]
[name="喀兰贸易员工"]中层以上的员工都到齐了，录像也随时可以开始。
[charslot(slot="m",name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]直接开始吧。
[charslot]
[Dialog]
[PlaySound(key="$d_avg_devicebeep")]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1161_1#1$1")]
[name="喀兰贸易员工"]好的，总监，这次公开会议的内容是？
[charslot(slot="m",name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]今日召集大家，是要宣布一项重大的人事变动。
[charslot(slot="m",name="avg_206_gnosis_1#2$1")]
[Dialog]
[Delay(time=1)]
[charslot(slot="m",name="avg_206_gnosis_1#7$1")]
[name="诺希斯"]即日起，恩希欧迪斯·希瓦艾什，将不再担任喀兰贸易的董事长与首席执行官。
[charslot(slot="m",name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]由于近期的业务事故，恩希欧迪斯引咎辞职，董事会已经批准了他的请求。
[name="诺希斯"]同时经董事会决议，本人将接任恩希欧迪斯的全部职务。
[charslot(slot="m",name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]由此，我谨代表董事会，向各位同事与谢拉格民众发表喀兰贸易新时期的第一份声明。
[charslot(slot="m",name="avg_206_gnosis_1#2$1")]
[name="诺希斯"]......
[charslot(slot="m",name="avg_206_gnosis_1#7$1")]
[name="诺希斯"]喀兰贸易将终止和维多利亚方面的一切合作。
[charslot(slot="m",name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]而过去由恩希欧迪斯一意孤行签订的诸多协议，全部暂时搁置，等待董事会做出进一步判断。
[name="诺希斯"]在如此特殊的时刻，我呼吁各位同事坚守岗位，以谢拉格的发展为重，扫清各类遗留的问题。
[charslot(slot="m",name="avg_206_gnosis_1#2$1")]
[multiline(name="诺希斯")]......
[charslot(slot="m",name="avg_206_gnosis_1#7$1")]
[multiline(name="诺希斯")]谢拉格需要我们。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_cellroomA",screenadapt="coverall", block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_npc_283_1#1$1",afrom=0, ato=1,duration=1,block=false)]
[charslot(slot="r",name="avg_npc_284_1#1$1",afrom=0, ato=1,duration=1,block=true)]
[delay(time=2)]
[charslot(slot="l",name="avg_npc_283_1#1$1",focus="l")]
[name="轻浮的谢拉格守卫"]醒醒，我俩来换班了。
[charslot]
[charslot(slot="m",name="avg_npc_286_1#1$1")]
[name="不耐烦的谢拉格守卫"]......真慢。
[charslot]
[charslot(slot="l",name="avg_npc_283_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_284_1#1$1",focus="n")]
[name="轻浮的谢拉格守卫"]这不头一回来，还要找地方呢。
[name="轻浮的谢拉格守卫"]这活儿麻烦吗？
[charslot]
[charslot(slot="m",name="avg_npc_286_1#1$1")]
[name="不耐烦的谢拉格守卫"]别人都不说话，你管管那个领头的老不死就行。
[charslot]
[charslot(slot="l",name="avg_npc_283_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_284_1#1$1",focus="n")]
[name="轻浮的谢拉格守卫"]哪一个？
[name="轻浮的谢拉格守卫"]蔓珠院有谁不是老不死吗？
[charslot]
众人听完哄堂大笑，随后散去，只留下两个值班的守卫。
[charslot(slot="l",name="avg_npc_283_1#1$1",focus="n")]
[charslot(slot="r",name="avg_npc_284_1#1$1",focus="r")]
[name="谨慎的谢拉格守卫"]......说话留点余地，你也是谢拉格人，怎么能对长老出言不逊？
[charslot(slot="l",name="avg_npc_283_1#1$1",focus="l")]
[name="轻浮的谢拉格守卫"]你还为他说话啊？这帮*谢拉格俚语*把我们祸害成这样——
[charslot(slot="r",name="avg_npc_284_1#1$1",focus="r")]
[name="谨慎的谢拉格守卫"]住嘴，不要命啦？
[charslot]
两名守卫不约而同地看向端坐在牢房内的阿德颂长老，他专心于手边厚重的典籍，捻起书页一角，若有所思。
[charslot(slot="l",name="avg_npc_283_1#1$1",focus="n")]
[charslot(slot="r",name="avg_npc_284_1#1$1",focus="r")]
[name="谨慎的谢拉格守卫"]还好，还好。
[cha

... (全文21377字符)
```

### level_act46side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g8_kjeragstreet",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_snowfall",volume=1)]
[Delay(time=2.5)]
远方躁动的轰鸣惊醒了树梢上的寥寥落雪，本该静谧的街道弥漫着一丝不祥的温热。
这里原本是圣山脚下通往蔓珠院的路，此时却有维多利亚的部队横亘道路中央，履带碾过路面，毫不避讳地留下不可逾越的障碍。
战车上的喇叭传出清楚的谢拉格语——
[Dialog]
[PlaySound(key="$radio",channel="o",volume=1)]
[Delay(time=1)]
“谢拉格居民们，请务必不要惊慌，依据维多利亚对当前态势的决策，我们会保障所有人的安全。”
“此次行动不会干扰居民正常生活，只是建议所有人，在这样的天气里待在家中。”
“也警告劫持维多利亚人士的不法分子，以及相关人士，立刻放归人质，否则我们会立刻采取行动！”
[Dialog]
[stopsound(channel="o",fadetime=2)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_279_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="谢拉格老人"]这位先生，可以让我过去对面吗？
[name="谢拉格老人"]我想要回家生火，到吃饭的时间了，我的妻子在等着我......
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="维多利亚士兵"]这里已经封锁了，绕道，或者待在这里。
[charslot(slot="m",name="avg_npc_279_1#1$1",focus="m")]
[name="谢拉格老人"]可......我只是要去马路对面。
[name="谢拉格老人"]您担心安全，检查我身上的东西吧，除了食物，没有别的。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="维多利亚士兵"]你是蔓珠院的人？
[charslot(slot="m",name="avg_npc_279_1#1$1",focus="m")]
[name="谢拉格老人"]我不属于蔓珠院，我只是个铁匠。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="维多利亚士兵"]那么绕路，或者待在这里。
[charslot(slot="m",name="avg_npc_279_1#1$1",focus="m")]
[name="谢拉格老人"]这条道路我走了几十年......
[Dialog]
[charslot]
[name="忧心忡忡的行人"]老人家，不要惹事，没有好处！
[name="阴沉无奈的行人"]快离开那里吧！听他的！
[Dialog]
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="维多利亚士兵"]我不想再说第三遍。
[charslot(slot="m",name="avg_npc_279_1#1$1",focus="m")]
[name="谢拉格老人"]......
[Dialog]
[charslot]
老人蹒跚地离开车队，回头望去，妻子也在橱窗后望着他。
他摆摆手，让妻子离开。
[charslot(slot="m",name="avg_npc_279_1#1$1",focus="m")]
[name="谢拉格老人"]耶拉冈德在上......我愿聆听你的盛怒......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image(image="67_i06",screenadapt="coverall",fadetime=0,block=true)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=45, block=false)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[name="怒不可遏的行人"]你们怎敢入侵我们的土地！赶快滚开！听到了吗？滚出去！
[name="忧心忡忡的行人"]维多利亚人，维多利亚人......这些日子最恨的就是这几个字。
[name="忧心忡忡的行人"]......居然还有人在这时候敢掳他们的人。
[name="阴沉无奈的行人"]看不出来吗，这显而易见只是最卑劣的借口，维多利亚人来了，谢拉格的天要变了......
[name="怒不可遏的行人"]*谢拉格俚语*，不光袖手旁观还讲这些丧气话，比饿了三天的驮兽还没出息，我就帮他们认识认识谢拉格！
[name="忧心忡忡的行人"]你要闹事就离远一点！别让他们以为我是跟你一伙的！
[name="阴沉无奈的行人"]对，对，你去喀兰贸易，他们不是有保安吗？
[name="怒不可遏的行人"]一群废物......
[name="阴沉无奈的行人"]废物？你有勇气，你在所不惜，你有家庭吗？
[name="阴沉无奈的行人"]如果这是谈判的结果，如果三大家族，蔓珠院，喀兰贸易......他们都无所作为，我们能做什么呢？
[name="阴沉无奈的行人"]耶拉冈德在上......请原谅我的畏惧，我的胆怯......
愤怒、畏惧、不安......各种情绪在手无寸铁的人群中弥漫，却无从撼动他们对面全副武装的军队。
直到他们的声音被引擎的轰鸣声淹没。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[Background(image="67_G12_deck",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>“荣光”号甲板</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_2013_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="开斯特亲卫队队长"]阁下，我们的舰队已经完成了对谢拉格雪山入口的包围。
[name="开斯特亲卫队队长"]在谢拉格内部的先遣部队同样严密包围了蔓珠院，谢拉格的武装力量无力对我们发起反抗。
[charslot(slot="m",name="avg_npc_2013_1#4$1",focus="m")]
[name="开斯特亲卫队队长"]谢拉格的圣女，现在不知所终。不过我们会确保，在她露面的第一时间，就锁定她的位置。
[name="开斯特亲卫队队长"]事态没有超出我们的掌控......所以请恕我直言。
[charslot(slot="m",name="avg_npc_2013_1#1$1",focus="m")]
[name="开斯特亲卫队队长"]阁下，您似乎没有必要亲临战场前线。
[charslot(slot="m",name="avg_npc_726_1#1$1",focus="m")]
[name="开斯特公爵"]......不要急躁，菲利帕。
[name="开斯特公爵"]注意你的言辞，我应该纠正过，谢拉格并非是我们的敌人，而是值得我们重视的合作伙伴。
[charslot(slot="m",name="avg_npc_2013_1#1$1",focus="m")]
[name="开斯特亲卫队队长"]可是喀兰贸易，到现在还没有正式回应我们的谈判邀请。
[charslot(slot="m",name="avg_npc_726_1#8$1",focus="m")]
[name="开斯特公爵"]呵呵......我能想象。
[charslot(slot="m",name="avg_npc_726_1#1$1",focus="m")]
[name="开斯特公爵"]恩希欧迪斯是个骄傲的人......想来要他消化这样一场失败，应该是无比艰难的事吧。
[name="开斯特公爵"]菲利帕，你应该多少听说过他的故事，细算来，他也是你的血亲。
[charslot(slot="m",name="avg_npc_2013_1#1$1",focus="m")]
[name="开斯特亲卫队队长"]我不理解，如果他当真如传闻中那样才学出众，又为何放弃留在您身边的机会，而甘愿埋没在这片深山中？
[charslot(slot="m",name="avg_npc_726_1#1$1",focus="m")]
[name="开斯特公爵"]就像我说的，他的确是个骄傲的人。
[name="开斯特公爵"]我可以给他一点时间......六个小时。
[name="开斯特公爵"]如果谢拉格官方还是不肯接受我们的协议，那事情就只能以令人遗憾的方式收场了。
[charslot(slot="m",name="avg_npc_2013_1#1$1",focus="m")]
[name="开斯特亲卫队队长"]明白。
[name="开斯特亲卫队队长"]可是阁下，还有一件不知是否算得上值得在意的小事。
[charslot(slot="m",name="avg_npc_2013_1#4$1",focus="m")]
[name="开斯特亲卫队队长"]那位在明面上已经是死人的布朗陶家的家主，我们又发现了她活动的痕迹。
[charslot(slot="m",name="avg_npc_2013_1#1$1",focus="m")]
[name="开斯特亲卫队队长"]目前她正在黑骑士的保护下藏身在蔓珠院里。
[charslot(slot="m",name="avg_npc_726_1#6$1",focus="m")]
[name="开斯特公爵"]嗯......我想在这种时候，恩希欧迪斯不会大费周章地隐藏一个丝毫不重要的人。
[charslot(slot="m",name="avg_npc_726_1#1$1",focus="m")]
[name="开斯特公爵"]虽然不值一提......但我不喜欢变数。
[name="开斯特公爵"]去找到她。找到她在隐藏的东西。
[charslot(slot="m",name="avg_npc_2013_1#1$1",focus="m")]
[name="开斯特亲卫队队长"]遵命，阁下。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[Background(image="30_ex1_snowmount",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_867_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="“灰礼帽”"]收到，我将执行有限度的调遣，等待进一步指示。
[name="“灰礼帽”"]全体注意，一队守住正面，二队向北门进发，封锁那里，三四队寻找制高点盯住院内。
[name="“灰礼帽”"]所有人，严阵以待，漏出去一个人，等着面见公爵。
[Dialog]
[PlaySound(key="$d_gen_soldiersrun", volume=1)]
[Delay(time=3.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="45_g11_karlanheadquarters",screenadapt="coverall")]
[Delay(tim

... (全文18890字符)
```

### level_act46side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[delay(time=0.5)]
[name="“灰礼帽”"]已到达预定位置。
[name="“灰礼帽”"]公爵的最新指示是，菈塔托丝的诈死必有隐情，她身上很可能带有重要情报，要留活口。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[charslot]
[Background(image="24_g2_temple_indoor",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_867_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="“灰礼帽”"]......
[name="“灰礼帽”"]这里是前院，院内空虚，准备直接突破。
[name="“灰礼帽”"]不要引起注意，力求速战速决。
[name="“灰礼帽”"]唯有一点要当心，黑骑士很有可能还在此处。
[name="“灰礼帽”"]......可是，黑骑士人呢？
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="none")]
入侵者警觉四顾，握紧手中武器。
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[name="“灰礼帽”"]不好！
[Dialog]
[PlaySound(key="$d_avg_spear", volume=1,channel="2")]
[Delay(time=0.4)]
[CameraShake(duration=-1, xstrength=10, ystrength=10, vibrato=60, randomness=90, fadeout=false, block=false)]
[charslot(slot = "m", action="zoom", poszoom = "0.5,0.5", scale=0.9, duration = 0.35)]
[charslot(slot = "m", afrom=1,ato=0, duration = 0.5)]z
[PlaySound(key="$d_avg_janttck_03", volume=1,channel="1")]
[bgeffect(name = "$eb_windburst" ,layer = 1)]
[Delay(time=0.2)]
[CameraShake(duration=1.5, xstrength=20, ystrength=20, vibrato=60, randomness=90, fadeout=false, block=false)]
[PlaySound(key="$d_avg_explosion_stone", volume=1)]
[Blocker(a=0.2, r=1, g=1, b=1, fadetime=1.5, block=true)]
一支黑色的锏以不可思议的速度飞袭而来，入侵者被巨大的力道击飞，重重撞在墙上。
[Dialog]
[Blocker(a=0.2, r=1, g=1, b=1, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="24_g5_guestroom",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_253_1#7$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_2006_1#12$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="r",name="avg_npc_2006_1#6$1",focus="r")]
[name="阿尔贝塔"]啊......！
[charslot(slot="r",name="avg_npc_2006_1#12$1",focus="r")]
[name="阿尔贝塔"]我听到外面......又有打斗的声音——到底发生了什么事？
[charslot(slot="l",name="avg_npc_253_1#7$1",focus="l")]
[name="菈塔托丝"]小点声！
[name="菈塔托丝"]现在外面都是最危险的敌人，那位锏在拼了命地保护我们。
[name="菈塔托丝"]你现在唯一能做的事，就是安静点，别让他们发现我们。
[charslot(slot="r",name="avg_npc_2006_1#12$1",focus="r")]
[name="阿尔贝塔"]我......我听到广播里说，我是被谢拉格挟持的人质？为什么......
[charslot(slot="l",name="avg_npc_253_1#9$1",focus="l")]
[name="菈塔托丝"]呵......你的维多利亚同胞现在正带着武器，开着战车，将这里围得水泄不通。
[name="菈塔托丝"]所以，是想要救你出去，还是要把知情者围困在这里以便展开其他行动，答案显而易见。
[charslot(slot="r",name="avg_npc_2006_1#11$1",focus="r")]
[name="阿尔贝塔"]你的意思是，他们用救我的借口，入侵谢拉格......
[charslot(slot="l",name="avg_npc_253_1#7$1",focus="l")]
[name="菈塔托丝"]这是你自己说的......不过现实差不多就是如此。
[charslot(slot="r",name="avg_npc_2006_1#12$1",focus="r")]
[name="阿尔贝塔"]......
[name="阿尔贝塔"]......怎么会变成这样？
[charslot(slot="l",name="avg_npc_253_1#2$1",focus="l")]
[name="菈塔托丝"]如果你的资料能传出去，你也可以向你的国家问问这个问题。
[charslot(slot="r",name="avg_npc_2006_1#12$1",focus="r")]
[name="阿尔贝塔"]我以为我来到谢拉格，可以为受压迫的人们带来帮助......我的镜头与文章，可以让更多人看到真实的谢拉格。
[name="阿尔贝塔"]我原本相信我做的这一切都是有意义的......
[charslot(slot="l",name="avg_npc_253_1#7$1",focus="l")]
[name="菈塔托丝"]......我是不是还该感谢你的好心？
[multiline(name="菈塔托丝")]好吧，我就当你是真的好心吧——
[charslot(slot="l",name="avg_npc_253_1#8$1",focus="l")]
[multiline(name="菈塔托丝")]别犯傻了，你凭什么觉得，你看到的就是“真实的谢拉格”？
[charslot(slot="l",name="avg_npc_253_1#7$1",focus="l")]
[name="菈塔托丝"]现状你也看到了，在压迫谢拉格人民的到底是谁？
[charslot(slot="r",name="avg_npc_2006_1#12$1",focus="r")]
[name="阿尔贝塔"]......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[Background(image="24_g2_temple_indoor",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[PlaySound(key="$blooddrop", volume=1)]
[Delay(time=1)]
[PlaySound(key="$blooddrop", volume=1)]
[Delay(time=1)]
屋檐上的融雪化为庭院中的积水，入侵者的血溅落出道道涟漪。
他的前方，逆光而来的暗沉面孔正直视着他。
不远处，堂厅内的烛火像是挣扎未释的杀气，激荡、翻涌......
[Dialog]
[PlaySound(key="$d_avg_sandstone", volume=1)]
[charslot(slot="m",name="avg_npc_867_1#1$1", afrom=0, ato=1, duration=1)]
[charslot(slot="m", posfrom="0,-30", posto="0,0", duration=1.5)]
[Delay(time=2.5)]
[name="“灰礼帽”"]这样的战力，怪不得那位在对谢拉格的报告中特意强调了黑骑士的存在。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_4116_blkkgt_1#6$1",duration=1.5)]
[PlayMusic(intro="$blkswb_intro", key="$blkswb_loop", volume=0.6)]
[Delay(time=2)]
[name="锏"]早知道你们会偷摸闯进来。
[name="锏"]你......哼，反正我也分不清你们这些面具下面到底谁是谁。
[charslot(slot="m",name="avg_4116_blkkgt_1#6$1",focus="m")]
[name="锏"]你们那个来过谢拉格的同事，难道没有告诉过你们，谢拉格不是能随便侵犯的土地？
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[name="“灰礼帽”"]是的，我们的确听说过你的大名。
[name="“灰礼帽”"]所以我们也做好了充分的准备......
[Dialog]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=0.2, block=true)]
[charslot(slot="l",name="avg_npc_867_1#1$1")]
[charslot(slot="r",name="avg_npc_867_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=0.2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_gen_soldiersrun", volume=1)]
[charslot(slot="l",afrom=1, ato=0, duration=0.6)]
[charslot(slot="l",posfrom="0,0", posto="-200,0", duration=1)]
[charslot(slot="r",afrom=1, ato=0, duration=0.6)]
[charslot(slot="r",posfrom="0,0", posto="200,0", duration=1)]
[Delay(time=2.5)]
[charslot]
[charslot(slot="m",name="avg_4116_blkkgt_1#10$1",focus="m")]
[name="锏"]原来是想靠数量取胜。
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[name="“灰礼帽”"]没有人打算和你争胜，只是任务而已。
[charslot(slot="m",name="avg_4116_blkkgt_1#2$1",focus="m")]
[name="锏"]能穿上这身衣服的，算是精英。
[c

... (全文35510字符)
```

### level_act46side_10_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_explosion_stone")]
[Background(image="67_G7_cave",screenadapt="coverall", block=true)]
[Delay(time=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
随着一声爆破声响，岩壁坍塌，一个幽深的山洞出现在众人面前。
[Dialog]
[PlaySound(key="$d_avg_marblefootsteps_loop")]
[charslot(slot="m",name="avg_1047_halo2_1#1$1",afrom=0, ato=1,duration=2)]
[delay(time=3)]
[charslot(slot="m",name="avg_1047_halo2_1#4$1")]
[name="埃琳娜"]果然......这里看上去可以通向更深处。
[charslot(slot="m",name="avg_1047_halo2_1#17$1")]
[name="埃琳娜"]我们只能看到洞口一带......还需要深入探索。
[charslot(slot="m",name="avg_1047_halo2_1#5$1")]
[name="埃琳娜"]恩雅？
[charslot]
询问声在洞中回响，圣女没有回答，她看到方才喋喋不休的老者，现在却紧紧抿住嘴唇。
[Dialog]
[PlayMusic(intro="$dignified_intro", key="$dignified_loop",volume=0.6)]
[charslot(slot="m",name="avg_174_slbell_1#3$1",afrom=0, ato=1,duration=1)]
[delay(time=2)]
[name="恩雅"]“不要求于我的殿，而要求于我的心。”
[charslot(slot="m",name="avg_174_slbell_1#1$1")]
[name="恩雅"]......阿德颂长老，我在等您。
[charslot(slot="m",name="avg_npc_1998_1#7$1")]
[name="阿德颂"]......
他的双腿像是苍老的树根，干涸的咽喉像是旱季的浅池。
他一动不动地伫立在原地......
[name="阿德颂"]......我守在此处，等待你们进去做完你们该做的事。
[charslot(slot="m",name="avg_1047_halo2_1#5$1")]
[name="埃琳娜"]但你不是和恩雅还有约定，要证明里面没有耶拉冈德吗？
[charslot(slot="m",name="avg_1047_halo2_1#17$1")]
[name="埃琳娜"]如果你不和我们一起——
[charslot(slot="m",name="avg_npc_1998_1#3$1")]
[name="阿德颂"]我已经言明，我会守在外面。
[charslot(slot="m",name="avg_npc_1998_1#7$1")]
[name="阿德颂"]如果祂真的存在，也应该是祂自己出来现身。
[charslot(slot="m",name="avg_174_slbell_1#6$1")]
[name="恩雅"]长老......
[charslot(slot="m",name="avg_174_slbell_1#7$1")]
[name="恩雅"]或许，比起探明真相，您宁可对祂存在的证明视而不见。
[charslot(slot="m",name="avg_npc_1998_1#7$1")]
[name="阿德颂"]......我，不可能......绝不能......
[charslot(slot="m",name="avg_npc_1998_1#3$1")]
[name="阿德颂"]这里没有答案......
[charslot(slot="m",name="avg_174_slbell_1#6$1")]
[name="恩雅"]那您为什么将我们带到此处，却不愿见证真相呢？
[charslot(slot="m",name="avg_npc_1998_1#7$1")]
[name="阿德颂"]......
[charslot(slot="m",name="avg_npc_1998_1#3$1")]
[name="阿德颂"]不，祂绝不能存在。
[charslot(slot="m",name="avg_npc_1998_1#1$1")]
[name="阿德颂"]希瓦艾什的长女，还有你，你们，不要假装没有看到。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.8, block=true)]
[charslot]
[CameraEffect(effect="Grayscale",amount=1,fadetime=0,keep=true)]
[Background(image="67_G10_kjeragwilde_n",screenadapt="coverall", block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[delay(time=0.8)]
[name="阿德颂"]用冻僵手指鞣制皮草的猎户，呛着灰尘的拾荒者，还有那些肌肤皲裂的矿石病患。
[multiline(name="阿德颂")]你可见过，因久跪在泥地里膝盖磨出鲜血的他们，只为恳求耶拉冈德拯救......
[multiline(name="阿德颂")]不，甚至是早日结束自己悲苦的生命......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.8, block=true)]
[charslot]
[Background(image="24_g11_snowylane",screenadapt="coverall", block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[delay(time=0.8)]
[name="阿德颂"]当你们蜷缩在温暖的房屋里推杯换盏，是我，是蔓珠院，踏遍你们都不愿扫视的禁区，以及那些最穷苦人的居所。
[name="阿德颂"]是我让他们重归宁静，是我不断复述着“没有人被放弃”......“即使生来活在漫漫长夜里，还有神在爱着你们”......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.8, block=true)]
[charslot]
[Background(image="45_g9_underkjerastastue",screenadapt="coverall", block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[delay(time=0.8)]
[name="阿德颂"]是我们建起了能让人带着微笑而死去的国度，但你们，但耶拉冈德——
[name="阿德颂"]这翻云覆雨的宗长，这以万物为牲畜的君王，祂明明可以，也应当救下那些人，救下整个谢拉格。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.8, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=1,fadetime=0,keep=false)]
[Background(image="67_G7_cave",screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_npc_1998_1#7$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[delay(time=0.8)]
[charslot(slot="m",name="avg_npc_1998_1#7$1")]
[name="阿德颂"]祂却无动于衷，每过一阵子略施所谓的奇迹宣告自己的王权......
[CameraShake(duration=0.4, xstrength=50, ystrength=50, vibrato=60, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1998_1#6$1")]
[name="阿德颂"]凭什么最后得救的都是少数人？！
[name="阿德颂"]现在，你们居然要去见这位魔鬼和暴君，去求祂来否定我，否定我们苦心经营的秩序。
[charslot(slot="m",name="avg_npc_1998_1#5$1")]
[name="阿德颂"]我，绝不能——
[Dialog]
[delay(time=1)]
[PlaySound(key="$bodyfalldown3")]
[charslot(slot="m",name="avg_npc_1998_1#5$1",posfrom="0,0",posto="0,-150",afrom=1,ato=0,duration=1,block=true)]
[delay(time=1)]
[charslot]
还有什么可以支撑一个老人？他瘦弱的身躯像是被无形的巨锤击中，他跌倒在泥土中，失声痛哭。
[name="阿德颂"]......你们说话，你们告诉我。
[CameraShake(duration=0.3, xstrength=40, ystrength=40, vibrato=40, randomness=90, fadeout=true, block=false)]
[name="阿德颂"]祂凭什么不知道，祂凭什么不理解？
[name="阿德颂"]你们又凭什么可以沉默......
[charslot]
[charslot(slot="l",name="avg_1047_halo2_1#18$1",focus="l")]
[charslot(slot="r",name="avg_4211_snhunt_1#10$1",focus="n")]
[name="埃琳娜"]这......
[charslot(slot="r",name="avg_4211_snhunt_1#10$1",focus="r")]
[name="茱安娜"]大长老他......到底怎么了......
[charslot]
[charslot(slot="m",name="avg_174_slbell_1#3$1")]
[name="恩雅"]阿德颂长老......我可以理解您。
[charslot(slot="m",name="avg_174_slbell_1#7$1")]
[name="恩雅"]我们不被允许目睹“神明”的真容，只能通过祂的训诫、祂的造物来描绘祂的存在。
[charslot(slot="m",name="avg_174_slbell_1#1$1")]
[name="恩雅"]但我认为，我依然是愿意相信的......
[charslot(slot="m",name="avg_174_slbell_1#1$1")]
[name="恩雅"]无论我在这个洞穴的另一头看到了什么，我的信仰都不会动摇——祂传授的美德与戒律，知识与智慧，这些都是有意义的。
[charslot(slot="m",name="avg_174_slbell_1#3$1")]
[Dialog]
[delay(time=1)]
[multiline(name="恩雅")]而我只是想看清......
[charslot(slot="m",name="avg_174_slbell_1#7$1")]
[multiline(name="恩雅")]谢拉格的人们，来时的路。
[Dialog]
[PlaySound(key="$d_avg_marblefootsteps_loop")]
[charslot(slot="m",name="avg_174_slbell_1#7$1",afrom=1, ato=0,duration=1.5)]
[delay(time=3.5)]
[charslot]
没有任何犹疑，恩雅转身走入了幽深的洞穴中，走向了信仰的方向。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=2.5)]
[delay(time=1)]
[charslot]
[Background(image="67_G12_deck",screenadapt="coverall", block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2,

... (全文34125字符)
```

### level_act46side_10_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Background(image="67_G6_karlanlake",screenadapt="coverall", block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="67_G6_karlanlake",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(key="$kjerag_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
风雪渐渐停了。
广袤的、宁静的雪原之上，蔚蓝色的湖泊闪烁着光辉。
谢拉格的冬日寒冷，水自然结冰，但它依旧柔软，水面如镜子一般倒映着天空的蓝色。
一个人出现在湖的中心。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_174_slbell_1#6$1",duration=1.5)]
[Delay(time=2)]
[name="恩雅"]......雅儿......
[name="恩雅"]雅儿？是你吗？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_2009_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="耶拉冈德"]恩雅......
[charslot(slot="m",name="avg_174_slbell_1#7$1",focus="m")]
[name="恩雅"]雅儿......？
[name="恩雅"]我到底该怎么称呼你......雅儿，还是耶拉冈德？
[charslot(slot="m",name="avg_npc_2009_1#1$1",focus="m")]
[name="耶拉冈德"]你呀......难道不记得了吗？
[name="耶拉冈德"]耶拉冈德，是过去的人们为我起的名字。
[charslot(slot="m",name="avg_npc_2009_1#6$1",focus="m")]
[name="耶拉冈德"]但是雅儿，永远是恩雅的侍女长。
[charslot(slot="m",name="avg_174_slbell_1#7$1",focus="m")]
[name="恩雅"]......
[Dialog]
[charslot]
漫长的旅途之中，恩雅曾有许多话想说。
那些想法和等着询问的句子在她脑海中摇荡，如同一个装满水的罐子，时不时发出声响，经历天长地久，此时打开，却发现早已干涸。
该说些什么呢？能说些什么呢？
[Dialog]
[charslot(slot="l",name="avg_npc_2009_1#6$1",duration=1.5)]
[charslot(slot="r",name="avg_174_slbell_1#7$1",duration=1.5)]
[Delay(time=3)]
[charslot(slot="r",name="avg_174_slbell_1#7$1",focus="none")]
她追寻的友人站定在她身前，温暖的双手接触到她的面颊与鼻尖。一如往日。
[charslot(slot="l",name="avg_npc_2009_1#1$1",focus="l")]
[name="耶拉冈德"]虽然算不上意外，可我还是很惊喜，你最终还是找到了这里。
[charslot(slot="r",name="avg_174_slbell_1#6$1",focus="r")]
[name="恩雅"]雅儿，我真的很担心你......
[name="恩雅"]我不知道你去了哪里，天灾发生后人们也都很惶恐......我只好作为圣女开始“圣巡”。
[charslot(slot="r",name="avg_174_slbell_1#7$1",focus="r")]
[name="恩雅"]我走过了许多地方......终于在圣山上发现了这一处遗迹。
[charslot(slot="l",name="avg_npc_2009_1#3$1",focus="l")]
[name="耶拉冈德"]你是说......你在这个季节进行“圣巡”？你——你是笨蛋吗？！
[charslot(slot="r",name="avg_174_slbell_1#7$1",focus="r")]
[name="恩雅"]我......
[charslot(slot="l",name="avg_npc_2009_1#5$1",focus="l")]
[name="耶拉冈德"]啊，对不起......作为侍女长，不该这样和圣女大人说话的。
[charslot(slot="l",name="avg_npc_2009_1#1$1",focus="l")]
[name="耶拉冈德"]恩雅......你没事就好。
[charslot(slot="l",name="avg_npc_2009_1#1$1",focus="none")]
朋友的声音和往日一样亲切，口吻一如从前。
[charslot(slot="r",name="avg_174_slbell_1#6$1",focus="r")]
[name="恩雅"]雅儿......
[name="恩雅"]我刚刚看到的那些画面，都是谢拉格的过去吗？
[charslot(slot="l",name="avg_npc_2009_1#2$1",focus="l")]
[name="耶拉冈德"]是的......那些都是我的记忆。
[name="耶拉冈德"]在不知多少年之前，我与这片土地上的人们一同生活的记忆。也是谢拉格，成为今天的谢拉格的故事。
[charslot(slot="l",name="avg_npc_2009_1#7$1",focus="l")]
[name="耶拉冈德"]你来到了耶拉冈德体内的禁地，所以你能通过耶拉冈德的眼睛，看到这上千年的过去。
[charslot(slot="r",name="avg_174_slbell_1#6$1",focus="r")]
[name="恩雅"]我现在......是在耶拉冈德的体内？
[charslot(slot="l",name="avg_npc_2009_1#1$1",focus="l")]
[name="耶拉冈德"]打个比方的话，就像是从我的臂膀，爬到了我胸膛的位置。
[charslot(slot="r",name="avg_174_slbell_1#7$1",focus="r")]
[name="恩雅"]这个湖泊......是幻象吗？
[name="恩雅"]这里就是......“喀兰之心”？
[charslot(slot="l",name="avg_npc_2009_1#2$1",focus="l")]
[name="耶拉冈德"]“喀兰之心”，其实就是这个湖泊的名字。你看到的，就是它千年前的模样。
[name="耶拉冈德"]千年前，藏匿于群山深处，终年不会冻结的湖泊。
[name="耶拉冈德"]当时颠沛流离的人们发现了这一处珍贵的水源，于是在这里扎根繁衍。人们将它比作心脏。
[charslot(slot="l",name="avg_npc_2009_1#7$1",focus="l")]
[name="耶拉冈德"]“心脏跳动，喀兰的血肉开始滋长。”
[charslot(slot="r",name="avg_174_slbell_1#10$1",focus="r")]
[name="恩雅"]所以，人们在这里建起了祭坛，为了纪念耶拉冈德赐福于他们的神迹......
[name="恩雅"]我在遗迹里看到了那个雕像，很大，很精美。
[charslot(slot="r",name="avg_174_slbell_1#7$1",focus="r")]
[name="恩雅"]不像银心湖旁，参考典籍建造的塑像，那是真的见过“你”的人才能做出来的东西吧？
[name="恩雅"]雅儿......你到底，是什么？
[charslot(slot="l",name="avg_npc_2009_1#1$1",focus="l")]
[name="耶拉冈德"]唔......这真是一个令人头疼的问题呀......
[charslot(slot="l",name="avg_npc_2009_1#7$1",focus="l")]
[name="耶拉冈德"]很长一段时间以来，我只知道自己体型庞大，与山川无异。
[charslot(slot="l",name="avg_npc_2009_1#2$1",focus="l")]
[name="耶拉冈德"]这片大地上曾经也有不少我的同类，早在那一次黑暗降临之前，它们也曾拥有过之前的生灵为它们赋予的名字。
[name="耶拉冈德"]“巨兽”“行星之子”“大地的主人”......
[charslot(slot="l",name="avg_npc_2009_1#1$1",focus="l")]
[name="耶拉冈德"]相比之下，我的年纪并不比你们当中最古老的文明年长多少......
[name="耶拉冈德"]如果让我来讲的话，我倒更情愿，将自己当作一种“生命”。我也更喜欢，耶拉冈德这个名字。
[name="耶拉冈德"]但很可惜，我并不是人们渴求的，那个可以支配一切的“神明”......
[charslot(slot="r",name="avg_174_slbell_1#7$1",focus="r")]
[name="恩雅"]可是人们还是将你当作了神明。人们相信你制定的戒律，也将一切祸福全都归因于你......
[name="恩雅"]还有那些圣女，她们......
[charslot(slot="l",name="avg_npc_2009_1#8$1",focus="l")]
[name="耶拉冈德"]那不是我的本意。
[name="耶拉冈德"]我曾经一度沉睡，可似乎是我的离开让人们惶恐，他们在寻找、唤醒我的路途中陷入迷茫......
[name="耶拉冈德"]我封存了这里，是希望人们可以忘记那很长一段时间以来的错误。
[charslot(slot="r",name="avg_174_slbell_1#2$1",focus="r")]
[name="恩雅"]我知道，我当然知道了！
[name="恩雅"]你又不是什么邪恶的、阴暗的、看着无辜女孩在面前失温还会笑嘻嘻的坏家伙......
[charslot(slot="r",name="avg_174_slbell_1#2$1",focus="none")]
恩雅抬起手，将面颊上温暖的触碰握在手中。
[charslot(slot="l",name="avg_npc_2009_1#8$1",focus="l")]
[name="耶拉冈德"]我并非人们需要的那个神明......我也从未制定过什么戒律......
[name="耶拉冈德"]我也不过是无端降生在这片大地上的生灵之一，我又何来教导人们生存下去的智慧......
[charslot(slot="l",name="avg_npc_2009_1#1$1",focus="l")]
[name="耶拉冈德"]可是在我以人的姿态与人们同行的时候，却意外发现，你们的族群虽然渺小脆弱，但是拥有着一种与生俱来的天赋，近乎本能的力量——
[name="耶拉冈德"]可以让你们彼此帮助，克服一切艰难险阻，在这片险恶的大地上生存下去。
[name="耶拉冈德"]在你们的语言中，将这种力量，称为“美德”。
[charslot(slot="r",name="avg_174_slbell_1#7$1",focus="r")]
[name="恩雅"]竟然......是这样......
[charslot(slot="l",name="avg_npc_2009_1#1$1",focus="l")]
[name="耶拉冈德"]我并非你们的导师，应该说，是你们教会了我生命的意义才对。
[name="耶拉冈德"]至于耶拉冈德这个名字，祂代表的形象，是属于人的造物。
[name="耶拉冈德"]但我也并不觉得这是一种谎言。只不过是借由耶拉冈德这个名字，让你们原本就拥有的力量得以显现罢了。
[charslot(slot="l",name="avg_npc_2009_1#6$1",focus="l")]
[name="耶拉冈德"]我想......这就是你在寻找的耶拉冈德吧。
[charslot(slot="r",name="avg_174_slbell_1#3$1",focus="r")]
[name="恩雅"]“祂说，我的路，终究是你们的路......”
[charslot(slot="r",name="avg_174_slbell_1#7$1",focus="r")]
[name="恩雅"]人们追问祂的模样，归根结底，也只是为了认清自身。
[name="恩雅"]可是人们走过的路绝大多数都并非坦途，更多时候，人们还是像晕头转向的驮兽一样原地绕圈打转......
[name="恩雅"]曾经，谢拉格人把你带回了我们之间，我们的信仰也随之稳固......
[name="恩雅"]......
[charslot(slot="r",name="avg_174_slbell_1#6$1",focus="r")]
[name="恩雅"]雅儿......这一次，你还会回来吗？
[charslot(slot="l",name="avg_npc_2009_1#5$1",focus="l")]
[name="耶拉冈德"]恩雅......
[charslot(slot="l",name="avg_npc_2009_1#8$1",focus="l")]
[name="耶拉冈德"]或许......这一次，我不能再陪在你身边

... (全文42115字符)
```

### level_act46side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act46side/OS01.mp4")]
```

### level_act46side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_manorindoor",screenadapt="coverall", block=true)]
[focusout(duration=0.1, type="bg", from=0, to=1, block=true)]
[Delay(time=1)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.6)]
[PlaySound(key="$d_avg_banquet_amb", volume=1, loop=true, channel="wy")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="优雅的青年"]......我想你错了，先生。
[name="优雅的青年"]或许维多利亚当下依然是这片大地上最强大的国家，但这并不意味着这样的繁荣是理所当然的常态。
[name="优雅的青年"]那场战争过后，维多利亚在高卢遗产的滋养下度过了黄金般的四十年......我们对这段历史都不陌生。
[name="优雅的青年"]但时过境迁，当曾经先进的生产力不再是独一无二的优势，维多利亚无法再消化对外扩张的野心，内部分裂的隐患才开始显现。
[name="优雅的青年"]那位陛下试图调停工厂与商人间根深蒂固的矛盾，却没有在两难的局面中提出一种新的出路。
[name="优雅的青年"]他的结局就是一种必然——无独有偶，紧随其后发生在莱塔尼亚的政变同样能佐证这一点。
[name="优雅的青年"]谁才是流血斗争中的胜利者？不......狮王被推上绞刑架已经过去了十余年之久，政变的余波却一直蔓延到今日。
[name="优雅的青年"]“布莱顿的麦子”“默西河事件”，十余年来公爵之间何曾停止过旧利益切割的纷争？
[name="优雅的青年"]每个人都相信自己能够在斗争中得利，而没有人相信这是属于维多利亚的死局。
[name="优雅的青年"]如果不能及时做出改变，维多利亚在下一个时代的主题，恐怕会是愈演愈烈的内战。
[Dialog]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs1",volume=0)]
[SoundVolume(volume=0.5, channel="bgs1",fadetime=2.5)]
[delay(time=2)]
......
[Dialog]
[delay(time=1)]
[name="有权势的长者"]我听说，今天有一位格外能言善辩的青年，抢过了所有人的风头。
[name="有权势的长者"]看上去你简直像是今天这场宴会的主角。
[Dialog]
[StopSound(channel="bgs1", fadetime=2)]
[delay(time=1)]
[name="优雅的青年"]无意冒犯，尊敬的开斯特公爵阁下。
[name="优雅的青年"]我本期待在大公爵的府邸上结识更多的有识之士，可不得不承认，我现在有些失望。
[name="开斯特公爵"]哦？或许在你看来，你能够胜任公爵的内阁幕僚，甚至是议会的议长。
[name="优雅的青年"]指出这个国家问题的症结并不算难事，但是要解决问题，则需要一点手段，甚至是一点时运。
[name="优雅的青年"]不过暂时来看，这也不该是我考虑的问题，您觉得呢？
[name="开斯特公爵"]呵......
[name="开斯特公爵"]我记得你的母亲......你并没有学会她的谦逊和礼节，倒是继承了她大胆轻佻的性格。
[name="开斯特公爵"]......恩希欧迪斯。
[Dialog]
[SoundVolume(volume=0.5, channel="wy",fadetime=2.5)]
[image(image="67_i01",screenadapt="coverall",xScale=1.3,yScale=1.3,y=-50,fadetime=2.5)]
[ImageTween(yFrom=-50, xTo=0, yTo=0, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1, yScaleTo=1, duration=25, block=false)]
[delay(time=3)]
[name="恩希欧迪斯"]如果不用这种方式博得您的注意，您恐怕也不会有兴趣关注一位来自异国的远亲。
[name="开斯特公爵"]有煽动性的演讲，但几句高谈阔论还不足以成为你的立身之本。
[name="开斯特公爵"]曾经有不少锋芒毕露的年轻人到访过这座府邸，只为在满堂宾客间博一个名声，好接下来在风流场上享受他人的追捧。
[name="开斯特公爵"]我要如何相信你不是其中之一？
[name="恩希欧迪斯"]我无意成为维多利亚贵族的座上宾，我只想向您，提出一个交易的申请。
[name="恩希欧迪斯"]谢拉格与开斯特公爵领，资源与工业可以达成完美的互补，二者会成为平等的合作伙伴。
[name="恩希欧迪斯"]我正在创立谢拉格的第一家跨国贸易公司，这是我向您提出的邀请。
[name="开斯特公爵"]......“平等”？
[name="恩希欧迪斯"]平等。
[name="恩希欧迪斯"]我可以向您保证，在三十年内，谢拉格就会成为泰拉版图上不可忽视的一股势力。
[name="恩希欧迪斯"]届时，两国之间的合作，对双方都只会有利无害。
[name="开斯特公爵"]勇气可嘉。
[name="开斯特公爵"]可是我看不出你有任何资本向我做出这样的承诺，孩子。
[name="恩希欧迪斯"]您会同意的。
[name="恩希欧迪斯"]作为一名有远见的政治家，您不会不知晓维多利亚当前的困境，或者说，“开斯特公爵”的困境。
[name="恩希欧迪斯"]一项举措，哪怕只有微小可能性可以为局面带来一丝改善，您也不该放过。
[name="恩希欧迪斯"]如今我站在您的面前，足以证明我是一个值得您投资的对象。
[name="开斯特公爵"]......你应该感谢自己的年轻，这样的锋芒还不至于招来我的厌恶。
[Dialog]
[delay(time=1)]
[name="开斯特公爵"]那么，年轻又有远见的政治家，能否用你的聪明才智回答我。
[name="开斯特公爵"]一个源石电路都尚未普及的国家，要如何在三十年内成为这片大地上“不可忽视的势力”？
[name="恩希欧迪斯"]我理解您的质疑，工业与科技，它们都很重要——但对于一个国家而言，有更重要的事物。
[name="恩希欧迪斯"]恕我直言，因为维多利亚政局的特殊性，您或许不曾想象，一个团结的国度可以爆发出多么惊人的力量。
[name="恩希欧迪斯"]我相信——
[Dialog]
[StopSound(channel="wy", fadetime=2)]
[stopmusic(fadetime=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[image]
[focusout(duration=0.1, type="bg", from=1, to=0, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Sticker(id="st1", multi = true, text="最后，祂站在最高的山峰上，指着远处的湖泊说：", x=300,y=150, alignment="center", size=24, delay=0.04, width=750,block = true)]
[Sticker(id="st1", multi = true, text="\n\n“你们要记得来时的路，不可忘却；",block = true)]
[Sticker(id="st1", multi = true, text="\n\n你们要敬畏未至的风雪，不可轻信己见；",block = true)]
[Sticker(id="st1", multi = true, text="\n\n要握紧手中的弓箭、镐头和种子，不可松懈；",block = true)]
[Sticker(id="st1", multi = true, text="\n\n要爱自己的兄弟姐妹，爱你的邻人与朋友、爱山石草木如同爱自己的兄弟姐妹那般。",block = true)]
[Sticker(id="st1", multi = true, text="\n\n你们若依此律，大地上将不再有灾难降于你们，你们定能家园永固。”",block = true)]
[Sticker(id="st1", multi = true, text="\n\n......",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="24_g3_mainhall",screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[PlaySound(key="$d_avg_woodcracle", volume=0.4, loop=true, channel="a")]
[PlaySound(key="$d_avg_drtywndblw", volume=0.7)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1998_1#4$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1998_1#4$1",focus="m")]
[name="蔓珠院长老"]圣女大人，时候差不多了......
[charslot(slot="m",name="avg_174_slbell_1#6$1",focus="m")]
[name="恩雅"]医生......还是没有办法吗？
[charslot(slot="m",name="avg_npc_1998_1#4$1",focus="m")]
[name="蔓珠院长老"]这几年来，不管是谢拉格还是维多利亚的医生，都已经试遍了各种方式来清除大长老身体里的余毒。
[name="蔓珠院长老"]可最终，将要夺走他生命的并非病痛，而是时间。
[charslot(slot="m",name="avg_174_slbell_1#7$1",focus="m")]
[name="恩雅"]我知道了......
[Dialog]
[delay(time=1)]
[charslot(slot="m",name="avg_174_slbell_1#7$1",focus="m")]
[name="恩雅"]我现在......可以进去看望他了吗？
[charslot(slot="m",name="avg_npc_1998_1#4$1",focus="m")]
[name="蔓珠院长老"]当然......
[name="蔓珠院长老"]耶拉冈德在上......请圣女大人，为大长老送行。
[Dialog]
[stopsound(channel="a", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="24_g5_guestroom",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlaySound(key="$dooropenquite", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
恩雅轻轻地推开了门。
垂暮的老人躺在病榻上，干瘪的胸腔几乎看不出任何起伏。他似是听到了响动，努力将耳朵偏向一侧，然后气若游丝地开口。
[name="大长老"]恩雅......是你吗......？
[Dialog]
[charslot(slot="m",name="avg_174_slbell_1#7$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_174_slbell_1#7$1",focus="m")]
[name="恩雅"]大长老......
[name="恩雅"]您感觉怎么样？要不要喝些水......


... (全文25630字符)
```

### level_act46side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g12_mountpath",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_snowstormflp", volume=0.6, loop=true, channel="wind")]
[PlayMusic(key="$kjerag_loop", volume=0.6)]
[bgeffect(name="$eb_blizzard", layer=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
枯瘦的树枝覆上一层白雪，裂云兽窜上枯枝前端，挤着双眼，一副严肃探查的模样。
圣女轻声叹息，她停下脚步回头望去，身后不远处紧跟着她的猎手一怔，脸颊被风刮得泛红。
[Dialog]
[charslot(slot="m",name="avg_npc_2010_1#12$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_2010_1#12$1",focus="m")]
[name="恩雅"]茱安娜......你不必跟着我。
[name="恩雅"]你所做的一切，我感激不尽。
[name="恩雅"]但是，我出发前也和你说过，“圣巡”必须独身一人完成，甚至与你对话已经是破例。
[charslot(slot="m",name="avg_4211_snhunt_1#1$2",focus="m")]
[name="茱安娜"]我知道。
[name="茱安娜"]我没有跟着您，不是您的护卫和侍从，我只是恰好和您同路。
[name="茱安娜"]放心，我不会和您说话，要是有人看到我们，我就装作不认识您。
[name="茱安娜"]我绝对不会再让您陷入那样的危险的，我就一直在您后面跟着您。
[charslot(slot="m",name="avg_npc_2010_1#1$1",focus="m")]
[name="恩雅"]那茱安娜知道我要去哪里吗？
[charslot(slot="m",name="avg_4211_snhunt_1#3$2",focus="m")]
[name="茱安娜"]您去哪里我都要跟着，我知道这个就行了。
[charslot(slot="m",name="avg_npc_2010_1#12$1",focus="m")]
[name="恩雅"]但......我要去找耶拉冈德。
[charslot(slot="m",name="avg_4211_snhunt_1#5$2",focus="m")]
[name="茱安娜"]啊？
[charslot(slot="m",name="avg_4211_snhunt_1#9$2",focus="m")]
[name="茱安娜"]找祂......祂消失了吗？！
[charslot(slot="m",name="avg_npc_2010_1#12$1",focus="m")]
[name="恩雅"]我不知道......但除非祂能再临，否则谢拉格还会面临像上次那般的灾厄。
[name="恩雅"]到那时候，有人会失去生命，更多的人会失去信念......
[name="恩雅"]现在，我要先回到蔓珠院，在典籍中寻找新的方向，这一点要先瞒着其他人。
[charslot(slot="m",name="avg_4211_snhunt_1#11$2",focus="m")]
[name="茱安娜"]那我也要跟着您，您放心，要是有人发现了您的踪迹，我就帮您赶走——
[Dialog]
[charslot(slot="m",name="avg_4211_snhunt_1#11$2",focus="n")]
“咕噜咕噜”——
[charslot(slot="m",name="avg_4211_snhunt_1#5$2",focus="m")]
[name="茱安娜"]裂云兽好像发现了什么。
[Dialog]
[charslot]
往裂云兽的方向看去，远处前往蔓珠院的山道上挤满了穿着黯淡的人。
[charslot(slot="m",name="avg_npc_2010_1#2$1",focus="m")]
[name="恩雅"]这是......有重要的人去世了。
[charslot(slot="m",name="avg_4211_snhunt_1#9$2",focus="m")]
[name="茱安娜"]那会是谁？
[Dialog]
[charslot]
恩雅摇摇头。不安的寒意透过厚厚的行装，让她不禁打了个冷战。
[charslot(slot="m",name="avg_4211_snhunt_1#10$2",focus="m")]
[name="茱安娜"]恩雅，你还好吗？
[charslot(slot="m",name="avg_npc_2010_1#12$1",focus="m")]
[name="恩雅"]......我们慢点走，避开人群。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopsound(channel="wind", fadetime=2)]
[bgeffect]
[charslot]
[Background(image="24_g2_temple_indoor",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(key="$monastery_sad_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
墨灰相交的云层低垂，直压寺院的瓦檐。今日的谢拉格尤为寒冷，北风几乎能灌进哀悼者的眼眶和骨髓。
聚在庭院里的家族成员与修士们默默低头，布朗陶的领民也自发围在院外，这位以生命守护谢拉格的家主，让他们骄傲，也让他们悲恸。
大雪随风飘来，积在一杆杆黑伞之上。伞柄稍一抖动，雪花如瀑落下，而伞下的布朗陶贵族也长叹了一口气。
[charslot(slot="m",name="avg_npc_272_1#1$1",focus="m")]
[name="布朗陶男贵族"]所以，大夫人的遗体......
[charslot(slot="m",name="avg_npc_274_1#1$1",focus="m")]
[name="布朗陶女贵族"]火势太凶，他们把残骸翻了个遍，一无所获。
[name="布朗陶女贵族"]我听说，今天棺材里放着的，是她平日里的常服，以及一点从现场取得的灰烬。
[charslot(slot="m",name="avg_npc_272_1#1$1",focus="m")]
[name="布朗陶男贵族"]是吗？没料到大夫人一世精明，竟然——
[Dialog]
[charslot]
[delay(time=0.2)]
[charslot(slot="m",name="avg_npc_262_1#6$1",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_272_1#1$1",focus="m")]
[name="布朗陶男贵族"]啊，二夫人......
[name="布朗陶男贵族"]......对不起，是我失言了。
[charslot(slot="m",name="avg_npc_262_1#9$1",focus="m")]
[name="休露丝"]......
[Dialog]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step",loop=false)]
[stopsound(channel="step",fadetime=2)]
[charslot(duration=1)]
[delay(time=1.5)]
休露丝不作回应，她径直走向庭院中间，等待着曾与自己朝夕相处的姐姐。
清脆的摇铃震颤，与婉转的笛子协奏。修士合上双手，低吟着赞美耶拉冈德的雅颂，领民随着歌声抚胸祈祷——
耶拉冈德垂怜，让她与您同行。
踏着泥泞的道路上山而来的，是六名布朗陶宗家的亲属，尤卡坦排在最前。他们缓步向前，厚实的楠木灵柩在他们的肩上起伏。
六人停在了布朗陶的继任者面前，小心翼翼地将灵柩放在一张桌台上。
尤卡坦踱步回到妻子的身边，他那悲戚不已的神色，正对着休露丝平静的面庞。
[Dialog]
[charslot(slot="l",name="avg_npc_262_1#6$1",focus="all")]
[delay(time=0.2)]
[charslot(slot="r",name="avg_npc_263_1#4$1",duration=1)]
[PlaySound(key="$d_avg_walk_stage", volume=1,loop="false", channel="nw")]
[stopsound(fadetime=2, channel="nw")]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_262_1#6$1",focus="l")]
[name="休露丝"]尤卡坦......
[charslot(slot="r",name="avg_npc_263_1#4$1",focus="r")]
[name="尤卡坦"]露丝，我......
[charslot(slot="l",name="avg_npc_262_1#6$1",focus="l")]
[name="休露丝"]辛苦你了。
[Dialog]
[charslot]
颂歌唱罢，万籁渐息，众人一同注视着休露丝。
她第一次理解菈塔托丝那不得不佩戴的面具，责任的重量，绝非软弱者的肩背可以担负。
[charslot(slot="m",name="avg_npc_262_1#6$1",focus="m")]
[name="休露丝"]......
[name="休露丝"]感谢大家来到这里，与我一同悼念，菈塔托丝·布朗陶夫人。
[name="休露丝"]她不仅仅是我的姐姐，是布朗陶家的卫士，也是耶拉冈德忠实的孩子......
[name="休露丝"]智慧为她带来勇气，她曾对我说，她会保护我和这里的一切......最艰难的日子里，她依然相信谢拉格会有充满希望的明天。
[name="休露丝"]于她而言，她没有辜负祖父的嘱托，在生命的最后一刻都在为布朗陶而奉献，至死不渝。
[name="休露丝"]于我而言......我失去了最重要的亲人，直到今天才如梦初醒般体会到她所有的苦衷，却再也不能向她诉说。
[name="休露丝"]相信在场的人都会和我一样，铭记她的音容、她的牺牲、她对谢拉格和布朗陶......对家人的，深沉的爱。
[charslot(slot="m",name="avg_npc_262_1#2$1",focus="m")]
[name="休露丝"]......相信各位也会和我一样铭记在心——是谁破坏了美好，是谁给我们烙下无法愈合的伤痕。
[name="休露丝"]“短暂的一生如昼将尽，终在永恒之所与祂同行”......
[name="休露丝"]耶拉冈德在上。
[Dialog]
[charslot]
“耶拉冈德在上”，此起彼伏。众人随着休露丝，一同行起跪礼。
在灾厄席卷一切的时代，耶拉冈德仍会给予每一个谢拉格人平和、安谧......
当所有人起身后，两人从人群中走出——阿克托斯与角峰，他们抱着洁白的花束，缓缓迈向灵柩。
[charslot(slot="m",name="avg_npc_254_1#14$1",focus="m")]
[name="阿克托斯"]节哀，休露丝......
[charslot(slot="m",name="avg_npc_254_1#6$1",focus="m")]
[name="阿克托斯"]菈塔托丝因我而死，我永远不会忘！
[charslot(slot="m",name="avg_npc_262_1#6$1",focus="m")]
[name="休露丝"]谢谢你，阿克托斯。
[name="休露丝"]我只希望这对于我们两家来说都是一个残酷的教训，我们都该搞清楚，谁才是真正的敌人。
[charslot(slot="m",name="avg_npc_254_1#14$1",focus="m")]
[name="阿克托斯"]我......
[Dialog]
[charslot]
[delay(time=0.2)]
[charslot(slot="m",name="avg_199_yak_1#10$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_199_yak_1#10$1",focus="m")]
[name="角峰"]休露丝大人......
[charslot(slot="m",name="avg_199_yak_1#1$1",focus="m")]
[name="角峰"]恩希欧迪斯大人为不能出席仪式而愧疚，派我前来表达歉意与哀思，他会在合适的时间亲自登门问候。节哀顺变，休露丝大人。
[charslot(slot="m",name="avg_npc_254_1#1$1",focus="m")]
[name="阿克托斯"]那家伙忙到这个地步了？
[charslot

... (全文15554字符)
```

### level_act46side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g5_guestroom",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_253_1#4$1",duration=1.5)]
[Delay(time=2)]
[name="菈塔托丝"]那么按照你的说法，那位开斯特公爵一早就在谢拉格派布了大量的特工。而这一切都是为了她将来吞并谢拉格而做的准备？
[name="菈塔托丝"]可是她如何能做到？
[charslot(slot="m",name="avg_npc_2006_1#5$1",focus="m")]
[name="维多利亚记者"]应该说......这都是我根据在谢拉格的见闻做出的合理推测。
[charslot(slot="m",name="avg_npc_253_1#1$1",focus="m")]
[name="菈塔托丝"]那么在这一众卧底在谢拉格的维多利亚人当中，偏偏有你这样一位追求正义的记者？
[charslot(slot="m",name="avg_npc_2006_1#7$1",focus="m")]
[CameraShake(duration=0.5, xstrength=5, ystrength=5, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="维多利亚记者"]这样的说法太失礼了！
[charslot(slot="m",name="avg_npc_2006_1#10$1",focus="m")]
[name="维多利亚记者"]我的名字叫阿尔贝塔，如果您对维多利亚的新闻业稍有了解的话，就该听说过这个名字写过多少篇不被允许见诸报纸的真实报道。
[name="阿尔贝塔"]无论如何，我为我的工作感到骄傲。
[charslot(slot="m",name="avg_npc_253_1#2$1",focus="m")]
[name="菈塔托丝"]哼......
[charslot(slot="m",name="avg_npc_253_1#7$1",focus="m")]
[name="菈塔托丝"]记者小姐，我姑且相信你的自述，但这不意味着你完全洗脱了嫌疑。
[name="菈塔托丝"]自从那次爆炸之后，你们派的探子，一直由我指挥护卫们拔除。
[name="菈塔托丝"]如果你所言属实，那就把我们带去摄制组的驻地，我和你所说的特工会有很多话题可聊。
[charslot(slot="m",name="avg_npc_253_1#1$1",focus="m")]
[name="菈塔托丝"]你肯定不会推辞吧？
[charslot(slot="m",name="avg_npc_2006_1#11$1",focus="m")]
[name="阿尔贝塔"]可是——
[Dialog]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_gnrtrllng", volume=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_253_1#4$1",focus="m")]
[name="菈塔托丝"]？！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4116_blkkgt_1#3$1",afrom=0, ato=1, duration=0.3)]
[charslot(slot="m",posfrom="-150,0", posto="0,0", duration=0.5)]
[Delay(time=0.5)]
[name="锏"]闪开！
[Dialog]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[charslot(slot="m",afrom=1, ato=0, duration=0.3)]
[charslot(slot="m",posfrom="0,0", posto="150,0", duration=0.5)]
[Delay(time=1)]
[PlayMusic(intro="$kjerag_n_intro",key="$kjerag_n_loop", volume=0.6)]
[PlaySound(key="$d_avg_gnrtrspbm", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
锏揪住身旁的菈塔托丝和记者，躲进身后的房间，而不知何处投来的闪光弹在审讯室内炸开。
[Dialog]
[charslot]
[PlaySound(key="$bodyfalldown1", volume=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[Delay(time=1)]
远处避让不及的布朗陶家护卫惨叫一声——一柄飞刀直插他的心脏。
[charslot(slot="m",name="avg_npc_253_1#8$1",focus="m")]
[name="菈塔托丝"]该死！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4116_blkkgt_1#6$1",afrom=0, ato=1, duration=0.3)]
[charslot(slot="m",posfrom="50,0", posto="0,0", duration=0.5)]
[Delay(time=1)]
[PlaySound(key="$d_avg_knifeplank", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4116_blkkgt_1#6$1",focus="none")]
锏从门边探出身子，旋即再次飞来一柄刀，她侧身躲开，看着飞刀插入门框。
[charslot(slot="m",name="avg_4116_blkkgt_1#7$1",focus="m")]
[name="锏"]使用这种刀具，对手是“灰礼帽”。
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",focus="m")]
[name="锏"]你们先在这里躲好，我去确认袭击的规模和作战方式。
[Dialog]
[PlaySound(key="$d_avg_jandrg", volume=1)]
[Delay(time=1)]
[PlaySound(key="$swordtsing1", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
[PlaySound(key="$swordtsing3", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[charslot(slot="m",name="avg_4116_blkkgt_1#3$1",afrom=1, ato=0, duration=0.3)]
[charslot(slot="m",posfrom="0,0", posto="-150,0", duration=0.5)]
[Delay(time=1)]
语毕，她猛地抽出腰间的双锏，正正击落两柄刚从暗处飞来的短刀，随后纵身一跃向前冲去，踏起的风尘让记者下意识地眯起眼睛。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_253_1#7$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_2006_1#12$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_253_1#7$1",focus="l")]
[name="菈塔托丝"]你——
[name="菈塔托丝"]这是怎么回事？“灰礼帽”是怎么知道这里的？
[name="菈塔托丝"]你向他们报信了？我一直盯着，这怎么可能......
[charslot(slot="r",name="avg_npc_2006_1#10$1",focus="r")]
[name="阿尔贝塔"]不对，我检查过带出来的所有东西，也确定没有人跟着。
[charslot(slot="r",name="avg_npc_2006_1#7$1",focus="r")]
[name="阿尔贝塔"]小心！
[Dialog]
[charslot(slot="r",posfrom="0,0", posto="-100,0", duration=0.5)]
[Delay(time=0.3)]
[charslot(slot="l",posfrom="0,0", posto="-50,0", duration=0.5)]
[Delay(time=0.5)]
[PlaySound(key="$a_bat_buildingshaking_1", volume=1)]
[charslot(slot="r",name="avg_npc_2006_1#10$1",posfrom="-100,0", posto="-100,0")]
[charslot(slot="l",name="avg_npc_253_1#4$1",posfrom="-50,0", posto="-50,0")]
[CameraShake(duration=1.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[PlaySound(key="$d_avg_explosion_stone", volume=1)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot="r",focus="none")]
房间剧烈晃动。记者拽住菈塔托丝的衣袖，往旁边一避，破损的天花板掉落下的碎块，正正砸中刚才她们所停留的位置。
[Dialog]
[charslot(slot="r",posfrom="-100,0", posto="0,0", duration=1)]
[charslot(slot="l",posfrom="-50,0", posto="0,0", duration=1)]
[Delay(time=1.5)]
[charslot(slot="l",name="avg_npc_253_1#4$1",focus="l")]
[name="菈塔托丝"]......那该怎么解释？
[charslot(slot="r",name="avg_npc_2006_1#10$1",focus="r")]
[name="阿尔贝塔"]......等等！还有一个地方。
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Delay(time=1.5)]
[charslot(slot="r",name="avg_npc_2006_1#10$1",focus="none")]
她拿起胸前的相机，取下镜头、按住快门，反光板抬起，内部

... (全文24304字符)
```

### level_act46side_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g3_mainhall",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(key="$monastery_sad_loop",volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_2014_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="年轻的修士"]圣女大人......
[name="年轻的修士"]那些跟随罪人阿德颂背叛了蔓珠院的修士，都尽数认罪了。此时都被控制在别院，等候您的发落。
[name="年轻的修士"]您打算......如何处置这些人呢......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_1046_sbell2_1#12$1",duration=1.5)]
[Delay(time=2)]
[name="恩雅"]......
[charslot(slot="m",name="avg_1046_sbell2_1#12$1",focus="none")]
大殿中空空荡荡，那些平日里坐满人的坐席都空了出来。
仅有一名年轻的修士恭候在座前，垂首等待着她的旨意。
[charslot(slot="m",name="avg_1046_sbell2_1#12$1",focus="m")]
[name="恩雅"]在动乱中发生的事，我都已经听说了。
[name="恩雅"]他们受到了阿德颂的蛊惑，做了错误的事。
[charslot(slot="m",name="avg_1046_sbell2_1#1$1",focus="m")]
[name="恩雅"]但我相信，他们的本心，从来都是保卫谢拉格。
[charslot(slot="m",name="avg_1046_sbell2_1#4$1",focus="m")]
[name="恩雅"]他们在面对入侵者时挺身而出的行为足以抵罪，于情于理都不该受重罚......
[name="恩雅"]就让他们去三族领地中，义务帮人们做完这个冬天的农活。同时也要他们自省，自己每天诵读的经文，到底该怎样实践。
[name="恩雅"]等到明年开春，再回蔓珠院吧。
[charslot(slot="m",name="avg_npc_2014_1#1$1",focus="m")]
[name="年轻的修士"]是......
[charslot(slot="m",name="avg_1046_sbell2_1#4$1",focus="m")]
[name="恩雅"]还有什么事吗？
[charslot(slot="m",name="avg_npc_2014_1#1$1",focus="m")]
[name="年轻的修士"]圣女大人......请准我斗胆向您请教......
[name="年轻的修士"]您在圣巡的途中，听到耶拉冈德的旨意了吗？
[charslot(slot="m",name="avg_1046_sbell2_1#3$1",focus="m")]
[name="恩雅"]......为什么要这么问？
[name="恩雅"]你难道忘了，我们不该向祂索求祂的显现......
[Dialog]
[charslot]
年轻的修士头垂得更低了，迟疑着开口。
[charslot(slot="m",name="avg_npc_2014_1#1$1",focus="m")]
[name="年轻的修士"]人们都相信，在维多利亚人入侵的时候，是祂又一次施展了神迹，吓退了入侵者。
[name="年轻的修士"]可是不知为何......我觉得，那更像是一场告别......
[name="年轻的修士"]我在想，或许是在那一场天灾发生的时候，耶拉冈德就已经离我们远去了。
[name="年轻的修士"]如果圣女大人要惩罚我不虔诚的罪......我也......
[charslot(slot="m",name="avg_1046_sbell2_1#1$1",focus="m")]
[name="恩雅"]......
[charslot(slot="m",name="avg_1046_sbell2_1#4$1",focus="m")]
[name="恩雅"]马修......你叫马修，对吗？
[name="恩雅"]能不能告诉我，你是如何决定要加入蔓珠院的？
[charslot(slot="m",name="avg_npc_2014_1#1$1",focus="m")]
[name="年轻的修士"]小时候，我的父母要养育五个孩子，家里的田地种不出足够一家人吃的粮食，于是他们决定把年纪最小的我送去蔓珠院。
[name="年轻的修士"]这样可以省下一个人的口粮，我也能从蔓珠院拿到补贴......
[name="年轻的修士"]我当然也有在认真学习！这些年来，我也一直在用心背诵《耶拉冈德》，学习祂的教导......
[name="年轻的修士"]可是后来，我发现谢拉格变了许多。
[name="年轻的修士"]有太多从没听说过的东西，甚至是《耶拉冈德》中也没有解释的事情。
[name="年轻的修士"]我原本以为，只要有足够的食物，还有可以遮挡风雪的住处，就可以过上幸福的日子......
[name="年轻的修士"]可是为什么，如今我们已然拥有了这些，却更加迷茫......
[name="年轻的修士"]圣女大人，会不会是现在的谢拉格人，已经偏离了祂指引的路，已经走出去太远......
[name="年轻的修士"]所以耶拉冈德，才会离开我们......
[charslot(slot="m",name="avg_1046_sbell2_1#4$1",focus="m")]
[name="恩雅"]......
[name="恩雅"]耶拉冈德，什么时候为祂的子民指引了一条具体的路呢？
[name="恩雅"]最早的谢拉格人来到这片群山中，用镐头破开冻土，用树木搭建房屋的时候，恐怕也不会想到......
[name="恩雅"]在今天，这片土地上的人们已经把目光投向星空之外。
[name="恩雅"]可是同样，耶拉冈德也从来没有向我们许诺过，我们可以拥有一片没有任何危难的永恒净土。
[charslot(slot="m",name="avg_1046_sbell2_1#8$1",focus="m")]
[name="恩雅"]我们必将面临更多的艰难险阻，在种种磨难中上下求索。
[charslot(slot="m",name="avg_1046_sbell2_1#4$1",focus="m")]
[name="恩雅"]直到有一日，我们可以抵达祂的座前，向祂叩问那个关于我们自身的问题......
[charslot(slot="m",name="avg_npc_2014_1#1$1",focus="m")]
[name="年轻的修士"]可是圣女大人，耶拉冈德作为先贤、师长、领袖......祂对祂的子民，难道没有任何的命令吗？
[charslot(slot="m",name="avg_1046_sbell2_1#4$1",focus="m")]
[name="恩雅"]算不上是命令吧......
[name="恩雅"]其实想一想，耶拉冈德想要叮嘱我们的，最重要的事，不是早就写在经文中了吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="24_g1_snowyforest",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="你们要记得来时的路，不可忘却；", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你们要敬畏未至的风雪，不可轻信己见；", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="要握紧手中的弓箭、镐头和种子，不可松懈；", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="要爱自己的兄弟姐妹，爱你的邻人与朋友、爱山石草木如同爱自己的兄弟姐妹那般。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你们若依此律，大地上将不再有灾难可胜过你们，你们定能家园永固。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="67_G3_rhineobservatory_i",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$calm_loop",volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_devicebeep",volume=1)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_devicebeep",volume=1)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_devicebeep",volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_1047_halo2_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot]
[PlaySound(key="$d_avg_glassdooropen",volume=1)]
[Delay(time=3.5)]
[charslot(slot="l",name="avg_1047_halo2_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_1031_slent2_1#7$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="r",name="avg_1031_slent2_1#7$1",focus="r")]
[name="赫默"]埃琳娜，你还在忙吗？
[charslot(slot="l",name="avg_1047_halo2_1#4$1",focus="l")]
[name="埃琳娜"]赫默主任？
[charslot(slot="r",name="avg_1031_slent2_1#7$1",focus="r")]
[name="赫默"]我听说你还在处理之前的观测数据——希望没有打扰到你。
[charslot(slot="l",name="avg_1047_halo2_1#1$1",focus="l")]
[name="埃琳娜"]我根据之前在圣山上收集到的数据，用计算机重新建模计算......
[name="埃琳娜"]如果顺利的话，应该很快就能得到那个天外来物在谢拉格降落的具体地点了——总比在雪山里漫山遍野地跑来得快点。
[charslot(slot="r",name="avg_1031_slent2_1#7$1",focus="r")]
[name="赫默"]这是非常重要的一次发现，多亏了你的勇气，还有决心......辛苦了，埃琳娜。
[charslot(slot="l",name="avg_1047_halo2_1#5$1",focus="l")]
[name="埃琳娜"]赫默主任不用因为这些分内的事夸奖我啦，我会不好意思的......
[charslot(slot="l",name="avg_1047_halo2_1#18$1",focus="l")]
[name="埃琳娜"]对了......卡罗琳前辈的事，有新的消息吗？
[charslot(slot="r",name="avg_1031_slent2_1#4$1",focus="r")]
[name=

... (全文25556字符)
```

### training_act46side_01_a

```
[header(is_skippable=false, is_tutorial=true)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true, black=0.3)]
[popupdialog(dialogHead="$avatar_hibisc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]欸？发生什么事了？
[tutorial(focusWidth=300, focusHeight=300, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_aguard", tileY=3, tileX=4)]这是耶拉冈德划定的禁止闯入的区域，祂不想被任何人打扰。
[tutorial(focusWidth=150, focusHeight=150, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_aguard", tileY=2, tileX=3)]是......是那个<@tu.kw>圣女像</>，祂会以<@tu.kw>圣女像</>为媒介，召唤<@tu.kw>雪崩</>驱逐闯入者。
[popupdialog(dialogHead="$avatar_aguard", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]就像刚才发生的那样，<@tu.kw>雪崩</>会依照<@tu.kw>圣女像</>所指的方向，以强大的力量<@tu.kw>推动</>敌人，并且造成<@tu.kw>真实伤害</>。
[popupdialog(dialogHead="$avatar_hibisc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]这么大阵仗，只是为了把闯入者都赶出去呀......
[battle.pause(pause=false)]
```

### training_act46side_01_b

```
[header(is_skippable=false, is_tutorial=true)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true, black=0.3)]
[popupdialog(dialogHead="$avatar_aguard")]只要敌人踏入<@tu.kw>雪崩禁区</>，<@tu.kw>雪崩</>的<@tu.kw>预警数值</>便会提升，<@tu.kw>圣女像</>的<@tu.kw>技力</>也会随之增长。
[tutorial(focusWidth=150, focusHeight=150, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_aguard", tileY=2, tileX=3)]达到一定数值，<@tu.kw>雪崩</>就会降临。
[battle.pause(pause=false)]
```


> 本章节共33个脚本文件，此处展示前30个。

## 统计

- 总字符数：564947
- 对话行数：4277


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
