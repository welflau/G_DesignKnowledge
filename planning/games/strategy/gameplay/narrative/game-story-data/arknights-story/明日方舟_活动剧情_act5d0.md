# 明日方舟 · 活动剧情 · act5d0（29段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act5d0」完整剧情脚本（29个文件，2879行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act5d0
- 脚本文件数：29

### level_act5d0_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
[Character]
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_motorway",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
6:44 P.M.    天气/晴
龙门绕城公路，车内
[dialog]
[Delay(time=1)]
[Character(name="avg_npc_029",fadetime=0.7,block=true)]
[Delay(time=1)]
[name="管家"]   少爷？
[name="管家"]   少爷，您睡着了？
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Image(image="ac5_1",xScale=0.9, yScale=0.9, fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[ImageTween(xFrom=0, yFrom=0, xTo=-30, yTo=0, xScale=0.9, yScale=0.9, duration=15, block=false)]
[name="拜松"]   唔，抱歉......我们到哪儿了？
[name="管家"]   就快到约定的碰头地点了，请打起精神来，少爷。企鹅物流的诸位已经在等着了。
[name="拜松"]   嗯，我知道。
[name="管家"]   您看上去很疲惫。
[name="拜松"]   没有的事。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image(fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[delay(time=0.5)]
[Character(name="avg_npc_029",name2="char_325_bison_1",fadetime=0.7)]
[delay(time=0.7)]
[Character(name="avg_npc_029",name2="char_325_bison_1",focus=1)]
[name="管家"]   请原谅我多嘴，但老爷这次的决定实在是有些仓促，如果少爷有什么难处，请务必开口。
[Character(name="avg_npc_029",name2="char_325_bison_1#2",focus=2)]
[name="拜松"]   ......父亲，一定有他自己的想法。
[name="拜松"]   而且，只要能在企鹅物流有所作为，父亲身边的那些人，说不定就不会再阻拦我了。
[Character(name="avg_npc_029",name2="char_325_bison_1#2",focus=1)]
[name="管家"]   少爷是家族有史以来最年轻的信使，您的工作能力无可挑剔，这就足够了。
[Character(name="avg_npc_029",name2="char_325_bison_1#2",focus=2)]
[name="拜松"]   也许吧，但是，那些大人们未必会这么想。
[Character(name="avg_npc_029#2",name2="char_325_bison_1#2",focus=1)]
[name="管家"]   少爷......
[Character(name="avg_npc_029#2",name2="char_325_bison_1",focus=2)]
[name="拜松"]   看看窗外，现在龙门大半的民营信使业务已经落到了父亲的手里。
[name="拜松"]   企鹅物流，他们是最后的，也是最独立的，奇怪传闻最多的公司。
[name="拜松"]   虽然父亲和大帝先生的关系好像很好，可我们必须了解他们，至少我得这么做。
[Character(name="avg_npc_029",name2="char_325_bison_1",focus=1)]
[name="管家"]   所以我才会担心少爷，企鹅物流太过于特殊了，我很清楚。
[Character(name="avg_npc_029",name2="char_325_bison_1",focus=2)]
[name="拜松"]   你不用总摆出这么一副表情。我可以自己处理好。
[Character(name="avg_npc_029#3",name2="char_325_bison_1",focus=1)]
[name="管家"]   您也是，少爷。多像同龄人一样笑一笑吧。
[name="管家"]   今晚是安魂夜，您本可以和朋友们一起去街上逛逛。
[Character(name="avg_npc_029#3",name2="char_325_bison_1#3",focus=2)]
[name="拜松"]   ......你是在嘲笑我没朋友吗？
[Character(name="avg_npc_029#3",name2="char_325_bison_1#3",focus=1)]
[name="管家"]   岂敢，岂敢，哈哈哈。
[dialog]
[Delay(time=2)]
[stopmusic(fadetime=1)]
[Character(name="avg_npc_029",name2="char_325_bison_1#3",focus=1)]
[name="管家"]   抱歉，少爷，您的盾还在手边吗？
[Character(name="avg_npc_029",name2="char_325_bison_1",focus=2)]
[name="拜松"]   怎么？
[Character(name="avg_npc_029",name2="char_325_bison_1",focus=1)]
[name="管家"]   我们被盯上了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[name="甘比诺"]   发现目标，准备好了吗？
[dialog]
[Character(name="avg_npc_031",fadetime=0.7,block=true)]
[Delay(time=0.7)]
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.8, crossfade=1.5)]
[name="黑帮"]   呃，引爆组的导火索似乎有点短......
[Character]
[name="甘比诺"]   那不是问题，动手。
[Dialog]
[Character]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_029",name2="char_325_bison_1#4",focus=2)]
[name="拜松"]   唔——爆炸！？
[Character(name="avg_npc_029",name2="char_325_bison_1#4",focus=1)]
[name="管家"]   少爷，抓稳了——
[dialog]
[Character]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Character(name="avg_npc_031")]
[name="黑帮"]   发现目标，还活着。
[Character]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[name="甘比诺"]   把他带走，动作快。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1.5, block=true)]
[name="拜松"]   （居然炸毁了公路.....？到底，是谁......）
[name="拜松"]   （该死，视野......看不清......）
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[name="甘比诺"]   情况怎么样？
[Character(name="avg_npc_031")]
[name="黑帮"]   目击者很多，但没有看见其他目标人员。
[name="黑帮"]   等等，烟雾里还有其他人！
[Character]
[name="甘比诺"]   还有幸存者？那就一起——
[Character(name="avg_npc_031")]
[Dialog]
[PlaySound(key="$pistol", volume=0.9)]
[CameraShake(duration=1, xstrength=15, ystrength=10, vibrato=30, randomness=90, fadeout=true,block=true)]
[name="黑帮"]   唔呃——
[dialog]
[Character]
[delay(time=0.4)]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[name="甘比诺"]   喂？喂！
[name="甘比诺"]   这么简单就被干掉了？
[name="甘比诺"]   嘁，我可不喜欢这么老套的电影戏码。
[name="甘比诺"]   企鹅物流。 
[Character]
[name="？？？"]   哟，看来你很清楚嘛。
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_103_angel_1#3",fadetime=2,block=true)]
[Delay(time=2)]
[name="能天使"]  不过在我看来，在边郊公路中央设置路障再埋下炸弹，这手法也是相当复古哦？
[Character]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[name="甘比诺"]   爆破只是个人爱好，环顾一下你的周围，事情没这么简单。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Character(name="avg_npc_031",name2="avg_npc_031",fadetime=2,block=true)]
[Delay(time=2)]
[Character]
[PlaySound(key="$d_gen_walk_n",volume=0.5)]
[Character(name="avg_npc_027#2",fadetime=1,block=true)]
[Delay(time=1)]
[name="卡彭

... (全文14753字符)
```

### level_act5d0_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Dialog]
[Character]
[PlaySound(key="$d_gen_dooropen")]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_pgbase_1",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=2, block=true)]
[PlayMusic(intro="$penguinlogistics_intro", key="$penguinlogistics_loop", volume=0.8, crossfade=1.5)]
7:10 P.M.    天气/晴
企鹅物流据点，糟糕的室内
[Dialog]
[Delay(time=1)]
[Character(name="char_325_bison_1")]
[name="拜松"]   这里就是企鹅物流的据点......
[name="拜松"]   （好乱，而且好暗。）
[Character(name="char_102_texas_1",name2="char_325_bison_1#2",focus=1)]
[name="德克萨斯"]   只是我们的据点之一，没怎么好好收拾，随意坐吧。
[Character(name="char_102_texas_1",name2="char_325_bison_1",focus=2)]
[name="拜松"]   啊，谢谢......我好像还没有正式向你们道谢，企鹅物流的各位。
[Character(name="char_102_texas_1",name2="char_325_bison_1",focus=1)]
[name="德克萨斯"]   只是工作，先做个自我介绍好了。
[Character(name="char_325_bison_1#3")]
[name="拜松"]   ——信使，代号拜松，来自龙门峯驰物流，受家父指教，前来贵司参观学习，请多关照。
[name="拜松"]   关于我与大帝先生的合同内容，虽然之前已经确认过了，但还是......
[Character(name="char_105_emper")]
[name="大帝"]   慢着，我有个小问题，你那五大三粗的爹是怎么把你养得这么——
[Character(name="char_102_texas_1#2")]
[name="德克萨斯"]   ......老板。
[Character(name="char_105_emper")]
[name="大帝"]   好，好，你继续。
[Character(name="char_325_bison_1#4")]
[name="拜松"]   咳，关于刚才的袭击，无疑是对峯驰物流和企鹅物流的挑衅。
[name="拜松"]   这件事情绝不能轻视，如果有必要的话，我会通知家父和近卫局，此事应当被视作一起恶性袭击——
[Character(name="char_102_texas_1",name2="char_105_emper",focus=2)]
[name="大帝"]   喂，德克萨斯。
[Character(name="char_102_texas_1",name2="char_105_emper",focus=1)]
[name="德克萨斯"]   嗯？
[Character(name="char_102_texas_1",name2="char_105_emper",focus=2)]
[name="大帝"]   晚上吃什么？
[Character(name="char_103_angel_1#8")]
[name="能天使"]   欢迎派对！还用问吗？但是空去哪儿了，不是留下看家了吗？
[Character(name="char_103_angel_1#8",name2="char_201_moeshd#3",focus=2)]
[name="可颂"]   反正只要德克萨斯联系她的话，她立刻就能赶回来吧。
[Character(name="char_201_moeshd")]
[name="可颂"]   啊，抱歉，你接着说。
[Character(name="char_325_bison_1#2")]
[name="拜松"]   （空？）
[Character(name="char_325_bison_1#4")]
[name="拜松"]   ......咳，当务之急是调查那些袭击我们的敌人，企鹅物流的各位有什么头绪吗？
[Character(name="char_325_bison_1#4",name2="char_103_angel_1#7",focus=2)]
[name="能天使"]   头绪？不就是普通的业务纠纷吗？
[Character(name="char_325_bison_1#2",name2="char_103_angel_1#7",focus=1)]
[name="拜松"]   呃，业务纠纷......？
[Dialog]
[Character(name="char_105_emper")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[name="大帝"]   德克萨斯！我抽屉里的雪茄呢！？
[Character(name="char_103_angel_1#8",name2="char_105_emper",focus=1)]
[name="能天使"]   老板，我们已经好久没回过这个据点了，恐怕早就发霉了。
[Character(name="char_102_texas_1",name2="char_105_emper",focus=1)]
[name="德克萨斯"]   空来打扫过，可能那时候扔掉了吧。
[Character(name="char_105_emper")]
[name="大帝"]   啊，那我今天晚上会死的，不行，这可不行......
[name="大帝"]   啊，你继续，别在意。
[Character(name="char_325_bison_1#4")]
[name="拜松"]   首先我们应该明确敌人的目的——
[Dialog]
[Character(name="char_105_emper")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[name="大帝"]   慢着，音乐！我的黑胶唱片！是不是放了一箱在这里？
[Character(name="char_201_moeshd#4")]
[name="可颂"]   啊，好像是我搬来的。那一箱得有我好几个月薪水。
[Character(name="char_103_angel_1#3",name2="char_105_emper",focus=1)]
[name="能天使"]   在这儿，要听哪张？
[Character(name="char_103_angel_1#3",name2="char_105_emper",focus=2)]
[name="大帝"]   随便哪张都行，被我选中的只会是宇宙末日级精品。
[Character(name="char_105_emper")]
[name="大帝"]   啊，音乐，有了艺术的人生才不会无聊，赞美音乐，以及我自己！
[name="大帝"]   拜松，接着说。
[Character(name="char_325_bison_1#2")]
[name="拜松"]   ......我、我说到哪了？
[Character(name="char_325_bison_1#2",name2="char_105_emper",focus=2)]
[name="大帝"]   他们的目的。
[Character(name="char_325_bison_1#4",name2="char_105_emper",focus=1)]
[name="拜松"]   对！他们的目的应该是我，也许，是为了挑拨贵司与我司的关系。
[Character(name="char_325_bison_1#4",name2="char_105_emper",focus=2)]
[name="大帝"]   什么啊，这点小事，还以为只是给之前的事情报仇......
[Character(name="char_325_bison_1#4",name2="char_105_emper",focus=1)]
[name="拜松"]   您有什么线索吗？
[Character(name="char_102_texas_1",name2="char_105_emper",focus=2)]
[name="大帝"]   ——咳咳！德克萨斯！去调查一下他们！
[Character(name="char_102_texas_1#2",name2="char_105_emper",focus=1)]
[name="德克萨斯"]   加班费，三倍。
[Character(name="char_103_angel_1#7")]
[name="能天使"]   唔，这种程度的打架每个月都会有个十七八次啦。信使不都是这样工作的吗？
[Character(name="char_325_bison_1#2",name2="char_103_angel_1#7",focus=1)]
[name="拜松"]   ......为什么？
[name="拜松"]   信使不是应该更加隐秘一点，迅速一点......从来不是以武力为标准的啊。
[Character(name="char_325_bison_1#2",name2="char_103_angel_1#7",focus=2)]
[name="能天使"]   是这样的吗？
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   ......我们明明是个物流公司，为什么总是被卷进帮派斗争里去？
[Character(name="char_105_emper")]
[name="大帝"]   因为他们的品味太低，对自己生而为人的品位太低。
[Character(name="char_201_moeshd")]
[name="可颂"]   也因为老板发我们薪水嘛。不过还是有在遵纪守法地运送货物啦。
[name="可颂"]   只是大部分时候都会变成武装运送而已。
[Character(name="char_103_angel_1#8")]
[name="能天使"]   对嘛，这有什么问题吗？
[Character(name="char_325_bison_1#4")]
[name="拜松"]   ......？这真的没问题吗？
[Character(name="char_102_texas_1#2")]
[name="德克萨斯"]   唉......
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   先等等。
[name="德克萨斯"]   这里，是空留下的密码。
[Dialog]
[Character]
[Delay(time=0.5)]
[Character(name="char_325_bison_1#2")]
[name="拜松"]   饼、饼干？
[Character(name="char_103_angel_1#6",name2="char_102_texas_1",focus=1)]
[name="能天使"]   啊，干嘛要打开了放在这里，受潮了就不好吃了。
[Character(name="char_103_angel_1#6",name2="char_102_texas_1",focus=2)]
[name="德克萨斯"]   有巧克力的一面是长，尾巴是短，这是密码。
[Character(name="char_325_bison_1#2")]
[name="拜松"]   （这是什么独特的密码学......）
[Character(name="char_201_moeshd#2")]
[name="可颂"]   什么？那时候是当真的吗？不是玩笑？
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   ......我只是普通地记下了空的话。
[name="德克萨斯"]   “可疑分子”，唔，空可能追出去了。
[Character(name="char_105_emper")]
[name="大帝"]   随她去吧，已经到下班时间了。
[name="大帝"]   今天可是安魂夜，没有加班，没有资本主义的压迫，否则死人都难安心。
[name="大帝"]   晚上谁想去喝一杯？
[Character(name="char_201_moeshd",name2="char_105_emper",focus=1)]
[name="可颂"]   啊，莫非老板请客？上次才进了一批价格不菲的藏酒~
[Character(name="char_201_moeshd",name2="char_105_emper",focus=2)]
[name="大帝"]   完全没问题，反正你们几个有大把的薪水可以扣。
[Character(name="char_201_moeshd#5",name2="char_105_emper",focus=1)]
[name="可颂"]   那算了！
[Character(name="char_325_bison_1#4",name2="char_105_emper",focus=1)]
[name="拜松"] 

... (全文8573字符)
```

### level_act5d0_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[stopmusic]
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[dialog]
[Delay(time=0.4)]
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.8, crossfade=1.5)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_201_moeshd#5")]
[name="可颂"]   咳咳，咳，大家还好吗？
[Character(name="char_325_bison_1#4",name2="char_201_moeshd#5",focus=1)]
[name="拜松"]   勉强，挡住了——
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   及时的反应，二位。
[Character(name="char_103_angel_1#4")]
[name="能天使"]   哎呀，这可......炸得真彻底啊。嗯？
[Dialog]
[Character(name="char_105_emper")]
[stopmusic(fadetime=1)]
[CameraShake(duration=2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true,block=false)]
[name="大帝"]   ————*难以名状的企鹅尖啸*————
[Character(name="char_103_angel_1#4",name2="char_201_moeshd#5",focus=2)]
[name="可颂"]   （怎、怎么了？老板发出很奇怪的声音喔！？）
[Character(name="char_103_angel_1#7",name2="char_201_moeshd#5",focus=1)]
[name="能天使"]   （喂！刚才那箱黑胶唱片是不是老板从黑市上淘来的哥伦比亚珍藏品？）
[Character(name="char_103_angel_1#7",name2="char_201_moeshd#4",focus=2)]
[name="可颂"]   （好像是的，怎么办，我已经很久没有见过老板这种万物皆空的表情了......）
[Character]
[dialog]
[Character(name="avg_npc_031",name2="avg_npc_031")]
[Delay(time=1)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Character(fadetime=1,block=true)]
[Delay(time=2)]
[Character(name="char_103_angel_1#7",name2="char_201_moeshd#5",focus=1)]
[name="能天使"]   什么怎么办——啊！他们上车了！那群穿黑衣服的家伙！
[Character(name="char_325_bison_1#4")]
[name="拜松"]   等等！可如果他们一开始就设好了陷阱，为什么不埋伏我们？情况古怪，我们应该定制一个具体的计划再去——
[Character]
[Character(name="char_103_angel_1#8")]
[name="能天使"]   德克萨斯！
[Dialog]
[playsound(key="$sportscarstart")]
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   上车。
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.8, crossfade=1.5)]
[Character(name="char_105_emper")]
[name="大帝"]   ......你们，给我听好了。
[name="大帝"]   今晚的所有违章罚单全部报销。
[name="大帝"]   我要让他们，给我的黑胶陪葬啊啊啊——
[playsound(key="$drift")]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_motorway",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_201_moeshd#3")]
[name="可颂"]   看见了，就是前面那辆！
[Character(name="char_105_emper")]
[name="大帝"]   能天使！把我的老伙计拿来！
[Character(name="char_105_emper",name2="char_103_angel_1#8",focus=2)]
[name="能天使"]   得令！老板！
[Character(name="char_325_bison_1#2")]
[name="拜松"]   那是把铳枪！？但您要怎么扣扳机......
[Character(name="char_105_emper")]
[name="大帝"]   啊哈！见识不小嘛，小少爷，让我们的铳械专家来介绍一下！
[Character(name="char_105_emper",name2="char_103_angel_1#8",focus=2)]
[name="能天使"]   总计四十二层运输纸板，工业胶水无缝粘贴，高质量橡皮筋驱动，嗯，真是一把不错的铳枪。
[Character(name="char_325_bison_1#2")]
[name="拜松"]   ......就是说，玩具？
[Character(name="char_105_emper",name2="char_103_angel_1#8",focus=2)]
[name="能天使"]   其实就是弹弓——痛！不对，是和平铳枪！
[Character(name="char_105_emper",name2="char_103_angel_1#8",focus=1)]
[name="大帝"]   在龙门市区不允许使用实弹，这是规矩。
[Character(name="char_102_texas_1#2")]
[name="德克萨斯"]   每次我都在想，老板只有在这个时候遵守规矩呢。
[Character(name="char_102_texas_1#2",name2="char_105_emper",focus=2)]
[name="大帝"]   如果连我们都不守规矩了，龙门立刻就会被炸上天，明白吗？打开车篷，德克萨斯！
[Character(name="char_102_texas_1",name2="char_105_emper",focus=1)]
[name="德克萨斯"]   注意点。不要像上次那样撞在信号灯上了。
[Character(name="char_102_texas_1",name2="char_105_emper",focus=2)]
[name="大帝"]   我有那么高吗？
[Character(name="char_105_emper",name2="char_103_angel_1#5",focus=2)]
[name="能天使"]   二号狙击位准备就绪，老板~！
[Character(name="char_325_bison_1#4")]
[name="拜松"]   等、等等，路上还有其他的车辆，我们难道就直接——
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$p_atk_smg_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$p_atk_smg_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[name="开车的黑帮"]   那帮家伙开火了！喂，还击啊！
[name="后座的黑帮"]   开什么玩笑，车开得这么颠簸怎么瞄准！
[PlaySound(key="$pistol", volume=0.9)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="开车的黑帮"]   你、你中弹了！？
[name="后座的黑帮"]   血，我流血了，快给我绷带——不对，这是什么，橡皮？
[name="开车的黑帮"]   只是橡皮！？
[name="后座的黑帮"]   但这橡皮能打穿玻璃！快甩开他们、啊，好疼！！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_105_emper",name2="char_103_angel_1#8",focus=2)]
[name="能天使"]   准头不错，老板！
[Character(name="char_102_texas_1",name2="char_105_emper",focus=2)]
[name="大帝"]   咬紧他们，德克萨斯！
[Character(name="char_102_texas_1#4",name2="char_105_emper",focus=1)]
[name="德克萨斯"]   要加速了。
[Character(name="char_325_bison_1#4")]
[name="拜松"]   慢点，小心前面的货车——噫——
[Character(name="char_201_moeshd")]
[name="可颂"]   抓稳点喔，德克萨斯姐飙起车来是不讲情面的。
[Character]
[Dialog]
[Character(name="char_105_emper",name2="char_103_angel_1#5",focus=1)]
[name="大帝"]   阿能，打爆他们的车胎！
[Character(name="char_105_emper",name2="char_103_angel_1#5",focus=2)]
[name="能天使"]   收到！
[Character(name="char_325_bison_1#4")]
[name="拜松"]   用橡皮弹打橡胶车胎！？
[Character(name="char_105_emper")]
[name="大帝"]   只要我想，就能做到。
[Dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$pistol

... (全文8780字符)
```

### level_act5d0_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Background(image="bg_park",screenadapt="coverall", fadetime=1)]
[Dialog]
[Character]
[Delay(time=1)]  
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.8, crossfade=1.5)]
7:16 P.M.    天气/晴
龙门中央公园，鳞鱼丸小摊
[dialog]
[Character(name="char_272_strong_1#3",fadetime=2,block=true)]
[Delay(time=2)]
[name="孑"]   您点的鱼丸。
[Character(name="avg_npc_032")]
[name="女性游客"]   哦哦，这口感，弹性，真不错。
[name="女性游客"]   不愧是百大民间美食攻略推荐的店家！
[Character(name="char_272_strong_1#3")]
[name="孑"]   客人喜欢就好。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_032",name2="avg_npc_033",focus=2)]
[name="男性游客"]   ......
[name="男性游客"]   ......哎，你不觉得那个店主有点可怕吗？
[Character(name="avg_npc_032",name2="avg_npc_033",focus=1)]
[name="女性游客"]   就是说啊，凶神恶煞的不讲，明明在卖鱼丸，为什么桌上要放把菜刀啦......
[Character(name="avg_npc_032",name2="avg_npc_033",focus=2)]
[name="男性游客"]   而且我看攻略上说，店主是个号称鱼丸之神的老伯伯才对啊。
[name="男性游客"]   啊，该不会是黑社会抢了摊子......
[Character(name="char_272_strong_1")]
[name="孑"]   嗯？客人，还有什么需要吗？
[Character(name="avg_npc_032")]
[name="女性游客"]   没、没事。
[Dialog]
[Character(fadetime=2,block=true)]
[Character(name="char_272_strong_1")]
[name="孑"]   ......最近的客人真奇怪。
[Character]
[name="？？？"]   还不是因为你的表情太凶了。
[Character(name="char_243_waaifu_1",fadetime=2,block=true)]
[Delay(time=2)]
[name="槐琥"]   还有你干嘛穿着这身就来看摊？你就不能为董阿伯的名声考虑一下吗？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   是你喔，打工结束了？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   算是吧。事务所那边说上次在你这儿赊了账，多少来着？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   三十二块六，零头抹了吧。要尝尝吗？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=2)]
[name="槐琥"]   突然干嘛，我可没带多余的零钱。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=1)]
[name="孑"]   就当是慰问品收下吧，毕竟你们总是照顾我生意。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   那，我就不客气了。
[name="槐琥"]   唔嗯......
[name="槐琥"]   好吃是好吃，但这不是阿伯的摊子吗？借花献佛？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   干嘛总是要挑我刺，我会自掏腰包的......
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   那就好。不过你的手艺的确有进步，要是那群家伙像你这样认真对待自己的工作该多好。
[Dialog]
[Character]
[name="？？？"]   您好，一份鱼丸。
[Character(name="char_272_strong_1#3")]
[name="孑"]   啊，好的，客人请稍等。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Image(image="ac5_3",screenadapt="coverall", fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[name="？？？"]   没关系，我不赶时间。这里能远远看到江景，很难得。
[name="？？？"]   香味真不错，这本美食攻略还是挺靠谱的嘛。
[name="槐琥"]   ......
[name="孑"]   ......久等了。这是找零。
[name="？？？"]   谢谢。
[name="孑"]   客人请慢走。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image(fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Dialog]
[Character]
[Delay(time=0.5)]
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#2",focus=1)]
[name="孑"]   槐琥？你在看什么？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=2)]
[name="槐琥"]   不，那位小姐总让人觉得有点怪怪的......萨科塔人会长角的吗？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=1)]
[name="孑"]   安魂夜化妆吧。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   不太像，算了，无端揣测他人可不是什么好习惯。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   接下来你打算干什么？回事务所？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   回去复习，过两天有考试。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   在安魂节当天还要念书？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=2)]
[name="槐琥"]   安魂节是恭送灵魂的节日，现代社会对于节日的定义基本就是消费，敬谢不敏。
[name="槐琥"]   重点是，我可没那么多薪水，倒不如说我更希望绩点高一点，还能拿到奖学金。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=1)]
[name="孑"]   呃，好吧，倒像是你的作风......
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=2)]
[name="槐琥"]   是那些家伙和社会脱节太久了。可不要把我看作那种人。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[stopmusic(fadetime=2)]
[Character(name="char_213_mostma_1")]
[name="？？？"]   嗯，时间应该还有很多，下一家该去哪里呢？让我看看，唔，这附近还有......
[Character]
[Dialog]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[name="好奇的龙门市民"]   喂！立交桥上发生什么了？是车祸吗？
[name="散步的龙门市民"]   好像不是简单的车祸，去不去凑个热闹？
[name="闲散的龙门市民"]   又打架喔？凑热闹算我一个！
[Dialog]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[name="黑帮"]   你们这群疯子，离我远点啊啊啊——
[Dialog]
[Delay(time=1)]
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.8, crossfade=1.5)]
[Character(name="char_213_mostma_1#1")]
[name="？？？"]   ......唔，这么快？
[Character(name="char_213_mostma_1#2")]
[name="？？？"]   看来要提前上工了呢。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_motorway",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_325_bison_1#4",fadetime=1,block=true)]
[Delay(time=1)]
[name="拜松"]   疼......我，被甩出来了......？
[Character]
[name="黑帮A"]   幸好栏杆够结实，不然冲出立交桥铁定完蛋。
[name="黑帮B"]   喂，帮我一把！把我拉出去！
[Character(name="char_325_bison_1#4")]
[name="拜松"]   他们要逃了，各位！我们得立刻追上去！
[CameraShake(duration=0.4, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character]
[name="能天使"]   唔唔唔，可这个，安全气囊，太，挤了！
[name="大帝"]   别乱动！我的老伙计要被压扁了！喂！可颂！扣你工资喔！
[name="可颂"]   可我、我动不了呀，德克萨斯姐压着我的腿了！
[name="德克萨斯"]   唉。
[Character(name="char_325_bison_1#4")]
[name="拜松"]   嘁，那就

... (全文9205字符)
```

### level_act5d0_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Character]
[Delay(time=1)]
[name="拜松"]   我被击落了？从桥上？
[name="拜松"]   离地面有多高？敌人从哪里发动的攻击？
[name="拜松"]   不，比起那个，我现在应该——！
[Background(image="bg_park",screenadapt="coverall",fadetime=1)]
[Dialog]
[Delay(time=1)]  
[Character(name="char_325_bison_1#4")]
[CameraShake(duration=0.3, xstrength=8, ystrength=6, vibrato=20, randomness=20, fadeout=true, block=false)]
[name="拜松"]   唔——！
[name="拜松"]   噗哈！
[Character(name="char_325_bison_1#2")]
[name="拜松"]   得、得救了。这是......？呃，好黏。
[name="拜松"]   是安魂夜的装饰蜡烛？谢天谢地，正好堆在这里......
[Character(name="char_213_mostma_1")]
[name="？？？"]   你角上也卡着一支喔。
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   呃？谢、谢谢，得把这个拔下来，唔——！
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1",focus=2)]
[name="？？？"]   蜡烛先生，先不要动。
[name="？？？"]   安静，躲到箱子后面去。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Character(name="avg_npc_031",name2="avg_npc_031",focus=1)]
[name="黑帮"]   弗伦佐的通讯断了，应该就在这附近！
[Character(name="avg_npc_031",name2="avg_npc_031",focus=2)]
[name="黑帮"]   企鹅物流也在这儿，发现目标立刻通知首领！
[Dialog]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Character(fadetime=1)]
[Delay(time=1)]
[Character(name="char_213_mostma_1")]
[name="？？？"]   可以出来了。
[Character(name="char_325_bison_1#4",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   啊、好......
[name="拜松"]   虽然很感谢你的帮助，但我不能把你卷进来，所以请快点离开这里。
[Character(name="char_325_bison_1#4",name2="char_213_mostma_1",focus=2)]
[name="？？？"]   我也想啊，难得回一趟龙门，但毕竟有委托嘛......
[Character(name="char_325_bison_1#4",name2="char_213_mostma_1#3",focus=2)]
[name="？？？"]   看你这幅狼狈样，和企鹅物流打交道很辛苦吧？
[Character(name="char_325_bison_1#4",name2="char_213_mostma_1#3",focus=1)]
[name="拜松"]   ......很辛苦。
[name="拜松"]   那么，你是谁？你不是普通的路人吧？
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=2)]
[name="？？？"]   也不用这么紧张，总之，我不是你的敌人。
[name="？？？"]   等等，他们又来了，先躲好。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_031",name2="avg_npc_031",focus=1)]
[name="黑帮A"]   娘咧，弗伦佐果然被企鹅物流抓到了。我们怎么办？
[Character(name="avg_npc_031",name2="avg_npc_031",focus=2)]
[name="黑帮B"]   那个叫拜松的丰蹄小子落单了，这是个大好机会。
[Character(name="avg_npc_031",name2="avg_npc_031",focus=1)]
[name="黑帮A"]   但这里已经是市区了，我们还能动手吗？
[Character(name="avg_npc_031",name2="avg_npc_031",focus=2)]
[name="黑帮B"]   卡彭先生都考虑过了，只要不动明火，做得隐秘一点，龙门是不会管的。
[name="黑帮B"]   没有人会特地去关照那些散发着垃圾臭味的小街暗巷吧？
[Character(name="avg_npc_031",name2="avg_npc_031",focus=1)]
[name="黑帮A"]   明白了，那我们去救人，你们去找人，没问题吧？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_213_mostma_1")]
[name="？？？"]   看来这里已经不能久留了呢，我们得离开这里。
[name="？？？"]   让我看看......在那儿呢，打个招呼吧。
[Dialog]
[Character]
[PlayMusic(intro="$marketplace_intro", key="$marketplace_loop", volume=0.8, crossfade=4)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Blocker(a=0, fadetime=1.5, block=true)]
[Character(name="char_105_emper",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]   老板，找到拜松了吗？
[Character(name="char_105_emper",name2="char_201_moeshd#2",focus=1)]
[name="大帝"]   我戴的是墨镜，不是望远镜，别催我！
[Character(name="char_105_emper")]
[name="大帝"]   啊......看见了。在向我招手呢。
[Character(name="char_103_angel_1#8")]
[name="能天使"]   那我们快去把他接回来吧，然后再来问问这个家伙，他们在打什么主意。
[Character(name="avg_npc_031")]
[CameraShake(duration=0.3, xstrength=8, ystrength=6, vibrato=20, randomness=20, fadeout=true, block=false)]
[name="黑帮"]   唔——唔唔——
[Character(name="char_105_emper")]
[name="大帝"]   不。
[name="大帝"]   看来我们幸运的实习生恰好摔在了一个安全的地方，他会自己回来的。
[Character(name="char_105_emper",name2="char_201_moeshd#4",focus=2)]
[name="可颂"]   嗯......从十二米高空自由落体到了一个安全的地方？怎么个安全法？
[Character(name="char_103_angel_1#7",name2="char_105_emper",focus=1)]
[name="能天使"]   而且他也是敌人的目标之一喔，真的不管他吗？
[Character(name="char_105_emper")]
[name="大帝"]   有她在。
[Character(name="char_103_angel_1#6")]
[name="能天使"]   ......她回来了？
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   能天使，别分神。
[Dialog]
[Character]
[name="黑帮"]   他们在那里！去把弗伦佐救回来！
[Character(name="char_103_angel_1#3")]
[name="能天使"]   哎呀，好像的确有点抽不开身呢。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Blocker(a=0, fadetime=1.5, block=true)]
[Character(name="char_213_mostma_1")]
[name="？？？"]   热热闹闹地走掉了。
[name="？？？"]   所以，德克萨斯他们又惹了什么麻烦？这次是和谁打架？
[Character(name="char_325_bison_1#4",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   我该信任你吗？
[Character(name="char_325_bison_1#4",name2="char_213_mostma_1",focus=2)]
[name="？？？"]   也是，自我介绍一下，我是企鹅物流的信使，莫斯提马。
[Character(name="char_325_bison_1#4",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   权且算是你的同行吧，不过我更喜欢自己行动多一点。
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   ......莫斯提马，我在父亲那里听过这个名字。
[name="拜松"]   （而且，长着漆黑双角的萨科塔......原来这个传闻是真的，不，还是不要问了吧......）
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   嗯......好事还是坏事呢？
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   不，怎么说，都是些不可思议的传闻......
[name="拜松"]   而且你刚才帮了我，也许我不该怀疑你的，抱歉。
[Character(name="char_325_bison_1",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   没关系的，你不用这么拘谨。
[Character(name="char_325_bison_1",name2="char_213_mostma_1#3",focus=1)]
[name="拜松"]   谢谢......总之，我们应该先共享一下情报......虽然我也是一头雾水。
[name="拜松"]   ......简而言之，企鹅物流和一支叙拉古黑手党发生了矛盾。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   嗯，我大概明白了。
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   欸？这就明白了？
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   没必要顾虑那么多，适当地放弃思考，放纵本心，才能跟上企鹅物流的节奏喔。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   呃，原来诀窍是放弃思

... (全文8083字符)
```

### level_act5d0_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Dialog]
[Character]
[PlayMusic(intro="$marketplace_intro", key="$marketplace_loop", volume=0.8, crossfade=2)]
[Background(image="bg_lmstreet_1",screenadapt="coverall", fadetime=1)]
[Dialog]
[Character]
[Delay(time=1)] 
[Character(name="char_272_strong_1")]
[name="孑"]   呼啊——都这个点了......赶紧回去睡觉......
[name="孑"]   唔，如果在这里开个海鲜摊，这客流量可真不得了啊。唔？那是？
[Dialog]
[Character]
[Delay(time=0.3)]
[Character(name="char_243_waaifu_1#4")]
[name="槐琥"]   ......
[Character(name="char_272_strong_1")]
[name="孑"]   喂~
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=2)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[name="槐琥"]   休想得逞！
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=1)]
[name="孑"]   是我，是我啊，放手！
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#2",focus=2)]
[name="槐琥"]   什么嘛，你怎么在这里。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#2",focus=1)]
[name="孑"]   ......收摊回家的路上。
[name="孑"]   倒是你在这里发呆——不对，立刻就能反手擒拿好像也不算在发呆......
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=2)]
[name="槐琥"]   你听说刚才在立交桥上发生的车祸了吗？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=1)]
[name="孑"]   ......你不是应该在复习功课吗？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   劳逸结合，不然明天拿到试卷的时候脑袋一白就完蛋了。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   欸，好吧。
[name="孑"]   刚才好像听客人提到过，但愿没有伤亡。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   嗯......但我在事务所听说，这事儿和一群不干不净的家伙有关系......
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   先说好，我绝对和什么杀手、帮派之类的没有关系，你知道的对吧？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   你的事情大家早就清楚了——不如说你总是这幅态度，不被怀疑才奇怪吧？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   ......是喔，难怪。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=2)]
[name="槐琥"]   而且两个小时前还在龙门边郊的高速公路上发生了一起瓦斯爆炸。
[name="槐琥"]   高速公路上，瓦斯爆炸？这个理由也太滥用了点。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=1)]
[name="孑"]   呃。你该不会想......
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=2)]
[name="槐琥"]   我说了嘛，劳逸结合。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=1)]
[name="孑"]   ......哈，就知道。
[name="孑"]   但这算劳还是逸？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_325_bison_1",name2="char_213_mostma_1",fadetime=0.5,focus=2,block=true)]
[Delay(time=0.5)]
[name="莫斯提马"]   差不多了吧，再怎么说这里也是市中心，他们不可能行动自如。
[name="莫斯提马"]   你刚才点的是抹茶味的？那这份是你的，我请客。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   的确没看见什么可疑的家伙，可......我们是不是太悠闲了点？
[Character(name="char_325_bison_1",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   什么话，这可是五星推荐，比黑手党厉害多了吧？
[name="莫斯提马"]   你能联系得到德克萨斯他们吗？
[Character(name="char_325_bison_1",name2="char_213_mostma_1#3",focus=1)]
[name="拜松"]   不能，事出突然......
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   既然这样，那就更不着急了嘛。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   ......
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   你的冰淇淋要化了喔，别这么紧张兮兮的。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   啊，我只是......谁能料到事情会变成现在这样。我是应该冷静一下。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   黑手党们千里迢迢从叙拉古来到龙门，总不会只是为了参加安魂节狂欢吧？
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   ......他们有别的目的，其中之一，是我。但是更具体的，我还不清楚。
[name="拜松"]   敌明我暗，既然已经摆脱了追击，应该利用单独行动的优势调查事态的因果......
[name="拜松"]   可我们该怎么入手？应该找机会进行反追踪吗？不，还是应该优先和德克萨斯小姐取得联系......
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   呵呵，比起德克萨斯他们，你倒是更像个普通的信使。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   啊，抱歉，突然就开始自说自话。
[Character(name="char_325_bison_1",name2="char_213_mostma_1#2",focus=2)]
[name="莫斯提马"]   不，你说的没错。
[name="莫斯提马"]   既然我们都知道黑手党另有目的，的确不该轻举妄动。
[name="莫斯提马"]   只是偶尔也要相信一下德克萨斯她们，别看他们总是那样，企鹅物流可是很强的。
[name="莫斯提马"]   虽然用“强”来形容一个物流公司有点奇怪，嗯......算啦，反正我也没资格抱怨。
[name="莫斯提马"]   也许我们一边逛街，一边看看风景，等见到德克萨斯的时候，他们已经把敌人一网打尽了喔？
[Character(name="char_325_bison_1",name2="char_213_mostma_1#2",focus=1)]
[name="拜松"]   ......是，是这样吗？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_213_mostma_1#4")]
[name="莫斯提马"]   啊......
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1#4",focus=1)]
[name="拜松"]   莫斯提马小姐？
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1#4",focus=2)]
[name="莫斯提马"]   看见那家糖果店了吗？
[Character(name="char_325_bison_1",name2="char_213_mostma_1#4",focus=1)]
[name="拜松"]   与其说店，更像一个摊铺。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   嗯，有些年头了。
[name="莫斯提马"]   很多年前我刚来龙门的时候就来过这里。
[name="莫斯提马"]   那个时候呀......身上也没有龙门币，说实话，灰头土脸的，倒是一眼就被糖果吸引了。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   是......这样。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   只是单纯的长途跋涉，路上遇到了一点小麻烦。信使都是这样吧。
[name="莫斯提马"]   走，我们去看看。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   ......
[Dialog]
[Character]
[Delay(time=1)]
[name="小女孩"]   哇！是彩色的星星！
[name="小女孩"]   爷爷，你为什么能把星星摘下来？
[name="老人"]   这就是秘密了，可不能随随便便告诉你们。
[name="小男孩"]   这哪里是星星，不就是加了色素的水果糖嘛！
[name="小女孩"]   哎，可是这么好看的糖果真的很少见诶......你不想要吗？
[name="小男孩"]   啰、啰嗦！喂！有棉花糖吗？
[name="老人"]   有，怎么没有，来，伸手。
[name="小女孩"]   诶——但比起这点棉花糖，我还是想要那个......
[name="小男孩"]   我讨厌吃水果糖！太甜了！而且舌头会变成奇怪的颜色！
[name="老人"]   想要的话就一并拿去吧，难得的安魂夜，就不收你们钱了。
[name="老人"]   这么晚了，赶紧回家睡觉！
[name="小女孩"]   谢谢爷爷！
[na

... (全文10053字符)
```

### level_act5d0_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[Background(image="bg_lungmen_n",screenadapt="coverall", fadetime=1)]
7:59 P.M.    天气/多云
龙门人工河流，码头
[Dialog]
[Character]
[Delay(time=1)] 
[name="路人"]   下次不要再突然跳到船上了啊！很危险的！
[Character(name="char_325_bison_1#2")]
[name="拜松"]   对不起，事出有因才......
[name="拜松"]   请问刚才你有看见一位萨科塔人吗？
[Character]
[name="路人"]   我没看见啦，真是遭不住，这些糖果可是今晚的后夜派对要用的，要是耽误了你赔得起......唔？
[name="路人"]   萨、萨科塔......
[Dialog]
[Character(name="char_213_mostma_1")]
[Delay(time=1)]
[Character(name="char_325_bison_1")]
[name="拜松"]   啊！莫斯提马小——
[Character(name="char_101_sora_1#3")]
[name="空"]   莫斯提马？你认识莫斯提马？
[Character(name="char_325_bison_1",name2="char_101_sora_1#3",focus=1)]
[name="拜松"]   ......不好意思，是我认错人了。
[PlayMusic(intro="$marketplace_intro", key="$marketplace_loop", volume=0.8, crossfade=2)]
[name="拜松"]   （这个人，好像在哪里见过？）
[Character]
[name="路人"]   咳嗯，总之这次就先放过你了，下次不要再做这么危险的事情了！
[Character(name="char_325_bison_1")]
[name="拜松"]   抱、抱歉，真的是麻烦你了。
[Character(name="char_101_sora_1#4")]
[name="空"]   嗯......年轻的丰蹄......总觉得好像忘了什么......是什么呢......
[Character(name="char_101_sora_1#3")]
[name="空"]   啊！
[Character(name="char_325_bison_1#2",name2="char_101_sora_1#3",focus=1)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="拜松"]   哇！？你要做什么！？
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=2)]
[name="空"]   你的角上卡着一颗糖！
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=1)]
[name="拜松"]   啊，真的。是不是该还回去......
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=2)]
[name="空"]   还有，看到这对角，我想起来了！和那个峯驰的标志一模一样！
[name="空"]   你是峯驰物流的小少爷，对不对？
[Character(name="char_325_bison_1#2",name2="char_101_sora_1",focus=1)]
[name="拜松"]   小、小少爷......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=1)]
[name="拜松"]   空前辈，这条路真的能和德克萨斯小姐他们汇合吗？
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=2)]
[name="空"]   放心放心，德克萨斯在想什么，我可是一清二楚。
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=1)]
[name="拜松"]   是这样。
[name="拜松"]   ......这个声音总有种熟悉感，在哪里？
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=2)]
[name="空"]   “前辈”吗，嘿嘿，想不到我也会有带着信使后辈的一天~你对大家的印象如何？
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=1)]
[name="拜松"]   印象？
[Character]
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_pgbase_1",screenadapt="coverall")]
[Character(name="char_102_texas_1#2",name2="char_201_moeshd")]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_motorway",screenadapt="coverall")]
[Character(name="char_105_emper",name2="char_103_angel_1#8")]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_lmstreet_2",screenadapt="coverall",block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_325_bison_1#2",name2="char_101_sora_1#5",focus=1)]
[name="拜松"]   非常，呃，激动人心。
[Character(name="char_325_bison_1",name2="char_101_sora_1#5",focus=2)]
[name="空"]   啊哈哈......我大概能猜到什么情况了......
[dialog]
[Character]
[Character(name="char_101_sora_1#3")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[name="空"]   啊，抱歉！
[Character]
[name="孩子"]   走路注意点啊！嘁！
[Character(name="char_325_bison_1#4")]
[name="拜松"]   明明是你冲过来的——
[Character]
[name="孩子"]   啊？关你屁事？
[Character(name="char_325_bison_1#4")]
[name="拜松"]   你这小鬼！
[Character(name="char_325_bison_1#4",name2="char_101_sora_1#5",focus=2)]
[name="空"]   算啦算啦，随他去吧。
[Character(name="char_325_bison_1#4",name2="char_101_sora_1#5",focus=1)]
[name="拜松"]   可是他刚才顺走了你的钱包——
[Character(name="char_325_bison_1#4",name2="char_101_sora_1",focus=2)]
[name="空"]   嘿嘿，我知道哦，不过那个钱包里只装了南瓜糖就是了。你看，真正的钱包在这儿~
[name="空"]   “不给糖就捣蛋”嘛。
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=1)]
[name="拜松"]   可他是直接来捣蛋的，而且今天也不是......为什么要特地这么做？
[Character(name="char_325_bison_1",name2="char_101_sora_1#4",focus=2)]
[name="空"]   龙门最近经历了很多事情，虽然在今天不太看得出来。
[name="空"]   安魂夜的蜡烛照亮不到这座城市的所有角落，这些孩子也太可怜了点。
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=2)]
[name="空"]   诶嘿，不过说到底还是一时兴起啦，不错的主意吧？
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=1)]
[name="拜松"]   那如果被偷的是我可怎么办......
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=2)]
[name="空"]   前面出去，就到了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$penguinlogistics_intro", key="$penguinlogistics_loop", volume=1, crossfade=1.5)]
[Background(image="bg_park",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]  
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=1)]
[name="拜松"]   这里是......刚才的公园？又回到这里了？
[Character(name="char_325_bison_1",name2="char_101_sora_1",focus=2)]
[name="空"]   看吧，果然在那里。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_031")]
[name="黑帮"]   唔——唔唔唔，唔！
[Character(name="char_103_angel_1#7",name2="avg_npc_031",focus=1)]
[name="能天使"]   喂，你再不说，我可就要点火了啊？
[Character(name="avg_npc_031",name2="char_201_moeshd",focus=2)]
[name="可颂"]   小哥你还是老实招了吧，这个烟花真的能带着你上天的喔。
[Character(name="char_102_texas_1#2")]
[name="德克萨斯"]   ......你们忘了把他嘴上的胶布撕掉。
[Character(name="char_103_angel_1#4",name2="avg_npc_031",focus=1)]
[name="能天使"]   啊，抱歉抱歉，嘿咻！
[Character(name="avg_npc_031")]
[CameraSha

... (全文11022字符)
```

### level_act5d0_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Background(image="bg_park",screenadapt="coverall", fadetime=1)]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Character]
[Delay(time=1)] 
[name="路过的观众A"]  喂，这是在拍电影吗？
[name="路过的观众B"]  那不是企鹅物流那群人吗？又在打架？
[name="路过的观众B"]  对！左勾拳！就这样！帅喔！
[name="路过的观众A"]  每次都是他们赢，没意思啦。
[name="路过的观众B"]  也是。喂，不知道哪儿冒出来的黑服，你们不要输太惨啊！
[Dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$p_atk_smg_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Character(name="char_103_angel_1#7")]
[name="能天使"]   嘿咻，不能用实弹可真麻烦啊。
[Character(name="char_103_angel_1#7",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]   这里再怎么说也是市中心，当然不能用实弹了。能天使姐，背后！
[Dialog]
[Character]
[playsound(key="$p_imp_blunt_h")]
[Blocker(a=1, r=0.95, g=0.95, b=0.95, fadetime=0.2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_103_angel_1#3",name2="char_201_moeshd",focus=1)]
[name="能天使"]   哎呀，危险危险~谢啦，可颂。
[Character(name="char_325_bison_1#4",name2="char_102_texas_1",focus=1)]
[name="拜松"]   这么纠缠下去可没完没了！德克萨斯小姐！
[Character(name="char_325_bison_1#4",name2="char_102_texas_1",focus=2)]
[name="德克萨斯"]   嗯......空和我，能天使和可颂，兵分两路，我们去大地的尽头。
[Character(name="char_325_bison_1#2",name2="char_102_texas_1",focus=1)]
[name="拜松"]   ......什么？
[Character(name="char_101_sora_1")]
[name="空"]   太棒...不，我明白了。
[Character(name="char_103_angel_1#8",name2="char_201_moeshd#2",focus=1)]
[name="能天使"]   哦~分头引开这些敌人是吗？没问题，我最擅长这个！
[Character(name="char_103_angel_1#8",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]   能天使姐，路上麻烦你小心一点，赔偿清单在变长......
[Character(name="char_325_bison_1#2")]
[name="拜松"]   等等，你们说的那个“大地的尽头”是什么意思？
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   一个小时后集合。
[Character(name="char_325_bison_1#4",name2="char_102_texas_1",focus=1)]
[name="拜松"]   所以是什么意思！？
[Character(name="char_101_sora_1#3")]
[name="空"]   可是我们要怎么杀出去？
[Character(name="char_103_angel_1#5",name2="avg_npc_031",focus=1)]
[name="能天使"]   我有一个办法......
[Character(name="char_103_angel_1#5",name2="avg_npc_031",focus=2)]
[name="黑帮"]   你，你想干嘛！？你这天使——我可不怕你——
[Character]
[Dialog]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_103_angel_1#3",name2="char_201_moeshd#2",focus=1)]
[name="能天使"]   可颂，上来！这辆摩托还挺帅的嘛！
[PlaySound(key="$motorbikestart")]
[Character(name="char_103_angel_1#3",name2="char_201_moeshd",focus=2)]
[name="可颂"]   好嘞，走着！
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   抢车？好主意......
[name="德克萨斯"]   嗯，就你了。
[Character(name="avg_npc_031")]
[name="黑帮"]   你别过来啊，该死的狼——你——噫噫——车、车给你，别打脸！
[Character]
[Dialog]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_102_texas_1",name2="char_101_sora_1#3",focus=1)]
[name="德克萨斯"]   嗯，空，赶紧上来。
[Character(name="char_102_texas_1",name2="char_101_sora_1#3",focus=2)]
[name="空"]   好、好的！
[Character(name="char_102_texas_1",name2="char_101_sora_1#3",focus=1)]
[name="德克萨斯"]   抓紧了，可不能比能天使他们动作慢。
[Character(name="char_102_texas_1",name2="char_101_sora_1#4",focus=2)]
[name="空"]   还是稍、稍微慢——
[Dialog]
[Character]
[PlaySound(key="$motorbikestart")]
[Delay(time=2)]
[Character(name="char_325_bison_1")]
[name="拜松"]   那我——
[stopmusic(fadetime=2)]
[name="拜松"]   ......
[Character(name="char_325_bison_1",name2="avg_npc_031",focus=2)]
[name="黑帮"]   ......
[Character(name="char_325_bison_1",name2="avg_npc_031",focus=1)]
[name="拜松"]   ......
[Character(name="char_325_bison_1",name2="avg_npc_031",focus=2)]
[name="黑帮"]   企鹅物流就把这小子丢这儿了？
[name="黑帮"]   那不是正好，一起上，看他怎么反抗！
[Character(name="char_325_bison_1#4",name2="avg_npc_031",focus=1)]
[name="拜松"]   嘁！那帮家伙一个个的在想什么！？
[name="拜松"]    该死——！这附近有没有——！
[Character]
[name="路过的观众A"]    啊，要自行车吗？借你也可以。
[Character(name="char_325_bison_1#4")]
[name="拜松"]   自、自行车......
[name="拜松"]   算了，也没空挑挑拣拣了，谢谢！
[Dialog]
[Character(fadetime=1,block=true)]
[Delay(time=2)]
[name="路过的观众A"]   好好加油啊！
[Character(name="avg_npc_031")]
[name="黑帮"]   你竟然敢帮企鹅物流——！？
[Character]
[name="路过的观众A"]   反正你们有车，也追得上吧？
[Character(name="avg_npc_031")]
[name="黑帮"]   你——
[Dialog]
[Character]
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.8, crossfade=1.5)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_027#2",fadetime=1,block=true)]
[Delay(time=1)]
[name="卡彭"]   忍着，不要对平民出手，否则我们就完蛋了。
[Character(name="avg_npc_027#2",name2="avg_npc_031",focus=2)]
[name="黑帮"]   对、对不起，追！都给我去追！
[Character(name="avg_npc_027#2")]
[name="卡彭"]   哼......
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_028",fadetime=1,block=true)]
[Delay(time=1)]
[name="甘比诺"]   “绑架拜松，分裂企鹅物流和峯驰物流，刺杀大帝”，你的好主意。
[Character(name="avg_npc_028",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   我们的目的是取而代之。没必要杀光那些蠢货，这笔账你都不会算了吗？
[Character(name="avg_npc_028",name2="avg_npc_027#2",focus=1)]
[name="甘比诺"]   德克萨斯，她可是德克萨斯。还有那个拉特兰人和峯驰物流的大少爷，给她们留后路，我们还会有安稳日子吗？
[name="甘比诺"]   必须得斩草除根。
[Character(name="avg_npc_028",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   那样会引起其他人的瞩目。不止我们盯着这块蛋糕。
[Character(name="avg_npc_028#3",name2="avg_npc_027#2",focus=1)]
[name="甘比诺"]   哈！你怕了？
[Character(name="avg_npc_028#3",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   进退是需要动脑子的，蠢货。
[Character(name="avg_npc_028#3",name2="avg_npc_027#2",focus=1)]
[name="甘比诺"]   低声下气地恳请鼠王已经是我的底线，懦夫。在龙门的这么些年，你变得畏首畏尾。
[name="甘比诺"]   如果不是念在你对家族的贡献，我早就把你撵出去了。
[Character(name="avg_npc_028#3",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   我们都有各自的事情要做，嘲讽的话一会再说。
[Character(name="avg_npc_028"

... (全文7363字符)
```

### level_act5d0_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[PlayMusic(intro="$penguinlogistics_intro", key="$penguinlogistics_loop", volume=1, crossfade=1.5)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_103_angel_1#8")]
[name="能天使"]   呀吼~
[Character(name="char_103_angel_1#8",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]   注意看路啦，能天使姐，不要单手扶握把！
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   总算跟上你们了。
[Character(name="char_102_texas_1",name2="char_101_sora_1#4",focus=2)]
[name="空"]   德克萨斯......下一次......请慢一点......
[Character(name="char_102_texas_1",name2="char_101_sora_1#4",focus=1)]
[name="德克萨斯"]   抱、抱歉。我已经尽量控制了。
[Character(name="char_103_angel_1#3")]
[name="能天使"]   既然咱们已经汇合，那么下一步就是去找老板啦——
[Character(name="char_103_angel_1#7")]
[name="能天使"]   慢着，我怎么觉得少了点什么？
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   嗯？
[name="德克萨斯"]   ......拜松呢？
[Character(name="char_103_angel_1#7",name2="char_102_texas_1",focus=1)]
[name="能天使"]   欸？不应该是你们带着他走吗？
[Character(name="char_103_angel_1#7",name2="char_102_texas_1",focus=2)]
[name="德克萨斯"]   ......
[Character(name="char_101_sora_1#3")]
[name="空"]   ......难道我们把他丢在那儿了？
[Character(name="char_102_texas_1#2",name2="char_101_sora_1#3",focus=1)]
[name="德克萨斯"]   ......习惯了我们自己的节奏，突然多出来一个人，是会把他忘掉啊。
[Character(name="char_102_texas_1#2",name2="char_101_sora_1#3",focus=2)]
[name="空"]   ——那我们是不是得赶紧回去帮忙？
[Character(name="char_103_angel_1#4")]
[name="能天使"]   不是有莫斯提马在吗？问题不大吧？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="char_325_bison_1#4")]
[name="拜松"]   喂——！等，等我一下！咳！
[Character(name="char_101_sora_1#3")]
[name="空"]   ......自行车？
[Character(name="char_201_moeshd")]
[name="可颂"]   唔噢！靠自行车就能追上德克萨斯的速度，拜松他挺行的嘛！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, fadetime=0.5, block=true)]
[name="黑帮"]   喂！他往哪个巷子去了！？
[name="黑帮"]   那个方向！
[Character(name="char_103_angel_1#4")]
[name="能天使"]   他身后还跟着一大批人喔。
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   你不能奢求一个人骑着自行车还能甩开一整支武装黑手党。
[name="德克萨斯"]   ......不对，有埋伏，能天使！
[Character(name="char_103_angel_1#4")]
[name="能天使"]   但好像有点来不及了喔——！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="char_325_bison_1#4")]
[name="拜松"]   唔！
[name="拜松"]   总、总算追上他们了！
[stopmusic(fadetime=1)]
[Character]
[name="甘比诺"]   是啊，辛苦你带路了。
[Character(name="char_325_bison_1#4")]
[name="拜松"]   谁——
[Character(name="avg_npc_028")]
[name="甘比诺"]   睡一小会吧，小少爷。
[Character(name="char_325_bison_1")]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="拜松"]   呃！
[Dialog]
[Character(fadetime=1,block=true)]
[Delay(time=1)]
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   啧，慢了一步。
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.8, crossfade=1.5)]
[Character(name="avg_npc_028#4")]
[name="甘比诺"]   晚上好，企鹅物流的各位，我是甘比诺·里奇，家族的首领。
[name="甘比诺"]   很遗憾，人质在我们手上。
[name="甘比诺"]   不过，你们也不是会因为这点小事就乱了手脚的人吧？
[Character(name="char_103_angel_1#7",name2="char_201_moeshd",focus=1)]
[name="能天使"]   本来就是我们把他忘了......
[Character(name="char_103_angel_1#7",name2="char_201_moeshd#5",focus=2)]
[name="可颂"]   倒、倒也是。
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   你想怎样？
[Character(name="avg_npc_028#4",name2="char_102_texas_1",focus=1)]
[name="甘比诺"]   哼......你们东躲西藏的，实在让人厌烦。动静闹太大，对大家都不好，不是吗？
[name="甘比诺"]   这个小少爷的确还有点用处。有了人质，你们就只能正面应战，别无选择。
[name="甘比诺"]   这样能为我省掉不少麻烦，能动手解决的问题，都是最好解决的问题。
[name="甘比诺"]   企鹅物流，你们现在无处可逃。
[stopmusic(fadetime=2)]
[Character(name="avg_npc_028#4",name2="char_102_texas_1",focus=2)]
[name="德克萨斯"]   原来如此。那可真是太好了。
[Character(name="avg_npc_028",name2="char_102_texas_1",focus=1)]
[name="甘比诺"]   ......什么？
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.8, crossfade=1.5)]
[Character(name="avg_npc_028",name2="char_102_texas_1",focus=2)]
[name="德克萨斯"]   毕竟我们也是这么想的。
[Character(name="char_102_texas_1#4")]
[name="德克萨斯"]   可颂和空维持阵型。
[name="德克萨斯"]   能天使注意掩护。
[name="德克萨斯"]   抢回拜松。
[Dialog]
[Character(fadetiem=1)]
[Delay(time=0.5)]
[Blocker(fadetime=2,block=true)]
```

### level_act5d0_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background]
[Delay(time=0.4)]
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.8, crossfade=1.5)]
[Blocker(a=0, fadetime=1, block=true)]
8:52 P.M.  天气/多云
龙门贫民窟
[Dialog]
[Delay(time=1)]
[name="黑帮A"]   啧！想活命就告诉我们，鼠王到底在哪儿！？
[name="贫民窟居民"]   我、我不知道啊！什么鼠王......真的没听说过啊！
[name="黑帮A"]   敬酒不吃吃罚酒——！
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[name="黑帮B"]   喂，卡彭先生说过不要随便对平民动手......
[name="黑帮A"]   这种下三滥的货色能算市民吗？遮遮掩掩的，说不定就是个感染者垃圾！还敢装糊涂！？
[name="贫民窟居民"]   等、等等！别打了！我真的不知道啊！！
[name="黑帮A"]   嘴硬！？
[name="贫民窟居民"]   唔——呃，呕——
[name="黑帮B"]   走吧，别管这家伙了，恶心。
[name="黑帮B"]   看名单，下一个老东西似乎就住在这里不远，是个卖鱼丸的，就在生鲜卖场对面。
[name="黑帮A"]   嘁，浪费时间。
[name="贫民窟居民"]   咕，哈啊——骨头都断了，这帮——该死的——下手真重，嘎哈！
[name="贫民窟居民"]   必须得......告诉他们......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_031")]
[name="黑帮A"]   那边的，站住。
[Dialog]
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",fadetime=1,block=true)]
[Delay(time=3)]
[Character(name="char_272_strong_1")]
[name="孑"]   .....
[Character(name="char_243_waaifu_1#2")]
[name="槐琥"]   ......你们有什么事吗？
[Character(name="avg_npc_031",name2="avg_npc_031",focus=1)]
[name="黑帮B"]   （等等，注意旁边那个男的，我总觉得不是什么善茬。）
[Character(name="avg_npc_031",name2="avg_npc_031",focus=2)]
[name="黑帮A"]   （龙门当地的帮派？不用担心，按照卡彭先生的报告，都是小角色。）
[name="黑帮A"]   我有点事情要问。
[name="黑帮A"]   谁也不想惹上麻烦，对吧？乖乖回答我们，我们就走。
[Character(name="char_272_strong_1",name2="avg_npc_031",focus=1)]
[name="孑"]   ......你的拳头上有血。
[Character(name="char_272_strong_1",name2="avg_npc_031",focus=2)]
[name="黑帮A"]   不好意思，只是些不配合的垃圾。
[name="黑帮A"]   但是像你们这样的好市民，当然会配合我们的吧？
[Character(name="avg_npc_031",name2="char_243_waaifu_1#2",focus=2)]
[name="槐琥"]   这是威胁？
[Character(name="avg_npc_031",name2="char_243_waaifu_1#2",focus=1)]
[name="黑帮A"]   大家心里清楚。
[Character(name="avg_npc_031",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   那我拒绝。
[Character(name="avg_npc_031",name2="char_243_waaifu_1#3",focus=1)]
[name="黑帮B"]   ......拒绝？
[name="黑帮B"]   小姑娘，你好像弄错了什么。
[name="黑帮B"]   还是说，你也想变成那边巷子里的垃圾，被打得半死不活？
[Character(name="char_272_strong_1")]
[name="孑"]   槐琥，我刚才听到的惨叫声......
[Character(name="avg_npc_031",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   ——你们刚才说了，“垃圾”，对吧？
[name="槐琥"]   以防万一我多问一句，你是指这里的居民吗？
[Character(name="avg_npc_031",name2="char_243_waaifu_1#3",focus=1)]
[name="黑帮A"]   我没那么多时间陪你废话，赶紧——
[Dialog]
[Character(name="char_243_waaifu_1#4")]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=0.4)]
[Character(name="avg_npc_031")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[name="黑帮A"]   敢、敢还手！？
[name="黑帮A"]   都给我上——
[Dialog]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[Delay(time=0.55)]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.7, xstrength=10, ystrength=12, vibrato=30, randomness=120, fadeout=true, block=true)]
[Character(name="avg_npc_031")]
[name="黑帮A"]   呃！？
[Dialog]
[Character(fadetime=0.7,block=true)]
[delay(time=0.7)]
[Character(name="char_243_waaifu_1#4")]
[name="槐琥"]   下一个。
[name="槐琥"]   不，算了，反正你们也就只是一群不入流的喽啰，一起上吧。
[name="槐琥"]   古往今来，邪不压正，你们这些滥伤无辜的下九流，何足挂齿。
[Dialog]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true,block=true)]
[delay(time=1)]
[Character(name="avg_npc_031")]
[name="黑帮B"]   什么情况！？这女人的动作——？
[Character(name="avg_npc_031")]
[name="黑帮A"]   那就尝尝弩弹——
[Character(name="char_272_strong_1#4")]
[name="孑"]   ......慢着。
[Character(name="char_272_strong_1#4",name2="avg_npc_031",focus=2)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[name="黑帮A"]   咕！松手！你这混账！
[Character(name="char_272_strong_1",name2="avg_npc_031",focus=1)]
[name="孑"]   唉，你这种人，属于冰箱断电馊了三天的海胆，差不多那个感觉吧。
[Character(name="char_272_strong_1",name2="avg_npc_031",focus=2)]
[name="黑帮A"]   你、你在说什么？
[Character(name="char_272_strong_1",name2="avg_npc_031",focus=1)]
[name="孑"]   ......算了，我不该学槐琥咬文嚼字的，还是直接点好。
[name="孑"]   嘿。
[Character(name="char_272_strong_1",name2="avg_npc_031",focus=2)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[name="黑帮A"]   好、好大的劲，等！等等！要断了！要断了！
[Character(name="char_272_strong_1#4",name2="avg_npc_031",focus=1)]
[name="孑"]   把武器放下，滚出这里。
[Character(name="char_272_strong_1#4",name2="avg_npc_031",focus=2)]
[name="黑帮A"]   我、我知道了，你先放手！
[Character(name="char_272_strong_1",name2="avg_npc_031",focus=1)]
[name="孑"]   ......但果然还是应该弄脱臼比较好吧。毕竟你拿着那么危险的武器。
[Character(name="char_272_strong_1",name2="avg_npc_031")]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[Character(name="char_272_strong_1",name2="avg_npc_031",focus=2)]
[name="黑帮A"]   呃啊！你，你真下得去手——
[Character(name="avg_npc_031")]
[name="黑帮B"]   这、这两个人怎么回事？我没听说这附近有什么注意目标啊！
[name="黑帮A"]   嘁，先走，回头再说。
[name="黑帮A"]   不管你们是哪个帮派的，都不会有好下场的！该死的龙门人！
[Dialog]
[PlaySound(key="$rungeneral")]
[Character(fadetime=1,block=true)]
[Delay(time=1)]
[Character(name="char_272_strong_1")]
[name="孑"]   不，都说了我不是黑社会，为什么都喜欢以貌取人......
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#2",focus=2)]
[name="槐琥"]   先别管这些，救人要紧，我去那边看看！
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#2",focus=1)]
[name="孑"]   啊，好。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$rungeneral")]
[Blocker(a=0,

... (全文6368字符)
```

### level_act5d0_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[Dialog]
[Delay(time=1)]
[PlayMusic(intro="$penguinlogistics_intro", key="$penguinlogistics_loop", volume=0.8, crossfade=1.5)]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Delay(time=0.4)] 
[Blocker(a=0, fadetime=1, block=true)] 
10:26 P.M.    天气/多云
日落大道，“大地的尽头”酒吧
[Dialog]
[Delay(time=0.4)]
[Character(name="char_201_moeshd#2")]
[name="可颂"]   那老板，这瓶酒又是哪一年的？
[Character(name="char_105_emper")]
[name="大帝"]   嗯哼，沉淀的色泽，悠久的香气，后觉的甜味，绵长的口感，这是——
[name="大帝"]   上个月在超市买来的便宜酒。
[Character(name="char_105_emper",name2="char_201_moeshd",focus=2)]
[name="可颂"]   十猜十中哎，不愧是自称龙门第一的品酒师！
[Character(name="char_105_emper")]
[name="大帝"]   呸，说了多少遍了，这是储备武器，不是用来喝的！空！
[Character(name="char_105_emper",name2="char_101_sora_1#3",focus=2)]
[name="空"]   好好好，这是漱口水。
[Character(name="char_201_moeshd#2")]
[name="可颂"]   欸......用炎国黄酒漱口吗......
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   酒精的确可以消毒，吧台下面有工业酒精，能凑合。
[Character(name="char_201_moeshd")]
[name="可颂"]   算了，有这个钱，不如买点别的好啦，花钱的精髓就在于过程，过程！和金额无关！
[Character(name="char_103_angel_1#8")]
[name="能天使"]   各位，苹果派烤好了！派对开始啦！
[Character(name="char_201_moeshd")]
[name="可颂"]   哦~是能天使姐亲手烤的派！
[Character(name="char_105_emper")]
[CameraShake(duration=0.3, xstrength=8, ystrength=6, vibrato=20, randomness=20, fadeout=true, block=false)]
[name="大帝"]   干杯！
[Character(name="char_103_angel_1#8",name2="char_101_sora_1#3",focus=2)]
[name="空"]   ......虽然不知不觉就变成这样了，但这是什么派对来着？
[Character(name="char_103_angel_1#7",name2="char_101_sora_1#3",focus=1)]
[name="能天使"]   嗯？拜松的欢迎会呀。
[Character(name="char_103_angel_1#7",name2="char_101_sora_1#3",focus=2)]
[name="空"]   ......那拜松本人呢？
[Character(name="char_103_angel_1#6",name2="char_101_sora_1#3",focus=1)]
[name="能天使"]   嗯！不知道！
[Character(name="char_105_emper")]
[name="大帝"]   那就换个借口，我们永远不缺借口。
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[PlaySound(key="$dooropenquite", volume=0.9)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_325_bison_1#4",fadetime=1,block=true)]
[Delay(time=1)]
[name="拜松"]   ......你们在做什么？
[Character(name="char_201_moeshd#4")]
[name="可颂"]   呃。在等你开派对，吧。
[Character(name="char_325_bison_1#4",name2="char_105_emper",focus=2)]
[name="大帝"]   啊，欢迎来到大地的尽头。
[name="大帝"]   迟到罚酒三杯，主角迟到翻三倍，但你不能喝酒，所以汽水九杯，请。
[Character(name="char_325_bison_1#4")]
[name="拜松"]   为什么要叫这个名字......
[name="拜松"]   （还有这个装修风格，好闪亮.....为什么还有企鹅......这是某种朋克艺术吗......？）
[Character(name="char_325_bison_1#4",name2="char_103_angel_1#3",focus=2)]
[name="能天使"]   别傻站着了，快进来，这可是你的欢迎派对，要不要苹果派？
[Character(name="char_325_bison_1#4",name2="char_103_angel_1#3",focus=1)]
[name="拜松"]   ......不了。
[Character(name="char_325_bison_1#4")]
[name="拜松"]   原来在我和莫斯提马小姐对付那些黑手党的时候，你们却在这里开派对。
[name="拜松"]   那么......那个头目呢？
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   让他跑了。
[Character(name="char_105_emper")]
[name="大帝"]   准确来说，是我准许了他跑了。
[Character(name="char_325_bison_1#4")]
[name="拜松"]   反正就是跑了呗......那接下来怎么办？
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   敌人的数量，目的，身份，都已经很明显了。
[name="德克萨斯"]   来自叙拉古的黑手党，想要夺取企鹅物流在龙门的势力范围。
[name="德克萨斯"]   ......虽然我们应该是个物流公司......算了。
[Character(name="char_102_texas_1",name2="char_101_sora_1",focus=2)]
[name="空"]   不要放在心上，德克萨斯，总会有那么几天要用来清扫门户的。
[Character(name="char_201_moeshd")]
[name="可颂"]   说这话就更不像是一个正经公司了哦？
[Character(name="char_103_angel_1#7")]
[name="能天使"]   他们这是白忙活啦，老板的那些生意，就算拱手相让他们也玩不来的。
[Character(name="char_105_emper")]
[name="大帝"]   企鹅物流是不可取代的，而我更是不可取代的。
[Character(name="char_325_bison_1")]
[name="拜松"]   既然如此，我们有很多种解决方法，为什么一定要和他们火拼起来？
[Character(name="char_325_bison_1",name2="char_102_texas_1",focus=2)]
[name="德克萨斯"]   不知道。
[Character(name="char_325_bison_1",name2="char_102_texas_1",focus=1)]
[name="拜松"]   不知道......你们，一直以来是怎么......
[Character(name="char_105_emper")]
[name="大帝"]   好啦好啦，不要这么认真嘛，找个机会把他们的头儿揍一顿扔进江里，不就完事了吗？
[name="大帝"]   这场闹剧就和没能睡着的回笼觉一样浪费时间，我完——全提不起兴趣。
[Character(name="char_325_bison_1",name2="char_103_angel_1",focus=2)]
[name="能天使"]   就是嘛，这可不是什么值得认真讨论的事情。来，口香糖。
[Character(name="char_325_bison_1",name2="char_103_angel_1",focus=1)]
[name="拜松"]   ......唉。
[name="拜松"]   但至少我们应该制定一个计划......等等，这口香糖是什么味道？
[Character(name="char_325_bison_1",name2="char_103_angel_1",focus=2)]
[name="能天使"]   白马醇味。
[Character(name="char_201_moeshd",name2="char_102_texas_1",focus=2)]
[name="德克萨斯"]   把这个牌子的口香糖列入危险品范畴吧，可颂。
[Character(name="char_201_moeshd",name2="char_102_texas_1",focus=1)]
[name="可颂"]   看到新口味就进货了，没注意，诶嘿。
[Character(name="char_105_emper")]
[name="大帝"]   喂，你们派对还搞不搞了，有酒有菜，音乐呢？
[Character(name="char_103_angel_1")]
[name="能天使"]   收到~！
[Dialog]
[Character]
[PlayMusic(intro="$bar_intro", key="$bar_loop", volume=0.8,crossfade=1)]
[Delay(time=5)]
[Character(name="char_325_bison_1#2")]
[name="拜松"]   居然真的是爵士乐......出乎意料......虽然有点.....
[Character(name="char_103_angel_1#8")]
[name="能天使"]   以前这里的主人的确是个爵士乐爱好者啦，只是在转让给老板之后发生了一些小小的风格变化。
[Character(name="char_101_sora_1#4")]
[name="空"]   小小的？
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   主要是因为老板自己的唱片刚才全部被——
[Character(name="char_105_emper")]
[name="大帝"]   打住，不要让我回忆起悲伤的往事。
[name="大帝"]   说到底，谁让他查出那种麻烦的病，我肯抽空来帮他照顾这家酒吧就不错了。
[Character(name="char_325_bison_1",name2="char_105_emper",focus=1)]
[name="拜松"]   难道是矿石病？
[name="拜松"]   龙门经历了那么多事情，对感染者的态度应该转变了不少才对......
[Character(name="char_325_bison_1",name2="char_105_emper",focus=2)]
[name="大帝"]   不。
[name="大帝"]   是酒精过敏。
[Character(name="char_325_bison_1",name2="char_105_emper",focus=1)]
[name="拜松"]   ......
[Character(name="char_201_moeshd#4")]
[name="可颂"]   对一个立志成为龙门最好的调酒师的家伙而言，的确是绝症了呢。
[Dialog]
[Character]
[stopmusic(fadetime=2)]
[playsound(key="$drift")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_105_emper")]
[name="大帝"]   怎么又有脏东西闯进来了，喂，你们几个，想活命的立刻趴到吧台后面去。
[Character(

... (全文10976字符)
```

### level_act5d0_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Dialog]
[Delay(time=1)]
[PlayMusic(intro="$bar_intro", key="$bar_loop", volume=0.8,crossfade=1)]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Delay(time=0.4)] 
[Blocker(a=0, fadetime=1, block=true)] 
[PlaySound(key="$e_atk_arrow_h")]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[PlaySound(key="$bottlebroken")]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$bottlebroken")]
[PlaySound(key="$e_atk_arrow_h")]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90)]
[PlaySound(key="$bottlebroken")]
[Dialog]
[Delay(time=2)]
[Character(name="char_105_emper",fadetime=2,block=true)]
[Delay(time=2)]
[name="大帝"]   晚上好，叙拉古的丧家犬，弩弹打完了？可我怎么还活着呢？
[Character(name="avg_npc_028#4")]
[name="甘比诺"]   真不愧是大帝，枪林弹雨里还端着酒杯，运气不错。
[Character(name="char_101_sora_1#2")]
[name="空"]   ......龙门从来不会纵容真正的厮杀。
[Character(name="char_103_angel_1#7")]
[name="能天使"]   不按游戏规则来，可是会被驱逐出局的。
[Character(name="avg_npc_028#4")]
[name="甘比诺"]   规则？
[Dialog]
[Character]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Character(name="avg_npc_031",name2="avg_npc_031",fadetime=1,block=true)]
[Delay(time=3)]
[Character(name="avg_npc_028#3")]
[name="甘比诺"]   当龙门警察到场的时候，只会看到你们几个支离破碎的尸首，企鹅物流。
[Character(name="char_325_bison_1#4")]
[name="拜松"]   ......街道上都是他们的人。
[Character(name="char_325_bison_1#4",name2="char_201_moeshd#3",focus=2)]
[name="可颂"]   连后门都堵上了，唉，看来这位先生一直怀恨在心嘛，做得很彻底。
[Character(name="avg_npc_028#3")]
[name="甘比诺"]   卡彭那个懦夫太过忌惮鼠王和魏彦吾了，后者兴许值得关注......
[name="甘比诺"]   至于你和那只装腔作势的老鼠，除了让人作呕的本事一流之外，一文不值。
[Character(name="avg_npc_028#3",name2="char_105_emper",focus=2)]
[name="大帝"]   嗯，你是真这么觉得？还是单纯想放狠话？
[Character(name="avg_npc_028#4",name2="char_105_emper",focus=1)]
[name="甘比诺"]   诚心实意，“大帝先生”。
[Character(name="char_201_moeshd#3",name2="char_105_emper",focus=2)]
[name="大帝"]   可颂，帮我捡瓶酒，我来帮他修理一下大脑皮层。
[Character(name="char_201_moeshd#4",name2="char_105_emper",focus=1)]
[name="可颂"]   但是老板，不瞒你说，我们已经砸掉了上百万龙门币的红酒了。
[Character(name="char_201_moeshd#4",name2="char_105_emper",focus=2)]
[name="大帝"]   ......那他们的命值多少钱？
[Character(name="char_201_moeshd#4",name2="char_105_emper",focus=1)]
[name="可颂"]   怎么看也没这个数吧。
[Character(name="char_201_moeshd#4",name2="char_105_emper",focus=2)]
[name="大帝"]   ......
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   要动真格的吗？
[Character(name="char_105_emper")]
[name="大帝"]   怎么会呢。我们一定会恪守和小魏的约定，在龙门之内，不打真架，不闹人命，一切生意上的纠纷，在商言商。
[name="大帝"]   只是今天我们总计逃亡了五个小时，超出了我日常工作时间的两倍，两倍！
[name="大帝"]   不仅如此，我们还炸掉了整整一年分的行动补贴！汽车，红酒，还有我的珍藏黑胶！
[name="大帝"]   现在，在我的酒吧发生了一些预料之内的意外死亡，这总没什么问题吧？嗯？
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   明白了。
[Character(name="char_102_texas_1",name2="avg_npc_028",focus=2)]
[name="甘比诺"]   德克萨斯，你的名字就让我感到不快。
[Character(name="char_102_texas_1",name2="avg_npc_028",focus=1)]
[name="德克萨斯"]   我不记得自己认识你这样的叙拉古人。但你会再次夹着尾巴逃离龙门。
[Character(name="char_102_texas_1",name2="avg_npc_028#3",focus=2)]
[name="甘比诺"]   你会后悔诋毁我的家族，德克萨斯。
[name="甘比诺"]   到底谁才是逃来龙门的丧家之犬，你心里清楚。你根本不配与西西里人为敌。
[Character(name="char_102_texas_1#4",name2="avg_npc_028#3",focus=1)]
[name="德克萨斯"]   ......
[Character(name="char_102_texas_1#4",name2="avg_npc_028#3",focus=2)]
[name="甘比诺"]   这才是像样的表情，德克萨斯！这才有点叙拉古人的样子！
[Dialog]
[Character]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_213_mostma_1#4")]
[name="莫斯提马"]   ......嗯？
[name="莫斯提马"]   真是意料之外呢，你也是被叫过来的？
[Dialog]
[Character]
[Character(name="avg_npc_035",fadetime=2,block=true)]
[Delay(time=2)]
[name="？？？"]   算是吧。不过能从商务酒会脱身的感觉也不错。
[Character(name="avg_npc_035",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   唔，这些黑手党的小打小闹，值得这么兴师动众的吗？
[Character(name="avg_npc_035",name2="char_213_mostma_1",focus=1)]
[name="？？？"]   不值得。而且我只是想从麻烦的社交里脱身，找个机会喘口气罢了。
[name="？？？"]   可颂为她的锤子定制了新的配件。能天使让我帮忙保养她的守护铳。总之，还有很多事情要做。
[Character(name="avg_npc_035",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   嗯，也许我也得麻烦你一下。
[Character(name="avg_npc_035",name2="char_213_mostma_1",focus=1)]
[name="？？？"]   没关系。除了本职工作，为同事们处理这些杂务，也是我的职责。
[Character(name="avg_npc_035",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   这把法杖，能帮我保管一下吗？
[Character(name="avg_npc_035",name2="char_213_mostma_1",focus=1)]
[name="？？？"]   白色的这把。你明白这其中的含义吧。
[Character(name="avg_npc_035",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   至少今晚，就让我轻松一点吧，只是一场狂欢而已。
[name="莫斯提马"]   我总不能真的带着它跳进舞会现场，那会失控的。
[Character(name="avg_npc_035",name2="char_213_mostma_1",focus=1)]
[name="？？？"]   我知道了。交给我吧，这也是工作。
[Character(name="avg_npc_035",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   呵呵，说来说去，不还是工作嘛，你也真是辛苦。
[name="莫斯提马"]   结束之后要不要去喝一杯？我请客好了。
[Character(name="avg_npc_035",name2="char_213_mostma_1#3",focus=1)]
[name="？？？"]   十分赞同。同事之间的酒会比无趣的应酬要好得多。
[name="？？？"]   但很可惜，看这动静，也许大地的尽头很难保全。
[Character(name="avg_npc_035",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   ......那么，你是刚回来龙门？对今晚的事情知道多少？
[Character(name="avg_npc_035",name2="char_213_mostma_1",focus=1)]
[name="？？？"]   全部。这次狂欢的来龙去脉并不复杂，一切情报昭然若揭。
[Character(name="avg_npc_035",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   你不打算去帮个忙？
[Character(name="avg_

... (全文13840字符)
```

### level_act5d0_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_motorway",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_031")]
[name="黑帮"]   首领，企鹅物流有动作了。
[Character(name="avg_npc_028#2",name2="avg_npc_031",focus=1)]
[name="甘比诺"]   ......意料之内，只是给她留下了点皮肉伤......
[name="甘比诺"]   但我更在意的是，卡彭呢？
[Character(name="avg_npc_028#2",name2="avg_npc_031",focus=2)]
[name="黑帮"]   其、其实在一个小时前就彻底联系不上了。
[Character(name="avg_npc_028#3",name2="avg_npc_031",focus=1)]
[name="甘比诺"]   ......最后一次例行联络是在哪里？贫民窟吗？
[Character(name="avg_npc_028#3",name2="avg_npc_031",focus=2)]
[name="黑帮"]   啊，是的。
[Character(name="avg_npc_028",name2="avg_npc_031",focus=1)]
[name="甘比诺"]   那还真是可惜。
[Character(name="avg_npc_028",name2="avg_npc_031",focus=2)]
[name="黑帮"]   您的意思是？
[Character(name="avg_npc_028",name2="avg_npc_031",focus=1)]
[name="甘比诺"]   先通知所有小队，按原计划拦截企鹅物流——
[name="甘比诺"]   但我猜，不出意外的话，大概会有那么两三个小队挂断联络吧。
[Character(name="avg_npc_028",name2="avg_npc_031",focus=2)]
[name="黑帮"]   您这是什么意思......啊。
[name="黑帮"]   难道——卡彭先生背叛了家族？
[Character(name="avg_npc_028",name2="avg_npc_031",focus=1)]
[name="甘比诺"]   我理解他，太理解他了。
[name="甘比诺"]   我们从小一起长大，亲手为父亲解决叛徒，那是我第一次杀人，是我们第一次杀人。
[name="甘比诺"]   叙拉古的惨败改变了我们。唯一的区别是，他变得更加懦弱，而我选择了更明确的道路。
[name="甘比诺"]   他打算出卖家族，或者说，给家族换个姓氏。
[Character(name="avg_npc_028",name2="avg_npc_031",focus=2)]
[name="黑帮"]   那我们应该如何是好？
[Character(name="avg_npc_028",name2="avg_npc_031",focus=1)]
[name="甘比诺"]   ......企鹅物流比想象中棘手，我们也不能同时树敌太多。
[name="甘比诺"]   也许，我们应该先解决叛徒的问题。
[stopmusic(fadetime=3)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_031")]
[name="黑帮A"]   这里是三道口，没有异常。
[Character]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[name="黑帮B"]   明白了，那么一切照常行动。
[Character(name="avg_npc_031")]
[name="黑帮A"]   ——等、等等！我们的计划是什么来着？
[Character]
[name="黑帮B"]   啊？你小子没搞错吧？
[Character(name="avg_npc_031")]
[name="黑帮A"]   呃，我只是确认一下，对龙门不太熟悉。
[Character]
[name="黑帮B"]   安魂节的午夜过后，龙门会按例举办狂欢活动，我们的任务就是趁着万人空巷时候解决企鹅物流，就这么简单！
[Character(name="avg_npc_031")]
[name="黑帮A"]   那关于首领的——
[Character]
[name="黑帮B"]   别问那么多，这是要求，照做就是了！快！
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[Character(name="avg_npc_031")]
[name="黑帮"]   ......就是这样了。
[name="黑帮"]    不会杀我的，对吧？
[Character(name="char_103_angel_1#8")]
[name="能天使"]   当然，多谢小哥啦，小睡一会吧~
[Character(name="avg_npc_031")]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true,block=true)]
[Delay(time=1)]
[Character(name="char_103_angel_1#3")]
[name="能天使"]   德克萨斯，听得见吗~？
[Dialog]
[Character]
[PlayMusic(intro="$penguinlogistics_intro", key="$penguinlogistics_loop", volume=0.8, crossfade=1.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   和这里的情况一样。他们打散了小队。
[name="德克萨斯"]   但既然首领亲自参与了战斗，他们一定有另一个指挥塔负责调度。
[name="德克萨斯"]   找到那里，一了百了。
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[Character]
[name="空"]   喂~？德克萨斯？
[name="空"]   我们已经到市中心啦，但是人真的很多。
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   注意敌方小队的动向。
[Character]
[name="空"]   知道啦~会拜托街上的熟人们留意的......等等，老板？你要到花车上面去看看？欸，等等我——
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   ......可颂，拜松，听得见吗？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_325_bison_1#4")]
[name="拜松"]   你说的那个指挥塔，我们稍微有点意外发现。
[Character(name="char_325_bison_1#4",name2="char_201_moeshd#3",focus=2)]
[name="可颂"]   ......拜松，压低身子，躲到那边的箱子后面，不要被发现。
[Character(name="char_325_bison_1#4",name2="char_201_moeshd#3",focus=1)]
[name="拜松"]   好，德克萨斯，一会联系。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_031")]
[name="黑帮A"]   我们，以后会怎么样？
[Character(name="avg_npc_031",name2="avg_npc_031",focus=2)]
[name="黑帮B"]   不知道，从我们挂断首领......挂断甘比诺·里奇的通讯开始，我们就没得选了。
[Character(name="avg_npc_031",name2="avg_npc_031",focus=1)]
[name="黑帮A"]   唉。
[Character(name="avg_npc_031",name2="avg_npc_031",focus=2)]
[name="黑帮B"]   叹什么气，卡彭先生在龙门为我们准备了这么多，结果呢？
[name="黑帮B"]   甘比诺从叙拉古转移过来就开始胡搅蛮缠，没一件好事！
[name="黑帮B"]   本来按照卡彭先生的计划，根本不需要这么大费周章。
[name="黑帮B"]   都和鼠王聊好了，为什么非要大开杀戒？这里可不是叙拉古！
[Character(name="avg_npc_031",name2="avg_npc_031",focus=1)]
[name="黑帮A"]   唉，首领，我是说前首领，可能只是在泄愤吧。
[Character(name="avg_npc_031",name2="avg_npc_031",focus=2)]
[name="黑帮B"]   呸，幼稚。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.4)]
[stopmusic(time=2)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_325_bison_1",name2="char_201_moeshd#3",focus=2)]
[name="可颂"]   （他们好像起了点内讧？）
[Character(name="char_325_bison_1",name2="char_201_moeshd#3",focus=1)]
[name="拜松"]   （似乎是，这是大好的机会，我们——）
[Character]
[Dialog]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$pistol")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Delay(time=1)]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_031")]
[name="黑帮A"]   ——！谁在那里！
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.8, crossfade=1.5)]
[Character(name="char_325_bison_1#4",name2="char_201_moeshd#5",focus=2)]
[name="可颂"]   欸？哪儿来的枪声？
[Character(name="char_325_bison_1#4",name2="char_201_moeshd#5",focus=1)]
[name="拜松"]   又是那个狙击手——！他暴露了我们的位置！
[Character(name="avg_npc_031")]
[name="

... (全文13031字符)
```

### level_act5d0_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Dialog]
[Character]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.8, crossfade=1.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[dialog]
[Character(name="char_102_texas_1#4")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[dialog]
[Character(name="char_102_texas_1#4")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="avg_npc_028#2")]
[name="甘比诺"]   哈啊，哈啊......
[Character(name="avg_npc_027#4")]
[name="卡彭"]   再来啊，企鹅物流！
[Character(name="avg_npc_027#4",name2="char_103_angel_1#7",focus=2)]
[name="能天使"]   你们这不是关系挺好的吗？
[Character(name="avg_npc_027#4",name2="char_103_angel_1#7",focus=1)]
[name="卡彭"]   嘁！
[Character(name="char_201_moeshd#3")]
[name="可颂"]   干嘛要冲着我来！？吃我一锤！
[dialog]
[playsound(key="$p_imp_blunt_h")]
[Blocker(a=1, r=0.95, g=0.95, b=0.95, fadetime=0.2, block=true)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_031",name2="avg_npc_028#2",focus=2)]
[name="甘比诺"]   呃！你到底是帮哪边的！？
[Character(name="avg_npc_031",name2="avg_npc_028#2",focus=1)]
[name="黑帮"]   不、不是我动的手！是那个天使！
[Character(name="char_103_angel_1#4")]
[name="能天使"]   诶嘿，打歪了，也没差啦。
[Character(name="avg_npc_031",name2="avg_npc_031",focus=1)]
[name="黑帮A"]   趁现在——危险！你往我这儿砍做什么！？
[Character(name="avg_npc_031",name2="avg_npc_031",focus=2)]
[name="黑帮B"]   对不起，我还是觉得应该忠于首领！！
[Character(name="avg_npc_031",name2="avg_npc_031",focus=1)]
[name="黑帮A"]   但我也是啊！
[Character(name="avg_npc_031",name2="avg_npc_031",focus=2)]
[name="黑帮B"]   呃。
[Dialog]
[Character]
[Character(name="avg_npc_028#3")]
[name="甘比诺"]   都躺地上干什么？没死的都爬起来！
[Character(name="avg_npc_031",name2="avg_npc_028#3",focus=1)]
[name="黑帮"]   是、是！
[Character(name="char_103_angel_1#5")]
[name="能天使"]   这么勉强部下可不好哦，有医疗补贴吗？
[Character(name="char_102_texas_1#4")]
[name="德克萨斯"]   ......有点混乱，但总之把穿黑衣服的全部打趴下就行了吧？
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="char_213_mostma_1#2")]
[name="莫斯提马"]   真是乱成一锅粥啊。
[Character(name="char_213_mostma_1#2",name2="char_325_bison_1#2",focus=2)]
[name="拜松"]   是啊——欸！？莫斯提马小姐？
[Character(name="char_213_mostma_1#3",name2="char_325_bison_1#2",focus=1)]
[name="莫斯提马"]   但是看你们还挺有活力的。
[Character(name="char_213_mostma_1#3",name2="char_102_texas_1",focus=2)]
[name="德克萨斯"]   ......你什么时候来的？
[Character(name="char_213_mostma_1#2",name2="char_102_texas_1",focus=1)]
[name="莫斯提马"]   老板喊我来的嘛。
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_027#2")]
[name="卡彭"]   嘁，是那个奇怪的萨科塔人。
[Character(name="avg_npc_028#3")]
[name="甘比诺"]   给我滚开！
[dialog]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_213_mostma_1#3")]
[PlaySound(key="$p_skill_blacktimewand_shot", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="avg_npc_028#3")]
[name="甘比诺"]   ——
[Character(name="char_213_mostma_1#3")]
[name="莫斯提马"]   好了好了，冷静一点。
[name="莫斯提马"]   在这里打赢了又能有什么结果？各退一步吧。
[Character(name="avg_npc_031")]
[name="黑帮A"]   她把首领给挡住了！？
[name="黑帮B"]   不对！那是法杖！首领小心！她是个术师！
[Character(name="avg_npc_027#4")]
[name="卡彭"]   ......看来没有和她正面作战是正确的选择......喂，先不要靠近他们！
[Character(name="avg_npc_028#2")]
[name="甘比诺"]   ......我从没见过你这样的萨科塔，不，你是萨卡兹？你到底是什么？
[Character(name="avg_npc_028#2",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   普通的信使啊，不然呢？
[Character(name="avg_npc_028#3",name2="char_213_mostma_1#3",focus=1)]
[name="甘比诺"]   故弄玄虚！
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[PlaySound(key="$p_skill_blacktimewand_shot", volume=0.9)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom

... (全文17496字符)
```

### level_act5d0_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[Dialog]
[Character]
[Delay(time=1)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Character(name="char_213_mostma_1#4")]
[name="莫斯提马"]   大家没事吧？
[Character(name="char_325_bison_1#2")]
[name="拜松"]   没、没事，整栋楼都不见了......那到底是什么......
[PlayMusic(intro="$penguinlogistics_intro", key="$penguinlogistics_loop", volume=0.8, crossfade=1.5)]
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   你呢？你刚才直接穿过了法术的正中心吧，总是那么乱来。
[name="莫斯提马"]   噗嗤，我这才发现，怎么把长头发剪短了？
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1",focus=1)]
[name="能天使"]   喂，你刚刚笑出来了吧！
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   头上都沾满了沙子，就算是短发也不能不珍惜啊。
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1#3",focus=1)]
[name="能天使"]   我没事的啦，谢谢。
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   ......谢谢？我们已经这么生疏了吗？
[Character(name="char_103_angel_1#8",name2="char_213_mostma_1",focus=1)]
[name="能天使"]   这只说明我讲文明懂礼貌。
[Character(name="char_103_angel_1#8",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   呵呵，说的也是。
[name="莫斯提马"]   如果你不总是在工作时间睡觉，在教堂外搞摇滚乐演出，出了岔子再让公证所的人追你三条街的话。
[name="莫斯提马"]   被你失手炸掉的母校在你离开拉特兰的那一天可是拉了横幅的哦？“欢送能天使前往龙门”。
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#3",focus=1)]
[name="能天使"]   什么？这是老友聚会互揭伤疤之类的必备项目吗？好嘞，该我了！
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   请便。
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#3",focus=1)]
[name="能天使"]   ......不好，这么一想，我好像都不太清楚你的黑料！
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   好孩子不该知道那么多喔。
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#3",focus=1)]
[name="能天使"]   你是我老姐吗！？
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#4",focus=2)]
[name="莫斯提马"]   欸，差不多吧。
[Character(name="char_325_bison_1#2")]
[name="拜松"]   ......
[name="拜松"]   （这两个人好像关系很好呢，因为都是拉特兰人吗？）
[name="拜松"]   （而且能天使竟然也会被抢走话茬......）
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1#3",focus=1)]
[name="能天使"]   那个......莫斯提马。我还是有一点小问题要问啦，小小的问题。
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   嗯？
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1",focus=1)]
[name="能天使"]   为什么这个时候回来？
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   唔，嗯，原因是有不少啦，怎么说呢。
[name="莫斯提马"]   第一，是工作。
[name="莫斯提马"]   第二，龙门安魂节总是会搞促销嘛，回龙门凑个热闹。
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1",focus=1)]
[name="能天使"]   ......那么多年的安魂夜你都不知所踪，偏偏在今年回来？
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   其实你想问的不是这个吧？
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1",focus=1)]
[name="能天使"]   诶......你察觉到了就直接告诉我嘛。
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   呵呵，难得看到你纠结的样子，让人很怀念。
[name="莫斯提马"]   而且，不管怎么说，也不能当着来参观学习的人面说那些弯弯绕绕的话题呢。
[Character(name="char_325_bison_1")]
[name="拜松"]   啊......没事，我会在后面跟着的，你们请便。
[Character(name="char_213_mostma_1#2")]
[name="莫斯提马"]   这可不行，还不排除被追踪的可能性。
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#2",focus=1)]
[name="能天使"]   啊！用拜松当借口也太狡猾了吧！
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#2",focus=2)]
[name="莫斯提马"]   先和德克萨斯他们汇合吧，那么多吓人的黑手党还在虎视眈眈呢。
[name="莫斯提马"]   我不在的时候，你们总是这么惹麻烦吗？
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#2",focus=1)]
[name="能天使"]   也算不上经常？每周有个四五六七八天的样子？
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#4",focus=2)]
[name="莫斯提马"]   ......嗯，的确不太经常。
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1#4",focus=1)]
[name="能天使"]   那你呢？去了哪里？
[name="能天使"]   你知道我刚见到老板的时候，老板说你已经离开龙门了，那种长跑到终点线前摔了一跤的感觉吗？
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   很多地方，多到数不清。
[name="莫斯提马"]   来到一座无人问津的村子，接下一封信，再前往群山的另一面，追着移动城市跑，就这样。
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1",focus=1)]
[name="能天使"]   听着真孤独呢。
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   但写成游记的话说不定能大卖？
[Character(name="char_325_bison_1#2")]
[name="拜松"]   莫斯提马小姐，去过所有国家吗？
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   大部分吧，羡慕吗？
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   ......有一点，一般的信使是不会有这样的机会的。
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   会有机会的。不过你可别指望企鹅物流哦，我们是不能用常理来判断的。
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   关于这点，我已经心知肚明了......
[Character(name="char_325_bison_1",name2="char_213_mostma_1#5",focus=2)]
[name="莫斯提马"]   在漫漫大漠中坐着卡车，盯着落日穿过黄沙，听着是很浪漫，但当浪漫持续上百个小时的时候，也就消磨殆尽了。
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#5",focus=1)]
[name="能天使"]   黄沙落日我是没怎么见到过啦，但你不觉得今天沙尘很大吗？
[name="能天使"]   这几年龙门的空气质量下降了不少喔，该增加几台空气净化器了！
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#2",focus=2)]
[name="莫斯提马"]   空气质量吗......也许吧。
[name="莫斯提马"]   能天使，拜松，虽然很抱歉，但你们得先——
[Character(name="char_103_angel_1#7",name2="char_325_bison_1#2")]
[name="拜松&能天使"]   又来？
[Character(name="char_213_mostma_1#3")]
[name="莫斯提马"]   哎呀，我对自己离开的时机拿捏的还是比较好的吧？
[Character(name="char_103_angel_1#7",name2="char_213_mostma_1#3",focus=1)]
[name="能天使"]   ......你认真的？
[Character(name="char_103_angel_1#6",name2="char_213_mostma_1#3",focus=1)]
[name="能天使"]   但是对你而言只是几个小时，对我而言可是——
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1#3",focus=1)]
[name="能天使"]   算了，莫斯提马！回头请我吃饭！必须！
[Character(name="char_103_angel_1#3",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   ——知道啦知道啦。
[name="莫斯提马"]   ......真是的，今晚还真热闹。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Charac

... (全文8378字符)
```

### level_act5d0_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Dialog]
[Character]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_lungmen_n",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=0.5, block=true)]
11:45 P.M.    天气/多云
龙门市区，露天咖啡吧
[Dialog]
[Delay(time=0.4)]
[Character(name="avg_npc_035")]
[name="伊斯"]   ——不错的香味。
[name="伊斯"]   露天咖啡吧，三明治，烛光，人流，糖果的香气。
[name="伊斯"]   如果没有这位小姐把我盯得死死的。我也许会更轻松一些。
[Character(name="char_300_phenxi_1#3",name2="avg_npc_035",focus=1)]
[name="？？？"]   ......我只是偶然路过，但是你手上拿着的东西似乎不太可以用偶然解释。
[Character(name="char_300_phenxi_1#3",name2="avg_npc_035",focus=2)]
[name="伊斯"]   我解释过。莫斯提马正作为企鹅物流的一员完成着她的委托。而我也只是帮她代为保管这把法杖。
[Character(name="char_300_phenxi_1#3",name2="avg_npc_035",focus=1)]
[name="？？？"]   你觉得我会放走一个对着她的法杖自言自语的怪胎吗？
[Character(name="char_300_phenxi_1#3",name2="avg_npc_035",focus=2)]
[name="伊斯"]   怪、怪胎......这就请当做没有看见吧。
[Character(name="char_300_phenxi_1",name2="avg_npc_035",focus=1)]
[name="？？？"]   ......
[Character(name="char_300_phenxi_1",name2="avg_npc_035",focus=2)]
[name="伊斯"]   她不会有事的。
[Character(name="char_300_phenxi_1",name2="avg_npc_035",focus=1)]
[name="？？？"]   我没有在担心她。
[Character(name="char_300_phenxi_1",name2="avg_npc_035",focus=2)]
[name="伊斯"]   她也不会惹事的。
[Character(name="char_300_phenxi_1",name2="avg_npc_035",focus=1)]
[name="？？？"]   ......但愿吧。
[Character(name="char_300_phenxi_1",name2="avg_npc_035",focus=2)]
[name="伊斯"]   ......
[Character(name="char_300_phenxi_1",name2="avg_npc_035",focus=1)]
[name="？？？"]   ......
[Character(name="avg_npc_035")]
[name="伊斯"]   ......（也许我应该乖乖呆在酒店里。）
[Dialog]
[Character]
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.8, crossfade=1.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="char_213_mostma_1#2")]
[name="莫斯提马"]   哟，你在这里，刚才那是怎么回事？
[Character(name="avg_npc_034",fadetime=2,block=true)]
[Delay(time=2)]
[name="鼠王"]   ......突然心血来潮罢了。
[Character(name="char_213_mostma_1#2",name2="avg_npc_034",focus=1)]
[name="莫斯提马"]   你的心血来潮是不是太用力了点？明明企鹅物流也在场。
[name="莫斯提马"]   而且你也一把年纪了，总是这么拼命，不会短命吗？
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   你觉得我出了几分力？
[Character(name="char_213_mostma_1#3",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   ......是吗。
[name="莫斯提马"]   那至少稍微收敛一些你的杀气如何？我都快不敢当着你的面说话了。
[name="莫斯提马"]   发生了什么？
[Character(name="char_213_mostma_1#3",name2="avg_npc_034",focus=2)]
[name="鼠王"]   嗯，也许我小看了年轻人的警戒心，龙门的年轻人总是会让我吃惊。
[Character(name="char_213_mostma_1#3",name2="avg_npc_034#5",focus=2)]
[name="鼠王"]   没什么大事，不过是有几个失控的傀儡，误伤了一位尽心尽责的鱼丸师傅，仅此而已。
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#5",focus=1)]
[name="莫斯提马"]   “仅此而已”？你应该学会管理一下表情，再来说这种话。
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   ......一直保持的微笑就失去了微笑的意义。比起你，我倒还轻松一点。
[Character(name="char_213_mostma_1",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   这难道不在你的预料之内吗？
[name="莫斯提马"]   比如，为了防止企鹅物流和黑手党的冲突不好收尾，先找一个可以亲自惩戒他们的借口，之类的。
[Character(name="char_213_mostma_1",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   ——你这丫头，陪着那只企鹅胡闹，真的是暴殄天物。
[Character(name="char_213_mostma_1#3",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   哪里哪里。
[Character(name="char_213_mostma_1#3",name2="avg_npc_034",focus=2)]
[name="鼠王"]   ......但我也没有允许他们随意践踏贫民窟。我从未允许。
[name="鼠王"]   我已经尽量容忍了他们的僭越，但他们还是坏了规矩。
[name="鼠王"]   本以为他们和叙拉古那点若有若无的联系可以为龙门带来那么一丁点有趣的利益......真是让人失望。
[Character(name="char_213_mostma_1#4",name2="avg_npc_034",focus=1)]
[name="莫斯提马"]   停一停......干嘛和我说这么多？下一步是要把我灭口了吗？
[Character(name="char_213_mostma_1#4",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   老人也是需要发发牢骚的。
[Character(name="char_213_mostma_1",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   是吗，那我就当只是一场安魂节狂欢吧。刚才你说的那些东西我全部都没听见喔。
[name="莫斯提马"]   那些黑手党闹的越大，说不定事后的尾款我就能拿到更多。
[Character(name="char_213_mostma_1",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   那有了钱之后呢？
[Character(name="char_213_mostma_1#3",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   先把那家糖果铺子买下来。
[Character(name="char_213_mostma_1#3",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   呵呵，你还真是情有独钟。
[name="鼠王"]   好啊，除了地下室，其他东西随你搬走。
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   果然是有地下室的吗......你就不能稍微保护一下我的美好回忆？
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   那可是我的铺子。
[Character(name="char_213_mostma_1#4",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   真是太可惜了，我本以为你退休之后真的会去当一个杂货铺老板。
[Character(name="char_213_mostma_1#4",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   也许吧，如果退休的时候我还活着的话。
[name="鼠王"]   时候不早了，接下来狂欢才算正式开始。戏子伶人都已经各就各位。
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   不打算继续袖手旁观了？
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#9",focus=2)]
[name="鼠王"]   ......这里风景不错吧。
[name="鼠王"]   安魂夜是恭送亡者的节日，而龙门终归是我们的城市。
[name="鼠王"]   活着的人们热热闹闹的，亡魂才能没有遗憾地离去。
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#7",focus=2)]
[name="鼠王"]   而且一个半只脚踏进棺材里的老鼠，要是不活动活动筋骨，说不定会被某些别有用心的家伙误当成已死的亡灵喔。
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#7",focus=1)]
[name="莫斯提马"]   那该怎么热闹？
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   就该如此热闹。
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   ——啊，原来如此。
[name="莫斯提马"]   那这场安魂的花销似乎有点大，嗯，甚至有点浪费。
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   你很聪明。
[Character(name="char_213_mostma_1#3",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   也是，否则魏长官早就来找你的麻烦了。
[Character(name="char_213_mostma_1#3",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   别说那么吓人的事，我可不想再和近卫局打交道了，太麻烦了。
[name="鼠王"]   而这一出好戏的精髓就在于，所有的开销，都由演员自己承担。
[stopmusic(fadetime=2)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Delay(time=0.4)]
[PlayMusic(intro="$penguinlogistics_

... (全文10462字符)
```

### level_act5d0_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[Dialog]
[Character]
[Delay(time=1)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Character]
[Dialog]
[Character(name="char_243_waaifu_1#3")]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[Delay(time=1)]
[Character(name="char_243_waaifu_1#3")]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.7, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=0.5)]
[Character(name="avg_npc_028")]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_028")]
[name="甘比诺"]   ......该结束了。
[Character(name="avg_npc_028",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   唔——！
[Dialog]
[Character(name="avg_npc_028")]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_028",name2="char_243_waaifu_1#3",focus=1)]
[name="甘比诺"]   你很强，让我见识到了一些有趣的功夫。
[name="甘比诺"]   但是我不能陪你继续耗下去了。
[name="甘比诺"]   很抱歉，你，你的同伴，还有那个叛徒，都要死在这里。
[Character(name="avg_npc_028#3")]
[name="甘比诺"]   所有人，抬起武器。
[Character(name="avg_npc_031",name2="avg_npc_031")]
[name="黑帮A"]   准备！
[Character(name="avg_npc_028#3",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   想利用人数优势吗......
[Character(name="avg_npc_027#4")]
[name="卡彭"]   没那么简单，甘比诺。
[name="卡彭"]   听着，“首领”开火的一瞬间，就宣告了正式的决裂，你们从此和甘比诺家族没有任何关系，不要手下留情。
[Character(name="avg_npc_031",name2="avg_npc_031")]
[name="黑帮B"]   明白！
[Character(name="char_272_strong_1#4",name2="char_243_waaifu_1#4",focus=1)]
[name="孑"]   槐琥，这边也......
[Character(name="char_272_strong_1#4",name2="char_243_waaifu_1#4",focus=2)]
[name="槐琥"]   我们被夹在中间了呢。
[Character(name="avg_npc_028#3",name2="avg_npc_027#4",focus=1)]
[name="甘比诺"]   哈，家族四分五裂，原本的猎物全都变成了猎手，踩着互相设下的陷阱混战一场。
[name="甘比诺"]   这情况真是和叙拉古那次如出一辙......但这一次，我们必须赢下赌局。
[Character(name="avg_npc_028#3",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   可惜你的赌运向来不顺。
[Character]
[name="鼠王"]   不，够了，停手吧。
[Character(name="avg_npc_027")]
[name="卡彭"]   ——！
[Character(name="avg_npc_028#2")]
[name="甘比诺"]   ——你竟然会离开那个肮脏的地方来到这里？
[Dialog]
[Character]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_034",fadetime=2,block=true)]
[Delay(time=2)]
[name="鼠王"]   甘比诺先生，很遗憾，我给了你和你的家族很多次机会。
[Character(name="avg_npc_034",name2="avg_npc_028#2",focus=2)]
[name="甘比诺"]   我们根本没有信任可言，你真以为我会把家族交给一个西西里人之外的怪物？
[Character(name="avg_npc_034",name2="avg_npc_028#2",focus=1)]
[name="鼠王"]   西西里人。尽管我这辈子都未曾踏足过叙拉古的城邦，但我也知道，你们早已经不配如此称呼自己。
[Character(name="avg_npc_034",name2="avg_npc_028#2",focus=2)]
[name="甘比诺"]   ......你到底准备做什么？
[Character(name="avg_npc_034#3",name2="avg_npc_028#2",focus=1)]
[name="鼠王"]   提问的机会已经用完了，年轻人，在龙门可没有那么多犯规机会。
[name="鼠王"]   有些是你，有些是那边那位，无论如何，你们越界过多了。
[Character(name="avg_npc_027#2",name2="avg_npc_034#3",focus=1)]
[name="卡彭"]   ......
[Character(name="avg_npc_034#3",name2="avg_npc_028#2",focus=2)]
[name="甘比诺"]   你想反悔？
[Character(name="avg_npc_034",name2="avg_npc_028#2",focus=1)]
[name="鼠王"]   我从未承诺。
[Character(name="avg_npc_034",name2="avg_npc_028#3",focus=2)]
[name="甘比诺"]   哼。你真觉得能对付得了我们？
[name="甘比诺"]   你只是坐在下水道里的王座上，对着那些不得不为你卖命的人指指点点，不是吗？
[Character(name="avg_npc_034#3",name2="avg_npc_028#3",focus=1)]
[name="鼠王"]   作为一家之长，你应当学会开阔一些视野。
[name="鼠王"]   比起我们所经历的一切，你在叙拉古的挫折不过是九牛一毛。
[Character(name="avg_npc_034#3",name2="avg_npc_028#3",focus=2)]
[name="甘比诺"]   闭嘴！
[Character(name="avg_npc_034#7",name2="avg_npc_028#3",focus=1)]
[name="鼠王"]   ......那么，你可曾见过真正的钢铁洪流兵临城下。
[name="鼠王"]   移动着的城市互相倾轧，硝烟浸染天空，濒死的感染者腐烂在垃圾堆旁，嘶声力竭？
[name="鼠王"]   你一无所知，却妄想要对抗一座城市。
[Character(name="avg_npc_027#4")]
[name="卡彭"]   （他的力量......超出常理，他和那个女人身边的......）
[name="卡彭"]   （该死，至少现在不能继续刺激鼠王......还没到时候......）
[Character(name="avg_npc_034#7",name2="avg_npc_028#2",focus=2)]
[name="甘比诺"]   ......你自以为能代表整个龙门？ 
[Character(name="avg_npc_034#3",name2="avg_npc_028#2",focus=1)]
[name="鼠王"]   龙门并不能代表我。
[Character(name="avg_npc_034#3",name2="avg_npc_028#3",focus=2)]
[name="甘比诺"]   废话少说！喝啊——！
[Dialog]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_243_waaifu_1#4")]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_028#2")]
[name="甘比诺"]   ——
[Character(name="avg_npc_028#2",name2="char_243_waaifu_1#4",focus=2)]
[name="槐琥"]   没有人允许，你对这位老人出手。
[Character(name="char_272_strong_1#4")]
[name="孑"]   ......躲开点，槐琥！
[Dialog]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=tru

... (全文14222字符)
```

### level_act5d0_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Dialog]
[Character]
[Background(image="bg_lmstreet_1",screenadapt="coverall",fadetime=2,block=true)]
[PlayMusic(intro="$penguinlogistics_intro", key="$penguinlogistics_loop", volume=0.8, crossfade=1.5)]
0:38 P.M.    天气/沙尘
龙门市区，广场，露天派对
[Dialog]
[Character(name="char_325_bison_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="拜松"]   虽然我们跟着指示过来了，但为什么......是个露天派对？
[Character(name="char_103_angel_1#8")]
[name="能天使"]   看到那个蜡烛了没！好大！
[Character(name="char_102_texas_1",name2="char_103_angel_1#8",focus=1)]
[name="德克萨斯"]   能天使，安静一点。
[name="德克萨斯"]   空气里甜味太重了，稍微有点不舒服。
[Character(name="char_201_moeshd#3")]
[name="可颂"]   嗯......要是下次在这里申请一个摊位的话，应该会大赚的吧。
[Character(name="char_101_sora_1#4",name2="char_102_texas_1",focus=1)]
[name="空"]   德克萨斯，老板有消息吗？
[Character(name="char_101_sora_1#4",name2="char_102_texas_1",focus=2)]
[name="德克萨斯"]   暂时没有，也许他就在哪里酩酊大醉吧。
[name="德克萨斯"]   ......能天使，把我头上的东西摘下来。
[Character(name="char_102_texas_1",name2="char_103_angel_1#7",focus=2)]
[name="能天使"]   为什么嘛！
[name="能天使"]   我可是因为这盏日光灯，根本没有办法戴这种高高的派对帽喔？我很羡慕的喔？
[Character(name="char_101_sora_1#3",name2="char_103_angel_1#7",focus=1)]
[name="空"]   那如果强行戴上会怎么样？
[Character(name="char_102_texas_1",name2="char_103_angel_1#8",focus=2)]
[name="能天使"]   就像是宿醉醒来的时候发现自己在德克萨斯的副驾驶上高歌猛进的感觉。
[Character(name="char_201_moeshd#5")]
[name="可颂"]   ......那真是不得了呢。
[Character(name="char_101_sora_1#4",name2="char_103_angel_1#8",focus=1)]
[name="空"]   你还真的这么试过啊......
[Character(name="char_103_angel_1#3")]
[name="能天使"]   所以，老板在哪儿呢？
[Character(name="char_325_bison_1#4")]
[name="拜松"]   这里人太多了，如果敌人追到了这里，会把普通人都卷进去的——
[Character(name="char_272_strong_1")]
[name="孑"]   啊。
[Character(name="char_243_waaifu_1")]
[name="槐琥"]   ......是你们，企鹅物流。
[Character(name="char_102_texas_1",name2="char_243_waaifu_1",focus=1)]
[name="德克萨斯"]   我记得你是......那个侦探所的打工妹......
[Character(name="char_272_strong_1",name2="char_103_angel_1#7",focus=2)]
[name="能天使"]   旁边这位就是传闻中一人一刀走码头的分舵主？
[Character(name="char_272_strong_1",name2="char_103_angel_1#7",focus=1)]
[name="孑"]   不是，呃，怎么还有这么夸张的版本......
[name="孑"]   我只是个普通的小商贩，啊，今晚还兼职鱼丸师傅。
[Character(name="char_102_texas_1",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   你就是德克萨斯？
[name="槐琥"]   今天晚上发生的事情，你们可别说自己不知道。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#3",focus=1)]
[name="孑"]   槐琥，用不着这么咄咄逼人的，她们应该也只是......
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=2)]
[name="槐琥"]   我知道。但是这种事件发生的次数实在是多到幽默。
[name="槐琥"]   如果不把其他人卷进去也就罢了。
[name="槐琥"]   殃及无辜，让平民蒙受财产损失，你们自己就没有作为合法公民的自觉吗？
[Character(name="char_102_texas_1#2")]
[name="德克萨斯"]   ......
[Character(name="char_325_bison_1#2")]
[name="拜松"]   （好像完全无法反驳！）
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   ......所以呢？
[Character(name="char_102_texas_1",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   所以，有必要纠正你们的劣根性。
[Character(name="char_101_sora_1#4")]
[name="空"]   用、用不着直接拉开拳架吧，我们也知道今晚给大家添了很多麻烦，但是有话好好说嘛。
[stopmusic(time=2)]
[Character(name="char_102_texas_1",name2="char_243_waaifu_1#3",focus=1)]
[name="德克萨斯"]   ——好啊。
[Character(name="char_101_sora_1#3",name2="char_102_texas_1",focus=1)]
[name="空"]   德克萨斯！？
[Character(name="char_102_texas_1#4",name2="char_243_waaifu_1#3",focus=1)]
[name="德克萨斯"]   话说在前头，今晚的事情，对我而言，同样莫名其妙，而且，很累。
[name="德克萨斯"]   所以我现在的心情实在不怎么好。
[name="德克萨斯"]   你明白吗？
[Character(name="char_102_texas_1#4",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   一对一，我赢了，你们接下来就得乖乖遵纪守法。
[name="槐琥"]   ......至少一个月。
[Character(name="char_325_bison_1")]
[name="拜松"]   （一个月就够了！？）
[Character(name="char_102_texas_1",name2="char_243_waaifu_1#3",focus=1)]
[name="德克萨斯"]   我赢了，就让你们那些成天不务正业的家伙多管好自己的工作，少管闲事。
[Character(name="char_102_texas_1",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   这说的倒是没错......但是，我是不会手下留情的！准备好！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9,block=true)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral",block=true)]
[PlaySound(key="$fightgeneral",block=true)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_272_strong_1")]
[name="孑"]   唉，怎么就变成这样了呢。
[Character(name="char_325_bison_1")]
[name="拜松"]   等等！都冷静一下！再怎么说，在市中心打架斗殴也有点太——
[Dialog]
[Character]
[name="酒客"]   好功夫，打得好！！
[name="酒客"]   狼小姐也不要输啊！打！小心背后！
[name="酒客"]   好久没见过这么漂亮的炎国功夫了！多耍几招啊！
[Character(name="char_325_bison_1#2")]
[name="拜松"]   这不是表演啊！
[Character(name="char_101_sora_1#2")]
[name="空"]   德克萨斯！加油！
[Character(name="char_103_angel_1#8")]
[name="能天使"]   小心脚下！是佯攻！
[Character(name="char_325_bison_1")]
[name="拜松"]   你们也不要跟着起哄啊！
[Dialog]
[Character(name="char_243_waaifu_1#3")]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_102_texas_1#4")]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9,block=true)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=1)]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(intro="$marketplace_intro", key="$marketplace_loop", volume=0.8, crossfade=1.5)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_272_strong_1")]
[name="孑"]   汽水，你们要吗。
[Character(name="char_201_moeshd#2",name2="char_272_strong_1",focus=1)]
[name="可颂"]   啊！谢谢。但是你不打算稍微劝个架吗？
[Character(name="char_201_moeshd#2",name2="char_272_strong_1",focus=2)]
[name="孑"]   阻止不了，看样子也知道吧。
[Character(name="char_325_bison_1")]
[name="拜松"]

... (全文11634字符)
```

### level_act5d0_10_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.9)]
[Character]
[name="小女孩"]  鼠爷爷~！
[Character(name="avg_npc_034#3")]
[name="鼠王"]   怎么是你这小妮子，一个人跑来干嘛啦？灰头土脸的，又钻通风管了？
[Character]
[name="小女孩"]  嘿嘿，鼠爷爷，这是大门口的何叔给我的！何叔说我个子小跑得快，一刻钟之内送到就请我吃酸奶！你要给我作证！
[Character(name="avg_npc_034#3")]
[name="鼠王"]   好，爷爷给你作证。你先去吧。
[Character]
[name="小女孩"]  谢谢爷爷！爷爷再见~！
[Dialog]
[stopmusic(fadetime=2)]
[Delay(time=2)]
[Character(name="avg_npc_034")]
[name="鼠王"]   ......
[Character(name="avg_npc_033")]
[name="看似普通的居民"]   老爷子。怎么了？
[Character(name="avg_npc_034")]
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.8, crossfade=1.5)]
[name="鼠王"]   还记得来找过我们的那几个叙拉古人吗？他们的“家族”已经完全从叙拉古转移到了龙门。
[Character(name="avg_npc_034",name2="avg_npc_033",focus=2)]
[name="看似普通的居民"]   需要联系线人吗？
[Character(name="avg_npc_034",name2="avg_npc_033",focus=1)]
[name="鼠王"]   没必要，按兵不动，他们会找上门来的。
[Character(name="avg_npc_034",name2="avg_npc_033",focus=2)]
[name="看似普通的居民"]   为了什么？
[Character(name="avg_npc_034",name2="avg_npc_033",focus=1)]
[name="鼠王"]   为了在这里生存下去。
[Character(name="avg_npc_034",name2="avg_npc_033",focus=2)]
[name="看似普通的居民"]   这可不需要经过任何人的同意，那他们怎么不去和天灾聊聊？
[Character(name="avg_npc_034#9")]
[name="鼠王"]   天灾要是会说话，兴许就用不着人们窝里斗了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_034",name2="avg_npc_027",focus=2)]
[name="卡彭"]   ——正如您所言，鼠王先生。
[name="卡彭"]   龙门有自己的规则，魏彦吾在十几年前就默认了这个铁律，我们绝不敢轻易违反。
[name="卡彭"]   但您才是执行者，这也是我们今天冒昧来访的原因。
[Character(name="avg_npc_034",name2="avg_npc_027",focus=1)]
[name="鼠王"]   ......你们想铲除企鹅物流，取而代之。
[Character(name="avg_npc_034",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   正是。
[Character(name="avg_npc_034",name2="avg_npc_027#2",focus=1)]
[name="鼠王"]   你们对他们缺乏了解，西西里人。这笔生意你们得不到任何好处。
[Character(name="avg_npc_028#2")]
[name="甘比诺"]   啧。
[Character(name="avg_npc_028#2",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   （甘比诺！）
[Character(name="avg_npc_028#3",name2="avg_npc_034",focus=1)]
[name="甘比诺"]   你是在说我们赢不了吗？“鼠王”先生？
[Character(name="avg_npc_028#3",name2="avg_npc_034",focus=2)]
[name="鼠王"]   “输赢”不是谈生意的时候应该出现的词，也难怪你逃离了叙拉古，你的确不是那个女人的对手。
[Character(name="avg_npc_028#3",name2="avg_npc_034",focus=1)]
[name="甘比诺"]   你敢侮辱我的家族？
[Character(name="avg_npc_028#3",name2="avg_npc_027#4",focus=2)]
[name="卡彭"]   你闭嘴，甘比诺！我们要的是针对企鹅物流的——
[Character(name="avg_npc_034#3",name2="avg_npc_027#4",focus=1)]
[name="鼠王"]   只要遵循规则，我没有庇护企鹅物流的理由。
[Character(name="avg_npc_034#3",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   ——意思是？
[Character(name="avg_npc_034#3",name2="avg_npc_027#2",focus=1)]
[name="鼠王"]   企鹅物流是明面上的合法公司，能庇护他们的只有龙门的钢铁律法。
[name="鼠王"]   不过他们有时候的确触犯了各方面的问题，而且从来不以为然。
[name="鼠王"]   但是切记，西西里人，切记不要越界。
[name="鼠王"]   另类的秩序不代表没有秩序，叙拉古应当最明白这个道理。可千万别再麻烦我这把老骨头动手了，答应我。
[Character(name="avg_npc_034#3",name2="avg_npc_027",focus=2)]
[name="卡彭"]   ——我明白。
[Dialog]
[Character]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_034")]
[name="鼠王"]   ......龙门这个季节的星星，比想象中的多。
[name="鼠王"]   放在桌上的茶，也凉了吧。
[Dialog]
[Character]
[PlayMusic(intro="$gorgeousdebut_intro", key="$gorgeousdebut_loop", volume=0.8, crossfade=1.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character]
[name="路人"]  这是老爷的......喂，上工了。
[name="路人"]  我不聋，赶紧打，打完正好去喝早茶。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_lungmen_n",screenadapt="coverall")]
[Blocker(a=0, fadetime=0.5, block=true)]
[name="黑帮"]   看来轮到我们了。
[name="黑帮"]   反正之前也打过招呼了，把弩枪都放下，注意不要误伤到无关人士。
[name="黑帮"]   ......该适应新的规则了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Character(name="char_201_moeshd#5")]
[name="可颂"]   我们是不是被包了个圆？里三层外三层的那种？
[Character(name="char_201_moeshd#5",name2="char_103_angel_1#8",focus=2)]
[name="能天使"]   啊，戚风蛋糕卷？
[Character(name="char_102_texas_1")]
[name="德克萨斯"]   鼠王是贫民窟的话事人，他的爪牙自然无处不在。
[Character(name="char_102_texas_1",name2="char_325_bison_1#4",focus=2)]
[name="拜松"]   ......为什么不早说？
[Character(name="char_102_texas_1",name2="char_325_bison_1#4",focus=1)]
[name="德克萨斯"]   我以为那只是个都市传说，而且我也不知道他真的是只老鼠。谁会这么取外号？
[Character(name="char_201_moeshd#5")]
[name="可颂"]   说什么人流密集不好动手，这哪里有什么无辜民众，明明全是敌人嘛！
[Character(name="char_101_sora_1#2")]
[name="空"]   寸步难行呢。
[Character(name="char_325_bison_1#4")]
[name="拜松"]   现在怎么办？
[Character(name="char_102_texas_1",name2="char_325_bison_1#4",focus=1)]
[name="德克萨斯"]   你一直在问怎么办，不如你自己想想？
[Character(name="char_102_texas_1",name2="char_325_bison_1#4",focus=2)]
[name="拜松"]   ......
[Character(name="char_102_texas_1#4")]
[name="德克萨斯"]   要来了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="avg_npc_034")]
[name="鼠王"]   ......你来了。这里能清楚地看见下面的情况。
[Character(name="avg_npc_034#3")]
[name="鼠王"]   你的朋友们正陷入苦战，你不打算去帮个忙吗？
[Character(name="char_213_mostma_1",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   我可没听说你会下这么重的手。
[Character(name="char_213_mostma_1",name2="avg_npc_034#3",focus=2)] 
[name="鼠王"]   我也不是所有事都会和年轻人推心置腹的。
[Character(name="char_213_mostma_1",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   也是，我总是会忘记，你是个什么样的人物。
[Character(name="char_213_mostma_1",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   很多人会忘记这一点，他们都死无葬身之地。你已经属于特别优待了。
[Character(name="char_213_most

... (全文16209字符)
```

### level_act5d0_10_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Dialog]
[Character]
[Delay(time=1)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[PlayMusic(intro="$penguinlogistics_intro", key="$penguinlogistics_loop", volume=0.8, crossfade=1.5)]
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   我们......就这么看着？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   就这么看着。虽然不知道是怎么回事。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   但反正没有殃及无辜对吧？
[name="孑"]   这么多美食和饮料，就这么浪费了......
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   这么浪费看的我都心疼。但我总觉得，这场斗殴好像也是派对的一部分？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   安排好的吗？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   也不太像，啊，有人冲过来了。
[Character(name="char_272_strong_1")]
[name="孑"]   呃？
[Dialog]
[Character(name="char_243_waaifu_1#4")]
[PlaySound(key="$fightgeneral",block=true)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="avg_npc_031")]
[name="黑帮"]   呃......！怎么......好像......打错人......
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   呆在这儿是不是有点不太安全？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   反正回事务所也不知道该干嘛，都快通宵了。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   你不是明天还要考试？下午？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   ......
[Character(name="char_243_waaifu_1#2")]
[name="槐琥"]   ......糟。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_035")]
[name="伊斯"]   那边两位，似乎不是这场闹剧的相关人员。
[name="伊斯"]   应该建议他们远离这里，不小心会受伤的。
[Character(name="avg_npc_035",name2="char_300_phenxi_1",focus=2)]
[name="？？？"]   ......慢着，那个肚子上被开了个洞的人，是企鹅物流的大帝吧？
[name="？？？"]   他死了喔，你们就不慌张吗？
[Character(name="avg_npc_035",name2="char_300_phenxi_1",focus=1)]
[name="伊斯"]   慌张？怎么会。
[name="伊斯"]   大帝先生每个月都会有那么几次玩火自焚。我们习以为常。
[Character(name="avg_npc_035",name2="char_300_phenxi_1",focus=2)]
[name="？？？"]   哪怕他死了？
[Character(name="avg_npc_035",name2="char_300_phenxi_1",focus=1)]
[name="伊斯"]   是的。
[Character(name="avg_npc_035",name2="char_300_phenxi_1#3",focus=2)]
[name="？？？"]   ......莫斯提马也许真的不该和你们走得太近。
[Character(name="avg_npc_035",name2="char_300_phenxi_1#3",focus=1)]
[name="伊斯"]   你在担心她？
[Character(name="avg_npc_035",name2="char_300_phenxi_1#3",focus=2)]
[name="？？？"]   我只是来确保她没有做出什么出格的事情。
[name="？？？"]   但是，嗯，真是拙劣的演技，既然她那么有闲情逸致，那看来应该没什么值得注意的了。
[name="？？？"]   先走一步。还有，不要告诉她我来过这里，等完事了我会去找她的。
[Dialog]
[Character]
[stopmusic(fadetime=2)]
[playsound(key="$d_gen_walk_n")]
[Delay(time=1)]
[Character(name="avg_npc_035")]
[name="伊斯"]   ......走掉了。
[name="伊斯"]   突然出现，突然质问，又突然离开。
[name="伊斯"]   拉特兰现在已经变成这个风格了？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, fadetime=2, block=true)]
[PlayMusic(intro="$gorgeousdebut_intro", key="$gorgeousdebut_loop", volume=0.8, crossfade=1.5)]
[Character(name="char_213_mostma_1",name2="avg_npc_034#7",focus=2)]
[name="鼠王"]   ......呵，我突然开始有些羡慕你这样的年轻人了。
[name="鼠王"]   你们总是喜欢自顾自地选择自己的道路，全然不顾自己在时局中的位置。
[Character(name="char_213_mostma_1#4",name2="avg_npc_034#7",focus=1)]
[name="莫斯提马"]   我也是有在好好工作的。
[Character(name="char_213_mostma_1#4",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   但是从来没有人能够查清你的根底。
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   如果你真的查到了什么，那才是最麻烦的事情。
[Character(name="char_213_mostma_1#2",name2="avg_npc_034",focus=2)]
[name="鼠王"]   说得对，有些事情的确不该过度深究，特别是和信使莫斯提马扯上关系的时候。
[Character(name="char_213_mostma_1",name2="avg_npc_034",focus=1)]
[name="莫斯提马"]   这算什么？职业歧视吗？
[Character(name="char_213_mostma_1",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   只是经验谈。
[name="鼠王"]   现在，先暂停一下吧。
[dialog]
[Character(name="avg_npc_034#3")]
[Blocker(a=0.4, r=0.9, g=0.8, b=0.7, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_driftsand", volume=0.9)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$e_skill_driftsand", volume=0.9)]
[Blocker(a=0,fadetime=4, block=true)]
[Character(name="char_213_mostma_1#4",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   唔。
[name="莫斯提马"]   法术被压制了.....？
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#3",focus=1)]
[name="莫斯提马"]   搞什么，原来一直在手下留情的人其实是你吗？
[Character(name="char_213_mostma_1#2",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   彼此彼此。
[name="鼠王"]   但至少，你拖延了足够的时间。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_031",name2="avg_npc_033",focus=2)]
[name="看似普通的居民"]   你这臭小子，怎么这么耐打......呃......
[Character(name="char_325_bison_1#4")]
[name="拜松"]   呼啊，呼啊，论耐力，我，可不会，输给任何人。
[Character(name="char_213_mostma_1#3")]
[name="莫斯提马"]   嗯，做得不错。
[name="莫斯提马"]   真亏你们能这么快解决那么多的敌人啊。
[Character(name="char_103_angel_1#8")]
[name="能天使"]   嘿，这次不会再让你一个人突然消失了。
[name="能天使"]   而且这家伙就是幕后黑手吧？当然要亲手暴揍他一顿啦！
[Character(name="char_201_moeshd#5")]
[name="可颂"]   今天的运动量真是超乎想象，唔，账单长度也是。
[name="可颂"]   德克萨斯姐，我感觉今晚有很多东西没法报销啊......
[Character(name="char_102_texas_1#2")]
[name="德克萨斯"]   不要问我，问老板去。
[Character(name="char_101_sora_1#4",name2="char_102_texas_1#2",focus=1)]
[name="空"]   但是老板他死了......
[Character(name="char_101_sora_1#4",name2="char_102_texas_1",focus=2)]
[name="德克萨斯"]   ......那就一会再说。
[Character(name="char_101_sora_1#4",name2="char_102_texas_1",focus=1)]
[name="空"]   话说，没有人去照顾一下老板的尸体吗？就那么躺在地上被踩来踩去的，是不是有点......
[dialog]
[Character]
[stopmusic(fadetime=2)]
[playsound(key="$d_gen_walk_n")]
[Delay(time=1)]
[Character(name="avg_npc_034#3")]
[name="鼠王"]   看来，人都到齐了。
[name="鼠王"]   ......年轻人总会做出自己的选择。
[name="鼠王"]   即使会在风雨飘摇的大地上粉身碎骨，你们也总是如此执意行事。
[Cha

... (全文24890字符)
```

### level_act5d0_ex01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Dialog]
[Delay(time=1)]
[PlayMusic(intro="$bar_intro", key="$bar_loop", volume=0.8,crossfade=1)]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Delay(time=0.4)] 
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_029")]
[name="管家"]   ——请在这里等待。
[name="管家"]   鼠王先生。
[Character(name="avg_npc_029",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   辛苦了，你先回去吧。
[name="鼠王"]   刚刚，不错的枪法。
[Character(name="avg_npc_029#2",name2="avg_npc_034#3",focus=1)]
[name="管家"]   谢谢您的夸赞，虽然很失礼，但您真的没有受伤吗？
[Character(name="avg_npc_029#2",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   怎么会。不过，如果你真的抱着杀了我的想法——
[Character(name="avg_npc_029#3",name2="avg_npc_034#3",focus=1)]
[name="管家"]   那我根本没有扣下扳机的机会。您就不要谦虚了，我和老爷都见识过您过去的模样。
[Character(name="avg_npc_029#3",name2="avg_npc_034",focus=2)]
[name="鼠王"]   那又如何，岁月不留情，今夜我再次认识到这个事实。
[name="鼠王"]   摆弄令他人畏惧的力量也会吞噬自身，陪那些初出茅庐的孩子们玩耍，竟然弄坏了我的宝贝大衣。
[Character(name="avg_npc_029",name2="avg_npc_034",focus=1)]
[name="管家"]   只是大衣？
[Character(name="avg_npc_029",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   针线活对我来说可是很艰巨的。
[name="鼠王"]   你已经完成了你的任务，信使，你先走吧，告诉你的主人，让他安心做好自己的事情。
[Character(name="avg_npc_029#2",name2="avg_npc_034#3",focus=1)]
[name="管家"]   ——我记下了，但老爷也许会想要亲自来见您一面，那么，容我告辞。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_034")]
[name="鼠王"]   ......嗯，这里真是一片狼藉，暴殄天物，不愧是那只企鹅干的好事。
[name="鼠王"]   ......这里还有一瓶完整的酒，嗯，看上去成色不错。
[name="鼠王"]   要来一杯吗？
[Dialog]
[playsound(key="$d_gen_walk_n")]
[Character(name="char_2005_weiyw_1")]
[name="魏彦吾"]   这可是鼠王亲自弯腰捡起的酒，我怎敢不喝？
[Character(name="char_2005_weiyw_1",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   哪里的话，魏长官。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034#3",focus=1)]
[name="魏彦吾"]   长官。我很久没从你嘴里听到这个称呼了。
[name="魏彦吾"]   你竟然会亲自参与这场闹剧，我以为你只会借企鹅物流的手——
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   老人应该有老人的样子，和蔼一些，参与进孩子们的活动之中。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   呵呵，我依旧对你的衰老没有实感。或许，是因为你的女儿一天比一天更像年轻时的你。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   我不知道她能走到哪一步，有些时候，我们应该放手，在这方面，我们似乎都做得不是很好。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   即使他们选的是一条断头路？
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   即使他们选的是一条断头路。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   呵，话说回来，哪条路真能走得长远？谁来决定？天灾吗？
[Character(name="char_2005_weiyw_1",name2="avg_npc_034#3",focus=1)]
[name="魏彦吾"]   ......也许你真的老了，林。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   你知道我为什么特别关注那个小信使吗？因为我想，也许她们之间有一些共同之处。
[name="鼠王"]   ——言归正传，也许你不应该亲自出现在这里，长官。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   附近有哪些“偶然路过”的“龙门市民”，我们心知肚明。
[Character(name="avg_npc_034")]
[name="鼠王"]   唉。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   鼠王也有叹气的时候。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   值得我叹气的事情有很多，我只是挑选了其中一件感慨一番。
[name="鼠王"]   ......说不定，也到了该退休的日子了。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   那可不行，龙门还不能失去鼠王。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   但可以失去林，我们都和过去大不相同。
[name="鼠王"]   没关系，至少，我会坚持到龙门足以失去鼠王的那一天。
[name="鼠王"]   那是我的女儿真正长大的那一天。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   你真的这么想吗？
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   我是他的父亲，也是贫民窟的鼠王，过去，曾是你的朋友，灰色的林。
[name="鼠王"]   也许我也没能下定决心。也许我已经做错了许多事情。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   ......你还在对以前的事情耿耿于怀，林。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   你将龙门夺回我们手中的时候，我答应过你，我会待在魏彦吾的阴影之中，你不必再来触碰这些腌臜的暗巷小道。
[name="鼠王"]   ——是啊，已经那么长时间了，正因为我答应了你，所以就有了鼠王。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   你牺牲了很多。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   别说这种假惺惺的话，我何时清白过？我们又何时清白过？
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   ......你恪守承诺，老朋友，但你也没有否认自己心怀不满。
[name="魏彦吾"]   是因为你的女儿吗？
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   我之所以用这么麻烦的方式驱逐那些叙拉古人，为的是什么，你再清楚不过。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   麻烦的对手有很多，但至少我信任你。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   信任和利用其实都是一回事。在其位谋其职罢了，我们该务实一些。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   ......以前，你很讨厌这么说话的。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   那可真巧，今夜有那么多的久别重逢，似乎没有一个令人满意。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   别这么说。现在，只是两个老朋友，在安魂夜之后的寒暄而已，也许我们都应该放轻松一点。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   你说的对，呼，天冷了，你似乎没有为那些老战友点上蜡烛的时间。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   这不会占用太多时间的，就在你离开了那里之后，我在。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   ......我可想象不出魏彦吾独自一人在墓地前献花的模样。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   我不会参加你的葬礼，但也许会在你坟前献一束花，那时你会知道的。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=2)]
[name="鼠王"]   ......你可还记得有人为了救你，这辈子都没法直起身来走路？
[Character(name="char_2005_weiyw_1",name2="avg_npc_034",focus=1)]
[name="魏彦吾"]   这样的人数不胜数，与我们并肩作战的，为我们慷慨赴死的。
[name="魏彦吾"]   而我一刻都未曾忘记过这些人。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   ——你的眼神从未改变，也许吧，兴许你会很长寿。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034#3",focus=1)]
[name="魏彦吾"]   总是有秘诀的。
[Character(name="char_2005_weiyw_1",name2="avg_npc_034#3",focus=2)]
[name="鼠王"]   罢了，你总得活久一些。
[Character(name="char_2005_weiyw_1",name2="avg_

... (全文12669字符)
```

### level_act5d0_ex02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Dialog]
[Character]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.8, crossfade=1.5)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="avg_npc_031",name2="avg_npc_031")]
[name="黑帮"]   鼠王先生。
[Character(name="avg_npc_034")]
[name="鼠王"]   唔，是你们。
[Character(name="avg_npc_034",name2="avg_npc_031",focus=2)]
[name="黑帮"]   他们怎么样了？
[Character(name="avg_npc_034",name2="avg_npc_031",focus=1)]
[name="鼠王"]   我说过，这座城市不需要流血，他们要是能逃得出去，就让他们逃吧。
[name="鼠王"]   怀念旧主是好事，你们用自己的效忠换来了其他同伴生存的权利，说明你们尚存良知，但千万不要奢求更多。
[Character(name="avg_npc_034",name2="avg_npc_031",focus=2)]
[name="黑帮"]   ......是、是的。但是后来的事情，已经明显僭越了龙门的规矩......
[Character(name="avg_npc_034#3",name2="avg_npc_031",focus=1)]
[name="鼠王"]   你们学的倒是挺快。
[name="鼠王"]   听说，远在叙拉古成为今天的模样之前，那时还必须苟且为生的黑手党之间，流传着一些默认的法则。
[name="鼠王"]   人人遵循，人人默许，在波涛汹涌的时局之中，黑手党反倒成为了最守信用的团体。
[name="鼠王"]   他们贩卖人情，四处兜售战争，最终走到了今天。
[name="鼠王"]   龙门有龙门的律宪，我有我的规矩。
[name="鼠王"]   企鹅物流也有他们自己那一套为所欲为的法则，只不过各不相同罢了。
[Character(name="avg_npc_034#3",name2="avg_npc_031",focus=2)]
[name="黑帮"]   ——
[name="黑帮"]   鼠王先生，如果当时首领......甘比诺先生不在第一次见面的时候拔剑的话，事情会演变到这一步吗？
[Character(name="avg_npc_034#3",name2="avg_npc_031",focus=1)]
[name="鼠王"]   我给过机会，在那之前之后，远不止那一次。
[name="鼠王"]   但有些时候，特别是谈生意的场合，第一印象是非常重要的，明白吗？
[Character(name="avg_npc_034",name2="avg_npc_031",focus=2)]
[name="黑帮"]   ......明白。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=2, block=true)]
[PlaySound(key="$rungeneral", volume=0.9)]
[Character(name="avg_npc_028#2")]
[name="甘比诺"]   ......呼，呼。
[name="甘比诺"]   出口......在那......！就快！
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="甘比诺"]   ——谁！？出来！
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_027",fadetime=1,block=true)]
[Delay(time=1)]
[name="卡彭"]   原来你没死，真是意外，看来鼠王办事也并非那么彻底。
[Character(name="avg_npc_028#2",name2="avg_npc_027",focus=1)]
[name="甘比诺"]   ......被你刺伤的伤口还隐隐作痛，卡彭，我非常高兴你会主动出现在我的面前。
[name="甘比诺"]   好让我亲手杀了你。
[Character(name="avg_npc_028#2",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   整个龙门都在追捕我们。我不想浪费时间在你身上。
[name="卡彭"]   所以，速战速决吧。
[Character(name="avg_npc_028#3",name2="avg_npc_027#2",focus=1)]
[name="甘比诺"]   你会为背叛家族付出代价——
[Dialog]
[Character]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_gen_walk_n")]
[name="？？？"]   哈哈，家族，家族呢。
[name="？？？"]   真是让人怀念的说法，嗯，你们见到德克萨斯了吗？
[Character(name="avg_npc_027#2")]
[name="卡彭"]   这、这个气味......！
[Character(name="avg_npc_028#3")]
[name="甘比诺"]   ......落单的狼。你为什么会在龙门？
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_140_whitew_1",fadetime=2,block=true)]
[Delay(time=2)]
[name="拉普兰德"]   因为德克萨斯在这里，这不是显而易见的吗？
[name="拉普兰德"]  话说，原来拖家带口地逃离叙拉古还能有资格自称家族？还有资格自称“西西里人”？
[name="拉普兰德"]  那么那位掠夺了你们引以为傲的荣光和历史的......西西里女士本人，同意了吗？
[Character(name="avg_npc_028#3")]
[name="甘比诺"]   ——住嘴！不要在我面前提起那个女人！
[name="甘比诺"]  你只是一个叛徒，你没资格对我们——
[Character(name="char_140_whitew_1")]
[name="拉普兰德"]   闭嘴，废物。
[name="拉普兰德"]   啊，原来你们受伤了？熟悉的血腥味，狼血，嗯，这就是所谓的家乡的味道？
[name="拉普兰德"]   德克萨斯变了吧？
[name="拉普兰德"]   她真的变得太多太多了，叙拉古的老朋友找上门来，而她居然让你们活着离开了龙门？
[name="拉普兰德"]   这也太不讲究待客之道了，没可能的吧？但是没关系，她没有做的事情，我会来帮她善后。
[name="拉普兰德"]   也许把叙拉古同僚的尸首摆在她的面前，能稍微刺激到她一点，是呢，真是个好主意......
[name="拉普兰德"]   你们觉得她逃得掉吗？从她家族的阴影里，从那段过去里？
[Character(name="avg_npc_028#2")]
[name="甘比诺"]   ......卡彭，给我站稳了。
[Character(name="avg_npc_027#2")]
[name="卡彭"]   呵，你竟然会和我并肩作战？你的荣耀和家族呢？
[Character(name="avg_npc_028#2")]
[name="甘比诺"]   念在你避开了要害的份上。
[Character(name="avg_npc_027#2")]
[name="卡彭"]   哼，你在害怕？
[Character(name="avg_npc_028#2")]
[name="甘比诺"]   我唯独不愿死在她的手上。
[Character(name="avg_npc_027#4")]
[name="卡彭"]   ......有点道理，就算要死，我也希望留下一具全尸。
[Character(name="char_140_whitew_1")]
[name="拉普兰德"]   哈哈哈哈，你们都在发抖哦？
[name="拉普兰德"]   站都站不稳了还想要和我战斗吗？
[name="拉普兰德"]   不错，真不错，亲眼目睹垂死挣扎也是不错的消遣。
[name="拉普兰德"]   现在，给你们十秒。
[name="拉普兰德"]   逃吧。
[Delay(time=1)]
[Dialog]
[Blocker(fadetime=2,block=true)]
[Image]
```

### level_act5d0_ex03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Dialog]
[Character]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6, crossfade=1.5)]
[Delay(time=1)]
[name="？？？"]   这次，是肚子上被开了个洞吧？被那个感觉很酷的老头？
[name="？？？"]   没错没错。我可是最前排观看的，看得一清二楚。
[name="？？？"]   你觉得是什么？会是替身吗？还是特效？
[name="？？？"]   不不不，不可能，完全不可能。你亲眼看看这段录像就知道了......
[name="？？？"]   唔。这也太逼真了吧！
[name="？？？"]   再说了，大帝的替身？这也太旷世罕见了吧？
[name="？？？"]   上一次呢？我记得是他在独自一人购物的时候，被突然窜出来的暴徒用弩枪贯穿了脑袋......
[name="？？？"]   那可做不到提前排练。
[name="？？？"]   还有汐斯塔的时候。音乐节上那次，私底下还有过无数人去找过他的麻烦。
[name="？？？"]   那时候我也在，为了能碰碰运气见到他，我特地订了和他们就隔了一条街的酒店，可热闹了。
[name="？？？"]   ......他不是个歌手吗？就算有钱了点，也不至于这么招人记恨吧？
[name="？？？"]   那是你不清楚他的行事风格。先说好，我真的很佩服他，但在树敌这方面，他大概也是全泰拉为数不多的天才。
[name="？？？"]   听说昨晚企鹅物流的仓库发生了事故。他从火焰里冲出来，根本不像受了伤的样子。
[name="？？？"]   很久以前有人目睹他在贫民窟被榴弹还是炸药一类的东西直接命中，第二天毫发无伤地出现在地下酒吧。
[name="？？？"]   这都不算什么了。
[name="？？？"]   啊。但是脑袋被榴弹砸了个包。
[name="？？？"]   ......明明是榴弹？
[name="？？？"]   说起来，哥伦比亚的音乐界最动荡的那会，有传言他被人枪杀在了街头，引起了巨大的轰动来着。
[name="？？？"]   不是被毒杀了吗？
[name="？？？"]   啊！那时候我在哥伦比亚旅游......我本来以为我这辈子都没法再见到偶像了。
[name="？？？"]   但是他活下来了？
[name="？？？"]   活下来了，还单枪匹马去找过场子。说是要为那些年轻人报仇。
[name="？？？"]   什么情况？不死身？
[name="？？？"]   应该有不少假新闻吧？媒体可不能全信哦。
[name="？？？"]   但命够硬是肯定的吧。
[name="？？？"]   不知道，也许把他捆在火山口，让天灾来对付他才有用吧。
[name="？？？"]   ......我怎么感觉就算这样他也活得下来？
[name="？？？"]   ......是啊，我甚至能想象到他对着喷发的火山爆粗口。
[name="？？？"]   还会很押韵。
[name="？？？"]   ......
[name="？？？"]   ......算啦。
[name="？？？"]   谁让他是大帝呢？
[Delay(time=0.6)]
[Dialog]
[Blocker(fadetime=1,block=true)]
[Image]
```

### level_act5d0_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[Character]
......
......以前的日子里，我一直以为我是个出色的信使。
信使，运送货物、信件。
也许是思念，也许是财富，也有时候，会带去毁灭。
父亲是个厉害的人物，从米诺斯到龙门，他建立了峯驰物流。
利益，谄媚，党同伐异。
这些东西很复杂，也很麻烦，但我勉强能应付。
但父亲告诉过我......
大地的彼端会更精彩一点。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[playsound(key="$drift")]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_325_bison_1#4")]
[name="拜松"]   ......唔！我这是......
[Character(name="avg_npc_031")]
[name="黑帮A"]   你在嘟囔什么！？
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.8, crossfade=1.5)]
[Character(name="char_325_bison_1#4",name2="avg_npc_031",focus=1)]
[name="拜松"]   ......
[Character(name="char_325_bison_1#4",name2="avg_npc_031",focus=2)]
[name="黑帮A"]   醒了的话，就安静点，否则有你好看。
[name="黑帮A"]   哼，等首领解决了企鹅物流，会来处理你的。
[Character(name="char_325_bison_1#4",name2="avg_npc_031",focus=1)]
[name="拜松"]   （我......被这些家伙......德克萨斯他们还在和黑手党交战吗？）
[name="拜松"]   （该死......为什么我一点用场都派不上......我可是峯驰物流的......）
[name="拜松"]   （......车停了。）
[Character(name="avg_npc_031",name2="avg_npc_031",focus=2)]
[name="黑帮A"]   是我们，首领把那个丰蹄小子抓住了......
[name="黑帮A"]   等等，你要做什么！？
[Character(name="avg_npc_031",name2="avg_npc_031",focus=1)]
[name="黑帮B"]   是卡彭先生的命令。
[Character(name="avg_npc_031",name2="avg_npc_031",focus=2)]
[name="黑帮A"]   卡彭？这可是首领的命令！他胆敢僭越——
[Dialog]
[delay(time=1)]
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_027#2",fadetime=1,block=true)]
[delay(time=1)]
[name="卡彭"]   我胆敢什么？
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)] 
[delay(time=0.7)] 
[Character(name="char_325_bison_1#4")]
[name="拜松"]   ——！
[Character(name="avg_npc_027#3")]
[name="卡彭"]   你好，峯驰物流的小少爷。
[name="卡彭"]   这是我们第一次正式见面，对吧？
[Character(name="char_325_bison_1#4",name2="avg_npc_027#3",focus=1)]
[name="拜松"]   ......你射杀了自己的同伴？
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=2)]
[name="卡彭"]   惩罚叛徒可没有违背龙门的规矩。
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=1)]
[name="拜松"]   我不是指这个......你想做什么？
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=2)]
[name="卡彭"]   做一笔交易。
[name="卡彭"]   显而易见，甘比诺的匹夫之勇会让家族溺毙在所谓的荣光里。
[name="卡彭"]   我并不想，相当一部分人并不想，做无意义的陪葬，谁会想呢？
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=1)]
[name="拜松"]   所以呢？
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=2)]
[name="卡彭"]   我会帮助你对付甘比诺。
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=1)]
[name="拜松"]   我不可能信任你。
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=2)]
[name="卡彭"]   ......我也能帮助你对付企鹅物流。
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=1)]
[name="拜松"]   ......
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=2)]
[name="卡彭"]   我不是傻子。在龙门待了很多年，我早就在做多种准备。
[name="卡彭"]   你的父亲大权在握，占据龙门七成以上的民事信使工作。
[name="卡彭"]   而且，和龙门高层有一些战略合作。
[name="卡彭"]   无论怎么看，企鹅物流都是你们事业上最大的障碍。
[name="卡彭"]   我们的目标只是接手企鹅物流的全部渠道。欠下这个人情，咱们之间的生意可以再议。
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=1)]
[name="拜松"]   父亲和大帝先生相交莫逆，很遗憾，你的猜测不过是自以为是。
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=2)]
[name="卡彭"]   峯驰物流这样的庞然大物，真的只是你父亲说了算吗？
[name="卡彭"]   你似乎有点小看我们，也许如今的家族已经在多次偶然的失败中损耗殆尽......
[name="卡彭"]   但很久以前，我们的祖辈可是曾在叙拉古那些漆黑的议事桌上，骄傲的自称“西西里人”。
[name="卡彭"]   权利不断轮换，血肉模糊，而我耳濡目染。
[name="卡彭"]   实话实说吧，你父亲身边的那些人对企鹅物流是怎么想的？对龙门是怎么想的？
[name="卡彭"]   你又是怎么想的？
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=1)]
[name="拜松"]   ......你口口声声在强调家族，刚才却亲手杀了自己的家人。
[name="拜松"]   你觉得我会接受你的提议吗？
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=2)]
[name="卡彭"]   他的死只是单纯的......利益交换。
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=1)]
[name="拜松"]   哼，天知道你们支付的会是钞票还是炸药。
[Character(name="char_325_bison_1#4",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   ——很遗憾，我本以为你会更加成熟一点。你却要为了一个与你无关的小小纰漏而丧命。
[Character(name="char_325_bison_1",name2="avg_npc_027#2",focus=1)]
[name="拜松"]   ——！
[Character(name="char_325_bison_1",name2="avg_npc_027",focus=2)]
[name="卡彭"]   你害怕了。就算身为峯驰物流的部门经理，你也只是个乳臭未干的臭小子。
[Character(name="char_325_bison_1#4",name2="avg_npc_027",focus=1)]
[name="拜松"]   ......不好意思，米诺斯的年轻人，向来都是以大胆出名的。
[Character(name="char_325_bison_1#4",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   看来你还是不打算改变主意。
[name="卡彭"]   如果你能活下去的话，你会见到更多这种事，可惜现在，你只有死路一条。
[Character(name="char_325_bison_1#4",name2="avg_npc_027#2",focus=1)]
[name="拜松"]   （啧——！这绳子怎么这么牢，来不及了！）
[Character(name="char_325_bison_1#4",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   哪怕你死了，峯驰物流按捺不住，说不定还会牵扯出龙门近卫局，局势会变得更加混乱，对我来说，也是好事。
[name="卡彭"]   交谈很短暂，说再见吧，小少爷。
[Dialog]
[Character]
[stopmusic(fadetime=1)]
[name="？？？"]   哎呀，可你对拜松出手的话，就不属于惩罚叛徒的范畴了喔。
[name="？？？"]   还是说你觉得在这里就结束，可以吗？
[Character(name="avg_npc_031")]
[name="黑帮"]   谁！？
[Character(name="char_213_mostma_1#3")]
[name="莫斯提马"]   路过的信使。
[Character(name="avg_npc_027",name2="char_213_mostma_1#3",focus=1)]
[name="卡彭"]   ......我对你有印象，长角的萨科塔，今晚你给我们添了不少麻烦。
[Character(name="avg_npc_027",name2="char_213_mostma_1#2",focus=2)]
[name="莫斯提马"]   非常荣幸。
[Character(name="avg_npc_027#2",name2="char_213_mostma_1#2",focus=1)]
[name="卡彭"]   我从没有在企鹅物流的任何情报中听说过你，你到底是什么人？
[Character(name="avg_npc_027#2",name2="char_213_mostma_1#2",focus=2)]
[name="莫斯提马"]   嗯......我有必要回答你吗？
[name="莫斯提马"]   我只是来找我丢失的包裹的，嗯，就像普通的信使那样。
[Character(name="avg_npc_031",name2="avg_npc_031")]
[name="黑帮"]   卡彭先生，我们已经控制了这个据点。这里都是支持您的人，她孤立无援。
[Character(name="avg_npc_027",name2="char_213_mostma_1#2",focus=1)]
[name="卡彭"]   ......
[Character(name="avg_npc_027",name2="char_213_mostma_1#2",focus=2)]
[name="莫斯提马"]   怎么？还是要动手吗？
[Character(name="char_213_m

... (全文21615字符)
```

### level_act5d0_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.8, crossfade=1.5)]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
0:00 A.M.    天气/沙尘
龙门市区，商业街
[Dialog]
[Delay(time=0.4)]
[Character(name="char_272_strong_1#4",name2="char_243_waaifu_1#3",focus=1)]
[name="孑"]   ——
[Character(name="char_272_strong_1#4",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   喂，你知道你现在的表情很吓人吗？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   ......你回来了，那些人你调查清楚了吗？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   稍微有一些眉目，虽然很想把那些胡作非为的家伙绳之以法，但似乎不是我一个人就能解决的事情。
[name="槐琥"]   说不定要拜托事务所的那些家伙。
[name="槐琥"]   对方势力不小，阿那个家伙，又不肯直接告诉我，故弄玄虚的......
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#3",focus=1)]
[name="孑"]   哪个家伙？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   阿。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#3",focus=1)]
[name="孑"]   啊？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   ......他就叫阿。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#3",focus=1)]
[name="孑"]   哦......那，总而言之，不是什么轻松的事情对吧。
[name="孑"]   我来帮忙。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   ......你没听明白吗？如果只是那些混混倒还好说，可如果是一个有组织有规模的帮派组织，我们当然不能轻举妄动。
[Character(name="char_272_strong_1#4",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   “不能轻举妄动”，也不是毫无办法，对吧。
[Character(name="char_272_strong_1#4",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   你竟然会和我抠字眼？
[Character(name="char_272_strong_1#4",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   我没在开玩笑。
[Character(name="char_272_strong_1#4",name2="char_243_waaifu_1#4",focus=2)]
[name="槐琥"]   ......阿伯他没事吧？
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#4",focus=1)]
[name="孑"]   伤不重，但这已经不重要了。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   ——没错，的确不重要了。如果只是黑吃黑的案子，我才不想多管闲事。
[name="槐琥"]   但在我的眼前伤及无辜，我可不能由着他们胡作非为。
[Character(name="char_272_strong_1#3",name2="char_243_waaifu_1#3",focus=1)]
[name="孑"]   ......谢谢，之后请你吃鱼丸。
[Character(name="char_272_strong_1#3",name2="char_243_waaifu_1",focus=2)]
[name="槐琥"]   鱼丸就不必了......
[name="槐琥"]   对了。
[name="槐琥"]   今晚的事件，也和企鹅物流有关系。他们根本没打算掩饰，一点都没。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1",focus=1)]
[name="孑"]   他们不是坏人，大概也是被卷进去的吧。
[Character(name="char_272_strong_1",name2="char_243_waaifu_1#3",focus=2)]
[name="槐琥"]   今年到现在已经被卷进去几十次了？他们应该更注意一点，不要总是惹是生非。
[name="槐琥"]   如果有机会见到他们，有必要警告他们一下。
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_027#2")]
[name="卡彭"]   沙子，源石技艺，法术，哼。
[name="卡彭"]   想来也是，掌控龙门暗面的怪物，总不能真的是个花架子。
[Character(name="avg_npc_031",name2="avg_npc_027#2",focus=1)]
[name="黑帮"]   难道卡彭先生的意思是？
[Character(name="avg_npc_031",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   当然是最不该招惹的人，不然呢？
[Character(name="avg_npc_031",name2="avg_npc_027#2",focus=1)]
[name="黑帮"]   鼠王？但是，我们岂不是要同时对付首领、企鹅物流，还有......
[Character(name="avg_npc_031",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   还有半座龙门。没错，情况不容乐观，所以，一步都不能走错。
[Character(name="avg_npc_031",name2="avg_npc_027#2",focus=1)]
[name="黑帮"]   卡、卡彭先生，您这是做什么？请把弩放下！
[Character(name="avg_npc_031",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   你以为背叛家族真的是一件小事吗？
[name="卡彭"]   愿意追随我在龙门扎根，做好了不惜背叛甘比诺也要活下去的准备，我记得他们每一个人的脸。
[name="卡彭"]   而你并不在其列，甘比诺的走狗，去死吧。
[Character(name="avg_npc_027#4")]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_gen_walk_n")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)] 
[CameraShake(duration=0.3, xstrength=8, ystrength=6, vibrato=20, randomness=20, fadeout=true, block=false)]
[name="卡彭"]   滚出来。
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_028",name2="avg_npc_027#4",focus=1)]
[name="甘比诺"]   我本以为你只是个忘恩负义的混账，看来你收买人心还是很有一套的。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=2)]
[name="卡彭"]   说起来，这还是你教我的。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=1)]
[name="甘比诺"]   我怎么不记得？
[Character(name="avg_npc_028",name2="avg_npc_027",focus=2)]
[name="卡彭"]   你曾经赢得过我的效忠，再让我失望至极，我可不会重蹈覆辙。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=1)]
[name="甘比诺"]   背叛意味着什么，你应该明白。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=2)]
[name="卡彭"]   背叛是叙拉古最肮脏的罪名，但可惜，你所拥戴的荣誉在龙门毫无价值。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=1)]
[name="甘比诺"]   收下这个吧。
[Character(name="avg_npc_028",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   ——黑桃J？
[Character(name="avg_npc_028#4",name2="avg_npc_027#2",focus=1)]
[name="甘比诺"]   我说过，你藏牌的速度太慢了！
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=0.7)]
[Character(name="avg_npc_028",name2="avg_npc_027",focus=2)]
[name="卡彭"]   你的剑更迟钝了，甘比诺，和企鹅物流的厮杀让你负伤了吗？还是说，旧伤复发？
[Character(name="avg_npc_028",name2="avg_npc_027",focus=1)]
[name="甘比诺"]   你的懦弱让我感到心寒，我只是在考虑怎样的血腥下场才适合叛徒。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=2)]
[name="卡彭"]   现在，你才是多余的那张牌。
[Dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.1, block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.1, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, blo

... (全文15012字符)
```

### level_act5d0_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[Dialog]
[Delay(time=1)]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Delay(time=0.4)] 
[Blocker(a=0, fadetime=1, block=true)]
3:21 A.M.    天气/晴
龙门市区，“大地的尽头”酒吧，废墟中
[dialog]
[Delay(time=0.4)] 
[Character(name="char_101_sora_1#5",name2="char_102_texas_1#2")]
[name="企鹅物流众人"]   干杯！！
[Character(name="char_103_angel_1#8",name2="char_201_moeshd")]
[name="企鹅物流众人"]   干杯！！
[PlayMusic(intro="$marketplace_intro", key="$marketplace_loop", volume=0.8, crossfade=4)]
[Dialog]
[Character]
[delay(time=1)]
[Character(name="char_103_angel_1#8")]
[name="能天使"]   哎呀，今晚可真是打了个痛快。
[Character(name="char_201_moeshd")]
[name="可颂"]   虽然是坐在这一片狼藉里开趴，但一想到所有损失都有人报销，我就感觉浑身舒畅！
[Character(name="char_101_sora_1#3",name2="char_102_texas_1",focus=1)]
[name="空"]   德克萨斯，你要是早就知道，好歹也告诉我们一声呀。
[Character(name="char_101_sora_1#3",name2="char_102_texas_1",focus=2)]
[name="德克萨斯"]   我猜的。
[Character(name="char_101_sora_1#5",name2="char_102_texas_1",focus=1)]
[name="空"]   你一点都不会撒谎，真是......
[Character(name="char_101_sora_1#5",name2="char_103_angel_1#8",focus=2)]
[name="能天使"]   反正都是老板的主意吧？别介意~吃饭喝酒打架，有益身心健康。
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="char_325_bison_1#4")]
[name="拜松"]   ......
[Character(name="char_325_bison_1#4",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   怎么了？不加入他们吗？
[Character(name="char_325_bison_1",name2="char_213_mostma_1#3",focus=1)]
[name="拜松"]   不，免了。
[name="拜松"]   怎么说呢，我稍微有点，不太能接受。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   习惯就好啦。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   我觉得习惯了就完了。
[name="拜松"]   那今晚这么多事都是为了什么？还有大帝，他......
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   只是用生命让派对变得更加热闹而已。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   ......莫斯提马小姐，你说过，你会决定我在企鹅物流的学习成绩，是吗？
[Character(name="char_325_bison_1",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   嗯，我考虑过了。虽然你大概和他们八字不合，但你的改变和成长有目共睹，也许——
[Character(name="char_325_bison_1#4",name2="char_213_mostma_1#3",focus=1)]
[name="拜松"]   不。
[name="拜松"]   我不会留在这里的。
[Character(name="char_325_bison_1#4",name2="char_213_mostma_1#2",focus=2)]
[name="莫斯提马"]   ——哎呀，我还以为以你现在的情况，你会更需要企鹅物流作为一个不被干扰的踏板呢。
[Character(name="char_325_bison_1",name2="char_213_mostma_1#2",focus=1)]
[name="拜松"]   本来是这么打算的，话说原来莫斯提马小姐早就看穿了啊......
[name="拜松"]   我不是觉得企鹅物流很糟糕，不，也许真的很糟糕。
[name="拜松"]   但是，我在想，原来还有这样的信使，还有这样的生活方式。
[name="拜松"]   虽然常识在告诉我，这很危险。
[name="拜松"]   但也许这样......反而更接近我的理想。
[name="拜松"]   不如说，如果我自己不这么认为的话，我会开始质疑现实的。
[name="拜松"]   ......就像一个梦，荒诞的梦。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=2)]
[name="莫斯提马"]   嗯，械斗、爆炸和高空坠落总是能叩开心扉的。
[Character(name="char_325_bison_1",name2="char_213_mostma_1",focus=1)]
[name="拜松"]   呃，这种企鹅物流式的洗礼真的不利于身心健康。
[Character(name="char_325_bison_1",name2="char_213_mostma_1#3",focus=2)]
[name="莫斯提马"]   但既然你已经下定了决心，作为一名信使同僚，我会祝福你的。
[Character(name="char_325_bison_1",name2="char_213_mostma_1#3",focus=1)]
[name="拜松"]   ——谢谢。
[Character(name="char_325_bison_1",name2="char_213_mostma_1#4",focus=2)]
[name="莫斯提马"]   而且这样你的父亲就找不到借口克扣我的薪水了吧。
[Character(name="char_325_bison_1#2",name2="char_213_mostma_1#4",focus=1)]
[name="拜松"]   老、老爹吗！我都忘了这件事了，也许我该和他好好聊聊，他到底在折腾些什么......
[Character(name="char_103_angel_1#8")]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="能天使"]   莫斯提马！干杯！
[Character(name="char_213_mostma_1#3",name2="char_103_angel_1#8",focus=1)]
[name="莫斯提马"]   干杯。
[name="莫斯提马"]   干嘛要突然冲过来，都洒到身上了不是吗。
[Character(name="char_213_mostma_1#3",name2="char_103_angel_1#7",focus=2)]
[name="能天使"]   一不留神你就会跑掉嘛，我可是有很——多事情想要问你呢。
[Character(name="char_213_mostma_1",name2="char_103_angel_1#7",focus=1)]
[name="莫斯提马"]   很多事，很多事呢......比如拉特兰的那件事？
[name="莫斯提马"]   你姐姐的事？或者是......我的角？
[Character(name="char_213_mostma_1",name2="char_103_angel_1#3",focus=2)]
[name="能天使"]   ——
[Character(name="char_213_mostma_1",name2="char_103_angel_1#3",focus=1)]
[name="莫斯提马"]   哈哈哈，笑容僵住了喔？你还是老样子，想什么都会放在脸上呢。
[Character(name="char_213_mostma_1",name2="char_103_angel_1#7",focus=2)]
[name="能天使"]   莫！斯！提！马！
[Character(name="char_213_mostma_1",name2="char_103_angel_1#7",focus=1)]
[name="莫斯提马"]   好了好了，我会告诉你的。
[name="莫斯提马"]   ......但不是现在，你私底下调查了很长时间了吧，你应该能理解。
[Character(name="char_213_mostma_1",name2="char_103_angel_1#3",focus=2)]
[name="能天使"]   嗯，虽然不知道为什么，那已经算得上国家机密了，但也没所谓吧？
[name="能天使"]   和你们有关的事情，我总得弄清楚啊。
[Character(name="char_213_mostma_1#2",name2="char_103_angel_1#3",focus=1)]
[name="莫斯提马"]   你还真的这么做了吗......
[name="莫斯提马"]   说不定会被超级麻烦又阴险，而且无处不在的坏孩子盯上，没收你的守护铳，然后尾随你直到天涯海角喔？
[Character(name="char_213_mostma_1#2",name2="char_103_angel_1#8",focus=2)]
[name="能天使"]   呃，为什么这么具体？
[name="能天使"]   但是没关系，我跑的够快嘛，他们从来追不上我！
[Character(name="char_213_mostma_1",name2="char_103_angel_1#8",focus=1)]
[name="莫斯提马"]   好吧。
[Character(name="char_213_mostma_1",name2="char_103_angel_1#3",focus=2)]
[name="能天使"]   放弃了？
[Character(name="char_213_mostma_1",name2="char_103_angel_1#3",focus=1)]
[name="莫斯提马"]   投降了，反正从来没有人能管得住你。
[Character(name="char_213_mostma_1",name2="char_103_angel_1#7",focus=2)]
[name="能天使"]   其实还是有的啊，比如老板和老板什么的。德克萨斯说的话我也会听啦，听一半。
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="char_102_texas_1#2")]
[name="德克萨斯"]   ......
[Character(name="char_102_texas_1#2",name2="char_201_moeshd",focus=2)]
[name="可颂"]   你也在意她们的悄悄话吗？
[name="可颂"]   虽然我听说过个大概啦，但说真的，我现在超好奇的。
[name="可颂"]   拉特兰到底是个什么样的地方？
[Character(name="char_102_texas_1",name2="char_201_moeshd",focus=1)]
[name="德克萨斯"]   ......没必要深究，那是她的自由。
[Character(name="char_101_sora_1#3",name2="char_102_texas_1",focus=1)]
[name="空"]   可是拜松好像状态不太对？
[Character(name="char_101_sora_1#3",name2="char_102_texas_1",focus=2)]
[n

... (全文26255字符)
```

### tutorial_act5d0_02

```
[HEADER(is_skippable=true, is_autoable=false)] 活动02关卡内剧情
[PopupDialog(dialogHead="$avatar_angel")] 这位发了疯的黑手党到底为什么要攻击龙门的<@tu.kw>指挥终端</>？拆了能换钱吗？
[PopupDialog(dialogHead="$avatar_emperor")] 顺便一提，就算是被敌人破坏的公共财产，最后还是要我赔偿，用你们的薪水。
[PopupDialog(dialogHead="$avatar_moeshd")] 欸！？刚才不是还说全部报销的吗！？
[PopupDialog(dialogHead="$avatar_emperor")] 可以阻止的财产损失当然不在报销范围之内，这是常识。
[PopupDialog(dialogHead="$avatar_emperor")] <@tu.kw>守住</>那些终端设备，守不住的话，就优先把敌人全都打趴下！
[PopupDialog(dialogHead="$avatar_emperor")] 否则，就等着陪近卫局喝茶吧。
[Blocker(fadetime=0.3, block=true, a=0)]
```

### tutorial_act5d0_10

```
[HEADER(is_skippable=true,is_autoable=false)] 活动10关卡内剧情
[PopupDialog(dialogHead="$avatar_mousek")] 既然是游戏，那么就需要一些小小的规则，比如...
[PopupDialog(dialogHead="$avatar_mousek")] 接下来，我将分别为场上<@tu.kw>生命上限最高</>和<@tu.kw>生命上限最低 </>的两位准备一些小小的惊喜
[PopupDialog(dialogHead="$avatar_mousek")] 撑住了，年轻人，一瞬间都不要松懈。
[PopupDialog(dialogHead="$avatar_mousek")] 不要让我太过失望。
[Blocker(fadetime=0.3, block=true, a=0)] 
```

### ui_act5d0_firstenter

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=0.5)]
[Background]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Delay(time=0.4)] 
[Blocker(a=0, fadetime=1, block=true)]
11:37 P.M.    天气/多云
龙门日落大道，某酒吧，靠后门边最后一张没擦干净的桌子
[Dialog]
[Delay(time=0.4)] 
[Character(name="avg_npc_027#3",fadetime=1,block=true)]
[Delay(time=1)]
[name="卡彭"]   黑桃J，同花顺，又是我赢了，甘比诺。
[Dialog]
[Character]
[Character(name="avg_npc_028#4",fadetime=1,block=true)]
[Delay(time=1)]
[name="甘比诺"]   是你赢了，但你藏牌的速度比我用脚趾还慢。
[PlayMusic(intro="$bar_intro", key="$bar_loop", volume=0.8,crossfade=1)]
[Character(name="avg_npc_028#4",name2="avg_npc_027",focus=2)]
[name="卡彭"]   你又想赖账了吗？
[Character(name="avg_npc_028",name2="avg_npc_027",focus=1)]
[name="甘比诺"]   给我闭嘴。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=2)]
[name="卡彭"]   闭嘴？你昨晚怎么不知道闭嘴？那样能省不少事，真的。
[Character(name="avg_npc_028#3",name2="avg_npc_027",focus=1)]
[CameraShake(duration=0.4, xstrength=0, ystrength=8, vibrato=30, randomness=30, fadeout=true, block=true)]
[name="甘比诺"]   你在龙门待的有点久了，卡彭。也许你该回忆一下怎么和我说话，我才是首领。
[Character(name="avg_npc_028#3",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   坐下，你这蠢货，叙拉古的生意越来越差就是因为你的好脾气。
[Character(name="avg_npc_028#3",name2="avg_npc_027#2",focus=1)]
[name="甘比诺"]   你在龙门待了七八年，除了学到几句龙门粗口，你又干了什么？眼睁睁看着我们的渠道越来越少？
[Character(name="avg_npc_028#3",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   至少昨天赢得了那位支持的人是我，而你，差点搅黄了我这么长久的努力。
[name="卡彭"]   还有，在龙门我们平起平坐，“首领”。
[Character(name="avg_npc_028",name2="avg_npc_027#2",focus=1)]
[name="甘比诺"]   鼠王在龙门搞的这一套，不都是叙拉古玩烂了的把戏？
[Character(name="avg_npc_028",name2="avg_npc_027",focus=2)]
[name="卡彭"]   但是你把叙拉古的一手好牌打得稀烂。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=1)]
[name="甘比诺"]   而你就是我手里最烂的一张牌。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=2)]
[name="卡彭"]   我们会在龙门占据一席之地的。好好想想，一座疲惫不堪、暗流涌动的城市，这里会成为家族的下一个故土。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=1)]
[name="甘比诺"]   只有叙拉古的土地会尊重我们，卡彭，别忘了被赶出那张桌子，夹着尾巴离开叙拉古的耻辱。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=2)]
[name="卡彭"]   信条喂不饱任何人。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=1)]
[name="甘比诺"]   哼。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=2)]
[name="卡彭"]   魏彦吾在这座城市定下了规则，只要不过界，我们依旧可以在这里大展拳脚，龙门需要一些“人情产业”。
[Character(name="avg_npc_028",name2="avg_npc_027",focus=1)]
[name="甘比诺"]   ......有几年没见，你越来越让我感到厌倦了。
[Character(name="avg_npc_028",name2="avg_npc_027#2",focus=2)]
[name="卡彭"]   彼此彼此，首领。
[Character(name="avg_npc_028#3",name2="avg_npc_027#2",focus=1)]
[name="甘比诺"]   你——！
[Character]
[Dialog]
[stopmusic(fadetime=2)]
[name="？？？"]   别在这里叭叭叭叭地吵架，这杯劣质气泡酒已经够让我烦躁的了，拿着玻璃瓶，去外面打一架如何？
[Character(name="avg_npc_028#3")]
[name="甘比诺"]   滚开，这不关你事。
[Character]
[name="？？？"]   注意你的口气，我才是这里的老板。
[name="？？？"]   顺便提供殡葬一条龙包办，如果你俩有幸同归于尽，丧葬费打八折。
[Character(name="avg_npc_028#3",name2="avg_npc_027",focus=2)]
[name="卡彭"]   喂......这家伙是......
[Character(name="avg_npc_028#3")]
[name="甘比诺"]   ......从叙拉古离开之后，这就是我们的境遇。没人还记得你是一个西西里人。
[Character]
[name="？？？"]   谁管你是谁。
[Character(name="avg_npc_028#3",name2="avg_npc_027",focus=1)]
[name="甘比诺"]   嘁！卡彭，炸掉这间品味令人作呕的酒吧，算不算美化市容？魏彦吾不会生气的吧。
[Character(name="avg_npc_028#3",name2="avg_npc_027#4",focus=2)]
[name="卡彭"]   闭嘴！别挑衅他！
[Character]
[name="？？？"]   啊？
[PlaySound(key="$bottlebroken")]
[CameraShake(duration=0.4, xstrength=0, ystrength=8, vibrato=30, randomness=30, fadeout=true, block=true)]
[Dialog]
[PlayMusic(intro="$emperor_intro", key="$emperor_loop", volume=0.6, crossfade=1.5)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_105_emper",fadetime=2,block=true)]
[Delay(time=2)]
[name="大帝"]   你说谁的品味令人作呕？
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_black",xScale=1.3, yScale=1.3)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.4)] 
[PlaySound(key="$pistol", volume=0.9)]
[Delay(time=0.2)]
[PlaySound(key="$bottlebroken")]
[CameraShake(duration=0.4, xstrength=8, ystrength=8, vibrato=30, randomness=30, fadeout=true, block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[Image(image="ac5_title1",  xScale=0.7, yScale=0.7,fadetime=3,block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[PlaySound(key="$bottlebroken")]
[CameraShake(duration=0.4, xstrength=8, ystrength=8, vibrato=30, randomness=30, fadeout=true, block=true)]
[Image(fadetime=2,block=true)]
[Delay(time=2)]
[stopmusic(fadetime=2)]
[Dialog]
```


## 统计

- 总字符数：316291
- 对话行数：2879


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
