# 明日方舟 · 活动剧情 · act23side（25段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act23side」完整剧情脚本（25个文件，3519行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act23side
- 脚本文件数：25

### level_act23side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="35_g9_yumensuburb",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_795_1#1$1",duration=0.7)]
[delay(time=1)]
[name="玉门守军A"]进了玉门城，应该已经安全了。
[charslot(slot="m",name="avg_4080_lin_1#1$1",focus="m")]
[name="林雨霞"]不要掉以轻心。
[charslot(slot="m",name="avg_4080_lin_1#1$1",focus="m")]
[name="林雨霞"]先回军营，将数据送去钦天监，再向左将军汇报城外的事情。
[charslot(slot="m",name="avg_npc_795_1#1$1",focus="m")]
[name="玉门守军A"]是。
[dialog]
[charslot]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$d_avg_arrow_rain", volume=1,delay=0.2)]
[PlaySound(key="$d_avg_sandsword", volume=1)]
[PlaySound(key="$d_avg_glassbroken", volume=1,delay=0.4)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=2)]
[charslot(slot="m",name="avg_4080_lin_1#8$1",focus="m")]
[name="林雨霞"]呵，我话音还没落。
[charslot(slot="m",name="avg_npc_795_1#1$1",focus="m")]
[name="玉门守军A"]有埋伏！保护林特使往回撤！
[charslot(slot="m",name="avg_4080_lin_1#1$1",focus="m")]
[name="林雨霞"]不用了，我们已经被包围了。
[dialog]
[character]
[delay(time=1)]
[PlaySound(key="$d_gen_soldiersrun", volume=1)]
[charslot(slot="l",bstart=0.2,bend=0.7,name="avg_npc_794_1#1$1",duration=1,afrom=1,ato=1,posfrom="-800,0",posto="0,0")]
[charslot(slot="r",bstart=0.2,bend=0.7,name="avg_npc_794_1#1$1",duration=1,afrom=1,ato=1,posfrom="800,0",posto="0,0")]
[delay(time=1.5)]
[charslot(duration=0.2)]
[delay(time=0.2)]
[charslot(slot="m",name="avg_npc_796_1#1$1",focus="m")]
[name="玉门守军B"]敢在玉门城内拦截官军，什么人？！
[dialog]
[charslot]
[charslot(slot="l",name="avg_npc_794_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_794_1#1$1",duration=0.7)]
[delay(time=1)]
[name="来历不明的凶徒"]......
[charslot]
[charslot(slot="m",name="avg_npc_796_1#1$1",focus="m")]
[name="玉门守军B"]林特使小心！
[Dialog]
[stopmusic(fadetime=1)]
[PlaySound(key="$d_avg_battlefield_environment", volume=0.4, loop=true, channel="steam")]
[delay(time=1)]
[Dialog]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[charslot(slot="r",name="avg_npc_794_1#1$1",posfrom = "500,0", posto = "-100,0",duration = 0.5,isblock=false)]
[playsound(key="$rungeneral",channel="run")]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$swordtsing2",volume=0.3)]
[PlaySound(key="$d_avg_axehitscrape", volume=1)]
[stopsound(channel="run")]
[charslot(slot = "m", action="shake",random=true, power=8, times=60,isblock=false,duration=0.2)]
[charslot(slot="m",name="avg_npc_796_1#1$1",posfrom = "0,0", posto = "-200,0",duration = 0.3,isblock=true)]
[PlaySound(key="$swordtsing1",volume=0.3)]
[charslot(slot="m",name="avg_npc_796_1#1$1",posfrom = "-200,0", posto = "-400,0",duration = 0.5,afrom=1,ato=0,isblock=false)]
[charslot(slot="l",name="avg_4080_lin_1#1$1",posfrom = "-500,0", posto = "0,0",duration = 0.5,isblock=false)]
[Dialog]
[charslot(slot = "right",posfrom = "800,0", posto = "-200,0",duration = 0.3,isblock=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_wepncontact", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[charslot(slot = "right", name = "avg_npc_794_1#1$1",posfrom = "-100,0", posto = "0,0",duration = 0.2,isblock=true)]
[delay(time=0.5)]
[charslot(slot = "right",focus="r")]
[name="来历不明的凶徒"]将沙石变成玻璃......很奇特的法术。
[dialog]
[charslot]
[CameraShake(duration=1, xstrength=20, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_wepncontact", volume=1)]
[PlaySound(key="$swordtsing4",delay=0.1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4080_lin_1#9$1",focus="m")]
[name="林雨霞"]我在城外就觉得蹊跷......
[charslot(slot="m",name="avg_4080_lin_1#1$1",focus="m")]
[name="林雨霞"]你们的目标是天灾观测数据吧。你们截杀了信使队伍，但并没有找到数据，只能草草将现场布置成流寇洗劫......拙劣。
[dialog]
[charslot]
[charslot(slot="l",name="avg_npc_794_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_794_1#1$1",duration=0.7)]
[delay(time=1)]
[name="来历不明的凶徒"]先杀了那个女人，东西一定还在她身上，当心源石技艺。
[charslot]
[charslot(slot="m",name="avg_4080_lin_1#11$1",focus="m")]
[name="林雨霞"]仗着人多？呵......
[dialog]
[charslot]
[PlaySound(key="$d_avg_singleblunt", volume=1)]
[delay(time=0.8)]
[PlaySound(key="$d_avg_singleblunt", volume=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$d_avg_hammer", volume=0.8)]
[PlaySound(key="$d_sp_ballista",volume=0.3)]
[PlaySound(key="$b_char_rockexplo",delay=0.04)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[Delay(time=1)]
重器破空而来，击飞林雨霞身前的凶徒，尾势未消，直至砸碎路面的石板。
那是一柄普通的锤。锻铁碎石，不知道多少时日，粗糙的锤面变得光滑。
来人捡起锤，挡在林雨霞身前。
那是一位普通的刀匠。脸庞被炉火燎红，又被风沙犁出沟壑，像是一面废弃的军鼓，粗糙，但仍坚韧。
[dialog]
[charslot]
[charslot(slot="l",name="avg_npc_789_1#10$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_296_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_789_1#2$1",focus="l")]
[name="？？？"]放肆！
[charslot(slot="l",name="avg_npc_794_1#1$1")]
[charslot(slot="r",name="avg_npc_794_1#1$1")]
[name="来历不明的凶徒"]......
[dialog]
[PlaySound(key="$d_avg_crowdrun", volume=1,channel="2")]
[charslot(duration=1.5,isblock=true)]
[stopSound(channel="2", fadetime=1)]
[stopso

... (全文36360字符)
```

### level_act23side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$escape_intro",key="$escape_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="m",name="avg_4078_bdhkgt_1#1$1",duration=1,posfrom="800,0",posto="0,0",isblock=true)]
[delay(time=0.5)]
[charslot(slot="m",duration=0.5,posfrom="0,0",posto="-500,0",afrom=1,ato=0,isblock=true)]
[charslot]
[delay(time=0.2)]
[charslot(slot="m",name="avg_npc_297_1#1$1")]
[name="左乐"]什么人？
[charslot(slot="m",name="avg_npc_297_1#1$1",focus="none")]
[name="异族装扮的少女"]......
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]站住。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]你可知你现在身在何处，手里拿着的那把剑又是何物？
[charslot(slot="m",name="avg_4078_bdhkgt_1#1$1")]
[name="异族装扮的少女"]一把剑，我要找的剑。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]......
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]我先不问你是受何人指使，又为何能出现在此处。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]把剑交出来，跟我去见宗师。
[charslot(slot="m",name="avg_4078_bdhkgt_1#7$1")]
[name="异族装扮的少女"]薄情寡义，背信弃义之人，不配拥有这把剑。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]放肆！
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]宗师守护玉门安危百年，岂容你信口玷污？
[charslot(slot="m",name="avg_4078_bdhkgt_1#5$1")]
[name="异族装扮的少女"]装模作样，你又知道些什么？让开！
[charslot(slot="m",name="avg_npc_297_1#1$1")]
[name="左乐"]逮捕过的不法之徒不少，像阁下这样嚣张的，我还是头一回见。
[charslot(slot="m",name="avg_4078_bdhkgt_1#1$1")]
[name="异族装扮的少女"]表面道貌岸然，其实自私自利。你们这样的人，我见多了！
[PlaySound(key="$d_avg_unsheathe",volume=1)]
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]那我只好用强硬手段请阁下伏法了。
[charslot(slot="m",name="avg_4078_bdhkgt_1#1$2")]
[name="异族装扮的少女"]你出刀，试试看。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[charslot]
[Background(image="35_g3_yumenobservationtower_n",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[CameraShake(duration=1, xstrength=20, ystrength=22, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$fightgeneral",volume=0.6)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing3",volume=0.7)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[PlaySound(key="$swordtsing5",volume=0.9)]
[PlaySound(key="$swordtsing6",volume=1,delay=0.04)]
[Delay(time=1)]
[charslot(slot="m",name="avg_2024_chyue_1#1$1",focus="m")]
[name="重岳"]胜负已分。
[charslot(slot="m",name="avg_npc_786_1#1$2",focus="m")]
[name="冷漠的女性"]我们的胜负，不是在这里分出的。
[charslot(slot="m",name="avg_2024_chyue_1#8$1",focus="m")]
[name="重岳"]人和说法，阁下总得留下一个。
[dialog]
[charslot]
[PlaySound(key="$d_gen_soldiersrun",volume=1)]
[charslot(slot="l",name="avg_npc_795_1#1$1",duration=0.5,isblock=false)]
[delay(time=0.51)]
[charslot(slot="l",name="avg_npc_795_1#1$1",duration=0.5,isblock=false,afrom=1,ato=0)]
[charslot(slot="r",name="avg_npc_796_1#1$1",duration=0.5,isblock=false)]
[delay(time=0.51)]
[charslot(slot="r",name="avg_npc_796_1#1$1",duration=0.5,isblock=false,afrom=1,ato=0)]
[charslot(slot="l",name="avg_npc_795_1#1$1",duration=0.5,isblock=false)]
[delay(time=0.51)]
[charslot(slot="r",name="avg_npc_796_1#1$1",duration=0.5,isblock=false)]
[delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_npc_786_1#1$2",focus="m")]
[name="冷漠的女性"]我想要一些答案。但你给不了我。
[Dialog]
[PlaySound(key="$d_avg_humanchange")]
[PlaySound(key="$p_aoe_nmag_h")]
[charslot(slot="m",name="avg_npc_786_1#1$2",focus="m",afrom=1,ato=0,duration=1,isblock=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.7, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_2023_ling_1#9$1",focus="m")]
[name="令"]还是让她逃了。
[charslot(slot="m",name="avg_npc_034#1",focus="m")]
[name="林"]受了那么重的伤，总该跑不远。
[charslot(slot="m",name="avg_npc_034#1",focus="m")]
[name="林"]魏老二，你这把老骨头也是不顶用了。
[charslot(slot="m",name="char_2005_weiyw_1#5",focus="m")]
[name="魏彦吾"]有劳林先生搭救。
[charslot(slot="m",name="avg_npc_034#1",focus="m")]
[name="林"]堂堂赤霄剑主人，被仇家找上门来，也要靠他人搭救了？
[charslot(slot="m",name="char_2005_weiyw_1#2",focus="m")]
[name="魏彦吾"]我可真不记得，我还有这么一号仇家——
[charslot(slot="m",name="avg_2024_chyue_1#1$1",focus="m")]
[name="重岳"]......
[charslot(slot="m",name="avg_2024_chyue_1#7$1",focus="m")]
[name="重岳"]声东击西！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[charslot]
[Background(image="35_g3_yumenobservationtower_n",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[CameraShake(duration=1, xstrength=20, ystrength=22, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing1",volume=0.7)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[PlaySound(key="$swordtsing2",volume=0.9)]
[PlaySound(key="$swordtsing3",volume=1,delay=0.04)]
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$d_avg_bldwhoosh", volume=1)]
[PlaySound(key="$d_avg_knife", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_4078_bdhkgt_1#7$2",duration=0.5,posfrom="800,0",posto="0,0",isblock=true,focus="l")]
[name="异族装扮的少女"]哼......！
[dialog]
[charslot(slot="r",name="avg_npc_297_1#6$1",duration=1,posfrom="800,0",pos

... (全文34609字符)
```

### level_act23side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="35_g11_yumendesert",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Dialog]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]	
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="阿纳萨。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="在一种古老的语言里，是“无根之人”的意思。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="族人说，一切世事无定，唯有生老病死的苦难不变。想要寻找某种依凭的念头，只会给自己徒增烦恼。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="所以我们居无定所，与荒野共生，在广阔的大地上，总能找到水源和猎物，等自己寿命终了，自然也会化为尘土，反哺大地。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但是，一场天灾摧毁了我们生存的营地，整个族群都险些在迁徙中丧命。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="一个来自移动城市的人偶然经过，她带领我们找到了另一处安身之所。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她教导我们武艺，传授我们知识，给我们讲述移动城市里的故事。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她说，人应当有一个可以称为家的地方。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Character]
[charslot]
[Delay(time=1)]
[Background(image="35_g13_yanlivingroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[dialog]
[charslot]
[charslot(slot="r",name="avg_4078_bdhkgt_1#2$1",focus="r")]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="受伤的少女"]——！
[charslot(slot="r",name="avg_4078_bdhkgt_1#2$1",focus="l")]
[name="？？？"]躺下。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "left", name = "avg_npc_785_1#1$1",posfrom = "-200,0", posto = "0,0",duration = 1,isblock=false)]
[delay(time=1.5)]
[charslot(slot="r",name="avg_4078_bdhkgt_1#7$1",focus="r")]
[name="受伤的少女"]（古老的萨卡兹语）你是什么人？！我为什么在这里？
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]我听不懂你在说什么。算了，听不懂也不打紧。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]你只许在这里养伤，吃喝起居、一举一动都得听医生的。医生不在，那就得听我的。否则，小命不保。
[charslot(slot="r",name="avg_4078_bdhkgt_1#7$1",focus="r")]
[name="受伤的少女"]（有些生硬的炎国语）这是哪......？你是谁？！
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]这是医馆，你是病人，我是医馆的伙计。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="r",name="avg_4078_bdhkgt_1#5$1",focus="r")]
[name="受伤的少女"]我的剑呢？！
[dialog]
[charslot]
少女紧张地四处摸索，直到手掌触碰到身旁的古剑，才慢慢放松下来。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="r")]
[charslot(slot="r",name="avg_4078_bdhkgt_1#9$1",focus="r")]
[name="受伤的少女"]还好......还在......
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]昨晚你倒在医馆门口，昏迷不醒，还紧紧抱着这把剑不松开。你是为了抢这个东西才受伤的？
[charslot(slot="r",name="avg_4078_bdhkgt_1#1$1",focus="r")]
[name="受伤的少女"]......和你无关。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]不用这么看着我。我要是想抢，早趁你昏迷的时候把东西拿走了。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]见多了为一件所谓的绝世神兵不要命的人，实在无聊。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]你们真的相信，靠一件兵器就能实力大增，打败自己原本打不过的人？
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]我就从不相信兵器，我只相信自己的拳头。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]习武之人，把胜负寄托于外物，就已经落了下乘。不好，不好。
[charslot(slot="r",name="avg_4078_bdhkgt_1#7$1",focus="r")]
[name="受伤的少女"]你不明白！
[charslot(slot="r",name="avg_4078_bdhkgt_1#8$1",focus="r")]
[name="受伤的少女"]我才不是要用这把剑去打架......我......是为了报恩。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]我只晓得剑能用来杀人。
[charslot(slot="r",name="avg_4078_bdhkgt_1#1$1",focus="r")]
[name="受伤的少女"]师父说，这把剑对她有很特殊的意义。
[charslot(slot="r",name="avg_4078_bdhkgt_1#3$1",focus="r")]
[name="受伤的少女"]我和她约定好了，要把这把剑带给她。如果她不在了，也要将这把剑带到她的坟前......
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]你说的师父，是已经离世了？
[charslot(slot="r",name="avg_4078_bdhkgt_1#2$1",focus="r")]
[name="受伤的少女"]嗯......
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]恩恩怨怨没完没了，我也没兴趣听。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]你说抢剑是为了报恩，那我就相信你。一个险些丢了命的人，应该犯不着说谎。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]所以说，你将这把剑看得比命重要，其实是把别人的恩情看得比命重要，是个重情义的人。那倒不错，不错。
[charslot(slot="r",name="avg_4078_bdhkgt_1#1$1",focus="r")]
[name="受伤的少女"]......你们为什么要救我？
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]医馆救人难道不是天经地义？哪来那么多为什么。
[charslot(slot="r",name="avg_4078_bdhkgt_1#11$1",focus="r")]
[name="受伤的少女"]可我没有钱，我知道，对生活在移动城市里的人来说，接受别人的恩惠，是要付钱的。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]欠债还钱的道理倒是没错，但是没钱也不打紧，帮医生干活也可以抵账。不然你以为我为什么在这里？
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]但我和你可不一样，我赔的是被我打伤的人的医药费。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]医馆里的体力活有我干了，你可以去晒晒草药，学学包扎之类的。你欠的钱也没我多，三两个月总能还清了。
[charslot(slot="r",name="avg_4078_bdhkgt_1#7$1",focus="r")]
[name="受伤的少女"]不行！
[charslot(slot="r",name="avg_4078_bdhkgt_1#7$1",focus="r")]
[name="受伤的少女"]你们救我的恩情，我会再还。但是现在，我很赶时间......
[charslot(slot="r",name="avg_4078_bdhkgt_1#7$1",focus="r")]
[name="受伤的少女"]我一定要出城。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]不许动。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]我说了，现在你只许好好养伤。
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]受这么重的伤都活了下来，要是在医馆养伤的时候死了，你丢人，医馆也丢人。 
[charslot(slot="l",name="avg_npc_785_1#1$1",focus="l")]
[name="魁梧的男人"]嗯......但是话说回来，报恩的事也很要紧。等你养好了伤还清了债，我再考虑要不要帮你。
[Dialo

... (全文27413字符)
```

### level_act23side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="35_g10_yumenfair",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="顽皮的小孩"]妈，妈，你快看，那边好像有人在打架！
[name="忙碌的女性"]有什么好看的，谈价谈不拢就打起来了呗。
[name="忙碌的女性"]跟紧一点，在这里走丢了，一会儿我都不知道该上哪儿找你。
[charslot(slot="l",name="avg_npc_297_1#1$1",focus="r")]
[charslot(slot="r",name="avg_322_lmlee_1#5$1",focus="r")]
[name="老鲤"]左公子，这伙人不会轻易罢休。再打下去，咱俩能不能自保先不说，很难保证不会伤及百姓。
[charslot(slot="l",name="avg_npc_297_1#6$1",focus="l")]
[name="左乐"]......鲤先生，有什么主意？
[charslot(slot="r",name="avg_322_lmlee_1#1$1",focus="r")]
[name="老鲤"]逃跑的办法倒是有，只怕后面会让你不好收场啊......
[charslot(slot="l",name="avg_npc_297_1#4$1",focus="l")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="左乐"]等——
[charslot(slot="r",name="avg_322_lmlee_1#3$1",focus="r")]
[name="老鲤"]（糟糕，来不及——）
[dialog]
[charslot(duration=0.5)]
[stopmusic(fadetime=2)]
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=0.5, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$d_avg_bldwhoosh")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[curtain(direction = 2,fillfrom = 0,fillto = 0.6,fadetime=0.01,grad=true)]
[curtain(direction = 6,fillfrom = 0,fillto = 0.01,fadetime=0.01,grad=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0,b=0,fadetime=2, block=true)]
[delay(time=2)]
[PlaySound(key="$d_avg_walk_stage")]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Sticker(id="st1",  multi = true, text="山海众以杂乱的人群为掩护，像是没入水中的鳞。", x=600,y=270, alignment="left", size=24,block = true,width=700)]
[Sticker(id="st1", multi = true, text="\n群鳞同时跃出水面，左乐和老鲤有所顾忌，断难接下那样凌厉的杀招。",block = true)]
[stickerclear]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_787_1#1$1",duration=2)]
[curtain]
[PlaySound(key="$d_avg_snowstormflp", volume=1)]
[PlaySound(key="$d_avg_swordexsheath", volume=1)]
[curtain(direction = 2,fillfrom = 0,fillto = 0.01,fadetime=0.01,grad=true)]
[curtain(direction = 6,fillfrom = 0,fillto = 0.6,fadetime=0.5,grad=true)]
[charslot(slot="m",name="avg_npc_787_1#1$1")]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]   
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Sticker(id="st1", text="在场似乎有人看到了雪。", x=100, y=270, alignment="left", size=24, delay=0.04, width=700)]
[stickerclear]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)] 
[delay(time=0.5)]
[curtain(direction = 2,fillfrom = 0.01,fillto = 0,fadetime=0.01,grad=true)]
[curtain(direction = 6,fillfrom = 0.6,fillto = 0,fadetime=0.01,grad=true)]
[curtain]
[delay(time=0.5)]
[curtain(direction = 0,fillfrom = 0.5,fillto = 0.5,grad = true,fadetime=0.01)]
[curtain(direction = 4,fillfrom = 0.2,fillto = 0.2,grad = true,fadetime=0.01,block = true)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Sticker(id="st2", text="不是细碎的雪花，而是一场纷纷扬扬的雪。", x=100, y=270, alignment="left", size=24, delay=0.04, width=700)]
[stickerclear]
[dialog]
[curtain(direction = 0,fillfrom = 0.5,fillto = 0.3,grad = true,fadetime=3)]
[curtain(direction = 4,fillfrom = 0.2,fillto = 0.4,grad = true,fadetime=3,block = true)]
[delay(time=0.1)]
[Sticker(id="st3", text="大雪截断了湍急的乱流，截断了所有山海众的脚步。", x=100, y=470, alignment="left", size=24, delay=0.04, width=700)]
[stickerclear]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]	
[delay(time=0.5)]
[curtain(direction = 0,fillfrom = 0.3,fillto = 0,grad = true,fadetime=0.01)]
[curtain(direction = 4,fillfrom = 0.4,fillto = 0,grad = true,fadetime=0.01,block = true)]
[curtain]
[delay(time=0.1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$swordtsing5",delay=0.2,channel="R",volume=1,block=true)]
[PlaySound(key="$swordtsing5",delay=0.6,channel="h",volume=1,block=true)]
[PlaySound(key="$swordtsing5",channel="o",volume=1,block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[charslot(slot="m",name="avg_npc_787_1#1$1",focus="none")]
[name="山海众成员"]（闷哼声）
这样的反应，绝不仅仅是高超的“武技”，那是从生死场里赚来的经验。
[charslot(slot="m",name="avg_npc_787_1#7$1",focus="m")]
[name="仇白"]还不退？
[dialog]
[charslot]
[name="山海众成员"]......
[playsound(key="$d_avg_crowdrun",channel="run")]
[soundvolume(channel="run",volume=0,fadetime=1)]
[Dialog]
[charslot(slot = "right", name = "avg_npc_787_1#7$1")]
[PlaySound(key="$rungeneral", volume=0.9)]
[charslot(slot = "left", name = "avg_npc_297_1#1$1",posfrom = "200,0", posto = "0,0",duration = 1,isblock=false)]
[delay(time=1.5)]
[charslot(slot = "right", name = "avg_npc_787_1#1$1",focus="r")]
[name="仇白"]别追。
[name="仇白"]集市人太多，这些凶徒下手残忍，容易伤及无辜。
[charslot(slot = "l", name = "avg_npc_297_1#6$1",focus="l")]
[name="左乐"]（粗重的喘息）
[charslot]
[charslot(slot = "m", name = "avg_npc_297_1#5$1",focus="m")]
[name="左乐"]仇、仇姐姐......好久不见。
[charslot(slot = "m", name = "avg_npc_787_1#11$1",focus="m")]
[name="仇白"]是好久不见。你的武功怎么没什么长进？
[charslot(slot = "m", name = "avg_npc_297_1#5$1",focus="m")]
[name="左乐"]......
[charslot(slot = "m", name = "avg_npc_297_1#1$1",focus="m")]
[name="左乐"]仇姐姐为何来此？
[charslot(slot = "m", name = "avg_npc_787_1#1$1",focus="m")]
[name="仇白"]宗师让我来帮一帮你。
[charslot(slot = "m", name = "avg_npc_787_1#11$1",focus="m")]
[name="仇白"]旁边这位是？
[charslot(slot = "m", name = "avg_npc_297_1#1$1",focus="m")]
[name="左乐"]是在先前的任务中，认识的一位朋友......也是梁大人的故交。
[charslot(slot = "m", name = "avg_npc_787_1#11$1",

... (全文20126字符)
```

### level_act23side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="35_g6_yumengate",screenadapt="coverall")]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot = "middle", name = "avg_npc_799_1#1$1", duration = 1)]
[Delay(time=1.5)]
[name="愤怒的武人"]让我们出去。
[charslot(slot = "middle", name = "avg_npc_796_1#1$1")]
[name="巡防营守军"]该说的话刚才已经说过了。
[name="巡防营守军"]将军有令，为了玉门安危，戒严期间，任何人不得擅自出城。
[name="巡防营守军"]请回吧。
[charslot(slot = "middle", name = "avg_npc_799_1#1$1")]
[name="愤怒的武人"]你跟我讲玉门安危？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="愤怒的武人"]我们守玉门城的时候，你小子还没摸过刀呢！
[charslot(slot = "middle", name = "avg_npc_796_1#1$1")]
[name="巡防营守军"]......
[name="巡防营守军"]非常时期，请大家以大局为重。
[charslot(slot = "middle", name = "avg_npc_799_1#1$1")]
[name="愤怒的武人"]大局为重？
[name="愤怒的武人"]那年一伙流寇潜入城中偷抢钱财，伤了好几个无辜百姓。
[name="愤怒的武人"]事发突然，不清楚具体情况，你们守军不敢妄动，是我们哥几个追了出去，整整三天，在沙漠里追出去几百里地。
[name="愤怒的武人"]我们背着一半只剩一口气的兄弟，最终把贼人逮回城里。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="愤怒的武人"]现在是我们的兄弟死在了城外，尸骨都没能收回来，你让我们在这里等着？！
[charslot(slot = "middle", name = "avg_npc_796_1#1$1")]
[name="巡防营守军"]荆前辈，我们都听过您的故事，也很敬重您。
[name="巡防营守军"]但左将军有令，城中正在缉拿要犯，没有他本人特许，任何人不得出入玉门。
[charslot(slot = "middle", name = "avg_npc_799_1#1$1")]
[name="愤怒的武人"]好大的威风！
[name="愤怒的武人"]那就叫左宣辽出来见我们！
[charslot(slot = "m", focus = "none")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="？？？"]放肆！
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot = "middle", name = "avg_npc_789_1#5$1", duration = 1)]
[Delay(time=2)]
[charslot(slot = "middle", name = "avg_npc_799_1#1$1")]
[name="愤怒的武人"]坊主......
[charslot(slot = "middle", name = "avg_npc_789_1#5$1")]
[name="孟铁衣"]大老远就听到你们在这嚷嚷，这些当兵的兄弟也是奉了上头的命令，何必为难他们。
[charslot(slot = "middle", name = "avg_npc_799_1#1$1")]
[name="愤怒的武人"]这口气，我们咽不下......
[charslot(slot = "middle", name = "avg_npc_789_1#6$1")]
[name="孟铁衣"]你们都是城里的老人了。
[name="孟铁衣"]参与过几次守城的战斗，顶着天灾护送过几次信使，这玉门城的安定，有你们一份辛苦。
[charslot(slot = "middle", name = "avg_npc_789_1#5$1")]
[name="孟铁衣"]但平祟侯还在，宗师也还在，哪里轮得到你们靠资历摆谱？！
[charslot(slot = "middle", name = "avg_npc_799_1#1$1")]
[name="失落的武人"]坊主，你难道心里......
[charslot(slot = "middle", name = "avg_npc_789_1#10$1")]
[name="孟铁衣"]好汉不提当年勇，那点事，不拿出来说，也有人记得。记不得的，说了也没用。
[name="孟铁衣"]先回去，别闹事。有我在，死去的兄弟们少不了说法。
[charslot(slot = "middle", name = "avg_npc_796_1#1$1")]
[name="巡防营守军"]......
[charslot(slot = "middle", name = "avg_npc_799_1#1$1")]
[name="失落的武人"]......知道了。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot = "m", afrom = 1, ato = 0,duration = 1)]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_npc_789_1#10$1", duration =0.5)]
[charslot(slot = "right", name = "avg_npc_796_1#1$1", duration =0.5)]
[Delay(time=1.5)]
[charslot(slot = "left", name = "avg_npc_789_1#10$1",focus="l")]
[name="孟铁衣"]是我管教无方，给大家伙添麻烦了。
[charslot(slot = "right", name = "avg_npc_796_1#1$1", focus="r")]
[name="巡防营守军"]不怪孟前辈。
[name="巡防营守军"]那四位武行的兄弟......孟前辈节哀。
[charslot(slot = "left", name = "avg_npc_789_1#6$1",focus="l")]
[name="孟铁衣"]他们的家人，我会负责照顾，不劳平祟侯费心。
[charslot(slot = "left", name = "avg_npc_789_1#10$1",focus="l")]
[name="孟铁衣"]但他们是死在为玉门送信的路上，我想替大伙问一句，平祟侯对这件事，到底有什么说法。
[charslot(slot = "right", name = "avg_npc_796_1#1$1", focus="r")]
[name="巡防营守军"]事分轻重缓急，等捉拿了城中刺客，平祟侯一定会出兵清剿流寇。
[charslot(slot = "left", name = "avg_npc_789_1#10$1",focus="l")]
[name="孟铁衣"]好......“轻重缓急”，言之有理。
[charslot(slot = "left", name = "avg_npc_789_1#10$1",focus="l")]
[name="孟铁衣"]我只是要平祟侯的一句话，不管这句话是什么，我都带去回复弟兄们。
[charslot(slot = "left", name = "avg_npc_789_1#1$1",focus="l")]
[name="孟铁衣"]等事了，还是欢迎大伙再来铸剑坊喝酒。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_g1_yumenstreet_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "left", name = "avg_243_waaifu_1#1$1", duration =1)]
[charslot(slot = "right", name = "avg_npc_296_1#1$1", duration =1)]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_243_waaifu_1#1$1",focus="l")]
[name="槐琥"]雨霞姐。
[Dialog]
[charslot]
[charslot(slot = "middle", name = "avg_4080_lin_1#1$1",duration =1)]
[Delay(time=1.5)]
[name="林雨霞"]你们那边情况怎么样？牺牲者的家属，有没有找到？
[charslot]
[charslot(slot = "left", name = "avg_243_waaifu_1#1$1",focus="n")]
[charslot(slot = "right", name = "avg_npc_296_1#1$1",focus="r")]
[name="杜遥夜"]其实四个人中，有两人都是独自生活。
[name="杜遥夜"]至于另外两人，家属恰好都不在家，我们冒昧闯了进去......
[charslot(slot = "left", name = "avg_243_waaifu_1#5$1",focus="l")]
[name="槐琥"]有些奇怪，他们的家中一如往常......
[charslot(slot = "right", name = "avg_npc_296_1#9$1",focus="r")]
[name="杜遥夜"]也可能是家属正好外出不在......？
[charslot]
[charslot(slot = "middle", name = "avg_4080_lin_1#6$1")]
[name="林雨霞"]昨日信使队伍遇难的消息传回，已经过去了整整一天。
[charslot(slot = "middle", name = "avg_4080_lin_1#9$1")]
[name="林雨霞"]......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Background(image="35_g1_yumenstreet_d",x=30, y=0, xScale=1.3, yScale=1.3,fadetime=0)]
[charslot(slot = "left", name = "avg_npc_798_1#1$1")]
[charslot(slot = "right", name = "avg_npc_797_1#1$1")]
[charslot(slot = "left", posfrom = "0,0", posto = "-100,0",duration = 0)]
[backgroundTween(xFrom=30, yFrom=0, xTo=-30, yTo=0, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1.3, yScaleTo=1.3, duration=20, block=false)]
[curtain(direction = 0,fillfrom = 0,fillto = 0.2,fadetime=0.1,block=true)]
[curtain(direction = 4,fillfrom = 0,fillto = 0.2,fadetime=0.1,block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Dialog]
[charslot(slot = "m", name = "avg_npc_794_1#1$1",focus="l,r",duration=0.3)]
[charslot(slot = "m",posfrom = "0,0", posto = "250,0",duration = 0)]
[Delay(time=0.5)]
[charslot(slot = "m",  afrom = 1, ato = 0.3,focus="l,r",posfr

... (全文27949字符)
```

### level_act23side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="35_g2_yumenstreet_n",screenadapt="coverall")]
[playMusic(intro="$suspenseful_intro",key="$suspenseful_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot = "left", name = "avg_npc_793_1#1$1", duration =1)]
[charslot(slot = "right", name = "avg_npc_794_1#1$1", duration =1)]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_npc_793_1#1$1",focus="l")]
[name="山海众头目"]事没有成？
[charslot(slot = "r", name = "avg_npc_794_1#1$1",focus="r")]
[name="阴鸷的山海众成员"]两边都有意料之外的高人跟着，没机会下手。
[charslot(slot = "left", name = "avg_npc_793_1#1$1",focus="l")]
[name="山海众头目"]那个年轻秉烛人由他去查，于我们的计划无碍。
[name="山海众头目"]从龙门来的那个女人不在原本的计划之内，但偏偏找准了方向。
[name="山海众头目"]她很麻烦。
[charslot(slot = "r", name = "avg_npc_794_1#1$1",focus="r")]
[name="阴鸷的山海众成员"]我们会继续盯着，再找机会动手。
[charslot(slot = "left", name = "avg_npc_793_1#1$1",focus="l")]
[name="山海众头目"]不，经过两次冲突，官府的人想必也会提高警惕，现在开始我们要谨慎行事。
[name="山海众头目"]让那个女人多活两日尚可接受，可暴露组织的踪迹，则万万不能允许。
[charslot(slot = "r", name = "avg_npc_794_1#1$1",focus="r")]
[name="阴鸷的山海众成员"]是......那接下来，怎么办？
[charslot(slot = "left", name = "avg_npc_793_1#1$1",focus="l")]
[name="山海众头目"]等。先生下一步指令不会太久。
[name="山海众头目"]“山海八荒，尽归其主。”
[name="山海众头目"]身为大地的窃贼而不自知......这里的人们终究会为自己的傲慢付出代价。
[name="山海众头目"]时间很近了。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot="m",name="avg_npc_299_1#4$1",duration=1.5)]
[delay(time=2)]
[name="太合"]你们是在等谁？
[charslot(slot = "m", name = "avg_npc_793_1#1$1",focus="m")]
[name="山海众头目"]......
[charslot(slot="m",name="avg_npc_299_1#2$1")]
[name="太合"]刺杀朝廷命官，惊扰百姓安生，汝等所作所为，皆视大炎律法如无物。
[charslot(slot="m",name="avg_npc_299_1#1$1")]
[name="太合"]两个选择。
[name="太合"]放下兵器，跟我走；要么，我抓你们回去。
[charslot]
[charslot(slot = "left", name = "avg_npc_793_1#1$1",focus="l")]
[charslot(slot = "r", name = "avg_npc_794_1#1$1",focus="n")]
[name="山海众头目"]你被跟踪了。
[charslot(slot = "r", name = "avg_npc_794_1#1$1",focus="r")]
[name="阴鸷的山海众成员"]是刚刚那个人。
[charslot(slot = "left", name = "avg_npc_793_1#1$1",focus="l")]
[name="山海众头目"]他反过来跟踪了你。这人武功很高，你无能为力。
[name="山海众头目"]但终归是你将这人引到这里的，明白吗？
[charslot(slot = "r", name = "avg_npc_794_1#1$1",focus="r")]
[name="阴鸷的山海众成员"]明白。
[charslot]
[charslot(slot = "m", name = "avg_npc_793_1#1$1",focus="m")]
[name="山海众头目"]好，那先解决他，再谈对你的处置。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_299_1#5$1")]
[name="太合"]狂徒，还敢造次？！
[Dialog]
[StopMusic(fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_g3_yumenobservationtower_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(key="$m_avg_yumennormal_loop",volume=0.6)]
[Delay(time=1)]
[charslot(slot = "left", name = "avg_2024_chyue_1#1$1", duration =1)]
[charslot(slot = "right", name = "char_2005_weiyw_1#1", duration =1)]
[Delay(time=2)]
[charslot(slot = "r", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]夜深了，还没有休息？
[charslot(slot = "l", name = "avg_2024_chyue_1#1$1",focus="l")]
[name="重岳"]以防再发生昨天那样的变故，还是应该多留意点。
[charslot(slot = "r", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]宗师这么晚约见我，应该不是为了看风景吧？
[charslot(slot = "l", name = "avg_2024_chyue_1#9$1",focus="l")]
[name="重岳"]最后这段时间，难得魏公在，本来确实该好好在这玉门城里走走，看看玉门的风景。
[charslot(slot = "r", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]平祟侯的决定，自然有他的考量。
[name="魏彦吾"]这话或许不该我来说，平祟侯背负的，远远不止玉门这一座城的安危。
[name="魏彦吾"]一件事出岔的后果足够严重，“信任”二字就担不起什么分量了。
[charslot(slot = "l", name = "avg_2024_chyue_1#1$1",focus="l")]
[name="重岳"]的确如此。左将军与我共事几十载，靠的也不是“信任”。
[charslot(slot = "r", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]望重岳兄体谅。
[charslot(slot = "l", name = "avg_2024_chyue_1#10$1",focus="l")]
[name="重岳"]我又何曾抱怨过。
[charslot(slot = "r", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]说起来，还没有和重岳兄好好叙旧。
[name="魏彦吾"]我上次来玉门，还是五年前，再上一次，是十年前，但都很匆忙。
[charslot(slot = "l", name = "avg_2024_chyue_1#10$1",focus="l")]
[name="重岳"]而我们上一次见面，还要再往前数......是在京城。
[name="重岳"]嗯，魏公离京那年，我回去述职，正好在。
[charslot(slot = "r", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]没想到重岳兄还记得那么久远的事情。
[charslot(slot = "l", name = "avg_2024_chyue_1#10$1",focus="l")]
[name="重岳"]魏公不也记得？
[name="重岳"]具体是哪一年，我倒真想不起来了。印象里当时也是春天。
[charslot(slot = "r", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]晚春。比现在的时节稍微迟一些。
[charslot(slot = "l", name = "avg_2024_chyue_1#9$1",focus="l")]
[name="重岳"]是了。
[name="重岳"]当时魏公还是用剑的......不，当时你也还不姓“魏”。
[charslot(slot = "r", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]......
[charslot(slot = "l", name = "avg_2024_chyue_1#10$1",focus="l")]
[name="重岳"]好景千万，武功无数，日子一长，真能留下印象的，也没几个。
[name="重岳"]但即使现在品评各式武学的时候，也时常会想到赤霄剑法的最后一式。
[charslot(slot = "r", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]......能在武学上得宗师一句赞扬，我应该荣幸。
[charslot(slot = "l", name = "avg_2024_chyue_1#4$1",focus="l")]
[name="重岳"]那天晚上看着是要下雨的，闷热，云压得很低。
[name="重岳"]我在城楼上，隔得很远，但仍然看到了驿馆方向的剑光。
[charslot(slot = "l", name = "avg_2024_chyue_1#1$1",focus="l")]
[name="重岳"]一剑之寒，天光乍破。何其凌厉、何其果决的招式。
[name="重岳"]“云裂之剑，当立则立。”
[name="重岳"]之后，魏公就出城了吧。那场雨，最后也没有落下来。
[charslot(slot = "r", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]这倒真是一段久远的陈年旧事。
[name="魏彦吾"]就是不知宗师现在提起这事......
[Dialog]
[PlaySound(key="$d_avg_wind")]
[charslot(slot = "l",  afrom = 1, ato = 0,duration = 1)]
[charslot(slot ="r", afrom = 1, ato = 0,duration = 1)]
城楼凭高处，两人的衣袂扬起。
这本是个无风的晚上。
目之所及，玉门的房屋和哨楼在夜色中绵延，不见尽头。也只有通过高处的风，才能清楚感知到这座城市正在高速移动。
[charslot(slot = "l", name = "avg_2024_chyue_1#1$1",focus="l")]
[charslot(slot = "r", name = "char_2005_weiyw_1#1",focus="n")]
[name="重岳"]朝堂诡谲，人心难测，没有人比魏公更懂。
[name="重岳"]但我也相信，一个心中只有权谋伎俩的人，万万使不出那样的剑法。
[name="重岳"]有一件事，想请魏公帮忙。
[charslot(slot = "r", name = "char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]宗师亲自开口，不敢不听。
[charslot(slot = "l", name = "avg_2024_chyue_1#4$1",focus="l")]
[name="重岳"]我想请魏公相信玉门一次。
[charslot(slot = "r",

... (全文23354字符)
```

### level_act23side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="35_g2_yumenstreet_n",screenadapt="coverall")]
[playMusic(intro="$escape_intro",key="$escape_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_knockdoorfast")]
[charslot(slot = "m", name = "avg_npc_296_1#6$1",duration=0.5)]
[Delay(time=0.5)]
[name="杜遥夜"]孟叔，孟叔，你在里面吗？我有话要问你！
[name="杜遥夜"]我是杜遥夜！
[charslot]
[name="附近的游侠"]姑娘，别敲了，没看见门口挂的牌子啊。
[name="附近的游侠"]晚饭时候门就关了，你有啥事明天再来吧。
[Dialog]
[charslot(slot = "m", name = "avg_npc_296_1#6$1")]
[playsound(key="$d_avg_knockdoorfast")]
[Delay(time=2)]
[charslot]
[name="附近的游侠"]嘿，怎么还不理人......
[charslot(slot = "m", name = "avg_npc_296_1#5$1")]
[name="杜遥夜"]孟叔！你是不是有事瞒着我？
[name="杜遥夜"]再不答应，我就自己进去了。
[Dialog]
[charslot]
[playsound(key="$rungeneral",volume=0.7)]
[charslot(slot="m",name="avg_npc_297_1#6$1",duration=0.5)]
[delay(time=1)]
[name="左乐"]......
[charslot]
[name="附近的游侠"]又来一个......
[name="附近的游侠"]现在的年轻人怎么都大半夜往铁匠铺跑。
[charslot(slot="m",name="avg_npc_297_1#9$1")]
[name="左乐"]嗯？行裕客栈郑掌柜的......
[charslot(slot = "m", name = "avg_npc_296_1#7$1")]
[name="杜遥夜"]你是之前找过爹的那个年轻官差？
[charslot(slot="m",name="avg_npc_297_1#9$1")]
[name="左乐"]杜小姐何时来的玉门？此刻出现在这里又所为何事？
[charslot(slot = "m", name = "avg_npc_296_1#1$1")]
[name="杜遥夜"]找人。
[name="杜遥夜"]你又是来干嘛的？
[charslot(slot="m",name="avg_npc_297_1#7$1")]
[name="左乐"]查案。
[charslot(slot = "m", name = "avg_npc_296_1#9$1")]
[name="杜遥夜"]官府查到铸剑坊，难道孟叔他真的做了什么事？
[charslot(slot="m",name="avg_npc_297_1#9$1")]
[name="左乐"]听杜小姐的语气，这里果真有问题......
[charslot(slot = "m", name = "avg_npc_296_1#6$1")]
[name="杜遥夜"]是我在问你。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]......
[name="左乐"]倘若杜小姐和此事无关，还请不要耽误在下查案。
[charslot(slot = "m", name = "avg_npc_296_1#6$1")]
[name="杜遥夜"]谁在耽误谁......
[Dialog]
[charslot]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$swordtsing4")]
[PlaySound(key="$d_avg_smashcello",delay=0.2,volume=0.6)]
刀光硬生生截断了杜遥夜的话头。
[PlaySound(key="$d_avg_metalcollar")]
[PlaySound(key="$rungeneral",delay=0.3,volume=0.7)]
门锁落下，“暂停营业”的牌子碎成两半，左乐已经冲进了铸剑坊。
[Dialog]
[Delay(time=2)]
[name="附近的游侠"]（孟大哥只是让我盯着些，想不到真有人来闹事。）
[name="附近的游侠"]（不行，得去叫人来帮忙。）
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_g5_swordcastingworkshop",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="杜遥夜"]你干什么！
[Dialog]
[PlaySound(key="$rungeneral")]
[charslot(slot = "l", name = "avg_npc_297_1#6$1",duration = 1)]
[Delay(time=1)]
[name="左乐"]......
[Dialog]
[charslot(slot = "r", name = "avg_npc_296_1#6$1",duration = 1)]
[Delay(time=1)]
[charslot(slot = "right", focus = "right")]
[name="杜遥夜"]跟你说话呢！
[Dialog]
[charslot(slot = "right",posfrom = "0,0", posto = "-100,0",duration = 0.3)]
[Delay(time=0.3)]
[PlaySound(key="$fightgeneral",volume=0.7)]
[CameraShake(duration=0.3, xstrength=10, ystrength=8, vibrato=20, randomness=90, fadeout=true, block=false)]
[charslot(slot = "right",posfrom = "-100,0", posto = "0,0",duration = 0.3)]
[charslot(slot = "l", action="shake", power=10, times=100,random=30, duration=0.3)]
[Delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_297_1#3$1",focus="l")]
[name="左乐"]你——
[charslot(slot = "r", name = "avg_npc_296_1#5$1",focus="r")]
[name="杜遥夜"]打你怎么了！官差就是这么查案的？
[charslot(slot = "l", name = "avg_npc_297_1#6$1",focus="l")]
[name="左乐"]出来！
[Dialog]
[charslot]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_794_1#1$1",duration=1.5,bstart=0.2,bend=0.4)]
[delay(time=2.5)]
[charslot]
[charslot(slot = "m", name = "avg_npc_296_1#6$1")]
[name="杜遥夜"]......
[Dialog]
[StopMusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[charslot(slot="m",name="avg_4080_lin_1#1$1", focus = "none")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[PlaySound(key="$doorknockquite")]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4080_lin_1#1$1")]
[name="林雨霞"]进。
[Dialog]
[charslot]
[PlaySound(key="$dooropenquite",volume=0.7)]
[charslot(slot="m",name="avg_322_lmlee_1#10$1",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_4080_lin_1#1$1")]
[name="林雨霞"]鲤先生。
[charslot(slot="m",name="avg_322_lmlee_1#10$1")]
[name="老鲤"]刚看到槐琥跑了出去，风风火火的，我喊她都没答应。
[charslot(slot="m",name="avg_4080_lin_1#9$1")]
[name="林雨霞"]......
[charslot(slot="m",name="avg_322_lmlee_1#10$1")]
[name="老鲤"]毕竟才刚大学毕业，正是一腔热血的年纪，难免头脑简单，雨霞姑娘多教教她。
[charslot(slot="m",name="avg_4080_lin_1#1$1")]
[name="林雨霞"]鲤先生的员工，哪儿轮得到我来指手画脚。是我给她添麻烦了。
[charslot(slot="m",name="avg_322_lmlee_1#9$1")] 
[name="老鲤"]哪儿的话。年轻人嘛，多长长见识，也是好事。
[charslot(slot="m",name="avg_322_lmlee_1#10$1")] 
[name="老鲤"]凭那孩子的身手，就算遇到几个坏人，也用不着担心就是了。
[charslot(slot="m",name="avg_4080_lin_1#1$1")]
[name="林雨霞"]昨天晚上，爸他找过鲤先生，是有事情找您帮忙？
[charslot(slot="m",name="avg_322_lmlee_1#10$1")]
[name="老鲤"]也谈不上帮忙......只是在找人的时候顺便听到了一些故事，侦探的耳朵总是灵一点。
[name="老鲤"]要是能对雨霞姑娘查案有帮助，那就再好不过了。
[charslot(slot="m",name="avg_4080_lin_1#1$1")]
[name="林雨霞"]鲤先生请坐，讲故事总不能站着。
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot="m",name="avg_322_lmlee_1#10$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_322_lmlee_1#2$1")]
[name="老鲤"]让我想想该从何说起......
[charslot(slot="m",name="avg_322_lmlee_1#1$1")]
[name="老鲤"]打个比方，如果魏彦吾和令尊不合，那龙门会变成什么样子？
[charslot(slot="m",name="avg_4080_lin_1#8$1")]
[name="林雨霞"]......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=2)]
[Background(image="35_g3_yumenobservationtower_n",screenadapt="coverall")]
“天灾当前，城里又有山海众作乱，将军亲自带兵镇守城门，哪有工夫见一个百姓？”
“我听说这个人以前和将军认识。”
“还是通报一下吧，万一他真有什么事呢？”
......
“你上去吧，将军同意见你。”
“他就在城楼上。”
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[delay(time=2)]
夜已经很深了。
军用源石射灯嵌进城墙，随

... (全文24747字符)
```

### level_act23side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="35_g2_yumenstreet_n",screenadapt="coverall")]
[playMusic(intro="$darkness02_intro",key="$darkness02_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[name="客栈掌柜"]欸欸，莫名其妙闯进来，转了一圈就走，那汉子到底是干什么的？
[name="客栈伙计"]掌柜的，难道是巡防营的便衣，来看咱们有没有收留走私犯？
[name="客栈掌柜"]你看他直直愣愣莽莽撞撞的样子，哪有那么扎眼的便衣。
[name="客栈伙计"]那就是来挑事的，我去把他抓回来。
[name="客栈掌柜"]你追得上吗？人家一眨眼就去了半箭地，明显会轻功。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playsound(key="$d_avg_Qinggong")]
[charslot(slot = "middle", name = "avg_npc_785_1#1$1",duration =0.3)]
[charslot(slot = "m", posfrom = "-180,60", posto = "0,0",duration = 0.4)]
[delay(time=1)]
[name="魁梧的男人"]刚才是最后一间客栈，没有。
[charslot(slot = "middle", name = "avg_npc_785_1#8$1")]
[name="魁梧的男人"]那个女娃说要出城，但也不在城门口。
[charslot(slot = "middle", name = "avg_npc_785_1#3$1")]
[name="魁梧的男人"]她伤重，用的都是最好的药，要是追不回来，医生保不齐把这笔钱算在我的头上，那还了得。
[charslot(slot = "middle", name = "avg_npc_785_1#1$1")]
[name="魁梧的男人"]一定要把她逮回来。
[dialog]
[delay(time=0.5)]
[playsound(key="$d_avg_Qinggong")]
[charslot(slot = "m",posfrom = "0,0", posto = "350,80",times=1,duration = 0.7)]
[charslot(slot ="m", afrom = 1, ato = 0,duration = 0.2)]
[delay(time=0.3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot="m",name="avg_4080_lin_1#1$1")]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="林雨霞"]鲤先生的比方，我有点听不懂。
[charslot(slot="m",name="avg_322_lmlee_1#1$1")]
[name="老鲤"]只是个不恰当的例子。
[name="老鲤"]我在龙门开那一间小小的事务所，只为混口饭吃，没承想生意竟然不赖。
[name="老鲤"]可见羽毛蒜皮、腌臜琐碎的事，总少不了，也不能事事都指望魏彦吾和近卫局来处理。
[name="老鲤"]总得有林先生这样的好市民来帮忙。
[charslot(slot="m",name="avg_4080_lin_1#1$1")]
[name="林雨霞"]这是无可奈何的事情。
[charslot(slot="m",name="avg_322_lmlee_1#1$1")]
[name="老鲤"]是无可奈何......龙门如此，玉门也是如此。
[name="老鲤"]玉门终年在北部边境巡航，是为了将种种危险拒于大炎国门之外。
[name="老鲤"]可在早些年，源石技术还远没有发展到今天这个地步的时候，维系玉门这样一座移动要塞的正常运转，需要数倍的人力。
[name="老鲤"]好在那个时候，有那么一批有志于为国效力的习武之人，主动奔赴玉门。他们没有正式加入军伍，但实际上帮玉门解决了不少后顾之忧。
[name="老鲤"]护送信使，勘探前路，甚至是与军队同赴战场......玉门百年安稳，离不开他们。这些武人在城中，自然也是受人敬重。
[charslot(slot="m",name="avg_4080_lin_1#1$1")]
[name="林雨霞"]庙堂江湖，上下一心。
[charslot(slot="m",name="avg_322_lmlee_1#1$1")]
[name="老鲤"]这是玉门曾经的样子......直到二十年前的一场意外。
[charslot(slot="m",name="avg_4080_lin_1#1$1")]
[name="林雨霞"]山海众？
[charslot(slot="m",name="avg_322_lmlee_1#1$1")]
[name="老鲤"]没错。同样是因为山海众。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot="l",name="avg_npc_788_1#1$1")]
[charslot(slot="r",name="avg_npc_789_1#10$1")]
[Background(image="35_g3_yumenobservationtower_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_789_1#10$1",focus="r")]
[name="孟铁衣"]也没别的事了。
[name="孟铁衣"]希望没有耽误平祟侯的公务。不然我有几个脑袋也不够砍的。
[charslot(slot="l",name="avg_npc_788_1#1$1",focus="l")]
[name="左宣辽"]......
[name="左宣辽"]你明知道我不会同意。
[charslot(duration=0.5)]
[dialog]
[delay(time=1)]
[PlaySound(key="$d_avg_horn",volume=0.6)]
[delay(time=2)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=false)]
[PlaySound(key="$d_avg_spotlightc",volume=0.6)]
一声短暂的鸣笛后，城楼的军用源石照明系统突然关闭，两人的对话断入黑暗。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=false)]
只片刻工夫，摇曳的光明自远处亮起。
[PlaySound(key="$d_avg_soldiersstep",volume=0.5)]
军士们往来奔行，十步一岗，烽火次第传开。
[playsound(key="$d_avg_drum")]
十七声鼓在此时擂响，又被高速移动的玉门城泼进夜色，在空气中拖出逶迤的长音。
[dialog]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_788_1#1$1",focus="n")]
[charslot(slot="r",name="avg_npc_789_1#10$1",focus="r")]
[name="孟铁衣"]今天是望烽节的第二天。
[name="孟铁衣"]设立望烽节，是为了提醒玉门人铭记过往。
[name="孟铁衣"]这场见面，要么再早一些，要么再迟一些。
[name="孟铁衣"]那时候平祟侯应该已经想起了一些事。
[charslot(slot="l",name="avg_npc_788_1#1$1",focus="l")]
[name="左宣辽"]我从来没有忘记过。
[charslot(slot="r",name="avg_npc_789_1#10$1",focus="r")]
[name="孟铁衣"]平祟侯还记不记得，这些为玉门牺牲的英烈里，有多少并不是玉门的军士？
[name="孟铁衣"]他们不欠玉门的。
[charslot(slot="l",name="avg_npc_788_1#1$1",focus="l")]
[name="左宣辽"]玉门同样不亏欠任何人。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="r",name="avg_npc_789_1#2$1",focus="r")]
[name="孟铁衣"]姓左的！
[Dialog]
[charslot]
[playsound(key="$d_gen_soldiersrun")]
[charslot(slot = "left", name = "avg_npc_795_1#1$1",posfrom = "-200,0", posto = "0,0",duration = 1)]
[charslot(slot = "right", name = "avg_npc_796_1#1$1",posfrom = "200,0", posto = "0,0",duration = 1)]
[Delay(time=2)]
[name="巡防营守军"]......
[charslot]
[charslot(slot="m",name="avg_npc_788_1#1$1")]
[name="左宣辽"]退下。
[charslot(slot="m",name="avg_npc_789_1#5$1")]
[name="孟铁衣"]二十年前，我的确疏忽大意，让那伙贼人乔装成玉门武人，混进城伤了百姓。你可以怨我，哪怕让我偿命！
[name="孟铁衣"]但你要问罪，也只该问我，或者问你自己！
[charslot(slot="m",name="avg_npc_788_1#7$1")]
[name="左宣辽"]一切罪责，当然由我一人承担。
[charslot(slot="m",name="avg_npc_789_1#2$1")]
[name="孟铁衣"]你是怎么承担的？这么多年来，疏远那些为玉门流过血汗的江湖兄弟，甚至要把他们通通逼走，就算你承担了吗？！
[charslot(slot="m",name="avg_npc_788_1#8$1")]
[name="左宣辽"]......
[charslot(slot="m",name="avg_npc_789_1#5$1")]
[name="孟铁衣"]玉门要给他们一个交代！
[charslot(slot="m",name="avg_npc_788_1#7$1")]
[name="左宣辽"]玉门是大炎的玉门。它做的所有事，都是为了保亿万大炎百姓平安。这便是我的交代。
[charslot(slot="m",name="avg_npc_788_1#2$1")]
[name="左宣辽"]请回吧。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot="m",name="avg_322_lmlee_1#1$1")]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_322_lmlee_1#1$1")]
[name="老鲤"]“山海众”，不是人人都知道的名字。
[name="老鲤"]也不能怪谁疏忽，当时只知道戒备外敌，并不知道暗处还有敌人想对玉门不利。
[name="老鲤"]镖客、拳师、武器工匠......这些玉门武人常与守军并肩作战，当年在玉门城内也算往来自由。山海众恰恰利用了这一点。
[charslot(slot="m",name="avg_322_lmlee_1#6$1")]
[name="老鲤"]城中缺少防备，各方面反应都慢了一步。虽然最终阻止了山海众破坏城市核心动力源的计划，但还是承受了不少伤亡。
[name="老鲤"]打那之后......
[charslot(slot="m",name="avg_4080_lin_1#1$1")]
[name="林雨霞"]应该是亡兽补牢，为时不晚。
[charslot(slot="m",name="avg_322_lmlee_1#2$1")]
[name="老鲤"]不如说，“矫枉过正”？
[charslot(slot="m",na

... (全文25208字符)
```

### level_act23side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="35_g1_yumenstreet_d",screenadapt="coverall")]
[playMusic(intro="$tech_intro",key="$tech_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
日渐西斜。
人和城墙的影子都被拉得很长。影子盖过了路边的铺面，店家便收起阳伞，伸了一个漫长的懒腰。
[name="慵懒的摊贩"]最后几件，七折清仓，卖完回家吃饭喽——
[name="无聊的摊贩"]回去吧，还惦记着卖你那没开刃的兵器模型呐，现在的游客早就不吃那套了。
[name="慵懒的摊贩"]我要真会铸剑的手艺，肯定也得去军营里做些大事。
[name="无聊的摊贩"]说起来，昨天我还真见到一个游客佩着一把赤红色的剑，看起来真不一般。也不知道是从哪儿搞来的......
[Dialog]
[delay(time=1)]
[charslot(slot="m",name="avg_4078_bdhkgt_1#1$1",duration=1)]
[delay(time=2)]
[charslot(slot = "m", focus = "none")]
少女茫然地看着四周。眼前尽是从未见过的景象。
脚下地面传来隐隐的震动感，大概是移动城市减速的征兆。但路上的行人却似乎习以为常，有条不紊地做着平常的事。
晚饭的香气钻入鼻腔。少女这才想起，自己已经整整两天没有吃过东西。
[Dialog]
[charslot(slot = "m",name="avg_4078_bdhkgt_1#2$1",focus = "m")]
[name="截云"]......
[charslot(slot = "m", focus = "none")]
浑身的酸痛随着饿意一起袭来。
双腿也不听自己使唤，跟着香味走向了一家饭馆。
[charslot(slot = "m", focus = "m")]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_doorbell")]
[charslot(slot="m",name="avg_4078_bdhkgt_1#1$1",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_303_1#1$1")]
[name="伙计"]客人要点什么？
[charslot(slot="m",name="avg_4078_bdhkgt_1#8$1")]
[name="截云"]旁边那桌人吃的......我也要一样的。
[charslot(slot="m",name="avg_npc_303_1#1$1")]
[name="伙计"]好嘞，三号桌烤肉凉面一份——
[charslot]
临近晚饭的时间，店里已经差不多坐满。对于朴实的人们来说，忙碌了一天后，一顿踏实的晚饭，就是最好的慰藉。
墙上的电视机里循环播放着刀光剑影的故事，偶有食客抬起头，被熟悉的桥段吸引一阵注意力。
[charslot(slot="m",name="avg_4078_bdhkgt_1#6$1")]
[name="截云"]（这个盒子里的人，为什么看起来和他一模一样？）
[charslot(slot="m",name="avg_4078_bdhkgt_1#8$1")]
[name="截云"]（他旁边的女侠，和师父有点像，又不太像......）
[charslot(slot="m",name="avg_4078_bdhkgt_1#2$1")]
[name="截云"]（“故事由真实事件改编”又是什么意思......）
[charslot(slot="m",name="avg_npc_303_1#1$1")]
[playsound(key="$d_avg_glassclink")]
[name="伙计"]客官您的面来了，慢用。
[charslot(slot="m",name="avg_4078_bdhkgt_1#1$1")]
[name="截云"]谢......谢谢。
[charslot(slot = "m", focus = "none")]
[name="居民A"]我就说应该送一幅百米长卷，让城里每个人都签上名字，这样的饯别礼物才有意义！
[name="居民B"]你是不是傻，宗师是要走的，这么大一件东西你让他怎么带得走？
[name="居民B"]反正都是心意，不如多备点我们这儿的特色美食，还实在一点。
[name="居民A"]我说......那位宗师到底守了玉门多少年？
[name="居民B"]具体我也说不清楚，只知道我爹那一辈的人出生的时候，宗师就已经守在这儿了。
[name="居民A"]那他岂不是已经有一百多岁了？怪不得要离任，应该是身体吃不消了吧。
[name="居民B"]可我听一些江湖人说，就在前阵子还有人见过他。看上去就是一副平常中年男人的样貌。
[name="居民A"]那位宗师，不是正常人......？
[name="居民B"]听说这世上有些人，就是有用法术延年益寿的本事，宗师他大概也是吧。
[name="居民B"]不管他到底是什么人，我们只要记得他是守护玉门城的大英雄，住在这儿的人，都应该记着他的好。
[name="居民B"]只可惜，从来没有听说宗师他有过婚配，或是有一儿半女的。明明左将军的公子都这么大了，真是......
[charslot(slot = "m", focus = "m")]
[charslot(slot="m",name="avg_4078_bdhkgt_1#8$1")]
[name="截云"]（他们说，那个人是......英雄？）
[charslot(slot="m",name="avg_npc_303_1#1$1")]
[name="伙计"]姑娘，这饭也吃完了......还算合口味？
[charslot(slot="m",name="avg_4078_bdhkgt_1#9$1")]
[name="截云"]谢谢，很好吃。
[charslot(slot="m",name="avg_npc_303_1#1$1")]
[name="伙计"]那这饭钱......
[charslot(slot="m",name="avg_4078_bdhkgt_1#11$1")]
[name="截云"]我......
[charslot(slot="m",name="avg_243_waaifu_1#4$1")]
[name="槐琥"]我来付吧。
[charslot(slot="m",name="avg_4078_bdhkgt_1#6$1")]
[name="截云"]谢、谢谢你......
[charslot(slot="m",name="avg_243_waaifu_1#4$1")]
[name="槐琥"]倒没什么啦......真巧，又见面了。
[name="槐琥"]你是弄丢了钱包，还是忘了带够钱？
[charslot(slot="m",name="avg_4078_bdhkgt_1#2$1")]
[name="截云"]是......弄丢了......
[charslot(slot="m",name="avg_243_waaifu_1#7$1")]
[name="槐琥"]欸？真倒霉。
[name="槐琥"]看起来你也是刚来的样子，应该对这里也不熟悉。我和你一起去报官吧。
[charslot(slot="m",name="avg_4078_bdhkgt_1#6$1")]
[name="截云"]谢谢你的好意，还是不用了！
[charslot(slot="m",name="avg_4078_bdhkgt_1#6$1")]
[name="截云"]这次的饭钱，我回头会还给你的！
[charslot(slot="m",name="avg_243_waaifu_1#7$1")]
[name="槐琥"]等一等。
[charslot(slot="m",name="avg_4078_bdhkgt_1#7$1")]
[name="截云"]？！
[charslot(slot="m",name="avg_243_waaifu_1#2$1")]
[name="槐琥"]你带着的这把剑......就是你之前说过，要找的那把？
[charslot(slot="m",name="avg_4078_bdhkgt_1#7$1")]
[name="截云"]你也要抢么？！
[charslot(slot="m",name="avg_243_waaifu_1#1$1")]
[name="槐琥"]我怎么会平白无故抢别人的东西......
[charslot(slot="m",name="avg_243_waaifu_1#5$1")]
[name="槐琥"]但我听说，最近城中有一把很特殊的剑失窃，该不会就是......
[charslot(slot="m",name="avg_4078_bdhkgt_1#2$1")]
[name="截云"]......先告辞了。
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "200,0",duration = 1)]
[charslot(duration=0.6)]
[playsound(key="$rungeneral",volume=0.6)]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_g13_yanlivingroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playsound(key="$dooropenquite")]
[charslot(slot="m",name="avg_npc_785_1#1$1",duration=0.5)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_785_1#11$1")]
[name="槐天裴"]有人......？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_785_1#7$1")]
[name="槐天裴"]出来！
[dialog]
[charslot]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[charslot(slot="m",name="avg_322_lmlee_1#10$1",duration=1)]
[delay(time=1)]
[name="老鲤"]听说不能和习武之人开这种玩笑。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_295_1#8$1",duration=1)]
[delay(time=1)]
[name="梁洵"]何况是世上所有习武之人里练得最刻苦、最厉害的那个。
[charslot]
[charslot(slot = "l", name = "avg_322_lmlee_1#10$1",focus="l")]
[charslot(slot = "r", name = "avg_npc_295_1#8$1",focus="n")]
[name="老鲤"]他要是一个条件反射，闭着眼对我一拳挥过来，我是不是就要交待在这了？
[charslot(slot = "r", name = "avg_npc_295_1#8$1",focus="r")]
[name="梁洵"]那我也只好把他抓起来，判一个过失杀人。
[charslot]
[charslot(slot = "m", name = "avg_npc_785_1#6$1")]
[name="槐天裴"]......
[charslot]
[charslot(slot = "l", name = "avg_322_lmlee_1#10$1",focus="l")]
[charslot(slot = "r", name = "avg_npc_295_1#8$1",focus="n")]
[name="老鲤"]梁大人，怎么说，刚才那个赌该算我赢了？
[charslot(slot = "r", name = "avg_npc_295_1#8$1",focus="r")]
[name="梁洵"]......确实。
[charslot(slot = "l", name = "avg_322_lmlee_1#10$1",focus="l")]
[name="老鲤"]我刚才和梁洵打赌，就赌你进门看见我俩是什么反应。
[name="老鲤"]他赌你会扭头就走，我赌你会愣在原地一句话都讲不出来。
[

... (全文16279字符)
```

### level_act23side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="35_g6_yumengate",screenadapt="coverall")]
[playMusic(intro="$prisonbreak_intro",key="$prisonbreak_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_243_waaifu_1#10$1",duration=0.3)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_794_1#1$1",duration=0.3)]
[charslot(slot = "l", posfrom = "-300,0", posto = "-100,0",duration = 0.3)]
[delay(time=0.2)]
[charslot(slot = "m", name = "avg_243_waaifu_1#1$1")]
[charslot(slot = "m", posfrom = "0,0", posto = "-150,0",duration = 0.3)]
[PlaySound(key="$d_avg_punchsp3")]
[delay(time=0.3)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "l", posfrom = "-100,0", posto = "-500,0",duration = 0.5)]
[delay(time=0.3)]
[charslot(slot = "l",  afrom = 1, ato = 0,duration = 0.3)]
[delay(time=0.3)]
[charslot(slot = "r", name = "avg_npc_794_1#1$1",duration=0.3)]
[charslot(slot = "r", posfrom = "0,0", posto = "100,0",duration = 0)]
[delay(time=0.3)]
[charslot(slot = "l", name = "avg_npc_794_1#1$1",afrom = 0.3, ato = 0.3,duration=0.2)]
[charslot(slot = "l", posfrom = "0,0", posto = "350,0",duration = 0)]
[charslot(slot = "r", posfrom = "100,0", posto = "180,0",duration = 0.3)]
[charslot(slot = "l", posfrom = "350,0", posto = "480,0",duration = 0.2)]
[delay(time=0.1)]
[charslot(slot = "l", afrom = 0.3, ato = 0,duration = 0.1)]
[delay(time=0.3)]
[charslot(slot = "r", posfrom = "180,0", posto = "-80,0",duration = 0.3)]
[delay(time=0.2)]
[charslot(slot = "m", posfrom = "-150,0", posto = "-300,0",duration = 0.3)]
[delay(time=0.4)]
[charslot(slot = "m", posfrom = "-250,0", posto = "-50,0",duration = 0.3)]
[delay(time=0.2)]
[CameraShake(duration=1, xstrength=30, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r", action="shake", power=50, times=100,random=30, duration=0.5)]
[PlaySound(key="$d_avg_punchsp5")]
[PlaySound(key="$d_avg_punchsp1",delay=0.1)]
[PlaySound(key="$d_avg_punchsp5",channel="a",delay=0.2)]
[PlaySound(key="$d_avg_punchsp4",delay=0.7)]
[delay(time=0.7)]
[CameraShake(duration=0.3, xstrength=30, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r", posfrom = "-80,0", posto = "400,30",duration = 0.5)]
[delay(time=0.2)]
[charslot(slot = "r",  afrom = 1, ato = 0,duration = 0.4)]
[delay(time=0.8)]
[charslot(slot = "l", name = "avg_npc_794_1#1$1",duration = 1)]
[charslot(slot = "l", posfrom = "480,0", posto = "-320,0",duration = 0)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_794_1#1$1",duration = 1)]
[charslot(slot = "r", posfrom = "400,0", posto = "300,0",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_243_waaifu_1#8$1",focus="m")]
[name="槐琥"]（这些人配合还真默契......到底还有多少人？）
[charslot]
[dialog]
[playsound(key="$d_avg_wolflordthreat")]
[charslot(slot = "m", name = "avg_npc_800_1#1$1",duration = 1)]
[delay(time=0.5)]
[name="长相凶狠的生物"]（低沉的嘶吼）
[charslot]
[charslot(slot = "l", name = "avg_npc_794_1#1$1")]
[charslot(slot = "r", name = "avg_npc_794_1#1$1")]
[name="山海众成员"]......
[Dialog]
[playsound(key="$d_gen_soldiersrun",volume=0.7)]
[charslot(slot = "l",  afrom = 1, ato = 0,duration = 1)]
[Delay(time=0.3)]
[charslot(slot ="r",afrom = 1, ato = 0,duration = 1)]
[Delay(time=2.5)]
[charslot]
[charslot(slot = "m", name = "avg_243_waaifu_1#7$1")]
[name="槐琥"]咦，这些人为什么突然间都不打了？
[dialog]
[charslot]
[charslot(slot = "r", name = "avg_4078_bdhkgt_1#1$1",duration=0.3)]
[Delay(time=0.5)]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[charslot(slot = "l", name = "avg_243_waaifu_1#1$1")]
[charslot(slot = "l", posfrom = "-250,0", posto = "0,0",duration = 1)]
[Delay(time=1.5)]
[charslot(slot = "l", name = "avg_243_waaifu_1#1$1",focus="l")]
[name="槐琥"]他们为什么要找你？
[charslot(slot = "r", name = "avg_4078_bdhkgt_1#1$1",focus="r")]
[name="截云"]你叫什么名字？
[charslot(slot = "l", name = "avg_243_waaifu_1#1$1",focus="l")]
[name="槐琥"]槐琥。槐树的槐，琥珀的琥。
[charslot(slot = "r", name = "avg_4078_bdhkgt_1#8$1",focus="r")]
[name="截云"]槐琥......我记住了。
[charslot(slot = "r", name = "avg_4078_bdhkgt_1#1$1",focus="r")]
[name="截云"]我叫截云。
[name="截云"]等我回来的时候，也会来找你的。
[Dialog]
[playsound(key="$rungeneral",volume=0.7)]
[charslot(slot = "r", posfrom = "0,0", posto = "350,0",duration = 1)]
[charslot(slot ="r",afrom = 1, ato = 0,duration = 1)]
[Delay(time=2)]
[charslot(slot = "l", name = "avg_243_waaifu_1#7$1")]
[name="槐琥"]等——
[charslot(slot = "l", name = "avg_243_waaifu_1#2$1")]
[name="槐琥"]奇怪的人......
[charslot(slot = "l", name = "avg_243_waaifu_1#5$1")]
[name="槐琥"]......
[name="槐琥"]还是先去抓那些坏人吧。
[stopmusic(fadetime=2)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[charslot(slot="m",name="avg_npc_301_1#1$1",focus="n")]
[Background(image="35_g7_zuosroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$storyendjp_intro",key="$storyendjp_loop", volume=0.6)]
[delay(time=1)]
老人的目光在地图上游移，勾勒出一条航线。
他看得很慢，他知道图纸上的每一寸画面，象征的是何等辽阔的土地。
桌案一旁的茶杯里，早已没了热气。
[dialog]
[charslot]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[charslot(slot="m",name="avg_2024_chyue_1#1$1",duration=1.5)]
[delay(time=2)]
[name="重岳"]这玉门的粗茶，还以为太傅会喝不惯。
[charslot(slot="m",name="avg_npc_301_1#1$1")]
[name="太傅"]留守这里的将士百姓喝的都是这种茶，我如何喝不得。
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]天气还未变暖，不适宜喝这凉茶。
[name="重岳"]太傅缝补天下事，却唯独没将自己的身体放在心上。
[name="重岳"]你要是倒下了，让其他人如何是好。
[charslot(slot="m",name="avg_npc_301_1#2$1")]
[name="太傅"]我若是倒下了，自然会有更优秀的后来人接替我的位置。江山代有才俊，炎国没有离不开谁的道理。
[charslot(slot="m",name="avg_npc_301_1#1$1")]
[name="太傅"]流水不腐，户枢不蠹。重要的不是一人一世，而是传承。
[name="太傅"]人生代代，自古如此。
[charslot(slot="m",name="avg_2024_chyue_1#9$1")]
[name="重岳"]“传承”。
[name="重岳"]对我们来说，恐怕是很难理解的一个词。
[charslot(slot="m",name="avg_npc_301_1#1$1")]
[name="太傅"]但你还是教出了无数于大炎有用的人才。
[name="太傅"]历任录武官对武学招式的记录还留作军队的训练教材，

... (全文20245字符)
```

### level_act23side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.6)]
[Delay(time=1)]
[Background(image="bg_warehouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot = "l", name = "avg_npc_794_1#1$1",duration=0.3)]
[charslot(slot = "l", posfrom = "0,0", posto = "-150,0",duration = 0)]
[delay(time=0.3)]
[charslot(slot = "m", name = "avg_npc_789_1#5$1",duration=0.3)]
[charslot(slot = "m", posfrom = "0,0", posto = "0,200",duration = 0)]
[PlaySound(key="$d_avg_Qinggong")]
[charslot(slot = "m", posfrom = "0,200", posto = "-50,-10",duration = 0.2)]
[delay(time=0.4)]
[charslot(slot = "m", action="jump",posto = "-100,10",power=-10,times=1,duration = 0.2)]
[PlaySound(key="$d_avg_singleblunt")]
[PlaySound(key="$d_avg_hammer", volume=0.8)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "l",  afrom = 1, ato = 0,posfrom = "-150,0", posto = "-300,-70",duration = 0.3)]
[delay(time=0.7)]
[charslot(slot = "r", name = "avg_npc_794_1#1$1",duration=0.3)]
[charslot(slot = "r", posfrom = "300,0", posto = "0,0",duration = 0.3)]
[delay(time=0.1)]
[charslot(slot = "m", name = "avg_npc_789_1#5$1")]
[charslot(slot = "m", action="jump",posto = "200,0",power=10,times=1,duration = 0.5)]
[PlaySound(key="$d_avg_twohandedblunt")]
[PlaySound(key="$d_avg_hammer", volume=0.8)]
[PlaySound(key="$bodyfalldown2",delay=0.5)]
[delay(time=0.3)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r",action="jump",posto = "500,30",power=10,times=1,duration = 0.5)]
[delay(time=0.2)]
[charslot(slot = "r",  afrom = 1, ato = 0,duration = 0.4)]
[delay(time=0.6)]
[charslot(slot ="m", afrom = 1, ato = 0,duration = 0.3)]
一个，两个，三个。
挥锤。
七千多个日夜，他都如此般挥锤。
他多么希望锤头不是落在未成形的铁坯，而是仇人的刀刃上，头颅上。
[PlaySound(key="$d_avg_hammer")]
[PlaySound(key="$bodyfalldown1",delay=0.8)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
就像，现在！
[dialog]
[delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_npc_786_1#1$2",duration=0.5)]
[delay(time=0.6)]
[name="山海众首领"]你们退下。
[charslot]
[Dialog]
[PlaySound(key="$e_skill_skulsrsword")]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_hammer",delay=0.2)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_786_1#1$2",duration=0.5)]
[delay(time=1)]
[name="山海众首领"]......锤很沉，但不够快。
[charslot(slot="m",name="avg_npc_789_1#5$1")]
[name="孟铁衣"]很沉就够了，很沉就能砸断你的刀，再砸烂你的脑袋！
[charslot(slot="m",name="avg_npc_786_1#1$2")]
[name="山海众首领"]......
[charslot(slot="m",name="avg_npc_789_1#5$1")]
[name="孟铁衣"]不不不，我原本为你们设计了更好的死法。我本应该在这间仓库里埋满炸药，天灾来的时候，用你们山海众的命为玉门祭旗！
[name="孟铁衣"]当然，包括我自己。
[charslot(slot="m",name="avg_npc_786_1#1$2")]
[name="山海众首领"]这才是你的计划？
[charslot(slot="m",name="avg_npc_789_1#2$1")]
[name="孟铁衣"]不然，我为什么要主动找你们合作？！
[charslot(duration=0.3)]
[Dialog]
[charslot(slot = "m", posfrom = "0,0", posto = "200,0",duration = 0.4)]
[delay(time=0.5)]
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$d_avg_hammer")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[PlaySound(key="$swordtsing3",delay=0.1)]
[PlaySound(key="$swordtsing4",delay=0.2)]
[delay(time=1)]
[charslot]
[charslot(slot="m",name="avg_npc_786_1#1$2")]
[name="山海众首领"]我们似乎，没有这么大的仇。
[charslot(slot="m",name="avg_npc_789_1#5$1")]
[name="孟铁衣"]当初你们是如何混进玉门，如何乔装成武人骗取守军信任，如何到处作乱，玉门又是如何变成今天的样子！
[name="孟铁衣"]记性，未免太差！
[charslot(slot="m",name="avg_npc_786_1#2$2")]
[name="山海众首领"]......
[charslot(slot="m",name="avg_npc_789_1#5$1")]
[name="孟铁衣"]你们这帮宵小出现在城里的第一天，我就认出来了。
[CameraShake(duration=0.7, xstrength=30, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_789_1#2$1")]
[name="孟铁衣"]我可是等了你们，二十年！
[charslot]
[Dialog]
[PlaySound(key="$d_avg_twohandedblunt")]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.03, block=true)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_skill_skulsrsword",delay=0.2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=false)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_789_1#5$1")]
[name="孟铁衣"]可惜啊可惜，一点意外，满盘皆输......
[name="孟铁衣"]但幸好，我还有这把锤！
[Dialog]
[PlaySound(key="$d_avg_twohandedblunt")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[charslot(slot="m",name="avg_4080_lin_1#12$1",focus="n")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_soldiersrun")]
[delay(time=2)]
仓库里光线昏暗，林雨霞手上的玻璃剑刃反而越发透明。
山海众似乎对她精妙的源石技艺有些忌惮，没有一拥而上，而是彼此配合，慢慢缩小着包围。
[charslot(slot="m",name="avg_4080_lin_1#12$1")]
[name="林雨霞"]（这样一伙人，居然能在城市里神出鬼没这么久不被发现......）
[name="林雨霞"]（不是民间的武术流派，也不是哪国的军方格斗术，但狠辣凌厉，而且远近分工，配合默契......究竟是什么来历？）
[charslot(slot="m",name="avg_4080_lin_1#9$1")]
[name="林雨霞"]（如果是陈的剑，大概更适合对付这些家伙......）
[charslot(slot="m",name="avg_4080_lin_1#2$1")]
[name="林雨霞"]（瞎想什么......当务之急是要想办法尽快脱身，把真的数据带出去。）
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_296_1#5$1",posfrom = "0,0", posto = "100,150",duration = 0,isblock=true)]
[PlaySound(key="$d_avg_Qinggong")]
[charslot(slot = "m", posfrom = "100,150", posto = "0,0",duration = 0.4,isblock=true)]
[name="杜遥夜"]喂，我来帮忙！
[charslot]
[charslot(slot="m",name="avg_4080_lin_1#6$1")]
[name="林雨霞"]......
[name="林雨霞"]你不该还留在这儿。
[charslot(slot="m",name="avg_npc_296_1#6$1")]
[name="杜遥夜"]刚把大小齐送出去，听到这边有打斗声——果然又是这伙人。
[charslot(slot="m",name="avg_4080_lin_1#7$1")]
[name="林雨霞"]你

... (全文32726字符)
```

### level_act23side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[playMusic(intro="$darkness02_intro",key="$darkness02_loop", volume=0.6)]
[Delay(time=1)]
[Background(image="35_g2_yumenstreet_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$rungeneral",volume=0.7)]
[charslot(slot="m",name="avg_npc_296_1#6$1",duration=0.5)]
[Delay(time=1)]
[name="杜遥夜"]来人！来人啊！
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[charslot(slot="m",name="avg_npc_796_1#1$1",duration=1)]
[Delay(time=2)]
[name="巡防营守军"]怎么又是你！不是刚把你放出来？
[name="巡防营守军"]再闹事，我可真要对你不客气了！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_296_1#5$1")]
[name="杜遥夜"]呆子！
[charslot(slot="m",name="avg_npc_296_1#1$3")]
[name="杜遥夜"]这个盒子里装的是能救整座玉门城的东西，别废话快送给左......
[Dialog]
[PlaySound(key="$bodyfalldown2",volume=0.7)]
[charslot(slot ="m", afrom = 1, ato = 0, posfrom = "0,0", posto = "0,-50",duration = 0.6)]
[Delay(time=1)]
[charslot]
[charslot(slot="m",name="avg_npc_796_1#1$1",duration=0.3)]
[Delay(time=1)]
[name="巡防营守军"]这是......钦天监的数据匣？还有令牌？
[name="巡防营守军"]喂，小姑娘？这东西怎么在你手里，醒醒！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="巡防营守军"]快！叫军医！
[stopmusic(fadetime=2)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_g2_yumenstreet_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_snowstormflp", loop=true,volume=0.5, channel="bgs")]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.6)]
[Blocker(a=0.3, r=0.3, g=0.2, b=0.1, fadetime=0.1, block=true)]
[CameraShake(duration=0.5,xstrength=30,ystrength=25,vibrato=30,randomness=90,fadeout=true,block=false)]
[PlaySound(key="$d_avg_glassbroken")]
[PlaySound(key="$d_avg_katanamagic", volume=1,delay=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=false)]
[Delay(time=0.5)]
[CameraShake(duration=0.3,xstrength=20,ystrength=15,vibrato=30,randomness=90,fadeout=true,block=false)]
[PlaySound(key="$swordtsing4",delay=0.1)]
[PlaySound(key="$swordtsing5",delay=0.3)]
[Delay(time=0.5)]
[Blocker(a=0.3, r=0.95, g=0.3, b=0.3, fadetime=0.1, block=true)]
[CameraShake(duration=0.5,xstrength=25,ystrength=10,vibrato=30,randomness=90,fadeout=true,block=false)]
[PlaySound(key="$d_avg_chixiaosword")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=false)]
[Delay(time=0.5)]
[Blocker(a=1, r=0.95, g=0.95, b=0.95, fadetime=0.1, block=true)]
[CameraShake(duration=1,xstrength=20,ystrength=15,vibrato=30,randomness=90,fadeout=true,block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.7)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_790_1#6$1",posfrom = "-100,0", posto = "0,0",duration = 0.5)]
[delay(time=1)]
[name="陈"]这个人，到底是什么来头？
[Dialog]
[charslot]
[PlaySound(key="$e_skill_driftsand", volume=0.8)]
[PlaySound(key="$d_avg_sandstone", volume=0.8)]
[CameraShake(duration=0.3,xstrength=25,ystrength=10,vibrato=30,randomness=90,fadeout=true,block=false)]
[charslot(slot = "m", name = "avg_4080_lin_1#12$1",duration = 0.5)]
[delay(time=1)]
[name="林雨霞"]陈警司也会感叹遇到对手了？
[charslot(slot = "m", name = "avg_npc_790_1#6$1")]
[name="陈"]她的源石技艺，赤霄斩不开。
[name="陈"]如果这真的算是源石技艺的话......
[Charslot]
[Dialog]
[PlaySound(key="$d_avg_ftrub", volume=1)]
[charslot(slot = "m", name = "avg_243_waaifu_1#1$1",posfrom = "150,0", posto = "0,0",duration = 0.5)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_243_waaifu_1#5$1")]
[name="槐琥"]她好像也根本不会什么武功招式，但出刀实在快得离谱。
[name="槐琥"]就好像，那种瞎编的武功秘籍上写的什么“移形换影”一样，真的能无视空间距离。
[charslot(slot = "m", name = "avg_243_waaifu_1#1$1")]
[name="槐琥"]我和她多对几招，看能不能摸清楚......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_spear")]
[PlaySound(key="$swordtsing6",delay=0.2)]
[CameraShake(duration=0.3,xstrength=25,ystrength=10,vibrato=30,randomness=90,fadeout=true,block=false)]
[charslot(slot = "m", name = "avg_npc_787_1#11$1",duration = 0.3)]
[delay(time=1)]
[name="仇白"]小心点，她可不是在和我们比试。
[name="仇白"]不留神的话，真的会死的。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_786_1#1$2",duration=0.5)]
[delay(time=1)]
[name="山海众首领"]......
[name="山海众首领"]留神的话，也会死。
[name="山海众首领"]是你说要和我多对几招？那就从你开始。
[charslot(slot = "m", name = "avg_243_waaifu_1#10$1")]
[StopMusic(fadetime=1)]
[StopSound(channel="bgs", fadetime=3)]
[CameraShake(duration=0.3,xstrength=25,ystrength=26,vibrato=30,randomness=90,fadeout=true,block=false)]
[name="槐琥"]——！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_katanamagic")]
[Effect(name="$e_bladeline_01_large",x =0,y=-100,rox=60,roy=10,roz=-40,layer = 1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
刀比刚才交手时更快，槐琥只觉得瑟瑟秋风扑面而来，根本没法做出什么反应。
[PlaySound(key="$d_avg_punchsp2")]
自己的面前突然多了一堵墙，或者说，一堵墙般宽阔厚实的背。
槐琥看着眼前的背影，已经十几年没有见过，但还是和记忆里的模样重叠起来。
重逢比想象的要更快，也更猝不及防。
[Dialog]
[playMusic(key="$m_avg_riversnow_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_785_1#1$1",bstart=0.3,bend=0.9,focus="m",isCopy=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_785_1#1$1",posfrom = "0,0", posto = "200,0",focus="n",isCopy=true)]
[charslot(slot = "m", name = "avg_npc_785_1#1$1",bstart=0,bend=0,duration=3,focus="m")]
[delay(time=3.5)]
[name="槐天裴"]鲤说的麻烦事，就是这个人？
[charslot]
[charslot(slot = "m", name = "avg_npc_786_1#6$2")]
[name="山海众首领"]又是你？
[charslot(slot = "m", name = "avg_npc_785_1#11$1")]
[name="槐天裴"]我说这几天睡觉怎么总不踏实，原来是要撞见不愿意见的人。
[charslot(slot = "m", focus="n")]
槐天裴侧过头，向身后扫了一眼。
动作很轻很快，但槐琥看得很清楚。
[charslot(slot = "m", name = "avg_npc_785_1#11$1")]
[name="槐天裴"]在和那位宗师比武之前，原本不想和别人动手。
[charslot(slot = "m", name = "avg_npc_785_1#3$1")]
[name="槐天裴"]唉......今天破戒也罢！
[charslot(slot = "m", name = "avg_npc_785_1#1$1")]
[name="槐天裴"]喂，我见你也有点功夫，但欺负晚辈算什么本事？
[CameraShake(duration=0.3,xstrength=35,ystrength=30,vibrato=30,rand

... (全文22608字符)
```

### level_act23side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[playMusic(key="$m_avg_yumennormal_loop", volume=0.6)]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="a",volume=0)]
[Delay(time=1)]
[Background(image="35_g6_yumengate",screenadapt="coverall")]
[SoundVolume(volume=0.5, channel="a", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_crowdrun",volume=1)]
[Delay(time=1)]
[PlaySound(key="$bodyfalldown2",volume=0.5)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="被挤到的百姓"]我的行李掉了，别挤别挤！
[name="巡防营守军"]时间还够，请大家有秩序地撤离，不要惊慌，避免踩踏。
[name="惊慌的孩子"]妈妈妈妈......
[name="惊慌的孩子"]呜呜，我怕。
[name="努力镇定的女性"]别怕，抓紧妈妈的手，别走丢了。
[name="惊慌的孩子"]我们去哪儿啊？
[name="努力镇定的女性"]咱们住的地方，每年都要刮上几次大风，这次也一样。
[name="努力镇定的女性"]不想被吹跑呀，就乖乖躲一躲。
[Dialog]
[StopSound(channel="a", fadetime=2)]
[Delay(time=1)]
[PlaySound(key="$d_avg_rampartclose",volume=0.6)]
[CameraShake(duration=7, xstrength=8, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
伴随着隆隆声响，庞大而方正的阴影自玉门城墙外升起，渐渐遮住了半边日头——
“玉门四卫”。四组被称作“屏风卫”的外挂移动防护墙体，由土木天师专门设计，军中冶造司承造。
数百年来，玉门作为炎国的屏障，戍守塞上；屏风卫作为玉门的屏障，抵御着来自大漠深处的沙尘、冬风与各类源石尘暴。
四卫不倾，三风不度。
[Dialog]
[Delay(time=1)]
[charslot(slot = "left", name = "avg_npc_795_1#1$1",duration = 0.5)]
[charslot(slot = "right", name = "avg_npc_796_1#1$1",duration = 0.5)]
[Delay(time=1)]
[charslot(slot = "right", name = "avg_npc_796_1#1$1",focus="r")]
[name="巡防营守军"]乖乖，好高......
[name="巡防营守军"]来到玉门三年，我还没看过屏风卫升起来呢。
[charslot(slot = "left", name = "avg_npc_795_1#1$1",focus="l")]
[name="千夫长"]少见多怪。
[name="千夫长"]玉门基础墙体本来就高，加上城头架设了全套的源石防御工事，一般规模的天灾，需要启动屏风卫的次数很少，但也不是没有。
[name="千夫长"]但这次为了避灾迁移半城的百姓，我入伍以来倒还没经历过......
[charslot(slot = "right", name = "avg_npc_796_1#1$1",focus="r")]
[name="巡防营守军"]那，这天灾，得是什么级别，屏风卫都挡不住吗？
[charslot]
屏风卫已经固定完毕，精钢板块彼此间榫合得严丝合缝，连风也透不进来。
排成长队的百姓在它投下的阴影里，向城墙的相反方向行进。或许是厚重坚实的屏风卫让大家安了心，短暂的混乱后，人群恢复了秩序。
长行塞外，胡杨早已习惯了风沙。
[charslot(slot = "left", name = "avg_npc_795_1#1$1",focus="l")]
[charslot(slot = "right", name = "avg_npc_796_1#1$1",focus="n")]
[name="千夫长"]怎么，你小子怕了？
[charslot(slot = "right", name = "avg_npc_796_1#1$1",focus="r")]
[name="巡防营守军"]......
[charslot(slot = "left", name = "avg_npc_795_1#1$1",focus="l")]
[name="千夫长"]别瞎想，坚守岗位。
[name="千夫长"]把眼睛放亮些，那帮山海众还混在城里。现在正是人流密集，最容易出事的时候。
[name="千夫长"]保护好百姓。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_033",duration = 0.5)]
[charslot(slot = "right", name = "avg_npc_140#2",duration = 0.5)]
[Delay(time=1)]
[charslot(slot = "left", name = "avg_npc_033",focus="l")]
[name="龙门暗桩"]老板，您怎么还不走啊？
[name="龙门暗桩"]广播都放了好几遍，玉门快要撞上天灾了，城东的住户要在今天中午前搬到城西的避难点去。
[charslot(slot = "right", name = "avg_npc_140#2",focus="r")]
[name="掌柜"]听到啦，不急，不急。那天灾云还没到眼前呢，我得收拾收拾东西......
[name="掌柜"]嘿，找到了。
[name="掌柜"]这一屋子桌椅板凳倒也罢了，这本菜谱可是命根子，不敢丢喽。
[charslot(slot = "left", name = "avg_npc_033",focus="l")]
[name="龙门暗桩"]哎，这次要是运气不好，这间客栈没保下来，不如您和我一起去龙门吧。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "right", name = "avg_npc_140#1",focus="r")]
[name="掌柜"]说什么呢！
[charslot(slot = "left", name = "avg_npc_033",focus="l")]
[name="龙门暗桩"]哎怪我多嘴，说些不吉利的话，呸呸呸！
[name="龙门暗桩"]只是来的这几天，蒙您照顾，我想着凭您的手艺，在龙门开家饭馆生意肯定也红火。
[charslot(slot = "right", name = "avg_npc_140#2",focus="r")]
[name="掌柜"]那可不成。
[name="掌柜"]我要是走了，这里的人就再吃不到我这一手独门秘制酱兽肉了。
[charslot(slot = "left", name = "avg_npc_033",focus="l")]
[name="龙门暗桩"]老板是玉门本地人？
[charslot(slot = "right", name = "avg_npc_140#2",focus="r")]
[name="掌柜"]那倒不是。
[name="掌柜"]老家在中原，本来是去龙门谋生计。有一次想往更北边的地方看看，就趁着城市对接的机会来了玉门。
[name="掌柜"]当时弄丢了钱包，就留在这家客栈打工，一转眼，自己当掌柜都这么多年了。
[name="掌柜"]房子算不上可惜......只要人还在，家就在。
[charslot(slot = "left", name = "avg_npc_033",focus="l")]
[name="龙门暗桩"]是这个理儿。
[name="龙门暗桩"]唉，我陪您快点收拾吧。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_g3_yumenobservationtower_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
无风。
即使隔得很远，深色的诡异气团依然遮蔽了小半个天空。
天灾云看起来没有移动，空气却越来越燥热。
仿佛只等一阵风起，就会在眨眼间吹落城头。
[dialog]
[charslot(slot="m",name="avg_2023_ling_1#8$1",duration=1.5)]
[delay(time=2)]
[name="令"]呼......
[name="令"]左将军也有心情来旁观我大哥的比武？
[charslot(slot="m",name="avg_npc_788_1#1$1")]
[name="左宣辽"]抗灾事宜已经安排妥当。宗师想赶在天灾之前看看那人是否值得托付，我又怎能不来。
[name="左宣辽"]只是用这种办法决定剑的归处，左某始终觉得荒唐。
[charslot(slot="m",name="avg_2023_ling_1#9$1")]
[name="令"]你与我大哥几十年的袍泽情谊，哪怕是作为朋友，也不愿意相信他的选择？
[charslot(slot="m",name="avg_npc_788_1#8$1")]
[name="左宣辽"]......朋友。
[charslot(slot="m",name="avg_2023_ling_1#9$1")]
[name="令"]唔。
[charslot(slot="m",name="avg_npc_788_1#2$1")]
[name="左宣辽"]我们同赴沙场，却谈不上生死与共。刀枪炮火伤不到你们，你们又怎能真正体会人的袍泽情谊？
[name="左宣辽"]你们终究置身事外。
[charslot(slot="m",name="avg_2023_ling_1#7$1")]
[name="令"]......
[name="令"]“置身事外”？
[charslot(slot="m",name="avg_2023_ling_1#1$1")]
[name="令"]我贪个“逍遥”，你这样说我倒也罢了，可对于大哥他，未免有些不公。
[charslot(slot="m",name="avg_npc_788_1#8$1")]
[name="左宣辽"]人兽有别，亘古不变。
[charslot(slot="m",name="avg_npc_788_1#1$1")]
[name="左宣辽"]令小姐应该清楚朝廷对你们的态度。
[name="左宣辽"]若能有人与你们相颉颃，则可以将你们视作助力。若无人能相制衡，那宁可不用你们。
[name="左宣辽"]我不如他，所以我不能毫无保留地相信他。
[charslot(slot="m",name="avg_2023_ling_1#7$1")]
[name="令"]没想到，左将军也会这样坦诚。
[charslot(slot="m",name="avg_2023_ling_1#1$1")]
[name="令"]可你未免太看轻自己了......
[charslot]
左宣辽无言望向城外大漠，城下人影依稀，像是苍茫画卷上飞溅出了两点残墨。
天地肃杀。
[charslot(slot="m",name="avg_2023_ling_1#1$1")]
[name="令"]那段日子，仿佛还在昨天一样。
[name="令"]在征战之余，我们也曾四处游猎，饮酒高歌。玉门依然是玉门，为什么偏偏是平祟侯，为那么多事愁白了头？
[name="令"]看着这两人，你可曾想起那段峥嵘岁月？
[name="令"]你说人兽有别，可你看看，偏偏此刻就有人在挑战这道沟壑屏障。这样的较量，难道不令人心潮澎湃吗？
[charslot(slot="m",name="avg_npc_788_1#8$1")]
[name="左宣辽"]......
[charslot(slot="m",name="avg_2023_ling_1#8$1")]
[name="令"]别皱着眉头了。
[name="令"]喝口酒？不如我们押个输赢。
[stopmusic(fadetime=2)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[cha

... (全文19762字符)
```

### level_act23side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[playMusic(intro="$taoyuan_intro",key="$taoyuan_loop", volume=0.6)]
[curtain(direction = 6,fillfrom = 0,fillto = 0.55,fadetime=0.1,block=false,grad=true)]
[curtain(direction = 2,fillfrom = 0,fillto = 0.01,fadetime=0.01,grad=true)]
[Delay(time=1)]
尚在那一片混沌鸿蒙之中，我见过两个顽童大打出手，只为争抢捡来的一颗果子。
两人年纪相仿，身材相仿。只是其中一个反应更快些，抡起的拳头也更沉些，就将对手打倒在地。
果子当然也就成了他的战利品。
胜者欢欣，败者垂泪。
我也见过那场围猎。
人类向不可企及的“祂们”宣战。渺小的个体战胜了连仰视都目不能及的神明，伏尸百万，流血漂橹。
胜者生存，败者消亡。
[dialog]
[delay(time=1)]
[charslot(slot = "r", name = "avg_2024_chyue_1#4$1",posfrom="0,0",posto="100,0",duration=0)]
[Background(image="35_g11_yumendesert",xScale=1.3, yScale=1.3)]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1.5)]
[Sticker(id="st1", multi = true, text="“武”到底是什么？", x=100,y=300, alignment="left", size=24, delay=0.04, width=500,block = true)]
[Sticker(id="st1", multi = true, text="\n力量？技巧？杀敌之术？",block = true)]
[Sticker(id="st1", multi = true, text="\n一个人力量再强，赢不过千军万马，敌不过高速战舰。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="可若暗杀偷袭都算技巧，杀人也可以无所不用其极。又何必将其当作一门学问？",x=100,y=270, alignment="left", size=24, delay=0.04, width=500,block = true)]
[Sticker(id="st1", multi = true, text="\n关隘难过，为了寻求一个答案，我舍弃了力量，将“自己”封印入剑，塑造出一副人的身躯。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="有多久了？" ,x=100,y=270, alignment="left", size=24, delay=0.04, width=500,)]
[Sticker(id="st1", multi = true, text="\n有多久没有遇到过这样一个对手，可以让自己不为求索，尽力挥拳？",block = true)]
[Sticker(id="st1")]
[charslot(slot = "r", name = "avg_2024_chyue_1#8$1",duration=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_clothmovementsp")]
[charslot(slot = "r",posfrom="100,0",posto="-100,0",duration=0.3,afrom=1,ato=0,isblock=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[curtain]
[Background(image="bg_black",screenadapt="coverall")]
[delay(time=0.5)]
[Blocker(a=0.8, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Effect(name="$e_fist_01",x=-100,layer = 2)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[PlaySound(key="$d_avg_punchsp5",volume=0.8)]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[Effect(name="$e_fist_01",x=0,y=50,rox=-180,roy=50,roz=-40,layer = 2)]
[PlaySound(key="$punch_n1")]
[delay(time=0.2)]
[Blocker(a=0.3, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Effect(name="$e_fist_hit_01",x=70,y=100,layer = 1)]
[Effect(name="$e_fist_01",x=240,y=-50,rox=-240,roy=110,roz=-230,layer = 2)]
[PlaySound(key="$d_avg_punch02",volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[delay(time=1)]
[Effect(name="$e_fist_01",x=240,y=-50,rox=-250,roy=150,roz=-240,layer = 2)]
[CameraShake(duration=0.3, xstrength=15, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_punchsp2",volume=0.7)]
[delay(time=0.45)]
[PlaySound(key="$d_avg_punchsp5",volume=0.7)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Effect(name="$e_fist_01",x=140,y=0,rox=-240,roy=110,roz=-230,layer = 2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Effect(name="$e_fist_hit_01",y=150,layer = 1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Effect(name="$e_fist_01",x=-40,y=-50,rox=-180,roy=60,roz=-250,layer = 3)]
[PlaySound(key="$d_avg_punchsp4")]
[delay(time=2)]
[name="录武官"]第八合。
[name="录武官"]面对抢攻，宗师只是撤了一步。槐天裴的拳在挨到宗师手掌边缘时便已势尽。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[curtain(direction = 2,fillfrom = 0,fillto = 0.55,fadetime=0.1,block=false,grad=true)]
[curtain(direction = 6,fillfrom = 0,fillto = 0.01,fadetime=0.01,grad=true)]
[Background(image="35_g11_yumendesert",xScale=1.3, yScale=1.3)]
[delay(time=0.45)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[charslot(slot = "l", posfrom="300,0",posto="-100,0",name = "avg_npc_785_1#1$1",duration=0.6)]
[PlaySound(key="$d_avg_clothmovementsp")]
[delay(time=1.5)]
[name="槐天裴"]（撑拔骨骼的声音）
[charslot(slot = "l", name = "avg_npc_785_1#3$1")]
[name="槐天裴"]呼......
[Dialog]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=1, block=false)]
[delay(time=1.5)]
[Sticker(id="st1", multi = true, text="习武四十余年，我从未见过高山，也未尝一败。", x=650,y=300, alignment="left", size=24, delay=0.04, width=500,block = true)]
[Sticker(id="st1", multi = true, text="\n拜的第一位师父教了我半年，摆摆手说已经没有东西可教，让我另找名师。",block = true)]
[Sticker(id="st1", multi = true, text="\n在那之后，又陆续拜了几位师父，每一位都只教了一年半载就将我逐出师门。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="世上武功门派数以百计，可人无非双手双脚，哪来那么多花招套路。",x=650,y=300, alignment="left", size=24, delay=0.04, width=500,block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="我要练我自己的武功。",x=650,y=300, alignment="left", size=24, delay=0.04, width=500,block = true)]
[Sticker(id="st1", multi = true, text="\n让拳头更重，脚步更快，眼神更准。" ,block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="可是眼前的这个人......",x=650,y=300, alignment="left", size=24, delay=0.04, width=500,block = true)]
[Sticker(id="st1")]
[charslot(slot = "l", name = "avg_npc_785_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_785_1#1$1")]
[PlaySound(key="$d_avg_clothmovementsp")]
[charslot(slot = "l",posfrom = "0,0", posto = "300,0",duration = 0.3)]
[charslot(duration=0.3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[curtain]
[Background(image="35_g11_yumendesert",screenadapt="coverall")]
[name="录武官"]第九合......
[name="录武官"]槐天裴重拳直取宗师身侧，封住其身法退路。
[dialog]
[charslot]
[delay(time=1)]
[PlaySound(key="$d_avg_clothmovementsp",volume=0.8)]
[delay(time=0.3)]
[CameraShake(duration=0.5, xstrength=20, ystrength=15, vibrato=30, randomness=90, fa

... (全文39356字符)
```

### level_act23side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[playMusic(intro="$midautumn",key="$midautumn", volume=0.6)]
[Delay(time=3)]
[Background(image="35_g7_zuosroom",screenadapt="coverall")]
[PlaySound(key="$d_avg_sandftsingle")]
咯吱。
街上积了厚厚的一层砾土。
城南大多数区域并未受到天灾波及，但风暴最剧烈的时候，狂沙吹雨，乱洒玉门，全城没有一处能看得见太阳。
[dialog]
[Background(image="35_g5_swordcastingworkshop",screenadapt="coverall")]
咯吱。
[dialog]
[Delay(time=1)]
[PlaySound(key="$d_avg_open_door")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
门锁坏了。
横倒的锻造炉，七零八落的兵器架，碎瓦残砖，院子里满地狼藉。
偏偏主人已经不会再回来打理。
[dialog]
[PlaySound(key="$d_avg_breezetree")]
[Delay(time=2)]
这棵树居然还在......
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot = "left", name = "avg_npc_297_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_4078_bdhkgt_1#1$3",duration = 1)]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_npc_297_1#1$1",focus="l")]
[name="左乐"]宗师。
[name="左乐"]左乐冒昧约您来铸剑坊。
[name="左乐"]佩剑已经追回。但此人非要自己把剑送回来。
[charslot(slot = "right", name = "avg_4078_bdhkgt_1#1$3",focus="r")]
[name="截云"]我有些话，要在这里和你说。
[dialog]
[charslot]
[charslot(slot="m",name="avg_2024_chyue_1#1$1",duration=1)]
[delay(time=1.5)]
[name="重岳"]嗯，无妨。
[charslot(slot="m",name="avg_2024_chyue_1#9$1")]
[dialog]
[Delay(time=2)]
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]说起来，我已经有十几年，没来过这里。
[name="重岳"]明明就在一座城里，竟然算得上“故地重游”。
[charslot(slot="m",name="avg_npc_297_1#7$1")]
[name="左乐"]孟前辈的事情......
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]不必多说。
[name="重岳"]将全城置于险境，天大的错事，他要做，也要偿，想必一开始就打算好了。
[charslot(slot="m",name="avg_npc_297_1#7$1")]
[name="左乐"]......
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]但前天的事，确实是左乐行事鲁莽，让玉门的江湖义士寒了心。
[name="左乐"]等到这一劫平定，我会去父亲那里领受责罚。
[name="左乐"]铸剑坊的全部损失，后续一应复原、修葺事宜，也都由我来承担。
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]平祟侯铁面无私，相信会给他们一个交代。
[name="重岳"]只是......
[name="重岳"]虽说事发突然，误会难免。但有没有乱了方寸，进而失了分寸，你自己要有评断。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]......
[name="左乐"]势在必行，左乐问心无愧。
[charslot(slot="m",name="avg_2024_chyue_1#3$1")]
[name="重岳"]——嗯。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]想必宗师应该清楚，于大炎而言，山海众，是比巨兽本身更应该警惕的存在。
[name="左乐"]巨兽虽有骇人威能，但千年前我们尚且能够赢得那场围猎，以今时今日大炎的国力，更加无惧祂们。
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]世殊时异，确实如此。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]真正可怖的，是生长在人们心间的，自混沌之初起便投下的阴影。
[name="左乐"]天地、星月、风雨、时令......顺逆无常，不知其源，超越我们所拥有的智识的边界。
[name="左乐"]对那时的人类来说，巨兽是同样的存在。
[name="左乐"]无知催生出恐惧，恐惧扭曲成信仰。在那些疯狂的人类眼中......我们才是这片土地上的异类，和“叛徒”。
[charslot(slot="m",name="avg_2024_chyue_1#4$1")]
[name="重岳"]信仰也不过是某种更深的执念罢了。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]巨兽从大炎疆土匿去身影后，山海众从未停止他们的活动。
[name="左乐"]更麻烦的是，近百年来，流寇、水匪、巨盗......亡命之徒，结党营私之辈，山海众尽数吸纳这些奸恶势力，“巨兽”成了遮掩他们的阴影。
[name="左乐"]根据司岁台的记录，山海众以“巨兽”之名所带来的祸乱，不计其数。
[name="左乐"]其数量之多，连枝带蔓，牵扯甚广，难以尽除。其行为之恶劣，更是令人胆寒。
[name="左乐"]最近他们开始尝试接触诸位代理人，所幸司岁台应对及时，他们并未成功。
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]我的那些弟弟妹妹们，大概也都不愿意和这样的“信徒”打交道。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]但，如今岁的本体即将苏醒，玉门归国，山海众潜入作乱，诸事错杂交织，很难用巧合来解释。
[charslot(slot="m",name="avg_2024_chyue_1#6$1")]
[name="重岳"]你是想说......
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]那个罪人以天下为棋枰，山海众未必不是一枚棋子。
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]如果司岁台已经得出了这样的结论，这是一项很严重的指控。
[charslot(slot="m",name="avg_npc_297_1#9$1")]
[name="左乐"]......
[name="左乐"]又或者，山海众已经与岁建立了某种联系。
[charslot(slot="m",name="avg_2024_chyue_1#8$1")]
[name="重岳"]......
[name="重岳"]也就是说，在司岁台看来，这或许是大炎面临的最为严重的一次巨兽问题。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]是。
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]追剑、缉凶、剿灭山海众成员......你是司岁台最年轻的秉烛人，又是玉门平祟侯之子，在这件事中，无疑要挑起最重的担子。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]是。
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]身在乱局，生杀决断，当用雷霆手腕，当断则断。
[name="重岳"]担得起行差踏错的过失，担不起误一漏万的后果。
[name="重岳"]宁可错拿，不可放过。
[name="重岳"]你想必，是这么想的。
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]......是。
[charslot(slot="m",name="avg_2024_chyue_1#9$1")]
[name="重岳"]倒是有几分左宣辽当年的气魄。只是......
[name="重岳"]你似乎忘了，左宣辽在责令你三日内完成三件事时，最后的那句嘱咐是什么。
[charslot(slot="m",name="avg_npc_297_1#9$1")]
[name="左乐"]......
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[charslot(slot="m",name="avg_npc_788_1#7$1")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="35_g7_zuosroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="左宣辽"]不得走漏消息，不得惊扰百姓安生。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[Background(image="35_g5_swordcastingworkshop",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="重岳"]朝廷专设司岁台，倾全力应对巨兽事宜，最终目的何在？
[name="重岳"]玉门远道归国，未来或将赌上一城之存亡，又是为了什么？
[charslot(slot="m",name="avg_npc_297_1#7$1")]
[name="左乐"]......
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]不正是此刻城中的那些百姓，不正是，被你带回军营的那些人。
[charslot(slot="m",name="avg_npc_297_1#7$1")]
[name="左乐"]......为苍生计。
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]莫在行事时，忘了最初的情和理。
[name="重岳"]这件事你或许没有做错，但身在局中，手握决断权柄，亦是手握杀伐重器。一念之间，行差踏错，便悔之莫及。
[charslot(slot="m",name="avg_2024_chyue_1#8$1")]
[name="重岳"]这些话，本不该由我来说。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_297_1#4$1")]
[name="左乐"]......
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[name="左乐"]左乐多谢宗师指点。
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]天灾尚未完全结束，你去帮忙吧。
[Dialog]
[charslot(slot="m",name="avg_npc_297_1#6$1")]
[delay(time=0.5)]
[dialog]
[playsound(key="$rungeneral")]
[stopmusic(fadetime=3)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35

... (全文22369字符)
```

### level_act23side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[playMusic(intro="$m_bat_act23side_02_intro",key="$m_bat_act23side_02_loop", volume=0.6)]
[Delay(time=1)]
[Background(image="35_g12_huanjing",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_2024_chyue_1#1$1",duration=1)]
[Delay(time=1)]
[name="重岳"]......
[charslot(slot="m",name="avg_npc_786_1#6$2")]
[name="睚"]......
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="35_g12_huanjing",xScale=1.3, yScale=1.3)]
那是第二次，在漫长的混沌中跋涉。
在跋涉的尽头苏醒——
懊悔。屈辱。不甘。浑噩。
......
更多的是，困惑。
[dialog]
[PlaySound(key="$d_avg_sphere")]
[Background(image="35_g12_huanjing",screenadapt="coverall",fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="睚"]既然你要留我，那就替祂，回答我的问题！
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]......
[Dialog]
[charslot(slot="m",name="avg_npc_786_1#5$2")]
[PlaySound(key="$d_avg_monsteroar",volume=0.5)]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=35, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_786_1#6$2")]
[name="睚"]为了见你，我一路走来。
[name="睚"]你可知道，目之所见，那些愚妄的蝼蚁，挖开岩脉，凿穿河床，山岳湖泽，清浊倒易，他们将那些狰狞的疮疤，命名为城市......
[name="睚"]这片早已病变的土地，还是我们曾栖居嬉游的宇？
[name="睚"]你可知道，这座名为玉门的丑陋城市，砖墙上还留着当初祂们临死前烙下的爪痕。
[name="睚"]千年以来，那群蝼蚁至今不曾修补那一块地方，视之为荣耀，视之为文明的巍峨里程。
[charslot(slot="m",name="avg_npc_786_1#5$2")]
[name="睚"]而你的碎片，如今却在守护这样一座城？
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]我是我，祂是祂。
[PlaySound(key="$d_avg_sandstone")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=35, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_786_1#5$2")]
[name="睚"]（天地的隐怒）
[charslot(slot = "m", focus = "n")]
船仍在行进。
两岸的草木矮去几分，雪压得更低了。
[charslot(slot="m",name="avg_npc_786_1#6$2")]
[name="睚"]你可还记得，我们的意识如何跋涉于无寐的混沌，成为此间最初的生灵？
[name="睚"]你可还记得，我们如何注视着鸿蒙升落，时得其序，物分其列，天地慢慢有了天地的样子？
[name="睚"]你可还记得，那破开云霭的眼睛？我们在苍穹间对视，碰撞，川江淤赤，群山夷为平地，伏尸耸入云霄，溃脓腐烂后化作新的峰岭......
[charslot(slot="m",name="avg_npc_786_1#4$2")]
[PlaySound(key="$d_avg_monsteroar",volume=0.5)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=35, randomness=90, fadeout=true, block=false)]
[name="睚"]那是何等壮阔的，真正的，战争？！
[PlaySound(key="$d_avg_sandstone")]
[charslot(slot="m",name="avg_npc_786_1#5$2")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=35, randomness=90, fadeout=true, block=false)]
[name="睚"]（天地的隐怒）
[charslot(slot = "m", focus = "n")]
船仍在行进，江面随着船头延伸，永无止境。
积雪更深，每一句发问，回声都如同雪崩。
上下皆白，天穹低得触手可及。
[charslot(slot="m",name="avg_npc_786_1#5$2")]
[name="睚"]经历过那样的时代，为何还会在意自己鳞爪间的蝼蚁，和蝼蚁扑腾起的尘埃？
[name="睚"]为了愚弄人类，你吹云作雨，降下可笑的“祥瑞”，助所谓的真龙赢下征伐，本就无聊至极......
[name="睚"]又为何千年之后，再次回应他们？惊扰、挑唆、围逐、驱杀自己的，同类？！
[name="睚"]相比他们渺小却勇敢的先族，这帮羸弱的、不堪的、肮脏的蝼蚁，你为何想要成为他们的主宰——？！
[name="睚"]成为他们可笑的“神”？！
[PlaySound(key="$d_avg_sandstone")]
[name="睚"]（天地的隐怒）
[charslot(slot="m",name="avg_npc_786_1#4$2")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=35, randomness=90, fadeout=true, block=false)]
[name="睚"]穷极寰宇，历数太古以来无垠的时间，我们这样的存在，可曾有过你这般耻辱？！
[charslot(duration=0.3)]
回答我，我的......同类！
[dialog]
[CameraShake(duration=2.5, xstrength=30, ystrength=30, vibrato=35, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.5, block=true)]
[Dialog]
[PlaySound(key="$d_avg_monsteroar",volume=0.7)]
[PlaySound(key="$d_avg_rockfall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3.5, block=true)]
[charslot(slot="m",name="avg_2024_chyue_1#8$1",duration=0.5)]
[delay(time=1)]
[name="重岳"]你很愤怒。
[name="重岳"]在沉睡的数千年里，祂也无时无刻不像现在的你一样......
[name="重岳"]吞咽屈辱，咀嚼背叛，追问答案。
[name="重岳"]不然也不会有我们这些碎片的诞生。
[charslot(slot="m",name="avg_npc_786_1#5$2")]
[name="睚"]......
[charslot(slot="m",name="avg_2024_chyue_1#4$1")]
[name="重岳"]但我们已然不是祂。
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="重岳"]所以你的问题，我给不了答案。
[name="重岳"]我理解不了你的愤怒，正如你理解不了我的愤怒。
[charslot(slot="m",name="avg_npc_786_1#5$2")]
[name="睚"]愤怒？
[charslot(slot="m",name="avg_npc_786_1#4$2")]
[name="睚"]你依然要为人类讨要说法？在这里？
[name="睚"]拔出那把剑，或许还有可能。
[Dialog]
[PlaySound(key="$d_avg_wind")]
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[delay(time=1.5)]
[name="重岳"]我在想，你是有多么珍惜这个空间。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Background(image="35_g3_yumenobservationtower_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background(image="35_g5_swordcastingworkshop",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background(image="35_g2_yumenstreet_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background(image="35_g12_huanjing",screenadapt="coverall")]
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[name="重岳"]春生夏荣秋伤冬藏，裁错春秋，剪宇怀腹。
[name="重岳"]我甚至能想象到，你在千年前逃离炎国时，是怎样将这几方小小的天地剪裁下来仓皇带走。
[name="重岳"]而后又是怎样隐匿在这片大地上某个僻远的角落，一遍又一遍地翻检查看，就着永远不会流逝的残景舔舐伤口。
[charslot(slot="m",name="avg_2024_chyue_1#8$1")]
[name="重岳"]巨兽，也变成了如此伤怀的一种生命？！
[name="重岳"]这和你口中那般羸弱的、不堪的、肮脏的人类，又有什么区别？！
[dialog]
[charslot(slot = "m", focus = "n")]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_thunders_amb",delay=0.2,volume=0.7)]
[delay(time=2)]
[charslot(slot="m",name="avg_2024_chyue_1#8$1")]
[name="重岳"]八千年为春，八千年为秋，雪永远不会停，这方天地永远是这天地。
[name="重岳"]这就是你们丈量时间的方式......
[charslot(slot="m",name="avg_2024_chyue_1#3$1")]
[name="重岳"]真是可笑。
[dialog]
[charslot(slot = "m", focus = "n")]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, bloc

... (全文17014字符)
```

### level_act23side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act23side/WB01.mp4")]
```

### level_act23side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]	
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_avg_chess")]
[Subtitle(text="二哥，你无事唤我陪你下棋也就罢了，还要用棋子摆一个“闲”字来嘲弄我，未免太欺负人了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可见平日我教过你的那些棋理，你完全不曾用心揣摩。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[PlaySound(key="$d_avg_chess")]
[Subtitle(text="二哥这话太过分，说得好像我仔细学过，就能在这方纹枰上和你有一战之力了？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="棋盘上这个字，也确实没你写得好看。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[PlaySound(key="$d_avg_chess")]
[Subtitle(text="二哥既然不是真心想下棋，何不找点别的消遣？要么去游山玩水，要么去学样乐器，实在不行，换我来教你书法？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="棋局搏杀无趣，但是手谈间能读出对手些许心思，还算有点意思。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="哦？那二哥从这一局棋中，读出我什么心思了？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我看出......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[stopmusic(fadetime=1)]
[delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[PlaySound(key="$d_avg_crwddiscuss_inside", channel="slide", loop=true, volume=0.4)]
[Background(screenadapt="showall", image="25_g04_yaninn",x=100, y=0, xScale=1.3, yScale=1.3)]
[backgroundTween(xFrom=100, yFrom=0, xTo=-100, yTo=0, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1.3, yScaleTo=1.3, duration=20, block=false)]
[curtain(direction = 0,fillfrom = 0,fillto = 0.2,fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0,fillto = 0.2,fadetime=0.1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[delay(time=1.5)]
[dialog]
[Background(image="25_g04_yaninn",screenadapt="showall",fadetime=2,x=-80, y=0, xScale=1.3, yScale=1.3)]
[stopsound(channel="slide", fadetime=3)]
[curtain(direction = 0,fillfrom = 0.2,fillto = 0,fadetime=3)]
[curtain(direction = 4,fillfrom = 0.2,fillto = 0,fadetime=3)]
[delay(time=3)]
[charslot(slot="m",name="avg_npc_033",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_033")]
[name="龙门游客"]老板，你这电视剧咋播的？怎么直接从十七集跳到二十集了？
[charslot(slot="m",name="avg_npc_140#2")]
[name="掌柜"]碟片被沙子刮花了，有几集就是播不了，将就看吧。
[charslot(slot="m",name="avg_npc_033")]
[name="龙门游客"]正看到关键地方呢，戚清秋和沈飞白上一集还打得你死我活，这会儿咋个又并肩作战了？
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="饮酒的老客"]中间这三集啊，讲的是戚清秋确认了沈飞白就是自己的杀师仇人，要去找他拼命。
[name="饮酒的老客"]但是到了玉门才发现，沈飞白已经投身军伍，还担任了不低的军职。
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="饮酒的老客"]当下正是强敌犯境，戚清秋夜不能寐，想通了国仇大过家恨的道理，便也投入宗师麾下一同抗敌。
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="饮酒的老客"]剧情很简单，但十九集那场悬崖论剑，可真是经典啊！
[charslot(slot="m",name="avg_npc_033")]
[name="龙门游客"]我天，您是看了多少遍，记得这么清楚？
[charslot(slot="m",name="avg_npc_140#2")]
[name="掌柜"]在这玉门城里，你路边随便逮一个小孩，都能把《玉门风云》的剧情倒背如流。
[charslot(slot="m",name="avg_npc_140#2")]
[name="掌柜"]不过这位客人刚刚漏说了一段。戚清秋在军中见到沈飞白，并没有马上放下仇恨。
[charslot(slot="m",name="avg_npc_140#2")]
[name="掌柜"]当时是那位宗师站了出来，说先由自己代沈飞白接下戚清秋报仇的一剑。这才有了那场悬崖论剑。
[charslot(slot="m",name="avg_npc_140#2")]
[name="掌柜"]当时乌云密布，飞沙走石，好像天地万物都要为这场比武作见证。说时迟那时快，两人拔出剑来——
[charslot(slot="m",name="avg_npc_792_1$1")]
[name="萨尔贡打扮的游客"]（不太熟练的炎国语）胡说，胡说！简直是胡说八道！
[charslot(slot="m",name="avg_npc_792_1$1")]
[name="萨尔贡打扮的游客"]这部电视剧，打戏好看，但细节一点都不严谨。
[charslot(slot="m",name="avg_npc_140#2")]
[name="掌柜"]何昔安，你又来了。炎国话都没学利索，你看得懂拍的是什么吗？
[charslot(slot="m",name="avg_npc_792_1$1")]
[name="萨尔贡打扮的游客"]当然，知道！《玉门风云》讲的是五十年前发生的真事。有许多，江湖侠客消除恩怨，在那位宗师的带领下抗击外敌。
[charslot(slot="m",name="avg_npc_792_1$1")]
[name="萨尔贡打扮的游客"]我还知道，里面好多场面就是在这只客栈拍的！
[charslot(slot="m",name="avg_npc_140#2")]
[name="掌柜"]“间”，“这间”。
[charslot(slot="m",name="avg_npc_792_1$1")]
[name="萨尔贡打扮的游客"]......
[charslot(slot="m",name="avg_npc_033")]
[name="龙门游客"]这外国兄弟，对大炎历史了解得还挺清楚。
[charslot(slot="m",name="avg_npc_792_1$1")]
[name="萨尔贡打扮的游客"]我当然清楚。那位宗师教我武功的时候亲自告诉我的，在萨尔贡。
[charslot(slot="m",name="avg_npc_792_1$1")]
[name="萨尔贡打扮的游客"]宗师是有一把剑。但那把剑很特殊，是绝对不能出鞘的！
[charslot(slot="m",name="avg_npc_140#2")]
[name="掌柜"]又是这套。你要真是宗师的亲传弟子，怎么昨天在擂台上三两下就输给了那个菲林小姑娘？
[charslot(slot="m",name="avg_npc_792_1$1")]
[name="萨尔贡打扮的游客"]菲林小姑娘怎么了，她武艺十分的厉害，你凭什么瞧不起人家？
[charslot(slot="m",name="avg_npc_033")]
[name="龙门游客"]萨尔贡老兄，炎国话里这种说法，不是瞧不起小姑娘，是瞧不起......
[dialog]
[charslot]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="起哄的众人"]哈哈哈哈哈......
[charslot(slot="m",name="avg_npc_033")]
[name="龙门游客"]话说回来，如果电视剧是真实事件改编，玉门还真有这样一段江湖武人与军队联手抗敌的历史吗？
[charslot(slot="m",name="avg_npc_033")]
[name="龙门游客"]“侠之大者，为国为民”，既身在江湖逍遥自在，又能保家卫国一展抱负，不愧是玉门，想一想真是酷。
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="饮酒的老客"]电视里演的终归是故事，多少美化过了。历史到底怎么样，不去问经历过的人，又怎么能说得清楚。
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="饮酒的老客"]再说了，现在早就不是在战场上撸袖子拼刀枪的时代了。真想报效国家啊，还是学好源石技艺，去当个天师靠谱。
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="饮酒的老客"]玉门这样的边防要塞，要没有这么多普通人生活在这里维持城市运作，光靠其他城市补给，得耗费多少倍的资源？
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="饮酒的老客"]当年兴建城市，愿意拖家带口搬迁到这偏远苦寒地方的人，还有至今愿意留在这里的人，哪一个担不起一句“为国为民”？
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="饮酒的老客"]说起来，电视剧里唯一可以确定是真人真事的那位宗师，现在也要走咯。
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="none")]
[name="？？？"]让一让。
[dialog]
[delay(time=1)]
[character]
[musicvolume(volume=0.2, fadetime=1)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_785_1#1$1",duration=1.5)]
[delay(time=2)]
[name="魁梧的男人"]送药。
[charslot]
[musicvolume(volume=0.4, fadetime=1)]
[charslot(slot="r",name="avg_npc_785_1#1$1",focus="l")]
[charslot(slot="l",name="avg_npc_140#2",focus="l")]
[

... (全文34750字符)
```

### level_act23side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[playMusic(intro="$storyendjp_intro",key="$storyendjp_loop", volume=0.6)]
[Delay(time=3)]
[Background(image="35_g11_yumendesert",screenadapt="coverall")]
[Subtitle(text="我生在江边。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="爹跟我说，江水连通了整片大地，有一条够坚固的船，就能去任何地方。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="爹最讨厌下雪，大雪封门，没有“生意”可做，全家都得饿肚子。我的名字就是这样来的。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我不晓得“生意”是什么，只是每个月底都见爹提着刀和物资回来，还有专门带给我的礼物。这时娘便一声不吭地分拣东西，帮爹浆洗沾血的袍子。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="直到有一天，一群穿着铠甲的人，攻破了寨子。爹一辈子都活在江上，最终也葬身江底。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我只记住了为首的那个人。明明是大获全胜，但他看起来并没有多少欣喜，只是望着被血染红的江水出神。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="当时我只剩下一个念头。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Delay(time=1.5)]
[Subtitle(text="我要报仇。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=3, block=true)]
[Subtitle(text="我打听到了那人的所在，也离开了家。从炎国的最东头，一直追到最西边。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我才知道，原来大地上不止有江，还有数不尽的山川和原野。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="大地上的人们，有千万种活法，也有千万般辛苦。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="水寨太小了，如果爹能出来看看，或许不会选择半辈子都做那样的营生。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="爹说的不对。一艘船，能去的地方不多。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我终于来到了玉门。那人就站在城头上，脸上是和那时一模一样的神情，我多少能看懂了些。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我应该报仇。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[charslot(slot = "left", name = "avg_npc_787_1#1$1")]
[charslot(slot = "right", name = "avg_2024_chyue_1#1$1")]
[Background(image="35_g3_yumenobservationtower_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "right", name = "avg_2024_chyue_1#1$1",focus="r")]
[name="重岳"]......
[charslot(slot = "left", name = "avg_npc_787_1#1$1",focus="l")]
[name="仇白"]事情就是这样。
[name="仇白"]剑在槐武痴手里，以他的武功，左乐估计拿他没办法。
[charslot(slot = "right", name = "avg_2024_chyue_1#6$1",focus="r")]
[name="重岳"]为这一个约定，他竟然在城里等了三年......倒是个有趣的人。
[charslot(slot = "right", name = "avg_2024_chyue_1#1$1",focus="r")]
[name="重岳"]太合的伤势怎样了？
[charslot(slot = "left", name = "avg_npc_787_1#5$1",focus="l")]
[name="仇白"]还没醒。
[name="仇白"]重伤太合先生的和前天刺杀魏彦吾的是同一人。她趁乱逃走，我不是对手，没能追上。
[charslot(slot = "left", name = "avg_npc_787_1#10$1",focus="l")]
[name="仇白"]现在左乐封了铸剑坊，不少武人都被......控制了起来。
[charslot(slot = "left", name = "avg_npc_787_1#11$1",focus="l")]
[name="仇白"]天灾当前，现在守军和江湖人士又彻底撕破脸，玉门的局势只怕会更乱。
[charslot(slot = "right", name = "avg_2024_chyue_1#4$1",focus="r")]
[name="重岳"]也不能怪他冲动。
[charslot(slot = "left", name = "avg_npc_787_1#5$1",focus="l")]
[name="仇白"]......这件事，你自己不出手，解决不了。
[charslot(slot = "right", name = "avg_2024_chyue_1#3$1",focus="r")]
[name="重岳"]左将军让我留守军营，我明目张胆跟他作对算怎么回事。
[charslot(slot = "left", name = "avg_npc_787_1#11$1",focus="l")]
[name="仇白"]你知道我说的不只是这几天的事。
[name="仇白"]你马上就要离开，临行前总要给城里的那些仰慕着你的人一个交代。
[name="仇白"]还是你觉得，解释不清的事，回避就够了？
[charslot(slot = "right", name = "avg_2024_chyue_1#1$1",focus="r")]
[name="重岳"]......
[name="重岳"]大家都当你是我的学生，有时候连我自己都忘了你的来历，也将你当作录武官、左乐一辈的孩子。
[charslot(slot = "left", name = "avg_npc_787_1#10$1",focus="l")]
[name="仇白"]可我从没叫过你一声“老师”。
[charslot(slot = "right", name = "avg_2024_chyue_1#1$1",focus="r")]
[name="重岳"]我也的确不能算是。
[name="重岳"]你的悟性很高，剑术多半是靠自己琢磨，我能教你的，本来就有限。
[charslot(slot = "left", name = "avg_npc_787_1#1$1",focus="l")]
[name="仇白"]毕竟是你对所有人隐瞒了我的身份，让我能留在玉门。
[charslot(slot = "right", name = "avg_2024_chyue_1#4$1",focus="r")]
[name="重岳"]总不能看着一个孩子再流落荒野......
[charslot(slot = "left", name = "avg_npc_787_1#1$1",focus="l")]
[name="仇白"]你从来不担心我会动手杀你？还是认定我永远都赢不了你？
[charslot(slot = "right", name = "avg_2024_chyue_1#1$1",focus="r")]
[name="重岳"]要想报仇，又何必要在武功上胜过我。
[name="重岳"]就算往饭里下毒，或者是在这城墙上推我一把，我也该死了千百遍了。
[name="重岳"]我只怕你杀了我，也没法放下执念。
[charslot(slot = "left", name = "avg_npc_787_1#2$1",focus="l")]
[name="仇白"]......如果不是跟在你身边五年，听到这种话，我一定会大骂你是世上最道貌岸然的伪君子。
[charslot(slot = "right", name = "avg_2024_chyue_1#10$1",focus="r")]
[name="重岳"]五年，竟然有这么久了。
[charslot(slot = "left", name = "avg_npc_787_1#4$1",focus="l")]  
[name="仇白"]从你的视角看，未必是多长的一段时间吧。
[charslot(slot = "right", name = "avg_2024_chyue_1#6$1",focus="r")]
[name="重岳"]这又怎么说？
[charslot(slot = "left", name = "avg_npc_787_1#10$1",focus="l")]
[name="仇白"]十几年过去，一个人的相貌没有半点改变，脸上也总是挂着这副世事看尽的无奈表情，我再迟钝，也该明白你不是普通人。
[charslot(slot = "left", name = "avg_npc_787_1#1$1",focus="l")]
[name="仇白"]知道这片大地上有一些寿命极长的种族，以前只是当故事听，没想到就在自己的身边。
[charslot(slot = "right", name = "avg_2024_chyue_1#9$1",focus="r")]
[name="重岳"]你早就想到了。
[charslot(slot = "left", name = "avg_npc_787_1#1$1",focus="l")]
[name="仇白"]我只是不太在乎。
[name="仇白"]我只为报仇，你能活多长和我没有关系。
[name="仇白"]更何况，总想着你不是普通人，不就等于在为自己找借口。
[name="仇白"]就像你说的，徒步登高，只需要一步一步往上走就好了。其他的事情，想多了只是干扰心志。
[charslot(slot = "right", name = "avg_2024_chyue_1#1$1",focus="r")]
[name="重岳"]但一心惦记着恩怨、输赢，就算真的得偿所愿，未必就能放下。
[name="重岳"]剑上承载的杂念太多，就会变得迟缓。
[charslot(slot = "left", name = "avg_npc_787_1#10$1",focus="l")]
[name="仇白"]普通人，总得靠那一点执念活着......你又何尝不清楚。
[charslot(slot = "right", name = "avg_2024_chyue_1#7$1",focus="r")]
[name="重岳"]我记得刚认识的时候，你说话还没这么“咄咄逼人”......
[charslot(slot = "left", name = "avg_npc_787_1#1$1",focus="l")]
[name="仇白"]这五年，我毕竟受了你不少教诲。
[charslot(slot = "right", name = "avg_2024_chy

... (全文22606字符)
```

### level_act23side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[Delay(time=1)]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_4080_lin_1#1$1",duration = 1)]
[charslot(slot="r",name="avg_npc_790_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot="r",name="avg_npc_790_1#1$1",focus="r")]
[name="陈"]林先生，怎么样了？
[charslot(slot="l",name="avg_4080_lin_1#7$1",focus="l")]
[name="林雨霞"]医生说没有大碍。
[name="林雨霞"]只是之前受了伤，又那样拼命使用源石技艺，过于劳累了。
[name="林雨霞"]爸他毕竟上了年纪。
[charslot(slot="r",name="avg_npc_790_1#7$1",focus="r")]
[name="陈"]有时都忘了，林先生，已经为龙门操劳了这么久......
[charslot(slot="l",name="avg_4080_lin_1#9$1",focus="l")]
[name="林雨霞"]爸和魏长官不一样。魏长官是龙门的象征，他必须时时刻刻出现在大众的视野里。
[charslot(slot="l",name="avg_4080_lin_1#7$1",focus="l")]
[name="林雨霞"]可要是人人都时常记得下城区有一位鼠王，对龙门而言并非一件好事。
[charslot(slot="r",name="avg_npc_790_1#1$1",focus="r")]
[name="陈"]我听说了，这次的麻烦事，是魏彦吾卷你进来的。
[charslot(slot="l",name="avg_4080_lin_1#1$1",focus="l")]
[name="林雨霞"]既然我接下了，那就是我自己的事。
[charslot(slot="l",name="avg_4080_lin_1#10$1",focus="l")]
[name="林雨霞"]而且多亏了某人，我最终也没出事。
[charslot(slot="r",name="avg_npc_790_1#2$1",focus="r")]
[name="陈"]啧。
[charslot(slot="l",name="avg_4080_lin_1#2$1",focus="l")]
[name="林雨霞"]也多亏这次机会，让我想明白了一些问题。
[charslot(slot="r",name="avg_npc_790_1#1$1",focus="r")]
[name="陈"]你接下来准备去维多利亚？我们可以同路。
[charslot(slot="l",name="avg_4080_lin_1#1$1",focus="l")]
[name="林雨霞"]不了。
[name="林雨霞"]我会回龙门。
[charslot(slot="r",name="avg_npc_790_1#1$1",focus="r")]
[name="陈"]“回龙门”的意思是......？
[charslot(slot="l",name="avg_4080_lin_1#1$1",focus="l")]
[name="林雨霞"]留下来。
[name="林雨霞"]“扔下包袱”是句漂亮话，一个人扔下的，总得有另一个人捡起来。
[name="林雨霞"]是去是留都是一个人的自由，但总要有人去照顾龙门。
[charslot(slot="r",name="avg_npc_790_1#7$1",focus="r")]
[name="陈"]嗯......
[charslot(slot="l",name="avg_4080_lin_1#10$1",focus="l")]
[name="林雨霞"]这句话是我说给自己听的，但你要是觉得我在批评你，我也很乐意。
[charslot(slot="r",name="avg_npc_790_1#8$1",focus="r")]
[name="陈"]你还有精神说这些废话，我倒是放心了一点。
[charslot(slot="l",name="avg_4080_lin_1#1$1",focus="l")]
[name="林雨霞"]鼠王的女儿，不一定是鼠王。但也可以是。
[charslot(slot="l",name="avg_4080_lin_1#7$1",focus="l")]
[name="林雨霞"]或者是，一个不一样的“鼠王”。
[name="林雨霞"]这一次，是我自己选的。
[name="林雨霞"]龙门有贫民区，但是不该有贫民区。这是件困难的事，也是不管多少年过去，都需要有人努力去做的事。
[name="林雨霞"]时代在向前走，但是不该有人被抛下。
[charslot(slot="r",name="avg_npc_790_1#8$1",focus="r")]
[name="陈"]这句话从你口中说出来，我可以相信。
[charslot(slot="r",name="avg_npc_790_1#5$1",focus="r")]
[name="陈"]话说......
[charslot(slot="l",name="avg_4080_lin_1#6$1",focus="l")]
[name="林雨霞"]有话直说，怎么连你也会支支吾吾的？
[charslot(slot="r",name="avg_npc_790_1#5$1",focus="r")]
[name="陈"]这几天，你有没有见过魏彦吾......？
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot="l",name="avg_2024_chyue_1#1$1")]
[charslot(slot="r",name="char_2005_weiyw_1#1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="r",name="char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]宗师要走了？
[charslot(slot="l",name="avg_2024_chyue_1#1$1",focus="l")]
[name="重岳"]嗯。
[name="重岳"]交接完公务，这就离开。
[charslot(slot="l",name="avg_2024_chyue_1#10$1",focus="l")]
[name="重岳"]说起来，我得对魏兄道谢。
[charslot(slot="r",name="char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]这又从何说起？
[charslot(slot="l",name="avg_2024_chyue_1#10$1",focus="l")]
[name="重岳"]魏兄的确相信了玉门一次。
[name="重岳"]也相信了，我的一些朋友。
[charslot(slot="r",name="char_2005_weiyw_1#5",focus="r")]
[name="魏彦吾"]事情已经结束。
[name="魏彦吾"]虽然受了些损失，但事态还在掌控之内。已经是不幸中的万幸。
[charslot(slot="l",name="avg_2024_chyue_1#10$1",focus="l")]
[name="重岳"]最重要的是，我看到了，不管多少年过去，这里的人们还是能团结一心。
[name="重岳"]玉门还是那个玉门。“人定胜天”，不是虚言。
[charslot(slot="l",name="avg_2024_chyue_1#4$1",focus="l")]
[name="重岳"]这样一来，我也能放心离开。
[charslot(slot="r",name="char_2005_weiyw_1#5",focus="r")]
[name="魏彦吾"]......
[name="魏彦吾"]这一次告别，就真的不知何时才能再见。
[name="魏彦吾"]前路山长水远，宗师珍重。
[charslot(slot="l",name="avg_2024_chyue_1#1$1",focus="l")]
[name="重岳"]庙堂风云诡谲，魏公也该当心。
[charslot(slot="r",name="char_2005_weiyw_1#5",focus="r")]
[name="魏彦吾"]宗师的提醒，我会放在心上。
[charslot(slot="r",name="char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]......突然想起，宗师昨天评价过陈的剑术。
[name="魏彦吾"]“炉火纯青，但不算登峰造极。”
[charslot(slot="l",name="avg_2024_chyue_1#1$1",focus="l")]
[name="重岳"]我是这样讲过。
[charslot(slot="r",name="char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]陈在剑术上有天赋，但毕竟修炼赤霄剑法的时日不算久。
[name="魏彦吾"]赤霄剑法的精髓，她还没有得到要领。
[charslot(slot="l",name="avg_2024_chyue_1#10$1",focus="l")]
[name="重岳"]原来魏公是要露一手武功。
[charslot(slot="r",name="char_2005_weiyw_1#1",focus="r")]
[name="魏彦吾"]之前向宗师提起过，云裂之剑，并非赤霄剑法的最后一式。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Image(image="35_i03", screenadapt="coverall",fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playsound(key="$d_avg_wind")]
以指为剑。
没有剑气激荡，却隐隐有风，杯中茶水泛起涟漪。
[name="魏彦吾"]赤霄的最后一式，名为天瞠。
[name="重岳"]剑意如何？
[name="魏彦吾"]天瞠之剑，当绝则绝。
[name="重岳"]心法如何？
[name="魏彦吾"]不破不立，破而后立。云裂之后，方能见苍穹怒目。
[name="魏彦吾"]不除心间迷障，不能领会剑意。
[name="重岳"]关隘如何？
[name="魏彦吾"]剑随心动，招出无悔。
[name="魏彦吾"]若一念回首，则剑失锋芒，反害其身。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[charslot]
[charslot(slot="m",name="char_2005_weiyw_1#1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[curtain]
[name="魏彦吾"]再会。
[dialog]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[charslot(slot ="m", afrom = 1, ato = 0,duration = 1.5)]
[delay(time=2)]
[playsound(key="$doorclosequite",volume=0.7)]
[delay(time=2)]
人离席，风还飘荡了许久。
男人盯着茶杯中的水纹沉思良久，终于露出一丝笑意。
[dialog]
[charslot(slot="m",name="avg_2024_chyue_1#10$1",duration=1)]
[delay(time=2)]
[name="重岳"]原来世上还有这样的剑法。
[StopMusic(fadetime=3)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[Background(image="35_g7_zuosroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_301_1#1$1",duration=0.5)]
[delay(time=1)]
[name="太傅"]进来吧。
[dialog]
[charslot]
[c

... (全文21042字符)
```

### training_act23side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动23side教学关_a

[PopupDialog(dialogHead="$avatar_jesica")] 这，这就是玉门城么？天灾工事都修得好高......
```

### training_act23side_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动23side教学关_b

[PopupDialog(dialogHead="$avatar_doberm")] 不要东张西望了！有敌袭，准备迎击！

[PopupDialog(dialogHead="$avatar_jesica")] 呜......知道了......

[PopupDialog(dialogHead="$avatar_beagle")] 杜宾教官，我也来帮忙！
```

### training_act23side_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动23side教学关_c

[PopupDialog(dialogHead="$avatar_beagle")] 是我的错觉吗？杰西卡今天打得又准又狠！

[PopupDialog(dialogHead="$avatar_doberm")] 不是你的错觉。炎国有句俗话说：居高临下，事半功倍。

[PopupDialog(dialogHead="$avatar_doberm")] 玉门的天灾工事修建得足够高大，部署在上面的干员依托于地形优势，在攻击地面敌人时<@tu.kw>造成的伤害会提升</>，而被地面敌人攻击时<@tu.kw>受到的伤害则会降低</>。

[PopupDialog(dialogHead="$avatar_doberm")] 当然，对于敌人来说也是如此。

```

### training_act23side_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动23side教学关_d

[PopupDialog(dialogHead="$avatar_jesica")] “对、对于敌人来说也是如此”难道是指......

[Tutorial(focusX=-300, focusY=100, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
没错。凭借着<@tu.kw>云梯</>的帮助，部分敌人也可以登上工事，威胁到我方干员的安全，请小心应对。

[Tutorial(focusX=-300, focusY=10, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
将敌人阻挡在天灾工事之下，这是最好的方式。

[PopupDialog(dialogHead="$avatar_melan")] 我也来帮忙。

```

### training_act23side_01_e

```
[HEADER(is_skippable=true, is_autoable=false)] 活动23side教学关_d

[PopupDialog(dialogHead="$avatar_jesica")] 啊！有敌人绕上来了！

[Tutorial(focusX=0, focusY=200, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
别惊慌。一些工事上的<@tu.kw>“城防路障”</>可以帮我们暂时延缓敌人的进攻。用它作掩护，快速歼灭敌人。

[PopupDialog(dialogHead="$avatar_jesica")] 好的教官，我......我会加油。

[PopupDialog(dialogHead="$avatar_kroos")] 我也来帮忙！
```


## 统计

- 总字符数：490898
- 对话行数：3519


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
