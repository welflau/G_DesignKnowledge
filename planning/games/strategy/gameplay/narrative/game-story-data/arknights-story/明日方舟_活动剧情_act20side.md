# 明日方舟 · 活动剧情 · act20side（23段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act20side」完整剧情脚本（23个文件，2881行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act20side
- 脚本文件数：23

### level_act20side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[character(name="char_401_elysm_na_1#9",fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_elevator", channel="slide",loop=true,volume=0.4)]
[delay(time=1)]
[stopsound(channel="slide", fadetime=3)]
[playMusic(intro="$relax_intro", key="$relax_loop", volume=0.4)]
[name="极境"]这可真够危险的，小朋友，你是不是根本不记得你来时的路？
[Character(name="avg_4054_malist_1#3$1")]
[name="斯第奇·画布"]我不是小朋友！
[Character(name="avg_4054_malist_1#5$1")]
[name="斯第奇·画布"]我只是，呃，有点不确定......
[character(name="char_401_elysm_na_1#2")]
[name="极境"]要不是有我这个行家里手带路，你这个小朋友怎么应付得来这么危险的洞窟？就算是我，都感觉到了一丝丝的勉强。
[character(name="char_401_elysm_na_1#1")]
[name="极境"]我说，要不然我们干脆趁机扎营休息一下，眯一觉？你们谁要是不擅长搭帐篷我可以帮忙。
[Character(name="avg_npc_075")]
[name="依娜姆"] 你认真的？在眼下这个情况下？
[character(name="char_401_elysm_na_1#1")]
[name="极境"]空气流动畅通，区域开阔，遮风避雨，温度也算合适，而且还很黑，连戴眼罩都免了。
[character(name="char_411_tomimi_1#5")]
[name="特米米"]唔......极境先生说得有道理！可是罗德岛的这种外勤帐篷我不是很熟悉......
[character(name="char_401_elysm_na_1#1")]
[name="极境"]没问题，我教你，你这种型号很简单的，展开就能用，之后只要把几个锁扣固定住......
[character(name="char_411_tomimi_1#2")]
[name="特米米"]哇！真的欸！好方便！
[character(name="char_401_elysm_na_1#2")]
[name="极境"]后勤部门当初设计这种帐篷的时候，可是专门咨询过我这个野外专家的意见！
[character(name="char_401_elysm_na_1#2")]
[name="极境"]我大方地同意了他们可以用我的名字给这个系列命名，也不知道为什么最后没有采用......
[character(name="char_401_elysm_na_1#5")]
[name="极境"]唔，或许是他们觉得这帐篷还有改进的空间，暂时不值得冠上本专家的名字？真是见外，这点小瑕疵我是不会在意的啦！
[Character(name="avg_npc_075")]
[name="依娜姆"]特米米，一直听说你在罗德岛过得不错，我还挺高兴的，不过现在我开始怀疑了......
[Character(name="avg_npc_075")]
[name="依娜姆"]你们罗德岛的人会在升降梯里搭帐篷睡觉吗？
[character(name="char_411_tomimi_1#4")]
[name="特米米"]呃，主要是极境先生比较特殊......
[Character(name="avg_4054_malist_1#3$1")]
[name="斯第奇·画布"]我再说一遍，这不是普通的升降梯，这是我们杜林人自豪的超方便大升降梯一号！
[character(name="char_401_elysm_na_1#1")]
[name="极境"]嗯，很便于搭帐篷。
[Character(name="avg_4054_malist_1#3$1")]
[name="斯第奇·画布"]你！
[Character(name="avg_npc_075")]
[name="依娜姆"]好了好了，斯第奇，极境，你俩别闹了。还有多久才能到你说的地下城市？
[character(name="char_401_elysm_na_1#1")]
[name="极境"]是啊，小朋友，这升降梯都坐了快半个小时了。
[Character(name="avg_4054_malist_1#6$1")]
[name="斯第奇·画布"]我不是......唉，不得不怀疑，我在部族里听到的那些有关嘉维尔的离谱事迹，你们也都是参与者？
[character(name="char_401_elysm_na_1#9")]
[name="极境"]当然了！那家伙经常揍我！
[Character(name="avg_4054_malist_1#7$1")]
[name="斯第奇·画布"]......要不然你们还是回去吧。
[character(name="char_401_elysm_na_1#10")]
[name="极境"]也不算经常吧，不过三周左右被揍一次还是......
[character(name="char_411_tomimi_1#2")]
[name="特米米"]停！！极境先生只是嘉维尔的普通同事而已，但......
[character(name="char_411_tomimi_1#1")]
[name="特米米"]我可是嘉维尔最在乎的伙伴，阿卡胡拉最强部落“嘉维尔意志”的族长呢！
[Character(name="avg_npc_075")]
[name="依娜姆"]后半句勉强算是真的。
[Character(name="avg_4054_malist_1#8$1")]
[name="斯第奇·画布"]......哈哈，谢谢你们慷慨无私的帮助，这座城市会热情地招待你们。
[Character(name="avg_4054_malist_1#2$1")]
[name="斯第奇·画布"]（小声）但愿你们那些丑死人的轨道机械能派上用场......
[Character(name="avg_npc_075")]
[name="依娜姆"]斯第奇，你说什么？
[Character(name="avg_4054_malist_1#8$1")]
[name="斯第奇·画布"]不，没什么，我说，我们快到了。
[dialog]
[PlaySound(key="$d_avg_elevator", channel="slide",loop=true,volume=0.4)]
[delay(time=1)]
[stopsound(channel="slide", fadetime=3)]
[stopmusic(fadetime=1)]
[PlaySound(key="$d_avg_animal_loop",volume=0.4, channel="HB", loop=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Image(image="30_i01", xScale=1.5, yScale=1.5, x=165, y=252)]
[ImageTween(image="30_i01", fadetime=0.5, xScaleFrom=1.5, yScaleFrom=1.5, xScaleTo=1.4, yScaleTo=1.4, xTo=-20, yTo=-200, duration=8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_unlock",volume=0.5)]
[delay(time=8)]
[Dialog]
[Character(name="avg_4054_malist_1#8$1")]
[name="斯第奇·画布"]各位，欢迎来到际崖城。
[dialog]
[Image(image="30_i01", fadetime=1, xScale=1.4, yScale=1.4, x=-20, y=-200)]
[playMusic(intro="$holiday_intro", key="$holiday_loop", volume=0.4)]
[delay(time=1)]
[ImageTween(image="30_i01", fadetime=0.5, xScaleFrom=1.4, yScaleFrom=1.4, xScaleTo=1.0, yScaleTo=1.0, xTo=0, yTo=0, duration=20)]
[stopsound(channel="HB", fadetime=3)]
[Character(name="avg_4054_malist_1#9$1")]
[name="斯第奇·画布"]探访杜林人城市的机会对于你们地上人来说可不多，更别说是这么一座优美......
[character(name="char_401_elysm_na_1#1")]
[name="极境"]喂喂喂那是什么？！
[Character(name="avg_npc_075")]
[name="依娜姆"]大瀑布？
[character(name="char_411_tomimi_1#2")]
[name="特米米"]是......是大滑梯！！！
[Character(name="avg_4054_malist_1#10$1")]
[name="斯第奇·画布"]不，那不是重点，你们就不能关注一下远处那座带花园的，优美而简约的......
[Character(name="avg_npc_075")]
[name="依娜姆"]杜林人的城市居然是这样的？我还以为会，呃，更......通俗一点儿？
[Character(name="avg_npc_075")]
[name="依娜姆"]神秘的地下宫殿之类的，杂志里是这么写的。
[Character(name="avg_4054_malist_1#9$1")]
[name="斯第奇·画布"]实际上，际崖城在杜林城市之中也足够特殊，因为这是一座由像我这样的传奇设计师们建立的城市。
[Character(name="avg_4054_malist_1#9$1")]
[name="斯第奇·画布"]我的前辈们来到这里，是为了创造一座美与和谐的城市，他们理念的继承者，就是那座优美！而简约！的......
[character(name="char_401_elysm_na_1#1")]
[name="极境"]超级旋转滑梯！！！
[character(name="char_401_elysm_na_1#1")]
[name="极境"]迪伦跟我说阿卡胡拉很好玩，看他一脸坏笑，我还以为那小子骗我，原来是真的啊！！
[character(name="char_411_tomimi_1#3")]
[name="特米米"]哦哦哦好想去看好想去看！下次一定要带嘉维尔也过来玩！
[Character(name="avg_npc_075")]
[name="依娜姆"]不知道这些传说中的杜林人，对做生意有没有兴趣呢？
[Character(name="avg_4054_malist_1#6$1")]
[name="斯第奇·画布"]你们的脑瓜真的明白什么叫简约吗？！我的作品在那堆大破烂面前真的就那么不起眼？！
[Character(name="avg_4054_malist_1#5$1")]
[name="斯第奇·画布"]算了......我大概真的找错人了。
[Dialog]
[delay(time=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[image]
[Background(image="bg_caveentrance",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_1026_gvial2_1#1$1", name2="char_416_zumama_1#1", fadetime=0.7)]
[delay(time=0.7)]
[Character(name="avg_1026_gvial2_1#1$1", name2="char_416_zumama_1#1", focus=1)]
[name="嘉维尔"] 呼，应该就是这附近没错。
[Character(name="avg_1026_gvial2_1#1$1", name2="char_416_zumama_1#1", focus=2)]
[name="森蚺"]我只是听部族

... (全文21075字符)
```

### level_act20side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="30_g1_durinstreet",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$relax_intro", key="$relax_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Dialog]
[Character(name="char_empty", name2="avg_npc_075")]
[name="依娜姆"]别害羞，特米米，很适合你嘛。
[Character(name="char_empty", name2="avg_npc_075",focus=1)]
[dialog]
[characteraction(name="left", type="move", xpos=-500, fadetime=0.3, block=true)]
[delay(time=0.51)]
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075",fadetime=0.7,focus=1)]
[characteraction(name="left", type="move", xpos=50, fadetime=0.5, block=false)]
[delay(time=0.7)]
[name="特米米"]真......真的吗？
[dialog]
[characteraction(name="left", type="move", xpos=450, fadetime=2, block=false)]
[delay(time=2)]
[Character(name="avg_npc_572_1#4$1", name2="avg_npc_075", focus=1)]
[name="特米米"]嘿嘿，这件泳衣我一眼就看中了，是我喜欢的风格！
[Character(name="avg_npc_572_1#4$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]这家店的裁缝可真了不起，居然这么快就能改出适合你身材的款式。
[Character(name="avg_npc_572_1#8$1", name2="avg_npc_075", focus=1)]
[name="特米米"]我、我的身材有什么问题吗？最近我有加大训练运动量的！
[Character(name="avg_npc_572_1#8$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]放心吧，很可爱。
[Character(name="avg_npc_572_1#7$1", name2="avg_npc_075", focus=1)]
[name="特米米"]呼，那就好，我可不想再被笑话尾巴又粗了......依娜姆不去挑挑看泳衣吗？
[Character(name="avg_npc_572_1#7$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]我就算了。我倒是对刚才那个帮裁缝打下手的金属脑袋更感兴趣。
[Dialog]
[character]
[Character(name="char_empty", name2="char_empty")]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[playsound(key="$d_avg_robotwalk", volume=1)]
[Character(name="avg_npc_576_1$1", name2="char_empty",fadetime=0.7)]
[delay(time=1)]
[characteraction(name="left", type="jump", power=5, times=2, fadetime=0.51,block=true)]
[delay(time=0.51)]
[dialog]
[characteraction(name="left", type="move", xpos=600, fadetime=1, block=false)]
[character(fadetime=1)]
[Delay(time=2)]
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]杜林的技术吗......
[Dialog]
[character]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="极境"]真是太高超了！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_573_1$1", name2="char_401_elysm_na_1#3", focus=2)]
[delay(time=0.51)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.51)]
[name="极境"]我从没喝过如此醇美的酒！
[Character(name="avg_npc_573_1$1", name2="char_401_elysm_na_1#3", focus=1)]
[name="微醺的杜林人"]来，兄弟，祝你健康！
[Character(name="avg_npc_573_1$1", name2="char_401_elysm_na_1#3", focus=2)]
[name="极境"]祝我们健康，干杯！老卡尔蜜酿万岁！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075", focus=2)]
[delay(time=0.51)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.51)]
[name="依娜姆"]喂特米米，这个叫极境的......真的靠得住吗？
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075", focus=1)]
[multiline(name="特米米")]呃，极境先生关键时候还是很厉害的，
[Character(name="avg_npc_572_1#6$1", name2="avg_npc_075", focus=1)]
[multiline(name="特米米",end=true)]大概！
[Character(name="avg_npc_572_1#7$1", name2="avg_npc_075", focus=1)]
[name="特米米"]说起来，罗德岛上也有杜林族干员，但他们从来不说自己城市的事情呢。
[Character(name="avg_npc_572_1#7$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]难道杜林族有什么隐藏的秘密？
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075", focus=1)]
[name="特米米"]不，我觉得他们只是不太在意，他们大概更关心中午食堂吃什么。
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]真没想到，我们居然有机会来到建在地下的杜林城市。
[Character(name="avg_npc_572_1#4$1", name2="avg_npc_075", focus=1)]
[name="特米米"]嗯，这或许是让嘉维尔的名字在杜林人里也传播开的大好机会......
[Character(name="avg_npc_572_1#4$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]你这次休假，居然没拉着嘉维尔、祖玛玛和克玛尔一起回来吗？
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075", focus=1)]
[name="特米米"]克玛尔说她想和煌小姐一起练拳。嘉维尔和祖玛玛去出任务了还没回来。
[Character(name="avg_npc_572_1#3$1", name2="avg_npc_075", focus=1)]
[multiline(name="特米米")]嘉维尔最近实在是太累了，让人操心！
[Character(name="avg_npc_572_1#6$1", name2="avg_npc_075", focus=1)]
[multiline(name="特米米",end=true)]真希望她能不要这么勉强自己......
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075", focus=1)]
[name="特米米"]我走之前给她们留了信，把你们发现斯第奇先生的事，还有斯第奇先生说的话都写下来了。
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075", focus=1)]
[name="特米米"]要是她们能借着这个机会回阿卡胡拉休息一下就好了......
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]那两个家伙，还有你，当初二话不说就让我当了这里的大酋长，也该回来看看我勉为其难了这么久的成果吧。
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]说句题外话，你们平时在罗德岛的时候有没有觉得，这个叫极境的，有点烦人？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="char_401_elysm_na_1#1", name2="avg_npc_574_1$1", focus=1)]
[delay(time=0.51)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.51)]
[name="极境"]唔哦哦，完全不同的风味！
[Character(name="char_401_elysm_na_1#1", name2="avg_npc_574_1$1", focus=2)]
[name="大醉的杜林人"]高个子，我看你刚才和那帮喜欢蜜酿的家伙混在一起，听我一句，那就是儿童饮料！
[Character(name="char_401_elysm_na_1#1", name2="avg_npc_574_1$1", focus=2)]
[name="大醉的杜林人"]真正的好东西还得看咱们七号烈酒，来，干杯。
[Character(name="char_401_elysm_na_1#3", name2="avg_npc_574_1$1", focus=1)]
[name="极境"]干杯！
[Character(name="char_401_elysm_na_1#3", name2="avg_npc_574_1$1", focus=1)]
[name="极境"]这香气，是暴雨过后的雨林，地下溶洞中苔藓的味道......!
[Character(name="char_401_elysm_na_1#3", name2="avg_npc_574_1$1", focus=2)]
[name="大醉的杜林人"]啊抱歉，是木头杯子有点发霉了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075", focus=2)]
[delay(

... (全文20733字符)
```

### level_act20side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_caveentrance",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="char_416_zumama_1#1", name2="avg_1026_gvial2_1#10$1", fadetime=0.7)]
[delay(time=0.7)]
[Character(name="char_416_zumama_1#1", name2="avg_1026_gvial2_1#10$1", focus=2)]
[name="嘉维尔"] 有句谚语是怎么说的来着，就是煌总挂在嘴边那句——
[Character(name="char_416_zumama_1#1", name2="avg_1026_gvial2_1#10$1", focus=1)]
[name="森蚺"]两点之间，直线最短。
[Character(name="char_416_zumama_1#1", name2="avg_1026_gvial2_1#10$1", focus=2)]
[name="嘉维尔"] 没错。
[Character(name="avg_npc_074")]
[name="大祭司"] 我有一个大胆的推断，是不是因为你们这些雨林人生在这地方已经足够倒霉了，所以别的方面运气都格外的好。
[Character(name="avg_npc_074")]
[name="大祭司"] 要不然为什么你们至今都还没灭绝？完全说不通。
[Character(name="char_416_zumama_1#1", name2="avg_1026_gvial2_1#3$1", focus=2)]
[name="嘉维尔"] 说明这是一种行之有效的生存方式。
[Character(name="char_416_zumama_1#1", name2="avg_1026_gvial2_1#3$1", focus=1)]
[name="森蚺"]大祭司，杜林的城市是什么样子的？
[Character(name="avg_npc_074")]
[name="大祭司"] 唔......记不得了，说明很无聊。
[Character(name="avg_npc_074")]
[name="大祭司"] 我大概一百多年前在地下世界里待过一阵，现在唯一能回想起来的感觉就是糟糕透顶，到处都是蠢蛋。
[Character(name="avg_npc_074")]
[name="大祭司"] 甚至还没有在河边看源石虫睡觉来得有意思。
[Character(name="avg_npc_074")]
[name="大祭司"] 不过，唔，好吧，年轻人就是该多经历经历。要像我一样好奇心旺盛才行！
[Character(name="avg_npc_074")]
[name="大祭司"] 顺便，下个路口左转，不要往下跳！
[Character(name="char_416_zumama_1#1", name2="avg_1026_gvial2_1#1$1", focus=1)]
[name="森蚺"]大祭司，我们走了多远了？
[Character(name="avg_npc_074")]
[name="大祭司"] 好问题，人生的路没有尽头，只管迈开步子往前走，反正还有我这个老家伙看着你们。
[Character(name="avg_npc_074")]
[name="大祭司"] 哦，要是说离那座城市还有多远的话，如果你们能像我一样穿过石头，那再垂直降落个五六百米就到了。
[Character(name="char_416_zumama_1#1", name2="avg_1026_gvial2_1#2$1", focus=2)]
[name="嘉维尔"] 祖玛玛，你到底是怎么忍受这家伙到现在的？实在太吵了。
[Character(name="char_416_zumama_1#1", name2="avg_1026_gvial2_1#2$1", focus=1)]
[name="森蚺"]一般和机器待在一起的时候他会安静一点。
[Character(name="char_416_zumama_1#1", name2="avg_1026_gvial2_1#3$1", focus=2)]
[name="嘉维尔"] 这把链锯算不算机器？
[Character(name="avg_npc_074")]
[name="大祭司"] 哼！没礼貌！
[dialog]
[character(fadetime=1.5)]
[delay(time=2)]
[Character(name="char_416_zumama_1#5", name2="avg_1026_gvial2_1#1$1", focus=1)]
[name="森蚺"]你看，很有用。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="30_g2_fountainlake",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$dontmaketrouble_intro", key="$dontmaketrouble_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_572_1#2$1", name2="avg_npc_075", focus=1)]
[name="特米米"]这就是......这就是！
[Character(name="avg_npc_572_1#6$1", name2="avg_npc_075", focus=1)]
[name="特米米"]呃，“大水坑”？
[Character(name="avg_npc_572_1#6$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]......先把杜林的取名风格放在一边。
[Character(name="avg_npc_572_1#6$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]这个水上乐园从远处看就已经很惊人了，走近了看更是......！
[Character(name="avg_npc_572_1#6$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]杜林人，平常到底过着一种怎样的生活啊！
[dialog]
[character]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.2, block=true)]
[PlaySound(key="$d_avg_ape",volume=0.4)] 
[Character(name="avg_npc_571_1#14$1")]
[characteraction(name="middle", type="move", xpos=1300 ,ypos=500,fadetime=0, isblock=true)]
[CameraShake(duration=0.2, xstrength=0, ystrength=0, vibrato=0, randomness=0, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[characteraction(name="middle", type="move", xpos=-1300,ypos=-500, fadetime=0.5, isblock=true)]
[PlaySound(key="$d_avg_jump_water", volume=0.5)]
[Effect(name="$e_shuihua", layer = 1)]
[characteraction(name="middle", type="move", xpos=-1300,ypos=500, fadetime=0.5, isblock=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="极境"] 呀吼！！
[Character(name="avg_npc_572_1#1$1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]这家伙，什么时候把泳装都换上了？
[Character(name="avg_npc_572_1#2$1", name2="avg_npc_075", focus=1)]
[name="特米米"]极、极境先生，请小心！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character]
[Character(name="avg_npc_567_1#3$1", name2="avg_npc_571_1#14$1")]
[characteraction(name="right", type="move", xpos=1300 ,ypos=500,fadetime=0, isblock=true)]
[delay(time=0.51)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-1500,ypos=-500, fadetime=0.5, isblock=true)]
[delay(time=0.1)]
[characteraction(name="right", type="jump", xpos=-200, power=0, times=1, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[characteraction(name="left", type="jump", xpos=-150, times=0.5, fadetime=0.3, block=false)]
[PlaySound(key="$fightgeneral",volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[characteraction(name="right", type="jump", xpos=200, power=5, times=1, fadetime=1,block=true)]
[dialog]
[Delay(time=1)]
[Character(name="avg_npc_567_1#3$1", name2="avg_npc_571_1#14$1",focus=2)]
[name="极境"] 唔哦，好危险！你没事吧？酒没洒吧？
[dialog]
[characteraction(name="right", type="move", xpos=200 ,fadetime=0.3, isblock=true)]
[characteraction(name="left", type="move", xpos=150 ,fadetime=0.8, isblock=true)]
[Character(name="avg_npc_567_1#3$1", name2="avg_npc_571_1#14$1",focus=1)]
[name="杜林青年"] ......真是稀奇，没见过的地上人怎么会出现在这里？
[Character(name="avg_npc_567_1#4$1", name2="avg_npc_571_1#14$1",focus=1)]
[name="杜林青年"]而且看上去已经和杜林人一样傻乎乎了。
[Character(name="avg_npc_572_1#1$1", na

... (全文30976字符)
```

### level_act20side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="30_g2_fountainlake",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_571_1#2$1")]
[name="极境"] 谢谢你，特米米，这份恩情回到罗德岛上我一定会还。
[Character(name="avg_npc_572_1#5$1")]
[name="特米米"]我、我不太擅长望风，但我会努力的！
[Character(name="avg_npc_571_1#2$1")]
[multiline(name="极境")]好，我先喝一口尝尝！
[Character(name="avg_npc_571_1#9$1")]
[multiline(name="极境",end=true)]嗯，醋栗酒的口感果然够奇怪，但是......
[Character(name="avg_npc_572_1#2$1")]
[name="特米米"]极境先生，极境！
[Character(name="avg_npc_571_1#7$1")]
[name="极境"] 怎、怎么了？我那些朋友们找过来了？你和他们说我可没喝他们对家的酒——
[Character(name="avg_npc_572_1#1$1")]
[name="特米米"]是斯第奇先生来了！
[Character(name="avg_4054_malist_1#10$1")]
[name="斯第奇·画布"] 呼，找了你们好久了。
[Character(name="avg_4054_malist_1#1$1")]
[name="斯第奇·画布"] 说起来，这家伙怎么会在这里？
[Character(name="avg_npc_567_1#1$1")]
[name="卡奇·叙光"]嗨，斯第奇。
[Character(name="avg_npc_567_1#1$1")]
[name="卡奇·叙光"]我们有多少年没见了？真不够意思，你是不是都没来看过我的“大水坑”？
[Character(name="avg_npc_571_1#4$1")]
[name="极境"] 既然你都过来了，要一起玩吗？冲浪区棒极了！
[Character(name="avg_npc_567_1#1$1")]
[name="卡奇·叙光"]我可以帮你们偷偷把水上滑梯的限流阀打开，让你体验一把真正的......
[Character(name="avg_4054_malist_1#5$1")]
[name="斯第奇·画布"] 不了，我赶时间。
[Character(name="avg_4054_malist_1#1$1")]
[name="斯第奇·画布"] 各位，跟我来吧，既然玩得还算开心，那接下来也该谈正事了。
[Character(name="avg_npc_567_1#2$1")]
[name="卡奇·叙光"]斯第奇，你总是匆匆忙忙，时间还有的是！我们完全可以......
[Character(name="avg_4054_malist_1#2$1")]
[name="斯第奇·画布"] 不，我的“时间”很有限。设计代表卡奇大师身体健康，精力充沛，而我是个矿石病患，可活不了几年。
[Character(name="avg_npc_567_1#4$1")]
[name="卡奇·叙光"]啊，抱歉，我不是那个意思！
[Character(name="avg_npc_567_1#4$1")]
[name="卡奇·叙光"]我只是觉得，我们可以好好聊一次，把当年的误会......
[Character(name="avg_4054_malist_1#6$1")]
[name="斯第奇·画布"] 听好了，卡奇。
[Character(name="avg_4054_malist_1#6$1")]
[name="斯第奇·画布"] 如果你想找认同，际崖城的市民已经够热爱你了，不缺我一个。
[Character(name="avg_4054_malist_1#6$1")]
[name="斯第奇·画布"] 如果你想找存在感，不如再建点超级大水炮之类的玩意，漆成红色也好，粉色也罢，我不拦着你。
[Character(name="avg_4054_malist_1#6$1")]
[name="斯第奇·画布"] 只是别在我这浪费时间了，我永远不可能昧着良心去恭维你那些，哈，“建筑作品”。
[Character(name="avg_4054_malist_1#1$1")]
[name="斯第奇·画布"] 该走了，地上人们，我会和你们讲讲我的规划......
[Character(name="avg_npc_567_1#2$1")]
[name="卡奇·叙光"]等等，斯第奇，听我说——
[Character(name="avg_4054_malist_1#1$1")]
[name="斯第奇·画布"] 卡奇，我对你的唯一建议就是，躲开我。
[Character(name="avg_4054_malist_1#1$1")]
[name="斯第奇·画布"] 我们各走各的路。
[Character(name="avg_npc_567_1#1$1")]
[name="卡奇·叙光"]斯第奇，找机会我们一定要聊聊你刚刚提到的超级大水炮，我很感兴趣。
[Character(name="avg_npc_567_1#5$1")]
[name="卡奇·叙光"]不过，在此之前......你有没有听见什么声音？
[Character(name="avg_4054_malist_1#6$1")]
[name="斯第奇·画布"] 肯定是那帮醉鬼又在犯蠢吧。
[Character(name="avg_npc_567_1#2$1")]
[name="卡奇·叙光"]不对......
[Character(name="avg_npc_075")]
[name="依娜姆"]难道是穹顶......？
[Character(name="avg_npc_567_1#5$1")]
[name="卡奇·叙光"]不可能，请相信我在工程结构上的水平。
[Character(name="avg_npc_572_1#2$1")]
[name="特米米"]那、那是！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_tinnitus", volume=1)]
下坠的感觉。
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="bgs")]
风从耳边吹过，很吵。
听说罗德岛有些奇怪的家伙迷恋这种感觉，搞不懂他们。
至于我？我会从高处往下跳只有一个理由，那就是跳下去才能解决问题。
用拳头也好、用法杖也好、用斧子也好。
面对问题，找到坏蛋，然后解决他。没什么难的，不是吗？
不管即将看见的是什么——
就算斧子崩了，法杖裂了，拳头再也握不紧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=200, g=200, b=200, fadetime=1, block=true)]
总之去做就是了。
[Dialog]
[delay(time=1)]
[name="嘉维尔"]不管是阴谋也好野兽也好蘑菇也好火雨也好，还是其他什么恶心的东西也好！
[name="嘉维尔"]我会全都揍趴下！
[name="森蚺"]喂，嘉维尔，好像不太对，前面的是！
[name="嘉维尔"]啊？
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic(fadetime=1)]
[Character]
[PlaySound(key="$bodyfalldown2", volume=1)]
[PlaySound(key="$d_avg_jump_water", volume=0.9)]
[Background(image="30_g2_fountainlake",screenadapt="coverall")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Effect(name="$e_shuihua", layer = 1,y=-200)]
[Dialog]
[Character(name="char_empty")]
[characteraction(name="middle", type="move", ypos=-400, fadetime=0.8, block=false)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_416_zumama_1#1", fadetime=0.7)]
[delay(time=0.7)]
[Dialog]
[character(fadetime=0.3)]
[delay(time=0.51)]
[Blocker(a=0, r=0, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.2, block=true)]
[Character(name="avg_4055_bgsnow_1#1$1", name2="avg_1026_gvial2_1#1$1")]
[characteraction(name="right", type="move", ypos=1000, fadetime=0, block=false)]
[characteraction(name="left", type="move", xpos=200, fadetime=0, block=false)]
[characteraction(name="left", type="move", ypos=1150, fadetime=0, block=false)]
[Blocker(a=0, r=0, fadetime=0.3, block=true)]
[characteraction(name="right", type="move", ypos=-1800, fadetime=0.8, block=false)]
[characteraction(name="left", type="move", ypos=-1800, fadetime=0.8, isblock=true)]
[character(fadetime=0.5)]
[PlaySound(key="$bodyfalldown2", volume=1)]
[PlaySound(key="$d_avg_jump_water", volume=0.9)]
[Effect(name="$e_shuihua", layer = 1,y=-200)]
[delay(time=2.5)]
[name="鲁珀"]喂，我说，差不多该把我放下来了吧！
[name="嘉维尔"]啊，抱歉。
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[Character(name="avg_4055_bgsnow_1#1$1", name2="avg_1026_gvial2_1#1$1", fadetime=0.7)]
[delay(time=1)]
[Character(name="avg_4055_bgsnow_1#1$1", name2="avg_1026_gvial2_1#1$1", focus=2)]
[name="嘉维尔"]......这是个啥？瀑布？滑梯？
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.2, block=true)]
[PlaySound(key="$d_avg_ape",volume=0.2)] 
[Character(name="avg_npc_573_1$1"

... (全文19634字符)
```

### level_act20side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="30_g11_malistgarden",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$bar_intro", key="$bar_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_4054_malist_1#1$1",fadetime=0.7)]
[delay(time=0.7)]
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_4054_malist_1#1$1",focus=1)]
[name="嘉维尔"] 所以，想要炸掉滑梯重修铁路，就得说服商业代表克罗绮·砖石、工业代表黛柯绮·银币，还有那个叫卡奇的家伙，没错吧？
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_4054_malist_1#1$1",focus=2)]
[name="斯第奇·画布"] 不错，他们的地位最重要，杜林人们也最愿意参考他们的态度来做选择。
[Character(name="avg_1026_gvial2_1#2$1",name2="avg_4054_malist_1#1$1",focus=1)]
[name="嘉维尔"] 你就不能自己去？
[Character(name="avg_1026_gvial2_1#2$1",name2="avg_4054_malist_1#5$1",focus=2)]
[name="斯第奇·画布"] ......
[Character(name="avg_1026_gvial2_1#10$1",name2="avg_4054_malist_1#5$1",focus=1)]
[name="嘉维尔"] 看来你不怎么受欢迎。
[Character(name="avg_1026_gvial2_1#10$1",name2="avg_4054_malist_1#10$1",focus=2)]
[name="斯第奇·画布"] 也不用说得这么直白吧。
[Character(name="avg_1026_gvial2_1#7$1",name2="avg_4054_malist_1#10$1",focus=1)]
[name="嘉维尔"] 听起来麻烦得很，不过，好吧，就当是为了阿卡胡拉。
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_4054_malist_1#10$1",focus=1)]
[name="嘉维尔"] 我该去哪里找他们？
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="char_empty",name2="avg_4054_malist_1#2$1",focus=2)]
[name="斯第奇·画布"] 呼，终于结束了。那个嘉维尔真的好吓人。
[dialog]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_564_1#1$1",name2="avg_4054_malist_1#2$1",fadetime=1.5)]
[delay(time=1.5)]
[Character(name="avg_npc_564_1#1$1",name2="avg_4054_malist_1#2$1",focus=1)]
[name="耶奇·地心"] 看来真的让你得逞了。
[Character(name="avg_npc_564_1#1$1",name2="avg_4054_malist_1#1$1",focus=2)]
[name="斯第奇·画布"]耶奇老头，心满意足了？
[Character(name="avg_npc_564_1#1$1",name2="avg_4054_malist_1#1$1",focus=1)]
[name="耶奇·地心"]不瞒你说，我还挺舍不得“大水坑”的。
[Character(name="avg_npc_564_1#1$1",name2="avg_4054_malist_1#8$1",focus=2)]
[name="斯第奇·画布"]哈！谁让它刚好挡在铁路桥中间呢？不然我还真找不到由头对它动手！
[Character(name="avg_npc_564_1#1$1",name2="avg_4054_malist_1#8$1",focus=1)]
[name="耶奇·地心"]不过，我倒有了个新想法，自从穹顶破碎，瀑布落下，这大滑梯建成也有半年多了。
[Character(name="avg_npc_564_1#9$1",name2="avg_4054_malist_1#8$1",focus=1)]
[name="耶奇·地心"]虽然大家玩得还是高兴得很，但应该也感觉到有一点无聊了。
[Character(name="avg_npc_564_1#10$1",name2="avg_4054_malist_1#8$1",focus=1)]
[name="耶奇·地心"]不如我们就趁这个机会，建点新的？你之前和卡奇好像说过一个超级大水炮之类的东西，已经在杜林人中传开了！
[Character(name="avg_npc_564_1#10$1",name2="avg_4054_malist_1#8$1",focus=1)]
[name="耶奇·地心"]不瞒你说，我也很有兴趣......
[Character(name="avg_npc_564_1#10$1",name2="avg_4054_malist_1#7$1",focus=2)]
[name="斯第奇·画布"]......唉！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="30_g6_reception",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_npc_566_1#1$1",fadetime=0.7)]
[delay(time=0.7)]
[Character(name="avg_4055_bgsnow_1#3$1",name2="avg_npc_566_1#1$1",focus=1)]
[name="阿芙朵嘉"] 那个阿达克利斯人！野蛮、无礼、鲁莽、放肆！克罗绮，你能想象吗？我只不过是创作陷入了瓶颈，想去山洞里采些野茶，散散心......
[Character(name="avg_4055_bgsnow_1#3$1",name2="avg_npc_566_1#8$1",focus=2)]
[name="克罗绮·砖石"] 结果被人抱着从瀑布顶跳了下来。
[Character(name="avg_4055_bgsnow_1#9$1",name2="avg_npc_566_1#8$1",focus=1)]
[name="阿芙朵嘉"] 简直糟糕透顶。
[Character(name="avg_4055_bgsnow_1#9$1",name2="avg_npc_566_1#8$1",focus=2)]
[name="克罗绮·砖石"] 但恐怕没有哪个正常的际崖城居民能抵挡这样的诱惑。如果把它写成故事，说不定能在城里大受欢迎。
[Character(name="avg_4055_bgsnow_1#9$1",name2="avg_npc_566_1#9$1",focus=2)]
[name="克罗绮·砖石"] “相信嘉维尔吧。”“阿芙朵嘉，抓紧我！”唔，还有点浪漫。
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_npc_566_1#9$1",focus=1)]
[name="阿芙朵嘉"] 可算了吧！
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_npc_566_1#5$1",focus=2)]
[name="克罗绮·砖石"] 起码比你那些有关雪的故事强。
[Character(name="avg_4055_bgsnow_1#4$1",name2="avg_npc_566_1#5$1",focus=1)]
[name="阿芙朵嘉"] 说起来，前两天，有几个孩子来找我讨那几本短篇小说，我还以为这些书也终于有了读者......
[Character(name="avg_4055_bgsnow_1#4$1",name2="avg_npc_566_1#1$1",focus=2)]
[name="克罗绮·砖石"] 他们的读后感呢？
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_npc_566_1#1$1",focus=1)]
[name="阿芙朵嘉"] “很好笑，下次还来看。”
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_npc_566_1#2$1",focus=2)]
[name="克罗绮·砖石"] 我就知道。
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_npc_566_1#1$1",focus=2)]
[name="克罗绮·砖石"] 阿芙朵嘉，他们没有恶意。只是，我们杜林人恐怕真的没法想象你的那些经历。
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_npc_566_1#1$1",focus=2)]
[name="克罗绮·砖石"] 我是听你说了多少次才了解一点你的感觉？更何况普通的杜林人了。
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_npc_566_1#1$1",focus=2)]
[name="克罗绮·砖石"] 我们连真正的雪都没见过，更别说你写的那些......那几个词怎么念来着，“诡诈”“逃亡”？
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_npc_566_1#1$1",focus=1)]
[name="阿芙朵嘉"] 那些词如果只存在于文学之中，才再好不过。
[Character(name="avg_4055_bgsnow_1#1$1",name2="avg_npc_566_1#1$1",focus=1)]
[name="阿芙朵嘉"] 总之，我对现在的日子很满意。不压榨别人，也不被人压榨。没有正在酝酿的恐怖阴谋，也不会卷入陷害与刺杀。
[Character(name="avg_4055_bgsnow_1#1$1",name2="avg_npc_566_1#1$1",focus=1)]
[name="阿芙朵嘉"] 我为我们的商店街写几条广告、设计几件标牌就足够填饱肚子。还有什么不满足的呢？
[Character(name="avg_4055_bgsnow_1#1$1",name2="avg_npc_566_1#1$1",focus=1)]
[name="阿芙朵嘉"] 我每天只用悠闲地在躺椅上沐浴阳光——虽然只是人造光源，但足够了。
[Character(name="avg_4055_bgsnow_1#9$1",name2="avg_npc_566_1#1$1",focus=1)]
[name="阿芙朵嘉"] 我真希望这样平静的日子继续下去，直到......
[Character(name="avg_1026_gvial2_1#1$1")]
[name="嘉维尔"]这里是商业代表克罗绮·砖石的办公室吗？
[Character(name="avg_1026_gvial2_1#1$1")]
[name="嘉维尔"]你好，我想把那个大滑梯炸了。
[Character(name="avg_4055_bgsnow_1#4$1",name2="avg_npc_566_1#1$1",focus=1)]
[name="阿芙朵嘉"] ......
[Character(name="avg_4055_bgsnow_1#4$1",name2="avg_npc_566_1#7$1",focus=2)]
[n

... (全文23379字符)
```

### level_act20side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="30_g4_durinsquare",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Dialog]
[Character]
[character(name="avg_npc_576_1$1",fadetime=0.7)]
[Delay(time=1)]
[Characteraction(name="middle", type="move", xpos=100, fadetime=1, block=true)]
[Delay(time=1)]
[Characteraction(name="middle", type="move", xpos=-120, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$getcast")]
[Characteraction(name="middle", type="jump",xpos=20,ypos=-5, power=20, times=1, fadetime=0.3,block=true)]
[Blocker(a=0, r=0, fadetime=0.3, block=true)]
[Characteraction(name="middle", type="jump",xpos=-20,ypos=-5, power=20, times=1, fadetime=0.3,block=true)]
[Blocker(a=0, r=0, fadetime=0.3, block=true)]
[name="奇怪的机械0429"]感觉到，崭新，完整。
[Character(name="char_416_zumama_1#5",fadetime=0)]
[name="森蚺"]哈哈哈，别围着我转了，小家伙。看到你能恢复活力，我也很高兴。
[character(name="avg_npc_576_1$1")]
[name="奇怪的机械0429"]祖玛玛，检修，很擅长。
[character(name="avg_npc_576_1$1")]
[name="奇怪的机械0429"]祖玛玛，请求协助，小小协助。
[character(name="avg_npc_576_1$1")]
[name="奇怪的机械0429"]编号0428，同伴，已退役，交互不响应，请求协助。
[character(name="avg_npc_576_1$1")]
[name="奇怪的机械0429"]与本机一起出厂，共同建造设施，现在，不响应。
[Character(name="char_416_zumama_1#1")]
[name="森蚺"]不响应？
[Character(name="char_416_zumama_1#1")]
[name="森蚺"]你别着急，带我去看看。
[character(name="avg_npc_576_1$1")]
[name="奇怪的机械0429"]祖玛玛，这边。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[name="停止活动的机械"]......
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=1)]
[name="森蚺"]这些结构，这些部件......唔，果然比起单纯的维修而言，难度是要大一些。
[Character(name="char_416_zumama_1#4", name2="avg_npc_576_1$1",focus=1)]
[name="森蚺"]这是什么原理？这个结构又是干什么的？和大姐的身体完全不一样，也从没听可露希尔师父说过类似的东西。
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=1)]
[name="森蚺"]如果接上这里......不，还是小心一点，它也是你的朋友吧？
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=2)]
[name="奇怪的机械0429"]朋友？祖玛玛，多次以朋友定义关系。暂不理解。
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=2)]
[name="奇怪的机械0429"]检修无法执行？
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=1)]
[name="森蚺"]如果能找到些资料的话......
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=2)]
[name="奇怪的机械0429"]资料？图书馆，保存资料。
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=1)]
[name="森蚺"]你能带我去吗？
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=2)]
[name="奇怪的机械0429"]辅助导航，光荣的使命。祖玛玛，这边。
[dialog]
[characteraction(name="right", type="jump", power=5, times=2, fadetime=0.51,block=true)]
[delay(time=0.51)]
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=1)]
[characteraction(name="right", type="move", xpos=1000, fadetime=1, block=false)]
[PlaySound(key="$d_avg_robotwalk")]
[Delay(time=1.2)]
[Dialog]
[characteraction(name="left", type="move", xpos=600, fadetime=1, block=false)]
[character(fadetime=1.2)]
[delay(time=1.5)]
[Character(name="avg_npc_569_1#8$1")]
[name="路过的杜林"]真有意思......
[Character(name="avg_npc_569_1#8$1")]
[name="路过的杜林"]一种我从没在书上见过的交互模式，地上人，值得研究。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="30_g2_fountainlake",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_571_1#1$1", name2="avg_npc_573_1$1",fadetime=0.7)]
[delay(time=1)]
[Character(name="avg_npc_571_1#1$1", name2="avg_npc_573_1$1",focus=2)]
[name="醉醺醺的杜林人"] 极境，我们来比比谁能头朝下最快从超级旋转滑梯上倒着飞出去，怎么样？
[Character(name="avg_npc_571_1#2$1", name2="avg_npc_573_1$1",focus=1)]
[multiline(name="极境")]哈，让你见识见识什么叫罗德岛的水上传说！
[Character(name="avg_npc_571_1#2$1", name2="avg_npc_573_1$1",focus=1)]
[multiline(name="极境",end=true)]棘刺那家伙可是从没在这项目上赢过我！
[dialog]
[character(fadetime=0)]
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#1$1",fadetime=0.7)]
[delay(time=1)]
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#1$1",focus=2)]
[name="斯第奇·画布"]说真的，我没有一点兴趣和你在这里闲逛，我宁愿在该死的阿卡胡拉丛林里被钳兽吃掉。
[Character(name="avg_npc_567_1#2$1", name2="avg_4054_malist_1#1$1",focus=1)]
[name="卡奇·叙光"] 别这么说嘛，斯第奇，我只是真的想听听你的意见。
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#1$1",focus=1)]
[name="卡奇·叙光"] 不管际崖城的其他居民怎么认为，我知道谁才是优秀的建筑设计师——无论是你的那位老师，还是你，都当之无愧。
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#1$1",focus=1)]
[name="卡奇·叙光"] 这座际崖城了不起的穹顶，我从没在杜林的任何一本建筑学书籍中看过类似的设想，如果你能愿意......
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#1$1",focus=2)]
[name="斯第奇·画布"]如果你把我叫来就是为了这种事，那我建议我们还是不要浪费彼此的时间了。
[Character(name="avg_npc_567_1#2$1", name2="avg_4054_malist_1#1$1",focus=1)]
[name="卡奇·叙光"] 我知道你不喜欢我对“大水坑”的设计，这里的这些滑梯也好，喷泉也好，的确算不上高明。
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#1$1",focus=1)]
[name="卡奇·叙光"] 但，斯第奇，你知道我真正想设计的是什么吗？和你一样，是我们头顶的这一片穹顶！我们曾经竞争了那么久的穹顶！
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#1$1",focus=2)]
[name="斯第奇·画布"]......哈哈，在我面前说这些，还真是大胆。你真的很想打架吗？
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#1$1",focus=1)]
[name="卡奇·叙光"] 你我是不错的对手。
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#8$1",focus=2)]
[name="斯第奇·画布"]哈！不错的对手！真是高看我了，我们是不是应该拥抱在一起，痛哭流涕一下？
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#8$1",focus=1)]
[name="卡奇·叙光"] 我是认真的，斯第奇。
[Character(name="avg_npc_567_1#4$1", name2="avg_4054_malist_1#8$1",focus=1)]
[name="卡奇·叙光"] 我只是想问你，为什么在几年前，你放弃了继续在穹顶改造方案上投入努力？
[Character(name="avg_npc_567_1#4$1", name2="avg_4054_malist_1#

... (全文22340字符)
```

### level_act20side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="30_g1_durinstreet",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$relax_intro", key="$relax_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_574_1$1", name2="avg_npc_575_1$1",fadetime=0.7)]
[delay(time=1)]
[Character(name="avg_npc_574_1$1", name2="avg_npc_575_1$1",focus=2)]
[name="搓手的杜林人"]你听说了吗？那个劲爆的消息！
[Character(name="avg_npc_574_1$1", name2="avg_npc_575_1$1",focus=1)]
[name="心痒的杜林人"]哪个？
[Character(name="avg_npc_574_1$1", name2="avg_npc_575_1$1",focus=2)]
[name="搓手的杜林人"]克罗绮说代表们正在商量着搞出点新东西！
[Character(name="avg_npc_574_1$1", name2="avg_npc_575_1$1",focus=1)]
[name="心痒的杜林人"]上次那个让全城灯光变成绿色的计划我可不太喜欢。
[Character(name="avg_npc_574_1$1", name2="avg_npc_575_1$1",focus=2)]
[name="搓手的杜林人"]不是那个！是关于滑梯的！
[Character(name="avg_npc_574_1$1", name2="avg_npc_575_1$1",focus=2)]
[name="搓手的杜林人"]听说斯第奇和卡奇正在吵“大水坑”的改建方案呢！
[Character(name="avg_npc_574_1$1", name2="avg_npc_575_1$1",focus=1)]
[name="心痒的杜林人"]他们两个吗？！已经吵到哪一步了？
[Character(name="avg_npc_574_1$1", name2="avg_npc_575_1$1",focus=2)]
[name="搓手的杜林人"]呃，好像是用水炮把人打进另一个水炮，再打进另一个......之类的？
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="30_g2_fountainlake",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#1$1",fadetime=0.7)]
[delay(time=1)]
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#3$1",focus=2)]
[name="斯第奇·画布"]绝对不行！
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#3$1",focus=1)]
[name="卡奇·叙光"]那我再换个方案，用水炮把人打上高处的跳板......
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#3$1",focus=2)]
[name="斯第奇·画布"]你除了水炮就说不出别的了是吗？
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#3$1",focus=1)]
[name="卡奇·叙光"]这是你给我的启发！那么大建筑设计师斯第奇又有什么好点子呢？
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#5$1",focus=2)]
[name="斯第奇·画布"]呃，我本来只是打算作为总建筑设计师，稍微把控一下那些阿卡胡拉人的方案的......
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#5$1",focus=1)]
[name="卡奇·叙光"]你让地上人来帮忙造铁路桥，我没意见。但我们现在讨论的，是在铁路桥之上的，与铁路桥共生的，际崖城的地标！
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#5$1",focus=1)]
[name="卡奇·叙光"]你不同意我碰穹顶，可以，我完全理解你对穹顶的感情，那我们就讨论大滑梯之后的下一个地标是什么。
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#1$1",focus=2)]
[name="斯第奇·画布"]我们完全可以更简洁优美地处理这个问题，它可以充满象征性！
[Character(name="avg_npc_567_1#5$1", name2="avg_4054_malist_1#1$1",focus=1)]
[name="卡奇·叙光"]也可以更刺激！
[Character(name="avg_npc_567_1#5$1", name2="avg_4054_malist_1#6$1",focus=2)]
[name="斯第奇·画布"]也可以更刺激地充满象征性！
[Character(name="avg_npc_567_1#5$1", name2="avg_4054_malist_1#6$1",focus=2)]
[name="斯第奇·画布"]呼，卡奇，我们在这里争不出什么东西。要比设计搞竞标？完全可以，我们给彼此留出创作时间，然后让际崖城的市民做选择。
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#6$1",focus=1)]
[name="卡奇·叙光"]可以，就和当年一样。
[Character(name="avg_npc_566_1#1$1")]
[name="克罗绮·砖石"]我也赞同——
[Character(name="avg_npc_567_1#1$1", name2="avg_4054_malist_1#1$1",focus=1)]
[name="卡奇·叙光"]克罗绮小姐？你这是喝酒了吗？
[Character(name="avg_npc_566_1#9$1")]
[name="克罗绮·砖石"]没事啦，就喝了一点点。
[Character(name="avg_npc_075")]
[name="依娜姆"]喝了三桶。
[Character(name="avg_npc_566_1#8$1")]
[name="克罗绮·砖石"]斯第奇，你的方案我听说了，我很有兴趣。
[Character(name="avg_npc_566_1#8$1")]
[name="克罗绮·砖石"]既然卡奇也不太反对，那事情就好办了！
[Character(name="avg_npc_566_1#9$1")]
[name="克罗绮·砖石"]只要再找到黛柯绮，我们就能推着际崖城搞出点新东西啦！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="30_g4_durinsquare",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$holiday_intro", key="$holiday_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_569_1#1$1")]
[name="黛柯绮·银币"]你的意思是，我该换一种方式对待它们......
[Character(name="char_416_zumama_1#5", name2="avg_npc_576_1$1",focus=1)]
[name="森蚺"]你不觉得它们很可爱吗？
[Character(name="char_416_zumama_1#5", name2="avg_npc_576_1$1",focus=1)]
[name="森蚺"]这些小家伙们的确还远不能被称作是“人”，我并不是医生，但就算如此，我也知道人的复杂度是现在的机器还难以企及的。
[Character(name="char_416_zumama_1#5", name2="avg_npc_576_1$1",focus=1)]
[name="森蚺"]但这并不妨碍我们更加友善地和它们相处。
[Character(name="char_416_zumama_1#5", name2="avg_npc_576_1$1",focus=1)]
[name="森蚺"]黛柯绮，你是这些小家伙的“家长”。
[Character(name="avg_npc_569_1#6$1")]
[name="黛柯绮·银币"]......家长，是吗。
[Character(name="char_416_zumama_1#5", name2="avg_npc_576_1$1",focus=1)]
[name="森蚺"]这些小家伙愿意依赖你，愿意相信你，就像刚刚破壳的羽兽在妈妈的翅膀下成长。
[Character(name="avg_npc_569_1#2$1")]
[name="黛柯绮·银币"]很长时间，我看待它们的态度......没有那么“关心”。我只是在做一个工业代表该做的，和一代代的工业代表没什么不同。
[Character(name="avg_npc_569_1#1$1")]
[name="黛柯绮·银币"]机器人的管理员们从那些喜欢泡在图书馆机械区里的杜林人中选拔而出，我们得掌握制造这些小东西的方法。
[Character(name="avg_npc_569_1#1$1")]
[name="黛柯绮·银币"]其实并不复杂，只要按照书上说的去做，把自己喜欢的零件装在一起......发挥自己的想象力，它们总能动起来。
[Character(name="avg_npc_569_1#1$1")]
[name="黛柯绮·银币"]我的老师曾经花费了很多年想要搞清楚这些小家伙运转的原理，不过最后毫无收获。
[Character(name="avg_npc_569_1#8$1")]
[name="黛柯绮·银币"]听说老师的老师也研究过，她成功让助理机器人可以讲笑话了。
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=2)]
[name="奇怪的机械0429"]你知道该怎么激怒一个杜林人吗？没人知道！哈哈哈。
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=1)]
[name="森蚺"]唔，水平很高。
[Character(name="avg_npc_569_1#1$1")]
[name="黛柯绮·银币"]而我，我只是理所当然地借助它们的力量。祖玛玛，你说得对，我应该试着和它们“交流”。
[Character(name="avg_npc_569_1#1$1")]
[name="黛柯绮·银币"]0429，你的同伴0428已经退役，它无法通过检修被唤醒。
[Character(name="avg_npc_569_1#1$1")]
[name="黛柯绮·银币"]但它仍是我们的一员，它建设过的东西不会消亡。
[Character(name="avg_npc_569_1#8$1")]
[name="黛柯绮·银币"]退役不是终点。
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=2)]
[name="奇怪的机械0429"]本机确认指令，退役不是终点。明白。
[Character(name="char_416_zumama_1#1", name2="avg_npc_576_1$1",focus=2)]
[name="奇怪的机械0429"]祖玛玛定义了关系，朋友。黛柯绮，希望和你定义为朋友。
[Character(

... (全文13434字符)
```

### level_act20side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="30_g2_fountainlake",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$dignified_intro", key="$dignified_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_566_1#1$1")]
[name="克罗绮·砖石"]根据大家表决的结果，陪伴了我们半年多的“大水坑”即将完成它的历史使命。它会被爆破拆解，重新回归为工程材料。
[Character(name="avg_npc_566_1#5$1")]
[name="克罗绮·砖石"]市民们，这场稍微延长了一点的夏日狂欢恐怕即将结束了。
[dialog]
[character]
[name="杜林人"]呜呜呜，我会永远记得这段美好的时光。
[name="杜林人"]超级旋转大滑梯真是怎么玩都玩不够，居然就要和它告别了......
[Character(name="avg_npc_566_1#3$1")]
[name="克罗绮·砖石"]不过！取代“大水坑”的，会是更新的，更美的，更不一样的建筑！！毕竟这里可是际崖城，是最棒的建筑设计师们缔造的城市！
[Character(name="avg_npc_566_1#6$1")]
[name="克罗绮·砖石"]斯第奇·画布和卡奇·叙光是际崖城新生代里最引人瞩目的建筑设计师，他们会在未来的几个月里交出自己的设计方案......
[Character(name="avg_npc_566_1#6$1")]
[name="克罗绮·砖石"]到那时，又会是一场怎样的强者对决呢！
[Character(name="avg_npc_566_1#2$1")]
[name="克罗绮·砖石"]呼呼，简直让人想起几年前，他们初露锋芒的时候，围绕着穹顶的那场竞标大赛！
[Character(name="avg_npc_566_1#3$1")]
[name="克罗绮·砖石"]当年的穹顶之争没有胜利者，那么这次，谁会取得下一个际崖城地标的设计权呢？让我们——
[dialog]
[stopmusic(fadetime=1)]
[delay(time=1)]
[Character(name="avg_npc_566_1#7$1")]
[name="克罗绮·砖石"]我先喝口水。
[dialog]
[characteraction(name="middle", type="move", ypos=-20, fadetime=0.3, isblock=true)]
[characteraction(name="middle", type="jump", ypos=20, fadetime=0.3, isblock=true)]
[playmusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[delay(time=0.51)]
[Character(name="avg_npc_564_1#5$1")]
[name="耶奇·地心"]克罗绮，你今天这个状态，不会是喝了酒来的吧？
[Character(name="avg_npc_566_1#10$1")]
[name="克罗绮·砖石"]暂时没有。
[Character(name="avg_npc_564_1#1$1")]
[name="耶奇·地心"]这风格可不像你啊。
[Character(name="avg_npc_566_1#1$1")]
[name="克罗绮·砖石"]依娜姆给我看的录像里，地上的比赛中有一个职位叫做主持人。
[Character(name="avg_npc_566_1#1$1")]
[name="克罗绮·砖石"]我打算拓展一下职业路径。
[Character(name="avg_npc_566_1#3$1")]
[name="克罗绮·砖石"]总之！建筑设计师们的设计虽然暂时还等不来，但是，市民们，这个夏天的尾巴可是稍纵即逝！
[Character(name="avg_npc_566_1#3$1")]
[name="克罗绮·砖石"]就让我们在滑梯消失前的最后时间里，去玩它个爽吧！
[dialog]
[character]
[PlaySound(key="$d_avg_crwdcheerup", volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="杜林人"]哦！！！！！
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_npc_572_1#4$1",enter="right",fadetime=0.7)]
[PlaySound(key="$runsand",channel="run")]
[delay(time=0.8)]
[stopsound(channel="run")]
[name="特米米"]嘉维尔！
[dialog]
[characteraction(name="middle", type="jump",power=60, fadetime=0.7,times=3,block=true)]
[characteraction(name="middle", type="exit",direction="left",fadetime=1,block=false)]
[character(fadetime=1)]
[delay(time=0.51)]
[Character(name="char_empty")]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=1, block=false)]
[PlaySound(key="$runsand",channel="run")]
[Character(name="avg_1026_gvial2_1#1$1",fadetime=0.7)]
[delay(time=0.8)]
[stopsound(channel="run")]
[name="嘉维尔"]特米米，小心！你慢点！
[dialog]
[characteraction(name="middle", type="jump",power=60, fadetime=0.7,times=3,block=true)]
[characteraction(name="middle", type="exit",direction="left",fadetime=0.7,block=false)]
[character(fadetime=1)]
[delay(time=0.51)]
[Dialog]
[Character(name="avg_npc_572_1#4$1", name2="char_empty")]
[name="特米米"]之前你们在阿卡胡拉的大瀑布玩水，我听说了以后可是羡慕了好久呢！
[name="特米米"]嘿嘿，这次我也可以加入啦！
[dialog]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_npc_572_1#4$1", name2="avg_1026_gvial2_1#1$1",fadetime=0.7)]
[delay(time=2)]
[Character(name="avg_npc_572_1#4$1", name2="avg_1026_gvial2_1#5$1",focus=2)]
[name="嘉维尔"]你这孩子。
[Character(name="avg_npc_572_1#4$1", name2="avg_1026_gvial2_1#10$1",focus=2)]
[name="嘉维尔"]嗯？平常你都小心翼翼地藏着尾巴，这么一看，是不是又变粗了点？
[Character(name="avg_npc_572_1#5$1", name2="avg_1026_gvial2_1#10$1",focus=1)]
[name="特米米"]欸？才没有！我来之前才刚用卷尺量过！已经好几个月没有变粗了！
[Character(name="avg_npc_572_1#5$1", name2="avg_1026_gvial2_1#3$1",focus=2)]
[name="嘉维尔"]哦，看来真的很在意？
[Character(name="avg_npc_572_1#3$1", name2="avg_1026_gvial2_1#3$1",focus=1)]
[name="特米米"]呜呜呜，看我的泼水攻击！
[dialog]
[characteraction(name="left", type="move", ypos=-150, fadetime=0.3, isblock=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Effect(name="$e_shuihua", layer = 1,x=100,rox = 50, roy=80)]
[PlaySound(key="$d_avg_jump_water", volume=0.9)]
[characteraction(name="left", type="jump", ypos=150, fadetime=0.3, block=true)]
[characteraction(name="right", type="move", xpos=80, fadetime=0.3, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[characteraction(name="right", type="jump", xpos=-80, fadetime=0.3, block=true)]
[delay(time=1)]
[Character(name="avg_npc_572_1#3$1", name2="avg_1026_gvial2_1#3$1",focus=2)]
[name="嘉维尔"]很大胆嘛！来就来！
[dialog]
[PlaySound(key="$runsand")]
[character(fadetime=0.5)]
[delay(time=1)]
[Character(name="avg_4055_bgsnow_1#1$1")]
[name="阿芙朵嘉"] 她们似乎比你更像杜林人呢，斯第奇。
[Character(name="avg_4054_malist_1#1$1")]
[name="斯第奇·画布"]你也未必知道什么叫“杜林人”，鲁珀。
[Character(name="avg_4055_bgsnow_1#1$1")]
[name="阿芙朵嘉"] 你好像有点紧张，在担心和卡奇的竞标吗？
[Character(name="avg_4054_malist_1#8$1")]
[name="斯第奇·画布"]担心他？笑话！我还没沦落到担心比不过卡奇的境地。不过是他的方案一向比较招外行人的喜欢罢了。
[Character(name="avg_4054_malist_1#8$1")]
[name="斯第奇·画布"]也有些人是比较看好我的方案的，或许我该拿出点不同的风格，好赢过那家伙。
[Character(name="avg_4054_malist_1#5$1")]
[name="斯第奇·画布"]要不然干脆......唉！现在还是别想了！
[Character(name="avg_4054_malist_1#1$1")]
[name="斯第奇·画布"]......说实话，如果不论美学，仅从可玩度上而言，这“大水坑”也还算凑合吧。
[Character

... (全文18642字符)
```

### level_act20side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="30_g3_fountainlake_ruins",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$bat_Imfxingback_intro",key="$bat_Imfxingback_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_566_1#8$1",fadetime=0.5)]
[Delay(time=1)]
[name="克罗绮·砖石"]那么，第一届际崖城与阿卡胡拉和罗德岛联合举办的游泳大赛，现在正式拉开帷幕！
[Character(name="avg_npc_566_1#9$1")]
[name="克罗绮·砖石"]本次比赛将由我，际崖城的商业代表克罗绮·砖石，借由黛柯绮·银币小姐亲手打造的高精度摄像机为各位带来直播。
[Character(name="avg_npc_566_1#8$1")]
[name="克罗绮·砖石"]首先，让我们介绍一下这次比赛的赛道。
[Character]
[name="克罗绮·砖石"]从这边的岸边到隧道所在的岸边，直线距离约为一公里的地下湖泊。
[multiline(name="克罗绮·砖石")]而比赛规则是——
[multiline(name="克罗绮·砖石")]没有比赛规则，谁第一个抵达湖的另一边就算是胜者！
[name="克罗绮·砖石"]胜者将代表所属的组织获得由我克罗绮提供的特质精酿麦酒一个月不限量自由饮用权！
[Dialog]
[PlaySound(key="$livecrowd",volume=0.8)]
[CameraShake(duration=2, xstrength=30, ystrength=30, vibrato=20, randomness=90, fadeout=true, block=false)]
[Delay(time=3)]
[Character(name="avg_npc_566_1#9$1")]
[name="克罗绮·砖石"]首先，罗德岛方面派出的参赛选手是——
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="克罗绮·砖石"]伊比利亚之风，罗德岛第一美男子，极境！
[Dialog]
[Character]
[Character(name="avg_npc_571_1#1$1",fadetime=0.5)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=20, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_crwdcheerup")]
[PlaySound(key="$d_avg_applause")]
[PlaySound(key="$d_avg_whistle", volume=0.6)]
[name="极境"]哈哈，杜林的各位大家好啊！
[Dialog]
[Character(name="avg_npc_571_1#2$1")]
[Delay(time=2)]
[Character(name="avg_npc_075#1")]
[name="依娜姆"]......他刚才把克罗绮拉过去在那交流半天原来就是想让她念这些吗。
[Character(name="avg_npc_566_1#8$1")]
[name="克罗绮·砖石"]阿卡胡拉方面派出的代表是——
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="克罗绮·砖石"]嘉维尔！
[Character(name="avg_npc_572_1#4$1")]
[name="特米米"]嘉维尔，加油！
[Dialog]
[Character]
[Character(name="avg_1026_gvial2_1#3$1",fadetime=0.5)]
[PlaySound(key="$d_avg_cheer_street", volume=1)]
[PlaySound(key="$d_avg_toyhorn", volume=1)]
[PlaySound(key="$d_avg_whistle", volume=0.6)]
[name="嘉维尔"]大家好啊！
[dialog]
[delay(time=2)]
[Character(name="avg_npc_566_1#4$1")]
[name="克罗绮·砖石"]而代表际崖城参加的选手，竟然是——
[Dialog]
[Character]
[PlaySound(key="$livecrowd",volume=0.7,delay=0.3)]
[Character(name="avg_npc_565_1#3$1",fadetime=0.5)]
[Delay(time=2)]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_566_1#4$1")]
[name="克罗绮·砖石"]竟然是我们的环境与气候代表，耶奇大师！
[Character(name="avg_4055_bgsnow_1#1$1",name2="avg_1026_gvial2_1#1$1",focus=1)]
[name="阿芙朵嘉"]......
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#1$1",focus=1)]
[name="阿芙朵嘉"]所以说，只是要派人去隧道那边要安放仪器的位置事先勘测一下，为什么，会变成，游泳比赛？
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#3$1",focus=2)]
[name="嘉维尔"]机会难得啊。
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#10$1",focus=2)]
[name="嘉维尔"]装备什么的还要等一等吧？
[name="嘉维尔"]而且，铁路还没修好的话，来来回回也不方便，既然都是要过去的，为什么不做点有趣的事情呢？
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#10$1",focus=1)]
[name="阿芙朵嘉"]哈......随你们的便吧。
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#5$1",focus=2)]
[name="嘉维尔"]你不来吗？
[Character(name="avg_4055_bgsnow_1#9$1",name2="avg_1026_gvial2_1#5$1",focus=1)]
[name="阿芙朵嘉"]我没兴趣，我宁愿去看看特米米和黛柯绮的施工准备得如何了。
[Character(name="avg_4055_bgsnow_1#9$1",name2="avg_1026_gvial2_1#2$1",focus=2)]
[name="嘉维尔"]唉，你这乌萨斯人真没意思。
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_4055_bgsnow_1#3$1",name2="avg_1026_gvial2_1#2$1",focus=1)]
[name="阿芙朵嘉"]我不是乌萨斯人！
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#2$1",focus=1)]
[name="阿芙朵嘉"]而且，你到底是怎么说服耶奇大师......
[Character(name="avg_npc_565_1#10$1")]
[name="耶奇·地心"]阿芙朵嘉，我是自愿的。
[Character(name="avg_4055_bgsnow_1#6$1",name2="avg_1026_gvial2_1#1$1",focus=1)]
[name="阿芙朵嘉"]欸，但是......
[Character(name="avg_npc_565_1#10$1")]
[name="耶奇·地心"]老头子我只是希望你们在玩乐的同时，也能帮帮我的忙。
[name="耶奇·地心"]现在既然你们帮了我的忙，参加这点活动我当然不会反对。
[Character(name="avg_npc_565_1#6$1")]
[name="耶奇·地心"]倒不如说啊，城里这帮家伙虽然喜欢玩水，但是要说游泳健将，那可真是一个都挑不出来。
[Character(name="avg_npc_565_1#7$1")]
[name="耶奇·地心"]唉，这毕竟也算是事关我们际崖城的脸面，所以也只好我这老胳膊老腿勉强拼一把咯。
[Character(name="avg_4055_bgsnow_1#9$1",name2="avg_1026_gvial2_1#1$1",focus=1)]
[name="阿芙朵嘉"]......
[Character(name="avg_4055_bgsnow_1#1$1",name2="avg_1026_gvial2_1#3$1",focus=2)]
[name="嘉维尔"]哈哈，没事的，大师，友谊第一，比赛第二嘛。
[Character(name="avg_npc_565_1#8$1")]
[name="耶奇·地心"]哼，就算你这么说，要是传出去，我们际崖城和地上人比赛输了，那我们的脸上怎么挂得住？
[Character(name="avg_4055_bgsnow_1#1$1",name2="avg_1026_gvial2_1#5$1",focus=2)]
[name="嘉维尔"]但是你刚才也听到了，阿芙朵嘉说她没兴趣，没说她不会。
[Character(name="avg_npc_565_1#7$1")]
[name="耶奇·地心"]我们杜林人从不为难别人，她既然不愿意参赛，我又怎么会强迫她呢？
[Character(name="avg_4055_bgsnow_1#9$1",name2="avg_1026_gvial2_1#1$1",focus=1)]
[name="阿芙朵嘉"]......
[Character(name="avg_npc_565_1#6$1")]
[name="耶奇·地心"]况且，阿芙朵嘉本来就不是我们际崖城的人，她不想代表际崖城也是情有可原。
[Character(name="avg_npc_565_1#7$1")]
[name="耶奇·地心"]老头子我啊，今天看来要豁出去才行了。
[Character(name="avg_4055_bgsnow_1#3$1",name2="avg_1026_gvial2_1#1$1",focus=1)]
[name="阿芙朵嘉"]......我知道了，我知道了，我代表杜林参赛还不行吗！
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#1$1",focus=1)]
[name="阿芙朵嘉"]这样你们满意了吧！
[Character(name="avg_npc_565_1#5$1")]
[name="耶奇·地心"]真的？
[Character(name="avg_4055_bgsnow_1#6$1",name2="avg_1026_gvial2_1#1$1",focus=1)]
[name="阿芙朵嘉"]您都这么说了，我还能不参加吗！
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#3$1",focus=2)]
[name="嘉维尔"]哈哈哈，这才对嘛！
[Character(name="avg_npc_565_1#3$1")]
[name="耶奇·地心"]克罗绮！
[Dialog]
[Character]
[Dialog]
[Character(name="avg_4055_bgsnow_1#1$1", name2="char_empty")]
[PlaySound(key="$runsand")]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]


... (全文23005字符)
```

### level_act20side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="30_g10_lakegarden",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$holiday_intro", key="$holiday_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_576_1#1$1",fadetime=0.5)]
[Delay(time=1)]
[PlaySound(key="$gavel1",volume=0.7)]
[CameraShake(duration=0.2,xstrength=15,ystrength=15,vibrato=10,randomness=90,fadeout=true,block=true)]
[Delay(time=1)]
[name="奇怪的机械"]祖玛玛，组装船只，这样正确？
[Character(name="char_416_zumama_1#1")]
[name="森蚺"]嗯，在结构上没有问题，但是我认为这个结构是可以调整的，比如你看——
[Dialog]
[Character(name="char_416_zumama_1#2")]
[characteraction(name="middle", type="move", xpos=50, fadetime=0.7, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_axehitscrape")]
[characteraction(name="middle", type="move", ypos=-20, fadetime=0.3, block=true)]
[Blocker(a=0, fadetime=0.3, block=true)]
[characteraction(name="middle", type="move", ypos=20, fadetime=0.3, block=true)]
[Delay(time=1)]
[name="森蚺"]你们看，这样就更加牢固了。
[Character(fadetime=0)]
[Character(name="avg_npc_576_1#1$1",name2="avg_npc_576_1#1$1")]
[name="奇怪的机械"]祖玛玛，祖玛玛，厉害。
[Character(name="char_416_zumama_1#5")]
[name="森蚺"]只是一点经验罢了。
[Dialog]
[Character(fadetime=0)]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[Character(name="avg_npc_075",fadetime=1)]
[Delay(time=2)]
[name="依娜姆"]祖玛玛，你果然在这里。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=1)]
[name="森蚺"]依娜姆？你怎么来了？
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=2)]
[name="依娜姆"]这些源石勘测设备不是要运送到对岸么，我正好没事做，就帮忙运过来了。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=1)]
[name="森蚺"]谢了。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=2)]
[name="依娜姆"]为什么是你来谢我......你还真把自己当成这群机器人的一员了。
[Character(name="char_416_zumama_1#5",name2="avg_npc_075",focus=1)]
[name="森蚺"]嗯，难得能交到这么多的好朋友。
[Character(name="avg_npc_576_1#1$1",name2="avg_npc_576_1#1$1")]
[name="奇怪的机械"]祖玛玛，祖玛玛，好朋友！
[Character(name="char_416_zumama_1#4",name2="avg_npc_075",focus=1)]
[name="森蚺"]而且，我其实一直想要帮Lancet-2大姐找到适合的相亲对象。
[Character(name="char_416_zumama_1#4",name2="avg_npc_075",focus=2)]
[name="依娜姆"]......如果我没记错的话，Lancet-2是当时跟罗德岛一起来的机器人吧？
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=1)]
[name="森蚺"]嗯，她现在是我的姐姐。
[name="森蚺"]我的技术还没有办法做到造出Lancet-2大姐那样智能的机器人，所以就想在这群机器人中找一找。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=2)]
[name="依娜姆"]结果怎么样？
[Character(name="char_416_zumama_1#5",name2="avg_npc_075",focus=1)]
[name="森蚺"]它们很善良，不过感觉都不是大姐会喜欢的类型。
[Character(name="char_416_zumama_1#4",name2="avg_npc_075",focus=1)]
[name="森蚺"]大姐似乎比较中意博士那样比较知性的，这点比较伤脑筋。
[Character(name="char_416_zumama_1#4",name2="avg_npc_075",focus=2)]
[name="依娜姆"]......
[name="依娜姆"]算了，提亚卡乌里奇奇怪怪的家伙也不止你一个。
[Character]
[PlaySound(key="$d_avg_femalecommentator",volume=0.2)]
[name="远处的广播声"]大家好，我是克罗绮，我找了一个比较安全的高处来为各位继续进行报道。
[name="远处的广播声"]距离终点还有，嗯......三百米吧？管他的。
[name="远处的广播声"]城市建筑设计师中，最为特立独行的一位，芬奇大师的唯一弟子，斯第奇·画布，不知道从哪里弄来了一条船，强行插入了我们的比赛。
[name="远处的广播声"]嗯？他好像在对着我们的方向说些什么，让我放大镜头看一看他的唇语......
[name="远处的广播声"]他在说，嗯......我猜是“我要拿第一！”
[name="远处的广播声"]哦，他还朝着我比划了一个愤怒的手势，没想到我们的建筑设计师小哥冷淡的外表下原来隐藏着这样一颗火热的心！
[name="远处的广播声"]虽然他出发的时间相当晚，但是，交通工具的优势毕竟是十分巨大的。
[name="远处的广播声"]就在我说这些话的时间，他已经拉近了相当一部分距离！
[Character(name="char_416_zumama_1#4",name2="avg_npc_075",focus=2)]
[name="依娜姆"]那边也真是热闹得不行。
[name="依娜姆"]虽然想说嘉维尔走过的地方永远都是这个样子，但是这群人的热闹程度也真是不得了。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=1)]
[name="森蚺"]你不习惯吗？
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=2)]
[name="依娜姆"]以前不习惯，在阿卡胡拉待久了，不习惯也习惯了。
[name="依娜姆"]现在，要是哪天没人打架和吵吵闹闹，我才会觉得不习惯。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=1)]
[name="森蚺"]你也是个提亚卡乌了。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=2)]
[name="依娜姆"]谁说不是呢。
[name="依娜姆"]说起来，祖玛玛，我记得，前年那会儿，如果不是嘉维尔跑了回来，你其实是打算当阿卡胡拉的大酋长的吧？
[Character(name="char_416_zumama_1#2",name2="avg_npc_075",focus=1)]
[name="森蚺"]确切地说，成为大酋长并不是我的目的，我只是希望通过那个方式来证明我自己。
[Character(name="char_416_zumama_1#5",name2="avg_npc_075",focus=1)]
[name="森蚺"]我的理想一直是造出最厉害的机器。
[Character(name="char_416_zumama_1#5",name2="avg_npc_075",focus=2)]
[name="依娜姆"]好吧，果然在这方面指望你这家伙是不可能的。
[Character(name="char_416_zumama_1#4",name2="avg_npc_075",focus=1)]
[name="森蚺"]你在考虑王酋的事情吗？
[Character(name="char_416_zumama_1#4",name2="avg_npc_075",focus=2)]
[name="依娜姆"]太好了，看来你和特米米在外面还是学到了一些有关国家体制的知识，不像嘉维尔。
[name="依娜姆"]真不知道她在外面这几年是怎么活下来的。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=1)]
[name="森蚺"]在嘉维尔面前，有些我们觉得理所当然的事会为她让步，比如，适应环境。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=2)]
[name="依娜姆"]哈哈，确实。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=1)]
[name="森蚺"]所以，你想让她来当王酋？她真的适合吗？
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=2)]
[name="依娜姆"]说实在的，我觉得随便去萨尔贡大街上找个路人，都比她适合当王酋。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=1)]
[name="森蚺"]我同意。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=2)]
[name="依娜姆"]但是，如果要从提亚卡乌中选出一个能够统领阿卡胡拉的人，那非她莫属。
[Character(name="char_416_zumama_1#2",name2="avg_npc_075",focus=1)]
[name="森蚺"]这是作为一个提亚卡乌的看法，还是作为一个萨尔贡信使的看法？
[Character(name="char_416_zumama_1#2",name2="avg_npc_075",focus=2)]
[name="依娜姆"]......
[Character]
[PlaySound(key="$d_avg_femalecommentator",volume=0.2)]
[name="远处的广播声"]比赛此时已经进入了后半程！
[name="远处的广播声"]嘉维尔依然保持领先，虽然她的领先优势已经越来越小了。
[name="远处的广播声"]但是要超过她的却不是阿芙朵嘉小姐！
[name="远处的广播声"]虽然阿芙朵嘉小姐已经十分努力了，但是选择直接下水还是为她带来了麻烦！
[name="远处的广播声"]衣服的重量让她的行动变得缓慢下来了！
[name="远处的广播声"]没错，紧咬在嘉维尔身后的正是极境！
[name="远处的广播声"]在经过前半段的蓄力后，如今，极境才将他真正的实力展现在我们的眼前。
[name="远处的广播声"]他超过了阿芙朵嘉小姐，并且眼看已经来到了和嘉维尔齐平的位置！
[name="远处的广播声"]但是——
[name="远处的广播声"]他们都没有注意到，真正的威胁正在从身后靠近！
[Character(name="char_416_zumama_1#2",name2="avg_npc_075",focus=2)]
[name="依娜姆"]居然能追上嘉维尔，极境这家伙果然本事不小。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075",focus=1)]
[name="森蚺"]他只是喜欢用浮夸的态度来掩饰自己，这也是一种自大。
[Character(name="char_416_zumama_1#1",name2="avg_npc_075

... (全文9761字符)
```

### level_act20side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="30_i03",x=0, y=0, xScale=1, yScale=1, fadetime=0)]
[playMusic(intro="$bat_Imfxingback_intro",key="$bat_Imfxingback_loop", volume=0.2)]
[ImageTween(xScaleFrom=1, yScaleFrom=1, xScaleTo=0.87, yScaleTo=0.87, duration=30, block=false)]
[Blocker(a=0.85, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
斯第奇挣扎着睁开眼，看到了两个熟悉的身影。
[name="克罗绮·砖石"]阿芙朵嘉，我帮你把换洗的衣服带来了。
[name="阿芙朵嘉"]谢谢。
[name="阿芙朵嘉"]还有，克罗绮，我建议你，以后还是少喝点酒比较好。
[name="克罗绮·砖石"]啊哈哈，抱歉抱歉。但是，你看，结果来说不是还挺好吗？
[name="阿芙朵嘉"]我是看不出有哪里好了......
[name="阿芙朵嘉"]唉，我还是找个地方换衣服吧。
然后，两人也注意到了斯第奇的醒来。
[name="阿芙朵嘉"]唉，早上好，斯第奇。
[name="斯第奇·画布"]我怎么了？
[name="阿芙朵嘉"]你还记得你是怎么昏倒的吗？
[name="斯第奇·画布"]我开着船，然后老耶奇跳了过来，然后......嘶......
[name="阿芙朵嘉"]然后船失控了，冲上了岸，把你们两个甩了出来。
[name="斯第奇·画布"]耶奇大师呢？
[name="阿芙朵嘉"]耶奇大师比你先醒来，已经带着极境先进去勘测了。
[name="斯第奇·画布"]对了，还有船上的装备！
[PlaySound(key="$e_atk_saw_n_2",volume=0.2)]
[name="阿芙朵嘉"]放在船上的那些设备基本都损坏了，勘测设备......已经让黛柯绮加紧制造了。
[name="阿芙朵嘉"]开凿设备倒是不用了。
[PlaySound(key="$e_atk_saw_n_2",volume=0.2,delay=1)]
[name="斯第奇·画布"]为什么？
[name="阿芙朵嘉"]从刚才开始，你就没有感觉到有什么东西很吵吗？
阿芙朵嘉无奈地向着不远处看了一眼。
[PlaySound(key="$e_atk_saw_n_2",volume=0.2)]
[PlaySound(key="$d_avg_rockfall",volume=0.2,delay=0.5)]
而在她的提醒下，斯第奇才意识到，原来，刚才开始就存在的噪音并不是天然的。这似乎是一种电锯轰鸣和山岩崩塌的混合声？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Image]
[dialog]
[character(fadetime=0)]
[Background(image="30_g9_collapsedtunnel",screenadapt="coverall")] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_1026_gvial2_1#8$1",fadetime=0.5)]
[characteraction(name="middle", type="move", xpos=300, fadetime=0, block=true)]
[Delay(time=1)]
[PlaySound(key="$e_atk_saw_n_2")]
[characteraction(name="middle", type="move", ypos=-30,xpos=10,fadetime=0.3, block=true)]
[Blocker(a=0, fadetime=0.3, block=true)]
[characteraction(name="middle", type="move", ypos=30,xpos=-10,fadetime=0.2, block=true)]
[PlaySound(key="$d_avg_vallyrck")]
[Delay(time=1)]
[PlaySound(key="$e_atk_saw_n_2")]
[characteraction(name="middle", type="move", ypos=-30,xpos=10,fadetime=0.3, block=true)]
[Blocker(a=0, fadetime=0.3, block=true)]
[characteraction(name="middle", type="move", ypos=30,xpos=-10,fadetime=0.2, block=true)]
[Delay(time=1)]
[PlaySound(key="$e_atk_saw_n_2")]
[characteraction(name="middle", type="move", ypos=-30,xpos=10,fadetime=0.3, block=true)]
[Blocker(a=0, fadetime=0.3, block=true)]
[characteraction(name="middle", type="move", ypos=30,xpos=-10,fadetime=0.2, block=true)]
[PlaySound(key="$d_avg_vallyrck")]
[Delay(time=2)]
[Character(fadetime=0)]
[Character(name="avg_4054_malist_1#7$1")]
[name="斯第奇·画布"]嘉维尔，你在干什么啊......
[Dialog]
[Character(fadetime=0)]
[PlaySound(key="$e_atk_saw_n_1")]
[Character(name="avg_1026_gvial2_1#8$1")]
[characteraction(name="middle", type="move", xpos=300, fadetime=0, block=true)]
[PlaySound(key="$d_avg_walk_stage")]
[Delay(time=2)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=1.5, block=true)]
[Delay(time=2)]
[Character(name="avg_1026_gvial2_1#10$1")]
[name="嘉维尔"]看不就知道了，我在清理岩壁啊。
[Character(name="avg_4055_bgsnow_1#4$1")]
[name="阿芙朵嘉"]虽然船把坍塌的地方砸出了不小的口子，但是，依然没有那么简单能够通行。
[name="阿芙朵嘉"]而开凿的装备也坏了，原本还以为要等一会儿，结果——
[Character(name="avg_4055_bgsnow_1#6$1")]
[name="阿芙朵嘉"]如你所见。
[Character(name="avg_1026_gvial2_1#3$1")]
[name="嘉维尔"]哈哈，比起修铁路和勘测，很显然，这个才是我的强项嘛！
[Dialog]
[Character]
环视四周，斯第奇看到了许多切面非常规整的岩石碎块，以及一个足够两人并肩通行的洞口。
这无疑是嘉维尔的杰作。
也就是说，在开凿设备全部损失的情况下，嘉维尔仅凭自己一个人，就打开了通往隧道内的路。
斯第奇忍不住开始怀疑，他在阿卡胡拉部族里听到的那些有关无敌的嘉维尔的离奇传言，是不是有一部分其实是真的。
[Dialog]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[Character(name="avg_npc_571_1#11$1",name2="char_empty",fadetime=0.5)]
[Delay(time=2)]
[Character(name="avg_npc_571_1#11$1",name2="avg_1026_gvial2_1#1$1",fadetime=0.5)]
[characteraction(name="right", type="move", xpos=200, fadetime=0, block=false)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Delay(time=1)]
[Character(name="avg_npc_571_1#11$1",name2="avg_1026_gvial2_1#5$1",focus=2)]
[name="嘉维尔"]哦，极境，你怎么回来得这么快？
[stopmusic(fadetime=3)]
[Character(name="avg_npc_571_1#11$1",name2="avg_1026_gvial2_1#5$1",focus=1)]
[name="极境"]......
[Character(name="avg_npc_571_1#11$1",name2="avg_1026_gvial2_1#9$1",focus=2)]
[name="嘉维尔"]发生了什么，耶奇大师呢？
[Character(name="avg_npc_571_1#12$1",name2="avg_1026_gvial2_1#9$1",focus=1)]
[name="极境"]情况有点不妙，嘉维尔。
[Character(name="avg_npc_571_1#12$1",name2="avg_1026_gvial2_1#6$1",focus=2)]
[name="嘉维尔"]怎么了？难道有什么巨大源石虫之类的东西？我听普罗旺斯说过她在汐斯塔见过那种玩意。
[Character(name="avg_npc_571_1#11$1",name2="avg_1026_gvial2_1#6$1",focus=1)]
[name="极境"]如果是某种生物，我现在一定还有心情跟你开玩笑。
[Character(name="avg_npc_571_1#9$1")]
[name="极境"]跟我来。
[Dialog]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[Character(fadetime=0.5)]
[Delay(time=1)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Background(image="bg_caveentrance",screenadapt="coverall")] 
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.4)]
在钻过隧道的坍塌处后，众人走入了隧道之中。
隧道之中的空间，实际上与其说是隧道，不如说是洞窟，宽广又幽深。
不过，极境的引导十分高效，在他的指引下，众人在洞穴中的穿行十分顺利。
顺利到让人忍不住好奇，他是怎么在这么短的时间内就摸清了隧道的构造，甚至怀疑他是否来过这条隧道。
然而，和这点近乎玩笑的怀疑相比，当极境停下脚步时，众人所看到的东西，更令他们感到怀疑。
那是一条裸露在岩层外的源石矿脉。
并且，任何对源石有些了解的人都能够轻易发现，这条源石矿脉已经活性化了很久。
而活性化，意味着——
爆炸。
或者说——
灾难。
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_4054_malist_1#3$1")]
[name="斯第奇·画布"]这怎么可能？！
[Character(name="avg_npc_564_1#6$1")]
[name="耶奇·地心"]这个方向上确实在建城时曾勘测到有源石矿脉的存在，但是它距离隧道应该很远——
[Character(name="avg_npc_571_1#7$1")]
[name="极境"]有没有可能是之前的大地震导致它被扯到了这里？听说之后也发生过几次小的余震。
[name="极境"]毕竟这矿脉看起来确实够突兀的。
[Character(name="avg_npc_564_1#6$1")]
[name="耶奇·地心"]不是没有可能......
[Character(name="avg_npc_564_1#4$1")]
[name="耶奇·地心"]对，没错！它很有可能是被之前的那场地震牵扯到这里来的！
[Character(name="avg_n

... (全文12953字符)
```

### level_act20side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_caveentrance",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$newhope02_intro",key="$newhope02_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_564_1#5$1")]
[name="耶奇·地心"]前往地面？
[Character(name="avg_4055_bgsnow_1#8$1")]
[name="阿芙朵嘉"]杜林人从来没有前往地面过！
[Character(name="avg_1026_gvial2_1#6$1")]
[name="嘉维尔"]斯第奇不就去过？图书馆里的那些书不也是去过地面的人带下来的？
[Character(name="avg_1026_gvial2_1#9$1")]
[name="嘉维尔"]况且也没有人规定不能去吧？
[Character(name="avg_1026_gvial2_1#1$1")]
[name="嘉维尔"]听你们说的，走隧道太危险，修新的避难所又来不及。
[name="嘉维尔"]那么，去地面上，在我们阿卡胡拉避难一段时间是最好的办法吧。
[Character(name="avg_4055_bgsnow_1#8$1")]
[name="阿芙朵嘉"]那座升降梯不可能容纳那么多......
[Character(name="avg_4055_bgsnow_1#9$1")]
[name="阿芙朵嘉"]......
[Character(name="avg_1026_gvial2_1#6$1")]
[name="嘉维尔"]怎么了？
[Character(name="avg_4055_bgsnow_1#9$1")]
[name="阿芙朵嘉"]虽然我很想反驳你，但是......
[Character(name="avg_4055_bgsnow_1#9$1")]
[name="阿芙朵嘉"]虽然你们在际崖城没有见到，但是，在杜林的社会中，列车是最常见的交通工具。
[name="阿芙朵嘉"]升降梯虽然在垂直方向的移动上很方便......
[name="阿芙朵嘉"]但是，杜林的城市由于无法移动，在建造之初就要面临毁灭的风险，只能垂直移动的升降梯对他们来说实用性远不如列车。
[name="阿芙朵嘉"]而且，有些杜林探险家也测算过，杜林的城市通常在距离地上一千米至一千五百米左右的位置，很少有超过这个范围的城市存在。
[name="阿芙朵嘉"]也就是说，杜林对地下的探索是水平式的，很少出现一座城市垂直往下一两百米有另一座城市的情况。
[Character(name="avg_1026_gvial2_1#6$1")]
[name="嘉维尔"]嗯......所以这和升降梯有什么关系？
[Character(name="avg_4055_bgsnow_1#1$1")]
[name="阿芙朵嘉"]虽然我也知道给你解释是浪费时间，但我要对别人负责。
[Character(name="avg_1026_gvial2_1#5$1")]
[name="嘉维尔"]什么啊，你的意思不就是对杜林人来说造列车更方便么。
[Character(name="avg_4055_bgsnow_1#6$1")]
[name="阿芙朵嘉"]唉，算你对吧。
[name="阿芙朵嘉"]那么，在这种情况下，升降梯又是为了什么而存在的呢？
[Character(name="avg_npc_571_1#1$1")]
[name="极境"]我明白了，是资源，对吧。
[Character(name="avg_npc_571_1#12$1")]
[name="极境"]虽然不知道为什么杜林人的城市是以横向拓展为主，可能是某种惯性吧。
[Character(name="avg_npc_571_1#1$1")]
[name="极境"]但无论如何，这不意味着，他们对资源的探索也是横向的，对吧？
[Character(name="avg_4055_bgsnow_1#9$1")]
[name="阿芙朵嘉"]我原本以为你说你走过许多地方只是吹嘘，现在看来你确实懂的很多。
[Character(name="avg_npc_571_1#4$1")]
[name="极境"]哇哦。
[Character(name="avg_npc_571_1#1$1")]
[name="极境"]嘉维尔，瞧啊，阿芙朵嘉小姐都比你能够意识到我的价值。
[Character(name="avg_1026_gvial2_1#2$1")]
[name="嘉维尔"]关我什么事。
[Character(name="avg_npc_571_1#2$1")]
[name="极境"]阿芙朵嘉小姐，下次你和嘉维尔吵架，我一定站在你这边。
[Character(name="avg_4055_bgsnow_1#6$1")]
[name="阿芙朵嘉"]......还是免了吧。
[Character(name="avg_4055_bgsnow_1#8$1")]
[name="阿芙朵嘉"]总之，你说得没错。杜林人对于地下的探索，尤其是对于矿物的探索是充满热情的。
[name="阿芙朵嘉"]而且，由于城市的规划需要许多人共同决策，但挖洞却是每个杜林人自己就能决定的事。
[name="阿芙朵嘉"]所以，他们经常一不小心就挖到了距离自己城市的头顶或者底下好几百米的地方。
[Character(name="avg_4055_bgsnow_1#9$1")]
[name="阿芙朵嘉"]实际上，有不少杜林历史学家认为......
[name="阿芙朵嘉"]第一座杜林族升降梯是因为一位杜林城市的工业代表在自己所属的城市头顶发现矿脉后，发现直接打洞过去最方便，才设计出来的。
[Character(name="avg_4055_bgsnow_1#1$1")]
[name="阿芙朵嘉"]不过，随着杜林人中对于地面感兴趣的人层出不穷，这些升降梯也经常被他们用来作为前往地上的捷径。
[Character(name="avg_1026_gvial2_1#9$1")]
[name="嘉维尔"]嗯......所以说，升降梯主要是杜林用来搬矿石的，偶尔还会让斯第奇那样的小鬼用来去地面玩玩。
[Character(name="avg_4054_malist_1#3$1")]
[name="斯第奇·画布"]我说过了，我和你差不多大，嘉维尔！
[Character(name="avg_1026_gvial2_1#1$1")]
[name="嘉维尔"]嗯。所以，这个我明白了，但是，说了这么多，我还是没明白你想说什么欸。
[Character(name="avg_4055_bgsnow_1#7$1")]
[name="阿芙朵嘉"]唉......
[Character(name="avg_npc_571_1#1$1")]
[name="极境"]阿芙朵嘉小姐的意思是，因为杜林的升降梯大多是面向工业设计的，所以十分坚固。
[name="极境"]我和特米米一起下来的时候也注意到了这一点，那座升降梯大概能很轻松地容纳几十个人吧。
[name="极境"]所以嘉维尔你的提议确实是可行的。
[name="极境"]是吧，耶奇大师。
[Character(name="avg_npc_564_1#5$1")]
[name="耶奇·地心"]对对。
[name="耶奇·地心"]超方便大升降梯一号最初确实是因为不知道哪个无聊的家伙发现了上面的矿脉，经过表决后设计的。
[Character(name="avg_npc_564_1#9$1")]
[name="耶奇·地心"]只是后来我们发现了更近的矿脉，于是就放着不管了。
[Character(name="avg_1026_gvial2_1#5$1")]
[name="嘉维尔"]哦，难怪，我听人说过那个山洞好像是被开采过的，该不会那个洞本身都是你们杜林挖通的吧？
[Character(name="avg_npc_564_1#1$1")]
[name="耶奇·地心"]那就不知道了，有可能吧。
[Character(name="avg_4055_bgsnow_1#9$1")]
[name="阿芙朵嘉"]而且，为了应对可能出现的情况，杜林人在设计升降梯时，本来就会挖更多的空间，方便未来进行扩建。
[Character(name="avg_npc_571_1#10$1")]
[name="极境"]也就是说，如果要最合理地运用剩下的时间，我们确实应该对升降梯进行扩建，让杜林们前往地面。
[Character(name="avg_1026_gvial2_1#3$1")]
[name="嘉维尔"]哦，那你直接这么说不就完了。
[Character(name="avg_4055_bgsnow_1#8$1")]
[name="阿芙朵嘉"]如果你只是知道怎么做，却不知道为什么这么做，那总有一天会遇到障碍的。
[Character(name="avg_1026_gvial2_1#10$1")]
[name="嘉维尔"]我知道啊。
[Dialog]
[Character(name="avg_4055_bgsnow_1#8$1",name2="char_empty")]
[Blocker(a=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#10$1",fadetime=0.5)]
[characteraction(name="right", type="move", xpos=200, fadetime=0, block=true)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1.5, block=true)]
[Delay(time=2)]
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#9$1",focus=2)]
[name="嘉维尔"]但我是医生，阿芙朵嘉。
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#1$1",focus=2)]
[name="嘉维尔"]而且，你不是知道得很清楚吗？
[name="嘉维尔"]我难道不能信任你吗？
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#1$1",focus=1)]
[name="阿芙朵嘉"]我怎么不知道我们的关系什么时候这么好了。
[Character(name="avg_4055_bgsnow_1#8$1",name2="avg_1026_gvial2_1#10$1",focus=2)]
[name="嘉维尔"]我觉得我们已经是好朋友了。
[Character(name="avg_4055_bgsnow_1#6$1",name2="avg_1026_gvial2_1#10$1",focus=1)]
[name="阿芙朵嘉"]......
[Character(name="avg_npc_564_1#2$1")]
[name="耶奇·地心"]总而言之，我同意嘉维尔的提议。
[Character(name="avg_npc_564_1#1$1")]
[name="耶奇·地心"]剩下的细节就交给你们讨论好了，我要继续勘测了。
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_571_1#1$1",focus=2)]
[name="极境"]耶奇大师，我来帮你吧，我的源石技艺能够传递信息，一旦你这里有结果我也能第一时间通知大家。
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_571_1#1$1",focus=1)]
[name="耶奇·地心"]行。
[Character(name="avg_4054_malist_1#7$1")]
[name="斯第奇·画布"]......
[Dialog]
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_571_1#1$1")]
[PlaySound(key="$d_gen_walk_n")]
[Blocker(a=0,fadetime=0.5,block=true)]
[PlaySound(key="$d_gen_walk_n")]
[characteraction(name="left", type="move", xpos=-350, fadetime=2, block=true)]
[Blocker(a=0,fadetime=0.5,block=true)]
[characteraction(name="right", type="move", xpos=-400, fadetime=2, block=true)]
[Delay(time=1)]
[Character(fadetime=0.5)]
[Delay(time=2)]
[Character(name="avg_4055_bgsnow_1#1$1",name2="char_empty")]
[Blocker(a=0,fadetime=0.5,b

... (全文21417字符)
```

### level_act20side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_caveentrance",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[playsound(key="$d_avg_walk_stage",volume=0.7)]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_571_1#1$1",fadetime=1)]
[Delay(time=2)]
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_571_1#1$1",focus=2)]
[name="极境"]说起来，耶奇大师，我有点好奇，斯第奇的师父，是个什么样的人？
[Character(name="avg_npc_564_1#5$1",name2="avg_npc_571_1#1$1",focus=1)]
[name="耶奇·地心"]我就知道你小子跟我来有别的目的。
[name="耶奇·地心"]你很关心斯第奇那小子啊。
[Character(name="avg_npc_564_1#5$1",name2="avg_npc_571_1#1$1",focus=2)]
[name="极境"]哈哈，被您看出来了吗。
[Character(name="avg_npc_564_1#5$1",name2="avg_npc_571_1#10$1",focus=2)]
[name="极境"]我这个人就是这样，希望大家都能和和气气地搞好关系。
[Character(name="avg_npc_564_1#10$1",name2="avg_npc_571_1#10$1",focus=1)]
[name="耶奇·地心"]那你一定会喜欢他的师父的。
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_571_1#10$1",focus=1)]
[name="耶奇·地心"]芬奇·画布，是际崖城最受欢迎的建筑设计师。
[name="耶奇·地心"]他的设计风格虽然和杜林中最流行的风格迥异，但在他的解释下，却总是能抓住大伙的心。
[name="耶奇·地心"]用他的话说，叫什么来着，对了，“对抗我们无休止的欲望”。
[name="耶奇·地心"]虽然他的理论比较独特，但际崖城的人都很喜欢他。
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_571_1#9$1",focus=2)]
[name="极境"]那这样的人为什么会离开际崖城？
[Character(name="avg_npc_564_1#6$1",name2="avg_npc_571_1#9$1",focus=1)]
[name="耶奇·地心"]不知道欸。
[Character(name="avg_npc_564_1#6$1",name2="avg_npc_571_1#7$1",focus=2)]
[name="极境"]啊？
[Character(name="avg_npc_564_1#7$1",name2="avg_npc_571_1#7$1",focus=1)]
[name="耶奇·地心"]他忽然就离开了，没有告诉任何人。
[Character(name="avg_npc_564_1#7$1",name2="avg_npc_571_1#12$1",focus=2)]
[name="极境"]这......还真是奇怪。
[Character(name="avg_npc_564_1#6$1",name2="avg_npc_571_1#12$1",focus=1)]
[name="耶奇·地心"]而他留下的这个徒弟呢，虽然才华大家都是认可的，但是人嘛，你也看到了。
[Character(name="avg_npc_564_1#6$1",name2="avg_npc_571_1#1$1",focus=2)]
[name="极境"]哈哈，大概这也和他老师的突然离开有关吧。
[Character(name="avg_npc_564_1#2$1",name2="avg_npc_571_1#1$1",focus=1)]
[name="耶奇·地心"]谁说不是呢。
[Dialog]
[Character]
[PlaySound(key="$d_avg_medicalbeep", channel="a", loop=true)]
[Delay(time=2)]
[stopsound(channel="a", fadetime=0)]
[Character(name="avg_npc_564_1#2$1",name2="avg_npc_571_1#10$1",focus=2)]
[name="极境"]哦？是不是出结果了？
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_571_1#10$1",focus=1)]
[name="耶奇·地心"]嗯，让我看看......
[Character(name="avg_npc_564_1#9$1",name2="avg_npc_571_1#10$1",focus=1)]
[name="耶奇·地心"]唉......
[Character(name="avg_npc_564_1#9$1",name2="avg_npc_571_1#11$1",focus=2)]
[name="极境"]怎么样？
[Character(name="avg_npc_564_1#7$1",name2="avg_npc_571_1#11$1",focus=1)]
[name="耶奇·地心"]唉，和我预测的差不多。
[name="耶奇·地心"]我们还有将近一个月的时间。
[Dialog]
[Character]
[name="嘉维尔"]一个月？那应该足够扩建升降梯了吧。
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_571_1#11$1",focus=1)]
[name="耶奇·地心"]你来了，嘉维尔。
[Dialog]
[Character]
[playsound(key="$d_avg_walk_stage",volume=0.7)]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_npc_572_1#7$1",fadetime=1)]
[Delay(time=2)]
[Character(name="avg_1026_gvial2_1#10$1",name2="avg_npc_572_1#7$1",focus=1)]
[name="嘉维尔"]是啊，不过看来已经不用我帮忙了？
[Character(name="avg_npc_564_1#1$1")]
[name="耶奇·地心"]嗯，勘测到这一步就差不多了。
[Dialog]
[Character(fadetime=0.3)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="avg_1026_gvial2_1#10$1",name2="char_empty")]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="avg_1026_gvial2_1#10$1",name2="avg_npc_564_1#1$1",fadetime=0.5)]
[characteraction(name="right", type="move", xpos=100, fadetime=0, block=false)]
[characteraction(name="right", type="move", xpos=-100, fadetime=0.8, block=false)]
[Delay(time=1)]
[Character(name="avg_1026_gvial2_1#10$1",name2="avg_npc_564_1#1$1",focus=2)]
[name="耶奇·地心"]你说服阿芙朵嘉了？
[Character(name="avg_1026_gvial2_1#10$1",name2="avg_npc_564_1#1$1",focus=1)]
[name="嘉维尔"]是啊，她说她会帮忙说服际崖城的居民们。
[Character(name="avg_1026_gvial2_1#10$1",name2="avg_npc_564_1#1$1",focus=2)]
[name="耶奇·地心"]嗯，那剩下的应该就是正式通知全城的居民这个状况了。
[name="耶奇·地心"]不仅要决定是不是前往地面，穹顶的事情也得解决掉。
[Character(name="avg_1026_gvial2_1#5$1",name2="avg_npc_564_1#1$1",focus=1)]
[name="嘉维尔"]嗯？关穹顶什么事？
[Character(name="avg_1026_gvial2_1#5$1",name2="avg_npc_564_1#5$1",focus=2)]
[name="耶奇·地心"]哦，我都快要忘了你们不是杜林了。
[Character(name="avg_1026_gvial2_1#5$1",name2="avg_npc_564_1#1$1",focus=2)]
[name="耶奇·地心"]杜林人的城市虽然说不经常遭难，但一个杜林，在一生中往往难免要面对一次自己居住城市的毁灭。
[name="耶奇·地心"]我们对于离开家乡这件事并不会有什么感想。
[name="耶奇·地心"]相反，我们在离开前，总是要将自己的城市维持在最好的状态，让它能够以最好的状态迎接毁灭。
[Character(name="avg_1026_gvial2_1#3$1",name2="avg_npc_564_1#1$1",focus=1)]
[name="嘉维尔"]听起来很酷嘛！
[Character(name="avg_1026_gvial2_1#3$1",name2="avg_npc_564_1#1$1",focus=2)]
[name="耶奇·地心"]是吗？对我们来说，这是理所当然的事。
[name="耶奇·地心"]而穹顶上的那个洞，之前放着不管有它的理由，现在就要想想办法了。
[Character(name="avg_1026_gvial2_1#10$1",name2="avg_npc_564_1#1$1",focus=1)]
[name="嘉维尔"]说到穹顶，斯第奇呢？
[Character(name="avg_1026_gvial2_1#10$1",name2="avg_npc_564_1#5$1",focus=2)]
[name="耶奇·地心"]嗯？他不是跟你们在一起吗？
[Character(name="avg_1026_gvial2_1#5$1",name2="avg_npc_564_1#5$1",focus=1)]
[name="嘉维尔"]啊？他说来找你们了啊。
[Character(name="avg_npc_572_1#2$1")]
[name="特米米"]嘉维尔，你要找斯第奇吗？
[Character(name="avg_1026_gvial2_1#6$1")]
[name="嘉维尔"]你知道他去哪儿了？
[Character(name="avg_npc_572_1#6$1")]
[name="特米米"]嗯。我们进来的时候遇到他了，他没跟我们说话，只是往洞窟外面去了。
[Character(name="avg_1026_gvial2_1#5$1")]
[name="嘉维尔"]啊？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Background(image="30_g5_library_indoor",screenadapt="coverall")] 
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_075")]
[name="依娜姆"]你信誓旦旦地跟我们说你有地图，结果现在又告诉我们，地图有可能在这一面书架上某本书里？
[Character(name="avg_4055_bgsnow_1#7$1")]
[name="阿芙朵嘉"]咳咳，这也是没有办法的事。
[name="阿芙朵嘉"]毕竟我对于返回地上没有任何兴趣，能够记得曾经在书里看到过前人记录下来的路线图这件事本身，你们就该知足了。
[Character(name="char_416_zumama_1#1")]
[name="森蚺"]时间还有一些，如果那个洞穴结构真有你们说的那么复杂，我也不介意在这里多花一些时间。
[Character(name="char_416_zumama_1#4")]
[name=

... (全文16867字符)
```

### level_act20side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="30_g11_malistgarden",screenadapt="coverall")] 
[Delay(time=1)]
[Character(name="char_empty",name2="avg_npc_569_1#2$1")]
[PlaySound(key="$d_avg_summercicada",volume=0.3, loop=true, channel="a")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[PlaySound(key="$radio",volume=0.6)]
[name="广播"]各位际崖城的居民，你们好。
[name="广播"]耶奇大师的勘测结果已经出炉。
[name="广播"]活性源石矿脉的爆发时间，大约在二十五天后。
[name="广播"]从现在开始，际崖城将正式进入撤离的准备阶段。
[name="广播"]接下来，经过各位代表的讨论后，将在合适的时间于广场举行一场全体会议。
[name="广播"]届时，我们将讨论具体的撤离方案，以及城市的遗容。
[name="广播"]请各位际崖城居民注意收听广播。
[Dialog]
[StopSound(channel="a", fadetime=2)]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.4)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#2$1",fadetime=0.5)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0, block=false)]
[characteraction(name="left", type="move", xpos=200, fadetime=1.5, block=false)]
[Delay(time=2)]
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#2$1",focus=1)]
[name="卡奇·叙光"]黛柯绮，醒醒，黛柯绮。
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#2$1",focus=2)]
[name="睡着的黛柯绮·银币"]......机器人斯第奇，真听话。
[Character(name="avg_npc_567_1#4$1",name2="avg_npc_569_1#2$1",focus=1)]
[name="卡奇·叙光"]......黛柯绮，黛柯绮。
[Character(name="avg_npc_567_1#4$1",name2="avg_npc_569_1#2$1",focus=2)]
[name="睡着的黛柯绮·银币"]机器人卡奇，笨笨的。
[name="睡着的黛柯绮·银币"]你们，打一架。
[Character(name="avg_npc_567_1#3$1",name2="avg_npc_569_1#2$1",focus=1)]
[name="卡奇·叙光"]你到底在做什么梦啊。
[Dialog]
[Character(name="avg_npc_567_1#4$1",name2="avg_npc_569_1#2$1")]
[characteraction(name="left", type="move", xpos=100, fadetime=1.5, block=true)]
[Delay(time=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="卡奇·叙光"]黛柯绮！醒醒！
[Dialog]
[Character(name="avg_npc_567_1#4$1",name2="avg_npc_569_1#4$1")]
[Delay(time=1)]
[Character(name="avg_npc_567_1#4$1",name2="avg_npc_569_1#1$1",focus=2)]
[name="黛柯绮·银币"]嗯？怎么了？
[Dialog]
[Character(name="avg_npc_567_1#4$1",name2="avg_npc_569_1#1$1")]
[characteraction(name="left", type="move", xpos=-100, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_567_1#4$1",name2="avg_npc_569_1#1$1",focus=1)]
[name="卡奇·叙光"]......我还想问你呢，你怎么又在斯第奇的花园里午睡。
[Character(name="avg_npc_567_1#4$1",name2="avg_npc_569_1#8$1",focus=2)]
[name="黛柯绮·银币"]因为斯第奇的花园很安静啊。
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#8$1",focus=1)]
[name="卡奇·叙光"]看你睡得这么死，肯定也没听到广播吧。
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#1$1",focus=2)]
[name="黛柯绮·银币"]发生什么事了吗？
[Character(name="avg_npc_567_1#2$1",name2="avg_npc_569_1#1$1",focus=1)]
[name="卡奇·叙光"]......耶奇大师去湖对岸勘测过后，发现了源石矿脉被之前的地震拉扯到了隧道出口的附近，而且活性化已经十分厉害了。
[name="卡奇·叙光"]我们接下来要开一次全体会议，决定如何避难。
[Character(name="avg_npc_567_1#2$1",name2="avg_npc_569_1#5$1",focus=2)]
[name="黛柯绮·银币"]哦。
[name="黛柯绮·银币"]但是，你应该不是特意来告诉我这个的吧？
[Character(name="avg_npc_567_1#2$1",name2="avg_npc_569_1#5$1",focus=1)]
[name="卡奇·叙光"]......没错。
[name="卡奇·叙光"]我是来找斯第奇的。
[Character(name="avg_npc_567_1#2$1",name2="avg_npc_569_1#1$1",focus=2)]
[name="黛柯绮·银币"]斯第奇的话，他应该乘坐我借给他的船去湖对岸找耶奇大师他们去了。
[Character(name="avg_npc_567_1#2$1",name2="avg_npc_569_1#1$1",focus=1)]
[name="卡奇·叙光"]是吗，那我在这里等他吧。
[Character(name="avg_npc_567_1#2$1",name2="avg_npc_569_1#5$1",focus=2)]
[name="黛柯绮·银币"]你找他有事吗？
[Character(name="avg_npc_567_1#4$1",name2="avg_npc_569_1#5$1",focus=1)]
[name="卡奇·叙光"]嗯，我希望，他......能回到设计部来参与穹顶的设计修改。
[name="卡奇·叙光"]既然际崖城面临毁灭，我们关于这座城市地标的比拼已经毫无意义，但好在我们还有些时间。
[name="卡奇·叙光"]那么，我们在之后的大会上肯定需要决定，该如何处理地震留下的穹顶缺口。
[Character(name="avg_npc_567_1#4$1",name2="avg_npc_569_1#10$1",focus=2)]
[name="黛柯绮·银币"]就那么放着不管我觉得也可以吧？
[Character(name="avg_npc_567_1#2$1",name2="avg_npc_569_1#10$1",focus=1)]
[name="卡奇·叙光"]即使如此，那也要城里的居民们都同意才行。
[name="卡奇·叙光"]让一座城市在这片土地上存在的最后一瞬间趋于完美，这对于每个建筑设计师来说都是非常有意义的事情。
[name="卡奇·叙光"]我们会对这座城市进行最后一次观察，并且给出一个在有限的时间里能够完成的方案。
[Character(name="avg_npc_567_1#2$1",name2="avg_npc_569_1#1$1",focus=2)]
[name="黛柯绮·银币"]所以，你希望斯第奇能够回去。
[Character(name="avg_npc_567_1#2$1",name2="avg_npc_569_1#1$1",focus=1)]
[name="卡奇·叙光"]嗯。
[name="卡奇·叙光"]我不知道芬奇大师为什么会忽然离开，别人或许会以为，是因为他们师徒的感情淡了，或者缘分尽了，但我知道，这是不可能的。
[name="卡奇·叙光"]作为芬奇大师过去的助手，我比任何人都了解，他虽然是个十分豪放的人，但心底里其实非常关心斯第奇。
[name="卡奇·叙光"]对他来说，斯第奇就像他的亲生儿子一样。
[name="卡奇·叙光"]所以，他的离开一定和斯第奇有密不可分的关系。
[name="卡奇·叙光"]而斯第奇在大师离开后的情况，身为工业代表你也看在眼里。
[name="卡奇·叙光"]他从一次次提出的方案被否决，到逐渐不再在设计部出现，在这中间，我一直想要帮他，却始终没有找到办法。
[name="卡奇·叙光"]这座穹顶，是斯第奇的老师，芬奇大师留给这座城市最宏伟的作品。
[name="卡奇·叙光"]但这座穹顶，对斯第奇来说，会不会反而是一种负担呢？
[Character(name="avg_npc_567_1#2$1",name2="avg_npc_569_1#5$1",focus=2)]
[name="黛柯绮·银币"]......
[name="黛柯绮·银币"]即使如此，你也不希望他留下遗憾，对吗？
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#5$1",focus=1)]
[name="卡奇·叙光"]嗯。
[name="卡奇·叙光"]这是最后的机会了，黛柯绮。
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#1$1",focus=2)]
[name="黛柯绮·银币"]真有你的风格。
[Dialog]
[Character]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_npc_564_1#1$1",fadetime=1)]
[Delay(time=2)]
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_npc_564_1#5$1",focus=2)]
[name="耶奇·地心"]斯第奇，斯第奇！你在吗？
[Character(name="avg_1026_gvial2_1#5$1",name2="avg_npc_564_1#5$1",focus=1)]
[name="嘉维尔"]嗯？怎么是你们两个？
[Character(name="avg_npc_571_1#2$1")]
[name="极境"]卡奇，原来你和黛柯绮是这种关系吗？
[Character(name="avg_npc_569_1#10$1")]
[name="黛柯绮·银币"]不是。
[Character(name="avg_npc_571_1#1$1")]
[name="极境"]哇哦，好果断。
[Character(name="avg_npc_567_1#1$1")]
[name="卡奇·叙光"]你就别拿我开玩笑了，极境哥。
[name="卡奇·叙光"]耶奇大师，嘉维尔小姐，你们辛苦了。
[Character(name="avg_npc_569_1#1$1")]
[name="黛柯绮·银币"]我在这里午睡，他在这里等斯第奇回来。
[Character(name="avg_npc_564_1#5$1")]
[name="耶奇·地心"]斯第奇没有回来吗？
[Character(name="avg_npc_569_1#4$1")]
[name="黛柯绮·银币"]他不是应该给大师你们送设备去了吗？还闹出了不小的动静呢。
[Character(name="avg_npc_564_1#6$1")]
[name="耶奇·地心"]但他中途就不见了，我们都不知道他去哪了，结果他也没有回家吗......
[Character(name="avg_1026_gvial2_1#1$1")]
[name="嘉维尔"]特米米遇到过这小子，说他的表情好像很难受。


... (全文20179字符)
```

### level_act20side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="30_g4_durinsquare",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[Character(name="avg_npc_564_1#1$1",fadetime=1)]
[Delay(time=2)]
[name="耶奇·地心"]咳咳，各位际崖城的居民们，我是你们的环境与气候代表，耶奇·地心。
[name="耶奇·地心"]现在，把大家都喊过来不是为了别的，正是为了讨论有关际崖城的未来。
[name="耶奇·地心"]现在勘测结果也已经出来了，我们几位代表也讨论出来了几套可行的方案，今天，我们会在这些方案中做出选择。
[Character(name="avg_npc_564_1#2$1")]
[name="耶奇·地心"]而且，有关最后怎么折腾这座城市，最好也能讨论出一个方案。
[Character(name="avg_npc_564_1#1$1")]
[name="耶奇·地心"]不过，今天这场会议不是我主讲，而是会由阿芙朵嘉来发言。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Background(image="30_g6_reception",screenadapt="coverall")] 
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_566_1#1$1")]
[name="克罗绮·砖石"]阿芙朵嘉，你真的没问题吗？
[name="克罗绮·砖石"]虽然你已经在际崖城生活了这么久，城里的人都认识你，但是，这还是你第一次真的站在大家面前吧？
[Character(name="avg_4055_bgsnow_1#1$1")]
[name="阿芙朵嘉"]嗯。
[Character(name="avg_npc_564_1#1$1")]
[name="耶奇·地心"]好了，阿芙朵嘉，该你上场了。
[Character(name="avg_4055_bgsnow_1#6$1")]
[name="阿芙朵嘉"]耶奇大师，我可能会说得久一些，没问题吗？
[Character(name="avg_npc_564_1#10$1")]
[name="耶奇·地心"]噢，我想你是不可能打破我曾经创下的，把半座城市的人都给说睡着的记录的。
[Character(name="avg_4055_bgsnow_1#6$1")]
[name="阿芙朵嘉"]还有这样的事情吗？
[Character(name="avg_npc_566_1#4$1")]
[name="克罗绮·砖石"]啊，我记得，那一次是大师说着说着，开始讲起了地质学的知识。
[name="克罗绮·砖石"]从下午说到了晚上，直到大师自己都撑不住了才终于结束了。
[Character(name="avg_4055_bgsnow_1#9$1")]
[name="阿芙朵嘉"]我大概也不会说那么久吧。
[Character(name="avg_npc_564_1#1$1")]
[name="耶奇·地心"]去吧，阿芙朵嘉，我看得出来，这也会是你作为地上人，在我们这里生活了这么久的一次总结。
[Character(name="avg_4055_bgsnow_1#10$1")]
[name="阿芙朵嘉"]......谢谢，那我去了。
[Dialog]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[Character(fadetime=0.5)]
[Delay(time=2)]
[playsound(key="$livecrowd",volume=0.2)]
[Delay(time=1)]
[name="远处的声音"]真的是阿芙朵嘉小姐！
[name="远处的声音"]阿芙朵嘉小姐！无论你说什么我都支持你！
[Character(name="avg_npc_564_1#7$1")]
[name="耶奇·地心"]为什么我演讲就没有这么受欢迎？
[Character(name="avg_npc_569_1#1$1")]
[name="黛柯绮·银币"]因为除了您的最长记录之外，其他由您主持的会议，也没有短到哪里去。
[Character(name="avg_npc_564_1#1$1")]
[name="耶奇·地心"]臭丫头，别以为我不知道，每次你都是第一个睡着的。
[Character(name="avg_npc_569_1#1$1")]
[name="黛柯绮·银币"]今天我可不会睡，今天的阿芙朵嘉，和平时不太一样，她到底想说些什么？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Background(image="30_g4_durinsquare",screenadapt="coverall")] 
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[Character(name="avg_4055_bgsnow_1#1$1",fadetime=0.5)]
[characteraction(name="middle", type="move", xpos=-400, fadetime=0, block=false)]
[characteraction(name="middle", type="move", xpos=400, fadetime=2, block=false)]
[Delay(time=3)]
[Character(name="avg_npc_574_1#1$1",name2="avg_npc_575_1#1$1",focus=1)]
[name="激动的杜林人"]太好了，虽然耶奇大师确实很厉害，但是要听他开会太折磨了。
[Character(name="avg_npc_574_1#1$1",name2="avg_npc_575_1#1$1",focus=2)]
[name="悠哉的杜林人"]阿芙朵嘉小姐人又美，声音也动听，如果是她来讲，多久我都愿意听啊。
[Character(name="avg_4055_bgsnow_1#10$1")]
[name="阿芙朵嘉"]各位际崖城的居民，大家好，我是文学代表，阿芙朵嘉。
[name="阿芙朵嘉"]今天，将由我来主持这场事关际崖城未来的会议。
[Character(name="avg_4055_bgsnow_1#8$1")]
[name="阿芙朵嘉"]关于在灾难之下如何撤离际崖城，最后，我们通过与耶奇大师的讨论，认为有三种可行的方案。
[name="阿芙朵嘉"]不过，在讨论具体的方案之前，我想和大家先聊些别的事情。
[Character(name="avg_4055_bgsnow_1#9$1")]
[name="阿芙朵嘉"]那就是，关于我的过去。
[Character(name="avg_4055_bgsnow_1#1$1")]
[name="阿芙朵嘉"]不是阿芙朵嘉·锐笔的过去，而是，阿芙朵嘉·尼古拉耶芙娜·伊万诺娃的过去。
[name="阿芙朵嘉"]在来到杜林的城邦生活后，我创作了许多故事，也和许多人分享了许多有关我的事情。
[name="阿芙朵嘉"]但唯有这一部分，我从来没有对任何人说过。
[name="阿芙朵嘉"]今天，我想分享给大家。
[Character(name="avg_4055_bgsnow_1#2$1")]
[name="阿芙朵嘉"]......
[Character(name="avg_4055_bgsnow_1#1$1")]
[name="阿芙朵嘉"]我出生在一个乌萨斯的贵族家庭......
[Image(image="30_i07", xScale=1.1, yScale=1.1, fadetime=1)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=0.9, yScaleTo=0.9,xTo=0, yTo=0, duration=30, block=false)]
阿芙朵嘉本以为自己会不知道该说些什么。
但是当她真正开口的时候，记忆却在一瞬间倾泻而出。
她发现，自己并不是不知道说什么，而是能说的太多了，自己竟一时间不知道从哪里开始。
杜林人们并不知道这对她来说意味着什么，但她自己却一清二楚。
这是她流落到杜林的城邦后，第一次回头去看自己的过去。
她本想让时间冲淡过去的经历，她曾无数次地想要让自己忘记自己身为乌萨斯的一部分。
而此时此刻，她终于真正意识到，她永远都无法抹去自己的出身，也不可能真正逃避自己的过去。
但是，见到嘉维尔，见到嘉维尔身边的那些人，让她明白——
或许这样也没有那么糟。
往事如潮水，将她一点一点地淹没，也将听故事的杜林们牵扯其中。
[StopMusic(fadetime=2)]
但她不再为此痛苦，于是，杜林们也甘之若饴。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Image(fadetime=0.5)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Background(image="30_g8_malistroom",screenadapt="coverall")] 
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
斯第奇坐在房间里，他试图强迫自己不去想这件事情。
但他发现自己做不到。
他知道，这是自己最后的机会。
如果放弃这个机会，自己将永远无法胜过老师。
而且，他有一种预感，这一次无法胜过的话，他将永远无法胜过某种他无法言喻的东西。
他知道。
但他做不到。
他缓缓抱住了自己的头。
[PlaySound(key="$doorknockquite")]
“哐哐哐——”
敲门声在这时响起。
[name="嘉维尔"]喂，斯第奇，你在里面吧？
[Character(name="avg_4054_malist_1#4$1")]
[name="斯第奇·画布"]......
[Character]
[name="嘉维尔"]别装了，我知道你在里面。
[Character(name="avg_4054_malist_1#6$1")]
[name="斯第奇·画布"]别来管我，嘉维尔！
[Character]
[name="嘉维尔"]那可不行，找你有事呢。
[Character(name="avg_4054_malist_1#1$1")]
[name="斯第奇·画布"]如果是穹顶的事，去找卡奇吧。
[Character]
[name="嘉维尔"]不行。
[Character(name="avg_4054_malist_1#5$1")]
[name="斯第奇·画布"]为什么？
[Character]
[name="嘉维尔"]因为那是你应该做的事情。
[name="嘉维尔"]你先开门，我进来再说。
[Character(name="avg_4054_malist_1#3$1")]
[name="斯第奇·画布"]我不会让你进来的！
[Character]
[name="嘉维尔"]那可就，由不得你了。
[Dialog]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_doorbreak",volume=0.7)]
[PlaySound(key="$d_avg_rockfall",delay=0.5,volume=0.7)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Image(image="30_i08", xScale=1.2, yScale=1.2, x=-100,y=150,fadetime=0)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=0.9, yScaleTo=0.9,xTo=0, yTo=50, duration=30, block=false)]
“轰”的一声，门连带着周围的墙壁应声而倒，嘉

... (全文17416字符)
```

### level_act20side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="30_g6_reception",screenadapt="coverall")]
[Delay(time=1)]
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_566_1#1$1")]
[playMusic(intro="$storyendjp_intro",key="$storyendjp_loop", volume=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_566_1#1$1",focus=2)]
[name="克罗绮·砖石"]欸，您说到这个的话，我也想起来了。
[name="克罗绮·砖石"]几年前，我有参加过两次他和卡奇关于穹顶的竞稿会。
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_566_1#2$1",focus=2)]
[name="克罗绮·砖石"]那时，芬奇大师刚离开不久，而两个初露锋芒的新星都想用穹顶的改造方案证明自己。
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_566_1#1$1",focus=2)]
[name="克罗绮·砖石"]卡奇经常在会议上滔滔不绝，阐述自己的想法，解说自己设计的得意之笔。
[name="克罗绮·砖石"]而斯第奇，会把他那些精美的图纸铺在桌子上，然后就退到一旁。他好像并不愿意花费精力在解释上，他希望我们能自己领悟。
[name="克罗绮·砖石"]有的人喜欢卡奇的细致思路，也有的人认可斯第奇对自己作品的自信乃至自矜。他们无疑都当得起新星的称号。
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_566_1#7$1",focus=2)]
[name="克罗绮·砖石"]这场较量持续了几年，谁也没能真正获得多数人的认可，让自己的设计得以通过。
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_566_1#5$1",focus=2)]
[name="克罗绮·砖石"]直到从某一次开始，斯第奇不再出现。
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_566_1#5$1",focus=1)]
[name="耶奇·地心"]芬奇还在的时候，曾经和我聊起过这个话题，他说，他很担心自己这个徒弟的将来。
[name="耶奇·地心"]只是，你说的这些，旁人说再多也没有用，只有他自己想通，放下自己的傲慢，才有可能听取他人的意见。
[name="耶奇·地心"]否则，别说卡奇了，就算是嘉维尔那样强硬的人，恐怕也拿他没有办法。
[Character(name="avg_npc_564_1#1$1",name2="avg_npc_566_1#1$1",focus=2)]
[name="克罗绮·砖石"]即使嘉维尔真心想帮他，也不行吗？
[Character(name="avg_npc_564_1#7$1",name2="avg_npc_566_1#1$1",focus=1)]
[name="耶奇·地心"]如果真的有这样的办法，芬奇那老家伙应该早就尝试了吧。
[Character(name="avg_npc_564_1#9$1",name2="avg_npc_566_1#1$1",focus=1)]
[name="耶奇·地心"]但是，谁知道呢......卡奇和嘉维尔在性格上完全相反，他们两个一起去帮斯第奇的话，或许真的会发生什么奇迹吧。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Background(image="30_g8_malistroom",screenadapt="coverall")] 
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_1026_gvial2_1#9$1")]
[name="嘉维尔"]唉，毕竟是祖玛玛的朋友，不能对这些家伙下重手还挺麻烦的。
[Character(name="avg_1026_gvial2_1#5$1")]
[name="嘉维尔"]嗯？对了，你们应该认识祖玛玛吧？我是她的朋友。
[Character(name="avg_npc_576_1#1$1",name2="avg_npc_576_1#1$1")]
[name="奇怪的机械"]祖玛玛......确认身份，祖玛玛的朋友，嘉维尔。
[name="奇怪的机械"]祖玛玛说过，不能伤害嘉维尔。
[name="奇怪的机械"]我们不伤害嘉维尔。
[Character(name="avg_4054_malist_1#10$1")]
[name="斯第奇·画布"]什么？！
[Character(name="avg_1026_gvial2_1#3$1")]
[name="嘉维尔"]哈哈，之前看那家伙跟你们玩得挺开心的，没想到提她还真的有用。
[Character(name="avg_4054_malist_1#4$1")]
[name="斯第奇·画布"]啧！
[Dialog]
[PlaySound(key="$rungeneral",volume=0.7)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=1.5, block=true)]
[Delay(time=1)]
[Character(fadetime=0.3)]
[Delay(time=1)]
[Character(name="avg_1026_gvial2_1#10$1")]
[name="嘉维尔"]能不能帮我围住他？
[Character(name="avg_npc_576_1#1$1",name2="avg_npc_576_1#1$1")]
[name="奇怪的机械"]我们不会伤害际崖城的居民。
[Character(name="avg_1026_gvial2_1#10$1")]
[name="嘉维尔"]放心，我只是要带他去他应该去的地方而已。
[Character(name="avg_npc_576_1#1$1",name2="avg_npc_576_1#1$1")]
[name="奇怪的机械"]了解。我们相信嘉维尔，我们帮助嘉维尔。
[Dialog]
[playsound(key="$d_avg_robotwalk")]
[characteraction(name="left", type="move", xpos=-400, fadetime=1.5, block=true)]
[characteraction(name="right", type="move", xpos=-400, fadetime=1.5, block=true)]
[Delay(time=1)]
[Character(fadetime=0.3)]
[Delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.7)]
[Character(name="char_empty",name2="avg_4054_malist_1#3$1",fadetime=0.3)]
[characteraction(name="right", type="move", xpos=100, fadetime=0, block=false)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1.5, block=false)]
[Delay(time=1)]
[playsound(key="$d_avg_robotwalk")]
[Character(name="avg_npc_576_1#1$1",name2="avg_4054_malist_1#3$1",fadetime=0.5)]
[characteraction(name="left", type="move", xpos=-100, fadetime=0, block=false)]
[characteraction(name="left", type="move", xpos=100, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_576_1#1$1",name2="avg_4054_malist_1#3$1",focus=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="斯第奇·画布"]别拦我的路！
[Dialog]
[Character(name="char_empty",name2="avg_4054_malist_1#3$1",fadetime=0.3)]
[Blocker(a=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_4054_malist_1#3$1",fadetime=1)]
[Delay(time=2)]
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_4054_malist_1#3$1",focus=1)]
[name="嘉维尔"]斯第奇·画布，我问你一个问题。
[Dialog]
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_4054_malist_1#3$1")]
[characteraction(name="right", type="move", xpos=100, fadetime=1, block=false)]
[Delay(time=1)]
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_4054_malist_1#6$1",focus=2)]
[name="斯第奇·画布"]......我已经没有什么可跟你说的了！
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_4054_malist_1#6$1",focus=1)]
[name="嘉维尔"]说了这么多，你讨厌际崖城的居民吗？
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_4054_malist_1#5$1",focus=2)]
[name="斯第奇·画布"]......
[Character(name="avg_1026_gvial2_1#9$1",name2="avg_4054_malist_1#5$1",focus=1)]
[name="嘉维尔"]不，你不用回答。
[name="嘉维尔"]如果你讨厌这里的居民，那你来到地上后，就该留在那里，你完全可以不告诉我们有关你部族的危机。
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_4054_malist_1#5$1",focus=1)]
[name="嘉维尔"]但你还是做了。
[name="嘉维尔"]你虽然不想修穹顶，但你依然割舍不下这里，所以你才会把特米米和依娜姆带下来的。
[Character(name="avg_1026_gvial2_1#1$1",name2="avg_4054_malist_1#6$1",focus=2)]
[name="斯第奇·画布"]是又怎么样？
[Character(name="avg_1026_gvial2_1#8$1",name2="avg_4054_malist_1#6$1",focus=1)]
[name="嘉维尔"]那我很好奇，斯第奇。
[name="嘉维尔"]你有没有去问过那些否定你的人，他们为什么不喜欢你的方案？
[Character(name="avg_1026_gvial2_1#8$1",name2="avg_4054_malist_1#7$1",focus=2)]
[name="斯第奇·画布"]......没有。
[Character(name="avg_1026_gvial2_1#8$1",name2="avg_4054_malist_1#7$1",focus=1)]
[name="嘉维尔"]我想也是，这就像你刚才说的那些话，肯定也从来没有告诉过身边的人一样。
[name="嘉维尔"]实际上，你真正的想法也还没有告诉我。
[name="嘉维尔"]我知道，有些话很难开口。
[name="嘉维尔"]我的病人里也有不少死撑着不想告诉别人的人。
[name="嘉维尔"]不想给人添麻烦，觉得没人理解自己，就是嘴硬说不出口什么的，都有。
[name="嘉维尔"]但无论如何，不说的话，直到你死，都没人知道

... (全文24814字符)
```

### level_act20side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act20side/IC01.mp4")]
```

### level_act20side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_smithy", volume=0.3)]
[Subtitle(text="叮当、叮当。真是忙碌啊，阿卡胡拉人。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你问我们在做什么？哈，阿卡胡拉的战士们还能做什么？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="最伟大的武器，强大的造物，有了大祭司与依娜姆商会的协助，我们可以轻松创造更多的器械！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="征服！“贡业”！阿卡胡拉的名号将会响彻云霄！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.3, block=true)]
[Background(image="bg_village_2",screenadapt="coverall")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_071", name2="avg_npc_070", fadetime=0.7)]
[delay(time=0.7)]
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="激动的阿达克利斯人"] “贡业”，“贡业”，啊，这个词真是太美好了......是这么发音的吧，尤吉？
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]不是，哥哥。是“工业”。而且，你应该注意休息。而不是跑来搅和......呃，全自动种植砍伐一体化机器人“丛林三号”的作业。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]准确来说经过昨晚的报废和重修，现在已经是四号了。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]尤吉，我最近状态好得很，不用担心。真没想到，石头......哦，源石还能这么用，真是让人大开眼界！是新的技术？谁搞来的？
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]多半是依娜姆。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]啊......如同嘉维尔一般的怪力，又可以将上半身螺旋发射，甚至还能滞留在空中半分钟之久......
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]唔，确实很惊人，不过大祭司将那玩意当时的状态称之为“解体”。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]我以前就在想了，尤吉。你看，外面的大地如此广阔，我们现在有了这么多的......“汞业”！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]工业。而且这个词不是这么用的，大祭司说过。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]那无所谓，更重要的是越来越多的巨大机械！还有越来越简单的操作，越来越低的事故概率！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]现在我们是不是可以做更多事情？！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]......比如？
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]有点野心，弟弟，把目光放向整个萨尔贡，你想象到了吗——
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]喔，喔......
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]——我们的雕像！有三座山那么高！有两片湖那么大！！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]喔哦哦——！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]当然了，族长的雕像也得有......还有大祭司的！依娜姆的也不能落下......
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]最后，还需要一些纪念性质的......建筑！对！宫殿！我想想......用木头？不行，得是砂岩或者坚硬的石头......干脆用源石！对！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]用源石块堆起来！堆一个巨大的建筑！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]堆起来？什、什么形状？和那些神殿一样？
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]还是简单一些好，比如圆形......唔，石头堆不出圆形。那就逐层向上，从每个方向看都是三角形！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]哦......哦！三角！塔！剩下的只有取名了啊！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]......不过，说这些也没用了啊。嘉维尔说过，我这种病是看不到那一天的......
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]哥哥......不！我们只要改变一下思维，把宫殿变成哥哥的坟墓不就好了吗？
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]这下别说阿卡胡拉了，整个萨尔贡都不会忘记哥哥的，名字也有了，就叫“尤吉尤塔塔”！我们一定会在哥哥有生之年建完那座塔！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="尤塔"]尤吉......！
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="char_411_tomimi_1#1",fadetime=1.5)]
[delay(time=2)]
[name="特米米"]不要说这么不吉利的话啦......
[Character(name="avg_npc_071")]
[name="尤塔"]唔，特米米......你怎么还在这儿呢？
[Character(name="avg_npc_071")]
[name="尤塔"]我还以为昨天你就一刻不停地跑回去找嘉维尔和族长啦。
[character(name="char_411_tomimi_1#1")]
[name="特米米"]难得有机会回来看一看，我总不能那么快就走吧？
[Character(name="avg_npc_071")]
[name="尤塔"]也是。所以你今天来这里做什么？已经来打过招呼了吧？
[character(name="char_411_tomimi_1#5")]
[name="特米米"]其实......
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_4054_malist_1#1$1",fadetime=1.5)]
[delay(time=2)]
[name="刻薄的杜林人"]......
[Character(name="avg_npc_071")]
[name="尤塔"]喔，你是依娜姆提过的那个小个子。怎么，难道是来抱怨今天的伙食的？哎呀，我也觉得最近的饮食太清淡了点，没肉怎么行......
[character(name="avg_4054_malist_1#1$1")]
[name="刻薄的杜林人"]不，别的事。还有，我是斯第奇·画布。别只看着别人的身高，阿达克利斯人都是这样吗？
[character(name="char_411_tomimi_1#4")]
[name="特米米"]哈哈，其实不是这样的......
[Character(name="avg_4054_malist_1#2$1")]
[name="斯第奇·画布"]算了，毕竟是一帮为了尾巴粗细就能吵起架来的奇怪家伙......我应当尊重这种文化差异。
[character(name="char_411_tomimi_1#2")]
[name="特米米"]欸、欸......
[Character(name="avg_npc_071")]
[name="尤塔"]好，斯第奇，你有什么事吗？我们正在规划萨尔贡的宏伟“蓝秃”。
[Character(name="avg_npc_070")]
[name="尤吉"]蓝图。
[Character(name="avg_npc_071")]
[name="尤塔"]喔，对。蓝图，你听见了吗，杜林人。这可真是个伟大计划！
[character(name="char_411_tomimi_1#5")]
[name="特米米"]我觉得......一座夸张的大坟墓应该不算什么伟大计划......而且如果大家都有那么大的坟墓，这座雨林就装不下啦。
[Character(name="avg_npc_071")]
[name="尤塔"]别总是当做坟墓，就是纪念，纪念性质！
[Character(name="avg_npc_071")]
[name="尤塔"]建造得大一点，我也可以和族长和嘉维尔放在一起吧，后世会抱着孩子们在我们几人的雕像前讲述祖玛玛与“嘉维尔意志”的美谈......
[Character(name="avg_4054_malist_1#10$1")]
[name="斯第奇·画布"]（我开始怀疑我的决定了......）
[character(name="char_411_tomimi_1#1")]
[name="特米米"]......！但、但是......
[Character(name="avg_4054_malist_1#1$1")]
[name="斯第奇·画布"]是的，眼下我们不该——
[character(name="char_411_tomimi_1#1")]
[name="特米米"]——但是这样就不能叫“尤吉尤塔塔”了！嘉维尔必须出现在名字里！我、我也可以顺便......！
[Character(name="avg_4054_malist_1#10$1")]
[name="斯第奇·画布"]......
[character(name="char_411_tomimi_1#1")]
[name="特米米"]啊，不是......是这样，依娜姆和斯第奇先生好好聊过了，我打算让大家都听听他说的事情。
[character(name="char_411_tomimi_1#1")]
[name="特米米"]毕竟事关重大，我也留了给嘉维尔的信，不知道她们能不能赶到......
[Character(name="avg

... (全文17379字符)
```

### level_act20side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="30_g4_durinsquare",screenadapt="coverall")] 
[Image(image="30_i10", xScale=0.9, yScale=0.9,x=-50,fadetime=0)]
[ImageTween(xTo=20, duration=30, block=false)]
[Delay(time=1)]
[playMusic(intro="$holiday_intro",key="$holiday_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
数日后
今天，斯第奇也在广场上努力着。
打扮城市的遗容与前往地面一样，都是需要全城居民来监督的行动。
而穹顶作为一座城市的脸面，自然是重中之重。
因此，就变成了需要在广场上当着所有人的面进行设计工作。
耶奇大师美其名曰：节省时间。
[name="斯第奇·画布"]可恶的臭老头，一定只是单纯觉得这样比较有趣。
斯第奇看着耶奇在下面洋洋得意的样子，气得牙痒痒。
不过，就连他自己都没有想到，他其实适应得并不慢。
当他不得不面对路过的人的问询，当他即使不想听也听到了其他人的意见，当他甚至因为坚持自己的意见而和人大吵一架时——
这一切并没有如想象中那样给他带来压力。
正如对现在在下方坏笑的耶奇老头那样，他虽然恨得牙痒痒，但他知道了别人是怎么想的。
就像别人也知道了他是怎么想的一样。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_564_1#7$1")]
[name="耶奇·地心"]这小子，结果这几天没少跟人吵架。
[name="耶奇·地心"]别人提一点意见都要和人争个半天。
[Character(name="avg_npc_564_1#10$1")]
[name="耶奇·地心"]不过，给出的东西倒确实让人没话说。
[Character(name="avg_npc_564_1#2$1")]
[name="耶奇·地心"]啧啧，芬奇啊，虽然不知道你这老小子现在在干什么，不过你应该可以放心了。
[Character(name="avg_npc_564_1#5$1")]
[name="耶奇·地心"]哦，对了对了。
[name="耶奇·地心"]斯第奇！
[Character(name="avg_4054_malist_1#7$1")]
[name="斯第奇·画布"]干什么，我忙着呢！
[Character(name="avg_npc_564_1#5$1")]
[name="耶奇·地心"]斯第奇，在先前检查穹顶的时候，有人在穹顶的尖端发现了一封信。
[Character(name="avg_4054_malist_1#4$1")]
[name="斯第奇·画布"]信？
[Character(name="avg_npc_567_1#1$1")]
[name="卡奇·叙光"]对，而且，是给你的信。
[Character(name="avg_4054_malist_1#4$1")]
[name="斯第奇·画布"]难道说......？！
[Dialog]
[Character]
[PlaySound(key="$d_avg_paper2")]
[Delay(time=1)]
[Blocker(a=0.8, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="我是芬奇·画布，际崖城最伟大的建筑设计师。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这封信被我放在了穹顶之尖。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="打开它的应该是下一任负责改造这个穹顶的人。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我希望那会是我最亲爱的徒弟。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这是我留给他的信。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但如果那个人不是他，那么，请你不要交给他。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="因为这说明他失败了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Background(image="30_g9_collapsedtunnel",screenadapt="coverall")] 
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#6$1",focus=2)]
[name="黛柯绮·银币"]卡奇，对不起。
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#6$1",focus=1)]
[name="卡奇·叙光"]嗯？
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#6$1",focus=2)]
[name="黛柯绮·银币"]如果我也像你一样......
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#6$1",focus=1)]
[name="卡奇·叙光"]每个人的性格都不一样，你的想法我也能够理解。
[name="卡奇·叙光"]只能说，我如果早一点察觉到的话，事情可能会不太一样吧。
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#5$1",focus=2)]
[name="黛柯绮·银币"]你现在留下来也没关系的。
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_569_1#5$1",focus=1)]
[name="卡奇·叙光"]没事的。
[Character(name="avg_npc_571_1#9$1")]
[name="极境"]唉，总觉得对你做了不好的事情啊，卡奇老弟。
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_571_1#9$1",focus=1)]
[name="卡奇·叙光"]不会啊，极境哥，我很感谢你当时给我的建议。
[name="卡奇·叙光"]虽然一开始确实是为了刺激斯第奇做出的决定，但是，我也是真心想要找到芬奇大师的踪迹的。
[name="卡奇·叙光"]别的不说，告诉他斯第奇现在的状况，他老人家一定也会开心吧。
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_571_1#1$1",focus=2)]
[name="极境"]你啊，真是让人不知道说什么好。
[name="极境"]说起来，那位芬奇大师既然还是很关心弟子的，我猜测，他也有可能前往地上寻找解决矿石病的方法。
[name="极境"]我回去之后，也会想办法找一找他的踪迹。
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_571_1#2$1",focus=2)]
[name="极境"]哈，有一天他找到了我们罗德岛也说不定呢。
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_571_1#2$1",focus=1)]
[name="卡奇·叙光"]啊，那太好了！
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_571_1#1$1",focus=2)]
[name="极境"]你知道我说这些的意思，对吧？
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_571_1#1$1",focus=1)]
[name="卡奇·叙光"]嗯，我们还会再见面的。
[name="卡奇·叙光"]我还想着重建际崖城的时候能够出一份力呢。
[name="卡奇·叙光"]到时候，我一定要和斯第奇一起做一些了不起的设计。
[dialog]
[Character(name="avg_npc_567_1#1$1",name2="avg_npc_571_1#4$1",focus=2)]
[PlaySound(key="$d_avg_inspiration",volume=0.6)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[name="极境"]比如一座我的雕像？
[Character(name="avg_npc_567_1#4$1",name2="avg_npc_571_1#4$1",focus=1)]
[name="卡奇·叙光"]这——恐怕还是不行。
[Character(name="avg_npc_567_1#4$1",name2="avg_npc_571_1#9$1",focus=2)]
[name="极境"]可惜！
[Dialog]
[Character(fadetime=0.5)]
[PlaySound(key="$d_avg_paper2")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.8, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="首先，老师要为自己的离开道歉。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但如果我不这么做，以你的性格，你将永远无法独立。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="好吧，主要是我如果留在你身边，也没法真的把你放着不管。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你很有天赋，斯第奇·画布。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="矿石病让你的生命变得短暂，但是同时，它也让你对生命的思考变得更加深刻。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这让你的风格有了进一步的蜕变。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这些，我都看在眼里。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Background(image="bg_caveentrance",screenadapt="coverall")] 
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_071")]
[playsound(key="$d_avg_axehitscrape")]
[Block

... (全文18566字符)
```

### training_act20side_01_a

```
[HEADER(is_tutorial=true, is_skippable=true)] 活动20side教学关1_a

[Battle.Pause]

[Tutorial(protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
际崖城的路边经常会出现<@tu.kw>自走车出发点</>。虽然我还没试过，不过，据说它可以用来发射自走车。

[Battle.Pause(pause=false)]
[Delay(time=3)]
[Battle.Pause(pause=true)]

[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]

[InputBlocker(blockInput=true, validX=205, validY=165, validWidth=150, validHeight=150)]

[Tutorial(waitForSignal="char_info", focusX=205, focusY=165, focusWidth=150, focusHeight=150, \
          animStyle="Click", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这就是<@tu.kw>自走车出发点</>。
[InputBlocker(blockInput=true)]

[Delay(time=1)]

[Tutorial(target="btn_skill",  waitForSignal="use_skill", \
          animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_stward")] \
<@tu.kw>自走车出发点</>准备就绪后，可以消耗一定费用，往固定方向发射一辆<@tu.kw>自走车</>，让我来试试看......

[InputBlocker(blockInput=true)]

[Battle.Pause(pause=false)]
[Delay(time=3)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=230, focusY=-65, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_stward")] \
自走车出发后会沿指定方向<@tu.kw>直线行驶</>，对碰撞到的敌人造成<@tu.kw>无视闪避的物理伤害</>与<@tu.kw>短暂晕眩</>。

[Battle.Pause(pause=false)]
[Delay(time=1)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=240, focusY=-150, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_stward")] \
一旦撞上不可通行的地形，自走车就算是出局了。看来发射之前必须要想好啊。

```

### training_act20side_01_b

```
[HEADER(is_tutorial=true, is_skippable=true)] 活动20side教学关1_b

[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]

[PopupDialog(dialogHead="$avatar_stward")] 好像也有办法改变自走车的行驶方向，让自走车避开障碍。让我翻翻随车附赠的使用说明......
[PopupDialog(dialogHead="$avatar_ardign")] 史都华德，这个很简单的！只要自走车<@tu.kw>经过我方单位</>，就会<@tu.kw>沿着其部署方向行驶</>啦！

[InputBlocker(blockInput=false)]
[Battle.EnsureMinCost(cost=11)]
[Tutorial(waitForSignal="put_down", dialogHead="$avatar_ardign", animStyle="Drag", \
          startX=-60, startY=60, startAnchor="BottomRight", endX=230, endY=-110)] \
让我<@tu.kw>到这里</>实地演示一下吧！
[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_ardign", animStyle="Drag", \
          startX=315, startY=-70, endX=40, endY=-90)] \
记得让我<@tu.kw>向左部署</>哦！
[InputBlocker(blockInput=true)]
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]

[Battle.Pause(pause=false)]
[Delay(time=1)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=205, focusY=165, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_ardign", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
好了，再发射一次自走车试试看？
```

### training_act20side_01_c

```
[HEADER(is_tutorial=true, is_skippable=true)] 活动20side教学关1_c

[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]

[PopupDialog(dialogHead="$avatar_ardign")] 哇，又出现了好多源石虫！史都华德，等它们到我面前，你就用自走车对付它们，剩下的我来挡住！
[PopupDialog(dialogHead="$avatar_stward")] 等等，卡缇，我们还有更好的办法，可以用<@tu.kw>自走车单行道</>改变自走车的行驶方向，延长它的行驶路线。

[InputBlocker(blockInput=false)]
[Battle.EnsureMinCost(cost=11)]
[Tutorial(waitForSignal="put_down", dialogHead="$avatar_stward", animStyle="Drag", \
          startX=-60, startY=60, startAnchor="BottomRight", endX=-350, endY=-110)] \
只要把自走车单行道<@tu.kw>设置在那里</>......
[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_ardign", animStyle="Drag", \
          startX=-215, startY=-110, endX=-193, endY=90)] \
然后将其<@tu.kw>向上部署</>就好。
[InputBlocker(blockInput=true)]
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]

[PopupDialog(dialogHead="$avatar_stward")] 这样一来，<@tu.kw>自走车</>经过这里时，就会改变原有方向，向上行驶了！
[PopupDialog(dialogHead="$avatar_stward")] 需要注意的是，每个自走车单行道或者我方单位只能使一辆自走车转向<@tu.kw>一次</>。

[Tutorial(focusX=205, focusY=165, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
卡缇，让自走车从远距离消灭这些源石虫吧，我们专心对付面前的敌人，这样防线就能稳固住了。
```

### training_act20side_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动20side教学关1_d

[PopupDialog(dialogHead="$avatar_stward")] 咦，这里还有一本花哨的杂志，让我看看......里面说，可以去一个叫<@tu.kw>装备集换处</>的地方，收集<@tu.kw>各式各样的自走车装备</>。
[PopupDialog(dialogHead="$avatar_stward")] 在<@tu.kw>后院工坊</>中用收集到的装备改装自走车，就可以让自走车拥有<@tu.kw>个性化的外观</>以及<@tu.kw>额外的性能</>......看起来挺有趣的。等战斗结束后，卡缇想试试看吗？
[PopupDialog(dialogHead="$avatar_ardign")] 当然了！战斗结束之后，我们也去装备集换处看看吧！
```


## 统计

- 总字符数：357626
- 对话行数：2881


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
