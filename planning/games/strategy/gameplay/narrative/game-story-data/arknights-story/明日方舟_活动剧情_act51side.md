# 明日方舟 · 活动剧情 · act51side（27段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act51side」完整剧情脚本（27个文件，3664行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act51side
- 脚本文件数：27

### act51side_6_a

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动51side普通关_6
[InputBlocker(blockInput=true)]
[Delay(time=1.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.4)]
[PopupDialog(dialogHead="$avatar_sut1", protectTime=0.5)]......就是这里，冬将军说会过来接应我们。
[PopupDialog(dialogHead="$avatar_sut1", protectTime=0.5)]要抓紧时间了，好不容易才从他们手底下逃出来，我们绝不——
[PopupDialog(dialogHead="$avatar_sut2", protectTime=0.5)]等等，那个声音......是格罗莫夫，他来了！
[Battle.Pause(pause=false)]
```

### act51side_6_b

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动51side普通关_6
[InputBlocker(blockInput=true)]
[Delay(time=1.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.4)]
[PopupDialog(dialogHead="$avatar_ubhh", protectTime=0.5)]又来了？这群小虫子真不老实......
[PopupDialog(dialogHead="$avatar_ubhh", protectTime=0.5)]你们几个，给我一起上！谁要是慢了一步，我就告诉老大，打不死你们！
[PopupDialog(dialogHead="$avatar_sut1", protectTime=0.5)]那边也有人......欸，同学，不能乱跑！
[Battle.Pause(pause=false)]
```

### act51side_6_c

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动51side普通关_6
[InputBlocker(blockInput=true)]
[Delay(time=1.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.4)]
[PopupDialog(dialogHead="$avatar_headb2", protectTime=0.5)]欺负人的家伙，看这边！认准你们的对手。
[PopupDialog(dialogHead="$avatar_headb2", protectTime=0.5)]你再也不能躲在大炮后面了，格罗莫夫！
[PopupDialog(dialogHead="$avatar_headb2", protectTime=0.5)]同学们，营地就在后方，我来挡着这些败类。
[PopupDialog(dialogHead="$avatar_sut2", protectTime=0.5)]是冬将军！我们得救了！
[Battle.Pause(pause=false)]
```

### level_act51side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="72_g7_ballroom",screenadapt="coverall")]
[curtain(direction = 0,fillfrom = 0.1,fillto = 0.1, fadetime=0.1,block=true)]
[curtain(direction = 4,fillfrom = 0.1,fillto = 0.1, fadetime=0.1,block=true)]
[PlaySound(key="$d_avg_highheeledshoe_carpet_fts",volume=0, channel="f", loop=true)]
[SoundVolume(volume=0.8, channel="f",fadetime=2)]
[name="早露"]一路走来，走廊上都只点着蜡烛。连皇宫也减少了电的用度吗？这真是......
[name="殷勤的近侍"]为将储存的能源节省起来分给民众，陛下是这样说的。
[name="殷勤的近侍"]不过请您放心，这只是陛下出于勤俭节约的提议，宫中的生活并没有受到影响，今年的冬季舞会也是如此。
[name="殷勤的近侍"]我们就要到了。罗斯托娃小姐，请让我为您取下大衣。
[dialog]
[StopSound(channel="f", fadetime=1)]
[Delay(time=1.2)]
[PlaySound(key="$d_avg_clothtrailground")]
[Delay(time=2.8)]
[PlaySound(key="$d_avg_highheeledshoe_carpet_fts", volume=0.8)]
[name="早露"]感谢您的帮助。
[name="殷勤的近侍"]职责所在。
[dialog]
[playMusic(key="$ouat_loop", volume=0.6)]
[focusout(type="bg", id="72_g7_ballroom", from=1, to=0.2, duration=4, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_2165_1#4$1", duration=1, block=true)]
[Delay(time=1)]
[name="早露"]好亮......
[charslot(slot = "m", name = "avg_npc_1982_1#1$1")]
[name="殷勤的近侍"]那么，我就退下了。祝您愉快。
[dialog]
[charslot(slot = "m",posfrom="0,0",posto="60,0",afrom=1,ato=0,duration=1)]
[Delay(time=1.1)]
[charslot]
[charslot(slot = "m", name = "avg_npc_2165_1#3$1",posfrom="-35,0",posto="35,0",duration=1)]
[Delay(time=1.1)]
[name="早露"]烦请稍等，我还有一些问题——
[charslot]
[charslot(slot = "m", name = "avg_npc_2173_1#1$1")]
[name="贵族女性"]——娜塔申卡？
[dialog]
[charslot]
[charslot(slot = "r", name = "avg_npc_2165_1#6$1")]
[name="早露"]嗯？您是......
[name="早露"]沃伦佐娃伯爵夫人？
[dialog]
[PlaySound(key="$d_avg_walkfast")]
[charslot(slot = "l", name = "avg_npc_2173_1#1$1",posfrom="-80,0",posto="110,0",duration=0.8)]
[Delay(time=0.8)]
[charslot(slot = "l",focus="l")]
[name="沃伦佐娃夫人"]陛下在上......可怜的孩子，真的是你。
[charslot(slot = "l",focus="n")]
稍远处的贵妇人看见了早露，立即快步迎了上来，惊喜的神情几乎让她有失贵族仪态。
她紧紧握住了早露的小臂，像是在努力确认眼前的女孩并不是幻影。
[dialog]
[charslot(slot = "l", name = "avg_npc_2173_1#1$1",afrom=1,ato=1,posfrom="110,0",posto="20,0",duration=1.8)]
[Delay(time=1.8)]
[charslot(slot = "l",focus="l")]
[name="沃伦佐娃夫人"]娜塔申卡......实在是太好了，我还能见到你......健康活着的你。
[name="沃伦佐娃夫人"]我听说了发生在切尔诺伯格的事情，我的心简直都要碎了。我实在是不明白，命运为何要让如此善良的一家人遭受这样可怕的事......
[charslot(slot = "r", name = "avg_npc_2165_1#8$1",focus="r")]
[name="早露"]承蒙您的挂念，虽说损失了些产业，但比起全家人的安危来说，那些已经不值一提了......总之，都过去了。
[charslot(slot = "l",focus="l")]
[name="沃伦佐娃夫人"]是的，是的，快让我们忘了那些不好的回忆吧......你不知道，我在收到你的信，得知你要来圣骏堡的时候有多高兴。
[name="沃伦佐娃夫人"]真希望你能够在这过上一段平静的日子，可如你所见，现在的圣骏堡也不是一个安稳平静的地方。
[name="沃伦佐娃夫人"]到处都是心怀不满的人，到处都是不知感恩的抱怨——仿佛那些无礼的军人闹得还不够似的，吵闹的平民也恨不得将圣骏堡翻个底朝天。
[charslot(slot = "r", name = "avg_npc_2165_1#13$1",focus="r")]
[name="早露"]......
[charslot(slot = "l",focus="l")]
[name="沃伦佐娃夫人"]哦，瞧我。你刚回来，恐怕还不知道。为近来这些事，我终日精神紧绷，多梦少眠，可见到老友的孩子，总归不该一上来就说这些。
[charslot(slot = "r", name = "avg_npc_2165_1#11$1",focus="r")]
[name="早露"]......不会的，只要是您说的，我都愿意听。
[charslot(slot = "l",focus="l")]
[name="沃伦佐娃夫人"]你是个好孩子，但现在却不是提这些事的好时候。
[name="沃伦佐娃夫人"]告诉我，娜塔申卡。你母亲身体还好吗？你父亲安德烈如今又在何处？
[name="沃伦佐娃夫人"]如果他来了圣骏堡，却没遣人告知于我，只让你来参加冬季舞会......
[name="沃伦佐娃夫人"]想来，应该是因为我们两家已经生分太久，我实在不算是个合格的朋友。
[charslot(slot = "r", name = "avg_npc_2165_1#8$1",focus="r")]
[name="早露"]不是这样的，沃伦佐娃夫人。父亲曾说，如果能在这里见到您，就让我代他向您致意，请您宽恕他的久疏问候。
[charslot(slot = "r", name = "avg_npc_2165_1#8$1",focus="r")]
[name="早露"]至于母亲那边就更不必说了，您当然是她最要好的女友，可罗斯托夫家族如今必须想办法将中部仅剩的那些产业紧紧抓住。
[charslot(slot = "r", name = "avg_npc_2165_1#5$1",focus="r")]
[name="早露"]“我们切不可再丢失任何体面。”所以，非常遗憾......他们在短时间内都脱不开身。
[charslot(slot = "l",focus="l")]
[name="沃伦佐娃夫人"]我了解了。但是孩子，你最后应该说的是：“所以，我就在这里了。”
[name="沃伦佐娃夫人"]看看你，已经是一个成熟体面的姑娘了，可以代表罗斯托夫家族了，不是吗？
[name="沃伦佐娃夫人"]我得说，你的仪态与教养，比许多生斯长斯的圣骏堡人都更为优秀——我相信用不了多久，圣骏堡会记住罗斯托夫这个姓氏的。
[charslot(slot = "r", name = "avg_npc_2165_1#1$1",focus="r")]
[name="早露"]不......我很清楚自己还有许多要学的事务。
[charslot(slot = "r", name = "avg_npc_2165_1#1$1",focus="r")]
[name="早露"]说起这点，夫人，其实我很想向您请教，关于圣骏堡现在的局势......
[charslot(slot = "l",focus="l")]
[name="沃伦佐娃夫人"]年轻的娜塔申卡，不要着急，我了解你的困惑，但这不是三言两语就能说清楚的问题。
[name="沃伦佐娃夫人"]你要学会用自己的眼睛去看，不会有比现在更好的机会了，你现在最应该做的就是——先好好享受这场冬季舞会。
[name="沃伦佐娃夫人"]在陛下到来之前，抛开那些恼人的问题、急于知道的答案，以及所有有关未来将会如何的奇谈怪论，只是享受当下。
[name="沃伦佐娃夫人"]去舞蹈，去嬉笑，去做年轻人应当做的事。
[name="沃伦佐娃夫人"]如果你看上某位青年军官，就算是那个老顽固博尔孔斯基家的，为了你母亲，我也会豁出这张老脸去替你说媒——
[name="沃伦佐娃夫人"]总之，在陛下的庇护下安宁地享乐，这是属于首都，属于我们这些忠诚的人的特权。
[name="沃伦佐娃夫人"]娜塔申卡，你必须先学会这点，才能真正融入其中。
[Dialog]
[curtain(direction = 0,fillfrom = 0.1,fillto = 0.01, fadetime=2)]
[curtain(direction = 4,fillfrom = 0.1,fillto = 0.01, fadetime=2)]
[Delay(time=2)]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot]
[curtain]
[Background(image="72_g2_sjbstreet_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[playMusic(intro="$mist_intro",key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$transmission", volume=0.8)]
[Subtitle(text="“......你必须先学会这点，才能真正融入其中。”",multi = true, x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_2156_1#2$1")]
[name="真理"]......矿工们仍在挨饿，哪怕是在圣骏堡，奥多耶夫区的居民也都已经用不起暖气，卡托加区更是在停工之后，被彻底切断了供电和供暖。
[charslot(slot = "m", name = "avg_npc_2156_1#2$1")]
[name="真理"]就算这样，他们也还是要享乐。
[charslot(slot = "m", name = "avg_196_sunbr_1#5$1")]
[name="古米"]我不明白......那个人不是说，陛下节省了皇宫的用电吗？那些省下来的能源呢？为什么——
[charslot(slot = "m", name = "avg_194_leto_1#4$1")]
[name="烈夏"]这都聊的些什么乌七八糟的，“大人物”就是麻烦。
[charslot(slot = "m", name = "avg_196_sunbr_1#21$1")]
[name="古米"]而且，早露姐一个人在里面，真的没关系吗？
[charslot(slot = "m", name = "avg_npc_2156_1#11$1")]
[name="真理"]学生联合大会召开的前几天，娜塔莉娅就和我们商量了，她会以罗斯托夫家继承人的身份进入舞会，探查情报。
[charslot

... (全文20087字符)
```

### level_act51side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[playMusic(intro="$rebel_intro",key="$rebel_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$firestorm")]
[bgeffect(name="$eb_smoke_01",layer=1)]
[Delay(time=1.2)]
[Image(image="72_i03_1", screenadapt="coverall", xScale=1, yScale=1, fadetime=0.5)]
[ImageTween(image="72_i03_1",xScaleFrom=1, yScaleFrom=1, xScaleTo=1.02, yScaleTo=1.02, duration=4, block=false)]
[PlaySound(key="$d_avg_churchfire",volume=0, channel="f", loop=true)]
[SoundVolume(volume=0.2, channel="f",fadetime=2)]
[PlaySound(key="$d_avg_audience_chaos",volume=0.8)]
[delay(time=2)]
[Image(image="72_i03_2", screenadapt="coverall", xScale=1.02, yScale=1.02,fadetime=1.5)]
[ImageTween(image="72_i03_2",xScaleFrom=1.02, yScaleFrom=1.02, xScaleTo=1.06, yScaleTo=1.06, duration=8, block=false)]
[delay(time=1)]
[name="乌萨斯学生"]释放拉列亚！释放被你们欺压的所有人！
[name="乌萨斯学生"]放出库存，均分能源，让人人都能用上暖气！
[name="古米"]对不起对不起，麻烦让我过一下......
[name="古米"]凛、凛冬姐，真理姐！你们......都在哪？
[PlaySound(key="$d_avg_audience_chaos",volume=0.8)]
[name="乌萨斯学生"]自由归于人民！面包归于人民！
[name="乌萨斯学生"]今日的沉默，就是明日的奴役，聆听我们发出的声音！
[name="乌萨斯学生"]快滚出来和我们谈判！
[StopSound(channel="f", fadetime=2)]
[StopSound(channel="kou", fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[image]
[bgeffect]
[Background(image="66_g12_deitygrypherburgmeeting",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_crowdtalk_fear",volume=0, channel="dis", loop=true)]
[SoundVolume(volume=1, channel="dis",fadetime=2)]
[charslot(slot = "m", name = "avg_405_absin_1#1$2")]
[name="苦艾"]这之后的故事，或许在场的各位都比我更熟悉。
[charslot(slot = "m", name = "avg_405_absin_1#2$2")]
[name="苦艾"]当时，舞会厅里乱作一团，甚至有的大人还在惊慌之下，脱了外衣，从侍从手中夺过一顶女帽就往外走......
[charslot(slot = "m", name = "avg_npc_2171_1#1$1")]
[name="愤怒的贵族"]胡说！你根本没去舞会，究竟是谁向你灌输了这些谣言？
[charslot(slot = "m", name = "avg_405_absin_1#4$2")]
[name="苦艾"]警队里早已传了个遍，很难说源头究竟出自哪里。不过，如果这是谣言，那我必须向您道歉——
[charslot(slot = "m", name = "avg_npc_2171_1#1$1")]
[name="愤怒的贵族"]不是我！
[name="愤怒的贵族"]不是，不是向我道歉，你应该向所有参加舞会的人道歉！
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]肃静！
[SoundVolume(volume=0.4, channel="dis",fadetime=0.1)] 
[name="仲裁人"]听证会对街谈巷议不感兴趣，我们需要知道学生们在当晚的情况。
[name="仲裁人"]比如具体说说，是谁喊出了那句不敬之语？
[charslot(slot = "m", name = "avg_405_absin_1#1$2")]
[name="苦艾"]哪一句？
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]......还能是哪句？最不敬的那句。
[charslot(slot = "m", name = "avg_405_absin_1#7$2")]
[name="苦艾"]当时说什么的人都有，我实在不知道您指的是——
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]就是最大逆不道、目无君上、傲慢无礼......这里没人能说得出口的那一句！
[charslot(slot = "m", name = "avg_405_absin_1#1$2")]
[name="苦艾"]啊，我明白了。
[StopSound(channel="dis", fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[playMusic(intro="$rebel_intro",key="$rebel_loop", volume=0.6)]
[bgeffect(name="$eb_smoke_01",layer=1)]
[PlaySound(key="$d_avg_churchfire",volume=0, channel="f", loop=true)]
[SoundVolume(volume=0.2, channel="f",fadetime=2)]
[PlaySound(key="$d_avg_studentsshout_amb_loop",volume=0, channel="kou", loop=true)]
[SoundVolume(volume=0.8, channel="kou",fadetime=2)]
[Image(image="72_i03_2", screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="激愤的学生"]打倒傻*乌萨斯粗口*皇帝！
[Dialog]
[ImageTween(xScaleTo=1.2, yScaleTo=1.2, duration=0.8, block=false)]
[Image(image="72_i03_2", screenadapt="coverall",fadetime=0.8)]
[Delay(time=0.8)]
[multiline(name="激愤的学生")]打倒傻*乌萨斯粗口*皇帝！
[ImageTween(xScaleTo=1.2, yScaleTo=1.2, duration=0.8, block=false)]
[Image(image="72_i03_2", screenadapt="coverall",fadetime=0.8)]
[Delay(time=1)]
[multiline(name="激愤的学生")]打倒傻*乌萨斯粗口*皇帝！
[ImageTween(xScaleTo=1.2, yScaleTo=1.2, duration=0.8, block=false)]
[Image(image="72_i03_2", screenadapt="coverall",fadetime=0.8)]
[Delay(time=1)]
[multiline(name="激愤的学生")]打倒傻*乌萨斯粗口*皇帝！
[ImageTween(xScaleTo=1.2, yScaleTo=1.2, duration=0.8, block=false)]
[Image(image="72_i03_2", screenadapt="coverall",fadetime=0.8)]
[Delay(time=1.5)]
[name="列昂尼德"]流着骏鹰血的秽种，把权力还给真正的乌萨斯人！
[name="激愤的学生"]让吸血虫维特滚出来！让草包费奥多尔滚出来！
[stopmusic(fadetime=2)]
[StopSound(channel="kou", fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[bgeffect]
[StopSound(channel="f", fadetime=2)]
[Background(image="66_g12_deitygrypherburgmeeting",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]你的意思是，在这场行动中，所有学生都是对陛下口出狂言的无礼之徒。
[charslot(slot = "m", name = "avg_405_absin_1#1$2")]
[name="苦艾"]也许，只除了极少数仍然保有理智的人。青年们总是很容易被热血带动着发出不属于自己的声音，仲裁人阁下。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]又或许，你只是为了替其中的一部分人遮掩，而有所夸大。
[charslot(slot = "m", name = "avg_405_absin_1#6$2")]
[name="苦艾"]我说的只是事实，您的猜想却实在令我惶恐。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]让我们先回到之前的叙述。你曾经解释过为什么娜塔莉娅小姐并未留意陛下的缺席，那么，你又是否知道陛下那时身在何处？
[charslot(slot = "m", name = "avg_405_absin_1#2$2")]
[name="苦艾"]通过警队的消息渠道，我的确了解一些，但也只是非常模糊的消息。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]你知道他当时在哪里？
[charslot(slot = "m", name = "avg_405_absin_1#1$2")]
[name="苦艾"]我知道他当时就在皇宫中，但不知道他为什么没有准时出现在舞会上。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]不，你知道。
[charslot(slot = "m", name = "avg_405_absin_1#4$2")]
[name="苦艾"]什么？
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]我这里的证据显示，圣骏堡警察厅夜巡部队是最先得知陛下失踪消息的，这就意味着你也能够通过相应渠道了解。
[name="仲裁人"]回答我，卓娅女士，你为什么要隐瞒陛下在那晚游行示威的混乱

... (全文31252字符)
```

### level_act51side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="66_g12_deitygrypherburgmeeting",screenadapt="coverall",xScale=1.1, yScale=1.1)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_crwddiscuss_inside",volume=0, channel="f", loop=true)]
[SoundVolume(volume=0.8, channel="f",fadetime=0.5)]
[Delay(time=2)]
[charslot(slot = "m", name = "avg_npc_2168_1#1$1",duration=0.8)]
[Delay(time=1)]
[name="仲裁人"]肃静！肃静！
[PlaySound(key="$d_avg_gavel", volume=1)]
[dialog]
[StopSound(channel="f", fadetime=1)]
[Delay(time=1)]
[name="仲裁人"]卓娅女士，请回答本庭的问题！
[charslot(slot = "m", name = "avg_405_absin_1#1$2")]
[name="苦艾"]仲裁人阁下，我已经回答过了。
[charslot(slot = "m", name = "avg_405_absin_1#1$2")]
[name="苦艾"]我没办法描述我没有亲眼见过的事情。索尼娅是否与刺杀皇帝陛下的歹徒有关，我不知道。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]可根据委员会收到的举报材料，你们总是一起行动。
[charslot(slot = "m", name = "avg_405_absin_1#6$2")]
[name="苦艾"]不，仲裁人阁下。
[charslot(slot = "m", name = "avg_405_absin_1#6$2")]
[name="苦艾"]我已声明过，我并不那么支持她们的行动，也非“自治团”的一员，您可以看到，我身上——
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]我知道，她们甚至没有分配给你一枚徽章。
[charslot(slot = "m", name = "avg_405_absin_1#1$2")]
[name="苦艾"]......以及，我想冒昧地询问阁下，现在已经到听证会质证环节了吗？
[dialog]
[charslot]
[name="书记官"]按照第八十七号临时审查听证会事先制定的章程，只有在所有证人和证据的关联性均已充分说明的情况下，听证会才会进入质证环节。
[name="书记官"]在那之前，证人可以选择不回答问题。
[charslot(slot = "m", name = "avg_405_absin_1#1$2")]
[name="苦艾"]我没有问题了。
[dialog]
[charslot]
[name="书记官"]仲裁人阁下......？
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]......卓娅女士。我看过你的资料和档案。我觉得很多事都很明显，比如——
[name="仲裁人"]你可以选择做一个好孩子。
[charslot(slot = "m", name = "avg_405_absin_1#1$2")]
[name="苦艾"]......
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]传唤下一位证人！
[dialog]
[charslot]
[name="书记官"]仲裁人传唤二号证人。一号证人请回到自己的坐席。
[dialog]
[charslot]
[charslot(slot="r", posfrom="0,0", posto="-150,0", duration=0)]
[charslot(slot="r", name = "avg_405_absin_1#1$2")]
[name="苦艾"]谢谢。
[dialog]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[BackgroundTween(xFrom=0, xTo=50, duration=1.5,ease="OutQuad",block=false)]
[charslot(slot="r", posfrom="-150,0", posto="0,0", duration=2)]
[charslot(slot = "l", name = "avg_4224_turdus_1#1$1", posfrom="-300,0", posto="0,0", duration=2, isblock=true)]
[charslot(slot="r",name = "avg_405_absin_1#4$2",focus="r")]
[name="苦艾"]你......？你怎么也会来？
[charslot(slot = "l", name = "avg_4224_turdus_1#1$1",focus="l")]
[name="冷漠的女孩"]......
[charslot(slot = "l", name = "avg_4224_turdus_1#5$1",focus="l")]
[name="冷漠的女孩"]哼。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="r",name = "avg_405_absin_1#1$2",posfrom="0,0",posto="200,0",afrom=1, ato=0, duration=2.5)]
[Delay(time=2.5)]
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]二号证人，你的名字？
[charslot(slot = "m", name = "avg_4224_turdus_1#1$1")]
[name="乌克西克"]乌克西克。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]奇怪的名字。
[dialog]
[charslot(slot = "r", name = "avg_npc_2171_1#1$1",posfrom="250,0",posto="120,0",duration=1.2)]
[Delay(time=1.5)]
[charslot(slot = "r", focus="r")]
[name="仲裁委员会成员"]（悄声）阿尔乔姆议员，您可以再看一遍这份资料。
[charslot(slot = "m", focus="m")]
[name="仲裁人"]（悄声）无父无母的流浪者，能活下来全靠一群年纪大些的流浪汉护着她，据说一直保护她的人最后死在了学生自治团的手上。
[charslot(slot = "r", focus="r")]
[name="仲裁委员会成员"]（悄声）她和学生们的关系并不融洽......什么该说，什么不该说，我都提前交代过她。
[charslot(slot = "m", focus="m")]
[name="仲裁人"]......
[name="仲裁人"]那么，乌克西克，孩子，不要害怕，开始讲吧。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_4224_turdus_1#2$1")]
[name="乌克西克"]也没什么好怕的......咳咳，“尊贵的仲裁委员会大人们”，是这么说没错吧？
[charslot(slot = "m", name = "avg_4224_turdus_1#2$1")]
[name="乌克西克"]事情是这样的——
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[bgeffect(name="$eb_smoke_01",layer=1)]
[bgeffect(name="$eb_blackmask",layer=2)]
[Image(image="72_i03_2", screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[PlaySound(key="$d_avg_churchfire",volume=0, channel="f", loop=true)]
[SoundVolume(volume=0.2, channel="f",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[name="乌克西克"]那天晚上，我正在街角卖报纸，顺便等待安托沙派人来换我的班。
[name="乌克西克"]安托沙就是我的老大，我后面会说到他——总之，我突然看见，一大伙人朝着舞会厅冲了过去，我心想，难道安托沙那边出了什么意外？
[dialog]
[StopSound(channel="f", fadetime=2)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_audience_chaos",volume=0.4)]
[name="乌克西克"]接着，又有好多警察冒了出来，堵住了几乎所有的路口。这时候我才反应过来，我应该在第一时间就溜走的。
[name="乌克西克"]我看见了我的一位同伴。他什么也没做，呆呆地站在那里，被人群挤过来又撞过去。他看见我，好像喊了一句什么——
[dialog]
[PlaySound(key="$d_avg_stickbeat", volume=0.9)]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[name="乌克西克"]但我没来得及听清，警棍就已经砸到了他的头上，我一下子就看不见他了......
[bgeffect]
[Image]
[dialog]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[name="仲裁人"]停一停！
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Background(image="66_g12_deitygrypherburgmeeting",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]不要讲太多没用的细节......没人听得懂，孩子。
[charslot(slot = "m", name = "avg_4224_turdus_1#3$1")]
[name="乌克西克"]那我应该怎么讲？我只是个小孩，连字母都没认全，你指望我像上门推销员一样能说会道吗？
[charslot(slot = "m", name = "avg_4224_turdus_1#4$1")]
[name="乌克西克"]要不，你告诉我好了，我照着你说的念，行吗？
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]不行！
[charslot(slot = "m",focus="n")]
仲裁人回头狠狠瞪了身旁的贵族一眼，男人没有与他对视，只是用手帕拍去了额角的汗。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]但也不能这样没头没尾的，你从头讲起吧——什么同伙，什么老大，你们到底是个什么组织？
[name="仲裁人"]那天晚上你为什么会出现在那个地方？将你知道的都说出来，不许隐瞒。
[charslot(slot = "m", name = "avg_

... (全文33885字符)
```

### level_act51side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_audience_chaos",volume=0.2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="乌萨斯警察"]所有人！立刻停止反抗！
[name="乌萨斯警察"]你们今晚在这里的行动是绝对不被允许的，希望你们认识到自己的错误！
[name="乌萨斯警察"]我们不想伤害你们这些年轻人，也希望你们配合我们——
[dialog]
[PlaySound(key="$d_avg_punch", volume=1)]
[Delay(time=0.5)]
[name="乌萨斯警察"]*激烈的乌萨斯粗口*！你还敢打我？
[name="乌萨斯警察"]他妈的，真是不要脸的畜生，简直不可理喻！
[Dialog]
[PlaySound(key="$d_avg_twohandedblunt", volume=1)]
[Delay(time=0.8)]
[PlaySound(key="$d_avg_punch", volume=1)]
[Delay(time=0.3)]
[PlaySound(key="$d_avg_fight_amb_loop",volume=0, channel="fi", loop=true)]
[SoundVolume(volume=0.6, channel="fi",fadetime=1)]
[Delay(time=2)]
[StopSound(channel="fi", fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="72_g2_sjbstreet_n",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1981_1#1$1", bstart=0.2,bend=0.7)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.6)]
[playsound(key="$d_avg_sldrrng")] 
[Delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_2170_1#1$1",posfrom="-200,-30",posto="0,-30",duration=1)]
[Delay(time=1.2)]
[charslot(slot = "l",focus="l")]
[name="乌萨斯警察"]报告！我们已经完全控制了舞会厅周围的街道，所有能抓住的人都在这了。
[charslot(slot = "r",focus="r")]
[name="警察厅厅长"]疯了......这世道真是疯了。
[name="警察厅厅长"]学生不在学校，集团军不在自己的属地......整个乌萨斯难道就没有一个人待在他应该在的地方吗？
[charslot(slot = "l",focus="l")]
[name="乌萨斯警察"]呃，那您看是不是先把这些人带回去，再慢慢审问......？
[charslot(slot = "r",focus="r")]
[name="警察厅厅长"]你难道真不认识这些学生的校服？这几所学校里能有多少平民？
[name="警察厅厅长"]你是打算把这些大人物的公子千金带回警察厅，然后等着那些公爵大人挨个上门要人吗？
[charslot(slot = "l",focus="l")]
[name="乌萨斯警察"]这......
[name="乌萨斯警察"]难道......要把他们原地放了？
[charslot(slot = "r",focus="r")]
[name="警察厅厅长"]动动你的脑子！这里面说不定还混着在舞会行刺的歹徒，说放就放，议会来要人的时候我送你去顶罪？
[charslot(slot = "l",focus="l")]
[name="乌萨斯警察"]我......
[charslot(slot = "r",focus="r")]
[name="警察厅厅长"]陛下在上......明明只要熬过今年最后一年，我就能参选议员，离开这个该死的警察厅！
[name="警察厅厅长"]为什么偏要在这个时候！该死......该死！
[name="警察厅厅长"]......我们的监狱还关得下多少人？
[charslot(slot = "l",focus="l")]
[name="乌萨斯警察"]哦，把那些马上要掉脑袋的人都清出去，就可以装下——
[charslot(slot = "r",focus="r")]
[name="警察厅厅长"]......再好好想想吧，我们的监狱真的装得下这么多人吗？
[charslot(slot = "l",focus="l")]
[name="乌萨斯警察"]呃......也许是，装不下的？
[charslot(slot = "r",focus="r")]
[name="警察厅厅长"]当然，当然。
[name="警察厅厅长"]不过我知道一个地方，可以关得下这些无法无天的年轻疯子......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="72_g6_blockcamp",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_2158_1#9$1", duration=1.5, block=true)]
[Delay(time=1.8)]
[name="巴普洛维奇"]陛下在上......有没有人能告诉我，为什么我一回到这片垃圾场，就看到十几辆装满了人的载具。
[charslot(slot = "m", name = "avg_npc_2166_1#1$1")]
[name="被雇佣的打手"]哦，刚才警察厅来人了。他们说牢房不够用了，要征用卡托加区的地盘收容一下这些大闹舞会的犯人。
[name="被雇佣的打手"]真好笑，我还从来没见过那些条子说话这样客气。对了，他们还给你留了封信。
[name="被雇佣的打手"]“尊敬的”......“卡托加区”......“没有用的东西”......
[charslot(slot = "m", name = "avg_npc_2158_1#8$1")]
[name="巴普洛维奇"]把信给我，我自己看。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_paper1", volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Sticker(id="st1", text="<i>尊敬的巴普洛维奇阁下：</i>", multi = true, x=200,y=260, alignment="left", size=24, delay=0.04, width=900,block = true)]
[Sticker(id="st2", text="\n<i>卡托加区已经收容了足够多的没有用的东西，想必也不介意再多装一些。</i>", x=300,y=300, alignment="left", multi = true, size=24, delay=0.04, width=900,block = true)]
[Sticker(id="st3", text="\n\n<i>代替特里波列夫公爵向您问好。</i>", x=300,y=340, alignment="left", multi = true, size=24, delay=0.04, width=900,block = true)]
[Sticker(id="st2", duration=1)]
[Sticker(id="st3", duration=1)]
[Sticker(id="st1", duration=1)]
[Dialog]
[PlaySound(key="$d_avg_paper2", volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_2158_1#3$1")]
[name="巴普洛维奇"]......
[charslot(slot = "m", name = "avg_npc_2158_1#1$1")]
[name="巴普洛维奇"]“没有用的东西”，这怎么会是没有用的东西？那个愚蠢的厅长害怕麻烦，就没有想过这是多么难得的机会？
[charslot(slot = "m", name = "avg_npc_2158_1#1$1")]
[name="巴普洛维奇"]把格罗莫夫叫过来，明天开始我需要频繁访问一些重要的大人物，管控这里的任务要交给他。
[charslot(slot = "m", name = "avg_npc_2166_1#1$1")]
[name="被雇佣的打手"]头儿昨晚喝醉了，现在还没醒呢——后街那家酒吧用的酒精一定有问题！
[charslot(slot = "m", name = "avg_npc_2158_1#8$1")]
[name="巴普洛维奇"]该死的......我请你们来维护治安可是花了大价钱的！
[charslot(slot = "m", name = "avg_npc_2158_1#7$1")]
[name="巴普洛维奇"]现在就去把他给我泼醒，告诉他，让他招待好我们这些客人。
[charslot(slot = "m", name = "avg_npc_2158_1#2$1")]
[name="巴普洛维奇"]从现在开始，连只鼷兽都不许从卡托加区放出去。
[charslot(slot = "m", name = "avg_npc_2166_1#1$1")]
[name="被雇佣的打手"]是要我们“好好招待”一下这些客人的意思？要注意留活口吗？
[charslot(slot = "m", name = "avg_npc_2158_1#9$1")]
[name="巴普洛维奇"]可怜的“小松针”，我知道凭你可怜的智慧是听不懂太复杂的指令的，所以我已经用了尽可能简单的语言。
[charslot(slot = "m", name = "avg_npc_2158_1#1$1")]
[name="巴普洛维奇"]收起你们的那些坏习惯，不许对这些人动手动脚......明白我指的“这些人”都是谁吧？
[charslot(slot = "m", name = "avg_npc_2166_1#1$1")]
[name="被雇佣的打手"]嘁。
[charslot(slot = "m", name = "avg_npc_2158_1#8$1")]
[name="巴普洛维奇"]听好了，如果没有忘记是谁给你们的钱，让你们还能去脏酒馆里浪费生命......就记住我说的话！
[charslot(slot = "m", name = "avg_npc_2158_1#8$1")]
[name="巴普洛维奇"]他们的命，天生比你们贵重！
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[Subtitle(text="我觉得自从我遇到安托沙他们后，自己的运气就变得格外好。",multi = true, x=300, y=340, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="那天晚上，我和其他人在人群中走散了，也许是因为我的个子实在是太小了，没有警察注意到我，我一个人逃了出来。",multi = true,  x=300, y=320, alignment="center", size=24, delay=0.04, 

... (全文34217字符)
```

### level_act51side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="72_g5_blockalley",screenadapt="coverall")]
[playMusic(intro="$suspenseful_intro",key="$suspenseful_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "l", name = "avg_npc_2177_1#1$1",focus="r")]
[charslot(slot = "r", name = "avg_npc_2187_1#1$1",focus="r")]
[name="“研讨会”成员"]你再说一遍！
[charslot(slot = "l", name = "avg_npc_2177_1#5$1",focus="l")]
[name="法杰伊"]“近卫军”不愿给列昂尼德收尸。这次听清楚了吗？
[charslot(slot = "r",focus="r")]
[name="“研讨会”成员"]收尸？他现在可是正靠着壁炉嘲笑你这个蠢货！
[name="“研讨会”成员"]你想在这里等一辈子，为了半盒罐头、几束柴薪大打出手——
[name="“研讨会”成员"]从你嚷着要武力营救拉列亚开始，我就知道“近卫军”都是成事不足的废物！
[charslot(slot = "l", name = "avg_npc_2177_1#1$1",focus="l")]
[name="法杰伊"]那你们去给那个管事的下跪吧，我倒要看看你们是真能出去，还是会像那个“小个子”一样给送回来。
[charslot(slot = "r",focus="r")]
[name="“研讨会”成员"]我们走——
[dialog]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[charslot(slot = "r",posfrom="0,0",posto="150,0",afrom=1,ato=0, duration=1.2)]
[Delay(time=1.5)]
[charslot]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot = "m", name = "avg_1051_headb2_1#9$1", block=true)]
[name="凛冬"]站住！
[charslot(slot = "m", name = "avg_1051_headb2_1#9$1")]
[name="凛冬"]你们想去哪？还觉得混混头子会听你们的话？
[Dialog]
[charslot]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[charslot(slot = "m", name = "avg_194_leto_1#4$1",duration=1.2)]
[Delay(time=1.2)]
[name="烈夏"]果然你们还是这副老样子......
[charslot(slot = "m", name = "avg_npc_2187_1#1$1")]
[name="“研讨会”成员"]罗莎琳？你怎么来了？
[charslot(slot = "m", name = "avg_194_leto_1#4$1")]
[name="烈夏"]我是来帮索尼娅的，顺便来拦着你们送死，笨蛋！
[charslot(slot = "m", name = "avg_npc_2177_1#1$1")]
[name="法杰伊"]哼，你管他们做什么......
[name="法杰伊"]昨天那个叫费佳的，把“小个子”的尸体背回来的时候，他们还在说风凉话。
[Dialog]
[charslot]
[charslot(slot = "r", name = "avg_npc_2187_1#1$1",focus="l")]
[charslot(slot = "l", name = "avg_npc_2155_1#1$1",focus="l")]
[name="忧郁的青年"]......同学，那里确实很凶险。那些混混收了钱也不会让你们走的。
[charslot(slot = "r", name = "avg_npc_2187_1#1$1",focus="r")]
[name="“研讨会”成员"]你说的就对？你算老几？你亲眼看见“小个子”贿赂他们了？
[charslot(slot = "l", name = "avg_npc_2155_1#3$1",focus="l")]
[name="忧郁的青年"]我——
[charslot(slot = "r", name = "avg_npc_2187_1#1$1",focus="r")]
[name="“研讨会”成员"]“小个子”的口袋干净得连虱子都不愿意钻，哪可能动贿赂人的心思，肯定是越狱的时候被打死了。
[Dialog]
[charslot]
[charslot(slot = "r", name = "avg_1051_headb2_1#1$1")]
[name="凛冬"]这只是猜测，自称“十六人议会”的那群人，根本不像是可以沟通的样子。
[Dialog]
[charslot(slot = "l", name = "avg_npc_2182_1#1$1",posfrom="-120,0",posto="0,0",duration=0.8)]
[Delay(time=0.8)]
[charslot(slot = "l", focus="l")]
[name="担忧的学生"]索尼娅......你不在的时候，有个人过来送了封信，研讨会的瑙姆写的。
[name="担忧的学生"]瑙姆说，“十六人议会”的老大格罗莫夫，是个能说上话的体面人，只要钱给足了我们都可以走。
[charslot(slot = "r", name = "avg_1051_headb2_1#6$1",focus="r")]
[name="凛冬"]那封信在哪？
[charslot(slot = "l", focus="l")]
[name="担忧的学生"]这儿。
[Dialog]
[PlaySound(key="$d_avg_paper1", volume=0.8)]
[Delay(time=1)]
[Dialog]
[charslot]
[charslot(slot = "l",name = "avg_npc_2187_1#1$1")]
[name="“研讨会”成员"]够了吧？结束了吧？不要再妨碍我们离开这个鬼地方。
[Dialog]
[charslot(slot = "l",name = "avg_npc_2187_1#1$1",afrom=1,ato=1, posfrom = "0,0", posto = "60,0",duration=0.5)]
[Delay(time=0.3)]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "r", name = "avg_1051_headb2_1#1$1", posfrom = "0,0", posto = "30,0",duration=0.3)]
[Delay(time=0.3)]
[charslot(slot = "r", name = "avg_1051_headb2_1#1$1", focus="r")]
[name="凛冬"]......等等。
[Dialog]
[charslot(slot = "l",afrom=1,ato=1, posfrom = "60,0", posto = "80,0",duration =0.5)]
[Delay(time=0.6)]
[charslot(slot = "l",focus="l")]
[name="“研讨会”成员"]索尼娅，即便是你也没有拦住我们的理由！
[name="“研讨会”成员"]让开！
[charslot(slot = "l",focus="n")]
他莽撞地挤开人群，伸出手去抓凛冬的衣袖。
[charslot(slot = "R", name = "avg_1051_headb2_1#9$1", action="jump", posto="-160,0", power=0, times=1, duration=0.5)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_slap",volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[charslot(slot = "R", action="jump", posto="70,0", power=5, times=1, duration=1)]
[dialog]
[Delay(time=1)]
[charslot(slot = "l",focus="n")]
啪！一记响亮无比的耳光落在了他的脸上。
这记耳光像是按下了某个按钮，所有人的动作都凝滞了。
[dialog]
[charslot(slot="r",name = "avg_1051_headb2_1#7$1",focus="r")]
[name="凛冬"]给我醒醒！你看不明白这封信吗？
[charslot(slot="r",name = "avg_1051_headb2_1#9$1",focus="r")]
[name="凛冬"]研讨会天天写作，你们中谁的字迹能这么潦草？手抖得都快写出纸外了。最好的结果，就是他拿你们的命换了一顿饱饭。
[charslot(slot="l",focus="l")]
[name="“研讨会”成员"]这不是真的——
[charslot(slot="r",name = "avg_1051_headb2_1#9$1",focus="r")]
[name="凛冬"]你是真没有看出来，还是只愿沉溺于幻想，认为除了反抗之外还有别的办法离开这个封锁区？
[charslot(slot="l",focus="l")]
[name="“研讨会”成员"]......
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2182_1#1$1")]
[name="担忧的学生"]那，你说怎么办？
[charslot(slot="m",name = "avg_1051_headb2_1#4$1")]
[name="凛冬"]救人。
[charslot(slot="m",name = "avg_1051_headb2_1#9$1")]
[name="凛冬"]如今，有这封信和“小个子”的事，已经能够说明“十六人议会”的危险性了，列昂尼德带走一堆人去送死，我们不能坐视不管。
[charslot(slot="m",name = "avg_1051_headb2_1#9$1")]
[name="凛冬"]只有一个人活着，我就会带回来一个人；如果他们都活着，我就带回来所有人。
[charslot(slot = "m", name = "avg_npc_2177_1#5$1")]
[name="法杰伊"]......索尼娅，你也不想活了？
[name="法杰伊"]被抓了只能说明他们又蠢又弱，活该去死——
[charslot(slot="m",name = "avg_1051_headb2_1#7$1")]
[name="凛冬"]闭上你的嘴，法杰伊。
[charslot(slot="m",name = "avg_1051_headb2_1#9$1")]
[name="凛冬"]我听够了你们无休止地侮辱自己的同伴，想保住大家的命，就必须团结。
[charslot(slot = "m", name = "avg_npc_2177_1#1$1")]
[name="法杰伊"]团结？哈，当年乌萨斯之所以能建成，就是因为它把研讨会这种软骨头一个个地丢进了河里！
[charslot(slot="m",name = "avg_1051_headb2_1#11$1")]
[name="凛冬"]所以现在乌萨斯自己也被丢进河里，它还把你拽了下来，不是吗？
[charslot(slot = "m", name = "avg_npc_2177_1#3$1")]
[name="法杰伊"]......
[charslot(slot="m",name = "avg_1051_headb2_1#1$1")]
[name="凛冬"]在这里，没有什么“近卫军”“研讨会”，没有贵族和平民。
[charslot(slot="m",name = "avg_1051_headb2_1#1$1")]
[name="凛冬"]在那些自称“十六人

... (全文24448字符)
```

### level_act51side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[Background(image="49_g12_diving",screenadapt="coverall")]
[BackgroundTween(image="49_g12_diving", duration=10, xScaleFrom=1, yScaleFrom=1, xScaleTo=1.08, yScaleTo=1.08, xFrom=0, xTo=-45,yFrom=0, yTo=-25, block=false)]
[PlaySound(key="$d_avg_marshbubble", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1.5)]
咕咚。咕咚。
我盯着饮水机里的气泡，它们不断上涌、破碎。
有很多人正在走出那间沉闷的大厅，在仲裁人宣布暂停会议的时间里活动一下膝盖，顺便发表自己的见解。
[dialog]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[PlaySound(key="$d_avg_lqudrppg", volume=1)]
[Delay(time=1)]
恍惚间，水溢了出来，溅到地上。身后那位贵妇人厌烦地躲避着，生怕那些“来自萨米的纯净雪水”打湿她过气的皮靴。
天哪，我曾经也有双一模一样的鞋子......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_carriagegoaway", volume=0.8)]
我赶紧转动轮椅，试图逃开。
[dialog]
[delay(time=1)]
[Background(image="72_g10_hallway",screenadapt="coverall")]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[dialog]
[charslot(slot = "m", name = "avg_npc_2176_1#4$1", duration=0.8, block=true)]
[Delay(time=1)]
[name="英俊的贵族男性"]是你吗？瓦尔瓦拉？
[name="英俊的贵族男性"]不可置信，你看上去......
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[Background(image="72_g11_schoolway",screenadapt="coverall")]
[charslot(slot = "m", name = "avg_npc_2181_1#1$1")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_avg_bookdrop1", volume=1)]
[Delay(time=1)]
[name="瓦尔瓦拉"]帮我拿着这些书。它们太沉了！
[name="瓦尔瓦拉"]我要把力气留给晚上的剧本朗读会......不，你不能来！这是学生小组内部的活动。
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[Background(image="72_g10_hallway",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[name="瓦尔瓦拉"]......这让你很意外吗？
[charslot(slot = "m", name = "avg_npc_2176_1#3$1")]
[name="英俊的贵族男性"]不，瓦尔瓦拉，我不是这个意思。
[charslot(slot = "m", name = "avg_npc_2176_1#2$1")]
[name="英俊的贵族男性"]我们可是从小就认识的好朋友。贵族之间的友谊没那么容易破裂。
[Dialog]
[charslot]
[name="瓦尔瓦拉"]瞧瞧我这副样子，你还觉得我是一名贵族？
[charslot(slot = "m", name = "avg_npc_2176_1#3$1")]
[name="英俊的贵族男性"]这到底——
[Dialog]
[charslot]
[name="瓦尔瓦拉"]没听到刚才卓娅她们在说什么吗？
[name="瓦尔瓦拉"]那个仲裁人，为什么要扭曲我们所遭受的一切......
[Dialog]
[PlaySound(key="$d_avg_carriagegoaway", volume=0.8)]
[BackgroundTween(image="72_g10_hallway", duration=1.3, xScaleFrom=1, yScaleFrom=1, xScaleTo=1.07, yScaleTo=1.07,ease="InQuart", block=false)]
[Delay(time=1.3)]
[charslot(slot = "m", name = "avg_npc_2175_1#1$1", bstart=0.1,bend=0.7,posfrom="0,-100",posto="0,-100",duration=1.5, block=true)]
[Delay(time=2)]
[name="瓦尔瓦拉"]呵，呵呵。你是在看我的裤子吗？
[name="瓦尔瓦拉"]没关系，你看得再久，我的腿也长不出下半截。
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2176_1#3$1")]
[name="英俊的贵族男性"]天哪......
[name="英俊的贵族男性"]瓦尔瓦拉......这简直......天哪！
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="72_g5_blockalley",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(intro="$lostmemory_intro",key="$lostmemory_loop", volume=0.6)]
[charslot(slot = "l", name = "avg_npc_2166_1#1$1",focus="l")]
[charslot(slot = "r", name = "avg_npc_2167_1#1$1",focus="l")]
[name="“十六人议会”暴徒A"]投票结果出来了吗？
[charslot(slot = "r",focus="R")]
[name="“十六人议会”暴徒B"]出来了。
[name="“十六人议会”暴徒B"]老大决定，以后我们都叫“十六勇士”。
[charslot(slot = "L",focus="L")]
[name="“十六勇士”暴徒A"]凭什么！我在古籍上看到过，最早追随伊戈尔大帝的那十六个人的头衔，就是议员的意思，“议会”才是对的！
[charslot(slot = "r",focus="R")]
[name="“十六勇士”暴徒B"]收收你那套没人信的理论吧......何况你都叫“议会”了，那肯定得尊重投票结果，现在大家都觉得“勇士”更好听。
[charslot(slot = "L",focus="L")]
[name="“十六勇士”暴徒A"]*乌萨斯粗口*，这钱是挣得越来越不开心了。
[name="“十六勇士”暴徒A"]除了改名字，还突然说每个人都要算战果，看谁处理的学生更多......
[charslot(slot = "r",focus="R")]
[name="“十六勇士”暴徒B"]少抱怨点啦，昨天看你闲了一天，又想挨老大的骂？
[charslot(slot = "L",focus="L")]
[name="“十六勇士”暴徒A"]别瞎说，昨晚我刚送走一个。
[charslot(slot = "r",focus="R")]
[name="“十六勇士”暴徒B"]谁啊？
[charslot(slot = "L",focus="L")]
[name="“十六勇士”暴徒A"]就是那个说自己是“纯正的圣骏堡贵族”的，叫什么列昂尼德·格拉什维利。
[name="“十六勇士”暴徒A"]我看了几遍圣骏堡的《贵族谱系》，都没见过这个家族，最后还是翻了编年史才知道，他们家就是普通的南方人而已。
[name="“十六勇士”暴徒A"]老大只让留着真正的贵族，我就把他处理掉了。
[charslot(slot = "r",focus="R")]
[name="“十六勇士”暴徒B"]唉......哪用那么麻烦，你听他口音，有一点圣骏堡的味道吗？
[charslot(slot = "L",focus="L")]
[name="“十六勇士”暴徒A"]口音？待在这个鬼地方那么久，我都快忘了本地人说话是什么调调了。
[name="“十六勇士”暴徒A"]喂，小子，你是圣骏堡人吗？
[Dialog]
[charslot]
[PlaySound(key="$d_avg_slap",volume=1)] 
[Delay(time=0.3)]
[PlaySound(key="$d_avg_male_scream",volume=1)] 
[Delay(time=1)]
他猛地一拍自己的屁股下方，那里竟传出一声惊叫——一个学生趴跪在地上，正给他当座椅。
[name="惊慌的学生"]我我、我、我是......我是圣骏堡的！
[name="惊慌的学生"]我口音是对的，我也有家族，大人放我出去吧！
[charslot(slot = "l", name = "avg_npc_2166_1#1$1",focus="l")]
[charslot(slot = "r", name = "avg_npc_2167_1#1$1",focus="l")]
[name="“十六勇士”暴徒A"]看我这记性......你在当椅子的时候是不能说话的，不然一会儿老大看到又要骂我了。
[name="“十六勇士”暴徒A"]好好闭上嘴，行吗？这一小时你能安安静静的，今天就不送你走了。
[charslot(slot = "r",focus="R")]
[name="“十六勇士”暴徒B"]得了得了，学生们也不容易，天天都要被你吓唬。
[charslot(slot = "l", name = "avg_npc_2166_1#1$1",focus="l")]
[name="“十六勇士”暴徒A"]还教育起我了？
[name="“十六勇士”暴徒A"]你倒好，坐在尸体上面，也不嫌硬。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_tear",volume=1)] 
[Blocker(a=0.2, r=0.92, g=0.4, b=0.3, fadetime=0.6, block=true)]
[Blocker(a=0, r=0.92, g=0.4, b=0.3, fadetime=0.4, block=true)]
听了同伴的话，暴徒抽出了插在“坐垫”上的刀，刀下冒出温热的鲜血。
[charslot(slot = "l", name = "avg_npc_2166_1#1$1",focus="r")]
[charslot(slot = "r", name = "avg_npc_2167_1#1$1",focus="r")]
[name="“十六勇士”暴徒B"]反正我喜欢盘腿坐着，死的活的都

... (全文28936字符)
```

### level_act51side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="72_g13_nobleroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[charslot(slot="m",name="avg_197_poca_1#4$1",duration=1.5)]
[delay(time=2)]
[name="早露"]......
[charslot(slot="m",name="avg_npc_2173_1#1$1")]
[name="沃伦佐娃夫人"]我必须重申一次，孩子。
[name="沃伦佐娃夫人"]如果你只是来还书，仍不愿考虑我先前的建议，那么你可以把书放在那边的壁炉上，然后离开。
[charslot(slot="m",name="avg_197_poca_1#5$1")]
[name="早露"]难道只要我不同意您的办法，您就真的连一句旁的话也不愿和我说了吗？
[charslot(slot="m",name="avg_npc_2173_1#1$1")]
[name="沃伦佐娃夫人"]放在其他时候，即使你因着年轻人可爱的轻率做出再多糊涂的选择，我都能继续同你促膝长谈，直到深夜。
[name="沃伦佐娃夫人"]毕竟，我的确错过了许多。关于你，关于你父母，关于你们在切城的经历......
[charslot(slot="m",name="avg_197_poca_1#4$1")]
[name="早露"]现在我同样能将这些都告诉您。
[charslot(slot="m",name="avg_npc_2173_1#1$1")]
[name="沃伦佐娃夫人"]可现在我却没有资格去听。
[name="沃伦佐娃夫人"]面对关乎生死的问题，我无法说服你接受我的安排——离开圣骏堡避避风头，或者至少提交一份对自己有利无害的证词。
[name="沃伦佐娃夫人"]我无法保护你，也就无颜面对你的父母，那我又有什么资格从你这里了解有关他们的任何事情？
[charslot(slot="m",name="avg_197_poca_1#16$1")]
[name="早露"]不是这样的，夫人——
[charslot(slot="m",name="avg_npc_2173_1#1$1")]
[name="沃伦佐娃夫人"]这本书，你读了吗？
[charslot(slot="m",name="avg_197_poca_1#8$1")]
[name="早露"]我读了，我全都读了，我已经明白您为什么要将它借给我。
[charslot(slot="m",name="avg_npc_2173_1#1$1")]
[name="沃伦佐娃夫人"]它的扉页上写着什么？
[charslot(slot="m",name="avg_197_poca_1#2$1")]
[name="早露"]“世上没有任何主义，值得人们用美好的生活去交换。”
[charslot(slot="m",name="avg_npc_2173_1#1$1")]
[name="沃伦佐娃夫人"]是的，是的。雅科夫·彼得洛夫的《忏悔录》，在他死后由其家人整理出版，一本背叛者用死亡换来的经验之谈。所以，我真的不明白......
[name="沃伦佐娃夫人"]如果你知道已经有人为这经验付出过生命的代价，而自己还能有所选择，那又为何......一定要重蹈覆辙呢？
[name="沃伦佐娃夫人"]难道一定要在你行将就木，甚至是像他一样在牢狱中咽下鲜血的时候，你才能意识到自己所坚信的只是注定被历史遗忘的瞬间？
[charslot(slot="m",name="avg_197_poca_1#8$1")]
[name="早露"]夫人，我......
[charslot(slot="m",name="avg_npc_2173_1#1$1")]
[name="沃伦佐娃夫人"]告诉我吧，孩子，告诉我为什么。
[charslot(slot="m",name="avg_197_poca_1#9$1")]
[name="早露"]......说实在的，我也问过我自己。可如果......
[name="早露"]......
[charslot(slot="m",name="avg_197_poca_1#5$1")]
[name="早露"]请原谅我的厚颜无耻，我还想提一个要求。
[name="早露"]如果我能按照您的办法出具这份证词，保全自己，您能答应我，对自治团里的其他成员也一视同仁吗？
[charslot(slot="m",name="avg_npc_2173_1#1$1")]
[name="沃伦佐娃夫人"]当然！只要你能按那些人想要的，在证词里列出特定人员的名字——
[charslot(slot="m",name="avg_197_poca_1#4$1")]
[name="早露"]好。那么，我会做的。
[name="早露"]我会向听证会提交一份这样的证词......
[charslot(slot="m",name="avg_197_poca_1#3$1")]
[name="早露"]一封“忏悔信”。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="66_g12_deitygrypherburgmeeting",screenadapt="coverall")]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.3, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_177",duration=0.5)]
[delay(time=1)]
[name="急切的贵族"]伯爵夫人？
[charslot(slot="m",name="avg_npc_2173_1#1$1")]
[name="沃伦佐娃夫人"]......啊，我在听。你想说什么？
[charslot(slot="m",name="avg_npc_177")]
[name="急切的贵族"]抱歉，我想提醒您，仲裁人刚才提到娜塔莉娅小姐了，一会儿需要您把她的证词递上去。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_2168_1#1$1",duration=1)]
[delay(time=2)]
[name="仲裁人"]下一位证人，娜塔莉娅·罗斯托娃小姐。出于特殊原因，她本人今日不会出席。
[name="仲裁人"]但是，她已提前申请，由现场某位人士代为诵读证词。
[charslot(slot="m",name="avg_npc_2173_1#1$1")]
[name="沃伦佐娃夫人"]仲裁人阁下——
[Dialog]
[charslot]
[charslot(slot="m",name="avg_405_absin_1#1$2",duration=1)]
[delay(time=2)]
[name="苦艾"]娜塔莉娅小姐在昨日将信件交付于我，请仲裁委员会诸位大人过目，并允许我诵读。
[charslot]
[SoundVolume(volume=0.6, channel="bgs",fadetime=2)]
当书记官接过苦艾手中的信件时，窃窃私议的声音越来越大，沃伦佐娃夫人感到无数目光汇集于自身，她摇了摇头。
[StopSound(channel="bgs", fadetime=2)]
[charslot(slot="m",name="avg_npc_2168_1#1$1")]
[name="仲裁人"]那么，请卓娅女士代为讲述娜塔莉娅小姐在此事中的见闻。
[charslot(slot="m",name="avg_405_absin_1#1$2")]
[name="苦艾"]“公正的仲裁委员会，以及受人敬仰的诸位大人，这是一封忏悔信......”
[name="苦艾"]“出于我的悔意，与这封信所涉及的敏感之事，除了不得不谈论的巴普洛维奇外，我不会提及任何大人的具体姓名。”
[charslot(slot="m",name="avg_npc_177")]
[name="急切的贵族"]（低声）夫人，这和我们说的——
[charslot(slot="m",name="avg_npc_2173_1#1$1")]
[name="沃伦佐娃夫人"]......先听她念完吧。
[charslot(slot="m",name="avg_405_absin_1#1$2")]
[name="苦艾"]“......我希望，这足以换取诸位的信任。”
[Dialog]
[PlaySound(key="$d_avg_paper1")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Subtitle(text="<i>“在舞会事件发生后不久，出于对索尼娅安危的深切忧虑，我托一位有影响力的人士帮忙，成功联系到了当天大多数被捕学生的家长。”</i>", x=300, y=330, alignment="center", size=24, delay=0.04, width=720)]
[Subtitle(text="<i>“我得知，所有擅闯萨列夫格勒区的‘罪犯’，都将被统一关押在卡托加区，也就是现在人们口中的‘封锁区’。”</i>", x=300, y=330, alignment="center", size=24, delay=0.04, width=720)]
[Subtitle(text="<i>“令我意外的是，尽管家长中不乏地位显赫的贵族，他们也难以获得封锁区内的确切消息。”</i>", x=300, y=330, alignment="center", size=24, delay=0.04, width=720)]
[Subtitle(text="<i>“其中一部分人，是考虑到自身身份敏感，不便直接涉足封锁区。于是，他们委托我作为所有人的代表，前往探视被捕学生。”</i>", x=300, y=330, alignment="center", size=24, delay=0.04, width=720)]
[Subtitle(text="<i>“他们向我推荐了封锁区的管理者——枢密官巴普洛维奇。为拜访他，隔日我便登上了隔绝卡托加区与外界的城墙。”</i>", x=300, y=330, alignment="center", size=24, delay=0.04, width=720)]
[Subtitle]
[stopmusic(fadetime=2)]
[delay(time=2)]
[Dialog]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$sjoyasorrow_intro",key="$sjoyasorrow_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_2158_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_197_poca_1#4$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_2158_1#1$1",focus="l")]
[name="巴普洛维奇"]......哈哈，我还见了一位您父亲的朋友，舒瓦洛夫男爵，当初他举债跑到切尔诺伯格搞投资，后来又一穷二白地回到圣骏堡。
[PlaySound(key="$e_atk_saw_n_1",volume=0.1)]
[name="巴普洛维奇"]但前天我们见面时，他被铐着双手，正由两位警官押着出城，要往东边送。我好奇问他，这是犯了多大的事儿，还要被流放？
[name="巴普洛维奇"]他神秘兮兮地凑到我耳边说，参加宴会的时候，他喊了一句“矿工万岁”。
[name="巴普洛维奇"]我惊讶地问他为什么，您猜他说什么？
[charslot(slot = "right", name = "avg_197_poca_1#4$1",focus="r")]
[name="早露"]抱歉，我猜不出来。
[charslot(slot = "left", name = "avg_npc_2158_1#6$1",focus="l")]
[name="巴普洛维奇"]他笑着回头，看向那两个押送他的警官，说：“被流放了，债主就找不到我了，哈哈哈哈。”
[charslot(slot = "right", name = "avg_197_poca_1#5$1",focus="r")]
[name="早露"]这真是，特别的见闻......如果我没有要事在身，或许听一天都不会疲惫。
[charslot(slot = "left", name = "avg_

... (全文20277字符)
```

### level_act51side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="66_g12_deitygrypherburgmeeting",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$darkness02_intro",key="$darkness02_loop", volume=0.6)]
[charslot(slot="m",name="avg_405_absin_1#1$2",duration=1)]
[delay(time=2)]
[name="苦艾"]“......之后，我对照名单，依次与各个学生见面。”
[name="苦艾"]“与索尼娅不同，他们被送到城墙边的办公室与我交谈，大多面带恐惧，什么都不敢说。”
[charslot(slot="m",name="avg_npc_177")]
[name="急切的贵族"]我受够了！仲裁人阁下，帝国的听证会怎能纵容如此荒谬的、针对一位清白贵族的侮辱？
[name="急切的贵族"]他曾是陛下亲封的枢密官，如果事实真如娜塔莉娅描述的那样，他又怎么可能取得这样的殊荣？
[name="急切的贵族"]任谁都能听出来，这封信名为忏悔，实为诘难，我们不能再被谣言牵着走了。
[name="急切的贵族"]据我所知，现场还有一份——
[charslot(slot="m",name="avg_405_absin_1#6$2")]
[name="苦艾"]这位大人，无论您对巴普洛维奇大人的“管理艺术”抱有怎样的欣赏态度，都请不要因此就把娜塔莉娅亲笔写下的血泪称为谣言。
[name="苦艾"]您不能因为我们此刻都在温暖的厅堂中对话，就否认外面正有人因饥寒交迫而战栗。
[charslot(slot="m",name="avg_405_absin_1#7$2")]
[name="苦艾"]毕竟，依照您的想法，如果世上真有那么多苦难，乌萨斯怎么可能繁荣数百年呢？
[charslot(slot="m",name="avg_npc_177")]
[name="急切的贵族"]卓娅女士，注意你的措辞。听证会尊重你烈士子女的身份，出于信任和对公正的索求让你来辅助作证，不是让你来这里侮辱贵族的！
[charslot(slot="m",name="avg_405_absin_1#6$2")]
[name="苦艾"]仲裁委员会明鉴，我分明是在维护一位真正的贵族，我决不容忍任何人轻率地用“谣言”去污蔑她。
[charslot(slot="m",name="avg_npc_177")]
[name="急切的贵族"]荒谬——
[charslot(slot="m",name="avg_npc_2168_1#1$1")]
[name="仲裁人"]安静！
[name="仲裁人"]卓娅女士，你的责任是代为陈述娜塔莉娅小姐的证词，事实判断是仲裁委员会才能做的。
[charslot(slot="m",name="avg_405_absin_1#1$2")]
[name="苦艾"]......抱歉，仲裁人阁下。
[name="苦艾"]如果诸位大人在意的是“忏悔”的部分，那么接下来就是了。
[name="苦艾"]还请仲裁人阁下允许我继续。
[charslot(slot="m",name="avg_npc_2168_1#1$1")]
[name="仲裁人"]记住，如果你继续试图对任何贵族的观点进行评判，那么我将不再允许你发言。
[name="仲裁人"]继续吧。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Subtitle(text="<i>“当我回到城中，向他们的父母汇报情况时，有的家长会多留我一会儿，想要了解更多有关他们孩子的情况。”</i>", x=300, y=330, alignment="center", size=24, delay=0.04, width=720)]
[Subtitle(text="<i>“为了寻找缓解封锁区内境况的契机，我必须要试探谁能够提供更多的帮助。”</i>", x=300, y=330, alignment="center", size=24, delay=0.04, width=720)]
[Subtitle(text="<i>“于是，我挑选了几位家长私下见面，刻意渲染了学生们所处境况的窘迫与凄惨。”</i>", x=300, y=330, alignment="center", size=24, delay=0.04, width=720)]
[Subtitle(text="<i>“最终，我找到了一位独生子被押的贵族，而他迫不及待地将我引荐给了他的上司。”</i>", x=300, y=330, alignment="center", size=24, delay=0.04, width=720)]
[Subtitle]
[Dialog]
[delay(time=1)]
[charslot(slot = "m", name = "avg_197_poca_1#4$1")]
[Background(image="72_g13_nobleroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[name="早露"]......以上就是我在封锁区内的全部见闻，议员阁下。
[charslot(slot = "m", name = "avg_197_poca_1#5$1")]
[name="早露"]若是继续坐视巴普洛维奇大人的行为，甚至继续放任他们使用大型武器，这一定会在不久后酿成无法挽回的惨剧。
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2162_1#1$1",duration = 1)]
[delay(time=2)]
[name="某位议员"]娜塔莉娅小姐，从你的表述来看，你似乎希望议会能公布巴普洛维奇的罪行，从而剥夺他的官秩，甚至将其撤职。
[charslot(slot = "m", name = "avg_197_poca_1#12$1")]
[name="早露"]我只是希望能阻止他。
[name="早露"]议员阁下，请原谅我话语的直接。我对议会既无意评判，也产生不了影响，但我能想象这其中会有多大阻力。
[charslot(slot = "m", name = "avg_npc_2162_1#1$1")]
[name="某位议员"]那么，或许我们就应该答应他的要求，暂缓抛下封锁区地块的决议，然后他就会如约释放学生们。
[name="某位议员"]你相信他会兑现承诺吗？
[charslot(slot = "m", name = "avg_197_poca_1#3$1")]
[name="早露"]......不，我无法信任巴普洛维奇大人。
[charslot(slot = "m", name = "avg_197_poca_1#4$1")]
[name="早露"]而且我也明白，您之所以会这么问我，是因为您同样无法信任他。
[charslot(slot = "m", name = "avg_npc_2162_1#2$1")]
[name="某位议员"]哈哈，你很聪明，也许你和我的女儿会聊得来。
[charslot(slot = "m", name = "avg_npc_2162_1#1$1")]
[name="某位议员"]我的下属也向我报告过，你从封锁区回来后并没有按照他的要求，煽动家长们一同想办法保留封锁区。
[name="某位议员"]反之，你选择从家长们的身份、状况和性格入手，找到了我。
[name="某位议员"]你认为我是能左右事情的关键，也是你目前能接触到的、最有政治影响力的对象。
[charslot(slot = "m", name = "avg_197_poca_1#4$1")]
[name="早露"]您的判断全都正确，我的想法，那些青涩的算计，在您面前一览无余。
[name="早露"]可是阁下，我只是无法不去想我的朋友们。就在我们交谈的时候，她们正在封锁区里遭受磨难，每一秒都有丧命的风险。
[name="早露"]我知道您的顾虑，是源于我想法的不现实。
[name="早露"]所以阁下，我并不奢望能立即处罚巴普洛维奇大人，但至少我们应该争取改善封锁区内学生们的待遇，并解除封锁区的重型武装。
[charslot(slot = "m", name = "avg_npc_2162_1#3$1")]
[name="某位议员"]......很遗憾，当下的议会大概无法满足这些请求。
[charslot(slot = "m", name = "avg_197_poca_1#4$1")]
[name="早露"]巴普洛维奇大人曾和我提到，他得到了议会当中许多贵族朋友的支持。
[charslot(slot = "m", name = "avg_npc_2162_1#1$1")]
[name="某位议员"]你恐怕说漏了一个“旧”字。或者说，“军事贵族”。
[name="某位议员"]开诚布公地说，乌萨斯贵族间的阵营对立，恐怕对玻利瓦尔人都谈不上是什么秘密了，你不必如此谨慎。
[name="某位议员"]由于近来的动乱，每一个决议，每一条规章，谁今天在议会上逞了口舌之快，谁明日被皇帝陛下夸奖，处处都是党同伐异，必分高低。
[name="某位议员"]仅是帝国议会，就有四百多名议员，他们大都家世显赫，功勋卓著。
[name="某位议员"]居住在圣骏堡的、姓氏被计入了《贵族谱系》的世袭贵族，有将近八百人。
[name="某位议员"]至于那些有影响力的荣誉市民，更是不计其数......每个人的态度都很复杂。
[charslot(slot = "m", name = "avg_npc_2162_1#8$1")]
[name="某位议员"]如果世事都像切薄饼一样能轻易分成两半......我想乌萨斯也不会走到现在这种局面。
[charslot(slot = "m", name = "avg_197_poca_1#5$1")]
[name="早露"]您是想告诉我......
[name="早露"]即使是新贵族，其中也有人支持巴普洛维奇大人。现在之所以无法阻止他，也是因为他有许多有权势的支持者。
[charslot(slot = "m", name = "avg_npc_2162_1#1$1")]
[name="某位议员"]所以即使是我，甚至是议长，都无法在这件事情上跨过众人的意见，给你们提供任何实质性的帮助。
[charslot(slot = "m", name = "avg_197_poca_1#4$1")]
[name="早露"]能有幸与您交流，就已经是莫大的帮助了。
[name="早露"]我的目标不会改变，要真正解救索尼娅以及封锁区里的人们，就必须尽量干扰巴普洛维奇大人。
[charslot(slot = "m", name = "avg_npc_2162_1#2$1")]
[name="某位议员"]判断不错，但只有判断是不够的。
[name="某位议员"]在年轻的时候，人们很容易知道自己应该反对什么，却很难知道自己应该去做什么。
[name="某位议员"]娜塔莉娅小姐，你会怎么做呢？
[charslot(slot = "m", name = "avg_197_poca_1#2$1")]
[name="早露"]......如果我能调查清楚不同人支持他的原因，并且联系上一些潜在的“朋友”......
[charslot(slot = "m", name = "avg_197_poca_1#8$1")]
[name="早露"]您提醒过我，每一个人的态度都是复杂的。换种角度说，即使是旧贵族，即使曾经是他的盟友，也可能会在特定情况下态度发生偏移。
[charslot(slot = "m", name = "avg_npc_2162_1#2$1")]
[name="某位议员"]你把那句话看作是“提醒”，这可真是......
[name="某位议员"]等事情解决之后，请一定要再来坐坐。等阿洛达没在做她自己的事的时候吧，也许......
[charslot(slot = "m", name = "avg_197_poca_1#4$1")]
[name="早露"]您说什么？
[charslot(slot = "m", name = "avg_npc_2162_1#1$1")]
[name="某位议员"]没什么。
[name="某位议员"]娜塔莉娅小姐，我这里有一个消息，是即使维特议长明令禁止，也已经在部分贵族中传播开来的。
[name="某位议员"]冬季舞会之后，出于一些原因，皇帝陛下没有返回宫殿。
[charslot(slot = "m", name = "avg_197_poca_1#12$1")]
[name="早露"]......
[charslot(slot = "m", name = "avg_npc_2162_1#1$1")]
[name="某位议员"]截至目前，议长暗中派人调查，却始终没有发现任何线索，排除到最后，就只剩下一个地方。
[charslot(slot = "m", name = "avg_npc_2162_1#9$1")]
[name="某位议员"]一个此时难以查证的地方。
[charsl

... (全文18063字符)
```

### level_act51side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[charslot]
[Background(image="72_g2_sjbstreet_n",screenadapt="coverall",xScale=1.2, yScale=1.2,x=50,y=50)]
[Delay(time=1)]
[PlaySound(key="$d_avg_steamburst", volume=0.8)]
[Delay(time=0.8)]
[PlaySound(key="$d_avg_audience_chaos",volume=0.5)]
[Delay(time=0.8)]
[PlaySound(key="$d_avg_male_scream", volume=0.5)]
[Delay(time=0.3)]
[PlaySound(key="$d_avg_tinnitus",volume=0, channel="z", loop=true)]
[SoundVolume(volume=0.8, channel="z",fadetime=1)]
[name="？？？"]......安娜！前面的街灯也都灭了，该死！这是为什么——
[name="？？"]先别管那么多。
[name="？？"]烈夏，拿上这根火把，到后面喊那些没跟上的学生，让他们跟着亮光朝我这个方向慢慢走过来，注意摔倒的同伴。
[name="？？？"]清楚了，我这就去！
......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[focusout(type="bg", from=0, to=1, duration=0.01, block=false)]
[backgroundTween(yFrom =50,yTo=20,xFrom =50,xTo=20, duration=3.5,ease="OutQuad",block=false)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=false)]
[Delay(time=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[name="？？"]你怎么在这儿......快醒醒！我们要走了！
[name="？？"]奥尔佳！
[dialog]
[StopSound(channel="z", fadetime=2)]
[playMusic(intro="$newhope01_intro",key="$newhope01_loop", volume=0)]
[MusicVolume(volume=0.6, fadetime=2)]
[bgeffect(name="$eb_dim_openeye",layer=1)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_2156_1#2$1")]
[Dialog]
[focusout(type="bg", from=1, to=0.5, duration=2, block=false)]
[Blocker(a=0.7, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",focus="n")]
[name="奥尔佳"]安、安娜......这是在哪？
[charslot(slot="m",name="avg_npc_2156_1#8$1",focus="m")]
[name="真理"]从萨列夫格勒区出来了。我们在外面的街道上，剩下的人都跟在后面。
[charslot(slot="m",name="avg_npc_2156_1#2$1",focus="m")]
[name="真理"]先别说这些了，有没有受伤？还能起身吗？
[charslot(slot="m",focus="n")]
[name="奥尔佳"]我的、我的左脚！
[charslot(slot="m",name="avg_npc_2156_1#11$1",focus="m")]
[name="真理"]......还有谁能搭把手？
[charslot(slot="m",focus="n")]
[Dialog]
真理下意识地想要咽下一口唾沫，可干涩的喉头只传来撕裂般的疼痛。她不知道自己迎着寒风走了多久。
圣骏堡的夜晚第一次让她感到陌生，除去少数几座城堡和高楼闪烁着点点灯光外，路灯、民居......全城都湮没在了黑暗之中。
但现在不是思考原因的时候。她高举火把，喘着粗气左右环视，眼中的火光摇曳，在这不寻常的昏暗里辨认着她熟悉的脸庞。
[charslot(slot="m",name="avg_npc_2156_1#11$1",focus="m")]
[name="真理"]谢尔戈，过来一下。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_2176_1#4$1")]
[charslot(slot = "m", action="shake", power=1, times=10, duration=0.3)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_2176_1#1$1",posfrom="0,0",posto="-50,0",afrom=1,ato=1,duration=1)]
[Delay(time=1)]
[name="谢尔戈"]我......我，她——
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_2156_1#2$1")]
[charslot(slot="r",name="avg_npc_2176_1#1$1",posfrom="60,0",posto="0,0",duration=1)]
[Delay(time=1.1)]
[charslot(slot="l",name="avg_npc_2156_1#9$1",focus="l")]
[name="真理"]帮我搭着奥尔佳的手臂，有什么事走出这片鬼地方再说。
[charslot(slot="r",name="avg_npc_2176_1#1$1",focus="r")]
[name="谢尔戈"]那......我们现在去哪？
[charslot(slot="l",name="avg_npc_2156_1#9$1",focus="l")]
[name="真理"]......剧院。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[focusout(type="bg", from=0.5, to=0, duration=0.01, block=false)]
[Background(image="66_g12_deitygrypherburgmeeting",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_2159_1#7$1")]
[name="奥尔佳"]......所以在当晚我没有直接回家，而是随着学生队伍去了废弃剧院。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]奥尔佳小姐，由于前三位证人的证词都出现了程度不一的离题——
[name="仲裁人"]为了避免浪费不必要的时间，我需要你接下来仅围绕事实本身进行陈述。
[name="仲裁人"]在听证会的事先调查中，你明确地向仲裁委员会声明，因为行动超出了你的预期，你选择与他们决裂。
[name="仲裁人"]但很快，安娜带领学生绑架了你，并利用你的失踪诱骗了特里波列夫公爵。是不是？
[charslot(slot="m",name="avg_npc_2159_1#8$1")]
[name="奥尔佳"]......是。
[charslot(slot="m",name="avg_npc_2159_1#8$1")]
[name="奥尔佳"]因此我也见证了安娜他们是如何谋划，并参与到索尼娅的暴力行动中的。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_crwddiscuss_inside",volume=0, channel="f", loop=true)]
[SoundVolume(volume=0.5, channel="f",fadetime=2)]
[name="刻薄的贵族"]终于来了个像样的证人，还是特里波列夫家族的人可靠。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]很好。
[name="仲裁人"]请你继续陈述，听证会需要更多真实的细节——安娜是如何帮助索尼娅，对封锁区秩序实施破坏的？
[Dialog]
[charslot]
奥尔佳局促地点点头，双手在证人台的边沿摩挲，耳边传来熟悉的咳嗽声——显然父亲比自己更加紧张。
[charslot(slot="m",name="avg_npc_2159_1#10$1")]
[name="奥尔佳"]在剧院里，我们惊吓过度，已经失去了判断力，除了那些哭泣的人，每个人都在互相指责......
[stopmusic(fadetime=2)]
[StopSound(channel="f", fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="72_g3_podium",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[charslot(slot = "l", name = "avg_npc_2177_1$2",focus="L")]
[charslot(slot = "r", name = "avg_npc_2187_1#1$1",focus="L")]
[name="“近卫军”成员"]......该死，这通讯设备怎么全没声音了？
[charslot(slot = "r", focus="R")]
[name="“研讨会”成员"]别摆弄你那破耳机了，“近卫军”。“伟大行动”的发起者，你们还有什么话说？
[charslot(slot = "l",focus="L")]
[name="“近卫军”成员"]不要乱讲，我们明明打算——
[charslot(slot = "r", focus="R")]
[name="“研讨会”成员"]打算劫狱？看到了吧，我们没带武器都被揍成了这样，要是真信了你们的鬼话，我们都得死！
[name="“研讨会”成员"]就是你们最开始煽动暴力行动的，不要狡辩！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_2178_1#6$1")]
[name="失望的学生"]问题根本不在这次行动上，明明是你们不相信国家，盲目扩大矛盾，非要在萨列夫格勒区喊什么批评皇帝陛下的口号。
[name="失望的学生"]我们明明是去向各位大人请愿的，原本想着，只要把动静闹大，传到陛下耳朵里，他一定会钦命稽查员帮我们解决此事。
[charslot(slot="m",name="avg_npc_2178_1#3$1")]
[name="失望的学生"]这下倒好，我们哪还能回头啊......
[charslot(slot="m",name="avg_npc_2176_1#5$1")]
[name="谢尔戈"]和我们都没有关系，都怪学生近卫军他们一意孤行，让法杰伊对这件事负责！
[Dialog]
[charslot]
[charslot(slot = "l", name = "avg_npc_2177_1$2",focus="L")]
[charslot(slot = "r", name = "avg_npc_2187_1#1$1",focus="L")]
[name="“近卫军”成员"]那怎么没见你投反对票？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_2176_1#1$1")]
[name="谢尔戈"]认识我的人都知道，我一直支持索尼娅和学生自治团，还不是因为你们摆出一副不听话就开除清算的鬼样子——
[Dialog]
[charslot]


... (全文21909字符)
```

### level_act51side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="66_g12_deitygrypherburgmeeting",screenadapt="coverall")]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]奥尔佳小姐，相信所有人都能察觉，当晚安娜·莫罗佐娃实际上夺取了属于你的权力。
[name="仲裁人"]但我好奇的是，你为什么没有像其他同学那样选择离开大会？
[charslot(slot="m",name="avg_npc_2159_1#8$1")]
[name="奥尔佳"]......
[charslot(slot="m",name="avg_npc_2159_1#8$1")]
[name="奥尔佳"]是因为——
[Dialog]
[charslot]
[playsound(key="$d_avg_clothmovement")]
[charslot(slot="m",name="avg_npc_2171_1#1$1",duration=0.4,posfrom = "0,-50", posto = "0,0")]
[Delay(time=0.4)]
[name="特里波列夫公爵"]仲裁人阁下，我建议听证会还是专注于对具体事件进行问询。
[charslot(slot="m",name="avg_npc_2159_1#10$1")]
[name="奥尔佳"]......我被当时的氛围冲昏了头脑，丧失了基本的判断力。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]那么奥尔佳小姐，你需要说明你为何与安娜等人决裂，讲清楚安娜一行人是如何绑架、胁迫你的。
[charslot(slot="m",name="avg_npc_2159_1#8$1")]
[name="奥尔佳"]......是，阁下。
[charslot(slot="m",name="avg_npc_2159_1#8$1")]
[name="奥尔佳"]第一夜，几乎所有人都选择了留在剧院，自愿帮助受伤的同学，为如何打听被抓同学的消息出谋划策。
[charslot(slot="m",name="avg_npc_2159_1#7$1")]
[name="奥尔佳"]但在第二天，情况就发生了变化——
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="72_g3_podium",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[charslot(slot = "l", name = "avg_npc_2176_1#1$1",posfrom="80,0",posto="80,0")]
[charslot(slot = "r", name = "avg_npc_2159_1#8$2")]
[Delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_2176_1#2$1",afrom=1,ato=1,posfrom="80,0",posto="0,0",duration=1.2)]
[Delay(time=1.2)]
[charslot(slot = "l",focus="l")]
[name="谢尔戈"]......好了奥尔佳，药都抹上了。
[name="谢尔戈"]虽然有些不好看，但为了尽早痊愈，你多忍一忍。
[charslot(slot = "r", name = "avg_npc_2159_1#8$2",focus="r")]
[name="奥尔佳"]......
[charslot(slot = "r", name = "avg_npc_2159_1#8$2",focus="r")]
[name="奥尔佳"]今天怎么是你？拉达呢？
[charslot(slot = "l",name = "avg_npc_2176_1#1$1",focus="l")]
[name="谢尔戈"]昨晚你睡得早，后面娜塔莉娅来剧院了，还有一位没见过的沃尔珀，那位沃尔珀和安娜她们说了些话，就带走了拉达。
[charslot(slot = "r", name = "avg_npc_2159_1#4$2",focus="r")]
[name="奥尔佳"]那其他人去哪了，怎么剧院都空了？
[charslot(slot = "l",focus="l")]
[name="谢尔戈"]我也不清楚，但安娜好像给大家安排了任务。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_open_door", volume=1)]
[Delay(time=1.2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_2156_1#2$1", duration=0.8, block=true)]
[Delay(time=1)]
[name="真理"]......当务之急，是弄清楚学生们被关押在哪。
[charslot(slot = "m", name = "avg_npc_2156_1#8$1")]
[name="真理"]按照这份统计名单，从他们的父母入手，或许能找到突破口。
[charslot(slot = "m", name = "avg_197_poca_1#3$1")]
[name="早露"]嗯，我也会去找家族的熟人打听消息，如果你有新的线索记得及时给我，我来出面查证。
[charslot(slot = "m", name = "avg_197_poca_1#4$1")]
[name="早露"]保重，安娜。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_197_poca_1#4$1",posfrom="0,0",posto="150,0",afrom=1,ato=0,duration=1.5)]
[Delay(time=1.5)]
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2156_1#6$1",posfrom="30,0",posto="0,0",duration=1,afrom=1,ato=1)]
[Delay(time=1)]
[name="真理"]嗯？你们怎么在这？
[Dialog]
[charslot]
[charslot(slot = "l", name = "avg_npc_2176_1#1$1",focus="l")]
[charslot(slot = "r", name = "avg_npc_2159_1#8$2",focus="l")]
[name="谢尔戈"]昨晚奥尔佳睡在舞台边，今早我来剧院时正好看到她醒来，所以就地帮她换药了。
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2156_1#8$1")]
[name="真理"]......也好。
[charslot(slot = "m", name = "avg_npc_2156_1#8$1")]
[name="真理"]谢尔戈，帮我把奥尔佳抬到三楼的排练室，她需要好好休息。
[Dialog]
[charslot]
[charslot(slot = "l", name = "avg_npc_2176_1#1$1",focus="r")]
[charslot(slot = "r", name = "avg_npc_2159_1#3$2",focus="r")]
[name="奥尔佳"]......安娜，或许我应该先回一趟家。
[charslot(slot = "r", name = "avg_npc_2159_1#1$2",focus="r")]
[name="奥尔佳"]我恢复得很好，已经可以自己走动了。即使我没有信心能让父亲帮大家脱罪，但至少也能问出他们被关押的地方。
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2156_1#1$1")]
[name="真理"]别担心，他们被关押的地方，我已经有线索了。
[charslot(slot = "m", name = "avg_npc_2156_1#8$1")]
[name="真理"]至于你本人，最好还是留下来安心养伤。如果你以现在这副模样回家，指不定会传出多少流言。
[charslot(slot = "m", name = "avg_npc_2156_1#8$1")]
[name="真理"]许多受伤的同学也选择留在这里接受照顾，他们会给家里人写信，再由我找人送出去。
[Dialog]
[charslot]
[charslot(slot = "l", name = "avg_npc_2176_1#1$1",focus="r")]
[charslot(slot = "r", name = "avg_npc_2159_1#9$2",focus="r")]
[name="奥尔佳"]......
[charslot(slot = "l", focus="l")]
[name="谢尔戈"]那奥尔佳，我去把担架取过来。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="66_g12_deitygrypherburgmeeting",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(intro="$newhope01_intro",key="$newhope01_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_2159_1#8$1")]
[name="奥尔佳"]......他们将我转移到了一间屋子里，并声称要给我提供保护。
[charslot(slot="m",name="avg_npc_2159_1#8$1")]
[name="奥尔佳"]但很快，我就见识到了什么叫“保护”——拿着消防斧的同学昼夜轮班，守在监禁我的屋子门口。
[charslot(slot="m",name="avg_npc_2159_1#7$1")]
[name="奥尔佳"]我向他们搭话，却被告知他们不能与我交流......我也就放弃了给父亲写信的想法，因为他们不可能会替我送出去。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]因此你意识到自己是被安娜等人软禁了？
[charslot(slot="m",name="avg_npc_2159_1#8$1")]
[name="奥尔佳"]是的。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]你清楚安娜的动机吗？
[charslot(slot="m",name="avg_npc_2159_1#3$1")]
[name="奥尔佳"]我的猜测是，前一晚她在暗示要利用贵族时，我表现出了抗拒。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]在你看来，这是否能说明自治团对贵族的仇恨态度？索尼娅与无缚者同盟勾结也同样符合这一判断。
[charslot(slot="m",name="avg_npc_2159_1#8$1")]
[name="奥尔佳"]......是的。
[charslot(slot="m",name="avg_npc_2159_1#7$1")]
[name="奥尔佳"]因为她不止监禁了我，所有被她判断为可能泄密的不坚定者，以及......有利用价值的贵族，都遭受了和我类似的待遇。
[charslot(slot = "m", name = "avg_npc_2168_1#1$1")]
[name="仲裁人"]这之后，你是否有与外界沟通或者走出房门的机会？
[charslot(slot="m",name="avg_npc

... (全文28444字符)
```

### level_act51side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="72_g5_blockalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[playsound(key="$d_avg_soldiersstep", loop=true, channel="bgs")]
[Delay(time=2)]
[StopSound(channel="bgs", fadetime=2)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_1051_headb2_1#1$1",duration = 0.5)]
[delay(time=1)]
[name="凛冬"]......米科拉，你在干什么？
[charslot(slot = "m", name = "avg_npc_2177_1#1$1")]
[name="乌萨斯学生A"]报告，有人没跟上——
[charslot(slot = "m", name = "avg_1051_headb2_1#1$1")]
[name="凛冬"]所以你就放弃维持队伍左翼的队形？重新走一遍！
[Dialog]
[charslot]
[playsound(key="$d_avg_soldiersstep", loop=true, channel="bgs")]
[Delay(time=1)]
[StopSound(channel="bgs", fadetime=2)]
[Delay(time=0.5)]
[CameraShake(duration=0.2, xstrength=10, ystrength=10, vibrato=20, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_stickimp")]
[Blocker(a=0, r=0, g=0, b=0, afrom=0.8, rfrom=1, gfrom=1, bfrom=1, fadetime=0.3, block=true)]
[Delay(time=0.5)]
[CameraShake(duration=0.2, xstrength=15, ystrength=15, vibrato=20, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_metallicclick",channel="3")]
[Blocker(a=0, r=0, g=0, b=0, afrom=0.8, rfrom=1, gfrom=1, bfrom=1, fadetime=0.3, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_1051_headb2_1#1$1")]
[name="凛冬"]好，拿长枪上来，顶住我的盾牌，把我逼到角落里。
[charslot(slot = "m", name = "avg_npc_2179_1#1$1")]
[name="乌萨斯学生B"]报告索尼娅，你的力气太大了，我们推不动。
[charslot(slot = "m", name = "avg_1051_headb2_1#1$1")]
[name="凛冬"]不是你们推不动，是你们劲儿使得不够齐。
[charslot(slot = "m", name = "avg_1051_headb2_1#11$1")]
[name="凛冬"]记住，我们不是什么散兵游勇。乌萨斯不保护我们，所以我们每个人都要当彼此的堡垒。
[charslot(slot = "m", name = "avg_1051_headb2_1#1$1")]
[name="凛冬"]明白了吗？
[PlaySound(key="$d_avg_crwdcheerup")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot]
[name="众人"]明白！
[Dialog]
[charslot(slot = "r", name = "avg_1051_headb2_1#1$1")]
[Delay(time=0.5)]
[charslot(slot = "l", name = "avg_194_leto_1#1$1",posfrom = "-150,0", posto = "0,0",duration = 0.8)]
[Delay(time=1.3)]
[charslot(slot = "l", name = "avg_194_leto_1#1$1",focus="l")]
[name="烈夏"]嘿！冬将军，还在训练呢？
[charslot(slot = "r", name = "avg_1051_headb2_1#2$1",focus="r")]
[name="凛冬"]刚回来吗？辛苦啦。
[name="凛冬"]今天情况怎么样？
[charslot(slot = "l", name = "avg_194_leto_1#8$1",focus="l")]
[name="烈夏"]好消息，昨天还摆出来耀武扬威的大炮和重武器，今天全不见了。
[name="烈夏"]尼卡那边还发现，有些人在往外搬物资，看着像是些军火。
[name="烈夏"]娜塔莉娅她们成功了，索尼娅。
[charslot(slot = "r", name = "avg_1051_headb2_1#2$1",focus="r")]
[name="凛冬"]......不愧是她们。
[charslot(slot = "l", name = "avg_194_leto_1#8$1",focus="l")]
[name="烈夏"]还有，就像之前我们聊过的那样，格罗莫夫每晚都驻扎在封锁区内的某处营地，只有巴普洛维奇才住在城墙上面。
[name="烈夏"]进攻城墙前，我们可以先消灭那些混混的主力。
[charslot(slot = "r", name = "avg_1051_headb2_1#1$1",focus="r")]
[name="凛冬"]还要找到更多食物和其他补给品，有人发现他们的仓库吗？
[charslot(slot = "l", name = "avg_194_leto_1#9$1",focus="l")]
[name="烈夏"]没有......现在的粮食还能撑多久？
[charslot(slot = "r", name = "avg_1051_headb2_1#1$1",focus="r")]
[name="凛冬"]最多三天，无缚者同盟那边也快见底了，我们欠安托沙的已经太多。
[charslot(slot = "r", name = "avg_1051_headb2_1#11$1",focus="r")]
[name="凛冬"]关于食物的事，我搞砸过一次......我不能——
[charslot(slot = "l", name = "avg_194_leto_1#8$1",focus="l")]
[name="烈夏"]快握住我的手！冬将军，不会有事的，我们一定能挺过去。
[charslot(slot = "r", name = "avg_1051_headb2_1#4$1",focus="r")]
[name="凛冬"]得抓紧训练了，烈夏，我有预感，接下来的几天会决定我们的命运。
[charslot(slot = "l", name = "avg_194_leto_1#7$1",focus="l")]
[name="烈夏"]那现在愿意上战场的人......
[charslot(slot = "r", name = "avg_1051_headb2_1#1$1",focus="r")]
[name="凛冬"]出乎意料地多，这几天的行军训练很有成效，大家都看在眼里。其他人也愿意帮助我们去做医疗和后勤工作。
[charslot(slot = "r", name = "avg_1051_headb2_1#2$1",focus="r")]
[name="凛冬"]在我们这个年纪，最不肯向不公低头了，对吗？
[charslot(slot = "l", name = "avg_194_leto_1#8$1",focus="l")]
[name="烈夏"]哼，那也是你做得好。
[name="烈夏"]说起来，那个叫费佳的，他不是学生，也愿意参与行动吗？
[charslot(slot = "r", name = "avg_1051_headb2_1#1$1",focus="r")]
[name="凛冬"]嗯......我不知道能不能信任他。
[name="凛冬"]直到现在，他的来历也是个谜，但他很有决心。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="72_g6_blockcamp",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_2178_1#2$1",duration = 0.5)]
[delay(time=1)]
[name="“铅笔头”"]费佳！我找到了一个带肉的罐头，一起来吃点吗？
[charslot(slot="m",name="avg_npc_2155_1#8$1")]
[name="费佳"]......不了，谢谢。
[charslot(slot="m",name="avg_npc_2176_1#2$1")]
[name="叶列梅"]别逼他了，“铅笔头”。你和费佳不熟，不知道他喜欢一个人待着吧？
[charslot(slot = "m", name = "avg_npc_2178_1#2$1")]
[name="“铅笔头”"]都认识好几天了，哪有你说的那么生分。
[name="“铅笔头”"]对了，费佳，你看起来不像是学生，也不像是工人。
[name="“铅笔头”"]我到现在都不知道，你是怎么到了这个鬼地方的。
[charslot(slot="m",name="avg_npc_2155_1#2$1")]
[name="费佳"]......抱歉，那是绝对不能说的。
[charslot(slot = "m", name = "avg_npc_2178_1#4$1")]
[name="“铅笔头”"]欸？
[charslot(slot="m",name="avg_npc_2176_1#4$1")]
[name="叶列梅"]你到底是......
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="72_g13_nobleroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>1101年12月24日</><p=2>冬季舞会开始前半个小时</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(intro="$escape_intro",key="$escape_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1984_1#1$1",duration=1)]
[delay(time=2)]
[name="维特"]陛下，时间不多了，我恳请您最后再考虑一下。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_2155_1#1$2",duration=1)]
[delay(time=2)]
[name="费奥多尔"]考虑，是的，我的确在考虑——我在考虑，或许我们真的应该把这些脑满肠肥的老东西统统送去喂蓄肉蝎。
[name="费奥多尔"]这样一来，我们不仅可以直接没收他们的家产拿到一大笔收入，还能得到一批肉质鲜美的蓄肉蝎。
[charslot(slot="m",name="avg_npc_1984_1#1$1")]
[name="维特"]陛下......我完全理解您的愤怒。
[name="维特"]可您也应该清楚，比起那些忠诚可以明码标价的产业贵族，这些资历更老的贵族是更愿意与您站在一起的。
[name="维特"]尤其是当您想要震慑住现在还盘踞在涅瓦湖彼岸的集团军的时候，您的确需要更多声音站在您这一边。
[charslot(slot="m",name="avg_npc_

... (全文26265字符)
```

### level_act51side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="72_g6_blockcamp",screenadapt="coverall")]
[playsound(key="$d_avg_woodcracle", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.6, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_2178_1#2$1",duration = 0.5)]
[delay(time=1)]
[name="“铅笔头”"]叶列梅！我今天在化工厂翻了一天，就找到这么一箱啤酒，你还要喝啊？
[charslot(slot="m",name="avg_npc_2176_1#6$1")]
[name="叶列梅"]去去去——
[charslot(slot="m",name="avg_npc_2183_1#2$1")]
[name="尼卡"]呵，你就让他喝吧，这几天他可被吓坏了。
[charslot(slot="m",name="avg_npc_2176_1#2$1")]
[name="叶列梅"]那还不是，扛过来了，嗝......反正这点啤酒，也不算什么，我平时还瞧不上呢！
[charslot(slot="m",name="avg_npc_2178_1#2$1")]
[name="“铅笔头”"]欸，这位老爷，怎么沦落到这个地步了，还要找我这种“草民”借酒喝？
[charslot(slot="m",name="avg_npc_2176_1#2$1")]
[name="叶列梅"]不，你是好人，最好的。
[charslot(slot="m",name="avg_npc_2183_1#2$1")]
[name="尼卡"]叶列梅，我也是“草民”，快夸夸我。
[charslot(slot="m",name="avg_npc_2176_1#2$1")]
[name="叶列梅"]那还是算了——嗝！
[charslot(slot="m",name="avg_npc_2178_1#5$1")]
[name="“铅笔头”"]......怎么突然扯到这个话题了，怪不好意思的。
[charslot(slot="m",name="avg_npc_2176_1#2$1")]
[name="叶列梅"]听着，亲爱的朋友们，我在这里每喝一杯，出去就多还你们一箱。
[name="叶列梅"]索尼娅、米科拉，还有费佳，人人都有份！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background]
[Image(image="72_i08_1",screenadapt="coverall")]
[bgeffect(name="$eb_062cg_phantom_front",layer=1,x=-200)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="尼卡"]叶列梅，你还好吗？
[name="“铅笔头”"]这么能喝哪像有事的样子......
[name="“铅笔头”"]喂，你现在就可以把剩下的啤酒留给我们，费佳就坐在你身后呢！
[name="叶列梅"]今晚，今晚不行，以后随便你们——
[Dialog]
[PlaySound(key="$d_avg_drinkwine_generous")]
[delay(time=1)]
[Image(image="72_i08_2",screenadapt="coverall",fadetime=2)]
[ImageTween(  duration=60, block=false,xScaleFrom=1, yScaleFrom=1, xScaleTo=1.2, yScaleTo=1.2)]
[delay(time=3)]
[name="伯塔尼"]你为什么不和其他人坐在一起？
[name="费奥多尔"]你呢？大英雄，俘虏了一个胆小的敌人。
[name="费奥多尔"]索尼娅和安托沙审了快一天，我想很快就有结果了。
[name="伯塔尼"]希望能早点终结格罗莫夫的暴行......
[name="费奥多尔"]但你看着并不高兴？
[name="伯塔尼"]不，我一直在想，封锁区内的无线电静默到底是什么原因造成的。
[name="费奥多尔"]这是第三局的强项，他们有很多手段可以做到。
[name="伯塔尼"]可你的设备依然能接收到我的信号，为什么......
[name="费奥多尔"]你的问题太多了，“伯塔尼”......哼，这个“书呆子”的代号真没起错。
[name="费奥多尔"]像你这么较真的乌萨斯人越来越少，我竟然有点怀念过去了。
[name="伯塔尼"]......我知道你有秘密，费佳。
[name="伯塔尼"]你不想说的话，我会假装那些都不存在。
[name="伯塔尼"]我想说的是，如果没有你，我不可能把帕夫洛男爵带回来......在这件事上，你才是我们的英雄。
[name="伯塔尼"]或许有一天，你会成为更多人的......
[name="费奥多尔"]......
[name="“铅笔头”"]嘿，费佳、伯塔尼！过来喝两杯吗？
[name="“铅笔头”"]叶列梅他，喝醉之后力气真大，刚才死活不让我碰酒。
[name="“铅笔头”"]现在他好像终于喝醉了，我不放心又补了两拳，应该暂时醒不过来了。
[name="费奥多尔"]啊？
[name="“铅笔头”"]总之，剩下的酒正好还够倒四杯，你们愿意的话，我想和你们多聊聊，交个朋友......
[name="伯塔尼"]当然，“铅笔头”，这好像是我第一次出现在你们面前。
[name="“铅笔头”"]哈哈，你刚来的时候浑身都是血，大家吓了一大跳，但一听到声音我就安心了。
[name="尼卡"]来吧，我已经倒好酒了。费佳，这是你的那杯。
[name="费奥多尔"]......谢谢。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[image]
[bgeffect]
[name="“铅笔头”"]敬明天！
[name="尼卡"]敬胜利！
[name="费奥多尔"]敬......
[name="费奥多尔"]自由与幸福的灵魂。
[stopmusic(fadetime=2)]
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="72_g6_blockcamp",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_2157_1#7$1",duration=1)]
[delay(time=1.5)]
[name="安托沙"]......我无法接受妥协。
[charslot(slot="m",name="avg_1051_headb2_1#1$1")]
[name="凛冬"]除非你能给出更有效率的方案。无论你怎么拷问，他只在意自己的安全保障。
[charslot(slot="m",name="avg_npc_2157_1#7$1")]
[name="安托沙"]......我警告过你，帕夫洛是最典型的乌萨斯贵族。
[name="安托沙"]他们短视、怯懦，永远幻想上级偶尔的仁慈与“点拨”，带着一副人畜无害的嘴脸，好把所有金银装进自己的衣兜。
[name="安托沙"]一旦让他们得以喘息，他们会毫不犹豫地向人民挥刀，将鲜血当作送给长官的礼物。
[name="安托沙"]这群擅长防腐的活尸......你就闻不到他们的臭味吗？
[charslot(slot="m",name="avg_1051_headb2_1#1$1")]
[name="凛冬"]我们可以一直争论下去，但也可以去制定更要紧的计划。我让他吐出的情报里，包括“十六勇士”的总部地图。
[name="凛冬"]那里有最足量的补给，而且他说格罗莫夫最近经常外出，这是一个绝佳的机会。
[charslot(slot="m",name="avg_npc_2157_1#7$1")]
[name="安托沙"]如果他活着离开，一定会出卖你的......就算离开了卡托加区，铺天盖地的警察也会去抓捕你，我们真要在法庭上相见吗？
[charslot(slot="m",name="avg_npc_2160_1#2$1")]
[name="马特维"]......至少我们现在的目标一致，要解放这个区域，其他争议可以以后再说。
[name="马特维"]突袭对方的老巢显然是一个艰巨的挑战，我们愿意配合你们的行动，只是我们还需要回去休整，或许——
[charslot(slot="m",name="avg_1051_headb2_1#4$1")]
[name="凛冬"]我明白了。等大家都准备好之后，我们再一起行动，让帕夫洛带路。
[charslot(slot="m",name="avg_1051_headb2_1#1$1")]
[name="凛冬"]安托沙，你觉得呢？
[charslot(slot="m",name="avg_npc_2157_1#1$1")]
[name="安托沙"]......多带点人，索尼娅，不要低估他。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_2155_1#1$1",duration=1)]
[charslot(slot="r",name="avg_4223_botany_1#1$1",duration=1)]
[delay(time=2)]
[charslot(slot="r",focus="r")]
[name="伯塔尼"]......索尼娅？
[charslot]
[charslot(slot="m",name="avg_1051_headb2_1#1$1")]
[name="凛冬"]嘘，伯塔尼、费佳，我们小点声，不要吵醒他们。
[charslot(slot="m",name="avg_1051_headb2_1#11$1")]
[name="凛冬"]我只是......想来火堆边休息一会儿。
[charslot(slot="m",name="avg_1051_headb2_1#1$1")]
[name="凛冬"]你们给这里的人帮了大忙，但是我有点不知道，我能不能带领好大家，不辜负你们的努力。
[name="凛冬"]回到乌萨斯的时候，我也想过要在家乡过上正常的生活。然而不只是我，跟随我的人们，至今都还在这片泥泞里挣扎......
[charslot(slot="m",name="avg_npc_2155_1#8$1")]
[name="费奥多尔"]......
[charslot(slot="m",name="avg_1051_headb2_1#1$1")]
[name="凛冬"]你们不知道，我其实辜负过许多人的期盼，看着同龄的朋友死在我的面前......不久后，我又要带着大家出发了。
[charslot(slot="m",name="avg_1051_headb2_1#12$1")]
[name="凛冬"]......我们能回到正常的生活吗？或许我还是什么都做不到......
[charslot(slot="m",name="avg_4223_botany_1#1$1")]
[name="伯塔尼"]可我觉得，你不是做到了吗？
[charslot(slot="m",name="avg_1051_headb2_1#6$1")]
[name="凛冬"]......嗯？
[dialog]
[PlaySound(key="$d_avg_pourwine",volume=0.7)]
[charslot(slot="m",name="avg_4223_botany_1#2$1")]
[delay(time=2)]
[name="伯塔尼"]来，给你半杯，我的酒还没动过呢。
[charslot]
凛冬怔在原地，不自觉地接过酒杯，嗅着浅浅的小麦香气，耳畔传来轻轻的鼾声。
她的目光拂过每张平和的睡脸，他们的脸颊都红扑扑的，在梦中咂着嘴......这是进入封锁区后，最安静的一个夜晚。
[charslot(slot="m",name="avg_1051_headb2_1#2$1")]
[name="凛冬"]嗯......
[name="凛冬"]还有半杯，哪怕只剩半杯......
[Dialog]
[Blocker(a=1, r

... (全文33134字符)
```

### level_act51side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[Background(image="bg_towerinside",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>圣骏堡，罗德岛临时办事处</><p=2>冬季舞会一周前</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=2, amount=0, block=true)]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.6)]
[PlaySound(key="$doorknockquite")]
[name="弑君者"]坚雷女士，我来提交近期的报告——
[name="弑君者"]......坚雷女士？
[dialog]
[CameraShake(duration=0.3, fadeout=true, xstrength=5, ystrength=15, vibrato=10, randomness=90, block=false)]
[PlaySound(key="$d_avg_heavyobject_putdown",volume=0.7)]
[delay(time=1)]
眼前只有一片混乱，看不出任何有人的踪迹。弑君者开始把面前的纸箱搬开，试图给自己清出一条道路来。
[name="弑君者"]怎么还是这么乱......完全没地方下脚。
[name="弑君者"]坚雷——
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_1051_headb2_1#1$1",duration=1.5,bstart=0.3,bend=0.5)]
[delay(time=2)]
[name="？？？"]是谁在外面？
[dialog]
[charslot(slot="m",name="avg_1051_headb2_1#1$1",duration=0.5)]
[delay(time=1)]
[name="凛冬"]坚雷教官不在，报告可以给我。
[charslot]
[dialog]
[charslot(slot="m",name="avg_1502_crosly_1#1$1",duration=0.5)]
[delay(time=1)]
[name="弑君者"]......
[charslot(slot="m",name="avg_1051_headb2_1#5$1")]
[name="凛冬"]啊，是你。
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="弑君者"]坚雷女士呢？
[charslot(slot="m",name="avg_1051_headb2_1#1$1")]
[name="凛冬"]不知道，我也刚从外面回来没几天，现在办事处里只有我和拉达——就是古米，只有我们俩在。
[name="凛冬"]正式建立办事处的事刚定下来，其他人大概在到处跑手续。我马上也要出去一趟，有份学联的稿件要争取在这几天发出去——
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="弑君者"]我的报告在这，麻烦你转交一下。
[charslot(slot="m",name="avg_1051_headb2_1#1$1")]
[name="凛冬"]......行。
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[dialog]
[playsound(key="$d_gen_walk_n", loop=true, channel="bgs")]
[StopSound(channel="bgs", fadetime=2)]
[charslot(duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_1051_headb2_1#1$1")]
[name="凛冬"]等等。
[charslot]
[name="弑君者"]还有什么事？
[charslot(slot="m",name="avg_1051_headb2_1#10$1")]
[name="凛冬"]呃......
[charslot(slot="m",name="avg_1051_headb2_1#4$1")]
[name="凛冬"]虽然你看上去好像不愿意跟我们说话，总是独来独往，但大家都是乌萨斯人，如今又都是罗德岛的干员。
[charslot(slot="m",name="avg_1051_headb2_1#1$1")]
[name="凛冬"]现在新建办事处，什么都要从头开始，我想，也许我们可以互相帮助，提高点效率。
[dialog]
[charslot]
[charslot(slot="m",name="avg_1502_crosly_1#1$1",duration=0.5)]
[delay(time=1)]
[name="弑君者"]......你们需要什么？
[charslot(slot="m",name="avg_1051_headb2_1#6$1")]
[name="凛冬"]不是！我是想说，如果你有什么需要，是可以向办事处、向我们寻求帮助的，懂吗？没必要什么事都自己扛着。
[charslot(slot="m",name="avg_1051_headb2_1#2$1")]
[name="凛冬"]当然，如果我们需要，也会找你的。
[name="凛冬"]教官说你除了定期递交报告之外，和办事处的人没有任何交集，虽然我觉得各司其职也不错，但你刚好来了，我就说一声。
[charslot(slot="m",name="avg_1502_crosly_1#3$1")]
[name="弑君者"]你不会希望我频繁出现在这里的。
[charslot(slot="m",name="avg_1051_headb2_1#1$1")]
[name="凛冬"]别擅自决定我的想法。我知道你和切城，甚至和整合运动有关系，但你到底干了什么，我不知道，也暂时不打算去了解。
[name="凛冬"]对我们来说那是个会反复开裂的伤口，可什么都躲着也不会让它真正长合。
[name="凛冬"]更重要的是，你和我们站在一起，现在又正是缺人的时候，这就够了。
[name="凛冬"]所以，如果你需要帮助，不要忘了告诉我们。
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="弑君者"]......
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_1051_headb2_1#5$1")]
[name="凛冬"]喂！
[charslot]
[name="弑君者"]谢谢。
[name="弑君者"]如果需要，我会的。
[Dialog]
[CameraEffect(effect="Grayscale", fadetime=1, keep=true, initamount=0, amount=1, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="72_g1_sjbstreet_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>圣骏堡，学院滨河街道警察分局</><p=2>12月24日 7:45 A.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1979_1#1$1",duration=0.5)]
[delay(time=1)]
[name="被捕的工人"]柳德米拉！
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="弑君者"]......我正想去保释你。
[charslot(slot="m",name="avg_npc_1979_1#1$1")]
[name="被捕的工人"]那就感谢有人做好事，又给咱们省了一笔保释金吧！
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="弑君者"]你是怎么被放出来的？刚才的爆炸声又是......
[charslot]
[name="远处的声音"]——都逃跑——
[name="远处的声音"]快追——！
[charslot(slot="m",name="avg_npc_1979_1#1$1")]
[name="被捕的工人"]圣骏堡嘛，这种事不稀奇。
[name="被捕的工人"]还是先别说了，要是站这等那些草包警察过来，我就又得进去蹲着了。
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="弑君者"]......先别回去，跟我走。我还有事要问你。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_oldwarehouse_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_1979_1#1$1",duration = 0.5)]
[charslot(slot = "right", name = "avg_1502_crosly_1#1$1",duration = 0.5)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_1979_1#1$1",focus="l")]
[name="被捕的工人"]你怎么知道我被条子带走了？我还以为自己要在那蹲坑蹲到天荒地老呢。
[charslot(slot = "right", name = "avg_1502_crosly_1#1$1",focus="r")]
[name="弑君者"]有人看到你被警察问话，住在你对面的那个小孩，记得吗？
[charslot(slot = "left", name = "avg_npc_1979_1#1$1",focus="l")]
[name="被捕的工人"]小孩？红头发的那个？我只记得他看上去阴恻恻的，有点讨人厌——
[charslot(slot = "right", name = "avg_1502_crosly_1#1$1",focus="r")]
[name="弑君者"]不要以貌取人。你手上的货都卖完了吗？
[charslot(slot = "left", name = "avg_npc_1979_1#1$1",focus="l")]
[name="被捕的工人"]还有一个人没跟我碰头，被抓走之前我就是在等他。奥多耶夫区的那个......叫什么来着？
[charslot(slot = "right", name = "avg_1502_crosly_1#1$1",focus="r")]
[name="弑君者"]鲁斯，理发师，住在第五大道，他家里有两个刚出生的孩子，妻子死于流感并发症。
[charslot(slot = "left", name = "avg_npc_1979_1#1$1",focus="l")]
[name="被捕的工人"]对......对，是他。除了他之外，其他人我都已经交接好了。
[charslot(slot = "right", name = "avg_1502_crosly_1#1$1",focus="r")]
[name="弑君者"]能量转换器的钱他们都是怎么付的？
[charslot(slot = "left", name = "avg_npc_1979_1#1$1",focus="l")]
[name="被捕的工人"]啊？不是不用付钱吗？只要持续找我们买货，

... (全文18900字符)
```

### level_act51side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="72_g15_wideunder",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(key="$calm_loop", volume=0.6)]
[charslot(slot="m",name="avg_1502_crosly_1#1$1",duration=0.5)]
[Delay(time=1)]
[name="弑君者"]你跟来，就要全程听我的，按我说的做。
[name="弑君者"]明白吗？
[charslot(slot="m",name="avg_196_sunbr_1#1$2")]
[name="古米"]明白！嘿嘿......
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="弑君者"]笑什么？
[charslot(slot="m",name="avg_196_sunbr_1#1$2")]
[name="古米"]柳德米拉姐真可靠啊。
[charslot(slot="m",name="avg_1502_crosly_1#3$1")]
[name="弑君者"]别轻易就下这种判断。
[charslot(slot="m",name="avg_260_durnar_1#1$1")]
[name="坚雷"]你们什么时候关系这么好的？之前我还担心弑君者不愿跟乌萨斯办事处的人打交道，看来是白担心啦。
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="弑君者"]......她不一样。在罗德岛那艘船上，在食堂里，我们早就打过交道。
[charslot(slot="m",name="avg_196_sunbr_1#9$1")]
[name="古米"]咦？是因为这个吗？在食堂里——
[charslot(slot="m",name="avg_196_sunbr_1#4$1")]
[name="古米"]啊！原来你就是那个做乌萨斯菜和叙拉古菜都很好吃的红头发姐姐！
[charslot(slot="m",name="avg_1502_crosly_1#9$1")]
[name="弑君者"]......
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="弑君者"]先别打岔了。我的源石技艺能帮我隐蔽，一会儿我先从这里出去找凛冬。只要早露留在报告里的坐标是准确的，那我就一定能找到。
[charslot(slot="m",name="avg_260_durnar_1#8$1")]
[name="坚雷"]嘶，根据早露的报告，封锁区里情况复杂，所以不排除凛冬的据点移动的可能。总之你先去看看吧，不行就回来。
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="弑君者"]嗯。
[charslot(slot="m",name="avg_196_sunbr_1#5$1")]
[name="古米"]为什么我们不能一起呢？
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="弑君者"]卡托加区被封锁之后，动力层通道也被巴普洛维奇的人接管了，在不惊动他们的情况下一起进去不现实，你们只能先在这里等我。
[name="弑君者"]这边不属于卡托加区，在这里工作的工人们都认识我，万一有人巡逻过来，报我的名字就行——柳德米拉·伊里尼奇娜。
[charslot(slot="m",name="avg_260_durnar_1#3$1")]
[name="坚雷"]明白，但最好还是别被人发现。我们会藏好了，然后等着接应你的。
[charslot(slot="m",name="avg_196_sunbr_1#11$1")]
[name="古米"]那等你见到凛冬姐，一定要看看她有没有受伤，是不是瘦了——
[charslot(slot="m",name="avg_1502_crosly_1#1$1")]
[name="弑君者"]好，我尽量。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="72_g4_blockst_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_1502_crosly_1#1$1",duration=0.5)]
[Delay(time=1)]
[name="弑君者"]......
[name="弑君者"]没有人巡逻？这和报告里提到的情况不一样。
[dialog]
[playsound(key="$d_avg_footsteps_flock", loop=true, channel="a",volume=0.5)]
[StopSound(channel="a", fadetime=2)]
[Delay(time=1.5)]
[name="弑君者"]前面应该就是索尼娅的营地了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="34_g10_tent_inside",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_194_leto_1#9$1",duration=0.5)]
[Delay(time=1)]
[name="烈夏"]......你不想让我去找马特维，那我就不去了。你想一个人待着，我也不烦你。
[charslot(slot="m",name="avg_194_leto_1#13$1")]
[name="烈夏"]只是万一你想找人说说话，或者商量点什么，就大声喊我的名字，懂吗？
[name="烈夏"]我都在的，别一个人扛。
[dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(duration=1)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_1051_headb2_1#4$2")]
[name="凛冬"]......
[dialog]
[charslot]
[playsound(key="$d_avg_smoke_grenade")]
[bgeffect(name="$eb_smog",layer=1)]
[Blocker(a=0.5, r=0.7, g=0.7, b=0.7, fadetime=0.5, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_1051_headb2_1#9$2")]
[name="凛冬"]......什么鬼东西......
[name="凛冬"]罗莎琳——
[dialog]
[charslot]
[charslot(slot="m",name="avg_1502_crosly_1#1$1",duration=0.5,bstart=0.3,bend=0.5)]
[Delay(time=1)]
[name="？？？"]别喊，是我。
[charslot(slot="m",name="avg_1051_headb2_1#5$2")]
[name="凛冬"]嗯？
[dialog]
[charslot]
[charslot(slot="m",name="avg_1502_crosly_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="弑君者"]你不是让我有困难，就来找你帮忙吗？
[name="弑君者"]现在，我来了。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[bgeffect]
[charslot(slot = "left", name = "avg_1502_crosly_1#1$1")]
[charslot(slot = "right", name = "avg_1051_headb2_1#1$2")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(key="$formal_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_1502_crosly_1#1$1",focus="l")]
[name="弑君者"]嗯，这套通讯设备应该没什么问题。
[name="弑君者"]......所以，你们已经在准备离开了。城墙内的那些打手已经被你们解决了。
[name="弑君者"]怪不得我在来的路上，一个巡逻的人都没看到。
[charslot(slot = "right", name = "avg_1051_headb2_1#1$2",focus="r")]
[name="凛冬"]城墙内的打手没了，也还有城墙上的，恐怕之后还有恶战。
[charslot(slot = "left", name = "avg_1502_crosly_1#1$1",focus="l")]
[name="弑君者"]你们都准备好了吗？
[charslot(slot = "right", name = "avg_1051_headb2_1#1$2",focus="r")]
[name="凛冬"]我们必须这样认为。我没有时间，也没有精力去过问每一个人的意见，但他们没有选择放弃训练，本身就是一种表态。
[charslot(slot = "left", name = "avg_1502_crosly_1#1$1",focus="l")]
[name="弑君者"]我不是在质疑你或者你们之中的任何人。从我在外面了解的情况来看，你们能在封锁区里活下来，还团结在一起，已经算是不可思议了。
[charslot(slot = "right", name = "avg_1051_headb2_1#1$2",focus="r")]
[name="凛冬"]外面都怎么说的？
[charslot(slot = "left", name = "avg_1502_crosly_1#3$1",focus="l")]
[name="弑君者"]说这里已经是巴普洛维奇陛下的独立王国了，他对里面的活物拥有生杀予夺的绝对权力。
[name="弑君者"]那些贵族老爷也已经不在乎了，反正这个地块马上就要像一块被割掉的烂肉那样被抛弃，上面的人也一样。
[charslot(slot = "right", name = "avg_1051_headb2_1#11$2",focus="r")]
[name="凛冬"]哼。
[charslot(slot = "left", name = "avg_1502_crosly_1#6$1",focus="l")]
[name="弑君者"]乌萨斯总是这样......乌萨斯总是这样。可被抛弃的对象却永远都挣扎着想活。
[charslot(slot = "right", name = "avg_1051_headb2_1#1$2",focus="r")]
[name="凛冬"]从前阿米娅不希望我们和你有过多接触，我都没机会知道你是个这么感性的家伙。
[charslot(slot = "left", name = "avg_1502_crosly_1#1$1",focus="l")]
[name="弑君者"]......这不是感性的问题......
[charslot(slot = "left", name = "avg_1502_crosly_1#2$1",focus="l")]
[name="弑君者"]换个说法吧。来的时候，我听见有人围着篝火在哭，安慰他的人却在笑，他们胳膊上打着绷带，身上和地上的雪一样脏。
[charslot(slot = "left", name = "avg_1502_crosly_1#3$1",focus="l")]
[name="弑君者"]其他人有的在聊天，有的手里捧着杯冒热气的水，有的在火上烤了点东西。
[name="弑君者"]在这样的地方，经历了这么多的事，他们看上去却没有特别痛苦，或者说，甚至看上去很期待明天。
[name="弑君者"]一无所有，但胸腔里塞满了希望。我从前也见过这样的情景和这样的表情，在......
[charslot(slot = "left", name = "avg_1502_crosly_1#6$1",focus="l")]
[name="弑君者"]......
[charslot(slot = "right", name = "avg_1051_headb2_1#2$2",focus="r")]
[name="凛冬"]谢谢你细致的观察。
[name="凛冬"]但物资终究是匮乏的。每天都可能是最后一天，你面前这杯茶也可能是最后一杯茶，所以，不喝就给我

... (全文31774字符)
```

### level_act51side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_oldwarehouse_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(key="$calm_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_2184_1#3$1",duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_2184_1#3$1")]
[name="尤拉"]不对，不能这么写。
[charslot(slot="m",name="avg_npc_2184_1#4$1")]
[name="尤拉"]“用一层雪水，擦拭灰色的街道”？“拿来一盒受潮的烟”？不对，都不对！
[charslot(slot = "m", focus = "n")]
他对着微弱的月光，拿起满是印子的草稿，不禁抱怨灵感枯竭的自己——这首诗还不如一旁熟睡的同学那含糊的梦话。
经历大火后，无缚者同盟的营地异常平静，冬风像是在用钝刀刮蹭年轻人们稚嫩的脸颊。
尚有精力的年轻人窃窃私语着，他们裹紧散发着霉味的大衣，在夜色下就像一个个土包，时不时发出几阵笑声。
[charslot(slot="m",name="avg_npc_2184_1#2$1")]
[name="尤拉"]......请给每一颗星星，一个能够记住的名字。
[name="尤拉"]请给想要遗忘的人，一杯最廉价的烈酒。
[name="尤拉"]请给我......
[name="尤拉"]请给我一张去往春天的单程票......
[name="尤拉"]可以让我住进，穿过苔原的风里。
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_4224_turdus_1#4$1")]
[name="乌克西克"]吓——
[charslot(slot="m",name="avg_npc_2184_1#5$1")]
[name="尤拉"]？！
[charslot(slot="m",name="avg_npc_2184_1#2$1")]
[name="尤拉"]果然是你......我发誓，总有一天我会对你所有的恶作剧免疫。
[charslot(slot="m",name="avg_4224_turdus_1#2$1")]
[name="乌克西克"]又在写那些酸掉牙的诗了，尤拉。
[charslot(slot="m",name="avg_npc_2184_1#2$1")]
[name="尤拉"]每首诗可都是我费尽心血写的，才不是什么酸诗，你看得懂吗？
[charslot(slot="m",name="avg_4224_turdus_1#2$1")]
[name="乌克西克"]我才不想看懂，你们这些能看得懂的人每天都愁眉苦脸的。
[name="乌克西克"]何况马特维才教我识了几行字，我能看懂地址就不错了。反正大家写什么，最后还不是要靠我送出去。
[charslot(slot="m",name="avg_4224_turdus_1#4$1")]
[multiline(name="乌克西克")]说说吧尤拉，这次要我帮你送给哪个姑娘？
[playsound(key="$d_avg_knock_head")]
[CameraShake(duration=0.2, xstrength=0, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_4224_turdus_1#10$1")]
[multiline(name="乌克西克")]哎哟——
[dialog]
[charslot(slot="m",name="avg_npc_2184_1#2$1")]
[PlaySound(key="$d_avg_paper1")]
[Delay(time=1)]
[name="尤拉"]送给你的，你这个小鬼！
[charslot(slot="m",name="avg_4224_turdus_1#10$1")]
[name="乌克西克"]你竟敢打小孩！我要收走这张纸，你别想再写了！
[charslot(slot="m",name="avg_npc_2184_1#2$1")]
[name="尤拉"]好啦好啦，就是拿纸筒打了下，哪有那么夸张......不过你想要，就拿去吧。
[name="尤拉"]这次......我是写给大家的，当然你也有份。
[charslot(slot="m",name="avg_4224_turdus_1#2$1")]
[name="乌克西克"]奇奇怪怪的......那我放包里了。
[charslot(slot="m",name="avg_npc_2184_1#2$1")]
[name="尤拉"]不说这些了，乌克西克。
[name="尤拉"]安托沙那里好像有很多信，我想，你得去找他一趟。
[charslot(slot="m",name="avg_4224_turdus_1#2$1")]
[name="乌克西克"]他不是每晚都和你们一起吃饭休息吗？我怎么没在这里看到他？
[charslot(slot="m",name="avg_npc_2184_1#2$1")]
[name="尤拉"]我哪知道？反正他就在里边，能问出原由的话，你也帮我问问他。
[name="尤拉"]对了，把大衣扣紧一点，你要是冻着了，安托沙又要骂人。
[charslot(slot="m",name="avg_4224_turdus_1#6$1")]
[name="乌克西克"]嗯？他可从来不骂我。
[charslot(slot="m",name="avg_4224_turdus_1#2$1")]
[name="乌克西克"]再见了，尤拉。
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot = "m",posfrom = "0,0", posto = "-200,0",duration = 1,afrom=1,ato=0)]
[Delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_npc_2184_1#2$1")]
[name="尤拉"]因为他骂的是我们，小鬼......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="bg_oldwarehouse_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_4224_turdus_1#4$1",duration=0.5)]
[Delay(time=1)]
[name="乌克西克"]安托沙，我来啦。
[charslot(slot="m",name="avg_npc_2157_1#2$1")]
[name="安托沙"]......不用每次都喊得那么大声，乌克西克。
[charslot(slot="m",name="avg_4224_turdus_1#2$1")]
[name="乌克西克"]尤拉和我说，你有些信件要交给我。在哪儿呢？
[charslot(slot="m",name="avg_npc_2157_1#2$1")]
[name="安托沙"]是，有些多。
[Dialog]
[charslot(duration=1)]
[PlaySound(key="$d_gen_walk_n")]
[delay(time=1)]
他走到角落，抱起厚厚一摞信件。
[charslot]
[charslot(slot="m",name="avg_4224_turdus_1#10$1")]
[name="乌克西克"]好麻烦......我先看看。
[PlaySound(key="$d_avg_paper1")]
[charslot(slot="m",name="avg_4224_turdus_1#6$1")]
[name="乌克西克"]这第一封，送到奥多耶夫区老街的34号？第二封送到铁河区左岸街的15号，第三封送到香料市场的......
[charslot(slot="m",name="avg_4224_turdus_1#1$1")]
[name="乌克西克"]等等安托沙，这些信都是你写的？这些地址都是什么地方？
[charslot(slot="m",name="avg_npc_2157_1#2$1")]
[name="安托沙"]奥多耶夫区老街的34号，是尤拉的家，然后是小列夫和维萨里昂的......
[name="安托沙"]我为每一个人都写了信，等我们打倒了那个枢密官后你再看看，需要送出多少封。
[charslot(slot="m",name="avg_npc_2157_1#11$1")]
[name="安托沙"]如果有人倒在明天，至少......我不希望他们的家人，是从乌萨斯给出的伤亡名单上知道他们的消息。
[charslot(slot="m",name="avg_4224_turdus_1#9$1")]
[name="乌克西克"]......你是什么时候记下这些的？
[charslot(slot="m",name="avg_npc_2157_1#5$1")]
[name="安托沙"]有人把命交给我的时候，我必须要知道这些命是从哪里来的......这是忘不掉的。
[charslot(slot="m",name="avg_npc_2157_1#2$1")]
[name="安托沙"]还记得吗？当初我也问过你的出身。
[charslot(slot="m",name="avg_4224_turdus_1#1$1")]
[name="乌克西克"]只不过你没想到，我是一个连名字都没有的孤儿？
[charslot(slot="m",name="avg_npc_2157_1#11$1")]
[name="安托沙"]......
[charslot(slot="m",name="avg_4224_turdus_1#2$1")]
[name="乌克西克"]好啦，你这是什么表情？
[name="乌克西克"]我自己都没有像你这样愁过，何况今天我还帮你省了一张纸呢。
[name="乌克西克"]说起来，这些信里，也有你和马特维的吗？
[dialog]
[charslot]
[playsound(key="$d_gen_walk_n", loop=true, channel="bgs")]
[StopSound(channel="bgs", fadetime=1)]
[charslot(slot="m",name="avg_npc_2160_1#1$1",duration=0.5)]
[Delay(time=1)]
[name="马特维"]说不定会有我的，但绝不会有他的。
[charslot(slot="m",name="avg_4224_turdus_1#2$1")]
[name="乌克西克"]马特维？
[charslot(slot="m",name="avg_npc_2160_1#1$1")]
[name="马特维"]要做什么大事前，我和他习惯单独聚一聚。
[charslot(slot="m",name="avg_npc_2157_1#2$1")]
[name="安托沙"]翻到啤酒了吗？
[playsound(key="$d_avg_bottlecollide")]
[charslot(slot="m",name="avg_npc_2160_1#1$1")]
[name="马特维"]最后两瓶，不知道被谁藏在了那堆烂菜叶里。不过今晚整理装备的时候，利斯特还是闻出来了。
[charslot(slot="m",name="avg_npc_2157_1#2$1")]
[name="安托沙"]......给我一瓶。
[charslot(slot="m",name="avg_4224_turdus_1#2$1")]
[name="乌克西克"]马特维，我也能尝一尝吗？正好有些口渴——
[charslot(slot="m",name="avg_npc_2160_1#9$1")]
[name="马特维"]你才多大？休想。
[charslot(slot="m",name="avg_4224_turdus_1#10$1")]
[name="乌克西克"]小气！
[charslot]
马特维轻轻地拍了一下女孩的头，接着他坐在了安托沙身旁，递去一个玻璃瓶。
[charslot(slot="m",name="avg_4224_turdus_1#2$1")]
[name="乌克西克"]不过马特维，你为什么说安托沙不会给自己家里写信呢？
[name="乌克西克"]他要是觉得自己不会死，又何必让我去送信？难道他不敢？
[charslot(slot="m",name="avg_npc_2160_1#1$1")]
[name="马特维"]哈哈，那怎么可能......
[charslot(slot="m",name="avg_npc_2160_1#3$1")]
[name="

... (全文21530字符)
```

### level_act51side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[bgeffect(name="$eb_blizzard",layer=1)]
[Background(image="72_g9_topwall",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(intro="$snowmonster_intro",key="$snowmonster_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_2158_1#8$2",duration=0.5)]
[Delay(time=1)]
[name="巴普洛维奇"]推进！把他们大卸八块！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_2158_1#5$2")]
[name="巴普洛维奇"]不要节省源石弩箭，打赢了你们人人有赏！
[dialog]
[charslot]
[playsound(key="$d_avg_explosion_stone",volume=0.6)]
[CameraShake(duration=3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[playsound(key="$d_avg_explosion_stone",volume=0.7,channel="2")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_2166_1#1$1")]
[name="“十六勇士”暴徒A"]射击！
[name="“十六勇士”暴徒A"]就算是这群疯子，沾上也要脱层皮！给我把他们压死在掩体后面！
[dialog]
[charslot]
[playsound(key="$d_avg_arrow_rain")]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_194_leto_1#13$1")]
[name="烈夏"]教官！我们该撤了！
[charslot(slot="m",name="avg_260_durnar_1#6$1")]
[name="坚雷"]你先带伤员走，我掩护你们！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="l",name="avg_npc_2166_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_2166_1#1$1",focus="l")]
[name="“十六勇士”暴徒A"]那帮小鬼撑不住了，集中火力对付那个拿盾牌的沃尔珀！
[charslot(slot="r",focus="r")]
[name="“十六勇士”暴徒B"]竟敢拿着老大的库存对付我们......找死！
[charslot]
[charslot(slot="m",name="avg_npc_2167_1#1$1")]
[name="“十六勇士”暴徒C"]为格罗莫夫报仇！
[charslot]
[playsound(key="$d_avg_riot", loop=true, channel="bgs")]
报仇的喊声如山呼海啸，暴徒如潮水般涌来......
[Dialog]
[StopSound(channel="bgs", fadetime=1.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_npc_2181_1#1$1")]
[name="焦虑的学生"]索尼娅，罗莎琳快撑不住了，我们得过去帮忙！
[charslot(slot="m",name="avg_1051_headb2_1#1$2")]
[name="凛冬"]在房子里藏好，她会没事的，一切都在计划内。
[charslot(slot="m",name="avg_npc_2181_1#1$1")]
[name="焦虑的学生"]可他们留存的火力超乎想象，如果还获得了外面的补给，我们——
[charslot(slot="m",name="avg_1051_headb2_1#1$2")]
[name="凛冬"]沉住气......相信你的同伴。
[name="凛冬"]我跟随过这片大地上最出色的战术指挥者，我们一定会活着离开这里。
[charslot(slot="m",name="avg_npc_2181_1#1$1")]
[name="焦虑的学生"]......是！
[charslot]
[playsound(key="$d_avg_snowrun", loop=true, channel="bgs")]
[StopSound(channel="bgs", fadetime=2)]
[CameraShake(duration=1.5, xstrength=10, ystrength=10, vibrato=15, randomness=90, fadeout=true, block=false)]
凛冬深吸一口气，她望着越来越近的人潮，紧紧追在罗莎琳他们的身后。
坚雷抵抗了一会，也随之转头跑去，而紧跟着她的暴徒们像是一群饥饿的裂兽，争先恐后地挤进了这条只有两个车身宽的狭窄巷道。
他们完全忽略了脚下那层黏稠的液体，也没注意到头顶两侧那一扇扇紧闭得有些诡异的窗户。
[charslot(slot="m",name="avg_npc_2166_1#1$1")]
[name="“十六勇士”暴徒A"]小毛头们怕了，继续追！
[dialog]
[charslot]
[CameraShake(duration=2, xstrength=6, ystrength=6, vibrato=25, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_crowdrun", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=1, channel="bgs",fadetime=2)]
[delay(time=2)]
[StopSound(channel="bgs", fadetime=0.3)]
[delay(time=0.3)]
[charslot(slot="l",name="avg_1051_headb2_1#1$2",duration=0.5)]
[delay(time=1)]
[charslot(slot="r",name="avg_4223_botany_1#8$1",duration=0.5)]
[delay(time=1)]
[charslot(slot="r",name="avg_4223_botany_1#8$1",focus="r")]
[name="伯塔尼"]“十六勇士”已经到达目标位置。
[charslot(slot="r",name="avg_4223_botany_1#9$1",focus="r")]
[name="伯塔尼"]索尼娅？
[charslot(slot="l",name="avg_1051_headb2_1#1$2",focus="l")]
[name="凛冬"]都做好准备，听我命令。
[charslot]
巷子的尽头，“慌乱逃窜”的坚雷突然停下了脚步。
[playsound(key="$sheildimpact")]
[CameraShake(duration=0.2, xstrength=10, ystrength=10, vibrato=35, randomness=90, fadeout=true, block=false)]
她没有回头，只是微微侧身，手中的盾牌轻轻磕在地上，发出一声清脆的“当”。
[charslot(slot="m",name="avg_1051_headb2_1#9$2")]
[name="凛冬"]一组、二组，上！
[dialog]
[charslot]
[playsound(key="$d_gen_explo_n")]
[CameraShake(duration=3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[playsound(key="$d_avg_explosion_stone",channel="1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[bgeffect(name="$eb_burn",layer=2)]
[playsound(key="$firestorm",channel="2")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1.5, block=true)]
窗户一齐打开，火把与炸药如同雨点般落下。它们没有被胡乱投掷，而是精准地砸在了敌人队伍的中部。
[playsound(key="$d_avg_fearscream",channel="3", loop=true)]
[StopSound(channel="3", fadetime=1.5)]
火苗攀爬上暴徒们单薄的服装，惊怖的叫声顿时此起彼伏。
[charslot(slot="m",name="avg_1051_headb2_1#9$2")]
[name="凛冬"]从两侧包抄到前方！避开巷子中间的火焰！
[name="凛冬"]轮到我们反击了！
[charslot]
[dialog]
[playsound(key="$d_avg_attack_ready")]
[charslot(slot = "left", name = "avg_npc_2178_1#1$1",duration = 0.5)]
[charslot(slot = "right", name = "avg_npc_2182_1#1$1",duration = 0.5)]
[delay(time=1)]
[charslot(duration=0.5)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_2179_1#1$1",duration = 0.5)]
[charslot(slot = "right", nam

... (全文30007字符)
```

### level_act51side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=0.5)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>圣骏堡</><p=2>1102年初</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[PlaySound(key="$d_avg_crwddiscuss_inside",volume=0, channel="bgs", loop=true)]
[SoundVolume(volume=0.2, channel="bgs",fadetime=2)]
[PlaySound(key="$d_avg_openftstpwalk",volume=0.8)]
[SoundVolume(volume=0.5, channel="bgs",fadetime=50)]
[playMusic(key="$formal_loop", volume=0.6)]
[Background(image="72_g10_hallway",screenadapt="coverall")]
[BackgroundTween(xFrom=0,xTo=-80, xScaleTo=1.2, yScaleTo=1.2, duration=60, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[PlaySound(key="$d_avg_openftstpwalk",volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.4, r=0, g=0, b=0, fadetime=1, block=true)]
[Sticker(id="st1", multi = true, text="......理解各位对青年才俊们的关爱，但年龄从不该是犯罪与堕落的借口。",x=250, y=150, alignment="left", size=24, delay=0.04, width=800)]
[Sticker(id="st2", multi = true, text="在乌萨斯，很多比他们还小的孩子，都已经在军队、工厂、矿区为帝国默默奉献了。",x=250, y=270, alignment="left", size=24, delay=0.04, width=800)]
[Sticker(id="st3", multi = true, text="唯独这些把头脑落在了学堂里的纨绔子弟，但凡劝他们停下那夸夸其谈的嘴，他们就失惊倒怪，俨然一副乌萨斯要亡国的模样。",x=250, y=390, alignment="left", size=24, delay=0.04, width=800)]
[Sticker(id="st1", duration=1, block=false)]
[Sticker(id="st2", duration=1, block=false)]
[Sticker(id="st3", duration=1, block=false)]
[delay(time=1)]
[PlaySound(key="$d_avg_openftstpwalk",volume=0.8)]
[Sticker(id="st1", multi = true, text="从来没有上过战场，没有背负过战友生命的重责，就敢对着报纸，摆弄沙盘与地图，喊着什么包抄迂回，“不惜一切代价”。",x=250, y=150, alignment="left", size=24, delay=0.04, width=800)]
[Sticker(id="st2", multi = true, text="从来没进过车间，没见过一条生产线停摆、几十双手等着你回应的夜晚，就敢喊着什么“提高待遇就能产能翻倍”。",x=250, y=270, alignment="left", size=24, delay=0.04, width=800)]
[Sticker(id="st3", multi = true, text="他们成双成对地溜进白桦林里，写出来的那些令人作呕的酸诗，念着倒是比远北矿工的生活还要忧郁凄凉。",x=250, y=390, alignment="left", size=24, delay=0.04, width=800)]
[Sticker(id="st1", duration=1, block=false)]
[Sticker(id="st2", duration=1, block=false)]
[Sticker(id="st3", duration=1, block=false)]
[delay(time=1)]
[PlaySound(key="$d_avg_openftstpwalk",volume=0.8)]
[Sticker(id="st1", multi = true, text="他们的立场，源于对周遭一切浅薄的认知。这些人牵强附会地搬用古人写出的格言警句，再反复念诵，直至让同立场的蠢材都深信不疑。",x=250, y=150, alignment="left", size=24, delay=0.04, width=800)]
[Sticker(id="st2", multi = true, text="由此，议会唯一的失误，便是不断地善意忍让。这只能换来他们的蔑视与仇恨，最终酿成如此大祸。",x=250, y=270, alignment="left", size=24, delay=0.04, width=800)]
[Sticker(id="st3", multi = true, text="我依然保持我的观点：这是一场没有任何必要的听证会，因为诸位所要讨论的事件性质一目了然。",x=250, y=390, alignment="left", size=24, delay=0.04, width=800)]
[Sticker(id="st4", multi = true, text="学生们妄图扰乱乌萨斯的秩序，他们拿起武器，摧毁封锁区的高墙，这无疑是处心积虑的谋反。",x=250, y=520, alignment="left", size=24, delay=0.04, width=800)]
[Sticker(id="st1", duration=1, block=false)]
[Sticker(id="st2", duration=1, block=false)]
[Sticker(id="st3", duration=1, block=false)]
[Sticker(id="st4", duration=1, block=false)]
[StopSound(channel="f", fadetime=0.5)]
[PlaySound(key="$d_avg_gateopen")]
[Dialog]
[StopSound(channel="bgs", fadetime=0.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="66_g12_deitygrypherburgmeeting",screenadapt="coverall")]
[PlaySound(key="$d_avg_crwddiscuss_inside",volume=0.8, channel="bgs", loop=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Stickerclear]
[charslot(slot = "m", name = "avg_npc_2171_1#1$1",duration=1,block=true)]
[Delay(time=1)]
[multiline(name="刻薄的贵族")]至于他们的“领袖”，所谓的“冬将军”——
[multiline(name="刻薄的贵族")]索尼娅·米哈伊里芙娜......
[name="刻薄的贵族"]更是彻头彻尾的，乌萨斯的叛徒。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2168_1#1$1", duration=1.5, block=true)]
[Delay(time=2)]
[name="仲裁人"]我尊重您的看法，尤苏波夫伯爵。但是在这场听证会得出结果之前，我们还无法轻易对这些学生下判断。
[name="仲裁人"]我也想再次提醒在座的各位，这场听证会最终的结果会直接定性“卡托加事件”。
[name="仲裁人"]对于这桩发生在伟大的圣骏堡、骇人听闻的恶性事件，我们必须进行公正而严肃的审议。
[name="仲裁人"]对于这些乌萨斯的未来——生活在圣骏堡的学生们，我们也要给出最公正的结果。
[StopSound(channel="bgs", fadetime=3)]
[charslot(slot = "m", name = "avg_npc_2171_1#1$1")]
[name="刻薄的贵族"]尊敬的仲裁人阁下，在开始之前，我还是有必要提醒您。
[name="刻薄的贵族"]现在站在议会大厦外的这些学生，他们的所作所为，直接伤害了乌萨斯的威严。
[name="刻薄的贵族"]乌萨斯的徽记在您的头顶之上，它在警醒我们，每一个乌萨斯人享有的荣耀究竟来源于何处。
[name="刻薄的贵族"]正如圣骏堡的过去属于诸位先皇，现在与将来应当属于当今陛下，以及在他身边拱卫乌萨斯意志的我们。
[name="刻薄的贵族"]如果我们不能审判索尼娅等人的叛国之罪，就等于把未来随手送给这帮少不更事的宵小......
[name="刻薄的贵族"]乌萨斯何以在这片大地立足？陛下的公正又何以彰显？
[charslot(slot = "m", name = "avg_npc_1981_1#1$1")]
[name="台下的贵族"]公正？你们也配妄言“陛下的公正”？
[name="台下的贵族"]没有律师，没有公诉人，没有陪审团......修订成文法的议案早在十几年前就给出来了，都是你们这些老古董在阻挠！
[charslot(slot = "m", name = "avg_npc_2171_1#1$1")]
[name="刻薄的贵族"]我得问问您，诸位“后起之秀”又为帝国做了什么？靠着挥舞切尔文金币，谋得半点爵位，现在还和叛国贼眉来眼去......
[name="刻薄的贵族"]别上陛下授予的勋章，从外边那些抗议的学生中走到这里高谈阔论，你们难道没有负责愧疚的器官吗？！
[dialog]
[charslot]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_gavel", volume=1)]
[Delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="72_g1_sjbstreet_d",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
与此同时，议会大厦外。
[dialog]
[charslot(slot = "l", name = "avg_npc_2177_1$2", posfrom="-100,0",posto="-100,0",duration=0.8)]
[charslot(slot = "r", name = "avg_npc_2182_1#1$1", posfrom="120,0",posto="120,0",duration=0.8)]
[charslot(slot = "m", name = "avg_npc_2187_1#1$1", posfrom="50,0",posto="50,0",duration=0.8)]
[delay(time=1.5)]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_2170_1#1$1", duration=1.5, block=true)]
[delay(time=1.5)]
[name="乌萨斯警察"]这群小鬼......
[charslot(slot = "m", focus="n")]
今天原本不是自己当值的日子。
而一大早，他在宿舍床上被紧急叫醒，上级告诉他，整个圣骏堡的学生都被动员了起来，他们围堵了议会大厦外的每一条街道。
他和同僚带好了完整的装备，做好了应对一场“战争”的准备，然而他们来到现场时才发现......
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_npc_2177

... (全文41271字符)
```

### level_act51side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="66_g12_deitygrypherburgmeeting",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$sjoyasorrow_intro",key="$sjoyasorrow_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_2168_1#1$1",duration=0.5)]
[Delay(time=1)]
[name="仲裁人"]肃静。
[name="仲裁人"]诸位，所有证人均已陈述完毕，相信诸位大人已从各方证词中得到了线索。
[name="仲裁人"]鉴于“卡托加事件”牵涉甚广，且证词存在诸多矛盾......
[name="仲裁人"]仲裁委员会需要时间对所有证据进行“闭门核查”。
[name="仲裁人"]现在宣布听证会流程到此结束。两小时后，我们将正式公布“卡托加事件”的最终审议结果。
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]......
[charslot(slot="m",name="avg_405_absin_1#7$1")]
[name="苦艾"]（压低声音）是时候了。
[charslot]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.4, channel="bgs",fadetime=2)]
七嘴八舌的讨论又一次在她四周响起，几位贵族不出所料地与仲裁人同行，走向厅内的过道。
苦艾摇了摇头，穿过熙熙攘攘的人群，走出门时，她回头对上书记官的目光。
书记官面无表情，视线仿佛穿透了她，落在虚无的空气中。但他不动声色地竖起了手中的记录本——
那上面一片雪白，空无一字。
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="72_g10_hallway",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_2168_1#1$1",duration=0.5)]
[Delay(time=1)]
[name="仲裁人"]呼......真是场漫长的闹剧。
[name="仲裁人"]难以置信，连特里波列夫家的小孩都会犯错。
[charslot(slot="m",name="avg_npc_2171_1#1$1")]
[name="焦虑的贵族"]不过，重点还是在索尼娅身上，仲裁人阁下，您打算怎么定性？
[charslot(slot="m",name="avg_npc_2168_1#1$1")]
[name="仲裁人"]这取决于我们需要她成为什么样的“反面教材”。
[charslot(slot="m",name="avg_npc_2171_1#1$1")]
[name="焦虑的贵族"]我们需要她是一个疯子，阁下。
[name="焦虑的贵族"]有的新贵族试图利用皇帝陛下狡辩，连“勤王护驾有功”这种鬼话都讲得出口。
[name="焦虑的贵族"]必须得放大索尼娅的危害性，不趁这个机会收拾那些暴发户，将来他们会变本加厉地颠倒黑白！
[charslot(slot="m",name="avg_npc_2168_1#1$1")]
[name="仲裁人"]......等特里波列夫公爵到了再一起决定，他还需要一些时间平复心情。
[dialog]
[charslot(slot = "m", focus = "n")]
[playsound(key="$d_avg_crwddiscuss_inside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.2, channel="bgs",fadetime=2)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_2168_1#1$1")]
[name="仲裁人"]等等......
[name="仲裁人"]这是什么声音？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="66_g12_deitygrypherburgmeeting",screenadapt="coverall")]
[SoundVolume(volume=0.4, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_npc_2170_1#1$1",duration=0.5)]
[Delay(time=1)]
[name="乌萨斯警察"]仲裁人阁下！
[charslot(slot="m",name="avg_npc_2168_1#1$1")]
[name="仲裁人"]发生什么事了？
[charslot(slot="m",name="avg_npc_2170_1#1$1")]
[name="乌萨斯警察"]有消息说，有一群歹徒突袭了三号监狱，劫走了许多犯人。
[name="乌萨斯警察"]因为这个事情，刚才大家都吵翻了，需要您来主持秩序。
[charslot(slot="m",name="avg_npc_2168_1#1$1")]
[name="仲裁人"]三号监狱这么随便就被突破了？
[charslot(slot="m",name="avg_npc_2170_1#1$1")]
[name="乌萨斯警察"]我们的警力都集中在这附近，余下的人不够提前发现那些歹徒，才导致了这一失误。
[charslot(slot="m",name="avg_npc_2168_1#1$1")]
[name="仲裁人"]......不对。
[name="仲裁人"]外面的学生呢？
[charslot(slot="m",name="avg_npc_2170_1#1$1")]
[name="乌萨斯警察"]他们刚刚都解散回家了，您的意思是......
[charslot(slot="m",name="avg_npc_2168_1#1$1")]
[name="仲裁人"]......
[name="仲裁人"]我的意思是，你们这些废物！赶紧找出带头的，把他抓回来！
[charslot(slot="m",name="avg_npc_2170_1#1$1")]
[name="乌萨斯警察"]是！
[StopSound(channel="bgs", fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="bg_cellroom_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_key")]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_2179_1#1$1",duration=0.5)]
[Delay(time=1)]
[name="积极的学生"]喂，醒醒！
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_2176_1#1$1",duration=1)]
[Delay(time=2)]
[name="拉列亚"]......你是？
[charslot(slot="m",name="avg_npc_2179_1#1$1")]
[name="积极的学生"]你就是拉列亚吧，这座监狱已经被我们攻占了。
[name="积极的学生"]趁他们的援军还没赶到，赶紧离开这里。
[charslot(slot="m",name="avg_npc_2176_1#1$1")]
[name="拉列亚"]我没有弄错吧......你们是来救我的吗？
[charslot(slot="m",name="avg_npc_2179_1#1$1")]
[name="积极的学生"]当然不止是你，你先出来。
[charslot]
惊喜与困意交织，拉列亚顶着发懵的脑袋，一步步地跨过倒在地上的狱警。
他的思绪飘荡，原来自己的威望已然如此......他要回到学生联合大会，成为不亚于奥尔佳的领袖角色。
[charslot(slot="m",name="avg_npc_2176_1#1$1")]
[name="拉列亚"]同学们......我的同胞们！
[name="拉列亚"]看着你们，我就知道，自由的火种从未熄灭！
[charslot(slot="m",name="avg_npc_2179_1#1$1")]
[playsound(key="$d_avg_crowdrun")]
[name="积极的学生"]二队！二队把缺口守住！这边的牢房都打开了！
[charslot(slot="m",name="avg_npc_2176_1#1$1")]
[name="拉列亚"]咳咳——
[name="拉列亚"]正如你们所见，虽然这漆黑的牢笼禁锢了我的肉体，但它无法禁锢我的——
[dialog]
[charslot(slot="r",name="avg_npc_2182_1#1$1",posfrom = "150,0", posto = "0,0",duration=0.5)]
[Delay(time=1)]
[charslot(slot = "m", focus = "r")]
[name="匆忙的学生"]借过！别挡道！
[dialog]
[charslot(slot="r",posfrom = "0,0", posto = "-250,0",duration=0.81,afrom=1,ato=0, focus = "r")]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_2176_1#1$1")]
[name="拉列亚"]......没关系。
[name="拉列亚"]我知道，你们是为了我而来的。为了——
[charslot(slot = "m", focus = "n")]
没有一个人回应他......他看着面前眼熟的各个身影，却发觉这群昔日的同学不知何时已经变得陌生。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="72_g1_sjbstreet_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[charslot(slot="m",name="avg_194_leto_1#1$1",duration=0.5)]
[Delay(time=1)]
[name="烈夏"]啊啊，累死我了。
[name="烈夏"]我刚从那鬼地方跑出来，又要和你们干这一票。
[charslot(slot="m",name="avg_1051_headb2_1#1$1")]
[name="凛冬"]别抱怨了，卓娅都没说什么呢。
[charslot(slot="m",name="avg_405_absin_1#4$1")]
[name="苦艾"]索尼娅，你的想法一直都这么大胆吗？
[name="苦艾"]没想到我们居然真的能在那些人的眼皮子底下玩出这套......
[charslot(slot="m",name="avg_npc_2156_1#1$1")]
[name="真理"]卓娅，先前你主动提出要出席听证会拖延时间，我们还担心了好久。
[name="真理"]本来娜塔莉娅都找人安排好了，不用让你去冒这么大风险。
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]古米本来也不用全程参与行动的，可她还是来了。
[charslot(slot="m",name="avg_1051_headb2_1#4$1")]
[name="凛冬"]哼，说到这个......
[charslot(slot="m",name="avg_196_sunbr_1#19$1")]
[name="古米"]凛冬姐——
[name="古米"]我已经道过歉啦！而且，我不也没怎么受伤吗？真理姐还说我

... (全文19945字符)
```

### training_act51side_01_a

```
[header(is_skippable=false, is_tutorial=true)]

[battle.pause(pause=true)]
[inputblocker(blockInput=true, black=0.3)]

[popupdialog(dialogHead="$avatar_leto")]嘿嘿，这个拐角是个埋伏的好地方，冬将军！

[Tutorial(tileX=4, tileY=3, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_leto", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这声音是......等等！我身后这座<@tu.kw>警戒塔</>，它好像会动？

[popupdialog(dialogHead="$avatar_headb2")]小心！它每隔一段时间就会朝顺时针方向旋转九十度！

[popupdialog(dialogHead="$avatar_headb2")]警戒塔会<@tu.kw>持续攻击所有暴露在它视野范围内的我方目标</>，并且每次攻击都会增强火力，直到<@tu.kw>将其全部击退</>后才会再次准备转向。

[popupdialog(dialogHead="$avatar_headb2", protectTime=0.5)]烈夏！别上去硬碰硬，优先和它周旋，寻找机会！

[battle.pause(pause=false)]
```

### training_act51side_01_b

```
[header(is_skippable=false, is_tutorial=true)]
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]

[inputblocker(blockInput=true, black=0.3)]
[popupdialog(dialogHead="$avatar_leto")]不好，它好像发现我了！

[InputBlocker(blockInput=false, black=0)] 
[Tutorial(protectTime=0.5,waitForSignal="put_down", dialogHead="$avatar_headb2", animStyle="Drag", \
           startCardIndex=0, startRightStart=true, endTileX=4, endTileY=4)] \
快使用<@tu.kw>伪装工具</>！潜伏起来！

[inputblocker(blockInput=true, black=0.3)]

[popupdialog(dialogHead="$avatar_leto")]这就是你从那个瑞柏巴朋友那里借来的好东西？它有什么用？

[popupdialog(dialogHead="$avatar_headb2")]它能让你在一段时间内不被敌人发现，但也<@tu.kw>无法再阻挡敌人</>。使用它潜伏时不会释放自动触发技能，一旦手动释放技能，就会<@tu.kw>解除潜伏状态</>。

[popupdialog(dialogHead="$avatar_headb2", protectTime=0.5)]别担心，我来解决剩下的那些家伙！

[battle.pause(pause=false)]
```

### training_act51side_01_c

```
[header(is_skippable=false, is_tutorial=true)]
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]

[popupdialog(dialogHead="$avatar_headb2")]时间紧迫，要不了多久，警戒塔就会转向我这边......

[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]

[InputBlocker(blockInput=true, validX=290, validY=60, validWidth=100, validHeight=100)]

[Tutorial(waitForSignal="char_info", focusX=290, focusY=60, focusWidth=100, focusHeight=100, \
          animStyle="Click", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_headb2", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
看我将他们一网打尽！
[InputBlocker(blockInput=true)]

[battle.pause(pause=false)]
```

### training_act51side_01_d

```
[header(is_skippable=false, is_tutorial=true)]
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]


[inputblocker(blockInput=false)]
[Tutorial(protectTime=0.5,waitForSignal="put_down", dialogHead="$avatar_headb2", animStyle="Drag", \
           startCardIndex=0, startRightStart=true, endTileX=7, endTileY=3)] \
就是现在，时间卡得刚刚好！

[inputblocker(blockInput=true, black=0.3)]

[popupdialog(dialogHead="$avatar_headb2")]烈夏，我该使用<@tu.kw>伪装工具</>了，警戒塔短时间内还不会转向你那边，剩下的敌人就交给你了！

[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[Battle.EnsureMinSp(charId="char_194_leto", sp=40)]

[popupdialog(dialogHead="$avatar_leto")]没问题！是不是我只要主动释放技能，就能<@tu.kw>提前解除潜伏状态</>？

[InputBlocker(blockInput=true, tileY=4, tileX=4, validWidth=110, validHeight=110)]

[Tutorial(waitForSignal="char_info", tileX=4, tileY=4, focusWidth=110, focusHeight=110, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_headb2", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
	  正是这样！现在就用技能解决掉他们！

[battle.pause(pause=false)]
```

### training_act51side_01_e

```
[header(is_skippable=false, is_tutorial=true)]
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]
[inputblocker(blockInput=true, black=0.3)]

[popupdialog(dialogHead="$avatar_leto")]警戒塔好像又要转过来了！

[Tutorial(tileX=4, tileY=1, focusWidth=110, focusHeight=110,\
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_crosly")] \
别忘了，我们还得解救被关押在禁闭所里的人。

[popupdialog(dialogHead="$avatar_crosly")]将干员部署在禁闭所<@tu.kw>周围4格</>，从而击破它！

[popupdialog(dialogHead="$avatar_crosly")]就像这样。

[battle.pause(pause=false)]
```

### training_act51side_01_f

```
[header(is_skippable=false, is_tutorial=true)]
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]
[inputblocker(blockInput=true, black=0.3)]

[popupdialog(dialogHead="$avatar_leto")]多谢了，弑君者，你救出了我们的同学。

[popupdialog(dialogHead="$avatar_leto")]不好，击破禁闭所时好像触发了某种警报，警戒塔朝那边转过去了！

[Tutorial(cardIndex=0, rightStart=true, focusWidth=110, focusHeight=110, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_crosly", dialogX="$f_lower_dialog_pos_x",  \
          dialogY="$f_lower_dialog_pos_y")] \
不必慌张，救出他们，就意味着我们能<@tu.kw>获得新的伪装工具</>，还有一些<@tu.kw>部署费用</>。

[popupdialog(dialogHead="$avatar_crosly")]给我一个<@tu.kw>伪装工具</>，是该它派上用场的时候了。

[popupdialog(dialogHead="$avatar_crosly")]记好了，这些东西制作不易，别浪费，但也别总是省着不舍得用！

[battle.pause(pause=false)]
```


## 统计

- 总字符数：490675
- 对话行数：3664


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
