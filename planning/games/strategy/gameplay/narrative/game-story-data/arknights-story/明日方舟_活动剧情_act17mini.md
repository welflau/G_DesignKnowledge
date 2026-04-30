# 明日方舟 · 活动剧情 · act17mini（6段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act17mini」完整剧情脚本（6个文件，1624行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act17mini
- 脚本文件数：6

### level_act17mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$calm_loop", volume=0.6)]
[PlaySound(key="$d_avg_amb_forestnight_loop", volume=0, loop=true, channel="e")]
[SoundVolume(volume=0.4, channel="e",fadetime=3.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Subtitle(text="你一定已经厌烦了这样的夜晚。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="湿冷的雾气缠上来，迫近燥热的炉火。灰尘飘浮着，呛人的气味难以驱散。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="难道就这样睡去吗？把一天的劳作存入短暂的梦里，醒来后看到的仍是......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="黑色的城市、黑色的石头、黑色的云，还有那一抹亘古不变的暗红色炉火。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="不想就这样睡去，起码也得给这死寂的夜空，增添些什么。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="比如......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Delay(time=1)]
[Dialog]
[stopmusic(fadetime=2)]
[StopSound(channel="e", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="52_mini02_katzdalesquare_n", screenadapt="coverall", block=true)]
[delay(time=2)]
[PlaySound(key="$d_avg_woodcracle", volume=0, loop=true, channel="a")]
[SoundVolume(volume=0.4, channel="a",fadetime=2)]
[playMusic(key="$comedy_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
9:30 P.M. 天气/阴
卡兹戴尔，生活区
[Dialog]
[charslot(slot="m",name="avg_npc_932_1#1$1",duration=0.7)]
[Delay(time=1)]
[PlaySound(key="$d_avg_wdnguitarpizz",volume=1)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_932_1#1$1",focus="m")]
[name="弹吉他的歌手"]熔炉里燃烧的火光~♪是卡兹戴尔的太阳~♪
[name="弹吉他的歌手"]烘干了小孩的衣裳~♪温暖了战士的胸膛~♪
[charslot(slot="m",name="avg_npc_1163_1#1$1",focus="m")]
[name="温驯的驮兽"]（用蹄子打节拍）
[playsound(key="$d_avg_pcknmgrwl", volume=0.7)]
[name="温驯的驮兽"]哞~哞~
[charslot(slot="m",name="avg_npc_932_1#1$1",focus="m")]
[name="弹吉他的歌手"]熔炉边是卡兹戴尔难得的好地方~♪小气的商人和落败的佣兵纷纷争抢~♪
[charslot(slot="m",name="avg_npc_053",focus="m")]
[name="修整武器的雇佣兵"]你*萨卡兹粗口*骂谁呢！臭唱歌的，成天跟个破喇叭似的叭叭叭。
[name="修整武器的雇佣兵"]我们输给那些维多利亚人了吗？我们那叫——那个词怎么说来着？
[charslot(slot="m",name="avg_npc_932_1#1$1",focus="m")]
[name="弹吉他的歌手"]战士们安慰自己~♪说这只是休养生息~♪
[charslot(slot="m",name="avg_npc_053",focus="m")]
[name="修整武器的雇佣兵"]对！修扬声器。
[Dialog]
[charslot(slot="m",name="avg_npc_932_1#1$1",focus="m")]
[PlaySound(key="$d_avg_wdnguitarstrum",volume=1)]
[Delay(time=1)]
[name="弹吉他的歌手"]但连他的驮兽也知道~♪他的行囊空空~♪分别多年的女儿~♪也嫌~弃~他~♪
[Dialog]
[charslot]
围着节点炉烤火的人们欢乐地笑了起来。
[Dialog]
[musicvolume(volume=0.3, fadetime=1)]
[PlaySound(key="$d_avg_axehitscrape",volume=0.8)]
[CameraShake(duration=0.7, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
忽然一声刺耳的声响传来，笑声戛然而止。
[Dialog]
[charslot(slot="l",name="avg_npc_932_1#1$1",focus="all")]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step",loop=false)]
[stopsound(channel="step",fadetime=2)]
[charslot(slot="r",name="avg_npc_053",posfrom = "70,0", posto = "-50,0",duration=1)]
[Delay(time=1.5)]
[charslot(slot="l",name="avg_npc_932_1#1$1",focus="l")]
[name="弹吉他的歌手"]呃......战士化身愤怒的裂兽......♪伸出、伸出死亡之手......♪有谁能把我救......♪
[name="弹吉他的歌手"]只有......她！她来了——♪♪
[Dialog]
[charslot]
[StopSound(channel="a", fadetime=2)]
[PlaySound(key="$d_avg_openftstprun", volume=1, loop=true, channel="nrun")]
[StopSound(channel="nrun", fadetime=2)]
[charslot(slot="m",name="avg_4146_nymph_1#11$1",duration=1)]
[Delay(time=1.5)]
[musicvolume(volume=0.6, fadetime=1)]
[charslot(slot="m",name="avg_4146_nymph_1#11$1",focus="m")]
[name="焦头烂额的女孩"]再过五分钟仪式就要开始了，你们还在这里打闹！这一堆乐谱也还放在警戒线里，破吉他，快把你的这一大堆东西从熔炉旁边挪开！
[name="焦头烂额的女孩"]还有你，铁大头，离警戒线远一点，你要等着你的驮兽战友的毛被烤焦吗？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_932_1#1$1",focus="all")]
[charslot(slot="r",name="avg_npc_053",posfrom = "-50,0", posto = "-50,0",duration=0)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_clothmovementsp",volume=0.8)]
[CameraShake(duration=0.8, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown2", volume=1,delay=0.2)]
[charslot(slot="l",afrom=1,ato=0,duration=0.7,focus="all")]
[Delay(time=1)]
[Dialog]
[charslot]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_053",focus="m")]
[name="修整武器的雇佣兵"]哦，是小妮芙，你也来凑热闹。
[name="修整武器的雇佣兵"]放心，这小破炉子能迸出几个火星子，我不比你清楚？慌什么。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[charslot(slot="m",name="avg_npc_932_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_932_1#1$1",focus="m")]
[name="弹吉他的歌手"]我的脑袋险些粉碎~♪而我此时想起~♪我起初只是想为熔炉中的魂灵~♪写下一首送别的歌~♪
[charslot(slot="m",name="avg_npc_1163_1#1$1",focus="m")]
[name="温驯的驮兽"]（安详地烤火）
[charslot(slot="m",name="avg_4146_nymph_1#12$1",focus="m")]
[name="妮芙"]就算你三十几岁了，也别倚老卖老。过去是过去，现在是现在。熔炉原来是靠燃烧死魂灵供能，现在马上就要换成新能源了。
[name="妮芙"]埃米讲过，今晚是将熔炉里的死魂灵请出来的关键仪式，万一出了什么意外，熔炉“轰”的一下——
[Dialog]
[charslot(slot="m",name="avg_4146_nymph_1#12$1",focus="n")]
[PlaySound(key="$d_avg_ironhitone",volume=1)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4146_nymph_1#12$1",focus="m")]
[name="妮芙"]铁大头！你还听不听人讲话！
[charslot(slot="m",name="avg_npc_053",focus="m")]
[name="修整武器的雇佣兵"]我在外头见过的危险多了去了！那帮菲林的城防炮都没燎着这些家伙的毛，还怕这点火星子吗！
[name="修整武器的雇佣兵"]趁今晚炉子温度正好，把我的这把刀重新锻一下才是正事。
[charslot(slot="m",name="avg_npc_1163_1#1$1",focus="m")]
[name="烤火的驮兽"]（惬意地哼叫）
[charslot(slot="m",name="avg_4146_nymph_1#11$1",focus="m")]
[name="妮芙"]你们......怎么还是不听劝......
[Dialog]
[PlaySound(key="$d_avg_crwlstps", volume=1,loop="false", channel="nf")]
[stopsound(fadetime=3, channel="nf")]
[CameraShake(duration=2, xstrength=15, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=0.5)]
[name="妮芙"]那我就、自己、动手！
[charslot(slot="m",name="avg_npc_053",focus="m")]
[name="修整武器

... (全文51340字符)
```

### level_act17mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="49_g4_kazdelstreet_shabby",screenadapt="showall")]
[cameraEffect(effect="Grayscale", keep=true, amount=0.7, fadetime=0)]
[Delay(time=1)]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=0, loop=true, channel="a")]
[SoundVolume(volume=0.4, channel="a",fadetime=3)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="贫民窟的穷小子"]我来找你，是来给你们这些上面人解决麻烦的。我身后这个街区，放眼整个卡兹戴尔，找不出比它更破烂的了吧？
[name="贫民窟的穷小子"]我手头有一支顶好的施工队，他们愿意参与节点炉的建设。你想想，只要通了能源，这个街区的其他产业很快就能发展起来。
[name="贫民窟的穷小子"]只要街区有产业，大家有活儿干有饭吃，就不会有人想闹事了。
[Dialog]
[charslot(slot = "m", name = "avg_npc_869_1#1$1",focus="m")]
[name="埃芒加德"]哦？这么有底气？那你想问我要什么？
[Dialog]
[charslot]
[name="贫民窟的穷小子"]铺管道必要的钢材，一点也不差地、整整齐齐地摞在街区正中央，也可以派几个人盯着。
[name="贫民窟的穷小子"]相信我，三个月后，我会让你看到一片全新的街区。
[Dialog]
[SoundVolume(volume=0, channel="a",fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="49_g4_kazdelstreet_shabby", screenadapt="coverall", block=true)]
[delay(time=1)]
[SoundVolume(volume=0.4, channel="a",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="贫民窟的穷小子"]看到那边看守钢材的守卫了没？这下你信了吧，造节点炉的事儿是上面的人指派的。给上面人办事，好处少不了你的。
[Dialog]
[charslot(slot = "m", name = "avg_npc_933_1#1$1",focus="m")]
[name="断角帮老大"]哦。所以呢？
[Dialog]
[charslot]
[name="贫民窟的穷小子"]我要粮食，足够我那支顶好的施工队的人吃的粮食——我知道你们断角帮存了很多。
[name="贫民窟的穷小子"]你们备好粮食，就堆在那边的仓库里，地方应该够用。
[name="贫民窟的穷小子"]相信我，我给你们提供的是一笔划算买卖。
[Dialog]
[SoundVolume(volume=0, channel="a",fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="49_g4_kazdelstreet_shabby", screenadapt="coverall", block=true)]
[delay(time=1)]
[SoundVolume(volume=0.4, channel="a",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="贫民窟的穷小子"]看到我仓库里的粮食了吗？来造炉子的，每人每天都能领一份，总比你们在街上打砸抢来得好。谁都不想把脑袋别裤腰带上过活。
[Dialog]
[charslot(slot = "m", name = "avg_npc_054",focus="m")]
[name="凶悍的雇佣兵"]小子，你还挺有胆量。你是要雇我们佣兵帮你干活？
[Dialog]
[charslot]
[name="贫民窟的穷小子"]对。你们高大结实，又坚强又仗义，绝对会是一支顶好的施工队。
[name="贫民窟的穷小子"]只要你们都听我的，我可以保证你们都过上好日子——至少比现在要好。
[Dialog]
[stopmusic(fadetime=2)]
[stopSound(channel="a", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(screenadapt="showall", image="52_mini01_katzdalesquare_d",x=250, y=0, xScale=1.4, yScale=1.4)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
7:40 A.M.  天气/阴 
[Dialog]
[charslot(slot = "l", name = "avg_npc_932_1#1$1",duration=0.7)]
[charslot(slot = "r", name = "avg_npc_054",duration=0.7)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="干瘦的萨卡兹男性"]早啊，大脑袋！来取衣服啊？你再晚来一会儿，估计领口都要烤焦了。
[charslot(slot = "r", name = "avg_npc_054",focus="r")]
[name="归乡雇佣兵"]你敢再叫一声大脑袋试试？还有，把你捡回来的那些破烂都收拾好，别*萨卡兹粗口*堆在我门口！
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="干瘦的萨卡兹男性"]嘿嘿，就放一晚上，等会儿我就拉去卖给烧锅炉的，不会碍事的。
[name="干瘦的萨卡兹男性"]要是放我家里，早被那些混混抢走了。您不一样啊，这几条街上，谁都不敢动您的货。
[charslot(slot = "r", name = "avg_npc_054",focus="r")]
[name="归乡雇佣兵"]你今天话挺多啊，不用去工地上抢活儿干了？
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="干瘦的萨卡兹男性"]还去啥啊，昨晚上那么响亮的动静，你没听到？这——么大一颗石头，就正好砸在工地上！
[name="干瘦的萨卡兹男性"]现在去上工，还得先把那颗大石头运走，整平地面......拿一样的粮食花几倍力气，傻子才去呢！对了，你这么早出门干嘛去？
[charslot(slot = "r", name = "avg_npc_054",focus="r")]
[name="归乡雇佣兵"]......
[name="归乡雇佣兵"]没事，我溜达会儿。
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="干瘦的萨卡兹男性"]哦，那你可别往南边儿底下去，那边正乱呢。
[name="干瘦的萨卡兹男性"]我早上去割铜线的时候听说，好像有个铁疙瘩砸下来，把谁家的屋顶给砸穿了。那人还没来得及乐呵两声，断角帮的人就找上门来了！
[name="干瘦的萨卡兹男性"]现在好几个帮派都聚在一起，打算把铁疙瘩分了换成粮食。可怎么分都不满意，眼见就要打起来了。
[charslot(slot = "r", name = "avg_npc_054",focus="r")]
[name="归乡雇佣兵"]铁疙瘩？这么值钱吗？
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="干瘦的萨卡兹男性"]啥时候异铁不值钱了，咱们也甭活了。
[name="干瘦的萨卡兹男性"]断角帮的那些愣头青为了半截黑砖都能掏刀子，要不是顾问老大镇着他们，估计早都把人家房子拆了。
[charslot(slot = "r", name = "avg_npc_054",focus="r")]
[name="归乡雇佣兵"]顾问老大在，这些小混混闹不起来的。
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="干瘦的萨卡兹男性"]反正我可劝过你了。还有，往前边那儿也绕着走，瞧见那两位了吗？
[charslot(slot = "r", name = "avg_npc_054",focus="r")]
[name="归乡雇佣兵"]哪里？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)] 
[charslot]
[Background(screenadapt="showall", image="52_mini01_katzdalesquare_d",x=-250, y=0, xScale=1.4, yScale=1.4)]
[charslot(slot="l",name="avg_4146_nymph_1#1$1")]
[charslot(slot="r",name="avg_npc_869_1#1$1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1.5, block=true)]
[Delay(time=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)] 
[charslot]
[Background(screenadapt="showall", image="52_mini01_katzdalesquare_d",x=250, y=0, xScale=1.4, yScale=1.4)]
[charslot(slot = "l", name = "avg_npc_932_1#1$1")]
[charslot(slot = "r", name = "avg_npc_054")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1.5, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="干瘦的萨卡兹男性"]小妮芙你见过。旁边那个面生些，不过应该是位巫妖。
[name="干瘦的萨卡兹男性"]前些日子，你还没回卡兹戴尔的时候，就是他们在这儿管事。
[charslot(slot = "r", name = "avg_npc_054",focus="r")]
[name="归乡雇佣兵"]巫妖？他们跑这来做什么，不怕把漂亮鞋子踩脏了？
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="干瘦的萨卡兹男性"]也不能这么说，兴许是小妮芙的朋友呢，有说有笑的。
[name="干瘦的萨卡兹男性"]嘿！烧锅炉的终于来了！大脑袋，借你推车用一下啊。
[charslot(slot = "r", name = "avg_npc_054",focus="r")]
[name="归乡雇佣兵"]叫啥？
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="干瘦的萨卡兹男性"]大、大哥！老大！嘿嘿，您慢慢溜达着，我先去拉破烂了。
[charslot(slot = "r", name = "avg_npc_054",focus="r")]
[name="

... (全文41268字符)
```

### level_act17mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="52_mini01_katzdalesquare_d",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1454_1#1$1",duration=0.7)]
[charslot(slot = "l", name = "avg_npc_932_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="干瘦的萨卡兹男性"]我这些和别人的不一样，你看！我这都是精挑细选过的，别人的是烟花碴子，我这可是烟花芯子！怎么能是一个价格呢？
[charslot(slot = "r", name = "avg_npc_1454_1#1$1",focus="r")]
[name="节点炉看守人"]没啥区别。最多三个。
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="干瘦的萨卡兹男性"]......这样吧，我这兜里还有一把，这些可都是纯纯的异铁，一点源石杂质都没有。算上这些，再把你贴的饼子分我一张呗。
[charslot(slot = "r", name = "avg_npc_1454_1#1$1",focus="r")]
[name="节点炉看守人"]不要。不给。
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="干瘦的萨卡兹男性"]你这倔老头子，烧个锅炉还真把自己当个人物了？三个烤红薯就想换我这三大筐异铁疙瘩，你把良心也扔进炉子里烧了是吧，啊？
[charslot(slot = "r", name = "avg_npc_1454_1#1$1",focus="r")]
[name="节点炉看守人"]老子的贴饼可都是纯白面的，你拿一把炉渣就想换？赶紧滚！下一个，来。
[name="节点炉看守人"]两筐？先上秤。嗯，两个烤红薯，自己去炉灰里扒拉。别多拿啊，我都有数的。
[name="节点炉看守人"]豆芽菜，不是让你滚吗，还站这干嘛？挡着后面的人了。
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="豆芽菜"]行，老东西。这城里又不止你一个管炉子的，我还不信没个识货的。
[charslot(slot = "r", name = "avg_npc_1454_1#1$1",focus="r")]
[name="节点炉看守人"]你可真是不识好歹，你要是能在别人那换到三个烤红薯，我贴的这一炉子面饼白送你都成！
[charslot(slot = "l", name = "avg_npc_932_1#1$1",focus="l")]
[name="豆芽菜"]大家都听见了啊，你可不准反悔！
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="49_g2_kazdelstreet_d",screenadapt="showall")]
[delay(time=1)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_932_1#1$1",focus="m")]
[name="豆芽菜"]*萨卡兹粗口*，一个比一个黑！这边管炉子的居然都只肯给两个，甚至还是去年窖子里剩下的，到底还让不让人活了？
[name="豆芽菜"]捡了一晚上，腰都要累断了，总不能连一天的饱饭都换不到吧......反正不可能再回老东西那儿去了，要不还是往东边的集市去一趟？
[name="豆芽菜"]但从这里往东边走的话，就绕不开那几间棚屋了......
[Dialog]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_932_1#1$1",focus="m")]
[name="豆芽菜"]按那几个老头子说的，打仗的时候，都把残缺不全的尸体扔在那里，到现在还有无法回归众魂的怨灵......
[name="豆芽菜"]不对，不对不对！那些小屁孩怕这种传说故事就算了，我怎么能怕呢？笑话！
[name="豆芽菜"]不就是一条黑巷子和几间没人住的棚屋吗？
[Dialog]
[charslot]
下定决心后，简陋的手推车便吱呀呀地被推动起来，绕过杂乱的柴堆和路面上积水的深坑，向曲折狭窄的小巷尽头闯去。
一道暗色的分界线将前路割开，再往前就是被魂灵熔炉的阴影覆盖的区域。干瘦的男人减慢了脚步，又脱下外套盖在推车上。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="49_g2_kazdelstreet_d",screenadapt="showall")]
[charslot(slot = "m", name = "avg_npc_932_1#1$1",focus="m")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_932_1#1$1",focus="m")]
[name="豆芽菜"]（咽口水）转过这个拐角就能看见了......
[name="豆芽菜"]哈，这鬼天气，都大中午了还这么冷！冻得老子打颤！
[Dialog]
[charslot(slot = "m", name = "avg_npc_932_1#1$1",focus="n")]
[PlaySound(key="$d_avg_woodenladder", volume=1)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_932_1#1$1",focus="m")]
[name="豆芽菜"]什么动静？谁！谁在说话？！
[Dialog]
[charslot(slot = "m", name = "avg_npc_932_1#1$1",focus="n")]
[PlaySound(key="$d_avg_sundries",volume=0.7)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_932_1#1$1",focus="m")]
[name="豆芽菜"]这里不是早就没人敢住了吗......这又是什么动静，磨刀？剁肉？
[name="豆芽菜"]*萨卡兹粗口*！大不了就闭着眼睛冲过去......
[Dialog]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(slot="m",name="avg_npc_932_1#1$1",posfrom="0,0",posto="-150,0",afrom=1,ato=0,duration=0.7,isblock=false)]
[delay(time=1)]
[PlaySound(key="$gavel1", volume=1)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[charslot]
[charslot(slot="m",name="avg_4151_tinman_1#1$1",bstart=0.2,bend=0.7,duration=1)]
[delay(time=2)]
[charslot]
在他即将钻出大熔炉的阴影时，推车却猛然撞上了一堵墙。
不，那似乎并不是墙，而是......他的目光上移，从灰白色的金属上滑过，与一双猩红的眼睛对视。
[Dialog]
[charslot(slot="l",name="avg_4151_tinman_1#1$1",bstart=0.2,bend=0.7,duration=1)]
[charslot(slot="r",name="avg_npc_932_1#1$1",duration=1)]
[delay(time=1)]
[charslot(slot="l",name="avg_4151_tinman_1#1$1",bstart=0.2,bend=0.7,focus="l")]
[name="？？？"]......
[charslot(slot = "r", name = "avg_npc_932_1#1$1",focus="r")]
[name="豆芽菜"]鬼啊！！
[charslot(slot="l",name="avg_4151_tinman_1#10$1",focus="l")]
[name="奇怪的路人"]不好意思，我好像迷路了。你没事吧？
[charslot(slot = "r", name = "avg_npc_932_1#1$1",focus="r")]
[name="豆芽菜"]你眼睛怎么长的！我这么大个手推车你都......你、你这身上......
[name="豆芽菜"]对不起，怪我没长眼，我这就走。
[Dialog]
[PlaySound(key="$d_avg_runstop", volume=1)]
[PlaySound(key="$bodyfalldown2", volume=1,delay=0.5)]
[charslot(slot = "l", posfrom="0,0", posto="20,0",duration=1)]
[charslot(slot = "r", posfrom="0,0", posto="-100,0", duration=0.5)]
[delay(time=0.3)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.2)]
[charslot(slot = "r", name = "avg_npc_932_1#1$1",focus="r")]
[name="豆芽菜"]不是，你......你站那儿别动！
[Dialog]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(slot = "r", posfrom="-100,0", posto="-600,0", duration=1.5)]
[charslot(slot="r",afrom=1,ato=0,duration=1)]
[delay(time=1.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="49_g2_kazdelstreet_d",screenadapt="showall")]
[charslot(slot = "m", name = "avg_npc_932_1#1$1",focus="m")]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_932_1#1$1",focus="m")]
[name="豆芽菜"]什么破天气，日头都没见到还这么热！害老子出了一脑袋汗！
[name="豆芽菜"]最近城里真是，什么稀奇古怪的人都有......
[name="豆芽菜"]咦，怎么又是你？你不是往西边儿走了吗？
[Dialog]
[charslot]
[stopmusic(fadetime=1)]
[delay(time=1)]
街角的阴影中，一双通红的眼睛慢慢升起，慢慢地高过了萨卡兹的头顶，高过了两侧的棚顶，高过了枯死的树木。
那具沉重的身躯慢慢地转动，迈出了熔炉的阴影。腐烂的麻布无法

... (全文37018字符)
```

### level_act17mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="52_mini01_katzdalesquare_d",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_4146_nymph_1#13$1",duration=0.7)]
[Delay(time=1)]
[PlaySound(key="$d_gen_transmissionget",volume=1)]
[CharacterCutin(widgetID="1", name="avg_npc_869_1#1$1", style="cutin",fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=200, width=200, block=true)]
[charslot(slot = "l", name = "avg_4146_nymph_1#13$1",focus="l")]
[name="妮芙"]怎么了，埃米？
[charslot(slot = "l", name = "avg_4146_nymph_1#13$1",focus="n")]
[name="埃芒加德"]已经过了两天了，有什么新进展吗？
[charslot(slot = "l", name = "avg_4146_nymph_1#1$1",focus="l")]
[name="妮芙"]我找到好几个了！嗯，其实也就两个......不过你放心，应该很快就能结束！怎么了？
[charslot(slot = "l", name = "avg_4146_nymph_1#1$1",focus="n")]
[name="埃芒加德"]没事，也就是老家伙突然想起来关心这件事，过来催我几句。
[name="埃芒加德"]本来以为这些碎片会把卡兹戴尔搞得天翻地覆的，现在看来还好。
[name="埃芒加德"]没人因为这件事去敲军事委员会的门，我们也没检测出来什么异常。
[charslot(slot = "l", name = "avg_4146_nymph_1#9$1",focus="l")]
[name="妮芙"]（小声）因为事情都被我碰上了啊，哈哈......
[charslot(slot = "l", name = "avg_4146_nymph_1#9$1",focus="n")]
[name="埃芒加德"]总之，你按照自己的节奏来就行。
[charslot(slot = "l", name = "avg_4146_nymph_1#13$1",focus="l")]
[name="妮芙"]就这样？
[charslot(slot = "l", name = "avg_4146_nymph_1#13$1",focus="n")]
[name="埃芒加德"]嗯，就这样，记得安全第一，遇上搞不定的事记得来找我。
[charslot(slot = "l", name = "avg_4146_nymph_1#3$1",focus="l")]
[name="妮芙"]嗯，好嘞，谢谢埃米~
[Dialog]
[PlaySound(key="$transmission",volume=0.6)]
[CharacterCutin(widgetID="1",fadetime=0.5,block=true)]
[delay(time=1)]
[charslot]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]埃米做事还是这么周到，我也得抓紧了。
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]想好吃什么没有？
[charslot(slot = "m", name = "avg_4146_nymph_1#17$1",focus="m")]
[name="妮芙"]欸？哦，对不起，我这就挑。
[charslot(slot = "m", name = "avg_4146_nymph_1#14$1",focus="m")]
[name="妮芙"]唔......
[charslot(slot = "m", name = "avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]那就尝尝这个吧。
[name="妮芙"]这是什么新食物吗？
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]还是烤面团啊，你又不是第一次在我这儿吃。
[Dialog]
[charslot(slot = "m", name = "avg_4146_nymph_1#16$1",focus="m")]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]但是，是不是变好吃了？
[name="妮芙"]比以前有嚼劲了，还有点......甜味？
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]是吗？可能是进的料比以前好了吧。
[name="街边摊贩"]最近回来的人越来越多，有渠道买点便宜的好料，面团也就更香了。
[charslot(slot = "m", name = "avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]那，以后还需要我去帮忙砍价吗？
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]不用了，之前一个来我这里吃东西的雇佣兵，帮我联络了一家更好的供应商，他们价格挺合适的，也好交流，就不麻烦你了。
[charslot(slot = "m", name = "avg_4146_nymph_1#9$1",focus="m")]
[name="妮芙"]那可太好了！再这样下去您这里是不是可以做维多利亚那儿的白面包了呢？
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]你个贪吃鬼，白面包有什么好吃的，下次找个机会，过来吃烤兽肉。
[charslot(slot = "m", name = "avg_4146_nymph_1#3$1",focus="m")]
[name="妮芙"]真的吗？！烤兽肉......
[Dialog]
[playsound(key="$d_avg_hungry", volume=1)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]能再给我三个烤面团吗？我想带走路上吃。
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]行，稍等会，我给你拿刚出炉的。
[charslot(slot = "m", name = "avg_4146_nymph_1#9$1",focus="m")]
[name="妮芙"]嘿嘿，谢谢您。
[charslot(slot = "m", name = "avg_4146_nymph_1#3$1",focus="m")]
[name="妮芙"]哼哼~这两天忙了这么多事，也该犒劳一下自己了。
[name="妮芙"]呼......没有什么比美美地填饱肚子更幸福的事了——
[musicvolume(volume=0.3, fadetime=1)]
[Dialog]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4146_nymph_1#7$1",focus="m")]
[name="妮芙"]嗯？
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1453_1#1$1",duration=1)]
[delay(time=2.5)]
[charslot]
妮芙一眼就瞥见了那个萨卡兹。当然，她并不是故意的。
无论是谁，只要路过这里，都会被那道身影吸引。
拄着手杖，戴着礼帽，昂着头颅，一动不动地站在那里。
在一个大部分人都蓬头垢面、衣冠不整的地方，这样的人实在是太稀奇了。
[Dialog]
[musicvolume(volume=0.6, fadetime=1)]
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]给，你要的面团。
[charslot(slot = "m", name = "avg_4146_nymph_1#13$1",focus="m")]
[name="妮芙"]哦，好，谢谢......
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]第一次见她吗？
[charslot(slot = "m", name = "avg_4146_nymph_1#17$1",focus="m")]
[name="妮芙"]我以前好像没见过这样的......人。
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]她也不是一开始就这样的，不知道什么时候发了疯，离开卡兹戴尔出去闯荡了一阵，回来以后就变这样了。
[charslot(slot = "m", name = "avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]哦......话是这么说，但是，很好看呀。
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]好看有什么用，往那一站就是一天，啥都卖不出去。
[charslot(slot = "m", name = "avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]她也卖烤面团吗？
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]那倒不是。她会用那些废料做首饰。
[name="街边摊贩"]还有些奇怪的玩意，像是透明玻璃巫术球，里面放个卡兹戴尔的模型，还有印着奇怪图案的杯子——全都又贵又容易碎，傻子才买。
[name="街边摊贩"]听说还有什么摆件和雕塑，那些就更属于没人买的玩意了。平常用不上，卖得还那么贵，也不知道她是怎么想的。
[name="街边摊贩"]周边那些和她关系稍微好点儿的都劝过她，但她就是听不进去。
[charslot(slot = "m", name = "avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]啊哈哈......
[name="妮芙"]每天能看到一个穿得漂漂亮亮的人在街上，总归也不是件坏事嘛。
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]只是希望她能赚点粮食养活自己......要是饿死在我这烤面团的摊位前面，那岂不是闹笑话了吗？
[charslot(slot = "m", name = "avg_4146_nymph_1#9$1",focus="m")]
[name="妮芙"]唔，您说的也有些道理......我该走了，回头见~
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="街边摊贩"]再见小妮芙，下次多介绍点朋友来光顾我这小摊啊。
[charslot(slot = "m", name = "avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]忘不了的，拜拜~
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="52_mini01_katzdalesquare_d",screenadapt="showall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]呼......吃饱喝足，该继续干活了。
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1453_1#1$1",durat

... (全文44967字符)
```

### level_act17mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_snowstormflp", volume=0.6, loop=true, channel="wind")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[Delay(time=1.5)]
[name="？？？"]这是......哪里？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background(image="40_g2_glacier",screenadapt="showall")]
[delay(time=1)]
[playMusic(key="$formal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="妮芙"]喂——
[name="朦胧的回音"]喂——
[name="妮芙"]我是......怎么到这儿来的？
[name="妮芙"]我的手......
[Dialog]
[charslot]
手上绽开淡粉色的纹路。血液结成了冰晶，挤开了皮肤，沿着那些纹路一点点钻出来。
刺骨的风刮过。血与肉片片剥落，像花瓣一样被风卷去，只剩下——
[name="妮芙"]好痛......为什么......
[Dialog]
[stopmusic(fadetime=2)]
[stopSound(channel="wind", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="showall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
半小时前
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="52_mini01_katzdalesquare_d",screenadapt="showall")]
[delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_4146_nymph_1#10$1",duration=0.7)]
[Delay(time=1)]
[PlaySound(key="$d_gen_transmissionget",volume=1)]
[CharacterCutin(widgetID="1", name="avg_npc_869_1#6$1", style="cutin",fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=200, width=200, block=true)]
[charslot(slot = "l", name = "avg_4146_nymph_1#10$1",focus="n")]
[name="埃芒加德"]抱歉啊小妮芙，我也不想这样催你的......
[name="埃芒加德"]可是这几块死魂灵碎片一天不收集齐，我这边就一天不得安宁......
[name="埃芒加德"]你知道吗，这几天老师他和维什戴尔吵了不少架，他俩听起来比熔炉里的老祖宗还要疯！
[charslot(slot = "l", name = "avg_4146_nymph_1#10$1",focus="l")]
[name="妮芙"]对不起呀埃米......这几天我快把卡兹戴尔转了个遍，剩下的死魂灵碎片就是没有线索。
[charslot(slot = "l", name = "avg_4146_nymph_1#10$1",focus="n")]
[name="埃芒加德"]唉，只能拜托你再加把劲了。对了，和你一起的那个贫民窟的小子呢？
[charslot(slot = "l", name = "avg_4146_nymph_1#13$1",focus="l")]
[name="妮芙"]他数了数这片生活区的住户数量，又算了算我们步行的速度，最后发现，如果想在天黑之前排查完这片生活区，只能分头行动。
[name="妮芙"]然后我们就从中间分开，一人负责一边。他说他负责的那边有些手脚不干净的维修工，以前坑过他，这次正好给他们点教训。
[name="妮芙"]希望他不会遇到什么危险的事情......不过，以他的能力，就算碰到了，应该也能轻松化解吧？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[CharacterCutin(widgetID="1",fadetime=0,block=true)]
[charslot]
[Background(image="49_g2_kazdelstreet_d",screenadapt="showall")]
[charslot(slot = "m", name = "avg_4147_mitm_1#4$1",focus="m")]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4147_mitm_1#4$1",focus="m")]
[name="珀耳"]喂，我不过就多问了几句，你们至于掏家伙吗？
[name="珀耳"]做了黑心生意就不要怕人家找上门来嘛，再说，我又没说要向军事委员会举报你们——算了，对付你们两个，我就当活动一下筋骨......
[charslot(slot = "m", name = "avg_4147_mitm_1#5$1",focus="m")]
[multiline(name="珀耳")]什么？那几十个人也是跟你们一伙的？
[charslot(slot = "m", name = "avg_4147_mitm_1#10$1",focus="m")]
[multiline(name="珀耳")]呃，咱们还有商量的余地吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="52_mini01_katzdalesquare_d",screenadapt="showall")]
[charslot(slot = "l", name = "avg_4146_nymph_1#13$1",focus="l")]
[CharacterCutin(widgetID="1", name="avg_npc_869_1#6$1", style="cutin",fadestyle= "horiz_expand_center", fadetime=0, offsetx=200, width=200, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_4146_nymph_1#1$1",focus="l")]
[name="妮芙"]埃米，你说，那些蹦出来的死魂灵，会不会出来游历几天后，因为想家，自己回到炉子里去呀？
[charslot(slot = "l", name = "avg_4146_nymph_1#1$1",focus="n")]
[name="埃芒加德"]你要不要听听自己在说什么......
[name="埃芒加德"]把你关在一个狭小的地方几百年，你会想回去？
[charslot(slot = "l", name = "avg_4146_nymph_1#13$1",focus="l")]
[name="妮芙"]我......我就是想想嘛......我也不知道，熔炉里到底是什么样。
[name="妮芙"]我在想，或许卡兹戴尔也是一个“熔炉”呢？外面的人觉得城里可怕得不得了，但对于我们来说，这就是我们的家呀。
[name="妮芙"]不过确实很难想象，被关在一个地方两百多年是什么感觉，毕竟我才在这里生活了十几年......在这方面，埃米应该更有经验吧？
[charslot(slot = "l", name = "avg_4146_nymph_1#13$1",focus="n")]
[name="埃芒加德"]小妮芙，这不是可以继续聊下去的话题哦。
[charslot(slot = "l", name = "avg_4146_nymph_1#1$1",focus="l")]
[name="妮芙"]嘿嘿......
[charslot(slot = "l", name = "avg_4146_nymph_1#1$1",focus="n")]
[CharacterCutin(widgetID="1", name="avg_npc_869_1#8$1", style="cutin",fadestyle= "horiz_expand_center", fadetime=0, offsetx=200, width=200, block=true)]
[name="埃芒加德"]唉，不知道该说你什么好。恐怕整个卡兹戴尔也只有你会这么想了，最善良的笞心魔。
[charslot(slot = "l", name = "avg_4146_nymph_1#7$1",focus="l")]
[name="妮芙"]咦？我怎么......（嗅嗅）......好像闻到了一股草药茶的香气。
[name="妮芙"]啊，我想起来了！前面就是卡莱莎女士的家了，要不顺便去拜访一下？
[charslot(slot = "l", name = "avg_4146_nymph_1#7$1",focus="n")]
[CharacterCutin(widgetID="1", name="avg_npc_869_1#7$1", style="cutin",fadestyle= "horiz_expand_center", fadetime=0, offsetx=200, width=200, block=true)]
[name="埃芒加德"]妮芙！我们还有要紧事要做的！
[charslot(slot = "l", name = "avg_4146_nymph_1#9$1",focus="l")]
[name="妮芙"]嗯......我是去寻找死魂灵碎片的下落的，才不是因为想吃莓果饼干了。没错！难道寻找死魂灵碎片不算要紧事吗？
[charslot(slot = "l", name = "avg_4146_nymph_1#9$1",focus="n")]
[CharacterCutin(widgetID="1", name="avg_npc_869_1#9$1", style="cutin",fadestyle= "horiz_expand_center", fadetime=0, offsetx=200, width=200, block=true)]
[name="埃芒加德"]......行吧，不过别耽搁太久。
[name="埃芒加德"]说起卡莱莎，那个人......也真亏你可以和她相处得那么好。
[charslot(slot = "l", name = "avg_4146_nymph_1#1$1",focus="l")]
[name="妮芙"]卡莱莎女士人很好的！之前每次去她家，她都会送我一些小礼物。为什么别人都害怕她呢......
[name="妮芙"]对了，这次我也不能空着手去拜访......呸呸，是执行公务！怎么也得带点伴手礼吧？
[charslot(slot = "l", name = "avg_4146_nymph_1#14$1",focus="l")]
[name="妮芙"]让我想想，她刚搬过来不久，这时

... (全文36084字符)
```

### level_act17mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="52_mini01_katzdalesquare_d",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4146_nymph_1#13$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4146_nymph_1#13$1",focus="m")]
[name="妮芙"]埃米埃米，收到请回答，收到请回答~
[Dialog]
[charslot(slot = "m", name = "avg_4146_nymph_1#13$1",focus="n")]
[playsound(key="$d_avg_recorderglitch",volume=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_4146_nymph_1#17$1",focus="m")]
[name="妮芙"]埃米......怎么不灵了？
[charslot(slot = "m", name = "avg_4151_tinman_1#10$1",focus="m")]
[name="奇怪的路人"]这位笞心魔小姑娘，能先把我的手解开吗？我保证不跑——至少让我先抽支烟？
[charslot(slot = "m", name = "avg_4146_nymph_1#12$1",focus="m")]
[name="妮芙"]不行！把你送回大熔炉之前我是不会解开的。
[charslot(slot = "m", name = "avg_4151_tinman_1#1$1",focus="m")]
[name="奇怪的路人"]你真的认错人了。虽然我本来就打算去一趟大熔炉，但我确实不是从那里面逃出来的。
[name="奇怪的路人"]我的上衣口袋里有哥伦比亚签发的身份证件，我可以拿给你看——只要你解开我的手。
[charslot(slot = "m", name = "avg_4147_mitm_1#1$1",focus="m")]
[name="珀耳"]从哥伦比亚跑到卡兹戴尔来，要挺久的吧？
[name="珀耳"]但凡你说自己是从雷姆必拓来的，我也许都信了。
[Dialog]
[charslot(slot = "m", name = "avg_4146_nymph_1#14$1",focus="m")]
[playsound(key="$d_avg_recorderglitch",volume=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_4146_nymph_1#14$1",focus="m")]
[name="妮芙"]埃米，听得到吗？喂，喂......
[charslot(slot = "m", name = "avg_4151_tinman_1#1$1",focus="m")]
[name="奇怪的路人"]那个箱子里的通讯术式构造已经被破坏了，你再怎么拍它也是修不好的。
[charslot(slot = "m", name = "avg_4146_nymph_1#11$1",focus="m")]
[name="妮芙"]你还好意思说！都怪你，把我的手提箱给撑坏了！
[charslot(slot = "m", name = "avg_4151_tinman_1#1$1",focus="m")]
[name="奇怪的路人"]那如果我帮你修好这个小箱子，你能解开这条锁链吗？
[charslot(slot = "m", name = "avg_4146_nymph_1#17$1",focus="m")]
[multiline(name="妮芙")]你真能修好？
[charslot(slot = "m", name = "avg_4146_nymph_1#12$1",focus="m")]
[multiline(name="妮芙")]你可不许耍赖！我、我有的是办法对付你！
[charslot(slot = "m", name = "avg_4151_tinman_1#9$1",focus="m")]
[name="奇怪的路人"]知道了，小笞心魔。放心，不需要你劳神，我绝对不会乱跑的。
[charslot(slot = "m", name = "avg_4147_mitm_1#5$1",focus="m")]
[name="珀耳"]等会儿，妮芙你不会当真了吧？这可是个被死......被老祖宗附身的家伙，你真要给他解开？
[charslot(slot = "m", name = "avg_4151_tinman_1#9$1",focus="m")]
[name="奇怪的路人"]老插嘴的小朋友，你对死魂灵和笞心魔都不够了解。如果说有谁绝对不会被死魂灵干扰到心智，那这人一定是位笞心魔。
[charslot(slot = "m", name = "avg_4146_nymph_1#13$1",focus="m")]
[name="妮芙"]我先给你解开一只手......欸！你怎么就挣脱了！你骗人！
[charslot(slot = "m", name = "avg_4147_mitm_1#4$1",focus="m")]
[name="珀耳"]就知道你不怀好心！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_wepncontact", volume=0.6)]
[playsound(key="$d_avg_ironchaindrop", volume=0.8,delay=0.6)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_4151_tinman_1#1$1",focus="m")]
[name="奇怪的路人"]两只手被绑了这么久，实在难受。
[charslot(slot = "m", name = "avg_4147_mitm_1#6$1",focus="m")]
[name="珀耳"]你这副铁皮身躯，也会疼吗？
[charslot(slot = "m", name = "avg_4151_tinman_1#1$1",focus="m")]
[name="奇怪的路人"]不是铁，是锡。疼倒不疼，就是......
[Dialog]
[charslot(slot = "m", name = "avg_4151_tinman_1#1$1",focus="m")]
[PlaySound(key="$d_avg_lighter", volume=0.7)]
[delay(time=1.5)]
[charslot]
金属打造的指关节灵巧地夹住一根香烟，那根香烟仿佛是凭空出现的。
凑近嘴边深吸一口后，怪人将香烟在指间打了个转，然后把每一颗火星都仔细地摁灭在掌心里。
[charslot(slot = "m", name = "avg_4151_tinman_1#2$1",focus="m")]
[name="奇怪的路人"]咻——舒服。
[name="奇怪的路人"]在卡兹戴尔可买不到这种级别的卷烟，得省着点儿抽。
[charslot(slot = "m", name = "avg_4146_nymph_1#12$1",focus="m")]
[name="妮芙"]喂，你答应了我要修好手提箱的。
[charslot(slot = "m", name = "avg_4151_tinman_1#9$1",focus="m")]
[name="奇怪的路人"]骗你的。
[name="奇怪的路人"]里面的术式出自巫妖之手，那些骄傲的家伙从来不会将可维修性纳入设计的考虑范围内，不过他们中的一些，也的确有骄傲的资格。
[charslot(slot = "m", name = "avg_4146_nymph_1#11$1",focus="m")]
[name="妮芙"]说这么多，不还是耍赖吗！
[charslot(slot = "m", name = "avg_4151_tinman_1#9$1",focus="m")]
[name="奇怪的路人"]听我说完。你的目的不是找人吗？虽然修不好它，但我帮你找到那个造出它的巫妖不就行了？
[charslot(slot = "m", name = "avg_4146_nymph_1#7$1",focus="m")]
[name="妮芙"]你、你怎么知道我要找的是谁？
[charslot(slot = "m", name = "avg_4151_tinman_1#9$1",focus="m")]
[name="奇怪的路人"]不知道呀，不过好像也不需要知道。
[Dialog]
[charslot]
怪人头向后仰，灰白色的烟雾从他的口中缓缓吐出。
灰雾如云弥散，亦如投石于一潭死水，属于死魂灵的印痕波动席卷而出，整座卡兹戴尔似乎都在一瞬间陷入寂静。
片刻后，嘈杂声重新涌来，那团灰雾也彻底消散不见。
[charslot(slot = "m", name = "avg_4147_mitm_1#5$1",focus="m")]
[name="珀耳"]你到底是谁？
[charslot(slot = "m", name = "avg_4146_nymph_1#7$1",focus="m")]
[name="妮芙"]您......到底是谁？
[charslot(slot = "m", name = "avg_4151_tinman_1#9$1",focus="m")]
[name="奇怪的路人"]叫我锡人就好。
[charslot(slot = "m", name = "avg_4147_mitm_1#5$1",focus="m")]
[name="珀耳"]锡人......？
[charslot(slot = "m", name = "avg_4151_tinman_1#2$1",focus="m")]
[name="锡人"]看，你要找的人来了。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_highheelfts", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_869_1#11$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_869_1#11$1",focus="m")]
[name="埃芒加德"]行走于大地的死魂灵屈指可数，您又是其中哪一位？
[charslot(slot = "m", name = "avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]他说他叫锡人。
[charslot(slot = "m", name = "avg_4147_mitm_1#1$1",focus="m")]
[name="珀耳"]他说他从哥伦比亚来的。
[charslot(slot = "m", name = "avg_npc_869_1#11$1",focus="m")]
[name="埃芒加德"]......卡兹戴尔没有为您备下位置。
[charslot(slot = "m", name = "avg_4151_tinman_1#9$1",focus="m")]
[name="锡人"]这不怪你，我离开这里时的确没想过自己还有回来的一天。
[charslot(slot = "m", name = "avg_npc_869_1#11$1",focus="m")]
[name="埃芒加德"]您想要什么？
[charslot(slot = "m", name = "avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]他说他想去大熔炉看看。
[charslot(slot = "m", name = "avg_npc_869_1#7$1",focus="m")]
[name="埃芒加德"]妮妮！
[charslot(slot = "m", name = "avg_4146_nymph_1#9$1",focus="m")]
[name="妮芙"]知道啦~你问你问，我不插嘴了。
[charslot(slot = "m", name = "avg_npc_869_1#11$1",focus="m")]
[name="埃芒加德"]那么请问......算了，好像也没什么要问的了。
[name="埃芒加德"]按理说，您这种级别的客人，我得去找我老师来接待才是，不过......
[charslot(slot = "m", name = "avg_4151_tinman_1#9$1",focus="m")]
[name="锡人"]你的老师不会是那个倔老头子吧？那还是别告诉他了，否则我这假期就算是彻底报废了。
[charslot(slot = "m", name = "avg_npc_869_1#1$1",focus="m")]
[name="埃芒加德"]如果您想去魂灵熔炉底下看看的话，我可以带您去，不会让别人知道的。
[charslot(slot = "m", name = "avg_4151_tinman_1#1$1",focus="m")]
[name="锡人"]（摇头）我想进去看看。
[chars

... (全文30519字符)
```


## 统计

- 总字符数：241196
- 对话行数：1624


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
