# 明日方舟 · 活动剧情 · act10mini（6段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act10mini」完整剧情脚本（6个文件，1985行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act10mini
- 脚本文件数：6

### level_act10mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] Green spark
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_mini02_victoria_street_n",screenadapt="coverall")]
[playmusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]	
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="夜幕降临。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="源石锅炉的轰鸣声并未减弱，高大的烟囱上方依然烟雾缭绕。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="工人们脱掉了破旧的防护设备，将其交给来换班的工友。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="卡拉顿城的一天即将结束。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[Background(image="25_mini01_naturalspark",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)] 
1097年11月16日 9:50 P.M.
[dialog]
[character(name="avg_377_gdglow_1#1$1",fadetime=1.5)]
[delay(time=2)]
晚上九点，是附近感染者工厂换班的时间。
不少人会选择来夏栎小姐的店里消磨时间。
[character(name="avg_377_gdglow_1#2$1")]
但是店里能提供给他们的东西并不多。
一块粗糙的炸鳞肉，一碗寡淡的土豆汤食，一杯没什么味道的果酒。
[character(name="avg_377_gdglow_1#10$1")]
尽管如此，这里还是多了几个常客。
[dialog]
[character]
[Character(name="avg_npc_005", name2="avg_npc_002",fadetime=1.5)]
[delay(time=2)] 
[PlaySound(key="$clink")]
[Character(name="avg_npc_005", name2="avg_npc_002", focus=1)]
[name="工人吉姆斯"] 干杯！
[Character(name="avg_npc_005", name2="avg_npc_002", focus=2)]
[name="感染者阿石"] 干杯！
[Character(name="avg_npc_005", name2="avg_npc_002", focus=1)]
[name="工人吉姆斯"] 哈哈哈哈！小布朗德万岁！
[Character(name="avg_npc_005", name2="avg_npc_002", focus=2)]
[name="感染者阿石"] 小火花！再来一杯！
[character(name="avg_377_gdglow_1#11$1")]
[name="苏茜"] 给，你的果酒。
[name="苏茜"] 有什么好事哦？今天这么高兴？
[Character(name="avg_npc_005", name2="avg_npc_002", focus=1)]
[name="工人吉姆斯"] 小布朗德先生这个月给每个人多发了奖金！
[Character(name="avg_npc_005", name2="avg_npc_002", focus=2)]
[name="感染者阿石"] 说是奖金，其实也就是一百个便士。
[name="感染者阿石"] 这还是大家拼命赶工期赚来的。
[name="感染者阿石"] 不过你这么晚不回去，你老婆真的不揍你？
[Character(name="avg_npc_005", name2="avg_npc_002", focus=1)]
[name="工人吉姆斯"] 开玩笑！我可是一家之主！她怎么敢！
[Character(name="avg_npc_005", name2="avg_npc_002", focus=2)]
[name="感染者阿石"] 好，为一家之主干杯！
[Character(name="avg_npc_005", name2="avg_npc_002", focus=1)]
[PlaySound(key="$clink")]
[name="工人吉姆斯"] 干杯！
[name="工人吉姆斯"] 小火花！再来一杯！
[character(name="avg_377_gdglow_1#10$1")]
[name="苏茜"] 哈哈哈......吉姆斯先生你少喝一点，你夫人真的会生气哦。
[Character(name="avg_npc_005", name2="avg_npc_002", focus=2)]
[name="感染者阿石"] 小火花，之前我听店长说，店里有度数高一点的酒？
[name="感染者阿石"] 能给我们来点吗？
[character(name="avg_377_gdglow_1#8$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="苏茜"] 不！行！
[name="苏茜"] 夏栎小姐说了，高度数的酒对你们的身体一点好处都没有！
[character(name="avg_377_gdglow_1#9$1")]
[name="苏茜"] 阿石哥，要对自己好一点啊。
[Character(name="avg_npc_005", name2="avg_npc_002", focus=2)]
[name="感染者阿石"] 唉，有什么不好？
[name="感染者阿石"] 反正得了这个病，迟早都得死，死前......
[character(name="avg_377_gdglow_1#9$1")]
[name="苏茜"] 不准这么说！
[character(name="avg_377_gdglow_1#8$1")]
[name="苏茜"] 城里的医生说过，哪怕是矿石病，依据病人的个体情况不同，病情的发展也是不一样的！
[Character(name="avg_npc_005", name2="avg_npc_002", focus=2)]
[name="感染者阿石"] 别这么严肃嘛，我只是......
[character(name="avg_377_gdglow_1#9$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="苏茜"] 阿石哥！
[Character(name="avg_npc_005", name2="avg_npc_002", focus=2)]
[name="感染者阿石"] 呃......我在？
[character(name="avg_377_gdglow_1#8$1")]
[name="苏茜"] 请注意身体，好好活着！不要总是把那个词挂在嘴上！
[Character(name="avg_npc_005", name2="avg_npc_002", focus=2)]
[name="感染者阿石"] 呃......对不起？
[Character(name="avg_npc_005", name2="avg_npc_002", focus=1)]
[name="工人吉姆斯"] 你看看你，惹小火花生气咯。
[Character(name="avg_npc_005", name2="avg_npc_002", focus=2)]
[name="感染者阿石"] 唉，我不是那个意思。
[dialog]
[character]
[PlaySound(key="$dooropenquite", volume=0.6)]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_012",fadetime=1.5)]
[delay(time=2)]
[name="苦根"] 欸？今天挺热闹啊？
[character(name="avg_377_gdglow_1#11$1")]
[name="苏茜"] 晚上好，苦根先生！
[Character(name="char_empty", name2="avg_npc_002", focus=2)]
[name="感染者阿石"] 哟！这不是苦根老哥吗！来来来，一起喝！
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_npc_012", name2="avg_npc_002",fadetime=0.7)]
[delay(time=1.5)]
[Character(name="avg_npc_012", name2="avg_npc_002",focus=1)]
[name="苦根"] 哎呦？看起来今天遇到好事了？
[character(name="avg_377_gdglow_1#1$1")]
卡拉顿城的感染者社区中有很多怪人，苦根先生应该算是其中一个。
[character(name="avg_377_gdglow_1#2$1")]
苦根先生隶属于一个叫作罗德岛的组织，是城镇议会里的贵族雇来的“专业人士”。
[character(name="avg_377_gdglow_1#12$1")]
但是罗德岛对待感染者的态度，却令人难以理解。
“罗德岛会协助卡拉顿城镇议会为感染者提供医疗帮助”，这是他们的公开说法。
[character(name="avg_377_gdglow_1#5$1")]
为什么会有人......甚至是一群外人，愿意主动向感染者提供帮助呢？
[Character(name="avg_npc_005", name2="avg_npc_012",focus=1)]
[name="工人吉姆斯"] 今天不忙了？居然有时间来喝酒？
[Character(name="avg_npc_005", name2="avg_npc_012",focus=2)]
[name="苦根"] 还好，最近招到了几个员工，人手充足了不少。
[Character(name="avg_npc_005", name2="avg_npc_012",focus=1)]
[name="工人吉姆斯"] 欸？罗德岛的工作好做吗？薪水怎么样？
[Character(name="avg_npc_005", name2="avg_npc_012",focus=2)]
[name="苦根"] 怎么，有兴趣了？
[Character(name="avg_npc_005", name2="avg_npc_012",focus=1)]
[name="工人吉姆斯"] 算啦算啦，我都不识字......就不自讨没趣了。
[character(name="avg_377_gdglow_1#5$1")]
起初，感染者社区的人并不信任他们，甚至还有人谣传他们会抓走重症的感染者做实验。
[character(name="avg_377_gdglow_1#2$1")]
但是罗德岛用行动证明了，他们是真的在帮助感染者。
[character(name="avg_377_gdglow_1#1$1")]
矿石病病情的诊断，矿石病急性发作的救治，甚至是普通工伤的处理，只要去了罗德岛医疗站，都能得到帮助。
[character(name="avg_377_gdglow_1#3$1")]
时至今日，依然有很多人怀疑罗德岛的动机。但是至少在这间小店里的客人都是信任他们的。
[Character(name="avg_npc_005", name2="avg_npc_012",focus=2)]
[name="苦根"] 说起来，吉姆斯，我刚才在路上看到你的夫人了。
[Character(name="avg_npc_005", name2="avg_npc_012",focus=1)]
[name="工人吉姆斯"] 啊？啊？？你确定？？糟......
[name="工人吉姆斯"] 咳咳

... (全文46629字符)
```

### level_act10mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="25_mini02_victoria_street_n",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
1097年11月19日 9:20 P.M.
[dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[Character(name="avg_npc_020",name2="avg_npc_020",fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="保安A"] 走这边。
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[characteraction(name="left", type="move", xpos=-500, fadetime=1.5,block=false)]
[characteraction(name="right", type="move", xpos=-500, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[PlaySound(key="$rungeneral", volume=0.9)]
[Character(name="avg_npc_020",name2="avg_npc_020",fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="保安A"] 前面。
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[characteraction(name="left", type="move", xpos=-500, fadetime=1.5,block=false)]
[characteraction(name="right", type="move", xpos=-500, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="保安A"] 还在前面，我好像看见她了。
[name="保安A"] 等等，这块路牌，我们刚才是不是见过？
[Character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="保安B"]我们回到原地了，我是说，又回到原地了。
[name="保安B"]那我说对了，那个菲林的源石技艺肯定有鬼。
[Character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="保安A"] 先别急，前面就是感染者社区了，那个小贼肯定就躲在里面。
[name="保安A"] 该死的感染者......今天就是把这里掀个底朝天也要把那个贼揪出来，看谁敢拦我们。
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_020",fadetime=1.5)]
[delay(time=2)]
[name="保安队长"] 算了，回去吧。
[Character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="保安A"] 头儿，就这么放过她，那些钱和东西就不管了......？
[character(name="avg_npc_020")]
[name="保安队长"] 算了算了，统共就那么点东西，这点钱大家凑一凑垫上吧。
[name="保安队长"] 老爷反复交代过，绝对不许多生事端。
[name="保安队长"] 谁要是给老爷惹了不必要的麻烦，那就不只是开除的事了。
[name="保安队长"] 先撤吧。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1)]
[delay(time=2)]]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_141_nights_1#8$1",fadetime=1.5)]
[delay(time=2)]
[name="夜烟"]呵呵~
[name="夜烟"]想要抓住猫猫的话，得再聪明一点才行哦~
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_indoor_u",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_141_nights_1#1$1",fadetime=1.5)]
[delay(time=2)]
[name="夜烟"]小敏，你在吗？
[character(name="avg_npc_045_nn_1")]
[name="感染者少女"]女巫姐姐！
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]给，今天的饭和药。
[character(name="avg_npc_045_nn_1")]
[name="感染者少女"]谢谢姐姐。
[character(name="avg_141_nights_1#11$1")]
[name="夜烟"]好啦，慢点吃，别噎到了。
一块干面包，一顿充饥的饭。
我是什么时候开始施舍他人的呢？
明明自己的生活已经难以为继了。
[character(name="avg_141_nights_1#9$1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="夜烟"]咳......咳......
[character(name="avg_npc_045_nn_1")]
[name="感染者少女"]姐姐你......脸色好差哦。
[character(name="avg_141_nights_1#2$1")]
[name="夜烟"]是吗......有那么明显吗？
[character(name="avg_npc_045_nn_1")]
[name="感染者少女"]女巫姐姐，我什么时候也能像你一样使用源石技艺啊？
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]现在还不可以哦~
[character(name="avg_npc_045_nn_1")]
[name="感染者少女"]欸......可是我也想变成女巫，像你那样。
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]等你再长大一点吧，小猫猫。
[character(name="avg_141_nights_1#9$1")]
[name="夜烟"]咳......咳......
[dialog]
[character]
刺痛。
矿石病病灶的刺痛从三个月前起就再也没有停止过。
也许自己也该离开这个地方了。
结晶粉尘化的时候，误伤到别人可不好。
不，对于一只优雅的猫来说，对于一个巫女林的术师来说——
离开这个世界的时候，也必须是孤独而优雅的。
[dialog]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_141_nights_1#1$1",fadetime=1)]
[Delay(TIME=1)]
[name="夜烟"]一家、两家、三家......
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]七只、八只、九只......
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]你猜猜，这片感染者区里，一共有几家酒馆，几只流浪猫？
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]我数得很清楚喔，一共有八家酒馆，三十二只流浪猫。
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]每家酒馆可以分到四只猫咪，每只猫咪都可以分到新鲜的鳞。
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]有没有算过，自己已经走过了多少个城市，去过几个感染者聚集区？
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]我记得，是五个城市，八个感染者聚集区，十七次越狱。
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]走过这么多城市，卡拉顿城算得上是相当有趣的一个地方了。
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]所有人都是一样，天亮了就去赚钱，天黑了就去喝酒。眼睛闭上的时候就绝不会为第二天的事担忧。
[character(name="avg_141_nights_1#9$1")]
[name="夜烟"]感染者，普通人，又有什么区别呢？
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]说不定哪一天，“轰隆”一声，整个卡拉顿港区全部掉进海里，就全都结束啦~
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]所以，如果要挑一个葬身之地的话，这倒是个不错的地方。
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]在一个可以俯视整个卡拉顿城的地方，全身变成一整块石头，然后，“嘭”的一下。
[character(name="avg_141_nights_1#1$1")]
[name="夜烟"]什么都不留下，谁也不知道——但还是要找个远些的地方，免得粉尘随风飘过去。
[character(name="avg_141_nights_1#3$1")]
[name="夜烟"]身体里的那些石头似乎平静下来了......
[character(name="avg_141_nights_1#3$1")]
[name="夜烟"]看来还不是时候，至少不是今天。
[character(name="avg_141_nights_1#8$1")]
[name="夜烟"]在那一天来临之前，还是要先考虑一下明天该上哪玩才行。
[character(name="avg_141_nights_

... (全文32761字符)
```

### level_act10mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]《终将同行》We Will All Go Together
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_manorindoor",screenadapt="coverall")]
[delay(time=1)]
[PlaySound(key="$d_avg_crwddiscuss_inside", channel="slide", loop=true, volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]	
[delay(time=1)]
1097年11月23日 8:45 P.M.
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_166_skfire_1#7$1",name2="char_empty",fadetime=1.5)]
[delay(time=2)]
[name="天火"] 哼，累死我了......
[name="天火"] 都是什么人啊，提的都是什么意见啊，他们脑子里想的都是什么啊？
[name="天火"] 那帮议员根本就是——
[stopsound(channel="slide", fadetime=3)]
[character(name="avg_166_skfire_1#4$1",name2="char_empty")]
[name="天火"] 根本就是——一群蠢货！！
[dialog]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_166_skfire_1#4$1", name2="avg_4016_kazema_1#2$1",fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_166_skfire_1#4$1", name2="avg_4016_kazema_1#2$1", focus=2)]
[name="记录员凯特"] 噗。
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Character(name="avg_166_skfire_1#9$1", name2="avg_4016_kazema_1#2$1", focus=1)]
[name="天火"] 要把他们说的那些车轱辘话记下来，也真是为难你了......
[Character(name="avg_166_skfire_1#7$1", name2="avg_4016_kazema_1#2$1", focus=1)]
[name="天火"] 他们根本就不是为了感染者在提议案，一个判定感染者身份的机构能做多少文章，是以为别人看不出来他们什么意思吗？
[name="天火"] 由什么机构来判定，判定之后以什么标准进行工作分配，哪些单位可以优先接收感染者员工......我当然知道，这里面都是利益。
[name="天火"] 他们没有谈感染者的实际情况，但也没去争这个利，就用假惺惺的车轱辘话说这么长时间，有什么意义？
[Character(name="avg_166_skfire_1#7$1", name2="avg_4016_kazema_1#11$1", focus=2)]
[name="记录员凯特"] 议员们都是些贵族，他们会不会考虑感染者的实际情况这一点先不提，他们是不能把分蛋糕的讨论摆在台面上的。
[Character(name="avg_166_skfire_1#8$1", name2="avg_4016_kazema_1#11$1", focus=1)]
[name="天火"] 这场会开下来，什么事情都没谈成！每个人都把感染者挂在嘴边，但进度完全是零！
[name="天火"] 所有人都在否定他人的提案，但也没人拿出有用的解决办法，他们拿出来的那些提案都算什么啊？
[Character(name="avg_166_skfire_1#8$1", name2="avg_4016_kazema_1#9$1", focus=2)]
[name="记录员凯特"] 这就是他们的隔空交锋过程啊，天火。在维多利亚城镇议会里，你刚才说的这些利益分配，在落实之前都要先走一次这样的体面流程。
[Character(name="avg_166_skfire_1#9$1", name2="avg_4016_kazema_1#9$1", focus=1)]
[name="天火"] 然后还有那个钱威议员——
[name="天火"] 还说自己是为了让感染者能赚更多的钱，得到更自由的选择，帮他们提高生活质量，把自己说得有多仁慈。
[Character(name="avg_166_skfire_1#9$1", name2="avg_4016_kazema_1#10$1", focus=2)]
[name="记录员凯特"] “如果不限制感染者们的工作时长，他们就可以自由地选择自己的工作时间，从而赚取更多的工钱。”
[Character(name="avg_166_skfire_1#10$1", name2="avg_4016_kazema_1#10$1", focus=1)]
[name="天火"] 你学得好像哦。
[Character(name="avg_166_skfire_1#6$1", name2="avg_4016_kazema_1#10$1", focus=1)]
[name="天火"] ......他那假惺惺语气真的好让我恶心！
[Character(name="avg_166_skfire_1#7$1", name2="avg_4016_kazema_1#10$1", focus=1)]
[name="天火"] 他自己心里清清楚楚，感染者那点工钱能有多少，最后赚的大头还不是进了自己口袋，还装出一副尽心尽力的样子......嘁。
[Character(name="avg_166_skfire_1#7$1", name2="avg_4016_kazema_1#1$1", focus=2)]
[name="记录员凯特"] 他确实提了解决方案——把感染者社区直接改建成工厂，这样人人有活干，有宿舍分配，还能养活自己。这也确实比大多数国家的政策好。
[Character(name="avg_166_skfire_1#4$1", name2="avg_4016_kazema_1#1$1", focus=1)]
[name="天火"] 呵！
[Character(name="avg_166_skfire_1#7$1", name2="avg_4016_kazema_1#1$1", focus=1)]
[name="天火"] ......
[name="天火"] 这里的人，都太自大了。
[Character(name="avg_166_skfire_1#7$1", name2="avg_4016_kazema_1#9$1", focus=2)]
[name="记录员凯特"] 嗯，突然？
[Character(name="avg_166_skfire_1#9$1", name2="avg_4016_kazema_1#9$1", focus=1)]
[name="天火"] 比如那几个反对感染者新政策的贵族......
[name="天火"] 他们说要把城里所有外来的感染者都赶出去，不论那些人来了多久，有没有成家，是不是已经适应了这里......
[Character(name="avg_166_skfire_1#7$1", name2="avg_4016_kazema_1#9$1", focus=1)]
[name="天火"] 他们的提案就是把这些人全都赶出去，然后呢？就让那些感染者流民在荒地上自生自灭？
[Character(name="avg_166_skfire_1#4$1", name2="avg_4016_kazema_1#9$1", focus=1)]
[name="天火"] 他们有没有想过这些走投无路的人最后会去哪里？
[Character(name="avg_166_skfire_1#4$1", name2="avg_4016_kazema_1#2$1", focus=2)]
[name="记录员凯特"] 噗。
[Character(name="avg_166_skfire_1#4$1", name2="avg_4016_kazema_1#9$1", focus=2)]
[name="记录员凯特"] 唉，这就是议会呀。
[Character(name="avg_166_skfire_1#8$1", name2="avg_4016_kazema_1#9$1", focus=1)]
[name="天火"] 什么......？
[Character(name="avg_166_skfire_1#8$1", name2="avg_4016_kazema_1#9$1", focus=2)]
[name="记录员凯特"] 这就是议会呀。
[Character(name="avg_166_skfire_1#8$1", name2="avg_4016_kazema_1#11$1", focus=2)]
[name="记录员凯特"] 如果这里谁都真的为了感染者谋利益，那就不叫议会了，叫感染者帮助协会。
[name="记录员凯特"] 双方的目的都很明确，他们首先在公开场合抛出最不可能实现的方案，然后再在交涉中互相让步，寻求平衡点，这也是常态。
[name="记录员凯特"] 倒是那位“白狼”伯爵，很多人都指望他表态呢。没想到今天竟然投了弃权票。
[Character(name="avg_166_skfire_1#6$1", name2="avg_4016_kazema_1#11$1", focus=1)]
[name="天火"] “白狼”斯卡曼德罗斯吗......这半年来他在议会上就没有公开表达过任何观点。也不知道为什么......
[name="天火"] 不是啊......不该是这样的......
[Character(name="avg_166_skfire_1#8$1", name2="avg_4016_kazema_1#11$1", focus=1)]
[name="天火"] 啊——他们今天这一屋子人，是我天真了。
[name="天火"] 我以为起码会有几个脑袋稍微清醒一点的人，就算是为了整个卡拉顿的平稳运作，也能提出几个正常一点的议案。
[Character(name="avg_166_skfire_1#3$1", name2="avg_4016_kazema_1#11$1", focus=1)]
[name="天火"] ......但他们只是把议会当作互相博弈的场所罢了，他们所有的心思，都只在如何给自己谋利益上。
[Character(name="avg_166_skfire_1#3$1", name2="avg_4016_kazema_1#8$1", focus=2)]
[name="记录员凯特"] 唔，大小姐啊，你刚才已经讲过这个了，我们在进去旁听之前，你就知道他们都是逐利的人了吧？这个事实本身不该再让你吃一惊啊。
[name="记录员凯特"] 稍等，你不是不怎么喝酒的......
[Character(name="avg_166_skfire_1#1$1", name2="avg_4016_kazema_1#8$1", focus=1)]
[name="天火"] ......觉得自己这样没问题的话，迟早会出大事的！！
[Character(name="avg_166_skfire_1#1$1", name2="avg_4016_kazema_1#9$1", focus=2)]
[name="记录员凯特"] 嗯嗯？
[Character(name="avg_166_skfire_1#4$1", name2="avg_4016_kazema_1#9$1", focus=1)]
[name="天火"] 迟早有一天会出事的！一直压迫，一直压榨，这样的状态能持续多久？他们难道真的不明白吗？没有人愿意这样活的......
[name="天火"] 哪怕只有一点点希望，那些人也是愿意的，他们会努力活下去的，我知道的！
[Character(name="avg_166_skfire_1#4$1", name2="avg_4016_kazema_1#9$1", focus=2)]
[name="记录员凯特"] ......蒙贝兰小姐，你前后的话有点接不上了哦。
[Character(name="avg_166_skfire_1#6$1", name2="avg_4016_kazema_1#9$1", focus=1)]
[name="天火"] 没有人生来就是恶人，没有人生来就会以剥夺他人的生命为乐......他们最开始就只是一群想努力生活的感染者。
[Character(name="avg_166_skfire_1#6$1", name2="avg_4016_kazema_1#9$1", focus=2)]
[name="记录员凯特"] 嗯——我也只是一个想努力让你别再喝的朋友。
[Character(name="avg_166_skfire_1#4$1", name2="avg_4016_kazema_1#9$1", focus=1)]
[name="天火"] 他们就该低人一等吗，就该躲躲藏藏吗？那些贵族，就该是生来就高贵的，就该压榨他们来换取利益吗？
[name="天火"] 简直愚蠢！他们要是一直不知收敛，感染者们迟早会爆发的......
[Character(name="avg_166_skfire_1#8$1", name2="avg_4016_kazema_1#9$1

... (全文33529字符)
```

### level_act10mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_storehouse",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
1097年11月19日 7:44 A.M.
[dialog]
[Character(name="avg_220_grani_1#1$1",name2="avg_npc_329_1#1$1",fadetime=0.7)]
[delay(time=0.7)]
[Character(name="avg_220_grani_1#1$1",name2="avg_npc_329_1#1$1",focus=1)]
[name="格拉尼"]所以你们也记不得是什么时候被人打开的？
[Character(name="avg_220_grani_1#1$1",name2="avg_npc_329_1#1$1",focus=2)]
[name="感染者毕恩"] 至少得是两个月前了。
[Character(name="avg_220_grani_1#1$1",name2="avg_npc_329_1#1$1",focus=2)]
[name="感染者毕恩"]不过这边本来就是用木头封死的，之前有几个孩子调皮，把木板拆了爬进去，说不定这次也一样。
[Character(name="avg_220_grani_1#1$1",name2="avg_npc_329_1#1$1",focus=1)]
[name="格拉尼"]你们看到有人进出吗？
[Character(name="avg_220_grani_1#1$1",name2="avg_npc_329_1#1$1",focus=2)]
[name="感染者毕恩"]没有，这下面黑灯瞎火的，谁没事往下爬啊。
[Character(name="avg_220_grani_1#6$1",name2="avg_npc_329_1#1$1",focus=1)]
[name="格拉尼"]行......我知道了。
[Character(name="avg_220_grani_1#2$1")]
[name="格拉尼"]唉，果然还是不行啊......明明那么可疑。到现在为止，我都已经查到六个被重新启用的废弃结构层出入口了。
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]很多证人也能证明地下通道晚上确实有拖动东西的声音。感染者社区的氛围也不太对劲，总觉得有人在里面动手脚。
[Character(name="avg_220_grani_1#6$1")]
[name="格拉尼"]真的没人有理由启用这些废弃的出入口啊......
[Character(name="avg_220_grani_1#9$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="格拉尼"]（拍了拍脸）
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]算了，还是不想这些了。琐碎的小事和关系城市存亡的大事都一样重要，嗯！
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]我看看还有什么......哦对......贝希曼伯爵家的盗窃案。
[Character(name="avg_220_grani_1#6$1")]
[name="格拉尼"]这要从哪儿开始查起呢。
[Character(name="avg_220_grani_1#6$1")]
[name="格拉尼"]唉......会是谁呢？能从守卫森严的大贵族家偷东西，这不是普通的窃贼能做出来的事。
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]按伯爵家仆人的说法，那个盗贼在感染者社区神出鬼没，那么，他要么非常熟悉感染者社区的地形，要么掌握了特殊的源石技艺。
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]——当然，前提是他们没有为推卸责任而撒谎。
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]......嗯，应该不会。最近半个月我听到过很多起类似的报案，卡拉顿城应该确实有那么一个流窜的惯偷。
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]奇怪的盗贼、特殊的源石技艺......
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]算了，去感染者社区看看吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="21_G7_decisivebattlealley_d",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_243")]
[name="感染者市民"]小格拉尼，终于找到你了！
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]萨妮大婶？别着急别着急，有什么事吗？
[Character(name="avg_npc_243")]
[name="感染者市民"]我的小绒跑丢了，我已经找了两个小时了，快帮我找找它！它那么乖，从来没有瞎跑过，会不会是被什么坏人给......
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]别多想，大婶，我马上去帮您找！
[Character(name="avg_npc_243")]
[name="感染者市民"]谢谢，谢谢！
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]小绒跑丢之前发生过什么吗？您有没有问过周围的人？......啊，大婶，您别急，慢慢说......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
一小时后。
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]来，萨妮大婶，小绒找到了！
[Character(name="avg_npc_243")]
[name="感染者市民"]呀......让我看看。呼，还好还好......没有受伤。真对不起啊，小格拉尼，明知道你工作那么忙，还要用找宠物这样的小事来麻烦你。
[Character(name="avg_220_grani_1#9$1")]
[name="格拉尼"]才没有呢。要是小绒真的没了，您要伤心多久呀，这怎么能算是小事呢！
[Character(name="avg_npc_243")]
[name="感染者市民"]可是，我听隔壁的老约翰说，你在警备队处境也不是很好，前几天好像还因为什么事被训斥了......
[Character(name="avg_220_grani_1#5$1")]
[name="格拉尼"]哈哈哈......其实也没什么。
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]不过萨妮大婶，饲养羽兽的话，还是建议用笼子关起来哦......咬到人的话就不好了。
[Character(name="avg_npc_243")]
[name="感染者市民"]哎呀，你说的有道理。
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]说起来，萨妮大婶。你最近在感染者社区有见到什么陌生人吗？
[Character(name="avg_npc_243")]
[name="感染者市民"]陌生人？这个社区很多人都是从其他城市来的，有陌生人也不奇怪啊。
[Character(name="avg_220_grani_1#6$1")]
[name="格拉尼"]我指的是那种......嗯......比如掌握一些奇怪的源石技艺的感染者？
[Character(name="avg_npc_243")]
[name="感染者市民"]这个啊......
[Character(name="avg_npc_243")]
[name="感染者市民"]上个月感染者社区停电那个事情你知道吧。
[Character(name="avg_220_grani_1#3$1")]
[name="格拉尼"]啊！我知道，就是感染者社区的发电机被人恶意破坏那个案子？不过犯人一直没找到......
[Character(name="avg_220_grani_1#6$1")]
[name="格拉尼"]但是我听说供电很快就恢复了，有人修好了发电机？
[Character(name="avg_npc_243")]
[name="感染者市民"]是！我听说他们找来了一个很厉害的工程术师，几个小时不到就把发电机修好了！但是感染者社区怎么会有这么厉害的工程术师呢？
[Character(name="avg_220_grani_1#9$1")]
[name="格拉尼"]是......确实有点奇怪......
[dialog]
[character]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_offce",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
1097年11月20日 6:44 P.M.
[dialog]
[Character(name="avg_220_grani_1#1$1")]
[name="格拉尼"]这是我今天的工作报告，请长官过目。
[playsound(key="$d_avg_paper1",volume=0.8)]
[delay(time=1.2)]
[Character(name="avg_npc_241")]
[name="警备队长"]嗯，两起盗窃、卡拉顿城流言调查报告......都是什么玩意儿。
[PlaySound(key="$d_gen_doorclose",volume=0.6)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[Character(name="avg_npc_241")]
[name="警备队长"]贝希曼伯爵家的盗窃案呢！都多久了，进展呢！
[Character(name="avg_220_grani_1#6$1")]
[name="格拉尼"]那个，不是才一天多吗......
[Character(name="avg_npc_241")]
[name="警备队长"]一天还不够吗！
[Character(name="avg_220_grani_1#6$1")]
[name="格拉尼"]但......
[Character(name="avg_npc_241")]
[name="警备队长"]我花大力气借调你的时候，骑警队可是说你是查案的一把好手。结果呢？小小一个失窃，一天时间都不够吗！
[Character(name="avg_220_grani_1#6$1")]
[name="格拉尼"]（小声）明明是城镇议会借调的骑警队......
[Character(name="avg_npc_241")]
[name="警备队长"]够了！目无尊长，顶撞上级，这就是骑警队的规矩吗！
[Character(name="avg_220_grani_1#2$1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fa

... (全文30346字符)
```

### level_act10mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]《必有所偿》Somethin's gotta give 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_wild_m",screenadapt="coverall")]
[PlayMusic(intro="$newhope01_intro", key="$newhope01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]	
[delay(time=1)]
1097年11月26日 9:33 A.M.
卡拉顿城外四十公里处 荒地流民聚居区
[dialog]
[character(name="avg_492_quercu_1#2$1",fadetime=1.5)]
[delay(time=2)]
高多汀的德鲁伊站在荒地之上，静静地伫立在一座矮坟前。
[name="夏栎"] “他骗过了死亡。”
[name="夏栎"] “夺走了它唾手可得的胜利。”
[name="夏栎"] “他骄傲地前往自己的安眠之地。”
[character(name="avg_492_quercu_1#5$1")]
她呼喊着，挥舞着自己的法杖。
太阳升起，这只是泰拉荒地上一次平凡的葬礼。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]	
[character(name="avg_492_quercu_1#7$1",fadetime=1.5)]
[delay(time=2)]
[name="夏栎"] 来，说好的酒。
[name="夏栎"] 虽然不烈，但也别喝多了。
[character(name="avg_492_quercu_1#7$1",focus=-1)]
[name="冷静的荒地人"] 梅伊这瓶怎么办？
[name="冷静的荒地人"] 我想浇在这儿，埋她的地方。
[name="消沉的荒地人"] 唉。但这可是夏栎送的......
[character(name="avg_492_quercu_1#8$1")]
[name="夏栎"] 没事，还给大地吧。
[PlaySound(key="$pourwater")]
[character(name="avg_492_quercu_1#8$1",focus=-1)]
[name="消沉的荒地人"] 你说三个星期就能酿好。我们没想到她没熬过去。
[name="消沉的荒地人"] 唉，现在就只剩下我们两个人了。
[name="冷静的荒地人"] 好了，老哥，干杯吧。
[name="消沉的荒地人"] ......干杯。
[PlaySound(key="$clink")]
[character(name="avg_492_quercu_1#7$1")]
[name="夏栎"] 嗯，干杯。
[character(name="avg_492_quercu_1#7$1",focus=-1)]
[name="冷静的荒地人"] 这段时间卡拉顿城还是管得很严，夏栎，我们没办法进去找你。
[name="冷静的荒地人"] 不过我其实知道，找到你也没用，我们的病是治不了的，她就是到了那个时候。
[name="冷静的荒地人"] 只是最后那几天，她哭得太惨了。
[name="冷静的荒地人"] 唉，你送走过那么多人了，也知道他们有多痛苦。
[name="冷静的荒地人"] 她求我用法术给她个痛快，但我下不了手。
[name="冷静的荒地人"] ......然后第二天，我们在山坡底下找到了她。睡着了，闭着眼睛，再也不用流泪了。
[name="冷静的荒地人"] 周围没有人，她没感染到其他人，也没影响到我们。没事，一切都挺好。我就是觉得......
[character(name="avg_492_quercu_1#5$1")]
[name="夏栎"] 有点孤独，是吧？
[character(name="avg_492_quercu_1#5$1",focus=-1)]
[name="冷静的荒地人"] 嗯，孤独。
[name="冷静的荒地人"] 来，再碰一杯。
[PlaySound(key="$clink")]
[character(name="avg_492_quercu_1#5$1")]
[name="夏栎"] 嗯。
[character(name="avg_492_quercu_1#9$1")]
[name="夏栎"] 剩下的酒就别浇了，留给活着的人吧。
[character(name="avg_492_quercu_1#9$1",focus=-1)]
[name="消沉的荒地人"] 好，听你的。
[name="消沉的荒地人"] 哦对了，那位天灾信使——艾尔瓦小姐前几天来过了，这是她让我们交给你的信件。
[character(name="avg_492_quercu_1#4$1")]
[name="夏栎"] 是那“逐尘者”艾尔瓦的信？
[character(name="avg_492_quercu_1#4$1",focus=-1)]
[name="消沉的荒地人"] 是的，你之前不是委托她帮你调查大公爵部队的驻扎情况吗？
[name="消沉的荒地人"] 这几天经常能看到军队的车队一路向北，也不知道那些城里的大人物到底要干什么。
[character(name="avg_492_quercu_1#6$1")]
[name="夏栎"] ......反正不是什么好事，你们一定要注意安全。
[character(name="avg_492_quercu_1#5$1")]
[name="夏栎"] 唉，我也准备回去了，无论如何，你们都保重。
[character(name="avg_492_quercu_1#9$1")]
[name="夏栎"] 还有这些药你们留着。已经冬天了，这边会越来越冷的，如果生了冻疮，用这个就好。
[character(name="avg_492_quercu_1#9$1",focus=-1)]
[name="消沉的荒地人"] “霜星”......这药名字还真有意思。
[name="冷静的荒地人"] 夏栎，你这次走了，什么时候回来？
[character(name="avg_492_quercu_1#10$1")]
[name="夏栎"] 嗯......我不能确定。
[character(name="avg_492_quercu_1#10$1",focus=-1)]
[name="冷静的荒地人"] 好了，好了，我明白。
[name="冷静的荒地人"] 既然很难再见到了，我最后问你一个问题，行吗？
[character(name="avg_492_quercu_1#8$1")]
[name="夏栎"] 多少问题都行，酒还没喝完呢。
[character(name="avg_492_quercu_1#8$1",focus=-1)]
[name="冷静的荒地人"] 夏栎，你为什么要这么帮我们，那些药都不便宜吧？
[name="冷静的荒地人"] 你经常向我们这些荒地人打探消息，你到底是为谁工作的？
[name="冷静的荒地人"] 这么久了，大家也只是好奇......他们都说你以前是个军官......
[name="冷静的荒地人"] 我们其实不在乎你的身份，我们不讲城里人的大道理，你做的事让我们能活得更久，所以不管你做的是什么事，我们都帮你。
[character(name="avg_492_quercu_1#9$1")]
[name="夏栎"] 不，我想认真回答，但我觉得你们不会相信。
[character(name="avg_492_quercu_1#2$1")]
[name="夏栎"] 如果我说，有一群人始终在救助感染者，你们能相信吗？
[stopmusic(fadetime=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_towerinside",screenadapt="coverall")]
[Character]
[delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
1097年11月28日 2:28 P.M.
[dialog]
[Character(name="avg_492_quercu_1#1$1", name2="avg_4016_kazema_1#1$1",fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_492_quercu_1#1$1", name2="avg_4016_kazema_1#1$1", focus=2)]
[name="记录员凯特"] 所以高多汀大公爵真的带着军队前往伦蒂尼姆了？
[Character(name="avg_492_quercu_1#4$1", name2="avg_4016_kazema_1#1$1", focus=1)]
[name="夏栎"] 是，我确定。
[Character(name="avg_492_quercu_1#4$1", name2="avg_4016_kazema_1#10$1", focus=2)]
[name="记录员凯特"] 多大规模的军队？
[Character(name="avg_492_quercu_1#10$1", name2="avg_4016_kazema_1#10$1", focus=1)]
[name="夏栎"] 荒地流民看到了至少两艘高速战舰。天灾信使那边告诉我他们看到攻城团的炮兵也离开了驻地。
[Character(name="avg_492_quercu_1#10$1", name2="avg_4016_kazema_1#11$1", focus=2)]
[name="记录员凯特"] 这是个坏消息......八个大公爵都带着军队前往伦蒂尼姆......
[Character(name="avg_492_quercu_1#10$1", name2="avg_4016_kazema_1#10$1", focus=2)]
[name="记录员凯特"] 总之，有什么新消息我会给苦根队长报告的。
[Character(name="avg_492_quercu_1#10$1", name2="avg_4016_kazema_1#1$1", focus=2)]
[name="记录员凯特"] 对了，凯尔希医生委托的事情办好了，这些文件千万要保存好。
[Character(name="avg_492_quercu_1#10$1", name2="avg_4016_kazema_1#13$1", focus=2)]
[name="记录员凯特"] 这是四个公爵领地的大型移动平台出入许可，这是罗德岛在维多利亚的业务证明。
[Character(name="avg_492_quercu_1#10$1", name2="avg_4016_kazema_1#13$1", focus=1)]
[name="夏栎"] “废旧工业资源回收与处理”。
[Character(name="avg_492_quercu_1#1$1", name2="avg_4016_kazema_1#13$1", focus=1)]
[name="夏栎"] 为什么不使用正常的名头，医疗服务什么的。
[Character(name="avg_492_quercu_1#1$1", name2="avg_4016_kazema_1#9$1", focus=2)]
[name="记录员凯特"] 矿石病防治的业务在维多利亚极其严格，不同的公爵领地的管理方式完全不一样，很难办。这是最简单的方式了，我们需要先进去。
[Character(name="avg_492_quercu_1#10$1", name2="avg_4016_kazema_1#9$1", focus=1)]
[name="夏栎"] ......原来如此。
[Character(name="avg_492_quercu_1#10$1", name2="avg_4016_kazema_1#1$1", focus=2)]
[name="记录员凯特"] 还有，这个是海蒂女士的信，一定要亲手交给凯尔希医生！
[Character(name="avg_492_quercu_1#7$1", name2="avg_4016_kazema_1#1$1", focus=1)]
[name="夏栎"] 明白，你放心吧。
[Character(name="avg_492_quercu_1#7$1", name2="avg_4016_kazema_1#11$1", focus=2)]
[name="记录员凯特"] 我该回市政档案馆了......出来太久会被同事怀疑的。
[Character(name="avg_492_quercu_1#7$1", name2="avg_4016_kazema_1#9$1", focus=2)]
[name="记录员凯特"] 哦对了！有件事必须得告诉你。
[Character(name="avg_492_quercu_1#7$1", name2="avg_4016_kazema_1#8$1", focus=2)]
[name="记录员凯特"] 你之前当据点的那家店，就那家“绿意火花”，前几天被人纵火烧毁了。
[Character(name="avg_492_querc

... (全文49824字符)
```

### level_act10mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_desert_3",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
1097年12月21日 8:44 A.M.
骸骨荒原 古老废城高塔
陡峭峡谷之中矗立着难以判断年代的建筑物，这片废城的故事已经无从知晓。
不少人生活在废墟的阴影下，让这片死寂之地恢复了些许生机。
[dialog]
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",fadetime=0.7)]
[delay(time=0.7)]
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]给，土豆。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]产量怎么样？
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]......一辆房车里就能种出这么多土豆，长见识了。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]我以前真没见过这样的农场......
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]叫什么来着，这个技术？
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]哈哈哈......移动城市里的水培农场也是这几十年才开始普及的，你没见过很正常。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]Guard先生很熟悉这些？
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]罗德岛上有很多这样的农场，我见过不少，也懂那么一点点。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]不过光靠一辆房车肯定养不活所有人。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]不要着急，有那几位卡西米尔的学者帮忙，我们需要的只是时间。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]但是所有的技术，只有那个工程师和他的团队懂。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]如果没有他们，一切都白搭。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]我还是不信任他。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]为什么？
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]他甚至不是个感染者。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]因为他的妻子和女儿感染矿石病去世了，所以他就帮助我们？
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]他的生活陷入了困境，他因为命运的不公而愤怒，他和感染者产生了共情，所以他帮助我们。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]那假如有一天，他有了新的家庭，有了新的家人，支持感染者反而会影响他的正常生活。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]那么他会不会变卦？他会不会为了他的生活和家人背叛我们？
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]他毕竟不是一个感染者。他无法设身处地地和我们站在一起。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]你在假设还没有发生的背叛和恶行，不要把“非感染者”摆在我们的对立面。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]如果我们假设对待我们的善意都会变质，假设帮助我们的人总有一天会变卦。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]那么我们永远不会有朋友。合作总是建立在信任的基础上，“整合”两个字本来就是要去求同存异的。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]我们必须保证塔露拉那样的事情不会再出现一次。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]那么我们需要的是一种应急预案，我们需要对可能出现的危机有充足的准备，而不是始终提防着所有人。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]行吧。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]有没有人说过，你越来越像爱国者先生了。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]我怎么配和爱国者先生相提并论......
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]说起来，衣服怎么样？
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]小了一点，不过还行。
[Character(name="avg_npc_080")]
[name="整合运动成员"]这布料，应该是很耐磨的那种，不错嘛。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]是，这种布料便宜又实用，非常适合拿来做战斗服。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]以前哪儿还想过有这么一天。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]新衣服欸！我这得有好几年没穿过新衣服了。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]感谢那些卡拉顿城里的感染者工人吧。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]不过有一点我不是很理解。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]我们为什么要把整合运动的标记拆掉？
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]因为我们不需要那个标记了。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=1)]
[name="整合运动战士"]我们不需要整合运动了？
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]当然不是。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]我们只是不再需要明确的符号，我们也不需要一个标记来证明我们自己。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]把我们凝聚在一起的，是一种精神，而不是一个符号。
[Character(name="avg_npc_330_1#1$1",name2="avg_npc_327_1#1$1",focus=2)]
[name="Guard"]我们不应该把自己和其他感染者加以区分，而是应该帮助他们，成为支持那些感染者的力量。
[Character(name="avg_npc_080")]
[name="整合运动成员"]那为什么第四小队的人还穿着带标记的衣服？
[Character(name="avg_npc_327_1#1$1")]
[name="Guard"]他们的活动有特殊目的，第四小队在为我们打烟雾弹。
[Character(name="avg_npc_330_1#1$1")]
[name="整合运动战士"]我......我不太明白？
[Character(name="avg_npc_331_1#1$1")]
[name="幻影弩手"]他们穿着带标记的衣服在乌萨斯东边行动，就会吸引乌萨斯人的注意，让乌萨斯军队以为整合运动只剩下零散的个体游荡在东边的荒地。
[Character(name="avg_npc_331_1#1$1")]
[name="幻影弩手"]而其他人的行动就不会引起乌萨斯，甚至是其他各国的注意。
[Character(name="avg_npc_331_1#1$1")]
[name="幻影弩手"]他们会以为我们做的一切都只是缺乏组织的独立行为。没有人会觉得我们是整合运动，也没有人会重视我们。
[Character(name="avg_npc_330_1#1$1")]
[name="整合运动战士"]毕恩先生！你来了！
[Character(name="avg_npc_331_1#1$1")]
[name="幻影弩手"]报告，毕恩归队。
[Character(name="avg_npc_327_1#1$1")]
[name="Guard"]辛苦了！还顺利吗？
[Character(name="avg_npc_331_1#1$1")]
[name="幻影弩手"]没什么问题，雷德队长已经把设备送到库房那边去了。
[Character(name="avg_npc_327_1#1$1")]
[name

... (全文29538字符)
```


## 统计

- 总字符数：222627
- 对话行数：1985


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
