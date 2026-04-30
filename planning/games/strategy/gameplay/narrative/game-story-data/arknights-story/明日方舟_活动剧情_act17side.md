# 明日方舟 · 活动剧情 · act17side（34段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act17side」完整剧情脚本（34个文件，4697行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act17side
- 脚本文件数：34

### guide_act17side_tech_1

```
[HEADER(is_skippable=false, is_tutorial=true)] 科技树使用引导1
[Tutorial(target="tech_part", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_irene", dialogX=-600, dialogY=-155)] 博士，这里是你新获得的组件，可以在“小帮手”里查看。
```

### guide_act17side_tech_2

```
[HEADER(is_skippable=false, is_tutorial=true)] 科技树使用引导2
[PopupDialog(dialogHead="$avatar_irene", dialogX=-600, dialogY=-235)] 激活组件能帮助我们更好地与海嗣作战，去继续探索吧，获取更多的组件。
```

### guide_act17side_tech_3

```
[HEADER(is_skippable=false, is_tutorial=true)] 科技树使用引导3
[Tutorial(target="btn_bg_hotsport", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_irene", dialogX=-500, dialogY=107)] “小帮手”的组件还可以在此处查看和调整。
```

### level_act17side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ibchurch",screenadapt="coverall")]
[playMusic(intro="$tech_intro", key="$tech_loop",fadetime=3, volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_450_1#6$1",name2="npc_2004_Alty",fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_npc_450_1#6$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]Alty小姐！那首《着魔的重构》我真的非常喜欢！
[Character(name="avg_npc_450_1#6$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]是吗？这我倒没想到，我以为在萨尔贡雨林随便想到的点子太过先锋了来着。
[name="Alty"]不过原来那个医生有你这样的手下？我还以为你们都和她一样无趣。
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]哈哈......其他几位呢？
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]Dan跑到海边去了，她比较兴奋。Aya和Frost去了我们落脚的地方，虽然很破败，但看上去很有趣。
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]有趣......吗？
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]凯尔希有和你说我们的事情吗？
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]只是略有耳闻。似乎有什么重要的东西在各位手上。
[name="极境"]听说大名鼎鼎的日落即逝竟然私下与凯尔希医生有来往的时候，我真是吃了一惊......
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]说实话，我也吃了一惊。
[name="Alty"]不过......我很高兴这里有我们的粉丝喔，感觉让这趟旅程多了点新意。
[Character(name="avg_npc_450_1#6$1",name2="npc_2004_Alty",focus=1)]
[PlaySound(key="$d_avg_paper2",delay=1)]
[name="极境"]见到各位，感觉这一个月来遭的罪就都回本了。啊，麻烦您给这张海报也签个名......
[Character(name="avg_npc_450_1#6$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]......你啊，是抱着什么心情回到伊比利亚的？
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]说起来稍微有点复杂，而我更没想到会被日落即逝的Alty问起这个问题。
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]你喜欢我们的乐队名吗？
[Character(name="avg_npc_450_1#6$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]简直称得上热爱。
[Character(name="avg_npc_450_1#6$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]谢谢。
[name="Alty"]她在哪里？我以为她会在这里等着，摆出那种“我什么都知道”的表情，然后什么都不告诉我们。
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]我还在等凯尔希医生的联络。她应当不会比你们晚抵达太多。
[StopMusic(fadetime=3)]
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]但愿她能快些......要涨潮了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Delay(time=0.6)]
[Background(image="bg_ibindoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop",fadetime=3, volume=0.4)]
[Character(name="avg_npc_459_1#1$1",name2="char_empty",fadetime=0.5)]
[Delay(time=0.6)]
[name="男性镇民"]......外来者。都是外来者。这段时间是怎么了，难道审判庭真的放松警惕到了这个地步？
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[Character(name="avg_npc_459_1#1$1",name2="avg_npc_453_1#1$1",fadetime=1.5)]
[Delay(time=1.5)]
[Character(name="avg_npc_459_1#1$1",name2="avg_npc_453_1#1$1",focus=2)]
[name="诡异的教徒"]是的，外人，都是外人。她们都很特殊，身上有海的气息。
[Character(name="avg_npc_459_1#1$1",name2="avg_npc_453_1#1$1",focus=1)]
[name="男性镇民"]阿戈尔人？
[Character(name="avg_npc_459_1#1$1",name2="avg_npc_453_1#1$1",focus=2)]
[name="诡异的教徒"]像是，可又不是，我们的兄弟姐妹都感到恐惧。
[name="诡异的教徒"]我们必须抓紧，审判庭极少如此疏忽......太可疑了，可哪怕现在这片海域的松懈是审判庭的陷阱，我们也必须义无反顾。
[name="诡异的教徒"]为了帮助我们的兄弟姐妹，为了重建使者与陆地的联系，我们必须先一步夺得伊比利亚之眼的控制权......或者是摧毁它！
[name="诡异的教徒"]我不愿意滥杀无辜，你们也曾是我的家人。
[Character(name="avg_npc_459_1#1$1",name2="avg_npc_453_1#1$1",focus=1)]
[name="男性镇民"]......
[Character(name="avg_npc_459_1#1$1",name2="avg_npc_453_1#1$1",focus=2)]
[name="诡异的教徒"]去让更多的人加入我们吧，我们有一条更宽阔的道路可以选择，远胜伊比利亚许诺的一切，更胜过这片大地。
[Character(name="avg_npc_459_1#1$1",name2="avg_npc_453_1#1$1",focus=1)]
[name="男性镇民"]那些......我们的兄弟们，它们躁动不安，是因为那些外来者？
[Character(name="avg_npc_459_1#1$1",name2="avg_npc_453_1#1$1",focus=2)]
[name="诡异的教徒"]很可能，但还不确定，我们都很弱小，兄弟姐妹们都很弱小，不能轻举妄动，审判庭会杀光我们。
[name="诡异的教徒"]我们得......谨慎......否则会在陆上流太多的血，她不喜欢流血......无论是我们，还是我们的兄弟姐妹，都没必要枉死。
[Dialog]
[MusicVolume(volume=0.1, fadetime=1)]
[PlaySound(key="$d_avg_chess")]
[Delay(time=0.6)]
[name="诡异的教徒"]......！谁？！
[Dialog]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
[CameraShake(duration=0.3, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.02, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[PlaySound(key="$swordtsing6",delay=0.5)]
[PlaySound(key="$swordtsing4")]
[Delay(time=0.6)]
[CameraShake(duration=0.5, xstrength=58, ystrength=56, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$bodyfalldown2", volume=0.5)]
[playsound(key="$d_avg_doorbreak", volume=0.5)]
[Delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty")]
[Background(image="bg_ibchurch",screenadapt="coverall")]
[MusicVolume(volume=0.4, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]我就知道。邪教徒，深海教徒......最近这些年我都没来过伊比利亚了，到处都是这种气息。
[name="Alty"]嗯......不过我开始期待再和她见面了。她还没来吗？
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]是的。凯尔希医生交代过，她极可能会遭到审判庭的监视，所以......
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]奇怪。她应该是看着伊比利亚崛起的，她怎么会没有办法找到他们的头儿？何必要用这么蹩脚的方式？
[Character(name="avg_npc_450_1#6$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]哈哈，伊比利亚的崛起都是好几百年前的事情了，就算是凯尔希医生......
[Character(name="avg_npc_450_1#6$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]看来她这么些年的经历还是让她学会了一些处世之道......唉，不是很懂，毕竟我很年轻嘛。
[Character(name="avg_npc_450_1#6$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]哈哈，Alty小姐说笑了......
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]......凯尔希医生如果真出了什么意外，你会帮她吧？
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",foc

... (全文20513字符)
```

### level_act17side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[playsound(key="$d_avg_snowstormflp", volume=0.7, loop=true, channel="b")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="27_g18_lighthouse_square",screenadapt="coverall")]
[playsound(key="$d_avg_sea", loop=true, channel="a")]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop",fadetime=3, volume=0.4)]
海是黑色的。
那是四五岁的时候，老蒂亚戈，格兰法洛的镇长，还有很多手持武器的大人，我们要出发去海边。
我仍旧记得那是一个怎样的天气。云雾汹涌，下午就比寻常的傍晚更冰冷。这种冰冷并非温度，而是色彩，一种失去热情的色彩。
后来我才知道，那是格兰法洛最后一次进行伊比利亚之眼的维护工作，不，准确来说，是尝试进行。
惩戒军很快就带来了一些消息，大人们满脸沮丧，我并不明白那意味着什么，只是看着海与天的交界处怔怔出神。
海是黑色的。
它与这片毫无希望的大地竟然如此般配。
[Dialog]
[StopSound(channel="a", fadetime=1)]
[StopSound(channel="b", fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[name="围观的群众"]蒂亚戈镇长来了！
[Dialog]
[Character(name="avg_npc_451_1#7$1",fadetime=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.8)]
[Delay(time=2)]
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_451_1#7$1",focus=2)]
[name="蒂亚戈"]所以老佩德里说的是真的，阿玛雅。
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_451_1#1$1",focus=1)]
[name="阿玛雅"]即使我想要否认，眼前的事情也不容许我开口了。
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_451_1#9$1",focus=2)]
[name="蒂亚戈"]但是，是什么人能杀死这个怪物？还随手丢在这里？
[Character(name="avg_npc_449_1#10$1",name2="avg_npc_451_1#9$1",focus=1)]
[name="阿玛雅"]我希望把它交给我处置。
[Character(name="avg_npc_449_1#10$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]这......
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_451_1#1$1",focus=1)]
[name="阿玛雅"]不处理好的话，我担心会有危险，而且，你看，这不是难得能够观察一只恐鱼的机会吗？
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]......可以。但我陪你一起处理它。
[name="蒂亚戈"]我们都不确定这个玩意到底是什么，我们更不确定它的血是不是会引来它的同伴。
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_451_1#1$1",focus=1)]
[name="阿玛雅"]我没有异议。
[Character(name="avg_npc_451_1#4$1")]
[name="蒂亚戈"]来吧，小伙子们，让开，让我把这具尸体抱起来——
[Dialog]
[CameraShake(duration=1, xstrength=20, vibrato=3, randomness=0, fadeout=false, block=true)]
[PlaySound(key="$d_avg_clothmovement",volume=0.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_empty",name2="avg_npc_451_1#1$1")]
[Character(name="avg_npc_457_1#1$1",name2="avg_npc_451_1#1$1",fadetime=0.5)]
[characteraction(name="right", type="move", xpos=-200, fadetime=0, block=true)]
[characteraction(name="left", type="zoom" , scale=0.8, fadetime=0, block=true)]
[characteraction(name="left", type="move", xpos=100, fadetime=0, block=true)]
[characteraction(name="left", type="move", ypos=-150, fadetime=0, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[Delay(time=2)]
[name="蒂亚戈"]......比看起来要轻，好了，阿玛雅，我们去哪儿？
[Character]
[Character(name="avg_npc_449_1#9$1")]
[name="阿玛雅"]跟我来吧。
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]你们，都别在这里待着，都回家去。
[Character(name="avg_npc_460_1#1$1")]
[name="慌张的镇民"]我们不需要去找审判庭吗......如果真的还有别的怪物，我们怎么办？
[Character(name="avg_npc_451_1#4$1")]
[name="蒂亚戈"]不需要找审判庭。
[Character(name="avg_npc_460_1#1$1")]
[name="慌张的镇民"]可是——
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_451_1#5$1")]
[name="蒂亚戈"]我说不需要！！
[Character(name="avg_npc_460_1#1$1")]
[name="慌张的镇民"]呃......
[Character(name="avg_npc_449_1#10$1",name2="avg_npc_451_1#5$1",focus=1)]
[name="阿玛雅"]蒂亚戈。
[Character(name="avg_npc_449_1#10$1",name2="avg_npc_451_1#2$1",focus=2)]
[name="蒂亚戈"]......
[Character(name="avg_npc_449_1#10$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]这座城镇还不需要惩戒军的介入，我们自有办法。
[Character(name="avg_npc_449_1#10$1",name2="avg_npc_451_1#4$1",focus=2)]
[name="蒂亚戈"]如果审判庭真的派人来，看见这玩意，那格兰法洛才是真的永无宁日，你们不明白吗？
[Character(name="avg_npc_460_1#1$1")]
[name="慌张的镇民"]可是......不......没什么。
[Character(name="avg_npc_449_1#10$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]走吧，阿玛雅。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[Character(fadetime=1)]
[Delay(time=2)]
[Character(name="avg_npc_460_1#1$1")]
[name="慌张的镇民"]我们真要听他的？
[Character(name="avg_npc_460_1#1$1",name2="avg_npc_459_1#1$1",focus=2)]
[name="茫然的镇民"]老蒂亚戈讨厌审判庭也不是一两天，可真要出什么事了，没有惩戒军，谁去战斗？我吗？
[name="茫然的镇民"]而且最近外来者很多。蒂亚戈就和看不见一样，如果那些外人里真的有......
[Character(name="avg_npc_460_1#1$1",name2="avg_npc_459_1#1$1",focus=1)]
[name="慌张的镇民"]果然还是应该派人去审判庭！等到惩戒军发现我们，我们怎么解释！我才不想被当成异教徒！
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[Character(fadetime=0.5)]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_450_1#2$1")]
[name="极境"]......阿玛雅小姐......那个作家......？
[Character(name="avg_npc_450_1#9$1")]
[name="极境"]先和日落即逝的各位打声招呼吧......总感觉不能放着不管。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Delay(time=1)]
[Background(image="bg_ibchurch",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="npc_2004_Alty")]
[name="Alty"]礼拜堂平时总这么冷清？你们的神和信仰呢？
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[Character(name="avg_npc_450_1#1$1",fadetime=1)]
[Delay(time=1)]
[name="极境"]并不是每一个伊比利亚人都信仰拉特兰教的。Alty小姐，这座小镇很危险，在凯尔希医生抵达之前，我需要保证你们的安全。
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]那不如来一场演出吧，音乐可以消除所有人的不安。
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]哈哈，我不是那个意思......
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]别急，让我猜猜发生了什么。
[Character(name="avg_npc_450_1#8$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]呃......
[Character(name="avg_npc_450_1#8$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]嗯......我看见了......一只海洋生物，对，你们称它们为恐鱼，第一个如此称呼的是伊比利亚人，或者是凯尔希，无所谓了。
[name="Alty"]一只恐鱼，它在干燥的天空下，它那充满批判性的鳞片无处安放，它很清楚，这里不是它的家，它的家关得住它流逝的生命。
[name="Alty"]......对了！我猜那是一只恐鱼，被悬挂在那座高高的雕塑上面，它在歌唱，最新潮的摇滚，对不对？
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=1)]
[name="极境"]......没挂在上面。也没歌唱。但八九不离十了。
[name="极境"]真让人意外，Alty小姐，这是您的法术吗？
[Character(name="avg_npc_450_1#1$1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]也许死亡本身也是一种歌

... (全文27179字符)
```

### level_act17side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ibchurch",screenadapt="coverall")]
[PlayMusic(intro="$plot_intro", key="$plot_loop", volume=0.2,fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",fadetime=1)]
[Delay(time=1)]
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]不去帮忙吗？
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",focus=1)]
[name="凯尔希"]你甚至都没打算从椅子上站起来。
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]用不着我嘛。
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",focus=1)]
[name="凯尔希"]我名义上还是伊比利亚的囚犯，没必要替一位大审判官担忧。
[name="凯尔希"]现在，接着聊我们之间的事情吧。
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]我们会留在海岸线上，留在这座小镇，嗯，稍作停留。
[name="Alty"]如果你和你的深海猎人们失败了，我们会带着伊比利亚人离开。退到一个恰到好处的位置，就像舞台上的调度。
[name="Alty"]不过前提是门外那个酷老头愿意听我们的话就是啦。
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",focus=1)]
[name="凯尔希"]......你们愿意帮助这片大地上的人类。
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]Frost很年轻，我和Dan差不多岁数，Aya可能年长一些。
[name="Alty"]以我们的维度来说，我们没什么可热爱的了，除了......嗯，音乐。
[name="Alty"]孱弱的躯体与脆弱的精神使得人类不得不在短暂的生命中寻找一些，嗯，突破口。
[name="Alty"]他们做到了，真厉害，不是吗？
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",focus=1)]
[name="凯尔希"]......是啊。
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]但海洋是不会喜欢重金属音乐的。
[name="Alty"]我们也没的选。站在生存的角度上，我也觉得现在的陆地更可爱一些。
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",focus=1)]
[name="凯尔希"]想让这个国度聆听你们的声音并不困难。揭示一些秘密，触碰他们的伤痕，向他们许诺，这样的灾难不会再次发生。
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]有这么简单吗？
[Character(name="char_003_kalts_1#1",name2="npc_2004_Alty",focus=1)]
[name="凯尔希"]如果许诺和哄骗划上等号，事情也许会简单些。
[dialog]
[MusicVolume(volume=0.4, fadetime=5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Delay(time=0.6)]
[Background(image="27_g16_lighthouse_street",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_457_1#1$1",name2="char_empty",fadetime=0.8)]
[playsound(key="$d_avg_fish_howl", volume=0.3)]
[Delay(time=1.2)]
[Character(name="char_empty",name2="avg_npc_457_1#1$1",fadetime=0.8)]
[playsound(key="$d_avg_fish_howl", volume=0.3)]
[Delay(time=1.2)]
[Character(fadetime=0.5)]
[Delay(time=1)]
[Character(name="char_empty",name2="avg_npc_460_1#1$1")]
[Characteraction(name="right", type="move", xpos=-200, fadetime=0, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Characteraction(name="right", type="move", xpos=-50, fadetime=0.2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.2, block=true)]
[Characteraction(name="right", type="move", xpos=100, fadetime=0.3, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
[name="慌乱的镇民"]这、这些怪物——这些怪物！
[name="慌乱的镇民"]我早就说过，该叫审判庭来！谁来帮帮忙——谁来——
[Dialog]
[Character(name="avg_npc_457_1#1$1",name2="avg_npc_460_1#1$1",fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Characteraction(name="right", type="jump", power=10, times=1,  xpos=150, fadetime=0.5, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_457_1#1$1",name2="avg_npc_460_1#1$1",focus=1)]
[name="恐鱼"]咕......咕哈......
[Character(name="avg_npc_457_1#1$1",name2="avg_npc_460_1#1$1",focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="慌乱的镇民"]咿——！
[Dialog]
[Character(name="avg_npc_457_1#1$1",name2="avg_npc_460_1#1$1")]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_bldwhoosh")]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0.5, r=1, g=0, b=0, fadetime=0.02, block=true)]
[Blocker(a=0, r=1, g=0, b=0, fadetime=0.07, block=false)]
[Blocker(a=0, r=1, g=0, b=0, fadetime=0.5, block=false)]
[Character(name="char_empty",name2="avg_npc_460_1#1$1",fadetime=0.3)]
[Delay(time=1)]
[Character]
[Character(name="avg_474_gladiia_1#5",fadetime=1)]
[Delay(time=1)]
[name="歌蕾蒂娅"]凯尔希挑选的见面地点，实在有些令人不敢恭维。
[name="歌蕾蒂娅"]这里发生了什么？
[Character(name="avg_474_gladiia_1#5",name2="avg_npc_460_1#1$1",focus=2)]
[name="慌乱的镇民"]谢、谢谢......你......你是阿戈尔人？你也是外来的阿戈尔人？
[Character(name="avg_474_gladiia_1#1",name2="avg_npc_460_1#1$1",focus=1)]
[name="歌蕾蒂娅"]......也？
[Character(name="avg_474_gladiia_1#4",name2="avg_npc_460_1#1$1",focus=1)]
[name="歌蕾蒂娅"]啊......你是在说日落即逝的各位。阿戈尔人......呵。
[Character(name="avg_474_gladiia_1#4",name2="avg_npc_460_1#1$1",focus=2)]
[name="慌乱的镇民"]......那个，你们，你们是来和它们战斗的？我看你一下就能把这些怪物干掉......
[Character(name="avg_474_gladiia_1#1",name2="avg_npc_460_1#1$1",focus=1)]
[name="歌蕾蒂娅"]你们对阿戈尔人的态度似乎与别处不太一样。
[Character(name="avg_474_gladiia_1#1",name2="avg_npc_460_1#1$1",focus=2)]
[name="慌乱的镇民"]其实直到二十多年前，这里的阿戈尔人都还挺多的......
[name="慌乱的镇民"]抱歉，你们是审判庭派来的吗？我们......我们应该向审判庭求援吗？
[Character(name="avg_474_gladiia_1#1",name2="avg_npc_460_1#1$1",focus=1)]
[name="歌蕾蒂娅"]与我无关。
[name="歌蕾蒂娅"]只是，如果不想受伤，就快点躲好，等着事情结束。
[Character(name="avg_474_gladiia_1#1",name2="avg_npc_460_1#1$1",focus=2)]
[name="慌乱的镇民"]呃，好......好......
[Dialog]
[playsound(key="$rungeneral")]
[Character(name="avg_474_gladiia_1#1",name2="char_empty",fadetime=0.5)]
[Delay(time=2)]
[Character(name="avg_474_gladiia_1#1",name2="char_263_skadi#3",fadetime=1)]
[Delay(time=1)]
[Character(name="avg_474_gladiia_1#1",name2="char_263_skadi#3",focus=2)]
[name="斯卡蒂"]这里，到处都是。
[name="斯卡蒂"]比盐风城好一些，但也很古怪。
[Character(name="avg_474_gladiia_1#4",name2="char_263_skadi#3",focus=1)]
[name="歌蕾蒂娅"]这里并没有沉入腐坏，看看这些人，他们甚至还在正常地生活。
[Character(name="avg_474_gladiia_1#4",name2="char_263_skadi#4",focus=2)]
[name="斯卡蒂"]......海浪没有触碰到这里。
[Character(name="avg_474_gladiia_1#1",name2="char_263_skadi#4",focus=1)]
[name="歌蕾蒂娅"]那么，那些深海的余孽就是躲藏了起来。
[name="歌蕾蒂娅"

... (全文23231字符)
```

### level_act17side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="27_g18_lighthouse_square",screenadapt="coverall")]
[Character(name="avg_npc_457_1#1$1",focus=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlayMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
[PlaySound(key="$d_gen_explo_n")]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$bodyfalldown1", volume=0.7)]
[Character(fadetime=1)]
[Delay(time=1)]
[Character(name="avg_npc_447_1#8$1")]
[name="圣徒卡门"]与报告如出一辙，我很好奇这究竟是一只怎样的生物。
[PlaySound(key="$Mon3tr_n")]
[Character(name="npc_10002")]
[name="Mon3tr"]（警示性的低鸣）
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]喔喔......别生气，小家伙，看来你能听懂人话。
[Character(name="avg_npc_447_1#1$1",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]这些恐鱼的身上有别的寄生物......但我从未在陆地上见过它们。
[Character(name="avg_npc_447_1#7$1",name2="avg_474_gladiia_1#1",focus=1)]
[name="圣徒卡门"]伊比利亚人称之为“溟痕”。
[name="圣徒卡门"]大静谧之后，伊比利亚的沿海居民偶尔会看见海洋发光的现象。最早的一次目击报告在十七年前。
[name="圣徒卡门"]我们的科研学者认为这是某种浮游生物集中爆发的结果。
[Character(name="avg_npc_447_1#10$1",name2="avg_474_gladiia_1#1",focus=1)]
[name="圣徒卡门"]那么，机会难得，我想知道阿戈尔人见过这些......令人不安的东西吗？
[Character(name="avg_npc_447_1#10$1",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]阿戈尔过去极少见到这样的现象，但是荧光的植物？科学院富丽堂皇的花园里从不缺这类观赏品。
[Character(name="avg_npc_447_1#1$1",name2="avg_474_gladiia_1#1",focus=1)]
[name="圣徒卡门"]原来阿戈尔人也懂得何为“观赏”。
[Character(name="avg_npc_447_1#1$1",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]“溟痕”——唯独这个命名十分准确，这种现象即是海洋对陆地的触碰。
[name="歌蕾蒂娅"]而这些蔓延的“溟痕”，本质上和我们在盐风城见到的恐鱼别无二致。
[Character(name="avg_npc_447_1#4$1",name2="avg_474_gladiia_1#1",focus=1)]
[name="圣徒卡门"]喔......你是说，这种自然现象本身亦是“恐鱼”的一种生物形式？
[Character(name="avg_npc_447_1#4$1",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]似乎伊比利亚的生物学家们还不够努力。
[Character(name="avg_npc_447_1#7$1",name2="avg_474_gladiia_1#1",focus=1)]
[name="圣徒卡门"]......情况比预想的复杂，但也不超过最坏的可能。
[name="圣徒卡门"]审判庭所目击、杀死、捕获的恐鱼种类几乎每个月都在变化。
[name="圣徒卡门"]而最快的一次发生在三号海岸线，只经过了四五个日落之后，我们面对的敌人就几乎面目全非。
[Character(name="char_003_kalts_1#1")]
[name="凯尔希"]海洋正在侵袭陆地，如我所说的那样，以它自己的方式。
[name="凯尔希"]现在，我要去救助罗德岛的干员。
[Character(name="char_003_kalts_1#1",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]我同你一起。
[Character(name="char_003_kalts_1#1",name2="avg_474_gladiia_1#1",focus=1)]
[name="凯尔希"]不必，你和猎人们尽快扫清威胁是最有效的办法。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[Character(name="char_empty",name2="avg_474_gladiia_1#1",fadetime=1)]
[Delay(time=2)]
[Character(name="avg_npc_447_1#1$1",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]......我以为伊比利亚会更谨慎地对待她。
[Character(name="avg_npc_447_1#1$1",name2="avg_474_gladiia_1#1",focus=1)]
[name="圣徒卡门"]凯尔希是一个必须谨慎对待的对象，但现在，我们有更明确的敌人。
[name="圣徒卡门"]你打算怎么做，阿戈尔的执政官？让我们继续为阿戈尔的傲慢争执？
[Character(name="avg_npc_447_1#1$1",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]十分钟。我将解决所有的麻烦，并和我的猎人们会合。
[name="歌蕾蒂娅"]之后我们再来商议如何前往那座灯塔。
[Character(name="avg_npc_447_1#1$1",name2="avg_474_gladiia_1#1",focus=1)]
[name="圣徒卡门"]那我便留在这里，这座礼拜堂已经失去律法许久，好在有人把它擦得锃亮。
[Character(name="avg_npc_447_1#9$1")]
[name="圣徒卡门"]它将是这场战争中唯一的光芒。伊比利亚的审判庭驻守于此，只我一人。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(fadetime=0)]
[Background(image="27_g16_lighthouse_street",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_451_1#4$1")]
[name="蒂亚戈"]喂，发生什么了？
[Character(name="avg_npc_451_1#4$1",name2="avg_npc_462_1#1$1",focus=2)]
[name="松懈的镇民"]蒂、蒂亚戈！你上哪儿去了？！
[name="松懈的镇民"]那些深海教徒突然出现了！还有怪物，好多怪物！
[name="松懈的镇民"]啊......而且......
[Character(name="avg_npc_451_1#4$1",name2="avg_npc_462_1#1$1",focus=1)]
[name="蒂亚戈"]而且什么？他们为什么在袭击城镇？
[name="蒂亚戈"]阿玛雅......阿玛雅呢？这些怪物伤害你们了吗？
[Character(name="avg_npc_451_1#4$1",name2="avg_npc_462_1#1$1",focus=2)]
[name="松懈的镇民"]他们......他们......
[name="松懈的镇民"]他们没有随便伤害别人，他们只是在和......一位......审判官战斗。
[Character(name="avg_npc_451_1#7$1",name2="avg_npc_462_1#1$1",focus=1)]
[name="蒂亚戈"]——
[Character(name="avg_npc_451_1#7$1",name2="avg_npc_462_1#1$1",focus=2)]
[name="松懈的镇民"]没有人去审判庭告密！蒂亚戈！真的！
[name="松懈的镇民"]我们在广场上发现那只怪物的尸体没多久，审判官就出现了，现在想来，说不定就是他们干的......啊。
[Dialog]
[Character]
[Character(name="avg_4042_lumen_1#8$1")]
[name="乔迪"]怎么了？叔叔......啊，女士，下午好。
[Character(name="avg_4042_lumen_1#1$1")]
[name="乔迪"]你们脸色怎么......
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]乔迪，跟我来。
[Character(name="avg_4042_lumen_1#8$1",name2="avg_npc_451_1#1$1",focus=1)]
[name="乔迪"]叔叔？
[Character(name="avg_4042_lumen_1#8$1",name2="avg_npc_451_1#7$1",focus=2)]
[name="蒂亚戈"]别出声。
[Character(name="avg_npc_462_1#1$1")]
[name="松懈的镇民"]蒂、蒂亚戈，真的不是我们干的......我们跑得再快，也不可能在这么短的时间里找到审判庭呀。
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]......我知道。现在我们要先保护好乔迪，必须把事情解释清楚。
[name="蒂亚戈"]可能是有人之前去的，一个星期前，一个月前，谁知道呢。邪教徒的流言蜚语已经传播这么久了。
[Character(name="avg_npc_462_1#1$1")]  
[name="松懈的镇民"]不、不是！起码不是我！也不是我的丈夫！
[Character(name="avg_4042_lumen_1#8$1",name2="avg_npc_451_1#1$1",focus=1)]
[name="乔迪"]难道是胡安？他们被审判庭发现了？
[Character(name="avg_npc_462_1#1$1")]
[name="松懈的镇民"]......你......
[name="松懈的镇民"]你知道......胡安是深海教会的人？你什么时候知道的？
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_451_1#4$1",focus=2)]
[name="蒂亚戈"]乔迪！走！
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_451_1#4$1",focus=1)]
[name="乔迪"]啊......好。
[Dialog]
[playsound(key="$rungeneral", loop=true, channel="bgs")]
[Character(fadetime=1)]
[StopSound(channel="bgs", fadetime=0.5)]
[Character(name="avg_npc_462_1#1$1")]
[name="松懈的镇民"]蒂亚戈！
[name="松懈的镇民"]唔......他走远了。
[Character(name="avg_npc_462_1#1$1",name2="avg_npc_459_1#1$1",focus=2)]
[name="警惕的镇民"]别理他，镇上情况怎么样了？
[Character(name="avg_npc_462_1#1$1",name2="avg_npc_459_1#1$1",focus=1)]
[name="松懈的镇民"]不、不知道，那个审判官和那些外来者在和怪物们打斗，我们帮不上忙。
[Character(name="avg_npc_462_1#1$1",name2="avg_npc_459_1#1$1",focus=2)]
[name="警惕的镇民"]嘁......等审判官解决了这些怪物，他就会来审判我们。
[Character(name="avg_npc_462_1#1$1",name2="avg_npc_459_1#1$1",focus=1)]
[name="松

... (全文27910字符)
```

### level_act17side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_room_2",screenadapt="coverall")]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4,fadetime=3)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_061#3",fadetime=1)]
[Delay(time=1)]
[name="玛莉娅"]呼哈——天都亮了吗？
[Character(name="avg_npc_061#1")]
[name="玛莉娅"]干员们的装备损耗，真是比想象中严重得多......不过，从天灾之下救出这么多人，大家还真厉害。
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]唔，我也要打起精神。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.7 )]
[Delay(time=1)]
[PlaySound(key="$dooropenquite")]
[Delay(time=1)]
[Character(name="char_220_grani#3",fadetime=1)]
[Delay(time=1)]
[name="格拉尼"]玛莉娅小姐，我来取工程部的订单啦。
[Dialog]
[Character(name="avg_npc_061#1")]
[PlaySound(key="$d_avg_clothmovement")]
[Delay(time=1)]
[name="玛莉娅"]啊，格拉尼！稍等，我看看放哪儿了......不好意思，几天没收拾，这儿有点乱......
[Character(name="avg_npc_061#1",name2="char_220_grani#2",focus=2)]
[name="格拉尼"]啊哈哈......这儿是不是比我上次来更接近一个卡西米尔式的工匠坊了......嗯？这是？
[Character(name="avg_npc_061#1",name2="char_220_grani#3",focus=2)]
[name="格拉尼"]......小说？
[Character(name="avg_npc_061#1",name2="char_220_grani#3",focus=1)]
[name="玛莉娅"]《最后的骑士》！怎么在这儿？难道是昨晚翻箱倒柜的时候压在图纸下面了......我说怎么找不到。
[Character(name="avg_npc_061#1",name2="char_220_grani#2",focus=2)]
[name="格拉尼"]《最后的骑士》？
[Character(name="avg_npc_061#1",name2="char_220_grani#2",focus=1)]
[name="玛莉娅"]姐姐在我小时候送给我的，是我以前最喜欢的小说。
[Character(name="avg_npc_061#1",name2="char_220_grani#3",focus=2)]
[name="格拉尼"]卡西米尔的骑士小说啊......
[Character(name="avg_npc_061#1",name2="char_220_grani#2",focus=2)]
[name="格拉尼"]可以借我看看吗？
[Character(name="avg_npc_061#1",name2="char_220_grani#2",focus=1)]
[name="玛莉娅"]没问题！
[name="玛莉娅"]啊，施术单元的理论书原来被丢在这里......不好意思格拉尼小姐，估计还要费点功夫，我一会自己送过去吧。
[Character(name="avg_npc_061#1",name2="char_220_grani#2",focus=2)]
[name="格拉尼"]没关系，我等你。这次回罗德岛可以待不少时间呢。
[name="格拉尼"]我就在这里看小说打发时间啦。
[Character(name="avg_npc_061#1",name2="char_220_grani#2",focus=1)]
[name="玛莉娅"]实在抱歉......
[Dialog]
[Character]
[Character(name="char_220_grani#2",fadetime=0.5)]
[PlaySound(key="$d_avg_paper2")]
[Delay(time=1)]
[Character(name="char_220_grani#3",fadetime=0.5)]
[name="格拉尼"]......
[Dialog]
[Character]
《最后的骑士》。
很浮夸的名字，也很常见。卡西米尔的小说里也许有几百个最后的骑士，几百个最快的骑士，几百个最强的骑士。
但既然是耀骑士送给自己妹妹的小说，那总该有些特殊之处吧？
格拉尼如是想着，翻开书页，发现其中夹着一枚书签。
上面用歪歪扭扭的卡西米尔文字，誊抄着一句兴许是来自书中的台词。
[StopMusic(fadetime=2)]
[name="格拉尼"]“如果觉得浪涛吵闹，就去令大海平静。”......？
[Dialog]
[PlaySound(key="$d_avg_sea")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
传说最后的骑士回到伊比利亚。他眼中的敌人全非活物，冲锋的目标只有群峦、城市和波涛。
传说最后的骑士定居海岸，餐风露宿，日复一日，直到他忘记如何摘下头盔。
传说最后的骑士与巨浪搏斗直至消失。他的家人发现了他留在岸边的遗物，带回骑士之国，埋进深山。
[dialog]
[Background(image="27_g19_lighthouse_front",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
传说他或她的故事被一位诗人知晓，加工，传唱，赋予其表意与符号。以这种形式，骑士回到了骑士之国，饱受争议......
但是......
[Dialog]
[Character(name="avg_npc_448_1#1$1",fadetime=1)]
[Delay(time=1)]
......也有人相信，相信疯癫的骑士战胜了海、时间与死亡。他奔赴追逐，直到万物终结。
[Dialog]
[playMusic(intro="$industv2_intro", key="$industv2_loop", volume=0.4,fadetime=3)]
[Delay(time=1)]
[name="？？？"]......
[name="？？？"]............
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]你是......什么东西？
[Character(name="avg_npc_448_1#1$1")]
[name="？？？"]......
骑士没有答话。他死死盯着歌蕾蒂娅。
歌蕾蒂娅很快意识到，他并非盯着自己。
他只是......盯着自己怀里的，那把钥匙。
[CameraShake(duration=0.3, fadeout=true, xstrength=25, ystrength=25, vibrato=30, randomness=90, block=false)]
[name="？？？"]嘎......咳咳......嘶......
骑士张嘴，骑士要发出声音。干瘪的声响，像是肌肉撕裂。
骑士开始向前迈步。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Character(name="char_003_kalts_1#1",name2="avg_npc_447_1#1$1")]
[Background(image="27_g16_lighthouse_street",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_003_kalts_1#1",name2="avg_npc_447_1#1$1",focus=2)]
[name="圣徒卡门"]你从哪里拿到那把钥匙的？
[Character(name="char_003_kalts_1#1",name2="avg_npc_447_1#1$1",focus=1)]
[name="凯尔希"]......
[Character(name="char_003_kalts_1#1",name2="avg_npc_447_1#8$1",focus=2)]
[name="圣徒卡门"]喔，我无意......打探所谓罗德岛的内部事务。
[name="圣徒卡门"]可那是布雷奥甘的遗产，经由那四匹巨兽的手，再交给了那个深海猎人。
[Character(name="char_003_kalts_1#1",name2="avg_npc_447_1#8$1",focus=1)]
[name="凯尔希"]因为一些机缘巧合，方才深海猎人中的一位，在卡西米尔发现了它。
[Character(name="char_003_kalts_1#1",name2="avg_npc_447_1#4$1",focus=2)]
[name="圣徒卡门"]......卡西米尔？真是个遥远的国度，我还记得年轻时跟随导师接待骑士之国的来使，私下听几位手持银枪的征战骑士描述他们的理想......
[name="圣徒卡门"]据说那个国家变了许多。
[Character(name="char_003_kalts_1#1",name2="avg_npc_447_1#4$1",focus=1)]
[name="凯尔希"]无论这种变化的好坏优劣，这种发生在当下时代的每一个政治实体上的变化，却与伊比利亚无缘。
[Character(name="char_003_kalts_1#1",name2="avg_npc_447_1#2$1",focus=2)]
[name="圣徒卡门"]我们就像落入陷阱的困兽，反抗挣扎，会痛，会流血。放弃，则死路一条。
[name="圣徒卡门"]在我们揪出那些尚是人类的背叛者之前，凯尔希，我有了一个新的问题。
[name="圣徒卡门"]你不会意识不到，那个少年绝非布雷奥甘的后裔。审判庭不可能漏过这样重要的线索。
[Character(name="char_003_kalts_1#1",name2="avg_npc_447_1#5$1",focus=2)]
[name="圣徒卡门"]你为什么还要让他去白白送死？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="27_g19_lighthouse_front",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_fish_howl",volume=0.3)]
[Character(name="avg_npc_457_1#1$1")]
[name="恐鱼"]（呼唤同伴的窸窣声）
[Dialog]
[Character]
[Character(name="avg_npc_457_1#1$1",name2="char_empty",fadetime=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_457_1#1$1",name2="avg_npc_457_1#1$1",fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]长官！
[Character(name="avg_npc_183#1")]
[name="大审判官达里奥"]......数量在增多。但是抵达灯塔之前，它们都没有现身。
[Character(name="avg_4042_lumen_1#13$1")]
[name="乔迪"]长、长官！我找到打开大门的办法了！
[name="乔迪"]但是伊比利亚之眼核心建筑是一座很高很高的塔！升降设施没有启动，我们只能——徒步！
[PlaySound(key="$d_avg_fish_howl",volume=0.1)]
[Character(name="avg_npc_457_1#1$1")]
[name="恐鱼"]（蠕动的窸窣声）
[Dialog]
[CameraShake(duration=0.3, ystrength=40, vibrato=30, ra

... (全文26524字符)
```

### level_act17side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibchurch",screenadapt="coverall")]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4,fadetime=3)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="npc_2001_Aya_1")]
[name="Aya"]你等不及了？
[Character(name="npc_2003_Frost_1")]
[name="Frost"]......
[Character(name="npc_2004_Alty")]
[name="Alty"]如果凯尔希说的那些是真的，那我们大概都等不及了。
[name="Alty"]就算我们行走在陆地上，我们还是存在于海里。那些腐败的后裔......它们在改变的是“环境”。
[name="Alty"]我们迟早无法幸免。现在是在坐以待毙。
[Character(name="npc_2001_Aya_1")]
[name="Aya"]坐以待毙的不止我们，而且大家的原因还都不一样。
[name="Aya"]想开点，说不定只是这片大地不适合我们生存了。
[Character(name="npc_2003_Frost_1")]
[name="Frost"]（表示赞同的独奏）
[name="Frost"]音乐......还不够。
[name="Frost"]我想做点什么。
[Character(name="npc_2002_Dan_1")]
[name="Dan"]为了音乐，做点什么吧！
[Character(name="npc_2003_Frost_1")]
[name="Frost"]（表示赞同的独奏）
[Character(name="npc_2004_Alty")]
[name="Alty"]怎么办？
[Character(name="npc_2001_Aya_1")]
[name="Aya"]唔......在这等着也是等着......
[name="Aya"]就当演唱会前的体能训练吧，别游太远，Frost。
[Character(name="npc_2003_Frost_1")]
[name="Frost"]......体能训练，那你们？
[Character(name="npc_2001_Aya_1")]
[name="Aya"]我就算了。
[Character(name="npc_2004_Alty")]
[name="Alty"]我懒。
[Character(name="npc_2002_Dan_1")]
[name="Dan"]我感觉就快要把灵感完成了，就差一点，一丁点。
[Character(name="npc_2003_Frost_1")]
[name="Frost"]......好吧。（激昂的独奏）
[name="Frost"]我出发了。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="27_g16_lighthouse_street",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$rungeneral", loop=true, channel="bgs")]
[Character(name="avg_npc_454_1#1$1",name2="char_empty",fadetime=1)]
[characteraction(name="left", type="move", xpos=600, fadetime=0, block=false)]
[characteraction(name="left", type="move", xpos=-600, fadetime=2, block=false)]
[Delay(time=2)]
[StopSound(channel="bgs", fadetime=1)]
[name="喘息的教徒"]哈啊......哈啊......
[name="喘息的教徒"]不，那个审判官和那个女人做了什么，他们怎么能这么轻易地抹除海的恩赐！
[name="喘息的教徒"]阿戈尔......一定是阿戈尔人，那些阿戈尔人留下的东西，那些古怪的机械！必须要毁掉那些机械！
[Dialog]
[Character(name="avg_npc_454_1#1$1",name2="avg_npc_457_1#3$1",fadetime=1)]
[Character(name="avg_npc_454_1#1$1",name2="avg_npc_457_1#3$1")]
[characteraction(name="right", type="move", ypos=-200,xpos=-50, fadetime=0, block=false)]
[characteraction(name="right", type="move", ypos=100,xpos=-50, fadetime=0.8, block=false)]
[Delay(time=1)]
[PlaySound(key="$d_avg_fish_howl",volume=0.3)]
[characteraction(name="right", type="move", ypos=100,xpos=100, fadetime=0.8, block=false)]
[Delay(time=1)]
[Character(name="avg_npc_454_1#1$1",name2="avg_npc_457_1#3$1",focus=2)]
[name="恐鱼"]（攀附上小腿的窸窣声）
[Character(name="avg_npc_454_1#1$1",name2="avg_npc_457_1#3$1",focus=1)]
[name="喘息的教徒"]是的......兄弟，惩戒军已经包围了这里，突围失败了......我们无路可退。
[name="喘息的教徒"]但是——我们尊敬的先知已经回到了海洋。
[name="喘息的教徒"]我们所要做的，只剩下，为她铺平道路。
[Dialog]
[PlaySound(key="$d_avg_fish_howl",volume=0.5,delay=0.3)]
[Character(name="avg_npc_454_1#1$1",name2="avg_npc_457_1#1$1",focus=2)]
[Blocker(a=0,fadetime=0.2, block=true)]
[Characteraction(name="right", type="jump", xpos=25,power=0,times=1, fadetime=0.2, block=true)]
[Blocker(a=0,fadetime=0.05, block=true)]
[Characteraction(name="right", type="jump", xpos=-25, power=0,times=1, fadetime=0.2, block=true)]
[Blocker(a=0,fadetime=0.05, block=true)]
[Characteraction(name="right", type="jump", xpos=25,power=0,times=1, fadetime=0.2, block=true)]
[Blocker(a=0,fadetime=0.05, block=true)]
[Characteraction(name="right", type="jump", xpos=-25, power=0,times=1, fadetime=0.2, block=true)]
[Blocker(a=0,fadetime=0.05, block=true)]
[Characteraction(name="right", type="jump", xpos=25, power=0,times=1, fadetime=0.2, block=true)]
[Blocker(a=0,fadetime=0.05, block=true)]
[Characteraction(name="right", type="jump", xpos=-30, power=0,times=1, fadetime=0.2, block=true)]
[Blocker(a=0,fadetime=0.05, block=true)]
[name="恐鱼"]（急躁的窸窣声）
[Character(name="avg_npc_454_1#1$1",name2="avg_npc_457_1#1$1",focus=1)]
[name="喘息的教徒"]如果他们想要阻拦潮汐，就让我们去毁灭他们，我的生命也只是漫长道路的一小部分。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="27_g17_lighthouse_alley",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_empty",name2="avg_npc_460_1#1$1")]
[Characteraction(name="right", type="move", xpos=-200,fadetime=0,block=true)]
[Delay(time=1)]
[name="惊疑不定的镇民"]咿！
[Dialog]
[Characteraction(name="right", type="jump", xpos=200, power=20, times=1, fadetime=0.4,block=false)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[Character(name="avg_npc_451_1#1$1",name2="avg_npc_460_1#1$1",fadetime=1)]
[Delay(time=2)]
[Character(name="avg_npc_451_1#1$1",name2="avg_npc_460_1#1$1",focus=1)]
[name="蒂亚戈"]别慌，是我。你怎么没去避难？
[Character(name="avg_npc_451_1#1$1",name2="avg_npc_460_1#1$1",focus=2)]
[name="惊疑不定的镇民"]蒂、蒂亚戈镇长......我喝醉了，睡得像头钳兽，啥也没听见......
[name="惊疑不定的镇民"]结果我醒过来的时候，外面乱糟糟的，地上全是这种恶心的东西......
[name="惊疑不定的镇民"]这里发生什么了？审判庭来人了吗？我们会怎么样？
[Character(name="avg_npc_451_1#2$1",name2="avg_npc_460_1#1$1",focus=1)]
[name="蒂亚戈"]......大海没有犯下任何罪过，但审判庭不同，他们捏着所谓的律法，他们判我们有罪。
[Character(name="avg_npc_451_1#1$1",name2="avg_npc_460_1#1$1",focus=1)]
[name="蒂亚戈"]只要等一段时间，恐鱼会回到海里的......但是我不能让审判官就这么宣判格兰法洛死刑。
[Character(name="avg_npc_451_1#1$1",name2="avg_npc_460_1#1$1",focus=2)]
[name="惊疑不定的镇民"]你在说什么——你疯了？
[Character(name="avg_npc_451_1#7$1",name2="avg_npc_460_1#1$1",focus=1)]
[name="蒂亚戈"]我没疯！我只是想知道！在审判庭摧毁这座小镇，然后把我们全部抓走审讯之前，我们还应该做什么！
[name="蒂亚戈"]审判官早就在这里了，我躲在小巷子里看见过那个人。我从来没见过那么老的审判官，我有种不好的预感......
[Character(name="avg_npc_451_1#7$1",name2="avg_npc_460_1#1$1",focus=2)]
[name="惊疑不定的镇民"]那你打算怎么办，蒂亚戈？难道你要冲到他面前讲道理？
[Character(name="avg_npc_451_1#1$1",name2="avg_npc_460_1#1$1",focus=1)]
[name="蒂亚戈"]又到了选边站的时候，对吧？
[Character(name="avg_npc_451_1#2$1",name2="avg_npc_460_1#1$1",focus=1)]
[name="蒂亚戈"]阿戈尔

... (全文30507字符)
```

### level_act17side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4,fadetime=3)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_445_1#1$1",blackstart=0.2,blackend=0.5,blackstart2=0.27,blackend2=0.5,fadetime=1)]
[Delay(time=2)]
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_445_1#1$1",focus=1)]
[name="阿玛雅"]我们就快抵达终点。
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]  ......
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_445_1#1$1",focus=1)]
[name="阿玛雅"]怎么，没有我，你根本不可能顺利抵达斯图提斐拉号。海的子嗣会撕咬你，粉碎你，或是缠住你的手脚，把你带去巢穴。
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]  你与昆图斯不同。
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_445_1#1$1",focus=1)]
[name="阿玛雅"]你是指，什么？皮囊吗？这幅皮囊？
[name="阿玛雅"]那不重要。
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]  你到底打算做什么？
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_445_1#1$1",focus=1)]
[name="阿玛雅"]你又打算做什么？猎人？你的同族都对敌人深恶痛绝，也因此怀疑自己的血。而你却......佯装镇定。
[name="阿玛雅"]你要从我这里得到什么？
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]  ......
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_445_1#1$1",focus=1)]
[name="阿玛雅"]聪明的沉默，看来阿戈尔人也并非全都不善交际。
[name="阿玛雅"]还是说，你其实是个不太受欢迎的臭脾气？
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]  ......
[Character(name="avg_npc_449_1#1$1",name2="avg_npc_445_1#1$1",focus=1)]
[name="阿玛雅"]......我可以回答你。昆图斯不会回答你，其他人也不会，但海嗣会。我们就应当像使者那样理解事物，而不局限在人类的想法里。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Character(fadetime=0)]
[Background(image="27_g21_goldenboat_deck",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_449_1#11$1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]  别故弄玄虚。
[Character(name="avg_npc_449_1#7$1",name2="avg_npc_445_1#1$1",focus=1)]
[name="阿玛雅"]嗯......
[name="阿玛雅"]在来这里前，我还在翻译一本乌萨斯的著作。关于种族，国家与历史。把它翻译成伊比利亚文，维多利亚文。
[name="阿玛雅"]看吧，猎人先生。
[Character]
乌尔比安顺着女人的手，下意识地望向海洋。
漆黑的海。乌云密布，压抑，但隐约能看见星空。
[Character(name="avg_npc_449_1#10$1",name2="avg_npc_445_1#1$1",focus=1)]
[name="阿玛雅"]即使是阿戈尔人也不常在海面上眺望海洋。种族、国家，大地被划分成一块一块，斗争永无止境。
[name="阿玛雅"]可在这一望无际的海平面上，你能看见象征着那些隔阂的界线吗？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Background(image="27_g20_lighthouse_core",screenadapt="coverall")] 
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_457_1#1$1",fadetime=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[playsound(key="$bodyfalldown1",volume=0.5)]
[Character(fadetime=0.5)]
[delay(time=1)]
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]啧！这些怪物——！
[name="审判官艾丽妮"]乔迪！你还好吗？！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_457_1#1$1")]
[characteraction(name="right", type="move", xpos=300, ypos=100,fadetime=0,block=false)]
[delay(time=1)]
[characteraction(name="right", type="move", ypos=-50 ,fadetime=0.8,block=false)]
[delay(time=1)]
[characteraction(name="right", type="move", xpos=-80,ypos=-50,fadetime=0.8,block=false)]
[delay(time=0.8)]
[playsound(key="$d_avg_fish_howl",volume=0.4)]
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_457_1#1$1",focus=2)]
[name="恐鱼"]（摩擦墙壁的窸窣声）
[Character(name="avg_4042_lumen_1#9$1",name2="avg_npc_457_1#1$1",focus=1)]
[characteraction(name="left", type="move", xpos=-30,fadetime=0.8,block=true)]
[name="乔迪"]别、别过来——！
[Dialog]
[Character(name="avg_4042_lumen_1#9$1",name2="avg_npc_457_1#1$1")]
[characteraction(name="right", type="jump", xpos=-280,times=1,power=20,fadetime=0.8,block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_183#1",name2="avg_npc_457_1#1$1")]
[characteraction(name="left", type="move", xpos=80,fadetime=0.3,block=true)]
[playsound(key="$p_imp_sword_n")]
[delay(time=0.8)]
[Character(name="avg_npc_183#1",name2="avg_npc_457_1#1$1")]
[characteraction(name="right", type="move", xpos=280,fadetime=0.8,block=false)]
[playsound(key="$punch_n1",delay=0.2)]
[Character(name="avg_npc_183#1",name2="char_empty",fadetime=0.5)]
[delay(time=1)]
[name="大审判官达里奥"]看来设备的运转让这些低劣生物意识到，这里并非理想巢穴。
[character]
[Character(name="avg_4042_lumen_1#13$1",name2="avg_npc_183#1",focus=1)]
[name="乔迪"]长官！
[Character(name="avg_4042_lumen_1#13$1",name2="avg_npc_183#1",focus=2)]
[name="大审判官达里奥"]向上走，阿戈尔人，你手里的是工具而非剑与火。
[name="大审判官达里奥"]与艾丽妮继续执行计划，找到审判庭与猎人们想要的。
[Character(name="avg_4042_lumen_1#13$1",name2="avg_npc_183#1",focus=1)]
[name="乔迪"]我、我知道了！您小心！
[Dialog]
[Character(name="avg_4042_lumen_1#13$1",name2="avg_npc_183#1")]
[playsound(key="$rungeneral")]
[Character(name="char_empty",name2="avg_npc_183#1",fadetime=1)]
[delay(time=1)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Background(image="27_g19_lighthouse_front",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_263_skadi#3")]
[name="斯卡蒂"]你觉得我们真能找到那艘船？
[Character(name="char_263_skadi#3",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]伊比利亚是唯一的切入点。
[Character(name="char_263_skadi#3",name2="avg_474_gladiia_1#1",focus=1)] 
[name="斯卡蒂"]我不明白......如果船就是像罗德岛那样的地方，那为什么六十年间，它没有试过回到伊比利亚？
[dialo

... (全文28198字符)
```

### level_act17side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Character(fadetime=0)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1, delay=0.5)]
[Background(screenadapt="coverall", image="bg_bridge", width=1, height=1, fadetime=0)]
[CameraEffect(effect="Grayscale", amount=0.7, keep=true)]
[Blocker(a=0, fadetime=2, block=true)]
[Delay(time=0.8)]
[Character(name="char_003_kalts_1",fadetime=1)]
[delay(time=2)]
[name="凯尔希"]布雷奥甘，是那把钥匙的主人。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]他在伊比利亚的黄金时代成为了王公贵族的座上宾，人们曾一度以为他象征着阿戈尔岛民与伊比利亚人和谐共处的开端。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]没人知道他在灾难前做了什么，又来不及做什么，但是他确确实实留下了足够多的遗产......以及对你们来说，足够多的方向。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]但他已经属于过去，毫无疑问，现在做出选择的是你们。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]那把钥匙......布雷奥甘的钥匙遗落在卡西米尔的缘由，是一个我们没必要知晓的答案。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]但找到它的，是猎人斯卡蒂。这不是什么巧合，这是必然。你们对海洋天生敏感。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]......是的，我把钥匙交给了那个乐队。你会知道她们是什么样的存在。也许阿戈尔人需要争取她们的帮助。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]她们也在寻找答案。她们大多年轻，也对海洋的变化感到不适，毕竟她们无法真正离开自己诞生的地方。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]是啊......希望我们能够成功。人类有太多问题需要面对，层层累叠的灾难可以轻松撕毁现在的文明。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]歌蕾蒂娅，你想单独行动，我不会劝阻你。斯卡蒂与你相似，也许猎人都是相似的。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]但千万别觉得，自己能解决陆地上的所有问题。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]嗯？你问吧，对你，我有问必答。
[Character(name="char_003_kalts_1#2")]
[name="凯尔希"]Ishar-mla......？
[Character(name="char_003_kalts_1#2")]
[name="凯尔希"]你在哪里听到的？
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(fadetime=0)]
[delay(time=1)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Background(image="27_g24_cloudy_sea",screenadapt="coverall")]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.8, crossfade=1, delay=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$d_avg_sea", volume=0.6, loop=true, channel="sea")]
[Character(name="avg_4009_irene_1#1$1",fadetime=1)]
[delay(time=1)]
[name="审判官艾丽妮"]我们就快到了。
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]但是，海洋......太宽广了，模糊的坐标会带来极大的误差......
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]......而且海洋比我想的要平静。
[Character(name="char_263_skadi#2")]
[name="斯卡蒂"]过于平静了，离开那座灯塔后，我们遭遇的袭击反而变得更少了。
[Character(name="char_263_skadi#2")]
[name="斯卡蒂"]甚至......没有风浪。
[Character(name="avg_4009_irene_1#1$1")]
[name="审判官艾丽妮"]这意味着什么？
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]这意味着——
[dialog]
[Character(fadetime=0)]
[Character(name="avg_1023_ghost2_1#2$1",name2="avg_4009_irene_1#1$1",focus=1)]
[name="幽灵鲨"]可怜的小鸟，你在紧张吗？
[Character(name="avg_4009_irene_1#2$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="审判官艾丽妮"]呀！你、你什么时候——别站在我背后！
[Character(name="avg_4009_irene_1#1$1")]
[name="审判官艾丽妮"]我没有紧张，我只是......很少很少有人能深入海洋到这个地步，我......我不确定......
[Character(name="avg_1023_ghost2_1#2$1")]
[name="幽灵鲨"]不，你在凝视身后，而非眼前。你在害怕失去，而不是面对未知。
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]......
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]你的长官为你创造了前往斯图提斐拉的契机，接触阿戈尔的契机，不是为了让你这么优柔寡断。
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]......我知道。
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]你得在战斗来临之前......唔。鲨鱼，你闻到了吗？
[Character(name="avg_1023_ghost2_1#2$1")]
[name="幽灵鲨"]是啊，让这艘舒适的小船微微向右，我们就能看见那艘更大的船。
[Character(name="avg_1023_ghost2_1#2$1")]
[name="幽灵鲨"]那里已经是一座巢穴，我们真的要去那里吗？
[Character(name="char_263_skadi#4")]
[name="斯卡蒂"]幽灵鲨，你要不要休息一下？
[Character(name="avg_1023_ghost2_1#4$1")]
[name="幽灵鲨"]我？我有什么不对的地方吗？为什么这么问？
[Character(name="char_263_skadi#2")]
[name="斯卡蒂"]你的手在抖。
[Character(name="avg_1023_ghost2_1#4$1")]
[name="幽灵鲨"]嗯？
[dialog]
幽灵鲨看向自己的手。没有握着武器的手，正在海风中微微颤抖。
她的意识逐渐明晰，又极快地坠入深海，触碰不得。
[Character(name="avg_1023_ghost2_1#4$1")]
[name="幽灵鲨"]我......啊，我这是在激动吗？还是......感动？
[name="幽灵鲨"]为什么？
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]......
[dialog]
[Character(fadetime=0)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[delay(time=1)]
歌蕾蒂娅默默握住了幽灵鲨的手，斯卡蒂随之效仿，三名深海猎人沉默了片刻。
[Character(name="avg_474_gladiia_1#4")]
[name="歌蕾蒂娅"]欢迎回家。猎人们。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Background]
[Image(image="27_i28", fadetime=2,xScale=0.9, yScale=0.9,x=-20, y=20)]
[ImageTween(xScaleTo=0.8, yScaleTo=0.8, duration=40,xTo=0, yTo=0,block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
歌蕾蒂娅默默地走上船头。
海风推开夜晚，传递着熟悉的气味。
一艘安静的大船，在海面上酣眠沉睡。它是海风的臣民，时代的贵客。
而那曾是一个遍地理想的时代，人们的探索精神在它身上体现得淋漓尽致，傲慢亦然。
斯卡蒂与歌蕾蒂娅无声地眺望着那艘船。
一瞬间她们想起了很多，但最后无疑都回到了自己的过去，童年，故土，与当下船舶摇晃的频率。
唯有幽灵鲨微微抱紧了手里的武器，海风微拂。
海风会把猎人们带回家。
[Dialog]
[stopmusic(fadetime=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[dialog]
[Character(fadetime=0)]
[Image]
[delay(time=2)]
[stopSound(channel="sea",fadetime=2)]
[Background(image="27_g16_lighthouse_street",screenadapt="coverall")]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.8, crossfade=1, delay=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_fish_howl")]
[Character(name="avg_npc_457_1#1$1",name2="avg_npc_457_1#1$1",fadetime=1)]
[delay(time=2)]
[name="恐鱼"]（沿石面爬行的窸窣声）
[Character(name="char_003_kalts_1")]
[name="凯尔希"]Mon3tr，烧毁它们。
[Character(fadetime=0)]
[dialog]
[Character(name="npc_10002",fadetime=0.5)]
[delay(time=0.51)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[PlaySound(key="$p_skill_Mon3trburst")]
[PlaySound(key="$d_sp_ballista", volume=0.9)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$Mon3tr_n")]
[name="Mon3tr"]（尖啸）
[Delay(time=1)]
[

... (全文30623字符)
```

### level_act17side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop",fadetime=3, volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
我看见。
我看见阿方索每天都要去大厅。大厅现在被他命名为伊比利亚。
他把卧室里的镜子搬到了大厅去，他日复一日审视着自己。
自大厨和小杰米被处决后，就只剩下我和他。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="27_g22_goldenboat_hall",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="大副"]......
[Character(name="avg_npc_446_1#1$1")]
[name="船长阿方索"]你来了。
[Character(name="avg_npc_446_1#2$1")]
[name="船长阿方索"]我睡了多久？我睡的时间好少，我被迫清醒。
[character(fadetime=0)]
[name="大副"]啊......不久......只是......
[Character(name="avg_npc_446_1#8$1")]
[name="船长阿方索"]别勉强说话。我知道，你说话会痛。
[Character(name="avg_npc_446_1#1$1")]
[name="船长阿方索"]低级怪物的血还剩不少，用来写字吧。
[dialog]
[character(fadetime=0)]
我点了点头。角落里有桶，里面装满了猎物的血。
[Character(name="avg_npc_446_1#2$1")]
[name="船长阿方索"]时间太长了。我只睡了很短的时间，但我的梦似乎比这几十年时间还要漫长......
[Character(name="avg_npc_446_1#2$1")]
[name="船长阿方索"]我们应该放弃吗？小杰米和那个老厨子已经离开很久了，我们该随他们而去吗？
[dialog]
[character(fadetime=0)]
我们应该放弃。
我的意识越发模糊，就像梦醒前的纠缠。
变化的不仅是肉体，是身为生物的所有部分。
我们应该放弃。应该在被吞噬前结束自己。无止境的海面。海风。浪涛。呢喃。
[Character(name="avg_npc_446_1#1$1")]
[name="船长阿方索"]......大副，这是我们的船，是我们的理想。
[Character(name="avg_npc_446_1#1$1")]
[name="船长阿方索"]我们迟早会无力行走，但它不会，“愚人号”不会。
[Character(name="avg_npc_446_1#1$1")]
[name="船长阿方索"]那个雪茄成瘾的工程师说的没错，即使我们死光，这艘船也不会沉没。
[Character(name="avg_npc_446_1#1$1")]
[name="船长阿方索"]今天......只是漫长时间中的二十四小时。
[character(fadetime=0)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[name="大副"]......（用恐鱼的血拼写单词的声音）
[Character(name="avg_npc_446_1#8$1")]
[name="船长阿方索"]别......放弃？
[Character(name="avg_npc_446_1#9$1")]
[name="船长阿方索"]哈，你已经成了这副样子，我都看不见你碧蓝色的瞳孔，解脱对你来说不是更好吗？
[character(fadetime=0)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[name="大副"]（书写）我是你的大副。
[Character(name="avg_npc_446_1#1$1")]
[name="船长阿方索"]......
[character(fadetime=0)]
[name="大副"]......为了......你。
[Character(name="avg_npc_446_1#6$1")]
[name="船长阿方索"]......别说话了。
[Character(name="avg_npc_446_1#10$1")]
[name="船长阿方索"]谢谢，加西亚。无论你变成什么，我们的感情都不会变。
[character(fadetime=0)]
[name="大副"]（点头）
[dialog]
[character(fadetime=0)]
但我知道，他在看镜子，是因为强壮如他，也终于败给了那些怪物。
我们吞食血肉，起初，我们生火，后来，我们被迫生啖其肉。
连最强大的审判官都曾对阿方索的力量赞叹不已，他曾被多少年轻的水手憧憬。他无所不能。
可他撑了够久了，他也迟早会变成那些怪物。
他在担忧。他在恼怒。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=3)]
他连自己那丁点怪物的部分都容忍不了，他又怎么能容得下我呢？
[dialog]
[delay(time=1)]
[character(fadetime=0)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Background(image="27_g23_goldenboat_pass",screenadapt="coverall")]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.8, crossfade=1, delay=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[Character(name="avg_474_gladiia_1#2")]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[dialog]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[character(fadetime=0)]
[character(name="char_empty")]
[characteraction(name="middle", type="move",xpos=-200,fadetime=0, block=true)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$swordtsing1", volume=1)]
[PlaySound(key="$d_avg_clothmovement", volume=0.9)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_456_1#1$1",fadetime=0.5)]
[characteraction(name="middle", type="move",xpos=300, fadetime=0.7, block=true)]
[delay(time=1)]
[character]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_474_gladiia_1#2",fadetime=1)]
[delay(time=1)]
[name="歌蕾蒂娅"]垃圾。你甚至不如盐风城那株上岸的植物，那个女人根本就是在故弄玄虚。
[name="歌蕾蒂娅"]海洋毫无变化可言。
[Character(name="avg_npc_456_1#1$1")]
[name="海嗣"]......Gla-dia......
[Character(name="avg_npc_456_1#1$1")]
[name="海嗣"]......我想见。你自由了？
[Character(name="avg_474_gladiia_1#2")]
[name="歌蕾蒂娅"]......
[Character(name="avg_npc_456_1#1$1")]
[name="海嗣"]这里有同胞。它受困。它需要帮助。它当回归族群怀抱。
[Character(name="avg_npc_456_1#1$1")]
[name="海嗣"]不少同胞，在这里死去。亲代不许。我必须救。
[Character(name="avg_474_gladiia_1#2")]
[name="歌蕾蒂娅"]用你那副丑陋的嘴脸发声，并不能让人感到惊喜。
[Character(name="avg_npc_456_1#1$1")]
[name="海嗣"]你回到大海。不必战斗。
[Character(name="avg_npc_456_1#1$1")]
[name="海嗣"]我们一同——
[dialog]
[character(fadetime=0)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]我已经厌倦了你们的说辞，该了结你了。
[Character(name="avg_npc_456_1#1$1")]
[name="海嗣"]......Gla-dia，你捕食我？
[Character(name="avg_npc_456_1#1$1")]
[name="海嗣"]捕食我，会让你强大？会让你富有活力？
[Character(name="avg_npc_456_1#1$1")]
[name="海嗣"]会让你脖颈上的鳞片生长蔓延，重回你原本模样？
[Character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]——！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.7, block=true)]
[character(fadetime=0)]
[delay(time=0.51)]
[Subtitle(text="深海猎人血脉相连。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
[Blo

... (全文29094字符)
```

### level_act17side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Character(fadetime=0)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.8, crossfade=1, delay=0.5)]
[Background(screenadapt="coverall", image="bg_ibbar", width=1, height=1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[Delay(time=0.8)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[Character(name="avg_npc_451_1#9$1",fadetime=1)]
[delay(time=1)]
[name="蒂亚戈"]......呃......怎么？
[Character(name="avg_npc_450_1#5$1")]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="极境"]你醒了！
[Character(name="avg_npc_450_1#9$1")]
[name="极境"]我可算求求你了，下次再有这种事情能不能提前打个招呼？再演下去，我可就救不了你了！
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]......哼。
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]情况怎么样了？那个女人的怪物，把他们烧光了吗？
[Character(name="avg_npc_450_1#9$1")]
[name="极境"]我不清楚，大概吧，Mon3tr火力全开的样子我也只在作战录像里看过啊......
[Character(name="avg_npc_451_1#7$1")]
[name="蒂亚戈"]......烧吧。烧吧。
[Character(name="avg_npc_451_1#7$1")]
[name="蒂亚戈"]格兰法洛已经是过去的事情了......全烧了吧。
[Character(name="avg_npc_450_1#2$1")]
[name="极境"]......蒂亚戈先生。你......
[dialog]
[character(fadetime=0)]
[Character(name="avg_npc_453_1#1$1",blackstart=0.1,blackend=0.25,fadetime=1)]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="烧伤的教徒"]......哦，叛徒！还有伊比利亚人！我嗅到了你们的味道，你们在这里！
[name="烧伤的教徒"]你们来得正好。你们来得正好——！
[Character(name="avg_npc_450_1#5$1")]
[name="极境"]——你是怎么？！
[Character(name="avg_npc_451_1#4$1")]
[name="蒂亚戈"]哼，他已经瞎了，面目全非，那只怪物让他好受，活该！
[Character(name="avg_npc_451_1#4$1")]
[name="蒂亚戈"]活该！听见了吗？！
[Character(name="avg_npc_453_1#1$1",blackstart=0.1,blackend=0.25)]
[name="烧伤的教徒"]活该？啊，是啊，蒂亚戈，我竟然选择信任一个被仇恨驱使的人，我竟然还对你这样的人抱有幻想，我确实活该。
[name="烧伤的教徒"]但现在，不同，了。（骨骼摩擦的声音）
[dialog]
[character(fadetime=0)]
[PlaySound(key="$d_avg_fish_howl")]
[Character(name="avg_npc_457_1#1$1",name2="avg_npc_457_1#1$1",fadetime=1)]
[delay(time=1.5)]
[Character(name="avg_npc_450_1#12$1")]
[name="极境"]——恐鱼？什么时候？
[Character(name="avg_npc_450_1#12$1")]
[name="极境"]蒂亚戈，别离他太近，这家伙不太对劲！
[Character(name="avg_npc_453_1#1$1",blackstart=0.1,blackend=0.25)]
[name="烧伤的教徒"]伊比利亚必须毁灭！我们会杀死这个国家，这里将成为海洋的起点，浪涛将会触及云层，千万山峦都将无声崩毁——
[name="烧伤的教徒"]我们——即将——融为一体！
[Character(name="avg_npc_450_1#7$1")]
[name="极境"]——！小心！蒂亚戈！
[Dialog]
[Character(name="avg_npc_451_1#4$1",name2="avg_npc_453_1#1$1",blackstart2=0.1,blackend2=0.25)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$p_imp_sword_n", volume=0.9)]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="left", type="move", xpos=-20, fadetime=0.3, block=false)]
[characteraction(name="right", type="move", xpos=-100, fadetime=0.2, block=false)]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
[Character(name="avg_npc_451_1#4$1",name2="avg_npc_453_1#1$1",blackstart2=0.1,blackend2=0.25,focus=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="蒂亚戈"]呃？！咳——！
[Character(name="avg_npc_450_1#12$1")]
[name="极境"]蒂亚戈！啧，他已经开始变成怪物了！就和盐风城的记录一样！
[Character(name="avg_npc_453_1#1$1",blackstart=0.1,blackend=0.25)]
[PlaySound(key="$d_avg_fish_howl")]
[name="烧伤的教徒"]先从你开始，叛徒。
[name="烧伤的教徒"]为了生命得以永恒延续，伊比利亚，不值，一提！
[dialog]
[character(fadetime=0)]
[name="？？？"]不值一提？
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_447_1#1$1",fadetime=1)]
[delay(time=2)]
[name="圣徒卡门"]你在呼唤我的姓名吗？异教徒？
[Character(name="avg_npc_453_1#1$1",blackstart=0.1,blackend=0.25)]
[name="烧伤的教徒"]......大审判官，你来得正好。
[name="烧伤的教徒"]向你们的神祈祷吧，而我们会证明，你们的神不值一提。你会见证伊比利亚沉入深渊。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]那不可能。
[Character(name="avg_npc_453_1#1$1",blackstart=0.1,blackend=0.25)]
[name="烧伤的教徒"]......什么？
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]我的名字是，卡门·伊·伊比利亚，九名圣徒早在给自己套上这个虚伪的称呼时，就摒弃了名字——也一并，摒弃了信仰。
[name="圣徒卡门"]谎言燃烧着我们，我们一清二楚。伊比利亚从未被神明拯救，我们必须成为我们自己的神。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]我代表审判庭，在此宣读对你的判决，异教徒。
[Character(name="avg_npc_453_1#1$1",blackstart=0.1,blackend=0.25)]
[name="烧伤的教徒"]——
为什么会感到沉重？
我的身体已经被同胞接纳，我的生命已经得到升华。
那为什么？为什么我没法从他的提灯上挪开眼？
警惕？对，审判官都很强大，我在警惕。
[name="烧伤的教徒"]你可以杀死我，但是你无法杀死族群。杀死族群，海洋就会死去，陆地就会死去。
[name="烧伤的教徒"]你们终将在进化的浪潮中迷失自我，你们看不见这片大地的未来！这个时代臃肿、无序，我们都是被困在笼中的牲畜！
[name="烧伤的教徒"]我会将你和你的审判庭——
[dialog]
[Character]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[Character(name="avg_npc_453_1#1$1",blackstart=0.1,blackend=0.25)]
[name="烧伤的教徒"]......怎......
他不可思议地看着自己的身体，一段漂亮的横截面。
自他们开始了对格兰法洛的侵袭之后，这位坐镇礼拜堂的老审判官从未真正出手一次。
他没有用过他的剑，从不去碰他的手炮。他只会用提灯和法术，符合他年迈的印象。
是，年迈。他很老了。是一段寻常生命无法承受的岁月。
[Character(name="avg_npc_453_1#1$1",blackstart=0.1,blackend=0.25)]
[name="烧伤的教徒"]陆上......牲畜......你怎么可能？
[name="烧伤的教徒"]你......我至少可以......拖延......
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]你做不到。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]崭新的生命，却连一个老迈的伊比利亚人都杀不死。这又有什么好得意的呢？
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]看着我，异教徒。
[Character(name="avg_npc_453_1#1$1",blackstart=0.1,blackend=0.25)]
[name="烧伤的教徒"]你......咳咳......你！
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]你本为人类，却狭隘地误判了自己种族的可能性。
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]我们赢下这场战争，如同千万年来，生命更迭，物竞天择。
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]你，和你可悲的想法，会被伊比利亚埋葬。在你咽气之前，记得将我们的咆哮传达给你的同族。
[Character(name="avg_npc_447_1#2$1")]
[name="圣徒卡门"]“大海面对的是被称作文明的古老敌人，你们毫无胜算。”
[Character(name="avg_npc_453_1#1$1",blackstart=0.1,blackend=0.25)]
[name="烧伤的教徒"]你......呃......你......什么都不明白......
[dialog]
[de

... (全文20724字符)
```

### level_act17side_10_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g19_lighthouse_front",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8)]
[PlaySound(key="$d_avg_sea", volume=0.6, loop=true, channel="sea")]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]......
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]伊比利亚之眼。距离我上一次登陆这里，已经过了很久很久了。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]无数惩戒军的战士牺牲于此，海嗣最终冲垮了我们的防线，无数工程师枉死在灯塔内。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]在最后一艘船被吞没之前，我们撤离了这里，十不存一。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]但是，现在，看呐。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]灯火！
[character]
卡门的声音久违地有些颤抖。
凯尔希沉默地眺望着远处礁石的中央。巨大的灯塔，照亮天空，如同白昼。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]我没看见船。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]这是个好兆头，说明他们找到了他们想要的。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]前进吧。只要灯火还没有熄灭，我们就能前进。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g19_lighthouse_front",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_457_1#1$1")]
[PlaySound(key="$d_avg_fish_howl")]
[name="恐鱼"]（环绕着大门蠕动的窸窣声）
[Character(name="char_003_kalts_1")]
[name="凯尔希"]......Mon3tr。
[dialog]
[character]
[Character(name="npc_10002",fadetime=0.5)]
[PlaySound(key="$Mon3tr_n")]
[name="Mon3tr"]（尖啸）
[Character(name="char_003_kalts_1")]
[name="凯尔希"]清理大门，我们进去。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]......
[dialog]
[character]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[PlaySound(key="$p_skill_Mon3trburst", volume=0.4)]
[PlaySound(key="$d_sp_ballista", volume=0.4)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[delay(time=1)]
火的温度。
这些恐鱼聚集在门口，徘徊，旋转。
卡门的视线扫向远方，他看见这些可憎怪物焦黑的尸体一路陈列，没入风中。
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]恐鱼不会恐惧。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]但它们懂得趋利避害，本能教会了它们如何谨慎地狩猎。
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]......它们在惧怕。即使这些生物不懂得何为国家，更不屑于律法与道德。
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]但它们仍在惧怕伊比利亚的大审判官，惧怕我们构建在文明之上的一切。
[Character(name="avg_npc_447_1#3$1")]
[stopmusic(fadetime=2)]
[name="圣徒卡门"]达里奥！
[Character(name="char_003_kalts_1")]
[name="凯尔希"]......
[character]
凯尔希没有说话。
[PlayMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.8)]
她看得见。她看得见散发着一片荧光的地面上，有一个诡异的环。
焦黑的尸体堆积成山，成千上万同胞的死亡令恐鱼养成了全新的习性——
——不要靠近那座塔。
[PlaySound(key="$burningloop1", volume=0.6, loop=true,channel="fire")] 
微弱的火苗仍在燃烧。这本是一场大火。
而在恐鱼如浪潮般死去前，这里本没有可燃物。
火焰的中心站着一个人。他提着灯，拄着剑，就像年轻时受训站岗那样，一动不动。
[dialog]
[character(fadetime=0)]
[Character(name="avg_npc_183#3",blackstart=0.2,blackend=0.8,fadetime=1)]
[delay(time=1)]
[name="无言的达里奥"]......
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]达里奥，你做得很好。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]安息吧。
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.5, block=true)]
[character(fadetime=0)]
[Image(image="27_i31",xScale=1, yScale=1,x=70, y=-40)]
[ImageTween(xScaleTo=0.8, yScaleTo=0.8, duration=40,xTo=0, yTo=0,block=false)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Delay(time=0.51)]
达里奥手中的提灯仿佛呼应着卡门的道别，火焰瞬间吞没了更多的恐鱼，熊熊大火将已无声息的大审判官包裹其中。
他早已浑浊的双眼仍看着远方。
卡门在达里奥如雕塑般的身躯前沉默良久。
凯尔希没有打断卡门的哀悼。她只是捕捉着眼中的事物，这里没有太多猎人的痕迹。
只有大审判官独自一人，与恐鱼持续不停地厮杀，至死方休。
而哪怕战士早已力竭而亡，那些恐鱼仍然忌惮他。因为火没有灭，灯没有暗淡。
审判官将自己化作了一种现象，誓死捍卫了伊比利亚之眼的纯洁。
良久，卡门抬起头。
凯尔希这才从眼前这位高龄老人的身上看见岁月的痕迹。即使审判庭用了各种手段延续他的生命，但此刻，他仍旧掩饰不住眼中的疲惫。
他回过头，看向凯尔希，又看了看逐渐没入火焰中的达里奥。
[dialog]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopSound(fadetime=2,channel="fire")] 
[character(fadetime=0)]
[image]
[Background(image="27_g20_lighthouse_core",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_447_1#7$1")]
[name="圣徒卡门"]他是我最好的学生，凯尔希。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]我们有三分钟时间惋惜这位战士的死。等火焰熄灭，恐鱼便没有了筑巢的障碍。它们会蜂拥而至。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]而且，我没看见那个女孩。至少达里奥的弟子活了下来。
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]这里没有更高级的海嗣吗？
[Character(name="char_003_kalts_1")]
[name="凯尔希"]暂时没有。
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]数量不足为惧。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]只是“暂时”。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]我们得寻找一劳永逸的办法。伊比利亚之眼由布雷奥甘建造，它有机会成为与阿戈尔建立联系的终端。
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]前提是她们已经找到了那艘船......慢着。
[Character(name="avg_npc_447_1#4$1")]
[name="圣徒卡门"]是谁重新启动了伊比利亚之眼？阿戈尔人和达里奥都应该是初来乍到......
[stopmusic(fadetime=1)]
[dialog]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[Dialog]
[character(fadetime=0)]
[dialog]
[character(name="char_empty")]
[characteraction(name="middle", type="move", ypos=300, fadetime=0,block=true)]
[Character(name="avg_npc_457_1#1$1",fadetime=0.4)]
[characteraction(name="middle", type="move", ypos=-300, fadetime=0.4,block=true)]
[CameraShake(duration=1, xstrength=10, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[delay(time=1)]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]......看来在上面。
[stopSound(channel="sea",fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g20_lighthouse_core",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8)]
[Character(name="avg_4042_lumen_1#7$1")]
[name="乔迪"

... (全文40213字符)
```

### level_act17side_10_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g20_lighthouse_core",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$plot_intro", key="$plot_loop",fadetime=3, volume=0.8)]
[Character(name="avg_4042_lumen_1#13$1")]
[name="乔迪"]......
[Character(name="avg_npc_447_1#4$1")]
[name="圣徒卡门"]......这，不可能。
[Character(name="avg_npc_447_1#4$1")]
[name="圣徒卡门"]如果真是这样，从一开始，深海猎人们寻找的东西竟然就如此之近......
[Character(name="char_003_kalts_1")]
[name="凯尔希"]这种可能性象征的东西太过恶劣。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]伊比利亚之眼始终注视着灾难的余波。但它只是一只沉沦的眼眸，它无法言语。
[Character(name="avg_npc_447_1#7$1")]
[name="圣徒卡门"]......这意味着什么？
[Character(name="char_003_kalts_1")]
[name="凯尔希"]这意味着阿戈尔溃败的速度在加快。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]也意味着......如果连这个距离的城市都会发出求援信号，那么“愚人号”从一开始就只是在它们巢穴的上方打转。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]......猎人们有危险。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]我知道你在想什么，但我们只有一艘船，两个人。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]救援斯图提斐拉并不现实。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]您也许不介意几名深海猎人命丧大海，但我们扼杀的是机会。对阿戈尔和伊比利亚而言都是。
[Character(name="avg_npc_447_1#2$1")]
[name="圣徒卡门"]......
[Character(name="char_003_kalts_1")]
[name="凯尔希"]......达里奥已经战死。您难道不想从剩下的那位审判官嘴里，获取宝贵的知识？
[Character(name="char_003_kalts_1")]
[name="凯尔希"]这是最后的机会。
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]不。一座几近崩溃的、无能为力的城市，意味着其中有多少已经倒向海洋的阿戈尔人？
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]我们应该谨慎对待，否则无异于引火烧身。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]即使如此，这也是，最后的机会。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]等到阿戈尔再不回应任何讯息，直到又一次静谧降临在伊比利亚头顶，真正的敌人才会显现。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]可那没有意义。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]我理解您背负的职责，在惩戒军真正接管这里之前，您不会选择任何冒险的举措。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]所以我一人去。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]......我不低估你和你那只宠物的力量。但路途遥远，你一个人真能安然无恙地抵达？
[Character(name="char_003_kalts_1")]
[name="凯尔希"]猎人们流着特殊的血。恐鱼未必会对寻常的船只产生过大的敌意。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]希望这不只是你试图取得我的认同而编撰出的事情。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]我也不会编撰这样的话语。我只是不能抛下猎人们。
[Character(name="avg_4042_lumen_1#1$1")]
[name="乔迪"]......
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]呼......
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]......要把猎人们和艾丽妮都带回来，凯尔希。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]我会的。
[Character(name="avg_4042_lumen_1#1$1")]
[name="乔迪"]......那、那个......
[Character(name="avg_4042_lumen_1#6$1")]
[name="乔迪"]我能帮上什么忙吗？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g19_lighthouse_front",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_sea", volume=0.6, loop=true, channel="sea")]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]Mon3tr，警戒周围，如果那些恐鱼躲回了海面下的巢穴，就别刺激它们。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]我们需要点时间，这艘船已经在刚才的航行中有所损伤。
[dialog]
[character]
[Character(name="npc_10002",fadetime=0.5)]
[PlaySound(key="$Mon3tr_n")]
[name="Mon3tr"]（点头回应）
[Character(name="avg_4042_lumen_1#6$1")]
[name="乔迪"]这艘船......
[Character(name="char_003_kalts_1")]
[name="凯尔希"]先前猎人们乘坐的是审判庭的谍报人员留下的船。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]而卡门阁下的原计划是在格兰法洛与惩戒军会合，建立前线指挥部后，乘中型水陆军舰前往这里。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]所以这艘被遗留在格兰法洛沙滩上的孤舟，是我们最后的希望。
[Character(name="avg_4042_lumen_1#13$1")]
[name="乔迪"]我、我来帮忙......我去船上稍微看看。虽然我从来没修过船，呃，不过我还是带着一些工具的。
[Character(name="avg_4042_lumen_1#11$1")]
[name="乔迪"]唔，只靠这艘船，真的能深入大海吗？
[Character(name="char_003_kalts_1")]
[name="凯尔希"]如果你觉得不能，那就一定不能——等等！
[Character(name="char_003_kalts_1")]
[name="凯尔希"]让开！乔迪！
[Character(name="avg_4042_lumen_1#8$1")]
[name="乔迪"]唔啊——！？
[dialog]
[character]
[PlaySound(key="$d_avg_fish_howl")]
[Character(name="avg_npc_457_1#1$1",name2="avg_npc_457_1#1$1",fadetime=1)]
[delay(time=2)]
[Character(name="avg_4042_lumen_1#8$1")]
[name="乔迪"]恐、恐鱼——！？
[Character(name="avg_4042_lumen_1#9$1")]
[name="乔迪"]呜啊啊——
[Character(name="char_003_kalts_1")]
[name="凯尔希"]潜藏在礁石的阴影下？Mon3tr！
[dialog]
[character]
[Character(name="npc_10002",fadetime=0.5)]
[PlaySound(key="$Mon3tr_n")]
[name="Mon3tr"]（欢快的尖啸）
[dialog]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[PlaySound(key="$p_skill_Mon3trburst", volume=0.4)]
[PlaySound(key="$d_sp_ballista", volume=0.4)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[delay(time=1)]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]乔迪！从船上跳下来！
[Character(name="avg_4042_lumen_1#8$1")]
[name="乔迪"]可、可是有什么在推着这艘船！船锚已经不见了！
[Character(name="avg_4042_lumen_1#13$1")]
[name="乔迪"]我、我试着把它开回来——
[Character(name="char_003_kalts_1")]
[name="凯尔希"]跳船！恐鱼群在包围它！
[Character(name="char_003_kalts_1")]
[name="凯尔希"]Mon3tr，把他救回来。
[Character(name="avg_4042_lumen_1#13$1")]
[name="乔迪"]等等——这样我们会失去这艘船的，我、我试着驾驶它，呃！
[Character(name="avg_4042_lumen_1#6$1")]
[name="乔迪"]你身后！
[Character(name="char_003_kalts_1")]
[name="凯尔希"]——
[dialog]
[character]
[PlaySound(key="$d_avg_fish_howl")]
[Character(name="avg_npc_457_1#1$1",fadetime=1)]
[delay(time=2)]
[Character(name="npc_10002",fadetime=0.5)]
[dialog]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[Character(name="avg_npc_457_1#1$1")]
[PlaySound(key="$bodyfalldown1", volume=1)]
[character(fadetime=1)]
[delay(time=2)]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]先去救乔迪。
[Character(name="npc_10002")]
[PlaySound(key="$Mon3tr_n")]
[name="Mon3tr"]（回应的欢鸣）
[Character(name="char_003_kalts_1")]
[name="凯尔希"]漩涡，洋流在变化，恐鱼也格外活跃......发生了什么？
[Dialog]
[Bloc

... (全文39686字符)
```

### level_act17side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act17side/SN01.mp4")]
```

### level_act17side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop",fadetime=3, volume=0.4)]
“大地”。
这个词语因狭隘而普及。
是否在某个远古的时期，我们曾有一些宏伟的语言，用来形容天地间的一切，用来形容我们的生活所触及到的全部？
这个伟大的词语囊括土地与天空，以及内陆诸国知之甚少的浩瀚海洋......只需唇齿开合，一个单词，或许就能描述万亿年来生命的进程？
这个词存在于人类思想的哪个角落，凯尔希？
[Dialog]
[Image(image="27_i25",  xScale=1.3, yScale=1.3, x=-200, y=-70)]
[Blocker(a=0, fadetime=3, block=true)]
[name="凯尔希"]您不会不知道。
[name="稳重的老者"]我知道的并不少，可我仍要日复一日地询问，所有人都摆脱不了未知，而未知会永远地拷问人类。
[name="凯尔希"]......
[name="凯尔希"]......（古老的萨卡兹语）“世界”。
[name="稳重的老者"]唔，我以为你会说......（萨尔贡语）“世界”。
[name="稳重的老者"]那是萨卡兹的语言吗？
[name="凯尔希"]是的。
[name="稳重的老者"]稀奇，一个自诩为医生的菲林，第一反应居然是使用魔族的语言。
[name="稳重的老者"]你的身份就像海上的云朵，变幻无常。
[name="凯尔希"]语言不会因此而改变性质。
[name="稳重的老者"]语言......你看，凯尔希，看这里。一口井。
[Dialog]
[ImageTween(xFrom=-200, yFrom=-70, xTo=-70, yTo=50, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=0.9, yScaleTo=0.9,ease="OutQuad", duration=20, block=false)]
[Delay(time=5)]
[name="稳重的老者"]你知道如何在这里获取淡水吗？你知道伊比利亚人如何利用这片蔚蓝的基石搭建房屋吗？
[name="凯尔希"]如果曾经的伊比利亚贵族并没有被傲慢冲昏头脑，那海洋势必会让伊比利亚成为一座坚不可摧的堡垒。
[name="凯尔希"]这口井很深，这里离海很近。
[name="稳重的老者"]看，这口井还没有干涸，它装着一个假的太阳。
[name="凯尔希"]我们该赶路了，阁下。
老者没有回答。他默默从地上拾起了一枚石子。
一枚再普通不过的石子，没有把玩的价值，可老者仿佛在感受海风留下的触感，他依旧看着井底。
凯尔希没有追问，她默默等待面前的老人给出回答。她能看见云在运动，风很大。
[name="稳重的老者"]不着急，凯尔希，不着急。我们还有很多时间歇息......无论你做好了什么布置。
[name="稳重的老者"]从这里投下一颗石子，要多久能听见水声？
[name="凯尔希"]五六秒。
[name="稳重的老者"]伊比利亚最朴实的人民也懂得如何利用海洋，这口井的深度蕴藏着智慧。
[name="凯尔希"]而如今，一名维多利亚的农夫或是哥伦比亚的工人，也许连海洋的全貌都不知晓。
[name="稳重的老者"]唔......凯尔希，这一路上，我总共问过你几个问题？
老人将握着石子的手臂悬在半空，松手，那枚石子从他的手中滑落。
二人都注视着这枚石子，尽管很快，缺乏阳光的视野就无法再捕捉石子的轨迹。
两秒，或者是三秒，寂静笼罩着二人。风声都在此刻停止。
寂静。凯尔希想着，多么寂静。
[Image(image="27_i25",  xScale=1.2, yScale=1.2, x=-150, y=50,fadetime=1)]
[image]
[Image(image="27_i25",  xScale=1.3, yScale=1.3, x=-150, y=50,fadetime=1)]
[CameraShake(duration=0.5, xstrength=10, ystrength=0, vibrato=15, randomness=20,fadeout=true)]
[ImageTween(xScaleFrom=1, yScaleFrom=1, xScaleTo=1.15, yScaleTo=1.15, duration=1, block=false)]
[Image(image="27_i25",  xScale=0.9, yScale=0.9, x=-70, y=50,fadetime=0.5)]
[playsound(key="$waterbubble_n",volume=0.7)]
[playsound(key="$watergun_n_cast",delay=0.2)]
“扑通”。
细小的声响穿过井壁，仿佛在提醒二人，那短暂的、仅有数秒的瞬间里，这片大地如此静谧。
[name="凯尔希"]一百二十三个，这是个具有魔力的数字。
[name="稳重的老者"]一百二十三个问题，一百二十三年。如今的审判庭里......没有比我更年长的审判官了。
[name="稳重的老者"]他们大都战死，极少寿终正寝，还有些许，在这场看不见尽头的折磨中败给了怯懦，他们的下场都不算好。
[name="稳重的老者"]我亲历过伊比利亚的所有。我曾看过舰队扬帆，听过维多利亚使节颤抖的嗓音。
[name="稳重的老者"]大静谧摧毁了一切，就像大梦初醒。所有伊比利亚人都还沉浸在对灾难的痛恨与美梦破灭的茫然之中。
[name="凯尔希"]黎博利并非长寿的种族，就算是黎博利的神民，那些健康的长寿者，也无法背负伊比利亚如今遭受的灾厄。
[name="凯尔希"]您的寿命是一个奇迹。审判庭创造的奇迹，也赋予了您前所未有的使命感。
[name="凯尔希"]在那个思想与荣耀开始坠落的时代，您与那些最初的审判庭成员被尊称为“圣徒”。
[name="稳重的老者"]“圣徒”，这个曾用来引领世人的称号就像一把薪柴......如今徒留灰烬。
[name="稳重的老者"]一百二十三轮春夏秋冬，仿佛只有寒冬给我留下了痕迹。我见过很多真相，却唯独记不住春天的样子。
[name="稳重的老者"]......凯尔希。
[name="凯尔希"]嗯。
老人的眼神变了。
信念是一种语言，祷告铺成道路。伊比利亚这个国家，或是超越了国家的个体，此刻正轻抚自己的下巴，计算风的速度。
[name="稳重的老者"]我活到今天，度过了一百二十三年岁月。我问了你一百二十三个问题，与我曾经的体悟一一对应。
[name="稳重的老者"]可你仍回答了我的每一个问题。你知道我知道的所有事情。
[name="稳重的老者"]人类在前进。秘密将永远不断涌现，可学识越不过名为“已知”的高墙。
[name="稳重的老者"]而我们所对抗的，却在那堵高墙的另一头，那是一片昏暗的黑森林。
[name="稳重的老者"]而你呢，凯尔希，你属于高墙这头......还是在森林的彼端？
[name="凯尔希"]取决于您。
[name="稳重的老者"]哼，呵呵......你甚至知道那边的树上有多少树叶，可怕的女人。
[name="稳重的老者"]伊比利亚的圣徒仍是穷尽人力所能抵达的顶峰，这毫无疑问。而你超出了这个范畴，所以你绝非常人。
[name="稳重的老者"]也许你利用了某种特别的法术延长了寿命，也许你传承着某些古老的身份，又也许，你有一个曾立下宏愿的灵魂。
[name="凯尔希"]......
[name="稳重的老者"]哪怕信仰不过是一场思想组成的骗局，我们也曾坚信希望。而可悲的是，直到衰老将我们一一打败，我们仍然找不出解决问题的办法。
[name="稳重的老者"]那些依靠自身的源石技艺或是别的手段战胜衰老的长生者，他们只会更加恐惧，恐惧遭受敌人无尽折磨的漫长岁月。
[name="凯尔希"]阿戈尔何时也被伊比利亚视作未知的恐惧？
[name="稳重的老者"]一个赤手空拳的孩子，怎能轻易接受一个手持利器的陌生人帮助自己？
[name="凯尔希"]可如果这个孩子即将溺毙？
[name="稳重的老者"]你仍旧得证明你所说的。阿戈尔的现状真如你所说那般吗？海嗣与其根源真的有办法被战胜吗？
[name="稳重的老者"]否则伊比利亚不会信任你。我不会信任你。
[name="稳重的老者"]在我死前，凯尔希，在我死前，你，你们，必须证明给伊比利亚看。
[name="稳重的老者"]否则，海水会浇灭文明的火，在其他国家准备好之前，它们会越过伊比利亚，它们会......撕扯这个“世界”。
[name="稳重的老者"]说不定否定泰拉文明与社会的全部过程，在它们的思维的尘埃里，都只是物竞天择的一小部分。
[name="凯尔希"]又也许，我们并无本质上的差异。
[stopmusic(fadetime=2)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Image]
[Background(image="27_g16_lighthouse_street",screenadapt="coverall")]
[playMusic(intro="$tech_intro", key="$tech_loop",fadetime=3, volume=0.4,delay=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="npc_2002_Dan_1",fadetime=1)]
[Delay(time=1)]
[name="Dan"]......海边的小镇，清闲，但又阴冷。宁静，但也喧闹。看似生机勃勃，可又危机四伏，谜团四起......
[name="Dan"]感觉会是个激发创作欲的好地方！
[name="Dan"]你们说呢？
[Dialog]
[Character]
[Character(name="npc_2003_Frost_1",fadetime=1)]
[Delay(time=1)]
[name="Frost"]（轻盈的独奏）
[Dialog]
[Character]
[Character(name="npc_2001_Aya_1",fadetime=1)]
[Delay(time=1)]
[name="Aya"]海边，不安的气氛。我已经能嗅到那些讨人厌的东西了。
[name="Aya"]我还是觉得我们不该这么草率地出现在海滨。
[Dialog]
[Character]
[Character(name="npc_2004_Alty",fadetime=1)]
[Delay(time=1)]
[name="Alty"]没关系，刺激能产生灵感，你看Dan已经迫不及待了不是吗？
[Character(name="npc_2003_Frost_1")]
[name="Frost"]（低沉的独奏）
[Character(name="npc_2002_Dan_1")]
[name="Dan"]音乐的灵感！
[Character(name="npc_2002_Dan_1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]......对。汲取灵感的机会。
[Character(name="npc_2001_Aya_1")]
[name="Aya"]我从没想过我们会依靠那片变异的海洋汲取灵感。
[Character(name="npc_2002_Dan_1",name2="npc_2004_Alty",focus=1)]
[name="Dan"]正因为没想过，才有取材的价值。
[Character(name="npc_2002_Dan_1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]说得好。
[Character(name="npc_2003_Frost_1")]
[name="Frost"]（赞同的独奏）
[Character(name="npc_2001_Aya_1")]
[name="Aya"]......那，我们要分头行动吗？我可以一个人把行李带去旅店。
[Character(name="npc_2002_Dan_1")]
[name="Dan"]好哎！那我先去那边看看？
[Character(name="npc_2001_Aya_1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]你一个人？
[Character(name="npc_2001_Aya_1",name2="npc_2004_Alty",focus=1)]
[name="Aya"]谢谢你的担心，也谢谢你记得我们在这里是会有“危险”的。
[Character(name="npc_2003_Frost_1")]
[name="Frost"]旅店，在哪儿？
[Character(name="npc_2002_Dan_1")]
[name="Dan"]说起来，这样的小镇竟然还能有旅店？会有人来这种地方吗？
[Character(name="npc_2001_Aya_1",name2="npc_2004_Alty",focus=1)]
[name="Aya"]大家总要想办法活下去的。
[Character(name="npc_2001_Aya_1",name2="npc_2004_Alty",focus=2)]
[name="Alty"]对，活下去才有音乐。
[

... (全文31955字符)
```

### level_act17side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_snowconutryinside",screenadapt="coverall")]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop",fadetime=3, volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_451_1#7$1",fadetime=1)]
[PlaySound(key="$rungeneral",volume=0.7)]
[Delay(time=1.5)]
[Character(name="avg_npc_451_1#4$1")]
[name="蒂亚戈"]乔迪！
[Character(name="avg_4042_lumen_1#8$1")]
[name="乔迪"]啊......蒂亚戈叔叔......怎么了吗？
[Character(name="avg_4042_lumen_1#8$1",name2="avg_npc_451_1#4$1",focus=2)]
[name="蒂亚戈"]......你......快收拾东西，准备离开这里。
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_451_1#4$1",focus=1)]
[name="乔迪"]呃、怎、怎么了？我们要去哪儿？
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_451_1#7$1",focus=2)]
[name="蒂亚戈"]审判庭很快就会来这座小镇。
[Character(name="avg_4042_lumen_1#10$1",name2="avg_npc_451_1#7$1",focus=1)]
[name="乔迪"]......什么？
[Character(name="avg_4042_lumen_1#10$1",name2="avg_npc_451_1#2$1",focus=2)]
[name="蒂亚戈"]那些邪教徒，海里的怪物，那些——
[Character(name="avg_4042_lumen_1#9$1",name2="avg_npc_451_1#2$1",focus=1)]
[name="乔迪"]......
[name="乔迪"]我们......要放弃这座小镇吗？
[Character(name="avg_4042_lumen_1#9$1",name2="avg_npc_451_1#6$1",focus=2)]
[name="蒂亚戈"]我们？
[Character(name="avg_4042_lumen_1#9$1",name2="avg_npc_451_1#2$1",focus=2)]
[name="蒂亚戈"]......
[Character(name="avg_4042_lumen_1#9$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]不，不，孩子，只有你要离开这里，审判庭发现这里有邪教徒之后，一定会找阿戈尔人的麻烦！
[name="蒂亚戈"]我不在乎那些邪教徒怎么样，也不在乎我们自己的命......我们在这里生活了太久，我们不知道去其他地方该怎么活下来，我们不会走。
[Character(name="avg_4042_lumen_1#9$1",name2="avg_npc_451_1#4$1",focus=2)]
[name="蒂亚戈"]但你不一样！你不是，一直想要看看外面的城市和风景吗？你还年轻，你有天赋......
[Character(name="avg_4042_lumen_1#11$1",name2="avg_npc_451_1#4$1",focus=1)]
[name="乔迪"]可是我、我......这太突然了。
[Character(name="avg_4042_lumen_1#11$1",name2="avg_npc_451_1#4$1",focus=2)]
[name="蒂亚戈"]这是一个机会，乔迪，一个改变的机会，最后的机会。你得勇敢一点。
[name="蒂亚戈"]留在这里，遭受审判庭的讯问，就算侥幸回家，也不过是在对海浪与恐鱼的担忧中空度余生。
[name="蒂亚戈"]可如果你离开......你的命运就握在了你自己的手里，不是那座小小的礼拜堂。
[Character(name="avg_4042_lumen_1#11$1",name2="avg_npc_451_1#2$1",focus=2)]
[name="蒂亚戈"]那座礼拜堂太小了......你不该就这么......
[Character(name="avg_4042_lumen_1#10$1",name2="avg_npc_451_1#2$1",focus=1)]
[name="乔迪"]蒂亚戈叔叔......我......可是这么突然......
[Character(name="avg_4042_lumen_1#10$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]别犹豫不决了，孩子，你要坚强些，更坚强些，就像你的父母和你的祖父母辈那样。
[Character(name="avg_4042_lumen_1#5$1",name2="avg_npc_451_1#1$1",focus=1)]
[name="乔迪"]......我的父母，他们真的是为伊比利亚的事业奉献了生命？
[Character(name="avg_4042_lumen_1#5$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]现在说这干什么——快，来一起收拾。
[Dialog]
[Character(name="avg_4042_lumen_1#5$1",name2="char_empty",fadetime=0.5)]
[Delay(time=1)]
[PlaySound(key="$d_avg_clothmovement",volume=0.5)]
[Delay(time=1)]
[Character(name="avg_4042_lumen_1#5$1",name2="char_empty",focus=3)]
[name="蒂亚戈"]唉，太久没见游商，都是些旧衣裳......年轻的小伙子想要穿一身新，还要费那么大力气......离开不好吗？
[Character(name="avg_4042_lumen_1#10$1",name2="char_empty",focus=1)]
[name="乔迪"]可是审判庭为什么要抓阿戈尔人？如果真有邪教徒，就没可能是黎博利、菲林之类的吗？
[Character(name="avg_4042_lumen_1#10$1",name2="char_empty",focus=2)]
[name="蒂亚戈"]阿戈尔人从海里来，怪物和灾难也从海里来。
[Dialog]
[Character(name="avg_4042_lumen_1#10$1",name2="avg_npc_451_1#9$1",fadetime=0.5,focus=2)]
[Delay(time=1)]
[name="蒂亚戈"]......你见过他们了？
[Character(name="avg_4042_lumen_1#11$1",name2="avg_npc_451_1#9$1",focus=1)]
[name="乔迪"]不......我......等等，蒂亚戈叔叔，你知道......？你知道他们在这里？
[Character(name="avg_4042_lumen_1#11$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]嗯......我知道那些谣言不是空穴来风，我们都心知肚明。
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_451_1#1$1",focus=1)]
[name="乔迪"]胡安是他们的一员......他从小巷躲进阴暗无人的仓库，他受伤了，而且......他对我没有恶意。
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_451_1#4$1",focus=2)]
[name="蒂亚戈"]只是因为你是个阿戈尔人，孩子。他们疯了，他们不正常，我也清楚。
[Character(name="avg_4042_lumen_1#11$1",name2="avg_npc_451_1#4$1",focus=1)]
[name="乔迪"]那你为什么......难道蒂亚戈叔叔是在包庇他们？
[Character(name="avg_4042_lumen_1#11$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]这都无所谓，你很快就要离开这里了。
[Character(name="avg_4042_lumen_1#13$1",name2="avg_npc_451_1#1$1",focus=1)]
[name="乔迪"]不，蒂亚戈叔叔，我不想离开。
[Character(name="avg_4042_lumen_1#13$1",name2="avg_npc_451_1#7$1",focus=2)]
[name="蒂亚戈"]什么？
[Character(name="avg_4042_lumen_1#11$1",name2="avg_npc_451_1#7$1",focus=1)]
[name="乔迪"]我......我生在格兰法洛，如果只是为了躲避审判庭就逃离这里，我......我不知道......
[Character(name="avg_4042_lumen_1#11$1",name2="avg_npc_451_1#4$1",focus=2)]
[name="蒂亚戈"]你什么？你知道自己在说什么吗？！
[Character(name="avg_npc_451_1#4$1")]
[name="蒂亚戈"]没有阿戈尔人被带去审判庭之后还能完好无损地回来！他们要么落下残疾，要么精神失常——
[CameraShake(duration=0.5, xstrength=5, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_451_1#5$1")]
[name="蒂亚戈"]——更多人直接人间蒸发了，有人说审判庭囚禁了他们，也有人说审判官直接处死了那些嫌疑犯！总之没有人回来，没有人！
[CameraShake(duration=3, xstrength=5, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="蒂亚戈"]在那些怪物和深海教徒开始肆虐之前，“好心的”审判庭会先把这里的一切付诸一炬，没有什么比毁灭更有效的净化方法！
[CameraShake(duration=0, xstrength=5, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_4042_lumen_1#1$1")]
[name="乔迪"]蒂、蒂亚戈叔叔......冷静点！
[Character(name="avg_npc_451_1#5$1")]
怒发冲冠的老人眼里映出乔迪的模样，就像多少年前他惴惴不安地来到这里，想要从一片废墟中亲手建起新的庭院那样。
半辈子过去了，一群年轻有力的人最黄金的年纪过去了，他们在格兰法洛建立了什么？伊比利亚如今怎样？
他们的添砖加瓦没有对命运产生丝毫的影响，就像投进深井的石子，而曾经他们满怀热情建起的家园如今也摇摇欲坠。
巨大的虚无感吞没了蒂亚戈。如同此刻海面上的阴云，笼罩一切。
[Character(name="avg_npc_451_1#4$1")]
[name="蒂亚戈"]......没有人......
[Character(name="avg_npc_451_1#2$1")]
[name="蒂亚戈"]没有人......没有人回来，马琳没有，他们都没有。格兰法洛已经在燃烧了，审判庭也好，怪物也好，我们没有出路......
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_451_1#2$1",focus=1)]
[name="乔迪"]蒂亚戈叔叔......
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_451_1#2$1",focus=2)]
[name="蒂亚戈"]......乔迪，你如果出了什么事，我没法向你的父母交代。
[Character(name="avg_4042_lumen_1#1$1",name2="avg_npc_451_1#2$1",focus=1)]
[name="乔迪"]......我......我知道。我......
[Character(name="avg_4042_lumen_1#11$1",name2="avg_npc_451_1#2$1",focus=1)]
[name="乔迪"]......
[Character(name="avg_4042_lu

... (全文19812字符)
```

### level_act17side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_183#1",blackstart=0.3,blackend=0.7,fadetime=1)]
[Delay(time=1)]
[name="大审判官"]艾丽妮。
[Character(name="avg_4009_irene_1#1$1",name2="avg_npc_183#1",blackstart=0.3,blackend=0.7,blackstart2=0.3,blackend2=0.7,focus=1)]
[name="审判官艾丽妮"]欸？啊，我在，老师......不，长官！
[Character(name="avg_4009_irene_1#1$1",name2="avg_npc_183#1",focus=2)]
[name="大审判官"]你还好吗？
[Character(name="avg_4009_irene_1#1$1",name2="avg_npc_183#1",focus=1)]
[name="审判官艾丽妮"]我......我没事。
[Character(name="avg_4009_irene_1#1$1",name2="avg_npc_183#1",focus=2)]
[name="大审判官"]格兰法洛只是一座小镇，在很多地图上也许都找不到的小镇。
[name="大审判官"]即使如此，这也是卡门阁下的委托，与凯尔希医生和那几个阿戈尔人都有关联。
[Character(name="avg_4009_irene_1#1$1",name2="avg_npc_183#1",focus=1)]
[name="审判官艾丽妮"]我知道，长官，所以我——
[Character(name="avg_4009_irene_1#1$1",name2="avg_npc_183#1",focus=2)]
[name="大审判官"]如果你还得不出答案，我不允许你同行。
[Character(name="avg_4009_irene_1#1$1",name2="avg_npc_183#1",focus=1)]
[name="审判官艾丽妮"]选择成为审判官跟随长官的时候，我就已经做好了准备！
[Character(name="avg_4009_irene_1#1$1",name2="avg_npc_183#1",focus=2)]
[name="大审判官"]如果你得出的答案还无法诠释你之前的所见所闻，就更不要简单得出结论。
[name="大审判官"]不要白白送死，艾丽妮。你已经明白我们对抗的是什么，你必须得出你自己的答案。
[Character(name="avg_4009_irene_1#1$1",name2="avg_npc_183#1",focus=1)]
[name="审判官艾丽妮"]我——
[name="审判官艾丽妮"]......我明白了，长官。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(fadetime=0)]
[Background(image="bg_ibchurch",screenadapt="coverall")]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4,fadetime=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_474_gladiia_1#1",fadetime=1)]
[Delay(time=1)]
[name="歌蕾蒂娅"]凯尔希女士。
歌蕾蒂娅的语调没有变化，但她的脚步能够反映出她的心情。
[Character(name="char_003_kalts_1#1",name2="avg_474_gladiia_1#1")]
[Characteraction(name="right", type="move", xpos=30, fadetime=0, block=true)]
[Characteraction(name="right", type="move", xpos=-30, fadetime=0.3, block=true)]
只消一瞬，风发出声响所需的时间，她就来到了凯尔希的身边。
[Character(name="char_003_kalts_1#1",name2="avg_474_gladiia_1#1",focus=1)]
[name="凯尔希"]辛苦了，歌蕾蒂娅。
[Character(name="char_003_kalts_1#1",name2="avg_474_gladiia_1#4",focus=2)]
[name="歌蕾蒂娅"]审判庭似乎没有对你做什么，对吧？
[Character(name="char_003_kalts_1#1",name2="avg_474_gladiia_1#4",focus=1)]
[name="凯尔希"]伊比利亚还没有沉没，这就是他们尚存些微谦卑与警觉的证明。
[Character(name="char_003_kalts_1#1",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]你找到办法了，如我们所约定的那样。
[Character(name="char_003_kalts_1#1",name2="avg_474_gladiia_1#1",focus=1)]
[name="凯尔希"]是的。但是......
[name="凯尔希"]......如果伊比利亚愿意放下他们所担忧的，那阿戈尔呢？
[name="凯尔希"]你呢？
[Character(name="char_003_kalts_1#1",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]如果我们别无他路......而短暂的合作能帮助我们回到海洋，我愿意合作。
[Dialog]
[Character]
[playsound(key="$d_gen_walk_n", loop=true, channel="bgs")]
[Character(name="npc_2004_Alty",fadetime=1)]
[Delay(time=1)]
[StopSound(channel="bgs", fadetime=1)]
[name="Alty"]总算有个像样的阿戈尔人了，对吧？就像浪涛本身，就像海洋的光线与触感。
[Character(name="npc_2004_Alty",name2="avg_474_gladiia_1#1",focus=1)]
[name="Alty"]你好啊，特别的阿戈尔人。我想你已经见过我们的其他成员了。
[Character(name="npc_2004_Alty",name2="avg_474_gladiia_1#3",focus=2)]
[name="歌蕾蒂娅"]是的，那么，您也是日落即逝的成员。
[Character(name="npc_2004_Alty",name2="avg_474_gladiia_1#3",focus=1)]
[name="Alty"]贝斯手Alty。很高兴见到你。
[name="Alty"]外面怎么样了？
[Character(name="npc_2004_Alty",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]那些深海教徒倾巢而出，数量不少，但很弱。
[name="歌蕾蒂娅"]猎人们足以处理所有问题。
[Character(name="char_003_kalts_1#1")]
[name="凯尔希"]解决格兰法洛的问题后，审判庭才会与我们合作。
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]那就让我们立刻开始。
[Dialog]
[Character(fadetime=0.5)]
歌蕾蒂娅提起了她的长槊。
可几乎与此同时，她感到了某种异样。
[Character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]......！
[Character(name="avg_474_gladiia_1#2")]
[name="歌蕾蒂娅"]......不，这些恐鱼中混杂着......不可能......
[Dialog]
[Character(name="char_003_kalts_1#1")]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[Delay(time=1)]
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]是我。
[Character(name="char_003_kalts_1#3",focus=3)]
[name="极境"]凯尔希医生！他们的目的是——
[Dialog]
[PlaySound(key="$d_sp_chixiaobadao",volume=0.4)]
[PlaySound(key="$transmission",volume=0.5)]
[PlaySound(key="Sound_Beta_2/Player/p_imp/p_imp_funnel_end_h",delay=1)]
[Delay(time=2)]
[Character(name="char_003_kalts_1#2")]
[name="凯尔希"]......极境？
[Character(name="char_003_kalts_1#2",name2="avg_474_gladiia_1#5",focus=2)]
[name="歌蕾蒂娅"]怎么了？
[Character(name="char_003_kalts_1#2",name2="avg_474_gladiia_1#5",focus=1)]
[name="凯尔希"]我们的干员遇到了危险。
[Character(name="char_003_kalts_1#2",name2="avg_474_gladiia_1#5",focus=2)]
[name="歌蕾蒂娅"]有什么潜藏在这里。
[Character(name="char_003_kalts_1#1")]
[name="凯尔希"]......Alty，就像我们说的那样。日落即逝的各位，只要留在岸上就足够。
[name="凯尔希"]我们会尽快解决问题。
[Character(name="npc_2004_Alty")]
[name="Alty"]好啊，我们等你。
[name="Alty"]如果你们的征途需要一些音乐点缀的话，那我们更乐意效劳。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Delay(time=0.6)]
[Background(image="27_g16_lighthouse_street",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$skadi_n", volume=1)]
[Character(name="avg_npc_457_1#3$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
[Character(fadetime=0.5)]
[Delay(time=1)]
[Character(name="char_263_skadi#3",fadetime=0.5)]
[name="斯卡蒂"]......太弱了。
[name="斯卡蒂"]它们这样前仆后继，就像在拖延时间......
[Character(name="char_263_skadi#8")]
[name="斯卡蒂"]......又或者，它们是在......散播什么？
[Character(name="char_263_skadi#8")]
[name="斯卡蒂"]得找出它们的头儿。
[Character(name="avg_npc_457_1#1$1")]
[name="恐鱼"]——嘎——！
[Dialog]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.03, block=true)]
[Character(fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_1023_ghost2_1#4$1",fadet

... (全文19653字符)
```

### level_act17side_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="27_g26_dusk_wild",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[delay(time=2)]
[Subtitle(text="“我从潮湿的居所抵达这处干燥的新天地，这里的一切都让人触目惊心，悲痛交加。”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“云朵并没有传说中那般美好，大地与天空都肆虐苦难，堪比阿戈尔的城市也会毁于天灾。”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“陆上的人们还困扰于某种无解的疾病，我曾在科学院的诸多文献中得知矿石病与源石的存在，如今亲眼目睹，深知它已然成为陆地的一部分，根深蒂固。”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“但即使如此，他们仍顽强地活着，以独有的方式探索科技与真理，谋求存续的凭证。”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“即使被称作叛徒，我也并不后悔来到陆地的决定。海嗣族群在扩张，十年内，阿戈尔将被彻底围困。而有朝一日，我也将完成游历，回到伊比利亚。”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“我会留下这些文献，供阿戈尔人解读和寻找。我不信任贵族，想必今天被称为岛民的阿戈尔人，迟早会因为种种原因失去伊比利亚的尊重。”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“黄金的大船，文明的眼睛，进化的法理，生命的石碑。大海和陆地必须结成阵线，抵御浪涛。”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“我无意成为先驱，我只是先命运一步。”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
——伊比利亚著名建筑师、首席船舶设计师布雷奥甘的笔记副本，用晦涩的阿戈尔文字写成。
[dialog]
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]这是阿戈尔人之间的事。
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=1)]
[name="大审判官"]只要你身在伊比利亚的国土上，律法便注视着你，我亦然。
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]哼......
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=1)]
[name="大审判官"]你与那三名深海猎人有什么联系？
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]你打伤过斯卡蒂，奇怪，她一定是打算避战的。
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=1)]
[name="大审判官"]......
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]她的血是特殊的，比我们所有人都特殊。希望你小心擦拭过你的武器了。
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=1)]。
[name="大审判官"]提问的是我。
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]决定是否回答的人是我。
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=1)]
[name="大审判官"]卡门阁下允许自由行动的猎人，似乎仅限于在盐风城之战中表明立场的阿戈尔人。
[Dialog]
[Character]
[CameraShake(duration=0.5, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_chixiaobadao", volume=0.7,delay=0.1)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.7)]
[delay(time=1.5)]
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]......嗯，碰得到她，看来不全是偶然。
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=1)]
[name="大审判官"]她并不弱。
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]......弱？
[name="乌尔比安"]不知轻重的评价。她只是对陆地感到生疏，欠缺变通的手段。
[Dialog]
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1")]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_chixiaobadao", volume=1)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.02, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.03, block=false)]
[characteraction(name="left", type="move", xpos=300, fadetime=0.5,block=false)]
[characteraction(name="right", type="move", xpos=50, fadetime=0.1,block=false)]
[CameraShake(duration=1, ystrength=4, vibrato=3, randomness=90, fadeout=false, block=false)]
[delay(time=1)]
[characteraction(name="right", type="jump", xpos=-80, power=7, times=2, fadetime=0.5, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$e_skill_skulsrsword", volume=0.5)]
[characteraction(name="left", type="jump", xpos=-400, power=5, times=1, fadetime=0.3,block=true)]
[dialog]
[Delay(time=1)]
[Character]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.03,block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
[Character(name="char_empty",name2="avg_npc_445_1#1$1")]
[Character(name="avg_4009_irene_1#1$1",blackstart=0.3,blackend=0.7,name2="avg_npc_445_1#1$1")]
[playsound(key="$d_avg_bldwhoosh")]
[characteraction(name="right", type="move", xpos=-200, fadetime=0,block=true)]
[characteraction(name="left", type="move", xpos=600, fadetime=0,block=true)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3,block=true)]
[Delay(time=0.6)]
[Character(name="avg_4009_irene_1#1$1",name2="avg_npc_445_1#1$1",focus=1)]
[name="？？？"]不要动，阿戈尔人。
[Character]
[Dialog]
[Character(name="avg_4009_irene_1#7$1",fadetime=1)]
[Delay(time=1)]
[name="审判官艾丽妮"]请配合长官的调查，深海猎人与审判庭缔结了契约，你的一举一动都在破坏我们建立的合作关系。
[Character(name="avg_npc_445_1#1$1")]
[name="乌尔比安"]......合作？
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]请三思。
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]审判官，伊比利亚有多少你这样的战士？
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=1)]
[name="大审判官"]与你无关。
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]够不够三千人？
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=1)]
[name="大审判官"]......
[Character(name="avg_npc_183#1",name2="avg_npc_445_1#1$1",focus=2)]
[name="乌尔比安"]那伊比利亚还不够格。
[Dialog]
[stopmusic(fadetime=3)]
[CameraShake(duration=0.5, xstrength=18, ystrength=16, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_183#1",name2="char_empty",fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_183#2",name2="char_empty",focus=1)]
[name="大审判官"]别想走！
[Dialog]
[Character]
[playMusic(intro="$suspenseful_intro", key="$suspenseful_loop",fadetime=2, volume=0.4)]
[Character(name="avg_npc_457_1#1$1",fadetime=0.5)]
[name="恐鱼"]（尖锐的摩擦声）
[Character(name="a

... (全文31376字符)
```

### level_act17side_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="27_g16_lighthouse_street",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.4,fadetime=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_451_1#7$1",fadetime=0.5)]
[Delay(time=1)]
[name="蒂亚戈"]哈......这些，恶心的地面，是怎么回事？
[name="蒂亚戈"]是这些恐鱼吗？
[Dialog]
[character]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_npc_449_1#1$1",fadetime=1)]
[Delay(time=1)]
[name="阿玛雅"]蒂亚戈。
[Character(name="avg_npc_451_1#6$1")]
[name="蒂亚戈"]......阿玛雅。
[Character(name="avg_npc_451_1#7$1",name2="avg_npc_449_1#1$1",focus=1)]
[name="蒂亚戈"]怎么回事？这些深海教徒，你不是说他们不会出现吗？他们把这里弄得一团糟......
[Character(name="avg_npc_451_1#7$1",name2="avg_npc_449_1#10$1",focus=2)]
[name="阿玛雅"]蒂亚戈，我是来道别的。
[Character(name="avg_npc_451_1#6$1",name2="avg_npc_449_1#10$1",focus=1)]
[name="蒂亚戈"]什么？
[Character(name="avg_npc_451_1#6$1",name2="avg_npc_449_1#10$1",focus=2)]
[name="阿玛雅"]时候差不多了，而现在机会难得，我只是这么觉得。
[Character(name="avg_npc_451_1#9$1",name2="avg_npc_449_1#10$1",focus=1)]
[name="蒂亚戈"]我不明白......
[Character(name="avg_npc_451_1#9$1",name2="avg_npc_449_1#8$1",focus=2)]
[name="阿玛雅"]蒂亚戈。
[name="阿玛雅"]审判官已经到了。足足三位。
[Character(name="avg_npc_451_1#6$1",name2="avg_npc_449_1#8$1",focus=1)]
[name="蒂亚戈"]——！
[Character(name="avg_npc_451_1#6$1",name2="avg_npc_449_1#4$1",focus=2)]
[name="阿玛雅"]乔迪在他们手上。
[Dialog]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=20, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_451_1#4$1")]
[Delay(time=1)]
[Character(name="avg_npc_451_1#4$1")]
[name="蒂亚戈"]唔——！
[Character(name="avg_npc_451_1#4$1",name2="avg_npc_449_1#10$1",focus=2)]
[name="阿玛雅"]别急，蒂亚戈。乔迪是以自己的意志回到的这里。三名审判官，你能做些什么？
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=20, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_451_1#5$1",name2="avg_npc_449_1#10$1",focus=1)]
[name="蒂亚戈"]他知不知道被审判庭发现意味着什么？！
[Character(name="avg_npc_451_1#5$1",name2="avg_npc_449_1#8$1",focus=2)]
[name="阿玛雅"]你说过很多次，我想他应该知道。
[name="阿玛雅"]但人就是这样。趋利避害只是逻辑推论得出的结果，人复杂得多，而这种复杂不能被轻易评判......我不会说乔迪愚蠢。
[Character(name="avg_npc_451_1#4$1",name2="avg_npc_449_1#8$1",focus=1)]
[name="蒂亚戈"]现在可不是当道德家的时候——！
[Character(name="avg_npc_451_1#4$1",name2="avg_npc_449_1#1$1",focus=2)]
[name="阿玛雅"]我们谈论的是性质，而非道德，蒂亚戈镇长。
[name="阿玛雅"]人之性具有美感。连时间都否定不了这一点。
[Character(name="avg_npc_451_1#9$1",name2="avg_npc_449_1#1$1",focus=1)]
[name="蒂亚戈"]......你到底要说什么？
[Character(name="avg_npc_451_1#9$1",name2="avg_npc_449_1#3$1",focus=2)]
[name="阿玛雅"]你憎恨审判庭吗？
[Character(name="avg_npc_451_1#2$1",name2="avg_npc_449_1#3$1",focus=1)]
[name="蒂亚戈"]......我......
[Character(name="avg_npc_451_1#2$1",name2="avg_npc_449_1#3$1",focus=2)]
[name="阿玛雅"]恐鱼确实遍布小镇，但是，蒂亚戈，回忆一下。
[name="阿玛雅"]那个雨夜，那些惩戒军，他们闯入镇上，撕碎房门。惨叫不绝于耳，盖过淅沥沥的雨点......
[Character(name="avg_npc_451_1#2$1",name2="avg_npc_449_1#3$1",focus=1)]
[name="蒂亚戈"]不，别说了......
[Character(name="avg_npc_451_1#2$1",name2="avg_npc_449_1#10$1",focus=2)]
[name="阿玛雅"]——现在呢？
[Character(name="avg_npc_451_1#2$1",name2="avg_npc_449_1#9$1",focus=2)]
[name="阿玛雅"]海的痕迹蔓延在这座小镇上——你听见惨叫了吗？你看到无理由的杀戮或狩猎了吗？
[name="阿玛雅"]没有。
[Character(name="avg_npc_451_1#2$1",name2="avg_npc_449_1#9$1",focus=1)]
[name="蒂亚戈"]......
[Character(name="avg_npc_451_1#2$1",name2="avg_npc_449_1#3$1",focus=2)]
[name="阿玛雅"]现在的格兰法洛——
[name="阿玛雅"]——徒留静谧而已。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Background(image="27_g24_cloudy_sea",xScale=1.1, yScale=1.1,screenadapt="coverall")]
[Delay(time=1)]
[backgroundTween(xFrom=0, xTo=-60, duration=20, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_sea")]
[CameraShake(duration=-1, xstrength=5, ystrength=2, vibrato=2, randomness=20, fadeout=true, block=false)]
[Character(name="avg_4042_lumen_1#1$1",fadetime=1)]
[Delay(time=1)]
[Character(name="avg_4042_lumen_1#8$1")]
[name="乔迪"]海洋原来，这么广阔......
[Character]
海风吹过。
乔迪不可置信地看着眼前的一切。他本以为海平线就是天空的终点。
直到亲眼确认这无限延伸的浪潮时——乔迪——这个阿戈尔人突然产生了一个疑惑。
[Character(name="avg_4042_lumen_1#1$1")]
[name="乔迪"]为什么人类从来没有过探索它的欲望呢......
[CameraShake(duration=2, xstrength=5, ystrength=2, vibrato=1, randomness=50, fadeout=true, block=false)]
[Character(name="avg_4042_lumen_1#1$1",name2="avg_4009_irene_1#1$1",focus=2)]
[name="审判官艾丽妮"]......除非星星是有规律的地图，或者双月能变成信号塔，否则我们怎么才能在这一片汪洋上确认方位？
[Character(name="avg_4042_lumen_1#7$1",name2="avg_4009_irene_1#1$1",focus=1)]
[name="乔迪"]呃，星星是没有规律的吗？
[Character(name="avg_4042_lumen_1#7$1",name2="avg_4009_irene_1#1$1",focus=2)]
[name="审判官艾丽妮"]去问专业的天文学家好了。
[Character(name="avg_4042_lumen_1#11$1",name2="avg_4009_irene_1#1$1",focus=1)]
[name="乔迪"]那如果......阿戈尔真的在海面以下，那阿戈尔究竟有多大......比伊比利亚还要大吗？
[Character(name="avg_4042_lumen_1#11$1",name2="avg_4009_irene_1#1$1",focus=2)]
[name="审判官艾丽妮"]那边有几个真正的阿戈尔人，你要不要去问问看？
[Dialog]
[Character]
[Character(name="avg_474_gladiia_1#1",fadetime=1)]
[Delay(time=1)]
[Character(fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_1023_ghost2_1#4$1",name2="char_263_skadi#3",fadetime=1)]
[Delay(time=1)]
[Character(fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_4042_lumen_1#1$1")]
[name="乔迪"]她们好像都有心事的样子，一脸严肃。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_sea")]
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]鲨鱼，你在听什么？
[Character(name="avg_1023_ghost2_1#4$1")]
[name="幽灵鲨"]......风。
[Character(name="avg_1023_ghost2_1#3$1")]
[name="幽灵鲨"]海风中夹杂着亲缘的馈赠，让我......很安心。
[Character(name="char_263_skadi#3")]
[name="斯卡蒂"]越接近海洋，她越是这样。
[Character(name="char_263_skadi#7")]
[name="斯卡蒂"]在盐风城的时候她明明......
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]......
[Character(name="avg_474_gladiia_1#1",name2="char_263_skadi#9",focus=2)]
[na

... (全文24527字符)
```

### level_act17side_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="27_g23_goldenboat_pass",screenadapt="coverall")]
[playMusic(intro="$nervous_intro", key="$nervous_loop",fadetime=3, volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$rungeneral", volume=0.6)]
[delay(time=1)]
[PlaySound(key="$d_avg_fish_howl")]
[Character(name="avg_npc_457_1#1$1",name2="avg_npc_457_1#1$1",fadetime=1)]
[delay(time=1.5)]
[Character(name="avg_4009_irene_1#4$1")]
[name="审判官艾丽妮"]啧，越往深处走，恐鱼的数量越多。
[Character(name="avg_4009_irene_1#4$1")]
[name="审判官艾丽妮"]如果不能快些会合......会很危险。
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]......
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]老师......我要怎么......才能像她们一样......
[Dialog]
[character(fadetime=0)]
[delay(time=2)]
[dialog]
[character(name="char_empty")]
[characteraction(name="middle", type="move", ypos=300, fadetime=0,block=true)]
[Character(name="avg_npc_452_1#1$1",fadetime=0.4)]
[characteraction(name="middle", type="move", ypos=-300, fadetime=0.4,block=true)]
[CameraShake(duration=1, xstrength=10, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[delay(time=1)]
[name="？？？"]......嘎......
[Character(name="avg_4009_irene_1#2$1")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="审判官艾丽妮"]海嗣......？！
[Character(name="avg_4009_irene_1#2$1")]
[name="审判官艾丽妮"]（是在甲板上见到的那只，那个猎人的一击居然没对它造成一点伤害......？！）
[Character(name="avg_npc_452_1#1$1")]
[name="？？？"]......
[Character(name="avg_4009_irene_1#2$1")]
[name="审判官艾丽妮"]（......会怎么攻击？四肢？啃咬？）
[Character(name="avg_4009_irene_1#4$1")]
[name="审判官艾丽妮"]（不，手炮，我必须拉开距离，我——）
[Character(name="avg_npc_452_1#1$1")]
[name="？？？"]......
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]......等等。
[Character(name="avg_4009_irene_1#2$1")]
[name="审判官艾丽妮"]等等，等等！你腰间的，你挂着什么？！
[Character(name="avg_4009_irene_1#2$1")]
[name="审判官艾丽妮"]你为什么会......你难道是......！
[Character(name="avg_npc_452_1#1$1")]
[name="？？？"]嗷啊啊啊啊——！
[dialog]
[character]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.4)]
[PlaySound(key="$d_avg_attack_heavy", volume=1)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[character]
[CameraShake(duration=0.1, xstrength=0, ystrength=0, vibrato=0, randomness=0, fadeout=true, block=true)]
[character(name="char_empty")]
[characteraction(name="middle", type="move",xpos=-200,fadetime=0, block=true)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$swordtsing1", volume=1)]
[PlaySound(key="$d_avg_clothmovement", volume=0.9)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_4009_irene_1#4$1",fadetime=0.5)]
[characteraction(name="middle", type="move",xpos=300, fadetime=0.7, block=true)]
[delay(time=1.5)]
[name="审判官艾丽妮"]呃！咳咳——咳咳——
[name="审判官艾丽妮"]（这个力度——！幸好挡下了——！）
[character(fadetime=0)]
[Character(name="avg_npc_452_1#1$1")]
[name="？？？"]......伊......
[name="？？？"]......
[Character(name="avg_4009_irene_1#4$1")]
[name="审判官艾丽妮"]你想说什么吗？怪物！
[Character(name="avg_4009_irene_1#4$1")]
[name="审判官艾丽妮"]我不会......也不可以在这里倒下！
[Character(name="avg_4009_irene_1#4$1")]
[name="审判官艾丽妮"]我是，伊比利亚的审判官！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g19_lighthouse_front",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_183")]
[name="大审判官达里奥"]......咳。
[Character(name="avg_npc_183")]
[name="大审判官达里奥"]烧毁溟痕花费了太多时间。
[Character(name="avg_npc_183")]
[name="大审判官达里奥"]......并不乐观。
[dialog]
[character(fadetime=0)]
[PlaySound(key="$d_avg_fish_howl")]
[Character(name="avg_npc_457_1#1$1",name2="avg_npc_457_1#1$1",fadetime=1)]
[delay(time=1.5)]
[name="恐鱼"]（成群的窸窣声）
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g20_lighthouse_core",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_4042_lumen_1#7$1")]
[name="乔迪"]（从这里可以看见下面的情况......）
[Character(name="avg_4042_lumen_1#10$1")]
[name="乔迪"]已经几个小时了？大审判官阁下......还能坚持得住吗？
[Character(name="avg_4042_lumen_1#7$1")]
[name="乔迪"]我......如果我......不，别想这些，乔迪，注意力集中点！
[Character(name="avg_4042_lumen_1#7$1")]
[name="乔迪"]审判庭......快啊......
[Dialog]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[character(fadetime=0)]
[Background(image="27_g22_goldenboat_hall",screenadapt="coverall")]
[PlayMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.8, crossfade=1, delay=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[Character(name="avg_1023_ghost2_1#1$1")]
[Character(fadetime=0)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[PlaySound(key="$e_atk_saw_n_1", volume=0.5)]
[PlaySound(key="$e_atk_saw_n_1", volume=1)]
[PlaySound(key="$e_atk_saw_n_2", volume=1)]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[Character(name="avg_npc_458_1#1$1")]
[delay(time=0.51)]
[PlaySound(key="$d_avg_fish_howl")]
[character(fadetime=1)]
[delay(time=1)]
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]怎么了，就这样而已？
[Character(name="avg_npc_458_1#1$1")]
[name="海嗣"]......嘎......嗷......
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]听啊，你的同伙们已经在发出哀嚎。盐风城的那朵小花至少有些美感，可你呢？
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]作为睡醒后的第一堂舞蹈课，实在乏味。
[Character(name="avg_npc_458_1#1$1")]
[name="海嗣"]嘎......！
[dialog]

... (全文21607字符)
```

### level_act17side_st07

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Character(fadetime=0)]
[PlayMusic(intro="$plot_intro", key="$plot_loop", volume=0.8, crossfade=1, delay=0.5)]
[Background(screenadapt="coverall", image="bg_ibbar", width=1, height=1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[Delay(time=0.8)]
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]啊，你回来了。
[dialog]
[character(fadetime=0)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_461_1#1$1",fadetime=1)]
[delay(time=1)]
[name="冷静的镇民"]......
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_461_1#1$1",focus=1)]
[name="古怪的教徒"]感谢你的付出，我知道，对于你而言，违背信仰仍然是一件痛苦的事情。
[name="古怪的教徒"]但是美好就在前方。这绝非虚妄的允诺，而是实际的救赎。
[name="古怪的教徒"]感谢你。
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_461_1#1$1",focus=2)]
[name="冷静的镇民"]卡门阁下深不可测，欺骗他没有多大意义。他很快就会发现真相。
[name="冷静的镇民"]你也该谢谢蒂亚戈。我们撒这个谎，意味着他一定会死，死在审判庭手里。
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_461_1#1$1",focus=1)]
[name="古怪的教徒"]......我没见过海洋的使者，但传言，使者不会拒绝同族的要求。
[name="古怪的教徒"]因为同族的选择一定有利于族群，同族的想法一定是族群的想法。我们应当学习，这也是其中一环。
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_461_1#1$1",focus=2)]
[name="冷静的镇民"]那就让蒂亚戈自己去愁吧。
[name="冷静的镇民"]但是......
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_461_1#1$1",focus=1)]
[name="古怪的教徒"]啊，你在担心。没必要。
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_461_1#1$1",focus=2)]
[name="冷静的镇民"]我们的先知，阿玛雅小姐，她真的还能回来吗？
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_461_1#1$1",focus=1)]
[name="古怪的教徒"]她只是选择先我们一步回归海洋，为了寻找道途、使者，和沉睡城市的踪迹。
[name="古怪的教徒"]她回来，是为了接济同胞，她一去不返，也只是为了未来做着准备。
[name="古怪的教徒"]我们不必为她担心，我们只要知道，阿玛雅小姐不希望审判庭过多地关注到她，无论她身在何方。
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_461_1#1$1",focus=2)]
[name="冷静的镇民"]......那这个人，伊比利亚人，我们抓来做什么？
[Character(name="avg_npc_450_1#3$1")]
[name="极境"]......
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]他的女主人似乎和那位卡门达成了某种协议。他是敌人。
[Character(name="avg_npc_450_1#4$1")]
[name="极境"]哈哈......真希望你别用这样的称呼描述我和医生的关系。
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]你一直在调查我们，不是吗？
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]我花费了不少时间，向你阐述我们的真理，我们不想伤害你。你想明白了吗？
[Character(name="avg_npc_450_1#1$1")]
[name="极境"]我想我对你们的伪善已经很明白了，不需要多说啦。
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]......伪善？哦......你还在谈论道德，人世的道德。
[Character(name="avg_npc_450_1#1$1")]
[name="极境"]先不论海嗣恐鱼这些玩意究竟算什么，我看到的是一群对伊比利亚和审判庭心存不满，然后找了各种借口想要加害审判庭的坏家伙。
[Character(name="avg_npc_450_1#1$1")]
[name="极境"]我是个伊比利亚人，虽然我在伊比利亚生活的时间不算特别长......
[Character(name="avg_npc_450_1#1$1")]
[name="极境"]可我去过很多地方，见过很多事情，你们这样的人其实很多，还总觉得自己特别。
[Character(name="avg_npc_450_1#1$1")]
[name="极境"]如果你们说的神是真的，就，呃，什么进化的崇高，生命的极致——
[Character(name="avg_npc_450_1#1$1")]
[name="极境"]——那你们的神一定对你们这样的人不屑一顾吧？
[Character(name="avg_npc_461_1#1$1")]
[name="冷静的镇民"]你——！
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]......不，你说得对。所以使者断绝了联系，只有先知阿玛雅能够听见海的言语，向我们传达指令。
[Character(name="avg_npc_450_1#9$1")]
[name="极境"]（阿玛雅果然有问题......啧，怎么就没早点抓到证据呢。）
[Character(name="avg_npc_450_1#9$1")]
[name="极境"]（不过......）
[dialog]
[character(fadetime=0)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_451_1#1$1",fadetime=1)]
[delay(time=1)]
[name="蒂亚戈"]......
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_451_1#1$1",focus=1)]
[name="古怪的教徒"]......情况怎么样？
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]你们的那些，溟痕，根本靠近不了城镇的核心区域。
[name="蒂亚戈"]那只黑色的怪物不仅会飞，还会喷吐可怕的热流，溟痕蔓延的速度完全赶不上它烧毁的速度。
[name="蒂亚戈"]再拖下去，等那些阻拦惩戒军的恐鱼全军覆没，格兰法洛就会落入审判庭的手里。
[name="蒂亚戈"]我们都会死。
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_451_1#1$1",focus=1)]
[name="古怪的教徒"]不，蒂亚戈，不。
[name="古怪的教徒"]你在谈论那些......为了拖延敌人脚步而自愿牺牲的同胞时，你并不悲伤。
[name="古怪的教徒"]换言之，你也没做好随时为族群牺牲的准备。
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]别这样和我说话，我们只是利害一致。我对拥抱海洋不感兴趣，我已经是一把老骨头了。
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_451_1#1$1",focus=1)]
[name="古怪的教徒"]......冥顽不化的低级生物......
[Character(name="avg_npc_453_1#1$1",name2="avg_npc_451_1#1$1",focus=2)]
[name="蒂亚戈"]彼此。
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]至于你，年轻人，我早说了，你别多管闲事。
[Character(name="avg_npc_450_1#5$1")]
[name="极境"]蒂亚戈，你......
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]你们互相认识？
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]......
[Character(name="avg_npc_450_1#1$1")]
[name="极境"]呃......
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]不。只是有一个总坐在礼拜堂的外乡人，我身为这里的镇长，总有印象的。
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]你不该多管闲事。
[Character(name="avg_npc_450_1#11$1")]
[name="极境"]......
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]好了。
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]我们也该有所动作了吧？难道要等着审判官和他那个带着怪物的同谋把我的小镇烧个精光？
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]不会。你真是执着于这个小镇，为什么？
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]格兰法洛是我们几代人重建伊比利亚愿景的缩影，异教徒，你问问那些加入你们的本地人，你会明白的。
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]审判庭毁了足够多的东西，我要他们加倍偿还。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[character(fadetime=0)]
[Background(image="27_g22_goldenboat_hall",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop",fadetime=3, volume=0.8)]
[Character(name="char_263_skadi#2")]
[name="斯卡蒂"]我是斯卡蒂，不是伊莎玛拉。
[Character(name="avg_npc_446_1#1$1")]
[name="船长阿方索"]那伊莎玛拉这个发音意味着什么？
[Character(name="char_263_skadi#9")]
[name="斯卡蒂"]我......
斯卡蒂知道，斯卡蒂不敢回答。
歌蕾蒂娅告诉过她没事，她愿意相信。
但这只是一种逃避。她知道这个称呼意味着什么。
意味着深渊里的巨响。血肉摩擦着岩壁下坠，唯有意志攀高直上，冲破海洋。
意味着那场鏖战之后，留在了自己体内的某些，“东西”。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Background(image="bg_ibcave",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_186")]
[name="海嗣"]我的血与你的血相同。
[name="海嗣"]你闻到我们气味，正如我们闻见你气味。
[name="海嗣"]你们找到我们，杀死我们......
[name="海嗣"]我们不懂时，我们也杀死你们。
[name="海嗣"]我们喂养海洋。我们的尸体供养了海洋。
[name="海嗣"]Ishar-mla，我们拥有同个故乡。
[Dialog]
[Block

... (全文14416字符)
```

### level_act17side_st08

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g23_goldenboat_pass",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1, delay=0.5)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_474_gladiia_1#5",fadetime=1)]
[delay(time=1)]
[name="歌蕾蒂娅"]......
[dialog]
[ShowItem(image="item_act27_1", fadestyle="horiz_expand_center", fadetime=0.5, offsetx=0, width=200)]
[delay(time=1)]
[hideitem]
[delay(time=1)]
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]这里。
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]（他引我来到这里，随后隐去了气味。看来他在陆地上学会了不少手段。）
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]......
[character]
歌蕾蒂娅环顾四周。
她知道，有一个曾经的友人就在这附近盯着她。
但她没有犹豫，也没有时间犹豫。她必须尽快得到关于这艘船的全部秘密，她必须......带着这些秘密，重回阿戈尔。
她想回到家园。她想帮助自己的家园，对抗灾祸。
歌蕾蒂娅看着手里的钥匙。
她打开了宝库的大门。
[PlaySound(key="$d_gen_dooropen")]
[Dialog]
[delay(time=2)]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g16_lighthouse_street",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$plot_intro", key="$plot_loop", volume=0.8, crossfade=1, delay=0.5)]
[PlaySound(key="$burningloop1",loop=true, channel="fire")]
[delay(time=1)]
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]焚烧这些溟痕很费功夫，我真该谢谢凯尔希和那只漆黑的生物。
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]溟痕吞噬不掉这片礁石。很遗憾。
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]但这也只是万千形态中的一种，你没有听过预言，你不会理解。
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]预言？不过是未知生物的信徒，一群逃避者，难道还需要未来？
[stopSound(channel="fire",fadetime=4)]
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]先知与你们不同。她从不描述虚伪的未来，从不做无法实践的许诺。
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]她只说，只说千万片巨鳞将汇成一体，飞向深空。只说大海将被光芒涂抹，此消彼长，永不干涸。
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]只说生命的死亡和消逝都将融为一体，届时，连这片虚假的群星都遮蔽不住生命的光芒。
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]我们将生存在那样一个生态中。我们皆是壮美循环的一部分。生命诞生，生命奉献，生命寻求价值，生命消逝，周而复始。
[Character(name="avg_npc_447_1#7$1")]
[name="圣徒卡门"]听上去，不过是某种源石技艺给你们看到的幻觉罢了。
[Character(name="avg_npc_447_1#7$1")]
[name="圣徒卡门"]将伊比利亚逼到如此境地，数百万生灵涂炭，这也是壮美循环的一部分吗？
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]你理解什么？！族群从不将个体的死当做“结束”，生命在结束后仍属于壮美循环的一部分！
[Character(name="avg_npc_447_1#1$1")]
[name="圣徒卡门"]你愤怒，你焦躁，你还只是个人类啊，异端。
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]......我不会被你抓住，审判官。我知道你的源石技艺，可恨的法术。我们都做好了奉献的准备。
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]你将永远无法触及先知，就像你抓不住时间，时间从你的指尖流逝！
[dialog]
[character(fadetime=0)]
[PlaySound(key="$d_avg_fish_howl")]
[Character(name="avg_npc_457_1#1$1",name2="avg_npc_457_1#1$1",fadetime=1)]
[delay(time=2)]
[Character(name="avg_npc_453_1#1$1")]
[name="古怪的教徒"]大审判官！格兰法洛的所有人都对你们积怨已久！惩戒军靠近不了这里，现在你孤身一人！
[name="古怪的教徒"]你逃不掉的！
[Character(name="avg_npc_447_1#2$1")]
[name="圣徒卡门"]......逃？
[Character(name="avg_npc_447_1#6$1")]
[name="圣徒卡门"]我们在这里，难道是为了费口舌争辩，正义与邪恶的吗？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(fadetime=0)]
[Background(screenadapt="coverall", image="bg_ibbar", width=1, height=1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[Delay(time=0.8)]
[Character(name="avg_npc_450_1#10$1")]
[name="极境"]哈啊......哈啊......
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]他什么都不说，愚蠢的伊比利亚人......
[name="负责拷问的教徒"]那只黑色怪物一定有弱点，它坚硬无比，还能轻易烧毁溟痕......它究竟是什么？！
[name="负责拷问的教徒"]如果再不得到些情报，等惩戒军突破了包围网，我们就——
[Character(name="avg_npc_450_1#1$1")]
[name="极境"]——就失败了？
[Character(name="avg_npc_450_1#1$1")]
[name="极境"]哈哈......就凭你们是对付不了凯尔希医生和那位审判官阁下的。你们已经输了。
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]住口！
[name="负责拷问的教徒"]我要把你——等等，你在做什么？！
[name="负责拷问的教徒"]你的杖为什么有动静！？你做了什么？
[Character(name="avg_npc_450_1#1$1")]
[name="极境"]你们似乎太关注你们的海洋动物了......哦，你们是不是都不懂什么叫“源石技艺”？
[Character(name="avg_npc_450_1#1$1")]
[name="极境"]太脱离现实生活可不好——
[dialog]
[Character(name="avg_npc_450_1#10$1")]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="极境"]咕哈——
[Character(name="avg_npc_453_1#1$1")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="负责拷问的教徒"]自以为是的家伙——！你以为我们什么都没准备？为了把你们这些和审判庭同流合污的人一网打尽，我们筹备了多久！
[character(fadetime=0)]
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_451_1#7$1",fadetime=1)]
[delay(time=1)]
[name="蒂亚戈"]别相信他的故弄玄虚，他在这个小镇躲藏了几个月，他是个间谍，精通通讯手段的间谍。
[Character(name="avg_npc_451_1#7$1")]
[name="蒂亚戈"]也许我们的位置已经暴露了。
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]......间谍，间谍，我们之中一定早就潜伏了审判庭的间谍！
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]我知道你们的存在，是因为你们不加掩饰，我和阿玛雅走得很近。但审判庭不同，他们确实怀着恶意对待格兰法洛，如果他们想藏......
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]我们毕竟只是世代为工的工人，我们怎么发现呢？
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]那就把他丢出去喂给同胞们吧。溟痕蔓延的速度在减缓，我们需要更多养分，阻拦惩戒军。
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]然后，我们也应当想办法离开。
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]好。我来带路，没有人比我更熟悉格兰法洛，过去我们留下了不少暗道和地下仓库......
[Character(name="avg_npc_450_1#2$1")]
[name="极境"]蒂亚戈，你不该这么做。
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]我们才认识多久？你来教我怎么做，空喊口号的卫道士？
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]站起来，走，你会变成海的一部分。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[character(fadetime=0)]
[Background(image="27_g25_goldenboat_core",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.8, crossfade=1, delay=0.5)]
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]（原来如此。）
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]（源石能源与阿戈尔科技的结合，更坚固的穹顶，陆地移动城市的应用模式，源石技艺的拓展性。）
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]（这就是科学院的天才眼中的大地。几十年时间，足够他做到这些......）
[Character(n

... (全文18483字符)
```

### level_act17side_st09

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g16_lighthouse_street",screenadapt="coverall")]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_451_1#4$1")]
[name="蒂亚戈"]走快点！
[Character(name="avg_npc_450_1#12$1")]
[name="极境"]呃......
[Character(name="avg_npc_451_1#9$1")]
[name="蒂亚戈"]......这些，溟痕。它们究竟是什么？
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]尽管微小，形式不同，但这些荧光的生命也是我们同胞的延展。
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]先知曾说，在海洋的某个部分，发光的生命已经充斥了整个海域。它们即是整体，它们为所有同胞塑造生命的摇篮。
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]“溟痕”......只不过是遥远的数千数万海里外的“祂”随波而来的些许意志。哪怕只有一丁点，也确确实实在蚕食陆地。
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]溟痕会将陆地化为另一种海洋。
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]......是啊。
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]伊比利亚是你们计划的第一个牺牲品，格兰法洛也是。
[Character(name="avg_npc_450_1#5$1")]
[name="极境"]......！
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]......牺牲品？你是不是，用错了词？
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]没有。
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]审判庭会夺走这座小镇，看看这些“美丽”的溟痕，它们一样会。
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]这里不再是我们的家。不再与那段如火的岁月有瓜葛。
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]蒂亚戈，你不该——
[Character(name="avg_npc_451_1#1$1")]
[name="蒂亚戈"]乔迪也被带走了......那些逃走的人此刻应该都被惩戒军抓起来了吧。
[Character(name="avg_npc_451_1#7$1")]
[name="蒂亚戈"]你们都是凶手。
[dialog]
[character]
[Character(name="npc_10002",fadetime=0.5)]
[delay(time=1)]
[PlaySound(key="$Mon3tr_n")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="Mon3tr"]——（激动的尖啸）
[Character(name="avg_npc_450_1#5$1")]
[name="极境"]Mon3tr——？！
[Character(name="avg_npc_453_1#1$1")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="负责拷问的教徒"]它怎么会在这里？！不可能！它明明在城镇的西边——！
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]你骗了我们，蒂亚戈！
[Character(name="avg_npc_451_1#7$1")]
[name="蒂亚戈"]......
[Character(name="avg_npc_453_1#1$1")]
[name="负责拷问的教徒"]还有你也是？！
[dialog]
[character]
[Character(name="avg_npc_461_1#1$1",fadetime=1)]
[delay(time=1)]
[name="冷静的镇民"]......在成为审判庭的卧底之前，我只是一名格兰法洛工人的女儿。
[Character(name="avg_npc_461_1#1$1")]
[name="冷静的镇民"]别小看我们的恨意。忍辱负重，只是为了让你们一同灭亡。
[Character(name="avg_npc_451_1#7$1")]
[name="蒂亚戈"]审判庭也好，你们也好，都只是践踏了我们家园的敌人。
[Character(name="avg_npc_451_1#7$1")]
[name="蒂亚戈"]来看看毁灭的模样吧，看看我们当年所看见的。
[Character(name="avg_npc_450_1#7$1")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="极境"]蒂亚戈——！躲开！
[Character(name="avg_npc_451_1#6$1")]
[name="蒂亚戈"]唔！
[Dialog]
[character]
[Character(name="char_empty",name2="avg_npc_451_1#6$1")]
[characteraction(name="left", type="move", xpos=-400, power=0, times=1, fadetime=0, block=true)]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="left", type="move", xpos=400, power=0, times=1, fadetime=1, block=true)]
[Character(name="avg_npc_450_1#7$1",name2="avg_npc_451_1#6$1",focus=1,fadetime=0.51)]
[characteraction(name="left", type="jump", xpos=100, power=0, times=1, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral",volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[characteraction(name="left", type="jump", xpos=-100, power=5, times=1, fadetime=1,block=true)]
[characteraction(name="right", type="move", xpos=300, power=0, times=1, fadetime=1, block=true)]
[Character(fadetime=0.5)]
[dialog]
[Delay(time=1)]
[Character(name="npc_10002")]
[PlaySound(key="$Mon3tr_n")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="Mon3tr"]（尖啸）
[dialog]
[character(fadetime=0)]
[Blocker(a=1,r=1, g=1, b=1,  fadetime=0.1, block=true)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$p_skill_Mon3trburst")]
[PlaySound(key="$d_sp_ballista")]
[PlaySound(key="$d_avg_rockfall", volume=1)]
[CameraShake(stop=true)]
[Blocker(a=0,r=0, g=0, a=0, fadetime=2, block=false)]
[delay(time=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g20_lighthouse_core",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_4042_lumen_1#7$1")]
[name="乔迪"]......已经没有还能操作的地方了。剩下的，能源都......
[Character(name="avg_4042_lumen_1#7$1")]
[name="乔迪"]最后，就看这座灯塔，还能坚持多久了。
[Character(name="avg_4042_lumen_1#9$1")]
[name="乔迪"]（溟痕，已经，爬到这一层了？）
[Character(name="avg_4042_lumen_1#9$1")]
[name="乔迪"]我得再往上走......
[name="乔迪"]大审判官阁下......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g19_lighthouse_front",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_183#3")]
[name="大审判官达里奥"]......
手臂发麻。
礁石的形状与排布已经发生了极大的变化。审判官不留余力，尽可能歼灭进入视野的敌人。
但敌人如字面意义上无穷无尽。
剑已锈蚀，卷匣中的炸药也已消耗殆尽。
只有提灯中的火焰，比先前还要旺盛。
达里奥没有一次看向身后，看向他始终捍卫的高塔。
他看着海平面的彼方。
[Character(name="avg_npc_183#3")]
[name="大审判官达里奥"]......海洋的生物，伊比利亚不会被你们毁灭。
[Character(name="avg_npc_183#3")]
[name="大审判官达里奥"]人类不会被你们毁灭。
他咳出了卡在喉咙里的鲜血。血腥味充满鼻腔。
[Character(name="avg_npc_457_1#1$1")]
[PlaySound(key="$d_avg_fish_howl")]
[name="恐鱼"]（缓慢的窸窣声）
[Character(name="avg_npc_183#3")]
[name="大审判官达里奥"]我，也不会，被毁灭。只是死亡而已。
[dialog]
[character(fadetime=0)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[CameraShake(duration=0.5, xstrength=8,

... (全文13643字符)
```

### level_act17side_st10

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g25_goldenboat_core",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$plot_intro", key="$plot_loop", volume=0.8)]
[dialog]
[character(fadetime=0)]
[PlaySound(key="$d_avg_footstep_stonestep", volume=0.6)]
[Character(name="avg_npc_448_1#1$1",fadetime=2)]
[delay(time=3)]
[Character(name="avg_npc_445_1#1$1")]
[name="乌尔比安"]你浪费了机会。
[Character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]什么？
[Character(name="avg_npc_445_1#1$1")]
[name="乌尔比安"]如果是我，在盐风城抓住那只会说话的海嗣时，我会逼迫它说出它所知的关于阿戈尔的全部。
[Character(name="avg_npc_445_1#1$1")]
[name="乌尔比安"]你在陆地上行走了数年。你从未听见过阿戈尔的讯息。但海洋不同，海洋从未断绝过联系。
[Character(name="avg_npc_445_1#1$1")]
[name="乌尔比安"]你就这么放任它死去，没有创造任何价值。低效的决策，歌蕾蒂娅。
[Character(name="avg_474_gladiia_1#2")]
[name="歌蕾蒂娅"]垃圾的讯息，我不需要。猎物给出的答案充斥着下级思维。
[Character(name="avg_npc_445_1#1$1")]
[name="乌尔比安"]看来你在陆地上找到了帮手，并倾注了相当的信任。
[character]
[Dialog]
[Character(name="avg_npc_448_1#1$1")]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[PlaySound(key="$d_avg_attack_heavy")]
[PlaySound(key="$d_sp_ballista", volume=0.4)]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
[character]
[character(name="char_empty")]
[characteraction(name="middle", type="move",xpos=-200,fadetime=0, block=true)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$swordtsing1", volume=1)]
[PlaySound(key="$d_avg_clothmovement", volume=0.9)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_474_gladiia_1#2",fadetime=0.5)]
[characteraction(name="middle", type="move",xpos=300, fadetime=0.7, block=true)]
[delay(time=1)]
[character]
[character(name="char_empty")]
[characteraction(name="middle", type="move",xpos=200,fadetime=0, block=true)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$swordtsing1", volume=1)]
[PlaySound(key="$d_avg_clothmovement", volume=0.9)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_445_1#1$1",fadetime=0.5)]
[characteraction(name="middle", type="move",xpos=-300, fadetime=0.7, block=true)]
[delay(time=2.5)]
[Character(name="avg_npc_448_1#1$1")]
[PlaySound(key="$d_gen_walk_n")]
[name="最后的骑士"]（尖啸）群星......墓地......
[Character(name="avg_npc_445_1#1$1")]
[name="乌尔比安"]你手下留情了。他怎么还站着？
[Character(name="avg_474_gladiia_1#2")]
[name="歌蕾蒂娅"]......不。
[Character(name="avg_474_gladiia_1#2")]
[name="歌蕾蒂娅"]他只是比我想象中要更结实一些。
[Character(name="avg_npc_448_1#1$1")]
[name="最后的骑士"]......
骑士没有还击。他突然呆立在原地，随后抬头，蹒跚着，盘旋着，看着上方。
歌蕾蒂娅本打算乘机结束这场追逐，但下一刻，她同样产生了一股隐隐的预感。
[Character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]......海嗣的气味，在变化。
[Character(name="avg_npc_445_1#1$1")]
[name="乌尔比安"]你已经敏锐到能捕捉到它们的变化了吗？
[Character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]......
[Character(name="avg_npc_445_1#1$1")]
[name="乌尔比安"]这就对了，歌蕾蒂娅。
[Character(name="avg_npc_445_1#1$1")]
[name="乌尔比安"]无论你怎么安慰其他人和你自己，这才是我们迟早要面对的难题——我们自己。
[Dialog]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g23_goldenboat_pass",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$batmeeting_intro", key="$batmeeting_loop", volume=0.8)]
[Character(name="avg_npc_446_1#6$1")]
[name="船长阿方索"]......加西亚！
[Character(name="avg_npc_452_1#1$1")]
[name="大副"]（呜咽般的鸣叫）
[Character(name="avg_npc_446_1#9$1")]
[name="船长阿方索"]好......好......你让它受了重伤！我们顺着血迹找，我们很快就会回来。
[Character(name="avg_npc_446_1#4$1")]
[name="船长阿方索"]等等，这些烧毁的痕迹是什么？它对我的船做了什么？！
[Character(name="char_263_skadi#8")]
[name="斯卡蒂"]......这不可能是那个怪物留下的痕迹。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]说得对。这是我们可爱的伊比利亚小鸟留下的，多稀奇呀，在这短短的时间里，她能成长到这样的地步。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]海嗣和这样的人谁比较可怕呢？
[Character(name="avg_npc_446_1#4$1")]
[name="船长阿方索"]......那个旧伊比利亚人？她？不可能，这艘船上随便一个身经百战的水手都比她要强。她怎么能做到？
[Character(name="avg_npc_452_1#1$1")]
[name="大副"]（轻咬船长的袖子）
[Character(name="avg_npc_446_1#2$1")]
[name="船长阿方索"]......我知道了。
[Character(name="avg_npc_446_1#1$1")]
[name="船长阿方索"]无论......无论那个旧伊比利亚人做了什么，我们都得抓紧。
[Character(name="avg_npc_446_1#1$1")]
[name="船长阿方索"]该结束这场持续数月的狩猎了。
[Character(name="avg_1023_ghost2_1#7$1")]
[name="幽灵鲨"]您看上去有些高兴，船长先生。
[Character(name="avg_npc_446_1#9$1")]
[name="船长阿方索"]高兴？哈！
[Character(name="avg_npc_446_1#9$1")]
[name="船长阿方索"]漫长的狩猎迎来了结局，谁会不高兴？
[Character(name="avg_npc_446_1#1$1")]
[name="船长阿方索"]你们继续追，我走另一条路。它凿不穿这里的墙壁......它会去更接近海的地方。
[Character(name="avg_npc_446_1#10$1")]
[name="船长阿方索"]加西亚......你的伤并不致命，坚强点，我们很快回来！
[Character(name="avg_npc_452_1#1$1")]
[name="大副"]......
负伤的大副还需要时间恢复。它默默看着船长的脸。
欣喜。难以掩饰的兴奋。还有久违的活力。
它放心地小睡片刻，集中精力恢复受伤的部分，以便帮助自己的爱人继续狩猎。
[stopmusic(fadetime=3)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
那是一个小小的梦境。短暂，恍惚，在肉体遭受巨大变化之后，这种情况就显得尤为少见。
梦里，是伊比利亚的海岸。漫天的礼花和轰鸣的汽笛。意气风发的阿方索站在它的身旁，问了它一个问题。
加西亚。
看见岸边的那些孩子了吗？我们都很喜欢孩子。
孩子是伊比利亚的未来。我们的荣誉，战功，一身本领，都会随着生命消亡。
但是，孩子，新的生命，伊比利亚共同养育的生命，会继承这一切。
加西亚。
你觉得他该戴你我的哪顶帽子？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g22_goldenboat_hall",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.8)]
[PlaySound(key="$rungeneral", volume=0.9)]
[Character(name="avg_4009_irene_1#4$1")]
[name="审判官艾丽妮"]（受了伤还能这么迅速地移动......追不上它！）
[Character(name="avg_4009_irene_1#4$1")]
[name="审判官艾丽妮"]（而且......勉强激发手炮......稍微有些......）
[Character(name="avg_4009_irene_1#4$1

... (全文21092字符)
```

### level_act17side_st11

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g22_goldenboat_hall",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.8, crossfade=1, delay=0.5)]
[Character(name="avg_npc_449_1#4$1")]
[name="阿玛雅"]你想起了我们是如何相遇的吗？劳伦缇娜？
[Character(name="avg_npc_449_1#4$1")]
[name="阿玛雅"]在那片如雪的沙滩上，你，身负重伤，像是一位睡美人那样躺在礁石上。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]顺着洋流漂泊了那么远，最后唤醒我的竟然还是散发着腐朽气味的陆地人，我多希望能一直睡下去。
[Character(name="avg_npc_449_1#6$1")]
[name="阿玛雅"]怎么会呢？我记得，初次见面的时候，我们互相留下的印象不是挺好的吗？
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]我不否认，不然你已经像昆图斯一样，从头到脚被区分成很多个部分了。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]真遗憾，盐风城那会，我怎么没今天这个状态？不然我就有更多精力和他好好叙旧啦。
[Character(name="avg_npc_449_1#6$1")]
[name="阿玛雅"]......
阿玛雅仍旧保持着优雅的姿势。她目光所及，溟痕随之蔓延。
但劳伦缇娜根本没有把她放在眼里。
她在看什么？
[Character(name="avg_npc_449_1#5$1")]
[name="阿玛雅"]......你似乎恢复得很好。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]托您的福。另外一位呢？他还好吗？
[Character(name="avg_npc_449_1#10$1")]
[name="阿玛雅"]谁知道呢，也许和昆图斯一样，都死在猎人手里了吧。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]......哪个猎人？
[Character(name="avg_npc_449_1#6$1")]
[name="阿玛雅"]随口一说。
[dialog]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$p_skill_spiritexplo", volume=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[Character(name="avg_1023_ghost2_1#5$1")]
[name="幽灵鲨"]源石技艺。的确，如果说陆地上还有什么能对猎人们造成威胁，大概就是所谓的“法术”了吧。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]不过，你似乎不太擅长用法术厮杀。不觉得太可怜了吗？
[Character(name="avg_npc_449_1#1$1")]
[name="阿玛雅"]劳伦缇娜，你就没有想过，为什么你的意识忽而清醒，忽而模糊，为什么你体内被注射了那般浓度的精炼液化源石，却依旧能够扛住？
[dialog]
[Character(name="avg_1023_ghost2_1#7$1")]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_atk_saw_n_1", volume=1)]
[PlaySound(key="$e_atk_saw_n_1", volume=1)]
[PlaySound(key="$e_atk_saw_n_2", volume=1)]
[PlaySound(key="$d_avg_attack_heavy")]
[PlaySound(key="$d_sp_ballista", volume=0.4)]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
[Character(name="avg_1023_ghost2_1#7$1")]
[name="幽灵鲨"]不是因为我比较结实吗？
[Character(name="avg_npc_449_1#11$1")]
[name="阿玛雅"]你还和我谈论过你的舞蹈课呢。
[Character(name="avg_1023_ghost2_1#5$1")]
[name="幽灵鲨"]......唉，真该死。在我自己想起来之前，竟然是你先告诉我的。
[Character(name="avg_1023_ghost2_1#6$1")]
[name="幽灵鲨"]好，舞蹈课。然后呢，我还对你说了什么，阿玛雅？
[Character(name="avg_npc_449_1#11$1")]
[name="阿玛雅"]别扯开话题了，劳伦缇娜。
[Character(name="avg_npc_449_1#11$1")]
[name="阿玛雅"]还是说，你很清楚自己是如何“清醒过来”的？
[Character(name="avg_1023_ghost2_1#5$1")]
[name="幽灵鲨"]......
[Character(name="avg_npc_449_1#11$1")]
[name="阿玛雅"]我们对你做了许多实验，睡美人。
[name="阿玛雅"]一直以来，只能通过岛民的知识了解海洋的我们，面前就放着那么完美的一个生物。
[Character(name="avg_npc_449_1#11$1")]
[name="阿玛雅"]我们的手段古老而原始。即使披上了教会的外皮，也遮掩不住我们身为陆地生物的瑕疵——
[Character(name="avg_npc_449_1#11$1")]
[name="阿玛雅"]——拥抱海洋的案例少之又少，而新的生命形式也并不稳定。
[Character(name="avg_npc_449_1#11$1")]
[name="阿玛雅"]还记得在你醒来并试图大闹一场之后，我和你的第一次对话吗？
[Character(name="avg_npc_449_1#10$1")]
[name="阿玛雅"]我问，“阿戈尔是怎么做到的？”
[dialog]
[Character]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_atk_saw_n_1", volume=1)]
[PlaySound(key="$e_atk_saw_n_1", volume=1)]
[PlaySound(key="$e_atk_saw_n_2", volume=1)]
[PlaySound(key="$d_avg_attack_heavy")]
[PlaySound(key="$d_sp_ballista", volume=0.5)]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
阿玛雅避开了幽灵鲨的攻击。
她轻抚着自己的脖颈，黄金大厅反射的光芒让她的皮肤略显苍白。
[Character(name="avg_npc_449_1#6$1")]
[name="阿玛雅"]巨量的液化源石在你的......这里。
[Character(name="avg_npc_449_1#6$1")]
[name="阿玛雅"]换作常人，脊髓液被换作如此浓度的液化源石，再怎么说，也不该只是“神志不清”而已吧。
[dialog]
[Character(name="avg_1023_ghost2_1#1$1")]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_atk_saw_n_1", volume=1)]
[PlaySound(key="$e_atk_saw_n_1", volume=1)]
[PlaySound(key="$e_atk_saw_n_2", volume=1)]
[PlaySound(key="$d_avg_attack_heavy")]
[PlaySound(key="$d_sp_ballista", volume=0.4)]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[Character(name="avg_npc_449_1#7$1")]
[name="阿玛雅"]唔......
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]......我该感谢你们，毕竟，你们让我体验了一段不一样的生活。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]知道吗？因为你们崇拜的那些海沟杂碎，多少阿戈尔人被迫改变了他们原本注定的轨迹。
[Character(name="avg_npc_449_1#10$1")]
[name="阿玛雅"]......你原本会成为什么？歌剧演员？剧作家？
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]不，怎么会呢，当然不是。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]我想当个雕塑家，连老师都说我有天赋。
[dialog]
[character]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_atk_saw_n_1", volume=1)]
[PlaySound(key="$e_atk_saw_n_1", volume=1)]
[PlaySound(key="$e_atk_saw_n_2", volume=1)]
[PlaySound(key="$d_avg_attack_heavy")]
[PlaySound(key="$d_sp_ballista", volume=0.4)]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
[Character(name="avg_1023_ghost2_1#3$1")]
[name="幽灵鲨"]很小的时候，我所在的城市有一座雪白的巨大的雕塑。
[Character(name="avg_npc_449_1#10$1")]
[name="阿玛雅"]它在海嗣的入侵之中崩毁了吗？
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]不，那也太俗套了。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]我连它崩毁的样子都没见过。很快，我们就迁移到了别的城市。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]但那座雕像始终在我的脑海里盘旋，我从未忘记过它的模样。而且......多亏了你们，我才理解了那座在阴影中黑白相间的雕塑有何寓意。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]“祈祷”。
[Character(name="avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"

... (全文29972字符)
```

### level_act17side_st12

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g24_cloudy_sea",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_sea", volume=1, loop=true, channel="sea")]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1, delay=0.5)]
[Character(name="avg_4009_irene_1#2$1")]
[name="审判官艾丽妮"]呼哈——！
[character(fadetime=0)]
[name="？？？"]上来！！
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.5, block=true)]
[character(fadetime=0)]
[Image(image="27_i36",xScale=0.9, yScale=0.9,x=60, y=-40)]
[ImageTween(xScaleTo=0.8, yScaleTo=0.8, duration=40,xTo=0, yTo=0,block=false)]
[Blocker(a=0, fadetime=0.5, block=true)]
[name="乔迪"]快！抓住我的手！
一艘小船。
这里离伊比利亚之眼有多远？离格兰法洛有多远？
[name="审判官艾丽妮"]欸，啊，好的——！
艾丽妮握住了他的手。
阿戈尔人的手和黎博利的没有区别。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[image]
[Background(image="27_g24_cloudy_sea",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_4042_lumen_1#1$1")]
[name="乔迪"]呃——抱、抱歉——我力气稍微有点小......
[Character(name="avg_4009_irene_1#1$1")]
[name="艾丽妮"]没事......
[Character(name="avg_4042_lumen_1#8$1")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="乔迪"]我远远看见那艘船爆炸的时候——真的吓了一跳！你们还好吗！？
[dialog]
[character(fadetime=0)]
[Character(name="avg_1023_ghost2_1#12$1",fadetime=1)]
[delay(time=1)]
[name="幽灵鲨"]你没事就好。调整呼吸，总会游泳吧？
[Character(name="avg_1023_ghost2_1#12$1")]
[name="幽灵鲨"]幸好现在还算风平浪静。
[Character(name="avg_4009_irene_1#2$1")]
[name="审判官艾丽妮"]哈啊......哈啊......其他人呢？
[Character(name="avg_1023_ghost2_1#12$1")]
[name="幽灵鲨"]......确认一些事情。
[Character(name="avg_4009_irene_1#2$1")]
[name="审判官艾丽妮"]刚才那是......阿戈尔？这么近？斯图提斐拉一直在阿戈尔城市的上面打转？
[Character(name="avg_1023_ghost2_1#12$1")]
[name="幽灵鲨"]我们也许可以想办法回那座城市看看情况，可是你坚持不了。
[Character(name="avg_1023_ghost2_1#12$1")]
[name="幽灵鲨"]而且，队长似乎也不太同意我们就这么开开心心地回家。城市不会这么靠近陆地，我对那座城市完全没有记忆。
[Character(name="avg_4009_irene_1#2$1")]
[name="审判官艾丽妮"]......咳咳......哈......
[Character(name="avg_4009_irene_1#2$1")]
[name="审判官艾丽妮"]所以，你们要，回到那座城市吗？
[character]
[dialog]
[Character(name="char_263_skadi#2",fadetime=1)]
[delay(time=1)]
[name="斯卡蒂"]不。歌蕾蒂娅说，这里同时也是海嗣的领地。这座城市，是避难退居于此的。
[Character(name="avg_4009_irene_1#2$1")]
[name="审判官艾丽妮"]什么？
[Character(name="avg_1023_ghost2_1#12$1")]
[name="幽灵鲨"]被你们称作岛民的阿戈尔人，就是那些靠近陆地的城市崩溃后逃离的难民。
[Character(name="avg_1023_ghost2_1#12$1")]
[name="幽灵鲨"]......我们应该去帮助他们。
[dialog]
[character(fadetime=0)]
[Character(name="avg_474_gladiia_1#5",fadetime=1)]
[delay(time=1)]
[name="歌蕾蒂娅"]两件事。
[Character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]乌尔比安没死，他也拒绝与我们同行。
[Character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]这附近还有其他的海嗣，它们被那场进化吸引而来，整个族群无比躁动。
[Character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]我们可以趁现在杀回去，但我们再也出不来。
[Character(name="avg_1023_ghost2_1#11$1")]
[name="幽灵鲨"]......我们......总算见到了故乡的城市，现在，又要背对着它离开？
[Character(name="char_263_skadi#2")]
[name="斯卡蒂"]......
[dialog]
[character(fadetime=0)]
歌蕾蒂娅无言地看了一眼斯卡蒂。
她掩饰得很好。就像在一切静谧的瞬间，她轻抚脖颈那时一样掩饰得很好。
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]......我们似乎别无选择。
[Character(name="char_263_skadi#6")]
[name="斯卡蒂"]为什么！？
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]这里不该有一座城市。
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]我们......我们应该回到岸边，重整旗鼓。
[Character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]我们的职责是护卫阿戈尔，而不是，“回家”。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="27_g24_cloudy_sea",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.8)]
[Character(name="avg_4042_lumen_1#11$1")]
[name="乔迪"]......
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]你怎么做到的？
[Character(name="avg_4042_lumen_1#8$1")]
[name="乔迪"]呃，啊，您和我说话？您指什么？
[Character(name="avg_4009_irene_1#1$1")]
[name="审判官艾丽妮"]这艘船比我们的那艘还要简陋。你怎么确定我们的位置？这片大海如此宽广。
[Character(name="avg_4042_lumen_1#7$1")]
[name="乔迪"]......我......我比对了“愚人号”每一次发出信号的位置......发现了一些规律，所以我就想，呃......碰碰运气。
[Character(name="avg_4009_irene_1#2$1")]
[name="审判官艾丽妮"]运气？这个规律的轨迹误差有多少？
[Character(name="avg_4042_lumen_1#11$1")]
[name="乔迪"]呃，两三百海里？
[Character(name="avg_4009_irene_1#1$1")]
[name="审判官艾丽妮"]这不能称之为规律。如果你赌错了，你几乎没有机会追上我们，你会死在海上。
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]......真是个奇迹。
[Character(name="avg_4042_lumen_1#11$1")]
[name="乔迪"]是......
[Character(name="avg_4042_lumen_1#7$1")]
[name="乔迪"]......那个......我想问一个问题......请审判官阁下不要笑我。
[Character(name="avg_4009_irene_1#7$1")]
[name="审判官艾丽妮"]我笑不出来。
[Character(name="avg_4042_lumen_1#7$1")]
[name="乔迪"]......我现在，是一个伟大的人吗？
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Image(image="27_i29",xScale=0.85, yScale=0.85)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_451_1#8$1")]
[name="蒂亚戈"]你的祖父母，你的父母，乔迪，格兰法洛的两代人，他们都曾为了这个蓝图努力。他们本该......永远伟大，真的。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[image]
[Background(image="27_g24_cloudy_sea",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_4009_irene_1#6$1")]
[name="审判官艾丽妮"]......呵。
[name="审判官艾丽妮"]不算吧。
[name="审判官艾丽妮"]你只是个幸运儿罢了。
[Character(name="avg_4042_lumen_1#4$1")]
[name="乔迪"]哈哈......是吗？
[Character(name="avg_4009_irene_1#1$1")]
[name="审判官艾丽妮"]老师......以及审判庭的其他同僚之间，总流传着这样的看法。
[Character(name="avg_4009_irene_1#1$1")]
[name="审判官艾丽妮"]只有牺牲者才配得上“伟大”一词。在我们努力存活并为伊比利亚而战的每一刻，我们都只是背负着巨大责任前行的普通人。
[Character(name="avg_4009_irene_1#1$1")]
[name="审判官艾丽妮"]并非审判官们喜欢妄自菲薄。我们选择最残酷的方式对待伊比利亚，是因为松懈的瞬间我们就会被摧垮。
[Characte

... (全文21796字符)
```

### ref_act17side

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 

[Image(image="27_kv",screenadapt="coverall", fadetime=0)]
```

### training_act17side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动17side教学关_a

[PopupDialog(dialogHead="$avatar_doberm")] 针对接下来可能面对的敌人与作战环境，今天我们要展开特殊的训练。
[PopupDialog(dialogHead="$avatar_doberm")] 虽然只是根据审判庭提供的前线情报模拟出的战场，但也务必认真对待。
[Tutorial(focusX=0, focusY=120, focusWidth=80, focusHeight=80, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_snakek", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
那、那些在蠕动的地块是什么？！

[PopupDialog(dialogHead="$avatar_doberm")] 那是溟痕。有学者声称它们是一种特殊的海洋生命，目前我们还没有掌握太多信息。你看——
```


> 本章节共34个脚本文件，此处展示前30个。

## 统计

- 总字符数：614453
- 对话行数：4697


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
