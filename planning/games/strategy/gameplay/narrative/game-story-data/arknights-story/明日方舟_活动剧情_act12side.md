# 明日方舟 · 活动剧情 · act12side（31段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act12side」完整剧情脚本（31个文件，2486行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act12side
- 脚本文件数：31

### guide_act12side_charm

```
[HEADER(is_skippable=false, is_tutorial=true)] 标志物使用引导
[PopupDialog(dialogHead="$avatar_takila")] 在多索雷斯，可以通过改造装备或者添加配件来更好地在这里行动。
[Tutorial(target="btn_change_charm", searchBtnInChildren=true, waitForSignal="act12side_charm_repo_routed",            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_takila")] 这里以我的武器为例吧。
[Tutorial(target="pool_act12side_first_charm_in_list", searchBtnInChildren=true,waitForSignal="act12side_charm_selected",            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_takila", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 比如说，这里有一个最常见的配件，我先给我的装备装上。
[PopupDialog(dialogHead="$avatar_takila", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 之所以做成<@tu.kw>标志物</>形式是为了方便辨识，一种标志对应一种装配，收集标志物可以进行对应的装配，是这两年才兴起的一种风潮。
[PopupDialog(dialogHead="$avatar_takila", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 各种改装或者配件有什么具体功效可以询问我，也可以在手机上查询，有专门的网站收录这些。
[Tutorial(focusX=211, focusY=-200, focusWidth=423, focusHeight=134, anchor="TopLeft",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_takila", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 比如说，这个配件的效果，是这样。
[Tutorial(focusX=211, focusY=-200, focusWidth=423, focusHeight=134, anchor="TopLeft",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_takila", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 对了，一般来说，一件装备推荐的改造上限是<@tu.kw>5</>个，也就是最多携带<@tu.kw>5</>个标志物，并且同一分类下的标志物<@tu.kw>不能同时携带</>进入战斗。
[Tutorial(target="btn_save", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_takila")] 当携带的标志物变多后，注意不要遗忘自己的定制方案，这些是会切实影响你的战斗的。
```

### level_act12side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_20_G02")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[character(name="char_010_chen_summer",fadetime=1.5)]
[delay(time=2)]
[name="陈"]（人感觉和汐斯塔一样多，不过氛围上完全不一样。）
[name="陈"]（到处都是酒吧、赌场、餐厅......）
[dialog]
[character(name="char_010_chen_summer",focus=-1)]
[name="轻浮的游客"]美女，要不要和我们一起去沙滩边玩啊？
[character(name="char_010_chen_summer")]
[name="陈"]滚。
[dialog]
[delay(time=1)]
[name="陈"]（林雨霞一大早人就不见了。）
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[musicvolume(volume=0, fadetime=1)]
[Delay(time=2)]
[Background(image="bg_indoor_n",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Character(name="char_308_swire_1#5",name2="char_010_chen_1#1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_308_swire_1#5",name2="char_010_chen_1#1",focus=1)]
[name="诗怀雅"]  ......我准备再给那只下水道老鼠打个电话。
[name="诗怀雅"]  虽然我没怎么来过这里，但我觉得特殊部队一定在做可怕的事。
[Character(name="char_308_swire_1#5",name2="char_010_chen_1#1",focus=2)]
[name="陈"]  你见过贫民区的林吗？
[Character(name="char_308_swire_1#5",name2="char_010_chen_1#1",focus=1)]
[name="诗怀雅"]  我见过。是个很和善的老人，比我爷爷好多了。
[Character(name="char_308_swire_1#5",name2="char_010_chen_1#1",focus=2)]
[name="陈"]  ......他可是“鼠王”。
[Character(name="char_308_swire_1#3",name2="char_010_chen_1#1",focus=1)]
[name="诗怀雅"]  这几个人不都这样。但他真的是个好人。
[name="诗怀雅"]  我只是没想到雨霞她会变成现在这个样子。明明以前是个又胆小又腼腆的孩子，经常躲在你背后来着。
[Character(name="char_308_swire_1#3",name2="char_010_chen_1#1",focus=2)]
[name="陈"]  我倒觉得她没有变。她只是......担负起了责任。也许并不该属于她的责任。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="bg_20_G02",screenadapt="coverall")]
[Character(name="char_010_chen_summer")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.4, fadetime=1)]
[Delay(time=1)]
[name="陈"]（算了，反正她跑不了。）
[name="陈"]唉，来都来了，找点事做吧。
[name="陈"]（做点什么呢......买土特产？）
[name="陈"]（星熊和诗怀雅她们......买回去还要寄，有点麻烦，等她们什么时候过来外勤给她们好了。）
[name="陈"]（对了，也要给文月夫人准备一份谢礼。）
[name="陈"]（罗德岛的话......白雪，风笛，阿米娅，还有......她？）
[name="陈"]（算了。总之，人有点多，不知道能不能带得过来，看情况再说吧。）
[name="陈"]（不过感觉也要不了多少时间......）
[name="陈"]（到处走走？......反正干什么都要到处走的。）
[name="陈"]（让那个埃内斯托带我参观一下城市的景点？）
[name="陈"]（......算了，不熟。）
[name="陈"]（对了，坎黛拉市长说的那件事......）
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character]
[musicvolume(volume=0.2, fadetime=1)]
[Background(image="bg_20_G01",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Character(name="avg_npc_198_1#5")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[name="坎黛拉"]最近这段日子里，城里的武器流通变得有些异常频繁，如果你们玩乐之余觉得有些不够刺激，那么，你们不妨试试调查着玩。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="bg_20_G02",screenadapt="coverall")]
[Character(name="char_010_chen_summer")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[musicvolume(volume=0.4, fadetime=1)]
[Delay(time=1)]
[name="陈"]（这个人明明是市长，却一点也不关心自己的城市，魏彦吾怎么会结交这样的人？）
[name="陈"]（而且这座城市，完全是纸醉金迷、骄奢淫逸的代名词......）
[name="陈"]（......诗怀雅说不定会喜欢这种地方，我宁愿回汐斯塔。）
[name="陈"]（唉，算了，来都来了，查案总比没事干强，还是查查看吧。）
[name="陈"]（虽然坎黛拉市长说查案的事也可以问埃内斯托，不过如果他们有明确的线索的话肯定早就行动了。）
[name="陈"]（直接去问大概是问不出什么的，还是先到处走走，从了解城市开始吧。）
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[character]
[character(name="avg_npc_201",name2="avg_npc_201")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[character(name="avg_npc_201",name2="avg_npc_201",focus=1)]
[name="懊恼的男游客"]昨晚战况怎么样？
[character(name="avg_npc_201",name2="avg_npc_201",focus=2)]
[name="高兴的男游客"]赢了几千，你呢？
[character(name="avg_npc_201",name2="avg_npc_201",focus=1)]
[name="懊恼的男游客"]啧，我输惨了。
[character(name="avg_npc_201",name2="avg_npc_201",focus=2)]
[name="高兴的男游客"]哈哈，没事，今天赢回来不就完了？
[character(name="avg_npc_201",name2="avg_npc_201",focus=1)]
[name="懊恼的男游客"]不用你说我也这么打算，*玻利瓦尔感叹词*，还是这里爽，我根本不想回去了。
[character(name="avg_npc_201",name2="avg_npc_201",focus=2)]
[name="高兴的男游客"]谁不是呢，一回到外面就又要看打打杀杀的。
[name="高兴的男游客"]可惜啊，咱们没钱在这买套房子。
[character(name="avg_npc_201",name2="avg_npc_201",focus=1)]
[name="懊恼的男游客"]赌赢不就有了？
[character(name="avg_npc_201",name2="avg_npc_201",focus=2)]
[name="高兴的男游客"]哈哈哈，有道理！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[character(name="char_010_chen_summer",fadetime=1.5)]
[delay(time=2)]
[Character(name="char_010_chen_summer",focus=-1)]
[name="热情的酒吧招待"]这位美丽的小姐，有兴趣来我们酒吧工作吗？
[name="热情的酒吧招待"]像你这么漂亮的人，一晚上就能赚大钱。
[character(name="char_010_chen_summer")]
[name="陈"]滚。
[dialog]
[delay(time=1)]
[name="陈"]赌场、酒吧、餐厅、卡拉OK，这座城市里除了这些就没有别的了吗。
[character(name="char_010_chen_summer",focus=-1)]
[name="？？？"]......距离海选结束，还有两天。
[dialog]
陈转过头去，发现声音是从路边商店橱窗中摆放的电视机中传来。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image(image="20_I00",xScale=1,yScale=1, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="电视台主持人"]各位市民们，游客们，有在好好享受你们的假期吗？
[name="电视台主持人"]我昨天在赌场输了三十万，今天可是打算去赢回来的。
[name="电视台主持人"]那么，在经过为期十天的角逐后，多索雷斯极限大奖赛的海选将在今天结束！
[name="电视台主持人"]而午后三点，也就是三个小时之后，我们将迎来海选中最后一场的大乱斗海选赛！
[name="电视台主持人"]是热爱大奖赛的你绝对不能错过的一场比赛！千万不要忘记前往比赛现场享受刺激的氛围！
[name="电视台主持人"]当然，不想忍受炎炎夏日和拥挤的人群也不用着急，锁定我们的官方电视台，我们会准点为你直播赛事内容！
[name="电视台主持人"]对了，这里还有一条说不定会让音乐爱好者们非常兴奋的消息。
[name="电视台主持人"]是的，可能你们已经听到了消息，坎黛拉市长居然请来了塞壬唱片旗下的知名音乐人，D.D.D.。
[name="电视台主持人"]而且，这位蒙面示人的音乐人，不仅将为我们带来她那奔放的电子乐，还将担任本次大奖赛的特邀主持！
[dialog]
[Blocker(a=0

... (全文21152字符)
```

### level_act12side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_20_G02")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#7",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]我说，Missy，我们已经到这座城市好几天了，我看你一点也没有去找林小姐的意思啊。
[name="星熊"]你一开始不是说你要偷偷跑到她跟前吓她一跳的吗？
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#1",focus=2)]
[name="诗怀雅"]吃不吃冰淇淋？
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#1",focus=1)]
[name="星熊"]我要三个球的，薄荷、草莓、巧克力。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]胖不死你。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#1",focus=2)]
[name="诗怀雅"]老板，一个三球，香草、草莓、巧克力。一个四球，前面的再加个柠檬。
[character]
[name="老板"]好嘞。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#1",focus=1)]
[name="星熊"]你好意思说我。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]林雨霞走的是官方程序，我们可不一样。你可是沾了我的光享受了一回VIP待遇。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#1",focus=2)]
[name="诗怀雅"]要我说呢，那个家伙现在应该还在路上呢，哈哈哈！
[name="诗怀雅"]假期长得很，我们慢慢等。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]死老鼠，居然背着我来这种好地方度假，等我找到你你死定了。
[character(name="avg_npc_203_1#5",name2="avg_npc_197_1#5",focus=1)]
[name="星熊"]唉，Missy，你可别忘了你是以什么为代价才拿到这次假的。
[character(name="avg_npc_203_1#5",name2="avg_npc_197_1#7",focus=2)]
[name="诗怀雅"]不就是所有年假外加回去后一个月的单休吗，小意思小意思。
[character(name="avg_npc_203_1#5",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]虽然为了防止你乱来我也把我的假期赔上了就是了。
[character(name="avg_npc_203_1#5",name2="avg_npc_197_1#1",focus=2)]
[name="诗怀雅"]哎呀，回去赔你就是了。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]行行。
[character(name="avg_npc_203_1#5",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]嗯？
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="星熊"]啊？
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#7",focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="星熊"]哈？！
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#7",focus=2)]
[name="诗怀雅"]干嘛，你看到她了？
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]我不仅看到林雨霞了，我还看到了一个更不可思议的人。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#7",focus=2)]
[name="诗怀雅"]谁啊......
[dialog]
[delay(time=0.51)]
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#4",focus=2)]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="诗怀雅"]哈？
[character]
[name="老板"]两位，你们的冰淇淋，球要掉了！两位！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[character(name="avg_npc_196_1#1",name2="char_010_chen_summer")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playsound(key="$livecrowd")]
[delay(time=2)]
[character(name="avg_npc_196_1#1",name2="char_010_chen_summer",focus=2)]
[name="陈"]哈......为什么会变成这样。
[dialog]
[character]
[delay(time=1)]
[playsound(key="$rungeneral")]
[character(name="avg_486_espumo_1#3",fadetime=1)]
[delay(time=1.5)]
[name="埃内斯托"]嘶......哈......总算找到你们了。
[name="埃内斯托"]两位，你们不是在追人吗，怎么跑到海选会场去了。
[name="埃内斯托"]要不是在路边的电视上看到你们，我差点没找到你们。
[character(name="avg_npc_196_1#5")]
[name="林雨霞"]误入。
[character(name="avg_486_espumo_1#6")]
[name="埃内斯托"]那怎么办，两位要干脆一起组成队伍参加大奖赛吗？
[character(name="avg_npc_196_1#1",name2="char_010_chen_summer",focus=1)]
[name="林雨霞"]我打算参加，但不是和她。
[character(name="avg_npc_196_1#1",name2="char_010_chen_summer",focus=2)]
[name="陈"]真巧，我也这么想。
[character(name="avg_npc_196_1#5",name2="char_010_chen_summer",focus=1)]
[name="林雨霞"]陈晖洁，你可以换一场海选参加。
[character(name="avg_npc_196_1#5",name2="char_010_chen_summer",focus=2)]
[name="陈"]不可能。这场海选已经是最后一场了。
[character(name="avg_npc_196_1#5",name2="char_010_chen_summer",focus=1)]
[name="林雨霞"]看来，我们之间要先分个高下。
[dialog]
[character]
[delay(time=0.7)]
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]两位，现在恐怕有半座城市的人正在通过屏幕看着这里。
[name="埃内斯托"]要不两位还是一起参赛吧，互相也好有个照应。
[character(name="avg_npc_196_1#1",name2="char_010_chen_summer",focus=1)]
[name="林雨霞"]......
[character(name="avg_npc_196_1#1",name2="char_010_chen_summer",focus=2)]
[name="陈"]......算了。
[character(name="avg_486_espumo_1#5")]
[name="埃内斯托"]那么，我也来帮忙吧。
[character(name="avg_486_espumo_1#2")]
[name="埃内斯托"]毕竟我是两位的向导，要是知道两位参赛我却没有，市长肯定要处罚我的。
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]虽然战斗力肯定不如两位，不过我毕竟是本地人，肯定能帮上两位的忙的。
[character(name="char_010_chen_summer")]
[name="陈"]他们允许再带一个人吗？
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]可以的，队伍上限七人，只要能在正式比赛前完成登记，在胜出后再去找队友都是可以的。
[name="埃内斯托"]事实上是人越多越有利的比赛。
[character(name="avg_npc_196_1#1",name2="char_010_chen_summer",focus=2)]
[name="陈"]多一个人比少一个人强。没问题吧，林雨霞？
[character(name="avg_npc_196_1#5",name2="char_010_chen_summer",focus=1)]
[name="林雨霞"]随便。
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]距离正式比赛还有两天时间，两位也可以再去找人。
[character(name="char_010_chen_summer")]
[name="陈"]不用了，就我们三个人吧。
[character(name="avg_npc_200")]
[name="工作人员"]那个，两位，请问你们可以上台了吗？
[character(name="char_010_chen_summer")]
[name="陈"]再加一个，三个。
[Dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_200")]
[name="海选主持人"]那么，让我们给本场海选的胜利者送去最热烈的掌声！
[dialog]
[playsound(key="$livecrowd")]
[delay(time=2)]
[character(name="avg_npc_200")]
[name="海选主持人"]请问三位有给自己的队伍起好名字吗？
[character(name="avg_npc_196_1#1",name2="char_010_chen_summer",focus=2)]
[name="陈"]怎么说？
[character(name="avg_npc_196_1#1",name2="char_010_chen_summer",focus=1)]
[name="林雨霞"]......你来起。
[character(name="avg_npc_196_1#1",name2="char_010_chen_summer",focus=2)]
[name="陈"]那就叫......鼠胆龙威队吧。
[

... (全文23075字符)
```

### level_act12side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[Delay(time=1)]
[PlayMusic(intro="$fesedm_intro", key="$fesedm_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_NPC_017_3")]
[name="D.D.D."]亲爱的观众们，万众期待的第八届多索雷斯极限铁人大奖赛，即将正式开幕！
[name="D.D.D."]在开幕前，让我们有请我们敬爱的坎黛拉市长发表开幕词。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_198_1#3")]
[name="坎黛拉"]市民们，游客们，欢迎来到我引以为豪的城市，多索雷斯！
[character(name="avg_npc_198_1#2")]
[name="坎黛拉"]无论你来自哪里，无论你有着怎么样的过去。
[character(name="avg_npc_198_1#5")]
[name="坎黛拉"]既然你能够来到这座城市，那就都放下吧。
[name="坎黛拉"]享受这座城市带给你的一切，享受你应该享受的一切吧。
[name="坎黛拉"]高兴起来，欢笑起来，尖叫起来。
[name="坎黛拉"]这里是我为你们所有人打造的乐园！
[character(name="avg_npc_198_1#3")]
[name="坎黛拉"]来吧，在这里收获你们一生中最难忘的时光吧！
[dialog]
[character]
[CameraShake(duration=1.5, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$livecrowd")]
[delay(time=1)]
[character(name="avg_NPC_017_3")]
[name="D.D.D."]好的，非常感谢坎黛拉市长一如既往点燃激情的开幕词，那么，接下来，我们来介绍各位参赛选手。
[name="D.D.D."]今年依旧有不少熟面孔，而且新面孔也不少！
[name="D.D.D."]首先，看起来是一对恩爱情侣，实际上也是一对恩爱情侣，但是战斗力却十分高的队伍！
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$livecrowd")]
[name="D.D.D."]甜蜜夏日队！
[dialog]
[character]
[character(name="avg_npc_201",name2="avg_npc_202",focus=1)]
[name="急躁的男游客"]是爱的力量让我们相遇。
[character(name="avg_npc_201",name2="avg_npc_202",focus=2)]
[name="懒散的女游客"]是爱的力量让我们相爱。
[character(name="avg_npc_201",name2="avg_npc_202",focus=0)]
[name="男游客&女游客"]我们两个人爱的力量，是无敌的！
[dialog]
[character]
[delay(time=0.51)]
[character(name="avg_NPC_017_3")]
[name="D.D.D."]爱的力量如此闪耀，连我都要眩晕过去了！让我们拭目以待爱的力量能够走多远吧！
[dialog]
[delay(time=1)]
[name="D.D.D."]然后是单人成队，来自大胃王海选的出线选手，水月！
[name="D.D.D."]外表人畜无害，却吃掉了我们一家餐厅仓库存量的食物，拥有着无底的胃袋以及与这片海洋相得益彰的蓝色头发。
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$livecrowd")]
[name="D.D.D."]吃豆人队！
[dialog]
[character]
[character(name="avg_437_mizuki_1#7")]
[name="水月"]哈喽哈喽，大家好呀。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]水月选手，有什么振奋人心的参赛宣言吗？
[character(name="avg_437_mizuki_1#3")]
[name="水月"]嗯......玩腻了就把你们都吃掉哦。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]噢噢噢，水月选手，用最平淡的口吻说出了最恐怖的话，让我们期待他的活跃！
[dialog]
[delay(time=1)]
[name="D.D.D."]接下来，是由本地人组成的队，队长拉菲艾拉小姐虽然外表可爱，却拿着一把凶恶大镰，这种反差正是这支队伍的一大看点。
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$livecrowd")]
[name="D.D.D."]让我们欢迎——灰羽队！
[dialog]
[character]
[character(name="avg_421_laplum_1#7")]
[name="拉菲艾拉"]大家好哦。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]拉菲艾拉小姐，你的参赛宣言是什么？
[character(name="avg_421_laplum_1#7")]
[name="拉菲艾拉"]嗯......我会努力的。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]嗯嗯，好的，好的，有的时候，朴实无华才最动人！灰羽队，我很看好你们！
[dialog]
[delay(time=1)]
[name="D.D.D."]紧接着，是本次比赛的新面孔，却也是最受瞩目的一队！
[name="D.D.D."]中途插入混战海选，以无人能敌的姿态获胜，得到了潘乔先生青睐的超新星。
[name="D.D.D."]由两位来自双日城友好城市——龙门的女侠，林雨霞小姐，陈晖洁小姐，以及本地的武器店老板，埃内斯托先生组成的队伍————
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$livecrowd")]
[name="D.D.D."]————鼠胆龙威队！
[name="D.D.D."]又强又新的队伍总是让人欲罢不能，他们的赔率相当高，但是，你真的敢对他们下注吗？
[dialog]
[character]
[delay(time=0.6)]
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#5",fadetime=0.1)]
[delay(time=1)]
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]唉。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]哈。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_NPC_017_3")]
[name="D.D.D."]那么，请队长发表一下参赛宣言吧。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]谁是队长？
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]埃内斯托，你来吧。
[character(name="avg_486_espumo_1#3")]
[name="埃内斯托"]啊？
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]反正林雨霞不可能听我的。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]你也不可能听我的。
[character(name="avg_486_espumo_1#3")]
[name="埃内斯托"]呃，好吧。
[character(name="avg_486_espumo_1#5")]
[playsound(key="$livecrowd")]
[name="埃内斯托"]那么，我们的参赛宣言是——在这场比赛的历史上刻下属于我们的痕迹！
[delay(time=1)]
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]怎么样，二位？
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]一般。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]确实。
[character(name="avg_486_espumo_1#5")]
[name="埃内斯托"]我想也是。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]非常霸气的宣言！让我们期待鼠胆龙威队的精彩表现。
[name="D.D.D."]然后，接下来的队伍是......
[Dialog]
[character]
[largebgtween(xFrom=-720,xTo=-180,  duration=1, ease="1", block=true)]
[delay(time=0.6)]
[playsound(key="$rungeneral")]
[character(name="avg_npc_203_1#1",name2="char_empty",fadetime=1)]
[delay(time=1.5)]
[name="星熊"]喂，Missy，这边。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=2)]
[name="诗怀雅"]来了！喂，别挤，我的冰淇淋！
[name="诗怀雅"]真是，人也太多了吧......
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]说明这场比赛万众瞩目啊。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]比起这个，你快看，老陈居然拿着跟铳差不多的玩意。
[name="星熊"]看来她这次是不打算用剑了啊。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#6",focus=2)]
[name="诗怀雅"]她这不是作茧自缚吗，她射击训练成绩也就和我差不多吧。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#6",focus=1)]
[name="星熊"]哇，你不要把优秀说得和不要钱一样好不好。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#2",focus=2)]
[name="诗怀雅"]她剑术可不止是优秀的水平。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#2",focus=1)]
[name="星熊"]哎，M

... (全文11494字符)
```

### level_act12side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[character(name="avg_NPC_017_3")]
[Delay(time=1)]
[PlayMusic(intro="$fesedm_intro", key="$fesedm_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="D.D.D."]好强，太强了！鼠胆龙威队，在被三支队伍联手围攻的局面之下，轻松将他们击退！
[name="D.D.D."]不过，林女侠在战斗中使用的究竟是什么能力？
[name="D.D.D."]导播，切一下回放！
[Dialog]
[delay(time=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.2, block=true)]
[Character]
[musicvolume(volume=0.2,fadetime=1)]
[Delay(time=2)]
[largebg]
[Background(image="bg_20_G02",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.5, keep=true)]
[Character(name="avg_npc_196_1#1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.2, block=true)]
[Delay(time=1)]
只见林雨霞的手在身边房屋的玻璃窗上轻轻一抹，玻璃如同熔化了一般缓慢消失。
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.2, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.2, block=true)]
[delay(time=1)]
而后，她的手中出现了一把锋利的刀刃，这把刀刃几近无色，只有反射阳光带来的细微光芒证明着它确实存在。
[Dialog]
[delay(time=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Delay(time=2)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[musicvolume(volume=0.4,fadetime=1)]
[character]
[character(name="avg_NPC_017_3")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.2, block=true)]
[musicvolume(volume=0.4, fadetime=1)]
[Delay(time=1)]
[name="D.D.D."]这一回终于看清楚了，林女侠居然能够将玻璃转化为武器，这真是令人意想不到的能力！
[name="D.D.D."]没想到林女侠不光武艺高超，还有这般精彩的源石技艺！
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]哎，不过Missy，林小姐这是什么能力？
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#7",focus=2)]
[name="诗怀雅"]和鼠王一样，其实她也是在操纵沙子，只是方向不太一样。
[name="诗怀雅"]她从小能随随便便地把沙子变成玻璃什么的，我经常问她要来玩。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]噢，懂了，确实，玻璃也是用沙子做的。
[name="星熊"]哎，我听说鼠王可以用沙子搞出沙尘暴，林小姐行不行啊？
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]不知道，不过我猜她就算会，也不会喜欢那么做。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=1)]
[name="星熊"]也是，林小姐看起来不像是喜欢大开大合的类型。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_NPC_017_3")]
[name="D.D.D."]林女侠那防不胜防的源石技艺，配合陈女侠精准的铳法，还有埃内斯托先生的补漏，一次完美的视觉盛宴！
[name="D.D.D."]如何，潘乔先生，您认为这次的胜利会属于这支队伍吗？
[character(name="avg_npc_192_1#1")]
[name="潘乔"]这支队伍个人能力很强，不过配合还欠缺火候。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]原来如此，确实，在这样的比赛中，如果过分强调个人能力，可是会被其他人盯上然后排除掉的。
[name="D.D.D."]历史一再地向我们证明，只有团结才能够取得最后的胜利！
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]这个老头眼光很尖啊，一眼就看出来老陈和林小姐现在最大的问题。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#1",focus=2)]
[name="诗怀雅"]确实，这两个人，老陈么，跟你搭档惯了至少知道配合，不过她完全不知道林雨霞是怎么打的，自己又用的不是最拿手的剑，束手束脚的。
[name="诗怀雅"]至于林雨霞，这个女人就根本不知道配合这两个字是怎么写的。
[name="诗怀雅"]我看好几次她差点把老陈也伤到了，全靠老陈反应够快闪了过去。
[name="诗怀雅"]笑死我了，不知道的还以为她们俩配合无间呢。
[name="诗怀雅"]那个叫埃内斯托的倒也聪明，根本没往两个人身边靠。
[name="诗怀雅"]不然啊，他有几条命都不够用。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#1",focus=1)]
[name="星熊"]不错啊，Missy，观察力越来越好了，我还以为我要给你讲解一下呢。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]为了接过陈晖洁的位置我也是很努力的好不好。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=1)]
[name="星熊"]我可从没怀疑过这一点，只是没想到Missy你的进步这么快，真不错。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#6",focus=2)]
[name="诗怀雅"]别一副老前辈的样子在那感慨了，小心我扣你工资。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#6",focus=1)]
[name="星熊"]哎，那可千万别，您老大人有大量，别跟我一个小卒一般计较。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#7",focus=2)]
[name="诗怀雅"]哼，这还像话。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]不过你还真别说，看她们这配合，让我有点想起刚认识老陈的时候了。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=2)]
[name="诗怀雅"]她那时就这样？
[character(name="avg_npc_203_1#2",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]哪里，反过来，那时的她，和现在的林小姐差不多吧。
[name="星熊"]要是让那时的她和现在的林小姐组队，那恐怕真的打着打着她们两个就打起来了，哈哈。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic(fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg]
[Background(image="bg_20_G02")]
[Delay(time=1)]
[PlayMusic(intro="$chasing_intro",key="$chasing_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[character(name="avg_1013_spchen_1#6",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]你的玻璃刀好几次差点割到我。
[character(name="avg_1013_spchen_1#6",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]你的水弹准头也不怎么样。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]看来不只是情感上，战术上我们也不适合组队。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]很有说服力的结论，还是分头行动吧。
[character(name="avg_486_espumo_1#2")]
[name="埃内斯托"]等等。
[dialog]
[delay(time=1)]
[name="埃内斯托"]......这样吧。
[name="埃内斯托"]虽然我知道两位彼此不太对付，不过既然组成了队伍，那还是尽量像一支队伍一样行动吧。
[name="埃内斯托"]之前也说过，比赛途中无法通信，而且两位不仅要找赤金，还想要调查可能存在的危险分子。
[name="埃内斯托"]虽然两位的个人能力很强，但炎国不是有句话叫做——不怕一万，只怕万一。
[name="埃内斯托"]所以我的提议是，无论有没有获得赤金，我们一小时在这里碰一次头，如何？
[name="埃内斯托"]如果有一方没来，另一方见机行事。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]我没意见。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]可以。
[character(name="avg_486_espumo_1#5")]
[name="埃内斯托"]呼，两位愿意配合那再好不过，那就这么办吧。
[character(name="avg_npc_196_1#5")]
[name="林雨霞"]那我先走一步。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1)]
[delay(time=1.5)]
[character(name="avg_486_espumo_1#3")]
[name="埃内斯托"]林小姐走得真快......
[character(name="avg_1013_spchen_1#1",name2="avg_486_espumo_1#1",focu

... (全文6633字符)
```

### level_act12side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[character(name="avg_NPC_017_3")]
[Delay(time=1)]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="D.D.D."]距离比赛开始已经过去了半个多小时，而令人吃惊的是，居然还没有一支获得了赤金的队伍选择提前结束比赛。
[name="D.D.D."]看起来，这一次大奖赛的参赛选手们野心都非常的大！
[name="D.D.D."]潘乔先生，您怎么看？
[character(name="avg_npc_192_1#7")]
[name="潘乔"]看起来今年的大奖赛会是非常激烈的一届，我很期待。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]没错，想必所有观众都和潘乔先生是同样的心情。
[name="D.D.D."]我们的各个分舞台将会持续进行对各个队伍的追踪，以保证观众们不会错过任何一场精彩的战斗。
[name="D.D.D."]而我们的观众也不要闲下来，让我们将这份急迫的心情转换成投票的动力，为心爱的选手投出宝贵的一票吧！
[name="D.D.D."]为他花钱，才是真的爱他！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg]
[Background(image="bg_20_G02")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[character(name="avg_npc_202",name2="avg_npc_204",focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="懒散的女游客"]亲爱的，救命！
[character(name="avg_npc_202",name2="avg_npc_204",focus=-1)]
[name="急躁的男游客"]别怕，宝宝，我这就来救你！
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="left", type="move", xpos=-300, fadetime=1.5,block=false)]
[character(name="char_empty",name2="avg_npc_204",fadetime=0.5)]
[delay(time=1.5)]
[character(name2="avg_npc_204")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[character(name="avg_npc_201",name2="avg_npc_204",enter="left",fadetime=0.5)]
[dialog]
[Character(name="avg_npc_201",name2="avg_npc_204")]
[delay(time=0.51)]
[characteraction(name="left", type="jump", xpos=100, power=0, times=1, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral",volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[characteraction(name="left", type="jump", xpos=-100, power=5, times=1, fadetime=1,block=true)]
[dialog]
[Delay(time=1)]
[Character(name="avg_npc_201",name2="avg_npc_204",focus=2)]
[name="急躁的参赛选手"]啧，还以为这对情侣是来搞笑的，怎么这么能打？！
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_202",name2="avg_npc_201",focus=2)]
[name="急躁的男游客"]宝宝，太好了，我差点以为我要失去你了。 （小声）你就不能自己想想办法吗？！
[character(name="avg_npc_202",name2="avg_npc_201",focus=1)]
[name="懒散的女游客"]呜呜呜，他们好凶。 （小声）*玻利瓦尔俚语*，我的人设可是弱女子！
[character(name="avg_npc_202",name2="avg_npc_201",focus=2)]
[name="急躁的男游客"]没关系，已经没事了，看我狠狠教训他们一顿！ （小声）啧，姑奶奶你也努努力好不好。
[character(name="avg_npc_202",name2="avg_npc_201",focus=1)]
[name="懒散的女游客"]亲爱的，你是最棒的~ （小声）你敢凶我？！
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_196_1#5")]
[name="林雨霞"]（这两个人，身手很不错，而且有军旅气质，恐怕过去是军人。）
[name="林雨霞"]（至于情侣身份，恐怕是一种噱头，用来博取观众好感。）
[name="林雨霞"]（虽然很浮夸，不过不失为一种方法。）
[character(name="avg_npc_196_1#4")]
[name="林雨霞"]（虽然真的很浮夸。）
[character(name="avg_npc_196_1#1")]
[name="林雨霞"]（要是诗怀雅那个女人看到，大概会兴冲冲地说她也想在这种比赛玩一玩这种角色扮演。）
[character(name="avg_npc_196_1#5")]
[name="林雨霞"]（......还是不要让她知道比较好。）
[dialog]
[delay(time=1)]
[name="林雨霞"]（总之，这对情侣稳赢，没什么好看的了，这里搜了一圈也没有赤金，该走了。）
[name="林雨霞"]（二十块赤金，恐怕有不少被放在了显眼的位置，比如各种地标建筑上，那些地方会很抢手。）
[name="林雨霞"]（没什么必要去抢这些赤金。）
[name="林雨霞"]（我应该去找那些剩下的被藏在隐蔽角落的赤金。）
[name="林雨霞"]（不过......如果真的存在想通过比赛引发混乱的家伙，他们至少肯定会寻找无人机和摄像头的死角再采取行动。）
[character(name="avg_npc_196_1#4")]
[name="林雨霞"]（两边都有做的必要......应该先和陈晖洁商量一下的，啧，走得太急了。）
[character(name="avg_npc_196_1#5")]
[name="林雨霞"]（算了，我也不想和那个幼稚的女人商量，走一步看一步吧。）
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic(fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[character(name="avg_1013_spchen_1#1",name2="avg_486_espumo_1#1",focus=2)]
[name="埃内斯托"]陈小姐，我可以问个问题吗？
[character(name="avg_1013_spchen_1#1",name2="avg_486_espumo_1#1",focus=1)]
[name="陈"]什么？
[character(name="avg_1013_spchen_1#1",name2="avg_486_espumo_1#1",focus=2)]
[name="埃内斯托"]你和林小姐原本是朋友吧？
[character(name="avg_1013_spchen_1#2",name2="avg_486_espumo_1#1",focus=1)]
[name="陈"]......为什么你会这么认为？
[character(name="avg_1013_spchen_1#2",name2="avg_486_espumo_1#5",focus=2)]
[name="埃内斯托"]因为要说你们是仇人的话，感觉没有那么尖锐。而要说你们只是有过节的话，你们又明显挺了解对方的。
[character(name="avg_1013_spchen_1#2",name2="avg_486_espumo_1#1",focus=1)]
[name="陈"]......算是吧。
[name="陈"]小的时候读过同一所小学，而且有一个共同的熟人。
[name="陈"]所以你猜得相当接近。
[character(name="avg_1013_spchen_1#1",name2="avg_486_espumo_1#1",focus=1)]
[name="陈"]不过我不会告诉你我为什么会和她关系不好。
[character(name="avg_1013_spchen_1#1",name2="avg_486_espumo_1#6",focus=2)]
[name="埃内斯托"]没事，像你们这样的人，要是有过节肯定不是小事，我也不打算细问，只是找个话题罢了。
[character(name="avg_1013_spchen_1#1",name2="avg_486_espumo_1#1",focus=2)]
[name="埃内斯托"]不过，你们看起来都没想到对方会出现在这里。
[name="埃内斯托"]那不管怎么说，也算是一种缘分，你有没有考虑过和她重新搞好关系？
[character(name="avg_1013_spchen_1#1",name2="avg_486_espumo_1#1",focus=1)]
[name="陈"]你很关心这件事？
[character(name="avg_1013_spchen_1#1",name2="avg_486_espumo_1#2",focus=2)]
[name="埃内斯托"]那倒不是......或者也是，这座城市里一天到晚都是钱钱钱的，友情这种东西很奢侈的。
[character(name="avg_1013_spchen_1#2",name2="avg_486_espumo_1#2",focus=1)]
[name="陈"]......这不是我或者她想要搞好关系就能搞好关系的事。
[character(name="avg_1013_spchen_1#2",name2="avg_486_espumo_1#3",focus=2)]
[stopmusic(fadetime=1)]
[name="埃内斯托"]等等，陈小姐，看那边巷子里。
[dialog]
[character]
[delay(time=1)]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.4)]
[character(name="avg_437_mizuki_1#4")]
[name="水月"]嗯......有点麻烦。
[character(name="avg_437_mizuki_1#2")]
[name="水月"]摄像头这么多，万一动起手来下手太重就不妙了欸。
[character(name="avg_npc_205")]
[name="急躁的参赛选手"]啧，不知道为什么，老是打不中这小子，莫名其

... (全文12215字符)
```

### level_act12side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[character(name="avg_NPC_017_3")]
[Delay(time=1)]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="D.D.D."]太惊人了，陈女侠，先是杀入巷子中救下被围攻的水月选手，然后直接在巷子中与其他参赛选手对峙。
[name="D.D.D."]其他队伍看来也已经认定鼠胆龙威队是个巨大的威胁，非常默契地达成了联手。
[name="D.D.D."]但是即使如此，陈女侠也丝毫不惧，选择与他们开战。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="D.D.D."]真是一场酣畅淋漓的战斗！
[dialog]
[delay(time=1)]
[name="D.D.D."]不过我们也不能忘记在巷子的另一边，林女侠的战斗！
[name="D.D.D."]和陈女侠在巷子中激烈的战斗不同，林女侠在巷子口仅凭几招就威慑住了赶来的其他队伍。
[name="D.D.D."]这次大奖赛中，真的有能够战胜这个组合的队伍存在吗？！
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]哈哈，这两个人果然还是适合各打各的。
[name="星熊"]哎，Missy，你猜老陈和林小姐对打的话，谁会赢？
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]问这个干嘛？
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=1)]
[name="星熊"]就是很感兴趣啊，两个很厉害的人放一起，一般都会想知道谁更厉害吧。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=2)]
[name="诗怀雅"]只有你才会这么想吧！
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]反正我不知道，今天是我这几年第一次看到这个女人真的出手。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#5",focus=1)]
[name="星熊"]啊？你不是和林小姐关系很好吗，这都没见过。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#6",focus=2)]
[name="诗怀雅"]谁和她关系好啊，整天神神秘秘的，有的时候电话都打不通。
[name="诗怀雅"]而且谁说熟了就一定要看过对方动手啊。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#6",focus=1)]
[name="星熊"]也有道理，看来是我跟老陈相处习惯了。老陈现在想赢我可不能只靠她那套剑法了。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]别把所有人都当成你们俩好不好。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#2",focus=2)]
[name="诗怀雅"]再说了，我没见过才好，我怕哪天我见到的时候就是要抓她的时候了。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#2",focus=1)]
[name="星熊"]有道理，毕竟是那位鼠王的女儿。
[name="星熊"]哎，不过也不能这么说，那位也不是什么坏人。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#2",focus=1)]
[name="星熊"]我刚来龙门混的时候......
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]行了，我又不是没见过鼠王，还用你告诉我。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=1)]
[name="星熊"]嗨，你明白就好。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#6",focus=2)]
[name="诗怀雅"]比起这个，你刚才用了“混”字吧。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#6",focus=1)]
[name="星熊"]瞧我，在诗大小姐面前说粗话，该掌嘴。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#2",focus=2)]
[name="诗怀雅"]哼。
[dialog]
[delay(time=1)]
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#6",focus=2)]
[name="诗怀雅"]所以你和老陈就见过她出手啊？
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#6",focus=1)]
[name="星熊"]我这不是没有才来问你嘛，老陈我估计也没有。
[name="星熊"]有一点你说得倒是没错，没见过她出手对我们这种立场的人是好事，不然熟归熟，该做的少不了。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#7",focus=2)]
[name="诗怀雅"]知道就好。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]所以我也没想到，居然会有老陈和她联手的一天。
[name="星熊"]真是活久了什么都能见到。
[name="星熊"]说回刚才的话题，所以你觉得谁会赢？
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#2",focus=2)]
[name="诗怀雅"]懒得猜。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#2",focus=1)]
[name="星熊"]哎，那我自己猜。
[name="星熊"]要我说，老陈要是拿着剑，林雨霞大概很难近她的身。
[name="星熊"]但是，要是让林雨霞近了身，老陈就输定了。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=2)]
[name="诗怀雅"]陈这么菜。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]也不能这么说，老陈的拳脚功夫肯定是不差的，擒拿、关节技什么的，咱们平时培训的她都做得很好。
[name="星熊"]你看她刚才打的，她用铳准头也不差。
[name="星熊"]但是老陈毕竟拿手的是剑术。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=2)]
[name="诗怀雅"]你的意思是林雨霞的拳脚功夫相当于老陈的剑术。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]差不多吧。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[largebg]
[Background(image="bg_20_G02")]
[Delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[character(name="avg_npc_196_1#1",name2="avg_1013_spchen_1#2",focus=1)]
[name="林雨霞"]陈晖洁，逞英雄开心吗？
[character(name="avg_npc_196_1#1",name2="avg_1013_spchen_1#2",focus=2)]
[name="陈"]不怎么开心，不过也不用你操心。
[character(name="avg_1013_spchen_1#1",name2="avg_486_espumo_1#3",focus=2)]
[name="埃内斯托"]抱歉，陈小姐，我......
[character(name="avg_1013_spchen_1#1",name2="avg_486_espumo_1#3",focus=1)]
[name="陈"]我说了，你在那里等我就好，你做得没有问题。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_437_mizuki_1#7",name2="avg_1013_spchen_1#1",focus=1)]
[name="水月"]谢谢你帮了我。
[character(name="avg_437_mizuki_1#7",name2="avg_1013_spchen_1#2",focus=2)]
[name="陈"]客气。
[character(name="avg_437_mizuki_1#4",name2="avg_1013_spchen_1#2",focus=1)]
[name="水月"]不过，你为什么要帮我呢？
[character(name="avg_437_mizuki_1#4",name2="avg_1013_spchen_1#1",focus=2)]
[name="陈"]不为什么，看到了，就帮了。
[character(name="avg_437_mizuki_1#3",name2="avg_1013_spchen_1#1",focus=1)]
[name="水月"]这样啊。姐姐你是个好人呢。
[character(name="avg_437_mizuki_1#1",name2="avg_1013_spchen_1#1",focus=1)]
[name="水月"]既然这样，给。
[character(name="avg_486_espumo_1#3")]
[name="埃内斯托"]这是......赤金？
[character(name="avg_437_mizuki_1#1")]
[name="水月"]嗯，我刚才就是想拿这个才被他们围住的。
[character(name="avg_486_espumo_1#3")]
[name="埃内斯托"]给我们没关系吗？
[character(name="avg_437_mizuki_1#7")]
[name="水月"]没事，我再去找就是了。
[character(name="avg_437_mizuki_1#1")]
[name="水月"]而且，我本来就不是很在乎比赛，能够认识陈姐姐这样的好人，对我来说已经很满足了。
[character(name="avg_npc_196_1#5")]
[name="林雨霞"]提醒一下，这里已经惊动了不少队伍，想聊天可以，别在这里停留太久比较好。
[character(name="avg_437_mizuki_1#3")]
[name="水月"]那我就先走啦，拜拜~
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1.5)]
[delay(time=2)]
[character(name="avg_npc_196_1#1",name2="avg_1013_spchen_1#1",focus=2)]
[name="陈"]我们也走吧。
[character(name="avg_npc_196_1#5",name2="avg_1013_spchen

... (全文8256字符)
```

### level_act12side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[character(name="avg_NPC_017_3")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="D.D.D."]首先，先来一点音乐！
[dialog]
[PlayMusic(intro="$ddd_intro", key="$ddd_loop", volume=0.6)]
[delay(time=1.5)]
[PlaySound(key="$livecrowd")]
[name="D.D.D."]那么，经过一天的等待，我们即将迎来大奖赛的第二轮比赛——铁人三项！
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image(image="20_I02_2",screenadapt="coverall", fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="D.D.D."]比赛规则十分简单，先是跑步，再是骑行，最后是游泳！
[name="D.D.D."]妨碍他人？没有问题！只要队伍中有一个人抵达终点就算出线！
[name="D.D.D."]抄近道是被允许的，但是要当心那埋伏在巷道里的家伙！他们可不会轻易让你通过！
[name="D.D.D."]而且，抵达终点的人，如果没有通过骑行和游泳的两个检查点的话，成绩是不被认可的！
[name="D.D.D."]也就是说，选手们可以在比赛开始后转身就跳入海中游上游轮，但那只会让你成为全城的笑柄。
[name="D.D.D."]如果你是个富豪，近地飞行器也是个可选项！
[name="D.D.D."]但是，如果不讨好观众的话，可是有可能被投票出局的！
[name="D.D.D."]另外，由于第一轮出线的队伍是十五支，加上一支通过观众投票复活的队伍，第一轮一共出线十六支队伍。
[name="D.D.D."]因此，第二轮的出线数量将是八支。
[name="D.D.D."]最先抵达游轮的八支队伍将获得出线的权利！
[name="D.D.D."]那么，让我们接下来有请十六支参赛队伍登场！
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-180)]
[musicvolume(volume=0.2,fadetime=1)]
[Image]
[delay(time=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_190_1#1",name2="avg_npc_206_1#8",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_npc_190_1#6",name2="avg_npc_206_1#8",focus=1)]
[name="艾雅法拉"]好漂亮的海......
[character(name="avg_npc_190_1#6",name2="avg_npc_206_1#8",focus=2)]
[name="铸铁"]确实。
[name="铸铁"]看来这座城市果然没白来。
[character(name="avg_npc_190_1#6",name2="avg_npc_206_1#8",focus=2)]
[name="铸铁"]我们就在这里坐下吧。
[character(name="avg_npc_190_1#4",name2="avg_npc_206_1#1",focus=1)]
[name="艾雅法拉"]要不然我还是回去吧，会给这里的其他人添麻烦的......
[character(name="avg_npc_190_1#4",name2="avg_npc_206_1#8",focus=2)]
[name="铸铁"]别太在意。这座城市好像不太在乎感染者问题的样子。
[character(name="avg_npc_190_1#4",name2="avg_npc_206_1#7",focus=2)]
[name="铸铁"]虽然很明显，这并不是因为他们开明，而是他们不在乎......
[character(name="avg_npc_190_1#4",name2="avg_npc_206_1#1",focus=2)]
[name="铸铁"]而且，有苏苏洛跟着，不会有问题的，对吧？
[character(name="avg_npc_199_1#1")]
[name="苏苏洛"]嗯。艾雅法拉小姐的病症我心里有数。
[name="苏苏洛"]其实你与其担心给别人添麻烦，更应该担心的是自己。
[name="苏苏洛"]你比其他人都要更加久居室内，这不仅对身体不好，对精神卫生也有影响。
[character(name="avg_npc_199_1#6")]
[name="苏苏洛"]这也是这一次我作为医生赞成将艾雅法拉小姐你带到这里来的理由。
[character(name="avg_npc_199_1#7")]
[name="苏苏洛"]每个人都应该拥有享受阳光的权利。
[character(name="avg_npc_190_1#4",name2="avg_npc_206_1#8",focus=2)]
[name="铸铁"]就是。
[character(name="avg_npc_190_1#4",name2="avg_npc_206_1#1",focus=2)]
[name="铸铁"]虽然博士那边也是遇到了麻烦，但是隔着屏幕听说他们在度假那叫什么事啊。
[name="铸铁"]我们艾雅法拉也该有个休假才对。
[character(name="avg_npc_190_1#2",name2="avg_npc_206_1#1",focus=1)]
[name="艾雅法拉"]没有，我是自愿做地质研究的，而且要是耽误大家......
[character(name="avg_npc_190_1#2",name2="avg_npc_206_1#8",focus=2)]
[name="铸铁"]哎呀，你就别操心了。
[character(name="avg_npc_190_1#2",name2="avg_npc_206_1#7",focus=2)]
[name="铸铁"]我们来这边也是有正当理由的，罗德岛想要在这座城市设立办事处，一直没有得到这座城市市长的同意。
[name="铸铁"]阿米娅让我们来再当一次说客。
[character(name="avg_npc_190_1#4",name2="avg_npc_206_1#8",focus=2)]
[name="铸铁"]所以你就安心在这里享受比赛节目吧。
[character(name="avg_npc_190_1#6",name2="avg_npc_206_1#8",focus=1)]
[name="艾雅法拉"]嗯，谢谢。
[character(name="avg_npc_190_1#6",name2="avg_npc_206_1#1",focus=2)]
[name="铸铁"]对了，红呢？
[character(name="avg_npc_206_1#1",name2="avg_npc_199_1#1",focus=2)]
[name="苏苏洛"]她好像不打算出来，一个人不知道哪里去了。
[character(name="avg_npc_206_1#5",name2="avg_npc_199_1#1",focus=1)]
[name="铸铁"]好吧，这家伙出任务以来就是这个样子，我也习惯了。
[dialog]
[delay(time=0.7)]
[character(name="avg_npc_206_1#1")]
[name="铸铁"]哦，快看，来了来了！
[dialog]
[character]
[largebgtween(xFrom=-180,xTo=-720,  duration=1, ease="1", block=true)]
[delay(time=1)]
[character(name="avg_NPC_017_3")]
[name="D.D.D."]让我们欢迎，鼠胆龙威队！
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$livecrowd")]
[character]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#5",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]......
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]......
[character(name="avg_486_espumo_1#5")]
[name="埃内斯托"]啊哈哈。
[character(name="avg_npc_196_1#1")]
[name="林雨霞"]还是分头行动？
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]铁人三项赛程很长，各做各的很容易失去联系。
[name="埃内斯托"]其他队伍里除了单独分出人来妨碍其他队伍，基本上都是共同行动的。
[name="埃内斯托"]两位要是没有类似的想法我还是建议一起行动。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]我没意见。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]也可以。动手的时候别妨碍我就好。
[character(name="avg_1013_spchen_1#7",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]原话奉还。
[dialog]
[character]
[largebgtween(xFrom=-720,xTo=-180,  duration=1, ease="1", block=true)]
[delay(time=1)]
[character(name="avg_npc_206_1#4")]
[name="铸铁"]真是没想到，一开始看电视我还以为看错了，没想到陈也来到了这里。
[name="铸铁"]看起来她也在度假中，等比赛结束后，我们去和她打个招呼吧。
[character(name="avg_npc_190_1#6")]
[name="艾雅法拉"]嗯。
[character(name="avg_npc_206_1#1")]
[name="铸铁"]好了，你们先看，我去给你们买点吃的，你们就在这里不要随意走动啊。
[character(name="avg_npc_199_1#7")]
[name="苏苏洛"]好。
[dialog]
[character]
[largebgtween(xFrom=-180,xTo=-720,  duration=1, ease="1", block=true)]
[delay(time=1.5)]
[character(name="avg_NPC_017_3")]
[name="D.D.D."]以上就是所有十六支队伍的介绍。
[name="D.D.D."]和第一轮一样，为了让观众们也享受到参与比赛的乐趣，我们为观众们也准备了丰富多彩的投注竞猜项目。
[name="D.D.D."]各位观众在官方网站上登录自己的信息后可以为自己赚一笔外快！
[name="D.D.D."]具体操作流程请参照官方发布的比赛指南。
[name="D.D.D."]第二轮比赛中，我们的嘉宾配置将有所变化。
[name="D.D.D."]潘乔先生为了准备第三轮比赛已经先一步前往了游轮上，他将通过视频连线的方式和观众们对话。
[name="D.D.D."]那么，参赛选手们已经都来到了预备线上，请坎黛拉女士来为我们拉响第二轮的礼炮吧！
[dialog]
[character]
[delay(time=

... (全文6838字符)
```

### level_act12side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[character(name="avg_NPC_017_3")]
[Delay(time=1)]
[PlayMusic(intro="$emperor_intro", key="$emperor_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="D.D.D."]虽然在比赛之初就被其他队伍盯上，但是鼠胆龙威队再次上演了一场精彩的突围。
[dialog]
[PlaySound(key="$phonevibration",volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[name="D.D.D."]潘乔先生，您在第一轮中提到了这支队伍的配合问题，那现在您怎么看？
[characteraction(name="middle", type="move", xpos=200, fadetime=1,block=true)]
[CharacterCutin(widgetID="1", name="avg_npc_192_1#1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=-300, width=200, block=true)]
[character(name="avg_NPC_017_3",focus=-1)]
[name="潘乔"]配合问题不是一夜之间就能解决的。
[name="潘乔"]不过很明显，这两个人自己也知道这个问题，所以她们在战斗中很明显有了分工。
[name="潘乔"]这一次，比第一轮里的战斗，要利落许多。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]原来如此，也就是说，他们获胜的几率变得更高了吗？
[character(name="avg_NPC_017_3",focus=-1)]
[name="潘乔"]还不好说，其他选手也会有自己的对策。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]说的也是，普通的阻拦对鼠胆龙威队已经不生效了，让我们期待一下其他选手会不会有什么新招吧！
[character]
[CharacterCutin(widgetID="1",block=true)]
[dialog]
[delay(time=1)]
[musicvolume(volume=0.4,fadetime=1)]
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]嘿，说得没错。
[name="星熊"]而且她们之间气氛也缓和了一点，不知道是不是发生了什么。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=2)]
[name="诗怀雅"]居然是伊比利亚时代的产物，怪不得......
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]嗯？Missy，你不看比赛在看什么呢？
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]我在看这艘游轮的信息。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#5",focus=1)]
[name="星熊"]有什么有趣的吗，你刚才好像说到伊比利亚？
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]对，这艘船，其实前身是伊比利亚时期留下的东西。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#5",focus=1)]
[name="星熊"]这么早？......不过仔细想想，除了伊比利亚，确实好像应该没别的国家有这种东西。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]嗯。
[name="诗怀雅"]而且这艘船还是坎黛拉市长花了重金再从伊比利亚人手上买来技术改造出来的。
[name="诗怀雅"]而做这些只是为了让这艘船在这座城市的海上漂着。
[name="诗怀雅"]这片大地上我觉得都不会再有第二个人这么做了。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=1)]
[name="星熊"]那确实是奢侈到一定境界了。
[name="星熊"]说到这个，Missy，你不是这两天在研究这个市长，有什么结论吗？
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#2",focus=2)]
[name="诗怀雅"]结论......其实还挺简单的。
[name="诗怀雅"]这个坎黛拉·桑切斯，在某种意义上，是能和魏长官比肩的人物。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#2",focus=1)]
[name="星熊"]有这么厉害？
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#6",focus=2)]
[name="诗怀雅"]有。虽然方向完全不同，但他们都是胸中完全装下了自己的城市，完完全全握住了城市的缰绳的人。
[character(name="avg_npc_197_1#2")]
[name="诗怀雅"]作为龙门近卫局的一员，我绝对不会说我佩服建造了这样一座城市的人。
[character(name="avg_npc_197_1#6")]
[name="诗怀雅"]但是作为诗怀雅家的女儿，我也必须承认，建造了这样一座城市的人非常厉害。
[character(name="avg_npc_197_1#5")]
[name="诗怀雅"]如果说这座城市根基要远比它表现的那样更稳固，那么这座城市的上层建筑就比它表现得还要疯狂。
[name="诗怀雅"]三方政府的人每天都在涌入这座城市，新闻上也偶尔会有他们发生争执甚至发生小规模冲突的报道。
[character(name="avg_npc_197_1#6")]
[name="诗怀雅"]但是，没有人在乎。
[name="诗怀雅"]他们秘密而又公开地来到这里，遵守着心照不宣的规则，在这里享受着他们在外面无法享受到的乐趣。
[character(name="avg_npc_197_1#5")]
[name="诗怀雅"]你能想象吗？
[name="诗怀雅"]当三方中有人第一次在这里发生冲突时，一定是坎黛拉市长出面，用我们谁都无法想象的方法“说服”了他们。
[name="诗怀雅"]并且在那之后，任何人来到这座城市，都必须遵守她定下的规则。
[character(name="avg_npc_197_1#2")]
[name="诗怀雅"]但我不知道那是什么，一些把柄？还是政治筹码？
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#2",focus=1)]
[name="星熊"]坎黛拉女士手上有能够保护这座城市的武装力量，这是肯定的。
[name="星熊"]但是在那之上，我觉得答案很简单啊，Missy，你不是已经发现了吗？
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=2)]
[name="诗怀雅"]是什么啊？
[character(name="avg_npc_203_1#2",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]就是——酒，糖，咖啡，还有娱乐。
[character(name="avg_npc_203_1#2",name2="avg_npc_197_1#4",focus=2)]
[name="诗怀雅"]这些东西怎么可能......
[character(name="avg_npc_203_1#5",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]老话说得好啊，Missy，由俭入奢易。
[name="星熊"]别说娇生惯养的老爷们，就算是我，忽然要我失去一个我已经习惯了而且觉得很好的东西，我也会很难受。
[name="星熊"]更不要说一旦失去后，我就只能再去忍受那些破烂。
[name="星熊"]人的意志在有些时候是很软弱的，更不要说玻利瓦尔变成现在这样，你跟我说这里有许多意志坚定的人，我是不信的。
[character(name="avg_npc_203_1#5",name2="avg_npc_197_1#2",focus=2)]
[name="诗怀雅"]......
[character(name="avg_npc_203_1#2",name2="avg_npc_197_1#2",focus=1)]
[name="星熊"]一开始肯定没有那么顺利，但是久而久之，没有人能够站出来否定这一切，这一切也就成为了某种理所当然。
[name="星熊"]不过我也承认，能在一开始就决定将这座城市变成如今这副样貌，这个市长确实非常厉害。
[character(name="avg_npc_203_1#6")]
[name="星熊"]厉害到令人害怕的程度。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[largebg]
[Background(image="bg_20_G03")]
[Delay(time=1)]
[playMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[character(name="avg_npc_196_1#1")]
[name="林雨霞"]前面有个弯道，走近道？
[character(name="avg_1013_spchen_1#1")]
[name="陈"]没有必要，从地图来看，骑行阶段近道才多，即使有人想搞事，也应该是那时候的事。
[character(name="avg_486_espumo_1#4")]
[name="埃内斯托"]别忘了，近道里埋伏着大量坎黛拉女士的手下，这些人可能比危险分子还要危险。
[name="埃内斯托"]对方第一轮都没有出手的话，我想，第二轮他们只会更加谨慎。
[character(name="avg_1013_spchen_1#1")]
[name="陈"]嗯，走一步看一步吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#2")]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#2",focus=1)]
[name="星熊"]说起来，Missy，这个主持人你眼不眼熟？
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=2)]
[name="诗怀雅"]嗯？你这么一说，好像确实在哪里见过。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]嗯，我也觉得在哪里见过。
[character(name="avg_npc_206_1#1",name2="avg_npc_203_1#1",focus=1)]
[name="铸铁"]她是D.D.D.啊。
[chara

... (全文7507字符)
```

### level_act12side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[character(name="avg_NPC_017_3")]
[Delay(time=1)]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="D.D.D."]随着比赛的进行，先头部队已经通过了骑行检查点，而就在这时，比赛也迎来了一些变化！
[name="D.D.D."]在第一轮比赛中大显神威的鼠胆龙威队，在通过了骑行检查点并骑上了车后，立刻就遭到了其他队伍的重点照顾。
[name="D.D.D."]而且，这一次他们似乎改变了策略。
[name="D.D.D."]坎黛拉女士，能否请您为大家讲解一下！
[Character(name="avg_npc_198_1#2")]
[name="坎黛拉"]这不明摆着吗，这帮人知道自己就算一起上也未必是这支队伍的对手，于是选择拖住他们的脚步，而不是打败他们。
[name="坎黛拉"]跑步环节即使用这种方法也很容易被这两人近身，但是骑行阶段，在车上很多招式不好施展。
[name="坎黛拉"]所以他们选择在骑行环节这么做。
[character(name="avg_npc_198_1#4")]
[name="坎黛拉"]不得不说，效果不错。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]确实，他们紧紧跟在鼠胆龙威队附近，不上前进攻，只用各种手段进行骚扰，让鼠胆龙威队无法安心地赶路。
[name="D.D.D."]我们看到，鼠胆龙威队现在已经落后先头部队许多了！
[name="D.D.D."]骑在车上施展不开，而下车只会落后！鼠胆龙威队，面临着比赛开始以来最大的危机！
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg]
[Background(image="bg_20_G03")]
[delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[character(name="avg_npc_196_1#5")]
[name="林雨霞"]他们的目的不是打败我们，是拖住我们。
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]怎么办，两位，骑行中战斗是很困难的，这样下去我们要被完全拖住了。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]（小声）看来，有人想让我们抄近道。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]（小声）我知道。
[dialog]
[delay(time=1)]
[character(name="avg_1013_spchen_1#7",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]（小声）闯一闯？
[character(name="avg_1013_spchen_1#7",name2="avg_npc_196_1#7",focus=2)]
[name="林雨霞"]（小声）呵。
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[character(name="avg_NPC_017_3")]
[delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[name="D.D.D."]为了摆脱阻碍自己的其他队伍选手，鼠胆龙威队选择了插入巷道之中！
[name="D.D.D."]但是，正如我们在别的舞台所看到的，在巷道中，等待着我们的选手的，是这座城市的精锐部队！
[name="D.D.D."]虽然我也想为各位讲解其他队伍的视角，但是鼠胆龙威队实在是太吸引人注目了！
[name="D.D.D."]鼠胆龙威队此举究竟是自寻死路，还是险中求胜，让我们拭目以待！
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg]
[Background(image="bg_20_G02")]
[delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[character(name="avg_486_espumo_1#1",fadetime=0.3)]
[delay(time=0.51)]
[name="埃内斯托"]各位，走这边！这条巷子很隐秘，我估计没人......
[character(name="avg_npc_196_1#5")]
[name="林雨霞"]当心。
[dialog]
[character]
[CameraShake(duration=0.3, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=false)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[character(name="avg_486_espumo_1#1",name2="avg_npc_196_1#5")]
[PlaySound(key="$swordtsing1", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
在埃内斯托回头的一瞬间，一支弩箭从角落处向他激射而来，却被林雨霞用手刀截开。
[dialog]
[character]
[delay(time=1)]
[playsound(key="$rungeneral")]
[character(name="avg_npc_194",name2="avg_npc_195",fadetime=1)]
[delay(time=1.5)]
[character(name="avg_npc_194",name2="avg_npc_195",focus=1)]
[name="伏兵A"]......
[character(name="avg_npc_194",name2="avg_npc_195",focus=2)]
[name="伏兵B"]......
[character]
[dialog]
[delay(time=1)]
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]两位，这里交给我，你们快走！
[dialog]
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#1")]
埃内斯托说着将一把钥匙丢给陈。
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#1",focus=1)]
[name="埃内斯托"]（小声）这把钥匙你们拿着。
[name="埃内斯托"]（小声）那边有一家我开的武器店，你们过去应该就能看到。
[name="埃内斯托"]（小声）武器店的地下室有一扇后门，从后门出去有一个地下行道，走那边会快很多。
[name="埃内斯托"]（小声）我在这里拖住他们，你们先走。
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#1",focus=2)]
[name="陈"]......你一个人没问题？
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#1",focus=1)]
[name="埃内斯托"]只要有一个人到达终点就算胜利，两位，你们先走！
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]好。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]先突破这里。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Image]
```

### level_act12side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[character(name="avg_NPC_017_3")]
[Delay(time=1)]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="D.D.D."]怎么办，鼠胆龙威队遭到了官方设置的伏兵的围堵。
[name="D.D.D."]混战之中，埃内斯托小弟选择了殿后，而接过他钥匙的两位女侠则继续向前。
[name="D.D.D."]埃内斯托小弟虽然战斗力同样不俗，但是敌人如此众多，落败也只是时间问题！
[name="D.D.D."]而反观两位女侠这边，虽然突破了包围圈，但是前方依然有伏兵，她们真的能够顺利逃脱吗？
[name="D.D.D."]哦？她们打开了路边一家店的门然后冲了进去！
[name="D.D.D."]这家店......
[Character(name="avg_npc_198_1#1")]
[name="坎黛拉"]是埃内斯托开的店。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]原来如此，看来埃内斯托小弟丢给两位女侠的钥匙就是让她们躲入自己的店中。
[name="D.D.D."]但是，这样真的有效吗？
[name="D.D.D."]等等，导播，切一下镜头！
[name="D.D.D."]原来如此，从另一角度看过去就明白了，这家店是有后门的。
[name="D.D.D."]而我们可以看到，后门有一条直通大道的小路，而这条路还没有被其他阻拦者发现！
[name="D.D.D."]这会是鼠胆龙威队的机会吗，还是——
[dialog]
[character]
[musicvolume(volume=0,fadetime=0)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=2.5)]
D.D.D.的话音未落，屏幕中，埃内斯托的武器店就发出巨大的爆炸声。
[character(name="avg_NPC_017_3")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[musicvolume(volume=0.4,fadetime=1)]
[name="D.D.D."]这、这这这究竟是什么情况？
[name="D.D.D."]坎黛拉女士，这也是您设置的障碍吗？
[Character(name="avg_npc_198_1#2")]
[name="坎黛拉"]如果我要设置，那就不是只炸这一家店这么简单了。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]这......难道是其他队伍知道埃内斯托小弟有这样的后手而设下的陷阱？！
[name="D.D.D."]如果是这样，那鼠胆龙威队这一次可以说是被彻底算计了！
[name="D.D.D."]鼠胆龙威队，难道要折戟于此了吗！
[character]
[dialog]
[delay(time=1)]
[character(name="avg_npc_190_1#2",name2="avg_npc_203_1#1",focus=1)]
[name="艾雅法拉"]好过分......陈小姐和林小姐不会有事吧？
[character(name="avg_npc_190_1#2",name2="avg_npc_203_1#1",focus=2)]
[name="星熊"]放心，她们两个都是老江湖，这点爆炸死不了。
[character(name="avg_npc_190_1#2",name2="avg_npc_203_1#5",focus=2)]
[name="星熊"]只不过嘛......虽然这种比赛使绊子不奇怪，但这也有点太针对了。
[name="星熊"]老陈这是和谁结梁子了吗。
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg]
[Background(image="bg_20_G02")]
[delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[character(name="avg_npc_194")]
[name="伏兵A"]......啧，这家伙，怎么回事，根本打不着他。
[character(name="avg_437_mizuki_1#4")]
[name="水月"]咦......那边好像是陈姐姐她们去的方向。
[character(name="avg_437_mizuki_1#1")]
[name="水月"]还是过去看一看吧。
[dialog]
[playsound(key="$rungeneral")]
[character(fadetime=1)]
[delay(time=1.5)]
[dialog]
[stopmusic(fadetime=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_20_G08")]
[delay(time=1)]
[Blocker(a=0.3, r=0,g=0, b=0, fadetime=2, block=true)]
[character(name="char_empty",name2="avg_npc_196_1#5",fadetime=0.5,block=true)]
[name="林雨霞"]陈晖洁，你没死吧？
[dialog]
[character(name="avg_1013_spchen_1#7",name2="avg_npc_196_1#1",fadetime=0.5,block=true)]
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]咳，咳，死不了。
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6,crossfade=1)]
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]没死就好。你的车呢？
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]没了。
[name="陈"]你的呢？
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]好好的。
[name="林雨霞"]看来，对方也没想要置我们于死地。
[name="林雨霞"]只不过......
[name="林雨霞"]凑巧，出口被堵住了。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]好一个凑巧。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]你怎么看？
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]想办法出去，还能怎么看。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]我是问，谁干的。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]......我们的直觉看来没错。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]嗯。埃内斯托看起来绷不住了。
[name="林雨霞"]但是你不觉得有些奇怪吗？如果我是他，我不会这么做。
[name="林雨霞"]只有走投无路的人会用这种自爆式的方法。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]要么，确实不是他。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]不可能。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]要么，他想让我们以为他走投无路。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]......
林雨霞挑了挑眉毛，没有接话。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]对了，你把这件事告诉坎黛拉女士了吗？
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]当然。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]她怎么说？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[musicvolume(volume=0, fadetime=1)]
[Delay(time=2)]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-180)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[character]
[character(name="avg_npc_198_1#1",name2="avg_1013_spchen_1#1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[character(name="avg_npc_198_1#1",name2="avg_1013_spchen_1#4",focus=2)]
[name="陈"]您不会做任何事......吗。
[character(name="avg_npc_198_1#2",name2="avg_1013_spchen_1#4",focus=1)]
[name="坎黛拉"]没错，陈世侄，你是个聪明人，你应该想得到。
[name="坎黛拉"]现在我派人去排查炸弹的话，不是等于在告诉幕后黑手我发现了他的阴谋吗？
[character(name="avg_npc_198_1#2",name2="avg_1013_spchen_1#2",focus=2)]
[name="陈"]我明白。
[character(name="avg_npc_

... (全文9257字符)
```

### level_act12side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6,crossfade=1)]
[character(name="avg_NPC_017_3")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="D.D.D."]水月选手在放弃了阻拦伏兵后，来到将陈林两位选手掩埋的武器店废墟之上，停留了一会儿后便不知所踪。
[name="D.D.D."]我们所有的摄像头和无人机都没有找到他的位置。
[name="D.D.D."]而第一梯队中，甜蜜夏日队，已经最先抵达游泳检查点。
[dialog]
[delay(time=1)]
[name="D.D.D."]第一梯队的其他队伍也陆续穿过了游泳检查点。
[name="D.D.D."]而我们最关心的鼠胆龙威队中，埃内斯托小弟为了殿后已经被打倒，我们的工作人员判断他已经失去战斗能力了。
[name="D.D.D."]陈林两位女侠此时却依然没有动静。
[name="D.D.D."]难道真的万事休矣了吗？！
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_203_1#4")]
[name="星熊"]老陈，你不是吧，你不会倒在这种地方的对吧。
[character(name="avg_npc_190_1#2",name2="avg_npc_197_1#7",focus=1)]
[name="艾雅法拉"]星熊小姐对比赛很上心呢。
[character(name="avg_npc_190_1#2",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]哪里，她绝对是给陈押了大注，才在那念叨。
[name="诗怀雅"]认识这么久了，这种比赛的输赢，谁在乎啊。
[name="诗怀雅"]输了又不代表就怎么了，赢了也不能证明什么。
[character(name="avg_npc_190_1#2",name2="avg_npc_197_1#1",focus=2)]
[name="诗怀雅"]我倒是希望她输了，这样我才好嘲笑她。
[character(name="avg_npc_190_1#2",name2="avg_npc_197_1#7",focus=2)]
[name="诗怀雅"]哎，艾雅法拉，来，我来给你试试这款面霜，我觉得一定适合你。
[character(name="avg_npc_190_1#6",name2="avg_npc_197_1#7",focus=1)]
[name="艾雅法拉"]好的，谢谢。
[character]
[dialog]
[delay(time=1)]
[stopmusic]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=2.5)]
突然，又一声轰鸣，从停留在埃内斯托武器店的镜头屏幕中传来。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]等等，这难道是......
[dialog]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.2, block=true)]
[character]
[largebg]
[Background(image="bg_20_G02",fadetime=0.2)]
[delay(time=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=3, block=false)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#1",fadetime=1.5)]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.4)]
屏幕中，硝烟散去，而从硝烟中走出来的，正是推着自行车的陈和林雨霞。
[delay(time=4)]
[dialog]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720,fadetime=0.2)]
[character(name="avg_NPC_017_3",fadetime=0.2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="D.D.D."]来了来了，终于来了！
[name="D.D.D."]陈女侠与林女侠又一次地站上了比赛的舞台！
[name="D.D.D."]但是，两人只剩下一辆车，位置距离游泳检查点还有一小段距离，而此时第一梯队已经开始了游泳。
[name="D.D.D."]鼠胆龙威真的还有机会吗？！
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg]
[Background(image="bg_20_G03")]
[delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]你先走，我用跑的。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]上车。
[character(name="avg_1013_spchen_1#4",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]？
[character(name="avg_1013_spchen_1#4",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]别让我再说一次，上车。
[character(name="avg_1013_spchen_1#7",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]你确定？
[character(name="avg_1013_spchen_1#7",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]我来骑，你来解决碍事的家伙。
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[character(name="avg_NPC_017_3")]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[name="D.D.D."]太令人感动了，虽然只剩下一辆车，但是林女侠并没有抛弃陈女侠。
[name="D.D.D."]她让陈女侠站上自己的车后座，由她来骑车，而陈女侠负责对付那些想要妨碍她们的人。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="D.D.D."]两个人，一辆自行车，一次让所有人都目瞪口呆的完美配合！
[name="D.D.D."]现在我敢说，她们两个的组合，是这场大奖赛中最强大的！
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg]
[Background(image="bg_20_G03")]
[delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[character(name="avg_1013_spchen_1#7",name2="avg_npc_196_1#1",fadetime=0.5,block=true)]
[delay(time=1)]
[character(name="avg_1013_spchen_1#7",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]你压到我头发了。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]敌人在前面，我也没办法。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]你能不能不要乱扭？
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#6",focus=2)]
[name="林雨霞"]要不然你来骑？
[dialog]
[character(name="avg_1013_spchen_1#7",name2="avg_npc_196_1#4")]
[characteraction(name="left", type="jump", ypos=-20,xpos=100,power=10,times=1, fadetime=0.2, block=true)]
[characteraction(name="right", type="move", ypos=-40, fadetime=0.3, block=true)]
陈忽地压下林雨霞的头，躲开了迎面而来的一个轮胎。
[delay(time=0.6)]
[dialog]
[character(name="avg_1013_spchen_1#4",name2="avg_npc_196_1#5")]
[characteraction(name="right", type="move", ypos=50,xpos=-100, fadetime=0.2, block=true)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$fightgeneral", volume=1)]
[characteraction(name="left", type="move", ypos=10,xpos=-80, fadetime=1, block=true)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[Dialog]
[delay(time=0.51)]
林雨霞却猛地抬头，狠狠撞在陈的脸上

... (全文6911字符)
```

### level_act12side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[character(name="avg_NPC_017_3")]
[Delay(time=1)]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="D.D.D."]不愧是鼠胆龙威队的两位女侠，如果是战斗的话，她们就绝不会让人失望！
[name="D.D.D."]她们轻松地解决了围住她们的人。
[name="D.D.D."]但是，此时第一梯队已经游过了一半距离！
[name="D.D.D."]鼠胆龙威队，赶得上吗？！
[dialog]
[character]
[largebgtween(xFrom=-720,xTo=-180,  duration=1, ease="7", block=true)]
[delay(time=1)]
[playsound(key="$rungeneral")]
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",fadetime=1)]
[delay(time=1.5)]
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]你在看什么？该游泳了。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]我在想一个问题。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]什么问题？
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]既然我们认为埃内斯托有问题，而他又在我们后面，其实我们应该以他为优先。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]有一定道理。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]但我们依然不能确定他就有问题。
[name="陈"]而且，无论这背后是谁，很明显，对方都不希望我们赢得比赛。
[name="陈"]但赢得比赛这个目的太宽泛了。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]也就是说，对方不希望我们上船，我知道。
[character(name="avg_1013_spchen_1#7",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]别废话了，要输了。
[character(name="avg_1013_spchen_1#7",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]输？不可能。
[name="林雨霞"]你先去吧，好久没做类似的事了，我要做一些准备。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]......好。
[dialog]
[characteraction(name="left", type="move", xpos=-300, fadetime=2,block=false)]
[character(name="char_empty",name2="avg_npc_196_1#1",fadetime=0.5)]
[delay(time=2)]
[character]
[largebgtween(xFrom=-180,xTo=-720,  duration=1, ease="1", block=true)]
[delay(time=0.51)]
[character(name="avg_NPC_017_3")]
[name="D.D.D."]经过短暂的讨论后，不知为何，两位女侠中，陈女侠先行下水。
[name="D.D.D."]而林女侠则留在沙滩上，一边热身，一边似乎在从沙滩上收集沙子。
[name="D.D.D."]我们已经知道，林女侠的能力是将沙子变成玻璃作为武器，难道说，她要用沙子在海面上造出一座玻璃大桥？
[dialog]
[character]
[largebgtween(xFrom=-720,xTo=-180,  duration=1, ease="1", block=true)]
[delay(time=0.51)]
[character(name="avg_npc_196_1#1")]
[name="林雨霞"]要是爸爸的话，肯定能用这里的沙子直接变出一座桥来。
[name="林雨霞"]不过，我可做不到。
[name="林雨霞"]但是，我也有我的方法。
[name="林雨霞"]这么多沙子应该足够了。
[character(name="avg_npc_196_1#7")]
[name="林雨霞"]陈晖洁的位置......正好。
[character(name="avg_npc_196_1#5")]
[name="林雨霞"]呼......走！
[Dialog]
[delay(time=0.7)]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=1,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="avg_1013_spchen_1#4",name2="avg_npc_196_1#5")]
[characteraction(name="left", type="move", xpos=200,ypos=-150, fadetime=0.1,block=false)]
[characteraction(name="right", type="move", xpos=900,ypos=500, fadetime=0.3,block=false)]
[delay(time=0.51)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[characteraction(name="right", type="jump", xpos=-1100,power=50,times=1, fadetime=0.5,block=false)]
[delay(time=0.51)]
[playsound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="right", type="jump", xpos=-1100,power=50,times=1, fadetime=0.5,block=false)]
[characteraction(name="left", type="move", ypos=-200, fadetime=0.4,block=false)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character]
[character(name="avg_NPC_017_3")]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[delay(time=0.51)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[name="D.D.D."]这、这是......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="D.D.D."]林女侠居然真的在海面上“走”了起来！
[Character(name="avg_npc_198_1#5")]
[name="坎黛拉"]不，她并不是走，而是在跳跃。
[name="坎黛拉"]在她的每一个落脚点，都有她用沙子生成的玻璃作为支撑，供她进行下一次的跳跃。
[name="坎黛拉"]而且，她为了省沙子，如果就近有其他人，她就直接踩在那个人身上，用那个人的身体作为跳板。
[character(name="avg_npc_198_1#3")]
[name="坎黛拉"]哈哈哈，有意思，太有意思了！
[character(name="avg_NPC_017_3")]
[name="D.D.D."]原来如此。这真是前所未有的渡海方式！
[name="D.D.D."]也就是说，两人是商量好，因为近海缺少跳板，所以由陈女侠来充当她的第一块跳板，为林女侠的前进铺平道路。
[name="D.D.D."]两人再一次向我们展现了她们令人感动的队友情谊！
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#1",focus=1)]
[name="星熊"]哈哈哈，林小姐这法子确实出乎意料，但我觉得吧，她们一定没有商量好。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#1",focus=2)]
[name="诗怀雅"]确实，镜头里一闪而过的老陈那张臭脸太有趣了。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#1",focus=1)]
[name="星熊"]啧啧，没想到这两个人合作起来这么好玩。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_NPC_017_3")]
[name="D.D.D."]保持第一的依然是甜蜜夏日队，嘉文选手以势不可挡的劲头向着终点进发。
[name="D.D.D."]其他队伍也紧跟其后。
[name="D.D.D."]但是，他们都没有想到，在他们的身后，还有一个林女侠！
[name="D.D.D."]她直接越过了第三名！
[name="D.D.D."]第二名的头也只能成为她的跳板！
[name="D.D.D."]嘉文注意到她了，但是那又能怎么样呢！
[name="D.D.D."]嘉文，嘉文也被林女侠无情地越过头顶！
[name="D.D.D."]第一，第一名是林小姐，第一名，依然是鼠胆龙威队！！！！！
[name="D.D.D."]这真是一场让人热血沸腾的逆转！
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg]
[character(name="avg_486_espumo_1#3")]
[Background(image="bg_20_G02")]
[delay(time=1)]
[Blocker(a=0, 

... (全文6366字符)
```

### level_act12side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Character(name="avg_npc_200")]
[name="工作人员"]咦，节目的内部线路怎么接不上了？
[name="工作人员"]这是......被占用了？
[dialog]
[Character]
[stopmusic(fadetime=1)]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image(image="20_I00",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.4)]
[PlaySound(key="$d_gen_transmissionget",volume=1)]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[dialog]
[character]
[Delay(time=1)]
[CharacterCutin(widgetID="1", name="avg_npc_192_1#6", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, width=200, block=true)]
[name="潘乔"]十年前，我相信只要把联合政府和辛嘉斯王朝都赶出去，玻利瓦尔就会获得和平。
[name="潘乔"]我为了真正玻利瓦尔人打生打死。
[name="潘乔"]最后，我三千个弟兄被我带去送死，如果不是我的老哥哥豁出性命，我那天就被枪决了。
[name="潘乔"]从那天起，我就明白了。
[name="潘乔"]联合政府，辛嘉斯王朝的贵族们，真正玻利瓦尔人，这三个没有一个真的想要拯救玻利瓦尔，他们只是在打仗。
[name="潘乔"]他们再打多少年，玻利瓦尔也不会有救。
[name="潘乔"]为了避难，我逃到了这座城市。
[name="潘乔"]然后，我发现，在这个已经没救的国家里，还有这样一座没救的城市。
[name="潘乔"]坎黛拉·桑切斯，比他们所有人都更加不可救药。
[name="潘乔"]她在这片没救的土地上建立了这座比所有玻利瓦尔城市加起来都要腐败的城市。
[name="潘乔"]她不仅自己享受其中，还将其他人也拉到自己身边和她一起享受。
[name="潘乔"]所有人都被她卷了进来，过着自以为体面的日子。
[name="潘乔"]他们根本不知道这座城市的下水道里流淌着多少恶臭的人血，饲养了多少的食腐饿兽。
[name="潘乔"]她吸食着生活在这片土地上的人民的血肉，而丝毫不关心他们的死活。
[name="潘乔"]这座城市他妈的该死，在这里享乐的你们也他妈的该死！！！
[name="潘乔"]大奖赛结束了。
[name="潘乔"]接下来，我会夺取这座城市。
[name="潘乔"]没人拯救这个国家，我来。
[CharacterCutin(widgetID="1",block=true)]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image]
[character]
[largebg]
[Character(name="avg_1013_spchen_1",name2="avg_486_espumo_1")]
[Delay(time=1)]
[Background(image="bg_20_G06",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_1013_spchen_1",name2="avg_486_espumo_1",focus=1)]
[name="陈"]......
[name="陈"]所以你的父亲才是这一切的主谋。
[name="陈"]当你发现我们有可能察觉到什么的时候，你选择将我们的注意力转移到你的身上。
[name="陈"]这样，即使我们真的发现了什么，你也为你背后的人争取了时间。
[Character(name="avg_1013_spchen_1",name2="avg_486_espumo_1",focus=2)]
[name="埃内斯托"]是的。我不想说我赢了，陈小姐，这本来就不是一场公平的较量。
[name="埃内斯托"]你们来得太晚，接受坎黛拉女士的委托又太匆忙。
[name="埃内斯托"]这是我最后的善意，陈小姐，和林小姐投降吧。
[name="埃内斯托"]两位要是愿意收手，我保证没有人会伤到你们。
[name="埃内斯托"]这里的事和你们无关，你们没有必要参与到这样一场没有对错可言的事情中。
[Character(name="avg_1013_spchen_1#2",name2="avg_486_espumo_1",focus=1)]
[name="陈"]我做不到。
[Character(name="avg_1013_spchen_1#2",name2="avg_486_espumo_1",focus=2)]
[name="埃内斯托"]这艘船已经被我们的人占领了，反抗的话，你和林小姐会死的。
[Character(name="avg_1013_spchen_1",name2="avg_486_espumo_1",focus=1)]
[name="陈"]有个老朋友说过，只有被狠狠捶打过一遍，我才会像过去的她一样，知道自己那些可笑的执着都不过是些冲动。
[name="陈"]我到现在也还没有分清，哪些是可以坚持的执着，哪些是不切实际的冲动。
[name="陈"]但我想她应该也是知道的，如果因此我就不去做的话，我也就不叫陈晖洁了。
[name="陈"]动手吧，我赶时间。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Delay(time=1)]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.4)]
[Character(name="avg_npc_201")]
[name="震惊的男游客"]喂，这不是潘乔先生吗？他在说什么？
[Character(name="avg_npc_202")]
[name="震惊的女游客"]不知道，是什么特别演出吗？
[dialog]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[character]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_gen_explo_n")]
[Delay(time=1.5)]
[Character(name="avg_npc_201")]
[name="害怕的男游客"]哪里来的爆炸声？！
[Character(name="avg_npc_202")]
[name="害怕的女游客"]好像是第一轮的城区那边！你看，那边冒烟了！
[Character(name="avg_npc_201")]
[name="害怕的男游客"]喂喂喂，不是吧，难道潘乔这个老头是来真的？！
[dialog]
[character]
[Delay(time=1)]
[Character(name="avg_npc_198_1#1",name2="avg_npc_207",focus=2)]
[name="护卫"]坎黛拉女士，城内和郊区出现了多股不明势力正在引发混乱。
[Character(name="avg_npc_198_1#2",name2="avg_npc_207",focus=1)]
[name="坎黛拉"]......啧啧，来这招啊，我的老潘乔。
[Character(name="avg_npc_198_1#2",name2="avg_npc_207",focus=2)]
[name="护卫"]坎黛拉女士，请前往安全的地方避难。
[Character(name="avg_npc_198_1#4",name2="avg_npc_207",focus=1)]
[name="坎黛拉"]避难？说什么呢，这里可是头等座，我哪里都不会去。
[name="坎黛拉"]城里那些突然冒出来的家伙随便应付一下就好了，反正他们的目的最后都会是我。
[Character(name="avg_npc_198_1#1",name2="avg_npc_207",focus=1)]
[name="坎黛拉"]啊，疏散群众还是要做的，不过，城门先封闭了，让他们都回到自己的住所去。
[name="坎黛拉"]然后嘛，把工作人员保护起来。
[name="坎黛拉"]但是。
[name="坎黛拉"]让他们筹备宴会，还有继续进行大奖赛的转播。
[Character(name="avg_npc_198_1#4",name2="avg_npc_207",focus=1)]
[name="坎黛拉"]保护好他们，别让我的大奖赛被破坏了，明白了吗？
[Character(name="avg_npc_198_1#4",name2="avg_npc_207",focus=2)]
[name="护卫"]好的。
[Character(name="avg_npc_198_1#3",name2="avg_npc_207",focus=1)]
[name="坎黛拉"]对了对了，去调一批新的无人机来，船上的那些估计被他们破坏了，这么有趣的事情，怎么能错过呢？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[delay(time=1)]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-180)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_203_1#4",name2="avg_npc_197_1#4",fadetime=0.5)]
[delay(time=1)]
[Character(name="avg_npc_203_1#4",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]喂，不是吧，我们只是来度个假，还能遇到这种事？
[Character(name="avg_npc_203_1#2",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]虽然应该说，这才有玻利瓦尔的感觉。
[Character(name="avg_npc_203_1#2",name2="avg_npc_197_1#4",focus=2)]
[name="诗怀雅"]别贫了，快想想怎么办。
[Character(name="avg_npc_203_1#5",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]Missy，我们现在只是游客，管不了也不该管这么多。
[Character(name="avg_npc_203_1#5",name2="avg_npc_197_1#6",focus=2)]
[name="诗怀雅"]要是陈晖洁站在这里，你会这么对她说吗？
[Character(name="avg_npc_203_1#5",name2="avg_npc_197_1#6",focus=1)]
[name="星熊"]会啊，只是你也知道她的答案。
[Character(name="avg_npc_203_

... (全文11006字符)
```

### level_act12side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[dialog]
[stopmusic]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image(image="20_I00",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.4)]
[PlaySound(key="$d_gen_transmissionget",volume=1)]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[dialog]
[character]
[Delay(time=1)]
[CharacterCutin(widgetID="1", name="avg_npc_198_1#4", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, width=200, block=true)]
[name="坎黛拉"]咳咳，听得到吗，听得到吗？
[name="坎黛拉"]亲爱的市民朋友们，还有游客朋友们，是我，坎黛拉。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[image]
[character(name="avg_npc_198_1#4")]
[CharacterCutin(widgetID="1",fadetime=0)]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[Delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[name="坎黛拉"]首先，不用太紧张。
[character(name="avg_npc_198_1#2")]
[name="坎黛拉"]不得不说，老潘乔这一出完全在我的预想之外。
[character(name="avg_npc_198_1#3")]
[name="坎黛拉"]我怎么想得到我信任的手下居然一直密谋着夺取我的城市这么可怕的事呢，这太可怕了！
[character(name="avg_npc_198_1#1")]
[name="坎黛拉"]但是，正如我一开始所说的，这并不是什么值得惊慌的事。
[character(name="avg_npc_198_1#5")]
[name="坎黛拉"]不如说，我要感谢老潘乔才行。
[character(name="avg_npc_198_1#1")]
[name="坎黛拉"]老实说，这两年，我也一直在思考，怎样才能让大奖赛变得更加刺激，更加引人注目，更加能让人从中获得快乐。
[name="坎黛拉"]而我一直没有找到特别好的方法。
[character(name="avg_npc_198_1#3")]
[name="坎黛拉"]而老潘乔为我找到了，他用自己的行动向我展示了一场更加刺激的大奖赛！
[character(name="avg_npc_198_1#1")]
[name="坎黛拉"]大奖赛结束了？
[character(name="avg_npc_198_1#3")]
[name="坎黛拉"]不，恰恰相反。就在刚刚那一刻，本次大奖赛进入了真正的高潮！
[name="坎黛拉"]所有队伍在此时都将复活，竞猜环节将会重新启动。
[name="坎黛拉"]尽可能地去阻止那些在城里闹事的家伙们，我知道你们有这个本事。
[name="坎黛拉"]事情结束后，我会给你们应有的奖赏。
[dialog]
[character]
[delay(time=1)]
[Character(name="avg_npc_197_1#7")]
[name="诗怀雅"]......
[Character(name="avg_npc_203_1#2")]
[name="星熊"]......
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_198_1#4",fadetime=1.5)]
[delay(time=2)]
[name="坎黛拉"]啊，就是你们两个吧，我的手下们说，你们在刚才帮他们挡住了一波针对我的刺杀。
[name="坎黛拉"]来吧，请坐，作为对你们的褒奖，你们也在这特等座和我一起享受这场比赛吧。
[Character(name="avg_npc_197_1#4")]
[name="诗怀雅"]您......是认真的？
[Character(name="avg_npc_198_1#4")]
[name="坎黛拉"]我当然是认真的。
[name="坎黛拉"]老潘乔知道，在我面前掀桌子的话，他的赢面很小。
[name="坎黛拉"]所以他缩在了这艘我交给他保管的船上。
[name="坎黛拉"]要是我没猜错的话，他应该私底下给这艘船加了不少东西，大炮之类的？
[Character(name="avg_npc_203_1#5")]
[name="星熊"]但是，如果只是这样的话，其实没有那么有威胁吧？
[Character(name="avg_npc_198_1#4")]
[name="坎黛拉"]没错。
[name="坎黛拉"]第二轮比赛和第三轮比赛期间，会邀请许多来自各方的权贵上船，让他们能够用自己的双眼体会比赛的乐趣。
[Character(name="avg_npc_197_1#6")]
[name="诗怀雅"]我懂了，这些权贵的性命才是关键。
[name="诗怀雅"]因为这座城市的运转需要和这些人打交道。
[Character(name="avg_npc_198_1#5")]
[name="坎黛拉"]对对对，现在就不是我想不想解决他的问题，而是那些老爷的手下们希不希望我立刻解决他的问题。
[Character(name="avg_npc_198_1#2")]
[name="坎黛拉"]啧啧，阵仗搞得这么大，结果还是来阴的嘛。
[name="坎黛拉"]多半是埃内斯托那小子教他的。
[Character(name="avg_npc_198_1#4")]
[name="坎黛拉"]反正如你们所见，现在我能做的事情并不多，但是，实际上他能做的事情也不多。
[name="坎黛拉"]那么，为什么不把事情变得更加有趣一点呢？
[Character(name="avg_npc_197_1#6")]
[name="诗怀雅"]但是这不是会更加刺激他......
[Character(name="avg_npc_198_1#1")]
[name="坎黛拉"]他要是真的敢把那些老爷拉出来挨个毙了，我就算把这座城市让给他又怎么样？
[Character(name="avg_npc_203_1#6",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]你不明白，Missy，他既然想要夺取这座城市去打仗，那终究也是要仰仗那些老爷的。
[name="星熊"]不然他打仗的钱和士兵哪里来？
[name="星熊"]真要我说，船上那些老爷里，恐怕早有几个和他已经谈好的了。
[Character(name="avg_npc_203_1#6",name2="avg_npc_197_1#2",focus=2)]
[name="诗怀雅"]......
[Character(name="avg_npc_198_1#5")]
[name="坎黛拉"]哦？你们两个年轻人很有意思啊，看打扮，不是玻利瓦尔人？
[Character(name="avg_npc_203_1#1")]
[name="星熊"]哈哈，我们来自龙门，现在还有两个朋友在船上。
[Character(name="avg_npc_198_1#1")]
[name="坎黛拉"]嗯？你们两个竟然是陈世侄和林世侄的朋友？怎么没有听她们提起过。
[Character(name="avg_npc_203_1#1")]
[name="星熊"]我们没有告诉她们，是偷偷来玩的，您不知道自然也正常。
[Character(name="avg_npc_198_1#3")]
[name="坎黛拉"]哈哈哈，原来如此。
[Character(name="avg_npc_198_1#5")]
[name="坎黛拉"]既然如此，我可以多告诉你们一点——
[name="坎黛拉"]我将这件事委托给了陈世侄与林世侄，而另一方面，我答应了文月夫人，她们两人在这里不会受到任何危险。
[name="坎黛拉"]你们知道这意味着什么吗？
[Character(name="avg_npc_203_1#1")]
[name="星熊"]意味着还不到时候。
[Character(name="avg_npc_198_1#3")]
[name="坎黛拉"]你很懂啊，东国的姑娘。
[name="坎黛拉"]如果两位世侄真的有什么闪失，那船上的那些老爷们，可就要给可怜的老潘乔陪葬了。
[Character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=2)]
[name="诗怀雅"]......
[Character(name="avg_npc_203_1#1",name2="avg_npc_197_1#4",focus=1)]
[name="星熊"]Missy，别怕。
[Character(name="avg_npc_198_1#3")]
[name="坎黛拉"]来来来，正所谓不打不相识，来，坐，我们好好聊聊。
[dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[largebg]
[delay(time=1)]
[Background(image="bg_20_G06",screenadapt="coverall")]
[Character(name="char_empty",name2="avg_npc_196_1#5")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[delay(time=1.5)]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[CharacterCutin(widgetID="1", name="avg_1013_spchen_1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=-300, width=200, block=true)]
[Character(name="char_empty",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]解决了？
[Character(name="char_empty",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]解决了。
[name="陈"]但是情况确实不妙。
[Character(name="char_empty",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]看来，你去对付埃内斯托，我来调查的分工还是太晚了。
[Character(name="char_empty",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]......没错。
[Character(name="char_empty",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]不甘心？
[Character(name="char_empty",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]不甘心......但也没办法。
[Character(name="char_empty",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]这件事没那么简单，早有预感的不是吗。
[Character(name="char_empty",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]我没想到会闹这么大。
[Character(name="char_empty",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]你怕了？
[Character(name="char_empty",name2="avg_npc_196_1#5",focus=1)]
[name="陈"]怎么可能。
[name="陈"]你现在在哪？
[Character(name="char_empty",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]某个船舱里。
[name="林雨霞"]在你和埃内斯托聊天的时候，我到处走了走，虽然在潘乔开始

... (全文11989字符)
```

### level_act12side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_20_G06",screenadapt="coverall")]
[character(name="avg_1013_spchen_1#1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[name="陈"]怎么样？
[character(name="avg_1013_spchen_1#1",focus=-1)]
[name="林雨霞"]进展顺利，我快摸到餐厅了。
[character(name="avg_1013_spchen_1#1")]
[name="陈"]好。
[dialog]
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="陈"]？！
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_486_espumo_1#1")]
[delay(time=1.5)]
[character(name="avg_486_espumo_1#3")]
[name="埃内斯托"]又见面了，陈小姐。
[character(name="avg_1013_spchen_1#1")]
[name="陈"]......你该好好躺在那。
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]我也想这么做，最好我睁眼之后，无论胜败，这件事都结束了。
[character(name="avg_486_espumo_1#4")]
[name="埃内斯托"]可惜，我不能这么做。
[character(name="avg_1013_spchen_1#1")]
[name="陈"]你打不过我的。
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]我现在越来越庆幸自己一开始将你们当做最大的敌人来对待了......如果我没有这么做，计划可能无法走到这一步。
[character(name="avg_1013_spchen_1#1")]
[name="陈"]你......不像是那种狂热分子，为什么一定要做这样的事？
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]事到如今，让我说说我真实的想法吧。
[character(name="avg_486_espumo_1#7")]
[name="埃内斯托"]坎黛拉女士曾经说过，她的父亲，这座城市的前市长，一个被莱塔尼亚政府扶持，除了贪污什么都不会做的废物。
[name="埃内斯托"]在被愤怒的市民们踢开办公室的门前，带着妻子和女儿逃离了这个国家。
[name="埃内斯托"]她的父亲虽然作为人是个彻头彻尾的垃圾，但是作为这个人渣的女儿，她跟着父亲先去了卡西米尔，然后去了维多利亚。
[name="埃内斯托"]跟着父亲，她知道了金钱的用法，更知道了钱的意义。
[name="埃内斯托"]然后她回到了这座城市，并成为了这里的市长。
[character(name="avg_486_espumo_1#4")]
[name="埃内斯托"]在反抗军一事无成的时候，这座城市已经能够生产出全玻利瓦尔最好的酒、咖啡，还有糖。
[name="埃内斯托"]多索雷斯的龙舌兰，在莱塔尼亚和哥伦比亚都能喝到。
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]在莱塔尼亚和哥伦比亚勾心斗角的时候，这座城市成为了两边的贵族都会选择的度假胜地。
[name="埃内斯托"]他们甚至还要遵循坎黛拉女士的规则，不能在这里动手。
[name="埃内斯托"]而让他们甘愿这么做的，不是武力，不是刀剑法术，是金钱、娱乐和奢侈品。
[character(name="avg_486_espumo_1#7")]
[name="埃内斯托"]是这座城市光鲜的外皮。
[delay(time=1)]
[character(name="avg_486_espumo_1#2")]
[name="埃内斯托"]我知道我不该这么想。
[name="埃内斯托"]但我无法阻止自己去这么想——
[character(name="avg_486_espumo_1#4")]
[name="埃内斯托"]在某种意义上来讲，从结果上来说，是不是坎黛拉女士比我父亲要更热爱玻利瓦尔这个国家？
[character(name="avg_486_espumo_1#7")]
[name="埃内斯托"]他只是在盲目地追求着国家这个意象，他想要一个名叫玻利瓦尔的国家。
[name="埃内斯托"]它的领土是它作为附属地时被决定的大小，它的人民是一直以来生活在这里的人民。
[name="埃内斯托"]然后呢？这个国家如何面对哥伦比亚和莱塔尼亚的倾轧？这个国家如何作为一个国家发展下去？
[name="埃内斯托"]他不知道。他其实不知道玻利瓦尔会是一个怎样的国家。
[name="埃内斯托"]而坎黛拉女士至少找到了一条路，她看到了它存在的意义，并打算让这种意义成为现实。
[character(name="avg_1013_spchen_1#1")]
[name="陈"]......歪理邪说。
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]好过空口白话，不是吗？
[character(name="avg_1013_spchen_1#1")]
[name="陈"]既然如此为什么你还要协助你的父亲？
[character(name="avg_486_espumo_1#7")]
[name="埃内斯托"]因为我自出生起就看着我父亲在战火里打滚，看着他从意气风发逐渐变得沉默寡言。
[character(name="avg_486_espumo_1#6")]
[name="埃内斯托"]我知道我的父亲是个怎样的人，他和那些已经选择了屈服于时代的人不一样。
[name="埃内斯托"]即使在坎黛拉女士手下做事让我产生了一些念头，也不意味着我就要背叛我的父亲。
[character(name="avg_486_espumo_1#4")]
[name="埃内斯托"]但我也无法否认，这些念头越来越强烈，以至于让我逐渐开始思考一些别的可能性。
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]所以我将这次计划作为一个分界点。
[name="埃内斯托"]我会全心全意协助父亲，如果他成功了，那我就协助他。
[name="埃内斯托"]如果他失败了，那我也将接受自己的改变，成为坎黛拉女士的拥趸。
[character(name="avg_486_espumo_1#7")]
[name="埃内斯托"]当然，如果我死了——
[delay(time=1)]
[character(name="avg_486_espumo_1#5")]
[name="埃内斯托"]那就是死了，哈哈。
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]而现在，还不到结束的时候。
[name="埃内斯托"]所以，我不会让你过去的。
[character(name="avg_1013_spchen_1#1")]
[name="陈"]......既然如此，那就没什么好说的了。
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]是的，认识你很高兴，陈小姐。
[name="埃内斯托"]如果不是在这种情况下认识，我还挺想好好带着你和林小姐认识一下这座城市的。
[character(name="avg_1013_spchen_1#1")]
[name="陈"]免了。
[character(name="avg_486_espumo_1#5")]
[name="埃内斯托"]我想也是。
[dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[image]
[Background(image="bg_20_G01",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.4)]
[Character(name="avg_npc_020")]
[name="船长护卫"]B队，来几个人，跟我走。
[Character(name="avg_npc_193",name2="avg_npc_193",focus=1)]
[name="迟钝的潘乔手下"]怎么了？
[Character(name="avg_npc_193",name2="avg_npc_193",focus=2)]
[name="机灵的潘乔手下"]好像是比赛里那个特别能打的鼠胆龙威队，里面那个姓陈的女侠好像还在反抗。
[Character(name="avg_npc_193",name2="avg_npc_193",focus=1)]
[name="迟钝的潘乔手下"]船上都是我们的人，其他不是的参赛选手也都在这了，她怎么反抗？
[Character(name="avg_npc_193",name2="avg_npc_193",focus=2)]
[name="机灵的潘乔手下"]她好像把埃内斯托给放倒了。
[name="机灵的潘乔手下"]然后在船上上蹿下跳的，船长都已经亲自去抓她了。
[name="机灵的潘乔手下"]啧啧，真是厉害。之前埃内斯托说不能小看她们，我还不信。
[Character(name="avg_npc_193",name2="avg_npc_193",focus=1)]
[name="迟钝的潘乔手下"]嗯？这么一说，那个姓林的女侠呢？
[name="迟钝的潘乔手下"]我好像也没在这些人质里看到。
[Character(name="avg_npc_193",name2="avg_npc_193",focus=2)]
[name="机灵的潘乔手下"]谁知道，跳海跑了吧。
[dialog]
[character]
[delay(time=1)]
[name="林雨霞"]我在这。
[dialog]
[delay(time=1)]
[Character(name="avg_npc_193")]
[name="迟钝的潘乔手下"]？！
[dialog]
[character]
[stopmusic(fadetime=1)]
[Dialog]
[Character(name="char_empty")]
[characteraction(name="middle", type="move", ypos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", ypos=-200, fadetime=0.5, block=false)]
[PlaySound(key="$fan", volume=1)]
[Character(name="avg_npc_196_1",fadetime=0.7)]
[delay(time=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.6, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[dialog]
[character]
[Character(name="avg_npc_193",name2="avg_npc_193",focus=1)]
[Dialog]
[delay(time=0.7)]
[Pl

... (全文18067字符)
```

### level_act12side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[playMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.4)]
[Background(image="bg_20_G09")]
[character(name="avg_npc_198_1",name2="avg_npc_203_1#5")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_198_1",name2="avg_npc_203_1#5",focus=2)]
[name="星熊"]喂，快看，那边被追赶的是老陈和林小姐吧？
[character(name="avg_npc_198_1",name2="avg_npc_203_1#5",focus=1)]
[name="坎黛拉"]啊，两位世侄，了不起，真是了不起......
[character(name="avg_npc_198_1",name2="avg_npc_203_1#5",focus=2)]
[name="星熊"]我们快去救......
[dialog]
[musicvolume(volume=0,fadetime=0)]
[CameraShake(duration=3, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[delay(time=1)]
忽然，已经驶到距离海岸不远处的游轮上发出了巨大的爆炸声。
[dialog]
[Character]
[Image(image="20_I06",xScale=1.05,yScale=1.05, fadetime=0)]
[CameraShake(duration=-1, xstrength=3, ystrength=5, vibrato=2, randomness=100, fadeout=false, block=false)]
[musicvolume(volume=0.2,fadetime=2)]
[Blocker(a=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="陈"]你搞了什么东西？
[name="林雨霞"]一点惊喜。
[name="林雨霞"]我不是问你，救完人之后干什么吗？
[name="林雨霞"]虽然我也同意直接走人，但是我想起我身上还有炸弹。
[name="林雨霞"]于是就给他们多留了一点惊喜。
[name="陈"]......
[name="林雨霞"]喝一杯？
[name="陈"]你还真是有雅兴。
[name="林雨霞"]开出来的时候才看到，就稍微摆了一下。
[name="陈"]无聊。
[name="林雨霞"]无趣。
[name="陈"]......
[name="林雨霞"]......
[name="陈"]我不知道你是不是故意的。
[name="林雨霞"]什么？
[name="陈"]你忘了？“而当你接过他们的班时，你不能只走他们的老路。”
[name="陈"]你说这段话的时候，我们的通讯还没有断开。
[name="林雨霞"]......
[name="陈"]所以，你老实告诉我，那件事里，你没有做我所想的那些事，对吗？
[dialog]
[delay(time=1)]
[name="林雨霞"]......到岸了。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[CameraShake(duration=0.01, ystrength=10, vibrato=10, randomness=10, fadeout=true, block=false)]
[Character]
[Image]
[delay(time=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[delay(time=1.5)]
[character(name="avg_npc_196_1#6",fadetime=0.2)]
[delay(time=0.51)]
[name="林雨霞"]你输了，老头。
[character(name="avg_npc_192_1#8")]
[name="潘乔"]......
[name="潘乔"]帮助坎黛拉那个女人，小姑娘，你们不理解自己做了什么。
[character(name="avg_npc_198_1#5")]
[name="坎黛拉"]你做得好啊，老潘乔。
[character(name="avg_npc_193")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="船长手下"]坎黛拉！
[character(name="avg_npc_192_1#8")]
[name="潘乔"]住手。我们已经输了。
[character(name="avg_npc_198_1#5")]
[name="坎黛拉"]明智的选择，老潘乔。
[name="坎黛拉"]来，坐。
[character(name="avg_npc_192_1#8")]
[name="潘乔"]坎黛拉，你想干什么？
[character(name="avg_npc_198_1#3")]
[name="坎黛拉"]看不懂吗？请你吃饭。
[Dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#3",fadetime=0.3)]
[delay(time=0.51)]
潘乔冷哼一声，却还是坐在了坎黛拉的对面。
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#5",focus=2)]
[name="坎黛拉"]别的人在这个时候恐怕已经吓破胆了，我就是看中你这一点，老潘乔。
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#5",focus=1)]
[name="潘乔"]当不起。
[name="潘乔"]我已经输了，你没有把我抓起来，还请我坐在这里，你究竟想干什么？羞辱我？
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#2",focus=2)]
[name="坎黛拉"]聊一聊，老潘乔。
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#1",focus=2)]
[name="坎黛拉"]用埃内斯托来分散我的注意力，让手下参加比赛，通过比赛在城市各处埋好炸弹。
[name="坎黛拉"]最后在第三轮前夕发难，挟持船上的富豪和权贵让我不能轻举妄动。
[name="坎黛拉"]我不得不说，这一次，可能是我最接近失去这座城市的一次了。
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#1",focus=1)]
[name="潘乔"]*玻利瓦尔俚语*，我真是不明白，坎黛拉，为了这一次的计划，我和我的手下准备了多少个日日夜夜。
[name="潘乔"]而你，你只是恰好请了两个什么都不知道的外地人，恰好把这件事交给她们。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#1",focus=1)]
[name="潘乔"]而她们，她们居然就正好破坏了我的计划！！！
[name="潘乔"]为什么赢的是你这样的人？
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#1",focus=2)]
[name="坎黛拉"]我赢了？
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#2",focus=2)]
[name="坎黛拉"]你在说什么，潘乔，我的老潘乔，看来你在我的城市里呆了太久，连我是什么人都忘了。
[name="坎黛拉"]或者说，你从未了解过我。
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#5",focus=2)]
[name="坎黛拉"]你的对手从来都不是我，你也没有输给我。
[name="坎黛拉"]你只是失败了，就这么简单。
[name="坎黛拉"]在最厌恶的城市中生活了十数年，说着痛恨三方政府的话，却为了推翻我而不得不接受其中一家的资助。
[name="坎黛拉"]让我猜猜，是莱塔尼亚的某一位吧，啊，我甚至能大概想到是哪一位。
[name="坎黛拉"]告诉我，老潘乔，你是怎么想的，居然向那些吃人不吐骨头的家伙寻求帮助。
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#5",focus=1)]
[name="潘乔"]......
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#2",focus=2)]
[name="坎黛拉"]啊，意思是，你学会了忍辱负重。
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#5",focus=2)]
[name="坎黛拉"]那你为什么不向我摇尾乞怜呢？
[name="坎黛拉"]你怎么知道我不会帮助你？
[name="坎黛拉"]说真的，老潘乔，要是你来求我，我说不定真的会给你人和钱去打你最爱的战争。
[name="坎黛拉"]如果你最后赢了，那这座城市也会投靠你。
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#4",focus=2)]
[name="坎黛拉"]我觉得不会有比这更有吸引力的方案了。
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#4",focus=1)]
[name="潘乔"]我这辈子都不可能向你低头。
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#2",focus=2)]
[name="坎黛拉"]唉，你这种人啊，就是在这方面太顽固了。
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#4",focus=2)]
[name="坎黛拉"]你们这样的人，对于完整，独立这样的词汇总是有着一种不切实际的期待。
[name="坎黛拉"]你们妄想着有一种气节会将你们联系起来，你们追寻着一种象征能够让你们团结其下。
[name="坎黛拉"]而事实上，玻利瓦尔从一开始就没有独立过，既然没有历史，又谈何气节，谈何象征？
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#3",focus=2)]
[name="坎黛拉"]如果你成功了，你所建立的玻利瓦尔真的是你想象中的玻利瓦尔吗？我看不见得。
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#3",focus=1)]
[name="潘乔"]不管你怎么说，我所想的从一开始就只是终结战争，让玻利瓦尔和平。
[name="潘乔"]今天我失败了，我认栽，坎黛拉。
[name="潘乔"]但是你记住，我的事业或许不是正义的，但我至少要比你正义！
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#2",focus=2)]
[name="坎黛拉"]啊，对不起，瞧我，又把你和你背后的人混为一谈了。
[character(name="avg_npc_192_1#8",name2="avg_npc_198_1#1",focus=2)]
[name="坎黛拉"]你不是我所描述的那类人，你发自内心地想要拯救这个国家，所以你能够坐在这里。


... (全文10062字符)
```

### level_act12side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[Delay(time=1)]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_200")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="海选主持人"]这可真是太惊人了！没想到在万众瞩目的混战海选中，居然发生了这样的事！
[name="海选主持人"]半路杀出来的两人成为了本场海选的最后赢家！
[name="海选主持人"]我想请问一下潘乔先生，这样的情况是可以被接受的吗？！
[character(name="avg_npc_192_1#2")]
[name="潘乔"]咳咳，这种情况确实比较少见。原则上，我们希望各位参赛者能够遵守比赛规则。
[character(name="avg_npc_200")]
[name="海选主持人"]那么很遗憾......
[character(name="avg_npc_192_1#2")]
[name="潘乔"]但是。
[dialog]
[delay(time=0.6)]
[character(name="avg_npc_192_1#7")]
[name="潘乔"]偶尔发生这样的事也不坏。
[character(name="avg_npc_200")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="海选主持人"]噢噢，没错！咳咳，那么很遗憾，这对其他参赛选手来说恐怕会是一个噩耗。
[dialog]
[character]
[CameraShake(duration=2, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$livecrowd")]
[delay(time=2)]
[character(name="char_010_chen_summer",name2="avg_npc_196_1#1",fadetime=0.6)]
[delay(time=1)]
[character(name="char_010_chen_summer",name2="avg_npc_196_1#7",focus=2)]
[name="林雨霞"]呵，这主持人还挺会临机应变的，他刚才是想说我们出局了。
[character(name="char_010_chen_summer",name2="avg_npc_196_1#7",focus=1)]
[name="陈"]或许吧。
[name="陈"]看来我们误入了比赛的赛场。
[name="陈"]没记错的话，应该是叫大乱斗海选赛。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_200")]
[name="海选主持人"]但是，各位，这场大赛的主旨就是为全市人民带来欢乐。
[name="海选主持人"]而这两位虽然没有办理过参赛手续，却凭借着矫健的身手和绝妙的配合在混乱的赛场上存活到了最后！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="海选主持人"]这难道不正是最绝妙的发展吗！这难道不值得我们为她们送上我们最热烈的欢呼声吗？！
[dialog]
[character]
[CameraShake(duration=2, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$livecrowd")]
[delay(time=2)]
[character(name="char_010_chen_summer",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]他说我们有绝妙的配合，有吗？
[character(name="char_010_chen_summer",name2="avg_npc_196_1#1",focus=1)]
[name="陈"]最好没有。
[name="陈"]唉......为什么会变成这样。
[Dialog]
[delay(time=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=3, block=true)]
[character]
[largebg]
[Background]
[delay(time=0.51)]
[PlaySound(key="$flashback")]
[Background(image="bg_20_G01")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$flashback")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Background(image="bg_20_G02")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$flashback")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Background(image="bg_20_G03")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$livecrowd")]
[Image(image="20_I01",xScale=1.8,yScale=1.8, fadetime=0)]
[ImageTween(yFrom=100, yTo=-100, duration=10, block=false)]
[delay(time=1)]
[image]
[PlaySound(key="$flashback")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-180)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$flashback")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[largebg]
[Background(image="bg_20_G06")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$flashback")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Background(image="bg_20_G07")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$livecrowd")]
[Image(image="20_I03",xScale=1.5,yScale=1.5, fadetime=0)]
[ImageTween(xFrom=-100, xTo=100, duration=10, block=false)]
[delay(time=1)]
[image]
[PlaySound(key="$flashback")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Background(image="bg_20_G08")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$flashback")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Background(image="bg_20_G09")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$flashback")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Image(image="20_I06",xScale=1.8,yScale=1.8,y=-300,fadetime=0)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Delay(time=1.3)]
[stopmusic(fadetime=0)]
[PlaySound(key="$livecrowd",volume=0.5)]
[PlaySound(key="$e_skill_demonkatk")]
[Image(image="20_I00", fadetime=0)]
[CameraShake(duration=0.5, xstrength=100, ystrength=100, vibrato=80, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[ImageTween(xScaleFrom=3, yScaleFrom=3, xScaleTo=1.05, yScaleTo=1.05, duration=0.2, block=true)]
[ImageTween(xScaleFrom=1.05, yScaleFrom=1.05, xScaleTo=1, yScaleTo=1, duration=5, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[delay(time=3)]
[Character]
[Background(image="bg_lungmen_m",screenadapt="coverall")]
[Delay(time=1)]
[image]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[character(name="avg_npc_036")]
[name="林雨霞"]爸，这封请帖是......
[character(name="avg_npc_034")]
[name="鼠王"]今年也来了吗，真是个不死心的女人。
[character(name="avg_npc_036")]
[name="林雨霞"]女人？不死心？
[dialog]
[delay(time=1)]
[name="林雨霞"]我会告诉妈。
[character(name="avg_npc_034")]
[name="鼠王"]别想太多。商业城市联盟里的一个市长，大概十年前左右魏彦吾还有心情亲自过去，往后就只是通过信使往来了。
[name="鼠王"]她倒是不死心，每年这个时候都会给我和魏彦吾寄信，请我们过去。
[character(name="avg_npc_036")]
[name="林雨霞"]商业联盟......哥伦比亚的那座？
[character(name="avg_npc_034")]
[name="鼠王"]不，玻利瓦尔的，你应当听说过，她是那

... (全文32445字符)
```

### level_act12side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_20_G02")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_421_laplum_1#1",fadetime=0.7)]
[name="拉菲艾拉"]......
[dialog]
[delay(time=0.51)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.7)]
[delay(time=2)]
[Character(name="char_empty")]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_npc_196_1#1",fadetime=0.7)]
[name="林雨霞"]......
[dialog]
[delay(time=0.51)]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.51)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_421_laplum_1#1",fadetime=0.7)]
[name="拉菲艾拉"]......
[Character(name="avg_421_laplum_1#5",fadetime=0.7)]
[dialog]
[delay(time=0.51)]
[character(fadetime=0.5)]
[Character(name="char_empty")]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_npc_196_1#4",fadetime=0.7)]
[delay(time=0.7)]
[name="林雨霞"]（不见了？！）
[name="林雨霞"]（她应该没有发现我。）
[name="林雨霞"]（是经受过训练，在平时也会保持反侦察的行动方式？）
[Character(name="avg_npc_196_1#1")]
[name="林雨霞"]（还是说，这一带有什么她要掩人耳目才能进去的地方？）
[Character(name="avg_npc_196_1#5")]
[name="林雨霞"]（......算了，先去找陈晖洁吧。）
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Image(image="20_I07",screenadapt="coverall", fadetime=0)]
[PlayMusic(intro="$emperor_intro", key="$emperor_loop", volume=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="D.D.D."]首先，由我来宣布出线队伍名单。
[name="D.D.D."]本次大奖赛的第一轮比赛中，一共有十五支队伍出线。
[name="D.D.D."]鼠胆龙威队，当之无愧的最大热门。
[name="D.D.D."]灰羽队、吃豆人队、甜蜜夏日队、商务合作请致电5453-46235队......
[dialog]
[stopmusic(fadetime=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg(imagegroup="bg_20_G04_1/bg_20_G04_2", solidwidth="920/920", solidheight=720,x=-720)]
[Image]
[delay(time=0.6)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[name="经纪人"]辛苦了，D.D.D.。
[name="经纪人"]让你做你不习惯的事真是不好意思。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]没事，大人物的面子，这种事我早就习惯了。
[name="D.D.D."]一开始确实很不适应，不过试了一下发现，其实和做DJ的感觉也很相似。
[name="D.D.D."]只不过一个是用音乐带动气氛，一个是用语言。
[character]
[name="经纪人"]你能这么想就好，要是你真的觉得不想做，我会全力帮你推掉的。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]一定要说的话，虽然只是逢场作戏，不过有的瞬间也会觉得自己说了些过去的自己绝不会说的话。
[name="D.D.D."]真是危险。
[dialog]
[delay(time=1)]
[name="D.D.D."]不过，别的不说，那支叫鼠胆龙威的队伍你也看到了。
[name="D.D.D."]这支队伍里面的两位女侠真是很厉害。
[character]
[name="经纪人"]啊，那确实。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]看着她们两个，我感觉我也不自觉地被带动起来了。
[name="D.D.D."]都要忍不住为她们两个作一首歌出来了。
[name="D.D.D."]为了能在特等席观看她们两个的比赛，我感觉我还能坚持很久。
[character]
[name="经纪人"]哈哈，那真是太好了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[largebg]
[Background(image="bg_20_G02")]
[Delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_203_1#5",name2="avg_npc_197_1#7",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_npc_203_1#5",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]哎，Missy，我真不明白，比赛结束了你反而来劲了。
[name="星熊"]看你这几天兴致勃勃地到处走，也不像是纯逛街，有什么这么让你感兴趣的？
[character(name="avg_npc_203_1#5",name2="avg_npc_197_1#7",focus=2)]
[name="诗怀雅"]逛街还是在逛的，不过，我还有另一个目的。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#7",focus=1)]
[name="星熊"]另一个目的？
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]我要了解这座城市。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#5",focus=1)]
[name="星熊"]了解这座城市？为什么？
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#6",focus=2)]
[name="诗怀雅"]在这座城市的围墙外，是玻利瓦尔，一个被三方政府割据的国家。
[name="诗怀雅"]莱塔尼亚扶持的辛嘉斯政府，哥伦比亚支持的联合政府，为了反抗这两家政府揭竿而起的真正玻利瓦尔人。
[name="诗怀雅"]三方政府之间的大小摩擦，恐怕我们现在坐在这里的时候都在不停发生。
[name="诗怀雅"]而这座城市，完全不像我们来的路上经过的那些玻利瓦尔城市。
[name="诗怀雅"]这座城市已经不能用繁华来形容了，就算是我，都没有见过这么奢侈和娱乐的城市。
[character(name="avg_npc_203_1#4",name2="avg_npc_197_1#5",focus=2)]
[name="诗怀雅"]在这样的一个国家里，为什么会有这样的一座城市，你不好奇吗？
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#5",focus=1)]
[name="星熊"]要说的话，确实有点好奇，不过这里不是龙门，我也懒得深究。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#6",focus=2)]
[name="诗怀雅"]你这人，明明什么都懂，结果只要是和龙门或者陈无关的事情，就不怎么上心。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#6",focus=1)]
[name="星熊"]习惯了嘛。接着说，Missy，既然你这么说，那你肯定有想法吧。
[character(name="avg_npc_203_1#1",name2="avg_npc_197_1#2",focus=2)]
[name="诗怀雅"]如果这座城市是灰暗的，那我一点也不会感到奇怪。但是相反，它具有一种让人讨厌的活力。
[character(name

... (全文29902字符)
```

### level_act12side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_20_G06")]
[character(name="char_empty",name2="avg_npc_192_1#2")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_421_laplum_1#7",name2="avg_npc_192_1#2",fadetime=1)]
[delay(time=1.5)]
[character(name="avg_421_laplum_1#7",name2="avg_npc_192_1#2",focus=1)]
[name="拉菲艾拉"]爸爸，下面的人让我告诉你，准备都做好啦。
[character(name="avg_421_laplum_1#7",name2="avg_npc_192_1#1",focus=2)]
[name="潘乔"]是吗。
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#1",focus=1)]
[name="拉菲艾拉"]嗯？爸爸，你好像不怎么高兴？
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#2",focus=2)]
[name="潘乔"]嗯。
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#2",focus=1)]
[name="拉菲艾拉"]为什么？爸爸不是等这一天等了很久吗？
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#5",focus=2)]
[name="潘乔"]坎黛拉是个难缠的女人，不到最后一刻都不能放松警惕。
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#1",focus=2)]
[name="潘乔"]拉菲艾拉。
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#1",focus=1)]
[name="拉菲艾拉"]嗯？
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#1",focus=2)]
[name="潘乔"]如果情况不对，你就让埃内斯托那小子带你跑。
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#1",focus=1)]
[name="拉菲艾拉"]诶？我要和爸爸在一起。
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#1",focus=2)]
[name="潘乔"]别任性。本来，这件事就不该把你卷进来的。
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#2",focus=2)]
[name="潘乔"]老皮尤要是知道他托付给我的女儿跟着我干这个，怕是要从坟墓里爬起来宰了我。
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#2",focus=2)]
[name="潘乔"]至于埃内斯托那小子......哼。
[character(name="avg_421_laplum_1#1",name2="avg_npc_192_1#2",focus=1)]
[name="拉菲艾拉"]哥哥怎么啦？
[character(name="avg_421_laplum_1#1",name2="avg_npc_192_1#2",focus=2)]
[name="潘乔"]那小子以为我看不出来，他那点心思，我怎么可能看不出来。
[character(name="avg_421_laplum_1#1",name2="avg_npc_192_1#2",focus=1)]
[name="拉菲艾拉"]哥哥没有背叛哦。
[character(name="avg_421_laplum_1#1",name2="avg_npc_192_1#1",focus=2)]
[name="潘乔"]我知道，没有这小子，这事成不了。
[name="潘乔"]但他其实不想这么做。
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#1",focus=1)]
[name="拉菲艾拉"]这是为什么呢？
[character(name="avg_421_laplum_1#2",name2="avg_npc_192_1#1",focus=2)]
[name="潘乔"]谁不想吃好喝好睡好，不去想那些有的没的？
潘乔揉了揉站在身边的养女的头。
[character(name="avg_421_laplum_1#1",name2="avg_npc_192_1#2",focus=2)]
[name="潘乔"]好了，乖，去把我的烟斗拿来，我要一个人静一静。
[character(name="avg_421_laplum_1#6",name2="avg_npc_192_1#2",focus=1)]
[name="拉菲艾拉"]哦......
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(name="char_empty",name2="avg_npc_192_1#2",fadetime=1)]
[delay(time=1.5)]
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[character(name="avg_486_espumo_1#1",name2="char_empty")]
[delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#1",fadetime=1)]
[delay(time=1.5)]
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#1",focus=1)]
[name="埃内斯托"]陈小姐，你来了。
[name="埃内斯托"]林小姐呢，我以为她会和你一起。
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#1",focus=2)]
[name="陈"]看来你不打算掩饰了。
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.4)]
[character(name="avg_486_espumo_1#6",name2="avg_1013_spchen_1#1",focus=1)]
[name="埃内斯托"]老实说，都到了这份上，我也没有什么掩饰的必要了，不是吗？
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#1",focus=1)]
[name="埃内斯托"]我确实没有想到，你们居然这样都能突破出来。
[name="埃内斯托"]我还是小看了你们。
[name="埃内斯托"]不过，我很好奇，你们是怎么发现的？
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#1",focus=2)]
[name="陈"]林雨霞在第一轮就发现了你们在安装炸药，只是我们没有告诉你。
[character(name="avg_486_espumo_1#3",name2="avg_1013_spchen_1#1",focus=1)]
[name="埃内斯托"]......在那时候，我就被怀疑了？
[character(name="avg_486_espumo_1#3",name2="avg_1013_spchen_1#1",focus=2)]
[name="陈"]那个时候只是以防万一罢了。
[name="陈"]而我们确认你有问题，是因为在你的武器店里发现了同样的炸药。
[character(name="avg_486_espumo_1#4",name2="avg_1013_spchen_1#1",focus=1)]
[name="埃内斯托"]原来如此。
[name="埃内斯托"]没想到胜负在这么早就分出来了。
[character(name="avg_486_espumo_1#4",name2="avg_1013_spchen_1#1",focus=2)]
[name="陈"]你现在是什么意思，垂死挣扎？还是想要自首？
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#1",focus=1)]
[name="埃内斯托"]我只是有一些话想说，陈小姐。
[name="埃内斯托"]听完或许你会有不同的看法。
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#2",focus=2)]
[name="陈"]洗耳恭听。
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#2",focus=1)]
[name="埃内斯托"]陈小姐，你知道玻利瓦尔的历史吗？
[character(name="avg_486_espumo_1#1",name2="avg_1013_spchen_1#1",focus=2)]
[name="陈"]不怎么清楚。
[character(name="avg_486_espumo_1#6",name2="avg_1013_spchen_1#1",focus=1)]
[name="埃内斯托"]也是，你过去是在维多利亚留学，维多利亚没有怎么插手玻利瓦尔的事，想来不特意调查的话不会知道得很清楚。
[character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]在伊比利亚发现这片土地之前，这里只是一片叫做玻利瓦尔的平原。
[name="埃内斯托"]伊比利亚人在这里发现了许多源石矿脉，于是他们驻足于此，将这里变成了他们的附属地。
[name="埃内斯托"]然后，因为种种原因，伊比利亚的统治终结了。
[name="埃内斯托"]经过混乱的一百三十年后，莱塔尼亚人来了。
[name="埃内斯托"]于是玻利瓦尔又成为了莱塔尼亚的附属地。
[name="埃内斯托"]两百年前，玻利瓦尔从附属地演变成了附属国，也就是辛嘉斯王朝。
[name="埃内斯托"]可以说，玻利瓦尔是从那个时候才成为了现在的玻利瓦尔——虽然辛嘉斯王朝的人从不自称玻利瓦尔人。
[name="埃内斯托"]然后，巫王时期，莱塔尼亚试图通过玻利瓦尔在哥伦比亚掀起内乱。
[character(name="avg_486_espumo_1#7")]
[name="埃内斯托"]但是，这么做的结果却是，内乱不仅失败，玻利瓦尔反被哥伦比亚入侵，联合政府就是在那时候建立的。
[name="埃内斯托"]玻利瓦尔从此进入了哥伦比亚和莱塔尼亚割据的状态。
[name="埃内斯托"]莱塔尼亚对于玻利瓦尔并没有那么上心，而哥伦比亚虽然野心勃勃却也没有办法一口吞下。
[name="埃内斯托"]双方于是进入了拉锯状态。
[name="埃内斯托"]而后，再也无法忍受这种状态的玻利瓦尔人选择了反抗。
[name="埃内斯托"]他们成立了反抗军，自称真正玻利瓦尔人，并立誓将玻利瓦尔变成真正独立的国家。
[name="埃内斯托"]但是，事情并没有好转，真正玻利瓦尔人的建立只是将玻利瓦尔拖入更深的泥潭。
[name="埃内斯托"]最后，玻利瓦尔变成了现在这副样子。
[name="埃内斯托"]联合政府，辛嘉斯王朝，真正玻利瓦尔人，三方陷入了永无止境的战火之中。
[name="埃内斯托"]不仅如此，在这样的环境中，诞生了多索雷斯这样一座城市。
[name="埃内斯托"]在坎黛拉女士的治理下，这座城市不仅在三方政府中都吃得开，而且甚至很多时候三方都要卖坎黛拉女士人情。
[name="埃内斯托"]因为这座城市坐拥他们无法忽视的资源，而且坎黛拉女士手上也有足够的力量保护这座城市。
[name="埃内斯托"]这座城市于是逐渐成为了玻利瓦尔人人都向往的地方。
[name="埃内斯托"]每一个饱受战火折磨的玻利瓦尔人，心中的梦想都是攒钱来这里玩，甚至是在这里翻身。
[dialog]
[delay(time=1)]
[character(name="avg_486_espumo_1

... (全文9861字符)
```

### level_act12side_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_hotel")]
[Delay(time=1)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_NPC_017_3",fadetime=0.2)]
[delay(time=1)]
[name="D.D.D."]......呼。
[character]
[name="经纪人"]你终于醒了，D.D.D.。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]怎么了，睡完觉醒过来不是很正常的事？
[character]
[name="经纪人"]但你昨天回来之后倒头就睡，搞得我有点害怕。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]......现在外面是什么情况？
[character]
[name="经纪人"]如果你是问城里的状况的话，和之前没什么差别，一样的喧闹。
[name="经纪人"]我去吃早饭的时候听到很多人在讨论昨天的事，但是他们也都不怎么在乎的感觉。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]毕竟事情已经被冲淡了。
[name="D.D.D."]坎黛拉市长真是个厉害人物。
[name="D.D.D."]在昨天那种情况下，居然会用那样的方式......
[character]
[name="经纪人"]我当时在电视前也震惊了。
[name="经纪人"]那种镇场的方式，真的是闻所未闻。
[name="经纪人"]而且还真的有不少人去和那些危险分子战斗了。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]我当时就在旁边，那种感觉，真是太奇妙了。
[name="D.D.D."]坎黛拉女士的不远处，是想要拼命冲过来杀掉她的危险分子。
[name="D.D.D."]而坎黛拉女士对此却不屑一顾，她只关心无人机有没有靠近游轮，能否看到船上的情况。
[name="D.D.D."]她就站在那里，对着屏幕和海面指指点点，一边和旁边的人说笑着。
[name="D.D.D."]在那一刻，正在发生的一切仿佛都是不真实的。
[name="D.D.D."]最后，那两位女侠出现了。
[name="D.D.D."]她们的出现又将一切拉回了现实。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="D.D.D."]这真是......这真是太刺激了！
[character]
[name="经纪人"]所以你想创作。
[character(name="avg_NPC_017_3")]
[name="D.D.D."]啊哈哈，不愧是你，真了解我。
[character]
[name="经纪人"]你以为我们认识了多久？
[character(name="avg_NPC_017_3")]
[name="D.D.D."]是的，我要创作，我要将此时此刻的害怕、感激、迷茫都记录下来，作成一首歌。
[name="D.D.D."]这首歌为我自己而作，但与她们有关。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_20_G02")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_437_mizuki_1#1",fadetime=1)]
[delay(time=1.5)]
[name="水月"]这座城市虽然还挺好的。
[character(name="avg_437_mizuki_1#7")]
[name="水月"]莱塔尼亚的歌剧，哥伦比亚的电影，还有玻利瓦尔的咖啡，之前想要体验的东西都体验到了。
[character(name="avg_437_mizuki_1#2")]
[name="水月"]不过，这座城市里的人还真是无聊，比赛过半就不想跟他们玩了。
[name="水月"]要是早知道最后会变成这样，中途确认陈姐姐没事后应该和她一起上船的，这样应该能多帮上她的忙吧。
[character(name="avg_437_mizuki_1#1")]
[name="水月"]算啦，反正这座城市也差不多玩腻了，看一看陈姐姐她们会去哪里吧。
[character(name="avg_437_mizuki_1#7")]
[name="水月"]陈姐姐来的地方，肯定也有许多和陈姐姐一样的好人吧。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1)]
[delay(time=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_hotel")]
[character(name="avg_npc_197_1#5",name2="avg_1013_spchen_1#1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[character(name="avg_npc_197_1#5",name2="avg_1013_spchen_1#6",focus=2)]
[name="陈"]你太乱来了，诗怀雅。
[character(name="avg_npc_197_1#5",name2="avg_1013_spchen_1#6",focus=1)]
[name="诗怀雅"]嗯嗯嗯，哦哦哦，好好好，知道了知道了，为什么我非得被你教训不可！
[character(name="avg_npc_197_1#5",name2="avg_1013_spchen_1#6",focus=2)]
[name="陈"]现在近卫局可以说就是交在你的手里，你却......
[character(name="avg_npc_197_1#5",name2="avg_1013_spchen_1#6",focus=1)]
[name="诗怀雅"]哎呀，我自己有数的。
[character(name="avg_npc_197_1#6",name2="avg_1013_spchen_1#6",focus=1)]
[name="诗怀雅"]你才是，明明是跑罗德岛当干员，结果却偷偷跑这里来度假！
[character(name="avg_npc_197_1#6",name2="avg_1013_spchen_1#2",focus=2)]
[name="陈"]我这是......算了，你说得也没错。
[character(name="avg_npc_197_1#2",name2="avg_1013_spchen_1#2",focus=1)]
[name="诗怀雅"]哼。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_203_1#1")]
[name="星熊"]接着吵啊，怎么停了，老陈走了之后，你们上次吵架感觉都不知道是什么时候的事了。
[character(name="avg_npc_197_1#5")]
[name="诗怀雅"]我上次去罗德岛的时候还是吵过的。
[character(name="avg_npc_203_1#1")]
[name="星熊"]哎呀，总之，来都来了，事情也都解决了，我们还是把一些不愉快给忘掉，然后好好地玩一玩才是正经。
[name="星熊"]对吧，老陈？
[character(name="avg_1013_spchen_1#2")]
[name="陈"]哈......也是。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_203_1#1",focus=2)]
[name="星熊"]怎么了，还在想昨天的事吗？
[character(name="avg_1013_spchen_1#2",name2="avg_npc_203_1#1",focus=1)]
[name="陈"]是。呵，这可能是我这辈子收到的最不想要的荣誉了。
[character(name="avg_1013_spchen_1#2",name2="avg_npc_203_1#1",focus=2)]
[name="星熊"]哈哈，确实，老实说，就算是我，也觉得够膈应人的。
[name="星熊"]但是它就是发生了。
[name="星熊"]老陈，世上可没有那么多两全其美和称心如意的事。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_203_1#1",focus=1)]
[name="陈"]我知道。
[character(name="avg_npc_197_1#1")]
[name="诗怀雅"]行了行了，比起坐着聊天，不如出去购物吃大餐才能提起精神。
[name="诗怀雅"]走了，中午本小姐请客。
[character(name="avg_npc_197_1#4")]
[name="诗怀雅"]那只死老鼠去哪了？
[character(name="avg_1013_spchen_1#1",name2="avg_npc_203_1#5",focus=2)]
[name="星熊"]她好像一大早就出去了，但是不知道去哪。
[character(name="avg_1013_spchen_1#1",name2="avg_npc_203_1#5",focus=1)]
[name="陈"]我大概知道，我去找她吧。
[character(name="avg_npc_197_1#5")]
[name="诗怀雅"]找到了记得告诉我。
[name="诗怀雅"]哼，昨晚开始就躲着我，等我找到她，她死定了。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_bar_1")]
[character(name="avg_npc_207",name2="avg_npc_196_1#1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[character(name="avg_npc_207",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]我离开后，这里就交给你打理。
[name="林雨霞"]教给你的那些没忘吧？
[character(name="avg_npc_207",name2="avg_npc_196_1#1",focus=1)]
[name="赌场老板"]当然，您放一百个心。
[dialog]
[character]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_1013_spchen_1#1",fadetime=1)]
[delay(time=1.5)]
[name="陈"]你们在聊什么？
[character(name="avg_npc_207",name2="avg_npc_196_1#1",focus=1)]
[name="赌场老板"]啊，是陈小姐，大姐头正在给我们训话呢。
[character(name="avg_npc_207",name2="avg_npc_196_1#5",focus=2)]
[name="林雨霞"]别跟她扯这个，小心她逮捕你。
[character(name="avg_1013_spchen_1#1")]
[name="陈"]我已经不是警察了。
[character(name="avg_npc_196_1#5")]
[name="林雨霞"]我可没见过你这么多管闲事的游客。
[character(name="avg_1013_spchen_1#2")]
[name="陈"]哼。
[character(name="avg_npc_207",name2="avg_npc_196_1#1",focus=2)]
[name="林雨霞"]先下去吧。
[character(name="avg_npc_207",name2="avg_npc_196_1#1",focus=1)]
[name="赌场老板"]是。
[dialog]
[playsound(ke

... (全文19708字符)
```

### level_act12side_tr01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_20_G08")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]陈小姐和林小姐，好厉害的身手。
[name="埃内斯托"]她们要是参加今年的大奖赛的话，比赛大概会变得很有意思吧，不过......
[dialog]
[character]
[PlaySound(key="$phonevibration",volume=0.6)]
[delay(time=1)]
[PlaySound(key="$d_gen_transmissionget",volume=1)]
[Delay(time=0.7)]
[CharacterCutin(widgetID="1", name="avg_npc_207", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=-300, width=200, block=true)]
[Character(name="char_empty",name2="avg_486_espumo_1#1",focus=-1)]
[name="护卫"]D.D.D.同意当主持人。
[Character(name="char_empty",name2="avg_486_espumo_1#1",focus=2)]
[name="埃内斯托"]是吗......那就只好对不起尤里卡小姐了。
[name="埃内斯托"]不过，出了那样的播放事故，也确实没办法就是了。
[name="埃内斯托"]备一份礼品，之后我亲自去向她说明。
[Character(name="char_empty",name2="avg_486_espumo_1#1",focus=-1)]
[name="护卫"]是。
[Character(name="char_empty",name2="avg_486_espumo_1#1",focus=2)]
[PlaySound(key="$d_gen_transmissionget",volume=1)]
[CharacterCutin(widgetID="1",block=true)]
[dialog]
[delay(time=1.5)]
[Character(name="char_empty", name2="avg_486_espumo_1#1")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_npc_205", name2="avg_486_espumo_1#1",fadetime=0.7)]
[delay(time=0.7)]
[Character(name="avg_npc_205", name2="avg_486_espumo_1#1",focus=1)]
[name="参赛选手"]老板，你终于开店了。
[Character(name="avg_npc_205", name2="avg_486_espumo_1#1",focus=2)]
[name="埃内斯托"]想在我这里做改造？
[Character(name="avg_npc_205", name2="avg_486_espumo_1#1",focus=1)]
[name="参赛选手"]没错，听说你手艺很好，我就一直在等你开店。
[Character(name="avg_npc_205", name2="avg_486_espumo_1#1",focus=2)]
[name="埃内斯托"]把你收集到的标志物给我看看吧。
[Character(name="avg_npc_205", name2="avg_486_espumo_1#1",focus=1)]
[name="参赛选手"]好嘞。
参赛选手将一个布包放在了柜台上。
[Character(name="avg_npc_205", name2="avg_486_espumo_1#5",focus=2)]
[name="埃内斯托"]看来你运气还不错......过来吧，仓库在这边。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[showitem(image="item_act12side_1")]
[delay(time=1)]
[name="Tips"]现在，可以前往<color=#ee4321>多索雷斯防卫精品</color>了解与标志物有关的各种信息了！
[Dialog]
[hideitem]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_205", name2="avg_486_espumo_1#1",fadetime=0.7)]
[delay(time=0.7)]
[Character(name="avg_npc_205", name2="avg_486_espumo_1#1",focus=2)]
[name="埃内斯托"]这样就懂了吧？
[Character(name="avg_npc_205", name2="avg_486_espumo_1#1",focus=1)]
[name="参赛选手"]懂了懂了，还挺方便的。
[name="参赛选手"]谢谢你啊，老板，对我这种外地人这么亲切，你可真是个大好人。
[Character(name="avg_npc_205", name2="avg_486_espumo_1#5",focus=2)]
[name="埃内斯托"]哪里哪里。
[Character(name="avg_npc_205", name2="avg_486_espumo_1#5",focus=1)]
[name="参赛选手"]那我就先走了！
[Character(name="avg_npc_205", name2="avg_486_espumo_1#5",focus=2)]
[name="埃内斯托"]欢迎下次光临。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-300, fadetime=2,block=false)]
[character(name="char_empty",name2="avg_486_espumo_1#5",fadetime=0.5)]
[delay(time=2)]
[character]
[delay(time=1)]
[Character(name="avg_486_espumo_1#1")]
[name="埃内斯托"]呼......之后，大概还要给陈小姐和林小姐解释一遍这一套东西，姑且先把她们两位的收藏品的空间准备好吧。
[Character(name="avg_486_espumo_1#5")]
[name="埃内斯托"]而且，好人啊......哈哈。
[name="埃内斯托"]但愿吧。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Image]
```

### training_act12side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12side教学关_a

[PopupDialog(dialogHead="$avatar_takila")] 两位可能还不熟悉这座城市，我来为两位讲解一下。
[PopupDialog(dialogHead="$avatar_takila")] 为了模拟大海的感觉，术师们操纵了潮汐，在潮汐的侵蚀下，无论是什么人的战斗能力都会受到影响。
[PopupDialog(dialogHead="$avatar_takila")] 很显然，一旦潮水侵蚀了地面，那要在上面<@tu.kw>部署</>就很困难了。
[PopupDialog(dialogHead="$avatar_npc196")] 真麻烦。
```

### training_act12side_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12side教学关_b

[PopupDialog(dialogHead="$avatar_chen3")] 啧，开始有点力不从心了……
[PopupDialog(dialogHead="$avatar_takila")] 是这样的，受到潮汐侵蚀后，留在水中的我方人员会受到<@tu.imp>水蚀</>，攻击速度会<@tu.imp>降低</>，并且作战装备会不断受到<@tu.kw>侵蚀</>，如果受到敌人<@tu.kw>攻击</>，还会加速这一过程。
```

### training_act12side_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12side教学关_c

[Tutorial(focusX=-6, focusY=85, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_takila", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
当<@tu.kw>侵蚀</>累积到一定程度，装备会发生严重的故障，这种情况会造成大量的<@tu.kw>物理</>伤害，并且导致<@tu.imp>防御力永久降低</>。
[PopupDialog(dialogHead="$avatar_takila")] 幸好，虽然并不绝对，但敌人控制潮汐的幅度往往无法没过高台。可以利用敌方术师的弱点，让擅长远程攻击的人在高处协助。
```

### training_act12side_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12side教学关_d

[PopupDialog(dialogHead="$avatar_takila")] 潮水暂时退去了，但我们也好不到哪里去。
[PopupDialog(dialogHead="$avatar_takila")] 而且不要忘了，被潮汐侵蚀的地面是无法进行<@tu.kw>部署</>的，在那之前，好好休整一下。
```

### training_act12side_01_e

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12side教学关_e

[PopupDialog(dialogHead="$avatar_chen3")] 我差不多习惯了。
[Tutorial(focusX=373, focusY=105, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_chen3", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
而且反过来说，潮汐的侵蚀不分敌我，敌人同样会受到<@tu.kw>水蚀</>，不仅攻击速度和移动速度<@tu.imp>降低</>了，还会持续<@tu.imp>损失生命</>。
[PopupDialog(dialogHead="$avatar_chen3")] 所以只要能坚持住，对我们来说，也是个进攻的机会，没错吧？
[PopupDialog(dialogHead="$avatar_takila")] 不愧是陈小姐，完全正确。
[PopupDialog(dialogHead="$avatar_chen3")] 那么接下来，就换我们进攻了。
```

### training_act12side_02_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12side教学关2_a

[PopupDialog(dialogHead="$avatar_takila")] 两位，以你们的身手，想必那点炸药不会让你们受到多大的伤害。拜托你们，被我困住吧。
[PopupDialog(dialogHead="$avatar_takila")] 呼......那么，看来这些人都是坎黛拉女士准备的埋伏，不是我们的人，得好好应对了。
[PopupDialog(dialogHead="$avatar_takila")] 幸好，这片天然水域十分宽阔，一般敌人很难通行。
[PopupDialog(dialogHead="$avatar_takila")] 敌人在水中行动迟缓，并且会不断受到伤害，渡水登陆并不明智，我只要能找一个狭窄的地形......
```

### training_act12side_02_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12side教学关2_b

[PopupDialog(dialogHead="$avatar_takila")] 啧，两栖摩托艇载具，连这种东西都准备了吗，这下，这片水域不会给他们造成任何麻烦了。
[PopupDialog(dialogHead="$avatar_takila")] 该怎么办好呢......
[PopupDialog(dialogHead="$avatar_takila")] 对了，在水上制造一些<@tu.kw>可以站立的平台</>吧，这种临时的平台应该<@tu.kw>什么人都可以用</>。 
```

### training_act12side_02_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12side教学关2_c

[PopupDialog(dialogHead="$avatar_takila")] 虽然你们的载具相当坚固，但是只要在水上破坏掉你们的载具，那掉进水里的你们和待宰的肉又有什么区别呢？
[PopupDialog(dialogHead="$avatar_takila")] 通过水上平台攻击他们，在他们登陆前击毁他们的载具。
[Tutorial(focusX=-55, focusY=93, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_takila", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
建议<@tu.kw>在这里布置重装干员</>，阻碍他们的前进应该不错。
```


> 本章节共31个脚本文件，此处展示前30个。

## 统计

- 总字符数：276586
- 对话行数：2486


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
