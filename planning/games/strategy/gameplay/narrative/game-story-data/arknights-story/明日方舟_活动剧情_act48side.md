# 明日方舟 · 活动剧情 · act48side（25段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act48side」完整剧情脚本（25个文件，2451行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act48side
- 脚本文件数：25

### level_act48side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, duration=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="69_g11_firsttemple_indoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, duration=1, block=true)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Delay(time=2)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_2081_1#1$1",duration=1)]
[Delay(time=2)]
[name="颓丧的男人"]我又梦到了当初在游击队里的事，卡珊卓拉小姐。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_2068_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="卡珊卓拉"]这是您这个月第三次拜访恩底弥翁神殿，找我解读梦境，墨格斯先生。
[name="卡珊卓拉"]您梦到的......仍是七年前的那个夜晚？
[charslot(slot="m",name="avg_npc_2081_1#1$1",focus="m")]
[name="颓丧的男人"]是的......
[name="颓丧的男人"]那个漆黑的夜晚，我们躲在树林里。萨尔贡人就堵在林子外，寻找我们的踪迹。
[name="颓丧的男人"]我们不能出声，更不能点灯，只能摸黑将手里的武器拆开。
[name="颓丧的男人"]螺帽、弹簧、源石元件......我把施术单元的配件一个个地系到衣服和鞋子上，伪装成装饰品。
[name="颓丧的男人"]恐惧令我浑身发冷，连源石元件划破手掌都毫无知觉，还以为手心里是汗水。
[name="颓丧的男人"]天亮了，我们装成附近村庄的伐木工，从萨尔贡人面前走过。要是暴露了，我们十几个人都会死......
[name="颓丧的男人"]他们面无表情地挨个儿扫视我们。有一瞬间，我以为他们发现了破绽，惊慌之下被树根绊了一跤，摔进泥地。
[name="颓丧的男人"]萨尔贡人哈哈大笑，说了一些像是嘲讽的话，用刀柄砸了我肩膀。但我很高兴，我知道我们安全了。
[charslot(slot="m",name="avg_npc_2068_1#4$1",focus="m")]
[name="卡珊卓拉"]......
[charslot(slot="m",name="avg_npc_2081_1#1$1",focus="m")]
[name="颓丧的男人"]最近这件事反复出现在我的梦里，您说......
[charslot(slot="m",name="avg_npc_2068_1#1$1",focus="m")]
[name="卡珊卓拉"]您想知道，这是否是个神谕？
[charslot(slot="m",name="avg_npc_2081_1#1$1",focus="m")]
[name="颓丧的男人"]卡珊卓拉小姐，去年在中央广场上，我亲眼见过英雄借您的声音开口，宣读他们的意志。
[name="颓丧的男人"]您是米诺斯众英雄的代言者，也是雅赛努斯城中唯一能区分普通梦境与神谕的祭司。
[name="颓丧的男人"]如果神谕为我指引的道路是再次拿起武器，那......即便我再恐惧......
[charslot(slot="m",name="avg_npc_2068_1#7$1",focus="m")]
[name="卡珊卓拉"]请坐下来，先生，您的腿在打颤，脸色也很不好。
[name="卡珊卓拉"]米诺斯的英雄不会迫使一位饱受战争痛苦的子民，回到他的噩梦之中。
[charslot(slot="m",name="avg_npc_2081_1#1$1",focus="m")]
[name="颓丧的男人"]您的意思是......？
[charslot(slot="m",name="avg_npc_2068_1#3$1",focus="m")]
[name="卡珊卓拉"]我想，您误读了神谕。
[name="卡珊卓拉"]智慧与勇气代替紧闭双眼的双月，照拂您和同伴，让你们在天亮时分脱困；您也从梦中醒来，迎接雅赛努斯美好的清晨......
[name="卡珊卓拉"]英雄般的美德本该得到嘉许，但七年来弥久不散的痛苦，让您忽略了命运的枝头已经结出甘美的果实......
[charslot(slot="m",name="avg_npc_2068_1#7$1",focus="m")]
[name="卡珊卓拉"]摘下它，先生，接受众英雄对您的赐福。
[charslot(slot="m",name="avg_npc_2081_1#1$1",focus="m")]
[name="颓丧的男人"]赐福......对我这样普通的米诺斯人？
[charslot(slot="m",name="avg_npc_2068_1#3$1",focus="m")]
[name="卡珊卓拉"]我们的神明与英雄，原本亦是普通的米诺斯人。
[charslot(slot="m",name="avg_npc_2081_1#1$1",focus="m")]
[name="颓丧的男人"]感谢您，尊敬的卡珊卓拉小姐，我有些明白了......
[Dialog]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_2085_1#1$1",duration=1)]
[Delay(time=2)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[name="助理祭司"]卡珊卓拉小姐，我来替您的班。
[charslot(slot="m",name="avg_npc_2068_1#5$1",focus="m")]
[name="卡珊卓拉"]哦，原来已经这个时间了。今天来拜访神殿的客人很多。
[charslot(slot="m",name="avg_npc_2085_1#1$1",focus="m")]
[name="助理祭司"]最近您既要顾及恩底弥翁神殿的访客，又因为克瑞斯拉第一神殿主管祭司空缺，要为其代行文书工作......但您的时间和精力是有限的。
[charslot(slot="m",name="avg_npc_2068_1#3$1",focus="m")]
[name="卡珊卓拉"]不用担心我，芙里欧。解读神谕、代神之口......是我天生的职责。
[charslot(slot="m",name="avg_npc_2085_1#1$1",focus="m")]
[name="助理祭司"]正因如此，您应该比我更清楚，那位先生做的只是普通的梦，那不是神谕，根据哥伦比亚的说法——
[charslot(slot="m",name="avg_npc_2068_1#3$1",focus="m")]
[name="卡珊卓拉"]他可能患有创伤后应激障碍，我知道。
[charslot(slot="m",name="avg_npc_2085_1#1$1",focus="m")]
[name="助理祭司"]那您为什么不直接告诉他......
[charslot(slot="m",name="avg_npc_2068_1#9$1",focus="m")]
[name="卡珊卓拉"]领受神谕对每个米诺斯人来说都是值得骄傲的事，而他的眼神却充满愧疚和惊惧。
[name="卡珊卓拉"]他希望得到神的指引，却又害怕那个噩梦真是无法违抗的神谕。
[charslot(slot="m",name="avg_npc_2068_1#3$1",focus="m")]
[name="卡珊卓拉"]若他相信我解读出的只言片语，胜过相信自己，那我必须承担责任，至少让他过得轻松一些。
[charslot(slot="m",name="avg_npc_2085_1#1$1",focus="m")]
[name="助理祭司"]......
[name="助理祭司"]随后我会送他一些安神的花草茶，联系医师关注他的情况。
[name="助理祭司"]您下午不是例行休假吗？请不要再为神殿的事操心了，去处理您的私事吧。
[charslot(slot="m",name="avg_npc_2068_1#3$1",focus="m")]
[name="卡珊卓拉"]你总是在为我分忧，芙里欧，谢谢。
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=1)]
[Delay(time=2)]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image]
[Background(image="69_g4_athenusstreet",screenadapt="coverall", block=true)]
[delay(time=2)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_npc_2070_1#1$1",duration=1)]
[charslot(slot="r",name="avg_4056_titi_1#1$2",duration=1)]
[Delay(time=2)]
[charslot(slot="r",name="avg_4056_titi_1#5$2",focus="r")]
[name="缇缇"]真是抱歉，赫卡德墨先生。
[name="缇缇"]我一到旅店就晕过去了，没想到睡了整整三个小时，害您在楼下等了那么久......
[charslot(slot="l",name="avg_npc_2070_1#1$1",focus="l")]
[name="赫卡德墨"]千万不要挂心，梅捷缇克缇小姐，等候也是理事官执笔人的工作之一。
[name="赫卡德墨"]您看上去还是有些虚弱......真的要现在就去第一神殿重建现场参观吗？再休息一会儿也是可以的。
[charslot(slot="r",name="avg_4056_titi_1#2$2",focus="r")]
[name="缇缇"]那怎么行？要说现在有什么能让我迅速恢复状态，那就非克瑞斯拉第一神殿莫属了！
[name="缇缇"]据说神殿的原址，正是米诺斯的建国英雄克瑞斯拉在群山中初次得到神谕的地方。
[name="缇缇"]她在那里建造的第一座神殿，也成了米诺斯的发源。
[charslot(slot="r",name="avg_4056_titi_1#10$2",focus="r")]
[name="缇缇"]萨尔贡人......侵占米诺斯后，将三座城邦改建为移动城市，受到战火侵害的克瑞斯拉第一神殿却被留在了原址。
[charslot(slot="r",name="avg_4056_titi_1#6$2",focus="r")]
[name="缇缇"]没想到时隔百年，雅赛努斯人决定重建这座神殿，我也因此有幸见到这座历史遗迹最初的风貌，真是令人期待！
[charslot(slot="l",name="avg_npc_2070_1#7$1",focus="l")]
[name="赫卡德墨"]您对米诺斯的历史倒是很了解......也少见地诚实。
[name="赫卡德墨"]可惜，原本的第一神殿图纸已经逸失，重建无法完全还原它过去的风貌。
[charslot(slot="l",name="avg_npc_2070_1#1$1",focus="l")]
[name="赫卡德墨"]不过，他们建造神殿的做派，倒是挺有“古风”的。
[charslot(slot="r",name="avg_4056_titi_1#1$2",focus="r")]
[name="缇缇"]古风？
[charslot(slot="l",name="avg_npc_2070_1#1$1",focus="l")]
[name="赫卡德墨"]“重振米诺斯的精神，就需效仿雅赛努斯的建城英雄们，完全自发地建造神殿。”
[name="赫卡德墨"]那位倡议人在全民投票前，用这句话打动了所有人，重建神殿的议题近乎全票通过。
[name="赫卡德墨"]不需要具体的工程规划，不用确定人员安排，民众的热情和米诺斯人骨子里对英雄的崇拜，会筑成最完美的克瑞斯拉第一神殿。
[charslot(slot="r",name="avg_4056_titi_1#9$2",focus="r")]
[name="缇缇"]早就听说米诺斯人做事随心随性，但就是这份随性让他们取得了辉煌的艺术成就......果然如此！
[charslot(slot="l",name="avg_npc_2070_1#7$1",focus="l")]
[name="赫卡德墨"]多谢赞美，但愿神殿能尽早完工......
[charslot(slot="r",name="avg_4056_titi_1#9$2",focus="r")]
[name="缇缇"]仿古重建......有意思！赫卡德墨

... (全文14143字符)
```

### level_act48side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, duration=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="69_g7_firsttemple",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, duration=1, block=true)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[PlaySound(key="$d_avg_crwddiscuss_inside",channel="1",loop=true, volume=0.7)]
[Delay(time=2)]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="果农代表"]搬不搬！
[name="工匠代表"]不搬！
[name="工匠代表"]搬不搬！
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="果农代表"]不！搬！
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_npc_1482_1#1$1",duration=1)]
[charslot(slot="r",name="avg_4056_titi_1#3$2",duration=1)]
[Delay(time=2)]
[charslot(slot="r",name="avg_4056_titi_1#3$2",focus="r")]
[name="缇缇"]好、好有气势的辩论！不愧是传承英雄血脉的米诺斯人！
[charslot(slot="r",name="avg_4056_titi_1#5$2",focus="r")]
[name="缇缇"]呃......就是没什么实质内容。
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]两边都在扯着嗓子大喊，根本不知道他们在吵什么。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="清醒的工匠"]在雅赛努斯航线修改一事上，果农跟我们神殿的工人积怨已久，都在气头上。
[name="清醒的工匠"]唉，真是惭愧，怎么能让随便拉来的游客来解决我们自己人的纠纷，他们吵的连我都听不明白......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="r")]
[charslot(slot="r",name="avg_4056_titi_1#5$2",focus="r")]
[delay(time=1.5)]
[charslot(slot="r",name="avg_4056_titi_1#3$2",focus="r")]
[Effect(name="$e_emoji_proud",layer = 1,x=250,y=150)]
[delay(time=1)]
[charslot(slot="r",name="avg_4056_titi_1#8$2",focus="r")]
[name="缇缇"]如果只是要听明白，哼哼......
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]缇缇，别给自己找麻烦。
[charslot(slot="r",name="avg_4056_titi_1#8$2",focus="r")]
[name="缇缇"]“随便拉来的游客”刚好想到了一个办法。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="r",posfrom="0,0",posto="200,0",afrom=1,ato=0,duration=1.5)]
[delay(time=2.5)]
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="清醒的工匠"]哎！小姑娘别往吵架的人堆里跑啊，当心被他们伤着！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_smashtable",volume=1,channel="2")]
[delay(time=0.5)]
[PlaySound(key="$d_avg_bowl_smash",volume=1,channel="4")]
[Image(image="69_i03")]
[ImageTween(xScaleFrom=1, yScaleFrom=1, xScaleTo=0.8, yScaleTo=0.8, duration=45, block=false)]
[delay(time=1.5)]
[PlaySound(key="$d_avg_cnstrctnck",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
神殿的工匠代表和庇护果农的义务兵各执一词、面红耳赤，丝毫没注意到一对黑色的尖耳朵从石桌下探了出来。
小个子菲林女孩一跃而出，笑眯眯地拉过两人的手，把他们的手交握在一起。
事件核心的双方代表一时没反应过来，被她扯得失去重心，双双趴在石桌上，齐齐看向这个开朗的外乡人。
[name="工匠代表"]这是谁带来的小女孩，跑到神殿来过家家吗！
[name="果农代表"]哈，你的无理取闹连外邦人都看不下去了，真丢雅赛努斯人的脸。
[name="工匠代表"]别趁机火上浇油！
[name="工匠代表"]喂，这是我们米诺斯人的事，不需要一个啥都不懂的外国小姑娘教我们怎么和好。
[name="缇缇"]谁说要让你们和好了？
[name="工匠代表&果农代表"]啊？
[name="缇缇"]不直面问题，是没办法解决问题的。就算现在重修旧好，又能维持多久呢？
[name="缇缇"]再说了，入乡随俗。米诺斯盛传激昂的英雄史诗和动人的故事，它们记载了无数前人的智慧，哪需要我教各位怎么解决问题？
[name="缇缇"]相传米诺斯最善战的英雄海格斯武艺高超，令所有外敌闻风丧胆。
[name="缇缇"]但面对米诺斯同乡，哪怕对方再冒犯，他也不会直接出手，而是以扳手腕的方式点到为止。
[name="工匠代表"]效仿英雄用力气定输赢？不错，省了那些口舌之辩！
[name="缇缇"]我还没说完。
[name="缇缇"]又相传，有一位沉默的英雄，他年轻时热情而大胆，曾是被鲜花簇拥的飞扬少年。
[name="缇缇"]但命运让他知晓了一个不应让任何人知道的秘密，从此他缄口不言，沉默了三十年。
[name="工匠代表"]等等，大力神海格斯的传说耳熟能详，但“沉默的英雄”？少诓我们！
[name="缇缇"]啊，这是小时候父亲给我讲的米诺斯故事，确实不是什么有名的典故，太适合用来举例所以说顺嘴了——
[name="缇缇"]咳，总之！我建议效仿米诺斯先贤，以扳手腕定输赢。
[name="缇缇"]不过要加一个小小的条件——不管怨气有多大，只有赢得对局的人才能说话。
[name="工匠代表"]呵，从来没听过这种规矩。
[name="缇缇"]你是不善言辞，还是四肢无力？
[name="工匠代表"]废话少说，比就比。
[name="缇缇"]嘿嘿，那第一届第一神殿扳手腕大赛——
[name="缇缇"]正式开始！
[Dialog]
[stopsound(channel="1", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[Image]
[Background(image="69_g7_firsttemple",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[PlaySound(key="$d_avg_bowl_smash",volume=1,channel="1")]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$d_avg_masses_cheer",volume=1,channel="4")]
[CameraShake(duration=2, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=true)]
[charslot(slot="m",name="avg_npc_1482_1#1$1",focus="m")]
[name="米奥"]嚯，没想到那个义务兵看着瘦弱，技巧却很娴熟，趁大块头卸力的瞬间使劲，漂亮！
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_2087_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_2086_1#1$1",focus="l")]
[name="工匠代表"]你——
[charslot(slot="r",name="avg_npc_2086_1#1$1",focus="r")]
[name="果农代表"]憋着，输家不准说话！
[name="果农代表"]石料堵在渡口，新采的苹果一筐都运不出去，而且种植区完全被山峰的阴影遮挡，未熟透的苹果根本照不到太阳，这样下去就要歉收了！
[name="果农代表"]一比零，再来。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_smashtable",volume=1,channel="2")]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$d_avg_masses_cheer",volume=1,channel="4")]
[CameraShake(duration=2, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=true)]
[charslot(slot="m",name="avg_npc_1482_1#1$1",focus="m")]
[name="米奥"]哇，这身肌肉果然不是白长的，看来背大理石对人类来说是不错的运动啊。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_2087_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_2086_1#1$1",focus="l")]
[name="工匠代表"]苹果得先搬走我们才能运石料吧？而且我们重建第一神殿是受到了米诺斯众英雄的感召，要是耽误了事情，你担得起责吗！
[name="工匠代表"]一比一，再来！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4056_titi_1#1$2",focus="m")]
[name="缇缇"]苹果采收和运送石料......原来是这样。
[charslot(slot="m",name="avg_npc_1482_1#2$1",focus="m")]
[name="米奥"]好看好看，米诺斯人真是有趣。不过再比几轮下去，双方选手没了力气，观赏性可就差了......
[Dialog]
[PlaySound(key="$d_avg_masses_cheer",volume=1,channel="4")]
[CameraShake(duration=2, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=true)]
[charslot(slot="m",name="avg_npc_1482_1#1$1",focus="m")]
[name="米奥"]欸，他们怎么停下来了？
[charslot(slot="m",name="avg_4056_titi_1#1$2",focus="m")]
[name="缇缇"]他们意识到了，扳手腕原本就不是为了决出胜负，而是为了让他们有机会听对方

... (全文18127字符)
```

### level_act48side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, duration=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="69_g7_firsttemple",screenadapt="coverall")]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, duration=1, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avgnew_482_pallas_1#10$1",duration=1)]
[charslot(slot="r",name="avg_4056_titi_1#9$2",duration=1)]
[Delay(time=2)]
[charslot(slot="l",name="avgnew_482_pallas_1#10$1",focus="l")]
[name="帕拉斯"]效仿英雄海格斯扳手腕......还真让工人和果农冷静下来沟通啦？你很聪明，缇缇。
[charslot(slot="r",name="avg_4056_titi_1#9$2",focus="r")]
[name="缇缇"]但帕拉斯小姐其实昨晚就想出了解决问题的方法，只是太过劳累栽倒在苹果箱里睡着了。
[name="缇缇"]可惜了你酿的苹果酒......原来是打算用来招待工人和果农，酒酣之后再让他们合作采石的，对吗？
[charslot(slot="l",name="avgnew_482_pallas_1#10$1",focus="l")]
[name="帕拉斯"]没错。不过用它来招待客人，也不可惜啊。
[Dialog]
[PlaySound(key="$d_avg_winebottle_open")]
[Delay(time=1)]
[charslot(slot="l",name="avgnew_482_pallas_1#11$1",focus="l")]
[name="帕拉斯"]你不是还在晕船吗？来，干杯，正好用我的酒来缓解！
[Dialog]
[charslot(slot="l",posfrom="0,0",posto="50,0",duration=1.5,focus="l,r")]
[charslot(slot="r",posfrom="0,0",posto="-50,0",duration=1.5,focus="l,r")]
[delay(time=2.5)]
[PlaySound(key="$d_avg_pourwine")]
[delay(time=3)]
[charslot(slot="r",name="avg_4056_titi_1#6$2",posfrom="-50,0",posto="-50,0",focus="r")]
[name="缇缇"]干杯！
[Dialog]
[charslot(slot="r",focus="l,r")]
[PlaySound(key="$clink")]
[delay(time=1)]
[charslot(slot="l",posfrom="50,0",posto="0,0",duration=1.5)]
[charslot(slot="r",posfrom="-50,0",posto="0,0",duration=1.5)]
[delay(time=2.5)]
[PlaySound(key="$d_avg_drinkwine_generous")]
[delay(time=1)]
[PlaySound(key="$d_avg_drinkwine_generous")]
[delay(time=1)]
[charslot(slot="r",name="avg_4056_titi_1#6$2",focus="r")]
[name="缇缇"]哈......甜滋滋的，真好喝！
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]......
[name="缇缇"]帕拉斯小姐，虽然最终我们的想法不谋而合，但请你诚实地告诉我，我擅自插手第一神殿的重建工作，是不是不合适？
[charslot(slot="l",name="avgnew_482_pallas_1#12$1",focus="l")]
[name="帕拉斯"]因为你是萨尔贡的大使？
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]因为萨尔贡曾经——
[charslot(slot="l",name="avgnew_482_pallas_1#12$1",focus="l")]
[name="帕拉斯"]缇缇，你只需回答我一个问题——你认为白鬃王帕赫里图出兵征服米诺斯是否有其必要？
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]没有。
[charslot(slot="l",name="avgnew_482_pallas_1#12$1",focus="l")]
[name="帕拉斯"]即使那样做可以转嫁萨尔贡国内的矛盾？
[charslot(slot="r",name="avg_4056_titi_1#15$2",focus="r")]
[name="缇缇"]帝国内部的矛盾，该当在帝国内部解决才是。转嫁给无辜的邻国是他的无能！
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]虽然回到萨尔贡之后，我多半就不敢说得这么直接了......
[charslot(slot="l",name="avgnew_482_pallas_1#13$1",focus="l")]
[name="帕拉斯"]哈哈！爽快，来，喝酒！
[Dialog]
[charslot(slot="l",name="avgnew_482_pallas_1#13$1",focus="l,r")]
[charslot(slot="r",name="avg_4056_titi_1#9$2",focus="l,r")]
[PlaySound(key="$d_avg_drinkwine_generous")]
[delay(time=1)]
[PlaySound(key="$d_avg_drinkwine_generous")]
[delay(time=1)]
[charslot(slot="l",name="avgnew_482_pallas_1#14$1",focus="l")]
[name="帕拉斯"]我原以为像你这样随性又异想天开的人，对待历史问题不会如此尖锐。
[charslot(slot="l",name="avgnew_482_pallas_1#14$1",focus="l")]
[name="帕拉斯"]只要你刚刚的回答是出自真心，而不是出于人身安全考虑准备的说辞，那我们就能成为朋友。
[charslot(slot="r",name="avg_4056_titi_1#1$2",focus="r")]
[name="缇缇"]帕拉斯小姐——
[charslot(slot="l",name="avgnew_482_pallas_1#14$1",focus="l")]
[name="帕拉斯"]对朋友还用敬称？
[charslot(slot="r",name="avg_4056_titi_1#1$2",focus="r")]
[name="缇缇"]帕拉斯，我认为入乡随俗也不能忘了自己的身份。
[charslot(slot="r",name="avg_4056_titi_1#10$2",focus="r")]
[name="缇缇"]虽然佩佩——我在萨尔贡的朋友，总说我的想法跳跃，行事风格也不合常理，但这是两码事！
[charslot(slot="l",name="avgnew_482_pallas_1#14$1",focus="l")]
[name="帕拉斯"]看来萨尔贡的帕夏选中你担任使节团的负责人，还是挺有眼光的......
[name="帕拉斯"]放心吧，工人和果农都很喜欢你。我们有辨别宵小之徒的经验，不至于迁怒每个萨尔贡人。
[charslot(slot="l",name="avgnew_482_pallas_1#15$1",focus="l")]
[name="帕拉斯"]而且在现在这个节骨眼，只要能解决问题，单纯参与第一神殿的重建工作算不上越界。
[charslot(slot="r",name="avg_4056_titi_1#5$2",focus="r")]
[name="缇缇"]唔......这话怎么说？
[charslot(slot="l",name="avgnew_482_pallas_1#14$1",focus="l")]
[name="帕拉斯"]你看啊，这神殿内的立柱、浮雕、纹饰还有大半没有完工；神殿外的露天剧场从第三排开始就看不见舞台了，坡度根本没有调整......
[name="帕拉斯"]还有矗立在剧场中央的克瑞斯拉雕像，因为雕塑家的完美主义，到现在仍处于打磨阶段，没能交付。
[charslot(slot="r",name="avg_4056_titi_1#5$2",focus="r")]
[name="缇缇"]这进度有些......
[charslot(slot="l",name="avgnew_482_pallas_1#12$1",focus="l")]
[name="帕拉斯"]“愁死人”。不用斟酌词句，又不是写诗——所有人都知道建造进度已经远远落后于预期。
[charslot(slot="l",name="avgnew_482_pallas_1#14$1",focus="l")]
[name="帕拉斯"]来，先喝酒。
[Dialog]
[charslot(slot="l",name="avgnew_482_pallas_1#14$1",focus="l,r")]
[charslot(slot="r",name="avg_4056_titi_1#9$2",focus="l,r")]
[PlaySound(key="$d_avg_drinkwine_generous")]
[delay(time=1)]
[PlaySound(key="$d_avg_drinkwine_generous")]
[delay(time=1)]
[charslot(slot="l",name="avgnew_482_pallas_1#12$1",focus="l")]
[name="帕拉斯"]虽说重建神殿没有工期限制，就算为了追求完美而导致效率不高，终究也是能完工的，但现在看来，再拖下去各方人员都会受到影响。
[charslot(slot="r",name="avg_4056_titi_1#1$2",focus="r")]
[name="缇缇"]果农们的采收......
[charslot(slot="l",name="avgnew_482_pallas_1#14$1",focus="l")]
[name="帕拉斯"]没错。再有下次，可就不是几局扳手腕和一瓶好酒能解决的咯......喝得这么快？再给你倒一杯？
[charslot(slot="r",name="avg_4056_titi_1#1$2",focus="r")]
[name="缇缇"]谢谢！可是帕拉斯，我有个问题。
[charslot(slot="l",name="avgnew_482_pallas_1#14$1",focus="l")]
[name="帕拉斯"]嗯？
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]明明你帮着工匠解决了不少问题，他们也很依赖你，但身为项目负责人，你怎么看起来一点都不着急？
[charslot(slot="l",name="avgnew_482_pallas_1#14$1",focus="l")]
[name="帕拉斯"]嗯？我从来都不是神殿重建的项目负责人啊。
[charslot(slot="r",name="avg_4056_titi_1#3$2",focus="r")]
[name="缇缇"]什、什么？
[charslot(slot="l",name="avgnew_482_pallas_1#14$1",focus="l")]
[name="帕拉斯"]“效仿古法”意味着整个项目只需要一位祭司——也就是卡珊卓拉小姐牵头，正式执行阶段根本不会设置负责人。
[name="帕拉斯"]我不过是一名好事又好酒的闲散人士，哪能担得起那种名头，不过......
[charslot(slot="l",name="avgnew_482_pallas_1#15$1",focus="l")]
[name="帕拉斯"]我看你倒是通情达理，脑子转得也快。
[Dialog]
[charslot(slot="r",name="avg_4056_titi_1#6$2",focus="r")]
[PlaySound(key="$d_avg_drinkwine_generous")]
[delay(time=1)]
[PlaySound(key="$d_avg_drinkwine_generous")]
[delay(time=1)]
[Effect(name="$e_emoji_shy",layer = 1,x=250,y=150)]
[charslot(slot="r",name="avg_4056_titi_1#6$2",focus="r")]
[multiline(name="缇缇")]（畅快地饮酒）哈......
[delay(

... (全文15204字符)
```

### level_act48side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, duration=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="69_g12_generalroom",screenadapt="coverall")]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, duration=1, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_1022_flwr2_1#1$2",duration=1)]
[charslot(slot="r",name="avg_npc_2069_1#1$1",duration=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_1022_flwr2_1#6$2",focus="l")]
[name="莱娜"]啊——
[charslot(slot="r",name="avg_npc_2069_1#10$1",focus="r")]
[name="吕刻伊昂"]......啊......
[charslot(slot="l",name="avg_1022_flwr2_1#1$2",focus="l")]
[name="莱娜"]不错，呼吸道和发声系统一切正常，肺部的结晶没有造成逆行感染。
[name="莱娜"]也就是说，几天前你到罗德岛办事处，紧盯着我们的医疗干员一言不发，不是因为病情加重说不出话。
[charslot(slot="l",name="avg_1022_flwr2_1#2$2",focus="l")]
[name="莱娜"]看来我本不必特地跑这一趟。
[charslot(slot="r",name="avg_npc_2069_1#1$1",focus="r")]
[name="吕刻伊昂"]莱娜小姐，您对雅赛努斯的感染者很上心，罗德岛带来的药物也远比我们之前服用的有效，我们都很感激，我就不耽误您的时间了......
[charslot(slot="l",name="avg_1022_flwr2_1#1$2",focus="l")]
[name="莱娜"]只是做个检查还不够。
[name="莱娜"]米诺斯对感染者的政策可谓宽松，除了不能从事神职等特殊职业，感染者的日常生活并不会受到太大影响。
[name="莱娜"]但“矿石病会隔绝米诺斯人的英雄气概”是很多人信奉的真理。不少患者对自己的病情态度消极，甚至有人刻意隐瞒。
[name="莱娜"]告诉我，吕刻伊昂先生，这是几？
[charslot(slot="r",name="avg_npc_2069_1#1$1",focus="r")]
[name="吕刻伊昂"]四。
[name="吕刻伊昂"]莱娜小姐，承蒙关心，您还是请回吧。我只是轻度感染，病痛还未波及我的视力。
[charslot(slot="l",name="avg_1022_flwr2_1#4$2",focus="l")]
[name="莱娜"]那这半个月来，你为何足足光顾了罗德岛办事处四次？
[charslot(slot="r",name="avg_npc_2069_1#3$1",focus="r")]
[name="吕刻伊昂"]我......
[charslot(slot="l",name="avg_1022_flwr2_1#4$2",focus="l")]
[name="莱娜"]你太不擅长说谎，而且，我在你的老师赞索斯先生身上看到了罗德岛出品的监测手环。
[name="莱娜"]你一直在替他求医？
[charslot(slot="r",name="avg_npc_2069_1#4$1",focus="r")]
[name="吕刻伊昂"]是......
[name="吕刻伊昂"]老师每日操心的事太多，总是忘了复诊。我帮他取药也很合理。
[charslot(slot="l",name="avg_1022_flwr2_1#14$2",focus="l")]
[name="莱娜"]但你没有在办事处登记他的名字，这意味着他不会留下矿石病的医疗记录。
[charslot(slot="r",name="avg_npc_2069_1#4$1",focus="r")]
[name="吕刻伊昂"]他救了我的命，教我水文知识和战斗的技艺，待我不薄。他是值得尊敬的前辈，所以我觉得不该让更多人知道......
[charslot(slot="l",name="avg_1022_flwr2_1#14$2",focus="l")]
[name="莱娜"]知道他与“英雄”无缘？
[charslot(slot="r",name="avg_npc_2069_1#4$1",focus="r")]
[name="吕刻伊昂"]......
[charslot(slot="l",name="avg_1022_flwr2_1#13$2",focus="l")]
[name="莱娜"]吕刻伊昂先生，出入感染者治疗中心或许会影响别人对赞索斯先生和你的判断，但不会改变你们选择的路。
[charslot(slot="l",name="avg_1022_flwr2_1#1$2",focus="l")]
[name="莱娜"]我不是卡珊卓拉小姐，并不擅长安抚人心，但我知道你们两个急需妥善治疗。
[charslot(slot="l",name="avg_1022_flwr2_1#2$2",focus="l")]
[name="莱娜"]我会调整你们在感染者治疗名单上的优先级，密切关注你们的病情。做好被我叨扰的准备吧，倔强的年轻人。
[charslot(slot="r",name="avg_npc_2069_1#5$1",focus="r")]
[name="吕刻伊昂"]您......并没有看起来那么好说话。
[charslot(slot="l",name="avg_1022_flwr2_1#2$2",focus="l")]
[name="莱娜"]如果你跟你弓箭上站着的小羽兽一样，用几粒甜玉米就能收买，我就不必费那么多口舌了。
[charslot(slot="r",name="avg_npc_2069_1#4$1",focus="r")]
[name="吕刻伊昂"]抱歉......
[charslot(slot="l",name="avg_1022_flwr2_1#1$2",focus="l")]
[name="莱娜"]对了，赞索斯先生呢？
[name="莱娜"]如果你之前带来的报告都是他的，那这段时间他体内的结晶密度波动剧烈，需要充足的休息。我叮嘱过你。
[charslot(slot="r",name="avg_npc_2069_1#1$1",focus="r")]
[name="吕刻伊昂"]我向老师转述了，但......
[charslot(slot="l",name="avg_1022_flwr2_1#13$2",focus="l")]
[name="莱娜"]他不会又去渡口了吧？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="69_g1_rivercrossing",screenadapt="coverall", block=true)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_4166_varkis_1#1$1",focus="m")]
[name="赞索斯"]果农和工匠的船只还没安排好，我现在很忙。长话短说吧，赫卡德墨。
[charslot(slot="m",name="avg_npc_2070_1#6$1",focus="m")]
[name="赫卡德墨"]......吕刻伊昂怎么没来帮您？平时他可不会离开您半步。
[charslot(slot="m",name="avg_4166_varkis_1#1$1",focus="m")]
[name="赞索斯"]家里来了个罗德岛的医生，正在给他看病，告假了。
[charslot(slot="m",name="avg_npc_2070_1#3$1",focus="m")]
[name="赫卡德墨"]上门看病？
[name="赫卡德墨"]（难道他上次拿的药依旧没有效果，现在已经病到......走不动路了？）
[charslot(slot="m",name="avg_4166_varkis_1#14$1",focus="m")]
[name="赞索斯"]如果你是来传达里底娅理事官的“建议”，那还是请回吧。我会解决渡口的问题，不用她操心。
[charslot(slot="m",name="avg_npc_2070_1#1$1",focus="m")]
[name="赫卡德墨"]这次理事官派我来就是想通知您，渡口的问题已经彻底解决了。
[charslot(slot="m",name="avg_4166_varkis_1#1$1",focus="m")]
[name="赞索斯"]解决了？帕拉斯这次动作倒是挺快。
[charslot(slot="m",name="avg_npc_2070_1#1$1",focus="m")]
[name="赫卡德墨"]不，给出解决方案的人并不是她。
[charslot(slot="m",name="avg_4166_varkis_1#1$1",focus="m")]
[name="赞索斯"]那是谁？是卡珊卓拉小姐出面稳定了人心，还是理事官动用了她的小手段？
[charslot(slot="m",name="avg_npc_2070_1#1$1",focus="m")]
[name="赫卡德墨"]都不是。
[name="赫卡德墨"]解决工匠和果农纷争的是萨尔贡使节团的大使，一位深色皮肤、黑色耳朵的小个子菲林。
[charslot(slot="m",name="avg_4166_varkis_1#10$1",focus="m")]
[name="赞索斯"]黑色耳朵的菲林......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Image]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Image(image="69_i02")]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Image]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Background(image="69_g1_rivercrossing",screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_4166_varkis_1#10$1",focus="m")]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="m",name="avg_4166_varkis_1#10$1",focus="m")]
[name="赞索斯"]那天早上在次级渡口遇到的“哥伦比亚人”......
[name="赞索斯"]就是萨尔贡的使节？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="69_g8_templetheater",screenadapt="showall",x=0, y=-50, xScale=1.2, yScale=1.2 ,block=true)]
[backgroundTween(xFrom=0, yFrom=-50, xTo=0, yTo=0, xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1.4, yScaleTo=1.4, duration=105, block=false)]
[delay(time=2)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="缇缇"]古老的米诺斯人从洁白的大理石中发现了美，用楔子、石凿、锉刀......塑造传说和史诗。
[name="缇缇"]《克瑞斯拉纪》中写道，建国英雄克瑞斯拉磨损了整整三十双鞋，

... (全文10653字符)
```

### level_act48side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, duration=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="69_g11_firsttemple_indoor",screenadapt="coverall")]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, duration=1, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avgnew_482_pallas_1#1$1",duration=1)]
[Delay(time=2)]
[name="帕拉斯"]自从一周前我被你手下的小祭司瞪了一眼之后，你可就再没来过我这儿了呀，卡珊卓拉？
[charslot(slot="m",name="avg_npc_2068_1#3$1",focus="m")]
[name="卡珊卓拉"]管理恩底弥翁神殿的同时接手第一神殿的重建工作并非易事。
[name="卡珊卓拉"]芙里欧只是担心我过于操劳，她知道我们还在祭司学院的时候就成了朋友。
[charslot(slot="m",name="avgnew_482_pallas_1#20$1",focus="m")]
[name="帕拉斯"]所以更不能接受我一回来就给你添麻烦？
[charslot(slot="m",name="avg_npc_2068_1#4$1",focus="m")]
[name="卡珊卓拉"]帕拉斯......
[name="卡珊卓拉"]半年前，当你放弃了走祭司的通道，像一个等待解梦的普通米诺斯人一样出现在恩底弥翁神殿时，我就知道我们都遇到了麻烦。
[name="卡珊卓拉"]一般的神谕，无论是深夜造访的梦境，还是不期而至的幻觉，大部分英雄的指示都可被归纳为常见的意象。
[charslot(slot="m",name="avgnew_482_pallas_1#1$1",focus="m")]
[name="帕拉斯"]我知道，我们上学的时候还专门背过，这样一来，不具备“天赋”的普通祭司也可以为领受神谕的民众指引方向。
[charslot(slot="m",name="avg_npc_2068_1#6$1",focus="m")]
[name="卡珊卓拉"]但你带来的那则神谕，它所呈现的每个细节都不曾记载于任何经典古籍......我确信它是一则强力的启示，正因如此，它令我非常不安。
[charslot(slot="m",name="avgnew_482_pallas_1#1$1",focus="m")]
[name="帕拉斯"]放心，我们会找到解决方法的。
[charslot(slot="m",name="avg_npc_2068_1#4$1",focus="m")]
[name="卡珊卓拉"]唉，你不该辞去祭司一职，那样或许能得到更多帮助......
[charslot(slot="m",name="avgnew_482_pallas_1#1$1",focus="m")]
[name="帕拉斯"]然后隐瞒自己的病症，继续做米诺斯边境传说中的“胜利女神”吗？
[name="帕拉斯"]哪怕这个名字已经被其他同胞继承，我也应当避免节外生枝。况且众英雄千里迢迢指引我回来，我必须对自己诚实。
[charslot(slot="m",name="avg_npc_2068_1#3$1",focus="m")]
[name="卡珊卓拉"]......看来你在罗德岛休养的那段时间，过得很好。
[charslot(slot="m",name="avgnew_482_pallas_1#16$1",focus="m")]
[name="帕拉斯"]当然。哦，我是不是没向你提起过，我在那艘舰船上还组织了一个“米诺斯联盟”？
[charslot(slot="m",name="avg_npc_2068_1#6$1",focus="m")]
[name="卡珊卓拉"]有这么多离开家乡求医的米诺斯人？
[charslot(slot="m",name="avgnew_482_pallas_1#10$1",focus="m")]
[name="帕拉斯"]确实不少。但在我们的联盟里，真正的米诺斯人只有埃拉托小姐和火神小姐，其他成员只是在精神上向往我们的国度。
[name="帕拉斯"]等有机会了我一定向你详细介绍。他们都是满怀英雄气概，对诗歌艺术和酿造技术充满热情的人！
[charslot(slot="m",name="avg_npc_2068_1#3$1",focus="m")]
[name="卡珊卓拉"]所以你们是个喝酒的联盟。
[charslot(slot="m",name="avgnew_482_pallas_1#11$1",focus="m")]
[name="帕拉斯"]哈哈没错，不过少了你还是差点意思。虽然你本人不胜酒力，但酿酒的技术是同期祭司中最高明的。
[name="帕拉斯"]学院交流大会的时候，你用衣带扎起典雅的衣袖，像老练的工匠一般捶打葡萄的样子，真是太迷人了！
[charslot(slot="m",name="avg_npc_2068_1#3$1",focus="m")]
[name="卡珊卓拉"]......
[name="卡珊卓拉"]我看你就是馋了，我给你的方子呢？
[charslot(slot="m",name="avgnew_482_pallas_1#10$1",focus="m")]
[name="帕拉斯"]去阿克罗蒂村的时候就丢啦。后来与我同行的萨卡兹护卫教了我卡兹戴尔的酿酒秘法，这才解了我的口舌之苦。
[charslot(slot="m",name="avg_npc_2068_1#3$1",focus="m")]
[name="卡珊卓拉"]我从不担心你找不到同伴。先是萨卡兹护卫，现在又跟萨尔贡使节团的大使交上了朋友。
[charslot(slot="m",name="avgnew_482_pallas_1#1$1",focus="m")]
[name="帕拉斯"]......
[name="帕拉斯"]你听说了果农和工匠的事，缇缇很可靠。
[charslot(slot="m",name="avg_npc_2068_1#6$1",focus="m")]
[name="卡珊卓拉"]梅捷缇克缇小姐或许很聪明，对米诺斯也没有敌意，但她的身份依旧敏感。
[name="卡珊卓拉"]要是我刚刚不打断你，不光是文物交换仪式的选址，你是不是会把我们原本商量好的戏剧仪式也交给她负责？
[name="卡珊卓拉"]你究竟是太过信任她，还是......
[charslot(slot="m",name="avgnew_482_pallas_1#4$1",focus="m")]
[name="帕拉斯"]唉，你的眉头又皱起来了，卡珊卓拉。是我离开祭司工作太久了，一时不太适应，偶尔犯懒罢了，不用担心。
[charslot(slot="m",name="avg_npc_2068_1#4$1",focus="m")]
[name="卡珊卓拉"]帕拉斯，我知道你从来不是逃避责任的人，不然米诺斯边境也不会流传关于你的传说。
[name="卡珊卓拉"]我并不介意替你主导神殿重建的工作，我只是感到可惜，明明你更擅长与人打交道，也深得工匠信赖。
[name="卡珊卓拉"]我以为，你向民众发出提议，是希望米诺斯人回归英雄传统，重新凝聚精神。
[charslot(slot="m",name="avgnew_482_pallas_1#11$1",focus="m")]
[name="帕拉斯"]你说得没错。
[name="帕拉斯"]但既然如此，由谁主导就更不重要了，不是吗？
[charslot(slot="m",name="avgnew_482_pallas_1#7$1",focus="m")]
[name="帕拉斯"]我们的同胞崇拜英雄，却也渐渐忘了米诺斯能有今日重现的繁荣，靠的不仅仅是某几位英雄。
[charslot(slot="m",name="avg_npc_2068_1#4$1",focus="m")]
[name="卡珊卓拉"]“英雄本就从民众中来，不问出身，也不问来由......”
[charslot(slot="m",name="avgnew_482_pallas_1#10$1",focus="m")]
[name="帕拉斯"]你我真是心意相通啊。
[charslot(slot="m",name="avg_npc_2068_1#4$1",focus="m")]
[name="卡珊卓拉"]我理解你的意思......但现在神殿重建工作正在收尾阶段，从现实角度来说，也比以往更需要一个统筹的负责人。
[charslot(slot="m",name="avgnew_482_pallas_1#10$1",focus="m")]
[name="帕拉斯"]不用担心，这个负责人，可能很快就会有了。
[charslot(slot="m",name="avg_npc_2068_1#5$1",focus="m")]
[name="卡珊卓拉"]什么？
[charslot(slot="m",name="avgnew_482_pallas_1#16$1",focus="m")]
[name="帕拉斯"]忘了跟你说，我似乎看到里底娅小姐往神殿广场的方向去了。
[charslot(slot="m",name="avgnew_482_pallas_1#1$1",focus="m")]
[name="帕拉斯"]这位从重建神殿之初就隐隐与你我不对付，甚至不想让祭司负责戏剧仪式的理事官，会是去干什么的呢？
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="69_g8_templetheater",screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_4056_titi_1#1$2",focus="l")]
[delay(time=2)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="r",name="avg_npc_2067_1#1$1",posfrom="200,0",posto="0,0",afrom=0,ato=1,duration=1.5)]
[delay(time=2.5)]
[charslot(slot="r",name="avg_npc_2067_1#1$1",focus="r")]
[name="里底娅"]梅捷缇克缇大使，终于见到您了。
[charslot(slot="l",name="avg_4056_titi_1#1$2",focus="l")]
[name="缇缇"]您是？
[charslot(slot="r",name="avg_npc_2067_1#1$1",focus="r")]
[name="里底娅"]我是雅赛努斯理事官里底娅，这次两国文物交换一事的负责人。
[charslot(slot="l",name="avg_4056_titi_1#11$2",focus="l")]
[name="缇缇"]里底娅小姐，真是抱歉，到访雅赛努斯的第一天我本该跟您照会，没想到......
[charslot(slot="r",name="avg_npc_2067_1#3$1",focus="r")]
[name="里底娅"]哈哈，梅捷缇克缇小姐脱离使节团从古道进入雅赛努斯，想必是为了感受克瑞斯拉初到雅赛努斯的见闻吧。
[name="里底娅"]为什么要因为太过热爱米诺斯的文化与史诗，而向一位米诺斯人道歉呢？
[name="里底娅"]再说了，我还要向您致谢。要不是您想出了办法来解决果农和工匠之间的矛盾，第一神殿的重建进度不会这么乐观。
[charslot(slot="l",name="avg_4056_titi_1#9$2",focus="l")]
[name="缇缇"]我只是想做一些力所能及的小事。
[name="缇缇"]理事官小姐，使节团的贝赫努先生已经跟您打过照面，我想交换仪式的流程和场地还未完全敲定？
[charslot(slot="r",name="avg_npc_2067_1#1$1",focus="r")]
[name="里底娅"]是的。
[charslot(slot="l",name="avg_4056_titi_1#9$2",focus="l")]
[name="缇缇"]既然如此，比起在狭小隐秘的豪华场所，文物交换仪式是否能在克瑞斯拉雕像低垂的眼眸之下，由雅赛努斯民众共同见证？
[charslot(slot="r",name="avg_npc_2067_1#1$1",focus="r")]
[name="里底娅"]您是说，在第一神殿的广场举办交换仪式？
[charslot(slot="l",name="avg_4056_titi_1#10$2",focus="l")]
[name="缇缇"]没错。您也知道，为了交换三城建设时期萨尔贡人遗留在这里的技术资料，我带来的是法尔贾万达巴德博物馆最珍贵的馆藏。
[name="缇缇"]无数流传下来的米诺斯英雄故事中都有它的

... (全文10312字符)
```

### level_act48side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, duration=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="69_g9_templetheater_n",screenadapt="coverall")]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, duration=1, block=true)]
[Delay(time=2)]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.4, channel="bgs",fadetime=2)]
[charslot(slot="m",name="avg_npc_2072_1#1$2",duration=1)]
[Delay(time=2)]
[name="醉酒的工匠"]仁爱又英勇的建国英雄克瑞斯拉，哪怕是夜晚也无法抹去您身上的辉光。
[name="醉酒的工匠"]是您庇护第一神殿的工匠，带来两位智者，替我们排忧解难，替您修建殿堂。
[name="醉酒的工匠"]虫鸣代替您手中的竖琴作响，头冠由后人编织出胜利的形状，而月光——
[name="醉酒的工匠"]哦，对不起，您身上闪烁的不是月光，是我们上周安的探照灯。
[Dialog]
[PlaySound(key="$d_avg_drinkwine_generous")]
[Delay(time=1)]
[PlaySound(key="$d_avg_drinkwine_generous")]
[Delay(time=1)]
[PlaySound(key="$d_avg_drinkwine_generous")]
[Delay(time=1)]
[name="醉酒的工匠"]（畅快的饮酒声）
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="清醒的工匠"]......
[name="清醒的工匠"]让你别喝这么多，你还记得我们今晚是来参加投票的吗？一会儿刻陶片的时候，可别伤了自己的手。
[charslot(slot="m",name="avg_npc_2072_1#1$2",focus="m")]
[name="醉酒的工匠"]当然记得，我是来为缇缇小姐投票的！
[name="醉酒的工匠"]昨天我一个人在神殿内厅摆弄雕像的时候差点摔倒，要不是缇缇小姐用她的源石技艺帮了我，我现在哪还能喝到酒呀。
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="清醒的工匠"]呃......
[charslot(slot="m",name="avg_npc_2072_1#1$2",focus="m")]
[multiline(name="醉酒的工匠")]你是不是不信？
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",posfrom="0,0",posto="-200,0",afrom=1,ato=0,duration=1)]
[multiline(name="醉酒的工匠")]我给你演示一下，当时我被雕像拖到地面的衣带绊倒，然后——
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="醉酒的工匠")]哎哟！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovementsp",volume=1)]
[CameraShake(duration=1, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="？？？"]小心！
几条柔软洁白的布带从暗处伸出，像有意识般地向醉酒女孩飞去，帮她稳住重心。
确认对方无碍后，它们松了劲头，抚过女孩被意外弄乱的头发，责怪地拍打着丰蹄女孩的双角。
[Dialog]
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="m",name="avg_npc_2072_1#1$2",posfrom="-200,-30",posto="0,0",afrom=0,ato=1,duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_2072_1#1$2",focus="m")]
[name="醉酒的工匠"]看到没？然后我就被另一些衣带救了，是不是很神奇！
[name="醉酒的工匠"]欸？缇缇小姐你怎么来了，一起喝酒呀。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4056_titi_1#9$1",duration=1)]
[Delay(time=2)]
[name="缇缇"]帕拉斯曾告诉我，搬运队里有个女孩爱喝酒，个子小但是力气大，就是很容易摔跤。
[name="缇缇"]只是没想到短短三天，我就看你摔了不下十次，坎提亚。
[charslot(slot="m",name="avg_npc_2072_1#1$2",focus="m")]
[name="醉酒的工匠"]谢谢你，缇缇小姐。
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="清醒的工匠"]她的酒量就是米诺斯人的平均水平，不能多喝。原本米诺斯人喝酒就是小酌怡情，哪知道她长了颗老酒鬼的心。
[charslot(slot="m",name="avg_4056_titi_1#9$1",focus="m")]
[name="缇缇"]哈哈......
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="清醒的工匠"]倒是你，缇缇小姐，需不需要来一杯？
[charslot(slot="m",name="avg_4056_titi_1#5$1",focus="m")]
[name="缇缇"]我看上去......是不是很紧张？
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="清醒的工匠"]脸上看不出，但这几天相处下来，工程队的大家都知道，这位菲林小姐的尾巴藏不住心事。
[charslot(slot="m",name="avg_4056_titi_1#12$1",focus="m")]
[name="缇缇"]唔......
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="清醒的工匠"]缇缇小姐，脚手架下那个灰尾巴上戴叶子饰环的是谁？
[charslot(slot="m",name="avg_4056_titi_1#1$1",focus="m")]
[name="缇缇"]萨瑞芬，粉刷组的，只有跟身材健壮的粉刷工分在一起才会有干劲，他说自己只是爱偷懒，所有人都不信。
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="清醒的工匠"]那蹲在角落里不跟任何人打招呼的埃拉菲亚呢？
[charslot(slot="m",name="avg_4056_titi_1#10$1",focus="m")]
[name="缇缇"]莱夫特瑞斯，雕刻组的，只有在太阳照不到的地方才能找到她。我跟她也就聊过几句，但我知道她对自己的作品一心一意。
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="清醒的工匠"]大部分工匠到现在为止甚至都不知道莱夫的存在，而你对她的了解已经不少了。
[name="清醒的工匠"]缇缇小姐，我不知道别人会如何评价你和你的身份，但对我而言，你就是我们中的一员。
[charslot(slot="m",name="avg_4056_titi_1#1$1",focus="m")]
[name="缇缇"]......！
[charslot(slot="m",name="avg_4056_titi_1#9$1",focus="m")]
[name="缇缇"]谢谢你，马诺斯。
[Dialog]
[stopsound(channel="bgs",fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[Background(image="69_g11_firsttemple_indoor",screenadapt="coverall", block=true)]
[charslot(slot="l",name="avgnew_482_pallas_1#7$1")]
[charslot(slot="r",name="avg_npc_2068_1#3$1")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot(slot="r",name="avg_npc_2068_1#3$1",focus="r")]
[name="卡珊卓拉"]不去安慰你的朋友吗？她看上去有些紧张。
[charslot(slot="l",name="avgnew_482_pallas_1#1$1",focus="l")]
[name="帕拉斯"]体恤人心是你的专长，恩底弥翁神殿的卡珊卓拉小姐。
[name="帕拉斯"]缇缇现在需要的不是一个朋友的安慰，而是亲身参与神殿建设的米诺斯人的支持。
[charslot(slot="r",name="avg_npc_2068_1#3$1",focus="r")]
[name="卡珊卓拉"]在那两位好心的工匠跟她搭话之前，梅捷缇克缇小姐一直在默诵一会儿的演讲词。
[name="卡珊卓拉"]一旦舌头打结了，她就会不由自主地抓住自己的尾巴，有两次还误揪了身边那只小宠物的皮毛，惹得它很不高兴。
[charslot(slot="l",name="avgnew_482_pallas_1#10$1",focus="l")]
[name="帕拉斯"]观察得这么仔细？看来你也挺喜欢缇缇的嘛。
[charslot(slot="r",name="avg_npc_2068_1#1$1",focus="r")]
[name="卡珊卓拉"]......
[name="卡珊卓拉"]仅凭这些，还不足以证明她是值得信任的人。我只是不想因为偏见，放弃用自己的眼睛进行确认的权利。
[charslot(slot="r",name="avg_npc_2068_1#3$1",focus="r")]
[name="卡珊卓拉"]你早就认定她是神殿建设负责人的最佳人选，我会尊重你的眼光。
[name="卡珊卓拉"]今天晚上，克瑞斯拉的双眸中没有迷困之徒的阴影，大家心中都有了自己的决定，无需英雄的代言人开解。
[name="卡珊卓拉"]既然如此，我还有一些个人问题需要处理，就先告辞了。
[charslot(slot="l",name="avgnew_482_pallas_1#1$1",focus="l")]
[name="帕拉斯"]你要走？
[name="帕拉斯"]明面上主导神殿重建的祭司不参与投票，恐怕会被理事官小姐歪曲成某种示威。
[charslot(slot="r",name="avg_npc_2068_1#7$1",focus="r")]
[name="卡珊卓拉"]放心，我的陶片已经在投票箱里了。况且，里底娅小姐要是想找神殿祭司们的过错，根本不需要这么明显的借口。
[charslot(slot="l",name="avgnew_482_pallas_1#1$1",focus="l")]
[name="帕拉斯"]交换仪式若是在第一神殿举办，那奉请众英雄的戏剧仪式......
[charslot(slot="r",name="avg_npc_2068_1#3$1",focus="r")]
[name="卡珊卓拉"]我会找里底娅小姐再商量一次，至少让她把选择剧目的权力还给雅赛努斯祭司。
[name="卡珊卓拉"]不过那都是后话了，先祝今晚的投票一切顺利。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="69_g9_templetheater_n",screenadapt="coverall", block=true)]
[delay(time=2)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker

... (全文15490字符)
```

### level_act48side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, duration=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="69_g14_luxuriousroom",screenadapt="coverall")]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, duration=1, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avgnew_482_pallas_1#18$1",duration=1)]
[charslot(slot="r",name="avg_4056_titi_1#9$2",duration=1)]
[Delay(time=2)]
[charslot(slot="l",name="avgnew_482_pallas_1#18$1",focus="l")]
[name="帕拉斯"]“于是阿加门最温柔的英雄，史诗的吟唱者克瑞斯拉，将她的竖琴挂在月桂的树梢上；”
[name="帕拉斯"]“那把琴——它的琴身来自荷谟伊高山中耸立的杉树，它的琴弦取自阿涅斯平原上勇猛驮兽的肚肠；”
[name="帕拉斯"]“当它鸣响，万物便在英雄的国度歌唱，自由地，飘向远方。”
[charslot(slot="l",name="avgnew_482_pallas_1#10$1",focus="l")]
[name="帕拉斯"]缇缇，难怪当时你看到克瑞斯拉雕像落成，就想到了要把文物交换仪式的地点放在神殿广场上。
[name="帕拉斯"]原来你带来交换的，就是克瑞斯拉当初使用过的竖琴，还是曾摆放在旧雅赛努斯城第一神殿中的那一把？
[charslot(slot="r",name="avg_4056_titi_1#9$2",focus="r")]
[name="缇缇"]是的！
[name="缇缇"]传说克瑞斯拉在荷谟伊山下听到群山讲述的故事，深受鼓舞。而后她便用山岩与杉树作为材料，制作了一把巨大的竖琴。
[charslot(slot="l",name="avgnew_482_pallas_1#10$1",focus="l")]
[name="帕拉斯"]那是一把获得了祝福的琴，传闻只有在重要的日子，或是由如克瑞斯拉般的英雄拨动琴弦，它才会将清越的琴声送进人们的心里。
[name="帕拉斯"]不过，萨尔贡人攻入旧雅赛努斯城后，城中一片混乱，第一神殿也随之被毁。
[name="帕拉斯"]竖琴似乎也为这悲痛的一幕而哑然，自此之后不再发声，后来更是不知所终。
[charslot(slot="r",name="avg_4056_titi_1#9$2",focus="r")]
[name="缇缇"]但幸运的是，赫里帕夏在他的收藏中找到了它。
[name="缇缇"]虽然不知道琴是怎么去的萨尔贡——我想可能是当时某个萨尔贡士兵将它从旧雅赛努斯盗走，转手卖给了帕夏的祖上。
[charslot(slot="l",name="avgnew_482_pallas_1#20$1",focus="l")]
[name="帕拉斯"]唔，按年份推算，现在雅赛努斯城内，已无人亲眼见过当年还在原址的那把竖琴。
[name="帕拉斯"]或许只有少数熟谙典籍的祭司，或是卡珊卓拉那种能与众英雄对话的天赋者，才对这把琴有所了解。
[name="帕拉斯"]这竖琴仍能发声？
[charslot(slot="r",name="avg_4056_titi_1#9$2",focus="r")]
[name="缇缇"]可以。
[name="缇缇"]对藏品进行检测时，我们确认过琴弦，虽有一定程度的老化，但仍能奏响。
[charslot(slot="l",name="avgnew_482_pallas_1#16$1",focus="l")]
[name="帕拉斯"]原来如此，看来传说中琴因战乱而沉默，或许只是一个米诺斯故事里惯用的比喻......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="69_g5_athenusalley",screenadapt="coverall", block=true)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="旅店老板"]怎么渡口的人还没来？
[name="旅店老板"]我们旅店付了这么高的租金开在河道边上，不就是为了以最快的速度拿到最新鲜的鳞获嘛。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_2069_1#1$1",duration=1.5)]
[delay(time=2)]
[name="吕刻伊昂"]老板，食材到了。
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="旅店老板"]哎哟，你们可算来了！今天的食材再不送到，可就来不及招待使节团的贵客了......
[charslot(slot="m",name="avg_npc_2069_1#1$1",focus="m")]
[name="吕刻伊昂"]我帮您卸货？
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="旅店老板"]等等，这船今天怎么停得这么远？一会儿卸货，人非得跌到水里不可。
[name="旅店老板"]小哥，麻烦你再把货船往前开开，离后厨越近越好。
[charslot(slot="m",name="avg_npc_2069_1#3$1",focus="m")]
[name="吕刻伊昂"]......
[name="吕刻伊昂"]好。
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="旅店老板"]多谢多谢。不过，今天来送货的怎么是你，往常不都是赞索斯负责的吗？
[charslot(slot="m",name="avg_npc_2069_1#1$1",focus="m")]
[name="吕刻伊昂"]老师有点事要处理，抱歉。
[charslot(slot="m",name="avg_npc_2074_1#1$1",focus="m")]
[name="旅店老板"]好说好说，反正食材也送到了，别耽误后厨开工就行。
[name="旅店老板"]你跟着赞索斯也有两三年了吧？他做事严谨，这么安排肯定有他的道理，我完全放心。
[charslot(slot="m",name="avg_npc_2069_1#1$1",focus="m")]
[name="吕刻伊昂"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="69_g14_luxuriousroom",screenadapt="coverall", block=true)]
[delay(time=2)]
[charslot(slot="l",name="avgnew_482_pallas_1#1$1",focus="all")]
[charslot(slot="r",name="avg_4056_titi_1#1$2",focus="all")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]不好意思啊，帕拉斯。今天神殿的所有人都在赶工，我实在没办法从搬运队里抽调帮手。
[name="缇缇"]作为交换仪式的一环，我想提前把琴放到第一神殿里去，看看是否能匹配上克瑞斯拉雕像。
[name="缇缇"]不过这么重的一把竖琴，我本该找个高大的工匠来帮忙搬运，仅凭我们两个......
[charslot(slot="l",name="avgnew_482_pallas_1#11$1",focus="l")]
[name="帕拉斯"]欸，此话差矣。据史料记载，克瑞斯拉本人身材也并不高大，站在竖琴旁会呈现出极大的反差。
[name="帕拉斯"]说不定我一个人就足够了——
[Dialog]
[charslot(slot="l",posfrom="0,0",posto="-50,-30",duration=1.5,focus="l")]
[delay(time=2.5)]
[charslot(slot="l",posfrom="-50,-30",posto="-45,-30",duration=2.5,block=true,focus="l")]
[CameraShake(duration=2.5, xstrength=0, ystrength=5, vibrato=10, randomness=10, fadeout=false, block=true)]
[playsound(key="$d_avg_dragheavybox")]
[charslot(slot = "l", action="shake",random=true, power=50, times=3,duration=0.8,focus="l")]
[delay(time=1)]
[charslot(slot="l",name="avgnew_482_pallas_1#9$1",focus="l")]
[name="帕拉斯"]呼......这个木箱里面是灌了铅吗，怎么这么沉？
[Dialog]
[charslot(slot="l",posfrom="-50,-30",posto="0,0",duration=1.5)]
[delay(time=2.5)]
[charslot(slot="r",name="avg_4056_titi_1#9$2",focus="r")]
[name="缇缇"]哈哈......我们从古道进入雅赛努斯，路途颠簸，而文物交换事关重大，不能有任何闪失。
[name="缇缇"]出发之前我特地找了我的博物馆的库管员，准备了既能防水避火，又能抗震减压的包材，货物的重量自然也就翻倍了。
[charslot(slot="r",name="avg_4056_titi_1#6$2",focus="r")]
[name="缇缇"]不过好处是，哪怕是楼房倒塌或者突发地震，也伤不了它一点！
[charslot(slot="l",name="avgnew_482_pallas_1#10$1",focus="l")]
[name="帕拉斯"]看得出来，你对自己的博物馆和藏品都很上心。
[charslot(slot="r",name="avg_4056_titi_1#10$2",focus="r")]
[name="缇缇"]我因为对什么都挺感兴趣的，所以干脆去哥伦比亚读了博物馆学，回萨尔贡之后，顺势就进了博物馆。
[name="缇缇"]不过，我的父亲早逝，家族没落......说实话，到现在我都不是很清楚，为什么我会被帕夏选为萨尔贡使节团的大使......
[charslot(slot="r",name="avg_4056_titi_1#9$2",focus="r")]
[name="缇缇"]但事已至此，就得认真对待才行！
[charslot(slot="l",name="avgnew_482_pallas_1#1$1",focus="l")]
[name="帕拉斯"]缇缇，我有没有说过，你——
[Dialog]
[stopmusic(fadetime=2)]
[PlaySound(key="$smallearthquake")]
[delay(time=0.5)]
[bgeffect(name="$eb_dust_01",layer=1)]
[charslot(slot="l",name="avgnew_482_pallas_1#8$1",focus="all")]
[charslot(slot="r",name="avg_4056_titi_1#12$2",focus="all")]
[CameraShake(duration=3.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.3)]
[bgeffect]
[charslot(slot="l",posfrom="0,0",posto="240,0",duration=0.5,focus="all")]
[delay(time=0.3)]
[charslot(slot="r",posfrom="0,0",posto="40,0",duration=0.5,focus="all")]
[PlaySound(key="$d_gen_explo_n", volume=0.3)]
[CameraShake(duration=3,fadeout=tru

... (全文14568字符)
```

### level_act48side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, duration=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="69_g14_luxuriousroom",screenadapt="coverall")]
[PlayMusic(intro="$plot_intro", key="$plot_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, duration=1, block=true)]
[Delay(time=2)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4166_varkis_1#1$1",duration=1)]
[Delay(time=2)]
[name="赞索斯"]萨尔贡大使的房间......这就是百年前被夺走的那件文物？
[Dialog]
[charslot(slot="m",name="avg_4166_varkis_1#1$1",focus="none")]
高大的米诺斯人注视着眼前的巨大木箱，拉响船桨上的马达，那件带有利齿、陪伴他渡河的工具变成了武器，精准地挑开了锁扣。
他郑重地用双手抬起木箱封盖，早该回归家乡的、属于英雄克瑞斯拉的乐器，被完好地包裹在防尘布中。
[charslot(slot="m",name="avg_4166_varkis_1#3$1",focus="m")]
[name="赞索斯"]克瑞斯拉使用过的竖琴，怎么能流落到萨尔贡人之手，又被当作交易的筹码，假惺惺地装在这种虚伪、沉闷的木箱里......
[charslot(slot="m",name="avg_4166_varkis_1#3$1",focus="none")]
[name="帕拉斯"]把琴放下吧，赞索斯。
[Dialog]
[charslot]
[PlaySound(key="$rungeneral")]
[charslot(slot="l",name="avgnew_482_pallas_1#1$1",duration=1)]
[charslot(slot="r",name="avg_4056_titi_1#1$2",duration=1)]
[Delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_4166_varkis_1#1$1",focus="m")]
[name="赞索斯"]帕拉斯，很多人赞扬你一回到雅赛努斯就提议重建第一神殿的壮举，那场投票大会上，我也刻了“赞成”。
[Dialog]
[charslot]
[charslot(slot="l",name="avgnew_482_pallas_1#1$1",focus="l")]
[charslot(slot="r",name="avg_4056_titi_1#1$2",focus="l")]
[name="帕拉斯"]谢谢。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4166_varkis_1#1$1",focus="m")]
[name="赞索斯"]但你不该跟萨尔贡人做朋友。
[Dialog]
[charslot]
[charslot(slot="l",name="avgnew_482_pallas_1#1$1",focus="r")]
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]......
[name="缇缇"]赞索斯先生，您让您的学生撞毁旅店后厨，引发火灾，自己趁乱进入旅店想要偷走涉及两国外交的文物......这并不明智。
[name="缇缇"]旅店外的巷子里挤满了人，现在您根本不可能带着如此巨大的竖琴离开。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4166_varkis_1#14$1",focus="m")]
[name="赞索斯"]......
[Dialog]
[PlaySound(key="$rungeneral")]
[charslot(slot="m",posfrom="0,0",posto="-200,0",afrom=1,ato=0,duration=1.5)]
[delay(time=1.5)]
[PlaySound(key="$d_avg_windowbreak",channel="2")]
[PlaySound(key="$d_avg_doorbreak",channel="3")]
[CameraShake(duration=0.5, xstrength=10, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
[stopmusic(fadetime=2)]
[PlaySound(key="$rungeneral")]
[charslot(slot="l",name="avgnew_482_pallas_1#1$1",posfrom="200,0",posto="0,0",afrom=0,ato=1,duration=1.5)]
[charslot(slot="r",name="avg_4056_titi_1#11$2",posfrom="200,0",posto="0,0",afrom=0,ato=1,duration=1.5)]
[delay(time=2.5)]
[charslot(slot="r",name="avg_4056_titi_1#3$2",focus="r")]
[name="缇缇"]跳窗逃脱？这里可是四楼！
[charslot(slot="l",name="avgnew_482_pallas_1#16$1",focus="l")]
[name="帕拉斯"]不，你房间的正下方就是旅店后厨，撞向一楼的船只不仅是掩护还是接应......他早就想好了。
[name="帕拉斯"]现在从旅店正门追赶一定来不及，倒不如——
[charslot(slot="r",name="avg_4056_titi_1#10$2",focus="r")]
[name="缇缇"]你送我一程？
[charslot(slot="l",name="avgnew_482_pallas_1#7$1",focus="l")]
[name="帕拉斯"]我正有此意。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="69_g5_athenusalley",screenadapt="coverall", block=true)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_npc_2070_1#6$1",duration=1.5)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_2088_1#1$1",focus="m")]
[name="治安官"]执笔人先生，火势已基本得到控制，至于旅店的损失......
[charslot(slot="m",name="avg_npc_2070_1#6$1",focus="m")]
[name="赫卡德墨"]受灾的问题，我会根据流程上报理事官办公室，后厨的损失我已跟旅店老板私了。
[charslot(slot="m",name="avg_npc_2088_1#1$1",focus="m")]
[name="治安官"]辛苦了，我们会在这里驻守一段时间，以防有人借机行不法之事，比如......
[charslot(slot="m",name="avg_npc_2070_1#6$1",focus="m")]
[name="赫卡德墨"]嗯？您怎么突然不说话了？
[charslot(slot="m",name="avg_npc_2088_1#1$1",focus="m")]
[name="治安官"]看、看天上！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_windowbreak",channel="2")]
[PlaySound(key="$d_avg_doorbreak",channel="3")]
[CameraShake(duration=0.5, xstrength=10, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
赫卡德墨抬头。
一对标准的丰蹄的洞角，在阳光下如漆黑的双月。掠过人群，那身影远远落在肇事船只的干草堆上，随后利落地翻下船只，沿河道逃亡。
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, style = "slider", inverse = true, fadetime=0.3, block=true)]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = false, fadetime=0.3, block=true)]
不过几秒，又有一道白色的身影，脚尖点着银色锁链的尖端从窗口一跃而出，数条柔软的衣带包裹着黑色的菲林，保护她轻盈落地。
[Dialog]
[charslot(slot="m",name="avg_npc_2088_1#1$1",focus="m")]
[name="治安官"]那是渡口的赞索斯和萨尔贡的大使小姐？
[name="治安官"]赞索斯身上背着的巨大包裹是什么......难不成......
[charslot(slot="m",name="avg_npc_2070_1#9$1",focus="m")]
[name="赫卡德墨"]......
[name="赫卡德墨"]治安官阁下，被您言中了，看来确实有人趁乱行不法之事。
[charslot(slot="m",name="avg_npc_2088_1#1$1",focus="m")]
[name="治安官"]我明白了。搜查队，封锁现场，扣押肇事船只；巡逻队，立刻跟上梅捷缇克缇小姐，追捕赞索斯！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="69_g5_athenusalley",screenadapt="coverall", block=true)]
[delay(time=2)]
[PlayMusic(intro="$dontmaketrouble_intro", key="$dontmaketrouble_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="l",name="avg_npc_2087_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_2086_1#1$1",duration=1.5)]
[delay(time=2.5)]
[charslot(slot="r",name="avg_npc_2086_1#1$1",focus="r")]
[name="果农代表"]新的一批苹果采收完了，一会儿也麻烦你们帮忙装箱。
[charslot(slot="l",name="avg_npc_2087_1#1$1",focus="l")]
[name="工匠代表"]好嘞，你们帮神殿采了那么多石料，这点小事包在我们身上。
[Dialog]
[charslot(slot="l",name="avg_npc_2087_1#1$1",focus="all")]
[delay(time=0.5)]
[PlaySound(key="$rungeneral")]
[charslot(slot="m",name="avg_4166_varkis_1#1$1",duration=1.5,focus="r,l")]
[delay(time=2.5)]
[name="赞索斯"]麻烦让让。
[charslot(slot="l",name="avg_npc_2087_1#1$1",focus="l")]
[name="工匠代表"]哦哦哦——
[Dialog]
[charslot(slot="l",name="avg_npc_2087_1#1$1",focus="r,l")]
[charslot(slot="l",posfrom="0,0",posto="-100,0",duration=1.5,focus="r,l")]
[charslot(slot="r",posfrom="0,0",posto

... (全文14759字符)
```

### level_act48side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="69_g14_luxuriousroom",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1482_1#8$1",posfrom="-200,0",posto="-200,0",afrom=0, ato=1,duration=1)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1482_1#8$1",focus="m")]
[name="米奥"]（呼呼大睡）
[name="米奥"]（挠挠耳朵）
[Dialog]
[delay(time=1)]
[PlaySound(key="$d_avg_closedoorheavy", volume=1)]
[CameraShake(duration=0.3, xstrength=40, ystrength=40, vibrato=60, randomness=90, fadeout=true, block=false)]
[delay(time=0.7)]
[charslot(slot="m",name="avg_npc_1482_1#8$1",afrom=1, ato=0,duration=0.7)]
[delay(time=0.7)]
[PlaySound(key="$d_avg_meowlong", volume=1)]
[charslot(slot="l",name="avg_npc_1482_1#1$1",afrom=0, ato=1,duration=0.7)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="r",name="avg_4056_titi_1#4$2",afrom=0, ato=1,duration=1.5)]
[Delay(time=2)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[PlaySound(key="$d_avg_meowlong", volume=1)]
[charslot(slot="l",name="avg_npc_1482_1#4$1",focus="l")]
[name="米奥"]梅捷缇克缇！
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]......
[charslot(slot="l",name="avg_npc_1482_1#5$1",focus="l")]
[name="米奥"]一大早就跑没影了不说，现在还摔门打扰我睡觉！交换仪式用的竖琴你到底修好没有，别因为雅赛努斯太好玩了就擅离职守啊！
[charslot(slot="r",name="avg_4056_titi_1#12$2",focus="r")]
[name="缇缇"]......竖琴修好了也没用......
[charslot(slot="l",name="avg_npc_1482_1#5$1",focus="l")]
[name="米奥"]怎么这就放弃了？你这小丫头留学的时候是不是没好好听课，学艺不精，连那么道小裂缝都没法修复？
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]填充和补漆本身不难，但那道裂缝破坏的不只是竖琴——
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]还有你摇摇欲坠的心？
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]还有萨尔贡的信誉。
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]什么？
[charslot(slot="r",name="avg_4056_titi_1#12$2",focus="r")]
[name="缇缇"]这件克瑞斯拉竖琴是我见过的保存最完好的文物之一。
[name="缇缇"]而且木制乐器有其特殊性，哪怕琴体发生一点磕碰，都可能改变它原本的音色。
[charslot(slot="r",name="avg_4056_titi_1#10$2",focus="r")]
[name="缇缇"]所以鉴定时我们非常小心，甚至放弃了所有带有破坏性质的检测......
[charslot(slot="l",name="avg_npc_1482_1#4$1",focus="l")]
[name="米奥"]这些讲解词我在博物馆听得耳朵都起茧子了——
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]“根据纹饰、琴弦材质、上漆工艺判断，这件文物确实是典型的米诺斯风格，再佐以史料证据，它极有可能是克瑞斯拉使用过的竖琴。”
[charslot(slot="r",name="avg_4056_titi_1#2$2",focus="r")]
[name="缇缇"]可昨天晚上修琴的时候我就觉得不对......
[name="缇缇"]根据裂口掉落的木屑来看，它的材质确实是古代米诺斯制琴常用的杉树，但断面的纹理却不太自然。
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]英雄的武器自然由千年古树制成，有点木纹也很正常。
[charslot(slot="r",name="avg_4056_titi_1#10$2",focus="r")]
[name="缇缇"]不，那不像是木材的自然纹理，反倒像是某种萨尔贡特有的保水工艺。
[charslot(slot="r",name="avg_4056_titi_1#1$2",focus="r")]
[name="缇缇"]我曾读过研究乐器制作的古籍。书上说，米诺斯的草木含水量充足，而萨尔贡大部分地区的气候都相对干燥。
[name="缇缇"]因此，哪怕是从米诺斯进口木料，也必须做一次特殊处理，以防木材因为湿度太低而开裂。
[name="缇缇"]这把琴上断面的纹理，很像是这种保水工艺的痕迹。
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]你是说这是一把从前的萨尔贡人用米诺斯木料仿制的竖琴，不是克瑞斯拉使用过的真品？你想太多了吧？
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]我也不愿意相信，但刚才，我带着部分木屑去找了化学实验室。
[name="缇缇"]实验证明，木料中确实混有特殊的化学物质，是一种百年前的萨尔贡树脂......
[charslot(slot="l",name="avg_npc_1482_1#4$1",focus="l")]
[name="米奥"]嘶......
[charslot(slot="r",name="avg_4056_titi_1#1$2",focus="r")]
[name="缇缇"]这把竖琴的外观简直天衣无缝，如果不进行破坏性的取样，几乎很难发现它是赝品，我猜赫里帕夏也并不知情。
[charslot(slot="r",name="avg_4056_titi_1#2$2",focus="r")]
[multiline(name="缇缇")]得尽快把这件事告诉里底娅理事官，不能在克瑞斯拉雕像的注视下，用一把假琴换取米诺斯人的信任，
[charslot(slot="r",name="avg_4056_titi_1#13$2",focus="r")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=50, randomness=70, fadeout=true, block=false)]
[multiline(name="缇缇")]我得终止这场交换仪式！
[charslot]
[name="？？？"]可梅捷缇克缇大使的任务，是顺利“完成”交换仪式啊。
[charslot(slot="m",name="avg_4056_titi_1#1$2",focus="m")]
[name="缇缇"]贝赫努先生......
[charslot]
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_2077_1#6$1",afrom=0, ato=1,duration=1.5)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_2077_1#6$1",focus="m")]
[name="贝赫努"]我们出使前曾向帕夏起誓。你若不能换回三城建设时期的工程资料，那怎么还有资格顶着萨尔贡大使的名号？
[charslot(slot="m",name="avg_4056_titi_1#10$2",focus="m")]
[name="缇缇"]......
[charslot(slot="m",name="avg_4056_titi_1#2$2",focus="m")]
[name="缇缇"]你说得没错，大使的工作是我的职责，但鉴定是我的专业，面对如此重大的失误，我不可能弄虚作假。
[charslot(slot="m",name="avg_npc_2077_1#6$1",focus="m")]
[name="贝赫努"]我说过，你并没有政治头脑。比起使节团的负责人，你更喜欢博物馆馆长这个身份。
[name="贝赫努"]文物交换仪式重要的并非“文物”，而是“交换仪式”。假琴又如何，它不是依旧可以鸣响吗？
[charslot(slot="m",name="avg_4056_titi_1#3$2",focus="m")]
[multiline(name="缇缇")]贝赫努，你想用假琴进行交换仪式？
[charslot(slot="m",name="avg_4056_titi_1#13$2",focus="m")]
[multiline(name="缇缇")]绝对不行！
[charslot(slot="m",name="avg_npc_2077_1#5$1",focus="m")]
[name="贝赫努"]现在真琴不知所终，交换仪式又迫在眉睫，你还能想出什么方法，梅捷缇克缇小姐？
[name="贝赫努"]在出使之前，米纳特哈玛仪的殿堂之上，你曾对赫里帕夏说，你喜爱米诺斯的英雄传说，从小就想知道在现实之中何为真正的英雄气概。
[name="贝赫努"]难不成你所谓的英雄气概，就是固执己见，我行我素，在两国建交后的第一次文化交流活动中，令自己的国家蒙羞？
[charslot(slot="m",name="avg_npc_2077_1#2$1",focus="m")]
[name="贝赫努"]哦，我想起来了。那你和你无病呻吟、一无是处的父亲，有什么区别？
[charslot(slot="m",name="avg_npc_2077_1#5$1",focus="m")]
[name="贝赫努"]是他令你们的家族没落，让“娜苏图-玛夏耶尔”沦为被其他贵族耻笑的名字。
[name="贝赫努"]是他沉溺文学，抛弃责任，甚至放弃抚养子嗣，让自己的女儿只能从书里，而不是从自己身上找到英雄的影子。
[charslot(slot="m",name="avg_4056_titi_1#13$2",focus="m")]
[name="缇缇"]这件事跟我的父亲无关！我喜欢米诺斯的故事只是因为——
[charslot(slot="m",name="avg_npc_2077_1#6$1",focus="m")]
[name="贝赫努"]“我们作为萨尔贡的使节，最重要的是顺利完成交换仪式，个人的执念和追求并不重要。”
[name="贝赫努"]这可是你的原话。
[charslot(slot="m",name="avg_4056_titi_1#10$2",focus="m")]
[name="缇缇"]......
[charslot(slot="m",name="avg_4056_titi_1#11$2",focus="m")]
[name="缇缇"]我会在交换仪式前想到办法，哪怕要耗费再多的精力和时间，也不能让一件赝品......
[charslot(slot="m",name="avg_npc_2077_1#6$1",focus="m")]
[name="贝赫努"]真是冥顽不灵。
[name="贝赫努"]既然如此，在你苦思冥想的这段时间里，我就代行梅捷缇克缇小姐的职权，替你处理萨尔贡大使本应该处理的工作好了，不过......
[charslot(slot="m",name="avg_npc_2077_1#1$1",focus="m")]
[name="贝赫努"]我猜，在理事官和受邀宾客的眼里，你只是一个兴致勃勃的小女孩，一个在神殿干苦力的负责人，而与理事官进行谈判的我——
[charslot(slot="m",name="avg_np

... (全文17565字符)
```

### level_act48side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="69_g8_templetheater",screenadapt="coverall", block=true)]
[charslot(slot="r",name="avg_4056_titi_1#10$2")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$dignified_intro", key="$dignified_loop", volume=0.6)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="l",name="avgnew_482_pallas_1#10$1",afrom=0, ato=1,duration=1.5)]
[delay(time=2)]
[charslot(slot="r",name="avg_4056_titi_1#10$2",focus="r")]
[charslot(slot="l",name="avgnew_482_pallas_1#10$1",focus="r")]
[name="缇缇"]......
[charslot(slot="l",name="avgnew_482_pallas_1#22$1",focus="l")]
[name="帕拉斯"]约我过来的人反而一言不发？我可是为了陪你推掉了第一神殿初步建成的庆功宴啊。
[charslot(slot="l",name="avgnew_482_pallas_1#10$1",focus="l")]
[name="帕拉斯"]能在交换仪式前一天按计划完成重建工作，你功不可没。按照惯例这可是要庆祝整整一天的，工匠们从白天就开始吟诗喝酒了。
[charslot(slot="r",name="avg_4056_titi_1#10$2",focus="r")]
[name="缇缇"]有些人的酒量不太好，要是贪杯，我估计今天晚上治安官可就有的忙了。
[charslot(slot="l",name="avgnew_482_pallas_1#11$1",focus="l")]
[name="帕拉斯"]哈哈，你说的是搬运队的坎提亚吧？你帮了她好几次，那个小姑娘很喜欢你。
[charslot(slot="r",name="avg_4056_titi_1#1$2",focus="r")]
[name="缇缇"]嗯......来雅赛努斯的这几天就像做梦一样。
[charslot(slot="l",name="avgnew_482_pallas_1#10$1",focus="l")]
[name="帕拉斯"]可不是嘛。
[name="帕拉斯"]到雅赛努斯的第一天你就解决了果农和工匠的争执，后来又成为神殿重建收尾阶段的负责人。
[name="帕拉斯"]前几天竖琴被盗，你还追了赞索斯七八条街。
[name="帕拉斯"]哪件事都比护送文物有趣多了，不是吗？
[charslot(slot="r",name="avg_4056_titi_1#10$2",focus="r")]
[name="缇缇"]是啊。
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]但保证交换仪式顺利进行，增进两国友好，才是我本来最该做的事。
[charslot(slot="l",name="avgnew_482_pallas_1#20$1",focus="l")]
[name="帕拉斯"]缇缇，你怎么了？这话可不像是你会说的啊？
[charslot(slot="r",name="avg_4056_titi_1#2$2",focus="r")]
[name="缇缇"]帕拉斯。
[charslot(slot="r",name="avg_4056_titi_1#2$2",focus="r")]
[name="缇缇"]萨尔贡使节团带来的克瑞斯拉竖琴......是仿制品。
[charslot(slot="l",name="avgnew_482_pallas_1#17$1",focus="l")]
[name="帕拉斯"]什么？
[charslot(slot="r",name="avg_4056_titi_1#1$2",focus="r")]
[name="缇缇"]要不是赞索斯先生跟我争夺竖琴，失手伤到了琴，我也不会发现竖琴有问题。
[charslot(slot="r",name="avg_4056_titi_1#10$2",focus="r")]
[name="缇缇"]现在使节团的副使贝赫努先生想用修补好的假琴进行交换仪式，完成帕夏交给我们的任务......但这件事不该这样收场。
[charslot(slot="l",name="avgnew_482_pallas_1#8$1",focus="l")]
[name="帕拉斯"]缇缇，明天就是交换仪式了，你今天找我，是不是已经想到了解决方法？
[charslot(slot="r",name="avg_4056_titi_1#12$2",focus="r")]
[name="缇缇"]说实话，除非出现神迹，否则没有任何妥善的解决方法。
[charslot(slot="r",name="avg_4056_titi_1#11$2",focus="r")]
[name="缇缇"]我翻阅了雅赛努斯图书馆能借阅到的所有相关古籍，发现克瑞斯拉竖琴很早就在战争中逸失，完全没有踪迹。
[name="缇缇"]我猜测，连制作这把仿制品的萨尔贡工匠都只见过图纸，没有接触过真品。
[charslot(slot="l",name="avgnew_482_pallas_1#16$1",focus="l")]
[name="帕拉斯"]那是不是说明真琴很有可能就在米诺斯？或者......
[charslot(slot="r",name="avg_4056_titi_1#12$2",focus="r")]
[name="缇缇"]早就被战争的炮火轰成灰烬了......对不起。
[charslot(slot="l",name="avgnew_482_pallas_1#16$1",focus="l")]
[name="帕拉斯"]......你不需要道歉。
[charslot(slot="l",name="avgnew_482_pallas_1#20$1",focus="l")]
[name="帕拉斯"]既然真琴的下落难以追觅，你打算怎么做？
[charslot(slot="r",name="avg_4056_titi_1#1$2",focus="r")]
[name="缇缇"]我无法在大庭广众之下以萨尔贡大使的身份宣告我们带来的是假琴，我很担心这样的举动，比起揭露真相，更可能再次引发冲突。
[charslot(slot="l",name="avgnew_482_pallas_1#16$1",focus="l")]
[name="帕拉斯"]唔，你的顾虑没有错。
[charslot(slot="r",name="avg_4056_titi_1#2$2",focus="r")]
[name="缇缇"]所以，终止仪式只能靠个人行为。
[charslot(slot="l",name="avgnew_482_pallas_1#20$1",focus="l")]
[name="帕拉斯"]什么意思？
[charslot(slot="r",name="avg_4056_titi_1#2$2",focus="r")]
[name="缇缇"]我要在仪式开始之前，带走假琴。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1.5)]
[Background(image="69_g4_athenusstreet",screenadapt="coverall", block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlayMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[charslot(slot="l",name="avg_npc_2089_1#1$1",afrom=0, ato=1,duration=1.5)]
[charslot(slot="r",name="avg_npc_2070_1#8$1",afrom=0, ato=1,duration=1.5)]
[delay(time=2)]
[charslot(slot="l",name="avg_npc_2089_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_2070_1#8$1",focus="l")]
[name="狱警"]你不能进去。
[charslot(slot="r",name="avg_npc_2070_1#10$1",focus="r")]
[name="赫卡德墨"]我知道探监和寄送物资都需要特殊访客证明，但我这不是一着急就忘了嘛......
[name="赫卡德墨"]您能不能通融通融，我那个老同学前天刚进去，什么都没准备，他家人托我给他带些东西。
[charslot(slot="l",name="avg_npc_2089_1#1$1",focus="l")]
[name="狱警"]......
[charslot(slot="r",name="avg_npc_2070_1#3$1",focus="r")]
[name="赫卡德墨"]唉，我实话跟您说吧，他病得很重，可能很快就......
[charslot(slot="r",name="avg_npc_2070_1#11$1",focus="r")]
[name="赫卡德墨"]雅赛努斯的监管所虽然配备了医生和基础药物，但本地的药物没有罗德岛带来的有效，要是抑制不住，怕是在拘留期间就会发作。
[charslot(slot="l",name="avg_npc_2089_1#1$1",focus="l")]
[name="狱警"]别跟我说这些，没用。
[charslot(slot="r",name="avg_npc_2070_1#10$1",focus="r")]
[name="赫卡德墨"]狱警女士，我真不想这样......
[charslot(slot="r",name="avg_npc_2070_1#9$1",focus="r")]
[name="赫卡德墨"]喏，看到工作证了吗？我是理事官的执笔人，赫卡德墨。
[name="赫卡德墨"]原则上我有进入监管所甚至提审嫌疑人的权力，虽然中间要过几道必要手续，但事后我会补齐。现在，我命令你开门。
[charslot(slot="l",name="avg_npc_2089_1#1$1",focus="l")]
[name="狱警"]......
[name="狱警"]你要见的是前天那两个偷东西的贼？
[charslot(slot="r",name="avg_npc_2070_1#9$1",focus="r")]
[multiline(name="赫卡德墨")]吕刻伊昂不是......
[charslot(slot="r",name="avg_npc_2070_1#8$1",focus="r")]
[multiline(name="赫卡德墨")]算了，是他们。
[charslot(slot="l",name="avg_npc_2089_1#1$1",focus="l")]
[name="狱警"]不行。
[charslot(slot="r",name="avg_npc_2070_1#5$1",focus="r")]
[name="赫卡德墨"]为什么还是不行！
[charslot(slot="l",name="avg_npc_2089_1#1$1",focus="l")]
[name="狱警"]执笔人确实可以探视监管所的犯人，但你说的那两位，已经不在这里了。
[charslot(slot="r",name="avg_npc_2070_1#4$1",focus="r")]
[multiline(name="赫卡德墨")]转狱了？
[charslot(slot="r",name="avg_npc_2070_1#3$1",focus="r")]
[multiline(name="赫卡德墨")]真少见，难道是莱娜小姐想推行的感染者治疗体系已经开始实施了......
[charslot(slot="r",name="avg_npc_2070_1#9$1",focus="r")]
[name="赫卡德墨"]麻烦您告诉我他们去了哪座监管所？
[charslot(slot="l",name="avg_npc_2089_1#1$1",focus="l")]
[name="狱警"]唉，别费工夫了。赫卡德墨，我不知道对方到底跟你是什么关系，但仅凭理事官执笔人的权限，可进不了死牢。
[CameraShake(duration=0.2, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="r",name="avg_npc_20

... (全文14059字符)
```

### level_act48side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="69_g9_templetheater_n",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1.5)]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[charslot(slot="r",name="avg_4056_titi_1#10$1",afrom=0, ato=1,duration=1.5)]
[charslot(slot="l",name="avgnew_482_pallas_1#20$1",afrom=0, ato=1,duration=1.5)]
[delay(time=1.5)]
[charslot(slot="r",name="avg_4056_titi_1#10$1",focus="l")]
[charslot(slot="l",name="avgnew_482_pallas_1#20$1",focus="l")]
[name="帕拉斯"]......
[charslot(slot="r",name="avg_4056_titi_1#10$1",focus="r")]
[name="缇缇"]......
[charslot(slot="r",name="avg_4056_titi_1#1$1",focus="r")]
[name="缇缇"]天色晚了，帕拉斯，该分头准备了。
[charslot(slot="l",name="avgnew_482_pallas_1#20$1",focus="l")]
[name="帕拉斯"]缇缇，你真的想好了要这么做？
[charslot(slot="r",name="avg_4056_titi_1#2$1",focus="r")]
[name="缇缇"]是的。自从贝赫努先生知道我们护送的文物是仿制品后，他就把竖琴交给了随行护卫看守，不让我靠近一步。
[name="缇缇"]今晚，他一定会派人加紧巡逻，以防出现任何意外，但到了明天的交换仪式，就不一样了。
[charslot(slot="l",name="avgnew_482_pallas_1#16$1",focus="l")]
[name="帕拉斯"]他必须让竖琴暴露在公共场所，这样我们才能有机会......
[charslot(slot="r",name="avg_4056_titi_1#1$1",focus="r")]
[name="缇缇"]没错。
[charslot(slot="l",name="avgnew_482_pallas_1#20$1",focus="l")]
[name="帕拉斯"]可是然后呢？
[charslot(slot="r",name="avg_4056_titi_1#10$1",focus="r")]
[name="缇缇"]然后？萨尔贡官方估计会对整桩事件进行形式化的公开道歉，私下会再派外交官与里底娅理事官沟通。
[charslot(slot="r",name="avg_4056_titi_1#2$1",focus="r")]
[name="缇缇"]表面上是萨尔贡使节携米诺斯国宝逃亡，实际上两国的相关负责人都会知道，丢失的只是一件仿制品而已。
[charslot(slot="l",name="avgnew_482_pallas_1#20$1",focus="l")]
[name="帕拉斯"]我问的不是这个，缇缇，我只想知道你会怎么样。
[charslot(slot="r",name="avg_4056_titi_1#10$1",focus="r")]
[name="缇缇"]我？
[charslot(slot="r",name="avg_4056_titi_1#11$1",focus="r")]
[name="缇缇"]我会带着假琴和米奥，从古道离开。米纳特哈玛仪是不能回了，赫里帕夏的卫兵肯定会满城追捕我。
[name="缇缇"]真要被逮到了，无论是贝赫努先生还是赫里帕夏都有可能会消除对己方不利的证据，并把过错推到米诺斯方。
[charslot(slot="r",name="avg_4056_titi_1#14$1",focus="r")]
[name="缇缇"]只有我一直逃，萨尔贡那些位高权重的贵族才不敢擅自给这桩“偷窃案”定性。我带走的是假琴，也是真相。
[charslot(slot="l",name="avgnew_482_pallas_1#4$1",focus="l")]
[name="帕拉斯"]缇缇......
[charslot(slot="r",name="avg_4056_titi_1#6$1",focus="r")]
[name="缇缇"]好啦，不要劝我了。
[name="缇缇"]如果有更好的方法，我也不想带着一把又大又重的琴环游泰拉啊。
[charslot(slot="r",name="avg_4056_titi_1#9$1",focus="r")]
[name="缇缇"]回去吧，帕拉斯，让我一个人待一会，我们明天早上再见。
[charslot(slot="l",name="avgnew_482_pallas_1#5$1",focus="l")]
[name="帕拉斯"]好......
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="l",afrom=1, ato=0,posfrom="0,0",posto="-150,0",duration=1.5,focus="l")]
[delay(time=2)]
[charslot(slot="r",name="avg_4056_titi_1#10$1",focus="r")]
[name="缇缇"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[gridbg(imagegroup="38_g21_skystarry_L1/38_g21_skystarry_r1/38_g21_skystarry_L2/38_g21_skystarry_r2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720",x=-640,fadetime=0)]
[largebgtween(duration = 60,yFrom = 360, yTo = 720,block = false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="缇缇靠在广场观众席的椅背上抬头看。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="在米诺斯，夜空总是晴朗通透，深得观星爱好者青睐。也正因这得天独厚的优势，自古以来米诺斯人都会将英雄与星辰的位置对应。", x=300, y=350, alignment="center", size=23, delay=0.04, width=700)]
[Subtitle(text="很小的时候，缇缇的父亲会一边望着星空，一边跟她讲英雄的故事。", x=300, y=350, alignment="center", size=23, delay=0.04, width=700)]
[Subtitle(text="有些能从书里找到，而没有出处的那些，它们或许是这个在功业上毫无建树、单单爱好文学的父亲胡编乱造的。", x=300, y=350, alignment="center", size=23, delay=0.04, width=700)]
[Subtitle(text="尽管后来病痛过早地将他带离人世，但缇缇现在还能清晰地记起父亲讲述的每一个故事。", x=300, y=350, alignment="center", size=23, delay=0.04, width=700)]
[Subtitle(text="在那些故事里，在米诺斯的故事里，会不会存在着一位带着假琴逃亡的英雄？", x=300, y=350, alignment="center", size=23, delay=0.04, width=700)]
[Subtitle(text="千万星辰沉默地在夜空中闪烁，缇缇没有找到答案。", x=300, y=350, alignment="center", size=23, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1.5)]
[charslot]
[gridbg]
[delay(time=1.5)]
[Background(image="69_g13_generalroom_n",screenadapt="coverall", block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=0.8)]
[charslot(slot="l",name="avg_npc_2070_1#9$1",focus="l")]
[name="赫卡德墨"]都这么晚了，早过了我的下班时间，有什么事明天上班再说——
[charslot(slot="l",name="avg_npc_2070_1#9$1",focus="n")]
[name="？？？"]理事官的执笔人先生，是我。
[charslot(slot="l",name="avg_npc_2070_1#4$1",focus="l")]
[name="赫卡德墨"]卡珊卓拉小姐？
[Dialog]
[PlaySound(key="$dooropenquite", volume=1)]
[delay(time=0.7)]
[charslot(slot="r",name="avg_npc_2068_1#1$1",duration=1)]
[delay(time=2)]
[charslot(slot="r",name="avg_npc_2068_1#1$1",focus="r")]
[name="卡珊卓拉"]实在抱歉，我知道现在是您的休息时间。
[charslot(slot="l",name="avg_npc_2070_1#10$1",focus="l")]
[name="赫卡德墨"]呃......您深夜造访所为何事？
[charslot(slot="r",name="avg_npc_2068_1#4$1",focus="r")]
[name="卡珊卓拉"]我想问您，对于赞索斯师徒的盗窃案，里底娅理事官有没有跟您说过什么？
[name="卡珊卓拉"]早些时候我造访理事官办公室与里底娅小姐商议戏剧仪式的剧目，提到前几天发生的那桩案件时，她态度模糊。
[charslot(slot="l",name="avg_npc_2070_1#3$1",focus="l")]
[name="赫卡德墨"]啊，里底娅理事官想必有自己的考量。明天就是文物交换仪式，她不仅需要处理流程问题，还要应付萨尔贡使节团。
[charslot(slot="r",name="avg_npc_2068_1#6$1",focus="r")]
[name="卡珊卓拉"]这正是我担心的。
[name="卡珊卓拉"]如果萨尔贡使节团以影响两国信任关系为由，要求对案件重新定性，负责外交事宜的里底娅理事官几乎无法拒绝。
[charslot(slot="r",name="avg_npc_2068_1#4$1",focus="r")]
[name="卡珊卓拉"]商谈的时候，我能看出她的神情有些紧张，一旁的办公桌上堆放着米诺斯法律大全和事件调查报告。
[name="卡珊卓拉"]她很有可能已经受到使节的胁迫。这样一来赞索斯师徒的罪名只会更重，而且......
[charslot(slot="l",name="avg_npc_2070_1#6$1",focus="l")]
[name="赫卡德墨"]而且？
[charslot(slot="r",name="avg_npc_2068_1#1$1",focus="r")]
[name="卡珊卓拉"]如果不是因为您感染矿石病的同窗危在旦夕，我想您家的沙发扶手后面，应该也不会有一条沃尔珀的尾巴。
[charslot(slot="l",name="avg_npc_2070_1#3$1",focus="l")]
[name="赫卡德墨"]......
[charslot]
[name="？？？"]......
[char

... (全文14594字符)
```

### level_act48side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_wilderness_y",screenadapt="coverall", block=true)]
[bgeffect(name = "$eb_blackmask" ,layer = 1)]
[bgeffect(name="$eb_oldtv",layer=2)]
[Delay(time=1)]
[PlayMusic(key="$minos_folk_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_2081_1#1$1",afrom=0, ato=1,duration=1.5)]
[charslot(slot="r",name="avg_4166_varkis_1#1$2",afrom=0, ato=1,duration=1.5)]
[delay(time=2)]
[charslot(slot="l",name="avg_npc_2081_1#1$1",focus="l")]
[charslot(slot="r",name="avg_4166_varkis_1#1$2",focus="l")]
[name="忧心的村民"]你真决定要离开村子啦？
[charslot(slot="r",name="avg_4166_varkis_1#1$2",focus="r")]
[name="赞索斯"]明天天一亮就动身。
[charslot(slot="r",name="avg_4166_varkis_1#8$2",focus="r")]
[name="赞索斯"]田地都已经重新耕过一遍，种子和存粮足够，仓库也都修过，摆渡的技术，我也教给了那几个年轻人，别担心。
[charslot(slot="l",name="avg_npc_2081_1#1$1",focus="l")]
[name="忧心的村民"]我是担心你啊，赞索斯。
[name="忧心的村民"]你从来没离开过这片沼地，现在跑那么远的路，就为了找一个外乡人？
[charslot(slot="r",name="avg_4166_varkis_1#10$2",focus="r")]
[name="赞索斯"]伊萨科斯是我的兄弟，他也帮助过我们所有人。
[charslot(slot="l",name="avg_npc_2081_1#1$1",focus="l")]
[name="忧心的村民"]一年过去了，或许他已经回雅赛努斯了......毕竟，那才是他的故乡。
[charslot(slot="r",name="avg_4166_varkis_1#13$2",focus="r")]
[name="赞索斯"]他答应过的事，都会做到。
[name="赞索斯"]他答应过我，打完了仗，便会回来。
[charslot(slot="l",name="avg_npc_2081_1#1$1",focus="l")]
[name="忧心的村民"]那你有没有想过，如果，如果他已经......
[name="忧心的村民"]他去的地方，可是和萨尔贡人的战场......
[charslot(slot="r",name="avg_4166_varkis_1#12$2",focus="r")]
[name="赞索斯"]那我就替他报仇，替米诺斯人报仇。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1.5)]
[Background(image="bg_wild_m",screenadapt="coverall", block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_heavy", pos = "-400,-200", block = false)]<p=1>米诺斯，北部山地</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot="l",name="avg_4166_varkis_1#2$1",posfrom="150,0",posto="150,0",afrom=0, ato=1,duration=1)]
[charslot(slot="r",name="avg_npc_2084_1#1$1",duration=1)]
[delay(time=1.5)]
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.7)]
[charslot(slot="l",name="avg_4166_varkis_1#2$1",focus="r")]
[charslot(slot="r",name="avg_npc_2084_1#1$1",focus="r")]
[name="游击队员A"]你别激动！你认错人了！我真的不是什么伊萨科斯！
[charslot(slot="l",name="avg_4166_varkis_1#1$1",focus="l")]
[name="赞索斯"]激动的是你，同胞。我只是认出了你身上的这块护甲。
[charslot(slot="r",name="avg_npc_2084_1#1$1",focus="r")]
[name="游击队员A"]......
[Dialog]
[charslot(slot="l",posfrom="150,0",posto="0,0",duration=1)]
[delay(time=1)]
[charslot(slot="l",name="avg_4166_varkis_1#3$1",focus="l")]
[name="赞索斯"]它属于伊萨科斯，我的弟弟。临行前，村里每家每户都送来了兽皮和铁器，我亲手为他缝制了勉强像样的全身甲胄，打造了武器。
[charslot(slot="r",name="avg_npc_2084_1#1$1",focus="r")]
[name="游击队员A"]抱、抱歉，一直在打仗，大大小小的仗，我已经很久没睡过好觉了，精神有些......
[charslot(slot="l",name="avg_4166_varkis_1#1$1",focus="l")]
[name="赞索斯"]给你，壶里还有一些宁神的草茶。
[Dialog]
[charslot(slot="r",name="avg_npc_2084_1#1$1",focus="r")]
[PlaySound(key="$d_avg_drinkswllw",channel="1")]
[PlaySound(key="$d_avg_drinkswllw",channel="2",delay=1)]
[delay(time=2)]
[charslot(slot="l",name="avg_4166_varkis_1#1$1",focus="l")]
[name="赞索斯"]请告诉我，你从谁那里得到的这块护甲？
[charslot(slot="r",name="avg_npc_2084_1#1$1",focus="r")]
[name="游击队员A"]另一个游击队的战友。我们在一场遭遇战中相遇......他中了箭，咽气前，给了我......
[charslot(slot="l",name="avg_4166_varkis_1#11$1",focus="l")]
[name="赞索斯"]......
[charslot(slot="r",name="avg_npc_2084_1#1$1",focus="r")]
[name="游击队员A"]但他不叫伊萨科斯。
[charslot(slot="l",name="avg_4166_varkis_1#15$1",focus="l")]
[name="赞索斯"]呼......
[charslot(slot="r",name="avg_npc_2084_1#1$1",focus="r")]
[name="游击队员A"]你看这护甲上面的痕迹，斑驳成这样，明显已经经手过很多人......
[name="游击队员A"]你或许不了解，游击队不比萨尔贡人的正规军，我们的物资非常有限。
[name="游击队员A"]大家往往会将武器、防具和粮食集中起来，再按照任务的优先级统一调配。
[name="游击队员A"]我可以告诉你那个战友所在游击队的番号，指给你他们现在所在的方位......啊，我得先把这块护甲还给你。
[charslot(slot="l",name="avg_4166_varkis_1#13$1",focus="l")]
[name="赞索斯"]留着吧，你还用得着。同胞，指给我方向就好。
[charslot(slot="r",name="avg_npc_2084_1#1$1",focus="r")]
[name="游击队员A"]可以是可以，但你真要进山找吗？
[name="游击队员A"]这一整片山地都是游击队活跃的地方，是我们和萨尔贡人的战场......
[charslot(slot="l",name="avg_4166_varkis_1#1$1",focus="l")]
[name="赞索斯"]那我申请加入游击队。
[charslot(slot="r",name="avg_npc_2084_1#1$1",focus="r")]
[name="游击队员A"]你上过战场吗？
[charslot(slot="l",name="avg_4166_varkis_1#13$1",focus="l")]
[name="赞索斯"]（摇头）在这之前，我的手只握过船桨和农具。
[charslot(slot="l",name="avg_4166_varkis_1#15$1",focus="l")]
[name="赞索斯"]但我们别无选择，不是吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1.5)]
[Background(image="bg_wild_a",screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_npc_2083_1#1$1",posfrom="0,0",posto="-40,0",duration=0)]
[charslot(slot="r",name="avg_4166_varkis_1#1$1")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_2083_1#1$1",focus="l")]
[charslot(slot="r",name="avg_4166_varkis_1#1$1",focus="l")]
[name="游击队员B"]抱歉，你说的那个爱笑的长发丰蹄，我没有太多印象。
[name="游击队员B"]至于这双靴子，是我刚加入游击队时领到的......按照当时送物资过来的战友的说法，它属于一个左边角缺了一块的中年大叔。
[charslot(slot="r",name="avg_4166_varkis_1#3$1",focus="r")]
[name="赞索斯"]它破了。
[charslot(slot="l",name="avg_npc_2083_1#1$1",focus="l")]
[name="游击队员B"]对、对不起。它对我来说有点小了，我还没来得及补。
[name="游击队员B"]那帮萨尔贡人一直撵在我们后面，要不是你及时赶到支援......
[charslot(slot="r",name="avg_4166_varkis_1#1$1",focus="r")]
[name="赞索斯"]坐下来。
[charslot(slot="l",name="avg_npc_2083_1#1$1",focus="l")]
[name="游击队员B"]啊？
[charslot(slot="r",name="avg_4166_varkis_1#1$1",focus="r")]
[name="赞索斯"]我帮你补。
[Dialog]
[PlaySound(key="$d_avg_clothmovement",volume=1)]
[charslot(duration=1.2)]
[delay(time=2)]
[PlaySound(key="$d_avg_putontable_large")]
[delay(time=1.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[B

... (全文19372字符)
```

### level_act48side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="69_g12_generalroom",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_1022_flwr2_1#12$2",duration=0.7)]
[charslot(slot="r",name="avg_npc_2070_1#6$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="l",name="avg_1022_flwr2_1#12$2",focus="l")]
[name="莱娜"]这里是两人份的矿石病抑制剂，从他俩上次注射到现在已经有几天了，最好是见到了就先给他们各注射一支，以免矿石病急性发作。
[name="莱娜"]剩下的是些比较常规的药，这一板是止痛的，这些可以增加心肺功能，剩下的可以控制血压和血氧饱和度。
[charslot(slot="l",name="avg_1022_flwr2_1#4$2",focus="l")]
[name="莱娜"]不过赞索斯先生有些讳疾忌医，可能不愿意服用，总之你先都带上，硬塞给他，让他身上备着就好。
[name="莱娜"]矿石病抑制剂一定得注射，其他的就看他自己吧。
[charslot(slot="r",name="avg_npc_2070_1#6$1",focus="r")]
[name="赫卡德墨"]好。这些都是给赞索斯的？那给吕刻伊昂的呢？
[charslot(slot="l",name="avg_1022_flwr2_1#16$2",focus="l")]
[name="莱娜"]吕刻伊昂？在他病情的那个阶段，能做的也就是注射抑制剂了。
[charslot(slot="r",name="avg_npc_2070_1#11$1",focus="r")]
[name="赫卡德墨"]......已经这么严重了吗......
[charslot(slot="l",name="avg_1022_flwr2_1#12$2",focus="l")]
[multiline(name="莱娜")]还好吧，不用太担心。
[PlaySound(key="$d_avg_plasticbag", volume=1)]
[multiline(name="莱娜")]先看看这个袋子，我给你们准备了三人份的水和奶酪皮塔派。
[charslot(slot="r",name="avg_npc_2070_1#10$1",focus="r")]
[name="赫卡德墨"]莱娜小姐，我不是去郊游的......
[charslot(slot="l",name="avg_1022_flwr2_1#12$2",focus="l")]
[name="莱娜"]我知道，带上嘛，万一一会儿肚子饿了呢？
[name="莱娜"]放心，我还给你准备了一些实用的物品。
[name="莱娜"]封在这个盒子里的，是一些我特制的香丸，捏开的时候会有迷香的效果。你也带上，以防万一。
[charslot(slot="l",name="avg_1022_flwr2_1#12$2",focus="l")]
[name="莱娜"]不过要当心，如果真需要拿出来用，记得站在上风口，别把自己给迷晕啦。
[charslot(slot="r",name="avg_npc_2070_1#10$1",focus="r")]
[name="赫卡德墨"]......莱娜小姐......我们不是都安排好了吗？
[charslot(slot="r",name="avg_npc_2070_1#6$1",focus="r")]
[name="赫卡德墨"]卡珊卓拉小姐帮我们弄到了狱警的换班时间表。
[charslot(slot="r",name="avg_npc_2070_1#3$1",focus="r")]
[name="赫卡德墨"]理事官办公室有监狱牢门和脚镣钥匙的备份，我也复制了——
[name="赫卡德墨"]该不该说百密一疏呢，里底娅小姐似乎完全没有防备，直接把它们摆在了桌上。
[charslot(slot="r",name="avg_npc_2070_1#6$1",focus="r")]
[name="赫卡德墨"]劫狱这种事儿这些年里没多少人干过，牢里的警戒不算森严，我掐着时间进去把人带出来就走，应该不至于遇到太大阻碍。
[name="赫卡德墨"]莱娜小姐不必太过紧张。
[charslot(slot="l",name="avg_1022_flwr2_1#9$2",focus="l")]
[name="莱娜"]......
[name="莱娜"]我知道，我在想的其实是......之后的事。
[charslot(slot="r",name="avg_npc_2070_1#11$1",focus="r")]
[name="赫卡德墨"]您是担心一会儿您拖不住里底娅小姐？还是说，在担心您的未来？
[name="赫卡德墨"]确实，虽然劫狱由我实施，但估计里底娅小姐之后也会知道，此事有您参与。
[name="赫卡德墨"]此后您任职的那家医药公司在雅赛努斯的办事处想要继续发展，说不定会受到一些阻挠......
[charslot(slot="l",name="avg_1022_flwr2_1#4$2",focus="l")]
[name="莱娜"]赞索斯和吕刻伊昂毕竟是我的病人——虽然某人不太听话，也不肯好好吃药，接受治疗。
[name="莱娜"]既然我已做好了准备，打算治病救人，从调香师成为一名专业的医生，那就不能放弃任何一位病人才是。
[name="莱娜"]有些事，无论代价是什么，该做的总得去做。
[name="莱娜"]我担心的其实是里底娅......无论如何，我需要与她好好谈谈。
[charslot(slot="l",name="avg_1022_flwr2_1#16$2",focus="l")]
[name="莱娜"]我的事不用担心，反而是你......
[charslot(slot="r",name="avg_npc_2070_1#6$1",focus="r")]
[name="赫卡德墨"]我也没什么可担心的，莱娜小姐。
[name="赫卡德墨"]我本来就对这份工作没什么留恋，没辞职也只是想看看有没有可能等到里底娅小姐开除我，给我赔偿金——
[charslot(slot="r",name="avg_npc_2070_1#1$1",focus="r")]
[name="赫卡德墨"]可惜计划落空了。这是我唯一的遗憾。
[charslot(slot="r",name="avg_npc_2070_1#6$1",focus="r")]
[name="赫卡德墨"]想到即将踏出这座移动城市，前往更广阔的天地，心里除了微微的忐忑之外，更多的是兴奋和激动。
[name="赫卡德墨"]莱娜小姐，我听说您也曾被迫离开雅赛努斯——这种心情，想必您也能够体会。
[charslot(slot="l",name="avg_1022_flwr2_1#9$2",focus="l")]
[name="莱娜"]......是啊。
[name="莱娜"]你们现在的情形，确实就和我那会儿差不多。
[charslot(slot="l",name="avg_1022_flwr2_1#1$2",focus="l")]
[multiline(name="莱娜")]你——
[charslot(slot="l",name="avg_1022_flwr2_1#7$2",focus="l")]
[multiline(name="莱娜")]你们，以后一定也会好起来的。
[name="莱娜"]就像我一样。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="58_g14_yanprison",screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_4166_varkis_1#10$2",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_4166_varkis_1#10$2",focus="m")]
[name="赞索斯"]我们必须想个办法离开这里。
[name="赞索斯"]不能再这么干等下去了。
[charslot(slot="m",name="avg_npc_2069_1#1$1",focus="m")]
[name="吕刻伊昂"]嗯，最好是能出去找莱娜小姐看看，您的身体——
[charslot(slot="m",name="avg_4166_varkis_1#1$2",focus="m")]
[name="赞索斯"]我的身体不重要。
[name="赞索斯"]文物交接仪式今天下午就会举行。
[name="赞索斯"]若是让萨尔贡人将三城建造时期的工程师手记带走，那日后，这段历史将只能任由他们粉饰。
[name="赞索斯"]必须想办法阻止这件事。
[charslot(slot="m",name="avg_npc_2076_1#1$1",focus="m")]
[name="伊萨科斯父亲"]先等等，赞索斯。
[name="伊萨科斯父亲"]你是矿石病人，我知道，在与萨尔贡人有摩擦的边境上，这些年里有许多像你这样因为战事而得病的人。
[charslot(slot="m",name="avg_4166_varkis_1#10$2",focus="m")]
[name="赞索斯"]......是。
[charslot(slot="m",name="avg_npc_2076_1#1$1",focus="m")]
[name="伊萨科斯父亲"]很多人流离失所，丧失了家园，他们过得非常辛苦，而你，来到雅赛努斯后，靠自己站稳了脚跟。
[name="伊萨科斯父亲"]你已经可以在这儿开启新的生活，为什么还要参与这样的事？
[charslot(slot="m",name="avg_4166_varkis_1#14$2",focus="m")]
[name="赞索斯"]......或许正因为我是矿石病人。
[charslot(slot="m",name="avg_4166_varkis_1#1$2",focus="m")]
[name="赞索斯"]我所剩无几的短暂生命，必须用来做一些在我看来更有意义的事。
[charslot(slot="m",name="avg_npc_2076_1#1$1",focus="m")]
[name="伊萨科斯父亲"]那你也是个被英雄梦束缚的米诺斯人。
[charslot(slot="m",name="avg_4166_varkis_1#1$2",focus="m")]
[name="赞索斯"]矿石病会隔绝英雄气概，自从离开故乡，英雄梦就已经离我很远了。我没有想过那些。
[charslot(slot="m",name="avg_npc_2076_1#1$1",focus="m")]
[name="伊萨科斯父亲"]是吗？
[name="伊萨科斯父亲"]没想到......
[name="伊萨科斯父亲"]伊萨科斯这小子，去边境还真是交了一个很好的朋友。
[charslot(slot="m",name="avg_4166_varkis_1#1$2",focus="m")]
[name="赞索斯"]......
[charslot(slot="m",name="avg_npc_2076_1#1$1",focus="m")]
[name="伊萨科斯父亲"]这里的守卫，十五分钟之后会换班，你们趁这个机会出去。
[name="伊萨科斯父亲"]出门后先往左走，在第二个岔口向右，再之后若是出现岔口都往右，只要能在五分钟的换班空当内出去，应该不会碰上守卫。
[name="伊萨科斯父亲"]最后你们会抵达后厨，现在这段时间，后厨应该没有人。你们可以从那里出去。
[charslot(slot="m",name="avg_4166_varkis_1#2$2",focus="m")]
[name="赞索斯"]......
[charslot(slot="m",name="avg_npc_2076_1#1$1",focus="m")]
[name="伊萨科斯父亲"]哦，对，还有脚镣。来，过来，我替你们打开。
[charslot(slot="m",name="avg_4166_varkis_1#2$2",focus="m")]
[name="赞索斯"]......为什么......
[charslot(slot="m",name="avg_npc_2076_1#1$1",focus="m")]
[name="伊萨科斯父亲"]为什么？我为什么不走？唔，我的情况和你们不太一样——在这死牢里，不仅有要处决的囚犯，还有些得被关到死的人，比如说我。
[na

... (全文21406字符)
```

### level_act48side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_courtyard",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Delay(time=1)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_181_flower_1#6$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_2067_1#8$2",duration=0.7)]
[delay(time=1)]
[charslot(slot="l",name="avg_181_flower_1#6$1",focus="l")]
[name="莱娜"]莱塔尼亚培育的细尾草是单叶还是复叶？
[charslot(slot="r",name="avg_npc_2067_1#8$2",focus="r")]
[name="里底娅"]不知道。
[charslot(slot="l",name="avg_181_flower_1#6$1",focus="l")]
[name="莱娜"]红锦葵的提炼方式有几种，哪种最能保留缓解精神疲劳的功效？
[charslot(slot="r",name="avg_npc_2067_1#8$2",focus="r")]
[name="里底娅"]不知道。
[charslot(slot="l",name="avg_181_flower_1#6$1",focus="l")]
[name="莱娜"]那你种下的这片波罗尼......
[charslot(slot="r",name="avg_npc_2067_1#8$2",focus="r")]
[name="里底娅"]我只帮你铲了土，莱娜姐姐。为什么种它，怎么种它，我一概不知道。
[charslot(slot="l",name="avg_181_flower_1#3$1",focus="l")]
[name="莱娜"]里底娅，这都是到时候要考你的东西。
[name="莱娜"]阿苏普欧洛家崇拜英雄芙罗拉，世代从事调香、草药制作、品种培育等与植物相关的工作。
[name="莱娜"]家族长辈对祖传的事业看得很重，等再过几年，你也要遵照传统参加家族继承人的选拔仪式，你得记下。
[charslot(slot="r",name="avg_npc_2067_1#8$2",focus="r")]
[name="里底娅"]谁都清楚阿苏普欧洛家的继承人只会是你。
[name="里底娅"]施特罗斯伯伯逢人便会提起他最骄傲的女儿，就差拉着他们的手说“莱娜就是阿苏普欧洛家的芙罗拉”了。
[charslot(slot="l",name="avg_181_flower_1#6$1",focus="l")]
[name="莱娜"]里底娅，我父亲对待你确实有失公平......
[charslot(slot="r",name="avg_npc_2067_1#1$2",focus="r")]
[name="里底娅"]他愿意收养父母早逝的我，已经是最大的仁慈。而且你知道，我对花花草草并没有兴趣。
[charslot(slot="l",name="avg_181_flower_1#6$1",focus="l")]
[name="莱娜"]唉，可下周我父亲安排了测试，要是你没有通过，又得受罚......
[charslot(slot="r",name="avg_npc_2067_1#1$2",focus="r")]
[name="里底娅"]我偷看了施特罗斯伯伯的记事本，百里香的收成没有达到预期，我猜这两天他就会动身，去科林尼亚找批可靠的货源来应急。
[charslot(slot="l",name="avg_181_flower_1#6$1",focus="l")]
[name="莱娜"]去科林尼亚？他没提起过啊——
[charslot(slot="l",name="avg_181_flower_1#6$1",focus="n")]
[name="施特罗斯"]莱娜，你怎么又蹲在花园里......我出趟远门，一周后回来，你照顾好自己和里底娅。
[charslot(slot="l",name="avg_181_flower_1#5$1",focus="l")]
[name="莱娜"]哇......
[charslot(slot="r",name="avg_npc_2067_1#1$2",focus="r")]
[name="里底娅"]就像你擅长辨认植物和调香，我也有自己擅长的东西，对吧？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_forest",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_openftstprun", volume=1, loop=true, channel="nrun")]
[StopSound(channel="nrun", fadetime=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_2067_1#5$2",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_2067_1#5$2",focus="m")]
[name="里底娅"]呼......呼......有人吗？有人吗！
[CameraShake(duration=0.7 ,xstrength=12, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="里底娅"]什么*米诺斯粗口*传统！阿苏普欧洛家偏要找个这么偏僻的地方进行继承人选拔仪式？
[name="里底娅"]采到稀有植株的候选人才最受英雄芙罗拉的青睐？简直荒谬！
[charslot(slot="m",name="avg_npc_2067_1#5$2",focus="m")]
[name="里底娅"]这里有人受伤了，我们需要医生......还有急性感染抑制剂！
[charslot(slot="m",name="avg_npc_2067_1#5$2",focus="n")]
[name="莱娜"]......里底娅，你的嗓子都喊哑了......背着我本来就很吃力，把我放下吧......
[charslot(slot="m",name="avg_npc_2067_1#9$2",focus="m")]
[name="里底娅"]你要是真想减轻我的负担，就把那棵重得要死的草扔了。就算没有它，你也是阿苏普欧洛家的继承人，至少在我心里，没人比你更合适。
[charslot(slot="m",name="avg_npc_2067_1#9$2",focus="n")]
[name="莱娜"]它对我而言确实已经没有意义了。
[name="莱娜"]阿苏普欧洛家的芙罗拉不能是个感染者，父亲不会接受，很有可能回去之后我就得离开雅赛努斯。
[charslot(slot="m",name="avg_npc_2067_1#8$2",focus="m")]
[name="里底娅"]如果他连自己的亲生女儿都能抛弃，那你根本不需要得到这种人渣的认可。
[charslot(slot="m",name="avg_npc_2067_1#8$2",focus="n")]
[name="莱娜"]但家族需要一位可靠的继承人。
[name="莱娜"]......
[name="莱娜"]里底娅，记下来，这株植物是紫草目，紫草科，琉璃草亚科，勿忘草属......
[charslot(slot="m",name="avg_npc_2067_1#9$2",focus="m")]
[name="里底娅"]什么意思......莱娜姐姐，不要告诉我这些，我不知道也不想知道！
[charslot(slot="m",name="avg_npc_2067_1#9$2",focus="n")]
[name="莱娜"]听我说完。
[name="莱娜"]这个品种在全泰拉范围内不算罕见，但根据目前的资料，它只生长于沼地附近，在米诺斯从未有人发现过。
[name="莱娜"]看到它的时候我想到了你。
[name="莱娜"]讨厌家族传统，对植物和草药毫无兴趣，最不像阿苏普欧洛的阿苏普欧洛......但我知道你擅长观察和沟通，你会是一位很好的继承人。
[charslot(slot="m",name="avg_npc_2067_1#9$2",focus="m")]
[name="里底娅"]那是你的位置，我不要......
[charslot(slot="m",name="avg_npc_2067_1#9$2",focus="n")]
[name="莱娜"]我们打个赌好吗？像小时候一样。
[name="莱娜"]请你暂时替我保管这株稀有植物，如果家族长老对我的病症并无意见，那我从此以后再也不会勉强你陪我去那座“无聊”的花园。
[name="莱娜"]但如果父亲对我的伤口露出厌恶的神情......你必须声称这棵“重得要死的草”是你找到的。
[name="莱娜"]放心吧，里底娅。成为继承人之后，不会再有人欺负你，哪怕是我的父亲。
[name="莱娜"]你会让阿苏普欧洛家变得更好，我相信。
[charslot(slot="m",name="avg_npc_2067_1#9$2",focus="m")]
[name="里底娅"]......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="69_g10_templegarden",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[delay(time=1)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_1022_flwr2_1#9$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_2067_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="l",name="avg_1022_flwr2_1#9$1",focus="l")]
[name="莱娜"]里底娅......
[charslot(slot="r",name="avg_npc_2067_1#1$1",focus="r")]
[name="里底娅"]为什么要约我在这座公共花园见面，我们之间就不用追忆往昔了吧？
[name="里底娅"]有什么话请你尽快说吧，我还有很多事情需要处理。
[name="里底娅"]文物交换仪式马上就要开始了，除了核对出席人员名单，保证仪式顺利进行，我还得——
[charslot(slot="l",name="avg_1022_flwr2_1#13$1",focus="l")]
[name="莱娜"]还得向所有雅赛努斯民众宣布，赞索斯先生和吕刻伊昂蓄意偷盗并损毁米诺斯的文化瑰宝，已经被判处叛国罪，是吗？
[charslot(slot="r",name="avg_npc_2067_1#8$1",focus="r")]
[name="里底娅"]......
[name="里底娅"]从调香师转行成为医生之后还不满足，现在又打算做辩护律师？
[name="里底娅"]如今是两国建交的关键时刻，作为理事官，我不可能任由一桩一时兴起的、荒唐的盗窃案毁了一切。
[charslot(slot="l",name="avg_1022_flwr2_1#14$1",focus="l")]
[name="莱娜"]持续百年的战争都没能毁去米诺斯，你在意的究竟是雅赛努斯民众的利益，还是自己理事官的头衔？
[charslot(slot="r",name="avg_npc_2067_1#7$1",focus="r")]
[name="里底娅"]俗套的道德选择题......
[charslot(slot="r",name="avg_npc_2067_1#1$1",focus="r")]
[name="里底娅"]我当然在意理事官的头衔。
[name="里底娅"]你以为罗德岛制药为什么能在这么短的时间内入驻雅赛努斯并设立办事处？
[name="里底娅"]捧着

... (全文28136字符)
```

### level_act48side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.15, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.15, fadetime=0.1)]
[Background(image="69_g8_templetheater",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avgnew_482_pallas_1#11$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avgnew_482_pallas_1#11$1",focus="m")]
[name="“克瑞斯拉”"]多么美好的时刻！暖风轻拂，特尔斐的河水在山间轻柔流淌。
[name="“克瑞斯拉”"]在废墟与乱石上，我们建起神殿，如今圣火熊熊燃烧，繁花与焚香的气息在风中缭绕。
[name="“克瑞斯拉”"]英雄的诗歌与传说让我们获得勇气，令我们聚集于此，聚集在这个美好的日子里——
[charslot(slot="m",name="avgnew_482_pallas_1#10$1",focus="m")]
[name="“克瑞斯拉”"]回想过去，贪婪的异邦人侵入我们的土地，奴役我们的身躯，让万物无法歌唱。
[name="“克瑞斯拉”"]但我们始终怀抱信念——异族无法统治我们坚韧的精神，更无法统治我们自由的灵魂。
[name="“克瑞斯拉”"]是我们，名为米诺斯的民族，凝聚在一起；我们的意志与信念，让我们取得了胜。
[charslot(slot="m",name="avgnew_482_pallas_1#7$1",focus="m")]
[name="“克瑞斯拉”"]现在，就让我们将那最后一个异邦人驱离我们的土地！
[Dialog]
[charslot]
在吟诵中，帕拉斯似乎透过克瑞斯拉的眼睛，见到了曾经的第一神殿，见到了那片群山环绕的花园。
克瑞斯拉的面前聚集着曾经流离失所的人们，就像在此时此刻，她的面前是观众席上或坐或站着的雅赛努斯公民。
所有人都屏息凝神，帕拉斯知道，他们在等待着最重要的时刻——
那能够宽慰所有米诺斯人的心灵，让大家知道漫长的黑夜与噩梦已经过去，神谕与英雄故事中的美好未来就在眼前的时刻。
[Dialog]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="m",name="avg_npc_2082_1#1$1",duration=0.5)]
[delay(time=0.7)]
[charslot(slot="m",name="avg_npc_2082_1#1$1",focus="m")]
[name="“阿加门士兵”"]最后一名异邦人已经送到。
[Dialog]
[charslot]
[delay(time=0.5)]
[PlaySound(key="$d_avg_walk_stage", volume=1, loop=true, channel="c")]
[StopSound(channel="c", fadetime=4)]
[charslot(slot="m",name="avg_4056_titi_1#2$2",duration=1)]
[delay(time=2)]
缇缇怀着忐忑，缓慢但坚定地踏上了舞台。
这是她自己选择的戏码，是她自己选择的角色。
她有必须要说的话、必须要念出的台词和必须做到的事。
[charslot(slot="m",name="avg_4056_titi_1#2$2",focus="m")]
[name="“异邦人”"]我为我们——我们的父辈与祖辈所做的一切而忏悔。
[name="“异邦人”"]出于贪婪与卑劣，出于恐惧与怯懦，我们主动或自以为被迫地，踏上了不应属于我们的土地。
[name="“异邦人”"]本应该养育家人的双手拆散了他人的家庭，本应该守护自己国度的长矛刺向了无辜的人群。
[charslot(slot="m",name="avg_4056_titi_1#11$2",focus="m")]
[name="“异邦人”"]我们所做过的一切......我们应该，也必须为之付出代价。
[Dialog]
[charslot(slot="m",name="avg_npc_2082_1#1$1",focus="m")]
[name="“阿加门士兵”"]您的匕首。
[charslot(slot="m",name="avgnew_482_pallas_1#1$1",focus="m")]
[name="“克瑞斯拉”"]......
[Dialog]
[stopmusic(fadetime=3)]
[charslot(duration=1)]
[delay(time=1.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_open_box", volume=0.7)]
[PlaySound(key="$d_avg_daggerexsheath", volume=1,delay=1)]
[delay(time=2)]
克瑞斯拉上前拿起了行刑用的匕首。
那是自从克瑞斯拉挂起她的竖琴之后，一直陪伴着她的武器。
经年累月的战斗让它磨损，原本锋利的刃上出现了缺口，但它的刀尖依然锋利，依然具备夺取生命的力量。
在克瑞斯拉的面前，异邦人顺从地舒展身体。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[curtain]
[image(image="69_i10",screenadapt="coverall",xScale=1.2,yScale=1.2,y=-70,block=true)]
[delay(time=0.5)]
[PlayMusic(key="$minos_folk_loop", volume=0.6)]
[ImageTween(yFrom=-70, yTo=70, duration=15, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[delay(time=2)]
音乐响起时，原本应当继续表演的帕拉斯动作似乎有些迟疑。
缇缇忽然想起，那名遮盖了面容的士兵，他的身形似乎有些陌生，动作也有些遮遮掩掩。
他是自己为这剧目挑选的演员吗？她突然有些不太确定。
剧场的舞台宽阔而空旷，让周围的观众显得距离极远。但缇缇依然能听到人群的鼓噪，他们是在为这戏码而激动吗？
[Dialog]
[Blocker(a=0.4, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="——“杀了她吧，让侵略者付出代价！”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
还是说，是在为她这个眼下就站在剧场中的萨尔贡人？
[Dialog]
[ImageTween(yFrom=70, yTo=0, xScaleFrom=1.2,yScaleFrom=1.2,xScaleTo=1,yScaleTo=1,duration=8, block=false)]
[delay(time=3)]
她抬起头，看着帕拉斯手中的匕首。那原本应该是橡胶质地的匕首尖端，在阳光下反射出了金属的光芒。
[name="“克瑞斯拉”"]......
[name="“克瑞斯拉”"]一切必须在此刻了结。
[name="“克瑞斯拉”"]唯有如此，我们才能取回挂在月桂树梢上的竖琴，纵饮美酒，重新回到滋养我们的群山与大地。
这出戏必须完成，她所能做的也只有相信，相信自己的朋友，相信米诺斯人的英雄气概。
缇缇闭上了眼睛。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2.5, block=true)]
[charslot]
[image]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[name="？？？"]多么肮脏的手段。
[name="？？？"]米诺斯人啊，你们还记得自己的矜持与骄傲吗？
[name="？？？"]你们最重要的英雄气概都去哪儿了？！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background(image="69_g8_templetheater",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
观众席陷入寂静。
在沉默中，人群渐渐分开，一个身影自人群中庄重而坚定地向舞台的中心走来。
他踏上舞台，将挡在自己与异邦人之间的阿加门士兵一脚踢开。
[Dialog]
[PlayMusic(intro="$minos_wardance_intro", key="$minos_wardance_loop", volume=0.6)]
[charslot(slot="m",name="avg_4166_varkis_1#7$1",duration=1.5)]
[delay(time=2)]
[name="赞索斯"]用一把替换了的匕首，制造一场仿佛是意外的血案，我们米诺斯人，是什么时候、从哪里学会的这种卑鄙的行径？
[Dialog]
[PlaySound(key="$d_avg_openftstpwalk", volume=1, loop=true, channel="walk1")]
[stopSound(channel="walk1", fadetime=3.5)]
[charslot(duration=1)]
[delay(time=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)] 
[charslot]
[charslot(slot="l",name="avg_npc_2078_1#1$1")]
[charslot(slot="r",name="avg_npc_2079_1#4$1")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_2078_1#10$1",focus="l")]
[name="佩里安德洛斯"]这才是我想看的戏码，总得有些我们料想不到的展开。
[name="佩里安德洛斯"]当然，若你刚才没忍住出手了，场面应该也会很有意思。
[charslot(slot="r",name="avg_npc_2079_1#4$1",focus="r")]
[name="西妮斯卡"]......雅赛努斯的事应该交给雅赛努斯人处理，即使没有这位......不知名的先生，也应该相信帕拉斯小姐。
[charslot(slot="r",name="avg_npc_2079_1#1$1",focus="r")]
[name="西妮斯卡"]我还是不够沉得住气，让你见笑了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)] 
[charslot]
[charslot(slot="l",name="av

... (全文11158字符)
```

### level_act48side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="69_g8_templetheater",screenadapt="coverall",xScale=1.3, yScale=1.3, block=true)]
[Delay(time=1)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_broadswordblood",volume=0.7)]
[CameraShake(duration=0.6, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=1,g=0.2, b=0.2, fadetime=0, block=true)]
[Blocker(a=0.4, r=1,g=0.2, b=0.2, fadetime=0.1, block=true)]
[Blocker(a=0, r=1,g=0.2, b=0.2, fadetime=0.6, block=true)]
[Delay(time=1)]
[name="赞索斯"]（很久没有体会到了，这种自己的身体里还有鲜血在流淌的感觉。）
[name="赞索斯"]（自从离开战场，离开故乡之后......）
[dialog]
[focusout(duration=1.5, type="bg", from=0, to=1, block=true)]
[delay(time=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=2.5, block=true)]
[Background(image="bg_black",screenadapt="coverall",block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=2, block=true)]
[delay(time=1)]
失血让他的视线模糊，眼前的一切变得朦胧、泛白。他不由得闭上了双眼。
[dialog]
[PlaySound(key="$d_avg_harp_normal_1",volume=0.7)]
[PlaySound(key="$d_avg_tinnitus", volume=1,delay=1.7)]
[delay(time=0.5)]
耳边似乎响起了竖琴声，他不知道是从哪儿传来的。
等他强撑着睁开眼睛，眼前的景象发生了改变。他的身体仿佛飘浮着，人们从他面前经过，却对他视若无睹。
他像是进入了某种幻象，或是另一个空间。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[focusout(duration=0.1, type="bg", from=1, to=0, block=true)]
[Background(image="bg_ibindoor",screenadapt="coverall", block=true)]
[CameraEffect(effect="Chaos",from = "chaos_none", to = "chaos_normal", fadetime =1, keep=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_2081_1#1$1",bstart=0.2,bend=0.7, focus="m")]
[CameraShake(duration=0.7, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="被俘的米诺斯人"]我是绝对不会跟萨尔贡人合作的！无论你们怎么审问我，拷打我，折磨我——
[name="被俘的米诺斯人"]也别想从我嘴里得到一点游击队的情报！
[Dialog]
[charslot]
[name="萨尔贡守卫"]你这么说，说明你们有游击队，否则你会直接说没有。
[charslot(slot = "m", name = "avg_npc_2081_1#1$1",bstart=0.2,bend=0.7, focus="m")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="被俘的米诺斯人"]......*米诺斯粗口*！
[Dialog]
[charslot]
[name="萨尔贡守卫"]你为什么这么生气？我以为你们米诺斯人会喜欢这样的思辨，我看过的英雄故事里都这么说。
[charslot(slot = "m", name = "avg_npc_2081_1#1$1",bstart=0.2,bend=0.7, focus="m")]
[name="被俘的米诺斯人"]你这是想跟我套近乎？我不会说的！
[Dialog]
[charslot]
[name="萨尔贡守卫"]......别太紧张，只是随便聊聊，我也不想审问你。
[name="萨尔贡守卫"]但要是不在这儿待够时间就出去会挨骂的，我也没有办法。
[charslot(slot = "m", name = "avg_npc_2081_1#1$1",bstart=0.2,bend=0.7, focus="m")]
[name="被俘的米诺斯人"]......
[Dialog]
[charslot]
[PlaySound(key="$d_gen_dooropen",volume=1)]
[Delay(time=1)]
[name="萨尔贡长官"]玛夏耶尔，你在做什么！连审问犯人这种小事都不会吗？！
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[Delay(time=0.5)]
[name="萨尔贡守卫"]哎呀！我正问着呢。
[name="萨尔贡长官"]真是废物。还贵族呢，呸！
[Dialog]
[charslot]
囚犯眼看着面前的守卫惊恐地从地上跳起，而他的长官就只是这么探头随意地骂了一句，之后便转身离开了。
那两人似乎都对这样的场景习以为常，就像长官在平日里曾千百次地骂过那名守卫，在他身上倾泻过恶意。
那名守卫长着一张年轻而苍白的脸，身材瘦弱，说话轻声细语，与村民印象中的萨尔贡人很不一样。
但决不能就这样掉以轻心，囚犯对自己说。
萨尔贡人都很卑鄙。说不定这是他们联合起来演的一场戏。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_ibindoor",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[name="萨尔贡守卫"]不管怎么样，我得做出在审问的样子......
[name="萨尔贡守卫"]能不能麻烦你......随便说一点什么？
[charslot(slot = "m", name = "avg_npc_2081_1#1$1",bstart=0.2,bend=0.7, focus="m")]
[name="被俘的米诺斯人"]随便说？那我可以不停歇地骂你。
[Dialog]
[charslot]
[name="萨尔贡守卫"]......说点儿别的吧。能让我们暂时忘记此刻的挣扎与不自由的，更美好的东西......能不能讲讲你们米诺斯的英雄故事？
[name="萨尔贡守卫"]我收藏了一些古书，知道一些你们的传说，但在萨尔贡要找到它们很不容易。
[charslot(slot = "m", name = "avg_npc_2081_1#1$1",bstart=0.2,bend=0.7, focus="m")]
[name="被俘的米诺斯人"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_ibindoor",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Dialog]
[charslot]
[name="萨尔贡守卫"]这个故事......你前天讲过了。我都记着呢。
[charslot(slot = "m", name = "avg_npc_2081_1#1$1",bstart=0.2,bend=0.7, focus="m")]
[name="被俘的米诺斯人"]啧。
[Dialog]
[charslot]
[name="萨尔贡守卫"]有没有新的？再想想！
[charslot(slot = "m", name = "avg_npc_2081_1#1$1",bstart=0.2,bend=0.7, focus="m")]
[name="被俘的米诺斯人"]（不是说我们装个样子骗过他的长官就好了吗？怎么还认真记录起来了。）
[name="被俘的米诺斯人"]（为什么会有这么喜欢米诺斯英雄传说的萨尔贡人？这家伙，脑子是不是有点问题？）
[Dialog]
[charslot]
[name="萨尔贡守卫"]我们才记了一百来个，米诺斯作为英雄之乡，传说故事应该不止这些才对？
[charslot(slot = "m", name = "avg_npc_2081_1#1$1",bstart=0.2,bend=0.7, focus="m")]
[name="被俘的米诺斯人"]（激我是吧。我会这么容易就上当吗？呸！）
[Dialog]
[charslot]
[name="萨尔贡守卫"]小时候随便听老人讲的只言片语也可以，不用很完整，也不用是大家都耳熟能详的故事。
[name="萨尔贡守卫"]再想想吧，能让萨尔贡的小女孩都对米诺斯心生向往的......肯定有，对吧？
[charslot(slot = "m", name = "avg_npc_2081_1#1$1",bstart=0.2,bend=0.7, focus="m")]
[name="被俘的米诺斯人"]（*米诺斯粗口*这家伙都这么说了......）
[name="被俘的米诺斯人"]（啧。瞎编算了，反正*米诺斯粗口*萨尔贡人也分不清。）
[name="被俘的米诺斯人"]行，那我给你讲个沉默的英雄西尔比的故事吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[CameraEffect(effect="Chaos", fadetime=0, amount=0, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
这绝对是囚犯人生中最奇怪的一段经历。说出去也不会有人信，他决定将这件事烂在自己肚子里——
只要他能平安地从这里离开。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_ibindoor",screenadapt="coverall", block=true)]
[CameraEffect(effect="Chaos",from = "chaos_none", to = "chaos_normal", fadetime =0.5, keep=true)]
[charslot(slot = "m", name = "avg_npc_2081_1#1$1",bstart=0.2,be

... (全文22018字符)
```

### level_act48side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, duration=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_black",screenadapt="coverall")]
[PlayMusic(key="$minos_lyresolo_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, duration=1, block=true)]
[Delay(time=2)]
[Sticker(id="st1", multi = true, text="于是阿加门最温柔的英雄，史诗的吟唱者克瑞斯拉，", x=180,y=170, alignment="left", size=24, delay=0.0001, width=700,duration=1.3,block = true)]
[Sticker(id="st2", multi = true, text="            将她的竖琴挂在月桂的树梢上；那把琴——", x=180,y=220, alignment="left", size=24, delay=0.0001, width=700,duration=1.3,block = true)]
[Sticker(id="st3", multi = true, text="它的琴身来自荷谟伊高山中耸立的杉树，它的琴弦取自阿涅斯平原上勇猛驮兽的肚肠；", x=180,y=270, alignment="left", size=24, delay=0.0001, width=1000,duration=1.3,block = true)]
[Sticker(id="st4", multi = true, text="            当它鸣响，万物便在英雄的国度歌唱，自由地，飘向远方。", x=180,y=320, alignment="left", size=24, delay=0.0001, width=700,duration=1.3,block = true)]
[Sticker(id="st5", multi = true, text="而现在，克瑞斯拉将她的竖琴挂在了月桂梢旁。", x=180,y=370, alignment="left", size=24, delay=0.0001, width=700,duration=1.3,block = true)]
[Sticker(id="st1",duration=1.3)]
[Sticker(id="st2",duration=1.3)]
[Sticker(id="st3",duration=1.3)]
[Sticker(id="st4",duration=1.3)]
[Sticker(id="st5",duration=1.3)]
[Delay(time=2)]
[Sticker(id="st1", multi = true, text="“异邦人自远方来，”克瑞斯拉握紧了她的匕首，开口回答道，", x=180,y=170, alignment="left", size=24, delay=0.0001, width=700,duration=1.3,block = true)]
[Sticker(id="st2", multi = true, text="“践踏我们的土地，焚烧我们的家园，让河流不再悠远流淌；他们还", x=180,y=220, alignment="left", size=24, delay=0.0001, width=900,duration=1.3,block = true)]
[Sticker(id="st3", multi = true, text="            命令万物为他们歌唱。不！单这最后一样，", x=180,y=270, alignment="left", size=24, delay=0.0001, width=700,duration=1.3,block = true)]
[Sticker(id="st4", multi = true, text="            便让我揪紧肚肠。", x=180,y=320, alignment="left", size=24, delay=0.0001, width=700,duration=1.3,block = true)]
[Sticker(id="st5", multi = true, text="我的琴声，只为英雄的故事而响！”", x=180,y=370, alignment="left", size=24, delay=0.0001, width=700,duration=1.3,block = true)]
[Sticker(id="st6", multi = true, text="——《克瑞斯拉纪》", x=880,y=450, alignment="left", size=24, delay=0.0001, width=700,duration=1.3,block = true)]
[Sticker(id="st1",duration=1.3)]
[Sticker(id="st2",duration=1.3)]
[Sticker(id="st3",duration=1.3)]
[Sticker(id="st4",duration=1.3)]
[Sticker(id="st5",duration=1.3)]
[Sticker(id="st6",duration=1.3)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_forest",screenadapt="coverall", block=true)]
[delay(time=2)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="兴奋的声音"]“虽然史料中没有确切的记载，但学界普遍认为，在萨尔贡为米诺斯建造的三大移动城市中，玛拉帕夏最偏爱的是雅赛努斯。”
[name="兴奋的声音"]“将它整体搬迁至移动平台上时，萨尔贡与米诺斯的技术人员花费了极大的心力，才保留了它‘四面环山的花园’这一著名的特征。”
[name="兴奋的声音"]“如今的游客若是从玛拉帕夏特地保留的山口进入雅赛努斯，所见的群山与河流，便与克瑞斯拉初到此地时别无二致。”
[name="兴奋的声音"]“这是笔者十分推荐的路线，建议所有读者都——”
[name="暴躁的声音"]闭嘴吧！看看你那本破书都把我们带到了什么破路上！
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_npc_1482_1#1$1",duration=1)]
[charslot(slot="r",name="avg_4056_titi_1#1$1",duration=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_1482_1#4$1",focus="l")]
[name="米奥"]还要搬这玩意儿！又大又重，麻烦得要死！就我们两个！
[Dialog]
[PlaySound(key="$d_avg_strikeharp")]
[Delay(time=1)]
[PlaySound(key="$d_avg_strikeharp")]
[Delay(time=1)]
[PlaySound(key="$d_avg_strikeharp")]
[Delay(time=1)]
[charslot(slot="r",name="avg_4056_titi_1#5$1",focus="r")]
[name="缇缇"]哎呀，轻点儿，别敲，别敲了！
[name="缇缇"]连着走了几天的路，本来就已经腰酸背痛口干舌燥了......
[charslot(slot="l",name="avg_npc_1482_1#5$1",focus="l")]
[name="米奥"]还好意思说！
[name="米奥"]我问你，为什么要脱离大部队？要不是你心血来潮瞎跑，这会儿我早就躺在雅赛努斯的花田里畅饮花香精酿了！
[charslot(slot="r",name="avg_4056_titi_1#1$1",focus="r")]
[name="缇缇"]这可不是心血来潮。
[charslot(slot="r",name="avg_4056_titi_1#10$1",focus="r")]
[name="缇缇"]我跟你说过的，从小时候父亲给我讲故事，让我知道阿涅斯河的对岸，有一个叫米诺斯的地方开始，我就......
[charslot(slot="r",name="avg_4056_titi_1#9$1",focus="r")]
[name="缇缇"]出发的时候我也说了，出使米诺斯可是难得的机会，我想沿着古道，踏着克瑞斯拉当年的足迹去雅赛努斯，重走一遍历史——
[charslot(slot="l",name="avg_npc_1482_1#4$1",focus="l")]
[name="米奥"]你重走历史的时候，能不能别带着这个百斤重的玩意！就我俩搬，累死了！干嘛，负重请罪啊？
[charslot(slot="r",name="avg_4056_titi_1#5$1",focus="r")]
[name="缇缇"]负“荆”请罪，你别瞎改炎国成语......
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]你是不是心眼都被历史书堵死了？这是重点吗？
[Dialog]
[charslot(slot="l",name="avg_npc_1482_1#4$1",focus="l")]
[PlaySound(key="$d_avg_strikeharp")]
[Delay(time=1)]
[PlaySound(key="$d_avg_strikeharp")]
[Delay(time=1)]
[charslot(slot="r",name="avg_4056_titi_1#9$1",focus="r")]
[name="缇缇"]好了好了，别敲了，交给其他人我不放心嘛。
[name="缇缇"]这可是法尔贾万达巴德博物馆最珍贵的馆藏，是对萨尔贡和米诺斯两国都至关重要的文物，我们大老远跑过来......
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]就是为了把它交还给米诺斯人，增进两国在新时代的友谊——原来你还记得自己的任务啊！
[charslot(slot="l",name="avg_npc_1482_1#4$1",focus="l")]
[name="米奥"]萨尔贡使节团的老大，梅捷缇克缇-娜苏图-玛夏耶尔女士，你迷路了！迟到了！错过了和雅赛努斯的理事官约定的会面时间！
[charslot(slot="r",name="avg_4056_titi_1#11$1",focus="r")]
[name="缇缇"]呜......大部队走常规出入口，现在应该已经进城了，贝赫努先生会帮我向理事官好好解释的。
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]贝赫努......那个趾高气扬的贵族？你是真傻还是假傻？
[name="米奥"]你难道没注意到，那家伙听说自己在使节团里只是给你当副手后，看你的眼神吗？就跟你偷了他五十车赤金一样。
[charslot(slot="r",name="avg_4056_titi_1#5$1",focus="r")]
[name="缇缇"]不、不会的，贝赫努先生人很好。
[name="缇缇"]我才刚当上博物馆馆长，就接到这么重要的任务，我其实......总之，贝赫努先生一路上帮了我很多。
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]算了，随你，反正我只是跟过来旅游的。
[name="米奥"]快点走吧，不然真的要一点力气都没有了。
[charslot(slot="r",name="avg_4056_titi_1#9$1",focus="r")]
[name="缇缇"]好了好了，这不是已经到了嘛。
[name="缇缇"]看前面——
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image(image="69_i01", xScale=1, yScale=1,x=100,y=-50, fadetime=0)]
[ImageTween(xTo=0,yTo=0, duration=45,xScaleFrom=1, yScaleFrom=1, xScaleTo=0.8, yScaleto=0.8,block=false)]
[delay(time=2)]
[PlayMusic(key="$

... (全文25589字符)
```

### level_act48side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="69_g3_pasture_n",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_2068_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_2068_1#1$1",focus="m")]
[name="卡珊卓拉"]在这里的，才是真正的克瑞斯拉竖琴。
[Dialog]
[charslot]
恩底弥翁的祭司伸手拂过驮兽牧场一角的篱笆，拔去了几根过长的牧草，让修筑在篱笆中的竖琴露了出来。
古朴的乐器几乎已与牧场融为一体，不远处，驮兽们悠闲地啃着祭司带来的萝卜，时不时发出满意的哼声。
[Dialog]
[charslot(slot="l",name="avg_4056_titi_1#5$1",focus="l")]
[charslot(slot="r",name="avg_npc_2068_1#1$1",focus="l")]
[name="缇缇"]......但它的色彩黯淡，底座涂漆斑驳，装饰虽然都在，上面却留有驮兽啃咬和磨蹄子的痕迹，整体看上去只是这家牧场一角的装饰品。
[name="缇缇"]虽然我不该质疑您......但这......我很难相信......
[charslot(slot="r",name="avg_npc_2068_1#1$1",focus="r")]
[name="卡珊卓拉"]你是这方面的专家，你们有一整套的鉴定方法和确认标准，你可以仔细查看。
[charslot(slot="l",name="avg_4056_titi_1#5$1",focus="l")]
[name="缇缇"]这么说的话，琴身用的确实是那个时代在旧雅赛努斯城附近生长的杉树，对比来看，它的造型也比我带来的那把琴更古朴自然。
[name="缇缇"]只是这弦太新了，这是近些年来才流行的金属弦......
[charslot(slot="r",name="avg_npc_2068_1#6$1",focus="r")]
[name="卡珊卓拉"]原本的琴弦早已断裂，现在用的是我近来换上的。
[name="卡珊卓拉"]我也试过传统的兽肠弦，但......无论用哪一种，结果都是一样。
[name="卡珊卓拉"]如传说所述，雅赛努斯旧城沦陷之日，克瑞斯拉的竖琴陷入了沉默，再也无法发出任何声音。
[name="卡珊卓拉"]金属弦也好，兽肠弦也罢，每个月我都会固定来到此地尝试弹奏，却一次也无法让它成为真正的乐器。
[charslot(slot="l",name="avg_4056_titi_1#10$1",focus="l")]
[multiline(name="缇缇")]......但再怎么说，它毕竟是克瑞斯拉用过的竖琴——
[charslot(slot="l",name="avg_4056_titi_1#1$1",focus="l")]
[multiline(name="缇缇")]假如您所说的一切是真的。
[name="缇缇"]如今已不再是萨尔贡人占据米诺斯的时代，不再需要让它隐于乡野来保护它。
[name="缇缇"]那为什么，之前我提出可以在第一神殿举行仪式时，不，再往前，理事官与我们约定要交换这件文物时——您是祭司，应该知道这件事。
[charslot(slot="l",name="avg_4056_titi_1#5$1",focus="l")]
[name="缇缇"]那时候，为什么您不把它拿出来呢？
[charslot(slot="r",name="avg_npc_2068_1#1$1",focus="r")]
[name="卡珊卓拉"]无法鸣响的竖琴只是几段漂亮的木头。
[name="卡珊卓拉"]它可以成为牧场的篱笆，成为驮兽的玩具，唯独不能成为......一座神殿落成的祭祀仪式上将所有人凝聚到一起的契机。
[charslot(slot="l",name="avg_4056_titi_1#5$1",focus="l")]
[name="缇缇"]......这不合常理。即使是我们带来的那件赝品，也可以弹出动人的音色。
[charslot(slot="r",name="avg_npc_2068_1#1$1",focus="r")]
[name="卡珊卓拉"]所以它只是赝品。至于眼前的竖琴，你若是不信我所说，一试便知。
[charslot(slot="l",name="avg_4056_titi_1#5$1",focus="l")]
[name="缇缇"]......
[charslot(slot="r",name="avg_npc_2068_1#3$1",focus="r")]
[name="卡珊卓拉"]你可以上手，不必客气。我完全理解你的疑虑。
[name="卡珊卓拉"]假如你能够奏响它......假如你能够为我们带来一个神迹，那么，你就可以将它当作你带来的琴，完成你需要完成的交易。
[name="卡珊卓拉"]我作为这把琴如今的保管者，可以向你承诺这一点。
[charslot(slot="l",name="avg_4056_titi_1#5$1",focus="l")]
[name="缇缇"]......我......很抱歉，我还得再多问一句——为什么是我？虽然我确实很需要这把真琴，第一神殿也需要它......
[charslot(slot="r",name="avg_npc_2068_1#9$1",focus="r")]
[name="卡珊卓拉"]梅捷缇克缇小姐，我是恩底弥翁神殿的祭司。
[name="卡珊卓拉"]我们作为神谕的祭司，会替市民们阐释梦境，解读神谕，揭示未来。
[name="卡珊卓拉"]有时候，我们能主动提供一些慰藉，但大多数时候，我们只会被动地遵从一些既定的事实和英雄的意志。
[name="卡珊卓拉"]言语自我的唇上流泻，并不受我控制，正如常常会出现在我双眼中的画面，未必是我乐见。
[name="卡珊卓拉"]我们可能会将巧合称为命运，但当真正的命运来临之际，所有的巧言令色都会失去意义。
[name="卡珊卓拉"]难道我能容许太阳照耀，能够允准河水流淌，自高到低？
[name="卡珊卓拉"]你带着克瑞斯拉的竖琴——即使它是仿制品——出现在雅赛努斯，这件事本身就是一种预兆，这几日发生的事已印证了这一点。
[charslot(slot="r",name="avg_npc_2068_1#7$1",focus="r")]
[name="卡珊卓拉"]但最重要的，是你身上具备的品质......正因为是你，而不是你那位同胞，我才能期待竖琴能与你的精神发生共鸣。
[charslot(slot="l",name="avg_4056_titi_1#5$1",focus="l")]
[name="缇缇"]......我......
[charslot(slot="r",name="avg_npc_2068_1#3$1",focus="r")]
[name="卡珊卓拉"]先试试给这把琴唱些英雄的赞歌吧，试试弹奏它，将你的心交给它，与它对话。
[name="卡珊卓拉"]然后，或许，你真的能够让它发出声音，让它显现神迹。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="69_g3_pasture_n",screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1482_1#1$1",focus="m")]
[name="米奥"]总算走了......神神秘秘的......
[charslot(slot="m",name="avg_4056_titi_1#10$1",focus="m")]
[name="缇缇"]......
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1482_1#1$1",focus="m")]
[name="米奥"]咋了？这就坐下开始准备弹琴了？你还真信？
[Dialog]
[charslot]
[name="缇缇"]她是米诺斯的祭司，是帕拉斯小姐的朋友，不至于在这件事上欺骗我。
[name="缇缇"]而且......若是能拿着真琴去完成第一神殿的仪式......这确实是一个比背着假琴满泰拉逃窜更好的选择。
[name="缇缇"]无论是祭司口中所谓的“真正的命运”也好，或者其实是米诺斯人的某种考验也罢，我总得先试试。
[charslot(slot="m",name="avg_npc_1482_1#4$1",focus="m")]
[name="米奥"]咋试啊？她说的那些，什么把心交给它，什么展现神迹，这怎么做得到嘛。
[Dialog]
[charslot]
[name="缇缇"]......总之，先弹弹看吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="69_g3_pasture_n",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_harp_unpleasant", volume=1)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_1482_1#4$1",duration=0.7)]
[charslot(slot="r",name="avg_4056_titi_1#11$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_1482_1#4$1",focus="l")]
[PlaySound(key="$d_avg_meowlong", volume=1)]
[delay(time=0.5)]
[name="米奥"]太难听了！
[Effect(name="$e_emoji_matter",layer = 1,x=250,y=150)]
[charslot(slot="r",name="avg_4056_titi_1#11$1",focus="r")]
[name="缇缇"]不行，怎么弹都只能发出这种闷闷的声响。
[charslot(slot="r",name="avg_4056_titi_1#5$1",focus="r")]
[name="缇缇"]......是琴的结构受损导致的吗？但这种手持的竖琴没有共鸣箱......应该不是这方面的问题。
[name="缇缇"]也调整了琴弦的松紧度，但没什么效果。难道是某个精细的内部构件出现了问题？可是这里没有工具，没法把琴拆开检查后复原回去。
[charslot(slot="r",name="avg_4056_titi_1#11$1",focus="r")]
[name="缇缇"]唉......
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]好麻烦。
[name="米奥"]我说，要不我们还是回去偷那把假琴吧，大不了我帮你去偷就是了。
[charslot(slot="l",name="avg_npc_1482_1#2$1",focus="l")]
[name="米奥"]偷完了也未必非得浪迹天涯......唔，要浪迹天涯也行，我们可以先去找佩佩那丫头要点儿跑路的资金。
[charslot(slot="r",name="avg_4056_titi_1#11$1",focus="r")]
[name="缇缇"]......
[name="缇缇"]但有真琴在我面前，再做那样的选择就像是在逃跑了。
[charslot(slot="l",name="avg_npc_1482_1#1$1",focus="l")]
[name="米奥"]啧。你要是很在意，我们也可以叫它战略转移。
[charslot(slot="r",name="avg_4056_titi_1#10$1",focus="r")]
[name="缇缇"]但从小......父亲给我讲的那些英雄故事里，英雄不会逃避。
[Dialog]
[Blocker(a=0, r=0, g=0, b=

... (全文12278字符)
```

### level_act48side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="69_g10_templegarden",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_1022_flwr2_1#1$2",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_1022_flwr2_1#1$2",focus="m")]
[name="莱娜"]喏，这是需要定期服用的药物和抑制剂，我都从罗德岛办事处带过来了。
[name="莱娜"]听说理事官办公室已经撤销了对赞索斯师徒的囚禁命令，也不打算追究你协助他们逃狱的事。
[charslot(slot="m",name="avg_npc_2070_1#2$1",focus="m")]
[name="赫卡德墨"]是的。我后来才知道，里底娅小姐早猜到了我们的计划，当时就给我大开方便之门，事后自然也不会追究。
[charslot(slot="m",name="avg_1022_flwr2_1#9$2",focus="m")]
[name="莱娜"]......
[charslot(slot="m",name="avg_1022_flwr2_1#16$2",focus="m")]
[name="莱娜"]即使如此，你们也还是打算离开雅赛努斯，去其他地方游历？
[charslot(slot="m",name="avg_npc_2070_1#2$1",focus="m")]
[name="赫卡德墨"]没错。
[name="赫卡德墨"]待在这里只会让我的老同学胡思乱想，还不如出去走走，跟更多的人交谈，做更多的事。
[charslot(slot="m",name="avg_npc_2069_1#1$1",focus="m")]
[name="吕刻伊昂"]没错。
[charslot(slot="m",name="avg_1022_flwr2_1#2$2",focus="m")]
[name="莱娜"]哦？很少见你如此坦诚啊，吕刻伊昂。要是你做我病人的时候能这么老实，我就不需要派三名罗德岛干员盯着你了。
[charslot(slot="m",name="avg_npc_2069_1#4$1",focus="m")]
[name="吕刻伊昂"]抱歉，之前给您添麻烦了......
[charslot(slot="m",name="avg_npc_2070_1#2$1",focus="m")]
[name="赫卡德墨"]看来赞索斯先生在第一神殿的行为，给你带来了不小的影响。
[charslot(slot="m",name="avg_npc_2070_1#7$1",focus="m")]
[name="赫卡德墨"]怎么样，要不要直接承认矿石病根本不会隔绝英雄气概，向我投降认输？
[charslot(slot="m",name="avg_npc_2069_1#8$1",focus="m")]
[name="吕刻伊昂"]做梦。
[charslot(slot="m",name="avg_npc_2070_1#6$1",focus="m")]
[name="赫卡德墨"]啧，嘴跟石头一样硬。
[charslot(slot="m",name="avg_1022_flwr2_1#7$2",focus="m")]
[name="莱娜"]快出发吧，再晚可就赶不上渡口的船了，代理的摆渡人没有赞索斯先生那么好心，要是误了时间，他可不会等你们。
[charslot(slot="m",name="avg_npc_2070_1#4$1",focus="m")]
[multiline(name="赫卡德墨")]糟了，吕刻伊昂，我们快走......
[charslot(slot="m",name="avg_npc_2070_1#2$1",focus="m")]
[multiline(name="赫卡德墨")]多谢莱娜小姐的药，我们以后再见！
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[charslot(duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_2069_1#1$1",focus="m")]
[delay(time=0.3)]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_1022_flwr2_1#15$2",focus="m")]
[name="莱娜"]哎，别从草坪那边走啊，我刚整理完——
[charslot(slot="m",name="avg_1022_flwr2_1#9$2",focus="m")]
[multiline(name="莱娜")]算了，这两个年轻人的破坏力哪有几十只驮兽来得厉害呢？
[charslot(slot="m",name="avg_1022_flwr2_1#10$2",focus="m")]
[multiline(name="莱娜")]它们踩坏的花卉和草皮都还没清理呢，可惜了那些淡蓝色的波罗尼......
[Dialog]
[musicvolume(volume=0.3, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_courtyard",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[name="小里底娅"]呜......呜......
[name="小莱娜"]别哭了，里底娅......
[name="小里底娅"]如果有一天你和施特罗斯伯伯住的地方，也像我原来的家那样，被别人砸坏了......
[name="小里底娅"]那我和你就都没有家可以回了呀，这该怎么办......
[name="小莱娜"]放心吧，就算没了这幢房子，就算我们走散了，我也绝对不会丢下你的！
[name="小莱娜"]对了！如果你离家太远，担心自己找不到回家的路，那你就找这片花圃。
[name="小里底娅"]花......花圃......？
[name="小莱娜"]嗯，我会在里面种满淡蓝色的波罗尼，你只要看到它们，就知道自己回家了。
[name="小莱娜"]同样的，如果你先找到了路，你也用同样的办法为我指路，好吗？
[name="小里底娅"]好......莱娜姐姐，我们说定了......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="69_g10_templegarden",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[delay(time=0.5)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
公共花园的草坪曾经种满花朵和香草，如今只剩下驮兽群踩出的凌乱脚印。
不过，即使花园暂时失去往日绚烂迷人的风貌，留下一片狼藉，那些蓝色的花瓣依旧在这片土地里。
[charslot(slot="m",name="avg_1022_flwr2_1#1$2",focus="m")]
[name="莱娜"]这么一大片，淡蓝色的波罗尼......你也在怀念从前，不是吗？
[charslot(slot="m",name="avg_1022_flwr2_1#7$2",focus="m")]
[name="莱娜"]谢谢你，里底娅。我回家了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="69_g11_firsttemple_indoor",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_2086_1#1$1",focus="m")]
[name="果农代表"]卡珊卓拉小姐，我来送今年份的苹果了！
[name="果农代表"]留给神殿做供品的那份已经送到楼下的仓库里了，这些是我特地留下来的，给您和神殿的大家尝尝鲜。
[charslot(slot="m",name="avg_npc_2068_1#3$2",focus="m")]
[name="卡珊卓拉"]谢谢，每年都麻烦您费心。
[charslot(slot="m",name="avg_npc_2086_1#1$1",focus="m")]
[name="果农代表"]我们能顺利收获，都仰赖雅赛努斯的大家帮助，还有神殿的协调安排，是我该说麻烦您了才对。
[charslot(slot="m",name="avg_npc_2068_1#3$2",focus="m")]
[name="卡珊卓拉"]您今天精神不错。
[charslot(slot="m",name="avg_npc_2086_1#1$1",focus="m")]
[name="果农代表"]嘿，我们果农关心的也就是收成，丰收能给人带来满足嘛。
[charslot(slot="m",name="avg_npc_2068_1#7$2",focus="m")]
[name="卡珊卓拉"]嗯，我们神殿关心的则是大家的精神，丰收确实是其中很重要的一环。
[charslot(slot="m",name="avg_npc_2086_1#1$1",focus="m")]
[name="果农代表"]那以后还要继续麻烦您了！我就先不打扰啦，接下来就得迎接石榴的收获季了，今天还有不少修剪枝条的活儿没干完呢。
[Dialog]
[PlaySound(key="$d_avg_walkfast", volume=0.7)]
[charslot(duration=1)]
[Delay(time=1.5)]
[PlaySound(key="$d_gen_dooropen", volume=0.7)]
[Delay(time=2)]
[charslot(slot="m",name="avgnew_482_pallas_1#22$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avgnew_482_pallas_1#22$1",focus="m")]
[name="帕拉斯"]苹果芬芳，阳光明亮，多么美好的一天！
[name="帕拉斯"]第一神殿的仪式顺利完成，雅赛努斯迎来丰收，你照拂的摆渡人先生也振作了起来。
[charslot(slot="m",name="avgnew_482_pallas_1#11$1",focus="m")]
[name="帕拉斯"]关心大家精神的祭司啊，明明一切都好，聪慧的你为何还如此忧心忡忡？
[charslot(slot="m",name="avg_npc_2068_1#6$2",focus="m")]
[name="卡珊卓拉"]......我担心的是你。
[charslot(slot="m",name="avgnew_482_pallas_1#9$1",focus="m")]
[name="帕拉斯"]我？为什么？
[charslot(slot="m",name="avg_npc_2068_1#4$2",focus="m")]
[name="卡珊卓拉"]这几日，我一直在想你当初回到雅赛努斯时说的话。
[charslot(slot="m",name="avgnew_482_pallas_1#20$1",focus="m")]
[name="帕拉斯"]......
[charslot(slot="m",name="avg_npc_2068_1#4$2",focus="m")]
[name="卡珊卓拉"]你说你在梦中看到了米诺斯的起点，看到了克瑞斯拉与她的第一神殿。
[name="卡珊卓拉"]你也说你思考了许多，关于米诺斯的曾经和未来，关于你自己的目标和方向。
[cha

... (全文19207字符)
```

### ref_act48side

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 

[Image(image="69_i04_a",screenadapt="coverall", fadetime=0)]

```

### training_act48side_01_a

```
[header(is_tutorial=true)]training_act48side_01_a
[battle.pause]
[inputblocker(blockInput=true, black=0.3)]
[popupdialog(dialogHead="$avatar_pallas")]欢迎来到雅赛努斯！这座城市会善待这片大地上的每一位客人。
[popupdialog(dialogHead="$avatar_pallas")]米诺斯的公民们热爱戏剧，在街道上也会随时表演英雄的传说故事。
[popupdialog(dialogHead="$avatar_pallas")]他们可能会过于热情，但要是你们有兴趣，也可以加入共演。
[popupdialog(dialogHead="$avatar_melan")]我......我也要一起演吗？
[end]
```

### training_act48side_01_b

```
[header(is_tutorial=true)]training_act48side_01_b
[battle.pause]
[popupdialog(dialogHead="$avatar_melan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]手脚......不知道该往哪儿放......施放技能需要的技力似乎也提高了......
[tutorial(focusWidth=120, focusHeight=120, animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", protectTime=2, dialogHead="$avatar_pallas", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=4, tileX=6)]是因为“拘谨”吧，还不习惯街头戏剧的氛围。那试试填满这些缀花喷泉的水池，让水中的花香来帮助大家习惯吧。
[popupdialog(dialogHead="$avatar_hibisc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]通过治疗来激活可用水流，补充水池中的水量吗？好精巧的公共装置，让我来试一试！
[end]
```

### training_act48side_01_c

```
[header(is_tutorial=true)]training_act48side_01_c
[battle.pause]
[popupdialog(dialogHead="$avatar_pallas", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", focusX=-225, focusY=259, focusWidth=120, focusHeight=72, animStyle="Highlight", focusStyle="HighlightCircle", anchor="TopRight", black="$f_tut_black", protectTime=0.5)]水量超过一半时，水会缓慢地向水位更低的相邻水池流淌。
[tutorial(animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", protectTime=0.5, dialogHead="$avatar_pallas", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=3, tileX=1)]除治疗之外，也可以去找负责维护缀花喷泉的祭司学徒来灌满水池。
[tutorial(focusStyle="HighlightCircle", dialogHead="$avatar_pallas", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=3, tileX=1)]不过他们有自己的工作安排，要他们帮忙的话......可能得用上一些手段。
[end]
```

### training_act48side_01_d

```
[header(is_tutorial=true)]training_act48side_01_d
[battle.pause]
[tutorial(animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", dialogHead="$avatar_pallas", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=4, tileX=3)]相连的所有水池灌满后，相邻的地块会进入“花香弥散”状态。
[tutorial(animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", dialogHead="$avatar_pallas", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=4, tileX=3)]这些地块上的干员和敌人会“入戏”，离开相应地块后“入戏”状态也会短暂持续。
[popupdialog(dialogHead="$avatar_pallas", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]“入戏”状态的敌人会降低攻击命中率和移动速度，部分敌人还会受到特殊的影响。
[popupdialog(dialogHead="$avatar_pallas", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]而“入戏”状态的干员会快速回复技力，请尽情享受米诺斯的芬芳与英雄故事吧！
[end]
```

### training_act48side_01_e

```
[header(is_skippable=true, is_autoable=true, is_tutorial=true)]training_act48side_01_e
[battle.pause]
[tutorial(animStyle="Highlight", focusStyle="HighlightCircle", dialogHead="$avatar_hibisc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=3, tileX=4)]是充盈的感觉......咦，那边的石柱柱头，它好像在飞！
[popupdialog(dialogHead="$avatar_pallas", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]啊，看来你完全沉浸在雅赛努斯的花香之中了。
[tutorial(animStyle="Highlight", focusStyle="HighlightCircle", dialogHead="$avatar_pallas", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=3, tileX=4)]干员左下方的进度标识满后，眼前会出现一些幻象，只有“入戏”状态的干员可以攻击它们。
[popupdialog(dialogHead="$avatar_pallas", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]别担心，只是一些想象。只要大家意志坚定，就不会受到伤害。
[end]
```


## 统计

- 总字符数：322250
- 对话行数：2451


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
