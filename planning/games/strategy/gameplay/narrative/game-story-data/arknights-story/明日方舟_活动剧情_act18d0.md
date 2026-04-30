# 明日方舟 · 活动剧情 · act18d0（18段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act18d0」完整剧情脚本（18个文件，2642行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act18d0
- 脚本文件数：18

### level_act18d0_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 1上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
现代 
2:48 P.M.  天气/晴     
萨尔贡中部，伊巴特地区，无名城镇
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Character(name="char_304_hvrain",fadetime=1,block=true)]
[Delay(time=1)]
[name="暴雨"]  ......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_indoor4",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_304_hvrain")]
[name="暴雨"]  没有人。（......还是没见到人影，他们不会有事吧......？）
[Character(name="char_304_hvrain", name2="char_379_sesa_1#4", focus=2)]
[name="慑砂"]  怪了，说好的接头地点就是这里吧？
[Character(name="char_304_hvrain", name2="char_379_sesa_1#4", focus=1)]
[name="暴雨"]  坐标没错。
[Character(name="char_304_hvrain", name2="char_379_sesa_1", focus=2)]
[name="慑砂"]  说不准是遇到沙尘暴耽搁了吧，不着急。
[Character(name="char_304_hvrain#4", name2="char_379_sesa_1", focus=1)]
[name="暴雨"]  慑砂......这样不太好。
[Character(name="char_304_hvrain#4", name2="char_379_sesa_1", focus=2)]
[name="慑砂"]  哎，接头的人还没来，我们这么严肃干嘛，大眼瞪小眼？
[Character(name="char_304_hvrain#4", name2="char_379_sesa_1", focus=1)]
[name="暴雨"]  ......那也不要玩游戏机。你怎么带来的？
[Character(name="char_304_hvrain#4", name2="char_379_sesa_1", focus=2)]
[name="慑砂"]  无所谓啦——
[Character(name="char_304_hvrain", name2="char_379_sesa_1", focus=1)]
[name="暴雨"]  ......也许情况不对。至少该有一次定时联络的。
[Character(name="char_304_hvrain", name2="char_379_sesa_1#4", focus=2)]
[name="慑砂"]  ......
[Character(name="char_304_hvrain#4", name2="char_379_sesa_1#4", focus=1)]
[name="暴雨"]  ......我们是不是该做点什么？
[Character(name="char_304_hvrain#4", name2="char_379_sesa_1#3", focus=2)]
[name="慑砂"]  别这么着急，我们能做什么呢？最好的办法就是好好在这里待着，等待回音。
[Character(name="char_304_hvrain#3", name2="char_379_sesa_1#3", focus=1)]
[name="暴雨"]  但......这太久了。
[Character(name="char_304_hvrain#2", name2="char_379_sesa_1#3", focus=1)]
[name="暴雨"]  等等，有——
[Character(name="char_304_hvrain#2", name2="char_379_sesa_1#3", focus=-1)]
[dialog]
[PlaySound(key="$dooropenquite", volume=0.6)]
[character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_172_1#4",fadetime=1,block=true)]
[Delay(time=1.2)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1.5, block=true)]
[delay(time=2.5)]
[name="？？？"]  （萨尔贡语）早安，二位。
[Dialog]
[Character(name="char_empty", name2="avg_npc_172_1#4")]
[PlaySound(key="$e_skill_skulsrsword", volume=0.6)]
[characteraction(name="left", type="move", xpos=200, fadetime=0.5, block=false)]
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1#4",fadetime=0.5)]
[delay(time=1)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=0.4)]
[Character(name="char_304_hvrain#4", name2="char_379_sesa_1#3", focus=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="慑砂"]  暴雨！慢着！
[Character(name="char_304_hvrain#4", name2="char_379_sesa_1#3", focus=1)]
[characteraction(name="left", type="move", xpos=-100, fadetime=1, block=true)]
[name="暴雨"]  唔——
[delay(time=0.6)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[dialog]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[character]
[Character(name="char_304_hvrain#3")]
[name="暴雨"]  抱、抱歉，下意识就攻击了......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_172_1#4",fadetime=1,block=true)]
[Delay(time=1)]
[name="？？？"]  （萨尔贡语）喔，与外表不同，真是一位激动的小姐，可这样只会毁坏大家的第一印象......
[name="？？？"]  （萨尔贡语）这里是沁礁黑市，大家都是生意人。我相信我们有话可说，不必兵戈相向吧？
[Character(name="avg_npc_172_1#4", name2="char_379_sesa_1", focus=2)]
[name="慑砂"]  （萨尔贡语）今天是什么日子？“沙卒”怎么会在这里？
[Character(name="avg_npc_172_1#4", name2="char_379_sesa_1", focus=1)]
[name="“沙卒”"]  （萨尔贡语）唔，你认得我？
[Character(name="avg_npc_172_1#4", name2="char_379_sesa_1", focus=2)]
[name="慑砂"]  （萨尔贡语）沁礁黑市的头号情报贩子，伊巴特绝大部分武装冲突的幕后黑手，当地人称他为“祖祖”。
[name="慑砂"]  （萨尔贡语）在古老的语言里，是符咒，或者护身符的意思——
[name="慑砂"]  （萨尔贡语）——但我知道你的公开代号是什么，“沙卒”，你可是个大人物，来这里想做什么？
[Character(name="avg_npc_172_1#4", name2="char_379_sesa_1", focus=1)]
[name="“沙卒”"]  （萨尔贡语）别这么说，我只是想和二位谈谈。和......嗯，罗德岛谈谈。
[name="“沙卒”"]  （萨尔贡语）还是说......我打扰了各位原本的行程？
[Character(name="char_304_hvrain#2", name2="avg_npc_172_1#4", focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="暴雨"]  ......！
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1#4", focus=1)]
[name="暴雨"]  （萨尔贡语）......我们的干员在哪里？
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1#4", focus=2)]
[name="“沙卒”"]  哦......原来这位小姐也是萨尔贡人，不错，那我们就开门见山吧。
[name="“沙卒”"]  你们的干员平安无事。你们的那批实验性药物材料......也纹丝未动。
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1#4", focus=1)]
[name="暴雨"]  ......他们在哪里？
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1#4", focus=2)]
[name="“沙卒”"]  ......谁知道呢。
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1#4", focus=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="暴雨"]  你——
[Character(name="char_304_hvrain#4", name2="char_379_sesa_1#3", focus=2)]
[name="慑砂"]  暴雨，别激动！
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1#4", focus=2)]
[name="“沙卒”"]  说得对，别激动，你们还没有在这里与我发生冲突的资本。
[name="“沙卒”"]  比起那批价格不菲的药物原料，几个来路不明的搬运工对我来说可没什么价值......
[Character(name="char_304_hvrain", name2="avg_npc_172_1#4", focus=1)]
[name="暴雨"]  你盯上了那批原料。
[Character(name="char_304_hvrain", name2="avg_npc_172_1#4", focus=2)]
[name="“沙卒”"]  ......如果我点头了呢？
[Charac

... (全文32119字符)
```

### level_act18d0_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 1下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
二十二年前  
3:09 P.M.  天气/晴     
萨尔贡中部，伊巴特地区
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_deserttownD",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_007")]
[name="河刃小队佣兵"]  顾问。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_007", focus=1)]
[name="凯尔希"]  确认回收目标，在其他小队联手堵截我们之前，离开这里。
[Character(name="avg_npc_171_1")]
[name="艾利奥特"]  ......
[Character(name="char_003_kaltsn07_1", name2="avg_npc_007", focus=2)]
[name="河刃小队佣兵"]  ......明白。
[playsound(key="$d_gen_transmissionget", volume=0.6)]
[dialog]
[Character(name="avg_npc_007")]
[name="河刃小队佣兵"]  这里是行动队，高级行动顾问已经回收了“沙卒”小队的幸存者及目标物品。
[name="河刃小队佣兵"]  ......收到。
[playsound(key="$transmission", volume=0.4)]
[dialog]
[Character(name="char_003_kaltsn07_1", name2="avg_npc_007", focus=2)]
[name="河刃小队佣兵"]  顾问，侦查队已经确保路线安全。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_007", focus=1)]
[name="凯尔希"]  那么，出发吧。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Character(name="char_003_kaltsn07_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="凯尔希"]  ......
[Character(name="avg_npc_007")]
[name="河刃小队佣兵"]  ......
[Character(name="avg_npc_171_1")]
[name="艾利奥特"]  ......
[Character(name="avg_npc_171_1", name2="avg_npc_007", focus=2)]
[name="河刃小队佣兵"]  唔，艾利奥特先生，请把那个箱子给我们。
[Character(name="avg_npc_171_1#8", name2="avg_npc_007", focus=1)]
[name="艾利奥特"]  ......！
[dialog]
[character]
少年抱紧了手里的箱子。
[dialog]
[Character(name="char_003_kaltsn07_1", name2="avg_npc_007", focus=2)]
[name="河刃小队佣兵"]  ......顾问？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_007", focus=1)]
[name="凯尔希"]  随他去吧。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_007", focus=2)]
[name="河刃小队佣兵"]  恕我直言，我们应当确认目标物品是否完好，并且保证“无论什么情况下”，它都在我们的掌控之中。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_007", focus=1)]
[name="凯尔希"]  你觉得他会逃跑？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_007", focus=2)]
[name="河刃小队佣兵"]  不，当然......好吧......听您的。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_007", focus=1)]
[name="凯尔希"]  ......嗯。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$drift", volume=0.6)]
[Character(name="avg_npc_007")]
[name="河刃小队佣兵A"]  唔，为什么停下了？
[Character(name="avg_npc_007", name2="avg_npc_008", focus=2)]
[name="河刃小队佣兵B"]  好像抛锚了。
[Character(name="char_003_kaltsn07_1#3")]
[name="凯尔希"]  ......
[dialog]
[character]
[name="河刃小队佣兵"]  怎么回事？术师呢，来检查一下。
[name="河刃小队佣兵"]  不会是没燃料了吧......离开据点的时候没有人检查？谁负责的？
[name="河刃小队佣兵"]  是顽锤小队的J5负责检查载具的，不过他们全队都去侦查队了，怎么搞？要不要联络他们？
[Character(name="char_003_kaltsn07_1#3", name2="avg_npc_171_1", focus=1)]
[name="凯尔希"]  ......艾利奥特。
[Character(name="char_003_kaltsn07_1#3", name2="avg_npc_171_1", focus=2)]
[name="艾利奥特"]  啊？
[Character(name="char_003_kaltsn07_1#3", name2="avg_npc_171_1", focus=1)]
[name="凯尔希"]  保护好那个箱子，低下头。
[Character(name="char_003_kaltsn07_1#3", name2="avg_npc_171_1#4", focus=2)]
[name="艾利奥特"]  ......什么？
[stopmusic(fadetime=1)]
[dialog]
[character]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=2.5)]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.4)]
[name="河刃小队佣兵"]  什么东西爆炸了——唔啊！
[dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[name="河刃小队佣兵"]  侦查队！？喂，听得到吗？让你们的术师停止施法！是我们，是我们啊！
[dialog]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[Character(name="char_003_kaltsn07_1#3")]
[name="凯尔希"]  Mon3tr。
[Character(name="char_003_kaltsn07_1#3", name2="avg_npc_171_1#7", focus=2)]
[name="艾利奥特"]  你、你手里那东西——
[Character(name="npc_10002")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="Mon3tr"]  （欢快地抖擞身体）
[Character(name="char_003_kaltsn07_1", name2="npc_10002", focus=1)]
[name="凯尔希"]  不，不要着急。
[name="凯尔希"]  保护好这个孩子。
[Character(name="npc_10002")]
[name="Mon3tr"]  （回应）
[Character(name="avg_npc_171_1#7")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="艾利奥特"]  嘶——
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1#8", focus=2)]
[name="艾利奥特"]  到底、到底怎么了！他们不是和你一起的吗！？不是来帮我们的吗！？
[Character(name="char_003_kaltsn07_1")]
[name="凯尔希"]  小心些，Mon3tr。
[dialog]
[character]
[playsound(key="$smallearthquake", volume=0.6)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[delay(time=0.6)]
[Character(name="avg_npc_171_1#7")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="艾利奥特"]  啊——
[Character(name="npc_10002")]
[name="Mon3tr"]  （不满）
[CameraShake(durat

... (全文29687字符)
```

### level_act18d0_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 2上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
十七年前
3:09 P.M.  天气/晴     
乌萨斯，移动城市切尔诺伯格主航道西北侧一百四十七公里，村落
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_snowconutry_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Character(name="avg_npc_168_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="？？？"]  村庄......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[dialog]
[Character(name="avg_npc_081")]
[name="乌萨斯村民"]  快，快，医生说要准备温水！
[name="乌萨斯村民"]  这突然要上哪儿去找温水......问问玛莎，问问她家早上烧的水还有剩的没。
[name="乌萨斯村民"]  皇帝在上，求求您保佑老头子吧......
[Character(name="avg_npc_168_1")]
[name="？？？"]  打扰一下......这里发生什么事了，您说的医生是？
[Character(name="avg_npc_168_1", name2="avg_npc_081", focus=2)]
[name="乌萨斯村民"]  唔，你......您是谁？
[name="乌萨斯村民"]  您从哪里来......您这身打扮，是城里来的？抱歉，抱歉，我们现在得忙着救人......您不介意的话，跟我往这儿走，至少能坐一坐。
[Character(name="avg_npc_168_1", name2="avg_npc_081", focus=1)]
[name="？？？"]  没关系......我就是来找那个医生的。她叫什么？
[Character(name="avg_npc_168_1", name2="avg_npc_081", focus=2)]
[name="乌萨斯村民"]  您......您不会是来......
[Character(name="avg_npc_168_1", name2="avg_npc_081", focus=1)]
[name="？？？"]  她只是一个可疑的医生，你们很信任她吗？
[Character(name="avg_npc_168_1", name2="avg_npc_081", focus=2)]
[name="乌萨斯村民"]  可她......可只有她能救好老头子啦，求求您，我求求您，至少现在，她只是个救人的医生啊。
[Character(name="avg_npc_168_1#5", name2="avg_npc_081", focus=1)]
[name="？？？"]  ......我不是来抓她的。我只是找她有点事。
[name="？？？"]  能为我带路吗？
[Character(name="avg_npc_168_1#5", name2="avg_npc_081", focus=2)]
[name="乌萨斯村民"]  我......我不知道......
[Character(name="avg_npc_168_1#5", name2="avg_npc_081", focus=1)]
[name="？？？"]  我也算是个医生。也许我能帮上忙。
[Character(name="avg_npc_168_1#5", name2="avg_npc_081", focus=2)]
[name="乌萨斯村民"]  哦，看您这身打扮，驮兽也知道您的才学......
[Character(name="avg_npc_168_1#2", name2="avg_npc_081", focus=1)]
[name="？？？"]  ......你可以先告诉凯尔希医生，告诉她，她的学生莉莉娅来探望她了，问问她需不需要帮手。
[Character(name="avg_npc_168_1#2", name2="avg_npc_081", focus=2)]
[name="乌萨斯村民"]  啊，原来您知道医生的名字，您是叫莉莉娅，是吗？好的，好的，真是个好听的名字，您请稍等，我这就去。
[name="乌萨斯村民"]  啊，喂！别忘了让玛莎送温水来！
[Character(name="avg_npc_168_1")]
[name="莉莉娅"]  ......
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_snowconutryinside",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="病患"]  呃，呃啊......
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]  咬紧牙关，坚持住。
[character]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="病患"]  呃啊啊啊——咕——
[PlaySound(key="$rungeneral", volume=0.6)]
[dialog]
[Character(name="avg_npc_168_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="莉莉娅"]  ......凯尔希......
[Character(name="avg_npc_168_1#2")]
[name="莉莉娅"]  ......
[Character(name="avg_npc_168_1#3")]
[name="莉莉娅"]  这是什么情况？
[Character(name="char_003_kalts_1", name2="avg_npc_168_1#3", focus=1)]
[name="凯尔希"]  遭到野兽袭击，应急处理罢了。
[Character(name="char_003_kalts_1#3", name2="avg_npc_168_1#3", focus=1)]
[name="凯尔希"]  刀。
[Character(name="avg_npc_081")]
[name="乌萨斯村民"]  哎，呃......在、在哪里......我找不着......
[Character(name="char_003_kalts_1", name2="avg_npc_168_1#3", focus=2)]
[name="莉莉娅"]  这儿，给。
[Character(name="char_003_kalts_1#2", name2="avg_npc_168_1#3", focus=1)]
[name="凯尔希"]  ......
[Character(name="char_003_kalts_1#2", name2="avg_npc_168_1", focus=2)]
[name="莉莉娅"]  ......感染生物？
[Character(name="char_003_kalts_1", name2="avg_npc_168_1", focus=1)]
[name="凯尔希"]  是的。
[Character(name="char_003_kalts_1", name2="avg_npc_168_1#6", focus=2)]
[name="莉莉娅"]  ......会感染吗？
[Character(name="char_003_kalts_1", name2="avg_npc_168_1#6", focus=1)]
[name="凯尔希"]  大部分感染生物都比人们想象的要干净，看齿痕，应该是附近游荡的獠兽。
[Character(name="char_003_kalts_1", name2="avg_npc_168_1#4", focus=2)]
[name="莉莉娅"]  ......但如果是误触了活性源石的獠兽......
[Character(name="char_003_kalts_1", name2="avg_npc_168_1#4", focus=1)]
[name="凯尔希"]  感染生物也许有办法和各种病菌和平共处，但是人类不行。
[Character(name="char_003_kalts_1#3", name2="avg_npc_168_1#4", focus=1)]
[name="凯尔希"]  情况很严重，不光是源石感染，还有坏死症状。
[character]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="病患"]  痛......好痛......
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  冷静些，深呼吸。
[character]
[name="病患"]  呼——喝——呼——
[Character(name="char_003_kalts_1", name2="avg_npc_168_1#3", focus=2)]
[name="莉莉娅"]  呼吸困难，可能是血栓。都是急性矿石病的症状。
[Character(name="avg_npc_081")]
[name="乌萨斯村民"]  但，但不是身上冒出石头才是矿石病吗！？老头子他这不是没事吗！？
[Character(name="avg_npc_168_1")]
[name="莉莉娅"]  某些情况下，感染源会在血液里迅速循环，不会像普通的矿石病那样出现体表源石结晶，而是在短时间内迅速加剧感染症状。
[Character(name="avg_npc_168_1#6")]
[name="莉莉娅"]  如果不靠药物抑制......唔。
[Character(name="avg_npc_081")]
[name="乌萨斯村民"]  皇帝在上，皇帝在上......
[Character(name="avg_npc_168_1#6")]
[name="莉莉娅"]  ......
[Character(name="char_003_kalts_1#4", name2="avg_npc_168_1#6", focus=1)]
[name="凯尔希"]  ......你学得很多。
[Character(name="char_003_kalts_1", name2="avg_npc_168_1#6", focus=1)]
[name="凯尔希"]  注射器，在那个灰色的药箱里。
[Character(name="char_003_kalts_1", name2="avg_npc_168_1", focus=2)]
[name="莉莉娅"]  给......你都随身带着这种抑制药物吗？
[Character(name="char_003_kalts_1", name2="avg_npc_168_1", focus=1)]
[name="凯尔希"]  总有必要的时候。
[character]
[name="病患"]  等等......咳咳，医、医生......这个，很贵吗？
[Character(name="avg_npc_081")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="乌萨斯村民"]  都什么时候啦！？
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  不贵，不用在意。现在当务之急是抑制你的急性矿石病反应，避免源石结晶粉尘的爆发。
[name="凯尔希"]  你不希望村里的其他人因为你而受难，对吧？
[character]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="病患"]  ......唔！
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]  稳住呼吸，别紧张。
[name="凯尔希"]  你不会有事的。
[character]
[name="病患"]  呃，好

... (全文20384字符)
```

### level_act18d0_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 2下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
十七年前
1:37 P.M.  天气/晴     
乌萨斯中部，松心山谷疗养院，食堂大厅
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sanatorium_dining",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Character(name="char_003_kaltsn09_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="凯尔希"]  先生，您的咖啡。
[dialog]
[character]
[name="老兵模样的人"]  ——新来的？
[Character(name="char_003_kaltsn09_1")]
[name="凯尔希"]  是的，先生。
[character]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="老兵模样的人"]  那该好好问问其他人，我喝咖啡的规矩是什么，给我把咖啡放凉了再端过来！
[name="老兵模样的人"]  你这该死的菲林——呵，菲林人！真让人恶心！我在战场上拼命，可不是为了被一个菲林照顾！
[character]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="老兵模样的人"]  给我滚开！
[dialog]
[PlaySound(key="$bottlebroken", volume=0.6)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[delay(time=1)]
[Character(name="char_003_kaltsn09_1")]
[name="凯尔希"]  ......十分抱歉，先生，是我疏忽了。
[name="凯尔希"]  请不要告诉护工长，我这就去为您重新准备......
[character]
[name="老兵模样的人"]  ......哼！不想丢工作的话，就在三分钟之内给我重新准备好。
[name="老兵模样的人"]  还有......你这眼神是怎么回事，如果你不懂怎么微笑的话，我就撕烂你的脸。
[Character(name="char_003_kaltsn09_1")]
[name="凯尔希"]  请别这样......很抱歉让您不愉快了，我这就去为您重新准备。
[character]
[name="老兵模样的人"]  啐，现在的仆人，只有姿色能看了吗？
[Character(name="char_003_kaltsn09_1#3")]
[name="凯尔希"]  非常抱歉，先生，请不要动怒。
[name="凯尔希"]  这对您的病情很不利。
[character]
[Character(name="avg_npc_082")]
[name="乌萨斯军官"]  滚开！
[Character(name="char_003_kaltsn09_1#3")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="凯尔希"]  是、是，非常抱歉。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_sanatorium_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_003_kaltsn09_1#3",fadetime=1,block=true)]
[Delay(time=1)]
[name="凯尔希"]  ......
[character]
[name="年迈的护工"]  小姑娘？喂，小姑娘！
[Character(name="char_003_kaltsn09_1#2")]
[name="凯尔希"]  您是在叫我吗？
[character]
[name="年迈的护工"]  哎，对咯，小姑娘，刚才的我都看见啦，你可千万别气馁啊。
[name="年迈的护工"]  那位是个纠察队的头子......按理说，那种人啊，是没有资格来疗养院的。
[Character(name="char_003_kaltsn09_1")]
[name="凯尔希"]  他可不是贵族......这样作威作福，就不怕得罪别人？
[character]
[name="年迈的护工"]  据说他在某位侯爵身边很吃香......哎，不光如此，听说这次来疗养院，也不是因为什么“战场上留下的顽疾”，他哪上过战场。
[name="年迈的护工"]  听说是帮侯爵做了什么脏活，被侯爵送来避风头的呐。有这么个靠山，对我们这些下人，当然就肆无忌惮起来。
[Character(name="char_003_kaltsn09_1")]
[name="凯尔希"]  ......侯爵......
[name="凯尔希"]  没想到那样的无赖，竟然也会高攀上一位侯爵老爷。
[character]
[name="年迈的护工"]  可不是！指不定哪天他就被安排成哪里的小老爷啦！穿着光鲜亮丽地坐在老大的办公桌后面......唉。
[name="年迈的护工"]  总之，你可别生气，惹上这种人，可比粘上源石虫还麻烦。像你这么年轻的好姑娘，干嘛要来这个地方工作。
[name="年迈的护工"]  千万别说是我告诉你的呀，也别四处乱打听，不然会惹火上身的！
[Character(name="char_003_kaltsn09_1#2")]
[name="凯尔希"]  是......我明白了，谢谢您。
[character]
[name="年迈的护工"]  唉，你下次见到他，躲远些，天知道他会对你做什么——咦，那是新来的医生？
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_168_1",fadetime=1,block=true)]
[Delay(time=1)]
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1", focus=2)]
[name="莉莉娅"]  ......凯尔希。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1", focus=1)]
[name="凯尔希"]  医生。
[character]
[name="年迈的护工"]  哦，哦，原来你们认识......那不打扰你们啦，现在可不是休息时间，小心些，别让护工长瞅见了。
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[dialog]
[delay(time=1)]
[Character(name="char_003_kaltsn09_1")]
[name="凯尔希"]  ......
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1", focus=2)]
[name="莉莉娅"]  她很关心我们这些新来的，她是个好人。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1", focus=1)]
[name="凯尔希"]  说得对，路易莎医生，我们都不能辜负她。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#6", focus=2)]
[name="莉莉娅"]  一会你还有别的工作吗？我有些话想对你说。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#6", focus=1)]
[name="凯尔希"]  抱歉，医生......我还要去冲一杯新的咖啡，如果那位侯爵的宠儿没有继续找茬的话，我随后就去找你。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1", focus=2)]
[name="莉莉娅"]  那好吧......记得小心些，凯尔希。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_sanatorium_balcony",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_003_kaltsn09_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="凯尔希"]  路易莎医生。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1", focus=2)]
[name="莉莉娅"]  ......现在只有我们两个人，凯尔希，你应该选一个化名。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1", focus=1)]
[name="凯尔希"]  “路易莎”，借用你女儿的名字，这种程度的伪装简直是看不起秘密警察的手段。
[name="凯尔希"]  在他们眼里，我已经死了。而这件事结束之后，我会离开乌萨斯，也许很久都不会回来。
[name="凯尔希"]  不会有人知道大公死于行刺。等他们再次来到大公身旁，只会发现他因衰老而停止了呼吸。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#3", focus=2)]
[name="莉莉娅"]  ......乌萨斯的技术不足以分析你制的毒？
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#3", focus=1)]
[name="凯尔希"]  目前而言，这的确超过了他们对“毒物”的理解范畴。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#2", focus=2)]
[name="莉莉娅"]  ......你的知识究竟能领先乌萨斯多少年？所长？
[Character(name="char_003_kaltsn09_1#3", name2="avg_npc_168_1#2", focus=1)]
[name="凯尔希"]  帝国的进步已经超乎我的想象了，但现在不必讨论这些细节。
[name="凯尔希"]  莉莉娅，你们所希望的仲裁只能以这种方式结束。
[name="凯尔希"]  你们没有办法奢求更进一步的报复，能将大公的荣耀与意义一并抹去的，只有乌萨斯至高无上的皇帝本人。
[Character(name="char_003_kaltsn09_1#3", name2="avg_npc_168_1#6", focus=2)]
[name="莉莉娅"]  ......我知道......
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#6", focus=1)]
[name="凯尔希"]  好。那么，就是这里？
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1", focus=2)]
[name="莉莉娅"]  是的，我们并不知道万尼亚大公身患何种顽疾。
[name="莉莉娅"]  但我从护工长那里了解到，每天下午三点，万尼亚大公会离开他的私人监护室，来到这里休憩。
[name="莉莉娅"]  这场日光浴往往持续到日落，偶尔有客人来访的时候，大公会直接与他们在这里共进晚餐。
[name="莉莉娅"]  我们不可能靠近大公的私房，但是这里......


... (全文15060字符)
```

### level_act18d0_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 3上  
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
十三年前
8:09 P.M.  天气/大雪     
维多利亚边境自治郡，多伦郡，文森特庄园
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_manorgate",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_170_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="文森特伯爵"]  多美妙的风雪夜，先生们女士们，欢迎，欢迎，快请进吧，让佣人们为你掸去风雪，去烤炉边取取暖。
[character]
[name="衣着靓丽的商人"]  伯爵先生，晚上好，真是盛大的晚会。
[Character(name="avg_npc_170_1")]
[name="文森特伯爵"]  欢迎，欢迎，戴安娜女士，能在新年的前夜见到您，是我的荣幸。
[character]
[name="衣着靓丽的商人"]  哪里的话。伯爵先生，您看，这是我从卡西米尔为您带来的礼物。
[Character(name="avg_npc_170_1")]
[name="文森特伯爵"]  多美的吊坠！谢谢您，戴安娜女士，代我向您的丈夫问好，现在，请快去屋里吧，可不能让雪花遮掩了您的美貌。
[character]
[name="衣着靓丽的商人"]  哈，您说话还是这么动听。
[Character(name="avg_npc_170_1#2")]
[name="文森特伯爵"]  哦哦，看看谁来了，这不是“麦田男爵”吗！
[character]
[name="恭敬的男性贵族"]  我可担不起伯爵的赏识，但我还是厚着脸皮来啦！
[Character(name="avg_npc_170_1#3")]
[name="文森特伯爵"]  瞧您说的，我们都发自肺腑地尊敬您呀，谁会不尊敬喂饱自己的人呢，哈哈哈！
[character]
[name="恭敬的男性贵族"]  哎，伯爵说的是，等到来年收成的时候，请赏脸光顾寒舍，多伦郡最大的风车和面粉的香气一定让您流连忘返。
[Character(name="avg_npc_170_1")]
[name="文森特伯爵"]  没问题，这场风雪过后，来年一定会大丰收的吧。
[character]
[name="恭敬的男性贵族"]  承您吉言。
[Character(name="avg_npc_170_1")]
[name="文森特伯爵"]  快进去烤火吧，晚上有您最爱的香料面包——当然，最细腻、最香甜的小麦粉，都是出自您的农场。
[character]
[name="恭敬的男性贵族"]  那您呢？您不进来吗？时间快到了......剩下的客人，就交给佣人们吧。
[Character(name="avg_npc_170_1")]
[name="文森特伯爵"]  也许您说得对，但是没关系，我喜欢亲自迎接我邀请的人，他们都是可爱的人，无论是贵族还是商人，是修士还是士兵。
[Character(name="avg_npc_170_1#3")]
[name="文森特伯爵"]  多伦郡真是个好地方，不是吗？
[character]
[name="恭敬的男性贵族"]  哦，您真是......
[Character(name="avg_npc_170_1#2")]
[name="文森特伯爵"]  喔，我看看，还有亚利桑那家的夫妇，那位可敬的灯塔守望者，还有......嗯？
[dialog]
[character]
[Character(name="char_empty", name2="avg_npc_169_1", focus=2, fadetime=1,block=true)]
[Delay(time=1)]
[characteraction(name="right", type="move", xpos=-20, ypos=0,fadetime=1, block=true)]
[delay(time=1.1)]
[characteraction(name="right", type="move", xpos=-40, ypos=0,fadetime=1, block=true)]
[delay(time=1.1)]
[characteraction(name="right", type="move", xpos=-60, ypos=0,fadetime=1, block=true)]
[delay(time=1.1)]
[Character(name="avg_npc_170_1#3")]
[name="文森特伯爵"]  咳哼。
[dialog]
[Character(name="avg_npc_169_1#2")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[delay(time=1)]
[Character(name="avg_npc_170_1")]
[name="文森特伯爵"]  我听说我最尊敬的同学，那位天生的演说家汤姆森，最近身体抱恙，我不忍心让他冒着风雪赴宴，于是专程派了信使，送去我的祝福——
[name="文森特伯爵"]  不过，我怎么好像在这里——发现了一位偷偷摸摸的可爱信使呢！
[characteraction(name="middle", type="move", xpos=60, ypos=0,fadetime=1, block=true)]
[delay(time=1.1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="文森特伯爵"]  嘿咻！
[Character(name="avg_npc_170_1", name2="avg_npc_169_1#2", focus=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="？？？"]  呀！
[Character(name="avg_npc_170_1#3", name2="avg_npc_169_1#2", focus=1)]
[name="文森特伯爵"]  啊哈，小海蒂，我们有多久没见啦？
[Character(name="avg_npc_170_1#3", name2="avg_npc_169_1#5", focus=2)]
[name="海蒂"]  文森特叔叔，别把我的头发弄乱啦！还有我花了好久才化好的妆！
[Character(name="avg_npc_170_1", name2="avg_npc_169_1#5", focus=1)]
[name="文森特伯爵"]  好，好，哎，小海蒂长大了，都是亭亭玉立的大姑娘了。
[name="文森特伯爵"]  但是！你的父亲可没有告诉过我你今天会来这里，老实和叔叔说吧，你是不是偷偷来的？
[name="文森特伯爵"]  还有，你还年轻着呢，这身打扮要是被你父亲看到了，又得唠叨吧？
[Character(name="avg_npc_170_1", name2="avg_npc_169_1", focus=2)]
[name="海蒂"]  叔叔！我就是不想听他唠叨，才偷偷溜过来的嘛！
[name="海蒂"]  听说今天叔叔邀请了许多名流雅士，我这不是好奇嘛。再说了，爸总让我开开眼界，不要拘泥在课堂上，这不正是个好机会嘛！
[Character(name="avg_npc_170_1#2", name2="avg_npc_169_1", focus=1)]
[name="文森特伯爵"]  真的不是来看看那些青年才俊，期待一次邂逅的？我可听你父亲说了，你最近沉迷那些庸俗的爱情小说，他为此头疼得很。
[Character(name="avg_npc_170_1#2", name2="avg_npc_169_1#2", focus=2)]
[name="海蒂"]  怎、怎、怎么会呢，我又不是那么幼稚的小女孩了，啊哈哈，哈哈。
[Character(name="avg_npc_170_1", name2="avg_npc_169_1#2", focus=1)]
[name="文森特伯爵"]  你父亲说得很好，浪漫主义是好的，但那些带着消费目的来欺瞒生活的真相，用以讨好读者并榨取题材价值的文字，一文不值。
[name="文森特伯爵"]  在这块，整个多伦郡都该向你的父亲学习。
[Character(name="avg_npc_170_1", name2="avg_npc_169_1#2", focus=2)]
[name="海蒂"]  咳咳，叔叔，别说这些话了，我听着都害臊......
[Character(name="avg_npc_170_1", name2="avg_npc_169_1", focus=2)]
[name="海蒂"]  爸爸也真是，年轻时把人都骂了个遍，结果最后自己变成了商人，变成了赚大钱的那个.......学会里的前辈，老是拿他开玩笑，我都烦死了。
[Character(name="avg_npc_170_1", name2="avg_npc_169_1", focus=1)]
[name="文森特伯爵"]  那也是受生活所迫。好啦，就当汤姆森为了你们娘俩吧，他年轻那会，可没少找我抱怨他的怀才不遇，最近他身体怎么样？
[Character(name="avg_npc_170_1", name2="avg_npc_169_1", focus=2)]
[name="海蒂"]  老毛病啦，等到冬天过去，又能活蹦乱跳啦。
[Character(name="avg_npc_170_1", name2="avg_npc_169_1", focus=1)]
[name="文森特伯爵"]  所以你趁着父母没空管你，偷拿了你母亲的衣服，来我这儿参加宴会？
[Character(name="avg_npc_170_1", name2="avg_npc_169_1#2", focus=2)]
[name="海蒂"]  没错——啊，不是，是出于学习目的，遵循家父的指导。
[Character(name="avg_npc_170_1", name2="avg_npc_169_1#2", focus=1)]
[name="文森特伯爵"]  海蒂......
[Character(name="avg_npc_170_1", name2="avg_npc_169_1#3", focus=2)]
[name="海蒂"]  嘿嘿，您就不能当没看见？
[Character(name="avg_npc_170_1#4", name2="avg_npc_169_1#3", focus=1)]
[name="文森特伯爵"]  你这次也太任性了，这大雪天的，万一路上出了什么事，我怎么向你的父亲交代？
[Character(name="avg_npc_170_1#4", name2="avg_npc_169_1", focus=2)]
[name="海蒂"]  哈、哈哈......那叔叔您看，反正已经这么晚了，我总不能再找辆车回去吧？
[Character(name="avg_npc_170_1#3", name2="avg_npc_169_1", focus=1)]
[name="文森特伯爵"]  你这孩子，快进屋去吧，别冻着了。
[Character(name="avg_npc_170_1#3", name2="avg_npc_169_1#3", focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="海蒂"]  好嘞！叔叔最好了！
[Character(name="avg_npc_170_1#3", name2="avg_npc_169_1", focus=2)]
[name="海蒂"]  欸，不过叔叔，您还在等谁呢？还有什么贵客值得叔叔您守在门口当雪人吗？
[Character(name="avg_npc_170_1", name2="avg_npc_169_1", focus=1)]
[name="文森特伯爵"]  哦，是一位出色的拉特兰修士。
[name="文森特伯爵"]  去年你婶婶不知染了什么病，高烧不退，多亏了那位修士，药到病除。
[name="文森特伯爵"]  之后我们成了朋友，我时常前去拜访，这位修士不仅医术高超，在各行各业都有独到的见解，让人大开眼界。
[Character(name="avg_npc_170_1", name2="avg_npc_169_1", foc

... (全文7527字符)
```

### level_act18d0_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 3下 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_manorgate",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="avg_npc_170_1#2",fadetime=1,block=true)]
[Delay(time=1)]
[name="文森特伯爵"]  啊，凯尔希修士，您总算来了。呃，您这身打扮......
[Character(name="char_003_kaltsn08_1", name2="avg_npc_170_1#2", focus=1)]
[name="凯尔希"]  您的邀请令我深感荣幸，但事出突然，修道院没法为我准备一身合适的礼服。只从仓库里翻出了这样一身，希望您不要介意。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_170_1#3", focus=2)]
[name="文森特伯爵"]  唔，我自然不会介意，不如说您的这身打扮十分的......十分的英姿飒爽。
[Character(name="avg_npc_170_1", name2="avg_npc_169_1", focus=1)]
[name="文森特伯爵"]  海蒂也别站着了，快，这位是凯尔希修士，打声招呼，然后快进屋吧。
[Character(name="avg_npc_169_1#2", name2="char_003_kaltsn08_1", focus=1)]
[name="海蒂"]  ————
[Character(name="avg_npc_170_1#2", name2="avg_npc_169_1#2", focus=1)]
[name="文森特伯爵"]  海蒂？
[Character(name="avg_npc_169_1", name2="char_003_kaltsn08_1", focus=2)]
[name="凯尔希"]  海蒂小姐，幸会。
[Character(name="avg_npc_169_1", name2="char_003_kaltsn08_1", focus=1)]
[name="海蒂"]  啊——欸——呃，那个，我叫海蒂——
[Character(name="avg_npc_169_1", name2="char_003_kaltsn08_1", focus=2)]
[name="凯尔希"]  我已经知道了，很可爱的名字。
[Character(name="avg_npc_169_1", name2="char_003_kaltsn08_1", focus=1)]
[name="海蒂"]  ——您就是，凯尔希修士，是吗？我经常听叔叔说起您。
[Character(name="avg_npc_169_1", name2="char_003_kaltsn08_1", focus=2)]
[name="凯尔希"]  是我的荣幸。
[Character(name="avg_npc_169_1#3", name2="char_003_kaltsn08_1", focus=1)]
[name="海蒂"]  ——
[Character(name="char_003_kaltsn08_1", name2="avg_npc_170_1", focus=2)]
[name="文森特伯爵"]  凯尔希修士，您也知道汤姆森先生吧，没错，这位海蒂·汤姆森正是那位古怪家伙的女儿。
[Character(name="avg_npc_169_1#3", name2="char_003_kaltsn08_1", focus=2)]
[name="凯尔希"]  是这样，您的父亲是个值得尊敬的人。
[Character(name="avg_npc_169_1", name2="char_003_kaltsn08_1", focus=1)]
[name="海蒂"]  
[Character(name="char_003_kaltsn08_1", name2="avg_npc_170_1", focus=2)]
[name="文森特伯爵"]  好了，请进吧，修士。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_170_1", focus=1)]
[name="凯尔希"]  再次感谢您的慷慨，文森特阁下。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_manorindoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_175", name2="avg_npc_176", focus=1)]
[name="欢快的女贵族"]  哦，您知道伯爵大人去伦蒂尼姆的事情吗，您去过那座城市吗？
[Character(name="avg_npc_175", name2="avg_npc_176", focus=2)]
[name="微醺的商人"]  别提啦，我曾经大包小包收拾好了，结果天灾信使跑过来说：前面路封啦，都回家吧。
[name="微醺的商人"]  我失魂落魄地回家之后，立刻就生了一场大病呢。
[Character(name="avg_npc_175", name2="avg_npc_176", focus=1)]
[name="欢快的女贵族"]  哎呀，这可真惨。
[Character(name="avg_npc_175", name2="avg_npc_177", focus=2)]
[name="附庸风雅的男人"]   那位大诗人今天来了吗？我私下做了几篇文章，还打算请他品鉴品鉴。
[Character(name="avg_npc_177", name2="avg_npc_176", focus=2)]
[name="微醺的商人"]  算了吧，你忘了汤姆森当着伯爵的面，撕掉过多少个所谓“思想家”的手稿吗？
[Character(name="avg_npc_175", name2="avg_npc_176", focus=1)]
[name="欢快的女贵族"]  哦，我记得。汤姆森可真是毫不留情。他还说过，“思想的碰擦就该是毫不留情的”。真是个可怕的人。
[Character(name="avg_npc_175", name2="avg_npc_176", focus=2)]
[name="微醺的商人"]  锋芒毕露，也不全是好事。
[Character(name="avg_npc_175", name2="avg_npc_176", focus=1)]
[name="欢快的女贵族"]  哎呀，但那样的年轻男人才有魅力，不是吗？意气风发，风流倜傥。
[Character(name="avg_npc_177", name2="avg_npc_176", focus=1)]
[name="附庸风雅的男人"]  我当然承认自己曾经很仰慕那样的汤姆森。不过在伯爵阁下面前，汤姆森还是甩不掉他那一身刻意而为的傲慢。
[Character(name="avg_npc_177", name2="avg_npc_176", focus=2)]
[name="微醺的商人"]  刻意而为？汤姆森吗？
[Character(name="avg_npc_177", name2="avg_npc_176", focus=1)]
[name="附庸风雅的男人"]  那当然，那可是我们敬爱的伯爵。不光是爵位和身份，这些年来，伯爵把他的土地治理得井井有条，我们有目共睹。
[Character(name="avg_npc_177", name2="avg_npc_176", focus=2)]
[name="微醺的商人"]  哦，虽然多伦郡并非伯爵阁下的领土，其实大家是一起治理的呐，不过伯爵阁下这份领头人的名号，倒的确实至名归，我得敬他！
[Character(name="avg_npc_177", name2="avg_npc_176", focus=1)]
[name="附庸风雅的男人"]  不仅如此，伯爵还数次受邀前往伦蒂尼姆，参加那里的盛会。这难道不值得我们这样的小地方——容我承认我们的边境处境——感到自豪吗？
[Character(name="avg_npc_177", name2="avg_npc_176", focus=2)]
[name="微醺的商人"]  嗨，贵族。
[Character(name="avg_npc_175", name2="avg_npc_176", focus=1)]
[name="欢快的女贵族"]  哎呀，别把话题变得这么刻板正经。我们都是维多利亚的子民，不是吗？
[Character(name="avg_npc_175", name2="avg_npc_177", focus=2)]
[name="附庸风雅的男人"]  唉！子民！自从那场匪夷所思的绞刑之后，我们也不知道自己是谁的子民咯！
[Character(name="avg_npc_177", name2="avg_npc_176", focus=2)]
[name="微醺的商人"]  快别这么说。陛下的离去让所有人都感到遗憾，但你瞧，我们今天不还是能在这里举杯畅饮吗？
[Character(name="avg_npc_175", name2="avg_npc_176", focus=1)]
[name="欢快的女贵族"]  就是说，今天是个快乐的日子，别提这么可怕的事情啦——快看，伯爵来了。
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[dialog]
[Character(name="avg_npc_170_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="文森特伯爵"]  我听见你们的话题了，很有趣，理查德，我很想拜见一番您的文章。
[Character(name="avg_npc_170_1", name2="avg_npc_177", focus=2)]
[name="附庸风雅的男人"]  哪里的话，伯爵阁下，我这点功夫和您比起来，那可是小巫见大巫啦。
[Character(name="avg_npc_175", name2="avg_npc_170_1", focus=1)]
[name="欢快的女贵族"]  对呀文森特，你快把你那趟伦蒂尼姆之行，说给各位听听呀。您见着了谁？是哪一位传说中的大公爵吗？
[Character(name="avg_npc_170_1")]
[name="文森特伯爵"]  别着急，别着急各位，晚会才刚刚开始，别忘了，今天是庆祝节日的日子。
[Character(name="avg_npc_170_1#3")]
[name="文森特伯爵"]  容我向各位介绍，我们两位特别的小客人。
[name="文森特伯爵"]  凯尔希修士，请。
[dialog]
[character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_003_kaltsn08_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="凯尔希"]  晚上好，各位尊贵的客人，请允许我向各位报以最诚挚的问候。
[Character(name="avg_npc_175")]
[name="欢快的女贵族"]  什么！您这副面容......居然是位淑女吗，真是太可惜了......
[Character(name="avg_npc_176")]
[name="微醺的商人"]  我看这没什么可惜的吧。凯尔希修士，晚上好。
[Character(name="avg_npc_177")]
[name="附庸风雅的男人"]  哦，哦，凯尔希修士，我似乎听伯爵说起过您，听说您帮过伯爵夫人一把，因此受到了伯爵阁下的赏识？
[Character(name="char_003_kaltsn08_1")]
[name="凯尔希"]  对于伯爵夫人而言，那可不是一件轻松的事情。
[Character(name="avg_npc_175", name2="char_003_kaltsn08_1", focus=1)]
[name="欢快的女贵族"]  快和我们说说您来自何处吧，萨科塔以外的拉特兰修士可不常见，哎呀，何况您这么......有魅力。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_176", focus=2)]
[name="微醺的商人"]  美丽的小姐，您来自哪里？又要去何方？
[Character(name="avg_npc_175", name2="avg_npc_176", focus=1)]
[name="欢快的女贵族"]  我不是正在问嘛，你别插嘴。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_177", focus=2)]
[name="附庸风雅的男人"]  听伯爵说，您是一位栋梁之才，不知道您关于哲学或是艺术，是否有独到的见解？
[Character(name="char_

... (全文23753字符)
```

### level_act18d0_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 4上 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
现代 
3:32 P.M.  天气/晴     
萨尔贡中部，伊巴特地区，无名城镇
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_indoor4",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_304_hvrain#2",fadetime=1,block=true)]
[Delay(time=1)]
[name="暴雨"]  ......你想跟我们走......？
[Character(name="char_304_hvrain")]
[name="暴雨"]  你应该明白，对我们而言，你只是个可疑分子。
[Character(name="char_304_hvrain", name2="avg_npc_172_1", focus=2)]
[name="“沙卒”"]  检查过你的队伍了吗？
[Character(name="char_304_hvrain", name2="char_379_sesa_1#2", focus=2)]
[name="慑砂"]  暴雨？
[Character(name="char_304_hvrain", name2="avg_npc_172_1", focus=1)]
[name="暴雨"]  ......一切正常。
[name="暴雨"]  但我不信任你。
[Character(name="char_304_hvrain", name2="avg_npc_172_1", focus=2)]
[name="“沙卒”"]  嗯嗯，说得好，我当然不值得信任。
[Character(name="char_304_hvrain", name2="avg_npc_172_1", focus=1)]
[name="暴雨"]  你的目的是什么？
[Character(name="char_304_hvrain", name2="avg_npc_172_1", focus=2)]
[name="“沙卒”"]  我的目的是......找到我的目的。
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1", focus=1)]
[name="暴雨"]  你在说什么——
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1", focus=2)]
[name="“沙卒”"]  你们知道吗？伊巴特地区的王酋——曾惨死在火灾之中。
[Character(name="avg_npc_172_1", name2="char_379_sesa_1", focus=2)]
[name="慑砂"]  ......那是两三年前的事了。现任王酋是他的儿子，在伊巴特地区引发了不小的骚动......
[name="慑砂"]  多亏了那场火，我还不得不重新找个老东家，多花几个月时间适应新工作，烦人得很。
[Character(name="avg_npc_172_1#3", name2="char_379_sesa_1", focus=1)]
[name="“沙卒”"]  是啊，是啊，可那是我的最后一个猎物。
[name="“沙卒”"]  织好了网，铺好了陷阱，却没有猎物，我现在，很无所事事啊。
[Character(name="avg_npc_172_1#3", name2="char_379_sesa_1#3", focus=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="慑砂"]  ——
[Character(name="char_304_hvrain#2", name2="avg_npc_172_1#3", focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="暴雨"]  ——你、你杀死了一位王酋......？
[Character(name="avg_npc_172_1#3", name2="char_379_sesa_1#3", focus=2)]
[name="慑砂"]  萨尔贡的军队会找上你——
[Character(name="avg_npc_172_1#3", name2="char_379_sesa_1#5", focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="慑砂"]  ——不，等等，你为什么要告诉我们！？
[Character(name="avg_npc_172_1", name2="char_379_sesa_1#5", focus=1)]
[name="“沙卒”"]  啊，不愧是黑市里的常客。是啊，除了你们和我，没有人知道王酋的死和我有关。
[name="“沙卒”"]  至于萨尔贡的军队嘛......今非昔比，统治伊巴特地区的帕夏，可完全瞧不上这片荒芜的土地。
[name="“沙卒”"]  我想，帕夏应该不会在乎是父亲还是儿子当领主吧，其实我也不是很在乎。
[name="“沙卒”"]  我只是索求他的死亡，很简单的要求。
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1", focus=1)]
[name="暴雨"]  你的目的到底是什么？
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1#5", focus=2)]
[name="“沙卒”"]  复仇。
[name="“沙卒”"]  这个答案太无趣了，所以我从来不会回答。也许这片大地上有一半的人类都有自己复仇的目标，对敌人，对城市，对这片大地，怎么都好。
[name="“沙卒”"]  二十多年过去了，我一直在做这一件事。
[name="“沙卒”"]  权力、地位、财富，这些都是附属品，如果有必要，丢掉就丢掉吧。
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1#3", focus=2)]
[name="“沙卒”"]  或者，我会全部赠送给，“罗德岛”。
[name="“沙卒”"]  这可是前所未有的酬宾了，不是吗？
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1", focus=1)]
[name="暴雨"]  ......
[Character(name="char_304_hvrain#4", name2="avg_npc_172_1", focus=2)]
[name="“沙卒”"]  呵，看来你还是不愿意信任我，谨慎的小姐，你以前是军人吗，萨尔贡的军人？
[Character(name="char_304_hvrain", name2="avg_npc_172_1", focus=1)]
[name="暴雨"]  ——与你无关。
[Character(name="avg_npc_172_1#2")]
[name="“沙卒”"]  你呢，年轻的“桥”？或者我该称呼你如今的名字，“慑砂”？
[Character(name="avg_npc_172_1#2", name2="char_379_sesa_1#5", focus=2)]
[name="慑砂"]  ......
[Character(name="char_304_hvrain", name2="char_379_sesa_1#5", focus=1)]
[name="暴雨"]  慑砂，他不值得信任。
[Character(name="avg_npc_172_1", name2="char_379_sesa_1#2", focus=2)]
[name="慑砂"]  ......你隐瞒了某些很关键的事情吧？
[Character(name="avg_npc_172_1#3", name2="char_379_sesa_1#2", focus=1)]
[name="“沙卒”"]  唔？
[Character(name="avg_npc_172_1#6", name2="char_379_sesa_1#2", focus=1)]
[name="“沙卒”"]  哦......是了，是啊，我怎么把这都忘了......
[name="“沙卒”"]  你们自诩是一个治疗感染者的医疗公司......好吧，我就暂且相信这片大地上还有这么异想天开的一群人吧。
[Character(name="avg_npc_172_1#3", name2="char_379_sesa_1#2", focus=1)]
[name="“沙卒”"]  我是一名感染者。
[name="“沙卒”"]  我拥有足够匹敌王酋的财富，也拥有能够陷害一位王酋的人脉与实力。
[Character(name="avg_npc_172_1", name2="char_379_sesa_1#2", focus=1)]
[name="“沙卒”"]  我用这全部，交换一份治疗机会，怎么样？
[Character(name="char_304_hvrain#2", name2="avg_npc_172_1", focus=1)]
[name="暴雨"]  ——你疯了。
[Character(name="char_304_hvrain#2", name2="avg_npc_172_1#3", focus=2)]
[name="“沙卒”"]  我常这么觉得。
[name="“沙卒”"]  但没有人是不想活命的。我抛弃这一切来寻求治疗，难道不合理吗？
[Character(name="avg_npc_172_1#3", name2="char_379_sesa_1#2", focus=2)]
[name="慑砂"]  不，我想暴雨不是在说这个。
[Character(name="avg_npc_172_1#3", name2="char_379_sesa_1#5", focus=2)]
[name="慑砂"]  你竟然连自己是感染者这件事，都毫不在意......？
[name="慑砂"]  那你到底想在罗德岛得到什么？
[Character(name="avg_npc_172_1#6", name2="char_379_sesa_1#5", focus=1)]
[name="“沙卒”"]  ......
[Character(name="avg_npc_172_1", name2="char_379_sesa_1#5", focus=1)]
[name="“沙卒”"]  好吧，时间也不多了，让我们坦诚相待吧。
[name="“沙卒”"]  我要找“凯尔希”。
[name="“沙卒”"]  也许她会告诉我很多事情，也许她会为我指出一条出路......当然，更多的可能是，她都不会做，狡诈地，把选择权重新交给我。
[name="“沙卒”"]  但就算那样也可以。
[name="“沙卒”"]  在每一位参与当年事件的人都被我逐一清除干净后，我对萨尔贡再无依恋，我迫切地想要离开这块令人作呕的土地。
[name="“沙卒”"]  我需要一个新的开始。
[name="“沙卒”"]  正巧在这个节点上，谁会放过一个出现在自己面前的，过去的影子呢？
[Character(name="char_304_hvrain", name2="avg_npc_172_1", focus=1)]
[name="暴雨"]  ......凯尔希医生和你是什么关系？
[Character(name="char_304_hvrain", name2="avg_npc_172_1", focus=2)]
[name="“沙卒”"]  啊哈......说来话长。
[name="“沙卒”"]  她是我的救命恩人。我很感谢她，发自肺腑。
[Character(name="char_304_hvrain#3", name2="avg_npc_172_1", focus=1)]
[name="暴雨"]  决定权不在我们......
[Character(name="avg_npc_172_1", name2="char_379_sesa_1#2", focus=2)]
[name="慑砂"]  ......三年前，伊巴特王酋在旅途中死于一场大火，那场大火烧光了整座城镇，之后，他的儿子掀起了叛乱，和其他人争夺王酋之位。
[name="慑砂"]  是你做的。
[Character(name="avg_npc_172_1", name2="char_379_sesa

... (全文11012字符)
```

### level_act18d0_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 4下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
二十二年前  
3:09 P.M.  天气/晴     
萨尔贡中部，伊巴特地区，荒漠边缘
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_171_1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="艾利奥特"]  我们......我们还要走多远？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1", focus=1)]
[name="凯尔希"]  你累了的话，我们可以停下。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1", focus=2)]
[name="艾利奥特"]  ......
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1", focus=1)]
[name="凯尔希"]  用不着逞强。
[name="凯尔希"]  从上一次遇袭，载具被毁，到现在已经过了七个小时十四分钟，以你的体格和年纪，能坚持到现在已经难能可贵。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1#8", focus=2)]
[name="艾利奥特"]  ......不需要。
[name="艾利奥特"]  我们......继续走，赶紧离开这里......
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_deserttownD",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1#4", focus=2)]
[name="艾利奥特"]  这里是哪里......？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1#4", focus=1)]
[name="凯尔希"]  离目的地最近的城镇。实际上我们已经进入了这片聚落区域，由多座依赖拖拉设备在荒漠上游移的集市城镇组成。
[name="凯尔希"]  同时这里也是萨尔贡无人区覆盖率最高的地区之一，为偷渡客，赏金猎人和信使们提供了一条通向外界的道路。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Background(image="bg_deserttownD",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1#4", focus=2)]
[name="艾利奥特"]  ......为什么我们不去米诺斯？
[name="艾利奥特"]  我不确定......我不确定比起那些雇佣兵，你到底可信到什么地步......你们有什么区别？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1#4", focus=1)]
[name="凯尔希"]  区别在于你还活着。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1", focus=2)]
[name="艾利奥特"]  ......反正你已经有安排了吧，接下来要怎么做？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1", focus=1)]
[name="凯尔希"]  找到一个可信任的人，我们要靠黑市的手段离开伊巴特。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1", focus=2)]
[name="艾利奥特"]  然后去哪儿？莱塔尼亚？玻利瓦尔？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1", focus=1)]
[name="凯尔希"]  ......在我回答之前，你必须清楚，任何选择都只是逃避的一种方案。
[name="凯尔希"]  你无法生活，无处可去，无路可逃。
[name="凯尔希"]  你是否做好了过去的生活早已支离破碎的觉悟？你是否真的有意识到这一点，而不是在各种突如其来的事件中失了神？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1#8", focus=2)]
[name="艾利奥特"]  ......别总是这么高高在上......
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1#8", focus=1)]
[name="凯尔希"]  如果怒火可以令你清醒的话。
[name="凯尔希"]  我会去更北方的地方，很远，远到足够你远离哥伦比亚和萨尔贡的一切。
[name="凯尔希"]  不得不说，你做得已经非常好了。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1#8", focus=2)]
[name="艾利奥特"]  ......你在挖苦我？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1#8", focus=1)]
[name="凯尔希"]  如果你不是这么年轻的话，你满溢个人情感的种种不成熟举措的确值得上我的挖苦。
[name="凯尔希"]  走吧，天黑之前，我们要找到带我们进入黑市的人选。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1#4", focus=2)]
[name="艾利奥特"]  谁？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1#4", focus=1)]
[name="凯尔希"]  ......还不清楚。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1", focus=2)]
[name="艾利奥特"]  呵，原来还有你不知道的事情？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1", focus=1)]
[name="凯尔希"]  我不否认，但我们很快就能找到他们。
[name="凯尔希"]  只要明白“沁礁之地”的含义和其由来，就不难找到那些散落在集市与人群中的遗民。他们愿意帮助同乡人——只要让他们相信，我们是他们的同胞。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1", focus=2)]
[name="艾利奥特"]  唔......你拿的那是......萨尔贡的金币？
[name="艾利奥特"]  但就这几枚金币能做什么......
[Character(name="char_003_kaltsn07_1#3", name2="avg_npc_171_1", focus=1)]
[name="凯尔希"]  我们会知道的。
[Character(name="avg_npc_165")]
[name="萨尔贡镇民？"]  ......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="萨尔贡镇民？"]  （萨尔贡语）去死吧，哥伦比亚人......！
[Character(name="avg_npc_171_1#7")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="艾利奥特"]  欸，敌——！？
[dialog]
[Character(name="npc_10002")]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[name="Mon3tr"]  （嘶鸣）
[delay(time=1)]
[Character(name="avg_npc_165")]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="萨尔贡镇民？"]  啊啊啊——呃啊啊——这只怪物——哪里冒出来——！
[Character(name="npc_10002")]
[name="Mon3tr"]  （发力）
[delay(time=1)]
[Character(name="avg_npc_165")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="萨尔贡镇民？"]  嘎哈......该死的......为什么......砍不动它......
[Character(name="avg_npc_163")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="路过的萨尔贡镇民"]  怎么了？发生什么——啊，啊，怪物！怪物杀、杀人啦！
[delay(time=0.4)]
[dialog]
[character]
[Character(name="char_003_kaltsn07_1#3", name2="avg_npc_171_1#7", focus=2)]
[name="艾利奥特"]  周围的人都聚集过来了......！喂，怎么回事，这个人是谁？
[Character(name="char_003_kaltsn07_1#3", name2="avg_npc_171_1#7", focus=1)]
[name="凯尔希"]  ......瓦伊凡地区的赏金猎人，看来追猎的范围还在扩大。
[name="凯尔希"]  快点，跟上。
[Character(name="char_003_kaltsn07_1#3", name2="avg_npc_171_1#8", focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="艾利奥特"]  呃，等等——
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_deserttownD",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_003_kaltsn07_1", name2="avg_npc_171_1", focus=2)]
[name="艾利奥特"]  如果我们逃到这么远的地方，但随便哪个路人都可能是杀手

... (全文13889字符)
```

### level_act18d0_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 5上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
二十二年前  
8:05 P.M.  天气/多云     
萨尔贡中部，伊巴特地区，沁礁镇周边
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_nobleN",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_003_kaltsn07_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="凯尔希"]  ......废弃的庭院。这就是你们的家？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=2)]
[name="老伊辛"]  几年前，一位商人建起了这座富丽堂皇的庭院，他却在一次行商旅途中，销声匿迹。是天灾还是人祸，无人知晓。
[name="老伊辛"]  但至少这座庭院成了我们这些无家可归者的庇护所。
[dialog]
[Character(name="avg_npc_165", name2="avg_npc_164", focus=1)]
[name="无家可归者"]  ......老伊辛带来了两个新人。
[name="无家可归者"]  而她的打扮可不像个穷人......
[Character(name="avg_npc_165", name2="avg_npc_164", focus=2)]
[name="衣衫褴褛者"]  我们该小心些......都回去屋里吧，老伊辛的秘密不值得我们深究。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(fadetime=1,block=true)]
[Delay(time=2)]
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=1)]
[name="凯尔希"]  ......这座庭院叫什么？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=2)]
[name="老伊辛"]  （萨尔贡语）“沉睡的萨尔贡”，流浪者都是这么称呼这里的......
[name="老伊辛"]  如同我们的故土，女士。我们安眠在大地最奢华的尸体之上。
[name="老伊辛"]  请耐心等待天明，天明才能离开这里，才能前往沁礁的中央。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=1)]
[name="凯尔希"]  礁石环绕之地。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=2)]
[name="老伊辛"]  是的......在沙海的正中央。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=1)]
[name="凯尔希"]  帕夏和王酋们选择了资源更加丰富的地区重建城市，那是座被遗忘的旧址，一片无法之地。
[name="凯尔希"]  可对于过去生活在那座城市里的人和他们的后代而言，那片土地是无法割舍的。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=2)]
[name="老伊辛"]  您可以在那里雇佣黑工和信使，他们会帮您伪造身份，顺利离开萨尔贡的国境。
[name="老伊辛"]  但......您要去的地方实在是太远太远了，老伊辛可不敢保证您能安然抵达。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=1)]
[name="凯尔希"]  艾利奥特还好吗？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=2)]
[name="老伊辛"]  他睡了，这里很安全。您比我想象的还要关心他，这是您慈悲的象征。
[Character(name="char_003_kaltsn07_1#2", name2="avg_npc_173", focus=1)]
[name="凯尔希"]  ......如果被他听到你这么说，他一定会生气的。
[Character(name="char_003_kaltsn07_1#2", name2="avg_npc_173", focus=2)]
[name="老伊辛"]  哦，老伊辛看得见......看得见那孩子身上的愤怒。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=1)]
[name="凯尔希"]  萨尔贡内乱与冲突频发，我以为你看过的这类人并不少。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=2)]
[name="老伊辛"]  勇猛的复仇者并没有世人所想的那般常见，他们大部分人都在仇恨中沉沦，在怒火中失去理智。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=1)]
[name="凯尔希"]  我能救他这一命，也只能救他这一命。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=2)]
[name="老伊辛"]  是的......老伊辛知道，他的命运在别处......与您那枚金币息息相关。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=1)]
[name="凯尔希"]  为什么是二十二年？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=2)]
[name="老伊辛"]  法术做不到所谓“预言”，没有凡人能摆弄时间——时间是命运之母，而老伊辛只是喜欢和时间打赌。
[Character(name="char_003_kaltsn07_1#3", name2="avg_npc_173", focus=1)]
[name="凯尔希"]  你是说......唔，怎么了？
[delay(time=0.4)]
[Character(name="npc_10002")]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="Mon3tr"]  （不悦的嘶鸣）
[delay(time=0.6)]
[Character(name="avg_npc_173")]
[name="老伊辛"]  啊......多美的生物。
[name="老伊辛"]  老伊辛看得出，看得出你们相依而生，看得出......它是您的伙伴。
[name="老伊辛"]  你们共同走过了很长很长的道路。
[Character(name="char_003_kaltsn07_1", name2="npc_10002", focus=1)]
[name="凯尔希"]  ......去吧，Mon3tr，我们去见见他们。
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=2)]
[name="老伊辛"]  哦......交流......你们心灵相通。
[name="老伊辛"]  老伊辛能感觉到......感觉到您对这只生物的信任，就仿佛它是你唯一的伙伴......
[name="老伊辛"]  可是......您这般悠远的旅途......您却只和这只美丽的生物一同？
[name="老伊辛"]  女士，您的荣耀竟如此孤独？
[Character(name="char_003_kaltsn07_1", name2="avg_npc_173", focus=1)]
[name="凯尔希"]  ......孤独与否并不会影响我的职责。
[name="凯尔希"]  似乎有追兵，我去应对一下。你待在这里，保护好艾利奥特。
[delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[characteraction(name="left", type="move", xpos=-300, fadetime=2,block=false)]
[Character(name="char_empty", name2="avg_npc_173", focus=1)]
[dialog]
[delay(time=2)]
[Character(fadetime=0.6)]
[Character(name="avg_npc_173")]
[name="老伊辛"]  当然，老伊辛有的是躲藏的办法，老伊辛躲藏太多年啦。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2.5, block=true)]
[Background(image="bg_nobleD",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_171_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="艾利奥特"]  凯尔希呢？
[Character(name="avg_npc_173", name2="avg_npc_171_1", focus=1)]
[name="老伊辛"]  敌人来袭，她与她信任的伙伴携手共进。
[Character(name="avg_npc_173", name2="avg_npc_171_1", focus=2)]
[name="艾利奥特"]  你是说那只奇异的生物......
[name="艾利奥特"]  ......你干嘛盯着远方？在担心她吗？
[Character(name="avg_npc_173", name2="avg_npc_171_1", focus=1)]
[name="老伊辛"]  不，老伊辛不担心。她的灵魂强韧而悠久，她使老伊辛相信，死亡都停不下她的旅途。所以老伊辛尊敬她，老伊辛想要询问她......
[Character(name="avg_npc_173", name2="avg_npc_171_1", focus=2)]
[name="艾利奥特"]  ......问什么？
[Character(name="avg_npc_173", name2="avg_npc_171_1", focus=1)]
[name="老伊辛"]  百余年了......老伊辛反复做着同一个梦。
[Character(name="avg_npc_173")]
[name="老伊辛"]  梦见黄沙之中的那座宏伟城市，城市会移动，从那里眺望的天空是清澈的......
[name="老伊辛"]  年轻的帕夏就站在老伊辛身边，面前是一望无际却空无一物的土地。年轻的帕夏在诉说......
[name="老伊辛"]  ......但老伊辛听不见。老伊辛忘记了。老伊辛罪无可赦。
[Character(name="avg_npc_171_1#2")]
[name="艾利奥特"]  （又开始自言自语了......）
[Character(name="avg_npc_173")]
[name="老伊辛"]  老伊辛一直在寻求这个答案。老伊辛一直在等待一个知晓那份荣耀，拥有那份知识的人。
[name="老伊辛"]  所有曾与那座城市有所牵连的人，都活在梦里，有的人遗忘了，大部分人，依旧在怀念自己的故土......
[name="老伊辛"]  ......我们用双手在帕夏的带领下建起了一座城市，一座伟大的城市，尽管天灾毁去了它，但那座城市才是沁礁之地的伊始......
[name="老伊辛"]  伊巴特的萨尔贡人不该遗忘任何关于沁礁之城的片段......可......可老伊辛罪无可赦。老伊辛忘了。
[Character(name="avg_npc_173", name2="avg_npc_171_1#4", focus=2)]
[name="艾利奥特"]  你在等别人告诉你......

... (全文15260字符)
```

### level_act18d0_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 5下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
现代
4:14 P.M.  天气/晴     
萨尔贡中部，伊巴特地区，战区
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_laccolith",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_172_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="“沙卒”"]  ......在最艰苦的日子里，我时常回忆起那个场景。
[name="“沙卒”"]  每当我厌烦了敲打，厌烦了劣质的原料创造不出理想的工具——我就会想起那天的所见所闻。
[Character(name="avg_npc_172_1", name2="char_379_sesa_1#3", focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="慑砂"]  ——你一个人就把这些雇佣兵全都——
[Character(name="char_304_hvrain", name2="char_379_sesa_1#3", focus=1)]
[name="暴雨"]  不，他提前布下了那些......武器，而且它们自行摧毁了......
[Character(name="avg_npc_172_1", name2="char_379_sesa_1#4", focus=2)]
[name="慑砂"]  你真的下得去手啊......这些东西都是你制造的吧......
[Character(name="avg_npc_172_1", name2="char_379_sesa_1#4", focus=1)]
[name="“沙卒”"]  什么样的工匠才会对造物有所眷恋？倾注感情的目的是为了创造更完美的工具，而不是反过来被感情束缚。
[Character(name="char_304_hvrain", name2="avg_npc_172_1", focus=1)]
[name="暴雨"]  你早就有所图谋。
[Character(name="char_304_hvrain", name2="avg_npc_172_1", focus=2)]
[name="“沙卒”"]  解决了对大家都不利的因素，又有什么不好呢？
[Character(name="avg_npc_172_1", name2="char_379_sesa_1#5", focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="慑砂"]  ——呕，焦糊味......
[Character(name="avg_npc_172_1", name2="char_379_sesa_1#5", focus=1)]
[name="“沙卒”"]  可别说罗德岛是和平主义者。
[name="“沙卒”"]  呵......你们当然不是。
[Character(name="avg_npc_172_1", name2="char_379_sesa_1#4", focus=2)]
[name="慑砂"]  ......那天的所见所闻又是指？
[Character(name="avg_npc_172_1", name2="char_379_sesa_1#4", focus=1)]
[name="“沙卒”"]  啊，你们亲眼见过她战斗的样子吗？
[name="“沙卒”"]  她就像把自己的瞳孔放在云端一般掌控着全局。
[Dialog]
[character]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_173", name2="avg_npc_171_1", focus=1)]
[name="老伊辛"]  ......近了。很近了。
[name="老伊辛"]  萨卡兹......魔族，她赢了。她已经赢了。老伊辛就知道会是这个结果......
[Character(name="avg_npc_173", name2="avg_npc_171_1", focus=2)]
[name="艾利奥特"]  咳，你一定要跟着我吗？
[Character(name="avg_npc_173", name2="avg_npc_171_1", focus=1)]
[name="老伊辛"]  这是凯尔希女士的请求，在她离开萨尔贡前，她的话语即是老伊辛的职责。
[Character(name="avg_npc_173", name2="avg_npc_171_1", focus=2)]
[name="艾利奥特"]  ......唔，在那头......？
[dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="翻过山坡，在逐渐习以为常的风沙中， 掺杂着源石火药和鲜血的气息。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="阵风推开纱雾，那只奇异的生物几乎扭曲了太阳的光泽。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="凯尔希就站在那里。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她近乎平静。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[stopmusic(fadetime=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_054",fadetime=1,block=true)]
[Delay(time=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="萨卡兹雇佣兵"]  ——咳，咳哈——
[delay(time=0.6)]
[Character(name="avg_npc_054", name2="char_003_kaltsn07_1", focus=2)]
[name="凯尔希"]  你本可以成为一位战士，萨卡兹的战士，无名者。
[Character(name="avg_npc_054", name2="char_003_kaltsn07_1", focus=1)]
[name="萨卡兹雇佣兵"]  ......我死得其所，术师。
[delay(time=0.3)]
[name="萨卡兹雇佣兵"]  不杀我？
[Character(name="avg_npc_054", name2="char_003_kaltsn07_1", focus=2)]
[name="凯尔希"]  我想——
[dialog]
[Character(name="npc_10002")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=0.4)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="Mon3tr"]  （愤怒的低鸣）
[Character(name="avg_npc_054")]
[name="萨卡兹雇佣兵"]  啧，这怪物......连命我都不要了，连道划痕都见不得吗？
[Character(name="npc_10002")]
[name="Mon3tr"]  （咆哮）
[dialog]
[Character(name="avg_npc_054")]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$bodyfalldown2", volume=0.9)]
[Character(fadetime=1,block=true)]
[Delay(time=2)]
[Character(name="char_003_kaltsn07_1#3")]
[name="凯尔希"]  Mon3tr，够了。
[name="凯尔希"]  他已经重伤濒死。
[Character(name="npc_10002")]
[name="Mon3tr"]  （不满的嘶鸣）
[dialog]
[Character(name="avg_npc_054",fadetime=1,block=true)]
[Delay(time=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="萨卡兹雇佣兵"]  哈......哈......嘁，呸，我们倒是替帕夏省事了......
[Character(name="avg_npc_054", name2="char_003_kaltsn07_1", focus=2)]
[name="凯尔希"]  萨卡兹，你的名字是什么？
[Character(name="avg_npc_054", name2="char_003_kaltsn07_1", focus=1)]
[name="萨卡兹雇佣兵"]  呸......你想听哪个？
[name="萨卡兹雇佣兵"]  告诉我，术师，你说的那个——卡兹戴尔——现在是什么面貌？
[Character(name="avg_npc_054", name2="char_003_kaltsn07_1", focus=2)]
[name="凯尔希"]  还很糟糕。
[name="凯尔希"]  但萨卡兹们在建设家园。
[Character(name="avg_npc_054", name2="char_003_kaltsn07_1", focus=1)]
[name="萨卡兹雇佣兵"]  家......园？魔族，感染者，能拥有那种......咳啊......
[name="萨卡兹雇佣兵"]  我从没离开过萨尔贡......
[Character

... (全文41353字符)
```

### level_act18d0_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 6上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
十三年前
8:09 P.M.  天气/大雪     
维多利亚边境自治郡，多伦郡，文森特庄园
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_manorindoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_170_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="文森特伯爵"]  那是一座伟大的城市，任何维多利亚人都应当抽空去瞻仰那座伟大的城市。
[Character(name="avg_npc_170_1", name2="avg_npc_177", focus=2)]
[name="附庸风雅的男人"]  这么说，我们可敬的公爵们依旧没有讨论出结果？
[Character(name="avg_npc_170_1", name2="avg_npc_177", focus=1)]
[name="文森特伯爵"]  是的，依旧没有，伦蒂尼姆依旧是一座“无主”的城市。
[Character(name="avg_npc_175", name2="avg_npc_170_1", focus=1)]
[name="欢快的女贵族"]  那您是有幸和诺曼底公爵一同游览伦蒂尼姆了吗？
[Character(name="avg_npc_175", name2="avg_npc_170_1", focus=2)]
[name="文森特伯爵"]  可惜，大公爵曾被立法禁止进入伦蒂尼姆，而绅士如公爵阁下，自然不会擅自作出这类僭越之举。我们只好在伦蒂尼姆郊外的舰船上共进晚餐。
[Character(name="avg_npc_170_1", name2="avg_npc_176", focus=2)]
[name="微醺的商人"]  公爵阁下是位怎样的英雄？
[Character(name="avg_npc_170_1", name2="avg_npc_176", focus=1)]
[name="文森特伯爵"]  啊......公爵阁下真是个温和儒雅的贵族，他对经济与政治都有独到的见解，不仅如此，听闻他还精通音律，他个人的收藏室又显示出他对艺术的崇敬之心。
[Character(name="avg_npc_170_1#3", name2="avg_npc_176", focus=1)]
[name="文森特伯爵"]  正因为我们有那么多这样的英雄，维多利亚才能依旧繁荣昌盛呀！
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_manorgarden",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=1)]
[name="凯尔希"]  没有最高统治者的维多利亚，保持了十数年的稳定。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=2)]
[name="海蒂"]  但事实上，几位大公爵暗中掣肘，相互摩擦，他们甚至还......
[name="海蒂"]  如果有那么多贵族会轻易死于食物中毒和狩猎意外，那维多利亚的贵族统治早就崩如散沙了。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=1)]
[name="凯尔希"]  而三年前，你的父亲几乎亲历了此事。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=2)]
[name="海蒂"]  ......是的。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=1)]
[name="凯尔希"]  他的腿受伤了，这不是句谎话。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#5", focus=2)]
[name="海蒂"]  是一位在学术上与爸爸有纠纷的贵族，在一场酒会之后对爸爸下的手。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#5", focus=1)]
[name="凯尔希"]  伪装得很好。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=2)]
[name="海蒂"]  爸爸清楚一些苗头，但他不希望这件事情耽搁情报的输送。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=1)]
[name="凯尔希"]  现在这座庄园里，有多少是汤姆森的人？
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=2)]
[name="海蒂"]  有很多人，例如刚才和您交谈的那几位......在今夜之前，他们都曾在爸爸的别墅露过面。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=1)]
[name="凯尔希"]  ......理查德刚才可没少说你父亲的坏话。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1", focus=2)]
[name="海蒂"]  啊哈哈......可能理查德叔叔有一半说的是真心话吧......他和我爸爸较劲有好多年啦......
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1", focus=1)]
[name="凯尔希"]  但他们依旧聚集在汤姆森身边，你的父亲是个很好的领袖。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1", focus=2)]
[name="海蒂"]  离不开您的指导，凯尔希阁下。
[name="海蒂"]  谁又能想到......当年来到维多利亚的一位拉特兰修士，会成为我们最信任的导师呢。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1", focus=1)]
[name="凯尔希"]  我们目的相同。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=2)]
[name="海蒂"]  凯尔希，他们会相安无事的，我们会相安无事的，对吗？
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=1)]
[name="凯尔希"]  ......海蒂。
[name="凯尔希"]  用你自己的眼睛去看。如果你真的决心走入这片大地，而不再被文明的假象蒙蔽双眼......你得自己去看。
[name="凯尔希"]  安慰的话语毫无意义，你会长大的。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_manorindoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_170_1#4")]
[name="文森特伯爵"]  不过，我倒是在一些不入流的小贵族和那些地痞流氓之间，听说了一些让人不愉快的说法......
[Character(name="avg_npc_175", name2="avg_npc_170_1#4", focus=1)]
[name="欢快的女贵族"]  哎呀，让您不高兴了吗？伯爵阁下？
[Character(name="avg_npc_175", name2="avg_npc_170_1", focus=2)]
[name="文森特伯爵"]  是的......如您所见，各大公爵的礼让与迁就造就了如今的和平繁荣。
[name="文森特伯爵"]  但不可否认的是，即使是哥伦比亚那群野蛮的叛徒，他们也能知晓，维多利亚已经很久没有君王主宰了。
[Character(name="avg_npc_170_1", name2="avg_npc_177", focus=2)]
[name="附庸风雅的男人"]  这有何妨呢？这不正说明我们在以......自己的方式强大吗？
[Character(name="avg_npc_170_1", name2="avg_npc_177", focus=1)]
[name="文森特伯爵"]  你说的没错，理查德，但有一股声音，一些天真的，怀着自己目的的人聚集在了一起，他们提出了一个荒唐的问题......
[name="文森特伯爵"]  他们问，维多利亚当真还有必要去渴求一个新王吗？
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="bg_manorgate",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=2)]
[name="海蒂"]  他们都说，文森特叔叔太懦弱了......
[name="海蒂"]  我们身处边境，却故步自封......明明这正是我们争取到权益的大好机会，但文森特叔叔只知道在庄园里召开宴会。
[name="海蒂"]  这趟伦蒂尼姆之行，也没有任何实质性的成果。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=1)]
[name="凯尔希"]  这不会是你父亲的意见，汤姆森不至于这么愚笨，以至于被激进的风气冲昏了头脑。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=2)]
[name="海蒂"]  但大人们总是这样对爸爸倾诉意见。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=1)]
[name="凯尔希"]  没有任何一个蠢笨的贵族，会受到一位真正的大公爵的召见。
[name="凯尔希"]  你认为，诺曼底公爵真的没有对文森特提出一些威逼利诱的条件吗？
[name="凯尔希"]  地处边境，地广人稀，正意味着这座无人问津的多伦郡尚不在任何庞大势力的影响之下。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=2)]
[name="海蒂"]  ......文森特叔叔他......
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1#4", focus=1)]
[name="凯尔希"]  这位似乎只懂得歌舞升平的贵族，在竭力保持多伦郡的和平。尽管这里的和平......一触即破。
[name="凯尔希"]  恰到好处的傲慢与中庸能遮掩他的想法，即使能揣摩到他真实意图的人寥寥无几。
[name="凯尔希"]  汤姆森不会对一个真正没有胆识和眼力的伯爵如此信任有加，他们看似渐行渐远，但总是殊途同归。
[Character(name="char_003_kaltsn08_1", name2="avg_npc_169_1", focus=2)]
[name="海蒂"]  ......嘿嘿......能听你这么说，真好。
[name="海蒂"]  凯尔希，你不用看那两封信吗？
[Character(name="char_003_kaltsn08_1", name2="av

... (全文17672字符)
```

### level_act18d0_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 6下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_manorgarden",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="npc_10002")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing4", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="avg_npc_077")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="“皇帝的利刃”"]  嘶......！
[name="“皇帝的利刃”"]  这种技巧......！你的肉体强度与你的判断反应截然不符，你究竟是什么东西？
[dialog]
[Character(name="npc_10002")]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="Mon3tr"]  （尖啸）
[dialog]
[character]
[delay(time=0.4)]
[Character(name="char_003_kaltsn08_1#4",fadeitme=1,block=true)]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="凯尔希"]  等等，Mon3tr！
[dialog]
[Character(name="npc_10002")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="Mon3tr"]  （悲鸣）
[Character(name="avg_npc_077")]
[name="“皇帝的利刃”"]  ......你令我屈辱，怪物，这是你应得的。
[name="“皇帝的利刃”"]  呵！
[dialog]
[Character(name="npc_10002")]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="Mon3tr"]  ——
[Dialog]
[PlaySound(key="$bodyfalldown2", volume=0.6)]
[Character(fadetime=1,block=true)]
[Delay(time=1)]
[Character(name="char_003_kaltsn08_1#4")]
[name="凯尔希"]  Mon3tr，调整态势，他已是强弩之末。
[Character(name="avg_npc_077")]
[name="“皇帝的利刃”"]  嘶......呼......嘶......呼......
[delay(time=0.6)]
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=1)]
[name="凯尔希"]  你受伤不轻，内卫。
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=2)]
[name="“皇帝的利刃”"]  彼此，叛国者。你为自己注射了药物......这理应使你剧痛。
[name="“皇帝的利刃”"]  真稀奇。你仿佛一个战士的影子，你有着最优秀的战士所具备的一切素养，但你的力量却必须依赖外物......一只怪物。
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=1)]
[name="凯尔希"]  战斗的痕迹尚可遮掩，但遭你浸染的土地无法恢复原状，你不该这么一意孤行。
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=2)]
[name="“皇帝的利刃”"]  ......你正在恐惧，是的，倘若你真的知晓内卫的秘密，你理当感到恐惧。
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=1)]
[name="凯尔希"]  “每一个内卫都是一个国度”，这种充斥着修饰词语的描述，其实是在谈论一个事实。
[name="凯尔希"]  需要我提醒你吗？你的面具正在破裂。现实维度正对你体内的邪魔产生反应，仪式施加的牢笼出现了裂隙。
[name="凯尔希"]  还是说，你真觉得一位皇帝内卫在伯爵庄园里引发一场恐惧的湮灭，维多利亚会依旧放任不管？
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=2)]
[name="“皇帝的利刃”"]  ......
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=1)]
[name="凯尔希"]  内卫的职责，在于乌萨斯存在的一切理由。
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=2)]
[name="“皇帝的利刃”"]  ......笑话！我岂需要一个叛国者来教训我“职责”一词！
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=1)]
[name="凯尔希"]  那么，你现在所效忠的，是如今的乌萨斯，还是一个伟大的幻影？
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=2)]
[name="“皇帝的利刃”"]  ......
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=1)]
[name="凯尔希"]  告诉我，内卫，不要辱没你的名号。
[name="凯尔希"]  ——告诉我当今的乌萨斯皇帝，究竟是如何对待松心山谷的事件的？
[name="凯尔希"]  难道你敢说，那些叛乱的种子，风波的起因，都是乌萨斯皇帝的授意？
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=2)]
[name="“皇帝的利刃”"]  这一切因你而起！
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$b_char_defboost", volume=0.6)]
[Blocker(a=0, fadetime=1.5, block=false)]
[PlaySound(key="$char_emp", volume=0.6)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[delay(time=1)]
[Dialog]
[Character(name="npc_10002")]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="Mon3tr"]  （咆哮）
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=1)]
[name="凯尔希"]  ——尽管诓骗你自己吧，事实是，年轻的皇帝甚至不知道那里发生的一切。
[name="凯尔希"]  你们认为，皇帝不需要知道。
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=2)]
[name="“皇帝的利刃”"]  ......
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=1)]
[name="凯尔希"]  你，你们在渴求一个逝去的时代。
[name="凯尔希"]  我不去评判这是否正确，但任由一位大公死于政斗，都会成为全新叛乱的苗头。
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=2)]
[name="“皇帝的利刃”"]  这不该由你判断。
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=1)]
[name="凯尔希"]  我能预见他的死带来的种种后果。有些人出于愤怒，谋求所谓的公正而要求他死。为了抹消证据，切断联系而希望他死。
[name="凯尔希"]  而另一些，则希望他活着。希望他继续行他脱离不了的职责，或者，也有人希望以一个活着的人证为踏板，向第三集团军所有的牵扯势力发难。
[name="凯尔希"]  他的死活无关紧要，如何处理一触即发的矛盾，才是重中之重。
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=2)]
[name="“皇帝的利刃”"]  你难道想说......
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", focus=1)]
[name="凯尔希"]  只有让一个平平无奇的乌萨斯刺客，出于个人情感杀死一位她本不可能碰触到的大公，罪行才如同被驮兽吞下的草籽般消化。
[Character(name="char_003_kaltsn08_1#4", name2="avg_npc_077", f

... (全文30189字符)
```

### level_act18d0_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 纯剧情1 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
十七年前
2:44 P.M.  天气/晴
乌萨斯中部，松心山谷疗养院外
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_iceforest_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
嘶——呼——
嘶——
呼——
嘶。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_sanatorium_dining",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_076")]
[name="维特"]  啊，老朋友，你好点了吗。
[name="维特"]  不，不，你躺下吧，我只是来看一看你，我随后就得走。驮兽可不能停下，何况给我套上鞍具的，正是我自己啊。
[name="维特"]  什么？不，当然。我还是您认识的那个年轻人，不是什么财政大臣......
[name="维特"]  摆弄身份又有什么意义呢，我们都在为乌萨斯浩大的大地而努力，为陛下所描摹的那个真正荣誉的未来而努力。
[name="维特"]  我们都是陛下的子民。那些遗忘了这点，还活在暴力过去的人，迟早会成为古旧传统的遗孤。
[name="维特"]  ......抱歉，看来处理政务让我积攒了不少火气。
[name="维特"]  别担心，我也能看到同僚和有志之士的意气风发，也能看到腐朽者的腐朽正在蚕食他们自己，我们会胜利的。
[name="维特"]  军队里的那些跋扈贵族......他们和那些蛀虫很快就会成为陛下脚边的尘土，而我们会将其从陛下的道路上彻底扫除。
[name="维特"]  ......是的。
[name="维特"]  ——帝国的议会正在蜕变。
[name="维特"]  我们要从那些顽冥不化的贵族手里，把那些属于乌萨斯，属于陛下的东西夺回来。
[name="维特"]  我们要把旧时代撕毁、蹂躏、亵渎，我们必须为乌萨斯打开一条新的航道，老朋友——我会去做的。我们都会去做的。即使这将耗费我们的一生。
[name="维特"]  乌萨斯必须改变。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sanatorium_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_003_kaltsn09_1")]
[name="凯尔希"]  今天？
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#3", focus=2)]
[name="莉莉娅"]  原计划是在下周......但今天是最好的机会。
[name="莉莉娅"]  刚才我听护工长说了，财政大臣的到来明显让那个畏首畏尾的懦夫动摇了，尽管那个大臣不愿意见他，但他至少愿意挪窝了。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#3", focus=1)]
[name="凯尔希"]  他在恐惧。而恐惧会使他露出破绽。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#3", focus=2)]
[name="莉莉娅"]  也许他的卫队顾不上布置这场突如其来的会面，他不得不以最仓促的姿态出现在我们的面前......
[name="莉莉娅"]  在乌萨斯另一位要员拜访此地的前后，选择去刺杀大公，是一件非常危险的事情，但这里的大人物从来不少，而大公离开他那座独立园区的次数屈指可数。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#3", focus=1)]
[name="凯尔希"]  我们还没有足够的把握。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#6", focus=2)]
[name="莉莉娅"]  我还没有足够的把握。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#3", focus=2)]
[name="莉莉娅"]  但我相信你有了。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#5", focus=2)]
[name="莉莉娅"]  我甚至愿意相信，你一直能做到。
[Character(name="char_003_kaltsn09_1#2", name2="avg_npc_168_1#5", focus=1)]
[name="凯尔希"]  ......
[Character(name="char_003_kaltsn09_1#2", name2="avg_npc_168_1#3", focus=2)]
[name="莉莉娅"]  告诉我，你还有什么顾虑？
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="莉莉娅"]  我会为你解决，哪怕我——
[Character(name="char_003_kaltsn09_1#2", name2="avg_npc_168_1#3", focus=1)]
[name="凯尔希"]  莉莉娅。
[name="凯尔希"]  我最大的顾虑，就是你能否如我希望地好好活着。
[name="凯尔希"]  无论你如何看待我接下来的话，我依旧得承认，在切尔诺伯格，那些富有理想最热忱也最年轻的科学家们......都牺牲了。
[name="凯尔希"]  我并不是乐意看着他们去死的。莉莉娅，现在我对你也是一样的。
[Character(name="char_003_kaltsn09_1#2", name2="avg_npc_168_1#2", focus=2)]
[name="莉莉娅"]  ......
[Character(name="char_003_kaltsn09_1#2", name2="avg_npc_168_1#6", focus=2)]
[name="莉莉娅"]  ......我做不到，凯尔希。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#6", focus=1)]
[name="凯尔希"]  这件事结束之后，我会去叙拉古，然后前往维多利亚。
[name="凯尔希"]  如果你和我同行......而不是继续你在切尔诺伯格的计划，你也许不必死。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#4", focus=2)]
[name="莉莉娅"]  我无法忍受叛徒踩在我丈夫干涸的血迹上，哪怕一秒。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#4", focus=1)]
[name="凯尔希"]  ......你很自私。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#6", focus=2)]
[name="莉莉娅"]  是的，所以别忘了我最自私的请求......
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#3", focus=2)]
[name="莉莉娅"]  照顾好我的女儿，如果她愿意的话，就教她学医吧。
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#5", focus=2)]
[name="莉莉娅"]  你一定能活下去的，凯尔希。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sanatorium_dining",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_076")]
[name="维特"]  老朋友。
[name="维特"]  今年的冬天很冷，但我相信春天温暖如故。
[name="维特"]  我还记得我们第一次见面的那天，也是初春。在那场激情洋溢的演说之下，你没有欢呼，也没有大笑。
[name="维特"]  我们一眼就发现了对方，当然还有别的人。
[name="维特"]  没有人为一场侵略的成功而感到自豪，欢呼者瞻仰着先皇荣光，却看不见脚下的贫瘠大地，已不允许他人生存。
[dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="维特，春天来临了吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Character(name="avg_npc_076")]
[name="维特"]  我不知道，老朋友。也许吧。
[name="维特"]  今年的春天会来得稍早一些，不过我的天灾信使说，受北方某场强烈的天灾影响，也许过段日子，还会降温。
[name="维特"]  也许我们还会回到冬天。
[dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="我们都不喜欢冬天，对吧？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Character(name="avg_npc_076")]
[name="维特"]  我也不喜欢，老伙计。
[name="维特"]  不过你倒是提醒我了，也许我该戒酒了......不该再用酒精对抗冬天。那只是一种麻痹，喝醉了，还是会冻伤的。
[name="维特"]  但冬天不会长久。
[name="维特"]  只是一场灾难的余波罢了。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sanatorium_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#2", focus=2)]
[name="莉莉娅"]  这是......
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#2", focus=1)]
[name="凯尔希"]  一次永眠。最安全的办法，十分有效，还不至于生效太快，让我们无处可逃。
[name="凯尔希"]  你做好撤离的全部准备了吗？
[Character(name="char_003_kaltsn09_1", name2="avg_npc_168_1#3", focus=2)]
[name="莉莉娅"]  从来到这里的第一天，我就已经做好了全部的准备。
[Ch

... (全文32641字符)
```

### level_act18d0_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 纯剧情2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_srgmarket",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[name="黑市商人"]  喂，都看过来，我们来了个新苦力！你，别发呆了，滚过去。
[dialog]
[Character(name="avg_npc_171_1", fadetime=1,block=true)]
[Delay(time=1)]
[name="艾利奥特"]  ......我是新来的工匠学徒，我叫艾——
[dialog]
[character]
[name="黑市商人"]  好了，闲话少说，都动起来！
[name="黑市商人"]  喂，你，还有你们，随便使唤他。他可是哥伦比亚的高学历分子，比你儿子还年轻！
[name="黑市商人"]  反正他背后没人，和那些被卖来的奴隶差不太多，别弄死了就行。
[name="黑市商人"]  准备工作到死，小学徒。
[Character(name="avg_npc_171_1")]
[name="艾利奥特"]  ......好的。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.2, block=true)]
[Background(image="bg_indoor4",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.2, block=true)]
[Character(name="avg_npc_171_1#6")]
[name="艾利奥特"]  ......伊辛，看！
[Character(name="avg_npc_173", name2="avg_npc_171_1#6", focus=1)]
[name="老伊辛"]  噢......令人惊奇，这是你用偷来的钢材焊接的？它就像一尊艺术品......
[Character(name="avg_npc_173", name2="avg_npc_171_1#3", focus=2)]
[name="艾利奥特"]  别说这么肉麻的话，只是个好看些的消耗品。
[Character(name="avg_npc_173", name2="avg_npc_171_1#3", focus=1)]
[name="老伊辛"]  但你该休息了，你骨折的臂膀刚刚恢复......
[Character(name="avg_npc_173", name2="avg_npc_171_1#6", focus=2)]
[name="艾利奥特"]  没关系。
[name="艾利奥特"]  你知道哪里可以搞到精炼源石吗？
[Character(name="avg_npc_173", name2="avg_npc_171_1#6", focus=1)]
[name="老伊辛"]  沁礁黑市没有赤金解决不了的事情。
[Character(name="avg_npc_173", name2="avg_npc_171_1#6", focus=2)]
[name="艾利奥特"]  ......那让我们拭目以待。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_srgmarket",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_172_1")]
[name="艾利奥特"]  ......漆黑的蝎子死了。
[name="艾利奥特"]  我们做得很好，不是吗？
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=1)]
[name="老伊辛"]  今天......老伊辛听那个走私贡品的小贩说，“沙卒”是新一任的沁礁之主。
[name="老伊辛"]  你认为你是吗？艾利奥特？
[Character(name="avg_npc_173", name2="avg_npc_172_1#6", focus=2)]
[name="艾利奥特"]  ......你希望我是吗？伊辛？
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=2)]
[name="艾利奥特"]  我不是个忘恩负义的人，你是我的长辈，这十多年来，我靠你才能活下来。
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=1)]
[name="老伊辛"]  现在你不需要老伊辛了......
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=2)]
[name="艾利奥特"]  不......也不能这么说，我们的关系很微妙。
[name="艾利奥特"]  要抱怨的话，就去向那个神神秘秘的女人抱怨吧。
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=1)]
[name="老伊辛"]  ......凯尔希......
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=2)]
[name="艾利奥特"]  你还记得她的名字，这些年，你越来越不清醒了，我以为你会忘记很多事情。
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=1)]
[name="老伊辛"]  你找过她吗？
[Character(name="avg_npc_173", name2="avg_npc_172_1#6", focus=2)]
[name="艾利奥特"]  找过。徒劳无功，我最优秀的情报员也没法在哥伦比亚找到一丁点她的情报，何况那家雇佣兵公司在那之后立刻就倒闭了。
[name="艾利奥特"]  研究所也被军方控制，一切资料都被销毁，我甚至找不到任何一个参与者......哥伦比亚把他们藏得很好。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_indoor4",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_172_1",fadetime=1,block=true)]
[delay(time=1)]
[name="“沙卒”"]  伊巴特王酋会在下周途经赤角小镇，呵，多么幽默的命运。
[name="“沙卒”"]  这是一个大好机会——老伊辛，你睡着了吗？
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=1)]
[name="老伊辛"]  ......
[name="老伊辛"]  老伊辛做了一个梦......
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=2)]
[name="“沙卒”"]  又是你的梦。
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=1)]
[name="老伊辛"]  还是那个梦......那个怯薛的脚步踏过冻土与草原，最终来到黄沙之地的梦......
[name="老伊辛"]  但这一次，梦稍有不同......
[name="老伊辛"]  那是帕夏未曾和老伊辛描述过的场景......我看见一个人......她很像......那个凯尔希......她的另一个姿态......
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=2)]
[name="“沙卒”"]  唔。
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=1)]
[name="老伊辛"]  她在。
[name="老伊辛"]  当千百年前怯薛的远征粉碎了旧时代的时候，她就在那儿......
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=2)]
[name="“沙卒”"]  梦说明不了什么。没有任何法术能越过时间窥伺命运，这是你自己说的。
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=1)]
[name="老伊辛"]  ......是的，这只是老伊辛的一个梦......一个没有意义的梦......凯尔希女士不可能和他们有关......但这是否寓意了什么？
[name="老伊辛"]  最后，老伊辛还是梦见了他的帕夏。
[Character(name="avg_npc_173", name2="avg_npc_172_1#6", focus=2)]
[name="“沙卒”"]  哦，这次你的主人又对你说了什么？老忠臣？
[Character(name="avg_npc_173", name2="avg_npc_172_1#6", focus=1)]
[name="老伊辛"]  他......
[name="老伊辛"]  他在梦里......告诉了老伊辛......萨尔贡的方向......
[name="老伊辛"]  ......
[name="老伊辛"]  你打算伏击王酋的队伍。
[Character(name="avg_npc_173", name2="avg_npc_172_1#3", focus=2)]
[name="“沙卒”"]  是的。
[Character(name="avg_npc_173", name2="avg_npc_172_1#5", focus=2)]
[name="“沙卒”"]  还是说，你这位曾经的萨尔贡贵族宠臣，要阻止我对一位王酋的大不敬？
[Character(name="avg_npc_173", name2="avg_npc_172_1#5", focus=1)]
[name="老伊辛"]  ——不敬？
[Character(name="avg_npc_173", name2="avg_npc_172_1#6", focus=2)]
[name="“沙卒”"]  唔。
[Character(name="avg_npc_173", name2="avg_npc_172_1#6", focus=1)]
[name="老伊辛"]  他们腐朽，无能，只知道无意义地伤害血亲，将无辜的萨尔贡人卷入争斗......
[name="老伊辛"]  他们踩踏着沁礁的土地，却干着最低劣的勾当，老伊辛怎会对这种人......表示敬意？
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="老伊辛"]  老伊辛要他们偿还代价，老伊辛想要萨尔贡恢复昔日荣光，而非由这些酒囊饭袋来达成！
[name="老伊辛"]  老伊辛......对了......老伊辛应当去寻找那座黄金之城！
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=2)]
[name="“沙卒”"]  很少看你这么激动，冷静些——
[Character(name="avg_npc_173", name2="avg_npc_172_1", focus=1)]
[name="老伊辛"]  ......是时候了。
[name="老伊辛"]  去吧，孩子，去点一把火，去完成你的复仇。
[name="老伊辛"]  等到风定沙落，等到那座永恒之城从风沙中显露面貌......老伊辛要等到那个时候，要找到那里......
[stopmusic(fadetime=2)]
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[Character(name="char_379_sesa_1")]
[name="慑砂"]  ......就是这儿了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_472_

... (全文12294字符)
```

### training_act18d0_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动18d0教学关_a

[PopupDialog(dialogHead="$avatar_melan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 敌人只有一个，玫兰莎......能够独自解决。

```

### training_act18d0_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动18d0教学关_b

[PopupDialog(dialogHead="$avatar_melan")] 无、无人机？从哪里......？
[Tutorial(focusX=-370, focusY=-110, focusWidth=200, focusHeight=200,\
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
		  dialogHead="$avatar_doberm")] \
这是一些佣兵的特殊作战方式，在战斗中向<@tu.kw>可移动战术机库</>呼叫<@tu.kw>空援无人机</>辅助作战。
[Tutorial(focusX=0, focusY=50, focusWidth=150, focusHeight=150,\
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
		  dialogHead="$avatar_doberm")] \
一旦呼叫完成，战术机库便会派出空援无人机<@tu.kw>直线赶往准星标示的呼叫坐标</>。
[PopupDialog(dialogHead="$avatar_doberm")] 空援无人机<@tu.kw>到达呼叫坐标后</>才会开始作战支援，且<@tu.kw>不再移动</>。
[PopupDialog(dialogHead="$avatar_melan")] 唔......我......我一个人......
[PopupDialog(dialogHead="$avatar_ansel")] 没事的，玫兰莎，我来负责医疗。

```

### training_act18d0_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动18d0教学关_c

[PopupDialog(dialogHead="$avatar_melan")] 我、我们撑住了！可敌人的无人机......怎么不见了......？
[PopupDialog(dialogHead="$avatar_doberm")] 佣兵组织都比较在意作战成本，空援无人机每次携带的燃料有限，<@tu.kw>出发一段时间后就会自动撤退</>。
[PopupDialog(dialogHead="$avatar_ansel")] 要是都这么抠门的话......我们不用管它们不就好了吗？
[PopupDialog(dialogHead="$avatar_doberm")] 它们虽然不会对我方基地生命值产生威胁，但进行作战支援时非常强力且<@tu.kw>不易被攻击</>。
[PopupDialog(dialogHead="$avatar_doberm")] 比如眼前的<@tu.kw>破片型空援无人机</>，攻击造成范围物理伤害，且可以临时削弱我方干员的防御力。
[PopupDialog(dialogHead="$avatar_doberm")] 让擅长对空作战的干员将其提前击落，会让正面作战更加轻松。

```

### training_act18d0_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动18d0教学关_d

[PopupDialog(dialogHead="$avatar_melan")] 啊......前方又有一个佣兵呼叫了空援无人机......！
[PopupDialog(dialogHead="$avatar_jesica")] 玫、玫兰莎小姐，我、我可以来帮你......

```


## 统计

- 总字符数：304622
- 对话行数：2642


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
