# 明日方舟 · 主线/常驻 · main（407段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 主线/常驻, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟主线/常驻「main」完整剧情脚本（407个文件，1741行对话）

## 正文
## 章节信息

- 分类：主线/常驻
- 目录：obt/main
- 脚本文件数：407

### level_main_00-01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Character]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Background(image="bg_cher_1",x=0, y=20, xScale=1.1, yScale=1.1, fadetime=1)]
[Dialog]
[Delay(time=1)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  可恶......
[name="杜宾"]  这里，究竟怎么了？
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Image(image="avg_2_2",x=0, y=0, xScale=1, yScale=1, fadetime=0)]
[Blocker(a=0, fadetime=0.6, block=false)]
[ImageTween(xFrom=0, yFrom=0, xTo=0, yTo=-20, xScaleFrom=1, yScaleFrom=1, xScaleTo=1.1, yScaleTo=1.1, duration=15, block=false)]
[name="整合运动成员"]  这边的屋子，也都给我搜干净！
[name="女性"]  放开他......不！你们......
[name="整合运动成员"]  反抗？太迟了！可恨的切尔诺伯格人！
[name="男性"]  快跑！不要管我......孩子就......
[name="孩童"]  妈妈......妈妈......！
[name="乌萨斯军警"]  别管平民！先把阵线守住！这些面具混蛋，人实在是太多了！
[name="整合运动成员"]  别让军警闲着！继续打！
[name="乌萨斯军警"]  增援怎么还没到！我们要......
[name="整合运动成员"]  上啊，上啊！！
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Image]
[Blocker(a=0, fadetime=1, block=true)]
[Dialog]
[Character(name="char_002_amiya_1#5")]
[name="阿米娅"]  怎么回事......？！为什么，为什么整合运动会......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  遮遮掩掩这么多年，还是露出本性了吗？
[Character(name="char_016_medic")]
[name="医疗干员"]  感，感染者......在袭击乌萨斯人......
[Character(name="char_013_riop")]
[name="近卫干员"]  为，为什么！感染者这样去骚扰乌萨斯政府的话，会死无葬身之地的......！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  不，他们的攻势相当猛烈。这绝对是有预谋的行动。
[name="杜宾"]  之前我们救出博士的位置，相当机密......就连那里都被他们渗入了。
[name="杜宾"]  可能切尔诺伯格各处，都已经遭到了整合运动的袭击。
[Character(name="char_013_riop")]
[name="近卫干员"]  啊......这，怎么会......
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  嘘！
[StopMusic(fadetime=0.8)]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.6, block=true)]
[name="整合运动成员A"]  还有逃脱的切尔诺伯格人吗？
[name="整合运动成员B"]  我在搜！
[name="整合运动成员A"]  一个也别漏掉！
[name="整合运动成员A"]  切尔诺伯格的冷血动物......刻在我父辈身上的痛苦，这次，就让我全都还给你们！
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_016_medic")]
[name="医疗干员"]  （咳......）
[Dialog]
[Character]
[name="整合运动成员A"]  什么声音？
[name="整合运动成员B"]  在那里！
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=1, crossfade=1.5)]
[Character(name="char_016_medic")]
[name="医疗干员"]  （唔！）
[name="医疗干员"]  （他，他们，发......）
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  （安静！）
[Character(name="char_016_medic")]
[name="医疗干员"]  （唔......！）
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.6, block=true)]
[Dialog]
[Delay(time=1)]
[Character(name="char_1002_nsabr_2")]
[Delay(time=1.5)]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Background]
[Blocker(a=0, fadetime=0.6, block=true)]
[name="女性"]  ......呜......
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Background(image="bg_cher_1",x=0, y=20, xScale=1.1, yScale=1.1, fadetime=1)]
[Blocker(a=0, fadetime=0.6, block=true)]
[name="整合运动成员A"]  在这儿！找到了！
[name="女性"]  ......呜哇哇哇！！！
[name="女性"]  啊！不，别......
[name="整合运动成员B"]  ......！
[name="整合运动成员B"]  躲在巷子里？
[name="整合运动成员B"]  出来。
[name="女性"]  啊，啊啊......！
[name="整合运动成员B"]  躲在那里，就有用吗......
[name="女性"]  对，对不起！对不起啊！！至少，至少饶了我的儿子！！
[name="整合运动成员B"]  ......
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Character]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  ......我们应该，立刻突袭整合运动。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ......阿米娅......
[Character(name="char_002_amiya_1#7",name2="char_130_doberm_ex",focus=1)]
[name="阿米娅"]  我知道有风险，杜宾教官。
[name="阿米娅"]  只是，等这些整合运动解散后再行动......会耗费大量时间。
[name="阿米娅"]  何况，谁知道现在的状况，会持续到什么时候......
[name="阿米娅"]  那么，就应该迅速击溃敌人并转移。我说的，没错吧？
[Character(name="char_002_amiya_1#7",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  ——————
[name="杜宾"]  明白了，我服从你的命令。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  各小组，听好。
[name="杜宾"]  这些整合运动，还没有意识到我们的存在。
[name="杜宾"]  记住，果断、迅速地解决掉！
[name="杜宾"]  Dr.{@nickname}，调集队伍吧，现在是你证明自己的时候了。
[name="杜宾"]  现在的局势，可不允许我们有所保留。
[Decision(options="早就该交给我了！;......;简单，我会轻松解决的。", values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  呵。
[name="杜宾"]  阿米娅，看你的了。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  我明白。
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.2, block=true)]
[Character(fadetime=0)]
[Background(fadetime=0)]
[Image(image="avg_1_3",x=0, y=-20, xScale=1.1, yScale=1.1, fadetime=1)]
[ImageTween(xFrom=0, yFrom=-20, xTo=0, yTo=0, xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=4, block=false)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Delay(time=0.6)]
[name="阿米娅"]   ......“如果争端能够避免，那我们应当沉默——
[name="阿米娅"]   ——如果战斗是必要的，那就战斗到最后！”
[name="阿米娅"]  罗德岛的信条......从来没有改变过！
[Delay(time=0.6)]
[Dialog]
[Image(image="avg_1_3",x=0, y=0, xScale=1, yScale=1, fadetime=1)]
[PlaySound(key="$flashback", volume=0.7)]
[ImageTween(xFrom=0, yFrom=0, xTo=0, yTo=-700, xScaleFrom=1, yScaleFrom=1, xScaleTo=8, yScaleTo=8, duration=1.6, block=false)]
[PlaySound(key="$flashback", volume=0.7, Delay=0.3)]
[PlaySound(key="$flashback", volume=0.7, Delay=0.7)]
[Delay(time=0.2)]
[Blocker(a=1,r=255, g=255, b=255, fadetime=0.3, block=true)]
[Image]
[Blocker(block=true, fadetime=0.5)]
```

### level_main_00-01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（后）
[Background(image="bg_cher_1",fadetime=1,screenadapt="coverall")]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Delay(time=1)]
[CameraShake(duration=1.5, xstrength=7, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_1002_nsabr_2")]
[Blocker(a=1, r=255, g=255, b=255, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, fadetime=1.5, block=true)]
[name="整合运动成员"]  呃 ......
[name="整合运动成员"]  你们不是......乌萨斯......人......
[Character(fadetime=0.7)]
[Dialog]
[Delay(time=0.7)]
[Character(name="char_013_riop")]
[name="近卫干员"]   呼，呼......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  看来，他们没来得及联络同伙。
[name="杜宾"]  ......做得不错，Dr.{@nickname}。
[name="杜宾"]  是该客观评价你的能力了。
[Character(name="char_016_medic")]
[name="医疗干员"]  咦，阿米娅......她去......
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   没事吧？
[Character(name="char_002_amiya_1#2",focus=-1)]
[name="女性"]   啊？谢，谢......
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   没事的，这是我们......
[Character(name="char_002_amiya_1#2",focus=-1)]
[name="女性"]   ......你，你也是感染者？
[name="女性"]   你们要做什么！我，我的孩子......别伤害我们，求你了，我......
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   ......
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   去找个安全的地方藏身。
[Character(name="char_002_amiya_1",focus=-1)]
[name="女性"]   呜，呜......宽恕我们......饶了我......
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_016_medic")]
[name="医疗干员"]  ......
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   各位休息好了吗？
[Character(name="char_016_medic")]
[name="医疗干员"]  啊，没事......
[Decision(options="她为什么害怕你？", values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   ......
[name="阿米娅"]   Dr.{@nickname}......
[name="阿米娅"]   类似的问题，你以前也问过呢。
[Decision(options="......", values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   因为我，得了病。
[name="阿米娅"]   我，还有杜宾，罗德岛的大多数人，都得了病。
[name="阿米娅"]   就连刚才那些整合运动的成员也是......
[name="阿米娅"]   我们得了很重的病，让人害怕的病......
[name="阿米娅"]   “矿石病”。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ......得了矿石病的人，就是感染者。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   杜宾......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  乌萨斯向来对感染者十分严苛。
[name="杜宾"]  说起来，谁又不是呢。只是乌萨斯在这方面的举措，尤为冷酷罢了。
[name="杜宾"]  宣传上让民众恐惧感染者，到了抓捕感染者的时候，民众自然就习以为常，甚至拍手称快。
[name="杜宾"]  所以，整合运动才选择了这里......
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   只是......这次，似乎不再是简单的示威游行了。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  这一次，他们开始大规模地使用暴力。
[name="杜宾"]  等到乌萨斯政府平息了事件，切尔诺伯格的感染者，只会遭到更残酷的对待。
[name="杜宾"]  ......与之相反，有了Dr.{@nickname}你，罗德岛的处境，也许能有所改善。
[Decision(options="......这和我也有关系？;......;那我还挺重要的。", values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  凯尔希和阿米娅都和我说过，你是最顶尖的矿石病研究学者。
[name="杜宾"]  ......现在，你陷入了记忆丧失的困境，我很怀疑，你还能不能再派上用场。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   唔唔，杜宾教官，这么说好过分！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ......也许就和指挥一样，等你稍作复习，说不定就能重新掌握那些理论？
[name="杜宾"]  毕竟你还是前线指挥官......
[name="杜宾"]  其实之前，我怎么也没法把神经学博士和战术家联系在一起......
[name="杜宾"]  看到你本人后，似乎好理解了一些。
[name="杜宾"]  毕竟罗德岛本身就很像你的专业。
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_016_medic")]
[name="医疗干员"]   喂！你！别跑！该注射药剂了！
[Character(name="char_016_medic",name2="char_013_riop",focus=2)]
[name="近卫干员"]   啊？啊？我没事，我没事呀！我，我还不需要治疗！
[Character(name="char_016_medic",name2="char_013_riop",focus=1)]
[name="医疗干员"]   是定量药剂，延缓感染症状的！
[name="医疗干员"]   你刚才不是还说头晕吗！
[Character(name="char_016_medic",name2="char_013_riop",focus=2)]
[name="近卫干员"]   那不是同一种症状吧！
[Character(name="char_016_medic",name2="char_013_riop",focus=1)]
[name="医疗干员"]   要是一会儿你的身体又出了问题，再碰上战斗怎么办？
[name="医疗干员"]   为了大家的安全你也该好好注意！
[Character(name="char_016_medic",name2="char_013_riop",focus=2)]
[name="近卫干员"]   ......
[Character(name="char_016_medic",name2="char_013_riop",focus=1)]
[name="医疗干员"]   别动！我要扎了！
[Character(name="char_016_medic",name2="char_013_riop",focus=2)]
[name="近卫干员"]   啊！！
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ......
[name="杜宾"]  ......罗德岛就是这样，既要找出治疗感染者的办法，又要减少感染者带来的问题。
[Character(name="char_130_doberm_ex",name2="char_002_amiya_1",focus=2)]
[name="阿米娅"]   ——是的。光是研究治疗方法，或者仅仅去平息种种争端，都是不够的。
[name="阿米娅"]   我们必须直面感染者带来的所有问题。
[name="阿米娅"]   只有这样，罗德岛才能替感染者争取到一线生机......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  作为感染者，我们也比普通人更能理解感染者。
[name="杜宾"]  无论是普通人还是感染者，无论是和平还是纷争，罗德岛想要解决问题，而不是任由仇恨和疾病蔓延肆虐。
[name="杜宾"]  Dr.{@nickname}，这可能也会是你职责的一部分。
[name="杜宾"]  ......至少，这是我粗浅的请求。
[Decision(options="你在说什么？？;......;我需要更慎重地思索一下。", values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  我们会留给你很多时间的，你可以慢慢理解。
[name="杜宾"]  只不过，给我们的时间却不多了。
[name="杜宾"]  整顿队伍，出发！
[name="杜宾"]  前往汇合点的路上，还不知道有什么等着我们！
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Background]
[Blocker(a=0, fadetime=0.6, block=true)]
[delay(time=1)]
[name="杜宾"]  （阿米娅......）
[name="杜宾"]  （切尔诺伯格现在的情况非常复杂，我们不能给整支救援队伍带去心理压力。但是......）
[name="阿米娅"]  （我们......还有多长时间？）
[name="杜宾"]  （......三小时。）
[name="杜宾"]  （三小时之后，天灾将会吞没这个城市。）
[name="杜宾"]  （等到天灾降临，一切就都完了。）
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Background(image="bg_cher_1",x=0, y=20, xScale=1.1, yScale=1.1, fadetime=1)]
[Blocker(a=0, fadetime=0.6, block=true)]
[Delay(time=1)]
[Character(name="char_1502_crowns#2")]
[name="？？？"]  ......
[name="？？？"]  不确定因素。
[name="？？？"]  去，通知其他人。
[name="？？？"]  我们追。
[Blocker(a=1, r=0,g=0, b=0, fadetim

... (全文6046字符)
```

### level_main_00-02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[Background]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Image(fadetime=0)]
[Background(image="bg_cher_1",fadetime=1,screenadapt="coverall")]
[Blocker(a=0, fadetime=0.6, block=false)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ......这终归还是，太超乎我的想象了。
[name="杜宾"]  爆炸，骚乱，火光，巷战......
[name="杜宾"]  难道整个切尔诺伯格，都陷入了这种混乱吗？
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Image(image="bg_0_tv",x=0, y=0, xScale=1, yScale=1, fadetime=0)]
[Blocker(a=0, fadetime=0.6, block=false)]
[ImageTween(xFrom=0, yFrom=0, xTo=0, yTo=-20, xScaleFrom=1, yScaleFrom=1, xScaleTo=1.1, yScaleTo=1.1, duration=15, block=false)]
[name="电视主持人"]   在切尔诺伯格军警的团结协作与迅速反应之下......
[name="电视主持人"]   ......情况已经被控制，大部分区域的意外事件已经被镇压。
[name="电视主持人"]   目前，切尔诺伯格军警已经包围了盘踞在瓦舒克大道上的暴徒......
[name="电视主持人"]   可见，这一次无谋的袭击，将很快结束。
[name="电视主持人"]   请各位不要惊慌，待在屋中，等待切尔诺伯格的又一场胜利......
[name="电视主持人"]   乌萨斯的荣光保佑着陛下和他的人民！
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Image(fadetime=0)]
[Background(image="bg_cher_1",fadetime=1,screenadapt="coverall")]
[Blocker(a=0, fadetime=0.6, block=false)]
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]   ......
[Character]
[name="乌萨斯军警"]   可恶，他们，他们......那些武器和装备，究竟是哪里来的！
[name="乌萨斯军警队长"]   不要畏缩！就算穿上护甲，懦夫依旧是懦夫！不过是些缺乏训练的暴徒！
[name="乌萨斯军警"]   可是，可是他们的数量......！！
[name="乌萨斯军警队长"]   我们已经干掉了我们数量三倍之多的敌人！再干掉三倍的敌人，战斗就结束了！
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]   少口出狂言了，切尔诺伯格的混蛋！
[Character]
[name="乌萨斯军警队长"]   感染者渣滓，也配和我们为敌？！
[name="乌萨斯军警队长"]   逮捕你们和你们肮脏的爹妈时就该把你们全部当场处死，而不是流放和苦役！
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]   你们这些家伙......！！
[Character]
[name="乌萨斯军警"]   呃......！他们在冲击防线，前卫没法再支撑多长时间了！
[name="乌萨斯军警队长"]   为了陛下！给我顶住！！
[name="乌萨斯军警"]   我，我要......坚持不住了......！
[name="乌萨斯军警队长"]   退后的人，统统处死！
[name="乌萨斯军警"]   咳......
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_013_riop")]
[name="近卫干员"]  我们......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  待在这里别动！我们还不能暴露！
[Character(name="char_002_amiya_1#5")]
[name="阿米娅"]   乌萨斯的军警队伍......居然被整合运动压制住了？
[Character(name="char_002_amiya_1#5",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  哼......电视上播放的内容，和现实完全不一样。
[name="杜宾"]  切尔诺伯格当局，到了这个时候，还在耍这种手段吗。
[name="杜宾"]  不过，对于我们来说，事情也同样在变糟。指望通过更加隐秘的手段离开，已经不现实了。
[Character(name="char_002_amiya_1",name2="char_130_doberm_ex",focus=1)]
[name="阿米娅"]   糟糕的路况和敌人的封锁......我们已经没办法再利用载具分别行动了......
[Character(name="char_002_amiya_1",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  是的，救援小队只有在具备一定规模时，才能有效消灭盘踞在要道上的整合运动敌人。
[name="杜宾"]  再切分小队，只会是自取灭亡。
[Character(name="char_013_riop")]
[name="近卫干员"]  这些乌萨斯军警......
[name="近卫干员"]  即使他们的装备很精良，看起来也很有实力，但整合运动......
[name="近卫干员"]  无论是人数还是士气，都占压倒性的优势！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  和我们对切尔诺伯格进行初步侦察时完全不同......
[name="杜宾"]  在我们潜入时，切尔诺伯格军警与驻扎部队的数量、分布，以及状态，处在一个非常古怪的状态。
[name="杜宾"]  只是在那个时候，我们没办法确定原因而已。
[Character(name="char_013_riop")]
[name="近卫干员"]  难道整合运动，已经秘密地消灭了切尔诺伯格的大部分防卫力量吗？
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  没有任何证据可以证明，整合运动的力量真的庞大到如此地步，还能够谋划这么大规模的战略......
[name="杜宾"]  现在，我怕是只能庆幸，被包围的是那些军警，而不是我们。
[name="杜宾"]  当然，我们也必须提防四周的情况，等到陷入危机，就已经晚了——
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   ......博士，快召集各小队。
[name="阿米娅"]   侦查干员发现了整合运动，他们马上就要和我们的救援队伍接触了！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ——至少，我们现在的优势，也就只有谨小慎微这一点了。
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]   嗯？
[name="整合运动成员"]   这，这里也有武装力量？！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  各小队，作战准备！不要给他们反击的机会！
[Delay(time=0.3)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_00-02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Background(image="bg_cher_1",fadetime=1,screenadapt="coverall")]
[Delay(time=1)]
[character(name="char_013_riop")]
[name="近卫干员"]  哈，哈......
[name="近卫干员"]  整合运动还真是......精力旺盛！
[character]
[name="乌萨斯军警队长"]  你们，是什么人？
[name="乌萨斯军警队长"]  怎么会这个时候，出现在切尔诺伯格！
[character(name="char_013_riop")]
[name="近卫干员"]  哈？怎，怎么回事——
[character]
[name="乌萨斯军警队长"]  间谍吗！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  （如果泄露了身份，被乌萨斯当局盯上，后果不堪设想！）
[name="杜宾"]  （必要的话......！）
[character]
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   先生。
[character]
[name="乌萨斯军警队长"]  ——小女孩？
[name="乌萨斯军警队长"]  你......感染者？
[name="乌萨斯军警队长"]  别动！放下武器！
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.3, block=true)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  （做好防护准备，一旦对方有敌对倾向......）
[Blocker(a=0.3, r=0.95, g=0.95, b=0.95, fadetime=4, block=true)]
[name="杜宾"]  （烟雾？从哪里......）
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=1, crossfade=1.5)]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0.3, r=0.95, g=0.95, b=0.95, fadetime=0.3, block=true)]
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   先生，对我们抱有敌意的人究竟是谁，你应该很清楚！
[name="阿米娅"]   杜宾！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  重装干员！敌袭！
[character]
[name="乌萨斯军警队长"]  什，什么？！
[character(fadetime=0)]
[Dialog(fadetime=0)]
[PlaySound(key="$d_sp_ballista",volume=0.7)]
[Blocker(a=1, r=100, g=100, b=100, fadetime=0.1,block=true)]
[Blocker(a=0.3, r=0.95, g=0.95, b=0.95, fadetime=0.3, block=true)]
[Delay(time=1)]
[Character(name="char_1502_crowns",fadetime=0.5)]
[name="？？？"]  ......
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   ......整合运动。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  阿米娅，小心......
[name="杜宾"]  她和那些普通的感染者暴徒，不是一回事！
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[Character(fadetime=0)]
[Background(fadetime=0)]
[Blocker(a=0.3, r=0.95, g=0.95, b=0.95, fadetime=0.3, block=true)]
[Image(image="avg_1_1",x=0, y=-50, xScale=1.2, yScale=1.2, fadetime=1)]
[ImageTween(xFrom=0, yFrom=-50, xTo=0, yTo=0, xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1, yScaleTo=1, duration=10, block=false)]
[name="？？？"]  哼，逃跑......
[name="？？？"]  又能逃到哪里？
[name="？？？"]  去，撕碎他们。
[name="整合运动成员"]  ——————
[Blocker(a=1, r=0.95, g=0.95, b=0.95, fadetime=4, block=true)]
[Background(image="bg_cher_1", width=1, height=1, screenadapt="coverall")]
[Image]
[Blocker(a=0.3, r=0.95, g=0.95, b=0.95, fadetime=0.3, block=true)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  就连手下的整合运动成员也是一副训练有素的样子......
[name="杜宾"]  难道是，整合运动的头目吗？
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   雾气越来越浓了......想借助雾气发动奇袭吗？
[name="阿米娅"]   军警先生，我们必须立刻撤离这个区域！
[name="阿米娅"]   如果让他们封锁了我们的退路，我们就......
[Character]
[name="乌萨斯军警队长"]  ——
[name="乌萨斯军警队长"]  你们这些感染者，都给我滚。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   ......
[Character]
[name="乌萨斯军警队长"]  我得到的命令是防卫这条大街。
[name="乌萨斯军警队长"]  感染兔子，我不管你们来这里有什么目的，想干什么。
[name="乌萨斯军警队长"]  如果你们是来破坏我们的城市的，自然会有人惩罚你们。乌萨斯的愤怒是无休止的。
[name="乌萨斯军警队长"]  如果不是，那这里发生的事情，和你没有关系。
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   ——我知道了。
[Character]
[name="乌萨斯军警队长"]  每个乌萨斯人都知道，不把背脊朝向敌人。
[name="乌萨斯军警队长"]  快滚！我们没空理你们。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   ——
[name="阿米娅"]   谢谢。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   杜宾！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  走！去第一汇合点！
[name="杜宾"]  各小队！动作要快！快！
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0.3, r=0.95, g=0.95, b=0.95, fadetime=0.3, block=true)]
[Character(name="char_1502_crowns")]
[name="？？？"]  ......
[Character]
[name="乌萨斯军警队长"]  来啊！感染者混球！
[name="乌萨斯军警队长"]  你们就这点本事吗？只会站在那里看着吗？
[Character(name="char_1502_crowns")]
[name="？？？"]  切尔诺伯格人......
[name="？？？"]  该死。
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_00-04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第三关（前）
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Background(screenadapt="coverall", image="bg_cher_5",fadetime=1,screenadapt="coverall")]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Delay(time=1)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  Ace！
[Character(fadetime=0.5)]
[Character(name="char_014_riope" ,fadetime=0.6)]
[delay=0.65]
[Character(name="char_014_riope" )]
[name="Ace"]  看来，你们都平安无事。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  这里还没到汇合点......怎么只有你一个人？
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.3, block=true)]
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]   他们就是那些从核心区出逃的人！别放他们走！
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.3, block=true)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  呿，穷追不舍！
[name="杜宾"]  E2小队，应敌——
[Character(name="char_014_riope")]
[name="Ace"]   杜宾，不要恋战，优先后撤！
[name="Ace"]   阿米娅，Dr.{@nickname}！快！
[Character]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  这里也不安全。
[Character(name="char_014_riope")]
[name="Ace"]  是的，我们还要继续向下一个汇合点移动。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  你的小队呢？
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.3, block=true)]
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]   藏到哪去了？把他们找出来！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  又来了吗！
[Character(name="char_014_riope")]
[name="Ace"]  Dr.{@nickname}，请下命令吧。
[name="Ace"]  就像以前那样。
[Decision(options="......？", values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   啊，Ace......
[name="阿米娅"]   其实有些，小小的变故。
[name="阿米娅"]   博士......意外失去了记忆。
[Character(name="char_002_amiya_1#4",name2="char_014_riope",focus=2)]
[name="Ace"]   ......原来如此。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   抱歉，Ace......事情和以前相比，有不小的区别。
[Character(name="char_002_amiya_1#4",name2="char_014_riope",focus=2)]
[name="Ace"]   是吗。你没必要向我道歉。
[name="Ace"]   博士的指挥能力，有没有因为失忆受到影响？
[Character(name="char_002_amiya_1",name2="char_014_riope",focus=1)]
[name="阿米娅"]   ......和以前一样。
[name="阿米娅"]   博士的决策依旧十分可靠，我保证。
[Character(name="char_002_amiya_1",name2="char_014_riope",focus=2)]
[name="Ace"]   那就好。我听从博士的指挥。
[name="Ace"]   失去了的东西是可以找回来的。
[name="Ace"]   眼下有更棘手的问题等着我们去解决。
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.3, block=true)]
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]   他们在这儿！快，快攻击！！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  聊天还没结束？我已经开始战斗了！
[Character(name="char_014_riope" )]
[name="Ace"]   Dr.{@nickname}，请下命令吧。
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]   放，把那些畜生放出来，让他们尝尝被撕咬的滋味！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  博士！Ace！敌人近在眼前了！
[Character(name="char_014_riope" )]
[name="Ace"]   ——
[Decision(options="立刻出动！;......好的。;趁现在，破坏敌人的计划吧。", values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_014_riope" )]
[name="Ace"]   明白。
[name="Ace"]   E3小队！支援杜宾！
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=1, crossfade=1.5)]
[character(fadetime=0)]
[Dialog(fadetime=0)]
[PlaySound(key="$d_sp_ballista",volume=0.7)]
[Blocker(a=1, r=100, g=100, b=100, fadetime=0.1,block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
[CameraShake(duration=1.5, xstrength=7, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[name="整合运动成员"]   埋伏？！！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   E3小队......一直隐藏着行踪，就是等着和我们配合，夹击敌人吗。
[Character(name="char_014_riope" )]
[name="Ace"]   在通讯受到干扰的情况下，小队应该在汇合点附近行动，这样，即使是我或者侦查干员发生了意外......
[name="Ace"]   整体的撤退计划，依然能够正常实施。这是我的判断。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  也就是说，Ace你把小队留在汇合点，一个人......
[Character(name="char_014_riope" )]
[name="Ace"]   毕竟最重要的，是去除汇合点周围的威胁。
[name="Ace"]   优先确认你们的状况是一种冒险。我不能带上整个小队一起。
[name="Ace"]   小队存在的目的，本来就是为了让战术更有效，而不是固步自封，成为拖累。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  哈。接下来，用实战去解决了整合运动再说吧！
[Character(name="char_014_riope" )]
[name="Ace"]   阿米娅，拜托你。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   知道了！我会辅佐博士，通过法术支援你们的！
[Character(name="char_014_riope" )]
[name="Ace"]   终于......
[name="Ace"]   Dr.{@nickname}，请你，指挥罗德岛。
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_00-06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第三关（后）
[Background(image="bg_cher_5",fadetime=1,screenadapt="coverall")]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Delay(time=1)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  哈，哈......
[name="杜宾"]  整合运动这帮丧心病狂的家伙！居然用，居然用......
[Character(name="char_013_riop",name2="char_002_amiya_1",focus=1)]
[name="近卫干员"]  那些野兽......
[name="近卫干员"]  是，是整合运动，布置的吗......
[Character(name="char_013_riop",name2="char_002_amiya_1",focus=2)]
[name="阿米娅"]   感染的野兽，被整合运动当做士兵驱使......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  不，那不只是野兽那么简单。
[name="杜宾"]  我能感受到，那种......
[name="杜宾"]  那不是单纯的野兽，它们比起野兽，更像我们......
[Character(name="char_013_riop")]
[name="近卫干员"]  杜宾教官......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ......
[Character(name="char_013_riop")]
[name="近卫干员"]  头儿......我们，该怎么办？
[Character(name="char_014_riope",name2="char_013_riop",focus=1)]
[name="Ace"]   帮它们从痛苦中解脱。
[Character(name="char_014_riope",name2="char_013_riop",focus=2)]
[name="近卫干员"]  头儿......
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_130_doberm_ex",name2="char_014_riope",focus=2)]
[name="Ace"]   战斗已经结束了，杜宾。
[name="Ace"]   我们同样也和整合运动发生了冲突。
[name="Ace"]   天灾已经盘旋在我们头顶，随时都可能坠落。
[name="Ace"]   即使是切尔诺伯格城，在天灾的直接冲击下，也会化作一摊废墟。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   整合运动在这个时候闹事，确实会制造更大的混乱。
[Character(name="char_130_doberm_ex",name2="char_014_riope",focus=2)]
[name="Ace"]   杜宾，没时间了。
[name="Ace"]   罗德岛能躲过整合运动的袭击，也能瞒着乌萨斯帝国行动，但面对天灾，我们终归是脆弱的。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ......
[name="杜宾"]  够了，走吧。
[name="杜宾"]  无论整合运动的计划有多疯狂，对于我们来说......
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   各位的安全才是最重要的。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  是。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   整合运动的领袖，可能把这次的事件看作一个标志，一种手段......
[name="阿米娅"]   对我来说，只是罗德岛的处境，变得越来越危险。
[Character(name="char_002_amiya_1",name2="char_014_riope",focus=2)]
[name="Ace"]   在这个时间点挑起事端——
[name="Ace"]   整合运动不是足够狠毒，就是足够疯狂。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  也许，两者兼有。
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_00-07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第四关（前）
[Background(screenadapt="coverall", image="bg_cher_5", width=1, height=1, fadetime=1)]
[PlayMusic(intro="$mist_loop", key="$mist_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   ——天空越来越暗淡了。
[name="阿米娅"]   天际线仿佛被云层捏住了一样......
[name="阿米娅"]   明明空气很通透，乌云却静止不动，好像在把各处的压抑感通通抽出，凝聚在一处。
[name="阿米娅"]   连风都停下了......
[Character(name="char_002_amiya_1",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  天灾确实，即将降临在这座城市。
[name="杜宾"]  看来，切尔诺伯格已经被整合运动彻底瘫痪了。
[name="杜宾"]  不过，哪怕是要拆分移动城市，也应该提前数周就完成准备工作。
[name="杜宾"]  难道在那时候，整合运动就......？
[Character(name="char_014_riope",name2="char_013_riop",focus=1)]
[name="Ace"]   不太现实。
[name="Ace"]   现在的整合运动，并没有体现出秘密接管所需要的精英部队素质。
[Character(name="char_014_riope",name2="char_013_riop",focus=2)]
[name="近卫干员"]   整合运动的大多数成员......不过是在街头游荡，向切尔诺伯格人寻仇。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   仅仅是在各处重复着杀戮和战斗，使整个城市陷入战火。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  天灾降临时，就连无比坚固的切尔诺伯格都会被撕得粉碎——
[name="杜宾"]  变成布满源石的巨型废墟。
[name="杜宾"]  无论整合运动想要的是资源还是名望，都只会一败涂地。
[Character(name="char_002_amiya_1",name2="char_130_doberm_ex",focus=1)]
[name="阿米娅"]   他们真能和乌萨斯军方正面对抗吗？即使乌萨斯的指挥系统陷入了混乱......
[name="阿米娅"]   乌萨斯的军事力量，怎么还没有集结反攻？
[Character(name="char_002_amiya_1",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  从我的经验来说，一般暴乱发生后，不出片刻，暴徒就会被全副武装的军警清剿。
[name="杜宾"]  虽然，我们刚才也见证了一小撮军警被整合运动围攻的景象......
[Character(name="char_002_amiya_1",name2="char_130_doberm_ex",focus=1)]
[name="阿米娅"]   ......
[Character(name="char_002_amiya_1",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  那个蒙面的整合运动头目，即使是有一点不同......但她也没有能够吞没一城的水平。
[name="杜宾"]  除非......
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   除非什么？
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  我以前经历的战争中......
[name="杜宾"]  也有行为与整合运动的掌控者如出一辙的领袖。
[name="杜宾"]  于他而言，士兵不过是棋子，达到目的后就可以随意丢弃。
[name="杜宾"]  既合理高效地运用兵力，又在不需要的时候放纵其自生自灭......
[name="杜宾"]  因为训练与管理的成本太高了。
[Character(name="char_014_riope" )]
[name="Ace"]   所以，他只是放养他们？
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  对。大多数时候，他只要把仇恨和恐慌当做口粮，喂养他们......
[name="杜宾"]  只需在必要时，轻轻地推一下——追随者就会振臂高呼。
[name="杜宾"]  如果整合运动的运作，真如他们宣传的那般......
[Character(name="char_013_riop")]
[name="近卫干员"]   唔......
[name="近卫干员"]   穿上衣服，戴上标志，所有的感染者都可以是整合运动？
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  是的。
[name="杜宾"]  他们确实......将源源不断。
[name="杜宾"]  被压迫、想要呼喊的感染者太多了。这时候，无论整合运动给出的是怎样的出路......
[name="杜宾"]  只要在铁屋子上钻个口，哪怕外面就是一片火海，里面的人依然会互相推搡着探出身子。
[Character(name="char_016_medic")]
[name="医疗干员"]   唔......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  Dr.{@nickname}.
[name="杜宾"]  这和你我不同。即使我还没有完全信任你，但至少我信任你的能力。
[Decision(options="......", values="1")]
[Predicate(references="1")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  与你完全不同......
[name="杜宾"]  这种领袖并不是指挥官。
[name="杜宾"]  践踏敌人，同时也践踏同伴，又或者说，“随从”，的生命。
[name="杜宾"]  也许连随从都算不上，整合运动的暴徒，不过是领袖的棋子。
[name="杜宾"]  这样的人，是暴君。
[Character(name="char_014_riope" ,name2="char_130_doberm_ex",focus=1)]
[name="Ace"]   无论敌人是谁，我们都会完成任务。
[name="Ace"]   以前有人训导过我和我的队友——
[name="Ace"]   “如果是棋子，那就吃掉；如果是堡垒，那就攻陷；如果是王权，那就推翻”。
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=1, crossfade=1.5)]
[Character(name="char_014_riope" ,name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  Ace......稍等一下。
[Character(name="char_014_riope" )]
[name="Ace"]   Dr.{@nickname}，正前方，盘踞着敌人的轻装甲部队。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   我们被发现了吗？
[Character(name="char_014_riope" )]
[name="Ace"]   还没有。
[Character(name="char_014_riope" ,name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  但是......
[Character(name="char_014_riope" ,name2="char_130_doberm_ex",focus=1)]
[name="Ace"]   我们避不开。这是这条路径中的最短路线，如果我们迂回，就会损失时间。
[Character(name="char_014_riope" ,name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  那没什么好说的了。无论他们是棋子还是暴徒，只要从战场上赶出去就好！
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_00-07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第四关（后）
[Background(image="bg_cher_5", width=1, height=1, fadetime=1)]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Delay(time=1)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Delay(time=1)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  依照既定路线，我们已经很接近切城南边的中城区了。
[name="杜宾"]  穿过这个公园，就是汇合点。不出意外的话，临光和E4小队应该已经在那里等着我们了。
[Character(name="char_013_riop",name2="char_130_doberm_ex",focus=1)]
[name="近卫干员"]   可是......
[name="近卫干员"]   要是临光......被袭击了，会怎么样？
[name="近卫干员"]   要是他们原本想用通讯设施警告我们，却发现信号遭到干扰......
[name="近卫干员"]   我们该怎么办？
[Character(name="char_013_riop",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  ......
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   我们会去确认。
[character(name="char_013_riop")]
[name="近卫干员"]   ......啊。
[Character(name="char_014_riope",name2="char_013_riop",focus=1)]
[name="Ace"]   我们要亲眼确认事件之后，才会做出揣测。
[name="Ace"]   不要用怀疑恐吓自己。
[Character(name="char_014_riope",name2="char_013_riop",focus=2)]
[name="近卫干员"]   明，明白了......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  失去联络手段所带来的恐慌情绪，比想象中蔓延得快得多......
[name="杜宾"]  特别是......在这个天灾仿佛近在眼前的时候。
[name="杜宾"]  我们得赶紧加快速度了。
[Dialog]
[Blocker(a=0.3, r=0.95, g=0.95, b=0.95, fadetime=4, block=true)]
[Character(name="char_002_amiya_1#5")]
[name="阿米娅"]    ......
[name="阿米娅"]    欸......这阵雾气......？
[name="阿米娅"]   ——难道——
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   小心！！
[Character(name="char_1502_crowns")]
[name="？？？"]  干掉他们。
[Dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=1, crossfade=1.5)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  敌军的射击！！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   这是陷阱......！
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.3, block=true)]
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]   ————！！
[character(name="char_013_riop")]
[name="近卫干员"]   不好，我们的后方也出现了整合运动的追兵......！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   侦查干员呢！
[character(name="char_013_riop")]
[name="近卫干员"]   被战场分割了！
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.3, block=true)]
[Character(name="char_1502_crowns")]
[name="？？？"]  罗德岛......
[name="？？？"]  追上你们了。
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]   ——！
[name="整合运动成员"]   杀！！
[Character(name="char_1502_crowns")]
[name="？？？"]  这次，就让你们粉身碎骨。
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.3, block=true)]
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   杜宾！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  狙击干员！压制敌人的冲锋！
[name="杜宾"]  重装干员，防御姿态，随时准备向前顶上！
[name="杜宾"]  Ace，准备————
[Character(fadetime=0)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_1507_Mephisto_1#6",fadetime=2)]
[stopmusic(fadetime=2)]
[name="？？？"]  等一下，等一下——
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   ？！
[Character(name="char_1507_Mephisto_1#6")]
[name="？？？"]  在清剿了东南要塞之后，我一听到你的消息，可是立刻就赶过来了。
[name="？？？"]  这里已经是我的处理范围咯，弑君者。
[Character(name="char_1502_crowns")]
[name="弑君者"]  ......
[name="弑君者"] 你来做什么？
[Character(name="char_1507_Mephisto_1#6")]
[name="？？？"]  该把他们，交给我了吧？
[Delay(time=0.3)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_00-08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第五关（前）
[Background(image="bg_cher_5", width=1, height=1, fadetime=1)]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Delay(time=1)]
[Character(name="char_1507_Mephisto_1#6",name2="char_1502_crowns#1",focus=2)]
[name="弑君者"]    ......
[name="弑君者"]    梅菲斯特？
[Character(name="char_1507_Mephisto_1#6",name2="char_1502_crowns#1",focus=1)]
[name="？？？"]    你没有拒绝的理由吧？一些不小心飞进来的小虫子......值得你亲自追击吗？
[name="？？？"]    我的部队已经接到了你的情报，你已经尽到了你的责任。
[name="？？？"]    接下来，请你回去吧。毕竟你负责的是核心能源区及其外围......
[Character(name="char_1507_Mephisto_1#6",name2="char_1502_crowns#1",focus=2)]
[name="弑君者"]    少做多余的事......！
[Character(name="char_1507_Mephisto_1#6",name2="char_1502_crowns#1",focus=1)]
[name="？？？"]    你还有其他事情要做，对吧？
[Character(name="char_1507_Mephisto_1#6",name2="char_1502_crowns#1",focus=2)]
[name="弑君者"]    ——
[name="弑君者"]    好。随便你。
[name="弑君者"]    我已经等不及要观赏你的惨败了。
[Character(name="char_1507_Mephisto_1#6",name2="char_1502_crowns#1",focus=1)]
[name="？？？"]    哦......
[Character(name="char_1502_crowns#1")]
[name="弑君者"]    收队。
[PlaySound(key="$d_gen_walk_n")]
[Character(fadetime=0.6)]
[delay(time=1)]
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]  ——
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Character(fadetime=0.6)]
[delay(time=1)]
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]    ......敌人的头目......带着一部分整合运动的部队，撤离了？
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    这小子，在做什么？
[name="杜宾"]    不能放松警惕......敌人的数量，依然是我们的数倍之多！
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_1507_Mephisto_1#6")]
[name="？？？"]    唉唉，弑君者的口气一直不是很礼貌，请允许我代她道歉。
[Character]
[delay=1]
[Character(name="char_1507_Mephisto_1#1",fadetime=1)]
[Delay(time=1)]
[name="梅菲斯特"]    你们可以称呼我，梅菲斯特。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    你们整合运动，究竟要做什么？
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]    也没什么。其实，放你们离开也无所谓。毕竟刚开始，你们也不算是整合运动的目标。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]    既然我们不是整合运动的目标，那为什么......
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]    不过，我有幸观赏了你们的战斗。
[name="梅菲斯特"]    你们的作战方式和你们的人员配置，很有趣哦。
[Character(name="char_016_medic")]
[name="医疗干员"]    ......有趣？
[name="医疗干员"]    说战场的厮杀......有趣？
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]    罗德岛......我看过你们的资料。
[name="梅菲斯特"]    原本，我只把你们当作是普通企业。
[name="梅菲斯特"]    现在看来，你们所涉猎的，可远远超出了摆弄试管的范畴哦？
[name="梅菲斯特"]    要是让你们轻轻松松地离开，就没什么意思了吧？
[name="梅菲斯特"]    我想和各位，来一场祭祀式的竞赛。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    ......我们没工夫和心智不全的小孩子浪费时间。
[name="杜宾"]    （阿米娅，准备好，我们可能要强行突围了。）
[name="杜宾"]    （我来吸引他的注意力......！）
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]    （啊，嗯！）
[Character(name="char_130_doberm_ex")]
[dialog]
[PlaySound(key="$d_gen_signalbomb")]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0, block=true)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.3, block=true)]
[delay(time=2.2)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0, block=true)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=1, block=true)]
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]    ......刚刚那是什么？你是向谁，打了什么信号吗？
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    与你无关，小子。
[name="杜宾"]    （阿米娅？）
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]    哎呀，都是些企业人士了，连谈话时要注意礼节这个道理，都不明白吗？
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    就是因为这世界上像你这样的人越来越多，才导致我不得不多学些能够形容你们的词汇！
[name="杜宾"]    （阿米娅，发生什么了？）
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]    （杜宾......我们的撤退路线，都被他的部队封锁了！）
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    （怎么会！短短几分钟内，他——）
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]    这样不好。
[name="梅菲斯特"]    我诚心诚意地邀请你们......
[name="梅菲斯特"]    你们却只想着——
[Character(name="char_1507_Mephisto_1#5")]
[name="梅菲斯特"]    ——逃之夭夭？
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    呿！
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]    其实，只要你们赢了，就可以安全地离开我的猎场。
[name="梅菲斯特"]    接下来，我的这些朋友们，会不断地尝试杀掉你们。
[Character(name="char_1507_Mephisto_1#5")]
[name="梅菲斯特"]    你们只要活下来，就是胜利！怎么样，规则，很简单吧？
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    Ace！
[Character(name="char_014_riope" )]
[name="Ace"]    已经做好了强行突围的准备！
[name="Ace"]    但我们要先扛过这次围攻！
[Character(name="char_002_amiya_1#7",name2="char_1507_Mephisto_1#1",focus=1)]
[name="阿米娅"]    ——
[name="阿米娅"]    为什么，明明天灾就要来了！再不撤出切城，所有人都会——
[Character(name="char_002_amiya_1#7",name2="char_1507_Mephisto_1#1",focus=2)]
[name="梅菲斯特"]    你在说什么......
[Character(name="char_1507_Mephisto_1#5")]
[name="梅菲斯特"]    正因为是天灾降临......这可是，一个最该被好好庆祝的时刻了呀。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]    ......你......
[Character(name="char_1507_Mephisto_1#5")]
[name="梅菲斯特"]    我高贵的客人们，能邀请你们参加游戏，我感到十分荣幸。
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_2")]
[name="整合运动成员"]    啊......啊......！
[name="整合运动成员"]    杀......杀！！杀了......他们！！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    阿米娅！小心！
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]    对了，对了......
[name="梅菲斯特"]    其实，我们是知道你们在核心区里做了什么的。
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]    ——！
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]    那个你们从核心区里救出来的，一直遮住面庞的家伙......令人非常，非常在意呢。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]    ——？！
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]    弑君者只关心你们之后要做什么，要去哪里。
[name="梅菲斯特"]    我不一样。我只关心......
[name="梅菲斯特"]    你，是什么？从哪里来？
[name="梅菲斯特"]    对，你，就是现在，盯着我看的你......你和我们有点不一样。
[name="梅菲斯特"]    那个设施里，究竟是什么装置，有着保存生命的功能呢？
[name="梅菲斯特"]    我非常，非常好奇。
[name="梅菲斯特"]    我也不是那种冷血的人......
[name="梅菲斯特"]    来吧，罗德岛的客人们，把这个家伙当成见面礼留给我吧？
[name="梅菲斯特"]    那样的话，虽然令人惋惜，但我放你们离开，也是可以的哦？
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]    博士——
[name="阿米娅"]    ——退到我身后！！
[Delay(time=0.3)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_00-09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第五关（后）
[Background(image="bg_cher_5", width=1, height=1, fadetime=1)]
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=1, crossfade=1.5)]
[Delay(time=1)]
[Character(name="char_1002_nsabr_2")]
[PlaySound(key="Sound_Beta_2/Enemy/e_skill/e_skill_skulsrsword", volume=0.6)]
[CameraShake(duration=1, xstrength=6, ystrength=10, vibrato=50, randomness=90, fadeout=true)]
[Blocker(a=1, r=1, g=1, b=1,fadetime=0.2, block=true)]
[Blocker(a=0, r=0, g=0, b=0,fadetime=0.2, block=true)]
[Delay(time=0.6)]
[Dialog]
[Character]
[Character(name="char_016_medic")]
[name="医疗干员"]   咿——！
[Character(name="char_013_riop", name2="char_016_medic", focus=1)]
[name="近卫干员"]  小心！！
[Character(name="char_013_riop", name2="char_016_medic", focus=2)]
[name="医疗干员"]  我没事，只是擦伤而已，不要紧......
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  还不够......再这样下去，包围圈会越来越小。
[Character(name="char_002_amiya_1#7", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]  我们已经找到了可突破口，但没有增援，我们只能采取守势，没法突围！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  ......请再坚持一下！优先用火力压制敌方射手！
[name="阿米娅"]  敌人的先锋，就由我们术师来处理！
[Dialog]
[Character]
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]  没错，没错！就该这样！接下来，f3，e5！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   可憎的小子......！
[Dialog]
[Character]
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]  很好！那么，b4，b5！
[character(name="char_013_riop")]
[name="近卫干员"]  敌人正在向我们侧后方迂回！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  调两位重装干员和一位狙击干员！只要能牵制他们就足够了！
[Dialog]
[Character]
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]  之后！h2，h6！
[Character(name="char_016_medic")]
[name="医疗干员"]   他们，他们在冲击我们的阵线！
[Character(name="char_014_riope")]
[name="Ace"]   近卫干员，把敌人赶出掩体！
[Dialog]
[Character]
[Character(name="char_1507_Mephisto_1#1")]
[name="梅菲斯特"]  没错，再让我多看一会儿，你们挣扎的样子！
[name="梅菲斯特"]  现在，术师，c7，吃掉敌人的战车吧！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  敌人的术师现身了......！之前，一直躲在重装干员身后吗！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   来不及了！趴下！
[character]
[Dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Delay(time=0.5)]
[Character(name="char_016_medic")]
[name="医疗干员"]   呜啊啊啊！
[character(name="char_013_riop")]
[name="近卫干员"]  咳......
[Character(name="char_1507_Mephisto_1#5")]
[name="梅菲斯特"]  然后就去死吧，就像雨夜中的火星一样！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  他，是在指挥自己的队伍吗......！仅仅运用象棋走法，就能下达精准的命令？
[name="阿米娅"]  明明都是些狂暴的感染者，战斗却完全由他一人指挥......！
[name="阿米娅"]  再这样下去，他会把指挥优势发挥到极致——
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   相应的，只要能压制他的话，也就没什么大不了！
[name="杜宾"]   不要让整合运动打开哪怕一丁点缺口！
[name="杜宾"]   混账，我们的时间越来越少了！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  不能再让整合运动拖延我们的脚步了！
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[name="阿米娅"]  有什么，有什么办法能迅速打开局面吗......！
[name="阿米娅"]  如果继续拖下去，博士和大家就......！
[Character(fadetime=0)]
[stopmusic(fadetime=1)]
[Dialog]
[playsound(key="$p_imp_blunt_h")]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=1, r=0.95, g=0.95, b=0.95, fadetime=0.2, block=true)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="整合运动成员"]  唔唔唔唔唔啊啊啊！！！
[Character(name="char_1507_Mephisto_1#2")]
[name="梅菲斯特"]  什么？
[name="梅菲斯特"]  ......唔唔......怎么回事？怎么有人被......撞飞起来了？
[name="梅菲斯特"]  这......
[name="梅菲斯特"]  ......什么啊？
[Character(name="char_148_nearl_1#5")]
[name="？？？"]   你们的速度比我估算的慢上太多了，我可是连平民都顺手安顿好了。
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]  ——？！！
[Character(name="char_148_nearl_1#5")]
[name="？？？"]   别挡道！
[Character(fadetime=0)]
[playsound(key="$p_imp_blunt_h")]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=1, r=0.95, g=0.95, b=0.95, fadetime=0.2, block=true)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlayMusic(intro="$m_bat_game02_intro", key="$m_bat_game02_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_2")]
[name="整合运动成员"]  呜啊！
[Character(name="char_148_nearl_1#5")]
[name="？？？"]   加大进攻力度！别给敌人重整阵形的机会！
[playsound(key="$p_imp_blunt_h")]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=1, r=0.95, g=0.95, b=0.95, fadetime=0.2, block=true)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.8)]
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]  临光小姐！！
[Character(name="char_148_nearl_1#5")]
[Character(name="char_148_nearl_1#1",fadetime=1,block=true)]
[Delay(time=0.3)]
[name="临光"]  我在。
[name="临光"]  你没事就好，阿米娅。快撤。
[PlaySound(key="$d_gen_soldiersrun",volume=0.8)]
[Character(name="char_130_doberm_ex", name2="char_148_nearl_1", focus=1)]
[name="杜宾"]   幸亏这次作战，有你参加。
[Character(name="char_130_doberm_ex", name2="char_148_nearl_1", focus=2)]
[name="临光"]  信号弹的定位很有效。看来你们遇到的麻烦确实不小。
[Character(name="char_148_nearl_1#1")]
[name="临光"]  ——
[name="临光"]  您就是{@nickname}博士吧？
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="char_148_nearl_1#1")]
[name="临光"]  耀骑士临光，前来迎接你们了。
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_00-10_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第六关（后）
[Background(image="bg_cher_5", width=1, height=1, fadetime=1)]
[PlayMusic(intro="$m_bat_game02_intro", key="$m_bat_game02_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Delay(time=1)]
[Character(name="char_1507_Mephisto_1#4")]
[name="梅菲斯特"]   这女人......怎么回事......
[Dialog]
[Delay(time=0.6)]
[Character(name="char_148_nearl_1")]
[name="临光"]   ————你。
[name="临光"]   制压切尔诺伯格军事据点的整合运动像机器一样高效——
[name="临光"]   而你领着的这批各个都像神经错乱的暴徒。
[name="临光"]   屠杀，纵火，围猎......只不过是为了满足你自己残忍的趣味而已吧？
[name="临光"]   会在这时煽动如此不堪之事的人，没可能策划出足以击溃整座城市的方案。
[name="临光"]   你的指挥官大概是命令你制造混乱，而你，顺应着自己低劣的品味肆意妄为。
[Character(name="char_1507_Mephisto_1#2")]
[name="梅菲斯特"]   ——
[name="梅菲斯特"]   ——浮士德。
[name="梅菲斯特"]   把她那张嘴给我打穿。
[Character(name="char_1508_Faust_1#2")]
[name="浮士德"]   ......
[Character(name="char_148_nearl_1#4")]
[name="临光"]   ！
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[Delay(time=1)]
[Character(name="char_148_nearl_1#3")]
[name="临光"]   咳，咳......
[Character(name="char_002_amiya_1#7 ")]
[name="阿米娅"]  临光！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  敌人的狙击手......很强！
[name="杜宾"]  临光再被击中的话，一定会失去防御能力！
[Character(name="char_002_amiya_1#7 ")]
[name="阿米娅"]  临光，快退后！
[Character(name="char_148_nearl_1#3")]
[name="临光"]   不行......威力太大了。如果击中我方小队，后果不堪设想。
[name="临光"]   我必须防住他的炮火！
[Character(name="char_1507_Mephisto_1#2")]
[name="梅菲斯特"]  挡开了浮士德的弩炮？凭盾牌——？！
[Character(name="char_1507_Mephisto_1#3")]
[name="梅菲斯特"]  不可能......不可能！
[name="梅菲斯特"]  再来！！把她......打成碎渣！
[Character(name="char_1508_Faust_1#2")]
[name="浮士德"]    ————！
[Character(name="char_148_nearl_1#3")]
[name="临光"]  居然......右侧？！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  糟了！快闪开————
[Character(name="char_014_riope" )]
[name="Ace"]  不会让你得逞！
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[Delay(time=1)]
[Character(name="char_002_amiya_1#7 ")]
[name="阿米娅"]  Ace！
[Character(name="char_014_riope")]
[name="Ace"]   狙击干员，准备！
[name="Ace"]   ——目标，南侧高台，齐射！
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[PlaySound(key="$e_atk_arrow_h")]
[Character(name="char_1508_Faust_1#2")]
[name="浮士德"]   ......！
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_1507_Mephisto_1#3")]
[name="梅菲斯特"]  什么！你们居然敢，居然敢......！
[Dialog]
[Character]
[Character(name="char_002_amiya_1#7 ")]
[name="阿米娅"]  打中了吗？
[Character(name="char_014_riope" )]
[name="Ace"]  没那么容易，这只能......稍稍压制他而已。
[name="Ace"]  没时间再去了解敌人的构成了！
[Character(name="char_014_riope",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  兼具机动性和威力，越拖下去，我们安全挡下他弩弹的几率就越小！
[Character(name="char_148_nearl_1#3")]
[name="临光"]  别给他喘息的机会......！趁着E3小队狙击干员干扰他们的时候，阿米娅！
[Character(name="char_002_amiya_1#7 ")]
[name="阿米娅"]  了解！
[name="阿米娅"]  E1小队射手，和我一起，压制整合运动！
[name="阿米娅"]  E2小队，用最大火力，撕开整合运动的防线！
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.3, block=true)]
[Character(name="char_1507_Mephisto_1#4")]
[name="梅菲斯特"]  你们这些家伙......
[name="梅菲斯特"]  为什么不肯老老实实地去死？
[name="梅菲斯特"]  你们的命运，为什么就不能在这里落下帷幕？
[name="梅菲斯特"]  ——————我要把你们，通通————
[Character(name="char_014_riope" )]
[name="Ace"]  临光，趁现在，快！
[Character(name="char_148_nearl_1#3")]
[name="临光"]   E4全体，随我冲击敌方阵形！
[name="临光"]   一次性击溃前方的阻挡目标！
[name="临光"]   狂奔起来！！
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]  射击！射击！别让她靠近......
[name="整合运动成员"]  啊......？
[name="整合运动成员"]  啊？？她刚刚不是还在二十米之外......
[name="整合运动成员"]  咕咳——唔啊啊啊啊！
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[playsound(key="$p_imp_blunt_h")]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[Delay(time=1)]
[Character(name="char_148_nearl_1#3")]
[name="临光"]   想要对抗卡西米尔骑士——再去训练个几十年再说！
[Character(name="char_148_nearl_1#3",name2="char_130_doberm_ex",focus=1)]
[name="临光"]   杜宾！跟上我！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  了解！
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_00-11_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第六关（后）
[Background(image="bg_cher_1", width=1, height=1, fadetime=1)]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Delay(time=1)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  侦查完毕，确认敌追击部队已被我方全歼。
[name="杜宾"]  我们成功突围，现在已经基本脱离了切尔诺伯格上城区。
[Character(name="char_014_riope", name2="char_130_doberm_ex", focus=1)]
[name="Ace"]    虽然我们消灭的，只是包围阵势中一小部分的兵力......
[name="Ace"]    但至少，我们暂时安全了。
[Character(name="char_014_riope", name2="char_148_nearl_1", focus=2)]
[name="临光"]  谢谢你刚才的援助，临光不会忘记这份恩情。
[Character(name="char_014_riope", name2="char_148_nearl_1", focus=1)]
[name="Ace"]    请别这么说。我可没资格让耀骑士还我人情。
[name="Ace"]    说说刚才那个狙击手吧，临光。
[Character(name="char_014_riope", name2="char_148_nearl_1", focus=2)]
[name="临光"]  好。
[name="临光"]  除却那把弩炮巨大的威力——
[name="临光"]  我认为......他可能预设了其他火力点，以及自动射击器械。
[name="临光"]  我遭到了交叉火力的射击......我们却只观测到了一个狙击手。
[Character(name="char_014_riope", name2="char_148_nearl_1", focus=1)]
[name="Ace"]    我也有同样感觉。
[name="Ace"]    第一发弹药和第二发弹药爆炸的时间点虽然非常接近，实际上却有着有相当微妙的时差。
[name="Ace"]    那并不是连射弩弦的功劳。至少，我发动火力压制时，对抗的，并不是第一位狙击手。
[Character(name="char_014_riope", name2="char_148_nearl_1", focus=2)]
[name="临光"]   ——你意识到了什么，Ace？
[Character(name="char_014_riope", name2="char_148_nearl_1", focus=1)]
[name="Ace"]    说不准。如果敌人不是飞速地移动......就是同时存在于许多地方。
[Character(name="char_014_riope", name2="char_148_nearl_1", focus=2)]
[name="临光"]  敌人狙击手的机动性......怎么也不可能达到这种程度。我不能想象这样的移动手段。
[name="临光"]  整合运动比我认知中更加危险。
[Character(name="char_130_doberm_ex",name2="char_148_nearl_1", focus=1)]
[name="杜宾"]  是那个凶狠的臭小子下令狙击你的。他在指挥围攻我们的时候，甚至没动用狙击手的力量......
[Character(name="char_130_doberm_ex",name2="char_148_nearl_1", focus=2)]
[name="临光"]  看来那么恶劣的性格，是有同样危险的力量支撑着的。
[Character(name="char_014_riope", name2="char_148_nearl_1", focus=1)]
[name="Ace"]    但他一直没有出手，哪怕是在暴怒的情况下。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  要么，在战斗上他是个废物；要么，现在还不到他展现实力的时候。
[name="杜宾"]  当然，他展现出的指挥能力......已经很令人怀疑了。
[name="杜宾"]   他的部队，就像是完全被他操纵着一样......
[Character(name="char_148_nearl_1#1")]
[name="临光"]   不管怎么说，我们已经脱离了他的控制区域。
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]  临光......谢谢你。
[name="阿米娅"]  没有你及时赶到的话，我们很可能就要深陷危机了。
[Character(name="char_002_amiya_1#1", name2="char_148_nearl_1#1", focus=2)]
[name="临光"]  这都是我们战前的作战计划的方针而已。
[name="临光"]  让我和Ace他根据局势采取不同计划的，是你。
[name="临光"]  是你解决了自己的问题。
[name="临光"]  一路上，我看到了整合运动的暴行，也对他们的实力产生过怀疑。
[name="临光"]  如果我在那时，停下来去与他们战斗呢？
[name="临光"]  如果我去帮助乌萨斯人抵御整合运动呢？
[name="临光"]  如果我原地坚守，只是等着你们撤退到我面前呢？
[Character(name="char_002_amiya_1#1", name2="char_148_nearl_1#7", focus=2)]
[name="临光"]  ——如果按照我自己的想法来做，也许会招致更糟的后果。
[name="临光"]  我不擅长预见，不断战斗是我达到目的的方式。
[Character(name="char_002_amiya_1#1", name2="char_148_nearl_1#1", focus=2)]
[name="临光"]  所以，阿米娅，你有自己解决危机的实力，而我只是履行了自己的职责。
[name="临光"]  这是你通过自己的努力摘下的果实，再自信点。
[Character(name="char_002_amiya_1#1", name2="char_148_nearl_1#1", focus=1)]
[name="阿米娅"]  临光小姐......
[Character(name="char_002_amiya_1#1", name2="char_148_nearl_1#6", focus=2)]
[name="临光"]  嘿嘿。
[Character(name="char_148_nearl_1#1")]
[name="临光"]  你身边这位，就是博士了吧。
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]  是的。只是......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ——我们每遇到一个人就要和她说说博士失忆了的事，这也太麻烦了。
[Character(name="char_148_nearl_1#1")]
[name="临光"]   Dr.{@nickname}吗......
[Character(name="char_148_nearl_1#1")]
[name="临光"]   我的一个朋友同样也失去了记忆，你一定会和她很合得来的。
[name="临光"]   毕竟对于你来说，没有什么比“现在”更重要了。
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]  嗯......嗯！
[Character(name="char_148_nearl_1#1")]
[name="临光"]  走吧，各位。
[name="临光"]  我们，还要把博士护送到罗德岛。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Background(image="bg_cher_5", width=1, height=1, fadetime=0)]
[Blocker(a=0, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_1508_Faust_1",fadetime=2,block=true)]
[name="浮士德"]   对不起......我失手了。
[Character(name="char_1507_Mephisto_1#1",name2="char_1508_Faust_1",focus=1)]
[name="梅菲斯特"]  不，不要道歉。是我的错，我太冲动了。
[name="梅菲斯特"]  能帮我追踪罗德岛他们吗？我会去把情况通报给塔露拉姐姐。
[name="梅菲斯特"]  她应该也已经压制住了切尔诺伯格的核心指挥塔。
[name="梅菲斯特"]  ——就让她来决定这些虫子的生死吧。
[Character(name="char_1507_Mephisto_1#1",name2="char_1508_Faust_1",focus=2)]
[name="浮士德"]   ......明白了。
[Character(name="char_1507_Mephisto_1#2",name2="char_1508_Faust_1",focus=1)]
[name="梅菲斯特"]  小心点，优先保护好自己，好吗？
[Character(name="char_1507_Mephisto_1#1",name2="char_1508_Faust_1",focus=2)]
[name="浮士德"]   ......好。
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Blocker(a=0, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_1507_Mephisto_1")]
[name="梅菲斯特"]   ......我的任务也完成了。
[Delay(time=0.6)]
[name="梅菲斯特"]   同胞们，该走了。
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Background]
[Character(fadetime=0)]
[Image(image="avg_ep00_2",x=0, y=0, xScale=1, yScale=1, fadetime=3, screenadapt="coverall")]
[Blocker(a=0, fadetime=0.6, block=false)]
[Character(name="char_1507_Mephisto_1#5")]
[name="梅菲斯特"]   去迎接属于我们的时代吧！！
[delay(time=3)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Image(fadetime=0)]
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_01-01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第七关（前）
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Background(screenadapt="coverall", image="bg_cher_1", width=1, height=1, fadetime=1)]
[Delay(time=1)]
[Character(name="char_130_doberm_ex", name2="char_013_riop", focus=2)]
[name="近卫干员"]   是我的错觉，还是天确实越来越暗了？
[Character(name="char_130_doberm_ex", name2="char_013_riop", focus=1)]
[name="杜宾"]  ......我也希望是你的错觉。
[name="杜宾"]  不过我们本来时间就不多。
[Blocker(a=1,r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="avg_9_2",x=50, y=30,xScale=1.15, yScale=1.15, fadetime=0)]
[ImageTween(xFrom=50, yFrom=20, xTo=0, yTo=0, xScaleFrom=1.15, yScaleFrom=1.15, xScaleTo=1, yScaleTo=1, duration=15, block=false)]
[Blocker(a=0, fadetime=1, block=true)]
[name="杜宾"]  天灾云的形状比刚才黑压压的一片更加清晰了。
[name="杜宾"]  啧，裸眼看着它慢慢在头上凝聚显形，可不是什么好兆头。
[Blocker(a=1,r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="char_130_doberm_ex", name2="char_148_nearl_1", focus=1)]
[Dialog]
[Image(fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="char_130_doberm_ex", name2="char_148_nearl_1", focus=1)]
[name="杜宾"]  加上，下城区的每一条街道都可能埋伏着整合运动......
[name="杜宾"]  不，这个说法太过保守了。
[Character(name="char_130_doberm_ex", name2="char_148_nearl_1", focus=2)]
[name="临光"]  该说是，整合运动满满当当地挤在街上。
[Blocker(a=0, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_016_medic")]
[name="医疗干员"]  几乎每条街上都有暴徒在搞破坏，抢劫，焚毁交通工具和店铺......
[name="医疗干员"]  这帮家伙，是觉得天气太好，所以出来野餐集会吗！
[Character(name="char_148_nearl_1#6")]
[name="临光"]  现在跑出来野餐，一定会遭到天灾的无情摧残。
[name="临光"]  这说明大部分整合运动都是些被野蛮冲昏头脑的傻瓜。
[Character(name="char_002_amiya_1#6", name2="char_016_medic")]
[Delay(time=1)]
[Character(name="char_002_amiya_1#6", name2="char_016_medic", focus=1)]
[name="阿米娅"]  ......
[Character(name="char_002_amiya_1#2", name2="char_016_medic", focus=1)]
[name="阿米娅"]   ......噗。
[Character(name="char_002_amiya_1#2", name2="char_016_medic", focus=2)]
[name="医疗干员"]   他们不是真的要......野餐啦......
[name="医疗干员"]   我，我只是发个牢骚，不是那个意思......
[Character(name="char_148_nearl_1")]
[name="临光"]  ——
[Character(name="char_148_nearl_1#6")]
[name="临光"]  这不是个形容吗？难道说这是个包袱？
[Character(name="char_148_nearl_1#2")]
[name="临光"]  嗯......
[name="临光"]  抱歉，总是在这种时候......
[Character(name="char_148_nearl_1#2", name2="char_016_medic", focus=2)]
[name="医疗干员"]  唔唔唔......没，没事......
[name="医疗干员"]  反而是憋笑有点难受......！
[name="医疗干员"]  唔，抱歉......明明是很紧要的时期，我却......
[Character(name="char_002_amiya_1#3 ")]
[Character(name="char_002_amiya_1#1 ")]
[name="阿米娅"]  没关系的。
[name="阿米娅"]  我们不是为了让大家都哭丧着脸才建立起罗德岛的。
[name="阿米娅"]  罗德岛，本来就希望各位，都能绽放笑容。
[Character(name="char_002_amiya_1#1 ",name2="char_016_medic",focus=2)]
[name="医疗干员"]  阿，阿米娅......
[Character(name="char_002_amiya_1#1 ",name2="char_016_medic",focus=1)]
[name="阿米娅"]  没关系的，医生！
[Character(name="char_130_doberm_ex",name2="char_014_riope",focus=1)]
[name="杜宾"]  那我们，就去为侦查工作贡献一份力量吧。
[name="杜宾"]  四点钟方向的敌人，我会安静地处理掉。
[name="杜宾"]  只要他们体内的病变器官不是什么警报器或爆炸物就行。
[Character(name="char_130_doberm_ex",name2="char_014_riope",focus=2)]
[name="Ace"]  另一侧，游离于据点之外的大批整合运动，就交给我们吧。
[name="Ace"]  只要杂音够大，就没有人能分辨出里面究竟包含了什么声音。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  那么，各自行动起来！
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_01-01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第七关（后）
[name=""]   时间未知 \ 天气未知 \ 能见度 低 
[name=""]   切尔诺伯格 行动组E0所在地
[name=""]   Dr.{@nickname}营救行动 第三阶段 
[Background(image="bg_cher_1", width=1, height=1, fadetime=1)]
[Delay(time=1)]
[PlayMusic(intro="$mist_loop", key="$mist_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Character(name="char_016_medic")]
[name="医疗干员"]  啊！
[name="医疗干员"]  这个诊所......
[name="医疗干员"]  阿米娅，是不是以前我们来过那个？
[Character(name="char_016_medic",name2="char_002_amiya_1#1",focus=2)]
[name="阿米娅"]  ......确实是......
[name="阿米娅"]  只是怎么......已经变成了，这个样子？
[Character(name="char_016_medic",name2="char_002_amiya_1#1",focus=1)]
[name="医疗干员"]  已经人去楼空了......看来，是遭到了整合运动的袭击吧......
[Character(name="char_016_medic",name2="char_002_amiya_1#4",focus=2)]
[name="阿米娅"]  ......
[Character(name="char_002_amiya_1#4",name2="char_013_riop",focus=2)]
[name="近卫干员"]  这难道就是那个感染者诊所，阿撒兹勒？
[Character(name="char_002_amiya_1#4",name2="char_013_riop",focus=1)]
[name="阿米娅"]  ......是。
[Character(name="char_002_amiya_1#4",name2="char_013_riop",focus=2)]
[name="近卫干员"]  明明掌握着整个切尔诺伯格的地下情报网，却不肯和我们合作......
[name="近卫干员"]  那时，他们和整合运动之间的关系也十分模棱两可......
[name="近卫干员"]  至少，如果他们当时肯向我们分享情报，或者仅仅是给个提示......
[name="近卫干员"]  我们也许就早点能离开这里了。
[name="近卫干员"]  这种下场，是他们自作自受！
[Character(name="char_002_amiya_1", name2="char_013_riop", focus=1)]
[name="阿米娅"]  也不全是这样......
[Character(name="char_002_amiya_1", name2="char_013_riop", focus=2)]
[name="近卫干员"]  阿米娅，当时和他们交涉时你也在场吧？
[name="近卫干员"]  他们那傲慢冷漠的态度，我真是......
[Character(name="char_014_riope" )]
[name="Ace"]  不能怪罪他们。
[Character(name="char_013_riop")]
[name="近卫干员"]  头儿......
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[Character(fadetime=0)]
[Background(fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, block=true)]
[Image(image="bg_0_ori",x=-100, y=0, xScale=1.2, yScale=1.2, fadetime=1)]
[ImageTween(xFrom=-100, yFrom=0, xTo=0, yTo=0, xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1.2, yScaleTo=1.2, duration=10, block=false)]
[name="Ace"]  感染者本就很难相信别人。
[name="Ace"]  经历过那么多苦难，当然会变得保守与顽固。
[name="阿米娅"]  至少他们那样做......我能理解，也愿意原谅他们。不提防他人，就会被他人伤害。
[name="阿米娅"]  何况，就连感染者之间，也是没法轻易互相信任的。而且并不是每个人都愿意像我们一样冒险......
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[Image]
[Blocker(a=0, r=0, g=0, b=0, block=true)]
[Background(image="bg_cher_1", width=1, height=1, fadetime=1)]
[Decision(options="感染者诊所？", values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]  啊......他们是一家只医治感染者的黑市诊所。
[name="阿米娅"]  鉴于感染者的社会地位，大家是不可能在街道上抛头露面的。
[name="阿米娅"]  有些不愿被抛进隔离区的感染者，依然也会在城市里，小心翼翼地掩藏自己的身姿，苟活着......
[name="阿米娅"]  阿撒兹勒，就是向这些感染者提供服务的。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  ......它们，一定是拒绝了整合运动的合作要求。
[name="阿米娅"]  博士，我之前和你说过，我们得了病吧？
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]  ......这种病，不仅会杀死我们，也会让我们拥有不同于常人的力量。
[name="阿米娅"]  我不用法杖，就能释放源石技艺哦。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  然而，这种病，不止在生理上，会消磨我们的生命......
[name="阿米娅"]  它也会让我们再也不能像正常人一样生活。正常人的社会，会剥去你的一切。
[name="阿米娅"]  这座切尔诺伯格城，已经是所有规则的象征了。
[name="阿米娅"]  驱逐感染者，消灭感染者，鄙夷感染者，恐惧感染者......
[Character(name="char_148_nearl_1#2")]
[name="临光"]  ......
[name="临光"]  最后，落到如此下场。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  可是，又有多少感染者，会有机会，选择整合运动，甚至是其他的感染者组织，或者罗德岛？
[name="阿米娅"]  大多数感染者，不过是失去了所有。
[name="阿米娅"]  这个诊所，大概，也曾经是最后那么几个感染者，温暖的家吧......
[name="阿米娅"]  矿石病是无药可医的。至少此时此刻，感染者只能在绝望中......痛苦地失去生命。
[name="阿米娅"]  而后他们的遗体......也会成为新的传染源。
[name="阿米娅"]  不同于常人的特殊力量，染上之后就必然会死去的可怕传染病——
[name="阿米娅"]  感染者......被这片大地上的多数人所恐惧。
[name="阿米娅"]  ——
[name="阿米娅"]  光是这么两三句话，博士大概也没法切身体会吧。
[name="阿米娅"]  但当你面对这些问题导致的后果时......你会明白的。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  你会明白，感染者的处境，究竟有多现实。
[Character(name="char_002_amiya_1#4", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]  像罗德岛这样不分彼此，或是整合运动那样狂热的排外拥内的感染者组织，都很少见。
[name="杜宾"]  我能理解你的怒气，但我也能理解那个小诊所的苦衷。
[Character(name="char_013_riop")]
[name="近卫干员"]  ......我明白了。
[name="近卫干员"]  可能，他们是真的碰上了什么问题吧......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  至少现在，我们的怨气，都该和这个诊所的曾经一样，化作粉尘。
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]  罗德岛的各位都是好人。也许会有很多人因畏惧与敌意，相互间产生了种种隔阂......
[name="阿米娅"]  但只要在罗德岛，大家一定能解开误会。
[name="阿米娅"]  阿撒兹勒......罗德岛，又何尝不是一个阿撒兹勒呢？
[Character(name="char_013_riop")]
[name="近卫干员"]  ......阿米娅......
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]  我们走吧，博士。
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_01-03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第八关（前）
[name=""]   时间未知 \ 天气未知 \ 能见度 低 
[name=""]   切尔诺伯格 行动组E0所在地
[name=""]   Dr.{@nickname}营救行动 第三阶段 
[dialog]
[Background(image="bg_cher_1", width=1, height=1, fadetime=1)]
[PlayMusic(intro="$chernormal_intro", key="$chernormal_loop", volume=0.8, crossfade=1, delay=0.5)]
[Delay(time=1)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  还剩不到一个小时，没时间从其他区域绕行了......
[name="杜宾"]  我们浪费的时间越多，天灾在我们头顶发生的可能性就越大。
[name="杜宾"]  必须直接穿过当前区域。
[name="杜宾"]  以我们现在的规模，团队行动难免会被发觉。
[name="杜宾"]  在狭窄的街巷中行动，很容易被埋伏包夹......
[Character(name="char_148_nearl_1", name2="char_130_doberm_ex", focus=1)]
[name="临光"]   怎么办？
[Character(name="char_148_nearl_1", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]   选择不多......
[name="杜宾"]  Dr.{@nickname}，你的想法呢？
[Decision(options="正面碾压过去就好！;......大概，他们也没法阻拦......;敌人想组织反击也需要时间。", values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  整合运动的个人实力并不能和我们相提并论。
[name="杜宾"]  大多数情况下，都只是在依赖人海战术围攻我们。
[Character(name="char_148_nearl_1")]
[name="临光"]   依靠速度，不断前进，尽量减少一次性交战的人数的话——
[Predicate(references="2")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   他们并没有构筑防御工事。
[Character(name="char_148_nearl_1")]
[name="临光"]   如果我们突袭他们的封锁线......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   虽然看上去人数众多，但整合运动这样松散的布置，是拦不住我们的。
[Predicate(references="3")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   整合运动的通信方式，从过往的战斗来看，是十分原始的。
[Character(name="char_148_nearl_1")]
[name="临光"]   在我们突破敌人的阻碍，当他们开始组织起来，尝试截击我们的时候......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   当整合运动终于集结完毕，我们也早已经到达了下一个区域。
[Predicate]
[Character(name="char_148_nearl_1")]
[name="临光"]   不错。
[name="临光"]   猛烈冲击，搅乱阵形，破坏火力点，迅速撤退。
[name="临光"]   ......杜宾，你在考验我，还是在考验——
[Character(name="char_002_amiya_1#1", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]  肉眼可见的威胁远比进退两难容易处理得多。
[name="杜宾"]  我可以把这看作是Dr.{@nickname}的命令吗，阿米娅？
[Character(name="char_002_amiya_1#1", name2="char_130_doberm_ex", focus=1)]
[name="阿米娅"]  局势很明了了。我相信博士的选择......
[Character(name="char_002_amiya_1#1", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]   ——所谓信任，也不光是一场战役就能轻松建立的。
[name="杜宾"]   我很看好Dr.{@nickname}，但阿米娅......
[name="杜宾"]   不要放松警惕。你当然可以借助博士的智慧，但不可以完全依赖他。
[Character(name="char_002_amiya_1#7", name2="char_130_doberm_ex", focus=1)]
[name="阿米娅"]  ——我知道。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  别介意，博士，我没想刁难你。
[name="杜宾"]   只是，希望你能理解——阿米娅需要更多的学习和成长。
[name="杜宾"]   站在我的立场上，你也不会允许阿米娅太依靠别人的。
[name="杜宾"]   不过，我已经认可了你的指挥能力。
[Decision(options="谢谢......", values="1")]
[Predicate(references="1")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   也别那么拘谨，我们可已经是共患难的战友了。
[name="杜宾"]   至少在战场，我的生命，已经交给你了。
[name="杜宾"]   闲谈到此为止，抓紧时间。
[Character(name="char_148_nearl_1#1", name2="char_130_doberm_ex", focus=1)]
[name="临光"]   是的。
[name="临光"]   卡西米尔有句谚语：“喘息时，死亡就会追上你。”
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_01-03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第八关（后）
[PlayMusic(intro="$chernormal_intro", key="$chernormal_loop", volume=0.8, crossfade=1, delay=0.5)]
[Background(image="bg_cher_1", width=1, height=1, fadetime=0)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[CameraShake(duration=3,xstrength=2,ystrength=3,vibrato=10,randomness=90,fadeout=true,block=true)]
[Character(name="char_148_nearl_1#3")]
[name="临光"]  冲锋——！！
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]   啊？
[name="整合运动成员"]   ——是谁在那边？！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   呿，你在看哪里！接招！
[playsound(key="$p_imp_whip_h", volume=0.7)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[Character(name="char_1002_nsabr_2")]
[CameraShake(duration=3,xstrength=2,ystrength=3,vibrato=10,randomness=90,fadeout=true,block=false)]
[name="整合运动成员"]   呃啊！！
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_013_riop", name2="char_148_nearl_1", focus=1)]
[name="近卫干员"]   呼......
[name="近卫干员"]   整合运动正在我们后方......组织进攻！
[Character(name="char_013_riop", name2="char_148_nearl_1#3", focus=2)]
[name="临光"]  他们跟不上我们的速度！继续冲刺！
[Character(fadetime=0)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.8)]
[CameraShake(duration=3,xstrength=2,ystrength=3,vibrato=10,randomness=90,fadeout=true,block=true)]
[Character(name="char_130_doberm_ex", name2="char_148_nearl_1#3", focus=1)]
[name="杜宾"]  马上就能离开整合运动控制的区域了！不要停下！！
[Character(name="char_130_doberm_ex", name2="char_148_nearl_1#3", focus=2)]
[name="临光"]   区区暴徒——
[name="临光"]   怎么能阻止我们！
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_01-04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第九关（前）
[Background(image="bg_cher_1", width=1, height=1, fadetime=1)]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Delay(time=1)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  呼......甩开他们了。
[Character(name="char_014_riope", name2="char_130_doberm_ex", focus=1)]
[name="Ace"]  按这个速度，我们很快就会离开中城区，抵达南面出口。
[Character(name="char_014_riope", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]  周围也变得越来越嘈杂......
[name="杜宾"]  可能是切尔诺伯格的居民想要逃出城市，反而和整合运动发生了冲突吧。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  ......
[Character(name="char_014_riope", name2="char_130_doberm_ex", focus=1)]
[name="Ace"]  似乎有几个城区已经撤离了。
[name="Ace"]  而没来得及逃出切尔诺伯格的本地居民，却依然被整合运动拦在这里。
[Character(name="char_148_nearl_1#3")]
[name="临光"]   ......
[Character(name="char_014_riope", name2="char_130_doberm_ex", focus=1)]
[name="Ace"]  ——
[name="Ace"]  这个开阔区域，曾经是个大广场吧。如今......只剩下些废墟。
[name="Ace"]  虐待感染者的城市，遭到了感染者的报复吗。
[Character(name="char_014_riope", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]  你似乎——
[name="杜宾"]  很有感触。
[Character(name="char_014_riope", name2="char_130_doberm_ex", focus=1)]
[name="Ace"]  呵，曾经......
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  天色......越来越暗淡了。
[name="阿米娅"]  好像连空气中......都弥漫着一股......燃烧的味道。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Image(fadetime=0)]
[Blocker(a=0, fadetime=0.6, block=false)]
[Character(fadetime=0)]
[name="平民"]  你们在干什么！
[name="整合运动成员"]  ......
[Character(fadetime=0)]
[name="平民"]  ......啊啊！！
[Character(name="char_014_riope")]
[name="Ace"]  ————!
[name="Ace"]  平民？
[Character(name="char_014_riope", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]  听不到了。
[name="杜宾"]  ——这个距离，没法确认身份。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  ——！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  整合运动在攻击他们——！
[Character(name="char_014_riope")]
[name="Ace"]  在这种地形没有优势。我们没有能力去顾及他人的生命安全。
[name="Ace"]  生命很宝贵，阿米娅。每个人的，都很宝贵。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  ......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ————
[name="杜宾"]  不管怎么样都来不及了。
[name="杜宾"]  毕竟我们已经有更大的麻烦找上了门。
[Character(name="char_148_nearl_1#3")]
[name="临光"]   ......
[name="临光"]   不好的事情还是发生了。
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]  ————
[Delay(time=0.5)]
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_2")]
[name="整合运动成员"]  ——————杀了他们。
[Character(name="char_148_nearl_1#1")]
[name="临光"]   开阔区各个出口同时出现大量整合运动！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  准备作战！
[Dialog]
[Blocker(block=true)]
[Delay(time=0.6)]
[Image]
```

### level_main_01-06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第九关（后）
[Background(screenadapt="coverall", image="bg_cher_0", width=1, height=1, fadetime=1)]
[PlayMusic(intro="$chernormal_intro", key="$chernormal_loop", volume=0.8, crossfade=1, delay=0.5)]
[Delay(time=1)]
[Character(name="char_1507_Mephisto_1")]
[name="梅菲斯特"]  是的，他们不知道自己被浮士德跟踪。我从浮士德派回来的斥候那里了解到了一些情报。
[name="梅菲斯特"]  罗德岛确实被困在中城区的外围了。
[name="梅菲斯特"]  虽然是些虫子，但他们也可能趁着天灾带来混乱逃跑。
[name="梅菲斯特"]  以他们对切尔诺伯格现状的了解，说不定会干扰到我们的计划。
[name="梅菲斯特"]  ——至少，把他们铲除掉没有任何坏处。
[Dialog(fadetime=0)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(name="char_011_talula_1#2",fadetime=1)]
[name="？？？"]   ————
[Character(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Background(image="bg_cher_1", width=1, height=1, fadetime=0)]
[Character(fadetime=0)]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_2")]
[name="整合运动成员"]  切尔诺伯格的混蛋，都是你们，都是你们，害得我们感染者变成这样！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  闪开！
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, block=false)]
[playsound(key="$p_imp_whip_h", volume=0.5)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]  呜！
[Character(fadetime=0.5)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  这些人，只不过是在前仆后继地送死！！
[Character(name="char_148_nearl_1#4")]
[name="临光"]  整合运动怎么全都陷入了狂躁状态？
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  为什么这个时候，这里会聚集着这么多整合运动？！
[name="杜宾"]  不合常理！整合运动根本没有坚守这里的理由！
[Character(name="char_148_nearl_1#3")]
[name="临光"]  罗德岛干员们，不要退缩！击退整合运动，打开撤退路径！
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Background(screenadapt="coverall", image="bg_cher_0", width=1, height=1, fadetime=0)]
[Background(fadetime=2)]
[Character(name="char_011_talula_1#2", fadetime=0.5)]
[Delay(time=0.5)]
[name="？？？"]   ————
[Delay(time=1)]
[Character(name="char_1505_frstar_1#2")]
[name="？？？"]   那些人就是情报中说的“罗德岛”？呵......很英勇。
[Delay(time=0.5)]
[Character(name="char_1502_crowns")]
[name="弑君者"]   ......
[Delay(time=0.5)]
[Dialog]
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Background(image="bg_cher_1", width=1, height=1, fadetime=0)]
[Blocker(a=0, fadetime=0.6, block=true)]
[PlaySound(key="$d_gen_explo_n")]
[StopMusic(fadetime=1)]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, block=false)]
[Blocker(a=0.7, r=0.93, g=0.40, b=0.32, fadetime=0.1, block=true)]
[Blocker(a=0, r=0.93, g=0.75, b=0.32, fadetime=0.2, block=true)]
[PlaySound(key="$d_gen_explo_n", volume=0.1)]
[Character(name="char_016_medic")]
[name="医疗干员"]  ......啊？
[Character(name="char_013_riop")]
[name="近卫干员"]  ......落石？这个时候？
[Character(name="char_014_riope",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  别停下！优先确保防线！
[Character(name="char_013_riop")]
[name="近卫干员"]  不对......是砸在建筑物上迸出来的......
[Character(name="char_014_riope",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]  你在说什么——
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_2")]
[name="整合运动成员"]  来了！来了！
[name="整合运动成员"]  哈哈......我们感染者的救赎！普通人的末日！
[name="整合运动成员"]  啊，啊啊——咕！
[dialog]
[PlaySound(key="$d_gen_explo_n", channel=2, volume=0.6)]
[Blocker(a=0.7, r=1, g=0.1, b=0.3, fadetime=0.02, block=true)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=1, xstrength=10, ystrength=10, vibrato=30, randomness=90, block=false)]
[name="整合运动成员"]  啊，啊啊——咕！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ——
[name="杜宾"]  他是被什么东西......击倒的？
[name="杜宾"]  你们有谁......攻击了他？
[name="杜宾"]  还是说，他是被......
[PlaySound(key="$d_gen_explo_n", volume=0.4, delay=2)]
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  杜宾！天空......！
[Character(name="char_148_nearl_1#3")]
[name="临光"]  ——
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.8, block=true)]
[name="临光"]  天空陷入了血色——
[name="临光"]  “沸腾的乌云翻涌在火焰之中......”
[Character(name="char_014_riope")]
[name="Ace"]  别惊慌！
[Character(name="char_148_nearl_1#7")]
[name="临光"]  保护好自己！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ......我们还有机会，用行动去拯救自己的生命！
[Dialog]
[Character(fadetime=0)]
[Background(fadetime=0)]
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Image(image="avg_9_3",x=-64, y=35, xScale=1.1, yScale=1.1, fadetime=2)]
[ImageTween(xFrom=-64, yFrom=35, xTo=64, yTo=35, xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1.1, yScaleTo=1.1, duration=10, block=false)]
[CameraShake(duration=3, fadeout=true, xstrength=15, ystrength=15, vibrato=30, randomness=90, block=false)]
[PlaySound(key="$d_gen_explo_n", channel=2, volume=0.6)]
[name="？？？"]  “——大地陷入寂静，恐惧取走了他们的声音。”
[Blocker(a=0, fadetime=1, block=true)]
[Blocker(a=0.1, r=0.93, g=0.40, b=0.32, fadetime=0.1, block=true)]
[Blocker(a=0, r=0.93, g=0.40, b=0.32, fadetime=0.1, block=true)]
[Blocker(a=0.05, r=0.93, g=0.40, b=0.32, fadetime=0.1, block=true)]
[Blocker(a=0, r=0.93, g=0.40, b=0.32, fadetime=0.1, block=true)]
[PlaySound(key="$d_gen_explo_n", channel=2, volume=0.8)]
[CameraShake(duration=3, fadeout=true, xstrength=25, ystrength=25, vibrato=30, randomness=90, block=false)]
[Delay(time=0.2)]
[name="？？？"]  “巨大的源石垂下头颅——”
[Blocker(a=0.1, r=0.93, g=0.40, b=0.32, fadetime=0.1, block=true)]
[Blocker(a=0, r=0.93, g=0.40, b=0.32, fadetime=0.1, block=true)]
[Blocker(a=0.05, r=0.93, g=0.40, b=0.32, fadetime=0.1, block=true)]
[Blocker(a=0, r=0.93, g=0.40, b=0.32, fadetime=0.1, block=true)]
[name="？？？"]  “——坠落，它坠落在死亡焦热的阴影。”
[PlaySound(key="$d_gen_explo_n", channel=2, volume=0.6)]
[CameraShake(duration=3, fadeout=true, xstrength=25, ystrength=25, vibrato=30, randomness=90, block=false)]
[Blocker(a=0.05, r

... (全文8881字符)
```

### level_main_01-07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第十关（前）
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[Background(image="bg_cher_10", fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5,block=true)]
[Delay(time=0.3)]
[PlaySound(key="$d_gen_explo_n")]
[CameraShake(duration=1, xstrength=3, ystrength=5, vibrato=30, randomness=90, fadeout=false)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  抗冲击准备！！
[name="杜宾"]  各自散开——！！！
[name="杜宾"]  规模太大了......这样下去，整个街区的建筑都会被彻底摧毁！
[name="杜宾"]  不行，糟了———！
[character]
[dialog]
[image(fadetime=1)]
[Character(name="char_014_riope")]
[name="Ace"]  ——！
[name="Ace"] 快转移！
[Character(name="char_016_medic")]
[name="医疗干员"]   ......！
[Character(name="char_014_riope")]
[name="Ace"]  坚持住！！
[Character]
[PlaySound(key="$d_gen_explo_n", volume=0.7)]
[CameraShake(duration=3, fadeout=true, xstrength=25, ystrength=25, vibrato=30, randomness=90, block=false)]
[Blocker(a=0.2, r=0.93, g=0.7, b=0.2, fadetime=0.1, block=true)]
[Blocker(a=0, r=0.93, g=0.75, b=0.32, fadetime=0.2, block=true)]
[name="整合运动成员"]     啊——！！掉，掉下来了！
[name="整合运动成员"]    天空掉下来了！
[PlaySound(key="$d_gen_explo_n", volume=0.7)]
[CameraShake(duration=3, fadeout=true, xstrength=25, ystrength=25, vibrato=30, randomness=90, block=false)]
[Blocker(a=0.2, r=0.93, g=0.7, b=0.2, fadetime=0.1, block=true)]
[Blocker(a=0, r=0.93, g=0.75, b=0.32, fadetime=0.2, block=true)]
[name="整合运动成员"]    不，不，啊好疼......
[name="整合运动成员"]    我的手，我的手！我的手哪里去了......
[name="整合运动成员"]    怎，怎么会！！我不想死......！
[name="整合运动成员"]    啊啊啊啊！！！
[PlaySound(key="$d_gen_thunders_amb", delay=2, volume=0.5)]
[Dialog]
[Blocker(a=0.2, r=0.93, g=0.8, b=0.4, fadetime=0.1, block=true)]
[Image(fadetime=0)]
[Blocker(a=0, r=0.93, g=0.75, b=0.32, fadetime=0.2, block=true)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[Character(name="char_148_nearl_1#3")]
[name="临光"]    重装干员！
[name="临光"]    保护我方术师！！
[name="临光"]    ——！！
[name="临光"]    那是什么声音？！
[Character(name="char_014_riope")]
[name="Ace"]  巨大的坠岩击垮了临街的建筑！卧倒！！
[Dialog]
[PlaySound(key="$d_gen_explo_n", volume=0.7)]
[CameraShake(duration=3, fadeout=true, xstrength=25, ystrength=25, vibrato=30, randomness=90, block=false)]
[Blocker(a=0.2, r=0.93, g=0.7, b=0.2, fadetime=0.1, block=true)]
[Blocker(a=0, r=0.93, g=0.75, b=0.32, fadetime=0.2, block=true)]
[Character(name="char_016_medic")]
[name="医疗干员"]  啊......！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]    ——那个位置——医生！危险！
[Character(name="char_013_riop")]
[name="近卫干员"]    糟糕，医生，快闪开！
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.3, block=true)]
[Decision(options="......！", values="1")]
[Predicate(references="1")]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.3, block=true)]
[Character(name="char_016_medic")]
[name="医疗干员"]  啊！
[name="医疗干员"]  ......唔，博，博士？
[Character(name="char_013_riop")]
[name="近卫干员"]    博士把医生推进了掩体？可这样......这样的话，博士——！
[name="近卫干员"]    不，博士！！
[Character(name="char_148_nearl_1#3")]
[name="临光"]    Dr.{@nickname}！！
[Character(name="char_013_riop")]
[name="近卫干员"]    啊？
[name="近卫干员"]    临，临光她冲出去了！
[Character(name="char_148_nearl_1#3")]
[name="临光"]    博士，蹲下！
[Character]
[Dialog]
[PlaySound(key="$d_gen_explo_n", volume=0.5)]
[CameraShake(duration=3, fadeout=true, xstrength=25, ystrength=25, vibrato=30, randomness=90, block=false)]
[Blocker(a=0.2, r=0.93, g=0.7, b=0.2, fadetime=0.1, block=true)]
[Blocker(a=0, r=0.93, g=0.75, b=0.32, fadetime=0.2, block=true)]
[Blocker(a=1, r=0.93, g=0.8, b=0.4, fadetime=0.1, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_148_nearl_1#3",fadetime=0.7)]
[name="临光"]    咯......
[name="临光"]    赶上了！
[Character(name="char_013_riop")]
[name="近卫干员"]    她救下......她救下博士了！
[Character(name="char_148_nearl_1#3")]
[name="临光"]    咳哈......！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]    临光！博士！快回来！
[Character(name="char_148_nearl_1#3")]
[name="临光"]    没问题的！
[name="临光"]    我的盾牌还撑得住——！
[name="临光"]    跳啊，博士！
[name="临光"]    跳！
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]    博士，博士......
[name="阿米娅"]    你，你没事吧？
[Decision(options="我没事，这算不了什么！;......;多亏临光小姐救下了我。", values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_148_nearl_1#3")]
[name="临光"]    一个人......处在那样的危险中！
[name="临光"]    至少拉上我一起，让我保护博士你！
[name="临光"]    无论怎样，我都不能允许你受伤——
[name="临光"]    何况，是在我面前！
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]    大家都还安全，就非常好了......！
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]    但我们......
[name="阿米娅"]    （还要坚持多久呢？）
[name="阿米娅"]    （我们真的能活下来吗？）
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]    ......唔......
[name="阿米娅"]    坠石的数量减少了？
[name="阿米娅"]    我们撑过了第一波主灾害了吗......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    还不能大意，谁知道这次的天灾会持续多久。
[name="杜宾"]    不过至少......我们不是身处天灾正中心的人。
[name="杜宾"]    我们侥幸躲过去了。
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]    嗯......
[name="阿米娅"]    大家怎么样了？
[Character(name="char_013_riop")]
[name="近卫干员"]    干员们基本都没事......！
[name="近卫干员"]    有些干员受了轻伤，但状况都还算不错！
[name="近卫干员"]    我们......活下来了！
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.3, block=true)]
[Dialog]
[Blocker(a=0, fadetime=0.3, block=true)]
[name="整合运动成员"]    啊......
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]    整合运动也有部分人员——
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]    ......啊？
[name="整合运动成员"]    啊......啊！！罗德岛！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    ......什么？
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_2")]
[name="整合运动成员"]    啊......！！！
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]    整合运动还要继续攻击我们吗？
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_2")]
[name="整合运动成员"]    ......
[name="整合运动成

... (全文6488字符)
```

### level_main_01-07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第十关（后）
[PlayMusic(intro="$chernormal_intro", key="$chernormal_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[Background(image="bg_cher_7", fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5,block=true)]
[Delay(time=0.3)]
[PlaySound(key="$d_gen_explo_n")]
[CameraShake(duration=1, xstrength=3, ystrength=5, vibrato=30, randomness=90, fadeout=false)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   哈，哈，哈.....
[Character(name="char_148_nearl_1#3")]
[name="临光"]   成功了......！
[name="临光"]   我们不仅击退了整合运动......
[name="临光"]   灾势也在以肉眼可见的程度衰弱！
[name="临光"]   情况太糟糕了......各位还是要多加小心！
[Character(name="char_002_amiya_1#5")]
[name="阿米娅"]   天灾......
[name="阿米娅"]   原本的街道都被倒塌的废墟掩盖，被摧毁的建筑，形成了障碍物......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   源石，已经开始疯长了吗......
[name="杜宾"]   明明到了最后关头，所有事情却都在阻挠我们！
[name="杜宾"]   如果我们能——
[name="杜宾"]   ......能......
[Character(name="char_014_riope")]
[name="Ace"]  ——
[name="Ace"]  来了。
[Character(name="char_014_riope",name2="char_013_riop",focus=2)]
[name="近卫干员"]   什么来了？
[name="近卫干员"]   整合运动？他们追上来了？！
[Character(fadetime=0)]
[Dialog]
[PlaySound(key="$d_gen_soldiersrun",volume=1)]
[Character(name="char_1002_nsabr_2",fadetime=1)]
[Delay(time=2)]
[Character(name="char_016_medic")]
[name="医疗干员"]   啊......
[name="医疗干员"]   那么多的......整合运动......
[Character(fadetime=0)]
[PlaySound(key="$d_gen_soldiersrun",volume=1)]
[Dialog]
[Delay(time=2)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   他们......不是追上来了。
[name="杜宾"]   他们是......
[Character(name="char_148_nearl_1#3")]
[name="临光"]   ——从各个地方涌了出来。
[Character(fadetime=0)]
[Dialog]
[PlaySound(key="$d_gen_soldiersrun",volume=1)]
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_2",fadetime=1)]
[Delay(time=2)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   广场，坡道，建筑......四处的废墟。
[name="杜宾"]   这个数量，呵......
[name="杜宾"]   难怪除了那些真的要被砸成泥浆的人以外，他们一点都不惧怕天灾。
[name="杜宾"]   哪怕天灾，说多些.......
[name="杜宾"]   已经消灭了他们一半人——
[name="杜宾"]   剩下的也够把我们在这里淹死十几次了。
[Character(name="char_148_nearl_1#3")]
[name="临光"]   ——
[name="临光"]   别停下脚步！继续顺着撤退路线行动！
[name="临光"]   在开阔地带停下等于找死！至少到达广场出口处之后再整顿队形！
[Character(name="char_148_nearl_1#3",name2="char_002_amiya_1#7",focus=2)]
[name="阿米娅"]   临光......
[Character(name="char_148_nearl_1#3",name2="char_002_amiya_1#7",focus=1)]
[name="临光"]   必须战斗。破开突围口以后，趁对方队伍混乱立刻脱离。
[Character(name="char_148_nearl_1#3",name2="char_002_amiya_1#7",focus=2)]
[name="阿米娅"]   能行吗？
[Character(name="char_148_nearl_1#3",name2="char_002_amiya_1#7",focus=1)]
[name="临光"]   希望渺茫，但我们没有别的办法。只是......
[name="临光"]   即使是数十倍于自己数量的敌人，如果只是些暴徒，罗德岛依然有机会！
[name="临光"]   无需惊慌！备战姿态！防御阵形！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   ......啧。
[name="杜宾"]   这样的数量，如果要拿下切尔诺伯格，也许......真的有可能。
[Character(name="char_148_nearl_1#3")]
[name="临光"]   太多了。
[name="临光"]   实在......太多了。
[name="临光"]   整合运动究竟......是从哪里纠集起这么多感染者的？
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   这种包围网......
[name="杜宾"]   整合运动是真的，很看得起我们啊。
[Character(name="char_013_riop")]
[name="近卫干员"]   大，大群整合运动敌人......包围了广场！
[name="近卫干员"]   敌人停止了行动！
[name="近卫干员"]   ......
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   啊......
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Character(fadetime=0)]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[dialog]
[Character(fadetime=0)]
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[Background(image="bg_cher_7", fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, block=true)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_011_talula_1#2",fadetime=1,block=true)]
[Delay(time=2)]
[character(fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_013_riop")]
[name="近卫干员"]   有敌人一名，正在靠近罗德岛的阵线！
[name="近卫干员"]   为什么，那个人会一个人，走向我们......
[name="近卫干员"]   难道敌人派出了使者？不可能......
[Dialog]
[character]
[PlaySound(key="$d_gen_walk_n")]
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[Blocker(a=0, r=0, g=0, b=0, block=true)]
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   她......
[name="阿米娅"]   她......她是资料上，整合运动的......
[Character(name="char_148_nearl_1#3")]
[name="临光"]   ——
[name="临光"]   她身上，有某种气味。
[Character(name="char_148_nearl_1#3",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]   ......临光......
[Character(name="char_148_nearl_1#3",name2="char_130_doberm_ex",focus=1)]
[name="临光"]   我不清楚，但是......
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[Background(image="bg_cher_7", fadetime=0)]
[Dialog(fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, block=true)]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[Character(name="char_011_talula_1#2",fadetime=2)]
[Background(image="bg_cher_7",x=0, y=0, xScale=1.1, yScale=1.1, fadetime=1)]
[BackgroundTween(xFrom=0, yFrom=0, xTo=0, yTo=0, xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=4, block=true)]
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[character]
[Background(image="bg_cher_7", fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, block=true)]
[Character(name="char_148_nearl_1#3")]
[name="临光"]   那是......钢铁和硫磺的味道。
[name="临光"]   有什么东西在焚烧。
[name="临光"]   如果是火焰的话......
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   罗德岛的各位干员......最高警戒状态。
[name="阿米娅"]   ......她就是......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   整合运动的暴君......
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   ......塔露拉。
[PlaySound(key="$d_gen_thunders_amb")]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, block=false)]
[stopmusic(fadetime=2)]
[character]
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, block=true, fadetime=1)]
[Background]
[Blocker(a=1, initr=2, r=1, g=1, b=1, block=true, fadetime=0.3)]
[Blocker(a=0, fadetime=0.3, block=false)]
[Character(name="char_011_talula_1")]
[name="塔露拉"]   ......
[name="塔露拉"]   ............
[Blocker(a=1, initr=2, r=0, g=0, b=0, block=true, fadetime=1)]
[Character(name="char_148_nearl_1#3")]
[name="临光"]   大概......是能烧尽整片大地的火焰吧。
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_01-08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第十一关（前）
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[Background(image="bg_cher_7", fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5,block=true)]
[Delay(time=0.3)]
[Character(name="char_148_nearl_1#3")]
[name="临光"]   阿米娅，带博士离开。
[name="临光"]   ......立刻！
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   不行！我不能......
[Character(name="char_002_amiya_1#4", name2="char_148_nearl_1#3", focus=2)]
[name="临光"]   你也感觉到了！她......再这样下去，整个救援队都会葬送在这里！
[name="临光"]   那个塔露拉......
[name="临光"]   她是活生生的怪物！阿米娅！
[Character(name="char_002_amiya_1#7", name2="char_148_nearl_1#3", focus=1)]
[name="阿米娅"]   我们一起战斗的话，不会有问题的！
[Character(name="char_002_amiya_1#7", name2="char_148_nearl_1#3", focus=2)]
[name="临光"]   那博士呢？你能保证博士的安全吗？
[Character(name="char_002_amiya_1#4", name2="char_148_nearl_1#3", focus=1)]
[name="阿米娅"]   ......唔......
[Character(name="char_148_nearl_1#3")]
[name="临光"]   E4小队，我们留在这里断后！
[name="临光"]   一定要让阿米娅和Dr.{@nickname}，以及各个医疗小组安全撤离！
[Character(name="char_014_riope")]
[name="Ace"]   不，交给我和我的小队吧。
[Character(name="char_014_riope",name2="char_148_nearl_1#3",focus=2)]
[name="临光"]   Ace！现在难道是说这种话的时候吗！
[Character(name="char_014_riope",name2="char_148_nearl_1#3",focus=1)]
[name="Ace"]   我很冷静。
[Character(name="char_014_riope",name2="char_148_nearl_1#3",focus=2)]
[name="临光"]   你难道没看到吗，她周围的东西，都在融化！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   我不会留下你们独自战斗的。
[name="阿米娅"]   罗德岛......绝不会丢下你们的！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   阿米娅，时间宝贵！你必须撤退！
[Character(name="char_014_riope")]
[name="Ace"]   ——你应该信任我们。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   我不能看着罗德岛的任何一个人牺牲！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   想想任务目标，想想我们的目的！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   不是说这个的时候！
[Character(name="char_011_talula_1")]
[name="塔露拉"]  ——
[Dialog]
[PlaySound(key="$d_gen_thunders_amb", volume=0.5)]
[PlaySound(key="$b_char_defboost", volume=0.5, Delay=0.4)]
[PlaySound(key="$d_gen_thunders_amb", volume=0.2, Delay=0.7)]
[PlaySound(key="$flashback", volume=0.2, Delay=0.7)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=10, randomness=20, block=false)]
[Blocker(a=0.3, r=1, g=0.4, b=0.4, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0.3, r=1, g=0.4, b=0.4, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0.1, r=1, g=0.4, b=0.1, afrom=1, rfrom=1, gfrom=0.4, bfrom=0.4, fadetime=0.2, block=true)]
[Blocker(a=0.1, r=0, g=0, b=0, afrom=0.8, rfrom=1, gfrom=1, bfrom=1, fadetime=0.3, block=true)]
[Blocker(a=1, r=0, g=0, b=0, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.3, block=true)]
[Blocker(a=0, fadetime=3, block=true)]
[Character(name="char_148_nearl_1#3")]
[name="临光"]   ——？热量......在......她手里......聚集？
[Character(name="char_013_riop")]
[name="近卫干员"]   她周身的景象......扭曲了？
[Character(name="char_148_nearl_1#3")]
[name="临光"]   不，那是她......加热了周围的空气！
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   小心，她将要使用的法术......
[name="阿米娅"]   不对......不对！临光！！快回来！！
[name="阿米娅"]   那不是......那个法术会把你——
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_cher_7", width=1, height=1, fadetime=0)]
[Blocker(a=0, fadetime=1.5, block=true)]
[Character(name="char_011_talula_1",block=true)]
[name="塔露拉"]  ——安静。
[Dialog]
[Character(fadetime=1)]
[Character(name="char_148_nearl_1#3")]
[name="临光"]   呜呃......！
[Dialog]
[Character]
[Character(name="char_011_talula_1",block=true)]
[PlaySound(key="$d_gen_thunders_amb", volume=0.5)]
[PlaySound(key="$b_char_defboost", volume=0.5, Delay=0.4)]
[PlaySound(key="$d_gen_thunders_amb", volume=0.2, Delay=0.7)]
[PlaySound(key="$flashback", volume=0.2, Delay=0.7)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, block=false)]
[Blocker(a=0.3, r=1, g=0.4, b=0.4, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0.3, r=1, g=0.4, b=0.4, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0.1, r=1, g=0.4, b=0.1, afrom=1, rfrom=1, gfrom=0.4, bfrom=0.4, fadetime=0.2, block=true)]
[Blocker(a=0.1, r=0, g=0, b=0, afrom=0.8, rfrom=1, gfrom=1, bfrom=1, fadetime=0.3, block=true)]
[Blocker(a=0.1, r=0, g=0, b=0, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.3, block=true)]
[Blocker(a=0.1, fadetime=2, block=false)]
[delay(time=1)]
[Character(name="char_148_nearl_1#3")]
[name="临光"]   哈，哈......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   临光！
[Character(name="char_148_nearl_1#3",name2="char_130_doberm_ex",focus=1)]
[name="临光"]   咳......退后！我不要紧......
[name="临光"]   只不过是......有点烫而已......
[Character(name="char_148_nearl_1#3",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]   说什么......不要紧？
[name="杜宾"]   全身的铠甲没有一块是完好的，究竟哪里不要紧了？！
[name="杜宾"]   你不能再与她战斗了！
[Character(name="char_148_nearl_1#3",name2="char_130_doberm_ex",focus=1)]
[name="临光"]   我说了——退后！
[Character(name="char_148_nearl_1#3",name2="char_130_doberm_ex",focus=2)]
[name="杜宾"]   临光！你这倔脾气......！
[Dialog]
[Character(fadetime=1)]
[Character(name="char_011_talula_1",block=true)]
[name="塔露拉"]   ——哦？
[Character(name="char_014_riope")]
[name="Ace"]   蹲下！
[Dialog]
[Character]
[PlaySound(key="$d_gen_thunders_amb", volume=0.5)]
[PlaySound(key="$b_char_defboost", volume=0.5, Delay=0.4)]
[PlaySound(key="$d_gen_thunders_amb", volume=0.2, Delay=0.7)]
[PlaySound(key="$flashback", volume=0.2, Delay=0.7)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, block=false)]
[Blocker(a=0.3, r=1, g=0.4, b=0.4, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0.3, r=1, g=0.4, b=0.4, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0.1, r=1, g=0.4, b=0.1, afrom=1, rfrom=1, gfrom=0.4, bfrom=0.4, fadetime=0.2, block=true)]
[Blocker(a=0.1, r=0, g=0, b=0, afrom=0.8, rfrom=1, gfrom=1, bfrom=1, fadetime=0.3, block=true)]
[Blocker(a=0

... (全文23074字符)
```

### level_main_01-10_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第十一关（后）
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1, delay=0.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Image(image="avg_11_2",x=0, y=0, xScale=1.1, yScale=1.1, fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Dialog]
[Delay(time=0.6)]
[name="杜宾"]  已经突破了整合运动的拦截！
[name="临光"]  但是——他们——
[name="临光"]  ......我......啊......
[Background]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Character(name="char_148_nearl_1#3", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]  嘘。
[name="杜宾"]  ......别让阿米娅她们听见。
[Character(name="char_148_nearl_1#7", name2="char_130_doberm_ex", focus=1)]
[name="临光"]  阿米娅心里清楚得很！她比我们想象的成熟得多......！
[name="阿米娅"]  ......唔......
[name="阿米娅"]  ......嗯......？
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Image]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(name="char_148_nearl_1#3", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]  就算这样，也不能让她听见！
[name="杜宾"]  再去加深她内心的煎熬是不明智的。她已经背负......太多东西了。
[name="杜宾"]  ......不要让......他们的努力白费！
[name="杜宾"]  既然他们让我们活下来，我们就应该让博士和阿米娅......安全回去。
[Character(name="char_148_nearl_1#2", name2="char_130_doberm_ex", focus=1)]
[name="临光"]  ......
[name="临光"]  是的。
[Character(name="char_148_nearl_1#2", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]  还不是垂头丧气的时候。
[name="杜宾"]  作为耀骑士，无论在什么时候，都该成为指引众人的光吧？
[Character(name="char_148_nearl_1#4", name2="char_130_doberm_ex", focus=1)]
[name="临光"]  ——
[name="临光"]  ——我不清楚。但，我会去做我该做的事。
[Character(name="char_148_nearl_1#3")]
[name="临光"]  重整队形！不要懈怠！我们就快到了！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  ......
[name="杜宾"]  呵......
[name="杜宾"]  嘴里说着让我放心的人，真的一个都没回来过。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Background(image="bg_cher_2", width=1, height=1, fadetime=1, block=true)]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  ......
[name="阿米娅"]  {@nickname}博士......？发生了......什么......
[name="阿米娅"]  请，请放我......放我下来吧......
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[CameraShake(duration=2, fadeout=true, xstrength=2, ystrength=5, vibrato=10, randomness=90, block=true)]
[name="阿米娅"]  嗯，没问题我可以自己走......
[name="阿米娅"]  我只是......失去意识了一会儿......没事的。
[name="阿米娅"]  ......我们逃出来了吗？
[name="阿米娅"]  Ace他们......
[Decision(options="......",values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  是嘛。
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]  没关系的。如果是Ace的话，一定没问题的。
[name="阿米娅"]  罗德岛的大家，都是很强的。
[name="阿米娅"]  已经，快到南方出口了。只要撤出切尔诺伯格，我们就......
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]  我们......就......
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  ......
[name="阿米娅"]  博士......能......让我靠一下吗......
[name="阿米娅"]  一下......一下就好......
[name="阿米娅"]  ......
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Background(image="bg_cher_10", width=1, height=1, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_011_talula_1")]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[name="塔露拉"]  ————
[name="塔露拉"]  难缠。
[Character(name="char_1507_Mephisto_1#2")]
[name="梅菲斯特"]  ......
[name="梅菲斯特"]  竟然......能，能做到这一步......这家伙......
[name="梅菲斯特"]  半个街区被烧成焦炭，整个广场都陷入火海......钢铁被融化又重新凝固......
[name="梅菲斯特"]  但他为什么......还能战斗？
[Character(name="char_1505_frstar_1")]
[name="？？？"]  奋战至尸骨无存——了不起。
[Background( fadetime=4, block=false)]
[Character(name="char_011_talula_1")]
[name="塔露拉"]  我记住了。
[Delay(time=0.6)]
[name="塔露拉"]  ......罗德岛。
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_01-12_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第十二关（前）
[name=""]   时间未知 \ 天气未知 \ 能见度 低 
[name=""]   切尔诺伯格 行动组E0所在地
[name=""]   Dr.{@nickname}营救行动 最终撤退阶段 
[dialog]
[Background(image="bg_cher_3", width=1, height=1, fadetime=1, screenadapt="coverall")]
[stopmusic(fadetime=1)]
[Delay(time=1)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   可恶！
[name="杜宾"]   明明已经在出口了！
[Character(name="char_1504_cqbw#2")]
[name="？？？"]  这么轻松就想离开切尔诺伯格......
[name="？？？"]  你们的白日梦，总该有人来戳醒吧？
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   通讯设备已经恢复，我联系上了接应的行动预备组，他们正准备与我们汇合！
[name="杜宾"]   可是，这个家伙......
[Character(name="char_148_nearl_1#3")]
[name="临光"]  小心她手中的爆破物！
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[character(fadetime=0)]
[Dialog(fadetime=0)]
[PlaySound(key="$d_sp_ballista",volume=0.7)]
[Blocker(a=1, r=100, g=100, b=100, fadetime=0.1,block=true)]
[CameraShake(duration=1, xstrength=3, ystrength=5, vibrato=30, randomness=90, fadeout=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
[Delay(time=1)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   但是，我还是联系不上侦查小组！
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  ——你究竟是谁？
[Dialog]
[Character]
[Character(name="char_1504_cqbw",fadetime=1)]
[Delay(time=1)]
[name="？？？"]  你不认识我很正常——
[name="？？？"]  不过，我认识你身边那个人。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  整合运动......还要，继续战斗吗？
[Character(name="char_002_amiya_1#7", name2="char_1504_cqbw", focus=2)]
[name="？？？"]  唉唉，别这样。
[name="？？？"]  我和那个塔露拉龙女可合不来。毕竟我并不是专职守门的人啊。做完了自己的工作赶过来也是很累的！
[name="？？？"]  为了搞好关系，我们互换姓名吧？
[name="？？？"]  你可以叫我——W。
[name="W"]  为了见你身边那个人，我在这里可是等了好久呢。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  ——博士？
[Character(name="char_002_amiya_1#7", name2="char_1504_cqbw", focus=2)]
[name="W"]  Dr.{@Nickname}......
[name="W"]  我有些问题想要问问{@Nickname}，能不能请各位把他......直接送给我呢？
[stopmusic(fadetime=1)]
[Character(name="char_148_nearl_1#1")]
[name="临光"]  你在浪费你自己的时间。
[Character(name="char_148_nearl_1#8", name2="char_1504_cqbw", focus=2)]
[name="W"]  ——别急嘛。我也有些你们会感兴趣的情报哦。
[name="W"]  其实，我们刚刚遇到了不少身手很利落的家伙......和你们的穿着打扮差不多。
[name="W"]  虽然做过伪装，但也就是骗骗乌萨斯人的程度，这点小把戏，可是难不倒我的~
[Character(name="char_002_amiya_1#2", name2="char_1504_cqbw", focus=1)]
[name="阿米娅"]  侦察小队的各位吗......？
[name="阿米娅"]  太好了......他们平安无——
[Character(name="char_002_amiya_1#2", name2="char_1504_cqbw", focus=2)]
[name="W"]  小兔子，你就是他们的组织者吧？
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]  ？！
[Character(name="char_002_amiya_1#1", name2="char_1504_cqbw", focus=2)]
[name="W"]  我很想知道，你究竟有什么魔力......能让他们都心甘情愿，毫无价值地为你送命？
[Character(name="char_002_amiya_1#7", name2="char_1504_cqbw", focus=1)]
[name="阿米娅"]  什么......你想说什么？
[Character(name="char_1504_cqbw")]
[name="W"]  没错，他们——没有一个人能跟着你回去哦。
[name="W"]  你呀......
[name="W"]  你真的......配得上别人的牺牲吗？
[PlayMusic(intro="$m_bat_game02_intro", key="$m_bat_game02_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  ————
[Decision(options="别管她，出口就在前方！;阿米娅......;你的行为，有什么意义吗，W？", values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_1504_cqbw")]
[name="W"]  还没轮到你。
[name="W"]  阿米娅......
[name="W"]  ————你。生气了吗？
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  ......你不该说这种话。
[Character(name="char_1504_cqbw")]
[name="W"]  好啊，好啊......就该这样嘛。
[name="W"]  来吧。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  整合运动的W，你不该说这种话！
[name="阿米娅"]  每个人的生命，都有价值......
[name="阿米娅"]  这不是你能玷污的事！
[name="阿米娅"]  博士！！
[Decision(options="罗德岛，准备战斗！", values="1")]
[Predicate(references="1")]
[Character(name="char_1504_cqbw")]
[name="W"]  哼哼......
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_01-12_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第十二关（后）
[Background(image="bg_cher_3", width=1, height=1, fadetime=1)]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Delay(time=1)]
[Character(name="char_1504_cqbw")]
[name="W"]  这个感觉......真是让人感到，十分熟悉啊。
[name="W"]  阿米娅，是吗。
[name="W"]  ——
[name="W"]  啊，啊，哈哈......是这样......原来是这样。
[name="W"]  我记住了，阿米娅。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  ......什么？
[Character(name="char_1504_cqbw")]
[name="W"]  我已经得到我想要的了。你们可以走了，快走哦。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  你——！
[Character(name="char_1504_cqbw",name2="char_1002_nsabr_2",focus=2)]
[name="整合运动成员"]  W......？
[Character(name="char_1504_cqbw",name2="char_1002_nsabr_2",focus=1)]
[name="W"]  ——你们，要留下来送死？我没问题哦，你们爱怎么样就怎么样。
[Character(name="char_1504_cqbw",name2="char_1002_nsabr_2",focus=2)]
[name="整合运动成员"]  ......
[name="整合运动成员"]  ......撤回下城区。放他们走。塔露拉的命令。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  ......？
[Character(name="char_1504_cqbw")]
[name="W"]  算了，事情再拖下去，就要变得没趣了。我很讨厌无聊的，就这样。
[name="W"]  我还是挺期待下次再会的哦，阿米娅。
[name="W"]  还有——那个人。
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]  什么——？！
[Character(name="char_1504_cqbw")]
[name="W"]  下次，我会从你身上得到真相的，{@Nickname}。
[name="W"]  再见~
[PlaySound(key="$d_gen_walk_n", volume=1.1)]
[Dialog(fadetime=1)]
[Character(fadetime=1)]
[Delay(time=1)]
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  ......为什么......她在......做什么？
[Delay=0.5]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  整合运动......撤退了。
[name="杜宾"]  ————已经超出了预定时间。
[name="杜宾"]  立刻......撤回罗德岛。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  ......
[name="阿米娅"]  ......我来......护送后方干员。
[Character(name="char_148_nearl_1")]
[name="临光"]  阿米娅......
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]  我没事。
[Character(name="char_148_nearl_1")]
[name="临光"]  ......好。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  去吧，阿米娅。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[delay(time=1)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.5, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Background(image="bg_cher_7", width=1, height=1, fadetime=0)]
[Character(name="char_014_riope", name2="char_013_riop", focus=2)]
[Blocker(a=0, fadetime=3, block=false)]
[name="近卫干员"]  .........
[name="近卫干员"]  ...............
[name="近卫干员"]  ......头儿......？
[name="近卫干员"]  其他人呢......
[Character(name="char_014_riope", name2="char_013_riop", focus=1)]
[name="Ace"]  临光杜宾她们，已经带着阿米娅和Dr.{@nickname}突破了封锁。
[name="Ace"]  而留下来断后的小队的干员们......
[name="Ace"]  ......都阵亡了。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(fadetime=0)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Background(image="bg_cher_7", width=1, height=1, fadetime=0)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="char_014_riope", name2="char_013_riop", focus=2)]
[name="近卫干员"]  ......什么......
[Character(name="char_014_riope", name2="char_013_riop", focus=1)]
[name="Ace"]  你我是最后两个活着的。
[Character(name="char_014_riope", name2="char_013_riop", focus=2)]
[name="近卫干员"]  ......我想起来了......那个......那个怪物塔露拉......仅仅一个人......
[name="近卫干员"]  近卫们竟然眨眼间就像棋子一样迸散横飞.......
[name="近卫干员"]  那个怪物像捏黄油一样捏碎了重装干员......
[Character(name="char_014_riope", name2="char_013_riop", focus=1)]
[name="Ace"]  别出声。你伤得很重。
[Character(name="char_014_riope", name2="char_013_riop", focus=2)]
[name="近卫干员"]  天灾......！她就是天灾的化身......否则，否则火力小组怎么可能一瞬间被焚烧成灰......
[name="近卫干员"]  明明见识过她的法术，我却......我不能相信......我......
[name="近卫干员"]  惨叫......唔......呜......
[Character(name="char_014_riope")]
[CameraShake(duration=0.5, xstrength=15, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[name="Ace"]  少说点！
[Character(name="char_014_riope", name2="char_013_riop", focus=2)]
[name="近卫干员"]  ......抱歉......我......我没法......
[Character(name="char_014_riope", name2="char_013_riop", focus=1)]
[name="Ace"]  冷静。
[name="Ace"]  我帮你应急处理了一下。
[Character(name="char_014_riope", name2="char_013_riop", focus=2)]
[name="近卫干员"]  ......头儿......你的手......？
[Character(name="char_014_riope", name2="char_013_riop", focus=1)]
[name="Ace"]  至少还有一只是能用的。
[Character(name="char_014_riope", name2="char_013_riop", focus=-1)]
[Dialog]
[Delay(time=0.6)]
[Character(name="char_014_riope", name2="char_013_riop", focus=2)]
[name="近卫干员"]  ......头儿，逃吧。你的话，一定能够杀出去。
[Character(name="char_014_riope", name2="char_013_riop", focus=1)]
[name="Ace"]  我们只拖了那个怪物几分钟。
[name="Ace"]  Dr.{@nickname}和阿米娅安全之前，我不能走。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(fadetime=0)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Background(image="bg_cher_7", width=1, height=1, fadetime=0)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="char_014_riope")]
[name="Ace"]  我得先阻止那个怪物。
[Character(name="char_014_riope", name2="char_013_riop", focus=2)]
[name="近卫干员"]  头儿......我也......
[Character(name="char_014_riope", name2="char_013_riop", focus=1)]
[name="Ace"]  你的命是我废了一只手换回来的。
[name="Ace"]  哪怕你只能再活一分钟，我也希望这只手，至少也值一分钟。
[Character(name="char_014_riope", name2="char_013_riop", focus=2)]
[name="近卫干员"]  ——
[Character(name="char_014_riope", name2="char_013_riop", focus=1)]
[name="Ace"]  我去去就回。照顾好自己。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(fad

... (全文8640字符)
```

### level_main_02-01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第十三关（前）
[stopmusic]
[name=""]   5:57 a.m. \ 多云 \ 能见度 17公里 
[name=""]   龙门外环外4公里，荒漠 
[name=""]   切尔诺伯格营救行动 结束后4天 
[dialog]
[delay(time=1)]   
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[image(image="bg_2_call", fadetime=2)]
[name="PRTS"]   Dr.{@nickname}, 早上好。您已经休息了99999999————
[name="PRTS"]   ————个小时。
[name="PRTS"]   虽然我知道您很不愿意起床，不过有人需要您立刻前往作战会议室。
[name="PRTS"]   另外来自凯尔希医生的医学建议，希望您多开窗保持通风，并且进入甲板晒太阳以平衡维生素D。
[dialog]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0, block=true)]
[Image(fadetime=0)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[delay(time=1.5)]
[Background(image="bg_bridge", width=1, height=1, fadetime=1, screenadapt="coverall")]
[PlaySound(key="$d_gen_soldiersrun",volume=0.4)]
[delay(time=1.4)]
[delay(time=2)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1, delay=0.5)]
[Blocker(a=0, fadetime=2, block=true)]
[Delay(time=1.4)]
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   啊，是博士！早啊。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  {@nickname}博士，你来了。
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   博士身体好些了吗？
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   昨天看你好像还有些伤痛，行动不太方便。
[Decision(options="我已经完全恢复了。你呢？", values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   感觉今天活力满满的，已经没什么问题了！
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   毕竟接下来，我们还有别的任务......
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   需要早点做好准备。博士也要把快速调整当成常态哦。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  博士。
[name="杜宾"]  之前我们在切城的行动，虽然遭受了很大损失，但是获得了不少关于整合运动的情报，而且还救出了博士您。
[name="杜宾"]  根据昨天会谈的结果，我们最近的移动城市————“龙门”，已向我们发送了一份合作框架协议，同意与我们交换情报。
[name="杜宾"]  而有迹象显示“龙门”已经成为整合运动下一个行动目标。
[name="杜宾"]  关于其他的内容，还需经过尚在龙门城内的凯尔希医生同意后，才能定下来。
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   龙门暂时答应了我们停泊在城市附近的要求，然后他们愿意给予一部分我们在行动中损失的物资，以及消耗的补给。
[name="阿米娅"]   作为交换，罗德岛需要协助龙门，进行城市外环的一些临时性防卫工作。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   不过今天这么早是因为......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  我来说吧，阿米娅。
[name="杜宾"]  从昨天晚上开始，又有一波切尔诺伯格的幸存者在荒野中被发现，他们正在移动前往龙门，预计下午到达。
[name="杜宾"]  和之前几天一样，我们仍然需要对龙门5区的外围进行防卫工作，只不过这次，可能会混入更多的整合运动。
[name="杜宾"]  战况有所不同，我们在出发之前需要告诉您一种新的战术策略。
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]  那么博士，今天还请多多指教......
[name="阿米娅"]  加油！
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  那么......
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Background(image="bg_0_rhodes3", fadetime=0, screenadapt="coverall", screenadapt="coverall")]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[name="杜宾"]  请你们各自完成出发前的准备。博士请把准备好的编队配置命令下达给其他干员，让他们做好准备。
[name="杜宾"]  完成演习后15分钟出发。
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[dialog]
[image(fadetime=0)]
[Delay(time=0.4)]
[name="杜宾"]  这次，千万不要迟到。
```

### level_main_02-01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第十三关（后）
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.6, block=true)]
[PlayMusic(intro="$mist_loop", key="$mist_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Character(fadetime=0)]
[Background(image="bg_lungmen_station", width=1, height=1, fadetime=0)]
[name=""]   10:14 p.m. \ 晴 \ 能见度 19公里 
[name=""]   龙门5区外 检疫口
[Dialog]
[delay(time=1)]
[Character(name="char_015_lmg")]
[name="？？？"]   长官。
[Blocker(a=0, fadetime=0.6, block=true)]
[name="？？？"]   他们来了。
[Character(name="char_010_chen_1", name2="char_015_lmg", focus=1)]
[name="？？？"]   ......
[Dialog]
[Character(fadetime=0.6)]
[PlaySound(key="$radio")]
[name="广播"]   请注意——
[name="广播"]   受天灾影响，龙门全域处于停航状态。龙门5区所有入城关口将于2小时后关闭。
[name="广播"]   请积极配合工作人员进行矿石病检疫。
[name="广播"]   一旦发现任何未经登记的感染者，请广大市民立刻向最近的警员通报，
[name="广播"]   近卫局将依照《紧急处理法案》依法对其进行拘捕。
[name="广播"]   请注意——
[PlaySound(key="$radio")]
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]   和传闻中一样......
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   走吧，博士。
[name="阿米娅"]   我们到了。
[Delay(time=1)]
[Character(name="char_010_chen_1")]
[name="？？？"]   罗德岛与近卫局约好在十点见面。
[name="？？？"]   现在是十点十四。
[Character(name="char_010_chen_1#4")]
[name="？？？"]   你们迟到了十四分钟，无谓地浪费了我十四分钟时间。
[Character(name="char_010_chen_1", name2="char_002_amiya_1", focus=2)]
[name="阿米娅"]   ......抱歉，陈长官，这片区域刚才有整合————
[Character(name="char_010_chen_1", name2="char_002_amiya_1", focus=1)]
[name="陈"]   行了，我知道。不过这些都不重要。
[Character(name="char_010_chen_1")]
[name="陈"]   ——这个人是？
[Character(name="char_010_chen_1", name2="char_002_amiya_1", focus=2)]
[name="阿米娅"]   Dr.{@nickname}是罗德岛的顾问。凯尔希医生应该通知过龙门的各位。
[Character(name="char_010_chen_1")]
[name="陈"]   哼.......
[name="陈"]   好了，人已经到齐，现在你们需要跟我去见——
[Character(name="char_010_chen_1", name2="char_015_lmg", focus=2)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.4)]
[name="近卫局队员"]   陈长官！不好了！不好——感染者——那又——
[Character(name="char_010_chen_1#4", name2="char_015_lmg", focus=1)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=15, randomness=90, fadeout=true, block=false)]
[name="陈"]   慌什么！
[name="陈"]   一队，戒备！狙击队员，就位！
[Dialog]
[Character(fadetime=0)]
[name="普通市民"]   发生，发生什么了！
[name="感染者"]   放开我！！
[Character(name="char_010_chen_1")]
[name="陈"]   啧......怎么回事，汇报情况。
[Dialog]
[Character(fadetime=0)]
[CameraShake(duration=1.5, xstrength=10, ystrength=12, vibrato=15, randomness=90, fadeout=true, block=false)]
[name="感染者"]   让我过去！！为什么要抓我！！
[name="感染者"]   我们不是怪物！！！
[Character(name="char_010_chen_1", name2="char_015_lmg", focus=2)]
[name="近卫局队员"]   有感染者——不服从管理——我们——
[Character(name="char_010_chen_1", name2="char_015_lmg", focus=1)]
[name="陈"]   ......我自己都看到了。
[name="陈"]   算了。
[Character(name="char_010_chen_1", name2="char_015_lmg", focus=1)]
[name="陈"]   把他们全部拘押。
[name="陈"]   立刻疏散人群，半小时后通过复查流程后，再开放关口。
[name="陈"]   还有，把检疫口检查线向前推四十米。
[Character]
[Dialog]
[Delay(time=0.4)]
[Character(name="char_010_chen_1#4")]
[name="陈"]   罗德岛的，除了你和Dr.{@nickname}，其他人不需要一起同行，留在这里协助龙门边防进行驻守。
[name="陈"]   要是连这点小事都处理不好，无论是什么任务，我可都没法交给你们。
[name="陈"]   PC94172，你给这些人安排一下任务，今晚不要再出乱子了。
[Character(name="char_010_chen_1", name2="char_015_lmg", focus=2)]
[name="近卫局队员"]   明白，陈警司！
[Character(name="char_015_lmg")]
[name="近卫局队员"]   诸位，请注意......
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[Character(fadetime=2)]
[Character(name="char_002_amiya_1#5")]
[name="阿米娅"]   ......
[name="阿米娅"]   （陈长官真的很严格......比我想象的要严格......）
[Decision(options="......（点头）", values="1")]
[Predicate(references="1")]
[Character(name="char_010_chen_1#4")]
[name="陈"]   你们，
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.4, block=true)]
[name="陈"]   跟我来。——
[Blocker(a=1, r=0, g=0, b=0, fadetime=2,block=true)]
[Background]
[Dialog]
[Character(fadetime=0)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[Character(name="char_010_chen_1")]
[name="陈"]   到了。
[Character(fadetime=0)]
[Delay(time=0.5)]
[Dialog]
[Background(image="bg_lungmen_n",x=40, y=0, fadetime=1, xScale=1.3, yScale=1.3)]
[Delay(time=0.5)]
[BackgroundTween(xFrom=40, yFrom=0, xTo=40, yTo=-150, duration=4, block=true)]
[Delay(time=1)]
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]   好，好高的建筑！
[Character(name="char_010_chen_1")]
[name="陈"]   ......
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]   唔......
[Character(name="char_002_amiya_1#5")]
[name="阿米娅"]   对，对不......
[Character(name="char_010_chen_1")]
[name="陈"]   ——罗德岛的身手还算不错。
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   啊......
[name="阿米娅"]   谢谢陈长官夸奖。
[Character(name="char_010_chen_1")]
[name="陈"]   只不过——
[name="陈"]   切尔诺伯格事件发生之后，什么人都疯了一样地向龙门跑。
[name="陈"]   感染者就该清楚，来龙门会有什么下场。
[Character]
[Dialog]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Background(image="bg_lungmen_o", width=1, height=1, fadetime=0, screenadapt="coverall")]
[Blocker(a=0, fadetime=1, block=true)]
[name="？？？"]   我再提醒你一次。
[name="？？？"]   龙门就是下一个切尔诺伯格。
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   是凯尔希医生......！
[Character(name="char_010_chen_1")]
[name="陈"]   你们罗德岛的代表已经和魏长官先行接触了。
[name="陈"]   在这里等着。
[name="陈"]   我一会儿通知你们。
[Dialog(fadetime=0.6)]
[Character(fadetime=0.6)]
[Delay(time=1)]
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   呼......那个陈警官，真的很难应付呢。
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   博士，接下来的交涉就交给凯尔希医生。
[name="阿米娅"]   请相信她吧。
[Dialog(fadetime=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_02-02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第十四关（前）
[name="陈"]   进来吧。
[Delay(time=0.3)]
[PlaySound(key="$d_gen_dooropen", volume=0.7)]
[character]
[Dialog]
[Background(image="bg_lungmen_o", width=1, height=1, fadetime=2)]
[PlayMusic(intro="$mist_loop", key="$mist_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Character(name="char_003_kalts_1",name2="char_2005_weiyw_1")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   ......凯尔希医生！
[Character(name="char_003_kalts_1")]
[Delay(time=0.6)]
[name="凯尔希"]   ——阿米娅......
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]   ......{@nickname}。
[name="凯尔希"]   你来了。
[PlaySound(key="$d_gen_doorclose", volume=0.5)]
[Delay(time=1)]
[Character(name="char_003_kalts_1#3", focus=-1)]
[Decision(options="......", values="1")]
[Predicate(references="1")]
[Character(name="char_010_chen_1")]
[name="陈"]   咳咳。
[name="陈"]   魏长官，罗德岛的另外两位代表也到了。
[Character]
[Dialog]
[Character(name="char_2005_weiyw_1")]
[Delay(time=1)]
[name="魏彦吾"]   哦，正好。
[name="魏彦吾"]   请坐。凯尔希小姐正向我说明现在的局势呢。
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=1)]
[name="凯尔希"]   那我就继续吧。关于现在的局势，我想魏先生也已经很清楚了。
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Image(image="bg_0_tv",x=0, y=-20, xScale=1.1, yScale=1.1, fadetime=0)]
[ImageTween(xFrom=0, yFrom=-20, xTo=0, yTo=0, xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=7, block=false)]
[Blocker(a=0, fadetime=0.6, block=true)]
[PlaySound(key="$slideshow", volume=0.2,channel="2", loop=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[name="凯尔希"]   龙门的情报网每天都在搜集大量针对整合运动的信息，想必也对这件事情极为重视。
[name="凯尔希"]   不过仅凭这样，龙门仍然还缺乏一些关键信息。
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[image]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_003_kalts_1", name2="char_010_chen_1", focus=2)]
[name="陈"]   ......
[Character(name="char_003_kalts_1", name2="char_010_chen_1", focus=1)]
[name="凯尔希"]   简单的感染者检疫是不能对抗整合运动的，想必龙门近卫局再清楚不过。
[name="凯尔希"]   整合运动不会乖乖过检，更不会等到当局反应过来才行动。所以————
[name="凯尔希"]   如果没有罗德岛的协助，龙门依靠目前对待感染者的策略，抵挡接下来整合运动的攻击会面临巨大损失。
[Character(name="char_003_kalts_1", name2="char_010_chen_1", focus=2)]
[name="陈"]   抱歉，我需要插一句。
[name="陈"]   关于龙门的防卫情报，龙门近卫局方面比罗德岛更了解。对于整合运动的渗透，也已经做了相应准备。
[name="陈"]   只是龙门目前没有将相关机密行动的方针通知罗德岛的义务。
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=2)]
[name="魏彦吾"]    ......
[name="魏彦吾"]    凯尔希小姐，请继续说。
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=1)]
[name="凯尔希"]   龙门的确有对付手无寸铁的感染者的经验，但恐怕龙门目前没有面对集团化感染者暴徒的经验，这可能会让龙门造成不必要的损失。
[name="凯尔希"]   以罗德岛目前的经验来说————只有感染者，才能更好对抗感染者。
[Character(name="char_2005_weiyw_1")]
[name="魏彦吾"]   那么，罗德岛是否已经从针对整合运动的行动中获得了有效的经验？
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Image(image="bg_0_rhodes2",x=0, y=0, xScale=1.2, yScale=1.2, fadetime=0)]
[ImageTween(xFrom=0, yFrom=-0, xTo=0, yTo=0, xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1, yScaleTo=1, duration=27, block=false)]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=1)]
[name="凯尔希"]   仅仅是有而已，大概是不敢自称专家的。
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=2)]
[CharacterCutin(widgetID="1", name="char_2005_weiyw_1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=300, width=200, block=true)]
[name="魏彦吾"]   哦——？
[name="魏彦吾"]   我听说，罗德岛曾卷入过切尔诺伯格事件，并且从中也获得了不少整合运动的其他情报。
[CharacterCutin(widgetID="1", fadetime=0.5, block=true)]
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=1)]
[CharacterCutin(widgetID="1", name="char_003_kalts_1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=-300, width=200, block=true)]
[name="凯尔希"]   无论魏先生是从哪里得到这条消息的——
[name="凯尔希"]   这都不是现阶段能与龙门交换的信息。这只是履历，只是站在这里与魏先生交谈的资格。
[CharacterCutin(widgetID="1", fadetime=0.5, block=true)]
[name="魏彦吾"]   决定是否要和你们进行利益交换的是龙门。如果这种程度的信息罗德岛都无法提供的话——
[name="魏彦吾"]   呵。
[name="魏彦吾"]   龙门将无法信任你们的真实实力。
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[character]
[image]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=1)]
[name="凯尔希"]   魏先生，我的言辞可能不够清晰。
[name="凯尔希"]   不过需要强调的是——罗德岛提供的信息，本身就是用实力换来的。
[Character(name="char_003_kalts_1", name2="char_010_chen_1", focus=2)]
[name="陈"]   但，无论怎样，龙门都无法信任同样是一群感染者的罗德岛。
[Character(name="char_003_kalts_1", name2="char_010_chen_1", focus=1)]
[name="凯尔希"]   如果陈小姐认为龙门的安危，尚不如对感染者进行盲目的惩罚来得重要————
[name="凯尔希"]   那我会立刻服从本地法令，任由陈小姐逮捕我，然后在监牢里看着龙门被整合运动焚烧殆尽，默默惋惜。
[name="凯尔希"]   这次，龙门别无选择。
[Character(name="char_003_kalts_1", name2="char_010_chen_1#5", focus=2)]
[Blocker(a=0.6, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=15, randomness=90, fadeout=true, block=false)]
[name="陈"]   ——龙门既不是因为有人出言不逊就拒绝善意的城市——
[name="陈"]   却也不是收留无用说客的慈善机构。
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1#5", focus=1)]
[name="魏彦吾"]   陈警官。
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1#5", focus=2)]
[name="陈"]   魏长官，让外来的感染者参与龙门的机密事务，我认为并不妥当。
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1#5", focus=1)]
[name="魏彦吾"]   冷静些，陈警官，他们是客人。
[name="魏彦吾"]   ——我的客人。
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1#5", focus=2)]
[name="陈"]   .....
[name="陈"]   是。
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1", focus=2)]
[name="陈"]   在他们违反龙门法律之前，我会容忍，长官。
[Character(name="char_2005_weiyw_1", name2="char_003_kalts_1", focus=1)]
[name="魏彦吾"]   啊，不好意思。我想起来了，有这么一句——
[name="魏彦吾"]   ——没错，呣......
[name="魏彦吾"]   我所看重的就只有一点。
[name="魏彦吾"]   实力。
[name="魏彦吾"]   据我所知，罗德岛也参与清剿了附近的感染者吧？
[name="魏彦吾"]   陈警官，以目前确切了解的情报，罗德岛在军事力量的实力如何？
[Character(name="char_010_chen_1")]
[name="陈"]   ......请容我简要描述一下我所见的罗德岛的行动情况。
[name="陈"]   ——详情如下——
[stopSound(channel="2", fadetime=1)]
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_main_02-02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第十四关（后）
[Background(image="bg_lungmen_o", width=1, height=1, fadetime=1, screenadapt="coverall")]
[PlayMusic(intro="$mist_loop", key="$mist_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Delay(time=1)]
[Character(name="char_010_chen_1")]
[name="陈"]   ——以上就是此次战斗的全过程。
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1", focus=1)]
[name="魏彦吾"]   你的评价？
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1", focus=2)]
[name="陈"]   他们的实力确实合格了。
[name="陈"]   但魏长官，无论是在战略层面，还是关于他们的身份，我都认为......
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1", focus=2)]
[name="陈"]   ......龙门近卫局完全可以胜任接下来的任务。
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1", focus=1)]
[name="魏彦吾"]   对抗犯罪与侵略，近卫局绰绰有余。
[name="魏彦吾"]   虽然罗德岛也能提供更多的可能性。但是......
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1", focus=1)]
[name="魏彦吾"]   罗德岛所要求的“东西”里有一样，可不是目前罗德岛给出的条件可以交换的。
[name="魏彦吾"]   哪怕是仅仅在临时防卫上的合作，也完全无法与之等价。相比之下，罗德岛的“要价”有点太高了。
[name="魏彦吾"]   我想凯尔希小姐和阿米娅小姐很清楚吧。
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=1)]
[name="凯尔希"]   魏先生，仅仅防卫是不够的。整合运动还有很多你不知道的信息。
[name="凯尔希"]   根据我们交战的情况推测，若不采取主动措施，整合运动将在未来数周内攻陷龙门。
[Character(name="char_010_chen_1#4")]
[name="陈"]   ......危言耸听。没有任何证据可以表明——
[Character(name="char_003_kalts_1", name2="char_010_chen_1#4", focus=1)]
[name="凯尔希"]   陈警官，想知道切尔诺伯格一夜失陷的真正原因吗？
[Character(name="char_003_kalts_1", name2="char_010_chen_1#4", focus=2)]
[name="陈"]   ......
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=2)]
[name="魏彦吾"]   请说。
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=1)]
[name="凯尔希"]   阿米娅。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   啊......好的。
[name="阿米娅"]   罗德岛不仅亲历了切尔诺伯格事件，而且......我们经历了天灾，并且自灾难中活了下来。
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=2)]
[name="魏彦吾"]   真是，真是，令人尊敬。
[name="魏彦吾"]   除了一些不要命的狂人，我还真没见到过多少人能从天灾中幸存呢。阿米娅小姐，请继续说，我在听。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   ......我们与整合运动的领袖交过手。
[Character(name="char_010_chen_1#6")]
[name="陈"]   ——
[Character(name="char_2005_weiyw_1")]
[name="魏彦吾"]   嗯？她的名字是？
[name="魏彦吾"]   我记得不是那么清楚了......
[Character(name="char_2005_weiyw_1", focus=-1)]
[Decision(options="塔露拉", values="1")]
[Predicate(references="1")]
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1", focus=1)]
[name="魏彦吾"]   哦，是的，塔露拉。
[name="魏彦吾"]   陈警官，你认为呢？
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1#5", focus=2)]
[name="陈"]   ————
[name="陈"]   我——知道。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   ......这就是罗德岛在切尔诺伯格的经历。遭受天灾的切城虽然脱离了乌萨斯的控制————
[name="阿米娅"]   但是他们会需要扩张，此时仍然有大量物资缺口。而龙门是他们的下一个跳板。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   虽然龙门的确可以阻止一系列破坏行动，如果无法在未来主动出击的话，整合运动对龙门的攻击将持续不断——
[name="阿米娅"]   而且......最难以搞清楚的，其实是失去了切城的乌萨斯帝国他们对此事的态度......
[Character(name="char_2005_weiyw_1")]
[name="魏彦吾"]   呵呵......小姑娘，你说的不错。
[name="魏彦吾"]   出于局势紧张，以及龙门近卫局人手有限，我可以以之前的临时协议为基础，考虑一下你们的具体方案。
[name="魏彦吾"]   但正如我刚才所说——
[Dialog]
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]   ......
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=1)]
[name="凯尔希"]   ......罗德岛的要价太高，是吗？
[Character(name="char_2005_weiyw_1")]
[name="魏彦吾"]   正是如此。
[name="魏彦吾"]   为了弥补龙门的支出，我的条件啊，也很简单，只有两条。
[name="魏彦吾"]   第一，罗德岛必须帮助近卫局解除整合运动对龙门的威胁。其中包括确认龙门内的威胁以及处理关于切城的相关问题。
[name="魏彦吾"]   还有所谓的感染者的渗透状况什么的。总之无论有什么样的有利情报，我需要你们同步共享给龙门。
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=1)]
[name="凯尔希"]   ——那，第二个要求是？
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=2)]
[name="魏彦吾"]   第二个，要等你们完成了首要任务再说。
[name="魏彦吾"]   当然，我的要求，不会超出罗德岛的能力范畴及业务内容。
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=1)]
[name="凯尔希"]   我并不能理解。我希望魏先生详细解释一下。
[Character(name="char_2005_weiyw_1")]
[name="魏彦吾"]   那就这么说吧。如果整合运动造成了超过罗德岛预期的损害——
[name="魏彦吾"]   我希望罗德岛能够协助近卫局，妥善处理，甚至参与某些部分的善后。当然，也在你们的能力范围内。这是大致的内容。
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=1)]
[name="凯尔希"]   ......
[Character(name="char_003_kalts_1", name2="char_2005_weiyw_1", focus=2)]
[name="魏彦吾"]   在这个点上，我尚不能细说。不过请不要忘了，罗德岛没有选择。
[name="魏彦吾"]   如果不能接受，那么我觉得我们之前的所有说的条件，以及你们想要的都......
[Character(name="char_003_kalts_1")]
[name="凯尔希"]   阿米娅？
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  凯尔希医生......
[name="阿米娅"]  魏先生，我希望将这一条也写入合约......
[name="阿米娅"]  “在诠释条例时，由双方共同参与讨论。”————这样可以吗？
[Character(name="char_2005_weiyw_1")]
[name="魏彦吾"]   哦，哦......当然可以。这是对龙门的尊重呢，阿米娅小姐。
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1", focus=1)]
[name="魏彦吾"]   陈警官，你有什么意见？
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1", focus=2)]
[name="陈"]   ——我认可这次行动。
[Character(name="char_2005_weiyw_1", name2="char_010_chen_1", focus=1)]
[name="魏彦吾"]   呵。
[name="魏彦吾"]   看来陈警官也有了她自己的目标。
[Character(name="char_010_chen_1#6")]
[name="陈"]   ......
[Character(name="char_2005_weiyw_1")]
[name="魏彦吾"]   那么——恭喜各位，龙门信任你们。陈警官将全权负责和你们的对接事宜。
[name="魏彦吾"]   不过，感染者自由行动会引起市民的恐慌。
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.7, block=true)]
[name="魏彦吾"]   希望你们在执行任务时，能服从龙门近卫局————
[name="魏彦吾"]   尤其是陈警司的命令。
[delay(time=1)]
[stopmusic(fadetime=4)]
[name="魏彦吾"]   龙门的关口将向罗德岛敞开，只要你们一切的行动都在正轨上。
[Dialog]
[Character(fadetime=0)]
[Background(image="bg_lungmen_station", width=1, height=1, fadetime=0, screenadapt="coverall")]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1, delay=0.5)]
[delay(time=1)]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_003_kalts_1", name2="char_002_amiya_1#5", focus=2)]
[name="阿米娅"]   唔......啊......！那个大叔超难对付的......
[name="阿米娅"]   讲起话来慢条斯理，感觉他完全不为所动......
[Character(name="char_003_kalts_1", name2="char_002_amiya_1#5", focus=1)]
[name="凯尔希"]   阿米娅，你总得学会自己与他们交涉。
[name="凯尔希"]   最后，你做的还不错。
[Character(name="char_003_kalts_1", name2="char_002_amiya_1#3", focus=2)]
[name="阿米娅"]   嘿嘿......

... (全文7045字符)
```

### level_main_02-03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第十五关（前）
[PlayMusic(intro="$loading_intro", key="$loading_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Background(image="bg_lungmen_b", width=1, height=1, fadetime=1)]
[Delay(time=1)]
[Character(name="char_012_misa_1")]
[name="？？？"]   快藏起来！
[name="？？？"]   我......我必须走了。
[name="？？？"]   这个......这个，给你们。
[name="？？？"]   这是我们的护身符，是我妈妈亲手教我做的......
[name="？？？"]   给你们的这个是我做的。
[name="？？？"]   亲手做的布偶，能保证重要的人平安无事。
[Character(fadetime=0)]
[Dialog]
[name="小孩们"]   嗯，米莎姐姐，我们会好好保管它的！
[Character(name="char_012_misa_1#3")]
[name="米莎"]   真乖。
[Character(name="char_012_misa_1")]
[name="米莎"]   藏好！别出声。
[Character(fadetime=0)]
[Dialog]
[name="小孩们"]   嗯！
[Dialog]
[Delay(time=2)]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Blocker(a=0, fadetime=0.6, block=true)]
[PlaySound(key="$d_gen_soldiersrun")]
[name="暴民"]   往哪去了？！你们，追！看那些感染者还能跑多远！
[name="暴民"]   嗯？这里......看来还有些东西呢？
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   ......依据能天使的情报，任务目标一定在这附近逗留过才对......
[name="阿米娅"]   啊啊，这里的地形真是很复杂，光凭罗德岛，这个任务果然也有些麻烦呢......
[name="阿米娅"]   幸好联系了企鹅物流......
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]   ......有人？
[name="阿米娅"]   这些人是......！
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[name="小孩"]   坏蛋！你们这些坏蛋！放开我！放——开——！
[name="暴民"]   说！她往哪跑了？
[name="暴民"]   别不知好歹！
[name="小孩"]   龙姐姐！龙姐姐！你在哪里！救命啊——
[name="小孩"]   米莎姐姐！米莎姐姐，救救我！！
[name="阿米娅"]   ......
[Character(fadetime=0)]
[name="暴民"]   谁？
[name="暴民"]   别想走！
[Character(name="char_002_amiya_1#7",fadetime=1)]
[name="阿米娅"]   ......
[name="阿米娅"]   ......我劝你们，立刻离开。
[Delay(time=1)]
[Character(fadetime=0)]
[name="暴民"]   ......？！
[name="暴民"]   你——？！
[name="暴民"]   哪里来的外地人！
[name="暴民"]   你就不怕我们......
[Dialog]
[playsound(key="$p_skill_spiritexplo", volume=0.4)]
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   否则——
[Character(fadetime=0)]
[name="暴民"]   啊？
[name="暴民"]   咕啊！！
[name="暴民"]   那，那是什么？
[name="暴民"]   法术！她，她在使用法术？！
[name="暴民"]   啊啊啊！别过来！
[blocker(a=0, block=true, fadetime=0.5)]
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   ——以后别再做些欺压弱小的事情。
[Character(fadetime=0)]
[CameraShake(duration=1, xstrength=3, ystrength=4, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="暴民"]   呃呃啊，怪物！
[playsound(key="$d_gen_soldiersrun", volume=0.4)]
[CameraShake(duration=1, xstrength=5, ystrength=6, vibrato=90, randomness=90, fadeout=true, block=true)]
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   呵......怪物......吗。
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]   ......
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   好啦，没事了，都出来吧。
[name="阿米娅"]   这里危险，快去安全点的地方吧。
[Character(fadetime=0)]
[name="小孩们"]   谢谢你，兔姐姐！
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   都小心点啊！
[Delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_106_franka_1", fadetime=1)]
[name="芙兰卡"]   阿米娅，这是什么情况？
[Character(name="char_002_amiya_1", name2="char_106_franka_1", focus=1)]
[name="阿米娅"]   嗯，我看见了一个，应该也是未登记的感染者......
[Character(name="char_002_amiya_1", name2="char_106_franka_1", focus=2)]
[name="芙兰卡"]   乌萨斯人？
[Character(name="char_002_amiya_1", name2="char_106_franka_1", focus=1)]
[name="阿米娅"]   是的，乌萨斯人，她往贫民区更深处去了。
[name="阿米娅"]   芙兰卡，让附近参与搜查的干员集合。
[Character(name="char_002_amiya_1", name2="char_106_franka_1", focus=2)]
[name="芙兰卡"]   Ok。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   越往贫民区前进，形势就越复杂......
[name="阿米娅"]   一般居民，犯罪分子，未确认身份的流民......层出不穷。
[name="阿米娅"]   必须多加准备才行。
[Character(name="char_107_liskam_1")]
[name="雷蛇"]   有通信，阿米娅。
[name="雷蛇"]   请稍等一下。
[name="雷蛇"]   ——
[name="雷蛇"]   是。
[name="雷蛇"]   阿米娅，是近卫局。
[Character(name="char_002_amiya_1",name2="char_107_liskam_1",focus=1)]
[name="阿米娅"]   是陈长官？
[Character(name="char_002_amiya_1",name2="char_107_liskam_1",focus=2)]
[name="雷蛇"]   没错。
[name="雷蛇"]   ——是的，我们已经搜查出了不少非登记感染者。
[name="雷蛇"]   ——是的。
[name="雷蛇"]   ——什么？
[name="雷蛇"]   ——白色短发，乌萨斯人，少年女性，身高一米四五左右，名叫米莎？
[Character(name="char_002_amiya_1",name2="char_107_liskam_1",focus=1)]
[name="阿米娅"]   这是——？
[Character(name="char_002_amiya_1",name2="char_107_liskam_1",focus=2)]
[name="雷蛇"]   ——明白。
[name="雷蛇"]   阿米娅，陈长官要求我们，立即搜查具备这种特征的感染者。
[name="雷蛇"]   一经发现，立刻交给近卫局。
[Character(name="char_002_amiya_1",name2="char_107_liskam_1",focus=1)]
[name="阿米娅"]   请给我一下通讯设备。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   喂，喂......
[name="阿米娅"]   陈长官，你听得到吗？
[CharacterCutin(widgetID="1", name="char_010_chen_1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=-300, width=200, block=true)]
[name="陈"]   我听得到。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   我能否确认下，刚才你下达命令的有效性？
[Character(name="char_002_amiya_1",focus=0)]
[name="陈"]   真实可靠，立刻执行。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   明白了。
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[CharacterCutin(widgetID="1",fadetime=0.5,block=true)]
[name="阿米娅"]   ......
[name="阿米娅"]   突然就挂断了......
[Character(name="char_106_franka_1")]
[name="芙兰卡"]   陈长官，好硬的脾气啊。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   那这就是我们接下来所要执行的任务了。
[Character(name="char_002_amiya_1",name2="char_107_liskam_1",focus=2)]
[name="雷蛇"]   阿米娅......几位重装干员向我发来了另一条通讯。
[name="雷蛇"]   他们遭遇了对罗德岛干员展现出攻击倾向的人。
[name="雷蛇"]   而且，那些袭击者不是普通人，他们是......感染者。
[Character(name="char_002_amiya_1#6")]
[Delay=0.5]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   ......让重装干员们向我们目前所在的区域撤退。
[name="阿米娅"]   侦察小队！去追踪任务目标，白发乌萨斯少女，身高1.45米，务必注意隐蔽和安全！
[name="阿米娅"]   其他干员，跟随各自的队长散开。
[Character]
[Decision(options="以逸待劳，很好。;这是......诱敌深入？;芙兰卡小姐，我们是不是要伏击敌人？", values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_106_franka_1", name2="char_107_liskam_1", focus=1)]
[name="芙兰卡"]   哟——不错嘛。
[name="芙兰卡"]   雷蛇，这孩子很聪明呢。
[Character(name="char_106_franka_1", name2="char_107_liskam_1", focus=2)]
[name="雷蛇"]   .....

... (全文6198字符)
```

### level_main_02-03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第十五关（后）
[Background(image="bg_indoor_2", width=1, height=1, fadetime=1, screenadapt="coverall")]
[PlayMusic(intro="$loading_intro", key="$loading_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Delay(time=1)]
[Character(name="char_012_misa_1")]
[name="米莎"]   ......呼。
[name="米莎"]   ......躲在这里，就不会被发现了吧。
[name="米莎"]   就算这样，也没法再回孩子们那里去了。
[name="米莎"]   他们不会有事吧......
[name="米莎"]   唉，为什么......
[name="米莎"]   ——！
[name="米莎"]   是谁？
[Character(name="char_002_amiya_1", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   ......
[Character(name="char_002_amiya_1#2", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   是米莎小姐吗？
[Character(name="char_002_amiya_1#2", name2="char_012_misa_1#4", focus=2)]
[name="米莎"]   ......咦？
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(fadetime=0)]
[Blocker(a=0, fadetime=0.6, block=true)]
[Character(name="char_012_misa_1")]
[name="米莎"]   ......
[Character(name="char_002_amiya_1", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   抱歉，米莎小姐，希望没有吓到你......
[name="阿米娅"]   这是我的同事，芙兰卡小姐和雷蛇小姐。
[Character(name="char_106_franka_1")]
[name="芙兰卡"]   你好呀。
[Character(name="char_107_liskam_1")]
[name="雷蛇"]   中午好。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   我们是罗德岛制药。作为一个为感染者服务的组织，至少......
[name="阿米娅"]   我们也希望能帮到你什么。所以想和你，交流一下。
[Character(name="char_002_amiya_1", name2="char_012_misa_1", focus=2)]
[name="米莎"]   交流一下？
[Character(name="char_002_amiya_1#3", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   嗯。
[name="阿米娅"]   这里也不太合适......
[name="阿米娅"]   不过现在，最需要的是能保证米莎小姐你的安全。
[name="阿米娅"]   这段时间里，我们会保护你，请不用担心。
[Character(name="char_002_amiya_1", name2="char_012_misa_1", focus=2)]
[name="米莎"]   ......你在说什么......啊。
[name="米莎"]   ......
[name="米莎"]   不就是把我抓住关起来吗？！
[name="米莎"]   走开！我的爪子很锋利的......！不想受伤的话......
[Character(name="char_106_franka_1", name2="char_012_misa_1", focus=1)]
[name="芙兰卡"]   ......噗。
[Character(name="char_106_franka_1", name2="char_012_misa_1#4", focus=2)]
[name="米莎"]   你......笑什么......
[Character(name="char_106_franka_1", name2="char_012_misa_1#4", focus=1)]
[name="芙兰卡"]   如果我们真的想抓你，你是根本没机会反抗啦。
[Character(name="char_106_franka_1", name2="char_012_misa_1", focus=2)]
[name="米莎"]   ......
[Character(name="char_002_amiya_1", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   米莎小姐......我们是真的想帮助你，所以才......
[Character(name="char_002_amiya_1", name2="char_012_misa_1", focus=2)]
[name="米莎"]   我不相信你......
[name="米莎"]   龙门对待感染者，比对待罪犯还严苛！
[name="米莎"]   你凭什么，凭什么要帮助感染者？
[Character(name="char_002_amiya_1", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   ......
[Character(name="char_002_amiya_1#4", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   ——米莎小姐，你看......
[Character(name="char_002_amiya_1#4", name2="char_012_misa_1", focus=2)]
[name="米莎"]   你在——干什么？
[Character(name="char_002_amiya_1#4", name2="char_012_misa_1", focus=2)]
[name="米莎"]   ......你......
[name="米莎"]   ......你的手......
[name="米莎"]   你也是......感染者？
[Character(name="char_002_amiya_1#4", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   是的，我和你一样。
[Character(name="char_002_amiya_1#7", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   龙门贫民区藏匿着许多感染者......刚才的孩子们......她们很信任你。
[name="阿米娅"]   米莎，你已经让他们陷入了危险。
[Character(name="char_002_amiya_1#7", name2="char_012_misa_1", focus=2)]
[name="米莎"]   ......你是想用孩子们威胁我吗？
[Character(name="char_002_amiya_1#7", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   不，我不会。但已经有人这么做了......
[name="阿米娅"]   罗德岛刚刚赶走过一批胁迫孩子们的人。
[Character(name="char_002_amiya_1#7", name2="char_012_misa_1", focus=2)]
[name="米莎"]   .......！
[Character(name="char_002_amiya_1#7", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   龙门同样也在搜查感染者。等到龙门发现你的话，可能就晚了。
[name="阿米娅"]   我们想通过你把暴徒们从孩子们身边引开——
[name="阿米娅"]   另一方面，我们也可以保护你，让你不受伤害。
[Character(name="char_002_amiya_1#7", name2="char_012_misa_1", focus=2)]
[name="米莎"]   ......你知道他们为什么抓我？
[name="米莎"]   你们......又为什么要保护我？
[Character(name="char_002_amiya_1#2", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   我其实并不太清楚，为什么会有感染者针对你......
[name="阿米娅"]   但是我们也在乎无辜感染者的安全，包括你。至少这样是目前最好的解决办法。我也只能希望你能相信我。
[name="阿米娅"]   请先允许我们带你离开这里，好吗？
[Character(name="char_002_amiya_1#2", name2="char_012_misa_1", focus=2)]
[name="米莎"]   ......
[name="米莎"]   ......那就......走吧。
[name="米莎"]   毕竟，我没什么选择，是吗？
[Character(name="char_002_amiya_1", name2="char_012_misa_1", focus=1)]
[name="阿米娅"]   也不是这么说......
[name="阿米娅"]   至少，谢谢你......米莎小姐！
[Delay(time=1)]
[Dialog]
[Blocker(block=true)]
[Image]
```


> 本章节共407个脚本文件，此处展示前30个。

## 统计

- 总字符数：162767
- 对话行数：1741


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
