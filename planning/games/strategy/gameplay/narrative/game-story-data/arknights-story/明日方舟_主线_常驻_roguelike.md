# 明日方舟 · 主线/常驻 · roguelike（38段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 主线/常驻, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟主线/常驻「roguelike」完整剧情脚本（38个文件，292行对话）

## 正文
## 章节信息

- 分类：主线/常驻
- 目录：obt/roguelike
- 脚本文件数：38

### level_rogue1_ending_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
由此，故事迎来终结。
灯光关闭，演员离场，红幕布缓缓拉上。
曲终人散，一切又重归寂静。
[dialog]
[Background(image="24_RL_castlehall",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
傀影恢复了自我。
他仍记得自己的所作所为。
他明白，身为主演的他仅是剧团准备的诱饵。
引诱着这些热诚而高尚的凡人一次次跃入这有来无回的陷坑。
一路艰险，无需言语。
如今他幸而获救，可在这之前呢？
可曾有人迷失在这高耸迷宫中？
自己又可曾将施以援手的同伴推下舞台？
他不敢想象。
他感到羞愧。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_4025_aprot2_1#1$1",blackstart=0.2,blackend=0.7,block=true,fadetime=1.5)]
[delay(time=2)]
[name="？？？"]该回家了，卢西恩。
[Character(name="avg_npc_293_1#3$1")]
[name="傀影"]你是......
[Character(name="avg_4025_aprot2_1#2$1")]
[name="暮落"]你可给罗德岛添了个大麻烦，希望你现在想好了面对博士时的台词。
[Character(name="avg_npc_293_1#7$1")]
[name="傀影"]......对博士念诵台词只会增加我的愧疚。
[Character(name="avg_npc_293_1#10$1")]
[name="傀影"]我会用行动补偿罗德岛。
[Character(name="avg_4025_aprot2_1#1$1")]
[name="暮落"]那就好。
[Character(name="avg_4025_aprot2_1#7$1")]
[name="暮落"]......
[Character(name="avg_4025_aprot2_1#8$1")]
[name="暮落"]话说回来，这里还真是令人熟悉啊。
[Character(name="avg_4025_aprot2_1#8$1")]
[name="暮落"]舞台，剧场，每位演员梦寐以求的场所。
[Character(name="avg_4025_aprot2_1#9$1")]
[name="暮落"]不想高歌一曲吗？
[Character(name="avg_npc_293_1#7$1")]
[name="傀影"]我的歌喉只会带来灾祸，可以的话......
[Character(name="avg_4025_aprot2_1#9$1")]
[name="暮落"]呼......
[Character(name="avg_4025_aprot2_1#1$1")]
[name="暮落"]抱歉，只是确认一下。
[Character(name="avg_4025_aprot2_1#1$1")]
[name="暮落"]你真的回来了。
[Character(name="avg_4025_aprot2_1#9$1")]
[name="暮落"]需要搭把手吗？
[Character(name="avg_npc_293_1#10$1")]
[name="傀影"]......
[Character(name="avg_npc_293_1#9$1")]
[name="傀影"]......多谢。
[Dialog]
[Character]
[Image(image="24_RL01", fadetime=2, xScale=1.1, yScale=1.1)]
[ImageTween(image="24_RL01", fadetime=1,xScaleTo=0.9, yScaleTo=0.9, duration=40)]
[delay(time=5)]
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=5, block=true)]
[stopmusic(fadetime=5)]
[Character]
[Image]
```

### level_rogue1_ending_2

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
由此，故事迎来终结。
灯光关闭，演员离场，红幕布缓缓拉上。
曲终人散，一切又重归寂静。
[dialog]
[Background(image="24_RL_castlehall",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
巨大的玩偶倒在舞台上，再也没了声响。
[Character(name="avg_npc_130",fadetime=1.5,block=true)]
Miss.Christine很想用这柔韧的缝布磨磨爪子，或者窝在玩偶爆开的棉花里小憩一会儿。
但对她来说，现在的首要任务，还是确认傀影的状态。
从傀影失去心智的那刻起，Miss.Christine就一直在给罗德岛的干员们留下线索。
虽然，她并不清楚那些愚钝的家伙能否理解脚印、爪痕与牙印的含义......
然而就结果来看，Miss.Christine还是十分满意的。
优雅的女士轻声嘟囔了几句。
那位斐迪亚还在确认玩偶的状态，女士知道，他在担心玩偶的操控者会突然现身，将傀影再次置入剧团的阴影。
答案自然是不会，女士早已洞察。
探查无果后，斐迪亚前去搀扶傀影。起初，斐迪亚的语气中带着一丝似有似无的戒备。
他也曾是剧团的成员，直至今日，他仍畏惧剧团的一切。
在确认傀影真正回归后，他也卸下了心头的重担，恢复了之前那副轻柔忧郁的模样。
他走下舞台，向着古堡的出口而去。
傀影在阶梯顶端驻足沉思，试图将自己如乱麻一般的心绪整理妥当。
而女士，就在他脚边舔舐着爪子。
出于天性，女士不经意地四下张望，在感到脊背上的瘙痒后，又自然地扭过头去，准备挠挠自己的后背。
但就在转头的瞬间，女士停下了动作。
在那里，她看到了......
[Dialog]
[Character]
[Image(image="24_RL02", fadetime=2, xScale=1.1, yScale=1.1)]
[ImageTween(image="24_RL02", fadetime=1,xScaleTo=0.9, yScaleTo=0.9, duration=40)]
[delay(time=2)]
一位不速之客。
[Dialog]
[delay(time=3)]
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=5, block=true)]
[stopmusic(fadetime=5)]
[Character]
[Image]
```

### level_rogue1_ending_3

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_RL_castlehall",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
“剧团喉舌”倒在了舞台上。
手中丝线散落一地，如同蛛网那般，密密麻麻。
他曾经以此操纵古堡机关，以及他那堆邪恶的玩偶。
但现在，随着这位前剧团成员的陨落，一切都结束了。
傀影松了口气。
他的半生被猩红剧团所支配，而今，他再一次挣脱了剧团的枷锁。
“闹剧已然落幕，该让生活重新回归平静了。”
傀影这样想着。
然而......
灯光闪耀，幕布拉开。
舞台还在等待着什么。
他不由自主地取过喉舌的椅子，放在了舞台中央。
他坐下，他思考，他沉默。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“歌唱吧，歌唱吧。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
一个细小的声音在他脑中回响。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“为了你自己。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
......
一个音节从傀影嘴唇间流出。
一个，又一个。
紧接着，是字词，是唱段。
舞台不再沉默，主演放声歌唱。
听闻这悠扬的旋律，阴影中传出了几不可闻的声响。
它们在应和，它们在歌唱。
倒地的报幕人也随之爬起，丢弃了手中的丝线，走向自己在舞台上的位置。
[dialog]
[character(name="avg_npc_291",blackstart=0.2,blackend=0.7,block=true)]
[name="“剧团喉舌”"]......演员已就位。
[character(name="avg_npc_291")]
[name="“剧团喉舌”"]......我也应，履行职责。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
......
暮落已经听到了声响，只要找到傀影，任务就大功告成了。
他推开了大门。
[dialog]
[Background(image="24_RL_castlehall",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_gateopen")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_npc_291",fadetime=1.5)]
[delay(time=2)]
[name="“剧团喉舌”"]喔，第一位客人。
[Character(name="avg_4025_aprot2_1#4$1")]
[name="暮落"]这，你怎么会......
[Character(name="avg_npc_291")]
[name="“剧团喉舌”"]两位游子如今都回到了剧团的怀抱。
[name="“剧团喉舌”"]可喜可贺。
[name="“剧团喉舌”"]那么，我在此宣布......
[name="“剧团喉舌”"]戏剧开幕。
[Dialog]
[Character]
[Image(image="24_RL03", fadetime=1, xScale=1.1, yScale=1.1)]
[ImageTween(image="24_RL03", fadetime=1,xScaleTo=0.9, yScaleTo=0.9, duration=20)]
[delay(time=3)]
在暮落眼中，往昔的梦魇于舞台上一一浮现：
赶车人扬起长鞭。
报幕人傲然挺立。
道具师校准器具。
灯光师呼来喝去。
厨师长磨刀霍霍。
管家沉默不语。
剧作家埋头书写。
“影子”飘忽不定。
“刀舞”寒光闪烁。
“白英花”满面微笑。
至于剧团长本人，他正凝视着暮落。
所有剧团成员都藏在舞台的阴影里，眼中红光烁烁。
唯一一位受到光芒照耀的，则是“血钻”卢西恩。
他清了清嗓子。
他正......
准备歌唱。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[stopmusic(fadetime=3)]
[Character]
[Image]
```

### level_rogue1_ending_4

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_RL_castlehall",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_292_1#7$1")]
[name="剧作家"]上好的剧本需要用时间来淬炼。
[Character(name="avg_npc_292_1#7$1")]
[name="剧作家"]舞台已写就，场景已编织。
[Character(name="avg_npc_292_1#7$1")]
[name="剧作家"]主角还听得到剧团的呼唤，主角还会再次登上舞台。
[Character(name="avg_npc_292_1#2$1")]
[name="剧作家"]而在主角身后，“正义的同伴”罗德岛从不缺席。
[Character(name="avg_npc_292_1#2$1")]
[name="剧作家"]主角逃离剧团，又在剧团的呼唤下回归。
[Character(name="avg_npc_292_1#2$1")]
[name="剧作家"]懦夫逃离剧团，却在此刻毅然回首面对我们。
[Character(name="avg_npc_292_1#2$1")]
[name="剧作家"]只为搭救一个有着些许关系的......
[Character(name="avg_npc_292_1#1$1")]
[name="剧作家"]陌生人？同伴？好友？
[Character(name="avg_npc_292_1#1$1")]
[name="剧作家"]总之，他的勇气已然得证，故事也因此迎来终结。
[Character(name="avg_npc_292_1#1$1")]
[name="剧作家"]主角与懦夫都回到了罗德岛，回到了他们的家园。
[Character(name="avg_npc_292_1#1$1")]
[name="剧作家"]而剧团什么都没得到。
[Character(name="avg_npc_292_1#1$1")]
[name="剧作家"]报幕人弃离职责，拿起人偶丝线的那一刻——
[Character(name="avg_npc_292_1#1$1")]
[name="剧作家"]他就注定像所有无聊的反派那样落得个被打倒在地的下场。
[Character(name="avg_npc_292_1#11$1")]
[name="剧作家"]颜面尽失。
[Character(name="avg_npc_292_1#8$1")]
[name="剧作家"]不得不说，以这样的结局收尾是对我个人的亵渎。
[Character(name="avg_npc_292_1#9$1")]
[name="剧作家"]所以我加了一些段落。
[Character(name="avg_npc_292_1#7$1")]
[name="剧作家"]执笔成为阻碍，将创造者的苦难与愤恨强加于主角。
[Character(name="avg_npc_292_1#7$1")]
[name="剧作家"]而作为成长的代价，主角将把对创造者的叛逆贯彻到底。
[Character(name="avg_npc_292_1#7$1")]
[name="剧作家"]再加上罗德岛的介入，我所企盼的，对于角色性格与个人命运的转变尽皆改道。
[Character(name="avg_npc_292_1#7$1")]
[name="剧作家"]由此，故事的终幕就不是我所能着墨的了。
[Character(name="avg_npc_292_1#7$1")]
[name="剧作家"]......
[Character(name="avg_npc_292_1#9$1")]
[name="剧作家"]一篇失败的故事在写就后便会被焚毁，一切都将从头来过。
[Character(name="avg_npc_292_1#5$1")]
[name="剧作家"]创作中难免会出些意料之外的差错，希望您理解。
[Character(name="avg_npc_292_1#5$1")]
[name="剧作家"]写就伏笔，却发现角色没有能力前去回收。
[Character(name="avg_npc_292_1#5$1")]
[name="剧作家"]铺垫许久，主角却倒在了回收伏笔前的那一刻。
[Character(name="avg_npc_292_1#5$1")]
[name="剧作家"]不应出现的配角，不应发生的事件，不应面对的障碍。
[Character(name="avg_npc_292_1#5$1")]
[name="剧作家"]还有不应做出的抉择。
[Character(name="avg_npc_292_1#5$1")]
[name="剧作家"]这属实是我近年来接手的，最具挑战性的剧本。
[Character(name="avg_npc_292_1#1$1")]
[name="剧作家"]万幸的是，在一次次书写中，有那么几篇熠熠生辉。
[Character(name="avg_npc_292_1#1$1")]
[name="剧作家"]而就您的要求来看，我更倾向于推荐您这篇。
[Character(name="avg_npc_292_1#1$1")]
[name="剧作家"]艰难险阻被尽扫一空，众人期盼的美好结局，以及深藏心中的黑暗种子。
[Character(name="avg_npc_292_1#1$1")]
[name="剧作家"]当它花开四瓣，结下果实，一切美好终将化为我们所希冀的悲剧。
[Character(name="avg_npc_292_1#7$1")]
[name="剧作家"]命运已成定数，主角茫然无知。
[Character(name="avg_npc_292_1#9$1")]
[name="剧作家"]我们则在暗处等待，等待着享受结局到来时的无上愉悦。
[Character(name="avg_npc_292_1#10$1")]
[name="剧作家"]不知您意下如何？
[Dialog]
[Character]
[Image(image="24_RL04", fadetime=2, xScale=1.1, yScale=1.1)]
[ImageTween(image="24_RL04", fadetime=1,xScaleTo=0.9, yScaleTo=0.9, duration=40)]
[delay(time=4)]
[name="剧作家"]剧团长阁下。
[Dialog]
[delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[delay(time=3)]
[stopmusic(fadetime=3)]
[Character]
[Image]
```

### level_rogue1_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_RL_castlehall",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
古堡矗立于林。
破碎得恰到好处。
剧团在此扎营。
为戏剧搭建舞台。
多年经营已显成效。
只可惜仍有疑惑尚未解答。
主演在哪里？
主角在哪里？
沉默，沉默，无人能够奉上答案。
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_293_1#6$1",fadetime=1.5)]
[delay(time=3.5)]
主演昭然若揭。
主角无需自证。
请登上舞台。
剧团的新星，剧团的血钻。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
万物齐备。
戏剧已然开演。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Image]
```

### ref_rogue_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]  rogue1ref

[Image(image="pic_rogue_1_1",screenadapt="coverall")]
[Image(image="pic_rogue_1_2",screenadapt="coverall")]
[Image(image="pic_rogue_1_3",screenadapt="coverall")]
[Image(image="pic_rogue_1_4",screenadapt="coverall")]
[Image(image="pic_rogue_1_5",screenadapt="coverall")]
[Image(image="pic_rogue_1_6",screenadapt="coverall")]
[Image(image="pic_rogue_1_7",screenadapt="coverall")]
[Image(image="pic_rogue_1_8",screenadapt="coverall")]
[Image(image="pic_rogue_1_9",screenadapt="coverall")]
[Image(image="pic_rogue_1_10",screenadapt="coverall")]
[Image(image="pic_rogue_1_11",screenadapt="coverall")]
[Image(image="pic_rogue_1_12",screenadapt="coverall")]
[Image(image="pic_rogue_1_13",screenadapt="coverall")]
[Image(image="pic_rogue_1_14",screenadapt="coverall")]
[Image(image="pic_rogue_1_15",screenadapt="coverall")]
[Image(image="pic_rogue_1_16",screenadapt="coverall")]
[Image(image="pic_rogue_1_17",screenadapt="coverall")]
[Image(image="pic_rogue_1_18",screenadapt="coverall")]
[Image(image="pic_rogue_1_19",screenadapt="coverall")]
[Image(image="pic_rogue_1_20",screenadapt="coverall")]
[Image(image="pic_rogue_1_21",screenadapt="coverall")]
[Image(image="pic_rogue_1_22",screenadapt="coverall")]
[Image(image="pic_rogue_1_23",screenadapt="coverall")]
[Image(image="pic_rogue_1_24",screenadapt="coverall")]
[Image(image="pic_rogue_1_25",screenadapt="coverall")]
[Image(image="pic_rogue_1_26",screenadapt="coverall")]
[Image(image="pic_rogue_1_27",screenadapt="coverall")]
[Image(image="pic_rogue_1_28",screenadapt="coverall")]
[Image(image="pic_rogue_1_29",screenadapt="coverall")]
[Image(image="pic_rogue_1_30",screenadapt="coverall")]
[Image(image="pic_rogue_1_31",screenadapt="coverall")]
[Image(image="pic_rogue_1_32",screenadapt="coverall")]
[Image(image="pic_rogue_1_33",screenadapt="coverall")]
[Image(image="24_RL01",screenadapt="coverall")]
[Image(image="24_RL02",screenadapt="coverall")]
[Image(image="24_RL03",screenadapt="coverall")]
```

### ref_rogue_1_2

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]  rogue1ref2

[Image(image="24_RL04",screenadapt="coverall")]
[Image(image="pic_rogue_1_34",screenadapt="coverall")]
[Image(image="pic_rogue_1_35",screenadapt="coverall")]
[Image(image="pic_rogue_1_KV1",screenadapt="coverall")]
[Image(image="pic_rogue_1_KV2",screenadapt="coverall")]

```

### tutorial_rogue1_b-6

```
[HEADER(is_skippable=true,is_autoable=false)] rogue1_b-6关卡内剧情
[PopupDialog(dialogHead="$avatar_cshost")] 时刻归正，红月已至。
[PopupDialog(dialogHead="$avatar_cshost")] 牵丝的人偶正在舞动。
[PopupDialog(dialogHead="$avatar_cshost")] 为了至高无上的艺术。
[PopupDialog(dialogHead="$avatar_cshost")] 去吧，“血钻”，去吧，他们正是你渴盼已久的观众。
[PopupDialog(dialogHead="$avatar_cshost")] 我，剧团忠诚的喉舌，在此宣布——
[PopupDialog(dialogHead="$avatar_cshost")] 演出开始！
[Blocker(fadetime=0.3, block=true, a=0)] 
```

### tutorial_rogue1_b-7

```
[HEADER(is_skippable=true,is_autoable=false)] rogue1_b-7关卡内剧情
[PopupDialog(dialogHead="$avatar_cshost")] 时刻归正，红月已至。
[PopupDialog(dialogHead="$avatar_cshost")] 牵丝的人偶正在舞动。
[PopupDialog(dialogHead="$avatar_cshost")] 为了至高无上的艺术。
[PopupDialog(dialogHead="$avatar_cshost")] 去吧，我的杰作，去吧，为观众们奉上精彩的演出。
[PopupDialog(dialogHead="$avatar_cshost")] 我，剧团忠诚的喉舌，在此宣布——
[PopupDialog(dialogHead="$avatar_cshost")] 演出开始！
[Blocker(fadetime=0.3, block=true, a=0)] 
```

### tutorial_rogue1_b-8

```
[HEADER(is_skippable=true,is_autoable=false)] rogue1_b-8关卡内剧情
[PopupDialog(dialogHead="$avatar_csphtm")] 你就是剧团最后的幸存者吗，喉舌？
[PopupDialog(dialogHead="$avatar_cshost")] 呵，呵呵......你并不了解剧团，“新人”。
[PopupDialog(dialogHead="$avatar_csphtm")] 我无需，也不必了解。
[PopupDialog(dialogHead="$avatar_csphtm")] 无论你从何处来，往昔的噩梦。回到你的归处去。
[PopupDialog(dialogHead="$avatar_csphtm")] 这场闹剧，该落下帷幕了。
[Blocker(fadetime=0.3, block=true, a=0)] 
```

### tutorial_rogue1_b-9

```
[HEADER(is_skippable=true,is_autoable=false)] rogue1_b-9关卡内剧情
[PopupDialog(dialogHead="$avatar_cswrtr")] 盛大篇章已经落幕。
[PopupDialog(dialogHead="$avatar_cswrtr")] 无趣至极，就让它随烈火燃尽。
[PopupDialog(dialogHead="$avatar_cswrtr")] 但你仍在这里，追求......真相？
[PopupDialog(dialogHead="$avatar_cswrtr")] 我以我的笔勾勒血钻的事迹。
[PopupDialog(dialogHead="$avatar_cswrtr")] 你又是为了什么，想要阻碍我的创作？
[PopupDialog(dialogHead="$avatar_cswrtr")] 无需多言，演员。
[PopupDialog(dialogHead="$avatar_cswrtr")] 开始你的演绎。
[Blocker(fadetime=0.3, block=true, a=0)] 
```

### level_rogue2_ending_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[PlayMusic(intro="$newhope01_intro", key="$newhope01_loop", volume=0.7)]
[delay(time=2)]
[Background(image="32_RL2_cliffday",screenadapt="coverall")]
[dialog]
[PlaySound(key="$d_avg_sea", volume=0.6, loop=true, channel="sea")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=2)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_4066_highmo_1#7$1",fadetime=1)]
[delay(time=3)]
[characteraction(name="middle", type="move", ypos=-60,  fadetime=1, block=false)]
[character(fadetime=1)]
[PlaySound(key="$bodyfalldown2", volume=1)]
[delay(time=2)]
[Character(name="avg_437_mizukisummer_1#7$1",fadetime=1)]
[delay(time=2)]
[character]
[Character(name="avg_npc_610_1#2$1",fadetime=1)]
[delay(time=2)]
[name="？？？"]  你做得很好，水月。
[Character(name="avg_437_mizukisummer_1#5$1")]
[name="水月"]  西塞罗爷爷。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  她只是没能像你一样完美。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  她是那么地渴望改变，哪怕使者的馈赠让她迷失——
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  那仍是她期盼的。
[Character(name="avg_437_mizukisummer_1#8$1")]
[name="水月"]  可回忆和歌唱呢？她看上去和以前一样喜爱歌唱。
[Character(name="avg_437_mizukisummer_1#8$1")]
[name="水月"]  变成那副样子，她只能发出些让自己害怕的杂音。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  我只能提供选择，至于个体最后走向何方，我想没有人能够决定。
[Character(name="avg_437_mizukisummer_1#10$1")]
[name="水月"]  即使她变成现在这样，您也无动于衷吗？
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  这样的个体确实并不多见。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  大多数人类并不知道自己在索取什么东西，或是被某种突发的情感所操控。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  当他们吞下使者的馈赠后，意识就被大群的本能征服，成为恐鱼，或是某种不完全的海嗣，迫不及待地游入海洋。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  海沫能够从这种形态下转变回来，想必还是打心底里想要抓住那些她所珍视的人类特质吧。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  某种程度上来说，就像你一样，水月。
[Character(name="avg_437_mizukisummer_1#8$1")]
[name="水月"]  ......
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  但是，你并没有这个过程，即便接受了海嗣之躯，你对自己的认知仍旧将你塑造成了现在这副模样。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  你接受了成为海嗣的一切，然后做出了人类的选择，就和曾经的我一样。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  可她失败了。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  因为恐惧，或是孤独？我并不清楚。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  就结果来说，她处在成功与失败之间。虽然接受了馈赠，但拒绝再将任何东西割离自身，成了自然的不和谐音。
[Character(name="avg_437_mizukisummer_1#8$1")]
[name="水月"]  如果您的实验所描绘的未来蓝图拒绝了那些不够强韧的个体，那么这对人类而言就不能算是一种成功的学习和进化。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  确实，确实，我亲爱的孩子。既然这是你给出的答案，我会修正我的研究。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  还记得我向你提出过的问题吗？
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  “如何成为一个更好的人类？”
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  我很满意你的答复。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  你看，正确地接受这份力量让你的思维也变得开阔了起来，看来你已经完全洞悉了我的目标。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  或许在我的努力下，所有品尝神明果实的人类都能变得如你一般聪慧。
[Character(name="avg_437_mizukisummer_1#8$1")]
[name="水月"]  那样的生命还能够被称作人类吗？
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  真正的人类，懂得运用超越物质的强韧精神来克服一切道具的副作用。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  而现阶段，那些没能克服的，或许只能哀叹自己孱弱的思维与肉体无法承载“人类”这一词语的重量。
[Character(name="avg_437_mizukisummer_1#8$1")]
[name="水月"]  ......
[Character(name="avg_437_mizukisummer_1#4$1")]
[name="水月"]  我会让海沫活下去。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  这是你仁慈的选择，只要是你想做的就去做吧。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  你的一切行为都将为后人所标榜。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  很高兴见到你，水月。正如我说的那样，只要你不偏离道路，我们终会重逢。
[Character(name="avg_npc_610_1#1$1")]
[name="西塞罗"]  我们会再见的。
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[character(fadetime=2)]
[delay(time=3)]
[Character(name="avg_437_mizukisummer_1#8$1")]
[name="水月"]  哼......老爷爷还是和以前一样固执。
[dialog]
[character]
[Character(name="avg_4066_highmo_1#7$1",fadetime=1)]
[delay(time=1)]
[name="海沫"]  呜......呜呜......
[Character(name2="avg_4066_highmo_1#7$1",name="avg_437_mizukisummer_1#5$1",focus=1)]
[name="水月"]  你醒了？
[Character(name2="avg_4066_highmo_1#7$1",name="avg_437_mizukisummer_1#1$1",focus=1)]
[name="水月"]  变成那样身体消耗也挺大的，想要吃点什么吗，我帮你做。
[Character(name2="avg_4066_highmo_1#7$1",name="avg_437_mizukisummer_1#1$1",focus=2)]
[name="海沫"]  好......
[Character(name2="avg_4066_highmo_1#5$1",name="avg_437_mizukisummer_1#1$1",focus=2)]
[name="海沫"]  哎等等，那个是？！
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background]
[Dialog]
[Image(image="pic_rogue_2_48", x=-100,y=60, xScale=1.2, yScale=1.2)]
[ImageTween(image="pic_rogue_2_48", xTo=0,yTo=0, xScaleTo=0.85, yScaleTo=0.85, duration=80)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Character(name="avg_437_mizukisummer_1#1$1")]
[name="水月"]  啊啊，这是你的肢体。
[Character(name="avg_4066_highmo_1#1$1")]
[name="海沫"]  ？！
[Character(name="avg_437_mizukisummer_1#1$1")]
[name="水月"]  你没能完全成为海嗣，所以增生出的组织大多会脱落。
[Character(name="avg_437_mizukisummer_1#1$1")]
[name="水月"]  至于一些粘连在肉体上的部分我也帮你切除了，以后你还是能够像个正常人一样生活，外形上不会被别人多嘴的。
[Character(name="avg_437_mizukisummer_1#1$1")]
[name="水月"]  来吧，趁着肢体还新鲜，多少吃一些补充点生命力呗。
[Character(name="avg_4066_highmo_1#1$1")]
[name="海沫"]  哎，啊，呃，这个，不是。
[Character(name="avg_437_mizukisummer_1#1$1")]
[name="水月"]  嘿咻。
[dialog]
[PlaySound(key="$fireburst",channel="fire")]
[delay(time=1)]
[stopsound(fadetime=2,channel="fire")]
[Character(name="avg_437_mizukisummer_1#1$1")]
[name="水月"]  不用担心，这个熟起来很快的。
[Character(name="avg_4066_highmo_1#1$1")]
[name="海沫"]  我我我不是这个意思。
[Character(name="avg_437_mizukisummer_1#1$1")]
[name="水月"]  嗯......这串可能确实有点焦了，那我先吃吧。
[Character(name="avg_4066_highmo_1#1$1")]
[name="海沫"]  ......
[Character(name="avg_4066_highmo_1#1$1")]
[name="海沫"]  水月......
[Character(name="avg_437_mizukisummer_1#1$1")]
[name="水月"]  嗯？
[Character(name="avg_437_mizukisummer_1#1$1")]
[name="水月"]  想要来一串吗？
[Character(name="avg_4066_highmo_1#1$1")]
[name="海沫"]  不要！！！！！！！
[Character(name="avg_4066_highmo_1#1$1")]
[name="海沫"]  不，不是这个问题......
[Character(name="avg_4066_highmo_1#1$1")]
[name="海沫"]  ..

... (全文7087字符)
```

### level_rogue2_ending_2

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[PlayMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.7)]
[delay(time=2)]
[Background(image="32_RL2_cliffday",screenadapt="coverall")]
[dialog]
[PlaySound(key="$d_avg_sea", volume=0.6, loop=true, channel="sea")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[PlaySound(key="$d_avg_attack_heavy")]
[PlaySound(key="$d_sp_ballista", volume=0.4)]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
[Character(name="char_empty",fadetime=0,block=true)]
[characteraction(name="middle", type="move", xpos=-60,  fadetime=1, block=false)]
[Character(name="avg_437_mizuki_1#6",fadetime=1,block=true)]
[delay(time=2)]
[name="水月"]  呜呃......
[dialog]
[character]
[Character(name="avg_npc_448_1#1$1",fadetime=1)]
[delay(time=1)]
[name="最后的骑士"]你引来浪涛。
[Character(name="avg_npc_463_1#1$1")]
[name="罗辛南特"]（低沉的嘶鸣）
[Character(name="avg_npc_448_1#1$1")]
[name="最后的骑士"]不，同类，泥土的芬芳......
[Character(name="avg_npc_448_1#1$1")]
[name="最后的骑士"]种子落在海里，绽开深蓝的花......
[Character(name="avg_npc_448_1#1$1")]
[name="最后的骑士"]这不是巨浪......
[Character(name="avg_npc_463_1#1$1")]
[name="罗辛南特"]（警觉地竖起耳朵）
[Character(name="avg_npc_448_1#1$1")]
[name="最后的骑士"]巨浪——
[dialog]
[stopmusic(fadetime=1)]
[stopsound(fadetime=1,channel="sea")]
骑士的自言自语戛然而止。
海浪翻涌声、羽兽嘶叫声、狂风呼啸声。
都在那一刻彻底消逝。
风起云涌，寂静无声。
[character]
[dialog]
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=0.7)]
[PlaySound(key="$d_avg_sea", volume=1, loop=true, channel="sea")]
[PlaySound(key="$d_avg_fish_howl", volume=0.4)]
[PlaySound(key="$pourwater", volume=0.4)]
[PlaySound(key="$d_avg_jump_water", volume=0.4)]
[PlaySound(key="$d_avg_walk_water", volume=0.4)]
经过片刻沉寂后，海浪拔地而起，灾难再度降临，
伊莎玛拉引领着大群从涌潮中现出身形。
伊比利亚不再是唯一的受害者，整片大地——
都将溺没于大静谧之中。
[Character(name="avg_npc_463_1#1$1",name2="avg_npc_448_1#1$1")]
骑士耳中失去了声响，他猛地扯起坐骑的缰绳，将矛头对准了海洋彼端。
他高声吼叫，颅腔震颤，可声音传到耳中，却只是诡异的尖啸。
臂膀在颤动，呼吸变得急促，罗辛南特不停摇晃着脑袋。
海嗣本能不断抗拒着这种无意义的同族相残，
但骑士丝毫不在意这些生理反应背后的残酷现实，他坚定地认为，那是心中抑制不住的狂喜，
因为——
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background]
[Dialog]
[Image(image="pic_rogue_2_49", x=-100,y=0, xScale=1.2, yScale=1.2)]
[ImageTween(image="pic_rogue_2_49", xTo=0,yTo=0, xScaleTo=0.85, yScaleTo=0.85, duration=80)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
眼前的巨物他追寻已久
那是天命所至，那是巨浪根源
Ishar......mla......他还记得这个名字
是祂唤起风浪，是祂驱使海洋吞噬陆地，是祂在代表大海发声
那么，只要这宏伟的生命在此陨落
海洋便将永远沉默，再也泛不起一丝浪花
[dialog]
[delay(time=1)]
海水打在铠甲上，引起如钢铁巨兽碾过大地时的轰响
雨水稀释了呼吸中的铁锈味，却将生物的腥臭送入鼻中
浪潮想要压下长枪，水流把他拖曳向陆地
整个世界都在阻止骑士
[dialog]
[delay(time=1)]
麦穗在摇荡，石榴花在呼唤
忠诚的坐骑打了个响鼻，不满地用头颅敲了敲海面
寂静之中，狂人放声大笑
[dialog]
[delay(time=1)]
最后的骑士一跃而起。
[stopSound(channel="sea",fadetime=3)]
[Dialog]
[Character]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Image]
```

### level_rogue2_ending_3

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.7)]
[delay(time=2)]
[PlaySound(key="$d_avg_sea", volume=0.6, loop=true, channel="sea")]
[Background(image="32_RL2_cliffnight",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[dialog]
[delay(time=1)]
这是新世界诞生以来，发生在“初生”之间的第一场冲突。
水月成了“蔓延的枝条”所缺失的意识，并借助这力量挑战“腐化之心”。
大群则静候这纷争的结果。
[dialog]
[delay(time=1)]
伊莎玛拉落败了。
祂将失去“初生”的身份，成为大群中籍籍无名的一员。
水月确实获得了胜利，但祂却没有丝毫喜悦。
正在祂的眼前，另一位“初生”已邻近疯狂。
深海主教们的诡计昭然若揭：他们将大静谧的元凶——“始源的命脉”再度引致疯狂，并诱导斯卡蒂体内的“腐化之心”觉醒。
两位“初生”一旦融合，便会引发灭世级别的大静谧。如此一来，深海主教们期盼已久的阿戈尔覆灭与海嗣时代便指日可待。
这位“初生”不似伊莎玛拉，祂是海嗣存续的象征，微生物的富集。
祂与海洋融为一体，除非大海干涸，否则绝无击败祂的方法。
除非......
[dialog]
[delay(time=1)]
海洋变得鲜红，静谧近在眼前。
即使平息命脉的疯狂，成为大群的引领者，
也并不能阻止它们刻入基因的进化与生存本能。
水月当然能够让大群远离陆地，
但随着海嗣本能与大群意识觉醒，
由祂带来的制约终将失效。
或许十年？或是一个世代？
祂自己也无法保证。
唯一能够做到的，只是在自我与人性彻底败退前，坚守与博士的约定。
......至少，得让博士与同伴们在余下的时光中免受海嗣侵扰。
浪潮将起，水月别无选择。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background]
[Dialog]
[Image(image="pic_rogue_2_50", x=-60,y=0, xScale=0.9, yScale=0.9)]
[ImageTween(image="pic_rogue_2_50", xTo=0,yTo=0, xScaleTo=0.85, yScaleTo=0.85, duration=40)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
祂走进了大海。
随着躯体转变，水月正在将自己转换成与命脉相同的形态，以此，祂便能抚慰这位同胞的癫狂。
深蓝从鲜红中扩散开来。
而水月的人类躯体逐渐消失。
在最后一刻，祂回过头来望向陆地，瞳孔中映着一个人的倒影。
下一秒，浪潮涌过。
再也寻不到水月的踪影。
......
深蓝遍染鲜红，“初生”的癫狂得以平息。
海嗣与恐鱼们朝着海洋深处游去，将大地留给了它的原住民们。
人类欢呼雀跃，庆祝着这一历史性的改变。
可他们不知道的是——
万事万物皆有代价。
一家医药公司，就此永远失去了一位值得信赖的成员。
[stopSound(channel="sea",fadetime=3)]
[stopmusic(fadetime=3)]
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Image]
```

### level_rogue2_ending_4

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[playMusic(key="$calm_loop", volume=0.6)]
[delay(time=2)]
[Background(image="bg_black",screenadapt="coverall")]
[dialog]
[PlaySound(key="$d_avg_sea", volume=0.6, loop=true, channel="sea")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=2)]
思考最终告一段落。
为人的自我将情感、渴望与思维尽数表达给非人的自我。
祂接受了。
祂漂浮在水面，轻柔地雕琢着水月的新躯体。
而大群则遵照祂的建议，养精蓄锐，陷入沉寂......
[Dialog]
[Background(image="32_RL2_cliffday",screenadapt="coverall",fadetime=2.5)]
[delay(time=3)]
[PlaySound(key="$d_avg_walk_water", volume=1)]
[charslot(slot="m",name="avg_437_mizuki_1#1",duration=2.5)]
[delay(time=4.5)]
在那之后不久，他诞生了。
一具承载着人类灵魂的碳基肉体——这是祂给予他的礼物——被轻轻放在了海岸边的礁石上。
他很快就苏醒过来，再一次以人类的感官接触这个世界。
潮湿的空气、阳光的温度、微风的吹拂都让他格外享受。然而，一根友好的触须顶了顶他的脑袋。
这提醒了他，在重新回归这个世界前，他还有一件事要做。
水月该和“水月”分别了。
[charslot(slot="m",name="avg_437_mizuki_1#7")]
[name="水月"]有你在旁边，这段日子也不算太无聊啦。
[name="水月"]谢谢你。
[charslot(slot="m",name="avg_437_mizuki_1#2")]
[name="水月"]......
[charslot(slot="m",name="avg_437_mizuki_1#3")]
[name="水月"]那么，再会了。
[Dialog]
他以人类的语言道别。
祂以海嗣的方式回应。
而后——
寰宇轰鸣。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=2.5, block=true)]
[charslot]
[delay(time=2)]
[Image(image="pic_rogue_2_55", x=0,y=0, xScale=1.5, yScale=1.5)]
[ImageTween(image="pic_rogue_2_55", xTo=0,yTo=0, xScaleTo=1, yScaleTo=1, duration=50)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
大地现出万千空洞，海洋则被掀起骇浪惊涛。
泰拉的每一个角落都有海嗣起身，向着天空而去。
幼嗣栖居亲族背脊。
子代跟随亲代游弋。
“初生”们如山岳般的躯体缓慢却坚定地向着天空彼岸游去。
[Dialog]
[PlaySound(key="$d_avg_run_water", volume=1)]
[delay(time=0.3)]
[PlaySound(key="$d_avg_jump_water", volume=1)]
[Image(image="pic_rogue_2_55", x=0,y=0, xScale=0.85, yScale=0.85,fadetime=2.5)]
[delay(time=3)]
不一会儿，庞大的“初生”便消失在了天幕中，然而地海之上仍有无数海嗣加入这浩浩荡荡的行列，走上“初生”行过的道路。
整个族群化作纽带，向着天空缓缓延伸。
当它们完成迁徙。
星空将迎来新的开拓者，而泰拉，将成为一片乐土。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=2.5, block=true)]
母亲啊，我们已得解答。
大群生发于海，也必将回归于海。
那无垠无界的璀璨星河。
即是我们，新的归宿。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[stopSound(channel="sea",fadetime=3)]
[Dialog]
[charslot]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Image]
```

### level_rogue2_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.7)]
[delay(time=2)]
曾经有人向水月抛出了这样一个问题：
“如何成为一个更好的人类？”
[dialog]
[delay(time=1)]
那时的他刚刚逃离死亡，脑中除了迷茫与讶异外别无他物。
[dialog]
[delay(time=1)]
现在他长大了。
[dialog]
[Background(image="32_RL2_cliffday",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=2)]
[PlaySound(key="$d_avg_sea", volume=0.6, loop=true, channel="sea")]
[Character(name="avg_437_mizuki_1#2",fadetime=1)]
[delay(time=2)]
随着年岁渐长，生活为水月提供了一些观点与视角，他已确信自己有资格回答这个问题。
所以他来到了海边，
循着海风、浪潮与大群的指引。
去往老主教的住处。
[dialog]
[PlaySound(key="$d_avg_walk_water", volume=0.6)]
[character(fadetime=1)]
[delay(time=2)]
个人疑虑将得解答,
然而......
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[stopmusic(fadetime=3)]
[Dialog]
母亲啊，我们将去往何方？
[stopSound(channel="sea",fadetime=3)]
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Image]
```

### level_rogue3_ending_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic]
[Dialog]
[Background]
[Dialog]
[PlaySound(key="$d_avg_snowstormlp", volume=1, loop=true, channel="bgs")]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.7)]
[Image(image="pic_rogue_3_31", x=-60,y=0, xScale=0.9, yScale=0.9)]
[ImageTween(image="pic_rogue_3_31", xTo=0,yTo=0, xScaleTo=0.85, yScaleTo=0.85, duration=40)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
“你要前往何处？”
[name="麦哲伦"]——
麦哲伦警惕地四下张望，捂住耳朵。
是幻听吗？
她走出冬牙群山，冰原铺陈在她眼前。
天地间风雪轰鸣，怒吼声穿透她的躯壳。
冻土山岩与亘古坚冰对抗的震颤自脚下升起，寒意扑面而来。
她已被卷入风雪。
她无法隔绝这个声音。
[dialog]
[Blocker(a=1, r=1, g=1, b=1, fadetime=2, block=true)]
[Background]
[Dialog]
[Image(image="pic_rogue_3_28", x=-60,y=0, xScale=1, yScale=1)]
[ImageTween(image="pic_rogue_3_28", xTo=0,yTo=0, xScaleTo=0.85, yScaleTo=0.85, duration=40)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=false)]
[delay(time=1)]
“你要前往何处？”
[name="麦哲伦"]......
千钧之重的视线，落在年轻的外来者身上。
可她感觉到的不是被质问的压迫感，而是向古老的意志倾诉的渴望。
[name="麦哲伦"]我——要探索未知之处。
“你凭借什么前行？”
[name="麦哲伦"]嗯......
[name="麦哲伦"]好奇心，勇气，知识，技术。
[name="麦哲伦"]还有......前人的经验，萨米的朋友们给我的帮助。
[name="麦哲伦"]联合科考队出发之前，宣言里还说，我们背负着“为全人类开拓未来的使命”。
[name="麦哲伦"]——虽然很满足虚荣心，但那种说法我担不起啦，嘿嘿。愿望就只是愿望而已。
[name="麦哲伦"]嗯，于我而言，重要的还有愿望。
“你渴望带走什么？”
[name="麦哲伦"]生态样本，数据，笔记，照片......
[name="麦哲伦"]关于萨米的知识，通向冰原的钥匙。
[name="麦哲伦"]还有......我自己！
[name="麦哲伦"]老师说，科考过程中，最最重要的事情就是活下去。只有这样，才能把收集到的东西带给其他人，让知识传承下去。
[name="麦哲伦"]......
[name="麦哲伦"]我也有一个问题。
[name="麦哲伦"]您就是萨米本身吗？
冰原的风声倏忽变得更加清晰。
庇护者放任她走出了自己的怀抱。
祂接纳了外来者，将她视如自己的孩子。
因此祂将外来者推向冰原的严寒与风雪，推向萨米人平静而自傲地领受的命运。
[name="麦哲伦"]......我其实一开始还有点不确定呢，因为以前从来没有萨米与外来者对话的记录。
[name="麦哲伦"]萨米人也说，您入睡了，很少再发出声音。
[name="麦哲伦"]祖灵之父......您以前也这样向其他人发问过吗？
[name="麦哲伦"]回答了您的探索者们，后来去了哪里？
[dialog]
[stopmusic(fadetime=2)]
[stopSound(channel="bgs",fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background]
[delay(time=1)]
[Dialog]
[Image]
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[Background(image="40_g2_glacier",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="bgs",fadetime=1)]
[PlayMusic(intro="$newhope02_intro", key="$newhope02_loop", volume=0.7,fadetime=1,crossfade=1)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_2012_typhon_1#6$1")]
[name="提丰"]一旦翻过冬牙群山，天气就会变得非常糟糕。唉，就像现在这样。
[charslot(slot = "m", name = "avg_2012_typhon_1#1$1")]
[name="提丰"]你还好吗，麦麦？
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]我对冰原也不算陌生啦。
[charslot(slot = "m", name = "avg_2012_typhon_1#1$1")]
[name="提丰"]唉，那难道你刚刚真的只是在发呆？
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[name="麦哲伦"]欸？！我只是在想事情而已！
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Dialog]
[Background]
[Dialog]
[Image(image="pic_rogue_3_31",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[delay(time=1)]
[name="麦哲伦"]......就像西蒙娜姐说过的一样，没道理只有哥伦比亚人喜欢到处探险，乌萨斯人喜欢扩张领土，而萨米人对外界就不好奇。
[name="麦哲伦"]每一个时代，一定都有探索者想要越过山脉，离开萨米的怀抱，走向无尽冰原。
[name="寒檀"]当然。
[name="寒檀"]萨米的战士缄默而保守，但任何人如果愿望如此，萨米的意志并不阻拦。
[name="寒檀"]怎么了？
[name="麦哲伦"]嘿嘿，没事。我们走吧。
她没有说，自己好像只是在恍惚中得到了一个不辩自明的答案，又好像听闻了一段漫长历史里的千万个故事。
她在刹那的时间里得知了无数未曾记载于史册的名字——那些探索者都没有再回来。
无尽冰原的面貌，也几乎没有变得更加清晰。
即便如此，也要前进吗？
萨米不再等待回答，群山缓缓隐没在身后的风雪之中。
眼前，只有无垠的银白与不见尽头的阴影。
[Dialog]
[charslot]
[stopSound(channel="bgs",fadetime=2)]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=1,g=1, b=1, fadetime=3, block=true)]
[Image]
[delay(time=1)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0, block=true)]
```

### level_rogue3_ending_2

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background]
[delay(time=1)]
[Dialog]
[Background(image="40_g2_glacier",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="bgs",fadetime=1)]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.7)]
人们知道，萨米的意志有时会展露出偏爱。
祂曾教生于冰寒的女儿驯服风雪，曾赠送将死的战士一截树枝的生命力。
北地战士中最有威望的雪祀，被大地修补了致死的伤痕，失去的角由树枝取代。
[charslot(slot = "m", name = "avg_341_sntlla_1#5$1")]
[name="寒檀"]......让我来拦住风雪吧，各位请立即离开这里。
[charslot(slot = "m", name = "avg_341_sntlla_1#5$1")]
[name="寒檀"]请尽快把消息带给北地的其他战士们。
[charslot(slot = "m", name = "avg_341_sntlla_1#5$1")]
[name="寒檀"]“我们又一次遇到了超越过去记载的灾异现象。”
[charslot(slot = "m", name = "avg_341_sntlla_1#5$1")]
[name="寒檀"]“来自冰原的威胁在不断加剧。”
[charslot(slot = "m", name = "avg_341_sntlla_1#5$1")]
[name="寒檀"]以及......
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background]
[Dialog]
[charslot]
[Image(image="pic_rogue_3_32", x=-60,y=0, xScale=0.9, yScale=0.9)]
[ImageTween(image="pic_rogue_3_32", xTo=0,yTo=0, xScaleTo=0.85, yScaleTo=0.85, duration=40)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
如今他的角已经折断。
祝福落回大地，被恩赐的生命枯萎，无法再回归山泽林木的身体遍布黑色的裂痕。
[charslot(slot = "m", name = "avg_341_sntlla_1#5$1")]
[name="寒檀"]......“阵线上的重要阵地陷落。”
[charslot(slot = "m", name = "avg_341_sntlla_1#5$1")]
[name="寒檀"]“但是，被邪魔转化的战士们已经在大家的携手努力下得到控制。”
[charslot(slot = "m", name = "avg_341_sntlla_1#5$1")]
[name="寒檀"]......“送别的仪式，交给了萨满‘寒檀’。”
千百场苦战，冬夜终于降临。
山地的战士比任何人都清楚，邪魔的侵蚀不可逆转，自己的意志与生命，注定成为敌人的领土与食粮。
他们定格在行进时最后的动作，躯体已经被死亡与虚无占据。
但寒檀知道，意志的星火仍对抗着冰原的寒风，尚有一丝意识支撑着他们等待。
忍耐过命运安排的所有苦痛折磨，忍受着眼下的悲惨结局，他们在等待后来者。
等待洁净的冰霜覆盖在他们被黑色伤痕侵蚀的躯壳上，盖过“树痕”在大地上仅存的痕迹。
于是寒檀高举起法杖为他们送别。
而英雄带领着他的战士，迎向他们最后的对手，迎向他们终将承受的命运。
无人怒吼，无人质问，无人回头。
命运始终如一，战士从不为时间所动。
年轻的后来者啊——
战士的生命就此凝固。
他们的视线越过寒檀，依旧守望着永恒的冰原。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background]
[delay(time=1)]
[Dialog]
[Image]
[charslot]
[Background(image="40_g2_glacier",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_snowfootstep")]
寒檀走入战士的碑林，穿过他们，前往阵线上的下一处营地。
曾得到萨米莫大爱怜的她，如今重新感到自己身处风雪的怀抱之中。
她驱使风拂去战士断角上的积雪，风的痕迹转瞬间又被埋在纷纷扬扬的雪片下。
但她知道，从今日起，自己还将执着地、一次又一次地为这片土地拂去黑色的雪花。
直至——
[Dialog]
[charslot]
[stopSound(channel="bgs",fadetime=2)]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Image]
```

### level_rogue3_ending_3

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background]
[delay(time=1)]
[Dialog]
[Background(image="40_g4_stargate_on",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[delay(time=1)]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.7)]
“我们见过被黑暗彻底吞噬的大地。”
“我们见过冰原尽头必然开启的门。”
“我们见证从始至终完整的命运。”
“为抵达它的尽头，我复原它的起因。”
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot = "m", name = "avg_npc_969_1#1$1",duration=2)]
[delay(time=2)]
[name="艾尔启"]远见所见的未来......在我眼前。
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=1)]
[delay(time=2)]
经历艰险与坎坷，经过无数次失败和更多的尝试。
科考队在独眼巨人的指引下抵达这里——北方以北，无尽冰原的尽头。
无人能够理解的巨构矗立着，艳丽的无根之花铺满它的基座。
走到这里的探索者已经熟知恐惧，而恐惧正在每个人的思维领域蔓延。
所有人都有预感，这如果是一扇可以打开的门，门外等候的必然是厄运。
但独眼巨人已经向它走去。
她从一开始走出岩窟，便只是在走向那里。
视野已经开始扭曲，辨识与理解的念头令空间急剧坍缩。
现实受到的侵蚀始于裂隙得到的认知，人们想要阻止厄运的降临，却在被干涉的恐惧中无法发出声音。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1",duration=1)]
[delay(time=1)]
[name="提丰"]......
[dialog]
[charslot]
与所有人一样，提丰注视着那个背影。
与所有人不同，提丰无数次看过那个赴命运之约的背影。
洞悉未来的独眼巨人从不解释自己的去向，只要顺着她口中命运的指引，她们总能在某处重逢。
但唯独这一次，提丰觉得自己一定要叫住她。
不是因为对大灾难的预感，不是出于对未知的恐惧，猎手敏锐地抓住自己确切的忧虑。
[charslot(slot = "m", name = "avg_2012_typhon_1#1$1")]
[name="提丰"]——艾尔启，不要走！
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background]
[Dialog]
[charslot]
[Image(image="pic_rogue_3_33", x=-60,y=0, xScale=0.9, yScale=0.9)]
[ImageTween(image="pic_rogue_3_33", xTo=0,yTo=0, xScaleTo=0.85, yScaleTo=0.85, duration=40)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
听到呼唤的独眼巨人回过头来。
圆环模样的巨大建筑开始运转，其中映出星空般璀璨的黑暗，绚烂的颜色扭曲流动。
规模远超全部已有记录的坍缩正在发生。
她已在远见之中看到过这一切。
一次向深渊中的窥视，将会为萨米乃至整个泰拉引来前所未有的灾异。
刹那的预言没有告知她，她的力量能将灾异拦住多久，更不会让她看到，此后她是多少人眼中的仇人与罪人。
关于她自己的使命，她只知道一件事——
在邪魔巨大阴影的笼罩下，独眼巨人用法术升起了黑色的帷幕，将自己引发的灾异与众人隔绝。
[name="艾尔启"]快离开吧。
那一瞬间，提丰就知道了她接下来要说什么，因为几乎永远神色悲哀的独眼巨人，此刻却面带微笑。
“这就是我的命运。”
[name="艾尔启"]你啊，我不知道命运的女儿，愿你能......
[name="艾尔启"]......自诩自由地活下去。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background]
[delay(time=1)]
[Dialog]
......不。
不！
我不相信！
我不相信是今天！
[PlayMusic(intro="$newhope01_intro", key="$newhope01_loop", volume=0.7)]
——无边无际的黑暗之中，还有一个人向前跑着。
挣脱恐惧的泥沼，甩下沉重的弓箭。
提丰想要抓住那个孤独前行的身影。
她不顾一切地伸出手。
一只纯洁无瑕的银白角兽从她身边轻巧地跃过。
轻盈得像一片雪，轻得无法触及，连蛛丝织成的捕梦网也无法捕捉。
那是每个萨米人都会在梦中遇见的，祖灵纯白色的慈悲。
[Image]
[dialog]
[Image(image="pic_rogue_3_34", x=-60,y=0, xScale=0.9, yScale=0.9)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
如极光一般，辉光撕裂黑暗，升上天幕。
萨米的兽主撞向了眼前的邪魔。
爆发的强光抛向扭曲的可视空间，光线在寂静中散射，湮佚于不可捉摸的璀璨虚空。
剧烈震荡中，角兽抖落的银霜与斑斓可怖的星辰一并消散。
湮灭的能量将冰晶升华。
冰原的尽头落下温热的水滴。
[dialog]
[Blocker(a=1, r=1, g=1, b=1, fadetime=2, block=true)]
[Background]
安玛的爱，温柔地融化在她的女儿伸向命运深渊的手上。
[Dialog]
[Image]
[delay(time=2)]
[Background(image="40_g3_stargate",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=6, block=true)]
[delay(time=2)]
邪魔的阴影褪去，银白角兽也不见踪迹。
圆环中溢出的异常色彩已经全部消失，澄净的冰面上只余下古老的银白。
所有人怔怔地仰头看着这一切。过了许久，终于有一名科考队员用脚步声打破了寂静。
科考队员们开始尝试来回穿过巨大的圆环，遗憾的是，他们没有找到启动这一建筑的方式，也没有发现可以穿行的“门”的缝隙。
在他们附近的雪地里，提丰低着头，四处搜寻。
她想捡到一团坚实的、带有兽角印记的小雪球。
[charslot(slot = "m", name = "avg_2012_typhon_1#4$1")]
[name="提丰"]......找不到了。
[charslot(slot = "m", name = "avg_2012_typhon_1#4$1")]
[name="提丰"]真奇怪，老妈妈来过的话，明明应该留下祝福的。
[charslot(slot = "m", name = "avg_2012_typhon_1#4$1")]
[name="提丰"]艾尔启......你说呢？
[charslot(slot = "m", name = "avg_npc_969_1#1$1")]
她不愿意承认那只巨大的角兽已经长久离去，但艾尔启只是缓缓地摇了摇头。
[charslot]
祂的足迹消失在无尽的落雪之中。
并不属于萨米埃拉菲亚族群的两名萨卡兹，低声感谢着萨米的祖灵赐予的爱。
一切风浪似乎已经过去。
然而，命运的预言并未完成。
就如同她注定的死亡——
人们注定会真正推开那道门。
[Dialog]
[charslot]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Image]
```

### level_rogue3_ending_4

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background]
[delay(time=1)]
[Dialog]
[Background(image="bg_laccolith",screenadapt="coverall")]
[PlaySound(key="$d_avg_sandwnd", volume=0, loop=true, channel="a")]
[SoundVolume(volume=1, fadetime=4,channel="a")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[delay(time=1)]
这是万王之王殿前的学者不曾测绘的黄沙之地。
生灵被吹散，金铁被熔化，砂砾本身也被磨灭。
时间归于混沌，时间不再有生命与消亡来度量，时间无边无垠。
[dialog]
[CameraShake(duration=3, xstrength=3, ystrength=2, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_mgcbttlfld", volume=0, loop=true, channel="b")]
[PlaySound(key="$d_avg_sldrchrg", volume=0, loop=true, channel="z")]
[SoundVolume(volume=0.4, fadetime=3,channel="b")]
[SoundVolume(volume=0.2, fadetime=3,channel="z")]
[delay(time=3)]
唯有号角声与猛兽的咆哮，唯有两支庞大、永不停歇地向彼此冲锋的军队清晰地存在于此，远至模糊的地平线，近至眼前。
这或许是一场因探索者的观测与认知而开始的战争。这或许是一场从未结束因而不曾开始的战争。
探索者们认出了这里。
[Dialog]
[StopSound(channel="a", fadetime=3)]
[StopSound(channel="b", fadetime=3)]
[StopSound(channel="z", fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Image(image="pic_rogue_3_35",  screenadapt="coverall",xScale=1,xScale=1)]
[ImageTween(xScaleTo=1.2, yScaleTo=1.2,yTo=50, duration=45, block=false)]
[PlayMusic(intro="$snowmonster_intro", key="$snowmonster_loop", volume=0.6)]
[PlaySound(key="$d_avg_churchfire", volume=0, loop=true, channel="c")]
[SoundVolume(volume=0.4, fadetime=3,channel="c")]
[bgeffect(name="$eb_burn",layer=1,y=-100)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
哈兰杜汗践踏大地，否认他的天途会有天堑、征服会有尽头。
路加萨尔古斯号令生死，仿佛战场的沙尘中不见晨昏，是因为他仍将时间握于手中。
古老的英雄支配一切。
有去无回的误入者成为战争的属臣。
——焚风热土。
万王之王与梦魇可汗的战争在大地最南端留下了这片死地。
探索者的步履，与千百年来在热风中焚化的闯入者一样，不过是死地的一阵烟尘。
只为避免被吹散，探索者们已经竭尽全力。
临时搭建的防御阵地摇摇欲坠，队员们通过多种辅助手段调节了身体机能，才勉强得以在高温中生存。
人们在恐惧中瞻仰着追寻伟业终点的英雄。
时间仿佛因失去标准而无比漫长。终于，巨构重启，黄沙中浮现出星光，探索者们狼狈不堪地向那扇门跑去。
“这一巨构的运转状态极不稳定。”
“空间稳定装置损坏......可运行时间很短......听到了吗，快走。”
[ImageTween(xScaleTo=1.5, yScaleTo=1.5, duration=45, block=false,yTo=150)]
踏入残破门扉的那一刻，队伍末尾的麦哲伦再次回头看向战场。
她呼吸着恐惧，感受着辐射的热量。
随后，她想起多年前人们第一次抵达无尽冰原尽头时目睹的湮灭，和曾落在自己身上的融雪。
她明白了两位统御者最后的伟业究竟是什么。
将雨林变为荒漠的可怖能量并非爆发自二者之间的战争。他们曾驱逐与克雷松相似的、穿过圆环的敌人。
巨构初次启动的结果如此令人欣喜。人类第一次获得焚风热土的信息，人类得以如此清晰地观测一段千年之前的历史——
与永恒搏斗的英雄，也同样是追寻着未知，最初从一片荒野上出发的人类。
如今，门扉洞开。
人们能够触及的疆域绝无穷尽。
探索者的视界已经扩展至未曾想象的遥远过去。
探索者也将走向命运无法预言的遥远未来。
[Dialog]
[charslot]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[StopSound(channel="c", fadetime=3)]
[bgeffect]
[stopmusic(fadetime=3)]
[Image]
```

### level_rogue3_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="40_g1_blackforest",screenadapt="coverall")]
[charslot]
[Delay(time=1)]
[playMusic(intro="$tech_intro",key="$tech_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1",duration=2)]
[delay(time=2.5)]
[charslot(slot = "m", name = "avg_248_mgllan_1#2$1")]
[playsound(key="$d_gen_transmissionget")]
[Delay(time=1.5)]	
[name="麦哲伦"]咳咳......嗯。科考队员麦哲伦，开始语音记录。
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]这是联合科考队进入萨米的第十二天。
[Dialog]
[charslot]
冻土，黑森林，木头与苔藓的气味，新雪的重量，风的温度，角兽的叫声。
记录数据的沙沙声，维生装置散发的热量，登山杖留下的痕迹，无人机升空的嗡鸣。
科考队员们摸索着这片陌生的土地。
[charslot(slot = "m", name = "avg_248_mgllan_1#9$1")]
[name="麦哲伦"]多亏有两个很好很好的萨米朋友陪同，到目前为止，我们的旅程十分顺利！
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[name="麦哲伦"]提丰，要不要来说句话？
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_2012_typhon_1#1$1",duration=1)]
[delay(time=1)]
[name="提丰"]嗯？不行，我没空。我得照顾你的那帮......“同事”。
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]那——
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]西蒙娜也没空，她在布置驱邪的物件，而且她还要追踪乌萨斯的什么东西。
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]欸嘿，好吧。
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]总之，感谢她们的帮助，不然我们一定会在森林里迷路的！
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]还有......我们马上要去见一位据说十分可靠的先知。
[Dialog]
[charslot]
握着录音笔，麦哲伦抬起头。
前方的雾气中，隐约有一个高大的人影。
能够看见厄运的萨卡兹独眼巨人，正等着为他们引路。
推敲与演算已无意义，探索者踏上坚实的土地，将视线投向了无垠的未知。
他们摸索着正在前方某处等待他们的命运。
[Dialog]
[charslot]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Image]
```

### ref_rogue_3

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]

[Image(image="pic_rogue_3_1",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_2",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_3",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_4",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_5",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_6",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_7",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_8",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_9",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_10",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_11",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_12",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_13",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_14",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_15",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_16",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_17",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_18",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_19",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_20",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_21",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_22",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_23",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_24",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_25",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_27",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_28",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_29",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_30",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_31",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_32",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_33",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_34",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_35",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_36",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_37",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_38",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_39",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_40",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_41",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_42",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_43",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_3_44",screenadapt="coverall", fadetime=0)]

[Image(image="pic_rogue_3_KV1",screenadapt="coverall", fadetime=0)]


```

### level_rogue4_ending_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[PlaySound(key="$grenade_explosion", volume=1)]
[CameraShake(duration=1.7, xstrength=20, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[PlaySound(key="$grenade_explosion", volume=1)]
[PlaySound(key="$d_sp_ballista", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=1.7, xstrength=20, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.4, block=true)]
[delay(time=2)]
[Background(image="52_mini03_sarkazfurnace",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=2)]
[playMusic(key="$calm_loop", volume=0.6)]
[charslot(slot="m",name="avg_4151_tinman_1#1$1",focus="m",duration=1)]
[delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_4146_nymph_1#2$1",focus="m",duration=1)]
[delay(time=2)]
[name="妮芙"]欸，我们回来了？
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1114_1#7$1")]
[CameraShake(duration=0.5, ystrength=20, vibrato=20, randomness=90, fadeout=true, block=false)]
[name="弗莱蒙特"]埃芒加德！
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_869_1#9$1",duration=1)]
[delay(time=2)]
[name="埃芒加德"]老师我在这里......
[dialog]
[charslot]
[charslot(slot = "r", name = "avg_npc_869_1#9$1",focus="l")]
[charslot(slot = "l", name = "avg_npc_1114_1#10$1",focus="l")]
[name="弗莱蒙特"]这就是你脑袋里挤出来的好主意？趁着我不注意拉半打萨卡兹来熔炉里？
[charslot(slot = "r", name = "avg_npc_869_1#8$1",focus="r")]
[name="埃芒加德"]我也就是想帮个忙，您看，您之前那一次也没有想象中的那么顺利嘛......
[charslot(slot = "r", name = "avg_npc_869_1#8$1",focus="r")]
[name="埃芒加德"]维什戴尔大人被炸上了天，死魂灵们也气得从熔炉里溜了出去。
[charslot(slot = "l", name = "avg_npc_1114_1#5$1",focus="l")]
[name="弗莱蒙特"]嗯？
[charslot(slot = "r", name = "avg_npc_869_1#1$1",focus="r")]
[name="埃芒加德"]我就是想说，我们举行仪式的结果还是不错的......
[charslot(slot = "r", name = "avg_npc_869_1#1$1",focus="r")]
[name="埃芒加德"]您不觉得熔炉已经平静下来了吗？
[Dialog]
[charslot]
熔炉里没有任何杂音，也感受不到任何死魂灵的躁动，他们就像是刚刚饱餐一顿陷入小憩的食客，抑或是......
躲在门后等着看某人笑话的顽童。
[charslot(slot="m",name="avg_4151_tinman_1#1$1",focus="m")]
[name="锡人"]（脱帽行礼）
[charslot(slot = "m", name = "avg_npc_1114_1#12$1")]
[name="弗莱蒙特"]......（颔首示意）
[dialog]
[charslot]
[charslot(slot = "r", name = "avg_npc_869_1#1$1",focus="l")]
[charslot(slot = "l", name = "avg_npc_1114_1#7$1",focus="l")]
[name="弗莱蒙特"]要是没人给你搭建通道，承受失控的魂灵之怒，把想法从那些张不开的嘴里扒出来，你现在就得和你的小朋友们躺在这里被烘干。
[charslot(slot = "r", name = "avg_npc_869_1#8$1",focus="r")]
[name="埃芒加德"]但——
[charslot(slot = "l", name = "avg_npc_1114_1#7$1",focus="l")]
[name="弗莱蒙特"]等回到知识圣殿我可以揪着你的命结慢慢听你狡辩，埃芒加德。
[charslot(slot = "l", name = "avg_npc_1114_1#7$1",focus="l")]
[name="弗莱蒙特"]现在给我过来，把嘴闭上。
[charslot(slot = "r", name = "avg_npc_869_1#6$1",focus="r")]
[name="埃芒加德"]唔......
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot = "r", name = "avg_npc_869_1#6$1",focus="l")]
[charslot(slot = "l", name = "avg_npc_1114_1#7$1",focus="l")]
[charslot(slot="r",focus="l",posfrom="0,0",posto="-200,0",duration=2)]
[delay(time=2.5)]
[charslot]
[charslot(slot = "m", name = "avg_npc_1114_1#12$1")]
[name="弗莱蒙特"]至于你们。
[charslot(slot = "m", name = "avg_npc_1114_1#12$1")]
[name="弗莱蒙特"]我不管你们是王庭稚儿、街区里的包打听、罗德岛的佣兵......
[charslot(slot = "m", name = "avg_npc_1114_1#12$1")]
[name="弗莱蒙特"]还是云游回来的裁缝又或是孽茨雷的弃信者。
[charslot(slot = "m", name = "avg_npc_1114_1#7$1")]
[name="弗莱蒙特"]回你们该回的地方，做你们该做的事。
[charslot(slot = "m", name = "avg_npc_1114_1#12$1")]
[name="弗莱蒙特"]卡兹戴尔那么多地方要垒起砖瓦，你们倒好，跑来这里做梦？
[charslot(slot = "m", name = "avg_npc_1114_1#12$1")]
[name="弗莱蒙特"]如果你们真想让自己梦想里的卡兹戴尔有那么一点成为现实的可能，就自己去动手。
[charslot(slot = "m", name = "avg_npc_1114_1#12$1")]
[name="弗莱蒙特"]别窝在这里靠臆想取悦自己和炉子里那帮老混蛋。
[dialog]
[charslot]
[PlaySound(key="$firestorm", channel="bg",volume=1)] 
[bgeffect(name="$eb_burn",layer=1,y=-100)]
[delay(time=3)]
[StopSound(fadetime=1, channel="bg")]
[charslot(slot = "m", name = "avg_npc_1114_1#7$1")]
[bgeffect]
[CameraShake(duration=0.5, ystrength=20, vibrato=20, randomness=90, fadeout=true, block=false)]
[name="弗莱蒙特"]说的就是你们，怎么了！
[charslot(slot = "m", name = "avg_npc_869_1#6$1")]
[name="埃芒加德"]好了好了老师，您消消气......
[charslot(slot = "m", name = "avg_npc_1114_1#7$1")]
[name="弗莱蒙特"]我没有气，说话声音大一点就叫气吗？
[charslot(slot = "m", name = "avg_npc_869_1#6$1")]
[name="埃芒加德"]是是是，您说得对......
[charslot(slot = "m", name = "avg_npc_1114_1#7$1")]
[name="弗莱蒙特"]哼。
[charslot(slot = "m", name = "avg_npc_1114_1#12$1")]
[name="弗莱蒙特"]现在离开这里，萨卡兹们，我不计较你们闯入魂灵熔炉的罪责。
[charslot(slot = "m", name = "avg_npc_1114_1#12$1")]
[name="弗莱蒙特"]埃芒加德，带他们出去。
[charslot(slot = "m", name = "avg_npc_869_1#8$1")]
[name="埃芒加德"]是......
[Dialog]
[charslot]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_gen_walk_n")]
于是萨卡兹们跟着埃芒加德离开了熔炉核心，对于他们的想法，巫妖之主并不在意。
但当锡人路过他身边时，弗莱蒙特伸手拦住了去路。
[charslot(slot="l",name="avg_4151_tinman_1#1$1",focus="r")]
[charslot(slot = "r", name = "avg_npc_1114_1#12$1",focus="r")]
[name="弗莱蒙特"]你还要在卡兹戴尔住多久？
[charslot(slot="l",name="avg_4151_tinman_1#1$1",focus="l")]
[name="锡人"]假期快用完了，我也该准备准备回哥伦比亚述职了。
[charslot(slot = "r", name = "avg_npc_1114_1#12$1",focus="r")]
[name="弗莱蒙特"]魂灵熔炉的历史使命已经接近尾声。
[charslot(slot="l",name="avg_4151_tinman_1#1$1",focus="l")]
[name="锡人"]他们烧了那么久，也该冷静一下了。
[charslot(slot = "r", name = "avg_npc_1114_1#12$1",focus="r")]
[name="弗莱蒙特"]有了那些技术，我们也不必抱着愧疚继续燃烧自己的同族。
[charslot(slot="l",name="avg_4151_tinman_1#2$1",focus="l")]
[name="锡人"]可你刚刚还在骂他们。
[charslot(slot = "r", name = "avg_npc_1114_1#1$1",focus="r")]
[name="弗莱蒙特"]呵，也就现在还能骂上几句，等他们离开百年千年，卡兹戴尔的熔炉只为节庆而燃烧的时候，我会想念他们的。
[charslot(slot="l",name="avg_4151_tinman_1#1$1",focus="l")]
[name="锡人"]那么，我有件事想和你商量。
[Dialog]
[charslot]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="49_g5_furnaceplatform",screenadapt="coverall")]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[charslot(slot="m",name="avg_4151_tinman_1#9$1",focus="m",duration=1)]
[delay(time=2)]
[name="锡人"]我回来了，老朋友们。
[charslot(slot="m"

... (全文7689字符)
```

### level_rogue4_ending_2

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background]
[delay(time=2)]
[Dialog]
[Background(image="bg_victoria",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[PlayMusic(intro="$newhope02_intro", key="$newhope02_loop", volume=0.7)]
[charslot(slot="r",name="avg_npc_1297_1#1$1",focus="all",duration=2)]
[charslot(slot="l",name="avg_npc_1296_1#1$1",focus="all",duration=2)]
[delay(time=2.5)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[dialog]
[Sticker(id="st1", multi = true, text="双王遣退周遭的卫兵，独留萨卡兹们在这新卡兹戴尔的议事厅前。", x=300,y=270, alignment="left", size=26, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n经过一场试探后，他们探查到了讲述者们不存在于这片大地的实质，同时也觉察到了这批陌生客人并没有恶意。 ",block = true)]
[Sticker(id="st1", multi = true, text="\n因此，两人放下暴力，准备倾听来客的申辩。",block = true)]
[Sticker(id="st1", multi = true, text="\n萨卡兹们各有各的想法，每个人口中的缘由也千差万别，但魔王们都听了，都认可了。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="他们让守卫放行，邀请客人们自由观览新卡兹戴尔，也欢迎来客为他们讲述更多的趣闻。", x=300,y=270, alignment="left", size=26, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n而后，主人走向台阶，客人走向大门。",block = true)]
[Sticker(id="st1", multi = true, text="\n或许在遍历这新卡兹戴尔的壮丽之后，这篇故事就将迎来它的结局。",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[dialog]
[charslot]
[charslot(slot="m",name="avg_4146_nymph_1#15$1",focus="m",duration=2)]
[delay(time=2.5)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Sticker(id="st1", multi = true, text="可妮芙还不想结束这一切，于她而言，这个故事应当才刚刚开始，她还想多游览一下这个卡兹戴尔，还想走到外面去，看看萨卡兹如今的生活。", x=300,y=270, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n可她很快就发现，自己的身体好像有些不听使唤了。时间变得黏稠而阻滞，周边的一切都停了下来。",block = true)]
[Sticker(id="st1", multi = true, text="\n而后，自己的存在突然离开躯体向着高空飞去，她只来得及瞥一眼变化后的大地，就彻底陷入了寂静黑暗。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="天空隆隆作响，昭示着死魂灵们心满意足，同时也意味着，故事要翻篇了。", x=300,y=270, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n失去意识的妮芙向下倒去，在那一瞬间，两位魔王就已经回头并准备扶起虚弱的萨卡兹。",block = true)]
[Sticker(id="st1", multi = true, text="\n在即将撞上地板前，一道无形的力量稳住了妮芙的躯体，将她慢慢扶起。",block = true)]
[Sticker(id="st1", multi = true, text="\n法杖上的钥匙四散而开，交织出难分虚实的空间。",block = true)]
[Sticker(id="st1", multi = true, text="\n一个白色的身影从笞心魔头顶浮现。",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Dialog]
[charslot]
[Image(image="pic_rogue_4_35", x=-60,y=0, xScale=1.4, yScale=1.4)]
[ImageTween(image="pic_rogue_4_35", xTo=0,yTo=0,duration=40)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=3)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Sticker(id="st1", multi = true, text="阿米娅。", x=300,y=270, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n特雷西斯与特蕾西娅心中最深的遗憾。",block = true)]
[Sticker(id="st1", multi = true, text="\n一位孤独无依的卡特斯少女，被他们收养，受他们影响，最终因他们的理念而死。",block = true)]
[Sticker(id="st1", multi = true, text="\n矿石病夺走了她的生命，他们对此无能为力。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="而现在......", x=300,y=270, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n那虚影中传来的情感，却与失去的别无二致。",block = true)]
[Sticker(id="st1", multi = true, text="\n“阿米娅”抬起了手，纯白的王冠从空中显现。",block = true)]
[Sticker(id="st1", multi = true, text="\n“文明的存续”，魔王们从未想过将这重担加在阿米娅身上。",block = true)]
[Sticker(id="st1", multi = true, text="\n但在另一片大地，另一种存在中，他们或许在身陨时将这传承交付给了她。",block = true)]
[Sticker(id="st1")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Dialog]
[charslot]
[delay(time=1)]
[Image(image="pic_rogue_4_35", x=-60,y=0, xScale=0.9, yScale=0.9)]
[ImageTween(image="pic_rogue_4_35", xTo=0,yTo=0, xScaleTo=0.85, yScaleTo=0.85, duration=40)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Sticker(id="st1", multi = true, text="于是他们也抬起了手，漆黑的王冠就此显现。", x=300,y=270, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n王冠交叠，诉说着逝去与懊悔。",block = true)]
[Sticker(id="st1", multi = true, text="\n同时，也将喜悦与希望传递给对方。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="那被改变的过去。", x=300,y=270, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n那不存在的当下。",block = true)]
[Sticker(id="st1", multi = true, text="\n那仍憧憬的未来。",block = true)]
[Sticker(id="st1", multi = true, text="\n经由“文明的存续”，两个世界所经历的所有信息，将在这点滴间不断传输。",block = true)]
[Sticker(id="st1", multi = true, text="\n直到......",block = true)]
[Sticker(id="st1", multi = true, text="\n......",block = true)]
[Sticker(id="st1")]
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Dialog]
[charslot]
[Image]
[Background(image="bg_rhodesinpatientcenter",screenadapt="coverall")]
[PlayMusic(intro="$ekg_loop", key="$ekg_loop", volume=0.4, delay=0)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[stopmusic(fadetime=2)]
[delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Sticker(id="st1", multi = true, text="妮芙睁开了眼睛。", x=300,y=270, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n她还记得自己是从魂灵熔炉旁进入故事的。",block = true)]
[Sticker(id="st1", multi = true, text="\n那这又是哪里？自己是怎么过来的？种种困惑让她有点紧张。",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[dialog]
[Delay(time=1)]
[name="？？？"]你醒了？
[dialog]
[Block

... (全文6523字符)
```

### level_rogue4_ending_3

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background]
[delay(time=1)]
[Dialog]
[Background(image="26_g1_laterano_cathedralfront",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=2)]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.7)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[dialog]
[Sticker(id="st1", multi = true, text="战斗结束了。", x=300,y=270, alignment="left", size=25, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n这是萨卡兹们从未见过的阵仗。",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[charslot(slot="r",name="avg_npc_358_1#1$1",focus="all",duration=2)]
[charslot(slot="l",name="avg_npc_358_1#1$1",focus="all",duration=2)]
[PlaySound(key="$d_avg_armywalking", volume=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[dialog]
[Sticker(id="st1", multi = true, text="萨科塔结成战阵缓步推进，头顶的光芒比太阳更甚。", x=300,y=270, alignment="left", size=25, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n铳械不间断地发出怒号，而走在最前面的铳骑，轮廓熟悉得令人恐惧。",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[charslot]
[dialog]
[charslot(slot="m",name="avg_4146_nymph_1#15$1",focus="m")]
[name="妮芙"]......
[dialog]
[charslot]
[PlaySound(key="$d_avg_land_impact", volume=0.4)]
[CameraShake(duration=1.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
[PlaySound(key="$d_avg_land_impact", volume=0.4)]
[CameraShake(duration=1.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[dialog]
[Sticker(id="st1", multi = true, text="他每向前一步，大地都会为之震撼。", x=300,y=270, alignment="left", size=25, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n铳械锃亮，坚盾如墙。",block = true)]
[Sticker(id="st1", multi = true, text="\n一如胜利本身。",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Dialog]
[charslot]
[name="？？？"]收起武器，提卡兹们。
[dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[dialog]
[Sticker(id="st1", multi = true, text="在铳骑号令下，萨科塔们整齐划一收起了铳械。", x=300,y=270, alignment="left", size=25, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n萨科塔？提卡兹？或许是这故事过于奇诡，连身在其中的讲述者都无法理解自己的思绪。",block = true)]
[Sticker(id="st1", multi = true, text="\n而就在他们陷入恍惚时，铳骑已来到了他们面前。",block = true)]
[Sticker(id="st1")]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Dialog]
[charslot]
[delay(time=1)]
[Image(image="pic_rogue_4_36", x=0,y=0, xScale=0.9, yScale=0.9)]
[ImageTween(image="pic_rogue_4_36", xTo=0,yTo=0, xScaleTo=0.85, yScaleTo=0.85, duration=40)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="？？？"]欢迎你们，未蒙福的同胞。
[name="博卓卡斯替"]我是博卓卡斯替，圣城的卫士。
[name="博卓卡斯替"]随我走吧，我将带你们回到卡兹戴尔，启迪在即，你们将不再苦于晦暗。
[dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Sticker(id="st1", multi = true, text="他的真切，他的诚挚，随着言语一同流入萨卡兹的心田。在这无可抗拒的温暖中，是更多人的善意，是心灵的袒露，是——", x=300,y=270, alignment="left", size=25, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n是天堂，是翼与环，是照耀一切的光。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="铳骑伸出了手。", x=300,y=270, alignment="left", size=25, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n他很清楚应当如何对待尚未蒙福的同胞，他们很迷茫，他们很害怕。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="因此，他将以超人的耐心对待同胞们，接受他们的谩骂与攻击，等待他们的倾诉与忏悔。", x=300,y=270, alignment="left", size=25, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n直到他们回到卡兹戴尔，重新成为提卡兹的一部分。",block = true)]
[Sticker(id="st1", multi = true, text="\n这便是他的职责。",block = true)]
[Sticker(id="st1", multi = true, text="\n他会等待。",block = true)]
[Sticker(id="st1")]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Image]
[Background(image="26_g1_laterano_cathedralfront",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[charslot]
[name="？？？"]Mon3tr！
[dialog]
[charslot(slot="m",name="npc_10002",focus="m")]
[CameraShake(duration=2, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$Mon3tr_n")]
[delay(time=1)]
[dialog]
[charslot]
[charslot(slot="m",name="npc_10002",action="zoom", poszoom = "1.5,1.5", focus="m",duration=0.5)]
[charslot(slot="m",name="npc_10002",afrom=1,ato=0,focus="m",duration=0.3)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$p_imp_whip_h", volume=1)]
[PlaySound(key="$d_avg_land_impact")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[delay(time=2)]
[PlaySound(key="$rungeneral", volume=0.9)]
[charslot(slot="m",name="char_003_kaltsn07_1#1",focus="m",duration=2)]
[delay(time=2)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.7)]
[name="凯尔希"] 跟我来，提卡兹们。
[dialog]
[charslot]
[charslot(slot="r",name="avg_4146_nymph_1#2$1",focus="all")]
[charslot(slot="l",name="avg_4151_tinman_1#1$1",focus="all")]
[delay(time=1)]
[charslot(duration=1)]
[PlaySound(key="$d_avg_crowdrun", volume=1)]
[delay(time=4)]
[name="博卓卡斯替"]......圣卫们，跟上，保护同胞。
[dialog]
[charslot]
[PlaySound(key="$d_gen_soldiersrun",volume=0.8)]
[delay(time=1)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Image]
[Background(image="bg_battlefield",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_crowdrun", volume=1)]
[charslot(slot="r",name="char_003_kaltsn07_1#1",focus="

... (全文8288字符)
```

### level_rogue4_ending_4

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background]
[delay(time=1)]
[Dialog]
[delay(time=2)]
[PlayMusic(intro="$newhope01_intro", key="$newhope01_loop", volume=0.7)]
[dialog]
辩论就像是场争斗，从大炎的垂柳湖畔到卡兹戴尔郊外的原野，一直都没有结论。
[Background(image="bg_black",screenadapt="coverall")]
[Dialog]
[charslot]
[delay(time=1)]
[Image(image="pic_rogue_4_39", x=0,y=0, xScale=0.9, yScale=0.9)]
[ImageTween(image="pic_rogue_4_39", xTo=0,yTo=0, xScaleTo=0.85, yScaleTo=0.85, duration=40)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
由是，即使这批西行至此的行者们见到了卡兹戴尔外沿的寺庙，离这故事的终点只有咫尺之遥，他们仍在求证，仍在辩论。
[Dialog]
[charslot]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[Image(image="pic_rogue_4_39", x=-100,y=20, xScale=1.4, yScale=1.4)]
[ImageTween(image="pic_rogue_4_39", xTo=-160,yTo=40,  duration=40)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
在选择与奎隆同行的萨卡兹中，泥岩是最早醒觉为阿纳萨的。
她聆听魔王的教诲，严格遵守每一条戒律，在苦修中顿悟，升起了黑色的圆轮。
但这种醒觉并没有带来解脱，不如说，成为阿纳萨让泥岩有了更多的疑惑——
为何黑轮会伴随阿纳萨的醒觉出现？为何萨卡兹生而苦难？
她的心变得平静，她的疑问却不断增多。
每有机会，她就向奎隆提问，而奎隆的解答只为她留下了更多的问题。
她的修行才刚刚开始。
[Dialog]
[charslot]
[delay(time=2.5)]
作为死魂灵与讲述者间的桥梁，锡人很少直接介入故事的演绎，但这一回，他也参与其中。
死魂灵的苦难深入灵魂，锡人想要尝试一下，这虚幻的法门是否能够解脱他身上这古老且不可逆的束缚。
可惜的是，这份修习没有带来任何变化。
可喜的是，他意识到了这份束缚早在进入熔炉前就已消逝。
既已解脱，又何来顿悟？于是他又回到了自己的位置上，旁观着讲述者们对故事的演绎。
然而遇到感兴趣的议题，他仍愿意说上几句，随后应和着众人的辩驳，重新归于沉默。
[Dialog]
[charslot]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[Image(image="pic_rogue_4_39", x=150,y=180, xScale=1.55, yScale=1.55)]
[ImageTween(image="pic_rogue_4_39", xTo=260,yTo=160, duration=40)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
所有的改变，妮芙都看在眼里，阿纳萨的黑轮与其说是转变，倒更像是一种内心的认可。
当一个萨卡兹愿意放下自己生来便潜藏于内心的对苦难的执念，似乎就能成为一名阿纳萨。
可是......妮芙打开自己的心扉，用钥匙解开每一件尘封往事仔细窥探，都没能找到自己的苦难。
随着卡兹戴尔生活越来越美好，它们好像早已逐渐溶化流逝了。
妮芙倒不是一定要变成阿纳萨，醒觉对她而言也并没有特殊的魔力，只是她想要弄清楚一件事——
那个心底里的“我执”，那个连笞心魔都毫无头绪的精神组成，到底是怎样的东西？
她为此苦恼着。
[Dialog]
[charslot]
[delay(time=2.5)]
醒觉的魔王坐在树下乘凉，坦然接受着大地的变化。
[multiline]走过耳边的风，奔于河道的水，
[multiline(end=true)]被嫩芽顶开的土壤，在心中沉寂的青火。
沧海桑田，万物流变，近在咫尺的圣地，说不定也只是座废墟。
世间万物皆为泡影，身在此中的自己，与自己口中讲与同伴的论述，或许并没有什么分别。
但奎隆仍会去讲，仍要去做。众生皆苦，若他只言片语能引人自觉自渡——
云雾散去，奎隆缓缓站起了身。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[delay(time=2)]
[ImageTween(image="pic_rogue_4_39", xTo=-300,yTo=-200, duration=20,block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=3, block=true)]
[image]
[delay(time=1)]
[BackgroundTween(yFrom=0, yTo=-30, duration=5,block=false)]
[gridbg(imagegroup="53_g16_sunnyday_L1/53_g16_sunnyday_R1/53_g16_sunnyday_L2/53_g16_sunnyday_R2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720",x=-900,fadetime=2)]
[largebgtween(duration = 30,yFrom = 300, yTo = 250,block = false)]
[Blocker(a=0, r=1, g=1, b=1, fadetime=2, block=true)]
[delay(time=2)]
西行的旅途尚缺一步，卡兹戴尔——迦师坻耶会是故事的终点吗？奎隆相信每位同胞都有自己的答案。
他们拾起行囊，向着阿纳萨的圣地走去。
如果这座城市能够成为答案，那便是吧。
[Dialog]
[charslot]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Image]
```

### level_rogue4_ending_5

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background]
[delay(time=1)]
[Dialog]
[delay(time=2)]
[playMusic(intro="$distressed_intro", key="$distressed_loop",volume=0.6)]
[dialog]
[Background(image="38_g21_skystarry_r1",screenadapt="coverall")]
[Dialog]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=5, block=true)]
带着妮芙的创想与关切，钥匙没入“阿米娅”的身躯，如源石般的黑暗包裹着她，消失在了空无之中。
[dialog]
[charslot(slot="m",name="avg_4146_nymph_1#10$1",focus="m",duration=1.5)]
[delay(time=2)]
[name="妮芙"]对不起，阿米娅......
[dialog]
[charslot(slot="m",name="avg_4146_nymph_1#17$1",focus="m")]
[name="妮芙"]唉，故事讲成这个样子，先祖们会不满意的吧......
[charslot(slot="m",name="avg_4146_nymph_1#17$1",focus="m")]
[name="妮芙"]锡人先生，我们该怎么办呢？
[dialog]
[charslot]
[delay(time=2.5)]
[charslot(slot="m",name="avg_4146_nymph_1#7$1",focus="m")]
[name="妮芙"]锡人先生？埃米？卡莱莎女士？
[dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[delay(time=1)]
妮芙转过头去，却发现一个人都没有。
曾经讲述过的故事，曾经走过的道路，此刻都消逝于无形。
只有远方的闪烁星点，可能记录过它们的存在。
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_6666_1#1$1",focus="m",duration=1.5)]
[delay(time=3)]
[charslot(slot="m",name="avg_4146_nymph_1#2$1",focus="m")]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="妮芙"]阿米娅？！
[dialog]
[charslot]
本应打开心锁的无终之钥此刻重新出现在了半空中，“阿米娅”摘下它，交还给了妮芙。
[dialog]
[charslot(slot="r",name="avg_npc_6666_1#3$1",focus="all")]
[charslot(slot="l",name="avg_4146_nymph_1#17$1",focus="all")]
[charslot(slot="r",posfrom="0,0",posto="-90,0",focus="all",duration=1.5)]
[delay(time=1.5)]
[delay(time=1)]
[charslot(slot="r",posfrom="-90,0",posto="0,0",focus="all",duration=2)]
[delay(time=2)]
[charslot(slot="l",name="avg_4146_nymph_1#17$1",focus="l")]
[name="妮芙"]谢......谢谢......
[dialog]
[charslot]
妮芙很肯定，眼前这个人仍旧是终结的化身，她确实是来结束一切的。
但同时，她也还是妮芙所熟知的阿米娅，悲悯与善意并未因身份的变化而褪去。
站在她面前，妮芙感受不到一点恐惧。
她甚至是微笑着把钥匙交还给妮芙的，那个笑容，笞心魔再熟悉不过了。
这到底是怎么回事？
妮芙只记得自己因为想法枯竭接受了老祖宗们的想象。
这中间到底发生了什么？
哒喀。
[dialog]
[charslot(slot="m",name="avg_4146_nymph_1#7$1",focus="m")]
[name="妮芙"]嗯？
[dialog]
[charslot]
手中响起奇怪的声响，像是某种倒放的蛋壳碎裂声。
低头一看，妮芙发现自己手中的钥匙不知从何时起变成了一颗发光的白茧，黑色碎壳正从底部缓慢向上附着。
在白茧与黑壳反射出的光芒中，妮芙看到了一篇又一篇的故事：
死于人祸，死于源石，死于天灾。
那是“阿米娅”的故事。或许是为了感谢妮芙展现的善意，她向这位素昧平生的朋友分享了自己的经历。
[dialog]
[charslot(slot="m",name="avg_npc_6666_1#1$1")]
[delay(time=1)]
[charslot(duration=3)]
[delay(time=4.5)]
但与此同时，她也为妮芙的旅途画上了句号。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=4, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Dialog]
[charslot]
[delay(time=1)]
所有讲述者终将面对这一刻。
在想象枯竭，灵感丧失之时，盲目地追求结局。
最终，迎来自己的末日。
[dialog]
[Image(image="pic_rogue_4_48", x=-20,y=0, xScale=0.87, yScale=0.87)]
[ImageTween(image="pic_rogue_4_48", xTo=0,yTo=0, xScaleTo=0.85, yScaleTo=0.85, duration=10)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[delay(time=2)]
散发着温暖光芒的白茧轻柔地包裹住讲述者们，阿米娅在他们尚未察觉时便已完成了这一步骤。
就像是午后小憩前的困意，轻轻将人引至沉睡。
在那之后，一切便不再变动。
悲伤就此斩断，欢乐永远停留，死亡也被驱逐，悻悻地从每篇故事中离开。
在那之后，如夜空般漆黑的“源石”缓缓攀附，将周边固定，如此一来，便没有外力能够变动故事分毫。
时光无尽，被固定的叙事如行星般环绕在它们的终结者身旁，见证着一段又一段故事加入它们的行列。
然而......
[dialog]
[Image(image="pic_rogue_4_47", x=0,y=0, xScale=0.85, yScale=0.85,fadetime=2)]
[delay(time=2)]
阿米娅一言不发，看着眼前封存到一半的故事。
曾经属于妮芙一行人的位置，如今只剩下了一块块人形空洞。
他们的使命已经完成，便可欣然回到来处。
只留下被固定的种种叙事，仍旧在阿米娅身边环绕。
讲述者一旦离开，这些奇语便再无终结，如此一来，那些故事中的苦难也就永远不会到来了。
可正如讲述者对故事有着种种无可奈何，故事本身也对讲述者的行为无能为力。
他们能够离开，但作为故事的一部分，阿米娅将会永远留在这片空无之中。
她的视线投向了远方。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Image(image="pic_rogue_4_47", x=-90,y=-70, xScale=1.3, yScale=1.3)]
或许，在她无法触碰到的某个彼端。
有着另一个人，另一个故事，另一种对终结的求索。
那个人闯过重重难关，击败无数强敌，在这迎来结局前的最后时刻，收到了一条来自远方的讯息。
那是一个由情感组成的图像，图像的主人公，很熟悉。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
她想要拯救一切，却只能眼睁睁看着苦难向那个人逼近。
然而那个人仍旧击碎了一切束缚，站在了终点的大门前。
她很开心，除了献上祝福外，再无所求。
这就是她想要传达的。
想必在一切都结束之前，那个人愿意就这条讯息给个回复。
权且把这当做是最后一页上的句号吧。
[dialog]
[delay(time=1)]
[Decision(options="如果累了，就闭上眼睛休息一会。我陪着你。;对不起，阿米娅，真希望我能为你做些什么。;（沉默）", values="1;2;3")]
[Predicate(references="1;2;3")]
[delay(time=1)]
[Image(image="pic_rogue_4_48", x=-90,y=-70, xScale=1.3, yScale=1.3,fadetime=2)]
[delay(time=5)]
[Dialog]
[charslot]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Image]
```

### level_rogue4_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="52_mini03_sarkazfurnace",screenadapt="coverall")]
[charslot]
[Delay(time=1)]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=2)]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot="m",name="avg_4146_nymph_1#10$1",focus="m",duration=2)]
[charslot(slot="m",name="avg_4146_nymph_1#10$1",focus="m",posfrom="0,-30",posto="0,0",duration=2)]
[delay(time=2.5)]
[name="妮芙"]疼疼疼......
[charslot(slot="m",name="avg_4146_nymph_1#7$1",focus="m")]
[name="妮芙"]这里是？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4151_tinman_1#1$1",focus="m",duration=1)]
[delay(time=2)]
[name="锡人"]魂灵熔炉，卡兹戴尔的魂灵熔炉。
[charslot(slot="m",name="avg_4146_nymph_1#17$1",focus="m")]
[name="妮芙"]锡人先生？
[charslot(slot="m",name="avg_4146_nymph_1#17$1",focus="m")]
[name="妮芙"]刚刚发生了什么，这里好像......不太对劲？
[charslot(slot="m",name="avg_4151_tinman_1#1$1",focus="m")]
[name="锡人"]你不是许诺给熔炉的死魂灵们讲述一个更好的故事，演绎一个更精彩的卡兹戴尔吗？
[charslot(slot="m",name="avg_4151_tinman_1#1$1",focus="m")]
[name="锡人"]他们现在把笔塞在我们手里了。
[charslot(slot="m",name="avg_4151_tinman_1#3$1",focus="m")]
[name="锡人"]尽情发挥吧，妮芙。就从这里，从我们最熟悉的熔炉开始。
[charslot(slot="m",name="avg_4151_tinman_1#3$1",focus="m")]
[name="锡人"]把脑袋里的想法全部拿出来，用从未说过的妄语编写萨卡兹所在的大地。
[charslot(slot="m",name="avg_4151_tinman_1#1$1",focus="m")]
[name="锡人"]让那帮老家伙们好奇、惊颤、愤怒、欢笑。
[charslot(slot="m",name="avg_4151_tinman_1#1$1",focus="m")]
[name="锡人"]让他们那被烧得模糊的灵魂重新感受下生活的滋味。
[Dialog]
[charslot]
熔炉很平静，内里也感受不到死魂灵们被灼烧的痛苦与愤怒。
他们并不在那里。
但妮芙感觉得到，死魂灵们正聚在一起，注视着，议论着，争吵着。
[charslot(slot="m",name="avg_4146_nymph_1#15$1",focus="m")]
[name="妮芙"]那等大家都醒过来，我们就出发吧。
[charslot(slot="m",name="avg_4146_nymph_1#14$1",focus="m")]
[name="妮芙"]我先去前面看看。
[charslot(slot="m",name="avg_4151_tinman_1#8$1",focus="m")]
[name="锡人"]别走太远。
[charslot(slot="m",name="avg_4146_nymph_1#1$1",focus="m")]
[name="妮芙"]嗯，我会当心的。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n")]
[delay(time=3)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Sticker(id="st1", multi = true, text="在这个故事的开端，萨卡兹们在卡兹戴尔的心脏中醒来。", x=300,y=270, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n没有沉重的过往，也没有绝望的未来。 ",block = true)]
[Sticker(id="st1", multi = true, text="\n一切尚未发生，一切尚未结束。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="于是，在准备妥当后，他们离开了熔炉，去往那还未被讲述的未知。 ",x=300,y=270, alignment="left", size=26, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n故事翻向了新的一页。",block = true)]
[Sticker(id="st1")]
[Dialog]
[charslot]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Image]
```

### ref_rogue_4

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]

[Image(image="pic_rogue_4_KV1",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_1",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_2",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_3",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_4",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_5",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_6",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_7",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_8",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_9",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_10",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_11",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_12",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_13",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_14",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_15",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_16",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_17",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_18",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_19",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_20",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_21",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_22",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_23",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_24",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_25",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_27",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_28",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_29",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_30",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_31",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_32",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_33",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_34",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_35",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_36",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_37",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_38",screenadapt="coverall", fadetime=0)]


```

### ref_rogue_4_dlc1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]

[Image(image="pic_rogue_4_39",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_40",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_41",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_42",screenadapt="coverall", fadetime=0)]
[Image(image="pic_rogue_4_KV2",screenadapt="coverall", fadetime=0)]

```


> 本章节共38个脚本文件，此处展示前30个。

## 统计

- 总字符数：82238
- 对话行数：292


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
