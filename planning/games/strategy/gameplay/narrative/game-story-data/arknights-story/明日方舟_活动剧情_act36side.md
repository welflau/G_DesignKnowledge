# 明日方舟 · 活动剧情 · act36side（21段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act36side」完整剧情脚本（21个文件，2536行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act36side
- 脚本文件数：21

### level_act36side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[name="法琳"]哥......快逃！
[Dialog]
[PlaySound(key="$d_avg_magicreverse",volume=1)]
[Background(image="bg_white",fadetime=1.5,screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.5, fadetime=0.1,a=1)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.5, fadetime=0.1,a=1)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[PlayMusic(intro="$m_sys_act01_intro", key="$m_sys_act01_loop", volume=0.6)]
[BackgroundTween(xScaleFrom=1.15, yScaleFrom=1.15, xScaleTo=1.15, yScaleTo=1.15, duration=2,xFrom=50, yFrom=0, xTo=0, yTo=0,duration=35, block=false,screenadapt="coverall")]
[Background(image="bg_white",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0.1, r=5, g=5, b=0, fadetime=2, block=true)]
[curtain(direction = 0,fillfrom = 0.5,fillto = 0.25, fadetime=1,a=1)]
[curtain(direction = 4,fillfrom = 0.5,fillto = 0.25, fadetime=1,a=1)]
[Delay(time=1)]	
[charslot(slot="m",name="avg_4142_laios_1#3$1",duration=1)]
[charslot(slot="m", action="zoom", poszoom = "0.35,0.65", scale=1.5,duration= 0)]
[Delay(time=2.5)]
[Subtitle(text="妹妹法琳在被炎龙吃掉的刹那，使用魔法将我们传送到了迷宫的外面。", x=300, y=550, alignment="center", size=24, delay=0.04, width=750)]
[subtitle]
[Delay(time=2)]
[charslot(slot="m",name="avg_4144_chilc_1#7$1",duration=1)]
[charslot(slot="m", action="zoom", poszoom = "0.65,0.49", scale=1.5,duration= 0)]
[Delay(time=2.5)]
[Subtitle(text="我们的行李和资金都掉落在迷宫深处，不得不几乎身无分文地再次进入迷宫，要赶在法琳被炎龙消化前把她救回来。", x=300, y=550, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4141_marcil_1#8$1",duration=1)]
[charslot(slot="m", action="zoom", poszoom = "0.35,0.59", scale=1.5,duration= 0)]
[Delay(time=2.5)]
[Subtitle(text="我们一路尝试通过食用魔物来填饱肚子。", x=300, y=550, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4143_sensi_1#1$1",duration=1)]
[charslot(slot="m", action="zoom", poszoom = "0.65,0.47", scale=1.5,duration= 0)]
[Delay(time=1)]
[Subtitle(text="虽然这样很艰苦，但是我们也获得了新的伙伴，解决了一路上遇到的各种问题，也对这座迷宫有了全新的认识。", x=300, y=550, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Delay(time=2.5)]
[charslot(duration=0.5)]
[Delay(time=1)]
[Delay(time=2)]
[Subtitle(text="但是在我们慢慢深入，以为一切顺利时，好像又陷入了新的困境......", x=300, y=550, alignment="center", size=24, delay=0.04, width=750)]
[subtitle]
[stopmusic(fadetime=1.5)]
[curtain(direction = 0,fillfrom = 0.25,fillto = 0.5, fadetime=1.5,a=1)]
[curtain(direction = 4,fillfrom = 0.25,fillto = 0.5, fadetime=1.5,a=1)]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(key="$normal_loop", volume=0.6,fadetime=2)]
[curtain]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Background(image="bg_forest",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[CameraShake(duration=1, xstrength=10, ystrength=10, vibrato=20, randomness=70, fadeout=true, block=false)]
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="m",name="avg_4142_laios_1#3$1",posfrom="0,-20",posto="0,0",afrom=0,ato=1,isblock=true,duration=0.5)]
[name="莱欧斯"]法琳！
[Dialog]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4142_laios_1#13$1",focus="m")]
[name="莱欧斯"]啊，是梦......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4141_marcil_1#7$1",focus="m")]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="玛露西尔"]你总算醒了，莱欧斯！
[charslot(slot="m",name="avg_4141_marcil_1#9$1",focus="m")]
[name="玛露西尔"]你精神怎么样，有觉得头晕吗？
[charslot(slot="m",name="avg_4142_laios_1#13$1",focus="m")]
[name="莱欧斯"]头倒是不怎么晕......但突然感觉有点饿了。
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]这里是......？
[Dialog]
[charslot]
[PlaySound(key="$d_avg_amb_forestnight_loop",volume=0.5,channel="1",loop=true,fadetime=1.5)]
[Delay(time=1.5)]
[Background(image="38_g20_skyblue_R2",screenadapt="showall",fadetime=2.5)]
[Delay(time=6)]
[Background(image="bg_forest",screenadapt="showall",fadetime=2.5)]
[Delay(time=3)]
[stopsound(channel="1",fadetime=1.5)]
[charslot(slot="m",name="avg_4142_laios_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="莱欧斯"]天空，太阳，树林......还有......
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]这里看起来很像是迷宫的外面，但不论是我、森西还是齐尔查克，都觉得这里不是任何我们见过的地方。
[Dialog]
[PlaySound(key="$d_avg_magic_1",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.2, block=true)]
[PlaySound(key="$d_avg_magic_1",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_4141_marcil_1#9$1",focus="m")]
[name="玛露西尔"]而且你看，还是没有反应......我都试了好几次了，微小精灵一点都不回应我。
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[multiline(name="莱欧斯")]真是少见......
[charslot(slot="m",name="avg_4142_laios_1#16$1",focus="m")]
[multiline(name="莱欧斯",end=true)]森西？你在干什么？
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="m",name="avg_4143_sensi_1#1$1",afrom=0,ato=1,duration=0.5)]
[charslot(slot="m",posfrom="0,-20",posto="0,0",duration=2)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]老夫在调查这里的土质。
[charslot(slot="m",name="avg_4143_sensi_1#3$1",focus="m")]
[name="森西"]你们看，这里的土壤湿润、色深，在掌心揉搓变热之后有臭味，说明里面含有大量腐殖质......
[charslot(slot="m",name="avg_4141_marcil_1#5$1",focus="m")]
[name="玛露西尔"]也就是说？
[Dialog]
[charslo

... (全文20431字符)
```

### level_act36side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_cave_2",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$darkness_03_loop", volume=0.6,fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$rungeneral",volume=1)]
[charslot(slot="m",name="avg_4142_laios_1#1$1",duration=1)]
[Delay(time=2)]
[name="莱欧斯"]我还是觉得哪里很奇怪。
[charslot(slot="m",name="avg_4141_marcil_1#4$1",focus="m")]
[name="玛露西尔"]莱欧斯！都这种时候了，你怎么还在乱想！我不觉得我们逃到这里来那个兽人就不会发现我们了啊！他要是追到这里来了怎么办！
[name="玛露西尔"]难道你一点危机感都没有吗！这里可是从来没有人知道的地方，所有的知识都不适用了啊！
[charslot(slot="m",name="avg_4142_laios_1#2$1",focus="m")]
[name="莱欧斯"]没想到这些虫子外壳不同，习性和攻击性也都不一样......
[charslot(slot="m",name="avg_4142_laios_1#16$1",focus="m")]
[name="莱欧斯"]但是，它们为什么会跟那个像兽人一样壮的生物一起行动，这些虫子难道真有可以被驯化的智力水平吗......？
[charslot(slot="m",name="avg_4144_chilc_1#16$1",focus="m")]
[name="齐尔查克"]嘘——小点声，那个兽人来了。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_npc_010",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_010",focus="none")]
[name="莱欧斯"]......
[name="森西"]......
[name="玛露西尔"]......
[Dialog]
[charslot(slot="m",name="avg_npc_010",focus="m")]
[PlaySound(key="$e_atk_saw_n_1",volume=1)]
[CameraShake(duration=1, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_010",focus="none")]
[name="玛露西尔"]（小声）他、他过来了！！
[Dialog]
[charslot]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_atk_saw_n_1", volume=1,channel="1")]
[PlaySound(key="$fightgeneral",volume=1,channel="2")]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_atk_saw_n_1", volume=1,channel="1")]
[PlaySound(key="$fightgeneral",volume=1,channel="2")]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_atk_saw_n_1", volume=1,channel="1")]
[PlaySound(key="$fightgeneral",volume=1,channel="2")]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[name="玛露西尔"]（小声）天哪！他怎么在攻击这些虫子？所以他们并不是同伴吗？
[name="玛露西尔"]（小声）他是在无差别地攻击身边的生物吗！
[Dialog]
[name="莱欧斯"]......等等，我有个想法。
[name="玛露西尔"]你要做什么！莱欧斯！
[Dialog]
[charslot(slot="l",name="avg_npc_010",focus="all")]
[Delay(time=0.5)]
[stopmusic(fadetime=1.5)]
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="r",name="avg_4142_laios_1#7$1",posfrom="0,-30",posto="0,0",afrom=0,ato=1,isblock=true,duration=0.5)]
[Delay(time=2)]
[charslot(slot="r",name="avg_4142_laios_1#7$1",focus="r")]
[name="莱欧斯"]嗨？
[charslot(slot="r",name="avg_4142_laios_1#7$1",focus="none")]
[name="玛露西尔"]欸？
[charslot(slot="l",name="avg_npc_010",focus="l")]
[name="恐怖兽人？"]......嗨？？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4141_marcil_1#2$1",focus="m")]
[name="玛露西尔"]......
[charslot(slot="m",name="avg_4144_chilc_1#7$1",focus="m")]
[name="齐尔查克"]......
[charslot(slot="m",name="avg_4143_sensi_1#4$1",focus="m")]
[name="森西"]......
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6,fadetime=1)]
[charslot(slot="m",name="avg_4141_marcil_1#4$1",focus="m")]
[name="玛露西尔"]我受够了！既然这样，要来就来吧！
[Dialog]
[PlaySound(key="$runsand",volume=1)]
[charslot(slot="m",posfrom="0,0",posto="-200,0",duration=1)]
[charslot(slot="m",afrom=1,ato=0,duration=0.5)]
[Delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_4143_sensi_1#5$1",focus="m")]
[name="森西"]玛露西尔！等等！
[charslot(slot="m",name="avg_4141_marcil_1#4$1",focus="m")]
[name="玛露西尔"]为了法琳，我可不能在这里被未知的恐怖兽人杀掉！
[charslot(slot="m",name="avg_npc_010",focus="m")]
[name="恐怖兽人？"]啊？
[charslot(slot="m",name="avg_4141_marcil_1#9$1",focus="m")]
[name="玛露西尔"]啊？
[charslot(slot="m",name="avg_npc_010",focus="m")]
[name="恐怖兽人？"]谁说要杀......我不杀你们！
[name="恐怖兽人？"]......我看起来这么凶恶吗？
[charslot(slot="m",name="avg_4141_marcil_1#4$1",focus="m")]
[name="玛露西尔"]......不用再废话了！
[charslot(slot="m",name="avg_npc_010",focus="m")]
[name="恐怖兽人？"]喂，小心——
[Dialog]
[charslot]
[stopmusic(fadetime=1.5)]
[charslot(slot="m",name="avg_npc_1432_1#1$1",focus="m")]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_atk_saw_n_1", volume=1,channel="1")]
[PlaySound(key="$fightgeneral",volume=1,channel="2")]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[charslot(duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_010",focus="m")]
[name="恐怖兽人"]这下最后一只也解决了，这些乱跑出来的小东西，真让人不省心。
[charslot(slot="m",name="avg_4142_laios_1#18$1",focus="m")]
[name="莱欧斯"]所以你果然不是无差别攻击人的恐怖狂暴兽人......！你只是想把这些虫子都处理掉......我就知道！
[charslot(slot="m",name="avg_npc_010",focus="m")]
[name="不是恐怖兽人"]......啊？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="54_g1_bobfarm",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]......
[charslot(slot="m",name="avg_4144_chilc_1#10$1",focus="m")]
[name="齐尔查克"]......
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")

... (全文20766字符)
```

### level_act36side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_jungle_1",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6,fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_4141_marcil_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]莱欧斯，快跟上啦。
[charslot(slot="m",name="avg_4142_laios_1#8$1",focus="m")]
[name="莱欧斯"]快来看这颗蘑菇！迷宫里最大的走路菇都没有这么大吧！
[charslot(slot="m",name="avg_4142_laios_1#18$1",focus="m")]
[name="莱欧斯"]要是走路菇长得这么大该有多威风啊......一会儿的午饭可以考虑吃它吗？
[charslot(slot="m",name="avg_4141_marcil_1#7$1",focus="m")]
[name="玛露西尔"]你小心一点啊，美食指南里说丛林里面的蘑菇多多少少都有一些毒性。
[name="玛露西尔"]比如吃了之后会全身起疹子，会导致血液凝固，会不断呕吐直到把内脏都吐出来之类的......
[charslot(slot="m",name="avg_4144_chilc_1#10$1",focus="m")]
[name="齐尔查克"]......不敢想象写下这本指南的人都经历了什么。
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]老夫只跟着兽人学了分辨迷宫蘑菇的方法，这些没见过的还是不要轻易尝试了。
[charslot(slot="m",name="avg_4142_laios_1#8$1",focus="m")]
[name="莱欧斯"]可这边有动物把这种厚厚的蘑菇当作食物！
[charslot(slot="m",name="avg_4143_sensi_1#3$1",focus="m")]
[name="森西"]不行，如果只有一两种动物在吃，那么这种植物对大部分动物可能都有毒性。
[charslot(slot="m",name="avg_4143_sensi_1#9$1",focus="m")]
[name="森西"]换句话说，如果很多动物都在吃，那么它才有可能是没有毒性的。
[charslot(slot="m",name="avg_4142_laios_1#13$1",focus="m")]
[name="莱欧斯"]嗯......
[Dialog]
[charslot]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="？？？"]（低沉的咆哮）
[Dialog]
[stopmusic(fadetime=1.5)]
[charslot(slot="m",name="avg_4144_chilc_1#8$1",focus="m")]
[name="齐尔查克"]什么声音？
[Dialog]
[charslot]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="？？？"]（尖锐的蜂鸣）
[charslot(slot="m",name="avg_4144_chilc_1#11$1",focus="m")]
[name="齐尔查克"]有什么东西往这边飞来了！大家小心！
[Dialog]
[charslot]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="莱欧斯小队"]哇啊啊啊啊啊啊啊啊！
[Dialog]
[PlaySound(key="$grenade_explosion", volume=1)]
[PlaySound(key="$d_sp_ballista", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=1.7, xstrength=20, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.5, block=true)]
[delay(time=2)]
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[charslot]
[Background(image="bg_jungle_1",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1429_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="大祭司"]（东敲敲，西敲敲）
[charslot(slot="m",name="avg_npc_1429_1#5$1",focus="m")]
[name="大祭司"]嚯！刚才那一发炸得真够狠的！
[charslot(slot="m",name="avg_npc_1429_1#6$1",focus="m")]
[name="大祭司"]幸好找了没人的测试场地。
[charslot(slot="m",name="avg_npc_1429_1#1$1",focus="m")]
[name="大祭司"]我看看......
[charslot(slot="m",name="avg_npc_1429_1#1$1",focus="m")]
[name="大祭司"]膛压，爆表。温度，爆表。装载量，也爆表！
[name="大祭司"]看来还是要劲够大才好使。
[charslot(slot="m",name="avg_npc_1429_1#6$1",focus="m")]
[name="大祭司"]接下来就是最后调试一下刚才的配置，松松皮带，紧紧螺丝就完成了！
[name="大祭司"]只要不出什么意外，我的最新力作“无敌的酷东西”就可以开出去了！
[name="大祭司"]啊，得赶紧先把易爆品都拆掉。
[name="大祭司"]远离明火，安全第一~
[name="大祭司"]（东敲敲，西敲敲）
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_jungle_1",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=2.5)]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_4142_laios_1#7$1",duration=1.5)]
[Delay(time=2)]
[name="莱欧斯"]咳咳......那边有东西一直在爆炸......！
[charslot(slot="m",name="avg_4141_marcil_1#6$1",focus="m")]
[name="玛露西尔"]咳咳......！
[charslot(slot="m",name="avg_4142_laios_1#3$1",focus="m")]
[name="莱欧斯"]玛露西尔，你没事吧？
[charslot(slot="m",name="avg_4141_marcil_1#6$1",focus="m")]
[name="玛露西尔"]我、我还好！只是，有点头晕......
[Dialog]
[charslot]
[name="？？？"]（低沉的咆哮）
[charslot(slot="m",name="avg_4142_laios_1#14$1",focus="m")]
[name="莱欧斯"]怎么还有......！小心！
[charslot(slot="m",name="avg_4141_marcil_1#4$1",focus="m")]
[name="玛露西尔"]是魔像吗？还是石像鬼？！
[name="玛露西尔"]看我用魔法——
[Dialog]
[charslot]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_magicreverse",volume=1)]
[PlaySound(key="$d_sp_ballista",volume=1.0)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_magicreverse",volume=1)]
[PlaySound(key="$d

... (全文16228字符)
```

### level_act36side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_village",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$dontmaketrouble_intro", key="$dontmaketrouble_loop", volume=0.6,fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[playsound(key="$d_avg_goldenlight", volume=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=20, randomness=30, fadeout=true,block=true)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=20, randomness=30, fadeout=true)]
[Effect(name="$e_magic_fire_01",y=0,x=0,layer = 3)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, fadetime=1.5, block=false)]
[Delay(time=1)]	
[charslot(slot="m",name="avg_npc_071",focus="m")]
[name="阿达克利斯A"]我的晒鳞架！我的床！
[charslot(slot="m",name="avg_4143_sensi_1#5$1",focus="m")]
[name="森西"]莱欧斯！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4142_laios_1#9$1",posfrom="-100,0",posto="0,0",afrom=0,ato=1,isblock=true,duration=1)]
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="m",posfrom="0,0",posto="100,0",duration=1)]
[charslot(slot="m",afrom=1,ato=0,duration=0.5)]
[Delay(time=1)]
[charslot]
[charslot(slot="m",name="avg_4141_marcil_1#23$1",focus="m")]
[Delay(time=1)]
[PlaySound(key="$d_avg_punchsp2",volume=1)]
[charslot(slot="l",name="avg_4142_laios_1#7$1",posfrom="0,0",posto="100,0",duration=1)]
[charslot(slot="l",afrom=0,ato=1,duration=0.5)]
[charslot(slot="m",posfrom="0,0",posto="200,0",duration=0.85)]
[charslot(slot="m",afrom=1,ato=0,duration=0.5)]
[Delay(time=1.5)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_goldenlight", volume=1)]
[charslot(slot="l",posfrom="100,0",posto="0,0",duration=1)]
[charslot(slot="l",afrom=1,ato=0,duration=0.5)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[charslot]
[charslot(slot="m",name="avg_4144_chilc_1#16$1",focus="m")]
[name="齐尔查克"]总觉得玛露西尔平时都没有这么敏捷......！
[charslot(slot="m",name="avg_4142_laios_1#22$1",focus="m")]
[name="莱欧斯"]她现在恐怕把我们当成炎龙了！
[charslot(slot="m",name="avg_4144_chilc_1#16$1",focus="m")]
[name="齐尔查克"]那怎么办？
[charslot(slot="m",name="avg_4142_laios_1#9$1",focus="m")]
[name="莱欧斯"]既然她现在想的都是法琳，让我来试试......
[charslot(slot="m",name="avg_4142_laios_1#3$1",focus="m")]
[name="莱欧斯"]玛露西尔，是我，法琳的哥哥，莱欧斯！
[charslot(slot="m",name="avg_4141_marcil_1#23$1",focus="m")]
[name="玛露西尔"]你、你根本不是莱欧斯！莱欧斯明明是个能摆出奇怪的姿势威吓住蛇尾鸡的家伙！
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m")]
[name="齐尔查克"]这还确实挺有说服力的。
[charslot(slot="m",name="avg_4142_laios_1#3$1",focus="m")]
[name="莱欧斯"]既然这样，只能通过这种方式证明我的身份了！
[Dialog]
[CameraShake(duration=-1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4142_laios_1#4$1",focus="m")]
[CameraShake(duration=1, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="莱欧斯"]咯——
[Dialog]
[charslot(slot="m",name="avg_4141_marcil_1#23$1",focus="m")]
[Delay(time=1)]
[charslot(slot="m",name="avg_4141_marcil_1#23$1",focus="m")]
[name="玛露西尔"]......
[name="玛露西尔"]莱欧斯......真的是你......？
[charslot(slot="m",name="avg_4144_chilc_1#7$1",focus="m")]
[name="齐尔查克"]居然真有用？！
[charslot(slot="m",name="avg_4141_marcil_1#23$1",focus="m")]
[name="玛露西尔"]莱欧斯！炎龙把法琳吃了，我们要打败它，把法琳抢回来，然后复活她！
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m")]
[name="齐尔查克"]等等，你指着我干什么！我哪里像炎龙？
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[playsound(key="$e_atk_magic_n", volume=1)]
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m")]
[charslot(slot="m",posfrom="0,0",posto="-100,0",duration=1)]
[charslot(slot="m",afrom=1,ato=0,duration=0.5)]
[CameraShake(duration=0.3, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Blocker(a=0, fadetime=1.5, block=true)]
[charslot]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[playsound(key="$e_atk_magic_n", volume=1)]
[charslot(slot="m",name="avg_4143_sensi_1#5$1",focus="m")]
[charslot(slot="m",posfrom="0,0",posto="100,0",duration=1)]
[charslot(slot="m",afrom=1,ato=0,duration=0.5)]
[CameraShake(duration=0.3, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[Delay(time=2)]
[charslot(slot="l",name="avg_4144_chilc_1#15$1",posfrom="-100,0",posto="0,0",duration=1)]
[charslot(slot="l",afrom=0,ato=1,duration=0.5)]
[charslot(slot="r",name="avg_4143_sensi_1#5$1",posfrom="100,0",posto="0,0",duration=1)]
[charslot(slot="r",afrom=0,ato=1,duration=0.5)]
[Delay(time=2)]
[name="齐尔查克&森西"]哇啊！
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[playsound(key="$e_atk_magic_n", volume=1)]
[charslot(slot="l",posfrom="0,0",posto="-100,0",duration=1)]
[charslot(slot="l",afrom=1,ato=0,duration=0.5)]
[charslot(slot="r",posfrom="0,0",posto="100,0",duration=1)]
[charslot(slot="r",afrom=1,ato=0,duration=0.5)]
[CameraShake(duration=0.3, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Blocker(a=0, fadetime=1.5, block=true)]
[charslot]
[charslot(slot="m",name="avg_4142_laios_1#7$1",focus="m")]
[name="莱欧斯"]她这是怎么了？
[charslot(slot="m",name="avg_npc_071",focus="m")]
[name="阿达克利斯A"]呜哇！她是不是眼睛打转，脚步凌乱？
[charslot(slot="m",name="avg_4142_laios_1#9$1",focus="m")]
[name="莱欧斯"]对！
[charslot(slot="m",name="avg_npc_070",focus="m")]
[name="阿达克利斯B"]张牙舞爪，胡言乱语？
[charslot(slot="m",name="avg_4142_laios_1#22$1",focus="m")]
[name="莱欧斯"]对对！
[charslot(slot="m",name="avg_npc_071",focus="m")]
[name="阿达克利斯A"]口吐白沫？
[charslot(slot="m",name="avg_4142_laios_1#7$1",focus="m")]
[name="莱欧斯"]对对对！
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_071",focus="l")]
[charslot(slot="r",name="avg_npc_070",foc

... (全文24563字符)
```

### level_act36side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="46_g4_rmbtwild_d",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.6,fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_4142_laios_1#13$1",duration=1)]
[Delay(time=2)]
[name="莱欧斯"]呼......呼......
[charslot(slot="m",name="avg_4141_marcil_1#19$1",focus="m")]
[name="玛露西尔"]（哼歌）
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m")]
[multiline(name="齐尔查克")]这片荒地根本看不到头，我们得走到什么时候啊——
[charslot(slot="m",name="avg_4144_chilc_1#16$1",focus="m")]
[multiline(name="齐尔查克",end=true)]喂，你这家伙也太开心了吧......
[charslot(slot="m",name="avg_4141_marcil_1#17$1",focus="m")]
[name="玛露西尔"]（哼歌）因为我得到了一件这个世界的魔法器具呀~
[charslot(slot="m",name="avg_4144_chilc_1#2$1",focus="m")]
[name="齐尔查克"]不过就是别人不要的东西......
[charslot(slot="m",name="avg_4141_marcil_1#17$1",focus="m")]
[name="玛露西尔"]哼，难道你看到一种全新的开锁工具不会觉得开心吗？
[charslot(slot="m",name="avg_4141_marcil_1#3$1",focus="m")]
[name="玛露西尔"]来到这个世界后，我一直觉得自己的魔法施展得没有之前那么顺畅了，这里好像有一股我没能利用上的......奇怪的魔力。
[charslot(slot="m",name="avg_4141_marcil_1#17$1",focus="m")]
[name="玛露西尔"]但是现在我有了这个D32钢手电筒！
[name="玛露西尔"]老板说这种叫“D32钢”的材料可以承载更大的能量输出，这里的魔法师会用它来做魔法器具，说不定我能通过它更好地使用魔法呢！
[charslot(slot="m",name="avg_4141_marcil_1#18$1",focus="m")]
[name="玛露西尔"]而且我亲眼见到老板用它施放了类似闪光魔法的法术！
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]老夫总觉得，世上不会有不需要付出努力就可以得到的好东西。
[charslot(slot="m",name="avg_4141_marcil_1#16$1",focus="m")]
[name="玛露西尔"]可能老板不希望好东西被白白浪费，就送给了我这个超厉害的魔法师吧~
[charslot(slot="m",name="avg_4141_marcil_1#17$1",focus="m")]
[name="玛露西尔"]我现在对这个世界的魔法原理超感兴趣的。
[charslot(slot="m",name="avg_4142_laios_1#18$1",focus="m")]
[name="莱欧斯"]唔......那要不要趁现在多练习练习？玛露西尔，你能试试用它把那些果子弄下来吗？
[name="莱欧斯"]这里长果子的树真的很少，也就水边有这么几棵，错过了可能就没有了。
[charslot(slot="m",name="avg_4141_marcil_1#22$1",focus="m")]
[multiline(name="玛露西尔")]其实是你想尝尝那些果子吧......
[charslot(slot="m",name="avg_4141_marcil_1#17$1",focus="m")]
[multiline(name="玛露西尔",end=true)]好吧，就当作是练习吧，我试试好了！
[charslot(slot="m",name="avg_4141_marcil_1#3$1",focus="m")]
[name="玛露西尔"]唔......
[name="玛露西尔"]嗯......！
[Dialog]
[stopmusic(fadetime=1.5)]
[charslot(slot="m",name="avg_4141_marcil_1#20$1",focus="m")]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=20, randomness=70, fadeout=true, block=true)]
[Delay(time=1.5)]
一片安静。
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.6,fadetime=1)]
[charslot(slot="m",name="avg_4144_chilc_1#2$1",focus="m")]
[name="齐尔查克"]什么都没有发生呢。
[charslot(slot="m",name="avg_4141_marcil_1#7$1",focus="m")]
[name="玛露西尔"]怎、怎么可能！之前在老板手里明明还能正常用的，而且我有感觉到它在回应我......！
[charslot(slot="m",name="avg_4144_chilc_1#2$1",focus="m")]
[name="齐尔查克"]那就是错觉。
[charslot(slot="m",name="avg_4141_marcil_1#13$1",focus="m")]
[name="玛露西尔"]哼！我再来一遍！
[name="玛露西尔"]唔唔......！
[Dialog]
[charslot(slot="m",name="avg_4141_marcil_1#20$1",focus="m")]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=20, randomness=70, fadeout=true, block=true)]
[Delay(time=1.5)]
又是一片安静。
[charslot(slot="m",name="avg_4144_chilc_1#2$1",focus="m")]
[name="齐尔查克"]还是什么都没有发生哦。
[name="齐尔查克"]玛露西尔，这个什么手电筒你真的能用吗......？
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]要不还是用法杖吧？
[charslot(slot="m",name="avg_4141_marcil_1#9$1",focus="m")]
[name="玛露西尔"]不过是还需要适应的问题！只要给我一点时间，我就能弄明白......
[charslot(slot="m",name="avg_4141_marcil_1#3$1",focus="m")]
[name="玛露西尔"]呼——
[charslot(slot="m",name="avg_4141_marcil_1#20$1",focus="m")]
[name="玛露西尔"]嘿......！
[Dialog]
[PlaySound(key="$d_avg_magicreverse")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.4, fadetime=0.4,a=1)]
[Blocker(a=0.5, r=255, g=255, b=255, fadetime=1.5, block=false)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.4, fadetime=0.4,a=1)]
[Delay(time=1.5)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[curtain(fadetime=0.1,a=1)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[charslot]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_4142_laios_1#8$1",focus="m")]
[name="莱欧斯"]哦！成功了！
[charslot(slot="m",name="avg_4142_laios_1#7$1",focus="m")]
[name="莱欧斯"]玛露西尔，你果然......呃？
[name="莱欧斯"]怎么你炸的是自己？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4141_marcil_1#6$1",duration=1)]
[Delay(time=2)]
[name="玛露西尔"]......
[name="玛露西尔"]咳咳咳咳！
[name="玛露西尔"]咳咳咳咳！咳咳咳咳！
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m")]
[name="齐尔查克"]......都说了不要逞强硬来啊......
[charslot(slot="m",name="avg_4141_marcil_1#6$1",focus="m")]
[name="玛露西尔"]怎么回事......为什么魔法会从这个魔法器具的末端冒出来......？
[name="玛露西尔"]他们这里的魔法器具怎么这么难控制......？
[charslot(slot="m",name="avg_4143_sensi_1#15$1",focus="m")]
[name="森西"]所以老夫很讨厌魔法。
[charslot(slot="m",name="avg_4141_marcil_1#6$1",focus="m")]
[name="玛露西尔"]这不一样......！咳咳咳咳咳！！
[name="玛露西尔"]下一次，下一次我一定就能成功了！
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="46_g1_transporter",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6,fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_4141_marcil_1#11$1",duration=1)]
[Delay(time=2)]
[name="玛露西尔"]老板！这个D32钢手电筒好像有问题——
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="厂主"]不是吧！白送给你我最宝贝的D32钢手电筒，还要被你们找麻烦？
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]咳咳......没有！我只是想问问，你们这里还有相关的书卖吗？我还是想系统地学一下......
[charslot(sl

... (全文19253字符)
```

### level_act36side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="46_g6_rmbtmine",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$darkness_03_loop", volume=0.6,fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$a_bat_buildingshaking_1",volume=1)]
[CameraShake(duration=2.5, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=2)]	
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="m",name="avg_4143_sensi_1#1$1",duration=1)]
[Delay(time=2)]
[name="森西"]......小心！我们好像是掉进矿洞里了！
[name="森西"]按刚才那个工人的说法，源石虫已经在这个矿洞里建起自己的巢穴了！
[charslot(slot="m",name="avg_4142_laios_1#9$1",focus="m")]
[name="莱欧斯"]因为工厂快要倒闭了，所以这里就被源石虫占领了吗......？
[charslot(slot="m",name="avg_4141_marcil_1#9$1",focus="m")]
[name="玛露西尔"]这里有赤金源石虫吗......？
[charslot(slot="m",name="avg_4142_laios_1#9$1",focus="m")]
[name="莱欧斯"]那边的那群看起来只是普通的源石虫。
[name="莱欧斯"]趁它们还没发现我们，快走！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="46_g6_rmbtmine",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4143_sensi_1#1$1",duration=1)]
[Delay(time=2)]
[name="森西"]......这里也没有赤金源石虫，老夫看了，都是普通的品种。
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]《鲍勃的美食指南》上写赤金源石虫是荒野上的常见品种，“生活在岩石缝或者是洞穴中”“与其他品种的源石虫生活习性相同”......
[charslot(slot="m",name="avg_4142_laios_1#16$1",focus="m")]
[name="莱欧斯"]在这里应该就能找到的......
[dialog]
[charslot]
[stopmusic(fadetime=1.5)]
[charslot(slot="l",name="avg_4144_chilc_1#15$1")]
[charslot(slot="m",name="avg_4141_marcil_1#9$1")]
[charslot(slot="r",name="avg_4143_sensi_1#15$1")]
[Delay(time=2)]
[charslot(slot="m",name="avg_4141_marcil_1#9$1",focus="m")]
[name="玛露西尔"]......你没有感觉到自己的脑袋上有东西吗？
[dialog]
[charslot]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.6,fadetime=1)]
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]嗯？啊！
[charslot(slot="m",name="avg_4142_laios_1#18$1",focus="m")]
[name="莱欧斯"]这只是源石虫的幼虫，它的甲壳部分刚刚长成，现在还是比较柔软的状态。
[name="莱欧斯"]加上它正在努力分泌黏液固化甲壳，所以体温上升了不少，让它趴在头上还挺舒服的。
[name="莱欧斯"]玛露西尔要不要试一下？
[dialog]
[charslot]
[charslot(slot="l",name="avg_4144_chilc_1#15$1",focus="m")]
[charslot(slot="m",name="avg_4141_marcil_1#22$1",focus="m")]
[charslot(slot="r",name="avg_4143_sensi_1#15$1",focus="m")]
[Delay(time=1)]
[charslot(slot="l",afrom=1,ato=0,duration=1.5,focus="m")]
[charslot(slot="r",afrom=1,ato=0,duration=1.5,focus="m")]
[Background(image="bg_black",screenadapt="showall",fadetime=2.5)]
[Delay(time=2.5)]
[charslot(slot = "m",action="zoom", poszoom = "0.4,0.72", scale=1.85, duration = 0,focus="m")]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_4142_laios_1#20$1",afrom=0,ato=0.5,focus="m",duration=1.5)]
[Delay(time=4.5)]
[charslot(slot="l",afrom=0.5,ato=0,focus="m",duration=1.5)]
[charslot(slot="r",name="avg_npc_1431_1#1$1",posfrom="-450,380",posto="-450,380",afrom=0,ato=0.7,focus="m",duration=1.5)]
[Delay(time=4.5)]
[charslot]
[Background(image="46_g6_rmbtmine",screenadapt="showall")]
[charslot(slot="l",name="avg_4144_chilc_1#15$1",focus="m")]
[charslot(slot="m",name="avg_4141_marcil_1#22$1",focus="m")]
[charslot(slot="r",name="avg_4143_sensi_1#15$1",focus="m")]
[Delay(time=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=30, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="玛露西尔"]......不要！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[stopmusic(fadetime=1.5)]
[Background(image="46_g6_rmbtmine",screenadapt="showall")]
[Delay(time=2)]
[PlayMusic(key="$darkness_03_loop", volume=0.6,fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_4144_chilc_1#11$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4144_chilc_1#11$1",focus="m")]
[name="齐尔查克"]再往里走感觉就有些不妙了......
[name="齐尔查克"]除了源石虫，好像还有别的生物在那里活动的声音......
[name="齐尔查克"]我们就在这里返回吧？
[charslot(slot="m",name="avg_4142_laios_1#13$1",focus="m")]
[name="莱欧斯"]可是还没找到赤金源石虫......
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]......这里真的有这个品种吗？
[name="玛露西尔"]或许赤金源石虫的分泌物用金色的粉就能代替呢？
[charslot(slot="m",name="avg_4143_sensi_1#3$1",focus="m")]
[name="森西"]再深入一点点吧，老夫不想让那些真心期盼黄金萝卜的年轻人失望。
[name="森西"]而且，找到了赤金源石虫，说不定就能买那辆车了。
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]嗯......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="46_g6_rmbtmine",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="l",name="avg_npc_1431_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_1431_1#1$1",duration=1)]
[Delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m")]
[name="齐尔查克"]嘘，你们脚步声轻一点。
[name="齐尔查克"]后面还有一群，也不像是赤金源石虫啊......都不是金色的。
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]那是什么......？
[dialog]
[charslot]
[stopmusic(fadetime=1.5)]
[PlaySound(key="$d_avg_strngspllmgc",volume=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0.5,g=0.5, b=0, fadetime=0.05, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[charslot(slot="m",name="avg_4142_laios_1#3$1",focus="m")]
[name="莱欧斯"]——是酸液源石虫！
[name="莱欧斯"]大鲍勃说过，这东西的黏液腐蚀性很强！小心不要被黏液溅到！
[dialog]
[charslot]
[PlaySound(key="$d_avg_strngspllmgc",volume=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0,g=0, b

... (全文25376字符)
```

### level_act36side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
沙沙、沙沙——
突如其来的声响打断了齐尔查克的梦境。
自从来到这个陌生的地方，他总是会轻易地被周围细小的动静惊醒。
他来不及思考那个梦的含义，翻身而起，看向应该在守夜的莱欧斯的方向。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="40_g1_blackforest",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
所幸，这个平日里总有些不着调的家伙，在这种时候还是十分可靠的。
他已经唤醒了森西和玛露西尔，并举起了武器。
[Dialog]
[charslot(slot="l",name="avg_4144_chilc_1#11$1",duration=1.5)]
[charslot(slot="r",name="avg_4142_laios_1#9$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="r",name="avg_4142_laios_1#9$1",focus="r")]
[name="莱欧斯"]齐尔查克，我们来吸引注意力，你来好好确认一下它们的状况吧。
[charslot(slot="l",name="avg_4144_chilc_1#11$1",focus="l")]
[name="齐尔查克"]明白。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="r",name="avg_4142_laios_1#9$1",focus="none")]
[PlaySound(key="$runsand",volume=1)]
[Delay(time=2.5)]
齐尔查克发现，这只是一群小队曾遭遇过多次的魔物，且对方还没有注意到他们。
他稍稍舒了口气，把这个消息带回给了自己的同伴们。
[Dialog]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
来到这个名叫泰拉的世界后，他们已经见识了太多陌生的事物。
一行人交换了眼神，确认彼此做好了战斗准备。
[Dialog]
[charslot(slot="r",name="avg_4142_laios_1#9$1",focus="r")]
[name="莱欧斯"]好，我们上！
[Dialog]
[PlaySound(key="$runsand",volume=1)]
[charslot(slot="l",name="avg_4144_chilc_1#11$1",posfrom="0,0",posto="-100,0",afrom=1,ato=0,duration=1.5)]
[charslot(slot="r",name="avg_4142_laios_1#9$1",posfrom="0,0",posto="100,0",afrom=1,ato=0,duration=1.5)]
[Delay(time=2)]
必须在这未知的世界里避开各种危险，无论是依靠那个罗德岛，还是自己另找办法，他们终究是要回去的，他想。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="40_g1_blackforest",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]呼......总算结束了。
[name="玛露西尔"]我难得做了一个美梦呢，真浪费。
[charslot(slot="m",name="avg_4144_chilc_1#2$1",focus="m")]
[name="齐尔查克"]从你的睡相来看，你每天都在做美梦吧。
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]也没有啦......等等，我的睡相很糟糕吗？
[charslot(slot="m",name="avg_4144_chilc_1#2$1",focus="m")]
[name="齐尔查克"]那倒没有，我猜的。
[charslot(slot="m",name="avg_4141_marcil_1#14$1",focus="m")]
[name="玛露西尔"]唔，话说我们已经在这片黑森林里走了好几天了。
[name="玛露西尔"]这里真的有萨米的部族吗？
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]萨米的本土部族都生活在一些奇怪的地方，而且大多不欢迎外人。
[name="齐尔查克"]哪有那么简单就能找到。
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]说得也是......唉，没想到这里居然这么偏僻。
[charslot(slot="m",name="avg_4144_chilc_1#12$1",focus="m")]
[name="齐尔查克"]要去找雪祀的事可是玛露西尔你提出来的，这就打退堂鼓了？
[charslot(slot="m",name="avg_4141_marcil_1#13$1",focus="m")]
[name="玛露西尔"]我提的时候又不知道这里的环境这么糟糕，还很吓人！
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]我们刚到萨米的时候，那边的条件明明还是很好的......
[charslot(slot="m",name="avg_4141_marcil_1#14$1",focus="m")]
[name="玛露西尔"]我在那听到了各种有趣的小故事，那里有个叫“巴斯克星象”的小帐篷，里面的人在占卜......
[name="玛露西尔"]虽然后来我发现她是骗人的啦，那个水晶球就是她自己操控的，但她说的什么“米诺斯传说中一千个头的怪物”还是挺有趣的......
[charslot(slot="m",name="avg_4142_laios_1#6$1",focus="m")]
[name="莱欧斯"]在一个叫“米诺斯”的地方，有长着一千个头的魔物！
[name="莱欧斯"]我之前也听传闻说过有种很厉害的魔物，吃下什么东西就可以获得什么样的能力。
[name="莱欧斯"]真好啊，多梦幻啊......
[charslot(slot="m",name="avg_4141_marcil_1#14$1",focus="m")]
[name="玛露西尔"]你就只对这种话题特别感兴趣。
[charslot(slot="m",name="avg_4141_marcil_1#13$1",focus="m")]
[name="玛露西尔"]我们还是先想想怎么找到雪祀吧，我真的走不动了......
[charslot(slot="m",name="avg_4143_sensi_1#3$1",focus="m")]
[name="森西"]强大的人会适应环境，玛露西尔。
[charslot(slot="m",name="avg_4141_marcil_1#13$1",focus="m")]
[name="玛露西尔"]不用担心，也不需要适应这样的环境，我可不想多来这样的地方。
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]这样思考会阻碍你成长的。
[name="森西"]对老夫而言，比起人为建造的街道，还是这样的地方更好。
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]我也不是说不找雪祀了......
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]而且，那个占卜师说去了黑森林就能找到他们，结果这不是什么都没有吗！
[name="玛露西尔"]这里又潮湿又没有光树木又多魔物还多补给又快吃完了你们肯定又要吃魔物了。
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]莱欧斯，你怎么看？
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]嗯——这片黑森林的魔物和我们之前遇到的并没有太大不同，我还以为能见到一些稀奇的魔物。
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]森林往往掩藏着许多秘密，只是我们还不了解它。
[charslot(slot="m",name="avg_4144_chilc_1#2$1",focus="m")]
[name="齐尔查克"]与其说又要吃了，不如说，那边那两个已经在割刚才打倒的魔物的肉了。太好了，玛露西尔，你又有口福了。
[charslot(slot="m",name="avg_4141_marcil_1#2$1",focus="m")]
[name="玛露西尔"]我不要我不要我不要！！！
[Dialog]
[charslot]
[PlaySound(key="$leaveshake",volume=1)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4141_marcil_1#9$1",focus="m")]
[name="玛露西尔"]怎么又来了！
[name="玛露西尔"]咦？
[Dialog]
[charslot]
[name="？？？"]看来我来晚了。
[Dialog]
[charslot(slot="m",name="avg_4142_laios_1#8$1",focus="m")]
[name="莱欧斯"]你是......？
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]莱欧斯，你能不能不要一只手握着你那沾血的剑用手背擦脸，一只手提着魔物的肉和人打招呼——
[Dialog]
[charslot]
[name="？？？"]啊，没关系的。
[name="？？？"]比这更刺激的场景我也经常见到。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_npc_964_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="橡杯"]你们可以叫我橡杯，我是一名萨满学徒。
[name="橡杯"]有一群羽兽告知了我你们的处境，于是我赶了过来。
[charslot(slot="m",name="avg_npc_964_1#9$1",focus="m")]
[name="橡杯"]不过，就算我不来，你们应该也能处理好。
[charslot(slot="m",name="avg_4142_laios_1#9$1",focus="m")]
[name="莱欧斯"]......
[charslot(slot="m",name="avg_npc_964_1#1$1",focus="m")]
[name="橡杯"]哦，请不用担心，我没有恶意，也不想惹麻烦，既然各位没有事，那我就不打扰——
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]等等，你刚才说，你是萨满学徒？
[charslot(slot="m",name="avg_npc_964_1#1$1",focus="m")]
[name="橡杯"]是的。

... (全文17006字符)
```

### level_act36side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_cave_2",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="m",name="avg_4144_chilc_1#15$1",duration=1.5)]
[Delay(time=2)]
[name="齐尔查克"]嘶——
[Dialog]
[charslot]
[name="？？？"]你醒了。
[charslot(slot="m",name="avg_4144_chilc_1#8$1",focus="m")]
[name="齐尔查克"]你是......？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_969_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_969_1#1$1",focus="m")]
[name="艾尔启"]我的名字是艾尔启。
[name="艾尔启"]我预见到今天在这片森林中会有厄运降临，于是来到这附近徘徊，结果发现了在雪地里昏倒的你。
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]......你有见到我的同伴们吗？
[charslot(slot="m",name="avg_npc_969_1#2$1",focus="m")]
[name="艾尔启"]抱歉。
[charslot(slot="m",name="avg_4144_chilc_1#16$1",focus="m")]
[name="齐尔查克"]......啧，我得去找他们。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m")]
[Blocker(a=0.3, r=0.5, g=0, b=0, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[name="齐尔查克"]嘶——
[charslot(slot="m",name="avg_npc_969_1#2$1",focus="m")]
[name="艾尔启"]你伤得不轻，先在这里休息一下吧。
[charslot(slot="m",name="avg_4144_chilc_1#10$1",focus="m")]
[name="齐尔查克"]......
[charslot(slot="m",name="avg_npc_969_1#1$1",focus="m")]
[name="艾尔启"]你似乎不是萨米人。
[charslot(slot="m",name="avg_4144_chilc_1#10$1",focus="m")]
[name="齐尔查克"]......我和我的伙伴们在寻找回家的线索，有一个叫橡杯的人告诉我们，萨米的意志指引我们往北走。
[charslot(slot="m",name="avg_npc_969_1#1$1",focus="m")]
[name="艾尔启"]橡杯......橡树之子。
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]你认识他？
[charslot(slot="m",name="avg_npc_969_1#3$1",focus="m")]
[name="艾尔启"]我只是有所耳闻，这个名字在萨米与“智慧”同义。
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]“智慧”......？那......你知道独眼巨人吗？
[charslot(slot="m",name="avg_npc_969_1#1$1",focus="m")]
[name="艾尔启"]......
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]......怎么了？
[charslot(slot="m",name="avg_npc_969_1#2$1",focus="m")]
[name="艾尔启"]我见过许多人被厄运缠身，死亡......并不是一件少见的事。
[name="艾尔启"]但是，为什么我在你的身上看到了许多死亡？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="40_g1_blackforest",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4142_laios_1#9$1",focus="m")]
[name="莱欧斯"]还是没找到齐尔查克吗？
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]嗯......
[charslot(slot="m",name="avg_4143_sensi_1#3$1",focus="m")]
[name="森西"]唯一值得庆幸的是，这附近的积雪相当厚，而且树木繁多，以齐尔查克的身手，他应该不会有大问题。
[charslot(slot="m",name="avg_4142_laios_1#9$1",focus="m")]
[name="莱欧斯"]嗯......但是齐尔查克缺乏自保能力，我们还是要尽快找到他。
[name="莱欧斯"]要是让他遇到那头跑走的奇怪角兽那就凶多吉少了。
[charslot(slot="m",name="avg_4143_sensi_1#9$1",focus="m")]
[name="森西"]我知道。而且，我们现在还有一个问题——
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_2013_cerber_1#7$1",duration=1.5)]
[Delay(time=2)]
[name="？？？"]对不起。
[charslot(slot="m",name="avg_4142_laios_1#13$1",focus="m")]
[name="莱欧斯"]唉......这不怪你。
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]不过，小姐，为什么你会一个人在这片森林里？
[charslot(slot="m",name="avg_2013_cerber_1#7$1",focus="m")]
[name="？？？"]因为我在这里打猎......
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]孩子，你生活在这里吗？
[charslot(slot="m",name="avg_2013_cerber_1#1$1",focus="m")]
[name="？？？"]不是哦，我生活在罗德岛！
[charslot(slot="m",name="avg_4141_marcil_1#8$1",focus="m")]
[name="玛露西尔"]罗德岛？！我们正在找罗德岛！
[charslot(slot="m",name="avg_2013_cerber_1#1$1",focus="m")]
[name="？？？"]欸？你们要去罗德岛吗？
[charslot(slot="m",name="avg_4141_marcil_1#17$1",focus="m")]
[name="玛露西尔"]嗯，我们正在找回家的路，据说罗德岛上会有线索。
[charslot(slot="m",name="avg_2013_cerber_1#7$1",focus="m")]
[name="？？？"]你们找不到家了吗？好可怜......
[charslot(slot="m",name="avg_4141_marcil_1#17$1",focus="m")]
[name="玛露西尔"]你可以带我们去找罗德岛吗？
[charslot(slot="m",name="avg_2013_cerber_1#10$1",focus="m")]
[name="？？？"]欸，但是我还不想回去......
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]为什么？
[charslot(slot="m",name="avg_2013_cerber_1#1$1",focus="m")]
[name="？？？"]因为我还没吃够呢！
[charslot(slot="m",name="avg_4142_laios_1#18$1",focus="m")]
[name="莱欧斯"]没有吃够？
[name="莱欧斯"]如果我们让你吃饱的话，你愿意带我们去罗德岛吗？
[charslot(slot="m",name="avg_2013_cerber_1#1$1",focus="m")]
[name="？？？"]嗯，可以哦！
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]......没想到，真的在这种地方找到了线索。
[charslot(slot="m",name="avg_4141_marcil_1#5$1",focus="m")]
[name="玛露西尔"]难道说，其实这就是萨米的指引？
[charslot(slot="m",name="avg_2013_cerber_1#8$1",focus="m")]
[name="？？？"]不过......
[name="？？？"]我还没找到这次的猎物呢。
[Dialog]
[PlaySound(key="$d_avg_hungry",volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]我们有食物——啊。
[charslot(slot="m",name="avg_4142_laios_1#13$1",focus="m")]
[name="莱欧斯"]看来我们的食物也在刚才丢失了。
[charslot(slot="m",name="avg_4142_laios_1#18$1",focus="m")]
[name="莱欧斯"]......你看这样可以吗？
[name="莱欧斯"]你先帮我们找到我们的同伴，然后，我们一起帮你狩猎你想要的猎物，最后，你带我们去罗德岛。
[charslot(slot="m",name="avg_2013_cerber_1#1$1",focus="m")]
[name="？？？"]嗯！好哦！
[charslot(slot="m",name="avg_4143_sensi_1#12$1",focus="m")]
[name="森西"]真是个纯真的孩子。你叫什么名字？
[charslot(slot="m",name="avg_2013_cerber_1#1$1",focus="m")]
[name="刻俄柏"]我是刻俄柏，你们可以叫我小刻！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_cave_2",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m"

... (全文20197字符)
```

### level_act36side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_plankroad",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$epic_intro", key="$epic_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="m",name="avg_4144_chilc_1#11$1",duration=1.5)]
[Delay(time=2)]
[name="齐尔查克"]五、四、三、二、一......
[Dialog]
[charslot]
[PlaySound(key="$bigbell",volume=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4144_chilc_1#5$1",focus="m")]
[name="齐尔查克"]好！钟声响了，开始吧！
[charslot(slot="m",name="avg_npc_143#1")]
[name="墨魉"]嘎！
[charslot(slot="m",name="avg_4144_chilc_1#5$1",focus="m")]
[name="齐尔查克"]玛露西尔，左边！
[charslot(slot="m",name="avg_4141_marcil_1#4$1",focus="m")]
[name="玛露西尔"]嘿！
[Dialog]
[charslot(slot="m",name="avg_npc_143#1")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot(duration=0.5)]
[delay(time=1)]
[charslot(slot="m",name="avg_4144_chilc_1#5$1",focus="m")]
[name="齐尔查克"]莱欧斯，前边！右边！
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_143#1",duration=1.5)]
[charslot(slot="r",name="avg_npc_143#1",duration=1.5)]
[delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_4142_laios_1#3$1",focus="m")]
[name="莱欧斯"]嘿！哈！
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_143#1")]
[charslot(slot="r",name="avg_npc_143#1")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0,fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot(duration=0.5)]
[delay(time=1)]
[charslot(slot="m",name="avg_4144_chilc_1#5$1",focus="m")]
[name="齐尔查克"]森西，身后！左边！前面！
[charslot(slot="m",name="avg_4143_sensi_1#8$1",focus="m")]
[name="森西"]嚯！嚯呀——
[Dialog]
[charslot]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot(slot="m",name="avg_4144_chilc_1#5$1",focus="m")]
[name="齐尔查克"]前后前右左左后！
[charslot(slot="m",name="avg_4141_marcil_1#4$1",focus="m")]
[name="玛露西尔"]呀————
[Dialog]
[charslot]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$e_atk_magic_n", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[charslot]
[charslot(slot="m",name="avg_4144_chilc_1#5$1",focus="m")]
[name="齐尔查克"]前后左前右左后！
[charslot(slot="m",name="avg_4141_marcil_1#4$1",focus="m")]
[name="玛露西尔"]呀——！！
[Dialog]
[charslot]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_windmagic", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[charslot]
[Background(image="bg_plankroad",screenadapt="showall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]呼、呼......这附近的墨魉都被处理完了......
[Dialog]
[charslot]
[stopmusic(fadetime=1.5)]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_npc_139#2",duration=1)]
[Delay(time=2)]
[name="黎"]辛苦了。
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[charslot(slot="m",name="avg_4141_marcil_1#17$1",focus="m")]
[name="玛露西尔"]不会！镇里人愿意收留我们，我们帮忙解决一些麻烦也是应该的。
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]老夫还要去田里帮忙种菜，先走一步。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]森西这家伙，已经完全和镇里人混熟了嘛。
[charslot(slot="m",name="avg_npc_139#2",focus="m")]
[name="黎"]齐尔查克小哥不也是，张伯刚才还让我喊你收拾完墨魉就过去喝酒呢。
[charslot(slot="m",name="avg_4144_chilc_1#2$1",focus="m")]
[name="齐尔查克"]那老伯也太不服输了，喝不过我还非要挑战我......
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4141_marcil_1#17$1",focus="m")]
[name="玛露西尔"]黎小姐，我今天能去你那里喝茶吗？
[charslot(slot="m",name="avg_npc_139#2",focus="m")]
[name="黎"]玛露西尔妹妹有空，我自然是有空的。
[name="黎"]今天轮到玛露西尔妹妹讲你的冒险故事了，我可是期待得紧。
[name="黎"]不过......我还记得，你们刚到这里时，说过自己还要去拯救莱欧斯小哥的妹妹。
[name="黎"]还不出发没关系吗？
[charslot(slot="m",name="avg_4141_marcil_1#17$1",focus="m")]
[name="玛露西尔"]......嗯，救法琳是我们的目的。
[name="玛露西尔"]但是——
[charslot(slot="m",name="avg_4141_marcil_1#18$1",focus="m")]
[name="玛露西尔"]要找到离开的方法毕竟急不得。
[charslot(slot="m",name="avg_4141_marcil_1#17$1",focus="m")]
[name="玛露西尔"]而且，在这里的生活也很好......
[name="玛露西尔"]到时候再说吧，你说对吧，莱欧斯？
[charslot(slot="m",name="avg_4142_laios_1#8$1",focus="m")]
[name="莱欧斯"]嗯？什么？
[charslot(slot="m",name="avg_4141_marcil_1#13$1",focus="m")]
[name="玛露西尔"]你又不听我说话！
[charslot(slot="m",name="avg_npc_139#2",focus="m")]
[name="黎"]......呵呵，莱欧斯小哥对墨魉的热情如今在镇里也已经是无人不知了。
[charslot(slot="m",name="avg_4142_laios_1#16$1",focus="m")]
[name="莱欧斯"]但是这种叫墨魉的史莱姆真的很有趣。
[charslot(slot="m",name="avg_4142_laios_1#18$1",focus="m")]
[name="莱欧斯"]它们有自己固定的形状，能明显看出头身和四肢的区别，攻击方式不是包裹敌人的头部，更像是野兽攻击人的方式，而且还会叫！
[name="莱欧斯"]最特殊

... (全文15270字符)
```

### level_act36side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_indoor",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="l",name="avg_npc_139#2",duration=1.5)]
[charslot(slot="r",name="avg_4141_marcil_1#17$1",duration=1.5)]
[Delay(time=2)]	
[charslot(slot="r",name="avg_4141_marcil_1#17$1",focus="r")]
[name="玛露西尔"]我跟着法琳走进了那座山洞。
[name="玛露西尔"]在那里，我才知道，她的秘诀究竟是什么......
[name="玛露西尔"]而且，她还告诉了我所谓的“生态”是什么，在那一刻，我才第一次知道自己原来是那么地缺乏实践。
[charslot(slot="r",name="avg_4141_marcil_1#18$1",focus="r")]
[name="玛露西尔"]也是在那一天，我和法琳成了好朋友。
[charslot(slot="l",name="avg_npc_139#2",focus="l")]
[name="黎"]人生得一知己，夫复何求？
[name="黎"]这位法琳妹妹，对你来说一定很重要吧。
[charslot(slot="r",name="avg_4141_marcil_1#19$1",focus="r")]
[name="玛露西尔"]嗯，她是我最好的朋友。
[charslot(slot="l",name="avg_npc_139#2",focus="l")]
[name="黎"]那么，你不应该去找她吗？
[name="黎"]我记得你说过，她被炎龙吃掉了，但是，你们有办法复活她。
[charslot(slot="r",name="avg_4141_marcil_1#11$1",focus="r")]
[name="玛露西尔"]炎龙......炎龙......
[charslot(slot="r",name="avg_4141_marcil_1#17$1",focus="r")]
[name="玛露西尔"]我们会去的，到时候，我会把她带来婆山镇见一见你！
[charslot(slot="l",name="avg_npc_139#2",focus="l")]
[name="黎"]也好。
[Dialog]
[charslot(slot="l",name="avg_npc_139#2",focus="none")]
[PlaySound(key="$bigbell",volume=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_139#3",focus="l")]
[name="黎"]咦，今天来得似乎有些频繁了。
[charslot(slot="r",name="avg_4141_marcil_1#13$1",focus="r")]
[name="玛露西尔"]......该不会是莱欧斯那家伙捅了什么娄子吧！
[name="玛露西尔"]我去看看！
[Dialog]
[PlaySound(key="$rungeneral",volume=1)]
[charslot(slot="r",posfrom="0,0",posto="100,0",duration=2)]
[charslot(slot="r",afrom=1,ato=0,duration=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_139#3",focus="l")]
[name="黎"]......
[charslot(slot="l",name="avg_npc_139#2",focus="l")]
[name="黎"]唉，我能做的......也只有这么多了。
[name="黎"]莱欧斯小哥，看来你的伙伴们，只能靠你了。
[Dialog]
[Delay(time=2.5)]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="r",name="avg_4141_marcil_1#1$1",posfrom="100,0",posto="0,0",duration=2)]
[charslot(slot="r",afrom=0,ato=1,duration=0.5)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_139#3",focus="l")]
[name="黎"]怎么了，玛露西尔妹妹？
[charslot(slot="r",name="avg_4141_marcil_1#1$1",focus="r")]
[name="玛露西尔"]怪了，明明钟声响了，但是，却没有墨魉来袭击镇子。
[name="玛露西尔"]莱欧斯也没有回来......
[charslot(slot="l",name="avg_npc_139#3",focus="l")]
[name="黎"]......欸？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[charslot]
[Background(image="bg_plankroad",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$rungeneral",volume=1)]
[charslot(slot="m",name="avg_4142_laios_1#18$1",posfrom="-100,0",posto="0,0",duration=2)]
[charslot(slot="m",afrom=0,ato=1,duration=1)]
[Delay(time=2)]
[name="莱欧斯"]哼哼，喜欢吃杏子的话，那就跑起来！
[name="莱欧斯"]嘿！
[Dialog]
[charslot]
莱欧斯说着，把采来的一把杏子往远处一丢，只见一群大大小小的兽形墨魉都向着杏子跑去。
看着它们抢杏子的光景，莱欧斯开心极了，他几乎要把这群家伙当成自己家里养的狗了。
对，简直就和奴莎、亚诺特里德、波夫、福奇、抹布和木木一样！
[Dialog]
[charslot(slot="m",name="avg_npc_143#1",duration=1)]
[Delay(time=1.5)]
[name="呆呆的墨魉"]嘎——
[charslot(slot="m",name="avg_4142_laios_1#18$1",focus="m")]
[name="莱欧斯"]别急，你们的份也少不了！
[Dialog]
[charslot]
对于这种有点像树懒的墨魉，莱欧斯自然不会选择让它们争抢。
他已经摸清楚了这种墨魉的喜好，特意摘了一堆水果，堆在那里让它们放肆地吃。
它们吃饱了就会躺下，背上的颜色也会变......
看着它们挺着圆滚滚的肚子还要奋力往嘴里塞果子的样子，莱欧斯很好奇，真的会有人不喜欢这群小家伙吗？
[Dialog]
[charslot(slot="m",name="avg_npc_1425_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="悠哉的墨魉"]啊——
[charslot(slot="m",name="avg_4142_laios_1#19$1",focus="m")]
[name="莱欧斯"]放心，我怎么会忘了你们呢？
[Dialog]
[charslot]
乌龟一样的墨魉可以说是莱欧斯现在最好奇的墨魉了，一开始，他还以为它们是一大块石头，直到自己一屁股坐了上去。
这种墨魉的性子和乌龟如出一辙，而最有趣的是，如果你让它们吃饱了，它们背上的假山会流下泉水——！
[Dialog]
[PlaySound(key="$d_gen_thunders_amb",volume=0.5)]
[Delay(time=2.5)]
远处雷声隆隆。
墨魉们听到雷声，纷纷想要站起来。
可是，它们发现自己站不起来......原因很简单——
它们吃得太撑了！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[charslot]
[Background(image="bg_landscape",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]看来今年的收成会很不错。
[charslot(slot="m",name="avg_npc_140",focus="m")]
[name="镇民"]多亏了你啊，森西老爷子。
[name="镇民"]要是没有你，我看这收成至少得少一半！
[charslot(slot="m",name="avg_4143_sensi_1#3$1",focus="m")]
[name="森西"]老夫也只是把自己知道的知识运用起来罢了。
[Dialog]
[charslot]
[PlaySound(key="$rungeneral",volume=1)]
[charslot(slot="m",name="avg_4141_marcil_1#9$1",duration=1.5)]
[Delay(time=2)]
[name="玛露西尔"]森西，别种田了！
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]玛露西尔，怎么了？
[charslot(slot="m",name="avg_4141_marcil_1#9$1",focus="m")]
[name="玛露西尔"]莱欧斯自从上次跑去镇子外面找墨魉后，好几天没回来了！
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]莱欧斯？他喜欢研究，就让他去吧。
[charslot(slot="m",name="avg_4141_marcil_1#9$1",focus="m")]
[name="玛露西尔"]而且，最近墨魉都没有来攻击镇子了——
[name="玛露西尔"]他会不会出事了？！
[charslot(slot="m",name="avg_4143_sensi_1#9$1",focus="m")]
[name="森西"]唔......反正我们要在这里待很久，不妨再等一等。
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]......
[name="玛露西尔"]不，不对......我们不能在这里待很久！
[stopmusic(fadetime=1.5)]
[name="玛露西尔"]我们要一起去打败炎龙、救出法琳的啊，你忘了吗？！
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]......嗯？
[name="森西"]......
[charslot(slot="m",name="avg_4143_sensi_1#3$1",focus="m")]
[name="森西"]玛露西尔，说到这里，我们在这座镇子里待多久了？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_plankroad",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[name="墨魉们"]嘎——！
[charslot(slot=

... (全文33454字符)
```

### level_act36side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibcave",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
猎人坠落的样子仿佛——
——流星。
身在深海中的人甚少看见这种奇景。
那沉迷欲望和阴谋、从不抬头仰望的主教，更不可能知晓这等景色。
但他们不一样。
当深海猎人们拼命向上游去，想从阴郁与牺牲中挣脱时，当他们跻身海面，静静欣赏无边星空时......
猎人们都在心中记录了这些短命星辰的命运。
即使如此，也会划破黑暗。
[Dialog]
[charslot(slot="m",name="char_263_skadi#8",duration=1.5)]
[Delay(time=2)]	
[name="斯卡蒂"]现在，死吧。
[Dialog]
[charslot]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_chixiaobadao")]
[Blocker(a=0,r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1,r=1, g=1, b=1, fadetime=0.01, block=true)]
[Blocker(a=0,r=0, g=0, b=0, fadetime=0.09, block=true)]
[Blocker(a=1,r=1, g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0,r=0, g=0, b=0, fadetime=1, block=true)]
三颗流星照亮了幽邃的通道。
主教恐惧万分，他没有肺，没有声道，这鸣响只是他的新身体用以替代惨叫的新方式。
残垣断壁里，怪物将死的臃肿肉体填塞了大半个溶洞。它原本不断散发出奇异之美的古怪躯体因它对死亡的畏惧而愈显僵硬。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[charslot]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[Subtitle(text="主教死去了。他的一切都将被遗忘。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Delay(time=2)]	
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[charslot]
[Background(image="32_RL2_cliffday",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_4142_laios_1#9$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4142_laios_1#9$1",focus="m")]
[name="莱欧斯"]情况不太妙啊。
[name="莱欧斯"]这个城市周围没有丝毫活物的气息......
[charslot(slot="m",name="avg_4142_laios_1#14$1",focus="m")]
[name="莱欧斯"]看起来在这里很难筹集到像样的补给。
[name="莱欧斯"]各位，有什么发现吗？
[charslot(slot="m",name="avg_4144_chilc_1#11$1",focus="m")]
[name="齐尔查克"]......没什么变化，这座城里其他地方也都是一句话都不会说的家伙。
[name="齐尔查克"]他们看到食物倒是会有反应，但还是不会回答我的问题。
[name="齐尔查克"]至于补给，别说让他们分我们一些了，我甚至把身上仅剩的口粮分了一点给他们。
[charslot(slot="m",name="avg_4142_laios_1#14$1",focus="m")]
[name="莱欧斯"]我也是，这座城市的大部分民居只能用凄凉来形容......
[name="莱欧斯"]真难以想象，这里的人能在这种环境下生存。
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]老夫找遍了好几个市场，看起来都很久没营业了。
[name="森西"]也就是说这里的大部分人已经很久没有好好吃过东西了。
[charslot(slot="m",name="avg_4143_sensi_1#7$1",focus="m")]
[name="森西"]老夫看在眼里实在是心痛。
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]嗯......
[name="玛露西尔"]我跟着一个人一路来到海边，本来以为能发现什么，结果——
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_187",duration=1.5)]
[charslot(slot="r",name="avg_npc_189",duration=1.5)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_187",focus="l")]
[name="居民A"]嗬......嗬......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]他就这样和其他人一样，漫无目的地在海边游荡，有的时候挖一挖沙，好像沙滩上会有吃的长出来一样......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_187",focus="r")]
[charslot(slot="r",name="avg_npc_189",focus="r")]
[name="居民B"]饿......
[charslot(slot="l",name="avg_npc_187",focus="l")]
[name="居民A"]鳞、壳，可以吃。
[name="居民A"]吃吧，吃吧。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]......
[Dialog]
[charslot]
森西放下了手中的斧子，快步走到两人的面前，伸手打开了他们的包裹。
里面堆放着刚从沙滩上捡拾来的鳞和壳，而且都已经轻微腐烂，发出难以忍受的腥臭味。
可两人浑然不觉，生怕森西抢他们的，赶紧就往嘴里塞。
[charslot(slot="m",name="avg_4143_sensi_1#5$1",focus="m")]
[name="森西"]唔，这实在是......
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m")]
[name="齐尔查克"]这也太凄惨了......
[name="齐尔查克"]既然这里没什么能帮我们的东西，我们还是尽快离开这里吧。
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]这里的民风民俗实在是太奇怪了，人们感觉也不太友善的样子......
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]......
[charslot(slot="m",name="avg_4143_sensi_1#3$1",focus="m")]
[name="森西"]这是老夫的猜测。
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]这里的人很可能是长时间没有吃过正常的食物，导致他们对周围的一切都逐渐麻木。
[name="森西"]如果这时候让他们吃到一顿美食，或许可以让他们恢复一点知觉。
[charslot(slot="m",name="avg_4144_chilc_1#16$1",focus="m")]
[name="齐尔查克"]真的假的......
[charslot(slot="m",name="avg_4143_sensi_1#3$1",focus="m")]
[name="森西"]嗯，你不清楚也不奇怪，长时间的食物匮乏，还有生活环境的压缩，是会让人一点一点麻木的。
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]你听起来很有经验。
[charslot(slot="m",name="avg_4143_sensi_1#7$1",focus="m")]
[name="森西"]......
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]如果可以的话，老夫也希望让这里的人吃上一顿饱饭。
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]......不管怎么说，我们也要为自己找食物，不然的话，我们也走不了多远，对吧，齐尔查克。
[charslot(slot="m",name="avg_4144_chilc_1#10$1",focus="m")]
[name="齐尔查克"]......唉，说得也是。
[charslot(slot="m",name="avg_4144_chilc_1#5$1",focus="m")]
[name="齐尔查克"]不过，事先说好，补给丢了是你们在萨米乱跑搞出来的事情，所以别指望靠我！
[charslot(slot="m",name="avg_4142_laios_1#18$1",focus="m")]
[name="莱欧斯"]那当然。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_npc_454_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_454_1#1$1",focus="m")]
[name="？？？"]游荡的旅行者，你们是否在寻找食物？
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]咦，你听得懂我们的话吗？
[charslot(slot="m",name="avg_npc_454_1#1$1",focus="m")]
[name="？？？"]是的。
[charslot(slot="m",name="avg_4141_marcil_1#17$1",focus="m")]
[name="玛露西尔"]太好了！我们——
[charslot(slot="m",name="avg_4144_chilc_1#11$1",focus="m")]
[name="齐尔查克"]等等，玛露西尔，其他人都听不懂我们说话，他却听得懂，你不觉得奇怪吗？
[charslot(slot="m",name="avg_npc_454_1#1$1",focus="m")]
[name="？？？"]......你们会有所警惕也很正常。
[name="？？？"]但是，不用担心，我是为了给你们提供指引而来。
[charslot(slot="m",name="avg_4144_chilc_1#11$1",focus="m")]
[name="齐尔查克"]你到底是谁？
[charslot(slot="m",name="avg_npc_454_1#1$1",focus="m"

... (全文14928字符)
```

### level_act36side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="32_RL2_cliffday",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_npc_454_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="教士"]哦？这个声音......
[name="教士"]我以为他们会更加谨慎一些......没想到，他们自信到如此地步？
[name="教士"]呵呵，无论如何，结果是一样的。
[name="教士"]教会正是需要人手的时候。
[name="教士"]成为我们的一员吧。
[name="教士"]然后，让我们共同为伊比利亚人带去启示。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(duration=1.5)]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="32_RL2_cliffday",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]陷阱大概就这样吧。
[name="齐尔查克"]剩下就等他们打够食材跑出来了，应该足够帮他们抵挡一下子。
[name="齐尔查克"]......
[charslot(slot="m",name="avg_4144_chilc_1#3$1",focus="m")]
[name="齐尔查克"]唉，莱欧斯这家伙，有些时候还是挺细致的。
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]嗯？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1426_1#1$2",duration=1.5)]
[Delay(time=2)]	
[name="箱子"]......
[charslot(slot="m",name="avg_4144_chilc_1#8$1",focus="m")]
[name="齐尔查克"]这里怎么会有个箱子？
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m")]
[name="齐尔查克"]......难道说，在这个世界也有宝箱怪？
[charslot(slot="m",name="avg_npc_1426_1#1$2",focus="m")]
[name="箱子"]......
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m")]
[name="齐尔查克"]呃，这家伙未免也太不专业了。
[name="齐尔查克"]在沙滩这么空无一物的地方，真的能骗到人吗？
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="none")]
[Delay(time=2)]
[charslot(slot="m",name="avg_4144_chilc_1#11$1",focus="m")]
[name="齐尔查克"]咦......？有脚步声......我猜，是那个神神道道的家伙。
[Dialog]
[charslot(slot="m",posfrom="0,0",posto="100,0",duration=1.5)]
[charslot(slot="m",afrom=1,ato=0,duration=0.5)]
[Delay(time=2)]
[charslot]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_npc_454_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="教士"]他们终会变成我们的兄弟手足，很快，很快，他们会变得更好......
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(duration=1.5)]
[Delay(time=4.5)]
[charslot]
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="m",name="avg_4144_chilc_1#11$1",posfrom="100,0",posto="0,0",duration=1.5)]
[charslot(slot="m",afrom=0,ato=1,duration=0.5)]
[Delay(time=2)]
[name="齐尔查克"]嘁，这家伙......果然想让我们去送死吗。
[charslot(slot="m",name="avg_4144_chilc_1#12$1",focus="m")]
[name="齐尔查克"]......有了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="32_RL2_cliffday",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_npc_454_1#1$1",focus="m")]
[name="教士"]等审判庭的人来了，正好拿他们试一试。
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]试什么？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_4144_chilc_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_454_1#1$1",focus="r")]
[name="教士"]你......你怎么没有进去？
[charslot(slot="l",name="avg_4144_chilc_1#1$1",focus="l")]
[name="齐尔查克"]我本来就没什么战斗能力，所以在等他们出来。
[charslot(slot="r",name="avg_npc_454_1#1$1",focus="r")]
[name="教士"]......是吗。
[charslot(slot="l",name="avg_4144_chilc_1#6$1",focus="l")]
[name="齐尔查克"]你刚才提到审判庭，那是什么？
[charslot(slot="r",name="avg_npc_454_1#1$1",focus="r")]
[name="教士"]......那是我们共同的敌人。
[charslot(slot="l",name="avg_4144_chilc_1#1$1",focus="l")]
[name="齐尔查克"]可以说给我听听吗？
[charslot(slot="r",name="avg_npc_454_1#1$1",focus="r")]
[name="教士"]（这个杜林看起来确实没什么战斗力......和他聊聊也没什么。）
[name="教士"]（就他这身板，他还能跑到哪里去呢？）
[name="教士"]当然。
[charslot(slot="l",name="avg_4144_chilc_1#1$1",focus="l")]
[name="齐尔查克"]这里好像会被人看到......我们去那边那个箱子上聊吧。
[charslot(slot="r",name="avg_npc_454_1#1$1",focus="r")]
[name="教士"]好的。
[charslot(slot="l",name="avg_4144_chilc_1#11$1",focus="l")]
[name="齐尔查克"]......
[Dialog]
[stopmusic(fadetime=1.5)]
[charslot(slot="r",posfrom="0,0",posto="200,0",duration=2)]
[charslot(slot="l",posfrom="0,0",posto="200,0",duration=2)]
[charslot(slot="r",afrom=1,ato=0,duration=1.5)]
[Delay(time=2)]
[charslot]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1426_1#1$2")]
[charslot(slot="l",name="avg_npc_454_1#1$1",posfrom="-200,0",posto="0,0",duration=1.5)]
[charslot(slot="l",afrom=0,ato=1,duration=0.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1426_1#1$2",focus="m")]
[name="箱子？"]......
[charslot(slot="l",name="avg_npc_454_1#1$1",focus="l")]
[name="教士"]那么，我们就从审判庭对伊比利亚的欺瞒开始——咦？
[Dialog]
[charslot(slot="m",name="avg_npc_1426_1#1$1",focus="m")]
[PlaySound(key="$d_avg_monsteroar",volume=1)]
[CameraShake(duration=0.5 ,xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=2.5)]
[name="？？？"]（猛地打开）（吞食）（关闭）（欢快地晃动）
[Dialog]
[charslot]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$d_gen_walk_n",volume=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[charslot(slot="m",name="avg_4144_chilc_1#2$1",duration=1.5)]
[Delay(time=2)]
[name="齐尔查克"]......嘴上说着兄弟，结果你对这些魔物也不怎么了解嘛。
[name="齐尔查克"]在我们这一行，这样是会吃亏的。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_ibcave",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]呼，总算全都干掉了！
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]本来以为会有很多......
[charslot(slot="m",name="avg_4142_laios_1#16$1",focus="m"

... (全文20503字符)
```

### level_act36side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="27_g26_dusk_wild",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot="m",name="avg_4141_marcil_1#7$1",duration=1.5)]
[Delay(time=2)]
[name="玛露西尔"]怎么回事？为什么这里的魔法器具追着我们打？我们被谁盯上了？
[Dialog]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n",channel="1")]
[PlaySound(key="$rungeneral", volume=1,channel="2")]
[charslot(slot="m",posfrom="0,0",posto="-200,0",duration=1.5)]
[charslot(slot="m",afrom=1,ato=0,duration=0.5)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot]
[Delay(time=1)]
[charslot(slot="m",name="avg_4142_laios_1#3$1",focus="m")]
[name="莱欧斯"]剑够不到它们，和之前对魔物的战斗都不一样！
[charslot(slot="m",name="avg_4144_chilc_1#7$1",focus="m")]
[name="齐尔查克"]玛露西尔！你用魔法啊！
[charslot(slot="m",name="avg_4141_marcil_1#6$1",focus="m")]
[name="玛露西尔"]我被炸到了......！
[name="玛露西尔"]咳咳咳！能施展爆炸魔法和冰冻魔法，还能这么精准地定位，这种魔法器具非常高级......
[name="玛露西尔"]它们动作太快了，很难瞄准......！
[charslot(slot="m",name="avg_4144_chilc_1#7$1",focus="m")]
[name="齐尔查克"]那怎么办！
[charslot(slot="m",name="avg_4141_marcil_1#6$1",focus="m")]
[name="玛露西尔"]......先跑！它们施魔法我就用魔法对冲！看看能不能跑出它们的攻击范围！
[Dialog]
[PlaySound(key="$rungeneral", volume=1,channel="2")]
[charslot(slot="m",posfrom="0,0",posto="-200,0",duration=1.5)]
[charslot(slot="m",afrom=1,ato=0,duration=0.5)]
[Delay(time=2)]	
[charslot]
[PlaySound(key="$d_avg_drone", volume=1,channel="2")]
[charslot(slot="m",name="avg_npc_1420_1#1$1",posfrom="200,150",posto="0,0",duration=1.5)]
[charslot(slot="l",name="avg_npc_1428_1#1$1",posfrom="200,0",posto="0,150",duration=1.5)]
[charslot(slot="r",name="avg_npc_1428_1#1$1",posfrom="200,-100",posto="0,-150",duration=1.5)]
[charslot(slot="m",afrom=0,ato=1,duration=0.5)]
[charslot(slot="l",afrom=0,ato=1,duration=0.5)]
[charslot(slot="r",afrom=0,ato=1,duration=0.5)]
[Delay(time=2)]	
[PlaySound(key="$d_avg_drone", volume=1,channel="2")]
[charslot(slot="m",posfrom="0,0",posto="-200,0",duration=1.5)]
[charslot(slot="l",posfrom="0,150",posto="-200,150",duration=1.5)]
[charslot(slot="r",posfrom="0,-150",posto="-200,-150",duration=1.5)]
[charslot(slot="m",afrom=1,ato=0,duration=0.5)]
[charslot(slot="l",afrom=1,ato=0,duration=0.5)]
[charslot(slot="r",afrom=1,ato=0,duration=0.5)]
[Delay(time=1.5)]
[charslot]
[Delay(time=1)]
[charslot(slot="m",name="avg_4142_laios_1#7$1",focus="m")]
[name="莱欧斯"]——那边好像有村庄！这些东西也都是从那里飞出来的，这次遇到的人对我们很不友好啊......
[charslot(slot="m",name="avg_4142_laios_1#3$1",focus="m")]
[name="莱欧斯"]玛露西尔！小心！
[Dialog]
[charslot(slot="m",name="avg_4141_marcil_1#13$1",focus="m")]
[name="玛露西尔"]呃——我看到它们的轨迹了！
[charslot(slot="m",name="avg_4141_marcil_1#20$1",focus="m")]
[name="玛露西尔"]给我......回去！
[Dialog]
[charslot]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_windmagic")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
炸弹被玛露西尔施展的魔法击飞，向着发射出它的无人机处飞去。
[Dialog]
[charslot(slot="m",name="avg_npc_1420_1#1$1",focus="m")]
[Delay(time=0.5)]	
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[charslot(slot="m",posfrom="0,0",posto="0,-50",duration=1.5)]
[charslot(slot="m",afrom=1,ato=0,duration=0.5)]
[Delay(time=1.5)]
[charslot]
无人机被炸弹击中，摇摇晃晃地掉落。
[Dialog]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$a_bat_buildingshaking_1")]
[Delay(time=1.5)]
一声巨大的炸响，建筑冒出火光，随即响起的是村庄中人们大呼小叫的声音。魔法器具随着刚刚的爆炸，更加狂乱地冲向几人。
玛露西尔不禁握紧了手中的法杖。
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]莱欧斯，我们现在好像真的惹怒他们了！
[charslot(slot="m",name="avg_4142_laios_1#9$1",focus="m")]
[name="莱欧斯"

... (全文17186字符)
```

### level_act36side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="27_g26_dusk_wild",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4142_laios_1#7$1",duration=1.5)]
[Delay(time=2)]
[name="莱欧斯"]打、打完了？都解决掉了？
[charslot(slot="m",name="avg_4141_marcil_1#9$1",focus="m")]
[name="玛露西尔"]哈......哈......累死我了......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_534_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_534_1#1$1",focus="l")]
[name="拓荒者A"]哈哈哈！不错啊小丫头，你那几招真有点意思，老子果然最喜欢术师了！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_090",focus="m")]
[name="瑞恩"]哎呀呀......还好大家没打起来，人都没事就好，人都没事就好......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_534_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_534_1#1$1",focus="l")]
[name="拓荒者A"]走，老子今天心情好！带你们去吃老子自己种的玉米！
[charslot(slot="r",name="avg_npc_534_1#1$1",focus="r")]
[name="拓荒者B"]大哥，你......
[charslot(slot="l",name="avg_npc_534_1#1$1",focus="l")]
[name="拓荒者A"]嗯？......玉米？
[Dialog]
[charslot]
刚还在哈哈大笑的拓荒者一骨碌爬了起来，举起武器，对准小队四人。
[charslot(slot="m",name="avg_4144_chilc_1#5$1",focus="m")]
[name="齐尔查克"]呼......呼......看来他这是回过神来了，我刚才真的以为他要和我们握手言和呢。
[Dialog]
[charslot]
玛露西尔也抬起法杖，头发随着魔法微微地荡漾起来。
[charslot(slot="m",name="avg_npc_090",focus="m")]
[name="瑞恩"]哎？哎？几位这又是怎么回事？怎么又闹起来了？刚还同生共死呢，你们不是和好了吗？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_534_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_534_1#1$1",focus="l")]
[name="拓荒者A"]......哼！
[Dialog]
[charslot]
[charslot(slot="l",name="avg_4144_chilc_1#15$1",focus="all")]
[charslot(slot="r",name="avg_4143_sensi_1#15$1",focus="all")]
[name="齐尔查克&森西"]呼......呼......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4142_laios_1#7$1",focus="m")]
[name="莱欧斯"]玛露西尔，你先别施展魔法。
[name="莱欧斯"]......这样吧，大家刚处理完这些东西，都很累了，再打下去没什么好处。
[name="莱欧斯"]我们数三声，都放下武器，各自退回原来的地方，承诺今晚互不打扰，怎么样？
[Dialog]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[charslot(duration=0.5)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_4144_chilc_1#7$1",focus="all")]
[charslot(slot="r",name="avg_4143_sensi_1#4$1",focus="all")]
[Delay(time=2)]
[charslot]
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="m",name="avg_4142_laios_1#7$1",bstart=0.5,bend=1,duration=1.5)]
[Delay(time=2)]
[name="莱欧斯"]咳咳咳咳！！怎......么......样......？
[charslot(slot="m",name="avg_npc_090",focus="m")]
[name="瑞恩"]看看这位大哥多有诚意啊，都这样了还在坚持！几位看呢？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_534_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_534_1#1$1",focus="r")]
[name="拓荒者B"]大哥，咱们的人也累惨了，再打下去没好处啊......
[charslot(slot="l",name="avg_npc_534_1#1$1",focus="l")]
[name="拓荒者A"]......行，三个数，今晚互不打扰。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_090",focus="m")]
[name="瑞恩"]哎！真好！
[charslot(slot="m",name="avg_4142_laios_1#7$1",bstart=0.5,bend=1,focus="m")]
[name="莱欧斯"]三、二、一！
[Dialog]
[playsound(key="$runsand")]
[charslot(duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_090",focus="m")]
[name="瑞恩"]真好......晚上可以睡个安稳觉了......
[Dialog]
[stopmusic(fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_coldforest",screenadapt="showall")]
[Delay(time=2)]
[playMusic(intro="$holiday_intro", key="$holiday_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[name="玛露西尔"]Zzz......
[charslot(slot="m",name="avg_4142_laios_1#7$1",focus="m")]
[name="莱欧斯"]玛露西尔？玛露西尔？
[Dialog]
[charslot]
[name="玛露西尔"]Zzz......嗯？......
[Dialog]
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="m",name="avg_4141_marcil_1#4$1",posfrom="0,-20",posto="0,0",afrom=0,ato=1,duration=1)]
[Delay(time=2)]
[name="玛露西尔"]啊！发、发生什么事了？！
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]没有，玛露西尔。
[charslot(slot="m",name="avg_4142_laios_1#10$1",focus="m")]
[name="莱欧斯"]我们想去看看刚才那些魔物的构造，顺便......
[charslot(slot="m",name="avg_4141_marcil_1#22$1",focus="m")]
[name="玛露西尔"]......啊？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_coldforest",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]老夫觉得那些东西很像螃蟹，吃起来或许就是宝箱怪的味道。
[charslot(slot="m",name="avg_4142_laios_1#12$1",focus="m")]
[name="莱欧斯"]啊啊，宝箱怪很有嚼头的，而且越嚼越好吃......
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m")]
[name="齐尔查克"]只要你们别再用我的开锁工具去掏肉吃就好。
[charslot(slot="m",name="avg_4142_laios_1#8$1",focus="m")]
[name="莱欧斯"]可是那个真的很好用！
[charslot(slot="m",name="avg_4141_marcil_1#22$1",focus="m")]
[name="玛露西尔"]......
[charslot(slot="m",name="avg_4142_laios_1#18$1",focus="m")]
[name="莱欧斯"]《鲍勃的美食指南》上写了这种东西是可以吃的，味道很鲜美，就是破开外壳有些麻烦！你不想尝尝吗？
[charslot(slot="m",name="avg_4141_marcil_1#2$1",focus="m")]
[name="玛露西尔"]不想！而且被误会成是返回战场准备偷袭的话，说不定还要再打一场！
[multiline(name="玛露西尔")]那些满天乱飞的魔法器具很烦人，那边现在还有不少！我也很累——
[charslot(slot="m",name="avg_4141_marcil_1#22$1",focus="m")]
[multiline(name="玛露西尔",end=true)]欸？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_534_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_534_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_534_1#1$1",focus="l")]
[name="拓荒者A"]吧唧吧唧吧唧......欸？
[charslot(slot="r",name="avg_npc_534_1#1$1",focus="r")]
[name="拓荒者B"]吧唧......欸？
[Dialog]
[charslot]
[name="拓荒者&莱欧斯小队"]欸？？？
拓荒

... (全文36490字符)
```

### level_act36side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_laccolith",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4142_laios_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="莱欧斯"]汇总一下我们一路上收集的有关罗德岛的情报吧。
[name="莱欧斯"]首先，大鲍勃和大祭司都认为罗德岛可以帮助我们......
[charslot(slot="m",name="avg_4142_laios_1#16$1",focus="m")]
[name="莱欧斯"]其次，小刻也说这里有个叫作“博士”的人肯定知道怎么解决我们的问题......
[charslot(slot="m",name="avg_4142_laios_1#18$1",focus="m")]
[name="莱欧斯"]以及，我们这次好像终于真的接近那艘舰船了！
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]希望那里真的有能解决我们问题的方法......
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]你们快过来看！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_0_rhodes3",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
在齐尔查克的招呼下，三人走到了悬崖边，那一瞬间，他们就理解了齐尔查克的语气为什么会有些焦急。
那是一艘过于巨大的陆上舰船。
在陆地上航行，却比他们见过的任何一艘水上船只都要庞大。
一座钢铁巨构。一座城市。一座......迷宫。
这就是——“罗德岛”。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_laccolith",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]......真的是一艘在陆地行驶的舰船啊。
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]我们真的能在那里找到回去的路吗？
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]首先，我觉得我们应该考虑的是——
[name="齐尔查克"]我们该怎么进去？
[charslot(slot="m",name="avg_4144_chilc_1#6$1",focus="m")]
[name="齐尔查克"]从这里我甚至看不见它的入口。
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]......你们看！那边好像有一支队伍在靠近罗德岛。
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]看起来好像是一支商队。
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]商队......
[name="莱欧斯"]各位，我们去和他们聊聊吧？看他们是否愿意带我们进去。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_rhodeslowerdeck",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_npc_090",focus="m")]
[name="先锋干员"]我们回来了。
[charslot(slot="m",name="avg_npc_942_1#1$1",focus="m")]
[name="泥岩"]辛苦了。
[charslot(slot="m",name="avg_npc_090",focus="m")]
[name="先锋干员"]没事。对了，我们刚刚还遇到了四个来求助的人，穿着打扮都挺奇怪的，说是和刻俄柏认识，想让罗德岛帮他们回家。
[charslot(slot="m",name="avg_npc_942_1#1$1",focus="m")]
[name="泥岩"]嗯？回家？
[charslot(slot="m",name="avg_npc_090",focus="m")]
[name="先锋干员"]大概是这个意思，总之辛苦你给他们带一下路，我去和外勤部对接了。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[Delay(time=2)]
[name="莱欧斯小队"]......
[Dialog]
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]你好！
[charslot(slot="m",name="avg_npc_942_1#1$1",focus="m")]
[name="泥岩"]如果你们是专门来罗德岛求助的，应该是要找博士或者是阿米娅吧？
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]嗯......小刻倒是说过“博士”，我们可能是要找这个人......
[name="玛露西尔"]你能带我们去见这个博士吗？
[charslot(slot="m",name="avg_npc_942_1#1$1",focus="m")]
[name="泥岩"]......我还需要确认下你们的身份，你们先跟我......
[Dialog]
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[CameraShake(duration=0.3 ,xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$book_close",volume=1,channel="1")]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_paper2",volume=1,channel="2")]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_4142_laios_1#8$1",focus="m")]
[name="莱欧斯"]哦哦......！不好意思，我的东西掉了......
[charslot(slot="m",name="avg_npc_942_1#1$1",focus="m")]
[name="泥岩"]《鲍勃的美食指南》？
[name="泥岩"]你们认识大鲍勃？
[charslot(slot="m",name="avg_4142_laios_1#18$1",focus="m")]
[name="莱欧斯"]嗯，我们来这里吃到的第一顿饭就是他做的。
[charslot(slot="m",name="avg_4143_sensi_1#3$1",focus="m")]
[name="森西"]能把那样坚硬的虫子处理成一道道美味的食物，老夫很敬佩那个人。
[charslot(slot="m",name="avg_npc_942_1#1$1",focus="m")]
[name="泥岩"]我明白了......原来他说的“那些朋友”就是你们。
[charslot(slot="m",name="avg_4142_laios_1#8$1",focus="m")]
[name="莱欧斯"]......什么？
[charslot(slot="m",name="avg_npc_942_1#1$1",focus="m")]
[name="泥岩"]我叫泥岩，大鲍勃和我讲过你们。当初他们刚决定不再当佣兵，想要换一个活法，但完全不知道开农场的事能不能行。
[name="泥岩"]荒野上的农场经常会遭到洗劫，大鲍勃也不认识几个做生意的人，啤酒做出来也不知道好不好。
[name="泥岩"]但你们当时吃他的料理的样子很幸福，给了他不少信心。
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]老夫当时并没有看出来他这样窘迫......
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]那......那他现在怎么样......？
[charslot(slot="m",name="avg_npc_942_1#1$1",focus="m")]
[name="泥岩"]不知道，我们也很久没见过了。
[name="泥岩"]我只是听说他后来源石虫啤酒厂办得很好，赚了不少钱，也过上好日子了。
[charslot(slot="m",name="avg_4143_sensi_1#2$1",focus="m")]
[name="森西"]那就好......
[charslot(slot="m",name="avg_npc_942_1#1$1",focus="m")]
[name="泥岩"]但后来又听说好像是挣钱的时候得罪了当地政府，说是税务还是什么问题，被关进监狱里了。
[charslot(slot="m",name="avg_4144_chilc_1#1$1",focus="m")]
[name="齐尔查克"]......啊？
[charslot(slot="m",name="avg_4141_marcil_1#11$1",focus="m")]
[name="玛露西尔"]监狱？那他们现在还好吗......？
[charslot(slot="m",name="avg_npc_942_1#1$1",focus="m")]
[name="泥岩"]前段时间又听说他们好像越狱还是保释出来了，人没什么问题。
[charslot(slot="m",name="avg_4142_laios_1#1$1",focus="m")]
[name="莱欧斯"]......嗯？嗯......
[charslot(slot="m",name="avg_4144_chilc_1#6$1",focus="m")]
[name="齐尔查克"]越狱啊......
[charslot(slot="m",name="avg_npc_942_1#1$1",focus="m")]
[name="泥岩"]再听说到的就是他们好像在萨米开了家杂货店，生意不错呢。
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]啊......
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]真是......很有毅力地在生活啊......
[charslot(slot="m",name="avg_npc_942_1#1$1",focus="m")]
[name="泥岩"]不管怎么说，先跟我来吧，我们坐电梯上去......
[charslot(slot="m",name="avg_4142_laios_1#8$1",focus="m")]
[name="莱欧斯"]电梯......？就是这个铁盒子吗......？它怎么用？
[charslot(slot="m",name="avg_4141_marcil

... (全文17143字符)
```

### level_act36side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_rhodesroom",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_npc_1424_1#1$1",duration=1.5)]
[Delay(time=2)]	
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="刻俄柏？"]（愤怒地吼叫）
[charslot(slot="m",name="avg_4141_marcil_1#9$1",focus="m")]
[name="玛露西尔"]魔法......魔法......唔，感觉无论用什么魔法都会伤到小刻——
[charslot(slot="m",name="char_002_amiya_1#7",focus="m")]
[name="阿米娅"]几位，请你们帮我压制住小刻，我来安抚她的情绪！
[charslot(slot="m",name="avg_4144_chilc_1#15$1",focus="m")]
[name="齐尔查克"]说是这么说，但是这家伙也太能闹腾了！
[charslot(slot="m",name="avg_4142_laios_1#14$1",focus="m")]
[name="莱欧斯"]......森西，我们之前吃的爆米花还有剩下的吗？
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]有。
[charslot(slot="m",name="avg_4142_laios_1#14$1",focus="m")]
[name="莱欧斯"]丢一把给小刻试试！
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]好！
[Dialog]
[charslot]
话音未落，森西就从口袋中掏出一把爆米花，朝着刻俄柏扔去。
而刚才还在发怒的刻俄柏立刻像是被吸引住了一样看向爆米花。
[charslot(slot="m",name="avg_4142_laios_1#14$1",focus="m")]
[name="莱欧斯"]果然，她还是想吃东西的——！
[name="莱欧斯"]可能是她在路上吃了些什么东西，把肚子吃坏了，所以才变成了这样！
[charslot(slot="m",name="avg_4144_chilc_1#16$1",focus="m")]
[name="齐尔查克"]......真的会有人吃坏了肚子变成魔物吗？
[charslot(slot="m",name="char_002_amiya_1#7",focus="m")]
[name="阿米娅"]凯尔希医生和我说过，小刻的身上有特殊的血脉，确实是有这种可能的......
[charslot(slot="m",name="avg_4144_chilc_1#7$1",focus="m")]
[name="齐尔查克"]真的假的？！
[charslot(slot="m",name="avg_199_yak_1#1$1",focus="m")]
[name="角峰"]之后再聊吧，趁现在把小刻压制住！
[name="角峰"]拿剑的，背锅的，你们两个看起来力气比较大，我们一起控制住她。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_4142_laios_1#3$1",focus="all")]
[charslot(slot="r",name="avg_4143_sensi_1#1$1",focus="all")]
[name="莱欧斯&森西"]好！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[CameraShake(duration=1.5, xstrength=10, ystrength=10, vibrato=20, randomness=70, fadeout=true, block=false)]
[Delay(time=2)]	
趁着刻俄柏在吃爆米花的工夫，三人小心地从背后接近，分别抱住她的三条腿。
[charslot(slot="m",name="avg_npc_1424_1#1$1",focus="m")]
[name="刻俄柏？"]（不开心地吼叫）
[charslot(slot="m",name="avg_199_yak_1#6$1",focus="m")]
[name="角峰"]趁现在，阿米娅！
[charslot(slot="m",name="char_002_amiya_1#7",focus="m")]
[name="阿米娅"]好的！
[charslot(slot="m",name="char_002_amiya_1#4",focus="m")]
[name="阿米娅"]回来吧，小刻......
[name="阿米娅"]别害怕，这里是你的家呀......！
[Dialog]
[PlaySound(key="$d_avg_magic_2",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_npc_1424_1#1$1",focus="m")]
[PlaySound(key="$d_avg_magic_2",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1.5)]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="刻俄柏？"]（吃痛吼叫）
[Dialog]
[charslot(slot="m",name="avg_2013_cerber_1#7$1",duration=1.5)]
[Delay(time=2)]	
[PlaySound(key="$bodyfalldown1",volume=1)]
[charslot(duration=1.5)]
[Delay(time=2)]	
[charslot]
[charslot(slot="m",name="avg_4141_marcil_1#1$1",focus="m")]
[name="玛露西尔"]好厉害，她用的魔法我从来没见过......
[charslot(slot="m",name="avg_199_yak_1#4$1",focus="m")]
[name="角峰"]快看，小刻变回来了！
[charslot(slot="m",name="char_002_amiya_1#2",focus="m")]
[name="阿米娅"]太好了！
[charslot(slot="m",name="char_002_amiya_1#3",focus="m")]
[name="阿米娅"]小刻，你没事吧！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[PlayMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[charslot(slot="m",name="avg_2013_cerber_1#7$1",posfrom="0,-20",posto="0,0",afrom=0,ato=1,duration=1)]
[Delay(time=2)]
[name="刻俄柏"]嗯......刚刚......怎么了......？
[name="刻俄柏"]我好像......做了个梦......！
[charslot(slot="m",name="avg_4141_marcil_1#8$1",focus="m")]
[name="玛露西尔"]梦？！
[charslot(slot="m",name="avg_2013_cerber_1#7$1",focus="m")]
[name="刻俄柏"]啊......
[Dialog]
[charslot]
刻俄柏环视四周，原本摆放整齐的房间被撞得七扭八歪，自己手中还攥着半个坏掉的玩具。
[charslot(slot="m",name="avg_2013_cerber_1#7$1",focus="m")]
[name="刻俄柏"]对不起......火神大姐说了，做错了事就要说对不起，我好像做错事了......
[name="刻俄柏"]我在梦里好饿......肚子咕噜地叫了一下......然后......
[charslot(slot="m",name="char_002_amiya_1#4",focus="m")]
[name="阿米娅"]然后......？
[charslot(slot="m",name="avg_2013_cerber_1#10$1",focus="m")]
[name="刻俄柏"]然后我就长出了好多个脑袋，想吃很多很多东西！
[charslot(slot="m",name="avg_2013_cerber_1#7$1",focus="m")]
[name="刻俄柏"]只要肚子吃饱了，我就很高兴，就又回到这里来了！
[charslot(slot="m",name="char_002_amiya_1#4",focus="m")]
[name="阿米娅"]（小声）......角峰，火神在哪里？她最近有发现这个情况吗......？
[charslot(slot="m",name="avg_199_yak_1#2$1",focus="m")]
[name="角峰"]（小声）我待会儿去问问她......
[name="角峰"]（小声）那小刻现在......？
[charslot(slot="m",name="avg_2013_cerber_1#10$1",focus="m")]
[name="刻俄柏"]......咕噜......
[charslot(slot="m",name="avg_4143_sensi_1#1$1",focus="m")]
[name="森西"]嗯？小刻，你肚子又饿了吗？
[charslot(slot="m",name="avg_2013_cerber_1#1$1",focus="m")]
[name="刻俄柏"]嗯！
[charslot(slot="m",name="avg_2013_cerber_1#3$1",focus="m")]
[name="刻俄柏"]我想吃好多好多东西！
[name="刻俄柏"]我在梦里吃饱了，可现在还是很饿！
[charslot(slot="m",name="avg_4142_laios_1#16$1",focus="m")]
[name="莱欧斯"]嗯......嗯......
[name="莱欧斯"]那你知道，一个长着三个脑袋的怪物吗？
[charslot(slot="m",name="avg_2013_cerber_1#1$1",focus="m")]
[name="刻俄柏"]我当然知道！
[charslot(slot="m",name="avg_4142_laios_1#7$1",focus="m")]
[name="莱欧斯"]它是......？
[charslot(slot="m",name="avg_2013_cerber_1#3$1",focus="m")]
[name="刻俄柏"]不只是三个脑袋，是一千个脑袋！
[charslot(slot="m",name="avg_4142_laios_1#8$1",focus="m")]
[name="莱欧斯"]......！
[charslot(slot="m",name="avg_2013_cerber_1#1$1",focus="m")]
[name="刻俄柏"]小刻每次都想吃好多好多的东西，长十个......一百个，啊不对，一千个！一千个脑袋都吃不够！
[charslot(slot="m",name="avg_2013_cerber_1#3$1",focus="m")]
[name="刻俄柏"]小刻有一千个脑袋哦！
[Dialog]
[charslot]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=20, randomness=70, fadeout=true

... (全文27254字符)
```

### training_act36side_01_a

```
[HEADER] 活动36side教学关_a

[executeactionarray(target="char_4142_laios", key="stop_sp_recovery")]
[camerafocusto(offsetX="3.5", offsetY="4", time="1", scale="CLOSE")]
[delay(time="1")]
[name="莱欧斯", avatarId="char_4142_laios", isAvatarRight="FALSE"]吃饱了走路也有劲了，不知不觉都走这么久了！
[delay(time="1")]
[summonenemy(enemyId="enemy_1001_bigbo", x="4", y="4", endX="4", endY="5", countAsKilled="True")]
[move(enemyId="enemy_1001_bigbo", row="4", col="4")]
[delay(time="0.5")]
[playAnim(enemyId="enemy_1001_bigbo", anim="Idle", dir="LEFT")]
[name="大鲍勃", avatarId="npc_010", isAvatarRight="TRUE"]慢着慢着！走那么急干什么......
[playAnim(charId="char_4142_laios", anim="Idle", dir="RIGHT")]
[delay(time="1")]
[name="莱欧斯", avatarId="char_4142_laios", isAvatarRight="FALSE"]是大鲍勃！还有什么事吗？
[name="大鲍勃", avatarId="npc_010", isAvatarRight="TRUE"]我才想起来，还没教给你们在野外烹饪的重要一课呢。
[name="大鲍勃", avatarId="npc_010", isAvatarRight="TRUE"]你们也想顿顿都能吃得和刚才一样好，对吧？
[resetCamera(time="1.5")]
[executeactionarray(target="char_4142_laios", key="recover_sp_recovery")]

[end]
```

### training_act36side_01_b

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动36side教学关_b

[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]

[PopupDialog(dialogHead="$avatar_marcil")]刚才那一顿......
[PopupDialog(dialogHead="$avatar_laios")]光是想一想就又有点饿了......

[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true, black=0)]
[Delay(time=3)]

[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]
[PopupDialog(dialogHead="$avatar_laios")]森西，我们下一餐吃什么？
[Tutorial(dialogHead="$avatar_sensi",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]老夫也得学一学这里的魔物怎么烹饪才行呢......
[PopupDialog(dialogHead="$avatar_bigbo")]那就从在野外烹饪源石虫学起吧！
[PopupDialog(dialogHead="$avatar_marcil")]......欸？

[Battle.Pause(pause=false)]
```

### training_act36side_01_c

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动36side教学关_c

[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]

[PopupDialog(dialogHead="$avatar_bigbo")]在野外冒险，饿着肚子会使人<@tu.kw>不断流失生命</>，而且流失的速度会<@tu.kw>越来越快</>。

[Tutorial(focusX=50, focusY=100, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_bigbo",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]但只要有这口<@tu.kw>大锅</>，就可以利用周围的食材填饱肚子。

[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true, black=0)]
[Delay(time=4)]

[Battle.Pause]

[Tutorial(focusX=50, focusY=100, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_bigbo",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]击倒<@tu.kw>可以食用</>的敌人，它们身上可食用的部分会作为食材加到锅里。

[Tutorial(focusX=50, focusY=100, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_bigbo",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]敌人<@tu.kw>越重</>，能够提供的食材就越多。

[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true, black=0)]
[Delay(time=11)]
[Battle.Pause(pause=true)]

[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]

[InputBlocker(blockInput=true, validX=50, validY=100, validWidth=100, validHeight=100)]

[Tutorial(waitForSignal="char_info", focusX=50, focusY=100, focusWidth=100, focusHeight=100, \
          animStyle="Click", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_bigbo", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
锅里装足食材以后，就可以开始烹饪。
[InputBlocker(blockInput=true)]

[Delay(time=1)]

[Tutorial(target="btn_skill",  waitForSignal="use_skill", \
          animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_bigbo")] \
烹饪要注意时间和火候，得稍等一会儿......

[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true, black=0)]
[Delay(time=6)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=true, black=0.3)]

[PopupDialog(dialogHead="$avatar_laios")]好香！我们也可以自己做源石虫大餐了！

[PopupDialog(dialogHead="$avatar_marcil")]好熟悉的香味！

[PopupDialog(dialogHead="$avatar_bigbo")]吃饱饭能让所有人<@tu.kw>提升</>少量攻击力，且不断<@tu.kw>恢复</>生命。

[PopupDialog(dialogHead="$avatar_bigbo")]但锅里的食物会<@tu.kw>不断消耗</>，总有吃完的时候。

[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true, black=0)]
[Delay(time=3)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=true, black=0.3)]

[PopupDialog(dialogHead="$avatar_bigbo")]你们需要击败可以食用的敌人来<@tu.kw>补充</>食材。

[PopupDialog(dialogHead="$avatar_bigbo")]不然食物没了，又会重新挨饿。

[Tutorial(dialogHead="$avatar_laios",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]啊？我可不想饿肚子——

[PopupDialog(dialogHead="$avatar_bigbo")]偶尔，你们可能会遇到一些<@tu.kw>特别的敌人</>。

[PopupDialog(dialogHead="$avatar_bigbo")]比如说，看到那只在睡觉的虫子了吗？

[Tutorial(dialogHead="$avatar_marcil",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]我来看看！

[Battle.Pause(pause=false)]
```

### training_act36side_01_d

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动36side教学关_d

[Battle.Pause(pause=true)]

[Tutorial(dialogHead="$avatar_marcil",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]呜哇，我的眼睛！

[InputBlocker(blockInput=true, black=0.2)]

[PopupDialog(dialogHead="$avatar_chilc")]真是的，还是我来吧。

[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true, black=0)]
[Delay(time=10)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=-70, focusY=70, focusWidth=100, focusHeight=100, anchor="BottomRight",\
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_bigbo",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]做得好，在一些特殊情况下，能够获得<@tu.kw>特殊食材</>。

[Tutorial(focusX=-70, focusY=70, focusWidth=100, focusHeight=100, anchor="BottomRight",\
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_bigbo",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]比如这个“闪亮果实”。

[InputBlocker(blockInput=true, black=0.3)]

[PopupDialog(dialogHead="$avatar_bigbo")]特殊食材的用途很多——

[PopupDialog(dialogHead="$avatar_bigbo")]可以直接<@tu.kw>放到锅里</>，做出特别的食物，给<@tu.kw>所有人</>提供特殊效果。

[PopupDialog(dialogHead="$avatar_bigbo")]也可以<@tu.kw>单独</>交给一个人，让他独享。

[PopupDialog(dialogHead="$avatar_bigbo")]当然，你也可以直接<@tu.kw>放在地上</>，也可能会有特别的效果......

[PopupDialog(dialogHead="$avatar_bigbo")]这片大地很大，到底什么可以吃、应该怎么吃，就需要你们自己去研究了！

[PopupDialog(dialogHead="$avatar_bigbo")]给你们的那本《鲍勃的美食指南》，就当最基础的准备吧。

[PopupDialog(dialogHead="$avatar_bigbo")]如果遇到什么新奇事，最好找个地方记下来。

[PopupDialog(dialogHead="$avatar_bigbo")]下次见面时再讲给我听，好酒好菜管够！

[Battle.Pause(pause=false)]
```

### training_act36side_08

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动36side_08
[Battle.lockFunction(mask="CARD_LIST")]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]
[PopupDialog(dialogHead="$avatar_cerber")]唔，身体怪怪的......
[PopupDialog(dialogHead="$avatar_cerber")]想吃这个，又想吃那个......
[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true, black=0)]
[Delay(time=9)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.1)]
[PopupDialog(dialogHead="$avatar_cerber")]呜啊，小刻......
[PopupDialog(dialogHead="$avatar_cerber")]一张嘴吃不下，小刻全都想要！
[Battle.unlockFunction(mask="CARD_LIST")]
[Battle.Pause(pause=false)]
```


## 统计

- 总字符数：353284
- 对话行数：2536


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
