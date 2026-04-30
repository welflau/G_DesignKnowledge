# 明日方舟 · 活动剧情 · act7fun（9段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act7fun」完整剧情脚本（9个文件，73行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act7fun
- 脚本文件数：9

### level_act7fun_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltruins",screenadapt="coverall")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot(slot = "m", name = "avg_npc_2250_1#3$1",focus="m")]
[name="博士？"]   带上这些以前被对面揍过的帮手，就能分散对方的注意力。
[charslot(slot = "m", name = "avg_npc_2250_1#3$1",focus="m")]
[name="博士？"]   趁此机会，我们把罗德岛珍藏的收藏品一个一个砸了，他们的强度就会大打折扣，只能屈辱地乖乖投降了。
[charslot(slot = "m", name = "avg_npc_2250_1#3$1",focus="m")]
[name="博士？"]   先毁了原型之手，他们的战斗力便会马上下降。
[charslot(slot = "m", name = "avg_npc_2250_1#8$1",focus="m")]
[name="博士？"]   在此之后，就是Miss.Christine摸摸券和金酒之杯！哈哈！
[charslot(slot = "m", name = "avg_npc_2251_1#1$1",focus="m")]
[name="阿米娅？"]   博士真的很辛苦，竟然做了这么精妙的计划！请务必好好休息！
[charslot(slot = "m", name = "avg_npc_2250_1#4$1",focus="m")]
[name="博士？"]   阿米娅你可真是太体贴了~
[dialog]
[charslot]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot = "l", name = "avg_npc_2255_1#1$1",focus="all",duration=2)]
[charslot(slot = "r", name = "avg_npc_2256_1#1$1",focus="all",duration=2)]
[delay(time=3)]
[charslot(slot = "l", name = "avg_npc_2255_1#1$1",focus="l")]
[name="能天使？"]  嗯，他们好像玩得很开心。我们干点什么？
[charslot(slot = "r", name = "avg_npc_2256_1#6$1",focus="r")]
[name="德克萨斯？"]  感觉很无趣。
[charslot(slot = "l", name = "avg_npc_2255_1#2$1",focus="l")]
[name="能天使？"]  那，试试那个？
[charslot(slot = "r", name = "avg_npc_2256_1#1$1",focus="r")]
[name="德克萨斯？"]  哪个？
[dialog]
[charslot(slot = "l", name = "avg_npc_2255_1#2$1",focus="all")]
[charslot(slot = "l", focus="all",posfrom="0,0",posto="50,0",duration=0.3)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[charslot(slot = "l", focus="all",posfrom="50,0",posto="0,0",duration=0.4)]
[delay(time=0.2)]
[charslot(slot = "l", focus="all",posfrom="0,0",posto="50,0",duration=0.3)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[charslot(slot = "l", focus="all",posfrom="50,0",posto="0,0",duration=0.4)]
[delay(time=0.7)]
[charslot(slot = "l", focus="all",posfrom="0,0",posto="50,0",duration=0.3)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[charslot(slot = "l", focus="all",posfrom="50,0",posto="0,0",duration=0.4)]
[delay(time=2)]
[charslot(slot = "l", name = "avg_npc_2255_1#5$1",focus="l")]
[name="能天使？"]  生气了吗？
[charslot(slot = "r", name = "avg_npc_2256_1#6$1",focus="r")]
[name="德克萨斯？"]  ......
[dialog]
[charslot(slot = "l", name = "avg_npc_2255_1#2$1",focus="all")]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$p_atk_smg_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$p_atk_smg_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[delay(time=0.5)]
[PlaySound(key="$shotgunreload",volume=1)]
[delay(time=1)]
[Dialog]
[PlaySound(key="$d_avg_gunshot", volume=0.9)]
[CameraShake(duration=1, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=1,g=1, b=1, fadetime=0, block=true)]
[Blocker(a=1, r=1,g=1, b=1, fadetime=0.03, block=true)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=false)]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_npc_2255_1#2$1",focus="l")]
[name="能天使？"]  生气了吗？
[charslot(slot = "r", name = "avg_npc_2256_1#5$1",focus="r")]
[CameraShake(duration=1, xstrength=3, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="德克萨斯？"]  你这个混蛋......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=4, block=true)]
[Dialog]
[Character]
[Image]
```

### level_act7fun_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltruins",screenadapt="coverall")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot(slot = "m", name = "avg_npc_2250_1#7$1",focus="m")]
[name="博士？"]   可恶，虽然成功了，但是看他们不仅不消沉反而变积极了的样子就来气！
[dialog]
[charslot(slot = "m", name = "avg_npc_2251_1#2$1",focus="m")]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[CameraShake(duration=1, xstrength=0, ystrength=10, vibrato=1, randomness=0, fadeout=true, block=false)]
[delay(time=1)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[CameraShake(duration=1, xstrength=0, ystrength=10, vibrato=1, randomness=0, fadeout=true, block=false)]
[delay(time=1)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[CameraShake(duration=1, xstrength=0, ystrength=20, vibrato=1, randomness=0, fadeout=true, block=false)]
[delay(time=1)]
[multiline(name="阿米娅？")]  只有这样多多锻炼！嗬啊！才能保护！
[charslot(slot = "m", name = "avg_npc_2251_1#6$1",focus="m")]
[charslot(slot = "m", focus="all",posfrom="0,0",posto="50,0",duration=0.3)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[charslot(slot = "m", focus="all",posfrom="50,0",posto="0,0",duration=0.4)]
[delay(time=0.2)]
[charslot(slot = "m", focus="all",posfrom="0,0",posto="50,0",duration=0.3)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[charslot(slot = "m", focus="all",posfrom="50,0",posto="0,0",duration=0.4)]
[delay(time=0.7)]
[charslot(slot = "m", focus="all",posfrom="0,0",posto="50,0",duration=0.3)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[charslot(slot = "m", focus="all",posfrom="50,0",posto="0,0",duration=0.4)]
[delay(time=2)]
[multiline(name="阿米娅？")]  嗬啊！博士和凯尔希医生！嗬啊！还有罗德岛！
[charslot(slot = "m", name = "avg_npc_2250_1#4$1",focus="m")]
[name="博士？"]   阿米娅这么可爱，一切努力都值了啊。
[charslot(slot = "m", name = "avg_npc_2253_1#8$1",focus="m")]
[name="维什戴尔？"]   那我呢那我呢？
[charslot(slot = "m", name = "avg_npc_2250_1#8$1",focus="m")]
[name="博士？"]   可恶，罗德岛太可恶了又生气起来了！
[charslot(slot = "m", name = "avg_npc_2253_1#6$1",focus="m")]
[name="维什戴尔？"]   啊？？
[dialog]
[charslot]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot = "l", name = "avg_npc_2255_1#1$1",focus="all",duration=2)]
[charslot(slot = "r", name = "avg_npc_2256_1#1$1",focus="all",duration=2)]
[delay(time=3)]
[charslot(slot = "l", name = "avg_npc_2255_1#1$1",focus="l")]
[name="能天使？"]  我们要去帮忙作战吗？
[charslot(slot = "r", name = "avg_npc_2256_1#6$1",focus="r")]
[name="德克萨斯？"]  反正也没人来要求我们帮忙，为什么要去？
[charslot(slot = "l", name = "avg_npc_2255_1#1$1",focus="l")]
[name="能天使？"]  但实在是没什么事做，要不下一关我们还是一起上吧。
[charslot(slot = "r", name = "avg_npc_2256_1#6$1",focus="r")]
[name="德克萨斯？"]  你知道怎么过去吗？
[charslot(slot = "l", name = "avg_npc_2255_1#1$1",focus="l")]
[name="能天使？"]  不知道，算了吧。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=4, block=true)]
[Dialog]
[Character]
[Image]
```

### level_act7fun_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor_4",screenadapt="coverall")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
一份粉色的小礼物放在桌子上，旁边的卡片上写着：“这是我准备了很久的礼物，请你收下♥......”
[dialog]
[charslot(slot = "m", name = "avg_doc_1#1",focus="all",duration=2)]
[delay(time=2)]
[Effect(name="$e_emoji_question",layer = 1,x=50,y=150)]
[dialog]
[delay(time=3)]
[dialog]
[charslot]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.02, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[PlaySound(key="$d_sp_ballista", volume=0.8)]
[CameraShake(duration=2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.02, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[PlaySound(key="$d_sp_ballista", volume=0.8)]
[CameraShake(duration=2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_rockfall", volume=1)]
[PlaySound(key="$d_avg_ship_creak", volume=1)]
[delay(time=4)]
[charslot(slot = "r", name = "avg_npc_2253_1#1$1",focus="all",duration=1)]
[charslot(slot = "l", name = "avg_1035_wisdel_1#1$1",focus="all",duration=1)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_1035_wisdel_1#7$1",focus="l")]
[name="维什戴尔"]你这个家伙，还不赖嘛？
[charslot(slot = "r", name = "avg_npc_2253_1#5$1",focus="r")]
[name="维什戴尔？"]   虽然我跟你不是一边的，但是我看你也还不错啊？
[dialog]
[charslot]
[PlaySound(key="$rungeneral")] 
[charslot(slot = "m", name = "avg_npc_2251_1#6$1",focus="m",duration=1)]
[delay(time=1)]
[name="阿米娅？"]   不许伤害博士！
[dialog]
[PlaySound(key="$d_avg_magicchange", volume=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.3, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[charslot]
[delay(time=0.2)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[PlaySound(key="$fightgeneral")] 
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[delay(time=0.5)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[PlaySound(key="$fightgeneral")] 
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[delay(time=0.3)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[PlaySound(key="$fightgeneral")] 
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[delay(time=0.1)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[PlaySound(key="$fightgeneral")] 
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=false)]
[delay(time=0.1)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[PlaySound(key="$fightgeneral")] 
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=false)]
[delay(time=0.1)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[PlaySound(key="$fightgeneral")] 
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=false)]
[delay(time=0.1)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[PlaySound(key="$fightgeneral")] 
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.1, block=false)]
[delay(time=0.1)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[PlaySound(key="$fightgeneral")] 
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.1, block=false)]
[delay(time=0.1)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[PlaySound(key="$fightgeneral")] 
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.1, block=false)]
[delay(time=0.1)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$punch_n1")]
[PlaySound(key="$d_avg_attack_heavy", volume=0.9)]
[PlaySound(key="$d_avg_bone_rub", volume=0.9)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=false)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[delay(time=1)]
[Background(image="bg_corridor_4",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "m", name = "avg_npc_2253_1#7$1",focus="m")]
[name="维什戴尔？"]   你到底保护的是哪边？！
[charslot(slot = "m", name = "avg_npc_2251_1#6$1",focus="m")]
[name="阿米娅？"]   哪个博士都不能受伤害！
[charslot(slot = "m", name = "avg_1035_wisdel_1#4$1",focus="m")]
[name="维什戴尔"] 我只是路过的，关我什么事？
[dialog]
[charslot]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot = "l", name = "avg_npc_2255_1#1$1",focus="all"

... (全文6854字符)
```

### level_act7fun_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor_4",screenadapt="coverall")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot(slot = "m", name = "char_349_chiave#2",focus="m",duration=1)]
[CameraShake(duration=2, xstrength=10, ystrength=10, vibrato=90, randomness=40, fadeout=true, block=false)]
[delay(time=2)]
[charslot]
[charslot(slot = "m", name = "avg_npc_2252_1#2$1",focus="m",duration=1)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_2252_1#2$1",focus="m")]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.4)]
[PlaySound(key="$d_avg_attack_heavy", volume=0.9)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[PlaySound(key="$rungeneral", volume=0.9)]
[charslot(slot = "r", name = "avg_npc_2251_1#1$1",layer=2,focus="all",duration=2)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_npc_2252_1#3$1",focus="m")]
[charslot(slot = "m", name = "avg_npc_2252_1#3$1",focus="all")]
[charslot(slot = "m",posfrom="0,0",posto="30,0",focus="all",duration=0.7)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_2251_1#3$1",focus="all")]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=0, vibrato=1, randomness=0, fadeout=true, block=false)]
[delay(time=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "m", name = "avg_282_catap_1#5$1",focus="m",duration=1)]
[CameraShake(duration=2, xstrength=10, ystrength=10, vibrato=90, randomness=40, fadeout=true, block=false)]
[delay(time=2)]
[charslot]
[charslot(slot = "m", name = "avg_npc_2252_1#2$1",focus="m",duration=1)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_2252_1#2$1",focus="m")]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.4)]
[PlaySound(key="$d_avg_attack_heavy", volume=0.9)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[PlaySound(key="$rungeneral", volume=0.9)]
[charslot(slot = "l", name = "avg_1037_amiya3_1#5$1",focus="all",duration=2)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_npc_2252_1#3$1",focus="all")]
[charslot(slot = "m",posfrom="0,0",posto="-20,0",focus="all",duration=0.7)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_1037_amiya3_1#11$1",layer=2,dfocus="all")]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=0, vibrato=1, randomness=0, fadeout=true, block=false)]
[delay(time=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_2252_1#3$1",focus="all")]
[charslot(slot = "r", name = "avg_npc_2251_1#3$1",focus="all")]
[charslot(slot = "l", name = "avg_1037_amiya3_1#11$1",focus="all")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot = "m",posfrom="0,0",posto="20,0",focus="all",duration=0.5)]
[delay(time=1)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=0, vibrato=1, randomness=0, fadeout=true, block=false)]
[delay(time=1)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=0, vibrato=1, randomness=0, fadeout=true, block=false)]
[delay(time=3)]
[charslot(slot = "m",posfrom="20,0",posto="-20,0",focus="all",duration=1)]
[delay(time=1.5)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=0, vibrato=1, randomness=0, fadeout=true, block=false)]
[delay(time=1)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=0, vibrato=1, randomness=0, fadeout=true, block=false)]
[delay(time=3)]
[charslot]
[charslot(slot = "m", name = "avg_npc_2250_1#4$1",focus="all",duration=1)]
[delay(time=1)]
[name="博士？"]   凯尔希还是这么宠阿米娅啊。真好。
[dialog]
[charslot(slot = "r", name = "avg_npc_2252_1#2$1",focus="r",duration=1)]
[delay(time=2)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.4)]
[PlaySound(key="$d_avg_attack_heavy", volume=0.9)]
[PlaySound(key="$d_avg_bone_rub", volume=0.9)]
[PlaySound(key="$d_avg_slip")]
[charslot(slot = "m", name = "avg_npc_2250_1#6$1",focus="all",duration=0)]
[charslot(slot = "m", name = "avg_npc_2250_1#6$1",afrom=1,ato=0,focus="all",duration=0.8)]
[charslot(slot="m",posfrom="0,0",posto="-200,200",duration=1)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot = "l", name = "avg_npc_2255_1#1$1",focus="all",duration=2)]
[charslot(slot = "r", name = "avg_npc_2256_1#1$1",focus="all",duration=2)]
[delay(time=3)]
[charslot(slot = "l", name = "avg_npc_2255_1#1$1",focus="l")]
[name="能天使？"]  真好，看来凯尔希和阿米娅的关系在哪里都一样。
[charslot(slot = "r", name = "avg_npc_2256_1#6$1",focus="r")]
[name="德克萨斯？"]  ......凯尔希和博士的关系看起来也一样。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=4, block=true)]
[Dialog]
[Character]
[Image]
```

### level_act7fun_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor_4",screenadapt="coverall")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$swordtsing1", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$swordtsing1", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
[PlaySound(key="$swordtsing2", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=20, ystrength=22, vibrato=50, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.02, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[PlaySound(key="$d_sp_ballista", volume=0.8)]
[CameraShake(duration=2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_rockfall", volume=1)]
[delay(time=4)]
[charslot(slot = "m", name = "avg_npc_2254_1#1$1",focus="m",duration=1)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_npc_2254_1#7$1",focus="m")]
[delay(time=2)]
[name="银灰？"]   你觉得我这发型如何？
[charslot(slot = "m", name = "avg_172_svrash_1#5$1",focus="m")]
[name="银灰"]   ......
[charslot(slot = "m", name = "avg_npc_2254_1#3$1",focus="m")]
[name="银灰？"]   ......
[charslot(slot = "m", name = "avg_172_svrash_1#2$1",focus="m")]
[name="银灰"]   ......
[charslot(slot="m",name="avg_174_slbell_1#8$1",focus="m")]
[name="初雪"]不太行。
[charslot]
[charslot(slot = "l", name = "avg_172_svrash_1#7$1",focus="all")]
[charslot(slot = "r", name = "avg_npc_2254_1#5$1",focus="all")]
[name="银灰&银灰？"]   ......
[charslot]
[charslot(slot = "m", name = "avg_npc_2250_1#7$1",focus="m")]
[name="博士？"]   你们这些家伙能不能认真干干活啊？
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot = "l", name = "avg_npc_2255_1#1$1",focus="all",duration=2)]
[charslot(slot = "r", name = "avg_npc_2256_1#1$1",focus="all",duration=2)]
[delay(time=3)]
[PlaySound(key="$d_avg_humaneat")]
[CameraShake(duration=1, xstrength=0, ystrength=3, vibrato=3, randomness=0, fadeout=true, block=false)]
[delay(time=3)]
[charslot]
[charslot(slot = "l", name = "avg_103_angel_1#1$1",focus="all",duration=2)]
[charslot(slot = "r", name = "char_102_texas_1#1",focus="all",duration=2)]
[delay(time=3)]
[PlaySound(key="$d_avg_humaneat")]
[CameraShake(duration=1, xstrength=0, ystrength=3, vibrato=3, randomness=0, fadeout=true, block=false)]
[delay(time=3)]
[charslot]
[charslot(slot = "m", name = "avg_npc_2256_1#3$1",focus="m")]
[name="德克萨斯？"]   ......为什么人变多了？
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=4, block=true)]
[Dialog]
[Character]
[Image]
```

### level_act7fun_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor_4",screenadapt="coverall")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot(slot = "l", name = "avg_npc_2251_1#5$1",focus="all",duration=1)]
[charslot(slot = "r", name = "avg_npc_2252_1#2$1",focus="all",duration=1)]
[delay(time=2)]
[charslot]
[charslot(slot = "m", name = "avg_npc_2250_1#2$1",focus="m",duration=1)]
[delay(time=2)]
[name="博士？"]   不、不会吧，忙活了这么久......
[charslot(slot = "m", name = "avg_npc_2250_1#5$1",focus="m")]
[name="博士？"]   只把原型之手破坏了就结束了？这样的话，下次集成战略他们岂不是还有金酒之杯可以用吗？
[charslot(slot = "m", name = "avg_npc_2251_1#5$1",focus="m")]
[name="阿米娅？"]   因为活动产能就这点了，只能做这么多了，博士我们还是好好回去吧。
[charslot(slot = "m", name = "avg_npc_2250_1#6$1",focus="m")]
[name="博士？"]   我不甘心啊！明年开始的复刻也都只是一模一样地重复一遍而已啊！
[charslot(slot = "m", name = "avg_npc_2252_1#2$1",focus="m")]
[name="凯尔希？"]   ......你给我走。别为难阿米娅了。
[charslot(slot = "m", name = "avg_npc_2254_1#6$1",focus="m")]
[name="银灰？"]  走吧走吧，这里太残酷了。我得去找个对我好点的妹妹。
[dialog]
[PlaySound(key="$d_avg_magicchange", volume=1)]
[charslot(duration=2)]
[delay(time=3)]
[charslot(slot = "l", name = "avg_npc_2251_1#3$1",focus="all")]
[charslot(slot = "r", name = "avg_npc_2252_1#2$1",focus="all")]
[delay(time=0.4)]
[dialog]
[PlaySound(key="$d_avg_magicchange", volume=1)]
[charslot(duration=2)]
[delay(time=3)]
[charslot(slot = "m", name = "avg_npc_2250_1#7$1",focus="m")]
[name="博士？"]   我一定不会善罢甘休的！
[dialog]
[PlaySound(key="$d_avg_magicchange", volume=1)]
[charslot(duration=3)]
[delay(time=4)]
[charslot(slot = "m", name = "avg_1037_amiya3_1#5$1",focus="all",duration=2)]
[delay(time=4)]
[dialog]
[charslot(slot = "m", name = "avg_1037_amiya3_1#5$1",focus="n")]
[Decision(options="这到底是怎么回事？", values="1")]
[Predicate(references="1")]
[charslot(slot = "m", name = "avg_1037_amiya3_1#7$1",focus="m")]
[name="阿米娅"]   我也不知道，可能......是某种神奇的源石技艺吧。
[charslot(slot = "m", name = "avg_1037_amiya3_1#16$1",focus="m")]
[name="阿米娅"]   希望我们不会受到什么影响。
[dialog]
[charslot]
[delay(time=4)]
[charslot(slot = "r", name = "avg_npc_2253_1#1$1",focus="all",duration=1)]
[charslot(slot = "l", name = "avg_1035_wisdel_1#1$1",focus="all",duration=1)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_2253_1#4$1",focus="r")]
[name="维什戴尔？"]伙计，我们就这样说定了，你帮我偷偷留下来吧。
[charslot(slot = "l", name = "avg_1035_wisdel_1#7$1",focus="l")]
[name="维什戴尔"]这好说，反正我们长得一模一样，没人能看出来。
[charslot(slot = "l", name = "avg_1035_wisdel_1#14$1",focus="all")]
[charslot(slot = "r", name = "avg_npc_2253_1#5$1",focus="all")]
[name="维什戴尔&维什戴尔？"]嘻嘻嘻。
[dialog]
[charslot]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot = "l", name = "avg_npc_2255_1#3$1",focus="all",duration=2)]
[charslot(slot = "r", name = "avg_npc_2256_1#1$1",focus="all",duration=2)]
[delay(time=3)]
[charslot(slot = "l", name = "avg_npc_2255_1#3$1",focus="l")]
[name="能天使？"]  事情就这么解决了？
[charslot(slot = "r", name = "avg_npc_2256_1#4$1",focus="r")]
[name="德克萨斯？"]  怎么还没完......
[charslot(slot = "l", name = "avg_npc_2255_1#5$1",focus="l")]
[name="能天使？"]  按照这个节奏，我们啥时候能动画化？应该能做个泡面番？
[charslot(slot = "r", name = "avg_npc_2256_1#6$1",focus="r")]
[name="德克萨斯？"]  ......你傻吗？
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=4, block=true)]
[Dialog]
[Character]
[Image]
```

### level_act7fun_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_rhodescom",screenadapt="coverall")]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>罗德岛会议室</><p=2>界园志异集成战略前某天</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[PlaySound(key="$d_avg_crwddiscuss_inside", channel="slide", loop=true, volume=0.4)]
[charslot(slot = "l", name = "char_196_sunbr_1#5",focus="all",duration=2)]
[charslot(slot = "r", name = "avg_328_cammou_1#1$1",focus="all",duration=2)]
[delay(time=3)]
[charslot]
[charslot(slot = "r", name = "avg_497_ctable_1#1$1",focus="all",duration=2)]
[charslot(slot = "l", name = "avg_181_flower_1#1$1",focus="all",duration=2)]
[delay(time=3)]
[charslot]
[charslot(slot = "l", name = "avg_172_svrash_1#1$1",focus="all",duration=2)]
[charslot(slot = "r", name = "avg_4145_Ulpia_1#2$1",focus="all",duration=2)]
[delay(time=3)]
[charslot]
[charslot(slot = "l", name = "avg_377_gdglow_1#1$1",focus="all",duration=2)]
[charslot(slot = "r", name = "avg_1038_whitw2_1#12$1",focus="all",duration=2)]
[delay(time=3)]
[charslot]
[charslot(slot = "l", name = "avg_1035_wisdel_1#1$1",focus="all",duration=2)]
[charslot(slot = "r", name = "avg_1041_angel2_1#1$1",focus="all",duration=2)]
[delay(time=3)]
[charslot]
[charslot(slot = "l", name = "avg_1037_amiya3_1#1$1",focus="all",duration=2)]
[charslot(slot = "r", name = "avg_4179_monstr_1#1$1",focus="all",duration=2)]
[delay(time=3)]
[charslot]
[charslot(slot = "m", name = "avg_doc_1#1",focus="all",duration=2)]
[delay(time=3)]
[stopSound(channel="slide",fadetime=2)]
[charslot]
[stopmusic(fadetime=2)]
[name="？？？"]   动手！
[dialog]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.02, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[PlaySound(key="$d_sp_ballista", volume=0.8)]
[CameraShake(duration=2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.02, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[bgeffect(name="$eb_dust_01",layer=1)]
[PlaySound(key="$d_gen_explo_n")]
[PlaySound(key="$d_sp_ballista", volume=0.8)]
[CameraShake(duration=2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_rockfall", volume=1)]
[PlaySound(key="$d_avg_ship_creak", volume=1)]
[delay(time=1)]
[name="干员们"]  咳咳咳，怎么回事？
[dialog]
[Decision(options="这又是要闹哪出？", values="1")]
[Predicate(references="1")]
[Decision(options="可露希尔，我猜肯定又是你干的！", values="1")]
[Predicate(references="1")]
[name="可露希尔"] 我本来设计的合体小车没时间完成被我放弃了啊！我冤枉！
[dialog]
[Decision(options="那到底是......", values="1")]
[Predicate(references="1")]
[name="？？？"]   从今天起，罗德岛就正式归我掌管了！
[name="？？？"]   我才是罗德岛真正的老大！
[name="？？？"]   哈哈哈哈哈哈！
[dialog]
[bgeffect]
[Background(image="bg_ltruins",screenadapt="coverall",fadetime=2)]
[charslot]
[charslot(slot = "m", name = "avg_npc_2250_1#1$1",focus="all",duration=2)]
[delay(time=3)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[name="博士？"]   只要按照我的计划行事，罗德岛一定会被我们夺回来。
[charslot]
[dialog]
[charslot(slot = "l", name = "avg_npc_2252_1#1$1",focus="all",duration=2)]
[charslot(slot = "r", name = "avg_npc_2251_1#5$1",focus="all",duration=2)]
[delay(time=3)]
[charslot]
[charslot(slot = "m", name = "avg_npc_2250_1#1$1",focus="m")]
[name="博士？"]   这群假冒罗德岛的人霸占了我们的位置！必须马上干掉他们！
[charslot(slot = "m", name = "avg_npc_2250_1#7$1",focus="m")]
[name="博士？"]   一刻都不能等！我们的机会就这几天！时间过了活动就没了！下一次还得等明年复刻！
[charslot]
[charslot(slot = "l", name = "avg_npc_2250_1#7$1",focus="r")]
[charslot(slot = "r", name = "avg_npc_2251_1#5$1",focus="r")]
[name="阿米娅？"]   博士，这样不会给博士惹麻烦吗？博士和博士都同样是博士，阿米娅希望博士能不置身于危险之中......
[charslot(slot = "l", name = "avg_npc_2250_1#4$1",focus="l")]
[name="博士？"]   阿米娅可真是好孩子，放心吧，不会有事的。
[charslot]
[charslot(slot = "m", name = "avg_npc_2254_1#1$1",focus="m")]
[name="银灰？"]   所以呢，就我们这几个人，要挑战对面几百名干员？
[charslot(slot = "m", name = "avg_npc_2253_1#4$1",focus="m")]
[name="维什戴尔？"]   这么嗨的？
[charslot(slot = "m", name = "avg_npc_2250_1#3$1",focus="m")]
[name="博士？"]   那不至于，就让我来说说我的计划......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=4, block=true)]
[Dialog]
[Character]
[Image]
```

### training_act7fun_01_a

```
[header(is_tutorial=true,is_autoable=false, is_skippable=false)]training_act7fun_01_a
[battle.pause]
[popupdialog(dialogHead="$avatar_izdoc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]本次作战，带上我从四面八方召集来的帮手，去攻占罗德岛的防御系统！
[tutorial(focusWidth=120, focusHeight=120, animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", protectTime=2, dialogHead="$avatar_izdoc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=5, tileX=3)]这就是防御系统的关键节点——原型之手。摧毁了它们，罗德岛的战力就会大打折扣。
[popupdialog(dialogHead="$avatar_izdoc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]我方人员会在入场后朝着最近的原型之手移动。
[popupdialog(dialogHead="$avatar_izdoc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]先发起一轮试探性进攻吧，让我看看你的实力。
[end]
```

### training_act7fun_01_b

```
[header(is_tutorial=true,is_autoable=false, is_skippable=false)]training_act7fun_01_b
[battle.pause]
[tutorial(focusWidth=120, focusHeight=120, animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", protectTime=2, dialogHead="$avatar_izdoc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=5, tileX=3)]这边的原型之手已经拿下！本次行动初步目标已经达成。
[popupdialog(dialogHead="$avatar_izdoc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]不过另外一边似乎还没能拿下，罗德岛防守得还不赖啊。为了突破防守，你还得知道下面这些。
[popupdialog(dialogHead="$avatar_izdoc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]每击倒一位罗德岛干员，我方都会回复大量部署费用，方便继续部署我方单位。
[popupdialog(dialogHead="$avatar_izdoc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]除此以外，每次作战都会有优秀强大的我方干员加入战斗，指挥他们帮你完成任务！
[popupdialog(dialogHead="$avatar_izdoc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]注意配合我，一起解决那边剩下的目标！
[end]
```


## 统计

- 总字符数：33284
- 对话行数：73


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
