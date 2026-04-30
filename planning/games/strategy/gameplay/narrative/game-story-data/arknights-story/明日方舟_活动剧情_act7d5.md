# 明日方舟 · 活动剧情 · act7d5（6段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act7d5」完整剧情脚本（6个文件，1976行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act7d5
- 脚本文件数：6

### level_act7d5_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1,block=true)]
[character]
[Delay(time=0.5)]
[Background(image="bg_trainingcom",screenadapt="coverall")]
[Blocker(a=0, fadetime=3, block=true)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
04:22 P.M.  天气/晴
罗德岛舰船，第五舱室，训练场
[name="香草"]     喝！哈啊！
[name="香草"]     劈砍！直刺！平挥！
[name="香草"]     呼......哈......
[Dialog]
[Character(name="char_240_Vanilla_1#6",fadetime=1,blok=true)]
[Delay(time=1)]
[name="香草"]     今天的......体能训练......呼，呼，终于完成了。
[Decision(options="注意极限，你对自己太严格了。;......;给，运动饮料。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_240_Vanilla_1")]
[name="香草"]     不，呼......不要紧！我没问题的，博士。
[name="香草"]     我很清楚自己的状况，现在这样的训练强度还在可以负担的范围之内。
[name="香草"]     之前雷蛇前辈和杜宾教官一起帮我调整了训练表，请不要担心我！
[Predicate(references="2")]
[Character(name="char_240_Vanilla_1")]
[name="香草"]     呼哈......呼哈......
[name="香草"]     嗯？怎么了，博士，怎么满脸担忧的样子。
[name="香草"]     没关系，不用担心，虽然的确很累，不过我能撑住！
[Predicate(references="3")]
[Character(name="char_240_Vanilla_1")]
[name="香草"]     啊，呼哈......哈......谢谢......
[name="香草"]     哈啊......终于又活过来了。不过这个饮料，恶，还是老样子好难喝啊。
[name="香草"]     杜宾教官强调过好几次，运动之后喝这个对身体比较好，芙兰卡前辈也这么说，但是真的味道好怪。
[Predicate(references="1;2;3")]
[Character(name="char_240_Vanilla_1#5")]
[name="香草"]     来这里训练的干员们都好努力，我也要加油，不能拖大家的后腿。
[name="香草"]     啊对了博士，过两天我要和黑钢的前辈们一起出任务，暂时不会来训练场，这段时间非常感谢您的指导！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_corridor",screenadapt="coverall")]
[PlaySound(key="$d_gen_walk_n", volume=0.9)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_240_Vanilla_1#3")]
[name="香草"]     ...... 
[Decision(options="你看起来好像还有话想说。",values="1")]
[Predicate(references="1")]
[Character(name="char_240_Vanilla_1")]
[name="香草"]     这、不愧是博士......我表现得很明显吗？
[name="香草"]     这次，能和前辈们一起出任务，我当然很开心。只是......
[name="香草"]     我，呃，养了一些小动物，那个，平常都是我在照顾，但是要出任务的话，就只好拜托其他同伴暂时照看了。
[name="香草"]     一般来说，我都是拜托黑钢的前辈们的。
[name="香草"]     雷蛇前辈和芙兰卡前辈都经常帮忙，不过两位前辈总是一起出任务，休息时间也经常一起行动。
[name="香草"]     如果找不到其中的一个人的话，另一个基本也就没指望了。 
[Character(name="char_240_Vanilla_1#5")]
[name="香草"]     别看芙兰卡前辈平时总是爱开玩笑，其实她相当可靠，圆圆、小尖、大黑还有坚强，大家都很喜欢芙兰卡前辈！
[name="香草"]     偶尔找不到两位前辈的时候，杰西卡也会帮忙照顾，不过，呃，她之前差点被大黑吓哭。
[Decision(options="能问一下......",values="1")]
[Predicate(references="1")]
[Decision(options="你养的都是些什么‘小动物’吗？",values="1")]
[Predicate(references="1")]
[Character(name="char_240_Vanilla_1#2")]
[name="香草"]     咦。
[name="香草"]     我没有带圆圆他们和博士打过招呼吗？
[Character(name="char_240_Vanilla_1#5")]
[name="香草"]     圆圆小刺和大黑都是源石蜗牛，坚强是小型萨尔贡沙漠磐蟹，大家都是很可爱的！
[Decision(options="......",values="1")]
[Predicate(references="1")]
[Character(name="char_240_Vanilla_1")]
[name="香草"]     嗯？怎么了吗，博士？
[Character(name="char_240_Vanilla_1#2")]
[name="香草"]     不好......博士你的这个眼神，不、不行哦，不能吃，圆圆小刺大黑还有坚强都不能吃！我知道您有瞒着凯尔希医生吃一些奇怪的零食！
[name="香草"]     （本来还想拜托博士帮忙照顾的，这样看来，哎，还是算了吧。）
[Character(name="char_240_Vanilla_1#3")]
[name="香草"]     伤脑筋了，这次大家一起出任务，圆圆他们该怎么办才好。
[name="香草"]     嗯......其他干员的话，大家好像都有各自的事情要做，贸然拜托是不是不太好？
[Decision(options="试试看？",values="1")]
[Predicate(references="1")]
[Decision(options="比如说，拜托接下来路过的干员。",values="1")]
[Predicate(references="1")]
[Character(name="char_240_Vanilla_1#2")] 
[name="香草"]     咦？！这也太草率了吧！
[name="香草"]     博士，您是认真的吗？！
[Character(name="char_240_Vanilla_1#3")]
[name="香草"]     会是谁，来的会是谁......呜呜，希望会是个靠谱的人......
[dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.9)]
[Delay(time=1)]
[Decision(options="有人来了。",values="1")]
[Predicate(references="1")]
[PlaySound(key="$d_gen_walk_n", volume=0.9)]
[Delay(time=1)]
[Character(name="char_240_Vanilla_1#2")] 
[name="香草"]     ！
[name="香草"]     脚步声......好轻！这种步调的节奏，很稳，来的人一定是个优秀的战士！
[name="香草"]     嗯？有香味？
[name="香草"]     我记得这个香味应该是......
[Dialog]
[character]
[Character(name="char_208_melan_1#2",fadetime=1,blok=true)]
[Delay(time=2)]
[Character(name="char_240_Vanilla_1")] 
[name="香草"]     玫兰莎小姐！
[Character(name="char_208_melan_1#2")]
[CameraShake(duration=0.3, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="玫兰莎"]     ？！
[name="玫兰莎"]     是、是我。
[name="玫兰莎"]     博士，还有香草小姐，下午好。
[name="玫兰莎"]     那个，请问......两位找我有什么事吗？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_240_Vanilla_1",name2="char_208_melan_1",focus=2)]
[name="玫兰莎"]     不好意思，难得你拜托我，我却......
[Character(name="char_240_Vanilla_1#5",name2="char_208_melan_1",focus=1)]
[name="香草"]     没这回事！玫兰莎小姐明明帮了大忙，太感谢了！
[Character(name="char_240_Vanilla_1#5",name2="char_208_melan_1#4",focus=2)]
[name="玫兰莎"]     这没什么，我也只是转而拜托了史都华德而已。
[name="玫兰莎"]     而且，能帮上忙，我很开心。
[Character(name="char_240_Vanilla_1#5")]
[name="香草"]     欸。
[name="香草"]    （脸红了！）
[Character(name="char_210_stward_1#6")]
[name="史都华德"]     哈哈，玫兰莎小姐在战斗以外的场合还是那么容易害羞。
[name="史都华德"]     请两位放心，照顾香草小姐的小动物这件事就交给我吧。
[Character(name="char_240_Vanilla_1#5")]
[name="香草"]     真是太麻烦您了，非常感谢！
[Character(name="char_208_melan_1")]
[name="玫兰莎"]     谢谢，史都华德。
[Character(name="char_210_stward_1")]
[name="史都华德"]     两人都太客气啦，特别是香草小姐，完全没必要用敬称。
[Character(name="char_240_Vanilla_1#2")]
[name="香草"]     这、这怎么能行！两位都比如我要更早加入罗德岛，是我的前辈！
[Character(name="char_240_Vanilla_1#2",name2="char_208_melan_1",focus=2)]
[name="玫兰莎"]     太夸张了......
[Character(name="char_240_Vanilla_1",name2="char_208_melan_1",focus=1)]
[name="香草"]     对了，说起来，原来这次任务玫兰莎小姐也会一起去吗？
[name="香草"]     完全没听前辈们提起过啊......
[Character(name="char_240_Vanilla_1",name2="char_208_melan_1",focus=2)]
[name="玫兰莎"]     是、是的。
[name="玫兰莎"]     这是临时决定的，我也刚被通知。
[name="玫兰莎"]     是师傅，啊，就是芙兰卡小姐，说要检查一下我的剑术，正好有机会，就申请让我也加入小队了。
[Character(name="char_240_Vanilla_1",name2="char_208_melan_1",focus=1)]
[name="香草"]     欸，芙兰卡前辈？前辈指导玫兰莎小姐剑术吗？
[Character(name="char_240_Vanilla_1",name2="char_208_melan_1",focus=2)]
[name="玫兰莎"]     是的。
[Character(name="char_240_Vanilla_1",name2="char_208_melan_1",focus=1)]
[name="香草"]     前辈，真的有在好好指导吗......
[

... (全文29960字符)
```

### level_act7d5_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1,block=true)]
[character]
[Delay(time=0.5)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, fadetime=1, block=true)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Character(name="char_108_silent_1",fadetime=1,blok=true)]
[Delay(time=1)]
[name="赫默"]     白面鸮，你回来了。
[Dialog]
[character]
[PlaySound(key="$d_gen_walk_n", volume=0.9)]
[Character(name="char_128_plosis_1",fadetime=1,blok=true)]
[Delay(time=1)]
[name="白面鸮"]     是的。
[Character(name="char_128_plosis_1",name2="char_108_silent_1",focus=2)]
[name="赫默"]     这次代替我实地考察辛苦了，在你离开的这段时间里，我手上的这场实验也接近完成了，之后我就可以自己去了。
[Character(name="char_128_plosis_1",name2="char_108_silent_1",focus=1)]
[name="白面鸮"]     没事。
[name="白面鸮"]     下次也可以让我去。
[Character(name="char_128_plosis_1",name2="char_108_silent_1",focus=2)]
[name="赫默"]     ......嗯？
[name="赫默"]     发生了什么吗？
[Character(name="char_128_plosis_1",name2="char_108_silent_1",focus=1)]
[name="白面鸮"]     嗯，那么，我先回去了。
[Character(name="char_128_plosis_1",name2="char_108_silent_1",focus=2)]
[name="赫默"]     ............好。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_room_2",screenadapt="coverall")]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_128_plosis_1")]
[name="白面鸮"]     我记得，应该是这本日记本......
[name="白面鸮"]     不对，这本是还在莱茵生命时写下的了。那么，应该是这本......
[name="白面鸮"]     找到了，是这本，在跟随赫默来到罗德岛后，换的新日记本。
[name="白面鸮"]     让我看看。
[character]
[name="日记"]     3月21日 阴
[name="日记"]     今天，岛上加入了两个新的干员，一个叫吽，一个叫阿，他们似乎是和槐琥小姐来自同一个地方。
[name="日记"]     其中，令人在意的是阿，他看起来十分年轻，据说在龙门是非常有名的黑医生，不过他似乎不会加入医疗部。
[name="日记"]     4月2日 多云
[name="日记"]     ......对了，自从阿发现华法琳就是“血先生”后，他就经常来医疗部。
[name="日记"]     但医疗部的大部分人都不喜欢他，因为他毫不掩饰地对身为同行的我们表现出厌恶感。
[name="日记"]     他明明医术相当高明，这是为什么呢？......
[name="日记"]     4月15日 晴
[name="日记"]     ......说到阿，在上次和华法琳比试的最后，吽过来把他带走之后，他收敛了一些。
[name="日记"]     而医疗组的各位已经逐渐习惯了他的性格——至少表面上如此。
[Character(name="char_128_plosis_1")]
[name="白面鸮"]     这么说起来，写下这篇日记的时候，正好是他和华法琳的第二次“对决”呢。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_corridor",screenadapt="coverall")]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_225_haak_1#1")]
[name="阿"]     喂，“血先生”，来比试吧！
[Character(name="char_171_bldsk_1",name2="char_225_haak_1#1",focus=1)]
[name="华法琳"]     哇，你这个小鬼好烦，上次输给我你还没意识到我们之间的差距吗？
[Character(name="char_171_bldsk_1",name2="char_225_haak_1#1",focus=2)]
[name="阿"]     你认真的？那个能算我输吗？
[Character(name="char_225_haak_1#1")]
[name="阿"]     喂，那边的羽毛大姐，你当时也在场，你说说！
[Character(name="char_108_silent_1")]
[name="赫默"]     ......
[Character(name="char_128_plosis_1",name2="char_108_silent_1",focus=1)]
[name="白面鸮"]     赫默，他在叫你。
[Character(name="char_128_plosis_1",name2="char_108_silent_1",focus=2)]
[name="赫默"]     他在叫我？
[Character(name="char_128_plosis_1",name2="char_108_silent_1",focus=1)]
[name="白面鸮"]     根据系统判断，虽然也有50%叫我的可能性，但我的逻辑思维判断我不想回应这个称呼。
[Character(name="char_128_plosis_1",name2="char_108_silent_1",focus=2)]
[name="赫默"]     我也不想。
[Character(name="char_108_silent_1",name2="char_225_haak_1#1",focus=2)]
[name="阿"]     你们在说什么悄悄话呢，快说啊，上次那个怎么也不算我输吧？
[Character(name="char_108_silent_1",name2="char_225_haak_1#1",focus=1)]
[name="赫默"]     ......阿，现在是工作时间，请你不要随意来打扰我们工作好吗？
[Character(name="char_108_silent_1",name2="char_225_haak_1#1",focus=2)]
[name="阿"]     是是是，我只是问个问题，问完就走，绝不打扰你们高尚的“工作”。
[Character(name="char_128_plosis_1")]
[name="白面鸮"]     好吧，调用系统记录中......
[name="白面鸮"]     根据系统记录显示，确实，客观来说，上次的比试，由于最后的突发状况，很难判断究竟是哪方的胜利。
[Character(name="char_171_bldsk_1",name2="char_225_haak_1#1",focus=2)]
[name="阿"]     嘿，听到了吧！
[Character(name="char_171_bldsk_1",name2="char_225_haak_1#1",focus=1)]
[name="华法琳"]     啧，行吧，看我今天让你输得心服口服！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[name="爱聊天的医疗干员"]     哎，自从这个阿来了之后，每天都鸡飞狗跳的。真是不明白博士为什么会把这样的人招进来......
[Character(name="char_128_plosis_1")]
[name="白面鸮"]     虽然性格很恶劣，但不可否认的是，他的临床经验以及天赋，确实十分惊人。
[character]
[name="爱聊天的医疗干员"]     你说的我也明白，但我觉得他根本就看不起我们欸。
[name="活泼的医疗干员"]     对对，上次那场手术确实让很多人对他刮目相看了，我本来也对他有些改观，想和他搞好关系，结果被他一通嘲。
[name="活泼的医疗干员"]     气死我了！
[name="八卦的医疗干员"]     也就只有华法琳大姐头能跟他搞好关系了。
[name="冷静的医疗干员"]     他们那叫搞好关系吗......白面鸮你觉得呢？
[Character(name="char_128_plosis_1")]
[name="白面鸮"]     从系统中检索词汇......检索结果，臭味相投。
[character]
[name="活泼的医疗干员"]     哈哈哈，没错，就是这个！
[Character(name="char_212_ansel_1")]
[name="安赛尔"]     你们在聊什么呢，这么开心。
[character]
[name="八卦的医疗干员"]     啊，安赛尔医生，我们在聊阿呢。
[Character(name="char_212_ansel_1")]
[name="安赛尔"]     噢......虽然我不是很擅长应付他那样的性格，但确实是一个很厉害的新人呢。
[character]
[name="活泼的医疗干员"]     不愧是安赛尔医生，即使对阿都这么温柔......
[Character(name="char_108_silent_1")]
[name="赫默"]     好了，就算今天没有什么事，工作时间也禁止闲谈，回到你们的工作岗位去。
[character]
[name="医疗干员们"]     是——
[Character(name="char_108_silent_1")]
[name="赫默"]     安赛尔，怎么样？
[Character(name="char_212_ansel_1",name2="char_108_silent_1",focus=1)]
[name="安赛尔"]     唔，这里是报告，总的来说，效果不是很令人满意。
[Character(name="char_212_ansel_1",name2="char_108_silent_1",focus=2)]
[name="赫默"]     嗯，虽然事先已经预想到了，那么，马上准备下一场实验吧。
[Character(name="char_108_silent_1")]
[name="赫默"]     白面鸮，你也一起去吧。
[Character(name="char_128_plosis_1")]
[name="白面鸮"]     Zzzzzzz......嗯？好，我知道了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_room_2",screenadapt="coverall")]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[name="日记"]     阿的加入为医疗部带来了一些吵闹和波澜，虽然其中有些不愉快，但不知为什么，我并不讨厌......
[Character(name="char_128_plosis_1")]
[name="白面鸮"]     嗯，我在这一篇写了，“我并不讨厌。”
[name="白面鸮"]     如果我没记错的话，往前应该还有......
[name="白面鸮"]     对了，在这里。
[Character]
[name="日记"]     6月10日 小雨
[name="日记"]     根据侦查干员的情报，在周边的山区里似乎发现了源石矿脉，凯尔希医生已经派人去勘查了。
[name="日记"]     保险起见，赫默和一些医疗干员也一起去了。
[name="日记"]     今天除了

... (全文22785字符)
```

### level_act7d5_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1,block=true)]
[character]
[Delay(time=0.5)]
[Background(image="bg_canteen",screenadapt="coverall")]
[Blocker(a=0, fadetime=1, block=true)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
9:50 A.M.  天气/晴
罗德岛舰船，第二舱室，公共食堂
[Dialog]
[Character(name="char_199_yak_1",fadetime=1,blok=true)]
[Delay(time=1)]
[name="角峰"]     北谢拉格风爆炒绿英菜，再撒上少许罗德岛特制调味粉......
[name="角峰"]     这样就完成了。
[Character(name="char_196_sunbr_1#5")]
[name="古米"]     哇！看起来好好吃！
[Character(name="char_199_yak_1")]
[name="角峰"]       过奖了。
[name="角峰"]     这种绿叶蔬菜在谢拉格很少见，我也很少有机会尝试去料理，能顺利再好不过。
[name="角峰"]     雪境不比罗德岛，在谢拉格的雪原上，许多东西都很匮乏，是花钱也很难买到的。这里虽说是在舰上，但物资却还是很充足，真是难得。
[Character(name="char_196_sunbr_1#3",name2="char_199_yak_1",focus=1)]
[name="古米"]     物资啊......这方面的事情，我好像听可露希尔姐姐提起过。
[name="古米"]     好像是说，罗德岛有专门的采购渠道，定期会有采购人员向舰内运送物资什么的。
[name="古米"]     因为在很多地方都有据点，所以就经常能尝到各地各种不同的食材啦。
[Character(name="char_196_sunbr_1#3",name2="char_199_yak_1",focus=2)]
[name="角峰"]     怪不得。不过，在很多地方都有据点？
[Character(name="char_196_sunbr_1#3",name2="char_199_yak_1",focus=1)]
[name="古米"]     嗯......好像是类似什么、办事处一类的地方。这个我不懂啦！
[Character(name="char_196_sunbr_1#2",name2="char_199_yak_1",focus=1)]
[name="古米"]     对了，食堂外面的告示板上不是还贴了心愿单吗？如果有什么特别想吃的东西，都可以写在那上面哦！
[name="古米"]     据说负责采购的哥哥姐姐们会参考那个！
[character]
[name="路过的采购员A"]     小古米的嘴真甜，再叫一声姐姐，姐姐给你带糖回来。
[Character(name="char_196_sunbr_1#5")]
[name="古米"]     采购姐姐！
[character]
[name="路过的采购员A"]     哎，乖。
[name="路过的采购员B"]     你正经点......
[name="路过的采购员B"]     角峰先生是吧，有什么想要的食材可以尝试写在告示板上，如果有机会的话，我们会进行采购。
[Character(name="char_199_yak_1")]
[name="角峰"]     明白了，有需要的话我会尝试，届时就辛苦各位了。
[character]
[name="路过的采购员B"]     不必这样客气，这是我们的职责。
[name="路过的采购员A"]     你们说话怎么那么死板？大家都是一条船上的人了，放轻松点、自由点说话行不？
[name="路过的采购员B"]     你那是自由过头了！
[name="路过的采购员B"]     两位别理这家伙，我们接下来还有任务，就不打扰两位了。
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[delay(time=2)]
[Character(name="char_196_sunbr_1#5")]
[name="古米"]     嘿嘿，大家都是很好的人呢，之前停靠在城市边的时候，可露希尔姐姐还带我一起去采购了哦！
[name="古米"]     虽然她会买些怪怪的东西......不过还是很有意思的！
[Character(name="char_196_sunbr_1#5",name2="char_199_yak_1#5",focus=2)]
[name="角峰"]     哈哈，这我也有所耳闻。之前是不是还因为买了巨大陶土面具，惹那位凯尔希医生生气了？
[Character(name="char_196_sunbr_1#5",name2="char_199_yak_1#5",focus=1)]
[name="古米"]     啊哈哈哈，没错没错，我试过一次，那个面具太怪了！
[Character(name="char_196_sunbr_1#5",name2="char_199_yak_1",focus=2)]
[name="角峰"]     那种一看就很奇怪的东西，就不要去尝试了吧。
[Character(name="char_199_yak_1")]
[name="角峰"]     嗯，菜凉下来了，温度正好。
[name="角峰"]     唔，好像有一点咸了，这个口味，可能会有一点刺激......
[Character(name="char_196_sunbr_1#5",name2="char_199_yak_1#5",focus=1)]
[name="古米"]     不会啦，我觉得一定很好吃。
[name="古米"]     啊，要不然让我试吃看看吧？可以吗，让我吃吃看吧，角峰大叔！
[Character(name="char_196_sunbr_1#5",name2="char_199_yak_1#2",focus=2)]
[name="角峰"]     大、大叔......
[name="角峰"]     （在这个年纪的孩子眼里，我已经是大叔了吗......）
[Character(name="char_196_sunbr_1#5",name2="char_199_yak_1#5",focus=2)]
[name="角峰"]     当然没问题，如果你愿意尝尝看的话，算是帮了我大忙了。
[Character(name="char_196_sunbr_1#5")]
[name="古米"]     好耶！
[Character(name="char_196_sunbr_1#2")]
[name="古米"]     嘿嘿嘿，让我尝一尝......咦？
[Character(name="char_196_sunbr_1#2",name2="char_199_yak_1",focus=2)]
[name="角峰"]     嗯？怎么了吗？
[Character(name="char_196_sunbr_1#2",name2="char_199_yak_1",focus=1)]
[name="古米"]     欸......怎么回事，这盘菜，怎么感觉好像、好像比之前要少了一点？
[name="古米"]     好奇怪啊，是我的错觉吗......
[Character(name="char_196_sunbr_1#2",name2="char_199_yak_1#3",focus=2)]
[name="角峰"]     ......
[Character(name="char_196_sunbr_1#5")]
[name="古米"]     算啦，让我来尝尝看！
[Character(name="char_196_sunbr_1#7")]
[name="古米"]     啊——唔。啊呜啊呜啊呜。
[name="古米"]     （咀嚼咀嚼）
[Character(name="char_196_sunbr_1#7",name2="char_199_yak_1#3",focus=2)]
[name="角峰"]     怎、怎么样？
[Character(name="char_196_sunbr_1#7",name2="char_199_yak_1#3",focus=1)]
[name="古米"]     唔姆唔姆。咕噜。
[Character(name="char_196_sunbr_1#5",name2="char_199_yak_1#3",focus=1)]
[name="古米"]     好吃！！
[name="古米"]     蔬菜又脆又多汁而且非常爽口，调味也很清爽，完全不会让人感觉味道很重！哇啊总之就是好好吃！
[Character(name="char_196_sunbr_1#5",name2="char_199_yak_1#5",focus=2)]
[name="角峰"]     是、是吗，多谢夸奖，这样我就放心了。
[name="角峰"]     不过没有你说的这么夸张，这种料理方法步骤简单，很适合家庭制作，之后我会把菜谱留一份挂在小厨房，大家都可以试试看。
[Character(name="char_196_sunbr_1#5",name2="char_199_yak_1#5",focus=1)]
[name="古米"]     好耶！
[name="古米"]     角峰大叔也可以看古米的营养满分乌萨斯秘制蔬菜冻汤！我们交换~
[Character(name="char_196_sunbr_1#5",name2="char_199_yak_1#5",focus=2)]
[name="角峰"]     听起来很美味，那么下次给小姐们做宵夜的时候，就让我来试试看吧。
[Character(name="char_196_sunbr_1#5",name2="char_199_yak_1#5",focus=1)]
[name="古米"]     嘿嘿。初雪小姐和崖心小姐一定会喜欢的~
[Character(name="char_196_sunbr_1#5",name2="char_199_yak_1#5",focus=2)]
[name="角峰"]     （大小姐和二小姐吗......）
[name="角峰"]     对了，古米小小姐，你做好的蛋炖肉排，不快点送过去可以吗？
[name="角峰"]     是给博士做的吧？再放下去就快要凉透了，会很影响口感......不要紧吗。
[Character(name="char_196_sunbr_1#3")]
[name="古米"]     哇！差点忘记了！！
[name="古米"]     那我先走啦！角峰大叔！炒绿英菜超好吃的，一定要记得留菜谱呀！
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[Character(fadetime=1,block=true)]
[Delay(time=2)]
[Character(name="char_199_yak_1#5")]
[name="角峰"]     真是个有活力的小姑娘。
[name="角峰"]     ......
[Character(name="char_199_yak_1")]
[name="角峰"]     ......
[name="角峰"]     出来吧。
[Dialog]
[delay(time=1)]
[name="角峰"]     ......不出来吗。
[name="角峰"]     呼。
[name="角峰"]     那么，别怪我不客气——
[Dialog]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_skill_skulsrsword")]
[character]
[name="？？？"]     哦！
[name="？？？"]     可怕可怕。
[name="？？？"]     也没必要上来就动刀动枪吧？说来，你那武器是从哪掏出来的？怎么来厨房还带着武器，真危险。
[name="？？？"]     唉，你是怎么发现我的？奇怪了，我觉得自己藏得挺好的啊。
[Character(name="char_355_ethan_1",fadetime=1,blok=true)]
[Delay(time=1)]
[name="伊桑"]     （咬苹果）
[Character(name="char_199_yak_1")]
[name="角峰"]     ......是你。
[name="角峰"]     又来厨房偷吃东西吗，其实你完全不必这样，如果饿了，直接去食堂就好。
[name="角峰"]     上次的教训还不够？我记得之前后勤处的人员应该有和你强调过，如果再被发现利用特殊能力擅自取用料理或食材，会有相对的处罚吧。
[Character(name="char_199_yak_1",name2="char_355_ethan_1",focus=2)]
[name="伊桑"]     处罚？哦，你是说他们定的那个，‘被抓一次就在脸上画一只乌龟’的那个？
[name="伊桑"]     这算什么处罚，我还以为是在开玩笑来着。
[name="伊桑"]     哎，不对，你还没说是怎么发

... (全文18494字符)
```

### level_act7d5_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1,block=true)]
[character]
[Delay(time=0.5)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, fadetime=1, block=true)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
罗德岛本舰
第六体检室
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     来，张嘴。
[name="芙蓉"]     啊~~
[character]
[name="？？？"]     ......
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     啊~~
[character]
[name="？？？"]     哼。
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     来吧，把嘴巴张开好不好，我就检查一下牙齿，不会做什么坏事的。
[character]
[name="？？？"]     ......
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     唉......
[name="芙蓉"]     不要每次都逼我用杀手锏啊。
[name="芙蓉"]     哼哼，马上就让你乖乖听话。
[name="芙蓉"]     嘿！
[name="芙蓉"]     佩洛小姐你看，这是什么？
[character]
[name="？？？"]     ？
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     是你最喜欢的东西，对吧。
[name="芙蓉"]     如果你好好协助我完成检查的话......
[name="芙蓉"]     这些蜜饼就全给你哦。
[character]
[name="？？？"]     （嗅嗅）
[name="？？？"]     ......
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     奇怪，她怎么对蜜饼没反应了？
[Character(name="char_121_lava_1")]
[name="炎熔"]     你配方有问题，芙蓉。
[name="炎熔"]     我说了多少次不要在食物里加奇怪的东西。
[name="炎熔"]     你又不听。
[name="炎熔"]     来，小佩洛，给你这个。
[character]
[name="？？？"]     （嗅嗅）
[name="？？？"]     啊呜。
[Character(name="char_121_lava_1")]
[name="炎熔"]     吃完记得听话。
[character]
[name="？？？"]     唔唔——
[name="？？？"]     啊呜啊呜。
[name="？？？"]     啊——
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     成功了！
[name="芙蓉"]     不愧是小炎熔呢，真是可靠。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     是你不行啊。
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     那，口腔检查开始了哦。
[name="芙蓉"]     把碎屑吞下去，好，然后嘴巴张大——
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     唉，我说啊芙蓉。
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     舌头不要乱舔啊佩洛小姐——啊，怎么了？
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     我们为什么要把她带回来啊。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     因为她很可怜啊，感染那么严重。
[name="芙蓉"]     而且莱塔尼亚分会的会长先生也说了：
[name="芙蓉"]     “还好是你们发现并且制服了她，要是被莱塔尼亚警察或者赏金猎人抓到，她就没有希望了。”
[name="芙蓉"]     “像她这种感染级别的感染者，按照最近莱塔尼亚对感染者的政策变化，有很大可能会被人道处理。”
[name="芙蓉"]     “如果可以的话，请至少把她带离莱塔尼亚境内，多谢各位了。”
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     就算不是感染者，像她那样无规律袭击行人也一定会被抓好吧。
[name="炎熔"]     在我们之前，已经有至少二十四批旅行者遭袭，近百人受到损失啊。
[name="炎熔"]     这还只是在莱塔尼亚境内，谁知道她在其他地方还做过什么事。
[name="炎熔"]     就她那个袭击技术，我觉得我们五个人都做不到那么好。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     可除了拿走食物填饱肚子外，她也没做什么坏事——好疼！
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     “没做什么坏事”？！我差点都没命了！
[name="炎熔"]     要不是克洛丝警戒做的还不错，米格鲁及时用盾护住我，她丢来的那根裹着岩石的标枪就要把你妹妹砸碎了。
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     佩洛小姐请不要咬我的手好吗！
[character]
[name="？？？"]     呜呜。
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     好好好，我这就帮你搞定炎熔。
[name="芙蓉"]     牙齿也马上就看好了，再稍微忍耐一小会，加油！
[name="芙蓉"]     嗯，好孩子。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     好啦炎熔，不要闹脾气了。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     我这是陈述事实，不叫闹脾气。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     怎么了，突然之间像小孩子一样斤斤计较的。
[name="芙蓉"]     你不也很喜欢佩洛小姐的吗。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     是啊，我是很喜欢。她也很喜欢我。
[name="炎熔"]     应付她的时候什么岩石火焰寒冰都往我身上砸。
[name="炎熔"]     也不知道她怎么掌握那么多复杂技巧的。
[Character(name="char_121_lava_1")]
[name="炎熔"]     喂，小佩洛。你真的没有学过源石技艺吗？
[character]
[name="？？？"]     喔？
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     啊啊不要乱动——炎熔你别在这时候捣乱啊！
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     只是问问题而已......
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     炎——熔——！
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     好好好我的错，我的错，行了吧。
[character]
[name="？？？"]     唔唔？
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     啊，抱歉，佩洛小姐，马上就好。
[name="芙蓉"]     还有这边和那边。
[name="芙蓉"]     ......
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     ......
[Character(name="char_120_hibisc_1")]
[name="芙蓉"]     呼，应该差不多了。
[name="芙蓉"]     来，佩洛小姐，检查差不多完成啦，拿这杯水漱漱口吧，记得吐在那个盆里，不要喝下去哦。
[character]
[name="？？？"]     嗯。
[name="？？？"]     （咕咚。）
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     小炎熔。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     啊？
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     你还是这么别扭。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     关你什么事。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     我们小队里第一个请她吃好吃的是你吧。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     你，突然说这个干嘛。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     虽然从营养学的角度来说她不该在饥饿过久以后摄入那么多糖分，但那时候她真的什么都需要补充。
[name="芙蓉"]     然后啊。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     等等......
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     炎熔就悄悄跑出去买了好多糖果。
[name="芙蓉"]     回过头来才发现自己把钱花光了。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     别说了......
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     护送佩洛小姐回来的时候呢，本来大家都怕她跑走。
[name="芙蓉"]     也只有炎熔鼓起勇气先和她沟通，帮助大家深入了解她，让她能够取下镣铐也不逃跑乖乖跟着我们走。
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=1)]
[name="炎熔"]     呃......
[Character(name="char_121_lava_1",name2="char_120_hibisc_1",focus=2)]
[name="芙蓉"]     知道佩洛小姐喜欢吃蜜饼后，我们小队五个

... (全文26870字符)
```

### level_act7d5_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1,block=true)]
[character]
[Delay(time=0.5)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, fadetime=1, block=true)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
PM9：39 罗德岛舰内
[Character(name="char_278_orchid_1",fadetime=1,blok=true)]
[Delay(time=1)]
[name="梓兰"]     呼......总算是搞定了。
[Character(name="avg_npc_012")]
[name="后勤干员"]     辛苦了，梓兰小姐。
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=1)]
[name="梓兰"]     真的是，不知不觉就跟你们熟起来了，结果搞得我像你们的编外人员似的。
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     啊哈哈，因为梓兰小姐你对这方面很熟练嘛，不知不觉就......
[Character(name="char_278_orchid_1#2",name2="avg_npc_012",focus=1)]
[name="梓兰"]     哈......比起带那帮怪胎来说，我倒确实更擅长这个就是了。
[Character(name="char_278_orchid_1#2",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     那梓兰小姐要不要申请一下转到我们后勤部门来？
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=1)]
[name="梓兰"]     欸？
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     其实像梓兰小姐你这样的民间人士，加入罗德岛后会选择成为干员的反倒是少数呢，大部分都是像我们一样加入后勤部门。
[name="后勤干员"]     不如说，我们其实一直都挺好奇为什么你会选择上前线呢。
[Character(name="char_278_orchid_1#4",name2="avg_npc_012",focus=1)]
[name="梓兰"]     你问为什么，嗯......
[Dialog]
[Character]
[stopmusic(fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     梓兰小姐，既然你想要加入罗德岛，那么你想做什么样的工作呢？
[name="后勤干员"]     根据测验的结果，你是拥有相当的源石技艺适应性的，只要你愿意，经过训练就可以加入前线的行列。
[name="后勤干员"]     不过，因为你是民间人士，没有相关的战斗经验，我们还是建议你加入后勤相关的部门。
[name="后勤干员"]     当然，请放心，即使你加入前线，我们不会给你安排危险的任务，会根据实力的评估。
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=1)]
[name="梓兰"]     后勤是做什么的？
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     嗯......后勤部门细分下来也有许多呢，不过总的来说，是为了维持罗德岛运转的各种工作吧。
[name="后勤干员"]     因为文职比较多，所以比较适合你这样习惯了都市生活的人呢。
[Character(name="char_278_orchid_1#4")]
[name="梓兰"]     （也就是说，坐办公室吗......）
[name="梓兰"]     （原本就是想要转换心情才想着试试在这边工作，我可不想再在这里过办公室生活。）
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=1)]
[name="梓兰"]     我......还是申请加入前线吧。
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     真的吗？前线干员可是很辛苦的哦？
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=1)]
[name="梓兰"]     嗯，我想试一试。
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     好的，我知道了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_278_orchid_1#2")]
[name="梓兰"]     （事到如今，我就是不想坐办公室才会那么选的这种话实在是说不出口啊。）
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=1)]
[name="梓兰"]     ......这么一说，好像我稀里糊涂地就变成干员了。
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     啊，确实，对我们不了解的话，是会出现这种情况呢。
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=1)]
[name="梓兰"]     是，是吗......
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     不过，我记得针对这样的情况，我们是有应对措施的，我看看条例......
[name="后勤干员"]     啊，没错，这一条写了，
[name="后勤干员"]     “民间出身的战斗干员，在作为战斗干员工作的一年内，若不适应前线生活并申请转为后勤干员，应予以无条件通过。”
[name="后勤干员"]     梓兰小姐还加入我们没多久，适用于这一条哦，不如说，其实你们A6的所有人，除了萨尔贡军人出身的斑点，都适用这一条呢。
[name="后勤干员"]     即使是斑点，也只是需要稍微过个审查而已，我们在这方面还是相当自由的。
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=1)]
[name="梓兰"]     这样啊，我都没想过这方面的事。
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     而且你也知道，我们的工作其实一点也不比要战斗的干员们轻松，罗德岛的方方面面还是靠我们维持的呢。
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=1)]
[name="梓兰"]     嗯，我知道，谢谢，我会考虑的。
[Dialog]
[character]
[Character(name="char_281_popka_1#7",fadetime=1,blok=true)]
[Delay(time=1)]
[name="泡普卡"]     梓兰姐姐，还没好吗？
[Character(name="char_278_orchid_1",name2="char_281_popka_1#7",focus=1)]
[name="梓兰"]     这就好。
[Character(name="char_278_orchid_1",name2="char_281_popka_1#6",focus=2)]
[name="泡普卡"]     好~
[Character(name="char_281_popka_1#6",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     咦，这不是小泡普卡吗，她在等你吗？
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=1)]
[name="梓兰"]     嗯，在路上遇到的，她就跟过来了。
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     这么说起来，我记得上个月你说过，申请和她搬进一间二人宿舍了吧？
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=1)]
[name="梓兰"]     是啊，唉，这丫头也是个不让人省心的，也不知道是谁让这么小的孩子也出来战斗的。
[name="梓兰"]     队里其他人要么靠不住要么比她还不让人省心，可不就只能这么办了。
[Character(name="char_278_orchid_1",name2="char_281_popka_1",focus=2)]
[name="泡普卡"]     梓兰姐姐，还没好吗？
[Character(name="char_278_orchid_1")]
[name="梓兰"]     来了来了。那我先走了。
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=2)]
[name="后勤干员"]     别忘了我刚才说的事，期待你的答复~
[Character(name="char_278_orchid_1",name2="avg_npc_012",focus=1)]
[name="梓兰"]     嗯。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_278_orchid_1#2")]
[name="梓兰"]     哈......其实现在想想也挺好笑的，原本是为了逃离办公室生活才选择试试战斗的，结果最后还是变成刚才那样。
[name="梓兰"]     难道我这辈子就注定是个上班族吗......
[Character(name="char_278_orchid_1#2",name2="char_281_popka_1",focus=2)]
[name="泡普卡"]     梓兰姐姐，什么是上班族？
[Character(name="char_278_orchid_1#3",name2="char_281_popka_1",focus=1)]
[name="梓兰"]     上班族就是天天坐在办公室里发霉8小时，做的事完全就是重复机械劳动，下班了还不一定能走的悲惨职业哦。
[Character(name="char_278_orchid_1#3",name2="char_281_popka_1",focus=2)]
[name="泡普卡"]     哦......不懂。
[Character(name="char_278_orchid_1",name2="char_281_popka_1",focus=1)]
[name="梓兰"] 

... (全文32830字符)
```

### level_act7d5_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1,block=true)]
[character]
[Delay(time=0.5)]
[Background(image="bg_trainingcom",screenadapt="coverall")]
[Blocker(a=0, fadetime=1, block=true)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
AM10：21 罗德岛训练场
[Character(name="char_123_fang_1")]
[name="芬"]     就是这里！
[Character(name="char_013_riop")]
[name="格瑞斯教官"]     还不够快！
[Character(name="char_123_fang_1")]
[name="芬"]     糟了！
[name="芬"]     但是......！
[Character(name="char_013_riop")]
[name="格瑞斯教官"]     到此为止！
[Character(name="char_123_fang_1")]
[name="芬"]     呼，呼......
[Character(name="char_013_riop")]
[name="格瑞斯教官"]     不错啊，芬，上次你可挡不住这一下。
[name="格瑞斯教官"]     你在战斗中越来越灵活了，这很好。
[Character(name="char_123_fang_1",name2="char_013_riop",focus=1)]
[name="芬"]     嗯，杜宾老师教导我的，不仅是要运用自己的脚力，还要适应自己的速度，我现在稍微有些掌握了这种感觉！
[Character(name="char_123_fang_1",name2="char_013_riop",focus=2)]
[name="格瑞斯教官"]     没错，你有库兰塔天生的速度，对奇袭很有帮助。但如果敌人挡住了你的攻击，而你无法做出回应，那就没有很大的意义。
[name="格瑞斯教官"]     总之，这次实战演习你通过了。
[Character(name="char_123_fang_1",name2="char_013_riop",focus=1)]
[name="芬"]     谢谢格瑞斯老师！
[Character(name="char_123_fang_1",name2="char_013_riop",focus=2)]
[name="格瑞斯教官"]     不过既然你通过了，下次的小测验可就会更加难了。
[Character(name="char_123_fang_1",name2="char_013_riop",focus=1)]
[name="芬"]     是，我会加油的！
[Character(name="char_123_fang_1",name2="char_013_riop",focus=2)]
[name="格瑞斯教官"]     嗯，要的就是这种精神。
[Character(name="char_122_beagle_1")]
[name="米格鲁"]     芬~~
[Character(name="char_122_beagle_1",name2="char_123_fang_1",focus=2)]
[name="芬"]     米格鲁，你的测验也结束了吗，怎么样？
[Character(name="char_122_beagle_1",name2="char_123_fang_1",focus=1)]
[name="米格鲁"]     唉，我没有通过......法伦老师的进攻太刁钻了......
[Character(name="char_122_beagle_1",name2="char_123_fang_1",focus=2)]
[name="芬"]     别灰心，下次再加油吧。
[Character(name="char_122_beagle_1",name2="char_123_fang_1",focus=1)]
[name="米格鲁"]     芬呢，通过了吗？
[Character(name="char_122_beagle_1",name2="char_123_fang_1",focus=2)]
[name="芬"]     嗯。
[Character(name="char_122_beagle_1",name2="char_123_fang_1",focus=1)]
[name="米格鲁"]     真好啊......
[Character(name="char_124_kroos_1")]
[name="克洛丝"]     呜呜，屁股好痛......
[Character(name="char_124_kroos_1",name2="char_122_beagle_1",focus=2)]
[name="米格鲁"]     克洛丝，你怎么了？
[Character(name="char_124_kroos_1",name2="char_122_beagle_1",focus=1)]
[name="克洛丝"]     我被苔丝老师射中了屁股......
[Character(name="char_124_kroos_1",name2="char_122_beagle_1",focus=2)]
[name="米格鲁"]     啊？
[Character(name="char_124_kroos_1",name2="char_122_beagle_1",focus=1)]
[name="克洛丝"]     我不是负责狙击嘛，所以测试是和苔丝老师互相隐蔽并找到对方，但是我完全没注意到她是怎么绕到我背后去的！
[Character(name="char_124_kroos_1",name2="char_013_riop",focus=2)]
[name="格瑞斯教官"]     哈哈哈哈哈！
[Character(name="char_124_kroos_1",name2="char_013_riop",focus=1)]
[name="克洛丝"]     格瑞斯大叔你还笑！
[Character(name="char_124_kroos_1",name2="char_013_riop",focus=2)]
[name="格瑞斯教官"]     我必须承认，其他的狙击教官这几天恰好不在，导致测试只能和苔丝对上的你确实有点倒霉。
[name="格瑞斯教官"]     我都受不了她的神出鬼没，你应该试试把你找偷懒地点的劲头拿出来。
[Character(name="char_124_kroos_1",name2="char_013_riop",focus=1)]
[name="克洛丝"]     嘁，你就笑吧。
[Character(name="char_124_kroos_1",name2="char_122_beagle_1",focus=1)]
[name="克洛丝"]     我刚刚去看了眼芙蓉和炎熔，炎熔通过了，芙蓉没有，她们两个先回去了，你们呢？
[Character(name="char_124_kroos_1",name2="char_122_beagle_1",focus=2)]
[name="米格鲁"]     芬通过了哦。
[Character(name="char_124_kroos_1")]
[name="克洛丝"]     啊，芬你这个叛徒！
[Character(name="char_124_kroos_1",name2="char_123_fang_1",focus=2)]
[name="芬"]     谁是叛徒啦！
[Character(name="char_122_beagle_1",name2="char_123_fang_1",focus=1)]
[name="米格鲁"]     唉，这次又没有通过测试，怎么办啊......
[Character(name="char_122_beagle_1",name2="char_123_fang_1",focus=2)]
[name="芬"]     别灰心啊，米格鲁，我们还有许多机会。
[Character(name="char_124_kroos_1",name2="char_122_beagle_1",focus=1)]
[name="克洛丝"]     就是啊，只是一次小测验，有什么好难过的，而且下午才是地狱呢。
[Character(name="char_124_kroos_1",name2="char_013_riop",focus=2)]
[name="格瑞斯教官"]     哈哈，确实，上午只是你们的个人小测验，杜宾是交给我们几个教官的，不过下午的团体实战测验就不一样了。
[Character(name="char_124_kroos_1",name2="char_013_riop",focus=1)]
[name="克洛丝"]     唉，别说了，我已经能够想象杜宾老师看到我的测验结果的表情了。
[Character(name="char_124_kroos_1",name2="char_013_riop",focus=2)]
[name="格瑞斯教官"]     现在知道后悔了？
[Character(name="char_124_kroos_1",name2="char_013_riop",focus=1)]
[name="克洛丝"]     才没有，杜宾老师说我们按照自己的步调来就好了，我只是比较晚熟！
[Character(name="char_124_kroos_1",name2="char_013_riop",focus=2)]
[name="格瑞斯教官"]     嚯嚯。
[Character(name="char_122_beagle_1")]
[name="米格鲁"]     但是我也担心杜宾老师对我们失望......
[Character(name="char_123_fang_1")]
[name="芬"]     米格鲁，克洛丝......
[Character(name="char_013_riop")]
[name="格瑞斯教官"]     好啦，认真地说，你们也不用太灰心，原本设置这样的测试，就不是为了让你们通过，而是让你们知道该往什么方向努力。
[Character(name="char_124_kroos_1")]
[name="克洛丝"]     哇，好不爽，这个人一脸正经地在说自己比我强，偏偏我还没法反驳！
[Character(name="char_013_riop")]
[name="格瑞斯教官"]     认真地说，你们也好，其他预备组也好，现在距离我们这一批教官确实还有不小的差距。
[name="格瑞斯教官"]     我们的存在意义之一，就是为你们提供一个背影。
[name="格瑞斯教官"]     而你们可能自己没有发现，现在的你们，和刚进入罗德岛时的你们相比，已经有了非常大的进步了。
[Character(name="char_123_fang_1")]
[name="芬"]     ......确实。
[Character(name="char_122_beagle_1")]
[name="米格鲁"]     嗯......这么说的话，确实呢。
[Character(name="char_013_riop")]
[name="格瑞斯教官"]     而且啊，说真的，你们算好了，负责你们的教官都是你们各自擅长领域的。
[name="格瑞斯教官"]     你们知道我们这批教官当时是怎么过来的吗？
[Character(name="char_124_kroos_1")]
[name="克洛丝"]     难道说......
[Character(name="char_013_riop")]
[name="格瑞斯教官"]     没错，我们是被杜宾一个人调教过来的。
[name="格瑞斯教官"]     你们可能无法想象，现在的杜宾，已经比过去的她温柔一百倍了。
[Character(name="char_124_kroos_1")]
[name="克洛丝"]     什么？现在的杜宾老师？温柔？
[name="克洛丝"]     你在说什么笑话吗，格瑞斯大叔。
[Character(name="char_013_riop")]
[name="格瑞斯教官"]     我可没在开玩笑。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]     格瑞斯，你是不是饭没吃饱！这点负重就让你跑不动了吗？
[name="杜宾"]     法伦，好好想想，如果你的敌人看到你刚才那拙劣又耿直的攻击会怎么想！
[name="杜宾"]     苔丝，你是不是睡着了？扶正你的枪把！别让我离开你的准心！
[name="杜宾"]     维克多，敌人不会给你施法完喝口水的空挡！
[name="杜宾"]     丽雅，我建议你在尝试练习治疗法术前，先学会急救的手法，你包扎的手法很配你手忙脚乱的样子！
[name

... (全文24337字符)
```


## 统计

- 总字符数：155276
- 对话行数：1976


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
