# 明日方舟 · 活动剧情 · act21side（138段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act21side」完整剧情脚本（138个文件，5541行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act21side
- 脚本文件数：138

### level_act21side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g4_srctheater",screenadapt="coverall")]
[playMusic(intro="$ghosthunter_intro",key="$ghosthunter_loop", volume=0.6)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_685_1#8$1",fadetime=1)]
[Delay(time=1)]
[name="贝纳尔多"]三位小姐，欢迎来到米兰剧场。
[Dialog]
[Character]
[Character(name="avg_103_angel_1#7$1",name2="avg_201_moeshd_1#11$1",fadetime=0.5)]
[Delay(time=1.5)]
[Character(name="char_101_sora_1#1")]
[name="空"]这里真是漂亮。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]叙拉古人热爱在这里伴随着音乐和表演消磨时间，毕竟，当现实乏善可陈，难以改变，人们就会需要一个寄托自己幻想的地方。
[name="贝纳尔多"]或者，把自己的血腥事业类比于舞台上英雄们的伟业，以此来获得道德上的满足。
[Character(name="char_101_sora_1#5")]
[name="空"]您的评价......真是毫不留情。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]做我们这行的，总得对自己的职业有个清楚的认知，对吧。
[name="贝纳尔多"]你的朋友们，从刚才开始似乎就很紧张。
[Character(name="avg_201_moeshd_1#15$1")]
[name="可颂"]总监先生，我无意冒犯，您说，正在排演的这出戏叫......
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]《德克萨斯之死》。
[Character(name="avg_103_angel_1#7$1")]
[name="能天使"]我从没听过比这更糟糕的，“玩笑”。
[Character(name="avg_npc_685_1#4$1")]
[name="贝纳尔多"]哦？看来你们对这个名字并不陌生？这在外乡人里可不常见。
[name="贝纳尔多"]叙拉古人不常说起这个名字，家族内的人更是讳莫如深。可是德克萨斯家族的故事......每个家族成员都必须铭记在心。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]它是一种告诫。
[Character(name="char_101_sora_1#4")]
[name="空"]......告诫。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]回到剧本吧，由德克萨斯家族的事迹改编而成的各种剧本不知凡几，但没有一个敢真正冠上“德克萨斯”这个名字。
[name="贝纳尔多"]他们更偏向于改编和化用，借助于隐射或戏仿。毕竟，剧作家们也不想给自己找麻烦。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]不过，时代在改变，对于如今的观众们而言，真实的历史总比披着假名的童话更有魅力，不是吗？
[Character(name="avg_npc_685_1#9$1")]
[name="贝纳尔多"]于是，一位了不起的人物把这部剧本带到了我们的面前。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]这是一出三幕剧。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]第一幕，在那个哥伦比亚刚刚建立的年代，诸多叙拉古的家族都向往着这块待开拓的土地。
[name="贝纳尔多"]于是，家族纷纷派出各自的队伍，加入了哥伦比亚拓荒的行列。
[name="贝纳尔多"]“那是一个混乱与机遇并存的时代，有的人被时代的浪潮吞没，而有的人，则站在了时代的先端。”
[name="贝纳尔多"]那之中的佼佼者，就是日后建立起了属于自己时代的萨尔瓦多雷·德克萨斯。
[Character(name="char_101_sora_1#4")]
[name="空"]（我知道德克萨斯不是她的名字，只是一个姓氏，但是......）
[name="空"]原来德克萨斯是叙拉古的家族？
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]确切地说，是发源自叙拉古，在哥伦比亚扎根的家族。
[name="贝纳尔多"]在哥伦比亚，这样的家族并不在少数。
[name="贝纳尔多"]老萨尔瓦多雷从始至终，都认为自己是一个叙拉古人。
[name="贝纳尔多"]叙拉古人也回报了他的坚持，始终以叙拉古人的方式尊重他。
[Character(name="char_101_sora_1#4")]
[name="空"]叙拉古人......
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]而第二幕，则是选取了他在哥伦比亚的奋斗史中最为人称道的几个片段。
[name="贝纳尔多"]在哥伦比亚历史的影子中，到处都有着叙拉古人的身影，而萨尔瓦多雷，也正是在这股时代浪潮中凝聚起了自己的家族。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]这一幕的内容，实际上也是最为众所周知的。
[name="贝纳尔多"]在数个版本中，这一幕的内容往往大同小异。
[name="贝纳尔多"]因为关于“那个在哥伦比亚的叙拉古人”的传记，你可以在书店里找到十几个版本，大部分是假托他名字的浪漫故事罢了。
[name="贝纳尔多"]可或许，也会有只言片语的真相。
[name="贝纳尔多"]如果你想读的话，我可以给你推荐几本不那么离谱的。
[Character(name="char_101_sora_1#1")]
[name="空"]啊，如果可以的话！ 
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]没问题。那么，第三幕，就是每个版本中，都会有巨大差异的部分了。
[Character(name="char_101_sora_1#4")]
[name="空"]因为涉及德克萨斯的......陨落吗？
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]没错。
[name="贝纳尔多"]关于德克萨斯的陨落，局外人只知道一件毫无疑问的事，那就是——
[Character(name="avg_npc_685_1#2$1")]
[name="贝纳尔多"]萨尔瓦多雷死于其子朱塞佩的谋杀，朱塞佩在那之后更是宣布德克萨斯家族将从叙拉古的家族体系中脱离。
[name="贝纳尔多"]这个举动惹怒了西西里夫人，并招致了西西里夫人的报复。
[name="贝纳尔多"]德克萨斯这个姓氏，在一夜之间销声匿迹。
[Character(name="char_101_sora_1#4")]
[name="空"]一夜之间......整个德克萨斯家族都消失了吗？！
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]至少每个叙拉古人都是这么相信的。
[name="贝纳尔多"]至于德克萨斯家的清算中具体发生了怎样的事，除了当事人谁都无从得知。
[Character(name="char_101_sora_1#4")]
[name="空"]但是......为什么我只看到两幕的剧本？
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]因为第三幕尚未完成。
[name="贝纳尔多"]关于这场清算，每个作者都会对这个过程展开不同的想象，并且得到完全不同的发展与结果。
[name="贝纳尔多"]而这份剧本的作者似乎正是在这方面陷入了瓶颈。
[name="贝纳尔多"]但前两幕的剧本内容已经十分优秀，所以，我还是毫不犹豫地把它买了下来。
[Character(name="char_101_sora_1#4")]
[name="空"]贝纳尔多先生，有没有可能，某一位德克萨斯家族的子嗣从那场清算中生还了呢？
[name="空"]她或许......或许成功离开了哥伦比亚，到了别的城市。
[name="空"]......比如说，龙门？
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]龙门？我记得，那是你们来的地方。
[Character(name="char_101_sora_1#4")]
[name="空"]......
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]据说，萨尔瓦多雷和他的儿子之间关系并不好。
[name="贝纳尔多"]但他却非常宠爱自己的孙女，甚至一度将自己的孙女送回了叙拉古，在萨卢佐家族中寄养了数年。
[name="贝纳尔多"]在德克萨斯被清算后，她也从此销声匿迹。
[Character(name="avg_npc_685_1#5$1")]
[name="贝纳尔多"]但实际上，关于她是否被卷入清算之中确实没有定论，据说当时在哥伦比亚，乃至在叙拉古边境都有人见到过她的身影。
[name="贝纳尔多"]于是，不同的德克萨斯故事中，关于她的结局往往也各不相同。
[Character(name="char_101_sora_1#4")]
[name="空"]......
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]据说，她有着德克萨斯家族标志性的黑发与橙色眼眸。
[Character(name="char_101_sora_1#3")]
[name="空"]如果，我是说如果！这位德克萨斯家族的末裔尚在人世，并且又一次回到了叙拉古的土地上......
[Character(name="char_101_sora_1#4")]
[name="空"]会发生什么？
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]这是个有意思的假设，任何一种发展都有可能。剧作家们往往根据逻辑来构建自己的剧本。
[name="贝纳尔多"]空小姐，遗憾的是，现实可不讲逻辑。
[Character(name="char_101_sora_1#4")]
[name="空"]......
[name="空"]据说，她正在一个名叫贝洛内的家族中，“做客”。
[name="空"]据说，贝洛内是这座城市中最有权势的家族。
[name="空"]据说，她......
[name="空"]据说她舍弃了一切前往那里，连告别都没来得及。
[Character(name="avg_npc_685_1#2$1")]
[name="贝纳尔多"]......
[Character(name="char_101_sora_1#4")]
[name="空"]我，我们，正是为了寻找她而来。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]可贵的勇气。
[name="贝纳尔多"]既然各位如此坦诚，又带来了我从没听说过的秘闻，那么，我也可以坦白告诉各位。
[Character(name="avg_npc_685_1#9$1")]
[name="贝纳尔多"]贝洛内家族和他们的客人确实常常光顾这家剧院，观赏本团这些不值一提的演出。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_101_sora_1#3")]
[name="空"]真的吗？！
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]巧合也罢，命运也罢，故事就是这么发生的，不是吗？
[name="贝纳尔多"]如果那位客人真的来访，我们剧团一定会用最大的热情欢迎她。
[name="贝纳尔多"]传言中，那是位沉默寡言，擅使双剑的人。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]她叫，切利尼娜·德克萨斯。
[stopmusic(fadetime=2)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g10_smallrestaurant",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[Delay(time=1)

... (全文21168字符)
```

### level_act21side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g4_srctheater",screenadapt="coverall")]
[Delay(time=1)]
[Character(name="char_101_sora_1#4",name2="avg_103_angel_1#7$1",focus=-1)]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_spotlight", volume=1)]
[bgeffect(name="$eb_spotlight_02",x=-200,layer = 1)]
[Blocker(a=0.2, r=0, g=0, b=0, fadetime=0.5, block=false)]
[Character(name="char_101_sora_1#4",name2="avg_103_angel_1#7$1",focus=1)]
[delay(time=1)]
[name="空"]你不明白他是什么样的人，我了解他。
[bgeffect(name="$eb_spotlight_02",x=200,layer = 1)]
[Character(name="char_101_sora_1#4",name2="avg_103_angel_1#7$1",focus=2)]
[name="能天使"]我们是不是太过相信自己有能力“了解”一个人了？我们是不是太容易被那些因感情和冲动而激发出的幻光蒙蔽了？
[bgeffect(name="$eb_spotlight_02",x=-200,layer = 1)]
[Character(name="char_101_sora_1#4",name2="avg_103_angel_1#7$1",focus=1)]
[name="空"]萨尔瓦多雷......他有资格走出哥伦比亚的暗巷。
[bgeffect(name="$eb_spotlight_02",x=200,layer = 1)]
[Character(name="char_101_sora_1#4",name2="avg_103_angel_1#5$1",focus=2)]
[name="能天使"]我的妹妹，他是个叙拉古人，你不明白他的手段。你以为他真的会帮助我们积累财富？
[name="能天使"]他只会引火烧身，连带我们一起。
[bgeffect(name="$eb_spotlight_02",x=-200,layer = 1)]
[Character(name="char_101_sora_1#4",name2="avg_103_angel_1#5$1",focus=1)]
[name="空"]他会用拳头保护自己，再用秩序约束拳头，这还不够吗？
[bgeffect(name="$eb_spotlight_02",x=200,layer = 1)]
[Character(name="char_101_sora_1#4",name2="avg_103_angel_1#2$1",focus=2)]
[name="能天使"]别说得这么浪漫。
[bgeffect(name="$eb_spotlight_02",x=-200,layer = 1)]
[Character(name="char_101_sora_1#4",name2="avg_103_angel_1#2$1",focus=1)]
[name="空"]不，哥哥。别的叙拉古人喜欢视血渍与伤口为勋章。
[name="空"]唯有他知道，血就是血。
[Dialog]
[bgEffect(layer = 1)]
[PlaySound(key="$d_avg_spotlightc", volume=1)]
[Character(name="char_101_sora_1#4",name2="avg_103_angel_1#2$1")]
[Delay(time=1)]
[StopMusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_101_sora_1#1",name2="avg_103_angel_1#10$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.6)]
[Character(name="char_101_sora_1#1",name2="avg_103_angel_1#10$1",focus=2)]
[name="能天使"]空，我演得怎么样？
[Character(name="char_101_sora_1#1",name2="avg_103_angel_1#10$1",focus=1)]
[name="空"]你想听实话吗？
[Character(name="char_101_sora_1#1",name2="avg_103_angel_1#10$1",focus=2)]
[name="能天使"]想听想听。
[Character(name="char_101_sora_1#5",name2="avg_103_angel_1#10$1",focus=1)]
[name="空"]糟透啦！能天使你果然不适合这个！
[Character(name="char_101_sora_1#5",name2="avg_103_angel_1#4$1",focus=2)]
[name="能天使"]欸，我觉得我还挺投入感情的啊。
[Character(name="char_101_sora_1#1",name2="avg_103_angel_1#4$1",focus=1)]
[name="空"]演戏也不光是投入感情就可以啦。
[name="空"]不过就对台本而言，还不错！起码几乎没有念错词。
[Character(name="char_101_sora_1#1",name2="avg_103_angel_1#3$1",focus=2)]
[name="能天使"]对我要求这么低吗？！
[Character(name="char_101_sora_1#1")]
[name="空"]可颂，你觉得怎么样？
[Character(name="avg_201_moeshd_1#1$1")]
[name="可颂"]我觉得很棒！
[name="可颂"]就是，刚才在表达对哥哥的不满的时候，是不是情绪应该下压一点？
[Character(name="char_101_sora_1#1")]
[name="空"]嗯，换一种表现方式吗......那我等一下试试。
[Character(name="avg_103_angel_1#4$1")]
[name="能天使"]哇哦，可颂，你什么时候这么懂行的。
[Character(name="avg_201_moeshd_1#1$1")]
[name="可颂"]不要小看每周都去给空探班的人好吗，我可不像某两位大忙人一样整天来无影去无踪的......
[Character(name="avg_103_angel_1#8$1")]
[name="能天使"]唔，但我可不会不告而别。
[Character(name="avg_201_moeshd_1#9$1")]
[name="可颂"]我不是那个......
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]不过，这是不是也说明了我们一定能找到她？
[Character(name="avg_201_moeshd_1#13$1")]
[name="可颂"]当然。
[Dialog]
[Character]
[PlaySound(key="$d_avg_shufflecards",channel="a", loop=true)]
[Delay(time=1.5)]
[stopsound(channel="a", fadetime=0)]
[name="？？？"]很有特色的表演。
[Character(name="char_101_sora_1#3")]
[name="空"]欸。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_694_1#1$1",fadetime=1)]
[Delay(time=2)]
[Character(name="char_101_sora_1#4")]
[name="空"]请问，您是......
[Character(name="avg_npc_694_1#5$1")]
[name="？？？"]我叫文索内希俄斯。
[Character(name="avg_103_angel_1#3$1")]
[name="能天使"]欸，文什么来着......
[Character(name="avg_npc_694_1#5$1")]
[name="文"]叫我文就好。
[Character(name="avg_103_angel_1#10$1")]
[name="能天使"]哦！文先生！
[Character(name="char_101_sora_1#4")]
[name="空"]请问，文先生，如果没有什么事的话，可以请您离开吗，我还在排练当中。
[Character(name="avg_npc_694_1#5$1")]
[name="文"]有事，我正在观赏一场演出，不是吗？
[Character(name="char_101_sora_1#4")]
[name="空"]我并不认为一个一边走路一边吃披萨的人是在观赏一场演出。
[Character(name="avg_npc_694_1#5$1")]
[name="文"]存在观赏时不能吃披萨的规定吗？
[Character(name="avg_103_angel_1#8$1")]
[name="能天使"]唔，剧院有类似的规定吧？
[Character(name="avg_npc_694_1#5$1")]
[name="文"]那也只是剧院对人的规定，不是歌舞剧对人的规定。
[name="文"]规范使人在表面上拥有了对事物相同的敬畏，虚假的高台于是拔地而起，真正的敬畏却反而难见踪影。
[Character(name="avg_103_angel_1#4$1")]
[name="能天使"]啊？
[Character(name="avg_npc_694_1#5$1")]
[name="文"]要吃吗，小姑娘。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]要！
[Dialog]
[PlaySound(key="$d_avg_humaneat", volume=0.6)]
[characteraction(name="middle", type="move", xpos=-20, fadetime=0.3, block=false)]
[Delay(time=0.3)]
[characteraction(name="middle", type="move", xpos=20, fadetime=0.3, block=false)]
[Delay(time=1)]
[Character(name="avg_103_angel_1#4$1")]
[name="能天使"]呜哇，口感好差！
[Character(name="avg_npc_694_1#5$1")]
[name="文"]毕竟这是街边最便宜的披萨。但是，酱料的滋味其实很不错。
[Character(name="char_101_sora_1#5")]
[name="空"]......那么，您既然旁观了刚才的演出，对我的表演有何评价？
[Character(name="avg_npc_694_1#5$1")]
[name="文"]这其中的重点在于你所擅长的捕捉情感与表达情感的方式与歌舞剧的方式有一些差异。
[name="文"]你很显然习惯于舞台，或者说，你太习惯于舞台了，这反而让你难以作为一名歌舞剧演员站在舞台上。
[name="文"]这很显然并不怪你，不过，这也是你必须跨过的考验。
[Character(name="avg_103_angel_1#4$1")]
[name="能天使"]哇，大叔，看不出来你还挺专业的嘛。
[StopMusic(fadetime=2)]
[Dialog]
[Character]
[Character(name="avg_npc_694_1#5$1",fadetime=1)]
[Delay(time=1)]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[Delay(time=2)]
[name="文"]思考一下，你，一个哥伦比亚富商的女儿。他，萨尔瓦多雷，来自叙拉古的无业游民。
[name="文"]他和你见过的所有男人都不一样，他对你的身份不屑一顾，却又对你关照连连。
[name="文"]他比所有人都懒惰，却又比所有人都精明。
[name="文"]他仿佛命中注定要成为一个家族的领袖，走上一条无法回头的危险道路。
[Character(name="avg_npc_694_1#3$1")]
[name="文"]告诉我，小姐，你爱这样一

... (全文30016字符)
```

### level_act21side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g4_srctheater",screenadapt="coverall")]
[Delay(time=1)]
[Character(name="char_101_sora_1#5")]
[playMusic(intro="$dignified_intro",key="$dignified_loop", volume=0.6)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_spotlight", volume=1)]
[bgeffect(name="$eb_spotlight_02",layer = 1)]
[Blocker(a=0.2, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="空"]德克萨斯。
[Character(name="char_101_sora_1#4")]
[name="空"]萨尔瓦多雷·德克萨斯。我该如何面对你？我该相信你吗？
[name="空"]你是一个叙拉古人，他们说，你从骨子里就浸透了暴力与野心。你和你的家族会彻底吞噬这里......吞噬哥伦比亚。
[name="空"]你在我面前所表现出来的，是真正的你吗？你看上去明明那么优雅，那么得体......
[name="空"]可是，我也看见过你挥拳的样子，指缝间流淌下鲜血，你的对手再也无法发出一声詈骂。
[name="空"]哪一边是真正的你，萨尔瓦多雷？
[name="空"]会不会有一天，你最终意识到这两者无法相容？会不会有一天，你身后的血迹终将追上你？
[name="空"]到那时，你会做何选择？
[name="空"]到那时......你还会留在我的身边吗？
[Dialog]
[bgEffect(layer = 1)]
[PlaySound(key="$d_avg_spotlightc", volume=1)]
[Delay(time=1)]
[StopMusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Character(fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[Delay(time=1)]
[Character(name="avg_npc_685_1#8$1",fadetime=0.5)]
[Delay(time=1)]
[name="贝纳尔多"]漂亮的演出，空小姐。
[name="贝纳尔多"]毫无疑问，你又一次给了我惊喜。
[Character(name="char_101_sora_1#1")]
[name="空"]这其实要感谢剧团里一位叫做文的先生，如果不是他的指导，我也做不到马上调整自己。
[Character(name="avg_npc_685_1#4$1")]
[name="贝纳尔多"]文？
[name="贝纳尔多"]我倒是没有听说过，在这座米兰剧场里，有这样一位人物。
[Character(name="char_101_sora_1#3")]
[name="空"]欸？
[name="空"]他对歌舞剧十分了解，给了我很好的指导，我还以为是剧团的重要人物呢。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]......没有印象。不过，对于歌舞剧有心得的人数不胜数，或许他也只是其中之一吧。
[name="贝纳尔多"]比起这个，空小姐，我有一个在见到你的简历时就产生了的疑问，不知道你能不能为我解惑？
[Character(name="char_101_sora_1#1")]
[name="空"]可以呀。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]你在龙门走的是偶像路线。
[name="贝纳尔多"]我们与龙门的合作在如今愈发频繁，但双方的演艺事业却由于各自底蕴的不同而呈现出了一种竞争的状态。
[name="贝纳尔多"]在这样的前提下，塞壬唱片发给我的那些试镜片段，却证明你在歌舞剧方面并非毫无实力。
[name="贝纳尔多"]这意味着你的野心并不局限于龙门。
[name="贝纳尔多"]是什么让你如此努力？
[Character(name="char_101_sora_1#5")]
[name="空"]......原因，有很多吧。
[name="空"]但是最开始，我的想法其实也没有很复杂，我只是希望，能够追上一个人而已。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]哦？
[Character(name="char_101_sora_1#5")]
[name="空"]嘿，就像这个剧本里写的一样。
[Character(name="char_101_sora_1#4")]
[name="空"]每当她偶尔看向天空，看向门外，看向空旷的街道时，她的眼神......
[name="空"]让我觉得，她总有一天会离开我们，离开龙门。
[name="空"]“到那时，你会做何选择？”
[StopMusic(fadetime=2)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g6_newtown_street",screenadapt="coverall")]
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_683_1#9$1")]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[playsound(key="$d_avg_rainlight_loop", loop=true, channel="a")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_683_1#9$1",focus=1)]
[name="德克萨斯"]......
[Dialog]
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_683_1#9$1")]
[characteraction(name="left", type="move", xpos=100, fadetime=0.7, block=false)]
[Delay(time=0.5)]
[characteraction(name="right", type="move", xpos=-50, fadetime=0.5, block=true)]
[Delay(time=0.8)]
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_683_1#9$1",focus=2)]
[name="拉普兰德"]别急，我们两个能在叙拉古重逢，你不觉得是一种奇迹吗？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_683_1#9$1",focus=1)]
[name="德克萨斯"]我现在有事。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_683_1#9$1",focus=2)]
[name="拉普兰德"]巧了，我也有事。
[name="拉普兰德"]保护这个人是你的任务吗？
[Character]
[Character(name="avg_npc_698_1#1$1",name2="char_empty")]
[characteraction(name="left", type="move", xpos=200, fadetime=0, block=false)]
[name="贝洛内家护卫"]你是什么......
[Dialog]
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_683_1#1$1",fadetime=0.3)]
[characteraction(name="right", type="move", xpos=300, fadetime=0, block=true)]
[Delay(time=0.2)]
[characteraction(name="right", type="move", xpos=-350, fadetime=0.4, block=true)]
[PlaySound(key="$p_skill_soulwolf")]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.3, block=false)]
[Character(name="avg_1028_texas2_1#7$2",name2="avg_npc_683_1#1$1",fadetime=0.1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[characteraction(name="left", type="move", xpos=100, fadetime=0.3, block=true)]
[Blocker(a=0.3, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Effect(name="$e_spark_01_mid",layer=1)]
[CameraShake(duration=2, xstrength=15, ystrength=15, vibrato=40, randomness=90, fadeout=true, block=false)]
[Effect(name="$e_spark_01_large",layer=2)]
[Effect(name="$e_spark_02_mid",layer=3,delay=0.2)]
[Effect(name="$e_spark_02_mid",roy=-180,layer=4,delay=0.3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=false)]
[Delay(time=2)]
[Character(name="avg_npc_698_1#1$1")]
[name="贝洛内家护卫"]噫......！
[Character(name="avg_1028_texas2_1#7$2",name2="avg_npc_683_1#9$1",focus=2)]
[name="拉普兰德"]真是不解风情，你说是吧，德克萨斯。
[Character(name="avg_1028_texas2_1#7$2",name2="avg_npc_683_1#9$1",focus=1)]
[name="德克萨斯"]你们去保护目标，我来应付她。
[Character(name="avg_npc_698_1#1$1")]
[name="贝洛内家护卫"]是，是！
[Dialog]
[PlaySound(key="$d_avg_shallowsrun")]
[Character(fadetime=0.5)]
[Delay(time=2)]
[Character(name="avg_1028_texas2_1#7$2",name2="avg_npc_683_1#9$1",fadetime=1)]
[Delay(time=2)]
[Character(name="avg_1028_texas2_1#7$2",name2="avg_npc_683_1#9$1",focus=2)]
[name="拉普兰德"]所以，你要吃千层酥吗？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_683_1#9$1",fadetime=1,focus=1)]
[name="德克萨斯"]......给我一块。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_683_1#9$1",focus=2)]
[name="拉普兰德"]哈，这就对了！
[name="拉普兰德"]德克萨斯，不，在叙拉古，是不是叫你切利尼娜更合适？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_683_1#9$1",focus=1)]
[name="德克萨斯"]免了。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_683_1#9$1",focus=2)]
[name="拉普兰德"]好吧，说实话，我也更习惯这么叫你了，习惯的力量真可怕，不是吗？
[name="拉普兰德"]在龙门过着悠哉的生活，偶尔在

... (全文34934字符)
```

### level_act21side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g11_mansionhall",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[PlaySound(key="$d_avg_clothmovement",volume=0.5)]
[Character(name="avg_427_vigil_1#2$1",fadetime=1)]
[Delay(time=2)]
[name="莱昂图索"]这里是......
[Character(name="avg_npc_690_1#1$1")]
[name="德米特里"]你终于醒了。
[Character(name="avg_427_vigil_1#7$1")]
[name="莱昂图索"]这里是......家里？
[name="莱昂图索"]德米特，你怎么在这？
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#8$1",focus=2)]
[name="德米特里"]是拉维妮娅小姐把你送回来的。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#9$1",focus=2)]
[name="德米特里"]根据医生的诊断，你是因为心力交瘁加上受伤，所以昏倒了。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#9$1",focus=1)]
[name="莱昂图索"]......
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#9$1",focus=1)]
[name="莱昂图索"]啧。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#1$1",focus=2)]
[name="德米特里"]吃苹果吗？
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#1$1",focus=1)]
[name="莱昂图索"]吃。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#1$1",focus=2)]
[name="德米特里"]就知道你想吃，已经给你削好了。
[Dialog]
[characteraction(name="right", type="move", xpos=-70, fadetime=0.8, block=false)]
[Delay(time=1)]
[characteraction(name="right", type="move", xpos=70, fadetime=0.6, block=false)]
[Delay(time=1)]
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#1$1",focus=1)]
[name="莱昂图索"]拉维妮娅呢？
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#9$1",focus=2)]
[name="德米特里"]她把你交给护卫就走了。
[name="德米特里"]你也知道，她向来是不愿意踏入这间宅邸的。
[name="德米特里"]为了你来一趟已经是奇迹了。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#9$1",focus=1)]
[name="莱昂图索"]......
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#3$1",focus=2)]
[name="德米特里"]卡拉奇的死，确实是个不小的麻烦。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#8$1",focus=2)]
[name="德米特里"]而你受伤的消息肯定也传出去了。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#7$1",focus=2)]
[name="德米特里"]现在，从其他家族的视角看，贝洛内家一瞬间从稳操胜券变成了内忧外患的状态。
[name="德米特里"]随时都可能有人来咬我们一口。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#7$1",focus=1)]
[name="莱昂图索"]袭击我的那帮人，有没有留下活口？
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#3$1",focus=2)]
[name="德米特里"]很遗憾。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#9$1",focus=2)]
[name="德米特里"]而且他们的尸体上也没有留下任何线索。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#9$1",focus=1)]
[name="莱昂图索"]我猜也是。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#9$1",focus=2)]
[name="德米特里"]你觉得会是谁？
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#9$1",focus=1)]
[name="莱昂图索"]萨卢佐一直没有出手，他们是在等待时机，这对他们来说，显然是一个好机会。
[name="莱昂图索"]罗塞蒂......虽然瓦拉赫跟我一起遇袭，他们似乎也是受害者......
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#8$1",focus=2)]
[name="德米特里"]但是哥伦比亚家族从来都不是铁板一块。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#8$1",focus=1)]
[name="莱昂图索"]对，他们起内讧的可能性是存在的。
[name="莱昂图索"]而且，也不是没有别的可能性。
[Character(name="avg_427_vigil_1#6$1",name2="avg_npc_690_1#8$1",focus=1)]
[name="莱昂图索"]啧，真是挑了个好时机。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#8$1",focus=1)]
[name="莱昂图索"]给我倒点水吧。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#1$1",focus=2)]
[name="德米特里"]你这家伙，躺在床上倒是比平时还会发号施令。
[Dialog]
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#1$1")]
[PlaySound(key="$pourwater")]
[Delay(time=3)]
[PlaySound(key="$d_avg_chess")]
[Delay(time=1)]
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#1$1",focus=1)]
[Delay(time=1)]
[name="莱昂图索"]......你就一定要端一杯开水给我？
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#1$1",focus=2)]
[name="德米特里"]是不是该怪你下达的命令不够准确呢？
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#1$1",focus=1)]
[name="莱昂图索"]......好吧，你总是用这种方法来表达不满，这次又是什么事？
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#3$1",focus=2)]
[name="德米特里"]对德克萨斯的安排，我没法同意。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#3$1",focus=1)]
[name="莱昂图索"]拉维妮娅是个公正的人，她不会诬陷任何一个清白的人，她有她的考虑。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#7$1",focus=2)]
[name="德米特里"]不，我是说，她原本应该成为你的武器。
[name="德米特里"]首领既然把她交给你，就有她不会危害家族的把握。
[name="德米特里"]你应该把她打造成一把利器。
[name="德米特里"]而现在，她却被拉维妮娅关了起来。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#7$1",focus=1)]
[name="莱昂图索"]别告诉我，你看不出她也是为了我们家族考虑。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#8$1",focus=2)]
[name="德米特里"]我承认，在如今这么危险的情况下，还握着德克萨斯这颗烫手山芋，会让你的处境更加岌岌可危。
[name="德米特里"]她的姓氏再度在叙拉古的土地上出现......实在是太惹眼了。
[name="德米特里"]确实，以拉维妮娅的立场，德克萨斯握在她的手上会更加安全。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#7$1",focus=2)]
[name="德米特里"]但我们家族内部的人，他们会怎么想？
[name="德米特里"]他们会觉得，你，贝洛内家的大少爷莱昂图索，已经太沉迷于在桌布上过家家的游戏，你变得软弱了。
[name="德米特里"]你甚至用不好一把刀，还丢失了它。
[name="德米特里"]贝洛内家已经落入下风，不论想找麻烦的是谁，我们都应该强硬地回击。
[name="德米特里"]莱昂，沃尔西尼的新城区不光是你在的建设部的什么无聊“事业”，它该属于贝洛内家。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#7$1",focus=1)]
[name="莱昂图索"]......
[name="莱昂图索"]所以这才是你的真心话。
[name="莱昂图索"]我也有我的考虑，德米特。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#9$1",focus=2)]
[name="德米特里"]愿闻其详。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#9$1",focus=1)]
[name="莱昂图索"]......
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#9$1",focus=1)]
[name="莱昂图索"]好吧，你是我最好的兄弟，也是我的顾问。
[name="莱昂图索"]在遇袭的时候我就感觉到有些不对了，在听到卡拉奇死后，我就更加明确了这个想法。
[name="莱昂图索"]你刚才问我觉得是谁下的手。
[name="莱昂图索"]实际上我不觉得是萨卢佐或者罗塞蒂的人干的。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#8$1",focus=2)]
[name="德米特里"]为什么？
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#8$1",focus=1)]
[name="莱昂图索"]下手的人太了解我了。
[name="莱昂图索"]他知道怎么样才能快速而且精确地打击到贝洛内，同时也能打击到我。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#5$1",focus=2)]
[name="德米特里

... (全文21610字符)
```

### level_act21side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g6_newtown_street",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_103_angel_1#1$1",name2="avg_201_moeshd_1#1$1",fadetime=1)]
[delay(time=2)]
[Character(name="avg_103_angel_1#4$1",name2="avg_201_moeshd_1#1$1",focus=1)]
[name="能天使"]哇哦，这套礼服看起来好漂亮啊。
[Character(name="avg_103_angel_1#4$1",name2="avg_201_moeshd_1#1$1",focus=2)]
[name="可颂"]嗯，空穿上一定很好看。
[Character(name="avg_103_angel_1#1$1",name2="avg_201_moeshd_1#1$1",focus=1)]
[name="能天使"]早知道我也答应当演员就好了。
[Character(name="avg_103_angel_1#1$1",name2="avg_201_moeshd_1#5$1",focus=2)]
[name="可颂"]你不行的啦，能天使你完全不懂什么叫演技。
[Character(name="avg_103_angel_1#10$1",name2="avg_201_moeshd_1#5$1",focus=1)]
[name="能天使"]但我可以本色演出啊。
[Character(name="avg_103_angel_1#10$1",name2="avg_201_moeshd_1#6$1",focus=2)]
[name="可颂"]叙拉古根本就没有萨科塔可以让你扮演啦！
[Character(name="avg_103_angel_1#4$1",name2="avg_201_moeshd_1#6$1",focus=1)]
[name="能天使"]谁说的，我就听说，那个西西里夫人身边就有一个——
[Dialog]
[Delay(time=1)]
[StopMusic(fadetime=2)]
[Character(name="avg_103_angel_1#1$1",name2="avg_201_moeshd_1#6$1",focus=1)]
[name="能天使"]嗯？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Background(image="33_g5_srcpark",screenadapt="coverall")]
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="轻佻的家族成员"]莎莉小姐，我们老大请你现在过去用餐。
[Character(name="avg_npc_175")]
[name="女演员"]这......但是......
[Character(name="avg_npc_031")]
[name="严肃的护卫"]莎莉小姐正要去剧场，滚开。
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="轻佻的家族成员"]我们老大现在就想见莎莉小姐，晚点再去剧场也一样吧。
[Character(name="avg_npc_175")]
[name="女演员"]我、我要去找总监......
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="轻佻的家族成员"]总监？放在以前，我可能会卖他的面子，但是现在嘛......
[Character(name="avg_npc_175")]
[characteraction(name="middle", type="move", xpos=-50, fadetime=1,block=true)]
[name="女演员"]那个，请不要......
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",focus=2)]
[name="愤怒的家族成员"]还跟他们客气什么？
[name="愤怒的家族成员"]我们老大想见你是你的荣幸，不想吃苦头的话就乖乖跟我们来。
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="轻佻的家族成员"]等等，老大没让我们......
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",focus=2)]
[name="愤怒的家族成员"]大哥的意思你还不明白吗，之前我们都是忌惮贝洛内。
[name="愤怒的家族成员"]现在既然贝洛内不行了，大人物们又要洗牌了，这是我们的机会！
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="轻佻的家族成员"]说的也是，弟兄们，把这些碍眼的家伙都给解决了！
[Character(name="avg_npc_031",name2="avg_npc_031",focus=1)]
[name="严肃的护卫"]啧，保护莎莉小姐！
[Dialog]
[Character]
[Character(name="avg_npc_031",name2="avg_npc_698_1#1$1")]
[characteraction(name="left", type="move", xpos=-100, fadetime=0, block=false)]
[characteraction(name="left", type="move", xpos=150, fadetime=0.5, block=false)]
[characteraction(name="right", type="move", xpos=-100, fadetime=0.5, block=false)]
[Delay(time=0.5)]
[playsound(key="$d_avg_knife",volume=0.7)]
[playsound(key="$knifegore",volume=0.7,delay=0.1)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.03, block=true)]
[playsound(key="$swordtsing5",delay=0.2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.01, block=true)]
[CameraShake(duration=1.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="left", type="move", xpos=-300, fadetime=0.3, block=false)]
[characteraction(name="right", type="move", xpos=30, fadetime=0.3, block=false)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g6_newtown_street",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_empty",name2="avg_201_moeshd_1#11$1",focus=2)]
[name="可颂"]能天使，怎么......欸，人呢？
[Character(name="char_101_sora_1#2")]
[name="空"]她已经冲上去了，我们也去帮忙！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.6)]
[Background(image="33_g5_srcpark",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_031")]
[characteraction(name="left", type="shake", power=10, times=100, fadetime=0.5, block=false)]
[Delay(time=0.5)]
[name="严肃的护卫"]唔......
[Dialog]
[characteraction(name="middle", type="move", ypos=-50, fadetime=0.8,block=false)]
[playsound(key="$bodyfalldown1")]
[Character(fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="轻佻的家族成员"]哼，这点水平也来当护卫？
[Character(name="avg_npc_175")]
[name="女演员"]......呜呜。
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="轻佻的家族成员"]莎莉小姐，请吧。
[Character(name="avg_npc_175")]
[name="女演员"]我、我知道了......
[Dialog]
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1")]
[PlaySound(key="$p_atk_smg_n")]
[characteraction(name="right", type="shake", power=10, times=100, fadetime=0.8, block=false)]
[Delay(time=0.8)]
[playsound(key="$bodyfalldown1")]
[Character(name="avg_npc_698_1#1$1",name2="char_empty",fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_npc_175")]
[name="女演员"]欸，你们是——
[Character(name="avg_npc_698_1#1$1")]
[name="轻佻的家族成员"]什么人？！
[Dialog]
[PlaySound(key="$p_atk_smg_h")]
[characteraction(name="middle", type="shake", power=10, times=100, fadetime=1, block=true)]
[Delay(time=1)]
[playsound(key="$bodyfalldown1")]
[Character(fadetime=0.5)]
[Delay(time=1)]
[Character(name=

... (全文36902字符)
```

### level_act21side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g5_srcpark",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_690_1#7$1",name2="avg_npc_698_1#1$1",fadetime=0.5)]
[Delay(time=0.5)]
[Character(name="avg_npc_690_1#7$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="德米特里"]......她为什么会出现在这里？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_690_1#7$1",name2="avg_npc_698_1#1$1",focus=2)]
[name="护卫"]是、是德克萨斯！
[name="护卫"]我们的人损失惨重！
[Character(name="avg_npc_690_1#9$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="德米特里"]啧，不该放任拉维妮娅和那个废物聊那么久的。
[name="德米特里"]算了，看到彻底堕落的同行，那女人的精神也完了。
[name="德米特里"]只要能熄灭莱昂那点幼稚，过程怎么样不重要。
[name="德米特里"]招呼我们的人，走了。
[StopMusic(fadetime=2)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_697_1#1$1",fadetime=0.5)]
[Delay(time=0.5)]
[name="书记员"]他......他们已经离开了！
[Dialog]
[Character(name="avg_4065_judge_1#6$1")]
[Delay(time=2)]
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]他已经死了，箭头贯穿了他的心脏。
[Character(name="avg_4065_judge_1#11$1")]
[name="拉维妮娅"]感谢你们，否则死在这里的就是我了。
[Character(name="avg_4065_judge_1#6$1")]
[name="拉维妮娅"]合上眼睛吧，杀手。
[Dialog]
[characteraction(name="middle", type="move", ypos=-30, fadetime=0.7, block=false)]
[Delay(time=1)]
[characteraction(name="middle", type="move", ypos=30, fadetime=0.7, block=false)]
[Delay(time=1)]
[Character(name="avg_4065_judge_1#4$1")]
[playsound(key="$book_close")]
[name="拉维妮娅"]这是......?
[Character(name="avg_1028_texas2_1#3$1")]
[name="德克萨斯"]一个本子？
[Character(name="avg_4065_judge_1#6$1")]
[name="拉维妮娅"]......
[name="拉维妮娅"]叙拉古的法官证，放在他胸口的口袋里。
[playsound(key="$d_avg_paper2")]
[name="拉维妮娅"]已经被剪了角，上面写，它的主人在三年前因为渎职而被吊销了法官资格。
[Character(name="avg_4065_judge_1#14$1")]
[name="拉维妮娅"]渎职，哈，渎职。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_4065_judge_1#15$1")]
[name="拉维妮娅"]他们当时就不能找个更体面的借口吗？
[Character(name="avg_1028_texas2_1#6$1")]
[name="德克萨斯"]你还好吗？
[Dialog]
[Character(name="avg_4065_judge_1#2$1")]
[Delay(time=1)]
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]......我似乎应该先问你为什么能从监狱里出来。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]......
[name="德克萨斯"]企业机密。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]好吧，现在我也没有力气追究这个了。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]你很需要休息。
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]但我还不能休息。
[name="拉维妮娅"]这条线索断了，我还要去找别的线索。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]炎国有一句谚语，叫“欲速则不达”。
[Character(name="avg_4065_judge_1#5$1")]
[name="拉维妮娅"]......我当然知道这个道理。
[name="拉维妮娅"]但是，我没有那么多时间了。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]卡拉奇对你来说，是个很重要的人吗？
[Character(name="avg_4065_judge_1#8$1")]
[name="拉维妮娅"]......不。
[name="拉维妮娅"]我和卡拉奇部长并没有见过几次。
[name="拉维妮娅"]毕竟我是法官，和他在职能上相差很远。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]但是，凡是沃尔西尼的居民都知道，他是一个非常具有活力的人，圆滑地处理着和家族的关系。
[name="拉维妮娅"]他花费了全部的精力在新城区的建设上，用尽各种手段来保证市民们能有一个比较安全的地方。
[name="拉维妮娅"]因为调查他的死，我开始真正了解这个人。
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]战战兢兢，如履薄冰，绞尽脑汁用手头上能交换的一切，来博得一点点能做事的空间。
[name="拉维妮娅"]比如，在远离家族利益纷争的区块多建几所学校，多建几所医院......
[Character(name="avg_4065_judge_1#6$1")]
[name="拉维妮娅"]我不知道该怎么评价他，或许，只是个有点良心的好人吧。
[name="拉维妮娅"]但好人在叙拉古的结局是注定的。
[Character(name="avg_1028_texas2_1#5$1")]
[name="德克萨斯"]......和这个揣着法官证的杀手一样。
[Character(name="avg_4065_judge_1#6$1")]
[name="拉维妮娅"]叙拉古是有正规的法律学校的。
[name="拉维妮娅"]使用的是哥伦比亚出版的教材，毕业后，不仅可以在叙拉古本地的法律机构任职。
[name="拉维妮娅"]也拥有被哥伦比亚承认的资质。
[name="拉维妮娅"]如今，我们和龙门的来往也越来越频繁了，再过一段时间，炎国可能也会承认这方面的资质。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]听起来是一件好事。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]是啊，当然是好事。
[name="拉维妮娅"]但是，这不会影响任何事情。
[name="拉维妮娅"]我的母校曾经邀请过我回去为学弟学妹们演讲，给他们一些信心。
[name="拉维妮娅"]我去了。
[name="拉维妮娅"]但是，当我站上台的时候，我发现，我没有办法告诉他们，相信自己学到的东西。
[Character(name="avg_4065_judge_1#8$1")]
[name="拉维妮娅"]......
[name="拉维妮娅"]法律之所以生效，在叙拉古，竟然是因为一个人的存在，而不是它真的基于一种被认可的公平。
[name="拉维妮娅"]某种意义上，这比无法之地还要荒唐。
[name="拉维妮娅"]而叙拉古人居然真的在这种环境下生活了将近六十年，以至于当所有人都习惯之后，没有人再敢质疑这一切。
[Character(name="avg_4065_judge_1#14$1")]
[name="拉维妮娅"]我是公正的化身吗？不，我是一个化身，但连我自己也不知道，我的背后是什么。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]......要去吃点东西吗？
[Character(name="avg_4065_judge_1#11$1")]
[name="拉维妮娅"]......要的。
[name="拉维妮娅"]谢谢。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g10_smallrestaurant",screenadapt="coverall")]
[Character(name="avg_427_vigil_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]我没想到你会在这，莱昂。
[Character(name="avg_427_vigil_1#1$1",name2="avg_4065_judge_1#1$1",focus=1)]
[name="莱昂图索"]我听说你遭到了袭击，就赶来了。
[Character(name="avg_427_vigil_1#1$1",name2="avg_4065_judge_1#1$1",focus=2)]
[name="拉维妮娅"]没出什么大事，德克萨斯帮了我。
[name="拉维妮娅"]只是线索断了。
[Dialog]
[StopMusic(fadetime=1)]
[Character(name="avg_427_vigil_1#1$1",name2="avg_4065_judge_1#1$1",focus=1)]
[Delay(time=2)]
[name="莱昂图索"]收手吧，拉维妮娅。
[Character(name="avg_427_vigil_1#1$1",name2="avg_4065_judge_1#2$1",focus=2)]
[PlayMusic(intro="$m_bat_imprisonment_intro", key="$m_bat_imprisonment_loop", volume=0.6)]
[name="拉维妮娅"]......莱昂，我们应该有过约定，不在吃饭时聊会吵架的事。
[Character(name="avg_427_vigil_1#1$1",name2="avg_4065_judge_1#2$1",focus=1)]
[name="莱昂图索"]现在不是说这个的时候。
[Character(name="avg_427_vigil_1#1$1",name2="avg_4065_judge_1#1$1",focus=2)]
[name="拉维妮娅"]不，这是我们唯一能无视各自的立场坐在一起吃饭的方法。
[name="拉维妮娅"]如果你打算打破这个约定，那我就先告辞了，莱昂图

... (全文12131字符)
```

### level_act21side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g4_srctheater",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_103_angel_1#1$1",fadetime=0.5)]
[delay(time=0.5)]
[name="能天使"]空，好了没啊。
[Character]
[name="空"]别催了啦！
[name="空"]呜呜，这衣服好紧！
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]你不会偷偷背着我吃披萨吃胖了吧。
[Character]
[name="空"]怎么可能啦！只是昨天晚上多吃了一片而已！
[name="可颂"]空，吸气！
[name="空"]嘶——
[name="可颂"]好嘞！完美！
[name="可颂"]好啦。
[Character(name="avg_103_angel_1#4$1")]
[name="能天使"]好了吗？快出来看看。
[Character]
[name="空"]来了来了。
[Dialog]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_npc_684_1#9$1",fadetime=1)]
[delay(time=3)]
[Character(name="avg_103_angel_1#10$1")]
[name="能天使"]哇哦，好漂亮啊。
[Character(name="avg_201_moeshd_1#1$1")]
[name="可颂"]真的，简直是完美。
[Character(name="avg_npc_684_1#3$1")]
[name="空"]嘿嘿。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]唉，要是德克萨斯那家伙也能看到就好了。
[Character(name="avg_npc_684_1#9$1")]
[name="空"]是啊。
[Character(name="avg_201_moeshd_1#6$1")]
[name="可颂"]真不愧是空，这么快就能在叙拉古的舞台上获得演出机会。
[Character(name="avg_npc_684_1#3$1")]
[name="空"]那当然~
[Character(name="avg_npc_684_1#9$1")]
[name="空"]《德克萨斯之死》这次采用了分幕演出的形式，第一幕已经顺利排练完成了，后天就要演出了！
[name="空"]要是顺利的话，说不定不是我去找她，反而变成她来找我了呢。
[Character(name="avg_103_angel_1#6$1")]
[name="能天使"]有可能欸，我想想，到时候我一定要买个披萨拍她脸上。
[Character(name="avg_201_moeshd_1#13$1")]
[name="可颂"]说到德克萨斯，我最近也一直在打听贝洛内家族的事，这个家族最近的状况好像有点不太好，希望她没有受到什么影响。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]那家伙肯定没事的。
[Character(name="avg_201_moeshd_1#13$1")]
[name="可颂"]嗯，现在也只能相信她了。
[Character(name="avg_201_moeshd_1#8$1")]
[name="可颂"]空的舞台首秀之前，我们可以好好休息一下。
[Character(name="avg_103_angel_1#3$1")]
[name="能天使"]原本还想在这座城市里多逛逛的，结果感觉我都成了空的贴身保镖了。
[Character(name="avg_npc_684_1#5$1")]
[name="空"]怪我哦。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]但是剧场的免费伙食被我蹭了不少，嘿嘿，披萨味道真不错。
[name="能天使"]感觉之后也会变得更忙，我们去到处走走吧。
[Character(name="avg_npc_684_1#9$1")]
[name="空"]嗯。
[Character]
[name="活泼的女演员"]哎，你听......吗？
[name="好事的女演员"]你说的是......德克......对吧？
[Character(name="avg_npc_684_1#1$1")]
[name="空"]嗯？
[Character]
[StopMusic(fadetime=2)]
[name="活泼的女演员"]对，德克萨斯......判......
[Character(name="avg_npc_684_1#7$1")]
[name="空"]欸。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlayMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.6)]
[Character(name="avg_npc_684_1#9$1",fadetime=0.5)]
[Delay(time=0.5)]
[name="空"]你好，请问你们刚才是不是提到了德克萨斯？
[Character(name="avg_npc_175")]
[name="活泼的女演员"]啊，对啊，你也感兴趣吗？
[Character(name="avg_npc_684_1#9$1")]
[name="空"]德克萨斯怎么了？
[Character(name="avg_npc_175")]
[name="活泼的女演员"]我也是听我贝洛内家族的男朋友说的。
[name="活泼的女演员"]前几天建设部部长不是遇害了吗？
[name="活泼的女演员"]好像凶手已经被找到了。
[name="活泼的女演员"]是那个德克萨斯家族最后的血脉，好像叫做什么切利尼娜的。
[Character(name="avg_npc_684_1#5$1")]
[name="空"]......
[CameraShake(duration=0.3,xstrength=20,ystrength=20,vibrato=30,randomness=90,fadeout=true,block=false)]
[name="空"]这怎么可能！
[StopMusic(fadetime=3)]
[Character(name="avg_npc_175")]
[name="活泼的女演员"]开庭的日子也已经决定了，就在后天。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g11_mansionhall",screenadapt="coverall")]
[PlayMusic(intro="$loading_intro", key="$loading_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#5$1",fadetime=0.5)]
[delay(time=1)]
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]莱昂图索少爷，我们约好的这场会面，可被你拖了好几次。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#5$1",focus=1)]
[name="莱昂图索"]实在抱歉，瓦拉赫先生，最近要我处理的事有些太多了。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]我听说你们让手下撤出了不少之前和其他家族有摩擦的地盘，正在担心你呢。
[name="瓦拉赫"]看到你没事，我就放心了。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#5$1",focus=1)]
[name="莱昂图索"]只是一点止损罢了。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]哈哈，我就喜欢你这种谨慎的性格。
[name="瓦拉赫"]放心，罗塞蒂家对趁人之危不感兴趣。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]不过，有个问题，我不吐不快。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_695_1#1$1",focus=1)]
[name="莱昂图索"]想必是德克萨斯的事。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]“切利尼娜·德克萨斯”，她回来了，还是你的护卫？
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_695_1#6$1",focus=2)]
[name="瓦拉赫"]真的是她本人？
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#6$1",focus=1)]
[name="莱昂图索"]如果我说是呢？
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]......
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#2$1",focus=2)]
[name="瓦拉赫"]我们从来都不知道，她原来还活着。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#2$1",focus=1)]
[name="莱昂图索"]......当年，是我父亲保下了她。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#3$1",focus=2)]
[name="瓦拉赫"]原来如此，原来如此，是他老人家的手笔。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#3$1",focus=1)]
[name="莱昂图索"]这座新城市的建造，本来也是因萨尔瓦多雷与叙拉古的缘分而起，家父也只是希望她能够回到叙拉古看看这座城市。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]唉，不愧是贝洛内家。
[name="瓦拉赫"]明知德克萨斯这个姓氏对罗塞蒂家族来说意义重大，却就这样落落大方地请了回来。
[name="瓦拉赫"]大气，真的大气。
[name="瓦拉赫"]我瓦拉赫今天算是服了。
[Character(name="avg_427_vigil_1#8$1",name2="avg_npc_695_1#5$1",focus=1)]
[name="莱昂图索"]你又在开玩笑了。
[Character(name="avg_427_vigil_1#8$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]玩笑？这哪里是玩笑？
[name="瓦拉赫"]切利尼娜小姐还活着的消息，对我们罗塞蒂来说意义非凡。
[name="瓦拉赫"]不管贝洛内怎么想，罗塞蒂都欠你们一次。
[Character(name="avg_427_vigil_1#8$1",name2="avg_npc_695_1#5$1",focus=1)]
[name="莱昂图索"]我们两家是将来要共同建设新城市的关系，有什么欠与不欠的？
[Character(na

... (全文14759字符)
```

### level_act21side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g4_srctheater",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$newhope01_intro",key="$newhope01_loop", volume=0.6)]
[Delay(time=1)]
对她来说，她的生活方式是始终如一的，只是别人会因此说——
她像个叙拉古人。
她像叙拉古人吗？
她不知道。
她只记得自己有一次和爷爷说过——
“我觉得，那些认为叙拉古的生活更加高贵的人，和认为哥伦比亚的生活更加高贵的人，都很无聊。”
爷爷哈哈大笑。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$transmission")]
[name="收音机"]今天，备受瞩目的卡拉奇部长遇刺案件即将开庭。
[name="收音机"]不过，似乎是出于安全考量，只有少数被邀请者能够进入法庭现场旁听。
[name="收音机"]其他人只能在法院外围等待审判的结果。
[name="收音机"]现在，法院已经被护卫重重包围，但是，依然有许多市民聚集在这里。
[name="收音机"]看来，卡拉奇部长的死还是牵动了许多市民的心。
[name="收音机"]我们会持续追踪报道，请听众们耐心等待。
[Dialog]
[Character(name="avg_npc_684_1#8$1",fadetime=0.5)]
[delay(time=0.5)]
[name="空"]......
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]空，准备好了吗？
[Character(name="avg_npc_684_1#1$1")]
[name="空"]嗯。
[name="空"]我在演出的时候，你们两个想去的话就去吧。
[Character(name="avg_103_angel_1#9$1")]
[name="能天使"]反正去了也进不去，还是算啦。
[Character(name="avg_201_moeshd_1#13$1")]
[name="可颂"]嗯，现在我们也只能耐心等待结果了。
[Character(name="avg_103_angel_1#10$1")]
[name="能天使"]你在舞台上可要加油哦。
[Character(name="avg_npc_684_1#9$1")]
[name="空"]放心吧，我已经做好心理准备了。
[Dialog]
[Character]
[name="女演员"]空，准备好了吗？要报幕了。
[Character(name="avg_npc_684_1#9$1")]
[name="空"]来了！
[StopMusic(fadetime=2)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g3_srccourt",screenadapt="coverall")]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_crwddiscuss_inside", channel="a",loop=true,volume=0.3)]
[Delay(time=1)]
沃尔西尼法院
[Dialog]
[Delay(time=1)]
[Character(name="avg_4065_judge_1#1$1",fadetime=0.5)]
[Delay(time=0.5)]
[name="拉维妮娅"]安静，安静。
[name="拉维妮娅"]今天这场庭审，结果将对所有沃尔西尼的市民公开。
[name="拉维妮娅"]今天审理的案件，是建设部部长卡拉奇遇刺一案。
[name="拉维妮娅"]将犯罪嫌疑人带上来。
[Dialog]
[Character]
[Delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_1028_texas2_1#1$1",fadetime=1)]
[Delay(time=2)]
[Character]
[MusicVolume(channel="a",volume=0.5, fadetime=2)]
[name="好奇的看客"]那就是......德克萨斯？
[name="聒噪的看客"]那个发色和瞳色，不会有错！德克萨斯家的人！
[Character(name="avg_npc_692_1#3$1")]
[name="？？？"]......
[name="？？？"]Zzz......
[Character]
[name="好奇的看客"]她怎么会还活着？
[name="聒噪的看客"]她杀了卡拉奇？
[Dialog]
[PlaySound(key="$gavel1", volume=0.7)]
[CameraShake(duration=0.5,xstrength=15,ystrength=15,vibrato=30,randomness=90,fadeout=true,block=true)]
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]肃静！
[StopSound(channel="a", fadetime=2)]
[name="拉维妮娅"]......
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]......
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]切利尼娜·德克萨斯，你曾出现在卡拉奇部长的遇害现场。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]是的。
[name="德克萨斯"]我安装了炸弹，在建设部部长路过的时候引爆了。
[Character]
[name="好奇的看客"]她就这么承认了？！
[name="聒噪的看客"]最后的德克萨斯......怎么如此堕落！
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]......你的动机是什么？
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]没有动机。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]谁指使你的？
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]无人指使。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]所以说，你独自做了这一切？
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]嗯。
[Character]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="刻薄的陪审团成员"]不可能！你从哪里搞到的炸弹？又怎么可能有机会安装呢！
[Character(name="avg_1028_texas2_1#8$1")]
[name="德克萨斯"]这重要吗？
[Character]
[name="多疑的陪审团成员"]你是不是来为德克萨斯家族复仇的？
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]不是。
[Character]
[name="多疑的陪审团成员"]可是......
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]拉维妮娅法官，我已经供认了一切。
[name="德克萨斯"]这几位坐在陪审团席位上的家族成员也实在太吵了一点。
[Character]
[name="刻薄的陪审团成员"]你！
[Character(name="avg_1028_texas2_1#2$1")]
[name="德克萨斯"]这些多余的流程，我们是不是可以干脆跳过？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g11_mansionhall",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$dooropenquite")]
[Character(name="avg_npc_690_1#9$1",fadetime=1)]
[Delay(time=2)]
[Character(name="avg_npc_690_1#5$1")]
[name="德米特里"]嗯？
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#5$1",focus=2)]
[name="德米特里"]莱昂，你怎么还在这？
[name="德米特里"]我还以为，你会在法庭。
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#5$1",focus=1)]
[name="莱昂图索"]你真的意外吗，德米特？
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#1$1",focus=2)]
[name="德米特里"]......要喝点什么吗？
[name="德米特里"]早上的话，我建议不要喝酒，我来给你调一些提神的果汁。
[Character(name="avg_427_vigil_1#6$1",name2="avg_npc_690_1#1$1",focus=1)]
[name="莱昂图索"]威士忌，最烈的。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#1$1",focus=1)]
[name="莱昂图索"]然后，回答我的问题。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#9$1",focus=2)]
[name="德米特里"]你是怎么猜到的？
[Character(name="avg_427_vigil_1#7$1",name2="avg_npc_690_1#9$1",focus=1)]
[name="莱昂图索"]很简单啊。
[name="莱昂图索"]对我的袭击也好，对卡拉奇的刺杀也好，都说明，有人想要十二家族互相猜忌。
[name="莱昂图索"]而且，拉维妮娅作为贝洛内在这件事上的代言人，一定要无法找到凶手，否则的话，事态也会得到一定控制。
[name="莱昂图索"]所以，在拉维妮娅逮捕切利尼娜后，对方一定不希望这场庭审进行。
[name="莱昂图索"]那么，拉维妮娅会遇上什么呢？
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#9$1",focus=1)]
[name="莱昂图索"]还好，你没有成功。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#9$1",focus=2)]
[name="德米特里"]你自己可能没有察觉，但她已经给你带去了许多影响。
[name="德米特里"]这让你的行为开始愈发摇摆。
[name="德米特里"]而通过对你的影响，拉维妮娅自己可能也开始相信，自己是能做到一些什么的。
[name="德米特里"]我必须掐断这种不切实际的妄想。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#9$1",focus=1)]
[name="莱昂图索"]......真亏你能理直气壮地说出这样的话。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#3$1",focus=2)]
[name="德米特里"]不，莱昂。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_690_1#9$1",focus=2)]
[name="德米特里"]我并不是心安理得做这些事的。
[name="德米特里"]我不希望等到一切结束的时候告诉你结果，让你被迫接受。
[name="德米特里"

... (全文19741字符)
```

### level_act21side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g7_reception",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Dialog]
[Delay(time=1)]
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",fadetime=1)]
[delay(time=2)]
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]虽然我也考虑过莱昂图索在诓我的可能性，但是，一见到你我就知道了。
[name="瓦拉赫"]你是货真价实的德克萨斯。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=1)]
[name="德克萨斯"]......
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]容我自我介绍一下，我是罗塞蒂家族的瓦拉赫。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=1)]
[name="德克萨斯"]你是哥伦比亚人？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]当然，罗塞蒂家族的大部分成员都是哥伦比亚人。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]如何，这里的监狱生活？
[Character(name="avg_1028_texas2_1#8$1",name2="avg_npc_695_1#5$1",focus=1)]
[name="德克萨斯"]没什么特别的。
[Character(name="avg_1028_texas2_1#8$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]真奇怪，照理说，你不应该在监狱里待这么久，贝洛内到底是怎么想的。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=1)]
[name="德克萨斯"]遵纪守法，很奇怪吗？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]遵纪守法？但是叙拉古的法院，跟所谓的法律真的有关系吗？
[name="瓦拉赫"]比如，在大部分的叙拉古城市，一个家族成员的成年礼，就是上一次法庭，进一次监狱。
[name="瓦拉赫"]然后，他的家族成员会像迎接一名战士一样，将他带回家族。
[name="瓦拉赫"]这个国家表面上的一切，对我们这种身处地下秩序的人来说，都形同虚设。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=1)]
[name="德克萨斯"]所以呢？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]你是在哥伦比亚长大的人，难道还需要我来解释吗？
[name="瓦拉赫"]“可笑”，我没有除此以外的评价。
[name="瓦拉赫"]当然，也拜此所赐，我们才能够如此顺利地在这里扎根。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=1)]
[name="德克萨斯"]你很喜欢和人聊政治吗？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]看来你不喜欢。
[name="瓦拉赫"]其实我也不喜欢。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]我就直说吧，你为什么没有死？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=1)]
[name="德克萨斯"]与你无关。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]好吧，那我换个问法，你为什么要回来？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=1)]
[name="德克萨斯"]莱昂图索没有告诉你吗？我欠贝洛内一次。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]那么，我是不是可以理解为，你知道贝洛内是为了让你对付我们罗塞蒂才让你回来的，你还是回来了。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=1)]
[name="德克萨斯"]我也是回来之后才知道的，不过——你确实可以这么理解。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]你的坦诚甚至让我怀疑是不是我出了问题，最后的德克萨斯。
[name="瓦拉赫"]难道你要告诉我，你已经完全忘记了，德克萨斯这个姓氏曾经统领着哥伦比亚大大小小的家族？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#4$1",focus=2)]
[name="瓦拉赫"]你的爷爷，萨尔瓦多雷曾经是每一个哥伦比亚家族成员的信仰？！
[Character(name="avg_1028_texas2_1#8$1",name2="avg_npc_695_1#4$1",focus=1)]
[name="德克萨斯"]......
[name="德克萨斯"]德克萨斯留下的一切，都与我无关。
[Character(name="avg_1028_texas2_1#8$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]都与你无关？！
[Character]
[CameraShake(duration=0.3, xstrength=30, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_smashtable", volume=1)]
[PlaySound(key="$blooddrop", volume=1)]
瓦拉赫一拳打在旁边的茶几上，鲜血从手指上流了下来。
而他仿佛浑然未觉。
[Character(name="avg_1028_texas2_1#8$1",name2="avg_npc_695_1#4$1",focus=2)]
[name="瓦拉赫"]你是切利尼娜·德克萨斯！萨尔瓦多雷的孙女！
[name="瓦拉赫"]你只要活着，那些东西就与你有关！
[name="瓦拉赫"]光是你的名字出现在罗塞蒂的会议桌上，就会让我们不得不去改变行动的方针！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="瓦拉赫"]我们曾经以德克萨斯为荣！
[Character(name="avg_1028_texas2_1#8$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]为了不让萨尔瓦多雷的心血白费，你知不知道，乔万娜花了多少力气才将剩下的哥伦比亚家族重新统合起来？
[name="瓦拉赫"]你知不知道，我们如何向西西里夫人卑躬屈膝，最终选择向叙拉古回流，从哥伦比亚千里迢迢返回叙拉古？
[name="瓦拉赫"]为了生存，我们甚至将建造移动城市的技术和盘托出，几乎在免费为叙拉古建造新的移动城市——
[name="瓦拉赫"]这一切都是因为德克萨斯的陨落，我们不得不接受了这个事实。
[name="瓦拉赫"]而现在，你，最后的德克萨斯，堂而皇之地踏上了这片土地。
[name="瓦拉赫"]却说你与这一切无关，你只是来还债。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_1028_texas2_1#8$1",name2="avg_npc_695_1#4$1",focus=2)]
[name="瓦拉赫"]你甚至站在了我们的对立面！
[name="瓦拉赫"]你欠贝洛内的？
[name="瓦拉赫"]既然你活着，那你欠哥伦比亚家族的更多！
[Character(name="avg_1028_texas2_1#7$1",name2="avg_npc_695_1#4$1",focus=1)]
[name="德克萨斯"]我或许欠乔万娜一个交代，但我不欠哥伦比亚家族的。
[name="德克萨斯"]完成和贝洛内的约定后，我会离开叙拉古。
[Character(name="avg_1028_texas2_1#7$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]你觉得我会相信吗？
[name="瓦拉赫"]你的存在，就是对罗塞蒂根基的动摇。
[Character(name="avg_1028_texas2_1#7$1",name2="avg_npc_695_1#1$1",focus=1)]
[name="德克萨斯"]......
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=1)]
[name="德克萨斯"]乔万娜呢？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]什么？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=1)]
[name="德克萨斯"]我问，为什么是你来见我，而不是乔万娜。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]我是她的代言人。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=1)]
[name="德克萨斯"]她不会说，向西西里夫人卑躬屈膝。
[name="德克萨斯"]她也不会派一个使者来见我。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]你以为你了解她？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=1)]
[name="德克萨斯"]从你的表现来看，或许是这样。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#1$1",focus=2)]
[name="瓦拉赫"]......
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#3$1",focus=2)]
[name="瓦拉赫"]啊......真可惜。
[name="瓦拉赫"]看来，我还是不够了解传闻中的德克萨斯。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_npc_695_1#5$1",focus=2)]
[name="瓦拉赫"]我还以为我的演技不错。
[Chara

... (全文17521字符)
```

### level_act21side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g1_srcstreet",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
萨卢佐家族周边
[Dialog]
[delay(time=1)]
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_685_1#1$1",fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_685_1#1$1",focus=2)]
[name="贝纳尔多"]莱昂。
[name="贝纳尔多"]我向来不会对你的做法指指点点，我希望你能对诸事有自己的判断。
[name="贝纳尔多"]这些年，你做得很好。
[Character(name="avg_427_vigil_1#2$1",name2="avg_npc_685_1#1$1",focus=1)]
[name="莱昂图索"]如果你真的这么想，又为什么......
为什么要在这时突然出手？
为什么要告诉我那些？
为什么要......背叛拉维妮娅？
莱昂图索心中有无数疑问，却发现自己一个都问不出口。
之前的所见所闻颠覆了他的认知，他忽然觉得，眼前的父亲是陌生的。
[Character(name="avg_427_vigil_1#2$1",name2="avg_npc_685_1#2$1",focus=2)]
[name="贝纳尔多"]因为，现在是最好的，也是唯一的机会。
[Character(name="avg_427_vigil_1#5$1",name2="avg_npc_685_1#2$1",focus=1)]
[name="莱昂图索"]这是什么意思？
[Character(name="avg_427_vigil_1#5$1",name2="avg_npc_685_1#1$1",focus=2)]
[name="贝纳尔多"]你会知道的。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_npc_689_1#1$1",fadetime=1)]
[Delay(time=2)]
[name="卢比奥"]贝纳尔多先生，莱昂图索先生，恭候多时了。
[Character(name="avg_npc_685_1#4$1")]
[name="贝纳尔多"]嗯？你不是萨卢佐的人。
[Character(name="avg_427_vigil_1#5$1")]
[name="莱昂图索"]食品安全部部长，卢比奥。为什么你会......
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]今晚的宴会，将由食品安全部提供食材，并由鄙人亲自下厨。
[Character(name="avg_npc_685_1#4$1")]
[name="贝纳尔多"]哦？
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]我听说过，在沃尔西尼，想要举办一场上好的宴会，离不开食品安全部的支持。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]您过誉了。
[name="卢比奥"]我只是希望能提供让每个家族的贵人们都满意的食物罢了。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]既然如此，今晚的宴会，倒是更让人期待了。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g5_srcpark",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_cardoorc")]
[Character]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_1028_texas2_1#1$1",name2="char_empty",fadetime=1)]
[Delay(time=2)]
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#1$1",fadetime=0.5)]
[Delay(time=0.5)]
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#1$1",focus=2)]
[name="拉维妮娅"]......你来了。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#1$1",focus=1)]
[name="德克萨斯"]他现在在哪里？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#5$1",focus=2)]
[name="拉维妮娅"]他去了萨卢佐家。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#5$1",focus=1)]
[name="德克萨斯"]好。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#5$1")]
[Delay(time=2)]
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#5$1",focus=2)]
[name="拉维妮娅"]你不问为什么吗？
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#5$1",focus=1)]
[name="德克萨斯"]我能感觉到，贝纳尔多对你来说，很重要。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#8$1",focus=2)]
[name="拉维妮娅"]......
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#6$1",focus=2)]
[name="拉维妮娅"]在我当上了这座城市的法官之后，他没有要求我必须像别的法官那样，在立场上维护自己背后的家族。
[name="拉维妮娅"]他允许我做我自己想做的事。
[name="拉维妮娅"]还有莱昂。
[name="拉维妮娅"]莱昂作为贝洛内家族在这座城市的领导者，他也愿意尊重我的工作，以及我所坚持的公正。
[name="拉维妮娅"]即便我将矛头指向贝洛内，他也会公事公办。
[name="拉维妮娅"]用他的话说，就是我的公正比单纯的暴力更有效率。
[name="拉维妮娅"]我不讨厌他这种对于公正的理解，他甚至也会闲暇时读一读法律相关的书籍。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#5$1",focus=2)]
[name="拉维妮娅"]但即便如此，身为法官，我依然要面对这座城市中时刻在发生的不公。
[name="拉维妮娅"]家族之间的倾轧，家族对普通市民的压迫，普通市民的敢怒不敢言......
[name="拉维妮娅"]我越是想要公正行事，就越意识到自己举步维艰。
[name="拉维妮娅"]我曾经安慰自己，起码并没有成为家族的帮凶，德克萨斯。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#2$1",focus=2)]
[name="拉维妮娅"]怎么可能呢，我的手早就脏了。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#1$1",focus=2)]
[name="拉维妮娅"]只是我还不想承认，脏才是理所当然的事。
[name="拉维妮娅"]即使这在你看来可能是可笑的。
[name="拉维妮娅"]贝纳尔多对我的许诺，是我能够在叙拉古坚持担任法官的唯一理由。
[Character(name="avg_1028_texas2_1#5$1",name2="avg_4065_judge_1#1$1",focus=1)]
[name="德克萨斯"]许诺？
[Character(name="avg_1028_texas2_1#5$1",name2="avg_4065_judge_1#8$1",focus=2)]
[name="拉维妮娅"]......他曾经对我说，等到贝洛内家族取得胜利的那一天，他会在叙拉古开辟出一片地方。
[name="拉维妮娅"]在那里，我所相信的律法将不再依托于单纯的权力，我所想要的公平能够真正实现。
[name="拉维妮娅"]所以在那之前，他希望我能够忍耐。
[name="拉维妮娅"]每当我坚持不下去的时候，我就会想到他的承诺。
[Character(name="avg_1028_texas2_1#1$1",name2="avg_4065_judge_1#6$1",focus=2)]
[name="拉维妮娅"]你说，如果这真的只是一个谎言，那我过去十几年的生活又算是什么？
[Character(name="avg_1028_texas2_1#8$1",name2="avg_4065_judge_1#6$1",focus=1)]
[name="德克萨斯"]......我想，以他的立场和地位，他没有必要说这种谎言。
[playsound(key="$d_gen_walk_n", loop=true, channel="bgs")]
[Character(name="avg_1028_texas2_1#8$1",name2="avg_4065_judge_1#6$1",focus=2)]
[name="拉维妮娅"]是啊。所以——
[StopSound(channel="bgs", fadetime=0.5)]
[CameraShake(duration=0.3, xstrength=20, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_698_1#1$1")]
[name="萨卢佐家族成员"]什么人？
[name="萨卢佐家族成员"]嗯？你是——
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]我是法官拉维妮娅，关于谋杀卡拉奇的罪犯，我有问题想要找阿尔贝托阁下谈谈。
[Character(name="avg_npc_698_1#1$1")]
[name="萨卢佐家族成员"]法官阁下......老爷正在宴请贵客，没有时间......
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]贵客，是指贝纳尔多·贝洛内，是吗？
[Character(name="avg_npc_698_1#1$1")]
[name="萨卢佐家族成员"]......
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]请转告两位领袖，兹事体大。
[name="拉维妮娅"]今天，如果见不到两位，我是不会回去的。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g7_reception",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_689_1#5$1")]
[name="卢比奥"]这道菜，是我从一位莱塔尼亚厨师那里学来的，请诸位品尝。
[Character(name="avg_npc_685_1#1$1")]
[playsound(key="$d_avg_dishes")]
[name="贝纳尔多"]......
[Character

... (全文20385字符)
```

### level_act21side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[character(fadetime=0)]
[stopmusic]
[Dialog]
[Background(image="33_g7_reception",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[Character(name="avg_427_vigil_1#2$1",fadetime=1)]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[delay(time=1.5)]
[name="莱昂图索"]......嘶。
[Character(name="avg_npc_698_1#1$1")]
[name="家族成员"]少爷，您没事吧。
[Character(name="avg_427_vigil_1#2$1")]
[name="莱昂图索"]做了个梦而已。
[Character(name="avg_427_vigil_1#6$1")]
[name="莱昂图索"]果然不能在沙发上睡觉。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="莱昂图索"]老头子呢？
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_698_1#1$1",focus=2)]
[name="家族成员"]首领已经前往剧院了。
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="莱昂图索"]......
[Character(name="avg_427_vigil_1#1$1",name2="avg_npc_698_1#1$1",focus=2)]
[name="家族成员"]您要去吗？
[character(fadetime=0)]
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[delay(time=1)]
莱昂图索将身体陷入沙发之中，没有回答。
[Dialog]
[character(fadetime=0)]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7)]
[Background(image="33_g11_mansionhall",screenadapt="showall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=3, block=true)]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[Character(name="avg_1028_texas2_1#5$1")]
[name="德克萨斯"]罗塞蒂，乔万娜。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]没错。
[name="贝纳尔多"]切利尼娜，你我之间最初的约定，是为贝洛内赢得最后的胜利。
[name="贝纳尔多"]不过，我改变了主意。
[name="贝纳尔多"]只要你能完成这件事，你就不再欠贝洛内任何东西。
[name="贝纳尔多"]届时，你可以自由地离开。
[name="贝纳尔多"]我以狼之主扎罗的獠牙身份向你保证。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[CameraEffect(effect="Grayscale", amount=0, block=false)]
[Background(image="33_g11_mansionhall",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_1028_texas2_1#5$1")]
[name="德克萨斯"]......
[dialog]
[character(fadetime=0)]
[Blocker(a=0.4, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="从日落时回到住处开始，直到旭日东升。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="听着雨声，德克萨斯一边擦拭着自己的佩剑，一边阅读着送到自己手上的剧本——《德克萨斯之死》。", x=300, y=370, alignment="middle", size=24, delay=0.04, width=700)]
[Subtitle(text="故事曲折动人，并且与她所知的相差不大。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她隐隐有种预感。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但首先，她要让自己的剑更加锋利。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="今天，她的剑或许需要比平时更快一点。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Dialog]
[delay(time=1)]
[playsound(key="$d_avg_telephonering")]
[Delay(time=3)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g2_srcalley",screenadapt="showall")]
[Delay(time=1)]
[playsound(key="$d_avg_rainlight_loop", loop=true, channel="a")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness02_intro",key="$darkness02_loop", volume=0.6)]
[Character(name="avg_npc_683_1#1$1",fadetime=1)]
[delay(time=1)]
[name="拉普兰德"]啧啧，明明在下雨，太阳倒还是挺刺眼。
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]监狱里的伙食还挺好的，建议你们也尝试一下。
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]确实不错，我以前还给他们提过几次建议。
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]请上车吧。
[Character(name="avg_npc_683_1#1$1")]
[name="拉普兰德"]我可以不参加吗？
[Character(name="avg_npc_683_1#5$1")]
[name="拉普兰德"]杀一个哥伦比亚人而已，用得着这么大张旗鼓吗？
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]老爷说，切利尼娜也会参加。
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]哦？
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]什么安排？
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]她会乔装成剧团的成员，在演出开始后，见机行动。
[Character(name="avg_npc_683_1#8$1")]
[name="拉普兰德"]嗯......那我的演出服呢？
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]老爷的意思是——
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]请您在观众席随机应变。
[Character(name="avg_npc_683_1#3$1")]
[name="拉普兰德"]......呵，呵呵。
[Character(name="avg_npc_683_1#3$1")]
[name="拉普兰德"]不解风情的老东西，他人呢，难道他想找个好位置自己看戏？
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]老爷另外有事，他要去见一个人。
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]见一个人？
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]是的，一个洗车工。
[Dialog]
[StopSound(channel="a", fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g8_srcroom",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$dooropenquite", volume=1)]
[delay(time=1)]
[Character(name="avg_201_moeshd_1#13$1")]
[name="可颂"]啊，空，我就知道你会在卡特琳娜小姐的工作室里练习。
[Character(name="avg_201_moeshd_1#13$1")]
[name="可颂"]我倒是不反对啦，但是，还是提前去剧院化妆准备演出比较好吧？
[Character(name="char_101_sora_1#1")]
[name="空"]......嗯，说的也是。
[Character(name="avg_201_moeshd_1#1$1")]
[name="可颂"]能天使已经去买早饭了，我们正好去和她会合吧。
[Character(name="char_101_sora_1#1")]
[name="空"]好。
[Character(name="avg_201_moeshd_1#14$1")]
[name="可颂"]对了，之前我们不是说要办个欢迎会迎接能天使的姐姐吗？
[Character(name="char_101_sora_1#1")]
[name="空"]对啊。
[Character(name="char_101_sora_1#5")]
[name="空"]现在都不知道能不能赶得上了。
[Character(name="char_101_sora_1#3")]
[name="空"]可颂，当心脚下！
[dialog]
[Character(name="avg_201_moeshd_1#5$1")]
[PlaySound(key="$fightgeneral", volume=0.6)]
[CameraShake(duration=0.5,xstrength=15,ystrength=15,vibrato=30,randomness=90,fadeout=true,block=false)]
[name="可颂"]哎？哎呀！
[Character(name="avg_201_moeshd_1#2$1")]
[name="可颂"]好疼......
[Character(name="char_101_sora_1#3")]
[name="空"]你没事吧？
[Character(nam

... (全文23347字符)
```

### level_act21side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g11_mansionhall",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$frontline_intro",key="$frontline_loop", volume=0.6)]
[Character(name="avg_npc_031",name2="avg_npc_683_1#3$1")]
[characteraction(name="left", type="move", xpos=-40, fadetime=1,block=false)]
[delay(time=1)]
[characteraction(name="left", type="move", xpos=60, fadetime=0.3,block=false)]
[characteraction(name="right", type="move", xpos=50, fadetime=1,block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_knife",volume=1)]
[delay(time=0.3)]
[characteraction(name="left", type="move", xpos=20, fadetime=0.5,block=false)]
[characteraction(name="right", type="move", xpos=80, fadetime=1,block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_knife",volume=1)]
[delay(time=0.9)]
[Effect(name="$e_slash_02_l",x = 300, y = 300, layer = 2)]
[characteraction(name="right", type="move", xpos=-180, fadetime=1,block=false)]
[characteraction(name="left", type="move", xpos=-20, fadetime=1,block=false)]
[Blocker(a=0.3, r=1, g=0.3, b=0.3, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=2, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$e_skill_skulsrsword",volume=0.7)]
[Delay(time=1.2)]
[character]
[Character(name="avg_npc_683_1#3$1",name2="char_empty")]
[delay(time=1)]
[Character(name="avg_npc_683_1#3$1",name2="avg_npc_031",fadetime=1)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1,block=false)]
[delay(time=0.2)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=0.3, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="left", type="move", xpos=-40, fadetime=0.3,block=false)]
[Effect(name="$e_spark_01_mid",layer=1)]
[playsound(key="$swordtsing1",volume=0.7)]
[CameraShake(duration=2, xstrength=50, ystrength=10, vibrato=80, randomness=60, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=2, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, block=false)]
[Effect(name="$e_spark_01_mid",layer=1)]
[playsound(key="$swordtsing3",volume=1)]
[playsound(key="$swordtsing2",volume=1)]
[characteraction(name="right", type="move", xpos=220, fadetime=1,block=false)]
[characteraction(name="left", type="move", xpos=10, fadetime=0.3,block=false)]
[delay(time=0.5)]
[Effect(name="$e_slash_01_l",x = 100, y = -200, rox = 30, roy = 70, roz = 90, layer = 2)]
[characteraction(name="right", type="move", xpos=20, fadetime=1,block=false)]
[characteraction(name="left", type="move", xpos=130, fadetime=0.3,block=false)]
[Blocker(a=0.3, r=1, g=0.3, b=0.3, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$e_skill_skulsrsword",volume=0.7)]
[Delay(time=2)]
[Dialog]
[Character]
[PlaySound(key="$bodyfalldown1")]
[Delay(time=2)]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[Character(name="avg_npc_683_1#3$1",fadetime=1)]
[Delay(time=3)]
[Character(name="avg_npc_031")]
[name="罗塞蒂家族成员"]撤退，这家伙很棘手。
[Character(name="avg_npc_031")]
[name="罗塞蒂家族成员"]不要和她硬来。
[Character(name="avg_npc_031")]
[CameraShake(duration=0.5,xstrength=20,ystrength=20,vibrato=30,randomness=90,fadeout=true,block=false)]
[name="罗塞蒂家族成员"]守住通往首领的包厢的走道和楼梯口！
[dialog]
[character]
[PlaySound(key="$d_gen_soldiersrun", volume=0.6)]
[delay(time=3)]
[Character(name="avg_npc_683_1#5$1")]
[name="拉普兰德"]啧啧，罗塞蒂的人还挺能干嘛。
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]想要强行突破看起来不太现实啊。
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]嗯......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="33_g4_srctheater",xScale=1.8,yScale=1.8,x=250,y=-150)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_1028_texas2_1#2$1")]
[name="德克萨斯"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="33_g11_mansionhall",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_683_1#3$1")]
[name="拉普兰德"]哈哈，德克萨斯这家伙，明明是在贝斯里装了录音器。
[Character(name="avg_npc_683_1#3$1")]
[name="拉普兰德"]弹得还挺像那么一回事。
[Character(name="avg_npc_683_1#1$1")]
[name="拉普兰德"]嗯？
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]啊哈，有了。
[Character(name="avg_npc_683_1#3$1")]
[name="拉普兰德"]正面突破不行的话......那就造一条路出来。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_ltroom",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_031")]
[CameraShake(duration=0.3, xstrength=20, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="罗塞蒂家族成员"]别慌张！
[Character(name="avg_npc_031")]
[name="罗塞蒂家族成员"]守住这里！
[dialog]
[Character(name="avg_npc_698_1#1$1")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=0.3, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fade

... (全文33946字符)
```

### level_act21side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g4_srctheater",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[Character(name="avg_103_angel_1#4$1")]
[name="能天使"]空，你没事吧！
[Character(name="avg_npc_684_1#6$1")]
[name="空"]嗯，我还好。
[Character(name="avg_103_angel_1#2$1")]
[name="能天使"]你要去找德克萨斯吗？
[Character(name="avg_npc_684_1#6$1")]
[name="空"]......刚才打照面的时候，她让我等她。
[Character(name="avg_201_moeshd_1#12$1")]
[name="可颂"]那我们也先去避一避吧，现在其他地方都已经乱作一团了。
[Character(name="avg_npc_683_1#1$1")]
[name="拉普兰德"]如果你们不想失去她的话，我建议你们追上她。
[Character(name="avg_npc_684_1#7$1")]
[name="空"]拉普兰德......
[Character(name="avg_201_moeshd_1#15$1")]
[name="可颂"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7)]
[Background(image="33_g8_srcroom",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_103_angel_1#9$1")]
[name="能天使"]我觉得拉普兰德也是一样的。
[Character(name="avg_103_angel_1#9$1")]
[name="能天使"]像她们这样的人，与其去猜她们到底在想什么，不如干脆地接受她们的每一句话。
[Character(name="avg_103_angel_1#9$1")]
[name="能天使"]只有相信她们的每一句话都是真的，才能看穿她们最后是不是在用真实编织一个谎言。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[CameraEffect(effect="Grayscale", amount=0, block=false)]
[Background(image="33_g4_srctheater",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_201_moeshd_1#15$1")]
[name="可颂"]为什么？
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]你知道的吧，那间房间里的人，是谁。
[Character(name="avg_npc_684_1#1$1")]
[name="空"]乔万娜·罗塞蒂。
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]如果说，这片大地上还有谁能让德克萨斯真正回归叙拉古。
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]那个人，不会是我，不会是贝纳尔多，也不会是西西里夫人。
[Character(name="avg_npc_683_1#8$1")]
[name="拉普兰德"]而是她，乔万娜。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g11_mansionhall",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[Character(name="avg_npc_687_1#9$1")]
[name="乔万娜"]切利尼娜，你长高了不少。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]过了这么多年，总是会长一些。
[Character(name="avg_npc_687_1#9$1")]
[name="乔万娜"]对了，我见过你的几个龙门朋友了，听她们说了一些你的事，她们很担心你。
[Character(name="avg_1028_texas2_1#5$1")]
[name="德克萨斯"]......我没想到她们也会来。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]她们和你倒是完全不一样，没想到以你的性格还能交到这么活泼的朋友。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]你不也是吗？
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]你真把我当朋友，就不会这么久也不给我报个信了。
[Character(name="avg_1028_texas2_1#2$1")]
[name="德克萨斯"]......
[Character(name="avg_npc_687_1#2$1")]
[name="乔万娜"]好啦，知道你肯定也有难言之隐。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]你呢？
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]我？
[Character(name="avg_npc_687_1#8$1")]
[name="乔万娜"]......其实没什么好说的。
[Character(name="avg_npc_687_1#2$1")]
[name="乔万娜"]清算来得太突然了，哥伦比亚的家族人人自危，我看不过去，站出来主持了一下局面。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]然后又和西西里夫人交流了一下，算是把事情摆平了。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]就这么简单。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]说得轻巧。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]......这么一说，我似乎应该向你诉苦。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]但我身边已经太久没有一个可以诉苦的人了。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]所以你才把心思都放在了写剧本上。
[Character(name="avg_npc_687_1#3$1")]
[name="乔万娜"]哈哈，你看出来了吗，《德克萨斯之死》可是我的得意之作。
[Character(name="avg_1028_texas2_1#2$1")]
[name="德克萨斯"]有些细节，也许只有你知道了。
[Character(name="avg_npc_687_1#9$1")]
[name="乔万娜"]那看起来我的记性还算可以。
[Character(name="avg_npc_687_1#9$1")]
[name="乔万娜"]不过，第三幕，关于你的“死”，我一直没有想好。
[Character(name="avg_npc_687_1#9$1")]
[name="乔万娜"]看起来，这下我不用想了。
[Character(name="avg_1028_texas2_1#10$1")]
[name="德克萨斯"]呵。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]其实写剧本还有一个目的。贝纳尔多把家族的担子交给儿子，自己在白日剧团担任艺术总监，是一个公开的秘密。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]我是想找个机会和这位接触一下的，你也知道，家族成员会去做这种事的不太多。
[Character(name="avg_npc_687_1#8$1")]
[name="乔万娜"]不过，没想到，做得最绝的，也是他。
[Character(name="avg_npc_687_1#8$1")]
[name="乔万娜"]不愧是在自己这一代把贝洛内家族壮大到这一程度的人。
[Character(name="avg_npc_687_1#8$1")]
[name="乔万娜"]看来，他是真的想要和西西里夫人扳手腕。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]你看起来并不紧张。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]我只能说，如果贝纳尔多把你当成对付罗塞蒂的杀手锏，那他未免有些太想当然了。
[Character(name="avg_npc_687_1#2$1")]
[name="乔万娜"]你来找我是对的，切利尼娜。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]无论你和贝洛内之间有什么，我都可以帮你摆平。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]加入我吧。
[Character(name="avg_npc_687_1#9$1")]
[name="乔万娜"]我们两个一起的话，一定能够在叙拉古闯出一番事业。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]这不是因为你是萨尔瓦多雷的孙女。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]而是因为，我知道，你，切利尼娜，是有这个本事的人。
[Character(name="avg_npc_687_1#6$1")]
[name="乔万娜"]我们可以一起重新开始，切利尼娜。
[Character(name="avg_1028_texas2_1#2$1")]
[name="德克萨斯"]......
[Character(name="avg_1028_texas2_1#8$1")]
[name="德克萨斯"]你不是想知道，我是怎么活下来的吗？
[Character(name="avg_1028_texas2_1#8$1")]
[name="德克萨斯"]乔万娜，我并不是因为侥幸才从那场清算中幸存的。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g4_srctheater",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_683_1#1$1")]
[name="拉普兰德"]既然你站在舞台上出演了这部歌舞剧......现在，你对七年前发生的事了解了多少？
[Character(name="avg_npc_684_1#2$1")]
[name="空"]七年前......德克萨斯的父亲朱塞佩谋杀了他的父亲——萨尔瓦多雷，并且宣布德克萨斯家族脱离叙拉古的掌控。
[Character(name="avg_n

... (全文16667字符)
```

### level_act21side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g11_mansionhall",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$plot_intro",key="$plot_loop", volume=0.6)]
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]最不起眼的食品安全部......
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]有人缘但不被重视的食品安全部部长......
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]事到如今，卡拉奇这样，为了各大家族之间的平衡而被推选出来的人已经不再需要了。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]您需要一个安全而又好用的傀儡。
[Character(name="avg_npc_689_1#5$1")]
[name="卢比奥"]不是吗？
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]卢比奥部长，真正安全而又好用的傀儡，从来不会这么自称。
[Character(name="avg_npc_689_1#5$1")]
[name="卢比奥"]我只是比其他人多一些自知之明而已。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]哈哈哈，好一个自知之明。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]卢比奥，如你所说，你确实是替代卡拉奇的最好人选。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]不过，既然你如此坦诚，那我也不妨告诉你一些事情。
[Character(name="avg_npc_689_1#5$1")]
[name="卢比奥"]您请说。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]卡拉奇，是我的人杀的。
[Character(name="avg_npc_689_1#3$1")]
[name="卢比奥"]......
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]你很有勇气，我不讨厌和你这样的人聊天。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]所以，我可以给你一个机会，卢比奥。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]走出这间房间，忘记你刚才说过的话，这样的话，你不会受到任何伤害。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]然后，回去和你的妻子还有女儿团聚，好好享受这座城市最后的一点安宁时光。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]如果是这样，您难道不是更加需要一个我这样的傀儡吗？
[Character(name="avg_npc_685_1#4$1")]
[name="贝纳尔多"]哦？
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]您想要的，正是眼下的混乱。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]您想要推翻西西里夫人定下的秩序，然而，西西里夫人治下也好，更早的时期也好。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]家族之间的斗争，从来与普通人无关。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]当一切发生时，我们只能等待一个结果。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]从这个角度来说，是西西里夫人统领这个国家，还是您统领这个国家，对我们普通人来说毫无分别。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]但是，最后的胜利者，却总是需要一个统领表面秩序的人。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]您作为一个家族的领袖，想必是明白这个道理的——
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]普通人离开家族并非无法生存，但家族离开普通人，却未必如此。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]你想说，你们才是强者？
[Character(name="avg_npc_689_1#5$1")]
[name="卢比奥"]不过是一些弱者的自圆其说罢了。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]好一个自圆其说。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]但这不能解释你真正的目的。
[Character(name="avg_npc_689_1#5$1")]
[name="卢比奥"]权力，尊敬的贝纳尔多。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]我从小就因为这副长相和孱弱的体格，被身边的人看不起。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]对我来说，来自身边的人的压迫，比来自家族的还要直接。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]我一路隐忍到现在，就是为了等这一个机会。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]所以您说是您杀了卡拉奇，我只觉得，我这一次来对了。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]说句您不爱听的，您想对抗西西里夫人，我觉得，您很难获胜。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]但这又有什么关系呢，我不在乎您到最后能不能赢——
[Character(name="avg_npc_689_1#4$1")]
[name="卢比奥"]但这份权力，西西里夫人给不了我，只有您能给我。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]你很诚实，卢比奥，我喜欢和诚实的人交朋友。
[Dialog]
[Character]
[CameraShake(duration=1.5, xstrength=20, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_explosion", volume=0.6)]
[Delay(time=2)]
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]嗯？
[Character(name="avg_npc_698_1#1$1")]
[name="贝洛内家族成员"]首领......（耳语）
[Character(name="avg_npc_685_1#2$1")]
[name="贝纳尔多"]......
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]传下命令，就说，今天到此为止。
[Character(name="avg_npc_698_1#1$1")]
[name="贝洛内家族成员"]是。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g4_srctheater",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[Character(name="avg_npc_684_1#5$1")]
[name="空"]刚才怎么了？！
[Character(name="avg_201_moeshd_1#15$1")]
[name="可颂"]那边的房间......好像震了一下？
[Character(name="avg_npc_683_1#5$1")]
[name="拉普兰德"]看来，她选择了你们。
[Character(name="avg_npc_684_1#5$1")]
[name="空"]欸？
[Character(name="avg_npc_683_1#5$1")]
[name="拉普兰德"]这股震动，是乔万娜的源石技艺。
[name="拉普兰德"]她们决裂了。
[Character(name="avg_103_angel_1#2$1")]
[name="能天使"]看，德克萨斯从窗户跳出去了，我们快跟上。
[Character(name="avg_npc_684_1#7$1")]
[name="空"]嗯！
[dialog]
[Character(name="avg_103_angel_1#2$1",name2="avg_npc_684_1#7$1")]
[Delay(time=0.2)]
[PlaySound(key="$rungeneral",volume=1)]
[character(fadetime=1)]
[Delay(time=2)]
[Character(name="avg_npc_683_1#1$1")]
[name="拉普兰德"]......
[Character(name="avg_npc_683_1#2$1")]
[name="拉普兰德"]唉，德克萨斯，如果，我是说如果，当年我们成了朋友，是不是，我就能把你留在叙拉古呢？
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]哈，不可能吧。
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]我们只会互相厮杀至死。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g11_mansionhall",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=0.3, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$e_skill_skulsrsword",volume=0.7)]
[playsound(key="$d_avg_hammer",volume=0.7,delay=0.3)]
[Delay(time=1)]
[Character(name="avg_npc_693_1#5$1")]
[name="洗车工"]拉维妮娅小姐，不要逼我......杀了你。
[Character(name="avg_npc_693_1#5$1")]
[name="洗车工"]我有我的任务要完成。
[Character(name="avg_4065_judge_1#7$2")]
[name="拉维妮娅"]......
[Delay(time=1)]
[dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=0.3, block=false)]

... (全文22883字符)
```

### level_act21side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[Background(image="33_g10_smallrestaurant",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="店员"]您点的披萨。
[Character(name="avg_4065_judge_1#9$1")]
[name="拉维妮娅"]谢谢。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]......
[character]
[dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[Character(name="avg_427_vigil_1#1$1",fadetime=1)]
[delay(time=2)]
[name="莱昂图索"]这个位置有人坐吗？
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]有人。
[Character(name="avg_4065_judge_1#1$1",name2="avg_427_vigil_1#8$1",focus=2)]
[name="莱昂图索"]那我就不客气了。
[Character(name="avg_4065_judge_1#1$1",name2="avg_427_vigil_1#8$1",focus=1)]
[name="拉维妮娅"]我说了，有人。
[Character(name="avg_4065_judge_1#2$1",name2="avg_427_vigil_1#8$1",focus=1)]
[name="拉维妮娅"]您还是回去继续完成您的家族任务，不要来管我这样的普通人。
[Character(name="avg_4065_judge_1#2$1",name2="avg_427_vigil_1#2$1",focus=2)]
[name="莱昂图索"]拉维妮娅姐。
[Character(name="avg_4065_judge_1#2$1",name2="avg_427_vigil_1#2$1",focus=1)]
[name="拉维妮娅"]......
[Character(name="avg_4065_judge_1#1$1",name2="avg_427_vigil_1#2$1",focus=1)]
[name="拉维妮娅"]我不怪你，莱昂。
[name="拉维妮娅"]我也不怪贝纳尔多。
[name="拉维妮娅"]如果我有一个责怪的对象，那只能是我自己。
[Character(name="avg_4065_judge_1#8$1",name2="avg_427_vigil_1#2$1",focus=1)]
[name="拉维妮娅"]是生在这个国家却依然心存幻想的我不对，我没有理由去责备你们。
[Character(name="avg_4065_judge_1#8$1",name2="avg_427_vigil_1#1$1",focus=2)]
[name="莱昂图索"]我不想在这个时候劝你理智一点。
[name="莱昂图索"]我知道，一切的安慰都没有意义。
[name="莱昂图索"]即使我自认与你同样是受害者，但你把我当做加害者也是理所当然的事。
[Character(name="avg_4065_judge_1#8$1",name2="avg_427_vigil_1#7$1",focus=2)]
[name="莱昂图索"]我只能告诉你......我还没有放弃。
[name="莱昂图索"]就这样。
[Character(name="avg_4065_judge_1#8$1",name2="avg_427_vigil_1#2$1",focus=2)]
[name="莱昂图索"]最近城里事情很多，自己注意安全，遇到麻烦可以给我打电话。
[Character(name="avg_4065_judge_1#6$1",name2="avg_427_vigil_1#2$1",focus=1)]
[name="拉维妮娅"]......
[Dialog]
[delay(time=1)]
[character]
[playsound(key="$phonevibration")]
[Delay(time=2)]
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]卢比奥部长。
[Character(name="avg_4065_judge_1#1$1",focus=-1)]
[name="卢比奥"]法官小姐，现在有空吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g2_srcalley",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_201_moeshd_1#12$1")]
[name="可颂"]街上的人感觉表情都好紧张。
[Character(name="char_101_sora_1#4")]
[name="空"]毕竟昨天发生了那样的事情......
[Character(name="avg_201_moeshd_1#9$1")]
[name="可颂"]你们真的要去见那个总监吗？
[Character(name="char_101_sora_1#4")]
[name="空"]嗯，无论如何，有些话还是要和总监说清楚的。
[Character(name="avg_201_moeshd_1#15$1")]
[name="可颂"]但是——
[Character(name="char_101_sora_1#5")]
[name="空"]没关系，可颂你继续去做你的事情吧。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]有我在，放心。
[Character(name="avg_201_moeshd_1#15$1")]
[name="可颂"]......
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]......这样的话，今天我就来保护可颂吧。
[Character(name="char_101_sora_1#5")]
[name="空"]嗯，那就拜托你啦。
[Character(name="avg_201_moeshd_1#11$1")]
[name="可颂"]出什么事的话记得立刻联络我们。
[Character(name="char_101_sora_1#1")]
[name="空"]好~
[dialog]
[Character(name="char_101_sora_1#1",name2="avg_1028_texas2_1#1$1")]
[delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[Character(fadetime=1)]
[delay(time=2)]
[Character(name="avg_201_moeshd_1#12$1")]
[name="可颂"]......
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]可颂，你在想德克萨斯的事，对吧。
[Character(name="avg_201_moeshd_1#15$1")]
[name="可颂"]......很明显吗？
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]很明显哦。
[Character(name="avg_103_angel_1#8$1")]
[name="能天使"]因为我也在想一样的事情。
[Character(name="avg_103_angel_1#8$1")]
[name="能天使"]我当然知道空的想法，如果德克萨斯想要留下来，她会尊重德克萨斯的意见。
[Character(name="avg_103_angel_1#8$1")]
[name="能天使"]我也一样。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]但是——
[Character(name="avg_103_angel_1#9$1")]
[name="能天使"]我还想让姐姐也见一见我的几个伙伴呢。
[Character(name="avg_103_angel_1#9$1")]
[name="能天使"]至少，如果有办法能让德克萨斯安全离开叙拉古，你想找到这种方法，不是吗？
[Character(name="avg_201_moeshd_1#3$1")]
[name="可颂"]唉......瞒不过你。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]肯定也没有瞒过她们两个。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]就像我们会尊重空的想法一样，她们也能理解我们的想法的啦。
[Character(name="avg_201_moeshd_1#15$1")]
[name="可颂"]但是，这里毕竟是叙拉古......而且德克萨斯是和这个国家最厉害的家伙们有牵扯，我也不知道该怎么办。
[Character(name="avg_103_angel_1#4$1")]
[name="能天使"]嗯？我还以为，你已经想到了呢。
[Character(name="avg_201_moeshd_1#15$1")]
[name="可颂"]欸？
[Character(name="avg_103_angel_1#6$1")]
[name="能天使"]嗯......说到这个国家的大人物，我们昨天不是也遇到过一个了吗？
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g7_reception",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]请进。
[dialog]
[character]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[Character(name="char_101_sora_1#4",name2="avg_1028_texas2_1#1$1",fadetime=1)]
[delay(time=3)]
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]空小姐，切利尼娜小姐，欢迎。
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[Character(name="avg_1028_texas2_1#7$1")]
[name="德克萨斯"]......
[Character(name="avg_1028_texas2_1#7$1")]
[name="德克萨斯"]为什么要把空她们牵扯进来？
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]空小姐的简历会来到我手上确实是一个意外。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]当然，这也可以称得上是某种必然。
[Character(name="avg_npc_685_1#8$1")]
[name="贝纳尔多"]毕竟，白日剧团在叙拉古也是小有名气的剧团。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]只不过，担任剧团总监的是贝洛内家族的领袖，终究算是一个秘密。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]贝洛内在这座城里的诸多事务，毕竟是交给了我的儿子，我并不打算干涉他的行动。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]切利尼娜小姐，空小姐，我担任这个剧团的总监有六年了。
[Character(name="avg_npc

... (全文27868字符)
```

### level_act21side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g1_srcstreet",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_rainheavy_loop", loop=true, channel="a",fadetime=1)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[Character(name="char_101_sora_1#3")]
[name="空"]德克萨斯！
[Character(name="avg_1028_texas2_1#3$1")]
[name="德克萨斯"]怎么了？
[Character(name="char_101_sora_1#4")]
[name="空"]卡特琳娜小姐......不，乔万娜小姐，可能有危险！
[Character(name="avg_1028_texas2_1#7$1")]
[name="德克萨斯"]你说什么？
[Character(name="char_101_sora_1#4")]
[name="空"]我刚才给她打了个电话，感觉很不好。
[character]
[dialog]
[PlaySound(key="$phonevibration",volume=0.6)]
[delay(time=2)]
[Character(name="avg_1028_texas2_1#7$1")]
[name="德克萨斯"]......拉普兰德。
[Character(name="avg_1028_texas2_1#7$1",focus=-1)]
[name="拉普兰德"]嗨。
[Character(name="avg_1028_texas2_1#7$1")]
[name="德克萨斯"]有什么事。
[Character(name="avg_1028_texas2_1#7$1",focus=-1)]
[name="拉普兰德"]我只是想要告诉你，你的那个老朋友，现在正在你们的据点附近，被自己家族的人团团围住。
[Character(name="avg_1028_texas2_1#7$1")]
[name="德克萨斯"]......
[Character(name="char_101_sora_1#2")]
[name="空"]德克萨斯，我们应该去帮乔万娜小姐！
[Character(name="avg_1028_texas2_1#7$1")]
[name="德克萨斯"]......我知道。
[Character(name="avg_1028_texas2_1#7$1",focus=-1)]
[name="拉普兰德"]等等。
[name="拉普兰德"]你真的打算去吗？
[name="拉普兰德"]你不惜与罗塞蒂为敌都要离开这片土地。
[name="拉普兰德"]却又要为了她主动留在这座泥潭里？
[name="拉普兰德"]想清楚了，德克萨斯。
[name="拉普兰德"]现在是你转身离开的唯一机会。
[Character(name="avg_1028_texas2_1#8$1")]
[name="德克萨斯"]......
[dialog]
[character]
[PlaySound(key="$transmission",volume=0.6)]
[delay(time=2)]
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]空......
[Character(name="char_101_sora_1#4")]
[name="空"]德克萨斯，你知道吗。
[Character(name="char_101_sora_1#4")]
[name="空"]虽然只是一点为了寻找你而发展的副业。
[Character(name="char_101_sora_1#4")]
[name="空"]但是，我发现，我逐渐喜欢上叙拉古的演艺氛围了。
[Character(name="char_101_sora_1#4")]
[name="空"]这里的人虽然也有那种傲慢，但比龙门那些充满铜臭味的商人要好了太多。
[Character(name="char_101_sora_1#4")]
[name="空"]能天使也总是喊着，要找到叙拉古最美味的披萨。
[Character(name="char_101_sora_1#4")]
[name="空"]可颂......可颂的性格本来就挺随遇而安的啦。
[Character(name="char_101_sora_1#4")]
[name="空"]我刚才就想和你聊聊，或许可以等到大家都玩够了再回龙门。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]但我们总会回到龙门，而且是四个人一起。
[Character(name="char_101_sora_1#5")]
[name="空"]对，四个人一起。
[Character(name="char_101_sora_1#5")]
[name="空"]啊，不对，我刚才和乔万娜小姐聊过了，我想请她也一起去龙门逛逛，所以应该是五个人。
[Character(name="avg_1028_texas2_1#9$1")]
[name="德克萨斯"]......好。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g2_srcalley",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraShake(duration=0.3, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$pistol", volume=0.9)]
[Delay(time=0.5)]
[CameraShake(duration=1, xstrength=12, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_gunsingle", volume=0.9)]
[PlaySound(key="$d_avg_gunsingle", volume=0.9,delay=0.2,channel="z")]
[PlaySound(key="$p_skill_blacktimewand_shot", volume=0.9,delay=0.5)]
[Delay(time=0.5)]
[Blocker(a=0.9, r=0.8, g=0.8, b=0.8, fadetime=0.2, block=true)]
[CameraShake(duration=1.5, xstrength=30, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_explosion", volume=0.9)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[PlaySound(key="$bodyfalldown2", volume=0.7)]
[PlaySound(key="$bodyfalldown2", volume=0.7,channel="z",delay=0.5)]
巷子里倒下了数人。
而乔万娜的身上已经出现了不少伤口。
所有人，包括她自己，都知道，她绝无可能逃脱。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]乔万娜，投降吧。
[Dialog]
[Character]
[Character(name="avg_npc_687_1#7$1",fadetime=1)]
[Delay(time=1)]
[name="乔万娜"]......
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]瓦拉赫，有酒吗？
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]......去车上拿一瓶。
[Character(name="avg_npc_031")]
[name="罗塞蒂家族成员"]是。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]......瓦拉赫，我是想过的，哥伦比亚的有些生意我们是不是做了会更好。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]源石武器，新型药物，军方的渠道......
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]我也想过，是不是有些机会我应该去把握住。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]那些官员的讨好，甚至是哥伦比亚政府的橄榄枝。
[Character(name="avg_npc_687_1#2$1")]
[name="乔万娜"]但是，我始终觉得，有些事应当适可而止。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]我们是既得利益者，我们抢占了太多的东西，我不会自称善良，但至少，我们不能忘记，有些事是我们不能做的。
[Character(name="avg_npc_687_1#1$1")]
[name="乔万娜"]你可以说是原则，也可以说是一点无聊的坚持。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]时代变了，乔万娜。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]新的时代，需要新的准则。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]那一套老人们信奉的所谓道义，该被抛弃了。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]即使我们不做，也会有人去做，到时候，我们就会成为被抛弃的那一方。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]难道说，看着哥伦比亚的其他家族染指那些东西，就是正确的吗？
[Character(name="avg_npc_687_1#10$1")]
[name="乔万娜"]如果是你，你会怎么做，瓦拉赫？
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]我会掌控那一切，无论是新的事物，还是旧的事物，都由我来支配。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]而不是回到一片守旧的土地上，选择对那些东西熟视无睹。
[Character(name="avg_npc_031")]
[name="罗塞蒂家族成员"]瓦拉赫，酒拿来了。
[Character(name="avg_npc_687_1#9$1")]
[name="乔万娜"]......
[Character(name="avg_npc_687_1#9$1")]
[name="乔万娜"]来吧，瓦拉赫，最后为我倒一杯。
[Character(name="avg_npc_695_1#5$1")]
[name="瓦拉赫"]好。
[Dialog]
[playsound(key="$pourwater")]
[Delay(time=3)]
[Character(name="avg_npc_687_1#9$1")]
[name="乔万娜"]是我的最爱。你早就准备好了，是吗？
[Character(name="avg_npc_695_1#5$1")]
[name="瓦拉赫"]本来是想等你回来，作为庆祝的。
[Character(name="avg_npc_687_1#9$1")]
[name="乔万娜"]呵。
[Character(name="avg_npc_687_1#9$1")]
[name="乔万娜"]好了，从现在起，你就是罗塞蒂的首领了。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]乔万娜。
[Character(name="avg_npc_687_1#2$1")]
[name="乔万娜"]动手。
[Character(name="avg_npc_695_1#2$1")]
[name="瓦拉赫"]......！
[Character(name="avg_npc_695_1#1$1")]
[Delay(time=0.5)]
[Character(fadetime=0.3)]

... (全文15928字符)
```

### level_act21side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[delay(fadetime=1)]
莱昂图索忘了那一天发生了什么。
那时候他还太小了。
只有两件事是确定的。
那一天，不是母亲的忌日。
那一天，是他唯一一次看到父亲有些失落的样子。
他走过阴雨连绵的街道，看到父亲坐在雨中的教堂边，没有撑伞。
他试图跑过去为父亲撑伞，却在中途跌倒了。
父亲将他抱起来。那一天的雨比往常要大一些，他看不清父亲的表情，却敏锐地察觉到父亲的狼狈。
他还记得，父亲在那时，问了他一个问题——
没有家族的叙拉古，会变得更好吗？
[Character]
[dialog]
[Background(image="33_g7_reception",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_690_1#5$1")]
[name="德米特里"]莱昂，莱昂！
[Character(name="avg_npc_690_1#5$1")]
[name="德米特里"]醒醒！
[Character(name="avg_427_vigil_1#2$1")]
[name="莱昂图索"]嘶——
[Character(name="avg_427_vigil_1#2$1")]
[name="莱昂图索"]德米特......
[Character(name="avg_npc_690_1#5$1")]
[name="德米特里"]你怎么会倒在这里？首领呢？你们被袭击了吗？
[Character(name="avg_427_vigil_1#7$1")]
[name="莱昂图索"]不......是父亲他......
[Character(name="avg_427_vigil_1#4$1")]
[name="莱昂图索"]对了，父亲，父亲他人呢？！
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]没人知道首领的行踪......而且，刚才在广播里，卢比奥把我们和萨卢佐联手的事情捅了出去。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]他还污蔑我们两家要联手夺城对付西西里夫人，现在，所有家族都在盯着我们。
[dialog]
[character]
没有家族的叙拉古，会变得更好吗？
[Character(name="avg_427_vigil_1#7$1")]
[name="莱昂图索"]这也不算污蔑，不是吗？
[Character(name="avg_npc_690_1#5$1")]
[name="德米特里"]莱昂？
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]我知道父亲想要干什么了。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_lungmencommand",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Character(name="avg_npc_701_1#1$1")]
[name="活泼的技术人员"]没想到，这个叫卢比奥的人，居然......
[Character(name="avg_npc_697_1#1$1")]
[name="冷静的技术人员"]真是个蠢货。
[Character(name="avg_npc_701_1#1$1")]
[name="活泼的技术人员"]说什么呢，他明明是个好人！
[Character(name="avg_npc_697_1#1$1")]
[name="冷静的技术人员"]我只是觉得，他这么说又有什么用呢。
[Character(name="avg_npc_697_1#1$1")]
[name="冷静的技术人员"]好不容易坐上了那个位置，说了几句好话就死了。
[Character(name="avg_npc_697_1#1$1")]
[name="冷静的技术人员"]这样的生命，也太没有价值了。
[Character(name="avg_npc_701_1#1$1")]
[name="活泼的技术人员"]......你在哭吗？
[Character(name="avg_npc_697_1#1$1")]
[name="冷静的技术人员"]我没有。
[Character(name="avg_npc_701_1#1$1")]
[name="活泼的技术人员"]......要纸巾吗？
[Character(name="avg_npc_697_1#1$1")]
[name="冷静的技术人员"]谢谢。
[character]
[dialog]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[Character(name="avg_npc_685_1#1$1",fadetime=1)]
[Delay(time=3)]
[Character(name="avg_npc_701_1#1$1")]
[name="活泼的技术人员"]......什么人？这里禁止无关人员进入。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]我是贝洛内家族的领袖，各位专家可以叫我贝纳尔多。
[Character(name="avg_npc_701_1#1$1")]
[name="活泼的技术人员"]欸，贝洛内家族的......领袖？！
[Character(name="avg_npc_697_1#1$1")]
[name="冷静的技术人员"]......堂堂十二家族之一的领袖怎么会来这里？
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]如果我没记错的话，这里应该是即将分离出去，成为新移动城市核心区的次级核心区指挥塔。
[Character(name="avg_npc_697_1#1$1")]
[name="冷静的技术人员"]......是又如何。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]那么，有一件事情想要拜托各位。
[Character(name="avg_npc_701_1#1$1")]
[name="活泼的技术人员"]你......您要做什么？
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]启动次级核心区的分离程序。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g7_reception",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_690_1#5$1")]
[name="德米特里"]......这不可能。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]但这样能够解释一切。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]父亲告诉你的，要掀起所有家族之间的撕咬，逼得西西里夫人下场的计划，就只是一个幌子。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]他从一开始，就把贝洛内家族也当成了筹码。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]眼下的这一切，都是他算计好的。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]一切，都是为了得到一个没有家族的叙拉古。
[Character(name="avg_npc_690_1#6$1")]
[name="德米特里"]这个国家最强盛的家族的领袖，竟然想要毁灭所有家族......你要我怎么相信......
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]你只能相信，德米特。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]你刚才说，其他家族在盯着我们，是吗？
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]对，就算他们信了卢比奥的话，也没有多少家族立刻就敢轻举妄动。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]但恐怕也只是时间问题。
[Character(name="avg_427_vigil_1#7$1")]
[name="莱昂图索"]导火索已经点燃了......
[dialog]
[character]
没有家族的叙拉古，会变得更好吗？
父亲，这就是你一直以来真正的想法。
所以你才会在一开始让德米特来试探我。
但是，你希望我怎么做？
我又能怎么做？
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]莱昂。
[Character(name="avg_427_vigil_1#7$1")]
[name="莱昂图索"]嗯？
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]......你说过，你会以你的方式来顾全大局，莱昂。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]我说过。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]那你就该打起精神来。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]无论如何，现在是危急关头，首领不在，你就是这个家族的领袖。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]我们必须立刻行动。
[Character(name="avg_427_vigil_1#6$1")]
[name="莱昂图索"]......我知道。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]......去告诉萨卢佐，就说我要见阿尔贝托。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]然后，你去找罗塞蒂的瓦拉赫。
[Character(name="avg_npc_690_1#9$1")]
[name="德米特里"]你的意思是......我明白了。
[dialog]
[PlaySound(key="$rungeneral", volume=0.6)]
[character(fadetime=1)]
[delay(time=2)]
[Character(name="avg_427_vigil_1#2$1")]
[name="莱昂图索"]......
[dialog]
[character]
我又希望自己怎么做？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_lungmencommand",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]通过卡拉奇的事迹建立共情，你让人们相信，你真的是单纯地想要替他复仇而选择了引火上身。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]直到最后的最后，你才终于表露了一点自己的心迹。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]隐忍至此，令人敬佩，卢比奥。
[Character(name="avg_npc_685_1#1$

... (全文34099字符)
```

### level_act21side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g2_srcalley",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]啧——结果还是让他走了。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]他在中途就已经不想跟我们打了。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]你难道没有感觉吗，他如果真的想杀了我们，也只是时间问题。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]他只是不想浪费那个时间而已。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]别小看任何一个叙拉古家族。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]你搞错了一件事。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]我从没小看过任何一个叙拉古家族。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]我认真地把每一个家族都视作我的敌人。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]包括贝洛内在内。
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.2, block=true)]
[PlaySound(key="$d_sp_chixiaobadao",volume=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]会不会有点太着急了？
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]看起来你也不怎么惊讶。
[Character(name="avg_npc_690_1#4$1")]
[name="德米特里"]既然你会背叛你的领袖，我又怎么能相信你会诚心和我们结盟。
[Character(name="avg_npc_690_1#4$1")]
[name="德米特里"]但我必须提醒你，现在确实不是时候。
面对瓦拉赫的利刃，德米特里却没有丝毫动摇，反而将头转向身边的手下。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]城内的状况如何？
[Character(name="avg_npc_698_1#1$1")]
[name="贝洛内家族成员"]......很糟糕。
[name="贝洛内家族成员"]所有家族都已经知道次级核心区分离程序的启动。
[name="贝洛内家族成员"]贝洛内和萨卢佐已经成为众矢之的。
[name="贝洛内家族成员"]就在刚才，其他家族的成员也对我们发动了攻击。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]我让你重点关注的事情呢？
[Character(name="avg_npc_698_1#1$1")]
[name="贝洛内家族成员"]您猜得没错......
[name="贝洛内家族成员"]从我们安插在其他家族的楔子传回来的情报看，虽然贝洛内和萨卢佐成为众矢之的，但这并不是他们关注的重点。
[name="贝洛内家族成员"]如今城内的混乱，对所有家族来说，都是求之不得的。
[name="贝洛内家族成员"]被西西里夫人压制许久的积怨，正在不断爆发。
[name="贝洛内家族成员"]以瓜分贝洛内和萨卢佐这两块蛋糕为由头爆发的冲突，乃至单纯想要借此一雪前耻的家族恩怨......
[name="贝洛内家族成员"]所有的家族都或主动或被动地卷了进来。
[Character(name="avg_npc_690_1#9$1")]
[name="德米特里"]（低声）......首领，这就是你想要的结果，是吗。
[Character(name="avg_npc_690_1#9$1")]
[name="德米特里"]（低声）你果然，背叛了我们。
[Character(name="avg_npc_690_1#3$1")]
[name="德米特里"]......
[Character(name="avg_npc_690_1#3$1")]
[name="德米特里"]瓦拉赫，你不是个蠢货，你应该能明白，我们现在在这里冲突没有任何好处。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]先解决掉一个大麻烦，难道不算好处？
[Character(name="avg_npc_690_1#9$1")]
[name="德米特里"]罗塞蒂在哥伦比亚难道就一呼百应？
[Character(name="avg_npc_690_1#9$1")]
[name="德米特里"]你真的妄想仅靠你们自己就吞下整个叙拉古？
[Character(name="avg_npc_690_1#9$1")]
[name="德米特里"]好好选择自己的盟友，瓦拉赫。
[Dialog]
[Character(name="avg_npc_695_1#1$1")]
[PlaySound(key="$d_avg_drawsword")]
[Delay(time=1)]
[name="瓦拉赫"]啧。
[Character(name="avg_npc_690_1#3$1")]
[name="德米特里"]别难过了。
[Character(name="avg_npc_690_1#3$1")]
[name="德米特里"]如果不是形势所迫，我也不是很想和你结盟。
[Character(name="avg_npc_690_1#9$1")]
[name="德米特里"]莱昂呢？
[Character(name="avg_npc_698_1#1$1")]
[name="贝洛内家族成员"]......
[Character(name="avg_npc_690_1#9$1")]
[name="德米特里"]怎么，他没有回家族吗？
[Character(name="avg_npc_698_1#1$1")]
[name="贝洛内家族成员"]是的，并且我们没有找到少爷的踪迹，他显然是有意避开了我们。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]......
[Character(name="avg_npc_690_1#6$1")]
[name="德米特里"]莱昂，你难道也......
[Character(name="avg_npc_690_1#6$1")]
[name="德米特里"]......
[Character(name="avg_npc_690_1#3$1")]
德米特里深吸了一口气。
此时此刻，多想无益，他必须面对当下的现实。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]既然所有家族都开始了互相撕咬，那么，眼下，就是我们夺取次级核心区的最佳时机。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]只有先控制住了那里，我们才有未来。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g11_mansionhall",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[Character(name="avg_npc_686_1#8$1",fadetime=1,block=true)]
[delay(time=2)]
[Character(name="avg_npc_698_1#1$1")]
[name="萨卢佐家族成员"]首领。
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]情况如何？
[Character(name="avg_npc_698_1#1$1")]
[name="萨卢佐家族成员"]很混乱。
[Character(name="avg_npc_698_1#1$1")]
[name="萨卢佐家族成员"]有许多家族的人在趁乱进攻我们，而我们下面的人也开始了反击。
[Character(name="avg_npc_698_1#1$1")]
[name="萨卢佐家族成员"]局势已经一发不可收拾了。
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]真有意思，这不可能是莱昂图索那个小崽子的意思。
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]现在想来，贝纳尔多，虽然拉普兰德只是一时起意，但你在那时就把我们萨卢佐也算计进去了，对吧。
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]西西里定下的铁则摇摇欲坠，这几十年来叙拉古之所以是叙拉古的根基被你一把火点燃。
[Character(name="avg_npc_686_1#3$1")]
[name="阿尔贝托"]这就是你想要看到的？为什么？
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]拉普兰德呢？
[Character(name="avg_npc_698_1#1$1")]
[name="萨卢佐家族成员"]从昨天开始，就联络不上她。
[Character(name="avg_npc_686_1#8$1")]
[name="阿尔贝托"]......罢了，罢了。
[Character(name="avg_npc_698_1#1$1")]
[name="萨卢佐家族成员"]首领，现在城里局势一片混乱，我们还要继续静观其变吗？
[Character(name="avg_npc_686_1#8$1")]
[name="阿尔贝托"]哼，现在，就算萨卢佐想要置身事外，也不可能做到了。
[Character(name="avg_npc_686_1#4$1")]
[name="阿尔贝托"]贝纳尔多那个老东西，连这一步都算到了。
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]让外面的人都回来。
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]然后，派一部分精锐去次级核心区的指挥塔，贝洛内和罗塞蒂，不会放过那里。
[Character(name="avg_npc_698_1#1$1")]
[name="萨卢佐家族成员"]您是指——
[Character(name="avg_npc_686_1#4$1")]
[name="阿尔贝托"]我对那座新城市没有兴趣，但背叛我的人也休想得到它。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="26_g6_laterano_chapelin",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[Character(name="avg_427_vigil_1#4$1")]
[name="莱昂图索"]父亲！
[Character(name="avg_npc_685_1#2$1")]
[name="贝纳尔多"]莱昂......没想到你能找到这里。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]我也只是凭着记忆找到这里的。
[Character(name="avg_npc_685_1#2$1")]
[name="贝纳尔多"]既然来了，就坐一坐吧。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]父亲，我已经理解了

... (全文29499字符)
```

### level_act21side_10_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_lungmencommand",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]侦察完毕，没有敌人。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]他们提供的路线图还真厉害啊，我们居然一路上没怎么遇到阻碍，就最先抵达了这里。
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]新城区的设计，使用的都是来自哥伦比亚的技术。
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]其中有许多家族成员们完全不曾了解的功能。
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]比如说，在我们通过之后，直接通往这座指挥塔的道路如今被封锁了。
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]其他的一些路口也或多或少被他们用一些技术手段封锁了。
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]加上，我们在路上也看到了。
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]家族之间的斗争已经逐渐蔓延开了，恐怕，大部分家族即使想要对指挥塔动手，也会被其他家族绊住吧。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]而且，他们根本想不到，指挥塔已经被我们占领了。
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]是的。但是，还不到放心的时候。
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]无论是贝洛内，罗塞蒂，还是萨卢佐，至少这三个家族，绝不会放弃这个次级核心区，他们一定会来的。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]有我和德克萨斯在，安心啦。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]......抱歉，我本意并不想把你们也卷进来。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]我是自愿的。
[Character(name="avg_103_angel_1#10$1")]
[name="能天使"]我也是自愿的！作为报酬，你可以之后告诉我，哪里的披萨比较好吃。
[Character(name="avg_4065_judge_1#9$1")]
[name="拉维妮娅"]好。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]......
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]你刚才说，这些技术来自哥伦比亚。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]对，罗塞蒂家族提供了不少支持，所以，我确实也有些担心他们会有突破的方法。
[Character(name="avg_1028_texas2_1#8$1")]
[name="德克萨斯"]......告诉我，如果他们有必经之路，会是哪里？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g1_srcstreet",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[dialog]
[character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=0.3, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$e_skill_skulsrsword",volume=0.7)]
[Delay(time=1)]
[Character(name="avg_npc_031",name2="avg_npc_031")]
[Delay(time=0.5)]
[playsound(key="$bodyfalldown2",volume=0.7)]
[Character(fadetime=0.5)]
[Delay(time=1.5)]
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]......
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]不对劲。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]你也感觉到了吗。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]虽然其他家族的阻碍也是一部分原因......
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]但是，如果说刚才那道大门，可能是因为某些意外而被启动了。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]那么我们绕路绕到现在，我基本可以确定，这些封锁，绝对是故意的。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]......你是说，有人先我们一步？
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]而且，他们很了解这个区域的构造。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]......而了解这些的，应该是我们罗塞蒂的人。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]或者，参与了这个次级核心区改造的人。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]......先不论究竟是谁。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]你知道该如何突破？
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]......我可以试试，我手下应该有人知道。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]太浪费时间了。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]而且......
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]如果这真的是有人刻意而为之，那一定会为此上保险。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]我知道你想说什么。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]虽然我们的合作也谈不上愉快，不过，看起来也就到此为止了。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]是啊。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]......
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]贝洛内的，某种意义上，我们也算是同病相怜了。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]别把我和你相提并论。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]难道不是吗？
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]我看得出来，你也是那种看起来很聪明，实际上忠心得要命的蠢货。
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]别给自己脸上贴金了。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]我不是在为自己辩解，我知道自己在做什么，我不后悔。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]但是你呢，如果真的如你所说，你的首领是这一切的始作俑者，而你的兄弟，或许也要站在你的对立面。
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]你真的下得了手吗？
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]你真的会得到你想要的东西吗？
[Character(name="avg_npc_690_1#7$1")]
[name="德米特里"]你呢，你得到了吗？
[Character(name="avg_npc_695_1#1$1")]
[name="瓦拉赫"]没有，我问心有愧，却别无他法。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_lungmencommand",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_699_1#1$1")]
[name="法庭护卫"]阁下，我发现这座指挥塔的技术人员都躲在一间屋子里。
[Character(name="avg_npc_699_1#1$1")]
[name="法庭护卫"]他们想要和你聊聊。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]好。
[Dialog]
[Character]
[Character(name="avg_npc_697_1#1$1",fadetime=1)]
[Delay(time=1)]
[name="冷静的技术人员"]你是......法官阁下？！
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]别紧张，我不会伤害你们。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]我既不代表某一个家族，也不代表西西里夫人。
[Character(name="avg_npc_697_1#1$1")]
[name="冷静的技术人员"]......那你代表什么？
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]现在的我不代表任何东西。
[Character(name="avg_npc_697_1#1$1")]
[name="冷静的技术人员"]......我知道了。
[name="冷静的技术人员"]只要你不伤害我们，我可以帮你们一些忙。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]......我想问你一个问题。
[Character(name="avg_npc_697_1#1$1")]
[name="冷静的技术人员"]嗯？
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]是谁让你们启动了次级核心区的分离程序，是贝洛内家族的人吗？
[Character(name="avg_npc_697_1#1$1")]
[name="冷静的技术人员"

... (全文27111字符)
```

### level_act21side_10_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g6_newtown_street",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$calamity_intro",key="$calamity_loop", volume=0.6)]
[Delay(time=1)]
[Character(name="avg_npc_688_1#1$1",fadetime=0.3)]
[bgeffect(name="$eb_wlfmster_eye_02",layer=1)]
[Blocker(a=0.8, r=0, g=0, b=0, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_wolflordattack",volume=0.7)]
[Blocker(a=0, fadetime=1, block=false)]
[Delay(time=1)]
[bgeffect(layer=1)]
[PlaySound(key="$d_sp_ballista",volume=1.0)]
[playsound(key="$e_skill_skulsrsword",volume=0.7)]
[playsound(key="$d_avg_wolflordclaw",volume=0.7)]
[dialog]
[character(fadetime=0.5)]
[Delay(time=0.8)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Character(name="avg_427_vigil_1#4$1")]
[Blocker(a=0, fadetime=0.3, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$b_char_defboost")]
[Delay(time=0.5)]
[Character(name="avg_427_vigil_1#4$1",fadetime=0.3)]
[name="莱昂图索"]扎罗，狼之主之间不是约定好了，不会干涉凡人的事务吗！
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]我改变主意了，因为贝纳尔多毁了我的计划！
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]我苦心培养了他六十八年。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]而他，竟敢以自尽来葬送我的胜利！！
[Character(name="avg_427_vigil_1#4$1")]
[name="莱昂图索"]你......说什么？
[Character(name="avg_427_vigil_1#5$1")]
[name="莱昂图索"]父亲......他自尽了？
[character]
[dialog]
莱昂图索的脑中瞬间闪过父亲对狼之主以及这场游戏的解释。
他猛然明白，父亲在教堂对自己说的那些话，既是对自己的承认——
同时也是遗言。
父亲在一开始就做好了自我了结的准备。
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]侮辱狼之主的代价是巨大的。
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]即便他已经死去，我依然要让他的血脉从此断绝于这片大地之上。
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]贝纳尔多之子，今天，你必须代替你的父亲付出代价。
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]这份代价，就是他的血脉，你的性命！！！
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]......
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]代价？
[Character(name="avg_427_vigil_1#4$1")]
[name="莱昂图索"]你说代价？
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]父亲确实错了，但他理想的根源，却始终是改变这个时代。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]他渴望着一个没有家族的叙拉古，并为此谋划了一生。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]我原以为，父亲只是将自己的家族作为筹码。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]我以为他在此刻发难，只因为时机正好。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]但现在，我知道了。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]他觉得没有时间了，错过这个机会，他就再也无法在实现自己理想的同时，完成对你的复仇。
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]我在他短暂的一生中，对他倾囊相授，换来的却是他的背叛！
[Character(name="avg_427_vigil_1#6$1")]
[name="莱昂图索"]......你不会明白的。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]高高在上，自以为掌控一切的狼之主。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]父亲甚至将自己的性命，也作为了筹码。
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]即使以自己的性命为代价，即使是违抗你这个傲慢的存在，他也要将自己的理想付诸现实！
[Character(name="avg_427_vigil_1#4$1")]
[name="莱昂图索"]该为此付出代价的是你！
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]无知！
[dialog]
[playsound(key="$d_avg_wolflordattack",volume=0.7)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=0.3, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista",volume=1.0)]
[playsound(key="$e_skill_skulsrsword",volume=0.7)]
[playsound(key="$d_avg_wolflordclaw",volume=0.7)]
[Delay(time=1)]
[Character(name="avg_1028_texas2_1#7$1")]
[dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista",volume=1.0)]
[PlaySound(key="$swordtsing1", volume=1)]
[Delay(time=2)]
[Character(name="avg_103_angel_1#10$1")]
[name="能天使"]德克萨斯，欢迎回来！
[Character(name="avg_103_angel_1#9$1")]
[name="能天使"]你那边搞定了？
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]嗯。
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]该解决这边的麻烦了。
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]最后的德克萨斯。
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]不要忘记，当年是谁许诺你可以离开叙拉古的掌控。
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]现在，你竟敢忤逆我？
[Character(name="avg_1028_texas2_1#1$1")]
[name="德克萨斯"]我已经完成了与贝纳尔多的约定，我不再欠你什么。
[Character(name="avg_npc_688_1#1$1")]
[name="扎罗"]愚昧！
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=0.3, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista",volume=1.0)]
[playsound(key="$e_skill_skulsrsword",volume=0.7)]
[playsound(key="$d_avg_wolflordattack",volume=0.7)]
[Delay(time=0.2)]
[PlaySound(key="$d_sp_ballista",volume=1.0)]
[playsound(key="$e_skill_skulsrsword",volume=0.7)]
[playsound(key="$d_avg_wolflordclaw",volume=0.7)]
[dialog]
[character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=0.3, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$e_skill_skulsrsword",volume=0.7)]
[Delay(time=2)]
[Character(name="avg_4065_judge_1#12$1")]
[name="拉维妮娅"]......贝纳尔多，自尽了？
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0,

... (全文36489字符)
```

### level_act21side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act21side/IS01.mp4")]
```

### level_act21side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="29_g7_mainstreet_n",screenadapt="coverall")]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[Delay(time=4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
哥伦比亚的街道整体上要比叙拉古宽敞许多，也更为繁华。
但走在路上，时而会有一种空旷感，仿佛自己不属于这里。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Image(fadetime=0)]
[Background(image="29_g8_alley_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[Character(name="avg_npc_523_1#1$1",name2="avg_npc_523_1#1$1",fadetime=1)]
[Delay(time=2)]
[Character(name="avg_npc_523_1#1$1",name2="avg_npc_523_1#1$1",focus=1)]
[name="轻佻的哥伦比亚人"]喂，洗车的，我听说你来自叙拉古，问你个问题。
[Dialog]
[Character]
[Character(name="avg_npc_693_1#4$1",fadetime=1)]
[Delay(time=2)]
[name="洗车工"]我这里只负责洗车，不负责回答问题。
[Dialog]
[Character(name="avg_npc_693_1#4$1",name2="avg_npc_523_1#1$1")]
[characteraction(name="right", type="move", xpos=100, fadetime=0, block=false)]
[characteraction(name="right", type="move", xpos=-150, fadetime=0.6, block=false)]
[Delay(time=0.6)]
[CameraShake(duration=0.5, xstrength=5, ystrength=5, vibrato=10, randomness=20, fadeout=true, block=false)]
[PlaySound(key="$d_avg_clothmovement",volume=0.7)]
[Delay(time=1)]
[Character(name="avg_npc_693_1#4$1",name2="avg_npc_523_1#1$1",focus=2)]
[name="轻佻的哥伦比亚人"]别这么不近人情嘛，朋友。
[name="轻佻的哥伦比亚人"]放心，我们不打算找你这种一身穷酸味的乡巴佬麻烦。
[name="轻佻的哥伦比亚人"]今天应该有一群你的老乡进城了，我们想知道他们在哪。
[Character(name="avg_npc_693_1#4$1",name2="avg_npc_523_1#1$1",focus=1)]
[name="洗车工"]你找他们做什么？
[Character(name="avg_npc_693_1#4$1",name2="avg_npc_523_1#1$1",focus=2)]
[name="轻佻的哥伦比亚人"]做什么？嗯......叙叙旧？
[Character(name="avg_npc_693_1#4$1",name2="avg_npc_523_1#1$1",focus=1)]
[name="洗车工"]叙旧。
[Character(name="avg_npc_693_1#4$1",name2="avg_npc_523_1#1$1",focus=2)]
[name="轻佻的哥伦比亚人"]嘿，毕竟我爷爷总是告诫我，不要忘了自己是个叙拉古人。
[Character(name="avg_npc_693_1#4$1",name2="avg_npc_523_1#1$1",focus=1)]
[name="洗车工"]你看上去，完全不像是一个......“叙拉古人”。
[Character(name="avg_npc_693_1#4$1",name2="avg_npc_523_1#1$1",focus=2)]
[name="轻佻的哥伦比亚人"]我？哈，叙拉古人！
[name="轻佻的哥伦比亚人"]朋友，哥伦比亚才是未来！有金券才有未来！
[character]
哥伦比亚家族的年轻人们都从自己的祖辈那里听说过他们来自叙拉古。
但他们总是不屑一顾。
[Character(name="avg_npc_693_1#4$1",name2="avg_npc_523_1#1$1",focus=1)]
[name="洗车工"]......
[name="洗车工"]但你们的根始终在叙拉古。
[Character(name="avg_npc_523_1#1$1")]
[name="愉快的哥伦比亚人"]只有那些老古董还会纠结这种说法。
[name="愉快的哥伦比亚人"]哥伦比亚是个属于开拓的国家！根？我们可不需要根。
[Dialog]
[Character(name="avg_npc_693_1#4$1",name2="avg_npc_523_1#1$1",focus=2)]
[name="轻佻的哥伦比亚人"]没错，乡巴佬，识相点告诉我们，你不会希望自己的小店......遇上点“意外”吧？
[Character(name="avg_npc_693_1#4$1",name2="avg_npc_523_1#1$1",focus=1)]
[name="洗车工"]......他们在街对面那家酒吧里。
[Character(name="avg_npc_523_1#1$1")]
[name="愉快的哥伦比亚人"]你很聪明，朋友，和你一样头脑灵光的狼崽可不多见。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[Character(fadetime=0.5)]
[Delay(time=1)]
开拓同时意味着混乱，哥伦比亚的家族们在这种混乱中逐渐失去了应有的秩序。
而对叙拉古来说，秩序高于法律。
[dialog]
[PlaySound(key="$d_avg_open_box",delay=0.5)]
[delay(time=1)]
洗车工对他们的喧闹置若罔闻，只是转身慢条斯理地打开柜子，从里面拿出了一把他再熟悉不过的工具。
[dialog]
[PlaySound(key="$swordtsing3",volume=0.6)]
[delay(time=1)]
它锋利又沉重，洗车工前不久才仔细打磨过。刃口反射的光芒会让人想起叙拉古的月亮。
[dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[delay(time=1)]
然后，他缓缓走向那些正背过身去，洋洋得意的蠢货们。
像一个只是想在开店前清洗一下地板的洗车工。
像一个叙拉古人。
[Dialog]
[stopmusic(fadetime=3)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_knife")]
[PlaySound(key="$blooddrop",delay=0.5)]
[Blocker(a=0.05, r=0.7, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Delay(time=1)]
[Character(name="char_102_texas_1#4")]
[PlaySound(key="$d_avg_clothmovement",volume=0.7)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
德克萨斯猛地睁开眼。
[Character(name="char_102_texas_1#1")]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
映入眼帘的是在黑暗中也能清晰辨认的，被能天使强行贴上的海报。
手中传来的是可颂换季时以特价为由硬卖给她的绒毛被的触感。
助眠用的空的CD也还在播放。
这一切让她微微松了一口气。
她清楚地知道这个梦的内容没有发生过，哥伦比亚的家族并没有先找叙拉古来客麻烦的机会。
而那名洗车工，她也只是有过一面之缘罢了。
一个除了提醒自己叙拉古人身份以外，毫无意义的梦。
而自从来到龙门，她已经许久没有做过这个梦了。
事到如今，做这个梦又有什么意义呢。
她下意识地想去看看窗外的夜色。
[character]
[Dialog]
[PlaySound(key="$d_avg_footstep_stonestep", volume=0.6)]
[delay(time=4)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Image(image="33_i01", xScale=1.15, yScale=1.15,x=-200,y=-150, fadetime=1.5)]
[ImageTween(xScale=1.15, yScale=1.15,xFrom=-200,y=-150, xTo=-170,duration=10, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[Delay(time=3)]
[stopmusic(fadetime=3)]
[Character]
月色依旧皎洁。
龙门的夜景依旧缤纷多彩。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="33_i01", xScale=1.0, yScale=1.0,x=-140,y=-80, fadetime=0)]
[ImageTween(xScaleFrom=1.0, yScaleFrom=1.0, xScaleTo=0.85, yScaleTo=0.85,xTo=0,yTo=0,duration=50, block=false)]
然而，在那之中，有一个与周围的一切都格格不入的存在。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[playMusic(intro="$plot_intro",key="$plot_loop", volume=0.6)]
[delay(time=1)]
窗外，月下的房顶上，有一头狼正在盯着自己。
若是周遭的一切能被称为文明的造物，那这头狼无疑是荒野的象征。
他绝不适合，也绝不应该出现在这里。
但他却堂而皇之地出现了，并且，他的身姿仿佛凌驾于周遭一切之上。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.7, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="出来吧，到你履行约定的时候了。",x=300, y=370, alignment="center", size=24, delay=0.04, width=700 )]
[Subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="德克萨斯"]......
德克萨斯在一瞬间理解了自己为何会做那个梦。
梦与现实并无连接。
但梦时而是一种预兆。
而她在今夜做的这个梦，毫无疑问意味着——
她的过去来敲门了。
[Dialog]
[Delay(time=0.5)]
[bgeffect(name="$eb_wlfmster_01",flip = 1,layer=1)]
[Delay(time=0.8)]
[PlaySound(key="$d_avg_wolflordroar_3",volume=0.7)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=

... (全文51827字符)
```

### level_act21side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g7_reception",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="激进的家族成员"]为什么我从来没听说过这事？！
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",focus=2)]
[name="忠诚的家族成员"]我也没有听说过。
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_698_1#1$1",focus=1)]
[name="激进的家族成员"]难道说，是她的独断专行......
[Dialog]
[character]
[Character(name="avg_npc_686_1#1$1",fadetime=1)]
[Delay(time=1)]
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]无妨。
[name="阿尔贝托"]是我默许了她的行动。
[Character(name="avg_npc_698_1#1$1")]
[name="激进的家族成员"]老爷！您原本就有这样的想法？
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]雪中送炭和锦上添花 ，你选哪一种？
[Character(name="avg_npc_686_1#7$1")]
[name="阿尔贝托"]贝洛内想要一手遮天，哼，哪有那么简单。
[Character(name="avg_npc_686_1#8$1")]
[name="阿尔贝托"]如果承担一点骂名就能从贝纳尔多身上割一块肉下来，那又有何妨？
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]我明白了。
[name="忠诚的家族成员"]那么，我们现在应该怎么做？
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]备车，我要去见一见我的女儿。
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]是。
[Character(name="avg_npc_686_1#10$1")]
[name="阿尔贝托"]对了，丹布朗现在在哪？
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]丹布朗？他似乎在一家洗车店工作。
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]把地址给我。
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]您要把他召回来......吗？
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]我没有同意过他离开家族。
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]......我明白了。
[Character(name="avg_npc_686_1#1$1")]
[name="阿尔贝托"]还有，准备一场宴会。
[Character(name="avg_npc_698_1#1$1")]
[name="忠诚的家族成员"]您是要......
[Character(name="avg_npc_686_1#9$1")]
[name="阿尔贝托"]宴请贝洛内少爷。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="bg_prison_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_npc_699_1#1$1",name2="avg_npc_541_1#1$1",fadetime=1)]
[Delay(time=1)]
[character(fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_npc_699_1#1$1",name2="avg_npc_542_1#1$1",fadetime=1)]
[Delay(time=1.5)]
[characteraction(name="right", type="shake", power=10, times=100, fadetime=0.3, block=false)]
[Character(name="avg_npc_699_1#1$1",name2="avg_npc_542_1#1$1",focus=2)]
[name="甘比诺"]放开我！
[Character(name="avg_npc_699_1#1$1")]
[name="护卫"]阁下，根据拉普兰德提供的线索，我们抓到了这两个杀手。
[name="护卫"]经过指认，他们确实参与了针对莱昂图索的刺杀。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]......你们两个认识她吗？
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]嗨。
[Character(name="avg_npc_698_1#1$1",name2="avg_npc_541_1#1$1",focus=2)]
[name="卡彭"]啧，拉普兰德，我就知道跟你扯上关系绝对不会有好事。
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]在叙拉古坐牢，难道不是一种新奇的体验吗？
[Character(name="avg_4065_judge_1#5$1")]
[name="拉维妮娅"]......
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]把他们两个关起来。
[Character(name="avg_npc_699_1#1$1",name2="avg_npc_699_1#1$1")]
[name="护卫"]是。
[Dialog]
[PlaySound(key="$d_gen_doorclose")]
[Character(name="avg_npc_541_1#1$1",name2="avg_npc_542_1#1$1",focus=-1)]
[Delay(time=0.5)]
[Character(fadetime=0.5)]
[Delay(time=1.5)]
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]是你在现场拖住了切利尼娜，并且派人用炸弹炸死了卡拉奇......
[name="拉维妮娅"]你还是坚持这个供词吗？
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]真多疑啊，法官小姐。
[name="拉普兰德"]对你来说，对贝洛内来说，快点结案不都是一件好事吗？
[name="拉普兰德"]是我，还是德克萨斯，有区别吗？
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]......
[Character(name="avg_npc_683_1#9$1")]
[name="拉普兰德"]说真的，法官小姐，你该把我处死。
[name="拉普兰德"]我只是一个被家族除名的弃子而已，你努力一下应该是能做到的。
[Character(name="avg_npc_683_1#5$1")]
[name="拉普兰德"]想象一下，我的死能够给叙拉古的司法公正带来多么正面的影响。
[Character(name="avg_npc_683_1#3$1")]
[name="拉普兰德"]这难道不值得你来尝试吗？
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]我不知道你究竟想做什么。
[Character(name="avg_4065_judge_1#7$1")]
[name="拉维妮娅"]但是，如果你真的是凶手，我会这么做的，拉普兰德·萨卢佐。
[Character(name="avg_4065_judge_1#8$1")]
[name="拉维妮娅"]不过，现在，我还要去见一个人。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g7_reception",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_npc_685_1#1$1",fadetime=1)]
[Delay(time=2)]
[Character(name="avg_npc_690_1#1$1")]
[name="德米特里"]首领，您回来了。
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]去休息吧，这段时间，你也辛苦了。
[Character(name="avg_npc_690_1#1$1")]
[name="德米特里"]是。
[Dialog]
[Character(fadetime=0.5)]
[PlaySound(key="$doorclosequite", volume=0.7)]
[Delay(time=2)]
[Character(name="avg_427_vigil_1#7$1",fadetime=0.5)]
[Delay(time=1)]
[name="莱昂图索"]......
[Character(name="avg_npc_685_1#5$1")]
[name="贝纳尔多"]不服气？
[Character(name="avg_427_vigil_1#1$1")]
[name="莱昂图索"]我倒想知道，我要怎样才能服气？
[Character(name="avg_npc_685_1#1$1")]
[name="贝纳尔多"]......跟我来。
[name="贝纳尔多"]有些事情，是时候让你知道了。
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[StopMusic(fadetime=3)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="33_g9_conferencehall",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_427_vigil_1#7$1",fadetime=0.5)]
[Delay(time=1)]
[name="莱昂图索"]为什么带我来这里？
[Character(name="avg_npc_685_1#2$1")]
[name="贝纳尔多"]吾主。
[Dialog]
[Character]
[Delay(time=0.5)]
[playMusic(intro="$plot_intro",key="$plot_loop", volume=0.6)]
[bgeffect(name="$eb_wlfmster_01",flip = 1,layer=1)]
[bgeffect(name="$eb_wlfmster_02",flip = 1,layer=1,delay=1)]
[Character(name=

... (全文32580字符)
```

### level_act21side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_hotel",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[dialog]
[character]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_4065_judge_1#1$1",fadetime=1)]
[delay(time=3)]
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]啊，真的是法官阁下！
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]你就是卢比奥阁下的女儿，是吗？
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]是的......我还以为，父亲跟我说您会来照看我是在开玩笑。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]我和我朋友都特别崇拜您。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]和我父亲那样的人一比，您简直就是政府里唯一的清流。
[Character(name="avg_4065_judge_1#4$1")]
[name="拉维妮娅"]......你和卢比奥先生关系不好吗。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]......谈不上好不好。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]我还是挺喜欢父亲的，因为他时间总是很多，经常陪我玩。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]但是，现在我也觉得，父亲这样只知道所谓明哲保身的人，实在是太没有志气了。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]曾经和他一起从基层做起的同僚，现在都飞黄腾达了。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]只有他到了这个岁数才混了一个边缘的职位，而且一点上进心都没有。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]他曾经的同僚？
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]是啊，前阵子死掉的那个建设部部长卡拉奇就是。
[Character(name="avg_4065_judge_1#8$1")]
[name="拉维妮娅"]那是个危险的位置。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]我知道......但是，我天天都能在电视上看到那个人，而且大家族的人都会对他有所礼让。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]您不觉得，如果要当官的话，就得做到那种地步才有意义吗？
[Character(name="avg_4065_judge_1#8$1")]
[name="拉维妮娅"]或许吧。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]所以，父亲这次忽然接任了建设部部长的位置，我其实是很惊讶的。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]不知道他怎么就忽然开窍了......要是他早点这么做，母亲也不会和他离婚了吧。
[Character(name="avg_4065_judge_1#4$1")]
[name="拉维妮娅"]离婚？
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]是啊，母亲也觉得父亲太窝囊了，所以前几年和他离婚了。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]不过，我母亲性格也不太好，所以我最后还是选择了跟着父亲。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]对了，法官阁下，您一定知道父亲是怎么被选为建设部部长的吧，跟我说说吧。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]......抱歉，我不知道。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]欸，好吧。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]那您在房间里随便坐坐吧。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]今天，我也不打算出去，就打算听一听父亲的就职演讲。
[Character(name="avg_4065_judge_1#8$1")]
[name="拉维妮娅"]......
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[Delay(time=3)]
[Character(name="avg_4065_judge_1#8$1")]
[name="拉维妮娅"]（卢比奥部长的房间......比想象中的整洁。）
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]很奇怪吧，父亲看起来是个邋遢的人，其实生活很规律。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]对了，他还有写日记的习惯。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]日记？
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]对，我记得，对了，就摆在这里。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]说是日记，其实我看他是想到了才会写一点上去。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]这些年断断续续加起来也就写了这么一些。
[Character(name="avg_4065_judge_1#4$1")]
[name="拉维妮娅"]随便看没关系吗？
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]没事的，父亲放在这里，就是不介意别人看到。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]我看过几次，上面写的都是些无聊的东西，要我说呀，就是一本活脱脱的中年男人生活实录，枯燥又冗长。
[Character(name="avg_npc_700_1#1$1")]
[name="卢比奥之女"]您要是有兴趣，尽管看。
[Character(name="avg_4065_judge_1#1$1")]
[name="拉维妮娅"]......
[PlaySound(key="$d_avg_paper1", volume=1)]
[dialog]
[character]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Subtitle(text="3月5日", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="餐厅偶遇卡拉奇，久违地一起小酌了一杯。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="念及往事，不禁潸然泪下。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="33_g11_mansionhall",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_698_1#1$1")]
[name="贝洛内家族成员"]卢比奥先生，这里就是您发表演讲的地方了。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]都出去吧。
[Character(name="avg_npc_698_1#1$1")]
[name="贝洛内家族成员"]但......我们接到的命令是保护您。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]没有人进得来，不是吗？
[Character(name="avg_npc_698_1#1$1")]
[name="贝洛内家族成员"]我知道了。
[Dialog]
[PlaySound(key="$doorclosequite")]
[Character(fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]......
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]啧啧，权力。
[Dialog]
[PlaySound(key="$d_avg_doorknob")]
[Delay(time=1)]
[Character(fadetime=0.5)]
[PlaySound(key="$d_avg_dragsofa")]
[Delay(time=3)]
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]用沙发把门堵住......能做的也就只有这么多了。
[Character(name="avg_npc_689_1#1$1")]
[name="卢比奥"]然后嘛......
[Character(name="avg_npc_689_1#5$1")]
[name="卢比奥"]卡拉奇，再等我一会儿，马上我就来陪你了。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_indoor_u",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[Character(name="avg_103_angel_1#2$1",fadetime=0.5)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_telephone")]
[Delay(time=0.5)]
[name="能天使"]怎么样了？
[Character(name="avg_103_angel_1#2$1",focus=-1)]
[name="空"]......医生说，对方下手的位置恰好偏离了心脏几厘米，所以没有立刻致死。
[name="空"]但是情况还是很不好。
[name="空"]德克萨斯呢？
[Character(name="avg_103_angel_1#5$1")]
[name="能天使"]嗯......
[Character]
[Dialog]
[Delay(time=1)]
[Character(name="avg_1028_texas2_1#6$1",fadetime=1)]
[Delay(time=1)]
[name="德克萨斯"]......
[Character(name="avg_103_angel_1#5$1")]
[name="能天使"]从昨天回来开始就一副失魂落魄的样子。
[Character(name="avg_103_an

... (全文31054字符)
```

### level_act21side_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="33_g2_srcalley",screenadapt="coverall")]
[playsound(key="$d_avg_rainlight_loop", loop=true, channel="a")]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playsound(key="$d_avg_shallowswalk", loop=true, channel="bgs")]
[Character(name="char_1502_crowns",fadetime=1)]
[Delay(time=1)]
[StopSound(channel="bgs", fadetime=1)]
[name="柳德米拉"]唔，尾巴弄湿了。
[name="柳德米拉"]还真是一点都没变。无论是这些脏兮兮的街，还是烦死人的雨。
[name="柳德米拉"]不知道为什么，乌萨斯的雪能要人命，可还是这里的雨更让人不爽。
[name="柳德米拉"]但愿老师家有吹风机......
[Dialog]
[Character(fadetime=0.5)]
[Delay(time=0.5)]
老师家就在这条巷子的尽头。当年，弑君者怀着一腔怒火离开了这里，为了证明自己已经足够强大，能够向笼罩她的那片阴云复仇。
如今，柳德米拉又回来了。她的努力是否有给阴沉的天空打开一丝缺口，她自己都拿不准。
或许，其实什么都没改变，或许，她只是成了更大灾难的帮凶。
还好，柳德米拉还能回到这里，她想，老师一定能告诉她接下来应该怎么办。
突然，她感到一阵恶寒。
柳德米拉原本只是以为，这来源于自己即将再度面对老师的紧张。
[StopMusic(fadetime=3)]
但马上，她意识到自己错了。
她正在控制不住地战栗。
[Dialog]
[CameraShake(duration=3, xstrength=20, ystrength=15, vibrato=20, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_shallowsrun")]
[Delay(time=1)]
[StopMusic(fadetime=2)]
[dialog]
[StopSound(channel="a", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$dooropenquite")]
[character(fadetime=0)]
[Background(image="33_g8_srcroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[playMusic(intro="$kjerag_n_intro",key="$kjerag_n_loop", volume=0.5)]
[Character(name="char_1502_crowns")]
[Delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="柳德米拉"]老师！！
[Dialog]
[Image(image="33_i16", xScale=1.6, yScale=1.6,y=300, x=350,fadetime=1)]
[ImageTween(duration=10,xTo=250, block=false)]
[Background]
[Character]
[Delay(time=2)]
[Image(image="33_i16", xScale=1.7, yScale=1.7,y=300,x=-100, fadetime=1)]
[ImageTween(duration=10,xTo=0, block=false)]
[Delay(time=2)]
[Image(image="33_i16", xScale=1.2, yScale=1.2,y=150, fadetime=1)]
[ImageTween(xScaleTo=0.88, yScaleTo=0.88, duration=30,yTo=-20, block=false)]
[Delay(time=1)]
化不开的血腥味。
她的老师仰面倒在地上，鲜血仍在向外流淌蔓延。
一把小刀掉落一边。
柳德米拉想要靠近，压住老师仍在流血的伤口，但她发现自己无法挪动一步，她连视线都无法移开。
有一股让她熟悉，又让她恐惧的气息正从阴影中浮现。
穿着红色连帽衫，有着灰色头发的狼。
[name="？？？"]真狼死了，红听了外婆的话。
[name="柳德米拉"]......是你。
[Background(image="33_g8_srcroom",screenadapt="coverall")]
[Dialog]
[Image(fadetime=1.5)]
[Delay(time=2)]
[Character(name="char_1502_crowns",name2="char_144_red_7#1",blackstart=0.15,blackend=0.4,fadetime=1)]
[characteraction(name="left", type="move", xpos=-100, fadetime=0, block=false)]
[Delay(time=1)]
[Character(name="char_1502_crowns",name2="char_144_red_7#1",focus=1)]
[name="柳德米拉"]你......做了什么......
[Character(name="char_1502_crowns",name2="char_144_red_7#1",focus=2)]
[name="红"]红是猎狼人，红听外婆的话。
[name="红"]真狼死了，真狼没有反抗。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_1502_crowns",name2="char_144_red_7#1",focus=1)]
[name="柳德米拉"]你！！
[Dialog]
[CameraShake(duration=0.5, xstrength=15, ystrength=10, vibrato=30, randomness=90, fadeout=false, block=false)]
[characteraction(name="left", type="move", xpos=300, fadetime=0.5, block=false)]
[Effect(name="$e_slash_02_s",rox=30,roy=-200,roz=-90,x=100,y=-60,layer = 1)]
[PlaySound(key="$knifegore")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_ftrub")]
[Character(name="char_1502_crowns",name2="char_empty",fadetime=0.2)]
[Delay(time=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=10, vibrato=40, randomness=90, fadeout=false, block=false)]
[name="柳德米拉"]我杀了你！
[Character(name="char_144_red_7#1")]
[name="红"]唔......红答应过凯尔希，只杀狼，你不是狼。
[Character(name="char_144_red_7#3")]
[name="红"]原来如此，她是你的凯尔希吗？怪不得你身上有狼的气味。
[Character(name="char_1502_crowns",blackstart=0.15,blackend=0.4)]
[name="柳德米拉"]呼......呼......老师明明已经没办法再战斗了，你为什么还？！
[Character(name="char_144_red_7#1")]
[name="红"]因为外婆告诉红，这就是游戏规则。
[name="红"]现在，她出局啦。
[name="红"]红要走了，红还要找别的狼，他们就在附近。
[Character(name="char_144_red_7#2")]
[name="红"]（嗅嗅）
[Character(name="char_144_red_7#7")]
[name="红"]不过，好像还有一只狼也出局了，是有人比红的动作更快吗？
[Character(name="char_1502_crowns",blackstart=0.15,blackend=0.4)]
[name="柳德米拉"]站住！
[Dialog]
[Character]
穿着红色连帽衫的狼没有回应柳德米拉的呼喊，她哼着破碎的小调，迈着轻快的步伐从柳德米拉身边掠过。
柳德米拉伸出的手停在了半空。
她突然想起，老师曾对她说：
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“柳德米拉，你知道成为我的学生意味着什么吗？”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“我已经残废了，没什么大用，你却甘愿成为我的学生，我的工具？”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“我们都会后悔的，孩子。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_1502_crowns",fadetime=0.5,blackstart=0.15,blackend=0.4)]
[Delay(time=1)]
[characteraction(name="middle", type="move", ypos=-50, fadetime=0.3,block=false)]
[CameraShake(duration=0.5, xstrength=20, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$bodyfalldown2")]
柳德米拉跪倒在地。
[name="柳德米拉"]“吞下死难者的苦”......
[StopMusic(fadetime=3)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[character(fadetime=0)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[Background(image="33_g4_srctheater",screenadapt="coverall")]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_spotlightc")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_avg_applause")]
[Delay(time=2)]
[name="激动的观众"]不愧是卡特琳娜女士酝酿了如此之久的作品。
[name="激动的观众"]切利尼娜在剧中，作为一个完美的叙拉古人形象，到最后竟才被揭示出是一个所有叙拉古人构建出的幻象。
[name="激动的观众"]但是，正因为她在市井传闻中是众所周知的完美形象，用一种共同的想象去解释她竟也是合理的。
[name="激动的观众"]最后点出她并不存在的那一幕，实在是太让我震撼了。
[name="激动的观众"]真是意味深长

... (全文15864字符)
```

### text_agenir_1_1_1

```


[dialog(head="npc_692_1",delay=1,style="self")]贝纳尔多，若是我说，你梦想中的叙拉古，恰是因为有你想要毁灭的那一切才存在，你会作何反应？
[dialog(head="npc_692_1",delay=1,style="self")]被需要的从来都不是家族，而是规则。
[dialog(head="npc_692_1",delay=1,style="self")]唉，罢了。
[dialog(head="npc_692_1",delay=1,style="self")]或许，我也老了。
[dialog(head="npc_694_1",delay=1,style="other")]哦？没想到平日里只会睡觉的老家伙，这时候倒是伤感起来了。
[dialog(head="npc_692_1",delay=1,style="self")]文......
```

### text_agenir_1_2_1

```
[dialog(head="npc_694_1",delay=1,style="other")]喝一杯吗？
[dialog(head="npc_692_1",delay=1,style="self")]免了。
[dialog(head="npc_694_1",delay=1,style="other")]无趣。
[narration(delay=1)]阿格尼尔坐到文的身边，拿起酒瓶，以与他外表不符的动作仰头灌了一口。
[dialog(head="npc_694_1",delay=1,style="other")]我还以为，你会在法院里睡到一切都结束。
[dialog(head="npc_692_1",delay=1,style="self")]我还以为，你会站在莱昂图索这头幼狼那边。
[dialog(head="npc_694_1",delay=1,style="other")]我在名义上，可是西西里手下的“巨狼之口”的一员，不是吗？
[dialog(head="npc_692_1",delay=1,style="self")]没想到你会在这时候承认这一点。
[dialog(head="npc_694_1",delay=1,style="other")]毕竟我是个矛盾的人，我不愿意承认文明的光荣，却也同样不愿意无意义地死去。
[dialog(head="npc_694_1",delay=1,style="other")]当然，你的矛盾也不比我少。
[dialog(head="npc_694_1",delay=1,style="other")]你为叙拉古制定了过去几十年的规则，但和西西里不同，你却从不觉得自己是正确的。
[dialog(head="npc_692_1",delay=1,style="self")]我只是相信，我并不是错误的。
[dialog(head="npc_694_1",delay=1,style="other")]谁知道呢。
[narration(delay=1)]文不置可否，只是猛地灌了一口手中的酒。
```

### text_agenir_1_3_1

```
[dialog(head="npc_692_1",delay=1,style="self")]你接下来有什么打算？
[dialog(head="npc_694_1",delay=1,style="other")]和过去没什么差别，哪里有好作品，我就去哪里看一看。
[dialog(head="npc_694_1",delay=1,style="other")]你呢，老家伙？
[dialog(head="npc_692_1",delay=1,style="self")]我？
[dialog(head="npc_694_1",delay=1,style="other")]老家伙，问你个问题吧。
[dialog(head="npc_694_1",delay=1,style="other")]今天的你，坐在这里看着时代变迁，感到力不从心。
[dialog(head="npc_694_1",delay=1,style="other")]但是过去呢，当你跟着西西里从拉特兰离开时，当你开始为这片土地制定规则时，你感觉如何？
[dialog(head="npc_692_1",delay=1,style="self")]在那一刻，我感到心潮澎湃。
[dialog(head="npc_694_1",delay=1,style="other")]彼时彼刻，恰如此时此刻。
[dialog(head="npc_694_1",delay=1,style="other")]我说过许多次了，老家伙。
[dialog(head="npc_694_1",delay=1,style="other")]我不喜欢你制定的规则，但这不意味着，我就会喜欢新的规则。
[dialog(head="npc_694_1",delay=1,style="other")]虚假的文明，自然不如发自内心的文明。
[dialog(head="npc_694_1",delay=1,style="other")]然而发自内心的，却总是瑰丽而又短暂的。
[dialog(head="npc_694_1",delay=1,style="other")]西西里很坚定，她会守着她的时代而死。
[dialog(head="npc_694_1",delay=1,style="other")]但你呢？
[dialog(head="npc_694_1",delay=1,style="other")]你想要的，并不是你的秩序牢不可破，而是证明“律法”也能被人创造，不是吗？
[dialog(head="npc_692_1",delay=1,style="self")]......是啊，我好奇究竟是什么东西让萨科塔能够在一个绝对平等的条件下共同生活。
[dialog(head="npc_692_1",delay=1,style="self")]而她，则渴望一种能让所有家族在同一张桌子上谈判的力量。
[dialog(head="npc_692_1",delay=1,style="self")]所以我们才会走到一起。
[dialog(head="npc_694_1",delay=1,style="other")]然而，当“铳与秩序”被实行的那一刻，你离开拉特兰的目的已经达成了。
[dialog(head="npc_694_1",delay=1,style="other")]让你守在这个国家几十年的，并不是她的时代，而是与她的承诺。
[dialog(head="npc_694_1",delay=1,style="other")]你已经守得够久了，老家伙。
[dialog(head="npc_692_1",delay=1,style="self")]怎么，你自己不打算走，就来劝我？
[dialog(head="npc_694_1",delay=1,style="other")]只是怕老人家老眼昏花，看不清前路而已。
[dialog(head="npc_692_1",delay=1,style="self")]......
```

### text_agenir_2_1_1

```
[dialog(head="npc_691_1",delay=1,style="other")]阿格尼尔。
[dialog(head="npc_692_3",delay=1,style="self")]......
[dialog(head="npc_691_1",delay=1,style="other")]老东西，又在这里装死。
[dialog(head="npc_692_3",delay=1,style="self")]Zzzz......Zzzz......
[dialog(head="npc_691_1",delay=1,style="other")]我同意你来这里进行你所谓的养老，可不是让你对这里发生的事袖手旁观。
[dialog(head="npc_691_1",delay=1,style="other")]即使现在结果还算可以接受，也不意味着我会轻易原谅你。
[dialog(head="npc_692_3",delay=1,style="self")]Zzzz......
[dialog(head="npc_691_1",delay=1,style="other")]阿格尼尔。
[dialog(head="npc_692_1",delay=1,style="self")]唉，大清早就发火，对身体不好。
[dialog(head="npc_691_1",delay=1,style="other")]回答我，你不会忘了，我让你来这里照顾一下谁了吧。


[OptionBranch(option0="option_Agenir_2_1_1_1",option1="option_Agenir_2_1_1_2",option2="option_Agenir_2_1_1_3",delay=2)]
```

### text_agenir_2_1_1_1

```
[dialog(head="npc_691_1",delay=1,style="other")]算你还没有老年痴呆。
[dialog(head="npc_692_1",delay=1,style="self")]所以我当时才邀请你一起来的，西西里。
[dialog(head="npc_692_1",delay=1,style="self")]有些事情，你必须坐在公园的长椅上才能看到。
[dialog(head="npc_692_1",delay=1,style="self")]我看到了一些有趣的东西，我想，你也应该看一看。
[dialog(head="npc_691_1",delay=1,style="other")]而有些事情，只有高坐在灰厅之中才能察觉。
[dialog(head="npc_691_1",delay=1,style="other")]我要听的不是这个，阿格尼尔。
[dialog(head="npc_692_1",delay=1,style="self")]好吧，这次确实做得过火了点。
[dialog(head="npc_692_1",delay=1,style="self")]我承认，我有不对的地方。
[dialog(head="npc_691_1",delay=1,style="other")]哼。
[dialog(head="npc_692_1",delay=1,style="self")]然后，到你了。
[dialog(head="npc_691_1",delay=1,style="other")]一副知道我接下来要做什么的口吻。
[dialog(head="npc_692_1",delay=1,style="self")]不然我也不会在这个时间，出现在这里。
[dialog(head="npc_691_1",delay=1,style="other")]唉，有个太了解自己的朋友，也不是什么好事。
[narration(delay=1)]西西里夫人笑了笑，走到阿格尼尔面前。
[narration(delay=1)]然后，叙拉古最为尊贵的存在，竟然缓缓跪下。
[narration(delay=1)]她的表情虔诚，像是一个信徒。
[dialog(head="npc_692_1",delay=1,style="self")]你在向谁祈求原谅。
[dialog(head="npc_691_1",delay=1,style="other")]向铳与秩序。
[dialog(head="npc_692_1",delay=1,style="self")]你犯了什么过错？
[dialog(head="npc_691_1",delay=1,style="other")]我接受了一个年轻人的挑战。
[dialog(head="npc_691_1",delay=1,style="other")]而他的目标，是摧毁我所建立的一切。
[dialog(head="npc_692_1",delay=1,style="self")]你认为这是对铳与秩序的背叛？
[dialog(head="npc_691_1",delay=1,style="other")]是的。
[dialog(head="npc_692_1",delay=1,style="self")]那你为何不将它扼杀在摇篮之中？
[dialog(head="npc_691_1",delay=1,style="other")]贝纳尔多的方法超出了规则的允许，我不会容忍。但莱昂图索，他选择了坐在我的面前，冒着死亡的风险，提出他的想法。
[dialog(head="npc_691_1",delay=1,style="other")]我决定给他一个机会。
[dialog(head="npc_692_1",delay=1,style="self")]不，这不是真正的理由。
[dialog(head="npc_691_1",delay=1,style="other")]......我对他说，叙拉古将在我活着的时候辉煌，并将随着我的死亡而衰落。
[dialog(head="npc_692_1",delay=1,style="self")]你不相信你所缔造的铳与秩序能够继续存在？
[dialog(head="npc_691_1",delay=1,style="other")]我对于继承人的种种培养，只告诉了我一件事：和平的时代，无法诞生下一个西西里夫人。
[dialog(head="npc_691_1",delay=1,style="other")]当我想要让所有家族臣服于我的脚下时，我的心中只有野心与激情。
[dialog(head="npc_691_1",delay=1,style="other")]而当我管理这个国家直到今天，我却难免对叙拉古这三个字产生情感。
[dialog(head="npc_691_1",delay=1,style="other")]我会尽我所能地击溃他。
[dialog(head="npc_691_1",delay=1,style="other")]但如果，他最后真的能够成功......
[dialog(head="npc_691_1",delay=1,style="other")]那就让他成功吧。
[dialog(head="npc_692_1",delay=1,style="self")]代表铳与秩序，你的所作所为将会得到谅解。
[narration(delay=1)]西西里夫人缓缓站起，她的表情也恢复如常，仿佛刚才发生的一切都与她无关。
[dialog(head="npc_692_1",delay=1,style="self")]你有多久没有这样向我告解了？
[dialog(head="npc_691_1",delay=1,style="other")]忘了。
[dialog(head="npc_692_1",delay=1,style="self")]感觉如何？
[dialog(head="npc_691_1",delay=1,style="other")]感觉更糟了。
[dialog(head="npc_692_1",delay=1,style="self")]对自己诚实可不是一件简单的事。
[dialog(head="npc_691_1",delay=1,style="other")]......阿格尼尔，你觉得，你失败了吗？
[dialog(head="npc_692_1",delay=1,style="self")]你呢，你觉得，你成功了吗？
[dialog(head="npc_691_1",delay=1,style="other")]当我去思考这个问题时，我发现，真正的问题在于，做到什么地步才算成功，让这个国家延续多久才算成功？
[dialog(head="npc_692_1",delay=1,style="self")]或许，只有在我们让所有家族都坐上同一张桌子的那个瞬间，我们是成功的。
[dialog(head="npc_691_1",delay=1,style="other")]你想说，我们打造的这个叙拉古，并不成功。
[dialog(head="npc_692_1",delay=1,style="self")]谁知道呢，有的时候，比别人少错一些，就算成功。
[dialog(head="npc_691_1",delay=1,style="other")]照你这么说，我错的，应当确实比其他人少一些。
[dialog(head="npc_691_1",delay=1,style="other")]毕竟，我有你这面镜子在。
[dialog(head="npc_692_1",delay=1,style="self")]......唉，遇人不淑啊。
```


> 本章节共138个脚本文件，此处展示前30个。

## 统计

- 总字符数：635567
- 对话行数：5541


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
