# 明日方舟 · 活动剧情 · act40side（29段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act40side」完整剧情脚本（29个文件，3714行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act40side
- 脚本文件数：29

### level_act40side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="58_g1_yusrestaurant",screenadapt="coverall")]
[Delay(time=1)]
[playsound(key="$d_avg_livelyrestaurant", loop=true, channel="bgs")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_dishes")]
[Delay(time=1)]
[MusicVolume(volume=0.3, fadetime=3)]
[StopSound(channel="bgs", fadetime=2)]
[playMusic(intro="$newhope01_intro",key="$newhope01_loop", volume=0.6)]
[CameraEffect(effect="Grayscale", fadetime=2, keep=true, initamount=0, amount=1)]
[Delay(time=2)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="老板，结账。", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[name="后厨传来的声音"]忙着呢！
[name="后厨传来的声音"]嗐，不就一碗素面，算我请你的！
[dialog]
[Subtitle(text="那不行......", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[PlaySound(key="$d_avg_coin")]
[Delay(time=1)]
[PlaySound(key="$d_avg_chairrub")]
[Subtitle(text="钱放在桌子上了，走了。", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[name="后厨传来的声音"]慢走，再来啊！
[dialog]
[Delay(time=1)]
[Subtitle(text="这么大一年轻小伙子，午饭就吃这么点，像什么话？", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="五色令人目盲，五味令人口爽，口腹之欲不可放纵。", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="先生不也只吃这一碗素面？", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="哼，我这是第五碗。", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="我和你可不一样，我就是好这口清爽的。我吃饭从来不许下佐料，什么盐醋辣椒，葱蒜香料，通通不放。", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="吃东西就要吃食材原本的味道，食材要是有半点不新鲜，也骗不过我的舌头。", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="看这官服，先生是大理寺的少卿？那先生的舌头也是天下第一等的判官了。", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="哈哈哈，你倒是会说话。", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="下回要是碰上什么冤枉事，来大理寺找我。我叫虞澄。", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="......不必劳烦大人，在下区区一介礼部奉礼郎，不会有什么冤枉事。", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="没有事，请你吃面也成。小伙子，你叫什么？", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="......在下顾筌。", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[Dialog]
[stopmusic(fadetime=2)]
[Delay(time=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_livelyrestaurant", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=1, channel="bgs",fadetime=2)]
[Delay(time=1)]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.6)]
[playsound(key="$dooropenquite")]
[charslot(slot="r",name="avg_npc_1639_1#1$1",duration=0.5,posfrom = "50,0", posto = "50,0")]
[delay(time=1)]
[name="饭馆的熟客"]老姜，点菜！
[dialog]
[SoundVolume(volume=0.2, channel="bgs",fadetime=2)]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(slot = "left", name = "avg_npc_1621_1#1$1",posfrom = "-200,0", posto = "0,0",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_npc_1621_1#1$1",focus="l")]
[name="老姜"]来啦来啦！老刘，今天想吃啥？
[charslot(slot = "r",focus="r")]
[name="饭馆的熟客"]老规矩，今天有什么新鲜菜啊？
[charslot(slot = "left", name = "avg_npc_1621_1#1$1",focus="l")]
[name="老姜"]现在正是吃柿子的季节，今天还有新到的板栗，那叫一个生吃爽脆，熟食糯甜......那就给您上一道桂香柿子饼，一道板栗炖腩肉？
[charslot(slot = "r",focus="r")]
[name="饭馆的熟客"]讲究。行，就听你安排。
[name="饭馆的熟客"]说起来，之前帮你们店里修的这个招牌......
[charslot(slot = "left", name = "avg_npc_1621_1#5$1",focus="l")]
[name="老姜"]放心，我们大厨说过的，这顿不记您的账。
[name="老姜"]这些年店里的木匠活都多亏了您照应，请您吃几顿饭，不算事的。
[charslot(slot = "r",focus="r")]
[name="饭馆的熟客"]哈哈哈......厚道！
[name="饭馆的熟客"]别说，他这手艺，的确可以称得上天下第一了。出了这个门，别的馆子都吃不到这一口。
[name="饭馆的熟客"]之前送他那木牌小挂件，我可是真心的，他还害羞不肯收。
[charslot(slot = "left", name = "avg_npc_1621_1#1$1",focus="l")]
[name="老姜"]哎哟哟......可真是折煞人了。
[name="老姜"]我们就是一寻常小饭馆，多亏大伙关照才能开下去，就别提什么“天下第一”了。
[charslot(slot = "r",focus="r")]
[name="饭馆的熟客"]对了，你们小大厨人呢？今天没见他坐在外面陪客人聊天啊。
[charslot(slot = "left", name = "avg_npc_1621_1#8$1",focus="l")]
[name="老姜"]别提了，今天一早就在那闹别扭呢。
[name="老姜"]这阵子不是有一个挺出名的美食评论家，要借最近百珍宴的风头，访遍全城不为人知的小店，还要在报刊上挨个点评打分吗？
[charslot(slot = "r",focus="r")]
[name="饭馆的熟客"]我知道我知道，听说她发表文章，把百灶数得上号的饭馆酒楼横评了个遍，还写了本书，号称要收集百灶古往今来所有优秀菜谱。
[name="饭馆的熟客"]好像叫什么“行箸散人”？
[name="饭馆的熟客"]这位志气真是不小，百灶有多少家酒楼，这些酒楼又做了多少年的菜。写书的这位肚子里不仅要有墨水，还要装得下不少美食啊。
[charslot(slot = "left", name = "avg_npc_1621_1#1$1",focus="l")]
[name="老姜"]可不是吗......但听说她在写的那本《百灶食珍录》，那四大名楼的主厨看了都赞不绝口。她写的评论，那些名厨也没有不心服口服的。
[name="老姜"]小道消息说，那位高人今天就要逛到我们这一片了。
[charslot(slot = "r",focus="r")]
[name="饭馆的熟客"]这又何必闹别扭呢？就他的手艺，再厉害的评论家能挑出一个不是？
[charslot(slot = "left", name = "avg_npc_1621_1#1$1",focus="l")]
[name="老姜"]他那脾气您又不是不知道，不管好评差评，就是听不得别人对他的菜说三道四。
[charslot(slot = "left", name = "avg_npc_1621_1#3$1",focus="l")]
[name="老姜"]（小声）说着不愿意和别人在厨艺上争个谁先谁后，还不是怕有人的手艺比他的更受欢迎——
[dialog]
[PlaySound(key="$d_avg_steelbasin", volume=0.5)]
[Delay(time=0.5)]
[charslot(slot = "l", action="jump",posto = "0,0",power=15,times=1,duration = 0.3)]
[charslot(slot = "left", name = "avg_npc_1621_1#9$1",focus="all")]
[Delay(time=0.8)]
[charslot(slot = "left", name = "avg_npc_1621_1#8$1",focus="l")]
[name="老姜"]......不说了不说了！
[charslot(slot = "r",focus="r")]
[name="饭馆的熟客"]哈哈，我倒是怕这家小饭馆被谁带火了，我们这些老熟客就都排不上队咯。
[charslot(slot = "left", name = "avg_npc_1621_1#4$1",focus="l")]
[name="老姜"]借您吉言吧——哎呀，又来客人了。
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n")]
[PlaySound(key="$d_gen_walk_n", volume=0.6,delay=0.5)]
[charslot(slot = "left", name = "avg_npc_1632_1#1$1",duration = 1)]
[delay(time=0.5)]
[charslot(slot = "right", name = "avg_npc_1630_1#1$1",duration = 1)]
[delay(time=2.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1639_1#1$1")]
[name="饭馆的熟客"]哟，二位也是这个点才来吃饭呀。
[name="饭馆的熟客"]这小饭馆开在大理寺对

... (全文24907字符)
```

### level_act40side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[Delay(time=2)]
[playsound(key="$d_avg_breezetree")]
[delay(time=2)]
[name="年轻的声音"]您要带我看什么？
[playsound(key="$d_avg_snowbootwalk",channel="2")]
[name="坚定的声音"]加紧几步，快到了。
[dialog]
[delay(time=1)]
[playMusic(key="$m_sys_bitw_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot(slot = "left", name = "avg_npc_1612_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1617_1#1$2",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_npc_1612_1#1$1",focus="l")]
[name="麟青砚"]溪边踏雪，古梅闻香，虽然难得，但山下也并非没有。
[name="麟青砚"]想来只有这从峰顶俯瞰城市烟火的满眼景色，值得您特意绕路攀山。
[charslot(slot = "right", name = "avg_npc_1617_1#3$2",focus="r")]
[name="虞澄"]满城烟火又有什么好看的？麟青砚，我想带你看的，是这棵松树。
[charslot(slot = "left", name = "avg_npc_1612_1#2$1",focus="l")]
[name="麟青砚"]......劲松历寒，不损其翠。
[charslot(slot = "right", name = "avg_npc_1617_1#1$2",focus="r")]
[name="虞澄"]不，不是这些谁都会说的空话。
[name="虞澄"]这棵松树是我前往百灶就职前，亲手栽下的。我种下这棵树时，心中所想，应当与你别无二致。
[charslot(slot = "right", name = "avg_npc_1617_1#3$2",focus="r")]
[name="虞澄"]这么多年过去，我已非当初那个我，这棵树也不再是当初那棵树。
[charslot(slot = "left", name = "avg_npc_1612_1#13$1",focus="l")]
[name="麟青砚"]晚辈不明白......
[charslot(slot = "right", name = "avg_npc_1617_1#1$2",focus="r")]
[name="虞澄"]没关系，你现在只需要看到它，记住它就好。
[name="虞澄"]青砚......大理寺很适合你。你将来会成为一名出色的少卿，甚至是大理寺卿。
[name="虞澄"]那些案件对你来说不会是什么问题，你真正需要思考的问题只有一个——
[name="虞澄"]你能否担得起真相的分量？
[charslot(slot = "left", name = "avg_npc_1612_1#3$1",focus="l")]
[name="麟青砚"]......
[charslot(slot = "left", name = "avg_npc_1612_1#13$1",focus="l")]
[name="麟青砚"]我不明白。
[charslot(slot = "right", name = "avg_npc_1617_1#1$2",focus="r")]
[name="虞澄"]没关系，不用你现在明白。将来，你会时不时想起这棵松树，当你想起足够多次，有些事你自然就会明白。
[charslot(slot = "right", name = "avg_npc_1617_1#3$2",focus="r")]
[name="虞澄"]等我死了，你砍下它。用它的木，做我的棺材。
[charslot(slot = "left", name = "avg_npc_1612_1#10$1",focus="l")]
[name="麟青砚"]虞前辈......
[charslot(slot = "right", name = "avg_npc_1617_1#1$2",focus="r")]
[name="虞澄"]走吧，高处不胜寒，该回去了。
[playsound(key="$d_avg_snowbootwalk")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[delay(time=1)]
[PlaySound(key="$firestorm",volume=0.6)]
[bgeffect(name="$eb_burn",layer=1)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[bgeffect]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Sticker(id="st1", text="数载风雪，朝夕瞬华。", x=320,y=340, alignment="center", size=24, delay=0.001, width=700,block = true,duration=1)]
[Sticker(id="st1",duration=1,block = false)]
[delay(time=1)]
[Sticker(id="st1", text="我又一次想起了那棵松树，和那条铺满雪的山径。", x=320,y=340, alignment="center", size=24, delay=0.001, width=700,block = true,duration=1)]
[Sticker(id="st1",duration=1,block = false)]
[Dialog]
[delay(time=2)]
[PlaySound(key="$d_gen_dooropen")]
[delay(time=2)]
[Subtitle(text="虞澄，你该当何罪？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
[stopmusic(fadetime=2)]
[delay(time=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="58_g9_dalitemple",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1612_1#1$1",duration=1)]
[delay(time=2)]
[name="麟青砚"]......
[charslot(slot = "m", name = "avg_npc_041")]
[name="解真"]（轻微的鼾声）
[dialog]
[charslot(slot = "m", focus = "n")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$gavel1")]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_041")]
[charslot(slot = "m", action="jump",posto = "0,0",power=15,times=1,duration = 0.3)]
[delay(time=0.8)]
[charslot(slot = "m", name = "avg_npc_041")]
[name="解真"]咳咳......！
[name="解真"]呃......几时了？嫌疑人招了吗？
[charslot(slot = "m", name = "avg_npc_1612_1#2$1")]
[name="麟青砚"]解真御史，这样严肃的场合，还请注意言行。
[charslot(slot = "m", name = "avg_npc_041")]
[name="解真"]这是大理寺内部的家务事，这种场合肃政院就是来走个过场，无所谓的。
[name="解真"]不过今天这个审决的场面，倒是有趣......那位好脾气的大理寺卿大人，我还从来没见她发过这么大的火。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1613_1#4$1",duration=1)]
[delay(time=2)]
[name="谌彻"]虞澄！你曾经也在大理寺为官，在这面铜镜下发过誓。
[name="谌彻"]这大理寺决院，难道是让你撒泼犯浑的地方？！
[charslot(slot = "m", name = "avg_npc_1617_1#8$1")]
[name="虞澄"]真是冤枉，大理寺卿大人该问的都问了，我该招的也都招了，难道还不够配合？
[name="虞澄"]上个月十五号，夜里丑时三刻，大理寺卷牍库南区被人放了一把火。那把火就是我亲手放的。
[charslot(slot = "m", name = "avg_npc_1613_1#4$1")]
[name="谌彻"]荒唐！火灾发生时，你正被关押候审，如何纵火？
[name="谌彻"]如果这件事是你谋划的，你的同谋又是谁？
[charslot(slot = "m", name = "avg_npc_1617_1#3$1")]
[name="虞澄"]没什么同谋，不过确实有一个帮手......
[charslot(slot = "m", name = "avg_npc_1617_1#9$1")]
[name="虞澄"]一只羽兽。
[name="虞澄"]那天晚上，有一只受伤的羽兽落在我那间牢狱的窗边。我喂了它几粒米、一点清水。
[name="虞澄"]那羽兽颇有灵性，我救了它，它愿意帮我一个忙。我给了它一根点燃的稻草，让它飞到卷牍库去。
[charslot(slot = "m", focus = "n")]
[name="解真"]噗——
[name="解真"]咳咳......咳......
[charslot]
[charslot(slot = "m", name = "avg_npc_1613_1#4$1")]
[name="谌彻"]虞澄，决院里的人都没有工夫陪你瞎胡闹！
[charslot(slot = "m", name = "avg_npc_1617_1#1$1")]
[name="虞澄"]我也不敢胡闹，你问我什么，我答什么就是。
[charslot(slot = "m", name = "avg_npc_1613_1#4$1")]
[name="谌彻"]......好，既然你坚称是自己放的火，那就把细节交代清楚。
[name="谌彻"]那是什么种类的羽兽？
[charslot(slot = "m", name = "avg_npc_1617_1#2$1")]
[name="虞澄"]我哪认得是什么品种的羽兽，只记得通体乌黑，不见一根杂毛......与天下人心一般黑。
[charslot(slot = "m", name = "avg_npc_1613_1#4$1")]
[name="谌彻"]你说用稻草引火，可牢房里哪来的稻草？
[charslot(slot = "m", name = "avg_npc_1617_1#1$1")]
[name="虞澄"]从垫子里抽出来的。
[charslot(slot = "m", name = "avg_npc_1613_1#4$1")]
[name="谌彻"

... (全文35906字符)
```

### level_act40side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="58_g12_ningfucourtyard",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_animal_loop", volume=1)]
[Delay(time=2)]
秋高气爽。
[playMusic(key="$saferoom_loop", volume=0.6)]
庭院幽静，长长的院墙将主人与外面的喧嚣隔得很远。只有一棵老柿子树斜倚在院墙阴凉处，苍老的树冠越过了墙头。
没有人知道老树见过什么，只知道从这棵树在这深院中种下，春去秋来过几回，它便红过几回。
枝头的柿子红得发透，是年复一年的新鲜。往年摘下的果子、埋在泥中的叶，都算不上与现在有关。
老人就坐在树下，趁着树荫酣睡。
[dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_298_1#10$1",duration=1.5)]
[delay(time=2)]
[name="宁辞秋"]......爷爷。
[charslot]
[name="慈祥的老人"]......
[charslot(slot="m",name="avg_npc_298_1#4$1")]
[name="宁辞秋"]爷爷？
[charslot]
[name="慈祥的老人"]......
[name="慈祥的老人"]呼......嗯......
[dialog]
[playsound(key="$d_avg_clothmovement",volume=0.5)]
[charslot(slot="m",name="avg_npc_1614_1#1$1",duration=1.5)]
[delay(time=2)]
[name="慈祥的老人"]辞秋啊......回来啦？
[charslot(slot="m",name="avg_npc_298_1#10$1")]
[name="宁辞秋"]嗯......路上耽误了一点时间，总算赶在中秋节前回来啦。
[charslot(slot="m",name="avg_npc_1614_1#1$1")]
[name="慈祥的老人"]唉......前阵子我就天天惦记着，看着这柿子一天比一天红，就想你再不回来呀，今年的柿子都吃不到了。
[charslot(slot="m",name="avg_npc_1614_1#5$1")]
[name="慈祥的老人"]也不知道，我还能看这柿子树挂几次果，你要是再回来晚一点呀，可能就连我这把老骨头都见不到咯。
[charslot(slot="m",name="avg_npc_298_1#8$1")]
[name="宁辞秋"]爷爷......
[charslot(slot = "m", focus = "n")]
宁辞秋将说惯了的玩笑话咽了回去，她看着身边的老人，将他和自己离开前记下的模样细细比照。老人眯起的眼角似乎又多了几道皱纹。
秋风乍起，像是顽童攀上老人膝头，将老人理好的花白须发拨弄得散乱。
[charslot(slot="m",name="avg_npc_298_1#1$1")]
[name="宁辞秋"]大荒城第一个移动地块的试运行工作，到上个月才算完工。礼部在那边的工作算结束了，这才给我批了半个月的假。
[charslot(slot="m",name="avg_npc_1614_1#8$1")]
[name="宁述"]回来就好啊，这一趟，辛苦你了。
[charslot(slot="m",name="avg_npc_1614_1#1$1")]
[name="宁述"]大荒城的事，我一早都听说了。批评的话，也都写在信里了。
[name="宁述"]我知道救灾的时候你也出了力，但是保护百姓，是每一个炎国官员的本职。而作为礼部侍郎，这个监管不力的过错，你必须承担。
[name="宁述"]罚你半年俸禄，算是轻的，你不许有怨。
[charslot(slot="m",name="avg_npc_298_1#1$1")]
[name="宁辞秋"]当然不会，这次的过错，我会牢牢放在心上。
[charslot(slot="m",name="avg_npc_1614_1#6$1")]
[name="宁述"]辞秋，你要记得，永远不要想自己做到了什么，而是要问自己没有做到什么。
[name="宁述"]身为百姓父母官，也身为人臣，上承君命，下受民禄，官无大小，肩上的责任都是千钧重。
[name="宁述"]何况你已经在这个位置上，做得再多，都是本分，但凡有些许责任没能尽到，那就是天大的过错。
[name="宁述"]要是没有这样的觉悟，就穿不起这身赤色官服。
[charslot(slot="m",name="avg_npc_298_1#1$1")]
[name="宁辞秋"]“鞠躬尽瘁，如是而已。”爷爷过去的教导，我都记得。
[name="宁辞秋"]这次的过错固然要放在心上，可若因此产生了放弃的想法，那才是真的对不起自己的职责。
[charslot(slot="m",name="avg_npc_1614_1#6$1")]
[name="宁述"]嗯......
[charslot(slot="m",name="avg_npc_1614_1#1$1")]
[name="宁述"]行啦，教训的话就说到这。不在其位，不谋其事，礼部的事，我到底是管不着了。
[name="宁述"]我现在就是担心，孙女的伤怎么样了。
[charslot(slot="m",name="avg_npc_298_1#10$1")]
[name="宁辞秋"]早都已经康复啦，爷爷，您就别操心了。
[charslot(slot="m",name="avg_npc_1614_1#1$1")]
[name="宁述"]伤筋动骨一百天，大意不得。这两天安顿下来，有空还是上大夫那看看。前阵子正好有老同事给我送了几贴膏药，一会你也带点回去。
[charslot(slot="m",name="avg_npc_298_1#9$1")]
[name="宁辞秋"]好好，都听您的。
[charslot(slot="m",name="avg_npc_1614_1#8$1")]
[name="宁述"]你们几个年轻人，没一个让人省心的。
[name="宁述"]眼看着马上要从这搬回老家了，我的儿子女儿也没空回来看一眼，你姐姐也一天到晚不着家，谁会记挂我这个老头子？
[charslot(slot="m",name="avg_npc_298_1#10$1")]
[name="宁辞秋"]呵呵，您说姐姐贪玩我信，可您要说没人记挂您......我看您这两天闭门谢客，应该也不是无缘无故吧？
[charslot(slot="m",name="avg_npc_1614_1#2$1")]
[name="宁述"]哼，还提呢！现在这些小年轻，从来就不知道心思该放在哪。
[name="宁述"]从上个月起，从早到晚，这院子里就不能清闲一刻。
[name="宁述"]现在这些年轻人都还学精了，不敢明着送茶送酒，就盯着给我的花浇水。我那门口好不容易种的绣球呀，都给我浇死好几盆了！
[charslot(slot="m",name="avg_npc_298_1#10$1")]
[name="宁辞秋"]噗......
[name="宁辞秋"]这阵子您的客人这么多，我猜，是尚书大人带着草拟的百珍宴宴请名单来找您了吧。
[name="宁辞秋"]一年里难得能见到真龙，探听朝局消息的机会，肯定多的是人放在心上。
[charslot(slot="m",name="avg_npc_1614_1#2$1")]
[name="宁述"]我都不想理那个小子，他才是现在的礼部尚书，这种事怎么还需要我拿主意？
[charslot(slot="m",name="avg_npc_298_1#10$1")]
[name="宁辞秋"]谁让您为官几十载，在礼部留下那么多功绩，威望比谁都高呢？
[charslot(slot="m",name="avg_npc_1614_1#2$1")]
[name="宁述"]那也是过去的事了，老看着过去，后来人还怎么做事？
[charslot]
[name="宁府管家"]宁大人，门外有客人。
[charslot(slot="m",name="avg_npc_1614_1#1$1")]
[name="宁述"]不是说了闭门谢客吗......这位又是打哪来的？
[charslot]
[name="宁府管家"]客人说，他是玉门参知——
[charslot(slot="m",name="avg_npc_298_1#4$1")]
[name="宁辞秋"]咦......？
[charslot(slot="m",name="avg_npc_1614_1#1$1")]
[name="宁述"]玉门参知？这倒是没听说过......
[charslot(slot="m",name="avg_npc_1614_1#2$1")]
[name="宁述"]不管是什么官，不见，一概不见。
[charslot(slot="m",name="avg_npc_298_1#4$1")]
[name="宁辞秋"]爷爷，请稍等一下。这位客人，好像是来找我的。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="58_g3_baizaomainstreet_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="宁府杂役"]先生，宁大人最近几天闭门谢客，您还是改日再来吧。
[name="不善言辞的男子"]还是烦请再通报一下宁......宁大人，就说是一位老朋友来找她......
[name="宁府杂役"]先生，无意冒犯......可是看您的岁数，您确定是宁大人的“老朋友”？
[name="不善言辞的男子"]确实如此，在下不敢妄言......
[name="宁府杂役"]先生，您还是回去吧。宁大人实在不方便见客，作为“老朋友”，您也别让他为难了......
[dialog]
[delay(time=0.5)]
[playsound(key="$d_avg_open_door")]
[delay(time=3)]
[name="？？？"]梁大人......？
[name="不善言辞的男子"]——！
[dialog]
[charslot(slot="m",name="avg_npc_295_1#4$1",duration=0.5)]
[delay(time=1)]
[name="梁洵"]......
[charslot(slot="m",name="avg_npc_298_1#10$1")]
[name="宁辞秋"]不认识我了？
[charslot(slot="m",name="avg_npc_295_1#8$1")]
[name="梁洵"]宁小姐......好久不见......
[name="梁洵"]听说......听说你刚刚回到百灶，我想......来见见你。
[charslot]
梁洵的目光落在了宁小姐的身后，那儿正站着一位慈眉善目的老人。
[charslot(slot="m",name="avg_npc_1614_1#1$1")]
[name="宁述"]别站着啦，辞秋啊，快招呼你的朋友进来坐啊。
[charslot(slot="m",name="avg_npc_295_1#1$1")]
[name="梁洵"]这......
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(intro="$tech_intro",key="$tech_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_295_1#1$1")]
[name="梁洵"]......
[charslot(slot="m",name="avg_npc_298_1#1$1")]
[name="宁辞秋"]......
[charslot(slot="m",name="avg_npc_1614_1#1$1")]
[name="宁述"]咦，怎么都不动筷子？
[name="宁述"]哈哈，看来是我这个老头子打扰了你们年轻人的兴致。要不，我先回避？你们慢慢吃，慢慢聊。
[charslot(slot="m",name="avg_npc_295_1#4$1")]
[name="梁洵"]岂敢！是晚辈贸然叨扰，前辈设宴款待，我怎敢——
[charslot(slot="m",name="avg_npc_298_1#10$1")]
[name="宁辞秋"]爷爷，您就别吓唬他了。
[charslot(slot="m",name="avg_npc_1614_1#8$1")]
[name="宁述"]哈哈哈......梁洵小友，就不必客气了。
[name="宁述"]辞秋还在尚蜀的时候就常常来信，说那里的知府是体恤百姓又有才学的俊杰，今天终于得以一见。
[cha

... (全文23040字符)
```

### level_act40side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="58_g2_downtownarea",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(key="$m_avg_dailylifeofbaizao_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_1040_blaze2_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",focus="r")]
[name="行箸"]煌小姐，这个味道怎么样？
[charslot(slot = "left", name = "avg_1040_blaze2_1#5$1",focus="l")]
[name="煌"]唔......嗯......还不错。
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",focus="r")]
[name="行箸"]我是说......这家的桔红酥，是你印象里的那种味道吗？
[charslot(slot = "left", name = "avg_1040_blaze2_1#3$1",focus="l")]
[name="煌"]好像......还是不太一样。
[charslot(slot = "left", name = "avg_1040_blaze2_1#2$1",focus="l")]
[name="煌"]还是没有我吃过的甜，口感也有些区别......
[charslot(slot = "right", name = "avg_4172_xingzh_1#6$1",focus="r")]
[name="行箸"]奇怪，这家一心坊的点心，做法应该是最传统的，近一百年都没有变过才对。
[charslot(slot = "left", name = "avg_1040_blaze2_1#11$1",focus="l")]
[name="煌"]可是——啊，一百年？这道点心有那么久的历史吗？
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",focus="r")]
[name="行箸"]没有那么久，但在百灶，这样能叫得上名字的点心，或多或少都能追溯到一些历史的。
[name="行箸"]煌小姐在找的这种桔红酥，其实就是早年间，一位进京求学的书生发明的。
[name="行箸"]那书生的故乡盛产柑桔，他在百灶的时候，怀念故乡物产，但路途遥远，不能轻易吃到，于是他便发明了一种点心的做法。
[name="行箸"]将陈年桔皮碾碎，和进做月饼的酥皮里，只加少量佐料，简单烘烤。这种做法成本极低，而且做出来的点心真的有一股柑桔的香味。
[name="行箸"]书生把这种配方卖给住宿的旅店换取生活费，还为这点心写了句诗，“遥知桔林染，乡心一点红”。所以，这种点心就叫桔红酥了。
[name="行箸"]后来这位书生考校高中，这道桔红酥便被众人所知，在流传的过程中，也被赋予了“思乡”或“思念”的含义。
[charslot(slot = "left", name = "avg_1040_blaze2_1#2$1",focus="l")]
[name="煌"]象征思念......
[charslot(slot = "left", name = "avg_1040_blaze2_1#1$1",focus="l")]
[name="煌"]食物象征一种情感......这还从来没有听说过，唔......有意思。
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",focus="r")]
[name="行箸"]嗯，炎国幅员辽阔，不同地区的气候、物产天差地别，也因此诞生了不同的菜系。这一道道菜品，说是炎国民生的历史书也不为过。
[name="行箸"]像以炎国四大菜系为特色，大名鼎鼎的“四大名楼”，在百灶还不是移动城市的时候就有啦。
[name="行箸"]城市发展日新月异，但是一些味道却总能留下来，所以一道流行过的点心在历史里完全找不到踪迹，那才是怪事呢。
[charslot(slot = "left", name = "avg_1040_blaze2_1#1$1",focus="l")]
[name="煌"]听同事说过，炎国天师分类很多，你懂得这么多，你该不会是什么“美食天师”吧？
[charslot(slot = "right", name = "avg_4172_xingzh_1#11$1",focus="r")]
[name="行箸"]噗......要是真的有人的源石技艺可以“点石成菜”，那说不定还挺值得研究的。
[name="行箸"]不过我只是一个爱好者罢了，平时习惯将美食相关的所见所闻都用笔记下来。时间长了，记得的也就多了。
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",focus="r")]
[name="行箸"]话说回来，煌小姐，如果像你说的，真有能让点心变得更好吃的一种配方，那它不该不为人知呀。
[charslot(slot = "left", name = "avg_1040_blaze2_1#2$1",focus="l")]
[name="煌"]可我总记得，小时候吃到的桔红酥，就是要更甜更香一点。
[charslot(slot = "right", name = "avg_4172_xingzh_1#6$1",focus="r")]
[name="行箸"]这就有点奇怪了......
[name="行箸"]传统桔红酥的做法，讲究不见桔子的果肉但能吃出桔子的香气，所以对糖的用量非常克制，是种口味比较清淡的点心。
[name="行箸"]可煌小姐说的桔红酥加了很多糖......我也没有听说过有哪家的桔红酥做了这种改动。
[name="行箸"]或许我们可以委托一位点心师傅，让他试试多放糖呢？
[charslot(slot = "left", name = "avg_1040_blaze2_1#2$1",focus="l")]
[name="煌"]可是这样也没法证明我吃过的那种桔红酥曾经确实存在过吧。
[name="煌"]我还是很想知道，这种点心从百灶到维多利亚，怎么就变了味......背后一定有故事。
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",focus="r")]
[name="行箸"]看来煌小姐的爱好，和我是一样的呢。
[name="行箸"]我还担心，带着你走了这么多地方，你会不耐烦呢。
[charslot(slot = "left", name = "avg_1040_blaze2_1#1$1",focus="l")]
[name="煌"]本来就是拜托你带我在百灶旅游的，你怎么还和我客气上了？
[charslot(slot = "right", name = "avg_4172_xingzh_1#11$1",focus="r")]
[name="行箸"]嗯，我们再多去找找吧！
[name="行箸"]不过时间也不早了，我们先去吃午饭吧。
[charslot(slot = "left", name = "avg_1040_blaze2_1#11$1",focus="l")]
[name="煌"]嗯？午饭？
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",focus="r")]
[name="行箸"]到了饭点，可不就该吃午饭吗？
[charslot(slot = "left", name = "avg_1040_blaze2_1#8$1",focus="l")]
[name="煌"]可是我们刚刚才去过五家点心店啊？！
[charslot(slot = "right", name = "avg_4172_xingzh_1#7$1",focus="r")]
[name="行箸"]那怎么能一样，点心是点心，不能当正餐的呀！
[charslot(slot = "left", name = "avg_1040_blaze2_1#13$1",focus="l")]
[name="煌"]我的肚子，已经满了......
[charslot(slot = "right", name = "avg_4172_xingzh_1#12$1",focus="r")]
[name="行箸"]呵呵......我知道一家小店，保证不会让你的肚子遭罪的。
[name="行箸"]煌小姐愿意赏光吗？
[charslot(slot = "left", name = "avg_1040_blaze2_1#5$1",focus="l")]
[name="煌"]你都这么说了，那我当然就“舍肚子陪君子”啦！
[charslot(slot = "left", name = "avg_1040_blaze2_1#2$1",focus="l")]
[name="煌"]......嗯？
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",focus="r")]
[name="行箸"]怎么了？
[charslot(slot = "left", name = "avg_1040_blaze2_1#2$1",focus="l")]
[name="煌"]总觉得......有人在跟着我们。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[curtain(direction = 0,fillfrom = 0.1,fillto =0.15,block=false)]
[curtain(direction = 4,fillfrom = 0.1,fillto =0.15,block=true)]
[charslot(slot="l",name="avg_2026_yu_1#15$1",posfrom = "-800,0", posto = "-800,0")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "l",posfrom = "-800,0", posto = "-380,0",duration = 2)]
[delay(time=2.3)]
[charslot(slot = "l", name = "avg_2026_yu_1#8$1")]
[charslot(slot = "l", action="jump",posto = "0,0",power=50,times=1,duration = 0.4)]
[delay(time=0.6)]
[charslot(slot = "l",posfrom = "-380,0", posto = "-900,0",duration = 0.7)]
[delay(time=0.8)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain]
[delay(time=2)]
[charslot(slot = "m", name = "avg_npc_1612_1#1$1")]
[Background(image="58_g3_baizaomainstreet_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$plot_intro",key="$plot_loop", volume=0.6)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1612_1#2$1")]
[name="麟青砚"]你是......禁军？
[charslot(slot = "m", name = "avg_npc_1615_1#1$1")]
[name="凛然的女性"]不要误会，不着玄铁甲，我还不属于正式禁军。只论官职，我是隶属于御林卫的校将。
[name="凛然的女性"]麟少卿应该也不会想去做那个在光天化日之下见到玄铁甲的人。
[charslot(slot = "m", name = "avg_npc_1612_1#3$1")]
[name="麟青砚"]......我听太合提起过，禁军学徒中有一位翘楚，年纪轻轻，实力已远超同僚。
[charslot(slot = "m", name = "avg_npc_1612_1#1$1")]
[name="麟青砚"]你就是那位小教头......
[charslot(slot = "m", name = "avg_npc_1615_1#4$1")]
[name="“禁军小教头”"]哼，不过是比武输给过我几次，他也不用这么惦记着，倒显得小气。
[charslot(slot = "m", name = "avg_npc_1615_1#2$1")]
[name

... (全文22984字符)
```

### level_act40side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="58_g8_baizaoacademy",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$newhope01_intro",key="$newhope01_loop", volume=0.6)]
[CameraEffect(effect="Grayscale", fadetime=2, keep=true, initamount=0, amount=1)]
[Delay(time=2)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="哟，这么巧，你也在这。", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="虞兄来学宫的藏书阁，是要查档案资料？", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="借两本书回去垫枕头，最近晚上总是睡不好，翻上几页书，倒头就睡。", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="还是这些学生好啊，脑袋里装得下书，心里装不下事。", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="虞兄说笑了......", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="也不是说笑，在大理寺天天泡在那一桩桩腌臜案子里，人都要腌入味了。", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="人都说百灶学宫的藏书阁是天底下最干净清白的地方，只留圣贤语，不存奸佞言......我在这坐一会，洗洗心。", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="顾筌兄以前也是学宫的学生？", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="很多年前的事了......", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="只是忝为学宫的学子，在学业上毫无建树，也没能做些什么实事，心中多是惭愧。", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="唯有一件幸事，在这里得遇良师指点，终身受用。", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="你说的这位老师......", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="......已经不在了。", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="那你今天来又是为了什么？是来借书？", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="查些档案资料......", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="礼部最近筹办庆典，需要参考一些旧时礼制......", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[stopmusic(fadetime=2)]
[Subtitle(text="呵......", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Subtitle(text="你是欺我这个大理寺少卿有眼无珠，还是不认字？", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="你手上拿的卷宗，分明是十五年前，太师谋逆的案子！", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="你可知这是什么样的禁忌？你好大的胆子......", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="我......无可隐瞒。", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="我确实在查找这件案子的相关资料，我怀疑......这背后还有隐情。若虞澄兄认为我在做不法之事，那将在下抓起来便是。", x=100, y=300, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="嚷嚷什么......我说要抓你了？我就是想说......", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Subtitle(text="......正巧，我也对这个案子很有兴趣。", x=600, y=500, alignment="left", size=24, delay=0.04, width=600)]
[Dialog]
[Subtitle]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2)]
[CameraEffect(effect="Grayscale", fadetime=2, amount=0, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_belltower", volume=1)]
[Delay(time=2)]
[playMusic(key="$victorianormal_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_1622_1#1$1",duration = 1)]
[delay(time=2)]
[name="认真的学生"]今天课上与老师辩论，获益匪浅。不过关于当今新政的种种问题，我还是坚持自己的观点。
[name="认真的学生"]今天遗留下的问题，我会继续思考的。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1631_1#1$1",duration = 0.5)]
[delay(time=1)]
[name="百灶学宫讲师"]无妨，这座学宫的校园够宽敞，足够容下不同的思想和声音。如果我的观点无法说服你，那你就不该因为我讲师的身份而勉强认同。
[name="百灶学宫讲师"]身处这座学宫里的学生，当以天下民生为己任，但也要注意，切不可沉湎于想象与空谈。
[charslot(slot = "m", name = "avg_npc_1622_1#1$1")]
[name="认真的学生"]多谢老师。
[dialog]
[charslot(duration=0.5)]
[Delay(time=1)]
[PlaySound(key="$bigbell", volume=1)]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.4, channel="bgs",fadetime=2)]
[PlaySound(key="$d_avg_crowdrun", volume=0.6,delay=1,channel="2")]
时钟悬挂在古朴楼宇的顶端，日影和时针一并流转。清脆的钟声响起，不一会，熙攘的人群便挤满了校园。
一个身影逆人流而上，摩肩接踵之间，看守也没有注意到这个陌生面孔。
[StopSound(channel="bgs", fadetime=2)]
[dialog]
[charslot(slot="m",name="avg_npc_1644_1#1$1",duration=1)]
[delay(time=2.5)]
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1628_1#1$1",duration = 0.5)]
[delay(time=1)]
[name="谨慎的学生"]你好......？请问，需要什么帮助吗？
[charslot(slot="m",name="avg_npc_1644_1#2$1")]
[name="麟青砚"]同学，请问，存放学生档案的档案室怎么走？
[charslot(slot = "m", name = "avg_npc_1628_1#1$1")]
[name="谨慎的学生"]你是问学籍科？你有什么事吗？
[charslot(slot="m",name="avg_npc_1644_1#1$1")]
[name="麟青砚"]我是新来的助教，教授让我去整理一下往届毕业生的档案......
[charslot(slot = "m", name = "avg_npc_1628_1#1$1")]
[name="谨慎的学生"]奇怪......
[name="谨慎的学生"]是哪一位教授？
[charslot(slot="m",name="avg_npc_1644_1#1$1")]
[name="麟青砚"]兵部属学院，讲军事理论的景教授。
[name="麟青砚"]她今天满课，所以才派我来帮她处理。
[charslot(slot = "m", name = "avg_npc_1628_1#1$1")]
[name="谨慎的学生"]啊......！
[charslot(slot="m",name="avg_npc_1644_1#2$1")]
[name="麟青砚"]怎么了？
[charslot(slot = "m", name = "avg_npc_1628_1#1$1")]
[name="谨慎的学生"]从这里往前走，过了主楼以后右转，丙申号楼就是了。
[name="谨慎的学生"]你......还是快点去吧，千万不能耽误了！
[charslot(slot="m",name="avg_npc_1644_1#1$1")]
[name="麟青砚"]......多谢。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="58_g13_yuskitchen",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(key="$comedy_loop", volume=0.6)]
[charslot(slot="m",name="avg_2026_yu_1#1$1",duration=1)]
[delay(time=2)]
[name="小大厨"]咳咳，任何饭店的第一道规矩——进了这后厨，大厨的话就是绝对的指令。
[name="小大厨"]你想要通过鼎丰楼的厨师选拔，去见那个莫不服，那从现在起，就要老老实实听我的指挥，明白了吗？
[charslot(slot="m",name="avg_1040_blaze2_1#1$1")]
[name="煌"]咱们不是约好了，拿到奖金三七分成，怎么你说得跟我欠你人情一样？
[charslot(slot="m",name="avg_2026_yu_1#2$1")]
[name="小大厨"]行了行

... (全文33502字符)
```

### level_act40side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="58_g1_yusrestaurant",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
一大早，小饭馆的门外尚冷清，仅有几只羽兽在落叶上来回蹦跶。
[playsound(key="$d_avg_wing")]
对门大理寺的值夜人打了个长长的呵欠，惊得羽兽四散飞离。
[dialog]
[playMusic(key="$normal_loop", volume=0.6)]
[charslot(slot="m",name="avg_2026_yu_1#1$1",duration=1.5)]
[delay(time=1.5)]
[name="小大厨"]啊——呜......
[charslot(slot="m",name="avg_2026_yu_1#19$1")]
[name="小大厨"]昨晚做了噩梦，梦见有只循兽把我后厨里的面粉都吃光了。好可怕......
[dialog]
[charslot]
[playsound(key="$rungeneral", loop=true, channel="bgs")]
[charslot(slot = "m", name = "avg_1040_blaze2_1#1$1",posfrom = "200,0", posto = "0,0",duration = 0.7)]
[delay(time=1)]
[StopSound(channel="bgs", fadetime=0.5)]
[delay(time=0.3)]
[name="煌"]早！
[dialog]
[CameraShake(duration=0.1, xstrength=10, ystrength=10, vibrato=10, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_plateplace")]
[delay(time=0.5)]
[charslot(slot="m",name="avg_1040_blaze2_1#1$1")]
[name="煌"]请！
[charslot(slot="m",name="avg_2026_yu_1#8$1")]
[name="小大厨"]你......学会了？
[charslot(slot="m",name="avg_2026_yu_1#9$1")]
[name="小大厨"]你这黑眼圈......难道真做了一整夜？
[charslot(slot="m",name="avg_1040_blaze2_1#6$1")]
[name="煌"]哈哈，也就到后半宿吧......行箸到现在还没醒呢。
[charslot(slot="m",name="avg_1040_blaze2_1#1$1")]
[name="煌"]先不说别的了，快尝尝这面！
[charslot(slot="m",name="avg_2026_yu_1#9$1")]
[name="小大厨"]你......啊？
[charslot(slot="m",name="avg_2026_yu_1#15$1")]
[name="小大厨"]你没学会和面，就煮了一把挂面来给我交差？！
[charslot(slot="m",name="avg_1040_blaze2_1#2$1")]
[name="煌"]这可不是一般的挂面。这是行箸和我挑遍了市面上所有种类的挂面后，精心挑选出的口感最接近你做的面的一款。
[name="煌"]当然，相比于手工面，口感还是略差一些的。不过行箸还对你汤底配方稍微进行了一点调整——保证做出来的口味和你做的差不多。
[charslot(slot="m",name="avg_2026_yu_1#15$1")]
[name="小大厨"]歪门邪说，投机取巧，还乱改我的配方！
[charslot(slot="m",name="avg_1040_blaze2_1#1$1")]
[name="煌"]先别急着下结论，你尝尝再说嘛！
[charslot]
[charslot(slot="m",name="avg_2026_yu_1#15$1", focus = "n")]
小大厨皱着眉，用筷子挑起几缕面，小心翼翼地闻了闻，才送入口中。
[playsound(key="$d_avg_eatnoodle_single",volume=0.5)]
[charslot(slot="m",name="avg_2026_yu_1#15$1")]
[name="小大厨"]......唔。
[charslot(slot="m",name="avg_1040_blaze2_1#2$1")]
[name="煌"]怎么样？
[charslot(slot="m",name="avg_2026_yu_1#9$1")]
[name="小大厨"]......嗯。
[charslot(slot="m",name="avg_1040_blaze2_1#2$1")]
[name="煌"]说话啊！
[charslot(slot="m",name="avg_2026_yu_1#8$1")]
[name="小大厨"]你们......为什么会觉得这样做就能行？
[charslot(slot="m",name="avg_1040_blaze2_1#4$1")]
[name="煌"]主要是行箸都快饿得不行了。当时想着，与其就这么和面团干耗着，不如先用你的配方做碗我能做的面给她吃。
[name="煌"]后来想了想，长寿面最重要的可能不是味道，而是让吃面的人有被祝福的感觉。
[charslot(slot="m",name="avg_1040_blaze2_1#2$1")]
[name="煌"]有些人就是学不会你这一手做面条的功夫，但是用一把挂面也能给自己或家人送上祝福，这就是长寿面的意义。
[charslot(slot="m",name="avg_1040_blaze2_1#1$1")]
[name="煌"]你看，这面条黄灿灿的，是不是比你那一碗看上去还热闹一点？
[charslot(slot="m",name="avg_1040_blaze2_1#7$1")]
[name="煌"]呃......当然，投机取巧也是事实啦......
[charslot(slot="m",name="avg_2026_yu_1#9$1")]
[name="小大厨"]你说“被祝福的感觉”......你觉得自己做出来了吗？
[charslot(slot="m",name="avg_1040_blaze2_1#2$1")]
[name="煌"]我......应该吧？
[charslot(slot="m",name="avg_1040_blaze2_1#1$1")]
[name="煌"]昨晚第一次成功做出这碗面的时候，我和行箸一起分享了。我觉得吃得很开心，她还偷偷抹眼泪来着......
[charslot(slot="m",name="avg_2026_yu_1#4$1")]
[name="小大厨"]把手工面换成了挂面，也跟着调整了香油和盐的用量，倒也算动了脑子......那位姑娘的舌头真是厉害。
[charslot(slot="m",name="avg_2026_yu_1#2$1")]
[name="小大厨"]但是挂面煮完需要过凉水，你做是做了，却没把凉水沥干。
[name="小大厨"]凉水留得太多，降低了汤的温度，也影响了整碗面的口感。要想精益求精的话，这些细节下次最好也要照顾到。
[charslot(slot="m",name="avg_1040_blaze2_1#5$1")]
[name="煌"]啊......好，我记住了！
[charslot(slot="m",name="avg_1040_blaze2_1#1$1")]
[name="煌"]欸，你说这话的意思是......
[charslot(slot="m",name="avg_2026_yu_1#3$1")]
[name="小大厨"]打住，我就是看在你花了心思的分上，决定继续教你罢了。
[charslot(slot="m",name="avg_2026_yu_1#2$1")]
[name="小大厨"]和面还是要接着练的，你总不能真的打算带着一把挂面去参加比赛吧？
[charslot(slot="m",name="avg_1040_blaze2_1#1$1")]
[name="煌"]嘿嘿，行！
[charslot(slot="m",name="avg_2026_yu_1#2$1")]
[name="小大厨"]这只是师父心软，觉得徒弟开窍了一点。但客人到底买不买单，还是要检验一番的。
[charslot(slot="m",name="avg_1040_blaze2_1#2$1")]
[name="煌"]这......要怎么检验？
[charslot(slot="m",name="avg_2026_yu_1#2$1")]
[name="小大厨"]等会儿客人来了，如果有点面条的，你就做一碗送去。
[name="小大厨"]客人要是觉得不好吃，那你就接着练习吧。
[charslot(slot="m",name="avg_1040_blaze2_1#1$1")]
[name="煌"]......我这就去！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="58_g1_yusrestaurant",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$dooropenquite")]
[delay(time=1)]
[PlaySound(key="$d_avg_walkfast")]
[charslot(slot="m",name="avg_1040_blaze2_1#1$1",duration=0.5)]
[delay(time=1)]
[name="煌"]这位客人！要不要来一碗本店新推出的特色长寿面！
[charslot]
[name="衣着光鲜的食客"]今天又不是我的生日，怎么平白无故让我吃长寿面？
[charslot(slot="m",name="avg_1040_blaze2_1#5$1")]
[name="煌"]呃......小店菜品试新，让客人免费品尝！
[charslot(slot="m",name="avg_1040_blaze2_1#1$1")]
[name="煌"]不对......您要是吃完觉得满意，还是付一下钱比较好，我也得给我们老板交差......
[charslot]
[name="衣着光鲜的食客"]真有意思，这小店的生意还有这种做法。
[name="衣着光鲜的食客"]把面放下吧，就算我点的。
[charslot(slot="m",name="avg_1040_blaze2_1#1$1")]
[name="煌"]（热切的眼神）
[charslot]
[name="衣着光鲜的食客"]呃......还有事吗？
[charslot(slot="m",name="avg_1040_blaze2_1#5$1")]
[name="煌"]没，没！我就是想等您吃过后，听听您的评价。
[charslot]
[name="衣着光鲜的食客"]好好......我吃就是。
[playsound(key="$d_avg_dishes")]
食客拿起筷子，先后夹起一根面、一片青菜、一点葱花，都仔细品尝过。
他动作优雅，可不一会的工夫，一碗面已经见底。
[charslot(slot="m",name="avg_1040_blaze2_1#1$1")]
[name="煌"]味道如何？
[charslot]
[name="衣着光鲜的食客"]嗯......好吃，很好吃。
[charslot(slot="m",name="avg_1040_blaze2_1#11$1")]
[name="煌"]真......真的？！
[charslot]
[name="衣着光鲜的食客"]这汤很鲜，所用食材也很讲究，如果再炖上一天一夜，味道能更完美。
[name="衣着光鲜的食客"]可是我已经很饿了，等不了那么久。如果为了那点“完美”再等上一天一夜，我恐怕早就饿死了。
[name="衣着光鲜的食客"]他想要求一份完美的味道，但客人却等不住了。
[name="衣着光鲜的食客"]即便我愿意等他，有些事也是没法再等下去了。
[charslot(slot="m",name="avg_1040_blaze2_1#2$1")]
[name="煌"]您这话......
[charslot]
[name="衣着光鲜的食客"]不要紧，你把我的话转告你们老板就行。
食客站起身，他衣服上的纹样流光溢彩，光线在他身侧扭曲虚化，让人看不清他的面孔。
[charslot(slot="m",name="avg_1040_blaze2_1#8$1")]
[name="煌"]哎，您......您还没给钱呢！
[charslot]
[dialog]
[charslot(slot = "m", name = "avg_npc_1236_1#9$1",duration = 1)]
[delay(time=1.5)]
[name="衣着光鲜的食客"]从我账上扣吧。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(tim

... (全文15453字符)
```

### level_act40side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="58_g15_restaurantlobby",screenadapt="coverall")]
[Delay(time=2)]
[name="礼貌的招待"]欢迎光临鼎丰楼。
[dialog]
[delay(time=0.5)]
[PlaySound(key="$d_avg_gateopen")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[playMusic(key="$m_avg_dailylifeofbaizao_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_1040_blaze2_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_1040_blaze2_1#5$1",focus="l")]
[name="煌"]哇......这就是传说中的鼎丰楼。
[charslot(slot = "right", name = "avg_4172_xingzh_1#6$1",focus="r")]
[name="行箸"]你......还紧张吗？
[charslot(slot = "left", name = "avg_1040_blaze2_1#1$1",focus="l")]
[name="煌"]嗯？有什么好紧张的。
[charslot(slot = "right", name = "avg_4172_xingzh_1#6$1",focus="r")]
[name="行箸"]马上就要比赛了，可为什么，我有种心虚的感觉......
[name="行箸"]毕竟......
[charslot(slot = "left", name = "avg_1040_blaze2_1#1$1",focus="l")]
[name="煌"]怕什么，小大厨最后都说可以了。
[name="煌"]再说了，我们又不是真的去当厨子的，我们只是想找到那位传奇大厨，亲口问问他那种桔红酥的做法。
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",focus="r")]
[name="行箸"]事到如今，也只能这么说服自己了......
[dialog]
[charslot]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1635_1#1$1",duration=1.5)]
[delay(time=2)]
[name="严厉的考官"]时间差不多了。观赛的客官请在这里留步，参赛的厨师请随我上前。
[charslot]
[charslot(slot = "left", name = "avg_1040_blaze2_1#1$1",focus="r")]
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",focus="r")]
[name="行箸"]遇到难题的时候，千万别冲动，冷静思考，总有办法的......
[charslot(slot = "left", name = "avg_1040_blaze2_1#5$1",focus="l")]
[name="煌"]放心吧，我去啦。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_npc_1635_1#1$1",duration=0.5)]
[delay(time=1)]
[name="严厉的考官"]请坐。
[name="严厉的考官"]虽说您今天是来参加考试的，但远来是客，还请先用一杯茶。
[charslot]
[playsound(key="$pourwater")]
考官端起桌上的茶壶，为煌倒上茶水，清甜的香味顿时盈满鼻腔。
[charslot(slot = "m", name = "avg_1040_blaze2_1#1$1")]
[name="煌"]说是比赛，这氛围还挺友好的嘛......
[charslot(slot = "m", name = "avg_1040_blaze2_1#5$1")]
[name="煌"]正好路上口渴，多谢啦！
[playsound(key="$d_avg_drinkswllw")]
[charslot]
煌拿起茶盏，仰头满饮。
[playsound(key="$d_avg_paper2")]
紧接着，考官将纸笔放在她的面前。
[charslot(slot="m",name="avg_npc_1635_1#1$1")]
[name="严厉的考官"]这壶茶中泡了几味料，写下来。
[charslot(slot = "m", name = "avg_1040_blaze2_1#8$1")]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=15, randomness=90, fadeout=true, block=false)]
[multiline(name="煌")]噗——
[charslot(slot = "m", name = "avg_1040_blaze2_1#11$1")]
[multiline(name="煌")]咳咳咳咳......啥？！
[charslot(slot = "m", focus = "n")]
煌看向自己的茶盏，仅剩的一点水珠挂在杯壁上。煌又抬起头看向了眼前的考官，他的脸上依然挂着一副礼貌的微笑。
[charslot(slot = "m", name = "avg_1040_blaze2_1#8$1")]
[name="煌"]我还能......再来一杯吗？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="58_g10_restaurantkitchen",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_1635_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1636_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1635_1#1$1",focus="l")]
[name="悠闲的厨师"]我估计今天应该是没戏咯，从上午到现在来了几十号人，到现在这第一关都没人能过。
[charslot(slot = "right", name = "avg_npc_1636_1#1$1",focus="r")]
[name="无聊的厨师"]总厨出题也太刁钻了，考试的人一进门就是这样一出，换谁来都会蒙啊。
[charslot(slot = "left", name = "avg_npc_1635_1#1$1",focus="l")]
[name="悠闲的厨师"]舌头就是厨师的眼睛，要是舌头上的功夫不过关，厨艺也高不到哪里去。
[name="悠闲的厨师"]连这一关都过不了，那也不用浪费总厨时间了，还是叫他们早些打道回府的好。
[dialog]
[charslot(slot = "m", focus = "n")]
[stopmusic(fadetime=2)]
[playsound(key="$doorknockquite")]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_npc_1635_1#1$1",focus="l")]
[name="悠闲的厨师"]哎哎客人，这里可是后厨。你怎么——
[dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1612_1#1$1",duration=1.5)]
[delay(time=2)]
[name="麟青砚"]大理寺查案，烦请各位配合。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[charslot(slot = "m", name = "avg_1040_blaze2_1#2$1")]
[Background(image="58_g15_restaurantlobby",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$newhope01_intro",key="$newhope01_loop", volume=0.6)]
[name="煌"]冷静......冷静......
[name="煌"]Mechanist说过，人的舌头只能尝出四种味道，但是鼻子可以分辨出上百种味道......
[name="煌"]虽然我也没有从他的“机油”酒中闻出过什么味就是了......
[charslot(slot = "m", focus = "n")]
煌小心翼翼地端起已经没那么烫的茶盏，仔细嗅闻着杯中余味。
[charslot(slot = "m", name = "avg_1040_blaze2_1#3$1")]
[name="煌"]能闻到花香，应该是茉莉花的味道......
[name="煌"]不，不止是茉莉花，还有一种......对，是菊花！小大厨饭馆里待客的菊花茶就是这种味道！
[charslot(slot = "m", name = "avg_1040_blaze2_1#2$1")]
[name="煌"]除了花香，茶水喝下去的时候，我记得明明有一点酸甜味......
[name="煌"]前面的料都不带酸，那最后的那点味道到底是什么......
[name="煌"]这个酸酸甜甜的味道，好像有点熟悉？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[charslot(slot = "left", name = "avg_1040_blaze2_1#1$1")]
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1")]
[Background(image="58_g2_downtownarea",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[delay(time=0.5)]
[charslot(slot = "left", name = "avg_1040_blaze2_1#1$1",focus="l")]
[name="煌"]为什么要带我来喝这个梅子酒？
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",focus="r")]
[name="行箸"]这梅子酒，其实也算百灶的一样特色。
[name="行箸"]在百灶城北方，有一大片梅林。每年六月初夏，新鲜的梅子成熟的时候，人们会采下许多拿来泡酒，最好是用小寒酒来泡。
[charslot(slot = "right", name = "avg_4172_xingzh_1#11$1",focus="r")]
[name="行箸"]嗯......这种苔麦酿成的酒，有种特殊的香味，搭配梅子正好。
[name="行箸"]泡制三个月左右的时间，到中秋就刚好能喝了。
[charslot(slot = "left", name = "avg_1040_blaze2_1#1$1",focus="l")]
[name="煌"]梅子酒......也有什么历史吗？
[charslot(slot = "right", name = "avg_4172_xingzh_1#1$1",focus="r")]
[name="行箸"]你刚才不是问我......那些百灶建城时牺牲的人，后来都怎样了吗？
[charslot(slot = "right", name = "avg_4172_xingzh_1#3$1",focus="r")]
[name="行箸"]其实也算不上什么历史，我只是想起

... (全文19604字符)
```

### level_act40side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="58_g10_restaurantkitchen",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$m_bat_kjerag_h_intro",key="$m_bat_kjerag_h_loop", volume=0.6)]
[PlaySound(key="$d_avg_firemagic")]
[CameraShake(duration=1.3, xstrength=30, ystrength=30, vibrato=35, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, afrom=1, rfrom=1, gfrom=1, bfrom=1, fadetime=1, block=false)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_1040_blaze2_1#9$1")]
[name="煌"]当心！
[charslot(slot="m",name="avg_npc_1619_1#7$1")]
[name="莫不服"]怎么回事——
[dialog]
[charslot]
[PlaySound(key="$fireburst")]
[Blocker(a=0.8, r=0.5, g=0.2, b=0.1, fadetime=0.5, block=true)]
[bgeffect(name="$eb_burn",layer=1)]
[playsound(key="$d_avg_churchfire", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.4, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, afrom=1, rfrom=1, gfrom=1, bfrom=1, fadetime=1, block=false)]
火焰自头顶燃起，点点火星从天花板落下，引燃了灶台上的面粉和油，顷刻间，后厨就化作了一片火海。
[charslot(slot="m",name="avg_npc_1619_1#4$1")]
[name="莫不服"]咳咳咳——！
[charslot(slot="m",name="avg_npc_1619_1#5$1")]
[name="莫不服"]你......走......不用管我！
[charslot(slot = "m", name = "avg_1040_blaze2_1#9$1")]
[name="煌"]捂住口鼻，别说话！
[name="煌"]这一招可能用得不是很熟练......试试吧。
[charslot(slot = "m", name = "avg_1040_blaze2_1#2$1")]
[name="煌"]麻烦低下头。
[dialog]
[charslot(duration=0.3)]
[PlaySound(key="$d_avg_windmagic")]
[CameraShake(duration=1, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[Background(image="58_g10_restaurantkitchen",x=0, y=0, xScale=1.1, yScale=1.1, fadetime=1)]
煌拿起刀，在掌心划出一道口子。一个气旋在煌的掌心逐渐成形，随即又扩散出去，形成一道气浪。
[dialog]
[PlaySound(key="$d_avg_strongwind")]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.5, block=true)]
[bgeffect(name="$eb_steam_sw",layer=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.5)]
[CameraShake(duration=1, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[BackgroundTween(xFrom=0, yFrom=0, xTo=0, yTo=0, xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=0.5, block=false)]
[Blocker(a=0.2, r=1, g=1, b=1, fadetime=2)]
[StopSound(channel="bgs", fadetime=5)]
[playsound(key="$d_avg_knockoverdish")]
[playsound(key="$d_avg_sundries",channel="2",volum=0.5)]
[bgeffect(layer=1)]
汹涌的气浪席卷了整个房间，火焰霎时熄灭，厨房中的厨具和货架也被吹得七零八落。
[dialog]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1619_1#1$1",duration=0.5)]
[Delay(time=0.5)]
[name="莫不服"]竟然有这样的本事......你难道是......
[name="莫不服"]......多谢。
[charslot(slot = "m", name = "avg_1040_blaze2_1#1$1")]
[multiline(name="煌")]不客气——
[charslot(slot = "m", name = "avg_1040_blaze2_1#2$1")]
[multiline(name="煌")]嗯？
[dialog]
[charslot]
[CameraShake(duration=1.5, xstrength=20, ystrength=2, vibrato=10, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_drawbridge", loop=true, channel="bgs")]
[Delay(time=1.5)]
[StopSound(channel="bgs", fadetime=2)]
煌抬头看去，吊灯架外饰已经烧得漆黑，露出通红的铁筋，架子在空中摇摇欲坠。
[charslot(slot = "m", name = "avg_1040_blaze2_1#9$1")]
[name="煌"]莫不服，躲开！
[dialog]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=0.5, block=true)]
[charslot]
[charslot(slot="r",name="avg_npc_1619_1#7$1")]
[Blocker(a=0.2, r=1, g=1, b=1, style = "slider", inverse = false, fadetime=0.5, block=true)]
[PlaySound(key="$d_avg_clothmovementsp")]
[charslot(slot = "l", name = "avg_1040_blaze2_1#9$1",posfrom = "-150,0", posto = "50,0",duration=0.5)]
[Delay(time=0.51)]
[charslot(slot = "m", focus = "n")]
煌抓住了老人的手臂，想要将他拉到一旁，但吊灯已经落下——
[charslot]
[dialog]
[Delay(time=0.3)]
[Blocker(a=0.2, r=1, g=1, b=1, afrom=0.6, rfrom=1, gfrom=1, bfrom=0.5, fadetime=1.5, block=false)]
[CameraShake(duration=0.3, xstrength=15, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_lightningmagic")]
[charslot(duration=0.3)]
[PlaySound(key="$d_avg_smashcello",delay=1,channel="2")]
[PlaySound(key="$d_avg_windowbreak",delay=1,channel="3")]
一声沉闷的雷鸣后，原本径直坠下的残骸骤然改变了方向，被重重地砸在了墙上。
[dialog]
[charslot(slot="m",name="avg_npc_1612_1#16$1",duration=0.5)]
[Delay(time=1)]
[name="麟青砚"]......没事吧？
[charslot(slot = "m", name = "avg_1040_blaze2_1#11$1")]
[name="煌"]惊蛰？！你怎么会在这？
[charslot(slot="m",name="avg_npc_1612_1#2$1")]
[name="麟青砚"]......我是不是该问问，你又为什么会出现在这里？
[charslot(slot = "m", name = "avg_1040_blaze2_1#8$1")]
[name="煌"]我......
[charslot(slot="m",name="avg_npc_1612_1#1$1")]
[name="麟青砚"]回头再和你算账......
[charslot(slot="m",name="avg_npc_1612_1#3$1")]
[name="麟青砚"]上个月，鼎丰楼的火，是不是也是这样......？
[charslot(slot = "m", focus = "n")]
麟青砚环顾四周，后厨的厨师们早已乱作一团。而她的目光很快锁定了一个戴着面具的身影。
那人似乎对上了她的视线，随即转身消失在人群中。
[charslot(slot="m",name="avg_npc_1612_1#16$1")]
[name="麟青砚"]......！
[name="麟青砚"]煌，留在这里，保护好莫不服！
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "250,0",duration = 0.5,afrom=1,ato=0)]
[delay(time=1)]
[charslot]
[charslot(slot = "m", name = "avg_1040_blaze2_1#11$1")]
[name="煌"]哎！你上哪去？
[charslot(slot = "m", name = "avg_1040_blaze2_1#9$1")]
[name="煌"]咳咳......这烟，呛死我了。
[charslot(slot="m",name="avg_npc_1619_1#4$1")]
[name="莫不服"]咳咳咳......那边的立柱上有拉闸......
[charslot(slot = "m", name = "avg_1040_blaze2_1#8$1")]
[name="煌"]这......这么多......到底该拉哪个......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="58_g15_restaurantlobby",screenadapt="coverall")]
[Blocker(a=0.2, r=1, g=1, b=1, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_clothmovementsp")]
麟青砚身轻如羽，几个起落间，那人已经被逼到角落。
只隔着数米的距离，但空气中烟尘弥漫，麟青砚看不清楚那个人的身形。
[CameraShake(duration=0.3, xstrength=5, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_lightningmagic")]
他正欲再跑时，一道炸雷就落在了他的身旁。
[charslot(slot="m",name="avg_npc_1612_1#16$1")]
[name="麟青砚"]站住！
[name="麟青砚"]你再动一下，下一道雷就会落在你头上。
[name="麟青砚"]回答我的问题。
[charslot(slot = "m", focus = "n")]
[name="戴面具的人"]......
[charslot(slot="m",name="avg_npc_

... (全文13743字符)
```

### level_act40side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[name="行箸"]你来了。
[dialog]
[PlaySound(key="$d_avg_snowstormflp", volume=0, loop=true, channel="sn")]
[PlaySound(key="$d_avg_open_door", volume=1)]
[charslot(slot = "m", name = "avg_4172_xingzh_1#1$1")]
[Background(image="58_g12_ningfucourtyard",screenadapt="coverall")]
[SoundVolume(volume=0.8, channel="sn",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1.5)]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_1040_blaze2_1#2$1", duration=1.5, isblock=true)]
[name="煌"]宁府的邀约，我没有不来的道理。
[charslot(slot = "m", name = "avg_4172_xingzh_1#9$1")]
[name="行箸"]......对不起，我不是有意瞒着你，我只是觉得，这不是需要刻意提及的事......
[charslot(slot = "m", name = "avg_1040_blaze2_1#2$1")]
[name="煌"]也没什么好道歉的，大小姐总有些难言之隐。我也不是那种因为别人是贵族就要摆臭脸的人。
[charslot(slot = "m", name = "avg_1040_blaze2_1#1$1")]
[name="煌"]所以，我该怎么称呼你？宁家大小姐？
[charslot(slot = "m", name = "avg_4172_xingzh_1#1$1")]
[name="宁茵"]我......叫宁茵。
[charslot(slot = "m", name = "avg_4172_xingzh_1#3$1")]
[name="宁茵"]其实，我不能算是宁家的人，我是从小被爷爷收养的。
[name="宁茵"]爷爷对所有人都介绍说，我是宁家的远房亲戚，可我从来没有见过哪怕一个和我有血缘关系的“亲人”。
[charslot(slot = "m", name = "avg_4172_xingzh_1#1$1")]
[name="宁茵"]我和你说过的，你记得吗？
[charslot(slot = "m", name = "avg_1040_blaze2_1#3$1")]
[name="煌"]我不太会说安慰人的话......
[charslot(slot = "m", name = "avg_4172_xingzh_1#1$1")]
[name="宁茵"]没什么，爷爷他对我很好，也从来不会有谁因为我的身份与我为难......大家都待我很好。
[charslot(slot = "m", name = "avg_1040_blaze2_1#2$1")]
[name="煌"]你的爷爷......就是前任礼部尚书，宁述？
[charslot(slot = "m", name = "avg_4172_xingzh_1#9$1")]
[name="宁茵"]是......
[charslot(slot = "m", name = "avg_1040_blaze2_1#9$1")]
[name="煌"]正好，我——
[charslot(slot = "m", name = "avg_4172_xingzh_1#9$1")]
[name="宁茵"]我知道......我知道。
[dialog]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_4172_xingzh_1#1$1")]
[name="宁茵"]天气有点冷，别在外面站着了，我们到屋里去说，好吗？
[charslot(slot = "m", name = "avg_1040_blaze2_1#3$1")]
[name="煌"]......都行。
[dialog]
[StopSound(channel="sn", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(key="$saferoom_loop", volume=0.6)]
[Image(image="cg_watersurface", screenadapt="coverall", xScale=1.1, yScale=1.1, fadetime=0)]
[ImageTween(xFrom=60, xTo=-60, duration=20, block=false)]
[PlaySound(key="$d_avg_animal_loop", volume=0, loop=true, channel="a")]
[delay(time=1)]
[SoundVolume(volume=0.4, channel="a",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_breezetree", volume=1)]
[Delay(time=1)]
蜿蜒漫长的游廊，穿过一片假山和竹林，又将一湾荷塘分为两半。
凉风拂过，秋水轻漾，宁茵与煌的倒影一前一后，行于廊桥之上。两人走过一间间空荡荡的屋子，打包好的行李和落叶铺了一地。
[name="宁茵"]院子里有些杂乱，实在不是待客的样子，失礼了。
[name="宁茵"]我们一家人很快就要从这里搬出去了，爷爷上了年纪，受不了百灶的干燥气候，准备要搬回江南老家了。
[name="煌"]......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[Background(image="58_g12_ningfucourtyard",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
宁茵走得很慢，可发觉友人无心赏景后，只得加快了一些脚步。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_4172_xingzh_1#1$1", duration=1.5, isblock=true)]
[name="宁茵"]就在前面，快到了。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[Background(image="bg_indoor",screenadapt="coverall")]
[delay(time=0.1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot(slot = "m", name = "avg_4172_xingzh_1#1$1")]
[name="宁茵"]你先坐，我去后厨拿些茶点过来。家里的厨师都已经休假去了，只有一些冷盘——
[charslot(slot = "m", name = "avg_1040_blaze2_1#2$1")]
[name="煌"]不用那么麻烦，我待不了太久。
[charslot(slot = "m", name = "avg_4172_xingzh_1#9$1")]
[name="宁茵"]......那么着急吗？
[charslot(slot = "m", name = "avg_4172_xingzh_1#2$1")]
[name="宁茵"]好吧......
[dialog]
[charslot(duration=1, isblock=true)]
[PlaySound(key="$doorclosequite", volume=0.5)]
[StopSound(channel="a", fadetime=1)]
宁茵轻轻掩上门，屋外羽兽的啼鸣渐弱，整个屋内显得更加寂静无声。
[charslot(slot = "m", name = "avg_1040_blaze2_1#2$1")]
[name="煌"]说吧，你到底为什么要约我来这里。
[charslot(slot = "m", name = "avg_4172_xingzh_1#9$1")]
[name="宁茵"]抱歉......其实昨天在鼎丰楼，发生火灾后，我想要去找你。
[name="宁茵"]结果，我无意间听到了你和那位大理寺少卿与莫大厨的谈话......
[charslot(slot = "m", name = "avg_1040_blaze2_1#2$1")]
[name="煌"]所以呢？
[charslot(slot = "m", name = "avg_4172_xingzh_1#2$1")]
[name="宁茵"]煌，我或许......见过你的父亲。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="58_g12_ningfucourtyard",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlayMusic(key="$monastery_sad_loop", volume=0.6)]
我记得十五岁那年，家里来了一位门客。
爷爷的工作繁忙，府上来来往往的门生同僚很多，那也大都与我无关。
可我慢慢注意到，府上多了一个穿蓝色低品官袍的人。我每次看见他，他都是孤身一人，好像从来不与人来往。
起初，我也没有放在心上，直到那年生日......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[background]
[PlaySound(key="$d_avg_firework_amb", volume=0, loop=true, channel="fire")]
[SoundVolume(volume=1, channel="fire",fadetime=2)]
和往年一样，爷爷为我举办了很热闹的生日宴。
宴会上张灯结彩，高朋满座，可是我认识的人也没有几个。
客人们高谈阔论，谈论的也是我听不懂的事。直到我偷偷从宴席上溜出来，也没人注意到我。
我一个人在院子里游荡了很久，觉得无聊，一时兴起，跑去了爷爷的书房。
[dialog]
[StopSound(channel="fire", fadetime=2)]
[charslot]
[Background(image="bg_indoor",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$dooropenquite", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
我在那里，又一次见到了那位先生。
我还记得，当时他正在把一叠信纸和几支笔装进口袋，他看到我时好像很慌张，又匆忙把口袋里的纸笔掏了出来。
[dialog]
[charslot(slot = "m", name = "avg_4172_xingzh_1#7$1", duration=0.5, isblock=true)]
[name="宁茵"]你......
[charslot(slot = "m", name = "avg_npc_1616_1#7$1")]
[name="神色慌张的男人"]小姐误会了！
[name="神色慌张的男人"]我......还有一些信没有抄完，想带回家去抄。因为是尚书大人要寄给重要官员的信，要

... (全文23802字符)
```

### level_act40side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Background(image="58_g12_ningfucourtyard",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", duration=1)]
[charslot(slot = "l", name = "avg_4172_xingzh_1#3$1", duration=1)]
[Delay(time=1.5)]
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", focus="r")]
[name="宁述"]你那位朋友这么快就走了？也不留人家吃个饭？
[charslot(slot = "l", name = "avg_4172_xingzh_1#3$1", focus="l")]
[name="宁茵"]嗯......她还有别的要紧事，没法久留啦。
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", focus="r")]
[name="宁述"]从小到大，都不见你带朋友回来，还想着可以认识一下。
[charslot(slot = "l", name = "avg_4172_xingzh_1#3$1", focus="l")]
[name="宁茵"]或许，也算不上是朋友......
[charslot]
老人看着垂头丧气的宁茵，想说些什么，却终究没有开口，只是伸手拂去了她肩头的落叶。
[charslot(slot = "l", name = "avg_4172_xingzh_1#3$1", focus="n")]
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", focus="r")]
[name="宁述"]快要走了，还有好多事放不下吧？
[charslot(slot = "l", name = "avg_4172_xingzh_1#9$1", focus="l")]
[name="宁茵"]......爷爷也是吗？
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", focus="r")]
[name="宁述"]呵呵，前些日子总盼着赶紧回去，真要走了，看着这一草一木，又都放不下了。
[name="宁述"]还记得吗？当年就在这亭子里，铺一层沙，拾一根棍，一笔一画地教你写字。
[name="宁述"]你当时和我说，来年，府上所有的对联都要由你来写。我陪你练了两个月，最后你自己坚持不下去了。
[charslot(slot = "r", name = "avg_npc_1614_1#8$1", focus="r")]
[name="宁述"]结果第二年，你还真送了我一副对联。
[name="宁述"]“花好月圆吃得饱，天长地久......”
[charslot(slot = "l", name = "avg_4172_xingzh_1#9$1", focus="l")]
[name="宁茵"]这些事，爷爷都还记得。
[charslot(slot = "r", name = "avg_npc_1614_1#8$1", focus="r")]
[name="宁述"]哪能忘呢......又是一年中秋，日子过得真快啊。
[dialog]
[PlaySound(key="$d_avg_wind", volume=1)]
[delay(time=1.5)]
[charslot(slot = "r", name = "avg_npc_1614_1#8$1", focus="r")]
[name="宁述"]我们爷孙两个是不是很久没这样聊过天了？
[charslot(slot = "l", name = "avg_4172_xingzh_1#2$1", focus="l")]
[name="宁茵"]......嗯。最近我一直出门在外，爷爷您也忙着接待客人，见面的机会都很少。
[charslot(slot = "r", name = "avg_npc_1614_1#4$1", focus="r")]
[name="宁述"]这次举家离京，折腾得不轻。
[name="宁述"]不过回到琅珆就清净了，路上也有大把时间让我们谈天说地。
[dialog]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1614_1#8$1", focus="r")]
[name="宁述"]你自己的那本书，终于要写完了？
[charslot(slot = "l", name = "avg_4172_xingzh_1#2$1", focus="l")]
[name="宁茵"]......
[name="宁茵"]爷爷，我可能......不能和你一起回琅珆了。
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", focus="r")]
[name="宁述"]......何时做的决定？
[charslot]
宁茵轻轻摇头，身子却往后退了几步。
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_4172_xingzh_1#2$1", focus="l")]
[name="宁茵"]爷爷此次归乡，是叶落归根，人之常情，家里人都非常明白。然而路途遥远，换谁也放心不下。
[name="宁茵"]宁家人才辈出，每个人都为大炎做着举足轻重的工作。相比下来，若要有一个人陪您回去，没人比我更合适。
[charslot(slot = "l", name = "avg_4172_xingzh_1#1$1", focus="l")]
[name="宁茵"]不过话说回来，我本就是琅珆远房遗孤出身，多亏爷爷怜悯，才能在这宁府住了几十年。
[name="宁茵"]如今前往琅珆，也算是回到父母生前故居了。
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", focus="r")]
[name="宁述"]当时你主动要求陪我回乡......是这么想的？
[charslot(slot = "l", name = "avg_4172_xingzh_1#2$1", focus="l")]
[name="宁茵"]......爷爷，我本来是这么想的。
[name="宁茵"]一切都合情合理，我几乎都要说服自己了。
[charslot(slot = "l", name = "avg_4172_xingzh_1#9$1", focus="l")]
[name="宁茵"]但这几日，为了给《百灶食珍录》结尾，我抱着告别的心思，又一次游历了百灶的大街小巷。
[name="宁茵"]......可我发现自己所有的回忆，都与这座城市有关。
[name="宁茵"]我能清楚地记得，院中那棵柿树是哪年栽下的，何时的果子最适合酿酒。
[name="宁茵"]还有街头巷尾的各家餐馆，它们的厨师各自有什么样的脾性，同一道菜又有多少种不同的做法。
[name="宁茵"]我突然发现，比起这座宁府的宅子，这座城市，才更像是我的家。
[charslot(slot = "r", name = "avg_npc_1614_1#5$1", focus="r")]
[name="宁述"]唉......
[name="宁述"]......怪我，怪我没有早些问你的想法。这阵子都是我自作主张了。
[charslot(slot = "l", name = "avg_4172_xingzh_1#9$1", focus="l")]
[name="宁茵"]爷爷，从小到大，您就是我唯一的亲人。
[name="宁茵"]当初我的确想和您回故乡，而如今坚持留在百灶......也是因为爷爷您。
[charslot(slot = "r", name = "avg_npc_1614_1#5$1", focus="r")]
[name="宁述"]因为我？
[charslot(slot = "l", name = "avg_4172_xingzh_1#2$1", focus="l")]
[name="宁茵"]......嗯。
[charslot(slot = "l", name = "avg_4172_xingzh_1#9$1", focus="l")]
[name="宁茵"]我最开始加入太史阁，参与编写史书时，有件事一直让我百思不得其解。
[name="宁茵"]大炎数千年的历史，突然从某个节点开始，推广文字，普及教育。一些研究用的碑文，最早也就能追溯到那个时期。
[name="宁茵"]我想，在那个时代，一定有人推动了这些变革。可我翻阅了几乎所有资料，却找不到一丝线索。
[name="宁茵"]我有一种奇怪的感觉，大炎的史书上，仿佛缺失了一个人。
[charslot(slot = "r", name = "avg_npc_1614_1#6$1", focus="r")]
[name="宁述"]......
[charslot(slot = "l", name = "avg_4172_xingzh_1#9$1", focus="l")]
[name="宁茵"]直到有次，我在一间棋馆遇到了个怪人，他和我讲了关于“那个人”的故事。
[name="宁茵"]我原先以为他只是个故弄玄虚的说书人，可是在后续的研究中，我渐渐发现，他和我说的那些故事，居然一一被印证了。
[name="宁茵"]在他的叙述里，“她”是个温柔的人，为天下苍生，付出了太多心血......可为何这样一个好人，却没法在史书上留下一个名字？
[charslot(slot = "l", name = "avg_4172_xingzh_1#2$1", focus="l")]
[name="宁茵"]那时我才意识到，原来史书从来不是一个容器，而是一把筛子。能留下的故事，少之又少。
[dialog]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_4172_xingzh_1#2$1", focus="l")]
[name="宁茵"]爷爷......我想要记录下您的故事。可是我回过头来，却突然发现，与您相伴几十年，我竟然都没有办法清晰地写下您......
[name="宁茵"]写下您，是一个什么样的人。
[dialog]
[charslot]
宁茵终于抬起头，直视着老人的眼睛。
她期待着老人会回答，回答她没有说出口的疑问。
她等了很久。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="58_g4_baizaomainstreet_n",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_reedmarshes", volume=1, loop=true, channel="r")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[StopSound(channel="r", fadetime=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "l", name = "avg_npc_1631_1#1$1", focus="l")]
[name="大理寺官员A"]有动静！
[dialog]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=1)]
[charslot(slot = "r", name = "avg_npc_1632_1#1$1", posfrom = "200,0", posto = "0,0",duration = 1)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1632_1#1$1", focus="r")]
[name="大理寺官员B"]哪有动静？
[charslot(slot = "l", name = "avg_npc_1631_1#1$1", focus="l")]
[name="大理寺官员A"]嘶......总觉得听到了什么。
[name="大理寺官员A"]可能是这几天见的古怪案子太多了，总觉得不知道什么时候就有人要跑来闹事。
[char

... (全文17837字符)
```

### level_act40side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Background(image="58_g14_yanprison",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1616_1#1$1", duration=1)]
[charslot(slot = "l", name = "avg_npc_1617_1#1$2", duration=1)]
[Delay(time=1.5)]
[charslot(slot = "r", name = "avg_npc_1616_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_1617_1#9$2", focus="l")]
[name="虞澄"]你真是命大。
[name="虞澄"]我在大理寺干了这么多年，进了死狱还有机会活着出来的，你是头一个。
[charslot(slot = "r", name = "avg_npc_1616_1#2$1", focus="r")]
[name="顾筌"]......这样的结果，在下自己也没想到就是了。
[charslot(slot = "l", name = "avg_npc_1617_1#5$2", focus="l")]
[name="虞澄"]哼，你们这些吃墨水的，就是有这个臭毛病。做事只为了一口气，不考虑后果。
[name="虞澄"]查了这么久的案子，这么多年的心血，就换来百珍宴上送上的一道菜，换来一个龙颜大怒。
[charslot(slot = "l", name = "avg_npc_1617_1#3$2", focus="l")]
[name="虞澄"]闹这么一出，落得这个下场，你就满意了？
[charslot(slot = "r", name = "avg_npc_1616_1#2$1", focus="r")]
[name="顾筌"]虞兄教训得是......
[charslot(slot = "r", name = "avg_npc_1616_1#1$1", focus="r")]
[name="顾筌"]可在下所作所为，于忠于义，都问心无愧。
[charslot(slot = "l", name = "avg_npc_1617_1#1$2", focus="l")]
[name="虞澄"]窥见渊鳞者为大不祥，还真是不祥......接下来你如何打算？
[charslot(slot = "r", name = "avg_npc_1616_1#1$1", focus="r")]
[name="顾筌"]调令已经下来，三天后随外交使团，前往维多利亚。
[name="顾筌"]此事过后，我再无可能留在百灶。这样的安排，也是尚书大人争取来的结果。
[charslot(slot = "l", name = "avg_npc_1617_1#7$2", focus="l")]
[name="虞澄"]维多利亚？你这副身子，如何撑得过那段路？
[charslot(slot = "r", name = "avg_npc_1616_1#1$1", focus="r")]
[name="顾筌"]蒙恩逢赦，夫复何求。
[charslot(slot = "r", name = "avg_npc_1616_1#2$1", focus="r")]
[name="顾筌"]何况此次去维多利亚，我也算回家了......
[charslot(slot = "l", name = "avg_npc_1617_1#7$2", focus="l")]
[name="虞澄"]那还能算是家吗？我记得你说，你的妻女都已经亡故了？
[charslot(slot = "r", name = "avg_npc_1616_1#2$1", focus="r")]
[name="顾筌"]嗯......很多年前的事了。
[charslot(slot = "l", name = "avg_npc_1617_1#1$2", focus="l")]
[name="虞澄"]......你觉得就算我信了你这句话，其他人会信？
[charslot(slot = "r", name = "avg_npc_1616_1#2$1", focus="r")]
[name="顾筌"]......
[charslot(slot = "l", name = "avg_npc_1617_1#1$2", focus="l")]
[name="虞澄"]你能记得当年的事，自然也会有别人记得。
[name="虞澄"]这次回去，你知道会有多少双眼睛盯着你？
[charslot(slot = "r", name = "avg_npc_1616_1#1$1", focus="r")]
[name="顾筌"]该怎么做......还请虞兄明示。
[charslot(slot = "l", name = "avg_npc_1617_1#5$2", focus="l")]
[name="虞澄"]借先生人命一用。
[name="虞澄"]你要的清白真相，我给你。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[curtain(direction = 0,fillfrom = 0.2,fillto = 0.2, fadetime=0.01)]
[curtain(direction = 4,fillfrom = 0.2,fillto = 0.2, fadetime=0.01)]
[Background(image="58_g7_forbiddencity", y=-200, xScale=1.1, yFrom=1.1, screenadapt="coverall")]
[focusout(type="bg", id="58_g7_forbiddencity", from=0, to=0.6, duration=0.1, block=false)]
[backgroundTween(xfrom=-60, xTo=60, duration=20, block=false)]
[playMusic(intro="$ghosthunter_intro", key="$ghosthunter_loop", volume=0.6)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_295_1#1$1", posfrom="0,-220", posto="0,-220", afrom=0 ,ato=1, duration=2)]
[Delay(time=4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain]
[focusout(type="bg", id="58_g7_forbiddencity", from=0.6, to=0, duration=0.1, block=false)]
[Background(image="58_g7_forbiddencity", screenadapt="coverall")]
[backgroundTween(yfrom=-70, yTo=0, xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
我第一次来到百灶求学时，印象最深的，是遮天蔽日的高楼和望不到头的万家灯火。
而那灯火的中央，就是禁城。
危楼千尺，高耸入云，目不能视。
老师说，这里进行的每一项决策、下达的每一条政令，都会影响万千百姓的生计。责任之重，重于山岳。
也因此，这里应当是每个学子，一生才学得以施展的地方。
为天地立心，为生民立命。
然而，当我真的站在这里，面对这琼楼玉宇、深宫高墙——
我感到令人透不过气的寒意。
[dialog]
[charslot(slot = "l", name = "avg_npc_295_1#2$1", duration=2)]
[Background(image="58_g7_forbiddencity", screenadapt="coverall", fadetime=2)]
[Delay(time=2)]
[name="梁洵"]......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_298_1#10$1", duration=1.5)]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_npc_298_1#10$1", focus="r")]
[name="宁辞秋"]梁大人来得真早。
[charslot(slot = "l", name = "avg_npc_295_1#9$1", focus="l")]
[name="梁洵"]宁小姐......？
[charslot(slot = "r", name = "avg_npc_298_1#1$1", focus="r")]
[name="宁辞秋"]嗯？梁大人看上去好像很惊讶，是不乐意见到我？
[charslot(slot = "l", name = "avg_npc_295_1#10$1", focus="l")]
[name="梁洵"]怎会......
[charslot(slot = "l", name = "avg_npc_295_1#8$1", focus="l")]
[name="梁洵"]只是没有听说，宁小姐也要来参加百珍宴。
[charslot(slot = "r", name = "avg_npc_298_1#1$1", focus="r")]
[name="宁辞秋"]尚书大人身体抱恙，今年礼部只好由我代他出席了。
[name="宁辞秋"]是临时的决定，没有来得及告诉梁大人。
[charslot(slot = "r", name = "avg_npc_298_1#8$1", focus="r")]
[name="宁辞秋"]不过梁大人赴宴的事，好像也没有打算告诉我呢。
[charslot(slot = "l", name = "avg_npc_295_1#8$1", focus="l")]
[name="梁洵"]我只当是公事......便没有烦扰宁小姐。
[charslot(slot = "r", name = "avg_npc_298_1#1$1", focus="r")]
[name="宁辞秋"]唔......
[charslot(slot = "r", name = "avg_npc_298_1#10$1", focus="r")]
[name="宁辞秋"]突然想起，尚蜀一别，和梁大人也已有大半年未见。这期间，我们书信都没有通过几次。
[charslot(slot = "l", name = "avg_npc_295_1#1$1", focus="l")]
[name="梁洵"]书信难通，又耽于公务，确实疏于联络了。
[charslot(slot = "l", name = "avg_npc_295_1#2$1", focus="l")]
[name="梁洵"]宁小姐怪罪，我无可辩驳......
[charslot(slot = "r", name = "avg_npc_298_1#10$1", focus="r")]
[name="宁辞秋"]哪里会责怪梁大人呢。
[name="宁辞秋"]梁大人担任知府时，心中就放不下家乡的一草一木。如今职责有变，要操心的事只会更多。
[charslot(slot = "r", name = "avg_npc_298_1#8$1", focus="r")]
[name="宁辞秋"]可是不知怎么，只是过了半年，就觉得和梁大人之间好像又变得生分了。
[name="宁辞秋"]有些话，也说不出口了。
[charslot(slot = "l", name = "avg_npc_295_1#7$1", focus="l")]
[name="梁洵"]......
[charslot(slot = "r", name = "avg_npc_29

... (全文30794字符)
```

### level_act40side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_churchfire",volume=0, channel="f", loop=true)]
[SoundVolume(volume=0.2, channel="f",fadetime=2)]
[name="杂乱的声音"]救火！快救火！
[name="杂乱的声音"]有刺客！保护陛下！
[name="杂乱的声音"]卫兵，卫兵——
[dialog]
[bgeffect(name="$eb_smoke_01",layer=1)]
[PlayMusic(intro="$m_bat_sfsui_intro", key="$m_bat_sfsui_loop", volume=0.6)]
[PlaySound(key="$d_avg_audience_chaos", volume=1)]
[Background(image="58_g6_baizhenbanquet",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_soldiersrun", volume=1)]
[charslot(slot = "l", name = "avg_npc_1637_1#1$1", posfrom="200,0", posto="0,0", duration=0.8)]
[Delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1637_1#1$1", posfrom="200,0", posto="0,0", duration=0.8)]
[Delay(time=0.8)]
[name="巡逻的守军"]清理火源，封锁现场！
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1612_1#16$1")]
[name="麟青砚"]当心——
[name="麟青砚"]这个火的来处......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_npc_1612_1#12$1")]
[name="麟青砚"]所有人！别碰杯子里的酒！
[dialog]
[Delay(time=0.8)]
[charslot(slot = "m", name = "avg_npc_1612_1#16$1")]
[name="麟青砚"]（是低温火焰......）
[name="麟青砚"]（是何人......他想做什么？）
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[background]
[charslot]
[curtain(direction = 0,fillfrom = 0.5,fillto = 0.15, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.5,fillto = 0.15, fadetime=0.1)]
[Background(image="58_g6_baizhenbanquet",screenadapt="coverall",xScale=1.2, yScale=1.2, y=-150)]
[backgroundTween(xFrom = 100, xTo = -100, duration=30, block=false)]
[focusout(type="bg", id="58_g6_baizhenbanquet", from=0, to=0.6, duration=0.1, block=false)]
[Delay(time=0.1)]
[PlaySound(key="$d_avg_audience_chaos", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "l", name = "avg_npc_1632_1#1$1", bstart=0.9,bend=1, posfrom = "-200,30", posto = "0,30", duration = 0.8)]
[charslot(slot = "l", action="zoom", poszoom = "0.5,0.5", scale=0.8, duration = 0)]
[Delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1633_1#1$1", bstart=0.9,bend=1, posfrom = "-200,30", posto = "0,30", duration = 0.8)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.8, duration = 0)]
[Delay(time=0.2)]
[charslot(slot = "l", posfrom = "0,30", posto = "200,30", afrom=1, ato=0, duration = 0.8)]
[Delay(time=0.3)]
[charslot(slot = "r", posfrom = "0,30", posto = "200,30", afrom=1, ato=0, duration = 0.8)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1630_1#1$1", bstart=0.9,bend=1, posfrom = "200,30", posto = "0,30", duration = 0.8)]
[charslot(slot = "l", action="zoom", poszoom = "0.5,0.5", scale=0.8, duration = 0)]
[Delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1631_1#1$1", bstart=0.9,bend=1, posfrom = "200,30", posto = "0,30", duration = 0.8)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.8, duration = 0)]
[Delay(time=0.2)]
[charslot(slot = "l", posfrom = "0,30", posto = "-200,30", afrom=1, ato=0, duration = 0.8)]
[Delay(time=0.3)]
[charslot(slot = "r", posfrom = "0,30", posto = "-200,30", afrom=1, ato=0, duration = 0.8)]
[Delay(time=1)]
麟青砚试图让慌乱的人群冷静下来，可她的声音很快就被嘈杂的呼喊声淹没。
在一片混乱中，她看到了一个熟悉的人。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1615_1#1$1", posfrom = "0,-70", posto = "0,-70", duration = 1.5)]
[Delay(time=2)]
只有一个眼神的交会，但麟青砚很清楚。
那人看到了自己，看到了自己方才试图当众做出的出格举动。
但她的目标并不是自己。
[dialog]
[charslot(slot = "m", name = "avg_npc_1615_1#4$1")]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[charslot(slot = "m", name = "avg_npc_1615_1#4$1", posfrom = "0,-70", posto = "200,-70", afrom=1, ato=0, duration = 0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[background]
[curtain]
[focusout(type="bg", id="56_g6_courtsquare_n", from=0.6, to=0, duration=0.1, block=false)]
[Background(image="58_g6_baizhenbanquet",screenadapt="coverall")]
[charslot(slot = "m", name = "avg_npc_1612_1#1$1")]
[Delay(time=0.1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_npc_1612_1#10$1")]
[name="麟青砚"]——！
[charslot(slot = "m", name = "avg_npc_1612_1#16$1")]
[name="麟青砚"]煌......！
[dialog]
[StopSound(channel="f", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[bgeffect]
[charslot]
[Background(image="58_g10_restaurantkitchen",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_crwddiscuss_inside", volume=0, loop=true, channel="cr")]
[SoundVolume(volume=1, channel="cr",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[SoundVolume(volume=0, channel="cr",fadetime=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1619_1#1$1", duration=1.5, isblock=true)]
[name="莫不服"]吵什么？怎么回事？
[charslot(slot = "m", name = "avg_npc_1636_1#1$1")]
[name="资深厨师"]不好了！听说百珍宴的会场，不知道怎么回事，突然起了一阵妖火！
[name="资深厨师"]卫兵已经把会场全部围起来了，不知道现在里面什么情况，也不知道陛下有没有受伤......
[name="资深厨师"]他们说要......中断百珍宴......
[charslot(slot = "m", name = "avg_npc_1619_1#5$1")]
[name="莫不服"]......
[dialog]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(slot = "m", posfrom="0,0", posto="200,0", afrom=1, ato=0, duration=0.8)]
[Delay(time=1.5)]
[charslot]
[charslot(slot = "m", name = "avg_1040_blaze2_1#2$2")]
[name="煌"]麟青砚......！
[dialog]
[charslot]
[PlaySound(key="$d_gen_soldiersrun", volume=1)]
[charslot(slot = "l", name = "avg_npc_1637_1#1$1", posfrom="-200,0", posto="0,0", duration=0.8)]
[Delay(time=0.5)]
[

... (全文32980字符)
```

### level_act40side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Background(image="58_g1_yusrestaurant",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1616_1#9$1", duration=1.5, isblock=true)]
[name="顾筌"]要一份桔红酥......打包带走。
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="小大厨"]哟，来啦。
[name="小大厨"]这次还是寄去维多利亚吗？
[charslot(slot = "m", name = "avg_npc_1616_1#1$1")]
[name="顾筌"]不......不寄了。我马上就要回去了......能不能回去，也不好说就是了。
[multiline(name="顾筌")]这次——
[charslot(slot = "m", action="shake", afrom=1 , ato=1, power=3, times=30, duration=0.3)]
[charslot(slot = "m", name = "avg_npc_1616_1#2$1")]
[multiline(name="顾筌",end=true)]咳咳，咳咳咳！就打包一份点心，路上吃。
[charslot(slot = "m", name = "avg_2026_yu_1#8$1")]
[name="小大厨"]哎哎，怎么咳成了这样。
[charslot(slot = "m", name = "avg_2026_yu_1#2$1")]
[name="小大厨"]我看你还是别吃甜食了，我给你熬一碗枇杷水喝吧。
[charslot(slot = "m", name = "avg_npc_1616_1#2$1")]
[name="顾筌"]没事......没事......不是肺上的毛病。
[charslot(slot = "m", name = "avg_2026_yu_1#2$1")]
[name="小大厨"]不管哪里的病都要注意啊，看过大夫了吗？
[charslot(slot = "m", name = "avg_npc_1616_1#9$1")]
[name="顾筌"]看过，看过了。大夫说，我活不了多久啦。
[name="顾筌"]想吃点啥，也不用忌口了。
[charslot(slot = "m", name = "avg_2026_yu_1#10$1")]
[name="小厨子"]......啊？
[charslot(slot = "m", name = "avg_npc_1616_1#9$1")]
[name="顾筌"]没事，没事......人总有一死嘛。
[name="顾筌"]我要做的事，差不多也都做完了......
[charslot(slot = "m", name = "avg_2026_yu_1#10$1")]
[name="小大厨"]怎......怎么可以有这种念头！
[name="小大厨"]你不是说......你在维多利亚还有家人，她......她们还在等你回家啊。
[charslot(slot = "m", name = "avg_npc_1616_1#9$1")]
[multiline(name="顾筌")]是啊......我也盼着，能再见她们一面，但想必是
[charslot(slot = "m", action="shake", afrom=1 , ato=1, power=3, times=30, duration=0.3)]
[charslot(slot = "m", name = "avg_npc_1616_1#2$1")]
[multiline(name="顾筌",end=true)]咳咳......不能如愿了......
[name="顾筌"]我此生虽然一事无成，但自以为没有愧对过心中那一点理想、道义。
[name="顾筌"]可到头才发现，对她们，我实在亏欠太多......
[charslot(slot = "m", name = "avg_2026_yu_1#11$1")]
[name="小大厨"]嗐......人不就是这样，哪有碟子不磕着碗的？一个人要是打心眼里觉得自己对得起所有人，那才叫没心没肺呢。
[charslot(slot = "m", name = "avg_2026_yu_1#12$1")]
[name="小大厨"]就算这样，你也不能就不打算回家去了呀？
[charslot(slot = "m", name = "avg_npc_1616_1#2$1")]
[name="顾筌"]我想见她们，但是不见，可以让她们活得更好。
[name="顾筌"]人不就这样......总得放下点什么，才能成全点什么。
[name="顾筌"]他们都放下了，我也该放下了......
[dialog]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1616_1#9$1")]
[name="顾筌"]小大厨，这些年多受你照顾，连最后这点大梦呓语，也只能说给你听了。
[charslot(slot = "m", name = "avg_2026_yu_1#12$1")]
[name="小大厨"]那你......
[name="小大厨"]你还有......什么愿望吗？
[charslot(slot = "m", name = "avg_npc_1616_1#1$1")]
[name="顾筌"]我的愿望......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="58_g12_ningfucourtyard",screenadapt="coverall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[PlaySound(key="$d_avg_sweep", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_walkingstick_slow", volume=1)]
[charslot(slot = "m", name = "avg_npc_1614_1#2$1", duration=1.5, isblock=true)]
[name="宁述"]仔细点，都仔细点。看看你扫过的这地，全是灰。
[name="宁述"]那些边边角角的地方都别漏了，脏东西都打扫干净。要搬走了，也别给这屋子后来的主人留麻烦。
[charslot(slot = "m", focus="n")]
[name="宁府管家"]老爷，都这么晚了，您上哪去啊？
[charslot(slot = "m", name = "avg_npc_1614_1#5$1")]
[name="宁述"]没事，别管我，我就出去散散步。
[dialog]
[PlaySound(key="$d_avg_walkingstick_slow", volume=1)]
[charslot(duration=1.5, isblock=true)]
[Delay(time=0.5)]
[name="宁府杂役"]宁大人今天真奇怪。
[name="宁府杂役"]这中秋节，不待在屋里赏月，怎么监督起我们搞卫生了。
[name="宁府管家"]别想了，专心扫你的地。
[name="宁府管家"]今晚月亮把这儿照得这么敞亮，地上的事也给它打扫干净些。
[dialog]
[PlaySound(key="$d_avg_sweep", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_indoor",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(slot = "m", name = "avg_4172_xingzh_1#2$1", posfrom="0,-30", posto="0,0", duration=2, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_4172_xingzh_1#3$1")]
[name="宁茵"]我怎么......在这......
[name="宁茵"]爷爷的书房？
[charslot(slot = "m", focus="n")]
脑袋又昏又沉，自己好像忘记了什么重要的事。
一本陈旧的书册，静静躺在案头。
[charslot(slot = "m", name = "avg_4172_xingzh_1#6$1")]
[name="宁茵"]《炎史一百廿四卷十七策补》......1062年......太史阁里哪里有这一卷？
[name="宁茵"]......爷爷？
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="58_g14_yanprison",screenadapt="coverall")]
[name="监狱卫兵A"]这第五层的监狱多久没关过犯人了，今晚进来的这位，什么来头？
[name="监狱卫兵B"]御前行刺，被禁军亲手逮回来的。
[name="监狱卫兵A"]这么狠——！
[name="监狱卫兵B"]嘘！
[name="监狱卫兵B"]别多想，别多问，看紧就是了。出了半点差错，你我加起来都不够顶。
[dialog]
[PlaySound(key="$d_gen_doorclose", volume=1)]
[PlaySound(key="$d_avg_cavewaterdrop", volume=1, loop=true, channel="a")]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0.2, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
从我回到百灶起，遇上的每件事都像是安排好的。
摆在我面前的一系列线索像是诱饵，最终都指向一个死局。
[dialog]
[SoundVolume(volume=0, channel="a",fadetime=2)]
[PlaySound(key="$d_avg_humanchange", volume=1)]
[delay(time=0.4)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background]
[Image(image="58_i05", screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[name="谌彻"]作案者不仅武功高强，还对大理寺相当熟悉，而且一定与虞澄早有串联......
......
[name="谌彻"]虞澄指名要让你来做审决他时的笔录，这是你现在站在这里的原因，也是我不能让你进一步参与的原因。
[name="谌彻"]不管虞澄有什么谋划，你一定是其中的一环。
[dialog]
[PlaySound(key="$d_avg_humanchange", volume=1)]
[delay(time=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block

... (全文24678字符)
```

### level_act40side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Background(image="58_g9_dalitemple",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1617_1#1$1", duration=1)]
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", duration=1, isblock=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1617_1#1$1", focus="n")]
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", focus="r")]
[name="宁述"]虞澄......你想要的，当年太师案的真相，就是这样。
[name="宁述"]你还有什么想问的？
[charslot(slot = "l", name = "avg_npc_1617_1#5$1", focus="l")]
[name="虞澄"]说了这么多，宁大人倒是只字不提，自己在这一系列事件中的位置。
[name="虞澄"]......你为什么要派人刺杀刑部尚书？
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", focus="r")]
[name="宁述"]虞少卿不是已经有答案了吗？许多年前，你不是指控我在乱局中为求自保，便派人谋害了查案的刑部尚书吗？
[charslot(slot = "l", name = "avg_npc_1617_1#2$1", focus="l")]
[name="虞澄"]宁大人倒不必急着这样抹黑自己。
[name="虞澄"]其实这个问题也困扰了我很久，顾筌时隔十几年再回到百灶，为何偏偏留在你的家中？
[charslot(slot = "l", name = "avg_npc_1617_1#1$1", focus="l")]
[name="虞澄"]直到那一次，我在你家看到那个女孩，我的最后一个问题才得到解答。
[name="虞澄"]顾筌九死一生，还是要回到百灶，不只是为了查明当年真相，也是为了找到，自己遗落在百灶的女儿。
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", focus="r")]
[name="宁述"]看来顾筌告诉你的事，似乎也没有那么多。
[charslot(slot = "l", name = "avg_npc_1617_1#1$1", focus="l")]
[name="虞澄"]是啊，剩下的事，都只是我的猜想，要是有不对的地方，宁大人大可笑话我。
[name="虞澄"]我听说，当年太师背负谋逆之罪自尽后，举国哗然，文武百官纷纷表态与太师割席。可是有一个学宫的学生，竟敢当众上门凭吊太师。
[name="虞澄"]也因此，他撞见了太师被抄家的场面。慌乱中，他只得带走了太师家中一个出生不久的女婴——巧的是，他自己的女儿也刚刚出世。
[name="虞澄"]他不知所措，带着妻子和两个婴儿想要逃离百灶，可他不过是一个势单力薄的书生，没过多久，就被赶来的禁军抓到。
[charslot(slot = "l", name = "avg_npc_1617_1#3$1", focus="l")]
[name="虞澄"]大概是那位禁军心存恻隐，也是有意为太师保留血脉，放了那书生一条生路，带回了那个书生的孩子。
[name="虞澄"]我不知顾筌该作何想，不过当时的他大概也别无选择。
[charslot(slot = "l", name = "avg_npc_1617_1#1$1", focus="l")]
[name="虞澄"]这个孩子落在刑部尚书手中，她的血脉一查便知，可如何处理这个本是局外人的孩子反而成了悬而未决的难题。
[charslot(slot = "l", name = "avg_npc_1617_1#5$1", focus="l")]
[name="虞澄"]就在这个时候，对于刑部尚书过激之举早有不满的宁大人，终于选择铤而走险，派人刺杀了刑部尚书。
[name="虞澄"]太师案牵连甚广，手上沾满了血的刑部尚书遭人报复似乎也在情理之中，时局既定，真龙便默许这一系列风波以这种方式落下帷幕。
[name="虞澄"]那最后没有解决的问题，也只剩下了那个孩子。从结果来看，她既然被宁大人收养，其中过程，似乎也不难猜。但要说目的......
[name="虞澄"]宁大人，我没记错的话，你也在太师门下读过书，对吧？
[charslot(slot = "r", name = "avg_npc_1614_1#6$1", focus="r")]
[name="宁述"]......虞澄啊虞澄，你要是不在大理寺为官，你要是不在这狱中，我真不敢想，你这样的心计，还能做出什么事来。
[name="宁述"]可怕，真可怕......
[charslot(slot = "l", name = "avg_npc_1617_1#3$1", focus="l")]
[name="虞澄"]宁大人过奖了，和顾筌比起来，我不过是个笨人。只是当这大理寺少卿，见过太多人了——见多了，也就懂了。
[name="虞澄"]现在想起来，顾筌在百珍宴上为真龙献上那道菜，近乎求死之举，实际上是已经与真相和解。
[name="虞澄"]而他在临死前，没有告诉我真相，却向我透露了太师遗孤的下落——他是希望我查明真相后，也能选择和解。
[charslot(slot = "l", name = "avg_npc_1617_1#5$1", focus="l")]
[name="虞澄"]......可我和解不了。
[name="虞澄"]我只能用这种方式，找到那些留下的人、你在乎的人，逼你把真相吐出来。
[name="虞澄"]宁大人，细算来，你不能算是个坏人，或许只能算是懦弱......
[name="虞澄"]你大可恨我。
[charslot(slot = "r", name = "avg_npc_1614_1#1$1", focus="r")]
[name="宁述"]......
[name="宁述"]再见到那个孩子一面，也算了了我一桩心愿。
[name="宁述"]我会去见陛下......
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="58_g1_yusrestaurant",screenadapt="coverall")]
[PlayMusic(key="$midautumn", volume=0.6)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_4172_xingzh_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_1040_blaze2_1#11$1", focus="l")]
[name="煌"]你......都知道了？
[charslot(slot = "r", name = "avg_4172_xingzh_1#3$1", focus="r")]
[name="宁茵"]就在刚刚......
[name="宁茵"]我还想问你——
[charslot(slot = "l", name = "avg_1040_blaze2_1#11$1", focus="l")]
[name="煌"]你怎么......还能这么冷静......
[charslot(slot = "r", name = "avg_4172_xingzh_1#2$1", focus="r")]
[name="宁茵"]只是一个在心里藏了很多年的猜想......终于被证实了。
[name="宁茵"]就像扎在手心里的一根刺，拔掉了，流了血，也就好了。
[charslot(slot = "r", name = "avg_4172_xingzh_1#6$1", focus="r")]
[name="宁茵"]你......
[name="宁茵"]你怎么......不说话？
[charslot(slot = "l", name = "avg_1040_blaze2_1#3$1", focus="l")]
[name="煌"]我不知道......怎么会是这样......
[name="煌"]我该难过吗？还是该生气......？
[name="煌"]我不知道......我只是觉得脑子一团糟，心里堵得难受......我不知道这一肚子火到底该向谁发！
[charslot(slot = "r", name = "avg_4172_xingzh_1#9$1", focus="r")]
[name="宁茵"]现在，是不是该我反过来问你了。
[name="宁茵"]煌......你能不能告诉我，顾筌......我的父亲他，是个什么样的人？
[charslot(slot = "l", name = "avg_1040_blaze2_1#10$1", focus="l")]
[name="煌"]他......他就是一个笨蛋，书呆子，说谎精！
[name="煌"]我讨厌说谎！我见过太多谎言，利欲熏心的谎言、懦弱的谎言、狡诈的谎言......
[charslot(slot = "l", name = "avg_1040_blaze2_1#12$1", focus="l")]
[name="煌"]可我真的没见过......有人用一辈子去撒一个谎，还把自己的亲女儿弄丢了，把自己也弄丢了，就为了保护一个毫不相干的人......
[name="煌"]他怎么......能这么笨。
[charslot(slot = "r", name = "avg_4172_xingzh_1#9$1", focus="r")]
[name="宁茵"]我想起，以前在书上看过的一个故事......
[name="宁茵"]从前有一个卫兵，守着江边的一所驿站。有一天，他注意到上游发了洪水，想要跑到上游，去提醒那里的人关闭水闸。
[name="宁茵"]可是他跑到一半，发现江水涨得太急，想要关闸已经来不及了，便想立刻赶回下游的村庄，让那里的人赶快疏散。
[charslot(slot = "r", name = "avg_4172_xingzh_1#2$1", focus="r")]
[name="宁茵"]这个人就这样来回跑着，直到最后他也葬身在这场洪水里，他什么都没能做到，谁也没有救下......
[charslot(slot = "l", name = "avg_1040_blaze2_1#12$1", focus="l")]
[name="煌"]又说这些弯弯绕的......
[charslot(slot = "r", name = "avg_4172_xingzh_1#9$1", focus="r")]
[name="宁茵"]你说......这个人做的事，听起来是不是很熟悉？
[charslot(slot = "l", name = "avg_1040_blaze2_1#10$1", focus="l")]
[name="煌"]我明白！虽然我搞不懂你说的弯弯绕绕的例子，但你在说他的坏话对不对？
[charslot(slot = "l", name = "avg_1040_blaze2_1#12$1", focus="l")]
[name="煌"]他不是个坏人！他只是......唉！
[name="煌"]我知道，你当然有理由怨他，可是如果是他主动抛下了你，他又怎么会花这么多时间回来找你——
[charslot(slot = "r", name = "avg_4172_xingzh_1#9$1", focus="r")]
[name="宁茵"]你怎么反而安慰起我来了......
[name="宁茵"]煌......你是感染者，对吗？
[charslot(slot = "l", name = "avg_1040_blaze2_1#11$1", focus="l")]
[name="煌"]你什么时候知道——
[name="煌"]你这个人——是人精吧！
[charslot(slot = "r", name = "avg_4172_xingzh_1#2$1", focus="r")]
[name="宁茵"]抱歉，我没有什么别的意思......我只是在想，这其实本应该是我的命运......
[charslot(slot = "l", name = "avg_1040_blaze2_1#10$1", focus="l")]
[name="煌"]你在胡说八道什么！
[name="煌"]你做错了什么事？有什么厄运需要你承担？
[name="煌"]我现在活得没什么不好的，有许多伙伴，找到了自己的理想......
[name="煌"]而且，明明你过得很惨吧！一个人生活在深宅大院里，孤零零地长大就开心

... (全文15968字符)
```

### level_act40side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="sn")]
[Background(image="30_ex1_snowmount",screenadapt="coverall", screenadapt="coverall")]
[backgroundTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1.2, yScaleTo=1.2, yFrom=0, yTo=70, duration=4,block=false)]
[bgeffect(name="$eb_lightsnow", layer=1)]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Subtitle(text="离维多利亚已经不远了......", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="又下雪了......她们应该已经换上冬衣了吧。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[delay(time=1)]
[BackgroundTween(yFrom=70, yTo=-80, duration=6, ease="OutQuad", block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=4, block=true)]
[charslot]
[background]
[gridbg(imagegroup="47_g14_skyovercast_L1/47_g14_skyovercast_R1/47_g14_skyovercast_L2/47_g14_skyovercast_R2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720",x=-640,fadetime=1)]
[largebgtween(duration = 25,yFrom = 720, yTo = 360,block = false)]
[Delay(time=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=4, block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Subtitle(text="小时候就像个小火炉，一腔热血，想来是不怕这样一点风雪的。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="百灶没有这样冷的冬天，她说等开春的时候，第一卷书应该已经写成了。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="如此就好......", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="浮生至此，了无挂怀。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[delay(time=1)]
男人脱下官服，仔细折叠整齐，和随身带的书籍放在一处，向东边的方向再三拜首。
他走出了营地。
[dialog]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[StopSound(channel="sn", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[gridbg]
[charslot]
[bgeffect]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$swordtsing3", volume=1)]
[Effect(name="$e_spark_01_large",layer=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.01, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=false)]
[Effect(name="$e_bladeline_01_large",x =116.1, y =0,rox =-60.2, roy =0, roz =16, layer = 2)]
[delay(time=0.4)]
[PlaySound(key="$swordtsing4", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.01, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=false)]
[Effect(name="$e_bladeline_01_large",x =120.1, y =-103.4,rox =-60.2, roy =145, roz =16, layer = 3)]
[delay(time=0.6)]
[PlaySound(key="$fireburst")]
[Effect(name="$e_magic_fire_01",y=-650,x=300,layer = 4,delay=0.2)]
[Effect(name="$e_magic_fire_01",y=-650,x=-300,layer = 5,delay=0.2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.3, r=0.4, g=0.1, b=0.1, fadetime=1.5, block=false)]
[Effect(name="$e_magic_fire_01",y=-550,x=450,layer = 1,delay=0.4)]
[Effect(name="$e_magic_fire_01",y=-550,x=-450,layer = 2,delay=0.4)]
[Effect(name="$e_magic_fire_01",y=-450,x=650,layer = 3,delay=0.6)]
[Effect(name="$e_magic_fire_01",y=-450,x=-650,layer = 4,delay=0.6)]
[PlaySound(key="$d_avg_churchfire",volume=0, channel="f", loop=true)]
[SoundVolume(volume=0.4, channel="f",fadetime=2)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="58_g7_forbiddencity",screenadapt="coverall")]
[bgeffect(name="$eb_burn",layer=1)]
[playMusic(intro="$m_bat_act23side_01_intro", key="$m_bat_act23side_01_loop", volume=0.6)]
[delay(time=0.1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_avg_ftrub", volume=1)]
[charslot(slot = "m", name = "avg_npc_1615_1#8$1", posfrom="600,0", posto="0,-10", duration=1, isblock=true)]
[Delay(time=0.2)]
[charslot(slot = "m", name = "avg_npc_1615_1#1$1", posfrom="0,-10", posto="0,0", afrom=1, ato=1, duration=1.5, isblock=true)]
[Delay(time=0.5)]
[name="“禁军小教头”"]你的火的确变得更烫了。
[name="“禁军小教头”"]感染者，你的源石技艺对自己身体的消耗很大。
[charslot(slot = "m", name = "avg_1040_blaze2_1#9$3")]
[name="煌"]开始怕热了吗？
[name="煌"]呵，这不过是我一个人的血......我清楚，我之所以还能站在这里，是因为已经有太多人流过血。
[charslot(slot = "m", name = "avg_npc_1615_1#1$1")]
[name="“禁军小教头”"]看来你已经知道了很多。
[charslot(slot = "m", name = "avg_1040_blaze2_1#9$3")]
[name="煌"]算不上很多，但最重要的是，我只要知道一件事就够了——
[name="煌"]那些被掩盖掉姓名的人，那些死得不明不白的人......都不能就这样算了。
[charslot(slot = "m", name = "avg_1040_blaze2_1#3$3")]
[name="煌"]说真的，我从来没有想过自己的身世还会牵扯出这么复杂的故事，也没有想过自己还有为感染者而战之外的使命。
[charslot(slot = "m", name = "avg_1040_blaze2_1#9$3")]
[name="煌"]但是我想明白了，道理是一样的。我的血，是为制止我看到的一切不公义的事情而流的。
[charslot(slot = "m", name = "avg_npc_1615_1#1$1")]
[name="“禁军小教头”"]以血引火......感染者，你倒有几分古时义士之风。
[charslot(slot = "m", name = "avg_npc_1615_1#7$1")]
[name="“禁军小教头”"]但现在你一叶障目，最好不要轻易谈什么公正。
[name="“禁军小教头”"]无论如何，我受命要将你带回，断不可再放走你......
[charslot(slot = "m", name = "avg_1040_blaze2_1#9$3")]
[name="煌"]我知道，我知道......我见过你这种人。
[name="煌"]或许不能简单地说你们是坏人，你们只是被训练成这副无血无泪的样子......所以别人的血和泪，你们也不在乎。
[charslot(slot = "m", name = "avg_1040_blaze2_1#10$3")]
[name="煌"]没有关系，我不会和你讲什么道理——你大可以试着拦住我。
[charslot(slot = "m", name = "avg_npc_1615_1#3$1")]
[name="“禁军小教头”"]虽是贼寇乱党......勇气可嘉。
[charslot(slot = "m", name = "avg_npc_1615_1#1$1")]
[name="“禁军小教头”"]当心点，我会留你一命，但未必能保你四肢健全。
[dialog]
[charslot(slot = "m", focus="n")]
[name

... (全文21432字符)
```

### level_act40side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="58_g5_dragonpalace",screenadapt="coverall",xScale=1.2, yScale=1.2, y=-50)]
[backgroundTween(xFrom = 100, xTo = -100, duration=20, block=false)]
[focusout(type="bg", id="58_g5_dragonpalace", from=0, to=1, duration=0.1, block=false)]
[PlaySound(key="$d_avg_drkcludsthdr", volume=0, loop=true, channel="d")]
[SoundVolume(volume=0.3, channel="d",fadetime=2)]
[playMusic(key="$m_sys_bitw_loop", volume=0.6)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[Delay(time=1)]
有谁生来便该担负这一切？
我记得父亲生前常常站在这宫殿高楼上，而兄长就站在他的身侧。 
父亲常常说，水能载舟，亦能覆舟；身处这百尺危楼，亦是临万丈深渊。
[dialog]
[SoundVolume(volume=0.6, channel="d",fadetime=2)]
[Background(image="58_g7_forbiddencity", screenadapt="coverall", xScale=1.15, yScale=1.15, fadetime=4)]
[BackgroundTween(xScaleFrom=1.15, xScaleTo=1, yScaleFrom=1.15, yScaleTo=1, yFrom=-30, yTo=0, duration=30, block=false)]
[delay(time=4)]
他曾久久地望着眼前的城市，或者是远处更大的疆土——
看得见的，和看不见的。
我看到眼前的城市日渐繁荣，他的身子却逐渐佝偻，须发也变得白如霜雪。
我知道，他老了。
我开始听到流传着的各种各样的声音。
“真龙专权独断，多施苛政。若长此以往，大炎有难！”
“请殿下以社稷为重，劝谏真龙，废除弊政，与天下更始！”
人心惶惶。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[background]
[focusout(type="bg", id="58_g7_forbiddencity", from=1, to=0, duration=0.1, block=false)]
我应该去做点什么......
可我该怎么办？我又可以信任谁？
我想到了一个人，一个传说中算无遗策的“人”。
那座古寺早已人去楼空，但我想方设法，寻到了一枚黑子的下落。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[PlaySound(key="$d_gen_thunders_amb", volume=1)]
[SoundVolume(volume=1, channel="d", fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[charslot]
[playsound(key="$d_avg_rainheavy_loop", loop=true, channel="r",volume=0)]
[SoundVolume(volume=0.3, channel="r",fadetime=2)]
[bgeffect(name="$eb_rain_fp",layer=1)]
[gridbg(imagegroup="47_g14_skyovercast_L1/47_g14_skyovercast_R1/47_g14_skyovercast_L2/47_g14_skyovercast_R2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720",x=-640,fadetime=1)]
[largebgtween(duration = 60,yFrom = 360, yTo = 720,block = false)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Subtitle(text="“所求何事？”", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“为炎国，为吾兄，求一破局之法。”", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“我为何要帮你？”", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“你帮我一次，在将来，我也可放你一命。”", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“有趣......年轻的龙，你很有胆识。”", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“破局不难，但凡事必有取舍......你愿意承担这个代价？”", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[PlaySound(key="$d_gen_thunders_amb", volume=1)]
[SoundVolume(volume=1, channel="d", fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[gridbg]
[bgeffect]
[SoundVolume(volume=1, channel="r",fadetime=2)]
[Image(image="cg_rainsplash", screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
有太师相助，兄长最终还是走进了那座禁城，带着赤霄剑。
六军辟易，无人敢挡。
没有人知道，当时禁城中究竟发生了什么。
父亲死了。
兄长消失在所有人的视野中。
......为什么？
从此，就只剩我一个人了？
[dialog]
[StopSound(channel="r", fadetime=2)]
[StopSound(channel="d", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background]
[dialog]
[Image(image="58_i01_1", screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_plateplace", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[name="真龙"]这碗面是何意？
[name="煌"]特意为你做的“长寿面”，不尝尝吗？
[name="真龙"]......为何？
[name="煌"]其实今天才是你的生日吧。
[name="煌"]有个小个子告诉我说，真龙的生日其实是在中秋节后一天，但为了不那么铺张，只好把自己的生日放在中秋节一块过——
[name="煌"]在隐藏生日这一点上，我还挺有共鸣的。
[name="煌"]想了想，一个人就算有至高无上的地位，但连自己何时过生日都身不由己，那也是怪可怜的。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background]
[Image(image="58_i02", screenadapt="coverall", xScale=1.05, yScale=1.05)]
[ImageTween(xScaleFrom=1.05, yScaleFrom=1.05, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[name="真龙"]你......
[name="真龙"]我知道你......
[name="真龙"]你冒着风险，不惜代价，不顾性命也要走到这里......
[name="真龙"]你应该有话要对我说。
[name="煌"]当然。
[name="煌"]虽然是个从来没有见过的人，但自己整个人生都和他息息相关，这种感觉还挺微妙的。
[name="煌"]所以我必须来见你。
[name="煌"]我本来是要在昨天的宴会上给你送一碗长寿面的，但又因为一些乱七八糟的事，计划被打乱了。
[name="煌"]不过现在把这碗面送给你，时机也正好。
[name="煌"]我知道，炎国人的习惯嘛，聊一些要紧事的时候总要在饭桌上。
[name="煌"]尝尝吧，等你吃完，我还有好多问题要问你——
[name="煌"]要你给我一个答案。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Image(image="58_i01_1", screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_pickupchopsticks", volume=1)]
[Image(image="58_i01_2", screenadapt="coverall", fadetime=1)]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[name="余"]咳咳......呸呸呸，桌上怎么这么多灰，都要吃进嘴里了......
[dialog]
[Image(image="58_i03", screenadapt="coverall")]
[bgeffect(name="$eb_tyndall",layer=1)]
[Delay(time=1)]
[PlaySound(key="$d_avg_plateplace", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="望"]你......？
[name="余"]是我。这算什么态度？不乐意见我？
[name="望"]......我没想到，最后一个来阻拦我的，会是你。
[name="余"]拦你干嘛？我可不操这份闲心。
[name="余"]就是自家不让人省心的哥哥好久没回家，留他吃顿饭嘛。
[name="余"]隔了一百年回来，第一件事居然还是到这破庙里来。还嫌在这里关得不够久——难不成你还挺喜欢这的？

... (全文46225字符)
```

### level_act40side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act40side/OR01.mp4")]
```

### level_act40side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_indoor",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(key="$midautumn", volume=0.6)]
[Delay(time=2)]
[playsound(key="$d_avg_chess")]
[Delay(time=1.5)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="先生是说，大炎历史上当真有这么一位奇人？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="是......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="收录书卷，整理文字，推广教育......为何她为天下苍生做了这么多事，却没有人记得她，甚至没有人知道她的名字？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
[playsound(key="$d_avg_penrustle")]
[Delay(time=1.5)]
[Subtitle(text="先生，这是什么字？我似乎从来没有见过？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="并非无人记得“她”，只是她的一字真名，没有被史书记录在册。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这样岂不可惜？明明她的笔写下了炎国悠久的历史，写遍了炎国万里的山河，可史书中没有一页留下了她的名字......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="您说......如果我把这些史书尽数补全，能从中还原出她的模样吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Sticker(id="st1", text="四十年前", x=320,y=340, alignment="center", size=24, delay=0.001, width=700,block = true,duration=1)]
[Sticker(id="st1",duration=1,block = false)]
[delay(time=2)]
[dialog]
[PlaySound(key="$d_gen_thunders_amb",volume=0.4)]
[playsound(key="$d_avg_rainheavy_loop", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.6, channel="bgs",fadetime=2)]
[playsound(key="$d_avg_drkcludsthdr")]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1062年4月21日    谷雨</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playsound(key="$d_avg_shallowswalk", loop=true, channel="a")]
[delay(time=2)]
[StopSound(channel="a", fadetime=2)]
[name="吆喝的伙计"]客人，客人！
[name="吆喝的伙计"]这么大的雨，进来喝壶热茶，避避雨再走吧。
[name="沉稳的男性"]不必了。这场雨眼看着一时半刻也停不下来，还是快些赶路吧。
[name="吆喝的伙计"]哈哈，有人盼着这场雨停下，可还有人盼着它多下一阵哩。
[name="吆喝的伙计"]卖伞的商贩笑开花，就是愁死了赶路人。
[name="沉稳的男性"]阁下说的话倒是有趣......
[name="吆喝的伙计"]客人还是歇歇脚吧。有人托我嘱咐您，前路坑洼不好走，怕您踏错沾湿了鞋。
[name="沉稳的男性"]嗯......？
[dialog]
[PlaySound(key="$dooropenquite")]
[SoundVolume(volume=0.2, channel="bgs",fadetime=2)]
[delay(time=1.5)]
[name="吆喝的伙计"]客人，这边请吧，要见您的那位已经在里面等着了。
[Dialog]
[Background(image="35_g13_yanlivingroom",screenadapt="coverall")]
[playMusic(intro="$mist_intro",key="$mist_loop", volume=0.6)]
[Blocker(a=0.15, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_2024_chyue_1#6$1",duration = 1)]
[delay(time=1.5)]
[name="朔"]尚书大人......好久不见。
[charslot(slot = "left", name = "avg_2024_chyue_1#1$1",focus = "l")]
[name="朔"]不，现在应该称......太傅。
[dialog]
[charslot(slot = "right", name = "avg_npc_301_1#1$1",bstart=0.2,bend=0.5,duration = 1)]
[delay(time=1.5)]
[charslot(slot = "m", focus = "r")]
[name="？？？"]玉门一别，的确很久不见了。
[charslot(slot = "left", name = "avg_2024_chyue_1#1$1",focus = "l")]
[name="朔"]我以为这次回京述职，应该要先见司岁台和兵部才对。
[charslot(slot = "m", focus = "r")]
[name="？？？"]所以我才赶在那之前来见你一面。
[name="？？？"]......陛下驾崩了。
[charslot(slot = "m", focus = "n")]
[dialog]
[PlaySound(key="$d_gen_thunders_amb",volume=0.5)]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_2024_chyue_1#6$1",focus = "l")]
[name="朔"]何时......？
[charslot(slot = "m", focus = "r")]
[name="？？？"]半月前。
[charslot(slot = "left", name = "avg_2024_chyue_1#1$1",focus = "l")]
[name="朔"]我想......如果陛下是寿终正寝，太傅也不会专程来见我。
[charslot(slot = "left", name = "avg_2024_chyue_1#8$1",focus = "l")]
[name="朔"]难道......
[dialog]
[charslot(slot = "m", name = "avg_npc_301_1#1$1",posfrom = "200,0", posto = "200,0")]
[charslot(slot = "r", afrom=1,ato=0,duration = 1.5, focus = "r")]
[delay(time=2.5)]
[charslot(slot = "m", focus = "n")]
坐在阴影中的人伸出手，他的掌心，正躺着一枚黑色云子。
[charslot(slot = "left", name = "avg_2024_chyue_1#6$1",focus = "l")]
[name="朔"]......！
[charslot(slot = "right", name = "avg_npc_301_1#1$1",focus = "r")]
[name="太傅"]六十年前，他逃离了那座古寺，将自己化作一百八十一颗黑子，分散各地，至今下落不明。
[name="太傅"]而就在半月前，司岁台在京城发现了这一枚黑子的踪迹。
[charslot(slot = "left", name = "avg_2024_chyue_1#8$1",focus = "l")]
[name="朔"]......他做了什么？
[charslot(slot = "right", name = "avg_npc_301_1#1$1",focus = "r")]
[name="太傅"]尚不知晓......
[name="太傅"]唯一可以确定的是，他绝无可能进入禁城......应是有人主动见了他。
[name="太傅"]这个人的身份，不方便去查。
[charslot(slot = "left", name = "avg_2024_chyue_1#3$1",focus = "l")]
[name="朔"]他想做的事，按理不该牵扯到旁人才是......
[charslot(slot = "right", name = "avg_npc_301_1#1$1",focus = "r")]
[name="太傅"]今天我本不该见你。可当初那个罪人引起动乱时，毕竟是你亲手将他制服的。
[name="太傅"]......宗师，对此事你知道什么吗？
[charslot(slot = "left", name = "avg_2024_chyue_1#1$1",focus = "l")]
[name="朔"]......并无所知。
[name="朔"]那次事故之后，我也没有再见过他。
[charslot(slot = "right", name = "avg_npc_301_1#1$1",focus = "r")]
[name="太傅"]......
[name="太傅"]那我相信宗师。
[charslot(slot = "left", name = "avg_2024_chyue_1#1$1",focus = "l")]
[name="朔"]需要我做些什么吗？
[charslot(slot = "right", name = "avg_npc_301_1#1$1",focus = "r")]
[name="太傅"]不要停留，即刻返回玉门。
[charslot(slot = "right", name = "avg_npc_301_1#1$1",focus = "r")]
[name="太傅"]乌萨斯动荡不断，玉门守将新旧交替，这个时间，切不可再使人心动荡。
[name="太傅"]司岁台与兵部，我自会处理。你不在局中，我才能以重任相托。
[charslot(slot = "left", name = "avg_2024_chyue_1#1$1",focus = "l")]
[name="朔"]......明白。
[charslot(slot = "right", name = "avg_npc_301_1#1$1",focus = "r")]
[name="太傅"]棋局之事，我会让司岁台暗中继续查下去。
[name="太傅"]特殊时期，宗师不便再露面——你可以当今日没有见过我。
[charslot(slot = "left", name = "avg_2024_chyue_1#6$1",focus = "l")]
[name="朔"]真龙他究竟是......炎武殿下还好吗？
[name="朔"]这个时候，他应该——
[charslot(slot = "right", name = "avg_npc_301_1#2$1",focus = "r")]
[name="太傅"]炎武......
[charslot(slot = "right", name = "avg_npc_301_1#1$1",focus = "r")]
[name="太傅"]陛下去世的那天晚上，是炎武去见了他。
[stopmusic(fadetime=2)]
[PlaySound(key="$d_gen_thunders_amb",volume=0.3)]
[StopSound(channel="bgs", fadetime=2.5)]
[Dialog]
[Blocker(a=1, r=0, g=0,

... (全文13585字符)
```

### level_act40side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[Delay(time=2)]
[Sticker(id="st1", text="让贤？哈哈，要是让父亲听到这句话，又少不了对你一顿责骂。", x=320,y=340, alignment="center", size=24, delay=0,width=700,block = true,duration=1)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1)]
[Sticker(id="st1", text="兄长莫要戏言。论文韬武略，这一众兄弟姐妹有谁比得上你？", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=0.5)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1)]
[Sticker(id="st1", text="等兄长荣登大宝，搬进禁城，那时我也就安心前往天镜阁，当个抄书匠。我照顾好大炎的这些典籍，也算为兄长分忧了。", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=0.5)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1)]
[Sticker(id="st1", text="......", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=0.5)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1.5)]
[Sticker(id="st1", text="兄长，不能再犹豫了！事到如今，只有你能......劝住父亲了。", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=1)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1)]
[Sticker(id="st1", text="太师......不，三公全都支持此举！哪怕将来面对文武百官，哪怕是面对炎国万民，此事也当有公论。", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=0.5)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1)]
[Sticker(id="st1", text="兄长，这是大义之举，你不可再推辞！", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=0.5)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1)]
[Sticker(id="st1", text="......我会和你站在一起。", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=0.5)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1)]
[Sticker(id="st1", text="......", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=0.5)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1.5)]
[Sticker(id="st1", text="为什么是我？为什么要是我？！", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=1)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1)]
[Sticker(id="st1", text="幺弟是因你而死的！那些人都是因你而死的！", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=0.5)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1)]
[Sticker(id="st1", text="你把这一切都甩给我，让我一个人去面对那些口诛笔伐、那些勾心斗角，然后自己就一走了之？！", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=0.5)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1)]
[Sticker(id="st1", text="......", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=0.5)]
[Sticker(id="st1",duration=0.5)]
[Delay(time=1.5)]
[Sticker(id="st1", text="炎武，永远不要回来了。", x=320,y=340, alignment="center", size=24, width=700, delay=0,block = true,duration=1)]
[Sticker(id="st1",duration=1)]
[Delay(time=2)]
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="bg_lungmen_o",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_1645_1#4$1",duration = 1)]
[charslot(slot = "right", name = "char_2005_weiyw_1#1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1645_1#4$1",focus="l")]
[name="文月"]你还这么悠闲，龙门今年中秋节的那么多项活动，你是准备一项也不出席了？
[charslot(slot = "right", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]有什么好参加的，谁还想看我这张老脸出现在电视上？
[name="魏彦吾"]施怀雅家的孩子有想法，交给她办就是，总能办得热热闹闹的。
[charslot(slot = "left", name = "avg_npc_1645_1#4$1",focus="l")]
[name="文月"]......自打从玉门回来，我看你是一天比一天闲。在家的时候就整天坐在书房里吃点心，再不出门走走，晚年发福，也不是没可能的事。
[charslot(slot = "right", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]哈哈......这半年林舸瑞都没怎么出过门了，我连个晨跑的伴都找不到。
[name="魏彦吾"]呵......老了，老了，年轻人有能耐，再多插手就是不识风趣了。
[charslot(slot = "left", name = "avg_npc_1645_1#1$1",focus="l")]
[name="文月"]现在明白这个理了。你要是早这么想，小陈还会走吗？
[charslot(slot = "right", name = "char_2005_weiyw_1#5",focus="r")]
[name="魏彦吾"]......
[charslot(slot = "left", name = "avg_npc_1645_1#1$1",focus="l")]
[name="文月"]有多久了？
[charslot(slot = "right", name = "char_2005_weiyw_1#5",focus="r")]
[name="魏彦吾"]你说什么？
[charslot(slot = "left", name = "avg_npc_1645_1#1$1",focus="l")]
[name="文月"]小陈。走了有多久了？
[charslot(slot = "right", name = "char_2005_weiyw_1#5",focus="r")]
[name="魏彦吾"]五年。
[charslot(slot = "left", name = "avg_npc_1645_1#3$1",focus="l")]
[name="文月"]五年了。
[name="文月"]也不知道她在外面经历了什么，也不知道她的病怎么样了。
[charslot(slot = "right", name = "char_2005_weiyw_1#5",focus="r")]
[name="魏彦吾"]在玉门的时候，我知道她在那。
[name="魏彦吾"]她还好，剑术有长进......算得上好。
[charslot(slot = "left", name = "avg_npc_1645_1#1$1",focus="l")]
[name="文月"]那你就眼看着她又走了？
[charslot(slot = "right", name = "char_2005_weiyw_1#5",focus="r")]
[name="魏彦吾"]她不愿意来见我，也还不愿意回来，勉强不得。
[name="魏彦吾"]放心吧，她的路，总比我们的要长。
[stopmusic(fadetime=2)]
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_038",duration=1)]
[delay(time=1)]
[name="影卫"]魏公，有您的信。
[charslot(slot = "m", name = "char_2005_weiyw_1#2")]
[name="魏彦吾"]......让你们专门来送的信......
[charslot(slot="m",name="avg_npc_038")]
[name="影卫"]从京城寄来的。
[playMusic(intro="$longmenoffice_intro", key="$longmenoffice_loop", volume=0.6)]
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]......
[charslot(slot = "m", name = "avg_npc_1645_1#1$1")]
[name="文月"]送信的人是......？
[charslot(slot="m",name="avg_npc_038")]
[name="影卫"]当今禁军。
[charslot(slot = "m", name = "avg_npc_1645_1#1$1")]
[name="文月"]除了送信，他还说了什么？
[charslot(slot="m",name="avg_npc_038")]
[name="影卫"]真龙请魏公赴京城参加百珍宴，一同赏月。
[charslot(slot = "m", name = "avg_npc_1645_1#1$1")]
[name="文月"]......
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]信留在桌上，你先退下吧。
[charslot(slot="m",name="avg_npc_038")]
[name="影卫"]斗胆问魏公如何打算。
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]我自有安排，你们不必烦忧。
[c

... (全文26159字符)
```

### level_act40side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_bigcaveamb", volume=0, loop=true, channel="big")]
[SoundVolume(volume=1, channel="big",fadetime=2)]
[PlaySound(key="$d_avg_cavewaterdrop", volume=0, loop=true, channel="ca")]
[SoundVolume(volume=1, channel="ca",fadetime=2)]
......今夕何夕？
幽暗的陵墓不见天日，在这片混沌黑暗中，仿佛时间都已静止。
距离这里上一次传来动静已经过去多久？
而这一天，这里多出了一道声音。
[dialog]
[PlaySound(key="$d_avg_gintcrturnhle", volume=1)]
[delay(time=1.5)]
[Subtitle(text="这是哪里......？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="陵墓。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我是谁？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="不知。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......你是谁？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="也不知。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="不过......他们给我起过一个名字。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“岁”。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=2)]
[Image(image="58_i15_1", screenadapt="coverall", xScale=1.05, yScale=1.05, fadetime=0)]
[ImageTween(xScaleFrom=1.05, yScaleFrom=1.05, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[PlaySound(key="$d_avg_gintcrturbrth", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
你留在这里，很久了吗？
[dialog]
[StopSound(channel="ca", fadetime=2)]
[StopSound(channel="big", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=4, block=true)]
[image]
[charslot]
[Background(image="58_g3_baizaomainstreet_d",screenadapt="coverall")]
[playMusic(key="$ouat_loop", volume=0.6)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_fetterfts", volume=1)]
[charslot(slot = "m", name = "avg_npc_1617_1#1$1", duration=1.5, isblock=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1630_1#1$1")]
[name="大理寺官员"]虞先生，上车吧。
[charslot(slot = "m", name = "avg_npc_1617_1#1$1")]
[name="虞澄"]在下还有个不情之请。
[charslot(slot = "m", name = "avg_npc_1617_1#9$1")]
[name="虞澄"]这位兄弟，行个方便。帮我去那马路对面的小饭馆，买碗白饭，讨杯茶水。
[name="虞澄"]要入大狱，也不好空着肚子去。
[charslot(slot = "m", name = "avg_npc_1630_1#1$1")]
[name="大理寺官员"]分内的事，您稍等。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5, isblock=true)]
[Delay(time=1.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1644_1#1$1", duration=1.5, isblock=true)]
[Delay(time=1)]
[name="麟青砚"]要走了？
[charslot(slot = "m", name = "avg_npc_1617_1#1$1")]
[name="虞澄"]判决已下，总不好一直赖在大理寺。
[charslot(slot = "m", name = "avg_npc_1644_1#1$1")]
[name="麟青砚"]我知道......今日专程，来送送您。
[charslot(slot = "m", name = "avg_npc_1617_1#9$1")]
[name="虞澄"]你倒是不怨我。
[charslot(slot = "m", name = "avg_npc_1644_1#4$1")]
[name="麟青砚"]既然已经知晓事情全貌，又何怨之有？
[charslot(slot = "m", name = "avg_npc_1644_1#1$1")]
[name="麟青砚"]要怨，也只能怨您没有早些告诉我。
[charslot(slot = "m", name = "avg_npc_1617_1#9$1")]
[name="虞澄"]若我早些告诉你，恐怕现在你也得戴上这副镣铐。
[name="虞澄"]总要为大理寺留下几个好苗子......
[charslot(slot = "m", name = "avg_npc_1644_1#2$1")]
[name="麟青砚"]对前辈的定罪，我也提出过异议。
[name="麟青砚"]其实，前辈若是觉得量刑不公，大可申请三法司复审——
[charslot(slot = "m", name = "avg_npc_1617_1#5$1")]
[name="虞澄"]难道你觉得，我的所作所为，担不起这十年牢狱？
[charslot(slot = "m", name = "avg_npc_1644_1#2$1")]
[name="麟青砚"]可您做的这一切，终究是为了......
[charslot(slot = "m", name = "avg_npc_1617_1#6$1")]
[name="虞澄"]那又如何？
[name="虞澄"]法就是法，不是“道义”。
[name="虞澄"]今日的虞澄若不服法，将来又会有多少个虞澄，为了他们各自的“道义”，造出多少乱事？
[charslot(slot = "m", name = "avg_npc_1617_1#5$1")]
[name="虞澄"]还说这样的蠢话，不像我带出来的徒弟。
[charslot(slot = "m", name = "avg_npc_1644_1#4$1")]
[name="麟青砚"]晚辈失言......
[charslot(slot = "m", name = "avg_npc_1617_1#1$1")]
[name="虞澄"]当然，要如何让这个“法”，接近更多人心中的道义，那就是你们后来人的事了。
[charslot(slot = "m", name = "avg_npc_1617_1#3$1")]
[name="虞澄"]我会等着......山上的那棵松树还在，我还等着到时候，你把它砍下来给我做棺材。
[charslot(slot = "m", name = "avg_npc_1644_1#11$1")]
[name="麟青砚"]......
[charslot(slot = "m", name = "avg_npc_1617_1#1$1")]
[name="虞澄"]说起来，你今日来给我送行，为何不穿大理寺的官服？
[charslot(slot = "m", name = "avg_npc_1644_1#4$1")]
[name="麟青砚"]我辞官了。
[charslot(slot = "m", name = "avg_npc_1644_1#1$1")]
[name="麟青砚"]一道惊雷，能照亮眼前一瞬，但它断不清世上一切是非黑白与真假善恶。我看不清的事还有很多。
[name="麟青砚"]山上的那棵青松还在，但到底也只是一棵青松而已。登山人在这棵青松上看到了什么，还要看登山人自己的心。
[name="麟青砚"]我会回天师府，再修行一段时间。
[charslot(slot = "m", name = "avg_npc_1617_1#9$1")]
[name="虞澄"]......也好。
[name="虞澄"]想不明白的事，稀里糊涂地做下去，总归做不出名堂。
[charslot(slot = "m", name = "avg_npc_1644_1#2$1")]
[name="麟青砚"]前辈......我最后，还有一事不解。
[name="麟青砚"]您究竟为何......执意要查太师的案子？
[charslot(slot = "m", name = "avg_npc_1617_1#1$1")]
[name="虞澄"]......为什么这么问？
[charslot(slot = "m", name = "avg_npc_1644_1#1$1")]
[name="麟青砚"]我整理了这件案子的前后资料，才发现，为这案子付出一切的，不止顾筌一人。
[name="麟青砚"]顾筌如此尚有动机，可您除了当年奉命厘清大理寺未解决的旧案，与这件案子并无直接关联。
[charslot(slot = "m", name = "avg_npc_1617_1#2$1")]
[name="虞澄"]......
[charslot(slot = "m", name = "avg_npc_1630_1#1$1")]
[name="大理寺官员"]虞先生，给您打的饭。
[name="大理寺官员"]余味居的跑堂，说什么也不肯收钱，还说随时等着您再到店里去做客。
[name="大理寺官员"]奇怪，我也没说是给您打的饭呀......
[charslot(slot = "m", name = "avg_npc_1617_1#2$1")]
[name="虞澄"]我想起几十年前，我第一次在饭馆里遇见顾筌的时候，他跟我说什么“五色令人目盲，五味令人口爽”......
[charslot(slot = "m", name = "avg_npc_1617_1#9$1")]
[name="虞澄"]我后来才想明白，到底还是因为我这人目光短浅，舌头粗钝。
[name="虞澄"]眼中只能见得清白真相，嘴里只咽得下清白滋味。
[dialog]
[charslot]
身穿囚服的男人回过头，望向了大理寺的门匾，望向了藏在门后的决院。
他躬下身，掬起柏树下一抔未化的残雪，撒入碗中，三两口扒完了饭。
[charslot(slot = "m", name = "avg_npc_1617_1#10$1")]
[name="虞澄"]好滋味。
[name="虞澄"]......且去也。
[dialog]
[PlaySound(key="$d_avg_woodenstairfts", volume=1, loop=true, channel="w")]
[StopSound(channel="w", fadetime=2)]
[charslot(duration=2, isblock=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_carriage_loop", volume=1, loop=true, channel="ca")]
[StopSound(channel="ca", fadetime=4)]
[Blocker(a=0, r=0, g=0, b

... (全文23699字符)
```

### training_act40side_01_a

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动40side教学关_a

[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]
[PopupDialog(dialogHead="$avatar_nian")]喂夕，快来搭把手，有东西跑到外面来了！
[PopupDialog(dialogHead="$avatar_dusk")]唉，烦人......
[Battle.Pause(pause=false)]
```

### training_act40side_01_b

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动40side教学关_b
[Battle.SwitchToDefaultUIState]
[Battle.Delay(time=0.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]

[Tutorial(focusX=375, focusY=-130, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
又来了个新家伙？找打！

```

### training_act40side_01_c

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动40side教学关_c
[Battle.SwitchToDefaultUIState]
[Battle.Delay(time=0.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]

[Tutorial(focusX=148, focusY=21, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 没想到还留了<@tu.kw>“饮啄”</>，这味闻着就喜欢。
[Battle.Pause(pause=false)]
```

### training_act40side_01_d

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动40side教学关_d
[Battle.SwitchToDefaultUIState]
[Battle.Delay(time=0.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]

[Tutorial(focusX=-307, focusY=198, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 它好像被<@tu.kw>火灶</>给吸引过去了，到了灶前会被吸入灶内。
[Battle.Pause(pause=false)]
```

### training_act40side_01_e

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动40side教学关_e
[Battle.SwitchToDefaultUIState]
[Battle.Delay(time=0.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]

[Tutorial(focusX=-307, focusY=198, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 嗯？看来马上能开灶看见<@tu.kw>“人间烟火”</>了。
[Battle.Pause(pause=false)]
```

### training_act40side_01_f

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动40side教学关_f
[Battle.SwitchToDefaultUIState]
[Battle.Delay(time=0.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]

[Tutorial(focusX=-94, focusY=119, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_dusk", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 要都像你那样看着<@tu.kw>“饮啄”</>被变成<@tu.kw>“无谓”</>，这饭也就没味了。
[PopupDialog(dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]这东西还会被<@tu.kw>废弃火灶</>吸引啊？不过没事，我们多砸几下，砸到它出气，就能给它变回来。
[Battle.Pause(pause=false)]
```

### training_act40side_01_g

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动40side教学关_g
[Battle.SwitchToDefaultUIState]
[Battle.Delay(time=0.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]

[Tutorial(focusX=278, focusY=-119, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_dusk", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这就是你说的变回来？废弃火灶里的<@tu.kw>“饮露餐风”</>都快出现了......
[Battle.Pause(pause=false)]
```

### training_act40side_01_h

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动40side教学关_h

[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]
[PopupDialog(dialogHead="$avatar_dusk")]一身晦气......反正也伤不了本，你自己处理。
[PopupDialog(dialogHead="$avatar_nian")]小家子气，看我的。
[Battle.Pause(pause=false)]
```

### training_act40side_01_i

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动40side教学关_i
[Battle.SwitchToDefaultUIState]
[Battle.Delay(time=0.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]

[Tutorial(focusX=-307, focusY=198, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这不就成了，开灶！
[Battle.Pause(pause=false)]
```


## 统计

- 总字符数：470782
- 对话行数：3714


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
