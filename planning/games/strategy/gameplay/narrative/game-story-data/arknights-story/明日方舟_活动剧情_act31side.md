# 明日方舟 · 活动剧情 · act31side（27段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act31side」完整剧情脚本（27个文件，3038行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act31side
- 脚本文件数：27

### level_act31side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="47_g7_fieldhouse",screenadapt="coverall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
三个月前
[Dialog]
[charslot(slot="m",name="avg_npc_1249_1#1$1",duration=0.5)]
[Delay(time=0.7)]
[charslot(slot="m",name="avg_npc_1249_1#1$1",focus="m")]
[name="惊奇的职农"]什么......？！手上这条断了的是人纹不是地纹，意思是我不会有什么大病大灾，其实是脑子出了问题？
[charslot(slot="m",name="avg_npc_1250_1#1$1",focus="m")]
[name="快乐的职农"]哈哈哈哈，都说了那棵核桃树就是给你种的，赶快去施肥吧，迟了可不好了！
[charslot(slot="m",name="avg_2025_shu_1#9$1",focus="m")]
[name="黍"]也不是这么说，这道断纹只是代表着你大概在二十出头的年纪，会遇到一个很困难的抉择。
[name="黍"]可是哪有十全十美的出路呢，顺其自然吧。你看，之后的纹路不就平整多了？
[charslot(slot="m",name="avg_npc_1249_1#1$1",focus="m")]
[name="惊奇的职农"]准！真准！
[name="惊奇的职农"]我二十三岁的时候，老家的农田被天灾毁了，当时我实在不知道去移动城市能讨到什么生计。
[name="惊奇的职农"]现在跟着大伙来到大荒城研究庄稼，干回老本行了，不也活得挺好的？
[charslot(slot="m",name="avg_npc_1250_1#1$1",focus="m")]
[name="快乐的职农"]还有这种事......
[charslot(slot="m",name="avg_2025_shu_1#9$1",focus="m")]
[name="黍"]哪有人真的能预测命数呢，不过是给发生的事找个理由罢了。
[charslot(slot="m",name="avg_npc_1249_1#1$1",focus="m")]
[name="惊奇的职农"]之前只知道天师府的天师神通广大，没想到还懂得这么多......
[name="惊奇的职农"]黍姑娘，您这么年轻就已经是这里天师府的资深授业天师了？
[charslot(slot="m",name="avg_2025_shu_1#10$1",focus="m")]
[name="黍"]闻道有先后，只是先学到了一些知识，再把它转述给更多人罢了。
[charslot(slot="m",name="avg_npc_1250_1#1$1",focus="m")]
[name="快乐的职农"]了不起，了不起，不过......
[name="快乐的职农"]黍姑娘，我看那边有个年轻小伙子盯着你看半天了......是你的熟人？
[charslot(slot="m",name="avg_2025_shu_1#1$1",focus="m")]
[name="黍"]嗯......
[Dialog]
[Delay(time=1)]
[charslot(slot="m",name="avg_2025_shu_1#2$1",focus="m")]
[name="黍"]是位贵客。抱歉，我们改天再聊吧。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1249_1#1$1",focus="all")]
[charslot(slot="r",name="avg_npc_1250_1#1$1",focus="all")]
[Delay(time=0.2)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[PlaySound(key="$d_avg_walk_stage", volume=1,loop="false", channel="ww")]
[stopsound(fadetime=2, channel="ww")]
[charslot(duration=1)]
[Delay(time=3)]
[Dialog]
[charslot(slot="m",name="avg_4121_zuole_1#1$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4121_zuole_1#1$1",focus="m")]
[name="左乐"]大炎司岁台秉烛人，左乐，奉命前来监管大荒城建设以及岁兽相关事务。
[name="左乐"]我不会限制黍小姐的日常活动，但希望黍小姐近日不要离开大荒城。
[name="左乐"]还请黍小姐配合。
[charslot(slot="m",name="avg_2025_shu_1#14$1",focus="m")]
[name="黍"]哦，之前听说要新来一位秉烛人，原来就是你呀。
[charslot(slot="m",name="avg_4121_zuole_1#1$1",focus="m")]
[name="左乐"]是。
[name="左乐"]只是司岁台例行的检查，并不会妨碍黍小姐的农业研究，黍小姐只要专心原本的事务，不必担——
[charslot(slot="m",name="avg_2025_shu_1#13$1",focus="m")]
[name="黍"]怎么看上去这么年轻，今年成年了吗？
[charslot(slot="m",name="avg_4121_zuole_1#6$1",focus="m")]
[name="左乐"]......什么？
[charslot(slot="m",name="avg_2025_shu_1#9$1",focus="m")]
[name="黍"]这儿地方偏远，来的路上还顺利吗？有没有遇到歹徒刁难？
[charslot(slot="m",name="avg_4121_zuole_1#2$1",focus="m")]
[name="左乐"]我还不至于被几个剪径贼难为住。
[charslot(slot="m",name="avg_4121_zuole_1#1$1",focus="m")]
[name="左乐"]以及，关于此处十二楼五城的修建，司岁台支持各位与炎国工部共同施行、合作共赢，希望各位能够与诸位天师友好相处，少生事端。
[name="左乐"]除此之外，还有一些事情需要......
[charslot(slot="m",name="avg_2025_shu_1#9$1",focus="m")]
[name="黍"]对了，平时活动的话，这里田间可以随便走，小心别踩到庄稼就行，但要是去工厂那边恐怕还是要提前和天师他们打招呼。
[charslot(slot="m",name="avg_4121_zuole_1#10$1",focus="m")]
[name="左乐"]黍小姐......工作范围，我还是清楚的。我还有......
[charslot(slot="m",name="avg_2025_shu_1#9$1",focus="m")]
[name="黍"]上一个秉烛人在这里住过的屋子是那一间，平时生活用的物件已经换过新的，你可以直接用。
[charslot(slot="m",name="avg_4121_zuole_1#10$1",focus="m")]
[name="左乐"]我......
[charslot(slot="m",name="avg_2025_shu_1#9$1",focus="m")]
[name="黍"]嗯，就是这些了，你还有什么问题吗？
[charslot(slot="m",name="avg_4121_zuole_1#10$1",focus="m")]
[name="左乐"]没......没有了。
[charslot(slot="m",name="avg_2025_shu_1#10$1",focus="m")]
[name="黍"]好，田间要忙的事还有不少，我就不多招呼你啦。
[name="黍"]要是还遇到什么困难，开口和周围乡亲打招呼就行，这里的人都好客，不会让你为难的。
[charslot(slot="m",name="avg_4121_zuole_1#10$1",focus="m")]
[name="左乐"]......
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="47_g7_fieldhouse", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_4121_zuole_1#1$1")]
[delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="r",name="avg_4122_grabds_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="r",name="avg_4122_grabds_1#1$1",focus="r")]
[name="顽皮的少女"]喂！
[charslot(slot="l",name="avg_4121_zuole_1#1$1",focus="l")]
[name="左乐"]......
[charslot(slot="r",name="avg_4122_grabds_1#1$1",focus="r")]
[name="顽皮的少女"]喂！
[charslot(slot="l",name="avg_4121_zuole_1#2$1",focus="l")]
[name="左乐"]不好意思，这位姑娘，我有公务——
[charslot(slot="r",name="avg_4122_grabds_1#1$1",focus="r")]
[name="顽皮的少女"]喏。
[charslot(slot="l",name="avg_4121_zuole_1#10$1",focus="l")]
[name="左乐"]饭盒？这是什么意思？
[charslot(slot="r",name="avg_4122_grabds_1#9$1",focus="r")]
[name="顽皮的少女"]饿了吧。
[charslot(slot="r",name="avg_4122_grabds_1#10$1",focus="r")]
[name="顽皮的少女"]你在这一动不动站了一整天，看上去呆呆的，都不知道自己找饭吃，像个稻草人！
[charslot(slot="l",name="avg_4121_zuole_1#6$1",focus="l")]
[name="左乐"]多......多谢。
[Dialog]
[charslot(slot="l",name="avg_4121_zuole_1#9$1",focus="l")]
[delay(time=0.5)]
[PlaySound(key="$d_avg_dishes",volume=0.6)]
[delay(time=2)]
[charslot(slot="l",name="avg_4121_zuole_1#9$1",focus="r")]
[charslot(slot="r",name="avg_4122_grabds_1#2$1",focus="r")]
[name="顽皮的少女"]好吃吗？
[charslot(slot="l",name="avg_4121_zuole_1#9$1",focus="l")]
[name="左乐"]非常可口......
[charslot(slot="r",name="avg_4122_grabds_1#6$1",focus="r")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="顽皮的少女"]我说，你就准备白吃吗？
[charslot(slot="l",name="avg_4121_zuole_1#10$1",focus="l")]
[charslot(slot = "l", action="shake",random=true, power=5, times=70,duration=0.3,focus="l")]
[name="左乐"]咳咳咳咳......！
[Dialog]
[charslot]
[delay(time=0.2)]

... (全文26560字符)
```

### level_act31side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="35_g7_zuosroom",screenadapt="coverall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_4121_zuole_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_788_1#2$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="l",name="avg_4121_zuole_1#1$1",focus="l")]
[name="左乐"]将军，这是近几日追查山海众以及应对天灾的任务报告，还有......在事件中我自己的检讨。
[charslot(slot="l",name="avg_4121_zuole_1#7$1",focus="l")]
[name="左乐"]很惭愧，让父亲失望了......
[charslot(slot="r",name="avg_npc_788_1#2$1",focus="r")]
[name="左宣辽"]......
[charslot(slot="l",name="avg_4121_zuole_1#7$1",focus="l")]
[name="左乐"]接下来我会——
[charslot(slot="r",name="avg_npc_788_1#8$1",focus="r")]
[name="左宣辽"]不必了。
[name="左宣辽"]玉门归京的后续事务，你不用参与。
[charslot(slot="l",name="avg_4121_zuole_1#6$1",focus="l")]
[name="左乐"]这......
[name="左乐"]将军是让我停职反省？
[charslot(slot="r",name="avg_npc_788_1#1$1",focus="r")]
[name="左宣辽"]我无权干预司岁台任命，但身为玉门守将，我可以决定让谁来参与玉门的军事部署。
[name="左宣辽"]离开玉门后，你有别的要紧任务。
[name="左宣辽"]北边大荒城最近春种，人力紧缺。现在派你过去，添个人手。
[charslot(slot="l",name="avg_4121_zuole_1#10$1",focus="l")]
[name="左乐"]春种？农务？
[name="左乐"]这是......“要紧任务”？
[charslot(slot="r",name="avg_npc_788_1#1$1",focus="r")]
[name="左宣辽"]你觉得这不是要紧任务？
[charslot(slot="l",name="avg_4121_zuole_1#10$1",focus="l")]
[name="左乐"]不。农业是国家要脉，大荒城的事情我也有所耳闻，但......
[name="左乐"]我不明白，为什么是让我去？
[charslot(slot="r",name="avg_npc_788_1#2$1",focus="r")]
[name="左宣辽"]让你多看。
[charslot(slot="l",name="avg_4121_zuole_1#10$1",focus="l")]
[name="左乐"]然后呢......
[charslot(slot="r",name="avg_npc_788_1#2$1",focus="r")]
[name="左宣辽"]多想。
[charslot(slot="l",name="avg_4121_zuole_1#10$1",focus="l")]
[name="左乐"]......
[charslot(slot="r",name="avg_npc_788_1#1$1",focus="r")]
[name="左宣辽"]做完任务交接，就动身启程吧。
[charslot(slot="l",name="avg_4121_zuole_1#1$1",focus="l")]
[name="左乐"]......父亲，还有最后一事。
[name="左乐"]我在调查山海众行动路线的时候，发现了一些疑点。
[name="左乐"]从山海众的行动路线来看，他们似乎对玉门巡防营的行动时间和路线十分熟悉。
[charslot(slot="l",name="avg_4121_zuole_1#3$1",focus="l")]
[name="左乐"]如果......他们真的能拿到玉门守军的布防安排，只恐怕——
[charslot(slot="r",name="avg_npc_788_1#7$1",focus="r")]
[name="左宣辽"]我刚才已经说过。
[charslot(slot="l",name="avg_4121_zuole_1#7$1",focus="l")]
[name="左乐"]......
[charslot(slot="r",name="avg_npc_788_1#7$1",focus="r")]
[name="左宣辽"]这些事，已经与你无关。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="47_g2_desertedcityfield_n", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, amount=0, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_amb_forestnight_loop", volume=0, loop=true, channel="e")]
[SoundVolume(volume=0.5, channel="e",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$d_avg_bldwhoosh")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$d_avg_swrdclave", volume=0.7)]
[CameraShake(duration=0.8, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="35_g5_swordcastingworkshop", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, amount=0.7, block=true)]
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[delay(time=0.5)]
[musicvolume(volume=0.3, fadetime=1)]
[SoundVolume(volume=0.2, channel="e",fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_2024_chyue_1#1$1",focus="m")]
[name="重岳"]莫在行事时，忘了最初的情和理。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="35_g9_yumensuburb", screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_4078_bdhkgt_1#7$1")]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4078_bdhkgt_1#7$1",focus="m")]
[name="截云"]像你这样的人，根本不值得信任！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=2)]
[charslot]
[Background(image="47_g2_desertedcityfield_n", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, amount=0, block=true)]
[delay(time=1)]
[SoundVolume(volume=0.5, channel="e",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_punch02",volume=1)]
[playsound(key="$d_avg_breezetree",delay=0.4)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[StopSound(channel="e", fadetime=2)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4121_zuole_1#2$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4121_zuole_1#2$1",focus="m")]
[name="左乐"]呼......呼......
[Dialog]
[charslot]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_791_1#8$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_791_1#8$1",focus="m")]
[name="录武官"]白天忙着农活，晚上还不忘练习武艺，左乐兄最近一月来实在是辛苦了。
[charslot(slot="m",name="avg_4121_zuole_1#1$1",focus="m")]
[name="左乐"]是你......咳，云兄。
[Dialog]
[charslot]
[playMusic(key="$calm_loop", volume=0.6)]
[charslot(slot="l",name="avg_4121_zuole_1#1$1",focus="r"

... (全文26600字符)
```

### level_act31side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[Subtitle(text="这一季庄稼又没能挺过来。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="播下种，育出了苗，等不到抽穗，不知道什么时候就是一场天灾，之前做的一切都化为乌有。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我们从巨兽那里抢回了我们的土地，可为什么还有这么多人在受着苦？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我们能不能找到一块没有天灾的土地？不奢求年年风调雨顺，风霜雨雪总有办法对付，可天灾源石不讲道理，人挨着就病，庄稼碰上就死。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="种庄稼还要寻找适合的土地，这片大地要是真的不适合人类生存，最初又是谁把“人”种在了这片土地上？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="得想办法，人总得先吃饱肚子。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="47_g12_cityoperastage", screenadapt="coverall", block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_crwddiscuss_outside",loop=true, channel="crwd", volume=0.3)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_beatgong", volume=1)]
[Delay(time=1.5)]
[name="戏台上的唱段"]平莽原定沟壑气冲霄汉，凭壮志干凌云直面河山！东风烈，照霜月，天时难定，惊雷声咽♪
[name="戏台上的唱段"]愿稻香天南地北齐招展，哪怕是酷旱洪水也扑上前！我恨不能以身做云化春雨，迎来春色人间♪
[name="戏台上的唱段"]为耕耘先将身浸汗，好似锄头一把钉入这广袤平原！誓将千里土，踏平做肥田——♪
[Dialog]
[delay(time=1)]
六月阳光炽热，整座城被烤得像只大釜，风一吹，稻谷的清香隔着老远直扑鼻腔，心里也是暖烘烘的。
今年的社戏格外热闹，戏台前人围得层层叠叠，人头攒动，个个努力踮起脚尖瞅着戏台，嘴上不自觉地小声跟唱着。
左乐远远看着戏台，台上人穿着古朴戏服，神情坚毅，唱腔铿锵，一步一叹。戏腔用的不知是哪里的方言，他仔细分辨，有些听不懂。
[Dialog]
[StopSound(channel="crwd", fadetime=2)]
[Delay(time=1)]
[charslot(slot="l",name="avg_4121_zuole_1#10$2",duration=0.7)]
[charslot(slot="r",name="avg_4119_wanqin_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_4121_zuole_1#10$2",focus="l")]
[name="左乐"]这戏唱的是？
[charslot(slot="r",name="avg_4119_wanqin_1#1$1",focus="r")]
[name="禾生"]最早的时候，神农来大荒城开垦土地的故事。
[name="禾生"]每年祭祀神农的时候都要唱这个戏。戏共三出，这是第二出《争天时》。
[charslot(slot = "l", name = "avg_4121_zuole_1#10$2",focus="l")]
[name="左乐"]大荒城的社戏，怎么唱的却不是当地话？
[charslot(slot="r",name="avg_4119_wanqin_1#1$1",focus="r")]
[name="禾生"]第一批来这里的天师来自大炎各地，时间过了这么久，早就没人记得他们都是哪里人。
[name="禾生"]在排社戏的时候，只好凭着印象给每个角色定下一种方言，也算是一种纪念，到了今天，这场戏就是现在这样。
[charslot(slot = "l", name = "avg_4121_zuole_1#10$2",focus="l")]
[name="左乐"]那边排着队的人们又是在做什么？
[charslot(slot="r",name="avg_4119_wanqin_1#1$1",focus="r")]
[name="禾生"]“迎神农”。
[name="禾生"]传说每年夏收，神农都会回到大荒城，看看今年的收成怎么样。
[name="禾生"]早在一千年前，大荒城是一片难得的少受源石污染的土地，是炎国一片重要的耕地。
[name="禾生"]有一批农人就在这里开垦土地，搭起小屋，在这里生活。
[charslot(slot="r",name="avg_4119_wanqin_1#2$1",focus="r")]
[name="禾生"]直到天灾还是找上了他们......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_drumlp_02", volume=1)]
[Delay(time=2)]
又尖又细的唱腔从台上传来，带着几分刺耳，纤细的鼓槌雨点一般敲打在小小的鼓面上，发出一阵急似一阵的乐声。
台上人踏着圆场，粗衣短褐，挎着一个装满稻谷的竹篮。
[Dialog]
[charslot(slot="l",name="avg_4121_zuole_1#1$2",focus="l")]
[charslot(slot="r",name="avg_4119_wanqin_1#2$1",focus="l")]
[name="左乐"]那个人，扮的就是神农吗？
[charslot(slot="r",name="avg_4119_wanqin_1#2$1",focus="r")]
[name="禾生"]当年，大荒城遭遇了一场史无前例的天灾，大半土地被严重污染，同时还涌现出不少破坏田地的怪物。
[name="禾生"]几代人在这里的努力，全都化为乌有。
[name="禾生"]开垦田地不容易，找到一片可以开垦的土地更难。神农知道了这里发生的事情，决定要尽可能拯救这片来之不易的土地。
[charslot(slot="r",name="avg_4119_wanqin_1#10$1",focus="r")]
[name="禾生"]她带领一众农人、天师在这里住下，研究如何清除土地上的污染，培育能适应环境的谷种......一代又一代。
[Dialog]
[charslot]
鼓声从细密逐渐变得浑厚，台上人的唱腔也逐渐转为直冲人脑门的豪迈，一声铜锣的裂响声过后，撕裂般的吼唱声响彻一方戏台。
台上飘过纷纷一片白雪，逐渐掩盖住神农的背影。稻花和芦花做的雪飞向半空，台上终于化作一片安静的雪白。
一声脆生生的笛声响起，一株嫩绿的新芽从大雪中长出，笛声悠悠扬扬，左乐伸手接住一把飞下台的稻花。
[Dialog]
[charslot(slot="l",name="avg_4121_zuole_1#1$2",focus="l")]
[charslot(slot="r",name="avg_4119_wanqin_1#9$1",focus="l")]
[name="左乐"]这里演的是......？
[charslot(slot="r",name="avg_4119_wanqin_1#9$1",focus="r")]
[name="禾生"]神农最后，在前往北边寻找新种的路上离世了。
[name="禾生"]人们没能找到神农的骸骨，只发现了一个竹篮和装着稻谷的口袋。人们把这些东西带回了大荒城，立起了一个衣冠冢。
[name="禾生"]也有人说，在神农离世的那一年夏至，人们刚收完稻谷，就看到神农从天边降临，欣慰地拂过收获的作物，还在田地中撒下了新种。
[charslot(slot="r",name="avg_4119_wanqin_1#2$1",focus="r")]
[name="禾生"]从那以后，大荒城每年都会办社戏，迎神农，祈收成。
[charslot(slot = "l", name = "avg_4121_zuole_1#6$2",focus="l")]
[name="左乐"]神农......是神话人物吗？
[charslot(slot="r",name="avg_4119_wanqin_1#1$1",focus="r")]
[name="禾生"]当然不是！虽然有很多和她有关的神话故事，但神农是确有其人的。
[name="禾生"]天师府的教材上也有对她的记载，她是炎国农业理论最早的奠基人，是第一位系统地总结了农业理论，总结了二十四节气的规律的人。
[charslot(slot="r",name="avg_4119_wanqin_1#8$1",focus="r")]
[name="禾生"]这应该不只是天师府教材的记录？应该是大部分炎国人都有的常识才对......我才想问，你怎么连这些常识都需要来问我？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.3, fadetime=1)]
[charslot]
[Background(image="47_g6_civilengineermasteroffice", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[charslot(slot="m",name="avg_4121_zuole_1#1$1")]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_4121_zuole_1#1$1",focus="m")]
[name="左乐"]黍，其数为六。定天时，规二十四节气......于大饥荒时现身于大荒城，躬耕千年未曾离开......
[charslot(slot="m",name="avg_4121_zuole_1#3$1",focus="m")]
[name="左乐"]代理人中，竟然也有这样的人......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="47_g12_cityoperastage", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true,amount=0, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.6, fadetime=1)]
[charslot(slot="m",name="avg_npc_1249_1#1$1",focus="m")]
[n

... (全文22202字符)
```

### level_act31side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[Subtitle(text="这样的灾，我们还要遇上多少次......？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="刚长出来的嫩苗、压弯的稻穗、硕果累累的枝头......一场天灾下来，只剩下一大片毫无生气的土地。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="蝗虫会啃食掉作物所有的茎叶，大旱、雪灾、低温、洪水，数不胜数......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="初春的一场霜冻差点要了大半新苗的命，我们不知守了多少天才保住剩下的一点。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="还要努力多久，才能让所有人都吃饱肚子？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[gridbg(imagegroup="47_g14_skyovercast_L1/47_g14_skyovercast_R1/47_g14_skyovercast_L2/38_g20_skyblue_R2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720",fadetime=0)]
[delay(time=1)]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
节日热闹的氛围被一场突如其来的雨浇得凉透。
雨飘飘洒洒停了下来，田间的积水却不见消退，渐渐没过了人的脚踝。
[Dialog]
[name="着急的农业天师"]怎么前面就下了这么一会雨，水都漫到这了？！
[name="着急的农业天师"]水这么浑......该不会是连带上游的脏土一块冲过来了？再这么下去田全要被污染了！
[name="着急的农业天师"]*炎国粗口*工地上的在干嘛？快排水啊！
[Dialog]
[charslot]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[Delay(time=0.5)]
[name="惊慌的农业天师"]出事了！堰口水坝塌了！
[name="着急的农业天师"]他妈的！开什么玩笑？！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[gridbg]
[Background(image="47_g8_crestofweir", screenadapt="coverall", block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_xplstrbml", volume=0, loop=true, channel="a")]
[SoundVolume(volume=0.5, channel="a",fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_1245_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_1246_1#1$1",focus="l")]
[name="资深土木天师"]什么情况！
[charslot(slot="r",name="avg_npc_1246_1#1$1",focus="r")]
[name="年轻的土木天师"]不知道上游哪一块源石矿脉炸了，碎屑跟着河流被冲了下来，过闸的时候卷到了堰口轮机里，把坝炸出来一个洞！
[charslot(slot="l",name="avg_npc_1245_1#1$1",focus="l")]
[name="资深土木天师"]之前为什么没发现？！
[charslot(slot="r",name="avg_npc_1246_1#1$1",focus="r")]
[name="年轻的土木天师"]今年水位一直是正常的，之前也没有监测到异常的源石反应，源石活性变化怎么会这么不规律......
[charslot(slot="l",name="avg_npc_1245_1#1$1",focus="l")]
[name="资深土木天师"]见鬼的......偏偏还是汛期，水这么急。
[name="资深土木天师"]水里面不知道还混着多少源石碎屑，被冲到田里庄稼就全完了，可能还会造成人员感染。
[name="资深土木天师"]都小心点！大坝本身的裂口一时半会修不好，先分人去下游堵！
[charslot(slot="r",name="avg_npc_1246_1#1$1",focus="r")]
[name="年轻的土木天师"]这河水眼见越来越急，就怕坝体进一步崩塌，该怎么办——
[charslot(slot="l",name="avg_npc_1245_1#1$1",focus="l")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="资深土木天师"]怎么办？能怎么办！用源石技艺玩命堵着啊！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[StopSound(channel="a", fadetime=1)]
[charslot]
[Background(image="47_g7_fieldhouse", screenadapt="coverall", block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_bodyfallvalley", volume=0.6)]
[PlaySound(key="$d_avg_jump_water", volume=0.9,delay=1)]
[CameraShake(duration=2, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
污水还在蔓延着，田间早已是一片泥泞。
[Dialog]
[charslot(slot="m",name="avg_npc_1247_1#1$1",focus="m")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="焦急的农业天师"]动作快点！再搬点沙袋来！
[name="焦急的农业天师"]这片可是试验田，要是被水淹了损失就大了！
[name="焦急的农业天师"]哎！你的源石技艺不是玩沙子吗？加把劲啊！
[charslot(slot="m",name="avg_npc_1248_1#1$1",focus="m")]
[name="慌乱的农业天师"]你才是玩沙子的......我的源石技艺明明是分析土壤的！唉，试试！
[Dialog]
[charslot]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0, block=true)]
[PlaySound(key="$d_avg_originiumcastshort",volume=1)]
[Blocker(a=1,r=0.95, g=0.95, b=0.95, fadetime=0.3, block=true)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=1, block=true)]
[playsound(key="$d_avg_statueshake", volume=0.6)]
[CameraShake(duration=1.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$d_avg_sandstone", volume=0.8)]
[Delay(time=1.5)]
职农、天师已经排成长龙，一袋袋沙土经过无数双手传递到岸边，在源石技艺的控制下，筑起一道摇摇欲坠的堤坝。
而堤坝还有最后一个缺口。
[Dialog]
[charslot(slot="m",name="avg_npc_1248_1#1$1",focus="m")]
[charslot(slot = "m", action="shake",random=true, power=5, times=30,duration=0.3)]
[name="慌乱的农业天师"]有点......勉强......
[charslot(slot="m",name="avg_4121_zuole_1#4$2",focus="m")]
[name="左乐"]......！
[Dialog]
[PlaySound(key="$d_avg_Qinggong", volume=1)]
[charslot(duration=0.2)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_windmagic", volume=0.6)]
[CameraShake(duration=1.5, xstrength=10, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_4121_zuole_1#6$2",duration=1)]
[delay(time=1.5)]
少年抱起一袋沙土跃身而起，想要飞身去堵上那个缺口。只觉得面前一阵疾风吹来，牵绊住了他的脚步。
[charslot(slot="m",name="avg_4119_wanqin_1#6$1",focus="m")]
[name="禾生"]你要做什么？！
[name="禾生"]河水里混进去的泥沙里不知道有多少源石杂质，你是想被感染吗！
[charslot(slot="m",name="avg_4121_zuole_1#4$2",focus="m")]
[name="左乐"]保护百姓是我的职责......
[charslot(slot="m",name="avg_4119_wanqin_1#6$1",focus="m")]
[name="禾生"]你凭什么觉得所有人都需要你保护？你和站在这里的人有什么不一样？
[charslot(slot="m",name="avg_4121_zuole_1#10$2",focus="m")]
[name="左乐"]我——
[name="左乐"]......我还能帮上什么忙？
[charslot(slot="m",name="avg_4119_wanqin_1#5$1",focus="m")]
[name="禾生"]刚才去调查过了，这是堰口水坝破坏导致的洪水......农田原有的排水系统已经超过负荷了。
[name="禾生"]正是汛期，堰口一时半会也修不好，靠堵是堵不上的，再这样下去，损失只会越来越大......
[name="禾生"]......听说你是信使，脚程快？
[c

... (全文26762字符)
```

### level_act31side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$monastery_sad_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
姐姐。
我跟着那位先生远走，才发现原来外面的天地和这大荒城大不相同。我们留在这里短短几十年，人类又琢磨出不少新奇玩意。
炎国大地上还有各式各样的城市，除了望不到头的农田，还有华丽的宫殿，热闹的集市，样样有趣。
我回来歇歇就走。这一趟还是出远门，不知道多少年才能回来。
说起来，这大荒城也不是早些年艰苦的时候，能照料这片田地的人多得是，你真的不打算和我一起出去看看？
[Dialog]
[Delay(time=1)]
......姐姐，我发现，原来外面的大地与这大荒城也没有什么不同。
是啊。又走了几十年，还是百来年？想法总是会变的。
见得多了，发现原来不论走到哪里，人到底只是人，这人间好像没什么意思......人心叵测，但其实也不难猜。
嗯。先生死前说的话，我吃透了。
姐姐......你还打算留在这里多久？
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_cottage", screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avgnew_2014_nian_1#1$1",duration=0.7)]
[charslot(slot="r",name="avgnew_2015_dusk_1#3$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="l",name="avgnew_2014_nian_1#1$1",focus="l")]
[name="年"]喂——
[name="年"]怎么好不容易把你从那座山头揪出来，还是这么自闭？既然现在黍也不在，和我出去转转咯？
[charslot(slot="l",name="avgnew_2014_nian_1#7$1",focus="l")]
[name="年"]这里没什么新奇玩意，但是果蔬粮食的味道还真是移动城市的种植地块比不了的。对了，你是不是还从来没见过粮食是怎么酿成酒的？
[charslot(slot="r",name="avgnew_2015_dusk_1#3$1",focus="r")]
[name="夕"]心烦。
[charslot(slot="l",name="avgnew_2014_nian_1#8$1",focus="l")]
[name="年"]天师府是不是又来找你麻烦了？
[charslot(slot="r",name="avgnew_2015_dusk_1#5$1",focus="r")]
[multiline(name="夕")]我怕天师府什么！
[charslot(slot="r",name="avgnew_2015_dusk_1#3$1",focus="r")]
[multiline(name="夕")]我就是......我......
[charslot(slot="r",name="avgnew_2015_dusk_1#1$1",focus="r")]
[name="夕"]......有这功夫，你应该为外面一动不动的大家伙想想办法。
[charslot(slot="l",name="avgnew_2014_nian_1#7$1",focus="l")]
[name="年"]天师们都去救灾了，我一个人能有什么办法，又不能亲自上手......
[charslot(slot="l",name="avgnew_2014_nian_1#1$1",focus="l")]
[name="年"]好无聊啊！还是让我看看，你今天画的是......
[charslot(slot="r",name="avgnew_2015_dusk_1#5$1",focus="r")]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="夕"]不行！
[charslot(slot="l",name="avgnew_2014_nian_1#4$1",focus="l")]
[name="年"]别这么小气嘛，没灵感的话我还能给你出出主意？
[charslot(slot="r",name="avgnew_2015_dusk_1#5$1",focus="r")]
[name="夕"]给我，出去——
[Dialog]
[PlaySound(key="$p_imp_ancientsword_h",volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[Background(image="47_g5_factory_inside",screenadapt="coverall")]
[Delay(time=0.5)]
[charslot(slot="l",name="avgnew_2014_nian_1#4$1")]
[charslot(slot="r",name="avgnew_2015_dusk_1#3$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avgnew_2014_nian_1#4$1",focus="l")]
[name="年"]这么紧张？看来是真的有秘密。
[charslot(slot="r",name="avgnew_2015_dusk_1#2$1",focus="r")]
[name="夕"]不是秘密，是烦心事。
[charslot(slot="l",name="avgnew_2014_nian_1#4$1",focus="l")]
[name="年"]......天师府里的老家伙们是挺烦的，但其实奈何不了你什么。而且都有朝廷替我们打包票了，他们最多唠叨你几句。
[charslot(slot="l",name="avgnew_2014_nian_1#7$1",focus="l")]
[name="年"]所以你在烦......“他”。
[charslot(slot="r",name="avgnew_2015_dusk_1#3$1",focus="r")]
[name="夕"]......
[charslot(slot="l",name="avgnew_2014_nian_1#7$1",focus="l")]
[name="年"]我能感觉到他已经到了，从不藏掖的。我们怎么说也是一家人，不去看看？
[charslot(slot="r",name="avgnew_2015_dusk_1#3$1",focus="r")]
[name="夕"]我才不去。
[charslot(slot="l",name="avgnew_2014_nian_1#7$1",focus="l")]
[name="年"]这么生疏啊......我听说他每次路过你的山头，都会带些搜罗来的当世最好的画作送你的，你可别嘴硬说你不喜欢。
[charslot(slot="r",name="avgnew_2015_dusk_1#3$1",focus="r")]
[name="夕"]......不一样了。
[charslot(slot="r",name="avgnew_2015_dusk_1#9$1",focus="r")]
[name="夕"]你上次见他，是什么时候？
[charslot(slot="l",name="avgnew_2014_nian_1#6$1",focus="l")]
[name="年"]唔，还真记不清了。
[charslot(slot="l",name="avgnew_2014_nian_1#7$1",focus="l")]
[name="年"]他手中的生意做得太大，被司岁台提醒了好几次，之后好像收敛了一点。最近几年就只是游山玩水，把炎国每座城市都挨个转了个遍。
[name="年"]可司岁台盯他比盯我们要严密得多了。
[charslot(slot="r",name="avgnew_2015_dusk_1#9$1",focus="r")]
[name="夕"]你怎么知道得这么清楚......
[charslot(slot="l",name="avgnew_2014_nian_1#1$1",focus="l")]
[name="年"]和司岁台打交道的时候，偷偷瞄了两眼他们的记事本——藏得没那么深的那部分。
[charslot(slot="r",name="avgnew_2015_dusk_1#3$1",focus="r")]
[name="夕"]......
[charslot(slot="r",name="avgnew_2015_dusk_1#1$1",focus="r")]
[name="夕"]“生意做得太大”。我怎么记得，他不过只是个喜欢养蚕种桑，跟在黍身边的小呆子。
[name="夕"]最近一次见他的时候——就是你所谓的“路过”那时——我从画里探过一两眼。
[charslot(slot="r",name="avgnew_2015_dusk_1#3$1",focus="r")]
[name="夕"]那眼神，浑，讨厌，和那个——
[charslot(slot="l",name="avgnew_2014_nian_1#1$1",focus="l")]
[name="年"]——和臭棋篓子一样，我懂的。
[name="年"]而且臭棋篓子越狱那年，他人就在百灶。你以为这几年大炎对你我不闻不问，都主要盯着谁呢？
[charslot(slot="r",name="avgnew_2015_dusk_1#9$1",focus="r")]
[name="夕"]你觉得他俩勾搭上了？
[charslot(slot="l",name="avgnew_2014_nian_1#1$1",focus="l")]
[name="年"]不晓得。我还以为臭棋篓子只和令姐大哥关系好。
[name="年"]但要是司岁台做下了这种判断，他也不可能像现在这样到处串门了。
[charslot(slot="l",name="avgnew_2014_nian_1#4$1",focus="l")]
[name="年"]你又不是不知道他有多会做“人”，年年定期给司岁台上交的账本，每一笔生意、每一文的收支都记得明明白白，挑不出半点毛病。
[name="年"]不论哪里的城市遇上天灾受了损失，他自掏腰包赈灾的速度比谁都快。就是看在这一点上，司岁台再怎么说也得留几分情面。
[charslot(slot="r",name="avgnew_2015_dusk_1#9$1",focus="r")]
[name="夕"]你觉得他有几分好心？
[charslot(slot="l",name="avgnew_2014_nian_1#7$1",focus="l")]
[name="年"]到底也是我们的兄弟......我还能背后说他坏话？
[charslot(slot="r",name="avgnew_2015_dusk_1#3$1",focus="r")]
[name="夕"]这种事你少干了？
[name="夕"]何况人间本就不存在我们这样的关系。“兄弟姐妹”......我倒是......
[Dialog]
[charslot(slot="l",name="avgnew_2014_nian_1#4$1",focus="l")]
[charslot(slot="l",posfrom="0,0",posto="35,0",duration=0.4,focus="l",isblock=true)]
[name="年"]你倒是？
[charslot(slot="r",name="avgnew_2015_dusk_1#3$1",focus="r")]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="夕"]滚。别凑过来。也别趁机偷看！
[Dialog]
[PlaySound(key="$d_avg_branchrupture", volume=0.4)]
[PlaySound(key="$d_avg_pendrop",volume=0.7,delay=0.3)]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibra

... (全文24483字符)
```

### level_act31side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="47_g8_crestofweir",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_1236_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_1236_1#1$1",focus="r")]
[name="衣着华丽的男性"]......
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="l",name="avg_4121_zuole_1#1$2",duration=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_4121_zuole_1#1$2",focus="l")]
[name="左乐"]绩先生。
[charslot(slot="r",name="avg_npc_1236_1#1$1",focus="r")]
[name="绩"]你就是......左公子吧。
[name="绩"]初次见面，没什么准备，有失礼数了。
[charslot(slot="l",name="avg_4121_zuole_1#10$2",focus="l")]
[name="左乐"]你认识我......？
[Dialog]
[charslot]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_hgmlgscrm", volume=1)]
[charslot(slot="m",name="avg_npc_1244_1#2$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1244_1#2$1",focus="m")]
[name="奇异的织物"]（诡异的长鸣）
[Dialog]
[charslot]
左乐右手习惯性摸向平时腰间挂刀的位置，却只摸到一个用于操作农耕装置的天师仪。
这一细小的动作似乎没能逃过男人的眼睛，他嘴角挂上笑意。
[Dialog]
[charslot(slot="l",name="avg_4121_zuole_1#10$2",focus="r")]
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="r")]
[name="绩"]左公子不必紧张，只是一些无害的小玩意儿。
[charslot(slot="l",name="avg_4121_zuole_1#10$2",focus="l")]
[name="左乐"]“纺因织果，裁虚为实”......这些东西，是你的造物？
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="r")]
[name="绩"]举手之劳。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_hgmgrssvcm", volume=1)]
[charslot(slot="m",name="avg_npc_1244_1#2$1",focus="m")]
[Delay(time=1)]
[name="奇异的织物"]（诡异的嘶鸣）
[Dialog]
[PlaySound(key="$d_avg_shdwblwvr", volume=1)]
[charslot(duration=1.5)]
[Delay(time=2)]
男人轻轻挥了挥手，古怪的生物顷刻间化为缕缕细碎的丝线，继而灰飞烟灭。
[Dialog]
[charslot(slot="l",name="avg_4121_zuole_1#6$2",focus="l")]
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="l")]
[name="左乐"]你们巨兽代理人的能力，始终让人难以琢磨。
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="r")]
[name="绩"]不过是些雕虫绣花的功夫，能派上用场的地方不多。
[name="绩"]涝灾过后，紧跟着的就是虫害和病害。看不见摸不着的灾害难对付，织成具体物件，再去消灭就容易多了。
[name="绩"]要是让姐姐看到我做这种事，又要责备我“逆天而行”了。
[charslot(slot="l",name="avg_4121_zuole_1#1$2",focus="l")]
[name="左乐"]你本不该出现在这里。
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="r")]
[name="绩"]这里也算是我儿时待过的地方，许多年没有回来过了，有些想念。
[charslot(slot="l",name="avg_4121_zuole_1#1$2",focus="l")]
[name="左乐"]像你们这样的存在，竟然也会有“儿时”这样的概念。
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="r")]
[name="绩"]不论寿命长短，人都有蒙昧无知的时候。那时候见到的新奇事物，印象也会更深一点。
[name="绩"]对一直陪在身边的人，也总会多挂念一点。
[charslot(slot="l",name="avg_4121_zuole_1#4$2",focus="l")]
[name="左乐"]你们几位兄弟姐妹的会面是大事，事先都应该通报司岁台才对。
[charslot(slot="r",name="avg_npc_1236_1#1$1",focus="r")]
[name="绩"]朝廷补给的车队被天灾拦在了半路上，我收到那位老天师的消息后，可是立刻自掏腰包送了这一批应急的货物来。
[name="绩"]回到这里，我也只是匆匆看了姐姐一眼，那两位妹妹的面都没有见过。司岁台未免有点不近“人”情了？
[charslot(slot="l",name="avg_4121_zuole_1#4$2",focus="l")]
[name="左乐"]先生在司岁台的名单里，是需要重点盯防的一位。
[charslot(slot="r",name="avg_npc_1236_1#7$1",focus="r")]
[name="绩"]哪怕这些年，我从来没有做过一件违背规矩的事？
[charslot(slot="l",name="avg_4121_zuole_1#4$2",focus="l")]
[name="左乐"]这不该由先生说了算。
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="r")]
[name="绩"]可左公子现在，不也没穿着秉烛人的制服？
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="n")]
眼前的男人笑了笑，温和，礼貌，从容。
左乐却难自制地感到了一股寒意。
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="r")]
[name="绩"]其实在下久闻左公子玉名。今日终于得以一见，便想或许可以和左公子交个朋友。
[charslot(slot="l",name="avg_4121_zuole_1#1$2",focus="l")]
[name="左乐"]......不用这样客套。
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="r")]
[name="绩"]前些年逗留百灶，见过不少世家子弟。只论文章才学，其中也有不少人堪称青年才俊。
[name="绩"]但能真正像左公子这样肯踏踏实实做点实事的人，恐怕按学宫的名单挨个数也数不出几位。
[charslot(slot="l",name="avg_4121_zuole_1#1$2",focus="l")]
[name="左乐"]......
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="r")]
[name="绩"]去年十一月，琅珆山海众勾连匪患，左公子孤身涉险，救出了被困匪窝的数十无辜百姓。
[name="绩"]年初二月，为了追查那件特殊的酒盏，路上又是凶险无数。
[name="绩"]不知情的外人只道左公子年纪轻轻身居要职是蒙父辈荫庇，又哪能想到秉烛人的任务有多么凶险？
[name="绩"]左公子之前的所有努力，难道因为一次失误就要被全盘否定？
[charslot(slot="l",name="avg_4121_zuole_1#6$2",focus="l")]
[name="左乐"]这些事情......你没有理由知道。
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="r")]
[name="绩"]生意人，为了通晓行情，总是习惯多方打听。打听到的东西偶尔也能作为货物售卖。就看客人愿意出多少价钱。
[name="绩"]我还要知道，什么样的客人会愿意为什么情报付什么价钱。
[name="绩"]比如，我还知道大荒城北边的河对岸藏着什么，年在这里造的那件工程到底有什么用。
[name="绩"]我还知道，玉门遭遇天灾一事，你始终怀疑有更高位者从中做梗，但迟迟抓不住线索，对不对？
[charslot(slot="l",name="avg_4121_zuole_1#6$2",focus="l")]
[name="左乐"]......
[charslot(slot="l",name="avg_4121_zuole_1#2$2",focus="l")]
[name="左乐"]我当然知道先生行事周密，滴水不漏。
[charslot(slot="l",name="avg_4121_zuole_1#1$2",focus="l")]
[name="左乐"]可司岁台也绝非无能之辈，但凡有任何蛛丝马迹，司岁台都会一查到底。
[name="左乐"]在下敬告先生，不要做逾矩之事。
[charslot(slot="r",name="avg_npc_1236_1#1$1",focus="r")]
[name="绩"]这是左公子作为朋友的提醒？
[charslot(slot="l",name="avg_4121_zuole_1#1$2",focus="l")]
[name="左乐"]这是我作为司岁台秉烛人的忠告。
[charslot(slot="r",name="avg_npc_1236_1#9$1",focus="r")]
[name="绩"]我想左公子应该是多虑了......整个炎国最精锐的天师尽数留守在大荒城北边的天机阁里，我一个人又能掀起什么风浪呢？
[charslot(slot="r",name="avg_npc_1236_1#1$1",focus="r")]
[name="绩"]比起在下，此时此刻，还是这条河对岸的那些邪祟诡魔，更该让人担心吧。
[charslot(slot="l",name="avg_4121_zuole_1#10$2",focus="l")]
[name="左乐"]......什么？
[charslot(slot="r",name="avg_npc_1236_1#1$1",focus="r")]
[name="绩"]左公子大概还不知道，最近三个月以来，天机阁已经死了多少天师？
[charslot(slot="l",name="avg_4121_zuole_1#6$2",focus="l")]
[name="左乐"]——！
[name="左乐"]休要蛊惑人心......
[charslot(slot="r",name="avg_npc_1236_1#1$1",focus="r")]
[name="绩"]生意人诚信为本，我从来不说假话。左公子要是不信，不如自己先去查查。
[name="绩"]再好好想一想，自己想要做什么。要不要也来找我做一笔交易。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="47_g3_fieldpath", screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step",loop=false)]
[stopsound(channel="step",fadetime=2)]
[charslot(slot = "m", name = "avg_4122_grabds_1#5$1",duration=

... (全文22056字符)
```

### level_act31side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="35_mini01_villagevacancy",screenadapt="coverall",block=true)]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[charslot(slot="l",name="avg_npc_007")]
[charslot(slot="r",name="avg_npc_008")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=1, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$fightgeneral", volume=0.8)]
[PlaySound(key="$d_avg_punch", volume=0.6,delay=0.3)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[delay(time=0.2)]
[Dialog]
[PlaySound(key="$bodyfalldown1", volume=1)]
[PlaySound(key="$bodyfalldown2", volume=1,delay=0.2)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="l",name="avg_npc_007",afrom=1,ato=0,duration=0.5)]
[charslot(slot="r",name="avg_npc_008",afrom=1,ato=0,duration=0.7)]
[Delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_npc_785_1#1$1",duration=0.5)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_785_1#1$1",focus="m")]
[name="槐天裴"]你人没事？
[charslot(slot="m",name="avg_npc_1236_1#7$1",focus="m")]
[name="商队老板"]多谢大侠，多谢。
[name="商队老板"]难得从北方买了些珍贵矿石，想卖到南方去，没想到在这碰上拦路的劫匪。要不是遇上大侠您，我这一趟生意可就血本无归了。
[charslot(slot="m",name="avg_npc_785_1#1$1",focus="m")]
[name="槐天裴"]是商队，就别挑小路走。
[charslot(slot="m",name="avg_npc_1236_1#7$1",focus="m")]
[multiline(name="商队老板")]这不是急着赶路......
[charslot(slot="m",name="avg_npc_1236_1#9$1",focus="m")]
[PlaySound(key="$d_avg_wadmoney", volume=1)]
[multiline(name="商队老板")]唉，还得多谢您仗义出手，一点点心意，请笑纳。
[charslot(slot="m",name="avg_npc_785_1#1$1",focus="m")]
[name="槐天裴"]没兴趣，走了。
[Dialog]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1236_1#7$1",focus="m")]
[name="商队老板"]先生请留步！留步......
[charslot(slot="m",name="avg_npc_1236_1#9$1",focus="m")]
[name="商队老板"]我看先生的身手可真是了不得——您是武林中人？
[Dialog]
[charslot]
[PlaySound(key="$d_avg_runstop", volume=1)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_785_1#11$1",focus="m")]
[name="槐天裴"]你要和我比划比划？
[charslot(slot="m",name="avg_npc_1236_1#9$1",focus="m")]
[name="商队老板"]岂敢岂敢......您看到了，我就是个手无缚羽之力的商人，哪有和您比试的能耐。
[name="商队老板"]不过既然是武林中人......实在是巧，不久前我碰巧搜罗来一本珍贵的武学秘籍，先生说不定会感兴趣。
[charslot(slot="m",name="avg_npc_785_1#12$1",focus="m")]
[name="槐天裴"]笑话，这世上有我用得上的武学秘籍？
[charslot(slot="m",name="avg_npc_1236_1#9$1",focus="m")]
[name="商队老板"]别急嘛，先生要不先看一眼？在下做生意向来只卖客人用得上的商品。
[charslot(slot="m",name="avg_npc_785_1#1$1",focus="m")]
[name="槐天裴"]不看。
[charslot(slot="m",name="avg_npc_1236_1#10$1",focus="m")]
[name="商队老板"]还是看一眼吧，不会耽误您几分钟时间，保证不让您后悔。
[charslot(slot="m",name="avg_npc_785_1#7$1",focus="m")]
[name="槐天裴"]你有完没——
[Dialog]
[PlaySound(key="$d_avg_magicchange", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0.8, g=0.8, b=0.8, fadetime=1, block=true)]
[charslot]
[Background(image="35_g11_yumendesert",screenadapt="coverall",block=true)]
[charslot(slot="m",name="avg_2024_chyue_1#1$1",bstart=0.2,bend=0.7)]
[delay(time=0.5)]
[Blocker(a=0, r=0.8, g=0.8, b=0.8, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_2024_chyue_1#1$1",bstart=0.2,bend=0.7,focus="m")]
[name="重岳"]没想到，阁下的武艺竟然精进到如此地步。
[name="重岳"]如今我已经不是阁下对手。
[charslot(slot="m",name="avg_npc_785_1#6$1",focus="m")]
[name="槐天裴"]你......
[charslot(slot="m",name="avg_npc_785_1#12$1",focus="m")]
[name="槐天裴"]赢了你，我是不是就是天下第一？
[charslot(slot="m",name="avg_2024_chyue_1#1$1",bstart=0.2,bend=0.7,focus="m")]
[name="重岳"]你已经是天下第一。
[charslot(slot="m",name="avg_npc_785_1#12$1",focus="m")]
[name="槐天裴"]天下第一......我是天下第一？
[Dialog]
[charslot]
心头血热，拳锋上还留有余温。
登高临绝顶，毕生夙愿已然了却——
不，不对！
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
这人是谁？
[Dialog]
[charslot(slot="m",name="avg_2024_chyue_1#1$1",bstart=0.2,bend=0.7,focus="m")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_punchsp1",volume=1)]
[PlaySound(key="$d_avg_punchsp5",volume=1,delay=0.3)]
[CameraShake(duration=1, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[Dialog]
[PlaySound(key="$d_avg_shdwblwvr",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0.8, g=0.8, b=0.8, fadetime=0.5, block=true)]
[charslot]
[Background(image="35_mini01_villagevacancy",screenadapt="coverall",block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0.8, g=0.8, b=0.8, fadetime=1, block=true)]
[delay(time=1)]
一阵恍惚。
[charslot(slot="m",name="avg_npc_785_1#6$1",focus="m")]
[name="槐天裴"]......怎么回事？
[charslot(slot="m",name="avg_npc_785_1#5$1",focus="m")]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="槐天裴"]你到底是什么人？！
[charslot(slot="m",name="avg_npc_1236_1#9$1",focus="m")]
[name="商队老板"]刚说了，一介商贩。
[name="商队老板"]什么都卖，什么都收。
[Dialog]
[charslot]
他是如何找到我的？
[charslot(slot="m",name="avg_npc_785_1#12$1",focus="m")]
[name="槐天裴"]......为什么找我？
[charslot(slot="m",name="avg_npc_1236_1#9$1",focus="m")]
[name="商队老板"]我知道你习武四十年，就是为了打败一个对手。
[name="商队老板"]眼前就有一个少花几十年功夫就能追上那个人的机会，先生想不想要？
[charslot(slot="m",name="avg_npc_785_1#7$1",focus="m")]
[name="槐天裴"]用不着你来插手！
[charslot(slot="m",name="avg_npc_1236_1#9$1",focus="m")]
[name="商队老板"]先生不打算买我的东西，但先生却有一件我打算买的东西。
[name="商队老板"]听说先生不久前得到了一把宝剑，想问问您，愿意用什么价格卖给我？
[charslot(slot="m",name="avg_npc_785_1#5$1",focus="m")]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="槐天裴"]滚！
[Dialog]
[charslot(slot="m",name="avg_npc_1236_1#9$1",focus="m")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_punch02", volume=0.7)]

... (全文26174字符)
```

### level_act31side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="47_g10_fairyfarmland_ex",screenadapt="coverall", block=true)]
[Delay(time=1)]
[bgeffect(name="$eb_cnclouds",layer=1)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_2025_shu_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_2025_shu_1#1$1",focus="m")]
[name="黍"]......
[Dialog]
[charslot]
望不到头的稻田，迷离如幻。天地宽广，却万籁俱寂。
一丝酒香飘过，云做旋舞，飘飘然流入一只酒盏。
仰头饮尽，瞬间天朗气清。
[Dialog]
[charslot(slot="m",name="avg_2023_ling_1#2$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_2023_ling_1#2$1",focus="m")]
[name="令"]嗯......真是一场好梦。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_2023_ling_1#2$1",focus="r")]
[charslot(slot = "r", name = "avg_2025_shu_1#1$1",focus="r")]
[name="黍"]你怎么有功夫来我这里？
[charslot(slot="l",name="avg_2023_ling_1#8$1",focus="l")]
[name="令"]你这最近不是很热闹？正好来看看你答应我的高粱酒酿好没有。
[charslot(slot = "r", name = "avg_2025_shu_1#2$1",focus="r")]
[name="黍"]你在梦里，我怎么把酒给你？
[name="黍"]你说的是哪一年的酒，这又是你的哪个梦呢？
[charslot(slot="l",name="avg_2023_ling_1#8$1",focus="l")]
[name="令"]梦里喝不到，让我闻闻味儿也好啊。
[name="令"]或者是来看看我那个最辛苦的妹妹，最近是不是又累瘦了一点。
[charslot(slot = "r", name = "avg_2025_shu_1#9$1",focus="r")]
[name="黍"]......
[charslot(slot="l",name="avg_2023_ling_1#3$1",focus="l")]
[name="令"]原来这就是小年做出来的奇妙物件？
[Dialog]
[charslot(duration=0.5)]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[Delay(time=1)]
诗人挥一挥衣袖，手边便出现一坛酒，两只盏。
她抬手拍碎坛口的泥封，陈年酒香霎时蔓延。
诗人回身，眺望。稻田绵延百里、万里，春夏秋冬于天空中盘旋，寒来暑往，春去秋来。
[Dialog]
[charslot(slot="l",name="avg_2023_ling_1#9$1",focus="l")]
[charslot(slot = "r", name = "avg_2025_shu_1#9$1",focus="l")]
[name="令"]这就是你在这颗“心脏”里看到的风景？
[name="令"]无尽的稻田，轮转的四季，你每日都在耕作，这儿真能造出你们说的那个东西？
[name="令"]需不需要我也来帮你们一把？
[charslot(slot = "r", name = "avg_2025_shu_1#9$1",focus="r")]
[name="黍"]我怕你来了，这个容器也会变成一个大酒缸，或者是突然有了自己的想法，觉得世间不逍遥，不如长梦不醒。
[charslot(slot="l",name="avg_2023_ling_1#8$1",focus="l")]
[name="令"]真的不需要我帮帮？你在这里待了多少年，我都快要记不清了，再不出来走走就怕你憋成我的酒葫芦。
[name="令"]别的弟弟妹妹，只怕是看不清事里事外，只有你，我只担心你看得太透。
[name="令"]看得太透，就看不到“自己”了。
[charslot(slot = "r", name = "avg_2025_shu_1#9$1",focus="r")]
[name="黍"]不过是在这里耕种罢了。
[charslot(slot="l",name="avg_2023_ling_1#8$1",focus="l")]
[name="令"]山水草木皆有情，这一草一木在你看来，也未必和我们的生命有什么区别。
[name="令"]你还有什么放不下的东西呢，你还会在意什么呢？
[charslot(slot = "r", name = "avg_2025_shu_1#4$1",focus="r")]
[name="黍"]颉曾经也留下过那么多书卷字帖，她希望能教每个人读书识字。但她走后，那些字帖书文也一同消失，除了我们，没人记得她。
[name="黍"]可后来我去过几所学堂，还有天师府，看到有些书本中用的字迹，竟和她的一模一样。
[name="黍"]她那些东西早都没有了，连我都没能留下哪怕一张，但她说过的话又从那些学生的嘴里说了出来，写过的字又在那些学生的笔下复现。
[name="黍"]我记得她和我说过，“重要的是我能留下来的”。
[charslot(slot = "r", name = "avg_2025_shu_1#2$1",focus="r")]
[name="黍"]......我只是在看，这片稻田的尽头，能留下什么。如果有一日我也消散了，我能为这里留下什么。
[charslot(slot="l",name="avg_2023_ling_1#8$1",focus="l")]
[name="令"]你一直在看着的那个结局，有变化吗？
[charslot(slot = "r", name = "avg_2025_shu_1#4$1",focus="r")]
[name="黍"]白茫茫一片大雪，从来没有变过。
[name="黍"]......春种秋收，繁盛过后，最终都被一场大雪掩埋。
[charslot(slot="l",name="avg_2023_ling_1#4$1",focus="l")]
[name="令"]这样啊......
[charslot(slot="l",name="avg_2023_ling_1#1$1",focus="l")]
[name="令"]对这个结果，你会失望吗？还是觉得遗憾？
[charslot(slot = "r", name = "avg_2025_shu_1#2$1",focus="r")]
[name="黍"]来这世间走过一遭，这本身不就是结果？
[name="黍"]就像这世上无数人一样，有谁是想着生命有一个终点，便无所适从了呢。
[charslot(slot="l",name="avg_2023_ling_1#1$1",focus="l")]
[name="令"]可是，我们有的兄弟不这么想......那位弟弟，他回来了？
[charslot(slot = "r", name = "avg_2025_shu_1#1$1",focus="r")]
[name="黍"]嗯。
[charslot(slot="l",name="avg_2023_ling_1#7$1",focus="l")]
[multiline(name="令")]原来那个胆小又乖巧的绩去哪里了呢？
[charslot(slot="l",name="avg_2023_ling_1#4$1",focus="l")]
[multiline(name="令")]唉，这些弟弟妹妹，还是小时候比较可爱。
[charslot(slot = "r", name = "avg_2025_shu_1#8$1",focus="r")]
[name="黍"]......我会去见见他。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[bgeffect]
[charslot]
[Background(image="47_g3_fieldpath", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_npc_1238_1#2$1")]
[charslot(slot="r",name="avg_4122_grabds_1#2$1")]
[delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="r",name="avg_4122_grabds_1#2$1",focus="r")]
[name="小满"]一、二、三......
[charslot(slot="r",name="avg_4122_grabds_1#9$1",focus="r")]
[name="小满"]大嗓门，这些到底是什么新品种啊？我好像从来没见过，长得还怪好看的。
[charslot(slot="l",name="avg_npc_1238_1#2$1",focus="l")]
[name="暴躁的天师学徒"]说了你也听不懂，别多嘴，帮我找就对了。
[charslot(slot="r",name="avg_4122_grabds_1#8$1",focus="r")]
[name="小满"]嘁，叫人帮忙还这么大脾气......
[charslot(slot="r",name="avg_4122_grabds_1#2$1",focus="r")]
[name="小满"]对了大嗓门，我还想问你一个事情......
[name="小满"]你不是天师府的学徒吗，而且我认识的人里，除了黍姐姐和小禾，就数你懂得最多了。
[charslot(slot="r",name="avg_4122_grabds_1#4$1",focus="r")]
[name="小满"]......
[charslot(slot="l",name="avg_npc_1238_1#5$1",focus="l")]
[name="暴躁的天师学徒"]你要问什么，赶紧说啊。
[charslot(slot="r",name="avg_4122_grabds_1#11$1",focus="r")]
[name="小满"]......你......有没有见过我的爸爸妈妈？
[charslot(slot="l",name="avg_npc_1238_1#7$1",focus="l")]
[name="暴躁的天师学徒"]......
[charslot(slot="l",name="avg_npc_1238_1#6$1",focus="l")]
[CameraShake(duration=0.3, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="暴躁的天师学徒"]*炎国粗口*天师府上上下下多少人，你以为我是门卫大爷，把每个人都记得清清楚楚？！
[name="暴躁的天师学徒"]脑子被泥砸傻了吧你！
[charslot(slot="r",name="avg_4122_grabds_1#5$1",focus="r")]
[name="小满"]不知道就不知道嘛，干嘛突然凶人。
[charslot(slot="l",name="avg_npc_1238_1#5$1",focus="l")]
[name="暴躁的天师学徒"]你为啥想起来要问我这个？
[charslot(slot="r",name="avg_4122_grabds_1#8$1",focus="r")]
[name="小满"]今天我见到了一个奇怪的商人，他说他是从大荒城外面，从很远的地方来的。
[charslot(slot="l",name="avg_npc_1238_1#2$1",focus="l")]
[name="暴躁的天师学徒"]哦？
[charslot(slot="r",name="avg_4122_grabds_1#8$1",focus="r")]
[name="小满"]黍姐姐说，我的爸妈也是去很远的地方当天师了。但是不知道他们到底是去做什么，这么多年都没回来，也从来没有听别人说起过。
[name="小满"]大嗓门，你真的不能帮我打听打听吗？
[name="小满"]也不用让他们回来，我就是想写封信告诉他们，大荒城快搬家了，搬上了移动地块。他们回家的时候别找不到路。
[charslot(slot="l",name="avg_npc_1238_1#9$1",focus="l")]
[name="暴躁的天师学徒"]......
[na

... (全文18709字符)
```

### level_act31side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_snow_2",screenadapt="coverall")]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=2, keep=true, initamount=0, amount=0.7, block=true)]
[charslot(slot="m",name="avg_2025_shu_1#1$1",duration=1.5)]
[delay(time=2)]
[charslot(slot="m",name="avg_2025_shu_1#2$1")]
[name="黍"]你又要走了。
[charslot(slot="m",name="avg_npc_1242_1#9$1")]
[name="年迈的女性"]这次不劝我了？
[charslot(slot="m",name="avg_2025_shu_1#1$1")]
[name="黍"]你又有哪次听劝了呢。
[charslot(slot="m",name="avg_npc_1242_1#1$1")]
[name="年迈的女性"]可没有你唠叨两句，我反而觉得心里空落落的。
[name="年迈的女性"]我还能走得动，胳膊腿都还结实着。春天的风还是这么冷，我也不能躺在椅子上晒太阳。
[charslot(slot="m",name="avg_2025_shu_1#16$1")]
[name="黍"]你该知道，北边有多危险。
[charslot(slot="m",name="avg_npc_1242_1#6$1")]
[name="年迈的女性"]可是黍......你也知道，我们没有办法......
[name="年迈的女性"]我们花了几十年时间，才开辟出这点土地。可还是远远不够......
[charslot(slot="m",name="avg_npc_1242_1#1$1")]
[name="年迈的女性"]粮食和地总是不够的......再北一点的地方，说不定可以找到特殊的庄稼，可以种在源石污染过的土地上的庄稼。
[name="年迈的女性"]到时候，整片大地都可以当作我们的农田，再也不会有人忍饥挨饿。
[charslot(slot="m",name="avg_2025_shu_1#5$1")]
[name="黍"]那你更应该留下来。
[name="黍"]找不到这种庄稼，我们就慢慢培育。十代，百代，总有一天——
[charslot(slot="m",name="avg_npc_1242_1#3$1")]
[name="年迈的女性"]可是，我哪还有那么多时间呢？
[charslot(slot="m",name="avg_2025_shu_1#8$1")]
[name="黍"]......
[charslot(slot="m",name="avg_npc_1242_1#2$1")]
[name="年迈的女性"]何况，“种在源石污染土地里的庄稼”“整片大地变成良田”，这样的话，被人听到，只会被当作痴人说梦吧。
[charslot(slot="m",name="avg_2025_shu_1#3$1")]
[name="黍"]......我说不过你。
[charslot(slot="m",name="avg_npc_1242_1#9$1")]
[name="年迈的女性"]老人说的话总是更有道理的。
女性缓缓伸出一只手，手指轻轻地攥着。
[name="年迈的女性"]黍呀......能不能再请你看看我的手相？看看我这个老婆婆，到底还有没有在晚年实现理想的好运气？
[charslot(slot="m",name="avg_2025_shu_1#1$1")]
[name="黍"]我说过，我不会看的。
[charslot(slot="m",name="avg_npc_1242_1#9$1")]
[name="年迈的女性"]......
女性笑着，伸开手掌，掌心里躺着一朵白色的小花。她将花别在眼前女孩的发髻上。
[charslot(slot="m",name="avg_npc_1242_1#9$1")]
[name="年迈的女性"]今天我在田里发现了一朵花，应该是今年开的第一朵，我觉得应该是个好兆头。
[name="年迈的女性"]说不定赶在今年收获的时候，我就能回来了。
[name="年迈的女性"]你掐算着日子，炖好排骨汤等着我就好了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[Sticker(id="st1", text="黍啊......", x=500,y=400, alignment="center", size=22, delay=0.001, width=700,block = true,duration=0.5)]
[Sticker(id="st1",duration=0.5,block = false)]
[Sticker(id="st2", text="嗯？", x=0,y=300, alignment="center", size=22, delay=0.001, width=700,block = true,duration=0.5)]
[Sticker(id="st2",duration=0.5,block = false)]
[Sticker(id="st3", text="你其实一直都能看到那个未来的，对吧？", x=500,y=400, alignment="center", size=22, delay=0.001, width=700,block = true,duration=0.5)]
[Sticker(id="st3",duration=0.5,block = false)]
[Sticker(id="st4", text="......", x=0,y=300, alignment="center", size=22, delay=0.001, width=700,block = true,duration=0.5)]
[Sticker(id="st4",duration=0.5,block = false)]
[Sticker(id="st5", text="你最后......", x=0,y=300, alignment="center", size=22, delay=0.001, width=700,block = true,duration=0.5)]
[Sticker(id="st5",duration=0.5,block = false)]
[Sticker(id="st6", text="别......别告诉我，我可不想知道自己什么时候会死。", x=500,y=400, alignment="center", size=22, delay=0.001, width=700,block = true,duration=0.5)]
[Sticker(id="st6",duration=0.5,block = false)]
[Sticker(id="st6", text="我只是想问问......", x=500,y=400, alignment="center", size=22, delay=0.001, width=700,block = true,duration=0.5)]
[Sticker(id="st6",duration=1,block = false)]
[delay(time=0.5)]
[Sticker(id="st6", text="我们那个万顷良田的梦，最后实现了吗？", x=500,y=400, alignment="center", size=22, delay=0.001, width=700,block = true,duration=1)]
[Sticker(id="st6",duration=1,block = false)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="47_g1_desertedcityfield_d",screenadapt="coverall")]
[charslot(slot="m",name="avg_2025_shu_1#4$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="黍"]......
[dialog]
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[delay(time=1.5)]
[name="疲惫的职农"]天师......
[name="疲惫的职农"]黍姑娘？
[charslot(slot="m",name="avg_2025_shu_1#18$1")]
[name="黍"]欸？
[charslot(slot = "m", focus = "n")]
[name="疲惫的职农"]黍姑娘，我看您在这里愣了半天了，您肯定也不舍得这片地吧。
[charslot(slot="m",name="avg_2025_shu_1#2$1")]
[name="黍"]嗯......
[charslot(slot="m",name="avg_2025_shu_1#1$1")]
[name="黍"]山清水秀，粮食可口......我很喜欢这里。
[charslot(slot = "m", focus = "n")]
[name="疲惫的职农"]黍天师，您看上去这么年轻，调来大荒城没多久吧。
[name="疲惫的职农"]我从出生就在这里，现在都六十七了......六十七年，也从来没想过有一天，还得离开这儿。
[name="疲惫的职农"]听说，从神农她老人家开垦出这片农田，到现在都一千多年了。我们怎么舍得......
[charslot(slot="m",name="avg_2025_shu_1#1$1")]
[name="黍"]庄稼春种秋收，一年也躲不开风霜雨雪。世事不如意才是常态，我们也只能顺其自然。
[name="黍"]以后搬到移动城市里，大家会有别的活计可做，相信会给大家妥善安排的。
[charslot(slot = "m", focus = "n")]
[name="疲惫的职农"]我们就是不明白......本来以为这两年天气差点，所以收成差点，大家加把劲，总能扛过去的。
[name="疲惫的职农"]可现在告诉我们是这块地出了问题......黍姑娘，你们天师懂的多，你能不能再想想办法，救救这块地？
[name="疲惫的职农"]您只要告诉我们一个法子，我们也不怕辛苦，哪怕是要把这块地整个翻一遍——
[charslot(slot="m",name="avg_2025_shu_1#8$1")]
[name="黍"]......
[dialog]
[stopmusic(fadetime=2)]
[charslot]
[delay(time=1.5)]
[name="疲惫的职农"]前两天才下过大雨，这土地怎么......
[dialog]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[playsound(key="$d_avg_dkmgcvlspd")]
[Background(image="47_g1_desertedcityfield_d",screenadapt="coverall",fadetime=4)]
[backgroundTween(xScaleFrom=1.05, yScaleFrom=1.05, xScaleTo=1, yScaleTo=1, duration=3.5, block=false)]
[CameraEffect(effect="Grayscale", fadetime=3, keep=true, initamount=0, amount=1, block=false)]
[delay(time=2)]
田边的职农突然瞪直了眼。
[playsound(key="$d_gen_surfacefrozen")]
田间蓄水以肉眼可见的速度消失，仿佛是地底藏着一个无底的深渊，霎时间抽干了田地间所有水分，也抽走了土地的生命力。
湿润的水田转瞬间变成了板结的盐碱地，长出了无数深不见底的裂纹。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="47_g4_factory_outside",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[

... (全文16120字符)
```

### level_act31side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=2)]
[Background(image="47_g7_fieldhouse",screenadapt="coverall")]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[Delay(time=1)]
就像是做梦一样。
她走过了很长一段路，在冰天雪地中翻山越岭，路的尽头是一片望不到边际的稻田。
丰硕的稻穗像金子一样，黄灿灿的。不知是谁把它们种在了这里，不知为何它们能在这里长得如此繁盛。
真好啊。
“就留在这里吧。”
她听到有一个声音在呼唤她。
不......不。
她还记得，自己还有没做完的事，自己还有要回去的地方。
她拾起一株稻穗。
[dialog]
[Background(image="bg_snow_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_frmrwkhrd")]
[delay(time=1.5)]
[PlaySound(key="$d_avg_snowbootwalk")]
[charslot(slot="m",name="avg_npc_1242_1#8$1",duration=1.5,bstart=0.15,bend=0.5)]
[delay(time=2.5)]
[charslot]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_frmrwkhrd")]
模糊的身影挥舞着锄头，将一粒粒种子埋进地里。
[dialog]
[charslot(slot="m",name="avg_npc_140#2",duration=1)]
[delay(time=1.5)]
[name="忙碌的农民"]您回来了？！太好了，大伙都在等您呢！
[name="忙碌的农民"]您这次走了好久，路上还顺利吗？有没有找到想找的庄稼？
[dialog]
[charslot(slot="m",name="avg_npc_1242_1#8$1",bstart=0.15,bend=0.5)]
[delay(time=0.5)]
[charslot(slot ="m", action="shake", power=6, times=35, duration=0.3)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_140#2")]
[name="忙碌的农民"]老师......您还好吗？您看起来有点......
[dialog]
[MusicVolume(volume=0, fadetime=1)]
[charslot(slot="m",name="avg_npc_140#1")]
[Delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="忙碌的农民"]这......这是什么？！
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="忙碌的农民"]救命——救命！
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="47_g7_fieldhouse",screenadapt="coverall")]
[charslot(slot="l",name="avg_4119_wanqin_1#2$1")]
[MusicVolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="r",name="avg_npc_1240_1#1$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="r",name="avg_npc_1240_1#6$1",focus="r")]
[name="老乡长"]小禾？你怎么还在这？
[charslot(slot="l",name="avg_4119_wanqin_1#9$1",focus="l")]
[name="禾生"]我查到了......
[name="禾生"]污染......不是跟着洪水过来的，污染源应该在地下才对。
[charslot(slot="l",name="avg_4119_wanqin_1#5$1",focus="l")]
[name="禾生"]现在集合天师府的人手，抓紧开始研究应该还来得及！
[charslot(slot="r",name="avg_npc_1240_1#3$1",focus="r")]
[name="老乡长"]别琢磨了。
[charslot(slot="r",name="avg_npc_1240_1#2$1",focus="r")]
[name="老乡长"]已经决定了，要放弃这些地了......
[charslot(slot="l",name="avg_4119_wanqin_1#8$1",focus="l")]
[name="禾生"]不会耽误太多时间的！可能只要两三天，我就能锁定污染来源，肯定会有解决办法的！
[charslot(slot="l",name="avg_4119_wanqin_1#7$1",focus="l")]
[name="禾生"]大荒城每一厘田地都来之不易，我们都还没有努力过，怎么能说放弃就放弃了——
[charslot(slot="r",name="avg_npc_1240_1#1$1",focus="r")]
[name="老乡长"]不是几片地块，是整座大荒城。
[charslot(slot="l",name="avg_4119_wanqin_1#7$1",focus="l")]
[name="禾生"]什么......？
[charslot(slot="r",name="avg_npc_1240_1#1$1",focus="r")]
[name="老乡长"]明天之前，所有人都要搬到核心城上去，跟随核心城向东迁移，其他田地就丢在这了。
[name="老乡长"]其他天师都在着手组织大家搬家的事，这才是现在最要紧的事......你也去帮忙吧。
[charslot(slot="l",name="avg_4119_wanqin_1#8$1",focus="l")]
[name="禾生"]这是......谁的主意？
[charslot(slot="r",name="avg_npc_1240_1#3$1",focus="r")]
[name="老乡长"]能下令让一城搬迁的，你觉得呢？
[charslot(slot="l",name="avg_4119_wanqin_1#8$1",focus="l")]
[name="禾生"]为什么......
[name="禾生"]这些试验田，还有这些才种下去的作物......
[name="禾生"]今年已经是荒年，如果再放弃这些庄稼，会有多少人饿肚子。
[name="禾生"]......就像回到以前的时候。
[charslot(slot="r",name="avg_npc_1240_1#4$1",focus="r")]
[name="老乡长"]我们尽力了。
[name="老乡长"]尽早将人力撤走，尽早准备灾后应对措施。你是天师府的天师，别在这种时候拎不清——
[charslot(slot="l",name="avg_4119_wanqin_1#8$1",focus="l")]
[name="禾生"]神话是真的......？
[charslot(slot="r",name="avg_npc_1240_1#6$1",focus="r")]
[name="老乡长"]说什么傻话......
[charslot(slot="l",name="avg_4119_wanqin_1#8$1",focus="l")]
[name="禾生"]河北岸的冻土，藏着什么东西？就是它们污染了土地，对不对？
[charslot(slot="r",name="avg_npc_1240_1#7$1",focus="r")]
[name="老乡长"]就当是一场天灾。
[name="老乡长"]多少年来，我们保护不了的东西还少吗......
[charslot(slot="l",name="avg_4119_wanqin_1#5$1",focus="l")]
[name="禾生"]大家不会走的。
[name="禾生"]这是我们的土地，不弄明白这里到底发生了什么，大家都不会走的。
[name="禾生"]神农能把这些敌人挡在家园外面，我们也能。
[charslot(slot="r",name="avg_npc_1240_1#2$1",focus="r")]
[name="老乡长"]......
[dialog]
[charslot]
[stopmusic(fadetime=1)]
[delay(time=1)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[Background(image="47_g13_pollutedfield",screenadapt="coverall",fadetime=3)]
[delay(time=1)]
[Background(image="47_g7_fieldhouse",screenadapt="coverall",fadetime=2)]
[delay(time=2.5)]
是幻觉吗？
眼前广袤的田地瞬间变得荒芜。
不，不是田地荒芜，而是这一方天地都被另一片空间侵噬，这已不是人们熟悉的土地。
[charslot(slot="m",name="avg_4119_wanqin_1#7$1")]
[name="禾生"]那边是怎么回事？！
[charslot(slot="m",name="avg_npc_1240_1#8$1")]
[name="老乡长"]来不及了......
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="bg_snow_2",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[PlaySound(key="$d_avg_magic_5")]
[delay(time=1)]
[PlaySound(key="$bodyfalldown2",volume=0.7)]
[PlaySound(key="$d_avg_kneelsnow_s",delay=0.2)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(key="$monastery_sad_loop", volume=0.6)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_140#1",duration=0.5)]
[delay(time=1)]
[name="受惊的农民"]黍姑娘，刚才那到底是什么东西......
[name="受惊的农民"]老师她......生病了吗？她为什么会变成这副模样？
[dialog]
[charslot]
[charslot(slot="m",name="avg_2025_shu_1#16$1",duration=1.5)]
[delay(time=2)]
[name="黍"]......
[charslot(slot="m",name="avg_2025_shu_1#3$1")]
[name="黍"]把她，安葬了吧......
[dialog]
[PlaySound(key="$d_avg_snowbootwalk")]
[charslot(duration=1)]
[delay(time=2)]
一具瘦削的身躯倒在冷硬的土地上，单薄的衣衫口袋里，装着一小袋种子。
[charslot(slot="m",name="avg_npc_140#1")]
[name="受惊的农民"]这是她带回来的种子？她找到传说中的种子了吗？
[name="受惊的农民"]这两年收成实在不好，有了这袋种

... (全文17675字符)
```

### level_act31side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="47_g7_fieldhouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$d_avg_brdchrp")]
几声羽兽啼鸣随着日头的升起传入农舍的窗户，一位母亲睁开惺忪的眼，怀中的孩子正紧紧抓着她的衣摆。
她叹了口气坐起身，想起昨天发生的那些事，还有孩子受惊吓后整晚的哭闹。
幼童察觉到母亲的离开，从睡眠中惊醒，鼻子一抽，眼泪就流下脸庞。父亲熟练地接过孩子，站在窗边轻拍他的背，开始哄睡。
[PlaySound(key="$d_avg_reedmarshes", volume=0, loop=true, channel="reed")]
[SoundVolume(volume=1, fadetime=1,channel="reed")]
“哦，哦，不哭了不哭了，你看窗户外面什么都没有。”
“还是这些田，还是这些花，都好着呢，不哭了不哭了......”
可孩子的哭声渐大，甚至伸出手指向窗外，夫妻二人顺着他的手看向窗外，一头奇异的、惨白的异兽，站在了田埂上。
[dialog]
[backgroundTween(xScaleFrom=1, yScaleFrom=1, xScaleTo=1.05, yScaleTo=1.05, duration=3)]
[playMusic(intro="$plot_intro",key="$plot_loop", volume=0.6)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.1,fadetime=3)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.1,fadetime=3)]
[charslot(slot="m",name="avg_npc_1244_1#3$1",duration=0.01,afrom=0,ato=0,block=true)]
[charslot(slot = "m",action="zoom", poszoom = "0.5,0.5", scale=0.9,duration = 0.01,block=true)]
[charslot(slot="m",duration=3,afrom=0,ato=1)]
[Delay(time=4)]
它回首，看向这一家三口的窗。
[Dialog]
[stopsound(channel="reed",fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[curtain]
[Background(image="47_g8_crestofweir",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1243_1#1$1",duration=1)]
[delay(time=1.5)]
[name="沉默的樵夫"]......
[charslot]
沉默的樵夫拿起了斧子，一缕破碎的红色布带飘过，他抚摸着那粗糙的裂口，似乎想起了什么。
一双有力的长满刀茧的手，不算白净，但骨节分明，混合着血污和泥泞，将一缕红绸系在他的胳膊上，随后毫无生机地落到地面上。
那双手曾举起过沉重的武器，抚摸过他的脸庞，抱过一个啼哭着的孩子。
那双手的主人有着微微黝黑的皮肤，笑起来会露出洁白的牙齿，和一个浅浅的酒窝。
他站在河岸的树林前，树林中系着一条条红绸，红绸下挂着一个个木牌，上面刻着已经模糊的名字。
[PlaySound(key="$d_avg_woodensign", volume=1)]
一阵风吹过，枝干摇晃，木牌阵阵脆响。
[charslot(slot="m",name="avg_npc_1243_1#1$1")]
[name="沉默的樵夫"]嗯......
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$d_avg_hgmgrssvcm")]
一阵诡异的嘶鸣传来，樵夫半睁着浑浊的眼。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1244_1#3$1",duration=1)]
[delay(time=1.5)]
[PlaySound(key="$d_avg_hgmlgscrm")]
[name="诡异的织物"]（尖啸）
[dialog]
[charslot(slot = "l",name="avg_npc_1243_1#3$1",posfrom = "-150,0", posto = "0,0",duration = 0.4)]
[PlaySound(key="$d_avg_singleblunt")]
[PlaySound(key="$d_avg_hammer", volume=0.8)]
[delay(time=0.2)]
[charslot(slot="m",duration=0.3,posfrom = "0,0", posto = "200,0")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.7)]
[PlaySound(key="$d_avg_hgmdspr")]
[charslot(slot="m",afrom=1,ato=0,duration=1)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_1243_1#3$1")]
[name="沉默的樵夫"]——
[charslot(slot = "m", focus = "n")]
它们回来了。
它们不该回来。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="47_g1_desertedcityfield_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$smallearthquake")]
[CameraShake(duration=2.5, xstrength=10, ystrength=5, vibrato=50, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_1249_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_1250_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_1249_1#1$1",focus="l")]
[name="惊慌的职农"]怎么回事？地震了？
[name="惊慌的职农"]移动地块不是还没有建好吗？
[name="惊慌的职农"]那，那又是什么情况？！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot = "left", name = "avg_npc_1251_1#3$1",duration = 1,posfrom = "0,-200", posto = "0,-200")]
[charslot(slot = "right", name = "avg_npc_1251_1#3$1",duration = 1,posfrom = "0,-200", posto = "0,-200")]
[delay(time=1.5)]
[PlaySound(key="$d_avg_drone")]
[charslot(slot ="l", action="shake", power=10, times=100, duration=1)]
[charslot(slot ="r", action="shake", power=10, times=100, duration=1)]
[delay(time=1.1)]
[charslot(slot = "left", name = "avg_npc_1251_1#4$1",duration = 1,posfrom = "0,-200", posto = "0,-100")]
[delay(time=0.5)]
[charslot(slot = "right", name = "avg_npc_1251_1#4$1",duration = 1,posfrom = "0,-200", posto = "0,-100")]
[delay(time=2)]
[charslot(slot = "right", name = "avg_npc_1251_1#5$1",duration = 0.3)]
[PlaySound(key="$d_avg_drone")]
[delay(time=0.3)]
[charslot(slot = "right",duration = 0.5,posfrom = "0,-100", posto = "300,200")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[charslot(slot = "m",posfrom = "0,0", posto = "-200,0")]
[charslot(slot="m",name="avg_npc_1249_1#1$1")]
[charslot(slot="r",name="avg_npc_1250_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "l", name = "avg_npc_1251_1#5$1",duration = 0.1)]
[charslot(slot = "l",duration = 0.5,posfrom = "-500,-200", posto = "-100,200")]
[delay(time=0.1)]
[charslot(slot = "l",duration = 0.3,afrom=1,ato=0)]
[charslot(slot = "r",posfrom = "0,0", posto = "-100,0",duration = 0.3)]
[delay(time=0.3)]
[CameraShake(duration=0.5, xstrength=28, ystrength=26, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r",posfrom = "-100,0", posto = "100,0",duration = 0.5)]
[charslot(slot = "m",posfrom = "-200,0", posto = "0,0",duration = 0.5)]
[delay(time=0.51)]
[charslot(slot="m",name="avg_npc_1249_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_1250_1#1$1",focus="r")]
[name="担忧的职农"]当心！
[charslot(slot="m",name="avg_npc_1249_1#1$1",focus="m")]
[name="惊慌的职农"]好险......我的头......
[name="惊慌的职农"]怎么回事......天桩全都失控了？！
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$d_avg_drone")]
[PlaySound(key="$d_avg_drone",channel="1",delay=0.1)]
[PlaySound(key="$d_avg_drone",channel="2",delay=0.2)]
[PlaySound(key="$d_avg_drone",channel="3",delay=0.3)]
天桩像是受到了某种惊扰，成群从人们头顶掠过，铺天盖地，让人想起许久不曾见过的虫灾。
[charslot(slot="m",name="avg_npc_1249_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_1250_1#1$1",focus="r")]
[name="担忧的职农"]你们看！
[name=

... (全文28235字符)
```

### level_act31side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="47_g8_crestofweir",screenadapt="coverall")]
[playMusic(intro="$suspenseful_intro",key="$suspenseful_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4122_grabds_1#5$1",duration=0.5)]
[Delay(time=1)]
[name="小满"]大叔？
[name="小满"]哑巴大叔？你在哪？
[name="小满"]你别去打那些怪物，快出来！和我一起走！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[charslot(slot="m",name="avg_npc_1244_1#3$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_hgmlgscrm")]
[name="诡异的织物"]（凄厉的长鸣）
[dialog]
[PlaySound(key="$d_avg_hammer", volume=0.8)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[PlaySound(key="$d_avg_hgmdspr")]
[charslot(duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1243_1#3$1",duration=1)]
[delay(time=1)]
[charslot(slot = "m", focus = "n")]
他沉浸在自己的战场里。
他所对战的敌人不可说，他的舌头僵死在口中。
他所爱的人已经离去，看不到下一次春天的到来。
他高高举起自己的武器，他只知道自己好像要保护什么。
保护......什么？
一阵笛声悠悠地传来。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[charslot(slot="m",name="avg_4122_grabds_1#5$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4122_grabds_1#5$1")]
[name="小满"]（努力地吹着笛子）
[charslot(slot="m",name="avg_4122_grabds_1#6$1")]
[name="小满"]大叔！大叔！我在这里！快过来，别在树林里待着了！
[name="小满"]跟我一起走吧！我们回家去！
[PlaySound(key="$d_avg_hgmlgscrm")]
[charslot(slot="m",name="avg_npc_1244_1#3$1")]
[name="诡异的织物"]（尖啸）
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_4122_grabds_1#7$1")]
[name="小满"]——！
[charslot(slot="m",name="avg_4122_grabds_1#6$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="小满"]别以为我怕你！丑东西，滚开——！！
[charslot(slot="m",name="avg_4122_grabds_1#7$1")]
[name="小满"]......啊！
[dialog]
[PlaySound(key="$d_avg_hammer", volume=0.8)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1244_1#3$1")]
[delay(time=1)]
[PlaySound(key="$d_avg_hgmdspr")]
[charslot(duration=1)]
[delay(time=1.5)]
一柄长斧钉在诡异怪物的正胸口，怪物奋力地鼓起身躯，最终丝线脱力地四散，铺在地上。
长斧脱手后，樵夫的手还维持着掷出武器的动作，双眼看不清，他低头侧耳，细细分辨着四周的声音。
[charslot(slot="m",name="avg_4122_grabds_1#7$1")]
[name="小满"]大叔！终于找到你了！
[charslot(slot="m",name="avg_4122_grabds_1#5$1")]
[name="小满"]我在这里！你快过来！我带你去安全的地方！
[charslot(slot = "m", focus = "n")]
樵夫侧耳听了听，向小满的方向望去。
[PlaySound(key="$d_avg_grass")]
随即他再度提起斧子，转身准备走向树林。
[charslot(slot="m",name="avg_4122_grabds_1#7$1")]
[name="小满"]大叔？大叔！前面很危险，你不能回去了！
[charslot(slot="m",name="avg_4122_grabds_1#5$1")]
小满横起笛子，努力平了平气息，吹起了曲子。
[PlaySound(key="$d_avg_relaxflutem",volume=0.6)]
[charslot(duration=0.5)]
花开了，快回家吧♪
你听，你听，是我在呼唤你回来♪
樵夫并没有停下脚步。几头怪物在草丛中俯身，横在小满的身前。
他浑浊的眼睛看不清眼前的事物，天地仿佛在眼前无尽地旋转。他浑身的血液都在轰鸣，他再听不见任何声音。
直到那一声清脆的惊呼像一根针刺入他的耳朵。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="小满"]啊！！
[charslot]
[charslot(slot="m",name="avg_npc_1243_1#4$1")]
[name="沉默的樵夫"]——？！
[charslot]
小满转身想跑，但她随即又横起笛子，更尖锐的笛声传入他的耳朵。
[PlaySound(key="$d_avg_relaxflutem")]
花开了，快回家吧♪
你听，你听，是我在呼唤你回来♪
[charslot(slot="m",name="avg_npc_1243_1#2$1")]
[name="沉默的樵夫"]（......花开了，该回家了......）
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "100,0",duration = 1)]
[delay(time=1)]
他往前迈了一步。
一只白生生的小手牵住了他的手指。
[dialog]
[charslot(slot="l",name="avg_4122_grabds_1#2$1",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1243_1#1$1",focus="m")]
[name="沉默的樵夫"]......
[charslot(slot="l",name="avg_4122_grabds_1#8$1",focus="l")]
[name="小满"]大叔，我们走吧......你不认识回家的路了吗？
[name="小满"]你为什么不想回去？你怕吓到别人是不是？
[name="小满"]我保证，大家不会再怕你了，也不会再把你当怪人了......谁再敢说你的坏话，我挨个用笛子敲他们的头！
[name="小满"]我们一起回去，好吗......
[charslot(slot = "m", focus = "n")]
他臂膀上系着的红绸突然松开，被风吹着一卷，悠悠飞向天空。
樵夫浑浊的眼滚出大滴大滴的泪水，但小满浑然未觉。
[charslot(slot="m",name="avg_npc_1243_1#2$1",focus="m")]
[name="沉默的樵夫"]......
[dialog]
[charslot(slot = "r",name="avg_npc_1244_1#3$1",posfrom = "500,0", posto = "400,0",duration = 1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1243_1#7$1",focus="m")]
[name="沉默的樵夫"]——？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="l",name="avg_4122_grabds_1#6$1",focus="l")]
[name="小满"]大叔，快跑——
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="47_g13_pollutedfield",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$escape_intro",key="$escape_loop", volume=0.6)]
[delay(time=1)]
[charslot(slot="m",name="avg_4121_zuole_1#4$1",duration=0.5)]
[delay(time=0.5)]
[playsound(key="$e_skill_skulsrsword", volume=0.7)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_hgmdspr")]
[charslot(duration=0.5)]
[delay(time=1)]
[charslot]
[charslot(slot="m",name="avg_4119_wanqin_1#5$1",duration=0.5)]
[delay(time=0.5)]
[playsound(key="$d_avg_punch", volume=0.7)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_hgmdspr")]
[charslot(duration=0.5)]
[delay(time=1)]
[charslot]
[charslot(slot = "r",name="avg_4119_wanqin_1#5$1",posfrom = "150,0", posto = "0,0",duration = 0.5)]
[charslot(slot = "l",name="avg_4121_zuole_1#4$1",posfrom = "-150,0", posto = "0,0",duration = 0.5)]
[delay(time=1)]
[charslot(slot = "r",name="avg_4119_wanqin_1#5$1",focus="r")]
[name="禾生"]到底还有多少......这些怪物真的杀不完吗？
[charslot(slot = "l",name="avg_4121_zuole_1#4$1",focus="l")]
[name="左乐"]只能尽量把它们挡在这里......
[charslot(slot = "r",name="avg_41

... (全文16951字符)
```

### level_act31side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$chenandwei_intro",key="$chenandwei_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_gateopen")]
[Delay(time=2)]
暗无天日。
不知地深几许，没有半点阳光透进来，空气也凝重得仿佛能感受到穹顶的重量。
这是一座陵墓。
[dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avgnew_2014_nian_1#8$1",duration=1.5)]
[delay(time=2)]
[name="年"]啥情况......我回这来了？
[charslot(slot="m",name="avgnew_2014_nian_1#1$1")]
[name="年"]喂，老东西，还活着么？我来看看你啦。
[charslot]
[playsound(key="$d_avg_gintcrturnhle")]
[name="低沉的声音"]（喑哑的嘶吼）
眼前是一扇厚重的大门，声音是从门后传来的。
[charslot(slot="m",name="avgnew_2014_nian_1#1$1")]
[name="年"]睡了这么久，火气是半点都没少啊......
[name="年"]别装模作样吓唬人了，在这里躺了这么长时间，你真的还剩下什么能耐吗？
[charslot(slot="m",name="avgnew_2014_nian_1#6$1")]
[name="年"]呼......
[name="年"]没啥子好怕的......吧。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[PlaySound(key="$d_avg_gatecloz")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_snowstormflp", volume=0.6, loop=true, channel="bgs")]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avgnew_2014_nian_1#8$1",duration=1)]
[delay(time=1.5)]
[name="年"]尚蜀？
[name="年"]这是哪座山头，怎么连块路牌都没有......不对，这是哪一年？
[name="年"]看这路上两边的房子，像是没有移动地块的样子......怎么像是我刚来尚蜀的时候？
[charslot(slot = "m", focus = "n")]
叮——当——
一人正用绳子将自己悬在陡峭的山崖上，用一锤一凿在悬壁上刻下一行行字。
[charslot(slot="m",name="avgnew_2014_nian_1#1$1")]
[name="年"]喂——山上那兄弟，你做啥子呢？
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1245_1#1$1",duration=1)]
[delay(time=1.5)]
[name="土木天师"]你不认识我？！
[charslot(slot="m",name="avgnew_2014_nian_1#5$1")]
[name="年"]我为什么要认识你？
[charslot(slot="m",name="avg_npc_1245_1#1$1")]
[name="土木天师"]这整座尚蜀城都是在我的设计下建造出来的！
[charslot(slot="m",name="avgnew_2014_nian_1#1$1")]
[name="年"]喔，厉害厉害。
[charslot(slot="m",name="avg_npc_1245_1#1$1")]
[name="土木天师"]天灾就要来了，人都已经撤走了。但我建造的这些屋子，都要毁于这场天灾。
[name="土木天师"]我不甘心！
[charslot(slot="m",name="avgnew_2014_nian_1#8$1")]
[name="年"]靖炎五年，余至尚蜀，历三十载......《尚蜀城记》？
[charslot(slot="m",name="avg_npc_1245_1#1$1")]
[name="土木天师"]我要把我建造这座城的过程全部刻在这山崖上，让后世亿兆百姓全部记得我的功绩！
[charslot(slot="m",name="avgnew_2014_nian_1#8$1")]
[name="年"]可是天灾马上就要来了哎，就算你不惜命，一道天雷劈下来，这座山头都不一定保得住，你这不是白费功夫？
[charslot(slot="m",name="avg_npc_1245_1#1$1")]
[name="土木天师"]管不了那么多了，我就只有这一个法子。要是没人知道我的作为，我还不如不活了！
[charslot(slot="m",name="avgnew_2014_nian_1#5$1")]
[name="年"]哪有这样的人......行吧，你接着忙活，我不打扰了哈。
[charslot(slot="m",name="avgnew_2014_nian_1#1$1")]
[name="年"]喂，山上这条路最后通到哪儿啊？
[charslot(slot="m",name="avg_npc_1245_1#1$1")]
[name="土木天师"]不知道。
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="bg_indoor",screenadapt="coverall")]
[PlaySound(key="$d_avg_gatecloz")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avgnew_2014_nian_1#8$1",duration=1)]
[delay(time=1.5)]
[name="年"]是你......
[charslot(slot = "m", focus = "n")]
[name="盲眼的少年剑客"]恳请先生赐剑。
[charslot(slot="m",name="avgnew_2014_nian_1#8$1")]
[name="年"]要剑，做什么？
[charslot(slot = "m", focus = "n")]
[name="盲眼的少年剑客"]救人，报仇。
[charslot(slot="m",name="avgnew_2014_nian_1#1$1")]
[name="年"]我说过，我铸的剑很贵的，你用什么换？
[charslot(slot = "m", focus = "n")]
[name="盲眼的少年剑客"]我的命。
[charslot(slot="m",name="avgnew_2014_nian_1#8$1")]
[name="年"]又来......
[name="年"]......我应该已经拒绝了你。
[charslot(slot = "m", focus = "n")]
[name="盲眼的少年剑客"]......
[charslot(slot="m",name="avgnew_2014_nian_1#7$1")]
[name="年"]你记不记恨我，当年用一把破铜烂铁就打发了你？
[charslot(slot="m",name="avgnew_2014_nian_1#6$1")]
[name="年"]......我在说什么，不过是个幻影。
[charslot(slot = "m", focus = "n")]
[name="盲眼的少年剑客"]可是您偏偏还记得我。
[charslot(slot="m",name="avgnew_2014_nian_1#6$1")]
[name="年"]只是惦记着电影剧本的原型故事......还是忍不住会想，要是当时真的送你一把好剑，故事结局会不会有什么不一样。
[charslot(slot = "m", focus = "n")]
[name="盲眼的少年剑客"]像您这样神通广大、见识无数的人，又怎会对我这样的无名之辈抱有恻隐之心呢？
[name="盲眼的少年剑客"]区区一个人类的命，对您来说，确实太不值钱了。
[charslot(slot="m",name="avgnew_2014_nian_1#7$1")]
[name="年"]也不能说得这么过分吧，我还是很喜欢你们人类的。
[charslot(slot = "m", focus = "n")]
[name="盲眼的少年剑客"]您看我们，就像看戏。
[name="盲眼的少年剑客"]您的随性之举，就能为这出戏添一处奇景，改变无数人的命运。到兴起的时候，您甚至也想加入进来，唱上几句。
[name="盲眼的少年剑客"]可戏里风景千万，唯独您不在戏中。
[name="盲眼的少年剑客"]您始终孤身一人。
[charslot(slot="m",name="avgnew_2014_nian_1#2$1")]
[name="年"]真是，看走马灯这件事也能落到我的身上......
[charslot(slot="m",name="avgnew_2014_nian_1#7$1")]
[name="年"]乏了，这把剑是认真打的，你带走吧。
[name="年"]就让我看看，故事结局还有没有什么变数。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", focus = "n")]
[name="老人"]先生，有一个少年，托我一定在今年冬至日前，把这个包裹交给您。
[charslot(slot="m",name="avgnew_2014_nian_1#8$1")]
[name="年"]他不敢亲自来见我？
[charslot(slot = "m", focus = "n")]
[name="老人"]他应该，已经死了......
包裹是空的。
[charslot(slot="m",name="avgnew_2014_nian_1#6$1")]
[name="年"]......
[dialog]
[charslot]
[delay(time=1)]
[Dialog]
[CameraShake(duration=3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_collapse")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[Subtitle(text="国蚀器锈，如梦似电，无踪泡影。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[PlaySound(key="$dooropenquite")] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(key="$midautumn", volume=0.6)]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avgnew_2015_dusk_1#1$1",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avgnew_2015_dusk_1#9$1")]
[name="夕"]这是......？
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_799_1#1$1",duration=1)]
[delay(time=1.

... (全文16286字符)
```

### level_act31side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="47_g13_pollutedfield",screenadapt="coverall")]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4119_wanqin_1#5$1",duration=0.5)]
[delay(time=1)]
[name="禾生"]数量还是太多了......对付不过来......
[name="禾生"]外围的田地，恐怕都要保不住了。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1244_1#3$1")]
[delay(time=0.3)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_skill_skulsrsword")] 
[delay(time=0.5)]
[playsound(key="$d_avg_hgmscrmh")]
[charslot(duration=0.8)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4121_zuole_1#4$1",duration=0.3)]
[delay(time=0.3)]
[name="左乐"]情况紧急，优先救人......
[charslot(slot="m",name="avg_4119_wanqin_1#8$1")]
[name="禾生"]是错觉吗，总觉得......它们闹得好像没有之前凶了。
[charslot(slot = "m", focus = "n")]
[CameraShake(duration=3, xstrength=15, ystrength=15, vibrato=50, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_rampartclose",volume=0.3)] 
[dialog]
[charslot(slot="m",name="avg_npc_1244_1#3$1")]
[delay(time=0.5)]
[charslot(duration=0.8)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4119_wanqin_1#7$1")]
[name="禾生"]什么动静？
[charslot(slot="m",name="avg_4121_zuole_1#4$1")]
[name="左乐"]这里的地块，正在从核心城上脱离......
[name="左乐"]果然......这些怪物的生命力与大荒城的核心城是绑定的，断开了连接，它们的力量也在衰弱。
[charslot(slot="m",name="avg_4121_zuole_1#5$1")]
[name="左乐"]坚持住！大家都撤到这里来了吗？
[charslot(slot="m",name="avg_4119_wanqin_1#5$1")]
[name="禾生"]通知都已经送到了，各区域的人都到齐了吗？
[charslot(slot="m",name="avg_npc_1249_1#1$1")]
[name="职农组长甲"]子至卯号居民区人员到齐。
[charslot(slot="m",name="avg_npc_1250_1#1$1")]
[name="职农组长乙"]申至亥号居民区人员到齐！
[charslot(slot="m",name="avg_npc_1249_1#1$1")]
[name="职农组长丙"]巳至未号居民区人员到齐，派去辰号居民区的人还没有消息。
[charslot(slot="m",name="avg_4119_wanqin_1#6$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="禾生"]什么？！
[charslot(slot="m",name="avg_npc_1249_1#1$1")]
[name="职农组长丙"]从中央城区到辰号居民区的路上，有一片农田受到怪物袭击的情况格外严重，派出去的救援队也失去联络了。
[charslot(slot="m",name="avg_4119_wanqin_1#8$1")]
[name="禾生"]现在核心城能源装置故障，联络系统也瘫痪了......
[dialog]
[charslot(slot="m",name="avg_4119_wanqin_1#5$1")]
[charslot(slot = "m",posfrom = "0,0", posto = "200,0",duration = 0.8)]
[name="禾生"]我去找人！
[charslot(slot="l",name="avg_4121_zuole_1#4$1",focus="l")]
[name="左乐"]等等！
[name="左乐"]每次都是你拉着我不要逞能，怎么你跑得比谁都快。谁知道别处还有多少怪物，你打算一个人去？
[charslot(slot="m",name="avg_4119_wanqin_1#5$1",focus="m")]
[name="禾生"]那里是我的试验田，没人比我更熟路线！
[charslot(slot="m",name="avg_4119_wanqin_1#9$1",focus="m")]
[name="禾生"]留在那里的，都是平时受我委托帮我照顾农田的职农。我还骗了他们，说我的研究最近大有进展......
[charslot(slot="l",name="avg_4121_zuole_1#4$1",focus="l")]
[name="左乐"]要去也行，带我一个。我跑得快，还能拉你一把。
[charslot(slot="m",name="avg_4119_wanqin_1#5$1",focus="m")]
[name="禾生"]你是外地来的，这里的事原本和你没关系，你还比我小一岁——
[charslot(slot="l",name="avg_4121_zuole_1#4$1",focus="l")]
[name="左乐"]“......禾生，1101年晋升天师府中级农业天师，时年十七岁。”
[charslot(slot="m",name="avg_4119_wanqin_1#7$1",focus="m")]
[name="禾生"]你——
[charslot(slot="l",name="avg_4121_zuole_1#4$1",focus="l")]
[name="左乐"]来大荒城查资料的时候，翻过天师府的名册，算下来，你比我小一岁。
[name="左乐"]禾生兄弟，危难关头，勿要逞强。
[charslot(slot="m",name="avg_4119_wanqin_1#5$1",focus="m")]
[name="禾生"]*炎国粗口*，你平时都这么讲话吗？
[charslot(slot="l",name="avg_4121_zuole_1#5$1",focus="l")]
[name="左乐"]*炎国粗口*，我从来没这样讲过话！
[charslot(slot="l",name="avg_4121_zuole_1#4$1",focus="l")]
[name="左乐"]少废话，一起走！
[stopmusic(fadetime=2)]
[PlaySound(key="$rungeneral")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=2)]
[Background(image="47_g10_fairyfarmland_ex",screenadapt="coverall")]
[PlaySound(key="$d_avg_reedmarshes", volume=0, loop=true, channel="reed")]
[SoundVolume(volume=0.5, fadetime=2,channel="reed")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[delay(time=1)]
神话是一个谎言吗？
迷离的稻田绵延到天边，这是一片生命的沃野。
长风吹彻，稻浪如歌。
一个初生的意识在此孕育，有一个声音向她搭话。
[Dialog]
[delay(time=1)]
[name="混沌的意识"]你回来了。
[name="混沌的意识"]你看上去很疲惫，你还好吗？
[dialog]
[charslot(slot="m",name="avg_2025_shu_1#1$1",duration=1)]
[delay(time=1.5)]
[name="黍"]原来......你已经醒了。
[charslot]
[name="混沌的意识"]这是哪里？我从一开始就在这里吗？
[name="混沌的意识"]为什么，有很久远的记忆。
[name="混沌的意识"]我看到了许多......
战乱，死亡，疫病，饥馑......
来自穹顶之上的灾异翻洗整片大地，满目疮痍，之后又是无止尽的战乱动荡。
文明毁灭，生灵恐惧。
为什么我会被困在这里？
我到底是谁？
[name="混沌的意识"]我觉得，很害怕。
[name="混沌的意识"]外面，很恐怖。
[name="混沌的意识"]痛苦。
[name="混沌的意识"]我听到，有许多人在哭。
怎样才能不再这样痛苦下去。
我想起来了，有人给我起了名字......
[dialog]
[delay(time=1)]
“岁”。
[dialog]
[stopmusic(fadetime=1)]
[delay(time=2)]
[name="狰狞的声音"]我就是你。
[dialog]
[stopsound(channel="reed",fadetime=1)]
[PlaySound(key="$d_avg_monsteroar", volume=1)]
[CameraShake(duration=2, xstrength=10, ystrength=10, vibrato=90, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=0.3, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
杂草疯长，淹没了所有土地。
万古长夜凝结在这一瞬。
[Dialog]
[charslot]
[delay(time=2)]
[image(image="47_i09",screenadapt="coverall",xScale=1.1, yScale=1.1,x=0,y=30)]
[ImageTween( xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1,  yTo=0, duration=20)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$storyendjp_intro",key="$storyendjp_loop", volume=0.6)]
[delay(time=1)]
[name="黍"]......
[name="黍"]不，你只是一个影子......是我自己的影子。
[name="黍"]这些并非你的痛苦，是生活在这片土地上的人的痛苦。
[name="狰狞的声音"]不——
[name="黍"]你在害怕，因为你不曾真的活过，你不知道这片大地真实的样子。
[name="黍"]这世间并不可怕。
可是你不曾见过庄稼丰收，人们欢声笑语的样子。
你不曾见过万类竞生，历经磨难，却依然生生不息的样子。
如果有机会，你应当仔细看看。
我早已不是那傲慢孤寂的巨兽，也并非飘荡无依的游魂。
我已真实地活过，与大地上万千生灵一同。
[PlaySound(key="$d_avg_dripink", volume=0.7)]
一滴露水滴下，为大地注入跨越无数时间的生命。
[name="黍"]睡吧。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="霞红晚穗，", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="露染尘襟，", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="千秋种我一粟青。", x=300, y=3

... (全文20990字符)
```

### level_act31side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[Background(image="35_g11_yumendesert",screenadapt="coverall")]
[playMusic(key="$calm_loop", volume=0.6)]
[Delay(time=2)]
[Subtitle(text="原来那些渺小生灵眼中的天地，是这副模样。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraEffect(effect="Grayscale", fadetime=2, amount=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="从那片混沌蒙昧中脱身走出，初次行走在苍茫大地上。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我从何而来，往何处去？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="保留着那副庞大身躯的记忆，还有一些神乎其神的能力，以及有别于眼前芸芸众生的寿命。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但也只得像懵懂孩童，跟着眼前众人，有样学样。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="岁月漫长，我遇到过两位老师。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_2025_shu_1#9$1",duration=1)]
[delay(time=1.5)]
[name="黍"]在炎国的北边，有一片荒地。
[name="黍"]我和那里的人们正试着开垦农田。看着一棵棵庄稼从地里长出来，也是十分有趣。不知道该去哪，要不要来这里帮我打打下手？
[dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="那里是什么样的地方？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot(slot="m",name="avg_2025_shu_1#2$1")]
[name="黍"]嗯......比起这些城镇要荒凉许多，再加上还有些许从那扇门里跑出来的东西，有点危险。
[charslot(slot="m",name="avg_2025_shu_1#9$1")]
[name="黍"]不过你要是想知道，“人”是什么样的，那里说不定是个不错的地方。
[name="黍"]时间还长，可以慢慢找答案。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="bg_snow_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="我第一次知道，原来生命间还有“同胞”这样的概念。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="或许这就是他们能战胜那些庞然大物的原因？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_npc_1242_1#12$1",duration=1)]
[delay(time=1.5)]
[name="辛劳的农民"]真是稀奇，昨晚冰雹下那么大，这些庄稼看上去竟然一点事都没有。
[charslot(slot = "m", name = "avg_npc_1236_1#9$1")]
[name="绩"]或许是运气好呢？老天看大家种地辛苦，发了点善心呢？
[charslot(slot="m",name="avg_npc_1242_1#12$1")]
[name="辛劳的农民"]绩，是你做的吧？
[charslot(slot = "m", name = "avg_npc_1236_1#6$1")]
[name="绩"]......
[charslot(slot = "m", name = "avg_npc_1236_1#7$1")]
[name="绩"]我只是觉得，大家辛辛苦苦劳作半年，就因为这一场冰雹毁于一旦，实在是可惜......
[charslot(slot="m",name="avg_npc_1242_1#12$1")]
[name="辛劳的农民"]世间万物都有自己的运行规律，一季庄稼毁了，埋在地里，还能化作土地的肥料，来年的庄稼可以长得更好。
[name="辛劳的农民"]你救得了这片地的这一季庄稼，可炎国有多少片这样的农田，有多少靠天吃饭的人。
[name="辛劳的农民"]你是好心，但人们总要靠自己研究出在这片土地上找活路的办法......
[charslot(slot = "m", name = "avg_npc_1236_1#3$1")]
[name="绩"]有一天，您也会离去吗？
[charslot(slot="m",name="avg_npc_1242_1#12$1")]
[name="辛劳的农民"]当然。
[name="辛劳的农民"]但这片土地会永远存在，生命会永远存在。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_mini01_villagevacancy",screenadapt="coverall")]
[Subtitle(text="天地万物，都有各自的位置。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可是我们生于天地间，如无根之木，无水之萍。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="无因无果，无始无终。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我们又该归于何处？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1.5)]
[Subtitle(text="时过境迁。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$tech_intro",key="$tech_loop", volume=0.6)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1236_1#9$1",duration=1)]
[delay(time=1.5)]
[name="绩"]您是来收粮食的商人？
[charslot(slot = "m", focus = "n")]
[name="精明的商人"]今年各地大旱，听说北边这里的粮仓还有余裕。我来进点粮食，卖到粮食更紧张的地方去。
[charslot(slot = "m", name = "avg_npc_1236_1#8$1")]
[name="绩"]天地不仁风雨不调，实在是苦了这些农民。
[charslot(slot = "m", focus = "n")]
[name="精明的商人"]可是荒年，对农民来说未必不是好事。
[charslot(slot = "m", name = "avg_npc_1236_1#7$1")]
[name="绩"]先生莫不是在说梦话，荒年对农民来说怎么能是好事？
[charslot(slot = "m", focus = "n")]
[name="精明的商人"]多简单的道理，越是荒年，粮食越贵。
[name="精明的商人"]每斤粮食赚一文，卖五百斤，和每斤粮食赚十文，卖一百斤。这笔账三岁小孩都算得清楚。
[charslot(slot = "m", name = "avg_npc_1236_1#7$1")]
[name="绩"]我从小就生活在这，只知道粮食是用来喂饱百姓，救人性命的。
[name="绩"]外面的天地，竟还有这样的道理。
[charslot(slot = "m", focus = "n")]
[name="精明的商人"]你又没见过大荒城外的世面，并非人人都是临渊忘水的神人，只是守着这几亩田地，哪能悟出天下那么多道理。
[name="精明的商人"]小伙子，我的商队正好缺一个管事，你有没有兴趣，跟我一块去走走？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$dooropenquite")]
[charslot(slot = "m", name = "avg_npc_797_1#1$1",duration=0.5)]
[delay(time=1)]
[name="茶叶商贩"]住店。
[charslot(slot = "m", focus = "n")]
[name="精明的商人"]老规矩，货存仓库，先结账，再住店。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot = "m", name = "avg_npc_1236_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="绩"]这两年尚蜀开出来不少茶田，您说要来做茶叶生意。怎么只是在这包下了这一片客栈？
[charslot(slot = "m", focus = "n")]
[name="精明的商人"]一车最上品的“蜀山青”，从这里运到百灶，能赚多少钱，朝廷抽几成税？
[charslot(slot = "m", name = "avg_npc_1236_1#1$1")]
[name="绩"]一路上要是平安顺利，能有两成毛利——已经是相当好做的买卖。
[charslot(slot = "m", focus = "n")]
[name="精明的商人"]可是这来来往往，不愿意老实纳税的茶商都要从这条小路上走，我又能抽多少钱？
[charslot(slot = "m", name = "avg_npc_1236_1#3$1")]
[name="绩"]这样看来，还是您做的这笔买卖划算......
[charslot(slot = "m", name = "avg_npc_1236_1#1$1")]
[name="绩"]可我分明看到，您扣过一些货物交给了官府？
[charslot(slo

... (全文14151字符)
```

### level_act31side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_snow_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[Delay(time=2)]
谁料到会有这样的一场雪？
田垄上厚厚地覆盖着一层令人绝望的白，星星点点的黄色，是月前刚刚种下的麦子艰难地探出的头。
一旬后还能活下几株？叫人不敢想。
[playsound(key="$d_avg_pawfootstep_3")]
[playsound(key="$d_avg_pawfootstep_1",delay=0.15,channel="2")]
一只鼷兽东奔西走，跌跌撞撞来到这片寂静的麦田。
眼前稀稀拉拉的庄稼对它来说算是意外之喜，它小心地嗅闻着，盘算着多少够填饱一半自己的肚子，还有多少够带回洞穴里喂养同族。
[dialog]
[CameraShake(duration=0.2, xstrength=10, ystrength=30, vibrato=20, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$d_avg_frmrwkhrd")]
[PlaySound(key="$d_avg_smallbeastscream",delay=0.5,channel="1")]
直到一柄粗铁锄头落在它的脊柱上。
又少了三株麦子。
气愤的农夫抓住了那只糟蹋庄稼的畜生，恨不得将其扒皮啖肉，可瘦得只剩骨头的尸体拎在手里也没有几两重。
农夫悠长地叹了口气，把鼷兽的尸体埋进了地里。
[dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="？？？"]多可怜。
[name="黍"]风雨无常，总有这样的时候。
[name="？？？"]如果这些麦子死于这场雪，来年有多少人会死于荒灾？
[name="黍"]很多。
[name="黍"]但也会有很多人帮助他们，会有很多人幸存下来。
[name="黍"]生命本身不会断绝。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="47_g16_beautifulland",screenadapt="coverall")]
[playMusic(intro="$prisonbreak_intro",key="$prisonbreak_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$tactfulboost")]
[CameraShake(duration=1, xstrength=18, ystrength=26, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.8, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=0.8, r=1, g=1, b=1, fadetime=0.1, block=true)]
[PlaySound(key="$p_imp_ancientsword_d")]
[Blocker(a=0.8, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
天穹如幕。
飘渺的绸缎似有千钧之重，牢牢地隔开了二人的攻击，向二人压去。
[Dialog]
[Blocker(a=0.7, r=1, g=1, b=1, fadetime=0.02, block=true)]
[CameraShake(duration=1, xstrength=18, ystrength=6, vibrato=10, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_jghtket")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1236_1#1$1",duration=0.5)]
[delay(time=1)]
[name="绩"]年，收手吧。
[name="绩"]帮你造好这个心脏也算费了不少力气，再打下去，把它拆了，前功尽弃多不划算？
[charslot]
[charslot(slot="l",name="avgnew_2014_nian_1#3$1",focus="l")]
[charslot(slot="r",name="avgnew_2015_dusk_1#5$1",focus="l")]
[name="年"]你也不见得有功夫说闲话吧，刚才那个炮仗明明差一点就炸到你了。
[charslot(slot="r",name="avgnew_2015_dusk_1#5$1",focus="r")]
[name="夕"]怎么不见你在我的画里到处搞破坏的力气呢？你就不能铸把大号剪刀把他的那几匹布剪碎？
[charslot(slot="l",name="avgnew_2014_nian_1#8$1",focus="l")]
[name="年"]你倒是出点力气啊！你的画都要被他变成刺绣了！
[charslot(slot="r",name="avgnew_2015_dusk_1#6$1",focus="r")]
[name="夕"]你还说我——？
[charslot(slot="l",name="avgnew_2014_nian_1#3$1",focus="l")]
[name="年"]有点难啊，刚造好一个大号的炮仗就被他拆成线了，原来他一直能做到这种事的么？
[name="年"]我还以为这些年他不会有心思用在钻研能力上呢。
[charslot(slot="r",name="avgnew_2015_dusk_1#9$1",focus="r")]
[name="夕"]可是为什么，他好像对我们的能力都这么熟悉......
[name="夕"]慢着，他那边，真的只有一个人吗？
[charslot]
[charslot(slot = "m", name = "avg_npc_1236_1#3$1")]
[name="绩"]时间差不多了......
[charslot(slot = "m", name = "avg_npc_1236_1#9$1")]
[name="绩"]难得的聚会，本来确实想再多聊聊，可时间实在是有点紧张，还是容我先告辞了。
[name="绩"]实在不想动这个手的，下次有机会再见的话，再给你们赔礼道歉吧。
[name="绩"]如果还有机会的话......
[dialog]
[charslot]
[MusicVolume(volume=0.2, fadetime=2)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=10, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_jghtken")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[Background(image="bg_black",screenadapt="coverall")]
[PlaySound(key="$d_avg_lmrgcwnd")]
[Blocker(a=0.1, r=0, g=1, b=0.3, fadetime=1.5, block=false)]
[delay(time=0.5)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=1, block=true)]
[Background(image="47_g10_fairyfarmland_ex",screenadapt="coverall",fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[MusicVolume(volume=0.6, fadetime=2)]
[PlaySound(key="$d_avg_grass")]
[charslot(slot = "m",name = "avg_2025_shu_1#5$1",duration=1)]
[delay(time=1.5)]
[name="黍"]对妹妹也下得去手，太不像话了吧。
[charslot]
[charslot(slot="l",name="avgnew_2014_nian_1#5$1",focus="l")]
[charslot(slot="r",name="avgnew_2015_dusk_1#1$1",focus="l")]
[name="年"]黍姐？
[charslot(slot="l",name="avgnew_2014_nian_1#8$1",focus="l")]
[name="年"]虽然猜到你不至于就这样消失......你真的没事？
[charslot(slot="r",name="avgnew_2015_dusk_1#9$1",focus="r")]
[name="夕"]你最好不是在故意吓唬我们......
[charslot]
[charslot(slot = "m",name = "avg_2025_shu_1#9$1")]
[name="黍"]就当久违地做了一个长点的梦吧。抱歉，让你们担心啦。
[charslot(slot = "m",name = "avg_2025_shu_1#5$1")]
[name="黍"]还是要来看看我这个弟弟，难得回来一次就闹这么一场，是真的不把这里当家了？
[charslot(slot = "m", name = "avg_npc_1236_1#7$1")]
[name="绩"]......姐姐。
[charslot(slot = "m",name = "avg_2025_shu_1#5$1")]
[name="黍"]你每次做错了事，脸上都会是这个表情。
[name="黍"]有多久了？
[charslot(slot = "m", name = "avg_npc_1236_1#2$1")]
[name="绩"]......整六十七年。
[charslot(slot = "m",name = "avg_2025_shu_1#5$1")]
[name="黍"]那今天必须要留下来吃顿饭了，有什么话都可以饭桌上慢慢聊。
[charslot(slot = "m", name = "avg_npc_1236_1#1$1")]
[name="绩"]对不起姐姐。这一次，我不能听话了。
[charslot(slot = "m",name = "avg_2025_shu_1#2$1")]
[name="黍"]是听了另一位的话吧......
[name="黍"]一直躲起来的那位，还打算躲到什么时候？
[charslot(slot = "m",name = "avg_2025_shu_1#5$1")]
[name="黍"]有什么话，直接对我来说不好吗？
[dialog]
[charslot(duration=0.5)]
[stopmusic(fadetime=1)]
[delay(time=2)]
[bgeffect(name="$eb_cnclouds",layer=1,fade = true,fadetime=2)]
[PlaySound(key="$d_avg_reedmarshes", volume=0, loop=true, channel="reed")]
[SoundVolume(volume=1, fadetime=1,channel="reed")]
[Background(image="47_g9_fairyfarmland",screenadapt="coverall",xScale=1.03,yScale=1.03, fadetime=2.5)]
[delay(time=2.5)]
[stopsound(channel="reed",fadetime=2)]
[Background(image="47_g10_fairyfarmland_ex",screenadapt="coverall",xScale=1.03,yScale=1.03,fadetime=2.5)]
一人自远处缓缓走来，走过了亘古的时间。又仿佛他从一开始就在这里。
[PlaySound(key="$d_avg_hidehaystack")]
时间与空间随着他的足音静止。
[dialog]
[playMusic(intro="$chenandwei_intro",key="$chenandwei_

... (全文25921字符)
```

### level_act31side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act31side/HS01.mp4")]
```

### level_act31side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
哪里能见到这样一片农田？
稻子疯了似的长，齐刷刷笔挺挺地直立着，像是牧兽秋后的毛。风一吹，太阳一烤，便泛起热腾腾的浪来。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_reedmarshes", volume=0, loop=true, channel="grass")]
[SoundVolume(volume=0.3, fadetime=3,channel="grass")]
[charslot]
[Image(image="47_i01",screenadapt="coverall",fadetime=0,block=true)]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[Delay(time=1)]
女人站在田地中央，乱蓬蓬的枝叶不住拉扯着她的衣摆。她拨开茎秆，向浩瀚的金黄深处走去，像是穿越一片海。
[name="稚嫩的童声"]上哪去？
[name="温柔的女性"]找庄稼。
[name="稚嫩的童声"]这不是遍地都是庄稼？
[name="温柔的女性"]要找能种到更远的地方去的庄稼。
[name="稚嫩的童声"]为什么要到别的地方种庄稼？这儿有这么多，还不够？
[name="温柔的女性"]这些庄稼，喂不饱所有人。
[name="稚嫩的童声"]......
[name="稚嫩的童声"]你在这，找多久了？
[Dialog]
[Delay(time=1)]
[PlaySound(key="$d_avg_sandftsingle",volume=0.2)]
[PlaySound(key="$d_avg_sandftsingle", volume=0.2, loop=false, channel="bgs1",delay=0.6)]
沙沙。
一只鼹兽从地洞里探出头来，阴暗的坑洞应该连接到了很远的地方，渺小的生物也是漂泊的外来客。
直到它看见了这片无边际的田野，像是被这种宽广深深地震撼了，它悲哀地叹了一口气，又折回了暗无天日的地底。
......
[Dialog]
[Delay(time=1)]
[name="稚嫩的童声"]我们怎么知道，种子种下去会发芽？怎么预知天气的变化？
[name="温柔的女性"]看得多了，自然就知道了。
[name="稚嫩的童声"]看多了就能知道......包括发生在很久以后的事？
[name="温柔的女性"]种瓜得瓜，种豆得豆。
[name="稚嫩的童声"]庄稼是种子变的，“我们”又是什么变的？
[name="稚嫩的童声"]我们从哪里来？死后又会到哪儿去？
[name="温柔的女性"]我们是从大地里长出的，死了以后也会回到地里去。
[name="温柔的女性"]人和庄稼，都一样。天地万物，都在轮回。
[name="稚嫩的童声"]就像你教我的那首歌？
[Dialog]
[StopSound(channel="grass", fadetime=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[charslot]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Sticker(id="st1", multi = true, text="春雨惊春清谷天，夏满芒夏暑相连。", x=300,y=300, alignment="center", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n秋处露秋寒霜降，冬雪雪冬小大寒。",block = true)]
[Sticker(id="st1")]
[Delay(time=1)]
......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_nhvyprtn",volume=0.7)]
[Delay(time=1)]
[name="？？？"]喂——
[name="？？？"]喂————
[name="？？？"]醒一醒。
[name="温柔的女性"]......
[Dialog]
[charslot(slot="m",name="avgnew_2014_nian_1#8$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avgnew_2014_nian_1#8$1",focus="m")]
[name="年"]老姐？
[charslot(slot="m",name="avgnew_2014_nian_1#8$1",focus="n")]
[name="黍"]嗯......我在。
[charslot(slot="m",name="avgnew_2014_nian_1#8$1",focus="m")]
[name="年"]情况咋样？从外面看，这“大家伙”好像还不是很听话的样子。
[charslot(slot="m",name="avgnew_2014_nian_1#8$1",focus="n")]
[name="黍"]嗯。
[name="黍"]而且看起来比我的几个妹妹还要调皮一点。
[charslot(slot="m",name="avgnew_2014_nian_1#7$1",focus="m")]
[name="年"]先停一下吧，这儿又不是夕平时乱画的那些东西，我怕你待的时间长了，脑壳犯晕。
[name="年"]小心点......心急吃不了热豆腐。
[Dialog]
[charslot]
[name="黍"]说得也是，确实有些疲惫了......
[name="黍"]......小年，可以拉我一把吗？
[Dialog]
[delay(time=1)]
[PlaySound(key="$p_imp_ancientsword_h",volume=0.6)]
[Blocker(a=0,r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Image(image="47_i02",screenadapt="coverall",fadetime=0,block=true)]
[PlaySound(key="$d_avg_hvygnthrtbt", volume=0, loop=true, channel="mhrt")]
[SoundVolume(volume=0.7, fadetime=3,channel="mhrt")]
[delay(time=0.5)]
[ImageTween(yFrom=50,yTo=0, xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1, yScaleTo=1, duration=30, block=false)]
[playMusic(intro="$sjoyasorrow_intro",key="$sjoyasorrow_loop", volume=0.6)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=3, block=true)]
[delay(time=1)]
[name="夕"]你们再不出来，我就考虑自己回去了。
[name="年"]是吗？我看看，刚才是谁被吓得小脸发白了？
[name="夕"]......闭嘴。
[name="年"]我们现在在给“巨兽”做心脏起搏手术哎，哪有那么容易？
[name="夕"]......唉。
[name="夕"]你跟我讲这个计划的时候，我觉得你一定是疯了......亏你敢想这种点子。
[name="年"]不就是用整座移动城市模拟一只巨兽嘛，我形你意，形神兼备，有什么不行的？
[name="黍"]小年是越来越机灵能干了。
[name="夕"]少来。要是没有天师府的老家伙和黍姐，她能成什么事？
[name="年"]帮司岁台做了这么多杂事，积攒下的人情总该派上点用场。
[name="夕"]所以，情况到底怎么样？
[name="年"]好得很。
[name="年"]但要用这个玩意作为替代本尊的容器，在那个老家伙被干掉以后，我们这些虚无缥缈的可怜人还能有所依凭，恐怕还得费点力。
[name="黍"]毕竟是个麻烦的孩子。
[name="夕"]哪里好了，还不是一事无成。
[name="年"]你不就想说，造这个玩意你也出了力。没被姐姐表扬，吃醋了？
[name="夕"]......幼稚。
[name="黍"]夕的画技也精进了。虽然这么多年没见，看来还是有认真用功，没有虚度光阴的。
[name="夕"]......咳。
[name="夕"]我还是没法想象。靠一副假的躯体“以假乱真”不是难事，但终究只是“乱”。
[name="夕"]说到底它不过是我们分出来的一小部分......三个人的力量拼凑在一起的产物，而且还不完整。
[name="夕"]这十二楼五城，要怎么成为我们这些人的容身之处......
[name="黍"]嗯，或许吧。
[name="黍"]但在画卷里的时候，我确实感受到了......
[name="黍"]“生命”。
[name="黍"]兽与厚土行，“我们”原本也是这片大地上生长出的生命。
[name="黍"]......也许真的行得通呢。
[Dialog]
[StopSound(channel="mhrt", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image]
[charslot]
[Background(image="47_g5_factory_inside", screenadapt="coverall", block=true)]
[charslot(slot="m",name="avgnew_2014_nian_1#1$1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avgnew_2014_nian_1#1$1",focus="m")]
[name="年"]哎！聊点别的。
[name="年"]你们不知道朝廷那几个多难缠！说是把十二楼五城暂且借给咱们安个“家”，实际上既要把老天师换回来，又要解决他们另一个麻烦。
[charslot(slot="m",name="avgnew_2014_nian_1#4$1",focus="m")]
[name="年"]还是炎国人会做生意啊，直接把我们的“家”变成桥头堡了，办一件事，他们要得两份好处。
[name="年"]......只是没想到，大炎竟然在技术层面又更进一步了。有完没完，他们真的还有必要畏惧“岁”吗？
[charslot(slot="m",name="avgnew_2015_dusk_1#3$1",focus="m")]
[name="夕"]这“家”就算建好了，也是在他们眼皮底下被看着，真不自在。
[name="夕"]而且，做这件事有多少风险？我自己都没有把握。
[charslot(slot="m",name="avgnew_2015_dusk_1#7$1",focus="m")]
[name="夕"]刚才你们在画卷里，有一瞬间，我想起了三姐那个时候......
[charslot(slot="m",name="avgnew_2014_nian_1#6$1",focus="m")]
[name="年"]......
[charslot(slot="m",name="avg_2025_shu_1#13$1",focus="m")]
[name="黍"]小墨头也会担心姐姐啦？
[charslot(slot="m",nam

... (全文25568字符)
```

### level_act31side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=2)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="bg_indoor",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot = "m", name = "avg_npc_1236_1#1$1",duration=1)]
[Delay(time=2)]
[name="绩"]已经丑时了......这局是谁赢了？
[charslot(slot = "m", focus = "n")]
[name="低沉的声音"]自己数数。
[charslot(slot = "m", name = "avg_npc_1236_1#7$1")]
[name="绩"]都说过，我不擅长这个。
[charslot(slot = "m", focus = "n")]
[name="低沉的声音"]那你应该学学。
[charslot(slot = "m", name = "avg_npc_1236_1#9$1")]
[name="绩"]要见你一面可不容易。
[name="绩"]这古寺深寒，二哥倒是不改其道......你天天把自己关在这屋子里对着这副棋盘，到底在上面看出什么来了？
[charslot(slot = "m", focus = "n")]
[name="低沉的声音"]和你在那账本上看到的，差不多。
[name="低沉的声音"]棋盘上有同一种规则，棋盘外，也是一样。
[charslot(slot = "m", name = "avg_npc_1236_1#1$1")]
[name="绩"]天下熙熙，皆为利来；天下攘攘，皆为利往......二哥琢磨得通透。
[charslot(slot = "m", name = "avg_npc_1236_1#9$1")]
[name="绩"]这些年来，兄弟姐妹几个，自从找到各自感兴趣的事后，好像都活得越来越惬意了。
[name="绩"]老头子好像终于参透了“武道”，转身去北疆守城，大姐一梦千年四处神游，好不自在。
[charslot(slot = "m", name = "avg_npc_1236_1#3$1")]
[name="绩"]只是......除了那个姐姐。
[charslot(slot = "m", name = "avg_npc_1236_1#2$1")]
[name="绩"]多少年来......我还是为她不值。
[charslot(slot = "m", focus = "n")]
[name="低沉的声音"]看来是你最近的生意做得太顺，才有功夫操心这么多事。
[charslot(slot = "m", name = "avg_npc_1236_1#1$1")]
[name="绩"]我也是最近才想明白一个道理，学会了一种活法。
[name="绩"]天地者，万物之逆旅也，光阴者，百代之过客也......
[name="绩"]人活一世，无非是找到一处寄托，名心不化，这一生也就过去了。寿命长短，也无所谓什么区别。
[charslot(slot = "m", focus = "n")]
[name="低沉的声音"]你要是真的看透了，就不会坐在这。
[charslot(slot = "m", name = "avg_npc_1236_1#6$1")]
[name="绩"]......
[charslot(slot = "m", focus = "n")]
[name="低沉的声音"]我知道你想说什么。
[name="低沉的声音"]你想做的事，我能帮你。
[name="低沉的声音"]但是，我也要借你一样东西。
[charslot(slot = "m", name = "avg_npc_1236_1#9$1")]
[name="绩"]二哥何必客气，只要是我有的，需要什么拿去就是。
[charslot(slot = "m", focus = "n")]
[name="低沉的声音"]把你的命给我。
[charslot(slot = "m", name = "avg_npc_1236_1#3$1")]
[name="绩"]......
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="47_g7_fieldhouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$newhope01_intro",key="$newhope01_loop", volume=0.6)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="听说，我是从外面的村落来到大荒城的。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="那一年，有人在水田里捡到了一只木盆，里面装着一个还不太会说话的孩子。大概是顺着城外的大河漂到了水田里。幸好被人捡到。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="想到之前传来天灾的消息，上游发生的事，似乎也不难猜。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_2025_shu_1#9$1",duration=1)]
[delay(time=1.5)]
[name="温柔的女性"]你运气真好。花下一禾生......就叫你“禾生”吧。
[name="温柔的女性"]以后你就留在这吧。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_mini01_villagevacancy",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="后来，我四处打听，想要找到我出生的村子。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我见到了一片空无一人的“村落”，眼前尽是破败的房屋，源石晶簇遍布的土地。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这里的人，都去哪了？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_2025_shu_1#1$1",duration=1)]
[delay(time=1.5)]
[name="温柔的女性"]这里的土地，种不出庄稼了。
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="为什么......？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Dialog]
[charslot(slot="m",name="avg_2025_shu_1#2$1")]
[name="温柔的女性"]看到那些黑色的石头了吗，有这些东西在的地方，粮食长不出来。
[name="温柔的女性"]种不出粮食，就有人要饿肚子。
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="像这样的土地......还有很多？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="有没有办法，让这些坏石头都消失，让这片土地上长出作物？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Dialog]
[charslot(slot="m",name="avg_2025_shu_1#1$1")]
[name="温柔的女性"]有许多人，许多年来都在想办法。
[name="温柔的女性"]你想要学习吗？
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="嗯......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot(slot="m",name="avg_2025_shu_1#1$1")]
[name="温柔的女性"]但这可能会花很多时间，可能你付出了一生的努力，都不会看到结果。
[name="温柔的女性"]即便如此，你也不后悔吗？
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="嗯。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="47_g2_desertedcityfield_n",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[bgeffect(name="$eb_rain",layer=1)]
[playsound(key="$d_avg_rainlight_loop", loop=true, channel="a")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
最近发生了许多事，原本熟悉的土地仿佛已经变成了人们不认识的样子。古老的田地马上就要完成翻新，又偏偏天意弄人，灾异不断。
田边颓坐的职农抬起头，雨水落在他的脸上，清凉，温和。
田里伏倒的庄稼也挺直了腰杆，枝叶变回了青翠的绿色。
[Dialog]
[charslot(slot="m",name="avg_npc_1249_1#1$1",duration=1)]
[delay(time=2)]
[name="惊讶的职农"]这是......
[name="惊讶的职农"]神农，是神农......
[name="惊讶的职农"]神农真的回来了

... (全文15008字符)
```

### level_act31side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(key="$midautumn", volume=0.6)]
[Delay(time=2)]
[name="？？？"]咳咳咳......
[name="？？？"]咳咳......咳......呼......
[dialog]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "left", name = "avg_npc_1239_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1239_1#1$1",focus="l")]
[name="痨病的老人"]你就非要约我来爬这天岳。
[name="痨病的老人"]这个阳处的位置我先占了，你坐那边去。我身子没你好，你别跟我抢。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "right", name = "avg_npc_301_1#5$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_npc_301_1#5$1",focus="r")]
[name="太傅"]出来散散步，晒晒太阳，尝尝这天岳的泉水，对你的身体有好处。
[charslot(slot = "left", name = "avg_npc_1239_1#3$1",focus="l")]
[name="太尉"]真好笑，我们几十年没在那堵宫墙外打过照面，这次是你主动约的。
[name="太尉"]......到底还是你先坐不住了。
[charslot(slot = "right", name = "avg_npc_301_1#2$1",focus="r")]
[name="太傅"]很难坐得住。
[name="太傅"]玉门，大荒城。这一连串的事，总要一个说法。
[charslot(slot = "left", name = "avg_npc_1239_1#9$1",focus="l")]
[name="太尉"]对，都是我干的。
[name="太尉"]玉门山海众是我教唆的，睚也是我引入关的。
[charslot(slot = "right", name = "avg_npc_301_1#1$1",focus="r")]
[name="太傅"]......
[charslot(slot = "left", name = "avg_npc_1239_1#9$1",focus="l")]
[name="太尉"]这些够把我拉下台吗？要是嫌不够，望是我放出京城的，那个孩子是我送去维多利亚的，邪魔的口子也是我撕开的。
[name="太尉"]只要有需要，让三公的位置再空一个出来，这些事都可以是我干的。
[charslot(slot = "right", name = "avg_npc_301_1#1$1",focus="r")]
[name="太傅"]......
[charslot(slot = "left", name = "avg_npc_1239_1#4$1",focus="l")]
[name="太尉"]山海众，乌合之众，能成什么气候？
[name="太尉"]睚，不过是条痨病兽，派上几十上百个天师，总能打发了，不过用来当作唤醒岁的口粮倒是正好。
[name="太尉"]老魔小丑，不足挂齿。
[charslot(slot = "left", name = "avg_npc_1239_1#1$1",focus="l")]
[name="太尉"]咳......咳......呼......说到底，我也不过是个老痨病鬼，我这条命，也就只剩这点用得到的地方。
[charslot(slot = "right", name = "avg_npc_301_1#1$1",focus="r")]
[name="太傅"]你就不怕事情超出掌控，你从来不会怕。
[charslot(slot = "left", name = "avg_npc_1239_1#2$1",focus="l")]
[name="太尉"]我怕的东西可太多了......我怕“人心叵测”，我怕“大势所趋”。
[name="太尉"]见风使舵，一人拉一边，是求个平衡。
[charslot(slot = "left", name = "avg_npc_1239_1#3$1",focus="l")]
[name="太尉"]可事到如今，那个罪人已经掀了棋盘，我们还有半分求和的可能吗？
[name="太尉"]玉门城已经修复完毕，在赶来京城的路上了。太傅大人，早做打算吧。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="47_g6_civilengineermasteroffice",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_4121_zuole_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_039_1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_4121_zuole_1#6$1",focus="l")]
[name="左乐"]复职信......？
[charslot(slot = "right", focus="r")]
[name="麟青砚"]这封信原本不该由我来送。
[name="麟青砚"]大荒城的事件，那两个罪人的所作所为，朝廷已经得知。
[name="麟青砚"]现在司岁台、天师府、六部......朝野上下，全都忙成一团。我出公事路过大荒城，就代劳了。
[charslot(slot = "left", name = "avg_4121_zuole_1#10$1",focus="l")]
[name="左乐"]是母亲她，拜托你来的吧......
[charslot(slot = "right", focus="r")]
[name="麟青砚"]......
[charslot(slot = "left", name = "avg_4121_zuole_1#1$1",focus="l")]
[name="左乐"]......多谢。
[name="左乐"]这次代理人引发的动乱，朝中已经有结论了？
[charslot(slot = "right", focus="r")]
[name="麟青砚"]是。
[name="麟青砚"]玉门城已修复完毕，已重新启动驶向京城。
[charslot(slot = "left", name = "avg_4121_zuole_1#3$1",focus="l")]
[name="左乐"]......
[name="左乐"]还是到了这一步。
[charslot(slot = "right", focus="r")]
[name="麟青砚"]你倒是镇定，我还以为你会立刻嚷嚷着要回到前线呢。
[charslot(slot = "left", name = "avg_4121_zuole_1#4$1",focus="l")]
[name="左乐"]这段时间，我想明白一个道理。
[name="左乐"]恐惧才会急躁......越是不敢面对未知的敌人，就越想埋头冲过去，不管结果如何，只当给自己一个交代。
[name="左乐"]......可我现在不会害怕了。
[name="左乐"]那些代理人，纵使有改天换地的能力，可说到底，他们也有人情人性，在这方面，祂们与我们并无不同。
[name="左乐"]“对手”并非不可捉摸，那就没什么好怕的。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="bg_landscape",screenadapt="coverall")]
[charslot(slot = "m", name = "avg_npc_1236_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[name="绩"]左公子，在下的确无意与你为敌。刚才说过的话，只希望左公子记得。
[name="绩"]来日方长，我们还会有再见面的时候。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[charslot(slot = "left", name = "avg_4121_zuole_1#4$1")]
[charslot(slot = "right", name = "avg_npc_039_1")]
[Background(image="47_g6_civilengineermasteroffice",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot = "right", name = "avg_npc_039_1",focus="r")]
[name="麟青砚"]还不错，左将军让你来这里修心，也不算白来了。
[charslot(slot = "left", name = "avg_4121_zuole_1#1$1",focus="l")]
[name="左乐"]我已经准备妥当，随时可以动身。现在该去哪？玉门，还是百灶？
[charslot(slot = "right", name = "avg_npc_039_1",focus="r")]
[name="麟青砚"]不急，先回归一下你的本职工作吧。
[name="麟青砚"]有一个地方，与代理人接触颇多。虽说朝廷对那里并非一无所知，依照惯例，还是由司岁台去调查一下为好。
[charslot(slot = "left", name = "avg_4121_zuole_1#10$1",focus="l")]
[name="左乐"]......罗德岛？
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="47_g3_fieldpath",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_4119_wanqin_1#2$1",duration = 1)]
[charslot(slot = "right", name = "avg_4122_grabds_1#2$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_4122_grabds_1#8$1",focus="r")]
[name="小满"]你真的要走了？
[charslot(slot = "left", name = "avg_4119_wanqin_1#10$1",focus="l")]
[name="禾生"]真的。
[name="禾生"]这一批种子，有些种了出来，源石耐受性的表现比预想的要好，是时候带去外面的田地里做下一步培育了。
[charslot(slot = "right", name = "avg_4122_grabds_1#7$1",focus="r")]
[name="小满"]那是不是很辛苦？
[charslot(slot = "left", name = "avg_4119_wanqin_1#10$1",focus="l")]
[name="禾生"]和在大荒城做的事一样。
[charslot(slot = "right", name = "avg_4122_grabds_1#11$1",focus="r")]
[name="小满"]唔......那你什么时候回来？
[charslot(slot = "left", name = "avg_4119_wanqin_1#1

... (全文14976字符)
```

### training_act31side_01_a

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动31side教学关_01a

[Battle.Pause]

[InputBlocker(blockInput=true, black=0.2)]

[PopupDialog(dialogHead="$avatar_dusk")]呼，偶尔看看此处的风景也不错，省得有人烦扰。

[InputBlocker(blockInput=true, black=0)]

[Battle.Pause(pause=false)]
[Delay(time=3)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=true, black=0.2)]

[PopupDialog(dialogHead="$avatar_dusk")]嗯？这是田里的害兽？

[PopupDialog(dialogHead="$avatar_dusk")]不，不对......
```

### training_act31side_01_b

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动31side教学关_01b

[Battle.Pause]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(dialogHead="$avatar_dusk")]哼，果然不是什么好东西，田地被污染了。

[Tutorial(focusX=330, focusY=-140, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm")]是的，<@tu.kw>天桩</>检测到了病害。

[Tutorial(dialogHead="$avatar_doberm")]这次的战场在种植地块的田地里。

[Tutorial(dialogHead="$avatar_doberm")]除了地穴与通道，<@tu.kw>所有田地</>都覆盖有浅水，看来<@tu.kw>病害</>能顺着水直接<@tu.kw>传染</>到<@tu.kw>所有相接</>的<@tu.kw>地面地块</>。

[Tutorial(focusX=0, focusY=-45, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 幸好我们有<@tu.kw>阻流阀</>来区隔田地。

[Tutorial(focusX=0, focusY=-45, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这个<@tu.kw>阻流阀</>与高台隔出了两个<@tu.kw>封闭</>的田地。

[Tutorial(focusX=-200, focusY=-45, focusWidth=250, focusHeight=250, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]左边。

[Tutorial(focusX= 200, focusY=-45, focusWidth=250, focusHeight=250, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]以及右边的田地被区隔开了。

[Tutorial(focusX=0, focusY=-45, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]病害被阻隔住，就不会传播污染了。

[PopupDialog(dialogHead="$avatar_ardign")] 有更多敌人过来了，我来帮忙！

[PopupDialog(dialogHead="$avatar_dusk")] 好，别让病害继续蔓延。
```

### training_act31side_01_c

```
[HEADER( is_skippable=true, is_autoable=false)] 活动25side教学关_c


[Tutorial(dialogHead="$avatar_ardign", black="$f_tut_black", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]呜哇！好痛！

[Tutorial(focusX= 200, focusY=-45, focusWidth=250, focusHeight=250, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm")] 这些生物散播的病害会污染本有治愈效果的浅水。

[Tutorial(dialogHead="$avatar_doberm", black="$f_tut_black", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]在<@tu.kw>无病害的田地</>里的干员会持续恢复生命。

[Tutorial(dialogHead="$avatar_doberm", black="$f_tut_black", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]当干员被<@tu.kw>部署</>在<@tu.kw>有病害的田地</>里时，会受到<@tu.kw>一次高额</>的<@tu.kw>法术伤害</>，并将<@tu.kw>持续</>受到法术伤害。

[Tutorial(focusX=330, focusY=-140, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm")]敌人对田地造成的<@tu.kw>病害污染将会累积</>，一块田地受病害污染的程度越严重，干员受到的<@tu.kw>伤害就越高</>。

[Tutorial(focusX=330, focusY=-140, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm")]可以通过田地的颜色，或天桩的状态来判断病害的严重程度。

[Tutorial(dialogHead="$avatar_ansel", black="$f_tut_black")]坚持住，卡缇！
```

### training_act31side_01_d

```
[HEADER( is_skippable=true, is_autoable=false)] 活动31side教学关_d

[Tutorial(focusX=-15, focusY=-60, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_ansel", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]有东西在攻击阻流阀！

[Tutorial(focusX=-15, focusY=-60, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]是田鼷！

[Tutorial(focusX=-15, focusY=-60, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]这类生物是农人的眼中钉，它们适应了现代的耕种方式，<@tu.kw>只有</>它们喜欢去<@tu.kw>攻击阻流阀</>。

[Tutorial(dialogHead="$avatar_melan", black="$f_tut_black")]我来帮忙。
```

### training_act31side_01_e

```
[HEADER( is_skippable=true, is_autoable=false)] 活动31side教学关_d

[Tutorial(dialogHead="$avatar_melan", black="$f_tut_black")]它们太多了，我拦不住，阻流阀被破坏了！

[Tutorial(focusX=-200, focusY=-45, focusWidth=250, focusHeight=250, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm")]阻流阀被破坏后，病害便会在田地间传播，但这<@tu.kw>需要时间</>。

[Tutorial(anchor="BottomRight", focusX=-15, focusY=30, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]天师们提供的阻流阀到了。

[Tutorial(focusX=0, focusY=-45, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm")]<@tu.kw>堵住刚才的口子</>，继续区隔田地。

[Tutorial(focusX=-30, focusY=150, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm")]或是<@tu.kw>后撤防线</>，区隔出更多田地区域来阻挡病害蔓延。

[Tutorial(dialogHead="$avatar_doberm", black="$f_tut_black")]战场判断交给你，博士，请指挥干员继续迎战！
```

### training_act31side_02_a

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动31side教学关_02a

[Battle.Pause]

[InputBlocker(blockInput=true, black=0.2)]

[PopupDialog(dialogHead="$avatar_jesica")]糟了！已经有田地被病害污染了，我该怎么做？

[PopupDialog(dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]莫慌。

[PopupDialog(dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]来试试那帮书呆子造的<@tu.kw>泵站</>。

[PopupDialog(dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]只要这样放。

[InputBlocker(blockInput=true, black=0)]

[Battle.Pause(pause=false)]
[Delay(time=2)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(focusX=90, focusY=-45, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]可以把它<@tu.kw>身后一格</>的田地中的水抽到前面去。

[Tutorial(focusX=-90, focusY=-45, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]就能<@tu.kw>净化</>受病害污染的田地了。

[InputBlocker(blockInput=true, black=0)]

[Battle.Pause(pause=false)]
[Delay(time=4)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(focusX=-300, focusY=-45, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_jesica")]那、那边呢......我知道了，只要有更多泵站......

[PopupDialog(dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]莫慌，只要像这样。

[InputBlocker(blockInput=true, black=0)]

[Battle.Pause(pause=false)]
[Delay(time=2)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=true, black=0.2)]

[PopupDialog(dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]在<@tu.kw>泵站后</>部署一名干员，像我这样随便摆弄几下。

[PopupDialog(dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]就能让泵站的生效距离<@tu.kw>增加两格</>。

[PopupDialog(dialogHead="$avatar_jesica")]我明白了！
```

### training_act31side_02_b

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动25side教学关02_b
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(focusX=-90, focusY=-45, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_jesica")]完、完蛋了！它怎么开始喷脏水了！

[PopupDialog(dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]唉，书呆子造的玩意，只能抽水不能净水！如果泵站身后本来就是<@tu.kw>被病害污染</>的田地，抽水的时候自然也会<@tu.kw>导致病害传播</>！

[PopupDialog(dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]当然，无论怎么传播，病害的污染程度都<@tu.kw>不会超过</>其源头。

[PopupDialog(dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]与此同时，要记住<@tu.kw>只有净水</>才能净化病害，降低污染！

[Battle.Pause(pause=false)]
[Delay(time=1)]
[Battle.Pause(pause=true)]

[PopupDialog(dialogHead="$avatar_jesica")]年小姐！天师们又送新的泵站过来了！

[PopupDialog(dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]动作倒是麻利。那，听我指令。

[InputBlocker(blockInput=false)]
[Battle.EnsureMinCost(cost=10)]
[Tutorial(waitForSignal="put_down", dialogHead="$avatar_nian", animStyle="Drag", \
          startX=-60, startY=60, startAnchor="BottomRight", endX=230, endY=45)] \
把新到的泵站<@tu.kw>放到这里</>

[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_nian", animStyle="Drag", \
          startX=230, startY=45, endX=230, endY=-100)] \
<@tu.kw>向下部署</>

[InputBlocker(blockInput=true, black=0.2)]
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]

[PopupDialog(dialogHead="$avatar_nian")]这样，加上我站在这里，这片田地就不用担心了。

[PopupDialog(dialogHead="$avatar_nian")]快把剩下的敌人消灭干净吧！
```


## 统计

- 总字符数：416197
- 对话行数：3038


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
