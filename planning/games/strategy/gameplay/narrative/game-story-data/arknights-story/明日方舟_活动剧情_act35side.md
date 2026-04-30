# 明日方舟 · 活动剧情 · act35side（32段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act35side」完整剧情脚本（32个文件，3020行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act35side
- 脚本文件数：32

### guide_act35side_r1_buy

```
[HEADER(is_skippable=false, is_tutorial=true)] 宝石铭刻第一轮购买
[Tutorial(waitForSignal="carving_shop_routed")]
[PopupDialog(dialogHead="$avatar_avg_4139", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 欢迎来到博物馆的宝石铭刻课程。
[PopupDialog(dialogHead="$avatar_avg_4139", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 在这里，您可以学习到如何像古萨尔贡人一样对宝石进行刻印加工，感受到古老工艺的魅力。
[PopupDialog(dialogHead="$avatar_avg_4139", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这里是博物馆周边部，大家可以在这里购买、兑换铭刻课程所需要的工艺。
[Tutorial(target="panel_carving_next_round_mat", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1, dialogHead="$avatar_avg_4139", 		  dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 铭刻课程中的每一轮，我们都会提供一些宝石原料供大家加工。
[Tutorial(target="panel_carving_next_round_mat", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1, dialogHead="$avatar_avg_4139", 		  dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这些待加工原料都是“伊纳”，这个红色的原料是<color=#43deae>火焰伊纳</color>。
[Tutorial(target="panel_carving_next_round_mat", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1, dialogHead="$avatar_avg_4139", 		  dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 请让我来解释一下，在萨尔贡，“伊纳”是“石头”的意思。
[Tutorial(target="btn_carving_to_process", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1, dialogHead="$avatar_avg_4139", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 在去<color=#43deae>操作台</color>进行加工之前，我们还要完成一些准备工作。
[Tutorial(target="panel_carving_free_count", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1, dialogHead="$avatar_avg_4139", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 周边部特别提供了<color=#43deae>免费</color>工艺使用次数。
[Tutorial(target="panel_carving_buy_card_group", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_avg_4139")] 这里是周边部为大家提供的工艺。获取工艺后，就可以将手上的宝石原料刻印成更高级的宝石。
[Carving.FocusBuyCard(position=0)]
[Tutorial(target="btn_carving_buy_card", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=1, dialogHead="$avatar_avg_4139")] 确认了工艺的流派后，我们点击购买，然后就可以去<color=#43deae>操作台</color>上试试了！
```

### guide_act35side_r1_process

```
[HEADER(is_skippable=false, is_tutorial=true)] 宝石铭刻第一轮操作
[Tutorial(waitForSignal="carving_process_routed")]
[Tutorial(target="panel_carving_curr_mat", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_avg_4139", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这些就是本轮课程提供的宝石原料。
[Tutorial(target="panel_carving_score", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_avg_4139", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 课程的目标是使用工艺刻印宝石原料，刻印出更好的宝石，通过专家的评价，<color=#43deae>获得更高的分数</color>。
[Tutorial(target="panel_carving_hand_card", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_avg_4139")] 这里是刚刚我们从周边部获取的工艺，<color=#43deae>点击</color>它们可以看到详细效果。
[Carving.SelectHandCard(cardId="card_fire_1")]
[Tutorial(target="panel_carving_card_process_slot", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_avg_4139")] 我们需要在操作台上进行宝石铭刻，请将工艺<color=#43deae>放入</color>中间的操作台中。
[Carving.SelectCardSlot]
[Tutorial(target="panel_carving_hand_card", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_avg_4139")] 再选择一种工艺吧。
[Carving.SelectHandCard(cardId="card_fire_2")]
[Tutorial(target="panel_carving_card_process_slot", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_avg_4139")] 请注意，待加工原料会按照<color=#43deae>从左至右</color>的工艺顺序进行刻印。
[Carving.SelectCardSlot]
[Tutorial(target="panel_carving_output", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1, dialogHead="$avatar_avg_4139")] 这里我们能看到本次铭刻<color=#43deae>预测获得</color>的刻印产出，原料经过加工之后已经变得更加复杂和精巧了。
[Tutorial(target="btn_carving_handbook", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1, dialogHead="$avatar_avg_4139")] 发条羽兽会告诉大家各种宝石原料对应的<color=#43deae>分数</color>和<color=#43deae>铭刻</color>方法，经过<color=#43deae>越复杂</color>工艺处理之后的宝石原料，获得的分数就会<color=#43deae>越高</color>。
[Tutorial(target="btn_carving_handbook", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_avg_4139")] 如果有需要，大家也可以找它看看<color=#43deae>加工参考书</color>，确认每种宝石的分数和加工方法。
[Tutorial(target="btn_carving_process", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_avg_4139")] 那么，开始铭刻吧！
```

### guide_act35side_r2_buy

```
[HEADER(is_skippable=false, is_tutorial=true)] 宝石铭刻第二轮购买
[Tutorial(waitForSignal="carving_shop_routed")]
[Tutorial(target="panel_carving_next_round_mat", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_avg_4139", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 在新一轮课程里，我们会提供全新的伊纳，每一轮的待加工原料和上一轮都不一样。
[Tutorial(target="panel_carving_gold_count", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=1.5, dialogHead="$avatar_avg_4139", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 刚刚大家通过上一轮课程评价以后获得了周边兑换券，这种兑换券可以用来在周边部购买新的工艺或操作台。
[Tutorial(target="btn_carving_buy_slot", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_avg_4139", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 获得了<color=#43deae>新的操作台</color>之后，我们可以使用更多更复杂的铭刻工艺，最后刻印出的宝石可以拿到更高的分数。
[Tutorial(target="btn_carving_buy_card", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="$avatar_avg_4139", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 在周边部购买需要的工艺与操作台之后，就请大家自己去试试吧！
```

### act35side_05

```
[HEADER(is_tutorial=true, is_skippable=false, is_autoable=false)] 活动35side普通关_05
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.2)]
[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这里结晶太多了，还好我们有专业的装置<@tu.kw>结晶消除桩</>。
[Tutorial(cardIndex=0, rightStart=true, focusWidth=110, focusHeight=110,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", anchor="BottomRight",           protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x",            dialogY="$f_lower_dialog_pos_y")] 它可以帮我们大忙，<@tu.kw>直接消除</>它所指向的<@tu.kw>一条直线上</>的<@tu.kw>所有结晶</>。
[Tutorial(tileX=4.5, tileY=2, focusWidth=610, focusHeight=110,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 合理利用地形，争取让我们的装置发挥最大的作用。
```

### act35side_sub-1-1

```
[HEADER(is_tutorial=true, is_skippable=false, is_autoable=false)] 活动35sidesub关_01
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.2)]
[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 各位干员注意，这里有全新类型的结晶，我们必须通过<@tu.kw>消除结晶</>来<@tu.kw>获得新的费用</>！
```

### level_act35side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="53_g2_menatmainstreet_n",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$farce_intro",key="$farce_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1492_1#1$1",duration=1)]
[delay(time=1.5)]
[name="点灯人"]♪夜色笼罩在大河两岸♪
[name="点灯人"]♪双月，一对相爱的伴侣，缓缓升上天空♪
[name="点灯人"]♪黑暗中，他们悄悄地亲吻♪
[name="点灯人"]♪殊不知，群星一颗一颗亮起来了♪
[name="点灯人"]♪星光里，他们羞红了脸蛋♪
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot = "m",posfrom = "0,0", posto = "-150,0",duration = 1.5,afrom=1,ato=0)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",posfrom = "-100,0", posto = "-100,0",bstart=0.5,bend=0.9)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "r",name="avg_npc_1492_1#1$1",posfrom = "150,0", posto = "0,0",duration = 1)]
[delay(time=1.5)]
[playsound(key="$d_avg_cndlbrn",volume=0.6)]
[delay(time=1)]
[charslot(slot = "l",name = "avg_4058_pepe_1#2$1",duration=0.3)]
[delay(time=0.5)]
[charslot(slot = "r",posfrom = "0,0", posto = "100,0",duration = 0.3)]
[CameraShake(duration=0.31, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[charslot(slot = "r",focus="r")]
[name="点灯人"]啊——！
[charslot(slot = "r",focus="r")]
[name="点灯人"]小姑娘，大半夜你怎么在这里不声不响的？吓死我了！
[charslot(slot = "l", name = "avg_4058_pepe_1#3$2",focus="l")]
[name="佩佩"]大叔，你怕什么？你难道怕我打劫你吗？
[charslot(slot = "r",focus="r")]
[name="点灯人"]那倒不是，在这里生活的人哪里有缺钱的哟。
[name="点灯人"]你们年轻人，大晚上不去滨河大道谈恋爱，在博物馆门前干什么？
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="l")]
[name="佩佩"]来值夜班啊。
[charslot(slot = "r",focus="r")]
[name="点灯人"]啧啧啧，这几年真是邪了门了，以前点灯，点几盏就能碰上一对卿卿我我的小情侣，现在好了，全是摸黑加班的人。
[name="点灯人"]去吧，路给你点亮了，工作干完早点回啊。
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="l")]
[name="佩佩"]谢了，大叔。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot = "l",posfrom = "-100,0", posto = "-250,0",duration = 1,afrom=1,ato=0)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="53_g5_museum",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#1$1",duration=0.5)]
[delay(time=1)]
[name="佩佩"]真的一个人也没有......缇缇那家伙倒是没骗我。
[name="佩佩"]让我看看，这么久没来，他们又发现了什么好东西？
[Dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "-80,0",duration = 0.8)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1")]
[name="佩佩"]暗阑时代的宝石作坊遗迹坑，这设备的源石回路痕迹有点来头啊......这么完整的件，是整体成形的吗？
[name="佩佩"]不......是用整块源石雕琢而成，真精巧啊，不细看根本看不出来。
[Dialog]
[charslot(slot = "m",posfrom = "-80,0", posto = "70,0",duration = 1)]
[delay(time=1.2)]
[charslot(slot = "m", name = "avg_4058_pepe_1#4$1")]
[name="佩佩"]哇，是雨林里发掘的奔流时代的祭祀用具，上面有好多斑点......活物祭祀留下的血点吗？
[name="佩佩"]好多武器......是为了黑土之战而举行的祭祀吗？
[charslot(slot = "m", name = "avg_4058_pepe_1#5$1")]
[name="佩佩"]......
[charslot(slot = "m", name = "avg_4058_pepe_1#3$2")]
[name="佩佩"]唉......以后有空再好好和你们认识认识，我今晚可是有约的啊。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_gateopen", volume=1)]
[Background(image="53_g6_museum_core",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1",duration=0.5)]
[delay(time=1)]
[name="佩佩"]就在这里了......
[name="佩佩"]初次见面，老先生，很抱歉打扰您夜晚的平静，但我有许多疑惑，只有您能为我解答。
[name="佩佩"]拜托啦，请千万不要因为我的冒犯而生气。
[Dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "100,0",duration = 0.8)]
[delay(time=1.5)]
[charslot(slot = "m",posfrom = "100,0", posto = "70,0",duration = 1)]
[playsound(key="$d_avg_open_glasscabinet")]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_4058_pepe_1#11$1")]
[name="佩佩"]漂亮耶！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="53_g6_museum_core",screenadapt="coverall",y=-20, xScale=1.05, yScale=1.05)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.15,block=false)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.15,block=true)]
[charslot(slot = "m", name = "avg_npc_1479_1#2$1",action="zoom", poszoom = "0.5,0.5", scale=1.1,duration = 0.1,afrom=0,ato=0)]
[backgroundTween(yTo=20, duration=11.5, block=false)]
[focusout(type="bg", from=0, to=1, duration=4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$newhope01_intro",key="$newhope01_loop", volume=0.6)]
[delay(time=1.5)]
[charslot(slot = "m",afrom=0,ato=1,duration = 1.5)]
[charslot(slot = "m",posfrom = "0,-30", posto = "0,-90",duration = 10)]
[delay(time=3)]
[name="佩佩"]种族菲林，目测身高约两米，躯体大部分被金属机械置换，保有部分肉体组织。
[name="佩佩"]皮肤颜色为紫色，疑似被防腐药水浸染而成，触摸仍有弹性。
[name="佩佩"]面部佩戴黄金面具，周身覆盖黄金甲胄，体内脏器已被摘除。
[Dialog]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain]
[delay(time=1)]
[Background(image="53_g6_museum_core",screenadapt="coverall")]
[focusout(type="bg", from=1, to=0, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "m", name = "avg_4058_pepe_1#4$1",posfrom = "0,0", posto = "0,0",duration=0.5)]
[delay(time=1)]
[name="佩佩"]奇怪，无论是尸体本身还是陪葬器物，都没有指向宝库位置的线索。
[name="佩佩"]可现场所发掘到的一切都在这里了啊？
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1")]
[name="佩佩"]或许......线索还是这颗宝石本身......
[PlaySound(key="$d_avg_paper1", volume=1)]
[name="佩佩"]“第一颗代表心脏，自它跳动，我们便存在。”
[name="佩佩"]“第二颗代表肺，当我们初次呼吸，记忆便开始。”
[name="佩佩"]“第三颗代表胃肠，食物进入肚皮，舌头变得挑剔，我们有了喜好、个性。”
[name="佩佩"]“第四颗代表肝脏，我们清醒着进入夜晚，为了职责与义务。”
[charslot(slot = "m", name = "avg_4058_pepe_1#4$1")]
[name="佩佩"]那我又该如何使用这颗宝石？
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1")]
[name="佩佩"]......
[charslot(duration=1)]
看着尸体空空的胸腔，佩佩沉思片刻，将手伸入其中，将宝石放在了心脏的位置。
随即，她屏住呼吸，等待变化发生。
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1")]
[name="佩佩"]......
[name="佩佩"]......
[charslot(slot = "m", name = "avg_4058_pepe_1#5$1")]
[name="佩佩"]怎么会？
[name="佩佩"]毫无变化......
[ch

... (全文28036字符)
```

### level_act35side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="53_g6_museum_core",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$chasing_intro",key="$chasing_loop", volume=0.6)]
[Delay(time=1)]
[CameraShake(duration=3, xstrength=10, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_paniccrowd")]
[name="慌张的观众"]啊——！
[name="惊恐的观众"]尸体......尸体动了！
[name="惊恐的观众"]快，快离开这里！这里闹鬼！
[name="惊恐的观众"]那具古尸是不是朝我看过来了！
[name="慌张的观众"]我就知道！
[CameraShake(duration=0.3, xstrength=30, ystrength=28, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="慌张的观众"]我就知道一个城市历史太悠久迟早有天会发生这种事！
[Dialog]
[playsound(key="$d_avg_crowdrun",channel="2")]
[Delay(time=2)]
[charslot(slot = "m", name = "avg_npc_1478_1#6$1",duration=0.5)]
[Delay(time=0.7)]
[name="梅捷缇克缇"]诸位请冷静下来，不要着急，不要慌张！
[charslot(slot = "m", name = "avg_4058_pepe_1#8$1")]
[name="佩佩"]请大家从安全出口有序离开，往这边！不要挤！
[charslot(slot = "m", name = "avg_npc_1478_1#5$1")]
[name="梅捷缇克缇"]哎，让一下，让我们过去一下。
[Dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "80,0",duration = 0.7)]
[Delay(time=0.3)]
[charslot(slot = "right", name = "avg_npc_1491_1#1$1",duration = 0.2)]
[charslot(slot = "right",posfrom = "200,0", posto = "-50,0",duration = 0.7)]
[Delay(time=0.3)]
[charslot(slot = "right",afrom=1,ato=0,duration=0.3)]
[playsound(key="$d_avg_clothmovement")]
[CameraShake(duration=0.2, xstrength=10, ystrength=10, vibrato=10, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m",posfrom = "80,0", posto = "0,0",duration = 0.5)]
[Delay(time=0.7)]
[charslot(slot = "m", name = "avg_npc_1478_1#4$1")]
[name="梅捷缇克缇"]不好意思，抱歉。
[Dialog]
[charslot(slot = "right", name = "avg_npc_1490_1#1$1",duration = 0.2)]
[charslot(slot = "right",posfrom = "100,0", posto = "-50,0",duration = 0.4)]
[Delay(time=0.2)]
[playsound(key="$bodyfalldown2")]
[charslot(slot = "right",afrom=1,ato=0,duration=0.2)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=20, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m",posfrom = "0,0", posto = "-100,0",duration = 0.3)]
[Delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_1478_1#7$1")]
[name="梅捷缇克缇"]*萨尔贡粗口*，阿娜特！阿娜特！
[charslot]
挤过拥挤的人群，梅捷缇克缇看到阿娜特面色苍白瘫倒在地，嘴唇无力地张合，似乎有话要说。
但后方歪着头的尸体让她心生恐惧，不敢凑上前。
[charslot(slot = "m", name = "avg_4058_pepe_1#8$1")]
[name="佩佩"]缇缇，辛苦你确保参观者们的安全，我想办法将阿娜特和这具古尸带到别的地方去。
[charslot(slot = "m", name = "avg_npc_1478_1#4$1")]
[name="梅捷缇克缇"]你是一点也不害怕吗？那玩意在动啊！
[charslot(slot = "m", name = "avg_4058_pepe_1#3$2")]
[name="佩佩"]也......还好吧，咳咳，我今年参与了两座古历纪时期坟墓的考古工作，两位墓主人我都亲眼见过了。
[charslot(slot = "m", name = "avg_4058_pepe_1#1$2")]
[name="佩佩"]比起它们，这位老先生已经算是慈眉善目的了。
[charslot(slot = "m", name = "avg_npc_1478_1#5$1")]
[name="梅捷缇克缇"]你这干过考古的胆色就是不一般......你一个人行吗？
[charslot(slot = "m", name = "avg_4058_pepe_1#6$2")]
[name="佩佩"]放心，我们干过考古的体力也很不一般。
[charslot]
[name="阿娜特"]缇缇......
[charslot(slot = "m", name = "avg_npc_1478_1#8$1")]
[name="梅捷缇克缇"]阿娜特她......？
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1")]
[name="佩佩"]......她应该没大碍，只是昏迷中的呓语。
[charslot(slot = "m", name = "avg_npc_1478_1#6$1")]
[name="梅捷缇克缇"]馆长办公室离这里不远，你们从侧门出去，尽量避开人群，等我将游客疏散完毕再过去找你们。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Background(image="53_g5_museum",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playsound(key="$d_avg_paniccrowd",volume=0.4)]
[playsound(key="$d_avg_crowdrun",channel="2",volume=0.4)]
[Delay(time=2)]
[interlude(maskid = "group_interclude_square_common", char = "右边的耳机", switch = true, style = 1,offset = "-450,125", channel = 3)]
[interlude(channel = 3, type = 3, slot = "m", switch = false, pfrom = "450,0", pto="-435,-105", duration = 0.5)]
[interlude(maskid = "group_interclude_square_common", char = "左边的耳机", switch = true, style = 1,offset = "450,125", channel = 4)]
[interlude(channel = 4, type = 3, slot = "m", switch = false, pfrom = "-450,0", pto="435,-105", duration = 0.5)]
[charslot(slot="m",name="avg_4138_narant_1#8$1",duration=0.5)]
[delay(time=1)]
[name="娜仁图亚"]发生什么了？我还没到埋伏的地点呢！你们提前启动发烟器了吗？
[charslot(slot = "m", focus = "n")]
[interlude(channel = 4, switch = true)]
[name="左边的耳机"]没啊，我们还没有行动呢。
[interlude(channel = 4, switch = false)]
[charslot(slot="m",name="avg_4138_narant_1#12$1")]
[name="娜仁图亚"]怎么回事？
[charslot(slot = "m", focus = "n")]
[interlude(channel = 3, switch = true)]
[name="右边的耳机"]好像是会场中有其他人引起了骚动。
[interlude(channel = 3, switch = false)]
[charslot(slot="m",name="avg_4138_narant_1#8$1")]
[name="娜仁图亚"]真是......我没在人群中看到目标，她去哪里了？
[name="娜仁图亚"]好吧，状况有变，我们的计划提前进行。找到她，盯紧了，时刻向我汇报。
[charslot(slot = "m", focus = "n")]
[interlude(channel = 3, switch = true)]
[name="右边的耳机"]好的。
[interlude(channel = 3, switch = false)]
[charslot(slot="m",name="avg_4138_narant_1#8$1")]
[name="娜仁图亚"]尽快，等得手后我们需要汇入人群才行。
[name="娜仁图亚"]等到人都疏散干净，一切都晚了。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[interlude(clear = true)]
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",posfrom = "100,0", posto = "100,0")]
[Background(image="53_g6_museum_core",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",duration=1)]
[delay(time=2)]
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]很好......这里人都走光了......
[Dialog]
[charslot(slot = "l",posfrom = "0,0", posto = "100,0",duration = 1)]
[delay(time=1.5)]
靠上前去，佩佩看见古尸胸腔内正流动着萤蓝色的光芒。
而那颗宝石早已消失在光芒中，再也看不见。
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]哼，果然因为宝石的原因......
[name="佩佩"]你这个姿势......也不是很好扛啊......
[charslot(slot = "m", focus = "n")]
围着尸体观察几秒后，佩佩决定将古尸抬起的左臂按下去。
[Dialog]
[charslot(slot = "left",posfrom = "100,0", posto = "100,-15",duration = 0.4)]
[delay(time=0.41)]
[charslot(slot = "left",posfrom = "100,-15", posto = "100,0",

... (全文21204字符)
```

### level_act35side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="53_g8_sargondeluxeroom",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(key="$calm_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",duration=1)]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",duration=1)]
[Delay(time=1)]
[playsound(key="$d_avg_penrustle")]
[Delay(time=1)]
[charslot(slot = "left",posfrom = "0,0", posto = "50,0",duration = 1)]
[Delay(time=1.4)]
[charslot(slot = "l", name = "avg_4058_pepe_1#4$1",focus="l")]
[name="佩佩"]真是精细啊，刚刚没注意到，这个家伙居然连表情与口型都能够模仿。
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]张开嘴让我看看，啊......
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="无名古尸"]（张嘴）
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]咽喉处很明显有类似声带的发声装置，那为何到现在你都一言不发？
[name="佩佩"]奇怪，按理说，发声也是声带与肌肉的动作，你应该能够模仿才是啊......
[Dialog]
[charslot(slot = "left",posfrom = "50,0", posto = "80,0",duration = 0.6)]
佩佩靠近尸体，把手搭上它的喉咙，而尸体则依着她的样子，将手按在佩佩的喉咙上。
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]你知道......
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="无名古尸"]......
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]你......知......道......
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="无名古尸"]你......滋......得......
[Dialog]
[charslot(slot = "l", name = "avg_4058_pepe_1#11$1",focus="l")]
[charslot(slot = "left",posfrom = "80,0", posto = "50,0",duration = 0.3)]
迅速抽回手，佩佩不可思议地捂住嘴巴，眼中透出惊喜的光彩。
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="l")]
[name="佩佩"]真的能说话啊......
[name="佩佩"]太神奇了......想不到沙阿那个年代真有如此精巧的工匠技艺。
[charslot(slot = "l", name = "avg_4058_pepe_1#4$1",focus="l")]
[name="佩佩"]先祖曾在一本《古历纪工艺考证》中提及......
[name="佩佩"]有异人可用源石回路宝石封存人的意识，然后用黄金为其重塑躯壳，可供人行动千年而不腐。
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]长生军......失传的技艺......陛下会对你很有兴趣的......
[name="佩佩"]宝库肯定藏在你记忆的深处。
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="无名古尸"]......
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]你可不能仅仅是学我说话，你还得告诉我它到底在哪里。
[name="佩佩"]让我看看......
[Dialog]
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[playsound(key="$d_avg_paper1")]
[Delay(time=1)]
[name="佩佩"]“第一颗代表心脏，自它跳动，我们便存在。第二颗代表肺，当我们初次呼吸，记忆便开始。”
[name="佩佩"]“第三颗代表胃肠，食物进入肚皮，舌头变得挑剔，我们有了喜好、个性。第四颗代表肝脏，我们清醒着进入夜晚，为了职责与义务。”
[name="佩佩"]第五颗......
[playsound(key="$d_avg_paper1")]
[charslot(slot = "l", name = "avg_4058_pepe_1#4$1",focus="l")]
[name="佩佩"]第五颗是什么？
[Dialog]
[playsound(key="$d_avg_paper1")]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_4058_pepe_1#5$1",focus="l")]
[name="佩佩"]没有，诗歌到这里就断了......
[name="佩佩"]看起来那位阿尔萨兰的前代研究者也没有答案。
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="无名古尸"]......
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]但你一定能帮我找到答案，对吗？
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="无名古尸"]......
[charslot(slot = "left",posfrom = "50,0", posto = "80,0",duration = 1)]
女孩再次伸出手，将手指按在尸体的喉咙处。
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]是的，女士。
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="无名古尸"]是的，女士。
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]嗨，学人精。
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="无名古尸"]嗨，学人精。
[Dialog]
[charslot(slot = "m", focus = "all")]
[charslot(slot = "left",posfrom = "80,0", posto = "60,0",duration = 0.8)]
[Delay(time=1)]
[CameraShake(duration=0.3,xstrength=3,ystrength=0,vibrato=10,randomness=90,fadeout=true,block=true)]
缓缓抽回手，女孩又握住尸体的手，用尽力气攥紧，而尸体也回握住她。
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="无名古尸"]......
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="l")]
[name="佩佩"]我就当你答应了。
[stopmusic(fadetime=3)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="53_g5_museum",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[delay(time=1)]
[playsound(key="$d_gen_walk_n",volume=0.7,channel="2")]
[charslot(slot="m",name="avg_4138_narant_1#2$1",duration=1)]
[delay(time=1.5)]
[name="娜仁图亚"]阿雅吉，我已经到了，为什么我没在门前看到你？
[name="娜仁图亚"]你现在在哪里？
[Dialog]
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_4138_narant_1#9$1")]
[name="娜仁图亚"]什么？！
[charslot(slot="m",name="avg_4138_narant_1#8$1")]
[name="娜仁图亚"]（小声）你说你不知道你现在在哪里？
[name="娜仁图亚"]没有通行证我要怎么进去......该死，这里的馆长把办公室搞得像保险柜一样。
[name="娜仁图亚"]不，来不及了，这会儿人都快疏散干净了！
[Dialog]
[charslot(slot = "m", focus = "n")]
[playsound(key="$d_avg_wind")]
[delay(time=2)]
[charslot(slot="m",name="avg_4138_narant_1#4$1")]
[name="娜仁图亚"]......
[charslot(slot="m",name="avg_4138_narant_1#2$1")]
[name="娜仁图亚"]告诉我......阿雅吉，走廊上的窗户和馆长办公室的窗是相邻的吗？
[name="娜仁图亚"]......是，我知道很高。
[name="娜仁图亚"]我会小心的。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="48_g7_galleriesstaircase",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1477_1#8$1",duration=1)]
[delay(time=1.5)]
[name="阿斯帕齐娅"]第一，博物馆内禁止喧哗。第二，无序乃是理性的大敌。
[name="阿斯帕齐娅"]不要推搡，这里陈列的雕像与大型壁画没有展柜保护，很容易——
[Dialog]
[charslot(slot = "m", name = "avg_npc_1477_1#4$1")]
[charslot(slot = "m",posfrom = "0,0", posto = "150,0",duration = 0.4)]
[delay(time=0.4)]
[charslot(slot = "m",posfrom = "150,0", posto = "120,-30",duration = 0.4)]
[CameraShake(duration=0.3, xstrength=10, ystrength=30, vibrato=25, randomness=90, fadeout=true, block=false)]
[

... (全文19288字符)
```

### level_act35side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="53_g8_sargondeluxeroom",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(key="$normal_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_4139_papyrs_1#3$1",duration=1.5)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$1")]
[name="阿娜特"]唔......
[charslot(slot = "m", focus = "n")]
[name="？？？"]你醒了，阿娜特？
[charslot(slot = "r", name = "avg_4139_papyrs_1#9$1")]
[name="阿娜特"]嘶......好痛。
[Dialog]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="l")]
[name="佩佩"]你晕倒的时候磕到了后脑勺，可能是因为这个。
[charslot(slot = "r", name = "avg_4139_papyrs_1#9$1",focus="r")]
[name="阿娜特"]可我不止后脑勺痛，我全身都痛，咦，我肩窝上为什么会有淤青？
[playsound(key="$d_avg_clothmovement")]
[charslot(slot = "r", name = "avg_4139_papyrs_1#5$1",focus="r")]
[name="阿娜特"]怎么我的膝盖上也有......？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1479_1#1$1",duration=1)]
[delay(time=1.5)]
[name="无名古尸"]呜......
[charslot]
[Effect(name="$e_emoji_sweat02",layer = 1,x=200,y=170)]
[charslot(slot ="r", action="shake", power=10, times=50, duration=0.3)]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="r")]
[charslot(slot = "r", name = "avg_4139_papyrs_1#6$1",focus="r")]
[name="阿娜特"]啊——！！你不要靠近我！
[charslot(slot = "l", name = "avg_4058_pepe_1#11$1",focus="l")]
[name="佩佩"]冷静！冷静！阿娜特！
[charslot(slot = "r", name = "avg_4139_papyrs_1#6$1",focus="r")]
[name="阿娜特"]谁看到古尸复活都不能冷静吧！那家伙刚才是不是扯了我的耳朵！我的耳朵还在吗？
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]它不过是一具只会模仿人们动作的古尸，对你并无恶意，对其他人也没有。
[name="佩佩"]就当它是个会动的摆设吧，阿娜特！
[charslot]
[charslot(slot="m",name="avg_npc_1479_1#1$1")]
[name="无名古尸"]呜......
[charslot]
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="r")]
[charslot(slot = "r", name = "avg_4139_papyrs_1#7$1",focus="r")]
[name="阿娜特"]......你为什么丝毫不紧张，佩佩？
[charslot(slot = "l", name = "avg_4058_pepe_1#12$1",focus="l")]
[name="佩佩"]请不要用这么犀利的眼神看我，拜托！
[charslot(slot = "r", name = "avg_4139_papyrs_1#7$1",focus="r")]
[name="阿娜特"]你到底做了什么？
[charslot(slot = "l", name = "avg_4058_pepe_1#4$1",focus="l")]
[name="佩佩"]......我昨天将我挖掘到的宝石放入了它的胸腔，上面的源石回路可以将它唤醒。
[charslot(slot = "r", name = "avg_4139_papyrs_1#2$1",focus="r")]
[name="阿娜特"]昨天？
[charslot(slot = "l", name = "avg_4058_pepe_1#5$1",focus="l")]
[name="佩佩"]如此重要的考古发现，你肯定不会拱手让人，法尔贾万达巴德博物馆在陛下心中地位特殊，就算我是帕夏之女也没奈何。
[name="佩佩"]所以......只能背着你偷偷进来了。
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$1",focus="r")]
[name="阿娜特"]佩佩，我不想把它借给你是有理由的。
[charslot(slot = "l", name = "avg_4058_pepe_1#6$2",focus="l")]
[name="佩佩"]什么理由？放心好了，论文上加个署名的事情，没问题。
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$1",focus="r")]
[name="阿娜特"]不是这个......
[charslot(slot = "l", name = "avg_4058_pepe_1#7$2",focus="l")]
[name="佩佩"]投资？赞助？哪怕是翻修整个展馆都可以！
[stopmusic(fadetime=2)]
[charslot(slot = "r", name = "avg_4139_papyrs_1#9$1",focus="r")]
[name="阿娜特"]......
[charslot(slot = "l", name = "avg_4058_pepe_1#4$2",focus="l")]
[name="佩佩"]你这是什么眼神？
[playMusic(intro="$newhope01_intro",key="$newhope01_loop", volume=0.6)]
[charslot(slot = "r", name = "avg_4139_papyrs_1#9$1",focus="r")]
[name="阿娜特"]我只是不懂......你为何如此执着地要成为沙尔-阿加德的史官？就算继承了你父亲的帕夏头衔，你依然可以继续自己的研究。
[name="阿娜特"]你明知道作为史官进入黄金之城后，就再也无法离开那里了。
[name="阿娜特"]学院中学习到的一切，为深入沙漠寻找遗迹而经受的训练，四处游历的见闻，在你成为史官后将再也无法派上用场。
[name="阿娜特"]或许，你只是不甘心那个被选中的人是你的弟弟？
[charslot(slot = "l", name = "avg_4058_pepe_1#5$1",focus="l")]
[name="佩佩"]......我不是逞一时意气才想要成为史官的。这是我们家族中每个成员的梦想。
[charslot(slot = "l", name = "avg_4058_pepe_1#4$1",focus="l")]
[name="佩佩"]在小的时候，谁不期待着长辈将那支金色的灯芯草笔交给自己。
[name="佩佩"]他们会告诉你，拿起这支笔，你便要承担非凡的责任，记述所有曾经发生的事情以供后人阅览。
[name="佩佩"]你所记载的、所传递的是属于时代的真相。是不会被深埋进黄沙与泥土，不经猜测与考察便能得出的最为完整的真相。
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]这就是我从小到大一直想要做的。
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1",focus="l")]
[name="佩佩"]我想要参与记述萨尔贡的历史！我想要沙阿的荣光在我的笔下焕发出永恒的生命力，持续照耀着每一个读到它的人。
[name="佩佩"]在千年万年后，有一个我注定无缘得见的家伙，他会从那些文字中，与我，与沙阿产生共鸣，我们三人由此而连结。
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]想想，阿娜特，这不是很浪漫的事情吗？
[charslot(slot = "r", name = "avg_4139_papyrs_1#10$1",focus="r")]
[name="阿娜特"]唉......
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$1",focus="r")]
[name="阿娜特"]你的坚持，我都看在眼里......你从来都是不到头不死心。
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="l")]
[name="佩佩"]我就是这种执拗的人嘛，我还以为你和缇缇早就习惯了。
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$1",focus="r")]
[name="阿娜特"]......好，我可以代表博物馆出借这件文物，以及......另外一颗宝石。
[name="阿娜特"]多年前一位私人收藏家赠送给我们，研究时我们发现这具古尸与宝石有关联，但具体的使用方法我们毫无头绪。
[charslot(slot = "l", name = "avg_4058_pepe_1#11$1",focus="l")]
[name="佩佩"]在博物馆里也有一颗宝石？！
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$1",focus="r")]
[name="阿娜特"]这不重要，重要的是我也会一同将它交给你研究。
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1",focus="l")]
[name="佩佩"]就这么轻易地给我吗？
[charslot(slot = "r", name = "avg_4139_papyrs_1#7$1",focus="r")]
[name="阿娜特"]怎么可能？除了署名、投资、赞助，还有新展馆的冠名费，一个都不能少哦！
[charslot(slot = "l", name = "avg_4058_pepe_1#6$2",focus="l")]
[name="佩佩"]都是小钱！都是小事！
[charslot(slot = "r", name = "avg_4139_papyrs_1#2$1",focus="r")]
[name="阿娜特"]佩佩......
[charslot(slot = "l", name = "avg_4058_pepe_1#1$2",focus="l")]
[name="佩佩"]嗯？
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$1",focus="r")]
[name="阿娜特"]我还是希望你能接受，有些时候，没结果也是一种结果。
[charslot(duration=0.5)]
[PlaySound(key="$d_avg_open_drawer", volume=1)]
阿娜特打开抽屉，拿出一个层层裹好的布包。
掀开布料，一颗四棱锥体的宝石躺在其中，和放入尸体胸腔中的别无二致。
接过宝石，佩佩难以抑制内心的惊喜，简直就要惊呼出来。
[Dialog]
[MusicVolume(volume=0, fadetime=2)]
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",duration=1)]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="l")]
[name="佩佩"]“第二颗代表肺，当我们初次呼吸，记忆便开始。”
[Dialog]
[charslot(slot = "left",posfrom = "0,0", posto = "50,0",duration = 1)]
[Delay(time=1.5)]
[charslot(slot = "l", name = "avg_40

... (全文20672字符)
```

### level_act35side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="53_g8_sargondeluxeroom",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$farce_intro",key="$farce_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot = "m", name = "avg_4139_papyrs_1#1$1",duration=1)]
[delay(time=2)]
[name="阿娜特"]缇缇......
[charslot(slot = "m", name = "avg_npc_1478_1#10$1")]
[name="梅捷缇克缇"]去，捡回来！
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1488_1#1$1",posfrom = "-200,0", posto = "-200,0",duration = 0.3)]
[delay(time=0.5)]
[playsound(key="$d_avg_slip")]
[charslot(slot = "m", action="jump",posto = "400,0",power=15,times=1,duration = 0.4)]
[delay(time=0.41)]
[name="宝石构装体"]（飞速接球）
[Dialog]
[playsound(key="$d_avg_slip")]
[charslot(slot = "m", action="jump",posto = "-400,0",power=-15,times=1,duration = 0.4)]
[delay(time=0.41)]
[name="宝石构装体"]（飞速捡回）
[charslot]
[Effect(name="$e_emoji_kira",layer = 1,x=50,y=200)]
[charslot(slot = "m", name = "avg_npc_1478_1#10$1")]
[name="梅捷缇克缇"]嘿嘿嘿，谁是最乖的小可爱啊！嘿嘿，是你呀，小东西。
[charslot(slot = "m", name = "avg_4139_papyrs_1#7$1")]
[name="阿娜特"]缇缇，别玩了！
[charslot(slot = "m", name = "avg_npc_1478_1#9$1")]
[name="梅捷缇克缇"]以前家里不让养宠物，我一直都很想养一只的，看，它好乖的！
[charslot(slot = "m", name = "avg_4139_papyrs_1#7$1")]
[name="阿娜特"]那不是宠物，是博物馆里的文物。
[charslot(slot = "m", name = "avg_npc_1478_1#5$1")]
[name="梅捷缇克缇"]你怎么不管佩佩？你看，她甚至在冲着博物馆的文物发火！
[charslot]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="佩佩"]你再给我说一遍！
[name="祖拜尔"]很抱歉......佩佩小姐，我无法回答，搜索过记忆后，宝库的位置仍是模糊一片。
[charslot(slot = "m", name = "avg_npc_1478_1#5$1")]
[name="梅捷缇克缇"]真的不要拦一下她吗？感觉那具古尸缩在那里的样子有点可怜......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot = "r", name = "avg_npc_1479_1#1$1")]
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "l",posfrom = "0,0", posto = "50,0",duration = 0.4)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1",focus="l")]
[name="佩佩"]不行，再冥思苦想一下！说不定就回忆起来了！
[Dialog]
[charslot(slot = "r",posfrom = "0,0", posto = "50,0",duration = 0.6)]
[delay(time=0.7)]
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]那都只是无用功......
[name="祖拜尔"]为了确保秘密不被轻易透露，分割我记忆的人将有关宝库位置的信息打乱，均匀散布在每一颗宝石中。
[name="祖拜尔"]这样的宝石有五颗，或许你需要将它们收集齐全，我才能告知你答案。
[Dialog]
[charslot(slot = "l",posfrom = "50,0", posto = "100,0",duration = 0.4)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1",focus="l")]
[name="佩佩"]那其余宝石的位置在哪里？！这个你总知道吧！
[charslot(slot = "r", name = "avg_npc_1479_1#2$1",focus="r")]
[name="祖拜尔"]（摇头）
[Dialog]
[charslot(slot = "l", name = "avg_4058_pepe_1#9$2",focus="l")]
[charslot(slot = "l", action="jump",power=20,times=1,duration = 0.3)]
[delay(time=0.31)]
[charslot(slot = "l", name = "avg_4058_pepe_1#9$2",focus="l")]
[name="佩佩"]你不知道！
[Dialog]
[charslot(slot = "r",posfrom = "50,0", posto = "100,0",duration = 0.6)]
[delay(time=0.7)]
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]那支将我击败的军队，由许多帕夏和王酋集结......他们离去时，宝石也被他们带走。
[charslot(slot = "l", name = "avg_4058_pepe_1#4$2",focus="l")]
[name="佩佩"]找到它们的机会听起来非常渺茫......
[Dialog]
[charslot(slot = "l",posfrom = "100,0", posto = "150,0",duration = 0.3)]
[charslot(slot = "l", name = "avg_4058_pepe_1#8$2",focus="l")]
[name="佩佩"]不，也许还有其他的办法！给我再用你的黄金脑袋想想！
[Dialog]
[charslot(slot = "r",posfrom = "100,0", posto = "160,0",duration = 0.9)]
[delay(time=0.7)]
面对佩佩的步步逼问，高大的祖拜尔慢慢退至墙角。
从面前这个不及自己胸口高的女孩身上，他感受到莫大的威压，甚至那副坚硬的金属膝盖都只能勉强支撑身体。
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]请不要焦急......女士......
[charslot(slot = "l", name = "avg_4058_pepe_1#8$2",focus="l")]
[name="佩佩"]那你倒是说点有用的哇！
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]宝石之间存在微弱的引力，只要它们在我附近，我就能感知到。
[charslot(slot = "l", name = "avg_4058_pepe_1#9$2",focus="l")]
[name="佩佩"]你在开什么玩笑！难道我要带着你走遍萨尔贡吗？单这座城市中的宝石数量就是以千万计的！
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]我刚才好像隐约感知到了......
[charslot(slot = "l", name = "avg_4058_pepe_1#11$2",focus="l")]
[name="佩佩"]......
[Effect(name="$e_emoji_proud",layer = 1,x=-30,y=150)]
[charslot(slot = "l", name = "avg_4058_pepe_1#7$1",focus="l")]
[name="佩佩"]那还等什么，现在就走吧。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "m", name = "avg_npc_1478_1#4$1")]
[name="梅捷缇克缇"]你看，阿娜特，她甚至想把博物馆的文物带出去！
[charslot(slot = "m", name = "avg_4139_papyrs_1#8$1")]
[name="阿娜特"]......
[name="阿娜特"]佩佩，祖拜尔先生是博物馆的珍贵文物，我们必须确保他一直处在适宜的储存环境中，外界环境复杂，不能让他直接接触。
[name="阿娜特"]你得打消这个念头，留在这里研究，千万不要出去。
[charslot(slot = "m", name = "avg_4058_pepe_1#3$2")]
[name="佩佩"]明年追加百分之四十的投资？
[charslot(slot = "m", name = "avg_4139_papyrs_1#8$1")]
[name="阿娜特"]不行。
[charslot(slot = "m", name = "avg_4058_pepe_1#8$1")]
[name="佩佩"]加一倍？
[charslot(slot = "m", name = "avg_4139_papyrs_1#7$1")]
[name="阿娜特"]我会让员工一直盯着你们的，回见。
[Dialog]
[charslot(duration=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[delay(time=2.5)]
[charslot(slot = "m", name = "avg_4058_pepe_1#4$1")]
[name="佩佩"]她现在怎么油盐不进的......？
[charslot(slot = "m", name = "avg_npc_1478_1#9$1")]
[name="梅捷缇克缇"]祖拜尔先生，虽然讨要别人的陪葬品不是什么礼貌之举，但我还是想问下。
[charslot(slot = "m", name = "avg_npc_1478_1#10$1")]
[name="梅捷缇克缇"]你可以把它借我玩两天吗？
[Dialog]
[charslot(slot = "m", name = "avg_npc_1488_1#1$1")]
[charslot(slot = "m",posfrom = "0,0", posto = "100,0",duration = 0.3,isblock=true)]
[charslot(slot = "m",posfrom = "100,0", posto = "0,0",duration = 0.3,block=true)]
[name="宝石构装体"]（飞速转圈）
[charslot(slot = "m", name = "avg_npc_1479_1#1$1")]
[name="祖拜尔"]......
[name="祖拜尔"]当然可以，女士。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="53_g2_menatmainstreet_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=

... (全文26138字符)
```

### level_act35side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="53_g4_ctizengarden",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(key="$m_avg_dailylifeofsargon_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",duration=1)]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",duration=1)]
[Delay(time=2)]
[charslot(slot = "left", posfrom = "0,0", posto = "100,0",duration = 0.7)]
[Delay(time=1)]
[charslot(slot = "left", posfrom = "100,0", posto = "100,-50",duration = 0.8)]
[charslot(slot = "r", posfrom = "0,0", posto = "0,-50",duration = 0.8)]
[PlaySound(key="$d_avg_grass", volume=1)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="l")]
[name="佩佩"]嘘，你蹲在草丛里等我，不要出来，为了能白天带你出来，我这几天可是花了不少心思。
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]草丛太矮了，我的耳朵会露在外面。
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="l")]
[name="佩佩"]那就再伏低一点！
[Dialog]
[charslot(slot = "left", posfrom = "100,-50", posto = "100,-70",duration = 0.5)]
[charslot(slot = "r", posfrom = "0,-50", posto = "0,-100",duration = 0.5)]
[PlaySound(key="$d_avg_grass", volume=1)]
[Delay(time=1)]
[charslot(slot = "left", posfrom = "100,-70", posto = "100,0",duration = 0.6)]
[Delay(time=0.8)]
[charslot(slot = "left", posfrom = "100,0", posto = "0,0",duration = 0.8)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]哦......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[charslot(slot = "r", name = "avg_npc_1497_1#1$1")]
[charslot(slot = "l", name = "avg_npc_1490_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot = "r", focus="r")]
[name="好奇的女孩"]爸爸，那个姐姐在对绿化带胡乱揉搓耶。
[charslot(slot = "l", focus="l")]
[name="优雅的男子"]嘘，不要对别人指指点点，不礼貌。她一定是喝醉了。
[charslot(slot = "m", focus = "n")]
[name="佩佩"]不行！还是能看见！
[Dialog]
[PlaySound(key="$d_avg_grass", volume=1)]
[delay(time=2)]
[charslot(slot = "r", focus="r")]
[name="好奇的女孩"]那个姐姐快栽进绿化带了耶，我们要不要去拉她一把？
[charslot(slot = "l", focus="l")]
[name="优雅的男子"]嘘，这时候应该假装没有看见，摔一跤不是什么大事，被人看到才有损颜面。
[name="优雅的男子"]漫灌节的节前祭祀盛典会在这里举办，今日都是来报名的选手，比赛时要是不小心碰到，那就太尴尬了。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot = "r",posfrom = "0,0", posto = "200,0",duration = 1)]
[charslot(slot = "l",posfrom = "0,0", posto = "200,0",duration = 1)]
[charslot(slot = "r",afrom = 1, ato = 0,duration = 1)]
[charslot(slot = "l",afrom = 1, ato = 0,duration = 1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot = "r", name = "avg_npc_1479_1#1$1", posfrom = "0,-100", posto = "0,-100")]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "l", name = "avg_4058_pepe_1#4$1",focus="l")]
[name="佩佩"]米纳特哈玛仪有个小传统，在漫灌节前，附近的居民们会带来各种各样珍奇沉入河中来祭祀河神，向祂祈求好运。
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="l")]
[name="佩佩"]猜猜这座城市中最贵重的宝石在哪里？
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]就在这片河道中。
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="l")]
[name="佩佩"]你在这里等等，我去搞一辆修剪灌木丛的小推车，你可以坐在收集落叶的大桶里。
[charslot(slot = "l", name = "avg_4058_pepe_1#6$1",focus="l")]
[name="佩佩"]这样推着你到河边去没人会发现的！
[dialog]
[charslot(slot = "r",posfrom = "0,-100", posto = "-30,-100",duration = 0.5,isblock=true)]
[charslot(slot = "r",posfrom = "-30,-100", posto = "0,-100",duration = 0.5)]
[charslot(slot = "l",posfrom = "0,0", posto = "30,0",duration = 0.5,isblock=true)]
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]你确定这样行得通吗？
[dialog]
[charslot(slot = "l",posfrom = "30,0", posto = "0,0",duration = 0.5,block=true)]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",focus="l")]
[name="佩佩"]好啦，别扯我衣角，成熟一点，老古董！
[name="佩佩"]躲好，不要乱动！我马上就回来！
[Dialog]
[charslot(slot = "l",posfrom = "0,0", posto = "-200,0",duration = 1,afrom=1,ato=0)]
[PlaySound(key="$rungeneral", volume=0.7)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]......
[Dialog]
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$d_avg_grass", volume=0.7)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1482_1#1$1",posfrom = "0,0", posto = "0,0",duration = 1)]
[delay(time=2)]
[PlaySound(key="$d_avg_meownormal")]
[charslot(slot = "l", focus="l")]
[name="米奥"]喵......喵嗷......
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]嗯......动物？
[charslot(slot = "l", name = "avg_npc_1482_1#2$1",focus="l")]
[name="米奥"]（优雅地翘起尾巴）
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]啊，这里有很多雕像正是依着你的模样刻绘的。
[charslot(slot = "l", name = "avg_npc_1482_1#3$1",focus="l")]
[name="米奥"]（得意地晃动尾巴）
[charslot(slot = "r", name = "avg_npc_1479_1#5$1",focus="r")]
[name="祖拜尔"]真是个漂亮的家伙，怪不得这里的人会这样喜爱你。
[charslot(slot = "l", name = "avg_npc_1482_1#2$1",focus="l")]
[name="米奥"]（矜持地撅起臀部）
[charslot(slot = "r", name = "avg_npc_1479_1#5$1",focus="r")]
[name="祖拜尔"]哦......你是想让我摸摸你吗？可是你离我有些远，佩佩让我留在这里不要乱动。
[charslot(slot = "l", focus="l")]
[name="米奥"]（刻意地卖弄风情）
[charslot(slot = "r", name = "avg_npc_1479_1#5$1",focus="r")]
[name="祖拜尔"]你可以走近一些吗？
[charslot(slot = "l", name = "avg_npc_1482_1#4$1",focus="l")]
[name="米奥"]（不悦地扫动尾巴）
[charslot(slot = "r", name = "avg_npc_1479_1#5$1",focus="r")]
[name="祖拜尔"]请不要生气，或许我往前挪挪也不是不可以。
[charslot(slot = "l", name = "avg_npc_1482_1#2$1",focus="l")]
[name="米奥"]喵嗷......
[Dialog]
[playsound(key="$d_avg_wellwheel")]
[charslot(slot = "m", focus = "n")]
[delay(time=1)]
[playsound(key="$d_avg_meownormal")]
[charslot(slot = "l", focus="l")]
[name="米奥"]喵！
[Dialog]
[charslot(slot = "l", name = "avg_npc_1482_1#7$1")]
[charslot(slot = "l", action="jump",posto = "200,-5",power=15,times=1,duration = 0.7,afrom=1,ato=0)]
[delay(time=0.71)]
[charslot(slot = "r", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]别跑！
[Dialog]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$1",posfro

... (全文24012字符)
```

### level_act35side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="53_g4_ctizengarden",screenadapt="coverall")]
[Delay(time=1)]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.4, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(key="$comedy_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1492_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_4058_pepe_1#1$1",duration = 1)]
[delay(time=2)]
[StopSound(channel="bgs", fadetime=2)]
[charslot(slot = "left", focus="l")]
[name="出身高贵的学者"]哦，能够在此遇到您真是我的殊荣，哈特谢普苏特女士。
[name="出身高贵的学者"]您此次带来的新历纪时代初期制成的拖鞋当真是令我大开眼界，想不到数百年前的古人有如此精妙的制鞋工艺。
[name="出身高贵的学者"]他们竟然能锻造出如此贴合足部曲线的鞋履，上面装饰的莲花纹饰，更是生动无比。
[name="出身高贵的学者"]更不用说，这只拖鞋诞生自那场大爆炸不久后，体现了当地气候剧烈变化的一面。
[name="出身高贵的学者"]只可惜，拖鞋只有一只，不能凑成一双，恐怕不能在比赛中夺下第一啊。
[charslot(slot = "right", name = "avg_4058_pepe_1#3$2",focus="r")]
[name="佩佩"]没关系，能拿个二等奖也不错，重在参与嘛。
[charslot(slot = "left", focus="l")]
[name="出身高贵的学者"]也是，哈特谢普苏特女士您贵为帕夏之女，未来更是要继承帕夏之位，肯定不在乎这些微末荣誉。
[charslot(slot = "right", name = "avg_4058_pepe_1#4$2",focus="r")]
[name="佩佩"]这个......还早啦，很多事情都说不定呢。
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_177")]
[name="地位不凡的富商"]可我听闻哈特谢普苏特女士的幼弟已经被定为史官职位的继承者，两个月后便要出发前往黄金之城了。
[charslot(slot = "m", name = "avg_npc_1492_1#1$1")]
[name="出身高贵的学者"]唉，像哈特谢普苏特女士这样天资非同一般的孩子都没能中选，可见令弟的天赋之高。
[charslot(slot = "m", name = "avg_4058_pepe_1#3$2")]
[name="佩佩"]唉......都一样都一样，我和他差不多啦。
[charslot(slot = "m", name = "avg_npc_177")]
[name="地位不凡的富商"]看您说的，难道成为帕夏就不需要天赋与能力了吗？我看哈特谢普苏特女士要是成为帕夏，也必定能为家族延续荣光。
[charslot(slot = "m", name = "avg_npc_1492_1#1$1")]
[name="出身高贵的学者"]还是不一样的，毕竟哈特谢普苏特女士的家族是萨尔贡最为辉煌的史官家族啊。
[charslot(slot = "m", name = "avg_4058_pepe_1#5$1")]
[name="佩佩"]......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="53_g3_menatmainstreet_river",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "right", name = "avg_4138_narant_1#1$1",duration=0.7)]
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",duration=0.7)]
[delay(time=1.5)]
[charslot(slot = "right", name = "avg_4138_narant_1#1$1",focus="r")]
[name="娜仁图亚"]马上就轮到我们登记了，你想好了吗？
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]没有。
[charslot(slot = "right", name = "avg_4138_narant_1#12$1",focus="r")]
[name="娜仁图亚"]你那么自信地走进参赛的报名队伍，结果身上什么珍宝都没有？
[charslot(slot = "left", name = "avg_npc_1477_1#4$1",focus="l")]
[name="阿斯帕齐娅"]你觉得我走路的仪态有什么需要改进的地方吗？
[charslot(slot = "right", name = "avg_4138_narant_1#3$1",focus="r")]
[name="娜仁图亚"]没什么，算了。
[charslot(slot = "right", name = "avg_4138_narant_1#1$1",focus="r")]
[name="娜仁图亚"]看来这种时候，你还是得靠我。
[name="娜仁图亚"]我是不会看着我的手下吃亏的。给我一点时间，我想想办法。
[charslot(slot = "left", name = "avg_npc_1477_1#2$1",focus="l")]
[name="阿斯帕齐娅"]......
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]我在短跑竞速赛拿过银牌。
[charslot(slot = "right", name = "avg_4138_narant_1#12$1",focus="r")]
[name="娜仁图亚"]你想拿起那个金杯子就跑？不行。
[name="娜仁图亚"]这些有钱人带着的护卫，来头都不小。看那个人转身的步法就知道他在王酋的军队里干了不少年。
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]我在无甲格斗中也拿了银牌。
[charslot(slot = "right", name = "avg_4138_narant_1#12$1",focus="r")]
[name="娜仁图亚"]打劫？被抢的人就在现场，我们怎么可能拿抢来的东西参赛。
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]还有，在祭典舞蹈大赛中，我也拿了银牌。
[charslot(slot = "right", name = "avg_4138_narant_1#12$1",focus="r")]
[name="娜仁图亚"]......你要走这个路数？
[charslot(slot = "right", name = "avg_4138_narant_1#3$1",focus="r")]
[name="娜仁图亚"]唉，不用为难自己......
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]实际上，我在十个不同的项目里获得了十枚银牌，并且我一直将它们带在身边。
[charslot(slot = "right", name = "avg_4138_narant_1#10$1",focus="r")]
[name="娜仁图亚"]——十枚银牌？
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]这些奖牌是米诺斯传统文化的体现，也是我个人最为珍视的荣誉。
[name="阿斯帕齐娅"]荣誉本不该被当做可比试高低的珍奇，但情况特殊，我只有如此选择。
[name="阿斯帕齐娅"]另外，娜仁图亚，我希望你不要误解我。我绝不会以那样不正当的手段参与竞争，那会使我的家族蒙羞。
[charslot(slot = "right", name = "avg_4138_narant_1#10$1",focus="r")]
[name="娜仁图亚"]......
[charslot(slot = "right", name = "avg_4138_narant_1#4$1",focus="r")]
[name="娜仁图亚"]之前我确实误解你了。
[charslot(slot = "right", name = "avg_4138_narant_1#11$1",focus="r")]
[name="娜仁图亚"]唉，我的靠谱手下，我的大事业......
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]抱歉，你刚刚说什么？
[charslot(slot = "right", name = "avg_4138_narant_1#1$1",focus="r")]
[name="娜仁图亚"]没什么。我在说你怎么一块金牌都没有，难怪那么想要那个金杯子，哈哈。
[name="娜仁图亚"]放心，我有计划了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="53_g8_sargondeluxeroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1494_1#1$1")]
[name="紧张的集会裁判"]......
[name="紧张的集会裁判"]咳......
[name="紧张的集会裁判"]......请问......使者引我到这里，是为了什么指示？
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_4058_pepe_1#1$1",duration=1,bstart=0.3,bend=0.7)]
[delay(time=2)]
[name="宝石屏风后的女性"]嗯？没有没有，不是什么指示，就是想拜托你一件事。
[name="宝石屏风后的女性"]如果你看到一只黄金拖鞋......不要给它太高的分。
[name="宝石屏风后的女性"]啊，当然也不能太低！还是要保证历史学家的专业性！比如说，第二名的成绩就刚刚好。
[name="宝石屏风后的女性"]拜托啦，这对我真的很重要！
[charslot(slot = "m", name = "avg_npc_1494_1#1$1")]
[name="紧张的集会裁判"]......那件展品本就具有珍贵的历史价值，如果您主观想要降低评分，这也不算对其他参赛者不公平。
[charslot(slot = "m", name = "avg_4058_pepe_1#1$1",bstart=0.3,bend=0.7)]
[name="宝石屏风后的女性"]......
[name="宝石屏风后的女性"]你如果猜到了我的身份，也请帮我保密，谢谢啦。
[charslot(slot = "m", name = "avg_npc_1494_1#1$1")]
[name="紧张的集会裁判"]是，尊敬的女士。
[Dialog]
[charslot(duration=1)]
[delay(time=1.5)]
[PlaySound(key="$doorclosequite")]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1",duration=0.5)]
[delay(time=1)]
[name="佩佩"]......对不起。
[name="佩佩"]以前的老师们，考古行动的同僚们......我之后一定向你们好好道歉。
[charslot(slot = "m", name = "avg_4058_pepe_1#8$1")]
[name="佩佩"]只是......只有这一次，我绝对绝对不能输！凭什么大家都

... (全文20319字符)
```

### level_act35side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="53_g4_ctizengarden",screenadapt="coverall",xScale=1.05, yScale=1.05,x=30)]
[Delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$newhope02_intro",key="$newhope02_loop", volume=0.6)]
[Subtitle(text="♪河岸上摇曳着纸莎草，河面倒映着青金石♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="♪流过黄金沙丘的长河啊，因宝石的供奉永不干涸♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="♪愿我得见祂漫步河畔，愿我随祂的脚步走向永恒♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="53_g4_ctizengarden",screenadapt="coverall")]
[PlaySound(key="$d_avg_applause",volume=0.5,channel="2")]
[PlaySound(key="$d_avg_cheer_street")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$farce_intro",key="$farce_loop", volume=0.6)]
伴随着热烈的掌声与激昂的合唱，沿着璀璨的宝石大道，获奖者们机械地往前走着。
承载了历史厚重感的莎草船缓缓下沉。黄金拖鞋，来自米诺斯的十枚银牌，都变成了水面上的一串气泡。
[Dialog]
[charslot(slot = "left", name = "avg_4058_pepe_1#12$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1491_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_npc_1491_1#1$1",focus="r")]
[name="拉沙德"]遗憾？不，我怎么可能有遗憾呢？见到哈特谢普苏特女士才是我这次参赛最重要的收获！
[name="拉沙德"]相比之下，集会名次又有什么值得在意的呢？......不过，当然，我认为一张失去冠军的人和冠军的合影会很有意义。
[name="拉沙德"]尊敬的哈特谢普苏特女士，不知道您是否愿意赏脸与我合影？如果您愿意展示第一名获得的雕像，那就再好不过了。
[charslot(slot = "left", name = "avg_4058_pepe_1#12$1",focus="l")]
[name="佩佩"]哈哈，当然......谢谢您......
[Dialog]
[charslot(slot = "r",posfrom = "0,0", posto = "-150,0",duration = 1)]
[delay(time=1.3)]
[playsound(key="$skill_flash",volume=0.3,channel="x")]
[Blocker(a=0, r=1, g=1, b=1, afrom=0.3, rfrom=1, gfrom=1, bfrom=1, fadetime=0.3, block=false)]
[delay(time=0.2)]
[Blocker(a=0, r=1, g=1, b=1, afrom=0.4, rfrom=1, gfrom=1, bfrom=1, fadetime=0.3, block=false)]
[playsound(key="$skill_flash",volume=0.3,channel="y")]
[delay(time=0.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "right", name = "avg_4138_narant_1#2$1",duration=1)]
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",duration=1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]我参加了一场荒唐的竞赛。
[charslot(slot = "right", name = "avg_4138_narant_1#12$1",focus="r")]
[name="娜仁图亚"]是啊，一场荒唐的竞赛。
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]我的本意，是对历史的求索，对英雄伟业的尊敬，对胜利孜孜不倦的追求，以及，对命运的诘问。
[charslot(slot = "right", name = "avg_4138_narant_1#1$1",focus="r")]
[name="娜仁图亚"]是啊，对命运的......什么来着。总之，你的十枚银牌变成了一枚新的银牌。
[charslot(slot = "right", name = "avg_4138_narant_1#1$1",focus="r")]
[name="娜仁图亚"]但别太难过，这里可是萨尔贡，所以，这还不算失败。
[name="娜仁图亚"]“地上的黄沙，地下的黄金。”王酋帕夏一句话，沙子就能变得跟金子一样珍贵。
[name="娜仁图亚"]刚才的损失不用放在心上，只要哪天机遇来了，你得到了认可，说不定金杯就会白送给你。
[charslot(slot = "left", name = "avg_npc_1477_1#3$1",focus="l")]
[name="阿斯帕齐娅"]白送？
[charslot(slot = "right", name = "avg_4138_narant_1#4$1",focus="r")]
[name="娜仁图亚"]比如说，去和拿到金杯的人聊聊，骗他信任你......
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]——你说得很对！
[charslot(slot = "right", name = "avg_4138_narant_1#10$1",focus="r")]
[name="娜仁图亚"]啊？
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]我拿出的宝物得到了认可。这也代表着，米诺斯的文化得到了认可。
[name="阿斯帕齐娅"]哪怕裁判席给出的评价十分浅薄，这些银牌得到的分数和名次本身足以证明，专业的萨尔贡历史学者对米诺斯有基本的尊重。
[name="阿斯帕齐娅"]我应该跟拿到金杯的收藏家好好谈谈。他如果也能理解物品背后那段沉重的历史，或许会愿意以一个我负担得起的价格转手。
[charslot(slot = "right", name = "avg_4138_narant_1#4$1",focus="r")]
[name="娜仁图亚"]......真的认可了吗？
[charslot(slot = "right", name = "avg_4138_narant_1#1$1",focus="r")]
[name="娜仁图亚"]好吧，如果这样也算还上了你的人情，那也是好事。
[charslot(slot = "left", name = "avg_npc_1477_1#8$1",focus="l")]
[name="阿斯帕齐娅"]真心感谢，娜仁图亚。
[name="阿斯帕齐娅"]正如那些在白墙下辩论的智者，你点醒了我。我不会失去那些银牌所代表的荣誉，而且现在我获得了更多。
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]相比之下，命运如何捉弄我本人，不值得我在乎。
[charslot(slot = "left", name = "avg_npc_1477_1#2$1",focus="l")]
[name="阿斯帕齐娅"]而且，如果把那些银牌扔进水中，能帮助人们见到自己想见的影子，那我十分乐意效劳。
[charslot(slot = "left", name = "avg_npc_1477_1#1$1",focus="l")]
[name="阿斯帕齐娅"]如果把手里的这颗宝石扔进水中，也能请来人们口中神灵的影子，那我——
[charslot(slot = "right", name = "avg_4138_narant_1#10$1",focus="r")]
[name="娜仁图亚"]——等一下！
[charslot(slot = "right", name = "avg_4138_narant_1#1$1",focus="r")]
[name="娜仁图亚"]我看出来你心情变好了，但是冷静一点，别扔。
[charslot(slot = "right", name = "avg_4138_narant_1#4$1",focus="r")]
[name="娜仁图亚"]我有个想法......或者说，我现在就有一个想见的人。
[charslot(slot = "right", name = "avg_4138_narant_1#5$1",focus="r")]
[name="娜仁图亚"]既然这颗宝石你不太在乎，能不能......借我一用？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="53_g8_sargondeluxeroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "right", name = "avg_npc_1485_1#9$1",duration=0.5)]
[charslot(slot = "left", name = "avg_npc_1484_1#1$1",duration=0.5)]
[delay(time=1)]
[charslot(slot = "right", name = "avg_npc_1485_1#9$1",focus="r")]
[name="阿雅妮"]陷阱已经布置好了。
[name="阿雅妮"]放心吧，我活儿干得很仔细。越是懂行的人越不可能起疑心。
[charslot]
[charslot(slot = "m", name = "avg_4138_narant_1#1$1")]
[name="娜仁图亚"]好。
[charslot]
[charslot(slot = "right", name = "avg_npc_1485_1#9$1",focus="l")]
[charslot(slot = "left", name = "avg_npc_1484_1#1$1",focus="l")]
[name="阿雅吉"]邀约信也悄悄放在那个女孩的包里了。我戴了搬运文物用的手套，肯定不会留下痕迹。
[charslot]
[charslot(slot = "m", name = "avg_4138_narant_1#1$1")]
[name="娜仁图亚"]不错。
[name="娜仁图亚"]后面的事情我来安排。你们对这次计划还有什么疑问吗？
[charslot]
[charslot(slot = "right", name = "avg_npc_1485_1#9$1",focus="l")]
[charslot(slot = "left", name = "avg_npc_1484_1#4$1",focus="l")]
[name="阿雅吉"]有。我不明白，我们的诱饵为什么能钓到帕夏之女？
[name="阿雅吉"]这颗宝石看起来也没什么特别的，就像我和阿雅妮那天从下水道里捞起来的石头一样有很多杂质......
[charslot]
[charslot(slot = "m"

... (全文16919字符)
```

### level_act35side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="53_g1_menatmainstreet_d",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_mictest",volume=1)]
[Delay(time=2)]
[name="博物馆广播"]请排队购票，请排队购票。“与死而复生的沙阿时代将领相会”特别展览正在售票中！
[name="博物馆广播"]请排队购票，请排队购票......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot="m",name="avg_npc_1479_1#1$1")]
[Background(image="53_g6_museum_core",screenadapt="coverall")]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="a",volume=0)]
[SoundVolume(volume=0.7, channel="a",fadetime=2)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$marketplace_intro",key="$marketplace_loop", volume=0.6)]
[name="祖拜尔"]......
[SoundVolume(volume=0.5, fadetime=2,channel="a")]
[charslot(slot = "m", focus = "n")]
[name="狂热的观众"]对，就这样看着我，只看着我，不要看镜头。
[name="狂热的观众"]再稍等一下，我整理一下婚纱！
[name="狂热的观众"]虽然是连夜赶制出来的，但我以我收藏的三千册沙阿传奇小说担保，它一定符合历史！
[charslot(slot="m",name="avg_npc_1479_1#1$1")]
[name="祖拜尔"]本展览禁止使用闪光灯拍照，以免对文物造成损害，请您注意。
[charslot(slot = "m", focus = "n")]
[name="狂热的观众"]来——二十连拍！
[Dialog]
[charslot(slot = "m", focus = "m")]
[Blocker(a=0, r=1, g=1, b=1, afrom=0.3, rfrom=1, gfrom=1, bfrom=1, fadetime=0.3, block=false)]
[playsound(key="$d_avg_takphtrptly")]
[delay(time=0.3)]
[playsound(key="$skill_flash",volume=0.3,channel="x")]
[Blocker(a=0, r=1, g=1, b=1, afrom=0.3, rfrom=1, gfrom=1, bfrom=1, fadetime=0.3, block=false)]
[delay(time=0.2)]
[Blocker(a=0, r=1, g=1, b=1, afrom=0.4, rfrom=1, gfrom=1, bfrom=1, fadetime=0.3, block=false)]
[playsound(key="$skill_flash",volume=0.3,channel="y")]
[delay(time=0.5)]
[name="祖拜尔"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="53_g6_museum_core",screenadapt="coverall",xScale=1.05, yScale=1.05,x=30,y=-50)]
[charslot(slot="m",name="avg_npc_1479_1#1$1",posfrom = "30,-30", posto = "30,-30")]
[delay(time=0.1)]
[BackgroundTween(xFrom=30, xTo=-30, duration=6)]
[charslot(slot = "m",posfrom = "30,-30", posto = "0,-30",duration=6)]
[delay(time=0.2)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.1)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.1)]
[focusout(type="bg", from=0, to=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_201",afrom=0,ato=0)]
[charslot(slot = "left",action="zoom", poszoom = "0.5,0.5", scale=1.1)]
[charslot(slot="l",duration=1,posfrom = "0,-250", posto = "150,-250",duration=1,afrom=0,ato=1)]
[delay(time=1.5)]
[charslot(slot="l",focus="l")]
[name="踩着平衡车的观众"]大家好，现在我终于进入了法尔贾万达巴德博物馆里最神秘的房间。
[name="踩着平衡车的观众"]接下来我将通过流畅的运镜，三百六十度无死角地记录这位将领的英姿，探索辉煌之城死者复生的奥秘。
[Dialog]
[charslot(slot="l",duration=2,posfrom = "150,-250", posto = "350,-250",afrom=1,ato=0,duration=1)]
[delay(time=1.5)]
[charslot(slot="r",name="avg_npc_1497_1#1$1",posfrom = "100,-70", posto = "100,-70",duration=0.5)]
[delay(time=1)]
[charslot(slot="r",focus="r")]
[name="年幼的观众"]爸爸，它的腿里面好像是空的欸。
[Dialog]
[charslot(slot = "r",posfrom = "100,-70", posto = "70,-70",duration = 0.2)]
[PlaySound(key="$d_avg_chopsteeltube",volume=1)]
[CameraShake(duration=0.2, xstrength=10, ystrength=10, vibrato=20, randomness=90, fadeout=true, block=true)]
[charslot(slot = "r",posfrom = "70,-70", posto = "100,-70",duration = 0.2)]
[delay(time=0.5)]
[charslot(slot="r",focus="r")]
[name="年幼的观众"]爸爸你听，敲起来就是空的！
[charslot(slot="r",focus="n")]
[name="打电话的观众"]嗯，对，这批货要尽快送到东国，订单不大，重在信誉......
[Dialog]
[charslot(slot="r",focus="all")]
[delay(time=0.5)]
[charslot(slot = "r",posfrom = "100,-70", posto = "70,-70",duration = 0.2)]
[PlaySound(key="$d_avg_chopsteeltube",volume=1)]
[CameraShake(duration=0.2, xstrength=10, ystrength=10, vibrato=20, randomness=90, fadeout=true, block=true)]
[charslot(slot = "r",posfrom = "70,-70", posto = "100,-70",duration = 0.2)]
[delay(time=0.21)]
[charslot(slot = "r",posfrom = "100,-70", posto = "70,-70",duration = 0.2)]
[PlaySound(key="$d_avg_chopsteeltube",volume=1)]
[CameraShake(duration=0.2, xstrength=10, ystrength=10, vibrato=20, randomness=90, fadeout=true, block=true)]
[charslot(slot = "r",posfrom = "70,-70", posto = "100,-70",duration = 0.2)]
[delay(time=0.5)]
[charslot(slot="r",focus="n")]
[name="博物馆员工"]先生，麻烦管一下您的女儿。
[name="打电话的观众"]抱歉，等一下，我这边有点事......喂，过来！别乱摸！
[Dialog]
[charslot(slot = "r",posfrom = "100,-70", posto = "200,-70",duration = 1,afrom=1,ato=0)]
[delay(time=1.2)]
[charslot(slot="r",focus="n")]
[name="博物馆员工"]请不要在博物馆里大声喧哗......
[name="打电话的观众"]哎，你们自己要搞这种开放式展览，让你们那个展品到处走的嘛！还不限票，自己搞得展馆这么吵！
[charslot(slot="r",focus="m")]
[name="祖拜尔"]这是由于，本馆代理馆长阿娜特认为“历史与知识对所有人都是平等的”，不应该设置贵宾票。
[name="祖拜尔"]另外，我所处的展台周围高约六十厘米的护栏，本身具有阻拦游客进入的作用。您的孩子越过护栏，将被视为违规行为。
[name="祖拜尔"]请配合工作人员......
[Dialog]
[PlaySound(key="$d_avg_mummyhit",volume=1)]
[delay(time=0.3)]
[PlaySound(key="$d_avg_dropspanner",volume=0.5)]
[CameraShake(duration=0.2, xstrength=10, ystrength=10, vibrato=20, randomness=90, fadeout=true, block=true)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_523_1#1$1", afrom = 0, ato = 0,posfrom = "300,-300", posto = "300,-300")]
[charslot(slot ="r", name = "avg_npc_524_1#1$1", afrom = 0, ato = 0,posfrom = "200,-300", posto = "200,-300")]
[delay(time=0.1)]
[charslot(slot = "r",action="zoom", poszoom = "0.5,0.5", scale=1.05)]
[charslot(slot = "r",action="zoom", poszoom = "0.5,0.5", scale=1.05)]
[delay(time=0.1)]
[charslot(slot = "l",afrom = 0, ato = 1,duration=1)]
[charslot(slot ="r", afrom = 0, ato = 1,duration=1)]
[delay(time=1.5)]
[charslot(slot = "l",focus="l")]
[name="拿着硬币的游客"]唉，没投进去！
[charslot(slot = "r",focus="r")]
[name="看导览手册的游客"]手册上没写外国货币有没有用啊。
[name="看导览手册的游客"]好吧，手册上根本没写把硬币扔进去就有好运。
[charslot(slot = "l",focus="l")]
[name="拿着硬币的游客"]试试看，万一呢？
[charslot(slot = "r",focus="r")]
[name="看导览手册的游客"]......给我一枚。往它的身体中间投对吧？
[charslot(slot="r",focus="n")]
[name="博物馆员

... (全文31899字符)
```

### level_act35side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="53_g1_menatmainstreet_d",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_4138_narant_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]我们在等什么？
[charslot(slot = "left", name = "avg_4138_narant_1#1$1",focus="l")]
[name="娜仁图亚"]电话。对你这样上年纪的人来说，可能是有点新奇。
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]我们还要在这里等多久？
[charslot(slot = "left", name = "avg_4138_narant_1#7$1",focus="l")]
[name="娜仁图亚"]不要怀疑，等就是了。
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]等会儿能让我接电话吗？之前已经有人给我讲解过用法......
[charslot(slot = "left", name = "avg_4138_narant_1#3$1",focus="l")]
[name="娜仁图亚"]不不不，不行，你这个机械合成的嗓音一出声，别人会当成诈骗电话的。
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]好吧。
[charslot(slot = "left", name = "avg_4138_narant_1#1$1",focus="l")]
[name="娜仁图亚"]对了，按照你的说法，我们俩的合作是对历史上伟大同盟的效仿。
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]是的。
[charslot(slot = "left", name = "avg_4138_narant_1#1$1",focus="l")]
[name="娜仁图亚"]那请问，给你跑腿找宝石对我有什么好处？
[charslot(slot = "left", name = "avg_4138_narant_1#4$1",focus="l")]
[name="娜仁图亚"]哦，我确实有所收获。昨天半夜你吓到我的时候，我收获了这只飞到脸上的金拖鞋。
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]你有什么建议吗？
[charslot(slot = "left", name = "avg_4138_narant_1#6$1",focus="l")]
[name="娜仁图亚"]——不敢有，不敢有，我活着就是您最大的恩赐，您是萨尔贡的祖宗，带着您寻找宝石是我该做的，您千万别激动。
[charslot(slot = "left", name = "avg_4138_narant_1#12$1",focus="l")]
[name="娜仁图亚"]不过，赢得丰获集会第一名的文物好像也是这么一只纯金镶蓝宝石的拖鞋......
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]是的，它们应该恰好成对。
[charslot(slot = "left", name = "avg_4138_narant_1#3$1",focus="l")]
[name="娜仁图亚"]这么说......
[name="娜仁图亚"]半夜在大街上尖叫扰民，也是一种发家手段？
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]......原本成对的文物，其中一件永远沉进河底遗失，另一件自然也失去了大半价值。
[charslot(slot = "left", name = "avg_4138_narant_1#2$1",focus="l")]
[name="娜仁图亚"]哦。
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]......请允许我好奇。这个时代的梦魇......都是像你这样行事的吗？
[charslot(slot = "left", name = "avg_4138_narant_1#1$1",focus="l")]
[name="娜仁图亚"]你问倒我了。
[name="娜仁图亚"]为了打劫、倒卖和绑架，我调查过各大部族的风俗和信仰，但真没调查过我自己的出生地。
[name="娜仁图亚"]从某个清晨日出之后，我就再也没回去过了。
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]如此说来，你难道......正走在自己的天途上？
[charslot(slot = "left", name = "avg_4138_narant_1#12$1",focus="l")]
[name="娜仁图亚"]天途？
[charslot(slot = "left", name = "avg_4138_narant_1#3$1",focus="l")]
[name="娜仁图亚"]（古老的语言）天途。
[charslot(slot = "left", name = "avg_4138_narant_1#2$1",focus="l")]
[name="娜仁图亚"]——不不不，我一点也不想听到这个词。
[name="娜仁图亚"]我才不走天途，就算是我的老祖宗逼我也没用。
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]你难道至今没有践行成年的仪式？！
[charslot(slot = "left", name = "avg_4138_narant_1#1$1",focus="l")]
[name="娜仁图亚"]是啊，又不是什么重要的事情。
[name="娜仁图亚"]我也许有一点梦魇的血统，但那几滴血没把我变成暴君和征服者，我也不打算让它影响我自己的生活。
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]不，这很重要。
[name="祖拜尔"]若不走过天途，你的血要如何被你的先祖认可？
[charslot(slot = "left", name = "avg_4138_narant_1#1$1",focus="l")]
[name="娜仁图亚"]没事，我的老祖宗们多半都失踪在大地尽头了，不会像你一样突然从博物馆里坐起来骂我。
[name="娜仁图亚"]对了，那你呢？
[name="娜仁图亚"]我听说沙阿时代的人们会在成年时剃个光头，然后涂上香膏。但又有人说，所谓的“香膏”其实很难闻......我可好奇了。
[charslot(slot = "right", name = "avg_npc_1479_1#1$1",focus="r")]
[name="祖拜尔"]......
[name="祖拜尔"]我也......
[Dialog]
[charslot(slot = "m", focus = "n")]
[playsound(key="$phonevibration")]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_4138_narant_1#5$1",focus="l")]
[name="娜仁图亚"]哎呀，等到了。
[dialog]
[charslot(slot = "right",afrom=1,ato=0,duration=0.5)]
[delay(time=0.51)]
[playsound(key="$d_avg_ringoff")]
[interlude(maskid = "group_interclude_vertical_common" ,size = "290,760", style=0 , offset = "250,0", channel = 3,tsfrom = "0,1", tsto="1,1",tsduration = 0.5)]
[interlude(channel = 3, type = 3, slot = "m", switch = false, pfrom = "270,0", pto="270,0", name = "avg_npc_1490_1#1$1",duration = 0)]
[Delay(time=1)]
[charslot(slot = "left", name = "avg_4138_narant_1#1$1",focus="l")]
[name="娜仁图亚"]......怎么，这么快就有宝石的消息了吗？
[interlude(channel = 3, switch = true, type = 3, slot = "m", pfrom = "270,0", pto="270,0", name = "avg_npc_1490_1#1$1", duration = 0)]
[charslot(slot = "m", focus = "n")]
[name="宝石掮客"]是的，女士，十分巧合，刚刚宝石交易所的监管人放出消息，他手中有一块宝石亟待交易，各方面都符合您的描述。
[charslot(slot = "left", name = "avg_4138_narant_1#1$1",focus="l")]
[interlude(channel = 3, switch = false, type = 3, slot = "m", pfrom = "270,0", pto="270,0", name = "avg_npc_1490_1#1$1", duration = 0)]
[name="娜仁图亚"]好，我要直接去见他。
[charslot(slot = "m", focus = "n")]
[interlude(channel = 3, switch = true, type = 3, slot = "m", pfrom = "270,0", pto="270,0", name = "avg_npc_1490_1#1$1", duration = 0)]
[name="宝石掮客"]但是......即使有我从中介绍，你也很难直接和监管人谈这笔交易。
[interlude(channel = 3, switch = false, type = 3, slot = "m", pfrom = "270,0", pto="270,0", name = "avg_npc_1490_1#1$1", duration = 0)]
[charslot(slot = "left", name = "avg_4138_narant_1#12$1",focus="l")]
[name="娜仁图亚"]什么？我听我手下说，她们直接找前台就能卖宝石。
[charslot(slot = "m", focus = "n")]
[interlude(channel = 3, switch = true, type = 3, slot = "m", pfrom = "270,0", pto="270,0", name = "avg_npc_1490_1#1$1", duration = 0)]
[name="宝石掮客"]卖倒是容易，买就不一样了。宝石交易所并不是一般的商铺，你需要拿出够分量的砝码，才能从监管人手上直接拿到东西。
[charslot(slot = "left", name = "avg_4138_narant_1#12$1",focus="l")]
[interlude(channel = 3, switch = false, type = 3, slot = "m", pfrom = "270,0", pto="270,0", name = "avg_npc_1490_1#1$1", duration = 0)]
[name="娜仁图亚"]够分量的砝码？
[Dialog]
[charslot(slot = "left", name = "avg_4138_narant_1#4$1",focus="l")]
[delay(time=1.5)]
[charslot(slot 

... (全文12763字符)
```

### level_act35side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="53_g8_sargondeluxeroom",screenadapt="coverall")]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[PlaySound(key="$d_avg_summercicada", volume=1, loop=true, channel="s")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
室内，空气因为酷暑而变得沉闷，女孩坐在桌前，一边翻着厚厚的资料，一边擦拭从额角流下的汗水。
背后响起了脚步声，她知道有人进来了，但却懒得回头看。
桌子上有扁桃仁，他会自己拿的。
[dialog]
[SoundVolume(volume=0.1, channel="s",fadetime=2)]
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1", posfrom="0,-20", posto="0,-20", duration=1.5, isblock=true)]
[Delay(time=0.5)]
[charslot(slot = "m", focus="n")]
[name="？？？"]姐姐，你在看什么书啊？
[dialog]
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1")]
[playsound(key="$d_avg_paper1",volume=1)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1")]
[name="佩佩"]......
[charslot(slot = "m", focus="n")]
[name="？？？"]姐姐，下午太阳这么好，出去玩啊！
[dialog]
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1")]
[playsound(key="$d_avg_paper2",volume=1)]
[delay(time=1)]
[name="佩佩"]......
[charslot(slot = "m", focus="n")]
[name="？？？"]姐姐，你不会打算钻在这堆落灰的莎草纸卷里一辈子吧？
[dialog]
[charslot(slot = "m", name = "avg_4058_pepe_1#8$1")]
[playsound(key="$d_avg_paper1",volume=1)]
[delay(time=0.5)]
[playsound(key="$d_avg_paper2",volume=1)]
[delay(time=1)]
[name="佩佩"]......
[charslot(slot = "m", focus="n")]
[name="？？？"]姐姐，我去请求父亲了，他说他会考虑让我成为黄金之城的史官。
[dialog]
[playsound(key="$d_avg_paper1",volume=1)]
[delay(time=0.5)]
[playsound(key="$d_avg_paper2",volume=1)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#8$1")]
[name="佩佩"]......
[charslot(slot = "m", focus="n")]
[name="？？？"]姐姐，做个帕夏也很好，放弃吧。
[dialog]
[charslot(slot = "m", name = "avg_4058_pepe_1#9$2", posfrom="0,-20", posto="0,0", afrom=1, ato=1, duration=0.3, isblock=true)]
[name="佩佩"]够了！你小子别吵我了！
[dialog]
[musicvolume(volume=0, fadetime=1)]
[StopSound(channel="s", fadetime=1)]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(duration=0.2, isblock=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_bookdrop", volume=1)]
[delay(time=1)]
女孩猛地回过头，却发现背后空无一人。
只有她掷出的书卷，孤零零地躺在地板上。
[dialog]
[charslot(slot = "m", name = "avg_4058_pepe_1#8$2")]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_4058_pepe_1#5$1", duration=1, isblock=true)]
[delay(time=1.5)]
[charslot(slot = "m", focus="n")]
[PlaySound(key="$d_avg_knockdoorfast", volume=1)]
[delay(time=1)]
[name="梅捷缇克缇"]佩佩，你在吗？快开门！
[charslot(slot = "m", name = "avg_4058_pepe_1#12$1")]
[name="佩佩"]我在，请进。
[dialog]
[charslot]
[PlaySound(key="$dooropenquite", volume=1)]
[delay(time=1.5)]
[musicvolume(volume=0.6, fadetime=2)]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot = "l", name = "avg_4058_pepe_1#12$1")]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1478_1#1$1", posfrom="200,0", posto="0,0", duration=0.5, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1478_1#7$1", focus="r")]
[name="梅捷缇克缇"]我给你的通讯器发了那么多消息，你为什么不回？
[charslot(slot = "l", name = "avg_4058_pepe_1#12$1", focus="l")]
[name="佩佩"]我把通讯器关掉，在这里看了一晚上的书，发生什么了？
[charslot(slot = "r", name = "avg_npc_1478_1#6$1", focus="r")]
[name="梅捷缇克缇"]哈，昨夜发生那么多事情，难不成你在这里一无所知吗？
[charslot(slot = "l", name = "avg_4058_pepe_1#12$1", focus="l")]
[name="佩佩"]我不知道啊。
[charslot(slot = "r", name = "avg_npc_1478_1#6$1", focus="r")]
[multiline(name="梅捷缇克缇")]你这个闷起头来做事的性子真的是......
[charslot(slot = "r", name = "avg_npc_1478_1#2$1", focus="r")]
[multiline(name="梅捷缇克缇",end=true)]算了，我也不知道该说什么了。
[dialog]
[PlaySound(key="$d_avg_button", volume=1)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1478_1#1$1", focus="r")]
[name="梅捷缇克缇"]直接听吧。
[dialog]
[charslot]
[PlaySound(key="$d_avg_oldtvelectricity", volume=0, loop=true, channel="o")]
[SoundVolume(volume=1, channel="o", fadetime=2)]
[name="电台广播"]米城内多个区域发生紧急事件。
[name="电台广播"]有大量金属构装的人偶走上街头，从居民家中抢夺大量宝石后离开。
[name="电台广播"]据悉，已有众多市民向城市护卫队报告，护卫队队长表示正在追查中。
[charslot(slot = "m", name = "avg_4058_pepe_1#8$1")]
[name="佩佩"]金属人偶......？
[charslot]
[name="电台广播"]据目击者透露，他曾于昨夜目睹这些金属构装人偶从本市博物馆中逃出......
[dialog]
[StopSound(channel="o", fadetime=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r", name = "avg_npc_1478_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_4058_pepe_1#9$1", focus="l")]
[name="佩佩"]什么？！
[charslot(slot = "r", name = "avg_npc_1478_1#1$1", focus="r")]
[name="梅捷缇克缇"]那个......我想说的，她都说了。
[name="梅捷缇克缇"]阿娜特说，博物馆的工作人员跟随着构装体的踪迹，最后找到了大巴扎。
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]是祖拜尔做的吗？
[charslot(slot = "r", name = "avg_npc_1478_1#1$1", focus="r")]
[name="梅捷缇克缇"]我们怀疑是这样，但是没人看到他，你和他相处时间最久，你能去找找看吗？
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]知道了，我这就过去。
[name="佩佩"]那你和阿娜特呢？
[charslot(slot = "r", name = "avg_npc_1478_1#1$1", focus="r")]
[name="梅捷缇克缇"]作为博物馆的管理人员，我们总得将文物尽数找回来。
[name="梅捷缇克缇"]我们打算去街上看看。
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]一有消息我就通知你们，回见。
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot = "l", posfrom="0,0", posto="-200,0", afrom=1, ato=0, duration=0.5, isblock=true)]
[delay(time=1.5)]
[charslot(slot = "r", name = "avg_npc_1478_1#2$1")]
[name="梅捷缇克缇"]呼......
[dialog]
[charslot]
[PlaySound(key="$d_avg_oldtvelectricity", volume=0, loop=true, channel="o")]
[SoundVolume(volume=1, channel="o", fadetime=2)]
[name="电台广播"]呃，慢着，本台插播一条急讯。
[name="电台广播"]有市民发现家中取水器内流出的水变得浑浊，其中掺杂大量泥沙。
[name="电台广播"]护卫队方面称，他们正在紧急组织人力排查城市老地下水通道，由于通道情况复杂，可能仍然需要时间......
[charslot(slot = "m", name = "avg_npc_1478_1#5$1")]
[name="梅捷缇克缇"]啊，这又是什么情况？
[dialog]
[stopmusic(fadetime=2)]
[StopSound(channel="o", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=t

... (全文13906字符)
```

### level_act35side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="53_g10_grandbazaar_d",screenadapt="coverall")]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(slot = "r", name = "avg_npc_1492_1#1$1", posfrom="150,0", posto="-250,0", duration=0.8)]
[Delay(time=0.2)]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=0.8)]
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", posfrom="-200,0", posto="0,0", duration=0.5)]
[Delay(time=0.5)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[charslot(slot = "r", posfrom="-250,0", posto="-200,-20", afrom=1, ato=0, duration=0.3, isblock=true)]
[charslot(slot = "l", focus="n")]
[name="惊慌的路人"]哎呦！你这孩子走路怎么这么不小心。
[dialog]
[charslot(slot = "l", name = "avg_4058_pepe_1#12$1")]
[name="佩佩"]对、对不起，先生！我着急赶路没有看到您！您没事吧？！
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "r", name = "avg_npc_1492_1#1$1", posfrom="0,-30", posto="0,0", duration=1)]
[Delay(time=1.5)]
[charslot(slot = "r", focus="r")]
[name="惊慌的路人"]没事没事，我这把老骨头还算结实。
[name="惊慌的路人"]倒是你，匆匆忙忙往哪里跑？不知道出事了吗？
[name="惊慌的路人"]那些金属人偶，先是不断把全城的宝石都送进大巴扎，现在又开始四处拆除房屋，将我们从大巴扎中驱赶出来。
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]那些构装体现在在拆除房屋？
[charslot(slot = "r", focus="r")]
[multiline(name="惊慌的路人")]是啊！到处是崩落的石头，
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot = "l", posfrom="0,0", posto="200,0", afrom=1, ato=0, duration=0.5, isblock=true)]
[multiline(name="惊慌的路人",end=true)]哎，你怎么还在往那边跑啊？
[charslot(slot = "l", focus="n")]
[name="佩佩"]我去看看到底是什么情况！
[charslot(slot = "r", focus="r")]
[name="惊慌的路人"]你一个孩子能去干什么啊？
[name="惊慌的路人"]唉，你这孩子！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="53_g10_grandbazaar_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1", duration=1, isblock=true)]
[name="佩佩"]......没有一个人，大家都离开了。
[charslot(slot = "m", name = "avg_4058_pepe_1#12$1")]
[name="佩佩"]天......
[dialog]
[charslot]
[PlaySound(key="$d_avg_fsmetal", volume=1)]
[Delay(time=1)]
[PlaySound(key="$d_avg_fsmetal", volume=1)]
[Delay(time=1)]
平日里熙熙攘攘的街道上，早已空无一人，只有宝石构装体三三两两聚在一起。
它们抬手间，一座座房屋尽数化为流沙，落在地上。
而流沙之中，又升起层层叠叠的巨柱与高墙。
[dialog]
[CameraShake(duration=3, xstrength=5, ystrength=5, vibrato=20, randomness=70, fadeout=true, block=false)]
[PlaySound(key="$d_avg_sandstone", volume=1)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#9$1", posfrom="100,0", posto="0,0", duration=0.5, isblock=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#3$1")]
[name="佩佩"]呼......差点就被砸到了。
[PlaySound(key="$d_avg_meownormal", volume=1)]
[charslot(slot = "m", focus="n")]
[name="米奥"]咪......
[charslot(slot = "m", name = "avg_4058_pepe_1#5$1")]
[name="佩佩"]......？
[dialog]
[PlaySound(key="$d_avg_pawfootstep_3", volume=0.4)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#5$1")]
[name="佩佩"]谁......
[dialog]
[charslot]
[PlaySound(key="$d_avg_pawfootstep_3", volume=1)]
[charslot(slot = "m", name = "avg_npc_1482_1#6$1", posfrom="-200,0", posto="0,0", duration=1.5, isblock=true)]
[PlaySound(key="$d_avg_meowlong", volume=1)]
[charslot(slot = "m", name = "avg_npc_1482_1#1$1", duration=0.5, isblock=true)]
[name="米奥"]喵呜......
[charslot(slot = "m", name = "avg_4058_pepe_1#4$1")]
[name="佩佩"]咦......哪里来的小动物......？
[PlaySound(key="$d_avg_meownormal", volume=1)]
[charslot(slot = "m", name = "avg_npc_1482_1#1$1")]
[name="米奥"]喵！
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1")]
[name="佩佩"]快走吧，这里不是你该待的地方。
[name="佩佩"]去！去！
[charslot(slot = "m", name = "avg_npc_1482_1#1$1")]
[name="米奥"]......
[dialog]
[charslot(duration=0.5, isblock=true)]
[Delay(time=0.5)]
面前的动物并没有因为女孩的呵斥而恐惧，反而施施然地蹲坐下来，轻轻舔舐自己的皮毛。
佩佩内心疑惑，决定绕开继续前行，就在她准备踏出脚步的时候，那只动物抬起头，直勾勾看向佩佩的眼睛。
在它的盯视中，佩佩觉得寸步难行。
[dialog]
[stopmusic(fadetime=2)]
[Delay(time=1)]
但那只是一只很小很小的动物。
她鼓起勇气，往前踏了一步。
[dialog]
[PlayMusic(intro="$jealous_intro", key="$jealous_loop", volume=0.6)]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_monsterroar", volume=1)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_tinnitus", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.2, block=true)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_gen_heartbeat", volume=1, loop=true, channel="h")]
那是一声震耳欲聋的暴喝，女孩感觉自己的鼓膜隐隐作痛。
无论如何她也想象不到，这样的声音竟然发自一只不及人小腿高的动物。
她捂住耳朵闭上眼，将脸皱成一团，声浪几乎将她拍倒在地。
等到余喝散尽，她感觉自己被一个巨大的阴影笼罩。
[dialog]
[StopSound(channel="h", fadetime=2)]
[charslot]
[Image(image="53_i07", screenadapt="coverall", xScale=1.1, yScale=1.1)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
睁开眼，女孩看到一只凶兽盘踞在街道中央，身覆浓密的沙金色皮毛，隐隐可以看到有花纹在上面游走，溢散出曼妙的流光。
像是被吸引般，女孩看向凶兽的眼睛，对视的一瞬间，她感觉自己的灵魂都被吸进那双金色的瞳孔。
呼吸、心跳、脉搏......都好像被它捏紧，随时可以被终止。
她彻底动弹不得，只能看着那只凶兽向自己缓缓走来，张开猩红的巨口......
将自己整个吞下。
[dialog]
[CameraShake(duration=0.3, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_monsterroar", volume=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.3, block=true)]
霎时间，天地昏暗。
[dialog]
[Background(image="53_g4_ctizengarden",screenadapt="coverall")]
[Delay(time=1)]
[image]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$phone", volume=1, loop=true, channel="t"

... (全文21938字符)
```

### level_act35side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="s")]
[gridbg(imagegroup="44_g13_afterglow_L1/44_g13_afterglow_R1/44_g13_afterglow_L2/44_g13_afterglow_R2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720",x=-200,fadetime=1)]
[largebgtween(duration = 60, yFrom = 0, yTo = 720,block = false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="你们应该祝福我。在刚升上来的太阳下面跳起舞，敲起刀鞘祝福我。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="——哦，我忘记你们大都把刀卖了，那就敲敲锅碗瓢盆、铁砧、钢笔和墨水瓶吧。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="米纳特哈玛仪是个用宝石铺路的地方，我现在就要去走那条路啦。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我知道，你们会劝我别做白日梦。但我为什么不可能赚到那么一大笔钱？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我为什么买不到大家最好的日子？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我偏要试试。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[StopSound(channel="s", fadetime=3)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=3, block=true)]
[gridbg]
[Background(image="bg_desert03_d", screenadapt="coverall")]
[bgeffect(name="$eb_cnclouds",layer=1)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot(slot = "m", name = "avg_4138_narant_1#2$1", duration=1.5, isblock=true)]
[name="娜仁图亚"]我这是在——
[dialog]
[charslot]
[PlaySound(key="$d_avg_cheer_street", volume=0.5)]
[delay(time=1)]
[PlayMusic(intro="$marketplace_intro",key="$marketplace_loop", volume=0.6)]
[PlaySound(key="$d_avg_fssand", volume=1)]
[charslot(slot = "m", name = "avg_npc_163", posfrom="-30,0", posto="-30,0", duration=1, isblock=true)]
[delay(time=0.5)]
[PlaySound(key="$runsand", volume=1)]
[charslot(slot = "r", name = "avg_npc_1485_1#1$2", posfrom="200,0", posto="0,0", duration=1)]
[delay(time=0.4)]
[charslot(slot = "l", name = "avg_npc_1484_1#1$2", posfrom="-200,0", posto="0,0", duration=1, isblock=true)]
[delay(time=1.5)]
[charslot]
[charslot(slot = "m", name = "avg_4138_narant_1#1$1")]
[name="娜仁图亚"]——哦，是我的启程仪式！我一定是舞跳得太开心，把自己转昏了。
[charslot(slot = "m", name = "avg_npc_163")]
[name="开朗的前沙盗"]娜仁图亚，我祝福你。
[name="开朗的前沙盗"]我认识的一支商队会定期前往那座辉煌之城，你如果真的走到了那里，就去找他们。
[charslot(slot = "m", name = "avg_4138_narant_1#1$1")]
[name="娜仁图亚"]哈，我就知道你那里总有可用的人脉！
[charslot(slot = "m", name = "avg_4138_narant_1#5$1")]
[name="娜仁图亚"]多一个朋友，少一桩麻烦，谢啦。
[dialog]
[charslot]
[PlaySound(key="$d_avg_fssand", volume=1)]
[charslot(slot = "m", name = "avg_npc_165", duration=1.5, isblock=true)]
[name="犹疑的前沙盗"]娜仁图亚，我还是很担心。
[charslot(slot = "m", name = "avg_4138_narant_1#1$1")]
[name="娜仁图亚"]担心什么？我说了多少次了，我不在，大家也不会来报复你。
[charslot(slot = "m", name = "avg_4138_narant_1#7$1")]
[name="娜仁图亚"]这一切都跟你无关。你转投我手下，是我有魅力。
[name="娜仁图亚"]阿西姆那老家伙为此怨恨我，到处说我的坏话，是他小气。
[charslot(slot = "m", name = "avg_4138_narant_1#5$1")]
[name="娜仁图亚"]最后嫉妒我的人凑到一起，给我设圈套使绊子......就怪我运气好，太招金子喜爱也太招人喜爱吧。
[charslot(slot = "m", name = "avg_npc_165")]
[name="犹疑的前沙盗"]可是，娜仁图亚，我担心的是你。
[name="犹疑的前沙盗"]你要这样行囊空空地走进沙漠，如果找不到水源也遇不到野兽，该怎么办？
[charslot(slot = "m", name = "avg_4138_narant_1#2$1")]
[name="娜仁图亚"]啊？我们每个人的钱袋是都比以前空了不少，但也不至于落魄到连肉干和果脯都准备不了。
[charslot(slot = "m", name = "avg_4138_narant_1#4$1")]
[multiline(name="娜仁图亚")]你怎么会这么想的？难道说你们有人偷偷吃了苦不告诉我？谁？
[charslot(slot = "m", name = "avg_4138_narant_1#2$1")]
[multiline(name="娜仁图亚",end=true)]我现在就拿点金币出来——
[dialog]
[charslot]
娜仁图亚的手在腰上的钱袋里摸了摸。
然后，她缓缓瞪大了眼睛，解下兽皮袋，翻过来抖了抖。
几粒沙子落进了无边的大漠之中。
[charslot(slot = "m", name = "avg_4138_narant_1#4$1")]
[name="娜仁图亚"]奇怪，我不记得自己遇到过乞丐或者流浪汉......
[name="娜仁图亚"]倒是隐隐约约记得，遇到了不少有钱人？
[charslot(slot = "m", name = "avg_npc_165")]
[name="犹疑的前沙盗"]娜仁图亚，我想了想，应该把我寻找水源的秘诀教给你。
[name="犹疑的前沙盗"]事到如今，我没必要再担心自己会被一个暴徒首领选中当牺牲品了，也就不用捏着一个关系所有人生死的独门诀窍。
[charslot(slot = "m", name = "avg_4138_narant_1#1$1")]
[name="娜仁图亚"]——好，我喜欢这个祝福。
[name="娜仁图亚"]就让那几枚金币随流沙而去吧。
[charslot(slot = "m", name = "avg_npc_1484_1#5$2")]
[name="阿雅吉"]娜仁图亚，我也很担心。
[charslot(slot = "m", name = "avg_4138_narant_1#12$1")]
[name="娜仁图亚"]奇怪，你又担心什么？我再从车上劫一个奴隶小孩回来，抢走你的识字数量倒数第一？
[charslot(slot = "m", name = "avg_npc_1484_1#5$2")]
[name="阿雅吉"]我担心你的那两把黑刀，很久没用过了，也没有护理过。
[charslot(slot = "m", name = "avg_4138_narant_1#2$1")]
[name="娜仁图亚"]就是因为护理麻烦，我才一直不用那两把老古董。我宁可崇拜现代材料和机器锻造——
[dialog]
[PlaySound(key="$d_avg_sandwnd", volume=0, loop=true, channel="s")]
[SoundVolume(volume=0.4, channel="s", fadetime=2)]
[stopmusic(fadetime=3)]
[delay(time=1.5)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_4138_narant_1#10$1")]
[name="娜仁图亚"]——我的刀呢？我的匕首呢？我储备的麻痹毒剂和孢子瓶呢？
[charslot(slot = "m", name = "avg_npc_1485_1#3$2")]
[name="阿雅妮"]唉，娜仁图亚，我担心的确实是你总想招揽新的手下。
[name="阿雅妮"]你独自出发，如果遇到的是能立刻给你帮忙的手下，那的确很好，但大多数时候，其实是像我和阿雅吉那样被你救......
[charslot(slot = "m", name = "avg_4138_narant_1#10$1")]
[name="娜仁图亚"]“独自出发”？你们不跟我一起去那座“辉煌之城”了？
[charslot(slot = "m", name = "avg_npc_1485_1#3$2")]
[name="阿雅妮"]所以我和阿雅吉去雨林的伐木场干了两个月的活，把攒起来的金币全部丢进了一条据说会流到辉煌之城的河里。
[name="阿雅妮"]但愿你能在河水漫上来的时候捡到它们，但愿你的天途能更加顺利......
[charslot(slot = "m", name = "avg_4138_narant_1#1$1")]
[name="娜仁图亚"]好，我也喜欢这份祝福，虽然雨林在河的下游。
[dialog]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4138_narant_1#12$1")]
[name="娜仁图亚"]......等等。
[name="娜仁图亚"]天途？
[charslot(slot = "m", name = "avg_npc_1484_1#2$2")]
[name="阿雅吉"]是的，天途。
[charslot(slot = "m", name = "avg_npc_1485_1#2$2")]
[name="阿雅妮"]娜仁图亚，你已经准备好了，不是吗？
[charslot(slot = "m", name = "avg_4138_narant_1#10$1")]
[name="娜仁图亚"]没有啊，什么时候的事？
[charslot(slot = "m", name = "avg_4138_narant_1#4$1")]
[nam

... (全文22922字符)
```

### level_act35side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_falls_1",screenadapt="coverall")]
[playMusic(key="$calm_loop", volume=0.6)]
[bgeffect(name="$eb_cnclouds",layer=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#12$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="佩佩"]这又是什么地方啊？！
[name="佩佩"]瀑布？！
[charslot]
瀑布边，佩佩看见方才那个男孩正垂着头，清洗着什么。
她快步上前，想要唤起男孩的注意，却发现他长高了些，脸庞已经褪去了孩童的稚嫩。
现在的他，已经是个少年了。
[charslot(slot = "m", name = "avg_4058_pepe_1#8$1")]
[name="佩佩"]好了，够了，不管你是谁！让我离开......你......
[charslot(slot = "m", name = "avg_4058_pepe_1#5$1")]
[name="佩佩"]你受伤了吗？你的脸上......
[charslot(slot = "m", name = "avg_npc_1481_1#1$1")]
[name="受伤的少年"]姐姐，不用担心，这些血大多是敌人的。
[name="受伤的少年"]战场上的情况比我想象中的要复杂，但他们都不是我的对手，我赢了。
[charslot(slot = "m", focus="n")]
[name="温柔的少女"]祖拜尔，在阿尔萨兰的雨林中，我为你在神庙中祈求了一副护身符。
[name="温柔的少女"]我希望它能保护你不受伤害。
[charslot(slot = "m", name = "avg_npc_1481_1#1$1")]
[name="受伤的少年"]我不怕，姐姐，那些伤痕都是我成长的证明。
[charslot]
低下头，佩佩看见半跪着的少年的膝旁，横放着一柄长剑。
[dialog]
[PlaySound(key="$d_avg_dripink", volume=1)]
[delay(time=1)]
几道鲜红的血液顺着剑身流入潭水中，将水面染成粉红一片。
佩佩转头，看见背后的少女嘴角噙着温柔的笑意，但眼中却显露出担忧。
她将头扭回，却发现四周再次变换了场景。
[dialog]
[Blocker(a=1, r=255, g=255, b=255, style = "slider", inverse = true, fadetime=2, block=true)]
[Background(image="bg_jungleentrance",screenadapt="coverall")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=4, block=true)]
雨林中，少年举起一把匕首，翻转着，打量个不停。
[dialog]
[charslot(slot = "m", name = "avg_npc_1481_1#1$1", duration=1)]
[delay(time=1.5)]
[charslot(slot = "m", focus="n")]
[name="温柔的少女"]恭喜你，从明天开始，就要统领父亲的卫戍部队了。
[name="温柔的少女"]这是你梦寐以求的职位，为什么你看着一点也不开心？
[charslot(slot = "m", name = "avg_npc_1481_1#1$1")]
[name="安静的少年"]我也不知道，与我付出的努力与艰辛相比，这把指挥官匕首实在是有些太轻了。
[name="安静的少年"]你呢，姐姐？你不为我高兴吗？
[charslot(slot = "m", focus="n")]
[name="温柔的少女"]不，祖拜尔，只有你开心，我才会高兴。
[charslot(slot = "m", name = "avg_npc_1481_1#1$1")]
[name="安静的少年"]那些书卷，你已经在上面花费了无数个日夜。有找到什么吗？
[charslot(slot = "m", focus="n")]
[name="温柔的少女"]祖拜尔，萨尔贡的历史远比我们想象的更为悠久，但现存的抄本与记录都没有完整地将它们记述下来。
[name="温柔的少女"]我打算编撰一部史籍，记录下那些被遗漏的前代事迹，最好......
[charslot(slot = "m", name = "avg_npc_1481_1#1$1")]
[name="安静的少年"]最好......？
[charslot(slot = "m", focus="n")]
[name="温柔的少女"]最好它能将萨尔贡的历史完整地记述。
[charslot(slot = "m", name = "avg_npc_1481_1#1$1")]
[name="安静的少年"]篇幅一定很长......你要写的人一定很多。
[charslot(slot = "m", focus="n")]
[name="温柔的少女"]父亲认可了我的想法，他承诺会为我提供帮助。
[charslot(slot = "m", name = "avg_npc_1481_1#1$1")]
[name="安静的少年"]很好，我们都得到了自己想要的。
[charslot]
佩佩看到少年将匕首收回，对着姐姐露出笑容。
[dialog]
[Blocker(a=1, r=255, g=255, b=255, style = "slider", inverse = true, fadetime=2, block=true)]
[Background(image="bg_jungle_1",screenadapt="coverall")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=4, block=true)]
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1")]
[name="佩佩"]......
[name="佩佩"]另外一个地方？
[name="佩佩"]这又是什么时候......？
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1480_1#1$1", duration=1)]
[delay(time=1.5)]
[charslot(slot = "m", focus="n")]
[name="温柔的女人"]你为何愁眉不展......祖拜尔......
[charslot(slot = "m", name = "avg_npc_1480_1#1$1")]
[name="安静的青年"]那位来自东方的库兰塔，他让父亲变得不一样了。
[name="安静的青年"]这么多年，各个部族的叛乱与挑战都不能让父亲面容改色，一次又一次，他重整队伍，扬起旗帜。
[name="安静的青年"]当父亲用长剑劈砍面前的敌人，那些自他们脖颈处溅射而出的血液，不能让他面具后的冰冷目光融化分毫。
[name="安静的青年"]那位梦魇......当父亲与他战斗的时候，兵器相接，所击出的火花点燃了父亲瞳孔中的火焰。
[name="安静的青年"]我从未见过他如此狂热地注视一个人。
[charslot(slot = "m", focus="n")]
[name="温柔的女人"]祖拜尔，我能够察觉到......我们的父亲，他付诸国家的热情早已减退了。
[name="温柔的女人"]我听到了一些令人忐忑的消息，父亲他打算邀请哈兰杜汗一同挥师南下，去挑战那里的无形之敌。
[name="温柔的女人"]你也要去，对吗，祖拜尔？
[charslot(slot = "m", name = "avg_npc_1480_1#1$1")]
[name="安静的青年"]......那些怪诞的敌人已经在步步侵蚀我们的土地了。
[charslot(slot = "m", name = "avg_4058_pepe_1#5$1")]
[name="佩佩"]沙阿......你们都是沙阿的孩子......
[dialog]
[charslot]
[stopmusic(fadetime=2)]
[charslot(slot = "m", focus="n")]
跟着青年的视线向远处眺望，忽然间，千里之外的土地被一股引力拉至眼前。
[dialog]
[PlaySound(key="$d_avg_snowstormflp", volume=0, loop=true, channel="s")]
[SoundVolume(volume=1, channel="s",fadetime=2)]
[PlaySound(key="$d_avg_timetravel", volume=1)]
[BackgroundTween(xScaleFrom=1, yScaleFrom=1, xScaleTo=1.7, yScaleTo=1.7, duration=1, ease="OutQuad",block=false)]
[focusout(duration=0.2, type="bg", from=0, to=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=1, block=true)]
[bgeffect]
[Background]
[Background(image="bg_desert03_d", screenadapt="coverall", xScale=1, yScale=1)]
[focusout(duration=5, type="bg", from=1, to=0)]
[BackgroundTween(xScaleFrom=1.7, yScaleFrom=1.7, xScaleTo=1, yScaleTo=1, duration=3, ease="OutQuad",block=false)]
[bgeffect(name="$eb_sand02", flip = 1, layer=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=3, block=true)]
[Delay(time=1)]
佩佩看到了一片寸草不生的荒漠，风中夹着沙粒，打在她的眼皮上。
[dialog]
[charslot(slot = "m", name = "avg_4058_pepe_1#5$1", duration=1, isblock=true)]
[name="佩佩"]......焚风热土......
[name="佩佩"]发生什么了？
[charslot(slot = "m", focus="n")]
[name="温柔的女人"]祖拜尔，你感觉怎么样了？
[dialog]
[charslot]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_1480_1#1$1", duration=1)]
[delay(time=1.5)]
[name="安静的青年"]我很好，姐姐。 
[charslot(slot = "m", focus="n")]
[name="温柔的女人"]我现在为你换药，需要揭开你身上的绷带，忍耐下，很快就结束了。
[charslot(slot = "m", name = "avg_npc_1480_1#1$1")]
[name="安静的青年"]我不痛，没事的。
[charslot(slot = "m", focus="n")]
[name="温柔的女人"]怎么会不痛呢，你被抬回来的时候，浑身焦黑，没有一块皮肤是完好的。
[name="温柔的女人"]我该怎么办，祖拜尔......父亲不知所踪，你是我最后的亲人了。
[name="温柔的女人"]王兄已经即位，我们与他并非一母同出，你在军中立下的功绩已经让他有所忌惮。
[charslot(slot = "m", name = "avg_npc_1480_1#1$1")]
[name="安静的青年"]那位史官先生......他对你好吗？
[charslot(slot = "m", focus="n")]
[name="温柔的女人"]嗯......有他帮忙，那本史籍的编撰已近一半，或许在我有生之年，能有机会见到它的完本。
[charslot(slot = "m", name = "avg_npc_1480_1#1$1")]
[name="安静的青年"]你不该太过操劳。
[charslot(slot = "m", focus="n")]
[name="温柔的女人"]这是我对父亲的承诺......就算我完不成，我腹中的孩子也会继续......终有一日，它会告诉后来人，此时此刻所发生的一切。
[name="温柔的女人"]它会隔着遥远的时光，架起一座桥梁，让读者与所记录的人物在漫漫历史长河中彼此相认。
[charslot(slot = "m", name = "avg_npc_1480_1#1$1")]
[name="安静的青年"]我听说，他们要为父亲修建一座衣冠冢。
[charslot(slot = "m", focus="n")]
[name="温柔的女人"]嗯......
[charslot(slot = "m", name 

... (全文22560字符)
```

### level_act35side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="53_g13_invertedpyramid",screenadapt="coverall")]
[PlayMusic(intro="$ghosthunter_intro", key="$ghosthunter_loop", volume=0.6)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#4$3", duration=1.5, isblock=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1479_1#5$1")]
[name="祖拜尔"]欢迎来到这里，佩佩。
[charslot(slot = "m", name = "avg_4058_pepe_1#4$3")]
[name="佩佩"]这便是沙阿所留下的宝库吗？和博物馆好像......
[charslot(slot = "m", name = "avg_npc_1479_1#1$1")]
[name="祖拜尔"]你的感知是正确的，在我记忆还未恢复的时候，就觉得城中有些地方似曾相识。
[name="祖拜尔"]在建立城市的过程中，我想他们兴许是参考了陵寝的修建风格。
[charslot(slot = "m", name = "avg_4058_pepe_1#2$3")]
[name="佩佩"]这里到底有什么，祖拜尔？
[dialog]
[musicvolume(volume=0.2, fadetime=2)]
[PlaySound(key="$d_avg_cndlextngsh", volume=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background]
[Image(image="pic_sandbox_1_5", screenadapt="coverall")]
[ImageTween(yFrom=0, yTo=-30, xScaleFrom=1, yScaleFrom=1, xScaleTo=1.1, yScaleTo=1.1, duration=30, block=false)]
[musicvolume(volume=0.6, fadetime=2)]
[Delay(time=1)]
[PlaySound(key="$d_avg_cndlbrn", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=false)]
[Delay(time=1)]
[PlaySound(key="$d_avg_churchfire", volume=0, loop=true, channel="c")]
[SoundVolume(volume=0.2, channel="c",fadetime=2)]
[Delay(time=3)]
墙壁上的油灯燃起，光线在如镜面般光滑的墙体与支柱间游走，昏暗的大厅变得明亮。
一时之间，无数犹如鬼魂一般的虚影，齐齐出现在大厅之中，或行或立。
[name="佩佩"]原来在沙阿的宝库中藏着的宝物......都是他自己啊。
[name="佩佩"]原来他这么自恋的吗......？
[name="祖拜尔"]当然不是，这些影像都是姐姐让我保存在这里的，自父亲离去后，姐姐一直很想念他。
[name="祖拜尔"]千年前，史官们通过发掘到的古代科技，保存了父亲的一言一行，无不栩栩如生。
[name="佩佩"]我在阿尔萨兰地区也找到了类似的物品，在晶洞中，它为我展示了一段沙阿的影像。
[name="祖拜尔"]那正是我留下的，我以为会有梦魇后裔找到那段影像，然后顺着线索找过来。
[name="佩佩"]你把它藏得太隐秘了，祖拜尔，别人肯定找不到。
[name="祖拜尔"]隐秘？我可是在外面主持修建了一座巨大的神庙。
[name="佩佩"]看来它没能抵御岁月的侵蚀，在我到达的时候，那里已经是一片颓唐破败的废墟了。
[name="祖拜尔"]但它还是指引你来到了这里，并且将我唤醒。
[name="祖拜尔"]这正是岁月变迁的奇妙之处，一些当时看来派不上用场的安排，也会因为一系列阴差阳错，作用出美妙的巧合。
[name="佩佩"]原来这里还有沙阿摘下面具的样子......
[name="佩佩"]这样的影像我不仅仅在阿尔萨兰见过，小时候，我和弟弟捉迷藏，误入了一间存放棺椁与亡者的密室。
[name="佩佩"]虽然有家学教导，知道自己迟早要接触到这些，但让一个孩子独自面对这些还是过于勉强了。
[name="佩佩"]当时我慌张失措，不知是误触了什么机关，见到了一段沙阿的影像，但我对他毫无认知，只当他是一个试图与自己沟通的鬼魂。
[name="佩佩"]他告诉我，这些棺椁只是一段被掩埋在沙土中的历史。
[name="佩佩"]当后来人将它发掘后，会架起一座跨越时间的桥梁，让我们跨过漫漫历史长河，彼此相识。
[name="祖拜尔"]我记得这句话......当时母亲去世，姐姐靠在棺椁上流泪不止，这是父亲蹲下来安慰她的话。
[name="祖拜尔"]我还记得，姐姐成为史官后，父亲常叮嘱她的话，要关注......
[name="佩佩"]要关注那些让英雄成为英雄的——历史的背面。
[name="祖拜尔"]......原来你已经听过了。
[name="佩佩"]这是那段影像最后留下的话，我一直记着。
[dialog]
[PlaySound(key="$d_avg_openftstpwalk", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[Image(image="53_i10", screenadapt="coverall", y=-30, xScale=1.1, yScale=1.1)]
[ImageTween(yFrom=-30, yTo=0, xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
看着路加萨尔古斯的影像，佩佩突然觉得有些荒诞。
一路的追寻中，她曾无数次地想象过沙阿的宝库中究竟保存着什么。
但此刻她突然意识到，自己所谓的执着与追寻，不过是从一个虚影到另一个虚影。
她抓紧手中的重锤，竭力忍住想要挥动它驱散眼前影子的冲动。
更让她觉得恐惧的是，自己家族所谓的职责与传承，又何尝不是一道虚影呢？
[dialog]
[StopSound(channel="c", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[charslot]
[Background(image="53_g5_museum",screenadapt="coverall")]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1478_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot = "l", name = "avg_npc_1485_1#2$2", duration=1, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_1485_1#2$2", focus="l")]
[name="阿雅妮"]梅捷缇克缇女士，我按照黄页把其他员工都联系了一遍。
[charslot(slot = "r", name = "avg_npc_1478_1#1$1", focus="r")]
[name="梅捷缇克缇"]还有不怕死愿意过来帮忙的人吗？
[charslot(slot = "l", name = "avg_npc_1485_1#8$2", focus="l")]
[name="阿雅妮"]我不确定，大多数人回答得都很复杂......
[charslot(slot = "r", name = "avg_npc_1478_1#9$1", focus="r")]
[name="梅捷缇克缇"]......谢谢你，你能再给阿娜特女士找几瓶水来吗？
[charslot(slot = "l", name = "avg_npc_1485_1#9$2", focus="l")]
[name="阿雅妮"]好的，梅捷缇克缇女士。
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot = "l", posfrom="0,0", posto="-200,0", afrom=1, ato=0, duration=0.5, isblock=true)]
[delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_4139_papyrs_1#1$2", posfrom="0,0", posto="0,0", duration=1.5)]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1478_1#2$1", focus="r")]
[name="梅捷缇克缇"]......像吉雅阿和妮雅阿一样不知道怕的人，终究还是少数。
[charslot(slot = "r", name = "avg_npc_1478_1#8$1", focus="r")]
[name="梅捷缇克缇"]阿娜特，我们现在也许只有两个小时。
[name="梅捷缇克缇"]其实现在立刻向城外逃跑，才是最好的办法。
[charslot(slot = "l", name = "avg_4139_papyrs_1#7$2", focus="l")]
[name="阿娜特"]抱歉，缇缇，我在比对城市测绘记录，无法分心想那么多......
[name="阿娜特"]但你应该知道，我和你留在这里的原因一样。
[charslot(slot = "r", name = "avg_npc_1478_1#8$1", focus="r")]
[name="梅捷缇克缇"]......职责。
[name="梅捷缇克缇"]可是那两个游客呢？她们和祖拜尔的复活没有任何关系。
[name="梅捷缇克缇"]她们甚至和这座城市也没有什么关系......现在我们却让她们进入地下水道，去做最危险的探查工作，想办法堵住灌进来的沙子。
[charslot(slot = "l", name = "avg_4139_papyrs_1#7$2", focus="l")]
[name="阿娜特"]所以我只能尽我最大的努力，让她们的勇气不会被浪费。
[dialog]
[charslot(slot = "r", posfrom="0,0", posto="-50,0", afrom=1, ato=1, duration=1)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1478_1#1$1", focus="r")]
[name="梅捷缇克缇"]......我帮你捏捏耳朵。
[Effect(name="$e_emoji_proud",layer = 1,x=-150,y=200)]
[charslot(slot = "l", name = "avg_4139_papyrs_1#11$2", focus="l")]
[name="阿娜特"]谢谢你，缇缇。
[dialog]
[charslot(slot = "r", posfrom="-50,0", posto="0,0", afrom=1, ato=1, duration=0.5)]
[Delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1478_1#5$1", focus="r")]
[name="梅捷缇克缇"]啊，你看，这一段施工日志提到了异常地质结构。
[charslot(slot = "l", name = "avg_4139_papyrs_1#7$2", focus="l")]
[name="阿娜特"]——好，我立刻记录下来。
[dialog]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_4139_papyrs_1#9$2", focus="l")]
[name="阿娜特"]缇缇，你说，我关于祖拜尔先生的研究最终也没发表，我们死

... (全文36470字符)
```

### level_act35side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[charslot]
[PlaySound(key="$d_avg_sand_lp", volume=0, loop=true, channel="sa")]
[SoundVolume(volume=1, channel="sa", fadetime=1)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[Background(image="53_g13_invertedpyramid", screenadapt="coverall")]
[focusout(type="bg", id="53_g13_invertedpyramid", from=0, to=0, duration=0.1, block=false)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
睁开眼，佩佩看到祖拜尔的叉铃就在自己眼前，只要再往前延伸一点，就能将自己的脖子彻底击断。
而自己的锤子则抵在祖拜尔的胸前，他胸腔的宝石上蔓延出了细长的裂纹。
[dialog]
[PlaySound(key="$d_avg_bellfall", volume=1)]
[Delay(time=1.5)]
[name="祖拜尔"]恭喜你，佩佩......
[name="祖拜尔"]你做到了......
[name="祖拜尔"]小时候玩捉迷藏就一直输给姐姐，想不到现在还会输给你。
[dialog]
[StopSound(channel="sa", fadetime=3)]
[PlaySound(key="$d_avg_fssand", volume=1)]
[charslot(slot = "m", name = "avg_4058_pepe_1#5$3", duration=1.5, isblock=true)]
[Delay(time=0.5)]
[name="佩佩"]你胸口的宝石......
[charslot(slot = "m", focus="n")]
[name="祖拜尔"]......我想这次，应该没有什么修复的可能了。
[charslot(slot = "m", name = "avg_4058_pepe_1#5$3")]
[name="佩佩"]如果宝石彻底碎掉，你会怎么样？
[charslot(slot = "m", focus="n")]
[name="祖拜尔"]会获得永恒的宁静。
[charslot(slot = "m", name = "avg_4058_pepe_1#5$3")]
[name="佩佩"]你会死。
[charslot(slot = "m", focus="n")]
[name="祖拜尔"]对......我会死。
[dialog]
[delay(time=1)]
[charslot(slot = "m", focus="n")]
[name="祖拜尔"]佩佩，看在我是你祖宗的分上，帮个忙好吗？
[charslot(slot = "m", name = "avg_4058_pepe_1#2$3")]
[name="佩佩"]你说。
[charslot(slot = "m", focus="n")]
[name="祖拜尔"]可以送我进入那颗宝石的中央吗？
[charslot(slot = "m", name = "avg_4058_pepe_1#4$3")]
[name="佩佩"]那是可以进去的吗？我以为那就是个巨大的摆设。
[charslot(slot = "m", focus="n")]
[name="祖拜尔"]不，那里存放着一些独属于我的东西。
[name="祖拜尔"]在这里度过无数光阴，因为它们的存在，我的守护也不算是全然为了他人。
[name="祖拜尔"]至少......有一些时日，它们是属于我的。
[dialog]
[PlaySound(key="$d_avg_axeimp", volume=0.6)]
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1", duration=0.5)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_4058_pepe_1#2$1")]
[name="佩佩"]我扶你起来......
[dialog]
[charslot]
[PlaySound(key="$d_avg_bellshake", volume=1)]
[charslot(slot = "m", name = "avg_npc_1479_1#4$1", posfrom="0,-30", posto="0,0", duration=2, isblock=true)]
[name="祖拜尔"]当心，佩佩，这副身躯很沉重，不过好在......我马上就要摆脱它了。
[name="祖拜尔"]对，走到它的底下。
[dialog]
[PlaySound(key="$d_avg_fsmummy", volume=1)]
[charslot(duration=1.5, isblock=true)]
搀扶着祖拜尔，佩佩来到了大厅的正中，那块巨型棱锥宝石的底部。
一瞬间，光线变化，虚影游移，巨大的宝石像是有引力般，将室内所有光线汇聚在底部的尖角。
佩佩本应觉得刺眼，但光线围过来的那一刻，她却觉得彷如被温暖的水流包裹。
[dialog]
[backgroundTween(xScaleFrom=1, xScaleTo=1.3, yScaleFrom=1, yScaleTo=1.3, yFrom=0, yTo=-100, duration=20)]
[PlaySound(key="$d_avg_lightsurge", volume=0, loop=true, channel="l")]
[SoundVolume(volume=1, channel="l",fadetime=2)]
[Blocker(a=0.5, r=255, g=255, b=255, fadetime=3, block=true)]
[SoundVolume(volume=0.2, channel="l",fadetime=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=3, block=true)]
[delay(time=0.5)]
[SoundVolume(volume=1, channel="l",fadetime=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=4, block=true)]
[background]
[StopSound(channel="l", fadetime=2)]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Image(image="avg_5_7_shining", screenadapt="coverall")]
[focusout(type="bg", from=0, to=1, duration=0.1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
我看到了，年轻的梦魇。这是你自己的梦。
向前走吧。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Image]
[focusout(type="bg", from=1, to=0, duration=0.1)]
[Background(image="53_g13_invertedpyramid",screenadapt="coverall")]
[PlaySound(key="$d_avg_stream_loop", volume=0, loop=true, channel="st")]
[SoundVolume(volume=0.2, channel="st",fadetime=2)]
[Delay(time=1)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="娜仁图亚"]......嗯？
[name="娜仁图亚"]怎么有种熟悉的感觉......好像又被循兽踩住脑袋了一样......
[name="娜仁图亚"]——嗯？！
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "m", name = "avg_4138_narant_1#12$1", posfrom="0,-30", posto="0,0", duration=1, isblock=true)]
[name="娜仁图亚"]喂，阿娜特，我在什么地方？阿斯帕齐娅，听得到吗？
[charslot(slot = "m", name = "avg_4138_narant_1#3$1")]
[name="娜仁图亚"]......通讯器摔坏了，不意外。
[charslot]
她从一尊漆黑的循兽雕像下坐起身来。空旷的厅堂中回荡着水流落下的声音。
一颗庞大的晶体倒悬在建筑穹顶上，随着它闪烁的光芒，厅堂中浮现出许多如同水中倒影般的人像。
[charslot(slot = "m", name = "avg_4138_narant_1#2$1")]
[name="娜仁图亚"]......这不是我那天晚上，在河边没追到的影子吗？
[name="娜仁图亚"]难道说，这座城市的人们，一年又一年，看到的就是这些影子？
[charslot]
[PlaySound(key="$d_avg_darkmagic", volume=0.7)]
一个人影停在了她面前。
娜仁图亚似乎能辨认出对方赤红的头发，还能看出对方正居高临下地审视着坐在地上的自己。
片刻之后，那个幻影转过身，走入了大厅尽头一道封闭的门。
[charslot(slot = "m", name = "avg_4138_narant_1#1$1")]
[name="娜仁图亚"]......你的头发挺红的，但我还是看到背影才觉得，你说不定是我认识的人。
[name="娜仁图亚"]毕竟我见过的梦魇，个个都是头也不回地在自己的路上狂奔。
[charslot(slot = "m", name = "avg_4138_narant_1#4$1")]
[name="娜仁图亚"]那句话怎么说的来着？“但愿河水上涨时它们被需要的人捡到”......你们也是水涨起来的时候才会浮现的影子，是不是？
[charslot(slot = "m", name = "avg_4138_narant_1#1$1")]
[name="娜仁图亚"]好，现在我需要找到裂隙，我相信你一次。
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(duration=1, isblock=true)]
[PlaySound(key="$d_avg_erthshkng", volume=0.4, loop=true, channel="e")]
[CameraShake(duration=4, xstrength=3, ystrength=3, vibrato=90, randomness=90, fadeout=true, block=false)]
[StopSound(channel="e", fadetime=6)]
[SoundVolume(volume=1, channel="st",fadetime=2)]
[delay(time=2)]
[StopSound(channel="b", fadetime=1)]
地板在轻微地震颤，水流落下的声音越来越响。
娜仁图亚踏过厅堂中的积水，向那个披挂甲胄的身影飞奔而去。
[charslot(slot = "m", name = "avg_4138_narant_1#10$1")]
[name="娜仁图亚"]这是——
[dialog]
[charslot]
大门的里侧，不是另一条迷宫甬道，也不是流淌的黄沙。
透过门缝，她一眼瞥见的是堆积如山的金银财宝，闪耀着千年不可磨灭的辉煌光芒。
但她甚至没有来得及惊呼。
[dialog]
[PlaySound(key="$d_avg_mnwtrfll", volume=0, loop=true, channel="mn")]
[SoundVolume(volume=1, channel="mn",fadetime=2)]
[Background(image="53_g15_invertedpyramid_ruin", screenadapt="coverall", fadetime=3)]
[StopSound(channe

... (全文21095字符)
```

### level_act35side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act35side/AS01.mp4")]
```

### level_act35side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="53_g5_museum",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[Delay(time=2)]
[playsound(key="$d_avg_crowdrun",volume=0.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4139_papyrs_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4139_papyrs_1#1$1")]
[name="匆忙的女孩"]那盏灯再吊高一些，我需要打在展品上的灯光完美地照出每一处细节。
[charslot(slot="m",name="avg_npc_1490_1#1$1")]
[name="博物馆员工"]好的，馆长女士！
[Dialog]
[playsound(key="$rungeneral", loop=true, channel="a",volume=0.7)]
[StopSound(channel="a", fadetime=1.2)]
[charslot(slot = "m",posfrom = "0,0", posto = "-200,0",duration = 0.7,afrom=1,ato=0)]
[delay(time=1)]
[charslot]
[charslot(slot="m",name="avg_4139_papyrs_1#5$1")]
[name="匆忙的女孩"]谁把这尊歌女胸像放在古历纪暗阑时代的雕像群中的？它们根本不在一个时代，快取出来，送到第二展厅去。
[charslot(slot="m",name="avg_npc_1491_1#1$1")]
[name="博物馆员工"]我去送！
[Dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "200,0",duration = 0.7,afrom=1,ato=0)]
[playsound(key="$rungeneral", loop=true, channel="b",volume=0.7)]
[StopSound(channel="b", fadetime=1.2)]
[delay(time=1)]
[charslot]
[charslot(slot="m",name="avg_4139_papyrs_1#1$1")]
[name="匆忙的女孩"]那件按古历纪咏叹时代制作技艺复原的乐器呢？为什么我没在展台上看到？
[Dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "-100,0",duration = 1)]
[delay(time=1.2)]
[charslot(slot = "m",posfrom = "-100,0", posto = "-100,-30",duration = 0.4)]
[playsound(key="$d_avg_open_woodbox")]
[delay(time=1)]
[charslot(slot = "m",posfrom = "-100,-30", posto = "-100,0",duration = 0.5)]
[delay(time=0.8)]
[charslot(slot="m",name="avg_4139_papyrs_1#2$1")]
[name="匆忙的女孩"]不在这里......
[Dialog]
[charslot(slot="m",name="avg_4139_papyrs_1#1$1")]
[charslot(slot = "m",posfrom = "-100,0", posto = "0,0",duration = 1)]
[delay(time=1.2)]
[charslot(slot = "m",posfrom = "0,0", posto = "0,-30",duration = 0.4)]
[playsound(key="$d_avg_open_woodbox")]
[delay(time=1)]
[charslot(slot = "m",posfrom = "0,-30", posto = "0,0",duration = 0.5)]
[delay(time=0.8)]
[charslot(slot="m",name="avg_4139_papyrs_1#4$1")]
[name="匆忙的女孩"]也不在这里......
[Dialog]
[charslot(duration=1)]
[stopmusic(fadetime=1)]
[delay(time=2)]
[playsound(key="$d_avg_harppluck", volume=0.5)]
[delay(time=2)]
[playMusic(key="$comedy_loop", volume=0.6)]
[name="愉悦的歌声"]♪远方的客人啊，莲花池中潋滟的水波泛过你来时的足迹♪
[name="愉悦的歌声"]♪树荫下，我备好了清甜的椰枣与醇香的啤酒♪
[name="愉悦的歌声"]♪何不一同举杯，共庆盛夏♪
[Dialog]
[playsound(key="$d_avg_clapsologirl")]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_1484_1#12$1",posfrom = "-100,0", posto = "0,0",duration = 0.5)]
[delay(time=0.8)]
[charslot(slot="l",focus="l")]
[name="谄媚的员工"]啊，梅捷缇克缇女士，您的歌声就像天籁，萦绕不停！
[Dialog]
[charslot(slot="r",name="avg_npc_1485_1#1$1",posfrom = "100,0", posto = "0,0",duration = 0.5)]
[delay(time=0.8)]
[charslot(slot="r",name="avg_npc_1485_1#1$1",focus="r")]
[name="奉承的员工"]呀，梅捷缇克缇女士，您的琴音正如流水，缓缓流淌！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1478_1#10$1",duration=1)]
[delay(time=1.5)]
[Effect(name="$e_emoji_musicalnote",layer = 1,x=-80,y=170)]
[name="梅捷缇克缇"]那当然，为了完美演绎这首古老的歌谣，我可是苦练了一个多月。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot="m",name="avg_4139_papyrs_1#1$1",duration=1)]
[delay(time=2)]
[name="匆忙的女孩"]......
[charslot(slot="m",name="avg_4139_papyrs_1#10$1")]
[name="匆忙的女孩"]啧，你们一个个说起话来像嘴上抹了蜜，干起活来就像脚底抹了油，根本找不到影。
[charslot(slot="m",name="avg_4139_papyrs_1#2$1")]
[name="匆忙的女孩"]缇缇，你应该知道，明天这件复原乐器就要展出了吧？
[charslot(slot="m",name="avg_npc_1478_1#5$1")]
[name="梅捷缇克缇"]今天先借迎宾部一用嘛，阿娜特。有贵宾莅临，本馆总是要好好招待一番的。
[charslot(slot="m",name="avg_4139_papyrs_1#8$1")]
[name="阿娜特"]这可是为漫灌节准备的特别展会，缇缇。
[name="阿娜特"]当前我们首要的任务是确保展会的每个环节都不出错。
[name="阿娜特"]这里的人眼光有多挑剔，你作为老员工应该比我更清楚。
[charslot(slot="m",name="avg_npc_1478_1#4$1")]
[name="梅捷缇克缇"]别抓狂嘛，馆长大人。
[charslot(slot="m",name="avg_npc_1478_1#9$1")]
[name="梅捷缇克缇"]我知道你刚上任就要策划如此重要的展会，难免会有点小焦虑。
[name="梅捷缇克缇"]但相信我，阿娜特，放平心态就好。无论我们展出什么，都会有人挑刺的。
[name="梅捷缇克缇"]毕竟米纳特哈玛仪城中，家家户户都有些珍贵的小私藏，看不上我们的展品很正常。
[charslot(slot="m",name="avg_4139_papyrs_1#1$1")]
[name="阿娜特"]......我要去查看明天亮相的新展品了。
[charslot(slot="m",name="avg_npc_1478_1#10$1")]
[name="梅捷缇克缇"]放心，我不会去打扰你和那位男士约会的。
[charslot(slot="m",name="avg_4139_papyrs_1#8$1")]
[name="阿娜特"]它是我的研究对象，不是约会对象。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot="m",posfrom = "0,0", posto = "-200,0",duration = 1.5,afrom=1,ato=0)]
[delay(time=2.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1478_1#5$1")]
[name="梅捷缇克缇"]是你看它的目光实在太深情了嘛。
[Dialog]
[MusicVolume(volume=0.3, fadetime=1)]
[charslot(slot="m",name="avg_npc_1478_1#2$1")]
[playsound(key="$d_avg_harppluck", volume=0.5)]
[delay(time=1.5)]
[MusicVolume(volume=0.6, fadetime=2)]
[charslot(slot="m",name="avg_npc_1478_1#5$1")]
[name="梅捷缇克缇"]奇怪......
[charslot(slot="m",name="avg_npc_1478_1#3$1")]
[name="梅捷缇克缇"]话说这都几点了，那些家伙还没接到人吗？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="53_g3_menatmainstreet_river",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_1490_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1491_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1490_1#1$1",focus="l")]
[name="无所事事的市民"]我猜，那个女孩是在观察水利设施的运作，好写一篇城市水利发展史的论文。
[charslot(slot = "right", name = "avg_npc_1491_1#1$1",focus="r")]
[name="百无聊赖的市民"]或许她是个铭文学家，只是在清理河中石碑上的污泥。
[charslot(slot = "left", name = "avg_npc_1490_1#1$1",focus="l")]
[name="无所事事的市民"]唉，有什么区别呢？不都是些搞历史的家伙。
[name="无所事事的市民"]只能怪我们的城市历史太悠久，全萨尔贡的史学家都喜欢往这里跑。
[charslot(slot = "right", name = "avg_npc_1491_1#1$1",focus="r")]
[name="百无聊赖的市民"]......是啊，看这四百年的古代河道，又宽又阔，看这两百年的建筑，又高又大。
[name="百无聊赖的市民"]什么叫厚重的历史传承？这就是。
[charslot(slot = "left", name = "avg_npc_1490_1#1$1",focus="l")]
[name="无所事事的市民"]那有什么能比得上漫灌节呢？那可是承自千年前的传统节日。
[charslot(slot = "right", name = "avg_npc_1491_1#1$1",focus="r")]
[name="百无聊赖的市民"]哦，等到河水泛滥，我将

... (全文32562字符)
```

### level_act35side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[playMusic(key="$wasteland_loop", volume=0.6)]
[Background(image="53_g8_sargondeluxeroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "r", name = "avg_4139_papyrs_1#4$1", duration=1)]
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", duration=1)]
[Delay(time=1.5)]
[charslot(slot = "r", name = "avg_4139_papyrs_1#4$1", focus="r")]
[name="阿娜特"]看起来祖拜尔似乎是打破了窗子......自己离开了？
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]我会去找他回来的。
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$1", focus="r")]
[name="阿娜特"]交给博物馆去找吧，佩佩，你已经很多天都没好好休息了。
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]黄金之城的使者很快就会抵达父亲的领地，阿娜特，我必须抓紧每一秒。
[charslot(slot = "r", name = "avg_4139_papyrs_1#9$1", focus="r")]
[name="阿娜特"]佩佩......
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]博物馆的损坏辛苦你和缇缇收拾了，或许有几个地方祖拜尔会去，我这就出发。
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$1", focus="r")]
[name="阿娜特"]佩佩，你知道我为何一开始不愿将祖拜尔借给你研究吗？其实收到你的来信后，我就想告诉你了......
[charslot(slot = "r", name = "avg_4139_papyrs_1#2$1", focus="r")]
[name="阿娜特"]在两个月前，我去你父亲的领地出差，在那里我见到黄金之城的使者已经抵达。
[name="阿娜特"]你的弟弟已经出发了。
[charslot(slot = "l", name = "avg_4058_pepe_1#12$1", focus="l")]
[name="佩佩"]......
[name="佩佩"]你知道，但你却没有告诉我。
[charslot(slot = "r", name = "avg_4139_papyrs_1#2$1", focus="r")]
[name="阿娜特"]你在信中兴高采烈地向我描述你的发现，在里面连写了二十个感叹号来表达自己的兴奋。
[charslot(slot = "r", name = "avg_4139_papyrs_1#10$1", focus="r")]
[name="阿娜特"]我......我实在是不忍心。
[charslot(slot = "l", name = "avg_4058_pepe_1#12$1", focus="l")]
[name="佩佩"]那你为什么又要把他借给我，你让我白高兴一场......
[charslot(slot = "r", name = "avg_4139_papyrs_1#2$1", focus="r")]
[name="阿娜特"]这里是宝石之城，佩佩！这里的宝石数不胜数，我以为你根本没可能找到！
[name="阿娜特"]我想着，或许时间一到你自己就放弃了。
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]可......可黄金之城的使者一向都是八月份才会到的啊？为什么会提前？
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$1", focus="r")]
[name="阿娜特"]你父亲上书，希望使者提前到来。
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]所以他们早就做好了决定，只是怕我不罢休，才趁我离开家寻找沙阿遗迹的时候，将那小子送入黄金之城。
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "l", name = "avg_4058_pepe_1#9$1", focus="l")]
[name="佩佩"]可父亲不是和我说......他会等着看到我的发现再做决断吗？
[charslot(slot = "r", name = "avg_4139_papyrs_1#9$1", focus="r")]
[name="阿娜特"]佩佩，长辈总是有自己的决断，不是我们这些小辈能插手的。
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]你见到那小子了吗？
[charslot(slot = "r", name = "avg_4139_papyrs_1#9$1", focus="r")]
[name="阿娜特"]......嗯。
[charslot(slot = "l", name = "avg_4058_pepe_1#3$1", focus="l")]
[name="佩佩"]他一定很得意吧，为了进入黄金之城，我与他不知道明里暗里较过多少回劲。
[charslot(slot = "r", name = "avg_4139_papyrs_1#9$1", focus="r")]
[name="阿娜特"]佩佩，你弟弟并不开心，我看得出，他的神色中始终隐藏着忧伤。
[name="阿娜特"]那天，他将我叫到书房，说自己知道这辈子和你再也不会有见面的机会，希望我能带句话给你。
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]他说了什么？
[charslot(slot = "r", name = "avg_4139_papyrs_1#9$1", focus="r")]
[name="阿娜特"]他说他希望你能记得他的声音。说完后，他便离开了。
[name="阿娜特"]他行李很少，而其中只有几样是他的，剩下的，全部与你和伯父有关。
[charslot(slot = "l", name = "avg_4058_pepe_1#5$1", focus="l")]
[name="佩佩"]......
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$1", focus="r")]
[name="阿娜特"]佩佩......？
[charslot(slot = "l", name = "avg_4058_pepe_1#5$1", focus="l")]
[name="佩佩"]从小到大，所有人都和我说，成为陛下身边的史官是为整个家族延续荣耀。但是阿娜特，荣耀往往是用牺牲与奉献换来的。
[name="佩佩"]进入黄金之城成为史官，意味着要终身留在城中，再也不能与家人朋友相见，能够陪伴在身边的，只有无数的书卷。
[charslot(slot = "r", name = "avg_4139_papyrs_1#2$1", focus="r")]
[name="阿娜特"]你最厌恶成日枯坐在书桌前了......不是吗，佩佩？
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1", focus="l")]
[name="佩佩"]是啊，我也想在有生之年走遍萨尔贡，自由自在地寻访每一处历史留下的痕迹。
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]但我不能这样......因为我不能让那小子得偿所愿。
[charslot(slot = "r", name = "avg_4139_papyrs_1#9$1", focus="r")]
[name="阿娜特"]佩佩，你就这么看不惯你弟弟吗？宁可自己难受也不能让他顺遂心意。
[charslot(slot = "l", name = "avg_4058_pepe_1#8$1", focus="l")]
[name="佩佩"]从小到大，谁见到那小子都会夸一句，说他性格文静又沉稳，是做史官的料子。
[name="佩佩"]只有我才清楚，他本性有多调皮多贪玩，让他在桌子前多坐一秒都是折磨。
[charslot(slot = "r", name = "avg_4139_papyrs_1#5$1", focus="r")]
[name="阿娜特"]那他和你争史官的位置是为了什么？
[charslot(slot = "l", name = "avg_4058_pepe_1#2$1", focus="l")]
[name="佩佩"]因为他不想我去黄金之城。
[name="佩佩"]他只是不想我一个人留在那里......
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$1", focus="r")]
[name="阿娜特"]那你......？
[charslot(slot = "l", name = "avg_4058_pepe_1#5$1", focus="l")]
[name="佩佩"]我也是......
[name="佩佩"]我也不想他一个人留在那里。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="53_g12_gemexchange",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_open_woodbox", volume=1)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1479_1#1$1", duration=0.5, isblock=true)]
[name="祖拜尔"]缓解站立过久导致的腿酸的宝石？不是这个。
[dialog]
[PlaySound(key="$d_avg_jewelryimpact", volume=1)]
[delay(time=1)]
[name="祖拜尔"]让对方主动道歉的宝石？有点用，但也不是我要找的。
[charslot(slot = "m", name = "avg_npc_1479_1#4$1")]
[name="祖拜尔"]我能感觉到那一颗宝石十分接近，但这间屋子里的宝石也太多了吧......
[dialog]
[charslot]
[PlaySound(key="$d_avg_pawfootstep_1", volume=1)]
[delay(time=1)]
[PlaySound(key="$d_avg_pawfootstep_3", volume=1)]
[delay(time=1)]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
听到走廊中传来的脚步声，祖拜尔立刻慌忙地躺回到巨大的镀金箱子里。
他感觉到了目光的注视，然而没有声音打破这一阵沉默，他忐忑地将眼睛睁开一条缝——
是一只沙色的动物。
[dialog]
[PlaySound(key="$d_avg_pawfootstep_3", volume=1)]
[charslot(slot = "m", name = "avg_npc_1482_1#6$1", posfrom="-200,0", posto="0,0", duration=1.5, isblock=true)]
[PlaySound(key="$d_avg_meowlong", volume=1)]
[charslot(slot = "m", name = "avg_npc_1482_1#1$1", duration=0.5, isblock=true)]
[delay(time=1.5)]
[charslot(slot = "m", focus="n")]
[name="祖拜尔"]噢......不可思议......
[d

... (全文14917字符)
```

### level_act35side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(key="$comedy_loop", volume=0.6)]
[Background(image="53_g10_grandbazaar_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1494_1#1$1", duration=1)]
[charslot(slot = "l", name = "avg_npc_804_1#1$1", duration=1)]
[Delay(time=1.5)]
[charslot(slot = "r", name = "avg_npc_1494_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_804_1#1$1", focus="l")]
[name="珠光宝气的市民"]唉，真可惜，我的庭院只被毁了一半。我想借此机会给庭院换个风貌，结果剩下的雕塑和绿植反而不便处理。
[name="珠光宝气的市民"]不过修复工作倒是差不多完成了，也许休息日你有兴趣来坐坐？
[charslot(slot = "r", name = "avg_npc_1494_1#1$1", focus="r")]
[name="衣着考究的市民"]多谢好意，恐怕我抽不开身。我的宝石收藏都混到了一起，为了恢复那间几百年的收藏室，我得先逐一鉴定石头的功效。
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$2", duration=1.5)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$3", duration=1.5)]
[Delay(time=1.5)]
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$2", focus="r")]
[charslot(slot = "l", name = "avg_4058_pepe_1#1$3", focus="n")]
[name="阿娜特"]所以，博物馆损坏的事情......
[Effect(name="$e_emoji_proud", layer = 1, x=-150, y=180)]
[charslot(slot = "l", name = "avg_4058_pepe_1#6$3", focus="l")]
[name="佩佩"]我绝对会瞒过去的！要是瞒不过去，我就对父亲晓之以理，动之以情......总之，他会帮忙说服所有投资者的。
[charslot(slot = "r", name = "avg_4139_papyrs_1#1$2", focus="r")]
[name="阿娜特"]还有博物馆那批特殊的新藏品。
[charslot(slot = "l", name = "avg_4058_pepe_1#6$3", focus="l")]
[name="佩佩"]放心，这个我也会在信里帮你们说清楚的。
[charslot(slot = "l", name = "avg_4058_pepe_1#1$3", focus="l")]
[name="佩佩"]不过，我不觉得父亲会同意你们对任何人展出宝石构装体复建的古建筑局部哦？
[charslot(slot = "r", name = "avg_4139_papyrs_1#13$2", focus="r")]
[name="阿娜特"]嗯，我理解，比起展示，博物馆更重要的工作是保存历史......也包括保持历史的背面不被人看见。
[charslot(slot = "r", name = "avg_4139_papyrs_1#14$2", focus="r")]
[name="阿娜特"]谢谢你，佩佩，我今晚可以睡个好觉了。
[charslot(slot = "l", name = "avg_4058_pepe_1#1$3", focus="l")]
[name="佩佩"]不对不对，不是该我对你们道谢吗？感谢你和缇缇帮我寻找宝石，完成了这次历史大发现，以及......
[dialog]
[charslot]
[charslot(slot="m", name="avg_4138_narant_1#4$1", duration=1, isblock=true)]
[name="娜仁图亚"]......
[charslot(slot = "m", name = "avg_4058_pepe_1#1$3")]
[name="佩佩"]呃......娜仁图亚小姐？
[charslot(slot="m", name="avg_4138_narant_1#2$1")]
[name="娜仁图亚"]......嗯？没事没事，就是听你们讲了半天博物馆的事有点无聊。
[charslot(slot = "m", name = "avg_4139_papyrs_1#13$2")]
[name="阿娜特"]抱歉，我把您请过来，原本是想和佩佩一起，向您表达感谢......
[Effect(name="$e_emoji_blackline", layer = 1, x=50, y=180)]
[charslot(slot = "m", name = "avg_4139_papyrs_1#11$2")]
[name="阿娜特"]娜仁图亚女士，您说希望把“优待阿雅吉和阿雅妮”写进馆规，我们正在......以一种比较隐晦的方式兑现。
[charslot(slot = "m", name = "avg_4058_pepe_1#4$3")]
[name="佩佩"]那是哪个时代的陶俑吗？
[charslot(slot = "m", name = "avg_4139_papyrs_1#13$2")]
[name="阿娜特"]不，是博物馆两名正式入职的新人。
[charslot(slot="m", name="avg_4138_narant_1#1$1")]
[name="娜仁图亚"]就算天气热得路都熔化了，也会按时去上班的两个傻子。
[charslot(slot = "m", name = "avg_4139_papyrs_1#13$2")]
[name="阿娜特"]在卸下代理馆长的职责，离开博物馆之前，我会交代大家特别关照她们的。
[charslot(slot = "m", name = "avg_4058_pepe_1#2$3")]
[name="佩佩"]......我还是很难相信，阿娜特。你真的要放弃现在的职位吗？
[charslot(slot = "m", name = "avg_4139_papyrs_1#11$2")]
[name="阿娜特"]哈哈，父亲不会喜欢我这个决定的。
[charslot(slot = "m", name = "avg_4139_papyrs_1#13$2")]
[name="阿娜特"]只是，我从记事起就一直透过窗户看着这座城市，现在我觉得，或许我已经把它读完了。
[name="阿娜特"]它的历史，它的前身。它深埋地下的、若没有你这样横冲直撞的探险者就不会被发掘的秘密。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5, isblock=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[background]
[Image(image="53_i12", screenadapt="coverall", xScale=1.05, yScale=1.05, fadetime=0)]
[ImageTween(xScaleFrom=1.05, yScaleFrom=1.05, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="阿娜特"]......真奇妙，只过了两天，城市就恢复运转了。
[name="阿娜特"]虽然那么多房子不知道要修补到什么时候，出现裂痕的路也要重新铺......但是水道已经完全清澈了。
[name="娜仁图亚"]那当然啦。河水是一直在流淌的嘛。
[name="佩佩"]是呀，河水永远向前流淌，无论多少座城市变成沙子，沙子上再建起多少座城市。
[name="佩佩"]......让流水带走一切，或许算不上一种选择，只是在永恒面前必然的结果。
[name="阿娜特"]但永恒本无意义。
[name="阿娜特"]唉，就像缇缇说的那样，博物馆偶尔办一些出格的展览，其实也不坏。
[name="佩佩"]哼哼，这个我也觉得。
[name="佩佩"]说起来，我来到这里之前，还真的幻想过一场惊心动魄的冒险。
[name="佩佩"]不过，我想的可不是现在这种，而是有人盯上了我的宝石，我跟他斗智斗勇。
[name="佩佩"]唉，实际上根本没人跟我作对，想想还有点可惜呢。
[name="娜仁图亚"]......哈哈。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[image]
[Background(image="35_g17_deserttown_d",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_4139_papyrs_1#1$2", duration=1.5, isblock=true)]
[name="阿娜特"]对了，佩佩，我还有一个问题想向你请教。
[name="阿娜特"]你知道的，我一直都很崇拜埃里克森先生。
[name="阿娜特"]既然我之前研究祖拜尔的论文已经全数作废......我希望像埃里克森先生一样，去看看大地上其他的地方。
[charslot(slot = "m", name = "avg_4139_papyrs_1#7$2")]
[name="阿娜特"]然后，像他一样将自己的见闻整理成信......再寄给他！
[name="阿娜特"]总之，我一定要和他成为笔友！
[charslot(slot = "m", name = "avg_4058_pepe_1#1$3")]
[name="佩佩"]哦，这倒是很充分的离开博物馆的理由。
[name="佩佩"]可是你站在城市街心花园里都能中暑，要去野外考察，至少也该先找个力士训练体能吧？
[charslot(slot = "m", name = "avg_4139_papyrs_1#13$2")]
[name="阿娜特"]所以我才要向你学习经验，佩佩。
[charslot(slot = "m", name = "avg_4139_papyrs_1#12$2")]
[name="阿娜特"]......我可以乘着有冷气的长途车走遍大地吗？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="53_g6_museum_core",screenadapt="coverall")]
[cgitem(image="cgitem_41_i12_1", style="cg", layer = 1)]
[charslot(slot = "m", name = "avg_npc_1484_1#1$1", posfrom="0,0", posto="0,-50")]
[charslot(slot = "m", action="zoom", poszoom = "0.5,0.5", scale=1.8, duration = 0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_devicebeep")]
[delay(time=0.5)]
[PlaySound(key="$d_avg_signlntrfrnc", volume=1)]
[bgeffect(name="$eb_signalInterference", layer=2)]
[

... (全文20187字符)
```

### training_act35side_01_a

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动35side教学关_01_a

[Battle.Pause]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(tileX=2, tileY=2, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_popka")]这种半透明的<@tu.kw>结晶</>看起来好诡异，我去看看！

[InputBlocker(blockInput=true, black=0)]

[Battle.Pause(pause=false)]
[Delay(time=1)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
别急——

```

### training_act35side_01_b

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动35side教学关_01_b

[Battle.Pause]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(protectTime=0.5, dialogHead="$avatar_popka")]\
哎呀！

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
不要那么着急！

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这是当地经常会出现的<@tu.kw>结晶</>。

[InputBlocker(blockInput=true, black=0)]

[Battle.Pause(pause=false)]
[Delay(time=2)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=true, black=0.2)]


[Tutorial(protectTime=0.5, dialogHead="$avatar_popka")]\
感觉自己身体好沉，胳膊也抬不动......

[Tutorial(tileX=2, tileY=2, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 看来这里的结晶还<@tu.kw>未被净化</>，上面有<@tu.kw>特殊的力场</>。

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这种特殊力场会导致<@tu.kw>我方干员</>的行动变得迟缓，<@tu.kw>攻击速度大幅降低</>。

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
站在结晶上的敌人的<@tu.kw>作战能力会被强化</>，遇到这样的结晶要千万小心！

```

### training_act35side_01_c

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动35side教学关_01_c

[Battle.Pause]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(protectTime=0.5, dialogHead="$avatar_popka")] \
那我们有什么方法能<@tu.kw>摧毁</>这些结晶吗？怎么感觉<@tu.kw>打不动</>。

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
常规攻击是无法摧毁如此<@tu.kw>坚硬</>的结晶的，只能造成<@tu.kw>一点点伤害</>。

[Tutorial(protectTime=0.5, dialogHead="$avatar_popka")] \
那我要怎么办？

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
我的个人经验是，只要<@tu.kw>攻击十次</>，结晶上面的<@tu.kw>力场</>就会被<@tu.kw>削弱</>，从而<@tu.kw>净化并消除</>结晶。

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
让克洛丝来帮你，她的<@tu.kw>攻击速度</>很快！

[Tutorial(protectTime=0.5, dialogHead="$avatar_kroos")] \
在~这~里~哦~
```

### training_act35side_01_d

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动35side教学关_01_d

[Battle.Pause]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(protectTime=0.5, dialogHead="$avatar_popka")] \
结晶<@tu.kw>消失了</>，确实有用！

[InputBlocker(blockInput=true, black=0)]

[Battle.Pause(pause=false)]
[Delay(time=5)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(protectTime=0.5, dialogHead="$avatar_popka")] \
哎？这些敌人居然会制造<@tu.kw>新的结晶</>！
```

### training_act35side_01_e

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动35side教学关_01_e

[Battle.Pause]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(tileX=3, tileY=2, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_popka")]这个<@tu.kw>被净化的结晶</>为什么<@tu.kw>没有消除掉</>？

[Tutorial(tileX=3.5, tileY=2, focusWidth=20, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", \
          dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]当这些<@tu.kw>结晶相连</>的时候，情况会发生变化，<@tu.kw>注意这里</>。


[Tutorial(tileX=4.5, tileY=2, focusWidth=20, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", \
          dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]还有这里。

[Tutorial(tileX=4, tileY=2, focusWidth=300, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", \
          dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]这些<@tu.kw>互相连接</>的结晶会<@tu.kw>彼此强化</>，形成一个<@tu.kw>更大的结晶区块</>。

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
我们只有将<@tu.kw>区块内所有的结晶</>都净化完毕，整个结晶区块才会<@tu.kw>一起消除</>。

[Tutorial(protectTime=0.5, dialogHead="$avatar_popka")] \
啊，我懂了，把这些区块当作<@tu.kw>一个整体</>就行！

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
完全正确！

[Tutorial(tileX=4.5, tileY=2, focusWidth=200, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_popka")]但现在有个问题，那些<@tu.kw>超出我们攻击范围</>的结晶该怎么处理？

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
不用担心！

[Tutorial(tileX=4, tileY=2, focusWidth=300, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", \
          dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]这些结晶<@tu.kw>互相连接</>后，内部结构也会<@tu.kw>互相连通</>。

[Tutorial(tileX=3, tileY=2, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", \
          dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]<@tu.kw>攻击已净化结晶</>仍然会生成<@tu.kw>新的净化效果</>。

[Tutorial(tileX=4, tileY=2, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", \
          dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]这些净化效果可以<@tu.kw>扩散到相邻的结晶上</>，但是净化的效果会<@tu.kw>减半</>。

[Tutorial(protectTime=0.5, dialogHead="$avatar_popka")] \
所以我们只要<@tu.kw>不断攻击</>一块<@tu.kw>已净化的结晶</>，<@tu.kw>净化的效果</>就可以<@tu.kw>扩散</>到与之相连的其他结晶上？

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
完全正确。
```


> 本章节共32个脚本文件，此处展示前30个。

## 统计

- 总字符数：442621
- 对话行数：3020


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
