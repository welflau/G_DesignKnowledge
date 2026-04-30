# 明日方舟 · 活动剧情 · act33side（38段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act33side」完整剧情脚本（38个文件，3289行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act33side
- 脚本文件数：38

### act33side_09_a1

```
[HEADER(is_tutorial=true, is_skippable=false)] 活动33side教学关1_a1

[delay(time="2")]
[Battle.Pause]

[Tutorial(protectTime=0.5, dialogHead="$avatar_mamiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
欸，特蕾西娅小姐......发生了什么？

[Tutorial(protectTime=0.5, dialogHead="$avatar_tersia", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
阿米娅，接下来的事情，就交给我来处理吧。
```

### act33side_09_a2

```
[header]

[avatarId="", isAvatarRight="FALSE"]警告：PRTS系统权限读写中......
[avatarId="", isAvatarRight="FALSE"]内部序列开始检索，检索到管理员权限。
[avatarId="", isAvatarRight="FALSE"]是否确认关闭全舰防御系统......已确认。
[avatarId="", isAvatarRight="FALSE"]最优路线计算完成，数据已上传。安全窗口倒计时开始，PRTS系统待机中......
[delay(time="1")]

[resetcamera]
[end]
```

### act33side_09_b

```
[header(actId="act33side")]

[camerafocusto(offsetX="5", offsetY="3", time="3", scale="FAR")]
[delay(time="2")]
[name="特蕾西娅", avatarId="npc_1296_tersia", isAvatarRight="FALSE"]这就是你最后的决定吗，博士？
[name="特蕾西娅", avatarId="npc_1296_tersia", isAvatarRight="FALSE"]而我的同胞们，我敬佩你们赴死的决心。
[delay(time="1")]


[end]
```

### act33side_09_c

```
[HEADER(is_tutorial=true, is_skippable=false)]

[delay(time="1")]
[camerafocusto(offsetX="7", offsetY="3", time="2", scale="FAR")]
[avatarId="", isAvatarRight="FALSE"]检测到未识别目标！警报即将启动——管理员权限介入，警报已取消。
[avatarId="", isAvatarRight="FALSE"]指挥系统已加载最优路线数据，战术配置已完成。
[avatarId="", isAvatarRight="FALSE"]安全窗口倒计时开始，请尽快采取行动......
[delay(time="1")]
[resetcamera]
[end]
```

### act33side_09_d

```
[HEADER(is_tutorial=true, is_skippable=true)]

[InputBlocker(blockInput=true)]
[Delay(time=1)]


[Tutorial(tileY=4, tileX=8, focusWidth=80, focusHeight=80, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \



```

### act33side_09_e

```
[header(actId="act33side")]

[camerafocusto(id="enemy_1552_mmamiy", offsetY=0.5, offsetX=0, scale="MID", time="1")]
[name="阿米娅", avatarId="npc_1295_amiya", isAvatarRight="FALSE"]特蕾西娅小姐，你用什么力量把我包裹起来了吗？我怎么看不见也听不见......
[camerafocusto(id="enemy_3006_tersia", offsetY=0.5, offsetX=0, scale="MID", time="1")]
[delay(time="1")]
[name="特蕾西娅", avatarId="npc_1296_tersia", isAvatarRight="TRUE"]阿米娅，我从未想到最后的结局会是这样。

[end]
```

### act33side_09_f

```
[header(actId="act33side")]

[camerafocusto(offsetX="4", offsetY="3", time="1", scale="CLOSE")]
[delay(time="1")]
[name="特蕾西娅", avatarId="npc_1296_tersia", isAvatarRight="FALSE"]再见了，阿米娅。等你醒来，一切都会结束......
[resetcamera]

[end]
```

### act33side_09_s

```
[HEADER(is_tutorial=true, is_skippable=false)]

[camerafocusto(id="enemy_3006_tersia", offsetY=0.5, offsetX=0, scale="MID", time="1")]
[name="特蕾西娅", avatarId="npc_1296_tersia", isAvatarRight="TRUE"]我本以为我们还有更多的时间......
[name="特蕾西娅", avatarId="npc_1296_tersia", isAvatarRight="TRUE"]“魔王”......我本不该如此仓促地将这个重担交给你。
[name="特蕾西娅", avatarId="npc_1296_tersia", isAvatarRight="TRUE"]但真相对现在的你来说太过残忍。对与错，未来的你自有判断。
[delay(time="1")]
[camerafocusto(offsetX="4", offsetY="3", time="1", scale="FAR")]
[end]
```

### act33side_10_a

```
[HEADER(is_tutorial=true, is_skippable=false)] 活动33side

[Tutorial(protectTime=0.5, dialogHead="$avatar_doctor", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y",animStyle="NoWait")] \
我的记忆......在消散......
[Delay(time=3)]

[Tutorial(protectTime=0.5, dialogHead="$avatar_tersia",animStyle="NoWait")] \
剪断来自过往的一切之后，去找到真正的自己吧，博士。
[Delay(time=3)]

[Tutorial(protectTime=0.5, dialogHead="$avatar_tersia",animStyle="NoWait")] \
阿米娅......
[Delay(time=3)]

[Tutorial(protectTime=0.5, dialogHead="$avatar_tersia",animStyle="NoWait")] \
果然，阿米娅在你的心中分量如此之重，是直到最后都希望保护的记忆......
[Delay(time=3)]
```

### level_act33side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="49_g8_scarmarketcamp",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[interlude(maskid = "ui_cutin_mask_horizon", style = 1, size = "1280, 100",offset = "0,0", channel = 2)]
[interlude(channel = 2, type = 2, name = "bg_black", afrom = 0, ato = 1, aduration = 0.3,sfrom = "1.3,1.3", sto = "1.3,1.3", sduration = 0, block = false)]
[Sticker(id="st1",  text="六十四年前", duration=1,x=300,y=325, alignment="center", size=24, delay=0, width=700,block="false")]
[Sticker(id="st2", text="1030年秋" ,duration=1,x=300,y=365, alignment="center",size=24, delay=0, width=700)]
[Sticker(id="st1", duration=1)]
[Sticker(id="st2", duration=1)]
[interlude(channel = 2, clear = true)]
[Delay(time=1.5)]
卡兹戴尔地区，疤痕商场
[dialog]
[Delay(time=1)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[playsound(key="$d_avg_talentmarket", loop=true, channel="bgs1",volume=0)]
[playsound(key="$d_avg_lavarollp", loop=true, channel="bgs2",volume=0)]
[SoundVolume(volume=0.5, channel="bgs1",fadetime=2)]
[SoundVolume(volume=0.3, channel="bgs2",fadetime=2)]
[charslot(slot = "m",name="avg_npc_053",duration = 1)]
[delay(time=1.5)]
[name="负伤的雇佣兵"]把脖子上的牌子给我死死护好！你可是我宝贵的财产，奴隶！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="负伤的雇佣兵"]听懂了吗！*萨卡兹粗口*，你最好值点钱。
[dialog]
[charslot]
[Delay(time=1)]
[charslot(slot = "m",name="avg_npc_1305_1#8$1",duration = 1)]
[delay(time=1.5)]
[name="胆怯的奴隶"]......
[charslot(slot = "m",name="avg_npc_053")]
[name="负伤的雇佣兵"]待在这别动。你是负责验货的？
[charslot]
[dialog]
[charslot(slot = "m",name="avg_npc_1306_1#1$1",duration = 1)]
[delay(time=1.5)]
奴隶商人只瞥了一眼雇佣兵背后沉默的奴隶，便轻轻摇了摇头。
[name="奴隶商人"]货哪来的？
[charslot(slot = "m",name="avg_npc_053")]
[name="负伤的雇佣兵"]他路上快渴死了，被我从裂兽的爪子下面抢过来的。
[charslot(slot = "m",name="avg_npc_1305_1#8$1")]
[name="胆怯的奴隶"]我......从卡兹戴尔来......我可以找人......
[charslot(slot = "m",name="avg_npc_1306_1#1$1")]
[name="奴隶商人"]我们不关心你从哪里来，奴隶。如果有人来赎你，你说自己是东国人都行。
[name="奴隶商人"]我只是确认一下你是不是“有尾巴”，这些佣兵总是冒冒失失的。
[charslot(slot = "m",name="avg_npc_053")]
[name="负伤的雇佣兵"]我可以保证货的来源干净。
[charslot(slot = "m",name="avg_npc_1306_1#1$1")]
[name="奴隶商人"]你最好说的是真话。换钱还是换东西？
[charslot(slot = "m",name="avg_npc_053")]
[name="负伤的雇佣兵"]换钱我没命花，我想换点好用的武器。
[charslot(slot = "m",name="avg_npc_1306_1#1$1")]
[name="奴隶商人"]你说了算。他勉强算次等货，值两把新铸的刀。
[charslot(slot = "m",name="avg_npc_053")]
[playsound(key="$d_avg_exsheath")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="负伤的雇佣兵"]......你再好好看看我的货！
[charslot(slot = "m",name="avg_npc_1306_1#1$1")]
[name="奴隶商人"]你给次等货套上好衣服，他也还是次等货，不接受我们的出价可以滚。
[name="奴隶商人"]还有，把你的刀收好......
[name="奴隶商人"]这里是疤痕商场。
[dialog]
[playsound(key="$d_avg_unsheathe")]
[charslot(slot = "m",name="avg_npc_053")]
[delay(time=1)]
[name="负伤的雇佣兵"]......能再加点吗？我从莱塔尼亚边境过来，手里还有些关于核心圈的混战的一手情报——
[charslot(slot = "m",name="avg_npc_1306_1#1$1")]
[name="奴隶商人"]一个提醒，来这就学着管好自己的嘴。
[name="奴隶商人"]号称自己有需要花钱买的一手情报？你猜猜你的下场会是什么样的。
[name="奴隶商人"]把货留下赶紧滚吧，后面还排着队呢。
[charslot(slot = "m",name="avg_npc_053")]
[name="负伤的雇佣兵"]唔。
[charslot(slot = "m",name="avg_npc_1306_1#1$1")]
[name="奴隶商人"]觉得不爽？可以去那边的酒吧灌点我们老大“疤眼”特酿的好酒。呵，没钱也无所谓，他们会接受你拿手里的武器抵押，佣兵。
[charslot(slot = "m",name="avg_npc_053")]
[name="负伤的雇佣兵"]还有......你们的悬赏委托在哪领？我是来赚大钱的。
[charslot(slot = "m",name="avg_npc_1306_1#1$1")]
[name="奴隶商人"]酒吧会有人很乐意告诉你的。
[charslot(slot = "m",name="avg_npc_053")]
[name="负伤的雇佣兵"]*萨卡兹粗口*。
[dialog]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[StopSound(channel="bgs1", fadetime=3)]
[SoundVolume(volume=0.6, channel="bgs2",fadetime=3)]
[background(screenadapt="coverall", image="49_g8_scarmarketcamp",xScale=1.3, yScale=1.3,y=30)]
[backgroundTween(duration=30, yTo=70,block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
佣兵望向了这座隐藏在卡兹戴尔地下巨大空洞中的悬空聚集地。
他的耳边除了奴隶们的呻吟，还隐约可以听到商场下方源石粉尘不断爆鸣与熔岩翻滚的声音。
望着险峻的道路，他回味起从地面上一路涉险深入到集市的路程，不禁胆寒。
[Dialog]
[SoundVolume(volume=0.3, channel="bgs2",fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[charslot(slot = "m",name="avg_npc_053")]
[background(screenadapt="coverall", image="49_g8_scarmarketcamp")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs3",volume=0)]
[SoundVolume(volume=0.4, channel="bgs3",fadetime=3)]
[name="负伤的雇佣兵"]这下面的深沟里到底堆了......多少人？
[charslot(slot = "m",name="avg_npc_1306_1#1$1")]
[name="奴隶商人"]跳下去摔不死的程度。欢迎来到疤痕商场，新人，你会爱上这的。
[charslot(slot = "m",name="avg_npc_053")]
[name="负伤的雇佣兵"]......那边呢？为什么这么多人？
[charslot(slot = "m",name="avg_npc_1306_1#1$1")]
[name="奴隶商人"]准是又来了什么大人物。
[name="奴隶商人"]你不是要“赚大钱”吗，去啊。我可不愿多管闲事。
[charslot]
佣兵隐约看到了一道白色的身影闪过了凌乱灰暗的街道。
白色的衣服？这在卡兹戴尔地区并不常见。
[charslot(slot = "m",name="avg_npc_053")]
[name="负伤的雇佣兵"]......
[dialog]
[charslot]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_1297_1#1$1",duration=1.5,posfrom = "-200,0", posto = "0,0",bstart=0.15,bend=0.5)]
[delay(time=2)]
[name="？？？"]你受伤了。
[charslot(slot = "m",name="avg_npc_053")]
[name="负伤的雇佣兵"]用不着你管。
[CameraShake(duration=0.2, xstrength=10, ystrength=15, vibrato=25, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m",name="avg_npc_1306_1#1$1")]
[name="奴隶商人"]呃！咳咳！你——
[charslot(slot = "m",name="avg_npc_053")]
[name="负伤的雇佣兵"]......？
[charslot(slot="m",name="avg_npc_1297_1#1$1",bstart=0.15,bend=0.5)]
[name="？？？"]我上次来的时候，在这里负责交易的是另外一个人。
[charslot(slot = "m",name="avg_npc_1306_1#1$1")]
[name="奴隶商人"]呃。是的......
[name="奴隶商人"]那是我的祖父，他到死之前都一直以和您交过手来向我们吹嘘。
[name="奴隶商人"]您竟然还记得他，挺好，说明老头没有说胡话。那已经是六十年前了......
[name="奴隶商人"]......特雷西斯将军。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1297_1#1$1",duration=1)]
[delay(time=2)]
[name="特雷西斯"]是吗？可惜这里还是没有任何变化。
[charslot(slot = "m",name="avg_npc_1306_1#1$1")]
[name="奴隶商人"]想必那位殿下也来了，这次总不能又打起来吧？
[name="奴隶

... (全文20954字符)
```

### level_act33side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[warp(name="chiyu01")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="49_g4_kazdelstreet_shabby",screenadapt="coverall")]
[PlayMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
1031年秋
卡兹戴尔地区，卡兹戴尔移动城市
[dialog]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.6, channel="bgs",fadetime=2)]
[charslot(slot = "left", name = "avg_npc_932_1#1$1",duration = 1,bstart=0.2,bend=0.7,posfrom = "50,0", posto = "50,0")]
[Delay(time=1)]
[charslot(slot = "right", name = "avg_npc_934_1#1$1",duration = 1,bstart=0.2,bend=0.7,posfrom = "-50,0", posto = "-50,0")]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1305_1#1$1",duration=1,focus="n")]
[delay(time=2)]
[PlaySound(key="$d_avg_clothmovement")] 
[CameraShake(duration=0.5, xstrength=10, ystrength=5, vibrato=10, randomness=90, fadeout=false, block=false)]
[charslot(slot = "m",posfrom = "0,0", posto = "100,0",duration = 0.8)]
[charslot(slot = "right",duration = 1,posfrom = "-50,0", posto = "150,0",afrom=1,ato=0)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1305_1#1$1",focus="m")]
[name="好运"]让让，让让......让我过去！
[dialog]
[PlaySound(key="$d_avg_clothmovement")] 
[charslot(slot = "m",posfrom = "100,0", posto = "0,0",duration = 0.7)]
[delay(time=0.2)]
[charslot(slot = "left", duration = 0.5,posfrom = "50,0", posto = "-30,0")]
[delay(time=0.7)]
[PlaySound(key="$bodyfalldown2")] 
[CameraShake(duration=0.3, xstrength=20, ystrength=15, vibrato=30, randomness=90, fadeout=false, block=false)]
[charslot(slot = "left", duration = 0.3,posfrom = "-30,0", posto = "50,0")]
[charslot(slot = "m",posfrom = "0,0", posto = "200,0",duration = 0.7)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_932_1#1$1",duration=0.5)]
[Delay(time=0.8)]
[charslot(slot = "left", name = "avg_npc_932_1#1$1",focus="l")]
[name="不耐烦的平民"]别挤！想占好位置？拿矿区出的高纯度源石块和我换。
[dialog]
[charslot(slot="m",name="avg_npc_1305_1#3$1")]
[charslot(slot = "m", focus = "all")]
[PlaySound(key="$d_avg_paper2")] 
[CameraShake(duration=0.3, xstrength=20, ystrength=15, vibrato=20, randomness=90, fadeout=false, block=true)]
[Delay(time=1)]
[charslot(slot = "left", name = "avg_npc_932_1#1$1",focus="l")]
[name="不耐烦的平民"]欸，你怎么还抢我的传单！呃，你身上的血都臭了......
[charslot(slot="m",name="avg_npc_1305_1#7$1",focus="m")]
[name="好运"]钻那些死人的房子总是难免嘛。林......贡......斯，这传单上画的这地方应该是这么念的吧？
[name="好运"]林贡斯是个什么地方啊？
[charslot(slot = "left", name = "avg_npc_932_1#1$1",focus="l")]
[name="不耐烦的平民"]高卢。
[charslot(slot="m",name="avg_npc_1305_1#7$1",focus="m")]
[name="好运"]哦，高卢在哪？
[charslot(slot = "left", name = "avg_npc_932_1#1$1",focus="l")]
[name="不耐烦的平民"]......我*萨卡兹粗口*怎么知道高卢在哪！
[charslot(slot="m",name="avg_npc_1305_1#7$1",focus="m")]
[name="好运"]啧，凶什么？
[charslot(slot = "left", name = "avg_npc_932_1#1$1",focus="l")]
[name="不耐烦的平民"]别嚷嚷，两位殿下和王庭的大人物们在议事厅谈话呢。听说是要整顿城市，你没看这两天街上的卫兵又多起来了？
[name="不耐烦的平民"]小心点吧！
[charslot(slot="m",name="avg_npc_1305_1#3$1",focus="m")]
[name="好运"]唉。今天天气真闷。
[stopmusic(fadetime=2)]
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="49_g7_councilchamber",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1297_1#1$1",duration=1)]
[delay(time=1.5)]
[name="特雷西斯"]话已说完。
[name="特雷西斯"]军事委员会取代战争议会，帮助魔王特蕾西娅决策卡兹戴尔的军政要务。
[name="特雷西斯"]卡兹戴尔的正式管理者从此只有军事委员会，没有人再有权力以王庭的名义对萨卡兹发布任何一条命令。
[name="特雷西斯"]具体的决议诸位都已提前收到。那么，各位仍留恋战争议会之名的王庭之主们......
[name="特雷西斯"]今后，卡兹戴尔军事委员会将成为萨卡兹最后的、永恒的堡垒，也将为萨卡兹带来新的秩序。
[charslot(slot="m",name="avg_npc_1296_1#1$1")]
[name="特蕾西娅"]还有其他疑问吗？
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1071_1#3$1",duration=1.5)]
[delay(time=2)]
[name="女妖"]......殿下，您看上去比昨日更憔悴了。
[name="女妖"]注意您自己的身体，有再多个军事委员会——
[name="女妖"]——我们也不能失去特蕾西娅殿下您。
[charslot(slot="m",name="avg_npc_1297_1#1$1")]
[name="特雷西斯"]......
[charslot(slot="m",name="avg_npc_1296_1#8$1")]
[name="特蕾西娅"]菈玛莲......谢谢。
[charslot(slot="m",name="avg_npc_1071_1#7$1")]
[name="菈玛莲"]我清楚您为了今天付出了多少努力......也清楚，如今的卡兹戴尔如何看待躲藏在河谷之中的女妖们。
[charslot(slot="m",name="avg_npc_1297_1#1$1")]
[name="特雷西斯"]......
[charslot(slot="m",name="avg_npc_1071_1#1$1")]
[name="菈玛莲"]不过呢，在我们表态之前......我在来的路上碰上了迷路的巫妖特使，他有一封信希望转交给你们。
[name="菈玛莲"]这说明卡兹戴尔确实变化很大，那位特使甚至没能找到通往这里的路。
[charslot(slot="m",name="avg_npc_1296_1#3$1")]
[name="特蕾西娅"]唔......是从莱塔尼亚抵达这里的信件。
[charslot(slot="m",name="avg_npc_1071_1#1$1")]
[name="菈玛莲"]如果不出所料，殿下的信使应该仍旧没有得到独眼巨人们的半点消息。
[name="菈玛莲"]那么比起掩埋在风雪深处的声音，还是听听莱塔尼亚的巫妖们作何回答吧。
[charslot(slot="m",name="avg_npc_1296_1#2$1")]
[name="特蕾西娅"]你说得对。萨卡兹......许久没能真正团结在一起了。
[dialog]
[playsound(key="$d_avg_paper1")]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1296_1#3$1")]
[name="特蕾西娅"]嗯......？
[charslot(duration=1)]
信纸上的华美文字化作丝线，纠缠浮现于纸面之上，最终形成了一个熟悉的身影。
[dialog]
[Background(image="bg_black",screenadapt="coverall",fadetime=2)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1114_1#7$1",duration=1.5)]
[delay(time=2)]
[name="菈玛莲"]弗莱蒙特，久居莱塔尼亚的巫妖。看来现在的“誊录”是他了。
[name="特蕾西娅"]看来巫妖们在莱塔尼亚运用法术的风格发生了些变化。唔，他的神情似乎非常激动。
[name="特蕾西娅"]......
[name="特蕾西娅"]......可为什么光有影像，却没有任何声音？
[name="菈玛莲"]......呵呵。
[name="菈玛莲"]那位巫妖特使暗示过我，他实在很苦恼如何润色老师的措辞......我也没想到他干脆抹去了声音。
[name="菈玛莲"]总之，弗莱蒙特表达了巫妖们的歉意。他们仍然醉心知识，实在无法分心长途跋涉来相聚。
[name="菈玛莲"]但倘若卡兹戴尔需要他们的知识，巫妖很乐意为他们选中的人敞开圣殿之门。
[name="菈玛莲"]......当然，我想以殿下的能耐，也能从影像里看出弗莱蒙特的态度才是。看来他还是对激烈的变革过敏。
[dialog]
[charslot(duration=1)]
[Background(image="49_g7_councilchamber",screenadapt="coverall",fadetime=2)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1071_1#1$1")]
[name="菈玛莲"]对了，这里还有另一封弗莱蒙特交给将军的私人信件。
[charslot(slot="m",name="avg_npc_1297_1#1$1")]
[name="特雷西斯"]......可是，菈玛莲，你可不是谁的信使。
[name="特雷西斯"]你还没有表达女妖王庭的态度。
[charslot(slot="m",name="avg_npc_1071_1#1$1")]
[name="菈玛莲"]将军，我想昨日叙旧时我们已经达成了共识——女妖不会参与其中。
[cha

... (全文25530字符)
```

### level_act33side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[dialog]
[interlude(maskid = "ui_cutin_mask_horizon", style = 1, size = "1280, 100",offset = "0,0", channel = 2)]
[interlude(channel = 2, type = 2, name = "bg_black", afrom = 0, ato = 1, aduration = 0.3,sfrom = "1.3,1.3", sto = "1.3,1.3", sduration = 0, block = false)]
[Sticker(id="st1",  text="二十六年前", duration=1,x=300,y=325, alignment="center", size=24, delay=0, width=700,block="false")]
[Sticker(id="st2", text="1068年秋" ,duration=1,x=300,y=365, alignment="center",size=24, delay=0, width=700)]
[Sticker(id="st1", duration=1)]
[Sticker(id="st2", duration=1)]
[interlude(channel = 2, clear = true)]
[Delay(time=1.5)]
莱塔尼亚，瓦瑟领大区
[dialog]
[Delay(time=1)]
[PlayMusic(intro="$loading_intro", key="$loading_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_493_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_370_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", focus="l")]
[name="和蔼的文官"]您觉得这首曲子如何？
[charslot(slot = "right", focus="r")]
[name="拉特兰修士"]如顽童从昏睡中苏醒，狂奔出门，尽情嬉闹。栩栩如生。
[charslot(slot = "left", focus="l")]
[name="和蔼的文官"]其实这首曲子正是选帝侯阁下本人所作，受启发于三十八年前，也就是如今的教宗阁下还任拉特兰信使之际，拜访瓦瑟领大区的情景。
[name="和蔼的文官"]年轻热情的教宗阁下向孩子们讲述他的见闻......伊比利亚守望的大海，米诺斯史诗与阴谋共存的雅赛努斯城。
[name="和蔼的文官"]还有......被一语带过的，卡兹戴尔那座不知在何处的罪恶之都。
[name="和蔼的文官"]正巧选帝侯阁下也在现场，对教宗阁下描绘的经历如痴如醉。
[name="和蔼的文官"]可惜的是，虽然选帝侯阁下当时便谱下了初稿希望赠给教宗阁下，但总是难以满意，于是多年来一直修修改改。
[name="和蔼的文官"]直到前段日子，我们的斥候终于找到了魔族佬那座鲜为世人所窥探的移动城市的踪迹......并发回了相片。
[name="和蔼的文官"]选帝侯阁下凝视那座城市留下的巨大辙印时终于找到了曲中缺失的元素——野性，并最终完成了此曲。
[charslot(slot = "right", focus="r")]
[name="拉特兰修士"]......你们找到了卡兹戴尔？
[charslot(slot = "left", focus="l")]
[name="和蔼的文官"]是的。选帝侯阁下也极为感慨，此曲的命运原来早已与那座城市联系在一起。
[charslot(slot = "right", focus="r")]
[name="拉特兰修士"]在我要回拉特兰述职的这个节点上，选帝侯阁下拿出这首曲子......我明白是什么意思。
[name="拉特兰修士"]但如今，教宗阁下并不打算对萨卡兹付诸武力，他对萨卡兹的态度与以往百年的教宗都天差地别。
[name="拉特兰修士"]他并不热衷于无故审判无罪之人。选帝侯阁下恐怕会失望了。
[charslot(slot = "left", focus="l")]
[name="和蔼的文官"]无妨，选帝侯阁下说过，与那座无足轻重的城市相比，他更在乎和惶恐的是教宗阁下本人对此曲的评价。
[name="和蔼的文官"]此行就麻烦您了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r",posfrom = "0,0", posto = "200,0",duration = 1,afrom=1,ato=0)]
[delay(time=2.5)]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r",name = "avg_npc_1134_1#1$1",posfrom = "200,0", posto = "0,0",duration = 1.5)]
[delay(time=2)]
[charslot(slot = "right", focus="r")]
[name="传令官"]阁下，叙拉古的回信我们已经收到了。只有少数家族同意配合我们行动。他们的人很快就能跟上我们的主力舰队。
[charslot(slot = "left", focus="l")]
[name="和蔼的文官"]哼，拉特兰竟然拒绝了我们......那就告诉叙拉古人，速度要快，我们必须赶在其他大区反应过来之前就率先扫清那座城市。
[name="和蔼的文官"]只有拿下卡兹戴尔的领土，我们才不会被其他选帝侯抢占先机。当年高卢那一战，我们已经错失了太多机会。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="49_g9_cyclopsroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
卡兹戴尔地区，疤痕商场
[dialog]
[charslot(slot="m",name="avg_npc_1294_1#1$1",duration=1.5)]
[delay(time=2)]
[name="“疤眼”"]我喜欢你们莱塔尼亚人，你们总是给我带来很多的生意。
[name="“疤眼”"]你很聪明，混在被劫掠的走私队伍里装作俘虏，而不是打着信使的旗号。
[name="“疤眼”"]在我对你失去耐心前，直接说你们想要什么。
[name="“疤眼”"]交易，委托，消息，疤痕商场总有满足你们需要的业务。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_492_1#1$1",duration=1)]
[delay(time=2)]
[name="强装镇定的使者"]合作，首领阁下。
[charslot(slot="m",name="avg_npc_1294_1#1$1")]
[name="“疤眼”"]“合作”不在我们的公开价目单上。
[name="“疤眼”"]你确定你的选帝侯阁下能出得起我心里的价格吗？
[charslot(slot="m",name="avg_npc_492_1#1$1")]
[name="强装镇定的使者"]您不先问问合作的具体内容吗？
[charslot(slot="m",name="avg_npc_1294_1#1$1")]
[name="“疤眼”"]在这，没有什么是出钱办不了的，卡普里尼。
[charslot(slot="m",name="avg_npc_492_1#1$1")]
[name="强装镇定的使者"]如果是拿下卡兹戴尔呢？
[charslot(slot="m",name="avg_npc_1294_1#1$1")]
[name="“疤眼”"]......说说看。
[charslot(slot="m",name="avg_npc_492_1#1$1")]
[name="强装镇定的使者"]选帝侯阁下希望你们能够破坏城市的动力系统，其他什么都不用做。
[name="强装镇定的使者"]给您的订金已经送到了，就在您从我车里扣下的保险箱内。
[name="强装镇定的使者"]之后的报酬，选帝侯阁下可以在卡兹戴尔城内和您细聊。
[charslot(slot="m",name="avg_npc_1294_1#1$1")]
[name="“疤眼”"]你的胆子很大，我很喜欢。那为了表达我的诚意，就免费送你们一份占卜来的重要消息吧。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="49_g2_kazdelstreet_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
卡兹戴尔地区，卡兹戴尔移动城市
[dialog]
[charslot(slot="m",name="avg_npc_932_1#1$1",duration=1)]
[delay(time=2)]
[name="愤怒的萨卡兹"]拿着你的东西滚开，莱塔尼亚人！谁知道你这些东西是不是想要害我？
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_499_1#1$1",duration=1)]
[delay(time=1.5)]
[name="失落的巴别塔成员"]这些只是抑制剂，你们在战场上会用得上......
[charslot(slot="m",name="avg_npc_932_1#1$1")]
[name="愤怒的萨卡兹"]长官们都说了，外面正在围堵我们的军舰就是从莱塔尼亚来的！
[name="愤怒的萨卡兹"]准是你们这些外人把他们引过来的！
[dialog]
[charslot]
[charslot(slot = "left", name = "avg_npc_932_1#1$1")]
[charslot(slot = "right", name = "avg_npc_499_1#1$1",duration = 0.5)]
[charslot(slot = "right",posfrom = "50,0", posto = "-30,0",duration = 1)]
[delay(time=1.2)]
[charslot(slot = "r", focus="r")]
[name="失落的巴别塔成员"]唉，我......我没法解释。我知道你准备带上你的孩子一起出城迎战，这些药他也用得——
[dialog]
[PlaySound(key="$bodyfalldown2")] 
[charslot(slot = "left",posfrom = "0,0", posto = "50,0",duration = 0.3)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "right",posfrom = "-30,0", posto = "100,0",duration = 0.4)]
[delay(time=0.31)]
[charslot(slot = "left",posfrom = "50,0", posto = "-50,0",duration = 0.5)]
[delay(time=0.51)]
[charslot(slot = "left", focus="l")]
[name="愤怒的萨卡兹"]别想碰我的孩子！
[dialog]
[PlaySound(key="$rungeneral")] 
[charslot(slot="m",name="avg_npc_1305_1#7$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1305_1#4$1",focus="m")]
[name="好运"]我听到这边有骚动——你疯了？她是巴别塔的医生！
[dialog]
[PlaySound(key="$bodyfalldown3")] 
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m",posfrom = 

... (全文16179字符)
```

### level_act33side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_laccolith",screenadapt="coverall")]
[PlayMusic(intro="$epic_intro", key="$epic_loop", volume=0.6)]
[playsound(key="$d_avg_snowstormflp", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.4, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1296_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",focus="r")]
[name="特雷西斯"]我们站在这艘军舰的辙印旁竟显得如此渺小。
[charslot(slot = "left", name = "avg_npc_1296_1#1$1",focus="l")]
[name="特蕾西娅"]是啊，令人惊叹的军事器械。
[name="特蕾西娅"]食腐者的血肉防线付出极大代价才阻截了战舰的行进，女妖足以撕碎意识的尖啸也仅仅是逼迫他们舍弃舰桥，撤往下层的指挥中心......
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",focus="r")]
[name="特雷西斯"]如果不是天灾在前，加之这块峡谷地带的险要地势——
[charslot(slot = "left", name = "avg_npc_1296_1#3$1",focus="l")]
[name="特蕾西娅"]我们的时间真的不多了。
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",focus="r")]
[name="特雷西斯"]卡兹戴尔必须拥有同样的，甚至超越他们想象的武器。
[charslot(slot = "right", name = "avg_npc_1297_1#2$1",focus="r")]
[name="特雷西斯"]我们迄今为止的尝试都失败了......
[charslot(slot = "left", name = "avg_npc_1296_1#1$1",focus="l")]
[name="特蕾西娅"]百多年前，谁又相信我们能够将卡兹戴尔真的建成移动城市呢？循规蹈矩无法让卡兹戴尔追上那些国家的步伐。
[name="特蕾西娅"]变形者刚传回了消息，地平线上与我们遥遥相望的军舰都已经开始减速了。
[charslot(slot = "right", name = "avg_npc_1297_1#7$1",focus="r")]
[name="特雷西斯"]他们放弃了？
[charslot(slot = "left", name = "avg_npc_1296_1#1$1",focus="l")]
[name="特蕾西娅"]不。选帝侯发出的指令是继续追击，但是舰队的指挥下达了减速的指令。
[name="特蕾西娅"]他们在害怕天灾和恶劣的地形，我们眼前这艘军舰就是前车之鉴。
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",focus="r")]
[name="特雷西斯"]那按照他们的前进速度，傍晚就是决战的时候了。
[charslot(slot = "left", name = "avg_npc_1296_1#1$1",focus="l")]
[name="特蕾西娅"]......足够了，我们已经拖延了充足的时间。
[charslot(slot = "m", focus = "n")]
特蕾西娅回望荒野上两股逐渐纠缠的风暴，试图找寻那座庞大城市的踪迹。
一无所获。卡兹戴尔如今已经到了哪里？它是否仍然在风暴中迁徙？躲藏在庇护所中的居民是否依旧安好？
[dialog]
[charslot(slot = "right", name = "avg_npc_1297_1#3$1",focus="r")]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1296_1#4$1",focus="l")]
[name="特蕾西娅"]那两股风暴开始聚拢了，我们的后路已经被彻底堵上了。决战不可避免，无论如何......特雷西斯？
[charslot(slot = "right", name = "avg_npc_1297_1#3$1",focus="r")]
[name="特雷西斯"]......
[charslot(slot = "left", name = "avg_npc_1296_1#1$1",focus="l")]
[name="特蕾西娅"]你竟然会在战场上走神。
[charslot(slot = "right", name = "avg_npc_1297_1#3$1",focus="r")]
[name="特雷西斯"]......那是什么？
[charslot(slot = "left", name = "avg_npc_1296_1#10$1",focus="l")]
[name="特蕾西娅"]......？
[name="特蕾西娅"]那是......
[Dialog]
[stopmusic(fadetime=2)]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[image(image="49_i03_2",screenadapt="coverall")]
[ImageTween( xScaleFrom=1, yScaleFrom=1, xScaleTo=1.1, yScaleTo=1.1, duration=50)]
[PlayMusic(intro="$chenandwei_intro", key="$chenandwei_loop", volume=0.6)]
[playsound(key="$d_avg_sandstorm", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.3, channel="bgs",fadetime=20)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
风暴在发怒，年幼者正张扬着挑衅年长者。
新生的风暴裹挟着雷鸣撞向了奄奄一息的风暴。
紊乱的空气流在两股风暴之间交错，融合......
狂暴孕育平静。一条狭长的通路诞生于风暴交汇之处。
电光闪耀，雷鸣回荡。
[name="特雷西斯"]一条路，在风暴之中。
[name="特蕾西娅"]风暴......
[name="特雷西斯"]特蕾西娅，走吧，道路已被风暴铸下。
[name="特雷西斯"]活下来的人还有另一条路可以选。
[name="特蕾西娅"]我们一起。
他们的命令在下一刻便由变形者集群传到每一位在场萨卡兹的耳中。
战士们看到了两位领袖并肩走入风暴。无人迟疑，所有人动了起来。
健全者搀扶虚弱者，勇敢者鼓励畏怯者。漫漫长队迈入了风暴。
[name="特蕾西娅"]......特雷西斯，你看到了吗？
风暴的呼啸中，那道源自幼时梦中风雪的声音仿佛传入了他们的耳中。
他们看到了——
[SoundVolume(volume=0.2, channel="bgs",fadetime=3)]
[image(image="49_i03_1",screenadapt="coverall",fadetime=3,xScale=1.1, yScale=1.1)]
[ImageTween( xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1.2, yScaleTo=1.2, duration=20)]
[name="特蕾西娅"]......预言。
裹在披风下的瘦弱身影听到了身后的声音，转身回望，看到了迎风而行的队伍。
特雷西斯看到了一个孩子。薄暮般的烟雾拥着她的肩头，在风暴中升腾，流淌，向着高空狂啸。
特雷西斯摘下手甲，赤手没入烟中。
烟雾散去，他被血丝染红的手握住了孩子的石刃。
[name="？？？"]（含糊不清的发音）你......啊......抓！抓到！
[name="特雷西斯"]你为什么在这？
[name="？？？"]（含糊不清的发音）家。你......家！家！
[name="？？？"]（含糊不清的发音）你！闯进！家！
孩子用力从特雷西斯手中抽出石刃，随后又指向他，向他身后漫长的队伍宣战。
生于荒野，无惧荒野，孩子的刀下，人与野兽无异。
[name="特雷西斯"]你想杀我？
[name="？？？"]（含糊不清的发音）煞，撒......杀，你！
[name="特蕾西娅"]没有人教过她怎么说话。她只是模仿着过路人的声音而已。
[name="特蕾西娅"]......特雷西斯？
特雷西斯俯瞰着瘦削的生命，他沉默着。
[name="特雷西斯"]刀，该这么拿。
[name="？？？"]......
[name="？？？"]（含糊不清的发音）你！
孩子看着特雷西斯伸出的手，犹豫片刻后便将钝刃放在了他的手上。
[name="？？？"]（含糊不清的发音）......我。你！带，我......带上，我！
特雷西斯看到了特蕾西娅的眼神。
预言。
“弑君之刀剑，诛王之枪矛。”
可他们从未在乎过预言。
[name="特雷西斯"]好。
[name="特雷西斯"]跟我们走。萨卡兹的家不在荒野。
[StopSound(channel="bgs", fadetime=2)]
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[image]
[Background(image="49_g3_kazdelstreet_n",screenadapt="coverall")]
“你有名字吗？”
“名字？‘我’。”
“那从现在起，你有新的名字了。”
“阿斯卡纶。”
[dialog]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[Delay(time=1)]
十天后
卡兹戴尔地区，卡兹戴尔移动城市
[dialog]
[playsound(key="$d_avg_churchfire", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.5, channel="bgs",fadetime=1)]
[Delay(time=1)]
[StopSound(channel="bgs", fadetime=5)]
[charslot(slot="l",name="avg_npc_934_1#1$1",duration=1)]
[delay(time=1.5)]
[name="激动的萨卡兹"]医生，快看！熔炉重燃了！
[charslot(slot = "m", focus = "n")]
[dialog]
[PlaySound(key="$smallearthquake")]
[CameraShake(duration=2.5, xstrength=6,ystrength=3, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
[charslot(slot="l",focus="l")]
[name="激动的萨卡兹"]动了？是城市终于开始动了？嘶......
[dialog]
[charslot(slot="r",name="avg_npc_499_1#1$1",duration=0.5)]
[delay(time=1)]
[charslot(slot="r",focus="r")]
[name="巴别塔医生"]小心点！我才刚刚给你包扎好了伤口......
[charslot(slot="l",focus="l")]
[name="激动的萨卡兹"]医生，我得赶去熔炉那里。熔炉重燃，卡兹戴尔还在航行......
[name="激动的萨卡兹"]那些莱塔尼亚人没能杀死我们！
[charslot(slot="r",focus="r")]
[name="巴别塔医生"]......
[charslot(slot="l",focus="l")]
[name="激动的萨卡兹"]呃，我，我不是说你，医生。
[name="激动的萨卡兹"]和我一起出去看看吧，你应该和那些活下来的战士享受同样的荣誉。
[charslot(slot="r",focus="r")]
[name="巴别塔医生"]我......不是萨卡兹。
[charslot(slot="l",

... (全文22685字符)
```

### level_act33side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="49_g1_kazdelroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[interlude(maskid = "ui_cutin_mask_horizon", style = 1, size = "1280, 100",offset = "0,0", channel = 2)]
[interlude(channel = 2, type = 2, name = "bg_black", afrom = 0, ato = 1, aduration = 0.3,sfrom = "1.3,1.3", sto = "1.3,1.3", sduration = 0, block = false)]
[Sticker(id="st1",  text="八年前", duration=1,x=300,y=325, alignment="center", size=24, delay=0, width=700,block="false")]
[Sticker(id="st2", text="1086年夏" ,duration=1,x=300,y=365, alignment="center",size=24, delay=0, width=700)]
[Sticker(id="st1", duration=1)]
[Sticker(id="st2", duration=1)]
[interlude(channel = 2, clear = true)]
[Delay(time=1.5)]
卡兹戴尔地区，卡兹戴尔移动城市民居
[dialog]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Subtitle(text="同学们，上课前的约定还记得吗？很好，不要大声回答问题，也不要向别人提起我们的学习。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这几个月中，雷·坦卡老师一直为你们讲述我们的历史。而我一直在苦恼，我最后的这节课里，应当教会你们什么知识。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="数学？语言？如何种植庄稼？还是如何锻造武器？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但我发现了一个事实，无论我教给你们什么，都无法真正改变我们的生活。我们已经默默生活在绝望里太久。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="十八年前的那场战争从未结束，莱塔尼亚的舰队如同幽灵一般追逐着亲历过那次战争的人。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="许多人在对战争的恐惧中绝望死去，在对身上越长越多的黑色石头的恐惧中绝望死去。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但本能总能驱使我们寻找战胜绝望的办法。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="49_g8_scarmarketcamp",screenadapt="coverall")]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Subtitle(text="有人选择向绝望宣战，向曾经施加给我们苦难的外族宣战，却总会被无法战胜的现实击败——", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1305_1#1$1",duration=1.5)]
[delay(time=2.5)]
[name="好运"]......我来看看委托。
[charslot(slot="m",name="avg_npc_1294_1#1$1")]
[name="“疤眼”"]在我见过的那么多雇佣兵里，你也算是最贪得无厌的，好运。你是打算攒钱去哥伦比亚买座庄园吗？
[name="“疤眼”"]活着已经不错了，好运。呵，从活得长这个角度看，你也确实配得上“好运”这名字。
[charslot(slot="m",name="avg_npc_1305_1#1$1")]
[name="好运"]我听说有一批大单子，有高价的吗？
[charslot(slot="m",name="avg_npc_1294_1#1$1")]
[name="“疤眼”"]最近风头很紧，城里有人一直盯着，前几个接的人下场都不太好。
[name="“疤眼”"]......是牵扯巴别塔的事情，你确定想接？
[charslot(slot="m",name="avg_npc_1305_1#3$1")]
[name="好运"]接，我运气一向很好。
[charslot(slot="m",name="avg_npc_1294_1#1$1")]
[name="“疤眼”"]那好，最近城里有个教书的，每天都在替巴别塔那帮外族人讲话，有人花钱买他的命。
[charslot(slot="m",name="avg_npc_1305_1#1$1")]
[name="好运"]......好。
[playsound(key="$d_gen_walk_n")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="49_g3_kazdelstreet_n",screenadapt="coverall")]
[name="“疤眼”"]我很期待你还能给我带来什么惊喜。
[name="“疤眼”"]祝你的好运今天别到头，老兄。
[dialog]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
卡兹戴尔地区，卡兹戴尔移动城市
[dialog]
[Delay(time=1)]
好运很久都没有回到过这里。
城里变了很多，许多人来了又走，“巴别塔”“军事委员会”这些字眼他并不陌生，总有人为一些他完全不明白的问题闹得不可开交。
他不懂，大家都是萨卡兹，到底有什么好争的。
他拿出照片，检查了一下目标的长相，看上去是个有些秀气的年轻人，身上三角形的标志十分眼熟。
一个老师。替巴别塔的外族人说话。煽动对军事委员会的反抗。
真不走运，今天你的生命就要到头了。
[dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1305_1#1$1",duration=1)]
[delay(time=2)]
[name="好运"]看行踪，应该是在这附近。
[dialog]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1305_1#6$1")]
[name="好运"]等等，为什么是这儿......
[charslot(slot = "m", focus = "n")]
即使很久都没回来过，他也清楚记得，这是他的家。
也是奥达的家。
[charslot(slot="m",name="avg_npc_1305_1#8$1")]
[name="好运"]奥达，你不该参与进来......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="49_g1_kazdelroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="被无法抗衡的力量一次又一次击败后，我们学会了默默习惯绝望。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可我们得说服自己，绝望并非由我们自身造成，我们需要在目所能及的生活中为绝望找到一个根源。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="于是如今这个时代，罪恶的根源呼之欲出——巴别塔。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="是巴别塔引来了外敌。是巴别塔的药物加速了我们矿石病的恶化。是巴别塔的教育磨灭了反抗的意志......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="是巴别塔蛊惑了魔王，试图欺骗我们放弃向外族收取血债。巴别塔就是我们绝望的根源。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我看到你们有人在点头，想必你们的父母也是这样告诉你们的吧？危言耸听的话语往往总是会被深陷于绝望中的人奉为真理。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但事实真是如此吗？外族人从未靠近卡兹戴尔的时候，我们的生活就好过吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="不要被任何说法欺骗，去思考，去见证，去得出自己的答案。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="是的，离开卡兹戴尔，很困难。外面的大地充满危险，我们甚至很难安全地到达下一条国境线。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可我依然会离开这里，去莱塔尼亚，去哥伦比亚，去卡西米尔，去任何能找到改变现状的办法的地方......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="然后我会回来，把办法教给你们，教给所有的萨卡兹孩子。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="至于你们问巴别塔最后会如何？巴别塔的未来会——", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[playsound(key="$doorknockquite")]
[Delay(time=2)]
[charslot(slot="m",name="avg_4131_odda_1#2$1",duration=1)]
[delay(time=1.5)]
[name="奥达"]——！
[name="奥达"]躲好，不要出声。
[dialog]
[charslot(slot = "m", 

... (全文23902字符)
```

### level_act33side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="49_g2_kazdelstreet_d",screenadapt="coverall")]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
卡兹戴尔地区，卡兹戴尔移动城市
[dialog]
[charslot(slot="m",name="avg_4131_odda_1#2$1",duration=0.5)]
[Delay(time=1)]
[name="奥达"]让我过去！
[dialog]
[charslot]
[charslot(slot = "left", name = "avg_npc_419_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_419_1#1$1",duration = 1)]
[delay(time=1.5)]
[name="萨卡兹王庭军"]前面已经封锁了，不能通行。
[charslot]
[charslot(slot="m",name="avg_4131_odda_1#2$1")]
[name="奥达"]那边发生什么事了？
[charslot]
[charslot(slot = "left", name = "avg_npc_419_1#1$1")]
[charslot(slot = "right", name = "avg_npc_419_1#1$1")]
[name="萨卡兹王庭军"]你是巴别塔的人？
[charslot]
[charslot(slot="m",name="avg_4131_odda_1#4$1")]
[name="奥达"]......我，我不是。
[charslot]
[charslot(slot = "left", name = "avg_npc_419_1#1$1")]
[charslot(slot = "right", name = "avg_npc_419_1#1$1")]
[name="萨卡兹王庭军"]那就与你无关。
[charslot]
奥达被挡在王庭军的人墙之外。
但在慌乱散开的人群中，他看到了几张熟悉的，正在哭泣的面孔。
[charslot(slot="m",name="avg_4131_odda_1#8$1")]
[name="奥达"]是那些学生......？这些房子......从小巷里绕一下，我应该能过去！
[Dialog]
[playsound(key="$rungeneral")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.4, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4131_odda_1#2$1")]
[name="奥达"]可以告诉我那边到底发生什么事了吗？
[dialog]
[charslot]
[charslot(slot = "left", name = "avg_npc_932_1#1$1",duration = 1,bstart=0.15,bend=0.5,posfrom = "50,0", posto = "50,0")]
[charslot(slot = "right", name = "avg_npc_934_1#1$1",duration = 1,bstart=0.15,bend=0.5,posfrom = "-50,0", posto = "-50,0")]
[delay(time=2)]
[charslot(slot = "left", focus="l")]
[name="冷漠的平民"]有人当街弄死了人，动手的人也死了。你要去凑热闹？
[charslot(slot = "r", focus="r")]
[name="激愤的平民"]又是巴别塔，也不知道殿下到底打算做什么......
[charslot(slot = "left", focus="l")]
[name="冷漠的平民"]......住嘴，尊重殿下！你吃的穿的住的不都是殿下为你带来的？！
[dialog]
[charslot]
[charslot(slot = "left", name = "avg_npc_933_1#1$1",bstart=0.15,bend=0.5,duration = 1)]
[delay(time=1.3)]
[name="谨慎的平民"]嘘......
[charslot]
[charslot(slot="m",name="avg_4131_odda_1#2$1")]
[name="奥达"]......
[charslot]
[charslot(slot = "right", name = "avg_npc_934_1#1$1",posfrom = "-50,0", posto = "-50,0",bstart=0.15,bend=0.5)]
[name="激愤的平民"]事情很简单——一个老师动手把自己学生的父亲给打死了！
[charslot]
[charslot(slot="m",name="avg_4131_odda_1#7$1")]
[name="奥达"]老师？怎么会......
[charslot]
[charslot(slot = "right", name = "avg_npc_934_1#1$1",posfrom = "-50,0", posto = "-50,0",bstart=0.15,bend=0.5)]
[name="激愤的平民"]那孩子的父亲不过骂了他两句！是那个老师自己说了些教坏小孩的话！
[charslot]
[charslot(slot="m",name="avg_4131_odda_1#8$1")]
[name="奥达"]不是这样的......
[dialog]
[charslot]
[charslot(slot = "left", name = "avg_npc_935_1#1$1",duration = 0.5,bstart=0.15,bend=0.5)]
[delay(time=0.7)]
[name="讥讽的平民"]你也帮巴别塔说话？这样的年轻人他们都......
[charslot]
[charslot(slot="m",name="avg_4131_odda_1#9$1")]
[name="奥达"]......
[charslot]
[charslot(slot = "left", name = "avg_npc_935_1#1$1",bstart=0.15,bend=0.5)]
[name="讥讽的平民"]欸，你过去干什么？
[charslot]
奥达挤过了街道上的人群，他看到一些熟悉的面孔已经倒在地上。
当他好不容易来到混乱的源头时，他终于在扬起的尘埃中找到了那位“老师”。
[stopmusic(fadetime=2)]
[dialog]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_4131_odda_1#2$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_4131_odda_1#7$1")]
[name="奥达"]老师！到底是怎么回事？
[dialog]
[PlayMusic(intro="$dignified_intro", key="$dignified_loop", volume=0.6)]
[charslot(slot = "m", focus = "n")]
[name="“老师”"]我......真的没想......伤害......他爸爸......
[charslot(slot="m",name="avg_4131_odda_1#9$1")]
[name="奥达"]我带你去找医生！
[charslot(slot = "m", focus = "n")]
[name="“老师”"]不......那边......救他......
垂死的人指向了他一直望着的方向，奥达看到了一位受伤的孩子，守候在毫无动静的父亲身旁哭泣。
[charslot(slot="m",name="avg_4131_odda_1#9$1")]
[name="奥达"]......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="49_g2_kazdelstreet_d",screenadapt="coverall")]
奥达抱着受伤的孩子，穿越火光四起的街道时，终于从人群中拼凑出了一个真相。
一位激动的老师误杀了一位激动的父亲，随后被愤怒的人群包围，倒在了街道的尘埃里。
平民，巴别塔，佣兵，或许还有军事委员会，越来越多的人被卷入其中。
那里扬起的尘埃，从城市的一角，扩散到了城市的另一角......
直到巴别塔办事处的外墙被来源未知的炮火轰碎，王庭军才终于镇压下了这场引起轩然大波的混乱。
从一场意外开始，到一枚炮弹结束。巴别塔遭遇了自十八年前那场战争后，最大的损失。
[dialog]
[Delay(time=2)]
[playsound(key="$d_avg_riot", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.4, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[dialog]
[charslot(slot="m",name="avg_4131_odda_1#5$1",duration=0.5)]
[Delay(time=0.6)]
[name="奥达"]不要逼我动手，这个孩子已经受伤了，需要医生。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_053",duration=1)]
[Delay(time=1.5)]
[name="沉默的佣兵"]你是哪边的？巴别塔？军事委员会？
[charslot(slot="m",name="avg_4131_odda_1#8$1")]
[name="奥达"]都不是，我只是想带他去找医生，请让开！
[charslot(slot = "m", focus = "n")]
[name="虚弱的孩子"]我爸爸......
[charslot(slot="m",name="avg_4131_odda_1#9$1")]
[name="奥达"]来不及了......对不起。
[charslot(slot="m",name="avg_npc_053")]
[name="沉默的佣兵"]......
[name="沉默的佣兵"]走吧。但不要轻信外人......萨卡兹，现在局势很混乱。
[charslot(slot="m",name="avg_4131_odda_1#9$1")]
[name="奥达"]谢谢......
[charslot]
[StopSound(channel="bgs", fadetime=2)]
奥达沉默地抱着孩子向前走去，孩子的呼吸逐渐衰微。
穿过街道时，奥达好像感觉到有人与他擦肩而过，但他却什么也没看到。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_npc_1304_1#1$1",afrom=0.5,ato=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[charslot(duration=1)]
[delay(time=1.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4131_odda_1#4$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="奥达"]......错觉吗？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, ra

... (全文20383字符)
```

### level_act33side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[gridbg(imagegroup="38_g21_skystarry_L1/38_g21_skystarry_r1/38_g21_skystarry_L2/38_g21_skystarry_r2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720",x=-360)]
[largebgtween(duration = 60,yFrom = 0, yTo = 100,block = false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[Delay(time=2)]
[playsound(key="$d_avg_penrustle")]
凯尔希：
我收到了你的来信，希望你在巴别塔一切都好。
有件事我想告诉你，两个月前，我从失事的车队中救下了一个女孩，叫做阿米娅。
很遗憾，她的父母在事故中丧生，她自己也染上矿石病。
我本想安置好她再继续前行，但在当地，人们会将没有家庭照顾的矿石病患者关进载具，送到无人的荒野，所以只能将她带在身边。
机缘巧合之下，她成为我的同行者。
你根本想象不到我在照顾她时的慌乱与无措......
万幸，有位自称暴行的女士也加入了我们的旅程，有她帮忙照顾，我确实松了一口气。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[gridbg]
[Delay(time=1)]
[Background(image="46_g5_rmbtwild_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
月光下，一道黑影从“沙丘”中钻出。
[dialog]
[PlaySound(key="$d_avg_pawfootstep_1")] 
[charslot(slot = "m", name = "avg_npc_1190_1#1$1",posfrom = "-100,0", posto = "0,0",duration = 1.5,bstart=0.6,bend=0.9)]
[Delay(time=2)]
[name="？？？"]（警惕地靠近）
[name="？？？"]（威胁地嘶叫）
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1295_1#1$1",duration=1.5,bstart=0.4,bend=0.7)]
[delay(time=2)]
[charslot(slot = "m", action="jump",posto = "0,0",power=30,times=1,duration = 0.4)]
[delay(time=0.6)]
[name="？？？"]嘿！快走开！
[name="？？？"]不许靠近我们！
[dialog]
[charslot]
[PlaySound(key="$d_avg_pawfootstep_3")] 
[charslot(slot = "m", name = "avg_npc_1190_1#1$1",posfrom = "0,0", posto = "100,0",duration = 1.5)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1188_1#1$1",posfrom = "-100,0", posto = "0,0",duration = 1.5)]
[delay(time=2)]
[charslot(slot = "m", focus = "m")]
[name="巨大的沙地兽"]（激动地磨爪）
[charslot(slot = "l",name = "avg_npc_1188_1#7$1", focus = "l")]
[name="幼小的沙地兽"]（疑惑地探头）
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1360_1#1$1")]
[name="博士"]它们好像因为你的恐吓变得更兴奋了，阿米娅。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1295_1#5$1",duration=1.5)]
[delay(time=2)]
[name="阿米娅"]博士不用害怕，我能对付它们！
[name="阿米娅"]爸爸妈妈教过我该怎么赶走沙地兽，只要模仿它们死对头的叫声就好了。
[charslot(slot="m",name="avg_npc_1295_1#6$1")]
[name="阿米娅"]啾啾......
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1190_1#1$1",posfrom = "100,0", posto = "100,0",focus = "m")]
[charslot(slot = "l", name = "avg_npc_1188_1#1$1",posfrom = "0,0", posto = "0,0",focus = "m")]
[name="巨大的沙地兽"]（困惑地停下）
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1295_1#10$1")]
[name="阿米娅"]不、不对，好像不是这样的。难道是咻咻......？
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1190_1#1$1",posfrom = "100,0", posto = "100,0",focus = "l")]
[charslot(slot = "l", name = "avg_npc_1188_1#7$1",posfrom = "0,0", posto = "0,0",focus = "l")]
[name="幼小的沙地兽"]（疑惑地歪头）
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1295_1#10$1")]
[name="阿米娅"]还是不对，呜，到底是什么？
[charslot(slot="m",name="avg_npc_1295_1#7$1")]
[name="阿米娅"]嗷呜？咕咕？咯咯......？
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1190_1#1$1",posfrom = "100,0", posto = "100,0",focus = "m")]
[charslot(slot = "l", name = "avg_npc_1188_1#1$1",posfrom = "0,0", posto = "0,0",focus = "m")]
[name="巨大的沙地兽"]（不解地甩尾）
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1295_1#7$1")]
[name="阿米娅"]呜......看来都不对......
[charslot(slot = "m", name = "avg_npc_1360_1#1$1")]
[name="博士"]没关系的，阿米娅，让我来吧。
[charslot(slot = "m", focus = "n")]
随即，博士食指与拇指捏成环，吹出了一种奇怪而悠长的呼哨。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1190_1#1$1",posfrom = "100,0", posto = "100,0",focus = "m")]
[charslot(slot = "l", name = "avg_npc_1188_1#1$1",posfrom = "0,0", posto = "0,0",focus = "m")]
[charslot(slot = "m", action="jump",posto = "0,0",power=30,times=1,duration = 0.3)]
[name="巨大的沙地兽"]（惊恐地站立）
[charslot(slot = "l", name = "avg_npc_1188_1#5$1",focus = "l")]
[name="幼小的沙地兽"]（不安地张望）
[playsound(key="$d_avg_sandanimaldig")]
[charslot(slot = "m", name = "avg_npc_1190_1#1$1",posfrom = "100,0", posto = "100,0",focus = "m")]
[charslot(slot ="m", action="shake", power=10, times=100, duration=0.5)]
[charslot(slot = "m", focus = "m")]
[name="巨大的沙地兽"]（迅速地刨洞）
[playsound(key="$d_avg_sandanimaldig")]
[charslot(slot = "l", name = "avg_npc_1188_1#5$1",focus = "l")]
[charslot(slot ="l", action="shake", power=5, times=10, duration=0.5)]
[charslot(slot = "m", focus = "l")]
[name="幼小的沙地兽"]（缓缓地跟上）
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1295_1#1$1")]
[name="阿米娅"]博士，好厉害！和真的一模一样！
[name="阿米娅"]我也来！
[dialog]
[charslot(duration=0.5)]
[delay(time=1)]
[playsound(key="$d_avg_unskilledwhistle")]
阿米娅将小手捏成一团按在嘴边，因为力道过大，憋红脸蛋才吹出一声生硬的呼哨。
[playsound(key="$d_avg_pawfootstep_1")]
空旷的荒野上呼哨声相映成趣。很快，沙地兽就伏低身子，夹着尾巴钻进地下跑走了。
呼哨声渐弱，变成了孩童稚嫩的笑声。
然后笑声渐息，安静片刻后，又响起一声小小的叹息。
[charslot(slot = "l", name = "avg_npc_1360_1#1$1")]
[name="博士"]阿米娅，过来。
[name="博士"]沙地兽已经逃走了，你怎么还把脸蛋皱成一团？
[dialog]
[charslot(slot = "r", name = "avg_npc_1295_1#7$1",posfrom = "70,0", posto = "0,0",duration = 1)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1295_1#7$1",focus="r")]
[name="阿米娅"]......爸爸妈妈教了我那么多次，我都没有记住......我还说要保护博士，也没有做到......
[name="阿米娅"]博士的手还受着伤......到现在也没好。
[charslot(slot = "l", focus="l")]
[name="博士"]没事的阿米娅，我的手已经不疼了。更何况，你不记得了吗？
[name="博士"]刚才模仿的声音，还是你教给我的呢。
[charslot(slot = "r", name = "avg_npc_1295_1#1$1",focus="r")]
[name="阿米娅"]咦，我那么做过吗？
[charslot(slot = "l", focus="l")]
[name="博士"]看吧，我和你讲过，总是不睡觉，脑瓜就会变慢，最后忘掉很多东西。
[charslot(slot = "r", name = "avg_npc_1295_1#7$1",focus="r")]
[name="阿米娅"]我，我......不想睡。
[name="阿米娅"]......我害怕，怕睡着了会梦见当时的事情。
[charslot(slot = "l", focus="l")]
[name="博士"]可你也和我说过，有时候会梦见爸爸妈妈。
[charslot(slot = "r", name = "avg_npc_1295_1#7$1",focus="r")]
[name="阿米娅"]唔......
[charslot(slot = "l", focus="l")]
[name="博士"]阿米娅，距离载具到来还有一段时间，睡一会儿吧。
[charslot(slot = "r", name = "avg_npc_1295_1#2$1",focus="r")]
[name="阿米娅"]嗯......
[name="阿米娅"]博士，我能靠近一点吗......
[charslot(slot = "r", name = "avg_npc_1295_1#8$1",focus="r")]
[name="阿米娅"]等我醒了....

... (全文24667字符)
```

### level_act33side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_corridor_2",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
1091年秋
卡兹戴尔地区，巴别塔罗德岛本舰
[dialog]
[charslot(slot = "left", name = "avg_003_kalts_1#1$1",duration = 1)]
[delay(time=1.5)]
[name="凯尔希"]可露希尔，进度如何？
[name="凯尔希"]我不希望这次还会出现本舰核心系统失控的问题。
[dialog]
[charslot(slot = "right", name = "avg_npc_050",duration = 1)]
[delay(time=1.2)]
[charslot(slot = "right", focus="r")]
[name="可露希尔"]唔......哈哈，你非要说呢，那可能还是遇到了一些小小的问题来着。
[name="可露希尔"]就算拿着你给我的锦囊妙计，PRTS的很多程序加密模式也不是常人能理解的啊。我的解码仪器还不能完全适配。
[name="可露希尔"]就结果而言，可能来不及在博士登舰前完全关闭系统。
[charslot(slot = "left", name = "avg_003_kalts_1#5$1",focus="l")]
[name="凯尔希"]再尝试一次。
[name="凯尔希"]如果还是没有把握，就准备应急方案......完全切断本舰的所有能源。
[charslot(slot = "right", focus="r")]
[name="可露希尔"]放心交给我吧！
[name="可露希尔"]不过......看来你还藏了很多秘密呢，凯尔希。
[name="可露希尔"]我从来没有见过有人能让你如此紧张。
[charslot(slot = "left", name = "avg_003_kalts_1#1$1",focus="l")]
[name="凯尔希"]......这不重要，可露希尔。
[name="凯尔希"]重要的是，我不希望本舰出现任何意外。
[charslot(slot = "right", focus="r")]
[name="可露希尔"]唔，可按照阿斯卡纶传回的任务简报来看，博士只是一个普通人，还是一个会背着落难小兔子到处瞎逛的大善人。
[name="可露希尔"]我们好像没有必要这么防备他吧？
[charslot(slot = "left", name = "avg_003_kalts_1#1$1",focus="l")]
[name="凯尔希"]威胁并不来自博士。
[charslot(slot = "right", focus="r")]
[name="可露希尔"]那是啥？
[charslot(slot = "left", name = "avg_003_kalts_1#1$1",focus="l")]
[name="凯尔希"]你还不需要知道。
[name="凯尔希"]为了博士的安全，也为了巴别塔成员的安全，抹除他的登舰记录。
[name="凯尔希"]在博士和特蕾西娅得出结论前，不必让其他成员知道他的存在。
[charslot(slot = "right", focus="r")]
[name="可露希尔"]好好好，我再加把劲......
[name="可露希尔"]可是明明你一副很在意博士的样子，却又这么警惕那个人......
[name="可露希尔"]啊——难道博士抓住了你的什么把柄！
[charslot(slot = "left", name = "avg_003_kalts_1#5$1",focus="l")]
[name="凯尔希"]不要想着调查，你查不到。
[charslot(slot = "right", focus="r")]
[name="可露希尔"]呃。不用这么严肃吧。
[charslot(slot = "left", name = "avg_003_kalts_1#14$1",focus="l")]
[name="凯尔希"]还有......那个被救下的孩子，她的身份？
[charslot(slot = "right", focus="r")]
[name="可露希尔"]还是老结论。
[name="可露希尔"]我反复核对了当时与雷姆必拓有关的一切记录，还让Scout和军事委员会的内应做了确认。
[name="可露希尔"]阿米娅的身份没有问题。
[name="可露希尔"]她的父母的确是在为我们运送激光开采模块的车队里遇袭身亡，针对他们的袭击是绝对的意外。
[name="可露希尔"]没有人知道他们运送的是和萨卡兹有关的货物，而那场袭击也并非军事委员会的刻意安排。
[name="可露希尔"]而她应该也是在这场事故中才成了感染者。如果不是博士......她可能会在雷姆必拓凄惨地度过余生吧。
[charslot(slot = "left", name = "avg_003_kalts_1#1$1",focus="l")]
[name="凯尔希"]我会亲自负责那个孩子登舰后的检查和治疗方案。
[charslot(slot = "right", focus="r")]
[name="可露希尔"]你还是不放心那个孩子吗？
[charslot(slot = "left", name = "avg_003_kalts_1#1$1",focus="l")]
[name="凯尔希"]不放心。
[name="凯尔希"]她年纪太小，感染矿石病后没经过像样的治疗。
[charslot(slot = "right", focus="r")]
[name="可露希尔"]是这种“不放心”喔。
[charslot(slot = "left", name = "avg_003_kalts_1#4$1",focus="l")]
[name="凯尔希"]我不希望博士的善意变成拖延她治疗的罪魁祸首，而且......
[name="凯尔希"]......特蕾西娅会说，她是个善良的孩子，有权利选择未来。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[gridbg(imagegroup="38_g20_skyblue_L1/38_g20_skyblue_r1/38_g20_skyblue_L2/38_g20_skyblue_r2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720",x=-1200)]
[largebgtween(duration = 60,yFrom = 500, yTo = 720,block = false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="？？？"]阿米娅，阿米娅。
[name="阿米娅"]......好困......我......我在哪？
[name="阿米娅"]博士......博士？
[name="？？？"]博士就在这。
[name="？？？"]小懒虫，快醒醒，你快要到家了。
[name="阿米娅"]家？
迷迷糊糊地，阿米娅感受到温暖的指尖在脸颊旁移动。
[name="阿米娅"]好痒，哈哈，不要挠我的脖子。
[name="阿米娅"]呀！
[name="阿米娅"]你、你是谁？
[name="？？？"]特蕾西娅。我是特蕾西娅。
[name="阿米娅"]特蕾西娅......博士和我提起过你......
[name="特蕾西娅"]哦，博士怎么说我呢？
[name="阿米娅"]唔，忘记了......不过我当时在吃很好吃的胡萝卜蛋糕......
[name="阿米娅"]特蕾西娅应该是......香香的......甜甜的......热腾腾的。
[name="特蕾西娅"]那现在呢？特蕾西娅和你想象的样子一样吗？
[name="阿米娅"]嗯......也是香香的......甜甜的......热腾腾的，就是没有胡萝卜味......
[name="特蕾西娅"]呵呵，看来还没睡醒呢。
[name="特蕾西娅"]小阿米娅，要和我们一起回家吗？
[name="阿米娅"]家......嗯......好......
[dialog]
[bgeffect(name="$eb_dim_closeeye",layer=1)]
[Delay(time=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[bgeffect]
[gridbg]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
卡兹戴尔地区，巴别塔罗德岛本舰外
[dialog]
[charslot(slot = "left", name = "avg_npc_1360_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1296_1#8$1",duration = 1)]
[delay(time=2.5)]
[charslot(slot = "m", focus = "n")]
特蕾西娅的怀中，小小的卡特斯正环着她的脖子酣睡。
她轻轻拍拍阿米娅的后背，转头看向一旁显得有些疲惫的博士。
[charslot(slot = "left", focus="l")]
[name="博士"]谢谢你专程离舰来接我们......特蕾西娅。
[charslot(slot = "right", name = "avg_npc_1296_1#8$1",focus="r")]
[name="特蕾西娅"]看来你也不是无所不知的，博士。
[name="特蕾西娅"]至少在照顾小孩子这方面，你还有很多要学的东西。
[charslot(slot = "left", focus="l")]
[name="博士"]......当然。
[charslot(slot = "right", name = "avg_npc_1296_1#8$1",focus="r")]
[name="特蕾西娅"]你看上去和离开时很不一样了，博士。这趟旅程怎么样？
[charslot(slot = "left", focus="l")]
[name="博士"]我见到了很多，也学到了很多......在这片大地上所见到的都很有趣。
[name="博士"]以及，我遇见了阿米娅......在那场事故中救下她，简直算得上奇迹。
[charslot(slot = "right", name = "avg_npc_1296_1#8$1",focus="r")]
[name="特蕾西娅"]阿米娅。她的确比信中写的还要可爱。可怜的孩子，但也算幸运。
[charslot(slot = "left", focus="l")]
[name="博士"]她的病情不可避免地在变严重，我需要带她回来接受治疗。
[name="博士"]我离开的这段时间，巴别塔......
[charslot(slot = "right", name = "avg_npc_1296_1#3$1",focus="r")]
[name="特蕾西娅"]算不上顺利，我们遇到了许多问题，但并不急在这一时去解决。
[charslot(slot = "right", name = "avg_npc_1296_1#8$1",focus="r")]
[name="特蕾西娅"]经过那么漫长的旅途，你们一定很累了，请先休息一下吧。
[charslot(slot = "left", focus="l")]
[name="博士"]非常感谢，特蕾西娅。
[name="博士"]阿米娅，我们到家了。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1295_1#1$1",duration=1.5)]
[delay(time=2)]
[name="阿米娅"]唔......博士，你在叫我吗......我是不是睡着了？
[charslot]
[charslot(slot = "left", name = "avg_npc_1360_1#1$1",focus="r")]
[charslot(slot = "right", name = "avg_npc_1296_1#8$1",focus="r")]
[name="特蕾西娅"]呀，小阿米娅，你醒了。
[charslot(slot = "left", name = "avg_npc_1360_1#1$1",focus="l")]
[name="博士"]阿米娅，下来好不好？特蕾西娅一直抱着你会累的。
[charslot]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[CameraShake(duration=0.5, xstrength=5, ystrength=20, vibrato=5, randomness=90, fadeout=true, block=false)]
阿米娅乖巧地点点头，从特蕾西娅的怀中跃下，站在地上蹦了蹦。
[dialog]
[charslot(

... (全文18092字符)
```

### level_act33side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_victoria",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Subtitle(text="卡兹戴尔摄政王、军事委员会将领特雷西斯殿下：", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="远游的学者将他的见闻呈于公爵府邸，我们这才得知，在遥远的荒漠中，有一座新兴的移动城市正在崛起。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="古老的炉火盛燃不息，城市的围墙日渐高耸，曾经散漫的佣兵集结在同一面旗帜下。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你展现出了非同凡响的实力与威望，已足以让卡文迪许公爵驻足赞叹。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你以一己之力改变了我们对萨卡兹部族的认识，或许我们不应再囿于过去的成见，诚恳的开放交流对我们彼此都更有益处。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="卡文迪许公爵诚邀你来领地一叙。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你麾下英勇的战士，在这个古老的帝国中也会有用武之处。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="bg_corridor_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
1091年冬
[dialog]
[charslot(slot = "m", name = "avg_npc_048",duration = 1)]
[Delay(time=1.5)]
[name="博士"]再试一次......我必须要成功......
[name="博士"]如果连这点事都做不到，还谈什么，治愈矿石病......
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "0,-50",duration = 1)]
[Delay(time=1.5)]
[charslot(slot = "m",posfrom = "0,-50", posto = "0,-30",duration = 0.5)]
[charslot(slot ="m", action="shake", power=5, times=30, duration=0.5)]
[name="博士"]呃——
[dialog]
[charslot(slot = "m",posfrom = "0,-30", posto = "0,-50",duration = 0.3)]
[PlaySound(key="$bodyfalldown3")]
[CameraShake(duration=0.3, ystrength=30, vibrato=15, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[name="博士"]还是不行......呼......呼......
[dialog]
[charslot]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_1361_1#1$1",duration = 0.5)]
[Delay(time=0.8)]
[name="外勤战士"]您好，您还是把那个医疗箱放下吧，这些事交给我们就好。
[charslot(slot = "m", name = "avg_npc_048")]
[name="博士"]好......好吧......
[dialog]
[charslot(slot = "m", name = "avg_npc_1361_1#1$1")]
[Delay(time=0.5)]
[charslot(slot = "m",posfrom = "0,0", posto = "0,-50",duration = 0.5)]
[Delay(time=0.8)]
[PlaySound(key="$d_avg_clothmovement")]
[charslot(slot = "m",posfrom = "0,-50", posto = "0,0",duration = 0.8)]
[Delay(time=1)]
[name="外勤战士"]康复以后记得加强锻炼。
[dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[charslot(slot = "m",posfrom = "0,0", posto = "200,0",duration = 1,afrom=1,ato=0)]
[Delay(time=2.5)]
[charslot]
[charslot(slot = "m", name = "avg_003_kalts_1#11$1",duration = 1)]
[Delay(time=1.1)]
[name="凯尔希"]你暂时没办法通过“锻炼”赶上泰拉人的体能，博士。
[name="凯尔希"]比起体力劳动，有其他更能发挥你的长处的工作。
[charslot(slot = "m", name = "avg_npc_048")]
[name="博士"]我知道，只是偶尔不服输罢了......
[charslot(slot = "m", name = "avg_003_kalts_1#4$1")]
[name="凯尔希"]自那日之后，你就有些心神不宁。 
[charslot(slot = "m", name = "avg_npc_048")]
[name="博士"]我在想，呼......特蕾西娅。
[name="博士"]孤身一人前往敌对阵营掌控的城市，对于一个领导者来说恐怕不是理智的行为。
[name="博士"]与她同行的战士虽然强大，但不足以在军队面前保护她的安全。
[charslot(slot = "m", name = "avg_003_kalts_1#1$1")]
[name="凯尔希"]魔王在萨卡兹传统里的地位超乎想象，特蕾西娅的功绩也有目共睹。军事委员会反而不敢有过激的举动。
[charslot(slot = "m", name = "avg_003_kalts_1#5$1")]
[name="凯尔希"]但维多利亚对卡兹戴尔发出的邀请并不是一个友善的信号，这意味着卡兹戴尔再次进入了泰拉诸国的视野。
[name="凯尔希"]特蕾西娅需要出现在卡兹戴尔去表示她的态度，她决不同意卡兹戴尔再卷入一场战争。
[charslot(slot = "m", name = "avg_npc_048")]
[name="博士"]尽管了解了军事委员会与巴别塔成立的经过......
[name="博士"]以我的理解，已经面临诸多困境的萨卡兹，不该再在彼此之间形成对立。这是对他们手中为数不多的资源的消耗。
[charslot(slot = "m", name = "avg_003_kalts_1#1$1")]
[name="凯尔希"]萨卡兹有着复杂的历史，这造成了他们对外族人不同的态度。
[name="凯尔希"]特雷西斯与特蕾西娅就像两面旗帜，对于萨卡兹的人民来说，他们有权选择自己认为正确的道路。
[charslot(slot = "m", name = "avg_npc_048")]
[name="博士"]看上去在矿石病之外，我们还有很多麻烦。
[name="博士"]“了解”与“理解”之间还是有着不小的差异，我应该要继续学习泰拉的历史了。
[name="博士"]这一次，要靠你来指引我了。凯尔希。
[charslot(slot = "m", name = "avg_003_kalts_1#11$1")]
[name="凯尔希"]......当然。
[charslot(slot = "m", name = "avg_npc_048")]
[name="博士"]现在，我们只能尽量确保罗德岛上的矿石病患者，能有一个安稳的治疗环境——
[dialog]
[stopmusic(fadetime=1)]
[charslot]
[PlaySound(key="$d_sp_ballista",volume=0.5)] 
[CameraShake(duration=0.8, xstrength=35, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[CameraShake(duration=2, xstrength=10, ystrength=5, vibrato=50, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n",volume=0.5)] 
[delay(time=2)]
[playsound(key="$rungeneral", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.7, channel="bgs",fadetime=1)]
[charslot(slot = "m", name = "avg_npc_1361_1#1$1",duration=0.8,posfrom = "150,0", posto = "0,0")]
[delay(time=1)]
[StopSound(channel="bgs", fadetime=0.5)]
[name="外勤战士"]怎么回事——
[charslot(slot = "m", name = "avg_003_kalts_1#14$1")]
[name="凯尔希"]敌袭？这个时候？
[charslot(slot = "m", name = "avg_npc_048")]
[name="博士"]......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_419_1#1$1")]
[charslot(slot = "right", name = "avg_npc_419_1#1$1")]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot = "l", focus = "l")]
[name="冷酷的王庭军"]根据得到的情报，殿下已经启程。
[name="冷酷的王庭军"]诸位！我们敬重的只有殿下，只要摧毁巴别塔，殿下就会回到卡兹戴尔的怀抱。
[name="冷酷的王庭军"]我们可以承担背叛的罪名，但是在这关键的时刻，摄政王的事业不该受到阻挠，卡兹戴尔会夺回它失去的一切。
[name="冷酷的王庭军"]愿如殿下所说，萨卡兹可以团结在一起。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="49_g8_scarmarketcamp",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block

... (全文26822字符)
```

### level_act33side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_battlefield",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
1092年冬
卡兹戴尔地区，边境战区
[dialog]
[playMusic(intro="$m_bat_imprisonment_intro", key="$m_bat_imprisonment_loop", volume=0.6)]
[Delay(time=1)]
[playsound(key="$d_avg_animalrun",channel="1",volume=0.6,delay=1)]
[PlaySound(key="$smallearthquake")]
[CameraShake(duration=3,xstrength=5, ystrength=3, vibrato=50, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_419_1#1$1",duration=0.5)]
[delay(time=1)]
[name="受伤的士兵"]那些发疯的瘤兽......是在迁徙？该死，不光前哨部队被冲散了，那些没来得及躲开的人，都......
[name="受伤的士兵"]还有那些完全没有交流却行动一致的巴别塔士兵......之前的情报里可没提过这些！
[charslot]
[name="？？？"]这不是我们该操心的问题。
[dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1067_1#1$1",duration=1.5)]
[delay(time=2)]
[name="厄尔苏拉"]现在我的职级最高，通知活着的人马上归队收拢。这批物资很重要，没了这些，我们这个冬天不会好过。
[charslot(slot="m",name="avg_npc_419_1#1$1")]
[name="沉着的士兵"]......是，长官。我们明明提前了这次行动，但还是出了问题，是不是那边的内应——
[charslot(slot="m",name="avg_npc_1067_1#1$1")]
[name="厄尔苏拉"]内应的情报没问题。是负责协助运送物资的佣兵坐地起价耽误了时间，人我已经处理了。
[charslot(slot="m",name="avg_npc_1067_1#7$1")]
[name="厄尔苏拉"]所以我讨厌佣兵。
[charslot(slot="m",name="avg_npc_419_1#1$1")]
[name="受伤的士兵"]这么多巧合......
[charslot(slot="m",name="avg_npc_1067_1#1$1")]
[name="厄尔苏拉"]巧合每次都凑在一起就不是巧合了，这段时间我们莫名其妙吃的亏已经不少了。
[name="厄尔苏拉"]集中精神，巴别塔的人一定还在——
[charslot(slot="m",name="avg_npc_419_1#1$1")]
[name="受伤的士兵"]等等，救——
[dialog]
[playsound(key="$d_avg_animalrun",channel="1",volume=0.6)]
[playsound(key="$d_avg_arrow")]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.03, block=true)]
[charslot(slot="m",name="avg_npc_1311_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[charslot(duration=0.3)]
[delay(time=1)]
[CameraShake(duration=0.3,xstrength=5, ystrength=13, vibrato=10, randomness=90, fadeout=true, block=false)]
[playsound(key="$bodyfalldown1")]
一道白芒贯穿了士兵的头颅，在瘤兽急促的蹄声中，他们甚至找不到攻击的来源。
[dialog]
[charslot(slot="m",name="avg_npc_1067_1#5$1")]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="“这是第一次警告。留下物资离开，我们不会对你们动手。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
清冷嘶哑的声音在厄尔苏拉的脑海中响起，毫无预兆。
[charslot(slot="m",name="avg_npc_419_1#1$1")]
[name="沉着的士兵"]他......死了。*萨卡兹粗口*，我们得撤退，长官！你听到那个声音了吗？
[charslot(slot="m",name="avg_npc_1067_1#5$1")]
[name="厄尔苏拉"]哼......他们在虚张声势。跟紧我的位置隐蔽前进！
[charslot(slot="m",name="avg_npc_1067_1#6$1")]
[name="厄尔苏拉"]所有人不许脱队单独行动！想活着就跟着大部队一起行动！这批物资必须要送回！
[charslot(slot="m",name="avg_npc_1067_1#5$1")]
[name="厄尔苏拉"]至于前哨部队，他们只能自求多福了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot="m",name="avg_npc_1311_1#1$1",duration=1)]
[delay(time=1.5)]
[name="Scout"]他们开始撤退了，果然想要直接拿下这批物资还是有困难。
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="“不必冒进，按博士的安排执行即可。议长说过，最高优先级的任务是保证伤亡最小化。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="Scout"]我心中有数，Mantra女士。
[dialog]
[charslot]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1300_1#1$1",duration=1.5)]
[delay(time=2)]
[charslot(slot = "m", focus = "n")]
Mantra女士双唇紧闭，但Scout的脑海中却清晰地回荡着她说话的声音。
或许在巴别塔隐秘行动小队中，她是最完美的协调员。但Scout可以肯定，在敌人的心中，她会成为蚕食理智的阴影。
[charslot(slot="m",name="avg_npc_1300_1#1$1")]
[name="Mantra"]敌方前哨部队已经被兽群成功切割，逃进了那片树林。
[name="Mantra"]敌人的行动是临时起意，想必是意识到我们破解了他们的通讯暗号。但围剿计划还是成功了，滴水不漏。
[name="Mantra"]剩下的就交给阿斯卡纶了。
[charslot(slot="m",name="avg_npc_1311_1#1$1")]
[name="Scout"]阿斯卡纶不会失败。
[charslot(slot="m",name="avg_npc_1300_1#1$1")]
[name="Mantra"]我们也不会。
[charslot(slot="m",name="avg_npc_1311_1#1$1")]
[name="Scout"]哈哈，说的也是。休息会吧，Mantra女士，您“说话”的负担太重了。
[name="Scout"]之后的计划不用担心，我们有博士在。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_iceforest_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_npc_053",duration=1,posfrom = "0,-100", posto = "0,0")]
[charslot(slot ="m", action="shake", power=5, times=30, duration=0.5)]
[delay(time=1.5)]
[name="濒死的雇佣兵"]妈的，谁在指挥作战......又是恶灵？他究竟是哪个指挥官？哪个王庭的崽种？
[name="濒死的雇佣兵"]他能如此对我们，总有一天也能如此对你们！给这种人卖命有什么好处！
[name="濒死的雇佣兵"]我会活着走出这里——
[charslot(slot = "m", focus = "n")]
佣兵听到了不远处黑暗中的呼吸，手中的刀毫无犹豫地挥斩出去。
[charslot(slot="m",name="avg_npc_053")]
[name="濒死的雇佣兵"]我找到你了！
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "150,0",duration = 0.3)]
[playsound(key="$e_skill_skulsrsword", volume=0.6)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="r",name="avg_4131_odda_1#5$2",duration=0.4,posfrom = "100,0", posto = "240,0")]
[playsound(key="$d_avg_hammer",delay=0.1)]
[Delay(time=0.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[charslot(slot="m",name="avg_4131_odda_1#5$2")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4131_odda_1#9$2")]
[name="奥达"]嘶......
[charslot(slot="m",name="avg_npc_053")]
[name="濒死的雇佣兵"]呵，你也受了这么重的伤，你真有把握活着宰了我？
[name="濒死的雇佣兵"]滚开，否则我拼了命也要宰了你！
[charslot(slot="m",name="avg_4131_odda_1#5$2")]
[name="奥达"]你不能拿走马塞尔的遗物。他得回家。
[charslot(slot="m",name="avg_npc_053")]
[name="濒死的雇佣兵"]家？咳咳，咳——
[name="濒死的雇佣兵"]我们的家在......卡兹戴尔！你们——背叛了卡兹戴尔......
[charslot]
[playsound(key="$e_skill_skulsrsword", volume=0.6)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_metallicclick", delay=0.1)]
佣兵的刀不断向奥达挥去，但他只是竭力举起自己的大锤抵挡。
佣兵的动作越来越慢，气息也越来越弱。
[dialog]
[charslot(slot="m",name="avg_npc_053")]
[charslot(slot ="m", action="shake", power=5, times=30, duration=0.3)]
[delay(time=0.5)]
[name="濒死的雇佣兵"]巴别塔......都是傻......子......
[charslot(slot="m",name="

... (全文16875字符)
```

### level_act33side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$loading_intro", key="$loading_loop", volume=0.6)]
[Background(image="bg_iceforest_1",screenadapt="coverall")]
[bgeffect(name="$eb_lightsnow", layer=1)]
[PlaySound(key="$d_avg_snowstormflp", volume=0.5, loop=true, channel="snow")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_snowrun", volume=1, loop=true, channel="run")]
[StopSound(channel="run", fadetime=2)]
[charslot(slot = "m", name = "avg_npc_932_1#1$1", duration = 1, isblock = true)]
[name="萨卡兹平民"]前面！快看前面！
[name="萨卡兹平民"]桥梁......被炸毁了？我们要怎么过去？
[name="萨卡兹平民"]我们，我们还有别的路吗？走了这么久，天灾云还是在头顶上......
[name="萨卡兹平民"]队伍里还有伤员和孩子，我们，我们走不动了......
[dialog]
[curtain(direction = 6,fillfrom = 0,fillto = 1,fadetime=0.5)]
[delay(time=1)]
[curtain]
[charslot]
[Background(image="bg_snow_2",screenadapt="coverall")]
[charslot(slot = "m", name = "avg_npc_1308_1#1$1")]
[curtain(direction = 6,fillfrom = 1,fillto = 0,fadetime=0.5)]
[Delay(time=1)]
[name="巴别塔成员"]该死！森林和草地上到处都是源石晶簇，它们......它们已经开始发亮了。
[multiline(name="巴别塔成员")]在天灾爆发前，这些活性化的炸药会先要了我们的命......
[multiline(name="巴别塔成员", end=true)]咳。
[multiline(name="巴别塔成员")]我们必须立刻——
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[multiline(name="巴别塔成员")]咳咳——
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="巴别塔成员", end=true)]咳咳咳——
[name="巴别塔成员"]......不，不，不能再拖下去了。空气里都是源石颗粒，*萨卡兹粗口*。
[name="巴别塔成员"]七八天没有药物补给了......队伍里的伤员......感染情况......该死！
[dialog]
[PlaySound(key="$d_gen_thunders_amb", volume=0.4)]
[PlaySound(key="$d_avg_drkcludsthdr", volume=1, loop=true, channel="d")]
[delay(time=1.5)]
[name="巴别塔成员"]什、什么声音？
[dialog]
[CameraShake(duration=1, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[charslot]
[Background(image="30_ex1_snowmount_s",screenadapt="coverall")]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_053")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="萨卡兹雇佣兵"]巴别塔的救援还没到吗？没有？那就继续让斥候探路去，找不到别回来了！
[name="萨卡兹雇佣兵"]嘁，天灾云都成型了，是哪支*萨卡兹粗口*的部队袭击了医疗据点！“疤眼”都没这么疯！
[name="萨卡兹雇佣兵"]后面的人跟紧点！来不及离开天灾范围，我们得找几个干净的洞窟躲一躲！洞里有源石痕迹的不行，有一点都不行！
[name="萨卡兹雇佣兵"]......真该死！伤员都不放过，你真不是个东西特雷西斯......
[dialog]
[StopSound(channel="d", fadetime=1)]
[StopSound(channel="snow", fadetime=1)]
[curtain(direction = 2,fillfrom = 0,fillto = 1,fadetime=0.5)]
[delay(time=1)]
[bgeffect]
[curtain]
[charslot]
[Background(image="bg_cave_2",screenadapt="coverall")]
[curtain(direction = 2,fillfrom = 1,fillto = 0,fadetime=0.5)]
[Delay(time=1)]
[name="萨卡兹孩子"]妈妈......我疼......腿疼......
[charslot(slot = "m", name = "avg_npc_935_1#1$1")]
[name="萨卡兹平民"]不、不哭，孩子，再忍一忍，忍一忍就能回家了......
[charslot(slot = "m", focus="n")]
[multiline(name="萨卡兹孩子")]不要——不要——
[multiline(name="萨卡兹孩子",end=true)]呜啊啊啊疼——疼......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_thundercloud",screenadapt="coverall")]
[PlaySound(key="$d_avg_drkcludsthdr", volume=1, loop=true, channel="d")]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="s")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
孩子的哭声。
阴谋的声音，死亡的声音，求生的声音。
天灾无情，只是吞吃风雪，酝酿风暴。
[dialog]
[SoundVolume(volume=0.4, channel="s",fadetime=2)]
[SoundVolume(volume=0.4, channel="d",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="30_ex1_snowmount_s",screenadapt="coverall")]
[bgeffect(name="$eb_lightsnow", layer=1)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
远方的山崖上，有几道人影。
风雪肃穆，站在悬崖边的女性只是沉默地看着远方。
无情的天灾，在要道镇守的敌方士兵，逃窜的野兽，走投无路的伤员和平民。
生命如空谷回响，回到Mantra的耳中，那是——
——孩子的哭声。
[dialog]
[charslot(slot = "m", name = "avg_npc_1300_1#7$1")]
[name="Mantra"]......我听见了。
[name="Mantra"]孩子的哭声。
[dialog]
[charslot]
[playsound(key="$d_avg_snowbootwalk")]
[charslot(slot = "m", name = "avg_npc_1309_1#1$1", duration=1.5, isblock=true)]
[name="Ace"]开始飘雪了，情况不太好。
[charslot(slot = "m", name = "avg_npc_1300_1#3$1")]
[name="Mantra"]两千三百一十三人。
[name="Mantra"]全部确认。
[charslot(slot = "m", name = "avg_npc_1309_1#1$1")]
[name="Ace"]......位置，生命体征，已经全部录入。
[dialog]
[playsound(key="$transmission")]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1309_1#1$1")]
[name="Ace"]损失比想的要少，但还是得抓紧了。
[name="Ace"]Mantra小姐，近距离目睹你的源石技艺，还是让人大开眼界。
[charslot(slot = "m", name = "avg_npc_1300_1#3$1")]
[name="Mantra"]（谦逊地点头致意）
[charslot(slot = "m", name = "avg_npc_1309_1#1$1")]
[name="Ace"]人事部的那位笞心魔还没有为你物色到几名出色的通讯兵？
[charslot(slot = "m", name = "avg_npc_1300_1#2$1")]
[name="Mantra"]（轻闭双眼）
[charslot(slot = "m", name = "avg_npc_1309_1#1$1")]
[name="Ace"]遗憾。
[name="Ace"]......信息已发送至全部行动队。
[charslot(slot = "m", name = "avg_npc_1300_1#3$1")]
[name="Mantra"]东北方向，七公里，洞窟。
[name="Mantra"]孩子们在那里。
[charslot(slot = "m", name = "avg_npc_1309_1#1$1")]
[name="Ace"]但军事委员会的侦察无人机已经发现我们了。
[name="Ace"]我留下，你去吧。
[charslot(slot = "m", name = "avg_npc_1300_1#4$1")]
[name="Mantra"]（皱眉）
[charslot(slot = "m", name = "avg_npc_1309_1#1$1")]
[name="Ace"]他们不敢选在这个地形和我的小队正面冲突。
[name="Ace"]放心吧。只是去打个招呼，如果是曼弗雷德领头，我就争取把他活捉了。
[charslot(slot = "m", name = "avg_npc_1300_1#1$1")]
[name="Mantra"]不要冒险——
[dialog]
[charslot]
[playsound(key="$d_gen_transmissionget", volume=1)]
[CharacterCutin(widgetID="1", name="avg_npc_048", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=-300, width=200, block=true)]
[delay(time=1)]
[name="博士"]各位，是我。
[name="博士

... (全文31070字符)
```

### level_act33side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[Background(image="bg_room_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="博士"]......
一块源石结晶安静地躺在试验台上，在灯光下泛起橙黄色的光。
它看上去纯净、美丽、无害。
[dialog]
[charslot(slot = "m", name = "avg_npc_048", duration=1.5, isblock=true)]
[name="博士"]普瑞赛斯......我们究竟......
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[Background(image="46_g6_rmbtmine",screenadapt="coverall")]
[charslot(slot = "m", name = "avg_230_savage_1#5$1")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[name="暴行"]很遗憾......这是不可能的。
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[Background(image="46_g4_rmbtwild_d",screenadapt="coverall")]
[charslot(slot = "m", name = "avg_npc_1295_1#7$1")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[name="阿米娅"]博士......身上......好疼......
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[Background(image="bg_snowconutry_4",screenadapt="coverall")]
[charslot(slot = "m", name = "avg_npc_932_1#1$1", bstart=0.2,bend=0.7)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[name="垂死的感染者"]感......谢......您......
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[charslot(slot = "m", name = "avg_npc_048")]
[Background(image="bg_room_2",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[charslot(duration=1.5, isblock=true)]
坐在台前的人拿起了源石结晶，插入了自己的手臂。
[dialog]
[PlaySound(key="$d_avg_attack_heavy", volume=1)]
[Delay(time=1.5)]
[PlaySound(key="$blooddrop", volume=1)]
瘦削的手臂上鲜血淋漓，但除了多出一道血肉模糊的伤口，什么都没有发生。
痛感逐渐清晰起来。
可这不是被源石感染的痛。
检测仪器也清楚地显示，细胞和源石没有任何融合的迹象。
[charslot(slot = "m", name = "avg_npc_048")]
[name="博士"]......源石不会感染我。
[name="博士"]我们可曾想到这其中的痛苦会是这样的模样？
[name="博士"]如果是你，你打算怎么评判这片大地的现状呢......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[name="博士"]（未知语言）“源石”。
[name="博士"]（未知语言）我们唯一延续的——灯火。
[dialog]
[charslot]
[Background(image="bg_infirmary",screenadapt="coverall")]
[PlaySound(key="$d_avg_heartratemonitor", volume=0.6, loop=true, channel="h")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[StopSound(channel="h", fadetime=2)]
[name="阿米娅"]......
[name="阿米娅"]（平稳的呼吸）
[dialog]
[charslot(slot = "m", name = "avg_npc_048", duration=0.5, isblock=true)]
[name="博士"]生效了。
[charslot(slot = "m", name = "avg_003_kalts_1#1$1")]
[name="凯尔希"]效率比过去的抑制剂高出几倍。阿米娅血液里源石结晶密度也有明显下降。
[charslot(slot = "m", name = "avg_003_kalts_1#5$1")]
[name="凯尔希"]可是......
[charslot(slot = "m", name = "avg_npc_048")]
[name="博士"]还只是实验性质的。我还没找到能在泰拉量产的办法。
[charslot(slot = "m", name = "avg_003_kalts_1#5$1")]
[name="凯尔希"]博士！
[charslot(slot = "m", name = "avg_003_kalts_1#4$1")]
[name="凯尔希"]我知道你在用自己的身体做实验......可你的状态真的不太好。
[charslot(slot = "m", name = "avg_npc_048")]
[name="博士"]关于血液的研究而已。
[name="博士"]源石感染不了我，早在它还只是能源项目的时候便设下了保险。也许利用这一点，可以缓和矿石病的病症。
[name="博士"]还有特蕾西娅。她和你不一样，“文明的存续”本身不是什么强大的魔法，她只是靠着无数传承，创作了最根本的源石技艺形态。
[name="博士"]也许有她的帮助，我们可以研制出更进一步、可持续生产的矿石病药物......
[charslot(slot = "m", name = "avg_003_kalts_1#4$1")]
[name="凯尔希"]现在，我更担心你的状态，博士。
[charslot(slot = "m", name = "avg_npc_048")]
[name="博士"]没关系。
[name="博士"]既然源石已经把你们塑造成了与我们相差无几的形态，那么，总能找到替代我身体的办法制造血清......
[name="博士"]无论眼下的问题有多么复杂，只要巴别塔能拿出有效的矿石病药物，支持我们的萨卡兹......不......
[name="博士"]整片大地上支持巴别塔的人将会不计其数。
[name="博士"]到了那时，我们就可以——
[dialog]
[musicvolume(volume=0.2, fadetime=0.5)]
[PlaySound(key="$d_avg_humanchange", volume=1)]
[delay(time=0.4)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[Subtitle(text="<color=#000000>可以平静地、幸福地、安稳地等待源石孕育一个不必终结的未来。</color>", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Background(image="bg_infirmary",screenadapt="coverall")]
[musicvolume(volume=0.6, fadetime=1)]
[delay(time=0.4)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot(slot = "m", name = "avg_003_kalts_1#4$1")]
[name="凯尔希"]不，听我说。
[charslot]
凯尔希猛地抓住了博士的手腕。
她隐约察觉到，博士的手腕纤细了许多。
[charslot(slot = "m", name = "avg_003_kalts_1#4$1")]
[name="凯尔希"]从雷姆必拓之旅到萨卡兹内战，你从未有一刻放松过自己。
[name="凯尔希"]是我决定将你唤醒，是我希望你能为这片文明......这片令我越发意外、越发惊喜，也越发无所适从的文明指明出路。
[charslot(slot = "m", name = "avg_003_kalts_1#9$1")]
[name="凯尔希"]但我不希望你在此刻透支自己。
[name="凯尔希"]你该更爱惜你自己一些。
[charslot(slot = "m", name = "avg_npc_048")]
[name="博士"]......抱歉。
[name="博士"]不过现在，我更想减轻阿米娅的痛苦。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[charslot]
[Background(image="bg_motorroom",screenadapt="coverall")]
[PlaySound(key="$d_avg_labamb", volume=1, loop=true, channel="l")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
三个月后
卡兹戴尔地区，巴别塔罗德岛本舰
[charslot(slot = "l", name = "avg_npc_048")]
[name="博士"]......阿米娅，我看到你了，出来吧。
[dialog]
[SoundVolume(volume=0.2, channel="l",fadetime=2)]
[PlayMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[charslot(slot = "r", name = "avg_npc_1295_1#10$1", posfrom="200,0", posto="0,0", duration=1.5, isblock=true)]
[charslot(slot = "r", focus=

... (全文21652字符)
```

### level_act33side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_energywell", volume=0.4, loop=true, channel="e")]
[Background(image="bg_abyss_1",screenadapt="coverall", xScale=1.08, yScale=1.08)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_048", duration=1.5, isblock=true)]
[name="博士"]启用管理员权限加密。
[name="博士"]影像编号<color=#FF4200>（0018_admin）</color>......
[name="博士"]启动记录......开始录影。
[dialog]
[PlaySound(key="$d_avg_signlntrfrnc", volume=1)]
[bgeffect(name="$eb_signalInterference", layer=0)]
[delay(time=0.5)]
[bgeffect(name="$eb_oldtv", layer=1)]
[PlaySound(key="$d_avg_oldtvelectricity", volume=1, loop=true, channel="o")]
[delay(time=2)]
[name="博士"]......
[name="博士"]......
[name="博士"]......在沉睡岁月中，我们的家园在毁灭中孕育了新生。
[name="博士"]源石是他们的引航人，将来自塔卫二的生命，塑造成与我们相近的模样。
[name="博士"]我是幸运的。我能够跨越万年与他们交流。我甚至一度将自己视作这片大地上的一员，感受到他们的过去与未来。
[name="博士"]但我终究不属于这里。我甚至开始为特蕾西娅的努力......而感到不安。
[name="博士"]如果源石计划以失败告终，不，哪怕只是推迟一些时间，特蕾西娅，凯尔希，甚至是我许诺给阿米娅的那个未来......
[name="博士"]这颗星球所孕育的，我们已知范围内为数不多的生命，都只是一个一触即破的泡影。
[name="博士"]我自欺欺人了很长时间。可......我又要如何向凯尔希解释？如何向特蕾西娅，向阿米娅解释？
[name="博士"]我要怎么对她们说，“你们所遭受的折磨，才是拯救你们的唯一办法，你们应当放弃抵抗”？
[name="博士"]我要怎么对她们说，“泰拉文明只是昙花一现的错觉，唯有被源石接纳，我们才有逆转命运的机会”？
[name="博士"]看着一个个具体的生命以感染者之名在眼前如烟散去，我心里并不好受。
[name="博士"]这在泰拉早已让人司空见惯的景象，却终归是属于生命的逝去，悲哀而残酷。
[name="博士"]我已经太久没有听见过鲜活的话语。我无法真的把他们当做意外的火花。
[name="博士"]可我看见的，却并非战士之死......
[name="博士"]而是他们顺应了源石同化的进程，通过死亡成为了内化宇宙的局部，成为了生命能够突破终极黑暗的契机。
[name="博士"]我到底该为他们的死而垂头默哀......还是为计划的顺利而私下庆幸？
[name="博士"]特蕾西娅为此孜孜不倦地研究，凯尔希，我们的AMa-10，同样选择了相信泰拉的可能性，选择对抗源石，制止战争......
[name="博士"]......但是，我呢？
[name="博士"]源石计划经过了多少代人的努力，在那期间，我们的同胞死去了百亿千亿，换来的也只是跨过万年的等待......
[name="博士"]然后，火种递交到了我的手上。在万年之后。难道我就能......放弃了？
[name="博士"]因为这短短几年里，泰拉给我的惊喜？特蕾西娅和凯尔希......做出的选择？
[name="博士"]哪怕只是对阿米娅动了恻隐之心，始终自私的，难道不是我吗？
[name="博士"]我......以拯救者的身份被唤醒，我却是他们注定的毁灭者。
[name="博士"]她们，将毁灭者，将我，如拯救者那般唤醒......
[name="博士"]（哽咽）
[name="博士"]......阿米娅......凯尔希......
[name="博士"]......我该怎么做？
[name="博士"]普瑞赛斯......我该怎么做？
[dialog]
[StopSound(channel="o", fadetime=0.5)]
[PlaySound(key="$d_avg_humanchange", volume=1)]
[delay(time=0.4)]
[StopSound(channel="e", fadetime=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[bgeffect]
[charslot]
[Background]
[Subtitle(text="也许我应该把一切向凯尔希与特蕾西娅和盘托出。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="源石已经引领他们走向大致正确的道路。尽管傲慢，但这确实足以让这些生灵创造别样的奇迹。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Subtitle(text="<color=#000000>也许我必须重新审视特蕾西娅和凯尔希的计划。</color>", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<color=#000000>巴别塔的研究超乎预计，但泰拉的政治形态非常原始，巴别塔尚无跨过种族和国家的隔阂代表整体的能力。</color>", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[PlaySound(key="$d_avg_humanchange", volume=0.4)]
[delay(time=0.4)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.3, block=true)]
[charslot]
[Background]
[Subtitle(text="相信泰拉。相信人们总能够赢得自己的未来。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[PlaySound(key="$d_avg_humanchange", volume=0.6)]
[delay(time=0.4)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Subtitle(text="<color=#000000>推进计划。至少让他们存在过的痕迹得以在源石中保留。</color>", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[PlaySound(key="$d_avg_humanchange", volume=0.8)]
[delay(time=0.2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[charslot]
[Background]
[Subtitle(text="相信她。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[PlaySound(key="$d_avg_humanchange", volume=1)]
[delay(time=0.2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Subtitle(text="<color=#000000>制止她。</color>", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[PlaySound(key="$d_avg_humanchange", volume=1)]
[delay(time=0.2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[delay(time=2)]
[PlayMusic(key="$calm_loop", volume=0.6)]
[Background(image="49_g11_rhodesdeck_bc",screenadapt="coverall", xScale=1.05, yScale=1.05)]
[backgroundTween(xScaleFrom=1.05, yScaleFrom=1.05, xScaleTo=1, yScaleTo=1, duration=15,block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[Delay(time=1)]
[name="普瑞赛斯"]......怎么会！我怎么会怪你呢？
[name="普瑞赛斯"]我能理解你的忐忑不安。我们争论的事，本就远超“人类”这小小的生命形态该去插手的范畴。
[name="普瑞赛斯"]但这是唯一的办法。你我应该都如此坚信。
[name="普瑞赛斯"]如果......在祂回归之前我们还有时间，我们可以一同去想象，去实现。去描绘宇宙的边界与万事万物的形状。
[name="普瑞赛斯"]而那些脆弱的时刻，我希望你都能站在我这边。
[name="普瑞赛斯"]你一定会的，对吧。
[dialog]
[stopmusic(fadetime=1)]
[PlaySound(key="$d_avg_signlntrfrnc", volume=1)]
[bgeffect(name="$eb_signalInterference", fade = true, fadetime = 1.5,layer=1)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background(image="49_g10_theresaoffice",screenadapt="coverall")]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1296_1#1$1")]
[charslot(slot = "l", name = "avg_npc_1311_1#1$1")]
[PlayMusic(intro=

... (全文17029字符)
```

### level_act33side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Background(image="49_g3_kazdelstreet_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
1094年初
卡兹戴尔地区，卡兹戴尔移动城市
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1297_1#1$1", posfrom="-300,0", posto="0,0", duration=2)]
[delay(time=1.5)]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="b")]
[StopSound(channel="b", fadetime=2.5)]
[Delay(time=1.5)]
[charslot(slot = "l", name = "avg_npc_404_1#1$1",  posfrom="-300,0", posto="0,0", duration=0.8, focus="l", isblock=true)]
[Delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_404_1#6$1", focus="l")]
[name="曼弗雷德"]请等等，将军！
[charslot(slot = "r", name = "avg_npc_1297_1#4$1", focus="r")]
[name="特雷西斯"]你太浮躁了。
[charslot(slot = "l", name = "avg_npc_404_1#2$1", focus="l")]
[name="曼弗雷德"]但是！那位公爵的使者几乎是打算把唾沫吐在——
[charslot(slot = "r", name = "avg_npc_1297_1#1$1", focus="r")]
[name="特雷西斯"]我们得到想要的了吗？
[charslot(slot = "l", name = "avg_npc_404_1#2$1", focus="l")]
[name="曼弗雷德"]的确拿到了部分工业区的使用权和边境通行权......但一定要以那样屈辱的方式吗？
[name="曼弗雷德"]维多利亚的公爵对您呼来喝去，把萨卡兹当作顺从的野兽，那些从内战中抬起头来的战士们等待的并不是今天，将军！
[charslot(slot = "r", name = "avg_npc_1297_1#1$1", focus="r")]
[name="特雷西斯"]那不是正如我们所愿？
[charslot(slot = "r", name = "avg_npc_1297_1#4$1", focus="r")]
[name="特雷西斯"]难道我们想要维多利亚从一开始就把萨卡兹当作最大的敌人，然后团结一致来对付我们？
[charslot(slot = "l", name = "avg_npc_404_1#3$1", focus="l")]
[name="曼弗雷德"]这也是您的......我知道示敌以弱的必要性，可这......
[charslot(slot = "l", name = "avg_npc_404_1#9$1", focus="l")]
[name="曼弗雷德"]可我们之中的很多人，认为这毫不荣耀——
[charslot(slot = "r", name = "avg_npc_1297_1#1$1", focus="r")]
[name="特雷西斯"]我许诺他们的，是荣耀吗？
[name="特雷西斯"]维多利亚人眼里的萨卡兹，有荣耀吗？
[charslot(slot = "r", name = "avg_npc_1297_1#2$1", focus="r")]
[name="特雷西斯"]曼弗雷德，你最近太急躁了。
[charslot(slot = "l", name = "avg_npc_404_1#9$1", focus="l")]
[name="曼弗雷德"]......
[charslot(slot = "r", name = "avg_npc_1297_1#1$1", focus="r")]
[name="特雷西斯"]......尊严很重要，曼弗雷德。
[name="特雷西斯"]你会为战士们打抱不平，也会有人因此而尊敬你。若是平常，也许我会夸赞你。
[charslot(slot = "r", name = "avg_npc_1297_1#4$1", focus="r")]
[name="特雷西斯"]但现在，我们在做什么？在准备窃取一个国家的心脏。
[name="特雷西斯"]在瓦解这片大地上最强大的帝国。
[name="特雷西斯"]他们的隔阂令他们脆弱不堪，而萨卡兹正饥肠辘辘。
[name="特雷西斯"]那我们需要的本就不是“荣耀”“尊敬”。
[charslot(slot = "l", name = "avg_npc_404_1#1$1", focus="l")]
[name="曼弗雷德"]......我明白。
[charslot(slot = "r", name = "avg_npc_1297_1#1$1", focus="r")]
[name="特雷西斯"]我们的军队准备得如何了？
[charslot(slot = "l", name = "avg_npc_404_1#1$1", focus="l")]
[name="曼弗雷德"]整装待发。先行的同胞会在伦蒂尼姆接应我们。
[name="曼弗雷德"]很快就是卡文迪许公爵要求我们抵达的最后期限，我们随时可以出发。
[charslot(slot = "r", name = "avg_npc_1297_1#1$1", focus="r")]
[name="特雷西斯"]好。
[name="特雷西斯"]我们启程，去毁灭维多利亚。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="49_g7_councilchamber",screenadapt="coverall")]
[Delay(time=1)]
[charslot(slot="r", name="avg_npc_419_1#1$1")]
[charslot(slot="l", name="avg_npc_419_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1.5)]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m", name="avg_npc_404_1#1$1", duration=1.5, isblock=true)]
[name="曼弗雷德"]你们一直在值守？
[charslot(slot="m", name="avg_npc_419_1#1$1")]
[name="军事委员会卫士"]是的。
[charslot(slot="m", name="avg_npc_404_1#1$1")]
[name="曼弗雷德"]......
[name="曼弗雷德"]先退下吧，我想一个人待一会儿。
[charslot]
[charslot(slot="r", name="avg_npc_419_1#1$1")]
[charslot(slot="l", name="avg_npc_419_1#1$1")]
[name="军事委员会卫士"]是，长官。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="r", afrom=1, ato=0, duration=1)]
[delay(time=0.5)]
[charslot(slot="l", afrom=1, ato=0, duration=1, isblock=true)]
[delay(time=1)]
[charslot(slot="m", name="avg_npc_404_1#1$1")]
[name="曼弗雷德"]......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5, isblock=true)]
[PlaySound(key="$d_avg_opencabinet", volume=1)]
[delay(time=1.5)]
待守卫离去，曼弗雷德取出放在一旁的酒杯。
[dialog]
[PlaySound(key="$d_avg_openwindow", volume=1)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="sn")]
[delay(time=1.5)]
[charslot(slot="m", name="avg_npc_404_1#6$1", duration=0.5, isblock=true)]
[name="曼弗雷德"]来一杯吗？
[dialog]
[charslot]
[StopSound(channel="sn", fadetime=1.5)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_4132_ascln_1#1$1", bstart=0.2,bend=0.7, duration=1.5, isblock=true)]
[name="阿斯卡纶"]你以前从不喝酒。
[charslot(slot="m", name="avg_npc_404_1#1$1")]
[name="曼弗雷德"]我现在也不喝。
[name="曼弗雷德"]但是将军命令我学习维多利亚人的“礼仪”，为接下来的任务做准备。
[charslot(slot="m", name="avg_npc_404_1#3$1")]
[name="曼弗雷德"]我现在才知道，原来那些贵族吃一顿饭需要搭配好几种酒，每种酒还要搭配不同的杯子。
[dialog]
[delay(time=1)]
[charslot(slot="m", name="avg_npc_404_1#4$1")]
[name="曼弗雷德"]你还记得吗？小时候将军领着我们去古战场练剑......晚上天气冷，将军煮了汤才发现我们没有盛汤的东西。
[name="曼弗雷德"]不过战场四处都散落着炮弹壳，你就用它们削了四只杯子。
[name="曼弗雷德"]你、我、将军还有殿下，就端着弹壳做的杯子，围坐在篝火前。
[charslot(slot = "m", name = "avg_4132_ascln_1#1$1", bstart=0.2,bend=0.7)]
[name="阿斯卡纶"]我记得，很安静的一夜。
[charslot(slot="m", name="avg_npc_404_1#1$1")]
[name="曼弗雷德"]就和现在一样。
[dialog]
[charslot]
残冬冰凉的月光落进窗户，曼弗雷德的手按上剑柄，也是一样的冰凉。
空气里静极了，两人都可以听到彼此的心跳。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_4132_ascln_1#1$1", duration=1.5, isblock=true)]
[name="阿斯卡纶"]你们明天就会去伦蒂尼姆。
[charslot(slot="m", name="avg_npc_404_1#1$1")]
[name="曼弗雷德"]我知道，你想见将军。
[charslot(slot = "m", name = "avg_4132_ascln_1#1$1")]
[name="阿斯卡纶"]......
[charslot(slot="m", name="avg_npc_404_1#7$1")]
[name="曼弗雷德"]你应该没见到，不然也不会到我这来。
[charslot(slot = "m", name = "avg_4132_ascln_1#1$1")]
[name="阿斯卡纶"]是我放弃了。
[charslot(slot = "m", name = "avg_4132_ascln_1#4$1")]
[name="阿斯卡纶"]我发现自己远远看到他的第一眼，脑海冒出的念头是，我现在应该动手杀了他。
[charslot(slot="m", name="avg_npc_404_1#1$1")]
[name="曼弗雷德"]那你应该庆幸自己保住了一丝理性。
[name="曼弗雷德"]所以，你现在来找我？
[charslot(slot

... (全文15148字符)
```

### level_act33side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(key="$saferoom_loop", volume=0.6)]
[Background(image="49_g15_rhodesdeck_n",screenadapt="coverall")]
[PlaySound(key="$d_avg_snowstormflp", volume=0, loop=true, channel="sn")]
[SoundVolume(volume=0.4, channel="sn",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
1094年春
卡兹戴尔地区，巴别塔罗德岛本舰
[dialog]
[charslot(slot = "r", name = "avg_npc_1299_1#1$1", duration=1, isblock=true)]
[Delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1299_1#1$1", focus="r")]
[name="尤莉叶"]阿斯卡纶，我就知道你会来。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_4132_ascln_1#1$1", posfrom="-200, 0", posto="0, 0", duration=1.5, isblock=true)]
[charslot(slot = "l", name = "avg_4132_ascln_1#1$1", focus="l")]
[name="阿斯卡纶"]......也只剩下我了。
[charslot(slot = "r", name = "avg_npc_1299_1#1$1", focus="r")]
[name="尤莉叶"]是啊。
[charslot(slot = "r", name = "avg_npc_1299_1#3$1", focus="r")]
[name="尤莉叶"]这几年，我认识的，熟悉的，能说得上几句话的，也就剩你活着了。
[charslot(slot = "l", name = "avg_4132_ascln_1#7$1", focus="l")]
[name="阿斯卡纶"]......
[name="阿斯卡纶"]这次，你的任务......
[charslot(slot = "r", name = "avg_npc_1299_1#1$1", focus="r")]
[name="尤莉叶"]去伦蒂尼姆，你知道了。
[charslot(slot = "r", name = "avg_npc_1299_1#2$1", focus="r")]
[name="尤莉叶"]说实话，心里有点忐忑，卧底任务不是第一次做，但......
[name="尤莉叶"]这其实是我第一次离开卡兹戴尔。
[charslot(slot = "r", name = "avg_npc_1299_1#1$1", focus="r")]
[name="尤莉叶"]阿斯卡纶，听说你有过几个月外出游行的经验？
[charslot(slot = "l", name = "avg_4132_ascln_1#1$1", focus="l")]
[name="阿斯卡纶"]但是和去维多利亚不一样。
[name="阿斯卡纶"]你的任务是蛰伏在特雷西斯的雇佣兵队伍里，并在合适的时机发动叛乱。
[charslot(slot = "r", name = "avg_npc_1299_1#3$1", focus="r")]
[name="尤莉叶"]......杀了特雷西斯真的能解决问题吗？
[charslot(slot = "l", name = "avg_4132_ascln_1#1$1", focus="l")]
[name="阿斯卡纶"]不能，军事委员会已经不再依赖任何一个强大的个体。这也是特雷西斯的目的。
[name="阿斯卡纶"]所以你们任务的实际策略是，在必要的时候掀起骚乱，引起维多利亚公爵的怀疑，借刀杀人。
[name="阿斯卡纶"]伦蒂尼姆，维多利亚的腹地，他们无处可逃。那里将是整个军事委员会的覆灭之所。
[charslot(slot = "r", name = "avg_npc_1299_1#8$1", focus="r")]
[name="尤莉叶"]然后，你们就有机会把食腐者王庭暴打一顿，占领卡兹戴尔了，对吧？
[charslot(slot = "l", name = "avg_4132_ascln_1#7$1", focus="l")]
[name="阿斯卡纶"]但是，尤莉叶，你应该......
[charslot(slot = "r", name = "avg_npc_1299_1#9$1", focus="r")]
[name="尤莉叶"]别这样！我懂的，卧底不是没当过，但要同时欺骗特雷西斯和维多利亚人......我连菲林都没见过几个！
[charslot(slot = "r", name = "avg_npc_1299_1#8$1", focus="r")]
[name="尤莉叶"]我特地磨炼了一下维多利亚语来着......
[charslot(slot = "l", name = "avg_4132_ascln_1#1$1", focus="l")]
[name="阿斯卡纶"]......我不是说这个。
[charslot(slot = "l", name = "avg_4132_ascln_1#2$1", focus="l")]
[name="阿斯卡纶"]算了，给你。
[charslot(slot = "r", name = "avg_npc_1299_1#1$1", focus="r")]
[name="尤莉叶"]......这是？我的旧衣服？
[charslot(slot = "r", name = "avg_npc_1299_1#7$1", focus="r")]
[name="尤莉叶"]内衬上绣了我的名字......是殿下？
[charslot(slot = "l", name = "avg_4132_ascln_1#3$1", focus="l")]
[name="阿斯卡纶"]殿下本来想亲自交给你，但是，我不希望你们两个相见。
[name="阿斯卡纶"]我......不想让殿下难受。
[charslot(slot = "r", name = "avg_npc_1299_1#6$1", focus="r")]
[name="尤莉叶"]......
[charslot(slot = "l", name = "avg_4132_ascln_1#1$1", focus="l")]
[name="阿斯卡纶"]你知道我刚才的话是什么意思。你应该知道，在这个计划里，所有人都是弃子。
[name="阿斯卡纶"]殿下清楚这一点，她想亲自送别你们每一个人，但这样会让她夜不能寐。
[charslot(slot = "l", name = "avg_4132_ascln_1#2$1", focus="l")]
[name="阿斯卡纶"]所以我骗了她。我说你们提前出发了。
[dialog]
[delay(time=1)]
[charslot(slot = "l", name = "avg_4132_ascln_1#7$1", focus="l")]
[name="阿斯卡纶"]抱歉，尤莉叶。也许你是想见殿下一面的。
[charslot]
尤莉叶没有回答，只是默默摩挲着棉麻编织的名字，感受着其粗糙的质感。
“尤莉叶”。
她想起了殿下为他们上课的样子。
比起上课学习，她更习惯杀人。虽然在课上什么都听不懂老打瞌睡，但内心的声音告诉她，殿下只说正确的事。
所以她从不提问。
[charslot(slot = "l", name = "avg_4132_ascln_1#7$1", focus="n")]
[charslot(slot = "r", name = "avg_npc_1299_1#9$1", focus="r")]
[name="尤莉叶"]......谁不想最后见一眼殿下呢。不过，你来送送我，也挺好的。这些年，我也从你这儿学到了不少。
[charslot(slot = "r", name = "avg_npc_1299_1#8$1", focus="r")]
[name="尤莉叶"]啊。你不会觉得，自己是更胜任这个任务的人选吧？
[charslot(slot = "l", name = "avg_4132_ascln_1#2$1", focus="l")]
[name="阿斯卡纶"]我没有。
[charslot(slot = "r", name = "avg_npc_1299_1#8$1", focus="r")]
[name="尤莉叶"]其实会议上确实有人提到你，不过我们一致认为，你应该待在卡兹戴尔，待在殿下身边。
[name="尤莉叶"]至于我，本来就无依无靠的，所以就第一个提出......
[charslot(slot = "l", name = "avg_4132_ascln_1#1$1", focus="l")]
[name="阿斯卡纶"]......你可以去Scout的队伍。我记得你都提出申请了。
[charslot(slot = "r", name = "avg_npc_1299_1#8$1", focus="r")]
[name="尤莉叶"]那是为了向那个英雄好好学习，然后赢你一次。
[name="尤莉叶"]大家都是差不多的路数，我还没赢过你几次就要走了，心里过不去。
[charslot(slot = "r", name = "avg_npc_1299_1#9$1", focus="r")]
[name="尤莉叶"]哼。要不是临行前，我还真不乐意和你说这个。
[charslot(slot = "l", name = "avg_4132_ascln_1#7$1", focus="l")]
[name="阿斯卡纶"]还......有什么要说的吗？
[charslot(slot = "r", name = "avg_npc_1299_1#8$1", focus="r")]
[name="尤莉叶"]没了。没想到我第一次离开家乡，就是最后一次。也没想到，最后目送我离开的，是魔王身边不苟言笑的刺客头子。
[charslot(slot = "r", name = "avg_npc_1299_1#1$1", focus="r")]
[name="尤莉叶"]阿斯卡纶，你别骗我，你老实回答我。
[name="尤莉叶"]外面的大地，怎么样？
[charslot(slot = "l", name = "avg_4132_ascln_1#3$1", focus="l")]
[name="阿斯卡纶"]......
[dialog]
[charslot(duration=0.5, isblock=true)]
阿斯卡纶没有答话。而尤莉叶似乎也没打算从她嘴里得到回答。
尤莉叶只是缓缓地起身，缓缓地离去。
悠然的背影仿佛只是去取一壶上好的酒。
阿斯卡纶就这么看着她的背影，看着她走远。
她忽然有些不认识尤莉叶，就像不认识影子和另一个自己。
[dialog]
[StopSound(channel="sn", fadetime=2)]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="34_g1_victoriavillage",screenadapt="coverall", xScale=1.1, yScale=1.1,x=-60)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
三个月后
维多利亚，伦蒂尼姆郊外村庄
[dialog]
[playMusic(intro="$jealous_intro", key="$jealous_loop", volume=0.6)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1299_1#1$1", duration=1.5, isblock=true)]
[name="尤莉叶"]出来吧，你躲着没用。
[name="尤莉叶"]我们在城里收到消息，有一支准备去卡兹戴尔活动的队伍，应该就是你们吧？
[charslot(slot = "m", name = "avg_npc_1299_1#4$1")]
[name="尤莉叶"]这个村子其他路都被我们拦住了，你试图从我这里突破是在做梦。
[dialog]
[charslot(slot = "r", name = "avg_npc_1307_1#1$1", posfrom="200,0", posto="-50,0", bstart=0.2, bend=0.7, duration=0.2, isblock=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness

... (全文26550字符)
```

### level_act33side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_snowstormflp", volume=0, loop=true, channel="sn")]
[SoundVolume(volume=1, channel="sn",fadetime=2)]
[Background(image="bg_desert_3",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
卡兹戴尔地区，荒野某处
[dialog]
[charslot(slot = "m", name = "avg_npc_1294_1#2$1", duration=1, isblock=true)]
[name="“疤眼”"]......
[name="“疤眼”"]......哈。
[name="“疤眼”"]哈哈——哈哈哈哈——
[name="“疤眼”"]预言？什么预言，阿斯卡纶没有杀掉我，没有！
[name="“疤眼”"]被言说的仍需辨别，被辨别的仍可更改——预言法术的本质不过是推测和计算，当然没什么无法违逆的命运！
[name="“疤眼”"]独眼巨人王庭就是一个天大的笑话！
[name="“疤眼”"]......啐。真疼。
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[SoundVolume(volume=0.2, channel="sn",fadetime=2)]
[charslot(slot = "r", name = "avg_npc_053", duration=1)]
[Delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_053", duration=1, isblock=true)]
[Delay(time=1)]
[charslot]
[charslot(slot = "m", name = "avg_npc_1294_1#2$1")]
[name="“疤眼”"]我没有死在阿斯卡纶手里，我没有如自己预言的那般死在阿斯卡纶手里......
[name="“疤眼”"]那么死的就该是她了。
[name="“疤眼”"]她势必会来确认我的尸体，那么，你们就会钉住她的影子，撕扯她的身体。
[name="“疤眼”"]她也受了伤，我也不是白白挨打......
[dialog]
[PlaySound(key="$d_avg_drawsword", volume=1)]
[Delay(time=1)]
[name="“疤眼”"]......你们在做什么？
[charslot(slot = "m", name = "avg_npc_053")]
[name="萨卡兹雇佣兵"]......
[charslot(slot = "m", name = "avg_npc_1294_1#2$1")]
[name="“疤眼”"]在这个时候，把武器，对准我？
[name="“疤眼”"]谁收买了你们？
[charslot(slot = "m", name = "avg_npc_053")]
[name="萨卡兹雇佣兵"]没有任何人，老大。
[name="萨卡兹雇佣兵"]只是个借机上位的好机会。
[charslot(slot = "m", name = "avg_npc_1294_1#2$1")]
[name="“疤眼”"]好机会？确实是个好机会......巴别塔进了城，你们可以用我的人头讨好他们。
[name="“疤眼”"]巴别塔要是输了，你们也可以回到疤痕商场，把握住自己的处境。
[name="“疤眼”"]......
[charslot(slot = "m", name = "avg_npc_053")]
[name="萨卡兹雇佣兵"]......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5, isblock=true)]
[Delay(time=0.5)]
“疤眼”沉默地看着这些被他亲手安排在此的伏兵。
风掠过，有一些自己的血腥味。
[charslot(slot = "m", name = "avg_npc_1294_1#2$1")]
[name="“疤眼”"]呵。
[name="“疤眼”"]好算计啊，老伙计们。
[dialog]
[Blocker(a=0, r=255,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.4, r=255,g=0, b=0, fadetime=0.03, block=true)]
[CameraShake(duration=0.1, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_knife", volume=1)]
[Blocker(a=0, r=255,g=0, b=0, fadetime=0.2, block=true)]
[Delay(time=0.3)]
[Blocker(a=0, r=255,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.4, r=255,g=0, b=0, fadetime=0.03, block=true)]
[CameraShake(duration=0.1, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_attack_heavy", volume=1)]
[Blocker(a=0, r=255,g=0, b=0, fadetime=0.3, block=true)]
[Delay(time=0.5)]
[Blocker(a=0, r=255,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.4, r=255,g=0, b=0, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_broadswordblood", volume=1)]
[Blocker(a=0, r=255,g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1.5)]
[playsound(key="$bodyfalldown2")]
[charslot(slot = "m", name = "avg_npc_1294_1#2$1", posfrom="0,0", posto="0,-50", afrom=1, ato=0, duration=0.5, isblock=false)]
[Delay(time=1)]
[PlaySound(key="$d_gen_soldiersrun", volume=0.8)]
[Delay(time=2)]
[PlaySound(key="$knifegore", volume=0.8)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_attack_heavy", volume=0.4)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_broadswordblood", volume=0.2)]
[Delay(time=0.8)]
命运没有杀死他。确实。他做到了。他做到了逆转预言。
然后他死在了自己亲手搭建的舞台上。
[dialog]
[stopmusic(fadetime=2)]
[StopSound(channel="sn", fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_victoria",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
维多利亚，伦蒂尼姆
[dialog]
[playMusic(intro="$katzdale_intro", key="$katzdale_loop", volume=0.6)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1297_1#1$1", duration=1.5, isblock=true)]
[delay(time=0.5)]
[charslot]
坐落在伦蒂尼姆中的庞大宫殿群总是过于安静。
特雷西斯对生活在其中的麻木贵族嗤之以鼻，他唯独敬重一批又一批用生命为代价走到自己身前的同胞。
哪怕他们举起的刀，指向的是自己——
[dialog]
[charslot(slot = "m", name = "avg_npc_404_1#8$1")]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1297_1#4$1", posfrom="200,0", posto="-200,0", duration=0.5)]
[delay(time=0.2)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$swordtsing1", volume=1)]
[delay(time=0.2)]
[PlaySound(key="$swordtsing2", volume=1)]
[delay(time=0.2)]
[PlaySound(key="$swordtsing4", volume=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=1.5, block=true)]
[charslot(slot = "r", name = "avg_npc_1297_1#4$1", focus="r")]
[name="特雷西斯"]曼弗雷德，对敌人留情只会害死自己。不要再犯相同的错误。
[charslot(slot = "r", focus="n")]
[name="曼弗雷德"]抱歉，将军......我以为——
[charslot(slot = "r", name = "avg_npc_1297_1#1$1", focus="r")]
[name="特雷西斯"]专心应敌。这些埋伏在我们身边的叛徒恐怕已经准备了很久了。
[name="特雷西斯"]他们拨动了维多利亚人的心弦。现在唯有我们自己能扑灭这场叛乱。
[charslot(slot = "r", name = "avg_npc_1297_1#2$1", focus="r")]
[name="特雷西斯"]*古老的萨卡兹语*——
[dialog]
[charslot]
他轻细的密令声刚落，一道道身影已经无声无息地介入了混乱的现场。
像一阵掠过的风，吹散了倾盆而下的暴雨。
[dialog]
[charslot(slot = "m", name = "avg_npc_1307_1#1$1", duration=1.5, isblock=true)]
[name="弃名死士"]退后。
[dialog]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[charslot(slot = "m", name = "avg_npc_1307_1#1$1", posfrom="0,0", posto="-200,0", afrom=1, ato=0, duration=0.2, isblock=true)]
[delay(time=0.2)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[charslot]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30,

... (全文38444字符)
```

### level_act33side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.6)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
卡兹戴尔地区，巴别塔罗德岛本舰外
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1307_1#1$1", duration=1)]
[Delay(time=0.2)]
[charslot(slot = "l", name = "avg_npc_1307_1#1$1", duration=1, isblock=true)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1307_1#1$1", focus="r")]
[name="决然的刺客"]巴别塔并无防备，如摄政王所料。
[charslot(slot = "l", name = "avg_npc_1307_1#1$1", focus="l")]
[name="谨慎的刺客"]减少动静，提高警惕。
[name="谨慎的刺客"]按原定路线进入，找到魔王。A路线和B路线同样待命。
[charslot(slot = "r", name = "avg_npc_1307_1#1$1", focus="r")]
[name="决然的刺客"]核心战力不存在于这艘船上。他们撤回支援需要时间。
[name="决然的刺客"]巴别塔的护卫也依旧没有反应过来。
[charslot(slot = "l", name = "avg_npc_1307_1#1$1", focus="l")]
[name="谨慎的刺客"]......摄政王殿下赌对了。有敌方的大人物在帮我们。
[name="谨慎的刺客"]全队，即刻登舰。速战速决，减少意外。
[dialog]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = false, fadetime=2, block=true)]
[charslot]
[Background(image="bg_room_2",screenadapt="coverall")]
[PlaySound(key="$factory_low_drone", volume=0.4, loop=true, channel="f")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = false, fadetime=2, block=true)]
[StopSound(channel="f", fadetime=2)]
十分钟前，阿米娅被一阵奇怪的噪音吵醒。
巴别塔一直没有停止过维修和翻新，与她刚来到这个新家时相比，这里已经发生了很大变化。
“也许是可露希尔小姐又在忙前忙后了？”
在阿米娅的房间里，博士为她留下了很多绘本，上面画着她闻所未闻的故事。
她最喜欢的一本，讲述的是一个乘着奇异载具自天空坠向地面的人所经历的冒险。
但她并不喜欢它的结局，那人最终还是修好了载具，要与地上的孩子告别，回到天空。
[dialog]
[charslot(slot = "m", name = "avg_npc_1295_1#5$1", duration=0.5, isblock=true)]
[name="阿米娅"]......好讨厌的声音，博士还没来......
[charslot(slot = "m", name = "avg_npc_1295_1#4$1")]
[name="阿米娅"]特蕾西娅小姐......只好去找特蕾西娅小姐了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5, isblock=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[Background(image="bg_corridor_2",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1295_1#8$1", duration=1.5, isblock=true)]
[name="阿米娅"]唐宁叔叔，您好！您的钳子掉在地上了，给！
[charslot]
[charslot(slot = "m", name = "avg_npc_1308_1#1$1")]
[name="巴别塔成员"]谢谢阿米娅。你要去哪？
[charslot(slot = "m", name = "avg_npc_1295_1#1$1")]
[name="阿米娅"]去议长室找特蕾西娅小姐。对了，您有看到博士吗？
[charslot(slot = "m", name = "avg_npc_1308_1#1$1")]
[name="巴别塔成员"]博士？这几天好像一直没见过，应该是在指挥室指挥作战吧？
[charslot(slot = "m", name = "avg_npc_1295_1#8$1")]
[name="阿米娅"]哦，果然博士还是很忙......再见！
[dialog]
[playsound(key="$rungeneral", volume=1)]
[charslot(duration=1, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_1308_1#1$1")]
[name="巴别塔成员"]阿米娅，跑慢点！舰船上很多地方还在检修呢，别绊着了！
[name="巴别塔成员"]这孩子真是——
[dialog]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[name="巴别塔成员"]呃......
[dialog]
[PlaySound(key="$bodyfalldown2", volume=1)]
[charslot(slot = "m", name = "avg_npc_1308_1#1$1", posfrom="0,0", posto="0,-50", afrom=1, ato=0, duration=0.5, isblock=true)]
[delay(time=1)]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1307_1#1$1", duration=1)]
[charslot(slot = "l", name = "avg_npc_1307_1#1$1", duration=1.5, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_1307_1#1$1", focus="l")]
[name="谨慎的刺客"]解决一个，继续走。
[charslot(slot = "r", name = "avg_npc_1307_1#1$1", focus="r")]
[name="决然的刺客"]内应已经埋伏在各处待命，随时可以配合我们。
[name="决然的刺客"]遇到其他人直接动手，舰上剩下的人都没有威胁。
[dialog]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = false, fadetime=1, block=true)]
[charslot]
[Background(image="49_g10_theresaoffice",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = false, fadetime=1, block=true)]
[PlaySound(key="$doorknockquite", volume=0.5)]
[Delay(time=1.5)]
[name="阿米娅"]特蕾西娅小姐，我带来了我的故事书——
[name="阿米娅"]欸......为什么门关着？
[dialog]
[PlaySound(key="$doorknockquite", volume=1)]
[Delay(time=1.5)]
[name="阿米娅"]特蕾西娅小姐，是我！您在里面吗？
[dialog]
[Delay(time=1)]
[multiline(name="阿米娅")]可露希尔小姐教过我，这样也可以开门......
[PlaySound(key="$d_avg_doorknob", volume=1)]
[Delay(time=1)]
[multiline(name="阿米娅",end=true)]开了！
[dialog]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1295_1#1$1", posfrom="200,0", posto="0,0", duration=2, isblock=true)]
[name="阿米娅"]特蕾西娅小姐——
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1, loop=true, channel="w")]
[StopSound(channel="w", fadetime=1)]
[charslot(slot = "l", name = "avg_npc_1296_1#1$1", duration=1, isblock=true)]
[charslot(slot = "l", name = "avg_npc_1296_1#10$1", focus="l")]
[name="特蕾西娅"]阿米娅，为什么你会在这里？
[charslot(slot = "r", name = "avg_npc_1295_1#7$1", focus="r")]
[name="阿米娅"]我听到了讨厌的声音，离我很近......我有点害怕。
[charslot(slot = "l", name = "avg_npc_1296_1#1$1", focus="l")]
[name="特蕾西娅"]......
[charslot(slot = "l", name = "avg_npc_1296_1#8$1", focus="l")]
[name="特蕾西娅"]我们马上就能回家了。
[charslot(slot = "r", name = "avg_npc_1295_1#7$1", focus="r")]
[name="阿米娅"]您看起来很累......
[charslot(slot = "l", name = "avg_npc_1296_1#8$1", focus="l")]
[name="特蕾西娅"]那阿米娅想陪着我一起工作吗？
[charslot(slot = "l", name = "a

... (全文16183字符)
```

### level_act33side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(key="$monastery_sad_loop", volume=0.6)]
[Background(image="bg_light",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
阿米娅最后记得的事，是她睡在黑色的泡泡里。
特蕾西娅温柔地抱着包裹着她的泡泡。
讲述着一个她已经听过许多次的故事......
[dialog]
[charslot(slot = "m", name = "avg_npc_1296_1#1$1", duration=2, isblock=true)]
[name="特蕾西娅"]在绝望的沙漠里有很多恐怖的影子，他们追逐着不停寻找希望的小布人。
[name="特蕾西娅"]黑袍的影子是最古老最古老的，绝望和悲哀的回声。
[name="特蕾西娅"]一旦被他们抓住，就再也逃不开了。
[charslot(slot = "m", name = "avg_npc_1296_1#8$1")]
[name="特蕾西娅"]在沙漠中，小布人遇到了缀满赤金与宝石的国王，他答应小布人只要原路返回，就给他数不尽的财富。
[name="特蕾西娅"]尽管国王拉扯着他，小布人依旧丢下了诱人的宝石继续前进。
[charslot(slot = "m", name = "avg_npc_1296_1#1$1")]
[name="特蕾西娅"]但很快——
[name="特蕾西娅"]黑袍的影子追上了他。影子不断向他扑去，无穷无尽......
[name="特蕾西娅"]“砰，砰，砰”......
[charslot(slot = "m", name = "avg_npc_1296_1#3$1")]
[name="特蕾西娅"]他只能抽出针和线做的长矛与黑色的影子战斗，最终挡开了影子们的利爪继续向前逃去......
[name="特蕾西娅"]直到逃到一条泪水汇成的大河。没有船只，没有浮萍，小布人只能游过去......
[name="特蕾西娅"]可一沾上泪水，他就越来越沉，直至河底——
[dialog]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1296_1#6$1")]
[name="特蕾西娅"]他失败了。
[charslot]
这就是故事的结局了吗？阿米娅不愿意相信。
也许是特蕾西娅小姐念错了也说不定？
她焦急地想要让特蕾西娅小姐改变结局......
[charslot(slot = "m", name = "avg_npc_1296_1#6$1", focus="n")]
[name="阿米娅"]特蕾西娅小姐......
[charslot(slot = "m", name = "avg_npc_1296_1#1$1")]
[name="特蕾西娅"]......我在。
[charslot(slot = "m", focus="n")]
[name="阿米娅"]我们......能救救小布人吗？
[charslot(slot = "m", name = "avg_npc_1296_1#8$1")]
[name="特蕾西娅"]你想要救他吗？
[charslot(slot = "m", focus="n")]
[name="阿米娅"]想，我......很想很想......
[dialog]
[musicvolume(volume=0.2, fadetime=3)]
[PlaySound(key="$d_avg_underwtr", volume=0, loop=true, channel="un")]
[SoundVolume(volume=1, channel="un",fadetime=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[background]
声音淡去了。
挡住阿米娅视线的泡泡在消散。
特蕾西娅的身影在她的眼前越来越清晰——
[dialog]
[bgeffect(name="$eb_dim_openeye",layer=1)]
[delay(time=1)]
[Dialog]
[Background(image="49_g10_theresaoffice",screenadapt="coverall")]
[StopSound(channel="un", fadetime=4)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0.2, r=0.92, g=0.4, b=0.3, fadetime=3, block=true)]
在眼角的余光中，她看到了躺倒在地面上的黑袍影子们渗出的殷红。
这些人......是谁？他们是什么时候来的？为什么会躺在地上？
阿米娅有太多太多的疑惑想要问特蕾西娅，她努力睁大自己的眼睛......
她看到了白色衣服上沾染的殷红。看到了......特蕾西娅泛红的眼角。
特蕾西娅小姐还好吗？
阿米娅想问问特蕾西娅小姐身上的伤势。
但她发不出声音。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.4)]
[charslot(slot="m", name="avg_npc_1296_1#1$1", duration=2, isblock=true)]
[name="特蕾西娅"]......阿米娅，没事。
[name="特蕾西娅"]我在这呢。那些故事里的坏蛋已经暂时被打倒了。
[dialog]
[charslot(slot="m", focus="n")]
特蕾西娅小姐怎么了？
阿米娅想要拭去特蕾西娅小姐脸上的疲惫。
但她抬不起自己的手。
[dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background]
[Image(image="49_i17", screenadapt="coverall",fadetime=0)]
[ImageTween(xScaleFrom=1, yScaleFrom=1, xScaleTo=1.15, yScaleTo=1.15, duration=40, block=false)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[name="特蕾西娅"]抱歉，我没有能力改变故事的结局。
[name="特蕾西娅"]但是你可以，阿米娅......
[name="特蕾西娅"]你会走上一条艰难的道路。就像试图跨越泪水之河的小布人。
[name="特蕾西娅"]我能够帮上你的，唯有将这顶黑色的冠冕赠与你。
[name="特蕾西娅"]万年的时间，我的族群因为历史的局限性，错误地使用了这顶冠冕。
[name="特蕾西娅"]它被污染，被绑定。但本不该如此。
[name="特蕾西娅"]如果要打破诅咒，打破命运......我需要你的帮助。
[name="特蕾西娅"]你愿意改写结局吗？
阿米娅想要说出“愿意”，但她无法发出声音。
她焦急地点着头，她想，也许至少这样能够帮上特蕾西娅小姐......
能够救她——
[name="特蕾西娅"]虽然我现在剩下的力量能做的不多，但足以将它的权限转移给你。
[name="特蕾西娅"]我为你封存了它的大部分区域，以免无边无际的信息搅乱你的思绪。
[name="特蕾西娅"]......
[name="特蕾西娅"]阿米娅......抱歉，我将这顶冠冕的重量压在了你的身上。
[name="特蕾西娅"]我本以为......我能够陪伴你的日子还有好久好久，陪伴你长大，陪伴你到能勇敢地面对父母的离去，陪伴你到能自己给出回答——
[name="特蕾西娅"]回答你是否愿意替我继续走下去......
[name="特蕾西娅"]但留给我们的时间总是不够，阿米娅。
[name="特蕾西娅"]我如今自私地将我所背负的重担压在了你的身上......
[name="特蕾西娅"]对不起，孩子——
[dialog]
[PlaySound(key="$d_avg_daggerslow", volume=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Image(image="49_i19", screenadapt="coverall", xScale=1.05, yScale=1.05, fadetime=0)]
[ImageTween(xScaleFrom=1.05, yScaleFrom=1.05, xScaleTo=1, yScaleTo=1, duration=15, block=false)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
阿米娅试图喊出声，但她却无法张开口，甚至无法挪动自己的四肢。
黑色的剑刃似乎穿透了自己的胸口。
她理应感受到痛苦。但那柄剑留下的——
唯有温热。充满期盼的温热。
[name="特蕾西娅"]阿米娅，它是希望，亦是痛苦。
[name="特蕾西娅"]你会困惑，会犹疑。
[name="特蕾西娅"]但请相信，凯尔希医生会永远站在你的身边。
[name="特蕾西娅"]她会帮助你去探究，去重新接近存续的秘密。
[name="特蕾西娅"]你能克服的，对吧，阿米娅......
[name="特蕾西娅"]你一直都是一个坚强到令我都惊讶的孩子。
[name="特蕾西娅"]呼......
[name="特蕾西娅"]我真的很累了。
[name="特蕾西娅"]谢谢你，阿米娅，这些日子，是你将快乐带给了我。
[name="特蕾西娅"]现在，先暂且休息片刻吧。睡吧......
安心地睡吧。
我会一直陪着你。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[Background(image="49_g10_theresaoffice",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$dooropenquite", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
......
特蕾西娅听到了熟悉的声音。
[dialog]
[playsound(key="$rungeneral", volume=1)]
[charslot(slot="m", name="avg_npc_048", duration=1, isblock=true)]
[name="博士"]......阿米娅！
[charslot]
特蕾西娅并未抬头看向到来的人。
王冠抽离，又重聚。而她的气息却愈发微弱。
[dialog]
[name="特蕾西娅"]......博士。你何必来到这里呢。
[charslot(slot="m", name="avg_npc_048")]
[name="博士"]......
[charslot(slot="m", focus="n")]
[name="特蕾西娅"]我感到了......你的情感。我看见了，你的过去。
[name="特蕾西娅"]可你本可以待在别处，静待我的死亡到来。你知道这一次，我不会逃离，也不会撤退。
[name="特蕾西娅"]你来，是为了找阿米娅吗？还是为了......
[dialog]
[PlaySound(key="$d_gen_soldiersrun", volume=1)]
[charslot(duration=1)]
[delay(time=1.5)]
特蕾西娅已经不用听那个人的回答。
在那人的身后，潮水般的刺客不断从阴影中涌来，奔向了特蕾西娅——
[charslot(slot = "m", name = "avg_npc_1296_1#1$1")]
[name="特蕾西娅"]这就是你的答案吧，博士......
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=2)]
[charslot]
[Background]
[Image]
```

### level_act33side_10_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$ghosthunter_intro", key="$ghosthunter_loop", volume=0.6)]
[Background(image="49_g10_theresaoffice",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
特蕾西娅很庆幸阿米娅睡着了。
阿米娅没有看见博士的背叛，也没有看见特蕾西娅最后的悲伤。
在特蕾西娅将议长室中的最后一名刺客抹除的同时，那顶黑色的王冠终于安稳地传递到了阿米娅的手中。
[dialog]
[charslot(slot = "m", name = "avg_npc_1296_1#9$1", duration=1.5, isblock=true)]
[name="特蕾西娅"]没事了，阿米娅，没事了......
[name="特蕾西娅"]已经结束了。
[charslot]
她没有看向那个已经僵直在原地的人，只是轻轻拍了拍怀中孩子的后背，在那张稚嫩的小脸上，落下一吻。
[dialog]
[charslot(slot="m", name="avg_npc_048", duration=1.5, isblock=true)]
[Delay(time=0.5)]
[name="博士"]......
[name="博士"]特蕾西娅。我没办法放弃亿万生命和万年时间才换来的机会。
[name="博士"]我没办法允许你们突破源石的规划。没办法允许你......将这片大地变成一个美好但短暂的梦。
[charslot(slot = "m", name = "avg_npc_1296_1#4$1")]
[name="特蕾西娅"]所以，你伤害了阿米娅。
[charslot(slot="m", name="avg_npc_048")]
[name="博士"]......
[name="博士"]......既然魔王已看过了我的记忆，那我们多说无益。
[name="博士"]你恨我吗？
[charslot(slot = "m", name = "avg_npc_1296_1#4$1")]
[name="特蕾西娅"]你伤害了阿米娅，你也即将伤害凯尔希，和那些信任你的将士。
[charslot(slot = "m", name = "avg_npc_1296_1#5$1")]
[name="特蕾西娅"]这是你对待如今这些生命的方式吗？
[charslot(slot="m", name="avg_npc_048")]
[name="博士"]我会尽全力保证他们不在接下来的冲突中丧命。这也是特雷西斯给我的承诺。
[name="博士"]只要......你的死亡。
[charslot(slot = "m", name = "avg_npc_1296_1#1$1")]
[name="特蕾西娅"]......博士，你是出于此刻的愧疚而来到我面前的吗？
[charslot(slot="m", name="avg_npc_048")]
[name="博士"]比起我所做的事情，愧疚的分量......太轻。
[name="博士"]在凯尔希都不熟知的年代里，我们做出了太多选择。
[name="博士"]我只是......
[charslot(slot = "m", name = "avg_npc_1296_1#10$1")]
[name="特蕾西娅"]等阿米娅长大后，若她还记得我，若她问起我，你是否会如实告知她......我是怎样离去？
[charslot(slot="m", name="avg_npc_048")]
[name="博士"]不会。
[name="博士"]我会帮助他们寻找另一种生活。
[charslot(slot = "m", name = "avg_npc_1296_1#10$1")]
[name="特蕾西娅"]寻找在源石毁灭泰拉之前最后的安稳？
[charslot(slot="m", name="avg_npc_048")]
[name="博士"]......抱歉。这无法改变。
[charslot(slot = "m", name = "avg_npc_1296_1#1$1")]
[name="特蕾西娅"]你明知道这是无用功......你却仍旧，想治好阿米娅的病。
[name="特蕾西娅"]哪怕在不远的未来，阿米娅的家人、家乡，和你们未来可能建立起联系的那些人和事，都将成为不变的源石。
[name="特蕾西娅"]你也不忍看着眼前的孩子受苦。
[charslot(slot = "m", name = "avg_npc_1296_1#8$1")]
[name="特蕾西娅"]这是你的真心。是你的纯洁。是你的本性。
[charslot(slot="m", name="avg_npc_048")]
[name="博士"]......
[charslot(slot = "m", name = "avg_npc_1296_1#9$1")]
[name="特蕾西娅"]我其实......很欣慰，博士。
[name="特蕾西娅"]我很高兴，凯尔希愿意相信的那个你，愿意相信我们的那个你，是真实存在的。
[charslot(slot = "m", name = "avg_npc_1296_1#8$1")]
[name="特蕾西娅"]你......源石的缔造者......{@nickname}。你是毁去一切的毒，也可以是一切的解药。
[charslot(slot="m", name="avg_npc_048")]
[name="博士"]......什么？
[dialog]
[charslot]
[PlaySound(key="$d_avg_clothtrailground", volume=1)]
看见特蕾西娅强撑着站起，将双手伸向自己，博士本能地想要后退。
博士却发现自己的身体无法移动分毫，博士发现自己的悲伤远胜自己强撑的理性。
只好任由特蕾西娅触碰面罩之下的面庞。
[dialog]
[charslot(slot = "m", name = "avg_npc_1296_1#8$1", duration=1, isblock=true)]
[name="特蕾西娅"]你在落泪，博士......
[name="特蕾西娅"]是啊，你就是这样的人。你明知道自身的脆弱，明知道哪怕是此时的我，也对你有致命的威胁......你还是来了。
[name="特蕾西娅"]所以，我还是......愿意相信你。
[name="特蕾西娅"]相信原本的你。
[name="特蕾西娅"]相信那个，将雨露和艳阳带给我们的{@nickname}。
[dialog]
[PlaySound(key="$d_avg_magic_1", volume=0.5)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=0.5, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1.5, block=true)]
[Delay(time=0.5)] 
[PlaySound(key="$d_avg_magic_5", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=1, block=true)]
[charslot]
[Blocker(a=0, r=255, g=255, b=255, fadetime=2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[curtain(direction = 0,fillfrom = 0.5,fillto = 0.15, fadetime=0.01)]
[curtain(direction = 4,fillfrom = 0.5,fillto = 0.15, fadetime=0.01)]
[Background(image="49_g10_theresaoffice",screenadapt="coverall", xScale=1.5, yScale=1.5, y=-300)]
[BackgroundTween(xFrom=-100, xTo=100, duration=60,ease="OutQuad",block=false)]
[charslot(slot = "m", name = "avg_npc_048")]
[charslot(slot = "m", action="zoom", poszoom = "0.5,0.5", scale=1.8,duration = 0)]
[charslot(slot = "m", posfrom="-200,-380", posto="-100,-380", afrom=1, ato=1, duration=60)]
[focusout(type="bg", id="49_g10_theresaoffice", from=0, to=1, duration=1, block=false)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
这一张脸，既熟悉又陌生。特蕾西娅清楚它的样子。
她从未有机会如此直观地从上面捕捉到情绪。
她微笑着伸出手指，眼前的景象犹如布匹一般被撕裂开。
随后，她缓缓抽出自裂口处松脱的丝线，残余的画面也散解开来，博士的记忆不断消散。
[dialog]
[charslot(duration=2)]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_magicwarmthy", volume=0, loop=true, channel="wa")]
[SoundVolume(volume=1, channel="wa",fadetime=2)]
[Blocker(a=0.4, r=255, g=255, b=255, fadetime=2, block=true)]
[Delay(time=1)]
特蕾西娅头也不回地继续深入，继续将每一寸组成博士灵魂的记忆都拆解为一团团苍白混乱的断线。
像是很久很久之前的夜晚，幼小的她在特雷西斯身旁自学缝纫那般。
记忆消散殆尽，灵魂只剩下了最后一枚碎片。
而记忆的尽头处有一个背影。特蕾西娅对那个背影熟悉而又陌生。
那是博士，也不是博士。
[dialog]
[musicvolume(volume=0.6, fadetime=1)]
[PlaySound(key="$d_avg_humanchange", volume=0.4)]
[delay(time=0.4)]
[curtain(direction = 0,fillfrom = 0.15,fillto = 0, fadetime=0.5)]
[curtain(direction = 4,fillfrom = 0.15,fillto = 0, fadetime=0.5)]
[Blocker(a=0.4, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[Background(image="bg_white", screenadapt="coverall")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Subtitle(text="<color=#000000>你在对我做什么，特蕾西娅？</color>", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Background(image="bg_light",screenadapt="coverall", xScale=1.5, yScale=1.5, y=-100, x=-150, fadetime=2)]
[charslot(slot = "r", name = "avg_npc_1296_1#8$1", duration=2)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=1.8,duration = 0)]
[charslot(slot = "r", posfrom="0,-380", posto="100,-380", duration=60)]
[delay(time=3)]
[name="特蕾西娅"]虽然已经是最后了，但我突然想卖个关子，你可不要怪我呀，博士。
[name="特蕾西娅"]我会对你说......
[dialog]
[delay(time=1)]
[name="特蕾西娅"]“去找到你自己吧。”
[dialog]
[StopSound(channel="wa", fadetime=2)

... (全文6307字符)
```

### level_act33side_10_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=2, block=true)]
[charslot]
[PlayMusic(key="$desolate_loop", volume=0.6)]
[Image(image="49_i21_2", screenadapt="coverall", xScale=1.15, yScale=1.15, fadetime=0)]
[ImageTween(xScaleFrom=1.15, yScaleFrom=1.15, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=4, block=true)]
[Delay(time=1)]
特蕾西娅拉着眼前之人的手，就像他们的第一次见面。
她静静与那双眼睛对视，看到其中不停变换着情绪，最终，只留下空洞一片。
她知道，最后的记忆已经抹去，灵魂已经纯净。
[name="特蕾西娅"]你的记忆已经死去，你的灵魂会重生......
[name="特蕾西娅"]真是可怕的伎俩......
[name="特蕾西娅"]可那些人低估了你的善良，低估了你对胜利的渴望。那些人低估了我们，低估了泰拉坚忍至今的起源。
[name="特蕾西娅"]博士，姑且再让我最后一次如此称呼你......
[name="特蕾西娅"]这是我对你小小的报复。
[name="特蕾西娅"]也是我对你......最后的馈赠。
[name="特蕾西娅"]记忆从不塑造你自己。以你最本来的面目......
[name="特蕾西娅"]......重新生活在......大地之上吧。去看看这个世界，去感受生活的喜怒哀乐，去结识形形色色的泰拉人民......
[name="特蕾西娅"]也许......你的旅程会从苦难中开始，总是离不开这片大地昏沉的月影，可你总能......见到太阳升起。
[name="特蕾西娅"]然后，我相信，你会重新得出一个答案。得出真正属于你的答案。
[name="特蕾西娅"]那一定......和凯尔希，和我曾听到的那段呢喃一样......
[name="特蕾西娅"]令人热泪盈眶吧。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[image]
[charslot]
[Background(image="49_g10_theresaoffice",screenadapt="coverall")]
[Delay(time=1)]
[focusout(type="bg", id="49_g10_theresaoffice", from=0, to=1, duration=3, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
生命在流逝。 
她的耳边逐渐响起了来自远方的挽歌。对了，菈玛莲曾与她设下连接。
特蕾西娅自己的气息在逐渐微弱......但她也感受到了前所未有的轻松。
她尽力将阿米娅护在怀中，保护着。阿米娅的心跳令她安心。
[name="特蕾西娅"]我......我有点累了，捧住那顶冠冕真的很累。
[name="特蕾西娅"]累了就得休息，对吧，阿米娅？
[name="特蕾西娅"]我曾想过......
[name="特蕾西娅"]也许有天......我们会一起让这片大地上的每一个人，都能平静入梦。
[name="特蕾西娅"]虽然很遥远，但也许，你会替我看到那一天......
[name="特蕾西娅"]阿米娅，当你醒来......
[dialog]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[background]
[PlaySound(key="$d_avg_femalebreathesoft", volume=0, loop=true, channel="fe")]
[SoundVolume(volume=1, channel="fe",fadetime=2)]
[Image(image="49_i01", screenadapt="coverall", xScale=1.05, yScale=1.05, fadetime=0)]
[ImageTween(xScaleFrom=1.05, yScaleFrom=1.05, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[name="特蕾西娅"]......你就要继续前行。
[name="特蕾西娅"]呼——好累......
[name="特蕾西娅"]不，她还没有来......
[SoundVolume(volume=0.5, channel="fe",fadetime=2)]
她只有最后一丝珍贵的力气了。
她有必须要等的人。
万幸，她已经听到了那人赶来的声音。
[dialog]
[delay(time=1)]
终于，哪怕无力再睁开眼，但她也知道——
那人回来了——
凯尔希......
[StopSound(channel="fe", fadetime=2)]
凯尔希。
[dialog]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[focusout(type="bg", id="49_g10_theresaoffice", from=1, to=0, duration=0.1, block=false)]
[delay(time=1)]
[Background(image="49_g10_theresaoffice",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=1.5)]
[charslot(slot="m", name="avg_003_kalts_1#9$1", duration=1, isblock=true)]
[name="凯尔希"]......
[name="凯尔希"]特蕾西娅......
[name="凯尔希"]阿米娅......博士......
[charslot(slot="m", name="avg_003_kalts_1#8$1")]
[name="凯尔希"]我明知道这样的可能性始终存在......为什么......
[name="凯尔希"]我应该留下，是我......
[name="凯尔希"]......
[charslot(slot="m", name="avg_003_kalts_1#9$1")]
[name="凯尔希"]特蕾......西娅。
[name="凯尔希"]我......我们本可以......
[dialog]
[delay(time=1.5)]
[charslot(slot="m", name="avg_003_kalts_1#8$1")]
[name="凯尔希"]特蕾西娅......确认死......死亡。
[charslot(slot="m", name="avg_003_kalts_1#5$1")]
[name="凯尔希"]Mon3tr，听我命令......
[name="凯尔希"]准备......应对后续的袭击。
[name="凯尔希"]博士和阿米娅......不能再出事......不能！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m", name="avg_003_kalts_1#7$1")]
[name="凯尔希"]Mon3tr——！
[charslot(slot="m", focus="n")]
[name="？？？"]凯尔希......
[name="？？？"]凯尔希。
[charslot(slot="m", name="avg_003_kalts_1#4$1")]
[name="凯尔希"]——！
[dialog]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[background]
[Image(image="49_i18", screenadapt="coverall", fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
阿米娅睁开了眼，瞳孔中隐隐现出粉色的菱形。
特蕾西娅依旧紧闭双眼。
但凯尔希知道。
这就是她。
[name="“阿米娅”"]凯尔希......我一直在等你。
[name="凯尔希"]特蕾西娅！我——
[musicvolume(volume=0, fadetime=6)]
[name="“阿米娅”"]没事的，没事的，凯尔希。
[name="“阿米娅”"]听我说——
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[background]
[Image(image="49_i13", screenadapt="coverall", xScale=1.1, yScale=1.1, fadetime=0)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[PlaySound(key="$d_avg_magicrelievey", volume=0, loop=true, channel="ma")]
[SoundVolume(volume=0.8, channel="ma",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="“阿米娅”"]我已经死去。
[name="“阿米娅”"]你现在看到的，是我寄留于王冠中的意识，借由这个孩子的身体与你告别。
[name="“阿米娅”"]凯尔希，告诉我，你是否将那面巴别塔旗帜升上了卡兹戴尔的天空？
[name="凯尔希"]我将它送回卡兹戴尔了，我看着它升上了高空......
[name="“阿米娅”"]谢谢。
[name="凯尔希"]我回来得太晚了，我明知道有这种可能......
[name="“阿米娅”"]不要为此自责，凯尔希，你有自己的任务需要完成。
[name="“阿米娅”"]而且在最后......我还是等到你了，这已经足够。
[name="凯尔希"]......
[name="凯尔希"]......我们，没有更多时间告别了吗？
[name="“阿米娅”"]对不起，凯尔希......
[name="凯尔希"]......我明白。
[name="“阿米娅”"]请不要责怪自己，凯尔希。
[name="“阿米娅”"]我们曾信任过博士，我希望你能在未来继续沿着我们的道路前进。
[name="“阿米娅”"]凯尔希，不必再为此而疑虑。
[name="“阿米娅”"]我杀死了他，也救下了他。
[name="“阿米娅”"]请将他送回他应在的地方，如果他还能醒来......
[name="“阿米娅”"]指引他，他会带领我们走到我们道路的终点——
[name="“阿米娅”"]我深信不疑。
[dialog]
[StopSound(channel="ma", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[image]
[Background(image="49_g10_theresaoffice",screenadapt="coverall")]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1295_1#11$1")]
[charslot(slot = "l", name = "avg_003_kalts_1#4$1")]
[musicvolume(volume=0.6, fadetime=2)]
[Bloc

... (全文21864字符)
```

### level_act33side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Image(image="avg_5_7_shining", fadetime=0, screenadapt="coverall")]
[playsound(key="$d_avg_snowstormlp", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.6, fadetime=3,channel="bgs")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
男孩在梦中哭泣，女孩将男孩裹在自己抵挡风雪的斗篷中，为他拭去了眼泪。
冰冷。断续。呼啸。
巨人轻轻讲述一部遥远的史诗......
她的声音穿越了风雪的裂隙。
众魂的呼唤为其和音，男孩的呜咽敲打着节拍。
女孩在梦中的酷寒中微微喘息，她捂住了男孩的眼睛，然后闭上了眼。
千年前的歌谣仍在他们眼前演绎。
[dialog]
[Delay(time=1)]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Sticker(id="st1", text="......", x=300,y=370, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st1")]
[Delay(time=0.3)]
[Sticker(id="st2", text="我见远方的军队袭来家园，", x=300,y=370, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st3", text="从河谷到山岗，从高山到平原。", x=300,y=410, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st2")]
[Sticker(id="st3")]
[Delay(time=0.3)]
[Sticker(id="st4", text="君王授首，众魂恸哭。", x=300,y=370, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st4")]
[Delay(time=0.3)]
[Sticker(id="st5", text="我见六位英雄跨过魔王尸骸，", x=300,y=370, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st6", text="吹响号角，率万部回击。", x=300,y=410, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st5")]
[Sticker(id="st6")]
[Delay(time=0.3)]
[Sticker(id="st7", text="可惜，可叹，烈怒火光汹涌澎湃，", x=300,y=370, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st8", text="流浪者的城市灭于一旦。", x=300,y=410, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st7",duration=1)]
[Sticker(id="st8",duration=1)]
[Delay(time=1.5)]
[Sticker(id="st1", text="我见黑色的冠冕浮现，", x=300,y=370, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st2", text="荣耀、恩典与救济悉数归于双子。", x=300,y=410, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st1")]
[Sticker(id="st2")]
[Delay(time=0.3)]
[Sticker(id="st3", text="裂隙扩散，新诞的一切尽数背叛。", x=300,y=370, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st3")]
[Delay(time=0.3)]
[Sticker(id="st4", text="我见风暴降临，风暴中央的，", x=300,y=370, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st5", text="乃是弑君之刀剑，诛王之枪矛，", x=300,y=410, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st6", text="终结传说皆是按照公义。", x=300,y=450, alignment="center", size=24, delay=0.04, width=700)]
[Sticker(id="st4",duration=1)]
[Sticker(id="st5",duration=1)]
[Sticker(id="st6",duration=1)]
[StopSound(channel="bgs", fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
“这就是此章的结尾。”
巨人淡入了梦中的风雪中，将孩子抛弃在身后。
男孩渐渐不再听到自己啼哭的声音。
他醒了。
[dialog]
[image]
[Background(image="bg_thundercloud",screenadapt="coverall",xScale=1, yScale=1,x=0)]
[BackgroundTween(xFrom=0, xTo=20,xScaleFrom=1, yScaleFrom=1, xScaleTo=1.1, yScaleTo=1.1, duration=30, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
1094年夏
卡兹戴尔地区，荒废小镇外
[name="？？？"]这就是此章的结尾，阿斯卡纶。我的故事说完了。
[name="？？？"]这是我的族人......独眼巨人深入北境前，最后望向卡兹戴尔的所见。
[name="？？？"]这一章是已然逝去的未知历史，是尚未临近的可能未来，抑或是毫无意义的呓语？
[name="？？？"]近千年来，无人知晓......
[name="？？？"]直到他们出现，命运的湍流开始岔进更窄、更确定的河道......
[name="？？？"]现在，她所见的命运，已经近在眼前。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="bg_laccolith",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_4132_ascln_1#1$1",duration=1.5)]
[delay(time=2)]
[name="阿斯卡纶"]......
[name="阿斯卡纶"]我不关心。
[Dialog]
[charslot(slot="r",name="avg_npc_1294_1#2$1",duration=1)]
[delay(time=2)]
[charslot(slot = "right", focus = "right")]
[name="“疤眼”"]咳，难得你有耐心听我说完。
[charslot(slot = "m", focus = "n")]
红色的鲜血慢慢沿着他的面具下沿滑落到了他的胸口。
阿斯卡纶微微眯眼，他已走投无路。
[charslot(slot="l",name="avg_4132_ascln_1#1$1",focus = "l")]
[name="阿斯卡纶"]你会死，所以我给你最后的尊重。
[charslot(slot = "right", focus = "right")]
[name="“疤眼”"]咳。呵。
[name="“疤眼”"]从我们认识开始，你从未把那些个预言放在心上，对吧？
[charslot(slot="l",name="avg_4132_ascln_1#3$1",focus = "l")]
[name="阿斯卡纶"]......
[charslot(slot = "right", focus = "right")]
[name="“疤眼”"]那......你永远不会理解一个贪婪的人对控制命运的渴望。
[charslot(slot="l",name="avg_4132_ascln_1#1$1",focus = "l")]
[name="阿斯卡纶"]死前少废话。
[charslot(slot = "right", focus = "right")]
[name="“疤眼”"]我知道你急着去和巴别塔那些人会合，但现在还没到你走的时候。你看，天灾快到了。
[name="“疤眼”"]啊......我倒开始好奇了。
[name="“疤眼”"]你在风暴之中，找到了什么？
[charslot(slot="l",name="avg_4132_ascln_1#4$1",focus = "l")]
[name="阿斯卡纶"]让开。
[charslot(slot = "right", focus = "right")]
[name="“疤眼”"]委托必须完成，这是我自己在疤痕商场定下的规矩。
[name="“疤眼”"]无论生——
[dialog]
[charslot(slot="l",name="avg_4132_ascln_1#4$1")]
[PlaySound(key="$d_avg_clothmovementsp")] 
[charslot(slot = "l",posfrom = "0,0", posto = "200,0",duration = 0.3,afrom=1,ato=0)]
[delay(time=0.31)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30,vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_cnstrctnck")] 
[charslot(slot = "right",posfrom = "0,0", posto = "-200,0",duration = 0.3)]
[delay(time=0.2)]
[charslot(slot ="r", action="shake", power=10, times=50, duration=0.4)]
[charslot(slot = "right", focus = "right")]
[name="“疤眼”"]呃！
[charslot]
[Blocker(a=0.15, r=1, g=1, b=1, fadetime=3, block=false)]
阿斯卡纶的身形在他的背后消失，同一时间，薄暮般的雾气已经绕紧巨人的脖颈，将他的身躯高悬于危崖之外。
[dialog]
[charslot(slot = "m",name="avg_4132_ascln_1#1$1",duration = 0.5)]
[delay(time=1)]
[name="阿斯卡纶"]那你有看到过自己的结局吗？
[charslot(slot="m",name="avg_npc_1294_1#2$1")]
[name="“疤眼”"]......我不在乎预言，和你一样，哈。
[name="“疤眼”"]但事实就是，我们都逃不开命运。你不想挣扎吗？凭什么？为什么？怎么能够？
[name="“疤眼”"]不要忘了，预言中也有你的一席之地——
[charslot]
呜咽。风暴。
哀婉的吟唱在他们的耳畔响起，来自女妖河谷的挽歌掠过地平，卷入风暴中央。
阿斯卡纶的身体不由自主地战栗着，她浑身冰凉。
一阵无法诉说的刺痛从她的耳后一路激荡到脚底。
没有名字的挽歌，不祥的预兆。
[charslot(slot = "m",name="avg_4132_ascln_1#7$1")]
[name="阿斯卡纶"]......
[charslot(slot="m",name="avg_npc_1294_1#2$1")]
[name="“疤眼”"]别了......卡兹戴尔。
[charslot]
阿斯卡纶听到了一声叹息。
[PlaySound(key="$d_avg_cnstrctnck")] 
她的手越握越紧，直到“疤眼”的喉咙无法发出一丝轻微的

... (全文18165字符)
```


> 本章节共38个脚本文件，此处展示前30个。

## 统计

- 总字符数：437641
- 对话行数：3289


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
